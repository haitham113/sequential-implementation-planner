# Output Contract

Generate one project-specific Markdown execution manual. Adapt names (`Phase` vs `Milestone`) to the project.

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
| Milestone | Gate before continuing |
| --- | --- |
| 0. Plan | ... |
...

# Prompt 0 — Repository Assessment and Implementation Plan
```text
...
```

# Prompt 0A — Challenge the Plan
```text
...
```

# Milestone 1 — <Name>
## Prompt 1 — Implement
```text
...
```
## Prompt 1A — Verify
```text
...
```
## Prompt 1B — <Focused Review>
```text
...
```
## Prompt 1C — Fix and Revalidate
```text
...
```
...

# Final ...
...
```

Every executable agent prompt must be fenced as `text`.

## Working Method content

The generated document should instruct the operator to:
1. run one implementation prompt;
2. inspect the result;
3. run verification without modifying code;
4. run focused review(s) without modifying code;
5. decide which findings are justified;
6. run the fix prompt for approved findings only;
7. re-run validation and the milestone gate;
8. commit verified work;
9. continue only after the gate passes.

State that a failed gate remains failed until fixed or explicitly accepted as a non-spec-breaking limitation.

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
- update affected docs;
- after implementation/fixes report files changed, decisions, commands, actual results, limitations, remaining risks, docs, and suggested Conventional Commit.

## Prompt 0 contract

Prompt 0 must:
- modify nothing;
- inspect all authoritative context;
- propose the full milestone order;
- identify existing code to reuse;
- identify modules/files/data/API/state/infrastructure implications as applicable;
- identify tests, real-environment checks, security/privacy/data-integrity/performance concerns as applicable;
- identify risks, documentation, and meaningful commit boundaries;
- surface contradictions, missing prerequisites, unclear requirements, unnecessary complexity, and weak build order;
- recommend the smallest production-quality choice;
- stop after the plan.

## Prompt 0A contract

Choose 2–4 relevant reviewer personas. Challenge:
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

Modify nothing.

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
- "Stop after this milestone."

For transaction/order-sensitive workflows, spell out atomic steps when that materially improves correctness.

## Verification prompt contract

Verification prompts:
- modify nothing;
- execute relevant checks;
- test behavior, not merely code shape;
- include negative cases;
- use real runtime/database/browser/network/integration resources where material;
- return `PASS`, `FAIL`, or `NOT VERIFIED` plus evidence;
- never say something merely "should work".

## Focused review contract

Review prompts:
- modify nothing;
- adopt a relevant skeptical specialist role;
- attempt realistic failure/abuse cases;
- inspect both implementation and observed behavior where appropriate;
- classify findings `Critical`, `High`, `Medium`, `Low`;
- include evidence, impact, affected path when possible, and smallest correct fix.

## Fix/revalidate contract

Fix prompts:
- fix approved findings only;
- remain within current milestone;
- do not add future features;
- re-run all relevant validation and regressions;
- report actual results;
- do not pass while unresolved Critical/High issues violate the gate.

## Final prompt families

Include only when applicable:
- final production/portfolio/release polish;
- final golden-path or critical-transaction rehearsal;
- final architecture/security/quality audit;
- final fix;
- clean-clone/clean-environment verification;
- public repository/release safety check;
- final readiness check tied to Definition of Done or acceptance criteria.

The final readiness table should use:

| Requirement | Evidence | Status | Required Action |
| --- | --- | --- | --- |

with status limited to `PASS`, `FAIL`, `NOT VERIFIED`.
