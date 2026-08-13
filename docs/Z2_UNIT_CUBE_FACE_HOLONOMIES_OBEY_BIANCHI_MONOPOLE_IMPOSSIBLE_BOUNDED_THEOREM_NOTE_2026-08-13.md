---
claim_id: z2_unit_cube_face_holonomies_obey_bianchi_monopole_impossible_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the unit cube, every Z2 link field has even face-holonomy sum (Bianchi / 2-cocycle). The odd 6-tuple (1,0,0,0,0,0) is therefore not a holonomy image, so a one-cube magnetic monopole is impossible for a link field. The identity uses an extra edge 1-form that Lattice and Admissibility do not name. The six face bits are not independent plaquettes and are not the June 10 4D SU(3) ln Z_L count."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z2_unit_cube_face_holonomies_obey_bianchi_monopole_impossible_2026_08_13.py
---

# Z2 Unit-Cube Face Holonomies Obey Bianchi; a Monopole 6-Tuple Is Impossible

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact `Z2` arithmetic on the twelve edges and six faces of one unit cube.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z2_unit_cube_face_holonomies_obey_bianchi_monopole_impossible_2026_08_13.py`](../scripts/z2_unit_cube_face_holonomies_obey_bianchi_monopole_impossible_2026_08_13.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

A link field on the unit cube is an assignment `θ ∈ {0,1}^12` to the twelve
edges. Each face holonomy is the sum of its four edge bits modulo 2. Because
every edge lies in exactly two faces, the six holonomies always sum to `0`
modulo 2. The 6-tuple `m = (1,0,0,0,0,0)` has odd weight, so it is not in the
image of the holonomy map. A magnetic monopole supported on one cube is
impossible for a link field.

This is a 2-cocycle identity on an extra object — `θ` on the twelve edges —
not a one-site Admissibility 6-tuple of possibilities. The cube is not six independent plaquette bits.
The count `N_p = 6` on this cube is not
`N_p(L=2) = 96` of 4D `SU(3)`. The groups `Z2` and `SU(3)` are different.
This note does not treat the June 10 `ln Z_L` object as a lemma.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The Bianchi identity and the missing monopole 6-tuple are proved by exact Z2 linear algebra on one cube. Lattice and Admissibility do not name the link field, so the identity is extra structure, not axiom content."
trace_class: negative_route_pruning
artifact_role: theorem
conditional_surface_status: "exact for every Z2 link field on one unit cube; no 4D SU(3) or continuum claim"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Vertices of the unit cube are `{0,1}^3`. The twelve edges are labeled:

- x-edges `0..3` at `(y,z) ∈ {0,1}^2` in order `(0,0)`, `(1,0)`, `(0,1)`, `(1,1)`
- y-edges `4..7` at `(x,z)` in the same order
- z-edges `8..11` at `(x,y)` in the same order

The six faces are the unordered 4-edge sets (orientation does not matter over
`Z2`):

```text
z=0: {0,5,1,4}
z=1: {2,7,3,6}
y=0: {0,9,2,8}
y=1: {1,11,3,10}
x=0: {4,10,6,8}
x=1: {5,11,7,9}
```

A link field is `θ ∈ {0,1}^12`. Face holonomy is

```text
H_f(θ) = (sum of the four edges of f)  (mod 2).
```

Write `H(θ) = (H_{z=0}, H_{z=1}, H_{y=0}, H_{y=1}, H_{x=0}, H_{x=1})`.
The Bianchi sum is `∑_{f=1..6} H_f(θ) (mod 2)`.

The extra object used by the identity is `θ` on the twelve edges. It is a
`Z2` 1-cochain on the 1-skeleton. Face holonomies are the coboundary
2-cochain on the six faces.

## Quoted Axiom Content

The parent memo names Lattice as the cubic lattice `Z^3` with nearest-neighbor
adjacency, and Admissibility as one fixed nearest-neighbor rule that determines,
for each site, the probability distribution over local possibilities from the
nearest-neighbor conditions. Those two sentences do not name a link 1-form, a
closed 2-cochain, or a six-component face-holonomy tuple. The identity below
therefore uses extra structure.

## Theorem 1 — Bianchi Identity On Every Link Field

For every `θ ∈ {0,1}^12`,

```text
∑_{f=1..6} H_f(θ) ≡ 0  (mod 2).
```

Proof. Each edge lies in exactly two faces, so the six face sums count every
edge twice. Twice any `Z2` bit is `0`. Hence the total is `0`.

Witnesses. The zero field `θ = 0` has `H = 0^6`. Flipping a single edge
changes the holonomy of exactly the two faces that contain that edge, so the
Bianchi sum stays `0`. The runner enumerates all `2^{12}` fields through
`face_holonomies(θ)` and `bianchi_sum(H)`.

## Theorem 2 — A One-Cube Monopole 6-Tuple Is Not In The Image

Let `m = (1,0,0,0,0,0)`. Then `∑ m_f ≡ 1 (mod 2)`. By Theorem 1, `m` is not
`H(θ)` for any link field `θ`. A magnetic monopole on one cube — a single
nonzero face holonomy with the other five faces flat — is impossible for a
link field.

The image of `H` is exactly the even-weight subspace of `{0,1}^6`, of size
`2^5 = 32`. The runner builds that image by enumerating every `θ`.

## Theorem 3 — The Cube Is Not Six Independent Plaquettes

Six independent `Z2` plaquette bits would be the full cube `{0,1}^6`, which
contains `m`. The holonomy map lands only in the Bianchi hyperplane. The six
face bits are therefore not independent. Bianchi is a 2-cocycle constraint on
the coboundary of `θ`, not a one-site Admissibility 6-tuple of possibilities.

The mutation predicate “every 6-tuple in `{0,1}^6` is a face-holonomy image”
fails on `m`.

## Theorem 4 — The Identity Uses Extra Structure

Lattice names `Z^3` with nearest-neighbor adjacency. Admissibility names a
nearest-neighbor distribution over one-site possibilities. Neither sentence
names a link 1-form or a closed 2-cochain. The extra object required for
Theorems 1–3 is `θ` on the twelve edges of this cube.

This note does not edit an axiom and does not claim that the identity is
already axiom content.

## Theorem 5 — This Cube Is Not The June 10 `ln Z_L` Object

The unit cube has `N_p = 6` faces. The June 10 4D `SU(3)` count
`N_p(L=2) = 96` is a different integer. Group `Z2` ≠ `SU(3)`.
The identity is not that `ln Z_L` object. The runner compares the two
integers and the two group names only as a non-identification check. It does
not treat the June 10 note as a lemma.

## No-Go Discipline Gate

**Result:** exact Bianchi identity and missing monopole 6-tuple on one `Z2`
unit cube. No 4D gauge axiom, no continuum monopole theorem, and no change to
the four-axiom memo.

**N1 alternative routes.**

1. Independent six-bit plaquette assignment: ruled out on this cube by
   Theorems 1–3.
2. A monopole 6-tuple as a holonomy image: ruled out by Theorem 2.
3. Reading the identity as one-site Admissibility content: blocked by
   Theorem 4; the extra object is the edge field.
4. Identifying this cube with the June 10 `ln Z_L` 4D `SU(3)` count: blocked
   by Theorem 5.

**N2 wall independence.** The double-counting identity, the missing odd
6-tuple, the independent-plaquette mismatch, the extra-object gap, and the
`N_p`/`SU(3)` non-identification are distinct statements.

**N3 hidden-wall scan.** The note uses no observed masses, no fitted
selector, and no axiom edit.

**N4 residual matching.** The residual is the Bianchi parity of six `Z2` face
holonomies on one cube. It is not a 4D Wilson free-energy residual.

**N5 rhetoric audit.** The negative statement is at the one-cube `Z2` link
field. It is not a claim that every continuum monopole is impossible, and it
is not a claim that Lattice or Admissibility already contain a gauge 1-form.

## Imports And Claim Boundary

- **Imported:** the 2026-06-29 Lattice and Admissibility sentences, quoted
  only to show that they do not name `θ`.
- **Computed here:** edge-face incidence, `H(θ)`, Bianchi sums, the image of
  `H`, and the failure of the independent-plaquette predicate on `m`.
- **Quoted count only, not a lemma:** `N_p(L=2) = 96`.
- **Not imported:** unmerged work, a gauge axiom, or any identification of
  this cube with 4D `SU(3)` plaquettes.

## Review Record

Source proposal only. The independent audit lane grades.
