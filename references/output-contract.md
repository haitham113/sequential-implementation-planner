# Output Contract

Generate one project-specific Markdown execution manual. Adapt names (`Phase` vs `Milestone`) to the project, but preserve the status rules from `references/status-tracking.md`.

## Required top-level structure

```markdown
# <Project/Feature> — Sequential Implementation and Review Prompt Pack

Use this file together with:
- <authoritative specification>
- <repository rules, if any>

<source-of-truth precedence statement>

## Working Method
...

## Global Rules
...

## Milestone Gates
| Milestone | Status | Gate before continuing |
| --- | --- | --- |
| 0. Plan | [⚪ NOT STARTED] | ... |
...

# Milestone 0 — Plan [⚪ NOT STARTED]

## Prompt 0 — Repository Assessment and Implementation Plan [⚪ NOT STARTED]
```text
...
```

## Prompt 0A — Challenge the Plan [⚪ NOT STARTED]
```text
...
```

# Milestone 1 — <Name> [⚪ NOT STARTED]

## Prompt 1 — Implement [⚪ NOT STARTED]
```text
...
```
## Prompt 1A — Verify [⚪ NOT STARTED]
```text
...
```
## Prompt 1B — <Focused Review> [⚪ NOT STARTED]
```text
...
```
## Prompt 1C — Fix and Revalidate [⚪ NOT STARTED]
```text
...
```
...

# Final Readiness Check [⚪ NOT STARTED]
```text
...
```
```

Every generated milestone and prompt heading must contain exactly one canonical status flag from `references/status-tracking.md`: `[🟢 COMPLETE]`, `[🟡 IN PROGRESS]`, `[🔴 BLOCKED]`, or `[⚪ NOT STARTED]`. Every executable agent prompt must be fenced as `text`.

## Working Method content

The generated document should instruct the operator to:
1. start one prompt and set that prompt heading to `[🟡 IN PROGRESS]`;
2. perform the prompt and record actual evidence/results;
3. before ending, update that prompt to its terminal execution status;
4. for milestone child prompts, inspect every sibling prompt, recompute the parent milestone, and synchronize the Milestone Gates Status cell;
5. run verification without modifying implementation code;
6. run focused review(s) without modifying implementation code;
7. decide which findings are justified;
8. run the fix prompt for approved findings only;
9. re-run validation and the milestone gate;
10. commit verified work;
11. continue only after the milestone is `[🟢 COMPLETE]`.

State that a failed gate remains unsatisfied until fixed or explicitly accepted by the owner as a non-spec-breaking limitation where the playbook permits that exception. A prompt may be COMPLETE even when its verification result is `FAIL` or `NOT VERIFIED`; this never makes the parent milestone complete by itself.

## Global Rules content

Adapt these rules to the project:
- read authoritative docs before acting;
- inspect existing code before editing;
- preserve unrelated working behavior;
- keep changes scoped to the current milestone;
- do not implement future milestones early;
- use the declared stack and repository conventions;
- do not expose secrets/sensitive data;
- do not silently change product behavior;
- run real checks and report actual results;
- use `NOT VERIFIED` for blocked proof;
- keep prompt/milestone status durable and synchronized;
- never mark a milestone COMPLETE unless all required children are COMPLETE and its gate is satisfied;
- treat status reconciliation as the only permitted playbook edit inside otherwise read-only prompts;
- update affected docs;
- after implementation/fixes report files changed, decisions, commands, actual results, limitations, remaining risks, docs, and suggested Conventional Commit.

## Mandatory status instruction

Every prompt family below must explicitly include the appropriate required status footer from `references/status-tracking.md`.

For milestone child prompts, the footer must require:
- updating the prompt's own heading status;
- inspecting every sibling prompt in the current milestone;
- recomputing the parent milestone;
- synchronizing the Milestone Gates Status cell;
- enforcing that milestone COMPLETE requires every required child prompt to be COMPLETE plus a satisfied gate.

For standalone final checks that do not belong to a milestone, require only self-status update.

## Prompt 0 contract

Prompt 0 belongs to Milestone 0 and must:
- modify no implementation code;
- inspect all authoritative context;
- propose the full milestone order;
- identify existing code to reuse;
- identify modules/files/data/API/state/infrastructure implications as applicable;
- identify tests, real-environment checks, security/privacy/data-integrity/performance concerns as applicable;
- identify risks, documentation, and meaningful commit boundaries;
- surface contradictions, missing prerequisites, unclear requirements, unnecessary complexity, and weak build order;
- recommend the smallest production-quality choice;
- stop after the plan;
- perform required status reconciliation for itself and Milestone 0.

## Prompt 0A contract

Prompt 0A belongs to Milestone 0. Choose 2–4 relevant reviewer personas. Challenge:
- sequencing;
- dependency assumptions;
- premature abstraction;
- unnecessary infrastructure;
- untested risky capabilities;
- missing failure handling;
- weak security/data integrity;
- regression gaps;
- scope that should be deferred.

Return:
1. Critical changes
2. Recommended changes
3. Optional improvements
4. Scope to cut/defer first
5. Final recommended order

Modify no implementation code. Perform required status reconciliation before ending.

## Implementation prompt contract

Every implementation prompt should include:
- authoritative files to read;
- existing implementation to inspect;
- current milestone scope;
- concrete implementation requirements;
- mandatory invariants;
- explicit exclusions;
- tests to add;
- commands/flows to actually run;
- documentation updates;
- milestone gate;
- "Stop after this milestone.";
- required status reconciliation before ending.

## Verification prompt contract

Verification prompts:
- modify no implementation code/configuration/data except when the verification procedure itself necessarily exercises the system;
- permit only the playbook status-bookkeeping edit outside those test effects;
- execute relevant checks;
- test behavior, not merely code shape;
- include negative cases;
- use real runtime/database/browser/network/integration resources where material;
- return `PASS`, `FAIL`, or `NOT VERIFIED` plus evidence;
- may be marked `[🟢 COMPLETE]` after faithfully recording `FAIL` or `NOT VERIFIED`;
- never say something merely "should work";
- perform required status reconciliation before ending.

## Focused review contract

Review prompts:
- modify no implementation code/configuration;
- permit only the playbook status-bookkeeping edit;
- adopt a relevant skeptical specialist role;
- attempt realistic failure/abuse cases;
- inspect both implementation and observed behavior where appropriate;
- classify findings `Critical`, `High`, `Medium`, `Low`;
- include evidence, impact, affected path when possible, and smallest correct fix;
- perform required status reconciliation before ending.

## Fix/revalidate contract

Fix prompts:
- fix approved findings only;
- remain within current milestone;
- do not add future features;
- re-run all relevant validation and regressions;
- report actual results;
- are COMPLETE only when accepted findings are fixed and revalidated, or when the completed review explicitly records that no changes are required and the fix prompt records that fact;
- do not make the parent milestone COMPLETE while unresolved Critical/High issues violate the gate;
- perform required status reconciliation before ending.

## Final prompt families

Include only when applicable:
- final production/portfolio/release polish;
- final golden-path or critical-transaction rehearsal;
- final architecture/security/quality audit;
- final fix;
- clean-clone/clean-environment verification;
- public repository/release safety check;
- final readiness check tied to Definition of Done or acceptance criteria.

If a final prompt belongs to a named final milestone, use normal child-to-parent roll-up. If it is standalone, it must update only its own heading status before ending.

Read-only final audits/verifications permit only status bookkeeping edits to the playbook.

The final readiness table should use:

| Requirement | Evidence | Status | Required Action |
| --- | --- | --- | --- |

with result status limited to `PASS`, `FAIL`, `NOT VERIFIED`. This readiness result column is distinct from the prompt heading execution-status flag.
