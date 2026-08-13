---
claim_id: two_site_swap_corner_hosts_m3_with_unit_p_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The two-site swap F on T_2 ≅ M_4(C) is Hermitian of square I_4 and trace 2. The projector p=(I_4+F)/2 has rank 3 and is not I_4. The corner C=p M_4 p is a unital *-algebra with unit p, complex dimension 9, and is *-isomorphic to M_3(C) via the matrix units of an orthonormal basis of im(p), with ψ(I_3)=p. The inclusion C ↪ M_4 is not unital. The result does not install SU(3), does not name QCD, does not rewrite Qubit, and does not select color."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_site_swap_corner_hosts_m3_with_unit_p_2026_08_13.py
---

# Two-Site SWAP Corner Hosts `M_3` With Unit `p`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact two-site tensor algebra `T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)`
and the rank-3 corner of the displayed two-site swap projector.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_site_swap_corner_hosts_m3_with_unit_p_2026_08_13.py`](../scripts/two_site_swap_corner_hosts_m3_with_unit_p_2026_08_13.py)

Parents on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The Qubit axiom supplies one site with possibility algebra `M_2(C)`. The
two-site tensor leftover is `T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)`. In the product
basis `|00>`, `|01>`, `|10>`, `|11>` the swap operator `F` is the displayed
permutation matrix below. Its `+1` spectral projection `p = (I_4 + F)/2` is
an orthogonal rank-3 projector, not `I_4`. The corner

`C = p T_2 p = p M_4(C) p`

is a unital `*`-algebra with unit `p`, not `I_4`. It is `*`-isomorphic to
`M_3(C)` by the matrix units of an orthonormal basis of `im(p)`, and
`ψ(I_3) = p`.

This is a corner host. It is not a unital `M_3` factor of `T_2`, not an
installation of `SU(3)`, not a naming of QCD, not a Qubit rewrite to `M_3`,
and not a selection of color.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The swap projector and its rank-3 corner are proved by exact integer/Fraction matrix identities; a *-isomorphism onto M_3(C) with unit p is exhibited on an orthonormal basis of im(p). Unital factorhood in T_2, SU(3), QCD, Qubit rewrite, and color-axiom adoption remain outside the claim."
trace_class: type_split
target_claim_id: two_site_swap_corner_hosts_m3_with_unit_p
target_blocker_text: "does a two-site SWAP projector host an M_3 with unit p rather than I_4?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed two-site swap on T_2 ≅ M_4(C); other embeddings, other projectors, and unital M_3 factors of T_2 remain separate"
hypothetical_axiom_status: "color-as-corner leftover: p M_4 p ≅ M_3 with unit p; not adopted as QCD"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The current Qubit axiom names the full one-site possibility domain with
algebraic presentation `M_2(C)`. Write

`T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)`

for the two-site tensor leftover. Identify `T_2` with `4 × 4` matrices in the
product basis `|00>`, `|01>`, `|10>`, `|11>`. The two-site swap is the
permutation matrix

```
F = [[1, 0, 0, 0],
     [0, 0, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1]]
```

Define `p = (I_4 + F)/2`. Explicitly

```
p = [[1,   0,   0, 0],
     [0, 1/2, 1/2, 0],
     [0, 1/2, 1/2, 0],
     [0,   0,   0, 1]]
```

The corner is `C = p M_4(C) p`. Write `{E_{ij}}_{1 ≤ i,j ≤ 3}` for the
standard matrix units of `M_3(C)`, and write `I_3` (resp. `I_4`) for the
unit of `M_3(C)` (resp. `M_4(C)`). An orthonormal basis of `im(p)` is

`|e_1> = |00>`, `|e_2> = (|01> + |10>)/√2`, `|e_3> = |11>`.

The displayed `*`-isomorphism is `ψ : M_3(C) → C`, `ψ(E_{ij}) = |e_i><e_j>`.

No axiom is edited. The matrices `F` and `p` are displayed mathematical test
objects, not a proposed Qubit rewrite and not a registered primitive.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the two-site swap projector hosts a copy of
`M_3(C)` whose unit is `p`, and whether that copy is a unital factor of
`T_2`.

| Obligation | Role | Disposition |
|---|---|---|
| `F` Hermitian, `F^2 = I_4`, `Tr(F) = 2` | Theorem 1 | proved; runner checks |
| eigenvalues of `F` are `+1` (mult. 3) and `−1` (mult. 1) | Theorem 1 | proved as ranks of `p` and `I_4 − p` |
| `p` orthogonal projection, rank 3, `p ≠ I_4` | Theorem 2 | proved; runner checks the displayed matrix |
| `C = p M_4 p` unital `*`-algebra with unit `p`, `dim_C C = 9` | Theorem 3 | proved |
| `ψ : M_3(C) → C` a `*`-isomorphism with `ψ(I_3) = p` | Theorem 3 | exhibited on the ON basis of `im(p)` |
| inclusion `C ↪ M_4` unital | Theorem 4 | fails; `p ≠ I_4` |
| install `SU(3)`, name QCD, rewrite Qubit, select color | out of scope | not claimed |

## Theorem 1 — The two-site swap

`F` is Hermitian, `F^2 = I_4`, and `Tr(F) = 2`. The eigenvalues of `F` are
`+1` with multiplicity 3 (symmetric subspace) and `−1` with multiplicity 1
(antisymmetric subspace).

Proof. `F` is real symmetric, so `F* = F`. Direct multiplication of the
displayed matrix gives `F^2 = I_4`. The diagonal of `F` is `(1,0,0,1)`, so
the trace is `2`. The identity `F^2 = I_4` forces the minimal polynomial to
divide `x^2 − 1`, hence the only possible eigenvalues are `±1`. The `+1`
spectral projection is `p = (I_4 + F)/2` and the `−1` spectral projection is
`I_4 − p = (I_4 − F)/2`. Theorem 2 computes `rank(p) = 3` and
`rank(I_4 − p) = 1`, which are the geometric multiplicities.

## Theorem 2 — The swap projector

`p = (I_4 + F)/2` is an orthogonal projection: `p* = p = p^2`. It has
`rank(p) = 3` and `p ≠ I_4`. The displayed matrix in Exact Objects is this
`p`.

Proof. Hermiticity of `F` gives hermiticity of `p`. Then

`p^2 = (I_4 + 2F + F^2)/4 = (I_4 + 2F + I_4)/4 = (I_4 + F)/2 = p`.

The complementary projection `I_4 − p` is nonzero because `F ≠ I_4` (the
`(2,3)` entry of `F` is `1`). Hence `p ≠ I_4`. Exact rational row rank of
the displayed matrix is `3`. Equivalently, `im(p)` is spanned by the three
independent vectors `|00>`, `|01> + |10>`, `|11>`.

## Theorem 3 — The corner is `M_3` with unit `p`

The corner `C = p T_2 p = p M_4(C) p` is a unital `*`-algebra with unit `p`.
Its complex dimension is `rank(p)^2 = 9 = dim_C M_3(C)`.

The map `ψ : M_3(C) → C` defined on matrix units by
`ψ(E_{ij}) = |e_i><e_j|` is a `*`-isomorphism, and `ψ(I_3) = p`.

Proof. For any `X, Y ∈ M_4(C)`,

`(p X p)(p Y p) = p X p Y p ∈ C`, `(p X p)* = p X* p ∈ C`,

so `C` is a `*`-subalgebra of `M_4(C)`. The element `p = p I_4 p` lies in
`C`, and `p (p X p) = p X p = (p X p) p`, so `p` is the unit of `C`.

A rank-`k` orthogonal projection in `M_n(C)` has corner `p M_n p ≅ M_k(C)`
of dimension `k^2`. Here `k = 3`, so `dim_C C = 9`. The runner also computes
this dimension as the exact rational rank of the sixteen compressed matrix
units `{p E^{(4)}_{ab} p}_{1 ≤ a,b ≤ 4}`.

On the orthonormal basis `|e_1>`, `|e_2>`, `|e_3>` of `im(p)`, the operators
`|e_i><e_j|` satisfy the matrix-unit table

`|e_i><e_j| |e_k><e_l| = δ_{jk} |e_i><e_l|`, `(|e_i><e_j|)* = |e_j><e_i|`,

and each equals `p |e_i><e_j| p` because `p |e_i> = |e_i>`. Linear
independence of the nine units is the matrix-unit theorem. Therefore `ψ` is
a `*`-isomorphism onto `C`. The unit is

`ψ(I_3) = |e_1><e_1| + |e_2><e_2| + |e_3><e_3|`.

The first and third summands are the coordinate projectors onto `|00>` and
`|11>`. The middle summand is the Fraction matrix

```
|e_2><e_2| = [[0,   0,   0, 0],
              [0, 1/2, 1/2, 0],
              [0, 1/2, 1/2, 0],
              [0,   0,   0, 0]]
```

and the sum is the displayed `p`.

The same corner is available over `Q` without storing `√2`. The integer
spanning set `|w_1> = |00>`, `|w_2> = |01> + |10>`, `|w_3> = |11>` has Gram
matrix `G = diag(1, 2, 1)`. If `W` is the `4 × 3` matrix with those columns,
the map `φ(X) = W G^{-1} X W*` is a unital algebra isomorphism `M_3(C) → C`
given by integer and Fraction matrices, and `φ(I_3) = p`. The ON map `ψ` is
the `*`-isomorphism; it is `φ` transported along the diagonal rescaling that
sends `|w_2>` to `|e_2>`. The integer ket-bras `|w_i><w_j|` obey the matrix-
unit table with structure constants `<w_j|w_k>` and are closed under adjoint.
The runner checks `φ` as an algebra map, checks that table, and checks
`ψ(I_3) = p` by summing the three ON rank-1 projectors.

## Theorem 4 — The inclusion into `M_4` is not unital

The inclusion `C ↪ M_4(C)` is **not** unital: `p ≠ I_4`. So this is not a
unital `M_3` factor of `T_2`. It is a corner host whose unit is `p`.

The unit of `T_2` remains `I_2 ⊗ I_2 = I_4`. A unital algebra homomorphism
`M_3(C) → T_2` would have to send `I_3` to `I_4`. The displayed `ψ` sends
`I_3` to `p`, so it cannot be such a factor embedding. The obstruction to a
unital `M_3` factor of a finite qubit tensor is a separate hole; this note
does not adopt it and does not depend on it.

## Theorem 5 — Qubit is unchanged; color is not selected

Qubit still names one-site `M_2(C)`. This construction uses the two-site
tensor leftover and a displayed swap. It does not install `SU(3)`, does not
name QCD, does not flip Qubit to `M_3`, and does not select color.

The four axioms do not name a three-dimensional internal algebra. Hosting
`M_3(C)` as a corner of `T_2` with unit `p` is a type fact about a displayed
projector. It is not an axiom update and it is not adopted as QCD.

## Mutation

The predicate `p == I_4` must fail.
The predicate `rank(p) == 4` must fail.
The predicate `dim_C(C) == 9` must hold.

All three are runner-checked by constructing `p` from `F` and computing exact
rational ranks.

## No-Go Discipline Gate

The positive claim is only that the displayed swap projector hosts a corner
`p M_4 p ≅ M_3(C)` with unit `p`. The gate does not certify that color is
derived, that a unital `M_3` factor of `T_2` exists, or that Qubit should be
rewritten.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Displayed two-site swap `F` and `p = (I_4+F)/2` | compute involution, trace, rank, corner unit | Theorems 1–3: `p` rank 3, `C ≅ M_3` with unit `p` | **ATTEMPTED** |
| Opposite swap projector `(I_4−F)/2` | same tests on the antisymmetric line | rank 1; hosts `M_1`, not `M_3` | **ATTEMPTED** |
| Treat `C ↪ M_4` as a unital factor | require `ψ(I_3) = I_4` | fails; Theorem 4 | **ATTEMPTED** |
| Top-left pad `diag(X,0)` as the color algebra of `T_2` | unitality of that pad | independent hole; not used as a parent here | live |
| Install `SU(3)` from `M_3` matrix units | Lie algebra of traceless anti-Hermitians | not constructed and not adopted | live |
| Owner-approved primitive or retained derivation selecting color | governance, not this projector | not supplied by the current axioms or approved primitives | live |

The first three routes concern the displayed swap corner. The last three
remain possible or independent. Accordingly, the broad statement “color is
selected by the two-site swap” is not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `p ≠ I_4` / `rank(p) ≠ 4` | almost: a proper projection already has rank `< 4` once ranks are computed | almost: rank `3 ≠ 4` already implies `p ≠ I_4` | two readings of the same projection |
| corner `≅ M_3` / unital factor in `T_2` | no: a corner iso does not make `p = I_4` | no: failing unitality does not compute `dim C = 9` | independent type split |
| corner host / SU(3) installation | no: matrix units are not a Lie bracket selection | no: an `su(3)` basis would not change `p` | independent |
| corner host / QCD naming | no | no | independent; QCD is never used |
| corner host / Qubit rewrite | no: the current one-site wording is untouched | no: a rewrite would be a different object | independent |

The load-bearing positive wall is the rank-3 corner with unit `p`. Unital
factorhood, `SU(3)`, and QCD are not additional walls of this claim.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `T_2 = M_2 ⊗ M_2 ≅ M_4(C)` | standard finite-dimensional identification; dimension 16 is runner-checked |
| displayed swap `F` | explicit test matrix, not attributed to the axioms |
| `p = (I_4+F)/2` | spectral projection of that matrix |
| ON basis of `im(p)` | explicit; middle vector uses `√2` only as a label; runner identities are Fraction/integer |
| `*` | conjugate transpose on finite matrices |
| rank | exact rational row rank |
| “corner host” | unital `*`-algebra `p M_4 p` with unit `p` |
| “color algebra” | leftover name only; not a derived or selected object |
| `SU(3)`, QCD | named only to refuse installation and naming |
| observations or fitted constants | none |

No continuum limit, gauge connection, representation theory of `SU(3)`, or
empirical color quantum number is used.

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one-site possibility domain `M_2(C)`; further structure requires a retained derivation, bridge, or approved primitive | wording only; no composite or color conclusion is borrowed |

The swap identities, the projector, the corner dimension, and the
`*`-isomorphism are proved here and checked by the runner. No other
scientific parent is used.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | swap `F`, projector `p`, matrix units of `im(p)`, units `I_3` and `I_4` | no classification of every projector in `M_4` |
| per site | two-site tensor `T_2` only | no lattice-wide color field |
| per mode | the displayed swap and its `+1` corner | no spectral exhaustion of other involutions |
| per block | corner host with unit `p` | no QCD, no `SU(3)`, no axiom edit, no color selection |
| lattice-wide | not executed | no lattice-wide existence or no-go |

### N6 — live partial-closure paths

1. A unital embedding of `M_3(C)` into some other algebra is a separate
   question; for finite qubit tensors it is independently obstructed, but
   that obstruction is not adopted here.
2. A different involution or a different two-site operator could host a
   different corner; this note tests only the displayed swap.
3. A derived internal algebra could appear from Record/Admissibility
   structure rather than from a displayed swap.
4. An owner-approved primitive could register a three-dimensional internal
   algebra; none of the current approved primitives does so.
5. A Qubit rewrite that changes the one-site algebra is a governance act,
   not a consequence of this corner, and is not adopted.

Scale reference, kinetic isotropy, and realized state were checked in the
premise registry. None supplies a color algebra, and none is counted as an
extra wall.

### N7 — concrete-mechanism steelman

The strongest steelman of the corner is: treat `p M_4 p ≅ M_3` as “the color
block” of a two-site composite because it is unital for itself and has the
right dimension. That still fails as a selection of color, because the
two-site unit remains `I_4`, Qubit remains `M_2(C)`, and no axiom names the
swap as a color projector. Calling the corner “color” is a leftover name,
not an adopted axiom, and it is not adopted as QCD.

### N8 — cross-cycle echo

Historical color-selection and unital-factor notes reject other cheap
identifications, including the non-unital pad of `M_3` into `M_4`. This note
does not reuse those conclusions and does not take them as parents. It
recomputes only the displayed swap corner on `T_2` and refuses to import
QCD.

## FAIL / DO NOT SHIP

Do not ship any of the following from this note:

- “color is selected by the two-site swap”
- “the axioms derive QCD or `SU(3)`”
- “`M_3(C)` is a unital factor of `T_2`”
- “Qubit should be rewritten to `M_3`”
- “an axiom update is necessary”
- “this constructs the Standard Model color algebra”

The shipped claim is only: the displayed two-site swap projector hosts a
corner `p M_4 p ≅ M_3(C)` whose unit is `p`, not `I_4`.

## Provenance

Parent on `origin/main`: the axiom memo only. The runner binds

`AUDIT_INPUT_PATHS = (this note, docs/MINIMAL_AXIOMS_2026-06-29.md)`

as a string-literal tuple. No citation-manifest edit and no runner-cache
write are part of this surface.
