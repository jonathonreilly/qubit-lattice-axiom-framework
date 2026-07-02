# Native Finite-Carrier Registration Kernel: the Parameter-Free Rate vs the Unit-Variance Point

**Date:** 2026-07-02
**Claim type:** bounded_theorem
**Claim scope:** parameter-free native finite-carrier full-resolution
registration kernel, readout-floor split, and unit-variance-point route
refutation within the stated holonomy-family reading; no record-step
occurrence, position-classicality, Wilson action-surface selection, continuum
limit, global `tau = 1/2` refutation, or audit-status promotion.
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/native_carrier_registration_kernel_rate_vs_unit_variance_point_2026_07_02.py`](../scripts/native_carrier_registration_kernel_rate_vs_unit_variance_point_2026_07_02.py)

## Purpose

This note tests the candidate route
`one record step = full-resolution registration on the native finite gauge
carrier`.

If that route produced the declared unit-variance-per-record-step point, the
per-direction second moment would be `m^2 = 1` and `tau = m^2/2 = 1/2`.

The parameter-free native full-resolution construction does not give that
value. The three recomputed numbers are:

```text
m^2(T_V)  = 2.440631      total native step
m^2(T_id) = 1.835061      readout floor
increment = 0.605570      registration-attributable part
```

This is a refutation-shaped positive result: it gives exact properties of the
native finite carrier and quantifies the residual against the unit point.

The surrounding context rows are named in backticks as not a citation-graph
dependency:
`GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02.md`,
not a citation-graph dependency;
`GAUGE_LINK_PER_RECORD_STEP_RATE_DIAL_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md`,
not a citation-graph dependency;
`G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md`,
not a citation-graph dependency; and
`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md`,
not a citation-graph dependency.

The registration-kernel construction is re-derived in this packet, so this row
stands on the four linked dependency surfaces below rather than on the
backtick-only context rows.

## Supplied surfaces (cited at audited scope)

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  supplies the taste-cube commutant structure, including the selected-axis
  fiber and the residual complementary-axis swap that splits the base as
  `3 + 1`.
- [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md)
  supplies canonical normalization discipline and the selected zero-sum
  logarithm branch used for the second-moment readout.
- [`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md)
  supplies the record-step channel form with projector Kraus blocks.
- [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
  supplies the boundary discipline: this note does not turn a constructed
  channel into a dynamics-existence claim.

## Setup: the native carrier and its registrable content

Let `V = C^8 = C^2 selected-axis fiber tensor C^4 base`.

The selected-axis fiber carries the weak `su(2)` generators.

The residual complementary-axis swap acts on the base `C^4` and splits it as
`C^4 = C^3 symmetric + C^1 antisymmetric`.

The derived `su(3)` is the compact semisimple part of the joint commutant
`gl(3) + gl(1)`.

It acts on the symmetric block and trivially on the selected-axis fiber and on
the antisymmetric block.

Therefore, under the derived `su(3)`,

```text
V = 3 + 3 + 1 + 1,
m_3 = 2,
m_1 = 2.
```

The link carrier is `B(V) ~= V tensor V^*`.

The two-end action is `X -> rho(g) X rho(h)^dagger`.

The two-end-invariant central sectors are the isotypic pairs
`(i,j) in {3,1}^2`.

Their dimensions are:

```text
dim P_33 = 36,
dim P_31 = 12,
dim P_13 = 12,
dim P_11 = 4.
```

They sum to `64`.

The Record-axiom reading used here is that a step locks exactly one local
possibility from the available subset.

On the native central sector surface, that makes full central resolution
parameter-free:

```text
Kraus blocks = {P_33, P_31, P_13, P_11}.
```

No fitted scale or prefactor is introduced.

## Theorem 1 (the native registration kernel)

For a holonomy configuration, write `X_U = rho(U)`.

The central-sector overlap is
`<X_U, P_ij X_W> = delta_ij m_i chi_i(U^dagger W)`.

This follows directly from Schur orthogonality on the isotypic blocks:
`P_ij X_W = P_i rho(W) P_j`, and the Hilbert-Schmidt pairing leaves a trace on
the matching isotypic block exactly when `i = j`.

The induced transition density on the holonomy family is

```text
T_V(x) = sum_i m_i^2 |chi_i(x)|^2 / sum_i m_i^2,
x = U^dagger W.
```

Since `m_3 = m_1 = 2` and `chi_1 = 1`,
`T_V(x) = (|chi_3(x)|^2 + 1)/2`.

Using `|chi_3(x)|^2 = 1 + chi_8(x)`, the exact equivalent form is

```text
T_V(x) = 1 + chi_8(x)/2.
```

The spectral data are exact:

```text
w_trivial = 1,
w_8 = 1/16,
w_R = 0 for every other nontrivial block.
```

The density is strictly positive because
`chi_8(x) = |chi_3(x)|^2 - 1 >= -1`, hence `T_V(x) >= 1/2`.

Multiplicity robustness is exact. The equal multiplicities cancel in the
normalized density, so the same kernel is obtained from the spinless carrier
`3 + 1` with `m_3 = m_1 = 1`.

## Theorem 2 (readout floor, registration increment, Schur contrast)

Apply the same readout-family construction to the identity channel, with no
registration dephasing.

The identity-channel readout density is

```text
T_id(x) = |chi_3(x) + 1|^2 / 2
        = 1 + (chi_8(x) + chi_3(x) + conj(chi_3(x)))/2.
```

Its nontrivial spectral data are:

```text
w_3 = 1/6,
w_3bar = 1/6,
w_8 = 1/16.
```

Native full central registration kills exactly the `3` and `3bar` coherence
blocks, `1/6 -> 0`, and leaves the adjoint block unchanged, `w_8 = 1/16`.

That separates the readout floor from the registration-attributable increment.

The Schur contrast is load-bearing. If the antisymmetric block is dropped and
the triplet-only carrier is used, there is a single central sector.

Then the registration channel is the identity channel:

```text
T_3,reg(x) = |chi_3(x)|^2,
T_3,id(x)  = |chi_3(x)|^2.
```

No registration-attributable motion exists on that carrier. The derived
antisymmetric `gl(1)` block is load-bearing for registration dynamics.

## Theorem 3 (the parameter-free numbers and the unit-point comparison)

The per-direction second moment per step is
`m^2 = <sum_j theta_j^2>_T / 4`.

The licensed logarithm branch is the zero-sum canonical branch from the
rigidity surface:

```text
theta_1 + theta_2 + theta_3 = 0,
```

with representatives shifted by `2 pi` integers to the minimal-norm zero-sum
triple.

On the centered Weyl grid, with Haar density `|Delta|^2/6`, the runner
recomputes:

```text
m^2(T_V)  = 2.440631
m^2(T_id) = 1.835061
increment = 0.605570
```

The values are identical at grid sizes `M = 800` and `M = 1600` to the stated
gate.

None of the three values is the unit value `1`.

The naive-principal branch is not the licensed branch. It wraps the third phase
principally and does not enforce exact zero sum.

It is reported as convention sensitivity:

```text
m^2_naive(T_V) = 2.411846.
```

Under that naive branch, the runner observes the structural identity

```text
<|chi_3|^2 sum_j theta_j^2> = pi^2.
```

The observed value is `9.869604401089`, matching
`pi^2 = 9.869604401089`.

This is a consistency observation, not a load-bearing premise for the verdict.

Verdict within this defined reading:

```text
tau_native = m^2(T_V)/2 = 1.220315426.
```

The unit-variance point would require `tau = 1/2`.

The beta-map value from this native registration rate is
`N_c/tau_native = 3/tau_native = 2.458381`, not `6`.

Therefore this note refutes the single named route:

```text
native full central registration => unit variance per record step.
```

It does not derive or globally refute `tau = 1/2`; it locates the gap for this
specific construction.

## Boundary

This note does not claim:

- that the transition density on the non-orthogonal holonomy family is the
  unique possible reading. It is a defined construction with named premises.
- does not derive that a record step occurs; step occurrence remains outside
  this construction, and the semigroup boundary is respected.
- that it derives position-classicality.
- that it derives or globally refutes `tau = 1/2`; it refutes the single named
  route from native full resolution to unit variance within the defined
  reading.
- that the branch convention is hidden. The zero-sum convention is named, and
  the naive-principal sensitivity is reported.
- that it selects a Wilson action surface.
- that it proves a continuum limit.
- that it supplies an audit verdict or any effective-status promotion.

Forward surface:

- Study registration at the resolution the admissibility rule supports per
  nearest-neighbor step, including partial or soft registration.
- Study alternative licensed readout families. The readout floor versus
  registration-attributable split localizes what any such reading must address.
- Study composed or multi-step calibration, where the parameter-free one-step
  native number becomes an input datum rather than a fitted prefactor.

## Falsifiers

The runner falsifies this note if any of the following fail:

- selected-axis `su(2)` relations; residual swap commutation; joint commutant
  dimension `10`; rejector commutant dimension `16`; base split `3 + 1`.
- embedded `su(3)` closure using the `3 x 3` computed structure constants;
  Casimir spectrum `4/3 x6` and `0 x2`.
- link-sector projector orthogonality, sector traces `(36, 12, 12, 4)`,
  two-end generator commutation, and direct overlap versus character formula.
- Weyl-grid Haar normalization; `T_V(x) = 1 + chi_8(x)/2`; density
  normalization; strict positivity; and spectral data `w_8 = 1/16`,
  `w_3(T_V) = 0`, `w_3(T_id) = 1/6`.
- zero-sum moment anchors; naive-branch sensitivity; the `pi^2` identity; the
  Monte Carlo SU(3) cross-check; the triplet-only Schur contrast; and the
  source-boundary guards.

## Verification

Run:

```bash
python3 scripts/native_carrier_registration_kernel_rate_vs_unit_variance_point_2026_07_02.py
```

Expected final line:

```text
TOTAL: PASS=68 FAIL=0
```
