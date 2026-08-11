---
claim_id: admissibility_global_constraint_phase_ward_contact_reclassification_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the retained Block-19 globally constrained homogeneous Regge ensemble, all six Block-23 source-mass modes lie in the ten-dimensional constant-metric image and have zero intersection with the allowed compact tangent ker(M0^T); their 6x6 source coefficients are therefore transverse curvatures of directions excluded at k=0, not on-domain compact Hessian entries. Translation invariance makes the same uniform background stationary against every nonzero Bloch variation, so extending the six modes away from k=0 is a global-only ensemble and phase choice. The complete 61-orbit one-cell metric contact fits the three homogeneous matrices but its eleven-dimensional nullspace exposes only rank four to six held-out finite-momentum gauge-gauge Ward probes and leaves a relative incompatibility above 0.75. A stronger complete direct-edge one-cell class has 1,800 monomials in 142 simultaneous-axis orbits, fits the homogeneous matrices with rank 50 and nullity 92, and learns a small/axis training inventory, but fails held-out generic and root-of-unity Ward data. An independent neutral closed-history construction on the unchanged L=5 flat Regge carrier has zero compact source and solves all 100 nonzero sourced modes without projection. This reorders the gravity priority: select the physical ensemble and massless versus curved phase before selecting target-fitted homogeneous contact coefficients. It is not a gravity no-go, continuous-zone theorem, selected Record-to-geometry law, projective joint family, Lorentzian dynamics theorem, axiom necessity result, or axiom adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_fixed_metric_nonlinear_regge_kkt_continuation_boundary_bounded_theorem_note_2026-08-10
  - admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_bounded_theorem_note_2026-08-10
  - admissibility_endogenous_geometry_joint_record_rn_local_covariant_contact_selection_boundary_bounded_theorem_note_2026-08-10
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_global_constraint_phase_ward_contact_reclassification_2026_08_10.py
---

# Global-Constraint Phase / Ward Contact Reclassification Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** phase/ensemble ordering correction, finite-momentum contact
discriminator, constructive nonuniform escape, and narrowed axiom/law delta
**Scope:** the supplied Block-19 global compact ensemble, the three Block-23
homogeneous source tangents, the complete Block-28 metric-cell contact class,
one stronger direct-edge cell class, six held-out momenta, and the complete
`L=5` neutral closed-history torus.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_global_constraint_phase_ward_contact_reclassification_2026_08_10.py](../scripts/admissibility_global_constraint_phase_ward_contact_reclassification_2026_08_10.py)

## Result Up Front

The 11-dimensional Block-28 coefficient ambiguity is real, but it is not yet
the first physical gravity question.

Block 19 imposed the ten global affine constraints

    M0^T (ell-ell_flat)=0.                                      (1)

Let `P` be the `15 x 6` orthonormal matrix of Block-23 flat physical modes.
The runner reconstructs

    P subset image(M0),
    rank(M0^T P)=6,
    image(P) intersect ker(M0^T)={0}.                           (2)

Thus all six directions on which Blocks 22--28 define and cancel the
homogeneous source-mass matrices are **excluded at k=0** by the supplied
compact ensemble. Those matrices are transverse curvatures of a proposed
extension; they are not on-domain entries of the compact KKT Hessian.

A uniform first variation has only zero Fourier momentum, so the same
background is stationary against every nonzero Bloch variation. Under the
**global-only extension**, the six directions re-enter for arbitrarily small
nonzero momentum. Their `O(source)` coefficients then distinguish a massless,
curved, or massive phase. The correction is one of logical ordering:

> **Phase/ensemble selection precedes coefficient selection.**

If the law selects the constrained curved or massive phase, no homogeneous
contact cancellation is required. If it selects a massless source-deformed
phase, an inter-cell term, refined/perfect action, or the full background Ward
connection must close the complete momentum-dependent identity. Fitting the
six excluded compact directions alone is insufficient.

The finite-momentum tests make this concrete:

1. The complete 61-orbit metric-cell family fits the homogeneous matrices with
   rank 50 and nullity 11. Six held-out generic and root-of-unity momenta see
   only four of the eleven blind directions; the best nullspace adjustment
   leaves relative incompatibility above `0.75`.
2. The stronger actual-edge family contains all `1,800` monomials
   `J_e u_f u_g` and reduces to exactly **142 direct-edge orbits**. Its
   homogeneous design has rank 50 and nullity 92. It learns a small-momentum
   and coordinate-axis training inventory while preserving the homogeneous
   fit, but fails the **held-out finite-momentum Ward data**.
3. The retained neutral pair of closed histories has zero compact source and,
   on the complete `L=5` torus, all 100 nonzero sourced modes satisfy the
   actual Ward/null conditions and solve without source projection.

Gravity has a live explicit linear-response route. What fails is promoting a
homogeneous target fit into a selected all-momentum law. This is **not a
gravity no-go**.

No canonical axiom is edited here. Fixed TOE percentages remain unchanged.

## 1. Exact Variational-Domain Theorem

Block 19 supplies the full-column-rank map

    M0 : R^10 -> R^15                                      (3)

and the compact tangent `ker(M0^T)`. Block 23 supplies six columns `P` in
`image(M0)`. If `v` belongs to both spaces, then `v=M0 h` and

    0=h^T M0^T v=h^T M0^T M0 h=||M0 h||^2=||v||^2.          (4)

Hence `v=0`. Because `P` has rank six, `rank(M0^T P)=6` exactly. Numerical
singular values and the image residual check conditioning, not the proof.

The Block-23 matrices

    Ms=P^dagger Ds(0) P                                    (5)

are therefore transverse curvatures. They remain valid diagnostics for a
separately selected massless global-only phase, but are not Hessian entries on
the supplied compact variational domain.

This retires treating cancellation of (5) as logically prior to selecting the
ensemble. It preserves massless extensions, curved or massive phases, open
boundaries, fixed global modes, covariant constraints, and nonuniform
backgrounds.

## 2. Translation And Constrained Stationarity

On a periodic translation-invariant action, the first variation at a uniform
background is uniform. Pairing it with a nonzero Bloch variation gives

    sum_x exp(i k dot x)=0,       k != 0.                    (6)

The runner checks (6) on all 624 nonzero momenta of the `L=5` four-torus.
Only `k=0` needs the reactions in (1). The Block-19 branch is thus stationary
on its declared globally constrained torus; the open question is which
constraint/phase law is physical.

## 3. Differentiated Ward Discriminator

Let `Q(c,k)` be the geometry Hessian, `R(c,k)` a background generator, and
`C(c,k)` an additional contact. At zero source, `Q0 R0=0`. Differentiation
has the schematic form

    [D+C]R0+Q0 R1+connection/tadpole+joint-sector=0.          (7)

When the final two terms are absent, left multiplication by `R0^dagger` gives
the necessary pure-quadratic discriminator

    R0^dagger [D+C] R0=0.                                  (8)

The runner uses (8) only for the declared one-cell classes. Its failure does
not exclude the omitted terms in (7).

### 3.1 Complete metric-cell class

For the Block-28 design

    D_metric : R^61 -> R^216,
    rank D_metric=50,
    nullity D_metric=11.                                   (9)

The exact lattice gauge row is pulled through the full-rank metric map at each
held-out momentum. If `N` spans the homogeneous nullspace, the stacked Ward
system obeys

    rank(WN)=4.                                            (10)

The best solution of `WN z=b-Wc0` leaves relative residual above 0.75. The
data neither select all eleven directions nor agree with the homogeneous
one-cell family. The executed value is `0.814467`, with metric-gauge map
residual `4.638e-15`.

### 3.2 Complete direct-edge class

The stronger one-cell action is

    O_J(u)=1/2 sum_(e,f,g) a_[e,f,g] J_e u_f u_g.            (11)

There are `15 x 120=1,800` monomials. Simultaneous axis permutations give:

| orbit size | number |
|---:|---:|
| 1 | 1 |
| 3 | 1 |
| 4 | 17 |
| 6 | 14 |
| 12 | 81 |
| 24 | 28 |
| **total** | **142** |

Its homogeneous design again has rank 50, now with nullity 92. The runner
trains only within that nullspace on four small generic momenta and eight
coordinate-axis momenta, then validates without refitting on two
root-of-unity and four generic momenta. Training can be approximated while
preserving (5), but validation remains macroscopically nonzero. Refitting the
full 92-dimensional nullspace directly to validation also leaves a bounded
residual. The executed diagnostics are:

| diagnostic | value |
|---|---:|
| small/axis training relative residual | `3.915275e-05` |
| unregularized trained-vector held-out residual | `1.435578e3` |
| best held-out residual within the complete homogeneous nullspace | `0.386333` |
| homogeneous-plus-held-out design rank | `125` of `142` |

The very large unregularized validation value is disclosed as an overfit
diagnostic; the load-bearing nonmembership margin is the separately refitted
`0.386333`, not the coefficient blow-up.

This is a one-cell result. Inter-cell translations, oriented phase structure,
connected RN covariance, nonlinear source variables, mixed Schur sectors,
connection/tadpole terms, and a derived `R1` remain live.

## 4. Constructive Nonuniform Escape

For a complete closed line,

    F_L(theta)(exp(i theta)-1)=exp(i L theta)-1=0.           (12)

A transverse difference of two lines cancels the compact source. On `L=5`:

- the compact source is exactly zero;
- 100 momenta have nonzero source;
- 80 have nonzero tick frequency;
- every source annihilates the complete Regge null space; and
- every edge equation solves without projection.

The maximum gauge, complete-null, and solve residuals are respectively
`3.111e-15`, `2.214e-14`, and `3.093e-13`.

This does not select a signed neutral ensemble as physical matter. It proves
that the flat carrier, action-level Ward compatibility, nonuniform response,
and the retained `1/k^2` route coexist. The homogeneous mass-contact problem
is not equivalent to whether gravity can work.

## 5. Corrected Priority Graph

The new order is

    physical joint law
      -> ensemble and source typing
      -> massless versus curved/massive phase
      -> stationary background and full Ward generator
      -> contact/inter-cell coefficients if required
      -> continuous-zone and Lorentzian stability.           (13)

This burns down a false dependency. Selecting one of the 61 fitted vectors
before the first three nodes would overfit an optional target. Highest-value
next work is a selected ensemble/phase and full stationary Ward law, not
another homogeneous seagull tournament.

## 6. Exact Axiom Or Downstream-Law Consequence

The four current axioms explicitly leave source/action identification,
geometry dynamics, time evolution, and ensemble selection outside their
content. Nothing here contradicts them or proves a fifth ontology axiom
necessary.

The smallest sufficient interface presently visible is:

> **Compatible geometry-bearing joint Record/history family candidate
> (unadopted).** A covariant, projectively consistent, strictly positive joint
> family on Record histories has a distinguished null history and a covariant
> Record-to-geometry map. Its null-relative log density defines the total
> action. Local unit-oriented source changes are RN cocycles of that family.
> The law selects its compact, open, constrained, or background-subtracted
> ensemble and its massless, curved, or massive phase. On every selected
> stationary background, the full differentiated Ward identity includes
> geometry, connected, contact, mixed, source, multiplier, and generator
> connection/tadpole terms. The same family supplies an autonomous causal update
> compatible with permanent Records.

This content **can remain downstream** if derived. If foundation-level
autonomy is required first, it is the content needing approved registration
or amendment. It is sufficient, unadopted, and not proved minimal or
necessary.

No canonical axiom is edited here.

## 7. TOE Consequence

| lane | advance | remaining movement condition |
|---|---|---|
| gravity / source / resources | reclassifies the six compact targets, rejects two one-cell promotions on held-out Ward data, and preserves an exact nonuniform solve | select the ensemble/phase and full stationary joint Ward law |
| causal time | separates causal closure from Euclidean coefficient fitting | Lorentzian history/update and nonlinear stability |
| inertia / matter | prevents transverse curvature from being called physical graviton mass before phase selection | constituent-causal source typing and dressed inertia |
| operational quantum / Records | narrows the bridge to one compatible geometry-bearing family and map | derive/register the family and Record-to-geometry map |
| Born probability / realized history | preserves the joint-law route without selecting a member | functional/program selection and realized history |

Checkpoint-zero percentages remain fixed because the law and phase remain
unselected and independent audit is required.

## 8. Source And Residual Trace

| source | load-bearing use | boundary |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | exact exclusions of source/action and dynamics | no geometry law imported |
| [Block 19](ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | `M0`, constraints, stationary branches | ensemble remains supplied |
| [Block 22](ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | tangent kernels, gauge rows, massless target | phase remains supplied |
| [Block 28](ADMISSIBILITY_ENDOGENOUS_GEOMETRY_JOINT_RECORD_RN_LOCAL_COVARIANT_CONTACT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | metric orbits and homogeneous fit | fitted coefficients are not physical |
| [closed neutral history](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | action-level nonuniform escape | signed ensemble remains unselected |

The tested residual is `R0^dagger[D+C]R0`, not the complete nonlinear Ward
residual.

## 9. No-Go Discipline

N1--N8 status: `PASS` only for the exact domain theorem and the two declared
one-cell contact classes on the named inventories.

### N1 — materially distinct routes

| route | outcome |
|---|---|
| 61-orbit metric contact | homogeneous fit; rank-four Ward visibility and incompatible validation |
| 142-orbit edge contact | learns small/axis inventory; fails validation |
| global constrained phase | six compact directions are outside the domain |
| closed histories | complete `L=5` nonuniform inventory solves |
| inter-cell contact | live and excluded from both cell classes |
| connection/tadpole or mixed sector | live and omitted from (8) |
| refined/perfect action or curved phase | live and changes the law/phase |

### N2 — wall independence

Let `W1` be ensemble/phase selection, `W2` joint-family and geometry-map
selection, `W3` full Ward closure, `W4` nonuniform stationary existence, and
`W5` Lorentzian stability. No pair closes another: a joint family need not
select an infrared ensemble; an ensemble does not derive its contact; a
Euclidean Ward identity does not define a causal update.

### N3 — hidden-condition scan

The negative surface is limited to one fifteen-edge cell, simultaneous
four-axis permutations, real source-linear quadratics, three source rows, the
pure gauge-gauge condition without joint/connection terms, 12 training
momenta, six held-out momenta, and double-precision tangents. No
continuous-zone, arbitrary triangulation, diffeomorphism, infinite-volume, or
Lorentzian exhaustion is hidden.

### N4 — residual matching

The compact target is exactly the Block-23 tensor used by Block 28. The new
residual contracts the same tangent kernel with the exact lattice gauge rows.
The constructive escape solves the actual edge equation and complete null
space, not a continuum surrogate.

### N5 — rhetoric audit

| level | checked | not promoted |
|---|---|---|
| per element | all 825 metric and 1,800 edge monomials through complete orbits | no arbitrary functional |
| per site | one fifteen-edge cell | no inter-cell theorem |
| per mode | compact modes, named train/validation sets, all 625 `L=5` momenta | no continuous Brillouin result |
| per block | constraints, two contacts, Ward data, closed-history escape | no selected law |
| lattice-wide | one complete finite torus | no projective/infinite-volume theorem |

The eligible statement is that these one-cell classes do not promote the
homogeneous fit—not that gravity fails.

### N6 — partial-closure scan

Block 28 closes local contact existence. The closed-history parent closes one
nonuniform linear response. Block 19 closes stationary existence in one
ensemble. This result reorders them; it does not erase them.

### N7 — strongest steelman

Gauge-gauge failure of a direct quadratic says little about the complete
joint stationary identity. A source gradient, nonlinear transformation,
multiplier field, or dynamical source can supply the omitted
connection/tadpole term; an inter-cell contact adds Fourier structure; and a
curved phase need not cancel the compact coefficient. This objection is
accepted and defines the next target.

### N8 — cross-cycle echo

Earlier compact-source, fixed-normal, and support-confined walls were retired
by closed histories, full quotients, or geometry-spreading contacts. The
present boundary therefore ships only with its named class.

## 10. Reproduction

Run:

    python3 scripts/admissibility_global_constraint_phase_ward_contact_reclassification_2026_08_10.py

The runner checks the domain theorem, complete orbit counts, homogeneous
ranks/nullspaces, training-versus-held-out Ward systems, one complete finite
torus escape, axiom boundary, and N1--N8 source surfaces.
