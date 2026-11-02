from datetime import timedelta


# Test 1: a reminder is scheduled when an appointment is booked
def schedule_reminder(appointment):
    send_time = appointment["start"] - timedelta(hours=24)
    return {"appointment_id": appointment["id"], "send_at": send_time}


# Test 2: it is sent 24 hours (+ or - 5 minutes) before the start time
def is_time_to_send(send_at, now):
    difference = abs(now - send_at)
    return difference <= timedelta(minutes=5)


# Test 3: it includes clinic name, date, time, and a cancel link
def build_message(appointment):
    clinic = appointment["clinic"]
    date = appointment["start"].strftime("%Y-%m-%d")
    time = appointment["start"].strftime("%H:%M")
    link = appointment["cancel_link"]
    return f"Reminder from {clinic}: your appointment is on {date} at {time}. Cancel here: {link}"
