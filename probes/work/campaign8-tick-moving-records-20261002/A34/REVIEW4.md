# A34 hostile review, round 8 (REVIEW4): A38, A39, A40 and the doc's late text

**Scope.** This round covers:
- A38: D1, D2, D5 (the half-turn argument and its scope), D6, the D4 narrowing and D7.
- A39: Theorem T, Lemma V, the twist and positivity lemmas, the grading of "frustration-free ⇒ z ≥ 2", the escapes (especially (e)) and c1's fragility numbers.
- A40, added mid-round: the S1 verdict's grading, "factor-wise Record", payload exactness, T1/T3 (generalized Theorem S), T5's gauge argument on a torus versus Z³, T8 (the mass pattern) and the quantum-link photon comparator.
- MORNING_DRAFT.md: sections 12 and 13 (lines 349–370, version of 05:52), section 14 (lines 372–390, added 06:20), and the A38 sentence at the end of line 331. Lines 1–370 are unchanged between the two versions, so line numbers hold.
- MORNING_SUMMARY_DRAFT.md (05:52): the A38/A39 sentences in line 48. As of 06:20 it has no A40 text.

**Sources.** I worked only from primary files:
- A38: REPORT.md, A38_PROMPT.md and toys/verify_A38.py.
- A39: REPORT.md, A39_PROMPT.md, the code and output of c1–c3, and toys/verify_A39_edge.py.
- A40: REPORT.md, A40_PROMPT.md, the code and output of k1–k4, and toys/verify_A40_flux.py.
- Also BRIEF.md (the axioms verbatim) and A25 REPORT.md §3.3 and §6, for the role label.
- LOG.md lines 1727–1900.

**Rules followed.** I ran no git, made no repo edits and did not touch any other agent's files or the draft. All scripts are in `SP/c8/A34/`.

**Counts.**
- A38/A39: 6 MAJOR (C116–C121), 10 MINOR on doc text (C122–C131), 1 OPTIONAL outside the requested scope (C132), and 1 MINOR on lane and LOG wording (C133).
- A40: 5 MAJOR (C134–C138), 5 MINOR on doc text (C139–C143), and 1 MINOR on lane and LOG wording (C144).
- In all: 11 MAJOR, 15 MINOR on doc text, 1 OPTIONAL and 2 lane/LOG.

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

### A40: most pieces hold as graded; the verdict and the doc's section 14 overstate it

- **K1 (EXACT): holds.**
  - Turns about a V place have orbits {V}, {E}, {F} and {C} on the 8 classes, so a kinds pattern that moves with the layout is a role function.
  - A kinds pattern on a different translate would be a second 1-of-8 label, and the combined pattern would not map to a translate of itself under the turns. So "the same choice" is forced, not merely convenient.
- **G1 (EXACT; checked on A25's builder): holds.** It says where gravity's content acts (V and F). It does not say where extra room is needed (C136).
- **3.4 and k3 (EXACT within 270 combinations): hold.** The criterion doing the work is that charged matter and the lapse share one star (a place and its six neighbours). The doc should state it (C140).
- **The S1 verdict (ARGUED overall): overstated.** "Coherent" has not been shown. Three load-bearing pieces are open, and one of them is excluded in its simplest form: the charged hop (C134), light's fast phase on this grid (COMPARATOR), and matter's empty space (C135). See C138.
- **"Factor-wise Record": a change to the axiom's text, not a reading.**
  - Once a place's domain is a product of factors, "locks exactly one admissible local possibility" means a one-dimensional projector of the whole place, which would also lock gravity's factors.
  - Restricting it to the matter factor changes what "local possibility" means. That needs the owner's exact text, as decision 7 already says for permanence (C139).
- **Payload.**
  - "No finite domain holds A25's field" (tr[h, π] = 0 ≠ i·dim) is EXACT, given A25's canonical pairs.
  - "≥ 2 qubits for a glued charge" is EXACT. The constraint is in fact stronger: a charged hop through a glued link is covariant only if the matter states carry a vector index, so a one-component charge cannot hop at all (EXACT; c13).
  - "E and C keep one qubit" contradicts A25's own covariance construction, in which every place carries its 8-valued role label in its content (A25 S9.2; A40 §3.6 says so itself). See C136.
  - Light's one qubit per link is correctly graded COMPARATOR. The lapse pair is correctly graded ARGUED.
  - The weight W1 = N̂ ⊗ F_m needs N̂ ≥ 0, which a linearized lapse 1 + δN does not satisfy. A positive function of the lapse must be supplied (C144).
- **T1/T3, generalized Theorem S (EXACT): hold, for matter with one internal state per place** (kept real signs, or A33's parities). They do not cover matter with internal components. For neutral vector matter, the covariant hop i S^a already gives same-speed-in-every-direction touchings at k = 0, with no flux and no pattern, plus a flat middle band (EXACT; c13).
- **T5.**
  - **The classical part is EXACT.** On Z³, two link configurations with equal flux through every square differ by a gauge change. On the 4³ torus, the flux through every square leaves the holonomies around the torus's cycles undetermined. k4's explicit gauge functions settle those as well; the coordinator's square-only check (verify_A40_flux.py) would not do so on its own, though the conclusion stands because of k4.
  - **Both checks concern a classical link pattern, not light's quantum ground state.**
  - **The physical inference fails in its simplest form.** A light link's raising operator picks up a phase −i under a quarter turn about the link's own axis (EXACT; c13). So no hop of one-component charged matter through a link is covariant: there are 0 covariant parameters, and A40's example of a charge on the singlet is one such case.
  - Covariant charged hops exist only when the matter states carry a vector index. For a triplet charge over a singlet empty state, they form a family with 2 real parameters, made of helicity-changing matrices.
  - So "the single-particle problem is KS on the coarse lattice" (T5, T7) does not describe glued charged matter. What matter feels around a square is light's flux combined with a matrix holonomy, and that has not been analysed (my c14 scan was inconclusive).
- **T6 (COMPARATOR).**
  - A uniform coefficient on light's square term is covariant under every turn (EXACT; c13, an explicit 4-qubit check), so "one uniform sign, not a pattern" holds at the level of symmetry.
  - That the sign selects a π-flux fast-light phase comes from pyrochlore spin ice (six-sided rings on the diamond lattice) and is transferred to cubic squares. A40 flags this transfer for L2 but not at T6.
- **T8 (EXACT for one-component matter): holds as arithmetic.** A one-place staggered mass on the coarse lattice has period 4, giving a further 1-of-2 label.
  - It is moot for glued charged matter, which cannot be one-component (C134).
  - No mass removes the negative-energy branch over an empty matter vacuum (C135).
  - A mass generated by the dynamics would be a state-level 1-of-2 choice, not necessarily a supplied one (ARGUED).
- **T9 (ARGUED in A40; EXACT for single particles via A39's positivity lemma).** It is left out of A40's verdict costs and out of section 14 (C135).
- **Records never adjacent (EXACT).** The consequences for I2, A28 and Q7 are only partly in the doc (C137).

## What I ran

All runs used `nice -n 10` with the four thread caps at 1. The 1-minute load was 2.23–5.64 at run time, always under 6.

| Script | Toy | Result | Time, memory |
|---|---|---|---|
| `c11_h8_not_ground.py` | One-flip block over H8 on a 4³ torus, calm pair law J(σ·σ + σ^aσ^a), J = ±1 | Double-flip amplitude 2.0e-16 (calm). One-flip energies relative to H8 run from −8.0000 to +8.0000; 27 of 64 lie below zero; the spectrum is symmetric about 0. Identical for J = +1 and J = −1. | 0.20 s, 28 MB |
| `c12_fragility_control.py` | A39 c1's toy, rebuilt in my own code: 4×3 π-flux torus, 12 qubits, the same slow on-off cycle of δΣX (period 400, dt = 0.5) | See the table below | 3.6–6.2 s per run, ≤ 96 MB |
| `c13_glued_link_hops.py` | Glued action on A40's light links (E = σ^a, U = (σ^b + iσ^c)/2) and on matter hops through them, for all 24 turns | See the list below | 0.18 s, 64 MB |
| `c14_vector_matter_bands.py` | Bands of c13's covariant charged vector hops in classical zero-flux and π-flux link backgrounds, on a 20³ grid | Exploratory and inconclusive: band gaps and \|E\| reach about 1e-6 to 1e-3 on the grid, and the π-flux spectrum is symmetric about 0. Not used for any claim. | 3.0 s, 64 MB |

c13 results:
1. **Link phase.** A z-link's raising operator picks up −i under a quarter turn about its own axis. Over all 24 turns and 3 directions the phases are ±1 and ±i.
2. **Square term.** Light's square term U U U† U†, pushed forward by each of the 24 turns in each of the 3 planes, equals the image square's own term or its conjugate (maximum deviation 3.3e-16). So a uniform coefficient respects every turn.
3. **Charged hops through a link that respect all 24 turns.** One-component (turn-scalar) matter: 0 real parameters. Triplet matter over a singlet empty state: 2 real parameters.
4. **Neutral vector matter without links.** Covariant hops have 3 real parameters, and i S^a is among them (residual 1.3e-15). Its slopes at k = 0 are −2, 0 and +2 in all 200 directions tested.

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
    > Eight rounds of hostile review by four separate agents attacked the main claims (the second reviewed twice and the fourth four times; each later round had read the earlier ones; the eighth covered only the late sections 12 to 14), and their corrections are included.
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

### C134 — MAJOR (section 14): "the twist comes free (exact core)" assumes a charged hop that cannot respect the turns

- **Where.** Draft line 382.
- **Quote.** "**The twist comes free (exact core; my check).** Matter hopping from corner to corner passes through light's links. If light's own calm state carries a half-turn twist around every square, which needs only one uniform sign in light's rule, not a pattern, then matter feels exactly the twist it needs for light-like motion. That calm state looks the same after every turn of the grid; my check confirmed this on all 192 squares for all 24 turns. Whether light really settles into that state on this grid is a comparison with known magnet models, not shown here."
- **What is wrong.**
  - **The simple charged hop is not covariant.** "Matter feels exactly the twist it needs" assumes the simple one-component hop ψ†_V U ψ_V′ (KS on the coarse lattice: A40 T5, T7). Under the glued action, a link's raising operator picks up −i under a quarter turn about the link's own axis. No one-component charge can compensate for that phase, so no such hop is covariant (EXACT; c13: 0 parameters).
  - **Covariant charged hops need a vector index.** They exist only when matter states carry a vector index (for example a triplet charge over a singlet empty state; 2 real parameters), with matrices that rotate the internal state as it hops. Matter then feels light's flux combined with a matrix holonomy, which nobody has analysed. A40 lists the charged hop as open edge 2; its simplest form is now excluded.
  - **"My check confirmed this" concerns a classical link pattern.** The check covers the flux through every square of a classical link pattern after each turn, not light's quantum ground state. A40 T6's "one uniform sign" is fine at the level of symmetry: c13 confirms that a uniform square-term coefficient respects every turn.
  - **T1/T3 are scoped to one-component matter.** Matter with internal components can get a covariant twisting hop from the rule itself, giving same-speed motion in every direction with no pattern (EXACT; c13), so light's twist is not the only option.
  - **The comparison was made on a different grid.** It comes from spin ice on the pyrochlore lattice (six-sided rings), not cubic squares.
- **Corrected wording.**
  - Light's uniform π pattern respects every turn up to gauge (EXACT, classical), and its square-term sign respects the turns (EXACT).
  - Matter cannot hop through a glued link with one internal state (EXACT); with a vector index it can, and what its ripples do is open.
  - Light's settling into the π phase on this grid is COMPARATOR, from another grid.
- **Replacement text** for line 382:
  > - **The twist from light: promising, not shown (symmetry facts exact; the rest open).** Matter hopping from corner to corner passes through light's links. A half-turn twist in light's links around every square needs only one uniform sign in light's rule, not a pattern, and that twisted pattern of links looks the same after every turn of the grid, up to a relabelling that changes nothing physical (exact; my check on all 192 squares for all 24 turns, and the review confirmed that one uniform sign on light's square term respects every turn). But a charged hop through a link respects the turns only if matter at each corner has internal parts that turn with the grid: matter with a single internal state cannot hop through light's links at all (exact; fourth review's check). So this matter is not the simple one-part kind for which light's twist gives exactly light-like motion, and what its ripples do has not been worked out. Matter with internal parts can also get a twist from the rule itself, with no pattern (shown for uncharged matter, with a heavy partner beside the light-like ripples; fourth review's check), so light's twist is one option, not the only one. Whether light really settles into the twisted state on this grid is a comparison with magnet models on a different grid, not shown here.

### C135 — MAJOR (section 14): matter's empty space is left out; light-like matter over a never-recording empty space has negative energies

- **Where.** Section 14's price list (lines 383–389). Nothing there covers it.
- **Quote (A40 §3.8 T9, ARGUED).** "Over an empty, quiet matter vacuum, the lower Dirac branch is made of real one-particle states with no sea. A39's loopholes (a) and (a′) still bear on matter."
  - It is absent from A40's verdict costs (§2 item 9; §3.9) and from section 14.
- **What is wrong.**
  - S1 relies on A39's escape (e), which needs a quiet, empty matter vacuum.
  - Any zero-cost linear touching for single matter particles forces negative energies (A39's positivity lemma; EXACT). So the empty matter vacuum is then not the lowest state: section 13's third way out, now for matter, with its costs.
  - A mass does not help: the lower branch −√(m² + v²p²) stays negative.
  - Lifting every state above zero puts the light-like point at a finite energy with slower states below it (A39's (a′)).
  - Filling the negative states (a sea) breaks quietness (A39 cost 4; A9; the doc's decision 4).
  - This is the main physics price of S1's matter, and the doc omits it.
- **Corrected wording.** Light-like single-particle matter over S1's quiet empty matter vacuum makes that vacuum not the lowest state (EXACT, single particles). The alternatives are a finite-energy touching or a filled sea, which is not quiet.
- **Replacement text** (new price bullet after line 388):
  >   - Light-like matter over empty space that never records has states of negative energy, so its empty space is then not its calmest state: section 13's third way out, now for matter (exact for single particles; A39). A simple mass does not change this. Lifting all of matter's states above zero leaves slower matter states below the light-like point; filling the negative states, as real physics does with its sea, would make empty space record.

### C136 — MAJOR (section 14): the payload is understated; every place holds more than one qubit's worth

- **Where.** Draft line 384 (and line 375's "needs only half the places").
- **Quotes.**
  - Line 384: "Places hold more than one qubit's worth: corner and face places for gravity's parts, and corners need at least two qubits for charged matter."
  - Line 375: "**Gravity needs only half the places (exact).**"
- **What is wrong.**
  - A25 makes its layout covariant by putting "role labels in the site content" (A25 S9.2; open edge 1: "a role label of 8 values"). A40's own payload table lists "an 8-valued role label" for all places.
  - With the pattern held in the state and a law that treats all places alike, each place has to carry its job in its content. So E and C places hold more than one qubit as well.
  - The alternative, places built differently by job, distinguishes sites by something other than "the supplied lattice structure alone" (Lattice axiom).
  - If no place is privileged, every place must also have the same domain, which means every place carries the union of all jobs' content. A40 says so (§3.6, ARGUED), but its verdict ("E and C keep one qubit") and section 14 do not.
  - G1 (EXACT) says where gravity's content acts, not where room is needed.
- **Corrected wording.** Gravity's content acts on half the places (EXACT). Every place holds more than one qubit's worth: at least its 8-valued job label, and the union of all jobs if every place must have the same room (ARGUED).
- **Replacement text.**
  - Line 384:
    >   - Every place holds more than one qubit's worth (argued). Each carries its 8-way job label, as in gravity's own construction; corner and face places also carry gravity's parts, and corners need at least two qubits for charged matter. If every place must have the same room (no place privileged), every place carries all of it.
  - Line 375, first words: replace "**Gravity needs only half the places (exact).**" with "**Gravity's content sits on only half the places (exact).**" Keep the rest.

### C137 — MAJOR (section 14): never-adjacent matter places conflict with your I2, empty Q7's recorded-neighbour clause for matter, and need a two-site rule

- **Where.** Draft line 386.
- **Quote.** "Matter places are never next-door neighbours, so records step two places at a time, and "records form only next to records" would have to look two places away."
- **What is wrong.**
  - **I2.** Your instinct I2 says a record moves at most one grid space per tick. In S1 a record can only move between matter places two spaces apart, since nothing between them ever records (EXACT). The doc does not say that this departs from I2.
  - **Q7.** Q7 stands: "The menu ... is set by the conditions, including recorded neighbours." The Admissibility axiom is a nearest-neighbour rule. In S1 a matter place's nearest neighbours are light places, which never record. So under a nearest-neighbour rule, no matter place's odds can depend directly on another matter place's record (other records reach it only indirectly, through the change of the shared possibilities), and Q7's recorded-neighbour clause never applies to matter (EXACT).
  - **The cost of keeping it.** Keeping that clause meaningful means a rule that reaches two places, which changes the axiom's "nearest-neighbor" wording. A40 notes the reach-2 point (§3.7) but frames it as working "only at reach 2", without saying that this changes the axiom.
  - **Fairness.** Under the owner rules, the doc must show where a layout departs from the owner's picture.
- **Corrected wording.** The records' step is two places (EXACT), which departs from I2 unless I2 is counted on the coarse grid of matter places. Under a nearest-neighbour rule, Q7's recorded-neighbour clause is vacuous for matter (EXACT), so keeping it needs a rule reaching two places (an axiom-wording change). A28's gate likewise has to look two places away (EXACT).
- **Replacement text** for line 386:
  >   - Matter places are never next-door neighbours, and nothing between them ever records (exact). So records step two places at a time, which departs from your instinct that a record moves at most one grid space per tick (I2) unless that is counted on the coarser grid of matter places. "Records form only next to records" would have to look two places away. And a rule that looks only at next-door neighbours could never let a matter place's odds depend directly on another matter place's record (only indirectly, through how the shared possibilities change), so your Q7 clause "including recorded neighbours" would reach matter only if the rule looks two places away, which changes the nearest-neighbour wording of the rule's axiom.

### C138 — MAJOR (section 14): the opening says everything "fits"; coherence is not shown

- **Where.** Draft line 373.
- **Quote.** "Possibly yes: the same 8-way pattern gravity already needs can sort places into kinds so that light, gravity and records-bearing matter all fit. It works only if matter shares places with part of gravity, so it is not a clean three-way split (argued overall; the pieces are exact or checked as marked)."
- **What is wrong.**
  - "All fit" and "it works" overstate A40's ARGUED verdict, which itself overstates ("coherent single supplied choice").
  - Three load-bearing pieces are open:
    - the charged hop, which in its simplest form is excluded (C134);
    - light's fast twisted phase on this grid, which is COMPARATOR;
    - matter's empty space (C135).
  - The pattern is also not a single choice once a one-place mass is wanted (T8: a further 1-of-2 label).
- **Corrected wording.** A candidate layout with no contradiction found among the pieces checked (ARGUED). It is not shown to be coherent, and several pieces remain open.
- **Replacement text** for line 373:
  > Possibly, but not shown: the same 8-way pattern gravity already needs can sort places into kinds that light, gravity and records-bearing matter could share, with no contradiction found so far. It needs matter to share places with part of gravity, so it is not a clean three-way split, and three load-bearing pieces are open: how charged matter hops through light's links, whether light settles into the needed state on this grid, and matter's empty space (argued overall; the pieces are exact or checked as marked).

### C139 — MINOR (section 14): "factor-wise Record" changes the axiom's text and is not a reading

- **Where.** Draft line 385.
- **Quote.** "Record must be read as locking one place's matter share only, which is a wording choice for you."
- **What is wrong.**
  - "Read as" suggests a non-governing reading note.
  - With a multi-factor place, "locks exactly one admissible local possibility" (Record, verbatim) would lock the whole place, gravity included. Restricting it to the matter factor changes the axiom's text.
  - It also presupposes the Qubit change, since the axiom gives each site the domain M₂(C).
  - The doc already treats such changes as needing the owner's exact text (decision 7).
- **Replacement text** for line 385:
  >   - Record's wording would change: a record would lock one possibility of a place's matter share only, not of the whole place. That changes the Record axiom's text and needs your exact wording (as in decision 7); it presupposes the change to more room per place.

### C140 — MINOR (section 14): the clean-split no-go needs its coupling-reach condition

- **Where.** Draft line 376.
- **Quote.** "No arrangement that keeps every kind on its own places lets charged matter feel gravity's slowing of time."
- **What is wrong.** k3's criterion is that matter and the lapse share one star. With longer-reaching coupling terms the enumeration does not apply.
- **Replacement text** for line 376:
  > - **A clean split fails (exact, within 270 arrangements tried).** No arrangement that keeps every kind on its own places lets charged matter feel gravity's slowing of time through rule terms that stay within one place and its six neighbours.

### C141 — MINOR (section 14): the bundle list is incomplete, and decision 17's entry overstates

- **Where.** Draft line 390.
- **Quote.** "It bundles several of your decisions into one picture: 13 (room per place), 17 (matter's twist, now from light rather than painted), 21 (gravity's places never record, now share by share), 22 (rules on small groups), 24, and A39's "light invisible to records"."
- **What is wrong.**
  - A40 §3.9 also lists decisions 4, 8, 27, 16, 20 and I5.
  - The Qubit and Record axiom texts change, and so does Admissibility's nearest-neighbour wording if Q7's clause is to reach matter (C137).
  - "Now from light" is not shown (C134).
- **Replacement text** for line 390:
  > - **Why it matters.** It bundles several of your decisions into one picture: 13 (room per place, now at every place), 17 (matter's twist, possibly from light rather than painted; not yet shown for charged matter), 21 (gravity's places never record, now share by share), 22 (rules on small groups), 24, and A39's "light invisible to records". It also touches 4 (the next-to-records rule), 8 and 27 (how records step), 16, 20, your instincts I2 and I5, Q7's recorded neighbours, and the wording of the Qubit, Record and nearest-neighbour axioms.

### C142 — MINOR (section 14): records at corner places must lock charge-definite possibilities

- **Where.** Draft line 378.
- **Quote.** "**Corner places:** matter, together with gravity's stretch parts and its time-slowing. Records lock only matter's share of each such place."
- **What is wrong.**
  - Light's links carry Gauss's law at the corners: the charge at a corner equals the flux of light out of it.
  - A record's cut with a projector that does not commute with the corner's charge creates a mix of charges, while the links stay unchanged, so Gauss's law fails at that place (EXACT).
  - So the menu at corner places must consist of charge-definite possibilities. This is a constraint on the menus, and A40 does not state it.
- **Replacement text** for line 378:
  >   - **Corner places:** matter, together with gravity's stretch parts and its time-slowing. Records lock only matter's share of each such place, and only possibilities with a definite charge; otherwise light's bookkeeping (Gauss's law) breaks at that place (exact; fourth review).

### C143 — MINOR: section 14's label, and no A40 item in the summary

- **Where.** Draft line 372; MORNING_SUMMARY_DRAFT.md line 48, which has no A40 sentence as of 06:20.
- **Replacement text.**
  - Line 372: `### 14. Late result: one pattern of kinds of places for everything? (A40; checked by me and by one hostile review round)`
  - Optional summary sentence, appended to line 48:
    > A synthesis lane (A40) found that the same 8-way pattern gravity needs could sort places into kinds for light, gravity and matter, but only with matter sharing places with part of gravity, more room at every place, a change to the Record axiom's wording, records stepping two places at a time, and open questions about how charged matter hops through light's links and about matter's empty space.

### C144 — MINOR (A40 report and LOG; not doc text)

- **§2 item 5 and M2 example: "a charge projector onto the singlet".** With the singlet charged, the empty state is a triplet, which is degenerate and singles out a direction. Either way the hop needs a vector index (c13). Suggest the charged triplet over an empty singlet. Open edge 2 ("glued gauge-covariant hop for a two-qubit turn-scalar charge") is answered: none exists for a one-component charge, and a 2-parameter family exists for a triplet.
- **T5 "(EXACT; CHECKED k4)".** Add "for classical link patterns; on a torus, equal square fluxes do not by themselves fix the holonomies around the cycles; k4's explicit gauges do".
- **LOG 06:20, "T5's core ... CONFIRMED".** Add "(square fluxes of the classical pattern; gauge equivalence on the torus rests on k4)".
- **T6.** Add "from pyrochlore spin ice (six-sided rings on the diamond lattice), not verified for cubic squares".
- **T7 "The single-particle problem is KS on the coarse lattice".** Add "for one-component hops, which glued charged matter cannot have (A34 c13)".
- **§3.7 W1 = N̂_V ⊗ F_matter "(EXACT)".** Add "needs N̂ ≥ 0; a linearized lapse 1 + δN is not, so a positive function of the lapse is supplied".
- **§2 item 9 and §3.9 costs.** Add "matter's quiet empty vacuum is not its lowest state if matter is light-like (T9; A39)" and "the 8-valued role label at every place". Replace "a factor-wise reading of Record" with "a change to the Record axiom's text".
- **§3.9, "E and C keep one qubit".** This is true only if places are built differently by job. Under the state-level label (A25 S9.2) every place carries more (C136).

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
- **Section 14.**
  - **Line 374 ("No new pattern", exact).** Correct (K1). The combined pattern's covariance forces the same translate.
  - **Lines 377, 379, 380 and 381 (the S1 layout).** Accurate to A40.
  - **Line 387 ("Matter must never appear out of empty space").** The accurate rendering (see C133 on A39's stronger wording).
  - **Line 388 (mass).** Correct for one-component matter (T8); C135 adds that a mass does not remove the negative branch.
  - **Line 389 (no fully recorded region; "your black-hole picture changes").** EXACT in S1 and fair to I5.
  - **The last sentence of line 382** ("a comparison with known magnet models, not shown here") is honest. C134 keeps it and names the different grid.
  - **Owner rules.** No possibility is "read", no beat is adopted, and choices are framed as yours. The exceptions are the two items C137 and C139 make explicit: Q7's clause and the Record wording.

## Owner decisions raised or sharpened by this round (all yours)

1. Is an empty background that is not the calmest state acceptable at all? It is the only way A38's light-like point arises (C116, C120). For S1 it applies to matter too (C135).
2. If the 8-fold route is pursued, may its background have spots that share their possibilities, or more room per place? A pointing background cannot carry it (C117).
3. A38's four decisions (C130).
4. Under "light invisible to records": may matter multiply only where matter already is? A39's argument needs only that, not exact conservation (C133).
5. S1's decisions:
   - Would you change Record's text to lock one possibility of a place's matter share (C139)?
   - Would you accept records stepping two places, against I2 (C137)?
   - Would you widen the rule's reach to two places so that Q7's recorded-neighbour clause reaches matter (C137)?
   - Would you accept every place carrying its job label (C136)?
   - Would you accept matter whose charged states have internal parts that turn with the grid, the only kind that can hop through light's links (C134)?
