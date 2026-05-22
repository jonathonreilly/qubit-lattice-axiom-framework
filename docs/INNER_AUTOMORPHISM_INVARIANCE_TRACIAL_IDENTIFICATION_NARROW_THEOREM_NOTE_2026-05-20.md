# Inner-Automorphism Invariance Identifies Pre-Record State as Tracial (Narrow)

**Date:** 2026-05-20
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Supply the named `missing_bridge_theorem` flagged in the
audit verdict on
`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`
(`audited_conditional` on main):

> *"provide a retained-grade theorem or accepted framework rule
> deriving the no-extra-structure identification of the unique tracial
> state with the pre-record reference, rather than admitting it as a
> premise."*

This note records the **framework rule** half ("accepted framework
rule") explicitly, and then applies the **standard inner-automorphism-
invariance → tracial-state** theorem on type-I factors to identify the
pre-record reference with the unique tracial state on the qubit-lattice
substrate.

## Honest scope

This note **does not re-prove the inner-automorphism-invariance →
tracial-state theorem from scratch.** It applies the standard
finite-dim type-I factor result (Tomita–Takesaki theory background,
Dixmier 1981, Takesaki I §IV) to the framework's specific finite-region
algebras `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ) ≅ M_{2^|Λ|}(ℂ)`. The framework rule
("pre-record state is invariant under all inner unitaries") is recorded
as a single accepted framework principle, distinct from A1+A2.

If audit-retained, this row supplies a candidate upstream support
for the `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE` identification
step, addressing the named missing-bridge from that note's
`audited_conditional` verdict. It does not retag the parent row by
itself.

## Claim

On the qubit-lattice substrate
([`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md):
A1 = qubit at every site = `M_2(ℂ)`; A2 = `Z^3`), define the
**pre-record framework rule**:

```text
(PRR)  For every finite Λ ⊂ Z^3, the pre-record reference state
       ρ_ref|_Λ satisfies   U · ρ_ref|_Λ · U† = ρ_ref|_Λ
       for every unitary  U ∈ U(A_Λ).                                    (1)
```

In words: the pre-record reference state is invariant under all inner
unitary automorphisms of every finite-region algebra. This is the
framework's commitment that *no record yet exists* — there is no
preferred basis, direction, or eigenstate distinguishing one unitary
frame from another.

**Theorem (narrow).** The unique density matrix `ρ ∈ A_Λ` satisfying
(1) is the maximally mixed state:

```text
ρ_ref|_Λ = I_{2^|Λ|} / 2^|Λ|                                            (2)
```

equivalently, the normalized trace `τ_Λ(O) = Tr(O) / 2^|Λ|` on the
finite-region algebra. Composed with the
[`POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20`](POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
inductive-limit construction, this fixes `ρ_ref = ⊗_{x ∈ Z^3} (I_2 / 2)`
on the quasi-local UHF algebra.

This addresses the missing-bridge verdict: (PRR) is the **accepted
framework rule**, and (2) follows from the **standard math** with no
further admitted premise.

## Setup

By A1+A2, for each finite `Λ ⊂ Z^3`:
- `H_Λ = ⊗_{x ∈ Λ} ℂ²`, complex Hilbert space of dim `d = 2^|Λ|`
- `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ) ≅ M_d(ℂ)`, simple matrix algebra (type-I factor)
- `U(A_Λ)` = unitary group of `A_Λ`

A **state** is a density matrix `ρ ∈ A_Λ` with `ρ ≥ 0`, `Tr ρ = 1`.

The **inner automorphism group** is `Inn(A_Λ) = { Ad(U) : U ∈ U(A_Λ) }`
acting on `A_Λ` by `Ad(U)(X) := U X U†` and (dually) on states by
`U · ρ · U†`.

The **invariant states** are those fixed by all of `Inn(A_Λ)`:
```text
Fix(Inn(A_Λ)) := { ρ : U ρ U† = ρ for all U ∈ U(A_Λ) }                  (3)
```

## Step 1 — Framework rule (PRR) recorded explicitly

The note's contribution at this step is to **record (PRR) explicitly
as a framework rule**. The motivation is:

1. **Pre-record means no information.** Before any record formation,
   no measurement has been performed, no apparatus has triggered, no
   pointer state has been correlated with the system. The state of the
   system carries no information about which basis/direction/eigenstate
   is preferred.
2. **No-information ⇒ unitary-frame-independent.** A choice of unitary
   `U ∈ U(A_Λ)` is a choice of "frame" — a basis rotation on the
   algebra. If the pre-record state has no information about basis, it
   must be the same in every unitary frame: `U ρ U† = ρ`.
3. **(PRR) formalizes (1)–(2).** The pre-record state is invariant
   under the inner automorphism group.

This is the framework's principled commitment about what "pre-record"
means. It is *not* derived from A1+A2 alone, but it is a single,
clean, motivated framework rule — not a free numerical parameter or a
preferred-structure premise.

## Step 2 — Standard theorem: inner-aut-invariant state on type-I factor is tracial

**Standard result** (Tomita–Takesaki theory; Dixmier 1981
*Les algèbres d'opérateurs* §1.7; Takesaki I §IV.5; modern textbook
treatment in Bratteli–Robinson I §2.6.4):

> On a type-I factor `M = M_d(ℂ)`, the unique state `ρ` satisfying
> `U ρ U† = ρ` for every unitary `U ∈ U(M)` is the **normalized trace**
> `τ = Tr / d`, equivalently the maximally mixed density matrix
> `ρ = I_d / d`.

**Proof sketch.** Schur's lemma applied to the action of `U(d)` on
itself: any operator commuting with every `U ∈ U(d)` is a multiple of
the identity. Concretely, for any `X ∈ M_d(ℂ)`, the condition
`U X U† = X` for all `U` means `[U, X] = 0` for all `U`, which by
Schur forces `X = c · I_d` for some `c ∈ ℂ`. For a density matrix
(`Tr ρ = 1`, `ρ ≥ 0`), this fixes `c = 1/d`, so `ρ = I_d / d`. ∎

This is **standard math**: Schur's lemma + the dual action of
`U(d)` on density matrices.

## Step 3 — Application to qubit-lattice finite regions

For each finite `Λ ⊂ Z^3`, `A_Λ ≅ M_{2^|Λ|}(ℂ)` is a type-I factor by
Setup. By Step 2's standard theorem:

```text
Fix(Inn(A_Λ)) = { I_{2^|Λ|} / 2^|Λ| }                                   (4)
```

i.e., the **unique** state invariant under all inner automorphisms of
`A_Λ` is the maximally mixed state.

Combining with (PRR):

```text
ρ_ref|_Λ ∈ Fix(Inn(A_Λ))   (by PRR)
        = { I_{2^|Λ|} / 2^|Λ| }   (by Step 2)
       ⟹ ρ_ref|_Λ = I_{2^|Λ|} / 2^|Λ|                                   (5)
```

This identifies the pre-record reference on every finite region with
the maximally mixed state. ∎

## Step 4 — Extension to the quasi-local UHF algebra

The finite-region family `{ρ_ref|_Λ}` from (5) is compatible under
nested restriction (`ρ_ref|_{Λ_1}` is the partial trace of
`ρ_ref|_{Λ_2}` for `Λ_1 ⊂ Λ_2`, since
`Tr_{Λ_2 ∖ Λ_1}(I_{2^|Λ_2|} / 2^|Λ_2|) = I_{2^|Λ_1|} / 2^|Λ_1|`).

By the inductive-limit construction handled in the companion
[`POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20`](POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md),
the compatible family extends to the **unique tracial state** `τ_∞`
on the quasi-local UHF algebra `A = ⊗_{x ∈ Z^3} M_2(ℂ)`. Equivalently,
`ρ_ref = ⊗_{x ∈ Z^3} (I_2 / 2)`.

## Step 5 — Equivalent characterizations

The pre-record reference identified by (PRR) + Step 2 admits the
equivalent characterizations recorded in the parent note's Step 4:

- (C1) **Tracial property:** `τ(AB) = τ(BA)` for all `A, B ∈ A`
- (C2) **Inner-automorphism invariance:** `τ(U A U†) = τ(A)` for every
       unitary `U` (this is (PRR) at the state level)
- (C3) **One-point Pauli expectation vanishing:** `τ(σ_a^x) = 0`
- (C4) **Maximum von Neumann entropy:** `S(ρ_Λ) = |Λ| log 2`
- (C5) **Maximal symmetry:** invariant under `U(H_Λ)` by inner aut

(C1)–(C5) are all equivalent on the finite-dim factor. (PRR) selects
the same state by (C2) directly.

## What this can support after audit

- **The no-extra-structure identification step** flagged on
  `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`'s
  `audited_conditional` verdict. If retained, this row supplies the
  named `missing_bridge_theorem` via the (PRR) framework rule plus
  the standard inner-aut-invariance theorem.
- **Companion to the Powers-UHF + Tomita support** already in the
  Born/measurement narrow-theorem suite. The chain becomes:
  - (PRR) + Step 2 (this note) → unique tracial state at every finite Λ
  - Tomita tensor-trace → factorization on disjoint regions
  - Powers UHF → inductive-limit extension to quasi-local algebra
  - Born derivation via Gleason–Busch on `ρ_ref` (downstream)

## What this does not close

- **Re-derivation of Schur's lemma / Tomita–Takesaki content** —
  standard math, not re-proved here.
- **Justification of (PRR) below A1+A2** — (PRR) is the accepted
  framework rule. The note's contribution is to make it explicit
  rather than burying it as an unwritten "no-extra-structure"
  meta-principle. (PRR) is a principled commitment about what
  "pre-record" means, not a derivation from A1+A2.
- **Promotion of the parent tracial-derivation row** — the auditor
  still owns the verdict.
- **The Wilson-measure / `ρ_ref` Radon-Nikodym compatibility check**
  — separate retained_bounded row handled in
  `RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md`.

## Admitted inputs

1. **Framework rule (PRR):** the pre-record reference state is
   invariant under every inner unitary automorphism on every finite
   region. Single principled commitment about the meaning of
   "pre-record" on the qubit-lattice substrate. This is the note's
   explicit framework-rule admission.
2. **Standard inner-aut-invariance → tracial theorem on
   `M_d(ℂ)`** — Schur's-lemma-level finite-dim operator-algebra
   content (Dixmier 1981 §1.7; Takesaki I §IV.5;
   Bratteli–Robinson I §2.6.4). Cited as named non-derivation
   standard math.
3. **Inductive-limit extension to UHF type `2^∞`** — handled by the
   companion `POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`,
   not re-derived here.

## Risk classification

`positive_theorem` candidate at narrow-theorem granularity. Standard
type-I factor result (inner-aut-invariant state = trace) applied to
the framework's specific finite-region matrix algebras, plus an
explicit framework rule (PRR). The narrow contribution is:

1. Making (PRR) explicit as a framework rule rather than admitting
   a meta-principle.
2. Verifying that `A_Λ = M_{2^|Λ|}(ℂ)` is a type-I factor where
   the standard theorem applies cleanly.
3. Combining (PRR) + standard theorem → tracial identification.

Granularity matches retained narrow theorems
(`cl3_complexification_split_narrow_theorem_note_2026-05-10`,
landed Gleason / Busch / Kraus-Choi / Powers / Tomita / Stinespring
qubit-lattice companions): standard math applied to the framework's
specific operator structure, plus a single framework principle when
needed for the identification.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) — landed companion (audited_conditional) whose named missing_bridge_theorem this row supplies
- [`POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) — companion narrow theorem handling the inductive-limit extension to UHF type `2^∞`

**Upstream standard-math imports** (named non-derivation):

- Dixmier 1981 *Les algèbres d'opérateurs* §1.7 — type-I factor trace uniqueness
- Takesaki I §IV.5 — modern treatment
- Bratteli–Robinson I §2.6.4 — modern textbook treatment of invariant states on factors
- Schur's lemma (standard finite-dim representation theory)

**Plain-text pointer references** (NOT load-bearing deps):

- `TOMITA_TENSOR_TRACE_ON_FINITE_DIM_MATRIX_NARROW_THEOREM_NOTE_2026-05-20.md` — companion narrow theorem on finite-region tensor-trace factorization
- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer of the tracial-state derivation chain that this note completes
- `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` — explanatory pointer; explains why this note's inner-aut route differs from the Jaynes max-entropy route (the latter closed negatively, the former opens positively)

## What this file is not

- Not a re-derivation of Schur's lemma / inner-aut-invariance theorem (cited as standard math)
- Not a closure of the parent tracial-derivation row (auditor-owned)
- Not a derivation of (PRR) below A1+A2 — (PRR) is the recorded framework rule
- Not a numerical-prediction change
