# Check of row 1328 (gap-solve41-astra62.md) — FINISH row 1329

Checker: Claude Opus 5.5, by hand, line by line.
File checked: `library/gap-solve41-astra62.md` (row 1328, by gpt-6.2-astra).
Inputs read: rows 1323 and 1325 (`gap-solve39-astra62.md`, `gap-solve40-astra62.md`)
and their checks, row 1231 (6) with check row 1235, Theorem ZD-c in `gap-phys-seed.md`.
Numeric runs, if any, only guide. They are not proof steps.

Inputs used: row 1325 (12), (24)-(26) and its check; row 1151 (21)-(22a)
(dissemination and pressure slope) and its check; row 1231 (3)-(6) and check
row 1235; Theorem ZD-c. The chessboard method follows Sussman and Alpoge
(outline lines 2885-2912). The pressure slope (22a) of row 1151 rests on
Sourav Chatterjee's weak-coupling free-energy comparison.

Notation. Line numbers L refer to `gap-solve41-astra62.md`. I write
U = K/||K||, N for the number of packets in the filtered set, and
E(B,q) = prod_b [1 + (q-1) e^{-D m_b h(q)}] - 1 as in the file.

## 1. Fixing one bit per eight black sites (claim 1)

### 1a. Positive packet expansion (1), L19-24: HOLDS

- n even, so the spatial torus is bipartite. Each edge has one black and one
  white end. So the stars b* of distinct black vertices are disjoint, and
  m_b = 6|b|. Checked.
- The temporal link at a black vertex x on a cut lies in exactly the six
  temporal plaquettes of that cut over the edges at x. No spatial plaquette
  and no other cut contains it. The map U_0(x) -> -U_0(x) preserves Haar
  and sends each of these w_p to -w_p. So it reverses Y_b and fixes all
  other weights. Flips on different packets or cuts commute. Checked.
- Averaging over the group of flips turns prod_b e^{beta Y_b} into
  prod_b cosh(beta Y_b) in any integral of a flip-invariant integrand.
  Expanding each cosh gives the joint law (1): the J_b are conditionally
  independent given the field, with the stated masses. Checked.
- Positivity. Y_b^{2j} is a positive power of a sum of normalized
  fundamental characters on the product group of b*. Its expansion has
  nonnegative coefficients on characters of tensor representations. So
  convolution by it is a positive operator, and by centrality it commutes
  with left and right translations, hence with P. The pointwise value is
  >= 0, and so is its vertex average. Sums over residue classes keep both
  properties. Checked.

### 1b. The weakening bound (2), L26-34: HOLDS

- Reduction. After the flip average, Z(u) = int prod_b cosh((1-u_b) beta
  Y_b) x (rest). cosh(t y) increases in t >= 0. So Z(u) <= Z(h) with
  h_b = min(u_b, 1/3). Then Z(h)/Z(0) = e^{-beta sum_b m_b h_b}
  E_beta exp(beta sum_p h_p (1 - w_p)). Checked.
- Hölder over the three temporal orientations, exponent 3, gives tilts
  v_p = 3 h_p <= 1. So every layer coupling stays >= 0. Checked.
- Variable profiles. I re-derived the trace-Hölder proof of row 1151 (21)
  with an arbitrary profile. Along an axis in the plaquette plane the
  marked plaquettes sit in the crossing convolution: layer M C_i P M. Along
  an axis outside it they sit in the slice weight: C^{1/2} P M_i^2 C^{1/2}.
  Both are positive, also at coupling 0. log Tr prod_t T_t <=
  (1/N) sum_t log Tr T_t^N. Each replication keeps the pattern constant
  along the axes already done. After four axes each site carries one
  uniform pattern. With one plaquette of the orientation per site this
  gives log E exp(sum v_p beta(1-w_p)) <= sum_p [p(v_p) - p(0)]. Checked.
- Convexity of p (a log moment generating function) gives
  p(v) - p(0) <= v[p(1) - p(0)] on [0,1]. p(1) <= 0 since every weight
  e^{-beta(1-w)} <= 1 and Haar is normalized. Checked.
- Cap bound. The Haar ball of radius beta^{-1/2} has mass >= c beta^{-3/2}
  (radial density (2/pi) sin^2). Four links each within that angle give a
  plaquette angle <= 4 beta^{-1/2}, so beta(1-w) <= 8. With four links and
  six plaquettes per site, p(0) >= 4 log c - 6 log beta - 48
  >= -C log(2+beta) for beta >= 1. Checked.
- Assembly: log E <= sum_p h_p C log(2+beta) = C log(2+beta) sum_b m_b h_b.
  This is (2) with D_beta = beta - C log(2+beta). Checked.

### 1c. Residue filtering (3), L36-50: HOLDS

- q^{|B|} 1{J = r mod q} = sum_k prod_b e^{2 pi i k_b (J_b - r_b)/q}.
  Given the field, E[e^{2 pi i k J_b/q}] = cosh(e^{i pi k/q} lambda_b)/
  cosh(lambda_b), since (e^{i pi k/q} lambda)^{2j} = lambda^{2j}
  e^{2 pi i k j/q}. Checked.
- |cosh(z lambda)| <= cosh(lambda |Re z|) for |z| = 1. For k != 0 mod q,
  |cos(pi k/q)| <= cos(pi/q). So 1 - c_k >= 1 - cos(pi/q) and
  min(1 - c_k, 1/3) >= h(q). Checked.
- The bound prod_b cosh(c_b beta Y_b)/cosh(beta Y_b) is flip invariant. Its
  E_beta is Z((1 - c_b)_b)/Z(0) by the flip average. (2) bounds it by
  prod e^{-D m_b h(q)}. Summing over k != 0 gives exactly E(B,q). F enters
  only through ||F||_inf, so F may be any bounded function of the field.
  Needs D_beta > 0, which is stated. Checked.

### 1d. Overlap after fixing labels (4), L52-59: HOLDS

- Tr(rho_r rho_s) = Tr(B C_r B C_s)/(Z_1(r) Z_1(s)) and
  Tr rho^2 = Z_2/Z_1^2. With Pr_T(r) = Z_1(r)/Z_1 and
  Pr_{2T}(r,s) = Tr(B C_r B C_s)/Z_2 the first equality follows. Checked.
- (3) at F = 1 on the T-torus (set B) and on the 2T-torus (set B u B) puts
  each factor within E_2 of 1. For E_2 < 1/4 the ratio is 1 + O(E_2) with an
  absolute constant. Checked.
- rho = sum_s Pr_T(s) rho_s since C = sum_s C_s. Expanding
  ||rho_r - rho||_2^2 = Tr rho_r^2 - 2 Tr rho_r rho + Tr rho^2 gives
  O(E_2) Tr rho^2. Checked.

### 1e. The eight-site example, L61: HOLDS

- 4 | n lets the 2^3 cells pair along axis one. Each cell has four black
  sites. So packets of eight, m_b = 48, V/16 packets per cut. Checked.
- q = 2: h(2) = min(1, 1/3) = 1/3, so each factor is 1 + e^{-16 D_beta}.
  With beta/log n -> b_*, D_beta = beta(1 - o(1)), and
  E <= exp(N e^{-16 D}) - 1 = O(N n^{-16 b_* + o(1)}). One or two cuts:
  N = O(n^3). All T = O(n) cuts: N = O(n^4). Checked.
- b_* = 11/(3 pi^2) is the one-loop value for SU(2) with beta = 4/g^2
  (b_0 = 11/(24 pi^2), 1/g^2 = 2 b_0 log(1/a)). 16 b_* = 176/(3 pi^2).
  This exceeds 4 iff pi^2 < 44/3. The hexagon bound pi < 2 sqrt 3 gives
  pi^2 < 12 < 44/3. Checked. The file correctly says that a continuum
  trajectory must still be shown to have this bare schedule.

### 1f. Operator comparison (5), L65-77: HOLDS

- Roots of unity give q^N C_r = sum_k (phase) C^{(k)}, where C^{(k)} has
  coupling beta e^{i pi k_b/q} on packet b. The flip average removes odd
  powers, so cosh and exp give the same kernel. k = 0 gives K. Checked.
- |cosh(z_b beta Y_b)| <= cosh(c_b beta Y_b) pointwise inside the
  temporal-link integral. Undoing the flip average gives the kernel of the
  real transfer L_k. So |kernel of term k| <= kernel of L_k, and
  |<f, A g>| <= <|f|, L_k |g|> gives ||term k|| <= ||L_k||. Checked.
- Tr L_k^t / Tr K^t = Z(u)/Z(0) on the period-t torus with every cut
  weakened by u_b = 1 - c_b in [0,1]. (2) gives the displayed bound. For a
  positive trace-class A, (Tr A^t)^{1/t} -> ||A||. So
  ||L_k||/||K|| <= prod_{k_b != 0} e^{-D m_b h(q)}. Summing over k != 0
  gives E_1. No dimension factor enters. Checked.

### 1g. Individual levels (6), L79-83: HOLDS

- Weyl: |lambda_i(K~_r) - lambda_i(K)| <= E_1 ||K||. Top of K~_r is at
  least (1 - E_1)||K||. Then |a/A - b/B| <= |a-b|/A + (b/B)|A-B|/A
  <= 2 E_1/(1 - E_1). Checked.
- Energies. If a level has energy <= C_0 in physical units, u_i >=
  e^{-a C_0} -> 1. With E_1 = o(a) the partner eigenvalue is also >= 1/2
  eventually. log is 2-Lipschitz on [1/2,1]. So the energies differ by
  2 o(a)/a = o(1), uniformly over such levels. Checked.
- Eight-site example: E_1 = n^{3 - 16 b_* + o(1)} and a = L/n. E_1 = o(a)
  needs 16 b_* > 4. Checked.

### 1h. Heat trace (7), L85-95: HOLDS

- Tr K~_r^T / Tr K^T = q^{N T} Pr_T(J = r on every cut), so (3) on all T
  cuts gives |ratio - 1| <= E_all directly. Checked.
- ||K~_r|| lies in [(1 - E_1)||K||, (1 + E_1)||K||] by (5). The factor
  (||K||/||K~_r||)^T is 1 + o(1) when T E_1 -> 0. Checked.
- Eight-site example at T = O(n): E_all = O(n^{4 - 16 b_*}) and
  T E_1 = O(n^{4 - 16 b_*}). Both -> 0. Checked.

Verdict on claim 1: HOLDS. The bit-fixed transfer K_r has
Tr(K_r/||K_r||)^T = (1 + o(1)) Tr U^T at T = O(n), and every level of
bounded physical energy moves by o(1), on beta/log n -> b_* with 4 | n.
Scope note: this is a relative bound on 1 + S, so it controls the thermal
sum S = Tr U^T - 1 only to absolute o(1) times Tr U^T. That is enough to
move a seed between K and K_r at q = 2, in either direction, but no seed
for K_r at q = 2 is proved.

## 2. The altered-transfer seed (8), L99-108: HOLDS

- Zero residue mod q means 2 J_b in {0, s, 2s, ...} with s = 2q. After the
  flip average the packet weight is F_s(beta Y_b) = sum_j (beta Y_b)^{sj}/
  (sj)!. Checked.
- Factorial bound. log k! >= int_1^k log x dx = k log k - k + 1, so
  k! >= (k/e)^k. With |beta Y_b| <= beta m_b <= A:
  A^{sj}/(sj)! <= (eA/(sj))^{sj} <= (eA/s)^{sj}. The sum over j >= 1 is at
  most d. s even makes every term >= 0, so 1 <= F_s <= 1 + d. Checked.
- The product over the N packets lies in [1, 1 + d_0]. This needs the
  packets to cover every black vertex of the cut, which the partition
  gives. The vertex average keeps the bounds. Checked.
- The constant term is |1><1|, so in the sandwich it is |v><v|, v = M1
  (gauge invariant). The remainder M R M is positive by 1a. Its trace is
  int M^2 R(X,X) <= d_0 ||v||^2. lambda_0(K_0) >= <v,K_0 v>/||v||^2
  >= ||v||^2. So sum_{i>=1} u_i(0) <= (Tr K_0 - lambda_0)/lambda_0 <= d_0,
  and sum_{i>=1} u_i^t <= (sum u_i)^t <= d_0^t. Checked.
- d_0 = o(1). With s >= 2eA + 10 log n, eA/s <= 1/2, so
  (eA/s)^s <= 2^{-s} <= n^{-10 log 2} = n^{-6.93}. d <= 2 n^{-6.93}, and
  N d = O(n^{-3.9}) -> 0, so d_0 <= e^{N d} - 1 -> 0. s even makes
  q = s/2 an integer. This holds for every beta; no schedule is needed.
  Checked.
- One filtered cut per period. Tr(B C_0) <= (1 + d_0) <1,B1> since B has a
  nonnegative kernel. Tr(B C_0 B C_0) >= <1,B1>^2 from the pointwise lower
  bound 1. The lower bound 0 is purity <= 1. So
  0 <= 2 log Z_1(0) - log Z_2(0,0) <= 2 log(1 + d_0). Checked.

Verdict: HOLDS. The seed is for the altered transfer K_0 at the large
q = s/2 of order 130 beta + 5 log n. It says nothing about K. Notation
remark: K_0 here (large q) and rho_0 in L192 (q = 2) are different
objects.

## 3. Obstruction and the single-cut test (claim 3)

### 3a. Operator comparison cannot reach (8), L110: HOLDS

- I read row 1231 (3)-(6) and its check in row 1235 (HOLDS there). Row
  1231 assumes beta -> infinity, beta <= B log n. For 0 < delta < 1/192 and
  t = floor(beta^delta), the centered plaquette vector has spectral weight
  of order t^{-8} in every band c/t < E < d/t, with limit coefficient
  3(d^8 - c^8)/(2 pi^4 8!) > 0. Take c = 1, d = 2. The vector is orthogonal
  to the simple vacuum. So U has an eigenvalue in [e^{-2/t}, e^{-1/t}] off
  the vacuum, and u_1 >= e^{-2/t} -> 1. Checked.
- u_1(0) <= sum_{i>=1} u_i(0) <= d_0 -> 0 by (8). Checked.
- Weyl gives ||K/||K|| - K_0/||K_0|| || >= u_1 - u_1(0) -> 1. Both
  operators lie in [0, I], so the distance is <= 1. Checked.
- Free rescaling. For any c > 0 put delta = ||c K_0 - K||/||K||. Weyl at the
  top and second levels gives u_1 <= u_1(0)(1 + delta) + delta, so
  delta >= (u_1 - u_1(0))/(1 + u_1(0)) -> 1. So no bound of type (5) with
  small E_1 holds at this q. This is consistent with (3): h(q) is of order
  q^{-2} there. Checked.
- The closing remark is right. The witness has lattice energy <= 2/t -> 0
  but physical energy of order n beta^{-delta}/L -> infinity at fixed L.
  It gives no physical upper bound on the mass.

### 3b. The single-cut local test, L112: HOLDS

- Given everything except the |b| black temporal links of one packet, those
  links enter only the packet weight F_s(beta Y_b). So their joint density
  against product Haar is F_s/int F_s, in [1/(1+d), 1+d]. Checked.
- Under Haar, w_p is one coordinate of a uniform point of S^3, so
  E w_p^2 = 1/4. Since 0 <= w_p^2 <= 1, the filtered value differs from 1/4
  by at most d, for every exterior. w_p^2 is flip invariant, so the same
  holds in the history labelled by (1). Checked.
- Unaltered torus. The single-orientation bound at v = 1 gives
  log E exp(beta sum_o (1-w)) <= N_o C log(2+beta). Jensen and translation
  invariance in that orientation give E(1 - w_p) <= C log(2+beta)/beta.
  So E w_p^2 >= (E w_p)^2 -> 1. Checked.
- So strong filtering at one cut moves a bounded gauge-invariant local
  observable by 3/4 + o(1). Checked. (The bound C log beta/beta is weaker
  than the 3/(4 beta) slope of row 1151 (22a); it suffices here.)

## 4. Identity (12) and the reduction to Theorem ZD-c (claim 4)

### 4a. Identity (12), L184-190: HOLDS

- Here the packet set must cover the whole cut, so that "every degree zero"
  is the constant kernel. The file uses it so ("erasing the sole cut").
- J = 0 implies r = 0 at q = 2. So p_T = Pr_T(J = 0)/Pr_T(r = 0) and
  p_{2T}^{(2)} = Pr_{2T}(J = 0, J = 0)/Pr_{2T}(r = 0, r = 0). Checked.
- Pr_T(J = 0) = <1,B1>/Z_1, because erasing the cut leaves the kernel 1.
  Pr_{2T}(J = 0, J = 0) = <1,B1>^2/Z_2. Their ratio is Z_1^2/Z_2 = e^Psi.
  This is the first equality. Checked.
- (3) at F = 1 gives Pr_T(r = 0) = 2^{-N}(1 + O(E_2)) and
  Pr_{2T}(0,0) = 2^{-2N}(1 + O(E_2)). This is the second equality. Checked.

Restatement. The first equality of (12) is row 1325 (26) at k = l = 0.
There A_0 = B^{1/2}|1><1|B^{1/2} has rank one, so R_00 = 1 and (26) reads
P_{2T}(0,0)/P_T(0)^2 = e^Psi. Row 1325 (L154) already attributes this
rare-event form of the purity to row 1151 (25)-(26). The only new input in
(12) is the residue normalization from (3). So (12) restates an earlier
row, conditioned on the residues.

### 4b. The ratio bound suffices for Theorem ZD-c, L192: HOLDS

I read Theorem ZD-c and the definition of S(k; B) and t(2) = 1/1650 in
`gap-phys-seed.md`.

- Constants. If limsup_j p_{2T}^{(2)}/p_T^2 < 1651/1650 and E_2 -> 0, then
  (12) gives limsup e^Psi < 1651/1650. K >= 0, so U has eigenvalues in
  [0,1], Tr U^{2T} <= Tr U^T, and Psi >= log Tr U^T. Hence
  limsup (Tr U^T - 1) <= limsup e^Psi - 1 < 1/1650. With n = L/a_j and
  T = n/2 this is S_j(L/(2 a_j); (L/a_j)^3) below the two-stage threshold.
  That is (PHYS-SEED) of ZD-c. Strictness survives each step. Checked.
- The purity form. (4) at r = s = 0 gives Tr rho_0^2 = e^{-Psi}(1 + O(E_2)).
  So liminf Tr rho_0^2 > 1650/1651 is the same as limsup e^Psi < 1651/1650
  when E_2 -> 0. Checked.
- Sizes. ZD-c needs L in P = {2^i l_1} with l_1/(4 a_j) an integer >= 3.
  Then 4 | n, which the eight-site packets also need. Checked.
- Coupling range. Unlike row 1325 (24), nothing in (3), (4) or (12) needs
  beta <= B_0 log n or the rectangle shape. The only coupling hypothesis is
  D_beta > 0 and E_2 -> 0, and L192 states it ("On schedules with
  E_2 -> 0"). ZD-c has no coupling hypothesis, so this one is an added
  hypothesis on the trajectory, and it is stated. No hypothesis is missing.
  Clarification, not a correction: E_2 depends on the packet partition.
  For the eight-site partition, E_2 -> 0 is 16 D_{beta_j} - 3 log n_j ->
  infinity, so beta_j >= (3/16 + o(1)) log n_j. The one-loop schedule
  beta/log n -> 11/(3 pi^2) = 0.3715 meets it. Single-site packets
  (m_b = 6) would need beta >= (3/2 + o(1)) log n, which that schedule does
  not meet. The statement should name the partition.

Verdict on claim 4: (12) HOLDS; the sufficiency HOLDS with the stated
schedule hypothesis; no coupling-range hypothesis is missing. Neither
inequality is proved, as the file says.

## 5. Everything else

### 5a. Trace-norm bound at q = 2, L116-121: HOLDS

The statement follows from 5b and 5c. For the eight-site packets
E'_1 = O(n^3 e^{-16 beta + O(log beta)}) -> 0. |Tr(rho_r A) - Tr(rho A)|
<= ||A|| ||rho_r - rho||_1, uniformly in r, so the bound covers projectors
chosen after r. Checked.

### 5b. The coefficient bound for e^{i beta w}, L123-127: HOLDS

- The scalar of a central convolution on the spin of dimension d is
  (1/d) int f conj(chi_d). In the class variable t, chi_d = sin(dt)/sin t and
  the Haar density is (2/pi) sin^2 t. This gives the displayed c_d.
  Checked.
- f(t) = e^{i beta cos t} sin t is odd, smooth and 2 pi-periodic, and
  |f'''| <= C(1 + beta)^3. Three integrations by parts on the circle give
  |c_d| <= C(1 + beta)^3/d^4. Checked.
- The kernel of |D_e| is sum_d d |c_d| chi_d, and |chi_d| <= d, so it is
  bounded by sum_d d^2 |c_d| <= C(1 + beta)^3. Checked.

### 5c. The trace-norm proof, L129-141: HOLDS

- D_S is a product of commuting central convolutions times P, so it is
  normal and |P X| = P|X|. Checked.
- With D = W|D| and W commuting with |D|, B^{1/2} D B^{1/2} =
  (B^{1/2} W |D|^{1/2})(|D|^{1/2} B^{1/2}). Both factors have squared
  Hilbert-Schmidt norm Tr(B|D|). Checked.
- B has a nonnegative kernel. The kernel of |D_S| is bounded by
  [C(1 + beta)^3]^{sum_S m_b} times the kernel with S erased. So
  Tr(B|D_S|) <= [C(1+beta)^3]^{sum m_b} Z_deleted(S). (2) at u = 1 on S
  gives Z_deleted(S)/Z_1 <= e^{-D sum m_b/3}. Absorbing the polynomial
  factor gives the displayed exponent. Checked.
- Fourier inversion at q = 2: 2^N C_r = sum_S (+-1) D_S, with S = empty
  giving rho. The sum over S != empty is E'_1. With X the unnormalized
  filtered operator and tau = Tr X, ||X/tau - X||_1 = |1 - tau| <= E'_1.
  So ||rho_r - rho||_1 <= 2 E'_1. Checked.

### 5d. The constant cut and the forest bound (9), L143-147: HOLDS

- J = 0 on every packet has weight 1, so p_empty = Z_deleted/Z_1. (2) with
  u = 1 on all 3V plaquettes gives e^{-D V}. Checked.
- Inside the zero-residue state its weight is p_empty/Pr(r = 0)
  <= 2^N e^{-D V}/(1 - E_1) by (3). Checked.
- Forest. A forest on V vertices has at most V - 1 edges. So the
  zero-degree packets hold at least 2V + 1 of the 3V edges. For each such
  set S, Pr(J_b = 0 on S) = Z_deleted(S)/Z_1 <= e^{-(2V+1)D/3} by (2).
  There are at most 2^N sets. Checked. Equal packet sizes are not needed.

### 5e. Central degrees on growing sets (10), L153-164: HOLDS

- x_s solves s/x = tanh x, the unique maximum of log p_s, since
  -(log p_s)'' = s/x^2 + sech^2 x > 0. So 0 <= g_s <= 1. Checked.
- By (1), Pr(2 J_b = s on the k packets) = E prod_b p_s(lambda_b)
  = p_s(x_s)^k E prod g_s(lambda_b). Checked.
- k = o(beta): the one- and two-period ratios are e^{O(k/beta)}, so the
  analogue of (4) holds with error O_m(k/beta). p_s(x_s) is of order
  s^{-1/2}, so the joint probability tends to 0. Checked.
- Other packets. By conditional independence, F = prod g_s(lambda_b) is a
  field function in [0,1]. (3) with that F gives additive error E(B',q) in
  the normalized probability. Checked.

### 5f. Lower bound in (10), L166-168: HOLDS

- E e^{X/48} <= C_m. With u = 1/48 the display after row 1151 (22b) gives
  log E exp[(beta/48) sum_b (1-w)] <= (3/4) m/48 + O(m/48). That display
  needs beta -> infinity, beta = O(log n) and the rectangles of L153, which
  are stated. Checked.
- 0 <= m beta - lambda <= X for either sign of Y_b. So
  |lambda - x_s| <= X + C_m. Markov gives Pr(lambda < x_s/2)
  <= C_m e^{-c_m beta}. Checked.
- On lambda >= x_s/2 the curvature is <= 4/s + sech^2, so
  -log g_s(lambda) <= C(lambda - x_s)^2/s, with mean O_m(1/beta). Checked.
- Small lambda. The top spatial link lies in exactly one plaquette of the
  packet, so Y_b = c + (a unit coordinate of that link). Its conditional
  density against Haar is <= C(1+beta)^{3/2}: the cap of radius
  (1+t)^{-1/2} has mass >= c(1+t)^{-3/2} and exponent >= t - 1/2. The Haar
  coordinate has density <= 2/pi. So Pr(lambda < v) <= C sqrt(beta) v.
  Checked.
- -log g_s(lambda) <= s log(x_s/lambda) for lambda < x_s, since
  cosh lambda <= cosh x_s. The split of the tail integral at
  2 c_m beta + O(log beta) gives a term O(beta^2 e^{-c_m beta}).
  So E log g_s >= -C_m/beta, and Jensen gives the lower bound for every k.
  Checked.

### 5g. Upper bound in (10), L170: HOLDS

- Given all spatial and white temporal links, each black temporal link on a
  marked cut lies only in its six plaquettes. These sets are disjoint. So
  the black links are independent, on one cut and across the two cuts.
  Checked.
- Density e^{t z} sqrt(1 - z^2). With y = t(1 - z) it is proportional to
  e^{-y} sqrt(y(2t - y)) on [0, 2t]. For t >= 1 the normalizer is at least
  (2/3) e^{-1} sqrt(2t - 1) >= c sqrt t, so the density is <= C e^{-y}
  sqrt y. Convolution with independent terms and folding keep a bounded
  density. Checked.
- If all t_i < 1, lambda < l = m/6, far from x_s. Otherwise
  Pr(|lambda - x_s| < delta) <= 1/2 for a fixed delta. Log-concavity and
  curvature >= s/(x_s + delta)^2 give g_s <= 1 - c/s off that window. So
  the conditional mean is <= 1 - c_m/beta, and the product gives
  e^{-c_m k/beta}. Checked.

### 5h. The conditional coefficient (11), L172-178: HOLDS

- With t_i = 6 beta - A_i + o(1), the law of y_i tends, with all moments,
  to e^{-y} sqrt(y)/Gamma(3/2), the Gamma(3/2, 1) law. Its mean and
  variance are both 3/2. Checked.
- sum t_i z_i = m beta - A - sum y_i + o(1) (m = 6 l). With m beta - s -> D
  and x_s = s + o(1), lambda - x_s -> D - A - sum y_i. The curvature at x_s
  is 1/s + o(1/s) and s/beta -> m. So beta(1 - g_s) ->
  (D - A - sum y)^2/(2m). Checked.
- E(D - A - sum y)^2 = (D - A - 3l/2)^2 + 3l/2. This is (11). The
  domination by C_m(1 + sum y)^2 and the exponentially small complement
  justify the limit. Checked.

### 5i. Two near-flat exteriors, L180: HOLDS

- All white temporal links and slice links at 1: each staple is 1, so
  t_i = 6 beta and A = 0. Checked.
- Setting two bottom links at the chosen black vertex to make staple
  factors e^{i theta}, e^{-i theta} gives staple sum 4 + 2 cos theta, a real
  quaternion. t_i = 6 beta - 2 beta(1 - cos theta) = 6 beta - 4m. A bottom
  link on edge e touches only the staple of the black end of e on this
  cut. So other black vertices keep t_i = 6 beta. Needs beta >= m, true
  eventually. Checked.
- With D in [3m/4 - 1, 3m/4 + 1] and 3l/2 = m/4, the squares are about
  (m/2)^2 and (7m/2)^2. They differ. The chosen links have distinct black
  endpoints in distinct packets, so the k factors multiply. The log
  difference is (c + o(1)) k/beta. Checked.

### 5j. GUIDE and OPEN text

- L3, L9, L11 (sources). They credit Sussman and Alpoge, Bhattacharjee,
  Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy, and Zeng
  Chunping. L3 says the row 1327 report is absent at its pin; it exists on
  the current branch. Not an error at that pin.
- L15, L17 (setup) are consistent with the proofs. In L17 B is the
  open-cylinder operator; later the packet set is a script B. The two
  meanings never collide in a formula. K_0 (L108, large q) and rho_0 (L192,
  q = 2) are different objects; see section 2.
- L151 correctly notes that (1) defines a law on the raw history, and that
  identifying a raw observable needs flip invariance.
- L192 and the RESULT line match the proofs. No seed is claimed.

## 6. Restatement of earlier rows

- (12), the main closing step, restates row 1325 (26) at k = l = 0, with the
  residue normalization from (3). See 4a.
- The reduction in L192 repeats the row 1325 (25) argument
  (Tr U^{2T} <= Tr U^T, constants 1650/1651) with p_{2T}/p_T^2 in place of
  the overlap sum.
- (1) extends row 1325 (12) from one total degree to independent packets,
  as the file says. The proof of (2) is row 1151 (21) with a variable
  profile plus a cap bound.
- New and not restatements: the filtering estimates (3)-(7), the
  large-q seed (8) with its obstruction, the trace-norm bound, and the
  degree estimates (10)-(11) with the exteriors of L180.

## 7. Verdict table (25 PROVED blocks)

| # | Lines | Statement | Verdict |
|---|---|---|---|
| 1 | L19-24 | packet expansion (1), positive kernels | HOLDS |
| 2 | L26-32 | weakening bound (2), reduction to h = min(u, 1/3) | HOLDS |
| 3 | L34 | proof of (2): variable-profile dissemination, cap | HOLDS |
| 4 | L36-48 | residue filtering (3) | HOLDS |
| 5 | L50 | proof of (3) | HOLDS |
| 6 | L52-59 | overlap (4), Hilbert-Schmidt bound | HOLDS |
| 7 | L61 | eight-site example, b_* = 11/(3 pi^2) | HOLDS |
| 8 | L65-69 | operator comparison (5) | HOLDS |
| 9 | L71-77 | proof of (5) | HOLDS |
| 10 | L79-83 | levels (6), physical energies | HOLDS |
| 11 | L85-95 | heat trace (7) | HOLDS |
| 12 | L99-108 | large-q seed (8), d_0 = o(1), one-cut defect | HOLDS |
| 13 | L110 | operator comparison cannot reach (8) | HOLDS |
| 14 | L112 | single-cut local test | HOLDS |
| 15 | L116-121 | trace-norm bound at q = 2 | HOLDS |
| 16 | L123-127 | coefficient bound for e^{i beta w} | HOLDS |
| 17 | L129-141 | trace-norm proof | HOLDS |
| 18 | L143-147 | (9) and the forest bound | HOLDS |
| 19 | L153-164 | (10) statement and consequences | HOLDS |
| 20 | L166 | lower bound in (10), moderate lambda | HOLDS |
| 21 | L168 | lower bound in (10), small lambda | HOLDS |
| 22 | L170 | upper bound in (10) | HOLDS |
| 23 | L172-178 | conditional coefficient (11) | HOLDS |
| 24 | L180 | two near-flat exteriors | HOLDS |
| 25 | L184-190 | identity (12) | HOLDS (restates row 1325 (26) at k = l = 0) |
| - | L192 (OPEN) | ratio bound gives ZD-c (PHYS-SEED) at 1/1650 | HOLDS; schedule E_2 -> 0 stated; name the packet partition |

No numeric run was used as a proof step. The one script evaluated
16 b_* = 5.944 as a guide.

RESULT: 25 PROVED statements of row 1328 checked by hand by Claude Opus 5.5: 25 HOLD, 0 need correction, 0 FAIL; main finding: fixing one q = 2 degree bit per eight black sites per cut moves the vacuum-normalized heat trace by a factor 1 + o(1) at T = O(n) and every bounded physical energy by o(1) on beta/log n -> 11/(3 pi^2) with 4 | n, and the large-q seed (8) holds with d_0 = o(1) but no operator bound reaches it (norm distance -> 1); (12) restates row 1325 (26) at k = l = 0 with the residue normalization, and the reduction to Theorem ZD-c at 1/1650 holds with no missing coupling hypothesis beyond the stated E_2 -> 0 (beta_j >= (3/16 + o(1)) log n_j for eight-site packets); the strict ratio bound, hence the seed and the mass gap, remains open.
