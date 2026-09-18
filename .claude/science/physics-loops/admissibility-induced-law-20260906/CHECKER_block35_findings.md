# Refuting pass — block 35 (supervisor-run, disjoint machinery; 2026-09-18)

Routes compared (control `specs/supervisor_control_block35_kernel_sim.py`; refuting pass `specs/supervisor_control_block35_refuter.py`, run from `scripts/` as `python3 <specs>/supervisor_control_block35_refuter.py .`; outputs in `.out.txt`):

| item | runner's / control's route | refuting route | result |
|---|---|---|---|
| the cross-level covariance (T1) | exact rational recursions on `L = 3, 4` with the cosine characters | the recursion in floating point on `L = 8` for `300` levels, Fourier-projected, against `φ(k)^s` for `s ≤ 16` | see the output's first line (largest discrepancy) |
| the small-k forms (T2–T3) | symbolic series | numerical ratios `(1 − u)/(kᵀMk)` and `arg φ/((k₁ + k₂)/3)` as `k → 0` | both tend to `1` |
| the nonlinear normalization (executed) | fixed frame (orthogonal to the initial direction), `L = 256` | the frame rotating with the plane average, `L = 128`, `β = 12` | shell ratios agree with the fixed frame within the sampling error (see output) |
| the comparator's non-product form (T3) | the mixed derivative symbolically at a rational point | finite differences at five random points | never zero |

Findings: nothing refuted. Fold items: the control's real-space structure function carried a factor `L` from the transform's normalization (the ratio to the linear value was `≈ 256 c(β)`), corrected; the runner's classical-name scan matched the terms of art "Green function" and "Newtonian" inside the note's own statements and the two names were dropped from the scan (block 13's title already uses "Green function"). Facts settled while executing: the normalization `c(β)` is a property of the coupling (`0.89, 0.94, 0.97`) with a dip at the longest wavelengths; the cross-level phases match the drift exactly at every wavevector shown.
