# Direction 7 (Fable): the next attack on the gap after the (W-mix) rows 1600-1607

Row: FINISH.md row 1610. Author: Claude Fable 5.2 (direction author, one of two; the other file `library/gap-direction7-astra62.md` was not read).
Date: 2026-11-27. Status of this file: complete for this run. It was written as the work proceeded; sections were appended in order. Row 998 is cited through the passages copied in `parts/gap.md`.

Labels used: PROVED (complete proof in this file), ARGUED, GUESSED, ON FILE (with the row).

## 0. Reading log

(appended as files are read)
- R1. FINISH.md rows 1597-1611: RESULT texts read in full (rows 1610, 1611 have none; 1608 stopped, 1609 not run).
- R2. `library/gap-wmix-solve-fable.md` (row 1600): read in full, both passes.
- R3. `library/gap-k2-tool-design-fable.md` sections 2 and 3.1 (row 1468): the seed, Fact PUR, the consumer.
- R4. `library/gap-direction6-fable.md` (row 1597): read in full ((PZ), (PZ-why), (WB), Stage C table, Lemma EVEN, Remark TEMP).
- R5. `library/gap-wmix-solve-neon-check-opus.md` (check 1605), `library/gap-wmix-solve-astra62-check-fable.md` (check 1606), `library/gap-wmix-obstruct-astra62-check-opus.md` (check 1607): each read in full.
- R6. `library/gap-wmix-obstruct-astra62.md` (row 1603): sections 2, 3 and the closing paragraphs read (statements (5), (6), (7), the short-period statement, the ARGUED selection paragraph). Sections 1 and 4 known through check 1607 only.
- R7. Rows 1601 and 1602: known through their checks (1606, 1605) and their RESULT texts. Their files were not read line by line. Row 1604: RESULT text only (a reading row). `library/gap-wmix-wall-astra62.md` (row 1608, stopped): not read, not cited.
- R8. `parts/gap.md`: State of attack, Routes tried, Lead rules, Route registry, Test table, The exact price (read in full at L1-104 and L223-330).
- R9. RESULT texts read: rows 708, 710, 754, 1378, 1386, 1442, 1443, 1515-1523, 1526-1533, 1538, 1542, 1544, 1553, 1556. Passages read in the files: row 708 (`library/gap-mid-max.md` L52-67, L100-140, L209-215: (VIR_K), Theorem TR, Remarks CH and LEV, (CAS)); row 1198 (`library/gap-mini-solve-h-fable.md` 2.1, Remark TH); row 1386 (`library/gap-mech-direction2-fable.md` 2.1, (SV-Z)); row 1468 (sections 2, 3.1, 5, 6); check 1453 (`library/sa-ym4-lean-trajectory-check-astra62.md`, terminal band, BND-1, the shifted lattice, BND-2); row 697 (`library/gap-crux-restate.md`, outline and Theorem S lines); registry rows W-CUBE-23, R10, R11, R12, TWO-PER.
- R10. Not read: `library/gap-direction7-astra62.md` (as instructed); the account; the Lean sources; the bodies of rows 931, 975, 789, 859 (cited below through the files that quote them, and marked so).

Method of this row. Before each search I wrote down a candidate attack. Then I searched FINISH.md and library/ for it. Section 2.1 lists the eight candidates and where each is on file. Counts from grep are not readings; where I cite a row I say what I read.

## 1. What rows 1600 to 1607 established

Notation as in row 1468 section 3.1. P_K = Z_+(2u)/Z_+(u)^2 on the spatial torus (Z/n)^3, n = l b^K, u = n/512, at the calibrated root beta_K. s(v) is the neutral thermal sum at time v: the sum over the excited neutral levels i of r_i^v, with r_i the ratio of the level's eigenvalue to the vacuum eigenvalue. The consumer reads s_K(u) <= 4/21 (Fact PUR, row 1468 3.1; ON FILE).

### 1.1 Proved and checked (hand proofs; each checked line by line by one reader of another provider; no Lean)

| # | Statement | Anchor | Scope note |
|---|---|---|---|
| E1 | For a positive kernel: (1 - d)^2 <= P <= 1 - d^2, with d the mean total variation distance of the half-period laws of the whole opposite slice at two independent ends. Also 1 - sqrt(P) <= H_two^2 <= d <= sqrt(1 - P) and the joint-to-product forms. | check 1605 Step 1 (Theorem 1A of row 1602); check 1607 Step 3 ((6) of row 1603) | The lower bound P >= (1 - d)^2 was ON FILE (row 1526 Theorem 1, check 1527 (i)). |
| E2 | At the target aspect, each bounded whole-slice two-sample criterion (mean total variation, beta-mixing, Hellinger, affinity, a bounded f-divergence, a tail of the log cost J) is equivalent to (PUR-io) over the allowed sides. | check 1605 Steps 2, 3, 6; check 1607 Step 3 ((7) and the tail form) | Only for thresholds that force P >= 1/2 + eps, at even aspect A >= A_0(eps), given the checked rows 705/707, 1368/1370, 1453, 1527. The object is the whole-slice law of row 1526, not the one-cell (H-two) of rows 1115-1123. |
| E3 | Unbounded divergences (I, L, I + L, chi^2) are strictly stronger than the seed on abstract positive kernels. -log P <= 2 min(I, L). | check 1605 Step 3 | I + L case ON FILE (row 1573, check 1579). Strictness is not shown for the Wilson kernel. |
| E4 | Whole-slice mixing of one bounded observable at a time gives no lower bound on P. Witnesses: tensor powers of a 2 by 2 positive kernel; a massive free scalar; positive neutral transfer kernels on the actual slice space at the actual aspect. | check 1605 Step 4; check 1607 Step 3 (item 6) | The witnesses are not the Wilson kernel. The one-cell (H-two-N1) in its on-file role (a hypothesis for (CONV)) is not touched. |
| E5 | P D_p P = 0 for the projection P on functions invariant under both gauge groups. So Lemma CORNER of row 1574 is identically zero and its "necessary test" controls nothing. | check 1605 Step 5 (4.1) | A correction to an on-file reading. It refutes no estimate. |
| E6 | The swap budget (H-swap), the premise of Theorem CONV-swap of row 1118, fails at every beta >= 23/10 for raw-link ownerships with at most 81 incident cells and no block containing a whole ring 2-torus. At the late calibrated roots the maximum incident swap defect tends to 1 in probability. | check 1607 Step 1 | Not covered: gauge-aligned or smoothed exchanges, whole cylinder ends, non-raw variables. |
| E7 | For a cell of fixed lattice size R, the two-sample core coefficient is bounded below by c_phi > 0 in the order lim inf over R of lim inf over K. Exponential clustering in lattice units, uniform in the cutoff, is false. | check 1607 Step 2 ((5) of row 1603), given rows 1375/1376 | It says nothing at a cell of physical size. |
| E8 | The mean total variation of whole faces tends to 1 at half-periods up to floor(beta_K^alpha), 0 < alpha < 1/16. | check 1607 Step 3, given row 1375 L144 and row 1153 (5) | These periods have zero physical length in the limit. |
| E9 | The chamber and corridor estimates (5)-(17) of row 1601 hold. They hold at every fixed coupling in every bounded finite-range compact-spin model: weak 4D compact U(1), 5D SU(2), the gapped twin, and models with long-range order. | check 1606 sections 2 and 4 | 22 items, 22 HOLD. Constants are not uniform in beta; "large r" starts above 10^(5,800,000). |

### 1.2 Proved, with one reader only or unchecked

| # | Statement | Anchor | Standing |
|---|---|---|---|
| U1 | Lemma HS: w_0(v)^(3/2) <= BC(v) <= w_0(v)^(1/2), with BC the Hellinger affinity of the neutral two-slice law at half period to the product of its marginals and w_0 = 1/(1 + s(v)). So the seed forces BC(u) > 0.769. | row 1600 section 2 | PROVED there by hand, unchecked. I read the proof and found no wrong line (a reading, not a check). The consumer half is Lemma M1 (Lean, rows 1356, 1359). |
| U2 | Lemma PT (product of blocks; the Lean pressure seed only for beta <= 19/432000000) and Lemma VT (S(2) <= Var(K)/(E K)^2 for two samples of the slice law). | row 1600 section 10 | PROVED there by hand, unchecked. Strong coupling only. |
| U3 | Remark M: closed pinned walls of density O(1/r) make the chambers exactly independent in every model of range at most 3. Remark DP: the wall-law term of (17) of row 1601 contains the one-test two-sample estimate at separation r(1 - o(1)) and a joint total-variation demand on O(r^3 (log r)^2) links. Remark T: (8)-(9) of row 1601 follow from a comparison with Haar on the support of the score. | check 1606 section 3 | PROVED in the check file by its one reader. Elementary (Markov property, data processing). |

### 1.3 Argued, or a search disposition

- A1. "Every neutral-reading route ends at (W-mix)" (row 1597 (PZ-why) reason 2): ARGUED there as a reading of the rows. U1 turns one half into a statement about the target: every proof of the seed proves near-product structure of the periodic two-slice law at typical ends. U1 is unchecked.
- A2. "The four attacks of row 1600 fail at one step, the lack of an explicit reference law": ARGUED there. Two of the four failing steps rest on leading-order GUIDE values.
- A3. Row 1604: no published method beyond the Dobrushin range has a plausible 4D gauge extension and supplies (W-mix). A reading row; a search disposition, not a theorem.
- A4. Selectivity paragraphs: section 6.3 of row 1602 was not checked (check 1605 Step 7). The closing paragraph of row 1603 is ARGUED and says that none of its statements is a selective input.
- A5. "The wall term carries the whole difficulty" (check 1606 4 (c)): PROVED as far as Remarks M and DP go; the sentence that (W-mix) is thereby "restated in a stronger form" is a reading.

### 1.4 Not established by these rows

- No form of (W-mix) at a physical scale is shown to fail (check 1607 RESULT, last line).
- The one-cell forms at a cell of physical size, (H-two), (CONV-two), (H-two-N1), (H-two-col), have no consumer and no refutation (check 1605 Step 7 item 1; row 1600 section 8).
- (FL), (CM_k), (R11), (R12), (K-I), (K-II), (PUR-io) and the gap are untouched.
- No estimate on the calibrated trajectory was proved in any of the eight rows.

### 1.5 Where a proof cannot go, and where it still can (my reading; ARGUED from 1.1 to 1.4)

Cannot go:
1. Around the near-product statement. By U1, a proof of the seed by any route proves that the periodic two-slice law is within Hellinger affinity 0.769 of a product at typical ends. So "a route that avoids (W-mix)" does not exist in this form (unchecked).
2. Through a bounded whole-slice two-sample criterion at the target aspect. By E2 each such criterion is the seed. A proof of one is a proof of the seed, and a reduction to one is no progress.
3. Through cells of fixed lattice size, raw-link swaps, or short periods. E6, E7, E8 close them on the trajectory.
4. Through one observable at a time on the whole slice. E4.
5. Through pinning and the Markov property alone. E9 with U3: such statements are true in models with long-range order, so they carry no mixing content.

Can still go (nothing in rows 1600 to 1607 excludes these):
6. A carry in the spatial size at fixed aspect, or in the coupling, that ends at the periodic seed. This is the (K-flow) kind of row 998, the amended (T-carry) of row 1597 B4, and (R11), TWO-PER, (CAS), (DRIFT) in their on-file forms.
7. A one-cell form at a cell of physical size with a consumer. Both halves are open.
8. One renormalization step in law at order-one coupling: (FL), (CM_k), (K-II).

What I take from the eight rows (ARGUED). They worked on the statement side of (W-mix). The statement side is now closed in this sense: the forms with a consumer are the seed (E2, U1), the microscopic forms are false (E6 to E8), the pinned forms are empty (E9, U3). No row touched the supply side: an estimate at a physical scale at late cutoffs. So the next attack must be judged by its supplier, not by its statement. Section 2 does that.

## 2. The next attack

### 2.1 Eight candidates written before searching, and where each is on file

I derived each of these before I searched for it. All eight are on file. That is itself a finding: I found no attack that the folder does not already hold.

| # | Candidate (as I wrote it) | Where it is on file (what I read) | Standing there |
|---|---|---|---|
| 1 | The seed in thermal form: the pressure over T^4 of the box at temperature 512/l must fall from the Stefan-Boltzmann value to about 1e-9; carry it down in temperature with the trace anomaly | (ANOM) of row 931 (seen through `library/gap-direction-max.md` L189 and row 1198 2.1, Remark TH, read); (N-phys) "3e-9" in the same remark; the Stefan-Boltzmann constant pi^2/15 in row 1603 section 3 (read) | "has the strength of the seed" (row 1198 2.1) |
| 2 | A margin in the equation of state, eps >= (3 + delta) p below first passage | Remark TH of row 1198: "the integrand condition of (ANOM)" | same; its monotone form is false near the deconfinement point (GUIDE there) |
| 3 | A stiffness with a classical term: the odd-Pfaffian twist n_12 = n_34 = 1, cost pi^2 beta, scale-free in four dimensions; iterate it in the size | (MON), (MON') of row 859 (`library/gap-brainstorm-max.md` L613, L650-655, read as quoted lines); D4 and x_kap of `library/gap-dim-carry-fable.md` L76, L201; C4 of row 1533 | "its carry is (K-flow) renamed"; flux half only |
| 4 | A lattice lower bound, uniform in the box, for the least action in the odd-Pfaffian sector | row 789 (E13), as cited by check 1541 item 4 (`library/gap-mech-selective-fact-fable-check-astra62.md` L98, read): c_* <= inf <= 17 pi^2/8 | proved there (I did not read row 789). I had re-derived it from the commutators of the four Polyakov lines through a site. Not counted and not written here. |
| 5 | Transport in the coupling with the action identity (Feynman-Hellmann), from the strong-coupling side | Theorem TR, Remarks CH, LEV, (VIR_K) of row 708 (read); Theorem U of row 710; rows 1515-1523 with (R11), TWO-PER, TR2 (RESULT texts) | "contains the locality of an excitation against the vacuum" (row 710); no method |
| 6 | Cut the box by spatial walls and write the purity as a mean of a product over chambers | Remark M of check 1606; the junction cost is Proposition J of check 1121 (through check 1607) | Markov property; the mean is carried by atypical junctions |
| 7 | A one-cell criterion in law at a physical cell with a local-to-global step | Theorem S of row 697 is the in-law local-to-global step, for a periodic cell (read: statement and Corollary S3); pinned cells: rows 1115-1123 (through row 1600 section 8) | the periodic form is the seed at one size; pinned forms have no consumer |
| 8 | An explicit reference law, or a trial vacuum, for Lemma M1 | row 1600 Attacks 5 to 8; row 1496 (through row 1600) | extensive overlap deficit |

### 2.2 Judgement first: no attack earns a proof row on the band

I judge that no gap attack deserves a proof row now (ARGUED; a judgement over the record, not a theorem). Reasons:
1. Rows 1600 to 1607 closed the statement side and left the supply side as it was (section 1.5).
2. Every line that could supply the band is on file with one standing: it is the target in steps, or it has no method at order-one effective coupling (rows 708, 998, 1198, 1386, 1468, 1515-1523, 1553, 1597). My eight candidates add no ninth line.
3. Row 1604 found no method outside the folder.
So my advice to the lead and the owner agrees with row 1597 in substance. The brief asks me to rank one attack and to start it all the same. Sections 2.3 to 2.6 and section 3 do that.

### 2.3 The attack I rank first: transport downward in the coupling on the trajectory's own lattice

Kind. It is a (K-flow) statement in the sense of row 998 (lead rule W2 in `parts/gap.md`): it starts at ultraviolet data and is carried through the band. It is the mirror of Theorem TR of row 708. Theorem TR starts at strong coupling and needs an upper bound on the rate at which levels fall. The mirror starts at the hot (weak-coupling, small-box) end and needs a lower bound on that rate.

Setting. Fix K, the lattice (Z/n)^3 with n = l b^K, and u = n/512. Vary only the bare coupling beta on this fixed lattice. The lattice at beta_K is the seed box. The same lattice at a larger coupling beta_h is a smaller physical box (check 1453, "The shifted lattice has the same integer size", read). Write G(t; beta) for the neutral thermal sum at real time t >= 1, so s_K(u) = G(u; beta_K).

**Target statement (T-down).** For one l and one g_0 and infinitely many K there are beta_h > beta_K, a continuous kappa >= 0 on [beta_K, beta_h] and t_h = u exp(integral of kappa over [beta_K, beta_h]) with:
- (HOT) G(t_h; beta_h) <= 4/21. In words: the lattice at the hot coupling is cold at the long time t_h.
- (VIR-down) for every beta in [beta_K, beta_h], at the time t(beta) = u exp(integral of kappa over [beta_K, beta]):
      d/dbeta G(t; beta) >= - kappa(beta) t d/dt G(t; beta).
  In field terms, at integer t (Lemma D1 below): t a_0(beta) - A_t(beta) >= kappa(beta) t Ebar_t(beta). Here A_t is the mean Wilson action of the neutral torus of period t, a_0 is the action of one time slab in the vacuum, and Ebar_t is the thermal mean of the level energies. In words: the neutral torus of period t holds less action than t vacuum slabs, by at least kappa times t times its thermal energy.
Then s_K(u) <= 4/21, the seed of (M-io-exists) (Theorem TR-down, section 3; PROVED given a regularity clause).

Why I rank it first (ARGUED; four structural points, each can be checked against the rows):
- (i) It reads the whole seed, in the consumer's own variable, on the consumer's own lattice. The twist-scheme candidate (3) reads the flux half only.
- (ii) Its window is [beta_K, beta_h], so every coupling in it is a late bare coupling. It never crosses the bare crossover near beta = 2.2. The tests that bind statements at one bare coupling (Proposition V, the K7 line; test table of `parts/gap.md`) do not bind it. The ascending consumers on file either end at a fixed bare coupling and then need (R12) (TR, TR2: rows 708, 1517), or cross every bare coupling from 1/25600 up to beta_K (TWO-PER, check 1516 (v)).
- (iii) It needs no comparison of two cutoffs. (A1) and (R12) do not enter: both ends are the same lattice.
- (iv) Its start (HOT) asks for the low levels of a small box at a long time. That is a weak-coupling statement about a gap of order g^(2/3)/L and a count of low levels. It is not (UV-TS) at the aspect 512 (row 1515: `library/gap-seed-direction-fable.md` L176-186, read as quoted lines: the supremum over K of s_K(u) is finite), which is a bound on the whole thermal sum of a hot box and is "bounded and not small". Budget (Corollary B, section 3): the integral of kappa must be at least log(512 [t_0/n + (1/gamma) log(21 N_0/4)]), a number near 7 for gamma near 4 and N_0 near 10 (GUIDE; the gap value 4.1167 g^(2/3)/L is the BELIEF I33 quoted in row 1386 2.1).
And along the characteristic the lattice stays cold (Remark CH-down), so (VIR-down) is asked only at cold times.

### 2.4 Is it equivalent to the seed? Yes in substance, and I say so

Proposition EQ-down (section 3; PROVED given the regularity clause) says exactly what the hypothesis is:
- (T-down) at K implies the seed at K, and implies that G is non-decreasing in beta at each point of the characteristic.
- The seed at K, together with "G is non-decreasing in beta along its own level curve through (u, beta_K)", implies (T-down) at K, with kappa read off the level curve.
So (T-down) is the seed plus a monotonicity of the cold thermal sum in the coupling. In the class of positive symmetric kernels the monotonicity does not follow from the seed (Example NE, section 3; PROVED), so (T-down) is strictly stronger there. For the Wilson kernel I cannot show that it is strictly stronger, and I cannot show that the monotonicity follows from the seed. The integrated form of (VIR-down) along the level curve is the seed as an identity. By the rule of 2026-11-22 this is no progress on the statement side. Row 998 says the same of every known (K-flow) form: "(CAS), (DRIFT), (MON'), (CVX) are the target in steps". (T-down) is one more member of that family. I do not claim a reduction.
What (T-down) changes is where a supplier must work (points (ii) to (iv) of 2.3). That is a statement about the supply side only.

### 2.5 Where it must fail

- A model whose normalized neutral spectrum does not depend on beta (the free photon of the test table in `parts/gap.md`, "a rate or a drift that the photon does not have"). PROVED, one line: then d/dbeta G = 0 and - t d/dt G > 0 wherever G > 0, so (VIR-down) forces kappa = 0, t_h = u, and (HOT) becomes "the box is cold at the consumer's aspect at beta_h". That fails by the massless floor (Lemma FLOOR of row 988, as cited in `parts/gap.md`; not re-read).
- Weak 4D compact U(1). ARGUED: the photon levels do not depend on beta; the dependence on beta sits in flux and monopole terms, which do not change the low levels of a cold box at leading order. So the rate is zero to that order and (HOT) fails as for the photon. I did not prove the monopole part. First failing line: (VIR-down) with any kappa whose integral meets the budget.
- 5D SU(2) at weak coupling. ARGUED: the box coupling at the scale of the lattice grows like beta n (row 1386 2.1: "J_5 has no logarithm and b(L) grows like L"). The low levels depend on beta through beta n only, with logarithmic slope at most 1/3 in size (GUESSED: the toron scaling carried over from four dimensions). Then the integral of kappa over [beta_1, beta_h] is at most (1/3) log(beta_h/beta_1), while the budget grows like (1/3) log(beta_h n). So the budget fails for every beta_1 with beta_1 n large. First failing line: the budget of Corollary B.
- 4D SU(2) in the perturbative part (the (g5) test of row 1553). ARGUED: the box coupling is beta - c log n. The same count gives a drift (1/3) log of the ratio of box couplings, which the hot gap cancels. So perturbative drift alone never meets the budget. The drift must come from sizes where the box coupling is of order one. This is the band, restated; it agrees with L4 of row 998 ("first-passage data lie below the floor").
- A neutral massless spectator (test (g4)). ARGUED: the low levels of the cold box are the spectator's, with rate zero. Fails, as it must.
- The gapped twin beta < 2/9. ARGUED, not proved: at strong coupling every level falls with beta (row 710, Proposition EL for the electric part). I did not prove (VIR-down) there.

### 2.6 The first buildable component, and the ones after it

| Component | Statement | Method | State after this row |
|---|---|---|---|
| C1, the consumer | Theorem TR-down (level form and thermal form), Corollary B, Lemma D1, Proposition EQ-down | elementary | BUILT in section 3, by hand, unchecked |
| C2, the hot end | (HOT) at one coupling beta_h for each late lattice: n m_1(beta_h) >= gamma and G(t_0; beta_h) <= N_0, with gamma, t_0/n, N_0 independent of K | the release down to the box scale, then the toron comparison of row 1143; the same port as (SV-Z) of row 1386 2.1, for the low levels and not for a twist ratio | NOT BUILT. The only bound I can prove now is useless: a Doeblin bound gives m_1 >= exp(- C beta n^3) (section 3, Remark DB). |
| C3, the weak part | (VIR-down) on the part of the window where the box coupling is large | the release; this is (VIR-top) of row 1515 with a sign | NOT BUILT; on file as "a weak-coupling carry with no consumer". Theorem TR-down is now its consumer. |
| C4, the band | (VIR-down) where the box coupling is of order one | NONE | OPEN. This is the crux. |

## 3. The first component, built: the consumer C1

All proofs in this section are by hand and unchecked. No Lean was run (there is no Lean on this machine). One floating-point guide run is recorded in 3.7; it is not a proof step.

### 3.1 Setting (S)

Fix the lattice (Z/n)^3 and an interval I of couplings. For beta in I let R_beta = P_0 T_beta be the neutral Wilson transfer operator. I use three properties. They are ON FILE in substance and I did not re-read their proofs: row 1468 3.1 uses (S1) and (S2) in Fact PUR; the Lean kernel is quoted in row 1600 section 8 (`Transfer.lean` L548-556).
- (S1) R_beta is positive semidefinite and trace class, and its top eigenvalue lambda_0(beta) > 0 is simple.
- (S2) For every integer v >= 1: Tr(R_beta^v) = Z_+(v; beta) = (1/8) sum over z of Z^z(v; beta), and Z^z(v; beta) is the Haar integral of exp(- beta S^z_v(U)), with S^z_v the sum over the plaquettes p of the torus (Z/n)^3 x Z/v of 1 - (1/2) eps^z_p tr U_p, eps^z_p = -1 on the seam of the twist z and +1 elsewhere.
- (S3) beta -> R_beta is real-analytic in operator norm (its kernel is the gauge average of exp(- beta times a bounded continuous slab action)).
Let 1 = r_0 > r_1(beta) >= r_2(beta) >= ... >= 0 be the ratios of the eigenvalues of R_beta to lambda_0(beta), in decreasing order with multiplicity. Put m_i = - log r_i in (0, infinity], and for real t >= 1

    G(t; beta) = sum over i >= 1 of r_i(beta)^t = sum over i >= 1 of exp(- t m_i(beta)).

The sum is finite by (S1). For integer t, 1 + G(t; beta) = Z_+(t; beta)/lambda_0(beta)^t. With n = l b^K and u = n/512, s_K(u) = G(u; beta_K).

### 3.2 Lemma D1 (the action identity). PROVED given (S) and the Rellich-Kato theorem (not rebuilt; the same input as row 710). ON FILE in substance.

For every integer t >= 1, log(1 + G(t; beta)) is differentiable in beta and

    d/dbeta log(1 + G(t; beta)) = t a_0(beta) - A_t(beta),

where A_t(beta) = [sum over z of Z^z(t) E^z_t(S^z_t)] / [sum over z of Z^z(t)] is the mean Wilson action of the neutral ensemble of period t, and a_0(beta) = - d/dbeta log lambda_0(beta).
Proof. Z^z(t; beta) is the integral of a smooth bounded function over a compact group, so d/dbeta Z^z = - Z^z E^z_t(S^z_t). Hence d/dbeta log Z_+(t) = - A_t. By (S1) and (S3), lambda_0 is a simple isolated eigenvalue of an analytic family, so it is analytic and positive, and a_0 is defined. Subtract t times it. QED
Relatives on file: Remark LEV of row 708 ("the action of one time slab in the vacuum minus its action in the level i"); Theorem U of row 710; row 754 ("log(1 + eps) has the same form"). I restate it because (VIR-down) is read through it.

### 3.3 Theorem TR-down, level form. PROVED given (S1).

Let beta_1 < beta_2 in I and E >= 1. Assume
(LEV-down) for every i >= 1: m_i(beta_1) >= E m_i(beta_2).
Then for every real t >= 1:

    G(t; beta_1) <= G(t E; beta_2) <= exp(- t (E - 1) m_1(beta_2)) G(t; beta_2).

Proof. For each i, r_i(beta_1)^t = exp(- t m_i(beta_1)) <= exp(- t E m_i(beta_2)) = r_i(beta_2)^(tE). Sum over i >= 1. For the second inequality, r_i^(tE) = r_i^t r_i^(t(E-1)) <= r_i^t r_1^(t(E-1)), because r_i <= r_1 <= 1. QED
Remark. (LEV-down) compares ordered levels at the two ends only. A pointwise form is: m_i(s) >= m_i(s') exp(integral of kappa over [s, s']) for all s < s' in the window, with E the exponential of the whole integral. Where the levels are differentiable this is - d m_i/dbeta >= kappa m_i: every level falls at least at the logarithmic rate kappa. Compare (LEV_K) of row 708: no level falls faster than the rate K.
Warning (ARGUED). The level form with one rate for all levels is too strong to be true. In a gapped theory a level that carries momentum 2 pi k/n has energy sqrt(M^2 + (2 pi k/n)^2) in lattice units, and at fixed n only M moves with beta. Its rate is the rate of M times M^2 over the energy squared, which is small for large k. So the usable form is the thermal form below, which weights the levels.

### 3.4 Corollary B (the budget). PROVED given (S1).

Assume (LEV-down) for the pair (beta_K, beta_h) with the factor E. Assume at the hot end: m_1(beta_h) >= gamma/n, and G(t_0; beta_h) <= N_0 for some real t_0 >= 1 and some N_0 >= 4/21 (so the logarithm below is non-negative and uE >= t_0). If

    u E >= t_0 + (n/gamma) log(21 N_0/4),

then s(u; beta_K) <= 4/21. With u = n/512 the condition is E >= 512 [t_0/n + (1/gamma) log(21 N_0/4)].
Proof. By Theorem TR-down, s(u; beta_K) <= G(uE; beta_h). For t >= t_0, G(t; beta_h) <= exp(- (t - t_0) m_1(beta_h)) G(t_0; beta_h) <= exp(- (t - t_0) gamma/n) N_0. At t = uE this is at most 4/21. QED
The same holds for the thermal form of 3.5 with E = t_h/u, because only the bound G(t_h; beta_h) <= 4/21 is used.

### 3.5 Theorem TR-down, thermal form. PROVED given (S1) and the regularity clause (R).

(R) G is continuously differentiable in (t, beta) for t >= 1 and beta in [beta_1, beta_2]. I did not prove (R) for the Wilson operator; row 1520 lists the regularity at non-integer periods as open. (R) holds for every finite truncation of the spectrum with differentiable levels.
Let kappa >= 0 be continuous on [beta_1, beta_2] and t(beta) = u exp(integral of kappa over [beta_1, beta]). Assume
(VIR-down) for every beta in [beta_1, beta_2]: d/dbeta G(t(beta); beta) >= - kappa(beta) t(beta) d/dt G(t(beta); beta).
Then beta -> G(t(beta); beta) is non-decreasing on [beta_1, beta_2]. So G(u; beta_1) <= G(t(beta_2); beta_2).
Proof. By (R) and the chain rule, the derivative of beta -> G(t(beta); beta) is d/dbeta G + kappa t d/dt G at the point (t(beta), beta). By (VIR-down) it is non-negative. QED
Remark CH-down (PROVED, same proof; the mirror of Remark CH of row 708). The hypothesis is used on the characteristic only. There G is at most its value at the hot end. If (HOT) holds, the lattice is cold (G <= 4/21) at every point where (VIR-down) is asked.
Remark FIELD (PROVED from Lemma D1, for integer t). d/dbeta G = (1 + G)(t a_0 - A_t), and - t d/dt G = (1 + G) t Ebar_t with Ebar_t = [sum over i of m_i r_i^t]/(1 + G). So at integer times (VIR-down) reads t a_0 - A_t >= kappa t Ebar_t. In spectral terms, where the levels are differentiable: sum over i of (- d m_i/dbeta - kappa m_i) exp(- t m_i) >= 0.
Remark GAS (GUIDE; a formula for one model, not a proof step). For a dilute gas of one particle of lattice mass M(beta) on the fixed lattice, G = n^3 (M/(2 pi t))^(3/2) exp(- M t). If M falls at the rate c, then (VIR-down) holds with kappa up to c (x - 3/2)/(x + 3/2), x = M t. At x = 30 this is 0.905 c. So in the cold gas the usable rate is close to the rate of the mass.

### 3.6 Proposition EQ-down (what the hypothesis is) and Example NE. PROVED given (S1), (R).

Assume (R). Note d/dt G < 0 wherever some level is finite.
(a) If kappa >= 0 and (VIR-down) holds at a point, then d/dbeta G >= 0 at that point. (One line: the right side of (VIR-down) is non-negative.) So (T-down) at K implies the seed at K (Theorem TR-down) and implies that G is non-decreasing in beta at every point of the characteristic.
(b) Put g = G(u; beta_1) > 0. Suppose the level curve of g through (u, beta_1) exists on [beta_1, beta_2]: a continuously differentiable tau with tau(beta_1) = u and G(tau(beta); beta) = g. Suppose d/dbeta G >= 0 on it. Then tau' = - (d/dbeta G)/(d/dt G) >= 0, the function kappa = tau'/tau is continuous and non-negative, its characteristic is tau, and (VIR-down) holds along it with equality. If g <= 4/21, (HOT) holds at t_h = tau(beta_2).
Proof of (b). Differentiate G(tau(beta); beta) = g. QED
Reading. Up to the choice of curve, (T-down) at K is: the seed at K, and the cold thermal sum of the fixed lattice does not fall as beta grows along [beta_K, beta_h]. The integral of kappa is then log(tau(beta_h)/u), the factor by which the cooling time grows from beta_K to beta_h. So the integrated form is the seed as an identity. Its relatives: (ANOM) of row 931, called "EQUIVALENT to the SH seed" in `library/gap-direction-max.md` L147; (MONO-Delta) of row 720 (monotonicity in beta as the positivity of the interaction measure; seen through `library/gap-afield-b-max.md` L99); (MON_u) of row 1520.
Example NE (PROVED; the monotonicity does not follow from the seed for positive kernels). Take the 2 by 2 kernels k_r = (1/2)[[1 + r, 1 - r], [1 - r, 1 + r]], 0 < r < 1, with eigenvalues 1 and r and positive entries (the kernels of Theorem 3 of row 1602). Let r(beta) = rho exp(- (beta - beta_1)) with rho^u <= 4/21. Then G(t; beta) = r(beta)^t, the seed holds at beta_1, and d/dbeta G = - t G < 0 everywhere. By (a) no kappa >= 0 satisfies (VIR-down) at beta_1. So in this class (T-down) is strictly stronger than the seed. For the Wilson kernel I have no such separation and no proof of the monotonicity.

### 3.7 Remark DB, and the guide run

Remark DB (ARGUED; standard, constants not checked; it only shows why C2 is not free). The kernel of R_beta is positive with ratio of supremum to infimum at most rho = exp(beta Omega), Omega <= 12 n^3 twice the number of weighted plaquettes of one slab. The ground-state transform is then a Markov kernel with a Doeblin constant rho^(-2), so m_1(beta) >= exp(- 24 beta n^3). In Corollary B this gives a budget of order beta n^3 for log E. It is useless. C2 needs the true small-box gap, of order g^(2/3)/L by the belief I33.
Guide run (floating point; outside the repository; one process, a few megabytes; not a proof step, not a verification record). File: `dir7-guide/guide.py` in the lead's scratch folder of this session. 2000 random finite spectra: the two inequalities of Theorem TR-down had 0 violations. 2000 random families m_i(beta) = mu_i exp(- c_i beta) with every c_i >= kappa_0: the function beta -> G(u exp(kappa_0 beta); beta) was non-decreasing in all of them. The value 0.905 of Remark GAS was reproduced.

### 3.8 How far the component got

- C1 is built: the consumer exists in two forms, with its budget, its field form, and the exact statement of what its hypothesis is.
- C2, C3, C4 are not started. C2 and C3 have a method (the release at weak box coupling). C4 has none.
- Nothing in this section is selective by itself: Theorem TR-down holds for every positive transfer family. The selective statements are the hypotheses (VIR-down) on the band and (HOT), and neither is proved.
- No open input moves: (PUR-io), (R10), (R11), (R12), (K-I), (K-II) stand as before.

## 4. Next rows, and notes for the lead

I name no proof row on the band (2.2). Two rows could follow. The second is the owner's call.

**Row A. Cross-provider check of this row.** Check, in this order: (i) section 1 against the three check files and row 1600: is each line of 1.1 to 1.4 in the right class (checked, one reader, argued)? (ii) Lemma D1, Theorem TR-down in both forms, Corollary B, Proposition EQ-down, Example NE, line by line; is clause (R) needed, and can it be proved for integer times with a discrete schedule? (iii) Is Theorem TR-down on file under another name ((ANOM) of row 931, (DRIFT)_c of row 975, the step-scaling part of row 720 Part 2, which I did not read)? If yes, strike "new as text". (iv) The four points of 2.3: does an ascending consumer on file reach the trajectory lattice without crossing the bare crossover and without (R12)? (v) The failure lines of 2.5: the compact U(1) line and the 5D line are ARGUED or GUESSED; prove or refute each. (vi) Break test: an inequality for t a_0 - A_t from below on a cold neutral torus at a late bare coupling, by any method that fails for the free photon; or the first line where three attempts fail. Decisive outcome: if (vi) returns a bound with a method, C4 has a first lemma and a band proof row opens; otherwise the judgement of 2.2 stands.

**Row B (owner's call; I do not queue it). C2, the hot end.** Statement: for the release witnesses and one l, at all late K there is beta_h >= beta_K with n m_1(beta_h) >= gamma and G(t_0; beta_h) <= N_0 on the lattice (Z/n)^3, n = l b^K, with gamma, t_0/n and N_0 independent of K. Method: the release down to the box scale, then the toron comparison of row 1143 for the low levels (the port named in row 1386 2.1 for (SV-Z)). By the lane's rule 0 this row moves no open item while C4 has no method; rows 1386 and 1515 declined its relatives for that reason, and I agree. Its one merit: with C3 it would be the first proved statement that is selective, at a physical size, at late cutoffs and in the consumer's variable. That would change the inventory of Proposition NEG of row 1386, not the seed.

For the lead (I edited nothing but this file):
1. A trigger with a complete consumer could be added to the consolidated list of row 1597: "(T-down): a lower bound for t a_0 - A_t against kappa t Ebar_t on cold neutral tori at late bare couplings, with a method that fails for the free photon". Its consumer is Theorem TR-down with (HOT), which ends at (M-io-exists) with no (R12) and no (A1). It is the lower half of the ratio whose upper half is (R11).
2. Check 1541 item 4 cites row 789 (E13) for the uniform bound on the odd-Pfaffian action. Row 1533 C4 and `gap-dim-carry-fable.md` L201 still say "not attacked" and "not rebuilt". One cross-reference would stop a later row from re-deriving it, as I did.
3. Under the owner's rule of 2026-11-13 the hand proofs of section 3 cannot land as a proof note without a compute or Lean record. They are short; `lean/gapchain` already has the spectrum (BoxSpectrum, per row 1600 section 8). I did not write Lean.

## 5. Labels

| Statement | Label | Anchor |
|---|---|---|
| Section 1.1, each line | ON FILE, checked as stated there | checks 1605, 1606, 1607 (read in full) |
| Section 1.2 | ON FILE; proved by one author or one reader | row 1600; check 1606 section 3 |
| Section 1.5, items 1 to 8 and the closing reading | ARGUED | 1.1 to 1.4 |
| "All eight candidates are on file" | ON FILE for each anchor as read; the table says what was read | 2.1 |
| "No gap attack deserves a proof row on the band now" | ARGUED; a judgement | 2.2 |
| The four structural points of 2.3 | ARGUED | 2.3 |
| Lemma D1 | PROVED here given (S) and Rellich-Kato; ON FILE in substance | 3.2 |
| Theorem TR-down, level form; Corollary B | PROVED here, unchecked | 3.3, 3.4 |
| Theorem TR-down, thermal form; Remarks CH-down, FIELD | PROVED here given (R), unchecked; (R) not proved for the Wilson operator | 3.5 |
| Proposition EQ-down; Example NE | PROVED here given (R), unchecked | 3.6 |
| "(T-down) is the seed plus a monotonicity; its integrated form is the seed as an identity" | PROVED as stated in 3.6 (a), (b) | 2.4, 3.6 |
| "(T-down) is strictly stronger than the seed for the Wilson kernel" | NOT CLAIMED; I cannot decide it | 2.4 |
| Failure for a beta-independent spectrum | PROVED (one line) given Lemma FLOOR as cited | 2.5 |
| Failure for weak 4D compact U(1); for a massless spectator | ARGUED | 2.5 |
| Failure for 5D SU(2) | ARGUED, with one GUESSED input (toron scaling in five dimensions) | 2.5 |
| Budget "near 7"; Remark GAS; the warning in 3.3 | GUIDE or ARGUED; no proof uses them | 2.3, 3.3, 3.5 |
| Remark DB | ARGUED; not used | 3.7 |
| (HOT), (VIR-down) on any part of the window | OPEN; not proved at any coupling | 2.6 |

Not done in this row: no Lean; no numeric run inside the repository; no web search; the files of rows 1601, 1602, 931, 975, 789, 859, 720 Part 2 and the account were not read (rows 1601 and 1602 are known through their checks); `library/gap-direction7-astra62.md` was not opened. I did not prove (R), (S1) to (S3), or any estimate on the calibrated trajectory.

Provenance: Claude Fable 5.2, laptop subagent of the lead session; author only, checked by no one; hand proofs; one floating-point guide run outside the repository; nothing committed, pushed or posted; no other file in the repository written. Run on 2026-11-27.

RESULT: Row 1610 (Claude Fable 5.2; author only, unchecked; no Lean; one float guide run outside the repo). Letters as in rows 1600-1603: (a) a proof, (b) another route to the gap, (c) a disproof or obstruction, (d) a built tool.
Outcome: NONE of (a), (b), (c); (d) only as the consumer C1 of the attack ranked first. No open input moves.
Step 1: rows 1600-1607 closed the statement side of (W-mix): bounded whole-slice forms at the target aspect are the seed (checked), forms at fixed
lattice size, raw-link swaps and short periods fail (checked), pinned-wall forms are the Markov property (one reader), and the seed forces affinity
> 0.769 (row 1600, unchecked). No row touched the supply side; no physical-scale form is shown to fail.
Step 2: eight candidates derived before searching are all on file. Judgement: no attack earns a proof row on the band. Ranked first: (T-down),
transport downward in the bare coupling on the trajectory's own lattice, from a hot small box that is cold at a long time, with a lower bound on the
rate at which cold thermal sums respond to the coupling. It needs no (R12) and no (A1) and stays at late bare couplings. It is the seed plus a
monotonicity (Proposition EQ-down), so it is the target in steps, not a reduction; it fails for a beta-independent spectrum (proved) and, as argued,
for weak 4D compact U(1) and 5D SU(2).
Step 3, proved by hand: Lemma D1 (action identity), Theorem TR-down (level and thermal forms), Corollary B (budget), Proposition EQ-down, Example NE.
Not built: the hot end C2 and the weak part C3 (both have a method), the band C4 (no method). Open: (PUR-io), (W-mix), the gap.
