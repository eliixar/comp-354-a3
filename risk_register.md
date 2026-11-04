
# MediLink Risk Register

| # | Risk | Category | Warning signal | Potential consequence | Likelihood | Impact | Preventive action | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | pytest upgrade (#6) breaks tests | Technical dependency | Tests fail or aren’t found after upgrade | Test results can’t be trusted | Very Low | Medium | Read changes, have a rollback to undo updates, and test everything before and after. | Zain (Dev 3) |
| 2 | Items wait for a reviewer or verifier next release | Teamwork / workflow | The verifier wasn't appointed in advance in our cycle. #1 waited way too long for one | Items are blocked before done | Medium | Medium | When an item enters the ready box, someone should be assigned to review it and to verify it. The manager checks every day. | Alexa manager |
| 3 | Support schedule is not updated for the next cycle | Maintenance / production support | No schedule for the next 3 days | Developers might get interrupted by support request | Medium | Medium | Create a new support schedule before each cycle | Alexa<br>manager |
| 4 | Time zone bug because reminders do not use fixed time zone code | Defect/ Quality | reminders.py still subtracts 24h directly instead of using reminder_send_time | Patients see the wrong reminder time after a clock change | Medium | High | Make reminders call the shared time zone functions | Nikitas Dev 1 |
