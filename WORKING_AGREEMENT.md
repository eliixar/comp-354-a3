# Working Agreement

## Workflow
Backlog → Ready → In Progress → Code Review → Verification → Done
- An item enters Ready only with acceptance criteria, a priority, and an owner.
- Nobody verifies their own work.

## WIP limits
- In Progress: 3 items for the whole team
- Code Review: 3 items
- Verification: 2 items
- Rule: when a PR is waiting for review, review it before starting new work.

## Why these limits
Three developers do most of the implementation, and the manager takes only small
items. One active item per developer keeps context switching low. The
Code Review and Verification limits stop work piling up in the stages where the
previous release showed waiting (PRs left open for days, verification missed).

## Communication
Asynchronous by default: daily updates, PR comments, issue comments.
Switch to a call when:
1. A blocker is unresolved after one working day
2. A production incident (P1) occurs
3. Two people disagree about requirements or acceptance criteria

## Daily update format (posted in the Daily Updates thread)
Completed (issue #) | Planned (issue #) | Blockers / help needed
