# Pre-Record Reference State as the Unique Tracial State on A1+A2

**Date:** 2026-05-20
**Status:** proposal — pre-audit derivation note
**Type:** bounded_theorem candidate (positive_theorem on the uniqueness
half; bounded by a "no-extra-structure" identification premise on the
pre-record half)
**Supersedes (in part):** `archive_unlanded/a3-prime-pre-record-state-superseded-2026-05-20/A3_PRIME_MAXIMUM_ENTROPY_PRE_RECORD_REFERENCE_STATE_PROPOSAL_NOTE_2026-05-20.md`

## What this note proves

This note derives the pre-record reference state on the framework's
quasi-local operator algebra **as a consequence of A1+A2 plus a single
mild identification premise**, eliminating the need to adopt the
reference state as a separate axiom.

The framework's current axiom set is recorded in
`MINIMAL_AXIOMS_2026-05-20.md` — two axioms in qubit form (A1: qubit
per site, `M_2(ℂ) ≅ Cl(3,0)`; A2: `Z^3` substrate with tensor
composition).

The result:

> On the qubit-lattice operator algebra defined by A1+A2 (`A1`: per-site
> `M_2(ℂ) ≅ Cl(3,0)`; `A2`: `Z^3` substrate with tensor composition),
> there is a **unique tracial state** `τ`, characterized equivalently
> by: `τ(AB) = τ(BA)` for all `A, B`; invariance under all inner
> automorphisms; vanishing one-point Pauli expectation
> `τ(σ_a^x) = 0`; or maximum von Neumann entropy on every finite
> region. The density-matrix form of `τ` is `ρ_ref = ⊗_x I/2`.
>
> Identification (admitted): this unique tracial state is the
> pre-record reference. Any other choice would pick out preferred-basis
> / preferred-direction / preferred-eigenstate structure not present
> in A1+A2.

This supersedes the earlier proposal to adopt the reference state as
a third axiom (A3'). With the qubit framing of A1 in place (see
`A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md`), `ρ_ref` becomes a
*derived theorem* on A1+A2 plus the identification premise, not a new
axiom. The framework stays at two axioms.

## Setup

By A1 (qubit form), the per-site operator algebra at each site
`x ∈ Z^3` is `A_x = M_2(ℂ)`, the algebra of bounded operators on
`H_x = ℂ²`. By A2, the substrate is `Z^3` with sites composing via
tensor product. For a finite region `Λ ⊂ Z^3`:

- Hilbert space: `H_Λ = ⊗_{x ∈ Λ} ℂ²`, dimension `2^|Λ|`
- Operator algebra: `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)`, dimension `4^|Λ|` over `ℂ`
- Locality: `[A_x, A_y] = 0` for `x ≠ y`

The thermodynamic limit `Λ → Z^3` gives the **quasi-local algebra**
`A = ⋃_Λ A_Λ`, uniform-norm closure of the local algebras. This is
the **uniformly hyperfinite (UHF) C*-algebra of type `2^∞`**, a
completely standard object in operator algebra theory.

A **state** on `A` is a positive linear functional `φ: A → ℂ` with
`φ(I) = 1`.

## Step 1 — Unique tracial state on per-site `M_2(ℂ)`

**Lemma (standard).** On `M_2(ℂ)`, the unique state `τ` satisfying
`τ(AB) = τ(BA)` for all `A, B ∈ M_2(ℂ)` is the normalized trace:

`τ(A) = Tr(A) / 2`

In density-matrix form, `τ ↔ ρ = I_2 / 2`.

**Proof.** Standard finite-dim C*-algebra result. Any tracial linear
functional `τ` on `M_n(ℂ)` satisfies `τ(E_{ij}) = 0` for `i ≠ j` (by
`τ(E_{ij}) = τ(E_{ii} E_{ij}) = τ(E_{ij} E_{ii}) = 0`), and
`τ(E_{ii}) = τ(E_{jj})` for all `i, j` (by `τ(E_{ij} E_{ji}) =
τ(E_{ji} E_{ij})`). Normalization fixes `τ(E_{ii}) = 1/n`. For
`n = 2`: `τ(A) = Tr(A)/2`. □

## Step 2 — Tensor composition is tracial

**Lemma.** If `τ_x` is the tracial state on `A_x` for each `x ∈ Λ`,
then the tensor-product state `τ_Λ = ⊗_x τ_x` is the unique tracial
state on `A_Λ = ⊗_x A_x`.

**Proof.** *Tracial property:* immediate from `τ_x(A_x B_x) = τ_x(B_x A_x)`
per site applied factor-by-factor on simple tensors `A = ⊗_x A_x`,
`B = ⊗_x B_x`, then extended bilinearly to all of `A_Λ`.

*Uniqueness:* let `τ'` be any tracial state on `A_Λ`. The restriction
`τ'|_{A_x}` (defined by `τ'|_{A_x}(A_x) := τ'(A_x ⊗ ⊗_{y ≠ x} 𝟙_y)`)
is a tracial state on the simple finite-dim factor `A_x = M_2(ℂ)`, so
by Step 1 it equals the normalized trace on `A_x`. The same holds for
every `x ∈ Λ`. Now consider any simple tensor `A = ⊗_x A_x`. By the
tracial property and finite-dim factor-by-factor commutation argument
(any element of `A_x` commutes with any element of `A_y` for `x ≠ y`
because they live in commuting tensor factors), `τ'(⊗_x A_x)` decomposes
as `∏_x τ'|_{A_x}(A_x) = ∏_x (Tr(A_x) / 2)`. (This factorization step
uses that `A_Λ` is a finite tensor product of **simple matrix algebras**
`M_2(ℂ)`, which forces tracial states to factor — for general C*-algebras
tracial states need not factor on simple tensors, but for simple
finite-dim matrix algebras they do, by Tomita's theorem on tensor
products of factors.) Bilinear extension gives uniqueness on all of
`A_Λ`. □

So at any finite Λ, the tracial state is:

`ρ_Λ = ⊗_{x ∈ Λ} (I_2 / 2)`

equivalently, `τ_Λ(A) = Tr(A) / 2^|Λ|` for `A ∈ A_Λ`.

## Step 3 — Thermodynamic limit via Powers' theorem

**Theorem (Powers 1967).** The UHF C*-algebra of type `2^∞` admits a
unique tracial state, obtained as the inductive limit of the finite
tracial states above. The GNS representation of this tracial state
is the **hyperfinite type II_1 factor** `R`.

**Conclusion.** There is a unique tracial state `τ` on the quasi-local
algebra `A = ⊗_{x ∈ Z^3} M_2(ℂ)`, with finite-region density-matrix
form `ρ_ref|_Λ = ⊗_{x ∈ Λ} I_2/2`.

This is a closed-form positive theorem: **the math gives a unique
answer**. No additional input needed for this step.

## Step 4 — Characterization

The tracial state `τ` admits multiple equivalent characterizations,
all standard:

(C1) **Tracial property:** `τ(AB) = τ(BA)` for all `A, B ∈ A`.

(C2) **Inner-automorphism invariance:** `τ(U A U*) = τ(A)` for every
     unitary `U ∈ A`.

(C3) **One-point Pauli expectation vanishing:** `τ(σ_a^x) = 0` for
     every `a ∈ {1,2,3}` and `x ∈ Z^3`. (Equivalently: the per-site
     Bloch vector is zero in the tracial state.)

(C4) **Maximum von Neumann entropy:** `S(ρ_Λ) = |Λ| log 2` is the
     maximum value for any state on `A_Λ`.

(C5) **Maximal symmetry:** `τ` is the unique state invariant under
     the full unitary group `U(H_Λ)` action by inner automorphisms.

These are all equivalent for the finite-dim case; in the
thermodynamic limit (C1), (C2), and (C5) extend cleanly, and (C4)
becomes a "maximum entropy per site" condition.

## Step 5 — Identification with the pre-record reference (admitted)

To this point, the derivation is closed: there is a unique tracial
state on the A1+A2 algebra, with density-matrix form `⊗_x I/2`. The
remaining step is the *physical identification* of this unique state
as the pre-record reference.

The identification rests on the following principle:

> **No-extra-structure principle.** A1+A2 specify the operator
> algebra and the lattice substrate. Any pre-record state that breaks
> the algebra's natural symmetries (inner-automorphism invariance,
> per-site unitary equivalence) introduces structure — a preferred
> basis, direction, eigenstate, or polarization — not present in
> A1+A2. The pre-record reference should therefore be the unique
> state that introduces no such structure.

By Step 4, that unique state is the tracial state `τ`.

This principle is mild but admitted: it is a meta-principle about
the relationship between axioms and derived structure. Once accepted,
the identification of `τ` with `ρ_ref` is forced.

**Bounded-theorem status.** The Step 1–Step 4 mathematics is a
positive theorem on A1+A2 alone. Step 5's identification is admitted
under the no-extra-structure principle. The overall claim therefore
reads as a `bounded_theorem` with the principle listed in
`admitted_context_inputs`. If a reviewer accepts the principle, the
identification follows; if a reviewer rejects the principle, the
unique tracial state is still derived but its physical identification
as "pre-record reference" is open.

## What this derivation enables

With `ρ_ref` derived (not posited), the Born-rule derivation pipeline
proceeds without an axiom inflation:

1. **Born derivation via Gleason–Busch on `ρ_ref`.** The pinned
   reference state combined with the Gleason–Busch theorem on the
   POVM effect algebra of `A` gives the probability rule
   `p(E) = Tr(ρ_ref E)` uniquely. Record-conditioning via Lüders'
   rule then gives the standard `|⟨ψ|φ⟩|²` form for post-record
   measurements. See sketched derivation in
   `archive_unlanded/a3-prime-pre-record-state-superseded-2026-05-20/A3_PRIME_MAXIMUM_ENTROPY_PRE_RECORD_REFERENCE_STATE_PROPOSAL_NOTE_2026-05-20.md`
   §"Born derivation attempt" (the sketch is unchanged; only `ρ_ref`'s
   provenance changes from posited to derived).

2. **Vacuum-energy reframe.** Zero-point sums `Σ ℏω/2` are
   reinterpreted as relative entropies / free energies with respect
   to `ρ_ref`, finite by construction. (Same content as the previous
   proposal; only the reference state's status changes.)

3. **Cosmological initial condition.** The universe's pre-record
   reference is `ρ_ref` (now derived). Records accumulate from this
   reference; the arrow of time is structural.

4. **Persistent-record kernel grounding.** The kernel acts as a CPTP
   update on `ρ_ref` and its record-conditioned descendants.

## What this derivation does not do

- **Does not introduce a new axiom.** A3' is withdrawn; `ρ_ref` is now
  derived from A1+A2 + the no-extra-structure identification.
- **Does not change A1+A2.** They are unaffected. (See companion
  proposal `A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md` for a
  separate presentational sharpening of A1.)
- **Does not close any prior audit-conditional row** (e.g.,
  `observable_principle_from_axiom_note`'s scalar-additivity
  premise). Those conditions are observable-side or factorization-side
  and remain open under this derivation.
- **Does not bypass the dim-2 caveat for Born derivation.**
  Gleason's original theorem requires Hilbert dim ≥ 3; the
  single-site dim-2 case needs Busch's POVM extension. This caveat is
  unchanged by `ρ_ref` being derived rather than posited.
- **Does not close the Wilson-measure / `ρ_ref` Radon-Nikodym
  compatibility check.** That is a separate pending derivation.

## Relation to the BAE_MAX_ENTROPY obstruction

`BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md`
established that the *Jaynes max-entropy* route — deriving `ρ = I/2`
from A1+A2 + Born + Jaynes principle + physical-lattice — does not
have a unique answer without additional input.

The present note uses a *different* route: the **unique tracial
state** characterization via operator-algebra mathematics. This route
does not assume Born (which is good, since we want to derive Born from
`ρ_ref` downstream), does not use the Jaynes entropy functional, and
does not require additional Lagrange-multiplier inputs. The BAE
obstruction does not apply to this route.

A clean way to state the relationship: BAE_MAX_ENTROPY closed the
*Jaynes / max-entropy* derivation route negatively. This note opens
the *tracial / unitarily-invariant* derivation route positively.

## What this file is not

- Not a closure of the dim-2 Busch caveat for downstream Born
  derivation.
- Not a derivation that bypasses operator-algebra standard
  mathematics; it cites Powers' theorem and standard finite-dim
  tracial-state uniqueness.
- Not a unilateral retagging. The bounded-theorem candidacy depends
  on independent audit acceptance of the no-extra-structure
  identification premise.
- Not a numerical-prediction change.

## Citation-graph note

The mathematical content (Steps 1–4) is standard operator algebra
(finite-dim trace uniqueness, tensor traciality, Powers' UHF type
`2^∞` theorem) — named non-derivation imports. The identification
premise (Step 5) admits the no-extra-structure principle as input.

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — canonical axiom set; supplies A1+A2 on which the quasi-local algebra is built
- [`A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md`](A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md) — companion meta on the qubit identification

**Upstream standard-math imports** (named non-derivation; not framework rows):

- Finite-dim C*-algebra trace uniqueness (Dixmier / Glimm)
- Powers 1967 / standard UHF type-`2^∞` tracial-state uniqueness on `⊗_x M_2(ℂ)`
- Tomita / standard tracial-states-on-tensor-products result for finite-dim matrix algebras (used in Step 2 uniqueness)

**Plain-text pointer references** (NOT load-bearing deps; deliberately not markdown links to avoid polluting the audit dependency graph with non-load-bearing edges to conditional/contextual rows):

- `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md` — explanatory pointer; explains why this note's tracial route differs from the Jaynes route
- `AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md` — contextual pointer; `audited_conditional` at full-spinor scope. The narrow U1-U3 portion of its content is supported by the retained `cl3_complexification_split` + `cl3_faithful_irrep_dim_two` narrow theorems referenced in the canonical axiom doc, not via this row directly
