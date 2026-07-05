# Native Positive-Class Adjudication: On The Framework's 3+1 Canonical Class, Any Emergent Integer-Sector Weighting Has Non-Negative Masses, So The Gauge-Side Theta Dial Is Vacuous Or Zero -- Narrow Bounded Theorem

**Date:** 2026-07-04
**Claim type:** bounded_theorem
**Boundary:** supplied-class narrow theorem; effective status is pipeline-derived after independent audit ratification and dependency closure.
**Status authority:** independent audit lane only. This note does not set or predict an audit outcome and does not edit audit ledgers, queues, Tier-A registries, publication-status surfaces, active review queues, lane registries, or front-door status files.
**Primary runner:** [`scripts/frontier_theta_gauge_native_positive_class_emergent_sector_weighting_2026_07_04.py`](../scripts/frontier_theta_gauge_native_positive_class_emergent_sector_weighting_2026_07_04.py)
**Cached log:** [`logs/runner-cache/frontier_theta_gauge_native_positive_class_emergent_sector_weighting_2026_07_04.txt`](../logs/runner-cache/frontier_theta_gauge_native_positive_class_emergent_sector_weighting_2026_07_04.txt)

## Purpose

This source artifact states the gauge-side theta question inside the native
canonical class, rather than on an independently fundamental four-dimensional
lattice. The framework is natively 3+1: spatial `Z^3` with `SU(3)` links, the
canonical imported Wilson per-plaquette class, and emergent record-tick
evolution. There is no fundamental fourth lattice direction. When prior
gauge-side notes use finite `T^4` models or flux-cohomology language as
emergent OS0 surface carrier models, the content this note consumes is the
family of native transfer moments

```text
<Omega, O_1 T^{n_1} O_2 T^{n_2} ... Omega>.
```

This note therefore quantifies over any emergent integer-valued sector
functional `Q` on finite native history windows. It requires no four-dimensional
substrate input and no prior existence, integrality, nonvacuity, or
susceptibility theorem for such a `Q`.

The Record-side readout guard uses only the current Record wording in
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md): only records are
readable, and a readout value is determined by record content alone.

## Source Inputs

The bounded class used here is the canonical imported Wilson + staggered-Wilson
class, with these already separated source rows:

- [GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.md](GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.md): for `beta > 0`, every dominant `SU(3)` weight has a strictly positive Wilson class-function character coefficient, and the Wilson one-link normalized convolution eigenvalue is strictly positive.
- [WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md): the Wilson gauge one-link weight has `c_lambda(beta) >= 0` for all irreps and `beta >= 0`, equivalently the Wilson gauge transfer kernel is positive semidefinite.
- [STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md](STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md): on its supplied finite staggered + Wilson surface, `det(M) = product_i (alpha^2 + sigma_i^2) > 0`.
- [REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md): background gauge-half reflection-positivity carrier.
- [RP_MIXED_OBSERVABLE_SINGLE_TRANSFER_MATRIX_NARROW_THEOREM_NOTE_2026-05-29.md](RP_MIXED_OBSERVABLE_SINGLE_TRANSFER_MATRIX_NARROW_THEOREM_NOTE_2026-05-29.md): background mixed-observable transfer-moment carrier.
- [SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md): background finite single-clock transfer carrier.

Everything else named below is a context handle, not a citation-graph
dependency.

## L0 Native Connectivity

For any finite native gauge window, the gauge group is a finite product of
connected compact groups:

```text
G_window = product_{finite native sites or links} SU(3).
```

`SU(3)` is connected, and a finite product of connected spaces is connected.
Therefore `G_window` is connected. There is no native large-gauge
superselection label for a theta angle to decorate. This is elementary and is
checked in miniature by the runner on `SU(2)^3`, where explicit paths
`g(t) = exp(t log g)` witness the same finite-product connectivity pattern.

## L1 Native Positive Class

On any finite record window in the canonical class, the native history weight
is

```text
product over plaquettes of exp(beta Re tr U_p)
x staggered-Wilson fermion determinant factor.
```

The attribution of positivity is deliberately split by level:

- **Pointwise gauge positivity is elementary:** each per-plaquette Wilson
  Boltzmann factor `exp(beta Re tr U_p)` is the exponential of a real number,
  hence strictly positive at every configuration. No cited row is needed for
  this step, and none is misused for it.
- **Fermion factor:** the determinant factor is real and non-negative on the
  supplied finite staggered + Wilson surface per the 2026-05-05 source row.
- **Slicing structure:** the 2026-06-07 coefficient row and the 2026-05-30
  kernel row certify the character/coefficient-level and transfer-kernel-level
  positivity of the SAME weight when it is sliced along record ticks — i.e.,
  that the OS0 moment representation of this measure is generated by a
  positive transfer kernel. That is the level the emergent-surface
  reconstruction consumes; it is a distinct statement from pointwise weight
  positivity, and both levels are needed below.

Hence the finite-window history measure `mu` is pointwise real and
non-negative,

```text
dmu(h) >= 0,
```

and its record-tick slicing is by a positive kernel.

The Wilson gauge factor is conjugation-symmetric as a real class function. This
bounded theorem does not import or require a separate conjugation-pairing
theorem for the supplied determinant factor; the load-bearing property below is
only the real non-negativity of the native pushforward masses.

## L2 Inheritance To Any Emergent Sector Functional

The inheritance argument is intentionally small. It is stated separately
because the theta-value conclusion needs it for every emergent sector
functional, not only for a preferred four-dimensional carrier model.

**Lemma L2a, sector pushforward positivity.** Let `Q` be any measurable
integer-valued functional on finite-window histories. Define

```text
m(q) = mu({h : Q(h) = q}).
```

Since `mu` is pointwise non-negative, each sector mass `m(q)` is real and
non-negative. This conclusion does not use any special formula for `Q`.

**Lemma L2b, marginal positivity.** Marginalization and block coarse-graining
of a pointwise non-negative measure are sums or integrals of non-negative
weights. Therefore every effective description obtained by integrating out
finite-window variables remains in the positive class.

**Lemma L2c, weak-limit positivity.** If a sequence of non-negative finite
measures converges weakly, its limit is non-negative: for every non-negative
bounded continuous test function `f`, the integrals `int f dmu_n` are
non-negative, and their limit `int f dmu` is non-negative. Thus scaling limits
taken through finite native windows cannot generate signed or complex sector
masses from the canonical positive class.

## Main Theorem

**Theorem T.** In the canonical imported Wilson + staggered-Wilson class, for
every emergent integer-valued sector functional `Q`, every positive relative
sector weighting by a gauge-side theta dial is vacuous or zero.

**Proof.** Let `m(q)` be the native sector masses induced by `Q`. By L1 and L2,
all populated `m(q)` are real and non-negative.

Suppose an emergent effective description weights the sectors as

```text
w(q) = e^{i theta q} m_tilde(q),
```

with `m_tilde(q) > 0` on populated sectors. Since a common populated-sector
phase is a readout convention, the nonvacuous content is the relative
sector-weight ratio. Fix any populated reference sector `q0`. Reproducing the
native record ratios requires

```text
[e^{i theta q} m_tilde(q)] / [e^{i theta q0} m_tilde(q0)]
  = m(q) / m(q0)
```

for every populated `q`. If at least two adjacent sectors are populated, say
`m(q) > 0` and `m(q+1) > 0`, then

```text
e^{i theta}
  = [m(q+1) / m(q)] [m_tilde(q) / m_tilde(q+1)].
```

The right-hand side is a ratio of positive real numbers. Since
`|e^{i theta}| = 1`, this ratio must be `1`, so `theta = 0 (mod 2 pi)`. This is
exactly the nonvacuous weighting clause: adjacent populated sectors make the
phase dial observable at the sector-weight level, and positivity collapses it
to the zero branch.

More generally, let `S = {q : m(q) > 0}`. If `S` has at least two elements, set

```text
Delta(S) = gcd{|q - q0| : q in S}
```

for any fixed `q0 in S`; the value is independent of the choice of `q0`. Phases
with `theta Delta(S) = 0 (mod 2 pi)` are constant across the populated support
and are support-vacuous aliases. If `Delta(S) = 1`, the only positive relative
representation is `theta = 0 (mod 2 pi)`. Adjacent populated sectors are the
common sufficient case because they force `Delta(S) = 1`.

The `theta = pi` branch is therefore excluded as nonvacuous positive-class
content exactly when the populated support contains both parities. Then some
relative sector ratio changes sign, contradicting L1 and L2 while
`m_tilde(q) > 0`. If the populated support lies in one parity class, `theta =
pi` is a common populated-sector phase and is a vacuous alias rather than new
theta-value content.

If zero or one sector is populated, every value of `theta` is readout-equivalent
after absorbing the single populated-sector phase into convention. The dial is
then vacuous, not physical theta-value content.

Therefore, on the canonical class, for every emergent integer-sector
functional, every positive relative gauge-side theta weighting is vacuous or
zero. ∎

## Readout Guard

A theta reparametrization of an emergent description that changes no record
expectation is convention, not content: only records are readable, and a
readout value is determined by record content alone. A reparametrization that
would change record expectations contradicts L1 and L2, since all record
expectations are moments of the fixed native non-negative measure, and that
measure carries no theta parameter.

## Relation To Sector-Lattice Context

`THETA_GAUGE_Z2_CHARACTER_COLLAPSE_ODD_SUPPORT_AND_POSITIVE_CLASS_ZERO_BRANCH_SELECTION_BOUNDED_THEOREM_NOTE_2026-07-03.md`
(context handle, not a citation-graph dependency) is related sector-lattice
work, but this note does not import that artifact and does not certify all of
its hypotheses. The source result here is narrower: native positive-class
pushforwards make relative theta sector weighting vacuous or zero on the
populated support.

The Q-STRUCTURE questions remain open:
`THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`
(context handle, not a citation-graph dependency),
`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`
(context handle, not a citation-graph dependency),
`THETA_SUPPLIER_FLAVORED_GRADING_SPECTRAL_FLOW_REGISTERS_WINDING_2D_NARROW_THEOREM_NOTE_2026-07-02.md`
(context handle, not a citation-graph dependency), and
`THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md`
(context handle, not a citation-graph dependency). Those handles cover the
existence and integrality of a derived emergent `Q` with nonvacuous weighting,
the 4D-carrier model, defect or monopole closure,
`W_anomaly_covariant_assembly`, and `SU(3)` abelianization. They are not
theta-VALUE content under this theorem. If those lanes separately derive a
nonvacuous emergent `Q` and an applicable positive weighting surface, this note
can be used only for the positive-class sector-weighting subclaim.

## What This Note Does Not Claim

- no derivation of the existence, integrality, nonvacuity, or susceptibility
  of any emergent `Q`; Q-structure physics stays open;
- no discharge or retirement of the theta Tier-A admission and no
  effective-status claim; this is not a discharge, and the audit lane owns
  status;
- no mass-side content; the `arg det M` chain is separate source work;
- scope is the canonical imported Wilson + staggered-Wilson class; other UV
  completions are outside;
- no derivation that an arbitrary emergent description admits the positive
  factorization `w(q) = e^{i theta q} m_tilde(q)`; this is the conditional
  positive-weighting surface of the theorem;
- no new axiom, primitive, admission, normalization, or measured input;
- `theta = pi` is excluded as nonvacuous content only when populated sectors of
  both parities are present; single-parity support makes it a support-vacuous
  alias;
- a future signed native class would need its own analysis.

## Runner Verification

The companion runner verifies:

- finite-product connectivity in a small `SU(2)^3` path model;
- exact positive sector masses in a particle-on-a-circle sector toy;
- the theta-fit discriminator as a 360-point quantifier sweep — a positive
  representation `m(q) = e^{i theta q} m_tilde(q)` exists exactly at
  `theta = 0` and at no other grid angle — including a hand-inserted
  non-real theta positive control recovered at exactly its inserted value;
- contradiction of nonvacuous relative `theta = pi` when both parities are
  populated, plus sparse single-parity controls where `theta = pi` is correctly
  classified as a support-vacuous alias;
- positivity under block marginalization and a finite-window weak-limit
  demonstration;
- a small `1+1` `Z_N` gauge miniature with positive plaquette weights,
  non-negative transfer entries, a symmetric positive diagonal determinant
  stand-in, and non-negative emergent flux-sector masses;
- text guards for required boundary phrases, forbidden status-changing
  phrases, and markdown-link discipline.
