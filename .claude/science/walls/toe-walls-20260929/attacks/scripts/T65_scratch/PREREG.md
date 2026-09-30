# T65 pre-registration (written BEFORE any script was run)

Wall T65 = L14-W4: options B (recorded adjacency) and C (strongly correlated or
non-local gravity) "have no bounded test". Claim under attack: that nothing
bounded can be computed for either. I register necessary-condition tests. They
cannot show a graviton exists; they can show an exit fails a necessary condition.

## Test 1: does "distances are counts of steps" (MAP:1105-1107) give a Riemannian metric?
Facts used: for a periodic graph on Z^3 with symmetric generating set S the
large-scale step-count metric is the gauge (norm) of conv(S) (Burago, "Periodic
metrics", Adv. Soviet Math. 9 (1992) 205). Anisotropy A = R_out / r_in of conv(S)
= max/min of N(u) over unit vectors u.
- 1a periodic, unweighted, cubic-symmetric S (unions of octahedral-group orbits),
  degree D <= 26.
  PASS (slogan survives a periodic recorded adjacency): min A <= 1.05.
  FAIL: min A > 1.25. Between: inconclusive.
- 1b degree needed: min A over unions of orbits with max-norm <= 3, as a function
  of D. Descriptive: fit A-1 ~ D^-p. Expectation p in [0.5, 1.2].
- 1c graded (finite alphabet of edge lengths) on the 26-neighbour star: min A vs
  alphabet size N (integer weights 1..N); Euclid weights as the N->inf limit.
  Descriptive. Expectation: N ~ 10 reaches A <= 1.05 (so graded B = T64 finite slots).
- 1d aperiodic: Poisson random geometric graph in a periodic 3-torus, mean degree
  k in {8,16,26,50}; hop distance vs Euclid in cones (3 axes, 6 face diagonals,
  4 body diagonals), Euclid distance 8..14. PASS (aperiodic B is isotropic at
  bounded mean degree): A_RGG <= 1.06 at k = 26. FAIL: > 1.15.

## Test 2: what binary adjacency on a Z^3 background carries, and can it be TT-only?
- 2a: dilute 9 bond classes (3 axis, 6 face diagonal) of the 18-neighbour Z^3
  network with probabilities q_e; effective conductance tensor sigma(q) on a
  12^3 periodic torus, 8 samples, exact cell-problem solve.
  PASS (a smooth 6-component metric exists as a coarse-grained density): the
  9 -> 6 response matrix has rank 6 and sigma is linear in q to within 10% at q = 0.1.
  FAIL: rank < 6 or nonlinearity > 10%.
- 2b: helicity content of a q-independent (analytic) polarisation tensor e,
  direction-averaged: expected TT fraction 2/5 of any traceless unit tensor (Schur),
  0 for the trace. Also max over e of min over q-hat of the TT fraction.
  PASS for "analytic density modes can be TT-only": best min-over-direction TT
  fraction >= 0.9. FAIL: < 0.5.

## Test 3: the non-local exit (S5): how much range does a partner-gapping kernel need?
X(q) = I - P_TT(q-hat) on Sym^2(R^3) (6-dim), lattice momentum p_i = 2 sin(q_i/2)
(non-analytic only at q = 0). Inverse-FFT to K(r) on a 48^3 torus, truncate |r| <= R,
evaluate the symbol X_R(q) at |q| in {0.1, 0.2, 0.4} along (100), (110), (111).
rho = lambda_TT / lambda_partner (ideal 0: TT massless, partners massive).
  PASS (a local truncation suffices): rho <= 0.1 at |q| = 0.2 for some R <= 4.
  FAIL: rho > 0.5 for every R <= 4. If FAIL, report the R at which rho <= 0.1 and
  test R * |q| = const. Also fit the tail K(r) ~ r^-a; expectation a = 3.

## What each result would move
- 1a FAIL + 1d PASS: periodic B keeps the grid's anisotropy; only aperiodic B is
  isotropic, and it replaces Lattice wholesale.
- 2a PASS + 2b FAIL: B on a Z^3 background is option C (metric = density); a
  TT-only mode needs a direction-dependent polarisation, i.e. a constraint.
- 3 FAIL: the non-local exit needs range growing with wavelength (a 1/r^3 tail),
  which the nearest-neighbour Admissibility rule cannot supply directly.
