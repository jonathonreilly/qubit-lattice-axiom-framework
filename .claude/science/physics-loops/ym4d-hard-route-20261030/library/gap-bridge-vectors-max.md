lead: anthropic/claude-fable-5-2/max laptop-subagent
row: 1076

# Gap bridge vectors (row 1076): working file

Status: COMPLETE (2026-11-16 local). Written step by step; the step log is in order. Checked by no one. The RESULT line is the last line of the file.

## Plan (eight steps; fixed after reading row 1076; all eight done)

1. Read row 1076 in FINISH.md. Record the reading order, the question, the six tasks, the kill tests and the marks.
2. Read in full `library/gap-bridge-exercise-opus.md` (row 1072), then `library/prior/gap-bridge-read-luna.md` (row 1073). Record what each establishes and leaves open.
3. Fetch the remote branch; read check 1074 (astra) if pushed and check 1075 (opus) if present locally. Then, only to avoid redoing work, read `parts/gap.md` and `library/gap-aniso-check-astra.md` (row 1070) sections 6 and 9.
4. Task 1: walk the highest-ranked assumptions, routes BR-0 to BR-9 and the methods of section 6a. For each, say whether a new vector lies behind it (what is carried, what the path is, what the endpoint is). Grep the lane before naming any idea.
5. Tasks 2 and 3: for each vector, the exact statement, consumer, change, source and cheapest kill test; then apply the kill tests on file. A vector that renames an open statement FAILS, with the equivalence written.
6. Tasks 4 and 5: rank the survivors; for the top one or two, invent the mechanism, write the first lemma and try it by hand, or build the counterexample.
7. Task 6: write each surviving vector as a complete brief for a proof row.
8. Marks (PROVED, ARGUED, OPEN, FAILS), scope of every negative, credits, and the RESULT line.

## Step log

### Step 1 (row read). DONE.

Row 1076 read at FINISH.md L1157. What it fixes:

- Reading order: `library/gap-bridge-exercise-opus.md` (row 1072) in full; then `library/prior/gap-bridge-read-luna.md` (row 1073); then, only to avoid redoing work, `parts/gap.md`, `library/gap-aniso-check-astra.md` (row 1070) sections 6 and 9, and the checks 1074 and 1075 if present. Grep the lane before naming any idea.
- The bridge question: carry clustering from the anisotropic region where it is provable to the isotropic point in the window 2.3 to 2.6, by a statement that uses the anisotropic data non-trivially and is not equivalent to clustering at the endpoint.
- Six tasks: (1) for each top-ranked assumption, each route BR-0 to BR-9 and each method of section 6a, is there a new vector behind it; look for a change of what is carried, of the path, of the endpoint. (2) For each vector: exact statement, consumer, what it changes, source, cheapest kill test. (3) Kill fast with the tests on file. (4) Rank survivors by change divided by cost. (5) For the top one or two: mechanism, first lemma, hand attempt, or a counterexample. (6) A complete proof-row brief for each survivor.
- Kill tests named: compact U(1) first (in the valid form of 6c of row 1072); frozen Q_8 and 2T; Pin(2) as a GUIDE-grade test; the five-dimensional test; Lemma PT; Proposition NP; Theorem D2; Lemma SHEET; Lemma CEN+; Lemma WN; Proposition CA-FAIL; Corollary NO-MON; the four-test spec check.
- Marks: PROVED, ARGUED, OPEN, FAILS. Negatives scoped to what is proved. Sources credited by name. One RESULT line at the end.
- Context from the neighbouring rows (1069 to 1075, read in FINISH.md only): row 1072's RESULT says BR-2 (wounded) and BR-3 (blocked-stronger) survive; Lemma MON-T, Corollary NO-MON, Remark RP-ANI, Lemma CONT, Lemma MON-L-cov FALSE and Proposition CA-FAIL are marked PROVED there and are under check by rows 1074 and 1075.


### Step 2 (row 1072 file and row 1073 reading, read in full). DONE.

Read in full: `library/gap-bridge-exercise-opus.md` (506 lines) and `library/prior/gap-bridge-read-luna.md` (71 lines).

What row 1072 (Claude Opus 5.5 high, unchecked at the time of reading) gives. Its marks are its own; I take them as claims under check by rows 1074 and 1075.

- Model. W(beta_L, beta_M, beta_T) on Z^2 x Z^2, points (u, x). Type L = (0,1) planes, T = (2,3) planes, M = mixed. Face beta_L = infinity. Anchor (infinity, beta_M, 0) = product of 2D O(4) sheets. Region R_eps = { beta_T X^2 <= eps, beta_L >= X^2/eps }, X a whole-sheet mixing length. Seed (S): clustering in R_eps, OPEN (first line (MIX)).
- Targets. T_win: clustering of every limit state of W(beta, beta, beta) for beta in [2.3, 2.6]. T_cont: a gapped continuum limit. The lane's consumer needs (SEED) at each beta of the window with a carry (`parts/gap.md` L24-26, as cited there).
- Its statements: Remark RP-ANI (RP at every anisotropic point, all four axes). Lemma MON-T (mixed-plaquette covariance across one transverse step is c_2 beta_T^2 + O(beta_T^3), c_2 >= 0, > 0 off a discrete set). Corollary NO-MON (no coordinatewise monotone bridge from R_eps). Lemma CONT (a path argument is open-and-closed). Proposition CA-FAIL (uniform-in-boundary mixing fails at every window coupling, by a pinned slab = 3D O(4) with long-range order; given Frohlich-Simon-Spencer). Lemma MON-L-cov FALSE (covariance form of a descent in beta_L is false since Var(x_p) = 0 on the face). Lemma LIN-perp (ARGUED: transverse rate is infinite at beta_T = 0). U(1)-range correction: for window-only bridges the U(1) test binds at belief grade only (theorem grade needs Villain beta >= 2^14).
- Its ranking of assumptions (highest first): C-1 (the bridge is a path in the Wilson coupling space); C-3 (clustering is the quantity to transport); C-2 (the anchor is the start); A2 (the window is the endpoint; fixed by the consumer's carry; owner decision); E-2 (no transition separates R_eps from the window).
- Its routes: BR-0 endpoint (dead, target-equivalent given (S)); BR-1 coordinatewise monotone (dead by NO-MON); BR-2 face first then descent in beta_L (wounded; open (FACE-SG) on the face path and (MON-L) in rate form); BR-3 continuity carry (blocked-stronger; open (LIN-path), the anisotropic form of row 878 F5's missing linear law); BR-4 complete analyticity (dead in uniform form by CA-FAIL); BR-5 expansion region (blocked-stronger); BR-6 reverse transverse blocking (blocked-stronger); BR-7 finite transverse torus (blocked-equivalent in the full model; face part merges into BR-2); BR-8 Tomboulis-Kanazawa decimation (row 1025, not redone); BR-9 path from (beta, beta, 0) (dead for now).
- Its section 6a: 18 set-aside methods (endpoint bridge; soft bridge; coupling monotonicity; transverse blocking flow; the 2D theorems alone; trajectory in R_eps; V1; Durhuus-Frohlich; chessboard; method 27; continuity method m5; continuity in a compact size; Tomboulis-Kanazawa; Migdal-Kadanoff; Lee-Yang B9; V4; route RC; (NOCRIT) differential form).
- Its blockage sentence (6b): every carry on file is either stated at its endpoint, or uses a uniformity that is blind or false, and no carry reads the dimension at order-one coupling.
- What it leaves open and where it points: C-3 names three dimension-reading quantities (running coupling, centre-vortex free energy, a finite-box mixing inequality) but its routes BR-0 to BR-9 all carry clustering or a gap. C-1 names larger action spaces (B1: heat kernel; fundamental plus adjoint; Bhanot-Creutz line) but no route uses one. A2 is passed to the owner. No route changes the carried quantity, the action space or the endpoint. That is the room row 1076 asks me to search.

What row 1073 (gpt-6-luna high, reading only) gives.

- Fradkin and Shenker 1979 (open SLAC preprint, read): for fixed-length fundamental Higgs, a region of the (beta, K) plane of analyticity of the free energy and Green functions joining Higgs-like and confinement-like regimes, with local exponential clustering inside the expansion's convergence region. For continuous groups the region narrows as K grows. Covers U(1) too. Not pure Yang-Mills.
- Dobrushin and Shlosman 1987 (read): finite-range, finite-spin setup; uniform over volumes and boundary conditions.
- Martinelli, Olivieri and Schonmann 1994: 2D discrete spins, weak mixing implies strong mixing on squares.
- Ginibre (via Chevyrev and Garban): loop monotonicity in plaquette couplings; loops only, not gaps. Luna's two sentences on the group range are in tension; row 1072 does not take it as an SU(2) inequality.
- Tomboulis, Ukawa and Windey 1981 (abstract): loop inequalities for Z_2 and U(N).
- Ikeda and Kondo 2021: centre-group comparison for double-winding loops.
- Sharpness (Aizenman-Barsky; Aizenman-Barsky-Fernandez; Duminil-Copin with Tassion and Raoufi): percolation, scalar ferromagnets, FK.
- No rigorous dimensional-crossover theorem found. Seiler's notes not read.
- RESULT: no theorem found that carries a uniform gap along a coupling path from the anchor to isotropic 4D SU(2).

### Step 3 (checks 1074 and 1075; `parts/gap.md`; row 1070 sections 6 and 9). DONE for what is present.

- Check 1074 (gpt-6-astra, cross-provider): ABSENT. `git fetch -q origin` run twice (before and after the reading); `origin/claude/ym4d-hard-route` is at 5113576a3 and does not hold `library/gap-bridge-exercise-check-astra.md`. Nothing merged or pulled.
- Check 1075 (Claude Opus 5.5 max, same provider): IN PROGRESS. The local file holds its plan and step 1 only (3263 bytes). It has no verdict yet. I do not touch it. I look again before the kill step and before the RESULT line.
- So every statement of row 1072 is used below at the grade "stated by row 1072, unchecked". Where a vector rests on one of them, I say so.
- `parts/gap.md` read in full (265 lines), only to avoid redoing work. What matters here: the wall (W) and its forms (PHYS-SEED), (SEED) at each beta of the window with a carry; rule W2 with the kinds (K-one) and (K-flow); the test table (U(1), free photon, product with a massless factor = Lemma PT, frozen Z_2, Q_8, 2T, w_p with Proposition V, the K7 line, Theorem D2 with Lemma SUB, Lemma SHEET); the route registry RA to RG and LC; rows 1016 (Lemma CEN+), 1013 (Lemma WN), 1018 (the short step in three forms, (T-vor) with Lemma PAR), 1025 (Tomboulis-Kanazawa, (TB)_n, Lemma FAC), 1052 (Lemma FLUX-W, target T_JW-lat), 1053 (V1 to V5), 1066 (V2), 1068 (V4).
- Row 1070 sections 6 and 9 read. The points I must respect: given (S), (BR-iso)_beta is equivalent to C_beta; T_JW-lat needs a common rate across cutoffs and a total observable class; a torus route needs the all-flux seed and its carry; a verified uniform hypothesis along a path may be group-blind in form if it fails for U(1); loop monotonicity gives an upper bound on the tension at the stronger coupling, the wrong direction; no RG map is given for transverse blocking.

### Step 4 (task 1: is there a new vector behind each assumption, route and method). DONE.

Writer: Anthropic, Claude Fable 5.2, effort max, laptop subagent of the lead session. One agent. No subagent. Nothing here is checked by another model.

#### 4.0 What was searched before any idea was named

Scope of every search: `library/` (all files, `prior/` included), `parts/`, `FINISH.md`, `GOAL.md`, by `grep -rliE` and `grep -rniE`. `library/open-core.md` is about the ultraviolet parts (its headings C_M to C_V); it has no line on the gap bridge. Open PR branches were not searched, so the strongest mark below is "not found in the lane folder".

| Idea searched | Pattern | Result |
|---|---|---|
| carry by analyticity, two constants | Lebowitz, Penrose, two-constant, harmonic measure, Harnack, subharmonic, zero-free | **On file as Route Z**: rows 670, 677, 680, 681, 683, 685 (`gap-zero-transport.md` Theorems LP, Z, ZB; `gap-zf-box-x.md`; `gap-zf-box-s.md`; `gap-skeleton-final.md` nodes Z1 to Z7). Crux Z6, (ZF_B-x), OPEN. |
| diamagnetic bound, loop gas for S^3 spins in SO(4) backgrounds | diamagnetic, Kato, loop gas | **On file**: Proposition LG of row 1016 (`gap-global-reform-max.md` L331), verdict "free energies only"; the nonlinear form is OPEN since row 834 (`gap-brainstorm-max.md` L181, L277, L688). |
| fundamental Higgs field, Fradkin and Shenker path | Fradkin, fundamental Higgs, unitary gauge | **On file**: B9 of row 669, idea 33 of row 859, I10 of row 1004 (`gap-outside-box-max.md` L146, L191), `gap-thermpin-opus.md` L48, L113; Lemmas LYP, LYP2. |
| mixed fundamental-adjoint action | Bhanot, fundamental.adjoint, beta_A | **On file as tests**: K7 line and end point (`parts/gap.md` test table), Identity MIX, Lemma GG (row 1004 I11). |
| product of two-dimensional Yang-Mills planes (beta_M = 0) | 2D Yang-Mills, beta_M = 0 | **On file**: idea 23 of `gap-brainstorm2-max.md` L173, L228 ("two exact planes ... a toy"). |
| thin twisted torus, continuity in the geometry | Tanizaki, Unsal, adiabatic, twist eater | **On file**: row 842 (Theorem S1), ideas 31, 36 and G7 of row 859, I5 and I6 of row 1004. |
| Hamiltonian with Gauss law along a path; Hellmann-Feynman | frustration-free, Feynman-Hellmann | **On file** for the isotropic axis: I14 of row 1004; item 46 of `gap-brainstorm-max.md` L445; exercise 2 F5 (row 878). |
| linear potential between sheet quanta | linear potential, Coulomb energy | **On file as physics**: Orland 2007, abstract read by row 1053 (`gap-wall-vectors-max.md` L314). The lattice operator form was not found. |
| fifth direction, layers as a path, quiver | fifth direction, deconstruct, quiver | Not found as a path (row 1053 L309 records 0 hits for "deconstruct/quiver"; the layer papers of rows 1067 and 1073 are tests). |
| Renyi or mutual-information quantity as the thing carried | Renyi, mutual information | Not found as a bridge quantity. Chi-square information is on file in `gap-compress-check-astra.md` L169; Renyi divergence in `gap-ladder-max.md` L135. |
| partial freezing; couplings on one sublattice | checkerboard, sublattice, bipartite, site-dependent | Not found (the hits are heat-bath sweeps and chessboard norms). Nearest: V3 of row 1053 (frozen two-skeleton arrays) and its remark "why more freezing does not help". |
| exchange of the two pairs of directions | swap, exchange, self-dual | Not found as a statement about the bridge (row 1053 6.8 uses the symmetry once, for the doubly flat corner). |

The reading of the posted O(4) proof that I use below is row 1009's (`library/prior/gap-o4-pinned-cell-read-opus.md`, read from the primary PDF by that row; reading only, unchecked). I did not read OpenAI's paper. What that row reports: the stiffness induction is uniform over pins, signed couplings with modulus at most b, and fixed twists on one side; (3.61) and (3.62) give decay of charged quantities in that class; from 3.11 on the proof uses "the untwisted zero-field ferromagnet" and says "This restriction is essential" (association and a two-replica Ginibre step). So the posted theorem gives full mixing for untwisted ferromagnetic sheets only.

#### 4.1 The five assumptions that row 1072 ranks highest

| Assumption | Is a new vector behind it? | Vector |
|---|---|---|
| C-1, the bridge is a path in the Wilson coupling space | Partly. Extra fields and other actions are on file (Higgs, mixed action, heat kernel, geometry). Two paths are not on file: couplings that depend on the transverse site or plaquette, and a fifth direction of locked layers. | VB-11 (checkerboard couplings, not found in the lane folder); VB-10 (fifth direction, not found); VB-8, VB-9, VB-12, VB-13 (found) |
| C-3, clustering is the quantity to transport | The row's list is walked in 4.4. Every candidate is on file, or has no consumer, or renames clustering. One exact form is not on file: the longitudinal coupling as an electric energy. | VB-1 to VB-7 |
| C-2, the anchor is the right start | Row 1072 weighs strong coupling against the anchor. A third start is on file as a toy (the plane beta_M = 0). I add what each start reads: R_eps reads the group and is blind to the dimension; the plane beta_M = 0 reads the split 2 + 2 and is blind to the group. No start reads both. | VB-12 (found; reading added); VB-16 (reading) |
| A2, the endpoint is the window | Row 978 (R3) says the consumer reads only the tail of the cutoffs, and that its carry is (NOCRIT), open. So three other endpoints exist on paper: the tail, a coupling below the window, an anisotropic endpoint with an anisotropic carry. All three are on file in substance. | VB-14, VB-15 (found) |
| E-2, no transition separates R_eps from the window | No proof vector. A transition surface would show as a zero of the gap in Lemma KIN's family or as Fisher zeros in Route Z's sense. A GUIDE run could look for it; none was made (4^4 to 8^4 boxes decide nothing about a surface). | none |

#### 4.2 The routes BR-0 to BR-9

| Route (row 1072) | New vector behind it? |
|---|---|
| BR-0 endpoint bridge | No. Changing the endpoint is VB-14 and VB-15. |
| BR-1 coordinatewise monotone comparison | Its reopen condition asks for "an inequality comparing non-ordered points". Walked as VB-7; one exact inequality of that kind exists for free energies (VB-4, from the exchange of the two pairs of directions). None for truncated correlations. |
| BR-2 face first, then descent in beta_L | Yes, two. (a) The descent has an exact operator form: the longitudinal coupling is an electric energy of partial colour charges (VB-3, Lemma KIN). (b) Both legs have exact two-dimensional first cases with finitely many fields, reached by couplings on one sublattice (VB-11). Also noted: in three dimensions (split 2 + 1) there is no transverse plaquette, so the bridge is the descent alone (remark in step 6). |
| BR-3 continuity carry, (LIN-path) | The complex form of a volume-free law is Route Z (VB-1, found). Lemma KIN gives the anisotropic Hellmann-Feynman identity for the beta_L leg (VB-3). No new mechanism for the decreasing leg. |
| BR-4 complete analyticity | No. Constant-coupling zero-freeness is Route Z (VB-1). |
| BR-5 expansion region | A second expansion region is on file: beta_M small at any beta_L, beta_T (VB-12). It does not reach the window. |
| BR-6 reverse transverse blocking | No. The anisotropic-carry endpoint (VB-15) is the same statement at the consumer. |
| BR-7 finite transverse torus | The checkerboard family (VB-11) gives finite-field two-dimensional models on the infinite transverse lattice, with no uniformity in a torus size. That removes BR-7's renaming for the first test, not for the route. |
| BR-8 decimation (Tomboulis, Kanazawa) | No. Flux quantities are VB-2 (found: rows 1018, 1025). |
| BR-9 path from (beta, beta, 0) | The start (beta, beta, 0) is the end of the descent at beta_T = 0 (VB-3 and VB-11 act there). Step 6 (Remark FLAT) argues at the Gaussian level that the gap there is not expected to be of order one, so BR-9's second leg would carry the rise of the gap (belief). |

#### 4.3 The eighteen set-aside methods of section 6a of row 1072

| # | Method | New vector behind it? |
|---|---|---|
| 1 | endpoint bridge | no (VB-14, VB-15 found) |
| 2 | soft bridge | no; a verified uniform hypothesis is Route Z's (ZF) (VB-1) or (LIN-path) |
| 3 | coupling monotonicity | VB-7; VB-4 for free energies; Lemma KIN's operator order (VB-3) is the one monotone statement found, for the transfer operator, not for correlations |
| 4 | transverse blocking flow | no |
| 5 | the 2D theorems alone | VB-11 asks what they give for one-sided backgrounds (charged decay only, by row 1009's reading) |
| 6 | trajectory inside R_eps | no (VB-14) |
| 7 | V1, (FACE-SG) then (BR-L) | VB-3 and VB-11 |
| 8 | Durhuus-Frohlich layers | no; row 834's open nonlinear diamagnetic inequality is the same wall |
| 9 | chessboard in the transverse directions | no |
| 10 | the beta_t path (method 27) | no; VB-12 is its 2 + 2 relative with a trivial start |
| 11 | continuity method m5 | VB-1 (found) |
| 12 | continuity in a compact size | VB-13 (found) |
| 13 | Tomboulis-Kanazawa | VB-2 (found) |
| 14 | Migdal-Kadanoff | no |
| 15 | Lee-Yang in a link field | VB-8 (found); the kinetic coupling gives a second complex variable with a domination property (VB-1 note), same crux |
| 16 | V4, infrared measure first | no (VB-15) |
| 17 | route RC, one-scale number | no |
| 18 | (NOCRIT) differential form | VB-3 gives its beta_L form with one sign-definite ingredient (an electric energy), still a renaming |

#### 4.4 The row's three questions, answered by list

**What is carried (not clustering).** A free energy: VB-4 (exchange symmetry and convexity; proved; no consumer). A flux-sector ratio: VB-2 (found; consumer is the flux clause of (W) only). A transfer-matrix spectral datum: VB-1 (dominance of one eigenvalue in a complex neighbourhood, Route Z, found), VB-3 (electric energy of the excitation), VB-6 (convexity of log lambda_0 and of log lambda_0 lambda_1 in the kinetic time; proved; no sign for the gap). An entropy or Renyi quantity: VB-5 (renames clustering). A correlation inequality between non-ordered points: VB-7 (none found for truncated correlations).

**What the path is (not in the Wilson coupling space).** Extra fields: VB-8 (fundamental Higgs, found). Mixed action: VB-9 (found as tests; no anchor). A fifth direction: VB-10 (not found; fails). Couplings on a sublattice: VB-11 (not found; survives as a test-bed). Geometry: VB-13 (found).

**What the endpoint is.** VB-14 (the tail, found), VB-15 (below the window, or anisotropic with an anisotropic carry; found).

Seventeen vectors are named here: VB-1 to VB-17, with VB-16 a reading and VB-17 the empty entry for E-2. Step 5 states each and applies the kill tests; it adds VB-18 (three dimensions first).

### Step 3, addendum (both checks of row 1072 are now present; read before the kill step)

- Check 1074 (gpt-6-astra xhigh, cross-provider): now on `origin/claude/ym4d-hard-route`. Read by `git show` into /tmp/astra1074.md (440 lines; sections 2, 3, 5 to 8 and the RESULT read; nothing merged). Verdicts I use: Lemma MON-T, Corollary NO-MON, Lemma CONT and Lemma MON-L-cov FALSE HOLD. Remark RP-ANI holds as positivity of the transfer operators; its consequence "inverse spectral gaps at every point of every path" is corrected (positivity alone does not identify an infinite-volume correlation length with a torus gap; at a zero coupling the transfer operator can have a kernel). Proposition CA-FAIL HOLDS AFTER CORRECTION (full-specification strong mixing fails, given Frohlich, Simon and Spencer; threshold 2 I_3 below 2 by a hand bound). **The (MON-L) class argument FAILS as a refutation: (MON-L) as written is the endpoint inequality m(beta_L, beta, beta) >= m(infinity, beta, beta); a derivative-sign law is a stronger sufficient input.** Lemma LIN-perp FAILS at L428. The strength claims on BR-6 and BR-7 FAIL (no observable recovery; "by another name" not shown). BR-9: "no supplied start estimate", not a refutation.
- Check 1075 (Claude Opus 5.5 max, same provider): complete locally (703 lines; verdict table and RESULT read). No item FAILS there. Its corrections that I use: NO-MON (ii) needs X >= 1 stated; CA-FAIL is Lemma SLAB of row 1013 made explicit for the window, and the face escapes the device for u-boundary data only; a 2 + 2 method 27 also needs a carry in beta_L; BR-2 is stronger than the target, wounded at its face step and blocked at (MON-L); BR-3's first open statement in chain order is the beta_L leg at beta_T = 0.
- Where the two checks differ (LIN-perp; the (MON-L) class argument; BR-6 and BR-7) I follow the cross-provider check and say so at the place of use.

### Step 5 (tasks 2 and 3: each vector stated, then killed fast). DONE.

Tests, in the valid form of row 1072 6c as corrected by checks 1074 and 1075. A model refutes a claim only if the claim's hypothesis holds there and its conclusion fails. T0: renaming (the vector's open statement is an open statement on file, or contains the target; the equivalence is written). T1: compact U(1) (theorem grade only for statements whose conclusion includes a Villain point with beta at least 2^14; belief grade in the window). T2: frozen Q_8 and 2T (they bind torus forms with flux sectors). T3: Pin(2), GUIDE. T4: five dimensions, split 2 + 3, belief. T5: Lemma PT (product with a massless factor). T6: Proposition NP. T7: Theorem D2 and Lemma SHEET (suprema over pins, tilts or coupling fields). T8: Lemma CEN+ and Lemma WN. T9: Proposition CA-FAIL (full-specification strong mixing is false in the window). T10: Corollary NO-MON. T11: the spec check, read as row 1072 6c reads `parts/gap.md` L242-244: S1 non-abelian structure, S2 a rate, S3 the whole state space, S4 constant couplings or typical fields. A pass is no support.

Consumer chain common to all: a bridge gives C_beta (clustering of the isotropic limit states at one beta of the window). The lane's use of C_beta needs more: a common rate across cutoffs for T_JW-lat (check 1070 section 6), and row 978 says the carry to finer cutoffs is (NOCRIT), open. I do not repeat this under each vector.

#### VB-1. Zero transport along the anisotropic path (carried: dominance of one eigenvalue in a complex neighbourhood)

- Statement (ZF-path). Let P(z) be the path with its parameter made complex. There is a complex neighbourhood D of the parameter interval, the same for every box with free walls, on which the continued transfer operator has one simple eigenvalue of strictly largest modulus.
- Consumer. Theorem ZB of row 670 (two constants; repaired by a Harnack chain in check 681) turns a rate on a small disc into a rate at the endpoint, free of the box size. The disc must sit at the start: here the seed (S) in complex form, which is not on file.
- What it changes. The start, from the strong-coupling disc to the anchor. The crux does not change: (ZF-path) is node Z6 of `gap-skeleton-final.md` with the Wilson coupling replaced by the path parameter.
- Source. Lebowitz and Penrose; Nevanlinna; Denbleyker, Du, Liu, Meurice and Zou (zeros for SU(2), as cited by row 670); rows 670 to 685 of this lane.
- One exact fact that is special to the anisotropic family (PROVED in step 6, Corollary KIN-D): in the kinetic variable w = e^(-t/4) of a heat-kernel longitudinal action, T(w) = sum over k of w^k A_k with A_k >= 0, so T is analytic in the unit disc and |<f, T(w) g>| <= <f, T(|w|) f>^(1/2) <g, T(|w|) g>^(1/2). It gives bounds, not dominance.
- Kill. T0: **FAILS as a new vector.** Found on file; the open statement is Z6 in another variable. T1: the hypothesis must fail for U(1) on a path class that reaches Villain beta at least 2^14 (zeros reach the real axis); consistent. Cheapest further test: none needed.

#### VB-2. A flux-sector ratio carried from the anchor

- Statement (FLUX-M-path). Along the path, the ratio Z_tw/Z for a centre twist on a co-closed set of mixed plaquettes tends to 1 exponentially in the box side. Start value (ARGUED from Lemma ANCH): at the anchor the twist is an antiperiodic boundary condition on one column of sheets, so the ratio is a power of the O(4) ratio Z_ap/Z_per.
- Consumer. The flux clause of (W) (Lemma FLUX-W, one way), and an area law by an inequality of Tomboulis and Yaffe type (recalled). No theorem on file, and none known to me, turns a flux statement into C_beta.
- Source. 't Hooft; Tomboulis and Yaffe; Mack and Petkova; rows 1018 ((T-vor)), 1025 ((TB)_n, Lemma FAC), 1053 ((FACE-TW)).
- Kill. Consumer test: **FAILS for the bridge question** (no consumer in a chain to clustering). Found on file. T2 would bind it (frozen groups have degenerate flux sectors), which is the right behaviour, not a refutation.

#### VB-3. The longitudinal coupling as an electric energy (carried: the electric energy of the lowest excitation)

- Statement. Lemma KIN (PROVED in step 6): on a slice with free ends in direction 1, the transfer operator in direction 0, on gauge-invariant functions, is unitarily equivalent to S* D(beta_L) S on G-invariant functions of the transverse links. S* S is the face operator. D(beta_L) is the product over the cuts c = (k, x) of lambda_j(beta_L), where j labels the Casimir of the total colour charge, for the group at x, of the slice sites beyond the cut. Open statement (FLUX-EXC): in the heat-kernel form D = e^(-tN), the normalized first excited vector of e^(-tN/2) S S* e^(-tN/2) has <N> at least that of the ground vector, for all t > 0 and all boxes.
- Consumer. By the Hellmann-Feynman identity (step 6, KIN-5), (FLUX-EXC) holds for all t if and only if the gap m(t) is non-decreasing in t. That gives (MON-L) of BR-2. With (FACE-SG) it gives C_beta.
- What it changes. BR-2's second obligation gets an exact operator form with one sign-definite ingredient: an energy that is a sum of Casimirs. It also names the frustration-free case exactly (KIN-3) and proves that the face is not in it when beta_M > 0 (KIN-4).
- Source. Kogut and Susskind; Luescher; Osterwalder and Seiler (transfer operator); the elimination of a gauge field in one space dimension by Gauss's law (standard); Orland 2007 (linear potential between sheet particles; abstract read by row 1053). The lattice form was not found in the lane folder.
- Kill. T0: **FAILS as a reduction.** (FLUX-EXC) is the derivative-sign law. By check 1074 it is stronger than (MON-L) as written, and by KIN-5 it is exactly the monotone form of (MON-L). So it renames that form. T1: Lemma KIN holds for every compact group, so it is blind; (FACE-SG) is false for U(1) at large beta_M, so nothing is refuted and nothing is gained. T5, T11 (S3): the statement is on the whole state space. Class test (step 6, KIN-6): operators S* e^(-tN) S with N >= 0 exist whose gap decreases, so a proof must use the form of N and of the face vector, not the structure alone. **T2 (added after step 6.4): for frozen Q_8 on a small box (MON-L) and (FLUX-EXC) are false (Example KIN-7, PROVED in a limit; GUIDE values in the window), while SU(2) and U(1) show no dip on the same box (GUIDE). So a proof must use that the group is continuous.**
- Verdict: Lemma KIN and its corollaries PROVED; (FLUX-EXC) OPEN; the vector does not pass the wall. It survives only as a tool for a proof row on (MON-L).

#### VB-4. A free-energy inequality between non-ordered points

- Statement (Lemma SWAP, PROVED). Let Lambda be a box with four equal sides, free or periodic, and p(beta_L, beta_M, beta_T) = |Lambda|^(-1) log Z_Lambda. Then p is convex, and p(beta_L, beta_M, beta_T) = p(beta_T, beta_M, beta_L). So for abs(s) <= beta: p(beta, beta_M, beta) <= p(beta + s, beta_M, beta - s). The same holds for every limit of p along such boxes. Proof. log Z is convex in the couplings (its Hessian is a covariance matrix). The exchange of the pair of directions (0, 1) with the pair (2, 3) maps a box with equal sides to itself and exchanges the types L and T. A convex function that is symmetric about the midpoint of a segment is smallest there. QED
- Consumer. None. It compares the isotropic point with the points (2 beta, beta_M, 0) and (0, beta_M, 2 beta), which are not ordered against it, but it is a statement about free energies only (the verdict of row 1016 4.6 on the diamagnetic bound applies).
- Kill. Consumer test: **FAILS.** The gap is also symmetric on that segment, but it is a difference of two convex functions (VB-6), so the symmetry gives no bound for it.

#### VB-5. An entropy or Renyi quantity

- Statement. For regions A and B at distance r, the chi-square information I_2(A : B) = log(1 + chi^2(mu_AB | mu_A x mu_B)) is at most C(A, B) e^(-m r). In replica form 1 + chi^2 is a ratio of partition functions of two copies glued on A and on B.
- Kill. T0: **FAILS (renaming).** chi^2 is the sum of the squared singular values of the conditional expectation operator from L^2_0(mu_B) to L^2_0(mu_A), so it is at least the square of the largest normalized covariance between a function on A and a function on B. Hence decay of I_2 is clustering, uniform over L^2 observables: at least as strong as C_beta. The glued system has coupling 2 beta on the glued set, so it is outside the constant-coupling class (S4). Chi-square information is on file (`gap-compress-check-astra.md` L169); as a bridge quantity it adds nothing.

#### VB-6. Convexity of spectral data in the kinetic time

- Statement (Lemma KIN-CVX, PROVED in step 6). With the heat-kernel longitudinal action, log lambda_0(t) and log(lambda_0 lambda_1)(t) are convex and non-increasing in t.
- Kill. The gap is m = 2 log lambda_0 - log(lambda_0 lambda_1), a difference of two convex functions. No sign follows. **FAILS** (no consumer). It is recorded so that nobody tries it again.

#### VB-7. A correlation inequality between non-ordered points

- Candidates and their scope. Ginibre: abelian groups, loops, the Griffiths direction (rows 1066, 1069; luna row 1073). The inequalities for rotators with at most four components (Dunlop; Kunz, Pfister and Vuillermot; recalled, not read): spin models with ferromagnetic pair couplings; a mixed plaquette is a quartic form with both signs in the link components, so they do not apply to the gauge model. The association and two-replica steps of the posted O(4) proof: by row 1009's reading they are used for "the untwisted zero-field ferromagnet" and "this restriction is essential". The diamagnetic bound (Proposition LG): free energies. Chessboard estimates: one coupling point. Lemma SWAP: free energies.
- Kill. **FAILS: no candidate.** Scope: the families listed. I found no inequality for truncated correlations of SU(2) gauge-invariant observables between two points of the coupling space, ordered or not. Corollary NO-MON (T10) stands as checked.

#### VB-8. Fundamental Higgs field at the window coupling (Fradkin and Shenker)

- Found: B9 of row 669, idea 33 of row 859, I10 of row 1004, `gap-thermpin-opus.md` (the pin path is the line kappa = h at fixed beta). Not redone. In bridge terms: the start (large hopping at fixed beta) is group-blind, the carry is a continuation in kappa with no mechanism, and the half-plane Lee-Yang form is false (Lemmas LYP, LYP2). **FAILS; found.**

#### VB-9. Mixed fundamental-adjoint action

- Statement. Start at adjoint coupling infinity, where the model is frozen Z_2 at the fundamental coupling beta (local observables cluster by Peierls for beta above 2.191, `parts/gap.md` test table), and lower the adjoint coupling to 0 at fixed beta in the window.
- Kill. The start reads only the centre: by the lane's barrier remark (row 1018), the central-twist identities hold verbatim in frozen Z_2, so the start carries no SU(2) data (S1 fails at the start). The flux sectors are degenerate at the start (T2), so the start is not a torus seed. The carry is (NOCRIT) in the adjoint coupling, with the K7 line nearby (belief). **FAILS (ARGUED).** Found as tests; not found as a path.

#### VB-10. A fifth direction: locked layers

- Statement. N copies of the four-dimensional link field, each with Wilson coupling b = beta/N, with weight exp(beta_5 sum over links and adjacent copies of (1/2) tr(U^(s) (U^(s+1))^(-1))). This is the five-dimensional anisotropic Wilson model on Z^4 x {1..N} with free ends, in the gauge where the fifth links are 1. Lemma LOCK (PROVED): on a finite box, as beta_5 tends to infinity the law of one copy tends to Wilson at coupling N b = beta; at beta_5 = 0 the copies are independent at coupling b. Proof: the normalized link weight is an approximate identity, so all copies become equal and the plaquette weights multiply. QED. Open statement (LAYER): clustering with one rate for all beta_5 in [0, infinity], at b = beta/N below the strong-coupling radius.
- Consumer. C_beta, at beta_5 = infinity.
- Kill. T0: (LAYER) contains C_beta as its endpoint, so it is stronger than the target, like BR-3. T1: for U(1) the same family joins strong coupling to coupling N b; a blind proof is refuted when N b reaches the Villain range. The start is strong coupling, which reads neither the group nor the dimension. No selective step is named. **FAILS as a reduction (ARGUED).** Not found in the lane folder as a path; it is BR-3 with a different one-parameter family.

#### VB-11. Couplings on a sublattice: the checkerboard family (path outside the Wilson coupling space)

- Statement. Let beta_L depend on the transverse site and beta_T on the transverse plaquette. Lemma CB-L and Lemma CB-T (PROVED in step 6): (i) at beta_T = 0, with beta_L = infinity on the even transverse sites, the gauge-invariant measure is a product over the odd sites of copies of GH2_4(beta_L, beta_M): a two-dimensional SU(2) lattice gauge theory with four fundamental Higgs fields of fixed length; (ii) on the face, with beta_T on the black plaquettes of a checkerboard colouring only, the measure is a product over black plaquettes of copies of P4(beta_M, beta_T): four O(4) sheets with the on-site potential beta_T (1/2) tr(Phi_1 Phi_2 Phi_3^(-1) Phi_4^(-1)). Open statements: (GH2-MIX), exponential mixing of GH2_4 on gauge-invariant local observables for beta_M in the window and every beta_L in (0, infinity]; (P4-MIX), the same for P4 on G-covariant local observables for beta_T in [0, beta].
- Consumer. They are first cases of BR-2's two obligations: (P4-MIX) is (FACE-SG) with half of the transverse plaquettes, and (GH2-MIX) is the descent in beta_L at beta_T = 0 on half of the transverse sites. To reach C_beta the other sublattice must be turned on, and that is again a carry. So VB-11 gives start data and test models, not a bridge.
- What it changes. (a) BR-2's first tests become exact two-dimensional models with finitely many fields per site on the infinite transverse lattice; no uniformity in a torus size is needed (compare BR-7 and work item 2 of row 1072). (b) By row 1009's reading, the posted O(4) proof covers fixed one-sided twists in its charged estimates (3.61) and (3.62); in GH2 each Higgs field, given the gauge field, is such a sheet. So decay of every correlation that is charged under a far-end rigid group follows from the posted estimates (Proposition CB-CH, step 6, ARGUED). What is left is the singlet sector, where the posted proof uses association for untwisted ferromagnets. (c) At beta_L = 0 on the odd sites the model is explicit (Lemma GH2-0, step 6): a nearest-neighbour model on SU(2)\SU(2)^n with bond weight (2/(beta_M s)) I_1(beta_M s), s^2 = n + 2 sum over pairs of rho_ac(u) . rho_ac(u'); for n = 2 it is an O(4) ferromagnet with a weight that is a power series in rho . rho' with non-negative coefficients.
- Source. Row 1053 (the face, Lemma FACE-LIM, Lemma RIG); Orland; Bardeen, Pearson and Rabinovici (transverse lattice); Fradkin and Shenker (fundamental Higgs fields screen); OpenAI's posted O(4) proof as read by row 1009.
- Kill. T7 (SHEET, D2): one fixed periodic coupling pattern, no supremum over fields or pins: pass. T9: no full-specification mixing is claimed: pass. T1: for U(1) both models are massless at large beta_M (step 6, Gaussian, ARGUED): n - 1 relative phases for GH2, three combinations for P4. So the statements are false for U(1) there, as they must be: pass as a constraint (S1 needed). T2, T3: for Q_8 and 2T the sheets order at large beta_M, so charged correlations do not decay: pass as a constraint; Pin(2) as U(1) (GUIDE). T4: both models exist verbatim in the split 2 + 3 (six Higgs fields; the plaquette model unchanged). So they are blind to the dimension and cannot hold the bridge's dimension reading; that is consistent with their role as start data. T5: a product with a massless factor fails (S3 needed). T0: (P4-MIX) and (GH2-MIX) are two-dimensional statements with finitely many fields; they are not C_beta and not (FACE-SG); (FACE-SG-T) of row 1072 is the nearest statement on file.
- Verdict: **survives as a test-bed and as start data; as a bridge it has no carry, so it does not pass the wall.** Cheapest test that would kill its use: show that the posted argument's singlet step has no form without association (then (P4-MIX) and (GH2-MIX) are as far as (FACE-SG)).

#### VB-12. The plane beta_M = 0 as a start

- Found: idea 23 of `gap-brainstorm2-max.md` (a product of exactly solved two-dimensional Yang-Mills planes; expansion in the mixed coupling). Reading added here (ARGUED): this start is exact for every compact group, so it is group-blind; but it exists only in the split 2 + 2, because in 2 + 3 the transverse factor is three-dimensional Yang-Mills, whose gap is open. R_eps is the opposite: it reads the group (the sheet gap) and exists in every split 2 + d_perp. No start on file reads both.
- Kill. As a bridge its carry is (NOCRIT) in beta_M at fixed (beta, beta); T1 binds a blind carry. **FAILS as a reduction; found.**

#### VB-13. A path in the geometry (thin twisted torus)

- Found: row 842 (Theorem S1), ideas 31, 36 and G7 of row 859, I5 and I6 of row 1004, with credit to Tanizaki and Unsal there. Not redone. **Found.**

#### VB-14. The endpoint is the tail of the cutoffs, not the window

- Statement. A bridge to every isotropic beta above some beta_1, with a rate proportional to the lattice spacing a(beta), is T_JW-lat by row 978 (R3), with no carry.
- Kill. It is REN (2) of row 1066 and the misframing note of row 1072 7.1 in the tail form. T1 binds it at theorem grade, since the endpoints reach every large beta. It needs a family of paths with a physical rate; no mechanism. **FAILS as an easier form (it is stronger); found in substance.**

#### VB-15. Other endpoints

- A coupling below the window: on file (row 1072 A2; `gap-finishline-opus.md` L199: "No single bare beta_W finishes the proof"). An anisotropic endpoint with an anisotropic last step of the carry: this is BR-6 and (UNIV-aniso); check 1074 found that BR-6's strength claim lacks an observable-recovery step. **No vector.**

#### VB-16. Reading: where the dimension sits in the 2 + 2 split

- Statement (ARGUED; no proof obligation). Every link is a spin of a two-dimensional O(4) sheet. A transverse link Phi_l(u) is a sheet over the longitudinal plane. A longitudinal link U_b(x) is a sheet over the transverse plane. A mixed plaquette is one bond of a sheet of each family, twisted by the two neighbouring sheets of the other family. The L and T plaquettes are on-site potentials. Both families are two-dimensional only for d = 4 with the split 2 + 2. In 2 + 3 the longitudinal links form three-dimensional sheets, and that is where the slab device of Lemma SLAB and Proposition CA-FAIL finds order.
- Kill. It is not a route. Conditional laws that are two-dimensional do not give mixing of the joint law: the pinned slab is built from longitudinal sheets coupled through L plaquettes. **FAILS as a route.** Kept because it says which family a dimension-reading step must use. Adjacent on file: row 1053 L245 ("k = 2 is the only split where the group decides").

#### VB-17. E-2 (a transition between R_eps and the window)

- No vector. No statement found that excludes or builds a separating surface. Not run numerically.

#### VB-18. The bridge in three dimensions first (test-bed; added in step 5)

- Statement. In d = 3 with the split 2 + 1 there is no transverse plaquette. The family is (beta_L, beta_M). The face (infinity, beta_M) is the product of O(4) sheets on the links of Z, and its G-invariant local observables cluster, GIVEN the posted mixing bound for untwisted sheets (ARGUED: the measure is a product, and a G-invariant local observable is a local function of finitely many sheets). So in three dimensions the whole bridge is the descent: (MON-L)_3: m(beta_L, beta) >= c m(infinity, beta) for beta_L in [beta, infinity).
- Consumer. None for the four-dimensional target. It is the cheapest exact place to test a mechanism for the descent: (MON-L)_3 with the posted theorems would give a gap for three-dimensional lattice SU(2) at coupling beta.
- Kill. T1: three-dimensional compact U(1) is gapped at weak coupling (Goepfert and Mack, Villain form; recalled), and its face is massless at large beta_M (Frohlich and Spencer; recalled); so (MON-L)_3 is not refuted by U(1). No test on file refutes it. No mechanism. **OPEN; no consumer for the target; kept as a test-bed.** Orland's 2006 and 2007 papers are in this setting (row 1053, abstracts).

#### Kill summary

| Vector | Carried / path / endpoint | On file? | Verdict |
|---|---|---|---|
| VB-1 | zero-freeness on the anisotropic path | yes (Route Z) | FAILS as new; crux Z6 |
| VB-2 | flux-sector ratio | yes | FAILS at the consumer |
| VB-3 | electric energy, Lemma KIN | exact form not found | lemma PROVED; (FLUX-EXC) OPEN and a renaming of monotone (MON-L); false for frozen Q_8 on a small box (KIN-7); does not pass |
| VB-4 | free energy, Lemma SWAP | not found | PROVED; FAILS at the consumer |
| VB-5 | chi-square information | partly | FAILS (renaming) |
| VB-6 | convexity in the kinetic time | not found | PROVED; no sign for the gap; FAILS |
| VB-7 | inequality between non-ordered points | - | FAILS: no candidate |
| VB-8 | fundamental Higgs | yes | found; FAILS |
| VB-9 | mixed action as a path | tests only | FAILS (ARGUED) |
| VB-10 | fifth direction, locked layers | not found | FAILS as a reduction (ARGUED) |
| VB-11 | checkerboard couplings | not found | survives as test-bed and start data; no carry |
| VB-12 | plane beta_M = 0 | yes | found; FAILS as a reduction |
| VB-13 | geometry | yes | found |
| VB-14 | tail endpoint | in substance | FAILS as easier |
| VB-15 | other endpoints | yes | no vector |
| VB-16 | reading of the dimension | adjacent | not a route |
| VB-17 | E-2 | - | no vector |
| VB-18 | three dimensions first | setting on file (Orland) | OPEN test-bed; no consumer |

No vector passes the wall. Two leave work: VB-11 and VB-3. VB-18 is a test-bed for VB-3.

### Step 6 (tasks 4 and 5: ranking, then hand work on the top two). DONE.

#### 6.0 Ranking of what is left (task 4)

Ranked by what the item would change, divided by the cost to find out. No item passes the wall, so this ranks tools, not routes.

| Rank | Item | What it would change | Cost to find out | Why this rank |
|---|---|---|---|---|
| 1 | VB-11, checkerboard models GH2 and P4 | Decides whether BR-2's two obligations have a first case that the posted two-dimensional method can prove. A "no" at P4 kills BR-2 at its first step. | One reading-and-port row on the smallest model (GH2_2 at beta_L = 0, then P4). | Exact, small, and it uses the anchor's data in a model that is not a sheet. |
| 2 | VB-3, Lemma KIN and (FLUX-EXC) | Gives (MON-L) the form of one sign. | Small for the lemma (done below). A proof of the sign has no mechanism. | The lemma is proved; the open part is a renaming. |
| 3 | VB-18, three dimensions first | Tests any mechanism for the descent where the descent is the whole bridge. | A proof row with no consumer for the target. | Test-bed only. |

#### 6.1 Hand work on VB-3: Lemma KIN and its consequences

**Setting.** Slice Sigma = {1, ..., n} x Lambda_perp, n >= 2, Lambda_perp a finite rectangle of Z^2, free boundary. Slice links: a(k, x) in SU(2) from (k, x) to (k+1, x), 1 <= k <= n-1; Phi_mu(k, x) from (k, x) to (k, x + e_mu), mu = 2, 3. H = L^2 of all slice links with Haar measure. Slice gauge group: (g.a)(k, x) = g(k, x) a(k, x) g(k+1, x)^(-1), (g.Phi_mu)(k, x) = g(k, x) Phi_mu(k, x) g(k, x + e_mu)^(-1). For a real class function w >= 0 with integral 1 let K_w be convolution by w on one link, (K_w f)(a) = int w(V) f(V a) dV. K_a is the product of K_w over the a-links with w = w_L, proportional to exp(beta_L x) (Wilson) or the heat kernel at time t. K_Phi is the same over the Phi-links with w proportional to exp(beta_M x). V is minus the sum over the slice plaquettes of type (1, mu) of beta_M x_p, minus the sum over the slice plaquettes of type (2, 3) of beta_T x_p. The transfer operator in direction 0 is T = e^(-V/2) K_a K_Phi e^(-V/2) on the gauge-invariant subspace H^G. That T is the transfer operator of the anisotropic measure is the lane's (TM) (row 667) with one coupling per plaquette type (Remark RP-ANI of row 1072 as corrected by check 1074). I do not re-prove (TM).

Notation. G = SU(2)^(Lambda_perp) acts on the Phi variables by (g.Phi_mu)(k, x) = g(x) Phi_mu(k, x) g(x + e_mu)^(-1), the same g at every k. K = L^2(Phi)^G. For a cut c = (k, x), 1 <= k <= n-1, and W in SU(2), let rho_c(W) act on L^2(Phi) by the gauge rotation W at the sites (k', x) with k' > k and the identity at all other sites. Let J_c be its generators, C_c = J_c . J_c its Casimir, and P_c^j the projection on the part where C_c = j(j+1). V_f is V at a = 1: the face potential.

**Lemma KIN (PROVED).**
(a) The operators C_c commute with each other, with K_Phi and with G.
(b) R: H^G to K, (R f)(Phi) = f(1, Phi), is unitary.
(c) R T R^(-1) = S* D S, with S = K_Phi^(1/2) e^(-V_f/2) and D = product over the cuts c of M_c, M_c = sum over j of lambda_j P_c^j, lambda_j = (2j+1)^(-1) int w_L chi_j. For the Wilson weight lambda_j = I_(2j+1)(beta_L)/I_1(beta_L). For the heat kernel lambda_j = e^(-t j(j+1)) and D = e^(-tN), N = sum over c of C_c.
(d) S* S is the transfer operator of the face model M(beta_M, beta_T) on G-invariant functions. 0 <= D <= 1. D tends to 1 strongly as beta_L tends to infinity (as t tends to 0).

Proof. (a) Write J_(k', x) for the generators of the gauge rotation at one slice site. Generators at different sites commute. J_c is the sum of J_(k', x) over k' > k. For c' = (k'', x) with k'' > k: J_c = J_mid + J_c', J_mid the sum over k < k' <= k''. C_c' commutes with J_c' (Casimir) and with J_mid (other sites). So it commutes with J_c and with C_c. For cuts in different columns the sites differ. K_Phi convolves each link with a class function, so it commutes with left and right multiplications on each link, hence with every J. The generator of G at x is J_low + J_c (sites k' <= k and k' > k); C_c commutes with both.
(b) For a slice configuration put g_a(k, x) = a(1, x) a(2, x) ... a(k-1, x), g_a(1, x) = 1. Then g_a.a = 1. For f in H^G: f(a, Phi) = f(1, g_a.Phi). So f is fixed by R f, and R f is invariant under the gauge rotations that keep a = 1: the elements of G. The norm is kept: integrate over Phi first and use the invariance of Haar measure. R is onto: for h in K put f(a, Phi) = h(g_a.Phi). For a gauge rotation g one finds g_(g.a)(k, x) = g(1, x) g_a(k, x) g(k, x)^(-1), so g_(g.a).(g.Phi) = g(1, .).(g_a.Phi), and h is invariant under G.
(c) K_Phi and multiplication by a function of the plaquettes commute with R in the plain sense: (K_Phi f)(1, Phi) = (K_Phi R f)(Phi), and V = V_f at a = 1. For K_a: (K_a f)(1, Phi) = int prod w_L(V_l) f(V, Phi) dV = int prod w_L(V_l) h(g_V.Phi) dV, h = R f. In one column, g_V(k') = V_1 V_2 ... V_(k'-1), and h(g_V.Phi) = (rho_(n-1)(V_(n-1)) ... rho_1(V_1) h)(Phi): indeed (rho_2(V_2) rho_1(V_1) h)(Phi) = (rho_1(V_1) h)(w_2.Phi) = h(w_1 w_2.Phi), and w_1 w_2 = V_1 V_2 at the sites beyond the second cut. Integrating each V_l gives the product of M_c = int w_L(W) rho_c(W) dW. Since w_L is a real class function, M_c acts on the spin-j part of rho_c as lambda_j (Schur). The M_c commute by (a), and K_a commutes with K_Phi on H^G, so R T R^(-1) = e^(-V_f/2) K_Phi^(1/2) D K_Phi^(1/2) e^(-V_f/2). K_Phi is positive with eigenvalues that are products of I_(2j+1)(beta_M)/I_1(beta_M) > 0, so its square root exists.
(d) At D = 1 the operator is e^(-V_f/2) K_Phi e^(-V_f/2), the transfer operator of the weight of Lemma FACE-LIM. abs(chi_j) <= 2j+1 gives 0 < lambda_j <= 1. lambda_j tends to 1 for each j, and D is a function of the commuting C_c. QED

Lean form: Peter-Weyl on SU(2), Schur's lemma, change of variables under Haar measure, min-max.

**Corollary KIN-1 (operator order; PROVED, with one recalled fact for the Wilson weight).** R T(beta_L) R^(-1) <= S* S as quadratic forms on K. For the heat kernel, the family is non-increasing in t. For the Wilson weight it is non-decreasing in beta_L GIVEN that I_nu(b)/I_1(b) is non-decreasing in b for nu >= 1 (a known property of Bessel ratios; recalled, not proved here). T is compact and positive, so by min-max every ordered eigenvalue lambda_i(beta_L) is at most lambda_i(infinity).

**Corollary KIN-2 (the bound that this gives, and why it is not enough; PROVED).** m(beta_L) >= m(infinity) - [log lambda_0(infinity) - log lambda_0(beta_L)]. The bracket is the difference of two slice free energies. It is not bounded in the slice (ARGUED: it is a sum over the cuts of a positive local term). This is the volume factor of exercise 2 F5 (row 878) in the anisotropic family.

**Corollary KIN-3 (the frustration-free case; PROVED).** Let Omega be the top eigenvector of S* S (unique and strictly positive by Perron-Frobenius; G-invariant by uniqueness). If D S Omega = S Omega, then Omega is a top eigenvector of S* D S with the same eigenvalue, and m(beta_L) >= m(infinity). Proof. S* D S Omega = S* S Omega = lambda_0(infinity) Omega, and S* D S <= S* S, so lambda_0(beta_L) = lambda_0(infinity). lambda_1(beta_L) <= lambda_1(infinity) by KIN-1. QED

**Lemma KIN-4 (the face is not in that case when beta_M > 0; PROVED).** If beta_M > 0 and beta_L is finite (t > 0), then D S Omega is not S Omega. So lambda_0(beta_L) < lambda_0(infinity) strictly.
Proof. Put psi = S Omega and suppose D psi = psi. The M_c are commuting contractions, so norm(M_c psi) = norm(psi) for each c. lambda_j < 1 for j >= 1/2 (chi_j/(2j+1) < 1 off the identity), so P_c^j psi = 0 for j >= 1/2: psi is invariant under every rho_c(W). Put chi = K_Phi^(1/2) psi = K_Phi e^(-V_f/2) Omega. It is rho_c-invariant by (a). The eigen-equation gives e^(-V_f/2) chi = lambda_0 Omega, so chi = lambda_0 e^(V_f/2) Omega is continuous and strictly positive, and chi = lambda_0^(-1) K_Phi (e^(-V_f) chi). Apply rho_c(W): chi = lambda_0^(-1) K_Phi ((e^(-V_f) o w) chi), where w is the rotation of rho_c(W). Subtract and use that K_Phi is injective (beta_M > 0): (e^(-V_f) - e^(-V_f) o w) chi = 0. Since chi > 0, V_f o w = V_f for every W. But w changes the (1, mu) plaquettes that cross the cut: with outgoing bond quaternion q = Phi_mu(k+1, x) Phi_mu(k, x)^(-1), the term (1/2) tr q becomes (1/2) tr(W q); the plaquettes on one side of the cut and the transverse plaquettes are unchanged (a gauge rotation at one corner). At Phi = 1 the difference is beta_M d_x (1 - (1/2) tr W), d_x >= 1 the number of transverse links at x. It is not zero for W not 1. Contradiction. QED
Meaning: the face vacuum has colour-charge fluctuations across every cut, because the sheets are coupled along direction 1. The longitudinal coupling charges for them.

**Identity KIN-5 (Hellmann-Feynman for the kinetic time; PROVED where the two top eigenvalues are simple).** Heat-kernel form. B_t = e^(-tN/2) S S* e^(-tN/2) has the same non-zero eigenvalues as S* e^(-tN) S. For a simple eigenvalue lambda_i(t) with unit eigenvector phi_i(t): d/dt log lambda_i = - n_i(t), n_i = <phi_i, N phi_i> >= 0. (phi_i lies in the range of e^(-tN/2), so it is in the domain of N.) Hence dm/dt = n_1(t) - n_0(t). So, on an interval where lambda_0 and lambda_1 stay simple: **m is non-decreasing in t if and only if (FLUX-EXC) n_1 >= n_0 holds there.** N is the sum over the cut links of the Casimir of the colour charge beyond the cut: the electric energy in units of t. This is the anisotropic form of item 46 of `gap-brainstorm-max.md` (there the excess is of all plaquettes and has an electric and a magnetic part of opposite signs; here it is one non-negative operator).

**Example KIN-6 (the structure alone does not give the sign; PROVED).** On C^2 take S = diag(1, e^(-m/2)) and N = diag(a, c) with a > c >= 0. Then S* e^(-tN) S = diag(e^(-ta), e^(-m-tc)) and the gap is m - t(a - c): it falls and closes at t = m/(a - c). So no proof of (MON-L) can use only "S* e^(-tN) S with N >= 0". It must use what N and the face vector are.

**Corollary KIN-D (domination in the unit disc; PROVED).** Heat-kernel form. The eigenvalues of 4N are sums over the cuts of n_c^2 - 1, n_c = 2 j_c + 1: non-negative integers. With w = e^(-t/4): S* e^(-tN) S = sum over k >= 0 of w^k A_k, A_k = S* P_k S >= 0, P_k the spectral projection of 4N at k. The series converges in norm for abs(w) < 1 and defines an analytic family there; for abs(w) <= 1, abs(<f, T(w) g>) <= <f, T(abs(w)) f>^(1/2) <g, T(abs(w)) g>^(1/2) (Cauchy-Schwarz term by term). The face is the boundary point w = 1; beta_L = 0 is w = 0.

**Lemma KIN-CVX (PROVED).** log lambda_0(t) and log(lambda_0 lambda_1)(t) are convex and non-increasing in t. Proof. lambda_0(t) is the supremum over unit f of int e^(-t nu) d mu_(Sf)(nu), mu_(Sf) the spectral measure of N at S f. Each such function is log-convex and non-increasing; a supremum of log-convex functions is log-convex. lambda_0 lambda_1 is the top eigenvalue of the second exterior power of the operator, which is (Lambda^2 S)* e^(-t(N x 1 + 1 x N)) (Lambda^2 S) on antisymmetric vectors: the same form. QED

**Remark TOR (ARGUED).** On a slice that is periodic in direction 1 the reduction keeps one holonomy per column. At beta_L = infinity the operator is a direct integral over these holonomies, so on a torus the face has no isolated top eigenvalue. The face is an anchor for clustering of local observables in infinite volume, not a torus seed. This agrees with check 1074's correction of Remark RP-ANI and with check 1070 section 6.

**Remark FLAT (ARGUED, Gaussian level; GUIDE).** At beta_T = 0 and any finite beta_L, expand the action to second order about the trivial configuration. With transverse momentum k of length kappa, split the transverse field a = (A_2, A_3) into a_par along k and a_perp across k. Then a_perp decouples with action (beta_M/2)(k_0^2 + k_1^2) abs(a_perp)^2: one massless two-dimensional field for every transverse momentum. It is the transverse plaquette field, and it is gauge invariant. The rest, B_i = A_i - (k_i/kappa) a_par, is a two-dimensional massive vector field with mass^2 = (beta_M/beta_L) kappa^2. So the longitudinal gauge fields do not touch the transverse plaquette modes at this order. For SU(2) their mass can come only from the non-linear terms, so it is expected to stay of the size of the sheet mass on the whole leg beta_T = 0 (belief). With beta_T > 0 the same modes get the two-dimensional mass^2 (beta_T/beta_M) kappa^2. Consequence for the routes: on the leg beta_T = 0 from the anchor to (beta, beta, 0) the gap is not expected to rise to order one; the rise is on the beta_T leg. For compact U(1) the flat branch stays massless at large beta_M (belief), which is consistent with the anchor reading the group.

**Remark RATE (GUIDE; recalled exponents).** The inequality that a bridge with a non-decreasing gap would give, m_iso(beta) >= c m_O(4)(beta), is consistent at both ends of the coupling range: in the window the isotropic gap is of order one and the sheet gap is of order e^(-pi beta) (rows 1063, 1072); at large beta the perturbative exponents are 3 pi^2/11 = 2.69 for four-dimensional SU(2) and pi for the two-dimensional O(4) model, and 2.69 < pi. In five dimensions it fails at weak coupling if the isotropic model is gapless there (belief). This is a consistency check of BR-2's direction. It proves nothing.

**Where the attempt on VB-3 stops.** Lemma KIN turns (MON-L) into the sign of n_1 - n_0. I tried three ways to get the sign and each fails at a named point. (1) Operator order (KIN-1): gives each eigenvalue, not their ratio; it loses the volume factor (KIN-2). (2) Frustration-freeness (KIN-3): false on the face (KIN-4). (3) Convexity in t (KIN-CVX): the gap is a difference of convex functions. Near the face the sign is the physics of Orland's linear potential (found; row 1053): the lowest G-invariant face excitations contain a pair of charged sheet particles, and N adds the Casimir on the cuts between them. I did not make this a proof: it needs the particle content of the O(4) transfer operator, which the posted theorems do not state. (FLUX-EXC) is OPEN.

#### 6.2 Hand work on VB-11: the checkerboard family

**Setting.** Box Lambda_long x Lambda_perp with free boundary. Extended family: beta_L(x) in (0, infinity] for each transverse site x (the L plaquettes of the plane {x} x Lambda_long), beta_M(l) >= 0 for each transverse link l, beta_T(p) >= 0 for each transverse plaquette p. A site with beta_L(x) = infinity is frozen as in Lemma FACE-LIM of row 1053: its longitudinal links are 1 and its gauge group is rigid (one element for the whole plane). Every member is reflection positive for the reflections that keep its coupling pattern (the argument of Remark RP-ANI). The isotropic model and the face are members.

**Lemma CB-L (PROVED).** Let beta_T = 0 and F = {x : beta_L(x) = infinity}. On gauge-invariant functions the measure has, with respect to Haar measure on the unfrozen longitudinal fields a_x and on all sheets Phi_l, the density
  prod over x not in F of w_x(a_x) . prod over l = (x, y) of exp( beta_M(l) sum over bonds <u u'> of (1/2) tr( a_x(u, u') Phi_l(u') a_y(u, u')^(-1) Phi_l(u)^(-1) ) ),
with a = 1 at frozen sites and w_x the Wilson weight of the plane at x. So it is a product measure over the connected components of the graph whose vertices are the unfrozen sites and all links, a link being joined to its unfrozen ends. If F is the even sublattice, each odd site x is one component together with its n <= 4 links, and with Phi replaced by Phi^(-1) on the links that end at x the component measure is GH2_n:
  d mu_x proportional to prod over L plaquettes of e^(beta_L(x) x_p(a)) . prod over i <= n and bonds of exp( beta_M(l_i) (1/2) tr( Phi_i(u)^(-1) a(u, u') Phi_i(u') ) ) da dPhi,
a two-dimensional SU(2) lattice gauge theory with n fundamental Higgs fields of fixed length. Local gauge group: a to g(u) a g(u')^(-1), Phi_i to g(u) Phi_i. Far-end rigid groups: Phi_i to Phi_i k_i.
Proof. With beta_T = 0 a sheet meets only the two planes at its ends. A frozen plane has no variable. So the factors of the density are functions of the blocks of one component each. For a link l = (y, x) that ends at x, (1/2) tr(Phi_l(u') a^(-1) Phi_l(u)^(-1)) = (1/2) tr(Psi(u)^(-1) a Psi(u')) with Psi = Phi_l^(-1), since the trace of an SU(2) element equals that of its inverse. QED
Note. The observables are the functions that are invariant under the local groups at odd sites and the rigid groups at even sites. One rigid group acts on links of four different components. So clustering of the product measure on these observables needs, in each component, decay of the correlations that are charged under the far-end rotations, and clustering of the singlets.

**Lemma CB-T (PROVED).** Let beta_L = infinity at every site and B = {p : beta_T(p) > 0}. The face measure is a product over the connected components of the graph on links in which two links are joined when they lie on a common plaquette of B. If B is one colour class of the checkerboard colouring of the transverse plaquettes, every interior link lies on exactly one plaquette of B, and each component is P4: four sheets with density exp( sum over i of beta_M(l_i) sum over bonds of (1/2) tr(Phi_i(u) Phi_i(u')^(-1)) + beta_T sum over u of (1/2) tr(Phi_1 Phi_2 Phi_3^(-1) Phi_4^(-1))(u) ).
Proof. On the face the mixed terms act within one sheet and a transverse plaquette term joins its four links. Two plaquettes of Z^2 that share a link have different colours. QED

**Lemma P4-ORB (PROVED).** The rigid group SU(2)^4 of the four corners acts on (Phi_1, ..., Phi_4) with orbits labelled by the conjugacy class of H = Phi_1 Phi_2 Phi_3^(-1) Phi_4^(-1). So the functions of one longitudinal site that are invariant under the rigid group are the functions of the plaquette trace x_p(u).
Proof. With corner elements g_1, ..., g_4 the action is Phi_1 to g_1 Phi_1 g_2^(-1), Phi_2 to g_2 Phi_2 g_3^(-1), Phi_3 to g_4 Phi_3 g_3^(-1), Phi_4 to g_1 Phi_4 g_4^(-1), and H goes to g_1 H g_1^(-1). Take g_1 = 1 and choose g_2, g_3, g_4 in turn to make Phi_1, Phi_2, Phi_3 equal to 1. Then Phi_4 = H^(-1). The elements that keep this form are g_1 = g_2 = g_3 = g_4 = g, and they conjugate H. QED
Meaning: in P4 the whole singlet content at one longitudinal site is one real variable. On the full face it is the gauge-invariant content of a two-dimensional lattice gauge field.

**Lemma GH2-0 (PROVED).** In GH2_n with beta_L = 0 (the longitudinal field at the odd site is Haar distributed), integrating the longitudinal links gives a nearest-neighbour model for (Phi_1, ..., Phi_n) with bond weight
  omega(s) = (2/s) I_1(s) = sum over k >= 0 of (s^2/4)^k / (k! (k+1)!),   s^2 = sum over i of beta_i^2 + 2 sum over i < j of beta_i beta_j rho_ij(u) . rho_ij(u'),
where beta_i = beta_M(l_i), rho_ij(u) = Phi_i(u)^(-1) Phi_j(u) is gauge invariant, and the dot is the inner product of unit quaternions. The weight is a power series with non-negative coefficients in the inner products rho_ij(u) . rho_ij(u'). The far-end rotations act transitively on the single-site space SU(2)\SU(2)^n. For n = 1 the weight is constant. For n = 2 the model is a nearest-neighbour O(4) ferromagnet for rho = rho_12 with bond weight f(rho . rho') = omega( (beta_1^2 + beta_2^2 + 2 beta_1 beta_2 rho . rho')^(1/2) ); at beta_1 = beta_2 = b its logarithmic derivative in rho . rho' is (b/s) I_2(b s)/I_1(b s) with s = (2 + 2 rho . rho')^(1/2), which is less than b/2 at alignment.
Proof. For one bond, sum over i of beta_i (1/2) tr(Phi_i(u)^(-1) a Phi_i(u')) = Re(a S), S = sum over i of beta_i h_i, h_i = Phi_i(u') Phi_i(u)^(-1), as quaternions. int exp(Re(a S)) da = int exp(abs(S) (1/2) tr a) da = (2/abs(S)) I_1(abs(S)), by invariance of Haar measure. abs(S)^2 = sum beta_i^2 + 2 sum over i < j of beta_i beta_j Re(h_i h_j^(-1)), and Re(h_i h_j^(-1)) = Re(rho_ij(u) rho_ij(u')^(-1)). QED
Meaning. With n = 2 (a transverse site with two links: the split 2 + 1, or an edge site) the half-unfrozen model at beta_L = 0 is exactly a ferromagnetic O(4) model with a bond weight that is not an exponential. Its stiffness at alignment is below b/2: two sheets in series. It is the nearest relative of the posted class that the gauge family contains. It is not a member: omega is not a mixture of weights e^(c t) with c in [0, b] (omega(s(t)) has order 1/2 as an entire function of t, a non-trivial such mixture has order 1).

**Proposition CB-CH (ARGUED; charged decay in GH2 from the posted estimates).** GIVEN estimate (3.61) of OpenAI's posted O(4) paper in the form that row 1009 reports (for a sheet with fixed one-sided bond twists, couplings in [0, b] and pinned spins, an observable O with zero average under the rigid rotation has abs(E O) <= C norm(O) abs(A) e^(-c d_pin/s(b))): in GH2_n, for every beta_L in [0, infinity], let F and H be bounded local functions whose longitudinal supports are at distance r, and let F have zero average under the far-end rotation of one field Phi_i alone. Then abs(E[F H]) <= C norm(F) norm(H) abs(supp F) e^(-c (r - r_0)/s(beta_M)).
Argument. Condition on the longitudinal field a, on the other Higgs fields and on Phi_i on the support of H. Given a, the field Phi_i is a sheet with the fixed bond twists a(u, u'); given the rest it is that sheet with pins on the support of H. H is then a constant, F is a function of Phi_i with zero rigid average, and (3.61) bounds its conditional expectation. Integrate. The bound does not depend on the law of a.
Why ARGUED and not PROVED GIVEN: I know (3.61) only through row 1009's reading; I did not check that its pin class contains pins on an arbitrary finite set, nor its twist convention. The estimate is posted and unrefereed.

**What is left in each model: the singlet sector.** In GH2_n: the functions invariant under all far-end rotations, that is, the Wilson loops of a and the mixed plaquettes. In P4: the plaquette trace x_p(u) and the invariant functions of several sites, for example the bond energies of each sheet. By row 1009's reading, the posted proof reaches such observables only through association and a two-replica step for "the untwisted zero-field ferromagnet", and says the restriction is essential. Twists (GH2 with beta_L > 0) and the on-site potential (P4 with beta_T > 0) both leave that class. So the first open statement of VB-11 is the same in both models: **(SING) a mixing bound for the singlet sector of a two-dimensional non-abelian model with a rigid group, when the bond weights are twisted or an invariant on-site potential is present.** Row 1053 6.9 met the same statement on the full face ("every attempt to reach the singlet sector on the face from the rigid symmetry failed"). VB-11 does not remove it. It puts it in models with one singlet variable per site (P4) or with an untwisted ferromagnetic weight (GH2_2 at beta_L = 0), where a port of the posted singlet step can be tested first.

**Control: compact U(1) (ARGUED, Gaussian level).** GH2_n for U(1) at large beta_M: the sum of the n phases is taken by the gauge field; the n - 1 relative phases are free massless fields, so correlations of their gradients decay by a power law. For n = 2 and beta_L = 0 the reduced model is a plane-rotator ferromagnet for the relative phase with bond weight I_0(2 b abs(cos(delta/2))); at large b it is expected to be in the Kosterlitz-Thouless phase (belief; Frohlich and Spencer prove this for the standard weight). P4 for U(1): the potential gives a mass to phi_1 + phi_2 - phi_3 - phi_4 only; three combinations stay massless and the bond energies decay by a power law. So (GH2-MIX) and (P4-MIX) are false for U(1) at large beta_M at this level, as the anchor requires.

**Where the attempt on VB-11 stops.** Proved: the two factorizations, the orbit lemma, the explicit weight at beta_L = 0. Argued: charged decay in GH2 for every beta_L from the posted estimates. Open: (SING) in P4 and in GH2. Not decided here: whether the posted singlet step ports to GH2_2 at beta_L = 0 (untwisted, ferromagnetic, non-exponential weight with non-negative series). That needs OpenAI's text (Section 3.11), which I did not read.

#### 6.3 Counterexamples built in this step

- Example KIN-6: the form S* e^(-tN) S does not give a non-decreasing gap.
- Lemma KIN-4: the frustration-free route to (MON-L) is closed on the face for every beta_M > 0.
- Lemma GH2-0, last line: the half-unfrozen model is not in the posted class, even in its simplest case.
- Example KIN-7 (6.4): (MON-L) is false for frozen Q_8 on a small box.

Numeric runs: none for 6.1 to 6.3. Section 6.4 reports five small GUIDE runs.

#### 6.4 Example KIN-7: (MON-L) is false for frozen Q_8 on a small box (the limit statement PROVED by hand; the window values GUIDE)

Added after 6.1 to 6.3, as the kill test T2 for VB-3. It changes the entry of VB-3 in step 5 (note placed there).

**Setting.** Lemma KIN holds for every compact group with its own characters: its proof uses Peter-Weyl, Schur's lemma and Haar measure only. Take Q_8 = {+-1, +-i, +-j, +-k} inside SU(2), with x = (1/2) tr: x(+-1) = +-1 and x = 0 on the other six elements. Slice with n = 2 sites and one transverse link (two transverse sites); there is no transverse plaquette. Then K is the space of class functions of q = Phi_2 Phi_1^(-1). On a character chi_rho, K_Phi acts as lambda_rho(beta_M)^2 (two links) and D as lambda_rho(beta_L)^2 (two cuts), lambda_rho(b) = sum over g of e^(b x(g)) chi_rho(g) / (d_rho sum over g of e^(b x(g))). So R T R^(-1) = E K E with E the multiplication by e^(beta_M x(q)/2) and K = sum over rho of kappa_rho P_rho, kappa_rho = lambda_rho(beta_M)^2 lambda_rho(beta_L)^2.

**Data.** Characters of Q_8: the trivial one; sigma_a for a = i, j, k, equal to 1 on {+-1, +-a} and to -1 on the other four elements; tau of dimension 2 with chi_tau(+-1) = +-2 and 0 elsewhere. With c = cosh b, s = sinh b: lambda_sigma = (2c - 2)/(2c + 6), lambda_tau = 2s/(2c + 6). Put A = kappa_sigma, B = kappa_tau. Orthonormal class vectors: e_0 at 1, e_1 at -1, e_i, e_j, e_k. Then K_00 = (1 + 3A + 4B)/8; K_0a = (sqrt 2/8)(1 - A); K_aa = (1 + 3A)/4; K_ab = (1 - A)/4 for a not b. With f = (e_i + e_j + e_k)/sqrt 3: K_ff = (3 + A)/4 and K_0f = (sqrt 6/8)(1 - A). On differences of the e_a, K acts as A.

**Limit.** E = e^(beta_M/2) diag(1, eps^2, eps, eps, eps) with eps = e^(-beta_M/2). Fix beta_L and let beta_M tend to infinity. Then A tends to A_L = lambda_sigma(beta_L)^2 and B to B_L = lambda_tau(beta_L)^2. By the Schur complement, the top eigenvalue of e^(-beta_M) E K E is K_00 + O(eps^2) and the next is eps^2 mu + O(eps^3), with mu = max{ K_ff - K_0f^2/K_00, A }. So m(beta_L) = beta_M + log K_00 - log mu + o(1), and m(infinity) = beta_M + o(1) (there A = B = 1). Hence
  lim over beta_M of [m(beta_L) - m(infinity)] = delta(beta_L) := log K_00 - log mu, at (A_L, B_L).
For large beta_L, with eta = e^(-beta_L): A_L = 1 - 16 eta + O(eta^2), B_L = 1 - 12 eta + O(eta^2), K_00 = 1 - 12 eta + O(eta^2), mu = 1 - 4 eta + O(eta^2). So delta(beta_L) = -8 eta + O(eta^2) < 0.

**Statement (PROVED).** For frozen Q_8 on this box there are finite beta_L and beta_M with m(beta_L, beta_M) < m(infinity, beta_M). So (MON-L), in its endpoint form, is false for Q_8 on this box, and (FLUX-EXC) fails there. Lean form: explicit 5 x 5 real symmetric matrices, a Schur complement and two limits.

**Reading.** For a finite group the ordered face vacuum is close to a point mass at q = 1. A point mass has weight d_rho^2/8 on every character, so it pays the electric cost of all of them (12 eta). The first excited vector is the uniform vector on the six non-central elements; three quarters of it is the trivial character, and it pays 4 eta. The excitation carries less electric energy than the vacuum.

**GUIDE runs** (double precision, one thread, a few seconds each; five short scripts in the session scratchpad, not in the repo; they may refute or guide and they discharge no step).
- Lemma KIN's operator identity, Q_8, n = 2, checked by brute force from T = e^(-V/2) K_a K_Phi e^(-V/2): the two sides differ by at most 6 x 10^(-15) entrywise; M commutes with K_Phi to 10^(-17). Not refuted.
- Q_8: the dip exists for beta_M above about 2.2. At beta_M = 2.4, n = 2: m(infinity) = 1.9556 and the least m is 1.9162, at beta_L = 3.5. At beta_M = 2.4, n = 3: m(infinity) = 1.9774 and m(2.4) = 1.8416, so there the isotropic point itself lies below the face. The limit formula is met: at beta_M = 12, beta_L = 8 the run gives -2.680 x 10^(-3) against -8 e^(-8) = -2.684 x 10^(-3).
- 2T (binary tetrahedral), n = 2: a dip for beta_M above about 5 (at beta_M = 6: -0.150 at beta_L = 5.3); none on the grid for beta_M at most 4.
- SU(2), n = 2 (class functions; characters up to dimension 60): m(beta_L) - m(infinity) is positive at 160 values of beta_L in [0.05, 2000], for beta_M = 0.5, 1, 2.4, 4, 8. It decreases to 0 as beta_L grows.
- Compact U(1): n = 2, the same; n = 3 (two cuts; Fourier modes up to 10): positive at nine values of beta_L in [0.5, 200] for beta_M = 1, 2.4, 4.
So on these boxes the runs refute (MON-L) for the frozen groups and do not refute it for SU(2) or U(1). They prove nothing for SU(2).

**Consequence for the tests.** T2 binds VB-3 and BR-2's second obligation: a proof of (MON-L) on boxes, in endpoint or monotone form, must fail for frozen Q_8 and 2T. U(1) passes on these boxes and Q_8 fails, so "non-abelian structure" (S1) is the wrong reading for this step. The step must use that the group is continuous: the face vacuum is a smooth vector, not a point mass. Scope: boxes with one sheet and two or three slice sites. I computed nothing for Q_8 in infinite volume.

### Step 7 (task 6: each surviving item as a complete brief). DONE.

Model names are the lead's to set. Each brief is written so that a worker who has read nothing else can start.

#### 7.1 Brief K1 (check row; first): `gap-bridge-vectors-check`

- What to check, line by line, in `library/gap-bridge-vectors-max.md`: Lemma KIN (a) to (d) and Corollaries KIN-1 to KIN-3; Lemma KIN-4; Identity KIN-5; Example KIN-6; Corollary KIN-D; Lemma KIN-CVX (6.1); Lemma CB-L, Lemma CB-T, Lemma P4-ORB, Lemma GH2-0 and Proposition CB-CH (6.2); Example KIN-7 (6.4); Lemma SWAP and Lemma LOCK (step 5, VB-4 and VB-10); Remark FLAT's algebra; the kill verdicts of step 5 that are marked FAILS.
- Tests first: (1) the order of the rotations in KIN (c) and the claim that the M_c commute; (2) injectivity of K_Phi and positivity of chi in KIN-4; (3) the Schur complement and the two expansions in KIN-7 (the matrix entries K_00, K_0a, K_aa, K_ab can be recomputed from the character table of Q_8); (4) in GH2-0, the integral (2/s) I_1(s) and the order-1/2 argument against a mixture; (5) Proposition CB-CH against the primary text: OpenAI, "Sharp mass bounds for the two-dimensional O(4) model", commit pinned in row 1009, pp. 28 to 30, estimate (3.61): does its pin class allow pins on an arbitrary finite set, and on which side is the twist; (6) whether Lemma KIN, or the checkerboard factorization, is already in a PR branch (this run searched the lane folder only).
- Verdicts: HOLDS, HOLDS AFTER CORRECTION with the text, FAILS with the first failing line. No new attack. A cross-provider model is preferred; a same-provider check is labelled as such.
- Output: `library/gap-bridge-vectors-check-<model>.md`.

#### 7.2 Brief R1 (reading row, the rule on new paths): `gap-checkerboard-read`

- Read open copies only, each in a new empty directory; no sign-in; never commit a paper. Collect, with exact statements, hypotheses, group range and rigour: (1) two-dimensional lattice gauge theories with fundamental Higgs fields of fixed length: any proof of clustering or a mass gap away from the expansion regions (Brydges, Frohlich and Seiler; Balaban, Brydges, Imbrie and Jaffe; Borgs and Nill; Seiler's notes if an open copy exists); (2) transverse-lattice gauge theory in Hamiltonian form (Bardeen, Pearson and Rabinovici; Burkardt and Dalley): is the elimination of the longitudinal field by Gauss's law, with a Casimir of partial charges, written on the lattice; (3) Orland's three papers (arXiv:hep-th/0607013, 0704.0940, 0801.0389) in full: what is derived about the unfreezing of the longitudinal coupling, and with which approximations; (4) monotonicity of a spectral gap in a kinetic coefficient: results for H = -t Laplacian + V (single-well potentials; Ashbaugh and Benguria; Andrews and Clutterbuck) and for transfer operators; (5) gap theorems for two-dimensional sigma models on homogeneous spaces other than spheres, and for O(N) ferromagnets with a general bond weight.
- End with one RESULT line. Output: `library/prior/gap-checkerboard-read-<model>.md`.

#### 7.3 Brief P1 (proof row for VB-11; only if K1 holds for Lemma GH2-0 and CB-CH is settled): `gap-checkerboard-singlet`

- Statement to prove or refute, in this order. (a) (GH2_2-MIX at beta_L = 0): for every b > 0, the nearest-neighbour model on Z^2 with spins rho in S^3 and bond weight f(rho . rho') = omega((2 b^2 + 2 b^2 rho . rho')^(1/2)), omega(s) = (2/s) I_1(s), has exponential decay of covariances of Lipschitz local observables, uniformly on free subgraphs and tori. (b) (P4-MIX): the same for the four-sheet model P4(b, beta_T), 0 <= beta_T <= b, on functions that are covariant under the corner group. (c) (GH2-MIX) for beta_L > 0.
- Why these: Lemma CB-L and Lemma CB-T show that they are exact members of the anisotropic family with couplings on a sublattice. They are the first cases of BR-2's two obligations. In (a) the model is an untwisted ferromagnet whose weight is a power series in rho . rho' with non-negative coefficients, the nearest relative of the posted class.
- Inputs: OpenAI's O(4) paper, Section 3 (source pinned in row 1009; rows 1007 and 1009 are the lane's readings); Ding, Huang and Yang, arXiv:2611.04908 (row 1007); this file, 6.2; row 1053 Lemma RIG and its 6.9.
- Order of work. (1) List every place where the posted proof uses that the bond weight is exp(b_e t) with 0 <= b_e <= b: the stiffness induction (class "defined by bounds only"), the association inequality, the two-replica Ginibre step, the bond cutting and the interpolation in the coupling. (2) For each, decide whether it holds for the weight f of (a); write the port or the first failing line. (3) Only then (b): the singlet content is the one variable x_p(u) per site (Lemma P4-ORB); the charged sector has Lemma RIG; find a singlet step that does not use association, or show which inequality fails. (4) Then (c).
- Tests to run on any proof: compact U(1) (the same models are massless at large b at the Gaussian level; the proof must fail there, and the place must be named); frozen Q_8 and 2T (the sheets order; must fail); Lemma PT (a product with a massless factor); Lemma SHEET and Theorem D2 (no supremum over coupling fields or pins beyond the posted class); the five-dimensional test does not bind (the models are the same in 2 + 3).
- What it gives if proved: clustering for the anisotropic family on one sublattice, at window values of beta_M and beta_T (b) or for every beta_L on half of the sites (c). What it does not give: C_beta. The second sublattice is a carry.
- Stop rule: a proof, a counterexample, or one named step that failed in three written ways. No computer-assisted step. Output: `library/gap-checkerboard-singlet.md`.

#### 7.4 Brief P2 (proof row for VB-3 on its test-bed VB-18; lower rank): `gap-descent-sign`

- Statement. (FLUX-EXC) for SU(2) on one-sheet boxes: for the slice {1, ..., n} with one transverse link and free ends, m(beta_L, beta_M) >= m(infinity, beta_M) for all beta_L, beta_M > 0; in the heat-kernel form, n_1(t) >= n_0(t) for all t > 0. First case n = 2: K is the space of class functions of SU(2), and R T R^(-1) = E diag(kappa_j) E in the character basis, E the multiplication by e^(beta_M cos(theta)/2), kappa_j = lambda_j(beta_M)^2 lambda_j(beta_L)^2.
- Why: Lemma KIN reduces (MON-L) to this sign. Example KIN-7 shows the sign is false for frozen Q_8, so the proof has a named thing to use: the vacuum of a continuous group is smooth. The GUIDE runs of 6.4 found no dip for SU(2) at n = 2.
- Cheapest kill test, to run before any proof (GUIDE, small, one thread): compute m(beta_L) - m(infinity) for SU(2) at n = 3 with one sheet (invariant functions of two group elements under joint conjugation; basis labelled by (j_1, j_2, L); the cut operators need 6j symbols), and for two sheets on a transverse path of three sites. A dip for SU(2) refutes the box form of (MON-L).
- Order of work if no dip is found: (1) n = 2 by hand (a one-dimensional problem on [0, pi] with weight sin^2); (2) the structure that survives to n >= 3: in the character basis the operator has non-negative entries for the face part (the coefficients of e^(b cos) in characters are positive) and N is diagonal; look for an oscillation or total-positivity argument that fails for a point-mass vacuum; (3) only then several sheets.
- Tests on any proof: frozen Q_8 and 2T (must fail; KIN-7); compact U(1) (it may pass; that is allowed, since the face hypothesis fails for U(1) at large beta_M in infinite volume); Example KIN-6 (the proof must use more than the form S* e^(-tN) S).
- What it gives if proved for all boxes with a volume-free form: BR-2's second obligation; in three dimensions, with the posted theorems, a gap for lattice SU(2) at the isotropic coupling. That strength is a warning: no mechanism is on file beyond n = 2.
- Stop rule: as P1. Output: `library/gap-descent-sign.md`.

#### 7.5 Not proposed, and why

- A row on (ZF-path): it is Z6 of Route Z in another variable (VB-1).
- A row on the flux ratio from the anchor: no consumer for clustering (VB-2).
- A row on the fifth direction or on the mixed action as a path: no selective step (VB-9, VB-10).
- A numeric search for a transition surface (E-2): boxes of the size this machine allows decide nothing.

### Step 8 (marks, scope, credits, RESULT). DONE.

#### 8.1 Marks

| Mark | Items |
|---|---|
| PROVED (by hand in this file; checked by no one) | Lemma KIN (the operator identity; its link to the measure is the lane's (TM)); Corollary KIN-1 (for the Wilson weight GIVEN monotone Bessel ratios, recalled); Corollary KIN-2 (the inequality); Corollary KIN-3; Lemma KIN-4; Identity KIN-5; Example KIN-6; Corollary KIN-D; Lemma KIN-CVX; Example KIN-7 (the limit statement); Lemma SWAP; Lemma LOCK; Lemma CB-L; Lemma CB-T; Lemma P4-ORB; Lemma GH2-0 |
| ARGUED | Proposition CB-CH (rests on row 1009's reading of a posted, unrefereed estimate); Remark TOR; Remark FLAT (Gaussian); the U(1) controls of 6.2; the size of the bracket in KIN-2; the verdicts on VB-9, VB-10, VB-12, VB-16; the face clustering in three dimensions of VB-18 |
| GUIDE | the five runs of 6.4; Remark RATE |
| OPEN | (FLUX-EXC) and (MON-L) for SU(2); (SING), (GH2-MIX), (P4-MIX); (MON-L)_3; (ZF-path), which is Z6; (FACE-SG) and (LIN-path) as in row 1072 |
| FAILS | as a new vector: VB-1; at the consumer: VB-2, VB-4, VB-6; renaming: VB-3 as a reduction, VB-5; no candidate: VB-7; found and not redone: VB-8, VB-12, VB-13, VB-14, VB-15; no selective step: VB-9, VB-10; not a route: VB-16 |
| Left with work | VB-11 (test-bed and start data), VB-3 (a tool, with the Q_8 constraint), VB-18 (test-bed) |

#### 8.2 Scope of the negatives

- "No vector passes the wall" means: none of the eighteen named here gives C_beta from proved statements. It says nothing about vectors not named.
- "Found" means found in the lane folder by the searches of 4.0. Open PR branches were not searched.
- VB-7 ("no candidate") covers the inequality families listed there, as recalled or as read by other rows. No literature search was run in this row; brief R1 asks for one.
- Example KIN-7 is about frozen Q_8 on one small box. The runs for SU(2) and U(1) are GUIDE on two or three slice sites with one sheet.
- VB-9 and VB-10 fail as reductions by argument, not by theorem.
- Remark FLAT is a second-order computation about the trivial configuration.

#### 8.3 What this run did not cover

OpenAI's and Ding, Huang and Yang's papers (used through rows 1007 and 1009). Orland's papers (abstracts through row 1053). The files of rows 1025, 1066 and 1068 beyond what rows 1072, 1074 and 1075 quote. Seiler's notes. The proof of (TM) for couplings by type (taken from the lane with Remark RP-ANI as corrected by check 1074). The monotonicity of Bessel ratios (recalled). SU(2) on boxes with three or more slice sites or with several sheets. Frozen groups in infinite volume. A literature search for the checkerboard models and for Lemma KIN. Open PR branches.

#### 8.4 Strong words, read against the run

"New" is not used as a mark; the strongest is "not found in the lane folder". "PROVED" always means by hand here and unchecked. "Survives" means: left with work, not near closure. Lemma KIN-4 says "not" for every beta_M > 0 and every finite beta_L; that is what its proof gives.

#### 8.5 Credits

P. Orland (the anisotropic anchor and the linear potential between sheet particles); W. Bardeen, R. Pearson and E. Rabinovici (transverse lattice); J. Kogut and L. Susskind, M. Luescher, K. Osterwalder and E. Seiler (Hamiltonian and transfer operator); E. Fradkin and S. Shenker; J. Lebowitz and O. Penrose; R. Nevanlinna; A. Denbleyker, D. Du, Y. Liu, Y. Meurice and H. Zou; G. 't Hooft; E. Tomboulis and L. Yaffe; G. Mack and V. Petkova; E. Tomboulis; T. Kanazawa; D. Brydges, J. Frohlich and E. Seiler; J. Ginibre; F. Dunlop; H. Kunz, C.-E. Pfister and P. Vuillermot; J. Frohlich and T. Spencer; J. Frohlich, B. Simon and T. Spencer; M. Goepfert and G. Mack; G. Bhanot and M. Creutz; Y. Tanizaki and M. Unsal; OpenAI, and J. Ding, F. Huang and P. Yang (posted two-dimensional O(N) theorems, unrefereed); T. Balaban, and E. Sussman and L. Alpoge's account (with Claude and Codex as authors of their text); O. Perron, G. Frobenius, I. Schur, F. Peter and H. Weyl, H. Hellmann and R. Feynman (classical tools). In this lane: rows 670, 677, 680, 681 and 685 (Route Z), 834, 859 and 878, 978, 998, 1004, 1007 and 1009 (readings of the posted proofs), 1016 (Proposition LG), 1018, 1025, 1052, 1053 (the face, by Claude Fable 5.2), 1066, 1070, 1072 (the exercise, by Claude Opus 5.5), 1073 (gpt-6-luna), 1074 (gpt-6-astra) and 1075 (Claude Opus 5.5).

#### 8.6 Run record

Only this file was written in the checkout. Nothing was committed or pushed; no gh call. One `git fetch` of the lane branch (three times) and one `git show` into /tmp for check 1074. Five scripts in the session scratchpad (Q_8 brute force; SU(2) and U(1) class functions; Q_8 class model; finite subgroups Q_8 and 2T; U(1) with two cuts), each a few seconds on one thread. No download.

RESULT: Row 1076 (Claude Fable 5.2 max, laptop subagent; checked by no one; five small GUIDE runs): eighteen vectors behind row 1072's assumptions, routes and set-aside methods were stated and tested, none passes the wall, and (W) does not move. On file and not redone: zero transport (Route Z, crux Z6), flux ratios, the fundamental Higgs path, the mixed action, the plane beta_M = 0, the geometry path, the tail and other endpoints. Not found in the lane folder, with work left: VB-11, couplings on a sublattice (PROVED Lemmas CB-L, CB-T, P4-ORB, GH2-0: exact two-dimensional models GH2 and P4 are first cases of BR-2's two obligations; charged decay ARGUED from the posted O(4) estimates as read by row 1009; first open statement (SING), singlet mixing without association), and VB-3, the longitudinal coupling as an electric energy (PROVED Lemma KIN with KIN-1 to KIN-5, KIN-D, KIN-CVX: T = S* D S with the face on top of an operator order, no frustration-free case for beta_M > 0, and monotone (MON-L) is the sign (FLUX-EXC), OPEN and a renaming). PROVED in a limit, Example KIN-7: (MON-L) is false for frozen Q_8 on a small box; GUIDE: no dip for SU(2) or U(1) there, so a proof must use that the group is continuous. PROVED with no consumer: Lemma SWAP, Lemma LOCK. FAILS, each with its reason: the free-energy, Renyi, convexity, fifth-direction and mixed-action vectors. Briefs: check K1, reading R1, proof rows P1 on (SING) and P2 on (FLUX-EXC) for one sheet. Checks 1074 and 1075 of row 1072 were read and used.
