# A34 fourth hostile review: A28, A30, A31, A32, and MORNING_DRAFT (03:27 version)

**Provenance.**
- Primary files read: BRIEF; A16, A21 (both) and A29 reviews; LOG (headers, K1, the A28–A32 entries); the full reports of A28, A30, A31 and A32; A25's layout section; the scripts and outputs behind every number I question (A28 `c4_scales`, A30 `q1_dirac*`, `q2_seal`, `q2_dissolve`, `q4_horizon`, `q1_2d` porous/disk outputs, A31 `c1b`, `c2*` outputs, A32 `c5_tick_vs_grid`); the coordinator's `verify_A28_edge.py`, `verify_A30_capture.py`, `verify_A31.py`, `verify_A32.py`, `zeno_wall_1d.py` (as evidence only).
- I had read all three earlier reviews, so I am not independent of them. I did not re-litigate their corrections except where noted (C51's wording, C75).
- Draft line numbers refer to `MORNING_DRAFT.md` as of 03:27 (367 lines, A32 text included). `MORNING_SUMMARY_DRAFT.md` (03:28) is reviewed briefly in C87.
- **A33 had not landed** when I finished (scripts only, no REPORT.md). It needs the same treatment when it lands.
- No git, no repo edits, no edits to other agents' files or the drafts. I wrote only into `c8/A34/`.

**What I ran** (1-minute load 1.7–4.5 at the runs, always below 6; `nice -n 10`; all four thread caps = 1; each run < 5 s, peak ≤ 198 MB).

| Script → output | What it checks | Key result |
|---|---|---|
| `c1_star_terms.py` | Do glued, homogeneous star terms beyond pairs keep an aligned vacuum calm? | Chiral three-spin star term T: covariant under the 24 glued turns to 1.4e-13; every aligned state an exact eigenvector (7e-16); still calm next to a +n or −n record (6e-16); orthogonal to every pair term (relative distance 1.000); its whole one-ripple block is 0, so it acts only on two-or-more-ripple states |
| `c2_staggered_capture.py` | A30's "speed-only" law; is Γ = 2t the best strength for massive waves? | Law at Γ = 2t holds for both surface terminations and both bands (≤ 8e-16). Best Γ for massive waves ranges 0.67–6.0; best capture = massless value at the same wavenumber (0.987/0.911/0.775/0.481), not a function of speed |
| `c3_blind_step_energy.py` | A31 D11: is a blind swap energy-neutral in calm surroundings? | Lone record: 0. Two adjacent −n records separating: −4J (exact ring). One −n record stepping off a flat face of a 3D jam: −20J. Dissolving a 27-record −n cube: −216J. +n contents: always 0 |
| `c4_zeno_optimum.py` | A32 D33 optimum at small chance per tick | c = 0.1: Jτ* = 0.0372 (A32's 0.050 is the lower edge of its search grid); small-c law τ* ≈ c/(2√2 J) (continuum optimum γ* = 2.828J, rate J/√2) |
| `c5_staggered_edge.py` | A28's edge floor for the staggered (KS π-flux) half-filled sea, left ARGUED by A28 | 3D boxes L = 8, 10, 12, planar wall: wall-star ν ∈ [0.015, 0.985], smallest many-body eigenvalue 1.3–1.5e-5 (stable); bulk 7-star 4.7–5.2e-6. Full rank: CHECKED |
| `c6_law_schedules.py` | A32 D8(a): which law-level phase patterns treat every site and turn alike up to a global time shift? | Only u = 0 (one shared tick) and u = (τ/2)(1,1,1) (a two-sub-grid checkerboard) |

---

## 1. Verdicts per lane

| Lane | Verdict | One-line reason |
|---|---|---|
| **A31** assembly v2 | **Holds with narrowing** | D1, Theorem S, D5, D7 and K5's arithmetic are right. "Calm forces Heisenberg" holds only for pair terms (a glued three-spin star term keeps the aligned vacuum calm, C56); "no cone" is single-ripple and product-vacuum only (C57); "blind swaps are energy-neutral in calm surroundings" fails for −n records in clusters (C60); D10 collides with A25's all-places layout and with A30's reading RA (C61). |
| **A30** black hole | **Holds with narrowing** | Rate law, threshold theorem, per-tick law, seal algebra, leak lifetimes and horizon arithmetic check out (one stray number: "6 km", C69). The speed-only law holds at Γ = 2t (more generally than A30 tested), but Γ = 2t is not the best strength for massive waves (C65). "Lapse keeps running" is linear-order only, i.e. not for black-hole-sized jams (C66). |
| **A28** gated formation | **Holds with narrowing** | Void quietness, no-signalling and the GHZ contrast are right. The edge floor is EXACT for the uniform sea; I CHECKED it for the staggered sea (C72). The heating chain's arithmetic is right but one input is unsourced (C73). "A void's possibilities evolve by the smooth change alone" holds only on average over distant outcomes (Q1, C74). The Q4 consequence is a reading (C75). |
| **A32** tick in Option R | **Holds with narrowing** | The re-timing lemma is correct to first order (re-derived); the continuous limit holds per finite window (C81). D8's "must be global" holds only without global time shifts (a checkerboard also qualifies), and "neighbourhood ticks need memory" is construction-by-construction (C77). D33's small-c optimum is a grid artifact (C79). D20's "at most half" needs left–right-symmetric weights (C82). D21's clock result assumes Dirac-like matter, which over the calm background needs A31's painted pattern (C80). |
| **A33** | **Not reviewed** | Not landed at time of writing. |
| **MORNING_DRAFT** | **Needs changes: 1 BLOCKER, 11 MAJOR** | The BLOCKER is section 9's "gravity's clocks keep running inside" (C66). The MAJORs: missing conditionals on the A31 headline (C56–C59, C61), the catching law (C65), the seal-versus-motion conflict (C67), and the new A32 tick text (C77–C80). Also one lane-level MAJOR (C60) and the one-page summary (C87). Cross-reference numbering collides (C85). |

---

## 2. Findings (continuing the numbering)

### A31

**C56. MAJOR. "Calm forces Heisenberg" is a pair-term result; the draft states it for every rule.**
- **Claims.**
  - A31:62 and D2 (A31:238): "Calm forces K = 0. Once any record holds the content −n, it also forces D = 0, so H = J Σσ·σ (EXACT)."
  - Draft:92: "a change that treats every spot and turn alike must reduce to one simple form".
  - Draft:297: "the only rule that treats every spot and turn alike and leaves it calm is the simplest 'align with your neighbour' rule."
- **What is right.** D1 and D2 are correct inside A31's stated class (homogeneous, glued, nearest-neighbour *pair* terms). I re-derived the bond invariants (dim 5) and the double-flip and single-flip arguments.
- **What is wrong.**
  - (i) Campaign 7's sentence 2 is "star-local (a sum of nearest-neighbour terms)", and the framework has used star terms before (weight-5/7 star terms, Campaign "one dynamics clause"). Beyond pairs, D2's uniqueness fails.
    - **Counterexample (CHECKED, `c1_star_terms`).** T = Σ_x Σ_{octants (s₁,s₂,s₃)} s₁s₂s₃ σ_{x+s₁e₁}·(σ_{x+s₂e₂} × σ_{x+s₃e₃}). It is homogeneous, star-local, covariant under the 24 glued turns (1.4e-13), nonzero, and orthogonal to every pair term (relative distance 1.000 from the pair span; EXACT by twirling, since T is SU(2)-invariant). Every aligned state is an exact eigenvector (7e-16), also next to a +n or −n record (6e-16).
    - **General reason (EXACT, Schur).** Any SU(2)-invariant term acts as a number on the fully symmetric subspace of its support, which contains |m⟩^⊗; next to ±n records, compression plus S_n conservation keeps |n⟩^⊗ an eigenvector. So every SU(2)-invariant star term keeps the aligned vacuum calm.
  - (ii) Even for pairs, D = 0 needs a record of content −n; with only +n records, J + D survives (A31:62 says so; the draft drops it).
  - (iii) "Align with your neighbour" presumes the sign of J; for J > 0 the aligned state is calm but is the *top* of the spectrum.
- **What survives (EXACT).** D3's single-ripple conclusion: for any translation-invariant H over a translation-invariant product vacuum on one qubit per site, single ripples form one analytic band, so no cone. T even leaves the one-ripple sector untouched (off-diagonal norm 0) and acts only on two-ripple states (norm 27.7).
- **Corrected wording (EXACT).** "Among glued, homogeneous rules built from neighbour *pairs*, calm over an aligned vacuum forces K = 0, and any −n record also forces D = 0. Glued star terms on three or more sites (e.g. the chiral term T) keep the aligned vacuum calm too. In every case, single ripples over a calm product vacuum form one analytic band."
- **Draft.**
  - Line 92, replace with: "- **Only slow-particle ripples over the simplest calm background (A31).** Over a calm empty background where every spot points the same way, a change built from pairs of neighbours that treats every spot and turn alike must reduce to one simple form once any record holds the opposite content (exact). Rules with terms on three or more spots of a neighbourhood keep that background calm in more ways (my check). Either way, single ripples behave like slow, heavy particles, never like light (exact for single ripples). Over that background, light-like ripples need a fixed pattern of plus and minus signs on the rule (section 10); a background whose spots share their possibilities is open (A33)."
  - Line 297, replace with: "- **The sharp limit (exact, checked; single ripples).** Take empty space where every spot points the same way. Among rules built from pairs of neighbours that treat every spot and turn alike, only the plain 'line up with your neighbour' rule keeps it calm once any record holds the opposite content. Rules with three-spot terms keep it calm too (my check), but in every such rule single ripples behave like slow, heavy particles, never like light. Groups of ripples, and backgrounds that do not all point one way, are untested here."

**C57. MAJOR. "Never like light" and "light-like matter needs a painted pattern" lose both of their conditions in the draft.**
- **Claims.**
  - Draft:21: "over the calm empty background this shape needs, a change that treats every spot and turn alike can only move ripples that behave like slow, heavy particles, never like light (exact, A31). Light-like matter needs a sign pattern painted onto the rule".
  - Draft:297: "Calm empty space needs every spot pointing the same way."
  - Draft:298: "**Light-like matter needs a painted-on sign pattern.**"
  - A31:254: "Bogoliubov cones need a non-calm vacuum … a vacuum that is not exactly stationary."
  - A31:356: "To get light-like matter, a fixed pattern of plus and minus signs must be painted onto the rule."
  - A31:161 K2(c): "So the calm emptiness is forced at matter's edges … (c) EXACT (combination)".
- **What is wrong.**
  - (i) **Single ripples only.** D3 is "EXACT at harmonic order" (A31:249), i.e. one ripple. Groups of ripples (bound states) are untested; A31 itself lists "composite excitations" as an open escape (A31:122). T in C56 is exactly the kind of term that acts only on groups.
  - (ii) **Product backgrounds only.** The same plain rule with J > 0 has an entangled, exactly stationary ground state (the antiferromagnet) whose ripples are linear, light-like (COMPARATOR: Anderson spin-wave theory; Néel order on the cubic lattice). So A31:254's "not exactly stationary" is misphrased: what fails is stationarity of the *product reference state*; the Bogoliubov vacuum is stationary. The true trade-off is: light-like ripples from the plain rule need an entangled background, which is full rank on stars (ARGUED), so A28's edge floor makes it breed records next to matter.
  - (iii) **"Calm needs every spot pointing the same way"** is the definition of A31's class (row 20), not a result. Patterned product vacua with compass terms are A31's own open edge 5; entangled calm vacua are A33's search.
  - (iv) **"The calm empty background this shape needs"**: A28 makes voids quiet for any vacuum. The tidy background is needed only next to matter, and only via the edge floor (EXACT for free fermions; CHECKED for the staggered sea, C72), A24's ghost cost and heating bounds with J ~ E_P (ARGUED). A28's own exits (A12 windows, coarse records) remain. So K2(c)'s "forced … EXACT (combination)" is ARGUED (C62).
- **Corrected wording.** "Over a calm *product* background (every spot aligned), single ripples of any homogeneous glued change form one band with no cone (EXACT). Over that background, light-like single ripples need a law-level π-flux sign pattern (EXACT within the class). Entangled backgrounds can carry linear ripples without any pattern (COMPARATOR) but are full rank at matter's edges (ARGUED). Whether matter's edges force a calm product background is ARGUED."
- **Draft.**
  - Line 21, replace the bullet with: "- over the calm, all-pointing-one-way empty background, a change that treats every spot and turn alike moves single ripples only like slow, heavy particles, never like light (exact for single ripples; groups of ripples are untested). Over that background, light-like matter needs a sign pattern painted onto the rule, and in the version that keeps your gluing that pattern cannot keep the turns the gravity field's pattern keeps (proved). A background whose spots share their possibilities, instead of all pointing one way, can carry light-like ripples with the plain rule (a comparison from magnets, not adopted), but next to matter it gets recorded and heats (A28);"
  - Line 298, replace the bold lead with: "**Over that background, light-like matter needs a painted-on sign pattern.**"

**C58. MAJOR (draft); Theorem S itself holds. "Two separate supplied patterns" overstates it.**
- **Claims.**
  - Draft:301: "**Two patterns, not one (proved).** … So in the version that keeps your gluing, matter and gravity need two separate supplied patterns."
  - Draft:21 and :354: "that pattern can never be the same one the gravity field needs".
  - A31:200 and A31:356: "It lacks the quarter turns the field's layout has (proved)"; "the field's pattern keeps the grid's quarter turns and this one cannot".
- **What is right (EXACT; re-derived).**
  - A face-diagonal half turn about x fixes a plaquette through x and swaps its bonds in pairs, forcing flux +1. So no π-flux pattern is exactly kept by a face-diagonal half turn.
  - The maximal subgroups of O avoiding those six half turns are T and C4.
  - In the glued form, exact preservation is the right notion, because no on-site relabelling flips σ·σ (D5: spectra {1,1,1,−3} vs {3,−1,−1,−1}). So a projective realization through on-site relabellings of matter is impossible (EXACT).
- **What is wrong.**
  - (i) A31's own c2b (A31:142): "Tied to the layout, the joint symmetry is T: 12 of the 24 turns survive, and the joint structure is 1 of 16." So one *joint* supplied choice exists. The most symmetric π-flux pattern alone already keeps only T about sites, plus 12 elements that need a (1,1,1) shift (`out_c2b_stab.txt`); the standard KS gauge keeps only 4 (coordinator's check). Tying loses only those 12 screw/off-site elements. "Two separate patterns" is therefore not proved.
  - (ii) **Projective realization on the field side (OPEN).** Matter's best group is T plus the quarter turns and face-diagonal half turns *composed with a (1,1,1) shift*. The layout is not kept by a (1,1,1) shift (it swaps vertex↔cube and edge↔face roles). It would be kept if A25's field law had an internal symmetry exchanging those roles (a duality-type map). Then both could share one non-symmorphic group of order 24. A25 as built has no such map (ARGUED), so "never share" holds for A25 as built, not in general.
  - (iii) Wording: the theorem concerns face-diagonal *half* turns. A31:200 and :356 say "quarter turns"; that is wrong (the C4 case keeps quarter turns about one axis).
- **Corrected wording (EXACT + OPEN).** "No π-flux pattern is kept by a face-diagonal half turn (Theorem S). So, in the glued form, matter's pattern cannot be a covariant function of the field's layout; tied together they form one joint choice (1 of 16) that keeps only T. A field-side duality that composes with a (1,1,1) shift would allow a shared order-24 group; none is known for A25."
- **Draft.** Line 301, replace with: "- **The two patterns cannot be one pattern with all the field pattern's turns (proved).** The gravity field's 2×2×2 job pattern keeps certain half-turns of the grid; no sign pattern of the kind light needs can keep them. They can still be tied together as one supplied choice (1 of 16), but then the combined pattern keeps only 12 of the 24 turns. In the hop-only version they might share one label, which needs a piece not yet found."

**C59. MAJOR (draft). The hop-only version hides the pattern only if records' steps carry the signs.**
- **Claims.**
  - Draft:300: "**Signs on the hopping only.** This can be hidden from records, but the rule then favours one direction".
  - Draft:354: "or on the hopping only (one direction of the possibilities is favoured …)".
- **What is wrong.** A31's table (A31:107–108) and K1(c) (A31:160): with Option R's pattern-blind swap, records show the pattern (TV 0.37 in 2D, 0.10 in 3D). Only a signed swap hides it, "but then the step must know the matter pattern". So the record step, point 0's pattern-free selling point, carries the painted pattern too. Hiding also needs all contents and menus on the z axis (X-type records show it, TV 0.29).
- **Draft.**
  - Line 300, replace with: "- **Signs on the hopping only.** This can be hidden from records only if a record's step carries the same signs, so the step itself must know the pattern. The rule then also favours one direction of the possibilities, and 16 of the 24 turns are no longer treated alike."
  - Decision 17: see C64.

**C60. MAJOR (lane; affects decisions 13 and 19). A blind swap is energy-neutral only for a lone record, or for +n contents.**
- **Claims.**
  - A31:296 D11: "It is 0 for content −n in calm surroundings, by translation invariance (EXACT)."
  - A31:160 K1(b): "A swap changes ⟨H⟩ next to unrecorded excitations …, but not in calm surroundings with contents ±n."
  - A31:162 K3(c): "Blind swaps in calm surroundings do not [inject energy]."
  - A31:57: "The blind weight W = 1 is preferred: no back-action, and no energy change in calm surroundings (D11)."
- **What is wrong (EXACT arithmetic; CHECKED, `c3`).**
  - For calm product snapshots, ⟨σ_i·σ_j⟩ = n_i·n_j. So ⟨H_R⟩ = J(#bonds − 2·#(−n record ↔ unrecorded or +n contacts)).
  - Translation invariance covers only a record with no recorded neighbour before or after the step. A −n record joining or leaving a cluster changes the energy by 2J per contact gained or lost:
    - a separating pair: −4J (exact on an 8-ring);
    - one step off a flat face of a 3D jam: −20J;
    - dissolving a 27-record cube: −216J.
  - With +n contents, every snapshot has the same energy.
- **Consequences.**
  - With J ~ E_P (ARGUED), every cluster-changing step of a −n record is a grid-scale energy jump, i.e. a ghost source under the field route (A23/A24; decision 13).
  - This hits A30's leaking jams (its "caught matter" is −n), A28's V3 "living state" if contents are −n, and A31's own reason for preferring the blind weight.
  - But A31 D2 needs a −n record to force D = 0, and A30's seal needs −n.
- **Corrected wording (EXACT).** "A blind swap leaves ⟨H⟩ unchanged for a record with no recorded neighbour before or after the step, and for any configuration of +n records. A −n record that joins or leaves a cluster changes ⟨H⟩ by 2J per changed contact."
- **Draft.** Covered by C67's replacements for lines 265 and 280.

**C61. MAJOR (cross-lane + draft). "Gravity's places never hold records" collides with A25's layout and with A30's reading RA.**
- **Claims.**
  - A31:292 D10: "So F1 forbids hosting the field on any site that ever records."
  - A31:203: "**New: records only at matter places.**"
  - Draft:302: "**New: gravity's places never hold records (exact).** … Otherwise matter walls the field off: in the Earth, gravity ripples would die out within about 70 m".
  - Draft:291: "If each spot holds only its one qubit's possibilities (the axioms as written), a full region has nothing left to carry gravity, so everything stops."
  - Draft:365, decision 21.
- **What is right.**
  - D10 is an EXACT consequence of F1, Record and one qubit per place, read as A30's RA.
  - K5's arithmetic is right (by hand, Planck units, Cap₁ = 1/G(0) = 3.957):
    - Earth, one record per nucleon: u = 1.39e-74 per Planck site, m = 2.86e-9 eV, range 69 m;
    - water: 1.22e-9 eV;
    - ħω at 100 Hz: 4.1e-13 eV.
- **What is wrong.**
  - (i) **A25's layout gives every place a field job** (vertex, edge, face, cube roles; "3, 1, 2 or 3 reals per role", A25:296). With one qubit per place, D10 would forbid every record. D10 therefore presupposes a one-qubit field that leaves some places free (not built), which is also a new fixed pattern of record-free places. With more room per place (decision 13), D10 is moot. The draft's "Gravity" costs (and MORNING_SUMMARY:49–50) list both as joint costs; they are alternatives.
  - (ii) **Under D10 an I5 "fully recorded" region cannot exist**: field places inside it stay unrecorded and gravity runs through. So draft:291's "a full region has nothing left to carry gravity, so everything stops" holds only if records may form at every place.
    - That case is exactly the walled field K5 rules out, *if* ordinary matter carries about one record per nucleon. Below about 2e-8 records per nucleon the wall mass falls under ħω(100 Hz) (my arithmetic).
    - So A30's RA picture and A31's D10 are two different readings of the same axioms, and the draft presents them in separate sections without linking them.
  - (iii) The 70 m figure is conditional on about one record per nucleon, and its physics (wall mass for a tensor field) is ARGUED.
- **Draft.**
  - Line 302, replace with: "- **New: gravity's places never hold records, if gravity lives in the one qubit per place (exact consequence).** If the field lives in each place's one qubit and records never lock it, the places carrying the field can never be recorded. As built, every place carries part of the field, so this would forbid every record. It needs a one-qubit version of the field that leaves some places free (not built), or more room per place (decision 13). Otherwise records wall the field off: with about one record per nucleon, gravity ripples in the Earth would die out within about 70 m (argued), yet ripples that crossed the Earth have been detected (a comparison, not adopted). Under this rule no region can be fully recorded, so section 9's 'everything stops' picture cannot arise."
  - Lines 291–292: see C66.
  - Decision 21, replace with: "21. **Gravity's places.** If gravity's field lives in one qubit per place and records never lock it, may the places carrying it be ones that never hold records (A31)? As built, every place carries part of the field, so this needs a one-qubit field that leaves some places free (not built), and it is a fixed pattern of record-free places. Under it, no region can ever be fully recorded. Otherwise records wall off gravity ripples, which detected ripples rule out if matter carries about one record per nucleon."

**C62. MINOR (lane). K2(c) and A31's decision 6 overgrade the "tidy emptiness at matter's edges".**
- **Claims.**
  - A31:161: "(c) EXACT (combination)".
  - A31:212: "empty space next to matter must be the tidy kind (exact)".
- **What is wrong.**
  - The edge floor is EXACT only for the uniform free-fermion sea at a planar wall. I CHECKED the staggered sea (C72); interacting seas are ARGUED.
  - "Planck-scale ghosts" needs J ~ E_P (ARGUED).
  - Rank deficiency, not a calm *product* state, is what quietness needs.
  - A28's exits (A12 windows, coarse records) are not closed.
- **Corrected wording.** "ARGUED: with a full-rank sea at matter's edges, every nonzero gated weight records the sea there; with J ~ E_P the heating bounds then require a rank-deficient emptiness at edges, windows, or coarse records."
- **Draft.** No change; the draft's line 260 already keeps the many-tick exit.

**C63. MINOR (draft). Two A31 consequences lose their ARGUED grade.**
- **Claims.**
  - Draft:305: "the time-stretch that paces the field has to be a moving part of the field" (A31 K4(b): "ARGUED").
  - Draft:307: "Four choices then drop out" (A31 D13 and K1(e): "ARGUED").
- **What is wrong.** At a fixed Planck tick these choices are suppressed (O(τ²) per pair), not absent; they vanish only in the limit.
- **Draft.**
  - Line 305: "- the time-stretch that paces the field would have to be a moving part of the field, so each place holds more (argued);"
  - Line 307: "- **Ticks become bookkeeping if the chances per tick shrink with the tick** (argued), which avoids freezing and keeps records from outrunning light. Four choices then matter less and less as the tick shrinks: the claim rule, start-of-tick gating, the formation order and the change per tick."

**C64. MINOR (draft and lane). Stale after A31, and two omissions.**
- **Claims.**
  - Draft:334, decision 0: "Decision 12 does not yet, because light-like ripples have not been built in this shape".
  - Draft:354, decision 17: "No smooth, everywhere-alike change … has yet produced light-like ripples over a calm background".
  - A31:97: "So KS is the minimal supplied ingredient".
- **What is wrong.**
  - After A31 this is "cannot, over the calm product background, for single ripples", not "not yet".
  - A31 D7 also found no clean nearest-neighbour Dirac mass in the glued form (ARGUED), which the draft omits.
  - "Minimal" is ARGUED: entangled backgrounds, groups of ripples and more room per site are open.
- **Draft.**
  - Decision 0, last sentence: "Decision 12 does not yet: over the calm, all-pointing-one-way background, light-like ripples cannot be made without a painted-on pattern (A31; decision 17)."
  - Decision 17, replace with: "17. **Light and matter under point 0.** Over the calm, all-pointing-one-way background, no change that treats every spot and turn alike gives single ripples that move like light (exact). Light-like matter needs a painted-on sign pattern (A31). Either it goes on the whole rule: records can show it, it cannot keep the turns the field's pattern keeps, and tying the two together leaves 12 of 24 turns; and no simple way to give that matter a mass was found. Or it goes on the hopping only: one direction of the possibilities is favoured, against your Q3 for 16 of 24 turns, and records' steps must carry the signs. A background that supplies the pattern itself is being searched (A33). Is a fixed pattern acceptable, given that point 0 was chosen to avoid one for records? Which version, if either?"

### A30

**C65. MAJOR (draft). "At the best catching strength, capture depends only on speed" is false for massive matter.**
- **Claims.**
  - A30:68: "**At Γ_c, capture depends only on speed.**"
  - Draft:282: "At the best catching strength, how much is caught depends only on the speed of what arrives".
  - Draft:41: "it catches fast things almost always and bounces slow ones".
- **What I found (CHECKED, `c2`; own transfer-matrix code, validated against the closed form to 1e-12).**
  - At Γ = 2t, A = 2u/(1+u) holds to ≤ 8e-16 for the staggered chain on *both* surface terminations and in *both* bands, more generally than A30 tested (A30's open edge 8).
  - But Γ = 2t is the best strength only for the massless chain. For m = 0.2 and 0.6 the best Γ ranges from 0.67 to 6.0, depending on mass, energy and which sub-grid the surface sits on.
  - At the best Γ, capture equals the massless value 2 sin k/(1 + sin k) at the *same wavenumber*: 0.987, 0.911, 0.775 and 0.481 at four band positions, for every m and termination. It is not a function of speed.
  - Heavy waves near the gap (m = 0.6, u = 0.58) are caught at 0.987 with Γ = 6.0, against 0.736 at Γ = 2t.
  - What stays true (EXACT, threshold theorem): any *fixed* Γ reflects the slowest waves completely in the limit.
- **Corrected wording (EXACT + CHECKED, 1D).** "At Γ = 2t, the best strength for the massless chain, capture depends only on the arriving speed: A = 2u/(1+u), for massless and staggered-mass chains, either termination and either band. The best strength for massive waves differs, and there capture depends on the wavenumber. Any fixed strength reflects the slowest waves."
- **Draft.**
  - Line 282: "- In a one-line toy, at the catching strength that is best for the fastest things, how much is caught depends only on the speed of what arrives: things near the grid's top speed are caught almost always, slow things mostly bounce. A strength tuned for slow, heavy things catches them much better (up to 99% in my check) but other speeds less; no fixed strength catches the slowest things."
  - Line 41: "- at the catching strength best for the fastest things, it catches those almost always and bounces slow ones;"

**C66. BLOCKER (draft). "Gravity's clocks keep running inside, only slower" is a linear-order result applied where gravity is strong.**
- **Claims.**
  - Draft:292: "If each spot can also hold a never-recorded part for gravity …, gravity's clocks keep running inside, only slower."
  - A30:123: "the lapse keeps running: N = 1 − U > 0 at linear order [ARGUED; linear part EXACT]".
- **What is wrong.**
  - A30's own table (A30:397) grades "Lapse → 0 somewhere" OPEN. Its 4.4 says the linear route "cannot give horizons … the strong interior".
  - At one nucleon per spot, a jam is already at C = 1 at 14 kg. N_centre = 1 − 3C/4 turns negative for C > 4/3. For an Earth-mass jam C ≈ 6e15 (`q4_horizon`).
  - So in exactly the black-hole regime of your I5, "clocks keep running" is not established. It also clashes with draft:289, which says such regions would lie inside a horizon (comparison) and that the field route "cannot yet describe a horizon".
  - This answers the owner's own instinct ("time stops there") with an unsupported claim inside a decision framing.
- **Corrected wording.** "Under RB, the lapse inside a weakly self-gravitating jam (U ≪ 1) is N = 1 − U > 0 (EXACT at linear order). For jams near or past their horizon size, which is any jam above about 14 kg at one nucleon per site, the linear route fails, and whether the lapse reaches zero is OPEN."
- **Draft.** Replace lines 290–292 with:
  - "- **Do clocks stop inside?** That depends on choices for you and on strong gravity, which is not worked out.
    - If each spot holds only its one qubit's possibilities (the axioms as written), there are two cases. If records may form at every place, a full region has nothing left to carry gravity, so everything stops; but then its contents do not pull as ordinary mass, gravity ripples bounce off it, and ordinary matter would wall off gravity ripples too, which detected ripples rule out if matter carries about one record per nucleon (A31). If gravity's places never hold records (decision 21), no region can be fully recorded, and gravity runs through it.
    - If each spot can also hold a never-recorded part for gravity (decision 13's 'more room per place'), gravity's clocks keep running inside, only slower, as long as gravity there is weak. For any region big enough to be black-hole-like, gravity is strong, and the field route cannot yet say whether clocks stop (open)."
  - Line 46, replace with: "Whether gravity's clocks stop inside is open: it depends on choices for you and on strong gravity, which is not worked out (section 9)."

**C67. MAJOR (cross-lane + draft). Sealed jams and records that move forever need opposite step rules; and "any other stepping odds" is false.**
- **Claims.**
  - Draft:40 and :278: "With one stepping choice it never wears away."
  - Draft:265: "recording stops once there is nothing left to record, while records keep moving forever".
  - Draft:280: "With any other stepping odds the region slowly dissolves".
  - Draft:13: "with odds set by what that neighbour holds".
  - A31:57: "The blind weight W = 1 is preferred".
- **The conflict.** In calm surroundings there are three stepping options:
  - (a) Blind or β > 0 odds (A31's preference; A28 V3 used blind steps): records keep moving forever, but every jam dissolves (A30 2.8). With −n contents, every contact-changing step shifts the energy by 2J per contact (C60).
  - (b) Content weight with β = 0 and −n jams (A30's seal): jams are sealed, but lone records in calm space never move, A6 move clocks cannot run, and the "living state" disappears.
  - (c) Activity weight: flat faces and boxes are sealed for any content, and lone records in calm space are frozen too (A30:100, 2.4).
- **Two further links.**
  - A30's 2.4–2.5 give *other* sealing rules (the activity weight for boxes; "step only into a site touching ≥ 2 records" for flat faces), so draft:280's "any other stepping odds" is false.
  - The seal is the step rule that fits the *stricter* reading of "admissible" (A31 decision 5; draft decision 15). A blind −n step into calm |n⟩ lands where −n has zero odds given what the spot held. So the strict reading picks (b), and the frame reading permits (a).
  - A31 K2(d) (records that form traps must stay still, ARGUED) narrows the moving-forever case further.
- **Corrected wording (EXACT for the algebra; ARGUED for the readings).** "No step rule tested both seals a fully recorded region and keeps records moving through calm space."
- **Draft.**
  - Line 265, replace with: "- **One encouraging case, with a catch.** With a tidy emptiness and records whose content lies along its direction, recording stops once there is nothing left to record, while records keep moving forever: no freezing, no thinning. But this needs stepping odds that let records into calm space, so fully recorded regions then slowly dissolve (section 9). And if record contents are the opposite of the emptiness, every step that brings records together or apart changes the energy by a grid-scale amount."
  - Line 279: "- The price: a lone record in empty space can never move either, and records stop moving through calm space altogether, so section 7's 'records keep moving forever' does not hold under it. It is also the stepping rule that fits the stricter reading of 'admissible' (decision 15)."
  - Line 280: "- With fixed odds, or any chance of stepping into calm space, the region slowly dissolves, in a time that grows with its size far more slowly than a black hole's lifetime would. If its contents are the opposite of calm space, each record that leaves also changes the energy by a grid-scale amount. Two other stepping rules seal flat or box-shaped regions (A30)."
  - Decision 19, replace with: "19. **Sealing records in.** May a record step only into a neighbouring spot that already holds something like its own content (A30)? That lets a fully recorded region last forever, and it fits the stricter reading of 'admissible' (decision 15). But a lone record in calm empty space could then never move, and records would not keep moving forever (section 7). The alternative, fixed odds (A31's preference), lets records move but makes every fully recorded region slowly dissolve."

**C68. MINOR (lane + LOG). The seal's "fails off axis" contradicts A30's own table; one hypothesis is unstated.**
- **Claims.**
  - A30:108: "The seal fails as soon as any jam content is off the quiet axis."
  - LOG:1366: "the seal fails if any content is off axis".
- **What is wrong.**
  - A30's table: r = +n (on the axis) gives content odds 1.000, so the seal fails for any content that is not −n. The draft (line 278, "opposite of calm empty space") is right.
  - The seal proof (A30:318–319) uses "covariant terms a + bσ·σ", i.e. SU(2)-invariant bonds. A glued DM term compresses next to −n to a non-diagonal term. This is consistent with A31 D2 (a −n record forces D = 0), but it should be stated.
- **Replacement (A30:108, LOG:1366).** "The seal fails as soon as any jam content is not opposite to the quiet axis; the proof assumes the bond terms are of Heisenberg form, which A31 D2 forces once a −n record exists."

**C69. MINOR (lane). "At nuclear density … R_h ≈ 6 km" is wrong.**
- **Claim.** A30:422.
- **What is wrong.** R_h = √(3c²/(8πGρ)) gives 24–26 km for ρ = 2.3–2.7e17 kg/m³ (M ≈ 8–9 M_⊙). 6 km is about the Schwarzschild radius of 2 M_⊙. The script does not compute this line. It is not in the draft.
- **Replacement.** "At nuclear density the same formula gives R_h ≈ 25 km."

**C70. MINOR (draft). "Nothing from outside can reach in" is exact only for records and possibilities; two comparisons are unflagged.**
- **Claims.**
  - Draft:40: "literally a place where nothing can ever happen again … nothing outside can reach in".
  - Draft:276: "nothing from outside can ever reach in".
  - Draft:287: "A black hole hides what fell in."
  - Draft:289: "If each recorded spot carries ordinary mass".
- **What is wrong.**
  - A30 3.5: EXACT "for the record and matter sectors only". Gravity crosses under RB or D10.
  - Line 287 is a GR comparison, stated as fact.
  - Line 289's estimate assumes the region's mass pulls, which under RA it does not (A30 4.5).
- **Draft.**
  - Line 40: "7. **Your black-hole idea (A30, checked).** Inside the point-2 shape, a fully recorded region is a place where no record can ever form or move again, its possibilities never change, and no record or possibility from outside can reach in (gravity may still, depending on decisions 13 and 21). With one stepping choice it never wears away, but that choice also freezes every lone record in empty space. It is grey, not black:"
  - Line 276: "- nothing from outside can ever reach in (for records and possibilities; gravity's field may still cross, depending on decisions 13 and 21);"
  - Line 287, last sentence: "A black hole in Einstein's gravity hides what fell in (a comparison, not adopted)."
  - Line 289, first sentence: "If each recorded spot carries ordinary mass and that mass pulls (which needs more room per place, or gravity places that are never recorded), any packed region …"

**C71. MINOR (draft). Two catching statements need their toy scope.**
- **Claims.**
  - Draft:284 and :42: "No edge rule catches everything at every speed".
  - Draft:285: "A rough, spongy edge helps somewhat, but never for the slowest things."
- **What is wrong.**
  - The threshold theorem is proved in 1D, for fixed-rate catching over a finite depth, plus one catch-and-release channel.
  - In the 2D toy the porous shell helped *most* at the slowest wave tested: +10% at k = 0.39 (`out_q1_2d_porous_2.0.txt`), and −3% at k = 2.16. "Never for the slowest" is the 1D k → 0 statement.
- **Draft.**
  - Line 284: "- No fixed catching rule catches everything at every speed (proved in a one-line toy), and the records' own pull on what arrives can cap catching at two-thirds."
  - Line 285: "- A deeper, graded catching layer helps for all but the slowest things (one-line toy); in a flat 2D toy a spongy edge caught about 10% more of the slower waves tested, with a third fewer records."
  - Line 42: "- no fixed setting catches everything at every speed (proved in a one-line toy);"

### A28

**C72. MINOR (draft). The edge floor is exact for the simplest sea; for the repo's staggered sea it is now checked.**
- **Claims.**
  - Draft:260: "Next to any record, the half-filled sea always has some chance of being recorded (exact). So records creep into it, and each new one heats its surroundings far beyond what is seen."
  - A28:91: "[ARGUED] interacting seas, and the staggered sea with a wall."
- **What I found (CHECKED, `c5`).** KS π-flux half-filled sea, 3D boxes L = 8/10/12, planar wall: the 6-site wall star is full rank, ν ∈ [0.015, 0.985], smallest many-body eigenvalue 1.3–1.5e-5 (stable). That is about 35× below the uniform sea's 5.27e-4 but nonzero. Interacting seas remain ARGUED. "Far beyond what is seen" needs J ~ E_P (ARGUED).
- **Draft.** Line 260, first two sentences: "Next to any record, the half-filled sea always has some chance of being recorded (exact for the simplest half-filled sea; my check confirms it for the repo's staggered kind). So records creep into it, and each new one heats its surroundings, far beyond what is seen if the rule's energy scale is the Planck scale (argued)."

**C73. MINOR (lane). The heating chain to c ≲ 3e-86: the arithmetic is right; one input is unsourced.**
- **Claims.** A28:169: "c ≲ 3e-86 per tick for one isolated record per nucleon (λ_min = 5e-6)".
- **Checked.** `c4_scales`: 1e-90/(6 × 5e-6) = 3.3e-86 ✓; the ball case 5.6e-128 ✓; "1.6e42 s" ✓.
- **Assumptions.**
  - (i) λ_min = 5e-6 is computed nowhere in A28. Its computed values are 5.27e-4 (3D wall) to 5.7e-3 (1D); mine for the staggered sea is 1.4e-5. The choice is conservative: with A28's own 3D value the bound is 3e-88.
  - (ii) Each false record is charged E_P, not the CHECKED 0.21J (a factor of ~5, conservative).
  - (iii) A19's "1e-90 per nucleon per tick" is ARGUED from Earth's heat flow (COMPARATOR).
  - (iv) J ~ E_P is ARGUED.
  - (v) The geometry (one isolated record per nucleon) is supplied.
- **Grade.** ARGUED, order of magnitude. The draft does not quote the number; no draft change.

**C74. MINOR (draft; owner reading Q1). "Left completely alone" holds for the instruments and on average, not per outcome.**
- **Claims.**
  - A28:25: "so a void's possibilities evolve by the smooth change alone".
  - A28:74: "never disturbed by the record machinery".
  - Draft:257: "light crossing it is left completely alone".
  - Draft:258: "no faraway influence leaks".
- **What is wrong.**
  - By your Q1, when a record forms elsewhere, possibilities shared with it "change at once to agree". Light entangled with recorded matter changes per outcome; only the outcome-averaged state evolves by the smooth change alone.
  - Option R also has faint unrecorded influence beyond one site per tick (bottom line 2). What the gate guarantees is that no faraway *choice* steers records.
- **Draft.**
  - Line 257: "- light crossing it is never recorded and no recording rule acts on it there; it changes only through its links to records formed elsewhere (your Q1), and on average not at all;"
  - Line 258: "- no faraway choice can steer it, because the rule looks only at the records next door, and those always agree with the spot they sit on;"

**C75. MINOR (draft; owner reading Q4). The Q4 consequence is A28's ARGUED reading, presented as a consequence.**
- **Claims.**
  - Draft:341: "Under that rule your Q4 (an uninfluenced site has equal odds) never applies to an actual formation, because a site with no recorded neighbour never forms a record (A28)."
  - A28:221 grades this ARGUED.
- **What is wrong.** It equates "uninfluenced" with "no recorded neighbour". If "uninfluenced" means "nothing tilts the odds", Q4 still bites next to a record whose content sets the frame but not the odds. A29's C51 text was too strong; I flag this because it touches a decided reading.
- **Draft.** Replace the last sentence of decision 4 with: "Under that rule every forming site has a recorded neighbour. If 'uninfluenced' in your Q4 means 'no recorded neighbour', Q4 would never apply to an actual formation; if it means 'nothing tilts the odds', it still applies next to records (argued, A28)."

**C76. MINOR (draft). Transparency depends on record size, not sparseness.**
- **Claims.**
  - Draft:264: "light escapes recording only if records are small and sparse, recording is weak, or the rule ignores light."
  - Draft:364: "but in glass or water that recording must be very weak (A28)".
- **What is wrong.** A28's table (verified against `c4`) shows that one point-like record per nucleon passes at any strength: κ_max = 2e34 (fibre), 5e36 (water). Only nucleon-sized recorded balls need κ ≲ 4e-6 or 9e-4.
- **Draft.**
  - Line 264: "- in dense transparent matter such as glass or water, light escapes recording only if records are point-like rather than nucleon-sized, recording is weak, or the rule ignores light."
  - Decision 20: "… but in glass or water that recording must be very weak if records are nucleon-sized (A28)."

### A32

**C77. MAJOR (draft). "Ticks that differ by place are possible only if each place remembers" overstates A32's construction-by-construction result.**
- **Claims.**
  - Draft:26: "Ticks that differ by place are possible only if each place remembers where it is in its own cycle".
  - A32:55: "A tick written into the law must be the same everywhere, by covariance [EXACT]".
  - A32:571: "each place would then have to remember".
  - (A32:236 itself says "construction by construction; this is not a closure claim".)
- **What is wrong.**
  - (i) Draft:162 says random local times need no memory, which contradicts line 26's "only if".
  - (ii) **D8(a) holds only if "alike" is required with no global time shift.** Allowing an unreadable global shift (A32's own D3c), translation covariance forces φ(x) = u·x + φ₀ (mod τ), and the 24 turns force R^T u ≡ u. The only solutions are u = 0 and u = (τ/2)(1,1,1) (EXACT by hand; CHECKED `c6` over all u ∈ (τ/q)Z³, q ≤ 24). So a two-sub-grid checkerboard, offset by half a tick, is a set neighbourhood tick written into the law with no memory. Its cost is A16 C7's: records can tell the two sub-grids apart, at order τ (A32 D3d).
  - (iii) Phases set by the surrounding (permanent) records need no extra register and were not examined (D16 covers rates only).
- **Corrected wording.** "A law-level tick that treats every place alike is one shared tick, or (up to an unreadable overall shift) a two-sub-grid checkerboard that records can faintly tell apart (EXACT). Set ticks that differ by place needed per-place memory in every construction tried; record-set phases are untried."
- **Draft.**
  - Line 26: "- **Global or neighbourhood?** A tick written into the rule itself is the same everywhere if the rule treats every place exactly alike. The only other way is a checkerboard of two sub-grids half a tick apart, and records can faintly tell those apart. Set ticks that differ by place needed a per-place memory in every construction tried (your small-memory question). Random local times need none but are just a thinned-out shared tick. Ticks set by the surrounding records were not tried."
  - Line 160: "- A tick written into the law is the same everywhere if the law treats every place exactly alike. A checkerboard of two sub-grids half a tick apart also qualifies, up to an unnoticeable overall shift, but records can faintly tell its sub-grids apart."
  - Line 161: "- Ticks set differently by place needed each place to remember its phase in every construction tried (decision 9); ticks set by the surrounding records were not tried."

**C78. MAJOR (draft). "Far too small to see" is conditional on small chances per tick and gentle records.**
- **Claims.**
  - Draft:28: "Whichever choice is made shows in the records only in proportion to the chance of a record on a single tick, far too small to see on the finest grid."
  - Draft:157: "only in proportion to the chance of a record on that tick".
  - Draft:355: decision 18's first sentence.
- **What is wrong.**
  - A32's bound is order c *plus* order (tick × rate at which the odds vary), and it is first order in the shift (A32:36–39).
  - A32's own scope note (A32:117) says: "At the owner's matched tick (change per tick of about 1), the EXACT bound is of order 1 per record event. Near-undetectability then needs gentle records."
  - Small chances per tick are a named choice (P1), not a result.
- **Draft.**
  - Line 28: "- **How visible is it?** If the chance of a record on a single tick is tiny, as freezing and heating already require, whichever choice is made shows in the records only in proportion to that chance, and to how fast the odds change within one tick. That is far too small to see on the finest grid. With a real chance on every tick and sharp records, it could be visible."
  - Line 157, second sentence: "Moving one record event in time changes everything recorded later only in proportion to the chance of a record on that tick and to how much the change does during the shift."
  - Decision 18, first sentence: "In the point-0 shape, if record chances per tick are small, any tick schedule shows in the records only in proportion to that chance."

**C79. MAJOR (draft) + MINOR (lane numerics). No minimum tick follows; the "pinned" case needs more than order-1 chances.**
- **Claims.**
  - Draft:32: "This comes out as an upper limit … It is pinned to about that time only if every tick carries a real chance of a record, and odds that large would make glass and water cloudy."
  - Draft:175: "ticks that are too short freeze things beside records".
  - A32:108: "derivable as an upper bound".
  - A32:456: "For c = 0.5 and 0.1 the optimum sits at Jτ ≈ 0.248 and 0.050, that is τ* ≈ c/(2J)."
  - A32:458: "within a factor 2.5 of its maximum".
- **What is wrong.**
  - (i) Your instinct is a *minimum* tick. What is derived (given the premises: one site per tick should bound all influence, and light is a ripple of the possibilities) is a *longest* allowed tick. No smallest tick follows for records. D32's "minimum time of the change" is a bound on how fast odds can change, not a tick.
  - (ii) The "pinned" window needs order-1 chances *and* the unstated aim that recording run near its fastest (A32's arbitrary factor 2.5). Even at c = 1, the rate-optimal tick Jτ* = 1.17 lies outside the cone condition Jτ ≤ 0.5. Shorter ticks only *slow* recording (Zeno); they do not forbid it.
  - (iii) Order-1 chances per Planck tick would Zeno-freeze every process slower than the grid scale next to records. That already excludes them for weights on evolving content (A27 Step 8), independent of glass.
  - (iv) "Cloudy glass and water" holds only for nucleon-sized records with a rule that records light (C76).
  - (v) **Numerics (CHECKED, `c4`).** A32's c = 0.1 optimum 0.050 is the lower edge of its search grid (`c5_tick_vs_grid.py:95`, `linspace(0.05, …)`). The true optimum is Jτ* = 0.0372, matching the coordinator's 0.037. It is not a post-record convention issue: both use first passage from u. The small-c law is τ* ≈ c/(2√2 J) (continuum optimum γ* = 2√2 J, rate J/√2), not c/(2J).
- **Draft.**
  - Line 32: "- **Minimum distance and minimum tick.** No smallest tick follows. What follows is a longest one: if one site per tick is to be the limit for all influence, the tick must be shorter than the time light takes to cross one grid step (shorter by √3 in 3D). A tick near that crossing time is favoured only if every tick carries a real chance of a record and recording is to run near its fastest. Such chances would freeze anything slower than the grid's fastest motion next to records, and with nucleon-sized records they would cloud glass and water (argued)."
  - Lines 175–176: "- No smallest tick follows. A tick near light's crossing time is favoured only if every tick carries a real chance of a record and recording is to run near its fastest. Shorter ticks then slow recording beside records (they do not forbid it), and such chances already freeze slower motion beside records. With small chances the tick is only limited from above."
- **Lane replacement (A32:456).** "For c = 0.5 and 0.1 the optimum sits at Jτ ≈ 0.244 and 0.037; for small c, τ* ≈ c/(2√2 J)."

**C80. MAJOR (cross-lane + draft). "Moving clocks slow by Einstein's amounts" assumes Dirac-like matter, which this shape gets only from A31's painted pattern.**
- **Claims.**
  - Draft:29: "Moving clocks slow by Einstein's amounts."
  - Draft:169: "Clocks made of the possibilities slow with motion as Einstein says".
  - A32:582: "Moving clocks and clocks held low near a heavy body slow by the usual amounts."
- **What is wrong.**
  - D21's clock is a two-band lattice Dirac particle, H(k) = sin k·σ_x + m σ_z (A32:347–348). Over the calm product background, A31 shows single ripples are one quadratic band; Dirac-like matter needs the painted sign pattern (or more room per site). So D21 is conditional on decision 17.
  - Record-counting clocks slow with motion only partly (D20), and with gravity only if their chances carry the lapse (P5).
- **Draft.**
  - Line 29: "- **Light.** If records form only next to records, the ticks never touch how light and matter travel through empty space, so the precise relativity tests with light from distant explosions say nothing against them. Clocks made of light-like matter slow with motion by Einstein's amounts; in this shape that matter needs the sign pattern of section 10."
  - Line 169: "- **Light never sees the tick (exact, when records form only next to records).** In empty space the ticks act on nothing, so they add no energy-dependent speed and no twisting of light's polarisation. Clocks made of light-like matter slow with motion as Einstein says, with corrections around 10⁻³⁸ at laboratory speeds; in this shape that matter needs section 10's sign pattern."

**C81. MINOR (lane). The re-timing lemma is right; "all schedules share one continuous limit" holds per finite window.**
- **Checked by hand.**
  - Forming outcome: ‖D_k‖ ≤ 2δ‖H_∂S‖‖K_k‖.
  - No-record outcome: ‖[H,√(1−F)]‖ ≤ c‖H_∂S‖/√(1−c), from Σn|f_n|c^{n−1} = 1/(2√(1−c)).
  - Trace distance ≤ Σ(‖D_k‖‖K_k‖ + ‖D_k‖²/2).
  - Total δc‖H_∂S‖(4 + 1/√(1−c)) ✓.
- **Scope to add.**
  - (i) The constant 4 counts two forming outcomes, a qubit menu.
  - (ii) The bound is first order in δ; it controls the error only when ‖H_∂S‖δ ≪ 1, not at matched ticks.
  - (iii) ‖H_∂S‖ is the change on bonds touching the instrument's whole support S (the star for star weights). A32:37 says "the instrument's spot".
  - (iv) D3's joined bound grows like n_S·T, so "one continuous limit" holds for record statistics in any finite region and time window (EXACT scaling), not for the whole history of an infinite grid.
  - (v) "A global time offset is unreadable" (A32:59) needs "for stationary preparations" (as in D3c).

**C82. MINOR (lane). D20's "at most half slows" needs left–right-symmetric weights.**
- **Claim.** A32:339: "With momentum-independent blocks, the count ratio is (a + bR)/(a + b) with a ≥ |b|. **At most half of the count rate slows with motion** [EXACT; CHECKED f = 0.500000 …]".
- **What is wrong.** The ratio drops the odd term d·sin k/ω. With d ≠ 0 one direction's count can fall far below half (coordinator: 0.009). The draft's line 170 already carries the scope; the report should too.
- **Replacement.** "For weights that treat both directions alike (d = 0), at most half of the count rate slows with motion [EXACT, toy]."

**C83. MINOR (lane). D24's example weight is quiet only next to records along the emptiness.**
- **Claim.** A32:383: "An example compatible with a quiet emptiness and with no law-level axis: F^(R) = c(1 − |r⟩⟨r|) … with r taken from a recorded neighbour."
- **What is wrong.** Next to a −n record, F = c|n⟩⟨n|, so it records the calm |n⟩ at rate c per tick and breeds. A30's sealed jams and A31's D-forcing both use −n records.
- **Replacement.** "… compatible with a quiet emptiness next to records whose content equals the emptiness direction; next to opposite-content records it records the emptiness."

**C84. MINOR (draft). Smaller A32 wording items.**
- **Line 31.** "with no problem" omits D25 and D27. Replace with: "- **Same tick.** Two records can form on the same tick consistently. If the rule looks at neighbours, it needs an order or a joint rule, and a choice of whether same-tick neighbours see each other's new records. With small chances it almost never happens."
- **Line 156** (owner rule a). "Records form and step on ticks" becomes "In this option, records form and step on ticks; the possibilities change all the time."
- **Line 166.** "What consistency requires" becomes: "If clocks that count records are to agree with all other clocks near heavy bodies (your choice), the chance of forming a record per unit of local time must be the same everywhere."
  - This is A32's P5, motivated by the equivalence principle (COMPARATOR). A32 itself notes no tested clock is formation-limited.
- **Line 164.** After "only in proportion to the chance per tick", add "if that chance is small".
- **Decision 18.**
  - Add the missing choice P2: "- does a forming site look at the records present at its own tick (then chains of new records can outrun one site per tick) or at the previous tick's (a memory)?"
  - Change "(needed for gravity; …)" to "(needed for gravity if record-counting clocks are to agree; only partly possible for motion)".
- **Line 53 (stale).** Replace the parenthesis with: "(Point 0's shape gives this up for unrecorded influence. A32 has redone point 5's tick results there; the results of points 1 and 4 would need redoing.)"
- **Line 259.** "records spread at most one site per tick, provided the rule looks at the records present at the start of the tick" needs "and there is one shared tick". With ticks that differ by place, chains of new records outrun it (A32 D7). Line 99 ("one site per tick, exactly for records") holds for steps, and for spread only under one shared tick.

### Draft structure

**C85. MINOR (clarity). Two numbering systems collide.**
- **Claims.**
  - The same shape is "point 2's shape" or "the point-2 shape" in the bottom line (lines 16, 23, 25, 37, 40) and "point 0" or "the point-0 shape" in the body (lines 53, 68, 81, 92, 145, 156, 254, 272, 294, decisions 0, 7, 8, 15–18).
  - "Point 1's limit" means A20 at line 16 but A3 at line 137.
  - "See point 6" (line 37) means body section 6, while bottom-line point 6 is handedness.
  - "(point 9)" (line 46), "points 1 and 4 … point 5" (line 53) and "(point 3)" (line 63) mean body sections.
  - Line 92 says "section 10".
- **Fix.**
  - Name the shape once ("the record-tick shape") and use that name everywhere instead of "point 0" or "point 2" when the shape is meant.
  - Call body sections "section N" and bottom-line items "bottom-line item N".
  - Minimum edits:
    - line 16: "bottom-line item 1's limit" and "bottom-line item 4";
    - line 37: "section 6", and "the record-tick shape";
    - line 46: "section 9";
    - line 53: "sections 1, 4 and 5";
    - line 63: "section 3";
    - line 137: "section 1's one-site limit".

**C86. MINOR. Review count.**
- Line 1: "(v9, after four hostile reviews)".
- Line 50: "Four hostile reviews by separate agents attacked the main claims (each later one had read the earlier ones), and their corrections are included."
- Line 57: "all four reviews".
- Line 367: keep A33 as running until it lands.

**C87. MAJOR (owner-facing). `MORNING_SUMMARY_DRAFT.md` re-introduces three corrected overstatements and adds the A31/A32 ones.**
- **Regressions.**
  - Line 23 "only an exponentially faint leak" undoes C52. It should read "a leak that stays exponentially faint only if the change per tick is small".
  - Line 45 "is pinned by the grid's turns to Einstein's linear gravity" undoes C33. It should read "if its bookkeeping is kept exact, the grid's turns fix its form to Einstein's linear gravity at long wavelengths; its speed relative to light and its strength are not fixed".
  - Line 51 "records formed gently ('catch first, record later')" undoes C35. It should read "almost all records formed on caught, settled things (one working toy: catch first, record later)".
- **Inconsistency.** Lines 49–50 list "more settings per place than one qubit" and "the places carrying the field never recorded" as joint costs; they are alternatives (C61).
- **Same overstatements as the main draft.**
  - Line 28: C77.
  - Line 29: C84 conditional.
  - Line 30: "under the records-only-next-to-records rule".
  - Line 31: C79.
  - Line 32's "must be the tidy, lined-up kind": C62, should be "would have to be (argued)".
  - Line 33 "it can be sealed": add "by a stepping rule that also freezes lone records".
  - Line 34: C65.
  - Line 37: C66 and C61.
  - Lines 41–42: C57 and C58.
- **Draft.** Apply the corresponding replacement texts above, shortened.

---

## 3. Draft sentences that are fine as they are (03:27 version)

- **Bottom line.**
  - Lines 5–11; 13–20; 22.
  - Line 25, with C84's caveat optional: walls return for records only if a step needs both ends to tick together.
  - Lines 27 and 30.
  - Lines 34–37; 39; 43.
- **Section 0.**
  - Lines 63–68; 72–81; 84–86; 89; 91; 93–98; 100–101.
  - Line 90 is consistent with A32 (readable only at order c and order τ × frequency).
- **Section 5.**
  - Lines 146–154 (ticked change, already scoped).
  - Line 158 ("82% … where the ticked rule let nothing through" matches A32:44 and :202).
  - Lines 162–163; 165; 167–168 (c/g ≈ 1 year is exact arithmetic).
  - Line 170 (the coordinator's scope note is right).
  - Lines 171–173.
  - Line 174 (premises stated).
- **Section 7.** Lines 246–256, 261–263.
- **Section 9.**
  - Lines 274–275 and 277.
  - Line 278's condition ("the opposite of calm empty space") is correct.
  - Lines 283, 286, 288.
  - Line 289's numbers (R_h = 2.0e-26 m, 13.6 kg verified by hand and in `q4_horizon`).
- **Section 10.**
  - Lines 295–296; 299; 304; 306; 308.
  - Line 302's arithmetic (2.86e-9 eV, 69 m) is right; its framing needs C61.
- **Decisions.**
  - 13 (C54's text is in).
  - 14, 15 and 16.
  - 18's list, apart from C78/C84.
- **Owner-rule scan.**
  - No sentence says a possibility is "read" or that a "question is asked". Lines 109 and 318 use "read" for records' places and in a negation.
  - Q7 stands (lines 310–319).
  - No axiom or import is presented as adopted.
  - The tick is framed as an option or instinct everywhere, except line 156 (fix in C84).

---

## 4. New open questions for the owner (plain language; nothing adopted)

1. **Sealed regions or moving records?** No stepping rule tried tonight both keeps a fully recorded region from wearing away and lets records keep moving through calm empty space. The sealing rule is also the one that fits the stricter meaning of "admissible". Which matters more to you (C67)?
2. **What counts as a neighbourhood rule?** If the change may use terms on three or more spots of a neighbourhood, a calm, all-aligned emptiness allows more rules than the plain "line up with your neighbour" one, including a handed one. None of them makes single ripples move like light. Should the change be built from pairs only (C56)?
3. **A background that shares its possibilities.** The plain rule makes light-like ripples over a background whose spots share their possibilities (like a magnet whose neighbours point opposite ways), with no painted pattern. But such a background gets recorded and heats next to matter. Is that trade worth exploring, for example with recording that builds up slowly at edges (C57)?
4. **Places that never hold records.** As built, every place carries part of the gravity field. Would you accept a fixed set of places where records can never form? Under that rule no region could ever be fully recorded, so your black-hole picture would change (C61).
5. **Ticks set by records.** Would a neighbourhood tick whose timing is set by the records around each spot (no extra memory, since records are permanent) fit your idea of an influenced tick (C77)?
6. **"Minimum tick".** Did you mean a smallest possible tick (not derived tonight) or a longest allowed one (derived, if records should keep up with light) (C79)?

---

## 5. Lane and LOG wording fixes

| Location | Old | New |
|---|---|---|
| A31:62, D2 | "Calm forces K = 0 … so H = J Σσ·σ (EXACT)" | add "among nearest-neighbour pair terms; glued star terms (e.g. the chiral three-spin term) also keep it calm" |
| A31:254 | "a vacuum that is not exactly stationary" | "a vacuum that is not a stationary product state (e.g. the entangled antiferromagnetic ground state, COMPARATOR)" |
| A31:296, D11 | "It is 0 for content −n in calm surroundings, by translation invariance (EXACT)" | "… for a −n record with no recorded neighbour before or after the step; joining or leaving a cluster changes ⟨H⟩ by 2J per contact (EXACT)" |
| A31:161, K2(c) grade | "EXACT (combination)" | "ARGUED" |
| A31:200, :356 | "quarter turns" | "face-diagonal half turns" |
| A30:108; LOG:1366 | "off the quiet axis" / "off axis" | "not opposite to the quiet axis" |
| A30:422 | "R_h ≈ 6 km" | "R_h ≈ 25 km" |
| A28:25, :74 | "a void's possibilities evolve by the smooth change alone" / "never disturbed" | add "on average over unread outcomes elsewhere; per outcome they change at once to agree with distant records (Q1)" |
| A28:169 | "(λ_min = 5e-6)" | "(λ_min = 5e-6, a conservative stand-in; A28's computed 3D value 5.3e-4 gives 3e-88)" |
| A32:55 | "must be the same everywhere, by covariance [EXACT]" | add "or, up to an unreadable global shift, a two-sub-grid checkerboard (A16 C7's cost)" |
| A32:339 | "At most half …" | prefix "For left–right-symmetric weights (d = 0)," |
| A32:456 | "0.050, that is τ* ≈ c/(2J)" | "0.037; for small c, τ* ≈ c/(2√2 J)" |
| LOG:1407 | "This sharpens C30 from 'not built' to 'impossible in the class'." | add "for single ripples over calm product vacua; pair terms only for D2" |
| LOG (A32 entry, 'Minimum distance') | "comes out as an upper bound" | "no minimum tick follows; a longest allowed tick follows given the premises" |

**Scripts.** All in `c8/A34/`: `c1_star_terms.py`, `c2_staggered_capture.py`, `c3_blind_step_energy.py`, `c4_zeno_optimum.py`, `c5_staggered_edge.py`, `c6_law_schedules.py`, with `out_*.txt` and `time_*.txt` beside them.
