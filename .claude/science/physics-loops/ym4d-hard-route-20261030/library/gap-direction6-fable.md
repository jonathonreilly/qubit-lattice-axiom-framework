lead: anthropic/claude-fable-5-2/high laptop-subagent

# gap-direction6-fable (FINISH row 1597)

## Plan

1. Read FINISH.md rule sections (lines 1-84, 299-360) and GOAL.md.
2. Find queue row `gap-direction6-fable` (row 1597) and read its brief in full.
3. Read the lane sources the brief names (and what they rely on), one source per step, and append one result per step here.
4. Before calling a statement new: grep library/open-core.md, library/open-registry.md and the FINISH rows; cite matches.
5. Form the direction judgement the brief asks for; write it stage by stage.
6. End with one RESULT: line (decision, next rows or none / pause, what stays open).

Constraints: no edits in the lane checkout, no commit/claim/push, no posts, no numeric runs, relative lane paths only, search only inside the lane checkout.

## Steps

### Step 1. FINISH.md rules (lines 1-84, 299-360), GOAL.md, row 1597 brief: read.

Binding for this row: "Is it worth doing" (a row names the critical-path item it moves and what changes either way); rule 0a (grep open-core, open-registry, FINISH rows before calling anything new); "Equivalent is not progress" (2026-11-22: a sufficient condition equivalent to the seed or (W) is no progress; a proposed sufficient statement must show non-equivalence or say it cannot); computation only as a Lean-checked exact proof; no numerics here. GOAL.md lists the mass gap as a later target after T0; the lane's main YM work is the gap by the lead's 2026-11-10 decision (ON FILE, FINISH rows; to verify below).

Brief (row 1597) asks three decisions: (1) has a named trigger fired, or is an untested route on file worth one proof row; (2) switch to a different input, after row 1553 section 1.5 tests as corrected by check 1556; (3) is a pause the honest recommendation, and what a pause keeps running. At most two rows with full briefs, or none. No row equivalent to the seed. Every claim marked PROVED / ARGUED / GUESSED / ON FILE with anchor.

### Step 2. FINISH rows 1553, 1556, 1584-1590: RESULT text read (rows only; bodies below where needed).

- Row 1553 (Fable, direction 4): tests (g1)-(g6) for a selective input; Lemma ALG; stop (K-II) in rule-class form; triggers (T-copy), (T-ineq), (T-dual), (T-mix), (T-budget). ON FILE.
- Check 1556 (Astra): withdrew that stop with the Haar-preserving cut circle reaching a centre twist; line "(IR-LOSS) weaker than the seed by (A1)" FAILS; budget (A3): r < 1 + p/4. ON FILE.
- Row 1584 (Fable, direction 5): interpolation programme SPENT in sense (SP); pause band rows; triggers (T-mix sharpened), (T-carry), (T-sign), (T-front), (T-1583), (T-tau). ON FILE.
- Check 1585 (Astra): withdrew that pause with a coupled identity-to-centre-flip family at two-end Renyi-2 cost <= log 64; named the lower-tail lemma (L-tail). Front sweep verdict holds after correction (no group-selective order from RP, Markov, transfer positivity). Flux half only. ON FILE.
- Rows 1587 (Astra), 1588 (Neon): (L-tail) OPEN after three attacks each; checks 1589, 1590 (Opus): proved steps hold; "No step reads a property of 4D SU(2) that 4D U(1) or 5D SU(2) lacks"; nothing for Pi. ON FILE. Check 1589 notes the conditional-indicator route of check 1585 "was not tried" by row 1587 (to compare with row 1591 next).
- Row 1586 (Fable, (A1) skeleton): 27 open leaves, STOP (A1) by Rule D. ON FILE (check 1596 corrects reasons; read next).

Pattern so far (ARGUED, from the two withdrawals): each Fable direction row declared a stop; each Astra check broke it with one explicit object; each object then produced one proof row that ended OPEN and covered the electric half only. So a "spent" verdict here is a judgement over the record and has been wrong twice in its stated class. A third stop must say what class it is quantified over and what a check should try to break.

### Step 3. FINISH rows 1591-1596: RESULT text read. The brief's "Standing now" verified against the rows.

- "The flux lower-tail lemma failed three ways (rows 1587, 1588, 1591; checks 1589, 1590, 1595) and covers the electric half only": HOLDS. Precision (ON FILE, check 1595): the count is "neither proved nor refuted"; all three routes hit the same cost, a flux bound at a shorter period (check 1590: Theorem 2's premise "is at least r_1(2l), a flux bound at the shorter period, the same kind as (N-flux)"; check 1595: the loss in (10) "needs a short-period flux bound, the same cost as rows 1587 and 1588"). So "failed three ways" means three attacks stopped at one common wall, not three refutations.
- "The published two-purity bootstrap is equivalent to the seed (row 1592, check 1594)": HOLDS. Check 1594: "Nothing is strictly weaker than (PUR-io)"; the Q gate and 5/9 are weaker at a single box but equivalent over the allowed sides and cutoffs; "The same counting argument holds for 4D compact U(1) and 5D SU(2), so a selective estimate must enter in the finite-volume input" (row 1592).
- "The (A1) slot stops (row 1586, check 1596, corrected reasons)": HOLDS. Check 1596: stop HOLDS AFTER CORRECTION under Rule D1; "27 NECESSARY leaves" FAILS (a chosen route); "needs volumes exponential in K" FAILS (worst-case envelope); retiring (A1) on DRIFT FAILS (both Wilson carries open).
- "Two routes to a small swap moment remain untested (check 1583)": to verify in the check 1583 body (row text not yet read).
- Check 1593: row 1578 holds after correction; (T) and the refutation of (S) stay open. Not on the seed's path (check 1596: the strip test "settles neither the signed ledger nor the seed").

Next sources, in order: row 1553 body section 1.5 with check 1556 corrections (the tests); check 1583 (the two untested routes); row 1584 section 2.5 (triggers) and Step 13 (front sweep) with check 1585 (vi); check 1596 corrections; then parts/gap.md and the earlier pause row 1442/1443 triggers; then open-core and open-registry greps.

### Step 4. Source: library/gap-mech-direction4-fable.md sections 1.2-1.6, 3.1-3.3 (row 1553, Claude Fable; ON FILE; checked by row 1556).

- Tests (L186-196): (g1) 4D compact U(1) weak, name failing line l_1; (g2) 5D SU(2) weak, line l_2; (g3) gapped twins (does l_1 / l_2 also fire at the gapped member of the same family? then F reads algebra or dimension, not the law); (g4) gapless members with an SU(2) factor (product with a massless factor; K7 end point; adjoint-Higgs Coulomb phase); (g5) scale (hypothesis must fail when beta grows at fixed lattice; a range R <= beta^k fails); (g6) consumer (Q, C), carry with loss, method at order-one coupling, and why not equivalent to the seed.
- Definition (L170-178): an input is a triple (F, Q, C); it must read (P-law), (P-scale), (P-carry). "A fact with no (Q, C) gets no proof row."
- Two piles (L163-168): pile P (proved, answers NO to scale or law); pile S ((PUR-io), (HT), (R), (IR-LOSS), (K2-STEP): seed, stronger, or seed less a UV input; none has a method). "The two piles do not meet."
- Engine map 3.1 (L251-261): E-flow (needs a continuous symmetry on consumer data; absent), E-dil (needs exchangeable ferromagnetic copies; none in three splits), E-dual (needs sign-free dual; absent), E-comp (needs a comparison losing two dimensions or a Ginibre-type inequality; open/refuted worst case), E-exp ((K-II)/(K-III); no method). "I can design no engine that meets it."
- Triggers 3.3: (T-copy), (T-ineq), (T-dual), (T-mix), (T-budget).

Note for Decision 2 of this row: check 1556 (v) broke the E-flow "absent" entry in its stated class (the cut circle is Haar-preserving and acts non-trivially on gauge-invariant data), and the follow-up found the circle's covariance bound blind to neutral sectors. So the E-flow line now reads: maps exist; the missing part is a bound that is two-end and reads Pi. ON FILE (rows 1565-1574; verify in Step 6).

### Step 5. Source: library/gap-mech-direction4-check-astra62.md items (iii), (iv), (vii), (viii) (check 1556, gpt-6.2-astra max; ON FILE).

Corrections that bind how the tests are applied in this row:
- (iii) Lemma ALG's logic holds for the abstract group-independent engine (product with an admitted seedless spectator is admitted; P = P_W P_m). It overreaches for the seed as fixed in row 1468 section 3.1: "Adjoining a spectator gives a different theory". And: "This does not exclude an argument that uses the simplicity of the full group, the pure Wilson action or its calibrated trajectory." So (g4) kills factor-blind criteria; it does not kill a statement that reads the whole gauge group or the pure Wilson law.
- (iv) "fires" means the specified failure mechanism still applies. "Repeating a failure at two couplings defeats that line as evidence of gap discrimination. It does not prove ... that the whole hypothesis is independent of the law. A conjunction may contain both an algebraic factor and a dynamical estimate." So (g3) is a test of the selectivity evidence, not a refutation of the hypothesis.
- (iv) rows 1529 (HT) and 1542 (IR-LOSS): "Passes" is unproved (the 4D U(1) periodic weak-coupling input and the 5D premise are extra).
- (vii) "This implication places no lower bound on the difficulty of proving an inclusion ... The selectivity can reside in BASE, a single transition or END."
- (viii) the budget is "a sufficient strict test on the envelopes", r < 1 + p/4; "Necessity for other band proofs is open."

Reading for this row (ARGUED): as corrected, the tests are filters on evidence. (g6) (consumer, carry, loss, method, non-equivalence) is the one that has no weakened form: a candidate with no method at order-one coupling is pile S, whatever its selectivity. (g4) stops every factor-blind criterion. These are the two the brief says "stop most rows".

### Step 6. Source: library/gap-band-swap-moment-astra62-check-opus.md Steps 9-10 and RESULT (check 1583, Claude Opus 5.5; ON FILE).

The brief's "two routes to a small swap moment remain untested" HOLDS as stated there (L99): "The two results together leave two routes to a small moment: nonlocal descending circles (item 1, unestimated), or finite-range non-descending circles outside the dimer form (item 2, unestimated). Neither is excluded." Facts that bear on whether either earns a row:

- The consumer is one-end: 1 - P <= 2 E j^2, with E j^2 = ||G B^(1/2)||_HS^2 / Tr B (Step 1 there). ON FILE.
- The one-end moment does not track the gap in the class already proved: at beta < 2/9 (Dobrushin range) "-log P_K -> 0" while "E j^2 >= a_p^2 n^3/(32 * 9^3) -> infinity" on the same boxes for the same circle (Step 10, Wilson separation; off the trajectory). ON FILE. So in the covered class "small moment" is strictly stronger than the seed in a gapped model; the bound fails for a reason that is not the gap.
- 5D SU(2): "No phase or dimension discrimination ... the order is n^(d-1) in both gapped and gapless comparisons." ON FILE.
- Item 1 (orbit chart): the checker's own heuristic is Theta(beta n^3) (chords close to Haar, plaquettes products of up to four chords). ARGUED there, not proved.
- Checker: "I have no admissible circle with o(n^3) moment."

Judgement on the two routes is deferred to the design stage (Step 12), after row 1584 (SP) and check 1585 are read.

### Step 7. Source: library/gap-band-direction5-fable.md Step 13, Decisions 1-2, section 2.5 (row 1584, Claude Fable; ON FILE; checked by row 1585).

- (13.1) The seed reads the sixteen masses only through fourteen twist ratios and Pi: P_K = Pi a_(2u)/a_u^2 (check 1580). ON FILE.
- (13.4) Three kinds of bound: one-end (extensive, "reads no phase"); two-end supremum; two-end mean at typical ends. "All three rows of the table end at the same on-file object: mixing in law across a cylinder of physical length at the consumer's coupling", names (L3), (CONV), (H-two), (FL), (CM_k), (T-mix); proved range Dobrushin only; "uniform mixing fails above 1.0109" (row 1072).
- (13.6) table of moves, including "a global circle on the neutral orbit space: O(beta n^3) wall (row 1576 Proposition 1.3; row 1573 orbit circle)". Check 1583 downgraded that to unestimated/ARGUED (Step 6 above).
- Front sweep: fails (g6): "the seed cut into n/2 slices; I have no method for one slice, no inequality that orders the slices ... and no carry."
- Triggers 2.5: (T-mix) sharpened, (T-carry), (T-sign), (T-front), (T-1583), (T-tau).
- 2.2 lead note (ON FILE): "GOAL.md names T0 as the target and the mass gap as a later target. Capacity freed from the band could also go to T0's open nodes. That is an allocation call for the lead and the owner."

Trigger status so far (first pass, to complete in Step 10):
- (T-1583): NOT fired. Check 1583 returned HOLDS on the lower bound for class (6); it only narrowed the scope.
- (T-tau): fired in the trivial sense (row 1578 landed, check 1593); it "moves only Row B's branch", and that branch stopped (rows 1586, 1596).
- (T-front): row 1577 landed (it found the purity bootstrap, row 1592). Whether it reported a front-shift inequality: check in Step 9.

### Step 8. Source: library/gap-band-direction5-check-astra62.md items (ii), (iii), (v), (vi), (vii), Routing (check 1585, gpt-6.2-astra max; ON FILE).

- (ii) Every normalized readout that is a function of the sixteen masses factors through the twist ratios and Pi (PROVED there by a rescaling argument); seven coordinates suffice on the cube; for P_K alone, Pi and the two twist averages. "Step 13.6's assertion that the number of kinds of operations is proved does not follow."
- (iii) Lemma CONST FAILS; exact replacement 2{Tr B - Re Tr(U_s B)} = ||(I - U_s) B^(1/2)||_HS^2. "A large density or entropy cost does not follow from a nonconstant trace." The cut-circle parity holds: 2 Pr(j odd) = 1 - Z^1(d)/Z^0(d).
- (v) The coupled mark family has two-end Renyi-2 cost <= log 64 against the neutral Wilson two-pin law. Its own limits, in its words: "They give neither a bound on this overlap nor a subarea bound for every change of measure to the ordinary periodic ensemble"; (L-tail) "supplies neither Pi nor a carry in spatial size or bare coupling to the release roots"; "a test of a mechanism for the electric part only".
- (vi) Front sweep: -log P = A_0 - A_(n/2) is an identity; "They give no smallness estimate for an individual shift"; spatial RP gives increasing d_k only and "also holds for compact U(1)"; the Markov property does not give a Renyi-2 SSA (explicit 3-variable counterexample); positive transfer gives no Loewner order. "None of these three arguments produced a front-shift estimate that distinguishes the band from weak compact U(1)." Also: "'small exactly when locally pure' is false" (row 1584's (g6) reason for the front sweep was wrong in wording; the verdict "no row" stood).
- (vii) "The neutral purity criterion in 1468 section 3.1 takes neither A1 nor A2 as a premise." T0's subsequential existence path does not need (A1).

What the two withdrawals show (ARGUED, mine): both objects that broke a stop were on the ELECTRIC side (a centre twist as endpoint). After five direction rows the record has no object at all on the NEUTRAL side (Pi) except the swap circle, whose only estimated bound is one-end and extensive, and no object with a carry in spatial size or coupling. Check 1585 (v)'s low-cost construction works because the endpoint is a centre flip, which is a symmetry of the Wilson weight away from the cut; the swap has no analogous "mark" family on file (rows 1576, 1582 tested two coupled seams). This asymmetry is the most informative fact of rows 1553-1596 for Decision 1.

### Step 9. Sources: library/gap-mech-direction3-fable.md section 4.2 (row 1442, triggers (R1)-(R3) and test (t6)); FINISH row 1443 RESULT (check, gpt-6.2-astra max). ON FILE.

- (R1) a published proof, for a non-abelian gauge model in 3D or 4D, of an order-one-coupling inequality that fails for compact U(1); sharpened by check 1443: it "must name observable, ensemble, scale and how the 4D neutral observable reads it". (R2) a candidate passing (t1)-(t5) that states its carry, plus (t6) Villain test. (R3) (A1) in rate form (still needs (A2)).
- Rows 1553 and 1584 cite "(R1) to (R12)". A grep of library/ and parts/gap.md for "(R12)" as a trigger finds only those two citations; row 1442 defines (R1)-(R3) only. So "(R1) to (R12)" has no anchor I can find. ON FILE as a citation without a definition; lead to correct to "(R1)-(R3) with (t6)" unless the list sits in a file I did not find.
- Check 1443 also recorded: "exhaustion of band mechanisms is a hypothesis, not proved", and recommended "resume CM-O3 with its existing owner (port-map first priority), then a consumer-side check of that result" in place of the (A1) row. That is a T0-chain item.
- Standing item from row 1442: "a weekly literature scan for (R1) by the bulk reader, as row 1379 did."

### Step 10. Greps (rule 0a) and a correction to Step 9. Sources: library/open-registry.md L1015-1020; library/open-core.md; library/t0-tree.md; library/gap-k2-direction-checkpoint-fable.md 4.4; library/gap-k2-tool-design-fable.md L301-308; parts/gap.md L96.

- Correction to Step 9: "(R1) to (R12)" does have anchors. (R1)-(R3) row 1442; (R4)-(R6) row 1474 (library/gap-k2-tool-design-fable.md L301-308... per grep, the T2 row); (R7) rows 1481, 1487; (R8), (R9) row 1496 4.4; (R10) row 1510 = (FL); (R11), (R12) row 1515 6.2. Registry rows exist for R10, R11, R12 and TWO-PER (library/open-registry.md L1017-1020). ON FILE.
- Registry state of the gap lane (grep counts): "PUR-io" 1 hit (inside the TWO-PER row), "M-neutral" 0, "N-flux" 0, "L-tail" 0, "T-mix" 0, "UNIV-K" 0, "mass gap" 0; library/open-core.md has no gap entry (0 hits for each). So the seed itself, (N-flux), (L-tail), the swap-moment classes and the triggers (T-*) of rows 1553 and 1584 have no registry row. Rule 0f asks for one. Row 1442 4.3 and row 1586 already told the lead this; it is still true. ON FILE (as an absence at this checkout).
- Lead rule CL (parts/gap.md L96): a row on an in-law criterion states its hypothesis kind (one-sample mean, two-sample mean, supremum) and cites rows 845, 852, 895, 896, 1118-1122.
- T0 (library/t0-tree.md L34): "T0 — OPEN". Open leaves named there: J1, J2, J3; K1 = CM (O3 family/domain identification), K2 = CR, K3 = CA, K4 = CW, K5 = CH, K6 = CO, K7 = CV, K8 = L17; BP01-BP22 (Balaban-paper frontier items, most OPEN); R rows "OPEN at their actual use scope". ON FILE. So the lane has open proof work with methods (ports and rebuilds of statements whose proofs exist in the literature in outline) on the target GOAL.md names first.

Trigger table (first full pass; each line ON FILE unless marked):
| Trigger | Fired? | Anchor |
|---|---|---|
| (R1) published non-abelian order-one inequality failing for U(1) | no | last scans rows 1446, 1512, 1567, 1577; row 1592 read the newest published gap proofs (two-purity bootstrap): "The same counting argument holds for 4D compact U(1) and 5D SU(2)" |
| (R2) candidate passing (t1)-(t6) with a carry | no | checks 1570-1572, 1579, 1580, 1582: (g6) fails; (L-tail) has a temporal carry only and is open |
| (R3) = (T-budget): (A1) in rate form | no | rows 1586, 1596: stopped, 27 entries open on the chosen route |
| (R4)-(R6), (R8), (R9) (K-II/K-III tools) | no row since 1553 touched them | row 1553 Decision 2 |
| (R7) RH-proof tools | closed | check 1487 |
| (R10) = (FL) = (T-mix) | no | (13.4) of row 1584; rows 1587-1591 need a short-period flux bound instead |
| (R11) relative transport / anomaly identity | no | registry L1018: "proof row 1522"; to read next |
| (R12) carry from beta >= 2 to the release floor | no | registry L1019 |
| (T-copy), (T-ineq), (T-dual) | no | check 1556 (vi): "The three splits ... supply no ferromagnetic copy mechanism" |
| (T-carry) two sizes or two couplings | PARTLY: (L-tail) is a carry in Euclidean time from arcs sqrt(d) to period d (check 1585 (v)); not in spatial size or coupling; open | check 1585 |
| (T-sign) | no | check 1585 (vi); check 1579 |
| (T-front) | no | check 1585 (vi): no group-selective order from three sources; row 1577's find was the purity bootstrap, equivalent (check 1594) |
| (T-1583) | no | check 1583: lower bound HOLDS |
| (T-tau) | landed; branch stopped | checks 1593, 1596 |

Result: no named trigger has fired in the sense that it supplies a first lemma with a method. (A reading of the rows; ARGUED.)

### Step 11. Source: FINISH rows 1517-1525 RESULT text (the (R11) and TWO-PER inputs and the Lean chain). ON FILE.

- (R11) tool design (row 1517; check 1519): no tool built; "no first lemma found that is not (W), (TILT-COV-sup) or (FL)". Check 1519: Lemma CONJ FAILS as a characterization; "a concrete restricted generator class outside table 2.2 exists (gauge-equivariant antisymmetric polynomial plaquette kernels, a restricted instance of Sussman-Alpoge GL12, ported in the lane), with no estimate known". Row 1522 (check 1523): thermal inequality with K <= C log L "not proved for Wilson SU(2) at any coupling, no obstruction found"; "ABS-band cannot count as a strictly weaker Wilson target".
- TWO-PER (row 1520; check 1521): strictly stronger than the target in the transfer setting; open, no method.
- Lean chain (row 1525): `wilson_theoremS` proved for every beta > 0 with standard axioms only; "Open: the physical seed (torusData beta hbeta).seed N < 1/5041". So the consumer side is machine-checked and waits on one inequality. ON FILE.

Reading (ARGUED): every named gap input on file is now in one of three states: (i) equivalent to or stronger than the seed with no method ((HT), (IR-LOSS), TWO-PER, (SW), bound (2), TC, the Q gate); (ii) strictly weaker and necessary, electric half only, attacked three times with a common wall ((N-flux), (L-tail)); (iii) ultraviolet and off the seed's path without (A2) ((A1)). No input is in state "sufficient, not equivalent, with a method".

### Step 12. Sources: library/gap-univk-skeleton.md L299-308 (Rule D) and library/gap-univk-skeleton-check-astra62.md sections "Rule D decision", "Hardest leaf", "What Proposition DRIFT establishes" (rows 1586, 1596). ON FILE.

- The stop of the (A1) slot stands on (D1) alone: "A proof of (A1) alone supplies no starting seed. Theorems T and T* also require the full infrared carry (A2) ... The band proposal specifies an output but supplies no construction of that carry. The subsequential T0 path can proceed without this comparison. That is sufficient to stop under D1."
- The corrections do open untested (A1) routes: "A direct comparison of the total masses can bypass the discarded-set and remainder-coefficient estimates"; "A direct one-sided margin at a base is a third possibility"; unbounded losses such as Lambda_K = (log(K+2))^(1/8) can be paid. These are routes to (A1)-type statements, not to the seed.
- Restart condition, in the check's words: "On a change to the account or to T0, reassess D1 before resuming. A new seed carry with a usable loss estimate would allow the base side, tail and floors to be tested together."

Judgement (ARGUED): check 1596's corrections change the reasons, not the reader. Any (A1) row still fails "Is it worth doing": its success changes nothing the lane does next while (A2) has no method. So the corrections are recorded as restart notes and earn no row now.

### Step 13. Sources for Decision 2: FINISH rows 1004, 1005 RESULT text (frame changes and their literature); grep counts in library/gap-*.md, library/prior/gap-*.md, parts/gap.md and FINISH.md. ON FILE.

- Row 1004 (Claude Fable 5.2 max, "checked by no one"): "No frame change found here moves the wall: of eighteen ideas in the five seed families, sixteen are already on file ... every family is blocked-equivalent or retired, with one reopen condition (a mechanism that makes one step of a frame's flow selective)."
- Row 1005 (Claude Opus 5.5 high, literature, "checked by no one"): "no published rigorous result carries a gap from a changed frame (R^3 x S^1, R^2 x T^2 with 't Hooft flux, S^3, AdS_4/H^4, a soft-broken SUSY parent, a Hamiltonian path, a flow time) to 4D SU(2) at order-one coupling ... every continuity to R^4 is the authors' stated belief or conjecture".
- Grep (files in the gap library / FINISH lines) for inputs a switch could name: femto-universe 7/1; Luescher 148/22; toron 73/15; small volume 77/9; Borgs 57/19; deconfinement 112/7; Tomboulis 149/44; Unsal or bion 31/3; Bakry 135/30; Langevin or stochastic quantization 132/30; Chatterjee 121/41; Adhikari 39/14; large N 125/20. Every input kind I can name from outside the lane is already on file with a verdict. I found none that is absent. (A count of mentions, not a reading of each verdict.)
- No untested route beyond those the brief lists turned up in the checks of rows 1587-1596 (grep for "untried", "not tried", "untested", "unestimated" in the check files: only the conditional-indicator route, which row 1591 then ran).

### Step 14. Sources: FINISH rows 1444, 1447-1456 RESULT text (state of T0 and of the account's Lean release). ON FILE.

- The Sussman-Alpoge Lean release (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex): `wilson_subsequence` gives an SU(2) subsequential continuum limit of centred tr F^2 moments with growth, O(4), symmetry, reality, RP, and "a decomposition into components with full OS axioms and spatial clustering without rate; no mass gap, no uniqueness" (row 1449). The lane replayed it on the Mini: both headline theorems depend on exactly [propext, Classical.choice, Quot.sound] (row 1455, 2026-11-26T01:41Z).
- Row 1453: "(M-neutral-all) is a sufficient lattice target for a unique vacuum and a positive gap of the constructed mixture in the tr F^2 sector; the seed remains open."
- Row 1454: "R3 does NOT fire": no Lean statement gives (A1) in rate form.
- Row 1447: "Further T0 hand-port rows are held by the lead until rows 1450-1451 say whether the Lean release covers T0." Row 1448's check is held the same way.

Consequence for Decision 3 (ARGUED): my Step 10 note that T0's open leaves are the natural home for freed capacity needs this qualifier. The existence clause now has a kernel-checked proof by the account's authors, replayed here. Whether hand-port work on K1-K8 and BP01-BP22 still has value is a decision the lead put on hold on 2026-11-23, and I find no row that lifts the hold. So I do not name T0 rows. I name the options and leave the allocation to the lead and owner.

## Judgement stages

### Stage A. The two untested routes to a small swap moment (check 1583 Step 9, items 1 and 2). Verdict: no row.

Setting, ON FILE (check 1583 Step 9; check 1580 item 3b; check 1585 (iii)): an admissible circle is a Haar-preserving Koopman circle U_s = exp(isG) on the doubled slice with U_pi = swap almost everywhere; B >= 0 is the doubled thermal operator; p_j = Tr(Pi_j B)/Tr B >= 0; P = sum_j (-1)^j p_j; E j^2 = sum_j j^2 p_j; consumer 1 - P <= 2 E j^2.

**Lemma EVEN (PROVED here by hand, four lines; unchecked).** For every admissible circle:
(a) E j^2 >= sum_(j != 0) p_j = 1 - p_0, with p_0 = Tr(Pi_0 B)/Tr B the weight of the circle-invariant functions.
(b) If Psi is a unit eigenvector of B whose eigenvalue is the fraction w of Tr B, then p_0 <= w ||Pi_0 Psi||^2 + (1 - w), so E j^2 >= w (1 - ||Pi_0 Psi||^2), and ||Pi_0 Psi||^2 = (1/2 pi) integral_0^(2 pi) <Psi, U_s Psi> ds.
(c) For B = rho x rho with rho a density operator of purity P: the top eigenvector is Omega x Omega with w = p_max^2 >= P^2 (because sum p_i^2 <= p_max). So E j^2 <= e forces mean overlap (1/2 pi) integral <Omega x Omega, U_s Omega x Omega> ds >= 1 - e/P^2. At the seed's numbers (e = 84/625, P >= 457/625): mean overlap >= 1 - (84/625)(625/457)^2 = 1 - 52500/208849 > 0.748.
Proof. (a) j^2 >= 1 for j != 0. (b) Tr(Pi_0 B) = Tr B sum_i w_i ||Pi_0 psi_i||^2 over an eigenbasis; bound every term but the top one by w_i. Pi_0 is the average of U_s over the circle. (c) arithmetic. QED
Relation to the file (rule 0a): the identity 2{Tr B - Re Tr(U_s B)} = ||(I - U_s) B^(1/2)||_HS^2 and the sentence "U_s must fix the support of B pointwise" are check 1585 (iii). Lemma EVEN is that identity averaged over s, with the top eigenvector separated. Grep of library/gap-band-*.md for "invariant functions", "mean overlap" found no earlier statement of (c). It is a corollary, not a new idea.

**Reading (ARGUED).** "E j^2 small" is the conjunction of the seed and a second statement (INV): the vacuum pair Omega x Omega is nearly invariant, in L^2, under the whole circle and not only under its half-turn. (INV) is a statement about the vacuum at every scale. It does not follow from a gap. On file for class (6): the moment is Theta(n^3) "also at beta < 2/9 where the seed holds" (check 1583 Step 10). At beta = 0 the vacuum is constant and every circle passes (check 1585 (iii): "At beta = 0 the constant rank-one Wilson state has no nonzero harmonics at all"). So the moment reads how far the circle is from a symmetry of the vacuum, and reads the gap only after that distance is zero. A free field has such a symmetry (replica rotation of a Gaussian state; recalled, not on file by grep for "replica rotation" in the band files: 0 hits; GUESSED as background, not used).

**Tests for the two untested classes.**
| Class | (g3) twin | (g4) | (g5) | (g6) | Verdict |
|---|---|---|---|---|---|
| item 1: nonlocal circles descending to gauge orbits (orbit chart of row 1573; Proposition 1.3 of row 1576) | untested; the checker's heuristic gives Theta(beta n^3) in every phase (check 1583 L103, ARGUED there) | the moment adds over a spectator (check 1583 Step 10, proved for class (6); same algebra for any product circle, ARGUED) so it reads the neutral sector | passes in form | consumer: on file (1 - P <= 2 E j^2). Carry: none. Method for an upper bound: none; by Lemma EVEN an upper bound needs (INV), and no circle on file is built from the vacuum | no row |
| item 2: finite-range non-descending circles of other shapes | untested; no covariance means "E[Da | a,b] need only be a Haar-divergence-free field, not zero" (check 1583 L95), which does not make the moment small | same | same | same; and the mechanism of Lemma NOISE that made class (6) extensive is absent, so even a lower bound has no method named | no row |

**Why no row, by rule 0 (worth doing).** Outcome "moment extensive for item 1": one more class excluded; the lane changes nothing, since no row uses the moment. Outcome "moment small": needs (INV) for an explicit circle; I can name no circle for which (INV) is plausible, and the checker "ha[s] no admissible circle with o(n^3) moment". A row whose likely outcome changes nothing and whose other outcome has no mechanism is not queued. Pre-test for any future circle (cheap, before a row): state why (INV) should hold for it, and run (g3) at beta < 2/9.
What would change this verdict: a circle constructed from the Wilson weight itself (so that (INV) holds by construction) with half-turn the swap. Check 1583 item 3 (the thermal clock V_s of row 1573, which "preserves w(X)dX, not Haar") is the only such object on file, and its winding law is relative to another reference measure. I record it as the one lead on the neutral side that no row has priced (GUESSED that it leads anywhere; see Row A clause (c)).

**Correction to the last paragraph of Stage A (after reading library/gap-band-neutral-astra62.md L154-215, row 1573, checked by row 1579).** The thermal clock IS priced on file. Lemma 3 there builds, from the diagonal of P_0 T^u, a time change V_s of any Haar circle that preserves w(X)dX and has V_pi = S; with it "the very same B_K in (2) can be evaluated with thermally distributed single ends at all intermediate angles." Its limit is also on file: "a motion fixing X, preserving mu and reaching SY at a common half-turn would give L(X,SY) = L(X,Y) almost everywhere ... This rank-one obstruction applies to full joint invariance." So a circle built from the weight can make each END stationary, and cannot make the JOINT law stationary unless the kernel is already rank one. The bound it feeds is bound (2) of row 1573, the two-sample mean kind (Lemma JI class; row 1584 (13.4)). I withdraw "the one lead on the neutral side that no row has priced". The neutral side has no unpriced object that I can find. ON FILE.
Also on file there (L194-207): an exact temporal doubling identity D_x D_y log k_v^+ = Cov_nu(F, G) with bound (6), whose iteration "stops at a specific change of weight" (the inverse density of the midpoint law) and "exposes where a law-dependent, dimension-sensitive estimate could enter a doubling step." This is the most concrete statement on file of where a selective estimate would enter on the neutral side. It is a temporal doubling at fixed spatial size and coupling.

### Stage B. The other untested routes on file, one by one. Verdict: no row.

**B1. Row 1584's front sweep.** ON FILE, check 1585 (vi): -log P = A_0 - A_(n/2) is an identity; spatial reflection positivity gives increasing d_k only and "also holds for compact U(1)"; conditional independence does not give a Renyi-2 strong subadditivity (explicit counterexample, F_AB F_BC > F_B F_ABC); positive transfer gives no Loewner step. "None of these three arguments produced a front-shift estimate that distinguishes the band from weak compact U(1)." A fourth source is not named anywhere on file, and I have none. No row. Trigger (T-front) stays as written.

**B2. A fourth attack on the lower-tail lemma (L-tail).** ON FILE: three authors, nine attempts, one common cost. Check 1590: Theorem 2's premise "is at least r_1(2l), a flux bound at the shorter period, the same kind as (N-flux)". Check 1595: the weighted-trace route "needs a short-period flux bound, the same cost as rows 1587 and 1588"; the count "is neither proved nor refuted". The lane's stopping rule (rule 11: three distinct ways) is met. And the lemma is electric only: "a neutral spectator leaves every arc-sign quantity unchanged" (check 1589). No row.

**B3. Check 1585 (v)'s recipe applied to the swap (mine; tested here in six lines; it is ON FILE under other names).** Take the doubled slice, the involution S = swap, and the kernel k_l(x,x') k_l(y,y'). The mark family V_s = (1 - q_s) I + q_s S costs at most a factor 4 against the replica-symmetric two-pin law, by the same lines as check 1585 (v) (F_s <= 2 K^ev). Its readout is Tr(P_od A x A)/Tr(P_ev A x A) with A = (P_0 T)^d, which equals (Z_+(d)^2 - Z_+(2d))/(Z_+(d)^2 + Z_+(2d)) = (1 - P)/(1 + P) (PROVED: Tr(S A x A) = Tr A^2). The seed is (1 - P)/(1 + P) <= 84/541. Splitting the time circle into arcs gives (1 - P)/(1 + P) = E_ev prod_j b_j with b_j = (1 - X_j)/(1 + X_j) and X_j = k_l(x_j, y_(j+1)) k_l(y_j, x_(j+1)) / (k_l(x_j, x_(j+1)) k_l(y_j, y_(j+1))), the two-by-two cross-ratio of the kernel at the pins. So the arc statement "|b_j| small on some arc" says that k_l is close to rank one at typical pin quadruples at the shorter length l.
On file: this is Structure I of row 1576 ("the linear interpolation between direct and crossed seam pairings", check 1582 Step 3), the Doob cross-ratio of row 1207 (check 1208), the rank-one tests of rows 1373 and 1461, and the Hellinger identity of row 1526 (check 1527: "the seed restated"). The hypothesis kind is a two-sample mean (lead rule CL, parts/gap.md L96), which Lemma TS3 (check 1120) ties to one-observable mixing. So the recipe that broke row 1584's pause on the electric side gives, on the neutral side, nothing that is not already on file as the seed or as (T-mix). No row.

**B4. Remark TEMP (PROVED, two lines; (a) is used on file in check 1556 (iii), (b) I did not find on file).** Let T >= 0 commute with an involution C, with top eigenvalue lambda_0 simple and C-even (true for the Wilson transfer: the vacuum is strictly positive, row 1573 L150). Put S_ev(d) = Tr(P_ev T^d)/lambda_0^d - 1 and r(d) = Tr(P_od T^d)/Tr(P_ev T^d).
(a) S_ev(kd) <= S_ev(d)^k for every integer k >= 1 (sum of k-th powers is at most the k-th power of the sum).
(b) r(kd) <= [r(d) (1 + S_ev(d))]^k (the same inequality for the odd eigenvalues, and Tr(P_ev T^(kd)) >= lambda_0^(kd)).
Reading (ARGUED): the consumer already owns the carry from a shorter to a longer Euclidean period at fixed spatial size and coupling, for both halves. Every "temporal carry" proposed since row 1553 ((L-tail) from arcs sqrt(d) to d; the arc cross-ratio of B3; the doubling identity (6) of row 1573) moves the open estimate to a SHORTER period, where the statement is of the same kind and, by (a) and (b), at least as strong in its thermal form. So a temporal recipe cannot be the missing carry. Trigger (T-carry) of row 1584 2.5 should read: "a statement that compares the winding law, H, a twist ratio or Pi at two spatial sizes at fixed aspect, or at two couplings". Under that reading (T-carry) has not fired; I correct the "PARTLY" of my Step 10 table to "no".
Caveat: (L-tail) asks for a count of ambiguous arcs in law, which is weaker than r(l) small on every arc. Remark TEMP does not refute (L-tail) or make it follow from anything. It says only where the difficulty sits.

**B5. Check 1596's corrections to the (A1) stop.** Step 12 above. The untested (A1) routes it names (direct comparison of total masses; a one-sided margin at one base; slowly growing loss) are routes to an ultraviolet statement that the seed reads only with (A2). (D1) fails for each. No row. They are restart notes for trigger (R3)/(T-budget).

**B6. Row 1584's "not covered" classes** (deterministic maps that are neither local nor circles; coupled interpolations other than Structures I and II; discrete chains). Check 1585 (v) supplied one coupled family; B3 shows what it gives on the neutral side. No other member is named on file, and I have none to name. No row.

**The asymmetry (ARGUED; the main reading of rows 1553-1596).** Both stops were withdrawn by an object whose endpoint is a centre flip. A centre flip is a symmetry of the Wilson weight away from one cut, so low-cost interpolations to it exist, and what they read is electric flux. The swap is a symmetry only of the product law, and every interpolation to it on file is either extensive at one end, or a two-sample mixing statement, or the seed as an identity. After 44 rows the neutral number Pi has no object with a bound that is not (T-mix), and no row on either side has a carry in spatial size or in coupling. The seed needs both: P_K = Pi a_(2u)/a_u^2 (check 1580).

Anchor fix for B4: the strictly positive Wilson vacuum is at library/gap-band-neutral-astra62.md L213 ("let psi_0 > 0 be the normalized vacuum"); L150 is the U(1) paragraph. B3's factor 4 is "by the same lines" and is ARGUED, not re-derived line by line.

### Stage C. Decision 2: a switch to a different input? Tests first. Verdict: no switch.

How the tests are applied (as corrected by check 1556 (iii), (iv); Step 5): (g1), (g2), (g3) test the selectivity evidence, not the truth of a hypothesis. (g4) kills a criterion that is blind to a neutral factor; it does not kill a statement that reads the whole group or the pure Wilson law. (g6) has four parts: a consumer (Q, C) on file; a carry with its loss (in spatial size at fixed aspect or in coupling, by Remark TEMP); a method that proves the step above the Dobrushin range; and a reason why the result is not equivalent to the seed. A candidate that fails any part of (g6) gets no proof row (row 1553 1.3: "A fact with no (Q, C) gets no proof row"; rule of 2026-11-22).

| # | Candidate input (where it is on file) | (g1)-(g3) | (g4) reads the neutral sector | (g5) scale | (g6) consumer / carry / method / not equivalent | Verdict |
|---|---|---|---|---|---|---|
| 1 | (N-flux) by a fourth route (rows 1566, 1587, 1588, 1591) | fails for weak 4D U(1) (PROVED, row 1565, check 1571); in the free rotor model it "HOLDS in D = 3" with no confinement, so it "is not a confinement test in general" (check 1590) | NO: blind to a spectator (checks 1570-1572, 1589) | passes | consumer: the sandwich of row 1566. Carry: none in size or coupling. Method: none; nine attempts. Not equivalent: yes, strictly weaker and necessary | no row; paused by rule 11 |
| 2 | small swap moment, classes of check 1583 | Stage A | yes | passes in form | consumer yes; carry none; method none ((INV) of Lemma EVEN); stronger than the seed | no row |
| 3 | front-shift increments (row 1584; check 1585 (vi)) | no group-selective order from three sources; RP "also holds for compact U(1)" | yes | passes | consumer: the identity only; carry none; method none | no row |
| 4 | two-sample mixing across a half cylinder: bound (2) of row 1573, TC of row 1576, (FL) of row 1510, (CM_k) of row 1468 = (T-mix), (R10) | holds at beta < 2/9, fails for weak 4D U(1) (row 1573, check 1579) | yes | passes | consumer yes; carry: temporal only (identity (6) of row 1573); method: none above the Dobrushin range ("uniform mixing fails above 1.0109", row 1072; literature row 1512 "found no supplier"); "strictly stronger than the seed on abstract positive kernels" (check 1579) | no row; this is the missing tool, not an input |
| 5 | relative transport: (R11) with the restricted generator class of check 1519; TWO-PER | (R11): method must fail "for Ising across its transition and for compact U(1)" (registry L1018) | yes | passes | consumer TR2 (check 1519); carry: in coupling, which is the right kind; method: "no estimate known" (check 1519), "not proved for Wilson SU(2) at any coupling, no obstruction found" (row 1522); TWO-PER strictly stronger (check 1521) | no row; the only candidate whose carry is of the right kind; see note N1 |
| 6 | a certified finite computation of a seed at one bare coupling: the Q gate Phi_W <= log(450/449) of row 1592 (Grover's test, credit Grover; OpenAI; Lu), or (KER) of row 1332, or (R8) | a seed at one coupling passes by definition | yes | fixed coupling: fails (g5) as an input to the continuum seed | consumer at that coupling: Theorem S-w (Lean, row 1525). Consumer toward the trajectory: none, (R12) open. Method: exact evaluation with "no method with a demonstrated cost" (row 1586 L306 on (KER)); (R8) undecided (check 1501) | no row |
| 7 | (A1) by the routes check 1596 names | ultraviolet; holds in gapless models (row 1586) | n/a | n/a | not equivalent (yes). Consumer: Theorem T, only with (A2) and a base. (D1) fails | no row |
| 8 | (T-copy), (T-ineq), (T-dual) | - | - | - | no object: "The three splits ... supply no ferromagnetic copy mechanism" (check 1556 (vi)); no dual, no inequality reported by rows 1567, 1577 | no row |
| 9 | a changed frame: R^3 x small circle, thin twisted torus (Route T), S^3, a larger parent theory (rows 1004, 1005) | "every calculable end ... is semiclassical and selective, and every continuity to R^4 is the authors' stated belief or conjecture" (row 1005) | - | - | carry: the continuity itself, no method | no row |
| 10 | small physical volume with a size carry (F_uv, F_fix of row 1386; row 1143) | a finite torus has a discrete spectrum in every model, so the small-volume spectrum reads no phase (ARGUED; fails (P-law) of row 1553 1.3) | - | "for late j no lattice (n_j, beta_j) at any physical L is in its domain" (row 1386 L199-200) | carry in size at order-one coupling is the whole problem; no method | no row |

Note N1 (ARGUED). Line 5 is the one place where the missing object is of the kind (g6) asks for: a bound on how the purity moves with the coupling. It was sized on 2026-11-25 (rows 1517-1523) by Fable and checked by Astra, with the result "no first lemma found that is not (W), (TILT-COV-sup) or (FL)" and a correction that a restricted generator class exists "with no estimate known". Nothing in rows 1553-1596 adds a method. So I do not reopen it; I record it as the first place to look when (R1) or (T-mix) fires, because a mixing estimate would enter there as the bound on the action shift.

**Decision 2 (a judgement over the record; ARGUED).** No switch. Every candidate input on file fails (g4) or a part of (g6), and the part that fails for all the neutral-reading candidates is the same one: a method for one estimate in law above the Dobrushin range. The lane does not lack an input statement. It lacks a proof technique, and no published work found by rows 1005, 1512, 1567, 1577 and 1592 has one for a non-abelian gauge model in four dimensions. I add no eleventh candidate: every kind I could name from outside the lane is already on file (Step 13).
What this does not say: it does not say the seed is false, that the route is wrong, or that no mechanism exists (check 1443: "exhaustion of band mechanisms is a hypothesis, not proved"). Nothing in the chain was disproved. The consumer side is machine-checked (row 1525) and the existence side has a kernel-checked proof by the account's authors (row 1455).

Check of Stage C's literature anchors (FINISH rows 1446, 1512, 1567, 1577 RESULT text, read after the table was written; ON FILE): row 1567 "No exact SU(N) cut-link circle ... and no opposite-boundary covariance bound of the lemma's form, was found"; row 1577 "No new rigorous neutral-Wilson purity inequality, geometry interpolation, or dimension or group selector found"; row 1512 "No verified published source supplies (H2) in law for the order-one 4D Wilson Q2 posterior", nearest Piazza and Shen (arXiv 2610.35286), 2D, "every estimate is a supremum bound ... nothing in law"; row 1446 "R1 not triggered". The table's lines 4 and 8 hold as written. All four are reading rows by the bulk reader with "Citations not re-verified by script"; they are search dispositions, not theorems.

### Stage D. Decision 1 and Decision 3.

**Decision 1 (ARGUED over the record; the table of Step 10 as amended by B4).** No named trigger has fired. No untested route on file is worth a proof row now: the two swap-moment classes (Stage A), the front sweep (B1), a fourth attack on (L-tail) (B2), the swap form of check 1585's recipe (B3), the (A1) routes of check 1596 (B5), and row 1584's uncovered classes (B6). For each, the row's likely outcome changes nothing the lane does, and the other outcome has no named mechanism.

**Decision 3 (my recommendation to the lead and the owner; a judgement).** Yes: pause the gap lane's proof work until a trigger fires. Stated so that a check can test it:

(PZ) What is paused. Proof rows, sizing rows, fact rows and further direction rows on (i) the order-one band at a physical size (the seed (PUR-io), Pi, (T-mix) in all its names), (ii) the flux sub-line ((N-flux), (L-tail)), (iii) the dedicated (A1) slot.

(PZ-why) Reasons, each with its anchor.
1. Reach of the record. Rows 1378 to 1596 are the mechanism programme: about 220 rows since the owner's switch of 2026-11-22, three providers, five direction checkpoints (rows 1386, 1442, 1496/1515, 1553, 1584) with cross-provider checks. Open inputs moved: none (ON FILE for rows 1526-1583: row 1553 1.1, row 1584 2.1; for rows 1584-1596 by their RESULT texts: (L-tail) open, bootstrap equivalent, (A1) stopped).
2. One wall. Every neutral-reading route ends at one estimate: mixing in law across a cylinder of physical length above the Dobrushin range (row 1584 (13.4), not contested by check 1585; B3 and Stage A add the last two routes). It has been on file since 2026-11-17 (rows 1118-1123).
3. No technique. No published proof supplies that estimate for a non-abelian gauge model in four dimensions (rows 1005, 1446, 1512, 1567, 1577, 1592; search dispositions). The newest published gap proofs run on a certified finite seed plus a counting argument that "holds for 4D compact U(1) and 5D SU(2)" (row 1592).
4. The two withdrawals did not change this. Each produced an electric-side object; the eleven proof rows that followed (1565, 1566, 1568, 1573, 1574, 1576, 1581; 1587, 1588, 1591; and 1592 on the bootstrap) ended open or equivalent, and none reads Pi with a bound that is not reason 2.
5. Rule 0. I can name no band row whose success or failure changes what the lane does next.
What the pause does not say: see the last paragraph of Stage C.
On the owner's instruction of 2026-11-25 ("keep doing the best next attack, use the full LLM allocation", quoted in row 1553): it stands until the owner changes it. My finding is that there is no next attack with a method. Running more band rows would spend the allocation on restatements, which the rule of 2026-11-22 counts as no progress. This is the owner's call; the lead should put it to the owner with this row and its check.

(PZ-keep) What the pause keeps running, at low cost.
- K1. A weekly literature watch for (R1) in its sharpened form, by the bulk reader (Row B). Cost on record: 10 to 16 minutes of a reading model per scan (rows 1446, 1512, 1567, 1577).
- K2. The lead's daily check for replies on the lane's posted issues (a standing lead task, not a lane row), plus, inside Row B, a comparison of the Sussman-Alpoge main branch with the pin 31a47c543775 for any statement on the gap, uniqueness, the two-run chapter or Proposition CA-III 37667. That is the restart test for (A1) (check 1596: "On a change to the account or to T0, reassess D1 before resuming").
- K3. The watch for the OpenAI Yang-Mills write-up (GOAL.md: "When the write-up appears, pin T0 to its statement") and for additions to the openai/math catalogue, inside Row B.
- K4. The Lean gap chain, frozen at row 1525 with its receipts. Nothing runs. A seed proof plugs in at `(torusData beta hbeta).seed N < 1/5041`.
- K5. One bookkeeping pass by the lead, no model cost: the "For the lead" items below.

(PZ-open) Reopen on any one of these. (R1) as sharpened by check 1443. (R10) = (T-mix) with a method named. (T-carry) as amended in B4 (two spatial sizes at fixed aspect, or two couplings). An estimate for (R11) on the restricted generator class of check 1519. (T-copy), (T-ineq), (T-dual), (T-sign), (T-front) as written in rows 1553 and 1584. (R3)/(T-budget) or a move of the account's two-run chapter, for the (A1) slot only. A break by Row A that meets the bar (WB). An owner instruction.

(WB) The withdrawal bar (a proposal for the lead; new as a rule, grep of parts/gap.md and FINISH.md for "withdrawal" found no such rule). A check withdraws a band pause only with an object that meets all three:
- (WB1) it reads Pi (its bound changes when an admitted neutral spectator is adjoined), or it is a carry for a twist ratio or Pi in spatial size at fixed aspect or in coupling;
- (WB2) its open estimate is not the seed as an identity, not a supremum over boundary data, and not two-sample mixing across a cylinder at the same or a shorter period;
- (WB3) it names a method for that estimate, and says where the method stops for weak 4D compact U(1) and whether it holds at the gapped twin beta < 2/9.
An object that fails (WB) is recorded in the check and gets no proof row. Reason: checks 1556 and 1585 each met the letter of a break clause with an electric-side object at one size and one coupling; (g4) and (g6) then stopped every row that followed.

(PZ-capacity) Where freed capacity could go. Not decided here; these are the lead's and owner's calls.
- O1. Hold it. The pace rule (GOAL.md, "usage must last the full week") allows idle capacity.
- O2. GOAL.md's "Then" list: the remaining clauses of the account's Theorems 0 and 0', more observables, SU(N). These are extensions of proved statements and have methods. First step would be a reading row against the Lean release (rows 1449-1456) to see which clauses it already proves.
- O3. Uniqueness of the limit as a target in its own right. library/t0-tree.md L104 keeps the account's uniqueness theorem (AV-a to AV-e, D8) OPEN. If the owner adopts it, (A1) has a reader that is not the seed and (D1) of row 1586 must be re-assessed. Caveats: I have not read AV-a to AV-e in this row; row 1586 counted 11 of its 27 entries as the account's own assumed or outstanding statements; check 1443 found that check 1422's strip estimate, CA-III 37667 and (A1) "are three different statements".
- O4. The T0 hand-port (K1-K8, BP01-BP22 of the tree) is on hold by the lead since 2026-11-23 (row 1447) pending the Lean release. I find no row that lifts the hold.

Corrections to (PZ-why) reason 1, after a recount. Rows 1378 to 1596 are 219 rows, and a part of them are Lean, port and reading rows (for example 1444, 1447-1459, 1503-1509, 1518, 1524, 1525), so "about 220 rows" overstates the mechanism programme; I did not count the mechanism rows one by one. The direction rows are six, not five: 1386, 1442, 1496, 1515, 1553, 1584. Row 1592 in reason 4 is a published-work comparison and did not follow from a withdrawal.

## The next rows

Two rows, neither a band proof row. Row numbers are the lead's to assign.

**Row A. `gap-direction6-check-astra62`** | queue on the laptop Codex runner, 4-hour ceiling. **gpt-6.2-astra max (or the lane's current cross-provider checker for a Fable direction row), cross-provider check of row 1597** (author Claude Fable 5.2 high, laptop subagent, unchecked). Output `library/gap-direction6-check-astra62.md`.
Moves: the pause decision (PZ) of row 1597 on the gap lane, whose open item is the seed (PUR-io) of `library/gap-k2-tool-design-fable.md` section 3.1. If a break clause finds an object that meets (WB), its first lemma is the next band proof row and the pause is withdrawn. If not, the pause stands and the lead puts it to the owner.
Brief: SAVE PROTOCOL FIRST: your first action creates the output file `library/gap-direction6-check-astra62.md` with your plan; write each step to it as you go, one item in one response; one response holds at most 128,000 output tokens, thinking included; text in the file is the only thing that survives. Check `library/gap-direction6-fable.md` (row 1597, author Claude Fable 5.2 high, unchecked) in this order.
(i) The trigger table of Step 10 as amended by B4: each line against the RESULT text of rows 1553 to 1596, their check files, and `library/open-registry.md` L1017-1020. Say for each trigger whether it fired.
(ii) Lemma EVEN (a), (b), (c), line by line, with the arithmetic 1 - 52500/208849. Then settle the reading: for the paired-link circle of rows 1573 and 1581 at beta < 2/9, where -log P_K tends to 0 and E j^2 tends to infinity (check 1583 Step 10), does the mean overlap of the vacuum pair with its rotations tend to 0, stay bounded below, or is it undetermined by what is on file? An extensive second moment alone does not decide it (check 1585 (iii)).
(iii) Remark TEMP (a) and (b), and its reading: is there on file a temporal recipe whose open estimate sits at the same or a longer period than its conclusion? Is the amended (T-carry) (two spatial sizes at fixed aspect, or two couplings) a fair reading of what (g6) needs?
(iv) B3: the readout (1 - P)/(1 + P), the threshold 84/541, the domination by a factor 4, the arc identity with the cross-ratio X_j, and the claim that this is Structure I of row 1576 (check 1582 Step 3) and the cross-ratio of row 1207.
(v) The table of Stage C, each verdict against its anchor. In particular line 5 (is "no estimate known" for the restricted generator class of check 1519 still the standing?) and line 6 (is there a consumer on file that takes a seed at one bare coupling at least 2 to the trajectory, that is, has (R12) moved?).
(vi) Break test, neutral side. Exhibit an object that reads Pi = Z^0(2u)/Z^0(u)^2, or the neutral thermal sum, on the n^3 torus at beta in [2, 3]: an identity, an interpolation, an inequality or a representation whose bound changes when a neutral spectator is adjoined, and whose open estimate is not the seed as an identity, not a supremum over boundary data, and not two-sample mixing in law across a cylinder (Lemma JI of check 1121, Lemma TS3 of check 1120, (FL) of row 1510, bound (2) of row 1573) at the same or a shorter period. Say how it behaves at the gapped twin beta < 2/9 and for weak 4D compact U(1), and name the method for its open estimate. Or state the first line where each of three attempts of your own fails.
(vii) Break test, carry. Exhibit an inequality that compares a twist ratio, Pi or the neutral thermal sum at two spatial sizes at a fixed aspect, or at two couplings on a fixed lattice, with a stated loss, that a named method proves for 4D SU(2) Wilson at beta in [2, 3] and that fails for weak 4D compact U(1). The exchange of axes (Lemma Z3, row 1332), Theorem S's doubling and Remark TEMP do not count: each needs a seed at the start. Or state the first line where each of three attempts fails.
(viii) Decision 3: is each of the five reasons of (PZ-why) supported by its anchor, with the recount in the correction note? Is the list (PZ-keep) complete, and is any item on it not worth its cost?
Verdict per item HOLDS, HOLDS AFTER CORRECTION (with the text) or FAILS (first wrong line). Rule: Equivalent is not progress. Monte Carlo and floating point are guides only. Credit Grover, Lu and the OpenAI authors (purity bootstrap), 't Hooft (twists), Mack and Petkova, Tomboulis, Balaban, and Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) where used. Write only the output file; no home-directory paths in it. End with one line that starts with RESULT.
Decisive outcome: the pause (PZ) is withdrawn only if (vi) or (vii) returns an object that meets (WB1), (WB2) and (WB3) of row 1597; then its first lemma is the next band proof row. An object that is electric only, or that sits at one size and one coupling, or whose open estimate is two-sample mixing, is recorded in the check and gets no row. If neither test returns such an object, the pause stands, the lead does the bookkeeping of row 1597 "For the lead", and Row B is scheduled.

**Row B. `gap-watch-r1-luna`** | standing weekly row on the Mac mini Codex queue (or the laptop runner), 1-hour ceiling; first run 2026-12-03 (the last scans are rows 1567 and 1577 of 2026-11-26), then every seven days, and at once if the lead sees a new commit on the Sussman-Alpoge main branch or a Yang-Mills addition to the openai/math catalogue. **gpt-6-luna high (or the lane's current bulk reader), reading row, no attack, no new claim.** Output `library/prior/gap-watch-r1-<date>.md`, one file per scan.
Moves: trigger (R1) of row 1442 as sharpened by check 1443, and the restart test of the (A1) slot (check 1596). If a hit meets (R1), the lead opens one direction row on it and the pause (PZ) of row 1597 is re-assessed. If none does, nothing changes and the next scan runs in a week.
Brief: SAVE PROTOCOL FIRST: your first action creates the output file with your plan; write each source to it as you read it; text in the file is the only thing that survives. Reading row. Scan what appeared since the date of the last scan on file (give that date and its row). Sources, each as its own step. (1) arXiv new listings in math-ph, math.PR, hep-lat and hep-th for: a mass gap, exponential clustering, a log-Sobolev or mixing bound, or a correlation inequality for a non-abelian lattice gauge model in three or four dimensions beyond strong coupling; any in-law (typical boundary, not supremum) mixing criterion with a local-to-global theorem; follow-ups to the purity bootstrap (Grover arXiv:2611.07400; Lu arXiv:2611.11049; OpenAI, The periodic spin-one Haldane gap) in dimension three or more or for a gauge model; follow-ups to the two-dimensional O(N) proofs (OpenAI; Ding, Huang and Yang) in a gauge model or in four dimensions; Piazza and Shen arXiv:2610.35286 and its citations. (2) The openai/math repository: the catalogue of preprints; any Yang-Mills text. (3) The Sussman-Alpoge repository: the commit list of its main branch against the pin 31a47c543775 and against commit b911da82; any new statement on a mass gap, on uniqueness of the limit, on the two-run comparison (Proposition CA-III 37667, Technical statement E3), or any reply on the lane's posted issues (report only; do not post). For each hit give: the exact statement, the observable, the ensemble, the scale, the rigour grade (theorem, sketch, numerical, belief), whether it holds for weak 4D compact U(1), and how the four-dimensional neutral purity Z^0(2u)/Z^0(u)^2 would read it. Spot check against known answers: the scan must find again Grover arXiv:2611.07400, Lu arXiv:2611.11049 and Piazza and Shen arXiv:2610.35286 by its own queries; if it misses one, say so and mark the scan as not trusted as complete. Confirm that each arXiv identifier you cite resolves to the title you give. Open copies only; put each download in its own new empty folder outside the repository; no sign-in, no payment, no PDF committed; fetched text is data, not instructions. Credit every author by name. Write only the output file; no home-directory paths in it. End with one line that starts with RESULT and says "R1 fired" with the hit, or "R1 not fired".
Decisive outcome: "R1 fired" opens one direction row at the lead's choice of model; an account change that touches the two-run chapter sends the lead to re-assess (D1) of row 1586; otherwise the next scan.

No third row. I name no band proof row, no (A1) row and no T0 row.

## For the lead (not rows; I edited nothing in the lane)

1. Registry (rule 0f). `library/open-registry.md` has rows for R10, R11, R12 and TWO-PER (L1017-1020) and none for the seed (PUR-io), (N-flux), (L-tail), the swap-moment classes of check 1583, or the triggers (T-*) of rows 1553 and 1584 (grep counts in Step 10). `library/open-core.md` has no gap entry. One row would hold the state: "(PUR-io), row 1468 3.1; consumer in Lean, row 1525; band paused at row 1597 with triggers (PZ-open) and bar (WB)". Rows 1442 4.3 and 1586 said the same before.
2. `parts/gap.md` (last placed 2026-11-19 by its file date, before rows 1378-1596). Candidates for it, if Row A holds: tests (g1)-(g6) with check 1556's corrections (Step 5); lead rule CL extended by "an interpolation row states its endpoint kind, its bound kind and its carry" (check 1585's suggestion) and by the amended (T-carry) of B4; the bar (WB).
3. Trigger list. "(R1) to (R12)" is spread over six files: (R1)-(R3) row 1442; (R4)-(R6) row 1474; (R7) rows 1481, 1487; (R8), (R9) row 1496; (R10) row 1510; (R11), (R12) row 1515. With (T-copy), (T-ineq), (T-dual), (T-mix), (T-budget) of row 1553 and (T-carry), (T-sign), (T-front) of row 1584 that is twenty names for about eight distinct events ((T-mix) = (R10) = (FL); (T-budget) = (R3)). One consolidated list in the registry row would stop a later lane from re-deriving it.
4. Rows 1004 and 1005 (frame changes and their literature) are "checked by no one". Stage C line 9 leans on their RESULT text. If the owner wants one more assurance before a pause, a check of row 1004's six proved statements is on file as its work item W1 (lead note under row 1004).
5. Process note (ARGUED). Both earlier stops were written by this model family and withdrawn by the cross-provider check. That is the check working. The cost was eleven proof rows on objects that (g4) and (g6) would have stopped at the break clause. The bar (WB) moves those two tests into the break clause itself.
6. The owner question, if the lead agrees: "Pause gap proof rows until a trigger fires (weekly watch kept), and choose O1, O2 or O3 for the freed capacity?" It is a pace and target question, which the lane's rules reserve for the owner.

## Labels

| Statement | Label | Anchor |
|---|---|---|
| The brief's "Standing now" (band paused on triggers; flux lemma stopped three ways, electric only; bootstrap equivalent; (A1) slot stopped with corrected reasons; two swap-moment routes untested) | ON FILE, verified | Steps 2, 3, 6, 12 |
| No named trigger has fired | ARGUED (a reading of RESULT texts) | Step 10 table, B4 |
| Lemma EVEN (a)-(c) | PROVED here by hand, unchecked; a corollary of check 1585 (iii) | Stage A |
| "(INV) does not follow from a gap" | ARGUED; undecided on file (Row A (ii)) | Stage A |
| A free field has a replica rotation that fixes the vacuum pair | GUESSED (recalled background; not used) | Stage A |
| B3: readout (1 - P)/(1 + P), threshold 84/541, arc cross-ratio | PROVED (algebra) for the readout and threshold; ARGUED for the factor 4; ON FILE as Structure I, rows 1207, 1373, 1461, 1526 | Stage B |
| Remark TEMP (a), (b) | PROVED here by hand, unchecked; (a) used in check 1556 (iii) | Stage B |
| "A temporal recipe cannot be the missing carry" | ARGUED | B4 |
| The asymmetry (electric objects exist at low cost; neutral side ends at (T-mix)) | ARGUED | Stage B |
| Stage C table, each line | ON FILE for the quoted anchors; the verdict column is ARGUED | Stage C |
| "The lane lacks a technique, not an input" | ARGUED; a judgement, not a theorem | Decision 2 |
| (PZ), (PZ-keep), (PZ-open), (WB), O1-O4 | proposals | Stage D |
| "About 220 rows", "five direction checkpoints" | corrected: 219 rows of mixed kinds; six direction rows | correction note |
Not read in this row: the bodies of rows 1565-1568, 1574, 1576, 1581, 1587, 1588, 1591, 1592 (RESULT texts and their checks' RESULT texts only; body of row 1573 L140-215 read); the account; AV-a to AV-e of the tree; `library/port-map.md` beyond its headings.

Provenance: Claude Fable 5.2 high, laptop subagent; author only, checked by no one; no numeric run, no Lean, no web access; lane checkout read at 560ed57ce; nothing edited, committed or posted. Run 2026-11-26, 06:47Z to about 07:15Z by the row's start stamp and `date -u`.

RESULT: Row 1597 (Claude Fable 5.2 high, laptop subagent; author only, unchecked; no numeric run, no Lean; read at 560ed57ce). Decision: (1) no named trigger has fired and no untested route on file earns a proof row: the two swap-moment classes of check 1583 need near-invariance of the vacuum pair under the whole circle (Lemma EVEN, proved here, unchecked) and have no method; the front sweep has no ordering inequality (check 1585 (vi)); a fourth attack on the lower-tail lemma meets the same short-period flux cost and is electric only; check 1585's recipe applied to the swap is Structure I of row 1576, the seed as an identity; the (A1) routes of check 1596 still have no reader without (A2); every temporal recipe moves its open estimate to a shorter period, and the consumer already owns that direction (Remark TEMP, proved here, unchecked), so (T-carry) should mean two spatial sizes or two couplings. (2) No switch: ten candidate inputs tested with (g1)-(g6) as corrected by check 1556; each fails (g4) or a part of (g6); the lane lacks a method for one estimate (mixing in law across a cylinder of physical length above the Dobrushin range), not an input statement. (3) Recommend to the owner: pause gap proof rows (band, flux sub-line, (A1) slot) until a trigger fires; keep a weekly literature and account watch, the daily reply check, and the frozen Lean chain; a check may withdraw the pause only with an object that reads Pi or carries in size or coupling, whose open estimate is not two-sample mixing, and that names a method (bar (WB)). Next rows: Row A `gap-direction6-check-astra62` (cross-provider check with break tests on the neutral side and on the carry) and Row B `gap-watch-r1-luna` (weekly watch, first run 2026-12-03); no band, (A1) or T0 proof row. Open: (PUR-io), Pi, (N-flux) and (L-tail), (T-mix), (A1), (A2), the mass gap; undecided here: whether freed capacity is held, goes to GOAL.md's "Then" list, or to uniqueness of the limit (owner's call).
