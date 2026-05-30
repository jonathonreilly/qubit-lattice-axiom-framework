# Admitted-Input Registry — Tier A (Central Index of Named Non-Axiom Admissions)

**Date:** 2026-05-23
**Claim type:** meta
**Status authority:** independent audit lane only. This is an index/meta note. It
sets **no** audit status, promotes nothing, and changes no row's grade. It names
and tracks, in one place, the framework's irreducible admitted inputs so they
are not scattered across lanes as ad-hoc prose premises.

## Purpose

A single, curated registry of the framework's **Tier-A admitted inputs** — the
non-axiom inputs that (a) gate downstream work and (b) carry a *retained-no-go
portfolio* (i.e. derivation has been attempted and proven hard, so closing them
needs a yet-to-be-found mechanism). This is deliberately **separate** from:

- **Framework primitives** (one-qubit operator algebra at every site plus the
  `Z^3` spatial substrate): foundational, never to be derived; tracked in
  `docs/audit/data/axiom_premise_nodes.json`.
- **The in-progress derivation backlog** (~110 `audited_conditional`/`unaudited`
  rows that gate downstream but have *no* no-go portfolio — they simply await
  auditing/re-grounding, not a new mechanism). That backlog is the
  conditional-dependency frontier (see Appendix), not an admission.

Survey basis (live ledger, 2026-05-23): of 720 retained-grade rows, 703 have
all-retained dependencies; only 6 non-retained inputs touch retained rows
directly. The genuine admitted inputs gating the *bounded* corpus number ~118;
curated to those that are irreducible (no-go portfolio) **and not vacuous**, the
genuine admitted inputs are the **four** derivation-targets below (P1, AC_φλ, S,
θ). Two further rows (Y₀, g₀) are **vacuous rescaling conventions** — listed for
completeness but, like the AC_φλ naming, explicitly **not** counted as admitted
inputs (see "Rigor-pass refinement" below).

## Tier A-1 — Admitted derivation-targets (irreducible; have no-go portfolios)

| id | statement | leverage | no-go portfolio (verified `retained_no_go` rows) |
|---|---|---|---|
| **P1** | scalar observables are additive over independent subsystems ⇒ `W = log\|det(D+J)\|` | ~88 | `observable_principle_p1_bridge_{connes_nc_spectral, extensivity_primitive, jones_index_subfactor, locality_of_source_derivatives, tomita_gibbs_modular, structural_reframing}_..._2026-05-21` (6) |
| **AC_φλ** | the generation **mass pattern** (the C₃-breaking phase δ) + the abstract-sector → physical-species identification. The *naming* (which sector is e/μ/τ) is a vacuous relabeling, **not** an input. | ~41 | `koide_a1_radian_bridge_irreducibility`, `koide_delta_lattice_wilson_selected_eigenline_no_go`, `koide_delta_marked_relative_cobordism_no_go` (3) |
| **Scale** (was `S`) | the single **scale reference** — `a^{-1} = M_Pl` (the Planck scale): one dimensionful number that sets the physical scale, and thereby the units. Irreducible by dimensional analysis (a scale cannot come from the dimensionless `A_min`). *Whether this counts as an admitted empirical import or a framework-native unit declaration is deferred — see note below.* | pervasive | `planck_finite_response_no_go`, `planck_parent_source_hidden_character_no_go`, `planck_boundary_orientation_incidence_no_go` (3) |
| **θ** | the QCD vacuum angle `θ = 0` (strong-CP) | ~20 | `strong_cp_rp_half_cannot_forbid_cp_odd_imaginary_no_go_note_2026-05-16` (1); also unsolved in the Standard Model |

Notes:
- **P1** is *principle-grade* (mild): it is the extensivity/additivity that defines
  an extensive observable; its no-go portfolio shows additivity⟺log is circular,
  so it is a candidate to be **admitted as a stated principle** (not necessarily
  ever "derived").
- **AC_φλ — de-named (the labeling itself is not an input).** The gate states
  this as a labeling bijection `π:{c₁,c₂,c₃}→L₃`, but a bijection between two
  *bare* 3-element sets is pure relabeling with **zero physical content** — the
  *names* (which sector is electron/muon/tau) are **not** an admitted input and
  must not be banked as one. Stripped of naming, the genuine admission is two
  physical things: (i) the **mass pattern** — the C₃-breaking phase δ, which
  collapses into the *same* δ tracked as the Koide phase; and (ii) the
  **abstract-sector → physical-species** identification (an interpretive bridge,
  akin to the abstract-su(3) → physical-color gap). A third non-naming residual,
  *across* fermion types, is the relative alignment of the up/down/lepton mass
  bases (the mixing/CKM-PMNS structure). The gate's three closers
  (labeling-convention / C₃-breaking dynamics / PDG) and its `a3_route1..5`
  attempts (`unaudited`, not retained no-gos, listed as *attempts*) target the
  **pattern**, not the names. Net: AC_φλ is *not* a discrete 6-way labeling
  choice; the irreducible content is "the δ-pattern + the species bridge."
- **Scale (was `S`, for "scale-setting") — the single scale reference: `a^{-1} = M_Pl` (the Planck scale).** Two
  things are distinct. (i) The *unit choice* (meters vs Planck units vs natural
  units) is vacuous — a pure convention, like the AC_φλ naming. (ii) The genuine
  content is the *one dimensionful number* fixing the physical scale of the
  lattice spacing `a`, taken to be the Planck scale (`a^{-1} = M_Pl`). This
  single scale-setting is **irreducible by dimensional analysis**: `A_min` (pure
  `Cl(3) ⊗ Z^3`) carries zero dimensionful content, so every derived quantity is
  dimensionless or carries `[a]^n`, and exactly one dimensionful observable must
  be supplied to fix `a` — the unit reference. The three `planck_*_no_go` rows
  are consistent with this: they show the scale/carrier is not forced by symmetry
  alone, i.e. it behaves as the unit, not a theorem.
  - **Status of the identification `UNIT = Planck` (taken, not derived).** The
    package carries `a^{-1} = M_Pl` as the explicit pin
    (`PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md` §1). Whether the framework
    *derives* that its natural unit self-consistently equals the Planck length —
    the closure `a/l_P = 1` — is the open gravity lane: the conditional theorem
    `BP ⇒ a/l_P = 1` (`PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md`),
    whose entire forward chain (P_A selection, `c_cell = 1/4`, boundary-density
    extension, source-unit normalization, and the BP carrier premise itself) is
    currently `unaudited` per the 2026-05-30 chain audit. So `UNIT = Planck` is
    *taken*, not yet derived.
  - **Deferred classification.** Whether this single unit reference is counted as
    an *admitted empirical import* (one number taken from the world) or recast as
    a *framework-native unit declaration* (the trivial scale-fixing every
    physical theory makes, carrying no dimensionless physics) is left **open and
    to be decided later**. Either way it is the *only* dimensionful thing the
    structural core takes; the remaining open work is entirely on the
    dimensionless side (P1, θ, AC_φλ-δ).
- **θ** is admitted here exactly as the Standard Model admits it (the strong-CP
  problem); not a framework-specific deficit.

## Conventions — NOT admitted inputs (vacuous rescaling freedoms)

These two are **vacuous rescaling conventions** with zero physical content
(exactly parallel to the AC_φλ *naming*): a convention is not an input. They are
listed only so the survey is complete; they are **excluded from the
admitted-input count**.

| id | statement | leverage | why vacuous |
|---|---|---|---|
| **Y₀** | absolute hypercharge normalization (the `α=1/3` step) | ~18 | the `(2,3)+(2,1)` *structure* and the hypercharge *ratios* are retained-derived (#1755, `koide_y_substrate_anomaly_forcing_note_2026-05-08_probey_substrate_anomaly`); the overall `Y`-scale is a rescaling `Y ↔ g'` that leaves physics invariant — a gauge/normalization choice, not a number |
| **g₀** | bare coupling `g_bare = 1` | ~8 | `beta_gbare_rescaling_abstract_identity_narrow_theorem_note_2026-05-10` (retained) shows `g_bare` is rescaling-invariant (`g ↔ β`) — a gauge choice, not a number to derive |

**They are distinct, not mergeable:** Y₀ is the U(1) hypercharge normalization,
g₀ is the SU(3) color bare coupling (`β = 2N_c/g_bare²`, N_c=3) — different
gauge factors. (An earlier draft suggested merging them; that was wrong. The
correct move is to drop *both* as vacuous conventions, not merge them.)

## Rigor-pass refinement (2026-05-23)

Applying the AC_φλ de-naming lesson uniformly to every Tier-A item:

- **P1, θ, AC_φλ:** stand as genuine admitted inputs (P1 principle-grade; θ
  shared with the SM; AC_φλ = δ-pattern + species bridge, naming excluded).
- **Scale (was `S`):** restated above as the single **scale reference**
  `a^{-1} = M_Pl` (the Planck scale) — irreducible by dimensional analysis,
  *taken not derived*, with its classification (admitted empirical import vs
  framework-native unit declaration) explicitly **deferred**. So the
  genuine-admitted-input count below is "three dimensionless admissions (P1, θ,
  AC_φλ) **plus** one scale reference (Scale, import-vs-native deferred)."
- **Y₀, g₀:** vacuous rescaling conventions — **dropped** from the
  admitted-input count (a convention is not an input, just as a name is not).
- **θ rigor check:** verified NOT derivable from the retained
  real/anti-Hermitian `D` structure —
  `strong_cp_rp_half_cannot_forbid_cp_odd_imaginary_no_go` (retained_no_go)
  explicitly shows the real/RP-half structure cannot forbid the CP-odd term, so
  θ=0 remains a genuine admission (shared with the SM).

Net stratified by character: **three dimensionless admissions** — AC_φλ
(framework-specific physics), P1 (a mild principle), θ (an SM-shared problem) —
**plus one dimensionful scale reference**, Scale = `a^{-1} = M_Pl` (the Planck
scale), whose status as a counted import vs a framework-native unit declaration
is **deferred**. The dimensionless three are the genuine open derivation work;
Scale is the single scale-setting every physical theory takes, orthogonal to all
of them (the Planck scale cannot supply any dimensionless number).

## Propagation wiring (audit-lane sidecar)

The framework already has the machinery: `compute_effective_status.py` makes a
row retained-grade iff every one-hop dependency is retained-grade (transitive),
and `premise_nodes.py` reads a machine registry (`axiom_premise_nodes.json`) of
chain-satisfying premises. The Tier-A sidecar adds:

1. A registry data file `docs/audit/data/tier_a_admissions.json` listing the
   Tier A derivation-target ids separately from convention metadata.
2. A new accepted-premise class for Tier-A derivation targets in
   `premise_nodes.py`: chain-satisfying **only at `retained_bounded`** (so
   dependents are cleanly *bounded*, not blocked), but explicitly distinct from
   axioms (which are never-to-be-derived). Convention rows are not accepted
   premises, because the existing convention parent notes carry more than the
   vacuous normalization choice and must not be laundered as theorem inputs.
3. The convention that any lane consuming a Tier-A admission lists its id as a
   **real `deps` edge** (or a structured `admitted_context_inputs` field), not
   prose — otherwise auto-propagation cannot fire.

With (1)–(3), deriving a Tier-A item is two mechanical steps — land a retained
theorem for it, remove it from `tier_a_admissions.json` — after which
`compute_effective_status` automatically cascades every transitive dependent
from `retained_bounded` toward full `retained`/`positive_theorem` on the next
pipeline run when otherwise eligible. **No back-links are maintained by hand;
the reverse cascade is computed.**

This is a **governance decision**: it widens the chain-satisfying premise set
beyond pure axioms while preserving the bounded label for any dependency on an
unretired Tier-A derivation target.

## What this note does NOT do

- Does **not** set, promote, or change any row's `effective_status`.
- Does **not** add Tier-A ids to `axiom_premise_nodes.json`.
- Does **not** promote Tier-A derivation-target dependents to unbounded retained
  status; the machine policy keeps those rows bounded until the relevant
  admission is retired.
- Does **not** treat any admission as derived; Tier A-1 items remain open.
- Does **not** consume any PDG value, fitted selector, or comparator.
- Uses plain-text backtick cids (no markdown links), so the citation-graph
  builder does not create spurious dependency edges from this index.

## Appendix — full conditional-dependency frontier (auto-generatable)

The complete set of ~118 non-retained rows that gate ≥1 downstream row (the
"bounded backlog") is *not* reproduced here; it is mechanically reproducible
from the ledger (for each non-retained row, count rows listing it in `deps`).
Top gating rows beyond Tier A include `yt_ew_color_projection` (49),
`plaquette_self_consistency` (43), `three_generation_observable_no_proper_quotient`
(19), `axiom_first_lattice_noether` (17) — these are derivation/audit backlog,
not irreducible admissions, and must not be conflated with the Tier-A registry.

## Cross-references (plain-text, non-load-bearing)

- `docs/audit/data/axiom_premise_nodes.json` — the existing axiom-premise
  registry this Tier-A registry parallels.
- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` (P1 parent),
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (AC_φλ parent),
  `HYPERCHARGE_IDENTIFICATION_NOTE.md` (Y₀), `G_BARE_RIGIDITY_THEOREM_NOTE.md`
  (g₀) — canonical parents / convention-reference rows for the listed items.
