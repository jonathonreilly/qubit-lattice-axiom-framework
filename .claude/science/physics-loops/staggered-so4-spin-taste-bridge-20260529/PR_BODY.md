## Summary

Repairs the audit blocker for
`lorentz_boost_free_staggered_fermion_2point_so4_narrow_theorem_note_2026-05-29`
without narrowing the claim.

The new packet derives the displayed reduced-BZ spin/taste operator from
the framework canonical free staggered action/phases:

- block sites as `n=2y+b`, `b in {0,1}^4`;
- rephase `chi_b(p)=exp(i a p.b) zeta_b(p)`;
- verify the blocked difference is exactly
  `i sin(p_mu a)/a alpha_mu`;
- verify the canonical `alpha_mu` satisfy `Cl_4(C)`;
- verify generated algebra dimension `16` and commutant dimension `16`,
  giving the finite taste spectator identity;
- verify the fourfold taste degeneracy and closed inverse denominator.

## Checks

- `python3 -m py_compile scripts/frontier_lorentz_boost_free_staggered_fermion_2point_so4.py`
- `python3 scripts/frontier_lorentz_boost_free_staggered_fermion_2point_so4.py`
  - `SCORECARD: PASS=46  FAIL=0`
- `bash docs/audit/scripts/run_pipeline.sh`
  - target row reset to `unaudited`
  - queue ready: `true`
  - open dependency paths: `[]`

## Status

Branch-local status: bounded-support, re-audit ready.

This PR does not apply an audit verdict and does not claim effective
retained status. Independent audit is still required.
