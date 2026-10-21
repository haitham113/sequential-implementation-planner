# Status Tracking and Roll-Up

Generated playbooks use durable execution status so a later session can see exactly what has run and whether a milestone may advance.

## Canonical status flags

Use exactly one of these flags at the end of every generated milestone and prompt heading:

- `[🟢 COMPLETE]`
- `[🟡 IN PROGRESS]`
- `[🔴 BLOCKED]`
- `[⚪ NOT STARTED]`

Do not invent additional colors, emojis, or labels.

Examples:

```markdown
# Milestone 2 — Booking concurrency [🟡 IN PROGRESS]
## Prompt 2A — Verify concurrent booking behavior [⚪ NOT STARTED]
```

## What prompt status means

Prompt status records **execution of that prompt**, not whether the milestone gate passed.

- `[⚪ NOT STARTED]`: the prompt has not been run.
- `[🟡 IN PROGRESS]`: execution has started but has not reached a terminal prompt result.
- `[🔴 BLOCKED]`: the prompt itself cannot reach its defined stopping point because a prerequisite, required input, access, environment, or other external blocker is missing.
- `[🟢 COMPLETE]`: the prompt reached its defined stopping point and recorded its actual result.

A verification prompt may therefore be `[🟢 COMPLETE]` while reporting `FAIL` or `NOT VERIFIED`. The verification attempt finished; the milestone remains incomplete because its gate is not satisfied.

A focused review may be `[🟢 COMPLETE]` even when it reports Critical or High findings. The review finished; the milestone remains incomplete until accepted findings are resolved and the gate is satisfied.

## Prompt lifecycle

For every generated prompt:

1. When execution begins, change only that prompt heading from `[⚪ NOT STARTED]` to `[🟡 IN PROGRESS]` unless it already has a terminal status.
2. Perform the prompt's work.
3. Before ending, set the prompt heading to its actual terminal status:
   - `[🟢 COMPLETE]` when the prompt reached its defined stopping point and recorded the result;
   - `[🔴 BLOCKED]` when it cannot reach that stopping point because of a real blocker;
   - leave `[🟡 IN PROGRESS]` only when execution is intentionally interrupted before a terminal result.
4. If the prompt belongs to a milestone, recompute the parent milestone and synchronize the Milestone Gates table before ending.
5. If the prompt is a standalone final check with no parent milestone, update only its own heading.

## Milestone roll-up algorithm

After any child prompt changes status, inspect **every child prompt heading in the current milestone** and recompute the milestone:

1. `[⚪ NOT STARTED]` only when every child prompt is `[⚪ NOT STARTED]`.
2. `[🟢 COMPLETE]` only when:
   - every required child prompt is `[🟢 COMPLETE]`; and
   - the milestone gate is satisfied by observed evidence.
3. A gate is satisfied by `PASS`, or by an explicit owner acceptance of a non-spec-breaking limitation when the playbook allows that exception and records the acceptance as gate evidence.
4. `[🔴 BLOCKED]` when a required child is blocked or the gate cannot currently be pursued because of a real external blocker and there is no runnable in-milestone step that can resolve it.
5. `[🟡 IN PROGRESS]` in all other cases, including:
   - some children complete while others are not started;
   - all children are complete but the gate reports `FAIL` or `NOT VERIFIED`;
   - accepted review findings still require fixes/revalidation;
   - verification completed but the milestone gate is not yet satisfied.

Never mark a milestone COMPLETE solely because its implementation prompt completed.

## Milestone Gates table synchronization

The generated Milestone Gates table must contain a `Status` column.

The status cell must exactly match the corresponding milestone heading flag. After recomputing a milestone, update both locations in the same bookkeeping edit.

Example:

```markdown
| Milestone | Status | Gate before continuing |
| --- | --- | --- |
| 2. Booking concurrency | [🟡 IN PROGRESS] | Concurrent attempts prove no overlapping bookings... |
```

## Read-only prompt exception

Verification, review, audit, and other read-only prompts must still say they modify no implementation/code/configuration.

They must also state:

> Status bookkeeping exception: you may edit only this playbook's status flags and the matching Milestone Gates status cell as required by the status reconciliation rules. Do not make any other file or implementation changes.

This is the sole permitted mutation for a read-only prompt.

## Fix prompt completion

A fix/revalidation prompt is `[🟢 COMPLETE]` when either:

1. all owner-accepted findings assigned to that fix prompt are fixed and the required revalidation has been executed and recorded; or
2. the completed review explicitly records that no changes are required, and the fix prompt records that fact without making implementation changes.

A fix prompt is not complete merely because code was edited.

## Verification outcomes vs. status

Keep result vocabulary separate from heading status:

- verification result: `PASS`, `FAIL`, `NOT VERIFIED`;
- execution status: one of the four canonical heading flags.

`FAIL` or `NOT VERIFIED` may coexist with a COMPLETE verification prompt, but the milestone remains incomplete unless its gate is otherwise explicitly satisfied under the allowed limitation rule.

## Required status footer for generated prompts

Every generated milestone child prompt must end with a project-specific version of:

> **Status reconciliation (required):** Before ending, update this prompt heading to reflect the actual execution state. Then inspect every sibling prompt in this milestone, recompute the parent milestone using the status roll-up rules, and synchronize the matching `Milestone Gates` Status cell. The milestone is COMPLETE only when every required child prompt is COMPLETE and its gate is satisfied. This status-bookkeeping edit is permitted even when this prompt is otherwise read-only.

Every standalone final prompt must end with:

> **Status update (required):** Before ending, update this prompt heading to reflect the actual execution state. This prompt has no parent milestone, so do not roll up a milestone or edit unrelated status cells.
