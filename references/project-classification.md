# Project Classification

Classify the requested work before decomposition. Use the classification to change milestone order, not merely to label the project.

## Greenfield

Use when little or no implementation exists.

Planning implications:
- introduce only the minimum foundation needed for the first useful vertical slice;
- test risky external/platform assumptions early;
- avoid speculative infrastructure;
- establish CI/testing/config only to the degree needed by upcoming behavior.

## Existing Feature / Module Addition

Use when adding capability to a working system.

Planning implications:
- inspect current behavior before editing;
- identify reusable seams and modules;
- define explicit regression checks for affected flows;
- avoid rebuilding auth, infrastructure, state management, logging, or deployment already present;
- document compatibility and migration concerns.

## Major Refactor

Use when behavior should remain broadly stable while structure changes.

Planning implications:
- define behavioral baselines before refactoring;
- prefer expand/contract or strangler-style transitions for broad blast radius;
- separate preparatory refactors from product behavior changes;
- require regression and rollback evidence.

## Migration / Upgrade

Use for database, framework, runtime, API-version, vendor, hosting, or architecture migrations.

Planning implications:
- inventory compatibility and data/state transitions;
- prove backup/restore or rollback where meaningful;
- include representative real-data or production-like rehearsal where safe;
- explicitly distinguish irreversible steps;
- verify post-migration counts/invariants and client compatibility.

## Infrastructure / Deployment

Use when the primary outcome is runtime, hosting, networking, CI/CD, observability, security, or operational behavior.

Planning implications:
- make environment assumptions explicit;
- prove clean setup/reproducibility;
- validate failure/recovery behavior;
- include least-privilege, secret handling, and rollback review;
- verify from the deployed/runtime environment, not only config inspection.

## Prototype / Challenge / Demo

Use when reliability of a narrow demonstrable path matters more than general product breadth.

Planning implications:
- identify the golden path early;
- test risky browser/API/platform dependencies immediately;
- deploy early if the final environment materially differs from local;
- prefer one polished, repeatable story over optional breadth;
- include rehearsal and judge/user comprehension checks.

## Mixed Work

If multiple classifications apply, state the primary classification and the secondary constraints. Example: "existing feature + data migration".
