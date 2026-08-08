# N5 Evidence-Drain Repair Backlog (2026-08-08)

**Type:** operational audit-lane report. This file carries no claim, sets no
status, and supplies no premise. It routes repair work discovered during the
2026-08-07/08 N5 execution-certificate drain (PRs #6027, #6029, #6030) into
the science-fix lane, with evidence pointers.

**Provenance.** The drain triaged all 448 rows blocked on
`forensic_n5_execution_certificate_incomplete` by executing every runner live
and diffing totals against its cache, then certified the 399 that ran clean.
The remainder — and the defects agents found while reading runners they were
certifying — are recorded here. Commit bodies on the drain branches carry the
per-item detail; this file is the index.

## A. Broken-live rows (28): runner fails on current main behind a fresh-reading cache

Every row below has a cache reading `fresh` (sha-keyed) whose recorded PASS/FAIL
totals the live runner no longer reproduces. Root causes cluster in two
upstream events: the probability-semantics repository repair (`fb5e056dd`),
which deleted literal strings that note/registry greps assert, and the
premise-epoch audit invalidation (`5e74dd6ed`), which reset ledger statuses
that runners assert. Each needs the narrowest honest source/runner repair via
the science-fix lane — not a cache refresh, which would replace passing
evidence with failing evidence.

| claim_id | class | live vs cached totals |
|---|---|---|
| `acphilambda_measure_binary_axiom_update_no_go_note_2026-07-04` | broken_live | live [128, 3] vs cached [131, 0] |
| `acphilambda_occupancy_formation_append_non_supply_no_go_note_2026-07-04` | broken_live | live [128, 2] vs cached [130, 0] |
| `acphilambda_r_eta_doublet_clock_rate_normalization_no_go_note_2026-07-04` | broken_live | live [137, 2] vs cached [139, 0] |
| `acphilambda_r_eta_record_formation_non_supply_no_go_note_2026-07-04` | broken_live | live [59, 1] vs cached [60, 0] |
| `continuum_equivariant_eta_standard_form_delta_firewall_bounded_note_2026-06-12` | broken_live | live [23, 1] vs cached [24, 0] |
| `dm_neutrino_source_surface_split2_edge_transport_lane_obstruction_candidate_note_2026-04-18` | broken_live | live [10, 6] vs cached [16, 0] |
| `dm_strong_cp_gamma_transfer_no_go_note_2026-04-15` | broken_live | live [10, 1] vs cached [11, 0] |
| `koide_a1_fractional_topology_no_go_synthesis_note_2026-04-24` | broken_live | live [4, 1] vs cached [5, 0] |
| `koide_q_reduced_carrier_physical_identification_obstruction_note_2026-06-12` | broken_live | live [12, 1] vs cached [13, 0] |
| `lattice_physical_matching_theorem_bounded_obstruction_note_2026-05-10_match` | broken_live | live [86, 2] vs cached [88, 0] |
| `quark_c3_a1_source_domain_bridge_no_go_note_2026-04-28` | broken_live | live [47, 3] vs cached [50, 0] |
| `quark_route2_e_center_single_box_limit_underdetermination_no_go_note_2026-06-21` | broken_live | live [43, 2] vs cached [45, 0] |
| `quark_route2_nonlinear_e_center_readout_primitive_boundary_note_2026-06-21` | broken_live | live [88, 2] vs cached [90, 0] |
| `quark_route2_normalized_quotient_selector_trichotomy_note_2026-06-21` | broken_live | live [32, 2] vs cached [34, 0] |
| `quark_route2_positive_diagonal_e_center_selector_no_go_note_2026-06-21` | broken_live | live [36, 1] vs cached [37, 0] |
| `quark_route2_qe_bulk_limit_consumer_boundary_note_2026-06-21` | broken_live | live [36, 1] vs cached [37, 0] |
| `quark_route2_rconn_signed_center_bridge_selector_firewall_note_2026-06-21` | broken_live | live [77, 1] vs cached [78, 0] |
| `quark_route2_record_raw_q_selector_gate_note_2026-06-21` | broken_live | live [26, 1] vs cached [27, 0] |
| `record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06` | broken_live | live [5, 1] vs cached [6, 0] |
| `ring_monodromy_does_not_force_car_note_2026-06-04` | broken_live | live [27, 2] vs cached [29, 0] |
| `theta_g1_defect_closure_current_surface_no_go_note_2026-07-04` | broken_live | live [185, 1] vs cached [186, 0] |
| `theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04` | broken_live | live [179, 1] vs cached [180, 0] |
| `theta_gauge_winding_axiom_update_no_go_note_2026-07-04` | broken_live | live [151, 6] vs cached [157, 0] |
| `universal_gr_picurv_route_exhaustion_no_go_note_2026-06-18` | broken_live | live [21, 1] vs cached [22, 0] |
| `yt_connected_source_selector_scalar_lift_no_go_note_2026-05-29` | broken_live | live [122, 1] vs cached [123, 0] |
| `yt_primitive_unit_source_action_physical_premise_no_go_note_2026-05-25` | broken_live | live [50, 1] vs cached [51, 0] |
| `yt_top_coefficient_full_court_press_note_2026-05-25` | broken_live | live [56, 3] vs cached [59, 0] |
| `yt_top_response_coefficient_underdetermination_no_go_note_2026-05-25` | broken_live | live [40, 3] vs cached [43, 0] |

Also in this class, found post-triage via helper-runner binding on PR #6029:

| claim_id | class | diagnosis |
|---|---|---|
| `dm_neutrino_source_surface_split2_edge_transport_lane_obstruction_candidate_note_2026-04-18` | broken_live | live 10/6 vs cached 16/0. Toolchain drift: helper optimizer `xatol=1e-10` feeds quantities pinned at 1e-12; different scipy/BLAS build moves the result. All four physical inequalities still hold; only reproduction pins fail. Fix options ranked in PR #6029 comments. |

And the three pilot-batch skips (PR #6027), same root causes as section A:

| claim_id | class | diagnosis |
|---|---|---|
| `theta_mass_determinant_axiom_update_no_go_note_2026-07-04` | broken_live | live 109/8 vs cached 117/0; theta parent ledger row reset to unaudited by epoch invalidation + wording drift |
| `acphilambda_defect_identity_unit_rescale_obstruction_2026-07-01` | broken_live | live 117/2 vs cached 119/0; probability-semantics commit deleted a grepped literal |
| `acphilambda_r_eta_occurrence_axiom_hygiene_no_go_note_2026-07-04` | broken_live | live 136/4 vs cached 140/0; four grepped phrases deleted by the same commit |

## B. Crashes and timeouts (18)

Crashes need a reproducer-first tooling/runner repair; timeouts need a re-run
with the runner's own `AUDIT_TIMEOUT_SEC` budget (the triage used a flat 150 s)
before any deeper diagnosis — a slow runner is not a broken runner.

| claim_id | class | detail |
|---|---|---|
| `gauge_scalar_temporal_observable_bridge_no_go_theorem_note_2026-05-03` | crash | dent          negative proposal, not positive bridge promotion or audit verdict  =========================================================== |
| `koide_q_delta_readout_retention_split_no_go_note_2026-04-24` | crash | udit has FAILs. KOIDE_Q_DELTA_READOUT_RETENTION_SPLIT_NO_GO=FALSE Q_DELTA_READOUT_RETENTION_SPLIT_CLOSES_Q=FALSE Q_DELTA_READOUT_RETENTION_S |
| `physical_lattice_necessity_note` | crash | ending sibling notes     HILBERT-SEMANTICS commentary: narrowed-out / pending sibling notes     PACKAGE-DIAGNOSTIC commentary: narrowed-out  |
| `action_power_3d_operator_cauchy_note_2026-05-10` | timeout | >150s |
| `adaptive_coevolving_geometry_no_go` | timeout | >150s |
| `bae_max_entropy_retained_bounded_obstruction_note_2026-05-10_baemaxent` | timeout | >150s |
| `born_scattering_comparison_note` | timeout | >150s |
| `g_bare_dynamical_fixation_obstruction_note_2026-04-18` | timeout | >150s |
| `gate_b_poisson_self_gravity_note` | timeout | >150s |
| `microcausality_exact_h_expansion_route_quantified_obstruction_note_2026-06-09` | timeout | >150s |
| `p_flux_finite_species_density_from_determinant_matsubara_surface_narrow_no_go_note_2026-06-10` | timeout | >150s |
| `p_flux_point_zero_set_from_retained_rows_narrow_no_go_note_2026-06-10` | timeout | >150s |
| `persistent_object_adaptive_readout_v2_note` | timeout | >150s |
| `poisson_self_gravity_mechanism_note` | timeout | >150s |
| `quantum_horizon_note` | timeout | >150s |
| `quark_route2_qe_box_path_interpolation_family_no_go_note_2026-06-21` | timeout | >150s |
| `quark_up_amplitude_native_affine_no_go_note_2026-04-19` | timeout | >150s |
| `theta_phase_insertion_triality_flip_table_single_link_nogo_chain_reader_bounded_theorem_note_2026-07-02` | timeout | >150s |

## C. Defects found while certifying (recorded in drain-branch commit bodies, unrepaired)

Certifying agents read each note and runner in full and recorded what they
found without repairing anything. The highest-severity classes, with exemplar
rows (the drain-branch commit body on each named claim carries the exact
locations):

**C1. Claimed computations that do not exist.** A runner prints "We numerically
simulate the holonomy" while `holonomy = 2.0/9.0` is a literal assignment and
no lattice is allocated (`koide_a1_o13_cheeger_simons_rz_no_go_note_2026-04-24`,
30 of 44 checks hardcoded True). A "lattice Laplacian" is `np.eye`, so the
barrier commutator vanishes identically
(`koide_a1_probe_gravity_phase_bounded_obstruction_note_2026-05-08_probe3`).
A docstring promises a numpy cross-check that never runs
(`strong_cp_rp_half_cannot_forbid...2026-05-16`); another claims numpy that is
never imported (`yt_p1_shared_fierz_no_go_sub_theorem_note_2026-04-17`).

**C2. Self-comparisons and tautologies at load-bearing checks.** A
zero-argument function called twice and compared to itself as the headline
"species independence" check (`yt_class_5_non_ql_yukawa_vertex_note_2026-04-18`
and the class-4 sibling). `pi_A == pi_A`
(`staggered_dirac_substep4_labeling...2026-05-17`). Determinant-blindness legs
comparing a value with itself
(`neutrino_majorana_pfaffian_axiom_boundary_note`). A loop discarding its
variable so three "distinct" calls are identical
(`neutrino_majorana_observable_principle_obstruction_note`). Dead conjunct
`(1.0 >= 0)` (`route2_readout_record_positivity...2026-06-08`). A chained
`!=` that never compares first against third
(`quark_route2_channel_determinant_quotient_gate_note_2026-06-21`).

**C3. Note-versus-runner mismatches.** A note quotes closed form `2*sqrt(3)*sqrt(2)`
where the runner prints `3*sqrt(2)` (`closure_t2_df_physical_consequences_note_2026-05-10_t2df`).
A note cites runner task "T8" that the runner does not define
(`dm_dple_abcc_no_go_note_2026-04-19`). A note's advertised output line is
emitted under a different prefix (`quark_route2_magnitude_source_e_center_shear_no_go_note_2026-06-21`).
A note describes kernel sizes n=1,3,5 where the runner builds 2,3,5
(`neutrino_majorana_lower_level_pairing_nogo_note` — which also pins a runner
sha256 in prose at lines 6/128, now stale against the certificate edit and
needing an owner refresh). A stanza header states ~0.97 where the runner
prints 0.949990 (`cl3_t1` corrections family). A hopping matrix cancels to
zero at L=2 so only the mass term is tested
(`neutrino_majorana_native_gaussian_no_go_note`).

**C4. Vacuous or unreachable check structure.** Hardcoded expected-value
tables restated as checks; `math.isfinite` on an epsilon-regulated quantity
that cannot fail; an `assert` inside the check helper making its FAIL column
unreachable; large documentary-check fractions (up to 33 of 49) counted in
scorecards. Exemplars named in the slice-16, noscorecard-a and noscorecard-b
commit bodies.

## D. Cache-integrity mechanisms (tooling design, flagged in PR #6026)

Two distinct ways a cache reads `fresh` while its stdout no longer reproduces:

1. `declared_input_paths` does not cover doc/registry files that runners grep,
   so content drift there never invalidates the cache (mechanism behind most
   of section A).
2. Freshness is keyed on runner sha256, not re-execution, so toolchain drift
   (scipy/BLAS moving an optimizer inside its own tolerance) is invisible
   (mechanism behind the split2 row).

A runner-cache design change is needed; neither mechanism is repairable
row-by-row.

## Routing

Sections A and B are science-fix lane work
(`scripts/science_fix_loop.py`; see the backlog surface
`docs/audit/data/science_fix_backlog.json`). Section C items are per-row
repair candidates of mixed severity — C1 and C2 first, since those notes'
negative claims currently rest on checks that do not test what their labels
say. Section D is a tooling change with its own review.

Nothing here is a verdict, a status, or a premise. The independent audit lane
re-decides every row.
