lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 15:55:29 UTC 2026, pinned at commit 20e5a560a. Author only, checked by no one.

# Direction pass on (PUR-io) after campaign round one (FINISH row 1706)

## Status

Complete. Finished Sat Nov 28 16:09:39 UTC 2026. The RESULT line is at the end.

## 0. Reading log

- Read in full: the row 1706 brief (`~/ym4d-lead/items/gap-purity-direction-fable.item`); `library/gap-purity-crux-card.md`; `library/gap-direction9-fable.md` (row 1672); `library/gap-mech-direction4-fable.md` L46-L140 (row 1553, steps 5 to 17); `lean/gapchain/GapChain/Stage0.lean` L228-L290 (`ExpClusters` and the two consumers).
- Read as RESULT texts (pointers, not evidence): FINISH rows 1653, 1672-1675, 1682-1690, 1692-1696, 1698-1705. Rows 1691 and 1697 had no RESULT when I finished. Row 1707 (the twin) and its output: not opened.
- Read in part: `library/gap-purity-rh-strategy-fable.md` L300-L322 (Proposition OBS); `library/gap-purity-y4-solve-fable-check-astra62.md` L91-L95 (what survives of row 1696); `library/gap-purity-tool-design-fable.md` L90-L161 (N2, KT-A, the Phase 2 verdict).
- Not read: the proofs of any Lean stage; the release; the account; the files of rows 1673, 1674, 1683, 1689 and 1703 (their RESULT texts and their checks only).
- Grep counts (a count is not a reading): given in section 2.3. They cover FINISH.md and `library/`.
- No Lean run, no numeric run, no web access. Nothing committed, pushed or posted. One file written (this one).

Labels: PROVED (by hand, here, checked by no one), CITED (a row or file, named), ARGUED (my judgement), GUESSED.

## 1. Part 1: what every failed attempt lacked

### 1.1 The facts used

Write pur(n, beta) for the neutral purity of the cube of side n at coupling beta and time u = n/512. Write n_K = l L^K and beta_K for the calibrated coupling. Write h = log(625/457) (about 0.313, a float guide).

- (F1) CITED (row 1696, as corrected by check 1700, lines 91-95 of the check). On every fixed lattice, pur(n, beta) tends to 0 as beta grows, for SU(2), U(1) and Pin(2). So the passing set P(n) = {beta : pur(n, beta) >= 457/625} is bounded. Put B(n) = sup P(n). At a passing cutoff, B(n_K) >= beta_K. Check 1700 adds: no order, interval or slope inside P(n) follows.
- (F2) CITED (row 1688, Proposition OBS, as scoped by check 1692). Every one-way inequality found there holds for every positive trace-class operator with a commuting finite group action, or for every state on a tensor product. Such operators can have purity near 0.
- (F3) CITED (checks 1698, 1704, 1705). Three times a step was void for U(1) only because an operation is trivial for U(1) (adjoint test, singlet packet, orientation sheet). The U(1) twin with the same normalisation satisfied every proved line.
- (F4) CITED (row 1702; row 1553 step 9 for the rest of the record). The proved order-one crossings read in the campaign (Kopper-Magnen-Rivasseau; Gawedzki-Kupiainen; Kupiainen) need large N or an exact hierarchy. Row 1553 step 15 records two more, both in two dimensions and both unrefereed: the stiffness flow of the OpenAI O(4) text and the dilution proof of Ding, Huang and Yang. Neither has a gauge form on file (row 1553 steps 13 (a) and 17).
- (F5) CITED (rows 1703, 1705). The bare packets of row 1689 have thermal weight below every inverse power of the cube side. The same bounds hold in five dimensions and for the U(1) twins.

### 1.2 Lemma 1 (the budget in plain form). PROVED

Let p_i be the weights lambda_i^u / sum_j lambda_j^u on the neutral sector, and p_0 the largest. Then p_0^2 <= purity <= p_0.

Proof. sum p_i^2 <= p_0 sum p_i = p_0. And sum p_i^2 >= p_0^2. QED.

So a passing cube has p_0 >= 457/625: all excited neutral states together hold at most 168/625 of the thermal weight at time n/512. And p_0 >= sqrt(457)/25 (about 0.855) is enough. This is the deficit formula (P1) of row 1688 in substance. It is ON FILE and it is not progress. I state it because the next statements use it: the target is a bound on a **whole thermal sum**, not on one channel.

### 1.3 Statement 2 (three exclusions). PROVED from (F1), (F2); the third part ARGUED

Let E be any hypothesis on a pair (n, beta) that implies pur(n, beta) >= 457/625.

- (2a) **Not a one-coupling-direction statement.** For each n, the set of beta where E holds is bounded above. So no proof of E can work "for all beta above beta_0(n)" on a fixed lattice. This excludes every weak-coupling expansion at fixed lattice size. PROVED from (F1).
- (2b) **Not a general inequality.** E does not follow from inequalities that hold for all positive operators with a group action. PROVED from (F2), in the scope of Proposition OBS.
- (2c) **Joint in size and coupling.** (PUR-io) needs E at (n_K, beta_K) for infinitely many K, with n_K and beta_K both unbounded. By (2a), the proof must use the relation between n_K and beta_K. A proof that treats either variable as fixed while the other moves is excluded. ARGUED (it is the reading of check 1700's surviving statement B(n_K) >= beta_K; it adds no slope).

### 1.4 Statement 3 (the range at which the law reads the group). ARGUED; one-loop reasoning, not a proof

At bare coupling beta, the Wilson SU(2) law and the law of three independent compact U(1) fields at the same beta differ, on gauge-invariant data of lattice range R, by relative effects of order (log R)/beta. The reason: the non-abelian term changes the effective coupling by a fixed amount (proportional to C_A) per scale, and one scale changes 1/g^2 by order one out of beta.

Consequences.

1. On the calibrated cutoffs beta_K is above 2^2800 (CITED, crux card section 2). A step whose proof uses a bounded number of scales near the cutoff, or bare links with bare normalisation, sees a law that is abelian to one part in 2^2800 per scale. Its U(1) twin will satisfy every proved line. This is the content of (F3) and (F5): rows 1683, 1689 and 1703 worked with bare lines, bare packets and bare plaquette tests.
2. The group changes the law of a bounded region by order one only where the effective coupling is of order one. Below that scale the group appears only as a sum over about beta_K scales. The only object on file that holds such a sum exactly is the block map of the account (Lemma TW, row 1468, CITED through row 1672).
3. So "reads the group" has two possible meanings and no third: (i) an exact carry through all weak scales, which is an identity and has no sign; (ii) a local estimate at order-one effective coupling, where no small parameter exists.

### 1.5 Statement 4 (the common property). ARGUED from statements 2 and 3

**A successful estimate is a strict transport at order-one coupling.** In full:

- (T1) It compares two Wilson laws at two different points (size, coupling), or one Wilson law with a second law for which the result is proved. It is not a statement about one law at one point.
- (T2) It is an inequality with a strict sign. Its sign comes from a term that is zero for U(1) (the commutator) or from the finite centre, in the response of the law, not in the representation theory of one link.
- (T3) It holds where the effective coupling is of order one, with no large N and no exact hierarchy.
- (T4) It holds the whole neutral thermal sum (Lemma 1), or, at the second plug-in, a rate (section 2.2, class 7a).
- (T5) Its loss, summed over all scales it is used on, stays inside h. All weak scales must be crossed by an exact carry, because any loss per scale is summed about beta_K times.

(T5) is why the size of a gain matters as much as its sign. Row 1683 proved a gain c n^3 log beta and never spent it (check 1698). Row 1703 lost more than any power of the side.

I can not state this as a theorem. The honest form is: statements 2a and 2b are proved exclusions; statement 3 and (T1)-(T5) are the reading that explains all of (F1)-(F5) at once. Check 1675 showed that a short gate can admit useless estimates; (T4) and (T5) are there to close the door it found (the rare-low-mode estimate of row 1283 fails (T4)).

### 1.6 Each row of round one against (T1)-(T5)

| Rows | What it was | First clause it lacks |
|---|---|---|
| 1682, 1686 (strategy mining, 55 problems) | patterns from solved problems; lemmas HW-SU2, OU, REP, NC, B1, TT1 | (T1), (T2): one-law statements, group-blind; no candidate |
| 1684, 1685, 1694, 1695, 1699, 1702 (about 90 papers) | literature | (T3): every crossing found needs large N, a hierarchy, a finite group, a Higgs field or abelian duality |
| 1688 (RH architecture, Fable) | ENT, P1-P7, OBS | (T2): holds for all positive operators (its own Proposition OBS) |
| 1689, 1704 (RH architecture, Astra) | measurements A, B, C | (T2): the operation is trivial for U(1), the law is not read; (T3): finite lemmas at the bare scale |
| 1683, 1698 (far afield) | adjoint plaquette test, gain c n^3 log beta | (T2) by the cosine twin; (T5): the gain is never spent |
| 1696, 1700 (direct solve of (Y4)) | fixed-lattice limits | (T1): one lattice; the result is the exclusion (2a) |
| 1701 (tool design) | count, hypercontractive exponent, interpolation | (T3): the open link (HC-phys) is the crossing; all links on file |
| 1703, 1705 (proof lane on C, then A) | two obstructions | (T5) and (T2): bare packets, same bounds in 5D and for U(1) |
| 1687, 1693 (precedents) | the one-cube criterion D(n, alpha) | (T3): D is proved only at strong coupling; (T4): a gap does not bound the count |

No row of round one proposed a comparison of two laws. Round one tested measurements and general inequalities.

### 1.7 What is and is not new in Part 1

Not new: the wall itself. The record has it as Proposition NEG (row 1386), the kinds (K-I), (K-II), (K-III) (row 1553), the obstructions (N1)-(N7) of row 1674 ("one-level", "perturbative-range", "no small parameter is known at the correlation-length scale"; RESULT text only, file not opened) and the gate (EXC) of row 1672. Statement 4 is equivalent to these in kind. **Equivalent is not progress.**

New as a tool for the lead only: the row-by-row table, statement 3 as the reason the twin test fails every time at the bare scale, and the pre-filter of section 3.2. They save rows. They move no input.

## 2. Part 2: the classes the property leaves open

### 2.1 The classes, by what is transported

(T1) says a candidate compares two laws. There are six things that can differ between the two laws, and three ways to change the target. For each I give the standing in the record and the cheapest test.

| # | Class | Standing (what I opened, or count only) | Cheapest first test that kills it |
|---|---|---|---|
| 1 | Size, at a fixed coupling | ON FILE and proved as a carry: reflection positivity with the centre gives a gap on larger cubes from a seed on one (row 1553 step 13 (b)). It is the consumer. It needs the seed. | None needed. It is not an attack. |
| 2 | Coupling, at a fixed blocked scale | ON FILE: (VIR_K), Theorem TR, row 708; "three ways failed" (row 1553 step 13 (c)). | Ask for the bound on the sum of N^4 connected correlations with the action density at the physical scale. |
| 3 | Size and coupling together (a block step at order one) | ON FILE, counted as spent by row 1553 step 12 (rows 1468-1500, 1542-1552). The computer-assisted form (K-III) needs the carry (A1) and (A2) first. | Ask for the closed class of coarse laws and the signed decrement. Rows 1544 and 1549 show how this dies. |
| 4 | Model: compare with a model whose crossing is proved | ON FILE: Durhuus-Froehlich (loses one dimension; in 4D it lands on an ordered 3D model), the Z_2 fibre (row 1553), Migdal-Kadanoff and Tomboulis (not selective; check 1675 names rows 797-801, 1025, 1029), the two 2D engines (no gauge form). | The U(1) twin of the comparison inequality. The proved model side is never where the group is read; the comparison is. |
| 5 | Sector or observable, at one point | ON FILE: twist ratios and step-scaling couplings "hold the flux half at most" (a FINISH row near the step-scaling brief; RESULT text, row number not recorded here). Fails (T4). | Ask whether the quantity holds the whole neutral sum. |
| 6 | Copies (replicas, exchangeable copies) | ON FILE: Lemma REP of row 1682 (replicas carry only the k = 2 information); the copy structure of Ding, Huang and Yang has no gauge form (row 1553 step 17). | Ask for a conditional abelian model with non-negative couplings. |
| 7a | Target: the rate plug-in `ExpClusters` | ON FILE: rows 1672, 1673 (estimate (E), a Dobrushin-Shlosman-type one-link influence bound; open at calibrated SU(2); its path form fires on gapped 3D U(1)) and 1674. See 2.2. | Ask for an estimate that gives a rate and not a count. If it also needs order-one coupling, the class is the same wall with a smaller constant. |
| 7b | Target: another aspect in place of 512 | Not found as a row (check 1653 notes that the chain fixes the aspect 1024 w <= n). Examined here, 2.2. | One reading: the lemma of Stage 3 that uses 1024 w <= n. |
| 7c | Target: another one-box criterion (the Wasserstein criterion D(n, alpha) of Bhattacharjee, Bhattacharya, Lockwood and Romanov) | ON FILE (rows 1687, 1693): proved only for abs(beta W) < 1/3; no Lean; could feed the rate plug-in, not the purity. | The same crossing. A worst-case boundary criterion is stronger than the seed at weak coupling (ARGUED). |
| 8 | A continuum-side plug-in: prove the gap from the proved properties of the limit | Not found as a class (counts: "Kallen/Lehmann" 0 FINISH lines, 5 library files; "Weinberg-Witten" 0 and 2). Examined here, 2.2. | Two thought twins, 2.2. Killed. |
| 9 | A budget over scales, using that the target asks only infinitely many cutoffs | "dichotom": 36 FINISH lines, 134 library files (count only, not opened). Examined here, 2.2. | The massless twin. Killed as an attack; it changes the form of the open step only. |

### 2.2 The classes I examined here

**7a. The rate plug-in.** CITED: `Stage0.lean` L228-L231. `ExpClusters L K nu m` says: for every positive-span observable Z, for infinitely many j, there is a constant C with latticeU(nu_j, Z, t) <= C exp(-m t) at all odd lattice times. The constant may depend on j and on Z. PROVED by reading the quantifiers (it is Lemma 2.7 of row 1674 in substance, ON FILE): this is a statement about the support of a spectral measure of the infinite-volume lattice state at beta_K. It asks that the lattice mass in each channel is at least m L^(-K) at infinitely many cutoffs. It holds no count of states, no box, no aspect and no factor 12,000. ARGUED: it removes clause (T4) and nothing else. A lower bound for a lattice mass at beta_K, sharp to a constant factor in physical units, is the crossing in its plainest form. It is the better target for a candidate that controls one channel. It is not an attack.

**7b. The aspect.** ARGUED. A longer time (u larger than the side) makes the purity test easy in a small box: there the box gap is positive at weak effective coupling (GUESSED: the small-volume picture of Luescher, of order g^(2/3)/l), and a long time kills the excited weight. But such a seed can not feed a size carry. The carry needs the test at a time that is short against the side, so that the cube behaves like a piece of infinite volume. A small-box gap is a finite-size effect and tells nothing about the limit. A smaller aspect than 512 (a time still short against the side) lowers the constant 12,000 and leaves the crossing. So no aspect helps. The one fact I did not check is where Stage 3 uses 1024 w <= n; that is one reading.

**8. A continuum-side plug-in.** ARGUED, by two twins. The release proves the Osterwalder-Schrader conditions, Euclidean invariance and non-Gaussianity for the limit (CITED, crux card section 1). (i) A composite field of the free Maxwell field, for example the square of the field strength, has all three properties and no gap. So no argument from these three properties gives a gap. (ii) If the argument also uses the logarithmic short-distance behaviour (asymptotic freedom), the twin is a gauge theory in the conformal window, which is on the lane's test table as a gapless model (CITED: row 1553 step 16; belief-grade, not a constructed theory). So a continuum-side argument must read the absence of matter, and the limit has no proved property that does. Killed. This is a thought test; it is not a theorem.

**9. A budget over scales.** ARGUED. The target asks for infinitely many cutoffs at one l. A bounded quantity that is monotone along the scale has small increments at most scales. That gives a dichotomy (gap, or the same law at all large scales), not a gap. Excluding the second branch is the crossing, and the free photon is the twin. It changes the form of the open step from "a size" to "the flow does not stop", which is (MON-L) of row 1553 (CITED). Not an attack.

### 2.3 Bounded search for classes not on file

I counted FINISH lines and library files for thirty method names before calling anything new (rule: check the record first). Every class I could name has a presence. The thinnest (FINISH lines, library files): Kallen-Lehmann 0, 5; Weinberg-Witten 0, 2; Borel or resurgence 0, 4; large-N gauge theory 1, 3; supersymmetry 2, 10; Lanford or Koch-Wittwer 2, 11; hierarchical models 2, 12; perfect or fixed-point actions 2, 13; tensor renormalisation 3, 13; volume reduction 4, 19. I examined the first two as class 8. For the others, the reason they do not meet (T1)-(T5) is short and ARGUED:

- Resurgence and Borel methods are fixed-lattice or fixed-order statements in the coupling: excluded by (2a).
- Large N: the proved 1/N crossings are vector models (row 1702). For a gauge field the large-N limit is a matrix model with no proved crossing in four dimensions (CITED in kind: the literature question of the record, "is a gap proved for all 't Hooft couplings"; I did not open its answer). Volume reduction trades size for N and reads N, not the crossing.
- Computer-assisted flows (Lanford; Koch and Wittwer; Ebel, Kennedy and Rychkov) and perfect actions are class 3 in its (K-III) form. They wait on the carry.

**Result of Part 2.** I found no class that meets (T1)-(T5), is absent from the record, and has a first estimate. Classes 7b, 8 and 9 were not on file as rows; each fails a thought test. This is one more bounded pass. By check 1443 no exhaustion follows.

### 2.4 Options that are the owner's decision

Each of these leaves the SU(2) Wilson band or the purity campaign. None is mine or the lead's to choose.

1. **SU(N) at large N.** ARGUED: it does not lower the crossing, because no 1/N theorem exists for a gauge field in four dimensions; it would be a different theorem.
2. **Proof capacity on the carry (A1) in rate form** (the two-cutoff comparison; the row that check 1422 named, CITED through row 1553 step 14). It has a method. By statement 3, every route that can succeed uses an exact carry through the weak scales, so it is on every path. It is base work, and the owner's rule is hardest first.
3. **Off the band:** SU(N) existence or uniqueness of the limit (row 1672 section 5, item 4).
4. **Another dimension or law** (3D SU(2); Villain or heat-kernel weight). The consumer is proved for the Wilson law in four dimensions only.
5. **An outward offer** to the authors of the release (row 1672 section 5). Outward posts need the owner.
6. **Whether the campaign continues in its round-one form** (section 3.1).

## 3. Part 3: ranking and decision

### 3.1 Verdict

**No row on (PUR-io) is worth running now.** Reasons.

1. Round one ran 24 rows by four new methods (mining of 55 solved problems, about 90 papers, two architecture twins, a tool design) plus a direct solve and a proof lane. It moved no input. Every result fails a clause of (T1)-(T5), and for the same reason each time (section 1.6).
2. Part 2 found no class with a first estimate. A row without a first estimate is a search row, and the search methods of round one are now used.
3. The one strategy of the campaign that is still open is in flight: row 1697 (the toy setting first, the way the Riemann hypothesis proof was found). Its result is not in. A new row before it lands would not use it.
4. This row has an independent twin (row 1707). I did not read it. If it names a candidate, that candidate goes to the pre-filter of 3.2, not to this verdict.

This is a stop for seed rows of the present kinds. It is not a statement that no mechanism exists.

### 3.2 The pre-filter (use before any future row; it costs minutes)

A candidate must answer four questions in writing before a lane runs.

- (Q1) Which two laws does it compare (two sizes, two couplings, or a second model)? If it measures one law at one point, stop: statement 2.
- (Q2) At which scale is the effective coupling of order one in its key step, and what replaces a small parameter there? If the key step is at the bare scale, stop: statement 3.
- (Q3) Write the line where the commutator or the finite centre fixes the sign of the response of the law. Write the same line for the U(1) twin with the same normalisation, for 5D SU(2), and for gapped 3D compact U(1). The sign must differ for the first two and agree for the third.
- (Q4) What is the loss per scale, on how many scales, against h = log(625/457)? Does the quantity hold the whole neutral sum, or does it aim at `ExpClusters`?

ARGUED: these four questions would have stopped rows 1683, 1689 (A and C) and 1703 before they ran, and their three checks with them. They are the (Y4) filter and the twin test of the crux card, put in the order in which candidates die.

### 3.3 Ranking of what can run

| Rank | Item | Why | Decisive outcome |
|---|---|---|---|
| 1 | Wait for rows 1697 and 1707; apply 3.2 to anything they name | In flight; costs nothing more | A candidate that answers (Q1)-(Q4), or none |
| 2 | Add 3.2 to the crux card, section 3 | Saves about five rows per failed measurement | Lead edit; no model row |
| 3 | The standing probes of row 1672 (one closed-folder solve per new model; the weekly watch), with `ExpClusters` as the stated target and (Q1)-(Q4) as the only gate | The trigger is most likely external (row 1672 section 4) | A candidate, or a filed negative |
| 4 | Owner's choice from 2.4 (item 2 or item 3) for the proof capacity | Capacity is otherwise idle | Owner decision |

Not ranked: more strategy mining, more literature sweeps of the round-one kinds, more far-afield measurement rows, another direction row, another obstruction theorem. Each has been run and its outcome is known.

### 3.4 The trigger that changes the verdict

One written candidate that answers (Q1) to (Q4). In the words of the record: a strict, signed comparison of two Wilson laws at order-one effective coupling, whose sign fails for the U(1) twin and for 5D SU(2) and holds for a gapped twin, with its loss stated. It can come from row 1697, from row 1707, from a new publication, or from a new model. When it comes, the first row is the gate row of row 1672 section 5 on that candidate, by the provider that did not write it.

### 3.5 If the owner wants a row to run now in spite of 3.1

Then the row is the carry, not another measurement. Brief, in the solve-it form:

> Target. Prove the two-cutoff comparison (A1) in rate form for the calibrated SU(2) Wilson trajectory: for two cutoffs K < K' and one fixed physical box inside the range of the account, the two blocked laws at the common physical scale agree up to an error that is summable in K, with the rate stated. The exact statement is the one that check 1422 names ("the one-family change of read for the ordinary stored strip at a common datum"); read it there and in the account before you start.
> Gate. A proof, checked line by line by the other provider, with every constant fixed before K; or the first failing estimate, written out. A result that is equivalent to the assumed input (E3) of the account is not progress.
> Rules. Read the record first. Labels on every claim. No menu of methods is given.

I do not rank this above waiting. It moves a real input, and it does not touch the crossing.

## 4. Labels and limits

| Statement | Label |
|---|---|
| Lemma 1 | PROVED here; ON FILE in substance (P1 of row 1688) |
| Statements 2a, 2b | PROVED from CITED facts (rows 1696 with check 1700; row 1688 with check 1692) |
| Statement 2c, statement 3, (T1)-(T5) | ARGUED; statement 3 rests on one-loop reasoning |
| The table of section 1.6 | ARGUED, from RESULT texts and checks; I did not open the files of rows 1683, 1689, 1703 |
| Classes 1-6, 7a, 7c | CITED as ON FILE, at the depth named in each line |
| Classes 7b, 8, 9 | ARGUED here; thought tests, not theorems |
| "No class with a first estimate" | ARGUED; a bounded pass, no exhaustion |
| The small-volume gap in 7b | GUESSED |
| The verdict, the ranking, the pre-filter | ARGUED |
| (PUR-io), the seed, the gap | OPEN |

Limits. No statement about the Wilson law is proved here beyond Lemma 1. Rows enter through their RESULT texts unless section 0 says I opened the file. The counts of 2.3 are counts. This row is a direction pass by one model; its twin is row 1707.

Credits. Tadeusz Balaban (the method). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (the release and the account). Levent Alpoge, Luke Sernau and Michael Rubinstein (the Riemann hypothesis proof, its shortened form and its outline, as rows 1688-1690 cite them). Bhattacharjee, Bhattacharya, Lockwood and Romanov (the one-cube criterion). Durhuus and Froehlich; Ding, Huang and Yang; OpenAI (the 2D O(4) text); Kopper, Magnen and Rivasseau; Gawedzki and Kupiainen; Kupiainen; Luescher. The lane's rows by gpt-6.2-astra, gpt-6-luna, Claude Opus and Claude Fable, named at each use.

Provenance. Claude Fable 5.2 (claude-fable-5-2), laptop subagent, one session. Nothing committed, pushed or posted. No other file written.

RESULT: Row 1706 (Claude Fable 5.2; author only, unchecked; no Lean, no numerics). Common property: a successful estimate is a strict transport at order-one coupling: a signed comparison of two Wilson laws, sign from the commutator or the centre in the law's response, holding the whole neutral sum, loss inside log(625/457); round one tested one law at one point, at the bare scale, where SU(2) equals its U(1) twin to one part in beta. Open classes: none with a first estimate; ranked: wait for rows 1697 and 1707, add the four-question pre-filter (3.2) to the crux card, standing probes with ExpClusters as target. Verdict: no (PUR-io) row now; trigger: one candidate answering (Q1)-(Q4). Owner decisions: capacity to the carry (A1) in rate form or off the band; SU(N) at large N (argued: no help); outward offer; campaign form.
