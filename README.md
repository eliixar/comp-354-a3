# MediLink Release Cycle
Team 25: simulated release cycle for the MediLink appointment platform.

## Team
| Name | Role |
|---|---|
| Alexa Rokakis | Engineering Manager / Team Lead |
| Nikitas Vourtzoumis | Developer 1 |
| Nicolas Nahas | Developer 2 |
| Zain Yehia | Developer 3 |

## Links
- Project board: [[link]](https://github.com/users/eliixar/projects/5)
- Daily updates:  [[link]](https://github.com/eliixar/comp-354-a3/issues/11)
- Definition of Done: DEFINITION_OF_DONE.md 
- Working agreement: WORKING_AGREEMENT.md 

## Running the tests
The tests cover booking (including double-booking attempts), cancellation, and reminders. You need Python 3.9 or newer.

```bash
pip install pytest
pytest -v
```

Run them from the repository root. CI runs the same command on every pull request (see `.github/workflows/tests.yml`), and a PR should only be merged once that check passes.
