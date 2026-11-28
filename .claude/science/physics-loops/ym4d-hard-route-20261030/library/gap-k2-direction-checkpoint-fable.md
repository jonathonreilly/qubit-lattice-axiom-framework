lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T07:03Z

# Direction checkpoint over rows 1460-1495 (queue row 1496)

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, pinned at commit b223fb2f9. Started 2026-11-24T19:03Z (date -u). This is a direction note. It is not a proof row, not an audit, and it grants no status.

Labels used below: **proved** (a written proof is on file and I name the row), **checked** (another model read it line by line; I name the check row), **read** (I read the statement in the row or source; I did not re-derive it), **sketched** (argument outlined here, steps missing), **guessed** (my judgment, no argument).

## 0. Plan

1. Read the RESULT lines of rows 1460-1495 and their checks. Tabulate what each established (Section 1).
2. Question 1: what changed what is possible, what was restated; the consequence of checks 1484 and 1494 for the K-II programme (Section 2).
3. Question 2: is the weak-side branch (T1) still on the critical path without an order-one method (T2) (Section 3).
4. Question 3: one attack and its first lemma, or the statement that none passes the filter t1-t6 (rows 1386, 1442) with reopen triggers (Section 4).
5. The next two rows with decisive outcomes (Section 5).

Statements to settle: (a) the target reduction on file, Jaffe-Witten for 4D SU(2) from (M-io-exists); (b) the standing of K-II by step certificates; (c) the standing of T1 and T2; (d) one named attack or a reasoned "none".

## 1. What rows 1460-1495 say (Step 1, written between 19:03Z and 19:11Z; no clock read in that step)

Source: the RESULT lines of FINISH rows 1460-1495 at commit b223fb2f9, each read in full. I did not re-derive them. "Checked" names the check row and its verdict.

| Row | Content (read) | Standing |
|---|---|---|
| 1460 | Lemma LD-1 (blocked log-Hessian), Lemma SE, Theorem LOSS for the plain kernel at side 2^40. Remark PATH. | Check 1463: LOSS, LD-1, LD-2 hold after correction. PATH fails as stated. "The Lean flow is not a band vehicle" did not follow from 1460. |
| 1461 | (L1) any infinite set of late least-root depths carries a calibrated limit. (L2) bounded width. (L3) reciprocal-slope bound. Averaged inequality (4)/(6) open. | Checks 1462, 1465: hold after wording repairs. The useful target is **(M-io-exists)**. |
| 1464 | The release forces g^-2 above (2^51 L)^100 and 2^1600. No step at order-one coupling at any side. | Check 1467: holds. |
| 1466 | LD-loc for the release's adapted image refuted as a uniform assertion. | Author only. With 1464: the release's map is not a band vehicle. |
| 1468 | Design of the K-II tool: map Q2. Lemma TW (sixteen twisted masses carried exactly). Theorem K2 (conditional chain). Proposition GA (Gaussian readout marginal in 4D). | Check 1469: holds after correction as a design. Line 372 false: closed classes at order-one coupling are on file (rows 1345, 1348, 1418). |
| 1470 | Step certificates above the release floor are closed by count (x above 2^3457). | Author only, read only. |
| 1471 | Theorem END-K2 and entry Theorem EN: the end class holds only for beta at most log(1 + 1/(42e)), about 0.00872. | Check 1473: holds after correction. Rational parts kernel-checked. |
| 1472 | Pointwise small-field step for Q2 fails below x about 1e4 to 2.56e6 on explicit fields. | Check 1478: holds. |
| 1474 | T2 not solved. Six candidate representations fail at named lines. Lemma NG (heat noise, Ricci 2). | Check 1476: holds after correction. NG is classical (row 1477). No T2 and no impossibility. |
| 1475 | The class of row 1348 contains a member at beta = 23/10 with purity at most 41/81. Class-wide descent refuted. | Check 1484: holds. **Exact mass-preserving steps change the representation, not the target.** |
| 1477 | Curvature methods reach Wilson beta below 1/6 at most (Shen-Zhu-Zhu; Cao-Nissim-Sheffield). | Reading (luna). |
| 1479 | Laplace form of a Q2 step; slope -5 gbar in the action class; first-step decrement not selective. | Check 1483: FAILS as stated on a finite torus. Holds in an ordered limit. The signed SU(2) decrement is open. |
| 1480 | The integrated cold-block activity about the Gaussian centre violates Kotecky-Preiss at all large x. | Check 1488: holds. |
| 1481, 1482, 1486 | No tool of the Alpoge-Claude RH proof transfers. Lemma PRG. | Check 1487: closed on the record. Trigger (R7) kept. |
| 1485, 1489 | Interface row sum R at beta = 23/10 lies in an interval that contains 1. | Checks 1488, 1491: hold. R below 1 is open (row 1493, no result at the pin). |
| 1490 | Nonlinear Cartan-stripe centre is the unique local minimum with Hessian at least 1/108900. It cancels row 1480's quartic term. | Check 1491: holds. |
| 1492 | The normalized cold singleton about the nonlinear centre exceeds its rooted budget at fixed angle t = 1/8. | Check 1494: holds after correction. R2: a failure refutes only the star gas of unsplit marks, not an expansion that first decouples the Gaussian covariance (Balaban; Sussman-Alpoge). |
| 1493 | Certify the finite interface forms at 23/10. | No result at the pinned commit. |
| 1495 | The two-block test at x = 100 is open: the enclosure spans both decision boundaries. | Author only. |

## 2. Question 1: what changed, what was restated (Step 2, written 2026-11-24T19:11Z, date -u)

### 2.1 The target, as on file (read)

- (PUR-io), row 1468 Fact PUR with rows 1461, 1462, 1465: one side l and one level g_0, with P_K = Z_+(2u)/Z_+(u)^2 at least 457/625 at infinitely many K, on n = l b^K and u = n/512. It gives (M-io-exists) and a gapped calibrated limit with rate at least (2/l) log(2^18/5041). Checked by Opus (1462, 1465).
- P_K is a function of sixteen numbers: the Wilson masses on two tori with eight twists (row 1468, 3.1).
- Reading (mine, elementary): 1 + s = Z_+(u)/lambda_0^u is the neutral thermal sum of the box of side n at inverse temperature u. So (PUR-io) says that the neutral thermal sum of a box of aspect ratio 512 is at most 25/21 at one physical temperature, at infinitely many cutoffs. This is on file as the "neutral thermal sum" of rows 1367 and 1386. It is not new.

### 2.2 What rows 1460-1495 established that changes what is possible

Five results change the map. Each is a negative or a weakening, and none moves (PUR-io).

1. **The consumer got weaker (rows 1461, 1462, 1465; checked).** The gap needs a seed at infinitely many least roots, not at all late K. This is real progress on the reduction. It is the only positive change in the range.
2. **The release's own map is not a band vehicle (rows 1464, 1466, 1467; 1464 checked, 1466 author only).** Its step exists only for g^-2 above (2^51 L)^100. So any chain through the band needs a different map and its own analysis. Sussman and Alpoge's release (with Claude and Codex) gives the start (BASE) and nothing below its floor.
3. **A chain of exact mass-preserving steps cannot move the target (check 1484).** See 2.4.
4. **The end class is reachable by hand only at beta at most 0.00872 (rows 1471, 1473; checked, rational parts kernel-checked).** Published curvature methods reach beta below 1/6 (row 1477, reading). So the order-one part runs from readout about 2.3 down to about 0.01 to 0.17, not to 1.
5. **The cheapest weak-side representation is dead (rows 1472, 1478, 1480, 1488, 1492, 1494; checked).** Pointwise bounds fail below x about 1e4. The integrated star gas of unsplit marks fails at the Gaussian centre and at the nonlinear centre at fixed angle. See 2.5.

### 2.3 What was only restated

- Theorem K2 and (K2-STEP) (row 1468) restate (STEP) of row 1386 at one scale. Row 1468 says so itself (4.5: "That is the wall, restated at one scale").
- T2 as "a finite, evaluable criterion for decay at readout 2.3" (row 1474, Remark END) restates the cube criterion (W) of row 691 and the in-law criterion of row 845. Check 1476: no T2 representation was constructed and no impossibility was proved.
- Lemma NG (row 1474) is the classical Bochner estimate (row 1477). It is a gain that reads the group and not the dimension, like Proposition G1 of row 1128. It is not a carry.
- The first-step decrement of Q2 (rows 1479, 1483) is not selective: Wilson U(1) has a positive first-step coefficient too. The signed SU(2) decrement is open, and it would be the known one-loop statement, not a mechanism.
- The RH-tools rows (1481, 1482, 1486, 1487) found only identities and positivity already on file. Closed, trigger (R7).
- The interface row sum R at beta = 23/10 (rows 1485, 1489) is open in [529/2048, 7). Nothing was decided.

### 2.4 Consequence of check 1484 for the K-II programme (argued here from Theorem K2; elementary)

Statement (proved in two lines from row 1468's Lemma TW and Theorem K2). Let C_0, ..., C_N be classes with (STEP_k) and (END). Then every family in every C_k has purity at least 457/625 on its own sixteen tori.

Proof. Q2 keeps each of the sixteen masses, and the purity is a function of the masses. Apply N - k steps and (END). QED

So a class in a K-II chain is never a class of "regular local actions at readout x". It is a class in which the gap already holds at the matching sizes. Row 1475 shows the cost: the iterable class of row 1348 has a member at beta = 23/10 with purity at most 41/81, so that class is in no chain. Three consequences follow.

- (a) K-II cannot lower the difficulty. It can only cut one proof of (PUR-io) into steps. Each step is as selective as the whole: it must separate Wilson SU(2) from members at distance of order one (the K7 neighbours, the two-vacua members of row 1475, U(1), five dimensions).
- (b) The value of a step is its method. At weak coupling the method exists in kind (Balaban; Sussman and Alpoge with Claude and Codex), and the class is narrow because the expansion has a small parameter. At readout of order one no small parameter exists, so a narrow class must be given by numbers. Row 1468 sized that: 100 to 400 steps in the best case, each beyond exact evaluation (the smallest in-law instance needs at least 1e154 operations, row 1474 with Lemma DIM of row 1326; guide values, not proved).
- (c) Hence "build components of the Q2 chain" is not a route to (PUR-io) today. Components C2 (end class, row 1471) and the twist carry (Lemma TW) are done and correct. They do not shorten the open part.

### 2.5 Consequence of check 1494 (R2) for the weak-side tests

Check 1494 R2: a pair value above 1/(81 e) refutes Kotecky-Preiss only for the star gas built from the unsplit marks. It does not refute an expansion that first decouples the Gaussian covariance, as Balaban's and Sussman-Alpoge's do. So:

- Rows 1472, 1480, 1492 and 1495 test one representation, the cheapest. Their failures close that representation and say nothing about T1.
- The representation that T1 needs is the published one: a covariance decoupling (random-walk or multiscale), then polymers. With explicit constants at block side 2 this is a rebuild of Balaban's small-field step. Row 1470 found no number in Balaban (CMP 109 p. 259, CMP 122 pp. 175, 185) and a floor of at least 2^3457 in the release. Row 1470's best case X about 100 rests on three unproved assumptions.
- So the exact two-block test (row 1495) cannot decide T1 in either direction. Its enclosure is also 40,000 binary orders wide. I judge it not worth a second row (guessed, from the stated scope R2).

Together with 2.4: the K-II programme as a whole is a correct conditional frame with no open component whose proof would move (PUR-io). Its weak part is a large rebuild with no decision value now. Its order-one part is the open problem, with no representation.

## 3. Question 2: is the weak-side branch (T1) on the critical path? (Step 3, written 2026-11-24T19:11Z, date -u)

Answer: no. Park it. Reasons, in order of weight.

1. **T1 has no consumer.** A proved T1 puts the blocked Wilson family in a tube at readout X (best case about 100). By 2.4, a class that the chain can use at readout X must already imply the gap at the matching sizes. No such class is defined at X, because its definition is T2's entry class. So T1 would prove membership in a class that does not exist yet. (argued)
2. **T1's floor does not meet any T2.** Pointwise methods stop near 1e4 (row 1472, checked). The best case is X about 100 (row 1470, unproved). The end class starts at 0.00872 (row 1473). With the one-loop drift 0.2575 a step (guide), the stretch from 100 to 2.3 alone is about 380 side-two steps, each of order-one type. So T1 does not shorten the part that has no method. (read and arithmetic)
3. **T1 is not selective.** A small-field step with explicit constants holds for SU(2) in five dimensions and, with the monopole gas, for U(1). It is a carry at weak coupling. The lane's rule "hardest first" puts it after the order-one step. (guessed for five dimensions and U(1); not checked against a written step)
4. **T1 is not in doubt in kind.** Balaban's method gives it for some floor. The open point is the size of the floor, and that matters only when a T2 names an entry coupling. (read: rows 1464, 1470)

What T1 work is still worth keeping: none as a row now. The signed one-loop decrement of Q2 (row 1479's unrun computation) is a consistency number. It would not move (PUR-io).

Reopen T1 when a T2 candidate names its entry class and its entry coupling X_in. Then T1's statement is fixed: "the blocked family at readout X_in lies in that class", and its floor can be compared with X_in.

## 4. Question 3: one attack, or none (Step 4, written 2026-11-24T19:19Z, date -u)

### 4.1 Verdict

**No attack that I can name passes the filter (t1)-(t6) and is not equivalent to a closed line.** This is a judgment over a finite list, not a theorem (guessed). (PUR-io) is not moved. The reasons are 2.4 and the table below.

By 2.4 every proof through a chain is a proof by classes in which the gap already holds. So an attack must supply one of three things. Each is tested here.

| Kind | What it must supply | State on file | Verdict |
|---|---|---|---|
| A. A narrow class given by a small parameter | A step with a convergent expansion | Exists only above the release floor 2^3457 (rows 1464, 1470) and below beta 0.00872 (row 1473). Between them no small parameter exists. | No method on about 380 side-two steps (guide). |
| B. A narrow class given by numbers | A finite certificate per step, or one certificate with a consumer | Smallest in-law instance at least 1e154 operations (row 1474; Lemma DIM of row 1326). The one open finite test, the interface row sum, has no consumer (4.2). | Closed by cost, or no consumer. |
| C. A sign (K-I of row 1386) | An inequality that carries a typical-field stiffness through an exact step | No candidate. Tomboulis's bracket has no sign (row 1025). (BUB) has no level form (row 1383). Curvature gains are of order one and read the group only (Proposition G1 of row 1128; Lemma NG of row 1474). | No first lemma. |

Candidates I generated in this session, before searching, and where each is on file (repo search: `grep -c -i` on FINISH.md and `grep -l -i` on library/, counts in brackets as rows and files):

| Candidate | On file | Fails at |
|---|---|---|
| Thermal reading: (PUR-io) as a bound on the neutral thermal sum at temperature 512/l; integration along beta at a fixed lattice | (VIR_K), row 708; row 1402 Phase 1 ("thermal (Casimir) statement") | Equivalent to a closed line. The integrand is the target at each coupling. |
| Variational lower bound P at least norm(T^u psi)^2 / Z_+(u)^2 with an explicit trial state psi | Not found under this name. Elementary: a product or free-boundary trial has overlap e^(-c n^3) with the vacuum, and T^w-smoothed trials are circular. | Dead at once (sketched). No row. |
| Multiscale Bakry-Emery along a Polchinski or heat flow (Bauerschmidt, Bodineau, Dagallier) | [8 rows, 35 files]; inputs (TILT-COV-sup), (LOC-COV) | Needs a supremum of tilted covariances over external link fields. No correlation inequality for SU(2) gauge fields replaces it. Worst case, requirement (f). |
| Typical-field Bochner (integrated Gamma_2; Witten Laplacian on one-forms) | Curvature class, row 957; Lemma NG; Proposition G1 | The Ricci gain 2 is cancelled at order one by the mean of the term with F and [X, X]. The same computation gives no gap for the O(4) model in d at least 3. Not selective in dimension (sketched). |
| Loop-equation bootstrap with exact dual certificates (Anderson, Kruczenski; Kazakov, Zheng) | [16 rows mention a bootstrap in some sense]; rated "computer step, guide only" in rows 766-848, before the rule of 2026-11-20; class "bootstrap certificates" in row 1402 | See 4.3. It bounds loop expectations at fixed precision. No sufficient criterion reads such inputs. |
| Correlation inequalities (Griffiths, Ginibre, Simon-Lieb forms) | [12 and 19 rows] | None holds for SU(2) plaquette weights; row 737 has an explicit negative term. |
| Change of action, block map or reduction | Row 1442, check 1443 | Cosmetic. The band is a property of the target. |
| Tools of the Alpoge-Claude RH proof | Rows 1481-1487 | Closed, trigger (R7). |

So nothing here is new, and I claim no new statement in this section beyond 4.2.

### 4.2 The one open order-one line has no consumer (sketched; the test model is the lane's own)

Rows 1485, 1489 and 1493 try to certify R below 1 for the interface row sum of one open star at beta = 23/10. Row 1475 line 175 marks the criterion "Guessed". I asked what a pass would prove.

**Statement (JOIN-class), which a consumer theorem would need in its simplest form.** For every positive SU(2)-invariant plaquette weight w: if the open star of nine boxes with weight w has R(w) below 1, then the sixteen masses of w on the tori m = 512 v have purity at least 457/625 for all large v.

**Claim: (JOIN-class) is false as a statement over weights (sketched, not proved).** Take a weight of van Enter-Shlosman type (a deep narrow well; `gap-crux-fp.md` Proposition V; the lane's first-order test model). At its coexistence coupling the infinite system has an ordered and a disordered phase. The transfer operator then has two near-degenerate neutral vacua, and the purity tends to 1/2 at most (Fact PUR direction: P at most (1 + s^2)/(1 + s)^2 with s near 1). A finite open star has free boundaries. Free boundaries lower the energy-entropy balance of the ordered phase by a boundary term of order one for a star of fixed size, so at the coexistence coupling the star sits in the disordered phase with probability tending to 1 as the well narrows. Its interface correlations then tend to 0, and R(w) is below 1. The Potts model with many states is the standard case: the threshold of a finite free cluster is (S - 1)/B log q against (1/d) log q in the bulk, with B/S below d.

What is not done: the estimate R(w) below 1 for an explicit well, with constants. That is one hand row if anyone needs the refutation in full.

Consequences.

- A pass of the local test at Wilson 23/10 proves a bound on one finite open system. It does not give decay, even for bare Wilson at 23/10. A proof would need the joins, the charged boundary variables and the winding terms, with Wilson-specific numbers at each stage (row 1485 says this in its "Proved implication" paragraph). That is kind B again.
- Even a full lattice gap for bare Wilson at 23/10 is not on the trajectory. By 2.4 the chain needs the gap for the blocked family at readout 2.3, which is not the Wilson weight.
- So row 1493's result, pass or fail, changes no decision. I recommend no successor row to 1493 and none to 1495.

### 4.3 One change of standing that the record has not used (read; a trigger, not an attack)

The bootstrap of Kazakov and Zheng (arXiv 2404.16925, SU(2) included; row 766 era: "the SU(2) trace identity closes the loop equations on single traces") was rated "guide only" under the no-compute rule of 2026-11-01. The owner replaced that rule on 2026-11-20: an exact computation checked by the Lean kernel is a proof step. A semidefinite bound has an exact rational dual certificate, which is a finite identity plus a positive-semidefinite check. So trigger (R4) of row 1474, "a rigorous in-law method of polynomial cost, not sampling", is now met in part: for expectations of Wilson loops of bounded length in any translation-invariant reflection-positive state, at order-one coupling.

It is not an attack, because no consumer exists. (PUR-io) needs a difference of free energies of size e^(-m u), or a contraction on all observables. Loop expectations at fixed precision give neither (row 1326: no statement on file is both finite and sufficient). I did not find a criterion that reads them, and I tried only briefly (guessed: none of the standard finite-size criteria has this form).

### 4.4 Reopen triggers (the full list, with two additions)

On file: (R1) a published non-abelian inequality at order-one coupling that fails for compact U(1), naming observable, ensemble and scale (rows 1442, 1443; last scan row 1446, not triggered). (R2) a candidate that passes (t1)-(t6) and states its carry. (R3) (A1) in rate form. (R4)-(R6) of row 1474. (R7) of rows 1481, 1487.

Additions from this checkpoint:

- **(R8) A consumer for bounded-precision in-law data.** A proved theorem of the form: finitely many expectations of loops of length at most N in the infinite-volume state, each known to a fixed precision, imply exponential decay of all neutral correlations, or purity on the tori m = 512 v. With 4.3 the inputs are then certifiable. The theorem must fail for the first-order test model (4.2), so it must read more than one open cluster.
- **(R9) An entry class for T2.** A class of families at readout X_in of order one that is given by bounds naming no orbit, is closed under one Q2 step into a class of the same kind, and excludes row 1475's member. When one exists, T1 gets its statement and its floor (Section 3) and returns to the path.

## 5. The next two rows and their decisive outcomes (Step 5)

No attack row. Both rows are decisions.

**Row 1, `gap-k2-direction-checkpoint-check-astra62` (cross-provider check of this file; gpt-6.2-astra max).** Order: (i) the statement and proof of 2.4, and whether consequence (a) follows; (ii) Section 3 item 1, "T1 has no consumer"; (iii) 4.2: try to prove R(w) below 1 with purity at most 1/2 for one explicit deep-well weight, or show that the free-boundary argument fails for the pivot matrices; (iv) try to break 4.1 by naming one candidate of kind A, B or C that passes (t1)-(t6). Decisive outcome: if (i)-(iii) hold and (iv) finds nothing, the lead stops the K-II component rows (no successor to 1493 or 1495, no T1 row) and the band waits on (R1)-(R9). If (iv) names a candidate, its first lemma is the next proof row. If (iii) fails, the interface line keeps one more row: the join with charged boundary variables (row 1485 next row 2).

**Row 2, `gap-r8-loop-consumer-fable` (Claude Fable 5.2 high; held until Row 1 reports).** Decide trigger (R8): does any finite-size criterion on file (the rank-one test of rows 1373 and 1461; Theorem T of row 1332; the cube criterion (W) of row 691; the in-law criterion of row 845) reduce, exactly or with a stated loss, to finitely many loop expectations at fixed precision? First lemma to prove or refute: "for the Wilson state at beta = 23/10, the hypothesis of criterion (W) on a cube of side 4 follows from two-sided bounds of relative width 1e-3 on all loop expectations of length at most 16." I expect a refutation by a counting argument (the criterion reads the joint law of more than 1,000 links; guessed). Decisive outcome: a refutation with its count closes (R8) for these criteria and records what precision and length would be needed; a proof makes the bootstrap certificate the next build row, as the first order-one statement with a kernel-checkable proof.

## 6. Answers in short

1. Rows 1460-1495 weakened the consumer to (PUR-io) (checked), removed the release's map from the band, fixed the end class at beta at most 0.00872, and closed the cheapest weak-side representation. Check 1484 means a K-II chain cannot lower the difficulty: every class in it already has the gap (2.4). Check 1494 means the weak-side tests decide nothing about T1. The rest is restatement.
2. T1 is off the critical path until a T2 names its entry class (trigger R9).
3. No attack passes the filter. The interface test has no consumer (4.2, sketched). The bootstrap is now an admissible certificate method with no consumer (4.3). Triggers (R1)-(R9).

Credit: Balaban for the small-field and large-field method that T1 would rebuild; Ethan Sussman and Levent Alpoge, with Claude and Codex, for the YM4 Lean release, its kernel and contour mean, and the outline's Kotecky-Preiss step; Kazakov and Zheng for the bootstrap; van Enter and Shlosman for the first-order test model; Bauerschmidt, Bodineau and Dagallier for the multiscale criterion. Rows 1460-1495 are by Claude Fable 5.2, Claude Opus 5.5, gpt-6.2-astra and gpt-6-luna as their rows state.

Not done: no numeric run and no Lean (none was needed; memory was not measured). I read RESULT lines, not the full files, except rows 1386 (4.1-4.5), 1442 (triggers), 1468 (Sections 2-4.5) and 1485 (setup, pivot step, margins, next rows). Nothing here is checked by another model.

Finished 2026-11-24T19:19Z (date -u). Correction: the first draft of this file carried step times that I had not read from the clock; they are replaced by the times above.

RESULT: Row 1496 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; no numeric run, no Lean, RESULT lines read rather than full files). Direction checkpoint with a negative verdict: (PUR-io) / (M-io-exists) is not moved and no attack passes (t1)-(t6) without being equivalent to a closed line (a judgment over a finite list, not a theorem). Proved here in two lines from Lemma TW and Theorem K2 of row 1468: every class in a K-II chain already has purity at least 457/625, so a chain cannot lower the difficulty (the content of check 1484). Read: rows 1460-1495 weakened the consumer, removed the release's map from the band, fixed the end class at beta at most 0.00872 and closed only the cheapest weak-side representation (check 1494 R2). Verdict on T1: off the critical path until a T2 names its entry class (new trigger R9). Sketched, not proved: the interface test R below 1 has no consumer, because the class-level statement fails on the first-order test model with free boundaries. Read: under the rule of 2026-11-20 the loop-equation bootstrap is an admissible certificate method, with no consumer (new trigger R8). Open: (PUR-io), T2, the signed SU(2) decrement, and R at 23/10. Next rows: the cross-provider check of this file; then the decision of (R8), held.
