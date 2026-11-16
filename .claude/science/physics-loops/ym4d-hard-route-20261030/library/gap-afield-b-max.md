lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-17T00:18Z

# gap-afield-b-max (queue row 1032): far-afield invention row B

Started 2026-11-16T01:36Z (from `date -u`), pinned at commit 58baf6efc. Session model: claude-fable-5-2 at max effort. No subagents, no numeric job started so far.

Run 2 (this run): started 2026-11-16T12:18Z (from `date -u`), pinned at commit 594d6491b. The first run (01:36Z) wrote only the plan below and then failed for lack of credits (lead note in FINISH.md row 1032); its plan is kept and followed. Session model: claude-fable-5-2 at max effort. No subagents.

This file is written section by section. Each section states what was done, what failed, and what is left.

## 0. Status line (updated in place)

- State: run 2 started 2026-11-16T12:18Z; steps 1-3 done (Sections 1-3); step 4 (ideas, fields C, D, E) in progress.

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
