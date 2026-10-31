# sm55_2 — criteria (written before the script; SEAM55 §2.1-§2.3: the coarse-image two-scale bound and
# "conditional decay alone does not make the seam term vanish")

Written UTC 2026-10-29 (stamped by `date -u` in the command that created this file), before `sm55_2_model.py` exists.
Exact arithmetic only (sympy rationals and sqrt(3) as an exact algebraic number); no floats in any verdict.

Model (extends CODEX_REVIEW_SPHERE Finding 12's bounded-coarse Gaussian blocks; not a Yang-Mills model).
Coarse variable X uniform on {0,1,2}. Three disjoint blocks B, C (observable side) and D ("seam slab"), each of
M cells; in every cell an independent fine variable xi with E xi = E xi^3 = 0, E xi^2 = 1, E xi^4 = 3, independent
of X. Cell field H = A xi + X; block composite O_Y := M^-1 sum_{i in Y} (H_i^2 - E H_i^2). The "lattice" family is
A = n^2, M = n^4 (n -> oo is a -> 0). Observable F := O_B O_C (centred product of separated smearings, as in
SPHERE55 §3.3). Seam functionals J_tau := O_D - (1 - tau)(X^2 - E X^2), tau in [0,1] (tau = 1: untreated
"opaque" seam whose coarse image oscillates; tau -> 0: transparent).

Closed forms to be established (and cross-checked by exact enumeration at M in {1,2}, A in {1,2}, with the
three-point law xi in {-sqrt3, 0, sqrt3}, probabilities 1/6, 2/3, 1/6, which has the required four moments):
- K1  E[O_Y|X] = X^2 - m, m := E X^2 = 5/3;  Var(O_Y|X) = (2A^4 + 4A^2 X^2)/M.
- K2  Cov(O_B, O_C) = Var(X^2) = 14/9 (non-vacuous separated covariance at normalization Z_e = 1, all n).
- K3  Var(F) = E[(Var(O_B|X) + (X^2-m)^2)^2] - (E[(X^2-m)^2])^2; at A = n^2, M = n^4 its leading term is 4 n^8.
- K4  E[F|X] = (X^2-m)^2 (independent of n); ||E[F|X] - E F||_2^2 = Var((X^2-m)^2) (independent of n).
- K5  Cov(F, J_tau | X) = 0 for every X (perfect conditional decay: disjoint blocks are conditionally independent).
- K6  Cov(F, J_tau) = tau * E[(X^2-m)^3] = tau * 70/27.

Tests (PASS iff exactly true):
- T1  K1-K6 hold symbolically in (A, M, tau) and agree with the exact enumeration at the four (M, A) points
      (K3, K6 checked at the enumerated points through their M, A forms).
- T2  Corrected bound (SEAM55 Lemma 3.5'):  |Cov(F,J)| <= sup_X |Cov(F,J|X)| + ||E[F|X]-EF||_2 * inf_c sup_X |E[J|X]-c|
      holds for tau in {1, 1/2, 1/10, 0} and its right side is independent of n.
- T3  Uncorrected bound (SPHERE55 Lemma 3.5 at s = l_0, with E6's coefficient 1):
      sup_X|Cov(F,J|X)| + sqrt(Var F) * inf_c sup_X|E[J|X]-c|  is >= 2 n^4 * (7/6) tau for every n >= 1 (grows like
      n^4 for any fixed tau > 0): it is valid but not n-uniform, i.e. useless as a -> 0 at a non-vacuous normalization.
- T4  The seam functional's own variance Var(J_1) grows like 2 n^4 (lattice-scale slab fluctuations), while
      Cov(F, J_1) stays 70/27: the slab's fine variance does not control the separated covariance.

Controls (must FIRE):
- Y1  "Decay alone suffices" — the bound |Cov(F,J)| <= sup_X |Cov(F,J|X)| — FAILS at tau = 1 (left 70/27, right 0).
- Y2  A coarse-image bound that drops ||E[F|X]-EF||_2 for the deterministic constant 0 (i.e. claims Cov(F,J) = 0
      whenever the conditional covariance vanishes and E[F|X] is bounded) fails at tau = 1.
- Y3  Breaking conditional independence (block D := block B, J := O_B) makes Cov(F, J|X) nonzero for some X
      (conditional decay genuinely absent), so the first term of T2 is not identically zero in general.
- Y4  The enumeration cross-check is sensitive: replacing E xi^4 = 3 by a two-point law (xi = +-1, E xi^4 = 1)
      changes Var(O_Y|X), so K1's closed form fails for that law.

Verdict: PASS iff T1-T4 hold and Y1-Y4 fire. Scope: decides the logical structure of SEAM55's corrected two-scale
bound and of the "decay is not transparency" statement in an explicit model satisfying bounded coarse backgrounds
and a non-vacuous separated normalization. It decides nothing about Yang-Mills or the actual seam.

## Erratum to these criteria (appended before `sm55_2_model.py` exists; stamped by `date -u` in the same command)
- K2's value "14/9" is an arithmetic slip. X^2 takes 0, 1, 4 with probability 1/3 each, m = 5/3, E X^4 = 17/3,
  so Var(X^2) = 17/3 - 25/9 = 26/9. K2 is to be tested with **26/9**. Nothing else changes.
- Note on T3 (no change): inf_c sup_X |tau (X^2 - m) - c| = 2 tau (half the range 4 of X^2 - m), and
  sqrt(Var F) >= 2 n^2... no: sqrt(Var F) >= 2 n^4 because Var F >= E[Var(O_B|X)^2] - (26/9)^2 + ... >= 4 n^8; the
  printed lower bound 2 n^4 (7/6) tau is therefore weaker than the true 4 n^4 tau and remains a valid test as written.
