# Check of library/gap-solve2-astra62.md (FINISH row 1146)

Status: done (Steps 1-8). Verdict table and RESULT line at the end.

Checker: Claude Opus 5.5 (max effort), checker role, a laptop subagent.
The file under check is row 1145, by gpt-6.2-astra. Each step is checked
by hand. A numeric run, if any, is a guide only.

Note on the save protocol: the first tool call created this file with a
one-line log only. The plan below was added in the second write. No check
content was lost.

## Plan (at most eight steps)

1. Read the row text and the context files: the council brief, row 863
   Sections 3, 3.4 and 8.2, its check, and row 720 (gap-phys-seed.md lines
   300-340).
2. Read the file under check in full, in ranges.
3. Check Section 7: reference law, bridges, factors, the Kotecky-Preiss
   step, the seam comparison, (22).
4. Check Section 11: (25), the electric bound with r_beta^(d-1), the
   per-block gauge projection, the leaf argument, the weighted activities,
   the gap 2 log(I_1/I_2).
5. Check Section 10: the strip gap and the equivalence (24) with row 720.
6. Check the obstructions (1)-(4), (5) with det K, (6)-(9), (10), (11)-(15).
7. Check (16)-(20), (21), Section 8, Section 9, (26)-(28).
8. Write the verdict table and the RESULT line.

## Log

- Step 0: created the file.
- Step 1 done: read the row text; `library/gap-council-brief.md` (all);
  `library/gap-crux-skeleton-max.md` L1-175 (notation, Step 3 with 3.4) and
  L388-442 (Step 8 with 8.2); `library/gap-crux-skeleton-check-astra.md`
  L24-83, L245-264, L360-408 (A1, A2, path identity, KS-ZONE verdict);
  `library/gap-phys-seed.md` L240-345 (row 720: notation, Lemmas Z, Z',
  Z3, Theorem ZD, Theorem ZD-c).
- Step 2 done: read `library/gap-solve2-astra62.md` L1-445 in four ranges.

Notation used below (the file's own). Temporal coupling beta, spatial
coupling s (complex z). r_beta = I_2(beta)/I_1(beta), d_beta = -log r_beta,
b_beta = 1 + 6 beta. N = number of spatial sites. One-link density
p_beta(u) proportional to exp(beta Re u) on SU(2). Its multiplier on the
irreducible representation of dimension d is I_d/I_1. Line numbers "L" are
lines of `library/gap-solve2-astra62.md`.

Sources re-read for load-bearing citations (READ, at the pinned local copy
of the account, `YM4_sketch_500.tex`): L1222-1347 (hard-core tree
inequality; rooted-tree estimate; the theorem "absolute convergence and a
nonzero partition function", with |L(z)| <= sum_X |z_X| e^(a_X) and the
unrooted absolute bound sum_X |z_X| e^(a_X)); L2196-2231 (GL3:
c_l = 2 e^(-beta) I_(2l+1)(beta)/beta); L2313-2331 (GL8: Z = Tr L^s with
the vertex gauge projection); L20781-20797 (RF24, RF25: both passage-time
bounds, so K = Theta(beta)). They say what the file says they say. Also
read: row 865 `gap-sdcyl-ca-astra.md` L210-242 (Proposition W-phys-CA and
its even-gap upper bound) with its check `gap-sdcyl-ca-check-opus.md`
(all six statements HOLD, conditional on the account's premises); row 1144
`gap-solve-check-opus.md` verdict table (all 24 statements of row 1143
HOLD); row 720's check `gap-phys-seed-check.md` (Theorem ZD-c HOLDS).

## Step 3. Section 7 (L258-309): the block polymer expansion and (22)

Checked first, by hand, in this order.

**3.1 Reference law, L262 and L281-286. HOLDS.**
- L262. With Z_W the anisotropic Wilson integral, the temporal plaquettes
  give I(beta)^(3NT) times the normalized electric kernel, and the spatial
  ones give exp(-3NTz) exp(z sum_t X(U_t)). So
  Z_W = I(beta)^(3NT) e^(-3NTz) Z_T(z): an affine exponent in z. At s = 0
  every nonconstant gauge-invariant eigenvalue of K is a product of
  I_d/I_1 over at least four nontrivial edges, so the claimed bound
  e^(-1/b_beta) holds (it is weak but true). 1 <= Z_T(0) <= [1+eta(T/b_beta)]^(3N)
  holds because Tr(P C^T) <= Tr C^T = (sum_d d^2 (I_d/I_1)^T)^(3N).
- L281-286. Z_(T,h)(z) = Tr(U(h) (C e^(zX))^T) on the full link space, and
  the average over h is the projected trace, since P = integral of U(h) dh
  commutes with C and e^(zX). Grouping the T one-step kernels by blocks:
  the product of the kernels inside one block, for one link, equals
  D_l(u, v) times the bridge density. Each time t in 0..T-1 receives
  e^(z X(U_t)) once: block b takes its lower endpoint and its l - 1
  interior times. So the product expectation under (Haar endpoints,
  independent bridges) is exactly Z_(T,h)(z). Checked.
- Factorization. A label's variables are: for (e, b) electric, the
  endpoints of e at b and b+1; for (p, b) magnetic, the four bridges of p
  in block b and their endpoints. Two labels on disjoint links, or on the
  same link in blocks at cyclic distance at least two, share no endpoint
  and no bridge. Given the endpoints, bridges are independent, and each
  bridge law depends only on its own two endpoints. So families with
  disjoint variable sets are independent. The cyclic adjacency at the seam
  is right, because the last block ends at h.u_0. Checked.
- Bounds. ||D_l - 1||_inf <= sum_(d>=2) d^2 (I_d(beta)/I_1(beta))^l
  <= eta(l/b_beta) <= eta(A) for l >= H, by (1) at s = beta <= 6 beta.
  |exp(z sum_t w_p) - 1| <= e^(l|z|) - 1 <= e^(2H|z|) - 1, since
  |w_p| <= 1 and l < 2H. With H/(1+beta) <= 6A + 1, the choice
  c = log(1+sigma)/(2(6A+1)) works. Checked.

**3.2 Connected logarithm and the Kotecky-Preiss step, L288-293. HOLDS.**
- Neighbourhood count: a label has at most 4 links; per link and block
  there are 1 electric and 4 magnetic labels; 3 blocks. 4 x 5 x 3 = 60
  <= 64 = D. Checked.
- Connected sets of size r through a label: at most D^(2(r-1)) (closed walk
  around a spanning tree). Checked.
- Criterion: with sigma e^2 <= 1/(4D^3),
  D|X| sum_r D^(2(r-1)) (sigma e^2)^r <= |X| D^(-1)/(4D-1) < |X|.
  This is (eq:kp-explicit) of the account for the activities z_Y e^(|Y|)
  with a_Y = |Y|. The account's theorem then gives an absolutely
  convergent connected series, Z != 0, and the unrooted absolute bound
  sum_C |phi(C)| prod |z_Y| e^(|Y|) <= sum_X |z_X| e^(2|X|). The last sum
  is at most 6Nm times a number below one (3N electric and 3N magnetic
  labels per block). So all clusters with sum |X| >= m/4 have total
  absolute value at most 6Nm e^(-m/4). Checked.

**3.3 Seam comparison, L295. HOLDS.**
- A connected list with sum |X| < m/4 occupies a cyclic interval of fewer
  than m/4 blocks, since each label sits in one block and adjacency only
  joins equal or neighbouring blocks.
- Moving the seam: put u'_b = h.u_b and transform the bridge paths by h on
  the blocks between the seam and the first unused block b*. Haar is
  invariant; D_l(g_x u g_y^(-1), g_x v g_y^(-1)) = D_l(u, v) because D_l
  depends on u v^(-1) through a class function; bridges are equivariant;
  traced plaquettes are invariant. The seam moves into block b*, which no
  label of the list uses. So the short activities do not depend on h.
  Checked.
- Lifting from m to 2m blocks: an interval of fewer than m/4 blocks lifts
  in exactly two ways; block lengths, activities, the incompatibility graph
  and the Ursell coefficient are preserved; no new adjacency appears.
  Checked. Hence |2 log Z_(T,1) - log Z_(2T,1)| <= 24 Nm e^(-m/4) and
  |log Z_(T,h) - log Z_(T,1)| <= 12 Nm e^(-m/4).
- Averaging over h: |Z_(T,h)/Z_(T,1) - 1| <= e^eps - 1 pointwise in h, so
  the average lies in the same disk about 1. This gives zero-freeness of
  the projected Z_T and Z_(2T) and (22), under the stated smallness of
  C N m e^(-m/4). Checked.

**3.4 (22) and the thermal conclusion, L275-279, L297-301. HOLDS.**
- For real s, B(s) = e^(sX/2) K e^(sX/2) >= 0, so the normalized
  eigenvalues lie in [0, 1]. Then sum r_i^(2T) <= sum r_i^T, which gives
  1 + S(T) <= Z_T^2/Z_(2T) = e^J. Also J <= 2 log(1+S(T)) because
  Z_(2T) >= lambda_0^(2T). Checked.
- On physical cylinders m is of order t/(a(1+beta)) and beta = O(log(1/a)),
  so m dominates log N = 3 log(L/a). Checked.
- (21) and (22) together: the nearest zero of the projected Z_T lies at
  distance between c/(1+beta) and C/beta. Checked (with (21), Step 7).

**3.5 (23) and the two-level example, L304-309. HOLDS.**
- Cauchy on radius c/(2(1+beta)) with |J| <= C N m e^(-m/4) on the larger
  disk gives |a_q| <= C N m e^(-m/4) (2(1+beta)/c)^q, hence (23). Checked.
- Example: r(z) = exp[-1/b + (1/b - 1/T) z/beta] gives r(beta)^T = e^(-1),
  while |r(z)^T| <= e^(-T/(2b)) on |z| <= c/(1+beta) once
  c/(beta(1+beta)) <= 1/2. It refutes only the stated inference, as the
  file says. Checked.

Verdict for Section 7's positive claims: (22), the zero-free disk and the
thermal conclusion HOLD as written.

## Step 4. Section 11 (L384-410): (25) and the gap 2 log(I_1/I_2)

**4.1 The electric bound with d_beta, L394. HOLDS.**
- Riccati check: with R_k = I_(k+1)/I_k, R_k' = 1 - (2k+1) R_k/x - R_k^2
  (from I_k' = I_(k+1) + k I_k/x and I_(k+1)' = I_k - (k+1) I_(k+1)/x).
  At a point with R_(k+1) = R_k = R the difference of the two right sides is
  -(2k+3)R/x + (2k+1)R/x = -2R/x < 0, so no first contact from below. Near
  0, R_k ~ x/(2(k+1)) > R_(k+1). So R_(k+1) < R_k for all x > 0, and
  I_d/I_1 = R_1 ... R_(d-1) <= r_beta^(d-1). Then
  D_l = sum_d d (I_d/I_1)^l chi_d and |chi_d| <= d give
  ||D_l - 1||_inf <= eta(l d_beta). Checked.
- a <= (1+beta) d_beta <= B: the lower bound follows from (1) as displayed
  (it gives d_beta >= 1/b_beta, so (1+beta) d_beta >= 1/6), or with a = 1
  from its proof (u_1(beta) <= e^(-1/(1+beta))). The upper bound follows
  from 1 - r_beta <= C_1/beta. Checked.

**4.2 Per-block gauge projection, L396. HOLDS.**
- C and e^(zX) commute with every vertex gauge rotation (the kernel
  p(U U'^(-1)) is a class function of the product; X is gauge invariant),
  and P^2 = P. So Tr(P (C e^(zX))^T) = Tr(prod_b (C e^(zX))^(l_b) P): the
  insertions change nothing. Writing each P as an average over an
  independent h_b gives bridges from u_b to h_b.u_(b+1), as stated. The
  variables h_(x,b) enter only the D-factors and the bridges of block b:
  block b+1 starts at the untransformed u_(b+1). Checked.
- Dependency graph: two labels share a variable only if they are in the
  same block and share a vertex (gauge variable or bridge law), or are in
  adjacent blocks and share an edge (an endpoint). The file's graph (same
  or adjacent block and a shared vertex) contains all of these, which is
  all that the factorization needs. Neighbourhood: 8 x 6 x 5 x 3 = 720
  <= 1024 (4 vertices per label would already do). Checked.

**4.3 Leaf argument, L398. HOLDS.**
- In an occupied block with no magnetic label of X, the bridges of that
  block are not used by X and integrate to one. If x has degree one in
  E_b, the only factor of X that contains h_(x,b) is
  D_l(u, h_(x,b) v h_(y,b)^(-1)) - 1 (or the reversed edge). As h runs over
  Haar, u h_y v^(-1) h^(-1) runs over Haar, so the integral of D_l is 1 and
  the integral of D_l - 1 is 0. Factors of X in other blocks do not contain
  h_(x,b). So z_X = 0. Checked.
- A nonempty edge set with no leaf has all degrees >= 2, hence a cycle. On
  a periodic box with sides >= 4 the graph is simple and every cycle has
  length >= 4 (the shortest winding cycle has length = the side). So fewer
  than four edges always leave a leaf. The side hypothesis (>= 4) is
  needed here: at side 3 a winding 3-cycle has no leaf. The file states it.
  Checked.

**4.4 Weighted activities, L400-404. HOLDS.**
- Electric-only block (then at least four electric labels if z_X != 0):
  each of four D-factors gets e^(alpha d_beta l_b/4), and
  e^(alpha d_beta l/4) eta(l d_beta) <= C e^(-(1-alpha/4) d_beta l). Since
  l d_beta >= A_alpha b_beta d_beta >= A_alpha/6, a large A_alpha makes this
  at most sigma. alpha < 4 is used exactly here. Checked.
- Block with a magnetic label: e^(alpha d_beta l_b) <= e^(2 alpha d_beta H),
  and d_beta H <= 6 A_alpha B + B, H/(1+beta) <= 6 A_alpha + 1 are bounded,
  so a small c_alpha makes e^(2 alpha d_beta H)(e^(2H|z|) - 1) <= sigma.
  Checked.
- So |z_X| e^(alpha d_beta L(X)) <= sigma^(|X|) for every X (trivially when
  z_X = 0). Apply the Section 7 criterion to w_X := z_X e^(alpha d_beta L(X)).
  The account's unrooted bound for w gives
  sum_C |phi(C)| prod_(Y in C) |z_Y| e^(alpha d_beta L(Y)) <= C N m, with
  L counted once per polymer of the list. KP also gives Z_T(z) != 0 on the
  projected space directly. Checked.

**4.5 Cancellation and (25), L406. HOLDS.**
- On the 2m-circle a connected list that omits a residue r mod m avoids the
  blocks r and r+m; adjacency joins only equal or neighbouring blocks; so it
  lies in one of the two arcs of m - 1 blocks, and it projects to a list on
  the m-circle that omits r. Conversely a list on the m-circle that omits a
  block lies in an arc and has exactly two lifts. Block lengths repeat with
  period m, every block has its own gauge average (no seam), so
  activities, incompatibilities and Ursell coefficients agree. So all
  lists that omit a residue cancel in 2 log Z_T - log Z_(2T). Checked.
- A remaining list meets every residue class r, and l_r = l_(r+m), so
  sum_(X in C) L(X) >= sum_r l_r = T. The weighted bound then gives
  |2 log Z_T - log Z_(2T)| <= e^(-alpha d_beta T) (2 C N m + C N 2m). This
  is (25). Checked.

**4.6 The gap, L392 and L408. HOLDS.**
- At fixed beta, s, N: e^(-T m_lat) <= S(T) <= exp(C_alpha N m e^(-alpha d_beta T)) - 1.
  Take logs, divide by T, let T -> infinity at fixed N (m/T -> 1/H, and
  the prefactor N m only adds log(N m)/T -> 0). So m_lat >= alpha d_beta,
  uniformly in N. The trace runs over the whole gauge-invariant space, so
  all eight flux sectors are included. With alpha = 2:
  m_lat >= 2 log(I_1(beta)/I_2(beta)). Checked.
- s = 0: a nonconstant gauge-invariant spin network has no degree-one
  vertex (a lone nontrivial representation at a vertex has no invariant),
  so at least four nontrivial edges, each multiplier <= r_beta; the
  fundamental plaquette gives r_beta^4. So the s = 0 gap is 4 d_beta, and
  2 d_beta is half of it, as (KS-ZONE)(i) asks. Checked.
- Matching row 863 L420-422: weights beta_t on time-like and beta_s on
  space-like plaquettes are this file's beta and s. If s beta <= c_0 and
  beta >= 1 then s <= 2 c_0/(1+beta), so c_0 = min(c_2, c)/2 places both
  clauses in the proved strips (L408). Clause (i) HOLDS for every periodic
  box with sides >= 4.

Sanity point (my own, not used): first-order perturbation theory moves the
plaquette level by O(s) per lattice time step, against 4 d_beta of order
1/beta; on s <= c/(1+beta) this is a small fraction of the electric gap,
which agrees with the size of the claim.

## Step 5. Section 10 (L368-382): the strip gap and the equivalence (24)

**5.1 Unprojected reformulation, L370. HOLDS.**
- By (17), log Tr T^n - log Tr(P T^n) = log p_n(1) lies in
  [0, n^3 log(1 + eta(n/(7 b_beta)))]. At fixed beta this tends to 0 as
  n -> infinity, so the bulk pressures agree. At fixed physical L along the
  trajectory, n_j^3 eta(n_j/(7 b_(beta_j))) -> 0 since n_j grows like
  b^(K_j) and b_(beta_j) like K_j. So D^+ is unchanged.
- The top eigenvector of the unprojected operator is positive and unique,
  hence gauge invariant, hence the projected vacuum. Every non-singlet
  isotypic block has energy >= 1/(7 b_beta) by (18), and
  n_j/(7 b_(beta_j)) -> infinity, so z^- is unchanged (also when it is
  infinite). Checked.

**5.2 Strip gap 1/(4H) and thermal clause (ii), L372. HOLDS.**
- e^(-T m_lat) <= S(T) <= exp(C N m e^(-m/4)) - 1 at fixed N, T -> infinity,
  gives m_lat >= 1/(4H). Checked.
- H <= (7A+1) beta for beta >= 1. If N <= exp(T/(C_1 beta)) then
  log N <= (m+1) H_0/C_1. With C_1 = K H_0 and N >= 64 one gets
  m + 1 >= K log 64, so m is large, and C N m e^(-m/4)
  <= C e^((m+1)/K) m e^(-m/4) is below log(1 + 1/1650) for K large. Then
  S(T) <= 1/1650. Row 863's clause (ii) has the hypotheses
  t >= C beta log beta and |B| <= exp(t/(C beta)); the second alone suffices
  here, so (ii) follows with C = C_1 (after the change of product constant
  noted in 4.6). Checked.

**5.3 The equivalence (24), L374-380. HOLDS.**
- Derivative identity (stated in Section 9, L361): d/ds log Z_k(s) equals
  the mean of sum_t X(U_t) = 3Nk w_bar_k(s). So
  J'(s) = 2 (3NT) w_bar_T - 6NT w_bar_(2T) = 6NT [w_bar_T - w_bar_(2T)].
  The affine Wilson normalization cancels in J (2T - 2T = 0 and
  -6NTs + 6NTs = 0). Checked.
- Left side of (24) = limsup_j [J(beta_j) - J(s_0)], and J(s_0) -> 0 by (22)
  at T = n/2 (m of order n/log n, log N = 3 log n). So the left side is
  limsup_j J(beta_j). Checked.
- log(1+S) <= J <= 2 log(1+S) with S = S(n/2; n^3) of the isotropic cube
  (Step 3.4). So (24) gives limsup_j S_j < 1/1650, which is (PHYS-SEED) at L
  with the two-stage threshold (row 720 L313). Theorem ZD-c (row 720
  L311-320; checked HOLDS in `gap-phys-seed-check.md` L73, L126) then gives
  (BDD-Delta) and (Z-UNB), hence (W). Grid: L in P makes n = L/a_j
  divisible by 4, so T = n/2 is an integer. Checked.
- Converse: (W) gives (PHYS-SEED) at some l (ZD-c). Lemma Z3 gives
  D_j(L/4) <= 1024 s_k with s_k -> 0 along the dyadic sizes, and Lemma Z
  with T_0 = n/4 gives S_j(n/2; n^3) <= e^(64 D_j(n/4)) - 1, uniformly in j.
  So limsup_j S_j -> 0 along P, J <= 2 log(1+S), and (24) holds at a large
  L with strict margin. Checked.
- Remark (not a correction): (24) is (PHYS-SEED) with J in place of
  log(1+S) and the vanishing J(s_0) subtracted. It is an exact real form of
  (W), as the file says (L380), and it carries no estimate of its own.

## Step 6. Obstructions (1)-(4), (5) with det K, (6)-(10), (11)-(15)

**L17 (one-link conditional law). HOLDS.** A 4D link lies in 6 plaquettes;
each gives beta Re(u M) with |M| = 1, a linear functional of norm beta. The
sum has norm s <= 6 beta, so the conditional density is a translate of p_s.

**(1), L19-24. HOLDS.** With chi_d(theta) = sin(d theta)/sin(theta) and Haar
weight (2/pi) sin^2 theta, int e^(s cos theta) chi_d dHaar = I_(d-1)(s) -
I_(d+1)(s) = (2d/s) I_d(s), and the normalization is (2/s) I_1(s). So the
multiplier of p_s on dimension d is I_d/I_1; this is GL3 normalized. The Riccati equation, its positive root
u_k = e^(-arsinh((k+1/2)/s)), the first-contact argument and
arsinh x >= x/(1+x) (since 1/sqrt(1+x^2) >= 1/(1+x)^2) all check. The last
step needs (k+1/2)/(s+k+1/2) >= 1/(1+s), true for k >= 1/2. GUIDE run:
no violation of R_k < u_k, R_(k+1) < R_k or I_d/I_1 <= e^(-(d-1)/(1+s)) on
181 points of s in [0.01, 1946], d <= 39.

**(2), L26-32. HOLDS.** Each E pi_d(X_i) is a scalar of size <= (1) times a
unitary; products with fixed insertions keep the operator-norm bound;
inversion costs d^2. eta(x) <= C e^(-x) for x >= 1 by factoring e^(-x).

**(3), L34-38. HOLDS.** A mu-link and a nu-link of one plaquette share a
vertex; on a cubical grid two perpendicular coarse lines share a vertex
only at a coarse vertex, and the links there were dropped; collinear links
never share a plaquette; distinct parallel lines are h >= 5 apart. Same for
the four based winding lines (they meet only at the base point). The
conditional joint density is a product of densities each within eta of 1.

**L40 (windings: Haar limit against central concentration). HOLDS.** The
physical-torus limit follows from (3) with M = 4. E[(tr U/2)^2] = 1/4 under
Haar by character orthogonality, and = 1 at central tuples. The fixed-lattice
concentration is row 1143 Section 6 (READ; checked by row 1144, items 12 and
15).

**(4), L42-49. HOLDS.** Slice 1 is unselected, so F_1 is measurable for the
conditioning; |E(F_0 | ext)| <= ||p - 1||_inf ||F||_(L^1(nu)) <= delta ||F||_1;
the one-slice marginal has density in [1 - delta, 1 + delta]; and
||F||_1 <= ||F||_2. This gives delta(1+delta)/(1-delta). The spectral form
uses 1_[0,E](t) <= e^(E-t). The last claim: e^E delta ~ C M e^(-(h-2)/(2b)) -> 0.

**(5) with det K, L56-75. HOLDS.**
- im(d_1 B) = exact 2-forms and d_1 B injective: closed 1-forms have
  dimension (V-1) + 4, and the map "closed form -> values on tree + 4 base
  edges" is injective (a closed form vanishing on the tree has periods
  equal to its values on the base edges, so it is zero), hence bijective.
  Exact 2-forms have dimension 4V - (V+3) = 3V - 3 = M.
- S closed (S_ij depends on x_i, x_j only); the non-exact part of a closed
  2-form is its constant mode (Fourier homotopy for k != 0; exact forms
  have zero mean). The mean c_ij n^2/n^4 and the squared norm
  V (c_ij/n^2)^2 = |c_ij|^2 check.
- det K = (vol B_perp)^2 det(d_1* d_1 on co-exact), vol B_perp =
  1/vol(gradients + seams) = (V det' Delta)^(-1/2) (|det Q| = 1; cofactor
  = det' Delta/V by the matrix-tree theorem; seam harmonic parts of norm
  sqrt(V)/n, joint volume V), and det(d_1* d_1 on co-exact) = (det' Delta)^3.
  So det K = (det' Delta)^2/V. Checked.
- GUIDE run (pure Python, Cholesky of K for the comb tree and the four base
  wrapping links): log det K - [2 log det' Delta - log V] = 4.6e-13,
  3.4e-13, -1.1e-13 on the tori 3^4, (3,3,3,4), (4,3,3,3).
- The power count: h_0^(M+4) (2 pi)^(3M/2) differs from
  [h_0^3 (2 pi)^(9/2)]^V by V-independent factors only. The limiting integral
  itself is row 1143 (11) and Section 6 (READ; checked by row 1144 item 14).

**(6), L82-99. HOLDS.** The Frullani representation, the Poisson identity
H_n(t) = n^4 sum_m p_t(nm), the image bound P(Poisson(8t) >= n) <= (8t)^n/n!
(the extra e^8 is harmless), the contour shift giving
p_t(x) <= C t^(-2) e^(-|x|_1/sqrt t), and the scaling limit at t = n^2 u all
check. The 2 log n is -2 zeta(0) log n for the continuum torus, as expected.

**(7), L101-112. HOLDS.** Open box: d_1* d_1 = lambda_m on the r(m) - 1
co-exact components at frequency m, det' Delta_open = prod lambda_m, so
det K_open = b^4 prod lambda_m^(r(m)-1)/prod lambda_m = b^4 prod lambda_m^(r(m)-2).
GUIDE run: agreement to 3e-14 at b = 2 and b = 3. The face correction
O(b^3 log b), the Riemann mean -> h, and 3 + O(1/b) free edges per site
check. c_inf then follows from row 1143 (14)-(16) (READ; checked by row 1144
items 19-22).

**(8), L114-121. HOLDS.** log c_n - n^4 c_inf = log C_* + (3/2) log V
- 3(2 log n + k_Delta) + o(1) = log C_* - 3 k_Delta + o(1): the two log n
terms cancel exactly. With (16)-(17) of row 1143 this is (8).

**(9), L123-127. HOLDS AFTER CORRECTION.** (9) is the identity
R = D - B - C with D in [0, A] and C(n_j) bounded. The monotonicity step
holds: F/n_mu = log ||lambda||_(n_mu) is non-increasing in n_mu, so
F(n^4)/n^4 <= F(n_*^4)/n_*^4 and D(n) <= (n/n_*)^4 D(n_*) at the same beta.
Correction (wording): "(APR)" is used but not defined in this file. It is
row 720's hypothesis (`gap-phys-seed.md` L357: D(L_0 nu; beta(nu)) <= A),
and row 720 L363 (ii) says the account gives it as in 1.1.5 (iii). Name it.

**(10), L129-135. HOLDS**, with the hypothesis of (9) (bounded D at that
size), as the file says. RF25 (outline L20793-20795) gives both
(beta - h)/B_sharp - 1 <= K and K <= 1 + (beta - h - B_sharp + c_5)/lambda_sharp,
so log n_j = O(beta_j); then beta^(-q) P_q(log n) is bounded for each q <= Q.

**(5) on rectangles, L144-150. HOLDS.** prod_i sqrt(V)/n_i = V; the seam
mean is c_ij/(n_i n_j), so the constant-mode norm is c_ij^2 s_i^2 s_j^2
with s_i = V^(1/4)/n_i. Lagrange's identity gives the 3x3 matrix
diag(s_-q)(|u|^2 I - u_-q u_-q^t) diag(s_-q); its determinant is
(prod_(i!=q) s_i)^2 |u|^6 (u_q^2/|u|^2) = |u|^4. The max-coordinate
partition with x = (+-r)(b, 1) and int_0^inf r^3 e^(-a r^2) dr = 1/(2a^2)
gives sum_q int |u|^(-4) db = int_(R^4) e^(-sum s_i^2 x_i^2) dx = pi^2.
Checked. The shape enters the rest of row 1143's limiting integral only
through this term, as L144 states; I read that from the derivation of (5)
and did not re-derive row 1143's integral.

**(11), L152-157. HOLDS.** 2 cosh w - 2 cos phi = e^w |1 - e^(-w) e^(i phi)|^2
and prod_j (1 - r e^(2 pi i j/T)) = 1 - r^T give e^(T w_p)(1 - e^(-T w_p))^2;
the p = 0 product is T^2. Then V^(3/2) (det')^(-3) = n^(9/2) T^(3/2) T^(-6) ...
= n^(9/2) T^(-9/2) .... Checked.

**(12), L159-169. HOLDS.** Exponents k + 3k - 2(2k) = 0, so C_*, n^(9/2),
A^(n^3 T), e^(-3T sum w), beta^(...) and log beta cancel;
T^(-9/2) gives (9/2) log(4/3); (1-x)(1-x^3)/(1-x^2)^2 = (1+x+x^2)/(1+x)^2.
GUIDE: the two sides of this log identity agree to 12 digits at four x.

**(13), L170-174. HOLDS.** Cauchy-Schwarz gives Z(2k)^2 <= Z(k) Z(3k); g is
non-increasing; at a seed S(n; n^3) <= S(n/2; n^3) < 1/1650.

**Neutral sector, L176-180. HOLDS.** Check of the new step: with h_i h_t =
-h_t h_i and h_l h_t = -h_t h_l, the variable h_l' = h_i^(-1) h_l commutes with
h_t, h_i and the other spatial h_m; left translation keeps product Haar;
each new commutator error is at most a sum of two old ones, so the new
action is at most a universal multiple of the old one. The one-plane input
is row 1143 (1), (3)-(4) (READ; checked by row 1144 items 1-4, 16). Then
Z^w/Z = O(beta^(-3/2)/log beta) -> 0 and Z_(n,e)/Z_n -> 1/8 by the centre
projection, so each sector has the limit (12).

**(14)-(15), L182-193. HOLDS.** -nu log k - nu log 3k + 2 nu log 2k =
nu log(4/3); log[Q(k)Q(3k)/Q(2k)^2] >= 0; the bound (13) applies, also to
the neutral trace (vacuum in the even sector; S_ev <= S). With nu = 9/2 the
floor (9/2) log(4/3) = 1.2946 exceeds log(1 + 1/1650) = 6.06e-4.

## Step 7. (16)-(20), (21), Section 8, Section 9, (26)-(28)

**(16), L202-207. HOLDS.** Given the spatial links, a temporal plaquette
contains two temporal links of one layer at neighbouring sites, so layers
are independent. In one layer the conditional law of a temporal link is a
translate of p_s, s <= 6 beta. The greedy 7-colouring (degree 6) leaves a
colour with weight >= w/7; conditional on the other temporal links of the
layer, that colour's links are independent, and each E pi_d has norm <=
e^(-(d-1)/b_beta) by (1). Averages and time-ordered products keep the bound.

**(17), L209-215. HOLDS.** Fourier inversion on SU(2)^N with
|tr(A pi(h))| <= dim(pi) ||A|| gives ||p - 1|| <= prod_x (1 + eta) - 1. In
temporal gauge (gauge rotations on slices 1..T-1 leave the based holonomy
unchanged), the density of the holonomy vector at h is
Tr(T^T U(h))/Tr(P T^T); at h = 1 this is the trace ratio, which is >= 1
because P commutes with the positive T^T.

**(18), L217-221. HOLDS.** Tr(T^T U(h)) = sum_pi chi_pi(h) Tr T_pi^T, so the
character coefficient is Tr(P T^T) E chi_pi(H), bounded by
dim(pi) e^(-Tw/(7 b_beta)) via (16). With Tr T_pi^T >= ||T_pi||^T and
Tr(P T^T) = lambda_0^T (1 + S(T)), S(T) -> 0 at a fixed box, T-th roots give
(18). The flux sectors are singlets (w = 0). Checked.

**(19), L224-231. HOLDS.** floor(n/2)^2 n >= n^3/9 for n >= 3; the chosen
plaquettes are edge-disjoint; Cauchy-Schwarz gives I(2 beta)/I(beta); and
the row-sum bound applies to the positive operator C M^2, which is similar
to M C M. GUIDE: I(2b)/I(b) = (1/2) e^(-b) I_1(2b)/I_1(b) has sup 0.5177 (at
beta = 1) on [1, 3045] and tends to 2^(-3/2) = 0.3536. Lower bound: on the
ball of angular radius beta^(-1/2)/4 each plaquette costs beta a <= 1/2, a
one-step transition stays in the ball with probability >= c_1, and the
Rayleigh quotient gives e^(-CN).

**L233 (bare flux comparison). HOLDS AFTER CORRECTION.** The cut argument is
row 863's A1 (checked by row 879: HOLDS AFTER CORRECTION, the correction
concerns other groups). The norm is exactly r_beta^n: at least n distinct
half-integer edges, each multiplier <= r_beta, and the straight fundamental
winding attains r_beta^n and lies in the sector whose only odd bit is that
direction. Correction (citation): "I_d/I_1 <= r_beta for every d >= 2 by
the ratio bound in Section 1" - Section 1 proves only (1),
I_d/I_1 <= e^(-(d-1)/b_beta), which does not give this. The needed bound is
the ordering R_(k+1) < R_k proved in Section 11 (L394), or the classical
fact that I_nu(x) decreases in nu. The conclusion r_beta^n/lambda-hat_0 >=
e^(c n^3 - n d_beta) -> infinity stands.

**(20), L240-253. HOLDS.** The density bound of (17) survives plaquette
signs. For a negative boundary sign, sum_t (1 - Re(u_t u_(t+1)^(-1))) =
(1/2) sum_t |u_(t+1) - u_t|^2 with u_T = -u_0, and the antiperiodic
spectrum gives >= T(1 - cos(pi/T)), attained by u_t = exp(v pi t/T). Sign
count: at h^0, n^2 negative i-edges (twisted) against 0 (periodic); at
h^1, the cut n-1 -> 0 has sign (-1)(twist) = +1 and the cut 0 -> 1 has
sign -1 when twisted, and both cuts are negative when periodic. So
Delta m(h^0) = m and Delta m(h^1) = m - 2m = -m. All spatial plaquettes are
1 in the minimizers (two parallel i-links of one plaquette are on the same
cut and carry the same u_t). (20) and the "at least one of the two" claim
follow.

**(21), L264-272. HOLDS.** Mean zero: the flip of one link at all times
commutes with K and reverses the plaquettes through it; summing over links
gives 4 Tr(K^T X) = 0. Var Y = (T/Z_T(0)) sum_s Tr(K^(T-s) X K^s X), and
keeping the constant state gives r_beta^(4s) ||X||^2 = r_beta^(4s) 3N/4. The
Bernoulli step and Z_T(0) <= 2 give c N T beta. Zero radius: Re f <= 3NTr,
the circle mean of Re f is 0, the second Fourier coefficient of Re f is
f''(0) r^2/4, and a nonnegative function's Fourier coefficients are bounded
by its mean, so r <= 12/(c beta). GUIDE: beta(1 - r_beta) = 0.76, 1.23,
1.46, 1.496, 1.4996 at beta = 1, 2.5, 10, 100, 1000 (so C_1 = 3/2 works
there), and r_(2.5) = 0.50720 agrees with row 863.

**Section 8, L313. HOLDS.** E[tr(v)/2] = r_beta^H from the identity, and the
sup-norm bound gives |E[tr(v)/2]| <= eps; so H >= log(1/eps)/d_beta, of order
beta.

**Section 8, L315-316. HOLDS.** On the sign family the log weight is
s(1 + (H-1) prod eps_i); its fourth Walsh coefficient is s(H-1); endpoint
functions and functions missing one history have coefficient 0; a Walsh
coefficient is bounded by the sup norm. The essential-supremum remark needs
the approximants to be continuous, as the file says.

**Section 8, L318-330. HOLDS.** ||Y_p||_2^2 = (1/4) sum r^(4|t-u|) >= c_0 H beta.
Y_p° is orthogonal to the allowed class (each summand is linear in each
centred factor, and the bridges are independent given the endpoints), and
Y_p - Y_p° is in the class. The bridge mean bound
C exp(-min(t, H-t)/b_beta) follows from D_t D_(H-t)/D_H with D_H >= 1/2;
telescoping gives ||Y_p - Y_p°||_inf <= C' b_beta; so ||Y_p°||_2 >=
(1/2) sqrt(c_0 H beta) for H >= A_0 (1+beta). Note: the reference here is
stationary chains, not the bridge reference of Section 7; the paragraph
states this.

**Section 9, L337-342. HOLDS, conditional on the named witness.** W-phys-CA
(row 865 L218-240; its check finds all six statements HOLD, conditional on
the account's premises) gives S_ev(n_A; B) >= rho_CA^(2A/(3d)) with
A = n_A a_K >= 2d and box sides multiples of ell_*^CA. Here A = t = L/2 and
n_A = T = n/2. Since J >= log(1+S) >= log(1+S_ev), J(beta) >= j_L. With
(23), |J(beta) - P_p(beta)| >= j_L - o(1).

**Section 9, L344-357. HOLDS, conditional on the witness.** Jensen gives a
nonnegative circle mean of log|V_k|, so the mean of |log|V_k|| is at most
6Nkr; on a radius in [beta(1+3eps/4), beta(1+7eps/8)] avoiding zeros, the
mean of |Re J| is O(1 + NTr); the Herglotz kernel is at most
2r/(r - |z|) <= 8(1+eps)/eps on |z| <= beta(1+eps/2); Hadamard's three
circles with inner radius c/(2(1+beta)) and inner bound e^(-m/5) gives the
weight log(1+eps/2)/log[2 beta(1+eps/2)(1+beta)/c] >= c' eps/(1 + log beta).
With m of order n/log n and beta = O(log n), -c'' sqrt(m)/(1 + log beta)
beats O(log n). The branch remark holds (positive partition functions on
the real segment).

**Section 9, L359-363. HOLDS** (the identity is checked in 5.3).

**Section 9, L365. HOLDS.** F_0i = u F_0'i and dt = dt'/u give coefficients
u beta and s/u; the common value sqrt(beta s) <= sqrt(c) on the strip and
= beta at s = beta.

**(26), L414-420. HOLDS.** Relative to four stationary chains the reference
law of the four edge paths has density prod 1/D_l(u_e, v'_e) (given h_b,
v' = h_b.u_(b+1) is Haar); D_l <= 1 + sigma <= 2; the second moment is >=
2^(-4) c l beta; the flip of one edge path with its two endpoints keeps the
reference and reverses Y_p, so E e^(sY) = E cosh(sY) >= 1 + s^2 E Y^2/2.

**z_B, L422. HOLDS.** D_l - 1 is the kernel of C^l - P_e; the vertex averages
give the gauge projector of the four-edge space; all factors commute and
are positive; the fundamental plaquette trace is a common eigenfunction
with eigenvalue r_beta^(4T); a positive trace is at least that eigenvalue.

**L424 (absolute divergence). HOLDS.** A and B share edges in one block, so
they are incompatible; the Ursell value on the complete graph with k copies
of A and one B, times the k+1 orderings, is (-1)^k; equivalently
log(1 + u z_A + v z_B) has u^k v coefficient (-1)^k z_A^k z_B. These lists
meet every block, so they survive the cancellation of (25) on the T side
and have no partner on the 2T side. |z_A| >= c (s beta)^2 >= 1 once
s beta >= C. The file correctly limits the claim to absolute summation in
these activities.

**(27), L426-432. HOLDS, conditional on the witness.** W-phys-CA gives an
even eigenvalue at lattice energy <= a_j M_K (row 865 L234-240:
m_ev <= (2/(3d)) log(3 C_K/c_K)); the transfer is compact, so it is an
eigenvalue. On the span of the vacuum and that eigenvector a rank-one R
kills a unit vector, and U^h has smallest singular value e^(-a_j M_K h)
there. Checked.

**L434. HOLDS, conditional on the witness.** On the strip, the normalized
H-step transfer minus the vacuum projector has norm r_1^H <= e^(-2 d_beta H),
and d_beta H >= a A is bounded below. At s = beta, (27) gives an error
>= e^(-a_j M_K H) -> 1 for H = O(1 + beta_j).

**(28), L436-442. HOLDS, conditional on the witness.** K_j >=
m_ev(s_0)/m_ev(beta_j) >= 2 d_beta/(a_j M_K) >= c/(a_j(1+beta_j)); by RF25
this is exponential in K_j. Continuity: T(s) = e^(sX/2) K e^(sX/2) is norm
continuous and min-max applies; K has strictly positive eigenvalues, so
m_ev(s) is finite and continuous; the intermediate-value claim follows from
m_ev(s_0) >= 2 d_beta > eps_j > a_j M_K >= m_ev(beta_j) for large j.

**OPEN paragraphs (L51, L77, L137, L195, L235, L255, L332, L382, L410).**
No claim beyond what is proved; the small examples in L51 and L255 are
correct.

**GUIDE paragraphs.** One citation slip, L260: "Lemmas A1-A3" - row 863 has
Lemmas A1 and A2 and the path identity 3.3; there is no Lemma A3. Read
"Lemmas A1, A2 and the path identity 3.3". L279 "Check 879" is right
(FINISH row 879 is `gap-crux-skeleton-check-astra`).

## Step 8. Verdict table and result

Scope remarks (not corrections). (a) The strip results are anisotropic.
Theorem S needs exchange of time and space, so a strip seed does not feed
(W) directly (row 879 says the same of A2); the file claims no such use.
(b) The strip proof uses only the electric spectrum and small magnetic
blocks, so it is not selective in the sense of the brief, Section 4; it is
not offered as a step on the crux. (c) Everything at s = beta in Sections 9
and 12 is conditional on row 865's W-phys-CA and the account's premises, as
the file labels it.

| # | Statement (line in `gap-solve2-astra62.md`) | Verdict |
|---|---|---|
| 1 | Section 7 set-up: Z_W = I^(3NT) e^(-3NTz) Z_T(z); s = 0 vacuum and spectrum; 1 <= Z_T(0) <= [1+eta]^(3N) (L262) | HOLDS |
| 2 | Block construction: reference law, bridges, the two factor types, exact product expectation, factorization, sup bounds (L281-286) | HOLDS |
| 3 | Connected logarithm: D = 64, D^(2(r-1)) count, Kotecky-Preiss with a_X = |X|, weighted sum <= 6Nm, long terms <= 6Nm e^(-m/4) (L288-293) | HOLDS |
| 4 | Seam comparison: short terms independent of h, doubled on 2m blocks; averaging over h (L295) | HOLDS |
| 5 | (22) and zero-freeness of projected Z_T, Z_2T on |z| <= c/(1+beta) (L275-279) | HOLDS |
| 6 | Thermal conclusion 1+S <= Z_T^2/Z_2T; m dominates log N; nearest zero at distance in [c/(1+beta), C/beta] (L297-301) | HOLDS |
| 7 | (23) and the two-level example (L304-309) | HOLDS |
| 8 | (25) (L386-392) | HOLDS |
| 9 | Electric bound ||D_l - 1|| <= eta(l d_beta) via R_(k+1) < R_k; a <= (1+beta) d_beta <= B (L394) | HOLDS |
| 10 | Gauge projection at every block; dependency graph, D = 1024 (L396) | HOLDS |
| 11 | Leaf argument: zero activity unless >= 4 electric labels or a magnetic label per occupied block (sides >= 4) (L398) | HOLDS |
| 12 | Weighted activities |z_X| e^(alpha d_beta L(X)) <= sigma^|X|; weighted KP bound C N m (L400-404) | HOLDS |
| 13 | Cancellation of lists omitting a residue; remainder has sum L >= T (L406) | HOLDS |
| 14 | Gap m_lat >= alpha d_beta, so >= 2 log(I_1/I_2) at alpha = 2, uniform in volume, all flux sectors; s = 0 value 4 d_beta exact; KS-ZONE constants (L392, L408) | HOLDS |
| 15 | Unprojected operator gives the same D^+ and z^- (L370) | HOLDS |
| 16 | Strip gap 1/(4H); N <= exp(T/(C_1 beta)) gives S(T) <= 1/1650: clause (ii) of (KS-ZONE) (L372) | HOLDS |
| 17 | (24), its derivative form, and its equivalence with (W) through row 720 Theorem ZD-c, both directions (L374-380) | HOLDS |
| 18 | One-link conditional law, s <= 6 beta (L17) | HOLDS |
| 19 | (1) (L19-24) | HOLDS |
| 20 | (2) (L26-32) | HOLDS |
| 21 | (3) (L34-38) | HOLDS |
| 22 | Windings: Haar limit on physical tori against central concentration on fixed tori, 1/4 against 1 (L40) | HOLDS (fixed-torus part READ from row 1143, checked by row 1144) |
| 23 | (4) (L42-49) | HOLDS |
| 24 | (5) with det K = (det' Delta_n)^2/V (L56-75) | HOLDS (linear algebra checked; GUIDE run agrees to 5e-13; limiting integral READ from row 1143) |
| 25 | (6) (L82-99) | HOLDS |
| 26 | (7), open-box det K_empty (L101-112) | HOLDS (GUIDE run agrees at b = 2, 3) |
| 27 | (8) (L114-121) | HOLDS |
| 28 | (9) and D(n) <= (n/n_*)^4 D(n_*) (L123-127) | HOLDS AFTER CORRECTION: define "(APR)" (row 720, `gap-phys-seed.md` L357) |
| 29 | (10) (L129-135) | HOLDS (under the bounded-D hypothesis of (9), as stated) |
| 30 | (5) on rectangles, same C_*; shape-independent commutator integral pi^2 (L144-150) | HOLDS |
| 31 | (11) (L152-157) | HOLDS |
| 32 | (12) (L159-169) | HOLDS |
| 33 | (13) and the seed requirement on K (L170-174) | HOLDS |
| 34 | Neutral sector: Z^w = O(beta^(-9V/2)), Z_e/Z -> 1/8, same floor (L176-180) | HOLDS (multi-plane reduction checked; one-plane input READ from row 1143) |
| 35 | (14)-(15) (L182-193) | HOLDS |
| 36 | (16) (L202-207) | HOLDS |
| 37 | (17) (L209-215) | HOLDS |
| 38 | (18) (L217-221) | HOLDS |
| 39 | (19) (L224-231) | HOLDS |
| 40 | Bare flux comparison, norm exactly r_beta^n, r_beta^n/lambda-hat_0 -> infinity (L233) | HOLDS AFTER CORRECTION: I_d/I_1 <= r_beta is not "the ratio bound in Section 1"; cite L394 (R_(k+1) < R_k) or the monotonicity of I_nu in nu |
| 41 | (20) and the two pins (L240-253) | HOLDS |
| 42 | (21) and the zero within C/beta (L264-272) | HOLDS |
| 43 | Section 8: H >= c_eps beta for a sup-norm reference (L313) | HOLDS |
| 44 | Section 8: Walsh bound |s|(H-1) (L315-316) | HOLDS |
| 45 | Section 8: L^2 bound c|s| sqrt(H beta) (L318-330) | HOLDS |
| 46 | Section 9: witness floor j_L and the Taylor-remainder error (L337-342) | HOLDS, conditional on W-phys-CA |
| 47 | Section 9: uncanceled zero or pole within beta(1 + m^(-1/2)) (L344-357) | HOLDS, conditional on W-phys-CA |
| 48 | Section 9: J' = 6NT(w_bar_T - w_bar_2T) and the lower bound on its integral (L359-363) | HOLDS (identity unconditional; bound conditional) |
| 49 | Section 9: time rescaling, sqrt(beta s) (L365) | HOLDS |
| 50 | (26) (L414-420) | HOLDS |
| 51 | z_B >= r_beta^(4T) (L422) | HOLDS |
| 52 | Divergence of the absolute subseries for s beta >= C (L424) | HOLDS |
| 53 | (27) (L426-432) | HOLDS, conditional on W-phys-CA |
| 54 | Rank-one error on the strip against s = beta (L434) | HOLDS, conditional on W-phys-CA |
| 55 | (28) and the intermediate-value claim (L436-442) | HOLDS, conditional on W-phys-CA |
| 56 | RESULT line (L444) | HOLDS |
| - | GUIDE L260: "Lemmas A1-A3" | wording: row 863 has A1, A2 and the path identity 3.3 |

No statement FAILS. Two hold after a correction of a definition or a
citation (rows 28 and 40); neither changes a constant or a conclusion. No
mass gap is claimed by the file or by this check.

GUIDE runs (pure Python, scripts in the session scratchpad, not kept in the
repository; peak memory about 22 MB): (i) det K against
(det' Delta)^2/V on three small periodic rectangles and the open-box
formula at b = 2, 3; (ii) Bessel-ratio inequalities on a grid, the range of
(1+beta) d_beta (1.50 to 2.85 on [1, 2000]), sup I(2b)/I(b) = 0.5177, and
the identity behind (12). All agree. They guide only.

RESULT: HOLDS — check of row 1145 (`library/gap-solve2-astra62.md`),
checked line by line by hand by Claude Opus 5.5 (max effort), with the
positive claims first: the block polymer expansion of Section 7 (reference
law, bridges, factors, the Kotecky-Preiss step against the account's
theorem at outline L1222-1347, the seam comparison, (22)), Section 11
((25) with the bound eta(l d_beta), the per-block gauge projection, the
leaf argument, the weighted activities, the gap 2 log(I_1/I_2)) and
Section 10 (strip gap, clause (ii), and the equivalence (24) with row 720)
all HOLD, so both clauses of row 863's (KS-ZONE) are proved for SU(2) on
periodic boxes with sides at least 4; all obstructions hold, those at
s = beta conditionally on row 865's W-phys-CA as labelled; two corrections
of wording/citation only ((APR) undefined at L127; the ratio bound cited
at L233 is proved at L394, not in Section 1) and one citation slip in a
GUIDE line (L260); 0 FAILS; (24) is an exact real restatement of (W) with
no estimate of its own; at s = beta the bound (24), wall (W) and the mass
gap stay OPEN.
