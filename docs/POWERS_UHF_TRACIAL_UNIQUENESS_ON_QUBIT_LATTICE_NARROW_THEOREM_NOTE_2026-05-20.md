# Powers UHF Tracial Uniqueness on the Qubit-Lattice Quasi-Local Algebra (Narrow)

**Date:** 2026-05-20
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Apply the standard UHF tracial-state uniqueness result
(Dixmier; Glimm 1960; Powers 1967) to the qubit-lattice quasi-local
C*-algebra `⊗_{x ∈ Z^3} M_2(ℂ)` (UHF type `2^∞`) as a
framework-internal narrow theorem. Same pattern as the
`GLEASON_ON_QUBIT_LATTICE_*` and `KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_*`
companions: standard math applied to the framework's specific
operator structure.

## Honest scope

This note **does not re-prove the UHF tracial uniqueness theorem
from scratch.** It applies the standard finite-dim → UHF inductive
construction (Glimm 1960; Powers 1967; Dixmier 1981) to the
framework's specific UHF type-`2^∞` algebra, the qubit-lattice
quasi-local algebra. Standard operator-algebra mathematics applied
to the framework's substrate.

If audit-retained, this lifts the Powers/Dixmier/Glimm
external-textbook admission from the landed
[`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)
(bounded support; one of the admissions in the chain), enabling the
tracial-state derivation to potentially retain at higher grade.

## Claim

The qubit-lattice quasi-local C*-algebra

```text
A := ⊗_{x ∈ Z^3} M_2(ℂ)                                                  (1)
```

(UHF C*-algebra of type `2^∞`, the inductive limit of finite tensor
products `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ) ≅ M_{2^|Λ|}(ℂ)` over finite
`Λ ⊂ Z^3`) admits a **unique tracial state** `τ` characterized by

```text
τ(AB) = τ(BA)   for all A, B ∈ A                                         (2)
```

with the explicit finite-region form

```text
τ_Λ(O) = Tr_{A_Λ}(O) / 2^|Λ|   for O ∈ A_Λ                              (3)
```

This is the **standard UHF tracial-state uniqueness theorem**
applied to the qubit-lattice substrate. The unique tracial state
corresponds to the density matrix `ρ_ref = ⊗_x I_2 / 2` of the
companion
[`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md).

## Setup

By A1+A2 of
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md), the
per-site operator algebra is `M_2(ℂ)`. The quasi-local algebra
construction:

- For finite `Λ ⊂ Z^3`, define `A_Λ := ⊗_{x ∈ Λ} M_2(ℂ)_x ≅ M_d(ℂ)`
  with `d = 2^|Λ|`.
- For `Λ_1 ⊂ Λ_2`, the natural inclusion `A_{Λ_1} ↪ A_{Λ_2}` is
  `O ↦ O ⊗ 𝟙_{Λ_2 ∖ Λ_1}`.
- The inductive limit `A := lim_→ A_Λ` is the **UHF C*-algebra of
  type `2^∞`**.

A **state** on `A` is a positive linear functional `φ: A → ℂ` with
`φ(𝟙) = 1`. A **tracial state** additionally satisfies (2).

## Step 1 — Finite-region tracial uniqueness (Dixmier)

**Standard finite-dim result** (Dixmier 1981 §1.7): every finite-dim
simple C*-algebra (or matrix algebra) `M_d(ℂ)` admits a unique
tracial state, given by the normalized trace

```text
τ_Λ(O) = Tr(O) / d = Tr(O) / 2^|Λ|                                       (4)
```

**Proof sketch.** Tracial property + linearity forces `τ(E_{ij}) = 0`
for `i ≠ j` (off-diagonal matrix units have zero trace by
`τ(E_{ii} E_{ij}) = τ(E_{ij} E_{ii}) = 0` since `E_{ij} E_{ii} = 0`).
Tracial property also forces `τ(E_{ii}) = τ(E_{jj})` for all `i, j`
(via permutation-equivalent decomposition). Normalization `τ(𝟙) =
Σ_i τ(E_{ii}) = 1` forces `τ(E_{ii}) = 1/d`. So `τ(O) = Σ_i O_{ii}/d
= Tr(O)/d`.

This applies on each finite region `A_Λ`.

## Step 2 — Tensor compatibility of finite-region tracial states

For nested `Λ_1 ⊂ Λ_2`, the restriction of `τ_{Λ_2}` to `A_{Λ_1}` is

```text
τ_{Λ_2}|_{A_{Λ_1}}(O) = Tr_{A_{Λ_2}}(O ⊗ 𝟙_{Λ_2 ∖ Λ_1}) / 2^|Λ_2|        (5)
                     = Tr_{A_{Λ_1}}(O) · Tr_{A_{Λ_2 ∖ Λ_1}}(𝟙) / 2^|Λ_2|
                     = Tr_{A_{Λ_1}}(O) · 2^|Λ_2 ∖ Λ_1| / 2^|Λ_2|
                     = Tr_{A_{Λ_1}}(O) / 2^|Λ_1|
                     = τ_{Λ_1}(O)
```

So the family `{τ_Λ}_{Λ ⊂ Z^3, finite}` is **compatible** under the
inductive system — the restriction of a larger-region tracial state
to a sub-region is the sub-region's tracial state.

## Step 3 — Inductive limit gives a tracial state on `A`

A compatible family of states on the directed system `{A_Λ}` extends
to a unique state on the inductive limit `A` (standard inductive-limit
construction for C*-algebras, Bratteli–Robinson Vol I.2). The
extension preserves the tracial property:

```text
τ_∞(AB) = lim_Λ τ_Λ(AB)|_{A_Λ}  for A, B ∈ A_Λ
        = lim_Λ τ_Λ(BA)|_{A_Λ}   (since τ_Λ is tracial on A_Λ)          (6)
        = τ_∞(BA)
```

So `τ_∞` is a tracial state on `A = ⊗_{x ∈ Z^3} M_2(ℂ)`.

## Step 4 — Uniqueness on `A` (Glimm / Powers)

**Glimm 1960 / Powers 1967 theorem**: every UHF C*-algebra of any
type admits a **unique tracial state**, namely the inductive-limit
extension of the per-region normalized traces.

**Proof sketch.** Suppose `τ'` is any tracial state on `A`. For
each finite `Λ`, the restriction `τ'|_{A_Λ}` is a tracial state on
`A_Λ ≅ M_{2^|Λ|}(ℂ)`. By Step 1, the unique tracial state on
`M_{2^|Λ|}(ℂ)` is `Tr/2^|Λ|`, so `τ'|_{A_Λ} = τ_Λ`. The family
`{τ'|_{A_Λ}}` is therefore equal to `{τ_Λ}`. By uniqueness of the
inductive-limit extension, `τ' = τ_∞`.

So `τ_∞` is the unique tracial state on `A`. ∎

## Step 5 — Connection to `ρ_ref`

The unique tracial state `τ_∞` is the abstract C*-algebraic
formulation of the framework's pre-record reference state
`ρ_ref = ⊗_{x ∈ Z^3} (I_2 / 2)`. On any finite region
`A_Λ`, both objects compute the same expectation values:

```text
τ_∞|_{A_Λ}(O) = Tr_{A_Λ}(O) / 2^|Λ| = Tr_{A_Λ}(O · ρ_ref|_Λ)             (7)
```

where `ρ_ref|_Λ = ⊗_{x ∈ Λ} (I_2/2)` is the finite-region density
matrix. So `τ_∞` and `ρ_ref` are the same physical state in two
mathematical languages: abstract C*-state vs density-matrix.

## What this closes

- **The Powers 1967 / Dixmier / Glimm 1960 external-textbook
  admission** in the landed
  `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`
  (bounded support). The UHF tracial uniqueness now has
  framework-internal narrow-theorem status on the qubit-lattice
  quasi-local algebra.
- **Combined with the Tomita companion note** (also in this PR),
  the tracial-state derivation chain has framework-internal
  narrow-theorem upstream for all its standard-math admissions.

## What this does not close

- **The no-extra-structure identification of `τ_∞` as the
  pre-record reference state.** That's the philosophical
  identification still admitted in the tracial-state derivation
  note. Closing it requires either an explicit invariance premise
  (the unique inner-automorphism-invariant state) or an extension
  to a separate identification note.
- **Re-derivation of inductive-limit construction or Bratteli–Robinson
  machinery from scratch** — cited as standard operator-algebra
  content; not re-proved here.
- **Promotion of the tracial-state row to retained_clean** — the
  auditor still owns the verdict; this PR removes one named blocker.

## Admitted inputs

1. **Dixmier 1981 finite-dim simple C*-algebra trace uniqueness** —
   standard finite-dim algebra (*Les algèbres d'opérateurs dans l'espace
   hilbertien*).
2. **Glimm 1960 / Powers 1967 UHF tracial uniqueness theorem** —
   standard UHF C*-algebra content (*Trans. AMS* 95, 318; *Ann. Math.*
   86, 138). Cited as named non-derivation; the framework's
   contribution is the application to type-`2^∞`.
3. **Bratteli–Robinson 1979/1981 inductive-limit construction** for
   C*-algebras — standard math.

## Risk classification

`positive_theorem` candidate at narrow-theorem granularity. Standard
UHF tracial uniqueness applied to the framework's specific
quasi-local algebra. The narrow contribution is the explicit
application to the qubit-lattice type-`2^∞` structure plus the
verification that the standard theorem's hypotheses hold there.

Granularity matches retained narrow theorems (positive_theorem,
retained) that apply standard math to the framework's specific
operator structure.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) — landed companion (bounded support) whose Powers/Dixmier/Glimm admission this note supplies the framework-internal upstream for

**Upstream standard-math imports** (named non-derivation):

- Dixmier 1981 *Les algèbres d'opérateurs dans l'espace hilbertien*
- Glimm 1960 *Trans. AMS* 95, 318
- Powers 1967 *Ann. Math.* 86, 138
- Bratteli–Robinson 1979/1981 *Operator Algebras and Quantum Statistical Mechanics*

**Plain-text pointer references** (NOT load-bearing deps):

- `TOMITA_TENSOR_TRACE_ON_FINITE_DIM_MATRIX_NARROW_THEOREM_NOTE_2026-05-20.md` — companion narrow theorem in this PR handling the per-region tensor-traciality argument used in the tracial-state derivation Step 2

## What this file is not

- Not a re-derivation of the UHF tracial uniqueness theorem from scratch (cited as standard math)
- Not a closure of the no-extra-structure identification premise (separate philosophical admission)
- Not an automatic promotion of the tracial-state row to retained-clean (auditor-owned)
- Not a numerical-prediction change
