# Handoff

This block targets the `g_2(v)` bounded interval row's audit blocker for X6
and X7 only.

What changed:

- Hardened the existing 2026-06-15 bounded-support bridge with direct
  Planck-ruler / current repo `v` checks.
- Updated the bridge runner to read the scale primitive, unit-conversion
  runner, reusable-values index, and observable note before recomputing the
  scale logs.
- Updated the target note/runner to check that the bridge contains the new
  direct value-surface hardening.

What remains:

- `u_0(SU(2)) in [0.96,0.98]` is still an external literature interval.
- The perturbative one-loop ODE is not derived from the axioms in this block.
- Independent reviewer/auditor owns any audit movement.

Do not merge this as an audit verdict. It is source-side repair material only.

Verification passed:

- bridge runner: `TOTAL: PASS=27 FAIL=0`
- target `g_2(v)` runner: `PASS=31 FAIL=0`
- cached outputs fresh for both runners
- `py_compile` clean
- `git diff --check` clean
