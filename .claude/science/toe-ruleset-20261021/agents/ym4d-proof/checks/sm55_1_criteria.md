# sm55_1 — criteria (written before the script; SEAM55 §1, the W0 chart algebra)

Written UTC 2026-10-29 (time stamped by `date -u` in the same shell command that created this file), before
`sm55_1_chart.py` exists. Exact symbolic arithmetic (sympy, rationals); no floats in any verdict.

Objects (SPHERE55 §1.1 conventions). South chart x in R^4, Omega(x) = 2R^2/(R^2+|x|^2). Boost field
v_c(x) = R^2 c + 2(c.x)x - |x|^2 c. Transition map to the north chart phi(x) = R^2 x/|x|^2.
Profile u(x) = T(log(a Omega(x))) with T an arbitrary (undefined) smooth function.

Tests (each PASS iff the stated expression simplifies to exactly 0, or the stated equality holds exactly):
- C1  div v_c - 8(c.x) = 0  and  v_c.grad(log Omega) + div v_c/4 = 0.
- C2  v_c.grad(u) + (div v_c/4) T'(log(a Omega)) = 0, for undefined T (the profile identity used in SEAM55 §1).
- C3  D phi(x) v_c(x) + v_c(phi(x)) = 0 identically (north-chart representative of the boost is -v_c), and at
      |x| = R: D phi(x) = I - 2 x x^T / R^2 (reflection in the tangent hyperplane), checked on the parametrized
      equator point x = R e with e a symbolic unit vector built from two angles is NOT required; instead check
      D phi(x) - (I - 2xx^T/R^2) = (R^2/|x|^2 - 1) I - 2(R^2/|x|^4 - 1/R^2) x x^T  (exact identity, vanishing at |x| = R).
- C4  Polar angle t from S. South: x = R tan(t/2) e  gives Omega_S = 1 + cos t.  North: y = R cot(t/2) e gives
      Omega_N = 1 - cos t.  One-sided t-derivatives at t = pi/2: -1 (south), +1 (north).
- C5  For v_c: the symmetric part of d_mu v_nu - (div v/4) delta_{mu nu} vanishes (conformal Killing in the chart).
- C6  P4 two-loop rule: with log f(u) = (b1/(2 b0^2)) log(u/b0) - u/(2 b0), du/dlog s = 1/(d log f/du) equals
      -2 b0/(1 - b1/(b0 u)), and its expansion in 1/u is -2 b0 - 2 b1/u - 2 b1^2/(b0 u^2) + O(u^-3).
- C7  c4_pert(u) := (B_lat(u) - B_pert(u))/B_lat(u), B_lat = Binf + B1/u + B2/u^2, B_pert = 2 b0 + 2 b1/u + 2 b1^2/(b0 u^2):
      limit u -> oo equals (Binf - 2 b0)/Binf; with Binf = 2 b0, B1 = 2 b1 the expansion starts at order u^-2.
- C8  Two-loop model B(u) = 2 b0 + 2 b1/u. One RG step: Delta defined by integral_u^{u+Delta} du'/B(u') = log L,
      solved as a series in 1/u to order u^-2. Then Delta/log L - B(u + t Delta) has zero coefficient at orders u^0 and
      u^-1 for every t (interpolation error of the trajectory profile is O(u^-2), i.e. O(g^4)).
- C9  Exponent arithmetic of the two-scale thresholds (exact rationals): from a s^(-7/2), a^2 s^(-4), c4 s^(-2) the
      thresholds are a^(2/7), a^(1/2), c4^(1/2) (SPHERE55 E10); with the extra coarse-image factor s^(-4) they are
      a^(2/15), a^(1/4), c4^(1/6).

Controls (each must FIRE, i.e. the analogous test must FAIL on the deliberately wrong input):
- X1  wrong profile u = T(log(a Omega^2)): the C2 expression is not 0.
- X2  non-Killing field w = R^2 c (pure chart translation): w.grad(log Omega) + div w/4 is not 0.
- X3  wrong north sign: D phi(x) v_c(x) - v_c(phi(x)) is not 0.
- X4  value-problem control: Binf = (11/10) 2 b0 gives lim c4_pert = 1/11, not 0.
- X5  wrong north kink: Omega_N := 1 + cos t fails the C4 north formula (derived from the north chart).

Verdict: PASS iff C1-C9 all hold and X1-X5 all fire. Anything else: FAIL, reported as such.
What this check can and cannot decide: it decides the exact chart algebra and slope arithmetic used in SEAM55 §1
(could fail on a sign or factor slip; X1-X5 show the tests are sensitive). It decides nothing about the lattice
theory: LCS (the local Callan-Symanzik input) and every analytic input remain inputs.
