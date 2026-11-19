# Check of gap-solve11-astra62.md (FINISH row 1166)

Status: complete. Checker: Claude Opus 5.5, max effort, laptop subagent.
Task: check row 1165 (`library/gap-solve11-astra62.md`) line by line, by hand.
Positive claims first. A numeric run guides only.

## Plan (eight steps)

1. Read the setting (`library/gap-council-brief.md`) and the file under check in full.
2. Read the cited parts of rows 1145-1163 (`gap-solve2..10`) and their checks.
3. Check the equivalence of the strict wall with (22).
4. Check the reconstruction (23).
5. Check the query-complexity bounds in the competing magnetic branch.
6. Check the singularity count (25).
7. Check everything else, statement by statement.
8. Verdict table and the RESULT line.

## Step log

### Step 1. Setting and file read (done)

I read `library/gap-council-brief.md` (122 lines) and all 420 lines of
`library/gap-solve11-astra62.md` (commit `824d5cb01` in the lane clone). The file has 25 numbered
displays and about 60 labelled statements. The four positive claims named in the row are:
the equivalence of (W) with (22) (lines 283-344, built on (19)-(21)); the reconstruction (23)
(lines 346-360); the query bounds (24) and the matching order (lines 362-375); the count (25)
(lines 377-405). The wall form used throughout is line 9: one fixed side L with
limsup_j (Tr U^T - 1) < 1/1650, T = n/2.

### Step 2. Cited sources (done for the four positive claims)

Read in full the parts cited by the positive claims:
- Row 1161 (`gap-solve9-astra62.md`) L13-L84 (twist and overlap bounds, (3)-(5)) and L213-L227
  (the explicit K = 512 test). Its check (row 1162, `gap-solve9-check-opus.md`) gives S12 HOLDS
  for L215-L227. The second branch there says: all seven periodic charged top weights
  x = (lambda/lambda_0)^n are at least 1 - 2^{-46}. This is the form row 1165 uses at L294 and L342.
  The hypothesis is s(u) <= 1/2 at an integer 3 <= u <= n/512 with 4 | n, n >= 2^70.
  Row 1165 uses u = 2 floor(n/1024), which lies in that range for large n.
- Row 1155 (`gap-solve7-astra62.md`) L120-L134 ((9)) and L386-L477 ((27)-(32), open kernels).
  Its check (row 1156) gives (9), (27), (31), (32) and the open-kernel forms HOLDS.
- `gap-crux-restate.md` L172-L219: Lemmas K, X, E, E', Theorem S, Corollary S3'
  (checked by rows 698, 699). Lemma E': for h >= b > a >= 3,
  1 + S(a; h) <= (1 + S(a; b))^{h/(b-a)}.

- Row 1153 (`gap-solve6-astra62.md`) L49 (epsilon_beta = beta^{-1/4}[log(2+beta)]^{3/2}, so
  sqrt(epsilon_beta) = delta_B of row 1165), L152-L167 ((9), (10) and the secant bound
  p_V'(u) = 3/4 + O(|u| + sqrt(epsilon_beta)), |u| <= 1/4). Row 1154 gives (10) HOLDS.
- Row 1143 (`gap-solve-astra62.md`) L17-L19 (all rectangles with sides >= 3) and L84-L106
  ((4)-(6), absolute constants). Row 1144 gives all statements HOLDS.
- Row 1163 (`gap-solve10-astra62.md`) L185, L212, L276-L307 ((22)-(24)), L361-L422 ((27)-(33)
  and the connected-set disk). Row 1164 gives HOLDS.
- Row 865 (`gap-sdcyl-ca-astra.md`) L65-L169 (rectangular transfer, common counterterm,
  (SD-cyl-CA)). CA-I L2727-L2800 read in the lane's local copy of the account (same line
  numbers as the cited revision): the class T(d; theta), the depth s(d), the upper witness
  (8/3) b_0 C_K ||f|| ||h|| (g^{-2} + lambda s - c_5)^{-2}, and the volume transfer
  C_T(g) d^2 ||f|| ||h|| for tests in one ball of radius 5d.
- `gap-unit-check-opus.md` L62-L77: Lemma ORD HOLDS (contact of order 4t).
- Row 1147 (`gap-solve3-astra62.md`) L278: both drift bounds (RF25) at fixed reference coupling
  give beta_j ~ log n. Row 1148 gives HOLDS. (9), (25), the Z_2 factor and the two-state
  comparison use this two-sided growth.

### Step 3. The equivalence of (W) with (22) (done)

**S1. (19) and its proof (L283-L292). HOLDS.**
- Centre invariance gives K(hx, hy) = K(x, y). So the lift of P_H has density
  A^2 = g^{-1} sum_h K(x, hy)^2, and ||A||_HS = 1.
- Pi_H commutes with F and the vacuum is H-invariant. So ||Pi_H F^t||_op = lambda^t and
  X_H(u) = ||C||_HS^2 / ||C||_op^2 with C = Pi_H K.
- C is the mean and A the root mean square of g nonnegative numbers. So m A <= C <= A with m = g^{-1/2}.
- (C/A - m)(1 - C/A) >= 0 gives ||C||_HS^2 <= (1+m) b - m. Then ((1+m) b - 2m)^2 >= 0 gives
  b/||C||_HS >= 2 sqrt(m)/(1+m) = h_g.
- D = |sqrt(rho)><sqrt(rho)| has HS norm one. So ||C||_op >= <D, C> >= b - d_H ||C||_HS. This gives (19).
- GUIDE: 800 random invariant positive kernels, with (Z_2)^3 acting freely and |H| = 1, 2, 4, 8.
  The smallest value of (h_g - d_H)^{-2} - X_H(u) was +4.3e-5. No violation.

**S2. One fixed winding sign suffices (L294). HOLDS.**
- h_g = 2 sqrt(m)/(1+m) increases in m. For g <= 8, m >= 8^{-1/2} > 1/3, so
  h_g >= sqrt(3)/2 = 0.8660 > sqrt(2/3) + 1/32 = 0.8477. If limsup d_H < 1/32, then eventually
  X_H(u) < 3/2.
- For H = ker chi, Pi_H projects onto the characters 0 and chi. So X_H = X_0 + X_chi. This gives
  s(u) < 1/2, and the leading chi-weight satisfies r_chi^u < 1/2.
- u = 2 floor(n/1024) lies in [3, n/512] when n >= 2048, so row 1161's explicit test applies
  (S12 of row 1162, range 4 | n, n >= 2^70). In its second branch all seven x = r_q^n are
  >= 1 - 2^{-46}. Since r_q <= 1 and u <= n, r_chi^u >= 1 - 2^{-46}, a contradiction. The first branch
  gives Tr U^{n/2} - 1 < 2^{-19} < 1/1650 at every fine cutoff. That is (W) in the form of L9.
- Converse: d_H^2 <= D_KL <= I_u (the quotient map contracts, applied on each side), and
  I_u <= J(u/2) <= 2 log X_{u/2} by (3). The enlargement after (21) makes X_{u/2} - 1 small.
- With H = G the same bound gives s(u) <= 1/2, which is the input of row 1161's test.

**S3. A direct observable on one slice (L296). HOLDS.** Equal raw adjoints give a relative sign
cochain a. Equal spatial plaquette signs give da = 1. A flat Z_2 cochain on the 3-torus is a
vertex coboundary times one of the eight classes in H^1. The winding sign along gamma fixes the
chi-period, so the remaining flips form ker chi = H. Given the two gauge classes, the two vertex
gauge frames are independent Haar. So the Hellinger distance of the raw readings equals d_H.
d^2 <= D_KL holds (d^2 = 2(1 - BC) <= -2 log BC <= D_KL).

**S4. (20) and the reconstruction (L300-L309). HOLDS.**
- The comparison in each collar is drawn given the adjoints only. The involution of row 1155 (27)
  (checked by row 1156) acts on (O, O'_1, O'_2). It keeps the relative cochain, hence c. It
  exchanges the two plaquette weights on faces with dc = -1. It keeps the adjoint normalisers. So it
  preserves the joint law. The tube signs and the winding sign are read from O and are not
  conditions on the draw. This is the point stated at L307, and it is needed.
- Decoder geometry. With k = floor(r/10), 2k + 6 <= r/5 + 6, and r/5 + 6 < r/2 - 1 when r > 70/3.
  So r >= 100 suffices. A move to an adjacent face (common 3-cube) changes the face centre by at
  most one in max norm. So a component that leaves the tube meets its outer layer. A component
  that does not meet the outer layer is a whole collar component. A component whose filling meets
  gamma lies within distance 2k + 6 of gamma and does not meet the outer layer. So
  c_loc(gamma) = c(gamma) on the good event.
- The winding sign of the switched original is s c(gamma), because c is central. A flat flip in
  direction 1 changes that sign. Flips in directions 2 and 3 do not, since gamma has no such links.
  So the output equals the switched original modulo H and vertex gauge on the good event. The
  switched original has the true two-slice law. This gives (20).
- The probability bounds of (27) on the n^3 x u cylinder use row 1155 (9) on that torus. L316
  states this adaptation; see S5.

**S5. (21) and the sparse recording (L311-L316). HOLDS.**
- Sufficiency: d_H <= E_Y + sqrt(2 eta) + 2 sqrt(eta). The middle term uses contraction of
  Hellinger distance under the product channel D_1 x D_2. The outer terms use
  d^2 <= integral |p - q| = 2 TV, and TV <= 2 eta for the product of the two marginals.
- Sparse list: P(w_p < 0) <= e^{-c beta} E e^{c beta (1 - w_p)} <= C e^{-c beta}. The marked-face
  bound (9) of row 1155 uses Schatten Hoelder with exponent the circle length. Its steps do not use
  a particular even length. I accept the adaptation to the short aspect from that reading; I did not
  rewrite it. The overflow probability is <= C_r n^{eta_0} e^{-c beta} -> 0, because eta_0 is
  strictly below c liminf beta_j / log n.

**S6. Necessity even for complete collars (L318-L323). HOLDS.**
- The vacuum factors telescope round the cycle. So the density of the two complete segments,
  relative to two independent stationary segments, is p_d(e_1, s_2) p_d(e_2, s_1)/X_u, with
  d = u/2 - h.
- Each connecting pair is a pair of independent pi-points. So each factor has mean 1 and second
  moment X_{2d}. The two factors are dependent, and the Cauchy-Schwarz split used at L321 does not
  need independence: E|f_1 f_2 - 1| <= sqrt(X_{2d} S(2d)) + sqrt(S(2d)).
- Lemma E' with a = n/(2D), b = n/D, h = n has exponent h/(b - a) = 2D per side, so (2D)^3 for three
  sides. The time n/(2D) <= n/8192 is below u/2 = floor(n/1024) and below 2d = u - 4r for large n.
  S decreases in time. Product continuity costs 3 eps in TV, and d^2 <= 2 TV.

**S7. (22) (L327-L340). HOLDS.**
- Sufficiency: row 1155 (27) reconstructs the G-quotient from the adjoint collars. So eventually
  d_G < 1/32, and X_0(u) = X_G(u) <= (h_8 - 1/32)^{-2} = 1.393 < 3/2. Row 1161's test then gives
  one of its two branches at each fine cutoff. S8 shows that the second branch gives
  C_gamma >= 2/3 - o(1). So limsup C_gamma < 3/5 leaves only the first branch, hence (W).
- Necessity: under (W) the complete-segment law is close in TV to two independent stationary
  segments. The global flat flip in direction 1 preserves the stationary segment law, all adjoints
  and all plaquette signs, and changes s_i. So E_Q[s_i f(A_i, D_i^0)] = 0 and C_gamma -> 0. The
  bound is uniform over |f| <= 1.

**S8. The quantitative witness in the competing branch (L342-L344). HOLDS.** I checked each
constant.
- X_q(u) <= X_0(u) <= 3/2 by positivity of the twisted integrals. Two leading levels of size
  >= 1 - delta would give a sector trace >= 2 - 2 delta > 3/2. So each leading line is simple.
- The neutral second eigenvalue has rho^u <= s(u) <= 1/2. So 1 - (pi|h_q|)^2 <= delta/(1/2) = 2 delta,
  ||h_q - sigma_q||^2 = 2(1 - pi|h_q|) <= 4 delta, and E_u(sigma_q) <= 2 delta + 8 delta = 10 delta.
- E_u(sigma sigma_q) <= 20 delta by the union bound (E_u of a sign is twice the flip probability).
  Each nonleading eigenvalue of P^u in character q + chi is <= 3/2 - (1 - delta) = 1/2 + delta. So the
  off-line part of sigma sigma_q has squared norm <= 20 delta/(1/2 - delta) < 41 delta. Then
  sigma h_q = sigma sigma_q + sigma(h_q - sigma_q) gives the bound (2 + sqrt 41) sqrt(delta) = 8.40 sqrt(delta).
- The trace Tr(P^t M P^t M) = sum_{ij} lambda_i^t lambda_j^t |<i, M j>|^2 has nonnegative terms.
  Its eight leading pairs (q, q + chi) give >= 8 (1 - delta)(1 - 81 delta), since
  r^t >= (1 - delta)^{1/2} for t <= n/2. With X(u) <= 8 (3/2) = 12, the correlation is
  >= (2/3)(1 - delta)(1 - 81 delta). With delta = 2^{-46} this exceeds 3/5 by 0.0667.
- The pulled-back reading is E[sigma(out) | Y_i]. The comparison draw uses A_i only, and the
  output H-orbit is chosen by the sign s_i c_loc. So the reading has the form s_i f(A_i, D_i^0)
  with |f| <= 1. The channel is covariant under the half-period translation, so the same f serves
  both collars, as (22) requires. The cost of (20) is at most 2 eta.

Step 3 verdict: S1-S8 HOLD. The equivalence of (W) with (22) holds on these inputs: row 1161's
explicit test, row 1155 (27), Lemma E' and the propagation of row 720.

### Step 4. The reconstruction (23) (done)

**S9. (23) as stated (L348-L354). HOLDS.** The tree has M - 1 edges, each sweeping n spatial faces
at the central time, so the reading uses n(M - 1) signs. A comb tree fits in a square of side
ceil(sqrt M). Both choices of r and M are right: at fixed L, n^4 e^{-c beta M} -> 0 because
liminf beta_j/log n > 0. At fixed large beta, r, M = A(1 + log n/beta) give
C n^4 e^{-c beta A} n^{-cA} -> 0 when A > 4/c.

**S10. The finite minimisation (L356). HOLDS.** dc is -1 exactly on the selected components, so
B_0 = dc is a subset of B and equals B on every central spatial face. c has a buffer inside the
collar, so B_0 is closed on every cube of the extended complex. B_0 agrees with B on the tree
faces, so it is feasible. The decoder can compute B on the tree faces from the observed original
signs and the comparison. The minimum is over a finite set, and the bound below holds for every
minimiser.

**S11. The proof of the bit bound (L358-L360). HOLDS.**
- Stokes: <dc, R_root> = c(gamma) + c(gamma at the far end) = c(gamma), since c vanishes outside the
  collar.
- Both B_* and B_0 are closed. So every cube has an even number of faces in the symmetric
  difference. These faces share the cube, so they lie in one component. So each component D is
  closed. Toggling D keeps all three constraints. Minimality gives |D cap B_0| >= |D|/2.
- For tree neighbours v, w the slab (edge) x (circle) x [central time, far time] has boundary
  R_v + R_w + (far strip) + (tree strip). D vanishes on both strips. With dD = 0 this gives
  <D, R_v> = <D, R_w>. A wrong bit needs some D with <D, R_root> = 1. Then D meets all M disjoint
  ribbons, so |D| >= M.
- At least |D|/2 faces of D are true relative bad faces. The prescribed-face bound of row 1155
  (27) and the sum over subsets give 2^k (C e^{-c beta})^{k/2}. There are at most C n^4 C_0^k rooted
  connected supports. Summing over k >= M gives C n^4 e^{-c beta M} for large beta. The switch is
  the one of (20) and uses only common adjoints. So the pulled-back reading has the form
  s_i f(A_i, tree signs), as used in (22).

Step 4 verdict: S9-S11 HOLD.

### Step 5. The query bounds in the competing magnetic branch (done)

**S12. (24) as stated (L364-L369). HOLDS, with one reading made explicit.** Each observer queries
faces of its own collar, and the components A_{i,l} are built from those faces. L373 uses this when
it says that no boundary face reads both collars. If an observer could query faces anywhere, one
collar's flips could change the other collar's answers, and the product structure would need a new
argument. The statement's wording ("In each of two disjoint collars ... give an observer") supports
this reading. One intervening time step would already separate the two sets of boundary faces, so
two steps are enough.

**S13. The proof of (24) (L371-L373). HOLDS.**
- A (1, mu) face at x_1 = l contains two 1-links, both based at x_1 = l. A 1-link based at x_1 = l
  lies in no other faces. Each 1-link lies in exactly six faces. So |boundary A_{i,l}| <= 6|A_{i,l}|.
- A component of a links needs at least a - 1 queried edges. Faces in different planes are
  different. So sum_l (|A_{i,l}| - 1) <= D, which gives sum_l |A_{i,l}| <= n + D.
- The flip changes no queried face and no adjoint. By induction on the query steps, the transcript,
  and hence A_{i,l}, is unchanged. So each flip is an involution, the flips commute, and on each
  event {A = a} the flip is a fixed central translation of Haar measure. The winding loop has
  exactly one link in A_{i,l}, so s_i changes sign.
- On an orbit the weight is prod exp(eps_{i,l} J_{i,l}) with |J| <= beta |boundary A| <= 6 beta |A|.
  So the conditional mean of s_1 s_2 f_1 f_2 has modulus <= prod tanh(6 beta |A_{i,l}|).
- log tanh x = -2 artanh(e^{-2x}) <= -2 e^{-2x} (GUIDE grid check: no violation). Jensen on each
  collar gives sum_l e^{-12 beta |A_{i,l}|} >= n e^{-12 beta (1 + D/n)}. Two collars give the exponent
  -4n e^{-12 beta (1 + D/n)}. The bound holds on every orbit, so it holds after averaging.
- At fixed beta and 1 + D/n <= (1 - eps) log n/(12 beta), 4n e^{...} >= 4 n^{eps} -> infinity.

**S14. Queries that depend on the winding sign (L369). HOLDS** for odd readings, as stated. The
combined run of both sign branches is a rule independent of s_i with at most 2D queries. Its
transcript has the invariance used in S13.

**S15. Matching order at fixed coupling (L375). HOLDS, conditional on the magnetic seed, as stated.**
- Upper: D = n(M - 1) with M = ceil(C_1(1 + log b/beta)), which is O(b log b/beta) at fixed beta. The
  error of (23) at period b is <= C b^4 b^{-c C_1} -> 0 for large C_1. By (1) and the argument of (5),
  the antipodal pair is within O(sqrt v) in TV of two pi-slices with equal labels. The chi-sign
  (-1)^{chi . l} is a function of the ker(chi)-quotient, and its correlation under that law is 1.
  So the pulled-back dressing has correlation 1 - o(1).
- Lower: if D = o(b log b/beta), then 4b e^{-12 beta (1 + D/b)} = 4 e^{-12 beta} b^{1 - o(1)} -> infinity.
  So every reading covered by (24) has correlation -> 0.
- The constants differ: the lower bound holds for any c < 1/12, and the upper bound needs a large
  C_1. This matches "up to constants". The counts are of queried face positions, as L375 says.

Step 5 verdict: S12-S15 HOLD (S12 with the explicit locality reading).

### Step 6. The singularity count (25) (done)

**S16. (25) as stated (L379-L392). HOLDS AFTER CORRECTION.** The correction is in the proof at L394
(S17). It changes absolute constants only. The other assertions of L392 hold:
- If z lies in D_n, then |Im z| < w(x) <= W_0. Also 1 + x < (1 + Re z)/(1 - gamma_n), so
  |Im z| < 2 gamma_n (1 + Re z) once gamma_n < 1/2.
- The strong-coupling disk |z| < r_* is uniform and gamma_n -> 0. So Re z > r_*/2 eventually.
- If the seed fails, then J = 2 log X_T - log X_{2T} >= log X_T = log(1 + S), because
  X_{2T} <= X_T. So J >= log(1 + 1/1650) - o(1) on a subsequence.

**S17. The bound |PH| <= CN on the disks |z - x| <= w(x)/2 (L394). HOLDS AFTER CORRECTION.**
- Jensen gives O(N w) zeros of either transform in the w-disk, since |Z(x+q)/Z(x)| <= e^{12N|q|}.
- The Blaschke circle has a radius rho in [3w/4, w). Its "half disk" |z - x| <= rho/2 has radius
  between 3w/8 and w/2. It need not contain the disk |z - x| <= w/2 on which the bound is claimed
  and later used (the outer circle w/2 in L396).
- Correction: make the estimate on |z - x| <= 2 rho/3, which contains the w/2-disk. A nonnegative
  harmonic function u on the rho-disk has |grad u| <= 18 u(0)/rho there (Harnack and the Poisson
  gradient bound). Each reflected term zeta-bar/(rho^2 - zeta-bar q) is at most 3/rho there. So the
  bound |PH| <= CN holds on |z - x| <= w/2 with a larger absolute C. Nothing else changes.
- The other steps hold. P removes every pole of H in the disk, because the circle lies in D_n.
  Each pole term times P has modulus <= |nu|/D_0, because |z - zeta'| <= 2(B + W_0) < D_0. The total
  absolute residue is O(N w).

**S18. The transport along the real segment (L396). HOLDS.**
- H vanishes to order >= 4T - 1 at 0 (Lemma ORD). Schwarz from radius w(0)/2 to w(0)/8 gives the
  factor 4^{-(4T-1)}.
- The step is w(x)/16 and the slope of w is <= gamma_n <= 1 eventually. So
  w(x_next) <= (17/16) w(x), hence w(x)/16 + w(x_next)/8 <= w(x)/4, and the next inner disk lies
  in the current w/4-disk.
- log(w/4) is the midpoint of log(w/8) and log(w/2). So the three-circle inequality, with the bound
  CN on the outer circle, halves the gained exponent at worst.
- Each step adds at least (w/16)/(17w/16) = 1/17 >= 1/18 to the integral of dx/w. That integral is
  <= B/W_0 + log(1 + B)/gamma_n <= log n (K_B/W_0 + 1/A_0), where K_B bounds B/log n. So suitable
  W_0, A_0 give 2^{k+1} <= n^{eps/3}, and the final exponent is
  >= (2n - 1) log 4 * 2^{-k} >= c n^{1 - eps/3}.

**S19. The conclusion (L398). HOLDS.**
- At |q| < 1/(40N), |E e^{-qA} - 1| <= e^{12/40} - 1 = 0.35 < 1. So every real x is at distance
  >= 1/(40N) from all zeros, and |P(x)| >= (40 N D_0)^{-m}.
- J(B) = integral_0^B H dx <= B max|PH| / min|P|. The term m log(40 N D_0) = O(n^{1-eps} log n) is
  negligible against n^{1 - eps/3}.

**S20. The two-state comparison (L400-L405). HOLDS.**
- The 2 x 2 transfer has eigenvalues (1 +- e^{-az})/2. So X_T = 1 + q^k with q = tanh(az/2) and
  k = 4T, and R_a = (1 + q^k)^2/(1 + q^{2k}). Also 1 - q(B) = 2/(1 + e^{aB}), so
  q(B)^k ~ exp(-2k e^{-aB}) = exp(-4n e^{-aB}). This tends to 0 or to 1 on the two sides of
  a B/log n = 1, as the strict choices of a_- and a_+ require.
- The zero sets q^k = -1 (odd multiples of pi/k) and q^{2k} = -1 (odd multiples of pi/(2k)) are
  disjoint. At a zero the denominator is 2, and at a pole the numerator is 1 + q^k with q^k = +-i.
  So all these points are uncanceled.
- tanh(az/2) = e^{i theta} gives z = a^{-1}(log cot(theta/2) + i pi/2).
- X = pi/(a gamma_n) = O(log n/log log n) = o(log n), so [X, X+1] lies in [0, B] eventually. The
  number of points is about c_a k e^{-aX} = c_a k e^{-pi/gamma_n} = n^{1 - o(1)}.
- GUIDE: a direct 2 x 2 computation matches R_a to 2e-16. The stated point gives |1 + q^k| = 1e-15.
  At B = log n and A_0 = 5 the count exponent log(count)/log n rises from 0.59 (n = 10^4) to 0.85
  (n = 10^32). This is the slow approach that n^{1 - o(1)} predicts.

Step 6 verdict: S18-S20 HOLD. S16 and S17 HOLD AFTER CORRECTION (radius bookkeeping at L394;
constants only, (25) unchanged).

### Step 7. Everything else (done)

**Setting (L1-L15).**
- **S21. L5 (GUIDE, repo search).** Not re-run. The cited files exist. FINISH rows 1164 and 1165 are as
  stated. GUIDE.
- **S22. L7 (GUIDE, the account).** Spot-checked in the lane's local copy of the account (the line
  numbers agree; I did not verify the copy against revision `31a47c543775`). Outline L2313-L2336 is
  the transfer contraction, with Z_s(0) = Tr L^s. Outline L31871-L31882 says that polynomial
  clustering does not give a gap. CA-I L2704-L2712 lists "a mass gap" under "Not asserted". HOLDS
  as a reading.
- **S23. L9 (OPEN, the seed form of (W)).** HOLDS. Precision: "Row 1163 is unchecked at the pin" is
  now out of date. Row 1164 checked row 1163 (HOLDS).
- **S24. L13 (GUIDE).** HOLDS. It agrees with row 1161 L17-L38.
- **S25. L15 (setting of v).** HOLDS. Corollary S3' with b_0 = 2N gives S(D/2; b^3) <= q^{2^k}/71
  for 2^k b_0 <= b < 2^{k+1} b_0. Also t = b/2 >= D/2. Row 1161 L178 (checked) makes the same use of
  Theorem S-w for S_full.

**What a slice remembers (L17-L38).**
- **S26. (1), periodic case (L17).** HOLDS: ||p_t - 1||^2 = S(2t) <= S(t) <= v.
- **S27. (2) (L25-L30).** HOLDS. A temporal twist g != 0 becomes, after a rotation, a twist with a
  nonzero static part m. If all three g_i = 1, a temporal part remains. The bound covers this case
  too: |Tr(R_e F_m^b)| <= sum_q X_{m,q}(b) <= 8 X_{m,0}(b) <= 8 X_{m,0}(t) <= 8v, by row 1161 (3).
  Fourier inversion gives |X_q(b) - X_0(b)| <= (1/8) 7 (2)(8v) = 14v. Then
  r_q^t >= X_q(b)/X_q(t) >= (1 - 14v)/(1 + v), and sum_{i>=2} r_{q,i}^{2t} <= 45v.
- **S28. The labels (L32-L36).** HOLDS. E_t(|h|) <= E_t(h) by the two-slice formula. Neutrality of |h|
  gives 1 - (pi|h|)^2 <= (1 - r^t)/(1 - rho^t). Also ||sigma - h||^2 = 2(1 - pi|h|), and
  E_t(sigma) <= 2 E_t(h) + 2||sigma - h||^2 since 0 <= I - P^t <= I. Equivariance holds, l is
  uniform, and a sign changes with probability E_t(sigma)/2.
- **S29. Proof of (1) (L38).** HOLDS. Sum over the eight orthogonal sectors of
  ||P^t|_chi - |sigma_chi><sigma_chi| ||_HS^2 = O(v). The comparison kernel is
  sum_chi sigma_chi(x) sigma_chi(y) = 8 1{l(x) = l(y)}.

**Shannon test (L42-L76).**
- **S30. (3) (L42-L47).** HOLDS. GUIDE: 300 random positive kernels, smallest slack -4e-15
  (rounding).
- **S31. Proof of (3) (L49-L58).** HOLDS. <sqrt l, F^t sqrt l> <= lambda^t gives the affinity bound
  X_{2t}^{-1/2}. Jensen gives I >= log X_{2t}. Positive semidefiniteness of F^t gives
  L <= e^J m x m, and D(L || m x m) = I + 2 D(l || m).
- **S32. (4) (L60-L64).** HOLDS. X_m <= e^{I_m} < 3/2. For T/m >= 11 (m <= n/22),
  sum r^T <= (sum r^m)^{T/m} <= 2^{-11} < 1/1650. Converse: Lemma E' with exponent 2d per side, and
  m/2 = floor(n/44) >= n/(2d) for d >= 64 and large n.
- **S33. (5) (L66-L74).** HOLDS. Periodic: I_b <= 2 log(1 + v). Magnetic: X_b, X_t = 8 + O(v), so
  I_b = log 8 + O(v). TV: ||p_t^2 - k^2||_1 <= ||p_t - k||_2 ||p_t + k||_2, and the integral of k^2
  is 8, so k^2/8 = k. TV(k pi x pi, pi x pi) = (8 - 1)/8 = 7/8.
- **S34. Selection test (L76).** HOLDS, given the neutral input of row 1161. At each fine coupling one
  branch holds and propagates, with v -> 0 as b grows.

**Zero-free disks (L80-L111).**
- **S35. (6) (L80-L89).** HOLDS, on row 1153 (10) (checked). sqrt(epsilon_beta) = delta_B. Hoelder
  with exponent six needs the one-orientation bound at 6u, inside |6u| <= 1/4.
- **S36. Proof of (6) (L91-L96).** HOLDS. At |u| = 1/W_V the bound C V/W_V^2 + C V delta_B/W_V is
  O(1). With |s| <= c/W_V and c <= 1/2, |sY| e^{|sY|} <= c r e^{r/2} <= 2c e^r with r = |Y|/W_V.
  Z(B + Bs)/Z(B) = e^{-9Vs/2} E e^{-sY}.
- **S37. (7) (L98-L105).** HOLDS.
- **S38. Proof of (7) (L107-L111).** HOLDS. The selection keeps M >= V/7 parallel links. Six staples
  give the face weight 6 - k.v. If more than M/2 links have |k| < 3, then A >= 3M/2. Markov with
  log Z(B/2) - log Z(B) <= CV (row 1143 (4)) gives e^{-cBV}. The S^3 marginal density
  e^{-u} sqrt(u(2 - u/s)) is right. A uniform component on [1, 2] gives the variance and the
  characteristic-function bound. For the copies: E D^2 >= cM, E D^4 <= CM^2, and Hoelder gives
  E|D| >= c sqrt M. The two closing sentences are remarks about a first-moment criterion. They hold
  as such.

**The paired product and the matching error (L115-L148).**
- **S39. (8) (L115-L120).** HOLDS. The sign (-1)^{sum_{nu<mu} x_nu} on mu-links gives the product
  s_mu(x) s_nu(x + mu) s_mu(x + nu) s_nu(x) = -1 on every (mu, nu) face. It is periodic for even
  sides.
- **S40. Proof of (8) (L122).** HOLDS. Jensen gives <= C V R zeros in the R-disk. Dyadic sums give
  sum_{|zeta|>R} |zeta|^{-2} <= C V/R. The odd remainder is <= CV on the half disk (here the half disk
  of the circle is what is needed) and vanishes at 0. Schwarz gives CV|z|/r, which tends to 0 as
  r grows.
- **S41. Vanishing moments (L124).** HOLDS. Near 0 the double series for log R converges absolutely.
  Contact 4T (Lemma ORD) kills the coefficients of z^{2h} for 2h < 4T. The vortex contact b^2 of row
  1163 (32) is even when 4 | b.
- **S42. (9) (L126-L130).** HOLDS. H ~ N B^{-9/8} [log(2 + B)]^{3/4}, since N delta_B dominates sqrt N.
- **S43. Analytic error (L132-L141).** HOLDS. The tail is sum over |zeta| > r of (B/|zeta|)^{2m+2}/(1 - (B/r)^2)
  <= C N B (B/r)^{2m+1}. B/r <= Q^{-alpha}/2, Q^{2m+1} >= H/Q, N^{1-alpha} = n^{-p}, and
  m/log(1 + B) -> infinity.
- **S44. Lipschitz bound (L143).** HOLDS. |log|a| - log|b|| <= |a - b|/min(|a|, |b|). (6) gives
  1/|zeta -+ B| <= C H. The polynomial part is <= C Q^{2m} |zeta - xi| <= C H |zeta - xi|. The
  restatement of row 1163 (23) with these weights holds, because the weighted sum is J(B) + o(n^{-p}).
- **S45. (10) (L145-L148).** HOLDS, conditional on the cylinder witness, as stated.

**Sampling dynamics (L152-L173).**
- **S46. L152.** GUIDE.
- **S47. (11) (L154-L158).** HOLDS.
- **S48. Proof of (11) (L160-L167).** HOLDS. The AM-GM pairing gives corr(h) >= corr(b/2) for every h.
  Domination nu_k <= 2 mu holds because each kernel preserves mu. A shared slice forces equal common
  labels.
- **S49. Converse (L169).** HOLDS. Precision: |f - 1| <= 1 alone gives 2 d_b. The bound d_b also uses
  the vanishing X-marginal of L_b - l_b x l_b, which rewrites the signed mass as half the integral
  of a [-1, 1]-valued function. GUIDE: a linear-programme check on 300 random laws found the supremum
  below d_b in every case. Either constant suffices for (5) and for the criterion.
- **S50. Criterion (L171).** HOLDS, given the neutral input of row 1161. v <= C_beta e^{-c_beta b}, so
  (k_b + 1) b v -> 0 when log k_b = o(b).
- **S51. L173 (OPEN).** HOLDS. A global centre flip moves every slice, so it breaks the shared-slice
  condition.

**Fixed-torus divisor (L177-L207).**
- **S52. (12) (L177-L182).** HOLDS on row 1143 (4), (6) (checked). For the thermal ratio
  2 (9/2) V_T = (9/2) V_{2T}, and B(beta) remains. For the twist ratio (6) gives the same form.
- **S53. L184-L189.** HOLDS. The integral of the count against 2r^2/[s(s^2 + r^2)] is <= pi C r.
- **S54. L191.** HOLDS. e^{-6Vz} Z~ is bounded by 1 on Re z >= 0 and positive at real h. The zeros
  of G are zeros of the numerator integral, with at most twice its multiplicity.
- **S55. L193.** HOLDS. On the sector, (e^{-i theta_0} z)^{3/2} has argument at most 3 pi/8.
- **S56. L195.** HOLDS. log(1 + x^2) <= 2x. The harmonic measure argument gives a polynomial bound.
  A rational R contradicts log R(x)/log x -> 3/2.
- **S57. (13) (L197-L203).** HOLDS.
- **S58. Proof of (13) (L205-L207).** HOLDS. E_u A <= [log Z(u/2) - log Z(u)]/(u/2) = O_box(1/u). The
  angular bound gives |zeta +- x| >= c'(|zeta| + x). For s > 2x the series difference is
  <= 2(d/s) sum_h (x/s)^{2h}. On [x, 2x] the factor is 4. |3/2 - 2k| >= 1/2 for integer k.

**Ultraviolet route (L211-L279), conditional on the suppliers of row 865, as stated.**
- **S59. (14) (L211-L216).** HOLDS (conditional). The lower bound follows from (7) by
  Var >= (E|X - EX|)^2.
- **S60. (15) (L218-L223).** HOLDS. The layer-cake formula and Jensen extend the indicator bound to
  0 <= w <= 1. At u = +-1/(48 sqrt M) and M delta_B^2 <= 1 the bound is O(1).
- **S61. Depth admission (L225).** HOLDS (conditional). a q_K >= C_W(K - k_W) L^{-(K - k_W)} gives
  s(d) <= K - k_W. C_W >= 1 gives s(d) >= log_L(1/d). The CA-I upper witness (local copy L2782-L2789)
  is (8/3) b_0 C_K ||f|| ||h|| (g^{-2} + lambda s - c_5)^{-2}. So unit-height tests give C/[1 + log(1/d)]^2.
- **S62. Hats (L227).** HOLDS. The 1-D hat refines with weights 1/2, 1, 1/2. Child weights from all
  parents sum to one.
- **S63. Multiscale sum (L229-L234).** HOLDS (conditional). I checked the class T(d; theta) of CA-I
  (local copy L2758-L2763) at d = 4h:
  - each support lies in a ball of radius 2h <= d;
  - the integral is h^4 = d^4/256 >= d^4/300;
  - Lip <= 2/h <= 75/h = 1/(theta d);
  - the support distance lies in [4h, 24h] = [d, 6d];
  - both supports lie in one ball of radius 14h <= 5d.
  The pair coefficients stay in [0, 1]. The dyadic sum is <= C h_f^{-4}/[1 + log(1/h_f)]^2 <= C V/B^2,
  because q_K >= 1, B ~ K and log(1/h_f) ~ K.
- **S64. Last mesh (L236).** HOLDS. M = O(q_K^4) and delta_B^2 = O(B^{-1/4} polylog), so
  M delta_B^2 -> 0.
- **S65. (16) (L238-L244).** HOLDS (conditional). Schwarz on (h - 1)/(Q_* + 1) gives a zero-free disk.
  Carathéodory gives |c_k| <= 2 C_L V (r_L/2)^{-k}. V |z|^3 <= C B^3/sqrt V -> 0. Hoelder over the fixed
  number of hats then gives the first-order argument of (6) with W = sqrt V.
- **S66. L246.** HOLDS (conditional). N H^{-alpha} = N^{1 - alpha/2} B^alpha = n^{-p} B^alpha.
- **S67. (17) (L250-L254).** HOLDS (conditional).
- **S68. J' and near covariances (L256).** HOLDS (conditional). J'(B) = -2 N_T [E_T O(F) - E_{2T} O(F)],
  since the doubled rectangle has 2 N_T hats. The common E_F cancels, and Cauchy bounds h'(0). Near
  pairs fit in one ball of radius 7 h_0 <= 5d. The CA-I volume transfer (local copy L2791-L2798)
  has no sign or distance condition. The reference terms cancel because the offset sets agree and
  the number of centres doubles.
- **S69. Far covariances (L258-L262).** HOLDS (conditional). The cross term is
  |Tr(F^a D_z F^c D)| <= ||F^{a/2} D F^{c/2}||_HS^2, by Cauchy-Schwarz and tau_z-invariance. The pairs
  (ij, ji) give 2 (lambda_i lambda_j)^{N/2 - w} cosh((N/2 - k) log(lambda_i/lambda_j)), which decreases
  for k <= N/2. At k a = 6 h_0 the aligned pair is in T(4 h_0; 1/300).
- **S70. (18) (L264-L273).** HOLDS. J' = sum nu [1/(z - zeta) + 1/(z + zeta)] and
  J'' = -sum nu [1/(z - zeta)^2 + 1/(z + zeta)^2], from (8).
- **S71. Z_2 factor (L275-L279).** HOLDS. The flat mass is 2^{V+3}/2^{4V}. The fibres of the coboundary
  map have equal mass. The tail bound is (1 + e^{-J_0 Re z})^{6V} - 1 <= 7 n^{-p-1} on Re z >= B/2.
  2(3 - 3V_T) - (3 - 3V_{2T}) = 3, giving log 8. Cauchy on the B/2-disk gives the derivative bound.

**Closing sections (L409-L420).**
- **S72. Full centre quotient (L409).** HOLDS. 2d >= t follows from h <= b/4. Then
  ||P^d|_q - |h_q><h_q| ||_HS^2 <= (1 - r_q^t)^2 + sum_{i>=2} r_{q,i}^t = O(v). E_h <= E_t for h <= t,
  since 1 - lambda^h <= 1 - lambda^t. The label factors give 64 1{l(s_1) = l(s_2)}/X_b ~ 8 1{...}.
  The label is uniform given each centre-quotiented segment, so the quotiented comparison is a product.
- **S73. Finitely many dressings (L411-L416).** HOLDS. sigma is uniform given Z. The kernel
  prod_i (1 + alpha sigma_i(x) sigma_i(y)) is Markov, centre-invariant and positive semidefinite, with
  eigenvalues alpha^{|I|}. Given the spin cycles the blind data are i.i.d. A listed correlation is
  <= eps^2. The antipodal sigma_1 correlation is 2 alpha^{u/2}/(1 + alpha^u). The second kernel acts
  on v only, so all charged correlations vanish.
- **S74. L418 (OPEN).** HOLDS as a summary. It claims no estimate beyond those checked.
- **S75. L420 (RESULT).** HOLDS as a summary, with the correction of S16-S17 (constants only). "Order
  n log n/beta queries ... sufficient and necessary up to constants" is conditional on the magnetic
  seed for sufficiency, as L375 states.

Step 7 verdict: S21-S75 HOLD (S21, S46 as GUIDE). No FAILS.

### Step 8. Verdict table

| # | Statement (lines) | Verdict |
|---|---|---|
| S1 | (19) and proof (L283-L292) | HOLDS |
| S2 | One winding sign suffices (L294) | HOLDS |
| S3 | Direct observable on one slice (L296) | HOLDS |
| S4 | (20) and reconstruction (L300-L309) | HOLDS |
| S5 | (21) and sparse recording (L311-L316) | HOLDS |
| S6 | Necessity for complete collars (L318-L323) | HOLDS |
| S7 | (22): equivalence with (W) (L327-L340) | HOLDS |
| S8 | Witness in the competing branch (L342-L344) | HOLDS |
| S9-S11 | (23), the minimisation and its proof (L348-L360) | HOLD |
| S12 | (24) (L364-L369) | HOLDS (queries read in the observer's own collar) |
| S13-S14 | Proof of (24), sign-dependent queries (L369-L373) | HOLD |
| S15 | Matching order, conditional on the magnetic seed (L375) | HOLDS |
| S16 | (25) as stated (L379-L392) | HOLDS AFTER CORRECTION (proof constant at L394) |
| S17 | Bound on PH on the w/2-disks (L394) | HOLDS AFTER CORRECTION (use radius 2 rho/3, not rho/2) |
| S18-S19 | Transport and conclusion (L396-L398) | HOLD |
| S20 | Two-state comparison (L400-L405) | HOLDS |
| S21 | Repo search (L5) | GUIDE |
| S22-S25 | Account reading, seed form, setting of v (L7-L15) | HOLD (S23: row 1163 is now checked) |
| S26-S29 | (1), (2), labels (L17-L38) | HOLD |
| S30-S34 | (3), (4), (5), selection test (L42-L76) | HOLD |
| S35-S38 | (6), (7) and proofs (L80-L111) | HOLD |
| S39-S45 | (8), moments, (9), (10) (L115-L148) | HOLD ((10) conditional on the witness) |
| S46 | Change-of-law note (L152) | GUIDE |
| S47-S51 | (11), converse, criterion, OPEN (L154-L173) | HOLD (S49: the factor d_b uses the zero marginal) |
| S52-S58 | (12), both signs survive, (13) (L177-L207) | HOLD |
| S59-S69 | (14)-(17) and proofs (L211-L262) | HOLD (conditional on the suppliers of row 865) |
| S70-S71 | (18), Z_2 factor (L264-L279) | HOLD |
| S72-S73 | Centre quotient, finite dressing lists (L409-L416) | HOLD |
| S74-S75 | OPEN and RESULT (L418-L420) | HOLD as summaries |

Counts: 75 statements. 71 HOLD, 2 GUIDE (S21, S46), 2 HOLD AFTER CORRECTION (S16, S17, one
correction at L394, constants only). None FAILS.

Precisions that change no verdict:
- S12: (24) needs each observer to query faces of its own collar.
- S5 and S4: the marked-face bound (9) of row 1155 on the short n^3 x u torus is accepted from L316
  and a reading of its proof.
- S49: "within d_b" uses the zero X-marginal of L_b - l_b x l_b. Without it the bound is 2 d_b. Both
  constants suffice.
- S23: L9 calls row 1163 unchecked at the pin. Row 1164 has since checked it (HOLDS).
- S22: the account lines were read in the lane's local copy. Their text matches the citations. I did
  not verify the copy's revision hash.

Guide runs (pure Python and numpy, about 40 MB, scratch scripts outside the repository, not kept):
(3) on 300 random positive kernels; (19) on 800 invariant kernels; the converse-update bound on 300
random laws; the inequality log tanh x <= -2 e^{-2x}; the witness constants; the two-state formula,
its zero location and its counts. All agree. They prove nothing.

Who checked what: every statement above was checked line by line by hand by Claude Opus 5.5 (max
effort) in this row. The inputs that were checked in earlier rows are named in Step 2: row 1161
(S12 of row 1162), row 1155 (row 1156), row 1153 (row 1154), row 1147 (row 1148), row 1143
(row 1144), row 1163 (row 1164), Lemma E' (rows 698 and 699) and Lemma ORD (row 991). This check is
not an audit.

RESULT: HOLDS AFTER CORRECTION (constants only) - check of row 1165 (`library/gap-solve11-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1166, positive claims first: 75 statements, 71 HOLD, 2 GUIDE, 2 HOLD AFTER CORRECTION, none FAILS; the equivalence of (W) with (22) holds (via (19), (20), (21), row 1161's checked K = 512 test and the witness constant (2/3)(1 - delta)(1 - 81 delta) > 3/5); the reconstruction (23) holds; the query bound (24) holds when each observer queries its own collar, and the matching order n log n/beta holds up to constants at fixed coupling, conditional on the magnetic seed; the count (25) holds after one correction at L394 (the Poisson estimate must be made on the disk of radius 2 rho/3, which contains the w/2-disk, not on the rho/2 half disk; constants only); (14)-(17) hold conditional on the suppliers of row 865; guide runs agree and prove nothing; the physical correlation bounds in (22), the signed Wilson value, (W) and the four-dimensional SU(2) mass gap remain OPEN.
