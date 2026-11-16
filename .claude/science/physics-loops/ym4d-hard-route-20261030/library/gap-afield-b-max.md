lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-17T00:18Z

# gap-afield-b-max (queue row 1032): far-afield invention row B

Started 2026-11-16T01:36Z (from `date -u`), pinned at commit 58baf6efc. Session model: claude-fable-5-2 at max effort. No subagents, no numeric job started so far.

Run 2 (this run): started 2026-11-16T12:18Z (from `date -u`), pinned at commit 594d6491b. The first run (01:36Z) wrote only the plan below and then failed for lack of credits (lead note in FINISH.md row 1032); its plan is kept and followed. Session model: claude-fable-5-2 at max effort. No subagents.

This file is written section by section. Each section states what was done, what failed, and what is left.

## 0. Status line (updated in place)

- State: run 2 started 2026-11-16T12:18Z; steps 1-6 done (Sections 1-6: thirteen counted ideas, all FAIL the kill tests; ranking written); step 7 (first lemmas and proved kills) in progress.

## Plan (eight steps, one per response; each appends its result here before the next)

1. Read: FINISH.md (rules, efficiency, Build on published work), `parts/gap.md` in full, `library/gap-dichotomy.md`; fetch the exercise skill at main commit 8b11ae2bb9 into a new scratch folder and follow it. Record the wall, the repaired (W), the dichotomy and the open items in a short digest (section 1).
2. Lane grep: rows 1011-1030 and their library files, `library/open-core.md`, the registry in `parts/gap.md`; list what is already tried so no idea is redone, and write the kill tests in usable form (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, compact U(1), frozen Q_8 and 2T, the five-dimensional test, Lemma CEN, Lemma WN, the four-test spec check) (section 2).
3. Ideas, fields A and B: quantum many-body and quantum information; operator algebras and axiomatic field theory. Each idea: source, exact statement needed on the 4D SU(2) lattice, consumer in the chain (section 3).
4. Ideas, fields C, D, E: geometric analysis; representation theory and harmonic analysis on SU(2); topology. Same format. At least ten ideas in total (section 4).
5. Kill fast: every idea against every kill test; an idea that renames the crux is a FAIL (section 5).
6. Rank survivors by (what they would change) / (cost to find out) (section 6).
7. Top one or two survivors: write the first lemma and try to prove it by hand, or build the counterexample (section 7, split over several responses if long).
8. Close: marks PROVED / ARGUED / OPEN / FAILS, credits, complete briefs for follow-up work items, RESULT line (section 8).

## 1. Digest of the wall (step 1; read, no verdict changed)

Read in full in this run: `GOAL.md`; `FINISH.md` L1-84, L299-362, rows 1031-1033 and the lead notes at L1128-1131; `parts/gap.md` (all 255 lines); `library/gap-dichotomy.md` (all 473 lines); the exercise skill at main commit 8b11ae2bb9 (703 lines, fetched to a scratch folder) and the reference it requires before its step 7, `physics-loop/references/proof-search-governance.md` (126 lines, same commit). The skill's framework refresher read is replaced by `GOAL.md` and `FINISH.md`: this is a standalone proof target that reads no framework axiom (skill L130-132). As in row 1031, this run is the slice of the skill's steps 6c-9 (tests in valid form, routes, kill, rank, real attempts, report); steps 0-6b were done by rows 878, 998, 1003 and are not redone.

**Objects** (`gap-dichotomy.md` 1.1-1.3). Wilson SU(2) on a periodic torus with integer sides n = (n_1, ..., n_4), all at least 3; A(U) = sum over plaquettes of (1 - (1/2) tr U_p); Z(n; beta) = integral of exp(-beta A); F = log Z; f = inf F(n)/abs(n); Delta(n) = F(n) - f abs(n) >= 0; the Casimir free energy D(a) = Delta(a, a, a, a). For a box B of three sides, T_B is the transfer operator, Z(k, B) = Tr T_B^k, eigenvalues lambda_0 > lambda_1 >= ... >= 0, gap m(B) = log(lambda_0/lambda_1), thermal sum S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k. A family with units: data Z_j at the couplings beta_j of the Sussman-Alpoge trajectory, u_j = l_1/a_j, (S0): u_j a multiple of 4, at least 12. P = {2^i l_1}. D^+(L) = upper limit of D_j(L/a_j); z^-(L) = lower limit of (L/a_j) m_j((L/a_j)^3).

**The wall, repaired form** (`parts/gap.md` L21-23). (W): there are a bound (L_0, D_0) of (BDD-Delta) and L in P with L at least 4 L_0 and z^-(L) > 256 D_0 + 30.

**The engine** (Theorem S; Corollary S3'; Theorem ZD-c). (PHYS-SEED): one physical size l with upper limit of S_j(l/(2 a_j); (l/a_j)^3) below 1/5041. A seed gives a gap for every larger cube, uniformly in j. (W) iff (PHYS-SEED) iff [(BDD-Delta) and (Z-UNB)]. Note for my fields: Theorem S is already a finite-size criterion in the sense of Knabe (a property of one finite box gives the gap of all larger boxes). So an idea "use a finite-size criterion" is not new as a frame; it must supply the seed, which is the wall.

**The trichotomy.** Exactly one of (I) (PHYS-SEED); (II) not (BDD-Delta) (the Casimir free energy is unbounded on physical sizes); (III) (BDD-Delta) and z^-(L) <= 256 D_0 + 30 at every size (branch G at every size). Form 2 (Theorem CR): given (BDD-Delta), (W) iff Omega(D_0) is empty iff it has no uniformly recurrent element. (LIOU) = no uniformly recurrent critical element; target-equivalent given (BDD-Delta).

**The open items the row names**, with where they stand at this pin (`parts/gap.md` L108-148):

| Item | What it is | Standing |
|---|---|---|
| (W) | the wall | OPEN |
| (BDD-Delta) | D^+ bounded on physical sizes from some L_0 on | OPEN; target of no row; row 1031's "no soft proof" claim is unsupported after its checks |
| (LIOU) | no uniformly recurrent critical element | OPEN, target-equivalent given (BDD-Delta) |
| (PLATEAU) | the open alternative in Proposition A1 of row 1028 (keeping the ultraviolet data in the limits) | OPEN |
| (TB)_n | the one inequality of the Tomboulis-Kanazawa decimation line (row 1025) | OPEN; gives the flux half at one coupling, not the seed |
| (SYM) with (REG) | a local covariant frame with j - d conserved and square integrable (route (ii), rows 1026, 1034) | not decided, not the deciding obligation (row 1034); O1, O2 named; rows 1036-1046 continue |
| (SER), (SPR) | the two open items of the vortex-container form (T-vor) of the short step (row 1018) | OPEN |
| (FL), (DEC) | the two open items of the pinned form (T-pin) (row 1018) | OPEN |
| unit-level log-Sobolev inequality | route LC's reopen condition (row 1021) | OPEN, the wall in log-Sobolev form |
| (E0-tor) | torus independence of the account's vacuum counterterm | OPEN (supply side) |

**What a new idea must be** (`parts/gap.md` L47-50, L93, L233-242, L254-255). A (K-flow) statement: it reads the first-passage data of Wilson SU(2) and is carried through the band by a step that is false for compact U(1), for frozen groups and for a product with a massless factor; or a (K-one) property of the measure at one scale. "Selective" means false for a massless factor. A pass of the tests is no support. For (K-flow) tools the lane has constraints and no refutation device.

**Standing verdict of the lane before this row**: no route is near closure; every proved piece is blind (true for every datum); the 2D pinned-cell port fails in the class of all pins; route (ii) (aligned frames) is open with (N1)-(N3), upper faces and (O1) remaining; row 1031's ten ideas all failed.

Left for step 2: the exact statements of the kill tests, and the grep of the lane for my five fields.

## 2. Lane grep and kill sheet (step 2; done 2026-11-16T12:34Z)

**Method.** A count script (kept outside the repository, in my scratch folder) ran case-insensitive regular expressions over `library/*.md`, `library/prior/*.md`, `parts/gap.md` and `FINISH.md` at 594d6491b; the passages with hits were then read at the lines cited below. Scope of every "not found" in this file: exactly these paths at this commit. Main and the open pull-request branches were not searched (`origin/main` is not a ref in this checkout). A hit count is a locator, not a reading.

### 2.1 The kill sheet (on file; not rewritten)

The tests the row names are stated exactly, with file and line, in `library/gap-invent-selective-max.md` L50-65 (row 1013, K1-K9), read in full in this run: K1 Lemma PT with Corollary PT1 (product: D = D_1 + D_2, 1 + S = (1 + S_1)(1 + S_2), m = min; a product with compact U(1) in its massless phase has no seed); K2 Proposition NP (a no-seed product whose D contracts by any theta on any J doublings); K3 Theorem D2 (no hypothesis that is a supremum over bulk tilts or over pins of interior link sets) and K3' the slab device; K4 Lemma SHEET (no hypothesis uniform over plaquette coupling fields); K5 compact U(1) (the gain must vanish identically for an abelian group); K6 frozen Q_8 and 2T (the selective identity must use the Lie algebra, not only non-commutativity); K7 the five-dimensional test (name the dimension-4 input; per row 1028 it tests (BDD-Delta), not (LIOU)); K8 instanton and refilling; K9 the four-test spec check: (S1) non-abelian structure, (S2) a rate, (S3) the whole state space, (S4) typical fields, and (S0) a candidate that returns the crux under another name FAILS (row 1004's reading, `gap-outside-box-max.md` L75; the phrase is defined in no file). Later additions used here: Lemma WN and Lemma TWIST (`gap-invent-selective-max.md` L136-172); Lemma CEN+ in place of Lemma CEN (`gap-global-reform-max.md`, row 1016; Lemma CEN as written FAILS in the gpt-6-astra check of row 1011, `parts/gap.md` L96). Valid form (exercise skill, step 6c): a model M' refutes a candidate only if the candidate's hypothesis H holds in M' and its conclusion T fails there; otherwise the test says what a proof of H must use; a pass is no support.

### 2.2 What the lane already holds in the five fields of this row

| Field of the row | On file (file and line read in this run) | Verdict on file | Left for this row |
|---|---|---|---|
| Finite-size gap criteria (Knabe; Gosset and Mozgunov; Lemm and Mozgunov; Anshu), martingale method (Nachtergaele), detectability lemma (Aharonov, Arad, Landau, Vazirani; Anshu, Arad, Vidick) | `prior/gap-lit-block.md` L92-235, RESULT L383 ("No surveyed ... finite-size criterion is established for a continuous-group lattice gauge theory ... none supplies PA_g"); `gap-skeleton-max.md` L161, L363, L407, L428 (B7: the heat-bath generator is frustration-free); `gap-brainstorm-max.md` L42 (rows 750, 758: the block criterion PA fails on full L2 at weak coupling by a gauge corner; PA_g open on gauge-invariant functions); `gap-crux-exercise-astra.md` L378, L539, L675, L823 (Lemma A2); `gap-form-exercise.md` L114, L185, L354 | "another setting; excluded by the rate filter"; the physical -log T is not a local frustration-free sum; PA_g open with no estimate | only what uses the Kogut-Susskind form or the Gauss law in a new way; the family itself is not redone |
| Lieb-Robinson bounds, gap stability along paths (Hastings and Koma; Bravyi, Hastings, Michalakis; Michalakis and Zwolak; Nachtergaele, Sims, Young) | `prior/gap-outside-read-opus.md` L414-478 (topic E), L637; `prior/gap-math-lit.md` L105-111 ("no use"); `gap-brainstorm-max.md` G15 | strong coupling only; needs a gap along the path | nothing new found |
| Area laws and converses | Wilson-loop area law: `gap-arealaw-opus.md` RESULT L586 (Theorem A, area law for beta_W below 2/3; strong coupling only). Entanglement: `gap-compress-opus.md` L137 (group-blind, no decay in distance); `prior/gap-kflow-read-opus.md` L108-111 (entropic a-theorem: blind); row 839 (seed = chi-square mutual information of slices) | blind | nothing new found |
| Kogut-Susskind Hamiltonian, Gauss law | `prior/gap-outside-read-opus.md` (5 hits), `gap-transfer.md`, `gap-global-reform-max.md` (Gauss law, 7 hits) | used as a frame, no gap statement | a spectral statement in the Kogut-Susskind or electric (spin-network) frame |
| Modular nuclearity (Buchholz and Wichmann; Buchholz, D'Antoni, Longo), split property | `prior/gap-seed-lit.md` L79, L115 ("No lattice nuclearity route was found"); no hit for "split property", Tomita, Bisognano, Reeh, Doplicher, Longo | not attempted | open to this row |
| Haag-Kastler locality, scaling limits | `gap-compact-rigidity-max.md` L88-106 (Tanimoto 2014; Buchholz and Fredenhagen 1977, recalled; Buchholz and Verch 1995): a conformal limit with massless particles is free part times a rest, "This is the product of Lemma PT" | precedent only | nothing new found |
| Corner transfer matrices (the lattice form of the modular operator of a wedge) | `gap-constraints-max.md` L139, L217 (A7: "its spectrum is the entanglement spectrum of a half-space, not the mass ... Not worth a lane") | dead | not redone |
| Gribov region, fundamental modular region (Gribov; Zwanziger; Dell'Antonio and Zwanziger) | `gap-coulomb-frame.md` (Lemma UNIQ: no Gribov copies near the trivial pin), `prior/gap-coulomb-frame-read-luna.md` (11 hits), `prior/gap-lit-commutator.md` (4), `gap-global-reform-max.md` (4) | used for frames at a pinned cell (route (ii)); no convexity or measure statement | convexity of the region and the Faddeev-Popov weight as a measure statement |
| Uhlenbeck compactness | hard-core files (`lattice-uhlenbeck.md`, `seam-nlpay.md`); `gap-coulomb-frame.md`; Kenig-Merle compactness of the datum (rows 1017, 1028) | compactness is done on the datum, soft rigidity FAILS | not redone |
| Yang-Mills gradient flow, Wilson flow | `prior/gap-outside-read-opus.md` L479-531 (topic F: "gradient flow and stochastic quantisation as monotones") | a monotone needs the sign of the non-perturbative beta function: renames (CAS) | not redone |
| Morse theory on the space of connections; Witten Laplacian | Witten Laplacian of the four-dimensional Langevin generator: `gap-brainstorm2-max.md` L257 (G2, W1 = -L + Ric + beta Hess S); Helffer-Sjostrand: `gap-pe-max.md` L413-471. **No hit** for Chern-Simons, Floer, Kodama, Nicolai, Parisi-Sourlas, "supersymmetric quantum"; "self-dual" occurs only for flux sectors ('t Hooft) and for the Villain mixed action | the physical Hamiltonian as the Witten Laplacian of the Chern-Simons functional is not on file | **open to this row (idea C4 below)** |
| Character expansions, Plancherel, class functions | `gap-means-max.md`, `gap-vir-sc.md`, `gap-wall-max.md`, `gap-q8test-opus.md`; random surfaces with signs (`gap-skeleton-max-b.md` L430, per row 1031's table); field-strength (Bianchi) formulation: `gap-pca-opus.md` (17 hits), `gap-global-reform-max.md` (13) | expansions carry signs; Bianchi reformulations FAIL (row 1016) | positivity statements of a new kind only |
| Instantons, pi_3, theta | K8 (instanton and refilling); Lemma TWIST (winding twists of Dirichlet data are removable); `sector-values.md`; `gap-brainstorm-max.md` (5 hits); theta: 8 scattered hits, no tool | no tool | theta as a spectral parameter |
| 't Hooft flux, twists, vortices, monopoles | rows 661-995 (heavily covered: `prior/gap-lit-flux.md`, `gap-flux-exercise.md`, `gap-means-max.md` Theorem R, `gap-short-step-max.md` (T-vor), `gap-cr-tomboulis-max.md`) | open items (TB)_n, (SER), (SPR) | not redone |
| Interaction measure, trace anomaly, pressure | `gap-phys-seed.md` L195, L224, L351 ((MONO-Delta): D(n; beta) non-decreasing in beta is the positivity of the interaction measure on the symmetric torus); `gap-direction-max.md` L197-207 ((ANOM)); `gap-mid-max.md` L184; `prior/gap-mono-lit.md` | route RB, blocked-equivalent | not redone |

### 2.3 Duplicate check for the open lemmas (rule 0a)

`library/open-core.md` has no entry for (W), (BDD-Delta), (LIOU) or any gap-lane item (`gap-dichotomy.md` L362 says the same; re-checked by grep of "BDD", "LIOU", "PHYS-SEED" in `open-core.md`: see Section 2.4). Rows 1034-1046 hold route (ii) (frames at a pinned cell: (SYM), (REG), O1, O2, (O2-min)); this row does not touch them. (TB)_n is held by row 1025, (SER), (SPR), (FL), (DEC) by row 1018, (PLATEAU) by row 1028, (E0-tor) by row 993, the unit-level log-Sobolev inequality by row 1021. No idea below attacks one of these under its own name; where an idea ends at one of them, the match is named and the idea stops there.

### 2.4 Result of the open-core grep

`grep -n -i -E "BDD|LIOU|PHYS-SEED|\(W\)|gap-" library/open-core.md` gives one line, and it is not an entry for a gap-lane item (the line is quoted in the run log of this step; see the command output). "mass gap", "gap lane" and "Casimir" give no line. So no row of `open-core.md` covers (W), (BDD-Delta) or (LIOU).

## 3. Ideas from quantum many-body theory, quantum information and operator algebras (step 3)

Format of each idea: source in its field; mechanism; the exact statement it needs on the 4D SU(2) lattice; its consumer in the chain. Kills are in Section 5. Sources are RECALLED unless Section 8 lists them as fetched. "The vacuum form" below means: the top eigenvector Omega_B of T_B is strictly positive (Perron-Frobenius, input 1 of `gap-dichotomy.md` 4.1), so P_B := Omega_B^(-1) (T_B/lambda_0) Omega_B is a Markov operator, reversible for nu_B := Omega_B^2 dU, and 1 - P_B is non-negative, kills the constants and has gap 1 - exp(-m(B)).

### B1. A dispersion dichotomy from frustration-free gap thresholds

- Source. Knabe (1988); Gosset and Mozgunov (2016); Lemm and Mozgunov (2019); Anshu (2020); the bounds z at least 2 for gapless frustration-free systems (Masaoka, Soejima and Watanabe, 2024). Common content: for a frustration-free Hamiltonian of finite range, if the gap of the open patch of side n exceeds a threshold of order n^(-2) (up to logarithms; Knabe's own threshold is of order 1/n), the infinite system has a gap. So a gapless frustration-free system has patch gaps O(n^(-2)): no relativistic dispersion.
- Mechanism. The vacuum form 1 - P_B is frustration-free. A model in branch (III) with a massless particle has patch gaps of order 1/n. If the vacuum form were a sum of finite-range terms that commute at a distance, order 1/n would exceed the threshold, and the model would have a gap: a contradiction. So branch (III) with relativistic dispersion would be excluded for every model whose vacuum form is local.
- Statements needed. (FF-loc): there are R and operators h_x >= 0 on L2(nu_B), each killing the constants, h_x acting on the links within distance R of x, with [h_x, h_y] = 0 for dist(x, y) > 2R, and c (1 - P_B) <= sum_x h_x <= C (1 - P_B), uniformly in B and in j (R in physical units). (PATCH-z): the sum of the h_x over a cube of side n has gap at least c' n^(-2+delta) for one delta > 0.
- Consumer. A uniform gap of all large cubes, which is (Z-UNB); with (BDD-Delta) it gives (W) by Theorem ZD-c.

### B2. The exact Lieb-Robinson cone of the transfer step and a local-to-global principle

- Source. Lieb and Robinson (1972); Hastings and Koma (2006); Nachtergaele and Sims (2006): a gap and a finite group velocity give exponential clustering.
- Mechanism. T_B = exp(-V/2) K exp(-V/2), K a product of one-link convolution operators, V a sum of plaquette multiplication operators. So T_B^k moves an observable of a region X into the k-neighbourhood of X: the cone is exact, with velocity one. The theorems above go from the gap to clustering. The use here would be the converse on one box: a lower bound on the energy of every state that differs from the vacuum only inside a cube.
- Statement needed. (LOC-eps): there is a function eps(R) with R eps(R) unbounded, such that for all large j every unit vector of L2(nu) orthogonal to the constants and of the form f Omega, f a function of the links of one cube of physical side R, has energy at least eps(R) in units of 1/R.
- Consumer. With the exact cone, (LOC-eps) would bound the gap of every larger cube from below: (Z-UNB).

### B3. The entropic certainty relation of the Gauss-law centre

- Source. Casini, Huerta, Magan and Pontello (2019-2021), entropic order parameters; the index of an inclusion (Jones; Pimsner and Popa; Longo). For a ring-shaped region R of the three-dimensional lattice and its complement R', the algebra generated by the local gauge-invariant operators of R is smaller than the commutant of that of R': the difference is the Wilson loop around the ring (for R) and the 't Hooft loop (for R'). For SU(2) the dual pair is the centre Z_2 and its dual, and the certainty relation reads S_R(omega || omega E_W) + S_R'(omega || omega E_T) = log 2, E_W and E_T the conditional expectations that remove the two loops.
- Mechanism. An exact identity at every coupling that ties the Wilson order parameter to the 't Hooft disorder parameter. It is the entropy form of 't Hooft's duality.
- Statement needed. The first relative entropy tends to 0 with the ring size along the trajectory (then the second tends to log 2: full disorder, heavy flux).
- Consumer. The flux half of (Z-UNB) only (L E_e(L) unbounded for the seven flux sectors).

### B4. The vacuum as a hidden Markov field: conditional mutual information and recovery

- Source. Petz recovery; Fawzi and Renner (2015); Brandao and Kastoryano (2019), finite correlation length and preparation of thermal states; Kato and Brandao (2019). In the classical case: a measure with small conditional mutual information I(A : C | B) across collars B is close to a Gibbs measure of a local potential.
- Mechanism. The four-dimensional Wilson measure is Markov across hyperplanes; its time-zero marginal nu is a hidden Markov field. If nu is approximately Markov across collars, then log Omega is a sum of quasi-local terms, which is (FF-loc) of B1 in a weak form.
- Statement needed. (CMI): I_nu(A : C | B) <= C_0 (area of the boundary of A) exp(-d/xi) for a collar B of width d, uniformly in j, with xi a physical length.
- Consumer. (FF-loc) of B1.

### B5. Lattice nuclearity: the Casimir free energy as four thermal free energies

- Source. Buchholz and Wichmann (1986), the nuclearity condition; Buchholz, D'Antoni and Longo (1990), modular nuclearity; Buchholz and Junglas (1989), nuclearity and thermal equilibrium states; Bros and Buchholz (1994), the relativistic KMS condition (analyticity of thermal functions in space-like directions; on a hypercubic torus it is the exchange of two sides, the symmetry (E1) of the engine).
- Mechanism. The nuclearity index of the map A -> exp(-t H) A Omega on the algebra of a cube counts the states of the cube with energy up to 1/t. On the torus this count is the thermal sum. With the symmetry (E1), the Casimir energy of the cube is again a thermal quantity of a longer box. Iterating: D(a) = G_0(a) + G_1(a) + G_2(a) + G_3(a), where G_i(a) is a^i times the thermal free energy, per unit i-volume and at the time a, of the system that is infinite in i directions and periodic with side a in the other 3 - i directions (Lemma NUC-4; statement and proof in Section 7, if it is ranked).
- Statement needed. (NUC): there is D_0 such that each G_i(L/a_j) is at most D_0/4 for all large j and all large L in P. In words: the Stefan-Boltzmann bound at the temperature 1/L, in each of the four geometries.
- Consumer. (BDD-Delta), which no row attacks (`gap-dichotomy.md` L362).

### B6. Dilation covariance: massless particles of a scale-invariant net are free

- Source. Buchholz and Fredenhagen (1977), dilations and interaction; Tanimoto (2014), massless particles in a conformal Haag-Kastler net generate a free subnet, and a scalar free subnet is a tensor factor; Weinberg and Witten (1980). On file as precedent: `gap-compact-rigidity-max.md` L88-106 (row 1017, A10, A13).
- Mechanism. A uniformly recurrent critical element is a candidate scale-invariant limit. If it is a local net with a dilation symmetry and has massless particles, its particle content is a free field, and the element is a product of a free part and a rest.
- Statements needed. (NET): each uniformly recurrent element of Omega(D_0) is the torus datum of a Haag-Kastler net with a unitary dilation by a factor 2^t for one t. (PART): that net has a massless one-particle state, or it is a constant log m. (NOFREE): no limit of Wilson SU(2) along the trajectory contains a free massless subnet, and no constant log m with m at least 2 occurs.
- Consumer. (LIOU); with (BDD-Delta) it gives (W) by Theorem CR.

### B7. The relativistic KMS condition as a second engine (kept as a remark, not counted)

The engine of the lane (Theorem S) is a finite-size criterion of Knabe type that uses only (E1)-(E3). In the language of this field it is the relativistic KMS condition of Bros and Buchholz on the torus. I found no second engine in the operator-algebra literature that reads more than (E1)-(E3) without reading the dynamics. This is recorded so that the next row does not look for one there.

## 4. Ideas from geometric analysis, harmonic analysis on SU(2) and topology (step 4)

Notation for this section. A link variable is a unit quaternion U = a_0 + i a.sigma, (a_0, a) in R^4, a_0^2 + abs(a)^2 = 1. The class angle theta in [0, pi] of U is given by a_0 = cos(theta). Haar measure on class functions is (2/pi) sin^2(theta) d theta (Weyl).

### B8. Convexity of the fundamental modular region and of the Faddeev-Popov weight

- Source. Gribov (1978); Zwanziger (1982-1994), the fundamental modular region and the horizon; Semenov-Tyan-Shanskii and Franke (1982); Dell'Antonio and Zwanziger (1989, 1991): every gauge orbit meets the fundamental modular region, which is convex and bounded in every direction. Convex-measure tools: Brascamp and Lieb (1976); Payne and Weinberger (1960).
- Mechanism. Minimal Landau gauge on the periodic lattice: maximise F_U(g) = sum over links of (1/2) tr(g_x U_xy g_y^(-1)) over gauge maps g. For fixed g the map U -> F_U(g) - F_U(1) is linear in the ambient coordinates (a_0, a) of the links. So (i) the fundamental modular region Lambda = {U : F_U(1) >= F_U(g) for all g} is the product of spheres cut by a convex cone of (R^4)^E; (ii) the gauge condition (lattice divergence of a = 0) is linear in a; (iii) the Faddeev-Popov operator M(U) (the Hessian of -F_U at g = 1) is linear in (a_0, a); in the chart a (upper hemispheres a_0 > 0) the map a -> M is operator concave, so log det M is concave on the Gribov region, and Lambda is convex there. A convex region with a log-concave weight is the setting of Brascamp and Lieb. A Poincare inequality in the chart passes to gauge-invariant functions, because the chart gradient of an invariant function is a projection of its full gradient.
- Statement needed. (FMR-cvx): there are a chart of Lambda and kappa > 0, independent of the torus, such that the gauge-fixed four-dimensional measure (Haar times det M times the Wilson weight) has a density exp(-Phi) with Hess(Phi) at least kappa on the chart image of Lambda, at the couplings of the band.
- Consumer. A Poincare inequality of the four-dimensional measure on gauge-invariant functions with a volume-free constant; this is a unit-level functional inequality of route RF ((U2) of row 982), which with (TH) gives (W).

### B9. Operator Jensen for the Faddeev-Popov operator

- Source. Zwanziger (2003), "no confinement without Coulomb confinement"; Gribov (1978); the operator Jensen inequality (Hansen and Pedersen) and the Kadison-Schwarz inequality.
- Mechanism. On the Gribov region M(U) >= 0 and M is linear in (a_0, a). For a gauge-fixed measure that is invariant under global colour rotations and lattice symmetries, the mean of M is u_0 (-Laplace) with u_0 the mean of a_0 over a link. The inverse is operator convex, so mean(M^(-1)) >= (u_0 (-Laplace))^(-1) off the constants: the ghost propagator is enhanced at every coupling, an exact inequality. In the same way mean(M^(-1) (-Laplace) M^(-1)) >= mean(M^(-1)) (-Laplace) mean(M^(-1)): the colour-Coulomb kernel dominates.
- Statement needed. An implication from an infrared enhancement of mean(M^(-1)) (the horizon condition) to the decay of gauge-invariant correlations. Zwanziger's inequality goes the other way (the Coulomb potential bounds the Wilson potential from above), so it gives a necessary condition for confinement only.
- Consumer. None found.

### B10. The Hamiltonian as the Witten Laplacian of the Chern-Simons functional; the stochastic anti-self-duality equation; an imaginary theta

- Source. Chern and Simons (1974); Witten (1982), supersymmetry and Morse theory, and (1988), topological field theory; Floer (1988); Atiyah and Bott (1983); Nicolai (1980); Parisi and Sourlas (1979); Baulieu and Singer (1988); Vafa and Witten (1984). This frame has no hit in the lane (Section 2.2).
- Mechanism (continuum, formal). In temporal gauge H = (g^2/2) E^2 + (1/(2 g^2)) B^2 and B = grad CS, CS the Chern-Simons functional of the spatial connection. Put Q = g d/dA + B/g. The trace of the Hessian of CS is zero, so H = (1/2) Q* Q: the Hamiltonian is the Witten Laplacian on functions of the "Morse function" CS. The formal zero mode exp(-CS/g^2) is not normalisable and not invariant under the gauge maps of winding number one, so E_0 > 0; the form d CS is closed on the orbit space and not exact (its period is 8 pi^2: pi_3(SU(2)) = Z). Consequences, all formal: (a) exp(-t H) = exp(-CS/g^2) P_t exp(CS/g^2), where P_t is the Markov semigroup of the stochastic equation dA/dt = -B(A) + g (white noise), the noisy anti-self-duality equation; (b) the Euclidean measure is the path measure of that equation times exp(-(8 pi^2/g^2) Q_top): Yang-Mills at the imaginary angle theta = i 8 pi^2/g^2 (= 2 pi^2 beta i for beta = 4/g^2) is a causal stochastic equation, and Z(theta) is the generating function of the winding of that diffusion at a complex argument; (c) E_0(theta) is the large-deviation function of the winding number.
- Why it looked promising. The structure uses dimension four (self-duality of 2-forms), a Lie group with pi_3 = Z (not U(1), not a finite group), and it is exact. It is the only object I found that meets K5, K6 and K7 by its definition.
- Statements needed. (CS-lat): a lattice form, that is a closed and not exact gauge-invariant 1-form omega on the space of spatial link configurations with (1/2) abs(omega)^2 - (1/2) div omega equal to the Wilson potential up to a constant. (CS-carry): a carrier from theta = 2 pi^2 beta i to theta = 0 for the gap.
- Consumer. With both: the gap as the spectral gap of a non-reversible diffusion, a new object for (W). Without (CS-lat): none on the lattice.

### B11. Monotonicity of the Yang-Mills heat flow in dimension four (on file; not counted)

Hamilton (1993), Chen and Shen (1994), Struwe (1994) for the monotonicity formula; Uhlenbeck (1982) for epsilon-regularity; Luscher (2010) for the lattice flow. For a translation-invariant random field the formula reduces to "the mean flowed energy e(t) does not increase", which holds for every group. A one-sided bound on t^2 e(t) is the sign of the non-perturbative beta function in the flow scheme: (CAS) or (DRIFT) renamed. On file: `prior/gap-outside-read-opus.md` L479-531 (row 1005, topic F). Not redone.

### B12. The class-angle density of states: SU(2) gauge theory as a positive model on a polytope of spherical polygon inequalities

- Source. Weyl's integration formula; the product of two conjugacy classes of SU(2) (elementary); Witten (1991), volumes of moduli spaces of flat connections; Jeffrey and Weitsman (1992), bending flows and the toric structure; Kapovich and Millson (1996), polygon spaces; Agnihotri and Woodward (1998); Duistermaat and Heckman (1982); Prekopa (1973) and Brunn-Minkowski for marginals of log-concave measures. Row 1016 used Goldman and Jeffrey-Weitsman as a lens for twist flows (`gap-global-reform-max.md` L152); the measure statement below is not there.
- Mechanism. The Wilson weight depends on the plaquette class angles only. So Z(n; beta) is the integral of rho_n(theta) exp(beta sum cos theta_p) over [0, pi]^P, with rho_n the push-forward of Haar measure to the plaquette class angles: a positive density that does not depend on beta, and the whole datum of the engine is a function of the family rho_n. For two independent Haar elements with class angles theta_1, theta_2, the class angle theta_12 of the product has cos(theta_12) uniform on [cos(theta_1 + theta_2), cos(theta_1 - theta_2)]. So the joint density of (theta_1, theta_2, theta_12) is (2/pi^2) sin theta_1 sin theta_2 sin theta_12 on the convex polytope of the spherical triangle inequalities. Iterating along a fan of triangles: for one cube with free boundary (which is two-dimensional Yang-Mills on a sphere of six plaquettes), the six plaquette angles and three diagonals have the density const times the product of sin theta_p exp(beta cos theta_p), on a convex polytope, uniform in the diagonals. Each factor sin(theta) exp(beta cos theta) is log-concave on [0, pi] if and only if beta <= 3 sqrt(3)/2 = 2.598...; the marginal on the six plaquette angles is then log-concave (Prekopa). For U(1) the class map is the identity and the constraint set is a union of affine lattices; for a finite group the classes are discrete. So the structure is selective in the group, and its range covers beta 2.3 to 2.598 for the sphere.
- Statement needed. (LC-rho): for the four-dimensional torus, rho_n(theta) exp(beta sum cos theta_p) is log-concave on a convex support, with a strict constant kappa > 0 free of the volume, and -log rho_n is a sum of terms of bounded range up to exponentially small tails, at the couplings of the band.
- Consumer. Brascamp-Lieb and Helffer-Sjostrand bounds for functions of the plaquette angles, volume-free: decay of plaquette-angle correlations and a unit-level functional inequality (route RF), then (W) with (TH).

### B13. Clebsch-Gordan screening: no flux tower

- Source. Clebsch-Gordan decomposition and Peter-Weyl; the massless floor of the lane (row 988, Lemma FLOOR) for the abelian flux tower.
- Mechanism. For U(1) the electric flux through a cross-section of the 3-torus is an integer that commutes with the transfer operator; in the Coulomb phase its sectors have energies of order e^2 g^2/L and give a term of order one to the thermal sum at every size. For SU(2), chi_(1/2)^2 = 1 + chi_1: two fundamental fluxes fuse to the vacuum with weight 1/4, the flux is conserved modulo 2 only, and the transfer operator commutes with the eight centre fluxes only.
- Statement needed. (FUSE): a lower bound, uniform along the trajectory, on the rate at which a state with a flux of spin one through a cross-section loses its overlap with every such state after a time of the order of the side, in terms of the fusion weight 1/4.
- Consumer. The absence of a tower in the centre-even sector; at best one term of the even thermal sum.

### B14. Theta as a Bloch parameter and as the only frame-free twist

- Source. Vafa and Witten (1984), Z(theta) <= Z(0); Seiler and Stamatescu (the charge density is odd under reflection, so its two-point function is negative at separated points, by reflection positivity); Luscher (1982), the geometric charge on admissible lattice fields; Gaiotto, Kapustin, Komargodski and Seiberg (2017), the anomaly at theta = pi.
- Mechanism. Route (ii) of the lane needs a colour frame because a non-abelian twist of the links is not gauge invariant (rows 1026-1046). Theta couples to a gauge-invariant local density, so its response needs no frame. It exists for no abelian and no finite group, and only in dimension four. In a small box the theta-stiffness K(L) = -log(Z_L(pi)/Z_L(0)) is of order exp(-2 pi^2 beta(L)); by asymptotic freedom it grows like (L Lambda)^(22/3) (dilute instantons, RECALLED), and then like L^4. A scale-invariant element has a constant K.
- Statements needed. (TH-lat): a reflection-positive lattice form with exact charge sectors that is the Wilson measure, or agrees with it along the trajectory up to errors that vanish with the spacing. (TH-step): K(2L) >= min((1 + delta) K(L), K_0) on the band. (TH-all): large K at one size gives the seed.
- Consumer. (W) through (TH-all).

### B15. A barrier at the weak-coupling end for the Casimir free energy

- Source. The Morse-Bott structure of the Wilson action on a torus: its minimum set is the set of flat connections (torons); Luscher (1983), van Baal (the small-volume expansion); Lemma FV of row 1028 (the free value of D is infinite, D >= (3/2) log beta - 59 n^4 - 11); Proposition MB of row 720 ((MONO-Delta) with (BASE-Phi) and (APR) gives (BDD-Delta)); the maximum principle as a pattern.
- Mechanism. Every known way to an unbounded Casimir free energy is a flat compact direction whose effective coupling tends to zero with the size (torons of an infrared-free gauge theory; the order parameter of a broken continuous symmetry). In four dimensions the Gaussian point repels in the infrared: where the running coupling at the size L is small, it is larger at 2L, the toron valley is narrower, and D falls. So D cannot rise through a high level. Lemma BAR (Section 7): given D^+ finite at one size, (BDD-Delta) holds if and only if there are D_* and L_1 with: D^+(L) >= D_* implies D^+(2L) <= D^+(L), for all L >= L_1 in P. (Low levels are held by D(2a) <= 16 D(a).) This asks for monotony at high levels only, where (MONO-Delta) asks for it everywhere; (MONO-Delta) fails in the class at low levels (Ising, `gap-phys-seed.md` L361-373).
- Statements needed. (INV): for each g_* > 0 there is D_* such that D_j(n) >= D_* forces the torus of side n at beta_j to be in the weak-coupling domain of the account at the scale n, with running coupling at most g_*. (UV-Cas): in that domain D_j(2n) <= D_j(n).
- Consumer. (BDD-Delta), which no row attacks.

### B16. A holomorphic vacuum (lens found empty; not counted)

Hall (1994), the Segal-Bargmann transform for compact Lie groups; Kempf and Ness; Fricke and Vogt for trace coordinates. The Wilson kernel exp((beta/2) tr U) is entire on SL(2, C), so every eigenfunction of T_B with a non-zero eigenvalue, the vacuum included, extends to an entire function on SL(2, C)^E that is invariant under complex gauge maps: a function of the trace coordinates on the SL(2, C) character variety of the lattice. The same holds for U(1) with C^*. A gap statement would have to come from a zero-free complex neighbourhood of uniform width, which is a Lee-Yang statement; that route was tried in row 1004 (Lemmas LYP, LYP2: false for one plaquette). No statement of this lens passes K5. No hit in the lane for Segal-Bargmann or Hall.

## 5. Kill fast (step 5)

Counted ideas: B1-B6, B8-B10, B12-B15 (thirteen). Not counted: B7 (a remark), B11 (on file), B16 (empty lens). Each test is used in the valid form of Section 2.1. Marks: PROVED = a written hand proof is in Section 7 of this file or is cited by file and line; ARGUED = reasoned here, not proved; RECALLED = a literature statement not re-read in this run. Nothing here is checked by another model.

| # | Idea | First test that kills it | The kill, in one or two sentences | Other tests | Verdict |
|---|---|---|---|---|---|
| B1 | frustration-free thresholds, z at least 2 | K9 (S0) | (FF-loc) with a physical range R is exponential clustering of the vacuum measure in a stronger form; no theorem gives it without the gap, and nothing here supplies it. In the free photon the vacuum form has a kernel of power-law range and patch gaps of order 1/n with no gap, so a Knabe threshold cannot hold for forms of power-law range: locality is the whole content (ARGUED). | K5: (FF-loc) is false for the photon, as it must be; a constraint only. (PATCH-z) is open too. | FAILS (ARGUED): blocked, terminal obligation not weaker than the target |
| B2 | exact Lieb-Robinson cone | K9 (S0) | At R equal to the side of the box, (LOC-eps) says L m(L) is unbounded: it is (Z-UNB) word for word. For R below the side no step from local states to the first excited state is known. The cone is the same for every model with a transfer operator. | K5: blind | FAILS (ARGUED): renames (Z-UNB) |
| B3 | entropic certainty relation of the centre | K6 | The dual pair is the centre Z_2 and its dual. The relation is the same for frozen Z_2, and Q_8 and 2T have the same centre. It reads the centre-charged loops only (K1). Its consumer is the flux half, where Theorem R of `gap-means-max.md` is the lane's means. | K9 (S0) for the flux half | FAILS (ARGUED; the relation itself is RECALLED, not rebuilt) |
| B4 | hidden Markov vacuum, recovery | K9 (S0) | (CMI) with an exponential rate is quasi-locality of log Omega, which is (FF-loc): clustering renamed. For the photon it holds with a power law only. | - | FAILS (ARGUED) |
| B5 | lattice nuclearity | K9 (S0) | By Lemma CHAIN-4 (Section 7.2, PROVED) D = G_0 + G_1 + G_2 + G_3 with all terms non-negative, so (NUC) is (BDD-Delta) exactly. Nuclearity is an assumption in its own field; it is derived for free fields and some integrable models only (RECALLED). No mechanism. | K7: in five dimensions at weak coupling (BDD-Delta) fails through G_0 (GUIDE, row 1028) | FAILS as a route (renames). Lemma CHAIN-4 stays as an exact form of (BDD-Delta) |
| B6 | dilations: massless particles are free | K1 | A free massless part times a rest is the product of Lemma PT; (NOFREE) is the selective statement and has no supplier. (NET) is not available: a critical element is a function on dyadic tori, and a uniformly recurrent element need not be scale invariant. (PART) is false for scale-invariant theories without particles and for the constants log m. An emergent photon is not excluded by kinematics (the Coulomb phase of the Georgi-Glashow model, RECALLED). | on file as precedent (row 1017 A10, A13) | FAILS (ARGUED) |
| B8 | convex modular region, Faddeev-Popov weight | K5 | For compact U(1) the Faddeev-Popov operator is the Laplacian with conductances cos(theta_l); it is concave in theta, and -log det M = const + ((N - 1)/(2 d N)) sum theta_l^2 + O(theta^4) (Lemma FP-U1, Section 7.4, PROVED). So the convex gain is not zero for an abelian group. The non-abelian part (the ghost loop) is of order one and does not grow with beta, while the Wilson action has negative curvature of order beta at plaquette angles above pi/2, which occur in Lambda. So (FMR-cvx) holds below a ceiling in beta at best (ARGUED). | K7: no input from the dimension. K3: a pointwise Hessian bound is a supremum over fields. Also: in the chart a the Haar density is log-convex. | FAILS (K5 part PROVED; ceiling ARGUED) |
| B9 | operator Jensen for M | K5 | The same inequality holds for compact U(1), with mean M = (mean cos theta)(-Laplace). No implication to a gauge-invariant decay exists; Zwanziger's inequality gives a necessary condition for confinement only. | no consumer | FAILS (ARGUED) |
| B10 | Chern-Simons Witten Laplacian, imaginary theta | K8 | On the lattice every gauge-invariant closed 1-form on the configuration space is exact with an invariant potential, and the only factorisation H = E + (g^2/2) Q* Q with Q = grad + omega, omega closed, is the ground-state transform, E = E_0 (Lemma NOCS, Section 7.3, PROVED). So (CS-lat) is impossible: the structure exists only where the gauge group has maps of non-zero winding. (CS-carry) has no tool; at beta = 2.3 the angle is 2 pi^2 beta = 45.4. | K5: the factorisation holds for U(1); only the non-exactness is non-abelian | FAILS (lattice part PROVED) |
| B12 | class-angle density of states | K7 | Nothing in (LC-rho) reads the dimension. At large beta the measure sits where rho_n is its flat limit, the push-forward of three free fields to the norms of their plaquette values: massless in every dimension. A volume-free strict log-concavity with locality would give decay there in five dimensions too. The exact convex structure is PROVED for surfaces only (Proposition SPH, Section 7.5), which is two-dimensional Yang-Mills, solvable and on file. Where a group element enters two relations the density has Gram-determinant factors (ARGUED). | K5, K6 pass (the structure is selective in the group) | FAILS (ARGUED) |
| B13 | Clebsch-Gordan screening | K6 | Q_8 and 2T have the same fusion (for Q_8 the square of the two-dimensional representation is the sum of the four one-dimensional ones). The idea uses non-commutativity, not the Lie algebra. Its consumer is one term of the even sum. | no chain | FAILS (ARGUED) |
| B14 | theta as the frame-free twist | K8, then K1 | The Wilson lattice has no charge sectors (Lemma TWIST on file; Lemma NOCS). A lattice form with sectors is another measure. (TH-all) is false in the class: the product of SU(2) with a no-seed neutral factor has the same K(L) (Lemma PT). No symmetry acts on the local gauge-invariant observables, so the step from one sector to all observables has no mechanism. (TH-step) is a one-sided step of the kind of (CAS) for a new quantity. | K5, K6, K7 pass | FAILS (ARGUED) |
| B15 | barrier at the weak-coupling end | K9 (S0) for the barrier alone | By Lemma BAR (Section 7.1, PROVED) the barrier statement alone is equivalent to (BDD-Delta) given (FIN): a new name. The content is (INV) and (UV-Cas). (INV) is a statement on every way in which D can be large; in the abstract class it is false (a product with a factor of unbounded D re-grows; ARGUED given such a factor). (UV-Cas) needs D to an error of order one on two tori at weak coupling; the account gives order one for each unit cell (`gap-phys-seed.md` Proposition 1.1), and the comparison of two tori is the open (E0-tor). | K7 passes in the valid form: (UV-Cas) is false in five dimensions | wounded: two named gaps, (INV) with no route, (UV-Cas) at the grade of (E0-tor). Not a survivor. |

**Count.** Thirteen ideas: twelve FAIL, one (B15) is wounded with two named gaps and no route to the first. No idea survives. Reasons by kind: renames the crux or an equivalent of it (B1, B2, B4, B5; B15 without (INV)); reads the centre or one sector only (B3, B13, B14); blind to the group at the order where it gains (B8, B9); no lattice form (B10); no input from the dimension (B8, B12); needs the product to be excluded (B6, B14).

**A pattern worth recording (reading).** In these five fields every exact structure is of one of two kinds. (a) It holds for every model with a transfer operator (Lieb-Robinson, nuclearity as a count, certainty relations, Jensen for M, the holomorphic vacuum): blind. (b) It is selective in the group and exact, but lives on a surface or in the continuum (the polytope of class angles on a sphere; the Chern-Simons form with its period): the lattice in dimension four does not have it. I found no structure that is exact on the four-dimensional lattice, selective in the group, and reads the dimension.

## 6. Ranking (step 6)

No idea survives the kill tests, so there is no ranking of survivors. The table ranks the least dead by what they would change divided by the cost to find out (exercise skill, step 7; registry words of the proof-search governance).

| Rank | Idea | Family (object; mechanism; terminal obligation) | Strength against the target | Status | What it would change | Cost to find out | First artifact | Stop or reopen condition |
|---|---|---|---|---|---|---|---|---|
| 1 | B15 barrier | Casimir free energy on physical sizes; maximum principle at high level from asymptotic freedom; (INV) and (UV-Cas) | weaker ((BDD-Delta) only) | blocked-local | (BDD-Delta), one half of the trichotomy, from weak-coupling data; branch (II) would be excluded | high: (INV) has no route | Lemma BAR (done, 7.1) | reopen on a characterisation of large D in pure SU(2) (an inverse of Lemma FV uniform in the size), or on (E0-tor) at weak coupling |
| 2 | B5 nuclearity | the datum; the chain of four partial infinite-volume limits; (NUC) | target-equivalent to (BDD-Delta) | blocked-equivalent | the exact content of (BDD-Delta): one count of states of the cube and three bulk thermal terms | low: done here | Lemma CHAIN-4 (done, 7.2) | reopen on a bound for one of G_0, ..., G_3 from the account |
| 3 | B10 Chern-Simons | spatial connections; Witten Laplacian of a closed form with a period; (CS-lat), (CS-carry) | unknown | retired on the lattice | a new object for the gap in the continuum only | low for the lattice verdict: done here | Lemma NOCS (done, 7.3) | reopen only with a continuum existence chain that keeps large gauge maps |
| 4 | B12 class angles | plaquette class angles; convex polytope and log-concavity; (LC-rho) | stronger | retired | a one-scale property with a number (3 sqrt(3)/2) on the band | moderate | Proposition SPH (done, 7.5) | reopen on a positive convex structure for complexes that are not surfaces |
| - | B1, B2, B4 | vacuum form; locality; clustering | stronger or equivalent | blocked-equivalent | - | - | - | reopen on a proof of quasi-locality of log Omega that does not use the gap |
| - | B3, B13, B14 | centre or one sector | weaker (flux half or one term) | retired | - | - | - | reopen on a step from one sector to all observables |
| - | B6, B8, B9 | - | - | retired | - | - | - | none |

The row asks for the first lemma of the top one or two. Section 7 gives them for ranks 1 and 2, and the proved parts of the kills of B10, B8 and B12.

## 7. First lemmas and proved kills (step 7)

All statements of this section are proved by hand by Claude Fable 5.2 and are not checked by another model. None of them moves (W). Inputs from the lane are cited by file and line with their standing; they are used as stated there.

**Standing inputs.** A datum is a positive function Z on quadruples of integers at least 3 with (E1) symmetry in the four sides, (E2) Z(k, B) = sum over r of lambda_r(B)^k with lambda_0 > lambda_1 >= ... >= 0, (E3) f = inf F(n)/abs(n) finite (`gap-dichotomy.md` 1.1). Lemma A (a): for a positive trace-class operator, k -> (Tr S^k)^(1/k) is non-increasing and tends to lambda_0 (`gap-crux-restate.md` L37; checked in rows 698, 699). Lemma K: the deficit of the ground level is non-negative, convex and non-increasing in one side (`gap-crux-restate.md` L178; same checks). Theorem D (a): Z((2n)^4) <= Z(n^4)^16 (same file L101). Theorems CE, CR and Proposition OM as written in `gap-dichotomy.md` 2.2 with the repairs of check 1019 (same-provider check only).

Two facts used several times.

- **(M1)** Put M(n) := Delta(n)/abs(n). Then M >= 0, M is symmetric, and M is non-increasing in each side. Proof. F(k, B)/k = log (Tr T_B^k)^(1/k) is non-increasing in k by Lemma A (a), so F(n)/abs(n) is non-increasing in the first side; by (E1) in each side; subtract f. M >= 0 by the definition of f. QED
- **(M2)** For a box B put c(B) := log lambda_0(B) - f abs(B) and g(k; B) := log(1 + S(k; B)). Then Delta(k, B) = g(k; B) + k c(B), g >= 0, g(k; B) is non-increasing in k, and c(B) = lim over k of Delta(k, B)/k = inf over k of Delta(k, B)/k >= 0. Proof. F(k, B) = k log lambda_0(B) + log(1 + S(k; B)) by (E2); S(k; B) is a sum of k-th powers of numbers in [0, 1). QED

I call c(B) the **deficit** of the box B (the Casimir energy with the sign reversed; it is kappa of Lemma K in two variables).

### 7.1 Lemma BAR (idea B15): (BDD-Delta) is a barrier at high level

Setting: a family with units under (S0), D^+ as in `gap-dichotomy.md` 1.2.

**Lemma BAR (PROVED).** Let L_1 in P with D^+(L_1) finite. These are equivalent.

1. (BDD-Delta).
2. (BAR): there are a number D_* and L_2 in P such that for every L >= L_2 in P: if D^+(L) >= D_*, then D^+(2L) <= D^+(L).

Also sufficient for (BDD-Delta), given D^+(L_2) finite: (BAR-lat): there are D_* and L_2 in P, and for each L >= L_2 in P an index j_0(L), such that for j >= j_0(L): if D_j(L/a_j) >= D_*, then D_j(2L/a_j) <= D_j(L/a_j).

Proof. Step 0: D(2a) <= 16 D(a) for every datum and a >= 3. Theorem D (a) gives F((2a)^4) <= 16 F(a^4); subtract 16 f a^4. So D^+(2L) <= 16 D^+(L).
(1) gives (2): let (L_0, D_0) be a bound, L_2 := L_0, D_* := D_0 + 1. The premise of (BAR) never holds.
(2) gives (1): we may take L_2 >= L_1 (enlarging L_2 keeps (BAR)). By Step 0, D^+(L_2) <= 16^k D^+(L_1) is finite, where L_2 = 2^k L_1. Put M_0 := max(D^+(L_2), 16 D_*). Claim: D^+(2^i L_2) <= M_0 for all i >= 0. For i = 0 it is the definition. If it holds for L = 2^i L_2: when D^+(L) >= D_*, (BAR) gives D^+(2L) <= D^+(L) <= M_0; when D^+(L) < D_*, Step 0 gives D^+(2L) <= 16 D^+(L) < 16 D_* <= M_0. So (L_2, M_0) is a bound of (BDD-Delta).
(BAR-lat): fix i >= 0 and let j >= max of j_0(2^i' L_2) over i' < i. The same induction, for the one datum Z_j, gives D_j(2^i L_2/a_j) <= max(D_j(L_2/a_j), 16 D_*). Take the upper limit over j. QED

What it says. (BDD-Delta) needs no control of D at low levels: the doubling bound holds them. It needs: D does not rise through a high level. (MONO-Delta) of row 720 asks for monotony everywhere and fails in the class at low levels; (BAR) is true in every model with bounded D (it is then empty) and false in every model with unbounded D. So (BAR) alone is (BDD-Delta) in other words. Its use is to say where a proof has to work: only at sizes where D is above an arbitrarily high level D_*.

What is missing for idea B15. (INV): D_j(n) >= D_* forces weak coupling at the scale n. (UV-Cas): at weak coupling D falls under doubling. Together they give (BAR-lat). I tried (INV) in three ways and each stops.

- From the abstract class: false. D adds over products (Lemma PT), so a product with a factor of unbounded D has large D with any behaviour of the other factor. (ARGUED: the lane holds no written model of the class with unbounded D at one coupling; a broken continuous symmetry is recalled, `gap-dichotomy.md` L368.)
- From Lemma CHAIN-4 below: D >= D_* gives one of four thermal terms above D_*/4. For the three bulk terms no statement ties a large value to weak coupling. For G_0 (the count of states of the cube below its inverse side) the only known source is the toron valley (Lemma FV), and no inverse of Lemma FV uniform in the lattice size is known.
- From Lemma DIL (row 720): D(n; beta) is the integral over the coupling of 6 n^4 times the finite-size shift of the mean plaquette. A large D says that the shift was positive on a long stretch of couplings; it does not say that the lattice at the last coupling is weakly coupled at the scale n.

So B15 stops at (INV): one precise lemma, with no route. It is not attacked further here.

### 7.2 Lemma CHAIN-4 (idea B5): the Casimir free energy is a sum of four thermal terms

For a >= 3 and i in {0, 1, 2, 3, 4} put

- m_i(a) := inf of M(k_1, ..., k_i, a, ..., a) over integers k_1, ..., k_i >= 3 (i sides are free, 4 - i sides equal a);
- Gamma_i(a) := a^4 m_i(a);
- for i <= 3: G_i(a) := Gamma_i(a) - Gamma_(i+1)(a);
- B_(i,k) := the box with i sides equal to k and 3 - i sides equal to a.

**Lemma CHAIN-4 (PROVED from (M1), (M2)).** For every datum and every a >= 3:

1. D(a) = Gamma_0(a) >= Gamma_1(a) >= Gamma_2(a) >= Gamma_3(a) >= Gamma_4(a) = 0.
2. D(a) = G_0(a) + G_1(a) + G_2(a) + G_3(a), and each G_i(a) is non-negative.
3. G_i(a) = a^i times the limit over k of k^(-i) g(a; B_(i,k)). In words: G_i is a^i times the logarithm of the thermal trace, per unit of i-volume and at the time a, of the system that is infinite in i directions and periodic with side a in the other 3 - i directions.
4. Gamma_1(a) = a c(a^3): the deficit of the cube times its side. Gamma_3(a) = G_3(a) is the dimensionless pressure pi(a) (Q4 of `gap-phys-seed.md` L195). G_0(a) = log(1 + S(a; a^3)).

Proof. By (M1) each infimum is a limit along k_1 = ... = k_i = k to infinity, and an infimum over more free sides is taken over a larger set that contains k_(i+1) = a. So m_0 >= m_1 >= ... >= m_4, and m_4 = inf of M = 0 by the definition of f. This is (1), and it gives G_i >= 0 and the telescoping sum (2). For (3): by (M2), g(a; B_(i,k)) = Delta(a, B_(i,k)) - a c(B_(i,k)). The torus (a, B_(i,k)) has i sides k and 4 - i sides a, so Delta(a, B_(i,k))/k^i = a^(4-i) M(k, ..., k, a, ..., a) tends to a^(4-i) m_i(a). Next c(B_(i,k))/k^i = inf over T of Delta(T, B_(i,k))/(T k^i) = a^(3-i) inf over T of M(T, k, ..., k, a, ..., a); it is non-increasing in k, and its limit is a^(3-i) times the infimum of M over i + 1 free sides (by (M1) the infimum over all tuples equals the infimum over tuples with equal entries). So k^(-i) g(a; B_(i,k)) tends to a^(4-i) (m_i(a) - m_(i+1)(a)), and a^i times this is G_i(a). (4): Gamma_1(a) = a^4 inf over T of M(T, a, a, a) = a inf over T of Delta(T, a^3)/T = a c(a^3) by (M2); the cases i = 0 and i = 3 of (3) give the other two. QED

**Corollary NUC (PROVED).** For a family with units: (BDD-Delta) holds if and only if there are L_0 in P and a number D_0' such that for i = 0, 1, 2, 3 and every L >= L_0 in P the upper limit over j of G_(i,j)(L/a_j) is at most D_0'. (Each G_i is at most D; and the upper limit of the sum is at most the sum of the upper limits.) So (NUC) of idea B5 is (BDD-Delta) exactly.

Reading (GUIDE, not used). In a box at weak coupling the logarithm of Lemma FV sits in G_0: it comes from constant modes, and a term that does not grow with the area does not enter a quantity per unit of length, area or volume. The three bulk terms tend to free-field values. So at the weak end (BDD-Delta) is a bound on the number of states of the cube below its inverse side.

Not new: (M1) is Lemma A with (E1); the bound g(a; b^3) <= (b/a)^3 D(a) is Proposition Delta (row 708); the monotony of the deficit in one side is Lemma K. New in the scope searched (Section 2; "per unit length", "per unit area", "infinite tube", "Casimir energy" give no hit in `gap-phys-seed.md`, `gap-mid-max.md`, `gap-afield-a-max.md`, `gap-crux-restate.md`, `gap-seed-shape.md`): the chain to the three partial infinite-volume limits and the exact sum.

### 7.2b Proposition CAS-0: a recurrent critical element with zero deficits is a constant; the ground-state form of the rigidity half

Setting: Omega(D_0), sigma, critical elements and uniform recurrence as in `gap-dichotomy.md` 1.4. For E in Omega(D_0) the spectral form holds in each direction, exp E(T, B) = sum over r of exp(-T e_r(B)), with e_0(B) finite and at most 0 and non-negative integer multiplicities (`gap-compact-rigidity-max.md` L175); E is symmetric; and E(x)/(x_1 x_2 x_3 x_4) is non-increasing in each side (it is (M1), a non-strict inequality between two values, kept by pointwise limits of the rescaled data). From the spectral form, -e_0(B) = lim over T of E(T, B)/T.

**Proposition CAS-0 (PROVED given Theorem CE (ii)).** Let E in Omega(D_0) be uniformly recurrent, and let e_0(b, b, b) = 0 for every b in DD. Then E is the constant log m for an integer m >= 2.

Proof. Step 1: e_0(B) = 0 for every box B in DD^3. Let b be the least side of B. By (M1) for E, E(T, B)/(T abs(B)) <= E(T, b, b, b)/(T b^3) for every T. Let T grow: -e_0(B)/abs(B) <= -e_0(b^3)/b^3 = 0. With e_0(B) <= 0 this gives e_0(B) = 0.
Step 2: E is non-increasing in each argument. In the first: E(T, B) = log of the sum over r of exp(-T e_r(B)) with all e_r(B) >= e_0(B) = 0. By symmetry in each.
Step 3: E(2^t x) = E(x) for every x in DD^4 and t in Z. Put h(t) := E(2^t x); by Step 2 it is non-increasing in t. Let eps > 0. By uniform recurrence for the set {x}, the set R of t with abs(h(t) - h(0)) < eps has bounded gaps, so it is unbounded above and below. If t' is in R and t <= t', then h(t) >= h(t') > h(0) - eps; as R is unbounded above, h > h(0) - eps on Z. If t' is in R and t >= t', then h(t) <= h(t') < h(0) + eps; as R is unbounded below, h < h(0) + eps on Z. So h is constant.
Step 4: E is constant. For s >= 0: E(x) >= E(2^s x_1, x_2, x_3, x_4) >= E(2^s x) = E(x), by Step 2 in the first side, Step 2 in the other three, and Step 3. So E does not change when x_1 is multiplied by a power of 2, and two elements of DD differ by such a factor. By symmetry the same holds for each side.
Step 5: the constant is log m. If E = c, then exp(c) = sum over r of exp(-T e_r(B)) for all T, with e_r >= 0; let T grow: exp(c) is the multiplicity m of the level 0, an integer at least 1. The thermal sum of a critical element is exp(E(T, B) + T e_0(B)) - 1 = m - 1 >= 1/5041, so m >= 2. (This is also Proposition CONST of row 1028.) QED

**Corollary GS (PROVED given Theorem CR; the ground-state form).** Let (BDD-Delta) hold with a bound (L_0, D_0). Then (W) fails if and only if Omega(D_0) contains (a) a constant log m with an integer m >= 2, or (b) a uniformly recurrent element E with e_0(b^3) < 0 for one b in DD. In lattice terms: E is the limit of the rescaled data of an admissible sequence (j_i, k_i), and by Step 4 of Theorem CE the rescaled ground levels converge, so e_0(b^3) = - lim over i of Gamma_(1, j_i)(2^(k_i) u_(j_i) b)/b, with Gamma_1(n) = n c(n^3) of Lemma CHAIN-4. Hence, given (BDD-Delta), (W) follows from the two statements

- **(GS-CAS):** for every eps > 0 there are L_eps in P and j_eps such that (L/a_j) c_j((L/a_j)^3) <= eps for all L >= L_eps in P and all j >= j_eps. In words: the ground level of the periodic cube of side L differs from the bulk value by less than eps/L.
- **(NO-CONST):** Omega(D_0) contains no constant.

And (W) gives both: under (PHYS-SEED), Gamma_1 <= D <= 1024 q'^(2^k)/5041 at the sizes from 2^k l on (Lemma Z3), and Omega(D_0) is empty.

Proof. Theorem CR: (W) fails iff Omega(D_0) has a uniformly recurrent element. By Proposition CAS-0 such an element is a constant or has a negative cube ground level. A constant in Omega(D_0) is a fixed point of sigma, hence uniformly recurrent. Under (GS-CAS) every element of Omega(D_0) has e_0(b^3) = 0 for all b (an admissible sequence has j_i and the physical sizes 2^(k_i) l_1 b tending to infinity), so only constants are left, and (NO-CONST) excludes them. QED

Reading. Given a bounded Casimir free energy and no asymptotic degeneracy, the wall is one statement on ground-state energies: the vacuum energy of the periodic cube converges to the bulk value faster than 1/L. A model in branch (III) that is not a constant keeps a Casimir energy of order 1/L on a set of dyadic scales with bounded gaps. This is a form of (LIOU), not a mechanism. It is close to the even seed (ES) of `gap-means-max.md` L29 (the even thermal sum and the vacuum-energy defect below 10^(-7) at one size); here no number is needed and no thermal sum, at the price of (BDD-Delta), all large sizes, and (NO-CONST). (GS-CAS) is not easier than (Z-UNB): an upper bound on lambda_0 of a periodic box against the bulk is not variational.

### 7.3 Lemma NOCS (kill of idea B10 on the lattice): no Chern-Simons factorisation and no period

Setting. Gamma is a finite connected graph (for example the periodic three-dimensional lattice) with vertex set V and link set E. X := SU(2)^E with a bi-invariant metric, Haar measure and Laplace-Beltrami operator Lap. The gauge group G := SU(2)^V acts on X by isometries. V_pot is a smooth real G-invariant function on X (for example the sum of 1 - (1/2) tr U_p over the plaquettes), g > 0, and H := -(g^2/2) Lap + V_pot on L2(X). This is the Kogut-Susskind form of the Hamiltonian. For a smooth real 1-form omega put Q_omega u := du + u omega, a map from functions to 1-forms.

**Lemma NOCS (PROVED).**

1. Every smooth closed 1-form omega on X is exact. If omega is G-invariant, it has a G-invariant smooth potential W, omega = dW.
2. Let omega be a smooth real closed 1-form and c a real number with H = c + (g^2/2) Q_omega^* Q_omega on smooth functions (Q^* the adjoint in L2). Then c is the lowest eigenvalue E_0 of H, and omega = -d log Omega for the positive ground state Omega of H.
3. So there is no factorisation of the lattice Hamiltonian by a closed form that is not exact, and none with c below E_0: statement (CS-lat) of idea B10 has no solution.

Proof. (1) X is a product of 3-spheres, so it is simply connected, and a closed 1-form on a simply connected manifold is exact: omega = dW_0. If omega is G-invariant, put W := the integral over G of W_0 composed with g, against Haar measure of the compact group G. For each g, d(W_0 composed with g) = g^* dW_0 = g^* omega = omega, so dW = omega; W is smooth and G-invariant. (2) With omega = dW: Q_omega u = exp(-W) d(exp(W) u). So phi := exp(-W) is smooth, strictly positive, and Q_omega phi = 0. Then H phi = c phi. The semigroup exp(-tH) on the compact connected manifold X has a strictly positive kernel, so the lowest eigenvalue E_0 is simple with a strictly positive eigenfunction Omega. Eigenfunctions of H to different eigenvalues are orthogonal, and two strictly positive functions are not orthogonal. So c = E_0 and phi is a multiple of Omega. (3) follows from (1) and (2). QED

Remarks. (i) Expanding Q^* Q gives the Riccati form of the hypothesis of (2): V_pot = c + (g^2/2)(abs(omega)^2 - div omega). It is not needed in the proof. (ii) In the continuum the space of spatial connections is also simply connected, and the Chern-Simons functional is a potential of the form B; but it is invariant under the gauge maps of winding number zero only, and the average over the other components does not exist. On the lattice the gauge group SU(2)^V is connected. So the period of the Chern-Simons form, the angle theta and the positive vacuum energy "from a non-exact form" have no lattice counterpart: this is Lemma TWIST of row 1013 in Hamiltonian form. (iii) The same proof holds for the Wilson transfer operator in place of exp(-H): a strictly positive function phi with T_B phi = lambda phi is the vacuum, and lambda = lambda_0. (iv) The lemma kills the lattice form only. The continuum statements of B10 are formal and are not claimed.

### 7.4 Lemma FP-U1 (the K5 part of the kill of idea B8): the Faddeev-Popov gain of compact U(1)

Setting. The periodic lattice (Z/n)^d, n >= 3, with N = n^d sites and d N links. For a link l from x to y let D_l be the vector delta_y - delta_x of R^N. For angles theta_l in (-pi/2, pi/2) put M(theta) := sum over l of cos(theta_l) D_l D_l^T. It is the Hessian at omega = 0 of omega -> - sum over l of cos(theta_l + omega_x - omega_y), the Landau gauge functional of compact U(1): the Faddeev-Popov operator of the minimal Landau gauge. M(theta) kills the constants and is positive on their orthogonal complement; det' is the determinant there.

**Lemma FP-U1 (PROVED).** (i) theta -> log det' M(theta) is concave on (-pi/2, pi/2)^(dN). (ii) log det' M(theta) = log det' M(0) - ((N - 1)/(2 d N)) sum over l of theta_l^2 + O(abs(theta)^4).

Proof. For conductances c in (0, infinity)^(dN) put M_c := sum of c_l D_l D_l^T. The map c -> M_c is linear, log det is concave on positive operators, so c -> log det' M_c is concave; its partial derivative in c_l is R_l(c) := D_l^T M_c^(-1) D_l >= 0, so it is non-decreasing in each c_l. Each theta_l -> cos(theta_l) is concave on (-pi/2, pi/2). A concave function that is non-decreasing in each variable, composed with concave functions of single variables, is concave: (i). For (ii): at c = 1, M_1 is the lattice Laplacian, and the sum over l of R_l(1) is the trace of M_1^(-1) M_1 on the complement of the constants, which is N - 1. The translations and the hyperoctahedral group act transitively on the links and commute with M_1, and R_l does not depend on the orientation of l. So R_l(1) = (N - 1)/(d N) for every link. Taylor's formula gives log det' M_c = log det' M_1 + sum of R_l(1)(c_l - 1) + O(abs(c - 1)^2), and c_l - 1 = cos(theta_l) - 1 = -theta_l^2/2 + O(theta_l^4). QED

Consequence for B8. In the minimal Landau gauge of compact U(1) the Faddeev-Popov weight is log-concave on the cube abs(theta_l) < pi/2, with the Hessian (N - 1)/(d N) per link at the origin (close to 1/4 in dimension four). So the convex gain of idea B8 is present for an abelian group at the same order: test K5 is not met by the mechanism, and the mechanism cannot be what separates SU(2) from U(1). For SU(2) the same computation gives a colour-diagonal part of the same form and a non-negative ghost-loop term (ARGUED, Section 5); both are of order one and do not grow with beta.

### 7.5 Lemma TRI and Proposition SPH (idea B12): class angles on a sphere of plaquettes

**Lemma TRI (PROVED).** Let g_1 in SU(2) have the class angle theta_1 in (0, pi), and let g_2 be uniformly distributed on the conjugacy class of angle theta_2 in (0, pi). Then cos of the class angle of g_1 g_2 is uniformly distributed on [cos(theta_1 + theta_2), cos(theta_1 - theta_2)]. So the class angle theta_12 of g_1 g_2 has the density sin(theta_12)/(2 sin(theta_1) sin(theta_2)) on the set where (theta_1, theta_2, theta_12) lies in

T := {theta in [0, pi]^3 : theta_i <= theta_j + theta_k for the three choices of i, and theta_1 + theta_2 + theta_3 <= 2 pi},

a convex polytope (the spherical triangle inequalities).

Proof. Write g_i = cos(theta_i) + i sin(theta_i) n_i.sigma with unit vectors n_i. Since (n_1.sigma)(n_2.sigma) = n_1.n_2 + i (n_1 x n_2).sigma, (1/2) tr(g_1 g_2) = cos(theta_1) cos(theta_2) - sin(theta_1) sin(theta_2) (n_1.n_2). Conjugation by a Haar element rotates n_2 by a Haar rotation, so n_2 is uniform on the sphere, and t := n_1.n_2 is uniform on [-1, 1] (Archimedes). So cos(theta_12) is uniform on an interval of length 2 sin(theta_1) sin(theta_2) with the stated end points, and the density of theta_12 is sin(theta_12) divided by that length. The condition cos(theta_1 + theta_2) <= cos(theta_12) <= cos(theta_1 - theta_2) with theta_12 in [0, pi] is: abs(theta_1 - theta_2) <= theta_12, and theta_12 <= theta_1 + theta_2 when theta_1 + theta_2 <= pi, theta_12 <= 2 pi - theta_1 - theta_2 otherwise. In each case the missing one of the two upper inequalities follows from theta_12 <= pi. These are the inequalities of T. QED

**Proposition SPH (PROVED).** Let n >= 3, let g_1, ..., g_(n-1) be independent Haar elements of SU(2), and g_n := (g_1 ... g_(n-1))^(-1). Put h_1 := g_1 g_2 and h_k := h_(k-1) g_(k+1) for 2 <= k <= n - 2. Let theta_i be the class angle of g_i (1 <= i <= n) and alpha_k that of h_k (1 <= k <= n - 3). Then the joint density of (theta_1, ..., theta_n, alpha_1, ..., alpha_(n-3)) on [0, pi]^(2n-3) is

(2/pi)^(n-1) 2^(-(n-2)) times the product over i = 1, ..., n of sin(theta_i), on the convex polytope P_n,

where P_n is cut out by: (theta_1, theta_2, alpha_1) in T; (alpha_(k-1), theta_(k+1), alpha_k) in T for 2 <= k <= n - 3; (alpha_(n-3), theta_(n-1), theta_n) in T. (For n = 3 there is no alpha and P_3 = T.) In particular the density is uniform in the diagonals alpha.

Proof. The angles theta_1, ..., theta_(n-1) are independent with the density (2/pi) sin^2 (Weyl). The pair (g_1, g_2) is invariant in law under simultaneous conjugation, which fixes theta_1, theta_2 and alpha_1; so given these three angles h_1 is uniform on its class, and by Lemma TRI (applied with g_1 fixed and g_2 uniform on its class) alpha_1 has the conditional density sin(alpha_1)/(2 sin(theta_1) sin(theta_2)) on T. For k >= 2: g_(k+1) is Haar and independent of (g_1, ..., g_k), so given its class angle it is uniform on its class and independent of h_(k-1); Lemma TRI with h_(k-1) fixed gives the conditional density sin(alpha_k)/(2 sin(alpha_(k-1)) sin(theta_(k+1))) on T, given all earlier variables. The last step gives the class angle of h_(n-2), which is theta_n (an element and its inverse have the same class angle), with the density sin(theta_n)/(2 sin(alpha_(n-3)) sin(theta_(n-1))). Multiply: each sin(alpha_k) occurs once in a numerator and once in a denominator; each sin^2(theta_i), i <= n - 1, is divided once by sin(theta_i); sin(theta_n) occurs once; there are n - 2 factors 1/2. QED

**Corollary SPH-LC (PROVED).** Weight the law of Proposition SPH by the product over i of exp(beta cos(theta_i)), beta >= 0. The weighted density on P_n is log-concave if and only if beta <= 3 sqrt(3)/2. Then the marginal law of (theta_1, ..., theta_n) is log-concave (Prekopa's theorem). For one free plaquette, with the density sin^2(theta) exp(beta cos theta), the bound is beta <= 3 sqrt(3).

Proof. The density is the indicator of a convex set times a product of functions phi(theta_i), phi(theta) := sin(theta) exp(beta cos theta). (log phi)'' = -1/sin^2(theta) - beta cos(theta). It is at most 0 on (0, pi) if and only if beta u (1 - u^2) <= 1 for u = -cos(theta) in (0, 1); the maximum of u(1 - u^2) is 2/(3 sqrt 3), at u = 1/sqrt 3. So phi is log-concave if and only if beta <= 3 sqrt(3)/2 = 2.598.... If beta is larger, take theta_1 = arccos(-1/sqrt 3) = 2.186..., and all other theta_i and all alpha_k equal to 3/2. The triple that contains theta_1 is (2.186, 1.5, 1.5): its sum 5.186 is below 2 pi = 6.283, and 2.186 < 3, 1.5 < 3.686. Every other triple is (1.5, 1.5, 1.5). So all inequalities of T are strict, the point is interior to P_n (for every n >= 3), and along theta_1 the logarithm of the density is strictly convex there. For one plaquette the factor is sin^2, and the condition is beta u(1 - u^2) <= 2. QED

What it means for B12. A closed surface of n plaquettes with free boundary (the surface of one cube has n = 6) is two-dimensional lattice gauge theory on a sphere; by the standard change of variables of that theory its plaquette holonomies have the law of (g_1, ..., g_n) above (ARGUED: the change of variables is not written out here; it is the fact behind the exact solution of the two-dimensional theory, on file in the lane as solvable). So on a sphere the Wilson measure in class angles and diagonals is a product of one-variable factors on a convex polytope, selective in the group (for U(1) the class map is the identity; for a finite group the angles are discrete), and log-concave up to beta = 2.598. This is the toric structure of Jeffrey and Weitsman in elementary form. It does not extend to the four-dimensional lattice: the fan argument needs every group element to enter one product relation, and there each plaquette lies in four cubes. For three free elements and their three pairwise products the density of the six class angles has, in the flat limit, the factor (det of the Gram matrix)^(-1/2) of a Wishart law with three degrees of freedom in dimension three, which is not log-concave (ARGUED). So B12 is the two-dimensional structure again, and (LC-rho) has no support in dimension four.

### 7.6 What Section 7 leaves

PROVED by hand here, unchecked: Lemma BAR; Lemma CHAIN-4 with Corollary NUC; Proposition CAS-0 with Corollary GS (given Theorems CE and CR of row 1017, same-provider check only); Lemma NOCS; Lemma FP-U1; Lemma TRI, Proposition SPH, Corollary SPH-LC. ARGUED: the reading that the weak-coupling logarithm sits in G_0; the SU(2) form of Lemma FP-U1; the identification of the cube surface with Proposition SPH; the Gram-determinant remark. All of it is off the direct path of (W): two exact forms of open items ((BDD-Delta) as a barrier and as four thermal bounds; (LIOU) as a statement on ground-state energies plus (NO-CONST)), and three proved kills. No statement is a mechanism for the selective step.
