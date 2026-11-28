# Check of row 1337 (gap-solve44-astra62.md), FINISH row 1338

Checker: Claude Opus 5.5, line-by-line hand check.
File checked: library/gap-solve44-astra62.md (row 1337, by gpt-6.2-astra).
Line numbers refer to that file at the commit checked.
Verdicts are appended section by section.

## Inputs read

- Row 1337 in full (207 lines).
- Theorem ZD-c and the lead note on its coupling range, `gap-phys-seed.md` L311-L322.
- Row 1334 (`gap-solve43-astra62.md`) target (1) and the moment bound (5), L19-L66; its check, row 1336, RESULT line.
- Row 1151 (`gap-solve5-astra62.md`) Sections 8, 9 and 12, with (22b) and (24).
- Rows 1227 (14), 1161 (19), 1215 (5) at the lines named below.

Notation in this check: L-numbers are lines of row 1337. "Row 1334 (5)" is the moment bound E exp((beta/2) sum_S a_p) <= C_0^{|S|} for one orientation on either periodic torus, with C_0 uniform in beta >= 0 (its J-bounds c(1+b)^{-3/2} <= J(b) <= C(1+b)^{-3/2}). Its singleton case gives E a_p <= C/beta and E a_p^2 <= C/beta^2 by Jensen and e^x >= x^2/2.

## 1. The positive integral for the thermal deficit (L17-L45)

**V1. L17, squared-kernel density. HOLDS.** With K_t symmetric and the two arcs of length t, the opposite-slice density is K_t(x,y)K_t(y,x)/Z_T = K_t(x,y)^2/Z_T. Its integral is Tr F^{2t} = Z_T. The per-layer electric and magnetic normalizations are common to Z(n,T)^2 and Z(n,2T) and cancel in the ratio. This is row 1171's identity, as credited.

**V2. L19-L26, (1). HOLDS.** At s = 0, sqrt(P_0 Q_0) = K(x,y)K(x',y')K(x,y')K(x',y)/Z_T^2. In the order x, y, x', y' the four kernels chain to Tr F^{4t} = Z_{2T}. So A(0) = Z_{2T}/Z_T^2. At a fixed finite box, H_s p(.,y) tends uniformly to the Haar average m(y), so P_infty = Q_infty = m(y)m(y') and A(infty) = 1.

**V3. L28-L33, (2) and the integral identity. HOLDS.** I rederived the affinity derivative. For positive f, g with d_s f = (1/2)Delta f, d_s g = (1/2)Delta g on a compact manifold, d/ds int sqrt(fg) = (1/8) int sqrt(fg) |grad log(f/g)|^2. (Write u = log f, w = log g; the two integrations by parts give -(1/2) sqrt(fg)|grad(w-u)|^2 inside a factor -1/4.) Here P_s and Q_s both solve the heat equation in (x,x'). grad_{x_e} log(P/Q) = v_e(x,y) - v_e(x,y'). The swap (x,y) <-> (x',y') fixes P and Q, so the x' part equals the x part. The total is (1/4) sum_e int sqrt(PQ)|v_e(x,y) - v_e(x,y')|^2, which is (2). A' >= 0, and A is continuous on [0, infty] at fixed box, so 1 - Z_{2T}/Z_T^2 = int_0^infty A'. The threshold: limsup Z_T^2/Z_{2T} < 1651/1650 is liminf A(0) > 1650/1651, that is limsup (1 - A(0)) < 1/1651. Correct.

**V4. L35-L39, the zero-noise score. HOLDS.** In the sandwich convention K_t(x,y) carries e^{-V(x)/2}, and the first electric layer has exactly one temporal plaquette through x_e. With weight e^{-beta a_p} = e^{-beta} e^{beta Re U_p}, grad_{x_e} log K_t = -(1/2) grad V + beta E[J_e | x,y]. Doubling for K_t^2 gives the display. The magnetic term is the same for (x,y) and (x,y') and cancels in (2).

**V5. L39-L43, (3). HOLDS.** sqrt(P_0 Q_0)/A(0) is the joint density of four slices at spacing t on the period-4t = 2T torus, with Y ahead of X and Y' behind. Given (X,Y) the bridge between them is the single bridge law, so the inner expectations are as stated. The prefactor is (1/4)(2 beta)^2 = beta^2. Correct.

**V6. L45, the bound A'(0)/A(0) <= C n^3 beta. HOLDS.** Re U_p is the restriction of a linear function <x_e, w> with |w| = 1 to the unit sphere, so |J_e|^2 = 1 - (Re U_p)^2 <= 2(1 - Re U_p). Row 1334 (5) at a singleton on the period-2T torus gives E(1 - Re U_p) <= C/beta. Conditional Jensen and (a-b)^2 <= 2a^2 + 2b^2 give each summand <= C/beta. There are 3n^3 spatial links. The remark that this grows with volume is correct.

## 2. The large-noise conditional density (L49-L77)

**V7. L49-L53, delta <= C_0 e^{-3s/2}. HOLDS.** On the unit 3-sphere the spin-(d-1)/2 character is an eigenfunction of the Laplacian with eigenvalue -(d^2-1). The Peter-Weyl expansion of the heat density for generator (1/2)Delta is w_s = sum_d d e^{-(d^2-1)s/2} chi_d. With |chi_d| <= d, |r_s| <= sum_{d>=2} d^2 e^{-(d^2-1)s/2} <= C_0 e^{-3s/2} for s >= 1.

**V8. L55-L61, (4), and 1-delta <= b_e^S <= 1+delta. HOLDS.** The bracket bound holds because b_e^S is a posterior average of w_s(z_e ((g.b)_e)^{-1}). The expansion is checked in V9 and V10. The leading remainder is O(delta^5) = O(e^{-15s/2}).

**V9. L63-L68, the exact ratio expansion and the tail sum. HOLDS.** I rederived D_{S+e} - D_S = sum_{B ni e} h_B D_{S \ I(B)}. Terms of D_{S+e} with e in the support split as the component B of e times any support in S \ I(B), and the latter sum is D_{S \ I(B)}. Vertex-disjoint components factor, and a leaf component vanishes by its leaf gauge. The quotient bound: D_S is D_{S\I(B)}-weighted by at most |S cap I(B)| <= 6(|B|+1) factors in [1-delta, 1+delta]; positivity of the unexpanded product gives the two-sided bound. The doubled-tree walk gives at most 2*6^{2k} connected sets of size k through e. With 36 delta (1-delta)^{-6} < 1/2 the sizes k >= 5 sum to C delta^5. In the cubic 3-torus with n >= 8 a leafless edge set of size at most 4 is an elementary square. Its quotient is 1 + O(delta) and |h| <= delta^4, so the correction is O(delta^5).

**V10. L70, the square coefficient. HOLDS.** On a square every proper nonempty edge set has a leaf, so the density is 1 + h_{dp}. It is gauge invariant, so it is a class function of z_p. The holonomy of four independent central heat increments around b_p has class law of b_p diffused for time 4s, so E chi_d(z_p) = e^{-2(d^2-1)s} chi_d(b_p). Under product Haar z_p is Haar, and orthonormality of real characters gives the coefficient. The d = 1 term is the constant 1.

**V11. L72-L77, (5). HOLDS.** d - chi_d(theta) = sum_m (1 - cos m theta) over d weights with |m| <= d-1, and 1 - cos m theta <= m^2 (1 - cos theta), so |chi_d - d| <= d^3 a_p. The two conditionals in (4) differ by at most C e^{-6s} sum_{p ni e} a_p + C e^{-15s/2}, uniformly in z_S. D(f||g) <= int (f-g)^2/g with g >= 1-delta. The chain rule over the 3N edges, and (sum of at most four a_p)^2 <= 4 sum a_p^2, give (5).

## 3. The part erased by noise (L81-L95)

**V12. L81-L84, (6). HOLDS.** Given Y, the law of X is invariant under vertex gauges at the X end (K_t(g.x, y) = K_t(x,y)). So p_s(.,y)/m(y) = E[k_s^X | Y=y] exactly. Joint convexity of relative entropy, then (5), then E a_p(X)^2 <= C/beta^2 on the 3N spatial plaquettes, give (6). The bound uses row 1334 (5) only at singletons, which holds on the period-T torus for every beta >= 0.

**V13. L86-L90, (7). HOLDS.** Let mu be the law of (Z,Y) and nu = k^1 (x) m, d = D(mu||nu). Jensen gives int sqrt(mu nu) >= e^{-d/2}, so for the tensor squares 1 - int sqrt((mu (x) mu)(nu (x) nu)) <= 1 - e^{-d} <= d. nu (x) nu is swap invariant and the swap is an isometry, so ||sqrt P - sqrt Q||_2 <= 2 ||sqrt P - sqrt(nu (x) nu)||_2, whose square is at most 8d. Then 1 - A(s) = (1/2)||sqrt P - sqrt Q||^2 <= 4d. Correct as written.

**V14. L93, the range where the output still differs from Haar. HOLDS.** With u = N e^{-12s}, the right side of (7) is C(u/beta^2 + u^{5/4} N^{-1/4}), so u = o(min(beta^2, N^{1/5})) suffices. The N/4 squares of orientation 12 with even first two base coordinates are vertex disjoint. Under k^1 each holonomy is a product of conjugated increments whose law does not depend on the gauges, so the traces are i.i.d. with mean e^{-6s} (E chi_2/2 at heat time 4s) and bounded by 1. Under Haar they are i.i.d. with mean 0. The threshold test has Chebyshev errors at most 16/u each. The output marginal is within o(1) of k^1 in total variation by (6) and data processing. The conclusion holds.

**V15. L95, GUIDE example. Correct arithmetic:** u = N e^{-12s} = beta at s = (log N - log beta)/12.

## 4. (8) and (13) for noisy Wilson slices (L99-L155)

Coupling hypotheses as stated at L99: beta -> infinity and beta <= B log n, on the n^3 x (n/2) periodic Wilson torus. Both are used. beta -> infinity is needed for (24) of row 1151 and for the power beta^{-eta}. The upper bound is used for b/n << beta^{-2 eta}/log beta and for N e^{-15s} = (lambda beta^2)^{5/4} N^{-1/4} -> 0.

**V16. L99-L107, the input from row 1151 (24). HOLDS as cited.** I read row 1151 Section 9 (24) and Section 12 (the one-face covariance diagonal (1 - b^{-4})/2, the O(b^3) rank difference, position-average squared deviation O(1/b)). (24) is stated for the n^3 x T and n^3 x 2T Wilson tori, with Delta_b = (log beta)/b + (b/n) log beta. Row 1151 was checked by Claude Opus 5.5 (its check RESULT: HOLDS). The comparison method is credited to Sourav Chatterjee there and here. Correct.

**V17. L109-L117, (9) and its reflection step. HOLDS.** |g_p| <= 1 since both min(beta a_p, M) and c_M lie in [0, M]. With beta a_p = R_p^2/2, the derivative R/M is at most sqrt(2M)/M = sqrt(2/M) where unclipped. The reflection step I rederived: cut at b and b + T/2. X at 0 = T lies in the arc (b + T/2, T + b), and Y at T/2 in (b, b + T/2). Given the two cut slices the arcs are independent (nearest-neighbour Markov property in time). Time reflection t -> 2b - t fixes both cut slices, swaps the arcs, maps spatial slices to spatial slices without inverting spatial links, and maps the slice 0 to 2b, which lies in the Y-arc since b < T/2. So E|E[f(X)|Y]|^2 <= E phi(C)^2 = E[f(X_0) f(X_{2b})] with phi = E[f(X)|cuts]. Correct.

**V18. L119, the size of the reflected product. HOLDS.** 2k marks, sup bound 1, gradient norm at most sqrt(2k * 2/M) <= 2 sqrt(k). In (24), with l = 2k, H_1 = 2 sqrt k, H_0 = 1: the error is C k (sqrt(Delta_b) + 1/b + b/n + e^{-c beta/b^8}) = O(k beta^{-eta}), since sqrt((log beta)/b) = O(beta^{-eta}) for 2 eta < gamma and b/n is far smaller under beta <= B log n. Marks with the same spatial base are 2b apart in time and distinct marks are more than 4b apart in space, so they sit in distinct b-cubes and the Gaussian expectation factors. The one-mark mean: R_G^2 = v|G|^2, so |E g| <= E|min(v|G|^2/2, M) - min(|G|^2/4, M)|/M <= 3|v - 1/2|/(2M). Position-average of |v - 1/2| is O(b^{-1/2}) by Cauchy-Schwarz from the O(1/b) mean square, plus O(1/b) for dilation. Omitted faces have frequency O(1/b + b/n) and factor bounded by 1. Total O(b^{-1/2} + b/n) <= O(beta^{-eta}). (9) follows.

**V19. L121-L130, (10). HOLDS.** The d = 2 term of (4) is e^{-6s} chi_2(x_p) chi_2(z_p) = 2h(1 - a_p) chi_2(z_p), so q_e^x is (4) truncated at d = 2 with beta a_p clipped at M. Each term has zero integral in z_e because z_p is Haar in z_e. |q_e^x - 1| <= 16h for at most four plaquettes assigned to e, so q_e^x >= 1/2 for small h. The exact conditional minus q_e^x is at most 4h sum_p (beta a_p - M)_+/beta + C e^{-16s} + C e^{-15s/2}. The conditional chi-square bound with denominator >= 1/2, summed over 3N edges, gives C h^2 beta^{-2} sum_p (beta a_p - M)_+^2 + C N e^{-15s}. From E e^{beta a_p/2} <= C_0 one gets E(beta a_p - M)_+^2 <= C e^{-M/2}, so the mean is C(lambda e^{-cM} + N e^{-15s}). The gauge remark at L130 is correct: Z = H_s X has the same joint law with Y as the gauge-randomized reading, by separate gauge invariance at the X end.

**V20. L132-L140, (11). HOLDS.** q_e^x/r_e = 1 + d sum_p g_p(x) T_{e,p} with d = hM/beta and T_{e,p} = -2 chi_2(z_p)/r_e; I checked the algebra. Under R, E[T_{e,p} | earlier edges] = -2 int chi_2(z_p) dz_e = 0, and |T| <= 2*2/(1/2) = 8. Expanding the product over edges gives tuples with distinct last edges and coefficients m(y). Terms with different last edges are orthogonal martingale differences. At one last edge, pointwise Cauchy-Schwarz over at most four plaquettes and |T| <= 8 give a factor 256. Iterating over prefixes gives (C d^2)^k sum |m|^2.

**V21. L142-L146, (12) and the first conclusion of (8). HOLDS.** Tuples: at most (3N)^k/k!; those with a pair within 4b: at most (3N)^k C k^2 b^3/(N k!). With (9) on the rest and |m| <= 1 on exceptional tuples, the order-k term has L^2(R (x) L(Y)) norm at most (C N d^2)^{k/2} k (beta^{-eta} + b^3/N)^{1/2}/sqrt(k!). Minkowski over k and sum_k k v^{k/2}/sqrt(k!) <= (sum k^2 2^{-k})^{1/2} e^v with N d^2 = M^2 lambda give (12). With M = K log(2+lambda), cK > 2: lambda e^{-cM} <= lambda^{1-cK} -> 0; e^{-12s} = lambda beta^2/N gives N e^{-15s} -> 0; exp(C M^2 lambda) = exp(o(log beta)) = beta^{o(1)}, so (12) -> 0. Then L^1 <= L^2, Pinsker for (10), contraction under marginalization and the triangle inequality give TV(L(Z,Y), L(Z) (x) L(Y)) -> 0. Also M <= beta and h -> 0 hold.

**V22. L146, the second conclusion of (8). HOLDS.** With mu = L(Z,Y), nu = L(Z) (x) L(Y) and TV(mu, nu) = eps: TV(mu (x) mu, swap(mu (x) mu)) <= 4 eps since nu (x) nu is swap invariant, and 1 - int sqrt(PQ) <= TV(P,Q). So 1 - A(s) -> 0.

**V23. L148-L153, (13), the conditional mean and variance. HOLDS.** The holonomy of the heat output on a square is X'_p times four conjugated central increments, so E[Re Z_p | X'] = e^{-6s} Re X'_p = h Re X'_p. The bracket has conditional mean (h/beta)(A_p(X') - c_j), and after the prefactor the mean is m^{-1} sum g(A_p(X))(A_p(X') - c_j). Disjoint squares use disjoint increments. Each variance is at most 1 and |g| <= B_1, so the variance is at most B_1^2 beta^2/(m h^2) = 4 B_1^2/lambda -> 0. This needs lambda -> infinity, which is in (8).

**V24. L155, (13), the two limits and the test. HOLDS.** For X' = X the mean tends to E[g(A_*)(A_* - E A_*)] = Cov(min(A_*, B_1), A_*), since E g(A_*) = 0 and c_j -> E A_* by the exponential moment. Positivity is the standard (1/2) E[(f(A) - f(A'))(A - A')] > 0 for f nondecreasing and strictly increasing on [0, B_1], with A_* continuous. For X' independent the mean is exactly zero since c_j = E A_p, and the second moment tends to zero by two-mark asymptotic independence at separation > 4b (from (24) and the Section 12 diagonal, as for (9)) plus the O(b^3/N) near pairs. The threshold test then has both errors -> 0. Traces are gauge invariant, so an extra gauge changes nothing.

## 5. The centre bits and (14) (L159-L172)

**V25. L159, GUIDE. Accurate.** Row 1171 reconstructs a connection from local loop data up to gauge and the three centre flips.

**V26. L161, the conditional sign problem. HOLDS.** Ad x_e fixes x_e up to sign, so every lift is sigma_e r_e. The square products of sigma are sgn Re x_p / sgn Re r_p = 1, so sigma is closed. H^1 of the 3-torus with Z_2 coefficients is Z_2^3, read on the three primitive windings. Given D, the class and Y, vertex-sign lifts are equally likely by gauge invariance of K_t(., y) at the X end. A vanishing plaquette trace has probability zero.

**V27. L163, recovery at small noise. HOLDS.** The readings are sigma_e times i.i.d. signs with error probability q. The decoding error E is a closed cochain, that is a closed mod-2 dual surface. Two error edges in a common primal square are in one component, so each component is closed on its own. A wrong class needs a component with nonzero winding evaluation; it then meets every one of the n^2 parallel straight lines oddly, so its size is k >= n^2. Optimality against toggling that component gives at least k/2 errors on it. A primal edge lies in four squares, so a dual face has 12 neighbours and there are at most 3N 12^{2k} connected sets of size k. The union bound gives sum_{k >= n^2} 3N (288 sqrt q)^k <= C N 2^{-n^2} once 288 sqrt q < 1/2. The lower bound (min w / max w)^{n^2} for one seam flip holds because a seam meets n^2 edges.

**V28. L165, loss at large noise. HOLDS.** The decomposition into the centre-even part min(w(g), w(-g)) and a remainder of mass q_+ is valid, and q_+ -> 0 as s_+ grows. If the class difference restricted to the remainder subgraph is a coboundary tau there, multiplying the vertex signs by tau maps one experiment to the other: on remainder edges the signs agree, and the common part is insensitive. Uniform vertex signs are invariant under this map. A nontrivial restriction needs a winding cycle, which has at least n distinct edges. Counting 6N 5^{n-1} nonbacktracking starts gives C N (5 q_+)^n. The lower bound: the product of reading signs along one straight winding has conditional mean (class value) rho^n, so TV >= rho^n. rho_s > 0 by reflection of spherical Brownian motion in the equatorial hyperplane after the first hit, and positive survival before it.

**V29. L167-L172, (14). HOLDS.** Both lower bounds are monotonicity of the crossed affinity under a channel applied to the two first-slice readings (Cauchy-Schwarz on fibres). For the first upper bound: decode the class, then draw uniform vertex signs; given the correct class this is exactly the conditional law of X given (D, class, Y), by V26. So the reconstructed joint law is within TV eps = C N e^{-c n^2} of L(X,Y). A TV change eps moves sqrt(mu (x) mu) by at most 2 sqrt(eps) in L^2, so the affinity moves by at most 4 sqrt(eps). This is C sqrt(N) e^{-c n^2/2}; the file's form C sqrt(N) e^{-c n^2} holds with c renamed. The second upper bound is the same argument with V28. The closing remark (A_D(infty) - A(0) is not estimated) is accurate.

## 6. (15) (L176-L180)

**V30. L176-L180, (15). HOLDS.** grad_{x_e} V is beta times a sum of four spatial plaquette gradients, each with E|.|^2 <= 2 E a_p <= C/beta. The temporal term 2 beta E[J_e | x,y] has second moment at most 4 beta^2 C/beta by conditional Jensen. So int p |v_e|^2 <= C beta and sum_e ||grad_e sqrt p||^2 = (1/4) sum_e int p |v_e|^2 <= C N beta. Jensen for the Markov operator H_v gives sqrt(H_v p) >= H_v sqrt p. So ||sqrt p_v - sqrt p||^2 = 2 - 2<sqrt p_v, sqrt p> <= 2<(1 - e^{-vL}) sqrt p, sqrt p> <= 2v<L sqrt p, sqrt p> = v sum_e ||grad_e sqrt p||^2, with L = -(1/2) sum Delta_e. Tensoring costs a factor 2 for each of P and Q, so A(v) - A(0) <= 4 sqrt(C N beta v). The lower bound is A' >= 0. Valid on any period and for beta >= 1 (in fact beta > 0) through row 1334 (5).

## 7. The Wilson examples (L182-L188)

**V31. L182, the eight-state example from row 1227 (14). HOLDS.** Row 1227 (14) (`gap-solve25-astra62.md` L170-L178, checked by Claude Opus 5.5 with every statement holding) gives ||U^m - Pi||_1 -> 0 at fixed n >= 3 for m = floor(exp(beta^gamma)), 1/4 < gamma < 1/2, on the full gauge-invariant slice space. The file's gamma = 1/3 is in range. Pi = sum_e sigma_e psi (x) sigma_e psi has kernel 8 psi(x) psi(y) 1{l(x) = l(y)} by character orthogonality on Z_2^3. Trace norm bounds Hilbert-Schmidt norm, and |a^2 - b^2| = |a - b||a + b| with Cauchy-Schwarz gives L^1 convergence of K_t^2/||K_t||_HS^2 to 8 psi^2(x) psi^2(y) 1{l(x) = l(y)}. Each class has psi^2-mass 1/8 by the seam flips. I recomputed the limit crossed affinity: sqrt(PQ) is 64 prod psi^2 times the indicator that all four classes agree, with integral 64 * 8 * 8^{-4} = 1/8. This also matches z_{2T}/z_T^2 -> 8/64. D(X) (adjoints and plaquette signs) is invariant under seam flips, so in the limit experiment it is independent of the class and of Y, and A_D(infty) -> 1. (14) then gives A_D(s_-) -> 1/8 and A_D(s_+) -> 1, so the difference tends to 7/8. A(s_+) >= A_D(s_+) since D(X) together with Z carries more than Z alone. The diagonal choice n -> infinity, beta_n large, is valid because (14) is uniform in beta and the period. The file correctly makes no claim at T = n/2. The tunnelling credit to Luscher and van Baal is appropriate.

**V32. L184, (8) and (13) on n^3 x T' boxes with T' = 4 floor(kappa log n), beta = log n. HOLDS.** The changes to row 1151 (22b) and (24) are the ones needed: the uncovered fraction is C b/T' in place of C b/n. Crossing and boundary terms have density C(1/b + b/T'). The lower comparison costs C(1/b + b/T') log beta per unit volume. Row 1334 (5) on the rectangular torus gives E exp((beta/12) sum_box a_p) <= e^{C b^4}, hence the bad-box bound e^{-c beta/b^8}. With T' of order beta and b = beta^gamma, (b/T') log beta = O(beta^{gamma - 1} log beta) <= beta^{-2 eta}, since gamma + 2 eta < 1. The reflection cuts at b and b + T'/2 still separate the marks, because 2b < T'/2. (10)-(12) depend only on the slice volume N. The adaptation is a sketch, but each replaced term is named and each bound still holds.

**V33. L186, A(0) -> 0 on these boxes, from row 1161 (19). HOLDS.** Row 1161 (19) (`gap-solve9-astra62.md` L264-L271, checked by Claude Opus 5.5 as S25, HOLDS) at k = 1 gives at least M/2 >= c n^3 excited neutral levels with energy at most C, uniformly in beta >= 1. The full trace dominates the neutral count, so z_{T'} >= 1 + c n^3 e^{-C T'} >= 1 + c n^{3 - 4 C kappa} -> infinity when 4 C kappa < 3. Since z_{2T'} <= z_{T'}, A(0) = z_{2T'}/z_{T'}^2 <= 1/z_{T'} -> 0. With V32, int_0^s A' -> 1. The scope sentence is accurate: this shows the mark comparisons and the schedule alone cannot give the bound, not that the physical estimate fails.

**V34. L188, the T = n/2 example from row 1215 (5). HOLDS.** Row 1215 (5) (`gap-solve23-astra62.md` L89-L95, checked by Claude Opus 5.5, HOLDS) gives lambda_j/lambda_0 -> 1 as beta -> infinity at fixed n, for each fixed j, on the neutral periodic space. Choosing beta_n >= n with the first n ratios to the power T above 1/2 gives z_T >= n/2 and A(0) <= 2/n. With u = N^{1/10}: u/beta_n^2 <= n^{-17/10} -> 0 and u^{5/4} N^{-1/4} = N^{-1/8} -> 0, so (7) gives A(s) -> 1. The file correctly uses (7) and not (8) here, and states that beta_n is not logarithmically bounded.

## 8. The reduction (16) and Theorem ZD-c (L190-L205)

**V35. L190-L199, (16). HOLDS (identity); stated under the right coupling range.** I recomputed the window. With s_j as given, e^{-12 s_j} = beta_j^2 sqrt(log beta_j)/N_j, so lambda = N h^2/beta^2 = sqrt(log beta_j) -> infinity and lambda log^2(2 + lambda) = O(sqrt(log beta) (log log beta)^2) = o(log beta). So (8) gives 1 - A(s_j) -> 0. With v_j = (N_j beta_j^2)^{-1}, (15) gives A(v_j) - A(0) <= C sqrt(N beta v_j) = C beta_j^{-1/2} -> 0. Also v_j < s_j for large j. Then 1 - A(0) = [1 - A(s_j)] + int_{v_j}^{s_j} A' + [A(v_j) - A(0)], which is (16). L190 states beta_j -> infinity and beta_j <= B log n_j as hypotheses added to those of Theorem ZD-c. This meets the lead note on ZD-c (`gap-phys-seed.md` L322). The bound for one L in P implies it for every L in P with B changed by o(1), since log n_j changes by a constant.

**V36. Does (16) suffice for Theorem ZD-c? Yes, with these constants and this range.** I checked the chain myself. limsup_j int_{v_j}^{s_j} A'_j < 1/1651 gives liminf A_j(0) > 1650/1651. That is limsup Z(n_j,T_j)^2/Z(n_j,2T_j) < 1651/1650, which is row 1334 (1). Since z_{2T} <= z_T, z_T <= z_T^2/z_{2T}, so limsup_j S_j(L/(2a_j); (L/a_j)^3) = limsup (z_{T_j} - 1) < 1/1650 strictly, with S(T; b^3) = sum_{i >= 1} (lambda_i/lambda_0)^T as in `gap-phys-seed.md` L257. This is (PHYS-SEED) of ZD-c with the two-stage threshold 1/1650 at l = L in P. The constants 1/1651, 1651/1650 and 1/1650 match; row 1336 found the same for the step from (1). ZD-c itself has no coupling condition. The extra range comes only from (8), and L190 states it. An asymptotic-freedom trajectory meets beta_j -> infinity and beta_j <= B log(L/a_j).

**V37. The open target is equivalent to row 1334 (1), not weaker. Finding, no error.** int_{v_j}^{s_j} A'_j = A_j(s_j) - A_j(v_j) exactly. Both endpoints are within o(1) of 1 and A_j(0). So the open inequality at L201-L203 holds if and only if row 1334 (1) holds at the same L on the same trajectory. (16) moves the target to a noise window, where (2) gives a nonnegative integrand. It does not reduce the target. The file does not claim it does: L205 says the bound is still needed.

**V38. L205, the obstacle list. Accurate.** (3) grows as N beta. (12) needs exp(C M^2 lambda) = beta^{o(1)}, so it fails for lambda of order log beta and beyond, and the window [v_j, s_j] reaches lambda(v_j) = N e^{-12 v_j}/beta^2, about N/beta^2, far outside. The examples V31-V34 sit at other periods or couplings, as stated.

## 9. Everything else

**V39. L3, L5, L7, GUIDE.** The claims about row 1336 and Theorem ZD-c match those files. I did not refetch the PR refs 10114, 10133, 10134, 10141 or the Sussman-Alpoge line ranges. Nothing in the proofs uses them. The credits to Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy, and Zeng Chunping are as in row 1334.

**V40. L11, OPEN. Accurate.** The size grid, 4 | n, T = n/2 and the target match row 1334 (1) and ZD-c.

**V41. L13, GUIDE. Accurate.** Spot checks: row 1186 uses the squared-kernel two-slice density (its L322); row 1211 uses wall observations and a chi-square trace (its L278-L292); row 1321 treats replica exchange (its L127-L135); row 1330 uses a spherical heat representation of the Wilson one-link convolution (its L19-L38). The noise here has no physical units, as the file says.

**V42. L95 and L159, GUIDE.** Correct; checked in V15 and V25.

**V43. L207, RESULT line. HOLDS AFTER CORRECTION.** "on logarithmically bounded coupling trajectories" omits the second hypothesis. It should read "on trajectories with beta_j -> infinity and beta_j <= B log n_j". Both are used in (8) and stated at L99 and L190. The rest of the line is accurate. This is a summary line, not a PROVED statement.

## Restatement check

No main PROVED step only restates an earlier row. The squared-kernel density (L17) is row 1171's and is credited. The affinity form of A(0) differs from row 1173 (6), which uses the affinity of the joint law to the product of marginals. The heat-flow derivative (2), the noisy-orbit expansion (4)-(5), (6)-(9) and (13)-(15) are new here. Row 1334 (5) and row 1151 (24) are inputs, cited as such. The open target of (16) is an equivalent form of row 1334 (1) (V37).

## Verdict table (PROVED statements of row 1337)

| # | Lines | Statement | Verdict | Here |
|---|---|---|---|---|
| 1 | 17 | squared-kernel opposite-slice density | HOLDS | V1 |
| 2 | 19-33 | (1), (2), 1 - Z_{2T}/Z_T^2 = int A', threshold 1/1651 | HOLDS | V2, V3 |
| 3 | 35-45 | zero-noise score, (3), A'(0)/A(0) <= C n^3 beta | HOLDS | V4-V6 |
| 4 | 49-53 | heat density bound delta <= C_0 e^{-3s/2} | HOLDS | V7 |
| 5 | 55-61 | (4) | HOLDS | V8 |
| 6 | 63-68 | exact ratio expansion and tail | HOLDS | V9 |
| 7 | 70 | square coefficient | HOLDS | V10 |
| 8 | 72-77 | (5) | HOLDS | V11 |
| 9 | 81-91 | (6), (7) | HOLDS | V12, V13 |
| 10 | 93 | output differs from Haar in the range of (7) | HOLDS | V14 |
| 11 | 99-107 | (8) as stated, input row 1151 (24) | HOLDS | V16 |
| 12 | 109-117 | (9), reflection step | HOLDS | V17 |
| 13 | 119 | size of the reflected product | HOLDS | V18 |
| 14 | 121-130 | (10) | HOLDS | V19 |
| 15 | 132-140 | (11) | HOLDS | V20 |
| 16 | 142-146 | (12) and both conclusions of (8) | HOLDS | V21, V22 |
| 17 | 148-153 | (13), conditional mean and variance | HOLDS | V23 |
| 18 | 155 | (13), limits and test | HOLDS | V24 |
| 19 | 161 | conditional sign problem | HOLDS | V26 |
| 20 | 163 | recovery at small noise | HOLDS | V27 |
| 21 | 165 | loss at large noise | HOLDS | V28 |
| 22 | 167-172 | (14) | HOLDS (c renamed in the first bound) | V29 |
| 23 | 176-180 | (15) | HOLDS | V30 |
| 24 | 182 | eight-state example, row 1227 (14) | HOLDS | V31 |
| 25 | 184 | (8), (13) on n^3 x T' boxes | HOLDS | V32 |
| 26 | 186 | A(0) -> 0 there, row 1161 (19) | HOLDS | V33 |
| 27 | 188 | T = n/2 example, row 1215 (5) | HOLDS | V34 |

Not PROVED-labelled: (16) at L190-L199 holds as an identity under the stated range (V35) and suffices for Theorem ZD-c (V36); the open target is equivalent to row 1334 (1) (V37); GUIDE and OPEN paragraphs are accurate (V25, V38-V42); the RESULT line L207 needs the hypothesis beta_j -> infinity added (V43).

No numeric run was used in this check.

RESULT: row 1337 HOLDS, checked line by line by hand by Claude Opus 5.5; 27 PROVED statements: 27 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL; main finding: the positive integral 1 - Z_{2T}/Z_T^2 = int_0^infty A'(s) ds, (8), (13) and (15) hold, and the reduction (16) holds under beta_j -> infinity, beta_j <= B log n_j (stated at L190, as the ZD-c lead note requires) and suffices for ZD-c's two-stage seed with constants 1/1651, 1651/1650, 1/1650, but its open bound is equivalent to row 1334 (1), so the strict thermal estimate is moved to a noise window and not reduced; the RESULT line L207 should add beta_j -> infinity; no main step only restates an earlier row.
