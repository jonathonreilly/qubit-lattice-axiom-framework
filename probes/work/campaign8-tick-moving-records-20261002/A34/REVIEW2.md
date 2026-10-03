# A34 fifth hostile review (continuation): A33, the draft's new A33 text, and the one-page summary

**Provenance.**
- Same agent as the fourth review (A34), so this is a second round by one reviewer, not an independent one.
- Primary files read:
  - `A33/REPORT.md` (175 lines);
  - A33's outputs for the layer vacuum (`out_a20_flux_4_1`), the star composites (`out_a22`, `out_a23`), the calm tests (`out_a18`, `out_a19`), the redundant-check class (`out_a21_*`), and `a19_calm_signs.py`;
  - `toys/verify_A33_parity.py`;
  - the A33 and A34 LOG entries;
  - `MORNING_DRAFT.md` v9 (04:26, 376 lines) and `MORNING_SUMMARY_DRAFT.md` (04:26, 62 lines).
- Line numbers refer to those versions. No git, no repo edits; I wrote only into `c8/A34/`.

**What I ran.** `c7_parity_route.py` → `out_c7_parity_route.txt`. Load was 1.9–3.3 at the runs; `nice -n 10`; all four thread caps at 1; 1.5 s; 79 MB.
- **(A) Representation theory: what one qubit allows at each role, under the turns that turn possibilities along.**
  - Vertex and cube places (group O): one qubit's operators are 1 A1 + 1 T1. So there is no one-dimensional label other than the identity.
  - Edge and face places (D4 about the axis): one qubit's operators are A1 + A2 + E. σ^axis has parity −1 under the diagonal half-turns.
- **(B, C) An 8-band π-flux toy on the period-2 roles.** I varied the bond strengths per role pair and gave each role its own energy:
  - Equal role energies give a clean eightfold cone (slope 2.0).
  - Unequal bond strengths (1, 0.7, 1.3) keep the cone (slope 1.4).
  - A staggered energy part ±0.2 opens a gap of 0.40, i.e. a mass.
  - A vertex-only energy of 0.2 breaks the eightfold cone: one band leaves, and one turns quadratic (−0.011, −0.039 at the two offsets).
  - Energies (0.1, 0.1, −0.1, −0.1) split the cone point into crossings at shifted momenta, with slopes 1.14, 1.30 and 1.00 (anisotropic).

---

## 1. Verdicts

| Item | Verdict | One-line reason |
|---|---|---|
| **A33 lane** | **Holds** (minor narrowing) | I re-derived Theorems C and A and the parity formula; they are right as stated: protected (superselected) charges, pure Pauli-stabilizer vacua, independent checks. Impurity certificates are EXACT. "Immobile on Z³" for survivors is slightly overgraded (torus blind spot, C91). The parity route is correctly graded "symmetry-allowed, not built", but more is needed for light (C89). |
| **Draft v9, A33 text** | **Needs changes (2 MAJOR)** | "No disturbance can travel in all three directions" drops Theorem C's scope. That contradicts the draft's own open route, whose ordinary ripples do travel in 3D (C88). The parity route is described as supplying "light's twist" without the conditions for light (C89). |
| **One-page summary** | **Needs changes (3 MAJOR)** | It drops the Q3 gluing condition from the headline theorem (C95). It re-introduces three corrected overstatements (C96). It loses the conditionals on four "must"/limit sentences (C97). |

---

## 2. Findings

### A33 and the draft's A33 text

**C88. MAJOR (draft + summary). Theorem C is about disturbances the background protects; the draft says "no disturbance".**
- **Claims.**
  - Draft:309: "In any tidy, exactly solvable background where each place carries one independent condition, no disturbance can travel in all three directions; at best it slides within flat sheets (exact)."
  - Draft:21: "in tidy backgrounds with one condition per place, disturbances can at best slide within flat sheets (exact, A33)".
  - Draft:310: "Free 3D motion needs more conditions than places".
  - Draft:357 (decision 17): "with one condition per place, disturbances can at best move within flat sheets".
  - Summary:47: "with one condition per place, disturbances can at best slide within flat sheets (proved, A33)".
- **What holds (EXACT; re-derived).** A33:27 is stated correctly: "no *superselected* excitation, single defect or composite".
  - The sequence 0 → R^t → R^{2t} → R^t → C → 0 is exact (purity gives ker ε = im σ; t check orbits of a rank-t Lagrangian module make σ injective). So pd C ≤ 2.
  - Auslander–Buchsbaum then gives depth C_m ≥ 1 at every maximal ideal, so C has no finite-length submodule.
  - A class moving by a rank-3 set has (1 + y_i^n)s = 0 for i = 1, 2, 3. So R·s would be a quotient of R/(y_i^n − 1), which has finite length.
  - Type-changing moves reduce to the same move lattice.
  - **Composites.** The result covers every *nonzero class*, single or composite, so "planes at best" holds for all superselected composites.
  - **Hypotheses actually used.** A Pauli-stabilizer vacuum (the Laurent ring over F₂ encodes Paulis mod phase); finite-range checks; purity on the infinite grid (no local logical operator); check orbits per cell = qubits per cell; translations Γ ≅ Z³. Covariance is *not* used.
- **What is wrong.**
  - (i) **Locally creatable disturbances are not covered.** Any disturbance made by a single local operator p moves by one step via p·(translate of p), in all three directions. These are ordinary local ripples. A33:72 notes they carry ordinary translations, so they get no twist from the background's repeat on the Γ plaquettes. But they are exactly the "ordinary local ripple" of the open route (draft:311), which would travel in 3D.
    - So draft:309 contradicts draft:311.
    - Draft:310's "Free 3D motion needs more conditions than places" is false for ordinary ripples.
  - (ii) **"Tidy, exactly solvable" is broader than the proof.** Theorem C covers Pauli-stabilizer states only. Other exactly solvable commuting-projector models, and non-stabilizer calm vacua (A33 open edge 5), are not covered.
- **Corrected wording (EXACT).** "In a pure Pauli-stabilizer background whose independent checks number one per qubit, no excitation that cannot be created locally (single or composite) moves in three independent directions; at best in a plane. Locally creatable excitations move freely but carry ordinary translations of the background's lattice, so they get no twist from its repeat."
- **Draft.**
  - **Line 21**, replace the A33 sentences with: "A search for a tidy background that supplies the pattern itself found none: in tidy backgrounds built from flips (stabilizer states) with one condition per place, a disturbance that the background protects (one that cannot be made or removed on its own spot) can at best slide within flat sheets (exact, A33). Ordinary ripples move freely but do not pick up the twist from the background's repeat. One route stays open: an ordinary ripple that behaves differently on the background's sub-grids, which the grid's symmetry allows to get the twist (not built; whether it would then move like light is a further open question);"
  - **Line 309:** "- **No, in every tidy background tried, for a proved reason.** In any tidy background built from flips (a stabilizer state) where each place carries one independent condition, no disturbance that the background protects (one that cannot be made or removed on its own spot) can travel in all three directions; at best it slides within flat sheets (exact). Ordinary ripples, which can be made on a single spot, do travel in three directions, but they cannot pick up the twist from the background's 8-fold repeat this way. Inside the sheets, one background tried, with a uniform minus sign in the rule, supplies the twist. That gives cone-shaped motion within each sheet (never across it), at the energy it costs to make the disturbance, so it is not yet light-like."
  - **Line 310:** "- **Free 3D motion of a protected disturbance needs more conditions than places,** tied together by rules among the conditions (as charge and field lines are tied in the textbook toric code; a comparison, not adopted). In the classes searched, none of the turn-respecting versions pinned every spot down: each left some spot's possibilities free. One reason (A33, exact): turning possibilities along with the grid forces the textbook layout's edge places to use one kind of flip only, which makes them classical."
  - **Decision 17**, A33 sentence: "A tidy background that supplies the pattern itself was searched and not found (A33): in tidy backgrounds built from flips with one condition per place, a disturbance the background protects can at best move within flat sheets. An ordinary ripple that behaves differently on the sub-grids of an 8-fold patterned background remains possible in principle (decision 24)."
  - **Summary:47:** see the corrected summary in section 3.

**C89. MAJOR (draft). The parity route allows the twist; light needs more, and one qubit per place constrains it.**
- **Claims.**
  - Draft:311: "The grid's symmetry allows this to supply the twist everywhere, but no one has built it."
  - Draft:374 (decision 24): "The grid's symmetry then allows the background itself to supply light's twist, possibly sharing one pattern with the gravity field."
  - Draft:21: "One route stays open: a ripple that behaves differently on the background's sub-grids;" (no "not built").
  - A33:40–42 and :160.
  - LOG A33 entry: "That would also reopen sharing with F6."
- **The parity formula is right (EXACT; re-derived, and the coordinator checked it numerically).**
  - Let g fix x and c and swap a ↔ b, with U_g|y⟩ = p(y)|gy⟩ and H invariant. Then t(c→b) = p(c)p(a)·conj t(a→c) and t(b→x) = p(a)p(x)·conj t(x→a).
  - So Φ = |t(x,a)|²|t(a,c)|²·p(x)p(c).
  - In the period-2 layout, only the V–F diagonal (z-even faces) and the E–C diagonal (z-odd faces) half-turns keep the layout. The other diagonal of each face swaps roles. So A33's two conditions p_V ≠ p_F and p_E ≠ p_C are complete, with no extra consistency condition.
- **"Does it reopen sharing with F6?"** As a symmetry statement, yes. The joint system can keep all 24 turns about vertex and cube places, because the turns act on the ripple with site signs instead of requiring an invariant sign pattern. Theorem S (law-level painted signs) is untouched.
- **"Consistent with one qubit per site, given A31 D5?"** Yes, with constraints (EXACT rep theory; CHECKED, `c7` A).
  - D5 concerns relabelling the glued *law's* signs over a product vacuum. Here the law has no signs; the parities are eigenvalues of the turns on the ripple's local state in an entangled, patterned background. Nothing is relabelled, so there is no conflict.
  - At vertex and cube places (group O), one qubit's operators are A1 + T1. A ripple there with a definite parity under all six face-diagonal half-turns needs a creator spread over several places.
  - At edge and face places, σ^axis is A2 of D4, with parity −1 under both diagonal half-turns.
  - So p_V = p_C = +1 (multi-place scalar creators) and p_E = p_F = −1 (one-qubit σ^axis creators) meets both conditions, and every bond amplitude (V–E, E–F, F–C) is symmetry-allowed. A33's suggested assignment (A₂ at V/C, diagonal-even at E/F, A33:160) needs multi-place creators at all four roles; the reverse is cheaper.
- **What is missing for *light* (CHECKED, `c7` B/C; ARGUED beyond the toy).**
  - (i) **Bond strengths do not matter; role energies do.** Unequal bond strengths keep the cone, which answers A33's open edge 2: they neither gap nor split it. But the four roles are separate orbits of the layout, so the ripple's energy at V, E, F and C places is generically different.
    - A staggered energy difference opens a mass gap.
    - Other differences break or split the eightfold cone.
    - A clean, isotropic, massless cone needs all four role energies equal: three tunings that the layout's symmetry does not supply. So the route more naturally gives heavy, Dirac-like matter. That could be welcome for matter (A31 D7 found no clean glued mass), but it is not light.
  - (ii) **The cone must sit at the background's energy.** In a gapped stabilizer background every local ripple costs energy, so the cone sits above the vacuum unless the hop law cancels that cost. That needs tuning, like A31's site-sum-0 gauge (ARGUED).
  - (iii) **Sharing one pattern with F6 needs more room per place.** As built, every place carries field content (C61).
  - (iv) **Records might show the background's pattern.** A33:119 (ARGUED) says z-records on a face site's arms tell #87's translates apart. That weakens the "milder, state-level" ranking.
- **Draft.**
  - **Line 311:** "- **The open hope:** an ordinary local ripple that behaves differently on the different sub-grids of an 8-fold patterned background (a different 'parity' under the half-turns). The grid's symmetry allows this to supply the twist on every face (exact symmetry statement), but no one has built it. Further conditions are known (fifth review's check):
    - on one qubit per place, the ripple at vertex-type and cube-type places must be made by an operator spread over several places;
    - a light-like cone also needs the ripple's energy to be the same on all four kinds of place (otherwise the cone opens a gap or splits), and to cost nothing at the cone.
    So the route may more naturally give heavy matter than light."
  - **Decision 24:** "24. **An 8-fold patterned background for matter.** May matter's empty background carry an 8-fold pattern held in the state (1 of 8, like the field's jobs), so that its ripples can behave differently on the different sub-grids (A33)? The grid's symmetry then allows the background itself to supply the twist light-like matter needs, possibly with the same pattern as the gravity field (which would also need more room per place, decision 13). Not built yet. Whether it gives light rather than heavy matter is open, and records might still show the pattern (argued). It would trade a pattern painted onto the law for a pattern held in the state. A related choice (A33): may the rule carry a uniform minus sign on one kind of term? A33's in-sheet twist needs one."
  - **Line 21:** covered by C88's replacement, which adds "not built".

**C90. MINOR (draft). The layer vacuum's twist gives sheet-bound Dirac cones above the vacuum, and needs a law sign.**
- **Claim.** Draft:309: "Inside such sheets the background can supply the twist, giving light-like motion within the sheet but never across it."
- **What is right (EXACT, `out_a20_flux_4_1.txt`).** The planon's elementary loop equals one edge-role check, with phase s_E. With s_E = −1 it sees π per plaquette (the planon hops by 4 sites), giving 2D Dirac cones inside layers.
- **What is wrong.**
  - "Light-like" overstates it. The cones are confined to sheets and sit at the defect's creation energy, so they are not light-like relative to the vacuum (ARGUED).
  - The twist needs the uniform law sign s_E = −1, an owner decision A33 lists (A33:168) that the draft omits.
- **Draft.** Covered by C88's line-309 text and C89's decision-24 text.

**C91. MINOR (lane). A33 grading details.**
- **The torus blind spot.**
  - A33:143: "Immobility on any even torus larger than the checks implies immobility on Z³, because a Z³ mover wraps to a torus mover."
  - A Z³ mover by v ∈ LZ³ wraps to a closed loop on the L-torus, which the rank test cannot see. Fractal-like codes move only by such vectors (A33's own 24 half-torus movers on L = 16).
  - So "28 pure-looking, all immobile on Z³" (A33:91) and the 5,912 "immobile on L = 6, 8 or 10" are CHECKED for displacements not divisible by the torus sizes tested, not EXACT.
  - This does not affect the 3D conclusion: Theorem C covers every pure candidate.
- **"Every pure".** A33:43 says "every pure one-check-per-site vacuum at |d|² ≤ 2 has … a homogeneous, frustration-free, covariant law". It should say "every *pure-looking* (28)", since purity is CHECKED, not proved. The projector existence (`a19`) is EXACT for those 28.
- **The calm law is very weak.** The law ∏_o(1 − s g_o)/2 penalizes only states violating all 8 translate-checks at a place. Its ground space is very large (it includes the unpatterned star, A33:116). "Calm" is right; "selects the vacuum" would not be.
- **Two kinds of twist.** A33:37 says "It can supply π flux, but only to excitations that move in planes." That is true for the background-charge (projective) twist on the background's own lattice. The parity route gives a different, fine-plaquette twist to 3D-mobile ripples. A33 should say which twist it means.
- **Comparator label.** A33:152 says "The parity escape echoes symmetry fractionalization". The parity route is explicitly non-fractionalized (one state per site, a linear action with site signs). Better comparators: staggered-fermion site phases, and band representations with orbital characters at Wyckoff positions. Either way it is from memory and not adopted.
- **Theorem A (EXACT; re-derived).**
  - One qubit per site plus purity makes M = M^⊥ reflexive of rank 1, so M is free and principal, with u = (a, b) coprime.
  - The 3-fold soldered turn permutes X, Y and Z counts cyclically, so both parities of u at y = (1,1,1) vanish. The augmentation then shows a single defect is never locally creatable.
  - Theorem C bounds the move lattice to rank ≤ 2, and T or O acts irreducibly on Q³, so Λ = 0.
  - Both the soldered 3-fold turn and purity are used. An unglued version can have locally creatable, freely moving single defects.

**C92. MINOR (draft). Line 310 wording.**
- "None of the turn-respecting versions built tonight stayed fully settled" has two problems:
  - "settled" is the draft's word for A24's energy-gentle records (section 6), so reusing it for "pure" confuses;
  - the result is for the classes searched (≤ 2 checks per role, |d|² ≤ 3), not for everything built.
- "Tied together the way electric charge and field lines are tied" is an unflagged comparison.
- Fixed by C88's line-310 text. That text also adds A33's edge lemma (EXACT), the reason soldered turning blocks the textbook layout on one qubit per place.

**C93. MINOR (draft + summary). Scope of "proved" after A33.**
- **Line 301 heading.** "**The two patterns cannot be one pattern with all the field pattern's turns (proved).**" should read "(proved for ripples that behave alike on every sub-grid)". The item's last sentences already say so; the heading should not contradict them.
- **Line 92.** "a background whose spots share their possibilities is open (A33)" becomes "… is partly searched: in tidy backgrounds built from flips, the disturbances it protects stay in flat sheets (A33); other kinds are open."
- **Summary:46.** "The two can be tied together only by giving up half the grid's turns" becomes "A painted pattern can be tied to gravity's only by giving up half the grid's turns." That keeps it consistent with the parity route on line 47.

**C94. MINOR (draft). Decision 24 framing.**
- "May matter's ripples behave differently on different sub-grids …" asks for something that is not a free choice. Whether ripples carry sub-grid parities follows from the background and the law. The owner's choice is whether matter's background may carry an 8-fold state pattern (and share it with the field).
- A33's second decision (a uniform law sign) is missing.
- Fixed by C89's decision-24 text.

### The one-page summary (`MORNING_SUMMARY_DRAFT.md`, checked line by line against v9 and the lanes)

**C95. MAJOR. The headline theorem loses the gluing condition.**
- **Claim.** Summary:12–16 lists the conditions as reversible; next-door reach; one qubit per site; "treating every site and every turn of the grid exactly alike on every tick."
- **What is wrong.** v9:9 and A20/A21's Theorem N need soldered covariance: "with possibilities turning along with the grid (your Q3)". That is hypothesis (iii) of Theorem N (A29 Q-a). Dropping it widens a proved theorem to an unproved one and hides the owner's Q3 from the headline.
- **Replacement, line 16.** "- treating every site and every turn of the grid exactly alike on every tick, with possibilities turning along with the grid (your Q3)."

**C96. MAJOR. Three earlier corrections are undone.**
- **C32 (A29).** Summary:50: "In a ticked toy, matter tied to it bends light by the full amount and falls alike." This brings back the garble ("matter bends light") and drops the condition and the scope.
  - **Replacement:** "In a ticked toy with matter tied to it, light is bent by the full amount (given a supplied choice: the field's time-stretch also paces its own change), and everything whose weight sits at single places falls alike."
- **C61.** Summary:53: "either more settings per place than one qubit, or places that are never recorded". This presents the second option as available; v9:371 says it needs a one-qubit field "(not built)".
  - **Replacement:** "more settings per place than one qubit, or a one-qubit version of the field (not built) whose places are never recorded;"
- **C48.** Summary:55: "Neither ticks nor smooth change give simple particles a preferred handedness (exact)." This drops the scope and "untested".
  - **Replacement:** "Neither ticks nor smooth change give single free particles on a uniform grid a preferred handedness (exact); interactions and record edges are untested."
- **Owner-choice framing (rule d; cf. C33).** Summary:49 says "with its bookkeeping kept exact"; v9:35 says "If its bookkeeping is kept exact (a choice you would make)".
  - **Replacement:** "If you choose to keep its bookkeeping exact, a field of the shared possibilities has its form fixed by the grid's turns to Einstein's linear gravity at long wavelengths. Its speed relative to light and its strength are not fixed."

**C97. MAJOR. Four "must"/limit sentences lose their conditionals.**
- **Influenced tick (C84).** Summary:28: "What must follow gravity exactly is how often records form."
  - **Replacement:** "If clocks that count records are to agree with other clocks near heavy bodies (your choice), how often records form must follow gravity's slowing exactly."
- **Minimum tick (C79).** Summary:31: "No smallest tick follows, only a longest one: shorter than light's time to cross one grid step."
  - **Replacement:** "No smallest tick follows. If one site per tick is to be the limit for all influence, the tick must be shorter than light's time to cross one grid step."
- **Tidy emptiness (C62/C72).** Summary:35: "next to matter the emptiness must be the tidy, lined-up kind, or records creep in and heat it."
  - **Replacement:** "next to matter the emptiness would have to be the tidy, lined-up kind, or recording there would have to build up slowly over many ticks; otherwise records creep in and, if the rule's energy scale is the Planck scale, heat it far beyond what is seen (argued)."
- **"Untouched" (C74; your Q1).** Summary:33, and also v9:38 (bottom-line item 5, which C74 did not reach): "distant light crosses it untouched".
  - **Replacement (both):** "distant light crosses it without ever being recorded there".
- **Smaller (C52).** Summary:22: "The smooth change reaches faintly past next door". Make it: "The smooth change reaches past next door (faintly, if the change per tick is small)".

**C98. MINOR. Summary wording and owner rules.**
- **Line 21 (owner rule a).** Start with "In this option, records step at most one site per tick …".
- **Line 27.** Add the checkerboard's cost and the untried case: "…a checkerboard of two sub-grids half a tick apart, which records can faintly tell apart. … Ticks timed by the surrounding records were not tried."
- **Line 37.** Start with "In the record-tick shape, a fully recorded region …"
- **Line 38.** Add "In a one-line toy,".
- **Line 47.** "Tonight's last search" becomes "A search" (A36 and A37 are still running).
- **Line 57.** "the full list of 24" becomes "the full list, 0 to 24".
- **Line 10.** Review count: see C99.

**C99. MINOR (provenance).**
- After this round, "Four hostile reviews by separate agents" (v9:50) and "Four hostile reviews" (summary:10) should read: "Five rounds of hostile review by four separate agents (the fourth agent reviewed twice; each later round had read the earlier ones)."
- Title: "(v10, after five review rounds)".
- v9:57: "all review rounds".

---

## 3. Corrected one-page summary (drop-in replacement; every sentence checked against v9 and the lanes)

```
## The night in one page

**What we did.** We worked out what your instincts would do, using exact derivations and small computer toys. The instincts:
- records form at set ticks;
- they move at most one site per tick;
- clashes are settled by relative odds;
- the possibilities flow;
- a full region may act like a black hole.

These are explorations of your instincts, not positions: nothing is adopted. Five rounds of hostile review, by four separate agents, attacked the claims, and their corrections are folded in.

**1. A hard limit on motion (exact).** Suppose a change is all of these:
- reversible;
- reaching only next-door sites in one tick;
- built on one qubit per site;
- treating every site and every turn of the grid exactly alike on every tick, with possibilities turning along with the grid (your Q3).

Then nothing can move: not records, not light, not matter. Something has to give.

**2. The most coherent way through: "ticks for records, smooth change for possibilities" (the record-tick shape).**
- **How it works.** In this option, records step at most one site per tick by trading places with an empty neighbour, and the shared possibilities change smoothly in between.
- **It uses two of the limit's ways out at once.** The smooth change reaches past next door (faintly, if the change per tick is small), and records' steps cannot be undone. The two fit together, so records still move at most one site per tick.
- **The price.** Unrecorded influence loses its exact speed limit. A leak always remains, and it stays exponentially faint only if the change per tick is small.

**3. Your tick, in that shape (checked).**
- **No more seams.** The possibilities never notice the ticks, so the earlier troubles (mirror seams, freezing while waiting) disappear.
- **Global or neighbourhood.** A tick written into the rule is the same everywhere if the rule treats every place exactly alike; the only other way is a checkerboard of two sub-grids half a tick apart, which records can faintly tell apart. Set ticks that differ by place needed a per-place memory in every construction tried; ticks timed by the surrounding records were not tried.
- **Influenced.** The tick can be influenced by gravity. If clocks that count records are to agree with other clocks near heavy bodies (your choice), how often records form must follow gravity's slowing exactly.
- **Visible?** With the small chances per tick that freezing and heating already require, the choice is far too faint to see.
- **Light.** If records form only next to records, the tick never touches how light crosses empty space.
- **Minimum tick.** No smallest tick follows. If one site per tick is to be the limit for all influence, the tick must be shorter than light's time to cross one grid step.

**4. Empty space (exact, within the toys).** If records form only next to records, empty space far from matter is exactly quiet whatever it is made of, and distant light crosses it without ever being recorded there. The price:
- the world must start with some records;
- next to matter the emptiness would have to be the tidy, lined-up kind, or recording there would have to build up slowly over many ticks; otherwise records creep in and, if the rule's energy scale is the Planck scale, heat it far beyond what is seen (argued).

**5. Your black-hole idea (checked).** In the record-tick shape, a fully recorded region is a place where no record can form or move again, and no record or possibility from outside reaches in (gravity may still). With one stepping choice it never wears away, but that choice also freezes lone records in empty space.
- **Grey, not black.** In a one-line toy, at the catching strength best for fast things, it catches those almost always and bounces slow ones.
- **No glow.** What it caught stays as records on its skin, in plain view, and a sealed region gives off nothing.
- **Clocks inside: open.** Whether gravity's clocks stop inside depends on your choices and on strong gravity, which is not worked out.

**6. What the shape does not yet give.**
- **Light and matter.**
  - Over the calm, all-pointing-one-way background, a rule that treats every spot and turn alike moves single ripples only like slow, heavy particles, never like light (exact for single ripples).
  - Light-like matter then needs a pattern of plus and minus signs painted onto the rule.
  - In the version that keeps your gluing, that pattern cannot keep the turns that gravity's pattern keeps (proved). A painted pattern can be tied to gravity's only by giving up half the grid's turns.
  - A search for a tidy background that supplies the pattern itself found none: in tidy backgrounds built from flips, with one condition per place, a disturbance the background protects can at best slide within flat sheets (proved, A33). One route stays open: an ordinary ripple that behaves differently on the sub-grids of an 8-fold patterned background, which the grid's symmetry allows to get the twist (not built). Whether it would then move like light is open: its energy would have to be the same on all four kinds of sub-grid place.
- **Gravity.**
  - If you choose to keep its bookkeeping exact, a field of the shared possibilities has its form fixed by the grid's turns to Einstein's linear gravity at long wavelengths. Its speed relative to light and its strength are not fixed.
  - In a ticked toy with matter tied to it, light is bent by the full amount (given a supplied choice: the field's time-stretch also paces its own change), and everything whose weight sits at single places falls alike.
  - The costs:
    - a fixed 2×2×2 pattern of jobs (1 of 8 layouts);
    - more settings per place than one qubit, or a one-qubit version of the field (not built) whose places are never recorded;
    - almost all records formed gently, on caught, settled things (one working toy: "catch first, record later").
- **Handedness.** Neither ticks nor smooth change give single free particles on a uniform grid a preferred handedness (exact); interactions and record edges are untested.

**The decisions that matter most (all yours; the full list, 0 to 24, is at the end)**
- **(0)** Do you want the record-tick shape, at the price of no exact speed limit for unrecorded influence?
- **(4)** Records form only next to records?
- **(13)** May a place hold more than one qubit's worth, for gravity?
- **(17)** Is a painted-on sign pattern acceptable for light and matter, and which version?
- **(18)** Is "records form at set ticks" a physical statement or bookkeeping, and did "minimum tick" mean a smallest or a longest tick?
```

---

## 4. Sentences that are fine as they are

- **Summary.** Lines 3–8, 13–15, 18, 20, 23, 26, 29, 30, 34, 39, 40, 44, 45, 52, 54, 58–62.
- **Owner rules in the summary.** The instincts are listed as instincts (lines 3–10). No beat is adopted (line 62 quotes "records form at set ticks" as yours). No "read" possibility. No import presented as adopted. Q7 is not touched.
- **Draft v9.**
  - Line 301's parity sentence is accurate as a symmetry statement; only the heading needs scope (C93).
  - Line 308's heading.
  - Lines 295–300 and 302–307, as applied from the fourth review.
  - Decision 17's first five sentences.
  - Decision 23.
  - Line 376's footer.
- **A33.**
  - The Answer's statement of Theorem C (A33:27, with "superselected").
  - Theorem A (A33:31).
  - The certificate logic ("an anticommuting pair, each commuting with every Z³ check").
  - The parity formula (A33:73–76).
  - The calm-projector existence and the general lemma (A33:113, :117).
  - The honest "pure-looking = CHECKED" lesson (A33:141).
  - The flagged comparators other than A33:152.

---

## 5. New open questions for the owner (plain language)

1. **Heavy or light from the 8-fold background?** If matter's empty background carried an 8-fold pattern held in the state, the grid's symmetry would let it give ripples the twist. But unless the ripple costs the same on all four kinds of place, the result is heavy matter, not light. Would heavy matter from this route be welcome (it supplies a mass the painted version lacked), or is light the point (C89)?
2. **Protected or ordinary disturbances?** Tonight's proof says disturbances that the background protects cannot roam in 3D in the tidy backgrounds tried; ordinary ripples can. Should matter be protected disturbances, which would need a charge-and-field-line kind of background (blocked so far on one qubit per place by the turning-along requirement), or ordinary ripples with sub-grid labels (C88)?
3. **A uniform minus sign in the rule?** A33's in-sheet twist needs one. Is a uniform sign on one kind of term acceptable as "treating every place alike" (C90, C94)?

---

## 6. Lane and LOG wording fixes

| Location | Old | New |
|---|---|---|
| A33:37 | "only to excitations that move in planes" | "as a background-charge twist on its own lattice, only to excitations that move in planes; the sub-grid-parity twist (below) is a different mechanism" |
| A33:43 | "every pure one-check-per-site vacuum" | "every pure-looking (28) one-check-per-site vacuum" |
| A33:91 | "all immobile on Z³" | "immobile on the tori tested (displacements not divisible by the torus size)" |
| A33:143 | "Immobility on any even torus … implies immobility on Z³" | add "for displacements not in LZ³ (a mover by v ∈ LZ³ wraps to a closed loop)" |
| A33:152 | "echoes symmetry fractionalization" | "echoes staggered-fermion site phases and orbital characters in band representations (COMPARATOR)" |
| A33:160 | "pseudoscalar (A₂) at vertex and cube sites and diagonal-even at edge and face sites" | add "or the cheaper reverse: scalar at vertex and cube (multi-place creators), σ^axis at edge and face (one qubit; A2 of D4)" |
| LOG (A33 entry) | "That would also reopen sharing with F6." | add "as a symmetry statement; light-like cones additionally need equal role energies (A34 c7) and more room per place for sharing" |

**Script.** `c8/A34/c7_parity_route.py`, with `out_c7_parity_route.txt` and `time_c7_parity_route.txt` beside it.
