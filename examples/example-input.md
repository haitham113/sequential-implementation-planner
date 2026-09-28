# Example Input

Generate a sequential implementation and review prompt pack for adding subscription billing to an existing B2B SaaS.

## Context
- Existing NestJS API
- PostgreSQL + Prisma
- Organizations and users already exist
- Stripe will be used for subscription checkout and webhooks
- Existing authentication and organization authorization must not be rebuilt

## Requirements
- plans: Starter, Growth, Enterprise-contact-only
- one active subscription per organization
- trial support
- checkout session creation
- webhook-driven subscription state
- billing portal
- cancellation at period end
- plan change support
- audit history
- authorization: organization admins only
- webhook signature verification and idempotency
- no card data stored locally

## Delivery target
Merge-ready backend feature with API docs and integration tests.
