# Direction checkpoint 8 (FINISH.md row 1643)

Author: Claude Fable 5.2, high effort, one session, 2026-11-28. Lane folder
`.claude/science/physics-loops/ym4d-hard-route-20261030`. This file is written
as the work goes; later sections may correct earlier ones, and say so.

Labels: PROVED (complete proof in this file), ARGUED, GUESSED, ON FILE (row).

## 0. Reading log

(appended as files are read)

- Read in full: the brief (row 1643 text); the RESULT texts of FINISH.md rows
  1597-1651 (rows 1608, 1609, 1614, 1615 were stopped or not run; row 1599 is
  held and has no RESULT).
- Read in full: `library/gap-mech-direction2-fable.md` (row 1386); GOAL.md;
  registry rows VIR-DOWN, LEV-FAIL, WMIX-SLICE (`library/open-registry.md`
  L1028-1030).
- Read as RESULT openings only (first 400-480 characters of each RESULT):
  FINISH.md rows 1378-1596. These are pointers. Section 1.1 B to G rests on
  them and says so. Where sections 1.5, 1.6, 2 and 3 use a row, I opened the
  file or the full RESULT text, and the entries below say which.
- Read in full: `library/gap-direction7-fable.md` (row 1610, my own earlier
  row; re-read as a source, not trusted as evidence).
- Read in the sections named: `library/gap-direction7-fable-check-astra62.md`
  "The two seeds", "Regularity (R)", "Proposition EQ-down", RESULT (check
  1613); `library/gap-k2-tool-design-fable.md` 2, 3.1, 5,
  6 (row 1468); `library/gap-mech-direction4-fable.md` Step 13, Decisions 1 to
  3 (row 1553); `library/gap-vir-down-twoside-check-opus.md` section 1 (check
  1630); `library/gap-magdef-check-opus.md` 2.5, 3, 4, 5 (check 1648);
  `library/gap-k2-step-astra62-check-opus.md` 3, 4 (check 1651);
  `library/lean-gap-chain-design-fable.md` 4.3, 4.4, 5.2, 5.3, 6, 7, 8 (row
  1457); `library/gap-solve9-astra62.md` L46 to L63 and L213 to L227 (row
  1161);
  `library/gap-transfer-twisted.md` 1, 2, 3.5 (row 1004);
  `library/t0-tree.md` section 1; `library/port-map.md` 4.2 to 4.4;
  `library/assembly-status.md` 1.1.
- Read as primary Lean sources: `lean/gapchain/GapChain/Assembly.lean` in
  full; the theorem names of all eight modules; `TheoremS.lean` L534 (the
  definition of `seed`); `lean/gapchain/RECEIPT-1f.md`.
- Read as full RESULT texts: rows 1161, 1162, 1179, 1356, 1359, 1367, 1370,
  1387, 1391, 1442, 1449, 1453, 1454, 1455, 1458, 1459, 1461, 1470, 1497,
  1527, 1556, 1585, 1586, 1596, and check 1443's verdict.
- Not read: `library/gap-direction8-astra62.md` and its check beyond their
  RESULT texts (the brief allows reading them; I kept my method apart); the
  files of rows 1617 to 1647 other than the three checks named above; the
  account; the release's Lean sources; `parts/witness.md`.
- Grep is used below only to say whether a name is on file. A grep count is
  not a reading, and I say which files I opened.

## 1. What the five days since row 1378 established

Scope of this section. Rows 1378 to 1651 are about 270 rows. I read the RESULT
texts of rows 1597 to 1651 in full and the primary files listed in section 0.
For rows 1378 to 1596 I read the opening of each RESULT text and the full
texts listed in section 0. So the anchors of 1.1 B to G are RESULT texts. A
reader who relies on one of them must open the check file.

"Checked" below means: a hand proof by one provider, read line by line once
by a model of another provider. It is not an audit and it grants no status.
"Kernel-checked" means the Lean kernel checked it.

### 1.1 Proved and checked

A. The frame: what the seed is and what it gives.

| # | Statement | Anchor | Note |
|---|---|---|---|
| A1 | Fact PUR: P_K >= 457/625 gives s_K(u) <= 4/21. | row 1468 3.1 (proof read here; three lines); rows 1373, 1461; check 1465 | PROVED; elementary |
| A2 | (PUR-io) gives a calibrated continuum limit of the release with a unique vacuum and a gap at least (2/l) log(2^18/5041) in the tr F^2 sector. | (L1) of row 1461, checks 1462 (steps 1, 2) and 1465 (steps 3 to 7, same model family as 1462); trajectory bounds of row 1451, check 1453; even-sector consumer of row 1179; Lemma M1 of row 1356, check 1359; finite aspect of row 1161, check 1162 | hand proofs; each link read once by another provider; several "HOLDS AFTER CORRECTION" |
| A3 | A lower threshold suffices at a changed aspect (34 to 78). | check 1527 (ii); check 1370 | existential in the physical side |
| A4 | `wilson_theoremS`: for every beta > 0, a periodic cube seed below 1/5041 gives thermal decay and a gap on every dyadic cube. | `lean/gapchain/GapChain/Assembly.lean`; row 1525; checks 1503, 1505, 1507, 1518, 1524 | kernel-checked; see 1.5 for its scope |
| A5 | The release: existence along a subsequence with the Osterwalder-Schrader properties; no uniqueness, no gap. Replay built. | row 1449 (reading), check 1450, row 1455 (replay, exit 0) | theirs: Sussman and Alpoge with Claude and Codex; Balaban |

B. Negatives on mechanism candidates, rows 1378 to 1443.

| # | Statement | Anchor |
|---|---|---|
| B1 | The lab-frame ports of the two-dimensional engines are closed (Theorem C1, Lemma H). | row 1380, check 1381 |
| B2 | Proposition LIFT and Lemma THIN hold; the literal (BUB) holds for U(1) (Theorem U1), so it is not selective. | row 1383, check 1385 |
| B3 | Proposition NEG (b), Lemma GRP, Remark FI, Remark STAB (periodic form), Remark PAIR as a test: hold after correction. The inventory of NEG failed at one line: row 1141 (2) is a positive band estimate on growing boxes. Its follow-up (SHELL) stayed open. | row 1386, check 1387; rows 1388, 1389 |
| B4 | The grid class of carries is not closed (the closure claim failed). Time coarsening gives no rate and no entry. The submersion candidate C7 stops at its gate. | rows 1390, 1396, 1409; checks 1393, 1401, 1411 |
| B5 | A bare order-one block is finite, but two tensor implementations of a step are ruled out by cost. The one-link ring is rejected as a four-dimensional decrement; its finite arithmetic is kernel-checked. | rows 1418, 1425, 1432, 1435; checks 1420, 1429, 1433, 1437 |
| B6 | Three candidate classes are closed (heat rotation into a coarse link; joint commutator kick; thinned Haar commutators). The heat-factor class is realised by massless Villain U(1) (Proposition VIL). | rows 1434, 1438, 1439, 1442; checks 1436, 1440, 1441, 1443 |

C. The order-one tool, rows 1460 to 1500.

| # | Statement | Anchor |
|---|---|---|
| C1 | Thin transporters lose the coarse field when their length is large against the coupling (Theorem LOSS). | row 1460, check 1463 |
| C2 | The block map Q2 carries each of the sixteen twisted masses exactly (Lemma TW); a chain of steps into an end class gives (PUR-io) (Theorem K2, END-K2). No step is proved. | rows 1468, 1471; checks 1469, 1473 |
| C3 | Pointwise small-field steps of side two have floors between 12,500 and 2,560,000 in the inverse coupling, depending on the test. One class-wide route is refuted at beta = 23/10. The joined full-face interface criterion is refuted. | rows 1472, 1475, 1499; checks 1478, 1484, 1500 |
| C4 | The release forces inverse couplings above 2^2800 at every side. | row 1464, check 1467. Row 1470 raises it to 2^3457; that row is unchecked. |

D. Seed attacks, rows 1510 to 1527.

| # | Statement | Anchor |
|---|---|---|
| D1 | The boundary-uniform criterion (W) fails at side 4 and beta = 23/10, and at sides 1 to 10 for beta >= 23/10. | row 1511, check 1514 |
| D2 | A weighted Poincare inequality passes exactly through one Q2 step (Proposition PC). It has no source. | row 1510, check 1513 |
| D3 | Theorem EQ (a) to (c) for the two-period statement holds; the verdict "equivalent" failed, so TWO-PER stays a separate open statement. | row 1520, check 1521 |
| D4 | Seven approaches of row 1526 restate lines on file. | check 1527 |

E. The full-allocation attack, rows 1528 to 1556.

| # | Statement | Anchor |
|---|---|---|
| E1 | Every selective statement proved there has a range R <= beta^k (ultraviolet in the limit) or reads the algebra or a mode count. | rows 1530, 1532, 1536, 1538, 1549; checks 1535, 1543, 1540, 1546, 1551 |
| E2 | Classes of coarse rules are excluded (entire actions of fixed temporal range; polynomials in the electric Gram determinant; plaquette-trace interactions plus a log-cosh Gram profile); no step is built. | rows 1544, 1549, 1552, 1547; checks 1548, 1551, 1555, 1554 |
| E3 | Lemma ALG: a property with one truth value on a class that has a seedless member is not an input. | row 1553 1.4 (proof read here; three lines). Check 1556 holds items (i) to (iv), (vii), (viii) of that row after correction and withdrew its stop. |

F. Interpolation and flux, rows 1565 to 1595.

| # | Statement | Anchor |
|---|---|---|
| F1 | Circles of link maps exist that reach a centre twist, and paired-link circles that reach the neutral swap. | check 1556 (v); rows 1573, 1574; checks 1579, 1580 |
| F2 | The one-end swap moment of the paired-link circle is of order beta_K n^3. | row 1581, check 1583 |
| F3 | The lower-tail lemma of check 1585 was attacked three ways and stayed open. It covers the electric half only. | rows 1587, 1588, 1591; checks 1589, 1590, 1595 |
| F4 | The published two-purity bootstrap is equivalent to the seed here. | row 1592, check 1594 |

G. The two-cutoff comparison (A1), rows 1391 to 1417 and 1557 to 1596.

| # | Statement | Anchor |
|---|---|---|
| G1 | (A1) is not proved in any rate form. The account assumes the two-cutoff comparison (its input E3). The release takes its limit by compactness. | row 1391, check 1392; row 1454 |
| G2 | The dedicated (A1) slot is stopped. The count of 27 open entries describes one chosen route, not necessary leaves. | row 1586, check 1596 |

H. Rows 1600 to 1651.

| # | Statement | Anchor |
|---|---|---|
| H1 | Each bounded whole-slice two-sample criterion at the target aspect is equivalent to (PUR-io). Fixed-size cells, raw-link swaps and short periods fail on the trajectory. One-observable mixing gives no purity bound. | checks 1605, 1607; registry WMIX-SLICE |
| H2 | The chamber estimates of row 1601 hold in every bounded finite-range compact-spin model. | check 1606 |
| H3 | Theorem TR-down: (HOT) and the thermal (VIR-down) on the characteristic give the thermal seed s_K(u) <= 4/21. Lemma D1. Regularity (R) on each finite Wilson box. After correction, (T-down) at K is exactly the thermal seed at K plus "G(u; beta) does not fall on a right neighbourhood of beta_K". For Wilson it gives (PUR-io) at an enlarged side; the converse is open. | row 1610; check 1613 (sections "The two seeds", "Regularity (R)", "Proposition EQ-down", read here) |
| H4 | The level form (LEV-down) fails on every finite Wilson box. | rows 1617, 1618, 1619; checks 1621, 1622; registry LEV-FAIL. One route, three authors. |
| H5 | With r fixed first and l = L_h b^r, every constant rate kappa_0 > 0 suffices in Theorem TR-down, as an implication. A rate c/beta does not. | rows 1628, 1629; check 1630 1.1 to 1.4; check 1622 |
| H6 | The observed-loop test (15) implies (VIR-down) and is strictly stronger in abstract families; the two-sided tests (19), (2.12), (2.13) are sharper than (15). No lower bound on the visible slope is proved. | checks 1625, 1627, 1630, 1634, 1635, 1639, 1640 |
| H7 | A flowed-holonomy comparison would give (HOT). The comparison is open. | row 1642, check 1644 |
| H8 | In Kogut-Susskind form the magnetic-deficit condition is (VIR-down) exactly. In the one-vertex model at weak coupling the magnetic slope of every cold excited level tends to -m/(3B), in four and in five dimensions. | row 1647, check 1648 sections 2.2, 3 |
| H9 | The map of row 1650 is the strong-coupling cluster expansion regrouped by coarse label. It carries no class between scales. Its U(1) and five-dimensional tests do not separate. | check 1651 sections 3, 4 |

### 1.2 Proved, with one reader or none

- Lemma HS (the seed forces Hellinger affinity above 0.769 of the neutral
  two-slice law to a product), Lemmas PT and VT: row 1600, unchecked.
- The running budget (RB): check 1630 1.3 (d), proved by its one reader.
- Lemma F of check 1612; the corollary of check 1627; Remarks M, DP, T of
  check 1606: each proved by the one checker.
- The floor 2^3457 of row 1470: unchecked.
- Row 1619's Proposition TRUNC and its two identities: no check row names
  them (checks 1621 and 1622 cover LEV-FAIL through rows 1617 and 1618).

### 1.3 Argued, or a judgement over the record

- "Every neutral-reading route ends at (W-mix)" (row 1597); "the statement
  side is closed" (row 1610 1.5).
- "The (T-down) line reduces to (K-II)" (check 1648 section 4; row 1649).
  Section 1.6 examines it.
- "The delay closure hides nothing" (row 1633 5.2): argued, unchecked.
- The one-loop anisotropic running behind "the deficit is carried by the
  running" (check 1648 2.5): the algebra is checked; the premise is recalled.
- Every pause or stop: rows 1386, 1442, 1553, 1584, 1597. Checks 1387, 1556
  and 1585 each withdrew one; check 1598 kept one.
- The premise that five-dimensional SU(2) has no gap at weak coupling: belief
  (row 1553 (g2); row 1531 found no theorem).
- No exhaustion of mechanisms follows from any of this (check 1443).

### 1.4 Not established

- No open input moved: (PUR-io), (R10) to (R12), (A1), (A2), (K-I), (K-II).
- No sign and no size is proved for (VIR-down) at any cold point of the band
  (check 1622; registry VIR-DOWN).
- (HOT) is not proved at any box (check 1644).
- No form of (W-mix) at a physical scale is shown to fail (check 1607).
- No statement on the calibrated trajectory at a fixed physical size above
  the account's range is proved, except lattice-local facts, identities and
  negatives. This is Proposition NEG of row 1386 with the corrections of check
  1387, and rows 1597 to 1651 add no exception (ARGUED from H1 to H9).

### 1.5 A scope note on the Lean chain (established by reading the sources)

The brief says that the Lean files in `lean/gapchain` prove the seed-to-gap
step with the seed as the only open hypothesis. What the kernel checked is
narrower (ON FILE: `Assembly.lean`, `TheoremS.lean` L534, RECEIPT-1f):

- `seed n` is the full thermal sum at time n on the periodic cube of side 2n,
  at one fixed coupling. `wilson_theoremS` gives a gap on dyadic cubes at that
  coupling.
- The eight modules (about 3,200 lines, 173 theorems) contain no twist, no
  centre translation C_z and no projector P_0. A search of the sources for
  "twist" and "centre" finds only the element -1 of SU(2).
- So (PUR-io) does not plug into the kernel-checked theorem. Three hand links
  lie between them: the neutral seed to the kappa-seed (rows 1161, 1179,
  1356; nodes W3, W4, W6, W7, W8 of row 1457 5.2), the lattice bound to the
  cluster bound of the release's states (W9 to W11), and that bound to the
  gap of the limit (U0 to U7 except U4). Row 1457 sizes the whole chain at
  16,000 to 28,000 lines (a guess there).
- Built, by the theorem names in the sources: W1 (`lemmaM1`), W5 (the
  abstract Theorem S), U4 (`sequenceLemma`), and the untwisted parts of W2
  to W4 (`Wilson`, `Transfer`, `Trace`, `Periodic`). Not built: the twisted
  parts of W3 and W4, W6 to W11, and U0 to U7 except U4.

This does not weaken A2. It says who checked what: A2 is checked by hand, A4
by the kernel, and A4 is not A2.

### 1.6 Is the judgement of row 1649 right?

Row 1649 records, on the advice of check 1648: Theorem TR-down is proved; (HOT)
is supplied conditionally and its aspect is absorbed by the depth r; the only
open input is the thermal (VIR-down) on the band; no route on file reaches it
without an order-one renormalization step; so the (T-down) line reduces to
(K-II). The row calls this a judgement, not a theorem.

First an exact statement, so that the judgement can be read against it.

**Setting.** As in row 1610 3.1: one fixed lattice (Z/n)^3, the neutral
transfer operator R_beta with (S1) to (S3), ratios r_i(beta), levels
m_i = - log r_i, and G(t; beta) = sum over i >= 1 of exp(- t m_i(beta)) for
real t >= 1. Assume the regularity (R): G is continuously differentiable in
(t, beta). Check 1613 reports that (R) holds on each finite Wilson box at
positive coupling; I did not re-derive it. Assume G(1; beta) > 0, so some
excited level is finite.

For fixed beta, G is finite, continuous and strictly decreasing in t, and it
tends to 0 as t grows (each term does, and the terms are dominated by r_i,
which is summable by (S1); r_i < 1 because the top eigenvalue is simple). For
0 < s < G(1; beta) let tau_s(beta) be the unique t > 1 with G(t; beta) = s.
I call it the **cooling time at level s**.

**Proposition COOL (PROVED here; elementary; ON FILE in substance as
Proposition EQ-down (b) of row 1610 and as (RB) of check 1630).** Let I be an
interval of couplings and s > 0 with G(1; beta) > s on I.

(a) tau_s is continuously differentiable on I, and
    tau_s' = - (d/dbeta G) / (d/dt G) at the point (tau_s(beta), beta).
(b) At the point (tau_s(beta), beta), (VIR-down) with the rate kappa holds if
    and only if (log tau_s)'(beta) >= kappa.
(c) For beta_1 < beta_2 in I and u > 1:
    G(u; beta_1) <= s  if and only if  tau_s(beta_1) <= u  if and only if
    the integral of (log tau_s)' over [beta_1, beta_2] is at least
    log(tau_s(beta_2) / u).
(d) Let Omega be a set of points (t, beta) with beta in I, t > 1 and
    0 < G(t; beta) <= c. Then (VIR-down) holds with the constant rate kappa_0
    at every point of Omega if and only if, for every level s in (0, c], the
    function exp(- kappa_0 beta) tau_s(beta) has a non-negative derivative at
    every beta with (tau_s(beta), beta) in Omega.

Proof. (a) d/dt G = - sum of m_i exp(- t m_i) < 0, so the implicit function
theorem applies to G(t; beta) = s; differentiate G(tau_s(beta); beta) = s.
(b) (VIR-down) at a point is d/dbeta G >= - kappa t d/dt G. Divide by
- t d/dt G > 0 and use (a) with t = tau_s(beta). (c) The first equivalence is
strict monotonicity in t. The second is
log tau_s(beta_1) = log tau_s(beta_2) - integral of (log tau_s)'. (d) Every
point of Omega lies on exactly one level curve, the one of its own value of G.
Apply (b) at that point. QED

Three readings follow. The first is PROVED; the other two are ARGUED.

1. **The thermal seed is an identity about one function (PROVED, (c)).**
   "The seed" in the (T-down) line is the thermal bound s_K(u) <= 4/21 that
   Fact PUR derives from (PUR-io) and that the consumer reads (check 1613,
   "The two seeds"). Take s = 4/21, beta_1 = beta_K, u = n/512. The thermal
   seed at K says that log tau_s falls by at least log(tau_s(beta_h)/u) from
   beta_h to beta_K. (HOT) says tau_s(beta_h) <= t_h. So (HOT) with "the
   integral of (log tau_s)' is at least log(t_h/u)" gives the thermal seed,
   and the thermal seed gives both for every beta_h, with t_h = tau_s(beta_h).
   The integrated hypothesis is the thermal seed. By (b), the pointwise
   hypothesis with kappa >= 0 adds sign conditions: at each point of the
   characteristic, the cooling time of the level through that point does not
   fall as beta grows. This is Proposition EQ-down, as corrected by check
   1613, in one variable. Nothing in it is new.
2. **What the rate is (ARGUED; it uses the standard scaling picture as a
   guide, not as a step).** At a calibrated root beta_(K+i), the lattice n_K
   is the calibrated box of side l b^(-i) at cutoff K + i (check 1453, the
   shifted lattice; check 1630 1.3 (c)). If the levels scale as
   m_i = a(beta) E_i(n a(beta)), then
   (log tau_s)' = (- d log a / d beta) (1 - d log t_s / d log L),
   with t_s(L) the cooling time of the continuum box of side L. The first
   factor tends to 3 pi^2/11. The second is a property of the finite-volume
   theory alone. It is zero in a scale-invariant theory. It is small in a
   weak box, where the rate is about 1/(3 beta_box) (on file: check 1630 1.3
   (e)). It tends to 1 in a gapped box, where t_s grows like log L.
3. **What "any constant rate suffices" means (ARGUED from H5).** The band
   input of (T-down) is a uniform positivity: the second factor of reading 2
   stays above one positive constant on every box side between L_h and l,
   uniformly in the cutoff. A rate c/beta does not count, because beta_K grows
   and the window has a fixed width (check 1622). The uniformity in K is the
   running. In the compact Gaussian U(1) model the lowest cold levels are
   flux levels with the rate exactly 1/beta (check 1622), and photon levels
   do not depend on beta (row 1610 2.5).

**Verdict on row 1649 (a judgement of mine over the record; ARGUED).**

The judgement is right as a stop for the (T-down) line. Its wording is too
short in four places.

(i) It is right that no row gave a rate. Ten authored rows and their checks
    (rows 1617 to 1647) produced the consumer, sound tests, restatements and
    negatives. None bounds (log tau_s)' from below at a cold band point.
(ii) It is not a new reduction. By reading 1 the open input of (T-down) is the
    thermal seed plus sign conditions. Row 1610 2.4 said so before the line
    was run: "(T-down) is one more member of that family. I do not claim a
    reduction." The family is row 998's "the target in steps". Row 1386 said
    the same of every carry on file. What the line added is reading 3: the
    missing statement is a uniform positivity, not a number.
(iii) (HOT) is not supplied. Row 1642 proves that a flowed-holonomy comparison
    would give (HOT); the comparison is open, and check 1644 says its first
    estimate is not within one row. A hot box at a coupling of human size also
    lies below the release's floor (C4), where no step theorem is on file (row
    1468 5.1, component T1; check 1497 parked it).
(iv) The window is not the band. By check 1630 1.3 (c) it holds a weak part,
    the band and an infrared stretch up to l, and (VIR-down) is asked on all
    three. In the weak part the true rate is of order 1/beta_box, so the
    hypothesis needs a weak-coupling carry between the release's floor and the
    band. In the infrared stretch the box is at strong effective coupling. So
    one order-one step would not close the line. It would have to be iterated
    over the band and joined to two more statements.
(v) "Reduces to (K-II)" names one of the two input kinds of row 1386. The
    record does not show that a rate needs a renormalization step: an exact
    inequality with a sign and a size (K-I) would also do. No candidate of
    either kind is on file. And if a chain of order-one steps existed, Theorem
    K2 of row 1468 would give (PUR-io) directly, with no use of (T-down). So
    the accurate record is: (T-down) is not a route around the order-one
    input, and it has no supplier of its own.

I propose this wording for the registry row VIR-DOWN (the lead decides):
"The (T-down) line is stopped. Its open inputs are (HOT), a weak-coupling
carry below the release's floor, a uniform positive rate on the band, and the
same on the infrared stretch. None has a method. The line is the thermal seed
plus sign conditions (Proposition EQ-down as corrected by check 1613;
Proposition COOL of row 1643), not a reduction."

## 2. The decision

### 2.1 What I tried before deciding

Before each search I wrote a candidate down. Then I searched the folder for
it. The table gives each candidate and where it stands. "ON FILE" names what I
opened; "grep" means I only looked for the name.

| # | Candidate, as I wrote it | Where it is | Standing |
|---|---|---|---|
| 1 | A step-scaling inequality for the cooling aspect alpha_s = tau_s/n: one factor b in the physical side lowers alpha_s by b^(-eps). At fixed coupling in the size, or on one lattice in the coupling. | ON FILE in kind: (STEP) of row 1386 4.1; (IR-LOSS), (MON-L) of row 1553 2.2 and 3.2; Proposition COOL (c) above | the seed in steps; "no mechanism" (row 1553 2.2, citing row 1108) |
| 2 | A lower bound for the trace-anomaly matrix element of a cold level by a multiple of its energy | ON FILE: Lemma D1 of row 1610; rows 1645 to 1648 (check 1648 section 3) | (VIR-down) restated; stopped |
| 3 | Rate ordering: on the window the rate (log tau_s)' is at least its value at the hot end, where weak-coupling theory could give it. Stronger form: log tau_s is concave in beta. | Not on file by name (grep of the vir-down, magdef and direction 7 and 8 files for "concav" and "cooling time" finds no such statement) | By COOL (b) it is (VIR-down) at the hot rate: equivalent, no gain. The concave form is GUESSED false: neutral states made of two opposite flux loops have energy growing with the side, so the rate should rise above the scaling value and fall back. Not proposed. |
| 4 | The flux flow on a torus. With x the ratio of the twisted to the untwisted partition function: doubling a side in the twist plane gives x -> 2x/(1 + x^2), doubling a side along the sheet gives x -> x^2, each times a ratio of sector purities. | The identities follow in three lines from (T5) to (T7) of Theorem TW-T (`gap-transfer-twisted.md`). ON FILE in kind: Remark PAIR of row 1386 4.2 (the Migdal-Kadanoff recursion as an exact carry on a hierarchical lattice); row 1610 2.1 item 3 ("flux half only") | ARGUED: without the purity ratios this is the Ising recursion, with an unstable fixed point; all of the dynamics sits in the purity ratios, and the neutral seed is a statement about one of them. The seed as an identity. Not proposed. |
| 5 | Convexity of the logarithm of the partition function in the couplings (in Hamiltonian form, joint convexity of log Tr exp(- pK - qV) in (p, q)) as an exact carry with a sign | grep: "natural parameter" has no hit; "jointly convex" has five hits in other contexts, not opened | ARGUED: convexity bounds a mid-point partition function from above. A purity needs a lower bound. Group-blind. I found no use. |
| 6 | Twisted cells as seeds: (C_z T^v)^2 = T^(2v), so a doubled twisted torus is untwisted | ON FILE: Lemma TW of row 1468; the sixteen masses; test (t2) of row 1386 4.5 | the twisted gap is kinematic; the continuation is the band |
| 7 | A certified periodic seed at one fixed coupling above the hand range, fed to `wilson_theoremS` | ON FILE: RECEIPT-1f, "Next row"; row 1418 (cost); row 1386 4.4 (K-III) | not on the path of the continuum gap; cost out of reach above the expansion radius |
| 8 | A soft route: a sequence of band points with rate tending to zero has a scale-invariant limit; exclude it | no anchor | GUESSED: no route. A zero of one derivative at one side is not excluded by any axiom. |
| 9 | Prove the gap first in three dimensions as an engine prototype | ON FILE in part: `gap-mech-direction3-fable.md` L144 (the area law in three dimensions from two-dimensional O(4) decay) | not a route to the Jaffe-Witten gap |

Result of this pass: no new attack. Candidates 3, 4 and 5 are not on file
under these names, and each is the seed again or has no use. I count this as
one more blind pass with the same outcome as rows 1386, 1442, 1496, 1529,
1542, 1553, 1597 and 1610. By check 1443 no exhaustion follows from it.

### 2.2 The four options of the brief

**(a) A different design for an order-one step. I have none, and I say so.**
Every design on file is of one of four kinds:
1. an effective-action class under the block map Q2 (rows 1468 to 1500, 1542
   to 1555): no closed class at order-one coupling; pointwise floors between
   12,500 and 2,560,000; the release's own floor above 2^2800 (C2 to C4);
2. a tensor or enclosure computation (rows 1418 to 1437): ruled out by cost
   (B5; row 1468 5.2 and 5.3);
3. a regrouped strong-coupling expansion (row 1650): carries nothing between
   scales (H9);
4. a carry of spectral data in the bare coupling (rows 708, 1515 to 1523,
   1610 to 1648): the thermal seed plus sign conditions (1.6).
A fifth kind would be an exact inequality with a sign for non-abelian
plaquette weights (kind K-I). The reopen triggers (T-copy), (T-ineq), (T-dual)
of row 1553 3.3 name it. I found no instance. A design row with no method
would be a sixth blind pass. I do not propose one.

**(b) A disproof direction. Not ranked.** The seed is expected to hold, so a
counterexample direction does not exist. Obstruction theorems for classes of
methods are on file: Proposition NEG, Lemma ALG, Remark STAB, the tests (g1)
to (g6), Proposition VIL, WMIX-SLICE, LEV-FAIL. Three stops built on them were
withdrawn by a check that produced one more object (checks 1387, 1556, 1585).
One more obstruction theorem would not change which rows run. One true hole
remains in the obstruction record: the premise that five-dimensional SU(2) has
no gap at weak coupling is a belief, so every five-dimensional test is
conditional. Proving it would be new mathematics and would move no input of
the gap.

**(c) A change of target that still gives the Jaffe-Witten gap. None found.**
A theory with the Yang-Mills continuum limit has every scale, so it has a
regime of order-one effective coupling (row 1442 (1); ARGUED there and here).
The consumer is already the weakest form on file: one physical side, the
neutral sector only, infinitely many cutoffs, an existential witness (A2, A3).
It needs no area law. I found no sufficient statement that is weaker than the
seed and has a method. One remark for the owner: the Jaffe-Witten statement
asks for every compact simple group. Existence for SU(N) is on its path and
does not wait for the gap (GOAL.md, "Then").

**(d) Move capacity.** This is where the decision lies. Section 2.3 ranks it.

### 2.3 Ranking

The lane's rule 0 ("Is it worth doing?", as cited in row 1386 2.1: name the
open item that a row moves) gives the frame. No band row passes it, because no
band row has a method (1.4, 2.1, 2.2 (a)). So the question is which rows
with a method are worth the capacity. I rank three. The ranking is my
judgement (ARGUED).

**Rank 1. (V) Verify the reduction where the lane is exposed: the continuum
step and the neutral consumer, in Lean, in the order of the checked design.**
- What it moves: the standing of A2 from "hand proof, each link read once"
  to "kernel-checked". A2 is the premise of every seed row since row 1367,
  and no kernel has checked it (1.5). Row 1457 5.3 names the most likely
  place of a real gap: the explicit finite-aspect theorem (W7), a chain of
  numerical inequalities with one check (row 1162).
- Why now: the owner's rule of 2026-11-13 lets no proof note land with
  neither a formal check nor a computation (as row 1610 section 4 item 3
  records it). The reduction is the lane's one positive result on the gap. It
  cannot land as it stands.
- It is already on the lane's plan, and it is unblocked. Check 1458 named
  the next rows: the corrected statement file, then the upper half. They
  waited for the replay of row 1455. The replay ended on 2026-11-26T01:38Z
  and no Lean row was queued after it (3.1). The first product stands alone:
  a kernel-checked criterion on the release's own objects, "exponential
  clustering of the lattice states gives the gap of the limit", which the
  release does not contain by row 1457's reading (its section 6, Stage 2).
- It has a method, a measured cost and no dependence on the wall. Stage 1
  took six build rows for about 3,200 lines. Row 1457 sizes the whole chain
  at 16,000 to 28,000 lines (a guess there).
- Its risk: the form of the consumer may change if an engine appears that
  wants another seed. The neutral consumer has not changed since row 1461.
  The upper half does not depend on the form of the seed: it reads the
  clustering bound (EC-nu) only.
- What it is not: it is not progress on the seed. The lead holds an owner
  rule of 2026-11-11, "the crux over packaging" (it is not in this folder
  under that name). If the owner reads it as covering formal verification,
  this rank falls and Rank 3 is first. I read it as about notes and posts.
  This is the owner's call.

**Rank 2. (S) Standing probes at low duty.** They cost little. In my
judgement a new model or a new published method is the likely source of an
engine; a further pass by the same models over the same folder is not.
- Release the held weekly watch, row 1599.
- When the lead moves a model row in the settings to a new model of any
  provider, run the closed-folder solve brief once on it (the first three
  paragraphs of this row's brief, no lane files), and one cross-provider check
  with the tests (g1) to (g6). Two rows for each new model.
- Keep the triggers on file: (R1) to (R12), the component triggers of row
  1553 3.3, the reopen condition of row 1641, and the floor trigger of row
  1470. I add none. Section 2.1 gives no reason to.

**Rank 3. (U) New mathematics off the band. The owner chooses the item.**
- SU(N) existence. It is on the path of the Jaffe-Witten statement. First
  row: a reading row that lists every place where the release and the
  complete account use SU(2) itself (the three-sphere, quaternions, the
  centre Z_2, explicit characters) and gives each a status for N >= 3.
- Uniqueness of the continuum limit, (A1*). Stopped two days ago under Rule
  D1 because it has no reader on the gap chain (G2). As a clause of the
  existence theorem it needs no reader there: the release's limit is along a
  subsequence (A5). If the owner wants it for that reason, the restart rows
  are the ones row 1586 named: `gap-univk-rar-allsides`, then
  `gap-univk-geo-refiled`.
- The T0 port. By row 1449 Q4 (a reading; check 1450 holds after
  correction) and the replay of row 1455, the release covers the existence
  clauses that the port was built for. What remains of the T0 contract is for the lead's port map
  to say; I did not read `parts/witness.md` and I rank nothing here.

**Not ranked, with the reason.**
- A proof row on (VIR-down), (HOT), (E1), the magnetic deficit, (W-mix), a
  swap moment or the flux lower tail: each is stopped on the record with its
  reopen condition, and nothing in this row meets one.
- A port of (HOT) or of the small-volume statement (SV-Z): it has a method
  and it would be the first proved selective statement at a physical size.
  It moves no input while the band has no method. Rows 1386, 1515, 1610 and
  check 1644 declined it for that reason, and 1.6 (iii) adds that a hot box
  at a coupling of human size lies below the release's floor.
- A further obstruction row: 2.2 (b).
- A pause. The three ranks above use the capacity: (V) takes the build
  runners where Lean is installed and one reader for each statement file;
  (S) takes the bulk reader weekly and two rows for each new model; (U) takes
  the proof models on the item the owner picks.

## 3. The first row of Rank 1, and its first component

### 3.1 The row

The design of the Lean chain is on file and checked: row 1457 section 6 gives
the stages, and check 1458 holds after correction and names the next rows:
"finish Stage 0-1 (row 1459 and the corrected statement file after the
replay); Stage 2, the upper half massGap_of_expClusters". Stage 1 is built
(rows 1459 to 1525). Stage 0 and Stage 2 need the release's compiled files.
They waited for the replay of row 1455, which ended on 2026-11-26T01:38Z
(`lean/gapchain/RECEIPT.md` L189 to L190 lists them as the next rows). No
row was queued after it: there is no `Statement.lean` in `lean/gapchain`, no
Lean file there names `massGap_of_expClusters`, and FINISH.md has no
`lean-gap-chain` row after 1525. So the first row is the one
check 1458 named. I first wrote "hardest node first" (W7). Row 1457 section 6
ends "What not to do first: W7. It is the hardest and needs nearly all of the
rest." I follow the checked design.

**`lean-gap-chain-stage2-upper` (build row; Lean is on the Mac mini only; the
number is the lead's).**

Target.
1. Stage 0: the statement file of row 1457 4.1 to 4.5 with the corrections of
   check 1458 (dependency U1, the blocking-factor and test-domain hypotheses,
   the time-axis name, the same-witness packaging), compiled against the
   release, with `sorry` in the proofs only.
2. Stage 2: the upper half with no `sorry`: `massGap_of_expClusters`. In
   words: if the infinite-volume lattice states of the construction cluster
   exponentially in time, at one physical rate m, on the tr F^2 observables
   on the odd grid of times (the statement (EC-nu)), then the continuum limit
   has a unique vacuum and a mass gap m in its reconstructed tr F^2 sector.
   Nodes U0 to U7 of row 1457 5.1; about 1,300 to 2,200 lines (a guess
   there). Check 1458 resolved risk R1: the public lattice clauses of the
   release give positivity of the reflection form and the reconstruction.

Consumer. Every proof of a seed must end at (EC-nu) to reach the gap of the
release's limit. After this row that last step is kernel-checked on the
release's own objects, and the lower half (the seed to (EC-nu), nodes W2 to
W11) is the only hand part left.

Decisive outcome. `lake build` passes and `#print axioms` on
`massGap_of_expClusters` gives exactly `propext`, `Classical.choice`,
`Quot.sound`. Or the row reports the first declaration that does not
type-check, with the corrected statement; a corrected statement goes back
through a faithfulness reading before anything is built on it.

Why it is not equivalent to the seed. It is the consumer: an implication with
a clustering bound as its hypothesis. It asserts nothing about the Wilson law.

Where it must fail for weak four-dimensional U(1) and five-dimensional SU(2).
Nowhere, and it must not. The upper half is a statement about limits of
reflection-positive lattice states; it does not read the group or the
dimension. What fails in those models is the hypothesis: weak
four-dimensional U(1) has no exponential clustering (a theorem, given Guth
and Froehlich and Spencer), and five-dimensional SU(2) is believed to have
none. The tests (g1) to (g6) are tests for inputs. This row supplies no
input.

Process. The lane's memory rule for Lean builds: the replay of row 1455
peaked at 6.73 GB at two threads, above the 6 GB cap of the Mac mini, so this
row must load the replay's compiled files and must not rebuild the release.
No `native_decide`. Every theorem printed with its axioms. A receipt. A
cross-provider reading of the statement file for faithfulness before Stage 2
starts (the points of row 1457 4.1, 4.3, 4.5).

After it, in the design's order: Stage 3 (the lower half with the kappa-seed
as hypothesis: the twisted tori and transfer operators W3, W4, then W6, W9 to
W11), then Stage 4 (W7, W8).

### 3.2 A component of the same option, started here: the numbers of W7

The first row needs Lean and the release, and this machine has neither. So I
started the one part of option (V) that needs no tool: the node that row 1457
5.3 calls the most likely place of a real gap (W7, Stage 4 of the design).

I re-derived by hand every numerical inequality of the section "An explicit
aspect for the one-cube test" of `gap-solve9-astra62.md` (L213 to L227). This
is a reading of the arithmetic only. I read the statements of its inputs (3)
and (4) (L48 to L63) and the numbers below agree with them: with s_0 = 1/2
they give the factor 3/2 and the ratio d = 3/4. I did not check the proofs of
(3) and (4), and I did not re-read (5), (8), (9). I ran no script and no Lean.

| # | Line of the file | My derivation | Verdict |
|---|---|---|---|
| 1 | sup over z >= 0 of z^2 e^(-z/4) <= 64 | the maximum is at z = 8 and equals 64/e^2 < 9 | HOLDS (with room) |
| 2 | each sector trace has second derivative at most 96 on s in [1/2, 3/2] | (log x)^2 x^s = (log x)^2 x^(s - u/n) x^(u/n), and s - u/n >= 1/2 - 1/512 > 1/4, so the first two factors are at most 64 by line 1; the sum of x^(u/n) is at most 3/2 (the file's input) | HOLDS given the input |
| 3 | the signed sums I and the crossed coefficients H have second derivative at most 768 | eight sectors; H is an average of eight signed values of I | HOLDS |
| 4 | h = (3/2)(3/4)^511 < 2^(-169) | (3/4)^3 = 27/64 < 1/2, so (3/4)^510 < 2^(-170); then (3/2)(3/4) = 9/8 and (9/8) 2^(-170) < 2^(-169) | HOLDS |
| 5 | 2^(-70) <= r <= 2^(-69) for r = ceil(n 2^(-70))/n, n >= 2^70 | y <= ceil(y) <= 2y for y >= 1 | HOLDS |
| 6 | abs H'(1) <= h/r + 384 r < 2^(-59) | Taylor at 1 +- r with H(1 +- r) >= 0, 0 <= H(1) <= h, abs H'' <= 768 gives the first bound from both sides; h/r <= 2^(-99) and 384 r < 2^9 2^(-69) = 2^(-60) | HOLDS |
| 7 | U_N <= (3/2)(3/4)^255 < 2^(-84) | (3/4)^255 = ((3/4)^3)^85 < 2^(-85) | HOLDS |
| 8 | - x log x <= sqrt x on [0, 1] | the maximum of - sqrt x log x is 2/e < 1 | HOLDS |
| 9 | - x log x < 2^(-47) gives x <= 2^(-46) or x >= 1 - 2^(-46) | x(1 - x) <= - x log x; if x <= 1/2 then x/2 <= x(1 - x); if x >= 1/2 then (1 - x)/2 <= x(1 - x) | HOLDS |
| 10 | 7 2^(-23) + 8 2^(-84) < 2^(-19) | 7 2^(-23) < 2^(-20) | HOLDS |
| 11 | 56 2^(-18) < 1/1000 | 56/262144 < 0.00022 | HOLDS |

So the arithmetic of the riskiest node has no wrong number that I can find.
What a build row must still test is the structure: the bound 3/2 for every
sector, the zero slope of the vanishing crossed coefficients, and the passage
from the 160 h comparison to "all seven top weights take the same side".

### 3.3 Notes for the lead (I edited no other file)

1. Row 1597 K4 says that a seed proof plugs in at
   `(torusData beta hbeta).seed N < 1/5041`. By 1.5 a proof of (PUR-io) does
   not plug in there. The brief's sentence on the Lean chain should be read
   with the same scope. A one-line correction in the lane's standing text
   would stop a later row from relying on it.
2. The registry row VIR-DOWN could take the wording at the end of 1.6.
3. Row 1470 (the floor 2^3457, "closed by count") has no check row. Check
   1467 covers the 2^2800 of row 1464 only. A statement that uses the larger
   number should say that it is unchecked.
4. This file's hand proof (Proposition COOL) is three lines of calculus and is
   on file in substance. It does not need to land as a proof note.

## 4. Labels

| Statement | Label | Where |
|---|---|---|
| The tables of 1.1 | ON FILE, with the anchors given; B to G read as RESULT texts | 1.1 |
| The scope of the Lean chain | ON FILE; established by reading `Assembly.lean`, the theorem names of the eight modules, `TheoremS.lean` L534, RECEIPT-1f and row 1457 5.2 | 1.5 |
| Proposition COOL (a) to (d) | PROVED here given (S1) to (S3) and (R); ON FILE in substance (row 1610 EQ-down (b); check 1630 (RB)) | 1.6 |
| Reading 1 (the thermal seed is an identity for log tau_s) | PROVED from COOL (c) | 1.6 |
| Readings 2 and 3 | ARGUED; reading 2 uses the scaling picture as a guide | 1.6 |
| The verdict on row 1649, points (i) to (v) | ARGUED; a judgement over the record | 1.6 |
| "No new attack" from the nine candidates | ARGUED; candidates 3, 4, 5 found by grep only to be absent by name | 2.1 |
| The concave form of candidate 3 is false; candidate 8 has no route | GUESSED | 2.1 |
| The doubling identities of candidate 4 | ARGUED (three lines from (T5) to (T7); not written out; not used) | 2.1 |
| Options (a), (b), (c) | ARGUED | 2.2 |
| The ranking (V), (S), (U) | ARGUED; a judgement; one point is the owner's call | 2.3 |
| The first row is the one check 1458 named, and it was never queued | ON FILE: row 1457 section 6; check 1458 RESULT; row 1455 RESULT; the file list of `lean/gapchain`; grep of FINISH.md for `lean-gap-chain` | 3.1 |
| The eleven numerical lines of W7 | re-derived here by hand: all HOLD; the structural inputs were not re-read | 3.2 |
| (PUR-io), (VIR-down), (HOT), (K-I), (K-II), (A1), the gap | OPEN | |

Not done in this row: no Lean, no numeric run, no web search; no check of any
row; rows 1378 to 1596 read as RESULT texts except those listed in section 0;
`library/gap-direction8-astra62.md` not opened beyond its RESULT text; the
account and the release's sources not read; (R) and (S1) to (S3) not
re-derived.

Provenance: Claude Fable 5.2 (claude-fable-5-2), high effort, laptop subagent
of the lead session; author only, checked by no one; hand arguments only;
nothing committed, pushed or posted; no other file written. Written
2026-11-28, finished at 00:51Z (date -u).

Credits: Balaban; Sussman and Alpoge, with Claude and Codex as authors of
their text (the account and the release); the lane's rows by gpt-6.2-astra,
gemini-4-neon, Claude Fable, Claude Opus and gpt-6-luna, named at each use.

RESULT: Row 1643 (Claude Fable 5.2 high; author only, unchecked; no Lean, no numeric run). Outcome: NONE of (a), (b), (c), (d). No open input moves.
Task 1. Section 1.1 lists with anchors what rows 1378-1651 proved and checked: the consumer, identities, tests, negatives; nothing at a fixed physical
size above the account's range. Scope finding (1.5, Lean sources): the kernel-checked theorem is the periodic cube seed at one fixed coupling, with no
twist, C_z or P_0; (PUR-io) does not plug into it; the neutral consumer and the continuum step are hand proofs. PROVED here (elementary; on file in
substance as EQ-down (b), (RB)): Proposition COOL: with tau_s the cooling time at level s, (VIR-down) at rate kappa at a level-curve point holds iff
(log tau_s)' >= kappa, and the thermal seed is the identity "log tau_s falls by at least log(tau_s(beta_h)/u) from beta_h to beta_K". Row 1649 is
right as a stop for (T-down) and too short: (HOT) is not supplied; the window holds a weak part below the release's floor and an infrared stretch
besides the band; the line is the thermal seed plus sign conditions; a chain of order-one steps would give (PUR-io) by Theorem K2 without it.
Task 2. Nine candidates written before searching give no new attack; I have no order-one design with a method and propose no band row. Ranking (a
judgement): 1. (V) verify the reduction in Lean in the checked design's order; 2. (S) weekly watch, one closed-folder solve per new model; 3. (U)
new mathematics off the band at the owner's choice. Task 3. First row: Stages 0 and 2 of row 1457 (`massGap_of_expClusters`), named by check 1458
and never queued since the replay ended. Started here: the eleven numerical inequalities of W7 re-derived by hand; all hold.
