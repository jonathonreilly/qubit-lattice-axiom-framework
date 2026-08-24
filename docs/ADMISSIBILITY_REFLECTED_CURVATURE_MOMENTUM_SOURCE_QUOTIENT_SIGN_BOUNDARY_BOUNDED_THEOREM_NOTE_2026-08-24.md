---
claim_id: admissibility_reflected_curvature_momentum_source_quotient_sign_boundary_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "For the supplied twenty-two-edge reflected-curvature quadratic action family Q_mu=Q_union+mu D(-q)^T D(q), the y/z-odd six-edge Ward quotient on axial momentum (k,0,0,theta) has a source-independent rank-one update O_mu=O_0-mu r(theta)r(theta)^dagger. At mu=1/1024, a reconstructed degree-(5,4) bivariate fifth-elementary polynomial and Bernstein certificate localize the full-temporal-circle PSD threshold to k*=0.0890875879243, with a transition pole shell and one negative physical direction below it. On the exact L=72 static mode, a local TT edge source and a reflected closed-Record-line composite have the same common-metric stress and exact Ward conservation but opposite-sign raw covariance responses, so the raw covariance does not descend to common-metric source classes. Reducing the action to the common-metric image before inversion gives a positive, representative-independent odd metric quotient on the declared numerical atlas; projecting sources after raw inversion does not. The counterfactual mu=-1/1024 repairs the tested odd infrared fiber and retains the inherited source/Newtonian gates, but develops a cross-TT-visible even-sector unit-circle pole. These are bounded numerical/algebraic route decisions for this action family. A canonical physical reduction, other action, full Brillouin zone, nonlinear gravity, quantum/Record dynamics, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
parents:
  - admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_bounded_theorem_note_2026-08-24
  - admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_bounded_theorem_note_2026-08-14
  - admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_bounded_theorem_note_2026-08-13
upstream_dependencies:
  - minimal_axioms
  - admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_bounded_theorem_note_2026-08-24
  - admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_bounded_theorem_note_2026-08-14
  - admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_bounded_theorem_note_2026-08-13
runner: scripts/admissibility_reflected_curvature_momentum_source_quotient_sign_boundary_2026_08_24.py
---

# Reflected-Curvature Momentum, Source-Quotient, And Sign Boundary

**Type:** `bounded_theorem`

**Status:** bounded numerical/algebraic support; unaudited; no axiom is
amended.

**RAW_FULL_SOURCE_MATRIX_GNS_VERDICT: BOUNDED_INFEASIBLE.**

**EQUAL_MAGNITUDE_SIGN_FLIP_VERDICT: BOUNDED_INFEASIBLE.**

**PHYSICAL_REDUCTION_VERDICT: OPEN.**

**GRAVITY_VERDICT: OPEN.**

TOE accounting: **zero obligation retirement, zero percentage movement, and
no axiom is amended**. The result changes the gravity portfolio substantially,
but it does not complete or positively retain a gravity theory.

## Result Up Front

Block 184 proved a positive rank-five matrix density at one spatial momentum,
`k=pi/2`, in the odd sector of the `y <-> z` reflection. Extending the same
literal action and Ward border toward the infrared finds that this momentum
was not representative.

For

\[
 Q_\mu(q)=Q_{\rm union}(q)+\mu D(-q)^T D(q),
 \qquad O_\mu(q)=-Q_\mu(q),                              \tag{1}
\]

the axial odd restriction obeys

\[
 O_\mu(k,\theta)=O_0(k,\theta)-\mu r(\theta)r(\theta)^\dagger, \tag{2}
\]

where, in the committed odd edge basis,

\[
 r(\theta)=
 \begin{pmatrix}
 1+e^{-i\theta}&\sqrt2&0&0&-\sqrt2e^{-i\theta}&0
 \end{pmatrix}^{T},                                    \tag{3}
\]

and `||r||^2=6+2 cos(theta)` lies between four and eight. The update is
rank one, is independent of `k`, and is orthogonal to the Ward column. Thus
positive `mu` is literally a negative-semidefinite update of the covariance
kernel on one conserved direction; it can create at most one new negative
physical eigenvalue.

At `mu=1/1024`, the complete axial odd phase boundary is

\[
 k_c(0)=0.0884184579426,
 \qquad
 k_c(\pi)=0.0890875879243.                              \tag{4}
\]

The latter is the global full-temporal-circle threshold. Above it, the odd
kernel is positive semidefinite of rank five for every temporal frequency.
Between the two endpoints, the temporal circle contains a pair of bordered
unit-circle poles. Below `k_c(0)`, one conserved odd direction is negative at
every temporal frequency. The exact periodic controls make the distinction
concrete:

| periodic length | `k=2 pi/L` | static minimum physical eigenvalue | role |
|---:|---:|---:|---|
| `71` | `0.0884955677068` | `+5.29743e-6` | static positive, but temporal pole at `theta=0.691266304413` |
| `72` | `0.0872664625997` | `-7.92636e-5` | inside the all-frequency negative band |

This does not by itself prove a graviton ghost. The negative direction is
dominated by the reflected relative-orientation sector, and a concrete
common-metric reduction removes it. But it does refute the physical use of the
*raw* full-edge inverse for all conserved sources.

## The Decisive Source-Fidelity Test

Let `M(q)` be the supplied line-metric map. At the static `L=72` momentum,
compare the local TT edge source

\[
 o=e_y-e_z                                                   \tag{5}
\]

with the reflection-odd composite of four closed transverse Record-line
sources

\[
 r_R={j_{+y}+j_{-y}-j_{+z}-j_{-z}\over2\sqrt2}.             \tag{6}
\]

Each `j` uses the repository's coefficient-two diagonal edge convention. The
four lines and their oppositely weighted partners are displaced in the `x`
direction, so they share the same nonzero Fourier multiplier
`L(1-exp(i k))`. Reflection supplies the `z` pair from the `y` pair without a
new source rule.

Both sources are exactly odd and Ward-conserved, and

\[
 M^\dagger r_R=M^\dagger o,
 \qquad
 d=r_R-o\in\ker M^\dagger.                                \tag{7}
\]

Yet the raw Ward-bordered covariance gives

\[
 o^\dagger C o=+262.79515955,
 \qquad
 r_R^\dagger C r_R=-19528.1015920,
 \qquad
 d^\dagger C d=-19790.5978933.                            \tag{8}
\]

For a Hermitian form to descend from edge sources to common-metric source
classes, `ker M^dagger` must lie in its radical. Equation (8) directly
disproves that condition. Therefore one cannot first build the raw covariance
and then declare the relative directions to be auxiliary. If Record edge
microstructure is physical, `d` is a Ward-conserved negative-norm source of
this candidate. If only common-metric stress is physical, the calculation is
a source-interface failure that demands a reduction or selected section.

The local TT scalar is a particularly dangerous diagnostic by itself. On the
`L=72` temporal grid it stays positive and has

\[
 k^2 C_{TT}(k,0)=2.00129959,                               \tag{9}
\]

which looks like the expected infrared pole. It nevertheless has a small but
nonzero overlap, approximately `9.67e-6`, with the static critical mode and
therefore develops an extremely narrow simple pole at `k_c(0)`. The scalar
channel hides most of the matrix failure; it does not remove it.

## Constructive Escape: Reduce Before Inversion

The strongest steelman is constructive. Let `B_o` span the three odd metric
coordinates

\[
 h_{yy}-h_{zz},\qquad h_{xy}-h_{xz},\qquad h_{yt}-h_{zt}, \tag{10}
\]

and define

\[
 M_o(q)=M_{\rm line}(q)B_o.                               \tag{11}
\]

The odd edge Ward column lies in `im M_o`. Pull it back to a three-coordinate
metric gauge vector and let `Z_m` span its orthogonal complement. Reducing the
action *before* inversion gives

\[
 H_m(q)=Z_m^\dagger M_o(q)^\dagger[-Q_\mu(q)]M_o(q)Z_m.   \tag{12}
\]

This two-dimensional kernel was positive semidefinite on the declared
`41 x 65` axial atlas from `k=0.001` through `pi` and `theta=0` through `pi`;
the smallest sampled eigenvalue was `2.4999998e-7`. At `L=72`, both source
representatives in (5)--(6) reduce to the same stress and give

\[
 C_{TT,\mathrm{metric}}=262.79514446.                    \tag{13}
\]

The result is independent of `mu` on this common-metric image because the
added curvature rows annihilate it. This is an explicit positive route, not a
claim that no physical reduction exists.

The order of operations is load bearing. Orthogonally projecting `o` and
`r_R` to the same metric-image edge vector but retaining the already inverted
raw covariance gives `-4685.00374`, not (13). In symbols,

\[
 P Q^{-1}P\ne(PQP)^{-1}.                                 \tag{14}
\]

Consequently the metric-first construction is new constraint/reduction law
data. It cannot be obtained by relabeling Block 184's raw GNS after the fact.
It remains to derive why the common-metric image, its source map, and its
constraint elimination are the physically selected objects.

## Why Flipping The Sign Is Not The Answer

The equal-magnitude counterfactual `mu=-1/1024` is informative. On the axial
odd sector it changes (2) into a positive rank-one update. It repairs the
`L=72` odd minimum, makes both source responses positive, retains exact Ward,
reflection, and Hermiticity, solves all 6,528 inherited closed neutral
Record-source modes, and preserves the static `k^2 h_tt -> 2` residue.

Those successes do not select the sign or magnitude. The same counterfactual
changes the zero-mode action inertia from `(7-,5+,10 zero)` to
`(10-,2+,10 zero)`, changes a held-out curvature response by an order-one
amount, and fails in the complementary even sector.

At `k=pi/2`, the even edge/gauge dimensions are `16/3`. For
`mu=-1/1024`, a physical eigenvalue crosses zero at

\[
 \theta_*=1.058285602655.                                \tag{15}
\]

The quotient inertia changes from `(3-,10+)` to `(4-,9+)`; at the root it is
`(3-,9+,1 zero)` and the 19-by-19 Ward border has minimum singular value about
`6.1e-15`. The supplied cross-TT source has nonzero null-mode overlap
`4.56621e-4`, and its response changes from approximately `+518` to `-517`
across a `2e-7` frequency bracket.

Moreover, inside the even conserved quotient, the kernel of `D` has dimension
eleven and inertia `(3-,8+)` at the three declared temporal controls. Those
three negative directions are invisible to every coefficient multiplying
`D^dagger D`. Thus the one-parameter curvature coefficient cannot make the
raw all-conserved-source edge form positive even when a larger negative
magnitude removes the particular crossing in (15).

The sign flip is therefore a diagnostic of the relative edge band, not a
derived action repair.

## Trace And Claim Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_bounded_theorem_note_2026-08-23
target_blocker_text: "the originally promised terminal route verdict is blocked until a physical reduction/section (or an inner product inducing one) and directed state/source/observable refinement law are supplied"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
raw_full_source_matrix_gns_verdict: bounded_infeasible
equal_magnitude_sign_flip_verdict: bounded_infeasible
physical_reduction_verdict: open
gravity_verdict: open
next_trace_action: "derive the metric-first/common-metric constraint reduction and Record coupling tau=M^dagger j from independent local physics, then certify every sector over the full Brillouin zone before returning to OS, quantum, Record, and refinement construction"
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs, Types, And Non-Imports

The result extends [Block 184's action-glued matrix
GNS](ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_GLUED_MATRIX_GNS_UNITARY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md)
using the supplied flat quadratic 22-edge reflected action from [Block
74](ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md),
not the distinct nonlinear 15-edge sourced Regge action in the neighboring
gravity lane. It consumes the exact Ward maps, line-metric map, local TT rows,
and the [Block 68 closed neutral Record-line source
convention](ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md)
from typed parents. It does not promote any parent to retained status.

No observed constant, continuum Einstein theorem, Lorentzian signature,
canonical lapse/shift constraint, positive-energy state, quantum commutator,
Record instrument, clock, refinement map, nonlinear background, audit verdict,
or axiom amendment is imported. `mu=1/1024`, its equal-magnitude sign flip,
the axial ray, and the declared numerical grids are finite-probe inputs rather
than empirical fits.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are contextual. They
expressly say that Admissibility does not choose a Hamiltonian or transfer
operator. They also do not choose this quadratic action, a metric-first
section, a physical source quotient, or the coefficient `mu`. No tension with
the axioms has been established.

## Polynomial And Numerical Certificate

With one exact Ward null, define

\[
 \Delta_\mu(k,\theta)=e_5(O_\mu)
 =\sum_{a=1}^{6}\det O_\mu[\widehat a,\widehat a].        \tag{16}
\]

It is the product of the five physical eigenvalues. On the axial odd sector,
`Delta_mu` is a degree-five polynomial in `cos(k)` and degree four in
`cos(theta)`. A 32-by-32 Fourier reconstruction agrees with held-out direct
determinants at relative error below `1e-12`. Transforming the reconstructed
polynomial to Bernstein form on

\[
 \cos k\in[-1,\cos k_c(\pi)],\qquad
 \cos\theta\in[-1,1]                                   \tag{17}
\]

gives nonnegative coefficients up to a `1e-10` floating boundary residue;
the smallest nonboundary positive coefficient is about `3.5e-8`. Because the
interior Bernstein basis functions are positive and the threshold corner is
simple, the physical inertia cannot change above (4). Direct quotient spectra
on a held-out grid provide an implementation-disjoint cross-check.

The certificate is bounded numerical/algebraic, not exact interval arithmetic.
An outward-rounded high-precision interval transform would strengthen the one
floating boundary coefficient into an exact interval theorem without changing
the route decision.

## No-Go Discipline

### N1 — Alternative-route enumeration

The campaign compared nine distinct continuations: raw all-source GNS;
TT-only GNS; common-metric restriction before inversion; post-inversion source
projection; stationary Schur/Dirac elimination; `mu=0` with relative modes
left null; the equal negative sign; a changed curvature/action family; and a
connection/holonomy or Lorentzian quantum construction. Only the first and the
equal-magnitude sign fit are stopped here. Metric-first reduction is a positive
counterexample to a broad gravity no-go.

### N2 — Wall-independence audit

The odd infrared wall is seen independently in the physical quotient
eigenvalue, the fifth-elementary polynomial, the Ward-border singular value,
and an exact periodic Record-source response. Source non-descent is checked by
the common-metric pullback rather than inferred from the hostile eigenvector.
The sign-flip failure is independently in the even sector and uses a cross-TT
source. No single eigensolver or source convention carries the conclusion.

### N3 — Hidden-wall scan

The result keeps open the action signature, physical source cone, canonical
constraint surface, lapse/shift typing, nonlinear background, boundary state,
positive-energy condition, time contour, off-axis momenta, refinement, and
Record clock. It does not assume that every edge coordinate is a graviton or
that every conserved edge covector is a licensed matter source.

### N4 — Residual matching

The bounded negative conclusion matches the computed residual exactly: the
raw full-edge inverse cannot be a positive form for all conserved sources and
cannot descend to metric source classes; the tested sign flip is not a global
repair. The surviving residual is constructive: derive and certify the
metric-first physical reduction and its source/Record transport.

### N5 — Execution resolutions

`per_element`: all six odd edge coordinates, all sixteen even edge
coordinates, their one/three Ward columns, and the two same-stress source
representatives are checked.

`per_site`: exact `L=71` and `L=72` periodic closed neutral line witnesses are
checked; arbitrary inhomogeneous lattices are not.

`per_mode`: the full temporal circle is certified on the safe axial odd domain,
and explicit odd/even pole locations are resolved below it.

`per_block`: the supplied action, source quotient, metric-first escape,
equal-magnitude sign counterfactual, 6,528 inherited source solves, and static
residue are separated.

`lattice_wide`: not executed—there is no full Brillouin-zone, nonlinear,
refinement, quantum Record, or gravity theorem.

### N6 — Rhetoric audit

The permitted language is “source-visible negative mode of the unreduced edge
covariance,” “raw full-source route failure,” and “physical reduction open.”
“Gravity fails,” “graviton ghost,” “no physical action,” and “axiom
contradiction” are not licensed.

### N7 — Partial-closure path scan

The common-metric reduction is positive and source-faithful on the declared
atlas, the local TT response retains the expected static residue, and the
negative-sign counterfactual shows that the odd obstruction is action
sensitive. These are real positive seams. They prevent the raw-edge failure
from being inflated into a theory-wide negative result.

### N8 — Cross-cycle echo

Blocks 180--184 independently identified source-representative ambiguity,
stationary-section poles, and the difference between a positive kinematic GNS
and a physical boundary law. The present same-stress witness resolves that
open question at one exact periodic mode, while the metric-first construction
recovers the previously named escape. The result generalizes the route map; it
does not merely repeat an earlier negative sample.

**N1--N8 status: PASS.**

## Decision And Next Campaign

The highest-leverage next campaign is not more raw GNS work and not coefficient
scanning. It is to derive the common-metric/constraint reduction from
independent local physics:

1. identify the canonical presymplectic or constraint surface before
   inversion;
2. prove that Record matter couples only through
   `tau=M^dagger j`, including refinement transport;
3. eliminate gauge, lapse/shift, and relative-orientation variables without a
   momentum-fitted or singular section;
4. certify the resulting physical kernel over the full Brillouin zone and
   both reflection sectors; and
5. only then construct OS/positive-energy, quantum state, unitary dynamics,
   and operational Record instrumentation.

If this reduction cannot be derived and unreduced Record edge modes are
instead declared physical, equation (8) is a genuine ghost of that candidate
edge theory and the action must change. That decision is downstream law work,
not an axiom amendment.

## TOE Lane Accounting

| TOE lane | repository | physical | autonomous | movement |
|---|---:|---:|---:|---:|
| operational / Records | 95% | 92% | 50% | `0` |
| causal order / time | 76% | 72% | 41% | `0` |
| inertia / matter | 95% | 96% | 75% | `0` |
| gravity / source / resources | 70% | 45% | 29% | `0` |
| Born / history | 84% | 63% | 34% | `0` |

The percentage map is unchanged because no retained obligation is retired.
The route confidence changed materially: the raw full-source GNS and the
equal-magnitude sign fit are demoted, while metric-first constraint reduction
is promoted to the dominant gravity seam.
