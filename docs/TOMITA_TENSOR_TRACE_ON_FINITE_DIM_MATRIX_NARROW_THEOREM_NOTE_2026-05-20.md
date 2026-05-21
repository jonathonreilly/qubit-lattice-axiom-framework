# Tomita Tensor-Trace Factorization on Finite-Dim Matrix Algebras (Narrow)

**Date:** 2026-05-20
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Apply Tomita's tensor-product trace factorization theorem
on simple finite-dim matrix algebras to the qubit-lattice finite-region
tensor factors. Standard math applied to the framework's substrate;
same pattern as `GLEASON_ON_QUBIT_LATTICE_*` companion notes.

## Honest scope

This note **does not re-prove Tomita's theorem from scratch.** It
applies the standard finite-dim simple-algebra tensor-traciality
result (Tomita, Tomita–Takesaki theory background, Dixmier 1981) to
the framework's specific finite-region algebra
`A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)`. Standard operator-algebra mathematics
applied to the framework's substrate.

If audit-retained, this gives downstream notes such as
`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20` a
qubit-lattice-scoped theorem to cite for the finite-region
tensor-trace factorization step. It does not eliminate the named
standard-math imports, prove the no-extra-structure identification,
or retag any downstream row by itself.

## Claim

For any finite `Λ_1, Λ_2 ⊂ Z^3` with `Λ_1 ∩ Λ_2 = ∅`, the
qubit-lattice finite-region algebras

```text
A_{Λ_1} = ⊗_{x ∈ Λ_1} M_2(ℂ),   A_{Λ_2} = ⊗_{x ∈ Λ_2} M_2(ℂ)             (1)
```

are simple finite-dim matrix algebras (isomorphic to `M_{2^|Λ_i|}(ℂ)`).
The combined algebra `A_{Λ_1 ∪ Λ_2} = A_{Λ_1} ⊗ A_{Λ_2}` is itself a
simple matrix algebra `M_{2^(|Λ_1|+|Λ_2|)}(ℂ)`.

**Theorem (Tomita tensor traciality on simple matrix algebras).** If
`τ_i` is the unique tracial state on `A_{Λ_i}` for `i = 1, 2`, then
the tensor-product state `τ = τ_1 ⊗ τ_2` is the unique tracial state
on `A_{Λ_1 ∪ Λ_2}`. Equivalently, every tracial state on
`A_{Λ_1 ∪ Λ_2}` **factorizes** on simple tensors:

```text
τ(A ⊗ B) = τ_1(A) · τ_2(B)   for A ∈ A_{Λ_1}, B ∈ A_{Λ_2}                (2)
```

This is the framework's Step 2 of the tracial-state derivation (the
tensor-product factorization step) backed by standard finite-dim
operator algebra rather than admitted.

## Setup

By A1+A2 of
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md), the
per-site operator algebra is `M_2(ℂ)`. Each finite region's algebra
`A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` is a **simple finite-dim matrix algebra**
isomorphic to `M_{2^|Λ|}(ℂ)`.

This is the **simple matrix algebra** setting where the tensor-traciality
factorization argument applies cleanly. For general C*-algebras
(non-simple, type II_1 factors, etc.), tracial states need not factor
on simple tensors. The framework's restriction to **simple finite-dim
matrix algebras** is what makes the factorization rigorous.

## Step 1 — Cite Tomita-style result

**Standard finite-dim result** (Tomita 1957 *Math. J. Okayama Univ.*
7, 35; Dixmier 1981 *Les algèbres d'opérateurs* §1.7; modern
treatment in Takesaki I §IV.5): on tensor products of simple
finite-dim matrix algebras `M_{n_1}(ℂ) ⊗ M_{n_2}(ℂ) ≅ M_{n_1 n_2}(ℂ)`,
the unique tracial state `τ = Tr/n_1 n_2` **factorizes** as

```text
τ(A ⊗ B) = (Tr A / n_1) · (Tr B / n_2) = τ_1(A) · τ_2(B)                 (3)
```

**Proof sketch.** The combined algebra `M_{n_1 n_2}(ℂ)` has unique
trace `Tr/n_1 n_2` by simple-algebra trace uniqueness (Dixmier). On
simple tensors `A ⊗ B`, the matrix trace decomposes as
`Tr_{n_1 n_2}(A ⊗ B) = Tr_{n_1}(A) · Tr_{n_2}(B)` (standard
elementary matrix-trace identity). Dividing by `n_1 · n_2` gives
(3).

For general (non-simple-tensor) elements, the result extends by
linearity.

## Step 2 — Application to the qubit-lattice substrate

For disjoint `Λ_1, Λ_2 ⊂ Z^3` with `|Λ_1| = n_1`, `|Λ_2| = n_2`:

- `A_{Λ_1} ≅ M_{2^{n_1}}(ℂ)` — simple matrix algebra
- `A_{Λ_2} ≅ M_{2^{n_2}}(ℂ)` — simple matrix algebra
- `A_{Λ_1 ∪ Λ_2} = A_{Λ_1} ⊗ A_{Λ_2} ≅ M_{2^{n_1+n_2}}(ℂ)` —
  simple matrix algebra

Applying Step 1's standard result:

```text
τ_{Λ_1 ∪ Λ_2}(A ⊗ B) = τ_{Λ_1}(A) · τ_{Λ_2}(B)                          (4)
```

for `A ∈ A_{Λ_1}`, `B ∈ A_{Λ_2}`. The unique tracial state on the
combined region factorizes as a product on simple tensors.

## Step 3 — Tightening the tracial-state derivation Step 2 proof

The downstream `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`
Step 2 uses the factorization (4) with Tomita-style tensor-trace
factorization as its standard-math input. For general C*-algebras and
general tracial states on a tensor product, factorization is not
automatic; the framework's finite-region simple-matrix-algebra context
is what makes this narrow factorization rigorous.

This narrow theorem supplies a candidate upstream Tomita/matrix-trace
application for that downstream step after independent audit.

## What this can support after audit

- **The finite-region tensor-trace factorization step** used by
  downstream pre-record-reference notes. If retained, this row lets
  those notes cite a qubit-lattice-scoped theorem for disjoint
  finite-region matrix factors rather than carrying only an
  unlocalized textbook reference.
- **Dependency-chain repair for the tracial-state / Born support
  lanes** after independent audit. This row does not promote those
  parent rows by itself.

## What this does not close

- **Re-derivation of Tomita's theorem from scratch** — cited as
  standard finite-dim operator-algebra content.
- **The no-extra-structure identification of `τ` with the
  pre-record reference state** — separate philosophical admission.
- **Non-simple tensor factorization** (e.g., type II_1 factors,
  non-finite-dim algebras) — not in scope; the framework's
  finite-region structure is finite-dim simple matrix algebra.
- **Promotion of the tracial-state row** — the auditor still owns the
  verdict.

## Admitted inputs

1. **Tomita 1957 tensor-traciality on finite-dim simple algebras** —
   standard math (*Math. J. Okayama Univ.* 7, 35).
2. **Standard matrix-trace tensor factorization** `Tr(A ⊗ B) =
   Tr(A) · Tr(B)` — elementary linear algebra.
3. **Dixmier 1981 finite-dim simple C*-algebra trace uniqueness** —
   standard math, also used in the Powers UHF companion.

## Risk classification

`positive_theorem` candidate at narrow-theorem granularity. Standard
Tomita / simple-algebra tensor-traciality applied to the framework's
specific finite-region matrix algebras. The narrow contribution is
the explicit application to the qubit-lattice substrate plus the
verification that the simple-matrix-algebra hypothesis holds (which
it does because each `A_Λ` is `M_{2^|Λ|}(ℂ)`).

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)

**Upstream standard-math imports** (named non-derivation):

- Tomita 1957 *Math. J. Okayama Univ.* 7, 35 — original tensor-traciality result
- Takesaki *Theory of Operator Algebras* Vol I §IV.5 — modern treatment
- Dixmier 1981 *Les algèbres d'opérateurs* — trace uniqueness reference

**Plain-text pointer references** (NOT load-bearing deps):

- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — downstream/companion note that may cite this row for finite-region tensor-trace factorization
- `POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md` — companion narrow theorem in this PR handling the UHF tracial uniqueness step
- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer of the tracial-state derivation chain that this note completes

## What this file is not

- Not a re-derivation of Tomita's theorem (cited as standard math)
- Not a closure of the no-extra-structure identification (separate admission)
- Not an automatic promotion of the tracial-state row (auditor-owned)
- Not a numerical-prediction change
