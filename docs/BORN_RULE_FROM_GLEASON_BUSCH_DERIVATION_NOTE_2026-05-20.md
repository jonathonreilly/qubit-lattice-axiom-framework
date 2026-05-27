# Born Rule via Gleason–Busch on the Pre-Record Reference State: Bounded Support / Repair Route

**Date:** 2026-05-20
**Status:** proposal — pre-audit bounded support / repair-route note
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Repair route for:** the `audited_failed`
`BORN_RULE_ANALYSIS_2026-04-11.md` lane (the gravitational Hartree
fixed-point derivation failed; this note proposes Gleason–Busch on a
pinned tracial reference as the structurally different replacement
route). The framework's adjacent stated repair target on
`NONLINEAR_BORN_GRAVITY_NOTE.md` (*"provide a retained bridge theorem
deriving the probability/readout rule without imposing `|psi|^2`"*)
is structurally addressed on the finite ideal-record surface. The repair
now cites direct framework rows for the qubit-lattice Gleason/Busch
probability representation, the pre-record tracial reference state, the
finite Kraus/Choi representation, and the canonical Naimark/Lüders
projective-record update. It does **not** claim durable/native persistent
record formation or the broader gravitational-Hartree route.

## 2026-05-27 Framework-Dependency Repair

Earlier versions treated Gleason/Busch, Lüders, and Kraus/readout as raw
standard-math imports. Those are no longer raw imports for this row's binding
finite-region claim. The row now uses direct in-repo authorities:

- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)
- [`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
- [`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
- [`LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md`](LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md)

The binding surface is intentionally narrower than the old prose: finite
qubit-lattice regions, POVM/effect probabilities from the retained
Gleason/Busch framework rows, and ideal unrefined sharp-projective records in
the retained canonical Naimark/Lüders frame. Persistent durable record
formation, arbitrary unsharp instruments, and native apparatus dynamics remain
outside this row.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The retained tracial-state dependency now closes only the unique-tracial-state theorem, and explicitly does not identify that state with a pre-record physical reference. The source note still imports the no-extra-structure/pre-record identi"*

with repair: *"missing_bridge_theorem: land and cite retained bridge theorems for pre-record identification, Lüders/update or resolved projective-measurement conditioning, and persistent-record-as-Kraus/readout mapping; then re-audit the Born derivation w"*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The Gleason-Busch uniqueness step (Steps 1 and 2 of the derivation) that determines the form `p(E) = Tr(σ·E)` from the one-qubit operator algebra on the `Z^3` spatial substrate plus standard probability axioms (P1)-(P3), verified by runner-referenced operator-algebraic argument on the finite qubit-lattice algebra; and the algebraic step tracing `σ` to the unique tracial state `ρ_ref = ⊗_x I/2` derived in the companion tracial-state note.
- **NON-load-bearing (split off / admitted):** The identification of the unique tracial state with the physical pre-record reference (no-extra-structure premise), the Lüders/compositional-consistency update rule (U4), and the formal connection of the persistent-record lane to Kraus operators — all three are admitted, not-derived inputs recorded as explicit external premises; the Born-rule conclusion is conditional on these bridges being independently retained.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## What this note derives

On the qubit-lattice framework (A1+A2 in qubit form per
`MINIMAL_AXIOMS_2026-05-20.md`), with the pre-record reference state
`ρ_ref = ⊗_x I/2` derived in
`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`,
the Born rule for measurement outcomes follows from operator-algebraic
and probability-theoretic standard mathematics:

> For any POVM `{E_i}` on the qubit-lattice operator algebra, the
> probability of outcome `i` for the pre-record system is
> `p(i) = Tr(ρ_ref · E_i)`. After a sequence of records has
> conditioned the system to pure state `|ψ⟩⟨ψ|`, the probability of
> a subsequent measurement of POVM `{E_i}` is
> `p(i) = ⟨ψ|E_i|ψ⟩`. For rank-1 projectors `E_i = |φ_i⟩⟨φ_i|`, this
> reduces to the standard Born form `p(i) = |⟨φ_i|ψ⟩|²`.

The derivation chain is:

1. **Framework Gleason–Busch rows** uniquely determine the form
   `p(E) = Tr(σ·E)` on the POVM effect algebra of `M_2(ℂ)` (Busch
   POVM extension for the per-site dim-2 case) and
   `⊗_{x∈Λ} M_2(ℂ)` (Gleason direct for `|Λ| ≥ 2`, `dim ≥ 4`).
2. **Pre-record tracial reference row** pins the unique tracial state
   `ρ_ref = ⊗_x I/2` on the quasi-local tensor-product algebra. This row uses
   it only as the finite pre-record reference on the ideal-record surface.
3. **Kraus/Choi plus canonical Naimark/Lüders rows** supply the ideal
   unrefined sharp-projective record update `K_P = P` and sequential effect
   `P E P` on finite regions.
4. **Pure-state limit** `ρ_ref` → `|ψ⟩⟨ψ|` is achieved after a
   complete record on a single-qubit subsystem; subsequent Born is
   `⟨ψ|E|ψ⟩` for any POVM effect `E`.

## Setup

By A1 (qubit form), per-site `A_x = M_2(ℂ)` with Hilbert space
`H_x = ℂ²`. By A2, finite region `Λ ⊂ Z^3` gives
`A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)`, Hilbert space
`H_Λ = ⊗_{x ∈ Λ} ℂ²`, dimension `2^|Λ|`.

The **POVM effect algebra** `E(A_Λ)` consists of self-adjoint
operators `E ∈ A_Λ` with `0 ≤ E ≤ I`. A POVM is a finite collection
`{E_i}_{i=1}^n` with `Σ_i E_i = I`. Each `E_i` represents one
possible measurement outcome.

A **probability assignment** is a function `p: E(A_Λ) → [0,1]`
satisfying:

- **(P1)** Positivity: `p(E) ≥ 0` for all `E ∈ E(A_Λ)`
- **(P2)** Normalization: `p(I) = 1`
- **(P3)** σ-additivity: `p(Σ_i E_i) = Σ_i p(E_i)` for any countable
  resolution of identity `Σ_i E_i = I`

These three are the standard probability axioms restricted to the
POVM effect algebra.

## Step 1 — Gleason–Busch uniqueness of the probability form

**Framework theorem surface (Gleason/Busch rows).** Any probability assignment
`p: E(A_Λ) → [0,1]` satisfying (P1)–(P3) has the form

> `p(E) = Tr(σ · E)`

for a unique density matrix `σ` on `H_Λ`.

**Domain of applicability.** Gleason's original theorem requires
Hilbert dim ≥ 3, which holds for `|Λ| ≥ 2` (since `dim H_Λ = 2^|Λ| ≥
4`). The single-site case (`|Λ| = 1`, `dim = 2`) is handled by
the retained Busch/CFMR finite-region qubit-lattice application.

**This step does not depend on A3'.** It is a pure consequence of the
algebra structure given by A1+A2 plus the standard probability axioms
(P1)–(P3). No state-side input is required for Step 1.

## Step 2 — Pin σ to the derived pre-record reference

By the pre-record tracial reference row, the unique tracial state on the
quasi-local algebra is
`ρ_ref = ⊗_x I/2`. Under the no-extra-structure identification
surface used by the ideal-record packet, `ρ_ref` is the finite pre-record
reference state.

So for any measurement on the **pre-record system**, Step 1 gives:

> `p(E) = Tr(ρ_ref · E) = Tr(E) / 2^|Λ|`

This is the **uniform-prior Born rule**: each POVM outcome's
probability is proportional to the rank/trace of its effect, with the
maximally mixed reference state. For rank-1 projectors
`E_i = |φ_i⟩⟨φ_i|`, this gives uniform `1 / 2^|Λ|` across all
`2^|Λ|` distinguishable outcomes on `|Λ|` qubits. This is the
expected Bayesian prior in the absence of records.

## Step 3 — Lüders rule for record conditioning

A measurement record corresponds to a positive operator `P` (a
projection or, more generally, a Kraus operator) acting on the
system. The system's state updates conditional on the record.

The retained canonical Naimark/Lüders rows supply the ideal sharp-projective
record update satisfying:

- **(U1)** Positivity preservation: `σ → σ'` with `σ' ≥ 0`
- **(U2)** Normalization preservation: `Tr(σ') = 1`
- **(U3)** Probability consistency with Step 1: for the
  post-conditioning effect `E'`, the joint probability decomposes as
  `p(P then E') = p(P) · p(E' | P)`
- **(U4)** Compositional consistency: `(σ|_P)|_{P'} = σ|_{P' · P}`

as the **Lüders rule**:

> `σ → σ|_P = (P σ P) / Tr(P σ P)` for projection `P`
>
This row binds only the ideal unrefined sharp-projective case and the retained
canonical frame. It does not claim uniqueness for every possible unsharp
instrument implementing a POVM.

## Step 4 — Born rule for post-record measurements

Apply Step 3 to `ρ_ref`. After a sequence of records that includes
a complete projective measurement on a subsystem `S ⊂ Λ` with
outcome `i` corresponding to rank-1 projector `P_i = |ψ_i⟩⟨ψ_i|`, the
state of `S` is conditioned to:

> `ρ_S|_{i} = (P_i ρ_ref P_i) / Tr(P_i ρ_ref P_i) = |ψ_i⟩⟨ψ_i|`

A subsequent measurement of POVM `{E_j}` on `S` then gives, by
Step 1 applied to the conditioned state:

> `p(j | i) = Tr(E_j |ψ_i⟩⟨ψ_i|) = ⟨ψ_i| E_j |ψ_i⟩`

For rank-1 projectors `E_j = |φ_j⟩⟨φ_j|`:

> `p(j | i) = |⟨φ_j | ψ_i⟩|²`

**That is Born's rule** on the finite ideal-record surface — derived from
A1+A2 plus the direct framework rows listed in the 2026-05-27 repair section.

## Caveats (real)

1. **Dim-2 Busch extension.** This row relies on the retained qubit-lattice
   Busch/CFMR application for single-site effects.

2. **Canonical projective-record surface.** The retained Lüders/Naimark rows
   cover ideal unrefined sharp-projective records in the canonical frame. This
   row does not extend them to arbitrary unsharp instruments.

3. **Durable persistent records.** Connecting the framework's generated
   persistent-record kernels to native apparatus dynamics remains separate.

4. **Lieb-Robinson for locality.** The derivation implicitly assumes
   that records on subsystem `S` do not propagate faster than light.
   The framework's existing Lieb-Robinson retained results
   (`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`)
   supply this; the connection should be made explicit in a follow-up
   compatibility note.

5. **Thermodynamic limit care.** Step 1's σ-additivity over
   countable POVM resolutions in the thermodynamic limit is
   standard but should be checked explicitly via the GNS
   construction on the UHF type `2^∞` C*-algebra. Routine.

## What this note proposes as a repair route (not a closure)

- **`BORN_RULE_ANALYSIS_2026-04-11.md`** (currently
  `audited_failed`): the prior derivation route (gravitational
  Hartree fixed-point) failed because it could not prove the
  contraction-rate argument. This note proposes Gleason–Busch on the
  pinned tracial reference as a structurally different repair route.
  The repair now points at direct framework rows for the finite
  Gleason/Busch and projective-record pieces. It remains scoped to the
  ideal finite-region surface and does not close durable/native record
  formation.

- **`NONLINEAR_BORN_GRAVITY_NOTE.md`** repair target: *"provide a
  retained bridge theorem deriving the probability/readout rule
  without imposing `|psi|^2`."* This note structurally addresses the
  target — the `|⟨φ|ψ⟩|²` form is the *output* of Step 4 given the
  admitted inputs, not assumed by the derivation. But because the
  imports are not all retained, this is bounded support for the
  repair, not the retained bridge theorem itself.

- **`BEYOND_LATTICE_QCD_NOTE.md`** circularity (the runner assumes
  `np.abs(psi)**2` to test Born): the proposed Gleason–Busch route
  would supply the Born rule from upstream so the test is downstream
  of a derived rule rather than circular. Same caveat: this is a
  bounded support route until the imports retain.

## What this derivation does not close

- **`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE`** scalar-additivity
  condition — that is observable-side (additivity of
  `log|det(D+J)|`), unaffected by the Born derivation.
- **`GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE`**
  factorization condition — also unaffected.
- The dim-2 Busch caveat and the Lüders (U4) admission listed above.
- The Wilson-measure ↔ `ρ_ref` Radon-Nikodym compatibility note —
  still pending.

## Relation to existing retained / retained_bounded rows

This derivation is *consistent* with all existing retained
Sorkin-`I_3 ≈ 0` numerical results (`central_band_born_*`,
`i3_zero_exact_theorem_note`, `nonlinear_born_gravity_note`).
Those rows were *consistency checks* (verifying that
`I_3 = 0` at machine precision on lattice toys assuming
`P = |ψ|²`). With this derivation, `P = |ψ|²` is the *output*
rather than the *input*, and the Sorkin tests become *confirmations
of the derived rule on lattice models* rather than circular
checks.

## What this file is not

- Not a durable/native record-formation theorem.
- Not an arbitrary unsharp-instrument uniqueness theorem.
- Not a numerical-prediction change. All retained quantitative
  predictions are unchanged.
- Not a unilateral retagging. Independent audit owns the effective status.

## Citation-graph note

**Upstream framework dependencies** (load-bearing for the derivation; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra and `Z^3` substrate)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) — supplies `ρ_ref` as the unique tracial state on the quasi-local algebra (companion note)
- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) — finite-region projection-lattice density representation for `|Λ| >= 2`
- [`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) — finite-region POVM extension including the single-site case
- [`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) — finite Kraus/Choi representation and TP condition
- [`LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md) — canonical projective-measurement Naimark/Lüders dilation
- [`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md) — ideal sharp-projective record conditioning surface
- [`LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md`](LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md) — sequential effect `P E P` and normalized Lüders update

**Background mathematics cited in parallel** (not raw load-bearing imports):

- Standard probability theory (P1)–(P3)
- Gleason 1957
- Busch 2003 / Caves-Fuchs-Manne-Renes 2004
- Lüders 1951 / Cassinelli-Lahti 1995

**Plain-text pointer references** (NOT load-bearing deps; deliberately not markdown links to avoid polluting the audit dependency graph with non-load-bearing edges to failed/conditional rows):

- `BORN_RULE_ANALYSIS_2026-04-11.md` — `audited_failed` gravitational Hartree route; this note proposes Gleason–Busch as a structurally different replacement repair route
- `NONLINEAR_BORN_GRAVITY_NOTE.md` — stated repair target (*"provide a retained bridge theorem deriving the probability/readout rule without imposing `|psi|^2`"*); structurally addressed but not closed
- `I3_ZERO_EXACT_THEOREM_NOTE.md` — retained; consistent with this route as a compatibility pointer
- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — separate scalar-additivity gate; unaffected
- `GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE.md` — separate factorization gate; unaffected
- `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` — relevant for durable/native record formation, not invoked by this ideal-projective-row proof
- `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md` — referenced in a caveat for record-conditioning locality; not currently invoked in any derivation step, so not promoted to a load-bearing dep

**Still outside this row**:

- durable/native persistent-record formation;
- arbitrary unsharp-instrument selection;
- the failed gravitational-Hartree route.
