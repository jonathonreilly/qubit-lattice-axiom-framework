# sp55_kill — criteria (pre-registered before the script; SPHERE55.md §1.1, §3)

Written 2026-10-29 03:32 UTC (file mtime), before `sp55_kill.py` exists.

Purpose: decide whether the stereographic formulas used in SPHERE55 §1.1 and §3 are right. Exact arithmetic only:
`fractions.Fraction`, derivatives by forward-mode dual numbers over Q (exact for rational functions; independent of
any hand-derived Jacobian). Random rational points from a fixed seed; at least 40 points per item; radii R in
{1, 3/2, 7}.

Conventions under test. S^4_R = {X in R^5 : |X| = R}. South chart = stereographic projection from N = (0,0,0,0,R):
x = R X'/(R - X_5). Inverse X(x) = (2R^2 x, R(|x|^2 - R^2)) / (|x|^2 + R^2). Omega(x) = 2R^2/(R^2 + |x|^2).
Boost field v_c(x) = R^2 c + 2(c.x) x - |x|^2 c; rotation field v_J(x) = J x, J antisymmetric.

Items (each PASS iff the stated exact equality holds at every sampled point):
- K1  |X(x)|^2 = R^2, and X_5(x) <= 0 iff |x| <= R.
- K2  Pullback metric: (dX)^T (dX) = Omega(x)^2 * I_4 exactly (dX from dual numbers).
- K3  Flat conformal Killing equation for v_c: d_mu v_nu + d_nu v_mu = (1/2)(div v) delta_{mu nu}; and div v_c = 8 (c.x).
- K4  Killing equation for g = Omega^2 delta: d_mu v_nu + d_nu v_mu + 2 (v . d log Omega) delta_{mu nu} = 0, for v_c and
      for v_J; equivalently div v = -4 v . d log Omega.
- K5  On the equator chart sphere |x| = R (rational points of S^3_R), v_c(x) = 2 (c.x) x (purely radial).
- K6  Chart transition: north chart y = R X'/(R + X_5) equals R^2 x/|x|^2, and the south-chart coordinate of the
      reflected point (X', -X_5) equals the north-chart coordinate of X (theta_eq acts as the identity between charts).
- K7  The pushforward of v_c by the 5D rotation: the ambient vector field of the rotation in the (X_i, X_5)-plane,
      A(X) = X_i e_5 - X_5 e_i, satisfies dX(x) v_c(x) = lambda A(X(x)) for a constant lambda (to be found from one
      point and then checked at all points), with c = e_i. (Identifies the boosts as rotations of S^4_R.)

Controls that MUST fire (the check is invalid if any control passes):
- C1  v = R^2 c alone (pure chart translation) fails K4 at some sampled point.
- C2  v = c' + 2(c.x)x - |x|^2 c with c' = 2 R^2 c fails K4.
- C3  Omega' = R^2/(R^2 + |x|^2) fails K2.
- C4  v_c with c = e_1 fails K5 at some sampled point of |x| = R/2 (the radial property is special to the equator).

Verdict rule: PASS iff K1-K7 all hold at every point and C1-C4 all fire. Any failure of K1-K7 is reported verbatim and
the corresponding formula in SPHERE55 is corrected in an erratum. No floats are used for any verdict.
