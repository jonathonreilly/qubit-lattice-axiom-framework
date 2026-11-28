lead: anthropic/claude-opus-5-5/high laptop-subagent (row 1429)

Provenance: started 2026-11-23T01:36:58Z (date -u). Checker: Claude Opus 5.5.
Checked file: library/gap-rg-ring-sign-astra62.md (row 1425, 232 lines),
written by gpt-6.2-astra. Scratch producers are in the scratch folder of row
1425; they are treated as untrusted data. My runs use a fresh copy in my own
scratch folder, run as `python3 -I`. Research text only; no status is granted.

## Plan

1. Read row 1425 in full, then rows 1424, 1421, 1418 and Lemma T where cited.
2. Check items 1-7 of the brief in order.
3. Read each producer before running it. Copy to my scratch folder. Run those
   that fit (under 20 min, under 2 GB). Compare to the logs.
4. Recompute the degree-16 coefficient by my own route.
5. Ranked defects, outcome paragraph, RESULT line.

## Steps

### Step 0. Reading (done 01:47 UTC)

I read row 1425 in full (232 lines), row 1424 in full, and the cited parts of
row 1421 (the bound A(beta) < 2, the interval 136/157 <= b < 87/100) and
Lemma T. I read all eight producers in full before running any. Copies were
made into my scratch folder (SHA-256 recorded in my scratch notes). The copies
run through a small runner of my own, because `python3 -I` drops the script
folder from the import path. No producer was edited.

### Item 1. Frozen response and acceptance test: HOLDS (re-derived)

From row 1424 (7) and its two trace formulas, with the common constant
c = 2 C_2 / 9 for both rings: Y_grp = c E W and
Y_alt = c E[2 (h.k)^2 - W] = (4 C_2/9) E T - (2 C_2/27) E W. So
Y_alt = Delta_d - rho_d, as written in lines 28-32. The magnitude decreases
strictly iff |rho - Delta| < rho, that is 0 < Delta < 2 rho, that is
0 < E T < E W / 3. Also g_d = |1 - 6 E T / E W|. Each ring holds h twice and
k twice, so strand orientation signs cancel and the relative sign of the two
rings is fixed. The test is set out in the text (lines 26-35) before any
evaluation section, and line 35 states it was saved first. I cannot check
that time order from the files. The file times only show that all logs came
before the note.

### Item 2. Conditional four-link integration: HOLDS (re-derived)

- Free links. P's free links have x3 = x4 = 0 and touch only e1, e2, e1+e2.
  Q's free links have x1 = x2 = 0 and touch only e3, e4, e3+e4. They share no
  vertex, so no face holds links from both pairs. A link of the cube {0,1}^d
  lies in d-1 internal faces, so d-2 remain after the marked square. Hence
  |S|, |V| <= (d-2) beta. The density factorizes, so the pairs are
  conditionally independent, and their normalizers stay inside the outer
  Wilson integral.
- Convolution. With S = s g1 and V = v g2, S.X + V.(X^{-1} H) = X.(S + H V-bar).
  Also |S + H V-bar|^2 = s^2 + v^2 + 2 s v q(G^{-1} H) with G = g1 g2. This
  gives the stated density A(sqrt(...)).
- Quadrupole form. Conjugation by the U(1) subgroup through G fixes the
  density. So the traceless second moment of h is a (n n^t - I/3).
- a >= 0. At fixed q(H) = cos(theta), G.H = c' + e' t with t = n.omega
  uniform on [-1,1] and e' >= 0. With phi = (1-t^2)^2/8 one has phi'' = P_2
  and phi = phi' = 0 at t = +-1. So the integral of P_2 F equals the integral
  of phi F'', and F'' >= 0 because A(sqrt(x)) has nonnegative Taylor
  coefficients and c + e t >= 0.
- Minimum principle. The 4D Laplacian in S of exp(S.X) is |X|^2 exp(S.X),
  which equals exp(S.X) on unit quaternions. So (Delta_S - 1) f = 0, and a
  negative interior minimum is impossible. Doing S then V reduces each test to
  |S| = |V| = R. On that sphere the mean of P_{2,l} is
  (3/2) a ((l.n)^2 - 1/3) <= a. So a <= eta W_1/Z on the sphere implies the
  test integral is >= 0 on the whole product of balls.
- Contraction. With E[h h^t] = a_H Q_n + m_H I/3 (and the same for k), I get
  E[(h.k)^2 | ext] - m_H m_K/3 = a_H a_K ((n_H.n_K)^2 - 1/3). The bracket lies
  in [-1/3, 2/3]. This gives exactly the table rows on lines 103-106.

### Item 3. Character formulas and tails: HOLDS (re-derived)

- e^{R q(g)} = sum (n+1) L_n(R) chi_n(g). Convolving two centred kernels gives
  sum (n+1) L_n(R)^2 chi_n(G^{-1} H). Dividing by A(R)^2 = L_0(R)^2 gives
  a_n. Integrating against e^{beta q(H)} gives Z = sum a_n L_n(beta) U_n(u).
- W_1 = Z - d^2 Z / d beta^2, because the source stays along e_0. From the
  Bessel equation for I_{n+1}, beta^2 L_n'' + 3 beta L_n' =
  (beta^2 + n(n+2)) L_n. This gives the stated bracket. The series weight
  6k + n(1-n) is correct.
- D. At b = beta e_0 + y, only the term U_n''(u) (g.y)^2 / (2 beta^2)
  survives the spatial traceless projection. This gives
  beta^2 D = (1-u^2) sum a_n L_n U_n''.
- Tail. GL4 gives b_n(R) <= (R/2)^n / n!. The test functions are bounded by 1
  (for D the test (3/2)((n.h)^2 - |h|^2/3) has modulus at most 1), and
  A(beta) < 2. So the bound 4 (513/256)^2 (R/2)^42 / (21!)^2 holds. The ratio
  of successive terms is below 1/2 also for d = 5.
- Code. I read conditional_ring.py against these formulas. The Chebyshev
  recurrences for U_n, U_n', U_n'' are right. The Taylor remainder factor
  (2(6(K+1) + n(n-1)) + 12) term_{K+1} is right. Rounding is outward. Both
  denominators are asserted positive in every box. The rerun is in item 8.

### Item 4. The C_4 x C_4 torus contraction: HOLDS (re-derived, and recomputed by my own network)

- Geometry. The graph of {0,1}^4 is C_4 x C_4. The 16 mixed faces tile the
  torus. The four 12-faces are the rows and the four 34-faces are the
  columns. Each of the 32 links lies in two mixed faces and one circuit. P is
  row 0 and Q is column 0 through the root. Every triangle/parity rule on
  lines 114-116 and 163 follows from one Haar integral per link.
- Marked insertion. I re-derived the coefficient matrix -4 b_n Q^{ab}(J)/beta^2.
  Write b.U = |b| q(g_b^{-1} U) with b = (beta, t). Only the second-order
  term (1/2)(2 i t.J / beta)^2 of D_n(g_b)^{-1} survives the traceless
  projection. The |b| dependence is isotropic. The contraction of two such
  insertions gives T = Q(h):Q(k).
- K. Using [J_i, J_j] = i e_ijk J_k on separate factors, I get
  sum_ij Sym(A_i A_j) Sym(B_i B_j) = (A.B)^2 + (A.B)/2. So
  K = J_a.J_b (J_a.J_b + 1/2) - C_a C_b / 3, as on line 120. The mixed matrix
  element (C_s + C_t - C_r - C_u) O_ru / 2 follows from
  C_s = C_r + C_u - C_t + 2 J_a.J_b. The code in `marked` inserts the r-basis
  resolution correctly, with the right triangle weights dl, dr.
- Rationality. Over the torus each triangle factor of `local` appears once
  in a numerator and once in a denominator after the shift
  (i,j) -> (i-1,j) or (i,j-1). The sqrt((u+1)/(r+1)) factors cancel the same
  way. So the product is rational, as claimed.
- Orbit folding. The reflection fixing the root maps face column i to 3-i.
  That is `v[::-1]`, so the fold is right.
- Independent recomputation. I wrote my own network in pure Python. It
  builds explicit spin-n/2 matrices. It finds each link's invariant vector as
  the null space of the total generators (no 6j symbol, no CG formula, no
  phase convention borrowed). It contracts the four link ends at each vertex
  numerically. For every one of the 2046 marked configurations through spin
  order 24, my value times prod (n+1) equals `recouple.geom` to relative
  error below 1e-14. The same holds for all 33 vacuum configurations through
  order 10. Floating point: this is a guide, not a proof.
- Independent enumeration. I wrote my own enumerator (row-major cells,
  direct triangle tests per link). Its configuration sets equal those of
  `recouple.arrays` exactly at marked order 26 (5568 sets) and vacuum order
  22 (3516 sets). My first version had a pruning bug that double-counted a
  cell floor. It gave 30 instead of 62 at order 18. After the fix the sets
  agree. I record this because agreement is only as good as the two codes.

### Item 5. Circle bound, evenness, Cauchy remainder: HOLDS (re-derived; producer rerun)

- Entire and even. b_n <= (beta/2)^n / n!, so each face series is entire.
  The link sign (-1)^{sum_{j<i} x_j} multiplies every plaquette by -1 (the
  four signs give sigma_i(x)^2 (-1)^{2s+1}). Haar is invariant under the
  central -1 and chi_n(-g) = (-1)^n chi_n(g), also for the marked matrix
  series. So N(-z) = N(z).
- Temporal gauge. Gauge moves at the upper sites fix the 8 axis-4 links to
  1 and do not move the root, so T(H, K) is unchanged. P is a lower face.
  K = U_e V_e^{-1} on the axis-3 edge from the root.
- Norms. Convolution by sum c_n chi_n acts on spin n/2 by c_n/(n+1). So each
  ordinary crossing has norm sup lambda_n t^n = M. For the marked crossing,
  sum_ij (J_i J_j)^dagger (J_i J_j) = C_n^2, and the symmetric traceless
  projection is an orthogonal projection on the nine-tuple. With
  4/beta^2 <= 1 this gives M_Q. Schur gives the integral of |F_z|^2 = P and
  of sum |G^{ab}|^2 <= P_Q.
- Sphere gluing. For the six faces of a three-cube, Migdal's formula on the
  sphere gives sum_k (k+1)^2 prod_p mu_k^(p). Cutting one face bounds this by
  (integral of the first face function) times sup |phi^{*5}|. The bound
  sup |phi^{*5}| <= sum (k+1)^2 alpha_k^5 = E_5 follows. Cauchy-Schwarz in
  the direct sum over (a, b) gives the stated circle bound.
- Tail rule in circle_tail.py. sum_k (k+1)^2 alpha_k = (sum (n+1) b-hat_n)^2,
  so dropping indices above 24 costs at most (2 S_0 + E) E. Also
  alpha_k <= P, by integrating F^2 against chi_k / (k+1). This holds even with
  the outward-rounded B_n. The mean value step gives 5 P^4 (2 S_0 + E) E.
  The ratio test for E holds at every radius used.
- Remainder. With evenness, |N(1) - N_{<=46}(1)| <= sup t^{-48} / (1 - t^{-2}).
  The rerun of circle_tail.py reproduced circle.log byte for byte. The
  bound at t = 11/4 is 216821257148. The tails are 1543100 and 204047 in
  units of 1e-15.

### Item 6. Vacuum interval, division, final table: HOLDS (recomputed)

- The vacuum core (order 28, 128 cells) and the vacuum circle bound at 9/4
  give z_B in [1256270903611467, 1260000404969567] / 1e15. This is positive.
  I checked the endpoint additions by hand. The degree-6 shell equals
  8 b_1^6 / 16 (eight three-cubes). At beta = 2 this is 0.21127, inside the
  logged cell range.
- Division. With N < 0 < Z, [l_N / l_Z, u_N / u_Z] is the right outward
  quotient. Delta = b^9 E T / 144 follows from C_2 = b^9/64. The b endpoints
  are used in the right order for a negative moment. For g_4 - 1 =
  -6 E T / E W, the bounds use E W <= 1 and E W >= w_*^2 (from conditional
  independence and the minimum principle for W_1 - w_* Z).
- The rerun of quotient.py from my own regenerated logs reproduced
  quotient.log byte for byte, and with it every row of the final table.

### Item 7. U(1) zero and 5D statements: HOLDS (read and re-derived)

- U(1). A fixed-charge line carries a 1 x 1 holonomy, so the traceless part
  (G - q(G) I) vanishes before integration. This is a definitional zero, as
  in row 1424. The ratio g_d is undefined there, as the text says.
- 5D. Only the conditional bounds enter. With eta = 2934/10000,
  2 - 8 eta^2 = 1.31133152, so 2 g_5 > 13/10 on the band. The moment
  interval [-xi^2/3, 2 xi^2/3] crosses zero, as stated. No 5D torus
  computation was attempted or claimed.

### Item 8. Independent recomputation and reruns

Degree-16 coefficient, by my own route. I summed my own enumeration of the
order-16 supports, my own network values, and the leading term
b_n ~ (beta/2)^n / n! with the factor 16/beta^4. Result 9.259167114772439e-11.
The claimed 15655/169075682574336 = 9.259167114772466e-11. Relative
difference 3e-15. The per-support values also match the sphere fixture's list
(4 x -5/195689447424, 4 x 5/1320903770112, 2 x 5/86973087744,
1 x 5/77309411328). The all-fundamental term is 5/(72 * 4^15).

Degrees 18 and 20 as well. The rejection rests on a near cancellation
between spin shells 16 (+4.16e-7) and 18 (-4.23e-7), so one coefficient is
not enough. From groups34.txt, with exact Bessel series, I get the Taylor
coefficients -142165/1352605460594688 (degree 18) and
23134903/389550372651270144 (degree 20). My network and enumeration give
the same values to relative 2e-15. This uses only configurations up to
order 24. That range is covered in full by item 4's comparison.

Marked formula, numerically. At random SU(2) points and beta = 2, the
expansion sum_n (n+1) L_n tr(-4 Q(J_n) D_n(U)) / beta^2 reproduces
e^{beta q} Q(h) to 6e-9 absolute (this error comes from my truncated
matrix exponential). The trace identity for T used by the sphere fixture
holds to 3e-16 on 1000 random pairs.

Producer reruns (copies in my scratch folder, `python3 -I` through my
runner, peak memory below 60 MB, longest run 149 s):

| Run | Result |
|---|---|
| conditional_ring.py | conditional.log byte-identical |
| circle_tail.py | circle.log byte-identical |
| spin_order.py 16, 24 | logs identical |
| recouple.py 34, 40, 42 | counts and degree-16 lines identical; groups34/40/42.txt and groups42.local byte-identical |
| recouple.py 28 vacuum | vacuum28.txt and .local byte-identical |
| evaluate.py 34 64, 40 128, 42 512, 28 128 vacuum | evaluate34/40/42.log and vac-eval28.log identical |
| sphere_fixture.py | sphere.log identical |
| magnetic_check.py (groups42.local, vacuum28.local) | 1689 passed, 295 marked; identical |
| quotient.py (fed my regenerated logs) | quotient.log identical |

The cell count of the evaluate34 run is not stated in the note. My run used
64 cells and reproduced the log. No run was skipped for size.

Wider samples (done 02:00 UTC):

- Enumeration. My enumerator's sets equal `recouple.arrays` exactly at
  marked order 30 (35381 configurations) and vacuum order 28 (30034, the
  full vacuum core used). From marked order 32 to 42 completeness rests on
  `recouple.arrays` alone. I read its pruning and found it valid: column
  totals and circuit minima only grow, and the size loop breaks on sorted
  totals.
- Network against `geom`. Every 47th marked configuration of orders 26-34
  (3988 checked, spins up to 5/2) and every 7th vacuum configuration of
  orders 0-28 (4290 checked) agree to relative 1e-14. None disagree.

### What I re-derived, recomputed, or only read

- Re-derived: items 1-7, except the row-1424 constants below.
- Recomputed by my own code: the degree-16, 18 and 20 Taylor coefficients;
  the torus values of 2046 + 3988 marked and 4290 + 33 vacuum
  configurations; the configuration sets through marked order 30 and vacuum
  order 28; the marked-face expansion; the T identity.
- Rerun unchanged: all eight producers (table above).
- Only read: row 1424's prefactor C_2 = b^9/64 and the shared constant
  2 C_2/9 of the two rings. These set the Delta units in the table. They do
  not affect the sign of E_4 T or the value of g_4. Also only read: row
  1421's bounds on b and on A(beta).

## Ranked defects

1. No kernel replay. Every enclosure is Python exact-integer outward
   arithmetic. That is proof-grade under the brief's rule, but it is not
   Lean-checked. Row 1425 says so (lines 49, 227).
2. Completeness of the spin enumeration at orders 32-42 has one
   implementation. My independent enumerator stops at order 30 (marked) and
   28 (vacuum). The higher shells together contribute about -1e-9 against a
   total of -2.4e-8, so an omission there would have to be large to matter.
3. The verdict rests on a near cancellation. Spin shells 16 and 18 are
   +4.16e-7 and -4.23e-7. The net -2.4e-8 is about 6% of each. The certified
   interval [-2.58e-8, -2.30e-8] still stays far from zero, and my
   degree-16/18/20 checks cover both shells.
4. The effect is tiny. g_4 - 1 lies in [1.09e-7, 4.84e-7]. The ring
   coefficient equals its reference to seven digits. The sign is certified,
   but the channel is essentially null in 4D.
5. The claim that the convention was frozen before evaluation (line 35)
   cannot be checked from the files.
6. Row-1424 constants (C_2, and one prefactor shared by the two rings) were
   used here as read. They enter Delta_4 and Delta_5, not g_4.
7. Wording, lines 122 and 157: "unnormalized numerator" means before the
   vacuum division. The faces are already divided by A(beta).
8. The cell count of the evaluate34 run is not stated (64 reproduces it).

No item FAILS. I found no line of row 1425 that needs a correction.

## Outcome

The ring is rejected as a four-dimensional decrement. Every step from the
frozen test to the final table holds on my reading. My own torus network,
my own enumerator and my own Taylor sums reproduce the producer's support
values and the degree-16, 18 and 20 coefficients to 1e-14. Each producer
rerun reproduces its log byte for byte. On the whole band, E_4 T is in
[-2054, -1829]/1e11 < 0. So Delta_4 < 0 and the alternating coefficient
moves away from zero: g_4 > 1. In 5D, 2 g_5 > 1.311. The proof-grade standing
waits only on the kernel replay of the integer certificates and on a
second check of enumeration completeness above order 30.

RESULT: HOLDS (items 1-8, no corrections). Row 1425's rejection of the ring as a 4D decrement stands: E_4 T in [-2054,-1829]/1e11, g_4 - 1 in [109,484]/1e9, 2 g_5 >= 1.311. Degree-16 coefficient 15655/169075682574336 reproduced by an independent network to 3e-15. Lean replay still open.
