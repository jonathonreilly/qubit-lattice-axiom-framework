# na55_geo — criteria (written BEFORE checks/na55_geo.py exists)
Worker: claude-opus-5-5 (NODEA55.md). Exact integer set arithmetic in plain python (no numpy, no floats in any verdict).
Conventions (HW §35.2, quoted): level-j cubes indexed by Z^4; pi(X) = coordinatewise floor(./3); N_t(X) = l^inf radius-t
neighbourhood; Sigma(X) := N_1(pi(X)); Sigma^r its iterate; ||X||_sh := sum_{r=0..M} |Sigma^r(X)| over the levels counted;
col(D) := the 81|D| children of D one level finer; Col(X) := union_{r>=1} pi^r(X) (open column, one level per r).
No constant derived in NODEA55.md appears in a PASS/FAIL condition below except where a gate is labelled CONFIRMATORY;
2401 = 7^4, 81 = 3^4, 16 = 2^4 are lattice geometry; 10001/10000 are HW Corollary H-geo' (HW §35.2), 66 = 1 + 81 - 16 is
the arithmetic of the bound being tested (stated in the gate, not tuned).

G1 (PRE-REGISTERED). Radius map. For every integer u in [-60, 60] and t in {1,...,9}, and every v with |u - v| <= t:
   |floor(u/3) - floor(v/3)| <= floor((t + 2)/3).  PASS iff 0 violations.
   Negative control G1n: the same with floor((t + 1)/3) must FAIL for at least one (u, v, t). If it does not fail, G1 is
   reported as uninformative.

G2 (PRE-REGISTERED). On >= 300 samples X (finite sets of 1..6 cubes, half at uniformly random positions in [-200, 200]^4,
   half at "adversarial" positions whose coordinates are of the form (3^D - 1)/2 + small offsets, D in 3..12):
   (a) pi(N_8(X)) subset N_3(pi(X));  (b) pi(N_3(X)) subset N_1(pi(X)).  PASS iff 0 violations of (a) and (b).
   Negative control G2n: pi(N_8(X)) subset N_2(pi(X)) must FAIL on at least one sample.

G3 (PRE-REGISTERED). On >= 200 samples (D a *-connected set of n = 1..5 level-m cubes grown by a random *-walk, random or
   adversarial base point as in G2; M in 1..8 levels above m), with X := col(D) and C := Col(N_8(X)) restricted to the levels
   m, ..., m + M:
   (a) |C| <= 2401 n + sum_{s=1..M} |Sigma^s(D)|        (Sigma^s computed directly);
   (b) the closed column [D] (D at level m, pi^r(D) at level m + r, r <= M) is a subset of C;
   (c) |C| <= 12401 n + 10000 M   — CONFIRMATORY (it is (a) combined with HW's H-geo' bound ||D||_sh <= 10001 n + 10000 M).
   PASS iff 0 violations of (a), (b), (c).
   Negative control G3n: (a) with 2401 replaced by 81 must FAIL on at least one sample.

G4 (PRE-REGISTERED). On the G3 samples and on >= 100 arbitrary (not necessarily connected) sets: pi(N_1(col(X))) = N_1(X)
   (exact set equality).  PASS iff equality on every sample.  (Independent re-check of REVIEW55_HWPLD F4's identity.)

G5 (PRE-REGISTERED). Push-down bound. For S a set of level-k cubes and x a choice function (x_Q one of the 81 children of Q),
   with ||S||_sh over levels k..k+M and ||x(S)||_sh over levels k-1..k+M:
       ||x(S)||_sh <= 16 ||S||_sh + 66 |S|.
   Samples: >= 200 random (|S| = 1..4, random children, random/adversarial positions, M in 1..10), plus the single-cube family
   Q = (q,q,q,q), q = 3w, w = (3^D - 1)/2, x_Q = (3q,3q,3q,3q), D = 2..60 (computed coordinatewise; the sets are products).
   PASS iff 0 violations.
   G5c (CONFIRMATORY, reproduction of REVIEW55_HWPLD F9 / r55h_geo G-B): on the single-cube family the excess
   ||x(S)||_sh - ||S||_sh equals 81 + 175 D for D = 2..60 under one of the two natural level conventions (reported which).
   A mismatch is REPORTED, not counted as a failure of G5.
   Negative control G5n: on the single-cube family, ||x(S)||_sh <= ||S||_sh + 3073362 must FAIL at D = 20000.

Reporting: every gate prints its sample count, violation count and (for controls) whether the control fired. A gate whose
negative control does not fire is reported as UNINFORMATIVE, not PASS.
