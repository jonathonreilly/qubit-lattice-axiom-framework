# N5 Evidence-Drain Repair Backlog (2026-08-08)

**Scope:** operational audit-lane routing metadata only. This file carries no
claim, sets no status, supplies no premise, and has no audit authority. It
routes repair work discovered during the 2026-08-07/08 N5
execution-certificate drain (PRs #6027, #6029, and #6030) into the science-fix
lane, with evidence pointers. The `docs/audit/` path is outside the
science-note discovery surface used to build the citation graph.

**Provenance.** The drain started from 448 unique queue rows blocked on
`forensic_n5_execution_certificate_incomplete`. Final branch artifacts and
their generated queue snapshots reconcile as follows:

| branch | final reviewed head | new distinct primary pairs in the union | new original rows cleared in the union |
|---|---|---:|---:|
| PR #6027 | `645b9947af6ca6d18c522be69c9ad886a3615ea2` | 7 | 7 |
| PR #6029 | `4007c5d9a0590d08212641ecd99659e1bc3e5e85` | 178 | 180 |
| PR #6030 | `e086504bc9247752f27bd7fc8f4a7260ff2126b3` | 210 | 210 |
| **disjoint drain union** | — | **395** | **397** |

The table reports incremental union contributions, not raw cumulative queue
snapshot deltas: the PR #6029 snapshot also contains the 7 PR #6027
clearances, and the final PR #6030 inventory contains 2 pairs already present
in PR #6029. One new PR #6029 primary pair serves three original Wave-A queue
rows, accounting for 180 new cleared rows from 178 new pairs. The PR #6030
cross-branch duplicates make that branch inventory 212 runners without
changing its 210-pair contribution to the distinct union. Therefore 51 of
the original 448 rows remain:
28 fresh-cache/live mismatches, 3 nonzero runner exits, 15 flat-budget
timeouts, and 5 final pilot skips. Commit bodies and review findings on the
drain branches carry the per-item evidence; this file is the routing index.

## Fresh-cache/live mismatch rows (28)

Every row below has a cache reading `fresh` (sha-keyed) whose recorded PASS/FAIL
totals the live runner no longer reproduces. Most root causes cluster in two
upstream events: the probability-semantics repository repair (`fb5e056dd`),
which deleted literal strings that note/registry greps assert, and the
premise-epoch audit invalidation (`5e74dd6ed`), which reset ledger statuses
that runners assert. Each needs the narrowest honest source/runner repair via
the science-fix lane — not a cache refresh, which would replace passing
evidence with failing evidence.

| claim_id | observed live and cached totals |
|---|---|
| `acphilambda_measure_binary_axiom_update_no_go_note_2026-07-04` | live [128, 3] vs cached [131, 0] |
| `acphilambda_occupancy_formation_append_non_supply_no_go_note_2026-07-04` | live [128, 2] vs cached [130, 0] |
| `acphilambda_r_eta_doublet_clock_rate_normalization_no_go_note_2026-07-04` | live [137, 2] vs cached [139, 0] |
| `acphilambda_r_eta_record_formation_non_supply_no_go_note_2026-07-04` | live [59, 1] vs cached [60, 0] |
| `continuum_equivariant_eta_standard_form_delta_firewall_bounded_note_2026-06-12` | live [23, 1] vs cached [24, 0] |
| `dm_neutrino_source_surface_split2_edge_transport_lane_obstruction_candidate_note_2026-04-18` | macOS/Accelerate live [12, 4] and Linux/OpenBLAS live [10, 6] vs cached [16, 0] |
| `dm_strong_cp_gamma_transfer_no_go_note_2026-04-15` | live [10, 1] vs cached [11, 0] |
| `koide_a1_fractional_topology_no_go_synthesis_note_2026-04-24` | live [4, 1] vs cached [5, 0] |
| `koide_q_reduced_carrier_physical_identification_obstruction_note_2026-06-12` | live [12, 1] vs cached [13, 0] |
| `lattice_physical_matching_theorem_bounded_obstruction_note_2026-05-10_match` | live [86, 2] vs cached [88, 0] |
| `quark_c3_a1_source_domain_bridge_no_go_note_2026-04-28` | live [47, 3] vs cached [50, 0] |
| `quark_route2_e_center_single_box_limit_underdetermination_no_go_note_2026-06-21` | live [43, 2] vs cached [45, 0] |
| `quark_route2_nonlinear_e_center_readout_primitive_boundary_note_2026-06-21` | live [88, 2] vs cached [90, 0] |
| `quark_route2_normalized_quotient_selector_trichotomy_note_2026-06-21` | live [32, 2] vs cached [34, 0] |
| `quark_route2_positive_diagonal_e_center_selector_no_go_note_2026-06-21` | live [36, 1] vs cached [37, 0] |
| `quark_route2_qe_bulk_limit_consumer_boundary_note_2026-06-21` | live [36, 1] vs cached [37, 0] |
| `quark_route2_rconn_signed_center_bridge_selector_firewall_note_2026-06-21` | live [77, 1] vs cached [78, 0] |
| `quark_route2_record_raw_q_selector_gate_note_2026-06-21` | live [26, 1] vs cached [27, 0] |
| `record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06` | live [5, 1] vs cached [6, 0] |
| `ring_monodromy_does_not_force_car_note_2026-06-04` | live [27, 2] vs cached [29, 0] |
| `theta_g1_defect_closure_current_surface_no_go_note_2026-07-04` | live [185, 1] vs cached [186, 0] |
| `theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04` | live [179, 1] vs cached [180, 0] |
| `theta_gauge_winding_axiom_update_no_go_note_2026-07-04` | live [151, 6] vs cached [157, 0] |
| `universal_gr_picurv_route_exhaustion_no_go_note_2026-06-18` | live [21, 1] vs cached [22, 0] |
| `yt_connected_source_selector_scalar_lift_no_go_note_2026-05-29` | live [122, 1] vs cached [123, 0] |
| `yt_primitive_unit_source_action_physical_premise_no_go_note_2026-05-25` | live [50, 1] vs cached [51, 0] |
| `yt_top_coefficient_full_court_press_note_2026-05-25` | live [56, 3] vs cached [59, 0] |
| `yt_top_response_coefficient_underdetermination_no_go_note_2026-05-25` | live [40, 3] vs cached [43, 0] |

The split2 row is counted once in the 28. Its helper optimizer uses
`xatol=1e-10` while downstream reproduction checks are pinned at `1e-12`.
All four physical inequalities remain green in both reviewed environments;
only the reproduction pins move. The repair must align optimizer tolerance
and asserted precision, then establish the intended environment envelope
before refreshing the cache.

## Final pilot skips (5)

PR #6027 retained 7 of its 12 proposed pairs and restored these 5 pairs to
the merge base. The final two were removed during review rather than accepted
as print-only evidence changes.

| claim_id | observed defect and required repair |
|---|---|
| `theta_mass_determinant_axiom_update_no_go_note_2026-07-04` | live 109/8 vs cached 117/0; parent ledger row reset by epoch invalidation plus wording drift. Repair the narrow source/runner assertions before recaching. |
| `acphilambda_defect_identity_unit_rescale_obstruction_2026-07-01` | live 117/2 vs cached 119/0; the probability-semantics repair deleted a grepped literal. Bind the check to the intended semantic surface rather than old wording. |
| `acphilambda_r_eta_occurrence_axiom_hygiene_no_go_note_2026-07-04` | live 136/4 vs cached 140/0; four grepped phrases were deleted by the same repair. Replace wording-dependent checks with semantic predicates before recaching. |
| `koide_bae_probe_cl3_bivector_bounded_obstruction_note_2026-05-17_probecl3bivector` | review found `E_perp = 6|b|^2`, so two-dimensional Lebesgue log-volume gives `2 log|b| = log E_perp + const` (the F1 coefficient), not `2 log E_perp` (the F3 coefficient); the runner's decisive “F3 naturally” predicate is literal `True`. Correct or demote the measure inference, bind the corrected statement to a real predicate, regenerate an authentic cache, and only then add the certificate. |
| `dm_wilson_direct_descendant_canonical_fiber_schur_entropy_candidate_no_go_note_2026-04-19` | refreshed and fresh-live outputs changed complete optimizer witness vectors, packs, spectra, entropy values, and root while 12 qualitative predicates stayed green; the optimizer path is not bound to a deterministic witness contract. Choose and document a deterministic seed or remove stochastic witness dependence, verify stable margins, and regenerate an authentic cache before certification. |

## Nonzero exits and timeouts (18)

The flat triage labeled any nonzero exit a crash. Reproduction at the frozen
PR #6031 head shows that all three runners complete normally and exit 1
because their own checks report FAILs; none raises a Python exception. They
need source/runner repair, not crash debugging:

| claim_id | reproduced result |
|---|---|
| `gauge_scalar_temporal_observable_bridge_no_go_theorem_note_2026-05-03` | theorem pass 8, support pass 2, fail 3: claim-type declaration, forbidden-import firewall wording, and audit-consequence wording |
| `koide_q_delta_readout_retention_split_no_go_note_2026-04-24` | 9/10; the retained-note support check for local scalar source-response readout fails |
| `physical_lattice_necessity_note` | theorem/compute pass 9, support 19, commentary-neutral 16, fail 1; the fixed-gauge-surface `beta=6` source check fails |

The 15 timeouts need a re-run with each runner's own `AUDIT_TIMEOUT_SEC`
budget (the triage used a flat 150 seconds) before deeper diagnosis. A slow
runner is not thereby a broken runner.

| claim_id | flat-triage observation |
|---|---|
| `action_power_3d_operator_cauchy_note_2026-05-10` | exceeded 150 seconds |
| `adaptive_coevolving_geometry_no_go` | exceeded 150 seconds |
| `bae_max_entropy_retained_bounded_obstruction_note_2026-05-10_baemaxent` | exceeded 150 seconds |
| `born_scattering_comparison_note` | exceeded 150 seconds |
| `g_bare_dynamical_fixation_obstruction_note_2026-04-18` | exceeded 150 seconds |
| `gate_b_poisson_self_gravity_note` | exceeded 150 seconds |
| `microcausality_exact_h_expansion_route_quantified_obstruction_note_2026-06-09` | exceeded 150 seconds |
| `p_flux_finite_species_density_from_determinant_matsubara_surface_narrow_no_go_note_2026-06-10` | exceeded 150 seconds |
| `p_flux_point_zero_set_from_retained_rows_narrow_no_go_note_2026-06-10` | exceeded 150 seconds |
| `persistent_object_adaptive_readout_v2_note` | exceeded 150 seconds |
| `poisson_self_gravity_mechanism_note` | exceeded 150 seconds |
| `quantum_horizon_note` | exceeded 150 seconds |
| `quark_route2_qe_box_path_interpolation_family_no_go_note_2026-06-21` | exceeded 150 seconds |
| `quark_up_amplitude_native_affine_no_go_note_2026-04-19` | exceeded 150 seconds |
| `theta_phase_insertion_triality_flip_table_single_link_nogo_chain_reader_bounded_theorem_note_2026-07-02` | exceeded 150 seconds |

## Additional review observations routed for repair

Certifying agents read each note and runner in full and recorded what they
found without repairing anything. These are repair-routing observations, not
scientific verdicts accepted by this file. The drain-branch commit body on
each named row carries the exact locations.

**Priority: advertised computations that do not execute.** A runner prints "We numerically
simulate the holonomy" while `holonomy = 2.0/9.0` is a literal assignment and
no lattice is allocated (`koide_a1_o13_cheeger_simons_rz_no_go_note_2026-04-24`,
30 of 44 checks hardcoded True). A "lattice Laplacian" is `np.eye`, so the
barrier commutator vanishes identically
(`koide_a1_probe_gravity_phase_bounded_obstruction_note_2026-05-08_probe3`).
A docstring promises a numpy cross-check that never runs
(`strong_cp_rp_half_cannot_forbid...2026-05-16`); another claims numpy that is
never imported (`yt_p1_shared_fierz_no_go_sub_theorem_note_2026-04-17`).

**Priority: self-comparisons and tautological predicates.** A
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

**Other note-versus-runner mismatches.** A note quotes closed form `2*sqrt(3)*sqrt(2)`
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

**Other vacuous or unreachable check structure.** Hardcoded expected-value
tables restated as checks; `math.isfinite` on an epsilon-regulated quantity
that cannot fail; an `assert` inside the check helper making its FAIL column
unreachable; large documentary-check fractions (up to 33 of 49) counted in
scorecards. Exemplars named in the slice-16, noscorecard-a and noscorecard-b
commit bodies.

## Cache-integrity mechanisms flagged for tooling repair

Two distinct ways a cache reads `fresh` while its stdout no longer reproduces:

1. `declared_input_paths` does not cover doc/registry files that runners grep,
   so content drift there never invalidates the cache (mechanism behind most
   fresh-cache/live mismatches).
2. Freshness is keyed on runner sha256, not re-execution, so toolchain drift
   (scipy/BLAS moving an optimizer inside its own tolerance) is invisible
   (mechanism behind the split2 row).

A runner-cache design change is needed; neither mechanism is repairable
row-by-row.

## Routing

The 51 unresolved rows are science-fix lane work
(`scripts/science_fix_loop.py`; see the backlog surface
`docs/audit/data/science_fix_backlog.json`). The additional observations are
per-row repair candidates of mixed severity; start with advertised-but-absent
computations and tautological predicates because the check labels overstate
what those runners execute. The two cache-integrity mechanisms need a
separate tooling change and review.

Nothing here is a verdict, status, premise, ledger row, import, or retained
claim. Independent audit re-decides every repaired row from its primary
evidence.
