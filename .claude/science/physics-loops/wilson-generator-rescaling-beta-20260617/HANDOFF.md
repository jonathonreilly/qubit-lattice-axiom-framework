# Handoff

This block adds a source-side Wilson generator-rescaling beta bookkeeping
theorem for the `g_bare_rescaling` conditional blocker.

It proves exact convention maps under `T_a -> c T_a`:

- fixed component coupling/field coordinates: `beta_new / beta_old = 1/c^2`;
- fixed exponent with `g_new = g_old/c`: unchanged Wilson quadratic coefficient
  at the same beta;
- re-canonicalized coupling-coordinate reporting:
  `beta_canonical(g_new) / beta_canonical(g_old) = c^2`.

The note intentionally does not derive the Wilson action surface, `beta=6`, or
`g_bare=1`, and it does not edit audit data.

Verification:

- `python3 scripts/wilson_generator_rescaling_beta_bookkeeping_2026_06_17.py`
  -> `SUMMARY: PASS=29 FAIL=0`.
- `python3 scripts/frontier_g_bare_rescaling_conditional_algebra_check.py`
  -> `SUMMARY: PASS = 10, FAIL = 0`.
- `python3 -m py_compile scripts/wilson_generator_rescaling_beta_bookkeeping_2026_06_17.py scripts/frontier_g_bare_rescaling_conditional_algebra_check.py`
  -> pass.
