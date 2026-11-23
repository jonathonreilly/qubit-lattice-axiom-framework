# Check of row 1434: gap-mech-candidate-astra62.md

Checker: Claude Opus 5.5 (line-by-line hand check, exact rationals where computed).
Date: 2026-11-23.

## Plan
1. Equation (2): C_{w phi_m} >= c_m C_1, c_m = 2 I_{m+1}(beta)/beta, lower bound.
2. One-plaquette step: trace nonnegativity, kernel replacement.
3. Rectangle step: spectral representation, weights, Jensen, reorientation.
4. Neutral ensemble: twist reorientation for even m.
5. Obstruction (3), cost bound (5), factor-two bound (6).
6. Sign-change theorem (7)-(10).
7. Separation from the seed via Theorem DOB.
8. Judgement: does it move (M-neutral)? Novelty vs row 1330.
9. Feasibility of next row 2 (signed pilot).

## Findings

Inputs read: the row file in full (246 lines); FINISH rows 1330, 1367, 1386, 1431, 1434 and the rule
"Equivalent is not progress" (FINISH line 350); gap-solve14-astra62 (4) (lines 60-68) and its check S15
(gap-solve14-check-opus lines 45-50, HOLDS).

### Item 1. Equation (2). HOLDS.
- For central h with character coefficients h_k = int h chi_k, Peter-Weyl gives C_h = sum_k (h_k/d_k) Pi_k,
  since chi_k * chi_l = delta_kl chi_k/d_k. C_1 = Pi_0.
- w = exp(beta chi_1/2) = sum_n (beta/2)^n chi_1^n/n!; chi_1^n chi_m has nonnegative integer multiplicities.
  So every h_k of w phi_m is >= 0 and C_{w phi_m} - c_m C_1 = sum_{k>=1} (h_k/d_k) Pi_k >= 0.
- c_m = int w phi_m. With Haar (2/pi) sin^2 theta, chi_m = sin((m+1)theta)/sin theta:
  int w chi_m = I_m(beta) - I_{m+2}(beta) = 2(m+1) I_{m+1}(beta)/beta. So c_m = 2 I_{m+1}(beta)/beta.
- Lower bound: keep the k=0 term of I_{m+1} = sum_k (beta/2)^{2k+m+1}/(k!(k+m+1)!). Gives (beta/2)^m/(m+1)!.
- Exact check (scratch script, guide for the arithmetic only): the ballot multiplicity of V_m in V_1^{(x)n},
  n = 2k+m, equals n!(m+1)/(k!(k+m+1)!) for n <= 30. This is the termwise form of the Bessel identity above.

### Item 2. One-plaquette step. HOLDS.
- Choose time along one direction of p. The row's T = M P (C_E) P M equals TW-T's P M C_E M P, because M and
  C_E commute with P. The temporal plaquette at p is the bond kernel of one spatial link; inserting a central h
  in that factor of the two-slice integral replaces the weight w_p by h (TW-T 3.4 kernel form).
- C_{w phi_m} commutes with the gauge action because w phi_m is central. So the modified step is
  T_h = M P (C_{w phi_m} (x) R) P M, R = the other bond convolutions, R >= 0.
- T_h - c_m T_{p,1} = (PM)* [(C_{w phi_m} - c_m C_1) (x) R] (PM) >= 0. A tensor product of PSD operators is PSD.
- Tr(T^{k-1} D) = Tr(T^{(k-1)/2} D T^{(k-1)/2}) >= 0 for D >= 0, T >= 0, trace class. So
  Z W_m(1,1) - c_m Z_{p,1} >= 0. Here Z_{p,1} uses C_1, i.e. weight 1 at p.
- w <= e^beta pointwise gives Z <= e^beta Z_{p,1}. So W_m(1,1) >= c_m e^{-beta}.
- The row's remark is right: w phi_m changes sign, but its convolution operator is PSD.

### Item 3. Rectangle step. HOLDS.
- T_c = M P_c (C_E (x) I) P_c M with P_c the orthogonal projection onto covariant matrix functions (unitary
  action under tr(A*B)/d_m). C_E commutes with that action. So T_c >= 0 and every nu_l >= 0.
- Tr(T^{k-r} J* T_c^r J) = sum_{i,l} lambda_i^{k-r} nu_l^r |<f_l, J e_i>|^2. Weights
  w_il = lambda_i^k |J_li|^2 / Tr T^k are >= 0. sum_l |J_li|^2 = ||J e_i||^2 = 1 (J isometry; the f_l include
  the charged kernel). sum_i lambda_i^k / Tr T^k = 1. So the weights sum to one and do not depend on r.
- lambda_i = 0 terms vanish because k - r > 0. Then W_m(r,s) = sum w_il (nu_l/lambda_i)^r and Jensen for x^r
  on x >= 0 gives W_m(r,s) >= W_m(1,s)^r. Same in the other direction with s < its period:
  W_m(1,s) >= W_m(1,1)^s. This is exactly the checked S15 argument with D_m in place of the fundamental.
- Closing: the covariant projection inserts D_m of the temporal links at the endpoints; the normalized
  matrix trace gives phi_m(U_C). Correct.

### Item 4. Neutral ensemble reorientation for even m. HOLDS.
- Time = 0: the three 0i stacks are electric; sum over e of Tr(T^k C^e) = 8 Tr(T^k P_+) (TW-T (T5),(F1)).
- Time = j != 0: the 0j stack contains j and goes to the seam (Lemma P of TW-T moves stacks; for even m the
  loop is invariant since D_m(-U) = D_m(U)). The 0i stacks, i != j, are constant along j and are magnetic
  stacks of V_m in the new frame; T_m stays PSD (TW-T (T2)). The one seam bit gives 1 + C = 2 x projection.
- Flips commute with M_m, C_E, P (TW-T (T4)). For even m, J C = C_c J because centre signs on the path act
  trivially in D_m. So the spectral/Jensen argument runs in the projected spaces.
- Mixture: the weights p_{b'} w^{b'}_il with p_{b'} = Z_{b'}/Z do not depend on r. Jensen on the joint index
  gives the inequality for the mixture itself. The one-plaquette step: p lies in a plane through the time
  direction, the magnetic stacks lie in planes not through it, the electric stack is put away from p. Correct.
- Note: TW-T's own header says "checked by no one"; its sources (rows 667/671, 732) are checked. I re-derived
  the parts used here ((T2), (T4), (T5), Lemma P) and they hold. solve9 (3) is checked HOLDS (row 1162, S2).

### Item 5. Obstruction (3), cost (5), factor-two bound (6). HOLDS.
- (3): a central heat law has E D_m(H) = E D_m(H^{-1}) = e^{-t c(m)} I (Schur). Integrate the four noises one
  at a time given (V,t): E_Q[phi_m(V_C)|V,t] = e^{-c(m) sum t_e} phi_m(V_C^base). So |E_Q phi_m| <= e^{-tau c(m)}.
  Under P_b the coarse loop is the fine b x b loop, so E phi_m >= L_m(beta,b^2) for even m.
  -log L_m = b^2[beta + m log(2/beta) + log (m+1)!] = O(m log m) = o(m^2). Contradiction for large even m.
- Pushforward of product Haar under disjoint straight products is product Haar: F_b exists. Correct.
- (4): L_m <= E_Q phi_m <= Pr(S<u) + (1 - Pr(S<u)) e^{-u c(m)}. Rearranging gives (4). The mixture bound for
  epsilon follows the same way. Correct.
- (5): squares with base points even in directions 1,2 have pairwise disjoint edge sets (checked the wrap:
  the top row index 2c+1 <= N-1). K = floor(N1/2) floor(N2/2) N3 N4. Given (V,t) the X_i depend on disjoint
  noise sets, so they are conditionally independent. Conditional mean <= h_m. For X in [-1,1] the tilted
  variance is <= 1, so log E e^{theta X} <= theta mu + theta^2/2. Jensen under P_b and P_b <= D Q give
  theta K l_m <= log D + K(theta h_m + theta^2/2). theta = delta gives log D >= K delta^2/2. The
  Donsker-Varadhan form gives the same bound for relative entropy. l_m <= L_m on the band: correct.
- (6) upper half: the four chosen links (two collinear on each of two opposite sides, rows 2 apart, period >= 4
  so also >= 2 apart around the torus) share no plaquette. So their conditional laws factor. Each is
  exp(z Re tr(US)/2)/Z with z = |sum of six signed staples| <= 6 beta (matches gap-seed-astra62 g_h, |h| <= 6beta).
  The matrix mean of D_m(U) and of D_m(U^{-1}) is (I_{m+1}(z)/I_1(z)) times a unitary. Termwise
  (k+m+1)!/(k+1)! >= (m+1)! (exactly checked for k,m < 40, and true in general) gives
  I_{m+1}/I_1 <= (z/2)^m/(m+1)! <= (3beta)^m/(m+1)!. |tr X|/d <= ||X||. So the upper half holds.
  The squeeze -log W_m(2,2)/(m log m) -> 4 holds uniformly on compact beta bands.
- Wilson-noise remark: per-edge multiplier I_{m+1}(g)/I_1(g) <= (g/2)^m/(m+1)!, product (prod g/16)^m/((m+1)!)^4;
  comparing with the lower half for all even m forces prod g >= beta^4. Correct.

### Item 6. Sign-change theorem (7)-(10), and (11). HOLDS.
- (8): the 2b chosen links on the two horizontal sides share no plaquette (rows b >= 2 apart; period >= 2b
  gives >= b >= 2 the other way). Same argument as (6). Holds for all m, both ensembles.
- f = sum a_m chi_m, a_m = d_m W_m(b,b); uniform convergence by (8); identification by density of character
  polynomials (Chebyshev U_m on [-1,1]). Correct.
- (9): |a_m| chi_m(z) <= (m+1)^2 [(3beta)^m/(m+1)!]^q z^m <= [(3beta z^{1/q})^m/m!]^q, using
  (m+1)^2 <= (m+1)^q for q = 2b >= 4. Sum of q-th powers <= (sum)^q gives e^{3 q beta z^{1/q}}. Correct.
- (10): the R-marginal of V_C is f e^{-gamma phi_l}/Z_R because the removed factor depends on V_C only.
  Majorant series with |a_m| and +gamma, nonnegative multiplicities, chi_j(z) > 0 for z >= 1: absolute
  convergence, so regrouping is legal; at z = 1 it gives uniform convergence on the group, so the regrouped
  coefficients are the B_m. Limit: e^{3q beta z^{1/q}} e^{-gamma z^l/(l+1)} -> 0 since l >= 1 > 1/q. Correct.
- Sign step: B_0 = 1. Finitely many nonzero: a nonzero Laurent combination tends to +-infinity or is the
  constant 1. Eventually >= 0 with infinitely many nonzero: a positive term of degree above all negative ones
  dominates (chi_m(z) >= z^m), so the sum -> +infinity. The mirror case -> -infinity. All contradict (10).
  Even l: chi_m(-z) = (-1)^m chi_m(z); averaging z and -z keeps the exponential and the bound (9). Correct.
- Real-group remark and (11): correct (Z_R >= e^{-gamma}; (m+1)/2^m decreasing; chi_m(2) >= 2^m).

### Item 7. Separation via Theorem DOB. HOLDS, with one small precision.
- DOB (18) (gap-vmf-lip.md 438-516; Lemma DC, INF and the chord form checked HOLDS in gap-vmf-lip-check-opus):
  log(1+S(a;B)) <= Phi_B(a) <= 96 a |B| beta q^{floor(a/2)-1}/(1-q), q = 9beta/2 < 1, integer a >= 3, sides >= 3.
  With |B| = n^3, a = t_j = 2 floor(n/1024): the right side -> 0. S_0 <= S (DOB "Both halves") gives
  s_j(t_j) <= S. Also a = n/2 gives the two-period defect -> 0.
- Precision: DOB needs a >= 3, so t_j = 2 floor(n_j/1024) >= 4 needs n_j >= 2048. "Eventually" covers it.
- Scope (stated by the row): fixed beta < 2/9 is a comparison trajectory, not the prescribed band. The
  separation shows only that the heat premise is not necessary for the seed inequality. I did not check the
  definition of (W) against this use.

### Phase-1 filter line (t1). HOLDS.
- Conjugation by i sigma_z reverses the sigma_x axis, so a b a^{-1} = b^{-1}; the commutator b^{-2} =
  exp(-i pi sigma_x/3) is not +-1. (Quaternion product checked in the scratch script.)

### Other lines checked
- Group and dimension paragraph: U(1) coefficient I_m(beta) >= (beta/2)^m/m!; SU(3) coefficient of the
  all-conjugate term (beta/6)^m/m! times multiplicity >= 1 of Sym^m-dual in the m-fold conjugate power, divided
  by dim C(m+2,2). Correct. The SU(3) open-line transfer and the Casimir growth I accepted at outline level only.
- Heat equation for log F: d/ds log F = sum a_e (Delta_e log F + |grad_e log F|^2). Correct; no sign is claimed.

### Scope remark on (5) (not a defect in the proof)
- delta = l_m - h_m <= l_m, and m must satisfy tau m(m+2) > -log l_m. So delta is tiny when tau is small.
  Float guide (b = 2, band [2, 513/256]): tau = 1 needs m = 6, log l_m ~ -42; tau = 0.25 needs m = 48,
  log l_m ~ -586; tau = 0.05 needs m = 400, log l_m ~ -8034. The cost K delta^2/2 is then negligible
  against any lattice volume unless K > delta^{-2}. So (5) is extensive but with a coefficient of order
  exp(-c (1/tau) log^2(1/tau)). It does not obstruct an approximate extraction with a small or slowly
  shrinking floor. The row itself says row 1330's positive error is outside (3).

### Item 8. Judgement. Closes a class; does not move (M-neutral).
- Every proof in the row holds. But the content is the high-spin tail of the bare Wilson weight. Lower bound
  (1) is a rigorous version of the leading strong-coupling character term, [I_{m+1}/I_1]^{area}-like
  factorial decay, and (6) shows the factorial power is the area. A heat factor needs Gaussian decay
  e^{-tau m(m+2)}. Factorial decay is slower. So (3) is the expected statement: a Wilson-type law has no exact
  heat-kernel factor. (7)-(10) is the same fact read through the Laurent continuation: a density whose
  continuation is of order 1/q cannot be divided by e^{gamma phi_l} with a one-sign coefficient sequence.
- ARGUED by the checker: the obstruction depends on the bare action. With the heat-kernel action
  w = H_{t0}, (2) holds with c_m = e^{-t0 c(m)}, the lower bound (1) becomes Gaussian, roughly
  e^{-b^2 t0 c(m)} up to the e^{-beta}-type factor, and no contradiction follows for tau below about b^2 t0.
  So (3) is a property of the UV action's tail, not of the continuum theory. This is why it holds alike for
  U(1), SU(3) and 5D, as the row says.
- Under the rule "Equivalent is not progress" the row is honest: it claims no candidate and no gain. The
  separation via DOB is valid. Nothing here is a step toward (M-neutral); it closes the narrow class of
  exact independent heat factors with a positive floor (and one-sign coefficient control after one
  single-character extraction). Nobody on file used that class as an exact identity.
- Relative to row 1330: new but small. Row 1330 extracts an approximate heat factor on fine temporal links
  with relative error eps_R = 8 exp(-beta (R-1)^2/2) on a subprobability; row 1434 addresses an exact
  identity on coarse straight-product links. Its quantitative parts (4) and (5) bound the needed error from
  below, but, by the scope remark, the bound is super-exponentially small in 1/tau. It does not touch
  row 1330's route. The factor-two sharpness (6) and the sign theorem are new statements on file but of the
  same expected kind.

### Item 9. Next row 2 (signed pilot 12^4 -> 6^4 -> 3^4). Not feasible as a rigorous computation.
- g(F) = 4 int phi_1(V_C) log F(V) dV needs log of the exact pushforward density F of the 12^4 Wilson law
  (82944 SU(2) links) on 6^4 x 4 = 5184 coarse links, pointwise, then a second pushforward. At beta ~ 2 no
  convergent expansion is available (DOB-type and cluster bounds need beta < 2/9 here), and there is no
  finite exact representation of F or log F. Exact rationals or Lean cannot reach it. Monte Carlo estimates
  of log-density projections need free-energy-type estimators and would only guide. The thresholds (log 2)/4
  would have to be certified at three-place accuracy in a crossover region. I see no rigorous route.

## Verdict
HOLDS. Items 1-7: every checked step holds; no correction needed. One precision: the DOB step needs
t_j >= 3, i.e. n_j >= 2048 ("eventually"). Judgement: a valid but expected class obstruction tied to the
factorial tail of the bare Wilson weight; it does not move (M-neutral) and does not touch row 1330.
Next row 2 is not feasible rigorously.

Not checked: the SU(3) transfer and Casimir details; the definition of (W) used in the separation; the
GL3 and SA outline citations (not opened); the repo-search claims; TW-T was re-derived only for the parts
used, not checked as a whole; the heat-kernel-action counterpoint in item 8 is argued, not proved.
