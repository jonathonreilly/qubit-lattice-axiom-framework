## **Searches run.**

- Initial terms: `quantum link`, `Kogut`, `transfer matrix`, `toric code`, `D-theory`, `T0-start`, `3.1:thm-main`.
- Directories: `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104`.
- Follow-ups: `Creutz`, `Clifford Z2`, `Wilson`, `Gauss`, `finite clock`, `Peter–Weyl`, `G1`, and named source files.
- Read `ref/README.md` first. It identifies consolidation notes and ledger locations: lines 2–5, “Ledger rows: main/docs/audit/data/ledger/” and “Each has a *CONSOLIDATED* note.”
- `briefs/GB1.txt` was absent. The advertised CA full `index.tsv` was also absent. CA-I coverage below uses local maps, ports, and quoted statements. The index README cautions: “This index reads; it proves nothing” (`Y/library/sa-index/ca-full/README.md:5`).

Path abbreviations used below:

- `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`
- `Y` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030`
- `D` = `ref/main/docs`
- `C` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`
- `P35` = `ref/pr10135/docs`

## **Already in the repo.**

- **Finite-group links and the continuous-group obstruction.** The frozen GA2 note supplies a finite-group starting point: “entrywise-commuting unitary link with covariance at both ends” on \(L^2(K)\) (`T/GA2_Y2.md:47`, Theorem 2.3). For a nontrivial infinitesimal representation, a finite register has “no invertible covariant link” (`T/GA2_Y2.md:41`). Status: “FROZEN” (`:5`); its proofs are “author checks, not independent review” (`:14`). Its scope explicitly leaves invariant comparisons open: “does not exclude an identification of gauge-invariant correlators” (`:67`).

- **A supplied rung-2 Z₂ model.** The consolidation records commuting star and face operators: “All terms commute,” with torus code dimension “log2 = 3” (`C:789`, #10021). Its energies are supplied: “would have to come from the update rule, which is not shown” (`C:808`). Consolidation status is “author statements for review” (`C:11`).

- **A moving Z₂ tick on larger blocks.** Logged #10037 supplies two tilings of \(4^3\) blocks. It records “every P commutes with every G (any angle)” and finite-tableau conservation of all 128 stars. Scope remains narrow: “Not shown: a photon, deconfinement, a U(1) dynamics” (`C:1201`, status “logged”).

- **Rishon Gauss laws.** #9926 gives finite U(1) quantum links, a gauge-invariant dressed hop, and an eight-rishon plaquette. The raiser is “nilpotent … not unitary” (`C:263`); the plaquette commutes with “all corner numbers” (`C:266`). SU(3) requires the specified colour construction and determinant term (`C:267`). These results are conditional on “supplied role assignment” and “supplied couplings” (`C:259`); “No … continuum limit is derived” (`C:252`).

- **Five-mode laws already carry exact SU(2) subgroups.** “Every closed subgroup, in particular the Standard Model SU(2), has the restricted Gauss law at every angle” (`T/LW1_5.md:149`). The same passage preserves extra link blocks and the full gauge group. It states: “A pure SU(2) Yang–Mills limit is not established.” Status: “FROZEN” (`:5`). Magnetic dynamics remain conditional: “a plaquette class and its constants are OPEN law data” (`:104`).

- **Gauge-invariant magnetic layers and compilation.** GA1 proves that every ordered closed-walk operator “is gauge invariant” and that its proposed class defines “cell-covariant quasi-local automorphisms” (`T/GA1_5.md:85`). Under NN-a, every class member has finite nearest-neighbour depth (`:264`, Proposition C). Status: frozen, with compilation listed among “Referee closures, unrefereed” (`:5,11`). The magnetic symbol has a Yang–Mills quadratic form, but “The electric energy and a physical continuum limit are not derived” (`:13`).

- **Propagation is available without a gauge-boson identification.** The latest GA15PHI amendment covers every \(1\le m\le9\), under its proposed class and repaired dependencies. It says “the band is a conjugated neutral mode” (`T/GA15PHI.md:7`). The frozen statement calls it “not an identified photon or a Clifford cone” (`:5`). R-Φ is “not invariant under these admissible conjugations” (`:121`).

- **Exact local U(1) matter–electric–magnetic dynamics.** A supplied square with four spin-one links has separately Gauss-preserving generators and an exact joint exponential conserving the complete Hamiltonian (`D/U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md:37–50`, “complete matter-electric-magnetic Hamiltonian”). This is a one-face, supplied-model result (`:518`). Ledger status is `"effective_status": "unaudited"` (`D/audit/data/ledger/u1/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_bounded_theorem_note_2026-09-03.json:34`).

- **Finite clocks supply modular gauge dynamics.** The finite-clock note supplies an exact Weyl-clock Hamiltonian whose components preserve modular Gauss generators (`D/U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:43–64`, “all modular Gauss generators”). Additive Gauss law requires that the residual “cannot wrap” (`:83`). Ledger status is `"effective_status": "unaudited"` (`D/audit/data/ledger/u1/u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03.json:34`).

- **Wilson transfer machinery exists on supplied carriers.** For any compact group, the temporal-gauge mixed kernel “factorizes exactly as a tensor product” of one-link convolutions (`D/GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md:6–15`). SU(3) Wilson character coefficients are nonnegative for every \(\beta\ge0\) (`D/WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md:190`, “every irrep lambda and every beta >= 0”). Both ledger rows remain `"audit_status": "unaudited"` (`D/audit/data/ledger/ga/gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10.json:6`; `D/audit/data/ledger/wi/wilson_su3_gauge_transfer_kernel_positivity_bounded_note_2026-05-30.json:6`).

- **Full physical-cube transfer and Hamiltonian limit.** The supplied twelve-link SU(3) cube has an “exact onto isometry” to five loop variables with simultaneous conjugation (`D/GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md:37–39`). Its positive transfer preserves the physical space (`:43`). Under supplied anisotropic scaling, transfer products converge strongly to the compact interacting Hamiltonian semigroup, with an energy-cutoff rate (`D/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md:114`, “strong convergence for every vector”). Physical time is not selected (`:122`). Both ledger effective statuses are `"unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_full_cube_physical_transfer_geometry_bounded_theorem_note_2026-09-07.json:30`; `D/audit/data/ledger/ga/gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07.json:29`).

- **Peter–Weyl approximation has energy-priced bounds.** Complete-irrep compression preserves endpoint covariance (`D/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md:44–48`, “Gauge covariance remains exact”). Its high-energy defect has norm one (`:60`), while the state error decreases for “uniformly bounded electric energy” (`:77`). The companion local-observable theorem chooses spatial radius first, then representation cutoff; “No claim of a uniform all-energy fixed-R approximation follows” (`D/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75`). Both ledger effective statuses are `"unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_pw_compression_shell_and_energy_path_bounds_bounded_theorem_note_2026-09-07.json:29`; `D/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`).

- **A nearby truncated SU(2)/SU(3) programme exists.** MDTN uses finite Peter–Weyl link spaces and a supplied Hamiltonian. Its claimed gap concerns “Fixed-lattice … finite-truncation … at strong coupling” (`P35/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md:5–8`). Status is “proposed (unaudited)” (`:14`). The BHM-dependent gap step remains an “open obligation” (`:31–32`). The embedding separately names Hamiltonian and block-encoding bridges (`P35/QUBIT_LATTICE_GAUGE_MDTN_EMBEDDING_OUTLINE_NOTE_2026-10-31.md:10–11`).

- **CA-I and T0 have different scopes.** The local CA map lists first-passage flow, exact representation/stability, correlation bounds, subsequential limits, and witness clauses (`Y/library/chain-ca.md:30–39`). Its status account quotes: “No clause … is proved outright” (`Y/library/ro1-vs-ca.md:10`). CA’s continuum clause does not assert clustering, unique vacuum, Wightman functions, or full O(4) (`Y/library/t0-tree.md:13`, “CA does not assert”). T0 additionally requires those properties, NT1 dynamics, and NT2 agreement across scales (`Y/GOAL.md:22,30–31`). Current standing: “T0 remains open” (`Y/library/t0-tree.md:8`).

- **Fixed-lattice SU(2) reflection positivity is a reusable YM result.** LG1 Theorem 10 states that every periodic Wilson DLR state at \(\beta>0\) is “invariant and reflection positive at every admissible mirror” (`Y/library/lg1.md:365`). It also supplies signed-permutation symmetry. Latest status: “Status: frozen” (`:485`). This statement starts from Wilson DLR data; it does not supply the framework-to-Wilson identification.

## **Failed attempts on file.**

- **The old full-algebra zoom fails at exact Gauss-generator identification.** The trace/locality theorem forces \(L=1\) (`T/ZM1I1A.md:44`). The recorded failing requirement is “the exact generator identity (G1)” (`:50`). The owner’s replacement imposes “no map on charged fields or Gauss generators” (`T/TOE_ASSEMBLY.md:252`).

- **The broad finite-register exclusion overreached its proof.** The frozen correction limits Y2-0 to specified covariant link and generator identifications. It explicitly preserves “gauge-invariant correlators” and “group-valued Euclidean integration variables” (`T/GA2_Y2.md:67`).

- **Finite-list moment matching did not establish GA2.** The failing step is promoting one-scale agreement to control of all observables, scales, and errors: “moment agreement for finitely many observables at one scale does not control” them (`T/GA2_Y2.md:16`).

- **Three small-coupling-window arguments failed.** Cube products raise no end-number grading. Small angle ratios do not remove the fine-link bounds. Aligned block states were assumed rather than supplied. The note calls these “failures of particular arguments, not proofs that a window is absent” (`T/GA2_Y2.md:168`).

- **Rung-2 gauge energies did not follow from the original cube tick.** The logged analysis says “No star, plaquette or ice energy follows from the tick” (`C:1198`, #10024). Its small-cube preservation condition freezes local Pauli variables. The larger-block route is separately logged, rather than erased by that failure (`C:1201`, “on 4^3 blocks no edge or face site is forced in both tilings”).

- **Bare small-register coefficients missed the harmonic light cone.** The consolidation records that “bare coefficients miss the light cone at small registers”; dressed coefficients “are not established” (`C:21`, #9968). This was a supplied single-loop diagnostic.

- **A split tick did not conserve the simple summed Hamiltonian exactly.** The local U(1) note records “simple-H drift is O(h^3)” and Floquet interactions at “O(h^2)” (`D/U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md:360–361`).

- **Compressed source transfer did not automatically compose.** The full-cube correction states that \((I^*TI)^n\) inserts \(II^*\) and “need not equal I* T^n I” (`D/GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md:51`).

- **D-theory did not supply the present 3+1 bridge.** The repository literature digest records that reducing three spatial directions plus time “would leave three Euclidean dimensions” (`T/LIT_QLM.md:15`). Its general finding is “None … supplies T0-start or T0-rate” for the fixed-register law without an extra dimension (`:3`). These are reported source limits, not an impossibility theorem.

## **Overlap with this lane’s results.**

not run.

`T/TOE_ASSEMBLY.md:441`: “New 2026-11-07. Skeleton only.”

## **Missed inputs.**

- **Use the invariant-algebra owner decision first.** GB1 should test its actual map requirement, rather than restore the failed G1 requirement. The owner retained a “unital injective *-homomorphism” on invariant algebras and imposed “no map on charged fields or Gauss generators” (`T/TOE_ASSEMBLY.md:252`).

- **Use the finite-group construction and logged Z₂ ticks for the first rung.** They provide explicit carriers, Gauss operators, and candidate schedules. They do not supply GB1’s readout map. Relevant inputs are “covariance at both ends” (`T/GA2_Y2.md:47`) and “every P commutes with every G” (`C:1201`).

- **Reuse the U(1) layer and Wilson-transfer dictionaries with their schedule limits.** This would make electric, magnetic, and transfer operators explicit. Preserve “simple-H drift” (`D/U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md:360`) and the full-boundary requirement “no reset of omitted spectator modes” (`D/GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md:51`).

- **Use Peter–Weyl bounds only after identifying the regulator and state.** They offer an approximation route with priced energy and preparation. They do not identify the fixed rishon register. The local theorem retains “success probability and preparation … an explicit resource premise” (`D/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:73`).

- **Use the current YM contract, rather than treating exact SU(2) symmetry as sufficient.** The requested handoff still needs an admissible start, quantitative errors, and extensions for the actual groups. “These are requests, not established branch results” (`T/GA2_Y2.md:176`).

## **Consumers.**

- **GA2, Y1:** needs a local gauge-invariant Euclidean representation, “reflection positive in time” (`T/TOE_ASSEMBLY.md:603`). A named Hamiltonian and unitary tick alone do not state this required interface.

- **GA2, Y2 and GB1-H:** need the actual action inside the admitted RG domain, or a proved extension of that domain. “T0 is stated for the Wilson action” (`T/TOE_ASSEMBLY.md:604`). GB1-H explicitly asks which CA-I hypotheses the bridge “delivers and which it cannot” (`:443`).

- **YM fixed-lattice positivity inputs:** the weakest existing supplier starts from Wilson measure, normalized Haar links, and specified lattice mirrors (`Y/library/port/p8-positivity.md:31–49`, “finite-lattice reflection positivity”). LG1 accepts periodic Wilson DLR states (`Y/library/lg1.md:365`). GB1 must identify those data before transferring these statements.

- **ST1 route B:** needs reflection positivity of the “Euclidean tick transfer” (`T/TOE_ASSEMBLY.md:590`). This is weaker than full continuum Yang–Mills construction.

- **LZ1:** needs the gauge-sector symmetry bridge, followed by O(4) restoration and reconstruction. The outstanding lattice mismatch is “no lattice symmetry exchanging time and space” (`T/TOE_ASSEMBLY.md:605`).

- **GA2’s quantitative clause, then EW1, FL2, and CS1:** needs controlled correlator and running-coupling errors. Y5 asks for “O((a/r)^p)” (`T/TOE_ASSEMBLY.md:607`); the downstream consumers are named at `:590`. `T0-rate` remains a request (`T/GA2_Y2.md:176`).

- **The matter extension of GA2:** needs a local gauged chiral-matter measure and RG control. The weakest named entry is “CH1-ii (a local gauged measure)” (`T/TOE_ASSEMBLY.md:606`). Pure-gauge GB1 statements would leave this separate obligation open.