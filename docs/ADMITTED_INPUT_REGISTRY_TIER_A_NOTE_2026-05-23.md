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

- **Framework axioms and approved primitives** (the named Lattice, Quantum, and
  Record axioms, and any explicitly approved primitive such as the
  scale-reference primitive): foundational, never to be derived; tracked in
  `docs/audit/data/axiom_premise_nodes.json`. These dependencies
  chain-satisfy without bounding downstream status.
- **The in-progress derivation backlog** (~110 `audited_conditional`/`unaudited`
  rows that gate downstream but have *no* no-go portfolio — they simply await
  auditing/re-grounding, not a new mechanism). That backlog is the
  conditional-dependency frontier (see Appendix), not an admission.

Current registry basis (2026-06-04): Record/P1 scalar additivity is no longer a
Tier-A admission. It is included in the explicitly approved three-axiom
`minimal_axioms` node, with the narrow Record boundary stated in
`docs/MINIMAL_AXIOMS_2026-06-04.md`. The older
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not promoted: it remains a broader
conditional parent carrying readout/log-det/modulus material beyond Record.

Curated to inputs that are irreducible (no-go portfolio) **and not vacuous**,
the genuine Tier-A admitted derivation targets are now the **two** rows below
(AC_φλ and θ). The scale-reference primitive is likewise not counted here: it
is the explicitly approved units primitive registered in
`docs/audit/data/axiom_premise_nodes.json`. Two further rows (Y₀, g₀) are
**vacuous rescaling conventions** — listed for completeness but, like the
AC_φλ naming, explicitly **not** counted as admitted inputs (see
"Rigor-pass refinement" below).

## Tier A-1 — Admitted derivation-targets (irreducible; have no-go portfolios)

| id | statement | leverage | no-go portfolio (verified `retained_no_go` rows) |
|---|---|---|---|
| **AC_φλ** | the generation **mass pattern** (the C₃-breaking phase δ) + the abstract-sector → physical-species identification. The *naming* (which sector is e/μ/τ) is a vacuous relabeling, **not** an input. | ~41 | `koide_a1_radian_bridge_irreducibility`, `koide_delta_lattice_wilson_selected_eigenline_no_go`, `koide_delta_marked_relative_cobordism_no_go` (3) |
| **θ** | the QCD vacuum angle `θ = 0` (strong-CP) | ~20 | `strong_cp_rp_half_cannot_forbid_cp_odd_imaginary_no_go_note_2026-05-16` (1); also unsolved in the Standard Model |

Notes:
- **Record/P1 scalar additivity retired from Tier A (2026-06-04).** The
  owner-approved Record axiom states only that a finite scalar record
  functional is additive over disjoint record collections, with an explicit
  additive-baseline convention. It does not import P2/modulus, log-det,
  source/action, measurement, Born weights, dynamics, normalization, scale, or
  arbitrary observable identification. The old P1 parent note is therefore not
  an axiom authority; rows that need only Record should cite
  `MINIMAL_AXIOMS_2026-06-04.md`, while rows that need the older parent's
  additional readout/log-det content must cite separate retained authorities or
  remain bounded/pending.
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
- **AC_φλ — charged-lepton sharpening (2026-06-02).** For the charged-lepton
  sector specifically, the "mass pattern" admission decomposes (verified, see
  `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`) into **two named,
  equivalent selectors**, both shown to be the operative inputs and neither
  derivable on the current surface: **(i) K-reality** (time-reversal-reality of
  the generation-monitored coupling / δ=0 / transpose-symmetry `b=c̄`) — selects
  the **2-isotype-block partition** over the 3-mode one (else `r=0`); and **(ii)
  det_C / equal-power-per-block** (the block-counting measure) — selects `r=1/2`
  (Q=2/3) over `r=1` (Q=1) *within* the 2-block structure, where the Born/dimension
  measure gives `r=1`. The *structure* (carrier, exact `Q=1/3+(2/3)r`, channels,
  topological `2/9`, endpoint exclusion, `r=1/2` as the 2-sector-equipartition
  stationary point) is derived; only this two-pronged selection is admitted.
  No-go portfolio sharpened this session: [KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  (retained_no_go — singlet:doublet ratio free), [KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md](KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md)
  (retained_no_go — no canonical zero-section), [KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  (retained_bounded); and the records/decoherence flow makes `r=1/2` the *unstable
  separatrix* of the (entropy-decreasing) sharpening map `r→2r²` while the
  entropy-increasing thermalizing flow makes it the *stable* 2-sector-entropy
  attractor — so the admission is precisely "which coarse-graining + which arrow."
  This matches Koide's own Z₃ parametrization (arXiv:1301.4143), which leaves the
  per-sector ratio a free fit.
- **Scale-reference primitive (`a^{-1} = M_Pl`).** The single dimensionful
  reference fixing the physical scale of the lattice spacing `a` is now an
  explicitly approved framework primitive, registered as `scale_reference_primitive`
  in `docs/audit/data/axiom_premise_nodes.json` with source
  [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md). It is
  irreducible by dimensional analysis: the named Lattice, Quantum, and Record
  axioms carry zero dimensionful content, so every derived quantity is
  dimensionless or carries `[a]^n`, and exactly one dimensionful
  reference must be supplied to fix units. A lane whose only otherwise
  non-retained dependency is this primitive is **not** bounded merely for using
  that unit reference. The primitive carries no dimensionless content and does
  not assert `a/l_P = 1`; the self-consistency that the natural unit equals the
  Planck length remains the separate open gravity derivation.
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

## Rigor-pass refinement (2026-06-04)

Applying the AC_φλ de-naming lesson uniformly to every Tier-A item:

- **Record/P1 scalar additivity:** retired from Tier A and included in the
  approved `minimal_axioms` node as the narrow Record axiom. This retirement
  does not promote the old `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` parent,
  which contains additional non-axiom material.
- **θ and AC_φλ:** stand as genuine admitted derivation targets (θ shared with
  the SM; AC_φλ = δ-pattern + species bridge, naming excluded).
- **Scale reference:** removed from Tier A and registered as the
  explicitly approved `scale_reference_primitive`. It is a units primitive, not a
  derivation-target admission and not a status-bounding dependency.
- **Y₀, g₀:** vacuous rescaling conventions — **dropped** from the
  admitted-input count (a convention is not an input, just as a name is not).
- **θ rigor check:** verified NOT derivable from the retained
  real/anti-Hermitian `D` structure —
  `strong_cp_rp_half_cannot_forbid_cp_odd_imaginary_no_go` (retained_no_go)
  explicitly shows the real/RP-half structure cannot forbid the CP-odd term, so
  θ=0 remains a genuine admission (shared with the SM).

Net stratified by character: **two dimensionless Tier-A admissions** —
AC_φλ (framework-specific physics) and θ (an SM-shared problem). Record/P1
scalar additivity is axiom content only in its narrow finite-readout form. The
scale-reference primitive is the single scale-setting every physical theory
takes, orthogonal to all of them, and cannot supply any dimensionless number.

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
   axioms and approved primitives (which chain-satisfy without bounding).
   Convention rows are not accepted premises, because the existing convention
   parent notes carry more than the vacuous normalization choice and must not
   be laundered as theorem inputs.
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
- Does **not** treat approved primitives as Tier-A admissions; primitives and
  axioms chain-satisfy without imposing `retained_bounded`.
- Does **not** promote `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` or any
  readout/log-det/modulus parent wholesale into the axiom-premise registry.
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
- `MINIMAL_AXIOMS_2026-06-04.md` (Lattice, Quantum, Record),
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` (older conditional P1 parent, not
  an axiom-premise node), `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  (AC_φλ parent),
  `HYPERCHARGE_IDENTIFICATION_NOTE.md` (Y₀), `G_BARE_RIGIDITY_THEOREM_NOTE.md`
  (g₀) — canonical parents / convention-reference rows for the listed items.
