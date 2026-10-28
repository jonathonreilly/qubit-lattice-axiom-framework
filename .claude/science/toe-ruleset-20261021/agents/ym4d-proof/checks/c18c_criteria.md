# c18c pre-registered criteria (written 2026-10-27, session 7, BEFORE c18c_a1na_inregime.py was written or run)

Purpose: test the key step of Lemma A1-NA(1) inside its own regime (REVIEW_S5_S6 (4), binding): small phi,
near-extremal field, coarse torus side >= 3, principal-branch X_p, HS norms as in the lemma.

Setup.
- G = SU(2); S4' averaging (diagonal order pairing), L = 3.
- Cases: d = 2 with coarse side 5 (fine 15^2); d = 3 with coarse side 3 (fine 9^3).
- Fields U = exp(t H), H = lowest-Fourier-mode abelian tau_3 part (near-extremal for A1: the long-wavelength mode)
  plus a smooth non-abelian tau_1/tau_2 part of relative size 0.3 on the same lowest modes (two seeds).
- t grid: 0.0025, 0.005, 0.01, 0.02.
- phi(t) := max_p |X_p|_HS, X_p the principal log (eigen-angles in (-pi, pi]).
- R_log(t) := sum_P |log V'_P|^2_HS / sum_p |X_p|^2_HS ; R_s(t) := sum_P s(V'_P) / sum_p s(U_p).
- R_ab := the same ratio for the ABELIAN linearised S4' of the Lie-algebra field t H (computed independently, by linear
  sums of link logs along the same paths; t-independent).

Criteria (each field, each d):
- (a) Near-extremal (non-vacuity): R_ab / L^{4-d} >= 0.5. If it fails, the case is reported as not informative (FAIL).
- (b) A1 on the field: R_ab <= L^{4-d} (1 + 1e-9).
- (c) Leading constant is the abelian one, with an O(phi) correction: D(t) := |R_log(t) - R_ab| / phi(t) does not grow
      as t decreases: D(t_i) <= 1.5 D(t_{i+1}) + 1e-9 for consecutive grid points t_i < t_{i+1}.
- (d) In regime: every coarse |log V'_P|_HS <= 0.25 and every fine phi <= 0.25 at all t; coarse side >= 3.
- (e) The lemma's inequality with a reported constant: C_rep := max_t max(R_log(t)/L^{4-d} - 1, R_s(t)/L^{4-d} - 1, 0)/phi(t).
      REPORTED, not a pass/fail criterion (the lemma's C_6 is not computed, so no numeric ceiling would falsify it).
      Also reported: |R_s - R_log| at each t.

A FAIL of (b) or (c) inside the regime (d) would contradict the lemma's key step (leading constant L^{4-d} + O(phi)).
A FAIL of (a) or (d) means the instance is not a test. Results are kept as first-run output whatever they are.
Finite instances only; no uniformity in L, volume, or field is tested.
