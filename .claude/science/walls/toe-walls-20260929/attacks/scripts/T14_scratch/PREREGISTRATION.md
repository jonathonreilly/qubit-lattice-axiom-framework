# T14 pre-registration (written BEFORE running yukawa_euclid_gap.py)

Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family check).

## Question the test decides
Route R1 (put every field on the hypercubic Euclidean block, the primitive's
"equivalently" clause) claims the speed gap of probe 3 is a property of the
LOCAL-HAMILTONIAN / continuous-time regulator, not of the interaction. Two
things follow that the lane has NOT checked for a spinor (probe 3 T2, "Limits
of T2": "Spinors are not re-classified here"):

  (a) On Z^4 with the same Lorentz-invariant Yukawa coupling, a spinor's
      one-loop log-speed shift and a scalar's one-loop log-speed shift are each
      exactly zero at tree speed 1, so the gap is exactly zero.
  (b) The gap is NOT robust to a small time-step mismatch: it turns on linearly
      in (eps - 1), with an O(1) slope, and it reaches an eps-independent
      nonzero plateau as eps -> 0 (the continuous-time surface).

Comparator: 4-component naive Dirac fermion psi (mass m) + real scalar phi (mass
mu), Yukawa g phi psibar psi, Euclidean lattice with spatial step 1 and time step
eps, symmetric-difference fermion, second-difference scalar, tree speeds both
tuned to 1 for every eps. One loop only, coefficients of g^2. This is the same
model class as probe 3 (Lorentz-invariant Yukawa) but with Euclidean time.

Outputs: a_psi = f_x - f_t/c_psi, a_phi = (t_s - t_t/lam)/2, gap = a_psi - a_phi
(per g^2; log-speed shifts of fermion and scalar).

## Pass / fail readings (fixed now)
- P1 (symmetry point). At eps = 1, c_psi = lam = 1: |a_psi|, |a_phi|, |gap| < 1e-9
  (grid-exact) for every N and every (m, mu) tried.
  FAIL if any exceeds 1e-6: then the hypercubic protection does NOT cover the
  spinor sector in this comparator and route R1 loses its main support.
- P2 (mismatch turns it on). At eps = 0.5, 0.25, 0.1 (tree speeds 1) |gap| >= 1e-3
  and the sign and size are stable as N grows (N=32 vs N=40 within 5%).
  FAIL if |gap| < 1e-4 for all eps != 1: then the probe-3 gap is not a
  time-regulator effect and the wall is mis-diagnosed.
- P3 (linear slope at the symmetric point). gap(eps) for eps = 1 +- 0.02 is
  antisymmetric to within 20% and |dgap/d eps| >= 1e-2 (so a mismatch of 1e-13
  would give ~1e-15: the primitive must be exact).
- P4 (validation link to probe 3). In the limit eps -> 0.02, m = mu -> 0.1 (small),
  the FERMION-only coefficient a_psi is negative and of size 0.005-0.03, i.e. the
  same sign and order as probe 3's walker shift -0.011675 (p->0, then mu->0).
  Not a precision match: naive Dirac vs the walker, massive vs massless.
  FAIL of P4 only downgrades trust in conventions; it does not decide R1.
- P5 (IR attraction exponent, secondary). With tree speeds detuned by eta (scalar
  faster by eta) at eps = 1, d(gap)/d(eta) at small eta is negative (attractive)
  and its magnitude grows like a log as m = mu decreases. Its log-slope times
  g^2 = 4 pi/137 is the exponent gamma. Reading: gamma < 0.05 kills the
  "IR attractor at the comparator's coupling" route (needed: gamma >= 0.65 for
  1e-15 from a 2.4e-3 start over 19 decades).
