from datetime import datetime, timedelta
from reminders import schedule_reminder, is_time_to_send, build_message

# A fake appointment we use for all the tests
appointment = {
    "id": 1,
    "clinic": "Dental Pro",
    "start": datetime(2026, 11, 2, 10, 0),
    "cancel_link": "[test_empty]",
}

def test_reminder_is_scheduled():
    reminder = schedule_reminder(appointment)
    # Example: 24 hours before Nov 2 at 10:00 is Nov 1 at 10:00
    assert reminder["send_at"] == datetime(2026, 11, 1, 10, 0)

def test_sent_within_5_minutes():
    send_at = datetime(2026, 11, 1, 10, 0)
    assert is_time_to_send(send_at, send_at + timedelta(minutes=4)) == True
    assert is_time_to_send(send_at, send_at + timedelta(minutes=6)) == False


def test_message_has_everything():
    message = build_message(appointment)
    assert "Dental Pro" in message
    assert "2026-11-02" in message
    assert "10:00" in message
    assert "[test_empty]" in message
