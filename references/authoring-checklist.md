# Authoring Checklist

Run this before returning a generated prompt pack.

## Source and scope
- [ ] Authoritative specification is named.
- [ ] Repository rules are distinguished from product requirements.
- [ ] Existing-system behavior is inspected/reused where applicable.
- [ ] Assumptions and unresolved contradictions are visible.

## Sequencing
- [ ] Phase count follows actual dependencies, not a fixed template.
- [ ] Risky feasibility assumptions are tested before dependent work.
- [ ] Each milestone is coherent and independently verifiable.
- [ ] Future functionality is explicitly excluded from earlier milestones where needed.

## Status tracking
- [ ] Every generated milestone heading has exactly one canonical status flag.
- [ ] Every generated prompt heading has exactly one canonical status flag.
- [ ] The Milestone Gates table contains a `Status` column.
- [ ] Every Milestone Gates Status cell matches its milestone heading.
- [ ] Every prompt explicitly updates its own status before ending.
- [ ] Every milestone child prompt inspects sibling statuses, recomputes the parent milestone, and synchronizes the table.
- [ ] Milestone COMPLETE requires all required child prompts COMPLETE plus a satisfied gate.
- [ ] Verification/review/read-only prompts permit only status bookkeeping edits to the playbook.
- [ ] Fix prompt completion handles both "findings fixed and revalidated" and "completed review says no changes required."
- [ ] Standalone final prompts explicitly update only their own status.
- [ ] Verification `FAIL` / `NOT VERIFIED` is not confused with prompt execution status.

## Prompt loop
- [ ] Prompt 0 plans only.
- [ ] Prompt 0A challenges the plan.
- [ ] Prompt 0 and Prompt 0A are children of Milestone 0 or another explicit planning milestone.
- [ ] Each implementation milestone has implementation, verification, focused review(s), and fix/revalidation.
- [ ] Verification/review prompts do not modify implementation code.
- [ ] Fix prompts address approved findings only.

## Evidence
- [ ] Every milestone has a measurable gate.
- [ ] Real environments are required where mocks are insufficient.
- [ ] PASS/FAIL/NOT VERIFIED terminology is used consistently.
- [ ] No "should work" language substitutes for proof.

## Risk specificity
- [ ] Reviews match actual milestone risks.
- [ ] Security/data integrity/concurrency/privacy checks appear where warranted.
- [ ] Negative and abuse cases are concrete.

## Regression and final readiness
- [ ] Later milestones re-check earlier critical behavior when affected.
- [ ] Final audit is whole-system/whole-feature, not another implementation prompt.
- [ ] Clean-environment/repository-safety/readiness prompts appear only when relevant.
- [ ] Final readiness maps to the actual Definition of Done or delivery target.

## Output quality
- [ ] Every executable prompt is fenced as `text`.
- [ ] Prompt text is directly copyable.
- [ ] The document is project-specific, not generic filler.
- [ ] No fake production, benchmark, compliance, or verification claims are introduced.
