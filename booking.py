from cancellation import is_slot_available


# Books a slot only if nobody else holds it. Returns the new appointment,
# or None when the slot is already booked (double-booking attempt)
def book_appointment(appointments, patient, clinic, start):
    if not is_slot_available(appointments, clinic, start):
        return None

    next_id = max((a["id"] for a in appointments), default=0) + 1
    appointment = {
        "id": next_id,
        "patient": patient,
        "clinic": clinic,
        "start": start,
        "status": "booked",
    }
    appointments.append(appointment)
    return appointment
