## **Searches run.**

- Initial terms: `quantum.link`, `large.spin`, `QLR`, `rotor`. Follow-ups: `GB1QL`, `T0-QLR`, `Peter.Weyl`, `restricted.flux`, `large.register`, `Lieb.Robinson`, `rishon.*limit`, `truncat`.
- Directories: `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104`. Follow-ups inspected consolidation notes, ledger rows, drafts, referee reports, `LIT_QLM.md`, and `briefs/GB1QL.txt`.
- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” and says each consolidation PR has “a *CONSOLIDATED* note” (`ref/README.md:2–3`).

Path abbreviations:

- `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`
- `D` = `ref/main/docs`
- `Y` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030`
- `C` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`
- `P` = `D/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`
- `S` = `D/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md`
- `H` = `D/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md`

The lane’s target is an SU(2) correlator comparison with a rate “uniform in the volume for local observables” and in ticks “up to a stated time,” followed by an explicit T0-start handoff (`briefs/GB1QL.txt:1`).

## **Already in the repo.**

- **A finite-box U(1) register-limit bound.** GB1 Theorem 5.2 compares normalized spin links with bilateral shifts. It assumes integer spin, empty matter, bounded initial flux, and the same cube-face magnetic and electric terms (`T/GB1.md:107`, “On a fixed finite box”). Its rate is `O((log S)^4/S^2)` for fixed box, ticks, flux bound, and magnetic angle (`:111`, “For fixed box”). The referee records the repaired leakage estimate (`T/GB1_REFEREE.md:117`, “with the leak closure”). Status: frozen; the note explicitly says these are “not retained-status audit results” (`T/GB1.md:5,9`).

- **Exact quantum-link sectors inside the named law.** Theorem 5U supplies spin-1/2 U(1) inside `L5-U[m]` for odd `m`, including its fermion at `m=1` (`T/GB1.md:177,182`, “at sector level”). Theorem 6.1 supplies a frozen-spectator, empty-matter block with equality of integer-time expectations (`:121–123`). Its target is the “specified Trotterized U(2) rishon quantum-link model with cube faces,” not an established pure SU(2) Wilson theory (`:123`). The referee preserves that scope: “restricted-subgroup invariants” (`T/GB1_REFEREE.md:123`). Status: frozen, with the audit limitation above.

- **Exact-link and readout obstructions, with approximation routes left open.** GA2 Theorem N excludes an invertible link covariant under a nontrivial bounded infinitesimal generator (`T/GA2_Y2.md:39–43`, “no invertible covariant link”). GB1 Corollary R1 excludes the specified uniformly exponentially local invariant-algebra readout from infinite compact-group links (`T/GB1.md:93`, “at every finite zoom rung”). Its scope expressly preserves “an approximate low-flux dictionary” and “a finite truncation” (`:97`). GA2 is frozen (`T/GA2_Y2.md:5`, “FINISH: FROZEN”).

- **A local-observable approximation already uniform in ambient volume.** `P` treats a supplied cubic SU(3) Hamiltonian with nonlinear plaquettes and boundary charge sectors (`P:30`, “supplied cubic SU3 Hamiltonian”). It combines a spatial locality tail with a finite-energy Peter–Weyl cutoff estimate, uniformly for `|t|≤T` (`P:52–75`). The conclusion is “independent of total lattice size” (`P:75`). Preparation probability remains explicit (`P:73`, “an explicit resource premise”). This is a Wilson/Peter–Weyl carrier, not an identified rishon realization (`P:35,63`). Ledger status: `"effective_status": "unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`).

- **Energy-priced transporter compression.** Complete-irrep SU(3) Haar compression preserves exact gauge covariance (`S:48`, “Gauge covariance remains exact”). For distinct-link paths, a total electric-energy budget gives error at most `sqrt(E/g_(R−1))` (`S:98`, “TOTAL path electric-energy budget”). Its high-shell defect still has norm one (`S:64`, “||D_R||=1”). Scope excludes an automatic transfer of unbounded kinetic-energy estimates (`S:108`, “requires an additional energy-form estimate”). Ledger status: `"effective_status": "unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_pw_compression_shell_and_energy_path_bounds_bounded_theorem_note_2026-09-07.json:29`). Broader negative certification is “DEFERRED” (`S:24`).

- **A supplied Wilson-to-Hamiltonian bridge.** The full twelve-link SU(3) cube has a positive normalized Wilson transfer and a compact interacting Hamiltonian (`H:30–42`, “positive self-adjoint contraction”). Transfer products converge strongly, with right-input energy-cutoff error `C t²(1+E²)/n` (`H:114`, “strong convergence for every vector”). The theorem does not take an infinite-volume limit or select a physical clock (`H:122`, “does not select a physical clock”). Ledger status: `"effective_status": "unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07.json:29`).

- **Large-copy kinematics, without dynamical convergence.** GA2 Theorem 3.5 divides centered second moments and commutators by the copy number and gives coherences `k/(k+5)` and `k/(k+9)` in specified product states (`T/GA2_Y2.md:101`, “For independent copies”). The tensor-power `L5-U[ρ]` calculation is “not an adopted change of law” (`:105`). The note explicitly withholds a continuum or GA2 error conclusion (`:107`, “not a proof of a classical phase”).

- **Earlier supplied rishon and magnetic constructions.** Consolidated #9926 records exact U(1) and SU(3) Gauss laws, dressed hops, and plaquettes. Its spin-1/2 raiser is “nilpotent … not unitary” (`C:263`); the SU(3) determinant breaks the extra U(1) (`C:267`). Its role assignment, spin, and couplings are supplied (`C:259`). Consolidated #9968 records a classical Maxwell/Yang–Mills quadratic limit, while “the dressed coefficients are not established” (`C:21`). Consolidation status is “author statements for review” (`C:11`).

- **A nearby SU(2) Peter–Weyl regulator.** The MDTN note uses `j_max=1/2`, with five states per SU(2) link (`ref/pr10135/docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md:57–60`, “dim H_ℓ = 1 + 4 = 5”). Its scope is fixed-lattice, finite-truncation, strong coupling (`:5–8`). Status is “proposed (unaudited)” (`:14`); the BHM-dependent gap step remains an “open obligation” (`:31–32`). It supplies no growing-register comparison.

- **A repository literature map already separates the relevant limits.** `LIT_QLM.md` records exact coherent-state ingredients followed by a semiclassical expansion without “uniform remainder bounds” (`T/LIT_QLM.md:33`). Many-rishon flavor number is “neither the repo’s occupancy m nor a ZM1 block size” (`:45`). Its Tong summary records rigorous U(1)/SU(2) truncation theorems, but “No equality between those truncations is supplied” for the repo’s rishon regulator (`:83–85`). These are recorded literature findings, not native GB1QL results (`:3`, “No citation here discharges a repo proof obligation”).

## **Failed attempts on file.**

- **Uniform operator-norm convergence.** The top-flux state is killed by the finite raising operator but moved by the bilateral shift. The failing step is already explicit: “uniform operator-norm convergence fails” (`T/GB1.md:115`).

- **Extending the U(1) bound without repairing leakage.** The referee rejected treating truncated exponential series as contractions: “The truncated series is not a contraction” (`T/GB1_REFEREE.md:221`). The frozen proof instead obtains leakage from unitary gates (`T/GB1.md:113`, “Telescoping unitary-gate compressions”).

- **Treating the SU(2) block as autonomous on every matter-empty state.** Repaired SU2-B constructs states agreeing on the block but disagreeing after evolution. Its conclusion is “no map β” reproduces the full evolution for all such states (`T/GB1.md:129`). Frozen spectators remain essential.

- **Growing the register inside the existing fixed `L5-U[m]` law.** The U(1) family “does not fit inside one named law, because m is fixed” (`T/GB1.md:182`). GA2 likewise distinguishes available large-representation data from “the fixed L5-U rishon construction” (`T/GA2_Y2.md:161`).

- **Replacing the cube-face interaction with the full plaquette sum.** The existing Hamiltonian contains “half the plaquettes in each plane” (`T/GB1.md:105`). Mixed plaquettes share links and need not commute. GB1-CF remains open at that scheduling/construction step (`:105`, “whether another allowed member yields the full sum”).

- **Copying the frozen-sector route to `L5-O`.** Empty matter fails at the matter hop. Matching matter and rishon occupations fails when block plaquettes change those occupations. Filled matter fails by transfer into empty rishon ends (`T/GB1.md:159`, “fails first at the matter layer”).

- **Inferring a small-coupling window from simple diagnostics.** The three recorded failures are a U(1)-blind cube product, angle tuning that does not remove kinematic bounds, and assumed block alignment (`T/GA2_Y2.md:170`, “failures of particular arguments”). Promoting finite-list, one-scale matching to GA2 also fails: it “does not control the other observables, scales, or errors” (`:18`).

- **Discarding boundary Gauss sectors during local truncation.** A valid global Wilson-loop state has no support on the local singlet. Forced local zero-charge projection discards it “with probability1” (`P:81`).

- **Using D-theory reduction directly for the present dimensional target.** The recorded reduction of three spatial directions plus time “would leave three Euclidean dimensions” (`T/LIT_QLM.md:15`). This is a failure of that specified route, not a general quantum-link exclusion.

## **Overlap with this lane’s results.**

not run

## **Missed inputs.**

- **Use the local Peter–Weyl theorem as the closest quantitative template.** It already separates spatial locality from register cutoff and states the order: “First choose r … then choose R” (`P:75`). It would supply a model for the requested volume-independent local estimate. The missing step is identifying an admissible SU(2) five-mode regulator with the compared Hamiltonians.

- **Specify the growing representation family before claiming a limit.** `L5-U[ρ]` is only a “Recorded alternative”; its complete-law Gauss calculation still “must be checked” (`T/GA2_Y2.md:166`). The literature map also warns that block tensor products do not automatically select the required constrained irrep or aligned state (`T/LIT_QLM.md:45`, “does not automatically select”).

- **Keep the U(2)-to-SU(2) step explicit.** The existing sector target is U(2) (`T/GB1.md:123`, “U(2) rishon quantum-link model”). The recorded determinant mechanism “changes the gauge symmetry” (`T/LIT_QLM.md:23`). It is an additional construction obligation.

- **Price locality and time errors uniformly along the family.** The repository’s general walk bound requires “a finite uniform J_*” (`D/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md:4,87–89`). The finite-box register bound separately says “cutoff, time and volume are essential” (`T/GB1.md:115`). These inputs would prevent pointwise finite-register estimates from being reported as a uniform family theorem.

- **Supply the state comparison and observable dictionary.** GB1 does not show that “the VC1 vacuum belongs to” the frozen class (`T/GB1.md:147`). ZM1’s observable note says GA2 and T0-rate need an “independently fixed operator-to-continuum dictionary and rates” (`T/ZM1_OBS.md:218`). A theorem on prepared finite-energy states would therefore retain a separate vacuum handoff.

## **Consumers.**

- **GB1-QL itself:** needs a named SU(2) realization, state class, local correlator dictionary, and error uniform in ambient volume and ticks through a stated time. The brief explicitly permits recording “the first step that fails” (`briefs/GB1QL.txt:1`).

- **GA2 Y2 and ZM1-G:** need controlled invariant-correlator comparison to a “reflection-positive group-valued measure in the relevant RG class” (`T/GA2_Y2.md:178`). A finite-time Hamiltonian comparison supplies a regulator-error component; RG-class membership remains separately requested there.

- **YM T0-start and T0-rate:** need admissible small-coupling starts with scale-uniform CT1–CT4 bounds (`T/GA2_Y2.md:178`, “uniformly in the start”). The existing YM interface includes complex-source bounds and a partition-function volume bound (`Y/GOAL.md:70–71`); “All constants are independent of a and L” (`:73`). Local real-time convergence alone does not state those interfaces.

- **GB1-H, Y1, and Y3:** need the Wilson/Euclidean identification, reflection positivity, and lattice symmetry hypotheses. GB1 marks these “Not delivered” (`T/GB1.md:207–209`). Its finite tick does not select its imaginary-time correlators (`:43`, “The tick alone does not select this logarithm”).

- **GA2’s downstream consumers:** LZ1 needs O(4) restoration and reconstruction; ST1 route B needs reflection positivity; EW1 and FL2 need running-coupling control. These dependencies are explicit (`T/TOE_ASSEMBLY.md:600`, “Through GA2 it also feeds”). The quantitative GA2 interface asks for errors `O((a/r)^p)` (`:619`, “Y5, convergence rate”). The YM target remains open: “A frozen implication is not an established actual-construction input” (`Y/library/t0-tree.md:8`).