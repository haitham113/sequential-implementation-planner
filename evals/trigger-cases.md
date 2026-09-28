# Trigger Evaluation Cases

## Should trigger

1. "Create a Codex prompt pack that implements this PRD in phases with verification and review after each phase."
2. "Turn this approved feature spec into sequential implementation prompts with gates and security reviews."
3. "I want a milestone-by-milestone AI coding playbook for this existing repo, including verify/fix loops."
4. "Generate something like an implement-review-fix execution manual for this migration plan."
5. "Break this approved architecture into phased prompts where Codex stops after each verified milestone."

## Should not trigger

1. "Implement this endpoint now."
2. "Fix this failing test."
3. "Help me brainstorm whether this SaaS idea is useful."
4. "Write a technical specification for this vague idea."
5. "Review this pull request."
6. "Explain JWT refresh tokens."

## Borderline

1. "Break this spec into tickets." — Prefer a ticket-decomposition skill unless the user explicitly wants implement/verify/review/fix prompt loops.
2. "Plan this large architecture migration." — Use this skill only when the requested deliverable is a sequential AI execution playbook; otherwise prefer architecture/wayfinding planning.
