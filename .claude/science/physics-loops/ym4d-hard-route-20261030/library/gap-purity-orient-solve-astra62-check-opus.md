# Check of row 1703 (gap-purity-orient-solve-astra62.md), FINISH row 1705

lead: anthropic/claude-opus-5-5 laptop subagent

Started Sat Nov 28 15:54:50 UTC 2026, pinned at commit 4b439e050. Checked by Claude Opus 5.5; author of the checked file gpt-6.2-astra max.

## Plan

1. Read the crux card.
2. Read row 1689 Part 2 and Part 4, equations (4)-(5), and its Opus check.
3. Read row 1703 in full.
4. Read the calibration inputs (PurIo.lean lines 389-406), the kernel in Transfer.lean, and row 1145's long-line bound.
5. Check every PROVED step of (C) and (A), and the 5D and spectator claims. Give verdicts.
6. Write the RESULT line.

## Notes as I go

- Read in full: crux card (62 lines); row 1689 Parts 2 and 4 (L23-L264); check 1704 of row 1689 (163 lines); row 1703 (253 lines).
- Read `Transfer.lean` L490-L690. `transferKernel_apply`: kernel = exp(-beta(S(u)+S(v))/2) times a vertex-gauge integral of prod_e exp(-beta(1 - halfTrace(g_a v_e g_b^{-1} u_e^{-1}))). Each spatial edge has one temporal factor per step, coupling beta. Spatial plaquettes get beta/2 from each side, so the closed path has isotropic coupling beta.
- Read `PurIo.lean` L380-L410 (`su2_fixed_observable_cutoffs_at_fixed_offset`): every infinite set A has a subsequence in A with betaAt/(K log L) -> 11/(3 pi^2).
- Hand check of (2), (3), (4), (5), (5a), (6), (7), (8) under way; next: row 1145 (1)-(2), row 1689 proof of (11).
- Read row 1145 `gap-solve2-astra62.md` L15-L52: (1) I_d(s)/I_1(s) <= exp[-(d-1)/(1+s)] for tilt s, stated with s <= 6 beta; (2) the density of an m-link path transport, other links fixed, is within eta(m/(1+6 beta)) of 1, eta(x) = sum_{d>=2} d^2 e^{-(d-1)x}. Read row 1689 L313 (b_beta) and re-derived it (4V links in a Haar cap, 6V faces at deficit <= 8/beta, log 8 for the twists).
- Read `Stage3.lean` L1573-L1590 (`layerFactor_products`): X^* X is the release (magnetic) transfer and X X^* the symmetric (spatially weighted) one. This supports row 1703's statement that the purities agree and that columns are read on the spatially weighted side. I did not read Stage3.lean L1718-L1732 or L3332-L3343.
- `FixedObservableLimit`, `CubicPeriodSublattice` and `Γ.transfer` are defined in the imported release, not in the lane folder. I did not read their definitions. The estimates below are local and use only the n^3 vertex count and translation invariance.
- Guide script (floats and fractions, never proof): scratchpad `guide1705.py`, run with `python3 -I` (sympy is not available under -I). It agrees with: 11/(3 pi^2) = 0.3715 < 5/12; c_* = 0.676; 490/2025 = 98/405 > 1/16; log(9/5) = 0.588 > log(625/457) = 0.313; 4 sqrt2/(3 pi) = 0.600 <= 1; the cap density identity cos^2(alpha/2)/sin^2(alpha) = 1/(4 sin^2(alpha/2)) at three angles; the oscillator purity (1-q)/(1+q).

## Item 1. Calibration and (1)

**(1), L34-L42. HOLDS.** The theorem at `PurIo.lean` L393 gives, for every infinite set, a subsequence on which beta_K/(K log L) -> 11/(3 pi^2). If the full sequence did not converge, an infinite set outside one neighbourhood would contradict this. So the full sequence converges (row 1703 L24 is right). Since 11/(3 pi^2) = 0.3715 < 5/12 and log n >= K log L, eventually beta <= (5/12) log n. Then 2 r e^{-2 beta} >= 2 (n/1024) n^{-5/6} = n^{1/6}/512. With h_i h_{i+1} <= 1, row 1689 (4) gives (1) on every history and in every twist (a seam only changes the sign of one J_i). This is the correction of check 1704, item 1, restated. Also m/(1 + 6 beta) -> infinity because m = s L^K and beta = O(K).

## Item 2. Obstruction (C)

**(2), the common-mass test, L46-L53. HOLDS.** On G the row ratio H(+,t)/H(-,t) lies in [e^{l-a}, e^{l+a}], with a = delta + 2 artanh q_0, because the two terminal log ratios differ by 4 artanh q(H_h) and have mean l_h. The ratio of the two G-normalized laws is that row ratio times a weighted mean of its inverse. So it lies in [e^{-2a}, e^{2a}]. Then the common mass is at least min(P_+(G), P_-(G)) e^{-2a} >= (1 - eta) e^{-2a}. The bad-mass hypothesis of row 1689 (5) is exactly P_sigma^y(G^c) <= eta for each sigma. The bound does not use a common l for different y, so it also covers a centre that depends on y.

**(3), L55-L80. HOLDS.** I checked each step.
- The measure. omega has total mass Tr A/Z = 1. Its x-marginal is A(x,x) dx/Z = pi, and its conditional law of y given x is B(x,y)^2/A(x,x), which is the weight that row 1689 (5) uses for the squared overlap. So "terminal-weighted" has the same meaning in both files.
- The event. Test 1 uses g_a, the first-slice links off e and x off e. Test 2 uses the unordered first-slice pair {V_1, V_2} and x_e^#. These are retained variables, the same in both rows. Then TV >= P_x^y(E_x) - P_{x^#}^y(E_x).
- Test 1 under omega x bridge. B(x,y)B(y,x) sews a closed path of period u, so omega with its bridge is the neutral Wilson path measure. With `transferKernel_apply`, each spatial face gets beta/2 from each side and each temporal face gets beta, so the law is isotropic at beta. Row 1689's convexity bound gives E(sum of signed deficits) <= -log Z/beta <= V b_beta, V = n^3 u. A fixed orientation class has V faces of equal mean (the seam moves are Haar-preserving changes of variable). So each face has mean deficit <= b_beta. Chord^2 = 2 x deficit. Markov and a union over j = 5 faces give 32 j^3 b_beta/kappa^2.
- Test 2. The m-2 interior links of a far straight side of the bottom third petal are collinear, so they share no face. Each is in 4 spatial and 2 temporal faces, so the tilt is at most 6 beta and row 1145 (2) gives density <= 1 + xi_K for their product. The reflection in R^4 that fixes a_3 and reflects v_3 pulls back under U -> D U^{+-1} F to x_e^# = x_e - 2(x_e . N)N with N = D^{-1} n F^{-1} (or the inverted form). N is an isometric image of the remote product, so its density is <= 1 + xi_K. I re-derived the cap estimate: with theta the angle of N to v (N . v >= 0), alpha = pi - 2 theta, density (2/pi) cos^2(alpha/2), ratio to (2/pi) sin^2 alpha equal to 1/(4 sin^2(alpha/2)) = 1/|w - v|^2. Superlevel sets are balls about v, so a ball of given radius has the most mass at v. There the mass is Pr(2|v . N| <= kappa) <= (2/pi) kappa. Four balls give 4(1 + xi_K) kappa.
- The row from x^#. Conditional on all but g_a, the density is proportional to exp(beta R . g_a) with |R| <= 6. On E_x: each of the j other faces has gradient sqrt(1 - p^2) <= chord <= kappa/(4j); the private face has |V . x_e^#| <= 1 - kappa^2/2 (both signs are needed, and the file uses both), so its gradient is at least sqrt(kappa^2 - kappa^4/4) >= kappa/2. So |grad(R . g)| >= kappa/4, and |R| - R . g >= kappa^2/(32(j+1)). The cap of radius beta^{-1/2} has Haar mass >= beta^{-3/2}/(6 pi) (sin t >= t/2), and on it R . g >= |R| - (j+1)/(2 beta). The ratio gives the third term. The bound holds for each conditioning, so it holds after the signs are erased.
- The limit. With kappa = b_beta^{1/3}: the first two terms are O(b_beta^{1/3}); beta kappa^2 >= beta^{1/3} because b_beta >= 1/beta; so the third term goes to zero. Since b_beta = O(log beta/beta) and xi_K -> 0, Delta_K -> 0. Nothing in the proof depends on the cube shape or on which private edge e is chosen.

**Failure at the size of row 1689 (5), L119. HOLDS.** If the hypotheses hold with constant D, the common mass is >= (1 - eta) e^{-2a} >= e^{-D}. So the set S where D <= D_* has omega(S) e^{-D_*} <= integral of o <= Delta_K. The row 1689 constants give c_* = 0.676 (guide) > 0. This also covers the family bound D <= 1/sqrt(2N) of row 1689 L222, since it is a fixed D_* after one fixed edge.

**(4), L121-L130. HOLDS.** 2p(1-p) <= 2 min(p, 1-p) and the squared sine is at most 1, so D_sign <= 2 x (Bayes error). The plaquette rule errs only if |x_e - S| > t (probability <= 2 b_beta/t^2 under pi, the slice marginal of the closed path) or |x_e - x_e^#| = 2|x_e . N| <= 2t (cap, <= 2(1 + xi_K) t). This gives (4).

**Purity accounting for C, L132. HOLDS, label corrected.** The sign heat bath fixes every function of z, so its gap is zero and (1) of row 1689 gives nothing. That line is PROVED. "The guaranteed credit from C alone is zero" is a reading of the proved lines, so it is ARGUED, not PROVED.

**What (C) covers.**
- It covers Lemma C (5) of row 1689 as row 1689 defined it: the fine disintegration with every cut, every temporal link and one fixed private edge (row 1689 L181), both terminal weights, any fixed constants, and any endpoint set of thermal probability bounded below. It is uniform over the 4m private edges, so the auxiliary-edge choice of row 1689 L155 does not escape it.
- It is narrower than the measurement's target quantity. It refutes the hypothesis of (5), not its conclusion (the column angle). Row 1703's own electric-axis example (L208) shows the angle can tend to one while (3) holds. So (C) is an obstruction to the method of Lemma C, not to the angle.
- It does not cover a coarser disintegration in which the first-step temporal links and the first interior slice are integrated before the centre is imposed (for example a block version of row 1689 L133 that keeps only block-boundary data). Then E_x is not a function of the history. Row 1703 L132 says this.
- The mechanism is elementary (ARGUED, my reading). The first temporal face on e enters the row ratio, it depends on the retained first-step data, and its log ratio has spread of order beta kappa^2 across histories. The cross ratio q cancels it; the centre l_h does not.

## Item 3. Obstruction (A)

**(5), L138-L160. HOLDS.** At most 12m translates use the link f (in fact at most 4m, the packet edges parallel to f). All other packet functions do not depend on U_f, so in slice Haar the plaquette U_p is uniform given them. Pr(1 - Re U_p <= v) = integral of (2/pi) sqrt(1 - z^2) from 1 - v to 1 <= (4 sqrt2/(3 pi)) v^{3/2} <= v^{3/2}. So ||1_F P'||_op <= v^{3/4}. Tr(1_{F^c} rho) = pi(deficit > v) <= b_beta/v. The split of ||P' rho^{1/2}||_HS and v = b_beta^{2/5} give a t_K <= 4 b_beta^{3/5}. Positivity t_K > 0 holds: the one-link multipliers are positive (GL3), so T is injective on the gauge-invariant space and <f, P_0 T^u f> = ||T^{u/2} f||^2 > 0. Note: (5) alone gives only t_K = O((log beta/beta)^{3/5}), a power of 1/log n. It does not give the superpolynomial claim.

**(5a), L162-L178. HOLDS.** At the free end each marked link has 4 spatial faces at beta/2 and one temporal face at beta, so the tilt is at most 3 beta. The marked links are collinear and factor. For SU(2) the mean of a tilted link is (I_2(s)/I_1(s)) G with G in SU(2), and row 1145 (1) gives I_2(s)/I_1(s) <= e^{-1/(1+3 beta)}. f is linear in each marked link, so the conditional mean of f is the product of these scalars times f at a point of the group, and |f| <= 8 (64 orthonormal triple products, sum of squares 4^3). All kernel factors are positive and P_0 acts on the y side, so |Bf(y)| <= 8 e^{-(m-2)/(1+3 beta)} (B1)(y). Summing over 5 vectors and n^3 translates gives the constant 320. With m = s n/l and beta <= (5/12) log n, t_K <= exp(-c n/log n) for late K, so t_K = o(n^{-A}) for every A. **The superpolynomial claim of the Result rests on (5a) alone.**

**(6), (7), (8), L180-L204. HOLDS.** v_K/5 <= C_loc <= v_K from five eigenvalues per site. Row 1689 (2) gives Tr X^2 >= (7/8)(Tr X)^2, so 7/8 - 1/5 = 27/40. In (7) the P-block is <= t^2 and the mixed part is <= 2t(1-t) by |rho_ij|^2 <= rho_ii rho_jj. (8) is the algebra of p_perp >= (p_* - 2t + t^2)/(1-t)^2.

**Electric-axis frame counterexample, L206. HOLDS.** With zero spatial coupling, the convolution multiplies each fundamental factor by r_f, so the compression is r_f^{12mu} I_5 exactly. The ratio is 10/25 = 2/5, and all translates have the same eigenvalue, so the nonzero-momentum fraction is 1 - n^{-3}.

**Separation from the seed, L208. HOLDS.** The one-link half-time kernels lie in [1 - eps, 1 + eps] with n^3 eps -> 0 (row 1145 (1)-(2), CITED for the seed in row 1145 section 7). The proof of (3) uses only first-step temporal faces, a lower bound on Z and the remote-link tilt; with zero spatial coupling the first two only improve and the tilt is 2 beta <= 6 beta. So (3) also holds there.

**Positive spatial coupling, L210. HOLDS.** ||M - I|| <= 3 s n^3 (S in [0, 6 n^3]); the telescoping bound is 6 s n^3 u = a/8; the eigenvalues lie in [7a/8, 9a/8]; 490/2025 > 1/16; the purity factor is >= e^{-12 s n^3 u} = e^{-a/4}.

## Item 4. The Y4, group, dimension and spectator tests

**Items 1-3, L214. HOLDS** (bookkeeping on the proved lines).

**Weak 4D compact U(1), L216. HOLDS AFTER CORRECTION.** "C has a single sheet" and "A's coefficient space is one-dimensional" use operations that are trivial for U(1). This is the same artefact as check 1704, item 4, and it is what the crux card's twin test (added after checks 1698 and 1704) excludes. The twins are the sheet theta -> -theta on one loop with a private edge (x_e^# = conj(x_e) conj(R)^2) and the 8-dimensional packet of charges +-1 per loop. With them (ARGUED here, by the same steps): test 1 uses the U(1) b^ab; test 2 uses a remote product whose square has density <= 1 + xi and a chord ball of Haar mass <= kappa/2 on S^1; the row from x^# uses the same gradient formula on S^1 and an arc of mass beta^{-1/2}/pi >= beta^{-3/2}/(6 pi). So (3) holds in weak 4D U(1). (5) and (5a) hold for the twin packet by the file's own L218-L225 argument. The file's conclusion (neither obstruction is selective for the group) stands and is stronger after the correction.

**Abelian packet weight, L218-L225. HOLDS.** I re-derived b^ab (8 C(d,2) faces at 8/beta, d links in an arc of mass 1/(pi sqrt beta), 2^{d-1} twists), the bound 1 - cos theta >= 2(theta/pi)^2, and the constant (1 + 2^{-1/4})^2 = 3.39 <= 4 for a t_K.

**Five-dimensional SU(2), L227-L233. HOLDS.** b_{beta,5} = {80 + 5 log(6 pi) + (15/2) log beta + log 16}/beta (10V faces, 5V links, 16 twists); j = 7; 8 staples, so 1 + 8 beta; at the free end 6 half spatial staples and one temporal, so 4 beta.

**Strong coupling, L235. HOLDS.** With l(z) the log ratio of the initial half weights, the first-step matrix moves each row ratio by at most e^{2 beta}, so |l_h - l(z)| <= 2 beta, and q <= (tanh beta)^r < 1/16.

**Neutral spectator, L237-L245. HOLDS.** (M_s + 3)/(M_s + 1)^2 = 5/9 at M_s = 2, and log(9/5) > H. The oscillator purity is tanh(u eps/2) <= pi/512.

**Scale and scope, L247. ARGUED, one correction.** "It reads the noncommuting holonomies and the actual Wilson staple in (3)" is not right: the U(1) twin satisfies the proof of (3), so (3) reads no non-abelian structure. The rest is ARGUED and I accept it.

## Verdict table

| Item | Verdict | Note |
|---|---|---|
| Calibration (full-sequence limit) and (1) | HOLDS | restates check 1704's correction |
| (2) common-mass test | HOLDS | covers a y-dependent centre |
| (3) TV bound, all five steps | HOLDS | omega matches row 1689's terminal weight; uniform in e and cube |
| Failure at the size of (5), any fixed D_* | HOLDS | c_* = 0.676 |
| (4) D_sign | HOLDS | |
| Purity accounting for C | HOLDS, label corrected | "credit zero" is ARGUED |
| **(C) as stated** | **HOLDS** | covers Lemma C (5)'s hypothesis on row 1689's fine histories; not the column angle; not coarser disintegrations |
| (5) | HOLDS | gives only a power of 1/log n |
| (5a) | HOLDS | the superpolynomial rate comes from here |
| (6), (7), (8) | HOLDS | |
| Electric-axis and positive-coupling comparisons, seed separation | HOLDS | |
| **(A) as stated** | **HOLDS** | covers the bare packet family of row 1689 in its coverage role; test (2) on one isotropic packet and other channel families stay open |
| Y4 items 1-3 | HOLDS | |
| U(1) group test | HOLDS AFTER CORRECTION | single sheet and one-dimensional packet are artefacts; twins satisfy (3), (5), (5a) |
| 5D test, strong coupling, abelian packet weight | HOLDS | |
| Neutral spectator test | HOLDS | |
| Scale and scope (g5, g6) | ARGUED, corrected | (3) reads no non-abelian structure |

(PUR-io) stays open. This check grants no status. No Lean run was made; the Lean files were read only. Not read: the release definitions of `FixedObservableLimit`, `CubicPeriodSublattice` and `Γ.transfer`, and Stage3.lean L1718-L1732, L3332-L3343.

RESULT: Check 1705 (Claude Opus 5.5) of row 1703: both obstructions HOLD. (C): every step of (2)-(4) holds. It refutes row 1689's Lemma C (5) hypothesis for any fixed constants on its fine histories, uniformly in the edge. It does not touch the column angle or coarser disintegrations. (A): (5) and (5a) hold. The superpolynomial rate comes only from (5a). This kills bare-packet coverage; test (2) and other channels stay open. U(1) test HOLDS AFTER CORRECTION: the single sheet and one-dimensional packet are artefacts, and the twins satisfy (3), (5), (5a). 5D, strong-coupling and spectator tests hold. (PUR-io) open.
