# Born Rule from Gleason–Busch on the Pre-Record Reference State

**Date:** 2026-05-20
**Status:** proposal — pre-audit derivation note
**Type:** bounded_theorem candidate
**Closes (proposed):** the framework's named repair target on
`BORN_RULE_ANALYSIS_2026-04-11.md` (`audited_failed`), and the
adjacent circularity flagged on `NONLINEAR_BORN_GRAVITY_NOTE.md` —
*"provide a retained bridge theorem deriving the probability/readout
rule without imposing `|psi|^2`."*

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

1. **Gleason–Busch theorem** uniquely determines the form
   `p(E) = Tr(σ·E)` on the POVM effect algebra of `M_2(ℂ)` (Busch
   POVM extension for the per-site dim-2 case) and
   `⊗_{x∈Λ} M_2(ℂ)` (Gleason direct for `|Λ| ≥ 2`, `dim ≥ 4`).
2. **A1+A2 with no-extra-structure identification** pins
   `σ = ρ_ref = ⊗_x I/2` for the pre-record system (derived in the
   companion tracial-state note).
3. **Lüders update rule** for record conditioning is the unique
   CPTP map satisfying compositional consistency (admitted input;
   standard).
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

**Theorem (Gleason 1957, Busch 2003).** Any probability assignment
`p: E(A_Λ) → [0,1]` satisfying (P1)–(P3) has the form

> `p(E) = Tr(σ · E)`

for a unique density matrix `σ` on `H_Λ`.

**Domain of applicability.** Gleason's original theorem requires
Hilbert dim ≥ 3, which holds for `|Λ| ≥ 2` (since `dim H_Λ = 2^|Λ| ≥
4`). The single-site case (`|Λ| = 1`, `dim = 2`) is handled by
**Busch's POVM extension** (Busch 2003, Caves et al. 2004): the
extended additivity domain (POVM effects rather than projections only)
restores the uniqueness even at dim 2.

**This step does not depend on A3'.** It is a pure consequence of the
algebra structure given by A1+A2 plus the standard probability axioms
(P1)–(P3). No state-side input is required for Step 1.

## Step 2 — Pin σ to the derived pre-record reference

By `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`,
the unique tracial state on the quasi-local algebra is
`ρ_ref = ⊗_x I/2`. Under the no-extra-structure identification
premise (also admitted in that companion note), `ρ_ref` is the
pre-record reference state.

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

**Theorem (Lüders 1951; Cassinelli-Lahti 1995).** The unique
state-update map satisfying:

- **(U1)** Positivity preservation: `σ → σ'` with `σ' ≥ 0`
- **(U2)** Normalization preservation: `Tr(σ') = 1`
- **(U3)** Probability consistency with Step 1: for the
  post-conditioning effect `E'`, the joint probability decomposes as
  `p(P then E') = p(P) · p(E' | P)`
- **(U4)** Compositional consistency: `(σ|_P)|_{P'} = σ|_{P' · P}`

is the **Lüders rule**:

> `σ → σ|_P = (P σ P) / Tr(P σ P)` for projection `P`
>
> (or more generally, `σ → (K σ K†) / Tr(K σ K†)` for Kraus operator `K`)

**This step is the load-bearing admitted input.** Lüders' rule is
the standard quantum measurement update, but it depends on (U4)
compositional consistency, which is sometimes contested in the
foundations literature (some authors prefer "minimal disturbance"
updates that give the same predictions for projective measurements
but differ for unsharp measurements). The argument that (U4) is the
correct consistency condition rests on Bayes' rule applied to
sequential measurements. Standard, but admitted.

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

**That is Born's rule** — derived from A1+A2 plus operator-algebraic
standard theorems (Gleason–Busch, Lüders rule, finite-dim tracial
uniqueness, Powers' UHF), with the no-extra-structure identification
and Lüders' (U4) compositional consistency as admitted inputs.

## Caveats (real)

1. **Dim-2 Busch extension.** Gleason's original theorem requires
   Hilbert dim ≥ 3. For single-site measurements (`dim = 2`), Busch's
   POVM extension (Busch 2003; refined by Caves-Fuchs-Manne-Renes
   2004) restores uniqueness. The extension assumes additivity over
   the full POVM effect algebra, not just projections. This is a
   slightly stronger assumption than projective additivity, but
   matches the framework's commitment to POVMs as the natural
   measurement formalism.

2. **Lüders rule (U4) compositional consistency.** Some foundations
   literature (e.g., Marlow, Wright) explores update rules other
   than Lüders. The argument that Lüders is forced rests on Bayesian
   consistency for sequential measurements. The bounded-theorem
   status of this derivation reflects the (U4) admission.

3. **What is a "record" formally.** Step 3 takes "record corresponds
   to a Kraus operator" as a premise. The framework's existing
   `PERSISTENT_RECORD_*` lane delivers this in the lattice context,
   but formally connecting persistent-record kernels to Kraus
   operators is a separate derivation target.

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

## What this derivation closes

- **`BORN_RULE_ANALYSIS_2026-04-11.md`** (currently
  `audited_failed`): the prior derivation route (gravitational
  Hartree fixed-point) is replaced by the Gleason–Busch route. The
  failure mode (no proof of the gravitational contraction-rate
  argument) is irrelevant here; the new route uses operator-algebraic
  standard theorems instead.

- **`NONLINEAR_BORN_GRAVITY_NOTE.md`** repair target: *"provide a
  retained bridge theorem deriving the probability/readout rule
  without imposing `|psi|^2`."* This derivation does exactly that —
  the `|⟨φ|ψ⟩|²` form is the *output* of Step 4, not assumed by the
  derivation.

- **`BEYOND_LATTICE_QCD_NOTE.md`** circularity (the runner assumes
  `np.abs(psi)**2` to test Born): this derivation supplies the Born
  rule from upstream, so the test in the runner can be downstream of
  the derived rule rather than circular.

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

- Not a closure of the Lüders (U4) compositional-consistency
  admission. That premise is standard but not free; it is listed
  explicitly in `admitted_context_inputs`.
- Not a closure of the dim-2 Busch admission. That admission is
  standard but not Gleason-strict; it is listed explicitly.
- Not a numerical-prediction change. All retained quantitative
  predictions are unchanged.
- Not a unilateral retagging. The bounded-theorem candidacy depends
  on independent audit acceptance of the no-extra-structure
  identification, Lüders' (U4) consistency, and Busch's POVM
  extension.

## Citation-graph note

This note's mathematical content rests on:

- **Standard probability theory** (P1)–(P3) — universal background
- **Gleason 1957** — projection-valued measure case, dim ≥ 3
- **Busch 2003 / Caves-Fuchs-Manne-Renes 2004** — POVM extension to
  dim ≥ 2
- **Lüders 1951 / Cassinelli-Lahti 1995** — measurement update rule
- **Powers 1967** — UHF type `2^∞` tracial-state uniqueness (used
  via the companion derivation note)
- The framework's qubit-form A1+A2 — via
  `MINIMAL_AXIOMS_2026-05-20.md`
- The companion derivation note — via
  `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`

References to existing framework notes
(`BORN_RULE_ANALYSIS_2026-04-11`, `NONLINEAR_BORN_GRAVITY_NOTE`,
`BEYOND_LATTICE_QCD_NOTE`, `I3_ZERO_EXACT_THEOREM_NOTE`,
`CENTRAL_BAND_BORN_*`, `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE`,
`GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE`,
`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`,
`PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE`) are pointers — they
identify the framework lanes that this derivation closes, repairs,
or is compatible with. They are not upstream axiom dependencies.
