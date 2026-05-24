# Pre-Record Reference State as the Unique Tracial State on A1+A2

**Date:** 2026-05-20
**Status:** proposal — pre-audit derivation note
**Type:** bounded_theorem candidate (positive_theorem on the
unique-tracial-state characterization; the pre-record identification
half is demoted to a separate open admission, not part of this row's
audited claim — see `## Narrowed claim` and `## Open admission` below)
**Supersedes (in part):** `archive_unlanded/a3-prime-pre-record-state-superseded-2026-05-20/A3_PRIME_MAXIMUM_ENTROPY_PRE_RECORD_REFERENCE_STATE_PROPOSAL_NOTE_2026-05-20.md`

## Narrowed claim

Per auditor repair target (notes_for_re_audit_if_any on the 2026-05-23
audit verdict: "narrow the claim to the unique tracial-state theorem
only"), this row's audited claim is restricted to the unique
tracial-state characterization on the A1+A2 qubit-lattice algebra. The
physical identification of that unique tracial state as the pre-record
reference is **demoted to a separate open admission** (see
`## Open admission` below) and is *not* part of the audited claim of
this row.

The narrowed audited claim:

> On the qubit-lattice operator algebra defined by A1+A2 (`A1`: per-site
> `M_2(ℂ) ≅ Cl(3,0)`; `A2`: `Z^3` substrate with tensor composition),
> there is a **unique tracial state** `τ`, characterized equivalently
> by: `τ(AB) = τ(BA)` for all `A, B`; invariance under all inner
> automorphisms; vanishing one-point Pauli expectation
> `τ(σ_a^x) = 0`; or maximum von Neumann entropy on every finite
> region. The density-matrix form of `τ` is `ρ = ⊗_x I/2`.

The Steps 1-4 operator-algebra mathematics below (finite-dim trace
uniqueness, tensor traciality, Powers' UHF type `2^∞` theorem) close
this narrowed claim as a standard-math import composition. Step 5
below is retained as the open admission and is no longer load-bearing
on this row.

## Open admission (demoted; not part of the narrowed claim)

The further identification of the unique tracial state `τ` with a
pre-record reference state `ρ_ref` rests on the no-extra-structure
principle recorded in Step 5 below. This identification is **not**
part of this row's audited claim and is **not** closed by the
operator-algebra mathematics of Steps 1-4. It is recorded here as an
open admission for separate independent treatment (either an
independently audited bridge theorem from A1+A2 to the no-extra-structure
identification, or an independent forward derivation of a pre-record
reference state). Until that separate treatment lands, this note does
not claim that the unique tracial state has been identified with the
pre-record reference.

This narrowing supersedes the earlier proposal to adopt the reference
state as a third axiom (A3') only for the uniqueness half; the
pre-record identification half remains an open admission as noted
above. With the qubit framing of A1 in place (see
`A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md`), the unique tracial state
becomes a *derived theorem* on A1+A2 alone; identification with the
pre-record reference remains the separate open admission. The
framework stays at two axioms regardless.

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
form `ρ|_Λ = ⊗_{x ∈ Λ} I_2/2`. (Identification of this `ρ` with a
pre-record reference state `ρ_ref` is the demoted open admission of
`## Open admission` above and is not closed in this step.)

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

## Step 5 — Identification with the pre-record reference (demoted to open admission; not part of the narrowed claim)

**Scope.** Per the `## Narrowed claim` and `## Open admission` blocks
above, the identification of `τ` with a pre-record reference state is
**not** part of this row's audited claim. The material below is
retained for context describing the still-open identification but is
explicitly **not** load-bearing on the narrowed claim.

To this point (Steps 1-4), the derivation is closed: there is a unique
tracial state on the A1+A2 algebra, with density-matrix form `⊗_x I/2`.
The further (no-longer-audited-on-this-row) step is the *physical
identification* of this unique state as the pre-record reference.

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
the identification of `τ` with `ρ_ref` would follow.

**Narrowed-claim status.** The Step 1-Step 4 mathematics is the
narrowed audited positive theorem on A1+A2 alone (the
unique-tracial-state characterization). Step 5's identification is
the demoted open admission and is **not** part of the audited claim.
Closing it requires the separate independent treatment named in
`## Open admission` above.

## What this derivation enables (contingent on the demoted open admission)

The downstream enablements below all assume the demoted open admission
in `## Open admission` (identification of `τ` with the pre-record
reference). Within the narrowed audited claim alone they are *not*
enabled; they re-enter as enabled only once the open admission is
closed by independent treatment.

1. **Born derivation via Gleason–Busch on `ρ_ref`.** The pinned
   reference state combined with the Gleason–Busch theorem on the
   POVM effect algebra of `A` gives the probability rule
   `p(E) = Tr(ρ_ref E)` uniquely. Record-conditioning via Lüders'
   rule then gives the standard `|⟨ψ|φ⟩|²` form for post-record
   measurements. See sketched derivation in
   `archive_unlanded/a3-prime-pre-record-state-superseded-2026-05-20/A3_PRIME_MAXIMUM_ENTROPY_PRE_RECORD_REFERENCE_STATE_PROPOSAL_NOTE_2026-05-20.md`
   §"Born derivation attempt". Within this row's narrowed claim this
   downstream chain is not enabled.

2. **Vacuum-energy reframe.** Zero-point sums `Σ ℏω/2` would be
   reinterpreted as relative entropies / free energies with respect
   to `ρ_ref`, finite by construction. Contingent on the open
   admission.

3. **Cosmological initial condition.** The universe's pre-record
   reference would be `ρ_ref`. Records would accumulate from this
   reference. Contingent on the open admission.

4. **Persistent-record kernel grounding.** The kernel would act as a
   CPTP update on `ρ_ref` and its record-conditioned descendants.
   Contingent on the open admission.

## What this derivation does not do

- **Does not, within the narrowed claim, identify the unique tracial
  state `τ` with a pre-record reference state.** That identification
  is the demoted open admission of `## Open admission` above and is
  not part of this row's audited content.
- **Does not introduce a new axiom.** A3' is withdrawn for the
  uniqueness half (now a derived theorem); the pre-record
  identification half remains the separate open admission above.
- **Does not change A1+A2.** They are unaffected. (See companion
  proposal `A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md` for a
  separate presentational sharpening of A1.)
- **Does not close any prior audit-conditional row** (e.g.,
  `observable_principle_from_axiom_note`'s scalar-additivity
  premise). Those conditions are observable-side or factorization-side
  and remain open under this derivation.
- **Does not bypass the dim-2 caveat for any downstream Born
  derivation.** Gleason's original theorem requires Hilbert dim ≥ 3;
  the single-site dim-2 case needs Busch's POVM extension. This caveat
  is unchanged by the narrowing.
- **Does not close the Wilson-measure / `ρ_ref` Radon-Nikodym
  compatibility check.** That is a separate pending derivation,
  unaffected by the narrowing.

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

- Not a closure of the dim-2 Busch caveat for any downstream Born
  derivation.
- Not a derivation that bypasses operator-algebra standard
  mathematics; it cites Powers' theorem and standard finite-dim
  tracial-state uniqueness.
- Not a unilateral retagging. The narrowed positive-theorem candidacy
  depends on independent audit acceptance of Steps 1-4 only; the
  pre-record identification (Step 5) is the demoted open admission
  and is not part of the audited claim.
- Not a closure of the pre-record identification. That remains the
  separate open admission in `## Open admission` above.
- Not a numerical-prediction change.

## Citation-graph note

The mathematical content (Steps 1–4), which constitutes the entire
narrowed audited claim, is standard operator algebra (finite-dim
trace uniqueness, tensor traciality, Powers' UHF type `2^∞`
theorem) — named non-derivation imports. Step 5's identification
premise is no longer load-bearing on the narrowed claim and is
recorded as the demoted open admission only.

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
