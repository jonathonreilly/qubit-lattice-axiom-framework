# Lüders Rule from Compositional Bayesian Consistency

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Supplies (proposed):** a bounded candidate replacement for one of
the admitted inputs in
`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — the
Lüders rule import for record-conditioning state updates. The Born
note is a downstream consumer, not an upstream authority for this row.

## Claim

On the qubit-lattice operator algebra defined by
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) (A1+A2,
giving per-site `M_2(ℂ)` operator algebra and `Z^3` substrate), the
**unique** state-update rule for record conditioning that satisfies
the four standard consistency requirements

- **(U1)** Positivity preservation: `σ ≥ 0 ⇒ σ' ≥ 0`
- **(U2)** Normalization preservation: `Tr(σ) = 1 ⇒ Tr(σ') = 1`
- **(U3)** Probability consistency: for any subsequent measurement
  effect `E`, the joint probability decomposes as `p(P then E) =
  p(P) · p(E | P)` (Bayes rule on sequential measurements)
- **(U4)** Compositional consistency: recording `P_1` then `P_2` gives
  the same posterior state as recording `P_2 · P_1` once

is the **Lüders rule**: for a projection-valued record `P`,

> `σ → σ|_P = (P σ P) / Tr(P σ P)`

and more generally, for a Kraus operator `K`,

> `σ → σ|_K = (K σ K†) / Tr(K σ K†)`

If independently retained, this supplies the Lüders-rule input to the
Born-rule support / repair route under Gleason–Busch on the pre-record
reference. It does not retag or promote the Born row by itself.

## Setup

By A1+A2, the per-site operator algebra is `M_2(ℂ)` (equivalently
`Cl(3,0)` as a real algebra), composing over `Z^3` by standard
C*-tensor product. For a finite region `Λ ⊂ Z^3`, the local
operator algebra is `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` acting on
`H_Λ = ⊗_{x ∈ Λ} ℂ²`.

A **state** on `A_Λ` is a density matrix `σ` (`σ ≥ 0`, `Tr(σ) = 1`).
A **record** corresponds to a measurement outcome — formally, a
positive operator `P` (typically a projection, more generally a
Kraus operator) representing which outcome was obtained.

The **state-update problem**: given a pre-record state `σ` and a
record outcome `P`, what is the post-record state `σ|_P`?

## Step 1 — Lüders rule from (U3) Bayes consistency

Apply (U3) Bayes rule to two sequential measurements. Let the first
measurement record outcome `P` (rank-1 projection for clarity;
generalizes to higher rank). Let the second measurement be POVM
`{E_i}` with `Σ_i E_i = I`. By Bayes:

```text
p(P then E_i)  =  p(P) · p(E_i | P)                                      (1)
```

Using the standard state/effect trace pairing on the operator algebra
(the same standard-math probability representation used by the Born
route):

```text
p(P then E_i)  =  Tr(σ · M_{P, E_i})                                     (2)
```

for some effect `M_{P, E_i}` representing the joint "P then E_i"
outcome. Standard sequential-measurement composition gives
`M_{P, E_i} = P E_i P` (this is the *standard* sequential-measurement
combination; it is forced by associativity of the effect algebra
and the requirement that `M_{P, I} = P` and `M_{I, E_i} = E_i`).

So

```text
p(P then E_i)  =  Tr(σ · P E_i P)  =  Tr(P σ P · E_i)                    (3)
```

(using the cyclicity of trace). Substituting in (1):

```text
Tr(P σ P · E_i)  =  p(P) · p(E_i | P)  =  Tr(σ · P) · Tr(σ|_P · E_i)     (4)
```

For (4) to hold for **every** effect `E_i`, we must have

```text
Tr(σ|_P · E_i)  =  Tr( P σ P · E_i ) / Tr(σ · P)    ∀ E_i                (5)
```

Since `{E_i}` ranges over all POVM effects on `A_Λ` (the trace dual
of which is the full operator space), equality of these linear
functionals forces

```text
σ|_P  =  (P σ P) / Tr(P σ P)                                             (6)
```

This is the Lüders rule. (U3) Bayes consistency alone, combined with
standard sequential-effect composition `M_{P,E} = P E P`, forces (6).

## Step 2 — (U1), (U2) are corollaries

The Lüders rule (6) automatically satisfies:

- **(U1) Positivity:** `σ ≥ 0 ⇒ P σ P ≥ 0` (sandwich preserves
  positivity), so `σ|_P ≥ 0` after normalization.
- **(U2) Normalization:** `Tr(σ|_P) = Tr(P σ P) / Tr(P σ P) = 1` by
  construction.

These are immediate from the form of (6); they are properties of the
Lüders rule, not independent constraints.

## Step 3 — (U4) compositional consistency

Apply Lüders twice for sequential records `P_1` then `P_2`:

```text
(σ|_{P_1})|_{P_2}  =  (P_2 (σ|_{P_1}) P_2) / Tr((σ|_{P_1}) · P_2)         (7)
```

Substituting (6):

```text
                    =  (P_2 (P_1 σ P_1) P_2 / Tr(P_1 σ P_1)) /
                       Tr((P_1 σ P_1) · P_2 / Tr(P_1 σ P_1))
                    =  (P_2 P_1 σ P_1 P_2) / Tr(P_2 P_1 σ P_1 P_2)
                    =  ((P_2 P_1) σ (P_2 P_1)†) / Tr((P_2 P_1) σ (P_2 P_1)†)
                                                                          (8)
```

This is exactly Lüders applied once to the composite operator
`P_2 · P_1`. Compositional consistency (U4) is therefore automatically
satisfied by the Lüders form derived from (U3).

## Step 4 — Uniqueness

Any state-update rule `σ → f(σ, P)` satisfying (U1)–(U4) must reproduce
(6) by the argument in Step 1, since (U3) alone forces (6) up to the
ambiguity in `M_{P, E}`. The standard sequential-effect composition
`M_{P, E} = P E P` is the only one consistent with associativity of
the effect algebra and the boundary conditions `M_{P, I} = P`,
`M_{I, E} = E`. Therefore Lüders is the unique update rule satisfying
(U1)–(U4) on the standard effect-algebra structure of `M_2(ℂ)`-based
operator algebras.

## What this can close after audit

- **The Lüders-import admission** in the Born derivation note
  (`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
  Step 3 admitted Lüders 1951 / Cassinelli-Lahti 1995 as the standard
  measurement-update rule; this note derives the bounded replacement
  from (U1)–(U4) plus the standard sequential-effect composition
  import). Closure is conditional on independent audit of this row and
  any later dependency-chain update on the Born note.

## What this does not close

- **The standard sequential-effect composition `M_{P, E} = P E P`**
  is still admitted as the canonical operator-algebraic
  sequential-measurement composition. Alternative compositions (e.g.,
  "minimal disturbance" rules of Marlow, Wright) would give different
  update rules but at the cost of associativity in the effect
  algebra. The argument here treats `M_{P, E} = P E P` as the
  standard composition; if a reviewer disputes this, an additional
  derivation tying it to `M_2(ℂ)`-internal operator-product
  consistency would be needed.
- **The remaining four admitted inputs of the Born derivation**:
  Gleason 1957, Busch 2003 POVM extension, no-extra-structure
  pre-record identification, and persistent-record → Kraus operator
  identification. Each is a separate admission. This note addresses
  only the Lüders input.

## Admitted inputs

1. **(U1)–(U4) as the standard consistency requirements** on
   measurement update rules — these are mainstream-textbook
   foundational conditions (Cassinelli-Lahti 1995, Busch et al. 1995
   *Operational QM*, Heinosaari-Ziman 2012).
2. **Standard sequential-effect composition** `M_{P, E} = P E P` for
   the joint "P then E" measurement effect. Standard
   operator-algebraic composition; required by associativity of the
   effect algebra.
3. **State/effect trace-pairing probability representation** on the
   finite-region operator algebra. This is standard operator-algebraic
   probability machinery, not supplied by the downstream Born note.

## Risk classification

This is a `bounded_theorem` candidate. Steps 1–4 are textbook
operator-algebraic derivations (Cassinelli-Lahti 1995 Ch.3 covers
essentially the same content). The narrow theorem here is identifying
that the standard (U1)–(U4) requirements force Lüders on the qubit
lattice algebra.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra and `Z^3` substrate)

**Upstream standard-math imports** (named non-derivation; not framework rows):

- Cassinelli-Lahti 1995 *Found. Phys.* 25, 1395 — Lüders rule from (U1)–(U4)
- Busch-Lahti-Mittelstaedt 1995 *Operational Quantum Physics* — effect-algebra consistency conditions
- Heinosaari-Ziman 2012 *The Mathematical Language of Quantum Theory* — modern textbook treatment of measurement update
- Standard operator-algebraic sequential-effect composition `M_{P, E} = P E P`

**Plain-text pointer references** (NOT load-bearing deps; deliberately not markdown links to avoid polluting the audit dependency graph):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer that may cite this row after independent audit / dependency-chain update
- `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` — relevant for the persistent-record → Kraus operator identification (separate admitted input handled in the companion `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`)
- Marlow / Wright "minimal disturbance" rule literature — alternative measurement-update rules; not adopted here

## What this file is not

- Not a derivation of Gleason–Busch from A1+A2.
- Not a derivation of the standard sequential-effect composition (admitted).
- Not a numerical-prediction change.
- Not a unilateral retagging of the Born note. The bounded-theorem
  candidacy depends on independent audit acceptance of the (U1)–(U4)
  framing and the sequential-effect composition import.
