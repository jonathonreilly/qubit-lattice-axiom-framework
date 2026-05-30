# Busch POVM Extension on the Qubit-Lattice Effect Algebra (Narrow)

**Date:** 2026-05-20
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Apply Busch's 2003 POVM-extension of Gleason's theorem to
the qubit-lattice effect algebra, covering the single-site dim-2
case (`|Λ| = 1`) that Gleason's original projection-lattice theorem
does not handle. It is a companion to the separate
`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`
candidate, but does not depend on that row.

## Honest scope

This note **does not re-prove Busch's theorem from scratch.** It
applies Busch's standard 2003 POVM extension (and the CFMR 2004
refinement) to the framework's qubit-lattice effect algebra,
including the single-site `dim H = 2` case. Same narrow-theorem
granularity as the Gleason companion: standard mathematical-physics
content applied to the framework's specific substrate.

## Claim

Let `Λ ⊂ Z^3` be any finite region with `|Λ| ≥ 1`. The qubit-lattice
Hilbert space `H_Λ = ⊗_{x ∈ Λ} ℂ²` has dimension
`d = 2^|Λ| ≥ 2`. Let `E(H_Λ)` denote the POVM effect algebra on
`H_Λ` (the set of positive operators `0 ≤ E ≤ 𝟙`).

**Theorem.** Every countably additive POVM-additive probability
measure `m: E(H_Λ) → [0, 1]` (satisfying `m(0) = 0`, `m(𝟙) = 1`,
and σ-additivity over countable POVM partitions) is of the form

```text
m(E) = Tr(σ · E)                                                         (1)
```

for a unique density matrix `σ ∈ M_d(ℂ)` (positive, `Tr σ = 1`).

This is Busch 2003 applied to the qubit-lattice substrate, **including
the `dim H = 2` single-site case** that lies outside Gleason's
original projection-lattice theorem. The form `m(E) = Tr(σ E)` is the
**Born rule** for POVM measurements on the qubit-lattice effect
algebra at all dimensions `≥ 2`.

## Setup

By A1+A2 of
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md), the
per-site operator algebra is `M_2(ℂ)`. For any finite `Λ ⊂ Z^3`:

- `H_Λ = ⊗_{x ∈ Λ} ℂ²_x`, complex Hilbert space of dimension
  `d = 2^|Λ|`
- `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)_x = M_d(ℂ)`

The **POVM effect algebra** `E(H_Λ)` is the set of positive operators
bounded by the identity:

```text
E(H_Λ) := { E ∈ A_Λ : 0 ≤ E ≤ 𝟙 }                                       (2)
```

A **POVM** on `H_Λ` is a finite collection `{E_i}_{i=1}^n ⊂ E(H_Λ)`
with `Σ_i E_i = 𝟙`. POVMs generalize projective measurements (which
are POVMs with `E_i = P_i` projections) to unsharp measurements.

A **POVM-additive probability measure** is a function
`m: E(H_Λ) → [0, 1]` satisfying:

- (M1) `m(0) = 0`
- (M2) `m(𝟙) = 1`
- (M3) σ-additivity over POVM partitions: for any countable POVM
  `{E_i}` with `Σ_i E_i = 𝟙`, `Σ_i m(E_i) = 1`

(M3) is strictly stronger than projection-lattice σ-additivity:
POVMs include unsharp effects, which are not projections.

## Step 1 — Why Gleason's projection-lattice theorem fails at dim 2

At `dim H_Λ = 2` (single qubit, `|Λ| = 1`), the projection lattice
`P(H_Λ)` has a small structure: the only orthogonal pairs are
`(|ψ⟩⟨ψ|, |ψ^⊥⟩⟨ψ^⊥|)` for unit vectors `|ψ⟩`. The orthonormal-basis
constraint `m(|ψ⟩⟨ψ|) + m(|ψ^⊥⟩⟨ψ^⊥|) = 1` permits non-unique
extensions — frame functions on `S(ℂ²)` are not forced to be
quadratic.

Gleason's theorem proof relies on the dim ≥ 3 structure: orthonormal
bases come in continuous families, and the frame function's values
at "rotated" bases force the quadratic extension via a regularity
argument. At dim 2, the rotation freedom is insufficient and the
quadratic extension can fail.

This is the **classical Gleason gap at dim 2**, addressed by going
to the POVM-effect-algebra extension.

## Step 2 — Busch's POVM extension (cited)

**Busch's Theorem** (Busch 2003 *Phys. Rev. Lett.* 91, 120403;
refined Caves–Fuchs–Manne–Renes 2004 *Found. Phys.* 34, 193):

On a complex Hilbert space `H` with `dim H ≥ 2`, every POVM-additive
probability measure `m: E(H) → [0, 1]` is of the form

```text
m(E) = Tr(σ · E)                                                         (B)
```

for a unique density matrix `σ` on `H`.

The proof relies on the **richness of the POVM effect algebra at
dim 2**: even at dim 2, the POVM elements form a continuous family
parameterizing the full Bloch sphere, and POVM-additivity over
two-element decompositions `E + E^⊥ = 𝟙` plus σ-additivity over
multi-outcome POVMs (e.g., Pauli-string POVMs) is sufficient to
fix the density-matrix form.

**Sketch of Busch's argument** (Busch 2003, §III):

1. **Effect-algebra structure:** the POVM effect algebra
   `E(H)` is an order-and-additive algebra (with the partial sum
   defined when `E_1 + E_2 ≤ 𝟙`).
2. **Linear extension:** the POVM-additive condition (M3) forces
   `m` to extend linearly to all positive operators in `A_Λ`.
3. **Riesz representation:** any positive linear functional on the
   self-adjoint operators of a finite-dim C*-algebra is of the
   form `Tr(σ · )` for some positive `σ`.
4. **Normalization:** `m(𝟙) = 1` forces `Tr σ = 1`.

The key bridging step is (2): POVM-additivity is *strictly stronger*
than projection-additivity, so the dim-2 obstruction in Gleason's
proof does not apply.

## Step 3 — Application to the qubit-lattice substrate

For any `|Λ| ≥ 1` (so `dim H_Λ = 2^|Λ| ≥ 2`), Busch's hypothesis is
satisfied. Applying Busch's theorem (B):

```text
m(E) = Tr(σ · E)   ∀ E ∈ E(H_Λ)                                          (3)
```

with `σ` a unique density matrix on `H_Λ`.

This covers all qubit-lattice region sizes including:
- `|Λ| = 1` (single site, dim 2): the **single-qubit Born form**
  — not handled by the Gleason companion, supplied here
- `|Λ| = 2` (two sites, dim 4): both Gleason and Busch apply; they
  give the same `Tr(σ E)` form (Busch reduces to Gleason on
  projections)
- `|Λ| ≥ 3`: Gleason directly applies; Busch confirms on the
  larger POVM-effect algebra

Together, Gleason (`|Λ| ≥ 2`) + Busch (all `|Λ| ≥ 1`) cover **all
qubit-lattice substrate sizes**.

## Step 4 — Finite-region scope and inductive-limit boundary

The theorem above is finite-region: every finite `Λ` has effect
algebra `E(H_Λ)` and Busch's theorem gives the Born form on that
finite algebra. Passing from the compatible finite-region family to a
state on the quasi-local UHF algebra `A = ⊗_x M_2(ℂ)` is a separate
standard operator-algebraic inductive-limit step.

This note therefore supplies the finite-region Born form on the
framework substrate. It does not by itself prove an all-at-once
quasi-local normal-state theorem, nor does it identify the pre-record
state; those are separate rows / imports.

## What this can close after audit

- **The Busch 2003 admitted-input** in
  `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`'s
  derivation chain. If independently retained, this row supplies the
  framework-scoped finite-region Busch application on the qubit-lattice
  effect algebra.
- **The dim-2 single-qubit Born form**, which Gleason's projection-
  lattice theorem cannot supply directly.
- **One textbook-import slot** in the Born-support chain. This note
  does not by itself promote Born; parent-row status changes require
  the rest of the chain and independent audit closure.

## What this does not close

- **The other admissions in the Born derivation chain**: no-extra-structure
  pre-record identification, persistent-record → Kraus identification
  (latter handled by `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20`),
  Lüders rule (handled by the Lüders companion + Greechie
  sequential-product bridge).
- **Re-derivation of Busch's theorem from scratch** — cited as
  standard mathematical-physics content; not re-proved here.
- **Non-commutative joint-system Born forms** that go beyond the
  finite-dim POVM effect-algebra (e.g., continuous-variable
  systems) — out of scope; the framework's substrate is finite-dim
  per site.
- **The quasi-local inductive-limit state theorem** — only the
  finite-region Busch application is claimed here.

## Admitted inputs

1. **Busch 2003 POVM-extension theorem** on Hilbert spaces of
   `dim ≥ 2` — standard math (Phys. Rev. Lett. 91, 120403; refined
   in Caves–Fuchs–Manne–Renes 2004). Cited as named non-derivation
   standard content; the framework's contribution is the application
   to its specific effect algebra.
2. **Standard probability axioms (M1)–(M3)** — universal background.
3. **Standard finite-dim C*-algebra theory** (positive linear
   functionals, Riesz representation) — universal background.

## Risk classification

This is a `positive_theorem` candidate at the narrow-theorem granularity.
Standard Busch theory applied to the framework's specific effect
algebra `E(⊗_x M_2(ℂ))`. The narrow contribution is the explicit
application to the qubit-lattice substrate (especially the dim-2
single-site case) plus the verification of Busch's hypotheses on
that substrate.

Granularity matches retained Clifford-algebra narrow theorems
(positive_theorem, retained): standard math applied to the
framework's specific operator structure.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)

**Upstream standard-math imports** (named non-derivation):

- Busch 2003 *Phys. Rev. Lett.* 91, 120403 — original POVM-extension theorem
- Caves–Fuchs–Manne–Renes 2004 *Found. Phys.* 34, 193 — refined / clarified proof
- Standard finite-dim C*-algebra Riesz-representation result

**Plain-text pointer references** (NOT load-bearing deps):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer of this narrow theorem in the Born derivation chain
- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — supplies the pre-record reference `σ = ρ_ref` for the Born evaluation
- `GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` — companion projection-lattice candidate for `|Λ| ≥ 2`; not load-bearing for this finite-region POVM theorem

## What this file is not

- Not a re-derivation of Busch's theorem (cited as standard math)
- Not a closure of the Born derivation row (other admissions remain; see "What this does not close" above)
- Not an automatic Born promotion to retained (verdicts owned by audit lane)
- Not a numerical-prediction change
