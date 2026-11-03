from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest

from reminder_time import clinic_local_time, format_reminder_time, reminder_send_time


TORONTO = "America/Toronto"
HALIFAX = "America/Halifax"


def utc(year, month, day, hour, minute=0):
    return datetime(year, month, day, hour, minute, tzinfo=timezone.utc)


# Test 1: reminder time matches the clinic's local time, not UTC
def test_reminder_shows_clinic_local_time():
    start = utc(2026, 11, 2, 15, 0)

    shown = format_reminder_time(start, TORONTO)
    assert shown == {"date": "2026-11-02", "time": "10:00", "zone": "EST"}


# Test 3: the same appointment instant shown for clinics in two time zones
def test_two_time_zones():
    start = utc(2026, 11, 2, 15, 0)

    assert format_reminder_time(start, TORONTO)["time"] == "10:00"
    assert format_reminder_time(start, HALIFAX)["time"] == "11:00"
    assert format_reminder_time(start, HALIFAX)["zone"] == "AST"


def test_time_zone_can_change_the_date():
    # 02:00 UTC on Nov 3 is still the evening of Nov 2 at both clinics
    start = utc(2026, 11, 3, 2, 0)

    assert format_reminder_time(start, TORONTO) == {"date": "2026-11-02", "time": "21:00", "zone": "EST"}
    assert format_reminder_time(start, HALIFAX) == {"date": "2026-11-02", "time": "22:00", "zone": "AST"}


# Test 2: daylight saving ends Nov 1, 2026 at 2:00 in Toronto and Halifax
def test_local_time_correct_on_both_sides_of_dst_change():
    before = utc(2026, 10, 31, 14, 0)  # 10:00 EDT (UTC-4)
    after = utc(2026, 11, 2, 15, 0)    # 10:00 EST (UTC-5)

    assert format_reminder_time(before, TORONTO) == {"date": "2026-10-31", "time": "10:00", "zone": "EDT"}
    assert format_reminder_time(after, TORONTO) == {"date": "2026-11-02", "time": "10:00", "zone": "EST"}


@pytest.mark.parametrize("clinic_timezone", [TORONTO, HALIFAX])
def test_send_time_is_24_hours_before_across_dst_change(clinic_timezone):
    # Appointment at 10:00 local on Nov 1, the day the clocks go back
    start = datetime(2026, 11, 1, 10, 0, tzinfo=ZoneInfo(clinic_timezone))

    send_at = reminder_send_time(start)
    assert start - send_at == timedelta(hours=24)
    # The local clock went back an hour overnight, so the reminder goes out
    # at 11:00 the day before, not 10:00 (that would be 25 hours early)
    assert clinic_local_time(send_at, clinic_timezone).strftime("%Y-%m-%d %H:%M") == "2026-10-31 11:00"


def test_send_time_is_24_hours_before_when_dst_starts():
    # Clocks go forward Mar 8, 2026 at 2:00, so the reminder for 10:00 that
    # day goes out at 09:00 the day before (10:00 would be only 23 hours early)
    start = datetime(2026, 3, 8, 10, 0, tzinfo=ZoneInfo(TORONTO))

    send_at = reminder_send_time(start)
    assert start - send_at == timedelta(hours=24)
    assert clinic_local_time(send_at, TORONTO).strftime("%Y-%m-%d %H:%M") == "2026-03-07 09:00"


def test_start_without_time_zone_is_rejected():
    with pytest.raises(ValueError):
        format_reminder_time(datetime(2026, 11, 2, 10, 0), TORONTO)
    with pytest.raises(ValueError):
        reminder_send_time(datetime(2026, 11, 2, 10, 0))
