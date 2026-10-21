# Quality Evaluation Cases

A generated playbook should fail review if any of these occur:

- fixed phase count copied regardless of project size;
- same generic senior review repeated after every milestone;
- verification prompts modify implementation code beyond required system exercise or status bookkeeping;
- any milestone or prompt heading is missing a canonical status flag or carries multiple status flags;
- Milestone Gates omits the Status column or its status diverges from the milestone heading;
- a prompt updates itself but does not recompute its parent milestone;
- a milestone is COMPLETE while any required child prompt is incomplete or its gate is unsatisfied;
- a verification result of `FAIL` / `NOT VERIFIED` is incorrectly treated as an incomplete verification prompt rather than a completed prompt with an unsatisfied gate;
- a read-only prompt omits the status-bookkeeping exception;
- gates say only that code exists;
- real integration behavior is declared passed using mocks only;
- later milestones omit regressions for earlier critical paths they can affect;
- existing infrastructure is rebuilt without justification;
- hidden assumptions silently change the specification;
- final readiness is declared while Critical/High gate violations remain;
- output contains unsupported production, benchmark, or compliance claims.
