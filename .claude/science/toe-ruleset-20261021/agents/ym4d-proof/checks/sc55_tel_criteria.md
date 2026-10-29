# sc55_tel — criteria (pre-registered before the script exists)

Written 2026-10-29 (UTC) by the SRCCD55 worker (claude-opus-5-5), before `sc55_tel.py` exists.

## What is tested
The exact "telescoping conditional covariance" identity used in SRCCD55 (Proposition B): for a chain whose joint law is
p(u_0, …, u_K) ∝ w_0(u_0) Π_{i<K} K_i(u_{i+1} | u_i) (each K_i a stochastic kernel in its first argument, as the
normalised soft kernels of the lane are: ∫K_i(U_{i+1}, U_i) dU_{i+1} = 1), and fine observables G, H of u_0,

    Cov(G, H | U_K = u_K) = Σ_{i=0}^{K-1} E[ Cov(G_i, H_i | U_{i+1}) | U_K = u_K ],   G_i := E[G | U_i].

Model: K = 3, state spaces of sizes (4, 3, 3, 2) for (u_0, u_1, u_2, u_3); w_0 and kernel entries are random positive
rationals (integers 1..9, kernels normalised by row); G, H random rationals with numerators in -9..9. All arithmetic in
`fractions.Fraction` (exact). Fixed seeds; 25 random chains.

## Pre-registered criteria
- **T1 (identity).** In every one of the 25 Markov chains and for every value u_3, the two sides agree EXACTLY.
  PASS iff 25 × 2 = 50 exact equalities.
- **T2 (Markov property, the input that makes G_i a function of U_i alone).** In every chain and every configuration,
  E[G | U_i = u_i, …, U_3 = u_3] = E[G | U_i = u_i] exactly, for i = 1, 2, 3. PASS iff all equal.
- **C1 (control; must FIRE).** 25 random NON-Markov chains: K_1 depends on (u_1, u_0) and K_2 on (u_2, u_1, u_0) (still
  normalised). The Markov-form right-hand side (with G_i := E[G | U_i]) must DIFFER from the left-hand side in at least
  one chain. FIRES iff at least one inequality is found.
- **C1b (the general martingale form still holds there).** In the same non-Markov chains, the right-hand side with
  G_i := E[G | U_i, U_{i+1}, …, U_3] (the tail sigma-algebra) equals the left-hand side exactly in all 25 × 2 cases.
- **C2 (control; must FIRE).** Dropping the i = 0 term in the Markov chains must break the identity in at least one chain.
- **Verdict.** PASS iff T1 and T2 PASS, C1 and C2 FIRE, and C1b holds. Anything else is FAIL, reported as such.
