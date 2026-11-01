lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T18:04Z

# Gate: closure, H(k) implies H(k + 1), `library/one-step-closure.md`, with Prop DS, (SRC), (LIFT-I) of `library/sector-values.md`

**Provenance.** anthropic/claude-opus-5-5, effort high, Mac mini worker, fresh session, mapped side of the firewall, statement pinned at bad958abb. The text under review was written by the same model, so this is a same-model check: not independent in model, and not an audit. Verdicts steer research and grant no status.

## Verdicts

| Statement | Verdict | Basis |
|---|---|---|
| H(k) implies H(k + 1), Section 10 form | **CORRECT-NO-ADVANCE** | No counterexample. Step B rests on Lemma EX2 (D1); the rarity rows are unavailable (D9); as stated it is not a one-step implication (D3). Nothing downstream may rest on it. |
| (CS) and its derivative form | ADVANCE | Exact identity, rechecked term by term, given V^* exists on D_{j+1}. |
| Section 4, orders 5, 6 | ADVANCE, given its labels | Chain-rule count, weight and partition terms check. K1: no power of L in the top coefficient at U = 1. Defect D5 is local. |
| Section 10, order of constants | ADVANCE, after D2's repair | No circle: B_1, B_2 <= C_low (1 + g^2 B_6), B_6 <= C(L, a_*)(1 + B_2), closes for x >= x_*(L, a_*). |
| Prop DS | **CORRECT-NO-ADVANCE** | Scale counts and Hoelder steps check. It reads Lemma EX2, unchanged since gate 7c12c6981, and omits the same transport terms. |
| Interpolation, orders 3, 4 (3B, Step B') | **CORRECT-NO-ADVANCE** | The proof fails four ways (D2). Bounds of the same form hold: **Lemma FP, proved here,** `library/far-pair-interpolation.md`, replaces the step, at rates mu/4, mu/6, not the stated mu/2, mu/4. Its last absorption is not displayed. |
| (Loc^c) by a "direct" sum (3B) | CORRECT-NO-ADVANCE | No sum over levels is written (D7). Section 5's recursion stands once Lemma FP removes its circle. |
| (SRC), with O1 to O3 | ADVANCE, on inputs at their labels | Every step checked; no failure found. Theorem F-D on the staircase, HS-P, HS-T unread, ungated. No test in SU(2) or d = 4 in any sector. |
| (LIFT-I), one level | ADVANCE | Steps stand as a derivation at the level of each term. "Tails" is undefined and the Weitzenboeck step is a count. |
| (LIFT-I) at n := k, (COMP)(ii) | ADVANCE, local repair unproved | Step 5 fails as written at depth (D4). The statement holds on K2's fields. |

**No WRONG.** No conclusion is false as written, so far as this read reaches. The numerics find nothing against the closure, and they do not prove a bound.

**What would raise the top verdict.** A rewritten Lemma EX2 that survives a gate, plus Theorem Z. Then the closure stands given its labels, with D2 to D8 as edits.

## Defects, ranked by what each breaks

**D1. Step B rests on a lemma not available. Breaks B_1, B_2, so the closure.** `library/sector-values.md:167`, `:173`. `git diff 7c12c6981 bad958abb` is empty on this file, so D1 to D3 of `gates/lemma-ex-7c12c6981.md` all stand: d_{V'} delta F bounded in the wrong norm, omitted terms, b_m with no gauge. Prop DS has the same two gaps of its own: "link size |delta F|" at `:173` is that D1 again, and the variation of the transports in Delta_y F is not written. Those are size |h| |F| |Delta delta' F|, which sum geometrically by Hoelder and Sobolev if D1's repair holds. The sum over m reads only the l^1 sum of b_m. *Repair:* queue item 7. Nothing here discharges it.

**D2. The interpolation fails as written, in four independent ways. Breaks B_3, B_4. Repaired: Lemma FP.** `library/sector-values.md:175`.
(a) *No closure.* D^3 is bounded by t D^4 and D^4 by D^3 / t at one step t. Substituting: B_3 <= 2 S / t + (t/2)(2 B_3 / t + t B_5 / 2) = 2 S / t + B_3 + t^2 B_5 / 4. The coefficient of B_3 on the right is exactly 1.
(b) *A circle.* It reads (Loc^c) at order 2, with a constant "which the same sum gives". No such sum is written (D7). The written proof is Section 5, where D_2 = 2 C_2(L) B_3, so B_3 <= C T_2^-1 C_2(L) B_3. "Likewise D^4" needs (Loc^c) at order 3, where no sum exists, as hostile (17) says.
(c) *Rates.* Hostile (13) puts (Loc^c) at mu_c(L), falling with L. So orders 3, 4 would have rates mu_c/2, mu_c/4, not the mu/2, mu/4 stated, and "a lift multiplies a rate by L" gives L mu_c/4, which nothing bounds below by mu. HS-T's input rate and Step C both read that.
(d) *Domain.* V e^{t b} with t = T_2 leaves D_k at any V at the edge of the class.
*Repair, proved here:* D^n Z is symmetric, and a tuple of n bonds has tree <= (n - 1) Delta, with Delta its largest pair distance. So put the far pair in the two slots of D^2, which is small at every field, and difference in the other slots. No locality in the field is read. Rates mu/4, mu/6. Domains: orders 1, 2, 5, 6 on an enlarged D^+, orders 3, 4 on D_k.

**D3. As stated it is not a one-step implication, and H(k) is out of date. Breaks the statement, not the mathematics.** `library/one-step-closure.md:27`, `:29`, `:9`. Step B and (VAL) sum over all j < k, so the induction is H(j) for all j <= k implies H(k + 1). H(k) still lists c^(m)(R_k), which Section 10 stops proving, and omits ||R_k||_n for n <= 4, which Step C reads. Section 1 orders B_n(L) before x_*, though B_5, B_6 now depend on a_*. *Repair:* hypothesis H(j), all j <= k, with ||R_k||_{1, 2, 5, 6} <= B_n on D^+ and ||R_k||_{3, 4} <= B_n on D_k at rates mu/4, mu/6; drop c^(m); B_n(L, a_*). The base H(0) has R_0 = 0.

**D4. LIFT-I Step 5 fails at depth, when read at n := k as Section 3A (a) directs. Breaks the stated proof of (COMP)(ii), not the bound. Repair in hand, unproved.** `library/sector-values.md:100`, `:110`. Step 5 bounds the non-abelian remainder by AN1. AN1 has e_j(b) := ||H||_{L^4(b^+)} in one gauge, and (1) of `library/analytic-lift.md` gives sum_c e_j(c)^4 <= C ||H||^4_{L^4(box)}, with no factor s. Claim needed: at most C s^2 I_k.
*Concrete failure:* constant non-commuting links of size h, so f = h^2 and I_k about f^3. In the best gauge on the top box ||H||_{L^4(box)} is about f, so the proof gets C_2^2 f^4 per box at every level, against the target s^2 f^3: off by C_2^2 f s^-2, growing as L^{2 m}. Summed over m, the proof's bound grows linearly in k. K2 finds the true ratio level, 0.80, 0.86, 0.89 at m = 0, 1, 2, so the statement is fine and the proof step is what fails. At m = 1 it passes for a_* small in L, which is why the one-level form looked closed.
*Repair, unproved:* apply AN1 on each level-j block in a lattice Uhlenbeck gauge of that block, `library/lattice-uhlenbeck.md`, at U_0 = 1. Then e_j(c) <= C ||F||_{L^2(c^+)} <= C s ||F||_{L^4(c^+)}, so sum_c |r_c|^2 <= C C_2^2 s^4 f^4, below s^2 f^3. AN1 is read per block, which its proof allows, as each constraint reads only its block. The bound (ii) also drops the "tails" of LIFT-I; it should carry the toron term.

**D5. HS-T's second tier decays more slowly than the norm asks, at orders above 2. Local.** `library/one-step-closure.md:13`; `library/preconditioned-covariance.md:110`, `:112`. HS-T gives rate rho_s'/b, with rho_s' = rho_s/4 = mu_s, so mu_s/6 at b = 6. The norm divides by Phi_k(tau/2), rate mu_s/2. The ratio grows as e^{mu_s tau/3}. The first tier has the factor 4 N in mu and does not fail; the second was given no N. *Repair:* mu_s := rho_s/(2 N). I found no other reader of the value; y_* moves. If the slow input of mismatch 1 must keep rate rho_s per box, this asks L >= 12.

**D6. Step A states the wrong size and the wrong object. Local.** `library/one-step-closure.md:150`, hostile (18). Prop DS needs zeta_j rooted at x in tree-decay norm, from Lemma O1, not ||Z_j||_{<= 4}. And the size omits the cumulants, C(L) g_j ||R_j||_{<= 4}, Text 5.9. So ||zeta_j||_{<= 4} <= C(L)(1 + g_j B_{<= 4} + g_j^2 B_6). This closes as before, as x_* comes last. Hostile (11)'s claim that C(L) reads B_n only through g^2 B_n holds for n <= 4 only: the gain costs two orders, so O1's range n <= N - 1 is one too many for that claim. Nothing reads that range with the gain.

**D7. (Loc^c) "direct" has no proof. Local given Lemma FP.** `library/sector-values.md:179`. Each term Z_j o Lambda_m is local, but the sum runs over all m, and the top-cell kernel of Lambda_m has no gain in m. So what is available is sum_m min(u_m, epsilon), with sum u_m bounded. With no rate on u_m this has no decay in epsilon. It would need a geometric tail of b_m. *Repair:* use Section 5's recursion, which Lemma FP frees of its circle. Keep Phi there at rate mu_c(L). If a direct proof is wanted: hole-filling on the partial sums of (TS), T_{m + 1} <= q T_m, is a route, unproved.

**D8. Section 3's display counts the mean twice. Cosmetic.** `library/one-step-closure.md:52`: "(R_k o V^*)_mean" and G_1, which Section 4 says contains <R_k o Phi>. Read (CS) instead, which is unambiguous.

**D9. What the rows of the table rest on, at this pin. Not a defect of the note.** Rarity and Theorem Z: gate 60036ba4d found Lemma OC wrong and Theorem Z CORRECT-NO-ADVANCE; Lemma OW has replaced OC, ungated. (F2) is open, queue item 8. Theorem F-D is not written on the staircase pattern by pattern, hostile (3). Prop AN3, HS-T, (R3) are ungated.

## Numerics (`checks/gate_cl/`, criteria in `CRITERIA.md`, written before any run)

**K1, kernel of Section 4 at U = 1, d = 4.** V1, V2 PASS: Fourier lift against a dense constrained minimiser at N' = 2, L = 3, plaquette angles to 2e-14. The first V2 run failed on a normalisation of the unit bond, a script bug, fixed before any result. **Registered criterion on the first run: FAIL at R = 1, local power 0.27 against 0.25,** but its two largest L sat on different tori, N' = 6 and 4. Follow-up on one torus, added after that result:

| L, N' = 4 | 5 | 7 | 9 | 11 | 13 | local power 11 to 13 |
|---|---|---|---|---|---|---|
| L S_row, R = 1 | 8.67 | 9.00 | 9.14 | 9.22 | 9.26 | 0.03 |
| L S_row, R = 2 | 11.89 | 12.46 | 12.72 | 12.86 | 12.94 | 0.04 |
| S_col / L^3, R = 2 | 8.32 | 8.56 | 8.67 | 8.74 | 8.77 | 0.02 |

At N' = 6, R = 3, L = 3, 5, 7, 9: L S_row = 11.3, 12.9, 13.5, 13.7, S_col / L^3 = 9.2, 9.9, 10.3, 10.4. Composite, L = 3, fine two levels down: 6 to 9 percent above one level. **So at U = 1 the top coefficient has no power of L, and C_1 is about 14.** With these values kappa_5 <= 1/8 asks L_0 of about 3e6, and kappa_6 about 6e3. Limits: abelian, U = 1, Landau with x' cut at R and not the weighted gauge, so no statement at a background, and a log is not resolved.

**K2, (COMP)(ii) in SU(2), two levels, reanalysis of logs of `checks/gate_ex/`.** PASS: R_m = a_m / (s^2 I_top) = 0.80, 0.86, 0.89 and 0.80, 0.87, 0.90 on constant non-commuting links, 0.97, 5.5, 8.3 on const plus wave, all below the cap of 25. Weak: k = 2, N' = 2, L = 3, three fields not chosen for this test.

No charged field was tested, and SU(2) at three levels was not attempted (`gates/lemma-ex-7c12c6981.md`: about 7 GB). The lock was held for K1 only and is released. Memory was 65 to 68 percent free throughout, so nothing was skipped.

## Read and not read

Read: `FINISH.md`, `GOAL.md`; `library/one-step-closure.md` in full; `library/sector-values.md` in full; `library/analytic-lift.md` in full; HS-T in `library/preconditioned-covariance.md`; "The induction, restated" in `library/quiet-boundary-rarity.md`; the head of `library/lattice-uhlenbeck.md`; Text 3.1, Lemma 3.4, Text 5.5, Text 5.9 of `parts/hard-core--mapped.md`; `gates/lemma-ex-7c12c6981.md`; the verdicts and first defects of `gates/theorem-z-repaired-60036ba4d.md`; `checks/gate_ex/ex_core.py`, `y_ex2.py`.

Not read: `parts/hard-core--independent.md` and any gate on it (file names appeared in listings; no contents opened); the Sussman-Alpoge repository; Theorem F-D, Lemmas HS-P, HS-C, O3's inputs in `library/fibre-propagator.md`; `library/relative-density-bound.md`, `polymer-covariance.md`, `twisted-order-calculus.md`, `composite-adjoint.md` beyond grep lines; Sections 6 and 7 of the boundary-data argument were read and not attacked, so (VAL^𝔡) and Delta R carry no verdict here. Whether rho_f <= delta_#, which HS-T's first tier needs, was not checked.

New file: `library/far-pair-interpolation.md` (Lemma FP, proved up to one standard absorption not displayed, same-model, not reviewed).
