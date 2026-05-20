# A3' Proposal: Maximum-Entropy Pre-Record Reference State

**Date:** 2026-05-20
**Status:** proposal — pre-audit, pre-derivation work
**Type:** meta (proposed framework axiom)
**Proposed addition to:** `MINIMAL_AXIOMS_2026-05-03.md` (current two-axiom set: A1, A2)

## Headline

**Reality is probability until recorded "bits" on a lattice.**

This proposal formalizes the half of that sentence that A1+A2 currently
leave unstated: what "probability" refers to when no records exist.
A1+A2 supply the *operator algebra* (`Cl(3) ≅ M_2(ℂ)` per site, composed
by `Z^3` tensor product); they are silent on which *state* is the
"pre-record" reference. A3' fills that slot.

## What this note proposes

This note proposes adding a third framework axiom, **A3'**, to the
current two-axiom set (A1 = `Cl(3)`, A2 = `Z^3`). The proposal is
motivated by a state-side gap surfaced by:

- `BORN_RULE_ANALYSIS_2026-04-11.md` — the Born rule is currently
  borrowed from QM, not derived; an attempted gravitational
  fixed-point derivation failed.
- `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md`
  — the maximally-mixed state does not emerge canonically from A1+A2
  + Born + physical-lattice; additional input is required to select
  it.
- `MINIMAL_AXIOMS_2026-05-03.md` (lines 33–46) — A1+A2 are explicitly
  algebraic / geometric only, with zero state-side content.
- `DECOHERENCE_DECISION_NOTE.md` (Axiom 9: "measurement is durable
  record formation") — already axiomatic on the record-formation
  side, but with no corresponding *pre-record* reference.

Without a pre-record reference, the framework cannot meaningfully ask
"what is the state of the system before any records have formed?"
That question is required for: (i) deriving the Born rule from
A1+A2-internal structure rather than borrowing it, (ii) giving the
word "vacuum" a non-circular meaning, and (iii) converting "in the
beginning there was uncertainty" from a heuristic into a structural
claim.

## The proposed axiom

**A3' — Maximum-entropy pre-record reference state.**

> Let `A = ⊗_{x ∈ Z^3} M_2(ℂ)_x` be the quasi-local operator algebra
> defined by A1+A2 (per-site `Cl(3) ≅ M_2(ℂ)` composed by `Z^3` tensor
> product). The canonical pre-record reference state on `A` is the
> unique tracial state
>
>   `ρ_ref = ⊗_{x ∈ Z^3} (I_2 / 2)`
>
> equivalently, the state of maximum von Neumann entropy on each
> per-site factor. Every physical prediction is a conditional
> expectation or relative-entropy quantity with respect to `ρ_ref`,
> updated under the persistent-record-formation lane.

`ρ_ref` is the state assigned to any subsystem about which no records
have formed. Records (in the sense of
`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` and the
`TELEPORTATION_*_RECORD_*` lane) update `ρ_ref` to a conditioned state
on the record value. "Reality" is then the family of
record-conditioned states; "probability" is the relative weight of
configurations under `ρ_ref` prior to recording.

## Why this axiom

### What A3' does that A1+A2 alone cannot

1. **Pins a state-side reference.** A1+A2 are operator-algebraic and
   state-neutral. The framework currently borrows the Born rule and
   treats initial conditions as externally specified. A3' makes the
   pre-record state canonical, with no continuous tuning freedom.

2. **Makes "vacuum" non-circular.** The framework's existing
   "vacuum-as-zero" language is ambiguous between (i) algebraic zero,
   (ii) ground state of a Hamiltonian, and (iii) maximum-uncertainty
   pre-record state. A3' fixes the foundational meaning to (iii).
   Dynamical ground states are then recategorized as *partial records*
   — states in which the system has acquired information about being
   low-energy — rather than as the fundamental reference.

3. **Converts "in the beginning there was uncertainty" into a
   structural claim.** Pre-dynamical cosmological initial conditions
   become `ρ_ref`. Record formation (decoherence, persistent local
   records) is what drives the universe's history from this reference
   toward record-rich configurations.

### What A3' is *not*

- **Not a derivation of state from algebra.** The `BAE_MAX_ENTROPY_*`
  obstruction proved that max-entropy cannot be forced from A1+A2 +
  Born + physical-lattice without additional input. A3' adopts the
  reference axiomatically; it does not derive it.
- **Not a sign convention.** A3' is state-side; it does not interact
  with the Grassmann (formerly A3) or `g_bare = 1` (formerly A4) open
  gates. The Grassmann signs are forced by spin-statistics on the
  per-site dim-2 Hilbert space (see
  `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`) and
  remain forced under A3'.
- **Not a change to dynamics.** A3' specifies the pre-record state,
  not the Hamiltonian or the Wilson action.
- **Not a unique-state postulate.** Record-conditioned states are
  ordinary density matrices, not pure states. A3' gives the
  reference; dynamics + records select the family.
- **Not a closure of existing audit-conditional rows.** A3' creates
  new derivation targets (listed below) and reframes state-side
  interpretation. It does *not* discharge any condition currently
  held open by the audit ledger. In particular:
  - `observable_principle_from_axiom_note` (`audit_status:
    audited_conditional`, #2 load-bearing) is blocked by a *scalar
    additivity premise* on `log|det(D+J)|` —
    `W(r_1 · r_2) = W(r_1) + W(r_2)`. This is an observable-side
    condition, not a reference-state condition. A3' is orthogonal to
    it and does not contribute to closing it.
  - `gauge_vacuum_plaquette_residual_environment_identification_theorem_note`
    (`audit_status: audited_conditional`) — A3' reframes the
    "measurement" step as a record-update on `ρ_ref`, but the
    factorization condition (which correlations decouple) stands.
  - `beyond_lattice_qcd_note` (`audit_status: audited_conditional`)
    fails because the runner *assumes* the Born readout it claims to
    derive. A3' makes the Born rule a *named* derivation target via
    Gleason–Busch on `ρ_ref`, but does not itself supply the proof.
  Readers should not infer that A3' resolves these or any other
  currently audit-conditional rows. The proposal's value is in
  creating new derivation lanes and pinning a previously unstated
  pre-record reference; closure of any audit-conditional row remains
  the responsibility of the named follow-up derivation notes.

## Consequences

### Derivation targets enabled by A3'

| Target | Mechanism | Status |
|---|---|---|
| Born rule derivation | Gleason–Busch theorem on `M_2(ℂ)` per site, extended to the quasi-local algebra via product structure | Open. Previous gravitational route failed (`BORN_RULE_ANALYSIS_2026-04-11.md`); Gleason–Busch route on the A3'-pinned reference is the natural retry. |
| Persistent-record kernel grounding | The `PERSISTENT_RECORD_*` kernel becomes "update of `ρ_ref` under environmental coupling" rather than a free-standing graph-memory construct | Existing lane retargeted with a canonical reference. |
| Vacuum-energy reframe | Zero-point sums `Σ ℏω/2` are no longer a primitive physical quantity; the dynamical-ground-state energy is a *relative entropy* (or relative free energy) with respect to `ρ_ref`, finite by construction | `COSMOLOGICAL_CONSTANT_RETENTION_WITH_R_BUDGET_THEOREM_NOTE_2026-04-29.md` should be re-read under this framing; `R` remains open but the conceptual obstruction shifts. |
| `λ(M_Pl) = 0` interpretation | "Minimal coupling at the Planck scale" may admit a derivation from "minimal departure from `ρ_ref` on the scalar sector" | `VACUUM_CRITICAL_STABILITY_NOTE.md` open derivation target; currently the boundary is an admitted-context input. |
| Cosmological initial condition | Pre-dynamical state is `ρ_ref`; records (decoherence + persistent local records) drive the arrow of time | Frontier lane; connects to `Hubble`-closure and `R_budget` open lanes. |

### What A3' explicitly does *not* change

All A1+A2-only theorems (`MINIMAL_AXIOMS_2026-05-03.md` lines 147–161)
are algebraic and depend on no state choice. They are unaffected:

- `cl3_per_site_uniqueness`
- `cl3_color_automorphism`
- per-site Pauli group structure
- per-site `su(2)` spin-1/2 algebra (R5 Block 03)
- no-per-site `γ_5` chirality (R6 Block 01)
- `Z_3` Fourier diagonalization on hw=1
- structural `Z^3` lattice geometry

All gate-dependent quantitative results are computed as conditional
expectations on a state that, before A3', was implicitly the lattice
trace and, after A3', is explicitly `ρ_ref` (or a record-conditioned
update). The numerical predictions agree on the relevant observables
(gauge-invariant correlators, partition functions, matrix elements):

- `α_s(M_Z) = 0.1181`, `v = 246.282818290129 GeV`, `m_t`, `m_H`, the
  CKM atlas, Koide `Q = 2/3`, electroweak normalization, neutrino
  bounds, dark-matter exact-target package, and all retained
  quantitative results are **unchanged**.
- Reflection positivity remains a theorem on the staggered-only and
  symmetric-canonical-Wilson surfaces. A3' does not weaken or
  strengthen the existing RP scope; it changes the interpretation
  (the Euclidean Wilson measure is absolutely continuous with respect
  to `ρ_ref`).

### What A3' is at risk of breaking (open compatibility checks)

1. **Infinite-volume well-definedness.** `ρ_ref` as a tracial state on
   `⊗_{x ∈ Z^3} M_2(ℂ)` is well-defined via the GNS construction on
   the UHF C*-algebra of type `2^∞`. This is standard but must be
   stated explicitly rather than asserted. Parent note: pending.
2. **Reflection-positivity ↔ A3' compatibility.** The Wilson measure
   is a positive measure on configurations, not the tracial state
   itself; the Radon–Nikodym derivative `dμ_Wilson / dρ_ref` should be
   identified. Parent note: pending.
3. **Cosmological-constant value.** The reframe converts zero-point
   sums into relative entropies, but the numerical value of `Λ` is
   not determined by A3' alone. The existing `Λ = 3/R²` identity
   holds; `R` remains open.

## Relationship to existing open gates

A3' is *orthogonal* to the two existing open gates:

- The **Grassmann staggered-Dirac realization gate** (formerly A3)
  specifies fermion-sector dynamics. Its closure imports
  anticommutation by force (spin-statistics on per-site dim 2), not by
  choice. A3' does not alter this.
- The **`g_bare = 1` derivation gate** (formerly A4) specifies gauge
  normalization. Its closure pins canonical trace + Casimir rigidity
  (`G_BARE_RIGIDITY_THEOREM_NOTE.md`). A3' does not alter this.

Under A3' adoption, the framework's parameter reduction becomes:

> 19 SM numerical parameters → **3 framework axioms + 2 named open
> gates**, with explicit closure paths for each gate and explicit
> derivation targets for each A3'-enabled lane.

## Lanes that should be reviewed under A3'

If A3' is adopted, the following existing lanes shift in
interpretation (numerical predictions are unchanged unless flagged):

1. `BORN_RULE_ANALYSIS_2026-04-11.md` — retarget the failed
   gravitational derivation to a Gleason–Busch derivation on the
   A3'-pinned reference.
2. `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md`
   — the obstruction becomes structurally irrelevant under A3'
   (max-entropy is axiomatic, not derived).
3. `DECOHERENCE_DECISION_NOTE.md` Axiom 9 — gains a definite
   reference state to update from; the "measurement is durable record
   formation" axiom is then a direct counterpart of A3'.
4. `PERSISTENT_RECORD_*` lane — the overlap kernel becomes a definite
   update rule on `ρ_ref`. Previously it was defined on graph-memory
   states without a canonical reference.
5. `TELEPORTATION_*_RECORD_*` lane — the apparatus model gains an
   explicit pre-record state; the Bell-stabilizer transducer becomes
   a record-update on `ρ_ref` rather than on an externally specified
   pre-measurement state.
6. `VACUUM_CRITICAL_STABILITY_NOTE.md` — `λ(M_Pl) = 0` admits a
   candidate derivation via "minimal departure from `ρ_ref` on the
   scalar sector"; currently this boundary is an admitted-context
   input.
7. `COSMOLOGICAL_CONSTANT_RETENTION_WITH_R_BUDGET_THEOREM_NOTE_2026-04-29.md`
   — zero-point sums are reinterpreted as relative entropies; the
   open `R` derivation question is reframed but not closed.

## Open derivation targets created by A3'

A3' creates the following named derivation targets, each with a
canonical parent note pending:

1. **Born rule from A3' (parent note: pending).** Gleason–Busch
   derivation of the Born rule on the A3'-pinned reference, extended
   from per-site `M_2(ℂ)` to the quasi-local algebra. Should close
   `BORN_RULE_ANALYSIS_2026-04-11.md`'s open status.
2. **`ρ_ref` thermodynamic-limit construction (parent note:
   pending).** Tracial state on `⊗_{x ∈ Z^3} M_2(ℂ)` via GNS on UHF
   type-`2^∞`. Standard mathematics; should be a short note.
3. **Reflection-positivity ↔ A3' compatibility (parent note:
   pending).** Make the Radon–Nikodym density of the Wilson measure
   with respect to `ρ_ref` explicit; verify that RP Case A and Case B
   remain provable under the A3' reading.
4. **Record-update axiom compatibility (parent note: pending).** Show
   that the existing persistent-record kernel (`gamma`-parameterized
   overlap) is a CPTP map on `ρ_ref` and its conditional updates,
   compatible with A3'.

## Comparison with prior framings

**Prior (`MINIMAL_AXIOMS_2026-05-03.md`):**

> "Framework has 2 axioms (`Cl(3)`, `Z^3`). The fermion realization
> and gauge normalization are open gates."

**Under A3' adoption (proposed):**

> "Framework has 3 axioms (`Cl(3)`, `Z^3`, maximum-entropy pre-record
> reference state `ρ_ref`). The fermion realization and gauge
> normalization remain open gates. The Born rule, persistent-record
> grounding, and vacuum-energy reframe become explicit derivation
> targets. Reality is probability until recorded bits on a lattice:
> `ρ_ref` is the pre-record probability; records form via dynamics +
> decoherence and produce definite bits anchored at `Z^3` sites."

## What this file is not

- Not a derivation. A3' is a proposed axiom, evaluated by the
  framework's owner; it is not derived from prior content.
- Not a numerical-prediction change. All quantitative retained
  results are unchanged.
- Not a unilateral re-axiomatization. This is a proposal note
  documenting the conceptual case and the derivation targets that
  would follow from adoption.
- Not a replacement for the publication matrix.
- Not a closure of `BAE_MAX_ENTROPY_*`. That note's obstruction
  stands as a *derivation* obstruction; A3' bypasses it by
  *adopting* the reference rather than deriving it.

## Citation-graph note

This note has no upstream load-bearing dependencies. The plain-text
references to existing notes (`BORN_RULE_ANALYSIS_2026-04-11`,
`BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent`,
`DECOHERENCE_DECISION_NOTE`, `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE`,
`TELEPORTATION_MEASUREMENT_RECORD_NOTE`,
`MINIMAL_AXIOMS_2026-05-03`,
`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29`,
`Q_INTEGER_SPECTRUM_THEOREM_NOTE_2026-05-02`,
`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07`,
`G_BARE_RIGIDITY_THEOREM_NOTE`,
`VACUUM_CRITICAL_STABILITY_NOTE`,
`COSMOLOGICAL_CONSTANT_RETENTION_WITH_R_BUDGET_THEOREM_NOTE_2026-04-29`)
are pointers to existing evidence for why the proposal is well-formed
and to lanes that would shift in interpretation if adopted. They are
not load-bearing axiom dependencies. A3' would itself be a new
framework input with zero upstream dependencies, on par with A1 and
A2.
