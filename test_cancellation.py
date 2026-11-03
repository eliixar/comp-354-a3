from datetime import datetime
from cancellation import (
    create_cancel_link,
    open_cancel_page,
    is_slot_available,
    confirm_cancellation,
)


# Two fake booked appointments so we can check the link only reaches its own one
def make_appointments():
    return [
        {"id": 1, "clinic": "Dental Pro", "start": datetime(2026, 11, 2, 10, 0), "status": "booked"},
        {"id": 2, "clinic": "Dental Pro", "start": datetime(2026, 11, 2, 11, 0), "status": "booked"},
    ]


def token_from(link):
    return link.rsplit("/", 1)[1]


def test_link_opens_page_for_that_appointment_only():
    appointments = make_appointments()
    link_1 = create_cancel_link(appointments[0])
    link_2 = create_cancel_link(appointments[1])

    assert link_1 != link_2
    assert open_cancel_page(appointments, token_from(link_1))["appointment_id"] == 1
    assert open_cancel_page(appointments, token_from(link_2))["appointment_id"] == 2
    assert open_cancel_page(appointments, "made-up-token") is None


def test_confirming_frees_slot_immediately():
    appointments = make_appointments()
    token = token_from(create_cancel_link(appointments[0]))
    slot = datetime(2026, 11, 2, 10, 0)

    assert is_slot_available(appointments, "Dental Pro", slot) == False
    confirm_cancellation(appointments, token)
    assert is_slot_available(appointments, "Dental Pro", slot) == True
    # The other appointment is untouched
    assert appointments[1]["status"] == "booked"


def test_patient_sees_confirmation_message():
    appointments = make_appointments()
    token = token_from(create_cancel_link(appointments[0]))

    message = confirm_cancellation(appointments, token)
    assert "cancelled" in message
    assert "Dental Pro" in message
    assert "2026-11-02" in message
    assert "10:00" in message

    assert confirm_cancellation(appointments, token) == "This appointment was already cancelled."
    assert confirm_cancellation(appointments, "made-up-token") == "This cancellation link is not valid."
