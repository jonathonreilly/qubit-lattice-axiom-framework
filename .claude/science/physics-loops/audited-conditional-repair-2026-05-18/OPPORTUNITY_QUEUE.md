# Opportunity Queue — audited_conditional repair 2026-05-18

Ranking from survey agent (2026-05-18). Tier A targets are
file-attachment / dependency-wiring repairs whose helper artifact
already exists on the current `origin/main`. Tier B targets are
one-step algebraic derivations from retained primitives.

## Tier A — file/dependency-attach repairs

| # | source_path | repair class | one-line action | indep |
|---|---|---|---|---|
| A1 | `mirror_2d_gravity_law_note` | runner_artifact_issue | wire `scripts/mirror_born_audit.py` + cache as direct retained dep of restricted packet | coupled-A2 |
| A2 | `mirror_2d_validation_note` | missing_dependency_edge | same authority as A1; one repair, two promotions | coupled-A1 |
| A3 | `adaptive_coevolving_geometry_no_go` | runner_artifact_issue | include `scripts/generative_causal_dag_interference.py` in restricted packet | independent |
| A4 | `alternative_coupled_field_probe_note` | runner_artifact_issue | include `scripts/minimal_source_driven_field_probe.py` helper source | independent |
| A5 | `wave_static_fixed_beam_boundary_sensitivity_note` | runner_artifact_issue | include `scripts/wave_retardation_continuum_limit.py` + H=0.5 cache | independent |
| A6 | `decoherence_action_independence_note` | missing_dependency_edge | include `scripts/valley_linear_same_harness_compare.py` so action defs auditable | independent |
| A7 | `wilson_two_body_open_note_2026-04-11` | runner_artifact_issue | include `scripts/frontier_wilson_two_body_laws.py` + cached stdout | independent |
| A8 | `kubo_continuum_limit_families_note` | runner_artifact_issue | include `scripts/kubo_continuum_limit.py` + transitive helpers | independent |
| A9 | `audit_dm_gv_runner_stale_path_cleanup_block_two_note_2026-05-01` | runner_artifact_issue | attach current source/patch diff for 8 named Block-Two runners | independent |
| A10 | `chiral_layer_oscillation_2026-04-09` | runner_artifact_issue | supply `scripts/frontier_chiral_3plus1d_converged.py` impl or inline walk | independent |
| A11 | `k_dependence_review_safe_note` | runner_artifact_issue | provide completed fixed-window log/stdout + runner source | independent |
| A12 | `higher_symmetry_joint_validation_note` | runner_artifact_issue | attach registered cache + runner source as primary | independent |
| A13 | `directional_b_density_stencil_note` | runner_artifact_issue | include transitive helper runner sources | independent |
| A14 | `pmns_graph_first_cycle_frame_support_note` | runner_artifact_issue | include transitive helpers for graph_first_*.py | independent |
| A15 | `dm_leptogenesis_pmns_relative_action_stationarity_theorem_note_2026-04-16` | runner_artifact_issue | include `scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py` | independent |
| A16 | `asymmetry_persistence_pilot_note` | runner_artifact_issue | include `scripts/gap_topological_asymmetry.py` + dense/layernorm certificates | independent |
| A17 | `work_history.atomic.hydrogen_helium_atomic_companion_note_2026-04-18` | missing_dependency_edge | provide preserved runner + stdout + one-hop lattice kinetic + Coulomb-kernel auths | independent |
| A18 | `dm_abcc_basin_finite_search_support_note_2026-04-30` | missing_dependency_edge | add archived wrapper + completed runner certificate as direct audit inputs | independent |
| A19 | `central_band_layernorm_note` | missing_dependency_edge | add retained modular gap=2 + layernorm source note or cached cert | independent |
| A20 | `central_band_dense_joint_note` | runner_artifact_issue | rerun/slice card with high-precision asserts; update N=40 collapse table | independent |

## Tier B — one-step algebraic bridges (if Tier A exhausts)

| # | source_path | repair class | one-line action |
|---|---|---|---|
| B1 | `rconn_derived_note` | missing_bridge_theorem | derive adjoint Fierz projection from retained Cl(3) primitives |
| B2 | `nn_lattice_rescaled_kernel_identification_note_2026-05-10` | missing_bridge_theorem | derive `m_eff_width = L/σ` Gaussian-Schrödinger rescaling identity |
| B3 | `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | missing_bridge_theorem | retained theorem fixing Frobenius normalization on isotype split |

## Tier C — defer (cascade-resolvable only)

`cross_sector_a_squared_koide_vcb_bridge_promoted_via_v8_theorem_note_2026-04-29`,
`g_bare_derivation_note`, `higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02`,
`three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02`,
`lhcm_matter_assignment_block_proof_walk_lattice_independence_bounded_note_2026-05-10`,
`wilson_test_mass_continuum_note_2026-04-11`, `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29`,
`g_bare_constraint_vs_convention_theorem_note_2026-05-03`.

## Tier D — skip this campaign

All `missing_bridge_theorem` rows requiring new physics
(irrep theory, action-form derivations, Yang-Mills, KMS, NSPT, etc.).
All `scope_too_broad` rows.

## Value-gate self-check (per workflow step 7)

V1 (what specific obstruction does each PR close?):
  Each Tier A repair closes the verdict_rationale text "imported source
  and registered cache not actually supplied in the restricted packet"
  (or equivalent missing-dep-edge phrasing) for its specific row.
V2 (new derivation content?):
  No new derivation — these are dependency-wiring + audit-packet
  closure repairs. Honest classification: these are not promotion
  campaigns. They settle each row at the verdict its underlying
  science already supports once the dependency graph is sound.
V3 (could audit lane already complete this?):
  Yes — that IS the audit lane's expected behavior on a refreshed
  packet. These PRs are the necessary input for that re-audit.
V4 (non-trivial marginal content?):
  Trivial per-PR (file linkage), but the campaign aggregate is
  not trivial: ~20 rows that have been stuck in audited_conditional.
V5 (one-step variant of landed cycle?):
  No — each row has a distinct upstream and distinct repair vector.

**Value-gate verdict:** PASS for the campaign. Each individual repair
is small but coherent. The campaign moves the audit ledger materially.
This is dependency-wiring work, not promotion work; the audit lane
re-audits each row after merge.
