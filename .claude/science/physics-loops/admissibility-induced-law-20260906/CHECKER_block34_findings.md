# Refuting pass — block 34 (supervisor-run, disjoint machinery; 2026-09-17)

Routes compared (controls `specs/supervisor_control_block34_torus_msd.py`, `..._torus_sim.py`; refuting pass `specs/supervisor_control_block34_refuter.py`, run from `scripts/` as `python3 <specs>/supervisor_control_block34_refuter.py .`; outputs in `.out.txt`):

| item | runner's / control's route | refuting route | result |
|---|---|---|---|
| the mode formula (T1–T2) | exact rational covariance recursion on `L = 2, 3, 4` | the same recursion in floating point on `L = 8` for `400` levels against the mode sum with numerical cosines | largest discrepancy `1.4·10⁻¹³` (site and plane-average variances) |
| the memory times (T3.1) | exact enclosures through the series for `coth` | `numpy`'s `coth` in floating point | agreement to the printed precision at all twelve `(β, L)` |
| the nonlinear direction's diffusion | block 26's sampler (cosine by inversion in a tangent frame), the mean-squared angular displacement | an independent rotated-pole sampler with the exponential-fit estimator, `12` seeds, `(6, 16)` | ratio `1.28` against the control's `1.36` by the same noisy estimator and `1.34` by the displacement estimator |
| the stationary variance (T3.2) | the bracket `[3/(4π²), 9/16]σ²S_L` (exact) | direct summation of `(1/L²)Σ_{k≠0} 1/(1 − u_k)` for `L = 16, 32, 64, 128` | inside the bracket; `V_L/σ² − 2c₀ log L = 0.3514, 0.3525, 0.3527, 0.3528` |

Findings: nothing refuted. Fold items: the first estimator (an exponential fit of the ensemble mean of the projection) returned ratios from `0.5` to `1.9` for the nonlinear law and from `0.3` to `1.0` for the linear model at `8–32` seeds — it reads the random walk's fluctuations rather than the rate — and was replaced by the mean-squared angular displacement, which the linear model calibrates to `0.97–1.01`; the runner's classical-name scan matched "Machin" inside the section title "Machine status and trace" and the name was dropped from the scan (it appears only under Imports). Facts settled while executing: the nonlinear excess is a property of the coupling, not of the size (`L = 16` and `32` agree within errors), and tracks `1/|m|²`.
