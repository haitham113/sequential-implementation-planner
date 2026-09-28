---
name: sequential-implementation-planner
description: "Generate a project-specific sequential implementation and review playbook from an approved software project or feature specification. Use when a user wants phased AI-coding prompts, milestone gates, verification prompts, adversarial reviews, fix/revalidation loops, or final release-readiness checks. Do NOT use to directly implement the target project, for vague ideas that still need requirements discovery, or for a single small coding task that does not need a multi-stage execution plan."
---

# Sequential Implementation Planner

Turn an approved project or feature specification into a disciplined, project-specific AI implementation playbook. The playbook controls execution order, evidence gates, focused reviews, fixes, regression checks, and final readiness. It does **not** implement the target project.

## Core Invariants

1. **Specification first**: Identify the authoritative product/technical source of truth before planning work.
2. **One milestone at a time**: The generated playbook must never instruct an implementation agent to build all milestones in one run.
3. **Evidence before progression**: Every milestone has a checkable gate. Implementation alone is not completion.
4. **Review is separate from implementation**: Verification and adversarial review prompts do not modify code.
5. **Risk-shaped reviews**: Review prompts are selected from the actual risks of the milestone, not copied mechanically.
6. **Regression preservation**: Later milestones re-check important behavior proven earlier.
7. **Truthful validation**: Never claim a command, test, deployment, integration, browser flow, migration, or benchmark passed unless it was actually executed and observed. Use `NOT VERIFIED` when proof is unavailable.
8. **Smallest useful plan**: Use the fewest milestones that preserve safe sequencing, testability, and review quality.
9. **Existing-system awareness**: For existing repositories, plan the delta, reuse working code, and protect unrelated behavior.
10. **No hidden invention**: Surface contradictions, assumptions, missing decisions, and unresolved prerequisites explicitly.

## Map of Content

| Reference | Use it when |
|---|---|
| `references/project-classification.md` | Determining greenfield vs feature/refactor/migration/etc. and choosing milestone shape |
| `references/output-contract.md` | Rendering the final Markdown playbook and every prompt family |
| `references/review-catalog.md` | Selecting specialized adversarial reviews from milestone risks |
| `references/quality-gates.md` | Designing milestone gates, regression rules, and final readiness checks |
| `references/authoring-checklist.md` | Final self-review before returning the generated playbook |

Do not load every reference automatically. Read only the references needed for the current planning branch.

## Procedure

### Step 1 — Establish the planning basis
- **Action**: Read all user-supplied specifications, repository instructions, architecture notes, acceptance criteria, and relevant repository context.
- **Key Point**: Explicitly name the authoritative source(s) of truth and distinguish them from repository rules and this playbook's execution rules.
- **Why**: A sequencing document must not silently replace product requirements.

If the requirements are still fundamentally fuzzy or undecided, stop generation and route to requirements/specification work instead of inventing a build plan.

### Step 2 — Classify the work
- **Action**: Read `references/project-classification.md` and classify the work before decomposing it.
- **Key Point**: Existing features, refactors, migrations, infrastructure changes, prototypes, and greenfield projects require different sequencing and regression strategies.
- **Why**: Treating every request as a new application causes redundant foundations, missed migration risk, and unnecessary rewrites.

### Step 3 — Identify risks, invariants, and proof requirements
- **Action**: For each major capability, identify what can fail, what must never be violated, what prior behavior can regress, and what real environment is needed to prove correctness.
- **Key Point**: Separate logic that can be proven by unit tests from behavior requiring a real database, browser, queue, network, payment provider, deployment, or other integration environment.
- **Why**: The strongest prompt packs are specific about evidence rather than generic about testing.

### Step 4 — Design the milestone graph
- **Action**: Choose the smallest coherent ordered milestone set. Prefer vertical, independently verifiable slices and move risky feasibility checks earlier.
- **Key Point**: Do not force a fixed phase count. Dependencies precede dependents; high-risk unknowns are resolved before architecture depends on them.
- **Why**: Artificial phase counts create ceremony instead of control.

Inline check:
- [ ] Every milestone has one coherent purpose.
- [ ] Every milestone can be verified independently.
- [ ] The order respects technical dependencies.
- [ ] Risky or uncertain platform capabilities are tested early.
- [ ] No milestone exists only to imitate another project.

### Step 5 — Generate planning and challenge prompts
- **Action**: Use `references/output-contract.md` to generate Prompt 0 and Prompt 0A.
- **Key Point**: Prompt 0 plans without editing. Prompt 0A challenges the proposed plan from project-appropriate expert perspectives.
- **Why**: Challenging the plan before coding is cheaper than discovering sequencing errors after implementation begins.

### Step 6 — Generate each milestone loop
- **Action**: For each milestone, generate the implementation prompt, verification prompt, one or more justified specialist reviews, and fix/revalidation prompt.
- **Key Point**: Select reviews using `references/review-catalog.md`; do not mechanically generate the same review titles for every milestone.
- **Why**: Authentication, concurrency, browser lifecycle, financial integrity, migration safety, accessibility, and queue reliability fail in different ways.

The default loop is:

`Implement → Verify → Focused Review(s) → Human/owner approves findings → Fix → Revalidate Gate → Commit → Next milestone`

### Step 7 — Add regression and final gates
- **Action**: Read `references/quality-gates.md` and add cross-milestone regression checks plus final audit/readiness prompts appropriate to the delivery target.
- **Key Point**: Previously verified critical paths remain protected after later changes.
- **Why**: A new feature is not progress if it silently breaks an earlier gate.

### Step 8 — Render and self-review the playbook
- **Action**: Produce one complete Markdown document following `references/output-contract.md`, then run `references/authoring-checklist.md` against it.
- **Key Point**: Every generated coding-agent prompt must be directly copyable and bounded to its current phase.
- **Why**: The output is an execution manual, not an essay about good engineering.

## Required Output Behavior

The final response should normally produce or save a file named:

`<PROJECT_OR_FEATURE>_SEQUENTIAL_IMPLEMENTATION_AND_REVIEW_PROMPTS.md`

The document must include, when applicable:

- authoritative source-of-truth statement
- Working Method
- Global Rules
- Milestone Gates
- Prompt 0 — assessment/plan
- Prompt 0A — challenge plan
- sequential milestone prompt families
- project-specific final polish/hardening
- final critical-path rehearsal when meaningful
- final architecture/security/quality audit
- final fix
- clean-environment verification when meaningful
- public repository/release safety check when meaningful
- final readiness check when the project has a delivery target
- concise final principle

Omit sections that do not apply. Do not inflate the playbook with ceremonial prompts.

## Anti-Rationalization Guardrails

| Temptation | Binding rule | Why |
|---|---|---|
| “Ten phases looked good before, so use ten again.” | Choose phase count from dependencies and risks. | Fixed templates create useless work. |
| “Implementation passed, so the gate passes.” | Verification evidence is mandatory. | Presence of code does not prove behavior. |
| “Use one generic senior review everywhere.” | Reviews must match milestone failure modes. | Generic review misses domain-specific hazards. |
| “The spec is silent, so choose silently.” | State the assumption or unresolved decision. | Hidden invention changes product behavior. |
| “Mocks are enough for everything.” | Use real environments where the behavior materially depends on them. | Mocks cannot prove integration/runtime behavior. |
| “Add future infrastructure now because we may need it.” | Defer speculative infrastructure. | Premature complexity weakens maintainability and credibility. |
| “Write a huge SKILL.md with every template inline.” | Keep this file as the map; disclose detail through references. | Progressive disclosure preserves agent attention. |

## Completion Criteria

A generated playbook is complete only when:

- milestone order is justified by dependencies and risk;
- each milestone has a measurable gate;
- verification is non-mutating and evidence-based;
- focused reviews match the milestone's failure modes;
- fix prompts stay inside current scope and re-run relevant proof;
- prior critical behavior is protected by regression checks;
- final readiness is tied to actual acceptance/release evidence;
- no command/test/deployment is represented as successful without actual execution.
