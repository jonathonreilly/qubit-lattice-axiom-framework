# T55 pre-registration (written before t55_test.py was run)

Wall: the dark mass 16 v was found by scanning a list of framework numbers for one that makes
eta = C m^2 hit eta_obs; no mechanism. Author: Claude Sonnet 5.5 (same family as the supervisor).

Honest disclosure: before writing this file I had noticed by hand that the freeze-out condition fixes
only the ratio m/alpha_X, and I suspected that (m = 6 v, alpha_X = alpha_2(v)) also lands. So the
"6 v / alpha_2" hit is NOT blind. The counts and base rates below are what I did not know.

Fixed inputs (copied from the bypass note, unchanged): x_F = 25, S = 1.59, R = 31/9 * 1.59, g* = 106.75,
K = 1.07e9, BBN 3.65e7, M_Pl = 1.2209e19, eta_obs = 6.12e-10, canonical surface (P = 0.5934).

## Test A: what does the target constrain, and how strong is the scan?
Lambda* := m_target(alpha)/alpha (a constant, since m_target ~ alpha). Families declared now:
 - F22 = the note's 11 blocks {alpha_LM, u0, pi, 2, 3, N_c, N_sites, hw_dark, R_base, alpha_s(v), dim adj} x {p = +1, -1}.
 - F44 = the same with p in {+2, +1, -1, -2}.
 - A_file = couplings that sit on file: 1/(4 pi) [g_bare = 1], alpha_LM, alpha_s(v), alpha_2(v) at g_2 = 0.65939 / 0.6711 / 0.68283
   (docs/G_2_V_BOUNDED_INTERVAL...), 1/(16 pi) (SU2 lattice anchor), 0.048 (cosmology note alpha_GUT).
 Tolerances: 5 % (the note's) and 10.8 % (the note's own band [3422, 4255] around 3860).
 Random-target null: Lambda drawn log-uniform over a factor-10 window centred on Lambda*.
PASS (the 16 v match carries evidence): P_random(F22, alpha_LM fixed, 5 %) <= 0.05, or exactly one pair
 in F44 x A_file within 5 % of Lambda*.
FAIL (no evidential weight as a mass derivation): P_random(F22, alpha_LM fixed, 5 %) >= 0.10 AND at least
 three pairs in F44 x A_file within 5 % of Lambda*, not counting duplicates of (16, alpha_LM).
Guess before running: P_random about 0.15-0.20; three to six pairs.

## Test B: does the lane's own effective-potential machinery give 16 v?
Build the T1 operator (2^4 block, eta phases, antiperiodic wrap, D = u0 sum eta_mu Gamma_mu), confirm
D^2 = -4 u0^2 I and V''(0) = -N/(4 u0^2). Form the D1 recipe m^2 = |V''|/N v^2 and the two "all-channel
coherent" readings (incoherent sum N kappa, coherent amplitude sum N^2 kappa).
PASS (Origin A survives as a parallel of the Higgs derivation): some reading lies within 5 % of 15.68 v.
FAIL: none does. Guess: none does; the parallel reading is N v/(2 u0) = 9.12 v.

## Test C: the abundance fixes a cross-section
pi/Lambda*^2 in cm^3/s should sit near the canonical thermal value (2e-26). Sanity only.

Nothing in A-C uses any input beyond the repo's; no fitting.
