---
claim_id: cube_gauss_source_is_a_3_cochain_not_record_i_at_a_vertex_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On one unit cube with a Z2 link field, the unique 3-cochain forced by summing the six face holonomies is identically zero. Vertex Record lock count I is a content-only domain cardinality on the eight vertices and is not that 3-cochain. The cube Gauss source, if written at all, is the displayed 3-cell value rho. The row does not install Newton, a coupling, an inverse-distance kernel, a mass identification, a new Bianchi theorem, or 4D color."
upstream_dependencies:
  - minimal_axioms
  - newton_law_derived_note
runner: scripts/cube_gauss_source_is_a_3_cochain_not_record_i_at_a_vertex_2026_08_13.py
---

# Cube Gauss source is a 3-cochain, not Record I at a vertex

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** one unit cube; exact `Z2` link algebra; vertex Record lock patterns.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_gauss_source_is_a_3_cochain_not_record_i_at_a_vertex_2026_08_13.py`](../scripts/cube_gauss_source_is_a_3_cochain_not_record_i_at_a_vertex_2026_08_13.py)

## Result Up Front

A putative cube Gauss source forced by a `Z2` link field is a 3-cochain `ρ`
on the cube. Face holonomies sum to `0` for every link field, because each of
the twelve edges lies in exactly two faces. Hence `ρ=0` identically.

Record scalar readout `I` on a vertex lock pattern is the number of locked
vertices. There exist patterns with `I=1`. That value is not the cube source
`ρ`. Record names a content-only count of locks. It does not name a 3-cochain
on cubes. The extra object for a lattice Gauss source is `ρ` on 3-cells.

Display `ρ`; do not adopt it.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two-count identity and the I-versus-rho type split are exact on one cube. Newton, mass, coupling, and any lattice-wide Gauss law remain uninstalled."
trace_class: negative_route_pruning
target_claim_id: cube_gauss_source_type
target_blocker_text: "name the cube Gauss source type without identifying vertex Record I with a 3-cochain"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the one-cube Z2 source type; physical Gauss law and Newton remain open"
hypothetical_axiom_status: "no axiom edit, adoption, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  Lattice sites as points of `Z^3` and the Record wording quoted below. The
  axiom memo chain-satisfies as an approved premise; it is not a source of
  bounded status.
- [`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) is cited only
  for its source-linearity non-claim: that packet does not promote
  source-linearity to a physical Newton law. This row does not import that
  packet's kernel algebra.
- The unit-cube edge and face listing below is reconstructed in this note. It
  is not taken as a lemma from any other row.

## Exact Objects

Label the twelve edges of the unit cube by

```text
x-edges 0,1,2,3
y-edges 4,5,6,7
z-edges 8,9,10,11
```

Reconstruct the six faces as four-edge sets so that each edge lies in exactly
two faces:

```text
z=0  {0,5,1,4}
z=1  {2,7,3,6}
y=0  {0,9,2,8}
y=1  {1,11,3,10}
x=0  {4,10,6,8}
x=1  {5,11,7,9}
```

A link field is `θ ∈ {0,1}^12`. The face holonomy of face `f` is the exact
`Z2` sum of its four edges,

```text
H_f = (sum_{e in f} θ_e) mod 2.
```

A putative Gauss source is a 3-cochain `ρ ∈ {0,1}` on the cube obeying

```text
(sum_f H_f) mod 2 ≡ ρ.
```

A vertex Record lock pattern is a partial map `L` from the eight vertices to
`{A,B}`. Unlocked vertices lie outside `dom(L)`. The Record count on that
pattern is the content-only domain cardinality

```text
I(L) = |dom(L)| ∈ {0,…,8}.
```

## Theorem 1

For every link field `θ`,

```text
sum_f H_f ≡ 0 (mod 2).
```

Proof. Expand the left-hand side as a sum of edge values. Each of the twelve
edges appears in exactly two reconstructed faces, so each `θ_e` is counted
twice. Twice any `Z2` value is `0`. Therefore any Gauss `ρ` forced by a link
field is `0`.

This two-count is the entire identity. It is not a new Bianchi theorem beyond
the two-count of each edge.

## Theorem 2

There exist lock patterns with `I=1`: lock one vertex and leave the other
seven unlocked. For every link field the forced source is `ρ=0`. Hence

```text
I=1 ≠ 0 = ρ.
```

Vertex Record `I` is not the cube source.

## Theorem 3

Quote Record
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)):

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

So `I` is a content-only count of locks. It does not name a 3-cochain on
cubes. The extra object for a lattice Gauss source is `ρ` on 3-cells.

## Theorem 4

This does not install Newton, a gravitational coupling, or an inverse-distance
kernel. It does not identify `I` with mass. Display `ρ`; do not adopt it.

The Newton parent is used only as a source-linearity non-claim. That parent
already records that source-linearity is not a physical Newton force law.
Nothing here enlarges that non-claim into a derivation.

## Theorem 5

Do not cite the two-count as a new Bianchi theorem beyond the two-count of
each edge. Do not claim 4D color.

## What This Does Not Claim

- It does not install Newton or identify `I` with mass.
- It does not adopt `ρ` as a primitive, an axiom edit, or a lattice-wide law.
- It does not derive a physical Gauss law off this one cube.
- It does not claim 4D color.
- It does not cite any unmerged pull request.

The safe downstream use is only the type split: the cube source forced by a
link field is the displayed 3-cochain `ρ=0`, and vertex Record `I` is a
different object.

## Runner Certificate

The paired runner reconstructs the six face lists, checks the two-count,
evaluates `bianchi_sum(theta)` on every `Z2` link field, evaluates
`record_I(locks)` on lock patterns including `I=1`, and checks that the
hostile predicate "`I=1` equals Gauss `ρ`" fails. Identity gates call
`bianchi_sum(theta)` and `record_I(locks)`.

Run:

```bash
python3 scripts/cube_gauss_source_is_a_3_cochain_not_record_i_at_a_vertex_2026_08_13.py
```
