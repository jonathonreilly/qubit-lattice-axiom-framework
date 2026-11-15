lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T11:52Z

# Check of `library/gap-tiltproof-max.md` (FINISH row 979)

Provenance: Claude Opus 5.5, max effort, Mac mini worker 2, branch `claude/ym4d-hard-route` at commit 2601b4afd. One line-by-line reading by one other model than the author (row 977 was written by Claude Fable 5.2). Not an audit. Check item: no extension of the results, no new attack.

## Plan (at most eight steps, one per response, each appended before the next)

1. Read the note's setup, Section 2.0 (ZERO-CEIL), and the ported-lemma statements it cites; check ZERO-CEIL.
2. Check Lemma D1 (Step 4).
3. Check Theorem D2 attack 5.2: reflection structure with two pinned slices, gauge-fixed crossing links, end weights, layer coupling b. State the hypotheses of the ported reflection-positivity lemma as used, and whether each use meets them.
4. Check Theorem D2: the Gaussian-domination step with shifts on sheet bonds only (FSS hypotheses as used), the sum rule 5.4, and the passage 5.5 from one slice to q~, with its hand arithmetic.
5. Check Corollary CAP (6.1).
6. Check Proposition QUOT-CAP (9.1) and the hand arithmetic of 10.1.
7. Verdict table per statement (HOLDS / HOLDS AFTER CORRECTION / FAILS, with the line), and the RESULT line.

## Step 1. Section 2.0, ZERO-CEIL (note lines 54-72)

Sources read: the note in full; `library/gap-avgcurv-max.md` 44-60 (objects, K_a) and 124-200 (FLOW, Lemma Z, Theorem POL-BR, Lemma NEC).

Line by line.
- l.55-56. At phi = 0 the gauge orbit is {0}, so every z is admissible, and Lemma Z gives Var = k0_(s,b_t)|z|^2. So kbar_(s,t) >= k0_(s,b_t). tau_b >= 0 holds: L tau_b = d/db log Z_b(0) is non-decreasing (convexity), it is 0 at b = 0 because E_m x_l = 0 (centre -1 at one end site), and tau_b is the same on every link (translations and axis permutations/reflections of the cube preserve V, hence Omega by uniqueness of the top eigenfunction, and <x^(-1), w^(-1)> = <x, w>). So k0 >= k00. HOLDS.
- l.57. Generic phi has a discrete stabiliser (SU(2) holonomies that do not commute), so the horizontal space has dimension 12|B| - 3|B| = 9|B|; Cov is smooth in phi on the compact M x M; a limit point of horizontal planes at phi -> 0 is a 9|B|-plane on which Var = k0. HOLDS (remark only).
- l.58. POL-BR returns alpha_s^thm := 1/(integral over [0, c] of exp(2 integral over [0, t] of kbar)). With kbar >= k00: alpha_s^thm <= 2 k00/(e^(2 k00 c) - 1). HOLDS.
- l.59-60. k00 = (beta^2/4)(1/lam^2 + 1/(1 - lam)^2); with p = lam(1 - lam): r = (1 - 2p)/p, r + 2 = 1/p, r(r + 2) = (1 - 2p)/p^2 = 1/lam^2 + 1/(1 - lam)^2; 2 k00 c = (beta/2) r (r + 2) p = beta r/2. HOLDS.
- l.61. d/dr log[r(r + 2)/(e^(beta r/2) - 1)] = 1/r + 1/(r + 2) - (beta/2) e^(beta r/2)/(e^(beta r/2) - 1) < 1/2 + 1/4 - beta/2 on r >= 2, <= 0 for beta >= 3/2. HOLDS.
- l.62-63. r = 2 gives 4 beta^2/(e^beta - 1); averaging over s in (0, 1/beta) with the factor 1/2 gives 2 beta/(e^beta - 1). At beta 2.3: e^2.3 - 1 = 8.97418, so 21.16/8.97418 = 2.3579 and 4.6/8.97418 = 0.51258 < K_30. K_30 = (12.51 + 3 log 30)/28 = 0.8112 (C_beta = 12.51 is row 960's value, unchecked there). HOLDS.
- l.64-65 (marked ARGUED). I recomputed the values at lam = 0.10, 0.40, 0.50 (0.00754, 2.1548, 2.3579): they agree. The trapezoid sum is 1.0778, as written. But a trapezoid sum is not a bound. The integrand is increasing in lam on (0, 1/2] (r decreases there, and the bound decreases in r), so the right-endpoint sum with the same nodes IS an upper bound: 2 x 0.05 x 11.9565 = 1.1957, so alpha^thm <= 0.260 (given upper bounds for the nine listed values). CORRECTION: 0.234 is an estimate, not a bound; the bound from these nodes is 0.260, and K_a <= 0.260 needs a >= 104 (K_103 = 0.2615, K_104 = 0.2592).
- l.66-68. K_49 = 0.5146 > 0.5126 > K_50 = 0.5051, so "a >= 50" HOLDS. "a >= 117" (K_116 = 0.2348, K_117 = 0.2330) is right for the number 0.234, which is not a bound (previous item): read "a >= 104 from the monotone sum". The remark on tau_b > 0 is qualitative (tau = 1 is not the true value); it carries no weight.
- l.69-70. "Counterexample to the use, not to the statement": correctly scoped. Q_8, 2T: left times right multiplication of Q_8 on H has commutant R (Q_8 spans H), so Cov_m = Id/4 holds. U(1): k00 doubles, 2 k00 c = beta r, cap 4 beta/(e^(2 beta) - 1) = 9.2/98.484 = 0.0934. HOLDS.
- l.71-72. "it is at least 117": rests on the ARGUED number. PROVED: at least 50; from the monotone sum: at least 104.

**Verdict 2.0 ZERO-CEIL: HOLDS** (the PROVED part: every admissible kbar >= k00_s, and POL-BR returns at most 2 beta/(e^beta - 1) = 0.513 < K_30 on the a = 30 box). The ARGUED refinement at l.65/67/72 HOLDS AFTER CORRECTION: 0.234 is a trapezoid estimate; the bound from the same nodes is 0.260 (a >= 104), not 0.234 (a >= 117).

Numerics: the machine's numeric lock was held by row 976 (`gap-escape-976`, until 2026-11-15T03:31Z) when I tried at 23:58Z. So every number in this check is hand arithmetic (a few closed-form evaluations, each shown); no lattice sum was run.

## Step 2. Lemma D1 (note lines 175-200)

Line by line.
- l.181 (i). The tangent space of the orbit at phi is {X.phi}, (X.phi)_l = X_u phi_l - phi_l X_v for l = (u, v). phi^Lam_l = 0 on direction-1 links, so every tangent vector vanishes there. Any z supported on direction-1 links is orthogonal to the orbit. HOLDS.
- l.182 (ii). m is gauge invariant (V is, Haar is, and Omega is the unique top eigenfunction of a gauge-covariant T_0); <g x h^(-1), g w h^(-1)> = <x, w>; a transverse link has both ends in one plane x_1 = k, and <1, g x g^(-1)> = (1/2) tr x. So J_(b,phi^Lam) is invariant under plane-wise g(k). g(k) = -1 sends x_l to -x_l on the direction-1 links k-1 -> k and k -> k+1 and fixes every transverse link. So E q~_k(y) = 0. HOLDS.
- l.183 (iii), proof l.190-191. k' not in {k-1, k}: g(k) = -1 flips q~_k and q~_(k-1) only. k' = k-1: g(k+1) = -1 flips q~_(k+1), q~_k and not q~_(k-1) (needs k-1 != k+1, so S >= 3). k' = k+1: g(k) = -1 (needs k+1 != k-1). Same plane: M(y, y') := E[q~_k(y) (x) q~_k(y')] satisfies M = R M R^T for R(q) = g q h^(-1), g = g(k), h = g(k+1) independent; these R fill SO(4), whose commutant on R^4 is R, so M = (1/4) tr M Id_4 (M need not be symmetric; the commutant argument does not need it). For Q_8 and 2T the same holds: Q_8 spans H, so the commutant of left and right multiplication is R. HOLDS.
- l.184 (iv). E<z, q~> = 0 by (ii); Var = sum a(y) a(y') e^T M(y, y') e = (1/4) sum a a' G(y, y'); |z| = 1. HOLDS.
- l.185-187 (v), proof l.192-194. With Haar product reference, J_(b,phi^Lam) = F (nu_Lam (x) Haar_dir1)/norm, where F = m-density(x) m-density(w) e^(b<x,w>) is continuous and positive on the compact M x M, and nu_Lam is the normalised product of e^((Lam/s)<1,x_l>) e^((Lam/s')<1,w_l>) over transverse links. nu_Lam -> point mass at 1 weakly, so the integral of g F against nu_Lam (x) Haar converges for every continuous g, and the normaliser tends to a positive limit. <z, q~> is bounded and continuous, so Var converges. For each Lam, z on direction-1 links is admissible by (i), so kbar_(s,t) >= Var_Lam for all Lam, hence >= the hard-pinned value. HOLDS.
- l.195-197 (remark, generic points). Stabiliser of phi^Lam = plane-wise constant g(k) (each plane is connected by transverse links). A gauge-invariant function has a stabiliser-fixed gradient there, and v -> g v h^(-1) fixes no non-zero v, so the gradient vanishes on direction-1 links. Approach along phi^Lam + eps eta, eta generic: the limit of the orbit tangent spaces is spanned by g.phi^Lam (zero on direction-1 links) and h.eta (h the stabiliser algebra); <z_p, X.eta> = <e, X(k) E_p - E_p X(k+1)> (2/A)^(1/2) with E_p := sum over y of cos(p y) eta_k(y), which is 0 under the stated condition. So z_p lies in the limit horizontal space, and continuity of Cov gives the bound. HOLDS (one line in the note; the step is as I wrote it here). Not needed for (TILT-COV-sup) as stated, which already admits phi^Lam.
- l.199. G(y, y) = E|q~|^2 = 1/s^2 + 1/s'^2 + 2 tau/(s s'), tau := E<P_k(y), P'_k(y)> in the tilted law (depends on Lam and b; it is not the tau_b of Lemma Z unless Lam = 0). HOLDS with that reading.

**Verdict Lemma D1: HOLDS** (all five clauses, for S >= 3; the note asks S >= 4 even). The proof is complete as written; the only unwritten step is the weak-convergence detail of (v), supplied above.

## Step 3. Theorem D2, 5.1 and 5.2: slab form and reflection structure (note lines 202-222)

**5.1 (l.209-214).**
- l.209. T_0 Omega = lambda_0 Omega reads e^(-V(x)/2) (integral of e^(beta<x,w>) m(dw)) = lambda_0 Omega(x); multiply by e^(-V(x)/2). So m-density(x) = lambda_0^(-1) e^(-V(x)) (integral of e^(beta<x,w>) m(dw)). HOLDS.
- l.210-212. T_0 has a continuous strictly positive kernel on a compact space, so lambda_0 is simple and isolated and lambda_0^(-n) T_0^n 1 -> <Omega, 1> Omega uniformly. e^(-V(x)/2)(T_0^n 1)(x) = integral of e^(-V(x_0)) e^(beta<x_0,x_-1>) e^(-V(x_-1)) ... e^(-V(x_-n)/2): full beta on slices 0..-n+1, beta/2 on slice -n, beta on each time-like layer. The pinned set is closed and the densities converge uniformly on it, with positive normalisers, so the two-slice marginal of mu_n converges in total variation to the hard-pinned law. HOLDS.
- l.213-214. In the time-like layers t != 0, Haar time-like links can be gauged to 1 recursively outward from slices 0 and 1 (layer -1 by g on slice -1, layer -2 by g on slice -2, ...; layer 1 by g on slice 2, ...). No gauge transformation touches slices 0, 1, so the pinned links and the layer-0 links (kept at 1) are untouched, and Haar invariance gives Jacobian 1. HOLDS. (The time-like links of layer 0 cannot be restored: re-fixing them would need g on slice 0 or 1.)

**5.2 (l.216-222).** theta: y_2 -> 2j + 1 - y_2 (mod S), S even; halves Lam_+ = {j+1, ..., j+S/2}, Lam_- = {j+S/2+1, ..., j+S}.
- Crossing links are exactly the direction-2 links j -> j+1 and j+S/2 -> j+S/2+1 (every other link has both ends at one y_2 or inside one half). In slices 0, 1 they are pinned at 1. In a slice t not in {0, 1}, for each (x_1, x_3, t) the two crossing links have the four distinct end sites j, j+1, j+S/2, j+S/2+1 (S >= 4), so g at (x_1, j+1, x_3, t) and at (x_1, j+S/2+1, x_3, t) set them to 1 independently: a matching, hence a forest, Jacobian 1. These g are at sites outside slices 0, 1, so the law of the slice-0 and slice-1 links is unchanged, and so is Z(h) of 5.3 for every h (h acts on slice-0 links only). HOLDS.
- l.219. A straddling plaquette has two crossing links (= 1) and two links of one direction mu in {1, 3, time}, mirror images C, theta C; (1/2) tr U_p = <C, theta C> = 1 - (1/2)|C - theta C|^2 since |C| = 1. Orientation: theta reverses direction-2 links, and (1/2) tr U = (1/2) tr U^(-1) for SU(2), so the action is theta-invariant. Couplings: beta (bulk), beta/2 (end slices -n, n+1), all >= 0. In layer 0 the straddling (2, time) plaquettes have all four links pinned at 1: constant. HOLDS.
- l.220. In slices 0, 1 all direction-2 and direction-3 links are 1, so every (1,2)- and (1,3)-plaquette of slice 0 is beta <P_k(y), P_k(y')> (not only the straddling ones), and the (2,3)-plaquettes are constant. HOLDS.
- l.221. The pinning pattern (transverse links of slices 0, 1; time-like links of layer 0), the couplings (b on layer 0; beta/2 on the end slices) are invariant under theta, which preserves every slice and every layer. The layer coupling b enters only plaquettes of layer 0 that do NOT straddle (the straddling ones are constant), so the RP decomposition holds for any real b; b >= 0 is used only in 5.5. HOLDS.
- l.222. Same for direction 3 (crossing direction-3 links: pinned in slices 0, 1, gauged elsewhere; C in {1, 2, time}). HOLDS.

**The reflection-positivity lemma, exactly as used.** The Wilson-specific statement cited at l.204-205 (Osterwalder-Seiler: the Wilson measure is RP for planes bisecting links) does not apply as stated: mu_n has pinned links, couplings beta/2 and b, an open time interval, and in 5.3 shifts that are not gauge invariant. What 5.2 actually uses is the abstract criterion (Froehlich-Israel-Lieb-Simon 1978, Section 2; the form used by FSS 1976):

(RP-abs) Let nu_+ be a finite positive product measure on the variables of Lam_+ (here: Haar or a point mass at 1 on each link), nu_- := theta_* nu_+, crossing variables fixed. Let A and C_1, ..., C_m be bounded real measurable functions of the Lam_+ variables, c_i >= 0. Then B(F, G) := integral of F (theta G) exp(A + theta A + sum c_i C_i theta C_i) d(nu_+ (x) nu_-) is a symmetric positive semi-definite bilinear form on bounded functions of the Lam_+ variables; so B(F, G)^2 <= B(F, F) B(G, G). (Proof: expand the exponential of the cross terms; each term is c^alpha/alpha! times (integral of F e^A C^alpha d nu_+)(integral of G e^A C^alpha d nu_+).)

Hypotheses met by mu_n: product reference, theta-symmetric (yes, l.221); weight of the form exp(A + theta A + sum c_i C_i theta C_i) with c_i in {beta, beta/2} >= 0 after the gauge fixing (yes, l.219); C_i are the four real coordinates of a link variable on the Lam_+ side (bounded). The h-dependent form needed by 5.3 is checked in Step 4.

**Verdict 5.1: HOLDS. Verdict 5.2: HOLDS**, provided the ported tool is the abstract criterion (RP-abs), not the Wilson-specific theorem the note names (CORRECTION of the citation at l.204-205; the note's own reduction at l.222 already reaches the (RP-abs) form, so no step changes).

## Step 4. Theorem D2, 5.3-5.5, its numbers, and 10.1 (note lines 224-256, 423-427)

**The Gaussian-domination lemma (FSS 1976), exactly as used.** Fix plane k of slice 0. For h: (Z/S)^2 -> R^4 let Z(h) be the integral over the gauge-fixed mu_n with every sheet-bond term beta<P(y), P(y')> = beta - (beta/2)|P(y) - P(y')|^2 replaced by beta - (beta/2)|P(y) - P(y') - h(y) + h(y')|^2, all other terms unchanged. Hypotheses:
- (G1) For each theta in R := {planes y_2 = j + 1/2, y_3 = j + 1/2: j in Z/S}, the integrand at h has the (RP-abs) form with A and C_i depending on h only through h_+ := h on the Lam_+ sheet sites, and on the other side through the mirror field theta h_- (y) := h(theta y). Then Z(h) = B_theta(h_+, theta h_-) and Z(h)^2 <= Z(h_+ u theta h_+) Z(theta h_- u h_-).
- (G2) Every sheet bond is bisected by a plane of R.
- (G3) Z is continuous, depends on h only through its gradient on sheet bonds, and tends to 0 as the largest gradient tends to infinity (|P(y) - P(y')| <= 2): a maximiser exists modulo constants.
- (G4) A reflected field h_+ u theta h_+ is again a sheet field; the numbers of bonds with non-zero gradient of the two reflected fields add up to 2 (N(h) - N_cross(h)).
Conclusion: Z(h) <= Z(0) (a maximiser with the fewest non-zero-gradient bonds is constant).

Each use meets them.
- (G1). A crossing sheet bond gives -(beta/2)|P(y) - h(y)|^2 (into A_+), the mirror term (into theta A_+ at theta h_-), and the cross term beta <P(y) - h(y), theta(P(y) - theta h_-(y))>, i.e. c = beta >= 0 times C^a(h_+) theta C^a(theta h_-) with C^a = a-th coordinate of P(y) - h(y). Here theta acts on the random link and not on the constant h, which is what makes the mirror term the theta-image of a Lam_+ term at the field theta h_-. Sheet bonds inside a half go into A_+ or theta A_+. All other terms are the h-free (RP-abs) form of 5.2. MET.
- (G2) MET: sheet bonds lie in directions 2, 3, S is even. (G3) MET. (G4) MET (counting as in FSS).
So l.226-227 HOLDS.

**l.227-229 (second order).** E P = 0 holds in mu_n itself (g = -1 at every site of the hyperplane x_1 = k in every slice fixes all pinned and gauge-fixed links, which have both ends in that hyperplane, and flips the direction-1 links k-1 -> k and k -> k+1). With X := beta <P, (-Delta) h> and c := beta <h, (-Delta) h>, d^2/de^2 Z(e h)/Z(0) at 0 is E X^2 - c <= 0. For h = e cos(p y): -Delta h = 2E(p) h; translation invariance of mu_n in directions 2, 3 gives sum over y, y' of cos(p y) cos(p y') g(y - y') = (A/2) G^e-hat(p) if 2p != 0 (the cos(p(y + y')) part sums to 0) and A G^e-hat(p) if p in {0, pi}^2 \ {0}; sum of cos^2 is A/2 or A accordingly. Both cases give G^e-hat(p) <= 1/(2 beta E(p)). The bound is on the second moment; with E P = 0 it is the variance. The finitely many expectations converge as n -> infinity by 5.1. HOLDS for every real b (b >= 0 not needed here).

**5.4 (l.231-233).** G^e-hat(p) = (1/A) E|sum over y of e^(ipy) <e, P(y)>|^2 >= 0. (1/A) sum over p of G^e-hat(p) = g(0) = e^T E[P (x) P] e = 1/4 (D1(iii) argument applied to P alone). For Low containing 0 the bound applies on the complement. Sum over p != 0 of 1/(2 beta E(p)) = (A/beta) G_S with G_S as defined. HOLDS.

**5.5 (l.235-238).** The hard-pinned density m(x) m(w) e^(b<x,w>) on the pinned set is symmetric under x <-> w, so <z, P'> and <z, P> have one law. e^(b<x,w>) = sum over n of (b^n/n!) <x,w>^n, and <x,w> = sum over links and coordinates of x_l^a w_l^a: a kernel of positive type for b >= 0 (Schur products). So Cov(f(x), f(w)) = E[(f(x) - Ef)(f(w) - Ef)] >= 0 (E f(x) = E f(w)). Then Var(<z, q~>) >= Var(<z, P>)(1/s^2 + 1/s'^2) = 4 Var(<z, P>) k00_s. HOLDS. CORRECTION (no effect on any number): (2/A)^(1/2) cos(p y) e is a unit vector only if 2p != 0 mod 2 pi; for p in {0, pi}^2 \ {0} the unit vector is A^(-1/2) cos(p y) e. With that, Var(<z_p, P>) = G^e-hat(p) for every p. The Low sets used (Low = {0}; |n_i| <= 4 on side 120) contain no such p.

**Theorem D2 (l.240-242).** For every p, kbar_(s,t) >= (hard-pinned Var at b_t, D1(v)) >= 4 G^e-hat(p) k00_s, and max over Low >= average over Low. b_t in [0, beta]. HOLDS (also for Q_8, 2T: RP, FSS and the IR bound use only P in S^3 subset R^4 with |P| = 1, the plane-wise symmetry and the irreducibility checked in Step 2).

**Numbers (l.243-247), by hand.**
- S = 4. 2 - 2 cos p takes 0, 2, 4, 2. Sum over (a, b) != 0 of 1/(d_a + d_b) = 2 + 1/2 + 1 + 2/3 + 1/8 = 103/24 (pairs (0,2)x4, (0,4)x2, (2,2)x4, (2,4)x4, (4,4)x1). G_4 = 103/384. lam_* >= 64(1/4 - G_4/beta) = 16 - 103/(6 beta) = 16 - 7.4638 = 8.5362 at beta 2.3; positive iff beta > 103/96. HOLDS (PROVED, rational).
- S = 8 (10.1, l.423-427). Values 0, 2 - 2^(1/2), 2, 2 + 2^(1/2), 4, multiplicities 1, 2, 2, 2, 1: correct. I recomputed all 14 terms (pair (a, b), weight m_a m_b, doubled when a != b): 6.828427, 2, 1.171573, 0.5, 3.414214, 3.093836, 2, 0.872258, 1, 1.477592, 0.666667, 0.585786, 0.539504, 0.125; sum 24.274857. G_8 = 0.379295; lam_* >= 256(0.25 - 0.164911) = 21.78. HOLDS (each term is an explicit surd in 2^(1/2); the six-decimal values are right). CAP on side 8: lam_* beta = 50.09, 100.19/e^50.09 = 1.76e-20. HOLDS.
- S = 12, 16 (l.244-245, marked ARGUED). From the stated G_12 = 0.44405, G_16 = 0.48992: 576(0.25 - 0.193065) = 32.79 and 1024(0.25 - 0.213009) = 37.88; uniform-mode structure factor 256 x 0.036991 = 9.47 (l.247). Arithmetic HOLDS given the G values, which I did not recompute (lock held). Consistency: G_S - (1/2 pi) log S = 0.048344 (S = 8, exact), 0.048569, 0.048649, 0.048775 (S = 120): monotone with shrinking steps, as the known log S + const + O(S^-2) law requires.
- S = 120 (l.244-246, ARGUED). S_4 := sum over n != 0, |n_2|, |n_3| <= 4 of 1/|n|^2 = 12.747639: I enumerated the 14 classes (4 + 1 + 4/9 + 1/4 + 2 + 8/5 + 4/5 + 8/17 + 1/2 + 8/13 + 2/5 + 2/9 + 8/25 + 1/8). Since 2 - 2 cos a <= a^2, the low-mode sum is at least (120/2 pi)^2 S_4 = 364.756 x 12.7476 = 4649.8. With A G_120 = 11674.4: 4[3600 - (11674.4 - 4649.8)/2.3]/81 = 4 x 545.84/81 = 26.95. So "26.9 by hand from S_4" HOLDS given G_120; 27.1 uses the exact low-mode sum (not recomputed). G_120 itself stays ARGUED, as the note says.

**10.2 (not asked; cheap).** The one-momentum formula reproduces 103/384 at S = 4 (I recomputed 0.078125 + (2 x 0.291667 + 0.177083)/4 = 0.268229). The a = 0 line is sum over b != 0 of 1/(4 sin^2(pi b/S)) = (S^2 - 1)/12. HOLDS as a route; not carried out for S = 120.

**Verdicts.** 5.3 (with FSS as stated above): HOLDS. 5.4: HOLDS. 5.5: HOLDS AFTER CORRECTION (unit normalisation of z_p at p in {0, pi}^2 \ {0}; no number changes). Theorem D2: HOLDS. Numbers: side 4 and side 8 HOLD as PROVED arithmetic; sides 12, 16, 120 HOLD as ARGUED arithmetic given the floating G_S, as marked.

## Step 5. Corollary CAP (note lines 259-266)

- l.259-260. With kbar_(s,u) >= lam_* k00_s for all u in [0, c_s] (D2 gives every t): 1/alpha_s^thm >= (e^(2 lam_* k00 c) - 1)/(2 lam_* k00), 2 lam_* k00 = lam_* (beta^2/2) r(r + 2), 2 lam_* k00 c = lam_* beta r/2 (Step 1 algebra with beta -> lam_* beta in the exponent). The r-derivative bound of Step 1 becomes 1/r + 1/(r + 2) - lam_* beta/2 < 0, true for lam_* beta >= 3/2; so the maximum is at r = 2: 4 lam_* beta^2/(e^(lam_* beta) - 1), and the slice average with the factor 1/2 gives 2 lam_* beta/(e^(lam_* beta) - 1). HOLDS. It uses only the formula of POL-BR, so it holds whatever the status of POL-BR's proof (CONDITIONAL in row 968).
- l.261. Side 4: lam_* beta = 19.633, 39.27/e^19.633 = 39.27/3.361e8 = 1.17e-7. HOLDS (PROVED). Side 120: 2x/(e^x - 1) decreases in x, so a smaller lam_* gives a weaker valid cap; with lam_* = 26.9 (x = 61.87) it is 123.7/7.41e26 = 1.67e-25, with 27.1 (x = 62.33) it is 1.06e-25. "<= 1.7e-25" HOLDS (it belongs to the hand-bounded 26.9; the label "lam_* = 27.1" at l.261 should read 26.9) and stays ARGUED with G_120.
- l.262. K_a = (12.51 + 3 log a)/(a - 2) is decreasing for a >= 2, and K_(5e8) >= 72.6/5e8 = 1.45e-7 > 1.2e-7. So "a above 5 x 10^8" HOLDS (in fact a above 6 x 10^8).
- l.263-266. The seed box of a = 30 has spatial side 4a = 120, even, so D2 applies there. "24 orders": 0.811/1.7e-25 = 4.8e24. The scope sentence (a counterexample to the form the seed needs, not to the existence of a finite box-uniform kbar) is exact. HOLDS.

**Verdict Corollary CAP: HOLDS** (side 4 and side 8 PROVED; side 120 ARGUED through G_120; one label slip at l.261, 27.1 for 26.9, with no effect on the stated bound).

