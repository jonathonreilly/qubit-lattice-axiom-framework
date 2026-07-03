# Busch POVM Extension on the Qubit-Lattice Effect Algebra (Narrow)

**Date:** 2026-05-20
**Type:** positive_theorem candidate (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Apply Busch's 2003 POVM-extension of Gleason's theorem to
the qubit-lattice effect algebra, covering the single-site dim-2
case (`|Λ| = 1`) that Gleason's original projection-lattice theorem
does not handle. It is a companion to the separate
`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`
candidate. The current source packet also includes a native
effect-Gleason authority bridge for the single-site qubit case:
[`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
with runner
[`scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py`](../scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py)
and cache
[`logs/runner-cache/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.txt`](../logs/runner-cache/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.txt).

## Honest scope

The original May packet stated the standard Busch 2003 / CFMR 2004
effect-Gleason theorem as a named mathematical input. The current
restricted packet routes the finite qubit-lattice claim through
framework-local finite operator algebra instead:

- for `|Λ| = 1`, the single-site qubit effect case is supplied by
  [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
  which reproves the load-bearing `m(E)=Tr(σE)` direction from the
  parent hypotheses (M1)-(M3) on `M_2(C)`;
- for `|Λ| >= 2`, the projection-lattice companion
  [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
  supplies the projection values, while POVM additivity plus spectral
  decomposition extends those values from projections to effects.

Busch 2003 and CFMR 2004 remain the parallel literature comparators
for the same theorem. They are no longer the only source-side route
for the finite qubit-lattice statement claimed here.

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

This is the finite-region effect-Gleason statement on the
qubit-lattice substrate, **including the `dim H = 2` single-site
case** that lies outside Gleason's original projection-lattice
theorem. The form `m(E) = Tr(σE)` is the Born-form representation for
POVM effect functionals on the qubit-lattice effect algebra at all
finite dimensions `2^|Λ| >= 2`, under the stated POVM-additivity
hypotheses.

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

## Step 2 — Replacing the bare Busch import in the restricted packet

The standard comparator theorem is Busch's theorem (Busch 2003
*Phys. Rev. Lett.* 91, 120403; refined Caves–Fuchs–Manne–Renes 2004
*Found. Phys.* 34, 193):

On a complex Hilbert space `H` with `dim H ≥ 2`, every POVM-additive
probability measure `m: E(H) → [0, 1]` is of the form

```text
m(E) = Tr(σ · E)                                                         (B)
```

for a unique density matrix `σ` on `H`.

The current packet does not leave (B) as a bare theorem name. It
spells out the finite qubit-lattice route in two branches.

**Branch A: the single-site qubit `M_2(C)`.** The authority bridge
[`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
matches the parent hypotheses exactly:

- (M1) `m(0)=0`;
- (M2) `m(𝟙)=1`;
- (M3) POVM-additivity over `Σ_i E_i = 𝟙`, with `m:E(M_2)->[0,1]`.

From those hypotheses it reproves the load-bearing direction on
`M_2(C)`:

1. the two- and three-outcome POVM laws give partial additivity
   `m(E_1+E_2)=m(E_1)+m(E_2)` whenever `E_1+E_2 <= 𝟙`;
2. partial additivity plus boundedness gives homogeneity on effects;
3. the functional extends real-linearly to `Herm(M_2)`;
4. finite-dimensional Riesz representation gives `F(H)=Tr(σH)`;
5. `m(𝟙)=1` and `m(P_ψ)>=0` force `Tr σ=1` and `σ>=0`.

The paired runner
[`scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py`](../scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py)
and cache
[`logs/runner-cache/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.txt`](../logs/runner-cache/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.txt)
check the exact rational `M_2` reconstruction, randomized `M_2`
effect/POVM tests, a `M_4` cross-check, and the dim-2 guard showing
that projection additivity alone underdetermines the trace form while
POVM additivity selects it.

**Branch B: multi-site regions `|Λ| >= 2`.** Restrict any
POVM-additive `m:E(H_Λ)->[0,1]` to the projections `P(H_Λ)`. Since
orthogonal projection families are POVM subfamilies, the restriction
is a projection-lattice probability measure. The projection-lattice
companion
[`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
therefore supplies a density matrix `σ` with `m(P)=Tr(σP)` for every
projection `P` on `H_Λ`.

It remains only to extend from projections to effects. If
`E=Σ_j λ_j P_j` is the finite spectral decomposition of an effect
(`0 <= λ_j <= 1`, pairwise orthogonal `P_j`), then homogeneity on
effects gives `m(λ_j P_j)=λ_j m(P_j)`, and partial additivity over
orthogonal effects gives

```text
m(E) = Σ_j m(λ_j P_j)
     = Σ_j λ_j Tr(σP_j)
     = Tr(σE).
```

Thus the multi-site effect theorem is obtained by the projection
companion plus finite spectral decomposition and the same
effect-additivity/homogeneity laws used in Branch A.

## Step 3 — Application to the qubit-lattice substrate

For any `|Λ| ≥ 1` (so `dim H_Λ = 2^|Λ| ≥ 2`), the restricted packet now
has a finite-region route to the effect theorem:

```text
m(E) = Tr(σ · E)   ∀ E ∈ E(H_Λ)                                          (3)
```

with `σ` a unique density matrix on `H_Λ`.

This covers all qubit-lattice region sizes including:
- `|Λ| = 1` (single site, dim 2): the **single-qubit Born form**
  — not handled by projective Gleason, supplied by the native
  `M_2(C)` effect bridge;
- `|Λ| >= 2` (dim `>= 4`): the projection-lattice companion gives
  the projection values, and finite spectral decomposition extends
  the result to every POVM effect.

Together, the single-site native effect bridge plus the multi-site
projection/spectral route cover **all finite qubit-lattice substrate
sizes**. Busch 2003 / CFMR 2004 remain parallel literature
comparators for the same conclusion.

## Step 4 — Finite-region scope and inductive-limit boundary

The theorem above is finite-region: every finite `Λ` has effect
algebra `E(H_Λ)`, and the source-local single-site plus multi-site
routes above give the Born-form representation on that finite algebra.
Passing from the compatible finite-region family to a state on the
quasi-local UHF algebra `A = ⊗_x M_2(ℂ)` is a separate standard
operator-algebraic inductive-limit step.

This note therefore supplies the finite-region Born form on the
framework substrate. It does not by itself prove an all-at-once
quasi-local normal-state theorem, nor does it identify the pre-record
state; those are separate rows / imports.

## What this can close after audit

- **The previous bare Busch/CFMR admitted-input** in
  `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`'s
  derivation chain. If independently retained, this row supplies a
  framework-scoped finite-region effect-Gleason application on the
  qubit-lattice effect algebra, with native source support for the
  single-site case and a projection/spectral route for multi-site
  regions.
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
- **A general all-Hilbert-space re-derivation of Busch's theorem** —
  the packet proves the finite qubit-lattice cases it uses and cites
  Busch/CFMR in parallel.
- **Non-commutative joint-system Born forms** that go beyond the
  finite-dim POVM effect-algebra (e.g., continuous-variable
  systems) — out of scope; the framework's substrate is finite-dim
  per site.
- **The quasi-local inductive-limit state theorem** — only the
  finite-region effect-Gleason application is claimed here.

## Source dependencies and inputs

1. **Single-site effect-Gleason bridge on `M_2(C)`** —
   [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
   with runner/cache linked above, supplies the load-bearing dim-2
   case.
2. **Projection-lattice companion for `|Λ| >= 2`** —
   [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
   supplies `m(P)=Tr(σP)` on projections in dimensions `>= 4`.
3. **Standard probability/effect-algebra axioms (M1)-(M3)** — the
   stated hypotheses of this theorem.
4. **Standard finite-dimensional spectral and Riesz representation
   facts** — used to extend from projection values to effects and to
   identify the representing density matrix.

## Risk classification

This is a `positive_theorem` candidate at the narrow-theorem granularity.
Finite effect-Gleason theory applied to the framework's specific
effect algebra `E(⊗_x M_2(ℂ))`. The narrow contribution is the
explicit application to the qubit-lattice substrate, with the dim-2
single-site case supplied by a native authority bridge and the
multi-site effect case routed through projection Gleason plus spectral
decomposition.

Granularity matches retained Clifford-algebra narrow theorems
(positive_theorem, retained): standard math applied to the
framework's specific operator structure.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) — native `M_2(C)` effect-Gleason bridge for the single-site gap, with exact hypotheses matched to (M1)-(M3)
- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) — projection-lattice density representation for multi-site finite regions

**Runner/cache evidence** (load-bearing for the native single-site bridge):

- [`scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py`](../scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py)
- [`logs/runner-cache/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.txt`](../logs/runner-cache/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.txt)

**Parallel standard-math comparators** (not the only source route):

- Busch 2003 *Phys. Rev. Lett.* 91, 120403 — original POVM-extension theorem
- Caves–Fuchs–Manne–Renes 2004 *Found. Phys.* 34, 193 — refined / clarified proof
- Standard finite-dim C*-algebra Riesz-representation result

**Plain-text pointer references** (NOT load-bearing deps):

- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — downstream consumer of this narrow theorem in the Born derivation chain
- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — supplies the pre-record reference `σ = ρ_ref` for the Born evaluation

## What this file is not

- Not a re-derivation of Busch's theorem for arbitrary Hilbert spaces
- Not a bare standard-math import; the finite qubit-lattice cases used
  here are routed through source-local notes/runners, with Busch/CFMR
  cited in parallel
- Not a closure of the Born derivation row (other admissions remain; see "What this does not close" above)
- Not an automatic Born promotion to retained (verdicts owned by audit lane)
- Not a numerical-prediction change
