**Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” and says each consolidation PR has “a *CONSOLIDATED* note” (`ref/README.md:2–3`).
- Initial terms: `spinor`, `straight-string`, `Clifford`, `Fredenhagen`, `deconfinement`, `fractionalisation`, `toric`, `Gauss dressing`, `RC-W`, `RCSPO`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- Follow-up terms: `deconfined spinon`, `Buchholz`, `Senthil`, `Levin`, `Naaijkens`, `boundary label`, `self-adjoint unitary`, `charged sector`, `chiral matter`. Read relevant consolidation sections, ledger rows, TOE statements, drafts, referee passages and `LIT_QLM.md`. Broad inventories were narrowed before substantive line reads.
- The brief requests “spinor-class straight-string sectors” on `L5-O`, with “a Clifford node” and a decision about RC-W (`briefs/RCSPO.txt:1`). The assembly keeps both laws live and the charged prescription provisional: “keep both live” and “It is not adopted” (`T/TOE_ASSEMBLY.md:214,225`).
- Paths below: `T/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`; `M/` = `ref/main/docs/`; `L/` = `ref/main/docs/audit/data/ledger/`; `G` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.

**Already in the repo.**

- **The requested boundary label already has an obstruction on `L5-O[S_+]`.** CG16D Theorem 4 states that every finite-region spinor flux is the identity. Consequently, “every representation has `χ_sp=+1`” (`T/CG16D.md:45`). CG16B separately states that R-16^str′’s boundary label on this law “is `+1`” (`T/CG16B.md:182`). This concerns the proposed boundary-flux identification. CG16D explicitly leaves its physical scope open: “No physical identification shows that the proposed flux label exhausts every possible meaning of the CG1 16” (`T/CG16D.md:9`).

- **Changing the Spin(20) representation does not automatically remove link purity.** For any Spin(20) register, the endpoint kernel actions coincide, “so `d_ℓ=1`” (`T/CG16D.md:41`). On link-pure registers, relative negative flux class consists of finite odd centre differences (`T/CG16D.md:55`: “`D(κ)` finite and odd”). Over an even-translation-invariant flux-sharp background, every band in the stated negative-class representation satisfies “`V=1` on a neighbourhood of each node” (`T/CG16D.md:63`). These are frozen conditional results; imported closures remain “unrefereed” (`T/CG16D.md:5`).

- **The L5-O raising obstruction is absent, but the complete strings remain nonunitary.** Each individual `S_+` link factor “is a self-adjoint unitary” (`T/RCS1.md:197`). The referee therefore finds that “no bounded observable is raised by a link factor”; Lemma 5, Theorem 7 and Proposition 9 do not transfer as proved (`T/RCSPC_REFEREE.md:621–623`). However, the contracted string operator itself is not a unitary or isometry: “neither … is a scalar multiple of a unitary” (`T/RCS1.md:195`). Unitary link entries do not supply an automorphism-valued string construction.

- **Local-centre spinor charge is already static.** LW1_5’s Theorem SC conserves the changed centre pattern: “A spinor-class charge does not move” (`T/LW1_5.md:198`). Its conclusion uses the local-centre definition. The file distinguishes another possible CG1 identification: “Whether CG1’s ‘16’ needs a different notion … is … an owner question” (`T/LW1_5.md:204`). LW1_5 is “FROZEN” (`T/LW1_5.md:5`).

- **The older finite-site composite obstruction has a narrower domain.** Consolidated #10027 treats fixed finite sets of five-mode sites with site-bilinear Spin(10), at arbitrary invariant interaction strength. Its odd excitations are “in the vector class … never a spinor 16” (`G:987`). The scope explicitly excludes infinite-volume superselection sectors: “infinite-volume superselection sectors are outside it” (`G:979`). Consolidation standing is author-side: “These are author statements for review” (`G:11`).

- **Relative oddness is defined independently of spinor flux.** RCS1 defines `χ_tot` through strong convergence of background-normalized matter parity, along finite sets “ordered by inclusion” (`T/RCS1.md:165`). It agrees with the field-GNS odd grading on its stated domain (`T/RCS1.md:171`: “`χ_tot=−1` … of `H_odd`”). An arbitrary representation of the observable algebra has “no intrinsic odd subspace” (`T/RCS1.md:18`). Thus oddness and the requested Spin(10) boundary label are separate obligations.

- **The reusable no-node theorem allows the tick to move labels.** RCSPC Theorem 1 applies to separable covariant label structures with finitely many translation orbits and tick-permuted blocks (`T/RCSPC.md:51–55`: “finitely many orbits”). If every stabilizer has rank at most two, “no band has a Clifford node” (`T/RCSPC.md:67`). For covariantly chosen factor ray sectors, a Clifford node requires quasi-equivalence across “a subgroup of finite index in `Z³`” (`T/RCSPC.md:97`). Tick conservation of each ray label is not required by this theorem.

- **The bounded-rishon obstruction is established on named carriers.** Lemma 5 empties the background’s lowest occupied target-number level on every ray link (`T/RCSPC.md:168`: “the lowest level is emptied”). Corrected Theorem 7 gives disjoint distant rays for cell-invariant finite-block products; factor sectors then admit no Clifford node (`T/RCSPC.md:178`: “no update gives a Clifford node”). Proposition 9 derives a necessary cone-lift condition for factor sectors on the witness (`T/RCSPC.md:194`: “cone lift is necessary”). The extension to L5-U is recorded separately (`T/RCSPC.md:336–338`: “Theorem 7 … and Proposition 9 follow on `L5-U[m]`”). These statements do not establish the corresponding L5-O mechanism.

- **Longitudinal charged motion already exists on the alternative rishon witness.** RCSP16 constructs `V(K)=e^{iK₁}`, a node plane and `N=(−1,0,0)` (`T/RCSP16.md:80`). Its sectors have relative parity and boundary label `−1`, conditional on R-16^str′. It is not a three-direction cone: “No one-dimensional band has a three-dimensional Clifford cone” (`T/RCSP16.md:86`). The file expressly supplies no “irreducible 16, particle statistics, energy bound, VC1 vacuum identification, or chiral Weyl particle” (`T/RCSP16.md:11`).

- **Fluctuating loops have been constructed without hiding the ray.** RCSPC’s four backgrounds, including `Ψ_λ`, admit no Clifford-node band for any update for which the background is D1 (`T/RCSPC.md:160`: “matter-activated or not”). This extends the earlier matter-activated obstruction without extending its transverse-flatness conclusion (`T/RCSPC.md:164`: “its transverse-flatness clause is not extended”). RCSPC is frozen, but “No Clifford node is constructed” and “formal retained status remains separate” (`T/RCSPC.md:3`).

- **D-reg provides transfer and string defects, but its existing defects also have a no-node result.** Its invariant transfer makes boundary flux “not central in `𝔄^G`” (`T/CG16D.md:105`). Theorem 9 constructs a columnar D1 state and half-column string limit with “`χ_sp=−1`” (`T/CG16D.md:132`). RCSPC Corollary 10 excludes Clifford nodes on those defect sectors “for every update in LZ1’s class” (`T/RCSPC.md:282`). The `χ_sp`-to-`χ_tot` bridge remains open (`T/RCSPC.md:3`: “the `χ_sp`-to-`χ_tot` bridge on D-reg”).

- **RC-W is a scoped winding theorem.** For a translation-covariant finite-component walk that is a finite product of bounded-block layers, RC-W gives “`W₃[V]=0`”; individual layers need not commute with translations (`T/CG16S.md:120`). Its Weyl-pairing application requires a finite node set consisting of Weyl points. The scope leaves open “defects over a filled or entangled background”; setting F “has no links” (`T/CG16S.md:140`). RCSP16’s longitudinal band does not establish those hypotheses (`T/RCSP16.md:100`: “the pairing hypotheses are not established”).

- **Clifford-band engineering and NN-a compilation exist on other sectors.** Frozen LZ1I constructs “two neutral propagating bands of different Clifford speeds” on even-m L5-U laws (`T/LZ1I.md:5`). These do not settle the charged prescription: “the present bands are neutral” (`T/LZ1I.md:216`). GA1_5 Lemma U compiles any unitary on a finite connected link set into “a finite product of unitaries” on its stated edge algebras (`T/GA1_5.md:236`). That compilation is explicitly an “unrefereed” closure (`T/GA1_5.md:11`).

- **Topological charge comparators exist, with different content.** The unsoldered three-axis toric-code construction moves a vertex charge by `2e_a` using “a single Z” (`M/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md:46`). “The charges are bosons” (`same file:48`). Its ledger remains `"effective_status": "unaudited"` (`L/th/three_axis_qubit_site_stabilizer_rules_unsoldered_toric_codes_move_soldered_maximal_rules_do_not_bounded_theorem_note_2026-10-17.json:31`).

- **BKSF supplies a fermionic-string comparator, with a covariance cost.** The supplied cubic codes have T-junction sign “-1 for all 20 triples” (`M/BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md:37`). Within that translation-invariant ordering family, “No code is invariant under the full cubic group” (`same file:53`). The rotation-class companion makes its spinorial inference conditional on “the stated localization relation” (`M/BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md:175`). Both ledger rows remain `"unaudited"` (`L/bk/bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17.json:31`; `L/bk/bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17.json:30`).

- **Explicit dressing and charged spectral constructions precede this lane.** The integer-rotor note constructs an “explicitly constructed isometry” into exact Gauss space (`M/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md:32`). It does not identify invariant dynamics: “The full Hamiltonian can leave its range” (`same file:237`). The finite-clock note constructs a common space from the “actual mixed static kernel,” but concerns “not moving matter” (`M/FINITE_CLOCK_STATIC_CHARGE_TRANSFER_HAMILTONIAN_AND_PATH_COMPARISON_BOUNDED_THEOREM_NOTE_2026-09-15.md:59,4`). Their ledger statuses are `"unaudited"` (`L/ro/rotor_global_gauss_dressing_coulomb_variational_compression_bounded_theorem_note_2026-09-16.json:27`; `L/fi/finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_bounded_theorem_note_2026-09-15.json:29`).

- **Motion bounds do not already supply a particle band.** The native-charge note establishes low-energy spectral weight for its specified position observable, but does not identify “a sharp particle pole, or a nonzero curvature of the lowest band” (`M/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:270–271`). Its ledger is `"unaudited"` (`L/na/native_charge_motion_and_spectral_weight_bounds_bounded_theorem_note_2026-09-15.json:32`).

**Failed attempts on file.**

- **Fixed-site Mott composite 16.** The proposed odd level is “not an excitation above a singlet”; the fixed-site centre theorem then leaves odd excitations vector class (`G:1021–1022,987`).

- **Literal Z4 centre gauging.** Logged #10045 leaves the odd centre charge “a static c-number background”; charge-one link defects are “Spin(10) singlets with Levin-Wen sign +1” (`G:1204`). Its fractionalized-spinon alternative has no established “deconfined phase, spinon dynamics, statistics or spatial spin-1/2” (`same line`).

- **Frozen-background cone construction.** Locked states give no strings; the alternating U-law background gives transverse flatness. The O-law transfer fails because “empty matter is not generally preserved by the Majorana hop” (`T/RCS1.md:225`).

- **Free-link approximation and unspecified Dirac cloud.** The coherence bounds obstruct the stated c-number approximation. The cloud lacks “specified weights or sector decomposition” (`T/RCS1.md:227`). The same passage says those bounds “do not exclude collective deconfinement.”

- **Universal ray-label conservation.** The empty-matter argument needs distant hops to annihilate the background. In filled states, “hops can act on ray links”; “No general conservation theorem is supplied” (`T/RCS1.md:231`).

- **Finite-block loop condensation as the escape.** In `Ψ_λ`, loops miss the inter-block links. The string changes a sharp target count from eight to nine, so “the transverse position of the ray is observable” (`T/RCSPC.md:164`).

- **Decoupling all entangled backgrounds.** RCSPC attack A fails because the long string weight stays beside the tested line. The required positive factorization bound “is false for entangled states” (`T/RCSPC.md:214`).

- **Asymptotic flux detection.** Attack B has an exact raising relation but lacks control of the reweighted background: “`ν_x` itself is not controlled” (`T/RCSPC.md:216`).

- **Stacking seventeen strings.** Attack C cannot turn quasi-equivalence of single-string limits into composable local charge morphisms: “straight-string limit sectors carry no composition law” (`T/RCSPC.md:218`). Individual unitary O-law link factors do not repair the complete string’s nonunitarity (`T/RCS1.md:195`: “neither is an isometry”).

- **Rigid-plane counterexample.** Exact relations tying parallel lines instead give disjoint sectors and no node. Whether they satisfy the bare cone-lift limit “is not decided” (`T/RCSPC.md:274`).

- **Uncorrected block-product theorem.** Translation invariance of the partition did not ensure translation invariance of its state. The original general statement “is false”; summable lowest-level weights give non-disjoint ray sectors (`T/RCSPC.md:182`). The corrected theorem adds cell-translation invariance.

- **Moving D-reg defects with the existing matching state.** The transfer layer “breaks matchings.” A stationary moving-defect update, energy bound and base matter-gate compilation remain open (`T/CG16D_REFEREE.md:251`).

**Overlap with this lane's results.**

not run

**Missed inputs.**

- **Resolve the label interface before treating L5-O as an unblocked spinor route.** The brief asks for “chi_tot = -1, boundary flux label” (`briefs/RCSPO.txt:1`). Existing R-16^str′ gives boundary label `+1` on `S_+` (`T/CG16B.md:182`: “on `L5-O[S_+]` it is `+1`”). This changes the first obligation: distinguish odd charged sectors from sectors satisfying the specified spinor-flux reading.

- **Use the full-string result alongside link-factor unitarity.** RCS1 already shows that no rescaling of the displayed string conjugation “is an automorphism” (`T/RCS1.md:195`). A toric-code-style construction therefore needs an actual limiting morphism or intertwiner, rather than an inference from unitary entries.

- **Use finite-index quasi-equivalence as the factor-sector test.** RCSPC Corollary 2 requires transverse equivalence in two independent directions through a finite-index subgroup (`T/RCSPC.md:97`: “components orthogonal to `e` are linearly independent”). Merely finding one pair of non-disjoint rays would not discharge that necessary condition.

- **Specify a wider register’s law separately.** LW1_5 permits finite Spin(20) representations, but its displayed electric layer is defined only for `S_+`. A replacement “require[s] their own covariance check” (`T/LW1_5.md:94`). The existing literature inventory identifies the algebraic match, while warning that “The Lie algebra alone does not fix Spin(10) versus SO(10) … or matter representations” (`T/LIT_QLM.md:55`).

- **Reuse explicit sector and statistics comparators within their scope.** The rotor isometry and finite-clock mixed kernel replace an unspecified dressing by concrete maps (`rotor note:32`: “explicitly constructed isometry”; `finite-clock note:59`: “actual mixed static kernel”). BKSF provides straight-leg fermionic statistics, but its tested codes lack full cubic invariance (`BKSF orbit note:37,53`: “-1 for all 20 triples”; “No code is invariant”). These change intermediate construction choices; none supplies the requested L5-O Clifford band.

- **Check RC-W on the constructed charged representation.** Its scope expressly leaves open filled or entangled backgrounds (`T/CG16S.md:140`: “defects over a filled or entangled background”). A microscopic finite-depth decomposition alone does not establish the required finite-component charged-walk interface.

**Consumers.**

- **R-CS adoption.** The weakest immediate input is a scoped answer to the charged Clifford-node existence question. Adoption additionally waits for the physical vacuum test: “adoption waits until those settle” (`T/TOE_ASSEMBLY.md:225`).

- **MT1-S and VC1.** MT1-S needs the odd node in “the VC1 vacuum,” satisfying “ER’s Clifford one-cone condition” (`T/MT1.md:154`). Physical spin still needs identification of ER with physical rotations (`same line`: “remains necessary”). VC1 requires MT1 matter to be “its particle-hole excitations” (`T/TOE_ASSEMBLY.md:524`). A supplied witness background is a weaker input.

- **CG1, CH1 and SMG1.** A defined charged carrier and dressing would supply part of their interface. CH1 explicitly needs “a gauge-covariant dressing or a charge-sector prescription” (`T/CH1.md:45`). A family claim needs more than boundary class: R-16^str′ “does not establish an irreducible 16 or a band” (`T/CG16B.md:182`). The wall target additionally requires “every mirror and doubler gapped” (`T/TOE_ASSEMBLY.md:718`).

- **LZ1/CN1 and ZM1.** A charged dispersion statement would provide a species for the common-cone programme, whose target concerns species interacting “through a common gauge field” (`T/TOE_ASSEMBLY.md:720`). Charged scale comparison remains separate: charged sectors “get no zoom from this map; they need a separate bridge” (`T/TOE_ASSEMBLY.md:255`).

- **YM branch and GA2/Y4.** No direct RCSPO consumer was found in the searched YM material or its open-statement registry. The assembly identifies the indirect interface: “T0 is pure gauge”; adding chiral matter is outside its statement, with “CH1-ii (a local gauged measure)” as the entry point (`T/TOE_ASSEMBLY.md:606`). The weakest useful contribution is specified matter-sector data compatible with that separate extension.