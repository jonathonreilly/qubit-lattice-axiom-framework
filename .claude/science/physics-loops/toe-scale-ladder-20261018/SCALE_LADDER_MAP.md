# Scale-Ladder Frontier Map — 2026-10-18

Read-only analysis against `origin/main @ 584755767`. Planning material only:
this file asserts no theorem, applies no audit verdict, and adopts no axiom or
primitive. Following the caller's instruction, **every result cited below is
treated as unaudited conditional**, whatever grade words appear in the source
notes. Claim types follow `docs/ai_methodology/SCIENCE_WORKFLOW.md` §2:
PCI = proved conditional implication (author proof, supplied premises);
CON = construction / explicit model; NUM = numerical evidence; OBL = open
obligation; NOGO = obstruction theorem over a quantified family (still
conditional); META = plan or registry.

## 0. Supplied foundation (what may be used without a bridge)

| Item | Source | Content limit |
|---|---|---|
| Lattice, Qubit (`M_2(C)`), Admissibility, Record | `docs/MINIMAL_AXIOMS_2026-06-29.md` (machine form: `docs/audit/data/axiom_premise_nodes.json`, node `minimal_axioms`) | Admissibility is *not* a dynamics axiom: no Hamiltonian, transfer operator, time metric, rate, or record-production process. |
| Scale reference `a^{-1} = M_Pl` | `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` | Units only. Explicitly does **not** assert `a/l_P = 1`, which remains an open gravity derivation. |
| Kinetic isotropy `c_t = c_s` | `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | Regulator-geometry (OS0) graining fact; no dimensionless dynamical content. |
| Realized state | `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | Pointwise evaluation at one law-admissible state; no averaging or typicality. |
| Owner-approval record | `docs/audit/AXIOM_MINIMALITY_POLICY.md` §6 | Any new primitive needs owner approval. |
| Parked forks | `docs/repo/DEFERRED_DECISIONS.md` | Record Statistics (Born bridge), structuralist reading, C-add composition, `M_4(C)` enlargement, σ-reality, OS-closure residue. All parked. |
| Underdetermination plan | `docs/TOE_DERIVATION_CAMPAIGN_AXIOM_SUFFICIENCY_BY_UNDERDETERMINATION_WITNESSES_NOTE_2026-09-13.md` (META) | Contract for model-pair witnesses. |
| Fourth-axiom RG scoping | `docs/FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05.md` (META, historical) | RG fixed points are the wrong category for the generation moduli. No axiom proposed. |

**Supplied premises that recur everywhere above R0** (from the notes' own
premise tables):
- **(D)** a dynamics: a Hamiltonian, QCA tick or generator. Never supplied by the axioms.
- **(S)** a soldering action, i.e. how cubic rotations act on the qubit: `docs/THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md`.
- **(F)** a formation order or clock law for records.
- **(R)** the reading of Admissibility: static full-conditional, sequential formation, or hard-support stabilizer.
- **(C)** an enlarged carrier: several qubits per site, link qubits, or `C^8` color.
- **(I)** observable identifications and empirical inputs (e.g. `beta = 6`, `N_f`, the Sommer scale).

---

## R0 — Single site / axiom level

**(a) Strongest results**
- PCI/NOGO. Order-blind formation classification. Strictly positive, translation-covariant, order-blind rules are exactly the product form `r0 prod phi_d`. They are nonconstant only under soldering. Source: `docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md`.
- PCI. The static (full-conditional) reading of a binary rule is compatible only with an Ising-form action: `docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`.
- NOGO family. Record formation is not forced by the axioms (`docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`). The exchange sign is not supplied by records (`docs/ADMISSIBILITY_RULE_THE_EXCHANGE_SIGN_IS_NOT_SUPPLIED_BY_RECORDS_..._2026-09-24.md`). Shell-lock possibility and direction are not forced (`docs/BINARY_SHELL_LOCK_POSSIBILITY_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-10.md`, `docs/TERNARY_SHELL_LOCK_DIRECTION_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-10.md`).
- PCI. Cl(3) per-site uniqueness: `docs/AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`. Legacy surface; treat as conditional.
- Honest wall: Born weights and probability are not derived (`docs/repo/STATE_OF_THE_THEORY_2026-07-16.md`, "The honest walls"). The supplied-Born identities are collected in `docs/DYNAMICS_CLAUSE_CAMPAIGN_SYNTHESIS_WHAT_ONE_LOCAL_DYNAMICS_CLAUSE_BUYS_AND_WHAT_IT_LEAVES_OPEN_BOUNDED_THEOREM_NOTE_2026-09-24.md`.

**(b) Open upward bridge R0→R1**
- **OBL-R0.1 (dynamics):** obtain a local generator or tick from the axioms. It is not supplied, and the memo says so explicitly.
- **OBL-R0.2:** fix the soldering action (S) and the reading of Admissibility (R).
- **OBL-R0.3:** fix a formation order or clock (F).

**(c) Oct 2026 work.** About 150 of the 402 notes dated 2026-10 sit at this
level. Examples are the `CHIRAL_PAIR_*` family (68 notes, 2026-10-10) and the
`*_CAP_*`, `*_KERNEL_*`, `ZERO_ONE_TWO_*`, `MODULUS_THREE_*` and `*_ORBIT_*`
kernel enumerations. They densify the order-blind kernel census on the
48-point chiral pair and the 24-point orbit. None of them supplies (D), (S) or
(F). Densification only.

**(d) Blocking premises.** (D), (S), (F), (R). The Born/statistical bridge is
parked (`DEFERRED_DECISIONS.md` §1).

---

## R1 — Finite patch: local dynamics, generators, clocks, records, batteries

**(a) Strongest results**
- NOGO/PCI. **Cubic covariance freezes a one-qubit tick.** On the 27-point (and 125-point) cell, with the spin-1/2 soldered coin, every O- or T-covariant unitary walk is constant. 3D motion needs a symmetry group of order at most 4. Source: `docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md`. This is the most consequential recent R1 fact. Its range-3 extension is an unreproduced proof candidate.
- CON/PCI. A two-qubit site unfreezes the walk and gives a Dirac walk with gapped axis doublers (`docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md`, premise (C)). The same content can be spread over staggered one-qubit corner blocks (`docs/STAGGERED_ONE_QUBIT_BLOCKS_CARRY_A_CUBIC_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-16.md`).
- NOGO. A Maxwell tick with radius-one onsite unitarity cannot propagate (`docs/U1_RADIUS_ONE_ONSITE_UNITARY_MINIMAL_MAXWELL_TICK_BOUNDED_NO_GO_NOTE_2026-09-03.md`). Under every two-site generator, an exact Gauss law freezes the link field (`docs/DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_..._2026-09-24.md`).
- NOGO. One-qubit cubic stabilizer rules have no 3D-mobile fermionic defect. The only axis/full-soldered rule is the Chamon octahedron. Source: `docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md`. Companions: `THREE_AXIS_QUBIT_*`, `TWO_QUBIT_SITE_SOLDERED_SPIN_*` and `SITE_LOCALIZABLE_STABILIZER_CODE_FERMION_CANNOT_CARRY_THE_SPIN_HALF_CLASS_*` (all 2026-10-17).
- PCI. Locality of marginals makes a site's evolution between records linear and completely positive (`docs/DYNAMICS_CLAUSE_LOCALITY_OF_MARGINALS_MAKES_A_SITE_S_EVOLUTION_BETWEEN_RECORDS_LINEAR_AND_COMPLETELY_POSITIVE_BOUNDED_THEOREM_NOTE_2026-09-24.md`).
- CON (engineering). Finite compilers, controllers, clocks, buses, batteries and preparations. Example: `docs/LITERAL_L4_NEAREST_NEIGHBOR_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-10-14.md` gives an 802,688-slot Pauli ledger with a 3.6e13-pulse schedule that was neither expanded nor executed, and its strong-penalty recovery was not demonstrated at the fixture.

**(b) Open upward bridge R1→R2**
- **OBL-R1.1:** a framework-selected (D) whose infinite-volume dynamics has a nontrivial phase structure (gap, order, or deconfined gauge phase). Existence of infinite-volume dynamics for bounded finite-range interactions is textbook (Bratteli–Robinson Vol. 2 §6.2; Nachtergaele–Sims Lieb–Robinson bounds). It is **not** the open part.
- **OBL-R1.2:** a one-qubit-per-site dynamics compatible with (S) that propagates in 3D. The single-particle walk is frozen; the many-body QCA class is unclassified (see C4).
- **OBL-R1.3:** the infinite-volume and phase content of the record or formation law (see R2).

**(c) Oct 2026 work.** Roughly 80 controller/clock/compiler/memory/readiness
notes and roughly 50 energy/current/refinement notes are finite-patch
statements under supplied (D), mostly on 1D or fixed small graphs. They do not
move R1→R2: none proves a property uniform in volume for a 3D model. The
exceptions that touch the bridge are the 2026-10-16/17 freeze and no-mobile-
defect no-gos. Those *retire* routes, which is real progress on the
classification side of OBL-R1.2.

**(d) Blocking premises.** (D) for everything; (C) for every moving fermion; (S).

---

## R2 — Infinite volume / thermodynamic limit

**(a) Strongest results**
- PCI. **Order-blind positive formation is a 1-dependent Gibbs field on all of Z^3.** The static and formation readings agree for this class. There are no critical or Coulomb correlations, no long-range order and no pinch points. Source: `docs/ORDER_BLIND_POSITIVE_FORMATION_IS_A_ONE_DEPENDENT_GIBBS_FIELD_BOUNDED_THEOREM_NOTE_2026-10-16.md`. This is a genuine axiom-level R2 statement, under premises (R) and (F).
- PCI. With iid activation times there is a unique infinite permanent-record realization. Every ancestor set is finite almost surely, with `P(decreasing path of length n) <= 6*5^(n-1)/(n+1)!`. Source: `docs/NATIVE_RECORD_SUPPORT_PRESERVING_PRIORITY_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`. Premise (F) is supplied. The method is Penrose–Sudbury, cited there. **The mixing / no-phase corollary is not stated.**
- PCI. The level-order formation law has an ordered phase at strong coupling: a noisy majority eroder with an explicit threshold and at least six invariant laws. Sources: `docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md` and its 2026-09-15 parent. This is a Toom-type stability argument (Toom 1980), so it is known in kind. The level order picks a body diagonal; no total order on Z^3 is invariant under a proper rotation (`docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`, line ~176).
- PCI. Under independent exponential activation, formed sites at fixed time are Bernoulli site percolation. Critical-percolation consequences follow from an external formalized theorem. Source: `docs/RECORD_ACTIVATION_CRITICALITY_AND_CONDITIONED_PLANAR_MODELS_BOUNDED_THEOREM_NOTE_2026-10-08.md`.
- PCI (supplied H). Unique ground state and a uniform gap `> log(25/14)/4` for periodic PXP and the staggered spin-1/2 link *ring*, at every even L ≥ 6. Source: `docs/PERIODIC_PXP_AND_STAGGERED_LINK_RING_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-10-07.md` (1D/ladder only; the two-purity bootstrap is external).
- PCI (supplied H). The 3D Pauli ferromagnet has a translation-invariant KMS state with magnetization at least 1/4 at large β, via an external Lean-covered theorem. Source: `docs/SUPPLIED_FERROMAGNET_ORDER_AND_LOW_TEMPERATURE_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-10-08.md`.
- PCI (supplied quadratic H). Thermodynamic local-CAR limit of the quasi-local star creator: `docs/NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md`.
- PCI (supplied H). Lieb–Robinson / microcausality on the legacy staggered+Wilson carrier (`docs/AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`) and Combes–Thomas quasilocality (`docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`). These are textbook-type statements.
- NUM. The 3D cubic spin-1/2 link ring model (photon question) has about 38 `docs/RING_MODEL_*` notes. Projector / Green's-function MC at the pure-ring point gives guide-dependent energies (6–10σ shifts) and an unresolved curvature estimate (0.81–1.11). An effective population below 25 is reported in `docs/RING_MODEL_ON_16_CUBED_THE_PROJECTOR_ENERGY_DEPENDS_ON_THE_GUIDE_BY_SIX_STANDARD_ERRORS_AND_THE_EFFECTIVE_POPULATION_STAYS_BELOW_TWENTY_FIVE_BOUNDED_THEOREM_NOTE_2026-10-01.md`. Frozen flip components are found in the zero-winding sector (`docs/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md`). **No decision on Coulomb vs ordered.**

**(b) Open upward bridges R2→R3**
- **OBL-R2.1 (lowest):** a 3D deconfined U(1) (Coulomb) phase in some supplied one-qubit-per-link model with Gauss law, or a proof that it is absent. The pure-ring point is undecided.
- **OBL-R2.2:** infinite-volume record phases under a *covariant* formation law. Order-blind gives no phases; level order gives a phase but breaks covariance. The random-order case is undecided as a stated theorem (see C3).
- **OBL-R2.3:** a gapped phase hosting a stable mobile fermion in 3D, with stability under all small covariant perturbations.

**(c) Oct 2026 work.** The 2026-10-16 1-dependent Gibbs theorem and the
2026-10-07 uniform gap move R2 genuinely, but for restricted classes or in
1D. The ring-model MC in late Sep and Oct 1 densifies NUM without a decision.
The clocks, batteries and controllers do not touch R2.

**(d) Blocking premises.** (D) for every Hamiltonian phase; (F) and (R) for record phases; (C) for link qubits.

---

## R3 — Continuum / IR effective theory

**(a) Strongest results**
- PCI (supplied 1D transverse-Ising chain). Strong convergence of the actual boost/energy/current groups to a free massive 1+1D Poincaré representation on Fock space, with `O(a)` and `O(a^2)` packet rates. Not operator-norm convergence; no local-net convergence. Sources: `docs/GAPPED_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md`, `docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md` (exact finite-spacing Lie closure *fails*), `docs/CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md`, `docs/LOCAL_EVEN_NET_SECTIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md`. Textbook content: Ising chain → free Majorana via Jordan–Wigner.
- CON (supplied, C). The corner-fermion long-wavelength theory is one isotropic spin-1/2 doublet, using 48 qubits per site. The massless Dirac pair is protected by cube rotations. Sources: `docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`, `docs/CORNER_FERMION_MASSLESS_DIRAC_PAIR_PROTECTED_BY_CUBE_ROTATIONS_*_2026-10-17.md`. Prior art: Levin–Wen PRB 67 245316 (2003); Levin–Wen "quantum ether" PRB 73 035122 (2006); 3D Kitaev models.
- CON. Bravyi–Kitaev superfast (BKSF) cubic fermion codes have a fermionic charge but are not rotation-invariant (minimal orbit 4). Spinorial action holds only under bare permutations. Source: `docs/BKSF_CUBIC_FERMION_CODES_*_2026-10-17.md` (three notes).
- PCI (supplied comparator). The Gaussian lattice-Maxwell comparator: `docs/THE_GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_FINITE_SIZE_ENERGY_SHIFT_*_2026-10-01.md`. This is a free-field textbook object.
- PCI (supplied, C). Weyl nodes with exact charges in composite-site Majorana networks (`docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_*_2026-10-01.md`, about 20 notes) and in the two-qubit Dirac walk.
- PCI (supplied kinetic model). Fluid limits: `docs/D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md` and `docs/SPATIAL_PARTICLE_TO_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md`. Chapman–Enskog / Saint-Raymond-type content.
- Reduction (PCI with named imports). Sakharov-induced `G_N ~ a^2`. The residual is a metric-DOF posit, and heat-kernel and `N_f` are imported. Source: `docs/UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17.md`.
- CON (top-down, supplied continuum action). The `EXPONENTIAL_SCALAR_*`, `SCALAR_*`, `METRIC_CLOCK_*` and `CASSINI_*` families (about 58 notes, 2026-10-13..17). Supplied scalar-tensor actions with inverse problems and observational conditioning. They are **not** connected downward to R2. They hang from R3/R4 with no lattice bridge.

**(b) Open upward bridges R3→R4**
- **OBL-R3.1 (lowest, Lorentz):** a single model whose emergent photon and emergent fermion share one light cone. Kinetic isotropy fixes the regulator `c_t = c_s`, not the IR velocities.
- **OBL-R3.2 (chirality):** net chirality. Every walk found so far has three-winding 0 (CUBIC_COVARIANCE_FREEZES item 4). The Floquet evasion of Nielsen–Ninomiya under cubic covariance is untested.
- **OBL-R3.3:** a 3+1D continuum limit of any supplied 3D dynamics. Only 1+1D free exists.
- **OBL-R3.4 (gravity):** derive the metric DOF; derive `a/l_P` (scale-reference self-consistency).
- **OBL-R3.5:** interacting continuum limit of any gauge theory. Open, and not 24h-scale.

**(c) Oct 2026 work.** The 1D continuum Poincaré limit is a real but textbook
R2→R3 step for a supplied free model. The fermion-code and walk results move
OBL-R3.2's precondition, a classification of what moves, in the negative
direction. The scalar-gravity families densify an unanchored top layer. They
do not bridge to R2.

**(d) Blocking premises.** (D) and (C); the metric-DOF posit; (I) heat-kernel and `N_f`; the soldering (S) that decides spin-1/2.

---

## R4 — Physical scale hierarchy and observables

**(a) Strongest results (all conditional, many legacy)**
- The `beta = 6` / `g_bare` normalization is an import (`docs/repo/STATE_OF_THE_THEORY_2026-07-16.md` walls; `docs/audit/G_BARE_PROMOTION_PANEL_FINDING_2026-05-28.md`, source-blocked).
- Hierarchy: the `alpha_LM^16` magnitude is an open gate (`docs/HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md`, OBL). The exponent's species-count bridge is a regulator-dependence no-go (`docs/HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md`).
- Hadron `sqrt(sigma)`: imported SU(3) Yang–Mills / Sommer scale (`docs/CONFINEMENT_STRING_TENSION_NOTE.md`; `docs/lanes/open_science/01_HADRON_MASS_PROGRAM_OPEN_LANE_2026-04-26.md`).
- `y_t`: no-go on primitive unit source action (`docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md`).
- Cosmological constant: structural identity `Lambda_vac = lambda_1(S^3_R)`, conditional on upstream objects (`docs/COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`).
- CKM atlas and quark staircase: conditional, with supplied identifications (`docs/CKM_ATLAS_AXIOM_CLOSURE_NOTE.md`).
- Koide: open, with many no-gos. **Do not restart** (`docs/lanes/open_science/06_CHARGED_LEPTON_MASS_RETENTION_OPEN_LANE_2026-04-26.md`).
- DM / neutrino lanes: `docs/lanes/open_science/04_NEUTRINO_QUANTITATIVE_OPEN_LANE_2026-04-26.md`. The forecasts lean against the framework under NuFit-6.1 (STATE_OF_THE_THEORY walls).

**(b) Structural problem.** R4 rests on the *legacy* staggered-Cl(3) +
Wilson-SU(3) carrier and imports. None of it is reached from R3 objects built
under the post-2026-06-29 axioms. The lowest R4 obligation is
**OBL-R4.1: obtain any dimensionless ratio from an R3 object that was itself
reached from R2.** The ratio `c_photon / c_fermion` (C2) would be the first.

**(c) Oct 2026 work.** None of it moves R4. The scalar Cassini, lensing and
cosmology notes are conditioned inverse problems on supplied actions, not
predictions.

**(d) Blocking premises.** (I) everywhere; the whole R2→R3 chain is missing beneath it.

---

## Summary: lowest open bridge per rung

| Rung | Lowest open upward bridge |
|---|---|
| R0→R1 | OBL-R0.1: a dynamics (D) from the axioms. A fixed owner-level gap: it needs owner input or an underdetermination witness, not 24h math. Mathematics can map it with no-gos (C4). |
| R1→R2 | OBL-R1.2: a 3D-propagating one-qubit covariant dynamics, at the many-body QCA level (C4). Also OBL-R2.2: phases of covariant formation laws (C3). |
| R2→R3 | OBL-R2.1: a Coulomb (deconfined U(1)) phase in the 3D spin-1/2 link ring model, decided either way (C1). |
| R3→R4 | OBL-R3.1: a common light cone for emergent photon and fermion (C2), with chirality OBL-R3.2 (C5). |
| R4 | OBL-R4.1: any dimensionless ratio from an R2-anchored R3 object. |

---

## Ranked 24h campaign candidates

Each candidate lists: the target statement, the premises it may use, the
closest existing result and what it is missing, the mechanism, the outcome
witnesses, the difficulty, and novelty against standard literature.

### C1 — Decide the Coulomb phase of the 3D spin-1/2 link ring model with unbiased sign-free QMC (R2→R3)
- **Target.** For `H = -g sum_□ (U_□ + U_□^†) + V sum_□ (flippable_□)` on the Gauss-law sector of the supplied cubic spin-1/2 link model, with the repo's staggered background, at `V/g = 0` (pure ring): either (Coulomb) the equal-time transverse E-field structure factor obeys `S_T(q) ~ c|q|` and the static transverse susceptibility is `χ_T(q→0)` finite with a pinch-point form, with the `T→0` energy curvature extrapolating to a finite photon velocity; or (ordered) a plaquette/flippability Bragg peak with weight `O(1)` as `L→∞`. Run the same at `V/g = 0.5` and `0.9` as controls approaching the RK point.
- **Premises.** Supplied link model, Gauss law and background (as in the RING_MODEL notes). No framework adoption.
- **Closest result and gap.** The `docs/RING_MODEL_*` series uses guide-dependent projector MC with an effective population below 25. The 2026-09-03 ladder note already records nonnegative imaginary-time weights. Missing: an **unbiased** estimator.
- **Mechanism.** The ring term is stoquastic for either sign of g, because `U_l → -U_l` via `exp(iπE_l)` gauges a π-flux pattern. The π-flux configuration is consistent on cubic cubes since `6π ≡ 0 mod 2π`. This must be verified for the staggered background. Use a continuous-time worldline / SSE QMC with plaquette-flip vertices at finite β, `L = 4..16`, `β ∝ L^z` with z = 1 and z = 2 tested. Measure `S_T(q, iω_n)`, which gives the photon dispersion from the Matsubara pole without a guide. Ergodicity: the zero-winding sector has frozen flip components. Run in fixed winding sectors and report per-component, or add classical loop updates in the diagonal weight.
- **Witnesses.** Success means a size-converged `S_T(q)/|q|` plateau and a velocity matching the Gaussian comparator within errors, or a converging Bragg weight. Failure means the method fails ergodicity checks against exact L = 2 (9600 states, exact). Inconclusive means `L ≤ 12` cannot separate the `ω~k` and `k^2` regimes.
- **Difficulty.** Medium–high. Novelty: Coulomb phases are established in pyrochlore quantum ice (Hermele–Fisher–Balents PRB 69 064404 (2004); Banerjee et al. PRL 100 047208 (2008); Shannon et al. PRL 108 067204 (2012)) and in the cubic quantum dimer model near and below RK (Sikora et al. PRL 103 247001 (2009); PRB 84 115129 (2011)). The cubic spin-1/2 *link* model with this staggered background is not something I can confirm in the literature. Check before claiming novelty. The method is standard.

### C2 — Common-light-cone underdetermination witness and Chadha–Nielsen flow (R3→R4, Lorentz)
- **Target.** (i) Witness pair: two supplied models, both satisfying Lattice/Qubit/Admissibility (static reading), kinetic isotropy and cubic covariance, with emergent photon velocity `c_γ` and Dirac velocity `c_ψ` such that `c_γ/c_ψ` takes two different values. This shows kinetic isotropy does not imply a common IR light cone. (ii) Theorem: in the coupled IR theory (U(1) + Dirac on a cubic lattice), the one-loop flow of `ln(c_γ/c_ψ)` is attractive to 0 only logarithmically. Give explicit coefficients and the residual at the scale ratio `M_Pl/m_e`.
- **Premises.** Supplied photon comparator (`v = 1.025` in the Gaussian lattice-Maxwell note) and the supplied two-qubit Dirac walk or corner-fermion Hamiltonian. The `kinetic_isotropy_primitive` applies to the regulator.
- **Closest result and gap.** `docs/THE_GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_*` (photon velocity) and `docs/TWO_QUBIT_SITE_UNFREEZES_*` (Dirac speed bound). No note compares them.
- **Mechanism.** (i) Exact dispersion algebra. (ii) Standard one-loop vacuum-polarization and self-energy with independent velocities (Chadha–Nielsen 1983, Nucl. Phys. B217, 125). Then a cubic-lattice correction to dimension-4 LV terms, using Collins et al. PRL 93 191301 (2004) for the fine-tuning issue.
- **Witnesses.** Success: explicit pair plus flow coefficients. This retires "kinetic isotropy ⇒ Lorentz" as a route. Failure: a hidden constraint ties the velocities, e.g. if the photon is built from the same fermion's bilinears. That outcome would itself be interesting.
- **Difficulty.** Low–medium. Novelty: the flow is textbook. The witness under the framework premises is new bookkeeping, not new physics. It is high value because it fixes what R3 must still derive.

### C3 — Covariant-formation trichotomy: iid random order forbids record phases (R1→R2 no-go)
- **Target.** For any finite menu, any translation-covariant nearest-neighbour rule (positive or with zeros), and iid continuous formation times on Z^d, the infinite record law is a finitary factor of iid. Its coding radius R satisfies `P(R ≥ n) ≤ 2d(2d-1)^{n-1}/(n+1)!`. Hence for local observables at distance r, `|Cov(f,g)| ≤ C (2e(2d-1)/r)^{r/2}` (superexponential). There is no long-range order, no criticality and no Coulomb law in any such model. Combined with the level-order ordered phase and the covariance obstruction, this gives: an ordered or critical record phase requires a non-iid (correlated or non-covariant) formation clock.
- **Premises.** `minimal_axioms` plus a supplied (F) of iid clocks. Same as the 2026-09-07 note.
- **Closest result and gap.** `docs/NATIVE_RECORD_SUPPORT_PRESERVING_PRIORITY_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md` (existence via finite ancestors; the mixing corollary is unstated) and `docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_*_2026-09-16.md`. **Caveat:** part (1) is close to a corollary. The added value is the decay rate, the rule-independence, the trichotomy, and the extension to exchangeable, finite-range-correlated or rate-modulated clocks: does mixing survive covariant neighbour-dependent rates (as in `CLOCK_AND_RATE_COVARIANT_EXPONENTIAL_RACES_*_2026-09-22`)?
- **Mechanism.** Disjoint ancestor sets imply independence. Use a union bound over decreasing paths. The hard part is extending to state-dependent rates, by stochastic domination by a rate-λ_max path count.
- **Witnesses.** Success: a theorem plus exact finite checks. Failure: a covariant clock family with correlated rates that produces an ordered phase (a counterexample). Either outcome is decisive.
- **Difficulty.** Low (part 1); medium (rate-dependent extension). Novelty: the Penrose–Sudbury / random-sequential-adsorption methodology is known. The application to record-phase existence is repo-specific.

### C4 — Classify cubic-covariant one-qubit Clifford QCAs on Z^3 (R0/R1→R2 dynamics)
- **Target.** Enumerate all translation-invariant, range-1, proper-cubic-covariant Clifford QCAs on one qubit per site of Z^3, for each soldering action. Represent them as 2×2 symplectic Laurent matrices over `F_2[x^±,y^±,z^±]` à la Haah. Decide: (a) is every such QCA a finite-depth circuit times a shift, and which are trivial? (b) does any one admit a propagating (non-frozen) excitation or glider in 3D? Prediction to test: the many-body analogue of the single-particle freeze holds, i.e. only on-site Cliffords times translations survive under axis or full soldering.
- **Premises.** (D) of QCA type, supplied; (S) from the soldering menu.
- **Closest result and gap.** `docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_*` (single-particle walks only) and `docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_*` (static stabilizer rules). The many-body QCA class is untouched; there are no QCA notes on main.
- **Mechanism.** Covariance restricts the images of X and Z at the origin to O-orbits of Pauli strings on the 27-cell. Symplectic and commutation conditions are finite linear algebra over F_2; enumerate exhaustively. For triviality, use Haah's classification (Clifford QCA: trivial group in 2D, Witt-group-valued in 3D; J. Math. Phys. 2021) and Freedman–Hastings (2020). Check the qubit-per-site count of Haah's nontrivial 3D Clifford QCA example before relying on it (not verified here). The question is whether one qubit per site plus cubic covariance forbids any nontrivial element.
- **Witnesses.** Success: a complete list, plus either a no-go (no propagation) or an explicit propagating covariant QCA. The latter would be a first framework-compatible one-qubit dynamics that moves. Inconclusive: enumeration blow-up beyond range 1.
- **Difficulty.** Medium. Novelty: the covariance-restricted one-qubit classification appears new. The general framework is known.

### C5 — Equivariant three-winding: can cubic-covariant discrete-time walks carry net chirality? (R3 chirality)
- **Target.** For translation-invariant finite-range walks `U: T^3 → U(n)` covariant under `G ⊂ O` with the soldered coin action, compute the attainable values of `W_3[U] = (1/24π^2) ∫ tr (U^{-1}dU)^3`, which equals the net Weyl chirality of the quasienergy bands (Higashikawa–Nakagawa–Ueda, PRL 2019, "Floquet chiral magnetic effect"; discrete time evades Nielsen–Ninomiya). Quick lemma: the Clifford family `U = f + i h·τ + iτ_3 g·σ` of the two-qubit note maps into S^4, and `π_3(S^4) = 0`, so `W_3 = 0` identically. That family can never be chiral. Main question: does any D2-, D3- or D4-covariant one-qubit walk, or any O-covariant two-qubit walk outside the Clifford family, have `W_3 ≠ 0`? Construct one or prove an equivariant obstruction.
- **Premises.** Supplied walk; (S); (C) for n = 4.
- **Closest result and gap.** `docs/CUBIC_COVARIANCE_FREEZES_*` item 4 ("every moving walk found has three-winding zero"; this is a search, not a theorem) and `docs/TWO_QUBIT_SITE_UNFREEZES_*`.
- **Mechanism.** Equivariant degree theory. Proper rotations preserve orientation and conjugation preserves `W_3`, so there is no obvious constraint. Then constructive search over Laurent-polynomial unitaries, e.g. products of conditional shifts with non-commuting coins, and exact `W_3` by lattice integration with a certificate (integer rounding plus a gap bound).
- **Witnesses.** Success: an explicit covariant walk with `W_3 = ±1`, giving a single net Weyl node (a chiral fermion candidate), or an obstruction theorem. Failure: inconclusive search.
- **Difficulty.** Medium. Novelty: Floquet NN evasion is known. The cubic-equivariant, one-qubit version appears new.

### C6 — Stability of the emergent-fermion Z2 phase in infinite volume, and its no-photon corollary (R1→R2)
- **Target.** For the twisted BKSF / corner-fermion stabilizer codes, verify the TQO-1/TQO-2 conditions. Apply Bravyi–Hastings–Michalakis (J. Math. Phys. 51 093512, 2010) for a uniform gap and a stable fermionic point charge under every small, cubic-covariant, finite-range perturbation, uniformly in L. Corollary no-go: such a phase has no gapless excitation, so neither a photon nor a massless fermion arises without leaving the phase. This retires "Z2 code ⇒ QED" routes.
- **Closest result and gap.** `docs/BKSF_CUBIC_FERMION_CODES_*`, `docs/CORNER_FERMION_*`, `docs/MAJORANA_PER_DIRECTION_*` (all 2026-10-17). All are finite-torus code dimensions only.
- **Mechanism.** Local-indistinguishability checks are finite stabilizer computations. Fracton-type codes such as Chamon need care.
- **Difficulty.** Low–medium. Novelty: low (BHM is textbook). Value: the first R2 stability statement for the fermion lane.

### C7 — Massive continuum limit of the 3D two-qubit Dirac walk (R2→R3)
- **Target.** Under the scaling `m a → 0` at fixed m, the rescaled walk group converges strongly to the free massive 3+1D Dirac Poincaré representation on the doubler-free sector. The axis doublers stay at quasienergy ~π/a and decouple. Error rates must be explicit.
- **Closest result and gap.** The 1D analogue is `docs/GAPPED_CONTINUUM_LIMIT_*`. The 3D walk is `docs/TWO_QUBIT_SITE_UNFREEZES_*`, which notes the doublers become massless π-modes in the light-like regime. That must be quantified.
- **Difficulty.** Medium. Novelty: low. Dirac QCA limits are known (Bisio–D'Ariano–Tosini, Ann. Phys. 2015; D'Ariano–Perinotti PRA 90 062106, 2014; Arrighi et al.). Value: the first 3+1D R3 object under the framework's carriers.

### C8 — Lattice Sakharov coefficient for a supplied Dirac walk and an `a/l_P` test (R3→R4)
- **Target.** Compute exactly the induced `1/(16πG)` coefficient (the second spatial-momentum moment of the vacuum response to a slowly varying lapse or spatial metric) for the two-qubit Dirac walk under a declared metric coupling. Report `a/l_P` per species with `N_f` left symbolic.
- **Closest result and gap.** `docs/UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17.md`. It imports the heat kernel and the cutoff; this candidate replaces those with an exact lattice sum.
- **Risk.** The metric coupling is itself a supplied premise. It must be declared in advance with no tuning (rule §2.4). Difficulty: medium–high. Rank last.

**Not recommended for the 24h campaign:** Koide (do-not-restart); the
`alpha_LM^16` hierarchy (regulator-dependence no-go already on record);
further clock/controller/scalar-inverse densification, which does not move
any bridge.

## Recommended order
C1 (decisive R2→R3), C4 (lowest R1→R2, many-body freeze or escape), C3
(fast no-go), C2 (fast Lorentz witness), C5, C6, C7, C8. C2, C3 and C6 are
suitable as parallel low-cost workers alongside C1/C4.
