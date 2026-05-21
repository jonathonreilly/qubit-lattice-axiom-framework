# Pre-Record Reference State as the Cosmological Initial Condition: A Bounded Proposal

**Date:** 2026-05-20
**Type:** bounded_theorem candidate (foundational proposal)
**Status:** source-side proposal — independent audit lane owns the verdict
**Proposes:** identifying the qubit-trace pre-record reference state
`ρ_ref = ⊗_x I/2` (from
[`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md))
as the **cosmological initial condition** on the framework's
qubit-lattice substrate. Records form via dynamics; cosmological
history is the accumulation of records from `ρ_ref`.

## Honest scope

This is a **foundational proposal note**, not a derivation that
closes a numerical observable. It records the framework's stance on
the cosmological initial condition under the qubit reframe of A1
([`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)):

- The pre-record reference state `ρ_ref = ⊗_x I/2` is canonically
  defined on A1+A2 (derived; not a posited axiom; see companion
  tracial-state derivation note)
- Identifying `ρ_ref` as the cosmological initial state is a
  **separate proposal** — well-defined but admitted as an
  identification premise.

The note is structurally analogous to the proposal that the Wilson
Euclidean measure carries reflection positivity — both are
identifications of canonical positive-measure structures with
physical-theoretic roles. The identification does not derive new
observables; it makes the cosmological-initial-condition convention
explicit in qubit-lattice language.

## Claim

On the framework's qubit-lattice substrate, **the cosmological
initial state of the universe is the canonical pre-record reference
state**:

```text
ρ_universe(t = 0) := ρ_ref = ⊗_{x ∈ Z^3} (I_2 / 2)                       (1)
```

Records (irreversible classical bits encoding past measurement
outcomes, per
[`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md)
and the framework's record-formation lanes) accumulate over time
through dynamics, generating the universe's record-rich present
state. The **arrow of time** is the direction of increasing record
content; the **Past Hypothesis** (Albert 2000; Penrose 1989) is
realized as `ρ_universe(t = 0) = ρ_ref` (zero records).

## Setup

By A1+A2 of `MINIMAL_AXIOMS_2026-05-20.md`, the universe's quasi-local
operator algebra is `A = ⊗_{x ∈ Z^3} M_2(ℂ)`. A state on `A` is a
positive linear functional `φ: A → ℂ` with `φ(I) = 1`.

The canonical tracial state `ρ_ref = ⊗_x I/2` is supplied by the
companion tracial-state derivation note (bounded_theorem candidate,
admitted under the no-extra-structure identification premise on
A1+A2). It is the **unique state on `A` invariant under all unitary
automorphisms of the per-site algebra** — i.e., the state that
introduces no structure beyond A1+A2 itself.

## Step 1 — Information-theoretic interpretation of `ρ_ref`

The tracial state `ρ_ref` has **zero information** about the system
in the precise quantum-information sense:

- **Maximal von Neumann entropy:** `S(ρ_ref|_Λ) = |Λ| · log 2` is
  the maximum possible for a state on a finite region Λ.
- **No bias toward any basis:** every projective measurement returns
  uniform statistics over the projector's eigenvalues.
- **Zero recorded outcomes:** any partial trace of `ρ_ref` over any
  subset of sites returns `ρ_ref|_{remainder}` (tensor-product
  structure preserved under partial trace) — no classical record is
  encoded.

This matches the standard quantum-information notion of "no prior
information" / "uniform prior" / "Jaynes-maximum-entropy state."

## Step 2 — Cosmological-initial-condition identification

Identifying `ρ_universe(t = 0) = ρ_ref` makes explicit:

**(a) The Past Hypothesis:** the universe begins with the
lowest-information state. Records accumulate forward in time, never
backward. The arrow of time is the direction of record accumulation.

**(b) Cosmological CPT compatibility:** `ρ_ref` is CPT-invariant
(retained CPT acts as an antiunitary symmetry preserving the tracial
state, since the tracial state is invariant under all inner
automorphisms of the algebra). So this initial condition does not
break CPT.

**(c) No initial fine-tuning:** the cosmological initial state is
the canonical choice — the most symmetric state, the unique
unitarily-invariant state, the maximum-entropy state. No additional
parameters are admitted at the initial condition layer.

**(d) Compatibility with Wilson measure / RP:** by the companion note
[`RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md`](RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md),
the Wilson Euclidean measure is `dμ_Wilson / dρ_ref ∝ e^{-S_Wilson}`.
So the cosmological initial condition `ρ_ref` is the "infinite
temperature" / "zero action" limit of the Wilson Gibbs measure, with
records forming as configurations deviate from this maximum-entropy
reference via dynamics.

## Step 3 — Record-formation dynamics from `ρ_ref`

Records form by **CPTP dynamics** on the qubit algebra (per
[`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md),
in flight as PR #1608). For a measurement-like dynamics with Kraus
operators `{K_r}`, the unconditional state update is

```text
ρ_universe(t = 1) = Σ_r K_r · ρ_universe(t = 0) · K_r†                  (2)
                  = Σ_r K_r · ρ_ref · K_r†
```

In general `ρ_universe(t = 1) ≠ ρ_ref` (records are encoded in the
mixture), so the entropy of the universe's state **decreases** under
record-formation: `S(ρ_universe(t = 1)) ≤ S(ρ_ref)`. This is the
information-gain consequence of records, not violation of the second
law (which applies to thermodynamic entropy of records + environment,
not the universe's quantum entropy of state).

Equivalently in the Born derivation framework
([`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)),
record-conditional Lüders updates give the conditional probabilities
that the universe's records encode — these are the framework's Born
probabilities, with `ρ_ref` as the pre-record reference.

## Step 4 — What the proposal does NOT change

**Numerical observables.** This identification does not change any
retained quantitative prediction (`α_s`, `v`, masses, CKM, Koide,
etc.). Those are post-record-formation observables; their values
are determined by dynamics (Wilson action + gates), not by the
initial-condition identification.

**Open gates.** The Grassmann staggered-Dirac and `g_bare = 1` open
gates are independent of the cosmological initial condition.

**Reflection positivity.** Unchanged; the Wilson measure structure
that carries RP is related to `ρ_ref` via Radon-Nikodym
(`RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20`), but RP
itself does not require this cosmological-initial-condition
identification.

**Anthropic / fine-tuning questions.** This proposal does not
address the anthropic puzzle (why is the universe like ours?). It
addresses only the **initial-condition layer** (zero records, max
entropy on the qubit substrate); the post-record evolution that
leads to a structured present universe is dynamics-dependent.

## Step 5 — Relation to Past Hypothesis literature

The proposal aligns with the **Past Hypothesis** in cosmology
(Albert 2000 *Time and Chance*; Penrose 1989 *The Emperor's New
Mind*; Loewer / Carroll for modern statements). Penrose's
"low-Weyl-curvature initial condition" is a classical-GR statement;
this proposal is its quantum-information equivalent on the
qubit-lattice substrate. Both encode the same physical content (the
universe begins with low complexity / low information / high
symmetry) in different language layers.

## What this proposal does

- Records the framework's stance on the cosmological initial condition
- Makes the "Past Hypothesis at zero records" claim mathematically
  precise on the qubit-lattice substrate
- Connects record-formation dynamics to cosmological history via
  the in-flight Persistent-record-as-Kraus and Born-derivation
  lanes
- Identifies the arrow of time with record-content accumulation

## What this proposal does NOT do

- Does not change any retained numerical prediction
- Does not close any audited_conditional row (this is a foundational
  proposal, not a row-specific closure)
- Does not resolve the anthropic / fine-tuning question
- Does not claim that this is the unique sensible cosmological
  initial condition — only that it is the canonical one on the
  qubit-lattice substrate under the no-extra-structure identification

## Admitted inputs

1. **Pre-record reference state `ρ_ref` as the unique tracial state
   on A1+A2** — from the companion tracial-state derivation note
   (bounded support, admitted under no-extra-structure identification).
2. **No-extra-structure identification premise** — already admitted
   in the companion tracial-state note; carried forward here.
3. **Past Hypothesis** interpretation — admitted as the standard
   cosmological framing (Albert / Penrose / Carroll).

## Risk classification

This is a `bounded_theorem` candidate at the **foundational proposal
level**. The mathematical content (Steps 1, 3, 4) is standard
operator-algebra / quantum-information theory. The identification
(Step 2) is an admitted premise that the framework adopts as the
canonical cosmological initial condition. The narrow contribution
is recording this identification explicitly in qubit-lattice
language and connecting it to record-formation dynamics.

If accepted, this provides a clean foundational layer for downstream
cosmology / arrow-of-time / second-law lanes without changing any
numerical content.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra + Z^3 substrate)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) — supplies `ρ_ref` as the unique tracial state
- [`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md`](PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md) — supplies the framework's record-formation lane

**Upstream standard-physics imports** (named non-derivation):

- Albert 2000 *Time and Chance* — Past Hypothesis framing
- Penrose 1989 *The Emperor's New Mind* — low-Weyl-curvature initial-condition framing (classical GR analogue)

**Plain-text pointer references** (NOT load-bearing deps):

- `RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md` (in flight PR #1622) — companion compatibility note
- `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` — Born derivation companion
- `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md` (in flight PR #1608) — Kraus-operator identification of record formation

## What this file is not

- Not a derivation of cosmological structure formation (post-record dynamics depend on the open gates)
- Not a numerical-prediction change
- Not a unique-initial-condition theorem — alternative initial conditions are mathematically possible; this note proposes the canonical one
- Not a closure of any audited row
- Not a unilateral retagging
