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

## Prompt loop
- [ ] Prompt 0 plans only.
- [ ] Prompt 0A challenges the plan.
- [ ] Each milestone has implementation, verification, focused review(s), and fix/revalidation.
- [ ] Verification/review prompts do not modify code.
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
