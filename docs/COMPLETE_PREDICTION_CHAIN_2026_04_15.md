# Complete Prediction Chain: Cl(3) on Z^3

**Type:** bounded_theorem
**Claim type:** bounded_theorem


**Date:** 2026-04-15
**Status:** support - inventory of the prediction chain composed of upstream proposed and audited rows; this row is not itself a strong derivation claim independent of those upstream rows
**Scripts:** `scripts/frontier_complete_prediction_chain.py`,
`scripts/frontier_yt_zero_import_chain.py`, `scripts/frontier_yt_color_projection_correction.py`,
`scripts/frontier_higgs_mass_stability.py`, `scripts/frontier_higgs_mass_corrected_yt.py`,
`scripts/frontier_higgs_buttazzo_calibration.py`, `scripts/frontier_color_projection_mc.py`
**Historical support scan:** `scripts/frontier_yt_ew_coupling_derivation.py`
**Audit dependency note:** this support inventory depends on upstream rows
including
[ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md](ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md),
[RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md),
[YT_EW_COLOR_PROJECTION_THEOREM.md](YT_EW_COLOR_PROJECTION_THEOREM.md),
[YT_COLOR_PROJECTION_CORRECTION_NOTE.md](YT_COLOR_PROJECTION_CORRECTION_NOTE.md),
[YT_QFP_INSENSITIVITY_SUPPORT_NOTE.md](YT_QFP_INSENSITIVITY_SUPPORT_NOTE.md), and
[HIGGS_MASS_FROM_AXIOM_NOTE.md](HIGGS_MASS_FROM_AXIOM_NOTE.md). Audit status
and retained-grade reuse are pipeline-derived from those dependencies, not
from this inventory prose.

**Hierarchy formula honest-status note (2026-05-10):** The package-level
"DERIVED" rhetoric on the `v` row in §3.2, §5.2, §8.3, §9, §11, and
§12 has been corrected to "BOUNDED NUMERICAL MATCH (closure path open)"
to match the per-route hierarchy notes (which already use bounded
vocabulary correctly) and the YT UV-to-IR transport master obstruction
theorem (which already names the non-perturbative `α_LM^{16}` factor
as outside retention scope by design). See
[HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
for the four open primitives P1-P4 and the branch-local route search
record.



## Current reproduction boundary (2026-10-04)

The submitted 19,840-configuration, `6^4`, mass-scan and campaign-HMC
numbers below are **historical reported results whose raw data/code are not
provided here**. They are not reproduced by the current runner and cannot
support its PASS. The current own-code run uses three chains of 500 samples,
discarding ten per chain (1,470 retained), gauge PBC and fermion time APBC on
`4^4`, at mass 0.1. Its finite covariance and rooted reweighting diagnostics
have the printed overlap/ESS limits; they are not certified dynamical,
infinite-volume or physical-VEV predictions. The `Ns=0` linear response is
not a controlled `Ns=1` extrapolation and does **not** bracket the campaign HMC.
Exactly at fourth hopping order, `ln det(m+K)` contains
`[sum_p Re Tr U_p - sum_lines s_mu Re Tr P_line]/(8 m^4)` on `L=4`.
The local plaquette coefficient is positive in the heavy-mass expansion;
the winding term and higher orders prevent an all-mass monotonicity conclusion.
The expansion is not justified by mass 0.1. The degree 16 counts block
Grassmann components; its interpretation as `4 spin x 4 taste` uses the
supplied staggered realization, not a derived physical species census.
Only the three hash-bound April ensemble files and the current finite controls
are reproducible evidence here. All campaign-derived 214 GeV and taste-count
readouts below are arithmetic on unverified reported inputs. The replacement
of a pure-gauge measure by a physical matter-inclusive one remains open.

## Landing correction to the comparator (2026-10-04)

The common-scale diagnostic uses four-loop mass/coupling running with
explicit **two-loop** bottom-threshold coupling and strange-mass matching:
`m_s^(4)(mb) = [1 + (89/432)(alpha_s^(5)(mb)/pi)^2] m_s^(5)(mb)`.
It is a mixed-truncation diagnostic, not a fully matched four-loop prediction;
three-loop decoupling and truncation/systematic uncertainties remain open.
The earlier precise numbers below omitted strange-mass matching and are
superseded by the corrected runner. The mismatch remains about 19%.
The quoted PDG-2024 quark-mass errors are **90% confidence halfwidths**;
combining them with the 68% coupling error in quadrature measures sensitivity,
not a one-sigma significance or a joint statistical rejection. Any “16 sigma”
reading below is withdrawn. Ratio scale invariance applies to a common,
fixed-flavour, mass-independent QCD theory. The SM example only checks its
sampled scales in a supplied truncated one-loop flow (fixed tau Yukawa,
imported initial data, no threshold matching); it supplies no all-scale bound.
Mixed-scale root fits are restricted to the bracket `[1.3,8] GeV`; a root below
that bracket is not evaluated without charm matching.
Source for decoupling conventions: [RunDec, Eqs. 20 and 28](https://arxiv.org/pdf/hep-ph/0004189).
No framework coefficient, exponent or scale is derived by this comparison.

## Corrigendum (2026-09-30)

**What was wrong.** Section 11.3 says the bounded `5/6` bridge gives
`V_cb = (m_s/m_b)^{5/6}` "to `0.23%` on the threshold-local self-scale
comparator". That comparator divides the strange mass at 2 GeV by the bottom
mass at its own mass. The ratio of two MS-bar masses at one energy is
energy-independent, so the scale-consistent test is at one common scale. With
four-loop QCD running and PDG 2024 inputs (`m_s(2 GeV) = 93.5(8) MeV`,
`m_b(m_b) = 4.183(7) GeV`, `alpha_s(M_Z) = 0.1180(9)`) the bridge prediction
misses `m_s(m_b)/m_b(m_b) = 0.018878` by `+18.6% +- 1.2%` (about 16 sigma with
PDG errors, atlas `|V_cb|` taken as exact; `+16.9%` to `+20.4%` across standard
input sets). The exponent that fits is `0.7975`, not `5/6`.

**Corrected statement.** The `0.23%` is a mixed-scale convention coincidence and
is not evidence for the bridge; the Section 11.3 clause "full bridge/scale
closure remains open" stands and is understated. Other rows of this inventory
are not affected by this correction. The status of this note is unchanged; audit
status remains with the independent audit lane. Full table and evidence:
`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md` (Corrigendum).


## Corrigendum (2026-09-30): the single computed input is the pure-gauge plaquette, and the `v` match is not a physical agreement

A same-family check from the 2026-09-29 wall campaign, reproduced by the spot
check in `scripts/frontier_hierarchy_taste_in_plaquette_measure_spot_check.py`
(details and numbers in the 2026-09-30 corrigendum of
`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`), found two scope errors in
how this inventory presents the plaquette and the `v` row. No status label
here changes and no audit field is touched.

- **The plaquette has no fermions in its measure.** Section 2 calls
  `<P> = 0.5934` "the unique output of the axiom's own dynamics" and an
  evaluation on "the SU(3) gauge theory that Cl(3) on Z^3 generates". It is the
  pure-gauge Wilson plaquette at `beta = 6`, with no dynamical matter. The same
  chain uses a staggered fermion block (taste count, staircase, Ward identity,
  the vacuum-polarization channel behind the vertex power), whose modes the
  plaquette measure leaves out. With one dynamical staggered field (4 tastes) on
  a `4^4` lattice the plaquette at `beta = 6` rises by about `+0.02` (campaign
  HMC `+0.0212(11)`; own re-weighting `+0.0062(2)` for 1 taste and `+0.012(1)`
  for 2), and the hierarchy readout falls from 246.28 GeV to about 214 GeV (about
  227 to 236 GeV for 1 to 2 tastes). The statements "the `+0.0255 %` match is
  real and robust on the canonical surface" (Sections 3.2, 8.5 and 9; the same
  figure appears in 11.6 and 12) therefore hold for the pure-gauge value only. They are not an agreement of the
  framework with the observed VEV, and the `BOUNDED` label on the `v` row is the
  correct reading. Small lattice, same-volume difference, rooting and the
  infinite-volume shift not run.
- **The licensed number is a reuse number, not a certified Monte Carlo value.**
  Sections 2, 11.4 and 12 say the plaquette is "computed ... by lattice MC".
  The chain carries the licensed `0.5934` (admitted reuse number, see
  `PLAQUETTE_SELF_CONSISTENCY_NOTE.md`). Point estimates of the same quantity:
  `0.59369(2)` from the repository's own April 2026 ensembles
  (`outputs/alpha_s_wilson_loop_production/`) and `0.59372(4)` from a reduced
  wall-campaign run; both about `3e-4` above `0.5934`, no certificate issued. At
  `0.59369` the `v` readout is 245.80 GeV (`-0.195 %`) and `alpha_s(v)` is
  0.103279 instead of 0.103304, so the `+0.0255 %` residual changes sign; the
  shift is inside the `+/- 0.0006` that `YT_ZERO_IMPORT_CHAIN_NOTE.md` quotes for
  the plaquette. If
  the fermion-inclusive plaquette above were used, `alpha_s(v)` would be about
  0.1015 (`-1.7 %`, illustrative arithmetic `1/(4 pi sqrt(P))`). The other rows
  (`m_t`, `sin^2 theta_W`, `1/alpha_EM`, `y_t`, `m_H`) are not recomputed here and
  are not asserted unchanged.

Still standing: the inventory role of this note, the `BOUNDED` label on `v`, and
the open primitives P1 to P4.

---

## 1. Framework Statement

This inventory starts from the proposed Cl(3) on Z^3 framework and records
conditional readouts. It also uses the admitted scales, normalizations,
readout coefficients, matter realization, schemes and thresholds listed below;
this inventory does not derive those inputs from that starting statement.

---

## 2. The Supplied Plaquette Surface

The package uses `<P> = 0.5934`, the declared pure-gauge Wilson beta=6 reuse
value. It is not a certified new Monte Carlo determination or the unique
output of a physical matter-inclusive measure. The September30 and October4
corrections above preserve the independent ensemble comparisons and the
unverified campaign boundary. Subsequent arithmetic is conditional on this
value and on the separately supplied inputs; it does not establish the
physical VEV match.

## 3. Conditional Infrastructure

### 3.1 From the plaquette

| Quantity | Formula | Value | Status |
|----------|---------|-------|--------|
| u_0 | <P>^{1/4} | 0.8776 | Algebra on supplied P |
| alpha_LM | alpha_bare / u_0 | 0.09066 | Supplied coupling-map convention |
| alpha_s(v) | alpha_bare / u_0^2 (CMT, n_link = 2) | 0.1033 | Conditional n_link=2 physical map |
| alpha_LM^2 | alpha_bare alpha_s(v) | 0.00822066 | Exact identity under supplied definitions |

The package imports the CMT mean-field map and declares g_bare = 1. Its
identification with a physical coupling at scale v is an upstream premise.
With n_link = 2 (one gauge link per vertex leg): alpha_s(v) = 1/(4 pi u_0^2).
The intermediate coupling is therefore the exact geometric mean:
alpha_LM^2 = alpha_bare alpha_s(v).

### 3.2 From Cl(3) algebra and Z^3 lattice geometry

| Quantity | Value | Origin | Status |
|----------|-------|--------|--------|
| Gauge group | SU(3) x SU(2) x U(1) | Z_3 clock-shift, Z_2 bipartite, edge phases | Upstream structural premise; not independently closed here |
| Generations | 3 | BZ orbit decomposition: 8 = 1+1+3+3 | Upstream structural premise; not independently closed here |
| g_3^2(bare) | 1 | Z_3 clock-shift algebra | Upstream structural premise; not independently closed here |
| g_2^2(bare) | 1/(d+1) = 1/4 | Supplied upstream normalization at d=3 | Conditional input |
| g_Y^2(bare) | 1/(d+2) = 1/5 | Supplied upstream normalization at d=3 | Conditional input |
| N_taste | 16 | 2^4 BZ corners in 4D (staggered) | Upstream structural premise; not independently closed here |
| beta coefficients | b_1 = 41/10, b_2 = -19/6, b_3 = -7 | Group theory of derived gauge + matter content | Upstream structural premise; not independently closed here |
| v | M_Pl * (7/8)^{1/4} * alpha_LM^16 = 246.28 GeV | Hierarchy formula (taste-determinant route) | BOUNDED NUMERICAL MATCH |

The hierarchy formula carries the same-surface plaquette/coupling-chain
match between `M_Pl × (7/8)^{1/4} × α_LM^{16}` and PDG `v_obs = 246.22 GeV`
at relative deviation `+0.0255 %`. The residual is arithmetic at the declared pure-gauge reuse value (and
changes under the plaquette alternatives above); the underlying formula carries four named
load-bearing primitives (M_Pl import; Wick rotation Z³ → Z⁴ for the 4D
taste count `2^4 = 16`; the algebraic substitution `u_0^{16} → α_LM^{16}`;
EWSB observable identification) that have not been derived from the
physical Cl(3) local algebra plus Z^3 spatial substrate.
Per-route hierarchy notes
([HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md),
[HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md](HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md),
[HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md](HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md),
[HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md](HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md),
[OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md))
are bounded; the YT UV-to-IR transport master theorem
([YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md](YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md)
§3.2) already names the non-perturbative `α_LM^{16}` factor as outside
the current retention scope by design. The package-level rhetoric
demotion is documented in
[HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md);
closure path open.

---

## 4. The Color Projection (R_conn = 8/9)

### 4.1 Exact channel fraction and open physical matching

`F_adj = (N_c^2-1)/N_c^2 = 8/9` is the exact dimension fraction in
`N_c tensor conjugate(N_c) = 1 + adj` at N_c=3. Under the separately stated
isotropic/gauge-orbit averaging prescription it also appears as a normalized
channel average. Neither fact fixes the channel weight of an arbitrary
physical correlator. Large-N counting or OZI suppression does not select an
exact disconnected-channel coefficient at N_c=3.

The supplied physical readout families are
`K_EW(kappa_EW)=1/(8/9+kappa_EW/9)` and
`K_Y(kappa_Y)=8/9+kappa_Y/9`. The choices kappa=0 and kappa=1 share the
channel arithmetic but give different normalizations. Thus the packet does
not select either physical coefficient. See the explicit boundaries in
RCONN_DERIVED_NOTE and YT_COLOR_PROJECTION_CORRECTION_NOTE; no new selector
or error bound is supplied here.

### 4.2 Historical connected-trace consistency check

    R_conn(MC) = 0.887 +/- 0.008
    R_conn(derived) = 8/9 = 0.88889
    Agreement: 0.2% (within 0.9% statistical error)

Script: `scripts/frontier_color_projection_mc.py` (4^4 lattice, 100 configs, Cabibbo-Marinari). This reported comparison does not derive a physical selector or certify a general 1/N_c remainder bound.

### 4.3 What R_conn corrects

The historical specializations rescale two supplied readouts:

| Coupling | Color channel | Correction | Direction | Physics |
|----------|---------------|------------|-----------|---------|
| g_EW (g_1, g_2) | Adjoint | * sqrt(K_EW(kappa_EW)); `sqrt(9/8)` only at `kappa_EW=0` | UP at connected-trace specialization | EW vacuum polarization readout depends on named `kappa_EW` coefficient |
| y_t | Supplied scalar readout | * sqrt(K_Y(kappa_Y)); sqrt(8/9) at kappa_Y=0 | DOWN at kappa_Y=0 | Scalar matching coefficient remains open |

At the stated specializations the factors have the displayed directions.
Color dimensions alone do not select those specializations. A common
multiplicative factor on both EW couplings cancels exactly from
sin^2(theta_W); that cancellation does not fix the absolute normalization.

### 4.4 What R_conn = 8/9 unlocks

| Observable | How R_conn enters | Effect |
|------------|-------------------|--------|
| g_1(v), g_2(v) | `sqrt(K_EW(kappa_EW))` on EW couplings; `sqrt(9/8)` only at `kappa_EW=0` | Conditional absolute normalization |
| sin^2(theta_W) | Ratio invariant (cancels) | Preserved exactly |
| y_t conditional readout | sqrt(K_Y(0)) on Ward y_t | Historical kappa_Y=0 comparator |
| taste_weight | 7/18 = (7/8) * T_F * (8/9) | Enters taste threshold running |
| m_H | Through corrected y_t in CW stability prediction | Shifts m_H by ~25 GeV |

Downstream values depend on the supplied readout choices and transport
premises; the exact channel fraction does not derive those choices.

---

## 5. Electroweak Predictions

### 5.1 EW coupling derivation

The supplied bare normalizations g_2^2 = 1/4, g_Y^2 = 1/5 are run from M_Pl to v through
the taste threshold staircase:

- 16 BZ corner tastes with Hamming weight k = 0,...,4 decouple at
  mu_k = alpha_LM^{k/2} * M_Pl in a 4-segment staircase
- Each segment has effective beta coefficients shifted by n_extra * taste_weight
- taste_weight = (7/8) * T_F * R_conn = 7/18

After staircase running, the EW color projection is written as
`K_EW(kappa_EW)=1/(8/9+kappa_EW/9)`. The historical `sqrt(9/8)` coupling
factor is the connected-trace specialization `kappa_EW=0`.

### 5.2 Prediction table

| Observable | Derivation | Predicted | Observed | Deviation |
|-----------|-----------|-----------|----------|-----------|
| v | Hierarchy formula (BOUNDED NUMERICAL MATCH; per-route notes bounded; see HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10): M_Pl * (7/8)^{1/4} * alpha_LM^16 | 246.28 GeV | 246.22 GeV | +0.03% |
| alpha_s(M_Z) | same-surface plaquette chain + one-decade running bridge from `v` | 0.1181 | 0.1179 | +0.14% |
| sin^2(theta_W)(M_Z) | bare geometry + taste staircase + exact Fierz fraction + conditional `kappa_EW` matching + running bridge | 0.2306 at `kappa_EW=0` | 0.2312 | -0.26% |
| 1/alpha_EM(M_Z) | conditional `g_1, g_2` package after color projection + running bridge | 127.67 at `kappa_EW=0` | 127.95 | -0.22% |
| g_1(v) | staircase + connected-trace `sqrt(K_EW(0)) = sqrt(9/8)` specialization | 0.4644 at `kappa_EW=0` | 0.4640 | +0.08% |
| g_2(v) | staircase + connected-trace `sqrt(K_EW(0)) = sqrt(9/8)` specialization | 0.6480 at `kappa_EW=0` | 0.6463 | +0.26% |

These are historical comparator readouts on the declared package, including
kappa_EW=0. Agreement thresholds do not verify the missing physical maps,
selectors or the matter-inclusive VEV; no fresh execution is asserted here.

---

## 6. Top Quark Mass

### 6.1 Derivation chain

**Step 1: Ward identity at M_Pl.**

    y_t(M_Pl)_lattice = g_lattice / sqrt(6) = sqrt(4 pi alpha_LM) / sqrt(6) = 0.4358

This follows from SU(3) color-flavor locking on the lattice, where the Yukawa
vertex shares the gauge vertex with a 1/sqrt(6) Clebsch-Gordan coefficient.

**Step 2: Ward matching correction.**

    Delta = +0.02 (1-loop lattice-to-MSbar matching)

This is a perturbative, UV, scheme-dependent correction from Brillouin zone
sunset integrals over the staggered fermion action. It does not enter at the
current 2-loop level of the backward Ward scan.

**Step 3: Backward Ward scan.**

2-loop SM RGE from v to M_Pl, matching the Ward boundary condition:
y_t(v) such that y_t(M_Pl) = 0.4358. The reported QFP scan is a
UV-boundary sensitivity diagnostic on its supplied flow, not a general
higher-order error bound. Historical result:

    y_t(v) [Ward, uncorrected] = 0.9732

**Step 4: Color projection correction.**

    y_t(physical) = y_t(Ward) * sqrt(8/9) = 0.9732 * 0.9428 = 0.9176

This line assumes kappa_Y=0 in y_t(Ward)*sqrt(K_Y(kappa_Y)).
The physical scalar normalization/selector is not derived by the channel
fraction. The square-root power is part of the supplied one-leg readout.

**Step 5: MSbar-to-pole conversion.**

2-loop QCD conversion from MSbar mass to pole mass:

    m_t(MSbar, mu=v) = y_t(phys) * v / sqrt(2) = 159.79 GeV
    Run to mu = m_t:  m_t(MSbar, mu=m_t) = 163.01 GeV
    R_2loop = 1 + (4/3) alpha_s/(pi) + K_2 (alpha_s/pi)^2 = 1.0591
    m_t(pole) = m_t(MSbar) * R_2loop = 172.57 GeV

### 6.2 Results

| Quantity | Predicted | Observed | Deviation |
|----------|-----------|----------|-----------|
| y_t(v) [corrected] | 0.9176 | ~0.917 (SM extraction) | +0.06% |
| m_t(pole, 2-loop) | 172.57 GeV | 172.69 GeV | -0.07% |
| m_t(pole, 3-loop) | 173.10 GeV | 172.69 GeV | +0.24% |

**Conditional y_t comparison.** The displayed0.9176 and pole-mass values use
the supplied Ward boundary, running/matching choices and kappa_Y=0. Their
proximity to the supplied experimental comparators does not close the
physical Yukawa matching gate. Averaging different loop orders is not an
independent uncertainty estimate.

### 6.3 Improvement from color projection

| Quantity | Before (y_t = 0.973) | After (y_t = 0.918) | Improvement |
|----------|---------------------|---------------------|-------------|
| m_t(pole, 2-loop) deviation | +5.52% | -0.07% | +5.45 pp |
| m_H(2-loop) deviation | +13.08% | -4.37% | +8.71 pp |

The table records the reported effect of the chosen kappa_Y=0
specialization. It does not establish its physical selection, independence
from comparator-informed choices, or a certified error budget.

---

## 7. Higgs Mass

### 7.1 Derivation chain

**Step 1: Supplied Higgs-sector identification.** The package identifies
the physical Higgs with a color-singlet taste condensate and adopts no
tree-level quartic. That physical identification is an open premise here.

**Step 2: Coleman-Weinberg boundary condition.** lambda(M_Pl) = 0 is the
CW boundary condition: the Higgs potential is purely radiative in origin.
Here lambda(M_Pl)=0 is a supplied boundary condition. The identification
of a taste-condensate model with the physical Higgs sector is not established
by this inventory.

**Step 3: Conditional SM RGE running.** With the supplied y_t = 0.918 and
EW readouts, run lambda from M_Pl to v using 2-loop (and dominant 3-loop)
SM beta functions. lambda(v) is determined by the running, yielding
m_H = sqrt(2 lambda) * v.

### 7.2 Results at each loop order

| Level | m_H (GeV) | vs 125.25 GeV |
|-------|-----------|---------------|
| 1-loop | 127.95 | +2.2% |
| 2-loop | 119.77 | -4.4% |
| 2+3-loop (partial) | 120.30 | -4.0% |
| Historical full-3-loop label (not reproduced; §7.3) | 125.10 | Historical -0.12% |

The partial three-loop implementation omits terms and is not a complete
three-loop calculation. The historical 125.10 GeV entry is hardcoded in the
synthesis runner, not recomputed there.

### 7.3 Calibration consistency and supplied boundary

The cited calibration runner prints
`129.6 + 1.5*(m_t-173.34)/0.76 - 0.5*(alpha_s-0.1184)/0.0007` GeV.
Substitution of this note's 172.57 GeV and 0.1181 gives 128.2945 GeV,
not 125.10 GeV. This arithmetic does not run the full RGE or establish which
historical input set produced 125.10. That value and its old 0.12% comparison
are retained above as history, not as a reproduced full-three-loop result.
The parametric stability-boundary fit is an imported calibration conditional
on its boundary, matching conventions and input values; imposing a related
boundary in the SM is not an independent framework prediction.

### 7.4 Sampled vacuum-stability diagnostic

The cited runner samples 2000 points of a numerically integrated, truncated
RGE trajectory with supplied initial data, thresholds and the boundary
lambda(M_Pl)=0. Positivity on those sampled points, when obtained, is a
property of that diagnostic. It is not a certified all-scale bound or a
physical absolute-stability theorem. Changes in matching, missing terms,
Yukawa normalization and inputs remain material uncertainties. The historical
SM crossing-scale comparison likewise belongs to that supplied truncated
trajectory, not a universal assertion about the SM.

### 7.5 Alternative route: direct formula

From the taste-sector generating functional (HIGGS_MASS_FROM_AXIOM_NOTE):

    m_H = v / (2 u_0) = 246.22 / (2 * 0.8776) = 140.3 GeV  (+12.0%)

The parent HIGGS_MASS_FROM_AXIOM_NOTE defines this as a symmetric-point
curvature readout, not the broken-phase Higgs pole. The supplied external v,
channel assignment and physical matching remain explicit. Historical finite
spacing comparisons do not prove continuum convergence to the Higgs mass or
that the 12% gap is closed.

## 8. Import Audit

Every ingredient in the prediction chain, with its status:

### 8.1 Axioms

| Ingredient | Value | Source |
|------------|-------|--------|
| Cl(3) on Z^3 | axiom | Starting postulate |
| N_c = 3 | 3 | Cl(3) spatial dimension |
| d = 3 | 3 | Spatial dimensions from Cl(3) |
| M_Pl | 1.221 x 10^19 GeV | Framework UV cutoff |
| g_bare = 1 | 1.0 | Cl(3) canonical normalization |

### 8.2 Declared pure-gauge reuse input

| Ingredient | Value | Source |
|------------|-------|--------|
| <P> | 0.5934 | SU(3) plaquette at beta = 6 |

The 0.5934 value is the admitted reuse input described in the corrigendum.
F_adj=8/9 is channel arithmetic; physical readout weights remain separate.

### 8.3 Conditional algebra and reported running readouts

| Ingredient | Value | Source |
|------------|-------|--------|
| u_0 | 0.8776 | <P>^{1/4} |
| alpha_LM | 0.09066 | alpha_bare / u_0 |
| alpha_s(v) | 0.1033 | CMT: alpha_bare / u_0^2 |
| alpha_LM^2 | 0.00822066 | alpha_bare alpha_s(v) |
| v | 246.28 GeV | Hierarchy formula (BOUNDED NUMERICAL MATCH; HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10) |
| F_adj | 8/9 | Exact channel dimension fraction; physical matching separate |
| SU(3) x SU(2) x U(1) | -- | Cl(3) algebra |
| 3 generations | -- | BZ orbit decomposition |
| g_3^2(bare) = 1 | 1.0 | Z_3 clock-shift |
| g_2^2(bare) = 1/4 | 0.25 | Supplied upstream normalization |
| g_Y^2(bare) = 1/5 | 0.20 | Supplied upstream normalization |
| taste_weight | 7/18 | (7/8) * T_F * R_conn |
| g_1(v) | 0.4644 | Bare + taste staircase + color projection |
| g_2(v) | 0.6480 | Bare + taste staircase + color projection |
| b_1, b_2, b_3 | 41/10, -19/6, -7 | Group theory of derived gauge + matter |
| beta_{y_t} coefficients | -- | SU(3) x SU(2) x U(1) Casimirs |
| beta_lambda coefficients | -- | Gauge + Yukawa group theory |
| Ward BC: y_t(M_Pl) | 0.4358 | g_lattice / sqrt(6) |
| y_t(v) [Ward] | 0.9732 | Backward Ward + 2-loop RGE |
| y_t(v) [conditional] | 0.9176 | Ward * sqrt(K_Y(0)); selector open |
| lambda(v) [CW] | CW-determined | lambda(M_Pl) = 0 + RGE running |
| m_t(pole, 2-loop) | 172.57 GeV | MSbar-to-pole conversion |
| m_t(pole, 3-loop) | 173.10 GeV | MSbar-to-pole conversion |
| alpha_s(M_Z) | 0.1181 | 2-loop QCD running from v |
| sin^2(theta_W)(M_Z) | 0.2306 | EW running from v |
| 1/alpha_EM(M_Z) | 127.67 | EW running from v |
| m_H (2-loop) | 119.8 GeV | lambda(M_Pl) = 0 + 2-loop RGE |
| m_H (historical label: full 3-loop) | 125.10 GeV | Not reproduced by displayed calibration inputs; see §7.3 |

### 8.4 Infrastructure (threshold matching only)

| Ingredient | Value | Role |
|------------|-------|------|
| m_b(MSbar) | 4.18 GeV | Threshold for v-to-M_Z running |
| m_c(MSbar) | 1.27 GeV | Threshold for v-to-M_Z running |
| m_t(pole) | 172.69 GeV | Threshold for v-to-M_Z running |

These affect ONLY the v-to-M_Z cross-check transfer. They do NOT enter
the v-scale predictions. The m_t = 172.57 GeV prediction is independent
of these values. They are standard SM quark masses used for the
conventional running between v and M_Z.

### 8.5 Status summary

The v-scale package already depends on supplied normalizations, Ward/readout
and hierarchy premises. Threshold masses additionally enter the stated
transfer calculations; this inventory supplies no zero-import closure.

**Honest qualifier on `v` itself.** The hierarchy formula
`v = M_Pl × (7/8)^{1/4} × α_LM^{16} = 246.28 GeV` is a **bounded
numerical match** on the canonical surface (per
[HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md);
see §11.6 below). It rides on `M_Pl` from the Planck lane (admitted UV
import; the framework anchors `M_Pl` via Wald-Noether matching, itself
`audited_conditional`), on a Wick rotation `Z^3 → Z^4` for the 4D
taste count `2^4 = 16` not derived from the Z^3 spatial substrate, on
the algebraic substitution `u_0^{16} → α_LM^{16}` not derived as a
determinant identity, and on the lattice → SM-Higgs-VEV observable
identification. The +0.0255 % is a residual at the declared reuse value,
not a certified physical agreement; this package does not
supply a framework derivation of `v = Λ × α^N` for integer `N`.

---

## 9. The Key Theorems

**Supplied Coupling Map (CMT).** The package adopts the mean-field map
and its physical identification at scale v: alpha_s(v) = alpha_bare / u_0^{n_link}.
With n_link = 2, this gives alpha_s(v) = 0.1033.

**Hierarchy Formula (bounded numerical match; closure path open).**
`v = M_Pl × (7/8)^{1/4} × α_LM^{16} = 246.28 GeV` matches PDG
`v_obs = 246.22 GeV` to `+0.0255 %` on the same-surface plaquette /
coupling chain at the declared reuse value. It is not a physical VEV
agreement and rides on four named load-bearing primitives that have not been
derived from the physical Cl(3) local algebra plus Z^3 spatial substrate:
(P1) `M_Pl` import via the Planck lane's
Wald-Noether matching; (P2) Wick rotation `Z^3 → Z^4` to obtain the
4D taste count `2^4 = 16` (textbook lattice fermion-doubling result;
the framework's spatial substrate is `Z^3`); (P3) the algebraic
substitution `u_0^{16} → α_LM^{16}` between the determinant power
(per HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM) and the formula
power; (P4) identification of the formula's dimension-1 output with the
SM Higgs VEV. The framework's own
[YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md](YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md)
§3.2 already records the non-perturbative `α_LM^{16}` factor as
"outside the current retention scope by design"; this honest-status
correction propagates that admission to the package-level rhetoric.
Most defensible closure route: per-step Wilsonian transport on the
16-step taste staircase (C3 in
[HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
§5), still non-perturbative at canonical coupling per
[YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE_2026-04-17.md](YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE_2026-04-17.md).

**Supplied Ward boundary.** The package adopts y_t/g_s=1/sqrt(6) at M_Pl
from the cited Ward/color-flavor route. Its physical identification and
transport are upstream premises, not established by this inventory.

**QFP Insensitivity Theorem.** The top Yukawa has an infrared quasi-fixed
point (Pendleton-Ross focusing): y_t(v) is insensitive to the UV BC.
A 10% change in y_t(M_Pl) produces less than 0.5% change in y_t(v).
This reported sensitivity does not bound missing beta-function terms,
physical matching or arbitrary changes to the flow. The historical 14/14
score in `scripts/frontier_yt_qfp_insensitivity.py` is not a fresh result here.

**Conditional color readouts.** F_adj=8/9 is exact channel arithmetic.
The EW and Yukawa families K_EW(kappa_EW) and K_Y(kappa_Y) retain their
independent open physical matching coefficients. The historical package
chooses both zero; color dimensions and comparator agreement do not derive
those choices.

## 10. Superseded Documents

This document is the support inventory for the Cl(3) on Z^3 prediction
chain. It is not retained-status authority independent of the audit ledger.
The following route-local notes are provenance pointers. This inventory
does not supersede their current corrigenda or stronger scope boundaries;
current audit authority remains with the ledger. Older summaries are historical:

### y_t chain (all absorbed here)
- `YT_ZERO_IMPORT_CHAIN_NOTE.md` -- zero-import chain (pre-color-projection y_t)
- `YT_COLOR_PROJECTION_CORRECTION_NOTE.md` -- color correction to y_t
- `YT_EW_COLOR_PROJECTION_THEOREM.md` -- color projection for EW couplings
- `YT_EW_COUPLING_BRIDGE_NOTE.md` -- taste threshold development
- `YT_QFP_INSENSITIVITY_SUPPORT_NOTE.md` -- QFP robustness analysis
- `YT_ZERO_IMPORT_AUTHORITY_NOTE.md` -- earlier incomplete closure attempt
- `YT_GAUGE_CROSSOVER_THEOREM.md` -- gauge crossover analysis
- `YT_VERTEX_POWER_DERIVATION.md` -- CMT vertex power derivation
- All other `YT_*.md` files

### Higgs mass (all absorbed here)
- `HIGGS_MASS_DERIVED_NOTE.md` -- CW analysis and honest status
- `HIGGS_MASS_FROM_AXIOM_NOTE.md` -- direct formula with N_c tracking
- `HIGGS_MASS_HIERARCHY_CORRECTION_NOTE.md` -- hierarchy correction

### Color projection (absorbed here)
- `YUKAWA_COLOR_PROJECTION_THEOREM.md` -- Yukawa color correction derivation
- `RCONN_DERIVED_NOTE.md` -- 1/N_c derivation of R_conn

### EW couplings (absorbed here)
- `EW_COUPLING_DERIVATION_NOTE.md` -- EW coupling derivation and sensitivity

---

## 11. Remaining Open Questions

### 11.1 Higgs readout and calibration gap

The 125.10 GeV historical package label is not reproduced by the displayed
calibration inputs (§7.3). No numerical gap is closed here. Complete running,
matching and a physical Higgs-pole identification remain needed; the 140.3 GeV
curvature readout is a distinct diagnostic.

### 11.2 Dark matter

The old R=5.48 agreement is superseded by the September30 corrigendum in
[G_BARE_DERIVATION_NOTE.md](G_BARE_DERIVATION_NOTE.md). With its corrected
relative-speed Sommerfeld kernel the supplied model gives approximately 8.07,
not 5.48, at alpha_plaq=0.0923. This remains a conditional mismatch, not a
derivation of the cosmological boundary condition or evidence for g_bare=1.
No new Boltzmann calculation is claimed here.

### 11.3 CKM matrix

The structural machinery is strong:
- V_us = sqrt(m_d/m_s) to 0.31% (Gatto-Sartori-Tonin relation)
- **Superseded comparison:** the historical `0.23%` for
  `V_cb = (m_s/m_b)^{5/6}` used mixed scales. The October4 correction above
  reports about 19% mismatch on its common-scale mixed-truncation diagnostic,
  with no 16-sigma inference; physical bridge closure remains open
- delta_CP = 2pi/3 (exact, from Z_3)
- Schur cascade: c_13 = c_12 * c_23 (exact, from NNI structure)

Full closure requires deriving the quark mass ratios m_d/m_s and m_s/m_b
from the axiom. The route is identified: R_overlap and beta_JW (both
computable from the framework). Status: BOUNDED, viable route identified.

### 11.4 The plaquette

<P>=0.5934 is the declared pure-gauge reuse value, not a newly certified
Monte Carlo determination. Its ensemble uncertainty, action/measure matching
and physical matter-inclusive replacement remain open as described above.

### 11.5 Perturbative truncation

The backward Ward scan uses 2-loop SM RGE. The reported UV sensitivity does not
bound the omitted terms or matching errors. The old ~3% and <1% estimates
are not certified error bounds; a complete higher-order implementation and
systematic analysis are needed.

### 11.6 Hierarchy formula primitives (P1-P4)

The hierarchy formula `v = M_Pl × (7/8)^{1/4} × α_LM^{16} = 246.28 GeV`
matches PDG `v_obs = 246.22 GeV` to `+0.0255 %` on the same-surface
plaquette / coupling chain, but rides on four named load-bearing
primitives that have not been derived from the physical Cl(3) local
algebra plus Z^3 spatial substrate:

- **P1.** `M_Pl` import as the UV scale (Planck lane authority,
  itself `audited_conditional`).
- **P2.** Wick rotation `Z³ → Z⁴` to obtain the 4D taste count
  `2^4 = 16`. The framework's spatial substrate is `Z^3`, where the
  taste count is `2^3 = 8`. The 4D extension is borrowed from
  textbook 4D Wick-rotated lattice fermion-doubling literature.
- **P3.** The algebraic substitution `u_0^{16} → α_LM^{16}` between
  the determinant power (proven on the L_s=2/L_t=4 minimal block in
  HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM) and the formula
  power. Identity `α_LM^{16} = α_bare^{16} × u_0^{-16}` shows the
  formula's dominant suppression is `α_bare^{16} ≈ (4π)^{-16}`, not
  the determinant power `u_0^{16} ≈ 0.124`.
- **P4.** Identification of the formula's dimension-1 output with
  the SM Higgs VEV (lattice → physical observable identification).

This package does not supply a framework derivation of
`v = Λ × α^N` for integer `N` from the baseline. Closure path: derive at
least one of P1-P4 from primitives. Most defensible route is per-step
Wilsonian transport on the 16-step taste staircase (C3 in
HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10), which the framework's
YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE records as non-perturbative at
canonical coupling. Status:
**bounded numerical match; closure open.** See
[HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
for the full assumption-by-assumption counterfactual record, the
branch-local route search, and the cross-disciplinary mathematical
search context.

---

## 12. Summary Table

Historical package values under the supplied premises above. These entries
are not independent predictions or a current uncertainty-certified scorecard:

| Observable | Predicted | Observed | Deviation | Status |
|-----------|-----------|----------|-----------|--------|
| v [GeV] | 246.28 | 246.22 | +0.03% | BOUNDED [^v-status] |
| alpha_s(M_Z) | 0.1181 | 0.1179 | +0.14% | Conditional supplied-input readout |
| sin^2(theta_W)(M_Z) | 0.2306 | 0.2312 | -0.26% | Conditional supplied-input readout |
| 1/alpha_EM(M_Z) | 127.67 | 127.95 | -0.22% | Conditional supplied-input readout |
| m_t(pole, 2-loop) [GeV] | 172.57 | 172.69 | -0.07% | Conditional supplied-input readout |
| m_t(pole, 3-loop) [GeV] | 173.10 | 172.69 | +0.24% | Conditional supplied-input readout |
| y_t(v) | 0.9176 | ~0.917 | +0.06% | Conditional supplied-input readout |
| m_H (2-loop) [GeV] | 119.8 | 125.25 | -4.4% | Conditional supplied-input readout |
| m_H (historical full-3-loop label) [GeV] | 125.10 | 125.25 | Historical -0.12% | Calibration-input mismatch; §7.3 |
| Vacuum stability | Historical sampled trajectory | Supplied truncated SM trajectory | No all-scale conclusion | Diagnostic only |

[^v-status]: Bounded numerical match on the same-surface
plaquette/coupling chain at `+0.0255 %`. The hierarchy formula
`v = M_Pl × (7/8)^{1/4} × α_LM^{16}` rides on four open primitives
P1-P4 (M_Pl import; Wick rotation `Z^3 → Z^4` for 4D taste count;
`u_0^{16} → α_LM^{16}` algebraic substitution; EWSB observable
identification); see §11.6 above and
[HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md).

The table preserves historical reported values and comparators, including
correlated outputs of common inputs. Neither agreement percentages nor
different loop-order values establish independence, physical matching or an
uncertainty bound. The Higgs calibration and vacuum-stability limits are
stated in §7.3–7.4.

Conditional support inventory with the listed admitted and supplied inputs;
no independent closure is asserted.
