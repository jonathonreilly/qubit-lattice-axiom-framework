---
claim_id: cube_rotation_group_not_cyclic_dihedral_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Let G be the 24-element set of 3x3 signed permutation matrices with det=+1. Element orders in G lie in {1,2,3,4} only, the maximum is 4, and G has an order-4 element. Therefore G is not cyclic of order 24 and is not dihedral of order 24. The argument uses only matrix orders in G. It does not classify all order-24 subgroups of SO(3) and does not adopt an M_2 action."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_rotation_group_not_cyclic_dihedral_2026_08_14.py
---

# The 24 Cube Rotations Are Not `C_24` And Not `D_12`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer order census of one displayed 24-element matrix
set `G`. No classification of all order-24 subgroups of `SO(3)`. No
`M_2` action. No Qubit rewrite.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_rotation_group_not_cyclic_dihedral_2026_08_14.py`](../scripts/cube_rotation_group_not_cyclic_dihedral_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `G` be the set of all `3 × 3` signed permutation matrices with
`det = +1`. Each row and each column has a single nonzero entry in
`{+1, −1}`. There are `3! · 2^3 = 48` signed permutation matrices, and
exactly those with determinant `+1` belong to `G`. Direct listing gives
`|G| = 24`.

The order of `R ∈ G` is the least integer `k > 0` with `R^k = I`.
Enumeration of all 24 elements yields only the orders `1, 2, 3, 4`,
with multiplicities `1`, `9`, `8`, and `6` respectively. The maximum is
`4`, realized by a `90°` rotation about a coordinate axis. In particular
`G` has at least one element of order `4`, and no element of order `12`
or `24`.

`C_24` has an element of order `24`. Therefore `G` is not cyclic of
order `24`.

`D_12`, the dihedral group of order `24`, has a cyclic subgroup of
order `12`, hence an element of order `12`. `G` has no element of order
`12`, so `G` has no cyclic subgroup of order `12`. Therefore `G` is not
dihedral of order `24`.

The proof uses only this order census in `G`. It does not use an action
on the four space diagonals, and it is independent of the `S_4`-via-
diagonals isomorphism.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact enumeration of matrix orders in the displayed 24-element set G shows that G is not C_24 and not D_12."
trace_class: negative_route_pruning
target_claim_id: cube_rotation_group_not_cyclic_dihedral
target_blocker_text: "whether the 24-element cube-rotation set is C_24 or D_12"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded algebraic claim"
conditional_surface_status: "exact for the displayed 24-element matrix set G; no SO(3) classification and no M_2 action"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** For the displayed set `G`, prove `|G| = 24`, prove that
every element order lies in `{1, 2, 3, 4}`, prove that the maximum order
is `4` and is attained, and conclude that `G` is neither `C_24` nor
`D_12`.

| Obligation | Disposition |
|---|---|
| list of all `det = +1` signed permutation matrices | proved here; `|G| = 24` |
| element orders by repeated product until `I` | proved here; only `1, 2, 3, 4` |
| existence of an order-`4` element | proved here by a coordinate-axis `90°` matrix |
| `G` is not `C_24` | Theorem 1 |
| `G` is not `D_12` | Theorem 2 |

Boundary cases stay open on purpose. Other 24-element subsets of `SO(3)`,
improper signed permutations (`det = −1`), and any action on a one-site
algebra are outside the target. No terminal lemma for the two identifications
is left open.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  Lattice vocabulary that names proper cubic rotations about each site. As the
  registered `minimal_axioms` premise, it is not a bounded-status source.
- `G` is displayed matrix data: the `3 × 3` signed permutation matrices of
  determinant `+1`. Entries lie in `Z`.
- No measured, fitted, observational, literature, or other phenomenological
  value is used.
- No `M_2` representation, menu, or Record rule is an input.

## Exact Objects

Work in `M_3(Z)`. A signed permutation matrix has, in each row and each
column, exactly one nonzero entry, and that entry is `+1` or `−1`.

```text
G = { R in M_3(Z) : R is a signed permutation matrix and det(R) = +1 }.
```

Matrix products and determinants are the ordinary integer formulas. The
identity is `I = ((1,0,0), (0,1,0), (0,0,1))`. A displayed order-`4`
witness, a `90°` rotation about the third coordinate axis, is

```text
R_* = ((0,-1,0), (1,0,0), (0,0,1)).
```

Direct products give `R_*^2 = ((-1,0,0), (0,-1,0), (0,0,1))`,
`R_*^3 = ((0,1,0), (-1,0,0), (0,0,1))`, and `R_*^4 = I`, while no
smaller positive exponent is `I`.

## Theorem 1 — `G` is not cyclic of order 24

The `48` signed permutation matrices split by determinant into two sets
of equal size. Restricting to `det = +1` lists `24` distinct matrices,
so `|G| = 24`.

For each `R ∈ G` the products `R, R^2, …` are computed in `M_3(Z)` until
`I` appears. The first return occurs at an exponent in `{1, 2, 3, 4}`
for every listed matrix. In particular the maximum order in `G` is `4`,
attained by `R_*` and by the other coordinate-axis `90°` rotations.

A cyclic group of order `24` has an element of order `24`. `G` has none.
Therefore `G` is not isomorphic to `C_24`.

## Theorem 2 — `G` is not dihedral of order 24

Write `D_12` for the dihedral group of order `24`. That group contains
the cyclic rotation subgroup of a regular 12-gon, a cyclic subgroup of
order `12`. Any cyclic subgroup of order `12` is generated by an element
of order `12`.

The census of Theorem 1 shows that `G` has no element of order `12`.
Therefore `G` has no cyclic subgroup of order `12`, and `G` is not
isomorphic to `D_12`.

## Physical-Interpretation Boundary

The proved output is the pair of non-identifications `G ≇ C_24` and
`G ≇ D_12`. This note does not assign `G` a one-site algebra action and
does not change the Qubit sentence. `G` is displayed matrix data, not
axiom content, and no additional axiom is proposed.

## Mutation Checks

1. Replace the maximum-order target `4` by `24`: the listed orders still
   stop at `4`.
2. Assert an element of order `12`: none of the 24 matrices returns at
   exponent `12` as a first return.
3. Drop the determinant filter: the unsigned-sign listing has 48 matrices
   and is not the displayed set `G`.

## What This Does Not Claim

- This note does not classify all order-24 subgroups of SO(3).
- This note does not adopt an `M_2` action.
- No Qubit rewrite.
- No claim that `G` is the unique 24-element subgroup of `SO(3)`.
- No use of the action on four space diagonals, and no reliance on an
  `S_4` isomorphism.
- Improper signed permutations are not included in `G`.
- No Record, Admissibility, or menu-selection claim.

These are scope boundaries, not a census of every finite subgroup of
`SO(3)`.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> No site is privileged. Sites are distinguished by the supplied lattice structure alone.

Their dependency role is limited to the repository's Lattice vocabulary
that names proper cubic rotations. This theorem separately supplies the
matrix set `G` and its order census.

## Runner Contract

The companion runner lists all 24 matrices in `G`, computes each order by
repeated integer product until `I`, asserts `|G| = 24`, asserts that the
maximum order is `4`, asserts that the number of order-`4` elements is at
least one, and asserts that no listed order is `12` or `24`. Declared
review inputs are this note and the axiom memo only.
