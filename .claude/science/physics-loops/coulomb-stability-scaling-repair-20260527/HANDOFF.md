# Handoff

## Summary

This PR repairs the Coulomb upper-bound support row by replacing the admitted
P1/P2/P3 binding theorem with a self-contained Green-kernel scaling theorem.
The runner checks the radial harmonic kernel, dilation norm preservation,
kinetic scaling, potential scaling, and `d >= 5` negative-divergence witnesses.

## Claim Movement

- Before: conditional on admitted general-`d` Coulomb Hamiltonian, continuum
  QM scaling/spectrum facts, and physical Coulomb-sector identification.
- After: bounded theorem candidate for the Green-kernel scaling sublemma only.
- Remaining: no physical EM sector, no coupling value, no hydrogen spectrum,
  no parent dimension-selection promotion.

## Verification

- `python3 scripts/frontier_coulomb_stability_scaling_repair.py`
- `python3 scripts/vocab_lint.py --report-only docs/COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`

## Next Action

Open as a draft PR. If review accepts the scope, the reviewer can extract the
science and the independent audit lane can re-audit the changed row.
