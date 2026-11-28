# Check of gap-solve10-astra62.md (FINISH row 1164)

Status: DONE. Written step by step as the check went; RESULT at the end.

File under check: `library/gap-solve10-astra62.md` (441 lines).

Checker: laptop Claude subagent, Claude Opus 5.5, max effort. Cross-provider
check of row 1163. Started 2026-11-19.

## Plan (at most eight steps)

1. Read the setting (`library/gap-council-brief.md`) and the file under
   check in full, in ranges. Record its statement list.
2. Read the parts of rows 1145-1161 (`library/gap-solve2-astra62.md` ...
   `library/gap-solve9-astra62.md`) and their checks that the file cites.
3. Check the equivalence of (W) with the signed zero test (23), the error
   bound (22) and the matching estimate (24).
4. Check the forced singularities from the first winding coefficients.
5. Check the neutral-momentum count with (27).
6. Check the excess selection between 0 and log 8.
7. Check everything else, line by line.
8. Verdict table, corrections, and the RESULT line.


## Step 1 result: statement inventory (lines of the file under check)

I read all 441 lines in three ranges (1-150, 151-300, 301-441) and the
council brief (122 lines). The file marks these statements:

- GUIDE: L3, L5, L9, L13, L15. OPEN: L11, L123, L438.
- Positive claims named by the row, checked first:
  - (W) and the zero test: (22) L277-290, (23) L292-301, (24) L303-307.
  - Winding coefficients and forced singularities: (31) L401-408,
    (32) L410-414, (33) L416-420, disk r_* L422, count L424-428.
  - Neutral-momentum counts: (13)-(15) L160-201, (16)-(20) L205-258,
    (25)-(26) L311-340, (27) L361-370.
  - Excess selection: (1) L19-29, (2) L31-41, branch M L43-48,
    (3) L50-55.
- Everything else: (4)-(8) and (5) L59-99; (9)-(10) L103-121;
  (11)-(12) and limits L127-156; (21) L262-273; moment obstruction
  L344-357; (28) L374-383; (29)-(30) L385-397; semigroup example
  L432-436; RESULT L441.

Each statement gets a verdict below with its line.

## Step 2 result: cited inputs, read at their source lines

All paths are in `library/`. Status is as recorded at those lines.

- Row 720, `gap-phys-seed.md` L283-320: Lemma Z3 (L283-294), Theorem ZD
  (L296-304), Theorem ZD-c (L311-320). (PHYS-SEED) is
  limsup_j S_j(l/(2a_j); (l/a_j)^3) below 1/5041, or below 1/1650 with the
  two-stage line. Here S(N; (2N)^3) = Tr U^N - 1 on the cube (2N)^3, so
  (PHYS-SEED) at side L is limsup_j (Tr U^{n/2} - 1) < 1/1650 with n = L/a_j.
  This is the form used at L11 and L299 of the file under check.
- `gap-crux-restate.md` L174-219: Lemmas K, X, E, Theorem S, Lemma E'
  (L213-215: 1 + S(a; h) <= (1 + S(a; b))^{h/(b-a)} for h >= b > a >= 3) and
  Corollary S3' (L217-219: S(D/2; L^3) <= q^{2^k}/71).
- `gap-flux-exercise.md` L481-517: Proposition CL (the three sector sets),
  Lemma W, Theorem S-w (L507-513). Checked in `gap-flux-exercise-check.md`
  L255-300: Lemma W HOLDS, Theorem S-w HOLDS (constant 71, 5041 = 71^2).
- Row 1161, `gap-solve9-astra62.md` L83-228 and L265-290: (6)-(14), the
  finite-aspect theorem (L146), its consumer (L148), necessity (L150),
  (14) (L178-183), the K = 512 test (L215-227), (19). Row 1161 was checked
  as row 1162 (`gap-solve9-check-opus.md` L601): HOLDS AFTER CORRECTION,
  credit only; 44 of 45 statements hold, none fails. So L13 of the file
  under check ("an unchecked input at the pinned commit") is now out of date;
  this changes no step here.
- Lemma ORD: `gap-unit-max.md` L286-296, checked in `gap-unit-check-opus.md`
  Step 3 (L62-77): HOLDS. S(t; B) is analytic near 0 with a zero of order at
  least 4t on boxes with all sides at least 4.
- Rectangle port (P): `gap-seed-sc.md` L95: Z(Lambda; beta) is not 0 for
  |beta| <= 1/12800 on every torus with sides at least 3 (checked inputs,
  row 694).
- Cylinder witness, row 865: `gap-sdcyl-ca-astra.md` L121-269, checked in
  `gap-sdcyl-ca-check-opus.md`: all six statements HOLD, conditional on the
  account's kernel comparison (h1)-(h3) and the named transfer hypotheses.
  The class T(d; theta) (as re-derived in that check, L25-40): nonnegative,
  Lipschitz, support in a ball of radius d, mass >= theta ||f|| d^4,
  Lip f <= ||f||/(theta d), support separation in [d, 6d], common ball of
  radius 5d; theta = 1/300.
- Depth function: `port/p9-witness.md` L490-500: with t = log_L(1/d),
  t <= s(d) < 1 + t + log_L C_W(s(d) - 1), so s(d) is comparable with
  1 + log(1/d) for small d. This supports L185 and L212.
- (RF25): `gap-solve3-astra62.md` L9 and L278: both drift bounds give
  beta asymp log n at fixed reference coupling (used at L390).
- Row 1157 (9): `gap-solve8-astra62.md` L160-165 (individual-flip
  hypothesis), as L110 says.

Guide run (numerics, not proof; a scratch script outside the repository,
under 50 MB): pi^2/2560 = 0.003855 > 1/300; the m = 0 excited trace at L/2 is
0.2962 > 6e^{-pi} = 0.2593 > 1/1650; log tanh x + 2e^{-2x} <= 0 on a grid;
the Poisson tail is below (es/(d+1))^{d+1} on a grid; sign cos(5 theta) is
orthogonal to cos(j theta), j = 0..4; the parity model (21) at b = 6,
lambda = 1/2 has 72 distinct roots of c^A +- s^A with |Im z| <= pi/b. All
agree with the hand derivations below.

## Step 3 result: (22), (23), (24) -- the zero test for (W)

**(22), L277-288 and proof L290: HOLDS.** Re-derived by hand.
- The common constant e^{-z} per plaquette cancels in J: the T-torus has
  6n^3 T plaquettes and the 2T-torus 12n^3 T, and 2(6n^3T) - 12n^3T = 0. So
  weights e^{z w_p} may be used, both integrals equal 1 at 0, and the action
  sum is at most 6n^4 <= 12n^4 in modulus.
- Disk factorization on radius r (circle free of zeros). For each integral,
  g = Z / prod B_a with B_a(z) = r(z - a)/(r^2 - conj(a) z). On |z| = r,
  |g| = |Z| <= e^{12 n^4 r}; g has no zeros inside; |g(0)| >= 1. So
  12n^4 r - log|g| is nonnegative harmonic with value at 0 at most 12n^4 r.
  The Poisson-kernel gradient bound on |z| <= r/2 gives |g'/g| <= C n^4.
  For |a| < r and |z| <= r/2, |conj(a)/(r^2 - conj(a) z)| <= 2/r. Jensen on a
  circle of radius in [2r, 3r] gives N(r) <= 36 n^4 r / log 2. With weights
  2 and 1 for the two integrals, |G| <= C n^4 on |z| <= r/2, C absolute.
- Contact: J = 2 log X_T - log X_{2T} (the Perron term t log lambda_0
  cancels exactly). Lemma ORD gives X_T - 1 = O(z^{4T}) and
  X_{2T} - 1 = O(z^{8T}) on boxes with sides >= 4. So H = J' = O(z^{4T-1}).
  For m <= 4T - 1 the Taylor polynomial of G through degree m - 1 is minus
  that of the pole sum.
- Cauchy on the disk of radius r/2: the k-th coefficient of G is at most
  C n^4 (2/r)^k; for 2B < r the remainder on [0, B] is at most
  C n^4 (2B/r)^m/(1 - 2B/r). Integrating over [0, B] gives the factor B.
- Pole terms: Re of the integral over [0, B] of 1/(z - zeta) is
  log|1 - B/zeta|; the integral of its Taylor polynomial through degree m - 1
  is -sum_{k=1}^m (B/zeta)^k/k. So each pole contributes nu(zeta) Psi_{m,B}
  exactly. No zero lies on [0, B] (positive real integrals). This is (22).

**(23) and its quantifiers, L292-301: HOLDS, given Theorem ZD-c of row 720
and its two-stage line.**
- Admissibility: Q = 2 + B/r_s >= 2, so m = O(log n) <= 4T - 1 = 2n - 1 for
  large n when B = O(log n).
- Error: r >= 4(1+B)Q gives 2B/r <= 1/(2Q), so (2B/r)^m <= 2^{-m} Q^{-m}
  and Q^{-m} <= 1/(n^{4+p}(1+B)). The error is at most C n^{-p}.
- Zero count: r <= 8(1+B)Q <= C(1+B)^2 (absorbing 1/r_s), so Jensen gives
  at most C n^4 (1+B)^2 zeros with multiplicity in the disk.
- Equivalence: S_j - J(beta_j) = O(n^{-p}) -> 0, so
  limsup_j S_j = limsup_j J(beta_j). Since 1 <= X_{2T} <= X_T (normalized
  eigenvalues in [0, 1]), X_T <= e^J = X_T^2/X_{2T} <= X_T^2. If (23)
  holds, limsup_j (X_T - 1) < 1/1650, which is (PHYS-SEED) at side L with
  the 1/1650 threshold, hence (W) by ZD-c. Conversely (W) gives (PHYS-SEED);
  the two-stage line and Lemma Z3 (S <= q'^{2^k}/5041 at size 2^k l) make
  X_T - 1 as small as wanted at a fixed dyadic enlargement, and J <= 2 log X_T
  gives (23) there. Both limits are in the stated order.
- The zero-free radius r_s = 1/12800 is the port (P) (`gap-seed-sc.md` L95),
  valid on every torus with sides at least 3, so on both boxes once n >= 6.
  For (23) itself only Q >= 2 is used; r_s enters (24).

**(24), L303-307: HOLDS.**
- Analytic error with m = ceil(log(n^4(1+B)/eps)/log Q): at most
  C n^4 B (2Q)^{-m} <= C eps.
- |Im zeta| >= c n^{-4} for every zero: with |y| * 6n^4 < pi/4 all phases of
  e^{iyS} lie in (-pi/4, pi/4), so the tilted mean has positive real part.
  |zeta| >= r_s by (P).
- For a matched pair (zeta, xi): |log|zeta - B| - log|xi - B|| <=
  |zeta - xi| / min(|zeta - B|, |xi - B|) <= |zeta - xi| n^4/c, and the same
  with 0 and r_s. For the powers, zeta^{-k} - xi^{-k} =
  (xi - zeta) sum_{i=0}^{k-1} xi^{i-k} zeta^{-1-i}, so its modulus is at most
  k r_s^{-k-1}|zeta - xi|. Summing B^k/k times this over k <= m gives
  r_s^{-1} sum (B/r_s)^k <= 2 r_s^{-1} Q^m (Q > B/r_s, Q >= 2).
- The ceiling gives Q^m <= Q n^4 (1+B)/eps <= C n^4 (1+B)^2/eps. With eps < 1
  the per-pair change is at most C n^4 (1+B)^2 |zeta - xi|/eps. Summing gives
  (24). No path between the two points is needed: the bounds are direct
  differences at the two zeros.
- L307 last sentences (Jensen and contact do not bound the residual): a
  statement of scope, consistent with (29)-(30). HOLDS.

## Step 4 result: winding coefficients and forced singularities, (31)-(33)

**(32), L410-414: HOLDS.** Re-derived by two routes.
- Support. A changed monomial has a mod-two cycle S with odd intersection
  with every stack tau_{(x1,x2)} (the parity is the same for all stacks, see
  (4) in Step 7). At degree A = b^2 all exponents are 1, S has exactly one
  12-face per (x1, x2), and no other face. Closure at the 1-links and 2-links
  forces the (x3, x4) position to be constant between neighbouring stacks.
  So S is one flat 12-torus; there are b^2 of them, and each meets the
  twisted stack exactly once.
- Value, route 1 (Weingarten). Coherent orientation; each link appears once
  as U and once as U^dagger; the integral of U_ij conj(U_lk) is
  (1/2) delta_il delta_jk, the only contraction. Corner indices merge into
  one free index per vertex: integral of prod tr U_p = 2^{V-E} = 2^{A-2A}.
  With (1/2)^A from the normalized traces: 4^{-A}.
- Value, route 2 (independent). The links of the flat torus form a 2D
  lattice gauge field on a b x b torus. Migdal's formula with
  f = chi_{1/2}/2 (f_{1/2} = 1/2, d = 2, Euler characteristic 0) gives
  d^0 (f_{1/2}/d)^A = 4^{-A}. Same value.
- So Z_12 - Z_0 = -2 b^2 4^{-A} z^A + O(z^{A+1}); both are 1 + O(z), hence
  log R_b = -2 b^2 (z/4)^{b^2} + O_b(z^{b^2+1}).

**(33), L416-420: HOLDS.** Re-derived.
- rho_{1/2} = I_2/I_1: the coefficient of chi_j in e^{z cos theta} is
  I_{2j} - I_{2j+2} = 2(2j+1) I_{2j+1}(z)/z; the convolution eigenvalue on
  spin-j coefficients, normalized at j = 0, is I_{2j+1}/I_1;
  I_2/I_1 = z/4 + O(z^3).
- Min-max. With f = D^{-1} phi, phi in span(1, chi_p), <f, F f> =
  <phi, C phi> >= rho^4 ||phi||^2 (orthogonal eigenvectors, rho^4 <= 1) and
  ||f|| <= ||D^{-1}|| ||phi||. For real z > 0 and action 1 - w, ||D|| <= 1 and
  ||D^{-1}|| <= e^{3 n^3 z} -> 1; ||F|| <= 1. So F has at least 3n^3 + 1
  eigenvalues >= ||D^{-1}||^{-2} rho^4, hence 3n^3 normalized excited ones.
- X_T - 1 >= 3n^3 (z/4)^{4T}(1 + o_n(1)); log X_T >= (X_T - 1)(1 + o(1));
  J >= log X_T on real z > 0; J has contact 4T (Lemma ORD). Dividing by
  z^{4T} and letting z -> 0 gives [z^{4T}]J >= 3n^3 4^{-4T}.
- Precision (no change): the plaquette traces are orthogonal to each other
  and to the constant for every n >= 2 (a face not in the other face has a
  link used once); n >= 6 is harmless. The bound is not sharp: 2 log X_T
  contributes twice the plaquette count at this order, and J >= log X_T keeps
  half. Only the lower bound is used.

**Common zero-free disk, L422: HOLDS.** e^{z sigma_p w_p} = 1 + g_p with
|g_p| <= e^{|z|} - 1. Components of a plaquette set under shared-link
adjacency are link-disjoint, so Haar integrals factor, and the activity of a
connected set C is at most (e^{|z|} - 1)^{|C|}. The induction written after
(30) (see Step 7) then applies with the adjacency degree 20 of 4D plaquettes.
The bound uses only |sigma_p| = 1, so it is uniform for the twisted and
untwisted integrals and for both thermal boxes.

**Count, L424-428, hence (31) L401-408: HOLDS.** Re-derived.
- Lowest coefficient of H. Vortex: [z^{b^2-1}] H = -2 b^4 4^{-b^2}, so
  |.| = 2 V_0 4^{-D_0}. Thermal: [z^{4T-1}] H = 4T [z^{4T}] J >=
  4T 3n^3 4^{-4T} = 6 n^4 4^{-4T}. All lower coefficients are zero.
- P = prod over the N distinct uncanceled points in |z| <= R of
  (z - zeta)/(2R): |P| <= 1 there and |P(0)| >= (r_*/(2R))^N.
- |PH| <= C_{alpha,R} V_0 on |z| <= alpha R: the disk argument of (6) on a
  radius in ((1+alpha)R/2, R) bounds the analytic part by C V_0 (actions are
  at most 12 V_0); each pole term nu/(z - zeta) times P is at most
  |nu|/(2R); Jensen bounds the total |nu| by C_R V_0.
- PH is analytic, its lowest coefficient is P(0) h. Cauchy on radius
  alpha R: (r_*/(2R))^N c V_0 4^{-D_0} <= C V_0 (alpha R)^{1-D_0}. V_0
  cancels, so N log(2R/r_*) >= D_0 log(alpha R/4) - O_{alpha,R}(1). Divide by
  D_0, take the size limit, then alpha -> 1.
- L408 and L428 (zero-free continuation of the thermal ratio is impossible
  on such disks; contact plus volume growth cannot give a subarea criterion
  there): direct consequences of (31). HOLD.

## Step 5 result: neutral-momentum counts, (13)-(20), (25)-(27)

All statements here are marked conditional on (SD-cyl-CA) of row 865, which
is itself conditional on the account's named suppliers (Step 2). I checked
the implications by hand; the suppliers stay as they are recorded.

**(14), L168-173: HOLDS.** Each pair in the translation average is two
original tents at time separation t_2 a in [3d, 3d + 2a) with relative
displacement at most 2 sqrt3 d/100, so the support separation is about
2.5d, inside [d, 6d], and a ball of radius 5d holds the pair. Witness:
S = Z b_0 K*(1 + R), |R| <= 1/2, c_K r^2 <= K* <= C_K r^2 with r = d/4, one
common Z = Z_{K,s(d)}. Averaging gives G >= Z b_0 c_K r^2/2 and
G_1, G_2 <= (3/2) Z b_0 C_K r^2, so G_i <= 3(C_K/c_K) G. The absolute lower
bound uses the source's lower bound on Z (CA-I 2784-2789 as quoted at L212).

**L175-179 (energy and momentum cuts, zero-momentum consequence): HOLDS.**
Weight of G at E > C_1/d is at most e^{-C_1 a(u_2-u_1)} G_1 <=
C e^{-3C_1/2} G. The multiplier of the average over [-m, m] is
|sin((2m+1)pi k/n)| / ((2m+1)|sin(pi k/n)|) and |sin(pi k/n)| >= 2|k|/n for
|k| <= n/2. With 2m + 1 >= d/(200a) at fine cutoffs and J = ceil(C_2 L/d),
the multiplier squared at ||k|| > J is at most (100/C_2)^2, and the weight
there is at most that times G_2 <= C G. If (13) failed, all weight with
E <= E_* and ||k|| <= J would sit at k = 0, so the weight off k = 0 is at
most G/8, and the real part of the covariance at any lattice translation is
at least (7/8 - 1/8) G = 3G/4.

**L181-185 and (13): HOLDS.** M >= c_1 (D_0/d)^3 averaged little tents per
end, on a grid of spacing in [d, 2d]; each averaged support has radius at
most (1/4 + sqrt3/100) d < d/2, so they are disjoint; the sums have height
<= d/4 and slope <= 1. Every pair (i, j) is at time separation exactly t_2
and a lattice translation, so bilinearity gives S(F, H') >= 3M^2 G/4. Upper
bound: each of the four padded pairs (B_1 + F, B_2 + H') etc. is in
T(D_0; 1/300): mass ratio pi^2/2560 = 0.003855 > 1/300 with margin
(1 + d/D_0 <= 1.156 suffices), Lip <= 2 <= 75, separation about 1.5 D_0,
common ball 5 D_0. So |S(F, H')| <= C_{D_0}, with the source's upper bound on
Z at depth s(D_0), uniform in K. Since s(d) = O(1 + log(1/d))
(`port/p9-witness.md` L496), 3M^2 G/4 >= c D_0^6 d^{-4}/(1 + log(1/d))^2,
which exceeds C_{D_0} for small admitted d. The order (d, then the cutoff)
is as stated. Note: (14) says it does not compare running coefficients at
different scales; the contradiction at L185 does, through the source's two
absolute bounds on Z. This is what the text does, and the bounds are the
cited ones; no change.

**(15), L189-201: HOLDS.** w_l = |z| e^{i l arg z} is a unit neutral vector
with character l k. One coordinate k_i has 0 < |k_i| <= J, so its order in
Z/n is at least n/J, and l k are distinct and nonzero for l < n/J. The map is
l-Lipschitz: |w_l(X) - w_l(Y)|^2 = (|z_X| - |z_Y|)^2 +
4|z_X||z_Y| sin^2(l t/2) <= l^2 |z(X) - z(Y)|^2. So the u-step Dirichlet form
is at most l^2(1 - e^{-u a E_*}) and <w_l, U^u w_l> >= 1 - l^2 u a E_*. The
trace of the positive U^u dominates the diagonal on any orthonormal family
orthogonal to the vacuum; counting l with l^2 <= 1/(2uaE_*) gives (15). The
level statement uses -log(1 - x) <= 2x on [0, 1/2]. The comparison with
row 1161 (19) (s(u) >= c n^3 e^{-Cu} at beta >= 1) is correct.

**(16) and L212-249: HOLDS.**
- L212: s(x) is between constant multiples of l(x) for x <= D_max (both
  bounds in `port/p9-witness.md` L496; the lower uses C_W >= 1).
- L214-218: K(j - i) is the Gram matrix of U^{u_2/2} T_{hi} v, so PSD,
  |K(z)| <= G.
- (17): positive and negative coefficient sums are disjoint tent sums with
  height <= d/4 and slope <= 1, inside broad tents of radius x/4
  (2 sqrt3 m h + d/4 < x/4 holds since 2 sqrt3 R h/512 < R h/8 - h/4 for
  R >= 3). Padded pairs at scale x: centres 2x apart in space, at most 4d in
  time, separation about 1.5x, mass margin for large R. Sixteen witness upper
  bounds give (17).
- (18): E Y^2 = sum c_j^2, E Y^4 <= 3(sum c_j^2)^2, Hoelder gives
  E|Y| >= (sum c_j^2)^{1/2}/sqrt3; every row of I sees z_0 + I inside J'; the
  bound is for every sign choice. Then x^4/|I|^2 <= C d^4/R^2.
- (19): shells covered by (4R/m + 3)^3 boxes, a constant; for
  R <= d^{-1/2}, l(x) >= c l(d); larger shells cost C d, and d l(d)^4 is
  bounded; small offsets cost C G^2.
- Rank: diagonal of K_lo >= G/2 by the C_1 cut; Tr(A^2 - B^2) =
  Tr((A - B)(A + B)) >= 0 for 0 <= B <= A; rank >= (Tr)^2/Tr(.^2) >= N/(4C').

**(20), L252-258: HOLDS.** Averaged tents have disjoint supports at spacing
h (2(1/4 + sqrt3/100) d < d), the slope argument for disjoint nonnegative
pieces is right, and (17)-(19) carry over. The projection to E <= C/d and
||k|| <= c_2 L/(2 pi d) commutes with translations, so in each character
the translates span at most one vector, and the rank counts distinct
characters. The small cube has at most (1 + L c_1/(pi d))^3 characters.
Constants may depend on the fixed L (c_1 is chosen after L), as L210 allows.

**(25), L311-330: HOLDS.** The 4D array has disjoint supports; the complex
form splits into 16 positive pairs, each padded at scale x, so it is at most
C x^2/l(x)^2. The slab formula gives the entry
exp[-E a(b_r + b_s - t_2)] exp[i p (y_j - y_i)] (b_r a about x >> t_2 a), so
the form is the integral of |sum c e^{-Ea(b_r - t_2/2)} e^{i p y}|^2. Random
site signs give c M_s M_t^2 mu_d(E <= 1/x); the phase choice gives
c M_s^2 M_t^2 on a bin of side 1/x (phases vary by at most 0.03 over the
array of side x/50). With M_s >= c(x/d)^3, M_t >= c x/d and
G asymp d^2/l(d)^2 this gives the powers 3 and 6.

**(26), L332-338: HOLDS.** (25) at x = Kd removes E <= 1/(Kd) (mass at most
G/16 for large K), the cuts after (14) remove the high ends. The projected
Gram is G sum_k w_k e_k e_k^*; its HS^2 is at least N^2 sum w_k^2 and at most
C N by (19) and Gram domination, so sum w_k^2 <= C/N. Cauchy-Schwarz removes
the small momentum cube; labels below eta/N carry at most C_L eta and labels
above A/N at most C/A; at least N/(2A) labels remain, each with mass in
[eta G/N, A G/N], which is of order d^3 G.

**L340 (subsequential limits): HOLDS** as a statement about these damped
measures: mass bounded, energy tail C G e^{-(3d/2)E} by (14), momentum tail
from the multiplier, tightness, and the closed-set inequality.

**(27), L361-370: HOLDS.** d >= a q_K >= C_W(K - k_W) L^{-(K-k_W)}, so
s(x) <= s(d) <= K - k_W for d <= x <= D_max, which is the admission
K - s >= k_W; C_mesh >= 32/vartheta^2 pays a <= vartheta^2 x/32 (and
a <= x/8, m >= 1, h in [d, 2d]); D_max in the eventual H-depth tail gives the
other depth inequalities, since s(x) >= s(D_max). Then the proof of (16)
runs at this cutoff, and each of the c d^{-3} levels with E <= C/d gives
e^{-E a u} >= e^{-C a u/d} >= e^{-C} at time u, since a u <= d. a q_K -> 0 because C_W grows
polylogarithmically. L370 (the physical seed time need not lie in this
range): HOLDS.

## Step 6 result: excess selection between 0 and log 8, (1)-(3)

**(1), L19-29: HOLDS** (given Lemma W and Theorem S-w, both checked).
- Lemma W (b): W_w(a, B) = sum over (chi; m) in Sigma_w of
  Z_{chi,m} = Tr(T_{B,m}^a P_chi), eight positive terms that include (0; 0).
- Z_{chi,0} = (1/8) sum_e (-1)^{chi.e} Z^{(e;0)} <= Z_{0,0}, since twisted
  integrals are positive; so Z <= 8 Z_{0,0} <= 8 W_K.
- W_K <= W_M term by term ((-1)^{Pf} Z_B <= Z_B), or Z_{m,m} <= Z_{0,m}.
- Z_B <= Z: Z_{(k,m)} = sum_chi (-1)^{chi.k} Z_{chi,m} <= Z_{(0,m)} deletes
  the temporal part; three frames (time mu, then nu, then rho) delete all six
  components. So W_M <= (64/8) Z = 8Z.
- Equal pressures follow from (1); the common top eigenvalue is Lemma W (c).
- Wording precision (no change of substance): at L24, "their other seven
  terms are positive electric-sector traces" is literal only for W_P. For
  W_M the seven terms are the neutral traces of the seven magnetic boxes,
  and for W_K the sectors with electric character equal to the magnetic
  twist. Only their positivity is used.

**(2) with L41 and L43-48: HOLDS.**
- S-w with N >= 3, s < 1/5041, q = 5041 s: for D = 2^{k+1} N = 2^k n_0 and
  D <= L < 2D, S_w(D/2; L^3) <= q^{2^k}/71 = v. At L = d this is the stated
  input at time a = d/2. (Lemma Z3 of row 720 uses the sharper
  q^{2^k}/5041 at L = D; the weaker v is valid.)
- Lemma E' with b = d, a = d/2, h = x in [d, 4d]: exponent x/(d - a) <= 8;
  three directions give g(a; x_1, x_2, x_3) <= 512 g(a; d^3) <= 512 v; g does
  not increase with time and b >= a.
- The four one-side doublings of b^4 have spatial sides in {b, 2b}, inside
  [d, 4d) since b in [d, 2d). Each bracket 2 log W(t) - log W(2t) =
  2 log(1 + S(t)) - log(1 + S(2t)) lies in [0, 1024 v]; the identity
  16 F_0 - F_4 = 8(2F_0 - F_1) + 4(2F_1 - F_2) + 2(2F_2 - F_3) + (2F_3 - F_4)
  gives Phi_{2,w} in [0, 15360 v].
- D_w(b) = sum_h 16^{-h-1} Phi_{2,w}(2^h b) (the tail 16^{-h} D_w(2^h b) =
  b^4 [b_h^{-4} log W(b_h^4) - f] -> 0), and v_h <= v, so
  D_w in [0, 15360 v/15] = [0, 1024 v].
- Branch M: 8 W_M = Z + sum_{B != 0} Z_B. For B != 0 pick a time direction
  off one nonzero component, so m != 0; Z_B <= sum_chi Z_{chi,m} <=
  8 Z_{0,m}, and Z_{0,m}/lambda_b^b <= S_M <= v (W_M is frame-free and the
  cube is symmetric). So sum_{B != 0} Z_B/lambda_b^b <= 63 * 8 v = 504 v,
  W_M >= lambda_b^b, Z/W_M in [8 - 504 v, 8], and for 504 v <= 4,
  |log(Z/W_M) - log 8| <= 504 v/4 = 126 v. Then D = log(Z/W_M) + D_M =
  log 8 + O(v), and Phi_2 = 16 D(b) - D(2b) = 15 log 8 + O(v).
- The table is stated as v -> 0; for k = 0 and q near 1 one can have
  504 v > 4 (v < 1/71), which the text excludes by "for 504 v <= 4" and
  "as v decreases to 0". No change.

**(3) and L50-55: HOLDS, given its stated hypothesis** (the physical
Pfaffian seed with a strict uniform margin at one admissible size, or the
one-cube neutral test of row 1161).
- From the hypothesis: S-w propagates S_kappa; s <= S_kappa; the spatial
  enlargement at a fixed shorter time is row 1161 L150 (B3 for the
  Pfaffian transfer). Row 1161's finite-aspect theorem (L146) with
  s_0 = 1/2, J = [1/2, 1] and eps < 1/(8 * 5041) then gives at every fine
  cutoff alternative I (S_per(n/2) <= 8 eps) or II (S_full(n/2) <= 8 eps,
  row 1161 L178), a P or M seed with common q = 5041 * 8 eps < 1.
- With L = 2^k L_1, b = L/a_j = 2^k n_1 and v_k = q^{2^k}/71 uniform in j:
  P gives Phi_{2,j} <= 15360 v_k, M gives 15 log 8 + O(v_k). Both cannot
  hold once v_k is small.
- Infinitely many M cutoffs give limsup_j Phi_{2,j}(L/a_j) >= 15 log 8 -
  C v_k for every such L, so the lower limit over L is at least 15 log 8 and
  (3) fails. Finitely many M cutoffs give P seeds at all fine cutoffs with a
  common q < 1, which is (PHYS-SEED) at threshold 1/5041, hence (W)
  (ZD-c); and limsup_j Phi_2 -> 0. Under (W) itself, Lemma Z3 gives
  D^+(L) -> 0, which excludes infinitely many M cutoffs. So (W) iff (3).
  The same with D and log 8. (BDD-Delta) follows in both cases.
- L39 ("uniform exponential error"): v = q^{2^k}/71 with 2^k >= b/(2 n_0)
  is exponentially small in b. HOLDS.

## Step 7 result: everything else

**(4), L59-64: HOLDS.** Flipping the sign of one link preserves Haar and
multiplies each Taylor monomial by (-1)^{(number of its faces at that
link)}, so only mod-two cycles S survive. For the 2-links lambda at
x_1 + 1 (all x_3, x_4, fixed x_2), delta(lambda) = tau_{(x1,x2)} +
tau_{(x1+1,x2)} mod 2 (each 23- and 24-face of that plane holds two such
links), and <delta lambda, S> = <lambda, dS> = 0; so all b^2 stacks have the
same parity, each needs a face of S, and a changed monomial has degree at
least b^2.

**(5)-(8) and L95-99: HOLD.**
- L77: V(q) = E_x[e^{qS}], |V| <= e^{12 b^4 |q|}; Jensen on a radius in
  [2w, 3w] gives at most 36 b^4 w/log 2 zeros in |q| <= w.
- L79: on 3w/4 < r < w, log|g| <= 12 b^4 r, |g(0)| >= 1, gradient C b^4 on
  |q| <= w/2; reflected terms at most 3/r each; pole terms m/(z - zeta) have
  total |m| = O(b^4 w) and P removes each at cost 1/D. |P| <= 1 since
  |z - zeta| <= 2(B + w) <= D.
- (7): PH_b vanishes to order d = b^2 - 1 at 0, so |PH_b| <= C b^4 (2|z|/w)^d
  on |z| <= w/2; Hadamard's three circles at radii w/8, w/4, w/2 halve the
  exponent; centres move by w/16 (a w/8 disk about the new centre lies in the
  old w/4 disk), at most 2 + 16B/w times.
- (8): -log|sin| >= 0 is integrable over a period, so the angular average is
  at most (pi log 2/(2 theta_0)) M; log(D/|r - |zeta||) >= 0 has integral at
  most 2D, so the radial average is at most (2D/|I|) M.
- L95: the ray and the arc stay within B theta_0 < w/32 of [0, B];
  dist(s e^{i theta}, zeta) >= s|sin(theta - arg zeta)| and, on the arc,
  >= |r - |zeta||. For M <= c_* d the path bound C b^4 e^{-c_3 d} follows; the
  real part of the path integral of H_b is log R_b(r) because R_b(0) = 1 and
  R_b(r) > 0.
- L97: continuity of the finite-size seed in the coupling gives a common
  margin on I; row 1161 (14) gives R_b(x) <= (8/71) e^{-b log(1/q)/(2 n_0)}
  for x in I and all b >= n_0; this contradicts the path bound.
- L99: (5) holds for every w > 0, so liminf M_b(beta_j, w_j)/b^2 = 0
  excludes M at beta_j; P at every fine cutoff with a common q gives (W).

**(9), L103-112, and L114: HOLD.** Character projection and spatial gauge
averaging are contractions that keep O and the pairing <f, U h>. Cuts in
two planes differ by the gauge -1 on a slab of vertices, so f becomes odd
under every cut. On O-measurable data the partial flip of A_l equals the
cut. Affected plaquettes: |dA_l| spatial (transverse edges with one end in
A_l) and 2|A_l| temporal; none reads two planes (an ij-face has both
i-links in one plane). Haar gives equal weights to the orbit signs, the
conditional law is prod e^{eps_l J_l}, and E[f | orbit] = f_ref prod
tanh(J_l). Cauchy-Schwarz, the long-cylinder limit and Uh = b_h h give the
first bound. log tanh x = -2 artanh(e^{-2x}) <= -2e^{-2x},
2|A| + |dA| <= 6|A| and Jensen give the second. L114: with
sum|A_l| <= (1 - eps) n log n/(12 beta), the exponent is at least 2n^eps.

**(10), L116-121: HOLDS.** A full-plane flip of the input leaves every
spatial face (two flipped i-links each) and the magnetic multiplier
invariant, and flips the A_i temporal 0i-faces of that plane once each.
Averaging gives cosh J for the unsigned kernel and sinh J for a charged
input; |sinh J| <= tanh(beta A_i) cosh J; |f|, |g| are physical, so the
unsigned form is at most lambda_m ||f|| ||g||. **L123 (OPEN): HOLDS** as
stated (tanh(beta n^2)^{rn^2} -> 1; identity fields saturate J).

**(11)-(12), L127-150: HOLD.** k = e^{-2 beta} e^{beta(1+w)}; the relative
tail is P(Poisson(s) > d) <= (es/(d+1))^{d+1} <= 2^{-(d+1)} for
s <= 2 beta <= (d+1)/(2e) (Chernoff with t = log((d+1)/s) >= 0).
(1 - eta/p)^p >= 1 - eta gives 0 <= C - C_d <= eta C for the product
kernels. C_d commutes with gauge maps and with cuts (x.(-y) = (-x).y),
and these act linearly on each link, so ran F_{d,+} lies in V_{d,+}.
Q B = Q(F_+ - F_{d,+}) F_+^{k-1} has kernel at most eta B pointwise; the
two-block identity gives ||B||^2 - ||Pi B Pi||^2 = 2||Q B Pi||^2 +
||Q B Q||^2 <= 2||QB||^2. ||Q psi|| <= eta and B >= lambda^k |psi><psi|
give (1 - eta^2) lambda^k <= ||A||. The spectral statement
||Q 1_{[r,1]}(F_+/lambda)|| <= eta/r follows as written.

**L152-156: HOLD.** G^{-1/2} T G^{-1/2} is similar to the matrix G^{-1} T
of A. With Tr A^2/||A||^2 <= (3/2)(1 - 2 eta^2), (12) gives
Tr_+ U^{2k} <= 3/2 at 2k = 2 floor(n/1024) <= floor(n/512), and the trace
decreases in time. Degree bound: the Joukowski map u -> (u + 1/u)/2 sends
|u| = 1 onto [-1, 1] and u = 3 - sqrt8 to 3, so |h(3)| <= (3 + sqrt8)^d
||h||; with h(y) = p((y - 1)/2) this gives d >= (beta - 2 log C)/
log(3 + sqrt8). Dimension: products of traces of disjoint plaquettes are
orthogonal (an unshared face has a zero-mean independent trace) and have
per-link degree 1. The matrix example has entries (1 - delta)/m off the
diagonal and eigenvalues 1, delta (m - 1 times).

**(21), L262-273: HOLDS.** With S_i uniform under the parity condition,
E[F | prod S = +-1] = E F +- E[F prod S]; single-site factors give c and
lambda p sinh(bz), so the conditioned transforms are c^A +- s^A, and with
e^{-Abz} these are Laplace transforms on [0, 2Ab]. Contact is exactly A
(leading term 2(lambda p b)^A z^A). For real B > 0, c - s >=
1 - p + p e^{-bB} > 0. lambda = 1: 1 - t = (K + e^{-bB})/(K + cosh bB),
so -log R = (B - x_*) b - 2 log b + O(1). lambda < 1: t < lambda and
1 - R <= 2 lambda^A. Roots: s/c = omega gives
(lambda - omega) y^2 - 2 omega K y - (lambda + omega) = 0 with y = e^{bz};
the large root has |y| comparable with K, so z is within O(1/b) of x_*;
c = 0 would force y = +-1, where c is proportional to K +- 1 != 0; distinct
omega give distinct points, and exactly one of c^A +- s^A vanishes at each.
The guide run found the 2A points distinct at b = 6.

**Moment obstruction, L344-357: HOLDS.** Conditioning on the other links
and substituting the plaquette holonomy is a linear orthogonal change of
one link's quaternion coordinates, so the residual degree stays <= d_0;
conjugation averaging gives a polynomial of degree <= d_0 in cos theta;
sin^2 theta adds two; sign cos(K theta) has only frequencies in K(2Z + 1).
P_rho = sum_A rho^{|A|} |h_A><h_A| is positive, Markov (E h_p = 0) and
gauge invariant; compressed multiplication by an allowed polynomial is the
scalar int P (h_A h_B = h_{A sym-diff B}). So all such multitime
correlations factor for every rho, while the neutral traces are
(1 + rho^u)^M and 1.

**(28), L374-383: HOLDS.** (16) at one fixed admitted d gives
X_T - 1 >= c d^{-3} e^{-CL/(2d)}, and J >= log X_T. With a complete
pairing, J <= C n^4 (1+B)^2 d_sum/eps + C eps; eps = delta_L/(4 max{C,1})
leaves at least 3 delta_L/4 for the matching term, which gives (28).

**(29)-(30), L385-397: HOLD.** The plaquette-sign map is a group
homomorphism from link signs, so every fiber has 2^{V+3} elements (gauge
2^V/2 times holonomies 2^4); this gives both sides of (29), with 6V
plaquettes. With V_T = n^4/2 and V_{2T} = n^4 the main terms give exactly
3 log 2, and the error is O(n^4 e^{-J_0 beta_j}) = O(n^{-1}) for
J_0 beta_j >= 5 log n (beta_j asymp log n by (RF25)). The product with
Wilson adds J_Y to J and leaves Wilson correlations unchanged; the Z_2 action
(J_0/2)(1 - sigma_p) is reflection positive. L397: the electric character
ratio is tanh(J_0 z/2); even subgraphs start at length 4 (Lemma ORD's
argument gives contact 4T); the polymer induction is the standard
Dobrushin-Kotecky-Preiss type: Z(Lambda) = Z(Lambda \ p) + sum over closed
connected C containing p of v^{|C|} Z(Lambda \ (C u N(C))), each ratio costs
at most 2^{(Delta+1)m}, connected sets of size m through p number at most
max(2, Delta)^{2m}, and the series is below 1/2 for small |v|.

**Semigroup example, L432-436: HOLDS.** The 1D Poisson kernel
(1 - r^2)/(1 - 2r cos theta + r^2) is positive; P_t P_s = P_{t+s} by
Q_t Pi = Pi; the trace at L/2 is e^{-mL/2}[((1 + e^{-pi})/
(1 - e^{-pi}))^3 - 1] (sum over Z of e^{-pi|k|}); ((1+r)/(1-r))^3 - 1 >= 6r;
6 e^{-pi} = 0.259 > 1/1650. The band data (25)-(26) can be placed in both.

**GUIDE and OPEN lines.**
- L3, L5 (repo search, external citations): GUIDE; the lane-internal links
  resolve; I did not re-read the external PR or account lines.
- L9, L15: GUIDE framing; accurate.
- L13: GUIDE summary of row 1161; accurate, with two precisions: row 1161
  has since been checked (row 1162, HOLDS AFTER CORRECTION, credit only),
  and its explicit K = 512 test is proved on the range 4 | n, n >= 2^70
  (row 1161 L215), which L13 and L152 leave implicit. On the trajectory
  n -> infinity, so no step changes.
- L11 (target), L438 (remaining estimates): OPEN, consistent with the
  proved content.
- L441 (RESULT): accurate as a summary of what the file proves; with this
  check it is no longer "unchecked".

## Step 8 result: verdict table

Conditional statements keep their stated hypotheses: (W)-equivalences use
Theorem ZD-c of row 720 and Theorem S-w; (13)-(20), (25)-(28) use
(SD-cyl-CA) of row 865 and its open suppliers; (3) uses the Pfaffian seed
or the one-cube neutral test of row 1161.

| # | Statement | Lines | Verdict |
|---|---|---|---|
| 1 | (22) finite zero sum with analytic error | L277-290 | HOLDS |
| 2 | (23) (W) iff the signed zero test, quantifiers | L292-301 | HOLDS (given ZD-c) |
| 3 | (24) matching estimate | L303-307 | HOLDS |
| 4 | (32) first vortex coefficient | L410-414 | HOLDS (two derivations) |
| 5 | (33) first thermal coefficient | L416-420 | HOLDS (not sharp; lower bound only) |
| 6 | Common zero-free disk r_* | L422 | HOLDS |
| 7 | (31) area and linear counts in disks of radius > 4 | L401-408, L424-428 | HOLDS |
| 8 | (14) one-scale weight and ratios | L168-173 | HOLDS (conditional) |
| 9 | Energy and momentum cuts, zero-momentum consequence | L175-179 | HOLDS |
| 10 | (13) moving neutral state | L160-166, L181-185 | HOLDS (conditional) |
| 11 | (15) levels l k and the trace floor | L189-201 | HOLDS (conditional) |
| 12 | (16) count c d^{-3}; witness bounds | L205-212 | HOLDS (conditional) |
| 13 | Translation Gram matrix | L214-218 | HOLDS |
| 14 | (17) signed sums on separated boxes | L220-226 | HOLDS |
| 15 | (18) random-sign payment | L228-234 | HOLDS |
| 16 | (19) sum of squared entries | L236-241 | HOLDS |
| 17 | Rank in the energy window | L243-249 | HOLDS |
| 18 | (20) distinct momenta | L252-258 | HOLDS (conditional) |
| 19 | (25) energy and bin upper bounds | L311-330 | HOLDS (conditional) |
| 20 | (26) many sectors in both bands | L332-338 | HOLDS (conditional) |
| 21 | Subsequential limits | L340 | HOLDS |
| 22 | (27) short-time floor with explicit admission | L361-370 | HOLDS (conditional) |
| 23 | (1) sandwich of W_P, W_M, W_K | L19-29 | HOLDS (wording precision at L24) |
| 24 | (2) table and the shape details | L31-41 | HOLDS |
| 25 | Branch M: 504 v and 126 v | L43-48 | HOLDS |
| 26 | (3) branch selection by the ordinary defect | L50-55 | HOLDS (given its hypothesis) |
| 27 | (4) contact b^2 | L59-64 | HOLDS |
| 28 | (5) statement and conclusion | L66-71, L97 | HOLDS |
| 29 | (6) pole removal | L73-79 | HOLDS |
| 30 | (7) transport | L81-85 | HOLDS |
| 31 | (8) angle and radius choice | L87-93 | HOLDS |
| 32 | Path estimate | L95 | HOLDS |
| 33 | Weaker complex selection criterion | L99 | HOLDS |
| 34 | (9) one-slice charged reading | L103-112 | HOLDS |
| 35 | Logarithmic-width consequence | L114 | HOLDS |
| 36 | (10) one-step charged bound | L116-121 | HOLDS |
| 37 | OPEN on the full-cube cap | L123 | HOLDS as stated |
| 38 | (11)-(12) compression | L127-138 | HOLDS |
| 39 | Kernel comparison | L140-148 | HOLDS |
| 40 | HS and top-eigenvalue estimates | L150 | HOLDS |
| 41 | What would suffice at one size | L152 | HOLDS |
| 42 | Degree lower bound | L154 | HOLDS |
| 43 | Dimension and the matrix example | L156 | HOLDS |
| 44 | (21) parity models | L262-273 | HOLDS |
| 45 | Moment obstruction | L344-357 | HOLDS |
| 46 | (28) matching cost at fixed L | L374-383 | HOLDS (conditional) |
| 47 | (29)-(30) Z_2 comparison | L385-395 | HOLDS |
| 48 | Analytic inputs for the Z_2 factor | L397 | HOLDS |
| 49 | Semigroup example | L432-436 | HOLDS |
| 50 | GUIDE framing and searches | L3, L5, L9, L15 | GUIDE (external lines not re-read) |
| 51 | GUIDE summary of row 1161 | L13 | HOLDS, with two precisions |
| 52 | OPEN target and remaining estimates | L11, L438 | HOLD |
| 53 | RESULT line | L441 | HOLDS as a summary |

Counts: 53 statements: 52 HOLD, 1 is GUIDE (item 50; its external lines
were not re-read). None HOLDS AFTER CORRECTION. None FAILS.

Precisions recorded (no mathematics changes):
1. L24: "positive electric-sector traces" is literal for W_P; for W_M and
   W_K the seven terms are the neutral sectors of the magnetic boxes and the
   sectors with character equal to the twist. Only positivity is used.
2. L13 and L152: row 1161 is now checked (row 1162, commit e5ce9ba95,
   after the pinned b61681c80); its explicit K = 512 test is proved for
   4 | n, n >= 2^70.
3. (33) is a lower bound with half the leading plaquette count; it is all
   that (31) needs.
4. L173 says (14) compares no running coefficients at different scales;
   the contradiction at L185 does compare them, through the source's two
   absolute bounds on Z (CA-I 2784-2789 as quoted at L212). The text uses
   exactly those bounds.

What stays open, as the file says: the strict physical upper bound in (23)
at one size (equivalently (W)); the exclusion of the log 8 branch; the
suppliers of (SD-cyl-CA); the Jaffe-Witten mass gap. No mass gap is claimed
here.

Provenance: checked by hand by Claude Opus 5.5 (max effort), laptop
subagent, as FINISH row 1164, a cross-provider check of row 1163 (an astra
file by its name, a different provider). A numeric guide run was used only
for elementary constants. No commit, push, checkout or stash was run.

RESULT: HOLDS - check of row 1163 (`library/gap-solve10-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1164, positive claims first: 53 statements, 52 HOLD and 1 GUIDE (external lines not re-read), none HOLDS AFTER CORRECTION, none FAILS; in particular (22) and (24) hold, (23) is equivalent to (W) given Theorem ZD-c and its two-stage line, the first winding coefficients (32) and (33) hold (32 by two derivations) and force the counts (31) in every disk of radius above four, the neutral-momentum counts (13)-(20), (25)-(27) hold as implications from (SD-cyl-CA), and the excess selects 0 or log 8 under the stated seed, giving (W) iff (3); four precisions are recorded (L24 wording, row 1161 now checked with range n >= 2^70, (33) not sharp, L173 versus L185); OPEN: the strict physical bound in (23), hence (W) and the mass gap.
