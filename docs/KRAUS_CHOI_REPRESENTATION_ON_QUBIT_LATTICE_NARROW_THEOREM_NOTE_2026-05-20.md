# Kraus–Choi Representation on the Qubit-Lattice CPTP Map Algebra (Narrow)

**Date:** 2026-05-20
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Apply the Kraus 1971 operator-sum representation theorem and
the Choi 1975 CP-map characterization theorem to the qubit-lattice
CPTP map algebra as a framework-internal narrow theorem. Same
pattern as `cl3_complexification_split_narrow_theorem_note_2026-05-10`
(applying standard Clifford-algebra theorem to `Cl(3,0)`) and the
companion `GLEASON_ON_QUBIT_LATTICE_*` + `BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_*`
notes (applying standard Gleason/Busch to the qubit-lattice substrate).

## Honest scope

This note **does not re-prove Kraus' or Choi's theorems from scratch.**
It applies these standard finite-dim C*-algebra theorems to the
framework's specific algebra `⊗_x M_2(ℂ)` as a narrow positive_theorem.
The framework's contribution is the application-to-its-substrate
content, not the theorems themselves.

If audit-retained, this lifts the external-textbook admission of
Kraus/Choi from the
[`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md)
chain (landed on main with Kraus 1971 and Choi 1975 cited as standard
math), enabling that note's chain to potentially retain at higher
grade rather than bounded support.

## Claim

Let `Λ ⊂ Z^3` be a finite region. The qubit-lattice operator algebra
is `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ) ≅ M_d(ℂ)` for `d = 2^|Λ|`.

**Theorem (Kraus 1971 + Choi 1975, applied).** A linear map
`Φ: A_Λ → A_Λ` is completely positive (CP) if and only if it has an
**operator-sum representation**

```text
Φ(X) = Σ_r K_r · X · K_r†                                                (1)
```

for a finite (or countable, with appropriate convergence) family of
**Kraus operators** `{K_r} ⊂ A_Λ`. The map is additionally
**trace-preserving (TP)** iff `Σ_r K_r† K_r = 𝟙`. Equivalently
(Choi 1975), `Φ` is CP iff its **Choi matrix**

```text
C_Φ := (𝟙 ⊗ Φ) (|Ω⟩⟨Ω|)                                                 (2)
```

(where `|Ω⟩ = Σ_i |i⟩|i⟩` is the maximally entangled vector on
`A_Λ ⊗ A_Λ`) is positive semidefinite.

The framework's qubit-lattice algebra `A_Λ = ⊗_x M_2(ℂ)` is a
finite-dim matrix algebra (`M_d(ℂ)` with `d = 2^|Λ|`), so Kraus' and
Choi's hypotheses are satisfied and the standard theorems apply.

## Setup

By A1+A2 of
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md), the
per-site operator algebra is `M_2(ℂ)`. For finite `Λ ⊂ Z^3`:

- `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)_x ≅ M_d(ℂ)` for `d = 2^|Λ|`
- `A_Λ ⊗ A_Λ ≅ M_{d²}(ℂ)` — joint algebra used for the Choi matrix

A **linear map** `Φ: A_Λ → A_Λ` is **completely positive (CP)** iff
for every `n ≥ 1`, the extension `𝟙_n ⊗ Φ: M_n(ℂ) ⊗ A_Λ → M_n(ℂ)
⊗ A_Λ` is positivity-preserving. It is **trace-preserving (TP)** iff
`Tr(Φ(X)) = Tr(X)` for all `X ∈ A_Λ`.

CPTP maps describe physical state evolution: dynamics, measurements
(unconditional update over outcomes), decoherence, record formation
(per the framework's existing record lane).

## Step 1 — Choi's theorem (cited)

**Choi's Theorem** (Choi 1975 *Lin. Alg. Appl.* 10, 285):
A linear map `Φ: M_d(ℂ) → M_d(ℂ)` is CP iff its Choi matrix
`C_Φ ∈ M_{d²}(ℂ)` (constructed via the Choi–Jamiołkowski isomorphism
in equation (2)) is positive semidefinite.

The Choi matrix construction:
- `|Ω⟩ = (1/√d) Σ_i |i⟩|i⟩` (maximally entangled vector on
  `ℂ^d ⊗ ℂ^d`)
- `C_Φ = (𝟙 ⊗ Φ)(|Ω⟩⟨Ω|)`
- `Φ(X) = Tr_1[(X^T ⊗ 𝟙) C_Φ]` (inverse map)

CP ↔ positive Choi matrix is the **Choi–Jamiołkowski isomorphism**
between CP maps and positive bipartite operators.

## Step 2 — Kraus' theorem (cited)

**Kraus' Theorem** (Kraus 1971 *Ann. Phys.* 64, 311):
A linear map `Φ: M_d(ℂ) → M_d(ℂ)` is CP iff it has an
operator-sum representation

```text
Φ(X) = Σ_{r=1}^{r_*} K_r · X · K_r†                                     (1)
```

for some `r_* ≤ d²` and Kraus operators `K_r ∈ M_d(ℂ)`. The map is
**TP** iff `Σ_r K_r† K_r = 𝟙_d`.

Proof: spectral decomposition of the Choi matrix
`C_Φ = Σ_r |v_r⟩⟨v_r|` (positive iff CP, by Step 1) gives Kraus
operators `K_r = √d · vec^{-1}(|v_r⟩)` where `vec^{-1}` reverses
the column-stacking isomorphism `M_d(ℂ) → ℂ^{d²}`.

The Kraus representation is **unique up to unitary mixing** of the
Kraus operators (Naimark / Kraus uniqueness).

## Step 3 — Application to the qubit-lattice substrate

The qubit-lattice algebra `A_Λ = ⊗_x M_2(ℂ)` is isomorphic to
`M_d(ℂ)` with `d = 2^|Λ|`. So:

- Kraus' theorem applies directly: any CPTP map on `A_Λ` has an
  operator-sum representation with Kraus operators `K_r ∈ A_Λ` and
  `Σ_r K_r† K_r = 𝟙`.
- Choi's theorem applies directly: CP iff Choi matrix positive
  semidefinite.

In the **thermodynamic limit** `Λ → Z^3`, the quasi-local algebra
`A = ⊗_{x ∈ Z^3} M_2(ℂ)` is a UHF C*-algebra of type `2^∞`.
Kraus/Choi extend via the standard quasi-local construction:
finite-region CPTP maps approximate any quasi-local CPTP map via the
inductive limit (Bratteli–Robinson Vol I.6). The thermodynamic-limit
Kraus representation is consistent with the framework's existing
record-formation structure.

## Step 4 — Consistency with the framework's record lane

The framework's
[`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md)
identifies the persistent-record outcomes as Kraus operators `K_r`
on the system algebra, with the unconditional update being CPTP:

```text
σ → E(σ) = Σ_r K_r · σ · K_r†                                            (3)
```

Step 1–2 (Kraus/Choi theorems) supply the *theorem* that this is
the unique form of any CPTP map. Step 3 verifies the theorems apply
on the qubit-lattice substrate. Together, the record-as-Kraus
identification of `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE` has
framework-internal upstream theorem support, not just textbook
admission.

## What this closes

- **The Kraus 1971 / Choi 1975 external-textbook admissions** in
  the persistent-record-as-Kraus chain. These now have framework-
  internal narrow-theorem status on the qubit-lattice substrate.
- **Combined with the Gleason + Busch companion notes** (PR #1631)
  and the Greechie sequential-product narrow theorem (PR #1626),
  the Born derivation chain has framework-internal narrow-theorem
  status for all its standard-math admissions.

## What this does not close

- **Re-derivation of Kraus' or Choi's theorems from scratch** —
  cited as standard finite-dim C*-algebra content; not re-proved
  here.
- **The CPTP-map identification of specific record-formation
  dynamics** — that's the framework's record-lane derivation
  (existing in
  `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` retained_bounded and
  the landed `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20`).
- **The thermodynamic-limit extension** to the full quasi-local
  algebra — sketched in Step 3 via Bratteli–Robinson construction;
  full rigorous extension is a standard but separate result.

## Admitted inputs

1. **Kraus 1971 operator-sum representation theorem** on finite-dim
   matrix algebras `M_d(ℂ)` — standard math (*Ann. Phys.* 64, 311).
2. **Choi 1975 CP-map characterization theorem** via Choi matrix /
   Choi–Jamiołkowski isomorphism — standard math (*Lin. Alg. Appl.*
   10, 285).
3. **Standard finite-dim C*-algebra theory** (positive operators,
   spectral decomposition, tensor products of matrix algebras) —
   universal background.
4. **Bratteli–Robinson quasi-local construction** for the
   thermodynamic-limit extension to UHF type `2^∞` — standard math
   for operator-algebraic quantum statistical mechanics.

## Risk classification

This is a `positive_theorem` candidate at the narrow-theorem
granularity. Standard Kraus/Choi theorems applied to the framework's
specific algebra `⊗_x M_2(ℂ) ≅ M_d(ℂ)`. The narrow contribution is
the explicit application to the qubit-lattice substrate plus the
verification that the standard theorems' hypotheses hold there.

Granularity matches retained narrow theorems (positive_theorem,
retained) that apply standard math to the framework's specific
operator structure (e.g., `cl3_complexification_split` applies
standard Clifford theorem; `cl3_faithful_irrep_dim_two` applies
standard representation theory).

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md) — landed companion that this narrow theorem supplies the upstream theorem support for

**Upstream standard-math imports** (named non-derivation):

- Kraus 1971 *Ann. Phys.* 64, 311 — operator-sum representation theorem
- Choi 1975 *Lin. Alg. Appl.* 10, 285 — CP-map / Choi-matrix characterization
- Bratteli–Robinson 1979/1981 *Operator Algebras and Quantum Statistical Mechanics* — quasi-local construction in thermodynamic limit
- Nielsen–Chuang Ch.8 — modern textbook treatment of quantum operations

**Plain-text pointer references** (NOT load-bearing deps):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer of the Kraus structure for record-conditional Born evaluations
- `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` (retained_bounded) — existing record-lane structure that the Kraus operators model

## What this file is not

- Not a re-derivation of Kraus' or Choi's theorems (cited as standard math)
- Not a closure of the record-formation derivation (separate framework lane)
- Not an automatic promotion of record-as-Kraus or Born to retained (verdicts owned by audit lane)
- Not a numerical-prediction change
