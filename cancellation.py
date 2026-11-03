import secrets


BASE_URL = "https://medilink.example/cancel"


# Each appointment gets its own random token, so the link can't be guessed
# and only ever points at that one appointment
def create_cancel_link(appointment):
    appointment["cancel_token"] = secrets.token_urlsafe(16)
    return f"{BASE_URL}/{appointment['cancel_token']}"


def find_by_token(appointments, token):
    for appointment in appointments:
        if appointment.get("cancel_token") == token:
            return appointment
    return None


# Test 1: the link opens a cancel page for that appointment only
def open_cancel_page(appointments, token):
    appointment = find_by_token(appointments, token)
    if appointment is None:
        return None
    return {
        "appointment_id": appointment["id"],
        "clinic": appointment["clinic"],
        "date": appointment["start"].strftime("%Y-%m-%d"),
        "time": appointment["start"].strftime("%H:%M"),
    }


# Test 2: confirming the cancellation frees the slot immediately
def is_slot_available(appointments, clinic, start):
    for appointment in appointments:
        if (appointment["clinic"] == clinic
                and appointment["start"] == start
                and appointment["status"] == "booked"):
            return False
    return True


# Test 3: the patient sees a cancellation confirmation message
def confirm_cancellation(appointments, token):
    appointment = find_by_token(appointments, token)
    if appointment is None:
        return "This cancellation link is not valid."
    if appointment["status"] == "cancelled":
        return "This appointment was already cancelled."

    appointment["status"] = "cancelled"
    date = appointment["start"].strftime("%Y-%m-%d")
    time = appointment["start"].strftime("%H:%M")
    return f"Your appointment at {appointment['clinic']} on {date} at {time} has been cancelled."
