# Kraus–Choi Representation on the Qubit-Lattice CPTP Map Algebra (Narrow)

**Date:** 2026-05-20
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Route the finite-region Kraus/Choi representation of
qubit-lattice CPTP maps through the framework-local normalization-reconciled
Kraus/Choi correspondence, rather than through a bare textbook theorem
import. Kraus 1971, Choi 1975, and textbook quantum-information treatments
remain parallel references.
**Primary runner:** [`scripts/kraus_choi_normalization_convention_check_2026_06_05.py`](../scripts/kraus_choi_normalization_convention_check_2026_06_05.py)
**Primary runner cache:** [`logs/runner-cache/kraus_choi_normalization_convention_check_2026_06_05.txt`](../logs/runner-cache/kraus_choi_normalization_convention_check_2026_06_05.txt)
**Framework-local Kraus/Choi proof:** [`KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md`](KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md)
with proof runner
[`scripts/audit_companion_kraus_choi_normalization_reconciled_2026_06_05.py`](../scripts/audit_companion_kraus_choi_normalization_reconciled_2026_06_05.py)

## Honest scope

This note is finite-region only. Its Kraus/Choi representation step now
load-bears on the framework-local normalization-reconciled correspondence
note and runner, which reproves the closed Choi/Kraus round trip on
`M_2(ℂ)` and `M_2(ℂ) ⊗ M_2(ℂ)` with the `d`-factors fixed. The framework
contribution here is the application of that reconciled finite-dimensional
matrix calculation to the finite qubit-lattice algebra
`A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)`. Standard Kraus/Choi references are citations
in parallel, not load-bearing authority for this row.

If audit-retained, this gives downstream notes such as
`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20` a scoped
qubit-lattice theorem to cite when they need the Kraus/Choi
representation of a finite-region CPTP map. It does not prove that a
specific record-formation dynamics is CPTP, and it does not retag any
downstream row by itself.

## Claim

Let `Λ ⊂ Z^3` be a finite region. The qubit-lattice operator algebra
is `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ) ≅ M_d(ℂ)` for `d = 2^|Λ|`.

**Theorem (framework-local Kraus/Choi correspondence, applied).** A linear map
`Φ: A_Λ → A_Λ` is completely positive (CP) if and only if it has an
**operator-sum representation**

```text
Φ(X) = Σ_r K_r · X · K_r†                                                (1)
```

for a finite family of **Kraus operators** `{K_r} ⊂ A_Λ`. The map is
additionally **trace-preserving (TP)** iff `Σ_r K_r† K_r = 𝟙`.
Equivalently, `Φ` is CP iff its **Choi matrix**

```text
C_Φ := (𝟙 ⊗ Φ) (|Ω⟩⟨Ω|)                                                 (2)
```

(where this note uses the **unnormalized** convention
`|Ω⟩ = Σ_i |i⟩|i⟩` on `A_Λ ⊗ A_Λ`) is positive semidefinite.

The framework's qubit-lattice algebra `A_Λ = ⊗_x M_2(ℂ)` is a
finite-dim matrix algebra (`M_d(ℂ)` with `d = 2^|Λ|`), so the finite
matrix-surface hypotheses checked by the framework-local reconciled
correspondence note apply directly.

## Setup

By the named Lattice and Quantum axioms in
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md), the
per-site operator algebra is `M_2(ℂ)` on the `Z^3` lattice. For finite
`Λ ⊂ Z^3`:

- `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)_x ≅ M_d(ℂ)` for `d = 2^|Λ|`
- `A_Λ ⊗ A_Λ ≅ M_{d²}(ℂ)` — joint algebra used for the Choi matrix

A **linear map** `Φ: A_Λ → A_Λ` is **completely positive (CP)** iff
for every `n ≥ 1`, the extension `𝟙_n ⊗ Φ: M_n(ℂ) ⊗ A_Λ → M_n(ℂ)
⊗ A_Λ` is positivity-preserving. It is **trace-preserving (TP)** iff
`Tr(Φ(X)) = Tr(X)` for all `X ∈ A_Λ`.

CPTP maps are a standard finite-region model class for dynamics,
measurements, decoherence, and record-update maps when a separate lane
establishes that the update under discussion is CPTP.

## Step 1 — Choi correspondence on the finite matrix surface

The framework-local reconciled note proves the finite-dimensional Choi
round trip under one unnormalized convention:
A linear map `Φ: M_d(ℂ) → M_d(ℂ)` is CP iff its Choi matrix
`C_Φ ∈ M_{d²}(ℂ)` (constructed via the Choi–Jamiołkowski isomorphism
in equation (2)) is positive semidefinite.

The Choi matrix construction:
- `|Ω⟩ = Σ_i |i⟩|i⟩` (unnormalized maximally entangled vector on
  `ℂ^d ⊗ ℂ^d`)
- `C_Φ = (𝟙 ⊗ Φ)(|Ω⟩⟨Ω|)`
- `Φ(X) = Tr_1[(X^T ⊗ 𝟙) C_Φ]` (inverse map)

If one instead uses the normalized vector
`|Ω_norm⟩ = d^(-1/2) Σ_i |i⟩|i⟩`, then
`C_Φ^norm = C_Φ / d` and the inverse formula is
`Φ(X) = d Tr_1[(X^T ⊗ 𝟙) C_Φ^norm]`. The source convention for this
row is the unnormalized one above, so no extra factor appears in the
displayed inverse formula.

The proof runner checks this closed loop on the qubit and two-qubit
matrix surfaces, including the transpose-map CP boundary. Choi 1975 is
cited as parallel historical provenance.

## Step 2 — Kraus extraction from the same Choi convention

A linear map `Φ: M_d(ℂ) → M_d(ℂ)` is CP iff it has an
operator-sum representation

```text
Φ(X) = Σ_{r=1}^{r_*} K_r · X · K_r†                                     (1)
```

for some `r_* ≤ d²` and Kraus operators `K_r ∈ M_d(ℂ)`. The map is
**TP** iff `Σ_r K_r† K_r = 𝟙_d`.

Proof: spectral decomposition of the Choi matrix
`C_Φ = Σ_r |v_r⟩⟨v_r|` (positive iff CP, by Step 1) gives Kraus
operators `K_r = vec^{-1}(|v_r⟩)` under the same unnormalized Choi
convention, where `vec^{-1}` reverses the column-stacking isomorphism
`M_d(ℂ) → ℂ^{d²}`. With the normalized Choi convention, the same
calculation would instead carry the compensating `√d` factor.

Minimal Kraus representations are unique up to unitary mixing of the
Kraus operators; non-minimal representations are equivalent after
padding / isometric mixing.

## Step 3 — Application to the qubit-lattice substrate

The qubit-lattice algebra `A_Λ = ⊗_x M_2(ℂ)` is isomorphic to
`M_d(ℂ)` with `d = 2^|Λ|`. So:

- The framework-local Kraus extraction applies directly: any CPTP map on
  `A_Λ` has an operator-sum representation with Kraus operators
  `K_r ∈ A_Λ` and `Σ_r K_r† K_r = 𝟙`.
- The framework-local Choi correspondence applies directly: CP iff Choi
  matrix positive semidefinite.

In the **thermodynamic limit** `Λ → Z^3`, the quasi-local algebra
`A = ⊗_{x ∈ Z^3} M_2(ℂ)` is a UHF C*-algebra of type `2^∞`. This note
does not claim a full Kraus/Choi representation theorem for arbitrary
maps on that infinite algebra. It only records compatibility with the
standard quasi-local construction: finite-region CPTP maps form the
local building blocks used in the inductive system. Any full
infinite-volume channel theorem is a separate operator-algebraic input.

## Step 4 — Consistency with the framework's record lane

The framework's `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20`
identifies persistent-record outcomes as Kraus operators `K_r` on the
system algebra, with the unconditional update being CPTP:

```text
σ → E(σ) = Σ_r K_r · σ · K_r†                                            (3)
```

Steps 1-2 supply the framework-local finite-region representation
calculation for any CPTP map on the matrix surface. Step 3 verifies that
the finite-region qubit-lattice algebra satisfies the hypotheses. Together, this gives
the record-as-Kraus lane a scoped upstream representation theorem to
cite after that lane independently establishes that its record update
is a finite-region CPTP map.

## What this can support after audit

- **The finite-region Kraus/Choi representation step** used by
  downstream record-update notes. If retained, this row lets those
  notes cite a qubit-lattice-scoped theorem for finite-region CPTP
  maps instead of carrying a bare, unlocalized textbook reference.
- **Dependency-chain repair for record-update/Born support lanes**
  after independent audit. This row does not promote those parent
  rows by itself.

## What this does not close

- **Thermodynamic-limit Kraus/Choi representation** for arbitrary maps on
  the full quasi-local algebra — cited operator-algebra literature remains
  only parallel context unless a separate finite-to-infinite theorem is supplied.
- **The CPTP-map identification of specific record-formation
  dynamics** — that's the framework's record-lane derivation
  (existing in
  `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` retained_bounded and
  the landed `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20`).
- **The thermodynamic-limit representation theorem** for arbitrary
  maps on the full quasi-local algebra — Step 3 only records
  finite-region compatibility with the inductive system.

## Admitted inputs

1. **Framework-local reconciled Kraus/Choi correspondence** —
   [`KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md`](KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md)
   plus its proof runner, supplying the finite matrix-surface
   Choi/Kraus round trip under one convention.
2. **Finite-dimensional matrix linear algebra** (positive operators,
   spectral decomposition, tensor products of matrix algebras) on the
   explicit `M_d(ℂ)` surface.
3. **Bratteli–Robinson quasi-local construction** for the
   compatibility statement about finite-region maps inside the UHF
   type `2^∞` inductive system — parallel context only for the
   thermodynamic-limit discussion, not a load-bearing finite-region input.

## Risk classification

This is a `positive_theorem` candidate at the narrow-theorem
granularity. Framework-local finite-matrix Kraus/Choi correspondence is
applied to the framework's specific algebra `⊗_x M_2(ℂ) ≅ M_d(ℂ)`.
The narrow contribution is the explicit application to the qubit-lattice
substrate plus the verification that the finite matrix-surface hypotheses
hold there.

Granularity matches retained narrow theorems (positive_theorem,
retained) that apply standard math to the framework's specific
operator structure (e.g., `cl3_complexification_split` applies
standard Clifford theorem; `cl3_faithful_irrep_dim_two` applies
standard representation theory).

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — supplies the named Lattice and Quantum baseline: `Z^3` lattice plus per-site `M_2(ℂ)` operator algebra
- [`KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md`](KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md) — supplies the single-convention finite-matrix Choi/Kraus correspondence and `d`-factor repair
- [`scripts/audit_companion_kraus_choi_normalization_reconciled_2026_06_05.py`](../scripts/audit_companion_kraus_choi_normalization_reconciled_2026_06_05.py) — runner proving the reconciled chain on `M_2(ℂ)` and `M_2(ℂ) ⊗ M_2(ℂ)`

**Parallel references only** (not load-bearing graph deps):

- Kraus 1971 *Ann. Phys.* 64, 311 — operator-sum representation theorem
- Choi 1975 *Lin. Alg. Appl.* 10, 285 — CP-map / Choi-matrix characterization
- Nielsen–Chuang Ch.8 — modern textbook treatment of quantum operations

**Plain-text pointer references** (NOT load-bearing deps):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer of the Kraus structure for record-conditional Born evaluations
- `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md` — downstream/companion note that may cite this row for the finite-region CPTP representation theorem
- `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` (retained_bounded) — existing record-lane structure that the Kraus operators model

## What this file is not

- Not an infinite-volume channel theorem for arbitrary maps on the full
  quasi-local algebra
- Not a closure of the record-formation derivation (separate framework lane)
- Not an automatic promotion of record-as-Kraus or Born to retained (verdicts owned by audit lane)
- Not a numerical-prediction change
