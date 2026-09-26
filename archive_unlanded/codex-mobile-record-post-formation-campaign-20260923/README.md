# Unpublished mobile-record campaign science, 2026-09-20 to 2026-09-24

This directory preserves the files of the local Codex branch `codex/mobile-record-post-formation-campaign-20260923` (head `eb34060bef`) that are not on origin in any form: not on `main`, not on `ai/probes` and not on any `codex/*` PR branch, compared by file content. It follows the `archive_unlanded/<branch>/<original path>` convention, so every file sits at its original path under `.claude/science/mobile-record-formation-20260920/`.

The owner's rule is that all interesting science is preserved on the remote in a PR for review and classification. Nothing here carries review, audit or retained status. The models, rates, instruments and preparations in these notes are supplied, not derived from the axioms. The numerical results are finite diagnostics.

## Why an archive rather than the branch

The branch was Codex's private raw record of four twelve-hour campaigns, and Codex never pushed it. Two things made it unpublishable as it stands:

- its history contains copies of third-party papers;
- it carries about 670 MB of raw simulation arrays.

The campaigns published their milestones as the curated PRs listed below. This archive is cut fresh from `main` and holds the rest.

## Selection

- **Preserved here:** 4,089 files (39.8 MB). They are notes and derivations, independent-check specifications and reports, Python and C++ sources, results and per-history statistics, receipts, logs and figures.
- **Already on origin, not duplicated:** 3,283 files.
- **Excluded:** 405 files (743.4 MB). They remain in the local branch and are listed with their git blob ids in `PRESERVATION_MANIFEST.json`:
  - raw array/state data: 375 files, 691.9 MB
  - large per-run JSON output (aggregate kept): 11 files, 6.5 MB
  - large raw csv output: 5 files, 37.2 MB
  - compiled binary: 4 files, 0.3 MB
  - copy of a third-party paper: 4 files, 1.0 MB
  - copy of agent planning instructions: 3 files, 0.0 MB
  - large raw JSON (per-run data or hash inventory): 2 files, 4.7 MB
  - large raw log output: 1 files, 1.7 MB

The per-run arrays can be regenerated from the seeds, protocols and sources preserved here.

Two of the campaign-2 computations also have a curated copy on `ai/probes`, together with backlog units for independent replay:
- the geometric fixed-rate formation follow-up;
- the dimer-routed colour-wave screen, with its N = 256 follow-up.

That copy is in `probes/work/worktree-sweep-20260926/codex-sync-2026-09-21-second/`, and the backlog units are `C:recovered-*`.

## Notes by campaign

Each table lists the top-level notes of that campaign's folder that were never published. Titles and status lines are quoted from the notes as written. Several notes later received a separate independent packet, listed under each table. A quoted "independent check pending" can therefore be out of date. Plans, protocols, checkpoints and receipts are preserved but not listed.

### Campaign 1 (2026-09-20/21), `campaign12h/`

Published milestones: #8545, #8551, #8552, #8557, #8560, #8561, #8565, #8566, #8567, #8569 (open).

| Note | Title | Status as written |
|---|---|---|
| `ACOUSTIC_PRESSURE_DESIGN_AND_SELECTION.md` | Pressure-law freedom in immutable product-preserving exchanges |  |
| `ADMISSIBILITY_FORMATION_EULER_DERIVATION.md` | Neighbor-dependent formation on the immutable-wave Euler scale |  |
| `AXIS_BALANCED_COMPLETED_SCREEN_REPORT.md` | Completed axis-balanced wave screen |  |
| `AXIS_BALANCED_CONTEXT_EXCHANGE_DERIVATION.md` | Immutable context exchange with an acoustic sector at every interior density |  |
| `AXIS_BALANCED_NONLINEAR_SCOPE.md` | Nonlinear closure and the remaining cubic anisotropy |  |
| `CAMPAIGN_OUTCOME.md` | Twelve-hour campaign: mobile records, renewed formation and the TOE | completed. |
| `CENTERED_GAUSS_STAGGERED_SECTORS_AND_ADJOINT_ESCAPE.md` | Centered Gauss constraints, staggered sectors and an adjoint escape |  |
| `CONTEXT_EXCHANGE_ACOUSTIC_DERIVATION.md` | A context-dependent immutable exchange with an isotropic acoustic current sector |  |
| `CONTEXT_EXCHANGE_EULER_DERIVATION.md` | From the context-exchange generator to a smooth Euler profile |  |
| `CONTEXT_EXCHANGE_FLUCTUATION_DERIVATION.md` | A stationary Euler-scale wave limit for immutable context exchanges |  |
| `EMPTY_START_DERIVATION.md` | Primary working derivation: empty-start correlations and delayed motion response |  |
| `FINITE_PERTURBATION_INFLUENCE_DERIVATION.md` | Does relay propagation evade the lifetime activity bounds? |  |
| `FIXED_FOOTPRINT_CAPTURE_INERTIA_DIAGNOSTIC.md` | Capture, inertia and which quantity grows |  |
| `FORMATION_CLOCK_AND_SOURCE_OBLIGATIONS.md` | Formation clocks, acoustic travel, and what a capturing source must store |  |
| `FORMATION_INTENSITY_DERIVATION.md` | Primary extension: retain the whole motion semigroup at small formation rate |  |
| `FOUR_SITE_CONTEXT_CLASSIFICATION_DERIVATION.md` | The mean-current scope of a collinear four-site read footprint |  |
| `GAUSS_WORM_COMPLETED_SCREEN_REPORT.md` | Constrained-record equilibrium screens and global/local covariance |  |
| `GRAM_KERNEL_CUBIC_FORMATION_RESPONSE.md` | A Gram-kernel invariant controls the first density correction |  |
| `GROWING_PRODUCT_FLUCTUATION_DERIVATION.md` | Formation noise and the growing-product Euler fluctuation limit |  |
| `IMMUTABLE_STREAMING_DERIVATION.md` | Immutable directional exchange: a positive transport continuation |  |
| `IMMUTABLE_TRANSVERSE_MAXWELL_CONSTRUCTION.md` | Two transverse wave polarizations from supplied immutable exchanges |  |
| `INITIAL_RESPONSE_DERIVATION.md` | Primary derivation: population-normalized orientation in the growing process |  |
| `LITERATURE_CONTEXT.md` | Targeted literature comparison |  |
| `LOCAL_ACTIVITY_DERIVATION.md` | Primary derivation: a permanent formation clock and lifetime activity |  |
| `MAXWELL_ENTROPY_AND_WAVE_ENERGY.md` | Relative entropy and the energy flux of the transverse wave sector | primary derivation; |
| `MAXWELL_FORMATION_AND_FULL_OCCUPANCY.md` | Formation, empty start and a transverse sector that survives full occupancy | primary construction and theorem application; |
| `MAXWELL_GAUSS_SECTOR_PREPARATION.md` | Preparing a finite-mode Gauss sector without changing the exchange rule |  |
| `MAXWELL_POLAR_AXIAL_SYMMETRY_EXTENSION.md` | Polar/axial symmetry and physical time reversal of the transverse construction | primary derivation; |
| `NATIVE_FORMATION_SCREEN_REPORT.md` | Native formation wave screen: completed comparison and its limits |  |
| `NATIVE_FORMATION_THIRD_ORDER_CENTERING_DERIVATION.md` | A computable third-order formation correction below the Euler scale |  |
| `PAIRED_FORMATION_TRANSVERSE_NOISE_DESIGN.md` | Opposite-pair formation as a controlled alternative noise design |  |
| `PAIR_EXCHANGE_CURRENT_CLASSIFICATION.md` | What can be changed by tuning immutable pair-exchange rates? |  |
| `POLYNOMIAL_FLUX_REALIZATION_DERIVATION.md` | Realizing a polynomial current potential by immutable local exchanges |  |
| `PROPER_CUBIC_ELEVEN_COUPLINGS_AND_VECTOR_SELECTION.md` | Removing the extra reflection premise: all eleven proper-cubic couplings |  |
| `QUANTUM_DEADLINE_APPROXIMATION_DERIVATION.md` | A consistent quantum clock with sharp deadline error |  |
| `QUANTUM_FORMATION_INTERFACE_DERIVATION.md` | Primary derivation: a single-qubit interface for the formation kernel |  |
| `QUANTUM_RATE_SELECTION_DERIVATION.md` | Primary derivation: operational consistency and the formation clock |  |
| `QUANTUM_WAITING_TIME_DERIVATION.md` | Primary derivation: instantaneous rate consistency versus a full waiting law |  |
| `REPEATED_FORMATION_QUANTUM_MEMORY_DERIVATION.md` | Primary derivation: repeated formation and the quantum memory resource |  |
| `TERMINAL_CORRELATION_DERIVATION.md` | Primary derivation: terminal connected correlations at fixed positive rates |  |

Independent packets: `cubic_symbol_independent/`, `fourteen_quantum_independent/`, `gauss_loop_independent/`, `gauss_polymer_independent/`, `gauss_sampler_independent/`, `gibbs_transport_independent/`, `independent_admissibility_euler/`, `independent_axis_balanced_context/`, `independent_context_euler/`, `independent_context_exchange/`, `independent_context_fluctuations/`, `independent_finite_influence/`, `independent_growing_fluctuations/`, `independent_initial_response/`, `independent_native_centering/`, `independent_polynomial_flux/`, `independent_quantum_interface/`, `independent_quantum_waiting/`, `independent_repeated_formation/`, `independent_transverse_exchange/`, `local_curl_independent/`, `proper_cubic_extension_independent/`, `winding_stiffness_independent/`.

### Campaign 2 (2026-09-21/22), `campaign12h_second/`

Published milestones: #8589, #8594, #8600, #8604, #8609, #8610 (open).

| Note | Title | Status as written |
|---|---|---|
| `BOUNDED_CYCLE_FLOW_AND_EULER_DYNAMICS.md` | Bounded configuration cycles and the missing Gibbs-to-wave connection |  |
| `CAMPAIGN_REPORT.md` | Second mobile-record physics campaign |  |
| `DIMER_COLOR_OPERATIONAL_MOMENT_MAP.md` | The operational moment map of the fourteen classical pair colors |  |
| `DIMER_COVARIANT_QUANTUM_FLUCTUATION_ENCODING.md` | A covariant two-qubit encoding and its fluctuation-energy test | proposed construction and conditional calculations; |
| `DIMER_MIXED_ENCODING_INITIAL_DRIFT_AMBIGUITY.md` | Exact initial-drift ambiguity in the six-moment mixed quantum encoding | root-derived finite counterexample; |
| `DIMER_PAIR_COVARIANCE_CUBIC_MOMENT.md` | Cubic color information in a covariant single-pair density encoding | proposed exact representation identity and finite compatibility witness; |
| `DIMER_ROUTED_FINITE_WAVELENGTH_ASSESSMENT.md` | What the finite-wavelength winding calculation explains |  |
| `DIMER_ROUTED_FINITE_WAVELENGTH_PROJECTION.md` | A parameter-free finite-wavelength benchmark on the winding matching |  |
| `DIMER_TWO_PAIR_FAITHFUL_COVARIANT_ENCODING.md` | A faithful covariant density encoding on two record-pair Hilbert spaces | proposed constructive escape at the preparation-map level; |
| `GEOMETRIC_GROWTH_TABLE.md` | GEOMETRIC_GROWTH_TABLE.md |  |
| `GEOMETRIC_QUANTUM_LIFT_BOUNDARY.md` | Coherent dimer permutations and the literal qubit state-space question |  |
| `GEOMETRIC_SINGLET_CHANNEL_AND_COHERENT_FILTER.md` | Quantum channels for a matching-to-singlet conversion |  |
| `GEOMETRIC_SINGLET_FIBER_AND_LOCAL_HAMILTONIANS.md` | An antisymmetric record fiber and physical singlet-cover states |  |
| `PAIRED_RECORD_FORMATION_AND_DIMER_GAUSS.md` | Paired immutable records: nearest-neighbor formation and a dimer Gauss readout | proposed supplied classical process, with conditional elementary identities below. |
| `PAIRED_RECORD_PARITY_AND_RESIDUAL_VACANCIES.md` | Direction-count parity and a macroscopic Gauss bound |  |
| `PAIRED_RECORD_PERIODIC_JAM_AND_ESCAPE.md` | A periodic paired-record jam and a local immutable escape | author conditional construction and counterexample, 2026-09-21. |
| `PREPARED_TRANSVERSE_EULER_STATE.md` | A prepared transverse state for the immutable-record Euler wave process |  |

Independent packets: `cycle_flow_independent/`, `dimer_covariant_quantum_independent/`, `dimer_edge_face_gauss_independent/`, `dimer_finite_qubit_curl_independent/`, `dimer_local_dilute_curl_independent/`, `dimer_mixed_drift_independent/`, `dimer_moving_nonlinear_independent/`, `dimer_nonlinear_flux_independent/`, `dimer_pair_cubic_independent/`, `dimer_routed_diffusive_gap_independent/`, `dimer_routed_dynamic_independent/`, `dimer_routed_finite_wavelength_independent/`, `dimer_routed_moving_geometry_independent/`, `dimer_routed_preparation_independent/`, `dimer_routed_quantitative_euler_independent/`, `dimer_routed_transport_independent/`, `dimer_smooth_nonlinear_independent/`, `dimer_two_pair_encoding_independent/`, `geometric_all_stage_independent/`, `geometric_all_stage_polynomial_independent/`, `geometric_fixed_rate_independent/`, `geometric_fixed_rate_production_independent/`, `geometric_general_graph_independent/`, `geometric_last_pair_clock_independent/`, `geometric_partner_independent/`, `geometric_polynomial_relaxation_independent/`, `geometric_quantum_lift_independent/`, `geometric_rare_birth_independent/`, `geometric_singlet_independent/`, `paired_record_independent/`, `periodic_parity_independent/`, `prepared_state_independent/`.

### Campaign 3 (2026-09-22/23), `campaign12h_third/`

Published milestones: #8635, #8650, #8661, #8672 (closed after landing in narrowed form in 9d8596c758).

| Note | Title | Status as written |
|---|---|---|
| `ADAPTING_RECORD_COOLING_AWAY_FROM_THE_RK_POINT.md` | Adapting record cooling when the field Hamiltonian changes | personal conditional analysis, independent check pending. |
| `APPROACH_REGISTRY.md` | Third-campaign approach registry |  |
| `AUTONOMOUS_MOVING_FUEL_FOR_GAUGE_RECORD_FORMATION.md` | Autonomous moving fuel implements a conditional record-formation channel | author construction with explicit hypotheses; |
| `BALLISTIC_FIELD_SIGNALS_FROM_RECORD_FORMATION.md` | Ballistic field signals from record formation in a one-dimensional model | exact finite sector identities, a second-order microscopic coefficient, and an exact calculation for a separately declared reduced transport kernel; |
| `CAMPAIGN_OUTCOME.md` | Third campaign outcome |  |
| `CLASSICAL_PERMANENT_RECORDS_WITH_QUANTUM_GAUGE_MEMORY.md` | Classical permanent records with quantum gauge memory | personal provisional construction and proofs; |
| `COHERENT_NEUTRAL_PAIR_FORMATION_AND_GAUGE_MEMORY.md` | Coherent neutral-pair formation can retain a gauge-loop phase | author conditional channel classification and exact finite preparation. |
| `COHERENT_PREPARATION_AFTER_LOCAL_RECORD_COOLING.md` | Coherent ground preparation after local record cooling | conditional finite-component construction, exact integer spectral certificate, and converged numerical controls; |
| `COHERENT_RECORD_MOTION_AND_BIRTH_BACKACTION.md` | Coherent record motion and birth backaction in supplied occupation models | author derivations and exact finite checks; |
| `COHERENT_RING_FORMATION_WITHOUT_OCCUPATION_MONITORING.md` | Coherent ring motion can complete formation without occupation monitoring | author conditional theorem and exact finite observability certificates; |
| `COLLECTIVE_RECORD_CIRCULATION_RELEASES_GAUGE_TRAP.md` | Local collective record circulation releases the tested U(1) trap | author construction and exact finite certificate; |
| `DEPOLARIZED_POINTER_RATE_BOUNDARY.md` | A metric-compatible noisy pointer still fails the exact routed rate law |  |
| `DIMER_FIXED_ENCODING_QUANTUM_CONTRACTION.md` | Exact contraction test for the frozen fourteen-color preparation | exact author certificate; |
| `FINITE_CUBIC_RECORD_COOLING_AND_RETUNED_GROUND_PREPARATION.md` | Finite cubic record cooling and an explicitly retuned ground-state channel | personal conditional results, independent check pending. |
| `FINITE_CYCLIC_APPROXIMATION_OF_GAUGE_RECORD_INSTRUMENTS.md` | Finite cyclic approximation of gauge record instruments | personal conditional theorem candidate; |
| `FORMATION_COUNT_CONTROLS_GAUGE_COHERENCE.md` | Formation count controls a specified gauge-conjugation coherence | author conditional theorem and executed exact controls; |
| `FRESH_CHARGED_RECORD_READOUT_OF_SPIN_HALF_GAUGE_LOOPS.md` | Fresh charged records read spin-half gauge-loop coherence | personal conditional construction with direct operator proof; |
| `FRESH_MOVING_MEMORY_DILATES_COHERENT_PAIR_BIRTH.md` | Fresh departing memory gives an explicit coherent pair-birth dilation | author exact finite construction, awaiting independent check. |
| `GAUGE_COVARIANT_PERMANENT_RECORD_DYNAMICS.md` | Gauge-covariant permanent records: a finite positive construction and a truncation test | author conditional constructions and exact controls; |
| `INITIAL_ENERGY_COST_AND_NUMBER_OFFSET_OF_RECORD_FORMATION.md` | Initial formation, energy injection, and a number-energy ambiguity | author conditional calculation, independent check pending. |
| `LOCAL_GAUGE_RECORD_COOLING_TO_RK_STATES.md` | Local gauge cooling with fresh permanent records | personally derived conditional finite-volume theorem, awaiting independent reconstruction. |
| `LOCAL_WEIGHTED_RECORD_COOLING_AND_FINITE_GROUND_APPROXIMATION.md` | Local weighted record cooling and a finite ground-state approximation | personally derived conditional extension and finite variational test; |
| `OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md` | Occupation monitoring makes contact pair formation complete on finite graphs | author conditional theorem, exact four-site controls, independent check pending. |
| `PARTIAL_BIJECTIVE_GAUGE_HOPS_AND_QUANTUM_COMPLETION.md` | A finite quantum completion criterion for partially allowed gauge hops | author conditional theorem and exact finite controls; |
| `PERMANENT_RECORD_CONTENTS_AND_SYMMETRIC_FIELD_DYNAMICS.md` | Permanent record contents and symmetric field dynamics |  |
| `POST_FORMATION_NEXT_DECISIONS.md` | Next decisions after finite formation and fast motion |  |
| `REPEATED_FORMATION_AT_FIXED_FOURTH_ORDER_SCALE.md` | Repeated formation with a nonvanishing fourth-order energy scale |  |
| `SIX_QUBIT_COVARIANT_POINTER_DYNAMICS.md` | A covariant block pointer for records, vacancy, transport and renewed birth |  |
| `STATIC_SOURCE_COULOMB_ENERGY_IN_THE_ROTOR_TARGET.md` | Static-source Coulomb energy in the compact rotor target |  |
| `TWO_VACANCY_QUANTUM_COMPLETION_CLOCK.md` | Two remaining vacancies: exact clocks and fixed-size dephasing limits | author conditional results, with exact finite controls and an exploratory numerical screen; |
| `U1_EXTREME_FLUX_RECORD_TRAPPING.md` | Extreme-flux trapping of permanent records in a spin-half U(1) model | author exact finite certificates and analytic conditional trapping argument; |
| `VIRTUAL_MULTIPLE_OCCUPANCY_SOURCE_FOR_RECORD_CIRCULATION.md` | A virtual multiple-occupancy source for one record-circulation matrix element | author exact perturbative coefficient in an explicitly enlarged finite model; |

Independent packets: `autonomy_count_independent/`, `birth_backaction_independent/`, `gauge_coherent_birth_independent/`, `gauge_readout_cooling_independent/`, `gauge_record_independent/`, `large_spin_rotor_independent/`, `pointer_dynamics_independent/`, `quantum_clock_completion_independent/`, `quantum_metric_independent/`, `rk_cooling_adaptation_independent/`, `weak_field_waves_independent/`.

### Campaign 4 (2026-09-23/24), `campaign12h_fourth/`

Published milestones: #8831, #8832, #8839, #8841, #8845, #8852, #8865, #8870, #8873, #8891, #8898, #8923, #8929, #8936, #8946, #8953, #8957, #8958 (closed).

| Note | Title | Status as written |
|---|---|---|
| `FINITE_SPIN_WORKING_HYPOTHESES.md` | Finite-spin post-formation hypotheses, before controls |  |
| `GAPLESS_FLAT_SECTOR_LIMIT_WORKING_ARGUMENT.md` | Proposed finite-spin flat-sector limit: open proof obligations |  |
| `LOCAL_COUNTERTERM_PROPOSAL.md` | Root constructive follow-up: a local compensation candidate |  |
| `POST_FORMATION_WORKING_DERIVATIONS.md` | Fourth campaign: provisional post-formation calculations |  |

