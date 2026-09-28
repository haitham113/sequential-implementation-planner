# Focused Review Catalog

Select reviews because their failure modes exist in the current milestone. Do not include irrelevant reviews just to enlarge the prompt pack.

| Risk area | Review focus / attack ideas |
|---|---|
| Authentication | hashing, token/session lifecycle, refresh rotation, replay, enumeration, reset/verification, rate limiting, sensitive logs |
| Authorization / multi-tenancy | foreign IDs, ownership, role-only checks, cross-tenant enumeration, trusted client tenant IDs, stale memberships, admin bypass |
| Financial / ledger | rounding, currency, immutable history, duplicate financial operations, negative balances, rollback, auditability, races |
| Transactions / booking / inventory | atomicity, overbooking, partial state, locks, idempotency, retry-after-timeout, double cancellation/refund, deadlocks |
| Database / data access | missing indexes, unscoped fetches, isolation, constraints, N+1, pagination, expensive counts, unsafe cascades |
| Queues / async jobs | retries, duplicate execution, poison jobs, dead-letter behavior, job-before-commit, payload size, idempotency, sensitive logs |
| Import / batch processing | streaming, memory, batching, duplicates, partial failure, status reporting, retries, tenant boundaries |
| Payments / webhooks | signatures, replay, duplicate events, ordering, raw-body needs, secret handling, state transitions, duplicate refunds |
| Browser / WebRTC / platform APIs | real-object truth, lifecycle cleanup, permission/gesture constraints, unsupported browsers, races, stale async completions, deployed-origin behavior |
| Frontend state | stale data, race conditions, optimistic rollback, loading/error/empty states, navigation lifecycle, persisted state |
| Accessibility | keyboard use, focus, labels, semantics, contrast, reduced motion, error announcements, responsive reflow |
| Security / privacy | injection, mass assignment, authorization bypass, secret leakage, PII, unsafe logging, sanitization, upload handling |
| API contract | REST/GraphQL consistency, DTO leakage, validation, error shape, pagination, backwards compatibility, documentation |
| Performance / scale | indexes, N+1, payloads, memory, locks, connection use, cache invalidation, queue pressure, expensive aggregates |
| Time / timezone | UTC strategy, local-zone preservation, DST gaps/overlaps, cutoff calculations, serialization, recurring schedules |
| Migration / upgrade | compatibility, irreversible steps, backup/restore, rollback, schema/data counts, mixed-version behavior, downtime assumptions |
| Infrastructure / deployment | reproducibility, secrets, least privilege, health/readiness, rollback, TLS/network assumptions, config drift, failure recovery |
| Observability | truthful metrics, missing/zero confusion, correlation IDs, structured logs, alert actionability, sensitive telemetry |
| Repository / release hygiene | secrets, dumps, debug code, TODOs, dead files, generated artifacts, default scaffold text, local paths, unsupported claims |

## Review selection rules

- One high-risk milestone may justify multiple focused reviews.
- A low-risk milestone may need only one concise review.
- Prefer a concrete attack/challenge scenario over an abstract checklist.
- If the milestone depends on concurrency, use simultaneous attempts with explicit invariants.
- If it depends on a real platform API, verify in the target environment rather than mocks alone.
- If it mutates money, capacity, permissions, or user data, include rollback/idempotency/authorization attack cases.
