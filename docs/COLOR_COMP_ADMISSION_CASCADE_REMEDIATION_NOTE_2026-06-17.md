# Color `COMP` Admission — Audit Cascade Remediation (TARGETING / HANDOFF)

**Date:** 2026-06-17
**Type:** meta / audit-targeting handoff
**Status:** **PROPOSAL / audit-lane targeting metadata.** This note does **not**
edit `docs/audit/data/audit_ledger.json` or any `effective_status`, and sets no
audit status. It specifies the expected cascade for the audit lane to apply.

## HARD DEPENDENCY — must not be applied before the COMP admission lands

> This remediation is **gated on the `COMP` Tier-A admission proposal**
> (`docs/COLOR_COMPOSITION_CARRIER_TIER_A_ADMISSION_PROPOSAL_NOTE_2026-06-17.md`,
> PR that registers `color_composition_carrier_admission` in
> `docs/audit/data/tier_a_admissions.json`). **Do not apply any of the cascade
> below until `COMP` is owner-approved and registered.** If `COMP` is rejected,
> this note is moot. The two PRs are stacked: the COMP-registration PR must land
> first.

## Why this is a handoff, not a ledger edit

`effective_status` is owned by the audit lane and is **auto-computed**: once
`COMP` is a registered Tier-A admission and a color-consequence row's `deps`
include it, `compute_effective_status` cascades that row to `retained_bounded`
on its own. This note therefore (a) names the rows that should chain to `COMP`,
(b) states the expected resolution, and (c) flags the rows that need audit-lane
judgment — as **targeting metadata** for the lane to apply. The session does not
edit the ledger, wire `deps`, or set status.

## Cascade rule

`COMP` registered  →  chain-satisfying premise at the bounded tier  →  a clean
row whose `deps` include `color_composition_carrier_admission` resolves to
**`retained_bounded`** (terminal, retained-grade) instead of `unaudited`-blocked
or `audited_conditional` pending the physical-color bridge.

## Group A — resolve to `retained_bounded` (wire `deps` → `COMP`)

Physical-color *consequences* currently non-terminal whose only missing premise
is the physical-color carrier that `COMP` supplies. Expected: `→ retained_bounded`.

| row | current | expected |
|---|---|---|
| `cl3_quark_antiquark_color_singlet_theorem_note_2026-05-02` | `audited_conditional` (rationale: *"authority explicitly defers the bridge to physical SM color/quark carrier"*) | `retained_bounded` |
| `cl3_baryon_qqq_color_singlet_theorem_note_2026-05-02` | `unaudited` | `retained_bounded` |
| `color_depolarization_adm2_gating_admissions_collapse_to_two_...` | `unaudited` | `retained_bounded` |
| `color_depolarization_single_frame_dephasing_insufficiency_...` | `unaudited` | `retained_bounded` |
| `color_neutrality_entanglement_depolarization_is_global_invariant...` | `unaudited` | `retained_bounded` |
| `color_link_index_routing_via_cross_site_matter_bilinear_unitariz...` | `unaudited` | `retained_bounded` |
| `color_su3_symmetric_base_bridge_from_record_invariance_bounded_...` | `unaudited` | `retained_bounded` |

The bulk `unaudited` color-consequence rows not listed individually follow the
same rule once the audit lane processes them: given-color consequence + `COMP`
dep → `retained_bounded`. This note supplies the criterion; the lane applies it.

## Group B — NO status change (re-point provenance to `COMP` only if desired)

- **Pure SU(3) group-theory algebra — stays `retained` / `retained_bounded`,**
  independent of `COMP` (true given the group, not given physical color):
  `su3_wigner_intertwiner_block1/block2/block3/block4_block5`,
  `su3_casimir_fundamental_*`, `su3_adjoint_casimir_*`,
  `su3_character_diagonal_convolution_equivalence_*`,
  `gauge_wilson_su3_all_weight_positive_coefficient_*`,
  `unit_singlet_overlap_*`, `su3_wigner_l3_*`.
- **Already `retained_bounded` color consequences — status unchanged;** `COMP`
  only makes their bound canonical (optionally re-point dep to `COMP`):
  `matter_color_depolarization_necessary_for_gauge_link_ad_invariance_*`,
  `one_generation_anomaly_singlet_completion_*`,
  `rconn_vertex_color_singlet_projection_*`.
- **`retained_no_go` — unchanged:** `g2_bridge_c3_current_cannot_beat_gap_a_*`
  and the `beta6_plaquette_*` no-gos.

## Group C — audit-lane judgment required (`COMP` does NOT auto-resolve)

- `su3_dabc_symmetric_theorem_note_2026-05-02` — `audited_conditional` on the
  **Gell-Mann basis** (a retained-bounded algebra input), **not** on physical
  color; `COMP` does not discharge it.
- `cl3_su3_symmetric_base_commutant_gell_mann_embedding_*` — **`audited_failed`**
  (the *spatial*-base route). `COMP` does **not** rescue it; it is a different,
  failed route. Leave failed or re-examine separately; do not chain to `COMP`.
- `z3_character_isomorphism_color_generation_open_gate_*` and
  `color_generation_independent_z3_structures_2026-06-05` — the color-vs-
  generation `Z3` question. Separate from `COMP`. (NB: the "regular-vs-center
  character" argument distinguishing the cube body-diagonal triangle from color
  is only inequivalent to the color *center*; color's Weyl `Z3` shares the same
  `(3,0,0)` regular character — the robust discriminator is spatial/external vs
  internal, not the character. Audit lane should not rely on the character
  argument alone.)
- `plaquette_beta6_perturbative_derivation_bounded_obstruction_*`,
  `su3_beta6_gap_bulk_criticality_reduction_*` — conditional on a
  criticality/admitted-packet premise **in addition to** the gauge group;
  `COMP` discharges only the gauge-group part.

## Exclusions (matched by keyword but NOT color)

Rows containing "singlet" in a **flavor/taste** sense are not color consequences
and must not be chained to `COMP`: `koide_c3_*_singlet_*`,
`dm_neutrino_*_singlet_*`, `higgs_taste_singlet_*`,
`lepton_block_scalar_singlet_*`, `neutrino_majorana_adjacent_singlet_*`,
`fierz_singlet_channel_selector_*`.

## Net effect (for the audit)

Closes the physical-color hole: the deferred-bridge conditionals and the
given-color `unaudited` consequences become terminal `retained_bounded`
(advancing terminal coverage), with **no demotion** of the SU(3) algebra and
**no promotion** to unbounded/derived. Cost: `genuine_admitted_input_count`
2 → 3 (carried by the `COMP` PR, not this one). This note is the targeting
spec; the audit lane applies the cascade via `compute_effective_status`.
