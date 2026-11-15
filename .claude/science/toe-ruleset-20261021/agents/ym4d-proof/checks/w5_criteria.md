# w5 criteria (lane H session 5; written BEFORE checks/w5_crc2t.py)

Informational check, never a proof. Three parts. Each criterion is PASS/FAIL as stated; OVERALL PASS iff all pass.
Recorded inputs (quoted from RLARGE l.612, PLD §16.8): a = 1.0e-86, beta_- = 0.186, L = 3, a_ret = 2.0e-91, g_K^2 ceiling
1e-94 ((RLF-delta)). Symbolic node-A constants are scanned: c_A in {0, 1, 100}, C_l = C_A in {1, 1e6}, R in {0, 10}; c_U = 1.

## A. Arithmetic of the activity smallness of Theorem CRC-2T (HW §30.4, §30.6), exact integers + log space (mpmath, 50 digits)
- A1: b_n := 531441*38418*c_+ + 38417*c_U and b_D := 38416*(531441*c_+ + c_U), c_+ = c_A + c_U, are recomputed from their factors
  (6561 = 9^4, 81 = 3^4, 38417/38416 from H-geo (iv)); g2_CRC := a/(b_n + a*R + log(12800*C_l)). PASS iff for every scanned
  (c_A, C_l, R): g2_CRC * c_+ lies in [4.0e-97, 5.5e-97] (the hand value of §30.6: 4.9e-97/c_+).
- A2: at g_K^2 = g2_CRC/2 and n_sharp := max(ceil(b_D/(a*beta_-*log L)) - 1, 2e87): log(eps_2) <= log(1/2) AND (S1)
  log(Delta_rho^2 * x_*) <= log(1/2) with rho = 8, c_att = 1 + 153664*8, a_A = a. PASS iff both hold at every scanned point.
- A3 (negative control): at g_K^2 = 1e-94 (the recorded ceiling) (S2) must FAIL (log eps_2 > 0) at every scanned point.
  PASS iff it fails everywhere (a failure of the control to fail is a FAIL of A3).
- A4: n_T := b_D/(a*beta_-*log L). PASS iff n_T / c_+ lies in [5e96, 2e97] at every scanned point.
- A5 (comparison, not route): g2_ret := a_ret/(c_+*c_att + log(2*Delta_rho^2*C_A)). PASS iff g2_ret*c_+ lies in [1.0e-97, 2.0e-97]
  for c_A >= 1 (the §30.6 value 1.6e-97/c_+); report c_A = 0 as well.

## B. Lemma SH-att (HW §30.2), exact shadows on Z^4, L = 3, rho = 8, levels r = 1..M with M = 10
Shadows: Sigma(X) := N_1(pi(X)) (pi = floor division by 3 coordinatewise, N_1 = l-infinity radius-1 neighbourhood);
sh_{j+r}(X) := Sigma^r(X); ||X||_sh := |X| + sum_{r=1..M} |sh_{j+r}(X)|.
Samples: P a random *-connected set of 1-6 cubes; Y built by attaching cubes one at a time, each at l-inf distance in [1, 8] from
a random earlier cube of P u Y (so Y is rho-attached), |Y| in 1..8; at least 150 samples; seeded.
- B1: PASS iff ||P u Y||_sh <= 6561*||P||_sh + c_att*|Y| on every sample (c_att = 1 + 153664*8).
- B2 (sharper, informational but pre-stated): the excess e := ||P u Y||_sh - ||P||_sh satisfies e <= c_att*|Y| on every sample.
  PASS iff 0 violations.
- B3 (negative control: detachment restores a depth term): a single cube y at l-inf distance 3^(M+2) from P (never merges
  within M levels). PASS iff excess(M=10) >= 81*9 and excess(M=10) - excess(M=5) >= 81*4 (a depth term that grows linearly).
  [Pre-script edit: an unfinished alternative wording of B3 was removed before any script existed.]

## C. Two-level monotone toy gas (exact enumeration): the step containment and the two-species activity
Model: level 0 = ring of 12 sites, defects i.i.d. Bernoulli(p); level 1 = ring of 4 sites X (block X = sites 3X, 3X+1, 3X+2);
xi_X in {low, mid, high} with probabilities (q, q'-q, 1-q'); D1(X) = [xi_X = low] or [xi_X = mid and block X has a level-0 defect].
n_sharp = 1 (components of defects within the constrained set have <= 1 site; *-adjacency on a ring = nearest neighbour).
R: both levels fully constrained. B = {level-0 site 0}; R^{-B}: level-1 site pi(0) = 0 unconstrained.
Exact Z(R), Z(R^{-B}) by enumeration of 2^12 * 3^4 configurations with their weights.
Two-species activity (Harris inequality, monotone model): z := q + (1 - (1-p)^3)*(q' - q); bound rho <= 1/(1 - 2*z^2).
Grid: p in {0.02, 0.1, 0.3}, q in {0.001, 0.02, 0.1}, q' in {q, 0.3, 0.9} (q' >= q).
- C1 (containment, deterministic): every configuration in R^{-B} \ R has two adjacent level-1 defects containing site 0, both
  in the constrained-at-level-1 set of R. PASS iff 0 exceptions.
- C2: PASS iff Z(R^{-B})/Z(R) <= 1/(1 - 2*z^2) at every grid point with 2*z^2 < 1 (0 violations).
- C3 (negative control: the species link is load-bearing): the bound with the finer contribution dropped, z0 := q, must be
  VIOLATED at some grid point (some point with Z(R^{-B})/Z(R) > 1/(1 - 2*q^2)). PASS iff at least one violation.

Resource limits: one run under the numeric lock, nice 10, BLAS threads 1, < 20 min, < 1 GB.
