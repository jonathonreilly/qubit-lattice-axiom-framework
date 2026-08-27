---
claim_id: admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_bounded_theorem_note_2026-08-27
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_VARIABLE_CELL_WEIGHTED_SKEW_EDGE_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-27.md
claim_type: bounded_theorem
claim_scope: "Exact finite-graph classification of every zero-diagonal nearest-neighbour kernel that is skew-adjoint in a site-dependent positive block inner product; an endpoint-symmetric, local-frame-covariant cross-form construction from supplied D3 cells and invertible link comparisons; exact reduction to the constant-cell centered exterior link; and one four-cell rational witness. The link comparisons and D3 cells are supplied. Their physical selection, tangent compatibility, curvature law, time interpretation, dynamics, gravity equation, and continuum limit remain separate questions."
runner: scripts/admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_2026_08_27.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_weighted_exterior_kernel_metric_symbol_bounded_theorem_note_2026-08-27
target_blocker_text: "the transport/connection terms needed for adjointness when neighboring cells have different carriers"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Impose metric and tangent-Clifford compatibility on the supplied link comparisons, classify their orthogonal freedom, and identify which part of plaquette holonomy is independent connection data."
conditional_surface_status: "stacked on an unmerged ancestor chain; proposed science remains review- and audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the edge classification is an if-and-only-if algebraic theorem, and the D3 construction is checked with exact rational matrices under arbitrary local frame changes"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block214-weighted-kernel-metric-symbol-20260827
parent_commit: b2ebf69b0de86538c6e9cc0d3d4a96a4e0dc9a81
current_main: 66e478505e055faf4a5b9e6f4883211e44304718
registered: 0
adopted: 0
axiom_movement: none
---

# Variable-cell weighted-skew exterior edge coupling

**Date:** 2026-08-27

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result in plain language

The preceding [metric-weighted exterior-kernel theorem](ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_EXTERIOR_KERNEL_METRIC_SYMBOL_BOUNDED_THEOREM_NOTE_2026-08-27.md)
constructed the exact centered link when every cell carries the same positive
matrix `D3`. Its next stated problem was that neighboring cells can carry
different matrices, so simply copying the same forward and backward hop no
longer guarantees skew-adjointness.

This note solves that specific finite algebra problem completely. On each
undirected edge, choose one orientation `s -> r` and one cross-form `C_sr`.
Then set

```text
K_sr = D_s^-1 C_sr,
K_rs = -D_r^-1 C_sr^T.
```

Every such edge pair is skew-adjoint in the block inner product, and every
zero-diagonal nearest-neighbor weighted-skew kernel has exactly this form.
The result works for arbitrary site-dependent positive carriers; unequal
cell weights do not obstruct weighted skew-adjointness.

The theorem separates existence from physics. It supplies the full algebraic
solution space, while selection of a particular cross-form remains additional
structure. One explicit endpoint-symmetric construction is given below from
local exterior direction matrices and supplied invertible link comparisons.

## Exact target and hypotheses

**Target.** Given a finite nearest-neighbor graph, positive symmetric site
carriers `D_s`, and the constant-cell exterior link of the parent theorem,
construct and classify local edge blocks whose global operator is
skew-adjoint in `H = direct_sum_s D_s` and which reduce to the parent centered
link when all cells and comparisons agree.

The hypotheses are:

1. a finite graph with one chosen orientation for each undirected edge;
2. a real finite-dimensional fibre of common dimension `n` at every site;
3. an invertible symmetric matrix `D_s` at each site; positivity is used for
   the inner-product reading but not for the edge classification itself;
4. for the constructed D3 family only, local direction matrices `Gamma_s,d`
   satisfying `Gamma_s,d^T D_s = D_s Gamma_s,d`;
5. for the constructed family only, one supplied invertible comparison map
   `U_sr` from the `r` coordinates to the `s` coordinates.

The [Lattice axiom](MINIMAL_AXIOMS_2026-06-29.md#lattice--physical-locality)
supplies nearest-neighbor adjacency, but it does not select the matrices in
items 3–5. Those are declared inputs at this theorem boundary.

## The edge classification theorem

Let `K_sr` denote the block mapping the fibre at `r` into the fibre at `s`.
For the block-diagonal carrier

```text
H = direct_sum_s D_s,
```

the `(s,r)` block of `H K + K^T H` is

```text
D_s K_sr + K_rs^T D_r.                         (1)
```

Choose one orientation `s -> r` for each undirected edge and define

```text
C_sr := D_s K_sr.                               (2)
```

Equation (1) vanishes if and only if

```text
K_sr = D_s^-1 C_sr,
K_rs = -D_r^-1 C_sr^T.                          (3)
```

This proves both directions:

- any cross-form `C_sr` inserted through (3) gives a weighted-skew edge;
- any weighted-skew edge has the unique cross-form (2), and its reverse block
  is forced by (3).

Different edges do not mix in equation (1), so the theorem assembles over the
whole graph. With `m` undirected edges and fibre dimension `n`, the
zero-diagonal edge-supported solution space has exactly `m n^2` real
coordinates before any further covariance, Clifford, or physical-selection
condition is imposed. Reversing the chosen representative orientation for the
same operator replaces the cross-form by `C_rs=-C_sr^T`; it does not create a
second independent edge datum.

## A local-frame-covariant constructed family

Define the symmetric local direction form

```text
B_s,d := D_s Gamma_s,d,
B_s,d^T = B_s,d.                                (4)
```

For a supplied invertible comparison `U_sr`, define

```text
C_sr,d = (B_s,d U_sr + U_sr^-T B_r,d)/4.        (5)
```

The factor `1/4` gives the correct constant-cell normalization: if
`D_s=D_r=D`, `Gamma_s,d=Gamma_r,d=Gamma_d`, and `U_sr=I`, then

```text
C_sr,d = D Gamma_d/2,
K_sr = Gamma_d/2,
K_rs = -Gamma_d/2.                              (6)
```

Thus the parent kernel `Gamma_d(T_d-T_d^-1)/2` is recovered exactly.

The construction is also covariant under independent invertible local frame
changes. Use the coordinate convention

```text
psi_s' = G_s psi_s,
D_s' = G_s^-T D_s G_s^-1,
Gamma_s,d' = G_s Gamma_s,d G_s^-1,
U_sr' = G_s U_sr G_r^-1.                        (7)
```

Then equations (4)–(5) give

```text
C_sr,d' = G_s^-T C_sr,d G_r^-1,                 (8)
K_sr' = G_s K_sr G_r^-1.                        (9)
```

Consequently the full matrices transform as

```text
H' = G^-T H G^-1,
K' = G K G^-1,
```

and `H K + K^T H = 0` is frame independent.

Equation (5) is one endpoint-symmetric section of the full cross-form space,
not a uniqueness statement. The exact classification is equation (3).

## Exact rational witness

The runner builds a four-site ring. Its cells use the parent D3 carrier on the
metric-volume locus `V^2=det(g)` at

```text
g_0 = I,                                  V_0 = 1,
g_1 = metric(c_tx=3/5),                   V_1 = 4/5,
g_2 = metric(c_ty=5/13),                  V_2 = 12/13,
g_3 = metric(c_tx=c_ty=c_xy=11/50),       V_3 = 117/125.
```

All entries are rational. Every `D_s` is positive definite, every local
`Gamma_s,d` is `D_s`-self-adjoint, and every local Clifford anticommutator is
the exact inverse-metric coefficient. Four nontrivial rational comparison
maps are inserted into (5). The resulting `32 x 32` kernel has only the
declared edge blocks and obeys

```text
H K + K^T H = 0
```

entry by entry. A rational probe independently gives zero instantaneous
derivative of its quadratic `H` norm.

The runner then applies four independent nonorthogonal rational frame changes.
It verifies equations (8)–(9), the transformed carrier law, and transformed
weighted skew-adjointness exactly. Finally, a separate arbitrary-cross-form
test reconstructs all four `C_sr` matrices from `D_s K_sr`, so the test is not
limited to the endpoint-symmetric ansatz.

## Proof-obligation graph

| Obligation | Disposition |
|---|---|
| parent constant-cell `D3` and local `Gamma` construction | supplied by the linked parent note and rechecked exactly on four rational cells |
| edgewise weighted-skew classification | proved here by equations (1)–(3) |
| graph assembly | proved here because each off-diagonal block belongs to one undirected edge |
| endpoint-symmetric construction | proved here by substitution of (4)–(5) into (3) |
| independent local-frame covariance | proved here by equations (7)–(9) and exact four-site verification |
| constant-cell reduction | proved here by equation (6) and an exact four-site centered-difference check |
| physical selection of `U_sr` | open and not part of this theorem |
| compatibility of `U_sr` with changing tangent/Clifford frames | next theorem target |
| plaquette holonomy and curvature content | downstream of the compatibility theorem |

The proof graph is acyclic. The strongest missing lemma is not equivalent to
the theorem proved here: selecting a physically preferred compatible
connection is strictly stronger than classifying all weighted-skew edge
couplings.

## Imports and boundary

The finite matrix algebra and rational checks use no measured values, fitted
targets, empirical constants, or continuum field equations. The load-bearing
declared inputs are the parent `D3/Gamma` family and the chosen comparison maps.

This theorem establishes:

- exact existence and classification of variable-cell weighted-skew links;
- exact local-frame covariance of the constructed endpoint-symmetric family;
- exact recovery of the constant-cell exterior kernel.

Separate work is required to choose the comparison maps, relate their fibre
action to tangent-frame transport, form a physical curvature law, identify a
time direction or Lorentzian continuation, and supply dynamics, backreaction,
or a continuum limit. No axiom or framework primitive is added here.

## Review record

This note closes only the parent note's explicitly named weighted-adjoint edge
problem. It does not revise the earlier overlap-Hodge, gauge-link, or
common-differential packages. Those prior-art families were searched before
construction and do not contain equations (1)–(5) for the new site-dependent
`D3` carrier.

The independent audit lane alone controls any effective retained status.

## Reproduction

```bash
python3 scripts/admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_2026_08_27.py
```

Mutation checks used before review:

```bash
python3 scripts/admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_2026_08_27.py --mutation reverse_edge_sign
python3 scripts/admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_2026_08_27.py --mutation right_frame_law
python3 scripts/admissibility_dirac_kahler_variable_cell_weighted_skew_edge_coupling_2026_08_27.py --mutation constant_link_factor
```
