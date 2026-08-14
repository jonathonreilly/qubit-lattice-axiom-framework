---
claim_id: cube_rotations_s4_diagonals_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "The group G of 3x3 signed permutation matrices with det=+1 has order 24. Its action on the four space diagonals of the cube is a homomorphism phi: G -> S_4, and phi is an isomorphism. No Aut(M_2) identification and no axiom text are asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_rotations_s4_diagonals_2026_08_14.py
---

# Cube Rotations Are Isomorphic To `S_4` Via Space Diagonals

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer identities for the 24-element group `G` of `3 × 3`
signed permutation matrices with `det = +1`, and for the homomorphism
`φ: G → S_4` given by the action on the four space diagonals. No physical
force law, no `Aut(M_2)` identification, and no axiom edit are asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_rotations_s4_diagonals_2026_08_14.py`](../scripts/cube_rotations_s4_diagonals_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `G` for the set of `3 × 3` matrices with entries in `Z` that have
exactly one nonzero entry in each row and each column, each nonzero entry
equal to `±1`, and determinant `+1`. This is the proper cube rotation group
acting on `R^3`: each element is an orthogonal matrix of determinant `+1`
that preserves the cube with vertices `(±1, ±1, ±1)`.

There are four space diagonals, labeled by a representative vertex:

```text
D0: ±(1, 1, 1)
D1: ±(1, 1, -1)
D2: ±(1, -1, 1)
D3: ±(1, -1, -1)
```

For `R ∈ G` and a vertex `v` on one of these diagonals, the image `R v` is
again a vertex and lies on exactly one of `D0, D1, D2, D3`. The resulting
relabeling is a map `φ: G → S_4`.

**Theorem.** `φ` is a group isomorphism.

The proof is the four-step argument below: `|G| = 24`, `φ` is a
homomorphism, `ker φ = {I}`, and `|G| = |S_4|` then forces bijectivity.
The isomorphism is constructed by this action. It is not inferred from a
leftover character, and it does not use a classification of order-24
subgroups of `SO(3)`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer enumeration and the space-diagonal action construct an isomorphism of the det=+1 signed permutation group with S_4."
trace_class: frontier_discovery
target_claim_id: cube_rotations_s4_diagonals
target_blocker_text: "construct the isomorphism of the proper cube rotation group with S_4 by the space-diagonal action"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed 3x3 det=+1 signed permutation group and the four listed space diagonals"
hypothetical_axiom_status: "not proposed"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence below names proper
  cubic rotations as part of the site geometry. It is quoted without rewrite.
  The live Qubit sentence is quoted without rewrite so that the one-site
  algebra remains `M_2(C)`.
- **Explicit theorem-domain condition:** `G` is the displayed matrix group,
  and the four space diagonals are the listed pairs of opposite vertices of
  the cube `(±1, ±1, ±1)`. These are supplied mathematical data for the
  theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** no claim is made that Record or Admissibility
  selects this labeling, and `φ` is not proposed as axiom content.

## Exact Objects

All runner coefficients are integers in `Z`. No float is used.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Qubit sentence, quoted and not rewritten:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

A general element of `G` is written `R e_j = s_j e_{π(j)}` with
`π ∈ S_3` and `s_j ∈ {+1, −1}`. Then

```text
det(R) = sign(π) · s_0 s_1 s_2.
```

Membership in `G` is the condition `det(R) = +1`. The identity is `I`,
and matrix multiplication is the group law.

The four representative vertices are

```text
v0 = (1, 1, 1),   v1 = (1, 1, -1),   v2 = (1, -1, 1),   v3 = (1, -1, -1).
```

If `w` is any vertex, exactly one of `w` and `−w` equals some `v_i`, and
that index is the diagonal label of `w`. Define `φ(R) ∈ S_4` by

```text
φ(R)(i) = the diagonal label of R v_i.
```

Composition in `S_4` is written on the left: `(σ ∘ τ)(i) = σ(τ(i))`.

Two matrices that generate `G` are used as a check pair:

```text
A = 90° about the x-axis:   e0 ↦ e0,  e1 ↦ e2,  e2 ↦ −e1,
B = 120° about (1, 1, 1):   e0 ↦ e1 ↦ e2 ↦ e0.
```

## Exact Target And Proof Obligations

The exact target is to prove that `φ: G → S_4` is an isomorphism.

The obligation graph is:

1. `|G| = 24` by the signed-permutation count;
2. `φ` is a homomorphism because matrix product is composition of
   diagonal permutations;
3. `ker φ = {I}` by the on-diagonal sign analysis and by enumeration;
4. `|G| = |S_4|` and injectivity give bijectivity.

All four obligations are closed below and in the runner. The host is the
displayed matrix group on `R^3`. Other linear groups, improper isometries,
and any map out of `M_2(C)` are outside this theorem.

## Theorem 1 — `|G| = 24`

There are `3! = 6` choices of the axis permutation `π` and `2^3 = 8` sign
patterns `(s_0, s_1, s_2)`. The determinant condition
`sign(π) · s_0 s_1 s_2 = +1` holds for exactly half of the sign patterns
at each `π`, hence for `4` patterns per permutation. Therefore

```text
|G| = 6 × 4 = 24.
```

The companion runner enumerates the same set by constructing each matrix
and retaining those with `det = +1`, and it enumerates `S_4` as the
`4!` permutations of `{0, 1, 2, 3}`. Both counts equal `24`. Every
retained matrix satisfies `R^T R = I`.

The matrix `−I` has determinant `−1`, so `−I ∉ G`.

## Theorem 2 — `φ` is a homomorphism

The eight vertices partition into the four listed diagonals, two vertices
per diagonal. Each `R ∈ G` permutes the vertex set, and `R(−v) = −R v`,
so `R` sends opposite vertices to opposite vertices and therefore permutes
the four diagonals. Thus `φ(R)` is well-defined as an element of `S_4`.

For `R, S ∈ G` and each representative `v_i`,

```text
(RS) v_i = R (S v_i).
```

The vector `S v_i` lies on diagonal `φ(S)(i)`, and `R` sends that diagonal
to diagonal `φ(R)(φ(S)(i))`. Hence

```text
φ(RS) = φ(R) ∘ φ(S).
```

The runner checks this identity on the generating pair `A, B` and on every
pair in `G`. It also checks that `A` and `B` lie in `G`, that they have
orders `4` and `3`, and that they generate all of `G`.

## Theorem 3 — `ker φ = {I}`

Suppose `φ(R)` is the identity. Then `R` preserves each diagonal setwise,
so `R` acts as `±1` on each of the four lines `R v_i`. Write
`R v_i = ε_i v_i` with `ε_i ∈ {+1, −1}`.

The linear relations among the representatives force the four signs to
agree. In particular

```text
v0 + v3 = (2, 0, 0) = 2 e_0,
```

so

```text
R e_0 = (ε_0 v0 + ε_3 v3)/2
      = ((ε_0 + ε_3)/2, (ε_0 − ε_3)/2, (ε_0 − ε_3)/2).
```

This vector has entries in `Z` and is a signed basis vector only if
`ε_0 = ε_3`. The companion pairings `v1 + v2 = 2 e_0`,
`v0 + v2 = 2 e_1`, and `v0 + v1 = 2 e_2` likewise force
`ε_0 = ε_1 = ε_2 = ε_3`. Therefore `R = I` or `R = −I`.

The second option is unavailable: `det(−I) = −1`, so `−I ∉ G`. Hence
`R = I`.

The runner confirms the same conclusion by evaluating `φ` on all `24`
elements: the identity permutation occurs only at `I`.

## Theorem 4 — `φ` is an isomorphism

A homomorphism from a finite group of order `24` into `S_4`, which also
has order `24`, is bijective as soon as it is injective. Theorem 3 gives
injectivity, so `φ` is an isomorphism.

Equivalently, the runner computes that the image of `φ` contains `24`
distinct permutations.

## Physical-Interpretation Boundary

The proved output is the constructed isomorphism `φ: G → S_4`. This note
does not change the one-site Qubit statement. Qubit remains `M_2(C)`.
The map `φ` is displayed rotation-group data, not axiom content, and no
additional axiom is proposed. In particular there is no Aut(`M_2`)
adoption: `φ` is not an automorphism of the one-site algebra and is not
installed as one.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `−I` is a signed permutation but has `det = −1`, so it is not in `G`
   and is not a kernel candidate;
2. a non-identity element of `G`, such as the order-`4` generator `A`,
   moves at least one space diagonal;
3. the image of `φ` is not a proper subset of `S_4`: it has `24`
   elements.

## What This Does Not Claim

- No Aut(`M_2`) adoption.
- No axiom text is added or rewritten.
- No inverse-square law is used or derived.
- Qubit remains `M_2(C)`.
- `φ` is not a physical naming convention for sites, records, or menus.
- No classification of subgroups of `SO(3)` is used or asserted.
- Independent leftover characters are not used as parents.

These are scope boundaries, not impossibility claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Their dependency role is limited to the repository's name for proper cubic
rotations and to the unchanged one-site algebra. This theorem separately
supplies the matrix group `G`, the four space diagonals, and the map `φ`.

## Runner Contract

The companion runner enumerates `G` over `Z`, checks the
`sign(π) · ∏ s_j = +1` count, constructs `φ` from the four listed
representatives, checks multiplicativity on the generating pair `A, B` and
on all pairs, checks that the kernel is `{I}`, and checks that the image
has size `24`. It also quotes the live Lattice and Qubit sentences, rejects
the dispatch-forbidden substrings, prints substantive N5 scope
certificates, and records the import boundary. Declared review inputs are
this note and the axiom memo only.
