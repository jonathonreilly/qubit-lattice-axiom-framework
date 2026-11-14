# FINISH row 862, gap-pe-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Row 862. Author: Claude Fable 5.2 (max effort). Date: 2026-11-12.
Clone commit: 2b6acd1732dde4e18293f0fe0e2814edbca36da3 (/Users/jonreilly/ym4d-lead/clone, pulled --ff-only, already up to date).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Marks: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE, OPEN.

## Target

Lemma PE (restricted-ensemble expansion) of D/library/gap-s1-opus.md lines 530-600 (row 842, unchecked).
With that file's Theorem BAD and Theorem CH-D it would give Theorem S1 in the form (S1-loc) or (S1-T):
for each n >= 2 and beta >= beta_0(n), the Wilson SU(2) measure on the twisted thin torus
(Z/n)^2 x (Z/M)^2, centre twist in the thin plane, has a transfer-matrix gap in a base direction,
uniformly in M.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read the source: gap-s1-opus.md lines 530-600 (Lemma PE), then the statements it uses
   (Theorem BAD, Theorem CH-D, G2, G3, Lemma L, (S1-loc), (S1-T)). Record exact statements with line numbers.
2. Fix the reduction: what exactly PE must deliver for (S1-T). Choose the route for the thin geometry
   (2D polymer expansion in the base, or a base transfer-matrix argument). Record the fact tests the route must pass.
3. Local Peierls bound: conditional cost of a bad region given its boundary, explicit in n and beta.
4. Chart Jacobian (Faddeev-Popov) and the quadratic form on a good region: bounds explicit in n and beta.
5. Gaussian decoupling across blocks: the massive covariance (mass from the twist, SU(2) only) and its decay.
6. Sum over Z_2 labels and polymer activities; convergence criterion (Kotecky-Preiss) with explicit constants.
7. Assemble: state Lemma PE as proved or its strongest proved part; state (S1-T) with all hypotheses; run the fact tests
   (U(1) Coulomb must fail; Q_8 and 2T; Dobrushin caps; (AN1)).
8. Final status table and RESULT line.

## Log

### Step 1a. Reading of D/library/gap-s1-opus.md (all 670 lines; S1O below)

Short names: S1O = D/library/gap-s1-opus.md; CH = D/library/gap-twist-chart.md.

- READ S1O:125-166 (setup). Lambda = (Z/n)^2 x (Z/M)^2; site y = (x, b), x fibre, b base. Per base point: n^2 sites,
  4 n^2 links, 6 n^2 plaquettes. A^tw = sum_p d_p, d_p = 1 - (1/2) tr U_p off P_0, 1 + (1/2) tr U_p on P_0;
  P_0 = the (1,2)-plaquettes at fibre point (n-1, n-1), one per base point. 0 <= d_p <= 2. mu^tw = Z^{-1} e^{-beta A^tw} dU.
  Twist eater V: U_1 = i sigma_1 on x_1 = n-1, U_2 = i sigma_2 on x_2 = n-1, else 1; A^tw(V) = 0.
  Symmetries: base translations, base reflections, base centre flips.
- READ S1O:178-197 (Lemma RP). mu^tw is reflection positive for base reflections through site planes, M even.
  So a transfer matrix in a base direction exists (as a positive form; the note does not write the operator).
- READ S1O:240-256 (Theorem BAD). n >= 2, M even >= 4, beta >= 1, 0 < delta <= 2, every set S of base points:
  mu^tw(every b in S is delta-bad) <= eps^{|S|}, eps = 6 n^2 beta^{6 n^2} e^{27 n^2} e^{-beta delta/4}.
  Remark 2 (S1O:277): it is a bound for the torus measure, NOT for conditional measures.
- READ S1O:305-317 (Theorem CH-D). D connected, all plaquettes of Sigma_D with d_p <= delta <= delta_0(n). Then
  U^h = eps V exp(X), X transverse (D_0^* X = 0), sup|X| <= C(n) sqrt(delta), [eps] in H^1(K_D; Z_2) a gauge-invariant
  datum; X unique (h unique up to sign) among charts with sup|X'| <= eps_1(n); (b') sum_p d_p >= (mu_n/16) sum_l |X_l|^2;
  (c'') locality at rate 1/(3n) in the path metric. C(n) = 6.1e4 n^9, delta_0(n) ~ n^{-32}.
- READ S1O:390-433 (TB, GR). |d_p - (1/8)|(D_1 X)_p|^2| <= C_5 |u_p|^3; Delta_1 = D_1^* D_1 + D_0 D_0^* >= mu_n
  = (2 sin(pi/2n))^2 >= 4/n^2; |Delta_1^{-1}(l,l')| <= (2/mu_n) exp(-a_n d_D), a_n >= 1/(7n).
- READ S1O:441-463 (Prop. U1). U(1): the fibre-constant parts of X_1, X_2 are massless on the base.
- READ S1O:503-511 (Prop. FLUX). Flux -1 around a hole of a good region forces a bad point in the hole.
- READ S1O:514-546 (W1, W2; ARGUED there). (S1-loc): |X|,|Y| <= K, |Cov| <= C(n,beta,K) exp(-(c/n) dist).
  (S1-T): the base transfer matrix has a gap >= c/n uniformly in M; equivalently |Cov(F,G)| <= 2 exp(-(c/n) d)
  for |F|,|G| <= 1 on the two sides of a pair of base planes at distance d.
- READ S1O:550-575 (Lemma PE, OPEN there). beta_PE(n), absolute c_PE, C(n,beta,K); for beta >= beta_PE(n), even M,
  gauge-invariant F over X, G over Y in [-1,1], |X|,|Y| <= K: |Cov(F,G)| <= C(n,beta,K) exp(-(c_PE/n) dist(X,Y)),
  and (S1-T) with the same rate. Needed (their list): (a) local conditional Peierls activity; (J) the Jacobian
  with the Faddeev-Popov ratio; (c) Gaussian decoupling across blocks, Z_2 labels of holes, convergence.

First remark of mine (ARGUED; to be settled in Step 2). (S1-T) as written, "|Cov(F,G)| <= 2 exp(-(c/n) d) for ALL
|F|,|G| <= 1 on two sides", is a statement about ALL functions, including non-gauge-invariant ones and including
functions of the base Z_2 flux through large loops. The Z_2 vortex gas has its own correlation length. A dilute gas
of vortices of density rho ~ e^{-c beta} gives a transfer-matrix gap of order one in the vortex sector only if
vortices are independent at distance; the gap for the Z_2-odd (centre-flip odd) sector is -log of the ratio of the
second to the first eigenvalue, which is governed by the string tension times the transverse size M: NOT uniform in M
in the flip-odd sector unless handled. This must be checked before any expansion is written.

### Step 1b. Reading of the check of row 842: D/library/gap-s1-check-astra.md (all 195 lines; CK below)

Check by Codex gpt-6-astra xhigh (row 856), a research check, not an audit.
- READ CK:15-45. RP, CB, Z, BAD (SU(2), n >= 2, even M >= 4), BAD-b, beta_BAD: HOLD.
  The "group-free" rider of BAD FAILS: Lemma Z needs a zero-action twist eater (twisted U(1) has none).
- READ CK:47-64. CH-D HOLDS AFTER CORRECTION: D finite and connected; in (c'') "every link l based at b_0 that
  belongs to both complexes". Constants unchanged. CH-T holds.
- READ CK:66-80. BAD-s and TB HOLD.
- READ CK:82-112. GR HOLDS AFTER CORRECTION (replacement proof by the product splitting; rate a_n = sqrt(mu_n/192)
  >= 1/(7n), prefactor 2/mu_n). Transverse covariance kernel bound:
  |Cov_G(l,l')| <= (4/beta) [2/mu_n + 64 e^{2a}/mu_n^2] exp(-a_n d_D(b(l), b(l'))).
- READ CK:114-118. FLUX HOLDS (R a filled rectangle).
- READ CK:120-138. U1 holds after a factor: the action Hessian at V is K_V/4, >= mu_n/4 on transverse fields.
- READ CK:140-166. W1 and W2 FAIL as arguments.
- READ CK:168-189. **The covariance form of (S1-T) is FALSE for this measure.** Counterexample (CK:174-187): the base
  Polyakov loop F_t = (1/2) tr prod_j U_4(x, t, j) on the slice b_3 = t. A centre flip of the direction-4 links gives
  mu(F_t) = 0. As beta -> infinity at fixed M, mu(F_0 F_d) -> 1 (concentration on the zero set, where the base Z_2 field
  is flat). So Cov(F_0, F_d) > 3/4 for large beta, against 2 exp(-(c/n) d). Also (CK:185): a torus expectation is a
  trace state, not a vacuum state; site-plane RP does not by itself give a positive one-step transfer operator.
  Also (CK:170): (S1-T) => (S1-loc) needs bounded diameters, not bounded cardinalities.

Consequence for this row (mine). The remark at the end of Step 1a is confirmed by CK's counterexample: Lemma PE as
printed (S1O:550-553) includes a false clause. The flux-odd sector (odd under a base centre flip) has a gap of order
(string tension) x M, tiny for M << exp(c beta). So Step 2 must first restate the target correctly:
the gap c/n can hold only (a) on the sector even under the base centre flips, or (b) for all sectors once the
transverse period M exceeds about n e^{c beta}... or (c) for local gauge-invariant observables (S1-loc), which are
flip-even automatically (S1O:160-163, Step 2 (iii) there).

### Step 1c. Reading of CH = D/library/gap-twist-chart.md (all 262 lines)

- READ CH:23-27. (X,Y) = -2 tr(XY) on su(2); e_c = i sigma_c/2; (1/2) tr exp(X) = cos(|X|/2); rho = geodesic distance
  of the 3-sphere of radius 2. Gamma_1 = i sigma_1, Gamma_2 = i sigma_2.
- READ CH:33-47. tau_l = Ad(V_l^{-1}) diagonal with signs; D_0 lambda (y,mu) = lambda(y+mu) - tau_l lambda(y);
  D_1 X; D_0^*; Delta_0 = D_0^* D_0. (1.1): U_p = z_p W E_p W^{-1}, d_p = 1 - cos(|Y_p|/2), Y_p = log E_p.
  (1.2): (V e^X)^{exp lambda} at l is V_l exp(tau_l lambda(y)) exp(X_l) exp(-lambda(y+mu)).
- READ CH:92-97 (Lemma L). |d omega|^2 + |d^* omega|^2 >= mu_n |omega|^2 on all cochains; Delta_0 >= mu_n.
- READ CH:103-111 (Lemma G). |g_c(y,y')| <= (2/mu_n) exp(-alpha_n |b - b'|_1); weighted sup norm of G_0 <= K_n = 25 n^6.
- READ CH:115-129 (G1-G4). G2: near-commuting with Gamma_1, Gamma_2 implies near the centre. G3: commutator near -1
  implies near (Gamma_1, Gamma_2) up to conjugation. G4: absolute constants C_3, C_4 (second derivatives of BCH).
- READ CH:131-150 (Lemma R), 152-166 (Lemma T: lambda = G_0 D_0^*(X^0 + N(lambda, X^0)) by contraction), 168-177 (Lemma Q).
- READ CH:181-193 (part (b)). READ CH:197-206 (constants): eps_1 = 1/(4200 C_3 n^7), eps_2 = min(eps_1, 1/(13 C_4 n)),
  C(n) = 6.1e4 n^9, delta_0 = (eps_2/C(n))^2, C_c(n) = 1.1e4 n^7 C(n).
- READ CH:258. Open there: derivative bounds for U -> X (the Jacobian).

Step 1 is complete. Statements I may use as inputs (all PROVED by others, checked once each, not audited):
RP, CB, Z, BAD, BAD-s (S1O, checked CK); CH-D with CK's corrections; TB; GR with CK's replacement proof; FLUX; U1.

## Resumed 2026-11-13 after the 03:06Z interrupt

Clone commit now: 9f1e04272b03270994c98fb4b9716e071924bac4 (pulled --ff-only, already up to date). The earlier run
read at 2b6acd1732dd; Step 2 first checks that S1O, CK and CH did not change between the two commits.
The reading (Steps 1a to 1c above) stands. I do not redo it. The proof had not started.

Remaining plan (one step per response, each appended before the next):

2. Restate the target precisely. CK:168-189 shows the covariance form of (S1-T) is false (base Polyakov loop).
   Decide which statement is true and provable: the sector, the observables, the state (vacuum, not trace state).
   Choose the route for the thin geometry. List the fact tests.
3. Local Peierls bound: conditional cost of a bad region given its boundary, explicit in n and beta.
4. Chart Jacobian (Faddeev-Popov) and the quadratic form on a good region, explicit in n and beta.
5. Gaussian decoupling across blocks: the massive covariance (mass from the twist, SU(2) only) and its decay.
6. Sum over Z_2 labels and polymer activities; convergence with explicit constants.
7. Assemble: Lemma PE as proved, or its strongest proved part; the corrected (S1-T) with all hypotheses; fact tests.
8. Final status table and the RESULT line.

### Step 2. The target restated, and the route (2026-11-13)

Source check. `git diff --stat 2b6acd1732dd 9f1e04272b03` on S1O, CK and CH is empty. The three sources are unchanged.

**2.1 The abelian skeleton shows what can be true (PROVED for the model; ARGUED for SU(2)).**
On the zero set of A^tw the base links are central (CK:178, from CH-T). So the long-distance part of mu^tw is a
two-dimensional Z_2 gauge theory on the base, with the massive SU(2) modes on top. Take the exact model: Z_2 gauge
theory on a base torus with N plaquettes, plaquette weight 1 for flux +1 and rho in (0,1) for flux -1. Put
r = (1 - rho)/(1 + rho). The fluxes are independent, conditioned on an even number of -1 (a closed surface). Then:

(Z2-a) Transfer matrix on a ring of M links, gauge-invariant states: the space is two-dimensional (the holonomy P = +-1),
    eigenvalues (1 + rho)^M on the flip-even state and (1 - rho)^M on the flip-odd state.
    So the flip-odd sector sits at -log(ratio) = M log(1/r), about 2 rho M. This is NOT bounded below uniformly in M
    at fixed rho: at M = 4 it is about 8 rho. (Hand computation: the strip between two rings has M plaquettes;
    the sum over even, resp. odd, numbers of -1 gives ((1 + rho)^M +- (1 - rho)^M)/2.)
(Z2-b) Torus covariance of two flux detectors F_b = 1{flux at b is -1}, b != b', N = M^2:
    P(F_b) = (rho/(1 + rho)) (1 - r^{N-1})/(1 + r^N),   P(F_b F_b') = (rho/(1 + rho))^2 (1 + r^{N-2})/(1 + r^N),
    Cov(F_b, F_b') = 4 rho^2 r^{N-2} / ((1 + rho)^4 (1 + r^N)^2) > 0, the same for every pair b != b'.
    (The numerator is (1 + r^{N-2})(1 + r^N) - (1 - r^{N-1})^2 = r^{N-2} (1 + r)^2, and 1 + r = 2/(1 + rho).)
    So local gauge-invariant observables on the torus are correlated at every distance, at strength about
    4 rho^2 exp(-2 rho M^2). The cause is the parity constraint (trace state, both sectors), not a small mass.
    A bound C exp(-(c/n) dist) uniform in M then needs C >= rho^2 exp(c^2/(8 n^2 rho)) up to constants
    (maximise (c/n) M - M^2 log(1/r) over M): doubly exponential in beta when rho = exp(-kappa beta).
For SU(2) these two facts are ARGUED, not proved: the parity constraint is real (the Z_2 class of CH-D is flat on the
good region of a closed base, so the number of holes with flux -1 is even), and CK:174-187 proves the flip-odd failure
by hand for the SU(2) measure in the limit beta -> infinity at fixed M. I do not prove a lower bound on the SU(2)
vortex activity here.

**2.2 Consequences for the statement.** Lemma PE as printed (S1O:550-553) has three defects:
(D1) "(S1-T): gap >= c/n on the complement of the top eigenvector, uniformly in M" is false on the flip-odd sector
     for M below about (c/n)/sigma(n, beta), sigma the Z_2 string tension (CK:174-187 proves the failure; (Z2-a) is the model).
(D2) A torus expectation is a trace state. Its covariances contain the flip-odd sector with weight (lambda_odd/lambda_0)^M.
     So "(S1-loc) on the torus with C(n, beta, K) independent of M" is at best true with a doubly exponential constant ((Z2-b)).
(D3) The transfer operator must be named. Site-plane reflection positivity alone does not give it (CK:185).

**2.3 The target of this row (statements; proofs in Steps 3 to 6).**
Time = base direction 3. Slice = (Z/n)^2 x (Z/M): the links in directions 1, 2, 4 at one value of b_3.
T = the Wilson transfer operator of the twisted action on H = L^2 of gauge-invariant slice functions (defined in Step 3;
it is a positive operator with a strictly positive kernel; the twist enters only the slice potential).
c_4 = the centre flip of the direction-4 links on one fibre x {j_0}; it commutes with T. H = H_+ (+) H_- (c_4 = +-1).
lambda_0 = ||T||, a simple eigenvalue, eigenvector Omega > 0 in H_+.

    (S1-T') [vacuum form, flip-even sector]. For each n >= 2 there is beta_0(n) such that for beta >= beta_0(n) and
    every even M in the stated range, the spectrum of T on H_+ minus C Omega lies in [0, lambda_0 exp(-m_n)],
    m_n >= c/n, c absolute. Equivalently, for the Gibbs state of the infinite cylinder (Z/n)^2 x Z x (Z/M) and all
    flip-even gauge-invariant slice functions F, G:  |<F(0) G(d)> - <F><G>| <= ||F||_2 ||G||_2 exp(-m_n d).
    (S1-T'-odd) [no uniform claim]. ||T restricted to H_-|| = lambda_0 exp(-sigma_M); (Z2-a) is the model.
    (S1-tor) [torus form with its honest error term]. For gauge-invariant local F over X, G over Y on the base torus
    (Z/M)^2:  |Cov(F, G)| <= C_1 exp(-m_n dist(X, Y)) + C_2 (probability that the torus has a bad point).

"Stated range" is the point. I aim to prove (S1-T') and (S1-tor) for all even M with M eps_1^{1/2} <= eta_0/n,
eps_1 the bad-point bound of Theorem BAD at a threshold delta_1: that is M up to about exp(beta delta_1/8).
For larger M the same statements need a gas of defects at positive density; I state exactly what is missing (Step 7).
I do not claim uniformity in all M.

**2.4 Route (chosen for the thin geometry).** No multiscale expansion and no Faddeev-Popov determinant.
(R1) Fibre-wise gauge ("unitary gauge"). Read the model as a two-dimensional gauge-Higgs model on the base:
     the fibre configuration at a base point b is the Higgs field, the base links (n^2 group elements per base edge)
     are the gauge field, the fibre gauge group SU(2)^{n^2} acts at each base point. The twist breaks it to Z_2
     (the stabiliser of V on a fibre is +-1; this is where G2 enters). Fix the gauge fibre by fibre: CH-D with
     D = {one base point} gives U^h = V exp(xi_b) on the fibre over b, xi_b fibre-transverse, unique up to h -> -h.
     The gauge condition at b involves only the fibre over b. So the Jacobian is a product over base points of
     local factors J(xi_b). Item (J) of S1O:563-565 becomes a one-fibre computation. Base links become free variables
     u_e = eps_e exp(Y_e), eps_e = +-1, with residual gauge group Z_2 per base point.
(R2) Mass without interpolation. To second order the action is
     8 A_2 = sum_b <xi_b, Delta_1^F xi_b> + sum_e |xi_b' - xi_b|^2 + sum_e <Y_e, Delta_0^F Y_e> + sum_P |d_K Y|^2
     (the cross terms vanish: D_0^{F*} xi = 0), and Delta^F >= mu_n in degrees 0 and 1 (Lemma L on the fibre; SU(2) only).
     So on a product of small balls the exact action is uniformly convex in (xi, Y): Hessian >= beta mu_n/4 (1 - eta).
(R3) Convex sea. For a uniformly convex potential with nearest-neighbour coupling in time, the Helffer-Sjostrand
     representation with an exponential weight in time gives decay at a rate a_n of order sqrt(mu_n), about c/n,
     with constants that do not depend on the dimension, hence not on M. This replaces "Gaussian decoupling across blocks".
(R4) Defects by an operator Peierls bound. Split the kernel of T: T = T^g + T^b, T^g supported on slabs whose chart
     coordinates lie in the product of balls. Reflection positivity (Theorem BAD, traces of powers) gives
     ||T^b|| <= 2 M eps_1^{1/2} lambda_0. T^g is block diagonal in the Z_2 label P_4 = +-1 (a good slab is an annulus;
     its class is flat), and c_4 swaps the two blocks. On H_+ the problem is one block of T^g plus a small operator.
     This is the "sum over Z_2 labels". Weyl's inequality gives (S1-T') when M eps_1^{1/2} << 1/n.
(R5) The torus form (S1-tor) follows from (R1)-(R3) with weights in both base directions.

**2.5 Fact tests the route must pass (run in Step 7).**
(F1) U(1) in its Coulomb phase: no gap. The route must break: it does at (R2) (Delta^F has zero modes for trivial Ad).
(F2) Q_8 and 2T (rows 838, 843): to be read in Step 7 against (R2)-(R3) (these use the Lie algebra, not a finite group).
(F3) Worst-case Dobrushin caps 2/3 and 0.775, layer bound 4 G_3 = 1.0109 (row 839), (AN1) (row 845): the route uses no
     worst-case boundary condition; (R4) is a global reflection-positivity bound and (R3) is for the restricted ensemble.

**Revised plan for the remaining steps.**
3. Transfer operator, sectors, and the operator Peierls bound ||T^b|| <= 2 M eps_1^{1/2} lambda_0 (needs BAD on a
   rectangular base torus; check S1O's proof).
4. Fibre-wise chart on good slabs: coordinates (xi, Y, eps), inclusion of thresholds, the local Jacobian.
5. Convexity with explicit constants; weighted Helffer-Sjostrand bound; gap of one block of T^g, uniform in M.
6. Assembly: (S1-T') and (S1-tor) in the stated range.
7. Fact tests; the exact missing statement for all M.
8. Status table and the RESULT line.

### Step 3. The transfer operator, its sectors, and the operator Peierls bound

Notation. Time = base direction 3, with N time steps (N even, N >= 4). Ring = base direction 4, M sites (M even, M >= 4).
Slice sites y = (x, j), x in (Z/n)^2, j in Z/M. Slice links L_s = {(y, mu): mu = 1, 2, 4}: 3 n^2 M links.
Omega_s = SU(2)^{L_s} with product Haar measure d omega. A gauge transformation g = (g(y)) acts by
omega^g(y, mu) = g(y) omega(y, mu) g(y + mu)^{-1}. P = the average over g: the projection of L^2(Omega_s) onto H, the invariant functions.
V(omega) = the sum of d_p over the plaquettes of the slice (planes (1,2), (1,4), (2,4); the twist stack P_0 is in the plane (1,2)).
k(u) = exp(-beta (1 - (1/2) tr u)). For a slab configuration s = (omega, h, omega'), h = (h(y)) the temporal links,
    w(s) = e^{-beta V(omega)/2} prod_{l = (y, mu)} k( omega(l) h(y + mu) omega'(l)^{-1} h(y)^{-1} ) e^{-beta V(omega')/2},
    K(omega, omega') = int dh w(omega, h, omega'),    (T psi)(omega) = int K(omega, omega') psi(omega') d omega'.

**Lemma T1 (PROVED; standard, rebuilt).** (i) exp(-beta A^tw) on the base torus (Z/N) x (Z/M) equals
prod_t w(omega_t, h_t, omega_{t+1}), so Z_N = Tr T^N, and for functions F_i of single slices
mu^tw(prod F_i(omega_{t_i})) = Tr(T^{t_1} F_1 T^{t_2 - t_1} F_2 ...)/Tr T^N.
(ii) K is continuous, symmetric and strictly positive. T is Hilbert-Schmidt and self-adjoint, T = P T = T P.
(iii) T >= 0 as an operator.
(iv) lambda_0 := ||T|| is a simple eigenvalue with a strictly positive continuous eigenfunction Omega in H; every
unitary S that comes from a measure-preserving map of Omega_s with K(S omega, S omega') = K(omega, omega') fixes Omega.
*Proof.* (i) The time-like plaquette on the slice link l = (y, mu) between times t and t+1 is
omega_t(l) h_t(y + mu) omega_{t+1}(l)^{-1} h_t(y)^{-1}, with defect 1 - (1/2) tr. The slice plaquettes of slice t
give V(omega_t), split in two halves. (ii) Continuity and positivity are clear. The substitution h -> h^{-1} and
tr u = tr u^{-1} give symmetry. The trace of omega(l) h(y+mu) omega'(l)^{-1} h(y)^{-1} equals that of
omega^{g}(l) omega'(l)^{-1} with g = h^{-1}, so K(omega, omega') = e^{-beta V/2} [int dg prod_l k(omega^g(l) omega'(l)^{-1})] e^{-beta V'/2}:
T = e^{-beta V/2} C P e^{-beta V/2}, C = the product over links of convolution by k. V is gauge invariant and C commutes
with P, so T = PT = TP. (iii) tr u is the character of the fundamental representation, a positive-definite function on
the group. Products and positive combinations of positive-definite functions are positive definite (Schur product),
so exp((beta/2) tr u) is. Hence C >= 0, PCP >= 0, T >= 0. (iv) If T psi = lambda_0 psi, psi real, then
<|psi|, T |psi|> >= <psi, T psi>, so |psi| is a top eigenvector, |psi| = T|psi|/lambda_0 > 0 everywhere. Then
|psi| - psi and |psi| + psi are non-negative top eigenvectors, each zero or strictly positive: psi = +-|psi|.
Two strictly positive functions are not orthogonal: simple. S Omega is a positive top eigenvector: S Omega = Omega. QED.

**Vacuum state.** By (iv), for slice functions F, G: lim_{N -> infinity} mu^tw_N(F(omega_0) G(omega_d))
= <F Omega, (T/lambda_0)^d G Omega> with ||Omega|| = 1. This is the state of the infinite cylinder. (PROVED.)

**Lemma T2, sectors (PROVED).** c_4 multiplies omega(x, j_0; 4) by -1 for all x (one fixed j_0), nothing else.
It preserves V (a slice plaquette contains 0 or 2 of these links), commutes with gauge transformations, and
prod_l k(omega^g(l) omega'(l)^{-1}) is unchanged when c_4 acts on both arguments. So c_4 commutes with T and P,
H = H_+ (+) H_-, T maps each to itself, and Omega is in H_+ by T1 (iv).

**Splitting.** Call a slab configuration s = (omega, h, omega') delta-good if every time-like plaquette of the slab
and every slice plaquette of omega and of omega' has d_p <= delta. Let chi be a measurable function of s with values
in {0, 1} such that: (c1) chi is invariant under slab gauge transformations (omega^g, g h g'^{-1}, omega'^{g'});
(c2) chi(omega', h^{-1}, omega) = chi(omega, h, omega'); (c3) chi = 1 on delta_1-good slabs. (Step 4 chooses chi.)
    K^g := int dh chi w,   K^b := int dh (1 - chi) w >= 0,   T = T^g + T^b.
By (c1), (c2), K^g and K^b are symmetric and invariant under gauge transformations of each argument:
T^g, T^b are self-adjoint, Hilbert-Schmidt, and T^# = P T^# P. They commute with c_4 if chi is c_4-invariant (c4).

**Lemma T3, the operator Peierls bound (PROVED, given Theorem BAD on rectangular tori).**
Let eps_1 := eps(n, beta, delta_1) of Theorem BAD, beta >= 1, M even >= 4. Then ||T^b|| <= (2 M eps_1)^{1/2} lambda_0.
*Proof.* T^b is self-adjoint, so for even N: ||T^b||^N <= Tr (T^b)^N = int prod_t d omega_t prod_t K^b(omega_t, omega_{t+1})
= Z_N mu^tw_N( chi = 0 on every slab t in Z/N ) <= Z_N mu^tw_N( no slab is delta_1-good ), by (c3).
If slab t is not delta_1-good, some plaquette of slice t, of slice t+1, or between them has d_p > delta_1. Its base
point is (t, j) or (t+1, j) for some j (S1O:128: the base point is that of the first site). So there is a
delta_1-bad base point in {t, t+1} x (Z/M). Use only the even t: the N/2 sets {t, t+1} x (Z/M), t even, are disjoint.
Choose one bad point in each: at most (2M)^{N/2} choices of a set S with |S| = N/2, each of probability at most
eps_1^{N/2} (Theorem BAD). So ||T^b||^N <= Z_N (2 M eps_1)^{N/2}. Also Z_N = Tr T^N = sum lambda_i^N
<= lambda_0^{N-2} ||T||_HS^2 (T >= 0). Hence ||T^b|| <= (||T||_HS/lambda_0)^{2/N} lambda_0 (2 M eps_1)^{1/2}. Let N -> infinity. QED.

**Theorem BAD on the rectangular base (Z/N) x (Z/M), N and M even >= 4 (PROVED: S1O's proof, re-read for this case).**
S1O:240-256 states BAD for (Z/M)^2. I re-read 3.1 to 3.4 (S1O:178-256) with sides N, M. RP: the reflection in
direction 3 has site planes j and j + N/2. CB: cells t in (Z/N) x (Z/M); g_t is unique when each side is >= 4; the
run-length argument is per direction with half-length N/2, resp. M/2; the exponent is 1/(N M) (the number of cells).
Z: Z >= exp(-n^2 N M (6 log beta + 27)) (4 n^2 N M links). BAD: at least N M/4 distinct plaquettes are bad on the
constant event. The bound eps = 6 n^2 beta^{6 n^2} e^{27 n^2} e^{-beta delta/4} is unchanged.

Remarks. (1) T3 is the Peierls input of this row. It is global (traces of powers), not conditional. It replaces
"the local conditional activity" of S1O:556-560 in the range M eps_1 << 1/n^2, and only there.
(2) T3 costs a factor M: a slab of the whole ring is clean only if no defect sits anywhere on the ring. For
M eps_1 >= 1 the bound is void. This is the single place where the range of M enters (see Step 7).

### Step 4. The fibre-wise chart: coordinates (xi, Y, eps), thresholds, and the local Jacobian

Conventions are those of CH:20-47 (READ again for this step): |.| on su(2) from (X, Y) = -2 tr(XY); rho the distance of
the 3-sphere of radius 2; tau_l = Ad(V_l^{-1}); D_0, D_1, D_0^*; theta_delta = pi sqrt(2 delta) (G1, CH:114);
mu_n = (2 sin(pi/2n))^2 in [4/n^2, 2]; C_3, C_4 >= 1 absolute (G4); eps_1(n) = 1/(4200 C_3 n^7); C(n) = 6.1e4 n^9;
delta_0(n) = (eps_2/C(n))^2, so C(n) sqrt(delta) <= eps_2 <= eps_1 for delta <= delta_0 (CH:197-206).

Objects. D a finite set of base points, K_D and Sigma_D = F x K_D as in S1O:295-304. F = the fibre torus.
D_0^F, D_1^F, Delta_0^F = D_0^{F*} D_0^F: the operators of one fibre. T_F := ker D_0^{F*}, the fibre-transverse fields:
a subspace of su(2)^{2 n^2} of dimension 3 n^2 (D_0^F is injective since Delta_0^F >= mu_n, Lemma L on F, S1O:321-330).
For r > 0: K_r(D) := { (xi, Y): xi_b in T_F and sup_l |xi_b(l)| <= r for b in D; Y_e in su(2)^{n^2}, sup_x |Y_e(x)| <= r
for each edge e of K_D }. It is a product of convex sets, one per base point and one per base edge.
For (xi, Y) in K_r(D) and a Z_2 1-cochain eps on K_D, U^{xi,Y,eps} is the configuration on Sigma_D with fibre links
V_l exp(xi_b(l)) and base links eps_e exp(Y_e(x)) (e = (b, b + e_a), the link (x, b; a)).
G_r(D) := the set of configurations gauge equivalent to some U^{xi,Y,eps} with (xi, Y) in K_r(D) and eps flat.
R(n) := 1.5e5 n^10 (it is at least 2.41 n C(n)).

**Lemma F1, the site chart (READ: CH-D with D = {b}, S1O:305-317, held by CK:47-64).** If every fibre plaquette over b
has d_p <= delta <= delta_0(n), there is a fibre gauge h_b with (U^{h_b}) = V exp(xi_b) on the fibre over b, xi_b in T_F,
sup |xi_b| <= C(n) sqrt(delta). Among such charts with sup |xi'| <= eps_1(n): h' = +-h_b and xi' = xi_b.
(A single point is a connected D; K_D has no edge, so there is no sign field.)

**Lemma F2, the edge chart (PROVED).** Let delta <= delta_0(n), e = (b, b') a base edge, both fibres in the chart of F1,
and every mixed plaquette over e with d_p <= delta. Put u_e(x) := h_b(x) U_a(x, b) h_b'(x)^{-1}. Then there are a sign eps_e,
the same for all x, and Y_e(x) with u_e(x) = eps_e exp(Y_e(x)), |Y_e(x)| <= 1.2 n eta, eta := theta_delta + 2 C(n) sqrt(delta).
Hence sup |Y_e| <= R(n) sqrt(delta).
*Proof.* In the gauge h the mixed plaquette on the fibre link (x, mu) is
V_mu(x) e^{xi_b(x,mu)} u_e(x + mu) e^{-xi_b'(x,mu)} V_mu(x)^{-1} u_e(x)^{-1}, at distance <= theta_delta from 1 (G1). By (R1), (R2):
rho( u_e(x + mu), V_mu(x)^{-1} u_e(x) V_mu(x) ) <= theta_delta + |xi_b(x,mu)| + |xi_b'(x,mu)| <= eta.
Go once around the fibre circle of direction i from x. Conjugation is an isometry, so after n steps
rho( u_e(x), Gamma_i^{-1} u_e(x) Gamma_i ) <= n eta, for i = 1, 2 (the product of the V_i around the circle is Gamma_i).
Here n eta <= n (2 + pi sqrt 2 / C(n)) eps_1(n) < 2. G2 (CH:116) gives u_e(x) = s(x) exp(Y_e(x)), s(x) = +-1,
|Y_e(x)| <= 1.2 n eta. If s(x + mu) = -s(x), the first display and (R3) give 2 pi - 2.4 n eta <= eta: false. So s is constant.
Last, 1.2 n (2 + pi sqrt 2/C(n)) C(n) <= 2.41 n C(n) <= R(n). QED.

**Lemma F3, the Z_2 class (PROVED).** Let every plaquette of Sigma_D have d_p <= delta <= delta_0(n). Then
(i) U is gauge equivalent to U^{xi,Y,eps} with (xi, Y) in K_{r(delta)}(D), r(delta) := R(n) sqrt(delta), and eps flat on K_D.
So {delta-good on Sigma_D} is contained in G_{r(delta)}(D).
(ii) Changing h_b to s_b h_b (s_b = +-1) changes eps to eps . delta s and leaves (xi, Y) unchanged.
(iii) Every U in G_r(D) has d_p <= 2 r^2 on every plaquette of Sigma_D.
*Proof.* (i) F1 at each b, F2 at each edge. Flatness: over a face P of K_D the base plaquette at x is
eps_P e^{Y_1} e^{Y_2} e^{-Y_3} e^{-Y_4} up to conjugation, eps_P the product of eps around P. The exponentials are within
4 x 1.2 n eta < 1 of 1. If eps_P = -1 the plaquette is at distance > 2 pi - 1 > theta_delta from 1: not delta-good.
(ii) By the formula for u_e. (iii) Each link of U^{xi,Y,eps} is within r of V_l times a sign; signs cancel in every
plaquette (flatness on base faces; a mixed plaquette holds eps_e twice). By (R1), (R2), rho(U_p, z_p) <= 4r and
d_p = 1 - cos(rho/2) <= rho^2/8 <= 2 r^2. QED.

**Lemma F4, uniqueness (PROVED, from F1).** Let r <= r_inj(n) := sqrt(delta_0(n)/2) (this is below eps_1(n) and below 1).
If (xi, Y), (xi', Y') in K_r(D), eps, eps' are cochains, and U^{xi',Y',eps'} = (U^{xi,Y,eps})^g for a gauge transformation g,
then xi' = xi, Y' = Y, g(x, b) = s_b = +-1 for all x, and eps' = eps . delta s.
*Proof.* The fibre over b: V e^{xi_b} has fibre plaquettes with d_p <= 2 r^2 <= delta_0 (F3 (iii) on one fibre). The charts
(1, xi_b) and (g_b, xi'_b) both have sup <= r <= eps_1. By F1, g_b = +-1 and xi'_b = xi_b. On a base link:
s_b s_b' eps_e e^{Y_e(x)} = eps'_e e^{Y'_e(x)} with |Y|, |Y'| <= r < pi/2, so e^{Y} e^{-Y'} = +-1 at distance < pi from 1: it is 1,
Y' = Y (exp is injective on |Y| < 2 pi), and eps'_e = s_b s_b' eps_e. QED.

**Lemma F5, the measure in the chart; the Jacobian is local (PROVED).** Let r <= min(r_inj(n), sqrt(mu_n)/(4 sqrt 2)).
For (lambda, zeta) in su(2)^{n^2} (+) T_F put (M_xi (lambda, zeta))(l) := -lambda(y + mu) + Ad(e^{-xi(l)}) tau_l lambda(y) + Phi(xi(l)) zeta(l),
l = (y, mu) a fibre link, Phi(X) := int_0^1 e^{-s ad X} ds. Put J(xi) := |det M_xi| (a 6 n^2 x 6 n^2 determinant in
orthonormal bases) and varrho(Y) := (16 pi^2)^{-1} (sin(|Y|/2)/(|Y|/2))^2. Then for every bounded measurable gauge-invariant f
supported in G_r(D), with c_F > 0 depending only on n and c(D) the number of connected components of K_D,
    int f(U) prod_{l in Sigma_D} dU_l = c_F^{|D|} 2^{-c(D)} sum_{[eps] in H^1(K_D; Z_2)} int_{K_r(D)} f(U^{xi,Y,eps})
                                         prod_{b in D} J(xi_b) d xi_b  prod_{e, x} varrho(Y_e(x)) dY_e(x).
Moreover, on sup |xi| <= r:
(J1) ||M_xi - M_0|| <= 2 sup|xi|, ||M_0^{-1}|| <= sqrt 2 mu_n^{-1/2}, so M_xi is invertible, ||M_xi^{-1}|| <= 2 sqrt 2 mu_n^{-1/2}, J > 0;
(J2) |D^2 (log J)(xi)(zeta, zeta)| <= C_J(n) ||zeta||_2^2, C_J(n) := 240 n^2/mu_n <= 60 n^4;
(J3) -log varrho is convex on |Y| < 2 pi.
*Proof.* Theta(g, xi, Y, eps) := (U^{xi,Y,eps})^g maps (gauge group over D) x K_r(D) x {flat eps} onto G_r(D). By F4, two
points have the same image iff they are (g, xi, Y, eps) and (g s, xi, Y, eps . delta s) (s central, so (U)^{gs} = (U^s)^g):
every point of the image has exactly 2^{|D|} preimages. Differential. By CH:(1.2) the variation of V_l e^{xi(l)} under
g = exp(lambda) and xi -> xi + zeta is U_l^{-1} delta U_l = Ad(e^{-xi(l)}) tau_l lambda(y) - lambda(y + mu) + Phi(xi(l)) zeta(l)
(e^{-X} d(e^X)(zeta) = Phi(X) zeta). This is M_xi. Haar measure is left invariant, so the density of the fibre part in
the coordinates (g, xi) is c_F |det M_xi|, the same at every g. On a base link, Y -> g(x,b) eps_e e^{Y} g(x,b')^{-1} has the
density of Haar measure in exponential coordinates: with psi = |Y|/2, normalised Haar is (2/pi) sin^2 psi d psi on the
radius (S1O:235) and Lebesgue measure is 32 pi psi^2 d psi, so varrho = sin^2 psi/(16 pi^2 psi^2). The area formula for the
2^{|D|}-to-1 map Theta gives the display with 2^{-|D|} and a sum over flat eps; f depends on eps through [eps] (F3 (ii)),
and a class has 2^{|D| - c(D)} members.
(J1) On su(2), ||ad X|| = |X| and ad X is skew, so e^{-ad X} is orthogonal; Duhamel gives ||d/ds e^{-ad(X + sZ)}|| <= |Z| and
||d^2/ds^2|| <= |Z|^2; so ||d Phi|| <= |Z|/2, ||d^2 Phi|| <= |Z|^2/3. Each fibre site starts 2 fibre links. Hence
||d_zeta M_xi (lambda, zeta')||^2 <= sup|zeta|^2 sum_l (|lambda(y_l)| + |zeta'(l)|/2)^2 <= 4 sup|zeta|^2 (||lambda||^2 + ||zeta'||^2):
||d_zeta M|| <= 2 sup|zeta|, and likewise ||d^2_{zeta zeta} M|| <= 2 sup|zeta|^2. M_0 = (-D_0^F) (+) 1 on su(2)^{n^2} (+) T_F with
range(D_0^F) orthogonal to T_F, so ||M_0^{-1}|| = max(1, mu_n^{-1/2}) <= sqrt 2 mu_n^{-1/2} (mu_n <= 2). With 2r sqrt 2 mu_n^{-1/2} <= 1/2
a Neumann series gives the rest.
(J2) D^2 log|det M|(zeta, zeta) = tr(M^{-1} d^2 M) - tr((M^{-1} dM)^2), and |tr B| <= 6 n^2 ||B||. So the left side is at most
6 n^2 [2 sqrt 2 mu_n^{-1/2} . 2 + (2 sqrt 2 mu_n^{-1/2} . 2)^2] ||zeta||^2 <= 6 n^2 [8/mu_n + 32/mu_n] ||zeta||^2 (mu_n^{-1/2} <= sqrt 2/mu_n).
(J3) -log varrho = phi(|Y|) + const, phi(s) = -2 log(sin(s/2)/(s/2)); phi' = 2/s - cot(s/2) >= 0 and
phi'' = (1/2) csc^2(s/2) - 2/s^2 >= 0 on (0, 2 pi) (tan u >= u on (0, pi/2), cot <= 0 beyond; sin u <= u). A convex
non-decreasing function of the norm is convex. QED.

**The action in the chart does not see eps (PROVED).** For flat eps, A^tw(U^{xi,Y,eps}) = A^tw(U^{xi,Y,1}) =: A(xi, Y):
the signs cancel in every plaquette (proof of F3 (iii)). So in each Z_2 class the good part of mu^tw is the same measure
    exp(-Phi(xi, Y)) d xi dY on K_r(D),   Phi := beta A(xi, Y) - sum_b log J(xi_b) - sum_{e,x} log varrho(Y_e(x)).

**Lemma F6, the block form of T^g (PROVED).** Fix delta_1 with r_1 := R(n) sqrt(delta_1) <= min(r_inj(n), sqrt(mu_n)/(4 sqrt 2)),
and let chi := the indicator of G_{r_1}(D) for the slab D = {t, t+1} x (Z/M). Then:
(i) chi satisfies (c1)-(c4) of Step 3 ((c3) by F3 (i); (c2) and (c4) because K_{r_1} is symmetric under Y -> -Y on the
    temporal edges and under the relabelling of the two slices, and c_4 on both slices maps flat eps to flat eps).
(ii) K_D is an annulus: c(D) = 1 and H^1(K_D; Z_2) = Z_2, the class being the ring holonomy P_4 = prod_j eps_{(t,j),4},
    which is the same on both slices. Let S^+-_r be the slice configurations gauge equivalent to
    (V e^{xi_j}, eps_j e^{Y_j})_j with (xi, Y) in B_r := K_r(ring) and prod eps_j = +-1. K^g(omega, omega') = 0 unless omega, omega'
    lie in the same S^+-_{r_1}. So T^g = T^g_+ (+) T^g_- (+) 0 on H = L^2(S^+)^inv (+) L^2(S^-)^inv (+) (the rest), and c_4 swaps the two blocks.
(iii) With zeta = (xi_j, Y_j)_j in B_{r_1} and the unitary psi -> psi(U^{zeta,+}) (c_F^M J varrho(zeta)/2)^{1/2} from L^2(S^+)^inv to
    L^2(B_{r_1}, d zeta), T^g_+ becomes the integral operator with kernel
        k^+(zeta, zeta') = c_F^M int_{sup|Y_3| <= r_1} dY_3 exp(-Phi_s(zeta, Y_3, zeta')),
        Phi_s := beta A_slab(zeta, Y_3, zeta') - (1/2) log(J varrho)(zeta) - (1/2) log(J varrho)(zeta') - log varrho(Y_3),
    A_slab = V(zeta)/2 + V(zeta')/2 + the time-like defects; (J varrho)(zeta) = prod_j J(xi_j) prod_{j,x} varrho(Y_j(x)).
*Proof.* (ii) Flatness of eps on the faces between the slices. (iii) F5 for the ring (c = 1, class +) gives
int_{S^+} |psi|^2 = (c_F^M/2) int_B |psi~|^2 J varrho; F5 for the slab gives <psi_1, T^g psi_2> on the class +
= (c_F^{2M}/2) int psi~_1(zeta) psi~_2(zeta') e^{-beta A_slab} (J varrho)(zeta) varrho(Y_3) (J varrho)(zeta'). Insert the unitary. QED.

Remark (what Step 4 buys). The Faddeev-Popov item (J) of S1O:563-565 is closed in this gauge: J is one fibre's determinant,
with (J1)-(J2). No decay estimate for a ghost operator is needed. The price is F4's radius r_inj = sqrt(delta_0/2),
which pushes delta_1 down to delta_0(n)/(2 R(n)^2), of order n^{-52}.

### Step 5. Convexity in the chart, the weighted Helffer-Sjostrand bound, and the gap of one block of T^g

Setting. A stack is K = I x (Z/M), I an interval of times, with its sites, time edges, ring edges and faces; Sigma = F x K.
A field is Z = (zeta_b in T_F for sites b; W_e in su(2)^{n^2} for edges e), a 1-cochain on Sigma (fibre-transverse on fibres).
||Z||^2 = sum_b |zeta_b|^2 + sum_e |W_e|^2. Plaquette weights w_p in {1/2, 1}: 1/2 on the slice plaquettes of the two end
slices of I, 1 elsewhere (this is what a sum of slab actions A_slab gives).
For a plaquette p = (y; mu < nu) and X = (xi, Y): a_p(X) := (tau_nu X_mu(y), X_nu(y+mu), X_mu(y+nu), tau_mu X_nu(y)) in su(2)^4,
L(a) := a_1 + a_2 - a_3 - a_4, G(a) := 1 - (1/2) tr(e^{a_1} e^{a_2} e^{-a_3} e^{-a_4}). By CH:(1.1), d_p(V e^X) = G(a_p(X)) for
every X, and L(a_p(X)) = (D_1 X)_p. |a|_2^2 := sum_i |a_i|^2.

**Lemma H1 (PROVED).** G is real-analytic on su(2)^4, D^2 G(0)(b, b) = |L b|^2/4, and |D^3 G(x)(a, b, b)| <= |a|_2 |b|_2^2
for all x, a, b. Hence |D^2 G(x)(b, b) - |L b|^2/4| <= |x|_2 |b|_2^2.
*Proof.* G(a) = 1 - cos(|log E|/2) with log E = L a + O(|a|^2): the Hessian at 0. For skew-Hermitian A, B_1, ..., B_m the mixed
derivative of exp(A + sum s_i B_i) is a sum of m! Duhamel integrals over a simplex of volume 1/m! of products of unitaries and
the B_i: its norm is at most prod ||B_i||. By the Leibniz rule the third mixed derivative of the product of the four
exponentials in directions (a, b, b) has norm at most (sum ||a_i||)(sum ||b_i||)^2. In the 2 x 2 representation ||c|| = |c|/2
for c in su(2), and |tr| <= 2 ||.||. So |D^3 G(a, b, b)| <= (1/2) 2 (sum |a_i|/2)(sum |b_i|/2)^2 <= |a|_2 |b|_2^2 (sum of four
numbers <= 2 x their l^2 norm). Integrate D^3 G along the segment from 0 to x. QED.

**Lemma H2, the mass is local (PROVED; uses Lemma L on the fibre, READ S1O:321-330, CH:92-97).** For every stack and every field Z,
    sum_p w_p |(D_1 Z)_p|^2 >= (mu_n/2) ||Z||^2.
*Proof.* Fibre plaquettes over b: |D_1^F zeta_b|^2 = <zeta_b, Delta_1^F zeta_b> - |D_0^{F*} zeta_b|^2 >= mu_n |zeta_b|^2 (zeta_b is
transverse). Mixed plaquettes over an edge e = (b, b'): (D_1 Z)(x, b; mu, a) = (zeta_b - zeta_b')(x, mu) + (D_0^F W_e)(x, mu)
(tau = 1 on base links); the cross term is <D_0^{F*}(zeta_b - zeta_b'), W_e> = 0; so they give |zeta_b - zeta_b'|^2 + |D_0^F W_e|^2
>= mu_n |W_e|^2. Base plaquettes give >= 0. A site of an end slice has its fibre plaquettes with weight 1/2, and a ring edge
of an end slice has its mixed plaquettes with weight 1/2. QED.
This is the SU(2) step: for U(1), tau = 1, the constants are in the kernel of D_0^F and of D_1^F on transverse fields, and the bound is false.

**Lemma H3, uniform convexity, and a global extension (PROVED).** Let r <= r_cvx(n) := mu_n/12288, C_J(n) = 240 n^2/mu_n,
beta >= beta_J(n) := 2720 C_J(n)/mu_n. Let Psi(X) := beta sum_p w_p G(a_p(X)) - sum_b w_b log J(xi_b) - sum_{e,x} w_e log varrho(Y_e(x))
on K_r(stack) (w_b, w_e in {1/2, 1}; this is a sum of the slab potentials Phi_s of F6). Then there is a C^2 function Psi~ on the
whole linear space of fields with: (i) Psi~ = Psi on K_r; (ii) beta mu_n/32 <= Hess Psi~ <= kbar(n, beta, r) < infinity everywhere;
(iii) Psi~ = beta sum_p w_p G~(a_p(X)) + sum of functions of single xi_b or single Y_e(x), where the blocks of
D^2 G~ between two different arguments a_i, a_j have norm at most 1/4 + 128 r <= 0.26 everywhere.
*Proof.* On K_r, |a_p(X)|_2 <= 2r, so by H1 and H2, with sum_p |a_p(Z)|_2^2 <= 6 ||Z||^2 (a link lies in at most 6 plaquettes):
D^2 (beta sum w_p G)(Z, Z) >= beta (mu_n/8 - 12 r) ||Z||^2. Extension. Let c be a C^2 function on R, c = 1 on (-inf, 1],
c = 0 on [4, inf), 0 <= c <= 1, |c'| <= 1, |c''| <= 2 (a quintic step over [1, 4]). N(a) := G(a) - |L a|^2/8 has
|N| <= |a|^3/6, |grad N| <= |a|^2/2, ||D^2 N|| <= |a| (H1). Put G~(a) := |L a|^2/8 + c(|a|_2^2/(2r)^2) N(a). On |a|_2 <= 2r, G~ = G.
On the support of the cutoff |a|_2 <= 4r, and with s = |a|^2/(2r)^2:
||D^2 (c(s) N)|| <= |a| + 2 (2|a|/(2r)^2)(|a|^2/2) + (|a|^3/6)(2 . 4|a|^2/(2r)^4 + 2/(2r)^2) <= (2 + 16 + 42.7 + 2.7)(2r) <= 128 r.
So D^2 (beta sum w_p G~)(Z, Z) >= beta (mu_n/8 - 768 r) ||Z||^2 >= beta (mu_n/16) ||Z||^2 everywhere, and (iii) holds
(||L^T L|| blocks are +-1/4). Jacobian: -log J(xi) = -log J(0) - <g, xi> + q_J(xi), ||D^2 q_J|| <= C_J on sup|xi| <= sqrt(mu_n)/(4 sqrt 2)
(F5 (J2)); replace q_J by c(||xi||_2^2/(n sqrt 2 r)^2) q_J: equal on sup|xi| <= r, defined everywhere (2 sqrt 2 n r is inside the
domain of J), Hessian >= -85 C_J by the same count. -log varrho: replace phi (F5 (J3)) beyond s = 1 by its second-order Taylor
polynomial at 1: C^2, convex, non-decreasing. Total: Hess Psi~ >= beta mu_n/16 - 85 C_J >= beta mu_n/32. Upper bound: every
term has a bounded Hessian. QED.

**Lemma H4, weighted positivity (PROVED).** Let a_n := arccosh(1 + mu_n/300); then a_n >= sqrt(mu_n)/12.3 >= 1/(6.2 n).
Give the weight psi = -a t to the variables of slice t and psi = -a (t + 1/2) to the time edges between t and t+1, |a| <= a_n,
and let e^psi act on fields. Then for every point X and every field Z, with H = Hess Psi~(X):
    <e^{psi} Z, H e^{-psi} Z> >= (beta mu_n/64) ||Z||^2.
*Proof.* <e^psi Z, H e^{-psi} Z> = <Z, S Z>, S the symmetric part of e^psi H e^{-psi}. The single-site and single-edge terms of Psi~
commute with e^psi. A slice plaquette has one time: no change. A time-like plaquette p has four arguments with weights
differing by at most a; the (i, j) block of its Hessian is multiplied by cosh(psi_i - psi_j) in S. So
||S_p - H_p|| <= (cosh a - 1) . 3 . 0.26 beta (three off-diagonal blocks per row, H3 (iii)). A link lies in at most 6 time-like
plaquettes. So <Z, S Z> >= <Z, H Z> - 4.68 beta (cosh a - 1) ||Z||^2 >= beta (mu_n/32 - 4.68 mu_n/300) ||Z||^2 >= beta mu_n/64 ||Z||^2.
arccosh(1 + x) >= 0.999 sqrt(2x) for x <= 1/150, and mu_n >= 4/n^2. QED.

**Fact HS0 (standard; not rebuilt here; the method is due to Helffer and Sjostrand, 1994, as I recall it; their paper was not
read for this row).** Let Psi be C-infinity on R^N with kappa <= Hess Psi <= kbar and all higher derivatives bounded,
mu = e^{-Psi} dx/Z, L = Laplacian - grad Psi . grad. For every g in C_c^inf there is u in C^3 with bounded first and second
derivatives and -L u = g - mu(g). (One construction: u = int_0^inf (P_t g - mu(g)) dt for the Langevin semigroup P_t, with the
Bakry-Emery bound |grad P_t g| <= e^{-kappa t} P_t |grad g| and its second-order analogue.)

**Proposition HS (PROVED from HS0).** Let E = (+)_i E_i be a finite orthogonal sum, K = prod_i K_i with K_i compact convex in E_i,
Psi~ a C^2 function on E with kappa <= Hess Psi~ <= kbar, psi a real weight on the index set, and kappa' > 0 with
<e^psi v, Hess Psi~(x) e^{-psi} v> >= kappa' |v|^2 for all x, v. Let mu be the probability measure on K with density
proportional to e^{-Psi~}. Then for F, G in C^1(E):
    |Cov_mu(F, G)| <= (1/kappa') ( int |e^{-psi} grad F|^2 d mu )^{1/2} ( int |e^{psi} grad G|^2 d mu )^{1/2}.
*Proof.* (1) Smooth global case, K = E, Psi~ smooth with bounded higher derivatives, G in C_c^inf. Take u from HS0 for G and
v := grad u. Differentiating: -L v_i + sum_j H_ij v_j = d_i G. Multiply the block i by e^{2 psi_i} v_i, sum, integrate against mu and
integrate by parts (v and grad v are bounded and mu has Gaussian tails). With e^{2 psi} v = e^{psi} w' and v = e^{-psi} w' this reads
    sum_i e^{2 psi_i} int |grad v_i|^2 d mu + int <e^{psi} w', H e^{-psi} w'> d mu = int <w', e^{psi} grad G> d mu,   w' := e^{psi} v.
The first term is >= 0, so kappa' ||w'||^2 <= ||w'|| ||e^psi grad G||. Then Cov(F, G) = int F (-L u) d mu = int <grad F, v> d mu
= int <e^{-psi} grad F, w'> d mu, bounded as claimed. General G in C^1 with bounded gradient: approximate.
(2) C^2 potential: mollify. The Hessian of a mollified function is an average of Hessians, so both hypotheses survive,
and all higher derivatives are bounded. Pass to the limit (dominated convergence; uniform Gaussian tails).
(3) Hard walls: add N sum_i theta_i(x_i), theta_i a C^2 convex function on E_i with bounded Hessian that vanishes exactly on K_i.
For K_i = {v : |v(l)| <= r for all l} take theta_i = sum_l q(|v(l)|), q(s) = u^3/(1 + u), u = (s - r)_+ (q'' = (6u + 6u^2 + 2u^3)/(1 + u)^3
in [0, 2]). The added Hessian is >= 0 and block diagonal in i, so it commutes with e^psi: the hypotheses hold with the same
kappa, kappa'. As N -> infinity the measures converge weakly to mu and the bound passes to the limit. QED.

**Corollary H5, the gap of one block (PROVED from HS0).** Let delta_1 be such that
r_1 = R(n) sqrt(delta_1) <= min(r_inj(n), r_cvx(n)), and beta >= beta_J(n). Let T^g_+ be the block of F6, Lambda its largest
eigenvalue. Then Lambda is simple, with a strictly positive eigenfunction, and every other eigenvalue lambda of T^g_+ has
|lambda| <= Lambda exp(-a_n), a_n = arccosh(1 + mu_n/300) >= 1/(6.2 n). The bound does not depend on M.
*Proof.* Work with the kernel k^+ on L^2(B), B = B_{r_1} (F6 (iii)). It is continuous and strictly positive on B x B, so the
argument of T1 (iv) gives Lambda = ||T^g_+||, simple, eigenfunction Omega_B > 0 continuous; and -Lambda is not an eigenvalue
(if T phi = -Lambda phi then |phi| is a top eigenvector and equality in |<phi, T phi>| <= <|phi|, T|phi|> forces phi = +-|phi|).
For k, d >= 1 let P_{k,d} be the probability measure on paths (zeta_t)_{-k <= t <= d+k}, (Y_{3,t})_{-k <= t < d+k} in the product of balls with
density proportional to prod_t exp(-Phi_s(zeta_t, Y_{3,t}, zeta_{t+1})). Its potential is the Psi of H3 for the stack I = [-k, d+k].
For F, G in C^1(B): E[F(zeta_0) G(zeta_d)] = <1, T^k F T^d G T^k 1>/<1, T^{2k+d} 1> (T = T^g_+), which tends to
<F Omega_B, (T/Lambda)^d G Omega_B> as k -> infinity (||Omega_B|| = 1; spectral theorem, simple top, no -Lambda). Likewise the means.
By H3, H4 and Proposition HS (weight psi = -a_n t; kappa' = beta mu_n/64):
    |Cov_{P_{k,d}}(F(zeta_0), G(zeta_d))| <= (64/(beta mu_n)) sup|grad F| sup|grad G| exp(-a_n d),   uniformly in k and M.
Let k -> infinity: |<F Omega_B, Q (T/Lambda)^d Q G Omega_B>| <= the same bound, Q the projection off Omega_B.
Let phi be an eigenvector orthogonal to Omega_B, eigenvalue lambda. The functions F Omega_B, F in C^1(B), are dense in L^2(B)
(Omega_B is continuous and positive on the compact B). Choose F with <F Omega_B, phi> != 0. For even d the spectral sum
sum_i (lambda_i/Lambda)^d |<F Omega_B, phi_i>|^2 has non-negative terms, so (lambda/Lambda)^d |<F Omega_B, phi>|^2 <= C_F exp(-a_n d)
for all even d. Hence |lambda| <= Lambda exp(-a_n). QED.

Remarks. (1) This step replaces "Gaussian decoupling across blocks" (S1O:566-568). No covariance interpolation is used.
The rate a_n is of the order of the true one, arccosh(1 + mu_n/2); the constant 300 is crude.
(2) What is SU(2)-specific: Lemma H2. What is special to the thin geometry: the mass is a local term (one fibre, one edge),
so convexity holds on a product of balls and the weight commutes with the walls.
(3) HS0 is the one external analytic input of this row. It is a statement about a smooth uniformly convex potential on R^N.
A reader who wants no external input can replace Proposition HS by the Brascamp-Lieb inequality step by step in time;
I checked that route: it gives a contraction only in a norm adapted to the Riccati fixed point of the Gaussian part,
and with the temporal links integrated inside each step it needs two-sided bounds on mixed derivatives of marginals.
I did not carry it out.

### Step 6. Assembly: the two theorems, in their stated range

**6.1 Thresholds (all explicit up to the absolute C_3, C_4 of CH).**
    delta_1(n) := delta_0(n) / (2 R(n)^2),  R(n) = 1.5e5 n^10.   Then r_1 = R(n) sqrt(delta_1) = sqrt(delta_0/2) = r_inj(n),
    and r_1 <= r_cvx(n) = mu_n/12288 (delta_0(n) <= (4200 n^7 . 6.1e4 n^9)^{-2} is far below (mu_n/12288)^2 >= 1e-7 n^{-4}).
    eps_1 := eps(n, beta, delta_1) = 6 n^2 beta^{6 n^2} e^{27 n^2} e^{-beta delta_1/4}  (Theorem BAD).
    beta_0(n) := (192 n^2/delta_1) log(192 n^2/delta_1).   For beta >= beta_0(n): eps_1 <= exp(-beta delta_1/8)
    (the "Threshold" computation of S1O:262-268 with delta_1 in place of delta_0; it uses only delta <= 2), and
    beta >= max(1, beta_J(n)) (beta_J <= 40800 n^6).
    a_n := arccosh(1 + mu_n/300) >= 1/(6.2 n).     M_1(n, beta) := 1/(1922 n^2 eps_1) >= exp(beta delta_1/8)/(1922 n^2).
Sizes: delta_1 is of order n^{-52} and beta_0(n) of order n^{54} log n. They are crude (the chart constants of CH dominate).

**Theorem A (the corrected (S1-T); PROVED from the inputs listed in 6.4).** Let n >= 2, beta >= beta_0(n), and M even with
4 <= M <= M_1(n, beta). Let T be the transfer operator of Step 3 on H (gauge-invariant slice functions), lambda_0 = ||T||,
Omega its positive eigenvector, H = H_+ (+) H_- the sectors of the centre flip c_4. Put eta := (2 M eps_1)^{1/2} <= 1/(31 n). Then:
(A1) [flip-even gap] the spectrum of T on H_+ minus C Omega lies in [0, lambda_0 (e^{-a_n} + 2 eta)], inside [0, lambda_0 e^{-a_n/2}].
     So the gap there is at least a_n/2 >= 1/(12.4 n), with no other dependence on M or beta.
(A2) [vacuum form] for flip-even gauge-invariant bounded slice functions F, G and all d >= 0, in the state of the infinite cylinder,
     |<F(0) G(d)> - <F><G>| <= ||F Omega|| ||G Omega|| exp(-(a_n/2) d).
(A3) [flip-odd sector; this proves defect (D1) for SU(2)] ||T restricted to H_-|| >= lambda_0 (1 - 2 eta). So T has an
     eigenvalue in [lambda_0 (1 - 2 eta), lambda_0) with eigenvector in H_-, orthogonal to Omega: on all of H the gap is at most
     -log(1 - 2 eta) <= 3 (2 M eps_1)^{1/2} <= 3 (2M)^{1/2} exp(-beta delta_1/16). The remaining spectrum of T on H_- lies in [0, lambda_0 (e^{-a_n} + 2 eta)].
     The low spectrum is: two nearly degenerate states (the two Z_2 holonomy sectors), then a gap of at least a_n/2.
*Proof.* Take chi = the indicator of G_{r_1}(slab) (F6). T = T^g + T^b, all three commute with c_4 (Step 3, (c4)), and
||T^b|| <= eta lambda_0 (T3). By F6, T^g = T^g_+ (+) T^g_- (+) 0 and c_4 swaps the two blocks. So phi -> (phi +- c_4 phi)/sqrt 2 maps
L^2(S^+)^inv unitarily onto the flip-even, resp. flip-odd, part of the range, and carries T^g_+ to T^g restricted to that part.
By H5 the eigenvalues of T^g on H_+ (and on H_-) are Lambda, simple, then values of modulus <= Lambda e^{-a_n}, and 0.
Weyl's inequality (min-max) for the self-adjoint compact operators T = T^g + T^b on H_+: lambda_0 <= Lambda + eta lambda_0 and
lambda_2(T on H_+) <= Lambda e^{-a_n} + eta lambda_0; also Lambda <= lambda_0 + eta lambda_0. So lambda_2 <= lambda_0 ((1 + eta) e^{-a_n} + eta)
<= lambda_0 (e^{-a_n} + 2 eta). T >= 0 (T1), so the spectrum on H_+ minus C Omega is in [0, lambda_2]. Since a_n <= 0.12,
e^{-a_n/2} - e^{-a_n} >= 0.44 a_n >= 2/(31 n) >= 2 eta: (A1). (A2) is (A1) with the vacuum formula of Step 3 (F Omega, G Omega are in H_+).
(A3): on H_-, lambda_1(T) >= lambda_1(T^g) - eta lambda_0 = Lambda - eta lambda_0 >= lambda_0 (1 - 2 eta), and
lambda_2(T on H_-) <= Lambda e^{-a_n} + eta lambda_0 as before. lambda_0 is simple (T1), so the eigenvalue is < lambda_0. QED.

**Theorem B (the torus form (S1-tor); PROVED from the same inputs).** Let n >= 2, beta >= beta_0(n), base torus (Z/N) x (Z/M),
N, M even >= 4. Let F, G be gauge-invariant functions with values in [-1, 1], invariant under the two base centre flips
(automatic if the supports contain no non-contractible base loop, S1O:157-160), C^1 in the link variables over the base
sets X, resp. Y, with Lipschitz constants Lip(F), Lip(G) for the product of the metrics rho. Then
    |mu^tw(F G) - mu^tw(F) mu^tw(G)| <= (64/(beta mu_n)) Lip(F) Lip(G) exp(-a_n dist(X, Y)) + 4 N M eps_1.
*Proof.* Let E_g := G_{r_1}(whole base torus). If every base point is delta_1-good then U is in E_g (F3 (i)); so
p := mu^tw(not E_g) <= N M eps_1 (Theorem BAD with |S| = 1). K_D is the torus: c(D) = 1, H^1 = Z_2^2, and the flips permute
the four classes. By F5, for flip-invariant gauge-invariant f, mu^tw(f | E_g) = nu(f~), f~(xi, Y) := f(U^{xi,Y,1}), nu the
probability measure proportional to exp(-Psi) on K_{r_1}(torus), Psi as in H3 with all weights 1. H2 holds on the torus
(all weights 1), H3 gives Psi~, and H4 holds for any weight psi on base points and base edges whose values on the
variables of one plaquette differ by at most a_n (same count: a link lies in at most 6 plaquettes). Take
psi(b) := a_n min(dist(b, Y), dist(X, Y)) and psi(e) := the mean of psi at the two ends of e. On a mixed plaquette the values
differ by at most a_n; on a base plaquette two edge values differ by half the sum of two differences along base edges, at most a_n.
psi = a_n dist(X, Y) on the variables over X and psi = 0 on those over Y. Proposition HS:
|Cov_nu(F~, G~)| <= (64/(beta mu_n)) exp(-a_n dist(X, Y)) sup|grad F~| sup|grad G~|, and |grad F~| <= Lip(F) (the differential of exp has
norm <= 1). Last, mu(h) = (1 - p) nu(h~) + p e(h) with |e(h)| <= 1 for h = F, G, FG, which gives |Cov_mu - (1 - p) Cov_nu| <= 4p. QED.

**6.2 What Theorems A and B say about Lemma PE (S1O:550-553).**
- PE's clause "(S1-T) with the same rate" is false as printed. (A3) proves it for every beta >= beta_0(n) and even M <= M_1(n, beta):
  the gap on the complement of the top eigenvector is at most 3 (2 M eps_1)^{1/2}. (CK:174-187 had the limit beta -> infinity at fixed M.)
- The corrected clause, gap >= c/n on the flip-even gauge-invariant sector with c = 1/12.4, is PROVED for even M in [4, M_1(n, beta)].
  M_1 grows like exp(beta delta_1/8). The rate and beta_0(n) do not depend on M in that window.
- PE's clause (S1-loc) on the torus: PROVED in the form of Theorem B, with the non-decaying term 4 N M eps_1 (useful when N M eps_1 << 1)
  and with Lip(F) Lip(G)/(beta mu_n) in place of C(n, beta, K). (Z2-b) shows that some non-decaying term must be present on a torus.
- NOT proved: either clause for M above M_1(n, beta) (a positive density of defects per slab). See Step 7.

**6.3 Where each item of the brief's list went.**
- Local (conditional) Peierls bound: not proved and not used in the window; replaced by the operator Peierls bound T3 (global).
- Faddeev-Popov Jacobian: closed in the fibre-wise gauge (F5): local, with explicit first and second derivative bounds.
- Gaussian decoupling across blocks: replaced by uniform convexity (H2, H3) and the weighted covariance bound (HS, H4, H5).
- Sum over Z_2 labels: F5 (the sum over H^1), F6 (block form of T^g), and the sector statements (A1), (A3).
- Convergence: nothing to converge in the window. For M > M_1 a convergent defect expansion is what is missing.

**6.4 Inputs of Theorems A and B.**
(I1) READ, held by the check CK: Lemma RP, Lemma CB, Lemma Z, Theorem BAD (S1O:178-256; I re-read the proofs for the rectangular base).
(I2) READ, held by CK after correction: CH-D for D = one base point (the fibre chart with uniqueness), S1O:305-317, CK:47-64.
(I3) READ: Lemma L on one fibre (Delta^F >= mu_n in degrees 0 and 1), CH:92-97 and S1O:321-330; G1, G2 of CH:114-116.
(I4) Standard, not rebuilt: Fact HS0 (Poisson equation for a smooth uniformly convex potential with bounded derivatives on R^N).
Everything else in Steps 3 to 6 is proved in this file, by hand, and is unchecked by another model.

### Step 7a. Fact tests, a conditional Peierls bound, and the exact missing statement for all M

**7.1 Fact tests (READ: D/FINISH.md rows 786, 838, 839, 843, 845, result fields).**
(F1) U(1), no gap in the Coulomb phase (row 786: a group-blind proof of a volume-uniform gap is ruled out by a written theorem).
     PASSED. The route is not group-blind. It breaks for U(1) at three places: F1/F4 (the stabiliser of the fibre vacuum
     is the whole of U(1), not a finite group, so the fibre-wise gauge leaves a continuous residual gauge group);
     F2 (G2 needs the two anticommuting holonomies); and H2 (for trivial Ad the constants lie in the kernel of D_0^F
     and the harmonic fields in the kernel of D_1^F on transverse fields, so there is no uniform convexity). This matches
     Proposition U1 (S1O:441-463, CK:120-138): the U(1) Hessian has modes at 4 sin^2(pi/M). Twisted U(1) has no zero-action twist
     eater at all (CK:15-45). The group-blind parts of this file are T1 to T3 only (transfer operator, sectors, Peierls).
(F2) Q_8 and 2T (rows 838, 843: at the crossover a tool must see spin 2 or 3; the finite groups freeze near 1.15 and 2.15).
     DOES NOT BIND HERE, and I say why. Theorems A and B are weak-coupling statements, beta >= beta_0(n) of order n^54 log n.
     At such beta the Q_8 and 2T theories are frozen and the analogous statements hold for them for a trivial reason
     (every non-flat plaquette costs a fixed multiple of beta). So "they would otherwise pass" is a true pass, not a
     false positive. The proof here still does not apply to them: F1, F5, H1 to H4 use the exponential chart and the
     Lie algebra, which a finite group does not have (as row 843 found for (C4)-(C7) and D1: not formulable).
     Nothing in this file reaches order-one coupling, where the Q_8/2T test binds.
(F3) Worst-case Dobrushin caps (2/3, 0.775), the layer bound 4 G_3 = 1.0109 (row 839), (AN1) (row 845).
     CONSISTENT. No worst-case or background-uniform bound is used: T3 is a trace bound on the full torus, and H3 to H5
     are for the restricted ensemble. (A3) agrees with Proposition TB2 of row 839 in kind: a lower bound on the
     flip-odd energy that is uniform in the background cannot hold at large beta, because that energy is at most
     3 (2 M eps_1)^{1/2} in the window.
(F4) Order-one window (bare beta_W 2.3 to 2.6) and (SEED-FP): NOT TOUCHED. This is a weak-coupling result on a thin torus.

**7.2 Lemma CP, a local conditional Peierls bound for trivial flux (PROVED; not used in Theorems A, B).**
This is the first item of the brief's list. It holds for conditional measures, which Theorem BAD does not (S1O:279).
Let gamma be a finite set of base points (in Z x (Z/M) or in a base torus), C(gamma) := the base points outside gamma at
l^infinity distance 1 from gamma, gamma^+ := gamma u C(gamma). Free links: the links with at least one end over gamma.
The exterior data U_ext are all other links. Hypothesis (H_r), 0 < r <= 1: there are a gauge transformation h on the sites
over C(gamma), fields xi_b (b in C(gamma)) and Y_e (e an edge of K_{C(gamma)}) with sup <= r, and signs eps~_e on all edges of
K_{gamma^+}, flat on all faces of K_{gamma^+}, such that U^h = V e^{xi_b} on the fibre links over C(gamma) and = eps~_e e^{Y_e}
on the base links with both ends in C(gamma). (The collar is in the chart and its sign field extends flat across gamma:
trivial flux.) Then for beta >= 1 and delta > 0:
    mu^tw( every b in gamma is delta-bad | U_ext ) <= ( beta^{9 n^2} e^{131 n^2} e^{-beta (delta - 108 n^2 r^2)} )^{|gamma|}.
*Proof.* Let A_gamma := the sum of d_p over the plaquettes with at least one free link. The conditional law of the free
links has density proportional to exp(-beta A_gamma) for Haar measure: no other plaquette contains a free link.
Numerator. A plaquette with base point b in gamma has its two links at its first site free. On the event, each b in gamma
has such a plaquette with d_p > delta, distinct for distinct b; so A_gamma >= delta |gamma| and the numerator is <= e^{-beta delta |gamma|}.
Denominator. Every site of a plaquette with a free link lies over gamma^+ (l^infinity distance <= 1 from a point of gamma);
its links are free or have both ends over C(gamma). There are at most 6 n^2 |gamma^+| <= 54 n^2 |gamma| such plaquettes and at
most 6 n^2 |gamma| free links (4 n^2 start over each point of gamma; 2 n^2 base links end there). Extend h by 1 over gamma.
Let s := beta^{-1/2} and B := the free-link configurations with (U^h)_l within s of V_l on the fibre links over gamma and within s
of eps~_e on the free base links. By invariance, Haar(B) >= (s^3/40)^{6 n^2 |gamma|} (S1O:235-237). On B every link of every
plaquette of A_gamma is within max(r, s) of V_l times a flat sign, so d_p <= 2 max(r, s)^2 (proof of F3 (iii)) and
beta A_gamma <= 108 n^2 (beta r^2 + 1) |gamma|. So the denominator is at least
exp(-[9 n^2 log beta + 6 n^2 log 40 + 108 n^2 + 108 n^2 beta r^2] |gamma|), and 6 log 40 + 108 <= 131. QED.
Two thresholds. If the collar is delta'-good in the sense of F3 with r = R(n) sqrt(delta') and delta >= 216 n^2 R(n)^2 delta',
the bound is (beta^{9 n^2} e^{131 n^2} e^{-beta delta/2})^{|gamma|}. This is the ratio of thresholds asked for at S1O:558-560.
Flux -1. If the sign field of the collar does not extend flat across gamma, no such bound can hold: gamma must contain
a bad point (Proposition FLUX, S1O:503-514). Such a region is not rare given its exterior. Its weight must be compared
with a different exterior (the string must be summed), which is the Z_2 sum of 7.3 (iii).

**7.3 The missing statement for M > M_1 (OPEN), and what this file supplies towards it.**
Theorem A uses M at one place only: T3, ||T^b|| <= (2 M eps_1)^{1/2} lambda_0, the cost of asking a whole ring slab to be clean.
For M eps_1 >= 1 a slab has defects with probability close to one and the bound is void. The statement that remains open is:

    (A1-all) For each n >= 2 there are beta_*(n) and c > 0 such that for beta >= beta_*(n) and EVERY even M >= 4 the spectrum
    of T on H_+ minus C Omega lies in [0, lambda_0 e^{-c/n}].   [Equivalently (A2) for every even M.]
    (B-all) The same for (S1-loc) in infinite base volume: for the Gibbs state on (Z/n)^2 x Z^2 obtained as N, M -> infinity,
    |Cov(F, G)| <= C(n, F, G) exp(-(c/n) dist(X, Y)) for local gauge-invariant F, G.

Both need an expansion for a gas of defects at positive density in the convex sea. Stated as a list:
(i)   PROVED here: on any set of base points and edges whose chart coordinates lie in the balls of radius r_1, given
      any values of the neighbouring variables inside the same balls, the conditional potential is uniformly convex
      (H2, H3: the bounds are for arbitrary stacks and restrict to subspaces), and its covariances decay at rate a_n
      uniformly in those boundary values (HS, H4). So the mixed second derivative of the sea free energy in two
      distant boundary data is bounded by (64/(beta mu_n)) (derivative norms) exp(-a_n distance).
(ii)  PROVED here: the conditional Peierls bound for trivial-flux regions (CP), with the two-threshold ratio.
(iii) OPEN: the sum over Z_2 flux labels at positive density. F5 gives the exact formula (a sum over H^1 of the good
      region). Regions of flux -1 come in even numbers on a closed base and are joined by strings that flip-even local
      observables do not see. What is missing is the weight of a flux -1 defect: an upper bound exp(-c beta) for its
      activity relative to the sea, proved with the string summed. (Theorem BAD gives it unconditionally; CP does not apply.)
(iv)  OPEN: decoupling of the sea between defects beyond second order: tree-graph bounds for the higher mixed
      derivatives of the sea free energy in several boundary data (joint cumulants in a uniformly log-concave measure),
      or an interpolation formula that needs only (i). With (i)-(iv), a Kotecky-Preiss criterion on the base lattice
      at scale n log beta closes (A1-all) and (B-all).
I do not claim (iii) or (iv). I do not write that this is the only way to all M.

**7.4 A remark on what "uniformly in M" can mean (ARGUED).** By (Z2-a), (A3) and CK:174-187, a gap of order 1/n on the whole
gauge-invariant space cannot hold uniformly in M at fixed beta: it fails for M up to M_1(n, beta) at least. The expected
picture for all M is: flip-even gap >= c/n for every M (this is (A1-all)); flip-odd energy sigma_M about M sigma(n, beta),
which exceeds c/n only when M is above about (c/n)/sigma, a scale exponential in beta. So a consumer that needs the full
gap must either take M above that scale (then it needs (A1-all) and a lower bound on sigma, an area-law input),
or work in the flip-even sector (then Theorem A serves it for M <= M_1, and (A1-all) beyond).

### Step 7b. GUIDE run (discharges nothing)

Script and output: /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane862/scripts/guide_h.py
and guide_h.out in the same directory. Run on the MacBook, numpy, one BLAS thread, 5.5 s, peak 177 MB.
It builds D_0^F, D_1^F and the stack form sum_p w_p |D_1 Z|^2 on fibre-transverse fields from the definitions of CH:35-47
(signs of CH:35), for (n, M, time slices) = (2, 4, 3), (2, 6, 4), (3, 4, 3). Criteria were written before the run.
(1) D_1^F D_0^F = 0: exactly 0 in all cases. PASS (the conventions are read correctly).
(2) Least eigenvalue of D_0^{F*} D_0^F = mu_n (2.000000 for n = 2, 1.000000 for n = 3); least eigenvalue of D_1^{F*} D_1^F on
    ker D_0^{F*} = mu_n. PASS (Lemma L on one fibre, as used in H2).
(3) Lemma H2: least eigenvalue of the weighted stack form = 1.127, 1.146 (n = 2; bound mu_n/2 = 1) and 0.567 (n = 3; bound 0.5). PASS.
(4) Lemma H4 for the quadratic part (beta = 1): at a = a_n the symmetric part of e^psi (Q/4) e^-psi has least eigenvalue
    0.2806, 0.2855 (n = 2; my bound 0.2188) and 0.1412 (n = 3; my bound 0.1094). PASS.
    The weighted form stays positive exactly up to a_crit = 1.3170 (n = 2) and 0.9624 (n = 3), which equal
    arccosh(1 + mu_n/2) to four digits. So the true rate of the quadratic part is arccosh(1 + mu_n/2), about pi/n for
    large n; the proved a_n = arccosh(1 + mu_n/300) is smaller by a factor of about 12. GUIDE only.
(5) Lemma H1: the finite-difference Hessian of G at 0 equals L^T L/4 to 2e-8; over 4000 random points and unit
    directions the third directional derivative of G is at most 0.554 (bound 1). PASS.
No criterion failed. The run checks linear algebra and conventions only; it says nothing about T3, F1 to F6, HS or the assembly.

### Step 8. Status table and RESULT

**Lemma PE is not proved as printed, and cannot be: one clause is false. Its corrected form is proved in a window of M.**
Nothing in this file was checked by another model. "Even M" means even M >= 4.

**The theorem, with all hypotheses (restating Theorem A).** Lattice (Z/n)^2 x Z x (Z/M) (time = base direction 3, ring =
base direction 4), SU(2) Wilson action with the centre twist on the stack P_0 of fibre plaquettes (S1O:125-166), n >= 2.
T = the transfer operator of Step 3 on gauge-invariant slice functions. delta_0(n), C(n) from CH:197-206; R(n) = 1.5e5 n^10;
delta_1 = delta_0(n)/(2 R(n)^2); beta_0(n) = (192 n^2/delta_1) log(192 n^2/delta_1); eps_1 = 6 n^2 beta^{6n^2} e^{27 n^2} e^{-beta delta_1/4};
M_1(n, beta) = 1/(1922 n^2 eps_1) >= exp(beta delta_1/8)/(1922 n^2); a_n = arccosh(1 + mu_n/300) >= 1/(6.2 n), mu_n = (2 sin(pi/2n))^2.
For beta >= beta_0(n) and even M with 4 <= M <= M_1(n, beta):
  the spectrum of T on the flip-even sector, off the vacuum, lies in [0, lambda_0 exp(-a_n/2)]   (gap >= 1/(12.4 n));
  the flip-odd sector has its top eigenvalue in [lambda_0 (1 - 2 (2 M eps_1)^{1/2}), lambda_0), and then the same gap.

| Item | Statement | Status | Where |
|---|---|---|---|
| (Z2-a), (Z2-b) | exact Z_2 model: odd sector at M log(1/r); torus covariance 4 rho^2 r^{N-2}/((1+rho)^4 (1+r^N)^2) | PROVED (model) | 2.1 |
| T1, T2 | transfer operator: trace formula, positivity, simple top eigenvalue, sectors of c_4 | PROVED | Step 3 |
| BAD, rectangular base | eps^{|S|} bound on (Z/N) x (Z/M), N, M even | READ (S1O:178-256), re-read for this case | Step 3 |
| T3 | operator Peierls bound, norm of T^b at most (2 M eps_1)^{1/2} lambda_0 | PROVED (from BAD) | Step 3 |
| F1 | fibre chart with uniqueness | READ (CH-D at one point; held by CK) | Step 4 |
| F2, F3, F4 | edge chart, Z_2 class, thresholds, uniqueness; R(n), r_inj | PROVED (from F1, G1, G2) | Step 4 |
| F5 | measure in the chart; local Jacobian J with (J1)-(J3); sum over H^1(K_D; Z_2) | PROVED | Step 4 |
| F6 | block form of T^g; kernel exp(-Phi_s) on a product of balls | PROVED | Step 4 |
| H1, H2, H3, H4 | third-derivative bound; local mass mu_n/2; convex global extension; weighted positivity at a_n | PROVED (H2 from Lemma L on a fibre, READ) | Step 5 |
| HS0 | Poisson equation for a smooth uniformly convex potential on R^N | standard, not rebuilt (external input) | Step 5 |
| HS, H5 | weighted covariance bound on products of convex sets; gap exp(-a_n) of one block, uniform in M | PROVED from HS0 | Step 5 |
| Theorem A | (A1) flip-even gap, (A2) vacuum form, (A3) flip-odd near-degeneracy, for M <= M_1(n, beta) | PROVED from the inputs of 6.4 | Step 6 |
| Theorem B | torus covariance bound with the term 4 N M eps_1 | PROVED from the same inputs | Step 6 |
| Lemma CP | conditional Peierls bound, trivial flux, two thresholds | PROVED | 7.2 |
| parity term for SU(2) | the non-decaying torus term is really present | ARGUED | 2.1 |
| 7.4 | what "uniformly in M" can mean | ARGUED | 7.4 |
| rate | the quadratic part allows any rate below arccosh(1 + mu_n/2) | GUIDE | 7b |
| (A1-all), (B-all) | Theorem A and (S1-loc) for every M, in particular M > M_1(n, beta) | OPEN | 7.3 |
| 7.3 (iii), (iv) | flux -1 activity with the string summed; sea decoupling beyond second order | OPEN | 7.3 |
| odd M; C_3, C_4; sizes | odd M (BAD is for even sides); numerical values of the absolute C_3, C_4; delta_1 of order n^{-52} is crude | OPEN | - |

**What changed against the brief's list.** Local conditional Peierls bound: proved for trivial flux (CP); the window uses the
global bound T3 instead. Faddeev-Popov Jacobian: closed, local, by the fibre-wise gauge (F5). Gaussian decoupling across
blocks: replaced by uniform convexity and the weighted covariance bound (H2 to H5). Sum over Z_2 labels: F5, F6, (A1), (A3).
Convergence: not needed in the window; open beyond it. No estimate of Balaban is used. Nothing from the Sussman-Alpoge
account is used (credit to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, would be due
for any use; there is none here). Tools credited from memory, papers not read for this row: transfer matrices of lattice
gauge theories (Luscher; Osterwalder and Seiler), reflection positivity and chessboard estimates (Osterwalder and Seiler;
Frohlich, Israel, Lieb and Simon; rebuilt in S1O), positive kernels (Jentzsch), the weighted covariance identity
(Helffer and Sjostrand; weights in the manner of Combes and Thomas), convex-measure inequalities (Brascamp and Lieb).
Sources inside the lane: S1O (row 842, Claude Opus 5.5), its check CK (row 856, Codex gpt-6-astra, a check, not an audit), CH.

**Next decisions for the lead (not done here).** (1) A check of this file by another model, first of T3, F4 to F6, H3, H4 and
the proof of Theorem A. (2) Whether the consumer of S1 can work in the flip-even sector with M <= M_1(n, beta); if it
needs every M, the open item is 7.3 (iii)-(iv). (3) HS0 could be rebuilt in the lane if no external input is wanted.

Erratum to the reading notes of Steps 1a and 1b (line numbers only, checked 2026-11-13 against the source): Remark 2 of Theorem BAD is at S1O:279 (not 277); the centre-flip remark (iii) is at S1O:157-160 (not 160-163); Theorem CH-D is at S1O:305-317. No statement changes.

RESULT: Lemma PE as printed is false in its (S1-T) clause (Theorem A (A3), proved: for beta >= beta_0(n) and even M <= M_1(n, beta) the flip-odd sector lies within 3 (2 M eps_1)^{1/2} of the vacuum); the corrected statement is PROVED in a window, not uniformly in M: for n >= 2, beta >= beta_0(n) = (192 n^2/delta_1) log(192 n^2/delta_1) with delta_1 = delta_0(n)/(2 R(n)^2) (order n^54 log n), and every even M with 4 <= M <= M_1(n, beta) = 1/(1922 n^2 eps_1) >= exp(beta delta_1/8)/(1922 n^2), the Wilson transfer operator of the twisted thin torus in a base direction has gap >= a_n/2 >= 1/(12.4 n) on the flip-even gauge-invariant sector (Theorem A), and torus covariances of flip-invariant gauge-invariant observables decay at rate a_n >= 1/(6.2 n) up to the term 4 N M eps_1 (Theorem B); the route is a fibre-wise gauge with a local Jacobian, an SU(2)-only local mass giving uniform convexity, a weighted Helffer-Sjostrand bound, and an operator Peierls bound from Theorem BAD; inputs are Theorem BAD and CH-D for one fibre (both held by the check of row 842) and one standard fact (HS0), all else proved here by hand and unchecked; OPEN: every M above M_1(n, beta) (defects at positive density: the flux -1 activity with strings summed and sea decoupling beyond second order), so S1 uniformly in M is not proved.
