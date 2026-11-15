**Searches run.**

- Terms: `electroweak`, `FMS`, `Elitzur`, `Higgs`, `symmetry.breaking`, `stabilizer`, `rishon`, `thin.transport`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and the TOE folder, including drafts, referee reports and `LIT_*.md`. Followed hits with searches for theorem names, claim IDs, `10062`, `10082`, `9969`, classicality and inverse layers.
- Read `ref/README.md` first. Its corpus map identifies “Ledger rows: main/docs/audit/data/ledger/” and says each consolidation PR “has a *CONSOLIDATED* note” (`ref/README.md:2–3`).
- Path abbreviations below: `T/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`; `M/` = `ref/main/docs/`; `L/` = `ref/main/docs/audit/data/ledger/`; `F` = `ref/pr10129/docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- The brief narrows the first task to a gauge-invariant breaking statement and whether “any state of the law” realizes it (`briefs/ew1.txt:2`). The assembly target additionally requires the VC1 vacuum, vector spectrum, scalar and weak scale: “three massive weak bosons and a massless photon” (`T/TOE_ASSEMBLY.md:459`).

**Already in the repo.**

- **Conditional electroweak direction.** The older Higgs-hypercharge note derives the neutral annihilator, `Q = T_3 + Y/2`, after supplying a doublet and neutral VEV (`M/EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md:61`). Its VEV direction is an “admitted SM convention”; its magnitude is an “admitted external observable” (`:105`, `:120`). Ledger: `bounded_theorem`, `"audit_status": "unaudited"` (`L/ew/ewsb_pattern_from_higgs_y_note_2026-05-02.json:17`, `:6`).

- **Formal mass-matrix algebra.** The defined quadratic form has `rank(M0) = 1` and annihilator `span_C{T3 + Y}` (`M/EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md:119`, `:147`). It supplies neither dynamics nor particles: “No covariant derivative, field, action, or physical system is being defined” (`:54`); its mass symbols “are formal labels only” (`:171`). Ledger: `positive_theorem`, unaudited (`L/ew/ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26.json:17`, `:6`).

- **Existing synthesis does not remove the Higgs admission.** The unified matter/EWSB harness explicitly assumes “a scalar field Φ” with a nonzero lower-component VEV (`M/UNIFIED_MATTER_CONTENT_EWSB_HARNESS_THEOREM_NOTE_2026-05-03.md:106`). Its EWSB conclusion is labelled “conditional EWSB on derived rep” (`:147`). Ledger: `positive_theorem`, unaudited (`L/un/unified_matter_content_ewsb_harness_theorem_note_2026-05-03.json:17`, `:6`).

- **Formal scalar minimum.** The radial quartic note proves a “unique global minimizer” for a defined polynomial (`M/HIGGS_MECHANISM_NOTE.md:18`). It explicitly says, “No physical interpretation is part of the theorem” (`:5`). Ledger: `positive_theorem`, unaudited (`L/hi/higgs_mechanism_note.json:17`, `:6`).

- **Composite-Higgs candidate and mean-field threshold.** The proposed multichannel scalar leaves three named obligations: extending Z3 to quark bilinears, equal condensate magnitudes, and the strong-coupling magnitude (`M/COMPOSITE_HIGGS_MECHANISM_NOTE_2026-05-03.md:32`, `:34`, `:37`). It is “NOT a closing derivation” (`:42`); its ledger type is `open_gate`, unaudited (`L/co/composite_higgs_mechanism_note_2026-05-03.json:17`, `:6`). Separately, the supplied NJL mean-field potential requires `G_eff > G_critical := u_0² / 4` (`M/V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md:83`). Its leading-order estimate lies on the “symmetric side” (`:108`). Ledger: `bounded_theorem`, unaudited (`L/v_/v_eff_total_njl_style_bounded_theorem_note_2026-05-10.json:17`, `:6`).

- **Representation and local-algebra boundaries.** The singlet-to-doublet bridge note states `Hom_SU(2)(1, 2) = 0`; a singlet cannot derive the full doublet (`M/HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md:37`, `:42`). Ledger: `no_go`, unaudited (`L/hu/hunit_to_ewsb_doublet_representation_no_go_note_2026-06-15.json:17`, `:6`). The single-site CCR obstruction expressly leaves “any collective/effective bosonic limit” outside scope (`M/NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md:101`). Its ledger is also `no_go`, unaudited (`L/no/no_per_site_bosonic_ccr_theorem_note_2026-05-02.json:17`, `:6`).

- **Weak-scale identification remains conditional.** The hierarchy bridge supplies `H_EW` as a physical hypothesis (`M/HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md:44`). Its output is “assigned, conditional on H_EW” (`:65`); it does not promote the numerical match “to a derived theorem” (`:72–73`). Ledger: `bounded_theorem`, unaudited (`L/hi/hierarchy_formula_ew_vev_observable_identification_bridge_bounded_note_2026-05-26.json:17`, `:6`).

- **Exact invariance, centre and stabilizers.** CH1 proves that a covariant expectation “vanishes if ρ has no trivial summand” (`T/CH1_5O.md:38`). Its centre theorem says `Z` fixes every finite-dimensional even operator space (`:84`). It also constructs a proper stabilizer “exactly `HZ`” (`:98`), while warning that this “does not show that the law realizes this order” (`:102`). Status: frozen; the listed results are “Proved under those inputs” (`:5`, `:9`).

- **Coherent registers and inverse updates.** CH1-5O-E′ constructs irreducible `R_k^-`, with link operators “sums over the `k` copies” and mean `kO` (`T/CH1_5OEP.md:30–36`). Its Theorem 3 makes the tick followed by inverse layers “the identity” (`:62`). These are frozen “author-side checks, not independent review or retained status” (`:5`, `:7`).

- **Finite-register transport tools.** GA2 gives the Majorana identity for `𝐔†𝐔`, the bounded-grading floor, the `κ≤1/2` U-law bound, and copy averaging that divides fluctuations and commutators by `k` (`T/GA2_Y2.md:62`, `:76`, `:88`, `:92`). It explicitly does not establish “a continuum theory” (`:7`). CH1-5U-q separately proves the stronger matrix-norm statement `||u||,||v||≤1/2` (`T/CH1_5UQ.md:106`); its status is frozen and conditional (`:5`, `:9`).

- **Stationary witnesses.** VC1 supplies gauge averaging commuting with the tick and cell lifts (`T/VC1_5.md:41`), an automorphism-invariant trace (`:65`), dark O-law witnesses (`:77`), and U-law witnesses “at every filling” (`:105`). Its status explicitly does not establish “the full VC1 vacuum” (`:5`).

- **Literature already digested locally.** `LIT_HIGGS.md` separates stabilizer-adapted composites from particle poles: “its identification of particle poles needs dynamics” (`T/LIT_HIGGS.md:3`). It also flags the precise quantum-composite issue: “FMS starts with commuting classical Higgs coordinates” (`:71`). This is a local literature record, not a discharged proof obligation: “No literature citation below discharges a repo proof obligation” (`:3`).

**Failed attempts on file.**

- **Local VEV, local stratum and spectral definitions.** EW1 records that R-VEV vanishes in every symmetric state; R-ST without alignment calls confinement-like data broken; R-SPEC restates the target. Their recorded failing steps are respectively “Test 3 fails,” “Test 3 fails,” and “Test 1 fails” (`T/EW1.md:88`, `:92`, `:94`). R-A and R-L have earlier recorded reading failures (`:90`).

- **Composite and hierarchy shortcuts.** The multichannel proposal stops at NO1–NO3 (`M/COMPOSITE_HIGGS_MECHANISM_NOTE_2026-05-03.md:32–37`). The NJL leading-order route has no nontrivial root on its stated surface (`M/V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md:108–109`). The hierarchy formula still needs the supplied `H_EW` identification (`M/HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md:44`).

- **Mirror condensate as a weak-scale mechanism.** The consolidation’s logged #9974 finds that “unbroken colour forces v = f”; the proposed misalignment angle runs toward colour breaking (`F:477`). Logged #9969 likewise reports “no misalignment angle (v = f)” and no established weak-scale mechanism within the stated content (`F:475`).

- **Gapping channel as the electroweak Higgs.** Logged #10062 obtains `M_u = M_nu = Y v_u`, `M_d = M_e^T = Y v_d`, “hence `|V_CKM| = 1`.” It also leaves doublets and triplets degenerate (`F:487`). These are failures of that specified channel identification.

- **Shared-hypercharge slab route.** The logged chain ends with a Landau pole below its supplied cutoff and incompatible layer requirements: “46 to 58” versus “at most about 5 to 6” (`F:404`). Its consolidation calls these “supplied-model estimate[s]” (`F:406`).

- **Prior gauge-window arguments.** GA2’s three attacks stop at a U(1)-blind cube raising no grading, a small angle making a fine link classical, and assuming “block states are aligned products” (`T/GA2_Y2.md:161`). CH1’s Ward-identity shortcut stops at inferring “one massless physical channel per generator” (`T/CH1_5OEP.md:130`).

- **EW1’s fixed-register attacks.** Freezing `k` leaves `C_F(L)/k` uncontrolled; a one-link floor does not bound block transport; state-moment classicality does not force commuting operators. The file names those failing steps explicitly (`T/EW1.md:261`, `:262`, `:263`).

- **EW1’s U-law attacks.** Copying the O construction fails at near-group one-link transport; universal grading floors miss neutral data and growing cuts; collective transport lacks an exhibited state. Exact recorded phrases: “one L5-U link can be prepared with transport near a group element,” “every R-FMS alignment operator raises a bounded grading,” and “such a state of L5-U is exhibited” (`T/EW1.md:352`, `:354`, `:356`).

- **EW1’s own-tick attacks.** Known witnesses do not establish the required data; time averaging lacks preservation of `(O), (A) and (T)`; HEAT remains open and its odd-link argument misses even FMS transport (`T/EW1.md:374`, `:376`, `:378`).

- **Draft errors repaired on file.** Same-order reverse evaluation gives `1` where the adjoint gives `0` in the stated example (`T/EW1_REFEREE.md:172`). The omitted-classicality example satisfies `(O)` and `(A)` at every tolerance but “fails (C)” (`:252`). The frozen file adds `(C)` to the affected bounds (`T/EW1.md:302`, `:321`).

**Overlap with this lane’s results.**

EW1 has run: “FROZEN 2026-11-06.” Its reading remains “proposed, not adopted,” and its proofs do not have retained status (`T/EW1.md:5`, `:7`).

- **Theorem 4.1 — EXTENDS CH1’s centre theorem.** CH1 already says `Z` fixes even operator spaces (`T/CH1_5O.md:84`). EW1 applies this to carried bosonic composites on both laws and excludes literal `K = K_em`: “no state satisfies R-FMS with `K = K_em`” (`T/EW1.md:114–116`).

- **Lemma 4.2 — NEW.** Its simultaneous-adjoint obstruction leaves a ten-dimensional intersection rather than nine (`T/EW1.md:130`). The older #9974 statement, “No weight of the 45 is a colour-singlet doublet,” concerns a narrower representation-content question (`F:477`).

- **Propositions 4.3–4.4 — NEW.** They give `Stab(q_ψ) ∩ H = K_em` but show even site/adjoint product data retain an extra `U(1)_λ` (`T/EW1.md:155`, `:179`). The earlier constructed stabilizer was `HZ`, a different target (`T/CH1_5O.md:98`).

- **Lemma 5.1 — EXTENDS coherent-copy estimates.** The predecessor gives means and vector-norm fluctuations (`T/CH1_5OEP.md:34–38`). EW1 controls arbitrary ordered degree-`d` products by `d²/k` (`T/EW1.md:199`).

- **Lemma 5.2 — DUPLICATES inverse-update stationarity; EXTENDS the symmetry construction.** The identity update already makes “Every state” stationary (`T/CH1_5OEP.md:62`). EW1 verifies symmetry for its particular nontracial product/gauge-average state (`T/EW1.md:205–209`).

- **Theorem 5.3 — EXTENDS coherent-register realization.** It combines that machinery with the new site datum and all four R-FMS conditions. Its precise scope is “across the family of laws, not Q-EW for one fixed register” (`T/EW1.md:217`). The predecessor realizes finite loop data (`T/CH1_5OEP.md:49–54`).

- **Lemmas 5.4 and 5.4′ — EXTEND the rishon identity/rank bound.** The prior identity is in GA2 Theorem 2.5 (`T/GA2_Y2.md:62`). EW1 derives a vector floor of `9`, then a representation floor of `d−1` (`T/EW1.md:238`, `:244`). Scope remains “one link only” (`:258`).

- **Lemma 6.1 — DUPLICATES CH1-5U-q Theorem 4.2’s one-link norm result.** Both state the matrix bound `1/2` (`T/EW1.md:271`; `T/CH1_5UQ.md:106`).

- **Lemma 6.2 — NEW.** The adjoint fidelity bound is `F_ω(u) ≤ 3/10` (`T/EW1.md:279`). The predecessor’s `κ≤1/2` uses a different coherence diagnostic (`T/GA2_Y2.md:88`).

- **Lemma 6.3a — EXTENDS GA2’s unit-charge floor.** GA2 assumes `[E,Y]=Y` (`T/GA2_Y2.md:76`). EW1 allows `[E,Y]=qY` and replaces the chain length by `⌈K/|q|⌉` (`T/EW1.md:295–297`).

- **Theorem 6.3′ — EXTENDS that floor to charged FMS alignment.** It requires a specified cut, nonzero charge and `(O), (C) and (A)` (`T/EW1.md:302`). This is not a universal block-scale obstruction: EW1 records that its floor decays with cut size (`:354`).

- **Lemma 6.4 — EXTENDS empty-sector stationarity.** VC1 already observes that “every cube gate acts as the identity” on empty matter (`T/VC1_5.md:193`). EW1 generalizes the stationarity statement and adds the sharp-matter bound on charged orbit components (`T/EW1.md:319–321`).

- **Proposition 6.5 — NEW.** Neutral data can meet the Lie-algebra target, while the central `Z_5` obstructs the stronger group target (`T/EW1.md:330–331`). Its distinction is explicit: “EW at the Lie-algebra level is not excluded by neutral data” (`:331`).

- **Lemma 7.2 — NEW.** For its stated cut-link paths, trace-state realization at every tolerance forces `Stab(v) = G` (`T/EW1.md:366`). VC1 previously supplied trace stationarity, not this FMS obstruction (`T/VC1_5.md:65`).

- **CONTRADICTS — the superseded unrestricted draft bounds only.** The referee records the old hypotheses as `(O)` and `(A)` without `(C)` and gives a counterexample (`T/EW1_REFEREE.md:129`, `:252`). The frozen theorem explicitly requires `(C)` (`T/EW1.md:302`). The older supplied-doublet algebra is not contradicted; it assumes the Higgs carrier and VEV (`M/EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md:18–24`).

**Missed inputs.**

- **Add the older conditional EW algebra as a downstream interface.** It identifies exactly what extra carrier and kinetic interpretation would be needed before using the formal mass readouts. The existing matrix note supplies “formal labels only” (`M/EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md:171`); EW1 itself leaves “the spectrum and the scalar channel” open (`T/EW1.md:11`). This would clarify the remaining bridge, not close it.

- **Carry the failed gapping-channel identification into FL2 planning.** Any proposal equating EW1’s composite with that specific 10-channel must confront “hence `|V_CKM| = 1`” (`F:487`). It would add a concrete exclusion test beyond stabilizer matching.

- **Carry the weak-scale admissions explicitly.** The hierarchy bridge requires `H_EW` (`M/HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md:44`), while the logged condensate route gives `v=f` (`F:475`). These would prevent treating an orbit amplitude or condensate scale as a derived hierarchy.

- **Use the singlet/doublet distinction when pursuing the scalar channel.** `Hom_SU(2)(1,2)=0` blocks promoting a radial singlet into a full Higgs doublet (`M/HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md:37`). It would change the required representation check.

- **Use CH1-5U-q’s full matrix bound and frozen witnesses.** Its bound is exactly `||u||,||v||≤1/2` (`T/CH1_5UQ.md:106`), and its frozen states have sharp `N_x=n` (`:86`). These provide additional named inputs for testing U-law candidates against EW1’s sharp-matter restriction (`T/EW1.md:321`).

**Consumers.**

- **FL2.** This is the explicit direct consumer: “EW1 -> FL2” (`T/TOE_ASSEMBLY.md:588`). Its weakest usable interface needs a realized electroweak sector and a clear distinction between computed masses and registered values; FL2 requires each parameter to be “law-level” or “registered data” (`:471`). A varying-register stabilizer construction alone does not supply that interface (`T/EW1.md:217`).

- **Assembly T6.** It needs EW1’s physical breaking statement on the same law and vacuum as the other parts: “All parts are proved for one law `L` … and one vacuum” (`T/TOE_ASSEMBLY.md:650`). T6 explicitly consumes “EW1 (breaking)” (`:659`). The stated target includes vector masses, a photon, scalar content and scale (`:459`).

- **RCS1’s dressing attack.** It already cites EW1’s one-link coherence obstruction. The weakest input is the scoped failure of a lattice-scale c-number-unitary approximation; RCS1 explicitly says this does not exclude “collective deconfinement” or “a different dressing” (`T/RCS1.md:218`).

- **VC1/HEAT follow-up.** The needed result is a fixed-register, own-tick stationary realization or obstruction. EW1 names precisely that open question (`T/EW1.md:370`) and says its answer “bears on VC1 and on HEAT” (`:380`).

- **YM branch.** No direct EW1 consumer found. The documented direction is the reverse: “T0 … -> GA2” (`T/TOE_ASSEMBLY.md:584`). The YM comparison record rejects a Higgs scaling limit because it “fails the pure-Wilson/NT2 target” (`ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library/route-compare-2.md:112`).