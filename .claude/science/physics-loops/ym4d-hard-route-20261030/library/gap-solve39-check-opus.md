# Check of row 1323 (gap-solve39-astra62.md), FINISH row 1324

Checker: Claude Opus 5.5, by hand, line by line.
Target: library/gap-solve39-astra62.md (row 1323, by gpt-6.2-astra).
Cited: Theorem ZD-c in library/gap-phys-seed.md and earlier library rows.
Line numbers refer to the target file at the commit checked.

Status: complete.

## Method

I derived each step by hand. I did not trust the labels. A small numeric
guide run checked four constants and two closed forms (listed at the end). It
is a guide only. No verdict rests on it.

Cited inputs. I used these as inputs and did not re-derive them. Each has an
earlier check file whose RESULT line reports that it holds.
- Row 1155, (9) (gap-solve7-astra62.md, L130-134): the Wilson bound (2) with
  c_0 = 1/8. Check row 1156, item 17: HOLDS.
- Row 1151, (23) (gap-solve5-astra62.md, L291-298): the exponential moment past
  deletion, for one orientation and parity class.
- Row 1236, (16) and (21) (gap-solve27-astra62.md): the free-curvature entry
  b(s) and the band limits. Check row 1245: HOLDS.
- Row 1231, (2) (gap-solve26-astra62.md, L34): the joint radius limit. Check
  row 1235: HOLDS.
- Row 1290, (9) and (15) (gap-solve33-astra62.md): the rank-one tree cut and
  the higher-moment bound. Check row 1297: HOLDS.
- Theorem ZD-c (gap-phys-seed.md, L311-320) and the transfer statement (TM) with
  the definition of S(k; B) (gap-crux-restate.md, L33, L45).

## 1. The Wilson comparison (24)

**(16), L190-196. HOLDS.**
H is a spanning tree of the open box plus three wrapping bonds. Its cycle rank
is 3 and its cycles are the three rings. Integrating a leaf vertex gauge against
a mass-one kernel gives 1. On a ring, the inner vertex gauges convolve the n
kernels. The result is c^{*n} at a conjugated holonomy, and
c^{*n}(g) = sum_d d a_d^n chi_d(g). Since |chi_d| <= d,
|c^{*n} - 1| <= sum_{d>=2} d^2 a_d^n. I checked a_1 = 1 and
sum_d d^2 a_d = c_beta(1) = 1/z_beta. With 0 < a_d <= a_2 < 1 for d >= 2 this
gives zeta_n <= a_2^{n-1}/z_beta. I checked a_2 = int cos(theta) c_beta, since
chi_2(g) = 2 cos(theta). So 1 - a_2 = int (1 - cos theta) c_beta. The shell
theta in [beta^{-1/2}/2, beta^{-1/2}] has Haar mass of order beta^{-3/2}. On it
the integrand is at least c/beta, and z_beta <= C beta^{-3/2}. Hence
1 - a_2 >= c/(1+beta). The three ring factors lie in [1 - zeta, 1 + zeta] for
each root gauge. So the kernel lies in [(1-zeta)^3, (1+zeta)^3].

**(17), L198-202. HOLDS.**
Multiplying a temporal plaquette weight by e^{beta(1-w)} erases it. On link e
the normalized kernel c_beta becomes the constant 1/z_beta, that is, Haar of
mass one times 1/z_beta. The one-cut numerator is Tr(K^{T-1} M k_H M). The
two-cut numerator has two such cuts. All other weights are positive. So
replacing k_H by 1 changes each numerator by a factor in
[(1-zeta)^{3j}, (1+zeta)^{3j}], j = 1, 2. With k_H = 1 the cut is
M|1><1|M. The two-cut numerator is then <1|M K^{T-1} M|1>^2, the square of the
one-cut numerator. The z_beta powers cancel. The denominators are Tr K^T and
Tr K^{2T}. The per-step scalars also cancel. So
log M_2 - 2 log M_1 = 2 log Tr K^T - log Tr K^{2T} + O(zeta_n) = Psi(K,T) + O(zeta_n).
The error does not depend on T. This extends the exact rank-one identity of
row 1290, (9). There the cut is exactly rank one. Here it is rank one up to
the ring factor.

**(24), L267-271. HOLDS.**
- The rings are pairwise vertex-disjoint. Direction-1 rings have y, z even.
  Direction-2 rings have x even and z odd. Direction-3 rings have x, y odd.
  Each pair of directions differs in the parity of one coordinate. There are
  (n/2)^2 rings in each direction, so 3n^2/4 in all.
- After contracting the rings, the added edges form a tree. So the only cycles
  of H_many are the rings.
- Leaf step. Take a leaf of the contracted tree that is a ring. Its vertices
  other than the attachment vertex meet only ring edges. Integrating their
  gauges gives c^{*n} at a holonomy conjugated by the attachment gauge. This
  lies in [1 - zeta, 1 + zeta]. After this bound the bridge kernel integrates
  to 1 in the attachment gauge. A vertex leaf gives 1. Repeating to the root
  gives (1 - zeta)^N <= k <= (1 + zeta)^N, N = 3n^2/4.
- The proof of (17) then gives W_many = Psi(K,T) + O(n^2 zeta_n) and
  W_three = Psi(K,T) + O(zeta_n). If beta = O(log n), then
  (n-1)/(1+beta) >= c n/log n. So n^2 (1+beta)^{3/2} exp[-c n/log n] -> 0.
  Hence (24).
- The error is additive and does not depend on Psi. So the closing sentence
  holds too.

## 2. The Gaussian asymptotics (25) and the signed discrepancy (26)

(25) rests on (20)-(23), so I checked those first.

**Symbol and (20), L232-241. HOLDS.**
Symbol. At momentum (k_0, k) put D A = dA from 1-forms to 2-forms. On temporal
components D_{0i,0} = -v_i and D_{0i,j} = v_0 delta_ij. On the range of D,
D*D = (|v_0|^2 + s) I. So P_ex = D D*/(|v_0|^2 + s). Its temporal block is
(|v_0|^2 I + v v*)/(|v_0|^2 + s). Then I - P_ex has temporal block
(sI - vv*)/(s + 2 - 2 cos k_0), as stated. At zero spacetime momentum P_ex = 0.
Splitting. In period 2T, the single-cut block is the average over
k_0 = pi j/T. The cross block carries e^{i k_0 T} = (-1)^j. So A + B is the
average over even j, that is A_P in period T. A - B is the average over odd j,
that is A_A. Restricting to the coordinates S commutes with this. So
G_2 = det(A_P)_S^{-3/2} det(A_A)_S^{-3/2} and G_1 = det(A_P)_S^{-3/2}. This
gives (20).
Positivity. The kernel of A_A is gradients plus H_0, that is, the closed
1-forms. A closed form that vanishes on H must have zero periods on the three
rings. So it is a gradient df with f constant on a spanning tree of H, hence
zero. So both restricted matrices are positive definite.

**(21), L243-248. HOLDS.**
I checked the expansion
1/(2 cosh w - 2 cos k_0) = sum_m e^{-|m| w} e^{i m k_0}/(2 sinh w).
The periodic average keeps the m in TZ, giving coth(Tw/2)/(2 sinh w). The
antiperiodic average gives alternating signs, so tanh(Tw/2)/(2 sinh w). Also
s = 4 sinh^2(w/2), so s/(2 sinh w) = tanh(w/2). On H_0 (s = 0) only k_0 = 0
contributes. So A_P = I/T and A_A = 0. Both vanish on gradients, because
(sI - vv*)v = 0. Since coth(Tw/2) <= coth(w/2), A_P <= I. Clearly A_A <= A_P.

**(22), L250-255. HOLDS.**
The forms see only the cycle space Cyc = Z + H_0, the divergence-free fields.
Coordinate restriction rho: Cyc -> R^S is onto, by routing on a spanning tree
of H. Its kernel is D_H. So zero-extension followed by projection maps R^S
isomorphically onto the orthogonal complement of D_H in Cyc. The Gram factor
of this map is the same for A_P and A_A, so it cancels. D_0 = D_H n Z lies in
Z. The harmonic projections of D_H span H_0, so D_H = D_0 + {h + Rh} with
Rh in Z' = Z - D_0. A vector z + g (z in Z, g in H_0) is orthogonal to D_H
exactly when z is in Z' and g = -R* z. A_P is block diagonal on Z + H_0, with
H_0 block I/T, and A_A vanishes on H_0. So the pulled-back forms are
P' + RR*/T and A'. The parameterization factor cancels. Then
det(P' + RR*/T) = det P' det(I + R* P'^{-1} R/T), using the equal nonzero
spectra of LL* and L*L. This gives (22).

**(23), L257-263. HOLDS.**
Ring flow f_i has <f_i, h_i> = n * n^{-3/2} = n^{-1/2}. So the three harmonic
projections are independent and D_0 = 0. The lift of h_i is sqrt(n) f_i, with
squared norm n^2. So |R h_i|^2 = n^2 - 1, and different directions are
orthogonal. With Z' = Z the transverse factor is
(3/2) * sum over k != 0 of 2 polarizations * log coth^2(Tw/2)
= 6 sum_{k != 0} log coth(Tw/2). P' <= I gives
R* P'^{-1} R >= (n^2 - 1) I, so the harmonic term is at least
(9/2) log(1 + (n^2-1)/T).

**(25), first estimate, L273-278. HOLDS.**
- The Fourier coefficient of f_i at k is n^{-1/2} times the indicator of
  k_i = 0. So sqrt(n) f_i has unit coefficient at every k with k_i = 0. Polarization
  e_i is transverse there, since v_i = 0. Distinct polarizations are
  orthogonal, and A_P is scalar on the transverse space at each k. So
  R* P'^{-1} R is the scalar sum over k != 0, k_i = 0 of 1/a_P(k).
- Lower bound: a_P <= 1 gives at least n^2 - 1.
- Upper bound: tanh(w/2) = (sqrt(s)/2)/sqrt(1 + s/4) >= c sqrt(s), since
  s <= 12. Also sqrt(s) >= 2|sin(k_j/2)| >= 2|k_j|/pi. So a_P >= c ||l||_inf/n.
  A two-dimensional shell has at most 8j points. The sum is at most
  (n/c) sum_{j <= n/2} 8 = O(n^2).
- So the harmonic term is (9/2) log(1 + Theta(n^2)/T) = (9/2) log n + O_{alpha,A}(1).
- Transverse term: w = arccosh(1 + s/2) >= c sqrt(s), so Tw >= c alpha ||l||_inf.
  Also log coth(u/2) <= C_alpha e^{-u} for u >= c alpha. Three-dimensional shells
  have at most C j^2 points. So the sum is O_alpha(1).

**(25), second estimate, L280. HOLDS.**
- G_many >= 0, since A_A <= A_P.
- The flow 4 n^{-3/2} on the n^3/4 edges of the direction-i rings has squared
  norm 16 n^{-3} * n^3/4 = 4. Its inner product with h_i is 1, so its
  harmonic projection is h_i. It lies in D_H.
- The three flows have disjoint supports. So sum c_i F_i lifts h = sum c_i h_i
  with squared norm 4|h|^2. The lift in D_H minus D_0 has least norm. So
  |Rh|^2 <= 3|h|^2.
- A_P >= c/n on Z, so (P')^{-1} <= (n/c) I. So the log det of the harmonic
  factor is at most 3 log(1 + 3Cn/T) <= C_alpha.
- Transverse factor: the pencil ratios of A_P to A_A on Z are coth^2 >= 1. By
  Courant-Fischer, the ordered ratios on Z' are at most the corresponding ones
  on Z. Since all ratios are >= 1, det P'/det A' is at most the full Z ratio.
  The first estimate bounds that.

**(26), L282-287. HOLDS.**
N_many - N_three = (W_many - W_three) + (G_three - G_many). By (24) and (25)
this equals o(1) + (9/2) log n + O(1). The regime is n -> infinity,
beta = O(log n), T/n in [alpha, A]. (24) holds there because (17) is uniform
in T. Per-cut scalars c enter M_2 as c^2 and M_1^2 as c^2, so they cancel. The
closing sentence is a correct reading of (26).

## 3. (27) and (28) with their constants

**(27), L289-294. HOLDS.**
- v is a direction-1 field that is constant in x, so it is divergence-free.
  Its mean is a sum of cos(4 pi m/n) over m = 0..n/2-1. This is zero for n >= 4.
  So v is in Z and supported on H_many, hence in D_0.
- Cofactor identity: det(P restricted to v-perp) = det P * <v, P^{-1} v> for
  unit v. So the ratio of the two quotients is
  <v, A_A^{-1} v>/<v, A_P^{-1} v>.
- Z' lies in Z n v-perp. By the pencil argument of (25), restricting further
  can only lower the quotient. So
  G_three^perp - G_many^perp >= (3/2) log(<v,A_A^{-1}v>/<v,A_P^{-1}v>).
- Fourier content. The product (1+(-1)^y)/2 * (1+(-1)^z)/2 * cos(2 pi y/n)
  has 8 plane waves of equal amplitude. They sit at k_y in
  {+-kappa, +-kappa + pi} and k_z in {0, pi}. They are distinct when n > 4.
  Two of the 8, at (0, +-2pi/n, 0), carry a quarter of the squared norm. All
  are transverse, since k_1 = 0. The other six have w bounded below, so they
  contribute O(1).
- At the low pair, T w/2 -> pi alpha and tanh(w/2) ~ pi/n. So the inverse
  forms grow like n/(pi tanh(pi alpha)) and n/(pi coth(pi alpha)). Their ratio
  tends to coth^2(pi alpha). Hence the liminf is at least
  3 log coth(pi alpha) > 0.
- The condition n > 4 is needed for the 8 frequencies to be distinct, not for
  the zero mean. This does not change the statement.

**(28), L296-302. HOLDS.**
- At k = (2pi/n)(1,1,1) every k_i is nonzero. So a plane wave there has zero
  inner product with each ring flow, which sums e^{i k_i x_i} over a full
  circle. The bridges carry no cycle flow. So the modes at +-k are orthogonal
  to D_H, hence lie in Z'.
- This 4-dimensional real space W is invariant under A_P and A_A. Both are
  self-adjoint, so the compressions to Z' split as W plus its complement in
  Z'. On the complement all pencil ratios are >= 1.
- One polarization gives two real modes, each with ratio coth^2(Tw/2). Times
  3/2 this gives 6 log coth(Tw/2). Both polarizations would give
  12 log coth(Tw/2). So the stated bound is valid but not sharp.
- Constants. sinh(w/2) = sqrt(s)/2 = sqrt(3) sin(pi/n), so
  T w/2 = T arsinh(sqrt(3) sin(pi/n)). This is at most T sqrt(3) pi/n <= sqrt(3) pi/2 < 2.73 < 4
  for T <= n/2. coth is decreasing, so coth(Tw/2) > coth 4.
- coth 4 = 1 + 2/(e^8 - 1). Here e^8 - 1 < 2981 < 6560, so
  coth 4 > 1 + 2/6560 = 1 + 1/3280.
- Binomial: coth^6 4 > 1 + 6/3280 > 1 + 1/1650. So 6 log coth 4 > log(1651/1650).
  The bounds are loose but correct.
- Guide values (not proof): coth 4 - 1 = 6.71e-4. 6 log coth 4 = 4.03e-3.
  log(1651/1650) = 6.06e-4. T w/2 at T = n/2 rises to sqrt(3) pi/2 = 2.72.

## 4. The reduction (29) and the necessary sign (30)

**(29), L306-311. HOLDS.**
- Match with Theorem ZD-c. In gap-crux-restate.md L33 and L45, S(k; B) is
  sum_{i>=1} (lambda_i/lambda_0)^k for the transfer T with Z = Tr T^{n_mu}.
  Its top eigenvalue is simple. The ordinary Wilson torus trace is the trace
  over the whole gauge-invariant space, with every centre sector. Tr K^T
  equals Z up to c^T for every T. Power sums fix the spectrum. So the spectra
  agree up to the scalar, and S_j = Tr U_j^{T_j} - 1.
- (PHYS-SEED) at l = L uses S_j(l/(2a_j); (l/a_j)^3). That is time n_j/2 = T_j
  on the cube n_j^3, with l/(4a_j) an integer. This matches "n_j divisible by
  four" and T_j = n_j/2.
- Bounds. U has spectrum in [0,1] and contains 1. Then
  1 <= Tr U^{2T} = 1 + sum lambda_i^{2T} <= 1 + sum lambda_i^T = 1 + S. So
  Psi = 2 log(1+S) - log Tr U^{2T} lies in [log(1+S), 2 log(1+S)].
- (17) and (24) need n -> infinity and beta_j = O(log n_j). Both are
  hypotheses here. So W_many = Psi(K_j, T_j) + o(1).
- If limsup W_many < log(1651/1650), then limsup log(1 + S_j) < log(1651/1650),
  so limsup S_j < 1/1650. That is (PHYS-SEED) with the two-stage threshold of
  ZD-c, L313. The propagation to all sizes is ZD-c's own step (L320). The row
  does not claim more.

**(30), L313-318. HOLDS.**
- If limsup S_j < 1/1650, then (29) gives
  limsup W_many <= 2 log(1 + limsup S_j) < 2 log(1651/1650).
- In (22) the harmonic term is >= 0. So G_many >= G_many^perp, and (28) at
  T = n/2 gives G_many^perp >= 6 log coth 4.
- Then limsup N_many <= limsup W_many - liminf G_many
  < 2 log(1651/1650) - 6 log coth 4.
- Sign: coth^3 4 > (1 + 2/6560)^3 > 1 + 6/6560 = 1 + 1/1093.3 > 1651/1650.
  So the bound is negative.
- (30) is a necessary condition only. The row states it that way.

## 5. Everything else

**(1), L21-25. HOLDS.** The proof is in L27-31. The commuting claim holds
because D is bi-invariant.

**L27-31. HOLDS.**
- Right convolution by the class measure at angle t acts on V_d as
  chi_d(t)/d = sin(dt)/(d sin t).
- d/dt [sin(dt)/d] = cos(dt). The difference quotients are bounded by 1, so
  this holds weakly on L^2.
- In the unit round metric d(x, xg) = theta(g). Two points of a cap of radius
  r are less than 2r apart. So <f, S_t h> = 0 for 2r < t < pi, and
  W cos(tD) W = 0 there.
- cos(pi D) = (-1)^d. The element -1 acts on V_d as (-1)^{d-1}. So
  cos(pi D) is minus the antipodal map, which moves points by pi > 2r.
- sum_{h=0}^{q-1} cos(2 pi h d/q) = q 1_{q|d}. Each angle 2 pi h/q,
  1 <= h <= q-1, lies in [2r, 2pi - 2r] when r < pi/q. So W qJ_q W = W.
- A plaquette is A U_e^{+-1} B, so its cap is a translate of a cap in U_e.

**L33. HOLDS.** W_i is multiplication by a function of links of p_i. These
include no pivot other than e_i. So W_i commutes with J_j for j != i, and the
product factorizes: W J W = q^{-m} W. The isometry claim follows from
|q^{m/2} J W f|^2 = q^m <f, WJW f>. Gauge and centre invariance hold because
each p_i is contractible.

**(3), L44-55. HOLDS** given (2). The proof is in L57-70.

**L57. HOLDS.** For each mark, L_e and W_e commute with the cosine factors at
the other pivots. So each product splits into 2^s terms L_X O L_Y with
|O| <= 1.

**(4) and its use, L59-70. HOLDS.**
- |L_X K^{k/2}|_{2b}^{2b} = Tr(L_X K^k)^b. Divided by Tr K^{bk}, this is the
  probability that all of X is bad at all b times.
- Markov with (2): this is at most
  C_0^{b|X|} exp(-c_0 beta b sum (1 - cos r)). Take the 2b-th root.
- Hoelder (1/b = 1/2b + 1/2b) and trace Hoelder over the b samples give the
  bound. The 2b normalizers multiply to Tr K^{bk}.
- 1 - cos r_h >= 2 r_h^2/pi^2 with r_h = 2 pi min(h, q-h)/(3q). This gives
  the exponent u min(h,q-h)^2 with u = 4 c_0 beta/(9 q^2).
- Sides times angles give delta_q per mark. The bound
  sum_h e^{-u min^2} <= 2 e^{-u}/(1 - e^{-u}) gives the stated form.

**L72. HOLDS.** P_+ commutes with K, J and W_e. For H >= 0,
Tr(P_+ H^b) <= Tr H^b. Each twisted trace is a positive Wilson integral, so
Tr(P_+ K^{bk}) >= Tr K^{bk}/8. The factor 8 <= 8^{b|X|} for nonempty X.

**(5), L76-84. HOLDS.** Psi(B,b) - Psi(K,T) = 2 log(1+e_1) - log(1+e_2), with
|e_j| <= (1+delta)^{jmb} - 1. Example: q <= beta^{1/4} gives
u >= (4 c_0/9) sqrt(beta). So m b delta_q <= C beta^3 e^{-c sqrt(beta)} -> 0.
b <= beta^2 = O(log^2 T) divides the dyadic T.

**(6), L86-91. HOLDS.** At k = 1, Tr(U^{1/2} L_X U^{1/2})^b is at most
C_0^{b|X|} e^{-c_0 beta b sum} Tr U^b. Also |A| <= (Tr A^b)^{1/b}, and
(Tr U^b)^{1/b} -> |U| = 1 at fixed box. (2) applies to marks at distinct
consecutive times on any period.

**(7) and (8), L93-102. HOLDS.**
- For each term, |U^{1/2} L_X O L_Y U^{1/2}| <= |U^{1/2} L_X| |L_Y U^{1/2}|.
  Bound both factors by (6).
- For larger k, the outer factors U^{(k-1)/2} are contractions.
- With A = q^{m/2} J U^{k/2}, A A* = q^m J U^k J and A* A = U^{k/2} q^m J U^{k/2}.
  Weyl's inequality then gives (8).
- Energy remark. At bounded physical energy, lambda^k >= e^{-E_0 aT}, which is
  bounded below. So the log difference is O(eps_m). Divided by ak = aT/b it is
  O(b eps_m) -> 0.

**L104. HOLDS.** U^{1/2} Omega = Omega. So
|Q_E A_q Omega| <= |Q_E U^{-1/2}| |U^{1/2} A_q U^{1/2}| <= e^{E/2} delta_q.
I checked A_q^2 = (q-2) A_q + (q-1) I directly. The fraction e^u delta_q^2 -> 0.

**(9), L108-113. HOLDS.** The proof is in L115-121. The list corollary is a
union bound.

**(10) and inversion, L115-121. HOLDS.**
- The L_e act on the first end and commute with sqrt(E_y). Cauchy-Schwarz over
  y gives |L_X v| |L_Y v|.
- |L_X v|^2 = Tr(L_X K^{2t})/Tr K^{2t}. Cap radius t/3 satisfies
  2r < t <= pi <= 2pi - 2r.
- 1 - cos(t/3) >= 2t^2/(9 pi^2) gives (10).
- (2/pi) int_0^pi cos(dt) cos(d't) dt = delta_{dd'} for d, d' >= 1. Integrating
  the Gaussian bound gives (C/sqrt(beta))^m.

**L123. HOLDS.** Sum over d' of at most (2w+1)^m values of d, with each
weight at most sup_d p_{d,d'}. Then apply (9).

**(11), L125-136. HOLDS.**
- |p_{d+1} - p_d| <= (2/pi) int t |f(t)| dt <= C_1/beta, by (10) with m = 1.
- Continuation. For G a unit quaternion,
  (1/2) tr(e^{i z sigma_3} G) = g_0 cos z - g_3 sin z. At z = x - iy its real
  part is cosh(y) w(e^{i x sigma_3} G).
- The end link sits in 4 spatial half plaquettes (beta/2 each) and one
  temporal plaquette (beta). So the integrand modulus is at most
  e^{3 beta (cosh y - 1)} times the real rotated integrand. Haar invariance
  then gives E e^{2 y k_z} <= e^{6 beta (cosh y - 1)}.
- The reduced link state commutes with left translations, by gauge invariance
  at the first end and the partial trace. So k_z is uniform on the d weights
  given d. At least floor((d-1)/4) + 1 >= d/4 of them are >= (d-1)/2.
- Markov with y = min(1, (l-1)/(12 beta)) and cosh y - 1 <= y^2 (y <= 1)
  gives exponent -(l-1)^2/(24 beta) or -(l-1)/2.
- The linear-profile sum gives p_d^2 <= (2 C_1/beta) Pr(D >= d).

**(12), L138-143. HOLDS.** Put mu = min(q^2/beta, q) -> infinity. Then
q sum_j p_{jq} <= (C q/sqrt(beta)) e^{-c mu}/(1 - e^{-c mu}). This tends to 0
in both cases mu = q^2/beta and mu = q. The converse limit is (3) with
m = b = 1, since beta/q^2 -> infinity.

**(13), L149-154. HOLDS** given row 1236, (21) and row 1151, (23). The proof
is in L156-162. p^0_beta(1) = 2^{3/2} sqrt(2/pi) beta^{-3/2} = (4/sqrt(pi)) beta^{-3/2}.

**L156-160. HOLDS** given the inputs.
- Joining. C^{1/2} Pi_d C^{1/2} = a_d Pi_d on the link, and Pi_d is
  convolution by d chi_d. So the link kernel d a_d chi_d equals
  c_beta * z_beta d^2 a_d e^X chi_d/d. This is the displayed identity.
- The insertion is a central function invariant under inversion, so T_g is
  self-adjoint.
- Tr T_g^M/Tr U^M is the moment in row 1151, (23). It repeats one temporal
  plaquette column, which lies in one orientation and perpendicular-parity
  class. The bound is e^{C_0 M} with eta <= delta_0 = 1/40. The M-th root gives
  |T_g| <= C. Positive kernel domination gives the tail bound.

**L162. HOLDS** given the inputs.
- Under the law with density pi^{-3/2} e^{-|z|^2}, the weight e^{r^2/2} gives
  2^{3/2} times a standard normal. The sinc is the sphere average of
  e^{i x u.z}. So the limit is 2^{3/2} e^{-x^2/2}.
- a_d -> e^{-x^2/2}.
- z_beta ~ (2/pi) int theta^2 e^{-beta theta^2/2} = sqrt(2/pi) beta^{-3/2}.
- The product over p^0 tends to 1. Y U^{-1/2} is the polar isometry on the
  band.
- Varying test functions are handled by positive kernel domination on compact
  r-sets plus the tail. The subsequence argument is then valid.

**(14), L164-170. HOLDS.** The Q term is (13). Each of the three other terms is
at most (1 + 1/p^0) h^{T/2}. Here
h^{T/2} = exp(-(1+o(1)) T^{2/3}/2) and 1/p^0 <= C_R beta^{3/2} = O(log^{3/2} n).
The eigenvalue claim uses the AA*/A*A identity.

**(15), L172-180. HOLDS** given row 1231, (2), row 1236, (16) and row 1151, (23).
I recomputed the Gaussian step in L182.
- With A = (1/2)[[1, rho],[rho, 1]], the tilt gives (det A)^{-3/2} = 8 (1-rho^2)^{-3/2}
  and covariance Gamma A^{-1}.
- The bare multipliers add the identity: Gamma A^{-1} + I = A^{-1}.
- A^{-1} = (2/(1-rho^2)) [[1, -rho],[-rho, 1]]. So the exponent is
  -2x^2/(1-rho^2) + 2 rho x^2 u_1.u_2/(1-rho^2).
- Dividing by the single-cut product 8 e^{-2x^2} gives (15). The sphere
  average of e^{lambda t} with t uniform on [-1,1] is sinh(lambda)/lambda.
- The result is even in rho, so the sign convention of Gamma_12 does not
  matter.

**L182. HOLDS** given the inputs. The integrand of b(s) is nonnegative times
e^{-s w}, so b is strictly decreasing. The value b(0) = 1/2 also equals the
diagonal of P_ex. Guide value (not proof): a 60^3 sum gives b(0) = 0.49999996.

**L184. HOLDS.** The trial vector Pi_d Omega/sqrt(p) gives the lower bound.
At x = 0 it is (1-rho^2)^{-3/2} > 1. For large x the exponent is
2 rho x^2/(1+rho) minus a log of order x^2.

**(18), L204-213. HOLDS** given row 1290, (15).
- On a spanning forest, leaf integration gives I_F = z_beta^{|F|} at each
  (X, Y).
- Each extra weight lies in [e^{-2 beta}, 1] at each gauge. So
  I_H/I_F lies in [e^{-2 beta r}, 1].
- B_H = I_H B_0. Bounding the numerator and the denominator of L_p in both
  directions gives |L_p(H) - L_p(0)| <= 2 p beta r(H).

**L215. HOLDS.**
- If L_p(H) < c_p beta V/2, then (18) and row 1290 give r(H) >= c_p V/(4p).
- Edges crossing box faces number at most 3V/l < gamma V/2 for l > 6/gamma.
  Deleting an edge lowers the cycle rank by at most one.
- A box has rank at most 3(2l)^3, so at least gamma V/(6 (2l)^3) boxes contain
  a simple cycle of length at most (2l)^3.

**L217. HOLDS.**
- Fundamental characters of disjoint cycles are independent. Each has Haar
  norm one, and unpaired loops integrate to zero.
- Central convolution acts on each fundamental matrix entry by a_2.
- Contractible loops are centre invariant. The trace of a positive operator is
  at least the sum over an orthonormal set of eigenvectors. This gives
  (1 + a_2^{l_p k})^{floor(kappa V)}.

**(19), L223-228. HOLDS.** Per colour E exp(|g|^2/2) = det(I - Gamma_L)^{-1/2}.
A unit vector supported on L has Rayleigh quotient 1 exactly when it lies in
the range of P_ex.

**L230. HOLDS.**
- F = dA supported on L has zero spatial curvature. So A(t) is closed on each
  slice, and F_0 at a cut is a closed form that vanishes on the tree.
- Periods of F_0 are time differences of periods of A, so their sum over the
  b cuts is zero. A closed form zero on a spanning tree is fixed by its three
  periods.
- The converse uses h_t + grad f_t with a constant spatial A and temporal
  potential -f_t.
- So the dimension is 3b - 3. At b = 2 it is 3, so the tree-reset moment is
  infinite. Rings in H force zero periods.

## 6. Does any main step only restate an earlier row?

No.
- (2) is row 1155, (9) quoted as an input under GUIDE. It is not claimed as new.
- (17) extends row 1290, (9). The cut there is exactly rank one on a tree.
  Here it is close to rank one with three rings. The new input is the ring
  convolution bound (16).
- (18) is a short corollary of row 1290, (15).
- (13) applies row 1236, (21) to a test function that depends on d, with a
  tail from row 1151, (23).
- The positive claims (19)-(30) are new. A search of the library finds no
  earlier row with the periodic/antiperiodic determinant split, the coth
  winding factor or the graph H_many.

## 7. Notes that need no correction

- (27): n > 4 is needed for the 8 plane waves of v to be distinct. The zero
  mean already holds at n = 4.
- (28): only one polarization is used. Both give 12 log coth(Tw/2). Also
  T w/2 <= sqrt(3) pi/2 < 2.73, and e^8 - 1 < 2981. The constants 4 and 6560
  are loose but valid.
- The OPEN paragraph (L320) and the closing line (L322) are accurate. The row
  proves no seed. It shows that the Wilson defect on the two winding cuts
  agrees to o(1), while the Gaussian predictions differ by (9/2) log n + O(1).
  So a seed through H_many needs a negative interacting correction of definite
  size, (30).

## 8. Guide run (not a proof step)

A short script outside the repository computed four things. It found
coth 4 - 1 = 6.712e-4, 6 log coth 4 = 4.026e-3 and log(1651/1650) = 6.059e-4.
It found T arsinh(sqrt(3) sin(pi/n)) at T = n/2 to be 2.49, 2.65, 2.72 and 2.72
for n = 8, 16, 64 and 1000. The periodic and antiperiodic averages matched
tanh(w/2) coth(Tw/2) and tanh(w/2) tanh(Tw/2) to 1e-15 at two (w, T). It
found b(0) = 0.49999996 on a 60^3 grid. No verdict above uses these values.

RESULT: 42 PROVED statements checked by hand by Claude Opus 5.5: 42 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL; main finding: the positive claims hold, namely the Wilson comparison (24) (W_three - W_many = o(1) for beta = O(log n)), the Gaussian asymptotics (25) (G_three = (9/2) log n + O(1), 0 <= G_many <= C_alpha), the signed discrepancy (26), (27), (28) with coth 4 > 1 + 2/6560 and T w/2 < 4, the reduction (29) to the two-stage seed of Theorem ZD-c and the necessary sign (30); no main step only restates an earlier row; the row proves no seed, which stays open.
