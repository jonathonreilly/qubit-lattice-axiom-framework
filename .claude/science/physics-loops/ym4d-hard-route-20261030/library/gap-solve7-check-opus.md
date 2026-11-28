# Check of gap-solve7-astra62.md (FINISH row 1156)

Checker: laptop Claude subagent, Claude Opus 5.5 at max effort. Cross-provider
check of row 1155. Started 2026-11-19. Status: complete; written as the
check goes.

## Plan (at most eight steps)

1. Read the setting (`library/gap-council-brief.md`) and the whole file under
   check (`library/gap-solve7-astra62.md`, 540 lines), in ranges.
2. Read the cited parts of rows 1143-1153 and their checks, above all row
   1153's (5) and (24).
3. Check statements (1) and (2) by hand.
4. Check the adjoint-only identity (34) and its support: centre averaging,
   the neutral transfer in the mixed law, the accuracy of the replacements,
   the measure (35), and the recovery steps (27)-(33).
5. Check the comparison-transfer construction (matched moments do not decide
   the count).
6. Check the rest, including the obstructions.
7. Optional numeric guide run (Python -I, under 2 GB). A guide only.
8. Verdict table and the RESULT line.

## Step results

### Step 1 (done): setting and file read

I read `library/gap-council-brief.md` (122 lines) and all 540 lines of
`library/gap-solve7-astra62.md`, in four ranges. Notation used below is the
file's own (line 15): `U = F/||F||`, `E_i = -log lambda_i(U)`,
`g_s = log Tr U^s`, `S(s) = e^{g_s} - 1`, `J_s = 2 g_s - g_{2s}`, `T = n/2`,
`N = n^3`, `t = T/2`. So `e^{-J_T} = Tr U^{2T} / (Tr U^T)^2 = Tr rho_T^2`.

Statement groups, in the order checked:

- A. (1), (2), and the H_d rank bound (lines 17-45).
- B. The adjoint-only identity (34) (lines 494-505) with its support:
  B1 centre averaging (494-505), B2 the neutral transfer in the mixed law
  (507-515), B3 accuracy of the replacements (517), B4 the measure (35)
  (519-526), B5 the recovery steps (27)-(33) (386-490), and the twist
  classifier (29)-(30) (414-433) that (34) uses.
- C. The comparison-transfer construction (172-184, 218-276, 357-384).
- D. The rest: (3)-(26) and the obstructions (47-355, 434-460, 528-538).

### Step 2 (done): cited sources read

- Row 1153 (`library/gap-solve6-astra62.md`): (1)-(8) (L11-136), (13)
  (L224-230), (20)-(24) (L331-399). Its (5) is stated for
  `m^4 eps_beta -> 0` with `eps_beta = beta^{-1/4} [log(2+beta)]^{3/2}`.
  The wider window `m^4 e_beta -> 0`, `e_beta = beta^{-1/4} log(2+beta)`,
  which row 1155 uses at L19, is row 1153 L377 (with (22)-(23)).
- Row 1154 (`library/gap-solve6-check-opus.md`) checked row 1153 by hand:
  items 13 ((4), (5)), 54 ((23) and the wider window at L377) and 55 ((24))
  HOLD. So the input "row 1153 (5)" of row 1155 is checked once.
- Row 1151 (`library/gap-solve5-astra62.md`): Section 7, (19)-(22b),
  (28)-(30), Section 14. (29) gives `J_T <= C_sigma n^3 beta^{-sigma}` for
  every `sigma < 1/16`; (30) is the one-sided pair used in row 1155 (16).

### Step 3 (done): group A, statements (1), (2) and H_d (L17-45)

All by hand. Write `p_s(i) = e^{-s E_i - g_s}`.

- Exponential moment (L25). `E_m e^{u v Y} = e^{g_{(1-u)m} - g_m}`, so its
  log over `v` tends to `c[(1-u)^{-3} - 1]` by (5) at `m` and at the fixed
  dilation `(1-u)m`. Slope `3c` at `u = 0`. HOLDS.
- Tails outside `B` (L25). Chernoff with small fixed `u > 0` (upper) and
  `u < 0` (lower) gives `p_m(B^c) <= e^{-c' v}`. HOLDS.
- (1), upper half. `sum_{Y_i >= x} e^{-T E_i} <= e^{g_m} e^{-(T-m) x v/m}`;
  times `m/(Tv)` this tends to `-x` since `g_m ~ c v` and `m/T -> 0`
  (`m = o(beta^{1/16})`, `beta = O(log n)`). HOLDS.
- (1), lower half. Under `p_s` with `s = m (3c/z)^{1/4}` the variable
  `Y = (m/s)^4 (s E / v_s)` concentrates at `z`, so `(x, x + delta)` holds a
  state of weight `>= exp[-(T/m)(x + delta) v]`. HOLDS.
- Rank of `H_d` (L31-33):
  `|H_d| <= e^{g_{Am}} e^{Am (c+d) v/(T-m)}`, then `A -> infinity`. Complement
  weight `<= e^{g_m - (c+d) v}`. `p_m(H_d)` is between `e^{-g_m}` and
  `e^{o(v)} e^{-g_m}`. HOLDS.
- (2) (L41-45). Lower: the vacuum term is `min(e^{-g_m}, e^{-g_T}) = e^{-g_m}`
  (`g` decreases). Upper: `p_m(H_d) + p_T(H_d^c) <= e^{(-c+o(1))v} +
  e^{-(d+o(1))v}` with `d > c`. Both laws are diagonal in one eigenbasis of
  `U`, so `sum min = 1 - (1/2)||rho_m - rho_T||_1`. HOLDS.

Wording note on L19: the window `m^4 beta^{-1/4} log(2+beta) -> 0` is the
L377 extension of row 1153 (5), not (5) as printed at row 1153 L86-90 (which
has the 3/2 power of the log). Both are checked by row 1154. The narrower
checked-input route via (16)-(17) (L230-248) needs neither; see Step 5.

### Step 4 (done): group B, the adjoint-only identity (34) and its support

Notation: `G = (Z_2)^3`, `R_b` the flat-flip unitary, `P_+ = 8^{-1} sum_b R_b`,
`t = T/2`, `K_t` the symmetric nonnegative kernel of `F^t` on the gauge
quotient, `Z_b = Tr(R_b F^p)`, `theta_b = Z_b / sum_b' Z_b'`.

B2. Neutral transfer in the mixed law (L507-515). Checked each step.
- With the seam after the second slice, the twist-summed unnormalized pair
  density is `K_t(x,y) * 8^{-1} sum_b K_t(y, b x) = K_t(x,y) k_t(ybar, xbar)`.
  The second factor is invariant under separate flips of `x` and of `y`,
  because `K_t(g y, g z) = K_t(y, z)` for `g` in `G`.
- Averaging `K_t(b'x, b''y)` over the two orbits gives `k_t(xbar, ybar)`.
  Also `k_t(ybar, xbar) = k_t(xbar, ybar)` (symmetry of `K_t` plus
  equivariance). So the quotient density is `k_t^2` up to a constant.
- Normalization: `int int K_t(x,y) 8^{-1} sum_b K_t(y, b x) = Tr(P_+ F^T)`.
- On `G`-invariant functions, `P_+ F^t` acts by the kernel `k_t` against the
  pushforward measure. So the square-root operator is
  `P_+ F^t|_{H_+} / Tr(P_+ F^T)^{1/2}`, which is positive semidefinite. Its
  squared norm is `||F||^T / Tr(P_+ F^T)`, because the unique positive vacuum
  is flip invariant. Its rectangle affinity `Tr((K K^*)^2)` is
  `Tr(P_+ F^{2T}) / [Tr(P_+ F^T)]^2`.
- The remark on the untwisted cylinder (L515) is right: its quotient density
  is `8^{-1} sum_b K_t(x, b y)^2`, whose square root is not `k_t`.
Verdict: HOLDS.

B1/B3. The exact identities behind (34), and the replacements (L494-505,
L517). With `p_1(p) = Tr(P_+ F^p)/Tr F^p = sum_b Z_b / (8 Z_0) = 1/(8 theta_0(p))`:
- `e^{-g_T} = ||F||^T / Tr F^T = p_1(T) ||K^exact||^2 = ||K^exact||^2 / (8 theta_0(T))`.
- `e^{-J_T} = A(B^exact) p_1(T)^2 / p_1(2T) = A(B^exact) theta_0(2T) / (8 theta_0(T)^2)`.
Both are exact; I rederived them. The replacements:
- The seam can be moved outside both collars by flipping all slices between
  the old and new seam. This changes the fundamental slices by flat classes
  (quotiented) and leaves adjoint data unchanged. Room exists since
  `r < T/8`.
- In the mixed ensemble `mu_* = sum_b M_b / sum_b (Z_b/Z_0)` the denominator
  is at least one and each `M_b` obeys the tilted bound of L420, so (9)
  holds with a factor 8. The open-draw law of the disagreement given the
  original path (L465-469) does not see the twist. So (32), the
  free-boundary component bounds (L475) and the buffered switch go through,
  and `||B_T - B_T^exact||_TV <= C n^4 e^{-c beta r}`.
- `||sqrt p - sqrt q||_2^2 = 2(1 - H) <= 2 TV`, so the square-root kernels are
  within `(2 TV)^{1/2}` in Hilbert-Schmidt norm. Hence the squared top
  singular values differ by at most `2 (2 TV)^{1/2}` (both kernels have HS
  norm one), and `A` differs by at most `4 TV^{1/2}`.
- (29) gives `|u_p - theta_0(p)| <= C n^4 e^{-c beta n^2}`, and
  `theta_0 >= 1/8`, so `u_p >= 1/8 - o(1)`. The prefactors `1/(8 u_T)` and
  `u_{2T}/(8 u_T^2)` are bounded, so all errors stay absolute.
- With `r = ceil(A(1 + log n/beta))`, `beta r >= A log n`, so
  `C n^4 e^{-c beta r} <= C n^{4 - cA}`; its square root is `O(n^{-k})` once `A`
  is large. HOLDS.
Verdict on (34): HOLDS, given (27) in its open-kernel form, (29) and (30),
all checked below.

B4. The measure (35) (L519-526). For twist `b` and link signs `s`, the
fundamental weight is `exp(beta sum_p alpha_p) exp(-2 beta sum_{p in xi} alpha_p)`
with `xi = D + ds + sigma_b`. As `s` and `b` range, `xi` runs over the sets
with `xi + D` closed and of temporal class, each hit by the same number of
sign cochains (the flat ones). A change of representatives adds an exact
cochain to `D` and permutes the summands. HOLDS.

B5. Recovery steps (27)-(33).
- (27) (L388-401). The coupling logic is sound: the involution
  `(O, O') -> (O c, O' c)` keeps the relative cochain, hence `c`, so it is an
  involution; it exchanges the two plaquette weights exactly on faces with
  `dc = -1` (there `w_p(O') = -w_p(O)`), keeps both adjoint histories and
  the conditional normalizers, and so preserves the joint law. On the good
  event the switched original and the copy differ on the central slice by a
  sign cochain with zero spatial curvature, i.e. a gauge times one of eight
  flat classes. Components are closed because the faces of `B` in one
  3-cube are all in one component and `dB = 1` there. A small component
  fits in a box shorter than a period, and the dual box is contractible, so
  it bounds a dual 3-chain (a link cochain) inside the box. The probability
  bound: a face with `B = -1` has `1 - w_p >= 1` in one of the two paths;
  Cauchy-Schwarz over the `2^k` assignments and (9) give
  `2^k (C e^{-c beta})^{k/2}`. HOLDS.
- (28) (L403-408). Upper bound is (11). The orbit argument is right: a
  diagonal orbit is a fraction `|S_x||S_y| / (8 |S_x cap S_y|) >= 1/8` of
  the product of orbits, a uniform law on a fraction `f` has affinity
  `f^{1/2}` to the uniform product, and concavity covers mixtures. Data
  processing and the `4 eps^{1/2}` continuity finish. HOLDS.
- Sharpness remark (L410). HOLDS (free orbit, shared element: quotient
  affinity 1, full affinity `8^{-1/2}`).
- (29) (L414-424). The estimator is well defined (a change of lift adds an
  exact cochain to `D` and keeps the feasible coset). If the class is wrong,
  `D' + D_true` has a closed component `C` of nonzero class; minimality gives
  `|C cap D'| <= |C|/2`, so `|C cap D_true| >= |C|/2`. A nonzero class pairs
  with a coordinate 2-torus; all its `n^2` (temporal plane) or `n p`
  (spatial plane) translates are homologous, so `|C| >= min(n^2, np) >= n^2/2`
  at `p >= T = n/2`. The tilted bound (L420) and a count of rooted connected
  sets give `C n^4 e^{-c' beta n^2}`, and `sum_b Z_b/Z_0 >= 1`. HOLDS.
- Tilted bound (L420). Moving the twist to `R_b` and using Schatten Hoelder
  (the unitary has norm one) reduces each layer to an untwisted repeated
  pattern bounded by (9). HOLDS.
- (30) (L426-431). `Z_b/Z_0 = Tr(R_b F^p)/Tr F^p`, `|Tr(R_b F^p)| <= Tr F^p`,
  so `theta_0 >= 1/8` and `p_chi = sum_b chi(b) theta_b / (8 theta_0)`. HOLDS.
- Obstruction from decoding error (L433). HOLDS (reweighting by `v_b` in
  `[1, 2]` at most doubles the error).
- (31) and the three readings (L437-452). `h` is uniform given
  `(Y_i, reference)`, since a global flat flip preserves the Wilson law and
  `Y_i` and shifts `h` by its class. The coupling factor is
  `8 1{h_orig = h_copy}`. The switch with `c` = sum of all fillings (both
  colours) of the selected union components gives `dc = B_1 B_2` there,
  swaps the colours, leaves `c` invariant, and gives
  `f(B_1') = f(B_1) c`, `f(B_2') = f(B_2) c` (the `B_1`-fillings inside the
  selection cancel mod two). So both corrected cochains and readings are
  unchanged. On the central slice `f(B_1') = f(B_2)`, so the switched
  original and the copy differ there by a ratio of two flat cochains with
  equal periods: a vertex coboundary. HOLDS.
- Open kernels (L463-477). The open-draw law of `B` given `O` is
  proportional to `exp[-2 beta sum_{p in B} w_p(O)]` on exact cochains (each
  exact cochain has the same number of preimages). Toggling an exact `K`
  gives `P(K subset B | O) <= min(1, exp[-2 beta sum_K w_p(O)])`; with (9)
  this is (32). Components of nonzero class meet all `n(2r+1)` parallel
  spatial 2-tori; their class is a sum of at most three other classes, so a
  union of two to four components is exact and (32) applies to it. Two
  draws: each union component is covered by two exact unions of whole
  components, one of size `>= |C|/2`. Conditioning the comparison on the
  three readings costs exactly a factor eight per collar and its normalizer
  `Z_open(Y)/8` does not depend on the reference or the reading. HOLDS.
- (33) (L479-490). Both equivalences follow from (11), (10),
  `H(Pbar)/8^{1/2} <= H(P_L) <= H(Pbar)` and the TV bounds. HOLDS.
- Lie-group and local-weight obstructions (L454-459). The ideal argument
  for `su(2)` and the quaternion computations are right:
  `Re((uv)^2) = 2 cos^2 theta - 1` for pure imaginary unit `u, v`; the
  frame equations force every `h_i` central. HOLDS.

### Step 5 (done): group C, the comparison transfers (matched moments do not decide the count)

- Reservoir (L174). A tilt at `s = m (3c/z)^{1/4}` concentrates `Y` at `z` for
  any `z > 0` (the intervals need not lie below `3c`); each state has
  probability `<= e^{-g_s}` and `g_s / v -> c (z/(3c))^{3/4} >= c^{1/4} 3^{-3/4}`
  on `[1, 2]`. Different bands differ by `>= e^{-2B}` in eigenvalue for large
  `j`. HOLDS.
- Moment deficit (L176). Removed plus inserted rank is `e^{o(v)}`, each term
  at most one, so `max_s |y_s| <= e^{-gamma v + o(v)}`. The removed tail at `T`
  is `<= e^{-(1+o(1)) v}`. `E_*` and `E_* + (log 2)/T` lie below the cutoff of
  `H_1`. HOLDS.
- Exact matching for fixed `d` (L178). `det A = d! * mean Vandermonde`, all
  terms of one sign and size `>= e^{-2B d(d-1)/2}`; cofactors `<= C_d`; the
  remainder has Lipschitz constant `<= C_d ||t||`; the map is a contraction
  on the stated ball because `||A^{-1}||^2 ||y|| -> 0`. Shifts `<= e^{-gamma v
  + o(v)}`, far below `e^{-2B}`; band weight at `T` is `M (2 e^{-B})^T -> 0`.
  HOLDS.
- Growing `d_j` and the two limits (L180). Diagonal choice of indices.
  First model: `S(T) = n^{-1/2} + o(1)`. Second: `S(T) = n^{-1/2} + n^{1/2}/2
  + o(1)`, `S(2T) -> 1/4`, `J_T = log n - log 5 + o(1)`. `E_*` is the simple
  first level in both. HOLDS.
- Short-period law kept (L182). `log |H_1| <= g_{As} + A s (c+1) v/(T-m)`,
  and the second term over `v_s` is `O(A s^4/(T m^3)) = o(1)` since the window
  has `s^4 = o((log n)^{1/4})`. For `s/m` bounded the shifts move the trace by
  `e^{o(v)}` against `e^{(c+o(1)) v_s}`, `v_s >= c' v`; for `s/m -> infinity`
  the bands contribute `o(1)`. HOLDS.
- Positive realization (L184). `K = sum_{i>=1} (lambda_{i-1} - lambda_i) Q_i`
  has eigenvalue `lambda_{i-1}` on the `i`-th increment (telescoping), kernel
  `>= 1 - lambda_1 > 0` relative to the vacuum measure, and is trace class.
  Conjugation by `psi` keeps positivity and the vacuum. HOLDS.
- Actual first gap (L220-224). `F <= G <= e^{C beta} F` in operator order;
  the cut system has the constant and the traced fundamental plaquette with
  ratio `r_beta^4`; min-max gives `Delta_j <= C(1+beta)` (also row 1153 (13),
  checked). `T Delta_j = O(n beta) = o(v_s)`. The inserted
  `ceil(n e^{T Delta + 1})` levels at `Delta + 1/T` weigh `>= n`. The `X_j`
  version and its dichotomy are right. HOLDS.
- Number of matched moments (L228, L250-260). With `d = beta^alpha`,
  `m = beta^zeta`, `eps = beta^{-gamma} log(2+beta)`: `d = o(m)` needs
  `alpha < zeta`; `d^2 m^4 eps log -> 0` needs `zeta < (gamma - 2 alpha)/4`;
  both possible iff `6 alpha < gamma`, so `alpha < 1/72` for `gamma < 1/12`
  and `alpha < 1/24` for `gamma = 1/4`. HOLDS.
- (16) (L230-236). Upper half of row 1151 (30) at period `u` and lower half
  with `m = u/2` bracket `log Z_u` when `2u <= b`; the `2u` bracket needs
  `4u <= b`. Linear vacuum and per-step terms cancel in `J`, leaving
  `J_u^G = sum log((1 + e^{-u omega})/(1 - e^{-u omega}))`. HOLDS.
- Gaussian derivative bounds (L238-242) and (17) (L244-248). Iterating
  `g_u = (J_u + g_{2u})/2` over `O(log(2+beta))` doublings, each comparison
  error weighs `O(N s eps)`; the terminal term is `2^{-k}(g_H + g_H^G) =
  O((s/H)(N/H^3 + N H eps)) = O(N s eps)` at `H ~ eps^{-1/4}`. The constant:
  `6 (2 pi)^{-3} * 4 pi * sum_h 2/h^4 = (6/pi^2)(pi^4/90) = pi^2/15`. With
  `m ~ beta^{1/100}`, `gamma = 1/16` the error over `v` is
  `m^4 eps log(2+beta) ~ beta^{1/25 - 1/16} log^2 -> 0`. HOLDS.
- Growing bands (L250-258). Upper tail at `s_b - h`, `h ~ tau m/d`:
  `-tau c' v/d^2 + C tau^2 v/d^2 + C N m eps log`, and
  `N m eps log / (v/d^2) = d^2 m^4 eps log -> 0`. Gaps `>= e^{-C'B}` since
  `B/d -> infinity`. HOLDS.
- Conditioning (L260). A cofactor is a mean of alternants equal to
  Vandermonde times an elementary symmetric polynomial (`|e_k| <= 2^{d-1}`);
  the full determinant is a one-signed mean, at least `delta^{d-1}` times the
  same smaller Vandermonde mean. So `|(V^{-1})_{bs}| <= 2^{d-1} delta^{1-d}`
  and `log ||A^{-1}|| <= C d B + O(d) = o(v)`. HOLDS.
- Scope (L262). HOLDS as a scope statement.
- Sharpness of the surface-order endpoint (L266-270). The large multiplet
  gives `J_T = log floor(e^{eta R}) + o(1)` (I rederived
  `2(eta R - log 2 - (1/2) log n) - (eta R - 2 log 2 - log n) = eta R`).
  `g_{m_*} = O(R)`; removed log rank `O(R)` since `m_* v/(T R) =
  m_*^4/(m^3 T) -> 0`; below `c_* m_*`, `g_s >= c c_*^{-3} R - C c_* R`
  dominates all changes; above it the allowed error `N s eps >= (c_*/2) R`.
  HOLDS.
- Lifting (18) (L272-276). `i + 1 <= e^{g_m + m E_i}` limits the lifted set;
  new energies `O(v/T)` stay below the reservoir; the first `k` lifted levels
  stay below `C'(1+beta) l`. HOLDS.
- Symmetry channel (25) (L359-364). Each `Tr(R_gamma U^s) >= 0` by the
  nonnegative kernel; `|Gamma| <= 48 * 8 * N = 384 N`;
  `log |Gamma| = O(log n) = o(v)` and `o(v/d^2)`. HOLDS.
- Analytic symmetric comparison (L366-384). `L_b` is Markov, self-adjoint,
  PSD (`<f, L_b f> = int (int f w q_b)^2 / w_b`), injective (all one-link
  Fourier multipliers of `e^{b x.z}` are positive), trace class (factor
  through `q_b / w_b^{1/2}`), and `L_b -> I` strongly. The pulled-back kernel
  is `Gamma`-invariant and bounded below by `1 - lambda_1`. The sandwich
  converges in trace norm with derivatives, and the inverse function step
  restores the `d` moments and the first eigenvalue. Errors `o(1/T)` give
  `o(1)` trace errors at `T, 2T` (`||X^T - Y^T||_1 <= T ||X - Y||_1` for
  contractions). HOLDS.

### Step 6 (done): group D, the rest (L47-355, L434-460, L528-540)

I read Identity HS1 at `library/gap-global-reform-max.md` L382-390:
`exp(beta t_p) = e^{-beta} int gamma_beta(dw) exp(<w, U_1 U_2> + <w, U_4 U_3>)`
and `exp(<a, b>) = e^{-(|a|^2 + |b|^2)/2} int gamma_1(dz) exp(<z, a + b>)`.
Row 1155's scaled choice `a = s u`, `b = s^{-1} w vbar` has `<a, b> = <w, uv>`
and correction `exp[-(s^2 + |w|^2/s^2)/2]`, which depends on `w` only. Given
the links, `w` has mean `beta(uv + u'v')` and covariance `beta I_4`, and
`z = s u + s^{-1} w vbar + xi` with standard `xi` (completing squares). So
L78, L110, L142-146, L164 and L280-288 use HS1 correctly.

- Selection and factorization (L49-53). A spatial plaquette meets two
  direction-one bonds of opposite parity of `x_2 + x_3`; a temporal
  plaquette holds one bond at two times; `|h_t| <= 4 beta`; the scalar
  `e^{-6 N beta p}` cancels in `J_T`. HOLDS.
- Memory estimate (L55-59). This is Birkhoff's contraction: cross-ratio
  `beta (u - u').R(v - v')`, diameter `<= 4 beta`, coefficient
  `tanh(4 beta/4) = tanh beta`; the tilt bound is maximized at `z = D^{1/2}`
  with value `(D^{1/2} - 1)/(D^{1/2} + 1)`. HOLDS.
- (4) (L61-66). Eigen-density `l` by Cauchy sequences; normalizers within
  `delta_r`; `int l a = lambda`; diagonal between `e^{-delta_p} lambda` and
  `e^{delta_p} lambda`. HOLDS.
- (5) and the range (L68-72). `log tanh beta <= -2 e^{-2 beta}` gives
  `delta_r <= 4 beta n^{-24}`; `delta_p` is small when `e^{2 beta} log n = o(n)`.
  HOLDS.
- Flow inputs (L74). The arithmetic holds: for SU(2) the one-loop law gives
  `beta = (11/(3 pi^2)) log(1/(a Lambda))`, and `11/(3 pi^2) < 11/27 < 1/2`.
  The cited RF10-RF28 lines are external and were not checked here.
  HOLDS (conditional, arithmetic only).
- All spatial columns via HS1 (L78). Fields from HS1 are unbounded but drop
  out of the cross-ratio, so (4)-(5) hold with `|I| = 3N`. HOLDS.
- (6) (L80-86). Double-period auxiliary measure is the product of two
  single-period reference measures; sewing is kernel composition. HOLDS.
- (7) (L88-94). `B = a_B l_B e^{eps}`, `|eps| <= delta_T`, gives the
  replacement with log error `<= 4 * 3N delta_T`; static columns obey
  `sum_{i>0} <= e^{3N delta_T} - 1` by the diagonal comparison. HOLDS.
- Obstruction, fixed seam frame (L98-100). Derivative
  `-beta E_t[(u_+ - u_-).(v_+ - v_-)]`; endpoint fields within `2 beta` of
  `+-4 beta a`, angle `<= arcsin(1/2) = pi/6`; in the cones the product is
  `>= 4 cos 2 theta > 0`. HOLDS.
- Obstruction after seam optimization (L102-108). Every 12-plaquette of `b`
  is `-1`; four chord errors per disjoint plaquette sum to `>= 2`, squares to
  `>= 1`, `c_0 = 1/4`. Crossed minus original pinned products equal
  `-(1/2) sum (|a - g_1 b|^2 + |a - g_2 b|^2) <= -c_0 N`. HOLDS.
- Support of the example (L110). Each spatial link is the first link of
  exactly two forward paths. HOLDS (as stated: no probability lower bound).
- (8) (L114-128). Coupling coefficient `(R^{-1} + C R^{-3/2})|k - k'|`
  (axis rotation `<= |k - k'|/(|k||k'|)^{1/2}`, radial quantile coupling);
  fields `>= 7 beta/4`, angle `arcsin(8/15) < pi/4`; internal component
  `>= (15/4 - 1 + cos(pi/4 + 1/10)) beta > 3 beta`; `alpha = 2/5` gives
  `rho = 1/2`, and `2 rho^i + eps/(1 - 2 alpha)` is a supersolution. HOLDS.
- (9) (L130-134). Halving a marked coupling costs `z_{beta/2}/z_beta <= C`
  with the multiplier ordering; Schatten Hoelder; four direction classes and
  Hoelder with exponent four give `c = 1/8`. HOLDS.
- Pin conditions (L136) and the polylog range (L138). The pin conditions are
  functions of `h_t` and the transports, hence exterior-measurable; their
  failure forces a true witness plaquette (spatial or the temporal one).
  `q_* = tanh(1/4)`; window failure `<= (2 (C l e^{-c_1 beta})^{1/2})^k`, then
  a union over `O(n^4)`. HOLDS.
- Logarithmic range after HS1 (L142-146). Fields `>= 2 A^2 b - C(B)(A+1) b`
  on the retained set; every conditional vector `>= K_0(1+beta) - 2 beta`, so
  the coupling coefficient is `<= 2/5` with no exceptional event. HOLDS.
- (10)-(11) (L150-162). Rectangle of four `F^t` kernels;
  `||F^t||/(Tr F^T)^{1/2} = e^{-g_T/2}`; `pi >= e^{-g_T} psi^2`. Channel
  monotonicity and `|A(P) - A(Q)| <= 4 eps^{1/2}`. HOLDS.
- (12) (L164-168). Given all auxiliaries no spatial coupling remains;
  boundary influence `<= n^{-20}` per side; relative error `e^{O(N n^{-20})}`.
  HOLDS.
- (13) (L188-197). `dQ/dP = exp(beta W + J_T)`; a wrongly sewn plaquette
  contains a vertex whose gauge appears in none of its other three links, so
  the centre element there flips its trace and its mean is zero. Both lines
  of (13), `abar_p = O(1/beta)` by (9), `J_T = o(N)` by row 1151 (29), and the
  second-moment bound by Jensen are right. HOLDS.
- (14) (L199-203). `||A' - A||_HS <= (2 TV)^{1/2}`, trace-norm product
  inequality. HOLDS.
- (15) (L205-214). Density `p_d(x', y) p_d(y', x) e^{-g_T}` relative to two
  vacuum segments; `<k, (P_0^h (x) P_0^h) k> >= (int k)^2`;
  `int p_d^2 = Tr P_0^{2d} = e^{g_{2d}}`; Hoelder gives `int k >= e^{-g_{2d}/2}`;
  `A >= sigma_max^4 >= H^4`. So `-log A <= 4 g_{2d} + 2 g_T`. HOLDS.
- Separate marginals (L216). Cell coupling has `k` singular values `k^{-1/2}`,
  so `A = 1/k`. HOLDS.
- (19) (L280-288). Slice auxiliaries are drawn by a local channel from the
  slice links; the reverse reconstruction has per-link affinity
  `>= exp(-C |k|^2/|h|)`, product `>= exp(-C N beta^2/s^2)`. HOLDS.
- Exact finite table (L290). `(sqrt p_ab) (x) I_k / k^{1/2}` gives `A/k`.
  HOLDS.
- (20) (L294-315). `N/8` disjoint marked plaquettes, selected links
  conditionally independent with fields `<= 6 beta`; angle density
  `<= C (1 + |k|)^{1/2}`; class angles are gauge invariant and differ by at
  most `pi` times the chord sum, so `sum diff^2 <= pi^2 d_G^2`; at least
  `M/2` differences are `<= 4 pi eps_0 / (1+beta)^{1/2}`. HOLDS.
- (21) (L317-322). `rho_T >= e^{-g_T - h} P_{<=h}`, `Tr(rho_T 1_B) = pi(B)`,
  `g_T <= J_T = o(N)`. Row 1153's retained band has `T E_o = o(N)`. HOLDS.
- Seam consequence (L324). HOLDS.
- (22) (L326-334). Holds provided the union-of-balls bound is used with the
  common constant `c_0` (the text says so at L332): then
  `Tr(P_* 1_D P_*) <= e^{c_0 N/4 + c_0 N/4} e^{-c_0 N}`. The trial-function
  version follows from Jensen in the spectral measure. HOLDS.
- (23) (L338-346). Row 1151 (21) with both signs (raising a coupling keeps
  positivity), (22a), Chernoff with `|u| = r/(4 C_1 + 4)`, and the positivity
  comparison. HOLDS.
- (24) (L348-353). With `g_T <= C N beta^{-1/32}` (row 1151 (29),
  `sigma = 1/32 < 1/16`), `r = beta^{-1/100}` (needs `eta > 1/100`, allowed
  since `eta < 1/24`), `0 <= X <= 2 beta`. HOLDS.
- Counting obstruction (L355). Splitting a largest cell keeps every cell
  `>= 1/(2k)`; the projector diagonal is `<= 2k psi^2`; with `gamma = 1/16`,
  `R = N beta^{-3/64} log^{3/4} = o(N beta^{-1/50})`. HOLDS.
- Pressure-route obstruction (L534). HOLDS (elementary).
- OPEN paragraphs (L528, L536, L538) and RESULT (L540). Each is an accurate
  summary of what is proved and what is open. HOLDS as statements of scope.
- GUIDE paragraphs (L3-11, L532). Not checked as proof; external sources
  not fetched.

### Step 7 (done): numeric guide run (GUIDE only, not a proof)

Pure Python with `-I` (numpy is not installed for that interpreter), peak
memory about 16 MB, under one second. Script and output are in the session
scratchpad (`check1156/guide2.py`, `guide2_out.txt`), not committed.

- Toy for (34): state space `G x S` with `G = (Z_2)^k` (k = 3, 2, 1) acting
  freely, `F = I + M M^T / ||M M^T||` with `M` positive and `G`-equivariant
  (so `F` is symmetric, positive, PSD and commutes with the flips). I formed
  the twist-summed pair law of the slices at `0, T/2`, pushed it to the
  quotient `S`, and compared. All three cases agree to 12 digits:
  `e^{-g_T} = ||K||^2/(|G| theta_0(T))` and
  `e^{-J_T} = A theta_0(2T)/(|G| theta_0(T)^2)`. Example (k = 3, T = 4):
  0.401009489024 on both sides of the first identity, 0.176439689022 on both
  sides of the second. The untwisted quotient gives 0.324342951331 instead
  of 0.401009489024, which confirms the remark at L515.
- Same toy: (10) `A(P_L) = e^{-J_T}` to 12 digits; (11) and the two bounds
  of (28) hold (for k = 3: 0.2539 <= 0.6318 <= 0.6333 and
  0.2991 <= 0.6318 <= 0.8460).
- Gas constant: `6 (2 pi)^{-3} 4 pi int r^2 (-log(1 - e^{-r})) dr =
  0.657973626740`, and `pi^2/15 = 0.657973626739`.
- Tilt bound: the maximum of `(z-1)(D-z)/(z(D-1))` equals
  `(D^{1/2} - 1)/(D^{1/2} + 1)` at D = 2, 10, 1000. `q_* = tanh(1/4)`.
- Alternant identity used at L260: Vandermonde with one power removed equals
  Vandermonde times the elementary symmetric polynomial, for all five
  removals at d = 5.
- Second comparison model: `J_T - (log n - log 5)` is 0.040, 4e-4, 4e-6 at
  `n = 1e4, 1e8, 1e12`.
- Constants: `11/(3 pi^2) = 0.3715 < 1/2`; internal field component
  `3.383 beta > 3 beta`; `arcsin(8/15) = 0.563 < pi/4`.

### Step 8 (done): verdict table

Lines are lines of `library/gap-solve7-astra62.md`.

| # | Statement (line) | Verdict |
|---|---|---|
| 1 | Setting, seed test, `e^{-J_T} = Tr rho_T^2` (L15) | HOLDS |
| 2 | (1): band `B`, tails, physical weight rate (L17-25) | HOLDS (wording note on L19: the window is row 1153 L377) |
| 3 | `H_d`: complement weight, rank `e^{o(v)}`, rate `-c` (L27-39) | HOLDS |
| 4 | (2): overlap exponent and trace distance (L41-45) | HOLDS |
| 5 | Selected bonds and factorization (3) (L49-53) | HOLDS |
| 6 | One-column memory estimate, `q = tanh beta` (L55-59) | HOLDS (guide agrees) |
| 7 | (4) (L61-66) | HOLDS |
| 8 | (5) and the range `r` (L68-72) | HOLDS |
| 9 | Range from the flow inputs (L74) | HOLDS (conditional; arithmetic only, external lines not checked) |
| 10 | All `3N` columns via HS1 (L78) | HOLDS |
| 11 | (6) (L80-86) | HOLDS |
| 12 | (7) and the static columns (L88-94) | HOLDS |
| 13 | Fixed-seam obstruction (L98-100) | HOLDS |
| 14 | Gauge-optimized obstruction, `c_0 = 1/4` (L102-108) | HOLDS |
| 15 | Support of the example in HS1 (L110) | HOLDS |
| 16 | (8): pinned chain, one-site coupling, boundary influence (L114-128) | HOLDS (guide agrees on constants) |
| 17 | (9) (L130-134) | HOLDS |
| 18 | Exterior pin conditions and good blocks (L136) | HOLDS |
| 19 | Polylogarithmic range on Wilson exteriors (L138) | HOLDS |
| 20 | Logarithmic range after HS1 (L142-146) | HOLDS |
| 21 | (10) (L150-154) | HOLDS (guide agrees) |
| 22 | Channel monotonicity and `4 eps^{1/2}` continuity of `A` (L156) | HOLDS |
| 23 | (11) (L158-162) | HOLDS (guide agrees) |
| 24 | (12) (L164-168) | HOLDS |
| 25 | Comparison transfers, statement (L172) | HOLDS |
| 26 | Reservoir of true eigenvalues (L174) | HOLDS |
| 27 | Moment deficit and exact correction for fixed `d` (L176-178) | HOLDS |
| 28 | Growing `d_j`, `J_T = o(1)` versus `log n - log 5` (L180) | HOLDS (guide agrees) |
| 29 | Short-period law retained (L182) | HOLDS |
| 30 | Positive, positivity-improving realization (L184) | HOLDS |
| 31 | (13) and the second-moment bound (L188-197) | HOLDS |
| 32 | (14) (L199-203) | HOLDS |
| 33 | (15) (L205-214) | HOLDS |
| 34 | Separate exact marginals do not settle (11) (L216) | HOLDS |
| 35 | Actual first gap retained, `X_j` dichotomy (L220-224) | HOLDS |
| 36 | `d = beta^alpha`, `alpha < 1/72` (checked) and `< 1/24` (L228) | HOLDS |
| 37 | (16) (L230-236) | HOLDS |
| 38 | Gaussian derivative bounds, (17), `c = pi^2/15` (L238-248) | HOLDS (guide agrees) |
| 39 | Growing populated bands (L250-258) | HOLDS |
| 40 | Conditioning of the moment equations (L260) | HOLDS (guide agrees on the alternant identity) |
| 41 | Scope of the comparison (L262) | HOLDS |
| 42 | Surface-order sharpness, `J_T ~ eta R` (L266-270) | HOLDS |
| 43 | Lifting (18) and the rank lower estimate (L272-276) | HOLDS |
| 44 | (19) (L280-288) | HOLDS |
| 45 | Exact finite table at both times (L290) | HOLDS |
| 46 | (20) and the angle density bound (L294-315) | HOLDS |
| 47 | (21) (L317-322) | HOLDS |
| 48 | Seam consequence (L324) | HOLDS |
| 49 | (22) (L326-334) | HOLDS |
| 50 | (23) (L338-346) | HOLDS |
| 51 | (24) (L348-353) | HOLDS |
| 52 | Localization and action do not count states (L355) | HOLDS |
| 53 | (25), symmetry channel (L359-364) | HOLDS |
| 54 | Analytic symmetric comparison, (26) and restoration (L366-384) | HOLDS |
| 55 | (27) (L388-401) | HOLDS |
| 56 | (28) and its sharpness (L403-410) | HOLDS (guide agrees) |
| 57 | (29) and the tilted twisted bound (L414-424) | HOLDS |
| 58 | (30) and the decoding obstruction (L426-433) | HOLDS |
| 59 | (31), the three readings and the switch (L437-452) | HOLDS |
| 60 | Lie-group and local-weight obstructions (L454-459) | HOLDS |
| 61 | Open kernels, (32), free-boundary components, two draws (L463-477) | HOLDS |
| 62 | (33) (L479-490) | HOLDS |
| 63 | (34), centre averaging (L494-505) | HOLDS (guide agrees) |
| 64 | Neutral transfer in the mixed law (L507-515) | HOLDS (guide agrees, including the untwisted remark) |
| 65 | Accuracy of the replacements (L517) | HOLDS |
| 66 | (35) (L519-526) | HOLDS |
| 67 | OPEN remaining adjoint estimates (L528) | HOLDS as a statement of scope |
| 68 | Pressure-route obstruction (L534) | HOLDS |
| 69 | OPEN paragraphs and RESULT line (L536-540) | HOLDS as statements of scope |
| 70 | GUIDE paragraphs (L3-11, L532) | Not checked as proof; sources not fetched |

Notes (not corrections).
- L19 cites "row 1153 (5)" for the window `m^4 beta^{-1/4} log(2+beta) -> 0`.
  Row 1153's (5) as printed (L86-90) uses `beta^{-1/4} [log(2+beta)]^{3/2}`;
  the wider window is its L377 extension. Both are checked (row 1154,
  items 13 and 54).
- L9 says row 1153 is unchecked; row 1154 has since checked it, with every
  statement holding.
- L499 says "the channels of (32)"; they are the open kernels of L463,
  used with (27).
- Not checked: the external lines cited at L5, L7, L74 and L532.
- Independence: this check is by a different provider from the author,
  but it is one reading by hand; the toy runs test the exact identities on
  finite models, a separate data path, and prove nothing.

RESULT: HOLDS - check of row 1155 (`library/gap-solve7-astra62.md`), checked
line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1156,
positive claims first. No statement FAILS and none needs a correction; three
citation notes (L9, L19, L499). In particular: (1) and (2) with the rank
bound for `H_d`; the adjoint-only identity (34), with the twist-summed
neutral kernel `k_t`, the exact relations `e^{-g_T} = ||K||^2/(8 theta_0(T))`
and `e^{-J_T} = A theta_0(2T)/(8 theta_0(T)^2)`, the TV replacement in the
mixed cylinder, the classifier (29), the Fourier relation (30) and the
adjoint measure (35); the recovery steps (27)-(33) including the open-kernel
forms; and the comparison transfers with exactly matched growing-order
Wilson moments (to `beta^alpha`, `alpha < 1/72` on checked input) and both
physical alternatives, also in symmetric analytic form. A toy guide run
reproduces the two exact identities of (34) to 12 digits. These are
reformulations, bounds and obstructions: a cutoff-uniform bound on the
low-energy count, the strict bound `A(B_T) u_{2T}/(8 u_T^2) > 1650/1651`,
(W) and the four-dimensional SU(2) mass gap remain OPEN.
