# Agent fix list, 2026-10-17 reread

Wording, status labels, and citations only. Do not change algebra, runner mathematics, or ledger `effective_status`. Do not recreate a missing script to satisfy a stale path. Do not promote any row to `retained`, `retained_bounded`, or `retained_no_go`.

Checked against `origin/main` `fa841753c1` (2026-10-17). The cited files are byte-identical to `f389e89fe8`, where the line numbers were read. Re-read each cited line before editing. If the line has moved, follow the quote, not the number.

Live ledger at that tip: 5,722 shards, `effective_status` unaudited 5,346 and meta 376. Zero retained-grade rows. A header that says `proposed_retained`, `retained theorem content`, or `audited_conditional` is ahead of the shard.

## How to land a batch

- One batch per pull request. Branch from current `origin/main` in a worktree. Do not commit on the home checkout `~/Projects/Physics`. Do not push `main`.
- Batch A and Batch C both touch `docs/DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md`. Do that file once, in Batch A, and skip it in Batch C.
- Leave historic-intake wrappers alone. They are labeled as pinned originals.
- A banner printed after `assert` is still a dead `FAIL` channel. Replace it with a counter that can be nonzero. Do not delete the checks.

## Batch A — relic ratios

Put the 2026-09-30 corrigendum into the tables that still display the withdrawn numbers. Keep four symbols separate: `R_base = 31/9`, the entropy or Sommerfeld factor, the predicted relic ratio, and the observed ratio `0.1200/0.02237`.

- `docs/DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md`
  - Lines 126–134 still print the withdrawn pie chart: `eta` `6.38e-10` (+4.22%), `Omega_DM h^2` `0.1275` vs `0.1200` (+6.25%), `R = 5.48`.
  - Lines 160–163 still call `R = 5.48` a retained group-theory identity. `31/9 * 1.59 ≈ 5.48`. The `1.59` factor is the old half-argument Sommerfeld kernel. The corrigendum (lines 21–59) replaces it with `S = 2 π z / (1 - e^{-2 π z})`, `S_vis/S_dark = 2.314`, `R = 7.972`, and central `eta` `4.38e-10` (−28.4% from `6.12e-10`). `Omega_DM h^2 = 0.1275` is unchanged because it depends only on `alpha_X`.
  - Lines 18–19 still say the axiom is only `Cl(3)` on `Z^3`. Point at `docs/MINIMAL_AXIOMS_2026-06-29.md`.
  - Do not change the corrigendum’s statement of what still stands: `eta = C m_DM^2`, exact `R_base = 31/9`, and the open status of `m_DM = 16v`.
- `docs/COSMOLOGY_FROM_MASS_SPECTRUM_NOTE.md` lines 51–61 and 146–148. The header says “within 1%”. The table’s `R` error is about 2% (`5.48` vs `5.375`). The stated band `[4.8, 5.3]` does not contain `5.48`. Delete “within 1%” or replace it with the printed errors, and state a band that contains the printed `R`.
- `docs/OMEGA_LAMBDA_DERIVATION_NOTE.md` lines 15–29. Label `R = 5.38` and `Omega_b = 0.0492` as supplied comparison inputs.
- `docs/COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md` near line 296. Stop calling `5.3753` derived.
- `docs/COMPLETE_PREDICTION_CHAIN_2026_04_15.md` near line 650. `R = 5.48` is not derived from `eta`.
- `docs/DM_LIVE_CONSTANTS_CANONICAL_EDGE_CERTIFICATE_NOTE_2026-06-18.md` lines 57–67. Keep `5.4479` labeled observed.

## Batch B — gravity wording

The four axioms do not supply a metric degree of freedom. Conformal invariance of a supplied metric can stay. Delete “records derive the conformal class”, “from `{qubit, Z^3, Record}`”, and “forced by the axioms”.

- `docs/GRAVITY_CONFORMAL_SCALE_SPLIT_LENSING_RECORDS_DERIVED_SHAPIRO_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md` lines 13–16, 25–29, 40. Lines 64–66 already say the Einstein-equation content is named, not built. Lines 30–37 cite `retained_bounded` / `retained_no_go` parents; those grades are not live.
- `docs/GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md` lines 11–12. Keep the sign non-forcing result. Drop the conformal-class and Poisson derivations.
- `docs/UNIVERSAL_GR_CANONICAL_CHANNEL_SECTION_AND_EINSTEIN_SIGNS_NARROW_THEOREM_NOTE_2026-06-17.md` lines 67–72. Report the projector calculation on the stated operator.
- `docs/UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17.md`. The 2026-10-04 boundary (lines 20–29) withdraws “one residual wall” and “healthy graviton”. The title and body (lines 7–16, 112–118) still state them. Align the title and body to that boundary.
- `docs/GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION_REDUCES_TO_SHARED_ORIENTATION_DATUM_KCPT_CANNOT_SELECT_NARROW_THEOREM_NOTE_2026-06-18.md` lines 7–15 and 22–24. Do not collapse the open metric-DOF posit into an admitted datum.
- `docs/UNIVERSAL_GR_CANONICAL_PROJECTOR_CONNECTION_NOTE.md` lines 143–150. Call the completion a candidate. The same paragraph does not supply the connection.

Cross-check `docs/EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md` lines 10–12, which already says the class is not assembled.

## Batch C — stale one-axiom sentence

Replace “the single framework axiom `Cl(3)` on `Z^3`” with a pointer to `docs/MINIMAL_AXIOMS_2026-06-29.md`. Skip historic-intake files. Skip the freeze-out note if Batch A already edited it.

Top-level files:

- `docs/DM_NEUTRINO_TRANSPORT_CHAMBER_BLINDNESS_THEOREM_NOTE_2026-04-17.md:8`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_INFO_GEOMETRIC_SELECTION_OBSTRUCTION_NOTE_2026-04-17.md:8`
- `docs/PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17.md:21`
- `docs/PMNS_THETA23_UPPER_OCTANT_FULL_3SIGMA_RECTANGLE_NARROW_THEOREM_NOTE_2026-05-17.md:23`
- `docs/DM_NEUTRINO_VEVEN_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md:10`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_PARITY_COMPATIBLE_DIAGONAL_BASELINE_THEOREM_NOTE_2026-04-17.md:12`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_PERTURBATIVE_UNIQUENESS_THEOREM_NOTE_2026-04-17.md:23`
- `docs/PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md:10`
- `docs/DM_NEUTRINO_WEAK_TRIPLET_TRANSFER_CLASS_THEOREM_NOTE_2026-04-15.md:11`
- `docs/DM_NEUTRINO_CODD_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md:9`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_CUBIC_VARIATIONAL_OBSTRUCTION_NOTE_2026-04-17.md:8`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_CURVATURE_23_SYMMETRIC_BASELINE_BOUNDARY_THEOREM_NOTE_2026-04-17.md:12`
- `docs/DM_LEPTON_SYNTHESIS_NOTE_2026-04-19.md:16`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_SCALAR_BASELINE_ACTIVE_QUADRATIC_DIAGNOSTIC_NOTE_2026-04-17.md:9`
- `docs/CHARGED_LEPTON_UE_IDENTITY_VIA_Z3_TRICHOTOMY_NOTE_2026-04-17.md:8`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_PARITY_MIXING_SELECTION_OBSTRUCTION_NOTE_2026-04-17.md:8`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_PARITY_SPLIT_THEOREM_NOTE_2026-04-17.md:8`
- `docs/PMNS_FROM_DM_NEUTRINO_SOURCE_H_DIAGONALIZATION_CLOSURE_THEOREM_NOTE_2026-04-17.md:45`
- `docs/SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md:137`
- `docs/DM_FLAGSHIP_CLOSURE_REVIEW_NOTE_2026-04-17.md:21`
- `docs/CARRIER_ORBIT_INVARIANCE_NOTE_2026-05-03.md:32`
- `docs/HIGGS_Z3_CHARGE_PMNS_GAUGE_REDUNDANCY_THEOREM_NOTE_2026-04-17.md:9`
- `docs/PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md:21`
- `docs/DM_LEPTOGENESIS_EXACT_KERNEL_CLOSURE_NOTE_2026-04-15.md:9`
- `docs/PMNS_THETA23_UPPER_OCTANT_THRESHOLD_SURFACE_NARROW_THEOREM_NOTE_2026-05-17.md:20`
- `docs/CL3_SM_EMBEDDING_MASTER_NOTE.md:12`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_SCHUR_SCALAR_BASELINE_THEOREM_NOTE_2026-04-17.md:30`
- `docs/DM_NEUTRINO_SOURCE_AMPLITUDE_THEOREM_NOTE_2026-04-15.md:12`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_MICROSCOPIC_POLYNOMIAL_IMPOSSIBILITY_THEOREM_NOTE_2026-04-17.md:8`
- `docs/KOIDE_SELECTED_LINE_PROVENANCE_NOTE_2026-04-20.md:58`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_BIFUNDAMENTAL_INVARIANCE_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md:6`
- `docs/DM_NEUTRINO_OBSERVABLE_BANK_EXHAUSTION_THEOREM_NOTE_2026-04-17.md:9`
- `docs/DM_NEUTRINO_WEAK_EVEN_SWAP_REDUCTION_THEOREM_NOTE_2026-04-15.md:10`
- `docs/DM_NEUTRINO_SOURCE_SURFACE_QUARTIC_ISOTROPY_AND_U2_OBSTRUCTION_NOTE_2026-04-17.md:8`

## Batch D — red caches and the N5 list

Do not refresh a cache in order to hide a live failure.

- `logs/runner-cache/frontier_dm_leptogenesis_transport_status_terminal_synthesis.txt:57` prints `PASS=32 FAIL=12`. Cited by `docs/DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-05-10.md:24–25`. Read the 12 `FAIL` lines. Fix the checks or make the note report `FAIL>0`.
- `logs/runner-cache/p3_coupling_is_retention_eligible_composition_2026_06_06.txt:52` prints `PASS=35 FAIL=3`. Cited by `docs/P3_COUPLING_IS_RETENTION_ELIGIBLE_COMPOSITION_2026-06-06.md:11–13`.
- `logs/runner-cache/audit_unlock_keystone_map_2026_06_06.txt:53` prints `PASS=10 FAIL=2`. Audit tooling, not a physics theorem.
- Re-run the 28 rows plus 5 pilot skips in `docs/audit/N5_DRAIN_REPAIR_BACKLOG_2026-08-08.md` lines 44–94. Several runners are heavy. Refresh a cache only when the live `TOTAL` is `FAIL=0` because the checks passed.
- `scripts/tensor_helicity_review_certificates_2026_09_29.py:10` prints `TOTAL: PASS=2 FAIL=0` immediately after two imports. Print `PASS` from the imported checkers’ results.

## Batch E — dead `FAIL=0` banners

165 scripts print `TOTAL: PASS=<integer> FAIL=0` as a string. 164 have `assert` or `raise` earlier, so a failed check aborts instead of incrementing `FAIL`. Replace the literal with a counter. Start with runners paired to Batch A or B, plus `scripts/periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.py:156` (`PASS=3`).

## Batch F — CKM labels

Do not change the algebra. Do not average the Schur gap table with the atlas readout.

Surfaces that must stay named:

- Atlas-leading `|V_us|_0 = sqrt(alpha_s(v)/2) ≈ 0.22727`, conditional on supplied `alpha_s(v)`. `docs/CKM_ATLAS_AXIOM_CLOSURE_NOTE.md:264` and `docs/CKM_FIRST_ROW_MAGNITUDES_THEOREM_NOTE_2026-04-24.md:105`.
- `|V_us| = 0.2251` in `docs/THE_SMALL_MIXING_ANGLES_THETA_C_AND_THETA_13_ARE_C3_BREAKING_ORDER_PARAMETERS_UNIFICATION_NARROW_THEOREM_NOTE_2026-06-08.md:14`. This is not `sqrt(alpha_s(v)/2)`. Down-type `m_d/m_s = 0.05165` (`docs/DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md:170`) has square root in the `0.22727` class. `docs/CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md:102–103` already says `0.2251` is not a first-principles derivation. Delete `0.2251` from the “already reduced” sentence or mark it as an import.
- Schur gap table, already marked not load-bearing: `|V_us| = 0.328`, `|V_cb| = 0.015` and `0.041` on different rows, `|V_ub| = 0.023`, `J = 1.45e-4`, `delta = 29 deg`. `docs/CKM_SCHUR_COMPLEMENT_THEOREM.md:281–304` and `:369–383`. Keep that fence.
- `|V_ts|_0 = 0.0421736` versus exact-standard-matrix `|V_ts| = 0.0414407` inside `docs/CKM_THIRD_ROW_MAGNITUDES_THEOREM_NOTE_2026-04-24.md:96` and `:105`. Keep the subscript.
- Three Jarlskog prints: atlas `J = 3.331e-5` (`CKM_ATLAS_AXIOM_CLOSURE_NOTE.md:271`), CP-phase executable `J_0 = 3.4237e-5` (`docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md:218`), and `J_bar` with ratio `0.974174` (`docs/CKM_JARLSKOG_EXACT_NLO_CLOSED_FORM_THEOREM_NOTE_2026-04-25.md:36` and `:316`). Name which surface `3.331e-5` is.

Status headers versus unaudited shards. Replace `proposed_retained` and “retained theorem content” with “conditional, shard `effective_status: unaudited`”:

- `docs/CKM_FIRST_ROW_MAGNITUDES_THEOREM_NOTE_2026-04-24.md:5` and `:117`
- `docs/CKM_SECOND_ROW_MAGNITUDES_THEOREM_NOTE_2026-04-25.md:5` (`|V_cb| = 0.0421736` at `:93`)
- `docs/CKM_THIRD_ROW_MAGNITUDES_THEOREM_NOTE_2026-04-24.md:108`
- `docs/CKM_JARLSKOG_EXACT_NLO_CLOSED_FORM_THEOREM_NOTE_2026-04-25.md:27`
- `docs/CKM_NEUTRON_EDM_BOUND_NOTE.md:4`. Line 34 treats `J = 3.331e-5` as a promoted atlas input. Both shards are unaudited. Lines 43–45 already call the EDM scale an EFT bridge.
- `docs/CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md:5` and `:21`. Drop “single retained source” for `A^2 = 2/3`.
- `docs/CKM_MODULI_ONLY_UNITARITY_JARLSKOG_AREA_CERTIFICATE_THEOREM_NOTE_2026-04-26.md:7`
- Line-5 `proposed_retained` headers on `docs/CKM_THALES_PINNED_ALPHA_S_INDEPENDENT_RATIOS_THEOREM_NOTE_2026-04-25.md`, `docs/CKM_CP_PRODUCT_ALPHA_S_CROSS_SECTOR_EXTRACTION_THEOREM_NOTE_2026-04-25.md`, and `docs/CKM_MULTI_CHANNEL_ALPHA_S_EXTRACTION_CONSISTENCY_THEOREM_NOTE_2026-04-26.md`
- The same header on the other 2026-04-25/26 barred-triangle, Brocard, Bernoulli, Koide-bridge, `B_s`, and `epsilon_K` CKM notes. Their shards are unaudited.

`docs/CKM_FROM_MASS_HIERARCHY_NOTE.md:5` prints `Audit verdict: audited_conditional`. Shard `docs/audit/data/ledger/ck/ckm_from_mass_hierarchy_note.json` is unaudited. Replace the verdict string. Lines 155–168 are PDG comparators (`|V_us| = 0.2243`), not an axiom output.

`docs/QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md:178–179` labels `|V_us|_atlas = 0.227271` and `|V_cb|_atlas = 0.042174` DERIVED. Line 300 says the packet does not close the CKM gate. Change DERIVED to “atlas conditional readout”.

`docs/QUARK_PROJECTOR_PARAMETER_AUDIT_NOTE_2026-04-19.md:56–59` is the `0.22727` branch (`a_d = 1/sqrt(42)`). Add one sentence that this is a different conditional branch from the PDG `0.2243` line, and that neither is an axiom output.

Of 79 ledger shards whose ids contain `ckm`, `wolfenstein`, or `jarlskog`, 78 are `unaudited` and one work-history row is `meta`.

## Batch G — citation hygiene

- Point `docs/BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md:9` at `logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt`, or regenerate the dated cache `bertrand_stable_orbit_green_kernel_bridge_2026_05_29.txt`. The script exists. The dated cache does not.
- Point `docs/STAGGERED_FERMION_CARD_H2_POSITIVE_SOURCE_PHI_POSITIVITY_NARROW_THEOREM_NOTE_2026-05-17.md:224` at `logs/runner-cache/audit_companion_staggered_h2_positive_source_phi_positivity_narrow_exact_2026_05_17.txt`, which the same note already cites at line 11.
- Retarget or delete stale `scripts/*.py` citations. Do not recreate the script. Examples of names cited from top-level docs that are not under `scripts/`: `frontier_dm_chamber_signature_structure.py`, `frontier_koide_matrix_unit_source_law_cyclic_projection.py`, `frontier_signed_gravity_boundary_chi_candidate.py`, `signed_gravity_architecture_portability_sweep.py`, `lensing_phase_quarantine_audit.py`, `d3_bar_location_measurement_2026_07_10.py`. Many are historical probe names in prose.
- Paired `TOTAL` drift, both sides `FAIL=0`. After re-running the primary runner, set the note’s count to the cache’s count. Do not rewrite a mismatch that compares a note’s `TOTAL` to a different packet’s cache.

| Note PASS | Cache PASS | Cache |
|---:|---:|---|
| 55 | 57 | `admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.txt` |
| 6 | 4 | `frontier_cycle971_axiom_fidelity_reread_2026_08_09.txt` |
| 8 | 5 | `frontier_cycle984_born_compatibility_z3_adjacency_2026_08_11.txt` |
| 37 | 34 | `gauge_wilson_static_source_geodesic_2026_09_07.txt` |
| 42 | 32 | `gauge_wilson_static_source_sector_controls_2026_09_07.txt` |
| 7 | 11 | `frontier_epsstar_full_kernel_coefficient_2026_06_12.txt` |

## Batch H — PXP packaging only

`docs/PERIODIC_PXP_AND_STAGGERED_LINK_RING_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-10-07.md` and `scripts/periodic_pxp_and_staggered_link_ring_uniform_gap_2026_10_07.py`.

Do not change the inequality `gap > log(25/14)/4`. The shard is unaudited. The banner at runner line 156 is a literal `PASS=3`. Optional: record the even-L=6…16 gaps (about `0.984` down to a plateau near `0.968`) next to the bound `0.145`, so the bound is not read as the measured gap.

## Out of scope

Clifford multiplication tables that were opened match `e_i^2 = +1` and the Pauli product with `+i ε`. No table edit is queued. Do not treat scanner hits on the words “retained”, “finite additivity”, or an f-string `TOTAL` as defects. Those were negations and format strings.
