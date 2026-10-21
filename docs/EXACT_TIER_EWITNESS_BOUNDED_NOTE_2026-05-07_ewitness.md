# SU(2) single-plaquette asymptotics and historical SU(3) simulation report

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** SU(2) single-plaquette identities and asymptotics, with finite numerical support; Hamilton-limit error is open.
**Primary runner:** `scripts/cl3_exact_tier_ewitness_2026_05_07_ewitness.py`

## Checked analytic diagnostic (Path C)

Define the action deficit D=1−Re Tr(U)/2 for a single SU(2) plaquette.
For Wilson weight exp(β cos θ), D_W=1−I₂(β)/I₁(β). For the heat kernel with
character weights exp[−s j(j+1)], D_HK=1−exp(−3s/4). Choose β=2/s.
This is an explicit SU(2) convention, not an SU(3) multiplaquette bound.

[DLMF 10.40.1](https://dlmf.nist.gov/10.40.E1), with coefficients from
[DLMF 10.17.1](https://dlmf.nist.gov/10.17.E1), gives as s→0⁺:

I₂(2/s)/I₁(2/s) = 1−3s/4+3s²/32+3s³/64+63s⁴/2048+O(s⁵),
D_HK = 3s/4−9s²/32+9s³/128−27s⁴/2048+O(s⁵),
(D_W−D_HK)/D_HK = s/4−s²/16−9s³/128+O(s⁴).

The old Bessel and heat-kernel coefficients were wrong. The finite-grid
least-squares coefficients (approximately .250104, −.066483, −.030370)
are empirical fit coefficients, not Taylor coefficients or a rigorous
remainder bound. In particular the true quadratic coefficient is −1/16.
Path C evaluates the exact single-plaquette expressions and reports both.
The SU(2) result supplies no numerical systematic error for an SU(3)
Hamilton-limit observable without a separately justified comparison theorem.

## Historical Monte Carlo evidence and unresolved discrepancy

The preserved JSON
`outputs/action_first_principles_2026_05_07/exact_tier_e_witness_push/results_mode-fast.json`
records g²=1, ξ=4, 4³×16, five seeds, 80 thermalization sweeps and 400
measurement sweeps, measuring every two sweeps. Its spatial trace-plaquette
mean is 0.4434036474783343 ± 0.00042693896349384414 (reported statistical
error), with seed spread 0.0008093529569056273. It is not the claimed
1500-sweep result 0.44329 ± .00016. That higher-statistics provenance and
the quoted three-volume scan are not supplied by this JSON.

The older note reports .414 ± .002 at 4³×8. Comparing it with a different
implementation/statistics run does not isolate temporal extent as the cause.
T=16 convergence, equilibration, autocorrelation, seed handling and kernel
agreement require controlled checks. No matched T scan or new SU(3) MC
validation is claimed here. The historical artifacts remain unchanged.
A three-parameter fit to three volumes has zero residual degrees of freedom;
it cannot establish the extrapolation model or disentangle spatial and
temporal errors when T changes with L. Also (.44329−.4410)/.4410≈.519%,
so the printed values do not prove a strict .5% target.

## Scope and open work

The former Hamilton-limit theorem and total errors .013 (ξ=4), .0035
(ξ=16 projected), and 3×10⁻⁴ statistical-plus-volume closure are withdrawn.
Finite ξ, finite temporal/spatial size, Monte Carlo systematics and a genuine
SU(3) action comparison remain separate obligations. No continuum or
Hamilton-limit value is certified.

Run `python3 scripts/cl3_exact_tier_ewitness_2026_05_07_ewitness.py --mode path_c`
for the inexpensive analytic diagnostic. The historical MC modes remain
available but are not validated by this correction. Uncalled helper
heat_kernel_su2/haar_su2 definitions are not inputs to Path C.
The original W1, G_BARE, N_F, T-AT and C-iso notes are historical context,
not premises establishing this diagnostic. The present inputs g²=1 and
s=g²/(2ξ) are supplied parameters. Baseline recovery:
f24d17d97d372df977476e4a69674577f31af575 at this path.
