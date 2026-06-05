# Diagonal-Connection Thought Experiment — √2-Centered Foundation (Scoping)

**Date:** 2026-06-04
**Type:** scoping / thought-experiment surface
**Claim type:** meta
**Status authority:** independent audit lane only. This note proposes a
thought-experiment surface; it sets no audit status and changes no axiom.
**Primary runner:** [`scripts/diagonal_sqrt2_foundation_enumerator.py`](../scripts/diagonal_sqrt2_foundation_enumerator.py)
(SUMMARY: PASS=16 FAIL=0).
**Cached log:** [`logs/runner-cache/diagonal_sqrt2_foundation_enumerator.txt`](../logs/runner-cache/diagonal_sqrt2_foundation_enumerator.txt)

> This is one of two parallel diagonal-connection explorations. The sister
> build is a broad six-phase sweep across the three gates. THIS build is
> centered on the single load-bearing question: **is the √2 face-diagonal
> length weighting FORCED (not merely natural), so that the Brannen modulus
> `r = 1/2` becomes derived from substrate geometry?**

## Motivation

The current framework axioms (`MINIMAL_AXIOMS_2026-06-04.md`) fix:

1. **Lattice** — `Z^3` with nearest-neighbor (NN) cubic adjacency.
2. **Quantum** — per-site qubit `A_x = M_2(C) ≅ Cl(3,0)`.
3. **Record** — finite scalar record-readout additivity.

The just-landed `QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04`
proves a unitary connection between two NN qubit fibers carries the Lie
algebra `u(2) = su(2) + u(1)` (the electroweak shape), and notes that color
`su(3)` is **dimension-obstructed on a single qubit fiber**.

Three framework gates remain open:

- **GATE-COLOR** — origin of `SU(3)`; not native to one qubit.
- **GATE-CHIRALITY** — the `C_3`-orbit-splitting chiral grading `Γ_χ` on the
  generation `R^3` factor; a retained no-go
  (`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`) forbids it for
  `C_3`-equivariant (circulant) operators built on NN structure.
- **GATE-R-HALF** — the charged-lepton Brannen modulus `r = |b|^2/a^2 = 1/2`,
  currently admitted as Tier-A `AC_φλ`
  (`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`). Multiple
  prior attacks (24-physicist panel; (α,β)-cone panel; K₀-real panel) all
  converged on the same wall: the framework reaches **discrete** data but
  never the **continuous** modulus `r` (a category mismatch).

## The thought experiment

Extend the Lattice axiom's adjacency from NN-only to include **diagonals**
(face-diagonals of each unit cube, and optionally body-diagonals), and treat
each diagonal link as carrying its own qubit-link unitary connection.

Three commitment levels:

- **L1 (free / derived).** Diagonal connection = ordered product of NN
  connections along a chosen path. Adds nothing new; the existing Wilson-loop
  machinery already contains this. (Negative result; frame-clearing.)
- **L2 (convention extension).** Diagonal links are *independent* qubit-link
  connections, each carrying its own `u(2)`. Adjacency grows from cubic NN to
  cubic + diagonal. This is convention-adoption territory — audit-decided per
  the radian-reclassification precedent.
- **L3 (genuine new physics).** Distance-**weighted** connections: a
  face-diagonal link carries a weight set by its Euclidean length `√2`
  relative to the NN length `1`. The connection class becomes non-local but
  Lieb-Robinson-compatible. This is where `GATE-R-HALF` lives.

## Foundation facts (runner-verified, PASS=16/0)

The runner establishes four finite linear-algebra facts (the four scouts):

- **S1 (geometry).** The hw=1 BZ-corner generation orbit
  `{(1,0,0), (0,1,0), (0,0,1)}` has all three pairs at squared distance `2`
  — they are mutually **face-diagonal**. NN adjacency does **not** connect
  them; face-diagonal adjacency does. The generation orbit is *invisible to
  NN, visible to face-diagonal*. This is precisely the orbit on which
  `GATE-CHIRALITY` and the generation/color identification act.

- **S2 (color).** The three face-diagonal pair-connections (one `u(2)` per
  pair) on the 3-generation factor `C^3` generate the full `u(3) = su(3) + u(1)`
  Lie algebra (dimension 9). Under NN adjacency, those three pairs are not
  simultaneously connected (S1), which is *why* color was obstructed; under
  face-diagonal adjacency they are, and pairwise `u(2)` closes to `u(3)`.

- **S3 (chirality).** A single (non-`C_3`-symmetric) face-diagonal coupling
  `H` admits a `Z_2` grading `Γ` with `Γ^2 = I`, `{H, Γ} = 0`, while
  `[H, R] ≠ 0` (`R` = `C_3` shift). This operator lies **outside** the
  retained no-go's `C_3`-equivariant / circulant scope: the chirality grading
  is *available* on the wider face-diagonal connection class. (Whether
  dynamics *selects* a single non-circulant coupling versus a symmetric
  combination — which would be circulant again, back inside the no-go — is a
  separate open question.)

- **S4 (r=1/2).** The face-diagonal Euclidean length `√2` gives a circulant
  amplitude ratio `|b|/a = 1/√2`, hence `r = |b|^2/a^2 = 1/2` **exactly**.
  Three independent natural weight conventions — geometric length,
  inverse-distance, and K₀-real block-counting — all converge on `1/√2`. The
  discrete lattice thereby supplies a **continuous geometric datum** (`√2`)
  that lands `r = 1/2`. This directly targets the category-mismatch wall that
  defeated every prior `r = 1/2` attack: the continuous modulus the panels
  said the framework could never reach is the diagonal of a unit square.

## The load-bearing question (centerpiece of this build)

> Is the `√2` face-diagonal length weighting **forced** by the qubit-link
> connection structure on a face-diagonal edge, or merely **natural**?

- If **forced** → `r = 1/2` is *derived* from substrate geometry; the
  category mismatch is defeated; `GATE-R-HALF` closes.
- If only **natural** → `r = 1/2` becomes a much-better-motivated *convention*
  (still progress, adoptable per precedent), not a closure.

The deep-dive phases attack exactly this, with color (S2) and chirality (S3)
as corroborating context that the *same* adjacency change touches multiple
gates at once (per the "no coincidences in frontier physics" reasoning: one
structural change resolving three independent gates is structural, not
accidental).

## What this note does NOT do

- It does **not** modify any axiom. `MINIMAL_AXIOMS_2026-06-04.md` is
  untouched; the diagonal extension is proposed as a thought-experiment
  surface, not adopted.
- It does **not** claim `r = 1/2` is derived. The `√2`-forcing question is
  explicitly open and is the subject of the deep-dive phases.
- It does **not** set audit status, promote any row, or weaken any retained
  no-go. The chirality no-go remains correct *on its scope* (circulant /
  `C_3`-equivariant operators); the face-diagonal class is simply wider.
- It does **not** import external comparators or PDG values. `√2` is a lattice
  geometric datum; `r = 1/2` is compared only structurally.

## Cross-references

- `MINIMAL_AXIOMS_2026-06-04.md` — the three-axiom baseline.
- `QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md` — NN
  qubit-link `u(2)` and the color obstruction on one qubit.
- `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md` — the
  chirality no-go (circulant scope).
- `STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`
  — the hw=1 generation orbit.
- `CHARGED_LEPTON_TWO_HIGGS_CANONICAL_REDUCTION_NOTE.md` — `Y_e = A_e + B_e·C`.
- `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md` — the
  `AC_φλ` chain and the `r = 1/2` admission.
- `AXIOM_MINIMALITY_POLICY.md` / `RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md`
  — the convention-adoption governance precedent for the L2/L3 question.
