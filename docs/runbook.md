# MediLink Production Support Runbook

## Support rota
One person handles production-support requests each working day so the others can stay on planned work. The rota covers the 3-day cycle and would rotate again in the next one.

| Day | Primary | Backup |
|---|---|---|
| Day 1 | Alexa | Nikitas |
| Day 2 | Nicolas | Zain |
| Day 3 | Zain | Alexa |

## Common problems

### 1. Reminder not sent, or sent when it should not be
- Check: the appointment's status (booked or cancelled) and whether a reminder is still queued for it.
- Escalate: to the primary on support; if unresolved after one working day, switch to a call.

### 2. A booked slot still appears available
- Check: the booking record for that slot and time.
- Escalate: open a defect issue and assign it to the primary on support.

### 3. Admin schedule page is slow or unavailable
- Check: note the time, the clinic, and what the staff member was doing.
- Escalate: open a technical issue; switch to a call if clinics cannot work.

## After any incident
Open an issue, record what happened, and hold a short blameless review: what happened, why, and what we change.
