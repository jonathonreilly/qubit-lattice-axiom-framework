---
claim_id: s4_standard_3_only_so3_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Let G be the group of 3x3 signed permutation matrices of determinant +1, and let φ:G→S_4 be the action on the four space-diagonal lines of the cube. The standard inclusion G⊂SO(3) is the standard 3 of S_4. The twisted assignment 3'(R):=sgn(φ(R)) R sends a displayed 90° axis rotation to a matrix of determinant −1, so 3' is not a homomorphism G→SO(3). Only 3, not 3'=3⊗sgn, lands in SO(3)."
upstream_dependencies:
  - minimal_axioms
runner: scripts/s4_standard_3_only_so3_2026_08_14.py
---

# Only The Standard `3` Of `S_4` Lands In `SO(3)`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer-and-rational matrix identities for one displayed
rotation group `G` and the two three-dimensional irreps of `S_4`. The
target group is named `SO(3)` by the identification `Aut(M_2) ≅ SO(3)`;
that identification is a name for the target only. No physical inclusion
rule and no Qubit rewrite are asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/s4_standard_3_only_so3_2026_08_14.py`](../scripts/s4_standard_3_only_so3_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `G` be the group of `3 × 3` signed permutation matrices with
determinant `+1`. Label the four space-diagonal lines of the cube by the
representatives

```text
ℓ0 = (1, 1, 1),   ℓ1 = (1, 1, −1),
ℓ2 = (1, −1, 1),  ℓ3 = (1, −1, −1).
```

Opposite signs determine the same line. The action of `G` on these four
lines is a homomorphism `φ: G → S_4`. The standard inclusion
`G ⊂ SO(3)` is the standard three-dimensional irrep `3` of `S_4`. The
other three-dimensional irrep is the twist `3' = 3 ⊗ sgn`, realized on
the same matrices by

```text
3'(R) := sgn(φ(R)) R.
```

Take the displayed `90°` rotation about the first coordinate axis,

```text
R (x, y, z) = (x, −z, y).
```

Then `det R = +1`, so `R ∈ G`. The images of the four representatives are

```text
R ℓ0 = (1, −1, 1) = ℓ2,
R ℓ1 = (1,  1, 1) = ℓ0,
R ℓ2 = (1, −1,−1) = ℓ3,
R ℓ3 = (1,  1,−1) = ℓ1.
```

Thus `φ(R)` is the four-cycle `(0 2 3 1)`. A four-cycle is an odd
permutation, so `sgn(φ(R)) = −1`. The twist therefore returns

```text
3'(R) = −R,    det(−R) = (−1)^3 det R = −1.
```

Hence `−R` does not lie in `SO(3)`, and the assignment
`R ↦ sgn(φ(R)) R` is not a homomorphism `G → SO(3)`. The standard
inclusion already lands in `SO(3)`. Therefore only `3`, not `3'`, lands
in `SO(3)`.

The symbol `SO(3)` is the name of the target via `Aut(M_2) ≅ SO(3)`.
This note does not rewrite the Qubit sentence and does not treat the
matrix inclusion as a Lattice map.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact determinant and permutation-sign identities on one displayed rotation show that 3' leaves SO(3) while the standard inclusion remains in SO(3)."
trace_class: uniqueness_repair
target_claim_id: s4_standard_3_only_so3
target_blocker_text: "whether both three-dimensional irreps of S_4 land in SO(3)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed group G of 3x3 signed permutation matrices of determinant +1 and the displayed line action φ; no physical map is asserted"
hypothetical_axiom_status: "none; G and φ are displayed matrix data and are not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice and Qubit sentences below
  supply the repository's site lattice and one-site `M_2(C)` vocabulary.
  They are quoted without rewrite.
- **Name of the target:** `Aut(M_2) ≅ SO(3)` is used only as a name for
  the target group of the two candidate homomorphisms. It is not a
  derivation of the inclusion `G ⊂ SO(3)`.
- **Explicit theorem-domain condition:** `G`, the four space-diagonal
  lines, and the displayed axis rotation `R` are supplied mathematical
  data. This note does not claim that the axioms derive a physical
  rotation law.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** any physical reading of `G` as a site
  symmetry, and any identification of `3` with a physical frame law,
  remain separate obligations outside the target proved here.

## Exact Objects

All runner coefficients are exact integers in `Q`. No float is used.

A `3 × 3` matrix is a signed permutation matrix when each row and each
column contains exactly one nonzero entry and that entry is `±1`. The
group `G` is the subset of those matrices with determinant `+1`.

The four lines are undirected. The representative of a nonzero vector
`v` is obtained by flipping the global sign so that the first nonzero
coordinate is positive. On the four displayed vectors this returns the
same list.

The displayed witness is

```text
R = ((1, 0, 0), (0, 0, −1), (0, 1, 0)).
```

An even companion, used only as a consistency check, is the `120°`
rotation about `ℓ0`,

```text
S (x, y, z) = (z, x, y),
S = ((0, 0, 1), (1, 0, 0), (0, 1, 0)).
```

## Exact Target And Proof Obligations

The exact target is to show that the twist `3'` is not a homomorphism
into `SO(3)`, while the standard inclusion is the standard `3` and does
land in `SO(3)`.

The obligation graph is:

1. `R` is a signed permutation matrix of determinant `+1`, hence lies in
   `G` and in `SO(3)`;
2. the action of `R` on the four lines is a four-cycle;
3. a four-cycle is odd, so `sgn(φ(R)) = −1`;
4. `3'(R) = −R` has determinant `−1`, so `3'(R) ∉ SO(3)`;
5. therefore `3'` is not a homomorphism `G → SO(3)`, and only the
   standard `3` lands in `SO(3)`.

A separate even check on `S` is not required for the obstruction: `S`
is a three-cycle on the lines, hence even, and `3'(S) = S`.

There is no missing lemma for this bounded algebraic target.

## Theorem 1 — the displayed `R` lies in `G` and in `SO(3)`

Direct expansion gives `det R = +1`. Each row and each column of `R`
has a single nonzero entry `±1`, so `R` is a signed permutation matrix.
Thus `R ∈ G`. The same determinant identity places `R` in `SO(3)`.

## Theorem 2 — `φ(R)` is an odd four-cycle

Applying `R` to the four representatives yields the images listed in
the result section. The resulting permutation of `{0,1,2,3}` is the
single four-cycle `(0 2 3 1)`. A `k`-cycle is a product of `k−1`
transpositions, so a four-cycle is odd and `sgn(φ(R)) = −1`.

## Theorem 3 — `3'` leaves `SO(3)` on this witness

By definition `3'(R) = sgn(φ(R)) R = −R`. For any `3 × 3` matrix,
`det(−R) = (−1)^3 det R`. Substituting the value from Theorem 1 gives
`det(−R) = −1`. An element of `SO(3)` must have determinant `+1`, so
`−R ∉ SO(3)`.

A homomorphism into `SO(3)` cannot send an element of `G` outside
`SO(3)`. Therefore the assignment `R ↦ sgn(φ(R)) R` is not a
homomorphism `G → SO(3)`.

## Theorem 4 — only the standard `3` lands in `SO(3)`

The standard inclusion is the identity map on matrices: it sends `R` to
`R`, which Theorem 1 already places in `SO(3)`. That inclusion is the
standard `3`. The remaining three-dimensional irrep of `S_4` is the
twist `3' = 3 ⊗ sgn`. Theorem 3 shows that this twist does not land in
`SO(3)`. Hence only `3`, not `3'`, lands in `SO(3)`.

## Theorem 5 — even companion on a vertex rotation

The companion `S` has `det S = +1` and is a signed permutation matrix,
so `S ∈ G`. Its action on the four lines is

```text
S ℓ0 = ℓ0,
S ℓ1 = (1, −1, −1) = ℓ3,
S ℓ2 = (1,  1, −1) = ℓ1,
S ℓ3 = (1, −1,  1) = ℓ2,
```

the three-cycle `(1 3 2)` with `ℓ0` fixed. A three-cycle is even, so
`sgn(φ(S)) = +1` and `3'(S) = S`. On this even element the two irreps
agree, as required by the twist formula. The obstruction of Theorem 3
is confined to odd elements of `S_4`.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `det R` is `+1`, not `−1`;
2. `φ(R)` is a four-cycle, not a three-cycle, so its sign is `−1`;
3. `det(−R)` is `−1`, not `+1`.

## What This Does Not Claim

- The axioms are not edited. The displayed Lattice and Qubit wording is
  the current wording.
- The Qubit sentence is not rewritten.
- `Aut(M_2) ≅ SO(3)` is only a name for the target group.
- The matrix inclusion `G ⊂ SO(3)` is displayed data, not a Lattice map.
- No physical frame law, site-symmetry identification, or Record
  reading is asserted.
- Other hosts, other generating sets, and maps out of `O(3)` are
  outside this theorem.
- The even companion `S` is a consistency check, not an independent
  obstruction.

These are scope boundaries, not route-exhaustion claims.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Their dependency role is limited to the repository's lattice vocabulary
and one-site algebra name. This theorem separately supplies `G`, `φ`,
and the two candidate maps into the group named `SO(3)`.

## Runner Contract

The companion runner checks Theorems 1–5 with exact rational
arithmetic. It recomputes `det R`, the line permutation `φ(R)`, the
sign of that permutation, and `det(−R)` from the matrices. It also
checks the even companion `S`, quotes the live Lattice and Qubit
sentences, and records the import boundary. Declared review inputs are
this note and the axiom memo only.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | Of the two three-dimensional irreps of `S_4`, only the standard `3` can land in `SO(3)`. |
| V2 | New content? | Yes: the explicit four-cycle witness, the determinant identity `det(−R)=−1`, and the resulting exclusion of `3'`. |
| V3 | Independently checkable? | Yes. The runner recomputes the determinant, the line action, and the permutation sign from the displayed matrices. |
| V4 | More than a restatement? | Yes. Naming the two irreps does not by itself exhibit an odd element sent to determinant `−1`. |
| V5 | One-step relabel? | No. The sign twist is a different map from the standard inclusion; the witness distinguishes them. |

## Negative-Claim Scope Check

The only negative sentence is that `3'` is not a homomorphism into
`SO(3)`. No other representation of `S_4`, and no map into `O(3)`, is
excluded. No physical uniqueness claim is made.
