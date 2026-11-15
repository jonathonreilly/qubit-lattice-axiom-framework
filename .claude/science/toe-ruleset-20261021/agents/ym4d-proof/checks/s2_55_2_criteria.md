# s2_55_2 — criteria (written before the script; SPHERE2_55 §2.2-§2.3). Exact rational arithmetic (fractions) only.
Objects: a 3-level chain U0 -> U1 -> U2 (state spaces of sizes 4, 3, 2) with joint law p(u0) K0(u1|u0) K1(u2|u1),
rational, normalised (sum over the output of each kernel = 1). F, S (the "seam flux") and X are functions of U0.
Claims under test (exact identities / inequalities of SPHERE2_55):
- (TOWER) E[X|U2] = E[ E[X|U1] | U2 ] and, for every constant c, max_v |E[X|U2=v] - c| <= max_u |E[X|U1=u] - c|.
- (PB) Proposition B on the chain: E Cov(F,S|U2) = E Cov(F,S|U1) + E Cov(F1,S1|U2), F1 := E[F|U1], S1 := E[S|U1];
  total covariance: Cov(F,S) = E Cov(F,S|U2) + Cov(E[F|U2], E[S|U2]).
- (TOP) the top-level product bound: E|Cov(F1,S1|U2)| <= ||F1 - EF||_{L2} * max_u |S1(u) - c| for every c.
- (COARSE) |Cov(E[F|U2], E[S|U2])| <= ||E[F|U2] - EF||_{L2} * max_v |E[S|U2=v] - c| for every c.
L2 norms enter squared: an inequality A <= sqrt(B)*C (A, C >= 0) is tested exactly as A^2 <= B*C^2.
Gates:
- G1 (TOWER) holds exactly on 3 chains and for every c in {-2, -1, -1/2, 0, 1/3, 1, 2} (and c = EX). PASS iff all hold.
- G2 (PB) both identities hold exactly on the 3 chains. PASS iff exact.
- G3 (TOP) and G4 (COARSE) hold for every c in the grid on the 3 chains. PASS iff all hold.
- Non-vacuity: on at least one chain E|Cov(F1,S1|U2)| > 0 and max_v |E[X|U2=v] - EX| > 0.
Control Y1 (must FIRE): a NON-Markov law q(u0,u1,u2) = p(u0) K0'(u1) K'(u2|u0) (U1 independent of U0, U2 depending on U0
directly): then E[X|U1] = EX for every u1 while max_v |E[X|U2=v] - EX| > 0, so (TOWER) fails at c = EX.
What this check cannot decide: anything about Yang–Mills; it certifies the algebra of the tower lemma and of the
N5' decomposition on exact finite chains, and that the Markov property is load-bearing.
VERDICT PASS iff G1-G4 PASS, non-vacuity holds, and Y1 FIRES.
