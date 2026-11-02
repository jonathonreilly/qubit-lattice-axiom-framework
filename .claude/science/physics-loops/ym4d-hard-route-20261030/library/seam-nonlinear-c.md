lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T20:46Z

# seam-nonlinear-c: nonlinear (NL-pay), (PATCH) and (GLUE-E) at the flat background

Queue row 61, mapped side. Pinned at commit 9793658b6. Author: Anthropic
claude-opus-5-5, effort max, Mac mini worker, 2026-11-02. Same-model work:
not independent in model, not a gate, not an audit, no status.

Status: in progress; sections are written as they are finished. The result
summary at the top is filled in last.

## 1. The statement tested, and criteria fixed before any computation

**Setting.** As in `library/seam-quadratic-c.md` Sections 1 to 5: fine
lattice of unit spacing, L odd, depth n, B = L^n, Q_n, Q_path^(B), C_B, the
tensor maps R, T, Pi and the tensor homotopy h. As in
`library/seam-nonlinear.md` Section 2: a(P) = 1 - Re tr(P)/2, |Z|_F^2 =
tr(Z*Z)/2, (ALIGN) and (SEED). As in `library/seam-nlpay.md`: (PATCH), the
locked pair (PAIR), (LOCK). As in `library/excess-shell-end.md` 4.2: the
replacement cost R_D and (GLUE-E). **Flat background** means: the terminal
parent V has flux at most f <= T_2, with T_2 chosen after L; U is the class
minimizer of the terminal-parent problem with parent V (no frozen fine
links); T is the iterated trial of `parts/hard-core--excess.md` 2.3, with
M_n(T) = V. Top units have side B; for a fine 1-form h, H := B h is its top
normalization, so that, by (SCALE) of `seam-nlpay`,
sum_b |h_b|^4 = ||H||_(L^4)^4 and B^-2 sum_b |h_b|^2 = ||H||_(L^2)^2.

**Questions (queue row 61).**
- Q1. Does the path-gauge primitive H = hG with the chain-map right inverse
  T_n remove the transition-gauge term of (PATCH)?
- Q2. Do they pay the fourth-moment term of (SEED)?
- Q3. Are the remaining nonlinear errors of relative size C(L) x flux,
  uniformly in depth, so that the flux threshold chosen after L absorbs them?
- Q4. (GLUE-E) with exact parent preservation and class membership at every
  intermediate level.

**Registered criteria for the kill test (written before any run).**
1. Identities. Every exact identity used by the hand lemmas below (for the
   locked-pair field H_0 of `seam-nlpay` Section 4: Q_path H_0 = 0,
   G := dH_0 has dG = 0 and C_B G = 0, and hG = H_0 - d(h H_0)) must hold
   to relative error 1e-10. A failure above 1e-8 means a hand step is wrong
   and stops this item there.
2. The claim under test: *the path-gauge primitive is critical*, that is
   sum_b |hG(b)|^4 <= C ||G||_2^4 with C free of B, for closed G with
   C_B G = 0. This is what paying the fourth moment of (SEED) from energy
   alone needs. Record rho_4(B) := sum_b |hG(b)|^4 / ||G||_2^4 and
   sigma_4(B) := sum_p s_p(hG)^4 / ||G||_2^4 for G = dH_0, H_0 the locked
   pair oriented along the first tensor axis, for B = 3, 5, 7, 9, 11 and 13
   if memory allows. REFUTED if rho_4 grows by more than a factor 2 from
   B = 3 to the largest B with log-log slope at least 0.7 over the last two
   points. If it does not grow, the hand lemma of Section 2 has an error and
   I stop to find it. Control: the same pair oriented along the last tensor
   axis must stay bounded (slope below 0.3 over the last two points), and
   the natural representative H_0 itself has sum |H_0|^4 / ||G||^4 = 2/144.
3. What a run can and cannot show. A growing ratio on one explicit field
   only confirms a lower bound that is proved by hand in Section 2. A
   bounded control proves nothing. No statement below rests on a run.
