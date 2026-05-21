# Reflection Positivity ↔ ρ_ref Radon–Nikodym Compatibility

**Date:** 2026-05-20
**Type:** bounded_theorem candidate (operator-algebra compatibility result)
**Status:** source-side proposal — independent audit lane owns the verdict
**Closes (proposed):** the pending follow-up flagged in PR #1604 description:
*"Reflection positivity ↔ A3' compatibility. The Wilson Euclidean
measure is absolutely continuous with respect to ρ_ref; the
Radon-Nikodym derivative should be identified."*

## Claim

On the qubit-lattice operator algebra defined by
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) (A1 =
qubit at every site, A2 = `Z^3` substrate), the framework's
**reflection-positive Wilson Euclidean measure** `μ_Wilson` (the
positive measure on configurations underlying retained reflection
positivity per
[`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md))
and the **canonical tracial state** `ρ_ref = ⊗_x I/2` (from
[`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md))
satisfy the absolute-continuity relationship

```text
dμ_Wilson / dρ_ref = e^{-S_Wilson} · Z_Wilson^{-1}                       (1)
```

where `S_Wilson` is the Wilson action and `Z_Wilson` is the partition
function. The Radon-Nikodym derivative is the standard Boltzmann
weight relative to the tracial reference.

This makes explicit the compatibility between the framework's two
positive-measure structures: the Wilson Euclidean measure (carrier of
RP) and the tracial reference state (carrier of the pre-record
probability foundation under the qubit reframe).

## Setup

By A1+A2, the quasi-local operator algebra is
`A = ⊗_{x ∈ Z^3} M_2(ℂ)` (UHF type `2^∞` C*-algebra). The framework
defines two positive-measure structures on `A`:

**The Wilson Euclidean measure `μ_Wilson`.** For a finite Λ ⊂ Z³,
the Wilson action `S_Wilson[U, ψ]` (for gauge link variables and
staggered fermions) gives the Euclidean path-integral measure

```text
dμ_Wilson(U, ψ̄, ψ) = (1 / Z_Wilson) · e^{-S_Wilson[U, ψ̄, ψ]} · dU · dψ̄ · dψ      (2)
```

with `Z_Wilson = ∫ e^{-S_Wilson} · dU · dψ̄ · dψ`. This is a positive
measure (after the staggered determinant positivity, retained for
Cases A and B of the RP theorem), and reflection positivity
(`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29`) is
expressed as `⟨A · (θ A^†)⟩_μ ≥ 0` for observables `A` on one side
of a temporal hyperplane.

**The tracial state `ρ_ref = ⊗_x I/2`.** From the companion
derivation note, this is the unique tracial state on `A`, given by
`ρ_ref(O) = (1/2^|Λ|) · Tr_A(O)` for `O ∈ A_Λ`. As a state on the
algebra (not a path-integral measure on configurations), `ρ_ref` is
a different mathematical object than `μ_Wilson`. The compatibility
question: how are they related?

## Step 1 — Translation between the two language layers

The Wilson measure `μ_Wilson` lives on **configuration space**
(gauge links + fermion fields); the tracial state `ρ_ref` lives on
**operator algebra** observables. The translation is via the
operator-algebraic representation of observables:

For any observable `O ∈ A_Λ`, its expectation under `μ_Wilson` is

```text
⟨O⟩_Wilson = ∫ O(U, ψ̄, ψ) · dμ_Wilson(U, ψ̄, ψ)                          (3)
```

(where `O` here is the configuration-functional representation of the
operator). Its expectation under `ρ_ref` is

```text
ρ_ref(O) = (1/2^|Λ|) · Tr_A(O)                                          (4)
```

These two expectations are generally **not equal** for operators
with non-trivial Boltzmann weight in `S_Wilson`. The Wilson measure
weights configurations by `e^{-S_Wilson}`; the tracial state weights
all states equally.

## Step 2 — The Radon–Nikodym relationship

Both `μ_Wilson` and `ρ_ref` are normalized positive measures (on
configuration space and operator algebra respectively). They are
**mutually absolutely continuous** in the following sense: there
exists a positive density `f(U, ψ̄, ψ)` such that for any operator
`O`,

```text
⟨O⟩_Wilson = ρ_ref(O · f) / ρ_ref(f)                                    (5)
```

where `f` is the Radon-Nikodym derivative `dμ_Wilson / dρ_ref`. By
direct construction from (2) and (4):

```text
f(U, ψ̄, ψ) = 2^|Λ| · (1/Z_Wilson) · e^{-S_Wilson[U, ψ̄, ψ]}              (6)
```

So

```text
dμ_Wilson / dρ_ref = e^{-S_Wilson} · Z_Wilson^{-1} · 2^|Λ|              (1')
```

The factor `2^|Λ|` is the `dim H_Λ`, absorbed into the normalization
convention. Stripping this convention:

```text
dμ_Wilson / dρ_ref ∝ e^{-S_Wilson}                                       (7)
```

The Radon-Nikodym derivative is the **Boltzmann weight** of the
Wilson action, relative to the tracial reference state. This is the
standard statistical-mechanics relationship: the Wilson measure is
the Gibbs measure at unit inverse temperature on the qubit-lattice
algebra, with the tracial state as the infinite-temperature (or
zero-action) limit.

## Step 3 — Compatibility check on positivity

The Radon-Nikodym density `f(U, ψ̄, ψ) ∝ e^{-S_Wilson}` is positive
wherever `S_Wilson` is real and finite — which is the staggered-only
(Case A) and symmetric-canonical Wilson (Case B) sectors of the
retained RP theorem
([`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md),
narrowed scope per 2026-05-17 review).

On these sectors:
- `S_Wilson` is real (RP requires this)
- `e^{-S_Wilson} > 0` (real exponential is positive)
- Therefore `f > 0` (positive Radon-Nikodym density)
- Therefore `μ_Wilson` and `ρ_ref` are mutually absolutely continuous
- Therefore both measures see the same null sets — RP positivity on
  `μ_Wilson` translates correctly to positivity statements on `ρ_ref`

This is the explicit compatibility check: **the Wilson measure
(carrier of RP) and the tracial reference state (carrier of
pre-record probability) coexist via a positive Boltzmann-weight
Radon-Nikodym derivative.**

## Step 4 — Thermodynamic limit

For the thermodynamic limit Λ → Z³, both `μ_Wilson` and `ρ_ref`
extend to limit measures on the quasi-local algebra:
- `ρ_ref` extends to the unique tracial state on the UHF type `2^∞`
  C*-algebra (Powers / Glimm / Dixmier; supplied by the companion
  derivation note)
- `μ_Wilson` extends to the Gibbs measure at unit inverse temperature
  on the same algebra, provided the action `S_Wilson` admits a
  well-defined thermodynamic limit (standard lattice gauge theory)

The Radon-Nikodym relationship (7) extends to the thermodynamic
limit on the staggered-only and symmetric-canonical Wilson sectors
where RP retains. Outside those sectors (the broader Wilson surface
explicitly outside the load-bearing RP claim per the 2026-05-17
narrowing), the relationship is admitted as a structural property
of the Wilson action but is not load-bearing for this note.

## What this closes

- **The pending RP ↔ ρ_ref compatibility follow-up** flagged in PR
  #1604's qubit-reframe landing note. The Wilson measure and the
  tracial state are now explicitly related via Boltzmann-weight
  Radon-Nikodym derivative on the retained RP scope.

## What this does not close

- **The broader RP scope** (non-symmetric Wilson surfaces). The
  retained RP is narrow (Cases A and B); the Radon-Nikodym
  relationship inherits that narrowness.
- **The full thermodynamic-limit RP retention** — that's the
  Wilson-measure construction independent of this note.
- **The framework's `BORN_RULE_ANALYSIS_2026-04-11` repair** — that's
  the separate Born derivation chain.

## Admitted inputs

1. **Wilson action functional form** — admitted from standard lattice
   gauge theory; the framework's specific Wilson + staggered fermion
   action is on the `g_bare = 1` open-gate surface for full
   numerical pinning, but the Radon-Nikodym relationship (1) is a
   structural statement about any positive Wilson action and does
   not require the gate to close.
2. **Staggered determinant positivity** — retained on Cases A and B
   per the RP theorem's 2026-05-17 narrowing.
3. **Standard Gibbs / partition-function measure-theoretic
   construction** — named non-derivation import.

## Risk classification

This is a `bounded_theorem` candidate. The Radon-Nikodym
relationship (1) is the standard statistical-mechanics relationship
between Gibbs measures and tracial reference states; the narrow
contribution is the explicit identification that this relationship
holds between the framework's two positive-measure structures on
the qubit-lattice algebra. The Wilson action's specific form is
gate-conditional but the structural Radon-Nikodym relationship is
not.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) — supplies ρ_ref as unique tracial state on the quasi-local algebra
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md) — supplies the retained RP scope (Cases A and B) and the Wilson Euclidean measure structure

**Upstream standard-math imports** (named non-derivation):

- Standard statistical-mechanics Gibbs / Boltzmann-weight construction
- Standard Radon-Nikodym theorem (measure-theoretic)

**Plain-text pointer references** (NOT load-bearing deps):

- `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md` — Grassmann gate referenced for the Wilson-action specific form; not load-bearing for the structural Radon-Nikodym statement
- `G_BARE_DERIVATION_NOTE.md` — `g_bare = 1` gate referenced for the Wilson coupling normalization; not load-bearing here

## What this file is not

- Not a closure of the broader RP scope (narrowed Cases A and B remain the load-bearing scope per RP theorem)
- Not a derivation of the Wilson action (admitted gate-conditional)
- Not a re-derivation of standard Radon-Nikodym (textbook math)
- Not a numerical-prediction change
- Not a unilateral retagging
