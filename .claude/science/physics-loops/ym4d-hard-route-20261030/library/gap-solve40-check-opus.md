# Check of row 1325 (gap-solve40-astra62.md) — FINISH row 1327

Checker: Claude Opus 5.5, line-by-line hand check.
Target: library/gap-solve40-astra62.md (row 1325, by gpt-6.2-astra).
Inputs read: gap-solve39-astra62.md (row 1323), gap-solve39-check-opus.md,
Theorem ZD-c in gap-phys-seed.md, and other rows as cited below.
Line numbers refer to gap-solve40-astra62.md at the commit checked.

Status: complete. 39 PROVED statements checked by hand.

Target commit of the checked file: 28ccf3b6f2.

## 1. Grid-cut recovery of the thermal defect (L236-277)

### 1a. Bessel facts and (19) (L236-240): HOLDS

- I_j(t) = const t^j times the integral of e^{tx}(1-x^2)^{j-1/2} on (-1,1).
  With I_j' = I_{j+1} + (j/t) I_j, the log derivative of t^{-j} I_j is
  I_{j+1}/I_j. So this ratio is the mean of x in that density. Checked.
- Given |x| = y the mean is y tanh(ty), increasing in y. Going from j to j+1
  multiplies the y-law by the decreasing weight 1-y^2. Chebyshev's sum
  inequality lowers the mean. So I_{j+1}/I_j decreases in j, and
  a_d = prod_{j<d} I_{j+1}/I_j <= a_2^{d-1}. Checked.
- a_2 = I_2/I_1 is the mean of cos(theta) under e^{t cos theta} sin^2 theta.
  Its t-derivative is a variance, so a_2 increases. Checked.
- (19): with s = sqrt(t) theta the law tends to s^2 e^{-s^2/2} ds and
  t(1 - cos theta) -> s^2/2, mean 3/2. Domination by 1 - cos theta >=
  2 theta^2/pi^2 and sin theta <= theta. So 1 - a_2(t) ~ 3/(2t) and
  -log a_2(t) = (3/2 + o(1))/t. Checked.
- The coefficient convention also checks: e^{t cos theta} has character
  coefficient (2d/t) I_d(t) at dimension d, so the normalized coefficient
  per dimension is I_d/I_1 = a_d, with a_1 = 1.

### 1b. Uniform bound (20), upper half (L242-249): HOLDS

- D = floor(n/b) and D >= b give a remainder below D. So lengths b or b+1
  fit. Checked.
- After the forest leaves and the path interiors are integrated, each coarse
  edge carries c_beta^{*l} = sum_d d a_d(beta)^l chi_d at one group element.
  With |chi_d| <= d, a_d <= a_2^{d-1} and l >= b:
  |h_e| <= sum_{d>=2} d^2 r_0^{d-1} <= C r_0. Checked.
- h_e integrates to zero in either end gauge, since the integral of chi_d(gA)
  over g vanishes for d >= 2. Checked.
- The coarse graph is the cubic torus with D >= 8 sites a side. It has no
  multiple edges and girth four. A leafless connected edge set needs at
  least four edges. So Z = 1 + O(z^4) and the log has no z, z^2, z^3 terms.
- The vertex deletion bound of (9) (checked in 5c below) gives
  |log Z| <= N log 2 on |z| <= c_0/r_0. Cauchy's estimate for the
  coefficients of order >= 4 at z = 1 gives C N r_0^4 once r_0 <= c_0/2.
  Checked.

### 1c. Lower half of (20) (L251): HOLDS

- In each 12-plane, squares with corners at even coordinates are vertex
  disjoint. Omitting the wrap square when D is odd keeps them edge disjoint.
  Count per plane floor(D/2)^2 >= 49 D^2/256 for D >= 8. Total >= N/16.
- k_b, as a kernel in the coarse holonomies, is the gauge projection of a
  convolution by a function with positive character coefficients. So it is a
  positive operator, and the Wilson-loop products are eigenfunctions with
  eigenvalue prod_e a_2(beta)^{l_e} >= a_2(beta)^{4(b+1) j}.
- The coarse holonomies are independent Haar variables, since distinct coarse
  paths use disjoint fine links. Products over distinct square sets are
  orthonormal (integrate an unshared edge). Each has squared value 4^j at
  the trivial field.
- Subtracting finitely many eigenprojections leaves a positive operator with
  continuous kernel, whose diagonal is >= 0. Summing over subsets gives
  k_b(1,1) >= (1 + 4 a_2^{4(b+1)})^{N/16}. Then log(1+4x) >= c x for
  0 <= x <= 1. Checked.

### 1d. The interacting bound (21) (L253-270): HOLDS

I derived the identity used. Write E1 for the normalized law of the two ends
of one open cylinder B, and E2 for the product of two such laws. With
normalized cut weights the 1/z_beta factors cancel, and

  W_b - Psi = log E2[k_b(cut 1) k_b(cut 2)] - 2 log E1[k_b].

This is the identity behind (2). Then:

- B = M K^{T-1} M has full spatial weight M^2 on both end slices. So an end
  link lies in four full-strength spatial plaquettes and one bulk temporal
  plaquette. The cut plaquette is inside k_b. Checked.
- The bulk temporal links must be among the conditioned "unmarked fine
  links". Then the marked link's temporal plaquette is a single e^{beta w}
  factor with a unit-quaternion staple. The text says "all unmarked fine
  links", which includes them. Checked.
- Incidence. Two parallel marks on one grid line are never in one plaquette.
  Distinct parallel grid lines are at distance >= b >= 4. A direction-i edge
  and a direction-j edge of one unit square share a vertex. That vertex lies
  on a direction-i and a direction-j grid line, so all three of its
  coordinates are coarse, and it is a coarse vertex. The marks exclude links
  at coarse vertices. With T >= 3 the two end slices of one cylinder are
  >= 2 steps apart. So no plaquette holds two marks, and the marks are
  conditionally independent. Checked.
- The conditional density is e^{beta S.U} with |S| <= 5, a translate of the
  central Wilson density at t = beta|S| <= 5 beta. Centrality moves fixed
  factors to one end. Inversion preserves central densities. Checked.
- With the coarse gauges fixed, the integrand is a product over coarse edges.
  Each factor depends on the marks of its own segment on the two sides. So the
  conditional expectation factors. At dimension d the coefficient is
  a_d(beta)^l times prod a_d(t_i) over at least 2(b-2) marks. With
  a_d <= a_2^{d-1} and a_2 increasing this is <= r_1^{d-1}. Checked.
- The conditional expectation and the coarse-gauge integral commute
  (positive bounded integrands). The girth-four expansion of 1b gives
  e^{-CNr_1^4} <= E[k_b | unmarked] <= e^{CNr_1^4} uniformly. In E2 the two
  cuts use disjoint marks, so the conditional factors multiply. Hence
  |W_b - Psi| <= 4 C N r_1^4. Checked.

### 1e. The exponents in (22) (L272-277): HOLDS

Take b = ceil((2/5) beta log n), beta -> infinity, beta <= B_0 log n. Then
b = O(log^2 n), so D >= 8, D >= b and log N = (3 + o(1)) log n. By (19):

- -log r_0^4 = 4 b (3/2 + o(1))/beta = (12/5 + o(1)) log n. With the lower
  bound in (20) (a_2(beta)^4 -> 1) this gives
  sup |log k_b| = n^{3 - 12/5 + o(1)} = n^{3/5 + o(1)}. Both bounds checked.
- -log r_1^4 = 4 (b/beta)(3/2 + 3/10)(1 + o(1)) = (84/25 + o(1)) log n.
  So N r_1^4 = n^{3 - 84/25 + o(1)} = n^{-9/25 + o(1)}. Checked. r_1 -> 0, so
  (21) applies.
- For b ~ d beta log n the two exponents are 3 - 6d and 3 - 42d/5. They are
  positive and negative exactly when 5/14 < d < 1/2. Checked.

Remark. (21) and (22) hold for every T >= 3, not only T = n/2. The error
bound does not use the thermal-seed rectangles.

## 2. The overlap formula (24) and its inputs (L156-186, L293-303)

### 2a. Positivity of H_k (L156-160): HOLDS

- Flipping the temporal links on black vertices of one cut by -1 (central in
  SU(2), Haar invariant) flips w on every temporal plaquette of that cut,
  since n is even and each spatial edge has one black end. It touches no other
  plaquette. So the dg-integral of Y^k is zero for odd k, already pointwise.
- At g = 1 the cut function is F(x y^{-1}) with F = (sum_e tr(u_e)/2)^k.
  A normalized character is positive definite, sums keep this, and the
  Schur (tensor) power keeps it. So convolution by F is a positive operator.
  It commutes with gauge action, because the edge traces are conjugation
  invariant. So the gauge average is P Conv_F P >= 0. Pointwise >= 0 for
  even k. Finite rank from the finite tensor power. Checked.

### 2b. Degree law (12) (L162-168): HOLDS

- With the cut weights erased the measure is invariant under each flip.
  So the integral of f(|Y|) e^{beta Y} equals that of f(|Y|) cosh(beta Y).
  The joint weight of (D = k, |Y|) is (beta|Y|)^k/k! for even k. Dividing by
  cosh gives (12) times the Wilson law of |Y|. For two cuts the flips are
  independent. Checked.

### 2c. Concentration (13) (L170-178): HOLDS, given row 1151, (21)-(22a)

I did not re-derive (22a). The Hoelder step checks: with three orientations
of m/3 plaquettes each and arguments 3h,
sum_o (1/3)(m/3)(3)(3h/4) = 3mh/4 cancels the centring. The remainder is
C m (h^2 + |h| beta^{-eta}). With h = +-eps r and beta^{-eta}/r =
beta^{-eta/2} -> 0, Chernoff gives exp(-c m r^2). Checked.

### 2d. Retained degrees (14) (L180-184): HOLDS

- On the good event Y > 0 and lambda = beta m - X, so
  |lambda - d_*| = |X - 3m/4| <= m r. Checked.
- e^t - 1 - t <= t^2 for |t| <= 1 (the ratio (e^t-1-t)/t^2 increases in t
  and is e - 2 < 1 at t = 1). With t = c r/beta and lambda ~ m beta,
  P(|D - lambda| > 2mr) <= 2 exp(-(2c - c^2(1+o(1))) m r^2/beta).
  Parity conditioning costs a factor <= 2, since P(even) >= 1/2. Then
  |D - d_*| <= 3mr. The union bound covers two cuts. m r^2/beta =
  3 n^3 beta^{-1-eta} -> infinity. Checked.

### 2e. Replacement by C_I (L186): HOLDS

Tr(B C_I)/Tr(B C) and Tr(B C_I B C_I)/Tr(B C B C) are the one- and two-cut
probabilities that all degrees are retained. The trace-norm bound for a convex
mixture is correct: rho = p rho_I + (1-p) rho', so
||rho - rho_I||_1 <= (1-p)(||rho_I||_1 + ||rho'||_1) = 2(1-p). Checked.

### 2f. (24) itself (L293-303): HOLDS

- A_k = B^{1/2} H_k B^{1/2} >= 0 with finite trace z_k. So A_k/z_k is a
  density operator. R_kl = Tr(rho_k rho_l) >= 0 (two PSD operators) and
  <= ||rho_k||_op Tr rho_l <= 1. Checked.
- Expanding C_I = sum_{k in I} beta^k H_k gives exactly
  Tr(BC_IBC_I)/Tr(BC_I)^2 = sum p_k p_l R_kl. Checked.
- e^{-Psi} = Tr(BCBC)/Tr(BC)^2 = (retained purity) times P1^2/P2, where
  P1, P2 are the retained probabilities of 2e. Both are 1 - O(eps) with
  eps = exp(-c m r^2/beta). The retained purity is <= 1. So
  e^{-Psi} = sum p_k p_l R_kl + O(eps). Checked.
- Scope. (24) holds under the hypotheses of (13)-(14): T = n/2,
  beta -> infinity, beta <= B_0 log n. This matters in item 3.

## 3. (25) suffices for Theorem ZD-c (L305-310): HOLDS AFTER CORRECTION

I read Theorem ZD-c in gap-phys-seed.md (its statement and proof, and the
notation line S(k; B) = sum_{i>=1} (lambda_i/lambda_0)^k). With
U = K/||K|| one has S(n/2; n^3) = Tr U^{n/2} - 1, counted in the full
physical space with multiplicities.

- The constants. sum_{k,l} p_k p_l = 1, so the sum in (25) is
  1 - sum p_k p_l R_kl. If its limsup is < 1/1651, then by (24)
  liminf e^{-Psi} > 1650/1651, that is limsup Psi < log(1651/1650).
  K >= 0 gives eigenvalues u_i of U in [0,1], so Tr U^{2T} <= Tr U^T and
  Psi = 2 log Tr U^T - log Tr U^{2T} >= log Tr U^T. Hence
  limsup (Tr U^T - 1) < 1651/1650 - 1 = 1/1650. This is (PHYS-SEED) of
  ZD-c at the two-stage threshold t(2) = 1/1650. Strictness is kept at
  each step. Checked.
- Psi is unchanged when K is scaled, so the normalization of K does not
  matter. Checked.
- Correction. (24) is proved only under the hypotheses of (13)-(14):
  beta_j -> infinity and beta_j <= B_0 log(L/a_j). Theorem ZD-c has no
  hypothesis on the coupling. Its "limit hypotheses" are the size set P and
  the integrality of l_1/(4 a_j). So the sufficiency statement must add:
  along the trajectory beta_j -> infinity and beta_j <= B_0 log(L/a_j) for
  one fixed B_0. An asymptotic-freedom trajectory meets this. With that
  added, and L in P (so n = L/a_j is divisible by four), the statement
  holds as written.

## 4. The single-degree identity (26) and its consequence (L312-322): HOLDS

- P_T(k) = beta^k z_k/Tr(BC) and P_{2T}(k,l) = beta^{k+l} Tr(A_k A_l)/
  Tr(BCBC). Dividing, P_{2T}(k,l)/(P_T(k)P_T(l)) = R_kl Tr(BC)^2/Tr(BCBC)
  = R_kl e^{Psi}. This is (26). Checked.
- From (26), -log R_{k0k0} - Psi = 2 log P_T(k0) - log P_{2T}(k0,k0). Both
  probabilities are <= 1. For the lower bound, restrict to the good event
  (probability -> 1) and use conditional independence of D_1, D_2 given
  (|Y_1|, |Y_2|). There |k0 - lambda| <= mr + 2 and lambda ~ m beta. The
  log mass of (15) is -(mr)^2/(2m beta)(1+o(1)) + O(m r^3/beta^2 +
  log(m beta)), and m r^3/beta^2 <= m r^2/beta. With r^2 = beta^{-eta}
  this gives the bound C_eta(m beta^{-1-eta} + log(m beta)). The Taylor
  range |k - lambda|/lambda <= 1/2 holds. Checked.
- The closing remark is accurate: m = 3n^3, so the bound grows on the
  physical grid and cannot give (25).

## 5. The other PROVED statements

### 5a. The grid H_b, (1) and (2) (L21-45): HOLD

- L21. Growing a spanning tree from the connected grid gives the forest with
  one attachment per tree. With b | n and n/b >= 4 the coarse graph has no
  multiple edges, and it has 3(n/b)^3 coarse edges. HOLDS.
- L23-32, (1). Leaf integration of the forest gives one. With the coarse
  gauges fixed, each open path of length b gives c_beta^{*b} at one element,
  equal to 1 + sum_{d>=2} d a_d^b chi_d. Its distance from one is at most
  zeta_b. Multiply and then integrate the coarse gauges. HOLDS.
- L34 (GUIDE). a_d^b <= a_2^{b-1} a_d and sum d^2 a_d = 1/z_beta give the
  cited form of the row 1323 bound. Consistent.
- L36-45, (2). From the identity in 1d, with (1) on each cut, both
  log E2[kk] and 2 log E1[k] lie in [2m_b log(1-zeta_b), 2m_b log(1+zeta_b)].
  T >= 2 makes the two ends of B distinct slices. HOLDS.

### 5b. The Gaussian side, (3)-(8) (L51-102): HOLD

- L51-61, (3)-(4). A vanishes on gradients, so (A)_S = rho A rho^*, where
  rho is restriction from cycles to R^S. Its kernel is D and rho^* maps onto
  F. So the ratio in row 1323, (20), is det(A+Delta)_F/det A_F, which is (3).
  A constant h in F is orthogonal to D. Some d in D has harmonic part h, so
  |h|^2 = <h,d> = 0. Hence A_F > 0. From row 1323, (21):
  delta = tanh(w/2)[coth(Tw/2) - tanh(Tw/2)] = 2 tanh(w/2)/sinh(Tw).
  HOLDS.
- L63-72, (5). Q(h) = sup |<h,f>|^2/<f,Af> over f in F. f is orthogonal to
  D, so h may be replaced by h - d. h - d is a cycle with zero constant
  coefficient, and Cauchy-Schwarz over the k' != 0 modes gives (5). HOLDS.
- L74-83, (6), the lift. h is divergence free. On a direction-i segment the
  flow is constant. At a coarse vertex the identity
  1 - e^{-ibt} = b(1 - e^{-it}) phi(t) reduces the divergence to
  b^3 n^{-3/2} e^{ik.bx} sum_i v_i (1 - e^{-ik_i}) = 0. The Fourier sum
  gives d-hat(k) = v, with aliases v_i phi(k'_i)/phi(k_i) at
  k' = k + 2 pi m/b. For k != 0 with |k|_inf < pi/b no alias is zero.
  |phi(t)| = |sin(bt/2)/(b sin(t/2))| >= 2/pi for |bt| <= pi. HOLDS.
- L85, the alias sum. tanh(w/2) >= c w (w bounded) and
  T|k'|_inf >= 2 pi alpha give a(k')^{-1} <= C_alpha/|k'|_inf. Shells of
  radius j have <= 8j members at |k'|_inf >= pi j/b, so the total over the
  shells is <= C_alpha b^2. The sum of |phi|^2 over all b aliases is 1
  (finite orthogonality). So Q <= (pi^2/4) C_alpha b^2. HOLDS.
- L87-93, (7) upper. Tr(A_F^{-1} Delta_F) = sum over the Fourier basis of
  delta_h Q(h). Low modes: delta <= (C_alpha/n) j e^{-c j}, about j^2 modes
  per shell, Q <= C b^2. The constants cost 3 C b^2/T. High modes:
  delta/a = 1/sinh^2(Tw/2), and j >= n/(2b). HOLDS.
- L95, (7) lower. The minimum-norm lift of a constant h puts value
  b^2 v_i n^{-3/2} on the n^3/b^2 grid edges of direction i. Its squared
  norm is b^2, so |Rh|^2 = b^2 - 1. Different directions have disjoint
  supports, so R^*R = (b^2-1) I. A_P <= I because tanh(w/2) <=
  tanh(Tw/2). A_P >= A_A gives a transverse ratio >= 1. HOLDS. The
  "precisely when" clause follows from the two sides of (7).
- L97-102, (8). b ~ n^{1/3} gives m_b zeta_b <= C n^2 (log n)^{3/2}
  exp(-c n^{1/3}/log n) -> 0 and b^2/n ~ n^{-1/3}. HOLDS. The contrast with
  row 1323, (28), is stated correctly.

### 5c. The weak whole cut, (9)-(11) (L113-150): HOLD

- L113-119. h_e is analytic on a small disk and bounded by C_0 r. The
  integral over either end gauge is zero by Haar invariance. Products over
  vertex-disjoint components factor. HOLDS.
- L121, vertex deletion. Doubling the edges of a connected q-edge set gives a
  closed walk of length 2q from z. So there are at most 6^{2q} such sets.
  They have at most q further vertices, which gives the ratio bound 2^q.
  The sum is <= sum (72 C_0 r)^q <= 1/2, so the induction closes.
  |log k_u| <= V log 2, and Cauchy's estimate on |u| <= r/2 bounds the
  tail from order five. HOLDS.
- L123, the coefficient. The only leafless connected 4-edge sets are
  elementary squares. Overlapping-cluster terms start at order u^8. Each w_e
  is a real inner product <g_b, M g_a N> on R^4. Integrating a corner gives
  delta/4. The trace of g -> a g c on H = R^4 is
  tr_{C^2}(a) tr_{C^2}(c) = 4 Re a Re c. So the coefficient is
  4^{-4} * 4 w_p(x) w_p(y) = w_p(x) w_p(y)/64. HOLDS.
- L125-130, (10). Since k_u = 1 + (u^4/64) sum_p w_p(x) w_p(y) + O(u^5),
  the u^4 term is 2 E1[ww]/64 - 2 mu^2/64 per plaquette. In E2 the two
  arguments are on independent cylinders, and reversal makes the two means
  equal. B >= 0, and Cauchy-Schwarz against 1 gives the sign. HOLDS.
- L132-143, (11), given row 1151, (6), which I read but did not re-derive.
  Writing w = 1 - d splits the leading kernel into a scalar, f(x)f(y) and
  e^E. A rank-one tilt gives ratio one. Good ends give
  0 <= E <= C gamma V/beta^2. On bad ends E <= 12 gamma V. The tilt lies in
  [e^{-12 gamma V}, 1], so a bad set costs at most
  e^{24 gamma V} C e^{-c_1 V/beta^2}. Small c absorbs gamma V. The u^5
  remainder enters four logs. HOLDS.
- L145-150. V u_*^4/beta^2 = beta^{-2/3}, V u_*^5 = n^{-3/4} beta^{5/3}, and
  u_*^4 <= c beta^{-2} for large n. Distinct plaquettes share at most one
  edge, so the plaquette characters are orthonormal. a_2(u) = u/4 + O(u^3),
  so 3V a_2(u_*)^4 ~ 3 beta^{4/3}/256 -> infinity. HOLDS.

### 5d. Degree rates and the weak-cut overlap, (15)-(16) and L206-208: HOLD

- L188-198, (15). On the good event (k - lambda)^2/(2 lambda) =
  (m/beta)(x^2/2)(1 + O(r) + o(1)). The cubic error divided by m/beta is
  O(1/beta). The complement costs -c beta r^2 = -c beta^{1-eta} on the
  beta/m log scale, which tends to minus infinity. Conditional independence
  given (|Y_1|, |Y_2|) gives the sum for q = 2. HOLDS.
- L200-204, (16). The degree-tuple weights at u_* and beta differ by
  (u_*/beta)^{sum k} times a partition ratio within e^{+-qm beta}. On E_I,
  sum k = q m beta (1 + o(1)). log(beta/u_*) -> infinity absorbs the
  qm beta term, and P_beta(E_I) -> 1. HOLDS.
- L206, given row 1153, (5) (checked in row 1154), which I did not
  re-derive. For t_s ~ beta^{1/32}: t_s^4 beta^{-1/4} = beta^{-1/8}, so the
  cited condition holds. For t_v, a strictly positive continuous kernel has a
  simple top eigenvalue, and the trace class property gives
  Tr U^t - 1 -> 0. Then Psi <= 2 log Tr U^{t_v} <= 2 log(1 + 1/n). HOLDS.
- L208. This modifies the proof of row 1151, (22a)-(22b), to sides
  (n,n,n,t). I checked the parameter arithmetic, not the whole cited proof
  again. The leftover fraction is <= 4 b_0/s. With b_0 ~ beta^{1/64} and
  s >= c beta^{1/32}: 1/b_0 and b_0/s are both <= C beta^{-1/64}. The secant
  distance is O(beta^{-1/128} sqrt(log beta)), so any eta < 1/128 works.
  b_0^{12} log beta = beta^{3/16} log beta = o(beta). The limit in (15) does
  not depend on the period. HOLDS.

### 5e. Homogeneous weakening, (17)-(18) and L230: HOLD

- L212-219, (17). The Wilson identity follows by cancelling partition
  functions: the two deletion moments give Psi - J(u). For the Gaussian side,
  I - (1-e) Gamma = e + (1-e)(I - Gamma), and on a cut I - Gamma is A_P.
  Row 1323, (20), splits the two-cut form into A_P and A_A. Gradients cancel.
  The constants give (9/2) log((e + (1-e)/T)/e). Each transverse mode gives
  3 log of the stated ratio. HOLDS.
- L221-228, (18). Here e T -> alpha c and n w -> 2 pi |l|. Each term is
  >= 0 and at most delta/a = 1/sinh^2(Tw/2), which is summable uniformly.
  For n e -> infinity the terms are bounded by delta (1-e)/e -> 0. The
  monotony and the limits check. HOLDS.
- L230. u = beta c/n <= u_* iff c beta^{2/3} <= n^{1/4}, which holds under
  beta <= B_0 log n. n u_*/beta = n^{1/4} beta^{-2/3} -> infinity, so
  G -> 0. (11) is uniform in T >= 2, so it applies at T = t_s. HOLDS.

### 5f. The order-one coupling (23) (L279-289): HOLDS

- The integral over S^3 of e^{beta q.v} is 2 I_1(beta R)/(beta R) with
  R = |v|. This equals e^{beta R} (beta R)^{-3/2} (C + o(1)) uniformly near
  R = 5.
- For A = e^{i theta}, B = e^{i phi}:
  |3 + A + B| = 5 - (theta^2 + phi^2)/2 + (theta + phi)^2/10 + O(4th order).
  The cross ratio keeps only beta * 2 theta phi/10 = st/5. The quartic error
  is O(1/beta). HOLDS.
- The neighbors at offsets e_2, e_3 lie in the 12- and 13-planes, so no
  plaquette holds both. HOLDS.

## 6. Restatement, the OPEN paragraph, and scope

- No main step only restates an earlier row. (1)-(2) extend the ring
  convolution of row 1323, (16)-(17), to a grid. (3)-(4) apply row 1323,
  (20)-(22), to a new graph. The new parts are the lift (6), the bound (7),
  the marked-link convolution (21), the degree law (12) with (14), and the
  overlap form (24). (13) reuses row 1151, (21)-(22a), with one Hoelder
  step. The coefficient in (9) uses the quaternion contraction of row 1151,
  (25). I found no earlier row with the total-degree parity law (12).
- Inputs used and not re-derived here: row 1151, (6), (21), (22a)-(22b);
  row 1153, (5). The author marks them as cited. Row 1153 was checked in
  row 1154.
- The OPEN paragraph (L324) and the closing line (L326) are accurate. The
  row proves no seed. (25) at fixed physical size stays open. The single
  central degree bound (26) grows like m beta^{-1-eta}, far from the order
  one margin that (25) needs.
- Credits as given in the file: Ethan Sussman and Levent Alpoge (GL3, GL8,
  finite chessboard inequality); Sourav Chatterjee (weak-coupling
  free-energy method behind (22a)); Bhattacharjee, Bhattacharya, Lockwood,
  Romanov, Sessford and Singha Roy (straight-path convolution, row 1218).
- No numeric run was made for this check.

RESULT: 39 PROVED statements of row 1325 checked by hand by Claude Opus 5.5: 38 HOLD, 1 HOLDS AFTER CORRECTION, 0 FAIL; main finding: the grid-cut recovery holds, |W_b - Psi| <= C N r_1^4 = n^{-9/25+o(1)} at b = ceil((2/5) beta log n) while sup |log k_b| = n^{3/5+o(1)}, and the overlap formula (24) with 0 <= R_kl <= 1 and the identity (26) hold; the reduction of (25) to Theorem ZD-c holds with the constants 1/1651 and 1/1650 after adding the coupling range beta_j -> infinity, beta_j <= B_0 log(L/a_j) along the trajectory, which (24) needs and ZD-c does not supply; no seed is proved and (25) stays open.
