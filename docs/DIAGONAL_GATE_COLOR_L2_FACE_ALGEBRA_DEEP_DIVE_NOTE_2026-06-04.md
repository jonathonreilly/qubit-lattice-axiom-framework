---
claim_id: diagonal_gate_color_l2_face_algebra_deep_dive_note_2026-06-04
claim_type_author_hint: bounded_theorem
---

# Diagonal GATE-COLOR Deep Dive — Face-Diagonal Algebra on the Generation Triplet (L2)

**Date:** 2026-06-04
**Type:** bounded theorem (clean dimension + carrier-identity result with a
named residual)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note proposes a
source-note surface; it sets no audit status, predicts no audit outcome,
changes no axiom, and adopts no convention. Effective status is
pipeline-derived after independent review.
**Primary runner:** [`scripts/diagonal_gate_color_l2_face_algebra_deep_dive.py`](../scripts/diagonal_gate_color_l2_face_algebra_deep_dive.py)
(SUMMARY: PASS=35 FAIL=0).
**Cached log:** [`logs/runner-cache/diagonal_gate_color_l2_face_algebra_deep_dive.txt`](../logs/runner-cache/diagonal_gate_color_l2_face_algebra_deep_dive.txt)

> Phase 4 of the √2-centered diagonal-connection build. Deepens scout **S2**
> (color) of the foundation
> [`DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md).
> The foundation noted that face-diagonal pair-connections on the
> 3-generation factor `C^3` generate `u(3) = su(3) + u(1)`, with the caveat
> that the runner's `su(3)`-dimension check was a "coarse proxy." This note
> (a) makes the dimension result rigorous, and (b) answers the honest
> question the scout left open: **does that `su(3)` act as physical COLOR,
> or only as a generation-space rotation?**

## §0. Honest scoping

This note packages a finite linear-algebra result on `C^8 = (C^2)^{⊗3}` and
its hw=1 generation subspace `C^3`. It is `bounded_theorem`, not
`positive_theorem`, because:

- the **L2 face-diagonal adjacency convention** (treating each face-diagonal
  link as an *independent* qubit-link connection carrying its own `u(2)`) is
  an **input** inherited from the foundation scoping note, not an axiom and
  not derived here; and
- the **color/generation identification** that the result turns on is an
  **already-recorded open gate** of the framework, not closed here.

The note adds no axiom, no fitted selector, no PDG comparator, no unit
convention, and no import. It does not modify
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md).

The single sentence to carry downstream:

> Face-diagonal adjacency genuinely lifts a **real** nearest-neighbor
> obstruction — it turns the `u(1)^3` diagonal commutant on the generation
> triplet into the full `u(3) = su(3) + u(1)` — but the resulting `su(3)`
> acts on the **generation** carrier, which is a *different* subspace of `C^8`
> than the framework's symmetric-base **color** carrier, and the two carry
> *different* `Z_3` characters. The dimension matches; the identification does
> not. **GATE-COLOR is PARTIAL, not closed.**

## §1. Setup and the two candidate 3-spaces

The chiral cube is `C^8 = (C^2)^{⊗3}` with computational basis
`|b_1 b_2 b_3⟩`, `n = 4 b_1 + 2 b_2 + b_3`. Two distinct 3-dimensional
subspaces are relevant.

- **The hw=1 GENERATION carrier** `V_gen = span{|100⟩, |010⟩, |001⟩}`. This is
  the Hamming-weight-1 BZ-corner orbit. The retained
  [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  (`three_generation_observable_theorem_note`, `retained`)
  proves the lattice translations plus the induced `C3[111]` corner-cycle
  generate the full `M_3(C)` on `V_gen` irreducibly. Per
  [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  the three sites are the `S_3`-orbit `L_1`.

- **The symmetric-base COLOR carrier** `V_col`. The retained
  [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  (`cl3_color_automorphism_theorem`, `retained`, audited_clean) embeds the
  algebraic `SU(3)` on the **3D symmetric base subspace** of the
  `(b_1,b_2)`-base ⊗ `b_3`-fiber decomposition:
  `span{|00⟩, |11⟩, (|01⟩+|10⟩)/√2}` (the symmetric block of the 4D
  `(b_1,b_2)`-base), tensored with a fixed `b_3`-fiber. The explicit
  Gell-Mann embedding is packaged in
  [`CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md).

Both notes carry the **same explicit deferral**: identifying their 3-space
with the physical SM carrier (generations / `SU(3)_c`) is "a separate
retained-bridge requirement, not part of this theorem's load-bearing scope."

## §2. The nearest-neighbor obstruction is REAL (Part A)

On `V_gen` the three generation sites are mutually **face-diagonal**: every
pair `{e_i, e_j}` has squared Euclidean distance `2`, and **none** is a
nearest neighbor (`dist^2 = 1`). (This is scout **S1**.) Consequently the
NN-only connection convention supplies **zero** off-diagonal pair-generators
on the triplet: with no adjacent pair, the only connection generators are the
per-site phases the convention already carries on each fiber. The resulting
connection algebra on `V_gen` is the **diagonal commutant**

```text
u(1)^3   (real dimension 3),
```

which is abelian and **strictly smaller** than `u(3)` (real dimension 9).

This is the precise mechanism behind the color-obstruction statement of
[`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md):
you cannot build the three pair-generators of `u(3)` while the three pairs are
non-adjacent. (That note states the boundary on a *single* qubit fiber — real
endomorphism dimension 4, traceless Hermitian dimension 3 — which is the same
"no native `su(3)` from NN structure" fact viewed locally.)

> **Lemma A (NN obstruction).** The NN-connection algebra on the hw=1
> generation triplet is `u(1)^3`, of real dimension `3 < 9 = dim u(3)`. (Runner
> Part A, checks A1–A5.)

## §3. The face-diagonal closure to u(3), made rigorous (Parts B, C)

Under the L2 convention each face-diagonal link is an independent qubit-link
connection carrying its own `u(2)`. With face-diagonals all three generation
pairs are adjacent, so all three pair-`u(2)`s are present. Their real Lie
closure is

```text
u(3) = su(3) ⊕ u(1)   (real dimension 9 = 8 + 1).
```

**Repair of the foundation's "coarse proxy."** The foundation runner counted
trace-free vectors of an *orthonormalized* basis to gauge the `su(3)` part and
flagged this as coarse (Gram–Schmidt mixes the central `iI` direction into
off-diagonal vectors, so the trace-free count of an arbitrary orthonormal
basis is not basis-independent). The reliable statement is the
algebra-dimension split: the central phase `iI` lies in the algebra (verified
directly), so

```text
dim su(3) = dim u(3) − dim u(1) = 9 − 1 = 8,
```

and `su(3) ⊕ u(1)` is a genuine **Lie-algebra direct sum** because `iI` is
central (commutes with the whole algebra). (Runner Part B, checks B1–B5.)

**Certification that the traceless part is `su(3)`** (not merely 8-dimensional):
the canonical Gell-Mann generators satisfy real, totally antisymmetric
structure constants `[T^a, T^b] = i f^{abc} T^c`; the Killing form is
negative-definite and proportional to the identity (compact, simple); the
rank is `2` (`T^3, T^8` span the Cartan); and every `su(3)` generator lies in
the real span of the face-diagonal generators (the two 8-dimensional spaces
coincide, both equalling all traceless anti-Hermitian `3×3` matrices). (Runner
Part C, checks C1–C7.)

> **Lemma B (face-diagonal closure).** The face-diagonal connection algebra on
> the generation triplet is `u(3) = su(3) ⊕ u(1)`, real dimension `9`, with the
> traceless part a compact simple `su(3)` of rank 2.

So the **mechanism is non-trivial in the framework sense**: it is exactly the
structural change (NN → face-diagonal adjacency) that lifts a real obstruction
identified by a retained note. The "pairwise `u(2)` generates `u(N)`"
mathematics is standard; the framework content is that the *foundation
geometry decides whether the three pairs are adjacent*, and only the diagonal
extension makes them so.

## §4. Generation vs color — the deep question (Part D)

The `u(3)` of §3 acts on `V_gen`. Physical color `SU(3)_c` acts on a 3-dim
**color** space. Are these the same 3, or different? Three exact facts answer
this, and all three say **different**.

**(D1) The carriers are different subspaces of `C^8`.** With `V_gen` and
`V_col` as in §1, `rank[V_gen | V_col] = 5`, so

```text
dim(V_gen ∩ V_col) = 3 + 3 − 5 = 1.
```

They are **not** the same 3-space. The single shared direction is precisely
the hw=1 symmetric vector `(|100⟩+|010⟩)/√2` (it lies in both the generation
span and the symmetric base); every other generation direction (e.g. `|001⟩`)
lies outside `V_col`. (Runner Part D, checks D1, D1b, D4, D4b.)

**(D2) The `Z_3` characters differ.** The generation cyclic action is the
axis-cycle permutation `c: e_1 → e_2 → e_3 → e_1`, whose character on `C^3` is
the **regular** character `(3, 0, 0)`. The `Z_3` *center* of `SU(3)_c` acts on
the color fundamental by scalar `ω = e^{2πi/3}`, with character
`(3, 3ω, 3ω^2)`. These are **distinct**, so the color center is **not** the
bridge — exactly the durable content of the retained-graph open gate
[`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md`](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md).
(Runner Part D, checks D2, D2b, D2c.)

**(D3) Isomorphism requires imposing a common action.** If one *imposes* the
same cyclic label on both 3-spaces, they become isomorphic as `Z_3`
representations (both are the regular rep). But the color carrier does **not**
natively carry the generation permutation as its `SU(3)_c` center action — the
native center character `(3, 3ω, 3ω^2)` differs from `(3, 0, 0)`. So the common
action is an **extra bridge assumption**, which is the open gate, not a
consequence of face-diagonal adjacency. (Runner Part D, checks D3, D3b.)

**(D5) A `u(1)` is silently discarded.** The face-diagonal algebra is the
*reducible* `u(3) = su(3) ⊕ u(1)`. Reading "the `su(3)`" as color discards the
central `u(1)` factor — itself a choice the geometry does not make for you.
(Runner Part D, check D5.)

> **Lemma D (carrier mismatch).** The face-diagonal `su(3)` acts on `V_gen`,
> which meets the framework's color carrier `V_col` in a single dimension and
> carries a `Z_3` character `(3,0,0)` distinct from the `SU(3)_c` center
> character `(3,3ω,3ω^2)`. Identifying the face-diagonal `su(3)` with physical
> color is the **already-open** color/generation gate.

## §5. Body-diagonals add no fourth generation (Part E)

The unit cube has **4 body-diagonals** (`dist^2 = 3`), each joining opposite
corners whose Hamming weights sum to `3`. Hence body-diagonals connect
`hw=0 ↔ hw=3` and `hw=1 ↔ hw=2`; **no** body-diagonal connects two hw=1 sites.
Restricted to `V_gen` the body-diagonal connection content is therefore
**empty**: body-diagonals add no off-diagonal generator within the generation
triplet, create **no fourth generation**, and leave the `u(3)` of §3
unchanged. The three hw=1 body-diagonal links point to the `hw=2` orbit — the
charge-conjugate (`c(L_1) = L_2`) generation orbit per substep 3 — i.e. a
distinct sector, not a widening of the triplet. (Runner Part E, checks E1–E4.)

> **Lemma E (body-diagonal inertness on hw=1).** No body-diagonal connects two
> hw=1 sites; body-diagonals act between `hw=1` and the `hw=2` C-conjugate
> orbit. The generation triplet and its `u(3)` are unaffected.

## §6. Verdict and residual

**Verdict: PARTIAL.** Face-diagonal adjacency does **not** by itself close
GATE-COLOR, and it is **not** a red herring. Precisely:

- **Not a red herring.** The `u(3)` is *not* trivial. It lifts a **real**
  NN obstruction (Lemma A): `u(1)^3` (dim 3) → `u(3)` (dim 9), with a
  certified compact simple `su(3)` (Lemmas B, C). The single structural change
  that the foundation proposes genuinely produces an `su(3)`-shaped algebra
  where NN structure produced none.

- **Not closed.** The `su(3)` acts on the **generation** carrier `V_gen`,
  which is a *different* subspace of `C^8` than the framework's symmetric-base
  **color** carrier `V_col` (intersection dimension 1), with a *different*
  `Z_3` character (Lemma D). The dimension match (`9 = dim u(3)`) is **not** a
  color identification.

- **What changed.** Face-diagonal adjacency **relocates** the color
  obstruction from "*no `su(3)` algebra at all on the generation triplet*"
  (the NN statement) to "*`su(3)` present on generation space, color
  identification still required*." That identification is the **named
  residual**: the still-open color/generation bridge recorded by
  `Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10`, and
  the explicit deferral shared by `CL3_COLOR_AUTOMORPHISM_THEOREM` and
  `CL3_TASTE_GENERATION_THEOREM`.

**Bounded-theorem statement (safe to carry downstream).**

> On `C^8 = (C^2)^{⊗3}`, the nearest-neighbor connection algebra on the hw=1
> generation triplet is `u(1)^3` (real dim 3), while the face-diagonal
> connection algebra (L2 convention) is `u(3) = su(3) ⊕ u(1)` (real dim 9),
> with the traceless part a compact simple `su(3)`. The face-diagonal `su(3)`
> acts on the generation carrier `V_gen`, which intersects the framework's
> symmetric-base color carrier `V_col` in dimension 1 and carries the `Z_3`
> character `(3,0,0)`, distinct from the `SU(3)_c` center character
> `(3,3ω,3ω^2)`. Body-diagonals connect `hw=1 ↔ hw=2` and add nothing within
> the triplet. Therefore face-diagonal adjacency lifts the real
> nearest-neighbor color obstruction on the generation triplet but does not
> identify the resulting `su(3)` with physical color `SU(3)_c`; that
> identification is the open color/generation gate.

### What this note does NOT claim

- It does **not** claim face-diagonal adjacency closes GATE-COLOR.
- It does **not** claim the generation triplet *is* the color triplet (the
  carriers differ; the `Z_3` characters differ).
- It does **not** modify any axiom, adopt the L2 convention, set or predict an
  audit status, promote any row, or weaken any retained no-go.
- It does **not** import a comparator or consume a PDG value. `√2`, the cube
  combinatorics, and the `Z_3` characters are lattice/group-theoretic data.

## §7. Cross-references

- [`DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md)
  — the foundation (scout S2 deepened here).
- [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
  — NN `u(2)` and the single-fiber color boundary (the "obstruction").
- [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  (`retained`) — the framework's symmetric-base color `SU(3)` carrier `V_col`.
- [`CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md)
  — explicit Gell-Mann embedding on `V_col`.
- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  (`retained`) — `M_3(C)` on the hw=1 generation carrier `V_gen`.
- [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  — hw=1 orbit `L_1`, charge-conjugation `c(L_1)=L_2`.
- [`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md`](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md)
  — the named residual: the open color/generation identification gate.
- [`CL3_TASTE_GENERATION_THEOREM.md`](CL3_TASTE_GENERATION_THEOREM.md)
  — generation-candidate framing and its deferral of physical identification.
- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) — the
  three-axiom baseline (untouched).
