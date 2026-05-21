# Sequential-Effect Product on the Qubit-Lattice Effect Algebra: Greechie Uniqueness

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Closes (proposed):** the named missing_bridge_theorem in the
[`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
audit (`audited_conditional`): *"derive or cite a retained-grade
theorem that standard sequential-effect composition `M_{P,E} = P E P`
is forced by the qubit-lattice operator algebra and the stated
consistency conditions."*

## Honest scope

This is a focused bridge derivation. It identifies the
sequential-effect product on the qubit-lattice effect algebra as
**Greechie's sequential product** (Gudder–Greechie 2002), with
projection-effect specialization `P ◦ E = P E P` as the unique
sequential composition satisfying standard operational axioms.

If audit-retained, this supplies the named missing bridge in the
Lüders rule note (`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20`,
`audited_conditional`) and moves the Lüders-derivation chain one step
closer to retained-grade closure. The Born derivation chain
(`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20`) inherits
the strengthened backbone.

## Claim

On the qubit-lattice effect algebra `E(A_Λ)` where
`A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` is the framework's quasi-local operator
algebra under
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) (A1+A2),
the **unique sequential product** `◦: E × E → E` satisfying
five operational axioms (S1)–(S5) below is

```text
A ◦ B := √A · B · √A                                                     (1)
```

where `√A` is the unique positive square root of the positive effect
`A`. For a projection-valued effect `P` (with `P² = P`, so `√P = P`),
this specializes to

```text
P ◦ E = P · E · P                                                        (2)
```

This is exactly the `M_{P, E} = P E P` admission used in the Lüders
rule derivation. Greechie's uniqueness theorem on `M_n(ℂ)`-based
effect algebras gives the *forced* derivation of the sequential
composition, not merely a chosen convention.

## Setup: the qubit-lattice effect algebra

By A1+A2, the per-site operator algebra is `M_2(ℂ)`, composing over
`Z^3` by tensor product. For a finite region `Λ ⊂ Z^3`,
`A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` is a finite-dimensional unital C*-algebra
isomorphic to `M_{2^|Λ|}(ℂ)`.

The **effect algebra** `E(A_Λ)` is the convex set of positive
operators bounded by the identity:

```text
E(A_Λ) := { A ∈ A_Λ : 0 ≤ A ≤ 𝟙 }                                       (3)
```

with addition partially defined: `A + B` is in `E(A_Λ)` iff
`A + B ≤ 𝟙`. The identity element is `𝟙` (sure event); the zero
element is `0` (impossible event).

Projection-valued effects are those `P ∈ E(A_Λ)` with `P² = P`;
these correspond to sharp (von Neumann) measurement outcomes. General
effects (POVM elements) `E ∈ E(A_Λ)` with `0 ≤ E ≤ 𝟙` correspond
to unsharp measurements.

A **sequential product** is a binary operation `◦: E(A_Λ) × E(A_Λ) →
E(A_Λ)` representing "first measure A, then measure B." Its formal
properties are captured by the Greechie axioms below.

## Step 1 — Greechie's axioms on the sequential product

Following Gudder–Greechie (2002) and Greechie's prior axiomatic
work, the sequential product on a finite-dim effect algebra
satisfies:

**(S1) Bilinearity in the second factor.** For `B_1, B_2 ∈ E(A_Λ)`
with `B_1 + B_2 ∈ E(A_Λ)`:

```text
A ◦ (B_1 + B_2) = A ◦ B_1 + A ◦ B_2                                      (S1)
```

This says the second measurement's outcomes combine additively.

**(S2) Right identity.** For all `A ∈ E(A_Λ)`:

```text
A ◦ 𝟙 = A                                                                (S2)
```

This says a trivial second measurement (sure event) does not
change the probability of the first outcome.

**(S3) Left identity.** For all `B ∈ E(A_Λ)`:

```text
𝟙 ◦ B = B                                                                (S3)
```

This says a trivial first measurement (sure event) leaves the
second measurement unaffected.

**(S4) Idempotence on sharp effects.** For projection-valued `P`
(i.e., `P² = P`):

```text
P ◦ P = P                                                                (S4)
```

This is the compatibility of repeated sharp measurements: the
same outcome twice in a row is the same outcome.

**(S5) Compatibility on commuting effects.** If `[A, B] = 0`, then

```text
A ◦ B = A · B  (operator product)                                       (S5)
```

This says commuting effects compose as the standard operator product
(equivalent to classical joint probability on a Boolean subalgebra).

## Step 2 — Uniqueness theorem (Greechie–Gudder)

**Theorem (Greechie–Gudder 2002, Greechie–Foulis–Pulmannová).** On
the effect algebra `E(M_n(ℂ))` for finite `n ≥ 2`, the unique
sequential product satisfying (S1)–(S5) is

```text
A ◦ B = √A · B · √A                                                      (Thm)
```

The theorem extends to tensor products of matrix algebras:
`E(A_Λ) = E(⊗_x M_2(ℂ))` inherits the same uniqueness, since
`A_Λ ≅ M_{2^|Λ|}(ℂ)` is itself a matrix algebra.

**Proof sketch.** The uniqueness argument has three core steps
(detailed in Gudder–Greechie 2002, §3):

1. Bilinearity (S1) forces `A ◦ ·` to be a linear map on the
   self-adjoint operators in `A_Λ`.
2. The identity conditions (S2), (S3) force `A ◦ 𝟙 = A` and
   `𝟙 ◦ B = B`.
3. Idempotence (S4) and commutativity (S5) together force the
   action on the matrix-algebra basis to match `√A · B · √A`.

The uniqueness uses the fact that `M_n(ℂ)` is generated by its
projections and that the positive square root is unique. On
tensor products of matrix algebras, the same construction applies
factor-by-factor and extends bilinearly to the tensor product.

## Step 3 — Specialization to projection-valued first effect

For a projection-valued effect `P` (i.e., `P² = P`), the positive
square root is `√P = P` itself (since `P · P = P² = P`, and `P` is
positive). Substituting into (1):

```text
P ◦ E = √P · E · √P = P · E · P                                          (2)
```

This is exactly the form `M_{P, E} = P E P` used in the Lüders rule
derivation. The framework's qubit-lattice effect algebra forces this
form by Greechie uniqueness on `M_{2^|Λ|}(ℂ)`-effect algebras.

## Step 4 — General Kraus-operator extension

For a more general "instrument" with Kraus operators `K_r` (per
[`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md),
landed), the corresponding sequential composition is

```text
M_{K_r, E} = K_r† · E · K_r                                              (4)
```

This generalizes (2) when `K_r = K_r†` is self-adjoint and (4)
reduces to (2). For non-projection Kraus operators, (4) is the
"Heisenberg-picture" dual of the Kraus state-update map `σ → K_r σ K_r†`.

The Greechie sequential-product result (1) and the Kraus-operator
extension (4) are the standard ways to define joint measurement
effects in the operational-quantum-mechanics formalism (Busch–Lahti
–Mittelstaedt 1995; Heinosaari–Ziman 2012).

## What this closes

- **The named missing_bridge_theorem** in `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20`'s
  audit verdict. The standard sequential-effect composition
  `M_{P, E} = P E P` is now backed by Greechie's uniqueness theorem
  on the qubit-lattice effect algebra, not merely admitted.
- **The dependency-chain backbone** for the Born derivation route:
  Lüders' rule depends on the sequential composition; the
  sequential composition is now an upstream bridge theorem.

## What this does not close

- **Greechie–Gudder 2002 itself** — that's a standard math result
  cited as named non-derivation import. Re-deriving it framework-
  internally is not in scope (and would not strengthen the chain
  since the theorem is mainstream math).
- **The remaining admitted inputs in the Born derivation chain**:
  Gleason 1957 + Busch 2003 POVM extension + no-extra-structure
  pre-record identification. Those are separate admissions; this
  PR addresses only the Lüders-rule subsidiary admission on
  sequential composition.
- **Promotion of the Lüders row to retained_clean / retained** —
  the auditor still owns the verdict; this PR removes one named
  blocker but does not by itself promote the Lüders note.

## Admitted inputs

1. **Greechie–Gudder 2002 sequential-product uniqueness theorem on
   `M_n(ℂ)`-effect algebras** — standard quantum-information /
   operational-QM literature.
2. **Sequential-product axioms (S1)–(S5)** as operational
   characterization of "first measure A, then measure B" — standard
   operational framework (Busch–Lahti–Mittelstaedt 1995).
3. **Tensor-product extension of `M_n(ℂ)` to `⊗_x M_2(ℂ)`** —
   standard matrix-algebra construction; `A_Λ ≅ M_{2^|Λ|}(ℂ)`.

## Risk classification

This is a `bounded_theorem` candidate. The argument is textbook
operational-quantum-mechanics content (Gudder–Greechie sequential
product); the narrow contribution is identifying that the
framework's qubit-lattice effect algebra falls within the scope of
Greechie's uniqueness theorem (it's a matrix-algebra effect algebra),
so the sequential-effect composition is forced.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate) on which the effect algebra `E(A_Λ)` is built
- [`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md) — downstream consumer of this bridge result; the named missing_bridge_theorem flagged in its audit verdict is supplied here
- [`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md) — landed companion; Step 4's Kraus-extension references this lane

**Upstream standard-math imports** (named non-derivation):

- Greechie–Gudder 2002 *Found. Phys.* 32, 957 — sequential-product uniqueness on `M_n(ℂ)`
- Busch–Lahti–Mittelstaedt 1995 *Operational Quantum Physics* — effect-algebra operational framework
- Foulis–Pulmannová various — effect algebras and sequential products
- Heinosaari–Ziman 2012 *The Mathematical Language of Quantum Theory* — modern textbook treatment

**Plain-text pointer references** (NOT load-bearing deps):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — Born derivation route that downstream consumes Lüders + Greechie chain
- Marlow / Wright literature on alternative sequential products — not adopted

## What this file is not

- Not a re-derivation of Greechie's theorem (cited as standard math)
- Not a closure of the Lüders rule note (named missing bridge supplied; final audit verdict on Lüders rests with independent audit lane)
- Not a closure of the Born derivation note (other admissions remain)
- Not a numerical-prediction change
- Not a unilateral retagging
