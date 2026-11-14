# x8 criteria (pre-registered; written 2026-10-28 after EXISTENCE §18.0 and before any x8 script)

Purpose: check the deterministic inequalities that the session-9 Polyakov-loop route (T25) uses, and look at the size
of the Polyakov family's reflection covariance in the simplest class member (SU(2) Wilson, depth 0). Non-load-bearing:
the T25 proof is analytic; x8 can catch an algebra or sign error in its inequalities, nothing more.

Notation. SU(2) as unit quaternions; f(W) := (1/2) tr W = Re(q). For W1, W2: F(W1, W2) := f(W1)^2 + f(W2)^2 + f(W1 W2)^2;
comm := ||1 - W1 W2 W1^-1 W2^-1||_op (= |1 - q| for the quaternion q). Lattice: periodic, plaquette
U_p = U_mu(x) U_nu(x+mu) U_mu(x+nu)^-1 U_nu(x)^-1; ||1 - U_p||_op = sqrt(2 - 2 Re U_p). Polyakov loop W_mu(t, x) =
ordered product of the direction-mu links around the spatial cycle through x at time t; family S = {e1, e2, e1+e2} with
f_{e1} = f(W_1), f_{e2} = f(W_2), f_{e1+e2} = f(W_1 W_2) (loops based at the same site). Ribbon of a loop between slices t
and t': all time-plaquettes with a spatial edge on the loop, between the two slices (|loop| * |t - t'| plaquettes; the
shorter way round is allowed, since both are valid ribbons). T^2_{12}(t, x3): the n1 n2 plaquettes of the (1,2) 2-torus
through the base point.

## A (exact / deterministic; each must hold with zero violations at tolerance 1e-12)
- A1. min over (a, b) of cos^2 a + cos^2 b + cos^2(a + b): grid 2001 x 2001 on [0, 2pi)^2 plus local refinement.
  PASS iff the minimum is in [0.75 - 1e-9, 0.75 + 1e-6] and no grid value is < 0.75 - 1e-9.
- A2. F(W1, W2) >= 3/4 - comm on 10^6 random SU(2) pairs: 4 x 10^5 Haar pairs; 4 x 10^5 near-commuting pairs
  (W2 = exp(eps X) * (an element of W1's one-parameter subgroup), eps log-uniform in [1e-6, 1], X Haar-direction);
  2 x 10^5 exactly commuting pairs. PASS iff zero violations. Report the minimum slack F - 3/4 + comm.
- A3. On 8 x 4^3 configurations ((i) 20 small-field configs U = exp(eps X), eps in {0.02, 0.1, 0.3}; (ii) 20 Haar configs;
  (iii) every 50th measured Monte Carlo configuration of B), for every base point and every time slice:
  (a) comm(W1, W2) <= sum over T^2_{12} of ||1 - U_p||;
  (b) |f_n(t) - f_n(t')| <= sum over the ribbon of ||1 - U_p|| for n in S and every pair (t, t') (both ways round);
  (c) F <= 3 and F >= 3/4 - sum over T^2_{12} of ||1 - U_p||.
  PASS iff zero violations.
- A4 (informational, no verdict). SU(3): minimum over commuting triples (diagonal phase triples, random starts + local
  minimisation, 2000 starts) of sum_{n} |N^-1 tr h^n|^2 over the charged n in {-1, 0, 1}^3 (n not = 0 mod 3), and over
  S3 := {e1, e2, e1 + e2, e1 - e2, e1 + 2e2}. Report the minima.

## B (Monte Carlo; informational; expectation test, not implied by the theorem at these couplings)
SU(2) Wilson, 8 x 4^3 (time side 8), heatbath + 3 overrelaxation sweeps, Haar (hot) start, 1000 thermalisation +
2500 measured sweeps per beta, beta in {8, 16, 32}; fixed seeds. Link reflection theta: t -> 7 - t (planes between
slices 7|0 and 3|4). For d = 2t + 1 in {1, 3, 5}: X(d) := sum_{n in S} E[f_n(t) f_n(7 - t)], averaged over spatial base
points (translation invariance). By the center symmetry (Lemma CTR) E f_n = 0 exactly, so X(d) is the summed connected
covariance; f_n(t) f_n(7 - t) is centre-neutral, so a chain that stays in one centre image estimates it without bias.
Errors: jackknife, 25 bins.
- B0 sanity: <s> beta in [0.6, 0.9] at beta = 32 (x7 found 0.754 on this lattice).
- B1. PASS iff X(1) - 5 SE >= 0.375 at beta = 16 and at beta = 32 (an O(1) signal at half the asymptotic floor 3/4).
  FAIL iff X(1) + 3 SE < 0.375 at beta = 32. Otherwise INCONCLUSIVE.
- Also reported: X(3), X(5); E f_n (informational: centre-sector sticking); the theorem's bound
  3/4 - (n_s^2 + 4 n_s d) sqrt(eta) with eta = max_p E||1 - U_p||^2 (expected vacuous, i.e. < 0, at these beta).

Run under the numeric lock (mkdir/rmdir once, no trap), nice 10, BLAS/OMP threads 1, load < 8, python3 without -I, no
timeout. Record start/end, load, wall time and peak memory in checks/x8_time.txt.
