lead: Claude Opus 5.5 (lead session), dispatched 2026-11-17
row: 1109

Writer: Claude Fable 5.2, effort medium, laptop subagent. This file is the working
memory of row 1109. Each step appends its result. No mass gap is claimed.
What this file does not cover is listed in the last section (filled at the end).

Note on the save protocol: one read call (the grep of row 1109 in FINISH.md) ran
before this file was created. Nothing else ran before it.

# gap-descent-first-case: (GH2-DESC) in the model GH2_2(beta_L, beta_M)

## 0. Plan (eight steps at most)

1. Read the named sources (row 1108 sections 4.1 and 6.2; gap-bridge-vectors-max
   L220-240, L350-385; gap-descent-sign; gap-checkerboard-singlet-astra; row 1112
   if present). Write the exact statement and notation here.
2. Lemma KIN in GH2_2: transfer matrix in temporal gauge on a strip, the
   beta_L-dependence as a heat-kernel factor on each spatial link; state what
   replaces the operator-norm step of Proposition DIL.
3. Integrate the two-dimensional gauge field exactly (axial gauge, independent
   plaquette variables). Write the result as a weight on the colour flux across
   cuts.
4. Test whether the flux weight acts on neutral pair states only by lifting them.
   Decide between proof and refutation of the monotone form.
5. Interpolation in w = e^(-t/4) between the two proved ends (Corollary KIN-D),
   if steps 2-4 leave it needed.
6. Run the required tests: compact U(1) at large beta_M, frozen Q_8 (KIN-7),
   Example KIN-6, a product with a massless factor, GH-NA.
7. Optional small numeric guide (one job, /tmp scratch) if a sign must be seen.
8. Marks, what is not covered, RESULT line.

## Step 1 result: sources read, the statement, the notation. DONE.

**Read by me.** FINISH row 1109. Row 1108 (`gap-br2-direction-fable.md`) sections 4.1 and 6.2 in full. `gap-bridge-vectors-max.md` L215-242 and L296-390 (GH2, Lemma CB-L, Lemma GH2-0, Proposition CB-CH, (SING), Lemma KIN, KIN-1 to KIN-7, KIN-D, KIN-CVX). `gap-descent-sign.md` in full (Lemma TP-2, Lemma SC, Proposition DIL, the three failed ways of step (S)). `gap-checkerboard-singlet-astra.md` L187-300 (Lemma DEC) and L608-712 (Lemma GH-NA, (GH5), (GH6)). `library/prior/gap-gauged-sigma-read-luna.md` (row 1112) in full; it arrived during step 1 by a lead pull.

**Literature (read by gpt-6-luna in row 1112, not by me).** Row 1112 reports: no theorem and no monotonicity result is known for the two-dimensional SU(2) gauge-Higgs model, the gauged O(4) model or GH2. The SU(2) evidence (Gongyo, arXiv:1402.7124) is numerical; it speaks of a crossover "or possible first-order behavior". The large-N result of Bardeen, Lee and Shrock gives a model-specific tendency only. Bighin et al. (arXiv:1907.06253) find, in two coupled XY layers, a phase where one-copy correlations decay and a composite mode stays massless. I use these as test patterns in step 6. I did not read the papers.

**The model.** Sites u of a finite box in Z^2 (free subgraph or torus). Links a_e in SU(2). Two fields Phi_1, Phi_2 with values in SU(2) = S^3. Re g = (1/2) tr g. b = beta_M.
  d mu proportional to prod_p e^(beta_L Re a_p) . prod_(i = 1, 2) prod_(e = uv) exp( b Re( Phi_i(u)^(-1) a_e Phi_i(v) ) ) da dPhi.
Local gauge group: a_e to g(u) a_e g(v)^(-1), Phi_i(u) to g(u) Phi_i(u). Rigid group K = SU(2) x SU(2): Phi_i to Phi_i k_i. The heat-kernel form replaces e^(beta_L Re a_p) by the heat kernel h_t(a_p); beta_L = infinity is t = 0 and beta_L = 0 is t = infinity. lambda_j is the character coefficient of the plaquette weight: I_(2j+1)(beta_L)/I_1(beta_L) (Wilson), e^(-t j(j+1)) (heat kernel).

**The two forms.** Weak form (W): abs(Cov(F, tau_n H)) <= C_(F,H) e^(-a n) for gauge-invariant local Lipschitz F, H, with a = a(b) > 0 for all beta_L and all boxes named in the brief. Monotone form (M): rate(beta_L) >= rate(infinity), where rate is the best a.

**Gauge-invariant coordinates (argued; one line each).**
- rho(u) = Phi_1(u)^(-1) Phi_2(u) and v_e = Phi_1(u)^(-1) a_e Phi_2(v) for e = (u to v) are gauge invariant. In the gauge Phi_1 = 1 they are all the variables: a_e = v_e rho(v)^(-1).
- The Higgs part is b sum_e ( v_e . rho(u) + v_e . rho(v) ), the dot being the inner product of unit quaternions. This is the O(4) ferromagnet of Lemma DEC on the decorated lattice, with v_e as the midpoint spin. So the midpoint spin of Lemma DEC is the gauge link itself in these coordinates.
- The plaquette with corners 1, 2, 3, 4 and edges 12, 23, 43, 14 gives Re a_p = Re( v_14^(-1) v_12 rho_2^(-1) v_23 v_43^(-1) rho_4 ). So GH2_2(beta_L, b) is the decorated O(4) ferromagnet at coupling b plus beta_L times a six-spin term, the real part of an alternating product around the plaquette. K acts by rho to k_1^(-1) rho k_2, v to k_1^(-1) v k_2.
- At beta_L = infinity: a is a pure gauge, and the gauge-invariant functions are the functions of two free O(4) sheets Psi_1, Psi_2 that are invariant under one common left rotation. There rho = Psi_1^(-1) Psi_2, and E[rho(0) . rho(x)] = c(x)^2, with c the O(4) two-point function at coupling b (the conjugation average of a unit quaternion is its real part).

**Which channels set the rate at beta_L = infinity (argued).** A single sheet particle has left colour 1/2. It is not invariant under the common left rotation. A pair is: two on one sheet, or one on each sheet. So the rate at infinity is a two-particle rate, 2m, if m is the rate of c(x). This agrees with row 1108 section 4.1.

## Step 2 result: Lemma KIN in GH2_2, and the bound per unit length (way 1). DONE: lemma argued by hand; the bound per unit length FAILS at a written point.

**Setting.** Slice {1, ..., n} with free ends. Slice variables: a(k) on the link (k, k+1), k < n; Phi_i(k), i = 1, 2. H = L^2 with Haar measure. Slice gauge group g(k). V = - b sum_(i, k<n) Re( Phi_i(k)^(-1) a(k) Phi_i(k+1) ). K_a = product over k of convolution by the plaquette weight w_L on a(k). K_Phi = product over (i, k) of convolution by the normalised e^(b Re) on Phi_i(k). T = e^(-V/2) K_a K_Phi e^(-V/2) on H^G. G = SU(2) acts on the Phi variables by one common left rotation. K = L^2(Phi)^G. For a cut k < n let rho_k(W) multiply Phi_i(k') on the left by W for all k' > k and both i. J_k is its generator: the colour charge to the right of the cut. C_k = J_k . J_k.

**Lemma KIN-G (argued by hand; it is Lemma KIN of row 1076 for this slice).**
(a) R f(Phi) = f(1, Phi) is unitary from H^G to K.
(b) R T R^(-1) = S* D S, S = K_Phi^(1/2) e^(-V_f/2), V_f = V at a = 1 (two free O(4) chains), D = prod_k M_k, M_k = sum_j lambda_j P_k^j, P_k^j the projection on C_k = j(j+1). Heat kernel: D = e^(-tN), N = sum_k C_k.
(c) The C_k commute with each other and with K_Phi.
Proof. (a) On a path with free ends the gauge a = 1 is reached by g(1) = 1, g(k+1) = g(k) a(k); what is left is one common rotation. (b) For gauge-invariant f, f(a(k) = W, other a = 1, Phi) = f(1, rho_k(W) Phi): use g = 1 at sites up to k and g = W after. So R K_a R^(-1) = prod_k int w_L(W) rho_k(W) dW, and for a class function w_L the integral int w_L(W) D^j(W) dW is lambda_j times the identity (Schur). (c) rho_k and rho_k' are left rotations of nested sets of variables by independent elements; their Casimirs commute. K_Phi is a product of convolutions on the right, or by class functions; it commutes with left rotations. QED

**The same statement in the measure (argued).** In temporal gauge on a box with free boundary, the spatial link a_k(tau) is a random walk on SU(2) in tau with independent steps of law w_L, independent for different k, tilted by the two Higgs partition functions. So the gauge field is a product of n - 1 independent walks of twists, and D is its one-step operator. At beta_L = infinity the walks do not move.

**Per cut, Proposition DIL keeps its form.** For the operator with the weight on one cut k alone, T_k = S* M_k S, the proof of Proposition DIL gives (heat kernel) m_k(t) - m(0) >= - 2 t <Omega_f, C_k Omega_f>, because the second smallest value of C_k on K is 0. The loss is one number per cut. It does not depend on n. For all cuts the losses add. That is the volume factor of row 1081 in its exact place: **the bound charges each cut for the vacuum's own flux and gives the excited state no credit for carrying the same flux.**

**What a bound per unit length must compare.** By Identity KIN-5, where lambda_1 is simple,
  dm/dt = sum_k ( <C_k>_1 - <C_k>_0 ),
with <.>_i the mean in the unit eigenvector phi_i(t). A bound per unit length is a bound on each term that is summable in k. Write J_k = J_k^1 + J_k^2 (the two sheets). Then C_k = (J_k^1)^2 + (J_k^2)^2 + 2 J_k^1 . J_k^2.

**Lemma FACE-FLUX (argued by hand).** At beta_L = infinity the vacuum Omega_f of S* S on K is the product of the two one-sheet vacua, and <Omega_f, C_k Omega_f> = 2 q_k, q_k = <(J_k)^2> in the one-sheet vacuum. The cross term is 0.
Proof. S* S is a tensor product of the two chains. Each chain commutes with its own left rotation. Each one-sheet vacuum is unique and positive (Perron-Frobenius, as in Corollary KIN-3), so it is invariant under its own left rotation and <J_k^i> = 0 in it. The product is G-invariant and is the top vector. Then <J_k^1 . J_k^2> = <J_k^1> . <J_k^2> = 0. QED

**The decomposition of the excess for a pair (argued; physics reasoning; not a proof).** Take a face state with one particle on each sheet, total left colour 0, the particles at x < y. For a cut between them the charge to the right is the colour 1/2 of one particle plus vacuum fluctuations: the excess is 3/4 plus a correction. For a cut outside it is a correction only. So
  sum_k ( <C_k>_1 - <C_k>_0 ) = (3/4) <abs(x - y)> + (self term) + (contact term).
- The string term (3/4) <abs(x - y)> is non-negative. This is the mechanism of row 1108 section 4.1.
- The self term is sum_k ( <(J_k^i)^2> in a one-particle state minus q_k ), for each sheet. It is a property of one O(4) chain. Its sign is not known. A particle can lower the flux fluctuation of the vacuum near itself.
- At t = 0 on a long strip the pair is free, <abs(x - y)> grows like n, and the string term wins. For t > 0 the pair is bound, <abs(x - y)> is finite, and the self term is of the same order.
- The same two terms are in 't Hooft's two-dimensional model (recalled, not read here): the linear potential lifts the pair, and the self-energy lowers the mass squared of each quark by g^2/pi.

**Where way 1 stops (the written failure).** A bound per unit length needs the sign of (string term + self term) for the true excited vector at each t. I found no operator inequality for it. No inequality that uses only Lemma KIN-G, D <= 1, D = 1 on flux-free states, positivity of the kernel and a gap at the face can give it: frozen Q_8 has all of these, and there (M) is false (Example KIN-7 on a small box; step 4 below argues it in infinite volume). The self term needs the one-particle states of the O(4) chain, which the posted theorems do not give. **Way 1 FAILS at the self term. Scope: this is about the methods named; it does not say the sign is negative.**

## Step 3 result: the gauge field integrated exactly (way 2, first half). DONE: two exact forms, argued by hand.

**Form A, independent plaquette variables (argued).** Box with free boundary. Axial gauge: a = 1 on the links of direction 0 and on the spatial links of the row tau = 0. Then the plaquette variables P_k(tau) are independent with law w_L, and a_k(tau) is the ordered product of P_k(tau'), tau' < tau. Put g(k, tau) = a_1(tau) ... a_(k-1)(tau) and Psi_i = g Phi_i. The spatial bonds of Psi_i carry no twist. The time bond at (k, tau) carries the twist U_k(tau) = g(k, tau) g(k, tau+1)^(-1), the holonomy of the plaquettes of row tau to the left of column k. Because w_L is a class function, U_k(tau) is a random walk in k with independent steps of law w_L, and the walks of different rows are independent. So: **the gauge field is one independent SU(2) walk per row of plaquettes; the two sheets see it as a common left twist on their bonds across that row; the twist at column k has the heat-kernel law at time t times the area to the left.** This is the Euclidean form of D in Lemma KIN-G.

**Form B, loops (Lemma LOOP; argued by hand).** Write Phi in S^3 inside R^4 = quaternions, and L_a for left multiplication by a, an element of SO(4). Then Re(Phi(u)^(-1) a Phi(v)) = Phi(u) . L_a Phi(v). For one sheet in a fixed gauge field,
  Z_Phi(a) = int prod_u d omega(Phi(u)) prod_e exp( b Phi(u) . L_(a_e) Phi(v) ) = sum over loop configurations omega of p(omega) prod over loops l in omega of Re(a_l),
with p(omega) >= 0 independent of a, and a_l the holonomy of a around the loop l.
Proof. Expand each exponential: sum over n_e of (b^(n_e)/n_e!) (Phi(u) . L_(a_e) Phi(v))^(n_e). At each site use the moments of the uniform measure on S^3: int s_(i_1) ... s_(i_(2k)) d omega = c_k times the sum over pairings of the product of Kronecker deltas, c_k = 1/(4 . 6 ... (2k+2)) > 0, odd moments 0. A choice of pairings at all sites joins the strands into closed loops. Each loop gives the trace over R^4 of the ordered product of the L_(a_e) along it, and tr L_g = 4 Re g. A loop run backwards gives the same real part. So p(omega) = prod_e (b^(n_e)/n_e!) prod_u c_(k_u) 4^(number of loops). QED
Consequences (argued by hand).
- Diamagnetic bound: 0 < Z_Phi(a) <= Z_Phi(1) for every a, since abs(Re a_l) <= 1. Credit: the bound and the walk expansions are those of Brydges, Frohlich and Seiler and of Symanzik (recalled; not read here).
- With E_YM the two-dimensional Yang-Mills mean at beta_L and omega = (omega_1, omega_2) the loops of the two sheets:
  Z_GH2 / ( Z_YM Z_Phi(1)^2 ) = sum_omega pbar(omega_1) pbar(omega_2) W(omega), W(omega) = E_YM[ prod_(l in omega) Re(a_l) ], abs(W) <= 1, W = 1 at beta_L = infinity,
  pbar = p / Z_Phi(1) a probability. So Z_GH2 <= Z_YM Z_Phi(1)^2.
- W is computed by form A. On a cut (one link at one time) the strands of omega that cross it carry the colour (1/2)^(tensor n). The gauge field projects on the total spin J of these strands and gives lambda_J per plaquette step. This is "a weight on the colour flux across cuts".

**Hand values of W (one region of area A; A a single loop variable with E chi_j(A) = (2j+1) lambda_j^A).**
- One simple loop: W = lambda_(1/2)^A. Area law.
- Two loops around the same region (one strand of each sheet, or two of one sheet): Re(A)^2 = (1 + chi_1(A))/4, so W = (1 + 3 lambda_1^A)/4. It stays above 1/4. The colour-0 channel of the two strands pays no area cost. This is the neutral pair.
- One loop that runs twice around the region: Re(A^2) = (chi_1(A) - 1)/2, so W = (3 lambda_1^A - 1)/2. **It is negative when lambda_1^A < 1/3**, and equals -1/2 at beta_L = 0 (check: Haar mean of cos 2 theta with density sin^2 theta is -1/2).
So W is a signed weight on loop configurations.

## Step 4 result: the lift test (way 2, second half). DONE: the test is answered; way 2 FAILS as a proof; one argued counterexample for the test group Q_8 in infinite volume.

**Question.** Does the flux weight act on the neutral pair states only by lifting them?

**Answer in three parts.**

**(i) For each level alone: yes (on file).** 0 <= D <= 1 and D = 1 on flux-free vectors, so every eigenvalue of S* D S is at most that of S* S (Corollary KIN-1). In loop form: abs(W) <= 1. A neutral pair of strands keeps the colour-0 channel at no cost and loses the colour-1 channel (step 3, second hand value).

**(ii) For the gap: the weight does not decide it.** The gap is a level minus the vacuum level, and the vacuum is lifted too, by an amount per unit length. Two written facts show that "lifting only" has no relative form.
- The loop weight W has both signs (step 3, third hand value). So abs(W) <= 1 bounds the partition function and no normalised mean: numerator and denominator both go down. A gauge-invariant mean at beta_L is not bounded by its value at infinity by this route.
- **Example Q8-INF (argued counterexample to (M) for frozen Q_8; leading order of the low-temperature expansion, not written out).** Take GH2_2 with Q_8 in place of SU(2) and b large. At beta_L = infinity each sheet is ordered; its cheapest wall, a jump by q = +-i, +-j, +-k, has bond weight e^(0)/e^(b) = e^(-b). A truncated correlation over time n needs a tube of two walls, so rate(infinity) = 2b + o(1). At beta_L = 0, by the sum in Lemma GH2-0 over the eight elements, the bond weight of rho is f(q) = (1/8) sum_a exp( b (Re a + Re(a q)) ):
    f(1) = (e^(2b) + e^(-2b) + 6)/8, f(i) = (2 e^b + 2 e^(-b) + 4)/8, f(-1) = 1.
  So the wall weight is f(i)/f(1) = 2 e^(-b) (1 + o(1)), and rate(0) = 2b - 2 log 2 + o(1) < rate(infinity). The factor 2: on each wall bond the link can sit at a = 1 or at a = q^(-1), that is, the jump can be in either sheet. The gauge field gives the wall an entropy. This is Example KIN-7 without a box.

**(iii) Reading: the sign of the effect follows the phase (argued).** Lowering beta_L lowers the stiffness of the gauge-invariant field: at beta_L = 0 the stiffness of rho at alignment is below b/2 (Lemma GH2-0), against b for each sheet at infinity. In an ordered phase the rate is a wall cost and falls with the stiffness (Q8-INF). In a disordered phase the rate is an inverse correlation length and rises when the stiffness falls. So (M) is the statement "the sheets are disordered at the scale where the gauge field acts". For SU(2) on a box smaller than the correlation length of the sheet, the sheet looks ordered. That is the place of the dips on small boxes at large beta_M (row 1085, row 1090; guide there). So no bound uniform over small boxes can hold, and a proof of (M) must work at scales above the correlation length of the O(4) sheet.

**The scales for SU(2) (argued; physics reasoning with recalled exponents; guide grade).** Let xi = 1/m be the sheet's correlation length, of order e^(pi b) at large b.
- beta_L far above b xi^2: the string tension is below m^2. The pair picture of step 2 holds and the lift is the string term. This is the region R_eps.
- beta_L between order one and b xi^2: the gauge field acts at a scale below xi, where the sheets are stiff. It removes the common mode of the two sheets and leaves rho with stiffness near b/2. The rate of rho is then of order e^(-pi b/2) times the gauge scale. It is above 2m. The lift here is the loss of stiffness. It is not the string.
- So at guide grade (M) holds for SU(2) on the whole line, by two different mechanisms, and the pair mechanism of row 1108 section 4.1 covers only the first region.

**Where way 2 stops (the written failure).** The exact gauge integration gives a signed weight on loops and the operator D. Neither gives a comparison between the pair and the vacuum. The mechanism "the flux weight only lifts neutral pairs" is exact for levels and is false as a statement about gaps in the class of the lemma (Q8-INF). For SU(2) in the middle region it is not the acting mechanism at all. **Way 2 FAILS as a proof of (M), and gives no bound for (W).** For (W) the first unprovided input is unchanged from row 1084: the covariance of two plaquette traces under the annealed law (GH5).

## Step 5 result: the two ends and the interpolation in w (way 3). DONE: one finding on the ends; way 3 FAILS at a written point, with a hand example.

**The ends, form by form (argued).**
- For (W) both ends are on file, given OpenAI's Theorem 3.1: two free sheets at beta_L = infinity; Lemma DEC at beta_L = 0, with the rate 2c/Xi(b) of (DEC4).
- For (M) neither end comparison is on file. (M) compares true rates. Theorem 3.1 gives a lower bound with constants that are not named, at each end. So even (END-0): rate(0) >= rate(infinity), that is, "the rate of the decorated O(4) model at coupling b is at least twice the rate of c(x)", is open. A sufficient form is E_DEC[rho(0) . rho(x)] <= C c(x)^2.
- Guide for (END-0), by hand, leading orders at small b (not checked by a second reader): with u = I_2(b)/I_1(b) the one-bond mean, directed paths give the rate of c as - log u - 2u + O(u^2). The decorated model has the one-bond mean u^2 between rho sites, so its rate is - 2 log u - 2 u^2 + ... . The difference rate(0) - 2 rate(c) is 4u + O(u^2) > 0. At large b the stiffness argument of step 4 gives the same sign. For Q_8 at large b the sign is the other one (Q8-INF). So (END-0) is selective in the same way as (M).
- Consequence: **the weak form is the form whose two ends are theorems. A proof of the monotone form needs sharp rates at both ends first, and no file has them.**

**The interpolation.** By Corollary KIN-D, T(w) = sum_k w^k A_k with A_k = S* P_k S >= 0, w = e^(-t/4) in [0, 1]; T(0) = A_0 is the end beta_L = 0 and T(1) = S* S is the face. Three things were tried.
- (3a) Order. T(w) is non-decreasing in w as an operator, and abs(<f, T(w) g>) <= <f, T(abs w) f>^(1/2) <g, T(abs w) g>^(1/2). This orders each level between its end values. It gives lambda_1(w)/lambda_0(w) <= lambda_1(1)/lambda_0(0), and the right side has the volume factor (Corollary KIN-2).
- (3b) Convexity. log lambda_0 and log(lambda_0 lambda_1) are convex in t (Lemma KIN-CVX). The gap is their difference: 2 log lambda_0 - log(lambda_0 lambda_1). End values of a difference of two convex functions do not bound it inside.
- (3c) Three lines. A bound inside from the two ends by a maximum principle needs a function that is analytic in w and whose modulus is the quantity bounded. A covariance is a ratio with the partition function Z(w) below. For complex w the weights are complex, abs Z(w) <= Z(abs w) is all that KIN-D gives, and Z can vanish. A zero-free neighbourhood of [0, 1] uniform in the box is the lane's Route Z with its crux Z6 (on file as open). Not redone.

**Example INT-2 (argued counterexample to the interpolation step in the class of Corollary KIN-D; by hand).** On C^2 let Lambda = diag(1, e^(-m)), U the rotation by a small angle theta, S = U Lambda^(1/2), N = diag(a, 0) with a > 0. Then S* S = Lambda and
  T(w) = Lambda^(1/2) U^T diag(w^a, 1) U Lambda^(1/2), entries T_11 = w^a cos^2 + sin^2, T_22 = e^(-m)(w^a sin^2 + cos^2), T_12 = e^(-m/2) sin cos (1 - w^a) >= 0.
- It has the whole structure: T(w) = sum of w^k times positive operators, a non-negative kernel, irreducible for 0 <= w < 1 and theta not 0, N >= 0 with a flux-free vector.
- End w = 1: gap m. End w = 0: T(0) has rank one, the gap is infinite.
- At theta = 0 the two levels cross at w^a = e^(-m). For small theta the gap at that w is of order theta. So the interior gap is as small as wanted while both end gaps stay at least m.
This is Example KIN-6 with c = 0 and a small mixing. In the model a crossing of this kind is a first-order transition in beta_L between the face vacuum, which carries flux 2 q_k on each cut (Lemma FACE-FLUX), and the flux-free vacuum of beta_L = 0.

**Where way 3 stops (the written failure).** The two ends and the positive power series do not exclude a level crossing inside. The missing statement is (NO-1ST): for b in the window there is no first-order transition in beta_L, with a gap bound uniform in the box. It is not weaker than (W). First-order transitions do occur in two-dimensional models with a continuous non-abelian symmetry when the bond weight is sharply peaked (van Enter and Shlosman; recalled, not read here). Row 1112 (read by luna) quotes Gongyo's numerical paper on this same model family: a crossover "or possible first-order behavior" in the Higgs coupling. The bond weight of GH2_2 at beta_L = 0, omega(b abs(rho + rho')), is not sharply peaked, and no transition is expected (belief). **Way 3 FAILS at (NO-1ST).**

## The named step, and the stop

**Named step (INT-CMP).** A comparison, uniform in the box, between the first neutral level and the vacuum level of S* D S at interior beta_L in (0, infinity), for b in the window. (M) needs its sign form: sum_k (<C_k>_1 - <C_k>_0) >= 0 in the limit of long strips. (W) needs its bounded form: the ratio lambda_1/lambda_0 stays below e^(-a) with a = a(b) > 0.

**It failed in three written ways, none by association.**
1. Way 1 (Lemma KIN-G, bound per unit length): stops at the self term of the flux excess (step 2).
2. Way 2 (exact gauge integration, lift test): the weight is signed on loops and lifts the vacuum too; Q8-INF shows the lift statement is false for gaps in the class of the lemma (steps 3 and 4).
3. Way 3 (interpolation in w): Example INT-2; the missing statement is (NO-1ST) (step 5).
By the stop rule of the brief the row stops here. Neither form is proved. The monotone form is not refuted for SU(2). Scope: the three failures are about the methods as I applied them. They do not say that (INT-CMP) is false or cannot be proved.

## Step 6 result: the required tests. DONE.

There is no proof to test. Each test is applied to the statements argued above, and to what a later proof must do.

| Test | Result |
|---|---|
| Compact U(1) in GH2_2 at large b ((W) is false there) | Lemma KIN-G, form A, Lemma LOOP (loop weight cos of the holonomy angle), the diamagnetic bound and Lemma FACE-FLUX hold for U(1) with its own characters. None of them gives clustering, so none is refuted. The pair picture of step 2 stops for U(1): the sheets have no massive particle at large b. Row 1112 (read by luna) adds the pattern of Bighin et al.: one-copy correlations can decay while a composite mode stays massless. In GH2_2 this is the warning already in (GH6): decay of charged correlations does not give decay of neutral ones. |
| Frozen Q_8 (KIN-7) | Example Q8-INF argues that (M) is false for Q_8 at large b in infinite volume. Every statement argued here holds for Q_8. So nothing here proves (M) for a class that contains Q_8, as it must be. A proof of (M) must use disorder of the sheets at the scale of the gauge field (step 4 (iii)). |
| Example KIN-6 | Example INT-2 is KIN-6 with a small mixing. No statement here takes a sign from the form S* e^(-tN) S alone. |
| A product with a massless factor | (W) is a statement on all gauge-invariant local observables. Lemma KIN-G and Lemma LOOP hold for a product model and give no clustering. Not refuted, nothing gained. |
| GH-NA | No step uses association, monotone coordinates or FKG. The negative loop weight of step 3 is a second sign obstruction of the same family, in loop language (argued). |

**What a proof must use, collected (argued).** (1) The gap of the sheet as an input (U(1)). (2) Decay of the charged correlations, or another statement that the sheets are disordered at the scale where the gauge field acts (Q_8). (3) Scales above the sheet's correlation length; no bound uniform over small boxes (step 4 (iii), and the guide of step 7). (4) The absence of a first-order transition in beta_L (INT-2). (5) For (M): sharp rates at the ends (step 5).

## Step 7 result: one small guide run (guide; discharges no step). DONE.

**What was run.** GH2_2 on the two-site strip, the sector that is invariant under the gauge group and under K. There the functions are those of B_i = Phi_i(2) Phi_i(1)^(-1), i = 1, 2, under one common conjugation. In the basis (j_1, j_2, j_3) of row 1081 (two-sheet box): K_Phi = lambda_(j_1)(b)^2 lambda_(j_3)(b)^2, V_f = - b (Re B_1 + Re B_2), and the one cut gives D = lambda_(j_2)(beta_L), N = j_2(j_2+1). So the operator is that of row 1081's kill test B with the flux weight on j_2 alone. Script: a copy of `runs/gap-descent-sign/su2box.py` with this one model added, written in /tmp scratch and copied by the lead to `runs/gap-descent-first-case/` (`gh2strip.py`, `gh2strip_long.py`, logs `log_gh_14.txt`, `log_gh_18.txt`, `log_gh_long_14.txt`, and the JSON outputs). Serial, nice 10, one BLAS thread. Python ran with -I; numpy was added from the user site path by hand.

**Not covered by the run.** The K-charged sector (the rho channel). Strips with three or more sites. Infinite volume. The rate of a two-site strip is not the rate 2m of step 1.

**Values (truncation 2Jmax = 14; 18 agrees to all printed digits for b <= 4, to 3 x 10^(-6) at b = 8; b = 12 at 18 alone).**
| b | m(infinity) | m(beta_L = 0.05) - m(infinity) | least m(t) - m(0), t in (0, 20] | least n_1 - n_0 |
|---|---|---|---|---|
| 2.3 | 2.28072 | +0.811 | +1.28e-3 (first grid step) | above 0 on the grid |
| 2.4 | 2.28299 | +0.715 | +1.29e-3 | above 0 |
| 2.6 | 2.29504 | +0.543 | +1.32e-3 | above 0 |
| 2.8 | 2.31302 | +0.397 | +1.37e-3 | above 0 |
| 3.0 | 2.33335 | +0.276 | +1.45e-3 | above 0 |
| 3.2 | 2.35381 | +0.179 | +1.55e-3 | -0.016 at t = 1.5 |
| 3.5 | 2.38226 | +0.071 | +1.71e-3 | -0.047 at t = 1.5 |
| 4 | 2.42108 | -0.030 | below 0 | -0.079 at t = 1.0 |
| 8 | 2.54032 | -0.045 | below 0 | -0.102 at t = 0.3 |
| 12 | 2.57384 | -0.026 | below 0 | -0.115 at t = 0.15 |

**Reading (guide).**
- In the window the neutral gap of this strip rises from 2.28 to about 3.0 as beta_L goes from infinity to 0, and the derivative form holds on the grid. No refutation of (M) in the window on this strip.
- The derivative form (FLUX-EXC) fails on this strip from b between 3.0 and 3.2. The end-point form fails from b between 3.5 and 4. **So for SU(2) itself the monotone form is false on a small strip at b = 4 (guide).** The sudden change of the least n_1 - n_0 between 3.0 and 3.2 has the look of a crossing of two excited levels; I did not resolve it.
- This is the pattern that step 4 (iii) predicts: a box that the sheet sees as ordered gives a dip. The first failure, near b = 3.1, is not far above the window's top, 2.6, on the smallest strip. Row 1090 saw its crossing come down with the box. Prediction, not tested: on strips with n between a few sites and the sheet's correlation length the dip reaches the window. If that is so, (M) in the window is a statement for boxes with all sides above the correlation length only, and no proof can pass through finite strips of fixed width.

## Step 8 result: marks, what is not covered, RESULT. DONE.

**Marks.**
| Item | Mark |
|---|---|
| Gauge-invariant coordinates (rho, v); GH2_2 = decorated O(4) ferromagnet plus beta_L times a six-spin term (step 1) | argued |
| Lemma KIN-G; the walk form of the gauge field; Proposition DIL per cut (step 2) | argued |
| Lemma FACE-FLUX (step 2) | argued |
| Decomposition of the flux excess into string, self and contact terms (step 2) | argued (physics reasoning) |
| Form A; Lemma LOOP; the diamagnetic bound Z_GH2 <= Z_YM Z_Phi(1)^2; the three hand values of W, one negative (step 3) | argued |
| Example Q8-INF: (M) false for frozen Q_8 at large b in infinite volume (step 4) | argued counterexample (leading order; for the test group, not for SU(2)) |
| Order and disorder reading; the two scale regions for SU(2) (step 4) | argued (physics reasoning; guide grade) |
| (M) needs sharp rates at both ends; (END-0) (step 5) | argued; (END-0) open; small-b sign by hand is guide |
| Example INT-2 (step 5) | argued counterexample (to the interpolation step in the class of Corollary KIN-D) |
| Two-site strip run (step 7) | guide |
| (W) for b in the window, beta_L in (0, infinity) | open |
| (M) for SU(2) in infinite volume | open; not refuted |
| (M) on a small strip for SU(2) at b >= 4 | false at guide grade (step 7) |
| Named step (INT-CMP) | open; failed in three written ways |

**What this file does not cover.**
- No proof of either form. No counterexample to (M) for SU(2) in infinite volume.
- Tori. Lemma KIN-G uses free ends; on a torus one holonomy per column stays (Remark TOR of row 1076).
- The Wilson form apart from the heat-kernel form, where they differ (Corollary KIN-D is a heat-kernel statement).
- The text of OpenAI's Theorem 3.1 and estimate (3.61): used only as rows 1009, 1076 and 1084 report them.
- The low-temperature expansion behind Q8-INF is not written out. The high-temperature orders behind the (END-0) guide are leading orders only.
- Recalled and not read: 't Hooft's two-dimensional model; Brydges, Frohlich and Seiler; Symanzik; van Enter and Shlosman. The papers of row 1112 were read by gpt-6-luna, not by me.
- The guide run: K-neutral sector and two sites only.
- A stability argument at small beta_L from Lemma DEC was considered and not written: covariance decay between two sets, as in (DEC4), does not give the tree decay of joint cumulants that a polymer expansion in beta_L needs. Open.
- One session, one author (Claude Fable 5.2, effort medium, laptop subagent). Checked by no one. Every "argued" lemma here needs a line-by-line check before any use.

**Credits.** Lemma KIN, KIN-1 to KIN-7, KIN-D, KIN-CVX, Lemma CB-L, Lemma GH2-0, Proposition CB-CH: row 1076. Proposition DIL and the kill-test code: row 1081. Lemma DEC, Lemma GH-NA, (GH5), (GH6): row 1084. The statement and the order of work: row 1108. Literature reading: row 1112. Diamagnetic bounds and walk expansions: Brydges, Frohlich, Seiler; Symanzik. Exact two-dimensional lattice gauge theory by characters: Migdal. Linear potential and self-energy in two dimensions: 't Hooft. Screening by fundamental matter: Fradkin and Shenker. The exponential-decay theorem for O(n): OpenAI's posted preprint, with its debt to Balaban's programme credited in the lane. The lane builds on T. Balaban and on the account of Sussman and Alpoge; no step of theirs is used in this row.

RESULT: Row 1109 (Claude Fable 5.2 medium, laptop subagent; one session, checked by no one). STOP BY THE THIRD RULE: neither form of (GH2-DESC) is proved and the monotone form is not refuted for SU(2); the named step (INT-CMP), a box-uniform comparison of the first neutral level with the vacuum level of S* D S at interior beta_L, failed in three written ways, none by association: (1) Lemma KIN-G per unit length stops at the self term of the flux excess; (2) the exact gauge integration gives a signed loop weight (W = (3 lambda_1^A - 1)/2 < 0 for a doubly wound loop) and lifts the vacuum too, and Example Q8-INF (argued counterexample, test group) gives rate(0) = 2b - 2 log 2 < rate(infinity) = 2b for frozen Q_8; (3) the interpolation in w fails by Example INT-2 and needs (NO-1ST). ARGUED: Lemma KIN-G, the walk and loop forms, the diamagnetic bound Z_GH2 <= Z_YM Z_Phi(1)^2, Lemma FACE-FLUX, GH2_2 as the decorated O(4) ferromagnet plus a six-spin term; the monotone form needs sharp rates at both ends ((END-0) open), so the weak form is the form with theorem-grade ends; (M) is true only where the sheets are disordered at the gauge scale. GUIDE: on the two-site strip (K-neutral sector) the gap rises in the window (2.28 to about 3.0 at b = 2.4) and the monotone form fails for SU(2) from b near 3.1 (derivative) and b near 4 (end point). OPEN: (W), (M) in infinite volume, (INT-CMP), (END-0), (NO-1ST). No mass gap claimed. Output `library/gap-descent-first-case.md`.
