# Check of library/gap-mech-k2-step-astra62.md (FINISH row 1551)

Checker: Claude (Opus 5.5). Note checked: row 1549, author gpt-6.2-astra max.

## Plan

1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read the note in full; read check 1548 and row 1468 section 4.3.
3. Check positive claims in order: Q2 image formula and |M_c| <= 1; selective bound
   with J_y; obstruction with (3), (7); class (9); full colour rank suppression (8).
4. Check selectivity claims: U(1) and 5D vanishing; log cosh profile and one-link
   test; purity separation.
5. Check open-step statement vs row 1468 s4.3; zero Hessian remark; novelty.
6. Verdict per part; RESULT line.

## Steps

(complete; sections 1-8 below)
Step 1 done: read GOAL.md (computation-as-proof rule), FINISH Rules and Working efficiently (equivalent-is-not-progress). Step 2 done: read the note in full (234 lines), check 1548 in full, row 1468 sections 3-4.3, Lemma V (library/gap-pag-grow-astra.md 418-450), check 1527 (iii) lines 59-86.

Working notes so far (verdicts below are final unless revised):
- Image formula: matches row 1468 3.2; Re(M V^{-1}) = M.V for unit V; Zc(k|M|) = int exp(k M.q) dq by invariance.
- Lemma V re-derived by a different route: transverse moment = I_2(t)/(t I_1(t)); recurrence t I_1 = 4 I_2 + t I_3 gives (4+t) I_2 - t I_1 = t (I_2 - I_3) >= 0; longitudinal >= transverse iff t I_1 >= 4 I_2, same recurrence.
- Obstruction proof: Fourier/cosh step, subharmonic mean, chain rule, b-interval all verified (details in the sections below).
- Next: brute-force guide for (4) and the patch additivity; then write verdicts.

Guide run (python3 -I, floats, not a proof step; script in the session scratch folder): brute force of A_B with B(u) = u over all sites and all 384 signed permutations on coarse tori (4,8,4,4) (M = 8) and (5,4,5,4) (M = 5), with random labels and angles. A_B equalled the sum over A-labelled patches of sin^2(t_j)/32 to 12 digits; the all-B_0 field gave A_B = 0; all plaquette traces were equal between the labelled field and the all-B_0 field. This agrees with (4) and the patch additivity.

Provenance: Claude Opus 5.5, laptop subagent, lane checkout as found 2026-11-25; not an audit. Hand check; no Lean.

## 1. Image formula and |M_c| <= 1 (note lines 13-21) -- HOLDS

Row 1468 3.2 writes the kernel as exp(kappa Re(M_c V_c^{-1})) / Zc(kappa |M_c|). For unit V, V^{-1} = conj V, and Re(M conj V) = M.V (Euclidean product on R^4). By invariance of Haar, Zc(kappa|M|) = int exp(kappa M.q) dq. That gives the displayed formula. There are 16 x 4! = 384 contours, M_c is their mean of unit quaternions, so |M_c| <= 1. Mass is kept because the kernel is a probability density in V for each W (Fubini). Strength kappa = a x_k as in row 1468 3.2.

## 2. Selective bound on three electric plaquettes (lines 23-54)

- J_y = det Gram = det[E_1,E_2,E_3]^2 in [0,1]: Hadamard, |E_i| <= 1. HOLDS. Gauge invariance: conjugation at y rotates the three E_i by one SO(3) element. HOLDS. Degree >= 6 at the identity: each E_i is O(A), so the determinant is O(A^3) and J is O(A^6). HOLDS.
- Conditional structure (line 46). The free links V(y+0,i) each occur in exactly one P_i (periods >= 2 suffice). With the other links fixed, P_i = L V R, and h.(L^{-1} P R^{-1}) = (L h R).P, so P_i has density prop. to exp(t h'.q) with |h'| = 1 and t = kappa|M_c| <= kappa. Given W, coarse links are independent (product kernel). HOLDS.
- Lemma V. I re-derived it by a different route: transverse moment I_2(t)/(t I_1(t)); the recurrence t I_1 = 4 I_2 + t I_3 gives (4+t) I_2 - t I_1 = t (I_2 - I_3) >= 0, and longitudinal >= transverse iff t I_1 >= 4 I_2 (the same recurrence). The moment matrix is diagonal in an h-aligned basis, so E(v.q)^2 >= |v|^2/(4+t) for every v. The imaginary 3x3 block then satisfies S_i >= (4+t)^{-1} I_3 >= (4+kappa)^{-1} I_3. HOLDS.
- E J = <eps, (S_1 x S_2 x S_3) eps>: expand the squared determinant and use independence. Each S_i = c I + R_i with R_i >= 0, so the tensor product is >= c^3 I, and |eps|^2 = 6. This gives (1), m_kappa = 6/(4+kappa)^3. Averaging over orientations gives the G_y bound. HOLDS.
- P(J >= m/2) >= m/(2-m): from m <= p + (1-p) m/2 and J <= 1. HOLDS (conditionally too).
- Twisted lifts: a sign change of a link maps E_i to -E_i, so J does not change. HOLDS.
- Large-volume bound: stars with disjoint bonds have conditionally independent indicators given W. E[2^{-N_g}|W] = prod(1 - p_j/2) <= (1-p/2)^m <= e^{-pm/2}. Markov then gives P(N_g < pm/2) <= 2^{pm/2} e^{-pm/2} = exp[-(1 - log 2) pm/2]. HOLDS.

Verdict section 2: HOLDS, all numbered estimates included.

## 3. Obstruction, Theorem (3), with (4), (5) (lines 56-148) -- HOLDS

- Class (2). The proof uses only that S_tr takes one value on the 2^M labelled fields at fixed angles. So any function of the elementary plaquette traces is allowed, continuous or not, at any range. HOLDS. The tailed example (w(t) = (1-t)/(2+t), e^{-j^2} weights, degree four at the flat field) is in the class. HOLDS (not load-bearing).
- Trace-preserving test (line 108). Marked links (y+e_i, 0) sit at pairwise lattice distance 2, so no plaquette contains two of them. Each plaquette holonomy is then 1 or a marked link up to inversion, and tr(q^{-1}) = tr q. The traces are 0, 0, cos t in both A and B_0. HOLDS. In B_0 the imaginary parts lie in span(i,k), so J = 0 everywhere. HOLDS. In A: a star with a spatial distinguished axis contains a trivial spatial plaquette, so J = 0. If the common temporal link is marked, the three columns are parallel. So the other three temporal links must be the three marks. The only common nearest neighbour of e_1, e_2, e_3 in Z^3 is 0, so all spatial signs are +, and the base is y (time +) or y+0 (time -). The count is 2 x 3! = 12 of 384, i.e. 1/32. Columns are -i, -j, -k sin t at y and i, j, k sin t at y+0, so J = sin^2 t. Hence (4), H(t) = (B(sin^2 t) - B(0))/32. HOLDS (agrees with the guide run).
- Patches and additivity (line 115). Bases spaced by 4 have cyclic gaps >= 4, so marks of different patches in one slab differ by >= 3 in some coordinate. A temporal star sees spatial positions differing by <= 1 per coordinate. Consecutive-slab marks are collinear temporal links and never share a plaquette. Each (base, time sign) sees one slab. HOLDS.
- One-link likelihood (lines 117-119). t_j enters D only through one bond factor exp(kappa(M^1 cos t + M^k sin t)). The rest, including the normalizers 1/Zc(kappa|M_c(W)|), is a positive weight on W. The pushforward gives f_pi with |(u,v)| <= kappa. HOLDS.
- Compactness of P_kappa and attainment of the minimum in (5): weak compactness of the disc measures, t-equicontinuity, and q bounded away from 0 and 1. HOLDS.
- Positivity of d_{kappa,B} (lines 139-142). Equal odds give b f_pi = e^{-H} f_nu on R, hence on C (H is a trigonometric polynomial). |f(t+is)| <= exp(kappa cosh s) since Re cos(t+is) = cos t cosh s. The horizontal mean of (1/2) log(|f|^2 + eps) is convex in s (subharmonic, and the t-second derivative integrates to zero by periodicity), even in s (since conj f(z) = f(conj z)), and >= -kappa at s = 0. Monotone convergence keeps the bound as eps -> 0. So mean|u| <= 2 kappa cosh s + kappa. Re H(.+is) has j-th coefficient a_j cosh(js). The constant log b has no j != 0 coefficient. The top frequency 2n >= 2 of B((1 - cos 2t)/2) is nonzero. Letting s -> infinity gives the contradiction. HOLDS.
- Wrap bound (line 144). log(Q_unnorm / P_unnorm) = const - R(sigma) + err_sigma. Single flips change R by <= Gamma, so the oscillation is <= M Gamma + 2 eta. The log density ratio of two probability laws takes the value 0 in its range, so KL <= M Gamma + 2 eta. HOLDS.
- Chain rule (lines 146-148). The conditional Q-probability of A, as a function of t_j, is b f_{pi_A}/(b f_{pi_A} + f_{pi_B}). Here b = C_A/C_B, and pointwise the weights differ by exp(kappa M_{c2}.(j - i)), in [e^{-sqrt2 kappa}, e^{sqrt2 kappa}], inside the stated interval. So q is in P_kappa. The P_t-weights of earlier labels do not depend on t_j, so the integrated j-th term is >= d_{kappa,B}. Summing and comparing with M Gamma + 2 eta gives (3). HOLDS. M = V/64 on spatial periods divisible by 4, and R = 0 forces eta >= d V/128. HOLDS.
- Explicit exclusion (lines 150-157). The all-A and all-B_0 fields differ in kernel log weight by at most M sqrt2 kappa, which gives the displayed bound. For B = 192u: 6 - 3 sqrt2 = 1.757 > 3/2 > 51/50. HOLDS (the lower limit kappa >= 2 is not needed).

## 4. Radius and wrap, (6) and (7) (lines 159-176)

(6): a set of m bonds lies in at most 6m plaquettes. Each term of E_X is at most 2, so E_X <= 12m. Then sup|R_X| <= (1 + 12 theta x' m) w_X, and osc <= 2 sup. That gives Gamma <= A rho. HOLDS.
(7): the centre's ten-bond star supports survive the diameter cut. Dropping long terms keeps S_tr trace-only and only lowers Gamma. P_kappa is contained in P_{kappa_*} for kappa <= kappa_* (disc and b-interval), so d_{kappa,B} >= d_{kappa_*,B}. HOLDS.
Wording: "excluded uniformly in side" (line 176) should read "excluded on every untwisted torus with M > 2 eta/d_{kappa_*,B}, hence for all large sides at fixed aspect when eta = o(V)". This is a clarification, not a change of content.

## 5. Suppressing full colour rank, (8), (9), (10) (lines 178-213)

- alpha(h) = (2/pi) int_0^h sin^2: the Haar law of the S^3 angle. On the ball event, plaquette angle <= 4h (bi-invariant metric). |Im V_p| = sin(angle) <= 4h, so G_y <= (4h)^6 by Hadamard. There are 4V links. The KL identity D(mu||nu) = D(mu||H) + lambda E sum G + E S_0 + log Z_nu, with the restricted lower bound on Z_nu, gives (8). HOLDS AFTER CORRECTION: (8) uses (1), so the torus periods must be at least four (two suffice for the proof of (1)). Add "with periods at least four" to line 180.
- (9): |log D + eV + lambda sum G + S_0| <= eta gives dmu/dnu = c e^{err}, normalization gives |log c| <= eta, so KL <= 2 eta. With h = (m/2)^{1/6}/4 < 1/4 (m < 2), (4h)^6 = m/2, which rearranges to (9). HOLDS. What it shows: only large lambda is excluded. Guide arithmetic at kappa = 2: m = 1/36, h = 0.1225, alpha about 3.9e-4, so the threshold is about 72 (C + 31).
- (10): 8 x 32 interior + 10 x 8 crossing = 336 fine bonds. Every contour of a prescribed coarse bond uses interior links of its two cells and exactly one crossing link (both xi_mu cases checked), so M_c equals the prescription. The conditional density on the prescribed set is >= e^{-336 K_in}. Holonomy angle error is <= 10 u_f. Normalizing at most doubles the chordal error, and geodesic <= (pi/2) chordal, giving 10 pi u_f < eps/2. A radially decreasing density gives a centred ball at least its Haar mass, which yields alpha(eps/2) for every kappa. Columns move by <= 4 eps, the determinant moves by <= 12 eps = 3/16 < 1/2, so J >= 1/4. K_in <= 12 beta for Wilson (6 plaquettes, each at most 2 beta). HOLDS. m_in is astronomically small (about 10^{-4000}). It is not cutoff-uniform along beta_K, as the note says.

## 6. Selectivity claims (lines 54, 215-221)

- U(1) and 5D SU(2) vanishing: HOLDS. In U(1) the three imaginary parts are scalars (rank <= 1). In 5D, four vectors lie in R^3 (rank <= 3). The Gram determinant vanishes for every field. The contours and ties play no role in this.
  What it shows: in those models A_B = 0, the test of (4)-(5) is vacuous, and (8) loses m > 0, so the obstruction says nothing there. What it does not show: it is not a dynamical or gap-tracking selectivity. The vanishing tracks dim(Lie algebra) < d - 1 and nothing else. Counterexamples to reading it as a gap test: 3D compact U(1) (gapped, Polyakov / Goepfert-Mack) and strong-coupling 4D U(1) and 5D SU(2) (gapped) also have identically zero Gram determinants. 3D SU(2) has a two-vector Gram that is not identically zero. The note claims no more than "where the exclusion uses 4D SU(2)" and "no closure theorem", which is correct.
- Profile log cosh(c sin t): HOLDS. Atoms (0,+-c) with weight 1/2 give cosh(c sin t), and the origin gives 1. phi(u) = log cosh(c sqrt u) is analytic near [0,1] with linear term c^2 u/2. It is not a polynomial: cosh(c sqrt u) has zeros on the negative axis. With b = 1 the divergence (5) is zero. Clarification: in the normalization of (4) the accepted profile is B(u) - B(0) = -+32 log cosh(c sqrt u), 0 < c <= kappa, with either sign by swapping pi and nu. The positivity proof fails there because H is not entire, which is consistent. The note correctly says that acceptance by the one-link test does not mean the profile can be realized.
- Same-geometry purity separation: HOLDS. As beta -> 0 the normalized twisted integrals tend to 1, so P -> 1. At fixed geometry P -> 0 as beta -> infinity: check 1527 (iii) gives Z^0/8 <= Z_+ <= Z^0, and the order comes from row 1143 (4), which check 1548 verified. I did not re-derive row 1143 (4). Remark: d_{kappa,B} depends only on (kappa, B) and (3) holds for every input, so the separation follows from the input-independence of the theorem. It shows only that the class test is not a purity criterion.

## 7. Open step and zero-Hessian remark (lines 223-232) -- HOLDS

The display matches row 1468 4.3: (DR), (TR), (WR) with size(T) = |Lambda|, fixed a, r, delta_0, the start window x_0 in [H, W_*], the (C5) margin and the stop rule. It does not state that rho_bar stays below the end threshold, which does not change the open statement. The orbit-independence requirement matches 3.3 ("What Theorem K2 does not give"). Zero Hessian: G_y = O(A^6) at the flat field (and G = 0 on every flat field, since all P = 1), so lambda G_y does not change the transverse readout x. HOLDS. The rank term therefore cannot supply (DR) at quadratic order, and the note correctly claims no transfer from (1) to a decrement. ("Vanishes to sixth order" on line 199 means the Taylor series starts at degree six.)

## 8. Novelty against rows 1434, 1468-1500, 1544 and check 1548

I searched the gap-mech-* and gap-k2-* library files for Gram, determinant, colour rank, electric and chromoelectric. Nearest hits:
- row 1480 (library/gap-k2-integrated-activity-astra62.md 39-50): triple determinants of link vectors inside one plaquette, in a Gaussian expansion. A different object, with no obstruction.
- row 1532 (library/gap-mech-selective-fact-astra62.md; outside the listed range): a 2x2 Gram pin of two loops' imaginary parts. A different statement.
- Row 1544 Theorem A excludes globally entire actions, and Theorem B excludes fixed temporal range. Class (2) contains non-entire trace functions of unbounded range, so (3) is not implied by A or B. Row 1434 is a sign obstruction on character coefficients of a straight-product marginal and does not control colour axes at fixed traces.
Verdicts: (3), with (4), (5) and (7), is NEW. Its one-link growth method is credited to row 1544 A. The new parts are the trace-preserving labelled fields, the disc-transform class P_kappa, the subharmonic mean bound that allows zeros, and the chain-rule relative entropy. (1) is a new statement and a short corollary of Lemma V. (8)-(10) are new as statements, by the standard Gibbs-variational method. All of these are obstructions or lower bounds, not sufficient conditions, so the equivalence rule does not apply. On (K2-STEP) the row is CORRECT-NO-ADVANCE: it excludes one more closure class and leaves the step open.

## Defects (ranked; none breaks a stated theorem)

1. Line 180, (8): the hypothesis "periods at least four" (needed for (1)) is missing. Correction above.
2. Line 176: "uniformly in side" should be the explicit torus condition M > 2 eta/d_{kappa_*,B}.
3. Line 219: the accepted nonpolynomial profile should carry the normalization factor 32 of (4) and the sign choice.
4. Selectivity (lines 54, 217): the vanishing is algebraic and does not track the gap (3D compact U(1) is a gapped model with zero determinant). The note does not overclaim, but a reader should not count this as a selectivity result.

## Scope

Checked: all of library/gap-mech-k2-step-astra62.md lines 9-234, against row 1468 3.2, 3.3, 4.1-4.3, Lemma V (library/gap-pag-grow-astra.md 418-450), check 1527 (iii) lines 59-86, and check 1548. Not checked: the repo-search claims about PR branches, row 1143 (4) itself (taken via check 1548), and the release-witness facts. Hand check only; no Lean. The float run was a guide.

RESULT Image formula and |M_c| <= 1 HOLD; the moment bound (1), its probability and large-volume corollaries HOLD; the obstruction (3) with (4), (5) and the explicit exclusion HOLDS; (6) and (7) HOLD; (8) HOLDS AFTER CORRECTION (add periods >= 4); (9) and (10) HOLD; the U(1)/5D vanishing HOLDS (algebraic only, not a gap-tracking selectivity); the log cosh profile and one-link test HOLD (B - B(0) = -+32 log cosh(c sqrt u)); the purity separation HOLDS (a consequence of input-independence); the open-step statement matches row 1468 4.3 and the zero-Hessian remark HOLDS; (1), (3) and (8)-(10) are new relative to rows 1434, 1468-1500, 1544 and check 1548; CORRECT-NO-ADVANCE on (K2-STEP).
Checked line by line by Claude (Opus 5.5).
