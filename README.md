# Sequential Implementation Planner

An agent skill that converts an approved software project or feature specification into a project-specific **sequential implementation and review prompt pack**.

The generated playbook follows a disciplined loop:

> Plan → Challenge → Implement → Verify → Focused Review → Fix → Revalidate Gate → Commit → Next Milestone → Final Audit/Readiness

It is inspired by the execution discipline of real project prompt packs, but it does not force a fixed number of phases or generic reviews. The content is adapted to each project's dependencies, risks, invariants, runtime environment, and delivery target.

## What it does

Given a specification and optional repository context, the skill generates a Markdown execution manual containing:

- source-of-truth precedence;
- working method and global rules;
- evidence-based milestone gates;
- architecture/repository planning prompt;
- challenge-the-plan prompt;
- per-milestone implementation prompts;
- non-mutating verification prompts;
- project-specific adversarial review prompts;
- fix/revalidation prompts;
- regression checks;
- final audit, clean-environment, repository-safety, and readiness prompts when applicable.

## What it does not do

It does **not** implement the target project itself. It generates the execution protocol another coding agent can follow one milestone at a time.

It also should not be used when the idea is still too vague to specify or when a tiny one-step code change does not justify a staged implementation plan.

## Repository structure

```text
.
├── SKILL.md
├── references/
│   ├── authoring-checklist.md
│   ├── output-contract.md
│   ├── project-classification.md
│   ├── quality-gates.md
│   └── review-catalog.md
├── examples/
├── evals/
├── scripts/
└── tests/
```

## Example invocation

```text
Generate a sequential implementation and review prompt pack for adding subscription billing to an existing SaaS.

Authoritative spec: docs/subscriptions-spec.md
Repository rules: AGENTS.md
Target stack: NestJS, PostgreSQL, Prisma, Stripe.
The current application already has authentication and organizations; preserve them.
```

The expected output is a file similar to:

```text
SUBSCRIPTION_BILLING_SEQUENTIAL_IMPLEMENTATION_AND_REVIEW_PROMPTS.md
```

## Design principles

- smallest useful milestone set;
- vertical, independently verifiable progress;
- explicit negative scope;
- real proof before progression;
- reviews shaped to actual failure modes;
- regression protection across milestones;
- truthful `PASS` / `FAIL` / `NOT VERIFIED` states;
- progressive disclosure in the skill itself.

## Validation

Run:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```
