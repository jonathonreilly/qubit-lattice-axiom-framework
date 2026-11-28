lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T18:41Z

# Interface gate, independent attempt, at fcbb20f83

**Provenance.** Anthropic claude-opus-5-5, effort high, Mac mini worker, fresh session, pinned at commit fcbb20f83. This is a same-model check. It is not independent in model and it is not an audit. Verdicts steer research and grant no status.

**Scope.** Queue item 6, independent side: what `parts/hard-core--independent.md` delivers set beside what `parts/upper-chain.md` consumes. Statements only, mismatches only. A verdict here is on the match between two statements. It is not a verdict on any proof. Everything is conditional on Theorem I, which that file calls a target. UV-LOC-R and Proposition 8.1 are the mapped side's pairing; this attempt states no derivative form, so they do not apply here.

**Summary.** UV-CT is not delivered as written: CT3 fails as derived, and CT1 rests on a hypothesis that has no stated clauses. CT2 and CT4 fit. UV-OS is not delivered: no statement of (MD*_j), (SCR_j), (DEC_j), or (RAR^1_j) exists in the attempt. No counterexample to any consumer statement was found. No WRONG verdict on a consumer statement; one step of the attempt (6.1 item 4) is false on part of the class it is claimed for (D2).

## Verdicts: UV-CT (`parts/upper-chain.md` Text 7, line 339)

| Statement | Consumed | Delivered | Verdict | Defect |
|---|---|---|---|---|
| Source class W | complex, Lipschitz, may depend on orientation | scalar w_k(x) per site | CORRECT-NO-ADVANCE | D2 |
| E | E(0) = 0, analytic on polydiscs | E_sym, 6.2 | ADVANCE (fit) | none |
| CT1 | one-sided bound at the pattern | all w, 6.3 | CORRECT-NO-ADVANCE | D2, D3 |
| CT2 | symmetry, conjugation | by averaging | ADVANCE (fit) | none |
| CT3 | tau(v, eta), cutoff-free | Mobius in the support, 6.3, 6.5(b) | CORRECT-NO-ADVANCE | D1, D3, D7 |
| CT4 | real volume bound at one beta | 6.3 | ADVANCE (fit) | D8, local |
| L-adic a, no monotonicity | Text 15, Requests | 6.4(a), (d) | ADVANCE (fit) | settled |
| (RCT5) of Theorem 7.8 | real lower bound | not stated, not claimed | not delivered | none |

## Verdicts: UV-OS (`parts/upper-chain.md` Text 16, clauses in Text 10, 14, 20 to 22)

| Clause | Delivered | Verdict | Defect |
|---|---|---|---|
| (FF_j) | Requests, I(k), with b_0 >= 6 P | ADVANCE (fit) | none |
| (OS_j)(a), (b), (c), (d) | Requests, (2C): xi := b_hat / g centred at V^* | ADVANCE (fit) | none |
| (OS_j)(c') | needs (MD*_j) | not delivered | D4 |
| flow | Prop 8.4: (T2) both directions, (T3) with j = K | ADVANCE (fit) | D8, local |
| (CF_j) (b), (c), (d); (LE_j); (REG_j) | 4.5i, 9.4 | ADVANCE (fit) | none |
| (CF_j)(a), the (K2), (K3) parts | needs (MD*_j), (RAR_j) | not delivered | D4, D5 |
| (GS_j)(a) | Lemma 4.7c | CORRECT-NO-ADVANCE | D6 |
| (GS_j)(b), (d) | Lemma 18.5, Prop 18.6 of the consumer | ADVANCE (fit) | none |
| (GS_j)(c) | stated for n up to L / C only | CORRECT-NO-ADVANCE | D6 |
| (C2_j), (Q_j) | Text 18 of the consumer, given (EI) | ADVANCE (fit) | D9, wording |
| (MD*_j), (SCR_j), (DEC_j) | no statement | not delivered | D4 |
| (RAR^1_j), (RAR^ch_j) | no statement | not delivered | D5 |

## Defects, ranked by what each breaks

**D1. CT3 is derived at sources outside the class of I^w(k).** Attempt lines 1034, 1039 against 1007. *Breaks CT3 as written.*
The Mobius expansion puts a variable s_c on each cube c, so it evaluates E at w|_X and at s w, on the polydisc |s_c w| <= 1 / (2 g^2). I^w(k) is stated for |w| <= rho, Lipschitz with constant Lam. Two failures:
- *Jumps.* w|_X jumps at cube walls. A wall of a level-k cube carries (a_k / a_j)^3 level-j cells at every finer level j, and each has a jump not small in a_j. There the gain Lam a_k of 6.1 items 1, 2 and the term C Lam a_k of item 6 are absent.
- *Radius.* 6.5(b) claims the bound for the R polymers at W = 1 on that polydisc. There the stiffness falls to 1 / (2 g^2). 6.1 item 7 itself says that value "would have used up the whole margin": the factor of Theorem 4.3 becomes (3/2)(1/2) = 3/4, below the 5/4 that (T2) needs.

So the bound on e_k has no derivation. The conclusion is not contradicted.
*Repair, unproved.* Drop the Mobius sum. Add to I^w(k) a clause that a polymer changes by a decaying amount when w changes at distance d, inside the class. Then bound E(w_1 + w_2) - E(w_1) - E(w_2) as a mixed difference in s w_1 + t w_2, |s|, |t| <= 1. Disjoint supports keep this in W, with the same Lipschitz constant, since each w_i vanishes off its support. If the Mobius sum is kept, the class needs jumps on walls, written polymers on walls, and a radius c_0 / g^2 with c_0 <= 1/6, from (3/2)(1 - c_0) >= 5/4.

**D2. The class W is larger than what Text 6.1 treats.** Upper chain line 339 against attempt lines 1007 to 1020. *Breaks CT1 and CT3 on part of W; nothing consumed is lost.*
W may depend on the orientation of p. 6.1 has one scalar w_k(x) per site, and items 2 and 4 use "constant w gives w dF_k". Take w constant with a different value on each plane. Then the first-order term is sum w_(mu nu) dF^(mu nu) . Z, which does not vanish on the slice and has no factor Lam a_k. And Tr[C(W) H^(mu nu)(W)] depends on W, so item 4's "no term of order g^2 w in the marginal part" is false on this part of the class. A scaling check, not gated: a constant relative anisotropy of the couplings is removed in the continuum by rescaling the axes, so it is preserved by the flow. Then w_k tracks u_k, a relative change g_k^2 b log L per level, above the rate g_k^3 p^c of item 6.
*Repair, unproved.* The chain reads only sources sigma_f: Theorem 7.4 and Corollary 7.5 use t sigma_f and images of it, and Text 0 gives sum_p sigma_f(p) s_p = sum_x f(x) e_a(x) exactly. Narrow W to {sigma_f}, with the Lipschitz condition on f. In 6.1 start from f_(0,x) = e_a(x), not f_(0,p) = s_p, which also matches a_(0,x) in (CF_j).

**D3. I^w(k) has a form and no clauses.** Attempt lines 1009 to 1013, 1032, 1034. *CT1 and CT3 read clauses that do not exist.*
6.3 cites "I^w(k)(b)" and "sup |r_K^w| <= exp(C |T_K|)". I(k)(c) has its bound only "for w = 0" (line 325), and 4.7 says r_k^w may vanish (line 759). So no bound on |G_K^w| at a rough W is stated, and CT1 needs one. The displayed form sums w_k(x) f_(k,x) over all x, while the densities are defined through V^* on regular fields; at V with holes it has to be the region density of 4.5i. (2C) says "no linear term, at every W", at w = 0 only, while 6.1 item 2 keeps a linear term at w != 0. So (2C), (GOOD), (R1), (R2), (TAIL) have not been read with a source. The attempt names this as hardest item (3). Its sentence "Nothing changes in UV-CT as stated" (line 100) is true of the wording only. CT4 is at w = 0 and does not depend on this.
*Repair, unproved.* Write I^w(k) as clauses (a) to (d) on the class, with the bound of 3.3(c) at complex w and the sensitivity clause of D1.

**D4. (MD*_j), (SCR_j), (DEC_j) are not delivered, and the two parts disagree about the cost.** Attempt lines 24, 120, 942; upper chain lines 73, 142, 1012, 1268, Text 18 last paragraph. *Breaks UV-OS on this attempt: Lemma 20.5, Theorem 14.1c, Proposition 17.2, (OS_j)(c'), so the field tier and (c') of the milestone chain.*
I(k) is one function of V, with no data label. The attempt says of the label D: "not at reasonable cost, as things stand". The upper chain lists it as an implication and says none of these "looks like a new idea". Neither file has written I(k; D). Three further points:
- The attempt's plan is the relative bound at arbitrary far data, end of 4.9. The fourth form dropped rough data, and asks for regular quiet data only (20.5), so that plan aims at a stronger statement than the one consumed.
- "(RAR_j) and the local parts of (SCR_j), (DEC_j) follow from the gas" (line 120) is at W regular everywhere. (SCR_j) is for conditional copies under nu' in LL_(j+1), which are rough beyond Q'_m.
- The attempt says freezing is "the wrong direction for (4.3') in the denominator". Upper chain Proposition 17.5 says freezing "should only improve". These concern different things, the excess and the coercivity, and neither file settles the first.

*Repair.* The attempt answers the request at upper chain line 142 by item of its 4.8, for quiet data only.

**D5. (RAR^1_j) at the quiet threshold has no producer, and the size quoted for it is short.** Upper chain lines 823, 1019, 1057, 1436; attempt line 419. *Breaks (20.2) below a regular top, and so D4's chain even if (MD*_j) is supplied.*
Proposition 17.4 marks rough cells, with omega_l = exp(-c c_F eps_0^2 x_l). Text 22 needs non-quiet cells, at threshold eps_0 / C_2 = 2 C_s eps_0 L^-2, and the Text 16 row reads such a cell as a mid cube. A mid cube's weight in 4.4 is exp(-p^2 / 3), and p^2 = (log 1/g)^(2 p_0) is polylogarithmic in x_l. The clause needs exp(-8 w_0 lambda_l), with lambda_l = l_0 + l_1 (K - l), linear in x_l by (T3). Since x_l >= 2 gamma^-2 and gamma is last, the mid-cube weight falls short. The attempt has no statement with marks.
*Repair, unproved.* Mark in the noise. Flux above half the threshold forces |xi_c| >= y := c eps_0 / (L^2 C(L) g) in range, whose Gaussian tail is linear in x_l. Read it in xi_eff, centred at the exact mean, not in x, since |s_J| may reach p_2 / 16, which may exceed y. Carry one level of marks through 4.8 to a regular top. (RAR^ch_j), and the case of a stack reaching the top under mu (upper chain 22.4), stay open as listed there.

**D6. (GS_j) as written is not what Lemma 4.7c gives.** Attempt lines 260, 875, 130; upper chain lines 816, 821, 846 to 852, 888, Text 18 last paragraph. *Two clauses fail as stated; on my reading neither breaks a consumer.*
- *(a).* Rem_B holds C(L, M) sup |e| g^eta, with eta = c_3 / (8 c_1) small and no factor of the curvature. Line 816 demands that omega_j beat any power of g_j, and g^eta does not. One symbol is doing two jobs. In (GS_j) and theta_0 only smallness is used, which g^eta meets after gamma. The any-power rate is used through varpi'_j and x_j^2 omega_j in b^new_j, and in the lines I read that omega_j is the rarity P_W(A_c). If the (GS_j) term did reach b^new_j, then x_j^2 g_j^eta would diverge, and sum_j g_j^eta is not finite for eta < 2. I checked Lemmas 14.15 and 14.16 for this, not every later use.
- *(c).* The clause is for any n, and Step 2 of Lemma 14.15 uses it for n > n_L. Lemma 4.7c needs D_e small against L, and Text 18 says "with n up to L / C". The attempt states no moment bound of the energy beyond that.

*Repair, unproved.* Split the symbol: omega^GS_j tending to 0 at fixed L, and omega^R_j, the rarity. Derive (c) at large n from the chart and rarity directly, since no smoothing is needed there.

**D7. The formula tau <= C rho v eta^-4 has a wrong count.** Attempt line 1034; the same count in upper chain Remark 7.6. *Local.*
The number of level-k cells meeting a set of measure v is not v / a_k^4 once a_k exceeds the size of its pieces: N small pieces meet about N cells as v -> 0. Upper chain Text 8 records the same point about measure and neighbourhoods.
*Repair.* Count all cells of Tor: tau <= C rho a_*^4 eta^-4, by the same sum. Only independence of a is consumed in CT3, and v-dependence is not.

**D8. The trajectory is fixed on one torus and consumed on all.** Attempt lines 875, 904, 1120, 1212. *Local.*
(T5) gives g_K = gamma / sqrt 2 exactly for one sequence. CT4 compares tori at one beta, and UV-OS asks uniformity in the torus. Rem_B's term p exp(-c_3 T_(k+1) / 8) and the wrapping polymers make the flow depend on the torus in the last m_* levels. So on another torus at the same beta, g_K differs and g_j <= gamma, the hypothesis of Theorem I, has to be rechecked.
*Repair, unproved.* Fix (T5) on Tor and bound |u_K^(T) - u_K^(Tor)| by (T1) over the last m_* levels, against the margin gamma^-2.

**D9. Stale readings, none breaking a statement.**
- Lemma 18.1's proof puts V_zeta in the curvature class, which 3.3(b) withdrew. The attempt's repair (line 105) holds on my check: at |zeta| <= alpha / (3 (1 + n) f), V_zeta is exp(-Im(zeta) v) times a real field of curvature below alpha, with imaginary part at most alpha per link, inside the tube. It has not been absorbed there.
- Text 18 input (ii) has X at V^*. After (2C), X sits at V^# and the mean is b^*. The linear algebra of Theorem 18.3 reads the same on my reading.
- Lemma 20.3 cites the attempt's 1.1, 1.2 and one delta function per step. The final map of 5.4 is a mixture with choices private to blocks, so WW should carry them as variables.
- Text 7 and `GOAL.md` still say dyadic. Text 15 has the patch.

## What was and was not read

*Read.* `FINISH.md`, `GOAL.md`. In the attempt: state of attack, Obligations, Requests, 1.4, 3.1 to 3.3, 4.4 in part, 4.7 through Lemma 4.7c's statement and part of its proof, the recursion lines around 901 to 904, 4.8, 4.9, 5.4, Text 6, Proposition 8.4, 11.4(e). In the upper chain: state of attack, Obligations and Requests in part, Text 0, 7, 8 statements, Text 10 and 14 clauses, Lemmas 14.15, 14.16 and parts of their proofs, Text 15 last paragraph, 16, 17 statements, 18, 20.3 to 20.5 statements, 21.2, 22.1 to 22.4.

*Not read.* `parts/hard-core--mapped.md`, any `library/` file, any file in `gates/` other than this one, the Sussman-Alpoge repository, or any other AI-written account. The attempt's own library files were not needed. No proof was gated. Lemma 4.7c's proof was read for its constants only.

*Firewall disclosure.* The upper chain's audit tables, Obligations and Text 21 to 23, and the attempt's Requests, carry labels and a few quoted lines of the mapped attempt. I saw them in passing, and I read Text 23.1 for the rules it gives this attempt. Nothing above uses them.

*Numerics.* None run. This item is a statement comparison, and no question here was one a short run would settle. The scaling check in D2 and the size comparison in D5 are by hand.
