lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-17T04:34Z

# New attack vectors from the measured-physics assumptions file (FINISH row 1065)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session, pinned at commit 50e1952db. Research-stage working state. This file grants no status. No part of it is checked by another model.

Item: queue row 1065, `gap-measured-vectors-max`. Inputs read first: `library/gap-measured-assumptions-opus.md` (row 1063), then `library/prior/gap-measured-read-luna.md` (row 1064). Read only to avoid redoing work: `parts/gap.md`, `library/gap-wall-vectors-max.md` (row 1053) and its two checks.

Marks used: PROVED, ARGUED, OPEN, FAILS. A measured result may guide or refute. It never proves.

## Plan (eight steps, one step per response, each appended before the next)

1. Read row 1063's file in full. Record its top fifteen assumptions and each place where the measured mechanism disagrees with the lane's route.
2. Read row 1064's file in full. Record what it adds or contests.
3. Read `parts/gap.md`, row 1053 and its checks, only to list what is already on file (vectors, kill tests, open-core entries). Write the no-duplicate grep results.
4. Task (1): for each top-fifteen assumption and each disagreement, say whether it gives a new attack vector.
5. Tasks (2) and (3): for each vector, the exact statement, consumer, change, source and cheapest kill test; then run the kill tests on file.
6. Task (4): rank the survivors by change divided by cost.
7. Task (5): for the top one or two, invent the mechanism, write the first lemma and try it by hand, or build the counterexample.
8. Task (6): one complete brief per surviving vector, then the RESULT line.

## Step log

(Each step below is appended when it is done. Nothing is written here ahead of the work.)

## Step 1: row 1063's file, read in full (736 lines)

Source: `library/gap-measured-assumptions-opus.md` (Claude Opus 5.5 high, unchecked). Credit for every item of this step: that file and the sources it names (Athenodorou and Teper 2106.00364; Engels, Fingberg, Weber; Fingberg, Heller, Karsch; Lautrup and Nauenberg; Creutz; Bhanot and Creutz; Mathur and Gavai; Datta and Gavai; Lucini, Teper, Wenger; Luscher and Weisz; Bali and others; Kovacs and Tomboulis; de Forcrand and D'Elia).

**1.1 The ranking that exists.** Row 1063 does not rank fifteen assumptions. It ranks five bundles (its L389-401), which hold nine assumption IDs. It then names one lower-rank item (a10) and three "most expensive to be wrong" (e4, e5, e6), and its Elon pass lists the method-only requirements that can be deleted at a price. Row 1065 was queued before row 1063 ended, so "top fifteen" is filled here by this stated rule: the nine ranked IDs in rank order, then the Elon-pass deletable items not yet listed, then the expensive ones. This rule is mine.

| Rank | ID | Assumption (row 1063 wording, shortened) | What the measured record says (row 1063) |
|---|---|---|---|
| 1 | c2 | The band is the order-one bare coupling of the Wilson action | Gap scale meets the cutoff at beta 2.2-2.4 (L2, L5). The band [2.3, 2.6] is above the crossover (peak at 2.1-2.2, T-BAND guide run) and already scales |
| 2 | b3 | The Wilson plaquette action | Habit. Universality (BELIEF e6) says other actions give the same continuum |
| 3 | c4 | Strong-coupling tools reach the band | Contradicted as a guide: leading strong coupling misses sigma a^2 by 5.4x and m a by 2.4x at beta 2.30 (L9) |
| 4 | e4 | No bulk transition on the SU(2) Wilson axis at T = 0 | Strongly supported, not a theorem |
| 5 | c6 | A finite-volume criterion with small boxes at band couplings | Boxes of side below 1/(T_c a) are deconfined: side 4 at beta 2.3, 8 at 2.5, 11 at 2.6, 14 at 2.7 (L3, C8) |
| 6 | c10 | Small-lattice numerics guide the lane | Same contradiction (C8) |
| 7 | b6 | Periodic torus, then thermodynamic limit | Same contradiction at small sizes (C8) |
| 8 | d2 | Deconfined models are counterexamples to gap tools | Contradicted (recalled): spatial screening masses persist when the flux tube melts |
| 9 | e10 | The gap is caused by confinement | One scale with sigma (C1), but the gap is the weaker property (3.1h) |
| 10 | b2 | Lattice regularisation at the joining scale | The crossover features are lattice features. The lattice is needed only as an ultraviolet regulator |
| 11 | c7 | One inequality proves it all | BELIEF test only (adjoint-blind tools against the K7 end point, which is CONTESTED) |
| 12 | d6 | "It was tried" as a discard reason | A failed search rules out nothing |
| 13 | a10 | theta = 0 left implicit | chi is measured non-zero (L14); theta = pi cannot be trivially gapped (anomaly, recalled) |
| 14 | e5 | Asymptotic freedom holds non-perturbatively | Supported (L7, L8, E6); not contradicted |
| 15 | e6 | Universality of nearby actions | Supported (L8); not contradicted |

**1.2 Places where the measured mechanism and the lane's route differ (from row 1063 steps 3, 5, 6, 9).**

- D1. The lane's wall (W) is stronger than the Clay gap in four ways (row 1052, quoted by row 1063 5.0): bare Wilson action; every lattice of the sequence; periodic all-sector cubes, hence the flux half; a bounded Casimir free energy. The measured mechanism says the gap is the weaker property (3.1h, C6, 6b).
- D2. The measured gap is a 0++ plaquette-type correlator decay (L1, L2, b10). The lane's (W) reads the transfer gap of the periodic cube in all sectors.
- D3. The firm mechanism is the confining flux tube with universal string behaviour (L11-L13, T7). Every gauge-invariant measured form of it is a confinement quantity (6b). Vortex, monopole, Gribov and K7 end-point readings are CONTESTED.
- D4. Continuum ratios hold from correlation length 1.5 lattice spacings (C5). The lane's seed sits at box sizes of about 20 correlation lengths (row 720, quoted in M3).
- D5. The uncovered region is two to four factor-2 blockings at fixed physics (C10), each at order-one coupling.
- D6. Confined boxes need side at least 1/(T_c a) (C8). Smaller periodic boxes show the deconfined theory, which still has a spatial gap (d2, recalled).
- D7. Nothing singular happens at the gap scale in the continuum (b2). The band's difficulty is "no small parameter in a regime that already scales" (5.1 reading 1).
- D8. SU(2), SU(3) and large N agree within 20 percent (C7, S4): 1/N is a measured small parameter the lane does not use (d3 leaves "a small parameter in another variable" open).

**1.3 Row 1063's own verdict.** No new route: M1-M9 are each held by another FINISH row or dead (its step 7). No filter corrected. Its 9.5 says another measured-physics exercise on this wall mainly finds the lane's map again. This row must therefore produce vectors that M1-M9 do not contain, or report that none survives.

Left for step 2: row 1064's reading.

## Step 2: row 1064's reading, read in full (85 lines)

Source: `library/prior/gap-measured-read-luna.md` (gpt-6-luna, a literature digest, no proof, unchecked). It says its repository search could not be done (index and registry absent in its checkout).

**2.1 What it adds to row 1063's record (all MEASURED unless marked; guides only).**

- Scale at coarser couplings (Teper 1998 review, hep-th/9812187): a sqrt(sigma) = 0.69(5) at beta 2.0, 0.2686(21) at 2.4, 0.1834(26) at 2.5, 0.0636(12) at 2.85. Row 1063 had no value below 2.2986. So the lattice at beta 2.0 has a sqrt(sigma) about 0.69, and one factor-2 coarsening of the beta 2.3 lattice (0.368 to 0.74) lands near beta 2.0.
- The crossover peak (Engels and Scheideler, hep-lat/9610019): pseudo-specific-heat peak at beta_co = 2.23(2) for L at least 8, height C_V = 1.685(10), "not an ordinary phase transition". This agrees with T-BAND of row 1063 (peak 2.1-2.2 on 8^4).
- Closed-string correction (Lucini and Teper, PRD 64, 105019): torelon energy a m_l = a^2 sigma L - c_L pi/(3L) with c_L = 0.98(4), SU(2), beta 2.55, strings longer than 1 fm. Open-string term (Luscher and Weisz 2002): -pi/(12 r), SU(3).
- Second continuum determinations: SU(2) 0++ = 3.74(12) (Teper), 3.78(7) (Lucini, Teper, Wenger 2004), 3.781(23) (Athenodorou and Teper 2021). The three agree.
- Mixed action (Bhanot and Creutz 1981): triple point near (beta_F, beta_A) = (0.55, 2.34), end point near (1.57, 0.78). Row 1063 marks the end point CONTESTED (Mathur and Gavai; Datta and Gavai). Row 1064 does not contest it. I keep CONTESTED.
- T_c/sqrt(sigma) scales over beta 2.30-2.75 although T_c and sqrt(sigma) separately do not (Fingberg, Heller, Karsch).
- Large N: N = infinity scalar 3.307(53) (2004) against 3.072(14) (2021). Smooth 1/N^2 fits in both.

**2.2 What it marks CONTESTED.** Centre vortices (projection dependent), abelian monopoles and the dual superconductor (maximal abelian gauge), Landau-gauge propagators and the Gribov region (gauge dependent). A vector in this file whose only support is one of these is marked CONTESTED-ONLY.

**2.3 What is firm in both records (used as guides in step 4).** F1: the lightest state is the 0++ glueball, with m = 3.78 sqrt(sigma). F2: a finite string tension with the bosonic-string corrections in both the open and the closed geometry. F3: T_c/sqrt(sigma) about 0.70, second order for SU(2), in the 3D Ising class. F4: no bulk transition on the Wilson axis, a smooth peak at beta about 2.2. F5: ratio scaling from correlation length about 1.5. F6: smooth dependence on N.

Left for step 3: the lane's files, read only to list what is already on file.

## Step 3: what the lane already holds (read only to avoid redoing work)

Read in full: `parts/gap.md` (261 lines) and `library/gap-wall-vectors-max.md` (row 1053, 387 lines). Read in part: `library/gap-wall-vectors-check-astra.md` L335-492 (the verdicts on V1-V5). The same-provider check `gap-wall-vectors-check-opus.md` was read only through its summary in `parts/gap.md` L152.

**3.1 What binds this row.**

- The wall is (W): a bound (L_0, D_0) of (BDD-Delta) and a physical size L at least 4 L_0 with z^-(L) > 256 D_0 + 30 (`parts/gap.md` L21-23). The price: (W) iff (BDD-Delta) and (Z-UNB); (W) follows from (CAS) with theta < 1 (L257-259).
- Two kinds of input (L47-50): (K-one), a property at one scale in the band; (K-flow), a statement that reads first-passage data and is carried through the band by a step that fails for U(1), frozen groups and products with a massless factor. For (K-flow) the lane has constraints and no refutation device (L246-248).
- Route registry (L172-181): RA contraction of D, RB sign in beta, RC one-scale number, RD dichotomy, RE sector engines, RF functional inequalities, RG hierarchical comparison, LC level convexity. None near closure.
- Row 1053: V1 (2+2 anisotropic face, Orland's anchor) FAILS as a route; V2 (parametric seed near the anchor) and V4 (infrared measure first) are OPEN uncompleted proposals after the gpt-6-astra check; V3 FAILS; V5 (frozen Pin(2)) is a GUIDE-grade test.
- Row 1052: Lemma FLUX-W ((W) forces the flux energies above the gap) and the target T_JW-lat (no flux clause). Check 1054: the swap "loses the one-box reduction until a finite-size criterion for T_JW-lat exists".
- Row 1063's M1-M9: flux tube (rows 1025, 1052), vortex free energy (row 1018 (T-vor)), counted blockings ((CAS), row 708), a join away from the Wilson axis ((UNIV-FP)), area law to gap (dead), seed below the crossover (ceilings), effective string theory (no consumer), large N (off the path), misframing (none).

**3.2 Keyword count over `library/` and `parts/` (files that contain the word; done before any vector is named).** sharpness 46; Simon-Lieb 20; Borgs 39; Dobrushin 127; Aizenman 26; Duminil 15; Griffiths 41; Ginibre 42; Higgs 60; Fradkin 13; complementarity 2; Polyakov loop 29; torelon 20; toron 43; Koller 12; femto 2; step-scaling 31; Schrodinger functional 12; Tomboulis-Yaffe 34; 't Hooft loop 14; duality 100; large N 49; Makeenko 14; Eguchi 4; Hagedorn 4; random current 9; spin foam 9; Debye 9; screening mass 4 (three of them rows 1063, 1065); dimensional reduction 4; Svetitsky 1 (a not-read list); Bachas 1; gluelump 2; effective string 2; path coupling 1 (a search-term list); Ollivier 4.

**3.3 Specific places found (so they are not redone).**

- Higgs complementarity: `gap-assume-opus.md` item 77 ("every path to the pure theory at large beta crosses the order-one region at zero hopping. Removal needs a uniform rate"); `gap-wall-assumptions-opus.md` I29, N12.
- Femto-universe and the order of limits: `gap-brainstorm-max.md` idea 36 (merged into G7); `gap-kurt-max.md` L170.
- Free-wall boxes: Route W with crux (W-ENG) and the variant W' (`gap-next3-max.md` L281, L294; rows 858, 900).
- Schrodinger-functional coupling: `prior/gap-gauge-stiffness-read-opus.md` L67, L179 ("nothing rigorous is known about it beyond the classical minimum"; "no monotonicity in L").
- A rigorous four-to-three dimensional reduction at high temperature: "NOT in the lane" (`prior/gap-outside-read-opus.md` L51); `prior/gap-3dmix-read-opus.md` L211 searched for it.
- Hagedorn growth at the seed temperature: `gap-assume-opus.md` item 52 (a GUIDE).
- Transport and coarse curvature (Dobrushin, Wu, Ollivier): `gap-brainstorm-max.md` L91 (row 787 reading).
- Orbit-space curvature, Singer, Mondal: `prior/gap-crux-lit-2.md` L154; row 1032 B8.

Left for step 4: name candidate vectors from the fifteen assumptions and D1-D8, each with a grep of `library/open-core.md` and the FINISH rows.

## Step 4a: candidates that the measured record suggests at once, each grepped before it was named

Rule 0a grep for every line: `library/open-core.md` (0 hits for each word below), FINISH.md rows, and `library/`, `parts/`. "Found" means the idea is on file with the place named. None of these is attacked here.

| Candidate (measured source) | Grep words | Result |
|---|---|---|
| Centre-stabilised small circle, deformed Yang-Mills, continuity in the circle size (d2, e10, b6) | Unsal; deformed; adiabatic continuity | Found: rows 1004, 1005 (`gap-outside-box-max.md` L431, `prior/gap-outside-read-opus.md` L103-152), row 858 (`gap-crux-exercise-r858-max.md` L326: "the passage from thin n to n = a ... a conjecture"), `gap-skeleton-max.md` L371 |
| Rigorous 3D compact U(1) gap as a selective input (Gopfert and Mack) | Gopfert | Found: 19 files, 9 FINISH lines (row 1004 brief) |
| Binary icosahedral group as a finite twin of SU(2) in the band (c6, c10) | icosahedral | Found: `gap-brainstorm2-max.md` G13 and Top 3; 28 FINISH lines |
| The critical slab as a test: a tool must use the long sides (C8, L3) | SMALL-BOX; Borgs | Found: test K6 "Critical slab" (`gap-crux-exercise2-max.md` L430); SMALL-BOX (`gap-tiltproof-max.md` L100) |
| Free-wall boxes, no flux sector (D1, b6) | Route W; W-ENG | Found: rows 858, 900, `gap-next3-max.md` C1; a counterexample to (W-ENG) from positivity and axis exchange alone is in FINISH |
| Fundamental Higgs field as an infrared regulator, complementarity (d2) | complementarity; Fradkin | Found: `gap-assume-opus.md` item 77 ("Removal needs a uniform rate") |
| Hot phase: spatial gap at fixed N_t and large beta (d2) | screening mass; dimensional reduction | Not attacked on file; FAILS at once: at fixed N_t and beta to infinity it contains the 3D Yang-Mills gap at weak 3D coupling (the magnetic mass), which is the same wall in three dimensions (ARGUED, standard dimensional reduction, recalled). Rows 988, 992 met the 3D mixing input already |
| Large N as the small parameter (D8, S4) | large N; Eguchi | Found as M8 of row 1063, off the path. Measured addition (recalled, not re-read): Wilson SU(N) has a first-order bulk transition for N at least 5 (Lucini and Teper 2001), so e4 is false at large N; it binds fixed-coupling tools only, as K7 does |
| Loop equations with positivity (a bootstrap at order one) | Makeenko; loop-eq | Found: `gap-loop-eq-opus.md`, `prior/gap-crux-lit-nonab.md` L166 |
| Step-scaling or Schrodinger-functional coupling as the carried quantity (D5, D7) | step-scaling; Schrodinger functional | Found: row 859; `prior/gap-gauge-stiffness-read-opus.md` L67, L179 |
| Sharpness of the deconfinement transition by Ising-type inequalities for the centre (L3) | sharpness; Simon-Lieb; Griffiths | Found in form: (UNIV-FP) item with "an unfrustrated Z_2 theory with Griffiths inequalities" (row 900), Mack-Petkova (row 1018). It gives the flux half at best |
| Concavity of the static potential and of the Polyakov-loop free energy (Bachas; Borgs and Seiler) | Bachas | Found: `gap-brainstorm2-max.md` L470. Reflection positivity gives upper bounds on masses only (checked by hand here: log W_L(R) is midpoint convex in R, so the torelon energy is at most every finite-distance slope) |

Reading: every candidate that comes straight from the physics literature of the measured record is on file. This agrees with row 1063 step 7. The rest of step 4 (next block) looks for vectors that come from the numbers and from the places D1-D8, not from the literature list.

## Step 4b: candidates derived here from the measured numbers, and where each was found on file

These came from my own derivations, not from the literature list. Each was derived first and grepped second. All five are on file. I record the derivation in one line so that the match can be checked.

| Candidate (derivation in one line) | Measured support | Found on file |
|---|---|---|
| A bounded logarithmic derivative: -d(m a)/d beta is the action excess of the lightest state (Hellmann-Feynman), so "action excess at most C times mass" gives m(beta) >= m(beta_0) exp(-C (beta - beta_0)) | From L2 of row 1063: -d log(a m_G)/d beta = 2.44, 3.43, 3.11, 2.99, 3.14 on the five intervals from beta 2.2986 to 2.70 (computed here by hand from the table; a guide); one-loop value 3 pi^2/11 = 2.69 | `gap-brainstorm-max.md` idea 46 and G8, crux (NOCRIT-HF); `gap-ladder-max.md` A3, crux (SUM-RULE); `gap-vir-sc.md` (VIR_K), (LEV_K) |
| A positive finite-size plaquette shift: d D(n; beta)/d beta = 6 n^4 (P_n - P_inf), so "P_n >= P_inf" makes D non-decreasing in beta at fixed n, and on a halving sequence of spacings D^+(2L) <= D^+(L), which gives (BDD-Delta) from one start value | Positive interaction measure eps - 3p in SU(2) thermodynamics (recalled, not re-read) | (MONO-Delta), Lemma DIL, Proposition MB, Corollary MB1 (`gap-phys-seed.md` L344-384, row 720); route RB. The lane also records that the Griffiths-Ginibre identification argument is wrong and that (MONO-Delta) fails for the ordered Ising model |
| A two-torelon bound: by reflection in a transverse plane, <(P_x P_y)(0) (P_x P_y)(t)> >= G(t)^2, so the centre-even gap of a geometry with a short periodic side is at most twice the flux energy | Torelon energies sigma L - pi/(3L) (row 1064) | `gap-brainstorm2-max.md` Top 2 (L470) and its grep words "two-torelon", "transverse reflection positivity" |
| Area law gives the gap | One scale (C1) | Row 1063 M5, dead. Added here: it is false in the class, because a liquid-gas end point inside a confined phase keeps the area law and has a massless scalar (belief-grade for K7; the same reason as the w_p test) |
| The two banks nearly meet in physical units: Schrodinger-functional perturbation theory is quantitatively valid up to box side about 0.6/T_c (recalled: Luscher, Sommer, Weisz and Wolff), and the Wilson lattice is inside the proved strong-coupling range (beta <= 1.0109) at spacing about 0.84/T_c | a sqrt(sigma) = 0.69 at beta 2.0 (row 1064); my extrapolation to beta 1.0 uses leading strong coupling (a guide of low quality) | In form: C10 of row 1063, (CAS) "on a bounded range", (UNIV-FP). The factor is not on file; it is a guide and moves nothing, because the blocked action at that spacing is not Wilson's |

Reading after 4a and 4b: the lane's map contains the measured mechanism, the literature of the record, and the first consequences one can derive from the numbers. A new vector has to be a new mathematical object. Step 4c names the ones I could build, and says plainly where I could not.

## Step 4c: task (1), item by item

"Found" = on file with the place (steps 3, 4a, 4b). "New object" = not found by the greps named; it is written out in step 5. A blank vector column means no vector.

### The fifteen assumptions (ranking of step 1.1)

| Rank | ID | Does the measured verdict give a new vector? |
|---|---|---|
| 1 | c2 band in bare Wilson coupling | No. Join at an RG effective action: (UNIV-FP), V4 of row 1053 (OPEN proposal), no mechanism. Row 1063's own reading closes the hope that the band is an artefact |
| 2 | b3 Wilson action | No. Action choice is (UNIV-FP); positive-plaquette and no-monopole weights are row 900 item 2. One new object tried: W6 (a gap for almost every action of a family) |
| 3 | c4 strong coupling reaches the band | No. Counted blockings = (CAS), route RA; seed below the crossover = M6, ceilings |
| 4 | e4 no bulk transition | No route. One new object: W2 (what convexity alone gives for almost every beta). One test note: W7 (the Wilson axis has a bulk transition for SU(N), N at least 5, recalled) |
| 5 | c6 small-box criterion | No. Test K6 "critical slab"; SMALL-BOX; the seed needs about 40 correlation lengths (`gap-phys-seed.md` L432) |
| 6 | c10 small-lattice numerics | No vector (a caution for guides, on file) |
| 7 | b6 periodic torus | No. Free walls = Route W; twisted = Theorem TW-T. One new object: W1 (the flux ladder across widths) |
| 8 | d2 deconfined models as tests | One vector, W3 (the hot phase as a target); it FAILS in step 5. Not used as a test by the lane |
| 9 | e10 gap through confinement | No. T_JW-lat (row 1052); area law to gap is false in the class (step 4b) |
| 10 | b2 lattice at the joining scale | No. V4 of row 1053; continuum-first in a small box is `gap-brainstorm-max.md` idea 36 |
| 11 | c7 one inequality | No vector |
| 12 | d6 "it was tried" | No vector |
| 13 | a10 theta = 0 | No vector toward the theta = 0 gap (row 838 item 72) |
| 14 | e5 asymptotic freedom beyond perturbation theory | No vector. Its use as a carrier is (SUM-RULE), (NOCRIT-HF), on file |
| 15 | e6 universality | No vector beyond (UNIV-FP) |

### The eight places where mechanism and route differ (step 1.2)

| Place | New vector? |
|---|---|
| D1 (W) stronger than the Clay gap in four ways | No. T_JW-lat, FLUX-W, Route W |
| D2 measured object is one 0++ correlator | One object tried, W4 (enclosure of the first excited level from a trial state); a renaming, FAILS |
| D3 flux tube firm, the rest CONTESTED | W1 follows the firm mechanism (the sign of the Luscher term). Vortex, monopole and Gribov lines are CONTESTED-ONLY and get no vector here; (T-vor) and (TB)_n are on file |
| D4 scaling from correlation length 1.5 | No. It supports (SUM-RULE) as a guide (step 4b) |
| D5 two to four blockings | No. (CAS) |
| D6 box side at least 1/(T_c a); hot boxes keep a spatial gap | W3 (FAILS); W5 (the critical slab as an anchor; no consumer) |
| D7 nothing singular at the gap scale in the continuum | No vector |
| D8 smooth in N | W7 (a test note), no route |

So task (1) gives seven objects, W1 to W7. None is a new route across the wall on its face. Step 5 states each exactly and runs the kill tests.

## Step 5: tasks (2) and (3). Each object stated, then killed or kept

Kill sheet used: K1 Lemma PT (product with a massless factor), K2 Proposition NP, K3 Theorem D2, K4 Lemma SHEET, K5 compact U(1), K6 frozen Q_8 and 2T, K7 five dimensions, Lemma CEN+, Lemma WN, and the spec check S0-S4 (S0: does it rename an open statement; S1 selective; S2 a rate; S3 reads the whole state space; S4 not uniform over fields), in the form of `library/gap-invent-selective-max.md` L52-63 as row 1053 quotes it. A pass is no support.

Notation for W1. Periodic lattice with sides (n_1, n_2, n_3, n_4). C_mu is the centre flip of all mu-links that cross one hyperplane. T_4 is the transfer operator along direction 4 on the slice n_1 n_2 n_3; it commutes with C_1. Z_+ and Z_- are the traces of T_4^(n_4) over the sectors C_1 = +1 and C_1 = -1. Then Z_+ + Z_- = Z and Z_+ - Z_- = Z^tw, the partition function with a twist in the (1,4) plane. E(n_1) = log(lambda_0^+/lambda_0^-) is the flux energy of the slice.

### W1. The flux ladder across widths (source: D3, the sign of the Luscher term; b6)

- **Statement (SIG-MONO).** For Wilson SU(2) in dimension 4 and every width L in the confined range, E(2L) >= 2 E(L). Equivalent form (Lemma R1, step 7): the long flux tube has non-negative excess Renyi-2 entropy per unit length at inverse temperature L.
- **Consumer.** With one width L_1 where E(L_1) > 0, it gives L E(L) >= (L^2/L_1) E(L_1) on the widths 2^k L_1: the flux half of (Z-UNB) for slices that are doubled in the flux direction only.
- **What it changes.** The flux half would need one size, not a rate. It would not need the vortex containers of (T-vor) or the inequality (TB)_n.
- **Source and measurements.** D3; the closed-string correction c_L = 0.98(4) of Lucini and Teper (row 1064) gives E(2L) - 2E(L) = pi/(2L) > 0 in the free-string form. Firm as a sign in the measured range (strings longer than 1 fm).
- **Cheapest kill tests.** (a) Is the finite form true in a solvable Wilson model? (b) Does the consumer reach the cube? (c) K1.
- **Kill pass.** (a) The finite form (FIN), Z_-/Z_+ at (2 n_1, n_4) at most the square of Z_-/Z_+ at (n_1, n_4), is FALSE for two-dimensional Wilson SU(2) at small beta and large area (Counterexample R3, step 7, PROVED by hand). So (FIN) does not follow from positivity and axis exchange, which the two-dimensional model has. In the four-dimensional model with decoupled sheets (FIN) holds at large area, by the position entropy of the sheet (step 7, R4). The sign is therefore dynamics, not structure. (b) The consumer does not reach the cube: nothing controls the flux energy when the two transverse sides double. (c) K1: it reads the centre-odd factor only, so by Lemma FAC of row 1025 its conclusion is a flux statement, never the seed. K5: in two dimensions and for abelian groups at strong coupling the asymptotic form holds with equality or by positivity, so it is blind (S1 fails). S0: it is a part of the flux half of (Z-UNB) with a sign in place of a rate; the sign itself has no mechanism.
- **Verdict.** FAILS as a vector to the gap (flux half only, blind, consumer incomplete). Kept: Lemma R1 and Lemma R2 (exact identities, PROVED in step 7) and Counterexample R3.

### W2. What convexity alone gives for almost every coupling (source: e4)

- **Statement.** The pressure f is convex in beta and -12 <= f' <= 0. So the second derivative of f is a positive measure of total mass at most 12 on (0, infinity). Its atoms are at most countably many (the first-order points). Its absolutely continuous density chi satisfies: the set of beta with chi(beta) > K has Lebesgue measure at most 12/K.
- **Consumer.** None on the path of (W). Off the path: e4 ("no bulk transition") in the form "bounded specific heat" of row 996.
- **What it changes.** Nothing for the gap. It says that a bulk critical point costs measure: a divergent specific heat is confined to a null set, with an explicit Chebyshev bound around it.
- **Source.** e4; the measured peak of Engels and Scheideler (finite, row 1064).
- **Cheapest kill test.** K5: does compact U(1) pass? Yes. The statement holds for every lattice model with a bounded action, so it cannot separate anything (S1 fails). A finite specific heat does not give a gap: the Coulomb phase has a finite one (plaquette correlations fall like distance^(-8), summable in four dimensions; recalled Gaussian value, ARGUED).
- **Verdict.** PROVED (three lines: monotone f', total variation at most 12, Chebyshev) and FAILS as a vector (blind, no consumer). Not found on file (grep "Alexandrov", "almost every beta": 0 and 5 unrelated). It does not identify chi with the truncated correlation sum of an infinite-volume state; that step is not done.

### W3. The hot phase as the target (source: d2, D6)

- **Statement.** For fixed N_t and all beta above the deconfinement coupling of the slab, each pure phase of Wilson SU(2) on Z^3 x Z_(N_t) has exponential clustering of gauge-invariant local observables in the three long directions.
- **Consumer.** None toward (W) or T_JW-lat: it is a theorem about thermal states above T_c.
- **Cheapest kill test.** Is it easier? At fixed N_t and beta to infinity the three-dimensional gauge coupling is beta N_t to infinity, and the magnetic sector is three-dimensional Yang-Mills near its continuum limit. Its gap is as open as the four-dimensional one (ARGUED; standard dimensional reduction, recalled; the lane found no rigorous four-to-three reduction, `prior/gap-outside-read-opus.md` L51).
- **A further block, from the measured record.** A route by continuity in the slab width from the hot side to zero temperature crosses the width 1/T_c, where SU(2) has a second-order point (L3). So the periodic slab family cannot carry a gap from hot to cold. This is test K6 of the lane read as a block on a path.
- **Verdict.** FAILS (S0: it renames the three-dimensional wall; no consumer). The three-dimensional mechanism of Karabali, Kim and Nair is on file as a GUIDE only (`prior/gap-crux-lit-nonab.md` L197, Nair arXiv:2608.10133: "regularization issues prevent a general proof").

### W4. Enclosure of the first excited level from a trial state (source: D2, b10)

- **Statement.** Let psi be a smeared-plaquette trial vector orthogonal to the vacuum, eta its Rayleigh quotient for the transfer operator, eps^2 its variance, and nu a bound for the spectrum on the orthogonal complement of the vacuum and of psi, with nu < eta. Then lambda_1 <= eta + eps^2/(eta - nu) (Temple's inequality, recalled).
- **Measured support.** Large overlaps of smeared operators with the lightest state (recalled lore; not in rows 1063, 1064).
- **Cheapest kill test.** S0: the input nu is a bound on the spectrum of the transfer operator on a subspace of codimension two. That is a gap statement of the same kind as the target. Also, reflection positivity makes every measured effective mass an upper bound for the gap, so no measured correlator bounds the gap from below.
- **Verdict.** FAILS (S0, a renaming). Grep "Temple", "Kato-Temple": 0 files, so this failure was not on file.

### W5. The critical slab as an anchor (source: L3, D6)

- **Statement.** In continuum SU(2) on R^3 x S^1 of circumference L slightly above L_c = 1/T_c, the lightest state is the torelon with E(L) to 0 as L falls to L_c, and by the two-torelon bound the centre-even gap is at most 2 E(L). So t = (L - L_c)/L_c is a small parameter inside the theory, with the three-dimensional Ising field theory as the effective description (BELIEF: Svetitsky and Yaffe universality; measured class, L3).
- **Consumer.** None. A small parameter near L_c describes a regime with a small gap. It gives no bound at L = infinity, and the path to L = infinity is the confined phase itself.
- **Kill.** S0 for the route. As a test it is K6 of the lane ("critical slab", `gap-crux-exercise2-max.md` L430).
- **Verdict.** FAILS as a vector; found again as a test.

### W6. A gap for almost every action of a family (source: b3, e6, K7)

- **Statement.** In a finite-parameter family of reflection-positive plaquette weights that contains Wilson's, the set of parameters where the infinite-volume lattice theory has no gap is Lebesgue-null.
- **Consumer.** The Clay target needs one regularisation, so a generic member would do, given a carry to the continuum for that member (the account treats Wilson only: (UNIV-FP)).
- **Cheapest kill test.** Name the first lemma. The only soft tool that gives almost-everywhere statements in a coupling is convexity (W2), and W2 is blind. No analytic structure in the parameters is known beyond convexity of the pressure. The carry to the continuum is at couplings tending to infinity, where "almost every" gives no uniformity.
- **Verdict.** FAILS (no mechanism; first lemma blind; the consumer needs (UNIV-FP)).

### W7. A test note: the bulk transition of Wilson SU(N) at large N (source: e4, D8)

- **Statement (BELIEF, measured, recalled and not re-read: Lucini and Teper 2001; Campostrini).** Wilson SU(N) in four dimensions has a first-order bulk transition on the Wilson axis for N at least 5. So a fixed-coupling tool (T_fix, or uniqueness of the infinite-volume state at one coupling) whose hypothesis reads only "compact simple group, Wilson weight, four dimensions" and is uniform in N is refuted at that coupling.
- **What it adds.** K7 and w_p change the weight. This test keeps Wilson's weight and changes N. It does not bind T_W tools (their couplings tend to infinity, on the weak side). It is belief-grade.
- **On file?** `gap-phys-seed.md` L378 uses "SU(N) for N >= 5" for (MONO-Delta). As a line of the test table it is not on file (grep "bulk transition": 17 files, none in the table of `parts/gap.md`).
- **Verdict.** Not a vector. A GUIDE-grade line for the test table, at the lead's choice.

### Summary of the kill pass

| Object | Kind | First failing test | Mark |
|---|---|---|---|
| W1 flux ladder | flux-half inequality | finite form false (R3); blind; consumer stops at the cube | FAILS as a vector; identities PROVED |
| W2 almost-every-beta specific heat | soft lemma | K5 (blind), no consumer | PROVED, FAILS as a vector |
| W3 hot phase | changed target | S0 (three-dimensional wall); blocked at 1/T_c | FAILS |
| W4 enclosure | (K-one) | S0 | FAILS |
| W5 critical slab anchor | parametric regime | no consumer; is K6 | FAILS |
| W6 generic action | changed target | no mechanism | FAILS |
| W7 large-N bulk transition | test | - | GUIDE-grade test line |

No object is marked CONTESTED-ONLY, because none rests on the vortex, monopole, Gribov or end-point readings. Those readings gave no vector here: their gauge-invariant forms, (T-vor) and (TB)_n, are on file.

## Step 6: task (4), ranking

No object of step 5 survives as a vector to the gap. So the ranking is of the pieces that are kept, by what each would change divided by the cost to find out.

| Rank | Piece | What it would change | Cost to find out | Kind |
|---|---|---|---|---|
| 1 | W1, Lemmas R1, R2 and the open sign (SIG-MONO) | It turns the flux half on doubled widths into a sign: the excess Renyi-2 entropy of a long flux tube. The measured Luscher term gives that sign (firm on strings longer than 1 fm). It cannot give the seed (K1), and it stops before the cube | Done here for the identities (step 7). The sign has no mechanism; no row is proposed | exact identity; flux half; blind |
| 2 | W7, the large-N bulk transition as a test line | One more line in the test table for fixed-coupling tools, on the Wilson weight itself | A lead edit after a reading row confirms the source | test, GUIDE grade |
| 3 | W2, the almost-every-beta bound | Nothing on the path of (W). It bounds the measure of couplings with a large specific heat | Done (step 7.3) | soft lemma, blind |

**What the measured record weighs on statements already on file (guides; they move no status).** These are numbers the lead can use when ranking rows that exist. Each was computed here by hand from the tables quoted in rows 1063 and 1064.

| On-file statement | Measured guide | Reading |
|---|---|---|
| (SUM-RULE), `gap-ladder-max.md` A3: -E_j' <= c E_j + c', "c near c_AF" | -d log(a sqrt(sigma))/d beta = 3.25(4), 3.41(4), 3.51(3), 3.35(3), 3.11(3) on the five intervals from beta 2.2986 to 2.70; for a m_G: 2.44(24), 3.43(27), 3.11(15), 2.99(13), 3.14(13). One loop: 3 pi^2/11 = 2.69. Two loops at beta 2.5: 2.52 | The constant must be at least 3.5 in the band, 30 percent above one loop. A form with c within 25 percent of c_AF is refuted there for the string scale (guide-grade refutation). The ratio is bounded and has its maximum near beta 2.47 |
| Which half binds at the seed size | L m_G = 30 at L = 7.9/sqrt(sigma). L E_flux(L) = sigma L^2 - pi/3 = 30 at L = 5.6/sqrt(sigma) | At the size where the engine's 30 is reached, the glue half is the binding one. The flux half is reached 1.4 times earlier in size. Found in part: `gap-next3-max.md` L290 ("The glue half had one row") |
| (MONO-Delta), `gap-phys-seed.md` L351 | The slab analogue, eps - 3p > 0, is measured positive in SU(2) (recalled, not re-read) | Supports the sign as a guide. The symmetric-torus plaquette shift is below the errors of the data in rows 1063 and 1064 (8^4 at beta 2.3: 0.60226(26) against 0.6022) |
| Test K6 "critical slab" | beta_c(N_t = 4) = 2.2985(6); 1/(T_c a) = 3.8, 5.9, 7.8, 10.6 at beta 2.30, 2.43, 2.51, 2.60 | A tool that reads the specification through windows smaller than these sides has the same input on the critical slab. This is the lane's K6 with the measured sides |
| Frozen 2T as a test "at order one" | Freezing couplings (recalled, not re-read: Petcher and Weingarten): about 2.2 for 2T, 3.2 for 2O, 5.8 for 2I | In the band [2.3, 2.6] only Q_8 and 2T are frozen; 2T by a margin of about 0.1. 2O and 2I are twins of SU(2) there, not tests (found: `gap-brainstorm2-max.md` G13) |

## Step 7: task (5), hand work on the top piece (W1), and the short proof of W2

Rule 0a before the attempt. `library/open-core.md`: no hit for "Renyi", "excess entropy", "flux ladder", "superadditiv" of flux energies, "E(2L)". FINISH rows: the flux half is held by rows 1018 ((T-vor)), 1025 ((TB)_n) and 1052 (FLUX-W). None states or attacks the doubling of the width. `library/`: "Renyi" occurs for chi-square information between slices (`gap-direction-max.md` L346, `gap-ladder-max.md` L135), not for sector traces; "concavity of flux energies" is named once as an idea (`gap-crux-exercise2-max.md` L382), with no statement. I proceed, and I do not attack (T-vor), (TB)_n or (Z-UNB).

### 7.1 Setting and the three facts used

Wilson SU(2) on the periodic lattice with sides (n_1, n_2, n_3, n_4), all at least 3; the anisotropic Wilson weights are allowed. Notation as in step 5.

- (F1) T_4 is a positive trace-class operator, and it commutes with the centre flip C_1. This is the lane's (E2) with the flux sectors of Theorem R (row 744); used as given.
- (F2) Tr(T_4^(n_4) C_1) = Z^tw, the integral with the sign of the coupling reversed on the (1,4) plaquettes of one column (one value of (x_1, x_4), all (x_2, x_3)). So 0 < Z^tw <= Z, and Z_+ = (Z + Z^tw)/2, Z_- = (Z - Z^tw)/2. Used as given ('t Hooft 1979; lane: Theorem TW-T, row 1004).
- (F3) The reversed column is symmetric under the exchange of the axes 1 and 4. So Z^tw = Tr(T_1^(n_1) C_4), where T_1 is the transfer operator along direction 1 on the slice (n_2, n_3, n_4). Hence Z_+ and Z_- are also the traces of T_1^(n_1) over the sectors C_4 = +1 and C_4 = -1.

### 7.2 Lemma R1 (the Renyi ladder; PROVED)

**Statement.** (a) For both signs, Z_s(2 n_1, n_4) <= Z_s(n_1, n_4)^2. Put R_s(n_1, n_4) := log(Z_s(n_1, n_4)^2 / Z_s(2 n_1, n_4)) >= 0. It is the Renyi-2 entropy of the state T_1^(n_1)/Tr on the sector C_4 = s.
(b) log(Z_-/Z_+)(2 n_1, n_4) = 2 log(Z_-/Z_+)(n_1, n_4) - (R_-(n_1, n_4) - R_+(n_1, n_4)).
(c) Let lambda_0^s(n_1) be the top eigenvalue of T_4 on the sector C_1 = s of the slice (n_1, n_2, n_3), and rho_s(n_1) := 2 log lambda_0^s(n_1) - log lambda_0^s(2 n_1). Then rho_s >= 0, R_s/n_4 tends to rho_s as n_4 grows, and E(2 n_1) - 2 E(n_1) = rho_-(n_1) - rho_+(n_1).

**Proof.** (a) By (F3), Z_s(n_1, n_4) is the trace of A = T_1^(n_1) restricted to an invariant sector, and A >= 0. For a positive trace-class operator Tr A^2 <= (Tr A)^2, and Tr A^2/(Tr A)^2 = Tr(rho^2) with rho = A/Tr A. (b) is algebra. (c) In the 4-channel Z_s(n_1, n_4) = sum of the n_4-th powers of the eigenvalues of T_4 on the sector, so (1/n_4) log Z_s(n_1, n_4) tends to log lambda_0^s(n_1); the same with 2 n_1. So R_s/n_4 tends to rho_s, which is at least 0 by (a). E(n_1) = log lambda_0^+(n_1) - log lambda_0^-(n_1) by definition; subtract. QED

**Reading.** (SIG-MONO) at the width n_1 is the statement rho_-(n_1) >= rho_+(n_1): the doubling defect of the top eigenvalue is larger in the flux sector than in the vacuum sector. rho_+ is the doubling defect of the vacuum energy of the slice. rho_- - rho_+ is the excess Renyi-2 entropy per unit length of a long flux tube at inverse temperature n_1.

### 7.3 Lemma R2 (twist-ratio form; PROVED)

Put t = Z^tw/Z in (0, 1]. Then Z_-/Z_+ = (1 - t)/(1 + t) = exp(-2 artanh t). So the finite form (FIN) of step 5 holds at (n_1, n_4) if and only if artanh t(2 n_1, n_4) >= 2 artanh t(n_1, n_4), that is t(2 n_1, n_4) >= 2 t/(1 + t^2) with t = t(n_1, n_4). Proof: with t = tanh a, (1 - t)/(1 + t) = e^(-2a) and tanh 2a = 2t/(1 + t^2). QED

### 7.4 Counterexample R3: (FIN) is false for two-dimensional Wilson SU(2) (PROVED)

On the two-dimensional torus with A = n_1 n_4 plaquettes, the character expansion gives (recalled, standard; the lane uses it at `gap-phys-seed.md` L369): Z = sum over j in {0, 1/2, 1, ...} of c_j^A and Z^tw = sum of (-1)^(2j) c_j^A, with c_j = (2/beta) I_(2j+1)(beta), up to a common factor. So Z_+ = sum over integer j, Z_- = sum over half-odd j, and both depend on A only.

Put v = c_1/c_0 = I_3/I_1 and w = c_(3/2)/c_(1/2) = I_4/I_2, and q_A = Z_+/c_0^A = 1 + v^A + ..., p_A = Z_-/c_(1/2)^A = 1 + w^A + .... (FIN) reads p_(2A) q_A^2 <= q_(2A) p_A^2. As A grows, p_(2A) q_A^2 - q_(2A) p_A^2 = 2 (v^A - w^A) + O(v^(2A) + w^(2A)). So (FIN) fails for all large A when v > w.

v > w holds for small beta: I_n(beta) = (beta/2)^n/n! (1 + O(beta^2)), so v = beta^2/24 (1 + O(beta^2)) and w = beta^2/48 (1 + O(beta^2)). At beta = 2, by the series I_n(2) = sum over k of 1/(k! (k + n)!) summed by hand to six terms: I_1 = 1.590636, I_2 = 0.688948, I_3 = 0.212740, I_4 = 0.050728, so v = 0.13374 > w = 0.07363. QED

Reading. In two dimensions the energies are exactly additive, E(n_1) = n_1 log(c_0/c_(1/2)) and rho_- = rho_+ = 0. The finite form still fails, because the vacuum sector has the lighter first excitation (v > w) and so more Renyi entropy at the same temperature. The two-dimensional model has positivity and axis exchange. So (FIN) is not a consequence of those two.

### 7.5 Remark R4: decoupled sheets in four dimensions (PROVED at leading order in u^A; the remainder bound is not written)

Take the anisotropic Wilson weight with coupling beta on the (1,4) plaquettes and 0 on the others. Then Z = (Z_2D)^N and Z^tw = (Z^tw_2D)^N with N = n_2 n_3, so t = x^N with x the two-dimensional twist ratio. With u = c_(1/2)/c_0: 1 - x = 2 u^A p_A/q_A (1 + O(u^A)), hence Z_-/Z_+ = N u^A (p_A/q_A)(1 + O(N u^A)). So the ratio of the two sides of (FIN) is (1/N)(1 + O(v^A) + O(N u^A)). For N >= 2 and A large, (FIN) holds. The factor 1/N is the position entropy of the sheet. So the sign of the finite form is decided by a competition between the position entropy of the flux sheet and the spectra of the two sectors. The energies are again additive: rho_- = rho_+.

### 7.6 A toy in the abstract class (PROVED)

On the four points (s, y), s = +1 or -1, y = 1 or 2, let T have the kernel (1/2)(K_e(y, y') + s s' K_o(y, y')) with K_e = [[3/4, 1/4], [1/4, 3/4]] and K_o = [[1/5, 1/5], [1/5, 1/5]]. All entries are non-negative, T is symmetric, it commutes with the flip of s, and its eigenvalues are 1 and 1/2 on even functions and 2/5 and 0 on odd functions. Then Tr_odd T^k/Tr_even T^k = (2/5)^k/(1 + 2^(-k)), which is 4/15 at k = 1 and 16/125 at k = 2, and 16/125 > (4/15)^2 = 16/225. So the square law fails for a positive, positivity-preserving operator with a Z_2 symmetry.

### 7.7 The mechanism behind the measured sign, and the verdict

- In the free-string form E(L) = sigma L - pi (d - 2)/(6L), so E(2L) - 2E(L) = pi (d - 2)/(4L) = pi/(2L) for d = 4. In the language of Lemma R1 this is the Renyi-2 entropy rate of the two transverse modes of the tube. A bulk excitation that the tube excludes would lower it (ARGUED; no rigorous model built).
- (SIG-MONO), in the form rho_- >= rho_+, is OPEN for Wilson SU(2) in four dimensions. It holds with equality in two dimensions and for decoupled sheets, for every compact group with a centre flip. So it is blind.
- First step that fails for a proof: the comparison of the top-eigenvalue doubling defects of two symmetry sectors of one transfer operator. Positivity and axis exchange give each defect a sign (Lemma R1 (a)) and give no order between them (R3, 7.6).
- Verdict: W1 FAILS as a vector to the gap. I stopped after R4. Not done: a remainder bound in R4; any statement for the isotropic model; the cube.

### 7.8 W2, the proof (PROVED; blind; no consumer)

f is convex in beta (Lemma DIL of row 720 quotes it; it is a limit along doublings of the convex functions F(n)/abs(n)). For every torus, F'(n)/abs(n) = -<A>/abs(n) lies in [-12, 0], because there are six plaquettes per site and 0 <= 1 - x_p <= 2. So f' is non-decreasing with values in [-12, 0] where it exists, and the Stieltjes measure df' has total mass at most 12. Its atoms are countable. Write df' = chi d beta + singular part; then the integral of chi is at most 12, and by Chebyshev's inequality the set where chi > K has measure at most 12/K. On an interval the mass is 6 (P(beta_2+) - P(beta_1-)), with P the infinite-volume mean plaquette. QED

Not shown: that chi(beta) is the sum of truncated plaquette correlations of an infinite-volume state. Compact U(1) and every model with a bounded action satisfy the same statement.
