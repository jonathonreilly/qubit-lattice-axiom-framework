**Searches run.**

- Read `ref/README.md` first. It identifies the corpus and says “Ledger rows: main/docs/audit/data/ledger/” (`ref/README.md:2`).
- Initial terms: `gauge-covariant block`, `truncated two-point`, `tail-envelope`, `p=2`, `ZM1-I1`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104`.
- Follow-ups: `block map`, `relative tail`, `level-matched`, `constrained.fiber`, `straight-link blocking`, `Peter.Weyl`, `state compatibility`, `ZM1I1A`, and `ZM1-I1[a]`. Searched consolidation notes, ledger rows, the YM library, other TOE parts, drafts, referee reports, prior digests, and `LIT_*.md`.
- Used only the permitted read commands. No internet, git, or edits.

Path shorthand:

- `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`.
- `M` = `ref/main/docs`.
- `Y` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library`.
- `G` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `W[STEM]` = `M/WILSON_STAGGERED_STEM_BOUNDED_THEOREM_NOTE_2026-07-12.md`.
- `J[STEM]` = `M/audit/data/ledger/wi/wilson_staggered_stem_bounded_theorem_note_2026-07-12.json`, with the stem lowercased.

**Already in the repo.**

- **The target is specified, but existence remains open.** Section 3.8 selects local invariant truncated two-point functions, all finite support radii, singleton embedding sets, and the relative envelope budget with “`p=2`.” It explicitly “asserts no existence result.” The inherited coarse law is “of the `L5-U` form.” (`T/TOE_ASSEMBLY.md:243`; `T/ZM1.md:361`.) The amendment records “Open: ZM1-I1[a]” (`T/ZM1.md:12`).

- **The envelope forces exact asymptotic matching.** Lemma ER bounds the difference between the two tail envelopes by the same relative budget. For exponential tails, “`ξ₀=ξ₁` and `a₀=a₁`”; for power tails, “`η₀=η₁` and `a₀=a₁`.” This is channel-by-channel, at each fixed tick, when those asymptotic forms exist. ER is among the “Referee closures, unrefereed.” (`T/ZM1_OBS.md:284–292,9`.)

- **Invariant data have an established scope.** Theorem 2 permits replacing the stationary coarse state by its gauge average while preserving invariant data. Theorem 3 gives “`Φ(𝔄₁^G)⊆𝔄^G`” for representative-site maps. Theorem 4 says complete truncated data determine the tick/translation representation on “`H_phys⊖CΩ`.” They do not determine one-point values or arbitrary charged sectors. These are frozen results under their displayed hypotheses. (`T/ZM1_OBS.md:5,65–85`.)

- **Exact regrouping exists with growing content.** Z0 gives an exact, gauge-preserving regrouping of the base tick. Its cost is “`D` grows like `exp(c L^3)`.” Z4 separately gives “`D_u >= n_0 |S_u| + 1`.” Neither supplies the selected fixed-form coarse law with singleton gauge embedding. The source states that its proofs “are not independent audit status.” (`T/ZM1.md:93–105,311,14`.)

- **Exact quasi-free compression has a rank restriction.** Z1 requires “`d = L^3 r`” under exact intertwining, translation covariance, and summable-kernel hypotheses. Its scope is expressly “quasi-free block maps”; nonlinear maps remain undecided. (`T/ZM1.md:117,142`.)

- **A narrower free comparison already achieves second-order error.** Z2 gives exponentially local isometric blocking and the bound “`2.66 κ² + 1.5 t κ³`” for band-limited free dynamics. Its sea estimate has an additional `κ²` term. Lemma C′-free extends the free comparison to trace-class bilocals with absolute error “`8β(t)‖K‖₁‖K′‖₁`.” The relative and quantum-link extensions remain open. (`T/ZM1.md:242–255`; `T/ZM1_OBS.md:306–315,13`.)

- **Nonlinear dressed fields remain available algebraically.** The source gives `Ψ=WcW*` with a gauge-invariant circuit as an example satisfying CAR and singleton G1–G2. It immediately separates the remaining obligation: “a covariant, translation-consistent block map with a coarse law.” (`T/ZM1.md:359`.)

- **The level-matched gauge split supplies a concrete toy construction.** #9928 gives a gauge-, winding-, and translation-covariant polar map matching parent levels to low child levels. Its scope is “an isometry in a 2+1D Z_3 toy”; “no continuum limit of the register is computed.” The consolidation’s status is “author statements for review.” (`G:287,295,311,11`.)

- **Dyadic refinement separates algebra, state, and dynamics compatibility.** A supplied one-dimensional massive free chain has explicit support-preserving even embeddings and an intrinsic Cauchy criterion. The note says the refinement “does not make the actual finite-scale states or energy flows exactly compatible.” Ledger status is `"effective_status": "unaudited"`. (`M/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:38–50`; `M/audit/data/ledger/dy/dyadic_even_refinement_bounded_theorem_note_2026-10-12.json:33`.)

- **The constrained-fiber inputs extend beyond Amendment 1’s gauge-body results.** The following are supplied Wilson–staggered action-space statements. Their ledger status is **unaudited**, as quoted in the final column. Their stated scopes do not establish the selected VC1 operator comparison.

| Prior result | Scope and stated limit | Ledger |
|---|---|---|
| Uniform hard-fiber mixing and raw unit directions | For `alpha(beta,m)<1/2`, hidden Gibbs control is uniform in the coarse configuration. Raw integration obeys “`R(Phi+t Lf)=R(Phi)+t f`.” No multiscale trajectory is constructed. `W[CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS]:39–75`. | `J[CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS]:27`: `"unaudited"` |
| Exponentially local raw Hessian | Uniform first and second responses give a “volume-uniform exponentially local Hessian.” Retained-Grassmann directions are excluded from this positive-measure theorem. `W[RAW_CONSTRAINED_ACTION_HESSIAN_DECAY]:25–75`. | `J[RAW_CONSTRAINED_ACTION_HESSIAN_DECAY]:29`: `"unaudited"` |
| Complex-source gauge-body polymers | A strict small-activity region gives a common zero-free source domain and connected-cumulant bounds. “The theorem is gauge body only.” `W[CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER]:39–70`. | `J[CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER]:29`: `"unaudited"` |
| Simultaneous retained-Grassmann closure | The exact one-step logarithm belongs to an all-degree connected polymer norm; coefficients “remain jointly coarse-gauge invariant.” This is “one-step mathematical closure,” without an invariant RG neighborhood or critical trajectory. `W[RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM]:55–89`. | `J[RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM]:30`: `"unaudited"` |
| Declared rescaled charts | Extended raw lifted directions gain “`exp(-lambda)`.” The result covers the lifted subspace, “not on the full derivative”; it does not select physical coordinates. `W[DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION]:35–65`. | `J[DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION]:30`: `"unaudited"` |
| K-retaining marked attachment | At the displayed ultra-massive point, “`q_sw=exp(-1/2)`.” The strong-to-weak estimate does not return output to the same strong norm at the next level. `W[K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION]:95–125`. | `J[K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION]:30`: `"unaudited"` |
| Gaussian-adapted reference and quadratic center | At `eta=m^(-1/2)`, Gaussian reference norm is “exactly one.” The shortest Schur center satisfies “`S^(2)…>=mI`.” All-scale tagged control remains unproved. `W[GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER]:29–98`. | `J[GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER]:32`: `"unaudited"` |
| One-horizon lineage lift | The decorated lift evaluates exactly to the ordinary residual action. It supplies “genuine factor/cluster provenance,” but no scale-to-scale density or autonomous-norm theorem. `W[ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT]:11–15,103–109`. | `J[ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT]:32`: `"unaudited"` |
| Enhanced-moment generated-base return | Fresh enhanced input moments supply “decorated factor membership before the next preintegration.” This does not integrate the next fiber or estimate two marked insertions. `W[ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN]:11–22`. | `J[ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN]:33`: `"unaudited"` |
| Site-block marked response | Actual hidden-coordinate ownership supplies a strict marked response and an “ordinary retained-coefficient” output envelope. “No autonomous iteration, generic source ball, taste selection, or continuum follows.” `W[SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN]:150–184`. | `J[SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN]:33`: `"unaudited"` |
| External Schur-center/tail ownership | The note separates hidden-empty and centered tail pieces and gives explicit path-tail bounds. The larger center update remains a “conditional Weyl budget”; correlated-center mixed clusters were not included. `W[EXTERNAL_SHORTEST_SCHUR_CENTER_HAAR_TAIL_PROJECTED_QUADRATIC_WEYL_CONDITIONAL_REFERENCE]:11–20,55–90,105–125`. | `J[EXTERNAL_SHORTEST_SCHUR_CENTER_HAAR_TAIL_PROJECTED_QUADRATIC_WEYL_CONDITIONAL_REFERENCE]:33`: `"unaudited"` |

- **Finite local-observable approximation has quantified resources.** The supplied cubic SU(3) Hamiltonian has spatial and Peter–Weyl cutoff errors independent of ambient volume. The prescription is “First choose r … then choose R.” It retains boundary sectors and makes “No claim of a uniform all-energy fixed-R approximation.” Ledger status is unaudited. (`M/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75–87`; corresponding ledger `M/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`: `"unaudited"`.)

- **Separated tails and contact limits already have distinct comparators.** The supplied weak-window note obtains separated connected correlations “`o(ell^M)`” for every fixed power, while its Haar construction has contact variance “exactly1 at every n.” It asserts no dynamical limit. Ledger status is unaudited. (`M/GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md:64–85`; `M/audit/data/ledger/ga/gauge_wilson_weak_window_quantitative_bounds_and_haar_contact_fdd_bounded_theorem_note_2026-09-07.json:32`: `"unaudited"`.)

- **Other finite-register comparators remain model-specific.** The cyclic gauge/charged-rotor note supplies local finite-time approximation, but “the interacting ground-state and infrared phase problem remains open.” Its ledger is unaudited. The MDTN PR states a strong-coupling physical gap for finite-truncation SU(2)/SU(3), with constants “not on L”; its BHM rebuild remains an “open obligation.” Neither states this lane’s block comparison. (`M/POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md:10–16`; `M/audit/data/ledger/po/positive_finite_cyclic_gauge_histories_and_local_charged_rotor_approximation_bounded_theorem_note_2026-09-14.json:31`: `"unaudited"`; `ref/pr10135/docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md:29–33,143–151`.)

- **YM provides conditional machinery, not a completed existence input.** The Balaban A1 reconstruction calls its endpoint a “conditional proof,” retaining F0 as “cited-pending.” The branch summary says “Existence is not proved.” (`Y/a1-balaban.md:14–25`; `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/FINISH.md:11`.)

**Failed attempts on file.**

- **Minimal coupling of the free block field.** Attack 1 fails at “`Psi_u` is a fermion field.” Z3 and Z3′ force off-representative coefficients to vanish in their finite and norm-closed linear classes. (`T/ZM1.md:382`.)

- **Transferring the free estimate through coherent links.** Attack 2 fails at “the link operators act as c-numbers.” The recorded coherence bounds exclude that criterion. The source preserves the limit: “It does not rule out every state-dependent approximation.” (`T/ZM1.md:384`.)

- **Conserved-projection compression.** Attack 3 encounters Gauss operators containing neighboring-tile link ends. Its classification and rank inference are unproved. It is “not an attack on ZM1-I1 as stated,” and gives “No general conclusion on bounded content.” (`T/ZM1.md:386–388`.)

- **Replacing momentum support by spatial separation.** The missing step is explicit: “physical separation `r` alone does not imply that support.” The maps are also not shown “to compose into a tower.” (`T/ZM1.md:275`.)

- **Vacuum matching without excited-level matching.** The toy split sends parent excitations outside the child low-energy window: “Carrying the vacuum is not enough.” The level-matched polar construction is the recorded repair. (`G:311`.)

- **Raw full-space contraction or conditional centering as nonlinear closure.** Raw integration has exact unit directions. Conditional centering also fails to define an invariant nonlinear sector: “products of centered elements can have a nonzero conditional mean.” The unlocalized Cauchy certificate remains “`>68`.” These are scoped failures; the later chart and attachment results address narrower alternatives. (`W[CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS]:60–75`; `W[SPLIT_DERIVATIVE_AND_UNLOCALIZED_CAUCHY_CERTIFICATE_BOUNDARY]:59–67,95–103`.)

- **Exact finite-scale state and flow compatibility.** The dyadic chain supplies an “exact scalar counterexample” to state compatibility. Its flow derivatives also disagree on an explicit Pauli word. This concerns that supplied refinement, not every possible map. (`M/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:553–579`.)

- **Inferring gauge comparison from a finite diagnostic.** GA2_Y2 states “zero SC-loop defect does not establish SC.” Its product-copy attack additionally fails at “block states are aligned products.” (`T/GA2_Y2.md:138,161`.)

These records do not establish impossibility: “No counterexample is known” (`T/ZM1.md:390`).

**Overlap with this lane’s results.**

not run. The amendment records “Open: ZM1-I1[a]”; the observable-class source says the existence statements were “Specifications, not worked.” (`T/ZM1.md:12`; `T/ZM1_OBS.md:19`.)

**Missed inputs.**

- **Use Lemma ER before choosing a candidate coarse law.** It changes the first test from fitting a decay estimate to matching each nonzero tail’s asymptotic length and amplitude. The source requires “`ξ₀=ξ₁` and `a₀=a₁`.” This is a necessary-condition test, not an existence construction. (`T/ZM1_OBS.md:284–292`.)

- **Carry Amendment 1’s action-space inputs forward to their later extensions.** The retained-Grassmann theorem adds “one-step mathematical closure” beyond gauge-body control. The marked-attachment and site-block notes add strict strong-to-weak response estimates. They would replace a generic contraction aspiration with explicit norms, activity margins, and unresolved return obligations. Their boundaries remain “not an autonomous invariant ball” and “No autonomous iteration.” (`W[RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM]:85–89`; `W[K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION]:117–125`; `W[SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_RESPONSE_RETURN]:177–184`.)

- **Price register approximation and retain boundary sectors.** The Peter–Weyl theorem supplies separate spatial and energy-cutoff errors. It would prevent silently replacing the actual finite registers by unrestricted group links or local singlets. Its cutoff “does not project onto a boundary singlet.” (`M/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:59–83`.)

- **Use level matching for nonlinear candidates, and distinguish one step from a tower.** The toy requires matching “each sector’s parent levels” to low child levels. The dyadic note separately warns that compatible embeddings do not make states or flows “exactly compatible.” These supply distinct tests for a candidate and any later iteration. (`G:311`; `M/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:49–50`.)

- **Check summability before importing spectral-transfer lemmas.** ZM1_OBS’s Fourier setup requires absolutely convergent correlation sums. A supplied massless gauge comparator instead has plaquette correlations “not absolutely summable.” Its ledger is unaudited. This would restrict applications of Theorems 7–9 rather than invalidate class (a). (`T/ZM1_OBS.md:97–99`; `M/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:236–238`; `M/audit/data/ledger/ma/massive_wilson_loop_curvature_noncompact_covariance_and_compact_defect_bounds_bounded_theorem_note_2026-09-14.json:27`: `"unaudited"`.)

**Consumers.**

- **ZM1(a)1 needs the spatial comparison itself.** Its printed minimum is an “explicit `p >= 2`” for separated block correlations. The selected lane supplies one specified comparison step; full ZM1 additionally asks for a “fixed point or a controlled trajectory” and compatible site content. (`T/TOE_ASSEMBLY.md:288–291`.)

- **GA2 and ZM1-G need an observable dictionary and propagated errors.** The weakest useful handoff is a controlled invariant-correlator comparison that composes with the gauge-measure comparison. The source requires “a common dictionary and propagated errors.” ZM1-G additionally requests a “reflection-positive group-valued measure in the relevant RG class”; this lane alone does not supply it. (`T/ZM1_OBS.md:176`; `T/GA2_Y2.md:169`.)

- **LZ1-i can use physical-sector dynamical data, with additional spectral hypotheses.** Class (a) offers “physical-sector correlation data, not a proved speed equality.” Branch transfer needs summability, phase separation, and observable weights; Theorem 9 requires weights “at least `w`.” A common speed across species remains open. (`T/ZM1_OBS.md:110,176`; `T/LZ1.md:159`.)

- **YM’s block/smeared limit interface needs more than one-step two-point matching.** H-BLOCK asks for convergent expectations yielding a joint state on block and smeared observable algebras. It is “not a consequence of curvature cumulant bounds.” This is a prospective interface: the class-(a) source says it “could serve as an operator-side correlator interface for GA2 and T0-start.” (`Y/port/p8b-limits.md:57`; `T/ZM1_OBS.md:176`.)

- **Charged-sector and geometric consumers retain separate obligations.** Class (a) “excludes odd field entries” and does not reconstruct the complementary sector. ST1 still requires “reflection positivity for the chosen update with interactions.” GR2 imports ZM1 but separately requires nonlinear geometry and refinement with collapse. No weaker direct implication from this lane is stated in those sources. (`T/ZM1_OBS.md:176`; `T/TOE_ASSEMBLY.md:331,533–535`.)