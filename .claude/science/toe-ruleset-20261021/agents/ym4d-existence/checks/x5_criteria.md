# Check x5: criteria (written 2026-10-27, before checks/x5_su2_soft.py exists)

Purpose: test the session-6 claims of EXISTENCE §15 on the compact SU(2) soft chain: d = 4, L = 3, the literal S4'
contours (24 coordinate orders, 81 offsets, complete-axial legs, straight leg of L steps; as x4 A), the decision-4
normalised kernel k(V, M) = exp(-(kappa/g^2)[1 - Re tr(V^-1 M)/2]) / N(M). SU(2) is represented by unit quaternions
(tr U / 2 = q0, matrix average = quaternion average). Sampling: seeded numpy generators; every Monte Carlo number is
reported with its standard error (SE).

Claims under test (derived in §15 before this check is run):
- (NA-1) for SU(2) the contour mean is M = r W with W in SU(2), r = |M|, and the kernel is the central law
  mu_t (density prop. to exp(t cos theta), t = kappa r / g^2) translated by W.
- (NA-2) one-step convolution: given the parents, for a loop with distinct links,
  E[tr V_C / 2] = prod_c a(t_c) * tr W_C / 2, a(t) = I_2(t)/I_1(t), and the law of W_C^-1 V_C is central
  (in particular its vector part has mean 0); 0 <= 1 - a(t) <= 3/(2t).
- (NA-3) flat background: every block holonomy has a central law (mean of its quaternion vector part = 0).
- (NA-GS1) small-noise coefficient: for iid mu_t noise on the fine links (flat background) and one literal S4'
  averaging step, t * E[1 - tr W_P / 2] -> R1 := (3/2) * (4/3)(2 L^-2 + L^-4) = 38/81 = 0.469136 as t -> infinity
  (linear response = Theorem GS with three components); after two steps, -> R2 := 2(2 L^-4 + L^-8) = 0.049688.

**A (must hold; PASS criterion).**
- A1: 1000 random sets of 7 SU(2) elements with random probability weights: max over sets of
  || M - |M| (M/|M|) ||, || (M/|M|) in SU(2) (unit norm) || deviations <= 1e-12 (algebraic identity; trivial check of
  the representation).
- A2: the mu_t sampler: for t in {5, 20, 100}, 2*10^6 samples: |mean(q0) - I_2(t)/I_1(t)| <= 4 SE. The bound
  0 <= 1 - I_2(t)/I_1(t) <= 3/(2t) on 400 log-spaced t in [0.1, 10^4] (scipy.special.ive).
- A3: one plaquette, 4 Haar-random background links W_c and t_c in {8, 15, 30, 60}: 4*10^6 samples of V_c = W_c Z_c:
  |mean(tr V_P/2) - prod a(t_c) tr W_P/2| <= 4 SE; each component of mean(vector part of W_P^-1 V_P) within 4 SE of 0.
  Also the kernel itself: sample V from the normalised kernel by a direct (independent) route, rejection from Haar
  with weight exp((kappa/g^2)(Re tr(V^-1 M)/2 - r)), for one random M (7 random transporters), t = 6: the law of
  W^-1 V matches mu_t (compare mean q0 with a(t) within 4 SE, and the mean vector part within 4 SE of 0).
PASS iff all of A1-A3 hold.

**B (decides the one-step damping; interpretation fixed now).** Fine torus (Z/9)^4, coarse (Z/3)^4, flat background
(all fine links = 1 before noise), iid mu_t noise on all fine links, one literal S4' polar-averaging step (W_c =
M_c/|M_c|), all 81 * 6 coarse plaquettes. t in {25, 50, 100, 200, 400}; 2000 samples per t (batched).
Report R(t) := t * mean(1 - tr W_P / 2) with SE, the depth-0 value R0(t) := t(1 - a(t)^4) (exact), and the means of
the vector parts of W_P (base frame) and of one block link (gauge-variant, informational).
- Weighted least squares R(t) = R_inf + b/t over the five t.
- **PASS (no undamped term at one step)** iff |R_inf - 38/81| <= max(3 SE(R_inf), 0.015) and |R(400) - 38/81| <=
  0.05 * 38/81.
- **BIAS** iff R_inf > 1.0 (more than twice the linear-response value; the depth-0 value is 6): then an O(sigma^2)
  contribution is not damped by L^-2 at one step and §15's verdict is wrong.
- Otherwise INCONCLUSIVE (report).
- NA-3 sub-check (must hold): every component of the mean vector part of W_P within 4 SE of 0 at every t.
- Informational: b, compared with the depth-0 analogue b0 from R0(t) = 6 + b0/t + ... (fitted on the same t).

**C (informational; run only if B's wall time is < 5 min).** Fine torus (Z/27)^4 -> (Z/9)^4 -> (Z/3)^4, flat
background, iid mu_t noise on the fine links only, two literal deterministic S4' polar-averaging steps, t = 100,
at least 20 samples (one at a time). Report R2(t) := t * mean(1 - tr W^(2)_P / 2) against 2(2/81 + 1/6561) = 0.049688,
and the ratio R2/R(100) (linear response: (2L^-4 + L^-8)/(2L^-2 + L^-4) = 0.1059). Expected (not a pass criterion):
R2 within 30% of 0.0497. A value of R2 above 0.2 would indicate an undamped second-step contribution and is reported as
a FINDING against §15.

Resources: one process, nice 10, OPENBLAS/OMP/MKL/VECLIB threads = 1, peak < 1 GB, numeric lock held, `uptime` load
< 8 and >= 25% memory free (memory_pressure) before starting; no `timeout`. Output checks/x5_out.txt, record
checks/x5_time.txt (/usr/bin/time -l).
