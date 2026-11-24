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

## 1. What rows 1460-1495 say (Step 1, written 2026-11-24T19:20Z)

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

## 2. Question 1: what changed, what was restated (Step 2, written 2026-11-24T19:45Z)

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

## 3. Question 2: is the weak-side branch (T1) on the critical path? (Step 3, written 2026-11-24T19:45Z)

Answer: no. Park it. Reasons, in order of weight.

1. **T1 has no consumer.** A proved T1 puts the blocked Wilson family in a tube at readout X (best case about 100). By 2.4, a class that the chain can use at readout X must already imply the gap at the matching sizes. No such class is defined at X, because its definition is T2's entry class. So T1 would prove membership in a class that does not exist yet. (argued)
2. **T1's floor does not meet any T2.** Pointwise methods stop near 1e4 (row 1472, checked). The best case is X about 100 (row 1470, unproved). The end class starts at 0.00872 (row 1473). With the one-loop drift 0.2575 a step (guide), the stretch from 100 to 2.3 alone is about 380 side-two steps, each of order-one type. So T1 does not shorten the part that has no method. (read and arithmetic)
3. **T1 is not selective.** A small-field step with explicit constants holds for SU(2) in five dimensions and, with the monopole gas, for U(1). It is a carry at weak coupling. The lane's rule "hardest first" puts it after the order-one step. (argued)
4. **T1 is not in doubt in kind.** Balaban's method gives it for some floor. The open point is the size of the floor, and that matters only when a T2 names an entry coupling. (read: rows 1464, 1470)

What T1 work is still worth keeping: none as a row now. The signed one-loop decrement of Q2 (row 1479's unrun computation) is a consistency number. It would not move (PUR-io).

Reopen T1 when a T2 candidate names its entry class and its entry coupling X_in. Then T1's statement is fixed: "the blocked family at readout X_in lies in that class", and its floor can be compared with X_in.

