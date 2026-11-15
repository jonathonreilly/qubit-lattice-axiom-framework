**Searches run.**

- Read `ref/README.md` first. It identifies `main/docs/`, the consolidation PRs, and `ym/` as the reference corpus: “Ledger rows: main/docs/audit/data/ledger/” (`ref/README.md:2`).
- Initial terms: `gauge-invariant observ`, `Wilson loop`, `charged sector`, `coarse.grain`; then `zero.momentum`, `Creutz`, `string.axis`, `speed transfer`, `on.site return`, `quasi.energy origin`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- Follow-ups used `observable class`, `gradient.flow`, `gauge-invariant correlator`, `smeared`, `scaling limit`, `consolidated`, and named theorem identifiers. Read relevant consolidated notes, ledger rows, frozen parts, drafts, referee reports, `LIT_QLM.md`, and YM library files by line.
- Path abbreviations below: **T** = `repo/.claude/science/physics-loops/toe-assembly-20261104`; **Y** = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library`.

**Already in the repo.**

- **Lane status and target.** ZM1_OBS has run as an author draft. It “is not yet distilled or refereed” (`T/ZM1_OBS_DRAFT.md:7`). Its task is to compare several observable classes before selection: “the owner chooses after that” (`T/TOE_ASSEMBLY.md:227`). The five class-specific existence statements remain “stated, not attacked” (`T/ZM1_OBS_DRAFT.md:453`).

- **Charged two-point comparison already collapses to on-site data.** Frozen ZM1’s R-GI gives zero between distinct coarse sites under its representative-site embedding and local gauge-invariance hypotheses: “for all `X ≠ Y` and all `n ∈ Z`” (`T/ZM1.md:363`). With both states gauge invariant and coarse-translation invariant, the proposed vanishing-error bound requires exact on-site equality “for every coarse site `X`” and every tick (`T/ZM1.md:367`). Status: “FROZEN”; ZM1-I1 remains open (`T/ZM1.md:5`).

- **A controlled free comparison exists, with narrower observables.** ZM1’s free comparison has “constants independent of `k`” and “`p = 2`” (`T/ZM1.md:282`). It requires band-limited fields and a time restriction (`T/ZM1.md:278`: “times `t <= r/(2^k a)`”). Its scope explicitly excludes “arbitrary separated local block observables” and a proved compatible tower (`T/ZM1.md:268`). The O-law free version has “the same bounds (3)-(4)” (`T/ZM1.md:286`).

- **Finite-register Wilson-link obstruction.** Frozen GA2_Y2’s Theorem N states that an invertible covariant operator link forces “`τ=0`” (`T/GA2_Y2.md:30`). Its block extension covers bounded generators, “including a finite sum over a block”; it “fails for an unbounded summed-flux generator” (`T/GA2_Y2.md:48`). Status: “FROZEN” (`T/GA2_Y2.md:5`). This distinguishes correlator comparison from identifying quantum links with Wilson multiplication operators.

- **A prior observable dictionary exists as a proposed diagnostic.** SC fixes the state, scale, observable list, Wilson-function identification, products, normalization, and tolerance. “Constants, normalizations, state, map and list must be fixed before the comparison” (`T/GA2_Y2.md:22`). It is “not a sufficient definition of GA2” at that same line. The proposed ZM1-G already requests a “controlled gauge-invariant correlator comparison” with quantified errors (`T/GA2_Y2.md:169`).

- **Gauge-invariant observables already exclude odd field elements.** Frozen RCS1 Theorem 4 states: “Every `A∈𝔄^G` is matter-even” (`T/RCS1.md:59`). Its status block distinguishes field-algebra odd vectors from representations of the observable algebra, which “has no intrinsic odd subspace” (`T/RCS1.md:9`). R-CS remains a choice, not an adoption (`T/RCS1.md:5`).

- **Straight-string successes and obstructions are already separated.** Locked U-law states have string denominators that “vanish for every `x,e,r≥1`” (`T/RCS1.md:92`). The alternating empty-matter construction supplies another case (`T/RCS1.md:96`: “Let `ω_AB=Φ_AB∘E`”). Under existence, transverse disjointness, and tick-equivalence hypotheses, Corollary 9 makes bands “flat in both transverse directions” (`T/RCS1.md:120`). These are frozen conditional results (`T/RCS1.md:5`).

- **Cross-species speed equality was already distinguished from scale transfer.** Frozen LZ1 leaves “One common speed for all relevant propagating species” open (`T/LZ1.md:154`). The Lorentz consolidation records that “no symmetry fixes the ratio of two species’ dressed speeds” in its stated setting (`ref/pr10125/docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:21`). Its status is “author statements for review” (`…/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:11`).

- **Finite-region, finite-register local-observable approximation.** A supplied SU(3) Hamiltonian has explicit spatial and Peter–Weyl cutoff errors. Their combination is “independent of total lattice size,” but gives “No claim of a uniform all-energy fixed-R approximation” (`ref/main/docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75`). Boundary sectors are retained: the cutoff “does not project onto a boundary singlet” (`same file:83`). Source status is “conditional-support” (`same file:14`); its ledger says `"effective_status": "unaudited"` (`ref/main/docs/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`).

- **Separated correlations and contact observables already have distinct examples.** The supplied weak-window SU(3) note gives separated, polynomially normalized correlations smaller than every fixed power: “the right side is `o(ell^M)`” (`ref/main/docs/GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md:64`). At its Haar start it also constructs “Gaussian white-noise finite-dimensional distributions,” without claiming a dynamical limit (`same file:85`). Source status is “conditional-support” (`same file:17`); ledger status is `"unaudited"` (`ref/main/docs/audit/data/ledger/ga/gauge_wilson_weak_window_quantitative_bounds_and_haar_contact_fdd_bounded_theorem_note_2026-09-07.json:32`).

- **Relative Wilson-loop comparison has a native supplied-model example.** The finite-clock Villain note gives separated-loop ratios converging to the Maxwell current functional, with a growing clock alphabet (`ref/main/docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md:4`: “`beta=64L^4 and N=8beta`”). Its errors “remain relative errors even if each Wilson expectation tends to zero” (`same file:544`). This is bounded support (`same file:32`: “bounded-support”); the ledger is `"unaudited"` (`ref/main/docs/audit/data/ledger/fi/finite_clock_direct_maxwell_scaling_and_coulomb_wilson_interactions_bounded_theorem_note_2026-09-14.json:27`).

- **Creutz diagnostics predate this lane, without its comparison theorem.** The confinement note reports “Creutz ratio `χ(2,2) = 0.226`,” explicitly “dominated by short-distance perturbative contributions” (`ref/main/docs/CONFINEMENT_STRING_TENSION_NOTE.md:141`). Its status is “bounded support note / qualitative confinement consistency” (`same file:6`).

**Failed attempts on file.**

- **Transported linear block fermions.** ZM1 Attack 1 fails at “`Psi_u` is a fermion field”; Z3 and Z3′ force off-representative coefficients to vanish (`T/ZM1.md:375`).

- **Recovering the free comparison through classical links.** Attack 2 fails at “in some state the link operators act as c-numbers.” The recorded coherence bounds exclude that particular criterion, while “The error bounds of Theorem Z2 have not been transferred” (`T/ZM1.md:377`).

- **Conserved-projection renormalisation.** Attack 3 does not establish its projection classification or rank inference. “Boundary charges or functions can cancel link dependence” (`T/ZM1.md:379`). It concerns a subspace variant: “not an attack on ZM1-I1 as stated” (`T/ZM1.md:381`).

- **Finite moments implying the continuum comparison.** GA2_Y2 records the failing inference: finite-list agreement “does not control the other observables, scales, or errors” (`T/GA2_Y2.md:9`). Even zero cube diagnostic defect is insufficient: “zero SC-loop defect does not establish SC” (`T/GA2_Y2.md:138`).

- **Three small-coupling-window attacks.** The cube product is U(1)-blind; changing a bare angle does not remove the coherence bounds; and the product-copy estimate assumes alignment absent from the open block-map problem. The note identifies the latter failing step as “block states are aligned products” (`T/GA2_Y2.md:161`).

- **Charged-sector shortcuts.** Pair spectra require an unspecified inference and assumed factorization; Dirac clouds lack “fixed weights or representation” (`T/RCS1.md:204–205`, table rows R-CS^pair and R-CS^Dirac). The universal string kill attempt fails because matter-filled hops can act on distant ray links: “No general conservation theorem is supplied” (`T/RCS1.md:222`).

- **Unallocated multiscale error accumulation.** The YM extraction port records that summing `r` exponential errors yields `r` times the error, not the original bound with unchanged constants. Its missing absorption is “an open supplier estimate” (`Y/port/p9b-extraction.md:563`).

**Overlap with this lane’s results.**

- **Lemma A and A1–A2 — EXTENDS R-GI.** Prior R-GI treats charged two-point functions with singleton embedding sets (`T/ZM1.md:363`: “`S_X = {x_X}`”). The draft treats multi-time data with “(G1) alone” and general finite embedding sets (`T/ZM1_OBS_DRAFT.md:144`).

- **Lemma B — DUPLICATES RCS1 Theorem 4 for evenness; EXTENDS its block-map application.** The prior statement is “Every `A∈𝔄^G` is matter-even” (`T/RCS1.md:59`). The draft explicitly says “rebuilt from `RCS1.md` Theorem 4” and adds invariant-algebra preservation under representative-site maps (`T/ZM1_OBS_DRAFT.md:442`).

- **Lemma D — NEW statement found in these searches.** The draft says invariant data determine “the covariant structure on `H_phys`” and nothing in its orthogonal complement (`T/ZM1_OBS_DRAFT.md:443`). The earlier evenness statement alone does not supply this reconstruction (`T/RCS1.md:59`).

- **Theorem C — NEW statement found in these searches.** The twist family preserves invariant data while shifting charged quasi-energy origins; “slopes are unchanged” (`T/ZM1_OBS_DRAFT.md:444`). The draft expressly includes R-CS^str sectors (`same line`).

- **Theorem F — EXTENDS the referee’s on-site rigidity. Corollary F1 — DUPLICATES it.** Prior ZM1 already forces exact same-site equality (`T/ZM1.md:367`). F1 identifies itself as “the referee’s consequence”; F2 extends the conclusion to summed composite correlations under absolute convergence (`T/ZM1_OBS_DRAFT.md:225–227`).

- **Lemmas S and S′ — EXTENDS the free comparison to a conditional spectral-transfer statement.** Prior ZM1 gives the specified free comparison (`T/ZM1.md:282`: “this restricted comparison has `p = 2`”). The draft handles abstract bands and several branches, with branch-weight and gap hypotheses: “the sets of branch speeds … coincide” (`T/ZM1_OBS_DRAFT.md:243`). This does not duplicate a theorem establishing common speeds across species.

- **Lemma V and W1–W3 — NEW general comparison statements found; existing ingredients and diagnostics.** The draft proves absolute-budget vacuity (`T/ZM1_OBS_DRAFT.md:203`: “every candidate meets” the budget), sharp-grading loop vanishing, and normalization identities (`same file:447`: “Creutz ratios cancel perimeter and corner terms exactly”). Earlier work has small correlations and Creutz measurements, but those are narrower results (`ref/main/docs/GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md:64`; `ref/main/docs/CONFINEMENT_STRING_TENSION_NOTE.md:141`).

- **Theorem E — EXTENDS the prior string obstruction at the data level.** Prior Corollary 9 assumes limit-sector disjointness and tick equivalence (`T/RCS1.md:120`). The draft establishes finite-string vanishing for unequal far endpoints in every stated gauge-invariant background: “If `y ≠ y'`” the expectations vanish (`T/ZM1_OBS_DRAFT.md:269`).

- **Five classes and ranking — NEW assembled package found.** The draft supplies “definition, detection results, budget, ZM1-I1 form, downstream supply and four-test table” (`T/ZM1_OBS_DRAFT.md:449`). Individual ingredients already occur in SC, R-CS^str, and the main observable notes above.

- **CONTRADICTS — none found.** The draft reports “None to any frozen result” (`T/ZM1_OBS_DRAFT.md:451`).

**Missed inputs.**

- **Finite-clock relative loop ratios.** Add this as a native worked comparison for class (b). It supplies explicit self-energy cancellation and relative errors when individual loop expectations vanish (`ref/main/docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md:544–550`: “cancels the Gaussian self terms exactly”). It would add a separate normalization option; its growing alphabet remains explicit (`same file:4`: “`N=8beta`”).

- **Local Peter–Weyl approximation.** Use its spatial tail, energy-dependent cutoff error, and boundary-sector witness when specifying class (a)’s resources. It would replace an unpriced finite-register approximation with a quantified component: “First choose `r` … then choose `R`” (`ref/main/docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75`). It does not identify those truncations with either five-mode register.

- **Contact versus separated limits.** Use the Haar contact construction to distinguish what separation-envelope data and overlapping smeared data retain. Its separated-smearing theorem “says nothing about overlapping smearing regions” (`ref/main/docs/GAUGE_WILSON_WEAK_WINDOW_QUANTITATIVE_BOUNDS_AND_HAAR_CONTACT_FDD_BOUNDED_THEOREM_NOTE_2026-09-07.md:77`), while its contact variance survives (`same file:83`: “for `f=1` it is exactly1 at every `n`”).

- **Failure of absolute summability in a supplied massless comparator.** The massive-determinant/noncompact gauge note gives plaquette covariance “not absolutely summable” in its stated `d≥3` setting (`ref/main/docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:236–238`). This would qualify applications of F and S to massless gauge composites, whose hypotheses require summability (`T/ZM1_OBS_DRAFT.md:217–218`, `231`). The comparator remains `"conditional-support"` (`main note:828`) and `"unaudited"` (`ref/main/docs/audit/data/ledger/ma/massive_wilson_loop_curvature_noncompact_covariance_and_compact_defect_bounds_bounded_theorem_note_2026-09-14.json:27`).

- **YM’s existing observable interfaces.** Class (e) should be compared with H-BLOCK’s joint block/smeared state requirement, which is “not a consequence of curvature cumulant bounds” (`Y/port/p8b-limits.md:57`). This would state precisely what its weak-* compactness construction still needs to match on the YM side.

**Consumers.**

- **ZM1-I1.** Its immediate need is a precisely defined comparison class and budget, with four tests and selection still pending: “ZM1-I1 is not worked until then” (`T/TOE_ASSEMBLY.md:227`). This consumer does not yet require an existence theorem for the chosen class.

- **ZM1’s spatial comparison and tower.** It needs control of separated local observables and compatible maps. The existing residual explicitly includes “arbitrary separated local block observables” and says the maps are not shown “to compose into a tower” (`T/ZM1.md:268`).

- **LZ1-i.** Its weakest useful input here is dynamical comparison with enough spectral weight to transfer each relevant species’ slopes. The draft requires weights “bounded below near the node” (`T/ZM1_OBS_DRAFT.md:247`). Common speed across species remains a separate requirement (`T/LZ1.md:154`: “One common speed … remains open”).

- **MT1-S[R-CS^str] and CH1’s charged prescription.** They need a specified odd label and charged-sector comparison capable of testing a three-direction cone. The prior open target asks for “a Clifford-node band” (`T/RCS1.md:214`); class (d) supplies only axial information: “Transverse speeds are not in the data” (`T/ZM1_OBS_DRAFT.md:383`).

- **GA2, Y2, and Y5.** They need a fixed observable dictionary with errors propagated across scales. GA2’s target error is “`O((a/r)^p) + O(g_i(r)^4)`” (`T/TOE_ASSEMBLY.md:397`). Finite-list matching alone is insufficient (`T/GA2_Y2.md:9`).

- **T0-start[G], T0-rate, and YM extraction/limit items.** The interface needs a pinned start class and topology, uniform CT1–CT4 estimates, and quantified correlator errors (`T/GA2_Y2.md:169`: “the class and topology must be pinned”). H-BLOCK needs the joint observable state (`Y/port/p8b-limits.md:57`); extraction additionally needs support admission and allocated tail errors (`Y/port/p9b-extraction.md:226–227`: “printed rates” and “common-box margins”).