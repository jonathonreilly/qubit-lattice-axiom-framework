---
claim_id: admissibility_dirac_kahler_metric_compatible_exterior_transport_bounded_theorem_note_2026-08-27
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_METRIC_COMPATIBLE_EXTERIOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-27.md
claim_type: bounded_theorem
claim_scope: "Exact classification of tangent one-form isometries between positive D3 cells by an orthogonal coframe factor; construction of the volume-normalized exterior lift that is exactly isometric for the full D3 carrier and intertwines the weighted exterior Clifford generators; reduction of the Block 215 endpoint-symmetric cross-form to a covariant centered half-hop; and exact separation of endpoint metric data from independent orthogonal edge-connection freedom. Coframes and orthogonal edge factors are supplied. Their physical selection, plaquette curvature law, time interpretation, dynamics, gravity equation, and continuum limit remain separate questions."
runner: scripts/admissibility_dirac_kahler_metric_compatible_exterior_transport_2026_08_27.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_bounded_theorem_note_2026-08-27
target_blocker_text: "compatibility of U_sr with changing tangent/Clifford frames"
source_of_blocker_text: proof_obligation_graph
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Compose the compatible links around a plaquette, prove that the endpoint-only coframe section is flat, and isolate the nontrivial holonomy carried by the independent orthogonal edge factors."
conditional_surface_status: "stacked on unmerged Blocks 214-215; proposed science remains review- and audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the tangent-map factorization and exterior-carrier/Clifford identities are exact finite-dimensional theorems, checked symbolically on rational coframes and orthogonal links"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-metric-dynamics-bridge-block215-variable-cell-edge-kernel-20260827
parent_commit: 2d103defc71b5105f184c3b6cc958dcdd0905913
current_main: 66e478505e055faf4a5b9e6f4883211e44304718
registered: 0
adopted: 0
axiom_movement: none
---

# Metric-compatible exterior transport and connection freedom

**Date:** 2026-08-27

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result in plain language

The [variable-cell edge theorem](ADMISSIBILITY_DIRAC_KAHLER_VARIABLE_CELL_WEIGHTED_SKEW_EDGE_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-27.md)
proved exactly how two unequal positive cell carriers may be coupled without
breaking weighted skew-adjointness. It deliberately treated the comparison
map between the cells as supplied data. This note now identifies the precise
comparison maps that respect both the changing tangent metric and the full
weighted exterior Clifford system.

Write the inverse metric at each endpoint as a coframe square

```text
h_s := g_s^-1 = E_s^T E_s.
```

Every tangent one-form isometry from cell `r` to cell `s` is exactly

```text
A_sr = E_s^-1 R_sr E_r,       R_sr^T R_sr = I.       (1)
```

Let `Lambda(A_sr)` act on all exterior degrees by the minors of `A_sr`. On
the metric-volume locus `V_s^2=det(g_s)`, the normalized exterior link

```text
U_sr = sqrt(V_r/V_s) Lambda(A_sr)                    (2)
```

is an exact isometry from the `r` carrier to the `s` carrier and intertwines
their complete Clifford systems. The square-root density in (2) is forced by
the scalar sector of the carrier.

Equation (1) is also the central boundary result: the endpoint metrics fix
the coframe factors but do not fix `R_sr`. That orthogonal edge factor is
independent connection data. This block exposes it; it does not pretend to
derive its physical value.

## Exact hypotheses and conventions

The hypotheses are:

1. two positive symmetric three-dimensional cell metrics `g_s,g_r`;
2. positive volumes on the parent locus `V_s^2=det(g_s)` and
   `V_r^2=det(g_r)`;
3. chosen invertible coframes `E_s,E_r` satisfying
   `g_s^-1=E_s^T E_s` and `g_r^-1=E_r^T E_r`;
4. the parent D3 carriers and weighted exterior generators;
5. one supplied orthogonal matrix `R_sr` on each oriented edge.

The tangent map acts on one-form coefficient columns from the `r` frame into
the `s` frame. Its exterior lift is fixed by

```text
Lambda(A) epsilon_r(q) = epsilon_s(Aq) Lambda(A).    (3)
```

The [Lattice axiom](MINIMAL_AXIOMS_2026-06-29.md#lattice--physical-locality)
supplies adjacency, not the coframes or orthogonal edge factors. No new axiom
or primitive is introduced.

## Tangent-isometry classification

The tangent compatibility equation is

```text
A_sr^T g_s^-1 A_sr = g_r^-1.                       (4)
```

Substituting (1) immediately proves (4). Conversely, if (4) holds, define

```text
R_sr := E_s A_sr E_r^-1.                            (5)
```

Then

```text
R_sr^T R_sr
 = E_r^-T A_sr^T E_s^T E_s A_sr E_r^-1
 = E_r^-T g_r^-1 E_r^-1
 = I.                                               (6)
```

Thus (1) is if-and-only-if. Each connected component of `O(3)` supplies
three continuous edge parameters. Orientation reversal is allowed
algebraically; restricting to `SO(3)` would be an additional orientation
choice, not a consequence of positive metric compatibility.

Taking determinants of (4) gives

```text
|det A_sr| = V_s/V_r.                               (7)
```

This identity is what makes one normalization work simultaneously on every
exterior degree.

## Full exterior-carrier isometry

Let `D_s` be the parent D3 carrier, whose degree-zero block is `V_s`, degree-
one block is `V_s g_s^-1`, degree-two block is the induced two-form metric,
and degree-three block is `1/V_s`. The natural exterior lift obeys

```text
Lambda(A B) = Lambda(A) Lambda(B).                  (8)
```

Let `S=diag(1,-1,1)` for the parent two-form ordering. The lift blocks and
carrier identities are explicit:

| degree | lift block | carrier block | transformed block before the common density |
|---|---|---|---|
| 0 | `1` | `V_s` | `V_s` |
| 1 | `A` | `V_s g_s^-1` | `V_s g_r^-1` by (4) |
| 2 | `S(det A)A^-T S` | `S g_s S/V_s` | `(det A)^2 S g_r S/V_s` |
| 3 | `det A` | `1/V_s` | `(det A)^2/V_s` |

Here the degree-two line uses `g_r=A^-1 g_s A^-T`, the inverse of (4).
Multiplying every row by `V_r/V_s` from the square of (2), and using
`(det A)^2=V_s^2/V_r^2` from (7), gives on all four exterior degrees

```text
U_sr^T D_s U_sr = D_r.                              (9)
```

The degree-zero block alone reads

```text
(V_r/V_s) V_s = V_r,
```

so it fixes the magnitude of the scalar density before any higher-form
algebra is considered. Equation (2) chooses the positive root so the scalar
unit has positive normalization. Multiplying the whole link by `-1`, or by an
additional compatible module-commutant factor, is extra fibre freedom and is
not classified as tangent geometry here. The runner verifies all 64 entries
of (9) exactly on four rational coframe cells, including one orientation-
reversing edge.

## Clifford intertwining

Let

```text
Gamma_s(q) = epsilon_s(q) + epsilon_s(q)^dagger_Ds.
```

Equation (3) transports the wedge term. Equation (9) transports its weighted
adjoint, hence

```text
Gamma_s(A_sr q) U_sr = U_sr Gamma_r(q)              (10)
```

for every one-form direction `q`. This is the tangent/Clifford compatibility
left open by Block 215.

The result concerns the normalized natural exterior lift. It does not claim
that an arbitrary `8 x 8` Clifford intertwiner is unique without further
module-normalization or commutant conditions.

## Collapse of the Block 215 edge section

For a direction `q` at `r`, put

```text
B_r(q) = D_r Gamma_r(q),
B_s(Aq) = D_s Gamma_s(Aq).
```

Equations (9)–(10) imply

```text
B_s(Aq) U_sr = U_sr^-T B_r(q).                      (11)
```

The two endpoint contributions in the preceding block's cross-form are
therefore identical:

```text
C_sr(q)
 = [B_s(Aq)U_sr + U_sr^-T B_r(q)]/4
 = B_s(Aq)U_sr/2.                                   (12)
```

Consequently the forward half-hop has either equivalent form

```text
K_sr(q) = Gamma_s(Aq)U_sr/2
        = U_sr Gamma_r(q)/2.                         (13)
```

Together with the forced reverse block from Block 215, this is the exact
variable-cell analogue of the constant centered exterior link.

## Coframe gauge and genuine edge freedom

The square root `E_s` is not unique. Replacing it by

```text
E_s -> Q_s E_s,       Q_s in O(3),
```

leaves `g_s^-1` unchanged. Equation (1) leaves `A_sr` unchanged when

```text
R_sr -> Q_s R_sr Q_r^T.                             (14)
```

This is the exact local coframe-gauge law. It also shows why `R_sr` cannot be
read off from the two endpoint metrics alone. Even for equal flat endpoint
metrics, every nonidentity orthogonal `R_sr` gives a distinct compatible
link.

Choosing the endpoint-only section `R_sr=I` is mathematically valid, but it
is one section rather than a physical derivation. Its plaquette content, and
the part of holonomy carried by nontrivial `R_sr`, are the next theorem
target.

## Exact witness and mutations

The runner uses four rational coframes and four exact rational orthogonal
matrices (three Pythagorean rotations and one reflection). It verifies:

- `V^2=det(g)` and the local weighted Clifford identities;
- tangent congruence and recovery of orthogonal `R`;
- the determinant-volume law and exterior functoriality;
- wedge naturality, the complete D3 isometry, and Clifford intertwining;
- reverse-link inversion;
- the cross-form collapse and covariant centered half-hop;
- nontrivial compatible links between equal metrics;
- coframe-gauge covariance and the constant-cell limit.

Three declared mutations isolate load-bearing ingredients:

1. omitting the density factor breaks the full carrier isometry;
2. transposing a target coframe breaks tangent compatibility;
3. transposing the exterior minors breaks wedge naturality.

## Proof-obligation graph

| Obligation | Disposition |
|---|---|
| variable-cell weighted-skew edge classification | supplied by Block 215 and used through its cross-form formula |
| classification of tangent metric isometries | proved by equations (4)–(6) |
| volume normalization of the exterior lift | proved degreewise and checked exactly |
| wedge and Clifford transport | proved by naturality plus carrier isometry; checked exactly |
| reduction of the endpoint-symmetric edge section | proved by equations (11)–(13) |
| coframe-gauge covariance | proved by equation (14) and checked exactly |
| physical selection of `R_sr` | open and explicitly not imported |
| plaquette holonomy/curvature decomposition | next theorem target |
| time, Lorentzian continuation, action, backreaction, continuum | outside this finite theorem |

The proof graph is acyclic. Metric compatibility is strictly stronger than
the weighted-skew existence theorem supplied by Block 215, while curvature
and dynamics are strictly stronger than the single-edge compatibility proved
here.

## Scope boundary

This block establishes an exact finite kinematic bridge from changing local
metrics to compatible exterior-fermion transport. It does not derive a
physical spin connection, an action for `R_sr`, Einstein dynamics, a time
direction, Lorentzian signature, or a continuum limit. No empirical value,
fitted parameter, or external field equation is used. Existing Lattice-axiom
adjacency is the sole axiom-level input; no new axiom or framework primitive
is introduced.
