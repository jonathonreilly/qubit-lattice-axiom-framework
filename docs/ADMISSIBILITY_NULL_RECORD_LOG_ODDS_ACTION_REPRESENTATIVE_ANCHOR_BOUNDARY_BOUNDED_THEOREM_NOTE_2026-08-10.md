---
claim_id: admissibility_null_record_log_odds_action_representative_anchor_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For any finite strictly positive geometry-indexed normalized configuration family with a distinguished null configuration, the unique dimensionless action representative whose null action vanishes at every geometry is the log-odds action A_x(g)=-log[pi_x(g)/pi_null(g)]. It is invariant under every configuration-independent geometry-dependent shift, reproduces the original normalized family exactly, fixes all relative geometry derivatives, and composes additively for factorized independent families. The retained finite coframe cut action already satisfies this anchor for both empty and full configurations at zero two-form source, so its declared representative is recovered exactly from normalized log odds. The source-dependent arbitrary common shifts constructed in Block 25 violate the null anchor unless their Hessian vanishes; they remain possible only as separately selected joint interactions. The current Record axiom supplies I(empty)=0 but does not identify readout with action, select a positive joint family, impose a null action anchor, fix an action unit, or select the separate pure-geometry action. This is a bounded representative-uniqueness theorem and exact amendment interface, not a derivation or adoption of physical source action, gravity dynamics, locality, projective consistency, continuous-momentum closure, or Lorentzian nonlinear stability."
upstream_dependencies:
  - minimal_axioms
  - admissibility_normalized_family_additive_zero_contact_nonidentifiability_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_bounded_theorem_note_2026-08-10
  - admissibility_code_swap_cut_area_local_source_improvement_metric_response_axiom_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_null_record_log_odds_action_representative_anchor_boundary_2026_08_10.py
---

# Null-Record Log-Odds Action Representative Anchor Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** constructive repair of the normalized-family additive-zero ambiguity
and exact source/action amendment interface.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_null_record_log_odds_action_representative_anchor_boundary_2026_08_10.py](../scripts/admissibility_null_record_log_odds_action_representative_anchor_boundary_2026_08_10.py)

**Repository-local dependencies:**
[canonical axiom boundary](MINIMAL_AXIOMS_2026-06-29.md),
[normalized-family additive-zero theorem](ADMISSIBILITY_NORMALIZED_FAMILY_ADDITIVE_ZERO_CONTACT_NONIDENTIFIABILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
[coframe cut action and Ward boundary](ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md), and
[cut-area source/improvement boundary](ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md).

## 1. Result Up Front

Block 25 proved that normalized probabilities alone leave an arbitrary common
geometry-dependent shift in their unnormalized actions. The ambiguity has a
minimal exact repair whenever the family contains a distinguished null
configuration.

Let `Omega` be finite, let `0 in Omega` be the null configuration, and suppose
that every geometry-indexed probability is strictly positive:

```text
pi_x(g)>0,                 sum_x pi_x(g)=1.                 (1)
```

Define the dimensionless null-anchored log-odds action

```text
A_x(g)=-log[pi_x(g)/pi_0(g)].                               (2)
```

Then

```text
A_0(g)=0,                                                     (3)

pi_x(g)=exp[-A_x(g)] / sum_y exp[-A_y(g)].                  (4)
```

Moreover, (2) is the unique representative of (1) satisfying (3). If
`S_x(g)` is any other representative and `S_x -> S_x+F(g)` is the Block-25
common-shift gauge, then

```text
A_x=S_x-S_0,                                                  (5)
```

so the common `F` cancels exactly. Any second anchored representative differs
by a common shift whose null value is zero, hence that shift vanishes.

This fixes the **matter/source representative** once a positive joint family
and its null configuration are physically registered. It does not select the
separate pure-geometry action, an action unit, or the joint family itself.

The retained finite coframe cut family already realizes the anchor. At zero
two-form source, both the empty and full binary configurations have no cut
faces, hence

```text
S_cut[empty;F]=S_cut[full;F]=0                              (6)
```

for every supplied positive coframe field `F`. Its declared action is
therefore recovered exactly from its normalized log odds. The geometry-
dependent common shifts used as algebraic completions in Block 25 are not
allowed matter-action equivalences after this anchor: a nonzero quadratic
shift gives the null configuration a nonzero geometry response.

The exact remaining issue is now narrower. The current Record axiom says that
the scalar readout obeys `I(empty)=0`; it does not identify readout with
dimensionless action, provide one finite positive joint family, or require the
matter action itself to obey (3). A source/action law must make that bridge.
No canonical axiom is edited here, and fixed TOE percentages do not move.

## 2. Null-Anchor Uniqueness Theorem

### Proposition 1 — representatives differ by one common function

Suppose two finite actions `S_x(g)` and `T_x(g)` yield the same strictly
positive normalized family:

```text
exp[-S_x]/Z_S = exp[-T_x]/Z_T.                              (7)
```

Taking ratios with the null configuration gives

```text
exp[-(S_x-S_0)] = pi_x/pi_0
                 = exp[-(T_x-T_0)].                        (8)
```

For real actions,

```text
T_x-S_x=T_0-S_0=:F(g)                                      (9)
```

for every `x`. Thus the only finite positive-family ambiguity is one
configuration-independent function of the supplied conditions.

### Proposition 2 — the null anchor fixes that function

The representative (2) has `A_0=0`. If `B` is a second representative with
`B_0=0`, Proposition 1 gives `B_x=A_x+F`, while the null row gives `F=0`.
Therefore `B=A` pointwise in geometry.

The theorem requires `pi_0>0`. If the null configuration is excluded from the
support, a different registered reference is required. The current finite cut
Gibbs family is strictly positive, so this wall is absent there.

## 3. Geometry Derivatives Become Identifiable

Differentiating (2) gives

```text
d A_x = -d log pi_x + d log pi_0,                           (10)

d^2 A_x = -d^2 log pi_x + d^2 log pi_0.                    (11)
```

Equations (10)--(11) are invariant under `S_x -> S_x+F(g)`. They determine
the geometry insertion and contact **relative to the null Record**. In terms
of any representative,

```text
d^n A_x=d^n S_x-d^n S_0.                                  (12)
```

This is the exact sense in which the anchor repairs Block 25. It does not make
the absolute log partition `log Z` into a gravity action. A separate
pure-geometry term `G[g]` cancels out of every normalized matter probability
and must be selected by an independent geometry law.

## 4. Composition Control

The anchor respects independent composition. If two positive families
factorize,

```text
pi_(x,y)=pi^A_x pi^B_y,                                    (13)
```

with null pair `(0_A,0_B)`, then

```text
A_(x,y)
  =-log[(pi^A_x pi^B_y)/(pi^A_0 pi^B_0)]
  =A^A_x+A^B_y.                                            (14)
```

Thus the null-anchored action is additive for genuinely independent families,
matching the direction of finite Record additivity without identifying the
Record readout with action by assumption.

Equation (14) is not projective consistency under arbitrary marginalization.
Integrating out interacting records generally produces an effective action
with new local and nonlocal terms. Infinite-volume and refinement consistency
remain separate obligations.

## 5. Exact Retained Cut-Family Realization

For the Block-11 coframe family,

```text
S_cut[X;F,B]
  =tau sum_(i,a) m_(i,a)[X] A_(i,a)[F] + <B,J[X]>.          (15)
```

For `X=empty` or `X=full`, every signed jump `j_(i,a)` and every cut indicator
vanishes. Hence (6) holds even for nonuniform positive coframes and for every
two-form source coupled through `J`. At `B=0`, code swap gives

```text
S_cut[X;F,0]=S_cut[complement X;F,0],                       (16)
```

and consequently `pi_empty=pi_full`. The empty and full anchors are compatible
on this family rather than competing conventions.

Because `S_empty=0`,

```text
-log[pi_X(F,B)/pi_empty(F,B)]
  =S_cut[X;F,B]-S_cut[empty;F,B]
  =S_cut[X;F,B].                                           (17)
```

Equation (17) recovers the complete declared representative, including its
first and second coframe derivatives. It does not physically select this cut
family; it proves that the proposed anchor works on a concrete retained local
model and does not destroy its code-swap or geometry response.

## 6. Consequence For The Block-25 Completion

Block 25 constructs, for each named source tangent, a common quadratic

```text
F_s(c,delta ell)=c delta ell^dagger D_s delta ell/2,

D_s=-U M_s U^dagger.                                      (18)
```

It leaves every normalized configuration probability fixed and cancels the
six-mode coefficient algebraically. Under the null anchor, however, it also
changes

```text
A_empty(c,delta ell): 0 -> F_s(c,delta ell).                (19)
```

The runner reconstructs all three nonzero `D_s`. Therefore none is an allowed
common matter-action equivalence under (3). This is a feature, not a new
obstruction: the anchor restores predictivity by refusing target-tailored
geometry shifts that normalized probabilities cannot see.

There are still two honest ways such a tensor could enter:

1. derive it as a genuine source-dependent joint interaction whose value and
   transformations are fixed before variation; or
2. derive it from a separate geometry action only if that action is permitted
   to depend on the registered source coordinate.

Either route is new physical law, not normalization convention. A pure-
geometry action required to be source independent cannot supply three
source-responsive matrices.

## 7. Exact Axiom/Law Update Interface

The current axioms provide all of the following useful ingredients:

- a state is a configuration of records;
- the scalar Record readout is finitely additive with `I(empty)=0`;
- a local probability distribution is determined by neighboring conditions;
  and
- choices not fixed by supplied structure remain conditional or open.

They do **not** provide:

- one positive global or projectively consistent joint Record family;
- the identification of dimensionless source action with normalized log odds;
- the null action condition `A_empty[g,J]=0` at every geometry/source value;
- a physical action unit;
- a typed split between matter/source action and pure geometry action; or
- the geometry update/field equation.

The narrowest sufficient repair exposed by this block is:

> **Null-Record source/action anchor candidate (unadopted).** Each registered
> positive joint Record family has a distinguished null configuration. Its
> dimensionless matter/source action is the unique log-odds representative
> `A[X;g,J]=-log(pi[X|g,J]/pi[empty|g,J])`, so
> `A[empty;g,J]=0` before geometry variation. Independent registered families
> compose additively. The physical action unit and a source-independent pure-
> geometry action or causal update are registered separately. A common shift
> depending on geometry, source, or history is an equivalent convention only
> if it preserves this anchor and the complete geometry response; otherwise it
> is a new joint interaction requiring its own derivation and transformation
> law.

This clause could be a downstream source/action bridge or an owner-approved
amendment. It is sufficient for the representative ambiguity and compatible
with the retained cut family. It is unadopted and not proved minimal or
necessary for every possible formulation.

It still does not choose the cut family, `G[g]`, an action unit, a coupling
sign, a massless versus curved phase, or a Lorentzian update. Those are not
hidden inside the anchor.

## 8. TOE Consequence

| lane | exact progress | remaining condition for movement |
|---|---|---|
| gravity / source / resources | gives a unique dimensionless matter/source representative once a positive joint family and null Record are registered; removes arbitrary common contact tuning | select the joint family, pure-geometry action/update, unit, coupling, nonuniform Ward tensor, and stable phase |
| operational quantum / records | uses the already named empty Record readout as the exact reference shape without equating it to action silently | approve or derive the source/action log-odds bridge and joint family |
| inertia / matter | makes source-relative geometry Hessians predictive instead of gauge-arbitrary | derive the physical source carrier and complete connected/contact response |
| causal time | separates a static action anchor from a causal geometry update | Lorentzian update/history and nonlinear stability |
| Born / realized history | consumes a supplied positive normalized family but no probability-value or realization selector | physical family/program selection and realized-history law |

Fixed campaign percentages remain unchanged because the candidate bridge is
not adopted and the physical geometry law is still open.

## 9. N1--N8 Discipline

The bounded negative is only that the present axiom memo does not identify
`I(empty)=0` with a null matter-action anchor. No gravity or axiom-necessity
claim is made.

### N1 — alternative routes

| route | result |
|---|---|
| null log-odds anchor | exact uniqueness and derivative recovery |
| full-state co-anchor | compatible when code swap gives `pi_full=pi_empty`; realized by the cut family |
| arbitrary common shift | removed as an equivalence by the null anchor |
| allowed local counterterm class | live if every allowed term preserves anchor and complete response |
| separately selected joint interaction | live; must be derived rather than called normalization |
| pure-geometry action | live and still invisible to normalized matter probabilities |
| different registered reference | live when the null state has zero probability |
| causal update instead of Euclidean action | live; requires its own source/geometry law |

### N2 — independent walls

Representative uniqueness, positive joint-family existence, action unit,
source/geometry split, locality, projective consistency, and Lorentzian
stability are independent. Proposition 2 closes only the first after its
explicit premises are supplied.

### N3 — hidden-wall scan

The theorem assumes a finite strictly positive family and a distinguished
null state. The cut realization assumes its declared coframe action. Neither
assumption is promoted to a universal physical family or current axiom.

### N4 — residual matching

The repair targets exactly Block 25's common `F(g)` ambiguity. It does not
replace the missing geometry action with a normalization choice. The residual
is the selected joint source/geometry law and its full stationary response.

### N5 — resolution and rhetoric

The runner emits five substantive `N5_CERTIFICATE` lines: exact uniqueness,
retained cut realization, exclusion of arbitrary common completion, live
joint/geometry routes, and the current-axiom boundary.

### N6 — partial closure

Equations (2)--(14) are exact for every finite positive family. Equations
(15)--(17) are exact on the declared cut family. No statement is made for a
zero-probability null state, interacting marginal projective limit, or
continuous field measure.

### N7 — strongest steelman

One may treat physical actions as equivalence classes under counterterms.
Accepted: the candidate permits such an equivalence only after proving that
the anchor and complete geometry response are preserved. Otherwise the term
is observable to dynamical geometry and is a new interaction.

### N8 — cross-cycle echo

Block 11 already declared an explicit representative but could not license
it physically. Block 25 showed why a normalized law is insufficient. The
present anchor does not erase either lesson: it gives a minimal exact way to
license the representative while leaving family selection and dynamics open.

**N1--N8 status: `PASS` only** for the finite positive null-anchor uniqueness
theorem and the declared cut-family realization.

## 10. Verification And Next Work

The runner checks:

1. the exact common-shift invariance and log-odds reconstruction;
2. uniqueness under the null action condition;
3. first and second geometry-derivative invariance;
4. additivity for factorized independent families;
5. empty/full anchoring and complement symmetry on a nonuniform exact coframe
   cut fixture;
6. geometry-path persistence of the anchor;
7. nonzero Block-25 completion tensors and their exclusion as anchored matter-
   action equivalences; and
8. current-axiom, source/action, pure-geometry, and bounded-scope wording.

Expected final line:

```text
TOTAL: PASS=14 FAIL=0
```

The next physics calculation is no longer allowed to tune a common `F_s`.
Choose or derive the anchored local joint family, compute its complete
connected, contact, mixed/source, multiplier, and generator-connection tensor
on a fully stationary nonuniform background, and compare that tensor with the
Block-23 coefficient across continuous momentum. Separately derive the pure-
geometry action or causal update and test Lorentzian nonlinear stability.

No canonical axiom is edited. No audit verdict or fixed-percentage movement is
authored here.
