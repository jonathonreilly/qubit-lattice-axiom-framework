---
claim_id: three_axiom_coverage_audit_note_2026-06-04
claim_type_author_hint: meta
---

# Three-Axiom Coverage Audit: how much of the SM/gravity stack do {Lattice, Quantum, Record} + derivations reach?

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (strategic coverage map; sets no audit status)
**Status authority:** independent audit lane only. This is a survey/index note.
It promotes nothing, changes no row's `effective_status`, and adds no axiom,
primitive, admission, or import. It reads the `origin/main` ledger
(`docs/audit/data/audit_ledger.json`) and key source notes and classifies each
major framework target by its **current** standing.
**Primary runner:**
[`scripts/audit_companion_three_axiom_coverage_audit_2026_06_04.py`](../scripts/audit_companion_three_axiom_coverage_audit_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_three_axiom_coverage_audit_2026_06_04.txt`](../logs/runner-cache/audit_companion_three_axiom_coverage_audit_2026_06_04.txt)

## Axiom baseline being scored

The three named axioms of [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md):
**Lattice** (`Z^3` NN), **Quantum** (per-site qubit `M_2(C) = Cl(3,0)`),
**Record** (finite scalar record additivity, in the updated reading: an
irreversible registration of which real / CPT-even superselection sector is
realized — arrow, classical/quantum cut = real Wedderburn center, sector-weight
dial). Two approved framework **primitives** ride alongside the axioms in
`docs/audit/data/axiom_premise_nodes.json`: `minimal_axioms` and
`scale_reference_primitive` (`a^{-1}=M_Pl`, units only). The audit lane's
registry [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
records exactly **two** genuine dimensionless admitted derivation targets:
`AC_φλ` and `θ`.

Classification key: **DERIVED** (retained/positive on the three axioms + clean
derivations), **DERIVED-MODULO-INPUT** (structure derived; one named input
selects the value), **OPEN-GAP** (no derivation on the current surface). All
statuses below were read off the `origin/main` ledger on 2026-06-04.

## The 12-item coverage table

| # | target | class | load-bearing standing (ledger `effective_status`) | named input / gap |
|---|--------|-------|----------------------------------------------------|-------------------|
| 1 | **Gauge algebra `su(3)+su(2)+u(1)`** | **DERIVED** (algebra) | `native_gauge_closure_note` **retained**, `graph_first_su3_integration_note` **retained**, `cl3_color_automorphism_theorem` **retained**; `qubit_link_u2_connection_algebra` (unaudited) gives `u(2)=su(2)+u(1)` from the link-connection convention | the *Lie-algebra shape* is derived; chiral `SU(2)_L` restriction + the link-connection convention are not (feeds #4, #8) |
| 2 | **Spacetime signature (3,1)** | **DERIVED-MODULO-INPUT** | `anomaly_forces_time_theorem` **bounded_theorem (B-class)**; supports `single_clock_stone_finite_dim_uniqueness` (retained), `clifford_volume_chirality_even_dimension` (retained) | **ABJ anomaly→inconsistency** (one bare external admission) + Lorentzian real-time inheritance from the single-clock theorem |
| 3 | **Three generations** | **DERIVED** | `three_generation_observable_theorem`, `_count_corollary`, `_m3c_burnside`, `_no_proper_quotient` all **retained (positive_theorem)** | none for the **count** (the prize that stands cleanly) |
| 4 | **Chirality (generation/matter)** | **OPEN-GAP** | even-dim requirement `clifford_volume_chirality_even_dimension` **retained**; but generation/staggered realization: `flavor_emergent_chirality_no_transport` **audited_conditional**, `no_per_site_chirality_theorem` (no per-site γ₅), `cl3_frame_free_ambient_chiral_grading_no_go` + `cl3_chiral_body_diagonal_axis_forced_doublet_h_not_sourced` (2026-06-04 **no_go**) | a chiral grading on the **generation `R^3` factor** (C₃-orbit-splitting); spacetime γ₅ does not transport over (shared with #5) |
| 5 | **Charged-lepton Koide `Q=2/3` / `r=1/2`** | **DERIVED-MODULO-INPUT** | structure (carrier, exact `Q=1/3+(2/3)r`, channels, `2/9`, endpoint exclusion, `r=1/2`=2-sector equipartition stationary pt) on retained anchors; selection bounded | single Tier-A `AC_φλ` (sharpened: 2-sector partition + chiral/det_C readout). `flavor_r_half_is_a_stationary_point_not_forced` **retained_bounded**; `koide_r_reduces_to_chiral_vs_vector_yukawa_binary` **open_gate** |
| 6 | **Quark / neutrino mass structure** | **DERIVED-MODULO-INPUT** (structure) / OPEN (values) | same `Q=1/3+(2/3)r` line carries other dial lanes; `pmns_hw1_source_transfer_boundary` **retained_bounded**, `dm_neutrino_*` rows mostly unaudited/bounded | `AC_φλ` per sector **plus** the cross-type basis alignment (CKM/PMNS) — a strictly larger residual than #5 |
| 7 | **Hypercharge assignments** | **DERIVED-MODULO-INPUT** | exact SM hypercharges fall out of anomaly cancellation (AFT Step 2); `lh_doublet_su2_squared_hypercharge_anomaly_cancellation`, `su3_anomaly_forced_3bar_completion` (unaudited, positive-type) | inherits #2's **ABJ** admission; the overall `Y`-scale `Y₀` is a vacuous rescaling convention (not an input) |
| 8 | **Color `SU(3)` as internal color (not generation)** | **OPEN-GAP** | `z3_character_isomorphism_color_generation_open_gate` **open_gate**; `qubit_link_u2` shows native `su(3)` is dimension-obstructed on one qubit | the abstract-`su(3)` → physical-color identification (the same *species-bridge* class as `AC_φλ`'s sector→species map); top gating row `yt_ew_color_projection` (49 dependents) |
| 9 | **Born rule / probability** | **DERIVED-MODULO-INPUT** | `born_rule_from_gleason_busch_derivation`, `gleason_on_qubit_lattice`, `busch_povm_extension` (unaudited, positive-type) | the Gleason–Busch **measurement / non-contextual POVM** structure. The Record axiom does **not** supply it (`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO` 2026-06-05): Record gives additive readout *after* the scalar is supplied, not the branch→scalar / Born map |
| 10 | **CPT** | **DERIVED** | `cpt_exact_note` **retained (positive_theorem)**; decorations (mass/lifetime equality, CPT²=I) retained | none (the real / anti-Hermitian `D` structure gives it). The updated Record axiom's "real (CPT-even) sector" reading is consistent with this retained result |
| 11 | **Gravity / Planck scale** | **DERIVED-MODULO-INPUT** (law) / OPEN (scale self-consistency) | Newton law + `bh_quarter_wald_newton_coefficient` **retained**; `poisson_self_gravity_zero_coupling_exact_reduction` **retained**; broad gravity rows **retained_bounded** | absolute scale = approved `scale_reference_primitive`; the self-consistency that the natural unit **equals** the Planck length (`a/l_P=1`) is the separate **open** gravity derivation |
| 12 | **Higgs / EWSB / mass scale** | **OPEN-GAP** (value) | `ew_higgs_gauge_mass_diagonalization` **retained** (mechanism shape); `higgs_mass_*` chain almost entirely **unaudited / bounded**; `composite_higgs_mechanism` open_gate | the EW VEV / Higgs-mass *value* (`hierarchy_formula_ew_vev_observable_identification_bridge`, `higgs_lambda_m_pl_bounded_interval` open); EWSB pattern partly derived, scale not |

## Tally

- **DERIVED (clean, on the three axioms): 3** — generations (#3), CPT (#10),
  and the gauge **algebra shape** (#1, algebra only; its chiral restriction and
  color identification are separate gaps).
- **DERIVED-MODULO-INPUT: 5** — signature (#2), charged-lepton Koide (#5),
  quark/neutrino *structure* (#6), hypercharge (#7), Born (#9), gravity *law*
  (#11). (#6 and #11 are split targets: structure/law derived-modulo-input,
  the full mass spectrum / scale self-consistency open.)
- **OPEN-GAP: 4** — chirality (#4), internal color (#8), Higgs/EWSB *value*
  (#12), and the value-frontier halves of #6/#11.

## The minimal named-input set (the irreducible admissions)

Stripped of conventions and naming, the three-axiom framework currently still
needs this short list. Several candidate admissions **collapse onto each
other**:

1. **`AC_φλ`** — the generation mass pattern (the C₃-breaking phase δ) **plus**
   the abstract-sector → physical-species identification. For charged leptons
   this sharpens to two equivalent selectors: the **2-isotype-sector partition**
   and the **chiral / det_C readout** (chiral counts `b` once → `r=1/2`; vector
   counts `Re b, Im b` → `r=1`, per `koide_r_reduces_to_chiral_vs_vector_yukawa_binary`).
   This single admission therefore **absorbs** the "lane-assignment bit," the
   "`r=1/2` selection," and the **readout-class / √m-sign** dimension — they are
   one binary, not four inputs.
2. **Chirality on the generation `R^3` factor** — the C₃-orbit-splitting chiral
   grading. This is **shared** with #4's generation-ID chirality (spacetime γ₅
   does not transport: `flavor_emergent_chirality_no_transport`,
   `cl3_frame_free_ambient_chiral_grading_no_go`). It is *also* the chiral/vector
   binary of `AC_φλ` viewed at the operator level — i.e. **the same gate as (1)**.
3. **Color identification** — the abstract-`su(3)` → physical-color bridge
   (`z3_character_isomorphism_color_generation_open_gate`). Same *bridge class*
   as `AC_φλ`'s sector→species map, on the color factor.
4. **`θ`** — strong-CP `θ=0`, an admission the framework **shares with the
   Standard Model** (not a framework-specific deficit).
5. **ABJ anomaly→inconsistency** — the one bare external admission inside the
   (3,1) chain (#2, #7). A standard QFT result; an internal lattice companion
   was attempted (PR 402) and is the live closure target.
6. **Gleason–Busch measurement structure** — the non-contextual POVM premise
   that turns the Quantum axiom into the Born weight (#9).

Plus the **approved primitives** (not admissions): the `scale_reference_primitive`
(one ruler, zero dimensionless content) and the three-axiom node itself.

**Net irreducible count:** the genuine *framework-specific* admissions reduce to
**one physics binary** (chiral-vs-vector on the C₃ generation factor — which is
simultaneously `AC_φλ`'s value-selector and #4's chirality gate), **one bridge
pattern** (abstract-rep → physical-species, instantiated for both color #8 and
flavor), plus **two imports the SM also makes** (`θ`, ABJ) and **one
measurement-foundations premise** (Gleason–Busch). The scale is a primitive,
not an admission.

## How close to "everything from 3 axioms"?

**PLAUSIBLE, not FAR — but gated on one deep binary and one bridge pattern.**
The skeleton is derived: the gauge algebra, the generation count, CPT, the
spacetime signature (modulo a standard QFT import), the Koide *structure*, the
hypercharges, the Born rule (modulo measurement foundations), and the gravity
*law*. The framework reproduces the headline phenomenology with the named pins.
The gaps are **not** a long list of independent walls — the survey's main
finding is that **the candidate admissions are correlated**:

- the lane-assignment bit, `r=1/2`, the chiral/vector readout, the √m-sign
  class, and the generation-ID chirality gate are **the same single binary**:
  *is the generation mass/Yukawa fluctuation determinant chiral/holomorphic
  (→ count `b` once → `r=1/2`, distinct massive leptons) or vector/real
  (→ `r=1`)?*
- internal color (#8) and the flavor species-bridge inside `AC_φλ` are the
  **same bridge pattern** (abstract irrep → physical species), on two factors.

So "everything from three axioms" is **one chirality/holomorphy binary + one
representation→species bridge + the SM-shared (`θ`, ABJ) imports + a
measurement-foundations premise** away — a handful of *correlated* named items,
not dozens of independent ones. This is the strategic case for the program being
closeable rather than open-ended: collapse the chirality binary and the
species-bridge and the count of framework-specific admissions drops toward the
SM-shared floor.

## Top-leverage remaining gaps (where closure buys the most coverage)

1. **The chirality / holomorphy binary on the generation `R^3` factor.** Closing
   it (deriving that the generation determinant is chiral, not vector) would
   convert **#4 → DERIVED** and discharge the value half of **#5** (and the
   charged-lepton mass ratios, Brannen relations, every `Q=2/3` consumer) — and
   it is the *same* gate, so it is a single derivation buying two table rows plus
   the largest downstream cone. Live leads: `supertrace_index_holomorphic_route_to_koide_r_half`
   (open), `koide_r_reduces_to_chiral_vs_vector_yukawa_binary` (open_gate), the
   einselection / pointer-basis route in `flavor_r_half_is_the_records_flow_separatrix`.
2. **The abstract-rep → physical-species bridge** (color #8, and the flavor
   species map inside `AC_φλ`). The color instance gates **49** downstream rows
   (`yt_ew_color_projection`) — the single highest-leverage backlog node. A
   derivation that the `Z₃` character isomorphism *is* the physical color/flavor
   identification would move **#8 → DERIVED** and tighten #5/#6/#7.
3. **The ABJ internal companion** (the one bare external admission in the (3,1)
   chain). Landing a lattice Wess–Zumino/Fujikawa successor for admission (i)
   would move **#2 and #7** from a bare-import bridge to an internally-closed
   bridge — and these two rows already carry the SM hypercharges, so the payoff
   is the entire chiral-gauge consistency spine.

## What this note explicitly does NOT do

- Does not set, promote, or change any row's `effective_status`.
- Does not add or rename any axiom, primitive, admission, or import.
- Does not claim any OPEN-GAP is closed or any gap-set is exhaustive; every gap
  is framed as a path the framework opens, not a closed search space.
- Uses plain-text backtick cids in the input set so the citation-graph builder
  creates no spurious dependency edges from this index.
