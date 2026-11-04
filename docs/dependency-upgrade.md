# Dependency upgrade: pytest (#6)

- Current version: 8.3.4
- New version: 9.2.0 (latest version)

## Breaking changes found
Read the pytest changelog: https://docs.pytest.org/en/stable/changelog.html

There were no changes that can break our current tests. 

## Rollback
run `pip install pytest==8.3.4` and restore the previous `requirements.txt` file

## Test results before and after upgrade:
Before upgrade (pytest 8.3.4):
```
================================================================================= test session starts ==================================================================================
platform linux -- Python 3.14.3, pytest-8.3.4
...
collected 3 items

test_cancellation.py::test_link_opens_page_for_that_appointment_only PASSED                                                                                                      [ 33%]
test_cancellation.py::test_confirming_frees_slot_immediately PASSED                                                                                                              [ 66%]
test_cancellation.py::test_patient_sees_confirmation_message PASSED                                                                                                              [100%]

================================================================================== 3 passed in 0.01s ===================================================================================
```

After upgrade (pytest 9.2.0):
```
================================================================================= test session starts ==================================================================================
...
platform linux -- Python 3.14.3, pytest-9.2.0
...
collected 3 items

test_cancellation.py::test_link_opens_page_for_that_appointment_only PASSED                                                                                                      [ 33%]
test_cancellation.py::test_confirming_frees_slot_immediately PASSED                                                                                                              [ 66%]
test_cancellation.py::test_patient_sees_confirmation_message PASSED                                                                                                              [100%]

================================================================================== 3 passed in 0.01s ===================================================================================
```

Result: all 3 tests pass on both versions.