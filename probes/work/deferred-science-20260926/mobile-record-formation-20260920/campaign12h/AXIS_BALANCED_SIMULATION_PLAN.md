# Declared microscopic checks of the all-density context rule

2026-09-21. No result from this new simulator has yet been examined. The
occupation-only context experiments remain separate and their ongoing runs
are not modified. This plan tests the newly proposed feature s_i=2n-3v_i^2.

The supplied parameters are fixed at u=0, E=1/2, kappa0=1/20, so alpha=1.
Use the positive-part exchange rate only. Every event exchanges immutable
labels or inserts a fresh label into a vacancy. The simulator is a separately
identified adaptation of the earlier calibrated event engine; its source
transformation is recorded in `AXIS_BALANCED_SIMULATOR_ADAPTATION.json`.

Before any cubic run, independently assemble the full 2401-state generator
on a four-site ring. Compare every auto/cross correlation of the six measured
fields at k=pi/2,pi and 21 times from 0 to 5. Use 8192 independent paths per
case and these five cases/seeds:

| Product initial law | Per-label birth rate | Seed |
|---|---:|---:|
| rho=1/4, occupied labels equal | 0 | 2026092170 |
| rho=1/2, occupied labels equal | 0 | 2026092171 |
| rho=3/4, occupied labels equal | 0 | 2026092172 |
| weights (5,1,2,3,4,5,6)/26 | 0 | 2026092173 |
| rho=1/2, occupied labels equal | 0.08 | 2026092174 |

The gate is a maximum real/imaginary correlation discrepancy below 5.5
estimated standard errors, together with exact finite-generator product
evolution residual below 2e-12 and per-path count/Fourier audits. This is a
stochastic implementation sanity check, not a simultaneous confidence claim.
Preserve any failed attempt and its source before correction.

If the calibration passes, execute the following cubic cases in this order:

| Case | Side | Initial rho | Per-label birth rate | Paths | Seed |
|---|---:|---:|---:|---:|---:|
| balanced_r025_L32 | 32 | 0.25 | 0 | 256 | 2026092175 |
| balanced_r050_L32 | 32 | 0.50 | 0 | 256 | 2026092176 |
| balanced_r075_L32 | 32 | 0.75 | 0 | 256 | 2026092177 |
| balanced_growth_L24 | 24 | 0.50 | 0.04/24 | 512 | 2026092178 |
| balanced_growth_L48 | 48 | 0.50 | 0.04/48 | 512 | 2026092179 |
| balanced_r025_L64 | 64 | 0.25 | 0 | 256 | 2026092180 |
| balanced_r050_L64 | 64 | 0.50 | 0 | 256 | 2026092181 |
| balanced_r075_L64 | 64 | 0.75 | 0 | 256 | 2026092182 |

Use two simulation threads per run so the other already-running checks and
personal derivations can continue. Each path's random seed is independent
of thread scheduling. Keep the 13 Fourier representatives and six fields
from the earlier screen. Use 65 times through one predicted axial period,
namely t_max=L/c_s(rho_initial), with
c_s(rho)=2rho sqrt((1-rho)/3). Every run retains complete raw paths, counts,+seeds, parameter metadata, and a final Fourier reconstruction audit.

For stationary cases, normalize density by sqrt(rho(1-rho)) and longitudinal
vector by sqrt(rho/3), and form their normalized plus/minus combinations.
The declared diagnostic fit is the same complex damped exponential over the
first predicted half-period used in the earlier family, now chosen before
these new data exist. Use 4000 complete-path bootstrap samples and 1000
refits; intervals omit model error. Compare the three directional shells
and two sizes at each density with their separate supplied speed predictions.
Do not infer a scaling theorem from six finite simulations.

For growth, compare the full density/vector covariance with the linear
time-dependent reaction equations at beta=0.04 and exact background
rho(tau)=1-0.5 exp(-6 beta tau), tau=t/L. The quadrupole variables decouple
at first order in the proposed current algebra for the entire trajectory;
check the prediction using the full six-field Jacobian as a control. Use
the same whole-path bootstrap, but do not fit a single stationary speed.
The growth cases do not test permanent finite-speed density waves at full
occupancy, where the proposed acoustic coefficient vanishes.
