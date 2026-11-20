# Row 1326: sizing study for a verified computation of the seed

Lane: four-dimensional SU(2) Yang-Mills mass gap, in the sense of Jaffe and Witten.
Row: FINISH 1326. Author of this file: Claude Fable 5.2 (worker). Date: 2026-11-20.

Question. Could a computation whose every step is checked by the Lean kernel discharge the seed of the mass-gap chain?
Allowed forms: exact rationals, interval arithmetic, or a certificate produced by a fast program and checked in Lean.

Status: complete, 2026-11-20. Author only; checked by no one. The verdict is in Section 7. Four guide runs of seconds each; no large computation.

Labels: PROVED, ARGUED, GUIDE, OPEN.

## 0. Rule in force, and what this file is

Rule (GOAL.md, section "Computation only as a formal proof", owner 2026-11-20; read on the branch at 78565b162). A computation is a proof step only when it is exact and checked by the Lean kernel. Allowed: exact integer or rational arithmetic; interval arithmetic with every rounding bounded and checked; a certificate from a fast program, if Lean checks the certificate. Monte Carlo, unchecked floating point, fits and extrapolations are never proof steps. The trusted base must be stated. Until the Lean check exists, such a step is labelled "gap (computation specified, not yet formally checked)".

The row's brief was written before this rule change. The lead sent the change during the run. So this file sizes the computation as a real candidate proof step, and it names the trusted base. This row still runs no large computation. Small numeric runs here are GUIDE only.

Plan of the file.

1. The chain and its seed, with quantifiers (Section 1).
2. Each candidate statement: finite or not, sufficient or not (Section 2).
3. The sizes of the two nearest finite statements (Section 3).
4. Certificate methods, and the two named obstructions (Section 4).
5. Cost, the Lean side, and the trusted base (Section 5).
6. What is missing, and whether a finite statement can be proved sufficient (Section 6).
7. Verdict and RESULT (Section 7).

## 1. The chain and its seed

Read for this section: `library/gap-crux-restate.md` 3.1 and 3.4 (row 697); `library/gap-seed-shape.md` 1.4, 1.5 and 2 (row 705); `library/gap-phys-seed.md` 1 and 3.1 (row 720); `library/gap-finishline-opus.md` 1 and 2 (row 837); `library/gap-chain-ce-opus.md` Steps 6 and 7 (row 916); `parts/gap.md`; the FINISH rows named below.

**1.1 Objects (definitions, on file).** Wilson SU(2) on a periodic torus with sides n = (n_0, n_1, n_2, n_3), each at least 3. Z_beta(n) is the integral of exp(-beta sum over plaquettes of (1 - (1/2) tr U_p)) against product Haar measure. F = log Z. For a spatial box B, T_B is the transfer operator. Its eigenvalues are lambda_0 > lambda_1 >= ... >= 0. Z(a x B) = Tr T_B^a. The thermal sum is S(a; B) = sum over i >= 1 of (lambda_i/lambda_0)^a. Credit: Osterwalder and Seiler, and Luscher, for the transfer operator; rows 667 and 671 for the lane's form.

**1.2 The doubling defect (PROVED on file).** Put Phi_B(a) := 2 F(a, B) - F(2a, B). Theorem D-shape (a) of row 705 (Claude Fable 5.2; checked by row 707, Claude Opus 5.5):

log(1 + S(a; B)) <= Phi_B(a) <= 2 log(1 + S(a; B)).

So Phi_B(a) <= log(1 + t) gives S(a; B) <= t. Phi_B(a) reads two partition functions of finite tori at one coupling. It contains no infinite-volume quantity. Part (d) of the same theorem: Phi_B(a; beta) = 12 a |B| times the integral over s in [0, beta] of (p_(a,B)(s) - p_(2a,B)(s)), where p is the mean of (1/2) tr U_p over all plaquettes of the torus.

**1.3 The engine at one coupling (PROVED on file).** Theorem S (row 697, Claude Fable 5.2; checked by row 698, Claude Opus 5.5, and row 699, Codex gpt-6-astra), Corollary S3' (row 699) and Theorem SH (row 705; checked by row 707, same provider as its author). Let a >= 3 and b = r a. If S(a; b^3) <= t(r), every periodic cube of side L >= b has a transfer gap. The gap is at least log(1/(K s))/(2a) on all large cubes, with K of the table. The proved thresholds are t(2) = 1/1650 (two stages), t(3) = 1/100, t(4) = 1/25, t(6) = 1/10, and t(r) = 3/10 for r >= 24. The proof uses positivity of the transfer operators and the symmetry of Z under exchange of axes. It holds for every compact gauge group. With the limit theorem of row 700 (checked by row 703) the conclusion is exponential clustering in every infinite-volume limit state at that coupling. All of this is at one coupling.

**1.4 The seed of the continuum chain (the equivalences and the consumer are PROVED on file; the seed itself is OPEN).** The chain uses the account of Sussman and Alpoge (with Claude and Codex as authors of their text), built on Balaban's method. A first-passage datum is a pair (K, beta): K block steps bring the running inverse coupling into the window (g^(-2), g^(-2) + B_sharp]. The bare spacing is a_K = L^(-K) in the first-passage unit. g is small. Its ceiling gamma_H has no value in the text (row 837, `library/gap-finishline-opus.md` 1.1). The seed is

(SEED-FP) (row 837; it is (PHYS-SEED) of row 720 on the account's data): there are K_0, one physical size l and s_* below the threshold such that S_(K,beta)(l/(2 a_K); (l/a_K)^3) <= s_* for every first-passage datum with K >= K_0.

Theorem ZD-c of row 720 (Claude Fable 5.2; checked by row 727, Claude Opus 5.5, and by `library/gap-zd-astra.md`, gpt-6-astra) gives three more forms equivalent to it: (PHYS-SEED-Delta), (Z-SEED), and (BDD-Delta) with (Z-UNB). Each has an upper or lower limit over the cutoff index j. The consumer is checked: rows 700 and 703 (limit states), row 916 links (c) and (e) (Claude Opus 5.5; checked by row 917, Codex gpt-6-astra). Given the account's premises, (SEED-FP) gives a unique vacuum and spectrum in {0} union [M_*, infinity) on the tr F^2 sector.

**1.5 The quantifier (PROVED by reading).** (SEED-FP) asks for the seed at every late cutoff, at one physical size. The lattice side l/a_K = l L^K grows without bound. The bare coupling grows without bound. So the seed of the continuum chain is an infinite family of lattice statements. One finite computation covers finitely many of them.

**1.6 Two words used below.** "Genuinely finite" means: finitely many couplings, finitely many tori, finitely many integrals. "Sufficient through checked results" means: (SEED-FP) follows from the statement by statements that are PROVED on file and checked by a second model.

## 2. Step 1. The candidates, one by one

Read for this section: `library/prior/gap-onebound-read-sol.md` in full (row 1218); `library/gap-mini-solve-au-opus.md` in full (row 1295); `library/gap-solve9-astra62.md` L109-L216 (row 1161); `library/gap-phys-seed.md` L243-L336; `library/gap-solve38-astra62.md` L125-L197 (row 1321); `library/gap-solve39-astra62.md` L186-L322 (row 1323); `library/gap-chain-ce-opus.md` L253-L360 (row 916); the RESULT lines of rows 848, 917, 925, 978, 1143, 1144, 1162, 1183, 1232, 1242, 1265, 1266, 1288, 1311, 1322, 1324. I did not read the primary text of the published papers. Statements about them come from rows 1218, 1295 and 1311.

**2.1 One finite kernel (PROVED by reading the statements).** Each candidate of the brief contains the same finite object, or a thermal trace that it bounds:

(KER) 2 log Tr T_B^a - log Tr T_B^(2a) <= tau, for one coupling, one box B and one time a,

on the full slice space or on its centre-neutral part. The candidates differ in the sector, the threshold, the set of shapes, and the quantifier over cutoffs. C8 in the table is of another kind: a block test with a supremum.

| # | Statement | Quantifier over cutoffs | Finite | What it gives by checked results |
|---|---|---|---|---|
| C1 | The published window (A-B*), equivalently (A-B**), of Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy (their Theorem F; row 1218 L81-L100): Z(s, T_0)^2 <= e^(gamma V(s)) Z(s, 2 T_0) for every integer shape s in [2 T_0, 48 T_0)^3, with gamma = y_0/(2 (96 T_0)^3), y_0 <= 1/20 | for every p >= p_0 and every N >= N_0(p), with 3 <= T_0 <= N t_0 | no | with Corollary AU2 (row 1295, Claude Opus 5.5; check 1311, gpt-6.2-astra: HOLDS): (N-phys) at an admissible side L >= 16384 t_0 |
| C1' | (B**) at one coupling and one T_0 >= 3 | none | yes: (46 T_0)^3 ordered shapes, two tori each | a gap at least 0.172/T_0 on every cube of side >= 2 T_0, at that coupling (their Theorem 7.56; checked by rows 1295 and 1311). Not (SEED-FP) |
| C2 | (N-phys) of row 1161 (gpt-6.2-astra; check 1162, Claude Opus 5.5): one physical side L and j_0; for every j >= j_0 an integer u_j in [3, n_j/512] with neutral excited trace s_+(u_j; n_j^3) <= 1/2. Its equivalent forms (26) and (28) of row 1186 (check 1191: HOLDS) are upper limits over j of an information quantity (row 1218 L46-L57) | for every j >= j_0 | no | the gap clause, given the account's premises (rows 1179 and 1225; checks 1183 and 1232, both HOLD AFTER CORRECTION) |
| C2' | The one-cube neutral test of row 1161 at one coupling: 4 divides n, n >= 2^70, s(u) <= 1/2 for one integer u in [3, n/512] (L113-L215) | none | yes | at that coupling: S_per(n/2) < 2^(-19), or the all-magnetic neutral seed S_full < 2^(-18). Not (SEED-FP) |
| C3 | Theorem ZD-c: (PHYS-SEED), (PHYS-SEED-Delta), (Z-SEED), (BDD-Delta) with (Z-UNB) (`gap-phys-seed.md` L311-L320) | an upper or lower limit over j in each form | no | it states the target |
| C3' | Theorem ZD at one coupling, forms (A) and (C') (L296-L304). (A) reads two tori. (C') reads the gap of one cube and two symmetric tori | none | yes | a uniform gap at that coupling. Not (SEED-FP) |
| C4 | Row 1321 (16) (gpt-6.2-astra; check 1322): limsup as the spacing tends to 0 of E W_pair < 1/5 in the neutral symmetric circle (`gap-solve38-astra62.md` L170-L177) | an upper limit over the cutoff. The error 2 (T/k) e^(-c m) of its (15) vanishes only in the limit, and c has no value | no | the neutral input of C2 only (check 1322, its correction to line 177 of row 1321) |
| C5 | Row 1323 (29) (gpt-6.2-astra; check 1324): limsup over j of W_many < log(1651/1650) (`gap-solve39-astra62.md` L304-L311) | an upper limit over j. W_many equals the defect only up to o(1), along beta = O(log n) | no | the two-stage seed of Theorem ZD-c |
| C6 | The lane's fixed-coupling seed: Phi_B(a) <= log(1 + t(r)), B = (r a)^3 (`gap-seed-shape.md` Section 2) | none | yes: two tori | a uniform gap and clustering at that coupling (1.3). Not (SEED-FP) |
| C7 | (SEED-L) at the data of one cutoff K_0: Phi_L(d_0) := L^4 F_(d_0)(T_l) - F_(d_0)(T_(L l)) <= phi_* - (L^4 + 1) E(K_0), with phi_* < (L/2) log(13/10) (rows 837 and 916) | none | yes, once K_0, the base data and E(K_0) are numbers | (SEED-FP), GIVEN (UNIV-K). (UNIV-K) is OPEN. So not by checked results |
| C8 | (DS-W) at (R, delta) at one coupling (row 691; row 1258 Lemma WS, check 1265) | none | one finite block, with a supremum over all boundary values | the seed at that coupling. Not (SEED-FP). OPEN at the window |

Row 1325 (25) (gpt-6.2-astra; check 1327: HOLDS AFTER CORRECTION), which landed during this run, is one more form of C5: an upper limit over the spacing of an overlap sum, at one physical side. The exact finite parts of C4 and C5 are (KER) again. Row 1321 (12) is an identity at each finite lattice: the expected product of the continuation labels is tanh((2 log z_T - log z_(2T))/2). Row 1323 (29) is Theorem D-shape (a). What rows 1321 and 1323 add to it is asymptotic.

**2.2 Why none is finite and sufficient.**

(a) C1 to C5 (PROVED by reading). Each form that feeds the continuum chain has the quantifier "every late cutoff". Two statements on file say that the lattice must grow along the trajectory. The authors of C1 prove that the gap at a fixed lattice size closes as the coupling grows (their Theorem 7.59, as read in row 1218; not checked here). Row 1143 (gpt-6.2-astra; check 1144: all 24 statements HOLD) excludes a seed on a cube of side n whenever n^2 = o(beta).

(b) C1', C2', C3', C6, C8 (PROVED on file for the implication; ARGUED for the limit of its reach). These are finite. Their conclusion is a gap at one coupling. To reach (SEED-FP) from one coupling a carry to finer cutoffs is needed. Row 978 (Claude Fable 5.2) looked for one and found none: "the carry is (NOCRIT) of row 709 plus an asymptotic-freedom climb", and beta 2.3 "is not a lattice of the account's family (all at weak bare coupling)". Row 837 argues the same: no fixed beta_W finishes the proof without a renormalization step to that scale and a weight comparison there.

(c) C7 (PROVED on file for the implication; its hypothesis OPEN). This is the only statement I found on file that makes one cutoff enough. Lemma ONE-K is PROVED (row 916; check 917: HOLDS AFTER CORRECTION of the base-set quantifier). Its hypothesis (UNIV-K) is OPEN (rows 924 and 925). Rows 1233 to 1314 reduce (UNIV-K) to inputs of the account. Check 1288 lists what the carry still needs: "the physical normalization and two-torus estimates, the Section 9.1 inputs including the blind-site expansion, a uniform comparison of the two flows, and an infrared seed". The base is not one arbitrary coupling. Check 1242 FAILS "the identification of the seed with a positive lattice gap at one arbitrary coupling". Check 1265 FAILS the "one fixed coupling" wording in general. The base is every datum of cutoff K_0 that the predecessor chains reach. On the pin route it is one datum (Proposition PIN of row 1256; check 1266: HOLDS AFTER CORRECTION). K_0 = 0 is not usable (row 916, ARGUED there).

**Decision of step 1 (ARGUED).** No statement on file is both genuinely finite and sufficient for the seed through checked results. Scope of this sentence: the four candidates of the brief and the lane's own finite forms C6 to C8, read one by one. It is not a search of every library file. Two finite statements come nearest:

- C6 is checked-sufficient for a different conclusion: a lattice gap at one coupling.
- C7 has the right conclusion. Its sufficiency rests on (UNIV-K), which is OPEN, and its parameters are not numbers yet.

Sections 3 to 5 size both. Section 6 says what is missing.

## 3. Step 2. Sizes of the two nearest finite statements

Every number of lattice physics in this section is GUIDE. The inputs are published values quoted in `library/prior/gap-seed-size.md` (row 706, Codex gpt-6-luna): Athenodorou and Teper (arXiv:2106.00364, Appendix Table 1) for a sqrt(sigma) and a m(0++) at beta = 2.2986, 2.3714, 2.427, 2.509 and 2.60; Teper (hep-th/9812187) for m(2++)/sqrt(sigma) = 5.55; Lucini, Teper and Wenger (hep-lat/0404008) for the flux-tube energy. The model is the ideal gas of row 705 Section 5 and row 706: one scalar, five tensor states, three flux tubes, continuum dispersion, no interaction. I ran it once for the shapes of Theorem SH (Appendix A). A model value is not a bound. It guides the size only.

**3.1 The fixed-coupling seed (C6) as a specification.**

(W-FIX)(beta; a, r): Z_beta(a, b, b, b)^2 <= (1 + t(r)) Z_beta(2a, b, b, b), with b = r a, a >= 3, beta rational.

This is Phi_B(a) <= log(1 + t(r)) without logarithms. Its consumer is Theorem SH (1.3).

First time extent a that passes in the model, with b = r a:

| beta | r = 2, t = 1/1650 | r = 3, t = 1/100 | r = 4, t = 1/25 | r = 6, t = 1/10 | r = 24, t = 3/10 |
|---|---|---|---|---|---|
| 2.2986 | a = 10, b = 20 | 8, 24 | 8, 32 | 8, 48 | 11, 264 |
| 2.3714 | 11, 22 | 10, 30 | 9, 36 | 10, 60 | 13, 312 |
| 2.427 | 14, 28 | 12, 36 | 11, 44 | 11, 66 | 16, 384 |
| 2.509 | 18, 36 | 15, 45 | 14, 56 | 15, 90 | 20, 480 |
| 2.60 | 23, 46 | 19, 57 | 18, 72 | 19, 114 | 26, 624 |

The shape r = 2 has the fewest sites at every coupling. A larger threshold does not pay: the box grows faster than the threshold helps (row 705 Section 5 says the same).

The smallest instance in the measured window is beta = 23/10, a = 10, b = 20:

- tori 10 x 20^3 (80,000 sites, 320,000 links) and 20^4 (160,000 sites, 640,000 links, 960,000 plaquettes);
- after gauge fixing on a tree the two integrals have 720,003 and 1,440,003 real dimensions;
- quantity: Phi_B(10) = 2 F(10, 20, 20, 20) - F(20, 20, 20, 20), to be shown at most log(1651/1650) = 6.06e-4;
- in the model Phi_B(10) is 2.4e-4, so the slack is about 3.6e-4;
- accuracy: the enclosures of the two free energies need widths w_1 and w_2 with 2 w_1 + w_2 below the true slack. The free energy of the 20^4 torus is about 1.5e6 in size. So the relative accuracy is about one part in 10^10;
- in the form of Theorem D-shape (d): the integral over s in [0, 2.3] of the plaquette difference between the two tori must be shown at most 6.3e-10.

At beta = 2.60 the instance is a = 23, b = 46: 2.2e6 and 4.5e6 sites.

Below the measured window I have only the leading order of the strong-coupling series, with no error control: g(a; b^3) is about 3 b^3 u^(4a), u = I_2(beta)/I_1(beta) (row 701 has the exact leading term of Phi(n)). The smallest pair that Theorem SH admits at r = 2 is a = 3, b = 6: tori 3 x 6^3 and 6^4, 648 and 1296 sites. At leading order it passes for u <= 0.297, that is beta up to about 1.26. For comparison u = 0.055 at beta = 2/9 (the lane's proved seed range, row 837), u = 0.090 at beta = 9/25 (the range the authors of C1 prove, their Theorem 9.5 as read in row 1218), u = 0.479 at 2.3 and u = 0.520 at 2.6.

What (W-FIX) would give: a lattice gap of Wilson SU(2) at the one coupling beta, uniform in the volume. By the readings of rows 1124, 1126 and 1218, no proof of a gap at a coupling near 2.3 is published. It is not on the path to (SEED-FP) (2.2 (b)).

**3.2 The published window at one coupling (C1').** In the model the least T_0 at beta = 2.2986 is 17 (T_0 m = 20.8). The sides run over [34, 816). That is about 8e7 shapes up to order. The largest torus has 34 x 815^3 = 1.8e10 sites. The threshold per unit volume is gamma = 5.8e-12. At beta = 2.60: T_0 = 40, about 1e9 shapes, up to 5.7e11 sites. Remark AU3 of row 1295 says the same from the statements: Theorem S tolerates a thermal density about 877 times larger (check 1311). So C1' costs more than C6 on every count.

**3.3 The one-cube neutral test (C2') (PROVED on file).** Its proved lattice range is n >= 2^70 (row 1161 L215; check 1162 recomputed it). That is 1.2e21 sites on a side. One spatial slice has 1.6e63 sites.

**3.4 The one-cutoff datum (C7) (the floor is PROVED by reading the lane's readings of the account, given M R >= 1; the physics table is GUIDE).**

(W-TRAJ)(d_0): L^4 F_(d_0)(T_l) - F_(d_0)(T_(L l)) <= phi_* - (L^4 + 1) E(K_0), for the base datum d_0 = (K_0, beta_0).

- Tori: two symmetric tori with 2 L^(m + K_0) and 2 L^(m + K_0 + 1) sites on a side (row 916 Step 7). The account's tori have l = 2 L^m >= l_*(g) = 2 L^11 M R(g^(-2) + B_sharp) (the outline of Sussman and Alpoge at its lines 21521-21532, as read in row 720 1.1.1 and row 837 1.5). So m >= 11 when M R >= 1. K_0 >= 1, since row 916 argues that K_0 = 0 is not usable. L is odd. Lemma FL is written for L >= 25.
- For L = 25: sides at least 2 x 25^12 = 1.2e17 and 2 x 25^13 = 3.0e18. That is at least 2.0e68 and 7.9e73 sites.
- For L = 3, the least odd block factor: sides at least 1.1e6 and 3.2e6, at least 1.3e24 and 1.0e26 sites. I do not claim L = 3 is admissible. The account takes L large, and Lemma FL is not written below 25.
- Coupling: beta_0 lies in W_(K_0)(g), so beta_0 >= g^(-2) + B_sharp, with g <= gamma_H. The account gives no value for gamma_H.
- Accuracy: phi_* is below 0.131 L, which is 3.3 at L = 25. F(T_l) enters with the weight L^4 = 390,625. So F(T_l) needs an absolute enclosure of about 8e-6 on a torus of at least 2.0e68 sites. E(K_0) has no value yet.

The same size from the physics (GUIDE). The seed lives at a physical size where the running coupling is of order one. On a lattice at bare coupling beta that side grows like (beta)^(-51/121) e^((3 pi^2/11) beta), the two-loop scaling law for SU(2). Anchored at the beta = 2.60 row of 3.1 (r = 2, b = 46):

| beta | 2.6 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|---|---|---|---|
| seed side b in sites | 46 | 1.3e2 | 1.7e3 | 2.2e4 | 3.1e5 | 5.9e7 | 1.2e10 | 2.4e12 | 9.9e16 |

In this guide the floor 1.2e17 of the account at L = 25 matches a bare coupling of about 16.

**3.5 The two requirements do not meet (ARGUED).** (W-FIX) is small only at a coupling of order one, where no lattice of the account's family lies. (W-TRAJ) is on the path only at the weak couplings of the account, where its lattice has at least 10^24 sites in the most favourable reading and at least 10^68 in the lane's reading. No coupling on file serves both.

## 4. Step 2, continued. Certificate methods, and what blocks each

Read for this section: `library/gap-loop-pos-astra.md` Sections 1 and 3 (row 760); `library/gap-loop-grow-astra.md` Theorems A and B and Section 6 (row 767); `library/gap-solve39-astra62.md` L186-L322 (row 1323); `library/gap-solve38-astra62.md` L125-L197 (row 1321); `library/gap-bridge-exercise-opus.md` L337-L339 and L368 (row 1072); `library/prior/gap-lit-loops.md` L42-L48 (row 755); `library/prior/gap-mechanism-watch-read-luna.md` L50-L54 (row 1126); the RESULT lines of rows 762, 773, 1074, 1075, 1123, 1322, 1324.

**4.1 What a certificate must do.** (KER) is an inequality between partition functions of the actual Wilson measure. It needs an upper bound on Z(a x B) and a lower bound on Z(2a x B), each to about one part in 10^10 at the window (3.1). I list eight families. For each: the method, its cost, and what on file blocks it.

**M1. Exact evaluation by character expansion and contraction.**

- Method. Expand each plaquette weight in SU(2) characters (Peter-Weyl). Integrate each link exactly. Cut the spins at dimension d = 2j + 1 <= D with a proved tail. Contract the finite network with interval arithmetic.
- The cut (GUIDE arithmetic, double precision). The tail sum over d > D of d^2 I_d(beta)/I_1(beta) at beta = 2.3 is 3.3e-1 at D = 4, 5.0e-4 at D = 8 and 9.7e-8 at D = 12. The target needs about 1e-10 for each plaquette, so D is about 16.
- **Lemma DIM (PROVED here; elementary; unchecked).** Let Sigma be a periodic three-dimensional slice with abs(Sigma) sites, connected. The gauge-invariant space of its 3 abs(Sigma) links, with link spins restricted to 0 and 1/2, has dimension at least 2^(2 abs(Sigma) + 1). Proof. A subgraph with all degrees even is an element of the cycle space over the field of two elements. That space has dimension (links) - (sites) + 1 = 2 abs(Sigma) + 1. Put spin 1/2 on the links of the subgraph and spin 0 elsewhere. At a site with 2k marked links the invariant part of the tensor product of 2k copies of the spin-1/2 space is not zero (its dimension is the Catalan number C_k). So each subgraph carries an invariant state. States with different link spins are orthogonal. QED
- Cost. A transfer-matrix evaluation in the spin-network basis stores a vector of at least that dimension, and each step costs at least as many operations. The smallest slice of a x b^3 with a <= b is a x b^2.

| Torus | Smallest slice | Dimension at least |
|---|---|---|
| 10 x 20^3 | 4000 sites | 2^8001, about 10^2408 |
| 20^4 | 8000 sites | 2^16001, about 10^4816 |
| 3 x 6^3 (smallest pair of Theorem SH at r = 2) | 108 sites | 2^217, about 10^65 |
| 6^4 | 216 sites | 2^433, about 10^130 |

- These bounds use spins 0 and 1/2 only. The real cut D of about 16 makes them larger.
- No exact method with a smaller exponent is known to me (ARGUED; a statement about known methods, not a theorem). The cost of contracting a network is exponential in its treewidth. The treewidth of the four-dimensional torus grid is of the order of its smallest three-dimensional slice.
- Blocked by: nothing in logic. By its cost.

**M2. Interval cubature on the group variables (ARGUED).** The integrals have 720,003 and 1,440,003 dimensions (3.1). A covering needs at least two cells in each dimension. Worse than M1.

**M3. Loop equations with positivity (the bootstrap of Anderson and Kruczenski, and of Kazakov and Zheng).**

- Why it is the natural certificate. The dual solution of a semidefinite program is a sum-of-squares identity with rational coefficients. A fast solver finds it. Lean checks it with exact arithmetic. So this is the form "certificate from a fast program, checked in Lean".
- What Theorem O says (row 760, Codex gpt-6-astra; check 762, Claude Opus 5.5: HOLDS). Fix a patch radius r >= 2. Let K_r(s) be the set of all local moment functionals that obey the SU(2) identities, every Ward equation in the patch, positivity and reflection positivity there. A separate-state local certificate is a bound p(omega) - p(nu) <= b(s) for all omega, nu in K_r(s). Then the integral of b over any coupling interval I is at least J_r(I) > 0, and J_r(I) does not depend on the box. So for fixed r such a certificate fails for all large boxes (Corollary O-seed).
- Its reach by its own constants (row 767 Theorem A; check 773: HOLDS). The explicit width is 2^(-280 n)/n with n = 2r + 4. It excludes only radii below about (log_2 a)/70. At r = 2 it excludes only box sides a above about 2^553. So by its constants Theorem O does not block a certificate at a seed size.
- **Remark OS (PROVED here from (3.4) to (3.7) of row 760, which check 762 confirms; the remark itself is unchecked).** In the notation of row 760: n = 2r + 4, Phi_n(s) = 16 log Z_n(s) - log Z_(2n)(s), f_n(s) = p(omega_n(s)) - p(omega_(2n)(s)), Phi_n' = 96 n^4 f_n, and J_r(I) is the integral over I of abs(f_n). Phi_n(0) = 0. Hence

  J_r([0, beta]) >= Phi_n(beta)/(96 n^4).

  So for every separate-state local certificate of radius r, the integral of b over [0, beta] is at least Phi_(2r+4)(beta)/(96 (2r+4)^4). Here Phi_n(beta) = 16 F(n^4) - F((2n)^4) is the seed quantity of Theorem S for the symmetric torus of side n.
- Consequence (PROVED given Theorem D-shape (d), 1.2). Suppose such a certificate proves Phi_B(a; beta) <= tau for B = b^3 by integrating its pointwise bound: Phi_B(a; beta) <= 12 a b^3 times the integral of b(s), and that product is at most tau. Then

  Phi_(2r+4)(beta) <= 8 (2r+4)^4 tau/(a b^3).

  If (2r+4)^4 <= a b^3/8, this reads Phi_n(beta) <= tau at n = 2r + 4. By Theorem D (b) of row 697 the torus of side n then carries a seed itself: S(n; (2n)^3) <= e^tau - 1.
- Meaning. A local certificate can prove the seed of a box only if a symmetric torus of the size of its patch already passes a seed test of the same strength. The patch is as large as a seed box. The certificate does not make the problem local.
- GUIDE numbers (the model of 3.1). For beta = 2.2986, a = 10, b = 20 the condition first holds at n = 12, so r >= 4. Corollary O-seed needs a >= 2r + 3 = 11 for the patch to fit. It does not fit in the side a = 10. For beta = 2.60, a = 23, b = 46: n >= 28, r >= 12, and 2r + 3 = 27 exceeds 23. So in the model no certificate of this class proves the first instance that passes.
- Precision (GUIDE). Published SU(2) bounds reach sub-percent precision on the plaquette, with loops up to length 16 to 24 (Kazakov and Zheng, arXiv:2404.16925, as read in row 755). (KER) needs about 3e-10 on the same quantity. No rate of convergence in the loop length is on file.
- The one certificate written on file, the radius-two certificate of Corollary P-shift, fails by its own slack for beta above about 0.029/a to 0.049/a (check 762; one step of that check is argued, not proved).
- Not excluded: certificates with constraints that name the volume. Theorem B of row 767 (check 773: HOLDS): on a fixed finite periodic lattice the full system of polynomial Ward equations determines the Wilson measure. So a complete certificate exists in principle. Its size is that of the whole torus, and no bound on it is on file. The joint two-volume route collapses to the two marginals (check 773).
- Blocked by: Theorem O with Remark OS for every patch smaller than a seed box; by size and precision beyond that.

**M4. A Gaussian or perturbative enclosure.**

- Why one would try it. The lattices of (W-TRAJ) are at weak coupling. The rigorous tool there is a Gaussian main term with a bounded remainder.
- What row 1323 (26) to (30) say (gpt-6.2-astra; check 1324, Claude Opus 5.5: 42 statements HOLD). (24), (26): two winding cuts have the same Wilson thermal defect up to o(1), and their Gaussian predictions differ by (9/2) log n + O(1). So no one Gaussian substitution is right to order one on both cuts. (28): on the cut with a bounded Gaussian defect, two free transverse modes alone give at least 6 log coth 4 = 4.0e-3. The threshold is log(1651/1650) = 6.1e-4. (30): the seed therefore forces the interacting correction to be negative: N_many < 2 log(1651/1650) - 6 log coth 4 = -2.8e-3.
- Meaning. The main term fails the test by a factor of more than 3 even against twice the threshold. The remainder must cancel at least 70 percent of it, with a proved sign. That remainder is the generation of the mass. It is not perturbative.
- Blocked by: (26) to (30). Their scope is the trajectory, beta = O(log n). They say nothing at a coupling of order one, where M4 has no small parameter at all.

**M5. Finite-block criteria that are uniform over boundary values (Dobrushin and Shlosman; complete analyticity; their computer-assisted forms).**

- Why one would try it. Such a criterion is local. A computation on one small block could verify it.
- What is on file. Proposition CA-FAIL (row 1072, Claude Opus 5.5; checks 1074, gpt-6-astra, and 1075, Claude Opus 5.5: HOLDS AFTER CORRECTION, in the strong-mixing form, given the theorem of Frohlich, Simon and Spencer): mixing that is uniform over all volumes and all boundary values fails at every beta above the threshold 2 W_3 of Frohlich, Simon and Spencer. Its value is 1.0109; the two checks bound it by hand below 2 and below 2.3. So it fails at every window coupling. Pinned slabs carry an ordered three-dimensional O(4) model. The weak-mixing form (DS-W) of row 691 (C8) is not refuted. It is OPEN at the window. Its test takes a supremum over all boundary values of a block of side R: R^4 sites, and of the order of R^3 group variables under the supremum. No method bounds such a supremum of an in-law quantity. Of the in-law block criteria of rows 1115 to 1123, the swap form is false at the window (Proposition J of check 1121), and the others are one-scale mixing itself or have no consumer (`parts/gap.md`, method 34, with the corrections of check 1123).
- Blocked by: CA-FAIL in the uniform form; no method in the weak form.

**M6. Variational bounds (Jensen, Gibbs).** A Jensen bound on Z(2a x B)/Z(a x B)^2 in the periodic ensemble loses the relative entropy of the two closing laws. Row 1321 (18) (check 1322: HOLDS): along the trajectory that entropy is at least c m, and it diverges on the physical cube. At a fixed window lattice the same loss applies (ARGUED): a trial measure would need a total relative entropy below 1e-4 against the Wilson measure on 10^6 dimensions, and its energy and entropy would have to be exact.

**M7. Convergent expansions and zero-free regions.**

- Where a cluster expansion converges, or Z is proved free of zeros in a complex neighbourhood, rigorous methods of polynomial cost exist. Those are the ranges already proved by hand: beta below 2/9 in the lane (`library/gap-vmf-lip.md` Section 4, as cited in row 1258), beta up to 9/25 in the paper of the authors of C1.
- Computation extends such ranges only a little. Bhattacharjee, Bhattacharya, Lockwood and Romanov used ball arithmetic for a step from 1/3 to 0.351 in version 6 of their paper on the one-cube estimate (Hexagon 2610.00341), and give hand bounds up to 0.348 in version 7 (rows 1126 and 1218, readings). Remondiere's computed instance of a criterion of the shape of Theorem S is at beta at most 0.005 (row 1126, reading).
- The window has u = 0.48 to 0.52. Those ranges end at u = 0.09. Zero-freeness at the window is open on file (Route Z of `library/gap-skeleton-final.md`; row 1163 states (W) as a signed test on the zeros).
- Blocked by: the missing mathematics. M7 needs the theorem first.

**M8. Monte Carlo.** Not a proof step by the rule. Not sized.

**4.2 The best method (ARGUED).**

- For (W-FIX): M1. It is the only family that nothing on file blocks in logic. Its cost is in Section 5.
- For (W-TRAJ): none. M1 would run on at least 10^24 sites. M4 is blocked by (26) to (30).

**4.3 One reading of 4.1 (ARGUED).** Certificates come in two kinds. A worst-case certificate takes a supremum over boundary values or over all local states. It is cheap, and in the band it is false or too weak: CA-FAIL, Theorem O with Remark OS, and the lane's Theorem D2 and Lemma SHEET (rows 977 and 996) say so. An in-law certificate must evaluate the Wilson measure itself. Without sampling that is M1.

## 5. Step 2, continued. Cost, the Lean side, and the trusted base

**5.1 Cost (lower bounds from Lemma DIM; sizes from Section 3).**

| Statement | Tori | Accuracy needed | Best method | Operations | Memory |
|---|---|---|---|---|---|
| (W-FIX), beta = 23/10, a = 10, r = 2 | 10 x 20^3 and 20^4 | slack about 3.6e-4 on Phi_B (GUIDE); one part in 10^10 on F | M1 | at least 10^2408 and 10^4816 | at least as many interval values |
| (W-FIX), smallest pair that Theorem SH admits, a = 3, r = 2 (passes only up to beta about 1.26, leading order, GUIDE) | 3 x 6^3 and 6^4 | at most 6.1e-4 on Phi_B | M1 | at least 10^65 and 10^130 | the same |
| (B**) at beta = 2.2986, T_0 = 17 (GUIDE) | about 8e7 shapes, up to 1.8e10 sites | gamma V(s), gamma = 5.8e-12 | M1 | more than the first line, for every shape | the same |
| C2' | one cube with n >= 2^70 | 1/2 on a neutral trace | none | no method | no method |
| (W-TRAJ), L = 25 | sides at least 1.2e17 and 3.0e18 | about 8e-6 on F(T_l) | none (M4 is blocked) | no method | no method |

For scale (GUIDE). A machine that does 10^18 operations in a second does 3e25 in a year. The largest formal checks on record are of the order of 10^16 machine operations (for example the nonlinear inequalities of the Flyspeck proof of the Kepler conjecture, about 5000 processor-hours; credit Hales and coauthors; recalled, not re-read for this row). The smallest admissible pair is almost 40 orders of magnitude beyond a year of such a machine. The window pair is more than 2000 orders beyond.

So no item of 5.2 can be run. I state 5.2 and 5.3 because the lead asked for the trusted base.

**5.2 What Lean would have to check for (W-FIX) by M1 (ARGUED; a specification, not a plan).**

- L1. Definitions: Haar measure on SU(2), the torus, Wilson's weight, Z as an integral over the product of the links.
- L2. The consumer: the transfer operator and its positivity (TM); Lemmas A, K, X, E, E', E2; Proposition B3; Theorems D-shape, S and SH; the limit theorem. These are hand proofs on file. They would need a formalization. Remondiere reports a Lean formalization of an implication of the same shape as Theorem S, with the transfer representation as a hypothesis (row 1126, reading; not checked here).
- L3. The reduction of Z to a finite sum: Peter-Weyl for SU(2), orthogonality of matrix coefficients, the Haar integral of a product of representation matrices on one link (a projection onto invariants), and the tail bound in the spin cut. Hand mathematics, to be formalized.
- L4. Enclosures of the Bessel values I_d(beta) at rational beta, and of the recoupling coefficients (square roots of rationals), by interval arithmetic with rational end points. The soundness of that arithmetic is a Lean theorem, not part of the trusted base.
- L5. The evaluation itself: at least 10^65 steps for the smallest pair.

I did not survey Mathlib for L1 to L4 in this row.

For a certificate of kind M3 Lean would check two things. First the loop equations as theorems (integration by parts on SU(2)). Second one rational identity and the positive semidefiniteness of rational matrices, for example by an exact LDL^T factorization. The solver stays outside the trusted base.

**5.3 Trusted base, three options (ARGUED; the reach figures are GUIDE).**

- T1, kernel only. The evaluation runs by kernel reduction (`decide`, `rfl`, or proof terms from `norm_num`). Trusted: the Lean kernel with its GMP arithmetic on natural numbers, and the axioms propext, Quot.sound and Classical.choice. Reach (GUIDE): about 10^6 to 10^9 arithmetic steps.
- T2, `native_decide`. It adds the axiom `Lean.ofReduceBool`. Trusted in addition: the Lean compiler, the C compiler and the runtime. Reach (GUIDE): about 10^12 to 10^15 steps.
- T3, an external checker that is itself verified, with a certificate format proved sound in Lean. Trusted in addition: that checker and the proof of its compiler.

None of T1 to T3 reaches L5.

**5.4 Labels under GOAL.md.**

- (W-FIX) is a "gap (computation specified, not yet formally checked)". The statement is exact (3.1). The method is M1. The cost is 5.1. The computation cannot be run by any method I can find. And (W-FIX) is not the seed of the chain.
- (W-TRAJ) is not a specified computation. Its datum has no numbers (6.1, X2), and its sufficiency is OPEN (6.1, X1).

## 6. Step 3. What is missing, and whether a finite statement can be proved sufficient

**6.1 What is missing, exactly.**

- X1 (OPEN). (UNIV-K), in the form of row 916 Step 7: a predecessor map pi on first-passage data and numbers eps_K with finite sum, such that abs(F_d(T) - F_(pi d)(T) - c_d vol(T)) <= eps_K on both tori T_l and T_(L l). Open since rows 924 and 925. Rows 1233 to 1314 reduce it to inputs of the account that are still open: the two-cutoff comparison of its Section 9.1 with the blind-site expansion (rows 1309 and 1310), the physical normalization (V9), the comparison of the two flows (FI) and (MON), the inputs of (DET), and the account's premises (check 1288).
- X2 (OPEN). Numbers. The account fixes its constants by existence, in a written order: exponents, then L large, then the other constants, then g small (row 837 1.1). (W-TRAJ) needs K_0, the base datum, L, the torus floor and the margin (L^4 + 1) E(K_0) as numbers. None is on file.
- X3 (ARGUED). With X1 and X2, (W-TRAJ) is a finite and sufficient statement. It is still not a computation: its lattice has at least 10^24 sites in the most favourable reading (3.4). So X1 and X2 do not give a proof step by computation.
- X4 (OPEN; it is the crux). A carry from a coupling of order one to every finer cutoff. Only this would put a sufficient datum on a lattice of 10^5 sites. The account cannot give it: the ultraviolet stability theorem it rests on assumes that every effective coupling lies in (0, gamma] (row 837 1.1). Row 978 names what such a carry is: (NOCRIT) with an asymptotic-freedom climb. It is false for compact U(1), for the frozen groups and on the K7 lines (row 978). So it must read the Wilson SU(2) weight along the whole coupling path above the window. One finite computation at one coupling does not read that path.
- X5 (OPEN). A rigorous method of polynomial cost for the in-law quantity (KER) at a coupling of order one. Every such method on record needs a convergent expansion or a zero-free region first (M7). At the window those are open statements of the lane.

**6.2 Can a finite statement be proved sufficient?**

- In logic, yes (ARGUED). Lemma ONE-K is that proof, given (UNIV-K). (UNIV-K) is a statement about the ultraviolet. Row 1225 argues that it needs no estimate in the band. So a theorem "this one finite inequality gives (SEED-FP)" is a reasonable target. It is work on the account, not on the crux.
- The statement it would make sufficient is (W-TRAJ), at weak coupling. Row 1225 says of its cube: "side of order exp(c beta_0) lattice units at least", and "an infinite-volume statement about one lattice theory with no small parameter". So it can be proved sufficient, and it cannot be computed.
- A finite statement that is sufficient and of computable size needs X4. Even then it needs X5: by 5.1 the window pair costs at least 10^2408 operations with the best method on record.
- A different criterion would not help in size (GUIDE). The ceiling of row 705 Section 4 bounds every threshold of this kind by 1 (given two recalled facts on the Ising model; lead note of row 707). In the model of row 705 Section 5, S = 1 at the shape r = 2 sits at m a = 4.1 and m b = 8.2. At beta = 2.3 that is a torus of about 4 x 8^3. Its slice has 256 sites, and Lemma DIM gives at least 10^154.

**6.3 Where a kernel-checked computation can serve this chain (ARGUED).**

- The numeric constants of the hand proofs: 1/1650 and the other thresholds, 16.83 and 0.172 of the published ascent, 35 pi^2 < 352 (row 1315), Bessel-ratio bounds, the threshold 2 W_3 = 1.0109 in CA-FAIL, with W_3 the three-dimensional lattice integral (check 1075). These are small interval checks. T1 is enough.
- An exact small counterexample that kills a proposed inequality (GOAL.md allows it).
- Not the seed.

## 7. Verdict

**Decision.** No. With what is on file, a computation checked by the Lean kernel cannot discharge the seed of the mass-gap chain.

| Question of the brief | Answer | Label |
|---|---|---|
| Is a statement on file genuinely finite and sufficient through checked results? | No. Each sufficient form has the quantifier "every late cutoff". Each finite form gives a gap at one coupling. | ARGUED (2.2) |
| Which finite statements exist? | (KER) in five dresses: C1', C2', C3', C6, C7; and the block test C8 | PROVED by reading (2.1) |
| Nearest finite statement with checked sufficiency | (W-FIX): tori 10 x 20^3 and 20^4 at beta = 2.3; it gives a lattice gap at beta = 2.3 only | sizes GUIDE (3.1) |
| Nearest finite statement on the path | (W-TRAJ): sides at least 2 L^12 at the account's weak coupling; sufficiency OPEN | PROVED by reading; sizes from the account's floor (3.4) |
| Best certificate method | M1, exact contraction; at least 10^65 operations for the smallest admissible pair, 10^2408 and 10^4816 at the window | Lemma DIM PROVED here; "best" ARGUED |
| Does Theorem O block it? | It blocks local loop-equation certificates. By Remark OS their patch must be as large as a seed box. It does not block M1. | PROVED on file and here (4.1, M3) |
| Do (26) to (30) of row 1323 block it? | They block Gaussian enclosures on the trajectory, the only kind of tool I can name at the size of (W-TRAJ). They do not bear on M1 at the window. | PROVED on file (4.1, M4) |
| What would Lean check, on which trusted base? | L1 to L5; T1, T2 or T3; none reaches the cost | 5.2, 5.3 |
| What is missing? | X1 and X2 for a sufficient finite statement; X4 for one of computable size; X5 for a way to compute it | OPEN (6.1) |
| Can a finite statement be proved sufficient? | Yes in logic, through (UNIV-K); it then sits at weak coupling and cannot be computed | ARGUED (6.2) |

**What would change this verdict.** A proof of X4, which is the crux in another form. Or a rigorous method of polynomial cost for (KER) at a coupling of order one. Neither is on file. Neither has a route on file.

**Not done in this row.** I did not read the primary text of the published papers, of the account, or of Balaban. I did not survey Mathlib. I did not look for an exact-contraction algorithm beyond the treewidth argument. The claim "best method" is a claim about the methods I know. Nothing here is checked by a second model.

**Credits.** Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy: the one-scale window, its ascent and Theorem 7.59. Sussman and Alpoge (with Claude and Codex as authors of their text), after Balaban: the account, its tori and its floor. Osterwalder and Seiler, Luscher: the transfer operator. Frohlich, Simon and Spencer: long-range order of the three-dimensional O(4) model. Dobrushin and Shlosman: the block criteria. Anderson and Kruczenski; Kazakov and Zheng: the loop-equation bootstrap. Athenodorou and Teper; Teper; Lucini, Teper and Wenger: the published lattice values. Remondiere: the Lean-formalized implication. Hales and coauthors: Flyspeck. In the lane: Claude Fable 5.2 (rows 697, 705, 720, 978: Theorems S, SH, D-shape, ZD-c); Codex gpt-6-astra (rows 699, 760, 767: Corollary S3', Theorems O, A, B); gpt-6.2-astra (rows 1143, 1161, 1321, 1323); Claude Opus 5.5 (rows 837, 916, 1072, 1225, 1258, 1295: the finish line, Lemma ONE-K, CA-FAIL, Corollaries AU1 and AU2, and the checks cited); Codex gpt-6-luna and gpt-6.1-sol (readings 706, 755, 1126, 1218).

## Appendix A. The guide runs

Four short runs, each of seconds on one core, in a scratch folder outside the repository. They guide sizes. No proof step uses them.

1. Sizes of 3.1. The script below. Inputs are the five published rows quoted in `library/prior/gap-seed-size.md`.
2. Bessel ratios and tails of 3.1 and M1: I_d(beta) by its power series in double precision.
3. The patch condition of M3: Phi(n) = 8 d_1 + 4 d_2 + 2 d_3 + d_4 with d_i = 2 g(n; B_i) - g(2n; B_i) on the boxes B_i of Lemma Z3 of row 720, in the same gas model, tested against 8 n^4 tau/(a b^3).
4. The window of 3.2: the least T_0 with 2 g(T_0; s^3) - g(2 T_0; s^3) <= gamma s^3 for cubes of sides 2 T_0, 4 T_0 and 8 T_0, in the same gas model.

```python
# GUIDE only. Ideal Bose gas model of the thermal sum of the periodic cube.
import math, numpy as np
data=[(2.2986,.36778,1.224),(2.3714,.29023,1.025),(2.427,.24013,.8469),(2.509,.18011,.6563),(2.60,.13283,.5001)]
shapes=[(2,1/1650.),(3,1/100.),(4,1/25.),(6,1/10.),(24,3/10.)]
def g(a,b,sig,m0):   # log(1+S(a; b^3)); sig = a*sqrt(sigma), m0 = a*m(0++)
    K=max(12,int(math.ceil(4.0*b/a))+4)
    k=np.arange(-K,K+1)
    k2=(k[:,None,None]**2+k[None,:,None]**2+k[None,None,:]**2).astype(float)
    p2=(2*math.pi/b)**2*k2
    tot=0.0
    for m,deg in ((m0,1),(5.55*sig,5),(max(1e-9,sig*sig*b-math.pi/(3*b)),3)):
        tot+= -deg*np.log1p(-np.exp(-a*np.sqrt(m*m+p2))).sum()
    return tot
for beta,sig,m0 in data:
    for r,t in shapes:
        a=3
        while 2*g(a,r*a,sig,m0)-g(2*a,r*a,sig,m0) > math.log1p(t): a+=1
        print(beta,r,a,r*a)
```

RESULT: Row 1326 (Claude Fable 5.2 max, sizing study; author only, checked by no one; four guide runs of seconds, no large computation). Decision: NO. With what is on file, a computation checked by the Lean kernel cannot discharge the seed of the mass-gap chain. Step 1 (ARGUED): no statement on file is both genuinely finite and sufficient through checked results. Every sufficient form (the published window (A-B*) on the trajectory, (N-phys) of row 1161, Theorem ZD-c, row 1321 (16), row 1323 (29)) has the quantifier "every late cutoff". Every finite form (the lane's Phi_B(a) <= log(1 + t(r)), the published (B**) at one coupling, row 1161's one-cube test with n >= 2^70, Theorem ZD (A) and (C')) gives a gap at one coupling only. The one statement that would make one cutoff enough, (SEED-L) with Lemma ONE-K, rests on (UNIV-K), which is OPEN, and its datum has no numbers. Sizes: the smallest window instance (GUIDE) is beta = 2.3 with tori 10 x 20^3 and 20^4, Phi_B to about 3.6e-4 absolute, one part in 10^10 of the free energy; the one-cutoff datum has at least 2 L^12 sites on a side (1.2e17 at L = 25) at the account's weak coupling. Methods: exact contraction costs at least 2^(2 abs(slice) + 1) (Lemma DIM, PROVED here, unchecked), that is 10^2408 and 10^4816 at the window and 10^65 for the smallest pair Theorem SH admits; Theorem O with Remark OS (PROVED here from row 760, unchecked) shows that a local loop-equation certificate needs a patch as large as a seed box; row 1323 (26)-(30) block Gaussian enclosures on the trajectory; CA-FAIL blocks boundary-uniform block criteria at every window coupling. Trusted base stated (kernel with GMP; native_decide adds Lean.ofReduceBool, the compiler and the C toolchain; or a verified external checker); none reaches the cost. Missing: (UNIV-K) and explicit constants for a sufficient finite statement, which would still sit at weak coupling; a carry from a coupling of order one, which is the crux, for one of computable size; a rigorous method of polynomial cost for in-law quantities. OPEN: the seed, the mass gap. Output library/gap-verified-compute-sizing-fable.md.
