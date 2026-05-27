# PR #1980 Y_T Positive Closure Physics-Loop Campaign

Use the `physics-loop` skill in campaign mode.

Runtime target: 12 hours total, or stop early only if positive retained-grade
closure is actually achieved and the branch/PR are updated.

Work location:

- repo: `/private/tmp/yt-primitive-physical-source-theorem-20260526`
- branch: `physics-loop/yt-primitive-physical-source-theorem-20260526`
- PR: <https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/1980>
- do not create new PRs; update this branch and PR only
- do not commit or push to `main`

Current state:

- The first-principles transfer/Feynman-Hellmann bridge is closed as exact
  support by
  `docs/YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md`.
- Formal transfer first principles alone do not force `kappa`.
- The current first open gate is narrow:

```text
derive/certify the coefficient-bearing same-surface top sector matrix element
dM_t/dell = A/sqrt(12)
```

or:

```text
derive a non-mass-ordering same-surface C3 top-line law that assigns the
physical top pole to a nontrivial C3 character line and supplies the source
matrix element.
```

Campaign requirements:

1. Read the latest stack and all directly relevant Y_T docs/runners first.
2. Run assumptions exercise, first-principles/Elon exercise, literature/math
   search where useful, and no-go audit for each route before declaring it
   blocked.
3. Do not repeat already closed work unless needed to test a new premise.
4. Work routes in priority order:
   - same-surface top sector matrix element theorem;
   - non-mass-ordering C3 top-line law;
   - accepted C3 circulant dynamics/source law for `a(h), x(h), y(h)`;
   - strict sparse top/W pole-response evidence/certificate route;
   - any new first-principles route found during the loop.
5. If one route ends in a no-go or exact support boundary, checkpoint it and
   pivot to the next ranked opportunity. Do not stop the campaign merely
   because one route fails.
6. Every coherent science movement must add a theorem/support/no-go note,
   runner, output JSON, loop-pack state, and stack update on this branch.
7. Keep claim status honest. No retained/proposed-retained wording unless the
   coefficient row is genuinely derived/certified and the review gates pass.
8. Forbidden proof inputs: `H_unit`, old Ward authority,
   `yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG targets,
   `alpha_LM`, plaquette/u0, Planck, alpha_s, fitted selectors, or target
   value insertion.
9. Verification after each block:
   - new runner;
   - `scripts/frontier_yt_full_closure_stack_and_strict_pole_response_contract.py`;
   - adjacent relevant runners;
   - `python3 -m py_compile ...`;
   - `git diff --check`.
10. Commit coherent blocks, push the branch, and update PR #1980 body with
    the exact result and verification.

Positive closure marker:

If and only if full positive closure is achieved, write:

```text
.claude/science/physics-loops/yt-positive-closure-12h-20260527/POSITIVE_CLOSURE
```

The marker must include the commit hash, theorem note, runner output, and the
exact reason retained/proposed-retained wording is allowed.

If full positive closure is not achieved in this invocation, leave the narrowest
honest artifact and update:

```text
.claude/science/physics-loops/yt-positive-closure-12h-20260527/STATE.yaml
.claude/science/physics-loops/yt-positive-closure-12h-20260527/HANDOFF.md
```

Do not ask for permissions. Do not use `sandbox_permissions`.
