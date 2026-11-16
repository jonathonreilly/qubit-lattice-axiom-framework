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
