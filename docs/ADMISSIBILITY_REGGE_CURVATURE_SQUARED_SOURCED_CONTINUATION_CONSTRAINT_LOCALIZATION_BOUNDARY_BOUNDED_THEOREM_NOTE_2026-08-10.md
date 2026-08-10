---
claim_id: admissibility_regge_curvature_squared_sourced_continuation_constraint_localization_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the actual four-dimensional Kuhn/Coxeter Regge family S_alpha=sum_h A_h(epsilon_h+alpha epsilon_h^2), the Block-19-connected unsourced homogeneous stationary branch has a high-precision numerical saddle-node at alpha=0.0003941858600..., below the supplied flat repair alpha=1/1024. At alpha=1/1024 all three retained compact source covectors instead have interval-certified nearby five-normal stationary continuations from flat, but the complete off-flat Bloch Hessian on the largest Bundle-B continuation has double-precision-bracketed inertia crossings under both named affine constraint extensions: x=0.0240357490... along k=x(1,0.7,-0.4,0.2) for global-only constraints and x=1.9834291011... after constant pointwise five-normal projection. Independently, two root-of-unity flat momenta and exact positive-semidefinite coefficient monotonicity show that no real alpha in this one-parameter action family can retain five-normal inertia 4-negative/1-positive under the constant pointwise-affine localization at both witnesses: one requires alpha>21/4096 while the other requires alpha<20/4096. This is a bounded failure of that action/localization pair and a diagnosis of the two named sourced extensions, not a gravity no-go, continuous-zone theorem, interval certificate for the fold or momentum roots, action-selection result, Lorentzian stability result, or exclusion of the full gauge quotient, a covariant constraint localization, a richer local action, a nonuniform full field solution, or another realized geometry/history law."
upstream_dependencies:
  - minimal_axioms
  - admissibility_fixed_metric_nonlinear_regge_kkt_continuation_boundary_bounded_theorem_note_2026-08-10
  - admissibility_flat_regge_curvature_squared_branch_lift_boundary_bounded_theorem_note_2026-08-10
  - admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py
---

# Regge Curvature-Squared Sourced Continuation And Constraint Localization Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** test whether the Block-20 flat repair survives the first nonlinear
sourced backgrounds, and determine whether coefficient tuning can rescue the
constant pointwise-affine constraint extension.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py](../scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py)

## Result Up Front

Block 20 found a real flat weak-field repair. For

    S_alpha = sum_h A_h (epsilon_h + alpha epsilon_h^2),              (1)

the curvature-square term is local, leaves the Einstein `O(k^2)` term
unchanged at leading infrared order, lifts the unwanted fifth flat branch,
and preserves the intended four gauge zeros on the full flat symbol. The
bounded full-symbol tests admit a coefficient interval rather than selecting
one point.

The nonlinear sourced question is harder. This block differentiates (1)
away from the flat anchor, including every term in

    Hess(A epsilon^2)
      = epsilon^2 Hess(A)
        + 2 epsilon [dA tensor d epsilon + d epsilon tensor dA]
        + 2 A d epsilon tensor d epsilon
        + 2 A epsilon Hess(epsilon).                                  (2)

There are three main findings.

First, the unsourced nonflat Block-19 branch is not carried continuously to
the supplied repair point. The stationary equations and the determinant of
their symmetric two-coordinate Hessian vanish together at the numerical fold

    a_fold     = 0.00331923225513...,
    u_fold     = 0.0654141134844...,
    alpha_fold = 0.000394185860010... .                               (3)

This lies well below

    alpha_repair = 1/1024 = 0.0009765625.                             (4)

Equation (3) tracks the branch connected to the Block-19 root. It does not
prove that no disconnected nonflat stationary root exists.

Second, the three retained compact source covectors do have nearby stationary
continuations from flat at (4). With the same supplied coupling `1/100`, their
five normal equations have interval Krawczyk certificates and nondegenerate
inertia

    4 negative, 1 positive.                                           (5)

The largest deformation is Bundle B, whose fifth normal coordinate is
approximately `0.00937628428`. Its full off-flat Hessian is independently
validated against a periodic extended-action second difference.

But this sourced background does not retain one inhomogeneous inertia under
either affine extension inherited from Block 19. Along

    k = x (1, 0.7, -0.4, 0.2),                                       (6)

the global-only `15x15` Hessian changes from `7-/8+` to `8-/7+` at

    x_global = 0.0240357490... .                                      (7)

The constant pointwise five-normal projection changes from `4-/1+` to
`5-/0+` at

    x_pointwise = 1.9834291011... .                                   (8)

These are high-precision numerical brackets with independently validated
matrix construction. They are not interval root theorems.

Third, retuning `alpha` cannot make the constant pointwise-normal extension
healthy everywhere even on the flat background. Let `N` be the fixed exact
five-normal basis used by Block 19 and

    H_N(k,alpha) = N^dag Q_R(k) N + alpha N^dag R_2(k) N.              (9)

The second term is positive semidefinite. At the root-of-unity momentum

    k_L = (2 pi/3, -pi/2, 2 pi/3, -pi/2),                             (10)

`H_N(k_L,21/4096)` is still negative definite; its largest eigenvalue is
below `-0.22`. Monotonicity therefore makes `4-/1+` impossible for every
`alpha<=21/4096`, so the target requires

    alpha > 21/4096.                                                  (11)

At the separate root-of-unity momentum

    k_U = (0, 3 pi/4, 3 pi/4, 3 pi/4),                               (12)

`H_N(k_U,20/4096)` already has inertia `3-/2+`; its smaller positive
eigenvalue exceeds `0.37`. Monotonicity preserves at least two positive
directions for every larger coefficient, so the target requires

    alpha < 20/4096.                                                  (13)

Since `21/4096 > 20/4096`, (11) and (13) have no overlap. This is a
two-witness no-overlap result for the one-parameter action (1) under the
constant pointwise-affine localization. It is not a gravity no-go. At both
witness momenta the full flat repaired symbol at (4) still has the intended
`9-/2+/4-zero` inertia. The viable full gauge quotient, a momentum-covariant
constraint complement, additional local curvature invariants, and a full
nonuniform sourced field solution all remain live.

As an independent numerical control, whitening each positive-definite
restricted correction gives the generalized coefficient-crossing intervals
for exactly `4-/1+` inertia:

    k_L: (0.00568533816453..., 0.00898484714225...),
    k_U: (-0.0155808461836..., 0.00440073542103...).                  (14)

These intervals are disjoint and strictly strengthen the conservative dyadic
separator (11)--(13). Equation (14) is a double-precision pencil calculation;
the logical no-overlap uses the displayed dyadic sign margins and exact
positive-semidefinite ordering.

## 1. Retained Inputs And Exact Scope

The calculation uses only repository-local carriers:

- the current [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) and approved
  [scale](SCALE_REFERENCE_PRIMITIVE_NOTE.md),
  [isotropy](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md), and
  [realized-state](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) primitives;
- the actual 50-hinge, 15-edge [Kuhn/Coxeter Regge action and Bloch
  carrier](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md);
- [Block 17's three compact source
  covectors](ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md);
- [Block 19's exact five-normal basis, affine constraints, coupling, and
  interval-certified Einstein-action source
  continuations](ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md); and
- [Block 20's flat curvature-square action, Gram Hessian, gauge kernel, body
  source, finite-torus inventory, and bounded coefficient
  window](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md).

The following are fixtures, not derived consequences:

1. Euclidean signature;
2. the action family (1);
3. `alpha=1/1024` for the sourced continuation;
4. the compact source covectors and coupling `1/100`;
5. homogeneous edge-class backgrounds;
6. the ten affine fixed-metric constraints;
7. either global-only or constant pointwise localization of those
   constraints; and
8. the interpretation of inherited Hessian inertia as the tested stability
   diagnostic.

The present result neither changes canonical axioms nor raises campaign
percentages.

## 2. Full Off-Flat Curvature-Square Hessian

At flatness, only the Gram term in (2) survives:

    R_2(k) = 2 sum_h A_h d_h(k)^dag d_h(k).                            (14)

Away from flatness all four terms in (2) are required. The runner reconstructs
them in real space. Each area Hessian is analytic. Each deficit Hessian is the
sum of the actual ten-edge dihedral Hessians in the hinge star; these are
evaluated by complex-step differentiation of the retained analytic dihedral
gradients and symmetrized before assembly.

Two independent reductions validate the construction:

1. At the flat anchor, the complete formula reduces to Block 20's Gram kernel
   with maximum entry error below `2e-10`.
2. At a nonflat homogeneous background, its `k=0` projection agrees with an
   independent automatic-differentiation Hessian of the complete action (1)
   below `2e-10`.

On the sourced Bundle-B background, an independent periodic `L=3` action
second difference at `k=(2 pi/3,2 pi/3,0,0)` agrees with the Bloch prediction
to relative error below `2e-6` (the observed runner value is much smaller).
Thus the crossings (7)--(8) are not obtained by inserting an ad hoc spectral
projector.

## 3. Unsourced Branch Fold

Block 19 selects two coordinate-symmetric normal variables `(a,u)` and three
anisotropic variables. Along the symmetric subspace, define

    F(a,u,alpha) = grad_(a,u) S_alpha.                                 (15)

The fold calculation solves

    F_a = 0,
    F_u = 0,
    det Hess_(a,u) S_alpha = 0.                                      (16)

High-precision Newton iteration from the continued Block-19 branch yields
(3), with the stationary residual and Hessian determinant below the runner's
declared tolerances. Direct continuation from the Block-19 root through

    alpha = 0, 0.0002, 0.00036, 0.00039, 0.000394

keeps the branch stationary and decreases its positive symmetric Hessian
eigenvalue through approximately

    3.15141, 1.74729, 0.506561, 0.144821, 0.0277814.

At (3), the other eigenvalue is approximately `-43.0376`; the null-direction
parameter transversality is `114.484...`, and the null-direction quadratic
coefficient is `17.2157...`. Both are nonzero numerical saddle-node
nondegeneracy controls. This is still a numerical saddle-node witness, not an
interval certificate and not a route-exhaustion statement. In particular:

- it does not exclude another unsourced stationary branch;
- it does not say a physical sourced geometry should be obtained by
  continuing the arbitrary Block-19 unsourced fixture; and
- it does not select (4).

Its positive content is narrower: the two Block-20 statements “the old
nonflat background is unstable” and “the flat action is repaired” cannot be
silently spliced into one background. Changing the action changes the
stationary-background problem first.

## 4. Sourced Continuations At The Repair Point

For each retained source covector `J`, the normal equations are

    grad_N S_(1/1024)(x) = (1/100) N^T J.                             (17)

Newton iteration from flat finds all three solutions. Interval Krawczyk maps
on radius-`2e-9` boxes lie strictly inside their boxes, certifying one root in
each declared neighborhood. Their approximate centers are:

| source | five normal coordinates |
|---|---|
| two-stream | `(-0.0000404757, 0.0004062061, -0.0001685019, -0.0001685019, -0.0026694261)` |
| Bundle A | `(0.0005306155, -0.0016283518, -0.0016283518, -0.0016283518, -0.0002842484)` |
| Bundle B | `(-0.0002118903, 0.0012366780, 0.0012366780, 0.0012366780, 0.0093762843)` |

All three five-normal Hessians have (5). This is genuine nonlinear sourced
progress: the flat action repair is not confined to the exactly zero-source
normal equation.

It is not full sourced gravity. Equation (17) freezes ten affine metric
tangents and replaces them with reactions. The compact source, its coupling,
and its homogeneous background representative are supplied. A complete
geometry law must still specify the source and constraint fields over the
lattice and their transformation under the realized gauge and Lorentzian
evolution.

## 5. Why The Sourced Inhomogeneous Test Fails

On Bundle B, the complete global-only Hessian at `k=0` has no exact gauge
kernel and has inertia `7-/8+`. Along (6), four small branches cross in the
near-infrared before additional crossings occur. Equation (7) is the first
generic simple crossing on the declared path.

This does not establish a physical gauge anomaly. The background is
stationary only after affine reactions, while the straight edge-coordinate
Hessian is being tested without a covariant nonlinear constraint/source
connection. At an off-shell or constrained point, a nonlinear gauge-orbit
second variation contains gradient and constraint-curvature terms that vanish
at the flat stationary anchor but need not vanish here. The calculation shows
that those terms cannot be omitted and then replaced by the expectation that
the four flat zero modes remain exact.

The constant pointwise-normal projection removes those would-be gauge
directions by construction, but (8) shows a separate physical-sign crossing.
The two-witness argument (10)--(13) proves that this failure cannot be repaired
at all momenta merely by retuning the single coefficient in (1).

The immediate fix is therefore structural:

1. select the realized constraint localization and source transformation law;
2. compute the covariant sourced second variation on the resulting constraint
   and gauge quotient;
3. solve the full nonuniform sourced field equations rather than treating a
   homogeneous affine KKT surrogate as the finished geometry; and
4. only if that selected quotient still fails, enlarge the local action basis
   and derive its coefficients before testing Lorentzian nonlinear stability.

## 6. Candidate Geometry-Law Wording (Unadopted)

The evidence sharpens the sufficient or target-equivalent candidate from
Block 20. It does not prove this wording minimal or necessary and does not edit
the canonical axiom memo:

> A realized geometry/history law selects a local lattice-covariant geometry
> action and its dimensionless coefficients, a law-admissible sourced
> background or boundary sector, and the localization and nonlinear geometry
> of every constraint. About each selected sourced background, the covariant
> sourced second variation on the selected constraint and gauge quotient has
> no unintended zero modes or inertia crossings on realized momentum support,
> preserves the intended infrared gravitational pole and source Ward identity,
> and admits stable Lorentzian nonlinear evolution with the same source law.

The phrase “covariant sourced second variation” matters. The present failure
comes from treating a supplied affine Hessian extension as if it were already
the law-selected physical quotient. The current axioms do not make that
selection. This candidate may instead be derived from a stronger admissibility
or realized-history theorem; adoption requires explicit user/governance
authority.

## 7. No-Go Discipline Gate

The bounded negative claim in this note is only:

> No real `alpha` in the one-parameter family (1) gives inertia `4-/1+` at
> both fixed momenta (10) and (12) under the constant pointwise five-normal
> localization (9).

It is not “Regge gravity fails,” “curvature-squared repair fails,” or “no
sourced geometry exists.” The following N1--N8 stress test is part of the
claim contract.

### N1 — Alternative route enumeration

The exact target contract is: for all real `alpha`, test simultaneous
`4-/1+` inertia of the two fixed `5x5` pencils (9) at (10) and (12), using
only the fixed Block-19 normal subspace and the one-parameter action (1). A
completion witness is either one common coefficient or a proof that the two
target intervals do not intersect. Changing the action, constraint subspace,
background, target inertia, or witness momenta does not count as refuting this
contract; those changes instead test whether a broader physical claim would
be an overclaim.

| Family | Object / mechanism / terminal obligation | Outcome | Honesty marker |
|---|---|---|---|
| generalized-pencil intersection | whiten each positive-definite `N^dag R_2 N`, compute the five coefficient crossings, and intersect the first-inertia chambers | (14) gives disjoint target intervals | `ATTEMPTED` |
| dyadic Loewner separator | use exact PSD ordering and robust signs at `21/4096` and `20/4096`; prove reversed necessary half-line bounds | (11)--(13) close every real coefficient without sampling between them | `ATTEMPTED` |
| constant-basis reparametrization | replace `N` by `NB` for any invertible constant `B`; use Sylvester congruence, as in the [Block-19 chart audit](ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md#7-no-go-discipline-gate) | inertia is unchanged, so a chart change cannot create overlap | `ATTEMPTED` |
| boundary or singular-coefficient loophole | test equality at both dyadic separators and allow a zero eigenvalue as a candidate endpoint | the margins `-0.227754...` and `+0.373824...` exclude equality; a zero mode also fails the zero-free `4-/1+` target | `ATTEMPTED` |
| witness-construction adversary | reconstruct the flat correction from all 50 hinges, reduce it to the Block-20 Gram kernel, and challenge phase/action normalization with the independent reductions in Sections 2 and 9 | the witness matrices and positive correction survive; only interval certification of their decimal signs remains unexecuted | `ATTEMPTED` |
| full-symbol scope adversary | abandon constant `N` and test the complete repaired `15x15` symbol at the same two momenta, using the [Block-20 full-quotient construction](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md#result-up-front) | it succeeds with `9-/2+/4-zero`; this defeats every broad gravity reading but changes the exact target | `ATTEMPTED` |

These are distinct by primary object or invariant: matrix-pencil chamber
intersection, Loewner half-line separation, congruence invariance, endpoint
degeneracy, action-level matrix reconstruction, and the full quotient. The
narrow no-overlap passes. Momentum-covariant constraints, nonlinear
connection terms, richer actions, nonuniform solutions, and Lorentzian
evolution remain live because they alter the target rather than evade its
proof.

### N2 — Wall-independence audit

The collapsed wall set is:

- `W1`: flat Euclidean Kuhn/Coxeter geometry;
- `W2`: the one-parameter action (1), with no additional invariant;
- `W3`: the fixed constant Block-19 normal subspace `range(N)`;
- `W4`: the zero-free target inertia `4-/1+`;
- `W5`: the two fixed momenta (10) and (12); and
- `W6`: double-precision certification of the displayed matrix signs rather
  than an interval/exact algebraic matrix proof.

| Pair | close first => second? | close second => first? | independent? |
|---|---|---|---|
| `W1,W2` | no | no | yes |
| `W1,W3` | no | no | yes |
| `W1,W4` | no | no | yes |
| `W1,W5` | no | no | yes |
| `W1,W6` | no | no | yes |
| `W2,W3` | no | no | yes |
| `W2,W4` | no | no | yes |
| `W2,W5` | no | no | yes |
| `W2,W6` | no | no | yes |
| `W3,W4` | no | no | yes |
| `W3,W5` | no | no | yes |
| `W3,W6` | no | no | yes |
| `W4,W5` | no | no | yes |
| `W4,W6` | no | no | yes |
| `W5,W6` | no | no | yes |

No pair collapses. The proof itself uses two independent momentum matrices
and one exact structural fact: `R_2` is positive semidefinite. At `k_L`,
negativity at `21/4096` propagates to every smaller coefficient. At `k_U`,
two positive directions at `20/4096` persist for every larger coefficient.
The numerical wall is only certification of those two signs. Their margins
exceed `0.2` and `0.3`, while the restricted corrections have minimum
eigenvalue above `40`; this remains a bounded double-precision result rather
than an interval matrix theorem.

### N3 — Hidden-wall scan

The prescribed phrase scan gives:

| Hit | Classification | Disposition |
|---|---|---|
| “background” | hidden condition when it denotes the flat or sourced carrier | promoted to `W1`; sourced-background claims are separately bounded in Sections 4--5 |
| “by construction” in the pointwise gauge removal | hidden condition | promoted to `W3`; constant `N` is not treated as a derived covariant constraint law |
| “inherited” target inertia | hidden condition | promoted to `W4` |
| “root-of-unity momentum” / fixed witnesses | hidden condition | promoted to `W5` |
| “exact” PSD ordering | cited derived fact | retained as the Block-20 Gram identity; it does not make the decimal witness signs exact |
| “canonical axiom memo” | non-load-bearing governance context | no scientific premise is taken from the label |
| “current axioms do not select” | source-bound premise boundary | checked against the current memo and approved primitive registry; it is not phrased as a universal no-go |

No remaining occurrence of “we assume,” “as is standard,” “the framework
provides,” “bridge context,” “naturally,” “obviously,” or “standard QFT” is
load-bearing. Promoting the four hidden conditions above produces exactly the
six-wall set already audited in N2.

### N4 — Residual matching

No prior negative result is load-bearing for (11)--(14); the current two
matrices prove the narrow residual directly. Prior blocks are carrier or
motivation only, and their residuals are explicitly not counted as witnesses:

| Cited source | Its residual | Current residual | Match? |
|---|---|---|---|
| [Block 17, source line 4](ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | flat `k=0` null-space reaction rank | coefficient overlap of two nonzero-momentum normal pencils | no; provenance only |
| [Block 18, source line 4](ADMISSIBILITY_NONLINEAR_REGGE_EXTRA_BRANCH_CUBIC_LIFT_SOURCE_COMPATIBILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | leading-cubic source-image mismatch | coefficient overlap under fixed pointwise normals | no; provenance only |
| [Block 19, source line 4](ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | homogeneous affine KKT existence and mixed inertia at one background | simultaneous inertia at two flat momenta | no; supplies `N` and the target only |
| [Block 20, source line 4](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | full-symbol repair interval plus two different nonflat numerical crossings | constant-normal coefficient overlap at two new witnesses | no as a negative witness; supplies `Q_R`, `R_2`, and the full-quotient escape |

After dropping all four nonmatching residuals, the witness count required by
the proof is unchanged: it is the two current momentum matrices. The lower
witness leaves `alpha>21/4096`; the upper leaves `alpha<20/4096`; their
intersection is empty. For the sourced result, both tested affine extensions
have one bracketed crossing on one Bundle-B path. A covariant quotient and a
full source field were not tested and remain named work.

### N5 — Rhetoric audit

| Resolution | Executed evidence | Negative conclusion allowed? |
|---|---|---|
| per element | all 15 edge classes enter the reconstructed Hessian | no per-edge no-go; only matrix construction is checked |
| per site | all 50 hinge classes and 240 local incidences enter | no per-hinge no-go |
| per mode | exactly the two coefficient witnesses plus one sourced path are tested | yes, only at the named modes/path |
| per block | the fixed five-normal block and full `15x15` escape are compared | yes, only for those two formulations |
| lattice-wide | no continuous-zone or full source-field theorem is executed | no lattice-wide physical no-go |

Permitted language is “two-witness no-overlap for the constant pointwise-
affine one-parameter family” and “the two named sourced extensions are not yet
stable.” Forbidden language includes “gravity is impossible,” “all Regge
actions are unstable,” “no coefficient works physically,” and “the axioms
are inconsistent.” The primary cached stdout lands one substantive line for
each resolution class.

### N6 — Partial-closure path scan

This block advances three positive paths:

1. the full off-flat curvature-square Hessian is constructed and independently
   validated;
2. all three compact sources have interval-certified nonlinear normal
   continuations at the repair point; and
3. the failure is localized to background/constraint/source completion rather
   than the existence of a flat local repair.

Those gains survive the negative result. The approved primitives are not
walls and are not enlarged:

| Registered primitive | Exact grant | Does it close the present selection? |
|---|---|---|
| `scale_reference_primitive` | units conversion only | no dimensionless action coefficient or constraint law |
| `kinetic_isotropy_primitive` | structural OS0 kinetic-form isotropy only | no dynamics, Lorentz-closure theorem, or sourced quotient |
| `realized_state_primitive` | pointwise evaluation at a supplied law-admissible state | no background, state, source, measure, or selection rule |

The candidate wording in Section 6 is therefore not labeled “a new axiom is
required.” It may be derived by an admissibility/history theorem, implemented
as an explicit bounded law input and later retired, or replaced by a
momentum-covariant constraint construction. No convention reframe alone can
change the two fixed matrix inertias, but it can correctly reclassify constant
`N` as a nonphysical coordinate surrogate rather than a failed gravity law.

### N7 — Steelman

The strongest hostile case is that the constant pointwise-normal extension
was never a credible covariant physical law. Construct a momentum- and
background-dependent complement `N(k,l_*)`, include the second fundamental
form/connection terms of the nonlinear constraints and the transformed source
law, solve the full nonuniform sourced Euler--Lagrange/KKT equations, and then
diagonalize the true gauge quotient. Its terminal obligation is a continuous-
momentum quotient theorem followed by Lorentzian nonlinear stability. That
mechanism could completely remove the two present crossings and is supported
by the healthy full-symbol escape at both witnesses. This steelman defeats a
broad gravity or action no-go, so those claims are demoted and forbidden. It
does not refute the exact fixed-`N`, one-parameter, two-momentum theorem, which
is why only that narrow statement ships.

### N8 — Cross-cycle echo

| Prior wall | Later retirement mechanism | Echo applied here |
|---|---|---|
| Block 17: a flat quadratic source needs an extra reaction channel | Block 18/19 used native nonlinear lift and a nonzero stationary background | do not turn a flat fixed-normal defect into a nonlinear gravity no-go |
| Block 18: the leading cubic image misses the declared sources | Block 19 solved the complete nonlinear five-normal source equations | preserve higher-order/full-equation completion routes |
| Block 19: mixed Euclidean inertia on one affine surface | Block 20 changed the action and repaired the flat full symbol | action enlargement and a true quotient remain live |
| Block 20: two supplied nonflat affine extensions have soft modes | this block finds repaired sourced roots but again localizes failure to affine extensions | promote covariant constraint/source geometry instead of echoing a universal instability |

Earlier walls were retired by changing the background, using the full
nonlinear equation, or changing the action. Those same mechanisms are
explicitly preserved here. The source roots close a normal equation while
their full spectra remain open; the flat repair closes a branch obstruction
while its nonlinear sourced law remains open. **N1--N8 status: `PASS` only for
the fixed-`N`, one-parameter, two-witness no-overlap.**

## 8. Promotion Value And Cluster Gate

| Gate | Evidence |
|---|---|
| V1 — specific obstruction | Block 20 explicitly leaves nonlinear sourced completion and constraint localization open. This block executes both tests and isolates the failing surrogate. |
| V2 — new derivation | No upstream note contains the full off-flat Hessian (2), fold (3), repaired source roots, sourced Bloch crossings, or the reversed dyadic bounds (11)--(13). |
| V3 — generic machinery | Krawczyk and Loewner monotonicity are generic, but the five-normal sources, 50-hinge Hessian, two witness matrices, and margins are carrier-specific computations. |
| V4 — marginal content | The result changes the next action: stop tuning one coefficient under constant pointwise constraints; construct the selected covariant sourced quotient. |
| V5 — independently reviewable | The claim has a distinct nonlinear sourced carrier, independent action check, and a finite two-witness proof object. It is not another coefficient sample. |

**Cluster verdict: `OPEN` as a separate stacked science block.** The parent
coefficient-window extension concerns the flat full symbol. This claim concerns
off-flat sourced continuation and proves a localization-specific coefficient
incompatibility that the parent does not contain. Folding it into the flat
repair would obscure the premise change. Independent audit remains required.

## 9. Verification

Run:

```bash
python3 scripts/admissibility_regge_curvature_squared_nonflat_continuation_2026_08_10.py
```

The runner checks:

1. current-axiom and approved-primitive non-supply boundaries;
2. reduction of the off-flat Hessian to the exact flat Gram kernel;
3. an independent automatic-differentiation `k=0` reduction off flat;
4. numerical continuation from the Block-19 root, the unsourced branch fold,
   and both saddle-node nondegeneracy coefficients;
5. three sourced Newton continuations and three interval Krawczyk boxes;
6. the Bundle-B `k=0` Hessian and independent periodic nonzero-mode action
   difference;
7. global-only and pointwise sourced determinant brackets;
8. the two root-of-unity dyadic no-overlap witnesses and an independent
   generalized-pencil interval calculation; and
9. survival of the full flat gauge-quotient inertia at those same witnesses.

The canonical axiom memo and fixed TOE percentages are unchanged. No
`review-loop` is used.

## Boundary Verdict

Gravity is not closed, but the failure is now localized. The local
curvature-square term genuinely repairs the flat full symbol and supports
three nearby nonlinear sourced normal roots. It does not turn either supplied
affine constraint extension into a stable sourced gravity law. The old
unsourced nonflat branch folds before the repair point; the repaired Bundle-B
background has inhomogeneous crossings under both named extensions; and no
single `alpha` can make the constant pointwise-normal version retain its
inherited inertia even at two fixed flat momenta.

The highest-value fix is not another scalar coefficient scan. It is to derive
the realized source and constraint localization, form the covariant sourced
gauge-quotient second variation on a full field-equation background, and test
its continuous momentum and Lorentzian nonlinear stability. Only if that
selected construction still fails should the local action basis be enlarged.
The current axioms do not yet supply that selection; the candidate wording in
Section 6 records the exact obligation without adopting a new axiom.
