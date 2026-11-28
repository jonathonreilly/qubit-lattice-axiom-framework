# Check of library/gap-frameless-2d-astra.md (FINISH row 1140)

Status: complete (all six steps). Checker: Claude Opus 5.5. Written as the check went.

## Plan (six steps; each step appends its result here)

1. Read the file under check and `library/gap-council-brief.md` in full; record the setting and the list of statements.
2. Check the gauge-layer admissibility (R q = u q v^(-1)), the tile, its two ground states, the gap delta, the cost estimate and p.
3. Check the reflection (chessboard) bound (1) with the maximizer argument, the Peierls count (2), and the infinite-volume and pinned-square statements with the interpolation bound.
4. Check the moving-axis cost (3) and the 8-site diamagnetic counterexample (4), with the bridge expansion and 3 C_0 = t(1 - E z^2); small numeric guide only.
5. Check the reading of Durhuus-Frohlich and Cao-Nissim-Sheffield against open copies (new empty scratch directory), and the conditional area rate (5).
6. Verdict table and the RESULT line.

## Step 1. Setting and statements under check

Source under check: `library/gap-frameless-2d-astra.md`, 205 lines, read in full (row 1139, by gpt-6.2-astra).
Setting: `library/gap-council-brief.md`, 122 lines, read in full. The brief states the target (Jaffe-Witten, SU(2)),
the wall (W), and the rule that a numeric run may guide but never prove.

The model. A layer of a Wilson gauge theory, conditioned on its two horizontal faces, is an O(4) spin model on
unit quaternions with density proportional to exp(b sum_{xy} s_x . R_xy s_y). The note builds one face pair
(equal faces, a period-four "fold" background) and claims long-range order at zero field for all b >= b_*.
It also claims a finite-graph counterexample to O(4) diamagnetic domination, and a conditional area law.

Statements checked here, with the lines of the file under check:

| # | Statement | Lines |
|---|---|---|
| S1 | Gauge-layer admissibility, R q = u q v^(-1) | 37 |
| S2 | Tile, fold extension, two ground states | 46-53 |
| S3 | Local cost delta > 0, constants rho, a, b_*, and p | 55-70 |
| S4 | Chessboard bound (1), with the maximizer argument | 72-86 |
| S5 | Peierls count (2) and the correlation bound 41/64 | 88-99 |
| S6 | Infinite-volume form | 101 |
| S7 | Pinned squares and the interpolation bound | 103-112 |
| S8 | Moving-axis cost (3) and its scope | 116-137 |
| S9 | Eight-site counterexample (4): endpoint weights, bridge expansion, 3 C_0 = t(1 - E z^2) | 139-173 |
| S10 | Reading of Durhuus-Frohlich and Cao-Nissim-Sheffield | 3, 177-179 |
| S11 | Conditional area rate (5) | 181-195 |
| S12 | Dirichlet pins give the periodic hypothesis | 197 |
| S13 | The counterexample hits the charged hypothesis | 199 |
| S14 | Reading of the OpenAI O(4) paper (used in 35, 122, 135) | 35, 122, 135 |

S12-S14 are not named in the row, but they use the same interpolation or the same sources, so I check them too.
Lines 3-19 (repository search, plan) are GUIDE bookkeeping. I do not check them.

## Step 2. Admissibility, tile, ground states, delta and p (S1-S3)

**S1, line 37 (R q = u q v^(-1)). HOLDS.** Take the vertical link q_x from (x,k) to (x,k+1), and the face links
u_xy (bottom) and v_xy (top), oriented x to y. The mixed plaquette is U_p = u q_y v^(-1) q_x^(-1). For unit
quaternions (1/2) tr U_p = Re U_p. By cyclicity, Re(u q_y v^(-1) q_x^(-1)) = Re(q_x^(-1) u q_y v^(-1)).
Also Re(conj(a) X) = Re(a conj(X)) = a . X. So the term is s_x . R_xy s_y with R_xy q = u q v^(-1), as stated.
The map q -> u q v^(-1) is in SO(4). Reversing the bond replaces (u, v) by (u^(-1), v^(-1)), which gives
R_yx = R_xy^(-1). Equal faces u = v give Ad_u, which fixes 1. Horizontal plaquettes are constants once the
faces are fixed. Each vertical plaquette holds exactly two vertical links, so the layer law has zero site field.
Guide: a random test of Re(conj(q_x) u q_y v^(-1)) = q_x . (u q_y v^(-1)) = Re U_p gave error 3e-16.

**S2, lines 46-53 (tile and ground states). HOLDS.**
- (1+i)/sqrt2 = cos(pi/4) + i sin(pi/4), so Ad of it turns imaginary quaternions by pi/2 about i. By hand:
  A(j) = k, A(k) = -j, B(i) = -k, B(k) = i. Then AB(i) = A(-k) = j and BA(i) = B(i) = -k, as stated.
- The fold list phi(n) = 0,1,2,1 (n mod 4) has phi(2m + n) = phi(2m - n) for every m and n. Also
  |phi(n+1) - phi(n)| = 1. So every lattice edge maps to a template edge, the pulled-back transport is defined
  on every edge with R_yx = R_xy^(-1), and every reflection in a line of even coordinate preserves it.
  On a torus of side 2M this needs 4 | 2M, that is, M even. A power of two M >= 2 satisfies this.
- Q = {0,1,2}^2 has 12 edges: 4 interior (weight 1) and 8 on the perimeter (weight 1/2). An edge with an even
  coordinate across its direction lies on the sides of two tiles; other edges lie inside one tile. So the tile
  energies sum to the unit-bond energy. Also (1/2)|s_x - R s_y|^2 = 1 - s_x . R s_y for orthogonal R.
- The 10 identity bonds connect all nine sites (each top site has an identity bond down). Zero energy forces one
  common spin s with As = s and Bs = s. On R^4 the fixed spaces are span(1,i) and span(1,j). They meet in
  span(1). So the zeros are s = +1 and s = -1, and every bond is satisfied in both.
- A rotation by any 0 < theta < pi about i (or j) has the same fixed space span(1,i) (or span(1,j)). So the
  remark on general theta holds.
Guide: the quaternion products above were confirmed numerically (errors below 2e-15).

**S3, lines 55-70 (delta, rho, a, b_*, p). HOLDS.**
- U_+^9 union U_-^9 is open, so the bad set is closed in the compact (S^3)^9. It misses (1,...,1) and
  (-1,...,-1). E_Q is continuous and vanishes only there. So delta = min over the bad set is positive.
  A reflected tile is the template after relabelling its sites, and the bad event is relabelling-invariant.
- On the event that all 4M^2 spins lie within rho of 1: R fixes 1 and is orthogonal, so
  |R s_y - 1| = |s_y - 1| < rho and |s_x - R s_y| < 2 rho. The edge energy is below (1/2)(2 rho)^2 = 2 rho^2.
  With 8M^2 edges, Z >= a^(4M^2) exp(-16 b rho^2 M^2).
- If all M^2 tiles are bad, the energy is at least delta M^2, so the all-bad integral is at most
  exp(-b delta M^2).
- rho^2 <= delta/32 gives 16 rho^2 <= delta/2. Dividing: P(all bad) <= (a^(-4) exp(-b delta/2))^(M^2) = p^(M^2).
- For b >= b_*: b delta/2 >= 4 log(1/a) + 20 log 2, so p <= 2^(-20). Nothing depends on M.

Remark (not a correction). The note does not evaluate delta, so b_* is not located. One bad configuration
bounds delta from above: all nine spins equal to q = cos(t) + i sin(t) with |q - 1| = 1/4. Then A fixes q, and
the B bond has energy (1/2)(1/2)|q - Bq|^2 = (sin t)^2/2 = 63/2048. So delta <= 63/2048. b_* decreases as delta
grows, and with delta = 63/2048 the formula gives about 4.0e3. So b_* >= 4.0e3, far above the window 2.3-2.6.
The note claims nothing about the size of b_* (line 201 keeps the threshold OPEN), so no verdict changes.

## Step 3. Chessboard bound (1), Peierls count (2), infinite volume, pinned squares (S4-S7)

**S4, lines 72-86 (chessboard bound (1) and the maximizer). HOLDS.**
- Reflection. On the torus of side 2M, x_1 -> 4m - x_1 (mod 2M) fixes the lines x_1 = 2m and x_1 = 2m + M.
  Both have even coordinate because M is even, so the reflection preserves the background (S2). Each closed
  half is M/2 tile columns wide, and no tile crosses a seam, because seams lie on tile sides.
- Given the seam spins eta, the open halves are conditionally independent (nearest-neighbour bonds cannot
  join them). The half Hamiltonians map onto each other under the reflection theta, because theta fixes the
  seams pointwise and preserves the transports. So E[theta G | eta] = E[G | eta] for G on the left half.
  Hence E[F theta G] = E[f(eta) g(eta)] with f = E[F|eta], g = E[G|eta], a positive semidefinite form.
- Write S = S_L u S_R. Then P(S) = E[1_{S_L} theta 1_{theta S_R}] <= P(S_L u theta S_L)^(1/2)
  P(theta S_R u S_R)^(1/2). So P(S)^2 <= P(S_+) P(S_-) with |S_+| + |S_-| = 2|S|, as stated.
- Positivity: if every spin is near i, no spin lies in U_+ or U_- (|i - 1| = sqrt 2), so every tile is bad.
  This event has positive probability, so P(S) >= P(V) > 0 and D is finite on the finite family of sets.
- Maximizer. Let c = log P(V)/|V|. Then 2D(S) <= D(S_+) + D(S_-) <= 2 max D. So both doubled sets are
  maximizers. Start from one marked tile (an interval of length k = 1 in its row). Reflect in the line at an
  end of a marked interval of length k <= M/2 and keep the half that contains it (that half has M/2 tiles).
  The new maximizer marks 2k consecutive tiles of that row. Powers of two reach a full row. Then the same step
  in the other direction, applied to fully marked rows, reaches V. D(V) = 0 contradicts max D > 0.
  So P(S) <= P(V)^(|S|/|V|) <= p^|S| by S3. This is (1).

**S5, lines 88-99 (contours and (2)). HOLDS.**
- Each tile has four corners (coarse vertices). Going around them, the number of sign changes is even, so every
  dual vertex (tile) has even degree. An even-degree graph splits into edge-disjoint simple cycles.
- A tile on a drawn cycle has two corners of opposite sign of Re s. U_+ has Re > 31/32 and U_- has Re < -31/32,
  so the tile is bad. A specified simple cycle of length n has n distinct tiles, so probability <= p^n by (1).
- Long cycles: at most M^2 4^n rooted walks of length n; summing n >= ceil(M/2) gives
  M^2 (4p)^ceil(M/2) / (1 - 4p). Every non-contractible cycle has length >= M, so it is counted here.
- Short cycles (n < M/2): the displacement of the closed walk is a multiple of M in each coordinate and has size
  <= n/2 < M, so the lift is closed. Distinct lift vertices differ by less than M, so the lift is simple. Its
  interior is a disk inside a box of side below M, so it embeds in the torus.
- If tau_x != tau_y, a coarse path crosses the drawn edges an odd number of times. So it crosses some short
  cycle an odd number of times, and that cycle's disk holds exactly one of x, y. Coarse vertices never lie on
  dual edges. A short cycle around a given site has all vertices within n/2 of it (bounding rectangle of
  perimeter <= n), so (2n+3)^2 4^n bounds the number of such cycles. Both x and y give the factor 2.
- The case "x or y in no cap" makes an incident tile bad: at most 2p. Same cap and different caps exhaust the rest.
- Arithmetic: (2n+3)^2 <= 4^(n+1) for n >= 4 (121 <= 1024 at n = 4). The middle term is at most
  8 (16p)^4/(1 - 16p). With p <= 2^(-20): 2p <= 2^(-19) and the middle term is below 1e-18.
- On the same-cap event |s_x - s_y| < 1/2, so s_x . s_y = 1 - |s_x - s_y|^2/2 > 7/8, and
  (Re s_x)(Re s_y) > (31/32)^2 > 7/8. With failure probability eps < 1/8 each mean is at least
  (7/8)(1 - eps) - eps > (7/8)^2 - 1/8 = 41/64. Global negation is a symmetry at zero field, so the means vanish
  and the connected functions equal these. Every transport fixes 1, so it maps each cap to itself; the
  transported dot bound follows.

**S6, line 101 (infinite-volume form). HOLDS.** The periodized torus measures live on the compact space
(S^3)^(Z^2), so a subsequence converges weakly. The specification of a finite square is continuous in the
boundary spins. For a fixed square and fixed cylinder tests, the torus measure satisfies the same conditioning
identity once the supports fit in one period (no wrapped copy). The identity passes to the limit for continuous
cylinder tests and then, by a monotone class step, for all bounded exterior tests. The bounds 41/64 pass to the
limit (continuous local tests), and the limit is flip-symmetric.

**S7, lines 103-112 (pinned squares and the interpolation bound). HOLDS.**
- Given the ring of [-r,r]^2, the interior is independent of the exterior. So
  E[Re s_0 Re s_y] = E[m(eta) Re s_y] and 1/2 < E|m(eta)| <= max m. The maximum exists by continuity, and
  m(-eta) = -m(eta) by global negation. So the two pins eta and -eta move the centre mean by more than one.
- Interpolation: eta_w(t) = cos(pi t) eta_w + sin(pi t) xi_w with xi_w a unit vector orthogonal to eta_w. Speed pi.
  The derivative of the normalized mean is b times the sum over pin bonds of
  Cov(Re s_0, s_z . R_zw eta_w'(t)); pin-pin bonds are constants and cancel.
- Pin bonds: the ring has 2r - 1 non-corner sites per side, each with one bond inward: 4(2r - 1) bonds. Each
  inner endpoint z has max-norm r - 1. Since |m(-eta) - m(eta)| >= 1, some t and some bond give
  b pi |Cov(Re s_0, s_z . e)| >= 1/(4(2r - 1)) with e a unit vector. That is 1/(4 pi b (2r - 1)), as stated.
- A pin- and background-uniform bound C exp(-m (r - 1)) would contradict this for large r at fixed b.

## Step 4. Moving-axis cost (3) and the eight-site counterexample (4) (S8, S9)

**S8, lines 116-137 (moving-axis cost (3) and its scope). HOLDS.**
- Bond map: u e^(t f_y n_y) = e^(t f_y Ad_u n_y) u, so T_e becomes e^(t f_y Ad_u n_y) T_e e^(-t f_x n_x).
  For constant f the two generators are equal exactly when n_x = Ad_u n_y. Then the change is a conjugation and
  Re T_e is unchanged.
- In the basis (i, j, k): (1 - A)n = (n_j + n_k) j + (n_k - n_j) k, so |(1 - A)n|^2 = 2(n_j^2 + n_k^2).
  Likewise |(1 - B)n|^2 = 2(n_i^2 + n_k^2). The sum is 2(n_i^2 + n_j^2 + 2 n_k^2) = 2(1 + n_k^2) >= 2.
  |(1 - A^(-1))n| = |(1 - A)n|, so the loop orientation does not matter.
- The two upper plaquettes at z = (1,2) each contain one twisted bond and three identity bonds, so their
  holonomies are A^(+-1) and B^(+-1). Telescoping: n_z - H n_z is the sum of four transported bond differences
  D_e n. Cauchy-Schwarz gives |(1 - H) n_z|^2 <= 4 sum over the four sides. The bond (1,1)-(1,2) lies in both
  plaquettes. So 2 <= 8 sum_{e in Q} |D_e n|^2, and w_e >= 1/2 gives sum w_e |D_e n|^2 >= 1/8. Only |n_z| = 1
  is used.
- Hessian: at q = 1 every bond difference s_x - R s_y vanishes, so the second derivative of
  (1/2) w |s_x - R s_y|^2 is w |n_x - R n_y|^2 and does not see the accelerations.
- Scope (line 137): uniform mixing over this class is false by S5, so no argument can prove it. The OPEN item
  (the balance after averaging over dynamical faces) is stated as open.
- Guide: projected gradient descent over unit imaginary velocities on the tile (300 random starts) found a
  minimum of 0.3503 for sum w_e |D_e n|^2. The proved bound 1/8 is valid but not sharp.

**S9, lines 139-173 (eight-site counterexample (4)). HOLDS.**
- Graph: squares {0,1}^2 and {2,3}x{1,2}, bridge (1,1)-(2,1): 8 sites, 9 bonds. H = Ad_i fixes 1 and i and
  negates j and k. H = H^(-1), so the bond orientation does not matter.
- Endpoint weight: the cycle root-a-c-d-root gives K(x,a) K(a,c) K(c,d) K(d,Hx), and three integrations give
  K^4(x, Hx). The marginal of (s_x, s_y) is proportional to f(s_x) f(s_y) exp(t s_x . s_y). f is even because
  K(-u,-v) = K(u,v). For the flat square K^4(u,u) is constant by SO(4) invariance.
- Strict increase: K^2(u,z) = int exp(b (u+z).w) dsigma(w) = 2 I_1(b|u+z|)/(b|u+z|). Pairing w with -w gives
  an average of cosh, strictly increasing in |u+z|. The identity
  K^4(u,u) - K^4(u,-u) = (1/2) int [K^2(u,z) - K^2(-u,z)]^2 dsigma(z) holds because
  int K^2(-u,z)^2 = int K^2(u,z)^2. The integrand is positive wherever u.z != 0. Since u.Hu = 1 at u = 1 and
  -1 at u = j, f(1) > f(j).
- Bridge expansion: the linear terms vanish because int exp(t u.v) dsigma(v) does not depend on u, and int g = 0.
  The quadratic term is sum_k (t^k/k!) a_k with a_k = ||int g u^(tensor k)||^2 >= 0. k = 0 gives (int g)^2 = 0;
  odd k vanish because g is even. If all a_k = 0, then g is orthogonal to all polynomials; f (hence g) is a
  uniform limit of polynomials (Taylor series of exp(b u.v') with |v'| <= 2, or Stone-Weierstrass). So g = 0,
  which contradicts f(1) > f(j).
- 3 C_0 = t(1 - E_t z^2): the density of z = u.v is proportional to sqrt(1 - z^2). The derivative of
  e^(tz)(1 - z^2)^(3/2) is t e^(tz)(1 - z^2)^(3/2) - 3z e^(tz)(1 - z^2)^(1/2), and its integral over (-1,1) is
  zero. This gives the identity. Cross-check by a second route: C_0(t) = I_2(t)/I_1(t), and the recurrence
  I_1 - I_3 = (4/t) I_2 gives the same identity.
- E_t z^2 > 1/4: E_0 z^2 = 1/4 by symmetry of the four coordinates. The tilt of the even observable z^2 is by
  cosh(t|z|). Both z^2 and cosh(t|z|) increase strictly in |z|, so their covariance is positive (two independent
  copies). Hence 0 < C_0 < t/4.
- Final step: Z_f' - C_0 Z_f = sum (t^k/k!) a_k (k/t - C_0), since Z_1' = C_0 Z_1. For even k >= 2 and
  t <= sqrt 8: k/t - C_0 > 2/t - t/4 >= 0. One a_k is positive. So Z_f'/Z_f > C_0 = E_I > 0 at t = b <= sqrt 8.
  Note that f depends on b and t is the bridge coupling; the inequality holds for every t in (0, sqrt 8], so
  t = b is allowed.
- Guide (reduced two-spin integral, 2D Gauss-Legendre with 40 and 64 nodes, same digits). The flat value matches
  I_2(b)/I_1(b) to 12 digits. E_R - E_I = +2.5e-11 (b = 0.25), +1.2e-8 (0.5), +4.4e-6 (1), +7.1e-4 (2),
  +1.63e-3 (2.3), +3.12e-3 (2.6), +4.66e-3 (sqrt 8), +1.1e-2 (3.5), +2.4e-2 (5), +2.8e-2 (8). The small-b
  growth is about b^9, as the lowest term (k = 2, g of order b^4) predicts. The values above sqrt 8 are outside
  the proved range and are a guide only.
- Guide (independent data paths). f(1)/f(j) from a 1D quadrature of K^2 matches the character-sum value to six
  digits (1.02699 at b = 1, 1.81421 at 2.6, 12.4956 at 5). Metropolis on the full eight-site graph, with no
  reduction, at b = 5: flat 0.7185 +- 0.0010 (reduced 0.7193), twisted 0.7436 +- 0.0008 (reduced 0.7431).
## Step 5. Sources, conditional area rate, and the two hypothesis remarks (S10-S13)

Sources read (open copies, read through the web-fetch tool; the files stay in the session scratch area and are not
committed): Cao-Nissim-Sheffield, arXiv:2509.04688v2, 8 pages, read in full. Durhuus-Frohlich, IHES preprint
P/79/302, 89 scanned pages; I rendered and read the printed pages 11, 12, 16, 17, 18, 39 and 72 as images, and
searched the OCR layer of the rest. Printed page n is PDF page n + 1.

**S10, lines 3 and 177-179 (reading of DF and CNS). HOLDS.**
- DF (1.19), printed p. 11: the slab action is -sum Re chi(g_i^(-1) b_ij g_j t_ij^(-1)), and G x G acts by
  g -> b g t^(-1). For the SU(2) fundamental character this is 2 s_i . (b s_j t^(-1)): the two-sided transport
  of S1.
- DF Theorem 1.1, printed p. 12: for a class of boundary conditions "(including periodic and free)",
  part 1) bounds zeta(b,t) = Z(b,t)/Z by zeta(1,1) = 1 ("diamagnetic inequality"). It is a ratio of partition
  functions, as the note says.
- DF (1.35), printed p. 16: in the thermodynamic limit, |< U^q(g_0)^(-1)_mn U^q(g_j)_kl >(b,t)| <= e^(-V^q(j)),
  with V^q(j) -> +infinity, "uniformly in (b,t)" (p. 17). This is an absolute expectation of one inverse and one
  direct entry, uniform over both face fields, as stated.
- DF Theorem 1.2, printed p. 17: it assumes (1.35) uniformly in (b,t) and boundary conditions with
  zeta(b,t) >= 0 for all (b,t). The next paragraph says V^q(j) about m|j| gives a linearly rising potential.
- DF Theorem 1.3, printed p. 18: a faithful action character; then the one-point vanishing (1.39) for all
  (b,t) is equivalent to U^q being non-trivial on the centre. As the note says.
- DF printed p. 39 (Section 3): they write that one way forward "would be to prove" |<chi^q(g_0 g_x^(-1))>(b,t)|
  <= <chi^q(g_0 g_x^(-1))>(1,1) for all (b,t); it holds for abelian G; Section 7 argues that this is "hardly the
  case" for non-abelian G. DF printed p. 72 (Section 7): for SU(2) in a Gaussian limit, "the clustering ... is
  worse" for some external fields. So line 3 and line 177 report DF correctly. For SU(2),
  chi(q_x q_y^(-1)) = 2 s_x . s_y, so (4) is a compact, finite-graph test of exactly the p. 39 inequality.
  (The eight vertices induce exactly the nine bonds in Z^2, so the graph is a free-boundary region of Z^2.)
- CNS Section 2 (pp. 3-4): Definition 2.1 takes U(N)-valued boundary fields A, B and the action
  N beta sum Re Tr(Q_x A_e Q_y^(-1) B_e^(-1)) on the slice Lambda^(d-1) of the torus. Remark 2.2 says the U(N)
  values serve the U(N) extension and are "not needed" for SU(N), SO(2N). Theorem 2.3 asks
  |Cov_{A,B}(f_x^{i1 j1}, g_y^{i2 j2})| <= C_1 e^(-C_2 d(x,y)) for direct entries f and inverse entries g, with
  C_1, C_2 depending only on G, d, beta ("in particular not on A, B"). As stated in line 179.
- Convention: with N = 2, N beta Re Tr U_p = 4 beta (Re Tr U_p / 2), so b = 4 beta. CNS's bond
  Re Tr(Q_x A Q_y^(-1) B^(-1)) is the note's form after Q -> Q^(-1), which swaps direct and inverse entries; the
  set of hypotheses over all pairs (x, y) is unchanged.

**S11, lines 181-195 (conditional area rate (5)). HOLDS.**
- Lemma R in `library/gap-arealaw-opus.md` Section 4.2 states |E[W | H]| <= prod_k sup_O |E[q_(x,k) . O q_(y,k)]|
  with T_k : X -> conj(q_(x,k)) X q_(y,k). The note uses exactly this.
- By hand: with Q_l = H_b V_y conj(H_t) conj(V_x), W = Re Q_l = < T_(T-1) ... T_0 (H_b), H_t >. Given the
  horizontal links, slabs are independent (each vertical plaquette holds two vertical links of one slab), so
  E[W | H] = < E T_(T-1) ... E T_0 H_b, H_t >.
- <Y, conj(q) X q'> = Re(Y conj(q') conj(X) q) = <q Y, X q'> = q . (X q' Y^(-1)), and q' -> X q' Y^(-1) is in SO(4).
- Four coordinates: q_x . O q_y = sum_a (q_x . e_a)(q_y . O^T e_a). Centre symmetry q -> -q of the zero-field
  unpinned layer kills the one-point means. So ||E T_k|| <= 4 C e^(-mR) under the hypothesis.
- So |<W>| <= (4C)^T e^(-mRT); exchanging the roles of the two directions gives (4C)^R e^(-mRT). Hence (5)
  with K = max(1, 4C). If max(R,T) >= 2 log K / m then min(R,T) log K <= m R T / 2. Otherwise RT < (2 log K/m)^2
  and the trivial bound 1 is at most exp(2 (log K)^2/m) e^(-mRT/2).
- Distances: R <= L/2 makes the periodic distance R; T <= L/2 gives T distinct slabs. This is a conditional
  statement: it assumes (P) on the actual layers, as the label says.

**S12, line 197 (Dirichlet pins give the periodic hypothesis). HOLDS.** With max-norm separation R, the ring of
radius r = R - 1 around x has side 2R - 1 < L, so it does not wrap; y lies outside it. Given the ring, the
inside is the pinned-box law and is independent of y. The interpolation of S7 with a pin-uniform bound
C e^(-m d) on each of the 4(2r - 1) pin bonds (each term at most b pi C e^(-m(r-1))) gives
2|m_l(eta)| <= 4(2r - 1) b pi C e^(-m(r-1)), that is |m_l| <= (1/2) pi b 4(2r - 1) C e^(-m(r-1)), as stated.
Then |Cov(l(s_x), l'(s_y))| <= sup |m_l| <= C' e^(-mR/2). Small R is absorbed into C'.

**S13, line 199 (the counterexample hits the charged hypothesis). HOLDS.** For q in SU(2), Re q = Tr q / 2 and
Re q^(-1) = Re q. So (Tr q_x/2)(Tr q_y^(-1)/2) = (1/4) sum_{a,b} (q_x)_aa (q_y^(-1))_bb, and the covariance is
the mean of four direct-inverse diagonal covariances of the CNS form. One exceeds 1/2 in modulus. The fold faces
are honest face pairs: u = v = (1+i)/sqrt 2 or (1+j)/sqrt 2 or 1 on each bond, with u_yx = u_xy^(-1). On a fixed
finite torus the covariance is continuous in the faces, and the Wilson law of two adjacent planes has a positive
continuous density. So the failure also holds for an essential supremum. This is at b >= b_* only (S3 remark:
b_* >= 4.0e3); the note says so in lines 41 and 201.

**S14, lines 35, 122, 135 (reading of the OpenAI O(4) paper). HOLDS.** Read from the text layer of the PDF at
commit 4eaee8754 (102 pages); page 12 also checked as an image.
- p. 12, Theorem 3.1: Xi(beta) = exp[pi beta + C sqrt((1 + beta) log(2 + beta))]; the covariance bound is for
  unpinned rectangular tori with sides at least C Xi(beta), couplings 0 <= beta_e <= beta in the untwisted density
  exp(sum beta_e q_x . q_y), and "every unpinned free subgraph". As line 35 says.
- p. 13: the local class has t_e + s_e = q_y U_e q_x^(-1) with U_e "any fixed unit quaternion"; the stiffness part
  "allows arbitrary signed couplings and fixed right twists", and only the last part "requires nonnegative
  untwisted couplings". (3.6) uses one imaginary unit a at every site and gives D_f A = sum w_e (s_e . a)(f_y - f_x)
  and D_f^2 A = sum w_e t_e (f_y - f_x)^2, so a constant profile costs nothing (line 135). (3.7) is
  D_eta s_e = t_e(eta_y - eta_x) + (eta_y + eta_x) x s_e, the bracket; (3.8) on p. 14 carries it.
- p. 25, (3.52): Var J(A) >= c_sh min(v, 1) in the short regime, where v is the step's response parameter.
- Line 122 is a reading remark: with a left twist the two generators across a bond differ (S8), so the
  common-axis gradient formula (3.6) does not apply as written. This is accurate.

**Addendum to S9 (Monte Carlo guide at b = 2.6).** Metropolis on the full eight-site graph, two independent seed
sets of 40 x 1e5 sweeps each. Flat: 0.52084 +- 0.00029 and 0.51987 +- 0.00027; pooled 0.52036 +- 0.0002, exact
I_2/I_1 = 0.52034. Twisted: 0.52398 +- 0.00025 and 0.52304 +- 0.00025; pooled 0.52351 +- 0.0002, reduced value
0.52346. Pooled difference 0.00315 +- 0.0003 against 0.00312 from the reduced integral. Guide only; the proof
of (4) is analytic and checked above.

## Step 6. Verdicts

Checker: Claude Opus 5.5 (Anthropic), by hand, one pass. The author of row 1139 is gpt-6.2-astra, so this is a
cross-provider check. It is one check, not an audit. Numeric runs were guides only; no verdict rests on them.

| # | Statement | Lines | Verdict |
|---|---|---|---|
| S1 | Gauge-layer admissibility, R q = u q v^(-1), equal faces give Ad_u | 37 | HOLDS |
| S2 | Tile, A and B quarter turns, AB(i) = j, BA(i) = -k, fold extension, zeros +1 and -1 only | 46-53 | HOLDS |
| S3 | delta > 0 by compactness; Z >= a^(4M^2) e^(-16 b rho^2 M^2); P(all bad) <= p^(M^2); p <= 2^(-20) for b >= b_* | 55-70 | HOLDS |
| S4 | Chessboard bound (1), site reflections, P(S)^2 <= P(S_+) P(S_-), dyadic maximizer argument | 72-86 | HOLDS |
| S5 | Peierls count (2), long and short cycles, (2n+3)^2 4^n, the bound 41/64 > 1/2 | 88-99 | HOLDS |
| S6 | Infinite-volume Gibbs state with the same bound | 101 | HOLDS |
| S7 | Pinned squares: centre means differ by more than one; interpolation bound 1/[4 pi b (2r - 1)] | 103-112 | HOLDS |
| S8 | Moving-axis cost (3): 2(n_i^2 + n_j^2 + 2 n_k^2) >= 2, sum w_e |D_e n|^2 >= 1/8, Hessian; scope | 116-137 | HOLDS |
| S9 | Eight-site counterexample (4) for 0 < b <= sqrt 8: endpoint weights, bridge expansion, 3 C_0 = t(1 - E z^2) | 139-173 | HOLDS |
| S10 | Reading of Durhuus-Frohlich (pp. 11, 12, 16-18, 39, 72) and Cao-Nissim-Sheffield (Section 2) | 3, 177-179 | HOLDS |
| S11 | Conditional area rate (5) via Lemma R | 181-195 | HOLDS |
| S12 | Dirichlet pins give the periodic hypothesis | 197 | HOLDS |
| S13 | The counterexample meets the charged (entry) hypothesis, also as an essential supremum | 199 | HOLDS |
| S14 | Reading of the OpenAI O(4) paper (Theorem 3.1, local class, (3.6)-(3.8), (3.52)) | 35, 122, 135 | HOLDS |

No statement needs a correction. No statement fails.

Remarks (no verdict changes):
- b_* is not evaluated in the note. One explicit bad tile gives delta <= 63/2048 and hence b_* >= 4.0e3. So (C) is a
  statement far above the window 2.3-2.6. The note says the ordering threshold is OPEN (line 201), so it does not
  overclaim. Only (4) reaches the window, and (4) is a finite-graph comparison, not a mixing statement.
- The eight vertices of (4) induce exactly its nine bonds in Z^2, so (4) is a free-boundary region of Z^2. It
  answers, on a compact finite graph, the inequality that Durhuus and Frohlich ask about on printed p. 39 and
  doubt on printed p. 72. The note credits them for that warning (lines 3, 177).
- Not checked: lines 3-19 (repository search and plan, GUIDE), and the OPEN items in lines 25 and 201, which make
  no claim. Line 25 agrees with `library/gap-council-brief.md` Section 2 on (W).

Guide runs (scratch only, not in the repository): quaternion identities; tile velocity minimum 0.3503 >= 1/8; the
reduced eight-site integral at twelve couplings (E_R - E_I > 0 at every tested b, +3.12e-3 at b = 2.6); an
independent K^2 quadrature of f(1)/f(j); Metropolis on the full graph at b = 2.6 and 5. All agree with the note.

RESULT: Row 1140 (Claude Opus 5.5, by hand, cross-provider check of row 1139 by gpt-6.2-astra): all 14 statements of `library/gap-frameless-2d-astra.md` HOLD, none needs a correction and none FAILS: gauge-layer admissibility, the fold tile with zeros +1 and -1 and delta > 0, p <= 2^-20 for b >= b_*, the chessboard bound (1) with its dyadic maximizer, the Peierls bound (2) and 41/64, the infinite-volume and pinned-square statements with the interpolation bound 1/[4 pi b (2r - 1)], the moving-axis cost (3), the eight-site counterexample (4) for 0 < b <= sqrt 8 (so on 2.3-2.6), the conditional area rate (5), the Dirichlet-to-periodic step, the charged-hypothesis remark, and the readings of Durhuus-Frohlich (printed pp. 11, 12, 16-18, 39, 72), Cao-Nissim-Sheffield (Section 2) and OpenAI (pp. 12-14, 25), each checked against the primary text; remark: b_* >= 4.0e3 from one explicit bad tile, so (C) lies far above the window, as the note's own OPEN line says; numerics (guide only) agree, with E_R - E_I = +3.1e-3 at b = 2.6 by quadrature and by Monte Carlo on the full graph; one check, not an audit; the wall (W) is not moved.
