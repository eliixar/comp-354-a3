from datetime import datetime
from booking import book_appointment
from cancellation import create_cancel_link, confirm_cancellation


SLOT = datetime(2026, 11, 2, 10, 0)


def test_booking_creates_booked_appointment():
    appointments = []
    appointment = book_appointment(appointments, "Alice", "Dental Pro", SLOT)

    assert appointment is not None
    assert appointment["status"] == "booked"
    assert appointment["clinic"] == "Dental Pro"
    assert appointment["start"] == SLOT
    assert appointments == [appointment]


def test_each_booking_gets_its_own_id():
    appointments = []
    first = book_appointment(appointments, "Alice", "Dental Pro", SLOT)
    second = book_appointment(appointments, "Bob", "Dental Pro", datetime(2026, 11, 2, 11, 0))

    assert first["id"] != second["id"]


def test_double_booking_same_slot_is_rejected():
    appointments = []
    book_appointment(appointments, "Alice", "Dental Pro", SLOT)

    assert book_appointment(appointments, "Bob", "Dental Pro", SLOT) is None
    # The original booking is kept and nothing extra was added
    assert len(appointments) == 1
    assert appointments[0]["patient"] == "Alice"


def test_same_time_at_another_clinic_is_not_a_double_booking():
    appointments = []
    book_appointment(appointments, "Alice", "Dental Pro", SLOT)

    assert book_appointment(appointments, "Bob", "Smile Clinic", SLOT) is not None
    assert len(appointments) == 2


def test_cancelled_slot_can_be_booked_again():
    appointments = []
    original = book_appointment(appointments, "Alice", "Dental Pro", SLOT)
    token = create_cancel_link(original).rsplit("/", 1)[1]
    confirm_cancellation(appointments, token)

    rebooked = book_appointment(appointments, "Bob", "Dental Pro", SLOT)
    assert rebooked is not None
    assert rebooked["id"] != original["id"]
    assert original["status"] == "cancelled"
