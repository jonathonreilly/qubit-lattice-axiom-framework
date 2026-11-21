lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T11:10Z

First failing step: `library/l17c.md` line 192, in the proof of the small-exponential lemma (§3): "The auxiliary radii lie below the target radii and hence obey their individual ceilings." This does not follow for the stated range 0 < a_0, a_1 <= 1 (line 125). Repairable. No consumer changes. Repair in finding 1.

# Gate: referee of `library/l17c.md` (queue row 336, `l17c-gate`)

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, commit 48fc63485, branch claude/ym4d-hard-route. One line-by-line reading by one model. Not an audit, not human review.

## Scope and sources

What is refereed: `library/l17c.md` (538 lines, Codex, checkout a126e8a11): its §2 deduction from `library/b109.md` P20 (110), its admission budget (3)-(5), its small-exponential lemma (6)-(11), its `c_T` adjustment, its constant order (13)-(15), its §5 consumer split, its §6 consumer tables, and its Result.

What is not refereed: the proof of `b109.md` P20 itself. P20 is Codex's, row 325, "not refereed" in `FINISH.md`. I read P20's statement and its steps (111)-(113) with P19 once, because L17C uses them. I saw no failing step there. I did not read P20's inputs (`a1-balaban.md` §§3, 7, 9; `flat-port.md`). So this is not a check of P20. L17C's Result stays an implication from P20 and its premises (104)-(105).

Sources, each fetched once into a scratch folder at commit 31a47c543775: CA-I (166,711 lines), CA-II (145,624), CA-III (111,583) and `YM4_sketch_500.tex` (SA, 32,992). The line counts match the lane's. Balaban's CMP 109 OCR (`~/ym4d-papers/cmp109.txt`) was read at pp. 262-263 and pp. 275-278. Every source line cited below was read in a bounded excerpt. No file was read whole.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for every CA and SA passage cited; Tadeusz Balaban for CMP 102 and CMP 109.

## Findings

**1. Line 125 and line 192, §3 small-exponential lemma. The scope is too wide, and line 192 is a non sequitur. Repairable, not fatal.**

- What is wrong. The lemma claims its conclusion "for all target radii 0 < a_0, a_1 <= 1" (line 125). The proof fixes e_0 = a_0/(4C) and e_1 = min{a_1/2, sqrt(a_0/(4C))} by (10) (lines 180-181). It then needs P20 at (e_0, e_1). P20 holds only "at sufficiently small individual radii" (`b109.md` line 3342). Its ceilings, call them ebar_0 and ebar_1, are fixed after M and B^(109) (`b109.md` lines 3440-3443, 3646-3649). They are not the target radii. So e_i <= a_i does not give e_i <= ebar_i. For a_0 near 1, e_0 = a_0/(4C) can exceed ebar_0.
- The outline states the same lemma with the proviso. SA (ER8), SA 6586-6630, reads "Under (ER7), for sufficiently small a_0, a_1 there is a constant c>0". L17C copies its choice of radii and drops the proviso.
- §4 (14), lines 274-277, says "under its other ceilings". This is consistent with the repair. But (10) leaves no room for those ceilings.
- Repair (my wording, unproved beyond the arithmetic shown). Add the hypothesis a_0 <= 4C ebar_0 and a_1 <= 2 ebar_1. Then e_0 = a_0/(4C) <= ebar_0 and e_1 <= a_1/2 <= ebar_1, and the rest of the proof is unchanged. Every consumer's target radii are Balaban's absolute radii (alpha_0, alpha_1) or the running radii alpha_{i,j} <= alpha_i (CA-I 1667). So add one downward ceiling at Stage 7: alpha_0 <= 4C ebar_0 and alpha_1 <= 2 ebar_1. Its letters are fixed before the radii, since the radii come after (L, B^(109), M) (CA-I 34811-34830). No cycle.
- Alternative repair. Cap e_0 = min{a_0/(4C), ebar_0} and e_1 = min{a_1/2, sqrt(e_0), ebar_1}. Then shrink c_* to min{1/4, (16CD)^{-1}, ebar_0/(4D), ebar_1/2, sqrt(ebar_0)/2}. I checked by hand that Dr <= e_0/4, r < e_1 and C(e_0 + e_1^2) <= a_0/2 still hold. Then c_T depends on ebar_i, so it depends on M and B^(109). That is allowed: c_T° is already c_T°(d, L, M) (CA-I 29529), and every constant built from c_T is chosen before gamma.
- Add this ceiling to the §7 list of corrections, item 2.

**2. Lines 410-498, §6 consumer inventory. The listing is not exhaustive. The conclusion survives. Not fatal.**

The tables omit these ranges. Each has a (1.17)-shaped display, a `2B_3` factor, or a `c_T` use. I read each one. None is a use of complex (1.17), so none adds a requirement.

| Range | What it is | Why it adds nothing |
|---|---|---|
| CA-I 33598-33838 | near-case labels | The bound \|u_j - 1\| < B_3^2 O(1) M alpha_0 is CMP 109 (3.37). CMP 109 pp. 275-277 gets it from the axial frame (3.26) and Prop. 9, not from (1.17). The CA takes it as "the given bound" and reads it through CA-I 13336-13371. |
| CA-I 42198-42340, 42545-42640 | one-layer clause and its remark | The field U is G-valued (CA-I 42203, 42238). Real case. |
| CA-I 43590-44380 | §4.12 constrained minimisers U_E | CMP 102b Theorem 1 at real data. Real case. |
| CA-I 117207-117328, 121282-121350 | B' ball ceilings; §4.26 near-pair chain | Lipschitz bound in B' from Prop. 9, and the (3.37)-(3.52) chain. The route through (1.17) is named and not taken ("would"). |
| CA-I 128880-128930 | hypothesis (b) of §4.26 | A reading of the current bound at the real stage background U_*. Real case. The lane's row 128551-128758 covers the same lemma by range only. |
| CA-I 144962-145182 | §4.28 hypothesis (I) | A different CMP 109 sentence ("approximately the same regularity properties"), taken by statement. |
| CA-I 155940-156060 | minimiser path in §4.31 | (iv) comes from the nesting identity (N1), not from (1.17). |
| CA-I 29466, 29985-30107, 30571, 31308, 31398-31457, 31749-31874, 32264-32284, 35964 | further `c_T` uses in §4.7 | Each enters through (c_T r)^{-1}, (c_T r)^{-2} or a ceiling c_T r <= const. A smaller `c_T` only enlarges constants that are chosen before gamma. |
| CA-II 96276-96372, 96412 | §8.5 box extensions | Seeds e^{i sigma eta A} in the r_n-polydisc of `5.2:lem-polydisc-containment`. Covered through that lemma. |

The CA-I lines 70548, 75590-75665 and 119041-124591 use other constants also written c_T: a term's constant, and c_T^sz. They are unrelated.

**3. Lines 17-23 and 117-120: credit. Not a defect.** The corrected supplier (2)-(3) is the outline's own Theorem 5(a), SA 9746-9753: "once K^#(alpha_0' + alpha_1'^2) <= alpha_0, a triple ... belongs to the core". The lemma (6)-(11) is SA (ER8), SA 6586-6630, almost word for word. The lane credits both. For the five-check rule on contributions (`FINISH.md`, How we work, item 6), what is new against their outline is the following. P20 supplies the tower estimate that SA states as an assumption, (ER7) at SA 6571-6584. The consumer check shows that the CA's (1.17) consumers are all seeds or real. The correction itself is the CA moving to its own outline's Theorem 5(a) budget.

**4. Line 46 and (14): "early constant". Remark only.** L17C puts C before M. P20 says K is early. If K turned out to depend on M or B^(109), nothing breaks: every use of C (budget (3), c_*, hence c_T) comes after M and B^(109).

## Each step checked

- **(2) from (110), lines 46-74.** (1) is (104)-(105) word for word, with eta = xi_p and s = L^n xi_p. C = 2 max{K,1} > K and e_0 > 0 make the bounds strict. Correct.
- **(3)-(4), lines 76-101.** The change of units gives (mu e_0, mu e_1) at label (p,Z). This is CA-I 34107-34145 (Step 1 of `4.8:prop-small-pairs`), including the single mu on the cube gauge. Then K(mu e_0 + mu^2 e_1^2) xi_p^2 < C(mu e_0 + mu^2 e_1^2) xi_p^2 <= mu C(e_0 + e_1^2) xi_p^2 <= mu a_0 xi_p^2, because mu <= 1. The current bound is the same with (L^n xi_p)^2. The real factor gives C mu e_0. This is exactly `4.8:eq-tower-clause-a` (CA-I 33060-33069) at c = a_0 L^{-(j-p)}. The geometry Z^{wr p} in Omega_n is CA-I 34177-34189. Correct.
- **(5).** (mu e_1)^2 <= c mu e_0 follows from e_1^2 <= c e_0 and mu <= 1. Correct.
- **(7)-(8).** The linear term of the plaquette product is i eta^2 (dA)(p), and \|dA\| <= 2r. The rest is at most e^{4x} - 1 - 4x <= 8x^2 e^{4x} with x = b eta r. So \|d e^{i eta A} - I\| <= D r eta^2 with D = 2 + 8 b^2 e^{4b}, using r, eta <= 1. Correct.
- **(9).** CA-I `4.4:lem-current-remainder` (i), CA-I 10350-10376, at U_0 = I gives c = 0 and ell^3 \|F\| <= c_F \|A\|^2 for \|A\| <= 1. With top length one, \|J(e^{i eta A})\| <= \|d*dA\| + c_F r^2 <= (1 + c_F) r. Correct.
- **(10)-(11).** With c_* <= (16CD)^{-1}: Dr <= a_0/(16C) = e_0/4. r <= a_1/4 < a_1/2. r^2 <= a_0^2/(256 C^2 D^2) <= a_0/(16C) < a_0/(4C), since a_0 <= 1 <= 16CD^2. C(e_0 + e_1^2) <= a_0/2. Correct, except for finding 1.
- **`c_T` and its consumers, lines 199-251.** `4.7:not-true-pairs` (CA-I 29522-29605) has c_T = min{c_T°, 1/8, 1/C_IV} and seeds N_j(Z) <= c_T r_j with r_j = min(alpha_{0,j}, alpha_{1,j}). The primed radius is free (CA-I 29563-29589). Adding c_T <= c_* is allowed. It changes C_theta (CA-I 30032-30034), K-tilde (30006-30009), C' (32284) and C_Pi (CA-III 90592). Each is chosen before gamma (CA-I 32405-32409; CA-II 94857-94865). theta(gamma) -> 0 because q > p_0 (CA-I 30051-30105). The ratio (12) agrees with CA-II 4390-4398, and c_T cancels. CA-II 4381-4384 does apply "(i)-(iii) imply (iv)" at the target radii themselves, so the lane is right that this sentence is too broad. Correct.
- **(13)-(15), §4.** The order matches CA-I 1590-1690 and 2106-2140. A ceiling alpha_1^2 <= c alpha_0 on the absolute radii is a floor on alpha_0, because alpha_0 is chosen after alpha_1. The lane is right not to use it. The algebra of (15) is right: a_{1,n}^2/a_{0,n} = (C_1^2/C_0) x^{-1/2}(log x)^q. The hand bound x^{-1/2}(log x)^q <= 2^m m! t^{q-m} with t = log x is right. The `in1.md` example is at its line 238. Correct.
- **§5, MU and OC.** Both are "Proof outstanding" in the CA (CA-I 45162-45234). `mu.md` (7.4) is the sum-of-radii test the lane quotes. `mu.md` is frozen after its own Claude gate. `oc.md` line 90 keeps the real-background requirement separate. CA-I 4.9 `cor-printed-pairs` (36806-36905) confirms that the small pairs have U = 1 and that the real backgrounds are real. The six memberships of `4.8:prop-class-reproduction` (CA-I 34242-34403) are as the lane's table says: only (e) uses `4.8:prop-small-pairs`, at the unit pair, true pairs, small pairs and real backgrounds. Correct.

## Consumer list, from my own search

Searches over CA-I, CA-II and CA-III: every `1.17`; the labels `4.8:prop-small-pairs`, `4.8:eq-small-pairs-*`, `4.7:not-true-pairs`, `4.7:eq-true-pairs-*`, `5.2:lem-polydisc-containment` and the 4.13 lemmas; every `c_T`; every `2B_3` and `B_3^2`; and every "(i)-(iii) imply (iv)". CMP 109 (1.17) occurs in CA-I (31 lines) and at CA-III 111326 only. Every other `1.17` is CMP 116, CMP 122a, CMP 122b or a decimal. Each CMP 109 (1.17) line lies in a row of the lane's §6 tables. The lane's label-occurrence claims at its lines 412-418 are exact.

Uses that need the tower bound at a complex, non-real pair:

| Consumer | Pair | Need | Met by |
|---|---|---|---|
| CA-I 34058-34218, `4.8:prop-small-pairs` | the supplier slot | complex (1.17) | (2)-(4) |
| CA-I 29522-29605, `4.7:not-true-pairs` | e^{i eta Z}, own current, U = 1 | ball c_T r_j | (6)-(11), c_T <= c_* |
| CA-I 32412-32500, coupling increment | polydisc of radius xi^3 c_T r/(8d) | through true pairs | the same |
| CA-I 34288, 34372, membership (e) | unit, true and small pairs; real backgrounds | U = 1 seeds or real | the same, or e_1 = 0 |
| CA-I 34714, 34738 | layerwise input; orbit-form target | true backgrounds or seeds | the same |
| CA-II 4333-4398, `5.2:lem-polydisc-containment` | e^{i xi A}, independent current | ball r_j = c_T min(alpha_{0,j}, alpha_{1,j}) | the same |
| CA-II 4599-4688, 94811-97192; CA-III 90585-90624 | through r_j | radius only | (12); c_T cancels |

Every complex seed has U = 1 and a radius that is a fixed small multiple of min(a_0, a_1). This is why the quadratic term costs nothing. r^2 <= r min(a_0, a_1) <= a_0 r.

Uses at real pairs only, where e_1 = 0: CMP 109 p. 263 minimal configurations (CA-I 34087-34089, 34205-34208); CA-I 10750-10754; 36806-36905; 42198-42340; 43590-44380; 128551-128930; 155275-155438; CA-II 99767-99813. For these, (2) at e_1 = 0 gives C e_0, or the real CMP 102b bound 2B_3 e_0 is kept. Either way the bound is linear in e_0.

## Constant order

C (from K; at the latest after M and B^(109)); then M and B^(109); then P20's ceilings ebar_0, ebar_1; then Stage 7, alpha_1', alpha_0', alpha_1, alpha_0, with the new ceiling of finding 1; then alpha_2; then c_T = min{c_T°, 1/8, 1/C_IV, c_*}; then the constants built from c_T; then gamma, last. The auxiliary radii e_0, e_1 are chosen at each use, after the targets. Each new condition is a downward ceiling, or a floor on a letter chosen later. No cycle.

## Verdict

- (2) from P20 (110): **correct**.
- Admission (3) and one-power heredity (4): **correct**.
- Small-exponential lemma (6)-(11): **correct after the repair of finding 1**. As written, line 192 does not follow.
- `c_T` adjustment and its consumers in CA-I §4.7, CA-II §§5.2 and 8.5, and CA-III §10.4: **correct**.
- Constant order: **correct**, no cycle, with finding 1's ceiling placed at Stage 7.
- Consumer inventory: **conclusion correct**. Listing incomplete (finding 2), with nothing load-bearing missing.
- Overall: **ADVANCE.** Given P20 (110) and its premises (104)-(105), the corrected L17 suffices for every active consumer of CMP 109 (1.17) in the account. This needs the one repair of finding 1. The original eps_0-only L17 is neither proved nor refuted; it stays open. The closure of core statement L17 by the corrected statement still waits on a check of P20 (`b109.md`, row 325, not refereed).

Checked line by line by Claude (Mini worker).
