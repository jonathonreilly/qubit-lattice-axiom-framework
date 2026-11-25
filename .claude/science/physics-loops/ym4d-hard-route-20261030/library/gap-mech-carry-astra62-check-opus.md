# Check of library/gap-mech-carry-astra62.md (FINISH row 1540)

Checker: Claude (Opus 5.5). Target: row 1536 (author gpt-6.2-astra max).

## Plan
1. Read GOAL.md, FINISH.md (Rules, Working efficiently).
2. Read the target note in full; read row 1530 note and check 1535.
3. Check Theorem 3 (7) first (decisive), then carry (5), selectivity, Theorem 1 and m(H),
   Theorem 4, same-aspect separation at beta_* = 1/25600 vs row 708, spectator comparison,
   (R) and attainment, comparison with (PUR-io), novelty vs rows 1380, 1386, 1442, 1527.
4. Verdicts and RESULT line.

## Progress log
- step 1 started.
- step 1 done: read GOAL.md, FINISH.md Rules and Working efficiently; FINISH rows 1380, 1386, 1442, 1527 (RESULT text), 1536, 1540.
- step 2 done: read library/gap-mech-carry-astra62.md in full (189 lines), library/gap-mech-attack-astra62.md in full, check 1535 in full. Lane checkout commit 023d22c5d.
- step 3 in progress: Theorem 3 first. Working notes (Theorem 3): r_N fine radius h r_N in (u/16,u/8] checked (u = n/512). Coarse pin (Gram-matrix minimum, |(I-Ad g)a|^2 = 4|u x a|^2, Pr(|u x a|<=s) = s^2 under Haar, two-case exposure) checked. (8) from pins: telescoping and path bound checked; exponent k^4 (delta^-1 + k) <= C (log N)^(5/2) checked. ||D_r|| <= 3 r^-2 gamma^-2, X_r <= 12 ||D_r||^2 checked; (9) and the level sum checked.
- step 3 continued: inputs read: library/gap-solve2-astra62.md lines 15-40 (row 1145 (1)-(3)) and its check verdict (gap-solve2-check-opus.md: (1), (3) HOLD); library/gap-mid-max.md Corollary TR1, Proposition Delta, Identity FL, notation (lines 38-42, 144-156, 219-223); gap-mid-check.md §3 (TR1 HOLDS, 0.0101 re-derived); gap-transfer.md (2c), (4b), (4d) (T_P >= 0, simple top eigenvalue, positive ground state); check 1527 STIFF-TO-HELL paragraph (lines 114-116). Library grep for first-layer score regression and bridge-exchange parity: only hits outside this topic (row 1321's replica exchange is a different object).
- step 4: all parts checked; verdicts written below.

---

Provenance: Claude (Opus 5.5), laptop subagent, check by reading at lane checkout 023d22c5d, 2026-11-25. Cross-provider (author gpt-6.2-astra max). Not an audit. Hand check only: no numerical run, no Lean. Inputs taken as checked: row 1141 (2)-(7) as used in check 1535; row 1145 (1)-(3) (check gap-solve2-check-opus.md: HOLDS); row 708 Corollary TR1 entrance (check row 709, gap-mid-check.md §3: HOLDS); gap-transfer.md (2c), (4).

## Decisive outcome: Theorem 3, (7) -- HOLDS

Line by line:
- r_N = 2^floor(log2(N/4096)) lies in (N/8192, N/4096], so h r_N lies in (n/8192, n/4096] = (u/16, u/8] with u = n/512. HOLDS.
- Coarse pin. For g = t + u, Ad g is a rotation by 2 theta about u/|u| with |u| = sin theta, so |(I - Ad g)a|^2 = 4 sin^2 theta |a_perp|^2 = 4|u x a|^2. Sum over the two loops = 4(tr G - a^t G a), G = u1 u1^t + u2 u2^t; the minimum over unit a is 4 x (smaller nonzero eigenvalue) = 4 x lambda_min of the 2x2 Gram matrix. lambda_min >= det/trace = |u1 x u2|^2/(|u1|^2+|u2|^2) >= |u2 x u1hat|^2/2 when |u1| >= |u2|. HOLDS.
- Haar: |u x a|^2 is the squared radius in a fixed coordinate 2-plane of R^4, uniform on [0,1] on S^3; Pr(|u x a| <= s) = s^2. HOLDS. Conditional density of g_2 given all other fine links: one private fine link, tilt e^{k.x}, |k| <= 6 beta (seam signs keep the norm), max density <= C(1+kappa)^{3/2}; left/right multiplication and inversion preserve it. The opposite length ordering is covered by exposing a private link of the first loop with g_2 fixed. Both cases give probability <= C(1+6 beta)^{3/2} delta/2; with delta = c(1+6 beta)^{-3/2} the failure probability is <= 1/2 given any sigma-algebra not containing the two private links. Distinct 3-cells have disjoint coarse edges, hence disjoint fine links. HOLDS.
- Depth h <= sqrt n: N >= sqrt n, beta_K ~ log n <= C(1+log N). HOLDS. Depth h > sqrt n: row 1145 (3) applies (h >= 5; interior links of distinct coarse edges share no plaquette; selected tilts have s <= 6 beta for every seam sign); joint density of the 4 V_c coarse links relative to coarse Haar <= (1+eta)^{4V_c}, eta <= C exp(-(h-2)/(1+6 beta)); (h-2)/(1+6beta) >= sqrt n/(C log n), so 4 n^4 eta -> 0 and the factor is <= 2 at large K. The bad event is a function of the coarse links, so its Wilson probability is <= 2 x its coarse-Haar probability, where the pin holds with fixed delta. HOLDS.
- Boxes: intervals of length in [k, 2k], k = ceil((D log(2+N))^{1/4}); v/h >= N/512 > 2k at large N; >= c k^4 disjoint 3-cells per box; P(no pin) <= 2^{-c k^4}; <= N^4 boxes; total <= C N^{-8} for D large. HOLDS.
- (8): telescoping round each pin loop, |(I - Ad g_i) f_x|^2 <= 4 sum of |Df|^2 on its four bonds; loops edge-disjoint, so delta |f_x|^2 <= 4 E_B. A box path of length <= 8k gives |f_y|^2 <= 2|f_x|^2 + 16 k E_B. Sum over <= 16 k^4 sites and over disjoint boxes: ||f||^2 <= C k^4 (delta^-1 + k) <f, L f>. With delta^-1 <= C(1+log N)^{3/2} and k^4 ~ D log N: L >= c(1+log N)^{-5/2}. HOLDS.
- (9): D_r = 3a(L+a)^{-1}(L+4a)^{-1} gives ||D_r|| <= 3 r^{-2} gamma^{-2} <= C r^{-2}(1+log N)^5. X_r <= (1/2V_c)||M||^2 Tr(I_2 x D_r)^2 <= 12 ||D_r||^2 <= C (1+log N)^{10} r_N^{-4}, r_N >= N/8192. Off the good event the deterministic 4D bound X_r <= C r^{4-d} = C (checked below) times C N^{-8}. Both bounds are uniform in |xi_x| <= 1, so an axis field reading the whole sample is covered. HOLDS.
- (7): E sup over levels <= sum over levels; N = l b^{K-j} runs over a geometric sequence, so sum over N >= M of C(1+log N)^{10} N^{-4} + C N^{-8} -> 0 as M -> infinity, uniformly in K, v, z. A level chosen from the sample is covered by the sum. HOLDS.

Scope (not a defect): the mechanism is a spectral gap gamma >= c(1+log N)^{-5/2} of the coarse covariant Laplacian, far above r_N^{-2} ~ N^{-2}. The same proof works in five dimensions and for any action with a bounded one-link conditional density. So (7) is a dimension-blind negative. It is the straight-blocked form of row 1530 (5) and settles, for straight products, the case that row 1530's stopping statement left open ("successively renormalized fields").

## Theorem 2, the carry (5) -- HOLDS (range nonempty only for beta >= (8 r_0)^32)

- Action estimate: restricting all 4 V_f links to chord radius beta^{-1/2} gives F(beta) <= 6 V_f log beta + C V_f + 6 beta n^2 (positive faces <= 8/beta each; at most 3 n^2 negative faces, <= 2 each). F concave, F(0) = 0, so E A = F'(beta) <= F(beta)/beta; divided by V_f = n^3 v this gives C a_beta. HOLDS.
- Translation invariance of E d_f^2 within an orientation: flipping the i-links at time t+1 with fixed x_i moves a 0i stack from t to t+1 (each ij face at that time contains two flipped links; each affected 0i face contains one); flipping temporal links at fixed t and x_i = c+1 moves it in x_i. Haar and all Ad transports are preserved. d_f^2 = 4(1-w^2) <= 8(1 - sigma w). HOLDS. (6): a coarse face is a product of h^2 conjugated fine face rotations, so ||I - Ad V|| <= sum of d_f; Cauchy-Schwarz gives C h^4 a_beta. HOLDS.
- Good cubes: about 6 q^4 internal faces, Markov at q^{-3}: C q^{10} h^4 a_beta; sum over h = b^j <= beta^{1/8} gives C_b q^{10} beta^{1/2} a_beta <= C beta^{-3/16} log beta -> 0. Strips: C q h/v -> 0. HOLDS.
- Root curvature: tilt normalizer >= c e^kappa (1+kappa)^{-3/2} (ball of chord radius (1+kappa)^{-1/2}), so density <= C(1+kappa)^{3/2}; Haar mass of {|Im g| <= t} <= C t^3; with t = tau/sqrt(1+beta) the product is <= C' tau^3. The successive conditioning and (9/(8 sqrt 2))^M bound are as in check 1535. HOLDS.
- Lower estimate: root-comb errors <= d q^{-2} <= C r^{-2} for r <= q/8; ||L psi|| <= C r^{-2}||psi|| on the bump span; D_r^{-1} form <= C a; D_r >= c r^2 P; monotonicity of Tr(B M C M); block trace 16 |xi_root|^2 >= 16 tau^2; at least c V_c/r^4 bumps. X_r >= c tau^2. HOLDS. h = 1 with q = floor(beta^{1/16}): q^{10} a_beta -> 0. HOLDS.
- Deterministic upper estimate: D_r^2 <= 9a^2(L+a)^{-4}; heat-walk domination by 3 x the free trace; ball C r^{8-d}, annuli C(2^k/r)^{d-8}, zero mode included; times a^2: C r^{4-d}. HOLDS for d = 4, 5.
- Fine radius h r <= beta^{1/8} beta^{1/32}/8 = beta^{5/32}/8. HOLDS.
- Wilson-observable claim (gauge rotation of the root axis, seam change multiplying the coarse face and sigma_square by one sign, Ad unchanged). HOLDS.

Scope: (5) needs q = floor(beta^{1/32}) >= 8 r_0, so beta >= 8^32 (about 8 x 10^28) even at r_0 = 1, i.e. n >= exp(10^28) on beta ~ log n. Physical size: beta^{5/32} a_K -> 0. As in check 1535, (5) is a small-field ultraviolet statement. It does not escape Proposition NEG (a) or Remark STAB of row 1386.

## Selectivity -- HOLDS, as in check 1535

- U(1): the bracket is zero, so M_xi = 0 and X_r = 0 for every configuration. HOLDS, trivially; it is built into the observable.
- 5D: X_r <= C/r for every blocked configuration, every |xi| <= 1, each twist at the same aspect (deterministic count above; zero mode r^4/V_c <= C/r). HOLDS. The same lower-bound proof gives c/r in 5D, so the 4D/5D split is the free mode count r^{4-d}. The Wilson law supplies only that most q-cubes are near pure gauge.

## Theorem 1 and m(H) -- HOLDS

- (2): with E_Q Y = 0, inf_a E_Q(S - g - aY)^2 = Var_Q S - (E_Q SY)^2/E_Q Y^2; total variance gives the integrand = J + E_p inf_a(...). HOLDS. The consumer direction: B^2(A,A') = sqrt(k_A k_A') <sqrt p_A, sqrt p_A'>, Tr B^2 = Z_+(u), ||B^2||_HS^2 = Z_+(2u), P_K = E <,>^2; ||d sqrt p/ds||^2 = Var_p g = J; chord^2 <= int J; Jensen. HOLDS.
- (3): each spatial link at time 0 lies in exactly one temporal plaquette of the slab; that plaquette contributes beta <A_e, L_e X_{1,e} R_e>, so S = s_0 + beta sum_e t_e . X_{1,e}, |t_e| = |Adot_e|, t_e fixed by temporal and projection variables (twist signs change only the sign of t_e). HOLDS.
- One-link variance: marginal of one coordinate on S^3 is proportional to sqrt(1-t^2); y = kappa(1-t); for kappa >= 8, [1,2] and [3,4] have probability >= c, so Var t >= c/kappa^2; transverse coordinates variance E(1-t^2)/3 >= c/kappa, mixed covariances zero; for kappa <= 8 density >= e^{-16}. Var(a.x) >= c|a|^2/(1+6 beta)^2. HOLDS. A slice-1 spatial link lies in 2 temporal and 4 spatial plaquettes (w >= 2), so kappa <= 6 beta. HOLDS.
- Colouring: conflict degree <= 18, 19 colours; links of one colour share no plaquette, so given everything else they are independent tilts; the predictor (and any independent coins, the return bridge, C) is measurable for the conditioning. Residual >= E Var(S | G) >= c beta^2 (1+6 beta)^{-2} sum over the colour of |Adot_e|^2 >= (1/19) of the sum over H. HOLDS.
- Plaquette step: |fdot_p| <= sum over e in p of |Adot_e|; (sum)^2 <= 4 sum of squares; each link in at most 4 spatial plaquettes: factor 16. HOLDS. Spatial plaquette traces are invariant under gauge and under C_z (an ij face at x_i = c contains two flipped i-links; jk faces contain none). HOLDS. Var_pi f_p >= c/(1+6 beta)^2: pi is the time-zero marginal of the mixture of twisted u-tori with positive weights; one link of p, given the twist and the rest, is a tilt with kappa <= 6 beta, and f_p is a unit linear functional of it. HOLDS. Endpoint independence gives 2 Var. (1) HOLDS with constants independent of H, n, beta and the path.
- m(H): grid through time 0 reads no slice-1 spatial link (m = 3n^3); grid through time 1: every 12 face with x_3 off the grid planes has all four edges hidden, m >= (1 - 1/h) n^3; coarser nested levels and postprocessing read no more. Cost >= c n^3/(1+beta_K)^2. "Bounded cost requires m(H) = O(beta_K^2)": HOLDS.

Scope: Theorem 1 restricts a predictor class for the raw score of one half-slab representation. The infimum over all Y is J, which is intrinsic (check 1535). The note says this itself at its end (integrating slice 1 first changes S to its conditional mean). So Theorem 1 says nothing about E int J, and nothing about PUR-io.

## Theorem 4 (bridge-exchange parity), with the reversal as an iid copy -- HOLDS

- iid: in (11) the return half is drawn independently given A, C by construction. Its reversal has law Q_{A,C} because T (half spatial action on each side) is symmetric, vertex Haar is inversion invariant, z^{-1} = z, and the relative endpoint transformation moves between ends by a Haar change of variables. HOLDS. The note's alternative ("two independent copies of the same representation") makes this definitional.
- (10): S_1 - g = (S_1+S_2-2g)/2 + (S_1-S_2)/2, each of squared norm v_S/2; exchange preserves Q^{x2}, so the parity spaces are orthogonal; E[(S_1-g)Y] <= sqrt(v_S/2)(||Y_+|| + ||Y_-||); residual >= v_S(1/2 - sqrt(p(1-p))). With x = p - 1/2: 1/2 - sqrt(1/4 - x^2) = x^2/(1/2 + sqrt(1/4 - x^2)) >= x^2. HOLDS. Y = S_1 - S_2 subtracts exactly v_S/2. HOLDS. Symmetric functions of the two bridges are even. HOLDS.
- W_K >= c n^3 beta^2/(1+6beta)^4 (H = all spatial labels, m = 3n^3); then cost >= eps^2 W_K -> infinity on the trajectory; the weighted mean of (p-1/2)^2 is O((1+beta)^2/n^3). HOLDS.

Scope: the obstruction comes from scoring one bridge only. With the symmetric score S_1 + S_2 (the derivative of log b_A(C)^2), even tests lose nothing. The note says so ("Scoring both arcs symmetrically changes the regression problem").

## Same-aspect separation at beta_* = 1/25600 -- HOLDS

- Row 708, proof of Corollary TR1, entrance part only: g(t_0; b^3; beta_0) <= 0.0101 t_0/b for beta_0 <= 1/25600, t_0 = ceil(log_2 b) >= 8 (b >= 256), b >= t_0; here g = log Tr T^{t_0} - t_0 log lambda_0 on the gauge-invariant space, untwisted. Check 709 re-derived 0.0101. Evenness of b is not needed for this part; n = l b^K is even anyway. The use is correct and does not use (VIR_K).
- T_P >= 0 (gap-transfer.md (2c)), simple top eigenvalue with positive eigenvector; by Identity FL it lies in the range of P_0. So Tr(P_0 T^u) <= Tr T^u, every ratio is in [0,1], and G(t) is nonincreasing in t. For u >= t_0: 1 <= Z_+(u)/lambda_0^u <= exp(0.0101 t_0/n), Z_+(2u) >= lambda_0^{2u}, P_K >= exp(-0.0202 t_0/n) -> 1. HOLDS.
- Theorem 1 and Theorem 4 constants are uniform in beta (kappa <= 8 branch), so at beta_* the straight-grid test and parity-pure tests cost >= c(beta_*) n^3. HOLDS.

This is the first separation inside pure Wilson at the seed aspect (off the trajectory) between purity and a sufficient test. Check 1527 had only a circle-kernel toy separation, and said a strict ordering inside pure Wilson does not follow from a comparison model. Limit: the separation is for the restricted predictor classes only. Nothing here bounds E int J at beta_*, so purity is not separated from (11) with an unrestricted Y, nor from (R) with O containing the scored bridge.

## Spectator comparison -- HOLDS; on file

Eigenvalues 1 +- n^{-2}; factor (1 + r^{2u})/(1 + r^u)^2 -> 1/2 since u(1-r) ~ 2u/n^2 -> 0; P_K <= 1 by positivity. Normalized Wilson measurements are unchanged for each twist and period. HOLDS. This is the spectator of check 1527 (vi) and row 1530's stopping statement. Not new.

## A last grid of bounded size -- HOLDS

L <= 4d I gives D_r >= d_r I; X_r >= 8 d_r^2 for any unit axis field (the plaquette axis is not needed). For N < 4096, u/8 = n/4096 < h. Theorem 1 still applies for h >= b. HOLDS.

## (R) and conditional projection -- projection HOLDS; (R) holds after a wording correction

- Projection: for Y = E[S_1 | A,C,O] - E_Q S_1, E[S_1 Y] = E[Y^2], so the subtraction is Var(E[S_1|O']) and the residual is E Var(S_1 | O'), O' = (A, C, O). No O'-measurable Y does better (Pythagoras). So the optimum of (11) over O'-measurable tests is the left side of (R). HOLDS.
- Correction (wording; no inequality changes). "Directed boundary data" is undefined. (R) is meaningful for any sub-sigma-algebra O and should be stated so. When O contains the scored bridge, Var(S_1 | O') = 0, and (R) is E int J ds <= 2(1 - sqrt 457/25). That is the direct path-energy test of check 1527 (vi) (STIFF-TO-HELL at 457/625 at the original aspect), and the infimum over Y of row 1530 (11) (check 1535). For smaller O, (R) is that test plus a nonnegative residual, so it is stronger. The sentence "the precise remaining signed estimate" should name it as that test or a strengthening of it.

## Equivalent is not progress: (R) against (PUR-io)

(R) is STRONGER than (PUR-io), and not equivalent to it. For every O, (R) implies E int J <= threshold, which implies P_K >= 457/625 by (2.1)-(2.3) (rows 1373/1526, check 1527 (i)). The converse fails: (a) in the positive-kernel class, the circle kernels of check 1527 (vi) (purity 257/289, path energy >= c N^2); (b) inside pure Wilson at the same aspect, for O generated by a straight grid or parity-pure tests: at beta_* = 1/25600, P_K -> 1 while the left side of (R) is >= c(beta_*) n^3. For O containing the scored bridge, (R) is exactly the existing STIFF-TO-HELL test, so it is not new. For smaller O it is a strengthening of a test that is already only one-way. It is not weaker than (PUR-io) in any case. No progress under the rule.

## Are the negative results new relative to rows 1380, 1386, 1442, 1527

- Theorem 3 (7): new as a statement. It is the straight-blocked form of row 1530 (5), from row 1141's pin and row 1145 (3), and dimension-blind. Row 1386 NEG classes it as a negative, and the NEG verdict is unchanged. Row 1442 lists straight-product-specific obstructions (1434); this is one more of that kind. It is not a group-level obstruction.
- Theorem 1 and Theorem 4: new. The library grep finds no earlier first-layer regression bound or bridge-exchange parity bound for the midpoint score; row 1321's replica exchange is a different object. Rows 1380 (Theorem C1, link-end moves) and 1386 (Remark FI, small one-link score) treat other questions. Both theorems restrict predictor classes for a representation-dependent raw score, and leave the intrinsic infimum J untouched. So they do not obstruct STIFF-TO-HELL or (PUR-io).
- Same-aspect separation: new, and it partly answers check 1527's remark that no strict ordering inside pure Wilson was shown (for restricted predictors only).
- Spectator: not new (check 1527 (vi), row 1530).
- (5) and its selectivity: the coarse-level form of row 1530 (6). Same small-field scope and same free-count selectivity as check 1535 found. No new mechanism.

## Verdicts

| Part | Verdict |
|---|---|
| Theorem 3, (7), on every predetermined nested straight grid, all sixteen laws, axes and level reading the sample | HOLDS (dimension-blind; straight-blocked form of row 1530 (5)) |
| Coarse pin, (8), depth uniformity via row 1145 (3), (9) | HOLDS |
| Theorem 2, carry (5) to radii beta_K^(5/32)/8 in fine links | HOLDS (nonempty only for beta >= (8 r_0)^32; physical size -> 0) |
| Action estimate, stack translation, (6), good cubes, roots, lower estimate | HOLDS |
| Deterministic bound C r^(4-d) | HOLDS |
| Selectivity: U(1) zero | HOLDS (trivially, ad = 0) |
| Selectivity: 5D at most C/r | HOLDS (the split is the free mode count r^(4-d)) |
| Theorem 1, (1), with (2), (3), the colouring and the plaquette step | HOLDS |
| m(H) >= (1 - 1/h) n^3 for straight grids; cost >= c n^3/(1+beta_K)^2 | HOLDS |
| Theorem 4, (10), reversal of the return arc as an iid copy, Y = S_1 - S_2 | HOLDS |
| W_K lower bound and density-weighted corollary | HOLDS |
| Same-aspect separation at beta_* = 1/25600 and the use of row 708 | HOLDS (entrance part only; restricted predictors only) |
| Spectator comparison | HOLDS (on file) |
| Last grid of bounded size | HOLDS |
| Conditional projection attains the residual | HOLDS |
| (R) as "the remaining estimate" | HOLDS AFTER CORRECTION: define O as any sub-sigma-algebra; for O containing the scored bridge (R) is check 1527 (vi)'s STIFF-TO-HELL test at 457/625; otherwise a strengthening of it |
| (R) against (PUR-io) | STRONGER, not equivalent, not weaker; strict in the kernel class and, for straight-grid or parity-pure O, inside pure Wilson at beta_*; no progress |
| Novelty of negatives vs 1380, 1386, 1442, 1527 | Theorems 1, 3, 4 and the same-aspect separation are new statements; spectator not new; none changes NEG, the 1442 verdict, or the status of PUR-io |

RESULT Check 1540 of row 1536: every mathematical statement checked HOLDS, and (R) holds after one wording correction. Theorem 3, (7), holds on every predetermined nested straight grid under all sixteen twisted laws: the coarse covariant Laplacian has a gap c(log N)^(-5/2), and the argument is dimension-blind. The carry (5) holds but is small-field and ultraviolet (beta >= 8^32, physical size -> 0), with the free-count selectivity of check 1535. Theorems 1 and 4 and the beta_* = 1/25600 separation hold but restrict predictor classes for a representation-dependent raw score, leaving the intrinsic infimum J untouched. (R) is stronger than (PUR-io), and for O containing the scored bridge it is check 1527's STIFF-TO-HELL test. No progress toward (PUR-io).

Checked line by line by Claude (Opus 5.5).
