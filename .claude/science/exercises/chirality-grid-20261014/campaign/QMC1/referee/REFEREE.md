# Independent referee report: QMC-1

## Verdict and fixed reading

**VERDICT: CONFIRMED WITH CORRECTIONS.**

**Correct fixed reading: OPEN.** The sign-free AFQMC engine and the reported
finite-size enhancement of the filtered 10-vector structure factor are
confirmed. The fixed GPR-PILOT reading is not, because the pre-registered gap
estimator E1 does not resolve an open gap at both sizes, while E2, E3, and E3w
do not supply a valid lower-edge spectral-gap determination. E2 is a
shorter-time effective decay fit and E3/E3w bound low-energy *weight*, not the
absence of low-energy support. Thus the prerequisite "mirror gap is open" in
`TESTS.md:326-338` remains unclosed.

The scope of this verdict is the ungauged 2+1-dimensional analogue of the X2
matter Hamiltonian at lambda1 = 0, with global Spin(10), periodic square
lattices L = 4 and 6, filter f2, beta = 4, and the stated finite time steps. It
does not decide the zero-temperature or thermodynamic-limit phase, the 3+1D
model, or the gauged theory.

## Independent checks performed

I did not rerun a production point. All referee runs used the 1 GB watchdog
with two BLAS/OpenMP threads and peaked below 0.47 GB RSS.

1. I reconstructed the quartic identity by an independent exterior-algebra
   enumeration, rather than calling `FlavourModel.four_form`. The maximum
   residual was 8.88e-16, or 1.48e-16 relative to the largest target
   coefficient. The 64 retained channels had zero sign/parity defects, zero
   trace, and maximum defect 1.11e-16 from `O^2 = 1/4`.
2. On a reduced-flavour toy system I compared the low-rank vertex with a
   direct full-matrix product of `scipy.linalg.expm` factors: maximum defect
   6.66e-16. I found `log|det M| = -2.0e-14` (hence `det M = 1` to
   roundoff), agreement of the
   local and full determinant ratios to 1.11e-16, and agreement of the
   Woodbury-updated and directly recomputed Green matrices to 2.22e-16.
3. The archived corrected gate-(iii) QMC `.npz` files are absent, so I ran a
   short independent 3,000-sweep reduced-flavour check at the registered
   `dtau = 0.05` point (`ref_gate3.npz`, `ref_gate3.log:1-325`). It gave
   `W<Q> = -0.133245(1170)` versus ED `-0.1343829494`,
   `sum(S_X+S_Y) = 0.563006(1178)` versus `0.563822244`, and
   `E_kin = -2.4216061(1881)` versus `-2.4214828453`: respectively 0.97,
   0.69, and 0.66 standard deviations from ED.
4. I independently reloaded every main f2 `.npz`, recomputed all-sweep means,
   block errors, time-slice Green functions, and size ratios. The published
   main ratios are reproduced. Using all 45 L6 measurements rather than the
   first 40 gives approximately 1.00, 1.35, and 0.87 at W = 2, 4, and 8.
5. I instrumented one full L4 sweep at W = 0.25 and W = 4. All 640 proposal
   determinants in each run were finite and nonzero, despite Accelerate
   emitting its generic determinant floating-point warnings. This supports,
   but does not prove globally, the worker's diagnosis that those warnings are
   spurious in these runs.

## 1. Engine

### 1.1 Hamiltonian and Fierz decomposition

The simulated Hamiltonian is the stated 2D analogue of the X2 lambda1 = 0
member. The code constructs the real Cl(9) gamma matrices, rotates to the
Gamma9 eigenspaces, takes `N^a = Gamma^a` for a <= 9 and `N^10 = i I`, and
uses

`Q_x = -(1/4) sum_a [B^a B^a + h.c.]`.

This is explicit at `scripts/x2model.py:15-18,31-110`; the f2 filter and walker
are implemented at `scripts/afqmc.py:31-95`. The c-sector kinetic symbol
`h(k)^T` at `scripts/afqmc.py:88-95` is also correct: the particle-hole
transformation gives `-H^T` in real space, which is `h(k)^T` after the momentum
reversal in the full transpose.

The chosen Fierz point

`(kappa_sing8v, kappa_trip8v, kappa_sing56v, kappa_trip56v)
 = (1.5, -0.5, 0, 0)`

is exact and has no remainder. The code exhausts the 35,960 possible
four-annihilator components at `scripts/x2model.py:156-212`; my independent
wedge-product enumeration confirmed it. The relation between this identity
and the simulated square coefficients is correct:

`Q = -(1/2) sum kappa [(Re P)^2 - (Im P)^2]`,

with `c_Re = -kappa/2` and `c_Im = +kappa/2`, as implemented at
`scripts/x2model.py:214-243`. The even/negative and odd/positive Kramers sign
rule is satisfied for all 64 nonzero channels.

### 1.2 HS transformation, trace weight, and updates

For each channel,

`exp(-dt W c O^2) = integral dphi exp(-phi^2/2) exp(a phi O)`

with `a = sqrt(2 dt W |c|)` for `c < 0` and `i` times that for `c > 0`.
This is exact for each square (`scripts/afqmc.py:3-18,112-120`). Products of
different channel, site, and kinetic factors introduce the stated Trotter
error. Reversing channel order on alternating slices
(`scripts/afqmc.py:143-165`) does not make the kinetic-interaction split a
fully symmetric second-order decomposition; a time-step extrapolation is
still required.

The low-rank vertex identity follows from `F_x F_x^T = rho I` and is correctly
implemented at `scripts/afqmc.py:179-216`. The ordinary d-frame trace weight
is `det(1+M_d)/sqrt(det M_d)`. Every kinetic and HS one-body generator here is
traceless, so every factor and hence `M_d` has determinant one. The denominator
is therefore exactly constant (one, apart from convention-independent positive
normalisation), so sampling `det(1+M_d)` is correct. This is the special
lambda1 = 0 situation anticipated by `SIGN1_REFEREE_REPORT.md:25-38`.

The pCN proposal

`phi' = sqrt(1-s^2) phi + s xi`

is reversible with respect to the standard Gaussian prior, so the Gaussian
prior ratio cancels and the Metropolis acceptance is `min(1, det-ratio)`.
The implementation at `scripts/afqmc.py:256-293` uses `u < r.real`; for an
exactly real nonnegative ratio this is equivalent because `u` is uniform in
`[0,1)` and ratios above one are accepted automatically. Proposal phases are
monitored and remain below the registered 1e-8 tolerance. Adaptation stops in
warm-up (`scripts/runner.py:86-95`). My dense recomputation confirmed both the
rank-32 determinant ratio and the Green-function update.

### 1.3 Validation gate

- Gate (i) passes: the free Green function agrees to 3.6e-15 in 1D and
  5.7e-14 in 2D (`scripts/validate_a_v2.out:1-2`).
- Gate (ii) passes at the sign-free-theorem level and in the numerical phase
  checks. Random prior-scale full weights have phase at most 5.3e-14
  (`scripts/validate_a_v2.out:12-16`), while the worst production proposal
  phase is 3.0e-9 (`scripts/runs/L6_f2_W8.log:8-18`). The production runner
  monitors ratios, not a fresh full determinant after every proposal
  (`scripts/runner.py:105-119`); positivity of full weights therefore also
  relies on the exact Kramers construction.
- Gate (iii) is scientifically confirmed but the supplied archival evidence
  is incomplete. The ED side is present (`scripts/ed_reduced_gate3.py:12-19`),
  and the long QMC logs show completed 12,000-sweep chains, but the corrected
  QMC `.npz` files and a saved corrected analysis table are missing; the logs
  do not print `WQc` or `E_kin`. My short rerun above independently reproduces
  the claimed ED agreement through the same engine and an independently built
  psi-frame ED comparator (`scripts/ed_exact.py:26-113`).
- Gate (iv) passes: the filter zeros exactly protect the light modes and the
  recorded per-configuration deviations are at most 1.8e-13 in the main runs
  (`scripts/runner.py:66-77`; `scripts/runs/readout_final.out:15-47`).

The engine is therefore adequate for this pilot. The determinant warnings are
poorly handled operationally—nonfinite ratios are silently rejected—but my
instrumented checks found no nonfinite proposal ratio at weak or strong L4 in
the tested sweeps. A production implementation should use `slogdet`/factored
ratios and count nonfinite proposals explicitly.

## 2. Observables and gap estimators

### 2.1 The 10-vector structure factor

The observable is correct. `R0 = F_s^T F_s` at
`scripts/afqmc.py:351-361` represents the spatial kernel of
`sum_x B_S^a(x)`, and `structure` computes

`S10 = (1/N) sum_a [<(sum_x X_x^a)^2> + <(sum_x Y_x^a)^2>]`

at `scripts/afqmc.py:380-404`. Consequently the reported `S10/N = S10/L^2`
is the volume-normalised squared uniform order parameter. It tends to a
nonzero constant under true long-range 10-vector order and scales as `1/N`
for a fixed finite correlation length. The free-Wick comparison with ED at
`scripts/validate_a_v2.out:3-5` independently validates its normalisation.

### 2.2 E1 and E2

The mirror correlator itself is correctly projected to the mirror corners
(`scripts/afqmc.py:362-368,439-443`). However, the analysis does not quite
follow the pre-registration's "averaged over the 32 components": the runner
saves the s-particle and c-hole blocks separately (`scripts/runner.py:66-70`),
and `scripts/analysis.py:110-117` fits only the s block. Averaging the two
blocks in my check leaves the W = 2 E2 result qualitatively unchanged, but the
reported observable should be described as the s-block propagator.

E1 is the registered long-time single-cosh estimator
(`PREREG.md:82-89,114-122`). It fails at strong coupling because the tail is
noise-dominated, and mechanically gives OPEN
(`scripts/runs/readout_final.out:49-54`).

E2 is not an admissible replacement for establishing the *lowest* spectral
gap. It fits down to tau = 0.4 with a single cosh
(`scripts/analysis.py:43-62`), precisely after the long-time signal has been
lost. For a positive multi-state spectrum, a finite-time effective decay
scale is generally controlled by higher-energy weight and approaches the
lowest supported energy from above. An arbitrarily small low-energy pole can
coexist with the reported E2 value. Thus the stable W = 2 numbers 2.61(13)
and 2.51(25) (`scripts/runs/readout_final.out:56-61`) are useful effective
decay scales, not lower bounds on the mirror gap.

### 2.3 E3 and E3w

For an exact Hamiltonian with a nonnegative, unit-normalised fermion spectral
function,

`G(tau) = integral d omega A(omega) exp(-tau omega)/(1+exp(-beta omega))`.

At `tau = beta/2`, the kernel is
`1/[2 cosh(beta omega/2)]`. Therefore, for
`w_E = integral_{|omega|<E} A(omega) d omega`,

`w_E <= 2 cosh(beta E/2) G(beta/2)`.

So the E3 inequality at `scripts/analysis.py:65-70` follows. It does **not**
show that the gap exceeds E: it only shows that less than the chosen amount
of spectral weight lies below E. A system with a nonzero but 1% residue at
zero energy has zero gap and passes the worker's `w_1 < 0.1` rule. E3 is
therefore inadmissible as the fixed reading's "gap open" test.

The stated E3w proof in `PREREG.md:207-214` contains a correction: the kernel
is not pointwise at least its midpoint value for every tau in `[0,beta]`.
For beta = 4 and `|omega| = 1`, it is 0.0489 at tau = 1 or 3 on one spectral
side, below the midpoint value 0.1329. The implemented *symmetric window
average* nevertheless satisfies the same bound, because paired points obey

`[K(beta/2-s,omega)+K(beta/2+s,omega)]/2
 = cosh(s omega)/[2 cosh(beta omega/2)] >= K(beta/2,omega)`.

Thus E3w's inequality is repairable for the symmetric grid used at
`scripts/analysis.py:73-78`, but E3w remains a low-weight bound rather than a
gap estimator. Negative central "bounds" in
`scripts/runs/readout_final.out:66-75` are statistical noise and should be
reported as one-sided limits respecting physical nonnegativity.

### 2.4 Declaration times

`PREREG.md:187-198` records E2 and E3 at 12:23Z, before any L6 run, and
`PREREG.md:207-214` records E3w at 12:40Z while L6 W = 2 was running and before
an L6 result was seen. This internal chronology is consistent with the driver
order in `scripts/runs_L6.sh:1-8` and with the first reported L6 readout only
at `PREREG.md:239-249`.

It is not independently timestamp-verifiable from the supplied packet. All
copied source, `.npz`, log, and readout files have the same filesystem
modification time (13:04:06 EDT, i.e. about 17:04Z), and NumPy's archive
members carry the conventional 1980 ZIP time. The run logs contain elapsed
times but no wall-clock start time. I therefore treat "declared before the L6
data" as documented provenance, not externally authenticated provenance. In
any event, temporal declaration does not cure the observable mismatch above.

## 3. Statistics

The main size ratios are reproduced:

| W | L6/L4 ratio of S10/N | Difference from short-range 4/9 | Difference from free 0.54 |
|---:|---:|---:|---:|
| 1 | 0.616(23) | 7.5 sigma | 3.3 sigma |
| 2 | 0.984(51) | 10.6 sigma | 8.7 sigma |
| 4 | 1.351(262) | 3.5 sigma | 3.1 sigma |
| 8 | 0.868(103) | 4.1 sigma | 3.2 sigma |

These are the worker's binned values at
`scripts/runs/readout_final.out:81-85`. Thus W = 2 very clearly distinguishes
the observed finite-size behaviour from a short-range or free-size ratio.
W = 4 is noisy but does not drive that conclusion; its L6 history contains
large excursions (`scripts/runs/L6_f2_W4.log:11-16`). W = 8 also favours the
flat/long-correlation regime, though less decisively.

The quoted errors are plausible pilot errors, not publication-grade
uncertainties:

- Twenty bins mean only 2 sweeps per L6 bin and 3 per L4 bin. The binning code
  discards the remainder (`scripts/analysis.py:10-22`): it uses the first 40
  of 45 L6 sweeps and, for the 30-sweep dtau check, only the first 20. The
  all-sweep central values do not change the main ratios materially, but this
  is an avoidable analysis defect.
- The `tau_int <= 1.3` statement is a crude estimate from only 45-60 values,
  with a floor of 0.5 and an automatic Sokal window
  (`scripts/autocorr.py:7-22`; `scripts/runs/autocorr_final.out:7-27`). It does
  not exclude slow order-parameter-direction or metastable modes. There are no
  independent production chains.
- The L4 W = 2 thirds drift upward (approximately 2.94, 3.12, 3.64 in S10/N),
  while the L6 thirds drift oppositely (3.42, 3.15, 3.10). Larger block errors
  remain small enough that the W = 2 rejection of a 0.44-0.54 ratio is robust,
  but the nominal 0.98(5) precision should not be read as a controlled
  thermodynamic extrapolation.

## 4. Time-step, temperature, and phase interpretation

The finite-time-step theory explicitly selects Spin(8) x U(1)c through the
ordered Fierz factors. At W = 2, halving dtau changes L4 S10/N from 3.23 to
3.60 and restores the charged-plane fraction from 0.60 to 0.21, but the L6
charged-plane fraction remains about 0.85
(`PREREG.md:239-249,251-263`). Using all saved measurements, the dtau = 0.05
L6 central value is about 4.28 rather than 4.11; either value still gives a
flat-or-growing L6/L4 ratio. Hence the large total correlation is not created
solely by the L4 pinning, but no dtau-to-zero extrapolation exists and the L6
anisotropy is unresolved.

At beta = 4 this is a finite-temperature 2D short-range system. The
Mermin-Wagner theorem forbids true spontaneous breaking of continuous
Spin(10) in the exact-symmetry thermodynamic limit. The data can therefore
show only a finite-size broken-regime crossover or a large correlation
length, not a condensate phase at this temperature.

Moreover, `S(0)` at only L = 4 and 6 does not quantitatively lower-bound the
correlation length. A second-moment estimate would require at least
`S(q_min)`; the saved secondary observable is at `(pi,pi)`, not the smallest
nonzero momentum. "xi at least about 6" is a reasonable scaling heuristic,
but not a measured bound. The defensible statement is that the data are
consistent with correlations extending across the largest simulated box and
are inconsistent with the free/clearly short-range size scaling at W >= 2.

## 5. Fixed reading

The fixed alternatives at `TESTS.md:335-338` require an open mirror gap before
classifying the size dependence of S10/L².

- **Not SMG-PILOT:** W = 1 is the only main point with a clearly decreasing
  S10/L², and its registered gap is not open. No estimator finds an
  open-and-decreasing point.
- **Not GPR-PILOT:** E1 finds no coupling with a resolved open gap at both
  sizes. E2 supplies a high/finite-time effective decay scale, and E3/E3w
  supply low-energy-weight limits; none excludes a low-residue gapless pole.
- **OPEN:** the sizes convincingly establish strong, box-spanning 10-vector
  correlations once the propagator becomes strongly suppressed, but they do
  not establish the required lowest single-particle gap with the registered
  estimator or a logically equivalent replacement.

This is OPEN because the gap measurement fails, not because the validation
gate or sign-free construction fails.

### Repair target

**Issue:** the long-time mirror correlator is below the noise floor, while the
replacement estimators do not determine the lower spectral edge.

**Why this blocks:** both GPR-PILOT and SMG-PILOT require an open mirror gap;
small low-energy spectral residue is enough to invalidate that premise.

**Repair target:** obtain longer independent chains and a correlator with
substantially improved long-time signal; fit a positive multi-state spectral
model with a reported covariance/goodness-of-fit and an explicit lower-edge
sensitivity test; average the registered 32 components; repeat at several
beta and dtau values; and measure `S(q_min)` for a second-moment correlation
length. A direct spectroscopy estimator insensitive to small residue would be
preferable.

**Claim boundary until fixed:** the calculation establishes a validated
sign-free pilot and strong finite-size 10-vector correlations, but not mirror
mass generation or its GPR/SMG mechanism.

## 6. Side claims

### 6.1 Sector factorisation

The factorisation is correct with a narrower scope than the shorthand "in
2D": it holds on the even periodic bipartite square lattice, for f2 or the
on-site filter, after changing to the exact sign-correct singlet-only Fierz
point `(1.25, 0, 0.25, 0)`. The operator

`J_d = (-1)^(x+y) sigma_z tensor diag(+1_s,-1_c)`

commutes with every slice and is reversed by T2, so the two J sectors are
complex conjugates and `det(1+M) = |det(1+M_+)|^2`. The numerical checks at
`scripts/check_sector.py:16-43` and `scripts/check_sector.out:7-12` agree to
1e-10. It does not apply to the production triplet vertex, and the production
runs did not use it (`REPORT.md:118-125`).

### 6.2 Spin(8) gauge links

The algebraic claim is sound as a construction proposal. With real Cl(9)
gammas, Spin(8) generated by products of directions 1-8 is real and commutes
with Gamma9. Such links preserve the particle-hole split, K conjugation, and
T2; a gauge-covariant filter still has `F_x F_x^dag = rho I`. With the stated
embedding this contains colour, B-L, and one SO(2), but not the full weak group
or hypercharge (`REPORT.md:205-209`). This is not a simulated result, and the
absence of a G_SM-invariant real 2-plane rules out this fixed-plane
construction for arbitrary G_SM links, not every conceivable sign-free
formulation.

### 6.3 Cost model

The table is arithmetically consistent with the stated one-point calibration
`T = a N_d^3 L_tau`, `a = 4.86e-10`, using the measured 29.7 seconds per L6
sweep (`scripts/cost_model.py:13-28`; `scripts/cost_model.out:1-12`). It is an
order-of-magnitude hardware/code projection, not a scaling benchmark. The
factor-of-eight sector saving is the asymptotic cubic gain from halving matrix
dimension; it is not measured and ignores the singlet vertex's doubled
channel count and noncubic overhead. The 3-10x gauge-link penalty and claims
about tuned/GPU performance remain estimates (`REPORT.md:201-210`).

## Strongest correct statement

For the ungauged 2+1D f2-filtered lambda1 = 0 X2 analogue at beta = 4, the
worker has built a correctly sign-free AFQMC with an exact 64-channel Fierz/HS
representation, valid pCN determinant sampling, exact light-corner
decoupling, and independently reproduced small-system ED validation. On L = 4
and 6, strong coupling sharply suppresses the mirror propagator and changes
the volume-normalised uniform 10-vector structure-factor ratio from 0.616(23)
at W = 1 to 0.984(51), 1.351(262), and 0.868(103) at W = 2, 4, and 8, which is
consistent with correlations spanning the largest box and is incompatible
with plainly short-range/free scaling at those sizes. Because the registered
long-time gap fit fails, the substitutes do not exclude a low-residue gapless
mode, finite-dtau pinning is large, and finite-temperature Mermin-Wagner
forbids true continuous order, the result is suggestive of a GPR-like
crossover but does not establish either GPR mass generation or SMG; the fixed
reading is OPEN.
