# Quality Gates and Regression Discipline

## Gate design

A milestone gate must describe observed behavior, not artifact presence.

Weak:
- "Authentication implemented."
- "Migration completed."
- "UI built."

Strong:
- "Login, refresh rotation, logout, and replay rejection pass real integration/e2e checks, sensitive values are absent from logs, and existing public endpoints remain unaffected."
- "Migration completes on a production-like copy, invariant counts reconcile, rollback/restore is rehearsed where supported, and the upgraded application passes critical workflows."

A good gate usually proves:
1. intended behavior;
2. critical negative behavior;
3. relevant security/data-integrity invariant;
4. required environment compatibility;
5. regression safety.

## Gate status and milestone roll-up

Prompt execution status and gate outcome are separate.

A milestone may be `[🟢 COMPLETE]` only when:
- every required child prompt is `[🟢 COMPLETE]`; and
- the gate is satisfied by observed evidence.

A gate may be treated as satisfied by `PASS`, or by an explicit owner acceptance of a non-spec-breaking limitation when the generated playbook allows that exception and records the acceptance.

If verification returns `FAIL` or `NOT VERIFIED`, the verification prompt may still be COMPLETE, but the milestone must remain incomplete unless the gate is later satisfied under the rule above.

After any child prompt updates status, apply `references/status-tracking.md` and synchronize the milestone heading with the Milestone Gates Status cell.

## Regression discipline

From the second milestone onward:
- identify prior critical paths affected by the new change;
- re-run those checks after implementation and after fixes;
- do not let a later milestone invalidate an earlier gate silently.

Maintain a small set of named critical paths when useful, such as:
- auth lifecycle;
- tenant isolation;
- booking transaction;
- payment webhook replay;
- browser start/stop lifecycle;
- migration data reconciliation;
- primary end-user golden path.

## Truthful evidence states

Use exactly:
- `PASS` — executed/observed evidence satisfies the requirement;
- `FAIL` — executed/observed evidence violates it;
- `NOT VERIFIED` — proof could not be executed or observed.

`NOT VERIFIED` is not failure, but it cannot be treated as pass.

These are evidence/result states, not the four heading status flags.

## Final readiness

Final readiness should aggregate the project's real acceptance target:
- merge readiness;
- production release;
- deployment;
- client delivery;
- migration cutover;
- challenge submission;
- public portfolio publication.

End with one unambiguous verdict appropriate to the target, e.g. `READY FOR RELEASE` / `NOT READY FOR RELEASE`.

A standalone final-readiness prompt updates only its own heading status. Its heading may be `[🟢 COMPLETE]` even when the readiness verdict is `NOT READY FOR RELEASE`, because execution status records whether the check ran to completion, not whether the product passed.
