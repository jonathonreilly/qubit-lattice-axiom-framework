# A34 hostile review, round 8 (REVIEW4): A38, A39 and the doc's late text

**Scope.** This round covers:
- A38: D1, D2, D5 (the half-turn argument and its scope), D6, the D4 narrowing and D7.
- A39: Theorem T, Lemma V, the twist and positivity lemmas, the grading of "frustration-free ⇒ z ≥ 2", the escapes (especially (e)) and c1's fragility numbers.
- MORNING_DRAFT.md (05:52): sections 12 and 13 (lines 349–370), and the A38 sentence at the end of line 331.
- MORNING_SUMMARY_DRAFT.md (05:52): the A38/A39 sentences in line 48.

**Sources.** I worked only from primary files:
- A38: REPORT.md, A38_PROMPT.md and toys/verify_A38.py.
- A39: REPORT.md, A39_PROMPT.md, the code and output of c1–c3, and toys/verify_A39_edge.py.
- LOG.md lines 1727–1870.

**Rules followed.** I ran no git, made no repo edits and did not touch any other agent's files or the draft. All scripts are in `SP/c8/A34/`.

**Counts.** 6 MAJOR (C116–C121), 10 MINOR on doc text (C122–C131), 1 OPTIONAL outside the requested scope (C132), and 1 MINOR on lane and LOG wording (C133).

## Verdicts

### A38: holds, with narrowings

- **D1 (EXACT): holds.**
  - I re-derived the orbit–stabilizer step. A site stabilizer must fix a direction, so it is cyclic, with order 1–4. Orbits then have size 24, 12, 8 or 6. With 8 sites, the only option is one orbit with stabilizer C3, which puts every direction on a body diagonal.
  - Corollary: no site is fixed by a face-diagonal half-turn, because a C2 stabilizer needs an orbit of 12 > 8.
  - Scope: period 2, product textures, and all 24 turns acting up to a translation.
- **D2 (EXACT): holds.** The double-flip amplitude vanishes only at K = J, D = 0. The coordinator's check confirms this.
- **D3 (EXACT): holds.** I re-derived the bond map (J, K) → (−J, 2J + K) and the image of H8, which is Néel order along (111).
- **D5 (EXACT): holds, with a stated scope.**
  - I checked by hand that the half-turn g: (x,y,z) → (1−x, z, y), with R = [[−1,0,0],[0,0,1],[0,1,0]], maps H8 exactly to itself (R·m(g⁻¹r) = m(r)) and swaps the ends of the bond (0, e_x).
  - So each nearest-neighbour hop has its phase pinned mod π, for every homogeneous glued law of any range and body number. This holds for single ripples at harmonic order, on nearest-neighbour faces, whenever nearest-neighbour hops are nonzero.
  - The argument does not settle loops through longer hops. A similar half-turn pins face-diagonal hops; distance-2 hops are not obviously pinned.
- **D6 (CHECKED): holds as graded.**
  - The isotropic point has 2 + 2 linear modes (E = ±1.938|q|), 4 heavy modes beside them, and 2 heavy zone-centre zero modes. Its nearest-neighbour hop is 0.028.
  - Its negatives (no isotropy with a large NN hop; no full 8-mode Dirac cone) come from searches, so they are CHECKED, not EXACT, as A38 itself says.
- **D4 narrowing of A31: legitimate but partial.**
  - It shows an isotropic linear touching without π per face when longer hops dominate.
  - It is not a full cone. It needs tuning, and it sits on a vacuum that is not the lowest state (C116).
  - Grade the narrowing CHECKED.
- **D7 (CHECKED): holds.**
  - Under the pair law, only +m records keep H8 calm.
  - An 8-dimensional star subfamily also keeps −m records calm. The draft omits this (C128).
  - The quiet weight 1 − P is EXACT.
- **D8 (EXACT arithmetic): holds.** Readability is relative to other placed structure.
- **New, cross-lane (EXACT; my check c11): H8 is never the calmest state where it offers moving zero-cost ripples.** See C116.

### A39: holds; the doc overstates it

- **Lemma Q and the counterexamples (EXACT): hold.**
- **Lemma V (EXACT): holds.** I re-derived it. Visibility plus quietness gives h_yΩ = 0 for every y, so H − E₀ ≥ 0 and Ω is a frustration-free ground state.
- **Twist lemma, frustration-free version (EXACT): holds.** I re-derived steps 1–4:
  - h_y^{1/2} has the support of h_y;
  - the commutator sum is limited to |x − y| ≤ R;
  - for k ≠ 0, A_kΩ is orthogonal to Ω by momentum.
- **Twist lemma, clustering version (EXACT): holds.**
- **Positivity lemma (EXACT): holds.** The q → −q argument needs no Rellich: any first-order splitting M(q) has M(−q) = −M(q).
- **Theorem T (EXACT): holds, with a limited conclusion.**
  - It bounds only the softest ripple near the twist momentum k₀: that ripple's energy is at most quadratic.
  - It does not exclude a linear branch above it.
  - It assumes T4 (zero cost carried by a local twist). The lane itself names RK-type, ice-like vacua as the uncovered gap.
- **"Frustration-free ⇒ z ≥ 2" is graded correctly in the lane.** The core is EXACT under T4 or clustering; the general published theorems are COMPARATOR with unverified hypotheses. The draft mis-grades it (C119).
- **Escapes.**
  - **(e)** The construction is EXACT. Its cost 3, "matter number must be exactly conserved", is stronger than the argument needs (C133). Terms that create matter only where matter already is keep the vacuum exactly quiet. The draft's own rendering, "matter that never appears out of empty space", is the accurate one.
  - **(f)** Holds. It needs Ω to be the ground state, which the draft omits (C123).
  - **(b)** CHECKED. A39's ring gives 1.05e-2; the coordinator's open chain gives 6.1e-3 and 5.9e-3. These are different geometries, both full rank.
  - **(c)** EXACT for pairs, ARGUED for n ripples, CHECKED on 64². The draft grades it only as "checked" (C124).
  - **(a)**
    - "Energies drop below the vacuum" is EXACT.
    - "Needs a painted sign pattern" is true of A39's toy only; A38's H8 is a counterexample (C120).
    - The c1 numbers replicate exactly in my own code, but the comparison is confounded: the control vacuum is gapped (C120, my check c12).

## What I ran

All runs used `nice -n 10` with the four thread caps at 1. The 1-minute load was 2.47–5.64 at run time, always under 6.

| Script | Toy | Result | Time, memory |
|---|---|---|---|
| `c11_h8_not_ground.py` | One-flip block over H8 on a 4³ torus, calm pair law J(σ·σ + σ^aσ^a), J = ±1 | Double-flip amplitude 2.0e-16 (calm). One-flip energies relative to H8 run from −8.0000 to +8.0000; 27 of 64 lie below zero; the spectrum is symmetric about 0. Identical for J = +1 and J = −1. | 0.20 s, 28 MB |
| `c12_fragility_control.py` | A39 c1's toy, rebuilt in my own code: 4×3 π-flux torus, 12 qubits, the same slow on-off cycle of δΣX (period 400, dt = 0.5) | See the table below | 3.6–6.2 s per run, ≤ 96 MB |

c12 results:

| Vacuum | Lowest excitation above E_Ω | States within 0.05 of E_Ω | Return at δ = 0.10 | Return at δ = 0.03 | Flips per lost unit of weight |
|---|---|---|---|---|---|
| No field (not lowest; replicates A39) | −8.96 | 139 | 0.7192 | 0.9904 (A39's figure) | 3.7 at δ = 0.10; 2.1 at δ = 0.03 |
| Field W + 0.5 (A39's control; replicated) | +0.50 | 0 | 1.0000 (flip density 3.31e-8) | n/a | n/a |
| Field W + 0.1 (lowest, smaller gap) | +0.10 | 0 | 0.9853 | not run | n/a |
| Field W exactly (lowest, gapless) | 0.00 | 1 | 0.0385 | 0.9882 | 1.00 at both strengths |

- **Why c11 is EXACT, not just CHECKED.** H8 is a calm spin-1/2 product state, so the one-flip block is the exact compression of H − E₀. A38 D4 gives on-site cost 0 and hops of size 2|J|, so the block is traceless and nonzero and must have a negative eigenvalue for either sign of J. By the variational principle, H8 is not the ground state.
- **What c12 shows.** A39's 100% control is protected by its gap. Made the lowest state without a gap, the same toy is disturbed as much or more: 99% return at δ = 0.03 and 4% at δ = 0.10. What separates the two cases is where the lost weight goes. The excited vacuum loses into many-flip states (pairs, consistent with A39's mechanism); the gapless lowest-state control loses into its single zero-cost ripple.

## Findings

### C116 — MAJOR (cross-lane): A38's background is calm but not the calmest state; sections 12 and 13 never connect them

- **Where.** Draft line 353 (section 12) and the gap between lines 356 and 357. It bears on line 366 (section 13).
- **Quote (line 353).** "**One simple rule keeps it calm (exact; my check).** The neighbour rule must be one particular equal mix of "line up" and "line up along the link's own direction". Every other simple mix I tried disturbs it."
- **What is wrong.**
  - **H8 is not the lowest state under its calm pair rule, for either sign (EXACT; c11).** Its ripple spectrum is symmetric about zero: 27 of 64 one-flip states lie below it on 4³.
  - **The same holds at the partly light-like point and at every zero-cost linear touching.** At the tuned point the slopes are −1.938 (×2) and +1.938 (×2). In general, a linear touching forces negative energies (A39's positivity lemma; EXACT).
  - **So everything A38 offers light sits inside A39's escape (a).** Records cannot track energy there (Lemma V), and the vacuum is degenerate with a zero-energy continuum of ripple pairs: at harmonic order the bands are ±|f(k)| with f even, so pairs (k, +E) and (−k, −E) cost nothing. Any departure from K = J, D = 0 creates such pairs (ARGUED).
  - **The draft hides this.** It uses "calm" in section 12 (unchanging) and "calmest" in section 13 (lowest energy) with no bridge between them, so a reader can take H8 to be both. "Every other simple mix I tried" also undersells D2, which is EXACT for every mix of the pair terms.
- **Corrected wording.**
  - Calm means unchanging, and H8 is calm under one pair rule (EXACT).
  - H8 is not the lowest state of that rule, or of any rule giving it zero-cost moving ripples (EXACT).
  - Hence section 13's third way out applies (EXACT), and fragility follows (ARGUED).
- **Replacement text.**
  - Replace line 353 with:
    > - **One simple rule keeps it calm (exact; my check).** Among rules built from pairs of neighbours, exactly one keeps it unchanging: an equal mix of the ordinary neighbour coupling and the coupling along the link's own direction, with either overall sign. Every other mix of these pair terms, including the handed one, disturbs it (exact). Calm here means unchanging, not lowest in energy (see below).
  - Insert after line 356:
    > - **Calm, but not the calmest state (exact; fourth review's check).** Under its calm pair rule, of either sign, this background is not the rule's lowest-energy state: its ripples come in pairs of equal and opposite energy, so some cost less than nothing (on a 4×4×4 grid, 27 of 64 single-ripple states lie below it). The same is true at the partly light-like point, and wherever ripples leave a zero-cost point at a steady speed: such motion always brings energies below the background (A39's positivity lemma). So everything this background offers light falls under section 13's third way out: records cannot track energy, and the background sits among zero-cost pairs of ripples that a small change of the rule could create (argued).

### C117 — MAJOR: line 331 says A38 "tested the simplest version" of the open route, but A38 shows the route cannot be set up on pointing backgrounds at all

- **Where.** Draft line 331, the last sentence of section 10's "open hope" bullet.
- **Quote.** "A late lane (A38, section 12) tested the simplest version, a background whose spots simply point different ways: its ripples feel a third of a turn, never the half turn."
- **What is wrong.**
  - The route needs places fixed by face-diagonal half-turns, because its parity labels p(x) and p(c) are defined at those places.
  - H8 has none: 0 of 48 such half-turns fix a site (A38 D1). A38 itself says "A33's parity route does not apply".
  - By D1 and A38's note that "A25's role layout cannot be a product texture", no 2×2×2 background whose spots each point one way can carry the route's labels (EXACT).
  - So A38 did not test the route and see it fail. It showed the route needs a different kind of background. That moves the route toward shared-possibility backgrounds (decision 23) or more room per place, which is decision-relevant.
  - "Never the half turn" also implies the half turn is required, which holds only for nearest-neighbour hopping (C118).
- **Corrected wording.** The route cannot use pointing backgrounds with the 8-fold repeat (EXACT). The route itself is untested; it needs shared possibilities or more room per place (ARGUED).
- **Replacement text** for that sentence of line 331:
  > A late lane (A38, section 12) found that this route cannot use a background whose spots each simply point one way: the only such 8-fold background that respects every turn has no half-turn holding a spot fixed, so the sub-grid labels the route relies on cannot arise (exact; its ripples get a third of a turn per face instead). The route itself is still untested: it needs a background whose spots share their possibilities, or more room per place (argued).

### C118 — MAJOR: "the half turn light needs" holds only for nearest-neighbour hopping, and contradicts the section's own light-like point

- **Where.** Draft lines 350, 354 and 356. The summary's version is fixed in C121.
- **Quotes.**
  - Line 350: "The background-held pattern of section 10 does not give light here: ripples always feel a third of a turn on each face, never the half turn light needs (exact)."
  - Line 354: "...under every rule that treats every spot and turn alike. My check found exactly this on every face for several rules. So the open route of section 10 does not work for this background: no half-turn of the grid holds one of its spots fixed in the needed way."
  - Line 356: "...some ripples move at the same speed in every direction at zero cost, but heavy, slow ripples sit at the same spot and energy beside them."
- **What is wrong.**
  - A38 D6 states the narrowing itself: "An isotropic cone needs π per face" holds only for nearest-neighbour hopping.
  - The tuned point reaches isotropic linear motion with the face twist still a third of a turn, because its nearest-neighbour hop is tiny (0.028, against slopes of 1.94).
  - So line 350's "the half turn light needs" contradicts line 356 two bullets later.
  - "(exact)" on "does not give light" is too strong: the third-of-a-turn twist is exact, but the light-like point is CHECKED.
  - Line 354 omits D5's condition that nearest-neighbour hops are nonzero, and its "does not work" reads as a failed test (C117).
- **Corrected wording.**
  - The nearest-neighbour face twist is ±2π/3 under every glued law, whenever nearest-neighbour hops are nonzero (EXACT). So nearest-neighbour hopping gives no light-like cone (EXACT).
  - Farther hops give a partly light-like point without π (CHECKED). It has heavy partners and sits on a non-lowest background (EXACT).
- **Replacement text.**
  - Line 350:
    > The one background of this kind does not give clean light. Its ripples feel a third of a turn on each square face, never a half (exact), so with hops between nearest neighbours only they cannot form light-like cones. With richer, finely tuned rules a partly light-like point appears without the half turn (checked), but heavy ripples sit beside it, and this background is not the calmest state of these rules, which puts it under section 13's third way out (exact).
  - Line 354:
    > - **A third of a turn, never a half (exact; my check).** Ripples circling any square face pick up a twist of a third of a turn, with the sign alternating from face to face, under every rule that treats every spot and turn alike, whatever its reach, as long as ripples hop between nearest neighbours at all. My check found exactly this on every face for several rules. The half turn is what light-like cones need when ripples hop only between nearest neighbours; ripples that hop farther are not bound by it (next points). The open route of section 10 cannot even be set up on this background: no half-turn of the grid holds one of its spots fixed, so the sub-grid labels it relies on do not arise.
  - Line 356:
    > - **A partly light-like point, with tuning (checked).** With richer three-spot rules and carefully chosen strengths, some ripples leave a zero-cost point at the same speed in every direction, without the half turn: they travel mainly by longer hops, and the nearest-neighbour hop that carries the third of a turn is tiny there (0.028, against a speed of 1.94). Heavy, slow ripples sit at the same spot and energy beside them, and half of the light-like ripples have negative energy (next point). No sign pattern is painted on, but the background, the extra kinds of rule terms and finely set numbers are all put in by hand.

### C119 — MAJOR: section 13's opening overstates Theorem T (softest ripple only; T4 hidden; the general claim mis-graded as derived)

- **Where.** Draft lines 361, 362 and 363.
- **Quotes.**
  - Line 361: "Not if records can sense the rule's energy directly and empty space is its calmest state: then the gentlest ripples spread slowly, like waves in a magnet, never like light (exact, under stated conditions)."
  - Line 362: "...and the ripples are of the usual kind. Then empty space must be the rule's calmest state, and the rule must be calm at every spot of it. Such rules only allow ripples whose energy grows with the square of their wavenumber: slow and heavy-like, not light. This was derived in the lane; published results agree (a comparison, not adopted)."
  - Line 363: "**Three ways out, each with a price.**"
- **What is wrong.**
  - **"Only allow ripples whose energy grows with the square" is false as stated.** T bounds the softest ripple near k₀: ε(k) ≤ (C/s₀)|k−k₀|², which means no faster than quadratic, and softer is allowed. A39's own wording is exact: "no z = 1 ripple is softest at k₀". A light-like branch above a slower one is not excluded; it would come with a slow companion.
  - **"The ripples are of the usual kind" hides T4.** T4 requires the zero cost to come from a local twist. The lane names its gap explicitly: a frustration-free vacuum with no zero-mode twist, such as RK-type ice-like states (A39 open edge 1). That is the case nearest the program's photon work.
  - **"Derived in the lane" applies only to the core under T4 (or the clustering version).** The general "frustration-free ⇒ z ≥ 2" is COMPARATOR, recalled from memory with unverified hypotheses, so "published results agree" overstates it.
  - **"Like waves in a magnet" is ambiguous.** A39's light-carrying comparator, the antiferromagnet, is itself a magnet with linear ripples. The intended comparison is the aligned magnet.
  - **The headline lists "empty space is its calmest state" as a hypothesis.** Under visibility it is a consequence (Lemma V), as line 362 says.
  - **"Calm at every spot" clashes with the doc's use of "calm" for unchanging.** Frustration-free means each local piece is at its lowest.
- **Corrected wording.** Under visibility, quietness and a local-twist origin of the zero cost, the vacuum is the frustration-free ground state and the softest ripple near k₀ is at most quadratic (EXACT). Faster branches above it are not excluded. The no-twist case is not covered, and the general theorems are COMPARATOR.
- **Replacement text.**
  - Line 361:
    > Not as its gentlest ripple, if records can sense every part of the rule's energy and the ripples' zero cost comes from a local change of empty space: then quiet empty space is automatically the rule's calmest state, and its gentlest ripples spread no faster than ripples in a magnet whose spins all point one way, so anything light-like would sit above slower ripples (exact, under these conditions).
  - Line 362:
    > - **The tension, made exact.** Suppose three things hold: whatever triggers records can sense every part of the rule's energy; empty space is exactly quiet; and the zero cost comes from a local change of empty space that costs nothing when made everywhere in step (as turning a whole magnet costs nothing). Then empty space must be the rule's calmest state, every local piece of the rule must already be at its lowest there, and the gentlest ripple's energy grows no faster than the square of its wavenumber: slow and heavy-like, not light (exact; derived in the lane). The proof limits only the gentlest ripple: a faster ripple above it is not ruled out, but would come with that slower one. Empty space whose zero cost does not come from such a local change, as in ice-like states, is not covered. Every known example of exactly quiet, gapless empty space is slow, including ice-like states at their one exactly quiet point, but the conditions of the general published results were not checked (a comparison recalled from memory, not adopted).
  - Line 363:
    > - **Three ways out found, each with a price** (besides the uncovered kind of empty space above).

### C120 — MAJOR: escape (a) is said to need a painted pattern (contradicted by A38), and its fragility figures compare against a gapped control

- **Where.** Draft line 366.
- **Quote.** "**Empty space not the calmest state.** It is possible, but it needs a painted sign pattern and lets energies drop below the vacuum's. It is also fragile: in the toy it survived a gentle passing disturbance only 72% of the time, against 100% for a calmest-state vacuum."
- **What is wrong.**
  - **The painted pattern is not needed in general.** A38's H8 is a stationary, non-lowest vacuum with linear zero-cost ripples and no painted pattern (C116). A39's "it needs a painted sign pattern (A31)" is true of its own toy only, so the doc's two late sections contradict each other.
  - **The 100% comes from a gapped vacuum.** A39's control field is W + 0.5, which also opens a gap of 0.5. My c12 rebuilt the toy and replicated both of A39's numbers.
  - **A gapless lowest-state vacuum does no better.** With the field set exactly to W, the vacuum is still the lowest state but gapless, as any light-carrying vacuum must be. It returned 0.9882 at δ = 0.03 and only 0.0385 at δ = 0.10.
  - **What does discriminate is the kind of loss and the zero-cost count.**
    - Kind of loss: the excited vacuum's loss goes into many-flip states (3.7 flips per lost unit at δ = 0.10; 2.1 at δ = 0.03), while the gapless control's loss goes into one zero-cost ripple (1.00).
    - Zero-cost count: 139 states lie within 0.05 of the excited vacuum's energy, against 0 for the gapped lowest-state version and 1 for the gapless one.
  - **Two smaller points.** "Only 72%" quotes the stronger nudge only (it is 99% at δ = 0.03), and the toy size is not given.
- **Corrected wording.**
  - Painted pattern: true of A39's example only; A38 is a state-pattern example.
  - Energies below the vacuum, so no energy tracking: EXACT.
  - Fragility: ARGUED from the zero-cost pair continuum (139 vs 0 states, CHECKED). The survival percentages do not isolate it (CHECKED, c12).
- **Replacement text** for line 366:
  > - **Empty space not the calmest state.** It is possible. A39's example paints a sign pattern on the rule; A38's background (section 12) is a second example, using a pattern held in the state, extra rule terms and fine tuning instead. Either way, energies can drop below empty space's, so records cannot track energy (exact). It is probably fragile (argued): it sits among zero-cost pairs of ripples, one with positive and one with negative energy, which any sideways nudge can create (A39's 12-spot toy: 139 states within 0.05 of its energy, against none once a field makes it the calmest state). The toy's survival figures are weaker evidence. Under a slow sideways nudge it survived 99% of the time at the weaker strength and 72% at the stronger, against 100% for the calmest-state version, but that field also opens a gap. Made the calmest state with no gap, the same toy kept 99% and 4%, though its loss went into one zero-cost ripple rather than into pairs (fourth review's check).

### C121 — MAJOR: the summary's A38/A39 sentences carry the same overstatements

- **Where.** MORNING_SUMMARY_DRAFT.md line 48, its last two sentences.
- **Quote.** "A late lane (A38) found that the one patterned background whose spots simply point different ways gives ripples a third-turn twist, never the half turn. Another (A39) found that exactly quiet empty space cannot carry light if records can sense its energy directly and it is the calmest state; light escapes only by being invisible to records (recorded through matter), by slow energy-selective recording with a memory per spot, or by empty space not being the calmest state."
- **What is wrong.** These sentences repeat the problems found above:
  - the A38 result is presented as a failed test of the route, and the half turn as a universal need (C117, C118);
  - A38's background is not the calmest state, which goes unsaid (C116);
  - "cannot carry light" should be "not as the gentlest ripple" (C119);
  - the T4 condition is hidden (C119);
  - "light escapes only by" omits the uncovered case (C119).
  - "The one patterned background" also omits "that respects every turn" (D1's condition).
- **Corrected wording.** As in C116–C119, compressed.
- **Replacement text** for the last two sentences of line 48:
  > A late lane (A38) found that this route cannot use a background whose spots each simply point one way: the only such background that respects every turn gives its ripples a third of a turn per face, never the half turn (exact). Its partly light-like point, reached with finely tuned richer rules, has heavy ripples beside it, and the background is not the calmest state of its rules. Another lane (A39) found that if records can sense every part of the rule's energy, exactly quiet empty space is automatically the rule's calmest state, and its gentlest ripples are then slow, never light (exact, when the zero cost comes from a local change of empty space; ice-like empty space is not covered). The ways out found: light invisible to records (recorded only through matter), slow energy-selective recording with a memory per spot, or empty space that is not the calmest state, which is where A38's point sits.

### C122 — MINOR: escape (e) wording — comparisons unlabelled, an ambiguous aside, a law-only pattern and a missing cost

- **Where.** Draft line 364.
- **Quote.** "**Light invisible to records.** Records form only on matter, and light is noticed only when matter absorbs it, which is how photons are actually detected. The price: places that never record, a law that treats kinds of places differently, and matter that never appears out of empty space (real physics does allow that)."
- **What is wrong.**
  - **The photon-detection remark is a comparison but is not labelled.** A39 grades it COMPARATOR.
  - **"Real physics does allow that" can be read backwards.** It can mean either that real physics allows matter never to appear, or that it allows matter to appear. The comparator is vacuum pairs plus pair creation from light.
  - **"A law that treats kinds of places differently" is too narrow.** A39 says the pattern can be law-level or state-level. With neighbour-pair rules it must be written into the law; star terms are untested.
  - **A39's cost 4 is dropped.** Matter over a quiet matter vacuum has one analytic band: heavy matter is fine, but massless matter with a filled sea is excluded.
- **Replacement text** for line 364:
  > - **Light invisible to records.** Records form only on matter, and light is noticed only when matter absorbs it (in real physics, photons are detected this way; a comparison). The price: places that never record; two kinds of places, which with neighbour-pair rules must be written into the rule itself (richer rules are untested); no matter may ever appear out of empty space, not even briefly or from light (real physics does let matter pairs appear that way; a comparison); and matter over its quiet empty background can be heavy but not massless with a filled sea.

### C123 — MINOR: escape (f) omits that it needs the calmest state, and is inconsistent with section 7 on memory

- **Where.** Draft line 365.
- **Quote.** "**Slow, energy-selective recording.** Records form only when energy is actually delivered, slowly, as real detectors do. Empty space is then almost, not exactly, quiet. The price: a small memory at every spot, which the axioms do not supply."
- **What is wrong.**
  - "As real detectors do" is a comparison and is not labelled.
  - A39 says (f) needs Ω to be the ground state, so it cannot be combined with escape (a).
  - Section 7 (line 270) adds "A memory made of matter is not ruled out"; section 13 should match.
- **Replacement text** for line 365:
  > - **Slow, energy-selective recording.** Records form only when energy is actually delivered, slowly, as real detectors do (a comparison). Empty space is then almost, not exactly, quiet, and it must be the calmest state, so this cannot be combined with the third way out. The price: a small memory at every spot, which the axioms do not supply (a memory made of matter is not ruled out, section 7).

### C124 — MINOR: the pair-ripple result is under-graded and missing its conditions

- **Where.** Draft line 368.
- **Quote.** "Light built from pairs of slow ripples is still slow at the bottom (checked on a 64×64 grid)."
- **What is wrong.**
  - A39 (c) proves this for pairs: the continuum bottom is ≤ 2ε(K/2), and isolated bound states are analytic and ≥ 0. That part is EXACT; the n-ripple case is ARGUED.
  - The result holds over a calmest-state vacuum that conserves flip number. The draft gives no conditions.
  - A linear branch can only be embedded above the bottom.
- **Replacement text** for line 368:
  > - Light built from pairs of slow ripples, over a calmest-state empty space that keeps the number of flips fixed, is still slow at the bottom (exact for pairs, argued for bigger groups, checked on a 64×64 grid). A light-like branch could only sit above that slow bottom.

### C125 — MINOR: "never exactly quiet" overclaims from one tested emptiness

- **Where.** Draft line 369.
- **Quote.** "A light-carrying emptiness next to a record is never exactly quiet: in my check its smallest edge value is about 0.006, while the aligned emptiness gives zero."
- **What is wrong.**
  - Only the antiferromagnet was tested (in 1D, plus a frustrated 2D rank check).
  - A39 itself says exact edge quietness can occur "at most at isolated λ" (ARGUED), and it lists edge buffers as open (open edge 4).
  - The 0.006 is the coordinator's open chain; A39's ring gives 1.05e-2. Both are fine, but the difference should be visible.
- **Replacement text** for line 369:
  > - "Records form only next to records" moves the problem to matter's edges. The light-carrying emptiness tried, a magnet whose neighbouring spins point opposite ways, is not exactly quiet next to a record: in my check its smallest edge value is about 0.006 (A39's ring gives 0.01), shrinking but not vanishing as the record's pull is made stronger, while the aligned emptiness gives zero. Exact quietness there could happen at most at special pull strengths (argued); whether a record's surroundings can be made exactly quiet while light passes farther out is open.

### C126 — MINOR: the decision line misses A38 and decision 23

- **Where.** Draft line 370.
- **Quote.** "**A further decision for you.** Which way out, if any? (Light invisible to records ties to decisions 21 and 24; slow energy-selective recording ties to decision 9, memory.)"
- **What is wrong.**
  - Escape (a) has no tie. It connects to decision 17 (A31's painted pattern), to decision 24 (state patterns), and to A38's background.
  - Decision 23's shared-possibility background, with the plain rule, is not frustration-free. So under visibility it cannot be exactly quiet (Lemma V; EXACT). This bears directly on that decision's "Is it worth exploring?".
- **Replacement text** for line 370:
  > - **A further decision for you.** Which way out, if any? (Light invisible to records ties to decisions 21 and 24; slow energy-selective recording ties to decision 9, memory; empty space that is not the calmest state ties to decisions 17 and 24 and covers A38's background. The shared-possibility background of decision 23, with the plain rule, falls under this result too: if records can sense its energy, it cannot be exactly quiet.)

### C127 — MINOR: "zero-cost ripples run along lines" reads as motion along the diagonals

- **Where.** Draft line 355.
- **Quote.** "**What its ripples do.** With the simple rule, the zero-cost ripples run along lines (the cube's long diagonals), not light-like cones."
- **What is wrong.**
  - The nodal lines are lines of wave patterns (momentum space).
  - Near them, ripples move at speed 1.448 across the line and not at all along it (A38 D4). "Run along" suggests the opposite.
  - The bullet has no grade.
- **Replacement text** for line 355:
  > - **What its ripples do (checked).** With the simple rule, the ripples that cost nothing are the waves whose wave patterns lie on certain lines, lined up with the cube's long diagonals. Ripples near them move at a fixed speed across those lines but not along them, so these are not light-like cones.

### C128 — MINOR: the records bullet omits the −m subfamily and states readability as absolute

- **Where.** Draft line 357.
- **Quote.** "**Records.** Records holding the background's own local direction keep it calm; other contents disturb it. A single record shows which of the 8 layouts is the real one, which is expected for a pattern held in the state."
- **What is wrong.**
  - "Other contents disturb it" holds under the pair rule. A38 D7 found an 8-dimensional star subfamily that stays calm next to −m records. Record clusters were untested.
  - D8 says one record fixes the translate "relative to any other placed structure". On a uniform grid, "the real one" has no absolute meaning.
- **Replacement text** for line 357:
  > - **Records.** Under the simple rule, records holding the background's own local direction keep it calm and every other content disturbs it (checked). With richer rules, records holding the opposite direction can keep it calm too (checked; clusters of records untested). A single record fixes which of the 8 layouts is in place relative to anything else placed on the grid, which is expected for a pattern held in the state.

### C129 — MINOR: the class's 2×2×2 scope is unstated, and "what stays open" is out of date

- **Where.** Draft lines 352 and 358.
- **Quotes.**
  - Line 352: "If the pattern must look the same after any turn of the grid, apart from a shift, the 8 spots of each small cube must point to the cube's 8 corners."
  - Line 358: "Backgrounds whose spots share their possibilities instead of each pointing one way (decision 23), groups of ripples rather than single ones, and A39's question: whether quiet empty space can carry light at all."
- **What is wrong.**
  - D1 is EXACT only for period-2 product textures. A larger repeat is not covered: orbit counting would allow half-turn-fixed sites there (ARGUED).
  - The relaxed-turn search was not run (A38 open edge 1).
  - Line 358 still lists A39's question as open, though section 13 now answers it conditionally.
  - It omits H8 with F6 (A38 open edge 6) and fragility.
- **Replacement text.**
  - Line 352:
    > - **Only one such background exists (exact).** If the pattern repeats every 2×2×2 block of spots and must look the same after any turn of the grid, apart from a shift, the 8 spots of each small cube must point to the cube's 8 corners. My check confirmed every turn maps it onto a shifted copy of itself.
  - Line 358:
    > - **What stays open.** Backgrounds whose spots share their possibilities instead of each pointing one way (decision 23; section 13 applies to them), patterns with a larger repeat or that respect only some turns (not searched), how this background would sit with the field's 1-of-8 jobs (decision 13), groups of ripples rather than single ones, and how fragile this background is (section 13).

### C130 — MINOR: section 12 drops A38's owner decisions

- **Where.** Section 12. Insert after line 358.
- **What is wrong.**
  - A38 lists four owner decisions: in-star terms; whether tuned coefficients count as pattern-free; records holding only the background's direction; and H8 next to F6.
  - Section 12 has no decision line, while section 13 has one.
  - Under owner rule (d), choices should be framed as the owner's.
- **Replacement text** (new bullet after line 358):
  > - **Decisions for you (A38).** May the rule carry three-spot or farther-reaching terms (decision 22)? Do finely set strengths count as "no pattern painted on"? May records hold only the background's own direction? Is a 1-of-8 background in which all places are alike acceptable next to the field's 1-of-8 jobs (decision 13)? And is an empty background that is not the calmest state acceptable (section 13)?

### C131 — MINOR: provenance labels and review counts

- **Where.** Draft lines 349, 360, 1 and 51; summary line 10.
- **Quotes.**
  - "(A38; checked by me, not hostile-reviewed)"
  - "(A39; checked by me, not hostile-reviewed)"
  - "(v11, after seven review rounds)"
  - "Seven rounds of hostile review by four separate agents attacked the main claims (the second reviewed twice and the fourth three times; each later round had read the earlier ones), and their corrections are included."
  - Summary: "Seven rounds of hostile review, by four separate agents, attacked the claims, and their corrections are folded in."
- **What is wrong.** After this round, both late sections have had one hostile review, and the count is eight rounds, with the fourth agent reviewing four times. This round covered only the late lanes.
- **Replacement text.**
  - Line 349: `### 12. Late result: patterned calm backgrounds (A38; checked by me and by one hostile review round)`
  - Line 360: `### 13. Late result: can quiet empty space carry light? (A39; checked by me and by one hostile review round)`
  - Line 1: replace "(v11, after seven review rounds)" with "(after eight review rounds)". The version number is the coordinator's.
  - Line 51:
    > Eight rounds of hostile review by four separate agents attacked the main claims (the second reviewed twice and the fourth four times; each later round had read the earlier ones; the eighth covered only the late sections 12 and 13), and their corrections are included.
  - Summary line 10:
    > Eight rounds of hostile review, by four separate agents, attacked the claims, and their corrections are folded in.

### C132 — OPTIONAL (outside the requested scope): one clause each for the bottom line and decisions 23–24

- **Where.** Draft line 22 (bottom line) and decisions 23 and 24 (lines 418–419 of the 441-line draft).
- **What is wrong.** These lines still read as they did before A38 and A39, and each result bears directly on them.
- **Replacement text** (append only):
  - **Line 22.**
    - After "...but next to matter it gets recorded and heats (A28)", add: "; and if records can sense its energy, it cannot be exactly quiet (A39)".
    - After "...(not built; whether it would then move like light is a further open question)", add: "; its background cannot be one whose spots each simply point one way (A38)".
  - **Decision 23.** Append: "A39: with the plain rule, if records can sense its energy it cannot be exactly quiet; section 13 lists the ways out."
  - **Decision 24.** Append: "A38: if each spot simply points one way, the only turn-respecting 8-fold pattern has no half-turn holding a spot fixed, so this route needs spots that share their possibilities, or more room per place."

### C133 — MINOR (lane reports and LOG; not doc text)

These are for the coordinator's record wherever lane text is quoted.

- **A38 report §2 item 3 and LOG 05:36, D5: "under EVERY glued covariant law".** Add "on nearest-neighbour faces, whenever nearest-neighbour hops are nonzero; loops through longer hops are not covered".
- **A38 D6 and LOG: "Narrows A31 D4".** Add "(CHECKED; the isotropic point has 2 + 2 linear modes plus 4 heavy ones, and H8 is not the ground state there)".
- **LOG 05:36, D7: "others do not".** Add "under the pair law; an 8-dimensional star subfamily also keeps −m records calm".
- **LOG 05:36.** Add "H8 is not the ground state of its calm pair law, for either sign, nor at any zero-cost linear touching (A34 c11; A39 positivity lemma)".
- **A39 §3.3(a) item 5, its plain-language summary and LOG table row (a): "needs a painted sign pattern / painted signs".** Change to "in A39's toy; A38's H8 is a state-pattern example".
- **LOG table row (a): "return probability 0.72 vs 1.0000 for a ground-state vacuum".** Change to "vs 1.0000 for a gapped ground-state vacuum; the same vacuum made the ground state without a gap returns 0.04 at δ = 0.10, its loss into one zero-cost flip (A34 c12)".
- **A39 §3.3(e) cost 3 and LOG table row (e): "matter number exactly conserved".** Change to "no term may create matter from matter-empty space (matter number may still change where matter already is)". A term such as g·n_m(r)(a†_{r′} + a_{r′}) and its adjoint both vanish on |0_m⟩, so Ω stays exactly quiet.
- **LOG table row (f).** Add "needs the ground state".

## Fine as written (checked; no change needed)

- **Line 351.** The question is framed fairly.
- **Line 352.** The main claim is correct; only the scope clause is added (C129).
- **Line 354.** The core claim (a third of a turn, sign alternating, my check on every face) is EXACT and correctly graded. Only the scope and the route sentence change (C118).
- **Line 362.** The step "Then empty space must be the rule's calmest state" is Lemma V, EXACT and correctly placed. It is kept in C119's replacement.
- **Line 367.** "What does not help." Fine as a heading.
- **Line 369.** The first sentence ("moves the problem to matter's edges") is correct.
- **Line 370.** The decision framing ("for you", "if any") is correct.
- **Owner rules, across sections 12–13 and summary line 48:**
  - no possibility is said to be "read" and no "question is asked";
  - no beat or heartbeat appears;
  - Q7 is untouched;
  - memory and two kinds of places are presented as costs and decisions, not adoptions.
  - The only convention slips are the two unlabelled comparisons (C122, C123).

## Owner decisions raised or sharpened by this round (all yours)

1. Is an empty background that is not the calmest state acceptable at all? It is the only way A38's light-like point arises (C116, C120).
2. If the 8-fold route is pursued, may its background have spots that share their possibilities, or more room per place? A pointing background cannot carry it (C117).
3. A38's four decisions (C130).
4. Under "light invisible to records": may matter multiply only where matter already is? A39's argument needs only that, not exact conservation (C133).
