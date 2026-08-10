---
claim_id: admissibility_null_record_rn_cocycle_source_unit_gravity_contact_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For finite strictly positive Record laws with a distinguished null configuration, a positive Radon-Nikodym source intervention changes the unique null-anchored matter action by the negative logarithm of the RN density relative to its null value. The normalizing partition factor cancels, sequential interventions obey an exact additive cocycle, exponential tilts give the relative source observable, and a unit-Fisher convention fixes the positive dimensionless source scale while leaving orientation and the dimensionful action quantum open. The retained two-form cut source realizes the RN cocycle on all 256 configurations but is coframe independent and therefore supplies no metric contact tensor. Configuration-dependent null-anchored interactions can algebraically realize the Block-23 completions, so there is no gravity no-go; locality, covariance, physical selection, the joint-family law, pure geometry, and Lorentzian dynamics remain open."
upstream_dependencies:
  - minimal_axioms
  - admissibility_null_record_log_odds_action_representative_anchor_boundary_bounded_theorem_note_2026-08-10
  - admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_bounded_theorem_note_2026-08-10
  - source_measure_pcal_rn_cocycle_theorem_note_2026-05-30
  - source_measure_log_selection_boundary_theorem_note_2026-05-30
runner: scripts/admissibility_null_record_rn_cocycle_source_unit_gravity_contact_boundary_2026_08_10.py
---

# Null-Record RN-Cocycle Source Unit And Gravity-Contact Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** constructive source/action bridge after the null-Record anchor, plus
an exact diagnosis of why the retained topological source alone cannot supply
the missing metric contact.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_null_record_rn_cocycle_source_unit_gravity_contact_boundary_2026_08_10.py](../scripts/admissibility_null_record_rn_cocycle_source_unit_gravity_contact_boundary_2026_08_10.py)

**Repository-local dependencies:**
[current axiom boundary](MINIMAL_AXIOMS_2026-06-29.md),
[null-Record action anchor](ADMISSIBILITY_NULL_RECORD_LOG_ODDS_ACTION_REPRESENTATIVE_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
[finite conditional compatibility](ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
[earlier RN-cocycle support](SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md), and
[the RN source-scale boundary](SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md).
The older RN notes are prior conditional routes, not premise authority; all
load-bearing finite algebra is rederived here against the current axioms.

## 1. Result Up Front

Block 26 fixed the action representative after a positive joint family is
registered. This block proves that physical source interventions have a
natural exact composition with that repair.

Let `Omega` be finite, let `0 in Omega` be the distinguished null Record, and
let `P` and `Q` be strictly positive normalized laws. Define

```text
R_QP(x)=Q(x)/P(x),                 E_P R_QP=1.             (1)
```

The null-anchored actions are

```text
A_P(x)=-log[P(x)/P(0)],
A_Q(x)=-log[Q(x)/Q(0)].                                  (2)
```

Then the source-induced action increment is exactly

```text
Delta A_QP(x)=A_Q(x)-A_P(x)
             =-log[R_QP(x)/R_QP(0)].                     (3)
```

Thus the RN density's common normalizer cancels before geometry variation.
If `P -> Q -> T` are sequential interventions, the RN chain rule gives

```text
R_TP=R_TQ R_QP,
Delta A_TP=Delta A_TQ+Delta A_QP.                         (4)
```

This is the exact null-relative source/action cocycle. It supplies a coherent
downstream bridge without silently equating the scalar Record readout with an
action.

For an exponential source tilt

```text
Q_h(x)=P(x) exp[h O(x)] / E_P exp[h O],                   (5)
```

equation (3) becomes

```text
Delta A_h(x)=-h[O(x)-O(0)].                              (6)
```

The log-partition normalizer disappears, but every configuration-relative
source insertion remains. Consequently:

- a common geometry function cannot tune gravity after the anchor;
- a genuine geometry-dependent source observable can contribute a physical
  relative contact tensor; and
- the source law, rather than normalization, must select that observable.

The retained cut two-form source realizes (3) on all 256 configurations of
the exact `L=2` fixture. Its source term has no coframe argument, however, so
its metric first and second variations vanish identically. That source can
carry an exact higher-form Ward identity but cannot by itself cancel the
Block-23 metric contact defect.

This is not a gravity obstruction. Multiplying each Block-25 completion by a
configuration scalar `q(X)` with `q(empty)=0` produces an anchored joint
interaction whose singleton Hessian cancels the corresponding Block-23
matrix. The runner constructs all three below `2.037e-15`. The construction is
target-tailored and nonlocal in geometry; it is an algebraic escape, not the
physical law.

## 2. Exact RN Anchor Theorem

### Proposition 1 — RN normalization and null-relative action

Strict positivity makes `R_QP` well defined. Normalization gives

```text
sum_x P(x)R_QP(x)=sum_x Q(x)=1.                           (7)
```

Taking the ratio of (1) at `x` and at the null configuration gives

```text
R_QP(x)/R_QP(0)
  =[Q(x)/Q(0)]/[P(x)/P(0)].                              (8)
```

Taking the negative logarithm proves (3). In particular,
`Delta A_QP(0)=0`; the intervention preserves the null action anchor.

### Proposition 2 — sequential interventions form a cocycle

For a third positive law `T`,

```text
dT/dP=(dT/dQ)(dQ/dP)                                    (9)
```

pointwise. Dividing (9) by its null value and taking `-log` gives (4).
The composition is exact and does not require infinitesimal sources,
Gaussianity, a continuum limit, or an imported field theory.

### Proposition 3 — independent products

For independent positive laws `P_A P_B` and `Q_A Q_B`, the RN density and
null ratio factorize. Therefore

```text
Delta A_AB(x_A,x_B)
 =Delta A_A(x_A)+Delta A_B(x_B).                         (10)
```

This agrees with Block 26's action additivity and identifies the source-side
composition law that realizes it.

## 3. Exponential Tilts And Geometry Response

Equation (5) has RN density

```text
R_h(x)=exp[hO(x)]/Z_O(h),
Z_O(h)=E_P exp[hO].                                      (11)
```

Its null ratio is

```text
R_h(x)/R_h(0)=exp{h[O(x)-O(0)]},                         (12)
```

which proves (6). If the observable depends on supplied geometry `g`, then

```text
partial_a Delta A_h(x)
  =-h partial_a[O(x;g)-O(0;g)],

partial_a partial_b Delta A_h(x)
  =-h partial_a partial_b[O(x;g)-O(0;g)].                (13)
```

The source contact is therefore identifiable relative to the null Record.
It vanishes for a configuration-independent `O`, exactly reproducing the
Block-25/26 common-shift diagnosis. It can be nonzero only when the source
couples differently to different configurations.

A separate source-independent geometry action `G[g]` cancels from (8)--(13)
and remains invisible to normalized matter/source probabilities. The RN
bridge cannot replace that law.

## 4. Source Scale, Fisher Unit, And Action Quantum

On a reference law `P`, the origin score of (5) is

```text
s(x)=O(x)-E_P O,                                         (14)
```

and its Fisher norm is `Var_P(O)`. Replacing `O` by `lambda O` gives

```text
I_lambda=lambda^2 Var_P(O).                              (15)
```

For a declared unit-variance observable and positive source orientation, the
unit-Fisher condition selects `lambda=1`. If signed orientations are allowed,
Fisher norm alone leaves `lambda=+/-1`; the coupling orientation remains a
separate physical choice.

Let `kappa` be a physical action quantum and suppose the selected source law
is

```text
S_h=S_0-kappa h O.                                       (16)
```

Then `exp[-S_h/kappa]/exp[-S_0/kappa]=exp[hO]`, so (6)
follows. This is an exact action-to-RN bridge once (16) and `kappa` are
registered. It does not derive the dimensionful value of `kappa`; the approved
length/Planck scale alone does not fix an action normalization.

The source-unit problem therefore has two legitimate downstream repairs:

1. register a primitive Fisher coordinate plus its orientation; or
2. register an action quantum and identify physical interventions by (16).

Neither is currently part of the four minimal axioms.

## 5. Retained Cut-Source Test

Write the retained action as

```text
S_B[X;F]=S_cut[X;F]+S_2form[X;B].                         (17)
```

At fixed coframe `F`, the normalized law is proportional to `exp(-S_B)`.
Relative to the `B=0` family, its RN density contains a common partition
ratio, but (3) gives

```text
Delta A_B[X]
 =S_2form[X;B]-S_2form[empty;B]
 =S_2form[X;B].                                          (18)
```

The last equality uses the exact empty anchor. The runner checks (18) for all
256 configurations, both source orientations under complement, and three
nontrivial exact coframe values.

The same calculation exposes the limitation. `S_2form[X;B]` depends on the
oriented interface and supplied two-form but not on `F`. Hence

```text
partial_F Delta A_B=0,
partial_F^2 Delta A_B=0.                                 (19)
```

The retained topological source is a valid RN intervention and higher-form
source, but its own metric contact tensor is exactly zero. Connected response
through `S_cut` and a separately geometry-coupled source remain live.

## 6. Constructive Anchored Contact Escape

Let `D_s` be one of the three Block-25 fifteen-edge completion Hessians and
let

```text
q(X)=number of occupied Records in X.                    (20)
```

The joint interaction

```text
J_s[X;delta ell]
 =q(X) (1/2) delta ell^T D_s delta ell                  (21)
```

obeys `J_s[empty]=0`. On any singleton configuration its geometry Hessian is
`D_s`, so its six-mode projection cancels the corresponding Block-23 source
matrix. Unlike a common `F_s`, (21) changes probability ratios and is visible
as a genuine interaction. The count factor is invariant under proper cubic
permutations and additive over disjoint sites.

This is only an existence control. The matrices are reconstructed from the
target, act on the complete edge chart, and are not derived as local cell
terms. Equation (21) proves that the null anchor does not make contact repair
algebraically impossible; it does not prove locality, covariance under
geometry changes, gluing, source transformation, or physical selection.

## 7. Minimal Axiom Or Downstream-Law Delta

The RN composition shrinks the required update. The framework does not need
to declare a target contact tensor or a target-tailored common shift. The
narrow sufficient interface is instead:

> **Registered joint-family/RN source bridge candidate (unadopted).** The
> finite-region Record laws form one compatible strictly positive joint
> family with a distinguished null configuration. A physical source
> intervention is a positive Radon-Nikodym cocycle on that family. Its
> dimensionless matter-action increment is the null-relative log density
> `Delta A_J[X;g]=-log[(dP_J/dP_0)(X)/(dP_J/dP_0)(empty)]`. Sequential
> interventions compose by the RN chain rule and independent families add.
> Source coordinates carry a registered unit and orientation, fixed either by
> a primitive Fisher metric or by a physical action quantum. A separate
> source-independent pure-geometry action or causal update supplies geometry
> dynamics. Geometry-dependent source observables are new joint interactions
> and must satisfy the registered locality, covariance, gluing, and source-
> transformation law.

This can be a downstream bridge rather than a fifth foundational axiom. What
must be added to the current four-axiom surface, if no downstream derivation is
found, is only the joint-family compatibility/registration and intervention
typing. The pure-geometry law is independently unavoidable because it is
invisible to every probability ratio.

No canonical axiom is edited here. The candidate is sufficient on the finite
positive surface, unadopted, and not proved minimal across zero-support or
non-measure formulations.

## 8. TOE Consequence

| lane | exact progress | remaining condition for movement |
|---|---|---|
| gravity / source / resources | source action increments now have an exact null-relative RN composition law; arbitrary common contact tuning is excluded; anchored contact repair remains algebraically possible | derive the physical geometry-dependent RN score/local joint interaction and the separate geometry law |
| operational quantum / records | identifies the exact finite joint-law/intervention interface missing between local Admissibility and Record action | derive or approve compatible joint families and physical intervention typing |
| inertia / matter | unit Fisher norm can fix the positive dimensionless source scale | source orientation, action quantum, physical carrier, and stress response |
| causal time | sequential RN interventions have a cocycle but no time ordering or causal update is inferred | derive the Lorentzian update and realized history |
| Born / realized history | consumes positive laws and interventions without selecting their physical values or occurrences | physical family/program/occurrence selector |

Fixed campaign percentages remain unchanged because the candidate is not
adopted and the pure-geometry/dynamics law remains open.

## 9. N1--N8 Discipline

The bounded negative is only that the retained coframe-independent two-form
source has zero metric contact. No source, gravity, or axiom no-go is claimed.

### N1 — alternative routes

| route | result |
|---|---|
| geometry-dependent RN score | exact nonzero relative Hessian is possible by (13) |
| anchored count-weighted interaction | explicit full-tensor algebraic completion by (21) |
| proper-length source contact | live complementary source-coordinate route |
| hyperface seagull and connected covariance | live tensor components |
| generator/constraint connection | live differentiated-Ward route |
| pure-geometry action or causal update | separately required and unrestricted by the theorem |
| zero-support or alternate reference sector | outside the positive-family theorem |

### N2 — independent walls

Joint-family compatibility, source-intervention typing, dimensionless source
unit/orientation, local geometry dependence, pure geometry, projective
consistency, and Lorentzian dynamics are independent. The RN identity closes
only composition after the family and intervention are supplied.

### N3 — hidden-wall scan

Strict positivity, finite support, a distinguished null state, RN absolute
continuity, and the retained finite cut fixture are explicit. The old RN notes
are context, not hidden premise authority.

### N4 — residual matching

Block 26 left joint-family selection and source/action typing open. Equations
(1)--(16) target exactly that seam. Equation (19) then identifies the residual
metric contact of the retained topological source without changing the target.

### N5 — resolution and rhetoric

The runner emits five substantive `N5_CERTIFICATE` lines: RN repair, source
unit, retained zero-contact boundary, constructive anchored escape, and the
remaining axiom/geometry split.

### N6 — partial closure

The RN cocycle theorem is exact for every finite positive pair. The cut test is
exhaustive only on the declared 256-configuration fixture. No continuous-
measure, projective-limit, nonuniform Regge, or Lorentzian theorem is claimed.

### N7 — strongest steelman

A hostile reviewer may propose a local geometry-dependent source observable.
Accepted: equation (13) is precisely that live route, and equation (21) proves
algebraic sufficiency. The present negative cannot exclude it.

### N8 — cross-cycle echo

The earlier RN source-scale notes already separated normalized interventions
from physical source units. Block 25 separated normalized probabilities from
absolute geometry contact. The null-relative RN bridge composes both lessons
without claiming either missing selection law has been derived.

**N1--N8 status: `PASS` only** for the finite RN composition theorem and the
retained coframe-independent two-form zero-contact boundary.

## 10. Verification And Next Work

The runner checks exact finite RN normalization, null-relative action identity,
sequential cocycle composition, exponential-tilt normalizer cancellation,
geometry derivatives, Fisher scaling/orientation, the action-quantum bridge,
all 256 retained cut configurations, coframe-independent zero contact, cubic
count anchoring, and all three full-tensor algebraic escapes.

Expected final line:

```text
TOTAL: PASS=17 FAIL=0
```

The next decisive physics calculation must replace (21) by a local covariant
geometry-dependent source score derived from one registered joint action,
then compute its complete connected/contact/mixed/multiplier/generator tensor
on a stationary nonuniform background. In parallel, the source-independent
geometry action or causal update must be selected and tested for Lorentzian
nonlinear stability.

No canonical axiom, audit verdict, or fixed-percentage movement is authored
here.
