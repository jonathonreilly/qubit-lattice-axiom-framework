# Row 1600: solve row on (W-mix)

Author: Claude Fable 5.2 (laptop Claude subagent), started 2026-11-27.
Brief: FINISH.md row 1600, read from the lead's brief file (same text as the row).
This file is the only file this row writes. It is written as the work proceeds.

Status labels: PROVED (complete proof in this file), ARGUED, GUESSED, ON FILE (with the row).

## 0. Log

- Step 0. File created before any reading.
- Step 1. Read library/gap-direction6-fable.md in full (row 1597): (PZ-why) reason 2, bar (WB1)-(WB3), Lemma EVEN, Remark TEMP, Stage B3, Stage C table.
- Step 2. Read row 1584 (13.1)-(13.6), 2.4, 2.5; row 1468 3.1 (seed, Fact PUR) and 4.3 ((K2-STEP), (CM_k)); RESULT texts of rows 1120, 1121, 1123, 1510, 1566, 1576, 1579.
- Step 3. Read registry rows R10, R11, R12, TWO-PER; RESULT texts of rows 754, 760, 1496, 1498, 1501, 1502, 1511, 1514, 1517, 1519, 1522, 1523, 1526, 1527. Grep counts for bootstrap, loop equations, modern mixing tools: all on file.
- Step 4. Four attacks of my own, written in sections 2 to 5 below. Each stops at a line that is on file.
- Step 5. Verdict and RESULT written.

## 1. The estimate, as read

Sources read in full: row 1597 (`library/gap-direction6-fable.md`). Read in part: row 1584 (13.1)-(13.6), 2.4, 2.5; row 1468 sections 3.1 and 4.3. Read as RESULT text only: rows 754, 760, 1120-1123, 1496, 1498, 1501, 1502, 1510, 1511, 1514, 1517, 1519, 1522, 1523, 1526, 1527, 1566, 1576, 1579; registry rows R10, R11, R12, TWO-PER, W-CUBE-23. Not read: the bodies of those rows, Lemma TS3 and Lemma JI line by line, (FL) in its file, `lean/gapchain`. No file named `library/gap-wmix-*` other than this one was opened.

Notation. X is the slice field space with Haar measure. T is the Wilson transfer operator, P_0 the neutral projector. Z_+(v) = Tr(P_0 T^v). lambda_0 is the top eigenvalue of P_0 T. s(v) = Z_+(v)/lambda_0^v - 1. w_0(v) = 1/(1 + s(v)) is the vacuum weight at period v. The consumer reads s_K(u) <= 4/21 (Fact PUR, row 1468 3.1; ON FILE).

(W-mix), the form used below (ON FILE in kind: row 1584 (13.4), third line of the table; rows 1169 and 1173 use "the affinity of the joint law to the product of marginals"). Let v be even and B = P_0 T^(v/2), with kernel b(x, y) >= 0. Put q(x, y) = b(x, y)^2 / Z_+(v). This is the law of the pair of slices at times 0 and v/2 in the neutral ensemble of period v, lifted to X x X with uniform fibres over the gauge and centre orbits. Let nu be its marginal. BC(v) is the Hellinger affinity of q and nu x nu, that is, the integral of sqrt(q nu x nu). (W-mix, eta) at period v: BC(v) >= 1 - eta.

## 2. Attack 1: is there a route that does not need (W-mix)? No (PROVED), so outcome (b) and outcome (a) are one target

**Lemma HS (Hellinger sandwich). PROVED here; ON FILE in substance.** For every even v:

    w_0(v)^(3/2) <= BC(v) <= w_0(v)^(1/2).

Proof. A = B / sqrt(Z_+(v)) is positive semidefinite, has Hilbert-Schmidt norm 1, kernel a >= 0, and q = a^2. Its eigenvalues are sqrt(w_i) with w_i = mu_i^2 / sum_j mu_j^2 for the eigenvalues mu_i of B; the largest is sqrt(w_0). Let psi_i be an orthonormal eigenbasis; psi_0 >= 0 can be chosen because the kernel is nonnegative (replace psi by |psi|; the form does not decrease). Then nu(x) = sum_i w_i psi_i(x)^2. On the support of nu put h = a / sqrt(nu x nu) and (Hf)(x) = integral of h(x, y) f(y) nu(dy). The map g -> g / sqrt(nu) is unitary from L^2(dx) on the support to L^2(nu) and carries A to H. So H is positive semidefinite with norm sqrt(w_0). The constant 1 is a unit vector of L^2(nu), and <1, H 1> = integral of a sqrt(nu x nu) = BC(v).
Upper bound: <1, H 1> <= norm(H) = sqrt(w_0).
Lower bound: <1, H 1> = sum_i sqrt(w_i) <1, phi_i>^2 >= sqrt(w_0) <1, phi_0>^2 with phi_0 = psi_0 / sqrt(nu). And <1, phi_0> = integral of psi_0 sqrt(nu) dx >= sqrt(w_0) integral of psi_0^2 = sqrt(w_0), because nu >= w_0 psi_0^2 and psi_0 >= 0. QED

Consequences (PROVED, arithmetic).
- Consumer side. BC(u) >= 11/12 gives w_0(u) >= 121/144, so s_K(u) <= 23/121 <= 4/21 (483 <= 484). In total variation: TV(q, nu x nu) <= 1/12 is enough, since BC >= 1 - TV. No rate, no supremum over ends, and no local-to-global theorem is needed. One number at one period at typical ends is the whole input.
- Necessity. s_K(u) <= 4/21 gives BC(u) >= (21/25)^(3/2) > 0.769. So every proof of the seed, by any route, proves (W-mix, 0.231) at period u. Wherever a later step makes s small (Theorem S on larger tori), the same bound makes eta small there: eta <= 1 - (1 + s)^(-3/2) <= (3/2) s.

Reading. (W-mix) at typical ends is the seed in other words. The sentence of row 1597, "every neutral-reading route ends at one estimate", was ARGUED there as a reading of the rows. With Lemma HS it is a theorem about the target and not about the routes. Outcome (b), "a route that does not need (W-mix)", does not exist in this form.
What is on file (rule: equivalent is not progress): the squared-kernel pair law and its affinity to the product of marginals are rows 1169, 1171, 1173 (6); the identity P_K = E e^(-J) is row 1573 (1); the Hellinger identity is row 1373 and row 1526 Theorem 1; the cell forms are Lemmas TS2 and TS3 of check 1120. Greps for "w_0^(3/2)" and "vacuum weight" with a two-sided bound found no line with these constants, but I did not compare line by line with rows 1169 to 1173. I count Lemma HS as a restatement with explicit constants. It moves no input.
Selectivity of the form itself (ON FILE: rows 1573, 1576, check 1579): it holds at the gapped twin beta < 2/9; it fails for weak 4D compact U(1) and for a neutral massless spectator, because s(u) is then large at u = n/512. This is the seed's own selectivity. The form adds none.

## 3. Attack 2: a comparison of two volumes that needs no vacuum. An identity (PROVED); positivity gives only the wrong direction

**Remark HD. PROVED, two lines; a variant of Remark TEMP (a) of row 1597.** For integers k >= 1 put Delta_k(u) = log Z_+(u) - (1/k) log Z_+(k u). Then

    (1 - 1/k) log(1 + s(u)) <= Delta_k(u) <= log(1 + s(u)).

Proof. log Z_+(v) = v log lambda_0 + log(1 + s(v)), so Delta_k(u) = log(1 + s(u)) - (1/k) log(1 + s(k u)), and 0 <= s(k u) <= s(u). QED

At k = 512 the second torus is n^3 x n. So the seed is, within the factor 511/512, the statement Z_+(n^3 x u)^512 <= (25/21)^512 Z_+(n^3 x n): the trace inequality Tr(P_0 T^(512u)) <= (Tr P_0 T^u)^512 is nearly an equality.
Where it stops. Transfer positivity in each of the four directions makes log Z convex and subadditive in each side length (ON FILE: Remark TEMP of row 1597; the exchange of axes is Lemma Z3, cited in row 1584 (13.1) as row 1332 and stated in the file of row 720). Both properties bound Delta_k from below. I found no inequality from reflection positivity that bounds it from above. A bound from above is the seed. Check 1585 (vi) found the same for front shifts: reflection positivity "also holds for compact U(1)". No row.

## 4. Attack 3: a carry in the coupling at a fixed lattice. The identity is exact; the estimate it needs is (R11)

D(beta) = -log P at fixed (n, u). Exact: D'(beta) = 12 n^3 u (e_u - e_2u), where e_v is the mean plaquette on the torus n^3 x v (plain periodic case; ON FILE in this form in row 754 and as transport in rows 1515 to 1523). D tends to 0 on these boxes at beta < 2/9 (ON FILE: check 1583 Step 10, as quoted in row 1597). So the seed at beta_1 follows from a bound on the integral of e_u - e_2u over [2/9, beta_1].
PROVED, trivial: for a spatial plaquette, |e_u - e_2u| is at most the trace distance of the two thermal states, which is at most 4 (1 - P) (the two states are rho and rho^2/P; their trace-norm difference is at most 2 (1 - p_0) <= 2 (1 - P), p_0 the top weight). This gives D' <= C n^3 u D. Integrated, the factor exp(C n^3 u (beta_1 - beta_0)) is larger than any starting value allows. The bound is useless unless n^3 u is replaced by a number of order log n.
First failing line: |<i| V |i> - <0| V |0>| <= C for the thermal levels i, with V the sum of the plaquettes of one slice. This says that the masses move with the coupling at a rate that does not grow with the volume. It is (R11), consumer TR2 of row 1517 (check 1519), and with TR2 it implies (NOCRIT) up to beta_1 (check 1523). It fails across a first-order point, so it is selective, and it is not known at any order-one coupling. I have no method for it. No row.

## 5. Attack 4: a search for a selective mechanism outside the three kinds of row 1553. None found

Each line is ON FILE with the row named; I add no theorem.
- A finite criterion in law from reflection positivity alone exists and is in Lean: Theorem S (row 1525). Its input is one finite-box inequality at one coupling. A certificate for that inequality at beta = 23/10 has a stated size of 640,000 links and degree above 22,000,000 (check 1501). It gives nothing on the trajectory without (R12).
- Loop equations with positivity: local certificates cannot bound the finite-size shifts (row 754 Proposition VB, argued there; row 760 Theorem O). The winding-loop recursion has no contraction (row 754, argued there).
- Correlation inequalities, a sign-free dual, a ferromagnetic split through the centre: checks 1556 (vi), 1579; none.
- Curvature and log-Sobolev routes: Bakry-Emery refuted above beta = 1 on a witness (row 1576 Theorem 4.2); multiscale forms on file (row 1496).
- Sharp-threshold and local-to-global tools (spectral independence, stochastic localization, block dynamics): named on file by grep (12, 8 and 13 files; I did not read what those files conclude). From what I know of these tools, each needs a supremum over pinnings or a monotone measure (ARGUED).
Background, ARGUED and not used in any proof: the massless phase of 4D compact U(1) is tied to a continuous one-form symmetry; SU(2) has only a Z_2 one-form symmetry, and a discrete symmetry forces neither a gap nor its absence. So I expect no symmetry statement to select the gap. The selector is the sign of the flow of the coupling, read over the order-one band. That is (K-II) of row 1386, or a certified finite computation. The file has no method with a stated finite cost for either, and I found none.

## 6. Verdict

Outcome reached: none of (a), (b), (c), (d).
- (a) not reached. I have no proof of (W-mix) at any coupling above the Dobrushin range.
- (b) not reached. By Lemma HS, a proof of the seed is a proof of (W-mix) at typical ends. There is no separate route.
- (c) not reached in a form that counts. Lemma HS is an explicit two-sided equivalence between one typical-ends form of (W-mix) and the seed. By the lane's rule it is a restatement, and its substance is on file. I found no on-file form of (W-mix) that fails on the trajectory beyond the supremum and cube forms already refuted (row 1072 as cited in the brief; row 1511 with check 1514; check 1121 Proposition J).
- (d) not reached. I designed no method. Each attack stops at an estimate that is on file: the seed (sections 2, 3), (R11) (section 4), (R12) or (K-II) (section 5).
What this row adds to the record: Lemma HS with its constants (the consumer accepts BC(u) >= 11/12 or TV <= 1/12, with no rate and no local-to-global step; the seed forces BC(u) > 0.769), and Remark HD. Both are unchecked hand proofs. Neither moves an input.
What I did not do: no numeric run, no Lean (none was needed and none was run), no literature search outside the folder, no line-by-line reading of the files listed as RESULT-only in section 1. A truncated grep count proves nothing about what the matched files say.

Labels.
| Statement | Label |
|---|---|
| Lemma HS and its two consequences | PROVED here by hand, unchecked; restatement; substance ON FILE (rows 1169, 1171, 1173, 1373, 1526, 1573) |
| Remark HD | PROVED here by hand, unchecked; variant of Remark TEMP (a), row 1597 |
| D' = 12 n^3 u (e_u - e_2u); D' <= C n^3 u D | identity ON FILE (row 754, rows 1515-1523); the trivial bound PROVED in one line for spatial plaquettes, constant not tracked for temporal ones |
| "No route avoids (W-mix) at typical ends" | PROVED (it is the lower bound of Lemma HS) |
| "No reflection-positivity inequality bounds Delta_k from above" | not proved; I found none |
| Section 5, each line | ON FILE; the summary is ARGUED |
| The one-form symmetry remark | ARGUED background, not used |

RESULT: Row 1600 (Claude Fable 5.2, laptop subagent; author only, unchecked; no numeric run, no Lean).
Outcome: NONE of (a), (b), (c), (d). (W-mix) is not proved and not refuted, and no component of a method is built.
Proved by hand: Lemma HS, w_0(v)^(3/2) <= BC(v) <= w_0(v)^(1/2), with BC the Hellinger affinity of the neutral
two-slice law at half period to the product of its marginals and w_0 = 1/(1 + s(v)). So BC(u) >= 11/12, or total
variation <= 1/12, gives s_K(u) <= 23/121 <= 4/21 with no rate and no local-to-global step; and the seed forces
BC(u) > 0.769, so every proof of the seed proves (W-mix) at typical ends and no route avoids it. This is a
restatement with constants; its substance is on file (rows 1169-1173, 1373, 1526, 1573). Remark HD: the seed is,
within a factor 511/512, the defect log Z_+(n^3 x u) - (1/512) log Z_+(n^3 x n); positivity bounds it from below only.
Four attacks stop at on-file estimates: the seed, (R11), (R12), (K-II). Open: (W-mix), (PUR-io), the gap.
No next row proposed.

---

# Second pass (lead instruction: read the named forms line by line, then attack the weakest accepted form)

## 7. Log of the second pass

- Step 6. Second pass started. The first pass above stays as landed.
- Step 7. Read line by line: check 1120 section 3.15 and Step 5 (Lemmas TS, TS2, TS3, forms (H-two), (H-two-N1), (H-two-col)); check 1121 Steps 5, 6, 8 (H-swap, Theorem CONV-swap, Proposition J, Lemma JI); row 1122 sections 1.2, 1.3, 2, 3 (Lemma AFF, Example PROD, Lemma BACK, Remark RHO, the decision 3.5); row 1510 sections 3.0-3.2, 4.1-4.3 (Proposition PC, Lemma REV, (FL)); row 1468 section 4.3 ((K2-STEP), (CM_k), (END-K2)); `lean/gapchain/RECEIPT-1f.md` and `lean/gapchain/GapChain/TheoremS.lean` L318-345, L425-540, L660-760 (BoxSpectrum, TorusData, seed, phi, seed_of_phi); rows 677, 685, 988, 991 (Route Z and its Schwarz form); RESULT texts of rows 1340, 1353, 1354, 1473.
- Step 8. Sections 8 and 9 written: the forms with their consumers, and the weakest accepted form.
- Step 9. Section 10 written: four attacks on the periodic form (Lemma PT, Lemma VT, a conditional Poincare step, the w-step reference). Before writing each I searched the folder; the Schwarz zero-free route, which I had re-derived, is on file and is not counted.
- Step 10. Section 11 and the updated RESULT written.

## 8. The forms of (W-mix), exactly, each with its consumer (read line by line this pass)

Setting of the pinned forms (rows 1018, 1115, 1118): a cell c of side l, its core (the links at depth at least l/3), its ring (boundary links). mu is the state, m_Omega the law of the core given the ring value Omega, mbar the core marginal. By the Markov property the ring carries all dependence of the core on the outside.

| Name | Exact statement | Kind | Consumer on file | Standing |
|---|---|---|---|---|
| (H-two)(l, eta) | E d_TV(m_Omega, m_Omega') <= eta, for Omega, Omega' independent with the ring law (row 1115 3.4) | two-sample mean | none proved: (CONV-two), "exponential clustering at rate c/l from (H-two)", is open (check 1120 5.2) | within a factor 2 it is the mixing coefficient of core and ring (Lemma TS) |
| Lemma TS (check 1120 3.15) | E_mu d(m_Omega, mbar) <= E d(m_Omega, m_Omega') <= 2 E_mu d(m_Omega, mbar), and E_mu d(m_Omega, mbar) is the total variation distance of the joint law of (core, ring) to the product of its marginals | identity and two inequalities | - | PROVED, checked by Opus |
| Lemma TS2 | abs Cov_mu(F, G) <= 2 norm(F) norm(G) E_mu d(m_Omega, mbar) for F of the core and G of the outside | consequence | - | PROVED |
| Lemma TS3 (check 1120 5.2) | for one bounded core F put alpha_F = E_mu abs(m_Omega(F) - mbar(F)). (a) sup over outside G with norm(G) <= 1 of abs Cov_mu(F, G) equals alpha_F. (b) alpha_F <= E abs(m_Omega(F) - m_Omega'(F)) <= 2 alpha_F | converse of TS2, one observable | - | PROVED by the checker; cross-checked by row 1123 |
| (H-two-N1)(l, eta) (check 1120 5.3) | for every bounded neutral function F of the core (non-local allowed): E abs(m_Omega(F) - m_Omega'(F)) <= eta norm(F) | two-sample mean, one observable at a time | none: "Whether (CONV) can be proved from (H-two-N1) ... is open; couplings use total variation" | the weakest pinned two-sample form that passes the U(1) and coexistence tests (ARGUED there) |
| (H-two-col)(l, eta) | for every cell and every configuration tau outside the box of side 3l: E[d(m_Omega, m_Omega') given tau] <= eta, rings drawn from mu( . given tau) | specification, supremum over the far boundary only | none written | open; not tested |
| (H-swap) = (4.4)/(4.5) of row 1118 | p_c = 1 - m_c/A_c is the swap defect of cell c for two independent rings; (4.5): E prod over a self-avoiding chain pi of p_c <= eps^abs(pi) with 5^d eps < 1/2 | two-sample, joint tail of a free-energy cross-difference | Theorem CONV-swap (4.6): exponential clustering at rate (log 2)/(2l), constant 32 (3^d)^2 abs(A); PROVED, checked parts A-E | hypothesis FALSE at beta in [2.3, 2.6] for every l: Proposition J, E p_c >= (1 - e^(-3 beta l)) Pbar/2 >= 0.010 against eps_0 = 1/1250 |
| Lemma JI (check 1121 8.6) | for a ring block z and N_z the cells with z in S_c: E_(rho x rho) sum over N_z of Delta_z(c) = 2 (I + L), I the mutual information of block z and the other ring blocks, L its reverse form | identity | - | PROVED; so no localized ownership makes the mean exchange cost small |
| Lemma BACK (row 1122 3.4) | uniform clustering at rate c/l with constant C gives alpha_F <= 32 C l'^3 exp(-c l'/(3l)) norm(F), so (H-two-N1)(l', eta) for l' >= C' l log l | necessity | - | ARGUED there; held in check 1123 |
| (DS-W) (row 691) | one changed boundary link of a cube changes few links, for all boundary values, sum normalised by the volume | specification, full supremum | Theorem W: PROVED implication (row 691, check 693) | REFUTED at sides 1 to 10 for beta >= 23/10 (row 1511, check 1514; registry W-CUBE-23) |
| (FL) (row 1510 4.2) | Wilson at beta in J = [2, 3], every torus with even sides >= 8, Q2 with strength kappa = beta: there are gamma_cl >= 0 on X x Y and C, m > 0 independent of the torus with (H2): abs Cov_(mu^V)(f, S_c)^2 <= E_(mu^V)[sum_l gamma_cl abs(grad_l f)^2] for mu'-almost every V, and E[gamma_cl] <= C exp(-m dist(c, l)) under the joint law | in-law covariance bound with decay, in the posterior of one block step | Proposition PC and Lemma REV (weighted Poincare passes through one Q2 step both ways); the route then still needs a gap source at the coarse end, joint moments over levels, and decay from a weighted Poincare inequality (row 1510 4.2 (i)-(iii)) | not proved, not tested; "a carry, not a selective statement" |
| (CM_k) (row 1468 4.3) | mixing of the constrained system exp(-Phi(W)) K(W, V), with a rate and a constant, for every rule in Tube(Phi*_k, rho_k; eta_k) and every coarse field in a regular set, plus a bound on the weight outside it | supremum over a tube and a regular set | Theorem K2 through (K2-STEP), with (EN_k), (BASE-K2), (END-K2) | no method at order-one coupling; every class in a chain already has purity >= 457/625 (row 1496) |
| Periodic seed, trajectory | s_K(u) <= 4/21 at infinitely many K (from P_K >= 457/625 by Fact PUR) | one number on one torus | (M-io-exists), rows 1461, 1462, 1465 | open |
| Periodic seed, fixed coupling, Lean | T.seed N = thermal sum at time N on the spatial cube of side 2N; hypothesis T.seed N < 1/5041 for one N >= 3. Sufficient: T.phi N = 16 log Z(N^4) - log Z((2N)^4) <= 19/100000 (`seed_of_phi`). The transfer kernel is exp(-beta (V(u) + V(v))/2) times the gauge average of the product over edges of exp(-beta (1 - halfTrace(g v g'^-1 u^-1))) (`Transfer.lean` L548-556) | one number, or two partition functions | `wilson_theoremS`: s(2^k N) <= (5041 s(N))^(2^k)/5041 and gap >= log(1/(5041 s))/N on every dyadic cube; kernel-checked, standard axioms only (RECEIPT-1f) | "The physical seed ... remains open" (receipt) |
| Rank-one form | if B/c is within delta of a rank-one projector in Hilbert-Schmidt norm then (1 - delta^2) Tr B^2 <= norm(B)^2 | closeness of the kernel to any rank-one kernel | Lemma M1 (rows 1356, 1359; `LemmaM1.lean`, Lean) | consumer proved; supplier is the seed |

Three facts that the reading fixed for me.
1. The only forms with a complete proved consumer are the periodic ones (seed, pressure, rank-one) and the two supremum forms. (H-swap) has a consumer and is false at the window. (H-two-N1), (H-two-col) and (FL) have no complete consumer.
2. Lemma M1 already lets the consumer accept closeness to ANY rank-one kernel. So in Lemma HS the reference law need not be the marginal: for every probability density nu = u^2 on the slice, BC(q, nu x nu) = <u, A u> <= w_0^(1/2). Lemma HS adds only the lower bound (necessity). I correct section 2: its consumer half is Lemma M1, ON FILE and in Lean.
3. The Schwarz-lemma route from a zero-free domain of two torus families to the seed is ON FILE (row 988, check 991, method 29 of `parts/gap.md`). I re-derived it this pass before finding it. It is not new.

## 9. The weakest form that a consumer accepts

(W-per): the two-slice law at half period on one periodic box is within Hellinger affinity 11/12 of some product law. On the trajectory the box is n^3 with period u = n/512 and the consumer is (M-io-exists). At a fixed coupling the box is the cube of side 2N with period N, the threshold is tighter (s < 1/5041, so affinity >= (5041/5042)^(1/2) to the best product law), and the consumer is the Lean chain. Equivalent on that box: T.phi N <= 19/100000 is sufficient.
Why not a pinned form: (H-two-N1) is weaker in kind but has no consumer, and by Lemma BACK every sufficient hypothesis implies it at a scale larger by a logarithm. So I attack (W-per).

## 10. Attacks on (W-per), each with the step that fails and the attack it suggests

**Attack 5: a product trial law in the Gibbs variational principle. PROVED bound; fails at the junctions.**
Lemma PT. For every n >= 3 and beta > 0: 0 <= T.phi n <= 96 n^2 (2n - 1) beta e_n(beta), with e_n the mean of halfTrace of a plaquette on the n^4 torus.
Proof. Write Z_L for the partition function with weight exp(beta A), A the sum of halfTrace over plaquettes (the constant of the action 1 - halfTrace cancels in phi, since 16 times the plaquettes of n^4 equals the plaquettes of (2n)^4). For every probability law nu on the (2n)^4 fields, log Z_2n >= beta E_nu A_2n - D(nu || Haar). Cut the (2n)^4 torus into 16 blocks of n^4 sites. A link belongs to the block of its lower end. The links of one block are in bijection with the links of the n^4 torus. Let nu be the product over the blocks of the n-torus Gibbs law mu_n. Then D(nu || Haar) = 16 (beta E_(mu_n) A_n - log Z_n). A plaquette at x in the plane (i, j) has all three sites x, x + e_i, x + e_j in one block unless x_i or x_j is n - 1 modulo n. In the first case its nu-law is its mu_n-law. In the second case one of its links lies in another block and is independent of the rest; the mean of a link matrix under mu_n is 0 (invariance under a gauge transformation at one end, and the Haar mean of g is 0); so the mean of halfTrace is 0. The number of plaquettes of the second kind is 16 times 6 times (n^4 - n^2 (n-1)^2) = 96 n^2 (2n - 1). So log Z_2n >= 16 log Z_n - 96 n^2 (2n - 1) beta e_n. The lower bound 0 follows from `log_seed_le_phi` (log(1 + T.seed n) <= T.phi n) and T.seed n >= 0. QED
Corollary (PROVED, trivial range). With e_n <= 1: T.phi 3 <= 4320 beta, so the Lean seed holds at N = 3 for 0 < beta <= 19/432000000. This is far inside the on-file range beta < 2/9 (row 1340 Theorem BS with Proposition SL, hand proofs) and adds nothing to it.
Failing step: independent blocks give junction plaquettes mean 0, and the true law gives them mean e_n. The loss is a surface term, 96 n^2 (2n - 1) beta e_n, against a target of 19/100000. This is the mechanism of Proposition J (independent frames at a junction) in pressure form. ON FILE as a mechanism; the pressure bound itself I did not find.
Suggests: a reference that shares the junction. In one direction that is a rank-one reference for the transfer operator (Attack 6).

**Attack 6: a rank-one reference from the slice Gibbs weight, one time step. PROVED; fails where S(2) is not small.**
Lemma VT. Let T = M K M be the Lean transfer operator on the spatial box R, M = exp(-beta V/2), K the gauge-averaged temporal kernel. Let mu_3 be the three-dimensional Wilson law on R, density proportional to exp(-beta V). Then
    1 + S_R(2) <= E[K^2] / (E K)^2,   so   S_R(2) <= Var(K) / (E K)^2,
with K = K(u, v) and (u, v) two independent samples of mu_3. And S_R(N) <= S_R(2)^(N/2) for N >= 2.
Proof. For a unit vector phi, <phi, T phi> <= lambda_0, so 1 + S(2) = Tr T^2 / lambda_0^2 <= Tr T^2 / <phi, T phi>^2 (this is Lemma M1 with an explicit rank-one kernel). Take phi = M 1 / norm(M 1), norm(M 1)^2 = Z_3. Then <phi, T phi> = Z_3 E K and Tr T^2 = Z_3^2 E[K^2], because K is real and symmetric. T is Hilbert-Schmidt (continuous kernel on a compact space). The last claim is the inequality sum r_i^N <= (sum r_i^2)^(N/2) (Remark TEMP (a) of row 1597). QED
Consumer. On the cube of side 2N: Var(K)/(E K)^2 < 5041^(-2/N) gives T.seed N < 1/5041. The thresholds are 0.0034 (N = 3), 0.0141 (N = 4), 0.058 (N = 6), 0.18 (N = 10).
What it is: a two-sample statement across ONE time step, with no cylinder, in the law of the three-dimensional slice model. The same proof with phi replaced by any unit vector and T by T^w is Lemma M1.
Failing step: the bound needs S_R(2) < 1 on a cube of side at least 6. GUIDE (leading strong-coupling order, not a proof): S(2) is about N_s t^8 with N_s = 24 N^3 spatial plaquettes and t = I_2(beta)/I_1(beta), so the form can hold only for beta below about 1. At beta in [2, 3], t^8 is above 10^-3 and S(2) is large. I did not prove a lower bound on S(2) there.
Suggests: (i) below beta about 1, bound Var(K) (Attack 7); (ii) at the window, w time steps with a better reference vector (Attack 8).

**Attack 7: bound Var(K) by a Poincare inequality of the slice. Conditional (PROVED given the input); the input is the three-dimensional problem.**
If mu_3 x mu_3 has a Poincare inequality with constant C_P in the link gradients, then Var(K) <= C_P E[K^2 abs(grad log K)^2] <= eps E[K^2] with eps = C_P times the number of links of the two slices times G^2, G the supremum over (u, v) and the link of abs(grad_link log K). Then E[K^2] <= (E K)^2/(1 - eps) and S_R(2) <= eps/(1 - eps). (Two lines; PROVED given C_P and G.)
Reading: the four-dimensional seed at time 2 follows from the Poincare constant of the three-dimensional Wilson law and a one-step response of the temporal links. It is an induction on the dimension.
Failing steps: (a) C_P for mu_3 is known on file only in a Dobrushin or Bakry-Emery range of the three-dimensional model (ARGUED: twelve neighbours, so beta below about 1/3; I did not find the constant on file). At beta in [2, 3] it is the mass-gap problem of the three-dimensional model. (b) G needs a supremum over the pair of slices; its in-law form puts the weight K^2 back, which is the time-2 periodic law. (c) Attack 6's own failing step. GUIDE: with C_P near 10 and G near beta^4/16 this reaches beta near 0.25, a few percent above 2/9. Not worth a row.
Suggests: nothing at the window.

**Attack 8: w time steps and a better reference vector. Fails at the overlap.**
Lemma M1 with T^w: 1 + S(2w) <= Tr T^(2w) / <phi, T^w phi>^2, and the right side tends to abs(<phi, psi_0>)^(-4) as w grows. So the certificate needs a unit vector phi with abs(<phi, psi_0>)^2 >= (5041/5042)^(1/2) on a cube of at least 24 N^3 spatial plaquettes, N about 14 or more at beta = 23/10 (GUIDE from the lattice mass of about 1.4 and the count 3 (2N)^3 e^(-1.4 N) < 1/5041).
Failing step: for every explicit phi on file the overlap deficit is extensive in the slice (ON FILE as a verdict: "variational trial" in the list of row 1496; fifty files name a trial vector; I read row 1496's line and not each file). A vector with overlap of order one on such a box is the vacuum to relative precision 1/N_s. I have no construction.
Suggests: the vacuum built by a multiscale map, which is (K-II).

**What the four attacks have in common (ARGUED).** Each is a choice of reference for the two-slice law: independent blocks (5), a product of slice laws at one step (6, 7), a rank-one vector at w steps (8). The consumer accepts any of them (Lemma M1). The supplier must give a reference within Hellinger affinity (5041/5042)^(1/2) on a box whose side is many correlation lengths. Below beta about 1 the slice weight itself is such a reference on small boxes. At the window I know none that is explicit.

## 11. Verdict of the second pass

I did not reach (a), (c) or (d).
- (a): no proof of (W-per) at any coupling above the hand range. Lemma PT proves the Lean pressure seed only for beta <= 19/432000000.
- (c): no obstruction theorem. I found no on-file form that fails on the trajectory beyond those already refuted, and the equivalences I can prove are on file (Lemma M1, Lemma TS3, Lemma BACK, rows 1169-1173).
- (d): no component of a method that reaches the window. Lemma VT is a correct one-step consumer. Its reach is strong coupling only, and its supplier above 2/9 is not built.
The named step that failed in each attack: a reference law for the pair of slices at half period, within Hellinger affinity 11/12 (trajectory) or (5041/5042)^(1/2) (Lean, fixed coupling) of the true pair law, on a box of side many correlation lengths, at a coupling of order one. Ways written out this pass: independent blocks (surface loss, Lemma PT); the slice Gibbs weight at one step (S(2) not small); a Poincare bound for it (needs the three-dimensional gap); a trial vector at w steps (extensive overlap deficit). Ways on file: Dobrushin comparison (2/9), polymer end classes (0.00872), transport in the coupling ((R11)), zero-free domains in Schwarz form (rows 988, 991), circles and seams (rows 1565-1583).
The lead asked me not to stop short of a proof, an obstruction theorem or a built component. I stop here without one. I say so plainly: I have no further attack that is not on file as stopped, and writing more restatements would not be closure.

Labels of the second pass.
| Statement | Label |
|---|---|
| Section 8 table | ON FILE, read line by line at the places named in Step 7; (CM_k) and the Lean lines read in the source |
| Lemma PT and its corollary | PROVED here by hand, unchecked; mechanism ON FILE (Proposition J, check 1121) |
| Lemma VT | PROVED here by hand, unchecked; it is Lemma M1 (Lean) with phi = M 1; the temporal step is Remark TEMP (a) |
| Thresholds 5041^(-2/N) | arithmetic, floating point, GUIDE precision only |
| "S(2) is about N_s t^8", "beta below about 1", "N about 14" | GUIDE (leading order, recalled lattice values); not a proof step |
| Attack 7 implication | PROVED given C_P and G; both inputs open above the hand range |
| Attack 8 failing step | ON FILE as a verdict (row 1496); ARGUED here |
| "The four attacks are choices of a reference" | ARGUED |

RESULT: Row 1600 (Claude Fable 5.2, laptop subagent; author only, unchecked; no numeric run, no Lean; two passes).
Outcome: NONE of (a), (b), (c), (d). (W-mix) is not proved and not refuted; no component reaching the window is built.
Read line by line and recorded in section 8: Lemmas TS, TS2, TS3, JI, BACK, the forms (H-two), (H-two-N1), (H-two-col),
(H-swap), (DS-W), (FL), (CM_k), the Lean seed and pressure seed, Lemma M1. Weakest form with a complete consumer: the
periodic one, closeness of the two-slice law at half period to some product law (Lemma M1 in Lean; Lemma HS adds necessity).
Proved by hand this pass: Lemma PT, 0 <= T.phi n <= 96 n^2 (2n-1) beta e_n (so the Lean seed holds at N = 3 for
beta <= 19/432000000, inside the on-file range); Lemma VT, S(2) <= Var(K)/(E K)^2 for two independent samples of the
three-dimensional slice law, with S(N) <= S(2)^(N/2), a one-step consumer that can hold only at strong coupling.
Four attacks on the periodic form each fail at one step: no explicit reference law for the slice pair within the
required affinity on a box of many correlation lengths at order-one coupling. Corrections to the first pass: the
consumer half of Lemma HS is Lemma M1; the Schwarz zero-free route is on file (rows 988, 991).
Open: (W-mix), (PUR-io), the gap. No next row proposed.
