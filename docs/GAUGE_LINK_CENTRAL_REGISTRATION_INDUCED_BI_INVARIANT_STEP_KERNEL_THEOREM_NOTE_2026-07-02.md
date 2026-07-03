# Gauge-Link Record Step: Central Registration Induces Bi-Invariant Step Kernels

**Date:** 2026-07-02
**Claim type:** bounded_theorem
**Claim scope:** Central-scalar record registration on a one-link `L^2(G)`
carrier induces normalized convolutional, Ad-invariant, inversion-symmetric,
representation-positive step kernels for the registration class, with exact
finite `S3`/`Q8` witnesses and truncated `SU(3)` softness numerics; no
record-step occurrence, position-classicality, rate-value, heat-kernel,
continuum, or Wilson action-surface selection closure.
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [`scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py`](../scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py)

## Purpose

The gauge-dynamics lane uses a step-measure premise: the one-link step law
is bi-invariant, or equivalently Ad-invariant for the class function kernel.
The panel finding left that premise open because kinematic gauge covariance
does not supply the Ad-invariant step measure. The conditional attractor
surface
`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md`
is named here only as prose context, not a citation-graph dependency.

This note derives the premise from a different input. If a record step
registers the gauge-central content of a link, the induced position-classical
transition kernel is automatically normalized, convolutional,
Ad-invariant, inversion-symmetric, and positive in the representation
coefficients. The load-bearing input is registration-centrality, not
kinematic covariance.

The canonical record partition discussion in
`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`
is not a citation-graph dependency. The downstream rate and finite-link rows
`GAUGE_LINK_PER_RECORD_STEP_RATE_DIAL_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md`
and
`G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md`
are also not a citation-graph dependency; they are named as consumers of the
mechanism classified here.

## Supplied surfaces (cited at audited scope)

- [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md)
  supplies the canonical basis and fixed trace form used for the `SU(3)`
  numerical normalization.
- [`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md)
  supplies the record-step channel form
  `W|psi>|0> = P_0|psi> tensor |0> + P_1|psi> tensor |1>` with extracted
  Kraus blocks `K_r = P_r` in its bounded finite-qubit model. This note
  applies that channel form with the pointer partition taken to be the
  link's gauge-central partition.
- [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
  supplies the respected boundary: no continuous dynamics is claimed here;
  this is a classification of registration steps only.
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  supplies the lane surface whose kernel-positivity property is derived for
  the registration class below.

## Setup and definitions

For a finite gauge group `G`, the one-link Hilbert space is `L^2(G)` with
position basis `|g>`. The two-end gauge action is the two-sided regular
action. The left end translates one side of the group argument, and the
right end translates the other side.

For compact `G`, the same formulas are read in a Peter-Weyl truncation. The
runner uses exact finite checks for `S3` and `Q8`, and a deterministic
`SU(3)` character-grid truncation for the softness numerics.

A central registration channel has controlled-copy form

```text
W |psi>|0> = sum_j (K_j |psi>) |j>
K_j = sum_R sqrt(m_j(R)) P_R
m_j(R) >= 0
sum_j m_j(R) = 1  for each R.
```

Here `P_R` is the Peter-Weyl isotypic projector for irrep `R`. Sharp
partitions are indicator functions on the representation labels, and the
full-resolution projective case is `m_j(R) = delta_{jR}`.

For position-classical link states, the induced transition kernel is

```text
T(g|h) = sum_j |<g|K_j|h>|^2.
```

For finite `G`, define

```text
kappa_j(x) = sum_R sqrt(m_j(R)) (d_R / |G|) chi_R(x).
```

Then

```text
T(g|h) = sum_j |kappa_j(g h^{-1})|^2.
```

This note assumes the lane premise that link states are position-classical
between steps. It classifies the kernel produced by a record step once such
a step acts on the link sector.

## Theorem 1 (gauge-central pointer content of a link)

The registrable central content of a link is exactly its Peter-Weyl
representation-label content. Equivalently, the gauge-invariant observable
algebra of the two-ended link is the abelian algebra spanned by the isotypic
projectors `{P_R}`.

Proof sketch:

1. Peter-Weyl decomposes the link carrier as
   `L^2(G) = direct sum_R V_R tensor V_R^*`.
2. The two-sided regular action acts irreducibly on each
   `V_R tensor V_R^*` block.
3. Its commutant is therefore scalar on each block, so the central
   observable algebra is spanned by the block projectors `{P_R}`.

Thus the pointer partition `{P_R}` is derived by a commutant computation,
not invented. This structurally satisfies the partition-input guardrail
discussed in
`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`,
which is not a citation-graph dependency. By contrast, on an irreducible
carrier the central partition is trivial by Schur; the link/holonomy
carrier is reducible, and that is where registration has content.

## Theorem 2 (central registration induces bi-invariant positive step kernels)

Let

```text
K_j = sum_R sqrt(m_j(R)) P_R
```

with `m_j(R) >= 0` and `sum_j m_j(R) = 1` for every `R`. On
position-classical link states, the induced transition kernel is

```text
T(g|h) = sum_j |<g|K_j|h>|^2
       = sum_j |kappa_j(g h^{-1})|^2,
kappa_j(x) = sum_R sqrt(m_j(R)) (d_R / |G|) chi_R(x).
```

It has the following properties.

Normalization. Character orthogonality gives

```text
sum_g |kappa_j(g h^{-1})|^2
  = sum_R m_j(R) d_R^2 / |G|.
```

Summing over `j` uses `sum_j m_j(R) = 1`, and then
`sum_R d_R^2 = |G|`, so every column of `T` sums to one.

Convolution, Ad-invariance, and inversion symmetry. The kernel depends on
`g` and `h` through the group difference and the functions `kappa_j` are
class functions. Hence simultaneous two-end gauge transport conjugates the
argument without changing `T`. Since `chi_R(x^{-1}) = conjugate(chi_R(x))`,
the sum of moduli squared also gives `t(x) = t(x^{-1})`.

Positive representation coefficients. Products of characters decompose into
characters with nonnegative Kronecker multiplicities. Therefore the
character coefficients of `t(x) = T(x|e)` are nonnegative for every channel
in this central registration class.

Consequently, the bi-invariance and record-positivity premises of the
gauge-dynamics lane are, for this class, derived, not assumed; the
load-bearing input is registration-centrality, not kinematic covariance.

## Theorem 3 (contrast witnesses)

The central-scalar hypothesis is doing real work.

First, an intra-block non-scalar Kraus operator can preserve the
representation label while picking a frame inside the `R` block. Such a
channel is non-demolition for the `R` label, but it is not central-scalar.
The runner builds this witness inside the `S3` standard block and checks
that the induced transition probabilities fail to be a convolution kernel.
Mere pointer non-demolition therefore does not suffice; central-scalar
registration does.

Second, deterministic drift by a fixed noncentral group element gives a
convolution kernel but not a registration kernel of the above kind. In the
`S3` witness, the standard character coefficient is negative and the
standard Fourier block is non-scalar. This matches the lane's drift witness:
it is not the record-registration mechanism classified here.

## Theorem 4 (registration softness sets the step size; derived rates)

Registration softness controls the per-step size. Full-resolution
projective registration resolves the representation label as sharply as the
chosen carrier allows and induces a maximal kick in the tested truncation.
Soft POVM registrations, implemented as Gaussian bins along the quadratic
Casimir axis, induce concentrated kernels.

In the deterministic `SU(3)` truncation used by the runner, the variance
strictly decreases as the registration is softened:

```text
projective > width 0.5 > width 2.0 > width 6.0 > width 15.0.
```

The corresponding values are checked against the validation references
near `9.870`, `8.048`, `5.852`, `2.476`, and `1.861`. Each registration
channel therefore has a derived rate: the lane's rate dial is relocated
onto the registration resolution/softness of the step.

Honest limit: the per-step kernel is not the heat kernel. For the width-6
soft kernel, the runner computes

```text
eps_R = -log((<T, chi_R> / d_R) / <T, chi_triv>)
```

and gates the relative spread of `eps_R / C2(R)` across sampled blocks. The
spread is required to exceed `0.2` and remain below `1.0`; this prevents a
claim that the single-step generator is purely Casimir. The canonical
heat-kernel form belongs to the composed small-step limit, the content of
`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md`,
which is not a citation-graph dependency.

## Boundary

This note does not claim:

- It does not derive that a record step occurs or that the link sector is
  updated at all. The semigroup boundary is respected: "continuous Markov
  semigroups live on the probability/ensemble".
- It does not derive position-classicality between steps; that remains a
  named lane premise.
- It does not derive the registration resolution or softness value. The
  rate number, including `tau = 1/2` in
  `GAUGE_LINK_PER_RECORD_STEP_RATE_DIAL_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md`,
  is not pinned here; that row is not a citation-graph dependency.
- It does not claim the per-step kernel is the heat kernel; the per-step
  generator spread is gated in the runner.
- It does not claim kinematic covariance supplies the step-measure premise;
  the panel finding stands.
- It does not supply Wilson action-surface selection.
- It does not take a continuum limit.
- It does not set, predict, or apply an audit verdict or any effective-status
  promotion.

Forward surface: the native finite-carrier registration kernel is
parameter-free at full resolution. Computing its rate against the
unit-variance point is the next concrete calculation. That calculation is
outside this row.

## Falsifiers

The row fails if any runner-checkable surface below fails.

- `S3` exact projector reconstruction from the given character table and
  from the regular-representation formula: idempotence, orthogonality, and
  completeness must hold exactly.
- `S3` two-sided commutant dimension must be `3`, while the left-only
  wrong-object rejector must be `6`.
- `S3` full-resolution and coarse central registration kernels must match
  their independent closed formulas, normalize exactly, obey two-sided
  invariance, obey inversion symmetry, and have nonnegative exact character
  coefficients.
- `Q8` exact character rows must pass class-weighted orthogonality, and
  the dimension-square sum must be `8`.
- `Q8` two-sided commutant dimension must be `5`, while the left-only
  wrong-object rejector must be `8`.
- The `S3` intra-block witness must be a valid channel and must fail the
  convolution test by more than `1e-4`.
- The deterministic drift witness must be convolutional but must have a
  negative nontrivial character coefficient and a non-scalar standard
  Fourier block.
- The `SU(3)` character machinery must pass scalar Jacobi-Trudi dimension
  checks and sampled orthonormality checks.
- The `SU(3)` soft kernels must normalize, have real sampled character
  coefficients, and pass positivity checks; the projective kernel is
  checked for nonnegative sampled coefficients.
- The `SU(3)` variances must strictly decrease with registration softness
  and remain within ten percent of the validation references.
- The width-6 generator-spread gate must stay between `0.2` and `1.0`,
  enforcing the honest non-heat per-step statement.
- The exact rational summary must recover the `S3` full-resolution
  coefficients `(1/6, 1/9, 1/9)` and the Kronecker witness
  `std tensor std = triv + sign + std`.
- Source-boundary guards must find the four cited dependency files and the
  preserved boundary phrases, while forbidden status and overclaim strings
  must be absent from the note and runner.

## Verification

Run:

```text
python3 scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py
```

Expected:

```text
TOTAL: PASS=103 FAIL=0
```
