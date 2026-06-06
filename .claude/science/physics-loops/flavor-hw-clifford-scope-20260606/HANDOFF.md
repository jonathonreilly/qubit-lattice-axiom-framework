# Handoff

PR purpose:

Repair the audited scope-too-broad finding on
`FLAVOR_HW_CLIFFORD_DOES_NOT_CONSTRAIN_R_2026-06-02.md`.

What changed:

- Narrowed the source note to the runner-certified Fourier/HW no-go.
- Removed unproved Wigner/PSD/full-orbit `r=1` landmark claims from the
  load-bearing scope.
- Added a runner check that trace and traceless Hilbert-Schmidt norm are
  Fourier-conjugation invariant while not selecting a value.

Verification:

- Runner passes with `PASS=6 FAIL=0`.
- Runner cache is fresh.
- `git diff --check` passes.
- `git diff -- docs/audit --exit-code` passes.

Audit boundary:

No `docs/audit/**` files are modified. This PR does not set an audit verdict or
claim an effective status change.

Remaining science:

The separate `r=1` landmark package and the signed-vs-singular readout route
remain open frontier lanes.
