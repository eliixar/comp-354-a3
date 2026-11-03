from datetime import timedelta, timezone
from zoneinfo import ZoneInfo


# Appointment start times must carry a time zone (we store them in UTC).
# A naive datetime has no zone, so we can't tell what time it really is.
def _require_aware(start):
    if start.tzinfo is None or start.utcoffset() is None:
        raise ValueError("start time must include a time zone")


# Test 1: the reminder shows the time in the clinic's local time zone
def clinic_local_time(start, clinic_timezone):
    _require_aware(start)
    return start.astimezone(ZoneInfo(clinic_timezone))


def format_reminder_time(start, clinic_timezone):
    local = clinic_local_time(start, clinic_timezone)
    return {
        "date": local.strftime("%Y-%m-%d"),
        "time": local.strftime("%H:%M"),
        "zone": local.strftime("%Z"),
    }


# Test 2: across a daylight-saving change the reminder is still exactly
# 24 hours before the appointment. We subtract in UTC because subtracting
# from a local time keeps the wall clock and can be off by an hour.
def reminder_send_time(start):
    _require_aware(start)
    return start.astimezone(timezone.utc) - timedelta(hours=24)
