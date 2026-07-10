# Gleason's Theorem on the Qubit-Lattice Projection Lattice (Narrow)

**Date:** 2026-05-20
**Substrate authority update:** 2026-07-09 — the substrate citation moved from the historical `MINIMAL_AXIOMS_2026-05-20.md` (legacy `A1`/`A2` numbering) to the live `MINIMAL_AXIOMS_2026-06-29.md` plus the joint-presentation tensor-substrate bridge; the theorem content is unchanged.
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Primary runner:** [`scripts/frontier_gleason_qubit_lattice_projection_narrow_2026_07_09.py`](../scripts/frontier_gleason_qubit_lattice_projection_narrow_2026_07_09.py)
**Cached output:** [`logs/runner-cache/frontier_gleason_qubit_lattice_projection_narrow_2026_07_09.txt`](../logs/runner-cache/frontier_gleason_qubit_lattice_projection_narrow_2026_07_09.txt)
**Purpose:** Apply Gleason's theorem to the qubit-lattice projection
lattice as a framework-internal narrow theorem, on the model of the
retained `cl3_complexification_split_narrow_theorem_note_2026-05-10`.
If independently retained, this replaces the Born derivation chain's
bare Gleason import with a framework-scoped narrow theorem applying
Gleason's standard result to the framework's specific finite-region
Hilbert spaces.

## Honest scope

This note **does not re-prove Gleason's theorem from scratch.** It
applies the standard Gleason theorem (1957, refined by various
authors) to the framework's specific Hilbert space `H_Λ = ⊗_{x ∈ Λ}
ℂ²` for finite `Λ ⊂ Z^3` with `|Λ| ≥ 2`. The framework's contribution
is:

1. Identifying `H_Λ` as a Hilbert space satisfying Gleason's
   hypotheses (`dim ≥ 3`).
2. Verifying the probability-measure structure on the projection
   lattice `P(H_Λ)` matches Gleason's setup.
3. Reading off Born form `p(P) = Tr(σ P)` as the unique probability
   measure on the qubit-lattice projection lattice.

This is the same narrow-theorem granularity as `cl3_complexification_split_narrow_theorem_note_2026-05-10`
(which applies the standard Clifford-algebra complexification
theorem to `Cl(3,0)`) — standard math applied to the framework's
specific substrate.

## Claim

Let `Λ ⊂ Z^3` be a finite region with `|Λ| ≥ 2`. The qubit-lattice
Hilbert space is `H_Λ = ⊗_{x ∈ Λ} ℂ²` of dimension
`d = 2^|Λ| ≥ 4 ≥ 3`. Let `P(H_Λ)` denote the projection lattice on
`H_Λ` (the set of orthogonal projection operators).

**Theorem.** Every countably additive probability measure
`m: P(H_Λ) → [0, 1]` (satisfying `m(0) = 0`, `m(𝟙) = 1`, and
σ-additivity over countable orthogonal families) is of the form

```text
m(P) = Tr(σ · P)                                                         (1)
```

for a unique density matrix `σ ∈ M_d(ℂ)` (positive, `Tr σ = 1`).

This is Gleason 1957 applied to the qubit-lattice substrate. The
form `m(P) = Tr(σ P)` is the **Born rule** for projection-valued
measurements on the qubit-lattice projection lattice.

## Setup

By the Lattice and Qubit axioms of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), the
per-site possibility domain has algebraic presentation `M_2(ℂ)` acting
on `ℂ²`, and sites are the points of `Z^3`. The joint tensor carrier
over a finite region — the composition step the axiom memo leaves to
downstream bridges — is supplied by the declared joint presentation in
[`QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md`](QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md)
(minimal faithful joint carrier of the pairwise-commuting site
algebras, with its minimality selection named there). For `Λ ⊂ Z^3`:

- `H_Λ = ⊗_{x ∈ Λ} ℂ²_x`, complex Hilbert space of dim `2^|Λ|`
- `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)_x = B(H_Λ)`, finite-dim type-I factor

The **projection lattice** `P(H_Λ)` is the set of orthogonal
projections `P ∈ A_Λ` (i.e., `P = P^†` and `P^2 = P`). It is a
complete orthocomplemented lattice under inclusion of range.

A **probability measure on `P(H_Λ)`** is a function
`m: P(H_Λ) → [0, 1]` satisfying:

- (M1) `m(0) = 0`
- (M2) `m(𝟙) = 1`
- (M3) σ-additivity: for any countable family `{P_i}` of pairwise
  orthogonal projections with `Σ_i P_i ≤ 𝟙`:
  `m(Σ_i P_i) = Σ_i m(P_i)`

These are the standard probability axioms restricted to the
projection lattice (Mackey 1957; Gleason 1957).

## Step 1 — Hilbert dimension satisfies Gleason's hypothesis

Gleason's theorem requires `dim H ≥ 3` for the projection-lattice
version. The single-qubit case `dim H = 2` is outside this note's
scope and is handled, if retained, by the separate Busch-POVM
companion note.

For `|Λ| ≥ 2`:

```text
dim H_Λ = 2^|Λ| ≥ 2^2 = 4 ≥ 3                                            (2)
```

So Gleason's dimensional hypothesis is satisfied on any qubit-lattice
multi-site Hilbert space.

## Step 2 — Frame-function construction

Given a probability measure `m: P(H_Λ) → [0, 1]`, the
**frame function** `f_m` on the unit sphere `S(H_Λ)` is

```text
f_m(|ψ⟩) := m(|ψ⟩⟨ψ|)                                                    (3)
```

for `|ψ⟩ ∈ S(H_Λ)` (i.e., `‖ψ‖ = 1`). For any orthonormal basis
`{|e_i⟩}_{i=1}^d` of `H_Λ`:

```text
Σ_i f_m(|e_i⟩) = Σ_i m(|e_i⟩⟨e_i|) = m(Σ_i |e_i⟩⟨e_i|) = m(𝟙) = 1       (4)
```

using (M2) and σ-additivity (M3). So `f_m` is a **frame function**
in Gleason's sense: a bounded `[0,1]`-valued function on the unit
sphere whose values sum to 1 on any orthonormal basis.

## Step 3 — Gleason's theorem (cited)

**Gleason's Theorem** (Gleason 1957 *J. Math. Mech.* 6, 885):
On a complex Hilbert space `H` with `dim H ≥ 3`, every frame function
`f: S(H) → [0, 1]` is of the form

```text
f(|ψ⟩) = ⟨ψ| σ |ψ⟩                                                       (G)
```

for a unique positive trace-class operator `σ` with `Tr σ = 1` (i.e.,
a density matrix).

The proof (in Gleason's original paper and modern treatments such as
Hughston–Jozsa–Wootters 1993, Cooke–Keane–Moran 1985, Wright 1979)
proceeds in two main steps:

1. **Continuity:** any frame function is continuous on `S(H)` (a
   non-trivial regularity result).
2. **Quadratic extension:** every continuous frame function on
   `dim ≥ 3` extends to a bounded quadratic form on `H`, hence to a
   trace expression with positive semidefinite operator `σ`.

The dim ≥ 3 hypothesis is essential: at dim 2, the projection lattice
is "too small" (only 1-parameter family of orthogonal pairs) for the
quadratic-extension argument to apply.

This theorem is standard mathematical physics content (every QM
foundations / quantum-information textbook treats it).

## Step 4 — Application to the qubit-lattice substrate

On `H_Λ` with `|Λ| ≥ 2` (so `dim H_Λ = 2^|Λ| ≥ 4 ≥ 3`):

- Gleason's hypothesis is satisfied (Step 1).
- The frame function `f_m` constructed in Step 2 satisfies Gleason's
  theorem's premises.
- Applying Gleason's theorem (G):

```text
f_m(|ψ⟩) = ⟨ψ| σ |ψ⟩                                                     (5)
```

for a unique density matrix `σ ∈ A_Λ`.

Translating back to projection-lattice values:

```text
m(P) = m(Σ_i |ψ_i⟩⟨ψ_i|) = Σ_i ⟨ψ_i| σ |ψ_i⟩ = Tr(σ P)                  (6)
```

for any `P ∈ P(H_Λ)` with eigendecomposition `P = Σ_i |ψ_i⟩⟨ψ_i|`.
This is (1). □

## Step 5 — Uniqueness of σ

The density matrix `σ` in (1) is **unique** because the projection
lattice `P(H_Λ)` is large enough to separate density matrices. For
any two distinct density matrices `σ ≠ σ'`, there exists at least
one projection `P` with `Tr(σ P) ≠ Tr(σ' P)` (taking `P` as the
eigenprojection of `σ - σ'` for a non-zero eigenvalue).

So the framework's qubit-lattice projection lattice gives a unique
density-matrix representation of any countably-additive probability
measure.

## What this can close after audit

- **The Gleason-1957 admitted-input** in
  `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`'s
  derivation chain. If independently retained, this row supplies the
  framework-scoped Gleason application for finite regions with
  `|Λ| ≥ 2`.
- **One textbook-import slot** in the Born-support chain. This note
  does not by itself promote Born; parent-row status changes require
  the rest of the chain and independent audit closure.

## What this does not close

- **The single-site dim-2 case** (`|Λ| = 1`, `dim H = 2`) — outside
  this note's Gleason scope and addressed by the separate
  `BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`
  candidate if that row is retained.
- **The other admissions in the Born derivation chain**: no-extra-structure
  pre-record identification, persistent-record → Kraus identification,
  Lüders rule, sequential-effect product. Each has its own narrow
  theorem.
- **Re-derivation of Gleason's theorem from scratch** — cited as
  standard mathematical-physics content; not re-proved here.

## Admitted inputs

1. **Gleason 1957 frame-function theorem** on Hilbert spaces of
   `dim ≥ 3` — standard math (J. Math. Mech. 6, 885; modern proofs
   in Hughston–Jozsa–Wootters 1993, Cooke–Keane–Moran 1985, Wright
   1979). Cited as named non-derivation standard content; the
   framework's contribution is the application to its specific
   Hilbert space.
2. **Standard probability axioms (M1)–(M3)** — universal background.
3. **Standard Hilbert space theory** (orthonormal bases, projection
   spectral decomposition) — universal background.

## Risk classification

This is a `positive_theorem` candidate at the narrow-theorem granularity.
The argument is textbook Gleason theory applied to the framework's
specific Hilbert space `⊗_x ℂ²`. The narrow contribution is the
explicit application to the qubit-lattice substrate plus the
verification of Gleason's hypotheses on that substrate.

The granularity matches the retained `cl3_complexification_split_narrow_theorem_note_2026-05-10`
(positive_theorem, retained): standard Clifford-algebra theorem
applied to the framework's specific algebra.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — live axiom memo: per-site `M_2(ℂ)` possibility domain (Qubit) + `Z^3` substrate (Lattice)
- [`QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md`](QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md) — joint tensor carrier `H_Λ = ⊗_{x ∈ Λ} ℂ²` for finite `Λ`, derived from the live memo plus a named minimality selection

**Upstream standard-math imports** (named non-derivation):

- Gleason 1957 *J. Math. Mech.* 6, 885 — original frame-function theorem
- Hughston–Jozsa–Wootters 1993 *Phys. Lett. A* 183, 14 — short modern proof
- Cooke–Keane–Moran 1985 — alternative proof
- Wright 1979 — non-separable / general case

**Plain-text pointer references** (NOT load-bearing deps):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer of this narrow theorem in the Born derivation chain
- `BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` — companion narrow theorem handling the `|Λ| = 1` (dim-2) case

## What this file is not

- Not a re-derivation of Gleason's theorem (cited as standard math)
- Not a closure of the Born derivation row (other admissions remain)
- Not an automatic Born promotion to retained (verdicts owned by audit lane)
- Not a numerical-prediction change
