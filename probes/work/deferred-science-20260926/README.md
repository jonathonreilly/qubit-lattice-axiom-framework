# Deferred science 2026-09-26: unpublished Codex mobile-record research

Source: the local Codex branch `codex/mobile-record-post-formation-campaign-20260923` (head `eb34060bef`). It is the private raw record of four twelve-hour mobile-record campaigns, run 2026-09-20 to 09-24, and it exists only on the owner's machine. It was never pushed because its history carries copies of third-party papers and about 670 MB of raw simulation arrays.

The campaigns published their milestones as curated PRs:

- #8545–#8610 are open;
- #8635–#8672 and #8831–#8958 landed in narrowed form.

## Triage

Owner rule (2026-09-26): only validated science that moves the program forward goes into a PR; probable work goes on this backlog.

None of the unpublished material met the PR bar:

- every result is conditional on supplied carriers, Hamiltonians, instruments, rates or preparations;
- Codex's separate-context checks were within the same model family, so they are not cross-model confirmation.

The probable parts are queued as the eight research units below. Each unit's `RECOVERY_STATUS.json` must say whether its result is ready to become a science PR.

| Unit | Title |
|---|---|
| `J:derive:deferred-20260926-quantum-record-codes-and-pointers:a1` | Quantum codes and pointers for mobile records |
| `J:derive:deferred-20260926-coherent-vacancy-birth-and-clocks:a1` | Coherent vacancy motion, birth back-action and completion clocks |
| `J:derive:deferred-20260926-gauge-record-traps-and-circulation:a1` | Permanent charged records in a spin-half U(1) model: traps and circulation |
| `J:derive:deferred-20260926-coherent-formation-instruments:a1` | Coherent formation instruments and a retained gauge phase |
| `J:derive:deferred-20260926-local-rk-preparation:a1` | Local preparation of RK states by record cooling |
| `J:derive:deferred-20260926-author-only-field-results:a1` | Author-only field results: static-source Coulomb energy and formation energy offsets |
| `J:derive:deferred-20260926-colour-encodings-quantum-lift:a1` | Quantum encodings of the fourteen pair colours and the geometric quantum lift |
| `J:derive:deferred-20260926-cubic-couplings-and-gauss-screens:a1` | Proper-cubic coupling classification and Gauss-loop screens |

Also queued earlier today:

- `C:recovered-fixed-rate-geometric-formation:a1/a2`, for the fixed-rate formation follow-up;
- `C:recovered-dimer-routed-color-waves:a1/a2`, for the dimer-routed screens.

Their curated copies are in `probes/work/worktree-sweep-20260926/codex-sync-2026-09-21-second/`. The full packets are also in this bundle, under `campaign12h_second/`.

Not queued:

- **Campaign 1's working derivations.** They were rewritten into PRs #8545–#8569.
- **Campaign 2's paired-record and bounded-cycle notes.** They are an earlier route that preceded the geometric construction in open PR #8589.
- **Campaign 4's working notes:** finite-spin hypotheses, the flat-sector working argument, the local counterterm proposal and local electric moments at finite time. Their topics are covered by `J:derive:deferred-20260924-spin-packets:a1`, `J:derive:deferred-20260924-residuals:a1` and `J:derive:deferred-20260924-star-packets:a1`.
- **Campaign 4's "external S1 numerical ranks".** The closure note says they have no exact certificate, but the underlying computation could not be located in the branch.
- **The Gauss-loop screens.** They are folded into the cubic-couplings unit, which asks for a comparison with the uniform-ice results already landed on main.

## Layout

`mobile-record-formation-20260920/` mirrors `.claude/science/mobile-record-formation-20260920/` on the source branch. It holds only the 4,089 files (39.8 MB) whose content is not already on origin: on `main`, `ai/probes` or any `codex/*` branch.

`PRESERVATION_MANIFEST.json` lists, with blob ids:

- the 3,283 files already on origin;
- the 405 excluded files (743.4 MB):
  - raw array/state data: 375 files, 691.9 MB
  - large per-run JSON output (aggregate kept): 11 files, 6.5 MB
  - large raw csv output: 5 files, 37.2 MB
  - compiled binary: 4 files, 0.3 MB
  - copy of a third-party paper: 4 files, 1.0 MB
  - copy of agent planning instructions: 3 files, 0.0 MB
  - large raw JSON (per-run data or hash inventory): 2 files, 4.7 MB
  - large raw log output: 1 files, 1.7 MB

The excluded files remain only in the local source branch, so that branch should be kept.

## Unpublished notes by campaign

Titles and status lines are quoted from the notes as written. Many notes later received a separate independent packet, found in the sibling `*_independent/` folders, so a quoted "independent check pending" can be out of date. `campaign12h_third/APPROACH_REGISTRY.md` gives each campaign-3 family's evidence and status at closure.

### Campaign 1 (`campaign12h/`)

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

### Campaign 2 (`campaign12h_second/`)

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

### Campaign 3 (`campaign12h_third/`)

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

### Campaign 4 (`campaign12h_fourth/`)

| Note | Title | Status as written |
|---|---|---|
| `FINITE_SPIN_WORKING_HYPOTHESES.md` | Finite-spin post-formation hypotheses, before controls |  |
| `GAPLESS_FLAT_SECTOR_LIMIT_WORKING_ARGUMENT.md` | Proposed finite-spin flat-sector limit: open proof obligations |  |
| `LOCAL_COUNTERTERM_PROPOSAL.md` | Root constructive follow-up: a local compensation candidate |  |
| `POST_FORMATION_WORKING_DERIVATIONS.md` | Fourth campaign: provisional post-formation calculations |  |

