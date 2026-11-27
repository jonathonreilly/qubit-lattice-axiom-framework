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
