# Quality Evaluation Cases

A generated playbook should fail review if any of these occur:

- fixed phase count copied regardless of project size;
- same generic senior review repeated after every milestone;
- verification prompts modify code;
- gates say only that code exists;
- real integration behavior is declared passed using mocks only;
- later milestones omit regressions for earlier critical paths they can affect;
- existing infrastructure is rebuilt without justification;
- hidden assumptions silently change the specification;
- final readiness is declared while Critical/High gate violations remain;
- output contains unsupported production, benchmark, or compliance claims.
