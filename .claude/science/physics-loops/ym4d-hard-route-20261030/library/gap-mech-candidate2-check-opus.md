# Check of row 1438 (gap-mech-candidate2-astra62.md)

Checker: Claude Opus 5.5. Date: 2026-11-23 (UTC 18:48). Task row 1440.
Method: reading and hand derivation; small exact-rational / symbolic checks
with `python3 -I` in a scratch folder outside the repository.

## Plan

Items 1-9 of row 1440, in order: (1) law of H and q(H); (2) K, D, multiplier,
positivity, star disjointness, count 18; (3) reflected form (5), its limit, the
hypothesis list; (4) variance floor (6); (5) inverse-moment bound (7)-(9) and
lambda cancellation; (6) exclusion radius and m_J (10); (7) unitary and trace
identity (11)-(12), consistency with (5); (8) 5D and SU(3) test rows, separation
from seed and (W); (9) judgement against (M-neutral). Verdict at the end.

## Findings

Scratch computations: `/tmp/chk1440/s1.py`, `/tmp/chk1440/s2.py` (outside the repository). Exact
rational moment checks (Fraction); floating point only as a guide, never as a proof step.

### Item 1. Equation (1), lines 48-55. HOLDS.
- Re(xy) = x0 y0 - x.y for quaternions. With A B A^-1 = cos r + sin r Ad_A v and B^-1 = cos r - sin r v,
  q(H) = cos^2 r + sin^2 r (Ad_A v).v. Rotation of v about u by 2r gives (Ad_A v).v = z^2 + (1-z^2)cos 2r,
  so q(H) = 1 - 2 sin^4 r (1-z^2) = 1 - 2a^2(1-z^2). Checked by hand; float guide max deviation 1e-15.
- z = u.v uniform on [-1,1] (Archimedes). |H-1|^2 = 2 - 2q(H) = 4a^2(1-z^2) <= 4a^2. HOLDS.
- Conjugation invariance (conjugate A, B together; u, v uniform) and H^-1 = [B,A] (swap law). HOLDS.

### Item 2. Equations (2)-(4), lines 57-78. HOLDS.
- Q is Markov, self-adjoint for product Haar because law(H^-1) = law(H). K D = D K = I by the geometric
  series. HOLDS.
- (3): E rho_fund(H) = (E q(H)) I since E Im H = 0; E q(H) = 1 - 4a^2/3 (exact: E z^2 = 1/3). Q^k gives
  m^k. kappa = (3/4)/(3/4 + a^2/3) = 1/(1+4a^2/9). HOLDS.
- Star disjointness: a chosen bond (x, x+e_i) has x all-even, so a plaquette that contains it contains x.
  A spatial plaquette has exactly one vertex with both in-plane coordinates even, so at most one all-even
  vertex; a temporal plaquette has spatial bonds on two consecutive slices, one of them odd. So no plaquette
  reads two stars. HOLDS.
- Count: each spatial bond lies in 2(d-1) = 6 plaquettes; 3 bonds give 18 occurrences (a plaquette with two
  bonds of one star counts twice, which the telescoping bound needs). |q(g)-q(g')| <= |g-g'| and unit
  factors are isometries, so the exponent changes by at most 18 * 2a * beta = 36 beta a = beta/(2(1+beta))
  < 1/2. p e^{1/2} = 0.412 < 1. Pointwise positivity of prod_x D f_x HOLDS.
- Coarse-square attenuation kappa^2 (line 80): corner star conjugates the trace; the two mixed-corner stars
  contribute E rho(H) = kappa I and E rho(H^-1) = kappa I; the far corner has no outgoing bond. HOLDS.
  Alternative p range and factor (1-p)/(1-p+4pa^2/3): HOLDS.
- Not checked in detail: existence of the stationary infinite-time residual law (line 78); the argument
  (residual expectation = Wilson expectation of a D-transformed cylinder test, then positivity in the
  limit) is sound in outline.

### Item 3. Equation (5), lines 84-102. HOLDS, with one precision.
- Times -di and dj have separation d(i+j) >= d = R+1 unless i = j = 0. For those pairs E k(Y_s)k(Y_t)
  = E h(X_s)h(X_t) (conditional covariance zero), the Wilson moment <u, S^{b|t-s|} u>. At (0,0):
  E k^2 = E h^2 - v. Sum c_i c_j S^{bd(i+j)} = (I - S^{bd})^{2m}. Equation (5) HOLDS.
- Limit: T = M C_E M with M bounded and boundedly invertible at fixed box and C_E diagonal in Peter-Weyl
  with positive eigenvalues (GL3; I rederived c_n = 2 I_{n+1}(beta)/beta from the Bessel series and checked
  it against the Weyl integral as a guide), so ker S = 0, the spectral measure of u has no atom at 0, and
  (1-x^{bd})^{2m} -> 0 boundedly on (0,1]. Limit -v HOLDS.
- Hypotheses used: (1) conditional mean k(Y_t) with one k; (2) finite R; (3) v > 0. These are what the
  proof uses. Precision: the proof also uses (0) that the observed process h(X_t) reproduces the Wilson
  two-point function of h (implicit in "X_t = pi(U_bt)", line 84, but not listed). Only the two-point
  function of h enters, so the class is in fact larger than stated.
- Corollaries (line 90): Wilson laws at any coupling and reversible stationary Markov slice laws are
  site-RP through a slice, so they are excluded. HOLDS.

### Item 4. Equation (6), lines 104-116. HOLDS.
- Total variance over W = (kick count at the mixed-corner star, all other multipliers): Var(h|Y) >=
  P(N=1) min_{D'} Var q(H D'), P(N=1) = (1-p)p = 3/16. HOLDS.
- q(HD') = h0 c - Im H . Im D'. Conjugation invariance gives E Im H = 0, Cov(h0, Im H) = 0, isotropic
  second moment. Variance formula HOLDS.
- Exact rationals: E z^4 = 1/5; Var q(H) = 16a^4/45; E|Im H|^2/3 = 8a^2/9 - 32a^4/45; the second exceeds
  the first iff a^2 <= 5/6. v >= (3/16)(16/45)a^4 = a^4/15. HOLDS. Centre neutrality of the contractible
  square and k = kappa^2 h: HOLDS. Bound -v/2 <= -a^4/30: HOLDS.

### Item 5. Equations (7)-(9), lines 118-153. HOLDS.
- l_n <= c_n <= u_n: c_n = sum_j (beta/2)^{n+2j}/(j!(n+1+j)!); j = 0 term gives l_n; (n+1)!/(n+1+j)! <= 1
  gives u_n. HOLDS. Both series in B_J converge (sqrt((n+2)!)/(n+1)! times geometric). Guide value on
  J = [2, 513/256]: B_J ~ 35.1, C_J ~ 4.8e31.
- (8): degree-n block of the column has norm prod (n_e+1) c_{n_e}; multiplication by h (norm <= 1, one
  fundamental matrix element per distinct fine edge) shifts each n_e by +-1; triangle inequality over
  output blocks gives prod_e [sum_n (n+1)u_n sum_{k=n+-1} l_k^{-1/2}] = B_J^8. HOLDS.
- Kernel of X^*X is the Gram kernel of the columns; |.| <= B_J^16 <= C_J c_A(y,z) as c_A >= e^{-8 beta_+}.
  HOLDS.
- (9): inverse form of M C_E M at f is ||C_E^{-1/2} M^{-1} f||^2 (substitute z = Mv). M^{-1}Omega =
  C_E Phi/lambda, h commutes with M, so <hOmega, S^{-1} hOmega> = lambda^{-1} ||C_E^{-1/2} h C_E Phi||^2.
  X^*X tensor C_{E\A}, positive kernel C_{E\A} and Phi > 0 give <= C_J lambda^{-1}<Phi, C_E Phi> = C_J,
  since <Phi, C_E Phi> = <Omega, T Omega> = lambda. lambda cancels. HOLDS. Gauge-invariant restriction:
  T_full commutes with the gauge action, so the inverse form is the same on the invariant subspace. HOLDS.
- max x(1-x^2)^{2m} at x^2 = 1/(4m+1), value <= (4m+1)^{-1/2}. HOLDS (guide confirms). With
  ||(I-S^2)^m u||^2 <= max * <u,S^{-1}u>, the bound C_J/sqrt(4m+1) HOLDS.

### Item 6. Equation (10), lines 155-165. HOLDS.
- m_J = 1 + ceil((C_J/v_J)^2) gives 4m+1 > 4(C_J/v_J)^2, so C_J/sqrt(4m+1) < v_J/2. v_J = a(beta_+)^4/15
  <= a(beta)^4/15 on J. HOLDS.
- (6) is pointwise in D', so it holds for every residual law with these emissions; sum |c_i c_j| = 4^m;
  0 <= (residual form) < v_J/2 + eps 4^{m_J} - v_J gives (10). HOLDS. Volume independence follows from
  C_J. Size (guide): v_J ~ 3.0e-11, log10 (C_J/v_J)^2 ~ 84, so m_J ~ 10^84 and the radius is about
  4^{-10^84}: no practical content, as line 165 says.

### Item 7. Equations (11)-(12), lines 167-185. HOLDS, with one naming precision.
- (11): ϑ maps the kicks of F (slices t >= 1) to slices 1-t <= 0; kicks are i.i.d. per slice with one law
  (time-homogeneous, same stars on every even slice), so conditional on Y the two factors are independent
  and each averages to ϑ(conj KF), KG. HOLDS.
- Unitary: isometry by (11); every residual cylinder G' equals K(DG') with DG' a bounded cylinder test of
  the same time support, so the range is everything; null vectors go to null vectors. Positivity of the
  residual link form follows. Vacuum, centre action and the one-step shift are intertwined. HOLDS.
- Naming precision (line 172, 176): retained times 0 and 1 are fine times 0 and 2, so this "link"
  reflection of the retained chain is a fine-lattice SITE reflection through the unretained slice 1.
  Wilson has both positivities, so the statement holds; the word "link" refers to the retained lattice.
- (12): for full retained slices the Wilson link form is <Omega f_F, S^2 Omega f_G> (reversible Markov
  chain on gauge-invariant slice functions, kernel Omega^-1 S Omega per fine step); F -> S(Omega f_F) is
  an isometry onto a dense set (S injective self-adjoint, so dense range); the retained shift becomes S^2.
  Hence S_nu is unitarily equivalent to S^2 on the physical space, also on the neutral sector, and
  Tr_+ S_nu^w = Tr_+ S^{2w}. HOLDS. This is the general fact that an invertible, slice-local, time-
  homogeneous observation channel is a unitary on the OS data; its content is that the channel is an
  exact re-encoding.
- Consistency of (5) with (11): in the site form of (5) the time-0 kicks are shared by theta G and G and
  do not factor, which produces the -v; in (11) no slice is shared. No contradiction. HOLDS.
- Path projection (line 185): the note correctly limits (12) to the generated subspace there.

### Item 8. Tests table and separation, lines 187-197. HOLDS for what I checked.
- (t2) 5D: four outgoing bonds, each in 2*4 = 8 plaquettes: 32 occurrences, cost 64 beta a = 64beta/(72
  (1+beta)) < 8/9 < 1; p e = 0.68 < 1; disjointness argument unchanged; (6), (5), (11) dimension-free.
  HOLDS.
- (t3) SU(3): ||[A,B] - I|| = ||AB - BA|| <= 2||A-I|| ||B-I|| = 8 sin^2(r/2) <= 4 sin^2 r (cos^2(r/2)
  >= 1/2 for r < pi/2). |Re tr Z|/3 <= ||Z||, so 18 occurrences cost <= 72 beta a < 1, p e < 1. Positive
  conditional variance: Re tr H/3 takes the value 1 (commuting pair) and a value < 1 (noncommuting pair in
  the SU(2) block), with positive-probability neighbourhoods; the residual charges every open set because
  D f >= c f. Conditional mean real since law(H^-1) = law(H). Injectivity of the SU(3) electric
  convolution: e^{beta Re tr/3} expands in (tr g)^a (conj tr g)^b with positive coefficients, and every
  irrep occurs in some fund^a (x) antifund^b. HOLDS (qualitative v > 0 only; no SU(3) analogue of (6) is
  given or needed for (5)).
- (t1) U(1): the commutator word is the identity. Precision: by check 1431 a U(1) zero of this kind is
  kinematic, not a selectivity test; moot here, since the SU(2) gain is also exactly zero by (12).
- (t4): 1 - kappa = O(beta^-2) and floor O(beta^-4): HOLDS.
- Separation (line 187): row 1135 §6 lines have bond eigenvalue e^{-ma} at d = 2 with multiplicity 4 per
  line (I read §6), centre acts trivially, so the product has at least 4n^3 neutral levels at ratio
  e^{-m_0 a}; at time 2w_j this gives at least 4n^3 e^{-m_0 L/512} -> infinity. The star factor acts on the
  Wilson factor only, so (1)-(4) survive. HOLDS. DOB direction: check 1436 item 7 (I re-read it) gives
  the seed at fixed beta < 2/9 for n >= 2048; (5) holds at every beta > 0. HOLDS.
- Not checked: the (W) bounded-excess clause (definition of (W), additivity of excesses, and
  F((2n)^4) <= 16 F(n^4)); the prior-work table, lines 33-40, against rows 1380-1437; the chain in the
  RESULT paragraph beyond the two elementary inequalities s/(1+s) <= 4/25 iff s <= 4/21 and
  s(u) <= 1/2 => s(3u) <= 1/8, which HOLD.

### Item 9. Judgement.
- Does it move (M-neutral)? No. (1)-(4) are an exact positive re-encoding of the Wilson block law; (12)
  proves the re-encoding carries exactly zero change of the neutral spectrum, which is the lane rule
  "Equivalent is not progress" as a theorem for this class. (5), (6), (10) are the genuinely new content:
  the residual is not site-reflection-positive through a kept slice, so it cannot be read as a lattice
  gauge law (Wilson at any coupling, or a reversible Markov slice law) to feed a further transfer or RG
  step. That is a negative for a class, not a step toward the seed.
- Is the class stated precisely? Mostly yes. Exclusion (5): residuals whose same-slice observation has a
  one-slice conditional mean, finite conditional covariance range and v > 0, with the omitted hypothesis
  (0) of item 3. Zero gain (12): time-homogeneous slice-by-slice probability channels with an inverse on
  cylinder tests and the gauge and centre symmetries, on full retained slices. The RESULT's "closes the
  stated class of carries" is accurate. The open remainders (effective-interaction bounds, transitions that
  change later states, readers across the cut) are listed honestly. Not selective: (5) and (11) hold in
  5D and for SU(3), as the note says.
- Next row 1 is this check.
- Next row 2 (temporal plaquette across the cut). Well posed after two clarifications: (a) name the
  reflection: the fine link reflection through the slab mid-plane, which maps slab [2t,2t+1] to
  [-2t,-2t+1] and fixes the slab-0 observable, so slab 0 is the residual's site; (b) state which emission
  gives the floor v_J for a temporal plaquette (v_J is copied from (6), which is about a spatial coarse
  square; a star kick on the even-slice bond of the temporal plaquette gives a one-kick branch of the same
  q(HD') form, but the note does not say this). The necessity claim and the monotone limit
  (lines 205-210) HOLD by the argument of (5) with lag-k moment <A Omega, S^{2k-1} A Omega>.
- Exact reduction (mine, by hand, checked by no one). In temporal gauge the temporal plaquette at link l is
  q(U_l U'_l^-1), so T[q_p] = M (C_l[q] (x) C_rest) M with C_l[q], C_l[q^2] diagonal in Peter-Weyl with
  eigenvalues c_k'(beta), c_k''(beta). The same algebra as (9) gives exactly
      <Omega,B Omega> - ||S^{-1/2} A Omega||^2 = sum_k rho_k (log c_k)''(beta),
  rho_k = lambda^-1 c_k <Phi_k, (1 (x) C_rest) Phi_k> >= 0, sum_k rho_k = 1, Phi_k the spin-k part of
  Phi = M Omega on link l: a vacuum average of (log c_k)'' over the electric spin on one link. Guide
  (exact rationals at beta = 2, truncated series): (log c_k)'' = 0.163, -0.117, -0.391, -0.659, ... for
  k = 0..3, so the sign is decided by how much vacuum weight link l has at spin 0. Feasibility: deciding
  this rigorously at beta in [2, 513/256], uniformly in n (or refuting it at one n >= 4), needs two-sided
  bounds on the one-link electric-spin distribution of the Wilson vacuum at beta ~ 2. Nothing on file
  supplies that (cluster-type bounds stop near beta < 2/9; the pointwise ratio bounds of (9) cost factors
  of order e^{6 beta} and cannot fix the sign). My judgement: not feasible as a rigorous row with the tools
  on file; the test is equivalent to a nonperturbative vacuum estimate. The reduction above should be
  checked before the row is queued.

## Verdict

HOLDS. No failing line. Precisions, none of which changes a conclusion: (i) line 84-88, the hypothesis
list omits that the observed h-process reproduces the Wilson two-point function; (ii) lines 172/176,
"link reflection" of the retained chain is a fine site reflection through an unretained slice; (iii) line
193, the U(1) zero is kinematic (check 1431); (iv) next row 2 needs the reflection and the emission for
v_J stated.

Verified: items 1-7 line by line, the 5D and SU(3) rows, (t4), the line-spin and DOB separations, two
elementary chain inequalities. Not verified: existence of the infinite-time residual law in detail; the
(W) excess clause; the prior-work table; the literature quotations; the chain to the mass gap. My
reduction of next row 2 is mine and unchecked. Float computations are guides only.
