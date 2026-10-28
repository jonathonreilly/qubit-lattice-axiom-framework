# na55_const — criteria (written BEFORE checks/na55_const.py exists)
Worker: claude-opus-5-5 (NODEA55.md). Exact rationals (fractions.Fraction) in plain python; every logarithm / sine / cosine is
enclosed in a rigorous rational interval (atanh series for ln with explicit geometric remainder; alternating Taylor series
with remainder for sin/cos). No float is used in any verdict. Inputs quoted from HW §35.7 / checks/w6_arith.py:
a = 1e-86, beta_- = 0.186 (= 186/1000), L = 3, C_l = 1, R = 0; DX' ceiling 2.5e-152; recorded (RLF-delta) ceiling 1e-94.

K1 (CONFIRMATORY; reproduces HW §35.7's table with HW's own formulas, so it tests the interval code, not new mathematics):
   g2 = a/(b_n + ln 12800) with b_n = 81*81*10002*c_+ + 10001*c_U at c_U = 1, c_A = 0:
   c_+ = 1 -> g2 in [1.52361e-94, 1.52363e-94];  c_+ = 17 -> g2 in [8.96375e-96, 8.96377e-96].
   PASS iff both enclosures lie inside the stated bands. (Bands are HW's printed 6-figure values, not values derived here.)

K2 (CONFIRMATORY; the constants of NODEA55's route (4°), evaluated by the formulas written in NODEA55 Part B; nothing here is
   a pre-registration because the formulas were derived in the same session):
   b_n° = 12401 c_U + 810162 c_A, b_D° = 10000 c_U + 810000 c_A, c_f° = c_U + 81 c_A,
   g2° = a/(b_n° + ln 6400),  n_T° = b_D°/(a beta_- ln 3),
   REL-boot ceiling a/(h * (c_f° + 1)) and HIST-sum ceiling a/(h * (c_f° + 2) + ln 12800) with h in {38417 (HIST as written),
   10001 (H-geo')}; n_H = (4 + h0 * c_f°/ln 3)/(a beta_-), h0 in {38416, 10000}.
   Printed at (c_U, c_A) = (1, 0) and (1, 1). Reported: each value's enclosure, the binding (smallest) ceiling, and its decades
   above 1e-94 and above 2.5e-152. No PASS band; the gate is K2-sanity: every enclosure has width < 1e-6 relative. PASS iff so.

K3 (PRE-REGISTERED). The planar-annulus inequality of NODEA55 Proposition F-UNIV: for b in {1/1000, 1/100, 3/100},
   (2 sin(50 b))^2 / 72 > 100 (1 - cos b)   (rigorous enclosures: PASS iff lower(LHS) > upper(RHS) at all three b).
   Negative control K3n: at b = 1/10 the inequality must FAIL (upper(LHS) < lower(RHS)); if it holds there, K3 is reported as
   uninformative about the role of b.

K4 (PRE-REGISTERED). Geometry of the same proposition, by brute force on the 4D box [-2, 10]^4 with the block B := [0, 8]^4
   (the level-0 sites of one level-1 cube), links = nearest-neighbour pairs, plaquettes = unit squares:
   (a) every (1,2)-plaquette with (x3, x4) in [0,8]^2 and lower-left corner in [-1, 8]^2 contains a link with at least one
       endpoint in B ("free" link: inside or crossing); there are exactly 100 per such slice, of which 64 have all four vertices
       in B and 36 do not;
   (b) no (1,2)-plaquette with (x3, x4) outside [0,8]^2 contains a free link;
   (c) every link of the boundary loop of the square [-1, 9]^2 in a slice with (x3, x4) in [0,8]^2 has BOTH endpoints outside B.
   PASS iff (a), (b), (c) hold for all 81 slices.

K5 (PRE-REGISTERED). The one-step coupling ratio of Lemma DOM, by the route NODEA55 Part E uses:
   for every x = k/1000, 1 <= k <= 500: x/(1 - x) <= 2x (exact).  Negative control K5n: x = 3/4 must violate it.

K6 (CONFIRMATORY). Gaussian-model constant: the number of nearest-neighbour links with both endpoints in a 9^4 block of Z^4
   (brute force) and 3 times it; log c = (3*links/2) * ln(1/(1 - lambda_f)) at lambda_f = 1/2, enclosed.  No PASS band; the
   gate is that the brute-force count equals 4 * 8 * 9^3.

K7 (CONFIRMATORY). Hoelder route: for (p, q) = (2, 2) and (3/2, 3): theta_max = min{ 1/(24 p (1 + 2 r)), ... } printed at
   r := R g_K^2 = 0 and 1/100; and the kappa threshold 256 q theta c_pr / lambda at lambda = 1/2, c_pr = 1/1797760.
   No PASS band (arithmetic record).

Reporting: per gate, PASS / FAIL / UNINFORMATIVE with the enclosures printed to 12 significant digits.
