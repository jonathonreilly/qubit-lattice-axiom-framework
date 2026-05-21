# Koide SELECTOR Dimension Ratio from Qubit Reframe: 2/3 = dim(qubit) / |Cl(3) generators|

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Closes (proposed):** one specific admission in the
"qubit-lattice-dim algebraic closure" (note 22) of
[`CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md`](CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md)
(`audited_conditional`, load_bearing_score 16.93). Specifically, this
note grounds the structural identity `2/3 = dim(qubit Hilbert) /
|Cl(3) generators|` in the retained narrow theorems now binding under
the qubit reframe of A1
([`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)).

## Honest scope

This note **does not** close `δ = 2/9 rad` (the radian-bridge has a
retained no-go via
`KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md`), and does
**not** close the full Koide chain. It closes **one specific scalar
admission** (the dimension-ratio underlying `SELECTOR^2 = 2/3`) in
the existing qubit-lattice-dim algebraic closure route, which is
itself one of multiple support routes for `Q = 2/3` and
(via `Q = d · δ`) the dimensionless layer of `δ = 2/9`.

If accepted, this strengthens the qubit-lattice-dim closure route by
removing one of its admitted scalar inputs, but does not by itself
promote the Koide chain to retained closure. Other gates remain
(radian bridge, U(1) hypercharge commutant via Grassmann gate, etc.).

## Claim

Under the qubit reframe of A1 ("a qubit at every site"; per-site
operator algebra is `M_2(ℂ) ≅ Cl(3,0)` as real algebras), the
structural identity

```text
SELECTOR² := dim(qubit Hilbert space) / |Cl(3,0) generators|             (1)
           = 2 / 3
```

is a **retained-grade dimensional ratio**, with both numerator and
denominator supported by retained content:

- **Numerator (`dim = 2`):** from the retained narrow theorem
  [`CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md)
  (positive_theorem, retained). The faithful complex irrep of
  `Cl(3,0)` is 2-dim, equivalently the qubit Hilbert space `ℂ²` of
  the M_2(ℂ) operator algebra.
- **Denominator (`|gens| = 3`):** from A1 itself. `Cl(3,0)` is the
  Clifford algebra over `ℝ³` with three generators
  `e_1, e_2, e_3` satisfying `e_i² = +𝟙` and
  `e_i e_j = -e_j e_i` for `i ≠ j`. The count of three generators is
  the defining content of `Cl(3,0)` (not `Cl(2,0)` or `Cl(4,0)`).

The ratio `2/3` is therefore the canonical dimension ratio of A1's
per-site operator algebra under the qubit identification, with `SELECTOR
= √(2/3) = √6/3` the associated scalar.

## Setup

By A1 (qubit form), the per-site operator algebra is `M_2(ℂ)`
acting on `ℂ²`. Under the equivalent `Cl(3,0)` real-algebra reading,
the same algebra is presented with three anticommuting self-adjoint
generators `e_1, e_2, e_3` of square `+𝟙`.

Two dimensions are canonically associated with this single algebra:

1. **Hilbert dimension**: `dim_ℂ(ℂ²) = 2` — the dimension of the
   faithful complex irrep of `M_2(ℂ)`.
2. **Clifford-generator count**: `|{e_1, e_2, e_3}| = 3` — the
   number of self-adjoint anticommuting generators of `Cl(3,0)`.

The ratio (1) is the **canonical dimension ratio** of A1's per-site
algebra. It is a structural property of the algebra, not a choice.

## Step 1 — Retained backbone for the numerator

The faithful complex irrep dimension `2` is the load-bearing content
of:

- [`CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained`, positive_theorem). Establishes that the faithful
  complex irreducible representation of `Cl(3,0)` is 2-dim.

Combined with:

- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained`, positive_theorem). Establishes `Cl(3,0) ⊗_ℝ ℂ ≅
  M_2(ℂ) ⊕ M_2(ℂ)`, with each summand carrying a 2-dim irrep.

These together identify the qubit Hilbert dimension `2` as
retained-grade content under the qubit reframe of A1.

## Step 2 — A1 backbone for the denominator

A1 (per `MINIMAL_AXIOMS_2026-05-20.md`) states the per-site operator
algebra is `M_2(ℂ)`, equivalently `Cl(3,0)` as a real algebra. The
real-algebra reading explicitly involves **three** generators
`e_1, e_2, e_3` — this is the defining content of the Clifford
algebra over `ℝ³`.

The number `3` is a primitive part of A1's canonical statement (it's
the "3" in `Cl(3,0)`). It is not derived from upstream content; it
is part of the axiom itself.

This is consistent with `cl3_per_site_uniqueness_theorem_note_2026-04-29`'s
narrowed U1-U3 portion (the physical-`Cl(3)`-only content), which
treats `Cl(3,0)` as the named local algebra with its standard
three-generator structure.

## Step 3 — The ratio as canonical structural identity

Combining Steps 1 and 2:

```text
SELECTOR² = dim(qubit Hilbert) / |Cl(3,0) generators|
          = 2 / 3                                                        (2)
```

This is a **canonical structural identity** of A1's per-site
algebra, not an admitted scalar. Both factors are anchored:
- `2` retained via the two narrow theorems
- `3` part of A1's defining content

The scalar `SELECTOR = √(2/3) = √6/3 ≈ 0.8165` is the canonical
"projection norm" from a `Cl(3,0)`-generator-indexed basis (3 elements)
to a qubit-Hilbert-indexed basis (2 elements), as appears in the
note 22 qubit-lattice-dim closure route.

## What this closes (in the existing Koide chain)

In `CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md` note 22 (the April 20
evening qubit-lattice-dim algebraic closure), the structural identity
`dim(Cl(3) spinor) / dim(Z^3 lattice) = 2/3` is invoked alongside
the A-select axiom `SELECTOR = √6/3` (`SELECTOR² = 2/3`).

Under the qubit reframe of A1, the dimension ratio is **no longer an
admitted scalar** — it is the canonical structural identity (2). The
`SELECTOR² = 2/3` axiom in note 22 is therefore grounded in retained
narrow-theorem content rather than admitted by hand.

This **closes one admission** in note 22's closure route. Other
admissions in note 22 (the U(1) hypercharge commutant bridge,
`|Y(d_R)| = 2/3` from anomaly cancellation depending on the
Grassmann gate, etc.) remain.

## What this does not close

- **`δ = 2/9 rad` (the radian bridge)**: retained no-go in
  `KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md` rules out
  the canonical R/Z → U(1) qubit lift. The qubit reframe does not
  break this no-go. The radian bridge requires substantive new
  derivation work outside this note's scope.
- **`Q = 2/3` full closure**: even with the SELECTOR ratio grounded,
  Q = 2/3 in note 22's chain still depends on the anomaly arithmetic
  `|Y(d_R)| = 2/3` (Grassmann-gate-dependent), the U(1) hypercharge
  commutant bridge, and the V8 OP-locality content (audit-pending).
- **`δ = 2/9` dimensionless layer closure** via `Q = d · δ`:
  arithmetically gives `δ = 2/9` once `Q = 2/3` is closed, but
  inherits Q's open admissions.
- **Charged-lepton mass scale `v_0`**: separate hierarchy input, out
  of Koide chain scope.

## Admitted inputs

1. **A1 canonical form (qubit reframe)**: `MINIMAL_AXIOMS_2026-05-20.md`
   A1 = "a qubit at every site" with per-site algebra
   `M_2(ℂ) ≅ Cl(3,0)`. Retained as the canonical axiom doc.
2. **Retained narrow theorems** for the dimension `2`:
   - `cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10`
   - `cl3_complexification_split_narrow_theorem_note_2026-05-10`
3. **The `Cl(3,0)` generator count `3`** as part of A1's defining
   content.

No external math imports are required — the dimension ratio is pure
linear algebra on the canonical A1 algebra.

## Risk classification

This is a `bounded_theorem` candidate with **very narrow scope**: it
grounds one scalar admission (`SELECTOR² = 2/3`) in retained
narrow-theorem content. The narrow contribution is the explicit
identification that under the qubit reframe, the ratio `2/3` is no
longer admitted but is structural.

The note **does not overclaim**. It does not claim:
- That `δ = 2/9 rad` follows (radian no-go remains)
- That `Q = 2/3` is closed (other admissions remain)
- That the qubit-lattice-dim closure route is itself retained-grade
  (other admissions remain)
- That the broader Koide chain is closed (extensive open content
  remains per the existing audit-conditional state)

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — canonical A1 supplies the qubit / Cl(3,0) per-site algebra with the 3-generator structure
- [`CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md) — retained narrow theorem supplying the qubit Hilbert dimension 2
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md) — retained narrow theorem supplying the complexification split
- [`CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md`](CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md) — parent conditional note whose qubit-lattice-dim algebraic closure route (note 22) this note grounds one admission of

**Upstream standard-math imports** (named non-derivation; not framework rows):

- Standard finite-dim linear algebra (counting basis elements)

**Plain-text pointer references** (NOT load-bearing deps):

- `KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md` — retained no-go on radian bridge; explicitly NOT challenged by this note
- `KOIDE_DELTA_DIMENSIONLESS_CLOSURE_VIA_V8_THEOREM_NOTE_2026-04-29.md` — adjacent dimensionless-layer closure note; not load-bearing here
- `KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md` — arithmetic `Q = d · δ` link, retained; arithmetically connects Q closure to δ but doesn't bridge the radian gap

## What this file is not

- Not a closure of `δ = 2/9 rad` (radian no-go applies)
- Not a closure of `Q = 2/3` (multiple other admissions remain)
- Not a derivation of `SELECTOR` from first principles outside the qubit reframe — the reframe is essential
- Not a numerical-prediction change
- Not a unilateral retagging. The narrow bounded-theorem candidacy depends on independent audit acceptance of the dimension-ratio identification under the qubit reframe of A1.
