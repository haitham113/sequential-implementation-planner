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
