lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T02:43Z

# Gate: history-budget, pinned at 769697e8d

**Provenance.** anthropic/claude-opus-5-5, effort high, Mac mini worker, commit 769697e8d, 2026-11-01. Neutral side, one reader. The notes' author is openai/gpt-6-astra/max, so this read crosses providers for those two notes. A same-model check is not independent in model and is not an audit, and this report is not independent of any Claude-written statement it reads against. Verdicts steer research and grant no status.

**Routing.** This report sets statements of both attempts side by side, so it must not go to either attempt whole. Independent may receive D1(a), D5, D6 and the reduction below. Mapped may receive D1(b), D2, D3, D4 and the reduction.

## The two questions

**Does the sum really close, with the honest bottom and every source?** Yes, as a conditional implication. I re-derived every row of the source table, the 12x_0 bottom and its x_J/x_0 cancellation, (PATH), (SUM) and (HS-budget), and found no slip. No output hypothesis was used early. It does not close the induction, and the notes say so: K1, K3, z and beta at every vertex are inputs. So (H20.5) is not proved for the actual hierarchy, and (I-K3) remains the first open row.

**Is (FLOW-END) something each attempt can deliver?** One half yes, one half no.

- **Trajectory half** (window, upper growth, lower envelope): yes on both maps, conditional on each attempt's own closure, after the small repairs D4 and D5.
- **Rate half** (alpha, l_1 "within the producer's actual rates"): not yet on either map (D1). The form fits, since both rate statements are linear in x_l. But independent declines these clauses outright, so Lemma HS is not on its chosen route. Mapped has them only conditional on an inequality it reports as not derived.

## Verdicts

| Statement | Verdict | Note |
|---|---|---|
| Theorem GH, section 3 | ADVANCE | Proof stands. Equality reached in T1. |
| (G1), total mark, r^f identity, source table, section 2 | ADVANCE | By hand, and T2 to 4e-14. |
| Pointwise source sizes, sections 1 and 2 | ADVANCE | Conditional on CF and current K1. D3(b) on the domain. |
| Radius lemma and order of constants, section 7 | ADVANCE | Including R_j >= lambda_j + 1 and B_j Phi_j(R_j) <= 1/1024. |
| (GG-prob), (A-count), (A-joint), (PATH) | ADVANCE | Conditional on full (RAR^ch) and output K1, K3. D3(a) is local. |
| Lemma HS, with (SUM), (HS-budget) | ADVANCE | As an implication. D7 is local. |
| (K-transport) and the locality rows, section 4 | ADVANCE | Rows are bounds; their margins are not certified, as stated. |
| Bounded-shell example, section 4 | ADVANCE | Valid against the inference only. T6. |
| (H20.5) for the actual generated family | CORRECT-NO-ADVANCE | No counterexample, but its hypotheses are open. |
| (FLOW-END) as a joint producer clause | CORRECT-NO-ADVANCE | D1. Nothing downstream may read its rate half yet. |

## Defects

**D1. The rate half of (FLOW-END) has no producer value on either map. Breaks the use of Lemma HS, not its proof.**
(a) Independent, Text 6.0 and Requests: "(MD*_j), (SCR_j), (DEC_j), (RAR^1_j), (RAR^ch_j) have no statement here", and Text 4.9 calls the relative large-field bound at arbitrary far data open. Its rough cost exp(-c_F eps_0 Y_k / g_k^2) has the right form, but it bounds a density, not a probability below a regular top. So alpha and l_1 are undefined on this map, and HS, which reads (RAR^ch) below every regular top and under mu, cannot be applied. Its route is UV-CT.
(b) Mapped: the rates z_b = exp(-(1/4) x_k c_S eps_q^2 T^2) and exp(-(1/16) x_k c_T T^2) would give alpha and l_1, but (DM+) rests on (LMK_i), about which `parts/hard-core--dm.md` says "The physical inequality above was not derived". The joint bound under mu, including stacks reaching K, is a proposal.
Repair: none here. This is the producers' main open input.

**D2. "c_* < c_I" understates what (I-K3) forces. Breaks the rate condition in history-budget-sum.md, section 1 and (I-K3), and the sentence at `parts/hard-core--mapped.md:1020`. [Derived here.]** Take regular W, Wtilde agreeing on Q'_m(c') with m = floor(d/2) - 2 in [r', lambda'], so the midpoint is outside the cube and they differ there. (PAIR) makes (I-K3) require |F(W) - F(Wtilde)| <= 4 C_loc U exp(-c_* d) B' Phi'(m), with U = iota x'^(3/2). If the current's size bound C U exp(-c_I d) is saturated by such a pair, this gives (c_* + kappa/2 - c_I) d <= (1/2) log x' + C for d up to about 2 lambda', and so c_I >= c_* + kappa/2 - O(log x' / x'). A current tail at the rate c(L) that mapped prints, below kappa/2 with kappa absolute, would falsify (I-K3) for every c_* > 0 unless the gauge-invariant current decays faster. Mapped's "I have not found a place where a rate below c/L hurts" is therefore out of date. RC-rates asks sigma_v - c_* >= 2 kappa_v, which is consistent with this. Repair: replace c_* < c_I by c_I - c_* >= kappa/2 in the HS table, and have the producer bound the actual endpoint rate of the gauge-invariant current. Unproved.

**D3. The pullback domain n < T/4 is missed outside the current. Breaks (GOOD-v) as written on some tori.** The interface admits T_j far below x_j^2, and MC completes this domain for the current only.
(a) Take T_j = 3 R_j and V regular except one plaquette at distance T_j/2 - 1 from c. Then n_1 > R_j + 3, so V is off A_c, but pi_(n_1 - 1) is undefined and every radius in I_j is at least T_j/4, so GG tests nothing. The bound |x e| <= pol + u/32 has no proof at this V.
(b) (CF_j) defines a_(j+1) on non-regular W through pi'_(n_0 - 1), which is undefined when n_0 - 1 >= T'/4. Then "|A_j| <= C_A x_j on all fields" and the rho, Rem and h recipes are incomplete there.
Repair, unproved but short: if T_j <= 4 R_j + 16, set A_c to "V not globally regular", and (A-count) survives with a larger constant, since T_j^4 <= C (x_j + 2)^8. Otherwise stop the telescoping at the largest n < T_j/4, which lies in I_j. Extend MC to a.

**D4. The mapped flow is cited to the wrong text. Breaks the "window fits" entry for mapped as sourced.** Section 7 cites "Mapped, Text 2, the displayed induction item 3". That is `parts/hard-core--mapped.md:358`, in Text 1, a paraphrase of the Sussman-Alpoge account, which carries no weight here. Text 2.1 says (P1) is unproved there. First passage appears nowhere else in the attempt. Text 5.10 stops at x_(K') = x_*, and `library/dm-stopped-kernel.md:22` takes the lower envelope as a premise. The substance is available: Theorem P1 and the closure conclusion give beta = beta^0 + O(C(L) g^2) + O(x^M z), with beta^0_(l+1) = c_0 + c_l - c_(l+1) and sup |c_l| finite. Repair, unproved: mapped states one lemma giving |beta| <= B, the slope bound with b' = c_0/2 at x >= x_*, and K as first passage above x_*. All of it stays conditional on P1 and the closure.

**D5. "The independent T5 window has x_K = 2X" holds only on Tor. Breaks the window on other tori by at most 1.** Lemma 6.6 fixes g_0 with gamma / 2^(1/2), so x_K = 4 gamma^-2 on Tor, and elsewhere x_K is within 1 of that. With X = 2 gamma^-2, x_K can exceed 2X, and the interface asks for the window on every torus at one bare trajectory. Repair: X := 2 gamma^-2 + 1. Lemma 6.6 covers only tori with 2^m T_K last cells.

**D6. Independent fixes T_K before gamma, which conflicts with Lemma 10.6 at the top levels. Local, and only on the UV-OS route.** Lemma 10.6 asks log(1/g_j) <= T_j, and the interface asks log x_j <= T_j / (5 b_cb^4). Text 3.1 item 9 takes T_K before gamma, so the condition fails at level K for small gamma, and mu rarity through Lemma 10.6 is unavailable on Tor. Repair, unproved: take T_K after gamma, since item 9 says only c reads it. It needs a check that no smallness in Text 6 then reads T_K.

**D7. The list fixing A omits the locality rows. Local.** Lemma HS sets A >= max(32 C_pol C_eta, 8 C_A, 8 C_I, 12). The rows of section 4 also need A large against C_loc J_* and C_A, because their sources are bounded by a fixed constant and compared with U_v. S and N do not depend on A, and C_eta does not once X is large, so adding these terms changes nothing else.

## One reduction, proof here, unchecked and not run

The sum does not need the full (RAR^ch). Let D = N exp(B/(2Y)) and s_0 = ceil(8 log D / l_1), fixed before X. In (PATH), for a >= s_0, use the deepest s_0 levels of the path in place of the finer half. Then the A term is at most exp(-s_0 lambda_J - s_0 l_1 (a - s_0)), so its fourth root times D^a is at most D^(-a) exp((s_0^2 l_1 - s_0 l_0)/4). For a < s_0 use all a levels, which costs exp(-a l_0 / 4). The GG term only improves. So (HS-budget) survives with joint rarity on s_0 consecutive levels. This is the "fixed number of levels" of Text 22.4, there marked not developed, and it weakens what a producer must supply. It does not supply it. T3c shows that one-level rarity alone does not suffice.

Also, l_1 does not appear in E_*(X): the depth series is paid by l_0 and by y^(3/2), and l_1 is needed for the radius lemma and the floors.

## Checks

`checks/gate_hb/`, criteria in `REGISTRATION.md` before each run. All of this is abstract arithmetic and finite probability. Nothing bounds Yang-Mills or tests any hypothesis of Lemma HS.

| Test | Result |
|---|---|
| T1, GH on 4000 random chains, q = 1, 2, 4 | PASS, largest excess 2e-16, ratio reaches 1 |
| T1c, control, product of marginals | PASS, 36 violations, as a wrong bound should give |
| T2, source table and identities | PASS, error 4e-14 |
| T3, scalar sum on a grid | No exceedance, which meets the registered criterion. The script printed `pass: false` on a floor of 100 points that I had not registered: only 32 were admissible. |
| T3', wider grid | FAILED as registered: no exceedance on 1872 points, but 0 points near the edge of the series, so the edge was untested |
| T3'', parameters solved onto the edge | PASS, 576 points, no exceedance |
| T3c, control, one-level rarity | PASS, the direct sum blows up |
| T4, T4c, radius and controls | PASS, 0 failures; both controls fail as they should |
| T5, (K-transport) in a finite model | PASS, but the largest ratio is 0.19, so it is far from tight |
| T6, bounded shell | PASS at x = 150, 200, with ratios 3.3 and 303; at x = 100 the ratio is 0.06 |

The X needed for right side <= 1/2 is about 4e10, 3e14 and 3e18 at three sample constant sets of my own choosing, which carry no physical meaning. The chain sets no upper limit on X, so size alone is no objection.

## Read and not read

Read: `library/generated-observable-history.md` and `library/history-budget-sum.md` whole; upper-chain The interface, Texts 0, 10.6 (statement), 14 (class, clauses, 14.15 statement, 14.16, 14.13), 20.4, 21.1, 21.2, 21.7, 21.8, 22; independent Text 3.1, Proposition 8.4, Lemma 6.6, Requests, 6.0; mapped Texts 1, 5.9, 5.10 and the flow lines; `parts/hard-core--dm.md:60-84`; parts of `library/current-locality-reduced-law.md`.

Not read: the proofs of any rarity, closure or I(k) statement, Lemma 14.15's proof, the section of the current note on the proof of RC + MC => I-K3. The margins of Text 21.7 were not re-derived for the weighted rows; I checked only that their constants are fixed before X. Numeric lock held for each run; memory 64 to 68 percent free.
