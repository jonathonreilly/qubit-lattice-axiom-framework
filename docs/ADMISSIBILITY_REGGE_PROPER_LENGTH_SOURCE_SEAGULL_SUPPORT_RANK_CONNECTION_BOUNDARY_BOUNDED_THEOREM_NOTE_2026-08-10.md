---
claim_id: admissibility_regge_proper_length_source_seagull_support_rank_connection_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the three retained compact Regge source rows and the six homogeneous flat physical metric modes reconstructed in Block 23, the direct proper-length source contact obtained from U_s(g)=-c sum_e J_s,e sqrt(v_e^T g v_e) has ranks 2, 3, and 4, equal to the ranks of the active source-edge restrictions. Each Block-23 O(source) coefficient has rank six, so neither this contact nor any direct Hessian confined to the same 2-, 3-, or 4-edge coordinate support can cancel the coefficient: rank(M_s+D_s) is at least 4, 3, or 2. Moreover, if U_s=-c J_s dot ell is merely rewritten through nonlinear metric or coframe coordinates ell=ell(y), then at a fully stationary point its apparent proper-length seagull cancels the geometry connection term exactly and the total pullback Hessian is L^dagger H_g L; adding the source seagull alone would double count a coordinate term. A common six-edge chart algebraically admits source-responsive cancellation, preserving geometry-spreading contacts, dynamical source variables, nonuniform closed histories, richer local actions, and curved or massive phases. This is a support-confined contact and coordinate-rewrite boundary, not a gravity no-go, local-action selection, full-stationarity theorem for the reacted homogeneous sources, nonuniform or continuous-momentum theorem, Lorentzian stability theorem, axiom necessity result, or axiom adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_sourced_regge_joint_ward_schur_completion_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_bounded_theorem_note_2026-08-10
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_regge_proper_length_source_seagull_support_rank_connection_boundary_2026_08_10.py
---

# Regge Proper-Length Source Seagull: Support-Rank And Connection Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** direct-Ward/seagull transfer test and local-action requirement
**Scope:** the three retained homogeneous compact source rows and the six
flat physical metric modes reconstructed by Block 23.
**Audit-status authority:** independent audit lane only. This source authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_regge_proper_length_source_seagull_support_rank_connection_boundary_2026_08_10.py](../scripts/admissibility_regge_proper_length_source_seagull_support_rank_connection_boundary_2026_08_10.py)

## Result Up Front

Block 23 left a direct Ward/contact term as the highest-priority alternative
to its coefficient-level Schur completion. The retained cut-coframe family
shows that a same-family seagull can exist. That fact cannot simply be copied
onto the Regge source. This block performs the transfer calculation.

Let the fifteen actual edge classes be represented by nonzero binary vectors
`v_e in {0,1}^4`, with flat length `ell_e=|v_e|`. The retained sourced normal
equation uses the affine edge-length action

    U_s(ell)=-c sum_e J_(s,e) ell_e,                         (1)

so the total stationary equation has `grad S_g=c J_s`. If the same source is
written through a homogeneous metric `g=I+h`, then

    ell_e(h)=sqrt(v_e^T (I+h) v_e),                         (2)

    r_e=d ell_e|_0,

    d^2 ell_e|_0=-(r_e tensor r_e)/ell_e.                  (3)

Consequently the apparent source contact is

    C_s=d^2 U_s/dh^2|_0
       =c sum_(e in E_s) (J_(s,e)/ell_e)
          r_e tensor r_e.                                  (4)

The six Block-23 physical modes lie in the ten-dimensional affine metric
tangent to residual `3.91e-15`. Restricting (4) to those modes gives ranks

| source row | active edge classes `m_s` | `rank C_s` | `rank M_s` |
|---|---:|---:|---:|
| two-stream | 2 | 2 | 6 |
| Bundle A | 3 | 3 | 6 |
| Bundle B | 4 | 4 | 6 |

This is not merely a failure of the proper-length coefficient. Any direct
contact whose edge-coordinate Hessian is confined to the same active
`m_s`-edge coordinate subspace has rank at most `m_s`. Sylvester's rank
inequality therefore gives, for every such contact `D_s`,

    rank C_s <= m_s < 6,                                    (5a)

    rank(M_s+D_s) >= rank(M_s)-rank(D_s)
                    >= 6-m_s
                    =4,3,2.                                (5)

Equivalently, for a scalar rescaling of (4),

    rank(M_s + alpha C_s) >= 6 - m_s > 0                   (6)

for every real or complex `alpha`. A support-confined direct contact cannot
cancel the six-mode coefficient. With the sign fixed by (1), the contacted
inertias are `3-/3+`, `3-/3+`, and `2-/4+`; all remain nonsingular. Even the
Frobenius-best scalar multiples leave relative residuals

    0.971376, 0.934283, 0.648075.                           (7)

There is a second, independent boundary. Suppose (1) is not changed but is
only rewritten through nonlinear coordinates `ell=ell(y)`. Let `L=d ell/dy`
and `K_a=d^2 ell_a/dy^2`. At a fully stationary point of
`S_tot=S_g+U_s`, write `g_a=partial_a S_g` and
`u_a=partial_a U_s=-cJ_a`. Then `g_a + u_a=0`, and

    d_y^2 S_tot
      =L^dagger (H_g+H_U) L + sum_a (g_a+u_a) K_a
      =L^dagger H_g L.                                     (8)

Here `H_U=0` in independent edge-length coordinates. Split apart, the
geometry connection is `-C_s` and the source proper-length seagull is `+C_s`.
They cancel exactly. A coordinate rewrite is not a new action; adding only
`+C_s` to the edge-coordinate Hessian double counts one side of (8).

Equations (5) and (8) close two tempting shortcuts. They do **not** close the
gravity route. The runner finds one well-conditioned common six-edge chart
of the physical carrier. An arbitrary source-responsive Hermitian contact on
that chart cancels every `M_s` to below `7e-16`. This is an algebraic control,
not a selected law, but it proves that geometry-spreading contact terms can
escape (5). Dynamical source variables can likewise realize Block 23's
`p=q=1` mixed/source-block scaling. Nonuniform closed histories, richer
actions, and a curved or massive interpretation remain open.

The exact update is therefore:

1. do not borrow the cut-coframe seagull as an extra Regge term;
2. do not count a nonlinear coordinate rewrite as a physical completion;
3. require a derived local source action that spreads one source insertion
   over at least six independent physical geometry combinations, or a derived
   dynamical source/constraint sector with its complete mixed Hessian; and
4. test that action on a fully stationary nonuniform Ward-compatible source,
   rather than on the ten-reaction homogeneous surrogate alone.

No canonical axiom is edited. The fixed TOE percentages do not move.

## Machine Status And Trace

~~~yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The proper-length first and second variations, source-support ranks, Sylvester residual-rank bounds, stationary pullback cancellation, and six-edge algebraic escape are finite-dimensional derivations. The three mass coefficients are source-bound double-precision reconstructions. Physical source/action selection, full stationarity, nonuniform closure, and Lorentzian dynamics remain open."
trace_class: upstream_support
target_claim_id: admissibility_regge_local_joint_source_action_first_order_ward_completion
target_blocker_text: "derive a local joint Regge/source action whose direct contact or dynamical Schur term spans the six physical first-order source coefficient, solve a fully stationary nonuniform Ward-compatible background, and test its continuous-momentum and Lorentzian nonlinear quotient"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "construct the nonuniform closed-history or geometry-spreading source action and compute its full direct, mixed, source, multiplier, and connection Hessian blocks"
conditional_surface_status: "the retained proper-length source seagull has support rank 2/3/4 and cannot cancel the full-rank six-mode coefficients; as a coordinate-only rewrite it cancels the geometry connection at full stationarity; a six-edge spreading or dynamical joint action remains algebraically possible"
hypothetical_axiom_status: "if no downstream derivation selects such an action, a sufficient geometry-history amendment must type the local source carrier, its support spreading or dynamical variables, transformation law, action unit, full stationarity, and selected massless versus curved phase; this is unadopted and not proven minimal or necessary"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## Exact Target Contract

| Contract field | Block-24 value |
|---|---|
| target statement | test whether the direct proper-length Regge source seagull, or any direct contact confined to the same active source-edge coordinates, can cancel the Block-23 six-mode first-order coefficient |
| quantifiers/domain | all contacts supported on each declared source row's active `m_s` edge coordinates; the specific proper-length metric pullback; the three retained source tangents |
| allowed premises | Block-23 physical carrier and mass coefficients, the exact actual-edge metric map, elementary proper-length calculus, finite-dimensional rank inequalities, and explicitly supplied source rows |
| forbidden weakenings | calling a coordinate connection a new interaction, assuming the cut-coframe contact transfers, treating partial stationarity as full stationarity, or promoting a support-rank boundary to a gravity no-go |
| required controls | all fifteen edge directions, all three source supports, both representations of the contact, sign-fixed and best-scaled contacts, exact connection cancellation, and one support-spreading escape |
| completion witness | formulas (3)--(8), runner-reconstructed ranks/inertias/residuals, and a common six-edge chart |
| outcomes not counting as closure | an arbitrary `-M_s` counterterm, source-blind projection, a coordinate rewrite, an unselected auxiliary factorization, or candidate axiom wording |

## 1. Source-Bound Inputs

The load-bearing inputs are repository-local:

1. the [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), used only to
   bind the source/action-selection boundary;
2. [Block 23](ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
   supplies the reconstructed physical basis, the three full-rank `M_s`, and
   the `p=q=1` versus direct-contact decision;
3. the actual-edge source rows and affine metric map are reconstructed through
   Block 23's retained Regge dependencies;
4. the [closed-line history](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
   supplies the concrete proper-length actual-edge action and its exact flat
   telescoping Ward identity; and
5. the [cut-coframe family](ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
   supplies only the steelman that a derived same-family contact can exist.

No observed constant, fitted gravitational coefficient, continuum Einstein
equation, external theorem, audit verdict, or proposed axiom is used as a
scientific premise.

The source rows are the exact fifteen-component columns:

- two-stream: coefficient `2` on `v=(0,0,0,1)` and `(1,0,0,1)`;
- Bundle A: coefficient `2 sqrt(2)` on the three tick-space face diagonals
  with spatial Hamming weight one; and
- Bundle B: coefficient `3` on the tick edge and `sqrt(3)` on the three
  tick-space directions with spatial Hamming weight two.

Their support counts are therefore exactly `2,3,4`. Those counts are
conditions of the bounded theorem, not universal matter-source counts.

## 2. The Six Physical Modes Are Affine-Metric Modes

Let `M_0` be the exact `15 x 10` line-averaged edge-to-metric map. Its row for
edge direction `v` is the first derivative of (2):

    (M_0)_(e,aa)=v_a^2/(2|v|),

    (M_0)_(e,ab)=v_a v_b/|v|,  a<b.                         (9)

Let `P` be Block 23's orthonormal `15 x 6` physical zero-mode frame, formed by
removing the four leading vertex-displacement directions from the ten affine
metric modes. The runner constructs

    H=M_0^+ P                                                    (10)

and obtains

    ||M_0 H-P||_2=3.90e-15,

    ||H^dagger M_0^T M_0 H-I_6||_2<1e-14.                    (11)

Thus the support-rank comparison is made on exactly the same six-dimensional
carrier as `M_s`, not on a surrogate scalar or unrelated coframe space.

## 3. Proper-Length Contact

For symmetric metric coordinate `h_A`, define

    q_e(h)=v_e^T(I+h)v_e,
    ell_e(h)=sqrt(q_e(h)).                                   (12)

Because `q_e` is affine,

    partial_A ell_e=(partial_A q_e)/(2 ell_e)=r_(e,A),

    partial_A partial_B ell_e
      =-(partial_A q_e)(partial_B q_e)/(4 ell_e^3)
      =-r_(e,A)r_(e,B)/ell_e.                               (13)

The runner verifies (13) for all fifteen actual edge classes by independent
centered first and mixed-second differences. The maximum errors are below
`2e-9` and `2e-7`, respectively.

For the sign convention in (1),

    d_h^2 U_s
      =c sum_e (J_(s,e)/ell_e) r_e r_e^T.                   (14)

Restricting with the metric lift `H`, or equivalently using the source-edge
rows of `P=M_0H`, gives

    C_s
      =H^dagger d_h^2 U_s H
      =P_(E_s)^dagger diag(J_(s,e)/ell_e) P_(E_s).          (15)

The two evaluations agree below `1e-14`. Since every active weight is
positive, the diagonal matrix in (15) is positive definite on its support.
The support row ranks are `2,3,4`, so `rank C_s=2,3,4` exactly on the numerical
carrier with large singular margins.

The sign-fixed sums `M_s+C_s` have:

| source | inertia of `M_s+C_s` | smallest absolute eigenvalue |
|---|---:|---:|
| two-stream | `3-/3+` | `0.000884...` |
| Bundle A | `3-/3+` | `0.087227...` |
| Bundle B | `2-/4+` | `0.094657...` |

The contact changes the spectra substantially but does not create a massless
six-mode coefficient.

## 4. Support-Rank Theorem

### Proposition 1 — active-coordinate rank bound

Let `E` select `m` independent edge coordinates from the fifteen-dimensional
edge space. Any twice differentiable source action whose geometry dependence
at the expansion point is confined to those coordinates has edge Hessian

    D=E W E^dagger                                           (16)

for some Hermitian `m x m` matrix `W`. For any six-mode frame `P`,

    P^dagger D P=(E^dagger P)^dagger W(E^dagger P),          (17)

so

    rank(P^dagger D P) <= m.                                 (18)

This includes arbitrary cross terms among the active coordinates; it is not
restricted to the separable proper-length form (14).

**Proof.** Equation (16) follows from coordinate support. Equation (17) is
associativity. The rank of a product cannot exceed the inner dimension `m`.
`square`

### Corollary 1 — no support-confined cancellation

For invertible `6 x 6` matrix `M`, Sylvester's inequality gives

    rank(M+D) >= rank(M)-rank(D) >= 6-m.                     (19)

The declared supports have `m=2,3,4`, hence every support-confined direct
contact leaves rank at least `4,3,2`. In particular, (6) holds for every
scalar `alpha`, and no tuning of the proper-length coefficient changes the
conclusion.

This corollary says nothing about a contact that spreads one source insertion
into other local geometry variables, a mixed/source Schur term, or a phase in
which `M_s` need not vanish.

## 5. Best Scalar Control

For completeness, minimize

    ||M_s+alpha C_s||_F                                      (20)

over real `alpha`. The exact least-squares coefficient is

    alpha_*=-Re Tr(C_s^dagger M_s)/Tr(C_s^dagger C_s).       (21)

The runner finds:

| source | `alpha_*` | `||M+alpha_* C||_F/||M||_F` |
|---|---:|---:|
| two-stream | `-0.038712...` | `0.971376...` |
| Bundle A | `-0.310173...` | `0.934283...` |
| Bundle B | `-0.286843...` | `0.648075...` |

Negative fitted signs are already different from the sign in the actual
proper-length source action. More importantly, the residual-rank theorem does
not depend on their values or signs. These decimals are sensitivity controls,
not fitted physical parameters.

## 6. Stationary Pullback Cancellation

The contact in (14) must not be treated as an independent term when (1) is
only rewritten in new coordinates.

Let independent edge coordinates be `ell^a` and new coordinates be `y^i`,
with

    L^a_i=partial_i ell^a,
    K^a_ij=partial_i partial_j ell^a.                         (22)

For any scalar action `S(ell)`, the pullback Hessian is

    (H_y)_(ij)=L^a_i H_(ab) L^b_j+S_a K^a_ij.               (23)

Apply (23) separately to `S_g` and `U_s=-cJ_a ell^a`. Since `U_s` is affine
in the independent edge lengths, `H_U=0`. At a fully stationary point,

    g_a + u_a=0,
    g_a=cJ_a,
    u_a=-cJ_a.                                               (24)

Adding the two pullbacks gives

    H_y^tot
      =L^dagger H_g L+(g_a+u_a)K^a
      =L^dagger H_g L.                                      (25)

For the proper-length map, the two connection pieces are

    g_a K^a=-C_s,
    u_a K^a=+C_s.                                           (26)

This is the **stationary pullback cancellation**. It is a coordinate-covariance
identity, not a dynamical Ward completion. Adding `+C_s` to an already
stationary edge-coordinate Hessian while omitting `-C_s` double counts the
coordinate connection.

The Block-21 homogeneous source roots are only stationary in five normal
directions and use ten affine reactions. Therefore (25) is not promoted to a
claim that their complete reacted Hessian is already covariant. The missing
reaction curvature, source transformation, nonuniform stationarity, and
background-dependent generator remain precisely the open terms. Partial
stationarity is a named wall, not silently replaced by (24).

## 7. Explicit Geometry-Spreading Escape

The support bound is sharp in dimension. Exhausting the `15 choose 6` edge
charts, the runner finds a well-conditioned physical chart with directions

    (0,0,0,1), (0,0,1,1), (0,1,0,0),
    (0,1,1,0), (1,0,0,0), (1,0,1,0).                        (27)

Its `6 x 6` restriction `R` has smallest singular value `0.530649...` and
condition number `1.834997...`. For each source define

    W_s=R^(-dagger)(-M_s)R^(-1).                             (28)

Then

    R^dagger W_s R=-M_s                                     (29)

to residual below `7e-16`. The three `W_s` are indefinite and source
responsive. Equation (28) is not proposed as a physical counterterm: it is
target-tailored, not proper-cubic covariant as written, and has no supplied
source law. It is an exact steelman proving that six-edge geometry-spreading
can evade Proposition 1.

Other live structural routes are:

- a covariant area, volume, coframe, or simplex term in which one source
  insertion differentiates through at least six independent geometry
  combinations;
- dynamical worldline/history variables whose mixed and source blocks both
  scale as `p=q=1`, giving an `O(c)` Schur term with a derived zero-source rank
  change;
- a nonuniform closed-history source with exact translated Ward support and a
  fully solved background;
- a richer Regge/perfect/refined action whose background-dependent generator
  closes at the selected resolution; or
- a selected curved or massive phase in which `M_s` is interpreted rather
  than canceled, with its scale and stability derived from the same law.

The local joint action remains open. Equation (28) prevents the present
negative from being misread as algebraic impossibility.

## 8. Exact Axiom/Law Issue

The current axioms do not select:

- the physical source coordinate or history;
- whether its local action is proper length, area, volume, a determinant, or
  a dynamical constrained action;
- how a source insertion spreads over neighboring simplex/coframe variables;
- the source transformation and background-dependent gauge generator;
- full versus partial stationarity and compact-mode treatment; or
- a massless, curved, or massive physical phase.

This block therefore does not prove an axiom must be changed. The missing
content may be a downstream construction. If that construction cannot be
derived, the sufficient or target-equivalent amendment is now more precise:

> A realized geometry/history law selects a local joint source and geometry
> action, its action unit and additive normalization, the source variables and
> transformations, and a fully stationary nonuniform background. In a
> selected massless phase, the action-derived direct and mixed/source Hessian
> blocks span every first-order physical source coefficient not removed by the
> differentiated Ward identity; support spreading or any zero-source rank
> change is derived from the same local variables rather than inserted as a
> counterterm. A selected curved or massive phase instead derives its scale,
> constraints, causal propagation, and nonlinear stability from that action.

This wording is unadopted, sufficient or target-equivalent, and not proven
minimal or necessary. Adoption requires explicit user/governance authority.

## 9. N1--N8 No-Go Discipline

### N1 — Alternative-route enumeration

| route | treatment | status |
|---|---|---|
| sign-fixed proper-length contact | compute (14) on all three source rows | attempted; ranks `2/3/4`, no cancellation |
| scalar-rescaled proper-length contact | solve (21) exactly | attempted; large residuals remain |
| arbitrary active-edge Hessian | allow every Hermitian `W` on each `m_s` support | bounded by Proposition 1 |
| coordinate/coframe rewrite | include both geometry and source connection pieces | attempted; exact cancellation (26) |
| six-edge geometry spreading | construct (27)--(29) | succeeds algebraically; law/selection absent |
| dynamical source sector | Block-23 `p=q=1` mixed/source blocks | live; not executed here |
| nonuniform closed history | translated Ward-compatible source and full background | live; not executed here |
| curved or massive phase | retain nonzero `M_s` with derived scale/stability | live; not executed here |

### N2 — Wall-independence audit

Two independent walls are proved:

1. support confinement gives the rank bound (19), even if the contact is a
   genuinely new action term; and
2. coordinate-only rewriting gives (25), even before applying the rank bound.

Neither is inferred from the other. The full-stationarity condition in (24)
is not used to prove Proposition 1. The support count is not used to prove the
pullback identity.

### N3 — Hidden-wall scan

Promoted conditions:

- `W1`: exactly the three retained source rows and their active supports;
- `W2`: exactly the six homogeneous flat physical metric modes;
- `W3`: direct Hessians confined to active edge coordinates for (19);
- `W4`: affine edge source `U_s=-cJ dot ell` and full stationarity for (25);
- `W5`: cancellation of the complete `O(c)` six-mode coefficient as the
  tested massless-phase target.

Changing support, adding source variables, solving a nonuniform background,
or selecting a curved/massive target changes the theorem and remains live.

### N4 — Residual matching

Block 23's residual was a selected local first-order completion. This block
tests two concrete subroutes: direct proper-length contact and coordinate-only
seagull transfer. It does not substitute the cut-coframe family, the
closed-line flat Ward identity, or an arbitrary matrix completion for the
missing joint action. The surviving residual is action derivation plus full
nonuniform stationarity, exactly matching the parent.

### N5 — Resolution gate

The runner emits exactly five substantive resolution lines:

1. the negative is restricted to active-edge-support contacts and coordinate
   rewrites;
2. a common six-edge constructive escape is supplied;
3. gravity/source/worldline/axiom impossibility rhetoric is excluded;
4. geometry-spreading, dynamical, nonuniform, richer-action, and curved routes
   remain open; and
5. physical selection, locality, full stationarity, continuum, Lorentzian,
   and nonlinear closure remain unresolved.

### N6 — Rhetoric audit

Allowed: “the retained proper-length contact cannot cancel the complete
six-mode coefficient” and “a coordinate-only seagull is not an independent
repair.” Forbidden: “matter contacts cannot fix gravity,” “Regge gravity
fails,” “six new fields are necessary,” or “the axioms are inconsistent.”
This is not a gravity no-go and not an axiom necessity result.

### N7 — Actionable steelman

The strongest response is constructive: a local source insertion may couple
to the surrounding simplex volume, coframe area, or dynamical history
variables, so its second variation is not confined to the nonzero entries of
`J_s`. Equation (28) proves six independent geometry combinations are enough
at coefficient level. A dynamical source sector can also produce the required
first order through `p=q=1`. The next artifact must derive one such structure,
not merely choose `W_s=-M_s`.

### N8 — Cross-cycle echo

| earlier boundary | later mechanism | lesson applied |
|---|---|---|
| fixed-normal Block-21 obstruction | Block-22 momentum-dependent quotient escaped it | do not promote a support-confined negative |
| inherited Block-22 Ward defect | Block-23 constructed abstract Schur completions | provide an explicit escape before narrowing |
| Block-23 regular auxiliary order mismatch | `p=q=1` singular/dynamical route remained | keep source dynamics live |
| cut-coframe same-family seagull | present transfer gives rank and connection boundaries | derive contacts in the actual action; do not transfer by analogy |
| closed-line flat Ward carrier | present homogeneous sources remain reacted/partial | full nonuniform stationarity is the next physical test |

**N1--N8 status: `PASS` only** for the active-edge-support direct-contact
rank boundary and the fully stationary coordinate-pullback cancellation.

## 10. Assumption And Provenance Ledger

| item | status | use |
|---|---|---|
| current minimal axioms | source-bound premise boundary | establish only that no joint source/gravity law is selected |
| fifteen actual edge classes and metric map | retained constructed input | formulas (2), (9), and physical carrier |
| three source rows | retained supplied compact sources | support inventory and contacts |
| Block-23 `M_s` | reconstructed numerical input | tested cancellation targets |
| proper-length metric family | explicit conditional action family | direct contact test, not physical selection |
| full stationarity | condition of Proposition 2 / equation (25) | not asserted for reacted homogeneous roots |
| six-edge chart | constructed algebraic control | escape only, not action or axiom |
| TOE percentages | fixed campaign rubric | unchanged |

No premise is silently promoted to an observation, audit verdict, physical
source, or canonical axiom.

## 11. Verification And Exact Next Work

The runner:

1. source-binds the axioms, parent, cut-coframe, closed-line, and premise
   registry;
2. reconstructs the six physical modes and three `M_s` from the actual Regge
   carrier;
3. proves the physical frame lies in the affine metric tangent;
4. checks (13) independently on all fifteen edge directions;
5. constructs (15) both from metric and physical-row representations;
6. verifies support/contact ranks, sign-fixed inertias, and scalar-optimal
   residuals;
7. verifies the exact geometry-connection/source-seagull cancellation;
8. exhausts all six-edge charts and constructs (28) on the best-conditioned
   one; and
9. emits all five N5 certificates and the declared coverage boundaries.

Expected result:

    TOTAL: PASS=16 FAIL=0

The exact next science is to construct a geometry-spreading or dynamical
source action from retained local variables, solve one fully stationary
nonuniform closed-history background, and compute the complete direct, mixed,
source, multiplier, and connection Hessian. Only that action can determine
whether the selected phase restores an `O(k^2)` massless quotient or instead
derives a curved/massive response. Until then, no canonical axiom edit and no
fixed-percentage move is licensed.
