# Flavor — the (1,2)-vs-(1,1) generation-measure tie is NOT broken in favor of the observed value by any native positivity / normalization / modular principle: RP/T-positivity are AGNOSTIC; on-site unit-trace + KMS(β=0) + locality + Plancherel all FORCE the dimension measure (1,2) → Q=1

**Date:** 2026-06-02
**Claim type:** no_go / narrow native-principle demarcation (one angle of the charged-lepton Koide value).
**Status authority:** independent audit lane only. This note adds no axiom and no import, and sets no audit outcome. It is a /tmp deliverable from a single-angle attack; not landed.
**Runner:** `flavor_koide_measure_tiebreak_native_principles.py` (SCORECARD PASS=38 FAIL=0, venv-verified).

## Question (the angle)

The charged-lepton Koide value reduces (retained
`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`,
`charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10`)
to one weighting of the two `C₃` isotypes / minimal central idempotents of
`ℝ[Z₃] = ℝ ⊕ ℂ` (`e₀` = singlet, rank 1; `e₁` = doublet, rank 2):

- **(i) dimension / trace / Plancherel** weight `(1,2)` → `r=|b|²/a²=1` → **Q=1**;
- **(ii) block / idempotent-count** weight `(1,1)` → `r=1/2` → **Q=2/3** (observed).

Representation theory ranks neither a priori (retained no-gos
`koide_frobenius_isotype_split_uniqueness` and `action_normalization` both
decline to rank them).

**Is there an A1+A2-NATIVE principle — reflection positivity, KMS/modular
condition, locality/cluster, emergent-time T-positivity, or the on-site qubit
unit-trace normalization (`Tr=1`) — that SELECTS one of these two measures?**

## Verdict — NO (with a sharp asymmetry, and it does NOT favor the observed value)

**The tie is not broken in favor of the observed `Q=2/3` by any tested native
principle.** More precisely, the tested principles split cleanly into two camps,
and *neither camp lands on the observed value*:

1. **Reflection positivity / emergent-time T-positivity are AGNOSTIC.** The OS /
   transfer-matrix positivity Gram is positive for **both** candidate measure
   points (`r=1/2` and the `r=1` endpoint), and is PSD identically whether the
   doublet is realized as **one complex mode** (det_C → (1,1)) or **two real
   modes** (det_R → (1,2)) — the count lives in the field content/statistics,
   invisible to the covariance. RP/T-positivity selects only the **Hermitian
   readout class** (`H=iD`, the signed/Brannen reading), which holds for *every*
   `r`; it does not rank the measure. (Reproduces and re-verifies
   `FLAVOR_MEASURE_POSITIVITY_AGNOSTIC_NOTE_2026-05-31`.)

2. **On-site qubit unit-trace + KMS(β=0) + locality/cluster + Plancherel all
   FORCE the dimension measure (1,2) → Q=1.** This is the decisive, computed
   result of this angle:
   - The framework's **derived** reference state is the unique tracial state
     `ρ = ⊗ₓ I/2` (retained `pre_record_reference_state_tracial_derivation`,
     `powers_uhf_tracial_uniqueness`, `tomita_tensor_trace`). Restricted to the
     generation carrier it is `ρ_gen = I₃/3`, and its Born weight on the two
     central blocks is **`Tr(ρ e₀) : Tr(ρ e₁) = 1/3 : 2/3 = (1,2)`** — the
     dimension weighting → `r=1` → **Q=1** (runner BLOCK 2, exact).
   - The trace is the **β=0 (infinite-temperature) KMS state**; its
     Tomita–Takesaki modular operator is **`Δ=1`** (verified: the Tomita
     `S(x)=x*` is HS-anti-unitary, so `Δ=S^#S=1`, `S²=I`; runner BLOCK 3). A
     trivial modular flow reweights nothing → uniform per direction → again
     `(1,2)` → Q=1.
   - **Locality/cluster** gives the reference as a *product* state; the induced
     generation-block weight is `(1,2)` for **every** region size `|Λ|` (runner
     BLOCK 5). The product/trace structure is generation-block-agnostic — it
     fixes inter-site independence, not the within-doublet ratio, and what it
     *does* induce is again `(1,2)`.

So the native principles I was asked to test do **not** support the observed
value. The ones that have any selection power at all (`unit-trace`, `KMS`,
`locality`, `Plancherel`) all point at **`(1,2)` → Q=1**, the framework default;
the ones that are blind (`RP`, `T-positivity`) point at neither.

**The observed `(1,1)` → r=1/2 → Q=2/3 requires a NON-tracial / finite-β
weight** that none of these principles supply: realizing `(1,1)` as a Gibbs
factor needs `w₀/w₁ = exp(−β·gap) = 1/2`, i.e. `β·gap = ln 2 ≠ 0` — a finite
temperature / a dynamics (runner BLOCK 3 exhibits an explicit witness density
`diag(1/5,2/5,2/5)` with `gap = ln 2` that lands `r=1/2`, and verifies it is
**not** the tracial `I/3`). (Reproduces
`KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR_NOTE_2026-06-02` and
`FLAVOR_FIND_J_ROUND5`.)

## Anti-overreach discipline (the explicit honesty check)

The project memory records two failure modes to avoid: (a) privileging the
trace/dimension measure as "the consistent one" (a prior overreach toward Q=1),
and (b) privileging block-count toward Q=2/3 just because 2/3 is observed. This
note avoids **both**:

- **Not (b):** no tested native principle forces `(1,1)`. The `(1,1)` state is
  exhibited as fully admissible (PD, `C₃`-invariant, unit-trace — runner BLOCK 6)
  but **non-tracial**; admissibility is not forcing. The observed value remains
  an *unforced* selection from the standpoint of these principles.
- **Not (a):** the claim is **not** that `(1,2)`/Q=1 is "the consistent" or
  "the only" measure. `(1,1)` survives every native *constraint* (positivity,
  `C₃`-invariance, unit trace) — it is a different admissible state, not a
  forbidden one (runner BLOCK 6). The precise, defensible statement is the
  weaker and correct one: **among the tested native principles, the only one
  with a distinguished *selection* (the derived tracial reference) selects
  `(1,2)`; the others are blind.** This is a statement about which state the
  framework's *derived reference* is, not a ranking of the abstract measures.
  The retained no-gos `koide_frobenius_isotype_split_uniqueness` and
  `action_normalization` (both decline to rank `(1,1)` vs `(1,2)`) are **not**
  contradicted — this note does not rank the measures either; it locates which
  one the *native reference state* induces, and shows it is the one giving Q=1.

So the honest verdict is a **negative for the observed value**: the native
positivity/normalization/modular structure does not deliver `Q=2/3`. If anything
it is mildly evidence *against* `Q=2/3` being native-forced, since the framework's
own derived reference lands on `Q=1`. The observed value sits on a *non-tracial*
state that the tested principles neither forbid nor supply.

## Derive-vs-posit ledger

| principle | acts how on the (1,2)/(1,1) tie | derive or posit |
|---|---|---|
| Reflection positivity (OS) | AGNOSTIC — PSD for both counts, every physical r | selects readout class only (derived); measure: no selection |
| Emergent-time T-positivity | AGNOSTIC — same as RP (positive transfer ⟹ Hermitian H) | same |
| On-site qubit unit-trace `Tr=1` | FORCES `(1,2)` → Q=1 (derived reference `ρ=⊗I/2` ⟹ `ρ_gen=I/3` ⟹ blocks 1:2) | derived (retained tracial-reference chain) → Q=1 |
| KMS / Tomita–Takesaki modular | trace is β=0, `Δ=1` ⟹ no reweighting ⟹ `(1,2)` → Q=1 | derived → Q=1 |
| Locality / cluster | product/trace structure ⟹ `(1,2)` for all `|Λ|` | derived → Q=1 |
| (1,1) → Q=2/3 | requires non-tracial finite-β Gibbs weight (`β·gap=ln2`) | **POSIT / imported dynamics — not supplied by any tested native principle** |

## Import flags

- **IMPORT FLAG: requires user approval — a finite-β (non-tracial) reference
  state / temperature on the generation carrier.** This is the single ingredient
  the observed `(1,1)` → r=1/2 needs and that no tested native principle
  supplies. The framework's derived reference is the β=0 trace; selecting
  `(1,1)` requires departing from it. Adopting any finite-β / non-tracial weight,
  or a dynamics that lands one, is an import beyond A1+A2+retained.
- The reflection-positivity anchors (`axiom_first_reflection_positivity`,
  `osterwalder_schrader_from_framework`, `free_field_os_wightman_reconstruction`)
  are **`unaudited`** on the live ledger and are therefore **not load-bearing**
  here; the RP-agnosticism conclusion is carried by the explicit covariance
  computation (runner BLOCK 4), independent of those rows' tier.

## What is established vs not

- **Established (verified):** the exact line `Q=1/3+(2/3)r`; the two measure
  points; that the derived tracial reference induces `(1,2)`/Q=1 on the
  generation blocks via four independent native handles (unit-trace Born weight,
  `Δ=1` modular triviality, locality/`|Λ|`-independence, Plancherel); that RP/
  T-positivity are blind to the count; that `(1,1)` is admissible-but-non-tracial
  and needs a finite-β input.
- **Not established / not claimed:** that `(1,2)`/Q=1 is "the" measure or that
  `(1,1)`/Q=2/3 is excluded; a derivation of `Q=2/3`; any new axiom or import.

## Relation to the existing chain

This is the **native-principle** half of the angle named across the prior notes
(`FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT`,
`FLAVOR_MEASURE_POSITIVITY_AGNOSTIC`, `FLAVOR_FIND_J_ROUND5`,
`KOIDE_CARRIER_SCORING_NEEDS_NONTRIVIAL_MODULAR`,
`KOIDE_READOUT_LANE_DEMARCATION`). It consolidates them into one statement for
the specific principle-set (RP, KMS/modular, locality, T-positivity, unit-trace)
and adds the explicit **unit-trace Born-weight computation** showing the derived
on-site qubit normalization induces `(1,2)` on the generation blocks. It does not
weaken any retained no-go and does not load-bear on
`closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.

## The next path (open, not closing)

The result sharpens the open object exactly as the prior notes did: `r=1/2`
lives on a **non-tracial finite-β / 2-sector-coarse-grained** weight, and the
live question is whether the **emergent-time dynamics** (not the β=0 reference,
not RP, not locality, all of which give Q=1) *delivers* that finite-β structure
non-circularly — e.g. via a records/einselection 2-sector partition or a
chiral-mass-generation argument, both already flagged as `C³=I`-unobstructed.
The `N`-scaling cross-check survives: `(1,1)` gives `r=1/(N-1)`, tying `r=1/2` to
the derived `n_gen=3` — a structural constraint on any future finite-β
derivation.

## No-Go Discipline Gate (N1–N8)

- **N1 — Alternative route enumeration.** Five native principles checked:
  (1) RP — agnostic (PSD for both counts); (2) emergent-time T-positivity —
  same as RP; (3) unit-trace normalization — forces `(1,2)`/Q=1 (derived
  reference Born weight); (4) KMS/Tomita–Takesaki modular — trace `Δ=1`, no
  reweighting, `(1,2)`/Q=1; (5) locality/cluster — product/trace structure
  `(1,2)` for all `|Λ|`. None forces `(1,1)`/Q=2/3.
- **N2 — Wall-independence audit.** The principles collapse to two independent
  facts: RP/T-positivity blindness, and the derived-reference-is-the-trace fact.
  Closing one does not close the other; neither yields `(1,1)`.
- **N3 — Hidden-wall scan.** The tracial reference is the retained
  `pre_record_reference_state_tracial_derivation` chain; the finite-β witness is
  an explicit non-adopted state, not a hidden admission; the RP conclusion is
  carried by direct computation, not by the `unaudited` RP rows. No hidden
  physics input is used.
- **N4 — Residual matching.** `koide_frobenius_isotype_split_uniqueness` and
  `action_normalization` are cited only for the known absence of an a-priori
  ranking; this note does not rank the abstract measures, it identifies the
  native-reference-induced one.
- **N5 — Rhetoric audit.** "Native principles select `(1,2)`/Q=1" means the
  tested derived reference, modular, locality, and Plancherel handles. It does
  **not** mean `(1,1)` is forbidden, nor that no future dynamics can deliver it.
- **N6 — Partial-closure path scan.** A future audited finite-β / records /
  einselection dynamics could supply `(1,1)` without a new axiom. This note
  leaves that path open and does not require a new axiom.
- **N7 — Steelman.** A reviewer could argue the *physical* reference for mass
  generation need not be the pre-record β=0 trace — a finite-β equilibrium could
  be the relevant state, which would defeat this negative without contradicting
  it. That is exactly the open finite-β/dynamics handle named above; this note
  does not close it.
- **N8 — Cross-cycle echo.** The same `(1,1)`-vs-`(1,2)` wall recurs across the
  prior flavor notes; none was retired by a native principle. This note keeps the
  wall narrow (a specific principle-set) and does not relabel it as an axiom gap.

## Tiers verified on `origin/main` (`.rows[claim_id].effective_status`)

| claim_id | effective_status | role here |
|---|---|---|
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | `retained` | derived reference state = trace `ρ=⊗I/2` (the unit-trace selection) |
| `powers_uhf_tracial_uniqueness_on_qubit_lattice_narrow_theorem_note_2026-05-20` | `retained` | uniqueness of the tracial state on the qubit lattice |
| `tomita_tensor_trace_on_finite_dim_matrix_narrow_theorem_note_2026-05-20` | `retained` | tensor traciality (used in BLOCK 3 modular argument) |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | `retained` | `Q=1/3+(2/3)r` algebra |
| `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10` | `retained` | `Q=2/3 ⟺ r=1/2` biconditional |
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | `retained_no_go` | declines to rank `(1,1)` vs `(1,2)` |
| `action_normalization_note` | `retained_no_go` | declines to rank `(1,1)` vs `(1,2)` |
| `koide_q23_block_weight_frontier_bounded_note_2026-05-29` | `retained_bounded` | block-weight algebra anchor |
| `luders_rule_from_composition_consistency_note_2026-05-20` | `retained_bounded` | records-flow anchor for the finite-β next path |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | `retained_bounded` | chirality decoupling (this note introduces no chiral operator) |
| `inner_automorphism_invariance_tracial_identification_narrow_theorem_note_2026-05-20` | `audited_conditional` | trace = inner-automorphism-invariant state (context, not load-bearing) |
| `flavor_ba_ratio_bound_hs_equipartition_note_2026-05-30` | `audited_conditional` | HS-equipartition characterization (context) |
| `axiom_first_reflection_positivity_theorem_note_2026-04-29` | `unaudited` | RP anchor — **not load-bearing** (RP conclusion carried by direct computation) |
| `osterwalder_schrader_from_framework_narrow_theorem_note_2026-05-27` | `unaudited` | OS anchor — **not load-bearing** |
| `free_field_os_wightman_reconstruction_conditional_theorem_note_2026-05-30` | `unaudited` | statistics-selection gap (G3) — context for det_C/det_R blindness |
