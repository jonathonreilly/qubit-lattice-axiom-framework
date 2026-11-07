**Searches run.**

- Read `ref/README.md` first. Searched `ref/main/docs/`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`, including drafts, referee reports and `LIT_*.md`.
- Terms: `ice-t`, `tail.trivial`, `odd.m`, `transition system`, `Rokhsar`, `number shadow`; then `L5-U`, `rishon`, `Gauss.charge`, `gauge.invariant.*pur`, `uniform ice`, `ice.superposition`, `Schreier`, `frozen flip`, `VC1-5U-odd`, and `Σc.odd`.
- Used only the permitted file-reading commands. No internet search, git command or edit.
- Below, `T/` means `repo/.claude/science/physics-loops/toe-assembly-20261104/`. `D/` means `ref/main/docs/`. Ledger paths are relative to `D/audit/data/ledger/`.

**Already in the repo.**

- **Target and present status.** The brief asks for an odd-`m` state satisfying “(i)-(iii) and purity P on the gauge-invariant algebra”, or a nonexistence result (`briefs/vcodd.txt:2`). The lane remains a “proposed amendment” (`T/VC1_5U_ODD.md:5`). A referee report now exists, but “grants no status” (`T/VC1_5U_ODD_REFEREE.md:6`). Neither ICE-T nor R4 tail triviality is established: “Neither ICE-T nor tail triviality of an R4 limit is proved” (`T/VC1_5U_ODD.md:9`).

- **Frozen algebraic baseline.** Gauge averaging identifies invariant-algebra states with gauge-invariant field states: “with inverse `φ↦φ∘E`” (`T/VC1_5.md:35`). P implies factoriality for locally gauge-invariant states: “`π_ω(A)''` is a factor” (`T/VC1_5.md:164`). These belong to the frozen part, whose status is “FROZEN 2026-11-05” (`T/VC1_5.md:5`).

- **Integer filling and odd-link obstruction.** P makes every Gauss charge sharp; cell symmetry then gives integer filling: “`ω(N_x)=q_x-3m`” (`T/VC1_5.md:103`). For odd `m`, reversal symmetry forbids sharp end numbers and factorization across link ends: “no state factorizing across the two ends is reversal invariant” (`T/VC1_5.md:95`). These statements allow arbitrary constants and plaquette classes (`T/VC1_5.md:103`: “any `m`, constants and plaquette class”).

- **Product-partition obstruction.** A cell-invariant odd-`m` product with sharp matter and Gauss numbers cannot give P through a nontrivial invariant link partition: “no such nontrivial product partition gives a P-witness” (`T/VC1_5.md:121`). R3 includes matter in the partition and removes matter sharpness: “No sharpness of `N_x` is assumed” (`T/VC1_5.md:201`). Its scope is explicitly limited: “not a no-go theorem for states outside those classes” (`T/VC1_5.md:145`).

- **Even-`m` comparison states.** Empty- and full-matter P-witnesses already exist for even `m`: “It satisfies (i)–(iii) and P” (`T/VC1_5.md:111`). Pure, cell-symmetric all-site singlets also exist for `m=2,4,6,8`, but “No stationarity is claimed” (`T/VC1_5.md:152`). The older finite-box singlet construction exists for every `m`, while “full point-group invariance and stationarity remain open” (`T/LW1_5.md:225–229`).

- **R4 already supplies stationary symmetric odd-`m` limits.** Uniform zero-flux ice superpositions have limit points whose averages satisfy (i)–(iii), sharp `Q_x=3m`, and filling zero: “`ω∘E` satisfies (i)-(iii)” (`T/VC1_5.md:210–214`). Its unresolved obligation was already explicit: “Whether some `ω∘E` of R4 is pure” (`T/VC1_5.md:221`).

- **Earlier factor-to-tail argument.** The transport draft contains Remark 6.1, “factor states have tail-trivial Born laws; sketched, credited” (`T/LW1U_DRAFT.md:196`). It concerns the cube CAR algebra and site Born law. Its proof sketch invokes “Powers’ theorem (1967)” (`T/LW1U_DRAFT.md:198`). This is an antecedent of the lane’s shadow theorem, with narrower observables and a different proof presentation.

- **Finite cubic-ice RK construction.** The existing spin-half note identifies the RK Hamiltonian as a graph Laplacian; “the equal-amplitude vector on each connected component is an exact zero” (`D/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:174–191`). Its thermodynamic scope is limited: “does not itself establish … a thermodynamic limit” (`same file:260–262`). Ledger status is `"effective_status": "unaudited"` (`sp/spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03.json:32`).

- **Plaquette annihilator and component degeneracy.** A supplied covariant spin-half plaquette generator annihilates uniform ice on the RK line, `g(P_flip-U-U†)`. For `g>0`, its ground space consists of class-uniform vectors and their superpositions: “amplitudes are constant on each connected component” (`D/DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md:38–57`). This supplies “no preparation theorem” (`same file:65–67`). Ledger status is `"effective_status": "unaudited"` (`dy/dynamics_clause_the_covariant_plaquette_clause_annihilates_uniform_ice_exactly_at_the_rokhsar_kivelson_point_and_unrecorded_plaquettes_can_polarize_the_ice_bounded_theorem_note_2026-09-24.json:29`).

- **Zero winding does not imply plaquette connectivity.** Frozen configurations exist on every even torus: “each is a one-state flip component” (`D/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md:25–32`). The note does not classify all larger-volume components: “Not … every non-frozen zero-winding state” (`same file:61–64`). Ledger status is `"effective_status": "unaudited"` (`ri/ring_model_the_zero_winding_gauss_sector_has_frozen_flip_components_on_every_even_torus_bounded_theorem_note_2026-10-01.json:30`).

- **Classical measure selection.** On the specified finite torus, hard local rules admit uniform, zero-flux-uniform and point-mass laws: “Every probability measure on this finite support is compatible” (`D/COULOMB_MEASURE_SELECTION_HARD_STATIC_ICE_RULES_ADMIT_EVERY_ICE_MEASURE_POSITIVE_RULES_SELECT_THE_UNIFORM_ONE_BOUNDED_THEOREM_NOTE_2026-09-22.md:18`). A supplied positive weight selects uniform ice after conditioning, but “No … infinite-volume selection” follows (`same file:20–24`). Ledger status is `"effective_status": "unaudited"` (`co/coulomb_measure_selection_hard_static_ice_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_bounded_theorem_note_2026-09-22.json:30`).

- **Thin-prism construction.** Positive transfer blocks give stationary zero-flux ice chains with uniform conditional in-plane completions: “it reproduces the limit measure” (`D/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md:75–92`). The transverse sections are fixed: “Infinite height at fixed cross-section is not an infinite-cross-section Coulomb phase” (`same file:25`). Ledger status is `"effective_status": "unaudited"` (`un/uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23.json:29`).

- **A prior conditional Gibbs route to tail triviality.** The six-axis static-model note proves the implication “Unique implies tail-trivial” by conditioning on a tail event (`D/ADMISSIBILITY_RULE_STATIC_SIX_AXIS_REFLECTION_IDENTITIES_AND_CONDITIONAL_CONTOUR_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:201–205`). Its model and probability bounds are supplied; “unconditional … phase conclusions … are deferred” (`same file:252`). Ledger status is `"effective_status": "unaudited"` (`ad/admissibility_rule_static_six_axis_reflection_identities_and_conditional_contour_bounds_bounded_theorem_note_2026-09-15.json:30`).

**Failed attempts on file.**

- **Sharp-end and bounded-block products.** Reversal fails for odd sharp ends (`T/VC1_5.md:95`: “neither end number is sharp”). Nontrivial invariant products fail P (`T/VC1_5.md:121`: “restriction … is not pure”). These failures do not exclude general entangled states (`T/VC1_5.md:145`: “outside those classes”).

- **Finite-volume purity passed to a limit.** The missing step is precisely “finite-volume purity need not survive a weak-* limit” (`T/VC1_5.md:146`). The lane replaces this with a criterion, but still proves no R4 tail triviality (`T/VC1_5U_ODD.md:124–130`: “exactly when `ν` is tail-trivial”).

- **A1, deterministic transition systems.** Every invariant pairing system has infinite trails. Independent orientations leave a nontrivial tail event: “a tail event of probability `1/2`” (`T/VC1_5U_ODD.md:142–144`).

- **A2, independent random transitions.** The unproved step is “almost-sure finiteness of all trails” (`T/VC1_5U_ODD.md:146`). The referee reduces the remaining obligation to A2-FIN; conditional quasi-invariance is supplied there (`T/VC1_5U_ODD_REFEREE.md:199–202`: “A2 now stands on one open statement”).

- **A3, hierarchical finitary factor.** Finitary coding does not supply finite output change under finite input resampling (`T/VC1_5U_ODD.md:148`: “finitary coding alone does not imply it”). The referee’s counterexample has “infinitely many outputs change” with probability `1/2` (`T/VC1_5U_ODD_REFEREE.md:338`). For the proposed ice coding, “Neither that moment bound nor quasi-invariance is known here” (`same file:208`).

- **A4, uniform ice.** The missing estimate is decay of boundary influence: “no such estimate is proved here” (`T/VC1_5U_ODD.md:150`). Finite covariance evidence cannot replace it: “does not establish … an infinite-volume limit” (`D/UNIFORM_ICE_STATIC_PHOTON_HAS_TWO_DEGENERATE_TRANSVERSE_POLARIZATIONS_WITH_ONE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md:32`).

- **LSM exclusion.** The lane’s literature record reports that the surveyed theorems require a gap, unique ground state, short-range entanglement or split property; “Reading P assumes none of these” (`T/VC1_5U_ODD_DRAFT.md:49`). This records a failed application, not a nonexistence theorem.

- **Fixed local formation of finite uniform ice.** The specified torus search “visits 65 sets and finds no complete order” (`D/THE_LANDED_TORUS_UNIFORM_ICE_MEASURE_ADMITS_NO_LOCAL_FORMATION_ORDER_EVEN_WITH_EVERY_COORDINATOR_BOUNDED_THEOREM_NOTE_2026-09-23.md:19`). Its limitation is “fixed deterministic orders”; adaptive orders and hidden shared state are not excluded (`same file:25`). Ledger status is `"effective_status": "unaudited"` (`th/the_landed_torus_uniform_ice_measure_admits_no_local_formation_order_even_with_every_coordinator_bounded_theorem_note_2026-09-23.json:31`).

**Overlap with this lane’s results.**

The pass-2 text explicitly calls itself a “distillation” of its own draft (`T/VC1_5U_ODD.md:5`). Its main statements **DUPLICATE that same-lane draft**, whose inventory already lists the isotype, shadow, RK, purity, sufficiency, necessity, R4, resampling and singlet results (`T/VC1_5U_ODD_DRAFT.md:296–307`). Relative to work outside that draft:

| Lane result | Classification and prior overlap |
|---|---|
| Lemma 2.1, one isotype | **EXTENDS** frozen central sharpness from charges to isotypic projections. Prior: “central element … is sharp” (`T/VC1_5.md:49`). Lane: “selects exactly one isotype” (`T/VC1_5U_ODD.md:31`). |
| Theorem 2.2 and Corollary 2.3, number shadows | **EXTENDS** LW1U Remark 6.1. Prior: “Born law … trivial tail” (`T/LW1U_DRAFT.md:196`). Lane includes matter and link numbers, and factoriality of the invariant restriction: “or its restriction to `A^gauge`” (`T/VC1_5U_ODD.md:37`). |
| Lemmas 3.1–3.4 and Theorem 4.2, ice representation | **EXTENDS** R4’s finite uniform construction to arbitrary quasi-invariant ice laws. Prior uses “`|𝒞_L|^{−1/2}Σ`” (`T/VC1_5.md:210`). Lane starts with “a quasi-invariant Borel probability measure” and obtains stationary states (`T/VC1_5U_ODD.md:74,94`). The older RK graph-Laplacian mechanism is an antecedent, not a duplicate of this `U(5)` representation. |
| Theorem 4.3, purity iff tail triviality | **NEW** relative to the earlier independent work found. It says “pure … if and only if `ν` is tail-trivial” (`T/VC1_5U_ODD.md:102`). The frozen precursor explicitly lacked “invariant-algebra purity” (`T/VC1_5.md:146`). |
| Theorem 5.1, ICE-T sufficiency | **EXTENDS** even-`m` edge-filling witnesses conditionally to all odd `m`. Compare “Let `m=2k`” (`T/VC1_5.md:111`) with “If ICE-T holds, every odd `m`” (`T/VC1_5U_ODD.md:114`). It is not an unconditional existence result. |
| Theorem 5.2, edge necessity | **NEW** relative to the earlier independent work found. At `m=1,9`, edge-filling P-witnesses imply ICE-T⁻, with “any plaquette class” (`T/VC1_5U_ODD.md:118`). |
| Theorem 5.3, R4 characterization | **EXTENDS** R4. Prior supplies stationary symmetric limit points (`T/VC1_5.md:214`). Lane adds flip invariance, the representation identity, and the purity criterion (`T/VC1_5U_ODD.md:124`). This concerns each limit point: the referee rejects wording that “Presupposes one R4 limit” (`T/VC1_5U_ODD_REFEREE.md:49`). |
| Lemma 6.1, finite-resampling criterion | **NEW** relative to the earlier independent work found. Its hypothesis is that finite resampling “changes only finitely many arrows almost surely” (`T/VC1_5U_ODD.md:138`). |
| Proposition 6.2, deterministic systems | **DUPLICATES** the geometric path classification in VC1 Theorem 6.1: “all are bi-infinite paths” (`T/VC1_5.md:136`). It **EXTENDS** that classification by exhibiting the fair-orientation tail obstruction (`T/VC1_5U_ODD.md:144`: “probability `1/2`”). |
| Theorem 7.1, odd singlet necessities | **EXTENDS** finite-box Lemma P/F-U to infinite-volume necessary conditions. Prior: “Its eigenvalue then lies in `5Z`” (`T/LW1_5U_DRAFT.md:60`). Lane adds tail constraints and excludes its RK states from field-algebra-pure singlets: “No state `ω_ν` … is such a pure … state” (`T/VC1_5U_ODD.md:164`). |
| Records and LZ1 remarks | **DUPLICATE applications** of prior criteria. Records reuse Corollary 5.6 (`T/VC1_5U_ODD.md:132`: “proof … applies”). The static-band remark invokes existing RC1(c)(iii) (`same file:134`: “conditional conclusion … applies”). |

No substantive **CONTRADICTS** overlap was found. The draft itself states “No frozen claim is contradicted” (`T/VC1_5U_ODD_DRAFT.md:309`).

**Missed inputs.**

- **Credit the earlier factor-tail sketch.** LW1U already states the conceptual antecedent: “factor states have tail-trivial Born laws” (`T/LW1U_DRAFT.md:196`). This changes the shadow theorem’s prior-work description to an extension of an on-file result.

- **Keep the full zero-flux sector separate from one plaquette component.** Frozen zero-winding states exist “on every even torus” (`D/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md:54–55`). R4 sums over the full `𝒞_L` (`T/VC1_5.md:210`). Component-restricted Monte Carlo therefore needs an additional comparison before serving as evidence about R4; the RK note supplies “No … whole-sector mixing bound” (`D/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:498–503`).

- **Use the thin-prism transfer construction as a bounded test case.** Its positive block gives an explicit boundary-decay calculation: “rate … `14/60.91` per layer” (`D/UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md:77–83`). Extending such control uniformly in cross-section would address the kind of estimate A4 lacks; the existing result remains fixed-cross-section (`same file:25`).

- **Separate specification, state selection and preparation.** Hard finite specifications admit every ice measure (`D/COULOMB_MEASURE_SELECTION_HARD_STATIC_ICE_RULES_ADMIT_EVERY_ICE_MEASURE_POSITIVE_RULES_SELECT_THE_UNIFORM_ONE_BOUNDED_THEOREM_NOTE_2026-09-22.md:18`). The plaquette note likewise distinguishes “annihilating uniform ice, selecting a ground space and preparing a particular state” (`D/DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md:127–128`). These inputs limit what a proposed uniform-law construction would settle.

- **Carry the referee’s new conditional closures forward.** RC-A2 proves ICE-T under A2-FIN (`T/VC1_5U_ODD_REFEREE.md:317`: “tail-trivial, quasi-invariant”). RC-A3b supplies a summable-radius criterion; “`E[R^3]<∞`” suffices on `Z³` (`same file:342–346`). They narrow the remaining attacks without closing either missing hypothesis.

- **Remove unnecessary ICE-T dependence from downstream applications.** The referee notes “ICE-T is not needed at lines 132 and 134” (`T/VC1_5U_ODD_REFEREE.md:153`). Records and the LZ1 static-background conclusion already apply to every R4 limit point under their stated readings.

**Consumers.**

- **VC1 and assembly coherence.** The immediate need is one odd-`m` stationary, gauge-invariant, cell-symmetric P-witness (`briefs/vcodd.txt:2`: “for some odd m”). Full VC1 additionally needs sea continuation, stability, excitations and energy density; the lane establishes none of these (`T/VC1_5U_ODD.md:176`: “No statement establishes”). AS0 requires “one law … and one vacuum” (`T/TOE_ASSEMBLY.md:650`).

- **LW1-5U-Σc-odd.** It needs a field-algebra-pure symmetric singlet. ICE-T alone supplies only a classical necessary ingredient: it “does not construct the needed `SU(5)`-singlet quantum state” (`T/VC1_5U_ODD.md:170`).

- **TM1.** Sharp, identical site numbers at every tick suffice for the conditional tick-1 record conclusion; P is unnecessary (`T/VC1_5U_ODD.md:132`: “site numbers are sharp and constant”). The referee explicitly extends this to R4 limits without ICE-T (`T/VC1_5U_ODD_REFEREE.md:153`: “conditional record conclusion holds”).

- **LZ1 / LW1-5-BG.** Stationarity, gauge and cell invariance, plus positive variance of one traceless Gauss generator, suffice (`T/LZ1.md:174`: “some … generator … `>0`”). Tail triviality is unnecessary (`T/VC1_5U_ODD_REFEREE.md:153`: “tail-trivial or not”).

- **CH1-5UQ.** Sharp site numbers suffice for its number-diagonal obstruction. It already includes “the odd-`m` ice limits” (`T/CH1_5UQ.md:174`). End-number coherence alone does not escape it: “Coherence of single end numbers … does not suffice” (`same file:175`).

- **RCS-P / MT1-S[R-CS^str].** The selected vacuum must support the specified string sectors and charged-node test (`T/RCS1.md:13`: “in the VC1 vacuum”). Factoriality matters for localized-sector results, while sharp matter filling supplies the parity background (`T/RCS1.md:156,170`: “parity-sharp”; “vacuum sector … a factor representation”). The lane does not establish the required string propagation (`T/VC1_5U_ODD.md:134`: “does not prove a propagating physical excitation”).

- **GA1-P-5.** It needs preservation under a specified plaquette layer. Base-tick stationarity is insufficient: a plaquette layer “need not preserve these states” (`T/VC1_5U_ODD.md:110`).

- **GA2 / the YM bridge.** Y2-W needs the actual VC1 state and constants yielding “a controlled small-coupling window” (`T/GA2_Y2.md:161`). The bridge then requires controlled correlator comparisons and quantified errors (`same file:169`: “with quantified errors”). No direct YM-branch consumer of ICE-T or VC1-5U-odd was found; the documented interface remains GA2, whose T0 starting theory is “Wilson SU(2)” with other groups and matter separate extensions (`same file:169`).