# Handoff

Target claim: `lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07`

Remote branch: `physics-loop/lensing-h025-edge-kernel-20260608`

## What Changed

- Added `scripts/frontier_lensing_h025_edge_kernel_certificate_2026_06_08.py`, a streaming H=0.25 edge-kernel certificate.
- It streams 65,528,627 edge contributions without materializing the edge list.
- It reproduces the H=0.25 fine slope certificate values at `b={3,4,5,6}` and verifies `slope=-1.433549`, `R2=0.998404`.
- It verifies monopole cancellation at H=0.25: `|sum c|/sum|c|=0.000282`.
- It verifies the `|c|` non-cancelling control is monopole-like: slope `-0.989168`.
- It narrows the source note away from exact `b^-2` asymptotics because the fine-H signed large-b slope is `-2.358053`.

## Verification

- `python3 scripts/frontier_lensing_exponent_is_dipole_crossover.py` -> `TOTAL: PASS=8 FAIL=0`
- `python3 scripts/frontier_lensing_h025_edge_kernel_certificate_2026_06_08.py` -> `TOTAL: PASS=12 FAIL=0`
- cache refresh for both runners

## Remaining Blocker

The exact continuum signed-tail asymptotic order remains open. This branch should not be used to claim a continuum dipole theorem or standard `1/b` lensing.
