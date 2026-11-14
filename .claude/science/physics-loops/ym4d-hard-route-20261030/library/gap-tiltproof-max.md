# gap-tiltproof-max (FINISH row 977)

author: Claude Fable 5.2 max, laptop Agent lane, FINISH row 977 (gap-tiltproof-max), checked by no one
start time (date -u): Sat Nov 14 22:21:54 UTC 2026

## 0. Target statement

Target: (TILT-COV-sup) of row 968 (library/gap-avgcurv-max.md, statement at line 160),
for SU(2) Wilson at beta = 2.3, uniform over the slices and sides that the seed box of
row 974 needs (library/gap-trajtest-opus.md; a = 30). Goal: a proof, or a counterexample.
The verbatim statement is copied in Step 1 below (the first read).

## Plan (at most eight steps; one step per response; each step is appended here before the next)

1. Read the statement and definitions (gap-avgcurv-max.md Sections 3-4; the seed-box need in gap-trajtest-opus.md). Copy the statement verbatim.
2. Fact tests, one line of verdict each: free photon, compact U(1), frozen Q_8, frozen 2T, SMALL-BOX, K7, FT-FK.
3. Write at least three approaches of my own, from the statement and the SU(2) structure only. Pick the best. Name its CRUX lemma.
4. Attack the crux lemma, route 1.
5. Attack the crux lemma, route 2 (only if route 1 fails or is partial).
6. Attack the crux lemma, route 3 (only if routes 1-2 fail), or harden the proof / counterexample.
7. Only now: read library/prior/gap-lit-tiltcov.md (row 971) and the RESULT texts of FINISH rows 968-976. Say per approach whether it is already there or in the literature.
8. Current state, next step, proposed GUIDE rows (criteria fixed in advance), final RESULT line.

Marks used: PROVED, ARGUED, OPEN.

## Step 1. The statement and its objects (READ; copied from gap-avgcurv-max.md lines 46-52, 126-168; no new claim)

Objects. B a periodic spatial box, L = 3|B| links, M = (S^3)^L in R^N, N = 4L. V(x) = -beta sum_p (1/2) tr x_p.
T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2) (temporal gauge). Omega its top eigenfunction. m(dw) = e^(-V(w)/2) Omega(w) dw.
J(dx, dw) = m(dx) e^(beta <x, w>) m(dw)/Z, the two-slice vacuum law. Elitzur: Cov_m(w) = Id/4.
Fix s in (0, 1/beta), s' = 1/beta - s, lam = beta s, c = s s'/(s + s') = lam (1 - lam)/beta.
q~ := x/s + w/s'. For 0 <= b <= beta and phi in R^N:
  J_(b,phi)(dx, dw) := e^(b <x, w> + <phi, q~>) m(dx) m(dw) / Z_b(phi).        b_t := t/(s s'), t in [0, c].

Verbatim (line 160):
  (TILT-COV-sup):  Var_(J_(b_t,phi))(<z, q~>) <= kbar_(s,t) |z|^2  for every phi in R^N and every z orthogonal to the gauge orbit of phi.
Use (Theorem POL-BR, 3.3, conditional on BBD Theorem 3.6 and Theorem BR): then nu_s has (LSI-br)_s with
  1/alpha_s <= integral over [0, c_s] of exp(2 integral over [0, t] of kbar_(s,u) du) dt,
and (HC-vac)_alpha holds with alpha = (1/2) integral over (0, 1/beta) of alpha_s ds.
Zero field (Lemma Z, PROVED there): Cov_(J_(b,0))(q~) = k0 Id, k0 = (1/4)(1/s^2 + 1/s'^2 + 2 tau_b/(s s')) <= 1/(4 c^2).
Lemma NEC (PROVED there, given POL-BR and Prop HC): k* >= 2 beta log(1/E_1(B)), k* the sup of kbar over the middle half of the slices.

What a proof must deliver: a function kbar_(s,t), finite, with the box dependence that row 974 fixes (read next, Step 1b),
such that (1/2) integral of alpha_s ds >= K_30 = 0.811 (row 960 value, unchecked there).

## Step 1b. What the a = 30 seed box asks of kbar (READ gap-trajtest-opus.md lines 28-56, 258-276)

Seed box (a; (4a)^3), a = 30: spatial side 120. Need (1/2) integral over (0, 1/beta) of alpha_s ds >= K_30 = 0.811 at beta 2.3.
So the average of alpha_s over the slices must be at least 2 beta K_30 = 3.73. Row 974: at beta 2.3 nothing excludes a >= 21
(m_G about 1.2, GUIDE). The sides in play are up to 120, far above the sides 4-16 of the GUIDE runs.

## Step 2. Fact tests (run before any proof attempt; one verdict per test)

**2.0 Test ZERO-CEIL (my own; PROVED by hand from Lemma Z of row 968; elementary, Lean-formalizable).**
The statement must hold at phi = 0, where every z is horizontal. Lemma Z and tau_b >= 0 give, for EVERY admissible kbar,
  kbar_(s,t) >= k0_(s,b_t) >= k00_s := (1/4)(1/s^2 + 1/s'^2).
(Dropping the single point phi = 0 does not help: Cov is continuous in phi, and the horizontal spaces at phi -> 0 have dimension 9|B| > 0.)
So the output of Theorem POL-BR obeys 1/alpha_s^thm >= integral over [0, c] of e^(2 k00 t) dt, that is
  alpha_s^thm <= 2 k00/(e^(2 k00 c) - 1) = (beta^2/2) r (r + 2)/(e^(beta r/2) - 1),   r := (1 - lam)/lam + lam/(1 - lam) >= 2.
(Check: p = lam(1 - lam); 1/lam^2 + 1/(1 - lam)^2 = (1 - 2p)/p^2 = r(r + 2); 2 k00 c = beta r/2.)
For beta >= 3/2 the right side decreases in r on r >= 2 (d log/dr < 1/2 + 1/4 - beta/2 <= 0). So its maximum is at lam = 1/2:
  alpha_s^thm <= 4 beta^2/(e^beta - 1)   and   alpha^thm := (1/2) integral of alpha_s^thm ds <= 2 beta/(e^beta - 1).
At beta 2.3: alpha_mid^thm <= 2.358 (the Gaussian reference is 4 beta = 9.2) and alpha^thm <= 0.513 < K_30 = 0.811.
Finer (trapezoid by hand, step 0.05 in lam; values 0.0075, 0.147, 0.534, 1.040, 1.515, 1.892, 2.155, 2.308, 2.358 at lam = 0.10 ... 0.50):
  alpha^thm <= 1.078/(2 beta) = 0.234 (arithmetic, ARGUED until bounded by monotone Riemann sums).
Verdict. For SU(2) at beta 2.3 on the a = 30 box, NO kbar that satisfies (TILT-COV-sup) gives (LSI-br-seed)_30 through
Theorem POL-BR: the zero field alone caps the output at 0.513 (PROVED) and 0.234 (ARGUED). K_a <= 0.513 needs a >= 50;
K_a <= 0.234 needs a >= 117 (K_117 = 0.233). With the true tau_b > 0 the cap is lower (row 968 3.4: 0.04 with tau = 1, a about 830).
This is a counterexample to the USE of the statement at a = 30, not to the statement. It binds every model with
Cov_m = Id/4 (SU(2), Q_8, 2T); for U(1) (Cov_m = Id/2) the cap is 4 beta/(e^(2 beta) - 1) = 0.093 at beta 2.3.
Consequence for this row: the mathematical content left is the box-uniform bound itself (a finite kbar, uniform in
the side and in phi, at beta 2.3). The seed size must then be recomputed from the proved kbar; it is at least 117.

**2.1 Free photon (FP, row 929).** The statement HOLDS, mode by mode, with kbar = k/(1 - k t) exact and independent of phi
(a linear tilt does not change a Gaussian covariance; ported from row 968 3.3 check (i), 4.2(a)). kbar grows with the box
in the softest mode: at t = c it is k/(c alpha_s) with alpha_s about 2 kappa, kappa the precision of m in that mode. The
soft direction is x = w (both slices move together). What fails in the seed: the output is the true rate,
omega_min < 1.58/a < K_a. PASS (the statement is true and gives nothing).

**2.2 Compact U(1).** (a) On a fixed box the statement holds for every model with the trivial kbar = L/c^2 (|q~|^2 <= L/c^2).
All content is in the size of kbar. (b) Box-uniform kbar at beta 2.3 (Coulomb phase): cannot exist, by Lemma NEC, since
E_1 is about 2 pi/side (ARGUED; conditional on the chain POL-BR, HC; no gap RECALLED). (c) If one takes it to hold on one
box: the seed fails twice. The zero-field cap is 0.093 (2.0), a factor 8.7 below K_30. And the true rate is the photon's.
(d) OPEN, found here: I could not name the U(1) tilt that carries the growth NEC demands. Heuristic (spin wave, large
beta): a uniform tilt kappa gives Var about u^2 G/(1 + mu^2 G), with u the layer hopping expectation, G the soft transverse
propagator (about side/beta), and mu^2 proportional to u kappa/s: the same tilt that orders the links gives the photon a
layer mass, and the product stays bounded. A tree-pinning tilt gives link covariances equal to Wilson loops, which
decay by the perimeter law in every phase. NEC needs only k* >= 2 beta log(side/2 pi): a logarithm. Either a tilt
with logarithmic growth exists, or a step of the chain fails for U(1). This is a test of the chain, proposed below
as a GUIDE row. Verdict: PASS only in the sense of row 968 (nothing is proved for U(1)); the mechanism is not located.

**2.3 Frozen Q_8 and 2T.** Fixed box: trivial kbar. At beta 2.3, Q_8 is deep in its frozen (deconfined) phase and 2T is
near its transition (RECALLED, not verified). There E_1(B) is the splitting of the centre-flux sectors, of order
e^(-const side^2), so NEC demands k* of order side^2. Mechanism (ARGUED): take phi = kappa 1 on the links of one straight line
that winds around the box, zero elsewhere, z = the real direction on that line. The winding loop is near +1 or
near -1 times a fixed class; at the marginal kappa the law of the line sum is bimodal and Var is of order (side)^2/|z|^2 = side.
So the statement with a box-uniform kbar FAILS for Q_8. A proof for SU(2) must use an input that Q_8 lacks at beta 2.3:
disorder of winding loops (centre symmetry unbroken on the seed box). PASS.

**2.4 SMALL-BOX.** For SU(2) at beta 2.3 the box of side 4 is at the deconfinement point (N_t = 4 has beta_c about 2.30,
RECALLED). On sides <= 4 the winding-line tilt of 2.3 applies: torelon bimodality, variance growing with beta.
So no proof may be uniform in the side from below. A proof must contain a hypothesis that fails on side 4 and
holds on side 120: e.g. decay of Wilson lines over half the side. PASS (the statement is not claimed there).

**2.5 K7.** As row 968 4.5: with an adjoint term in V only, Section 3 holds, and at a coupling with no seed kbar grows
with the box. A proof must enter through a property of m that fails there. No approach below is group-blind in m. PASS.

**2.6 FT-FK.** An argument using only the middle layer e^(b<x,w>) and an arbitrary m must fail. Check: with m arbitrary
of the class, 2.3 gives growth. With V = 0 (product m): J_(b,phi) is a product over links and the bound is one link's
(at most 1/4-type values, all tilts). So every approach below is required to name its m-input. PASS as a rule for Step 3.

**2.7 Ceilings 2/3, 0.775, 1.0109.** They cap one-scale forms with a threshold (row 968 4.7, ported). POL-BR has no
threshold. They do not bind (TILT-COV-sup). The cap of 2.0 is a different thing: it bounds the output, not the hypothesis.

## Step 3. Approaches of my own (written before reading any route file or digest; 22:43Z)

Structure used below (all from the statement).
(S1) J_(b,phi) is the two-slice marginal of the four-dimensional Wilson measure with coupling b on one time-like layer and
     the source <phi, q~> on the two slices. So the statement is a link covariance bound for a 4D system with a defect layer.
(S2) Write phi_l = rho_l u_l, rho_l >= 0, u_l in S^3 = SU(2). Then <phi_l, x_l> = rho_l (1/2) tr(x_l u_l^(-1)): a time-like-plaquette
     coupling of the slice to a FROZEN slice u, with link-dependent coupling rho_l/s. rho_l = 0 is allowed, and so is rho_l -> infinity.
(S3) z = (alpha_l + zeta_l) u_l with alpha_l real, zeta_l in su(2). z is horizontal iff the field rho zeta is covariantly
     divergence-free in the background u. Where rho_l = 0 there is no condition on z_l. Where rho_l -> infinity, zeta_l is forced to 0
     up to O(1/rho), and the radial alpha_l is free but carries variance O(1/rho).
(S4) Gauge-Higgs form (exact). Z_b(g phi) = Z_b(phi). Averaging over the gauge group, Var_(J_(b,phi))(<z, q~>) = Var(O_z) in the
     model with a frozen-length site field g_v in SU(2) on the layer, hopping matrix rho_l u_l (u a background for the
     right-acting, custodial SU(2)), and O_z = sum_l (1/2) tr(g_s^(-1) q~_l g_t z_l^(-1)-type hopping observable). (E[O_z | g] is constant.)
(S5) At b = 0: J_(0,phi) = pi_(phi/s) x pi_(phi/s'), the one-step laws of the vacuum chain from the frozen slice u with couplings rho_l/s.

**Approach A (proof; regimes of rho in the gauge-Higgs form).** Split the links by rho_l: small (expand around Elitzur, Lemma Z),
large (unitary gauge, links pinned to u_l, polymer expansion of Osterwalder-Seiler / Fradkin-Shenker type in the layer),
middle (no expansion). Crux lemma A*: for every hopping profile rho and background u, the connected two-point function of
the hopping observables decays summably in the layer, uniformly in the side. m-input (FT-FK rule): spatial clustering of the
half-space vacuum, uniform in the layer condition. Fact tests: U(1), Q_8 fail A* through m (Coulomb, frozen). OPEN from the
start: A* contains a mass gap for the bulk at beta 2.3, and there is no convergent expansion there (strong coupling
parameter I_2/I_1 at 2.3 is about 0.48).

**Approach B (proof; the b = 0 end plus reflection positivity in b).** For lam = 1/2 the swap x <-> w is a reflection, and
e^(b<x,w>) is of positive type (characters with non-negative coefficients). So Cov(<z,x>, <z,w>) >= 0 and
(2/s^2) Var_x <= Var(<z, q~>) <= (4/s^2) Var_x. With (S5) the b = 0 end is: Hess Lambda(theta) <= kappa on horizontal vectors, for all
theta in R^N. Dual form: strong convexity of the rate function Lambda*, that is D(mu | pi_theta) >= |E_mu w - E_(pi_theta) w|^2/(2 kappa)
on horizontal differences, uniformly in theta. Crux lemma B*: a transport-type inequality for every one-step law pi_theta,
theta with arbitrary moduli. m-input: the same uniform clustering as in A*. This is the (COV)_kbar form of row 941 with
inhomogeneous couplings; I expect its ceilings to apply at single theta. OPEN.

**Approach C (proof; Lee-Yang form).** Var = d^2/dzeta^2 log Z_b(phi + zeta z). If Z_b(phi + i eta) != 0 whenever |eta_l| <= delta_0 for all l
(a zero-free polystrip around the real fields, uniform in the side), then Borel-Caratheodory on log Z gives
Var <= C |z|^2/delta_0^2 for z spread over many links (ARGUED; the bound uses |Z(phi + i eta)| <= Z(phi) and |E q~_l| <= 1/c per link).
Crux lemma C*: the zero-free polystrip. No Lee-Yang theorem is known for gauge fields; for O(4) spins it is known for the
single spin only. C* is "no phase transition in any real tilt", the same wall. OPEN.

**Approach D (counterexample; partial pinning that leaves an exact continuous symmetry).** By (S2)-(S3) the supremum over phi
contains all partial gauge fixings by pinning. Take
  phi^Lam: phi_l = Lam 1 on every link of directions 2 and 3, phi_l = 0 on every link of direction 1;   z = a(y) e on the direction-1 links of ONE plane x_1 = k.
z is horizontal for every Lam (phi vanishes where z lives). J_(b,phi^Lam) is invariant under gauge transformations that are
constant on each plane x_1 = k (conjugation keeps (1/2) tr x_l). So each family P_k(y) := x_(1)(k, y), y in a 2D torus of area
A = side^2, has the exact symmetry P -> g(k) P g(k+1)^(-1): an O(4) symmetry per plane. As Lam -> infinity the transverse links are
frozen at 1, every plaquette of the planes (1,2), (1,3) in the two slices becomes beta <P(y), P(y')>, and the plane carries a
two-dimensional O(4) sigma model (two layers, coupling b between them), dressed by the bulk. A 2D O(4) model at
stiffness rho_s has correlation length about 0.042 e^(pi rho_s)/(pi rho_s)^(1/2) (asymptotic freedom; RECALLED exact mass gap constant):
21 at rho_s = 2.3, 2 x 10^4 at rho_s = 4.6. The mean of P is zero by symmetry, so the whole coherent fluctuation is variance.
Expected: Var/(zero-field value) = structure factor of the sheet at zero momentum, of order min(A, xi_sheet^2): hundreds to
thousands on the side-120 box, and growing with the side up to xi_sheet. Fact tests of D: kinetic-only (V = 0): no plaquette,
no sheet coupling, product measure, no growth (correct). U(1): the same tilt gives a 2D XY sheet (growth; consistent with
NEC, and it may be the missing U(1) tilt of 2.2(d)). Strong coupling (beta below about 1): xi_sheet of order 1, no growth
(consistent: the statement should hold at strong coupling). The m-input is the explicit e^(-V): the magnetic term itself.

**Choice.** A, B, C each need, as a first step, that no tilt of type D has a long sheet correlation length. D is concrete,
its mechanism (weak-coupling sigma-model physics exposed by pinning the confining disorder away) is specific to
beta >= about 2, and it attacks the statement at beta 2.3 directly. So D is the best approach. Its CRUX lemma:
  (SHEET): for phi^Lam with Lam large, S(0) := (1/A) sum over y, y' of E<q~(k,y), q~(k,y')> grows with the side (at least to the
  seed side 120), or at least exceeds a fixed large multiple of E|q~_l|^2 = 4 k0.
Steps 4-6 attack (SHEET) by three routes.

## Step 4. Route 1 on (SHEET): the exact reduction (Lemma D1, PROVED by hand; checked by no one)

Setting: cubic periodic box of even side S >= 4, A := S^2, b in [0, beta], any s. phi^Lam as in Approach D (Lam on directions 2, 3; 0 on direction 1).
P_k(y) := x_l and P'_k(y) := w_l for the direction-1 link l from (k, y) to (k + 1, y); q~_k(y) = P_k(y)/s + P'_k(y)/s'.

**Lemma D1.** For every Lam >= 0:
(i) every z supported on direction-1 links is orthogonal to the gauge orbit of phi^Lam (phi^Lam vanishes there, so (xi phi^Lam)_l = 0 on those links).
(ii) J_(b,phi^Lam) is invariant under g_v = g(x_1(v)), acting on x and w at once. E q~_k(y) = 0.
(iii) E[q~_k(y) (x) q~_k'(y')] = 0 for k != k', and = (1/4) G(y, y') Id_4 for k = k', with G(y, y') := E<q~_k(y), q~_k(y')>.
(iv) For z = a(y) e on plane k (|e| = 1, sum a^2 = 1): Var_(J_(b,phi^Lam))(<z, q~>) = (1/4) sum over y, y' of a(y) a(y') G(y, y').
(v) As Lam -> infinity, J_(b,phi^Lam) converges weakly to the HARD-PINNED law: transverse links of both slices equal to 1, and the
    direction-1 links with density rho(x, w) = m-density(x) m-density(w) e^(b<x,w>) restricted to that set, with respect to Haar measure on them.
    So every admissible kbar_(s,t) is at least the hard-pinned value of (iv).
Proof. (ii) m(dx) m(dw) e^(b<x,w>) is invariant under every time-independent gauge transformation. A transverse link has both
ends in one plane, so it goes to g(k) x_l g(k)^(-1), and <1, g x g^(-1)> = (1/2) tr x = <1, x>: the tilt is invariant. g(k) = -1 on one plane flips
q~_k and q~_(k-1) only. (iii) k' not in {k - 1, k}: use g(k) = -1. k' = k - 1: use g(k + 1) = -1 (flips q~_k, q~_(k+1), not q~_(k-1); side >= 3).
k' = k + 1: use g(k) = -1. Same plane: q~_k(y) -> g(k) q~_k(y) g(k+1)^(-1) with independent g(k), g(k+1): the matrix commutes with SO(4), so it
is a multiple of Id_4; take the trace. (iv) from (iii). (v) The tilt weight is a product over transverse links of e^((Lam/s) x^0_l) e^((Lam/s') w^0_l),
a product measure that does not depend on the direction-1 links and tends weakly to the unit mass at 1; the density of
m (x) m e^(b<x,w>) is continuous and positive on the compact M x M. <z, q~> and its square are continuous. QED
Remark (generic points). At phi^Lam itself the gradient of a gauge-invariant function vanishes on direction-1 links
(stabiliser). As at phi = 0, this gives no relief: approach phi^Lam along eta with trivial stabiliser and with
sum over y of cos(p y) eta_k(y) = 0; then z_p below lies in the limit of the horizontal spaces, and Cov is continuous in phi.

At Lam = 0 this is Lemma Z (G(y, y') = 0 off the diagonal). The diagonal is G(y, y) = 1/s^2 + 1/s'^2 + 2 tau/(s s') for every Lam.
So Var/(its diagonal value) is exactly the zero-momentum structure factor of the sheet. D1 is an entry lemma. The crux is the size of G off the diagonal.

## Step 5. Route 2 on (SHEET): Gaussian domination on the pinned sheet (Theorem D2; PROVED by hand, checked by no one)

Tools ported, not rebuilt: reflection positivity of the Wilson action for planes that bisect links (Osterwalder-Seiler;
Froehlich-Israel-Lieb-Simon), and the Gaussian domination lemma of Froehlich-Simon-Spencer 1976 (FSS): for a weight
e^(A + theta B - sum_i (kappa_i/2)|C_i - theta C_i - h_i|^2) over an RP product measure, the integral is at most the geometric mean of the
two integrals with (A, A), (B, B) and h = 0. Both are textbook. They must be re-proved in the repo before use (rule on literature lemmas).

**5.1 Four-dimensional form of the hard-pinned law (PROVED).** m-density(x) = e^(-V(x)/2) Omega(x) = lambda_0^(-1) e^(-V(x)) integral of e^(beta<x,w>) m(dw).
T_0 has a continuous strictly positive kernel on a compact space, so lambda_0^(-n) T_0^n 1 -> <Omega, 1> Omega uniformly (Jentzsch). Hence the
hard-pinned law is the limit n -> infinity of the two-slice marginal of the slab measure mu_n: slices -n..0 and 1..n+1, weight
beta on every plaquette (beta/2 in the two end slices, b on the time-like layer 0-1), transverse links of slices 0, 1 equal to 1.
Time-like links may be restored as Haar variables everywhere except in the layer 0-1 (temporal gauge on an open interval
has trivial Jacobian). The gauge group of sites outside slices 0, 1 acts and leaves all weights invariant.

**5.2 Reflection structure (PROVED given the ported tools).** Let theta be the reflection in direction 2 through the pair of planes that
bisect the links between y_2 = j, j+1 and between y_2 = j + S/2, j + S/2 + 1 (S even). Crossing direction-2 links: in slices 0, 1 they are
pinned at 1; in the other slices fix them to 1 by gauge transformations at sites outside slices 0, 1. Then every plaquette
that straddles a plane is kappa <C, theta C> = kappa - (kappa/2)|C - theta C|^2, with C a link of direction 1, 3 or time on the left and theta C its mirror image
(kappa = beta, or beta/2 in an end slice). In slice 0 the straddling (1,2)-plaquettes are exactly beta <P_k(y), P_k(y + e_2)>. All other
terms are A + theta A. The pinning pattern, the layer coupling b and the end weights are theta-symmetric. Same in direction 3.
So mu_n has the FSS form for every bisecting plane of directions 2 and 3, with a product Haar reference measure.

**5.3 Gaussian domination and the infrared bound (PROVED given 5.2).** For h from the sheet sites y to R^4 put
  Z(h) := integral of exp( -(beta/2) sum over sheet bonds <y y'> of |P_k(y) - P_k(y') - h(y) + h(y')|^2 + all other terms unchanged ).
FSS: Z(h) <= Z(0) (reflect through the plane of a bond with non-zero gradient of a maximiser; only sheet bonds carry shifts,
all of them lie in directions 2, 3). The first-order term vanishes (E P = 0, D1). Second order with h(y) = e cos(p y), p != 0:
  G^e-hat(p) := sum over y of e^(i p y) E[<e, P_k(0)> <e, P_k(y)>] <= 1/(2 beta E(p)),   E(p) := 2 - cos p_2 - cos p_3.
This passes to n -> infinity, so it holds in the hard-pinned law, for every b in [0, beta].

**5.4 Sum rule and the lower bound (PROVED).** G^e-hat(p) >= 0. By D1(iii), (1/A) sum over p of G^e-hat(p) = E<e, P>^2 = 1/4. So for every set Low of momenta containing 0:
  max over Low of G^e-hat(p) >= [ A/4 - sum over p not in Low of 1/(2 beta E(p)) ] / |Low|.
With Low = {0}: G^e-hat(0) >= A (1/4 - G_S/beta), G_S := (1/A) sum over p != 0 of 1/(4 - 2 cos p_2 - 2 cos p_3) (about (1/2 pi) log S + 0.0488).

**5.5 From one slice to q~ (PROVED).** The hard-pinned density is symmetric under x <-> w, so the slice-1 function equals the
slice-0 one. e^(b<x,w>) is a kernel of positive type for b >= 0, so Cov(<z, x>, <z, w>) >= 0 for z on direction-1 links. Hence for the unit
vector z_p := (2/A)^(1/2) cos(p y) e on plane k (z_0 := A^(-1/2) e):
  Var(<z_p, q~>) >= G^e-hat(p) (1/s^2 + 1/s'^2) = 4 G^e-hat(p) k00_s.

**Theorem D2.** SU(2) Wilson (also Q_8, 2T: only Cov = Id/4 and irreducibility of g q h^(-1) are used), coupling beta, periodic box
of even side S >= 4. Every kbar that satisfies (TILT-COV-sup) obeys, for every s and every t in [0, c_s]:
  kbar_(s,t) >= lam_* k00_s,   lam_* := 4 max over Low of [ A/4 - sum over p not in Low of 1/(2 beta E(p)) ] / |Low|.
Numbers at beta 2.3. S = 4: G_4 = 103/384 exactly, lam_* >= 16 - 103/(6 beta) = 8.54 (PROVED, rational arithmetic). It is positive for beta > 103/96.
S = 8, 12, 16 (Low = {0}): lam_* >= 21.8, 32.8, 37.9. S = 120, Low = {|n_2|, |n_3| <= 4} (81 modes): lam_* >= 27.1. These four use
the lattice sums G_8 = 0.37929, G_12 = 0.44405, G_16 = 0.48992, G_120 = 0.81072 and the low-mode sum, evaluated in a few lines of
floating arithmetic and by hand with S_4 = 12.7476 (26.9). They are ARGUED until the sums are bounded by hand; no proof weight is put on the run.
The structure factor of the sheet in the uniform mode is at least 9.5 on side 16 against the Elitzur value 1/4.

**5.6 Fact tests of D2.** Kinetic-only (V = 0): the sheet coupling is 0, the bound is void (correct, FT-FK). Compact U(1): two
components, G-hat(0) >= A (1/2 - G_S/beta): at beta 2.3 this is positive up to side about 1000 and equals 2124 on side 120, 4248 times the
Elitzur value: the variance grows like the area. This is the U(1) tilt that 2.2(d) could not name, and it satisfies NEC.
Q_8, 2T: the bound is the same as for SU(2). So D2 does not separate SU(2) from the rivals: it is a lower bound that
holds for all of them, which is the right shape for a negative result. SMALL-BOX: holds on side 4. K7 (adjoint term in V
only, coefficient >= 0): the adjoint plaquette is 3 - (1/2)|Ad_P - theta Ad_P|^2, also of FSS form; the bound holds with the fundamental
coupling in place of beta. Strong coupling: void below beta = 4 G_S (1.07 on side 4), as it should be.

## Step 6. Consequences of D2, route 3 (growth with the side), and what stays open

**6.1 Corollary CAP (PROVED given D2 and Theorem POL-BR's formula; arithmetic as in 2.0).** With kbar_(s,u) >= lam_* k00_s for all u:
  alpha_s^thm <= lam_* (beta^2/2) r (r + 2)/(e^(lam_* beta r/2) - 1) <= 4 lam_* beta^2/(e^(lam_* beta) - 1),     alpha^thm <= 2 lam_* beta/(e^(lam_* beta) - 1).
At beta 2.3: side 4 (lam_* = 8.54, PROVED): alpha^thm <= 1.2 x 10^(-7). Side 120 (lam_* = 27.1, ARGUED arithmetic): alpha^thm <= 1.7 x 10^(-25).
The seed needs alpha >= K_30 = 0.811. K_a <= 1.2 x 10^(-7) needs a above 5 x 10^8.
Verdict on the row's goal. (TILT-COV-sup) holds on the seed box only with kbar >= 27 k00 at every slice and every flow time.
So it cannot deliver (LSI-br-seed)_30 through Theorem POL-BR: the gap is 24 orders of magnitude. This is a counterexample to
the statement in the form the seed needs (a kbar small enough for K_30), by the explicit family phi^Lam, z_p. It is not a
counterexample to the existence of some finite box-uniform kbar.

**6.2 Route 3: does the pinned-sheet variance grow with the side beyond the infrared range? (OPEN; ARGUED both ways.)**
(a) One slice, uniform mode: the bound A(1/4 - G_S/beta) grows up to S about 16 and is void from S = 28 (beta < 4 G_S). The low-mode form gives the
    constant 27 for all larger S, not growth.
(b) Two slices, common shift h_0 = h_1: the same lemma gives, for Q = P + P', Q-hat(0) >= A[(1 + tau)/2 - 2 G_S/beta], tau := E<P(y), P'(y)> >= 0 (tau' = Var >= 0).
    If tau >= 0.8 at b = beta, growth like A is proved up to S about 490. A lower bound on tau failed here: convexity in b and the
    positive-type expansion give only tau >= 0, because the bulk time-like plaquette (strength beta, unknown sign of its
    effective coupling) is as strong as one sheet bond. OPEN.
(c) Physics (ARGUED): the sheet is a 2D O(4) model with exact symmetry and stiffness between beta (b = 0) and about 2 beta (b = beta), plus a
    bulk dressing. Asymptotic freedom gives a FINITE sheet correlation length, about 21 at stiffness 2.3 and 2 x 10^4 at 4.6. So for
    SU(2) the sheet variance saturates at about xi_sheet^2: a finite, box-uniform kbar may exist, of order 10^3 to 10^8 k00. For U(1)
    the sheet is an XY model in its Kosterlitz-Thouless phase and the variance grows as a power of the side without bound.
    This is a real SU(2)/U(1) difference inside the criterion, and it is useless for the seed by 6.1.
Three routes on (SHEET): route 1 gave the exact reduction; route 2 proved the quantitative form (lam_* >= 8.5 to 38);
route 3 did not decide growth beyond side 27.

**6.3 What a repair must avoid (direction).** The tilts phi^Lam are far from typical for the flow: under nu_t they need the Gaussian
noise to push two thirds of the links to Lam >> 1, probability e^(-const L Lam^2/c). So the failure is a failure of the SUPREMUM
over phi, not of the flow. Every criterion with a supremum over R^N (or over a dense open set, see the remark in Step 4)
inherits D2. An averaged criterion must give partial-pinning tilts no weight: it cannot contain sup_phi of the
horizontal covariance, nor an exponential moment of it that is dominated by such tilts.

**6.4 Proposed Mac mini rows (GUIDE; criteria fixed here, before any run; I ran nothing beyond the lattice sums above).**
- Row P1 `gap-pinsheet-guide`: SU(2) Wilson, beta 2.3, lattices S^3 x T with S = 8, 12, 16, 24 and T >= 2S, two adjacent time slices with
  all spatial links of directions 2, 3 frozen at 1 and the time-like links between them frozen at 1 (this is J_(beta,phi^infinity)).
  Observables per plane k and slice: M = sum over y of P_k(y); R_S := E|M|^2/A (equals 4 G^e-hat(0)); tau; second-moment correlation length.
  C1 (test of Theorem D2): R_8 >= 21.8, R_12 >= 32.8, R_16 >= 37.9. If any is violated by more than 3 standard errors, D2 is
  wrong and this row's result is withdrawn. C2 (growth): "sheet longer than the box" if R_24 >= 0.25 x 576 = 144. C3: report tau; if tau >= 0.8, 6.2(b) applies.
- Row P2 `gap-pinsheet-u1`: the same for compact U(1) at beta 2.3 with sides 8 to 32. Criterion: R_S/A does not fall by more than
  a factor 2 from side 8 to side 32 (power-law order). This tests the U(1) reading of 5.6.
One worker, BLAS = 1, as the machine rules require.

## Step 7. Reading after the attack (22:54Z to 22:57Z): `prior/gap-lit-tiltcov.md` (row 971; grep for the key terms, Steps 3b and 5 and
the table read), RESULT texts of FINISH rows 968, 970, 974, 975 (rows 969, 972, 973, 976 have no RESULT text yet), and, because they
bear on Approach D, `gap-direction2-max.md` lines 181-232 and 299-343 and `gap-tiesearch-opus.md` lines 44-60, 232-249, 296-301.

**7.1 What "lambda about 2.4 to 2.9" is.** Row 973's lambda is E[X_a^2], the variance of the named tie mode of the one-step law at
seven frozen slices (u_xy and twists), sides 8 to 16, t = 0 only. By Lemma SUB of row 970 (PROVED there) it gives
kbar_(s,0) >= 4 beta^2 lambda, about 51 to 61 at the mid-slice at beta 2.3 (zero-field value 2 beta^2 = 10.6): a factor 5, GUIDE, at t = 0 only.
Theorem D2 gives, by proof and at EVERY t: kbar_(s,t) >= lam_* k00_s, at the mid-slice 2 beta^2 lam_* = 287 on side 120 and 401 on side 16.
Row 970 3.5 notes "a spike at one t costs nothing". D2 is not a spike: it enters the integral over t in full (6.1).

**7.2 Per approach: already there, or in the literature?**
- 2.0 ZERO-CEIL. In substance already in row 968, 3.4 (zero-field output 0.04 with tau = 1, "a about 830"). New here only: the
  rigorous side (tau >= 0, so the cap 0.513 is a theorem for every admissible kbar) and the remark that K_30 is out of reach.
  Row 968's RESULT says "the seed for some a", so the lane did not claim a = 30; the a = 30 in this row's brief is the size named by row 974.
- Approach A (regimes in the gauge-Higgs form). Literature: Osterwalder-Seiler / Fradkin-Shenker regions and Shen-Zhu-Zhu,
  all strong coupling or uniform tilt (row 971, Steps 2a, 2c). The crux A* is (LOC-COV) of rows 968 and 970 (their open item).
  Row 971 item 5: no source treats a tilted layer in a confining bulk or non-pure-gauge tilts. Not new as a route; the
  custodial-background form (S4) I did not find in the files read.
- Approach B (b = 0 end, reflection positivity in b, dual transport form). Already there: Lemma SUB (row 970, lower bound at
  t = 0), (COV)_kbar of row 941, and row 971 Step 3b (semi-log-concavity; Anari-Koehler-Vuong reduce b < 0.587/rho_m to one slice).
  The two-sided bound at lam = 1/2 by positive type of e^(b<x,w>) is elementary; I did not find it stated. No progress on B*.
- Approach C (Lee-Yang zero-free polystrip). Not in the files read. No Lee-Yang theorem for gauge fields is known to me. No progress.
- Approach D. The tilt family IS already there: row 970, working note (N4): "A tilt that freezes the x- and y-links leaves a
  layered O(4) model of z-links at coupling at least beta: its susceptibility bounds kbar from below at every beta,
  box-uniformly but hugely", left as "an ARGUED remark with no number" because "the factor Omega couples the layers and I
  have no control of it". New here: (i) Lemma D1, the exact plane-wise O(4) symmetry, which removes the coupling between
  layers at second moment for every Lam and every Omega; (ii) Theorem D2, the control of Omega through its four-dimensional
  form and Gaussian domination, with numbers (8.54 proved on side 4; 21.8 to 37.9 on sides 8 to 16; 27.1 on side 120) and at
  every flow time; (iii) Corollary CAP. Literature: the tools are Froehlich-Simon-Spencer 1976 and
  Froehlich-Israel-Lieb-Simon 1978 (reflection positivity for gauge models); row 971's digest has no infrared-bound or
  Gaussian-domination entry (grep: no hit), and its Leake-Li "pinnings" are two-site spectral-independence pinnings, a different thing.

**7.3 Limit of D2 against row 970's quotient form (important).** Theorem QUOT (row 970, 5.2) weakens the hypothesis to
(TILT-COV-quot): 2 Var - Q_phi(z) <= 2 kbar |z|^2, for z that also obey X z = 0 whenever X phi = 0. At phi^Lam the stabiliser is the
plane-wise group, and that side condition forces z = 0 on direction-1 links; near phi^Lam the gain Q is unbounded in the
directions of the broken stabiliser. The uniform mode of D2 is a rigid frame mode of exactly the kind that Proposition
ROTOR says QUOT removes. So D2 refutes the usefulness of the PLAIN supremum form (the target of this row) and does NOT
by itself touch (TILT-COV-quot). What would touch it (ARGUED, spin-wave level, not proved): phi^Lam plus a weak uniform
field h on the direction-1 links, and z a transverse wave of momentum p != 0. Then Var is about m^2/(rho_s p^2 + h) and
Q is about const/(h^2 s^2 A); with h of order A^(-1/2) the difference 2 Var - Q is of order the side. A proof needs a
lower bound on a Goldstone-wave variance; the Bogoliubov route fails here because the twist costs a time-like
plaquette per site that is not suppressed by p^2 (the bulk is not twisted with the sheet). OPEN.

## Step 8. State, marks, next step (written 23:00Z; wall time used about 40 minutes of 75)

**8.1 Marks.**
| Item | Where | Mark |
|---|---|---|
| ZERO-CEIL: every admissible kbar >= k00_s; POL-BR output <= 2 beta/(e^beta - 1) = 0.513 < K_30 = 0.811 at beta 2.3 | 2.0 | PROVED (hand; given Lemma Z of row 968) |
| The finer cap 0.234 (a >= 117) | 2.0 | ARGUED (trapezoid arithmetic) |
| Lemma D1: plane-wise O(4) symmetry of phi^Lam; Var = (1/4) sum a a' G; hard-pinning limit | Step 4 | PROVED (hand) |
| Theorem D2: kbar_(s,t) >= lam_* k00_s for every s, t; infrared bound on the pinned sheet | Step 5 | PROVED (hand), given two ported textbook lemmas (RP of the Wilson action for bisecting planes; FSS Gaussian domination), not rebuilt here |
| lam_* >= 8.54 on side 4, beta 2.3 | 5.5 | PROVED (rational arithmetic) |
| lam_* >= 21.8, 32.8, 37.9 (sides 8, 12, 16) and >= 27.1 (side 120) | 5.5 | ARGUED (lattice sums by floating arithmetic; to be bounded by hand) |
| Corollary CAP: POL-BR output <= 1.2e-7 (side 4), <= 1.7e-25 (side 120) | 6.1 | PROVED / ARGUED as the lam_* it uses |
| U(1): the same tilt gives area growth of the variance up to side about 1000 at beta 2.3 | 5.6 | PROVED given the same lemmas (N = 2); numbers ARGUED as above |
| K7 form of D2 | 5.6 | ARGUED |
| Growth of the SU(2) pinned-sheet variance beyond side 27; existence of ANY finite box-uniform kbar at beta 2.3 | 6.2 | OPEN (ARGUED: saturates near xi_sheet^2 for SU(2); unbounded for U(1)) |
| (TILT-COV-quot) of row 970 against the D family | 7.3 | OPEN (ARGUED to fail like the side; no proof) |
| A proof of (TILT-COV-sup) with a kbar usable for a seed | - | REFUTED as a goal by 2.0 (a = 30) and by D2 with CAP (every even box); not attempted further |

**8.2 Answer to the row.** The crux lemma was attacked on the counterexample side and the stop condition "a counterexample" is met
in the quantitative sense. For SU(2) Wilson at beta 2.3: (a) on the a = 30 box no admissible kbar reaches K_30, by the zero field
alone; (b) on every even box, the family phi^Lam (pin directions 2, 3; leave direction 1 free), z a low Fourier mode on one
plane, forces kbar >= lam_* k00 at every slice and flow time, with lam_* >= 8.5 (proved on side 4) and about 27 on the seed
box; Theorem POL-BR then returns at most 1.7e-25 on the seed box. So (TILT-COV-sup) is true only with a kbar that is
useless for the seed. Whether a finite box-uniform kbar exists at all at beta 2.3 is left open.
What this does not say: nothing about the true log-Sobolev constant of nu_s, and nothing about typical tilts. The tilts
used have probability e^(-const L Lam^2) under the flow. The quotient form of row 970 is not reached (7.3).

**8.3 Next step (one decision for the lead).**
1. One independent line-by-line check of Step 5 (5.2 is the place to attack: the reflection structure with two pinned
   slices and gauge-fixed crossing links; then the FSS lemma with shifts on sheet bonds only). If it holds: record that
   proofs of the plain (TILT-COV-sup) are not to be queued at any beta above 4 G_S (1.07 on side 4), which extends
   row 970's note for 2.5-2.6 down through 2.3.
2. Row P1 (6.4) as a test of D2 (criterion C1), and C2/C3 for growth. Row P2 for U(1). Both are small runs.
3. For the quotient form: a discrete-tie variant of D. Pin the transverse links of each plane to a twist-eater
   configuration (holonomies i sigma_1, i sigma_3), so that the continuous stabiliser is trivial (no gain Q, no side condition)
   while the centre flip P -> -P stays exact. Expected: a two-fold tie of an ordered sheet, variance like the area up to
   xi_sheet, which Proposition TIE of row 970 turns into a^2 for the supremum form and a^2/4 for (ABS-flow). Not proved;
   reflection positivity is not obvious with the twist. First a GUIDE row with the criterion of row 973.
4. Proof effort goes to forms that weigh tilts by the flow ((LSI-traj-seed)_a of row 970), with Lemma META of row 975 as
   the known price: the discarded tilts need a transience input. D2 gives a concrete family to test such an input on.

**8.4 Files.** Read only: `library/gap-avgcurv-max.md` (44-77, 124-255), `library/gap-trajtest-opus.md` (28-56, 258-276),
`library/prior/gap-lit-tiltcov.md` (grep, 307-360), `library/gap-direction2-max.md` (181-232, 299-343), `library/gap-tiesearch-opus.md`
(44-60, 232-249, 296-301), FINISH.md rows 967-977. Written: this file only. No git, no web, no numeric job; one few-line
arithmetic evaluation of the lattice sums G_S and of the low-mode bound (not a proof step). Checked by no one.

## Step 9. Amendment to 8.3 item 3: a simpler family against the quotient form, reduced to ONE number (written after Step 8)

**9.1 Family D'' (one free plane).** phi'': phi_l = Lam 1 on every spatial link EXCEPT the direction-1 links of one plane k, where phi_l = 0.
z = a(y) 1 on those free links (the trace direction; sum a^2 = 1). Facts (PROVED by hand unless marked):
(a) The stabiliser of phi'' is the group of constant gauge transformations (the pinned-link graph is connected). X z = a(y)[xi, 1] = 0
    for its generators. z is orthogonal to the orbit. So z is admissible for (TILT-COV-quot) of row 970 at phi'' itself.
(b) Gain: Q_(phi'')(z) = (3/Lam^2) sum over y of a(y)^2 R_eff(y), R_eff(y) the effective resistance between the two ends of the free link in
    the graph of pinned links; R_eff <= S - 1 (go round direction 1). So Q <= 3(S - 1)/Lam^2 -> 0 as Lam -> infinity. The quotient form gains nothing.
(c) Symmetry left: constant conjugations and the centre flip of plane k. E P = 0. E[P (x) P] is diag(q_0, q_v, q_v, q_v) in the basis
    (1, i sigma), q_0 + 3 q_v = 1, q_0 := E[((1/2) tr P_k(y))^2] = (1 + E chi_adj(P_k(y)))/4. The O(4) symmetry of D is gone, so q_0 is not 1/4 by symmetry.
(d) The pinning pattern is reflection symmetric in directions 2, 3 and the transverse links of slices 0, 1 are 1, so 5.1-5.3
    apply word for word, direction e = 1: G^0-hat(p) <= 1/(2 beta E(p)) for p != 0. Sum rule: (1/A) sum over p of G^0-hat(p) = q_0. Hence
      G^0-hat(0) >= A (q_0 - G_S/beta),   and   max over Low of G^0-hat >= [A q_0 - sum over p not in Low of 1/(2 beta E(p))]/|Low|.
(e) 5.5 applies (swap symmetry at hard pinning; positive type). So with Lam -> infinity:
      (TILT-COV-quot) forces kbar_(s,t) >= 4 max_p G^0-hat(p) k00_s for every s and t.
**Proposition QUOT-CAP (PROVED given D2's two ported lemmas; CONDITIONAL on the value of q_0).** If q_0 >= 0.24 in the hard-pinned law of D'':
kbar of the quotient form is at least 19 k00 (side 8), 28 k00 (side 16), 19.8 k00 (side 120, 81 low modes), at beta 2.3, at every s, t;
Theorem QUOT then returns at most 2 x 19.8 beta/(e^(19.8 beta) - 1) = 1.5 x 10^(-18) on the seed box. (Arithmetic as in 5.5, ARGUED until bounded by hand.)
The threshold is q_0 > G_S/beta: 0.117 (side 4), 0.165 (side 8), 0.213 (side 16).
**The one number.** q_0 is the second moment of the trace of ONE free link. Proved here: q_0 >= A_4(kappa)/kappa at kappa = 6 beta, about 0.064
(a von Mises-Fisher link in a field of size at most 6 beta has transverse variance at least that). This is below the
threshold. ARGUED: q_0 = 1/4 up to winding effects of order A e^(-m S), because a uniform frame G of the sheet is a flat
connection with holonomy G round direction 1, locally gauge-equivalent to the trivial one, and the layer and the bulk
are massive. The tie here is between gauge-inequivalent states (the class of the winding holonomy), nearly
degenerate, and joined by no exact symmetry: so no orbit direction, no gain. OPEN at proof level.

**9.2 Row P3 (replaces item 3 of 8.3; GUIDE; criteria fixed now).** `gap-pinsheet-quot`: the lattice of row P1 but with ALL spatial links
of the two slices frozen at 1 except the direction-1 links of one plane. Measure q_0 (one-link second moment of (1/2) tr P), and
R^0_S := E[(sum over y of (1/2) tr P(y))^2]/A on sides 8, 12, 16. C1 (test of 9.1(d)): R^0_S >= A (q_0 - G_S/beta) with the measured q_0, within 3
standard errors; else 9.1 is wrong and is withdrawn. C2: "QUOT-CAP applies" if q_0 - 2 errors >= 0.22 on sides 8 to 16.
C3 (growth, rule of row 973 Section 2): REFUTED (GUIDE) for a box-uniform (TILT-COV-quot) at beta 2.3 if g - 2 sigma_g > 1.25 on 8 -> 16
with no decreasing step. Expected by the sigma-model reading: R^0 about m^2 A/4 with growth factor near (L + 2)^2/L^2 per step.

## Step 10. Hardening of the arithmetic (by hand), and the end state

**10.1 Side 8 by hand (upgrades lam_* >= 21.78 on side 8 to PROVED arithmetic).** On the 8 x 8 torus 2 - 2 cos takes the values
0, 2 - 2^(1/2), 2, 2 + 2^(1/2), 4 with multiplicities 1, 2, 2, 2, 1. The sum over (a, b) != (0, 0) of m_a m_b/(d_a + d_b) is
6.828427 + 2 + 1.171573 + 0.5 + 3.414214 + 3.093836 + 2 + 0.872258 + 1 + 1.477592 + 0.666667 + 0.585786 + 0.539504 + 0.125 = 24.274857.
So G_8 = 0.379295 and lam_* >= 4 x 64 x (1/4 - G_8/2.3) = 21.78. Side 8 at beta 2.3 is above the deconfinement length (N_t = 4 has beta_c about
2.30, N_t = 8 about 2.51, RECALLED), so this is not a SMALL-BOX artefact. CAP on side 8: at most 2 lam_* beta/(e^(lam_* beta) - 1) = 1.8 x 10^(-20).

**10.2 Route to a hand bound of G_S for S = 120 (Lean-formalizable; not carried out).** Summing over one momentum in closed form:
  G_S = (S^2 - 1)/(12 S^2) + (1/S) sum over a = 1..S-1 of coth(S alpha_a/2)/(mu_a^2 - 4)^(1/2),   mu_a := 4 - 2 cos(2 pi a/S), alpha_a := arccosh(mu_a/2).
(Uses (1/S) sum_b 1/(mu - 2 cos(2 pi b/S)) = coth(S arccosh(mu/2)/2)/(mu^2 - 4)^(1/2) and sum over b = 1..S-1 of 1/(4 sin^2(pi b/S)) = (S^2 - 1)/12.)
Check at S = 4: 0.078125 + (2 x 0.291666 + 0.177080)/4 = 0.268228 = 103/384. The terms are monotone in a on [1, S/2], so the sum of 119
terms is bounded by an integral; with the low-mode sum S_4 = 12.7476 (rational, by hand) this would turn 27.1 into a PROVED number.

**10.3 Correction.** In 9.1 the side-120 value with q_0 = 0.24 is 19.9 (not 19.8): [3456 - 3052]/81 = 4.99, times 4.

**10.4 End state.** Stop condition met: a counterexample to the statement in the form the seed needs (Sections 2.0, 5, 6.1).
Three routes on the growth form of (SHEET) are recorded (Step 4, Step 5, 6.2). The next step is 8.3 with 9.2 in place of its item 3.
**10.5 In the units of the lane's GUIDE tables (per-link covariance, zero-field value 1/4).** D2 gives G^e-hat(0) >= 5.44, 8.20, 9.47 on
sides 8, 12, 16 at beta 2.3 (side 8 PROVED arithmetic, the others ARGUED arithmetic). Row 968's runs found 0.275, 0.300, 0.309 for the uniform
tilt on the same sides; rows 970 and 973 found tie-mode variances 2.4 to 2.9 at frozen slices (their own normalisation, t = 0).
Those runs searched uniform tilts and frozen slices u in M (all moduli equal); the family phi^Lam has moduli 0 and infinity and lies outside both.

End time (date -u): Sat Nov 14 23:05:07 UTC 2026 (start 22:21:54Z; about 43 minutes of wall time; stopped on the stop condition, not on the clock).

RESULT: no proof of (TILT-COV-sup) at beta 2.3; instead a counterexample to it in the form the seed needs. PROVED by hand (checked by no one): ZERO-CEIL (every admissible kbar >= k00_s, so Theorem POL-BR returns at most 2 beta/(e^beta - 1) = 0.513 < K_30 = 0.811 on the a = 30 box); Lemma D1 and Theorem D2 (given two ported textbook lemmas, reflection positivity for bisecting planes and Froehlich-Simon-Spencer Gaussian domination, not rebuilt): the tilt that pins the links of directions 2, 3 and leaves direction 1 free (row 970's undeveloped note N4) leaves exactly O(4)-symmetric sheets whose infrared bound forces kbar_(s,t) >= lam_* k00_s at every slice and every flow time on every even box, lam_* >= 8.54 (side 4) and 21.78 (side 8) PROVED, 37.9 (side 16) and 27.1 (seed side 120) ARGUED arithmetic, so POL-BR returns at most 1.7e-25 on the seed box; the same tilt gives compact U(1) area growth up to side about 1000 (the tilt Lemma NEC asks for). CONDITIONAL (Proposition QUOT-CAP): row 970's quotient form fails the same way if the one-link number q_0 >= 0.24 (proved only q_0 >= 0.064). ARGUED: the SU(2) sheet variance saturates near xi_sheet^2, so a finite but useless box-uniform kbar may exist. OPEN: existence of any finite box-uniform kbar at 2.3, q_0, growth beyond side 27. Next: one line-by-line check of Step 5.2, then Mini rows P1-P3 (criteria in 6.4, 9.2).
