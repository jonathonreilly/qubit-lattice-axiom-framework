## Summary

This PR retires textbook-math imports from the SU(3) fundamental Casimir
source row.

Changes:

- replaces Schur/SU(N)-formula proof dependence with a direct finite-matrix
  proof on the framework-supplied `V_3` Gell-Mann matrices;
- proves `sum_a (lambda^a/2)^2 = (4/3) I_3` in the source note;
- updates the runner so the direct matrix identity and centrality are proof
  gates;
- keeps Schur's lemma and the SU(N) formula as parallel context only;
- refreshes the runner cache and adds a branch-local physics-loop pack.

## Claim Boundary

This is bounded algebraic support on the `V_3` carrier. It does not identify
`V_3` with physical SM quark color and does not derive one-gluon-exchange,
self-energy, cross-section, or confinement readouts.

## Verification

- `python3 scripts/su3_casimir_fundamental_check.py`
- `python3 scripts/cached_runner_output.py scripts/su3_casimir_fundamental_check.py --refresh`
- `python3 scripts/cached_runner_output.py scripts/su3_casimir_fundamental_check.py --check-only`
- `python3 -m py_compile scripts/su3_casimir_fundamental_check.py`
- `git diff --check`
- source-side diff guard for audit/publication/front-door files

## Reviewer Notes

Review-loop was not run here; disposition is `reviewer_owned_not_run`.
