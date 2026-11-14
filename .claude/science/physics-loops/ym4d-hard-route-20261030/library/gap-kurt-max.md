# FINISH row 886, gap-kurt-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Author: Claude Fable 5.2 (max effort). Date: 2026-11-13.
Clone: /Users/jonreilly/ym4d-lead/clone at commit c71f9498b5e32bae683db3ca593d7786a623f9be (read-only).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Labels: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE, OPEN.

## 0. Target

(KURT), from D/library/gap-brainstorm2-max.md (row 876, unchecked). At the seed
size, uniformly in the cutoff, each heavy flux sector's top eigenfunction g of
the ground-state-transformed transfer operator has fourth moment
kappa = integral g^4 dmu >= 1 + c_0. Equivalent reading: the chi-square
distance between the flux state g^2 dmu and the vacuum mu is at least c_0.
Task: prove (KURT) or its strongest form with explicit constants, or show it
fails at order one. Exact statement to be copied from row 876 in step 1.

## Plan (one step per response; each step is appended before the next)

1. Read row 876 (KURT, Lemma SQ, Theorem SQ, Theorem SQ-F, the window
   statement, the three failed attempts) and the consumer FUSE-suff
   (gap-es1-opus.md lines 200-236). Record exact statements.
2. Read the fact-test rows (786, 838, 839, 843, 845) and (SEED-FP) only as far
   as needed. Record what each says in one line.
3. Decide whether (KURT) can hold. Exact identities for kappa. When is a flux
   ground state chi-square close to the vacuum? Solvable cases: U(1) Villain
   or Gaussian, Z_2, strong coupling, 2D twin.
4. Attack A: spectral or gap route. kappa - 1 = ||g^2 - 1||^2. Relate it to
   the sector gap by a variational or commutator identity.
5. Attack B: hypercontractivity or log-Sobolev for the transfer operator;
   reverse direction (lower bounds on the fourth moment from eigenvalue
   decay).
6. Attack C: structure of g as a twisted ground state; reflection positivity
   across the flux; center symmetry characters; nodal set.
7. Run the fact tests on whatever survives: U(1) Coulomb, Z_2 at beta 5/2,
   frozen 2T, Q_8. Optional GUIDE numerics on a small model.
8. Assemble: strongest statement proved, explicit constants, what stays OPEN,
   RESULT line.

## Step 1. What row 876 states (READ D/library/gap-brainstorm2-max.md L387-422, L486-500; D/library/gap-es1-opus.md L200-236)

Setting (READ L389-391). X = SU(2)^E, Haar dU. L is self-adjoint with a
continuous, symmetric, strictly positive kernel. Omega > 0 is its top
eigenfunction, eigenvalue lambda_0. mu = Omega^2 dU. P f = (lambda_0 Omega)^(-1)
L(Omega f). P is Markov and self-adjoint on L^2(mu). A finite group Gamma of
flips commutes with L. Sectors = characters chi of Gamma, values +-1.

Lemma SQ (READ L393-394). P g = theta g, Int g^2 dmu = 1, kappa = Int g^4 dmu.
Then <g^2, P^t g^2> >= theta^(2t) kappa. (Jensen: (P^t g)^2 <= P^t g^2.)

Theorem SQ (READ L396-400). For chi != 0, g = Psi_chi/Omega, theta =
lambda_chi/lambda_0, rho = lambda_1^+/lambda_0 (second even eigenvalue):
  theta^(2t) <= 1/kappa + (1 - 1/kappa) rho^t.                         (SQ)
t = 1: 1 - theta^2 >= (1 - 1/kappa)(1 - rho).

Window (READ L406). If theta^2 > rho then kappa <= (1 - rho)/(theta^2 - rho).

Theorem SQ-F (READ L490-493). gamma_chi = (kappa_chi - 1)/(8 kappa_chi):
  p_chi(a; B) <= (1 + S_ev(a/2; B)) max(S_ev(a; B)^gamma_chi, e^(-gamma_chi a)).

(KURT) (READ L359, L413, L422, L496). At the seed size, every crossed flux
sector either is light (top eigenvalue within the consumer's tolerance of
lambda_0) or has kappa >= 1 + c_0, c_0 independent of the cutoff. In lane
notation: Var_pi(psi_chi^2) >= c_0 for the heavy electric sectors.

Consumer (READ gap-es1-opus.md L204-221). (FUSE_K): a set L of four light
sectors; (F-h) p_z <= K S^(1/2) for z not in L; (F-l) s_z <= K S for z in L;
S = S_ev(a; box). By Remark 6.1 (per row 876 L496) any positive exponent
serves in (F-h).

Row 876's three failed attempts (READ L418-421). (a) Chapman-Robbins with a
sum of plaquettes: order 1/a only. (b) Half-box conditioning: needs (HC).
(c) Dynamics: no even observable that sees the sign flips, other than g^2.

Row 876's rival values (READ L410, ARGUED or GUIDE there). U(1) Coulomb:
kappa = 3/2 for a pure cosine. Z_2 ordered, frozen Q_8, 2T: kappa -> 1.
2D Ising ring of 8: kappa 2.48, 2.14 (K = 0.2, 0.3); 1.18 (K_c); 1.0015,
1.0000 (K = 0.6, 0.8).

First remark of mine (PROVED, one line). (SQ) at t = 1 rearranges to
  kappa - 1 >= (theta^2 - rho)_+ ... no: it gives an UPPER bound on kappa
  when theta^2 > rho and no bound otherwise. So (SQ) never gives a lower
  bound on kappa. A lower bound needs another idea.

## Step 2. Fact tests and the real object (READ, summaries only)

All READ from D/library/gap-brainstorm2-max.md L40-47, L88-137 (row 876's
status digest; I did not re-open the primary rows).

- Row 786 (FINISH.md L863): the Villain U(1) twist theorem. U(1) in its
  Coulomb phase has no gap and light flux sectors. An argument for a heavy
  flux must fail there.
- Row 838: frozen Q_8 (about beta 1.15) and 2T (about 2.15) bind at order
  one. Haar moments of Q_8, 2T first differ from SU(2) at degrees 4, 6.
- Row 839 (checked 849): every background-uniform one-layer twist bound is
  false above 4 G_3 = 1.0109 (flat background, Frohlich-Simon-Spencer).
- Row 843 (checked 854): commutator contraction and the W_a area bound hold
  verbatim for Q_8 and 2T. The spin-5/2 filter is SU(2)-specific.
- Row 845 (checked 852): the annealed condition (AN1) is a worst-case
  exterior bound in disguise.
- Caps: single-site Dobrushin 2/3; vertex blocks 0.775.
- (SEED-FP) (READ digest L91; source gap-finishline-opus.md L114-118): the
  thermal sum of the bare Wilson transfer operator of the periodic cube of
  physical side ell at physical time ell/2 is below s_* < 1/5041, for every
  first-passage datum (K, beta), K >= K_0. One size, all large cutoffs.
- Objects (READ digest L100-106): p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr L_m^a,
  the weight of the odd electric sector at time period a. (FQ): 8 Q_F <=
  K(a) sqrt(S_ev(a)), Q_F < 1/192.

What (KURT) must respect (my reading, ARGUED).
(T-U1) In U(1) Coulomb the flux sectors are light, so (KURT) as stated
  (light OR kappa >= 1 + c_0) is not contradicted by U(1), whatever kappa is.
  Row 876 has kappa = 3/2 for a pure cosine there. So a proof of
  "kappa >= 1 + c_0" alone need not fail for U(1). What must fail for U(1)
  is the conclusion "heavy flux", and (KURT) plus (SQ) gives E >= c (1 -
  e^(-m)), which is empty when m is small. Consistent.
(T-Z2) In Z_2 at beta 5/2 (ordered, deconfined), frozen Q_8, 2T: kappa -> 1
  and the flux is light. Again (KURT)'s first alternative holds. So the
  dangerous case is not a rival's own phase. It is a sector that is neither
  light nor has kappa away from 1: the window.

## Step 3. Decision: when can (KURT) hold? (working notes; proofs follow in Steps 4-6)

Notation. P Markov, self-adjoint on L^2(mu). g odd, P g = theta g, Int g^2 = 1.
kappa = Int g^4. h = g^2 - 1 (even, orthogonal to 1, ||h||^2 = kappa - 1).
rho = top of P on even functions orthogonal to 1. E = -log theta, m = -log rho.

3.1 Every general tool bounds kappa from ABOVE (PROVED below, Step 4).
Jensen ((P g)^2 <= P g^2), hypercontractivity (||P^t f||_4 <= ||f||_2 gives
kappa <= theta^(-4t)), log-Sobolev (bounds Ent(g^2) <= kappa - 1 from above):
all say "the flux state cannot be too far from the vacuum". (KURT) is a lower
bound. It says "the flux state is not a sign function". No inequality of the
Jensen or hypercontractive kind can give it. Reason: an autonomous Z_2 bit
(product chain, 3.3) satisfies all of them with kappa = 1.

3.2 When MUST kappa be close to 1? (READ row 876 L406, the window; PROVED
there.) If theta^2 > rho then kappa - 1 <= (1 - theta^2)/(theta^2 - rho).
In words: a flux much lighter than the even gap (2E << m) forces a
sign-like ground state. So (KURT) for a sector implies
  1 - rho <= (1 + 1/c_0)(1 - theta^2), roughly m <= 2(1 + 1/c_0) E.
(KURT) is therefore at least as strong as the eigenvalue form of the fusion
bound it is meant to deliver. It is not a free regularity statement.

3.3 Is the converse true (E >= c m forces kappa >= 1 + c')? NO in the class
(PROVED, Step 6): product chain X = {+1,-1} x Y, P = (bit flip chain) x P_Y.
g = the bit. kappa = 1 exactly, theta arbitrary, rho = gap of Y arbitrary.
A gauge model with the same structure is in Step 6.

3.4 The exact content of (KURT) (PROVED in Step 4). With
lambda_bar := <h,(1-P)h>/||h||^2, the mean one-step energy of the fused state
g^2 - 1:
  kappa - 1 <= (1 - theta^2)/(lambda_bar - (1 - theta^2))   when the
  denominator is positive, and for a diffusion generator EXACTLY
  kappa = 3r/(3r - 2), r = lambda_bar/(2E).
So for diffusions (KURT) <=> lambda_bar <= C E: "the square of the flux
ground state, minus its vacuum part, is an even state of energy O(E)".
Since lambda_bar >= m, (KURT) is the fusion bound m <= C E with m replaced by
the larger number lambda_bar. It is stronger than what the consumer needs,
and of the same kind. It is not easier.

3.5 Where (KURT) holds for free (PROVED, Step 5): when the flux ground level
is a multiplet of a continuous symmetry. O(4) twin: kappa >= 2 at every size
and cutoff. U(1): kappa >= 3/2. SU(2) gauge theory has no such symmetry on
the flux multiplet (non-abelian one-form symmetries do not exist), so the
twin's mechanism is absent. This is where the twin stops being a twin.

3.6 Where (KURT) fails for SU(2) (ARGUED; recalled physics, no source opened):
below the centre crossover (box side below about 1/T_c, the femto-universe of
Luscher and van Baal) the vacuum sits near the eight centre-valued flat
connections, the flux states are the eight sign patterns up to tunnelling,
and kappa -> 1. So (KURT) is not true "in every phase": it is a statement
about which side of the crossover the box is on. In the order-one window
beta 2.3 to 2.6 the crossover sizes are about a = 4 to 10 lattice units; a
seed (m a >= 17) sits at about 3.4 crossover lengths, where recalled string
and glueball values give E about 1.3 m and kappa about 3 (GUIDE-level
physics, not proved).

3.7 Decision. (KURT) at the seed size is equivalent to excluding a "hidden
centre bit": an odd function s with |s| <= 1 and <s,g> >= 1 - c (Step 4,
dual form). By 3.2 that exclusion contains E >= c m. By 3.3 nothing in the
class gives it. The only SU(2)-specific handle I see: a box with a hidden
centre bit is a deconfined box, and for a continuous group a deconfined box
should have even modes with m a = O(1) (torons, magnetic gluons), which the
seed m a >= 17 excludes. Q_8, 2T and Z_2 lack this (their ordered phases are
gapped). U(1) fails the seed itself. I do not prove that step; it is a
weak-coupling small-volume statement of the same kind as the lane's open
Theorem S1. OPEN.

## Step 4. General theorems on kappa (all PROVED here, by hand, unchecked)

Standing assumptions (S). (X, mu) a probability space. P a Markov operator
(P 1 = 1, P f >= 0 for f >= 0), self-adjoint on L^2(mu). A finite group Gamma
acts on X, preserves mu, commutes with P. chi != 0 is a real character.
g is real, bounded, g o gamma = chi(gamma) g, P g = theta g, Int g^2 = 1, and
theta > 0 is the top of the spectrum of P on the sector chi. rho is the top of
the spectrum of P on Gamma-invariant functions orthogonal to 1. When a power
t >= 2 of P is used I also assume P >= 0 (true for the lane's T_(B,m), READ
row 876 L499). M_q := Int |g|^q dmu, c := M_1, kappa := M_4, h := g^2 - 1.

**Theorem 4.1 (moment hierarchy).** For every real p >= 1 and integer t >= 1:
  theta^(pt) M_(2p) <= M_p^2 + rho^t (M_(2p) - M_p^2).                 (MH)
Proof. P^t(x, .) is a probability measure and |.|^p is convex, so
|P^t g|^p <= P^t |g|^p pointwise. The left side is theta^(pt) |g|^p. Multiply
by |g|^p >= 0 and integrate: theta^(pt) M_(2p) <= <|g|^p, P^t |g|^p>.
|g|^p is Gamma-invariant. Write |g|^p = M_p + u with Int u = 0. Then
<|g|^p, P^t |g|^p> = M_p^2 + <u, P^t u> <= M_p^2 + rho^t ||u||^2 and
||u||^2 = M_(2p) - M_p^2. QED
p = 2 is row 876's (SQ). p = 1 is new to the lane as far as I read:
  theta^t <= c^2 + rho^t (1 - c^2), i.e. 1 - c^2 <= (1 - theta^t)/(1 - rho^t).
Corollary (flatness of every moment in the window). If theta^p > rho then
M_(2p)/M_p^2 <= (1 - rho)/(theta^p - rho). A flux much lighter than the even
gap has a ground state that is flat in every L^q, not only in L^4.

**Theorem 4.2 (flip identity).** Assume mu(g = 0) = 0. Put s := sign(g) and
q(x) := P(x, {y : s(y) != s(x)}), the one-step flip probability from x. Then
  (1 - theta) Int |g| dmu = 2 Int q |g| dmu,                           (FLIP)
and qbar := Int q dmu >= (1 - theta)/2, with equality iff P s = theta s.
Proof. theta c = <s, P g> = IntInt mu(dx) P(x,dy) s(x) g(y), and by
stationarity c = IntInt mu(dx) P(x,dy) s(y) g(y). Subtract:
(1 - theta) c = IntInt mu(dx) P(x,dy) |g(y)| (1 - s(x) s(y)). The bracket is
2 on sign changes and 0 otherwise. Reversibility turns the integral into
2 Int |g(y)| q(y) mu(dy). For qbar: 1 - 2 qbar = <s, P s> <= theta ||s||^2 =
theta because s lies in the sector chi. QED
Reading: weighted by |g|, flips happen at exactly the rate (1 - theta)/2.
Unweighted they happen at least that often. Flips sit where |g| is small.

**Theorem 4.3 (kurtosis-energy relation, discrete).** Assume kappa > 1 and
put lambda_bar := <h, (1 - P) h>/||h||^2 and V(x) := (P g^2)(x) - theta^2
g(x)^2 >= 0 (the conditional variance of g at the next step). Then
  (kappa - 1)(lambda_bar - (1 - theta^2)) = - Cov_mu(g^2, V),          (KE)
  lambda_bar (kappa - 1) <= kappa (1 - theta^2).                       (KE-ineq)
Hence: (i) kappa >= 1 + c_0 implies lambda_bar <= (1 + 1/c_0)(1 - theta^2);
(ii) lambda_bar > 1 - theta^2 implies
     kappa - 1 <= (1 - theta^2)/(lambda_bar - (1 - theta^2)).
Proof. <g^2, P g^2> = 1 + <h, P h> = kappa - lambda_bar (kappa - 1). Also
<g^2, P g^2> = theta^2 kappa + Int g^2 V dmu and Int V dmu = 1 - theta^2, so
Int g^2 V = (1 - theta^2) + Cov(g^2, V). Equate: (KE). V >= 0 gives
<g^2, P g^2> >= theta^2 kappa (Lemma SQ), which is (KE-ineq). QED
Since 1 - rho <= lambda_bar, (ii) contains row 876's window. (KE) says more:
kappa is fixed by the fused state's energy and by how the next-step variance
of g correlates with g^2.

**Theorem 4.4 (kurtosis-energy relation, diffusion form, exact).** Let
H >= 0 be a self-adjoint diffusion generator on L^2(mu) with carre du champ
Gamma (chain rule as in row 876 Step 4), H g = E g, E > 0, Int g^2 = 1,
kappa > 1, lambda_bar := <h, H h>/||h||^2. Then lambda_bar > (4/3) E and
  kappa = lambda_bar/(lambda_bar - (4/3) E) = 3r/(3r - 2), r := lambda_bar/(2E).
Also Var_mu(Gamma(g)) = (1/4) <h, (H - 2E)^2 h>, and
<h, (2E - H) h> = (2E/3)(kappa - 3).
Proof. Int Gamma(g^2) = 4 Int g^2 Gamma(g) = (4/3) Int Gamma(g^3, g) =
(4/3) <g^3, H g> = (4/3) E kappa (READ row 876 L403; re-derived). The left
side is <g^2, H g^2> = <h, H h> = lambda_bar (kappa - 1). Solve for kappa.
For the variance: H(g^2) = 2 g H g - 2 Gamma(g) = 2E g^2 - 2 Gamma(g), so
Gamma(g) - E = E h - (1/2) H h = -(1/2)(H - 2E) h. Square and integrate.
The last identity: <h, H h> - 2E ||h||^2 = (4/3)E kappa - 2E(kappa - 1). QED
Table (exact): Ornstein-Uhlenbeck, g = x: r = 1, kappa = 3. Circle, g =
sqrt2 cos: r = 2, kappa = 3/2. Sphere S^(d-1), g = sqrt(d) x_1: r = d/(d-1),
kappa = 3d/(d+2). Autonomous bit: r = infinity, kappa = 1.
Reading: in Hamiltonian form the kurtosis is a function of one number, the
mean energy of the fused state g^2 - 1 in units of 2E. Free fusion (r = 1)
is the Gaussian value 3. (KURT) with constant c_0 is EQUIVALENT to
  lambda_bar <= (4/3)(1 + 1/c_0) E.                                (KURT-E)

**Theorem 4.5 (dual form; the hidden bit).** Under (S):
(a) kappa >= 1/c^2, and c = sup{<s, g> : |s| <= 1}.
(b) kappa - 1 >= 2(1 - c). So kappa - 1 <= eta implies ||g - sign g||^2 <= eta.
(c) If kappa - 1 <= eta, P >= 0 and mu(g = 0) = 0, then s = sign g satisfies
    theta (1 - eta) <= <s, P s> <= theta: the vacuum carries a sign bit whose
    one-step flip probability lies in [(1 - theta)/2, (1 - theta(1 - eta))/2].
Proof. (a) Holder: 1 = Int |g|^(2/3) |g|^(4/3) <= c^(2/3) kappa^(1/3).
(b) kappa - 1 = Int (|g| - 1)^2 (|g| + 1)^2 >= Int (|g| - 1)^2 = 2 - 2c, and
||g - s||^2 = 2 - 2c. (c) <s, P s> = theta + 2 theta (c - 1) + <s - g, P(s - g)>
>= theta - theta eta, using P >= 0 and (b). The upper bound is the sector
bound. QED
So (KURT) fails with small eta exactly when the vacuum measure carries a
"hidden centre bit": a sign function within eta of the flux ground state.
Sufficient for (KURT): c <= 1 - c_1, i.e. no odd observable with values in
[-1, 1] has overlap above 1 - c_1 with the flux ground state. Then
kappa >= (1 - c_1)^(-2).

**Proposition 4.6 (energy-density form, diffusion).** In the setting of 4.4,
for every bounded psi with primitive Psi: Int psi(g) Gamma(g) dmu =
E Int Psi(g) g dmu. Consequences:
(a) Int over {|g| < delta} of Gamma(g) dmu >= E delta (c - delta).
(b) If Int Gamma(g)^2 dmu <= C_2^2 E^2 then kappa - 1 >= min(1, 1/(9(C_2^2 - 1))).
Proof. Chain rule: psi(g) Gamma(g) = Gamma(Psi(g), g); integrate; use H g =
E g. (a) psi = indicator of (-delta, delta), Psi(s) s = min(|s|, delta)|s| >=
delta |s| - delta^2. (b) By 4.4, Var(Gamma(g)) = (1/4)<h,(H - 2E)^2 h> >=
(1/4)(kappa - 1)(lambda_bar - 2E)^2 (Jensen for the spectral measure of h)
and lambda_bar - 2E = E (4 - 2 eta)/(3 eta) with eta = kappa - 1. If eta <= 1
this gives E^2/(9 eta) <= Var(Gamma(g)) <= (C_2^2 - 1) E^2. QED
Reading: for a sign-like g at least a quarter of the energy sits in the thin
set {|g| < 1/2}. (KURT) follows from a reverse Holder bound on the energy
density of g (its relative variance is bounded). That is the central-limit
mechanism: a flux state that is a sum of many weakly dependent tube
positions has a self-averaging energy density. It is a property of g, which
the lane does not control.

## Step 5. Where (KURT) holds for free: a continuous symmetry through the flip (PROVED)

**Theorem 5.1 (circle through the flip).** Assume (S) with Gamma = {1, z}.
Assume a circle group {gamma_phi : phi in R/2 pi Z} acts on X, preserves mu,
commutes with P, and gamma_pi = z. Let W be a finite-dimensional eigenspace
of P inside the odd sector. Then W contains a unit eigenfunction g with
  kappa(g) = (3/8) Int |G|^4 dmu >= 3/2,
where G is a complex function with G o gamma_phi = e^(ik phi) G, k odd,
g = Re G, Int |G|^2 dmu = 2. Equality holds iff |G| is constant.
Proof. W is invariant under the circle. Its complexification splits into
weight spaces; pick a weight vector G of weight k. Since gamma_pi = z acts
as -1 on W, e^(ik pi) = -1, so k is odd and k != 0. Then Re G and Im G lie
in W, are orthogonal and have equal norms (rotate by phi = pi/(2k)).
Normalize Int (Re G)^2 = 1, so Int |G|^2 = 2. Put g = Re G. For fixed x,
g(gamma_phi x) = |G(x)| cos(k phi + alpha_x). The circle preserves mu, so
kappa = Int dmu(x) (1/2 pi) Int_0^(2 pi) g(gamma_phi x)^4 dphi
      = (3/8) Int |G|^4 dmu >= (3/8)(Int |G|^2 dmu)^2 = 3/2. QED

**Theorem 5.2 (transitive multiplet).** Assume (S). Let a compact group G_0
act on X, preserve mu and commute with P. Let W be an eigenspace of P in the
sector chi, of dimension d, with orthonormal basis g_1..g_d, and assume G_0
acts transitively on the unit sphere of W. Then every unit g in W has
  kappa(g) = (3/(d(d+2))) Int (g_1^2 + ... + g_d^2)^2 dmu >= 3d/(d+2).
Proof. Q(v) := Int (sum v_a g_a)^4 dmu is invariant under the orthogonal
action of G_0 on W = R^d, hence constant on the unit sphere: Q(v) = kappa.
Average over the sphere: for fixed x the average of (sum v_a g_a(x))^4 is
|g(x)|^4 times E[v_1^4] = 3/(d(d+2)). Then Cauchy-Schwarz and
Int sum g_a^2 = d. QED

**Where these apply.**
- U(1) lattice gauge theory. The flip z (multiply the links through a plane
  by -1) lies in the circle "multiply them by e^(i phi)", a symmetry of the
  action. Theorem 5.1: kappa >= 3/2 for the flux-one eigenfunction Re G, at
  every coupling and size. Row 876's value 3/2 for the pure cosine is the
  equality case. PROVED. Fact test: U(1) passes (KURT) and still has no gap.
  No contradiction: there "even under z" contains the flux-two states, and
  (SQ) only says that the flux-two energy is at most 4E. The even sum is not
  small in the Coulomb phase, so the consumer gets nothing.
- 2D O(4) twin. -1 = gamma_pi for the circle gamma_phi = (rotation by phi in
  the 12-plane) x (rotation by phi in the 34-plane), i.e. left multiplication
  by e^(i phi sigma_3) on SU(2) = S^3. Theorem 5.1: kappa >= 3/2 in every odd
  eigenspace, every size, every cutoff. If the top odd level is the vector
  multiplet (d = 4; ARGUED, the lightest particle is the vector), Theorem
  5.2 gives kappa >= 2, with equality in the rotor limit. PROVED given that.
  So in the twin (KURT) is a theorem and the flux half is exactly the mass
  gap, as row 876 L497 says.
- SU(2), Q_8, 2T, Z_2 gauge theories. The symmetries that commute with the
  transfer operator on gauge-invariant functions are the lattice symmetries
  and the centre flips: a finite group. The flip does not lie on a circle of
  symmetries (left multiplication of a plane of links by u in SU(2) is a
  symmetry only for u = +-1). Neither theorem applies. The twin's reason for
  (KURT) has no counterpart in the gauge theory. This is a real difference
  between the twin and the target, not a gap in the argument.
- Remark. The finite symmetry group permutes the three flux directions. Its
  invariant quartics on span(g_1, g_2, g_3) are sum g_i^4 and (sum g_i^2)^2,
  two of them, so no bound follows: three independent hidden bits
  (g_i^2 = 1) are allowed by symmetry.

## Step 6. Where (KURT) fails: two exact examples (PROVED)

**Example 6.1 (product chain).** X = {+1, -1} x Y, mu = uniform x nu,
P = B x P_Y, B = [[1-b, b], [b, 1-b]] with 0 < b < 1/2, P_Y any reversible
Markov operator on (Y, nu) with a strictly positive kernel and P_Y >= 0.
The flip is z(sigma, y) = (-sigma, y). The odd sector is {sigma f(y)} and
P(sigma f) = (1 - 2b) sigma P_Y f. So g = sigma, theta = 1 - 2b, kappa = 1.
The even sector is {f(y)}, so rho = rho_Y and S_ev(a) = Tr P_Y^a - 1.
theta and the spectrum of P_Y are independent. Take theta^a = 1/2 and
rho_Y -> 0: p(a) = theta^a/(1 + theta^a) = 1/3 while S_ev(a) -> 0.
So "light or kappa >= 1 + c_0" is false in the class of (S), and so is
(F-h) with any K and any positive exponent. Every inequality of Step 4
holds here with equality or trivially. QED

**Example 6.2 (a Z_2 gauge theory with a hidden bit that is heavy).**
Z_2 gauge theory on the spatial torus (Z/a)^3, a >= 1, with spatial plaquette
coupling beta_s and temporal coupling beta_t. One-step kernel on spatial
link configurations: T(s, s') = e^(-V(s)/2) Kt(s, s') e^(-V(s')/2),
V(s) = beta_s sum_p (1 - s_p), Kt = the gauge average of
prod_l e^(beta_t s_l s'_l). Kt is strictly positive and positive definite.
(a) beta_s = infinity. Only flat s survive. Gauge-invariant functions of a
flat Z_2 connection on the 3-torus are functions of its class eta in
H^1 = Z_2^3. Adding a flat connection commutes with T, so T(eta, eta') =
w(eta + eta') with w > 0: a convolution on Z_2^3. Its eigenfunctions are the
eight characters. The vacuum is the constant, mu is uniform on Z_2^3, and
each flux eigenfunction is g_chi = chi, with values +-1. So kappa_chi = 1
EXACTLY. Each sector is one-dimensional, so the even sector has no excited
state: S_ev = 0 at every time. theta_chi = w^(chi)/w^(0) is continuous in
beta_t, equals 0 at beta_t = 0 (w uniform) and tends to 1 as beta_t ->
infinity (w -> delta), and is >= 0 because Kt is positive definite. So every
value in (0, 1) occurs: the flux can be made as heavy as wanted.
(b) beta_s large and finite. The kernel is strictly positive, (S) holds.
T converges entrywise to the constrained operator, the sector tops are
simple in the limit, so theta_chi, the vacuum and Psi_chi converge.
g = Psi_chi/Omega stays bounded: with k_min <= Kt <= k_max entrywise,
|g(s)| <= (lambda_0/lambda_chi)(k_max/k_min) (sum e^(-V/2)|Psi_chi|)/
(sum e^(-V/2) Omega), and the right side has a finite limit. Since
mu(non-flat) -> 0, kappa_chi -> 1 and S_ev(t) -> 0 for every t >= 1. QED
So a lattice gauge theory with a positive transfer operator, local action,
gauge invariance and exact centre symmetry can have a flux sector that is
heavy (theta^a = 1/2 or anything else), an even sum as small as wanted, and
kappa - 1 as small as wanted. (KURT) and (F-h) both fail there.
Scope. The model is anisotropic (frozen space-like plaquettes, hot
time-like ones). It is not invariant under exchange of a time and a space
axis, which the lane's continuation uses (READ row 876 digest L90). So it
refutes "(KURT) follows from the transfer-operator structure", not "(KURT)
follows from the lane's full class". I found no isotropic counterexample:
for isotropic Z_2 at large beta the electric sectors are light, the first
alternative of (KURT) (ARGUED; at a = 3 the window would need 9 u^9 of
order one with u^12 negligible, impossible). An isotropic model with a stiff
vortex sheet (small tension, large bending cost) is a candidate. OPEN.

**What the examples say about a proof.** A proof of (KURT) for SU(2) must
use (i) isotropy or the exchange of axes, and (ii) something that separates
SU(2) from Z_2, in the same step. Example 6.2 with Q_8 or 2T in place of
Z_2 has the same structure on the centre-valued flat classes (ARGUED, not
worked out).

## Step 7. Corrections, a Cheeger form, the guide run, and the fact tests

**7.1 Correction to Theorem 4.2 (found by the guide run).** g can vanish on
a set of positive measure (in the Z_2 run below mu(g = 0) = 0.44 at small
beta_s). The proof of 4.2 gives, with no assumption on the zero set and
s = sign g in {-1, 0, 1}:
  (1 - theta) Int |g| dmu = IntInt mu(dx) P(x,dy) |g(y)| (1 - s(x) s(y)).
The form with q needs mu(g = 0) = 0. Theorem 4.5 (c) holds as stated without
that assumption (its proof never uses it; then ||s|| <= 1).

**7.2 Corollary (Cheeger form of 4.5; PROVED).** Assume (S), P >= 0. For an
odd s with |s| = 1 put q_1(s) := mu-probability that s changes in one step
= (1 - <s, P s>)/2, and h_odd := inf over such s of q_1(s). Then
h_odd >= (1 - theta)/2, and with delta := (h_odd - (1 - theta)/2)/theta:
  kappa - 1 >= 2 delta.
Proof. Extend s = sign g to the zero set of g by any odd choice of sign;
this changes neither <s, g> = c nor the bound <s, P s> >= theta(2c - 1) from
the proof of 4.5 (c). So h_odd <= q_1(s) <= (1 - theta(2c - 1))/2, hence
delta <= 1 - c, and kappa - 1 >= 2(1 - c) by 4.5 (b). QED
Reading: (KURT) holds as soon as no antisymmetric cut of the configuration
space is close to an eigen-cut. A cut is an eigen-cut when its flip
probability is the same from every configuration (an autonomous bit).
There is no converse: a heavy tail of g makes kappa large with delta small.

**7.3 GUIDE run (a run can refute or guide; it proves nothing).** Scripts
`scratchpad/lane886/scripts/kurt_guide.py` and `kurt_guide2.py` (numpy, a
few seconds, under 100 MB). Criteria written in the script header first.
C1: (MH) for p in {1, 1.5, 2, 3}, t in {1, 2, 3}, (FLIP), (KE), 4.5 (a)-(c)
on 300 random symmetric positive-definite kernels with an involution: no
violation.
C2: Example 6.2 in 2+1 dimensions (Z_2, spatial torus 2 x 2, 8 links, 256
states, Gamma = both flips, sector chi = (1, 0)):
  beta_t = 0.2:  beta_s  0.25    0.5     1.0     2.0      4.0
     kappa       1.788   1.420   1.070   1.0013   1.000000
     theta       0.0443  0.0573  0.0776  0.0832   0.0833
     rho         2.6e-3  3.0e-3  1.0e-3  2e-5     below 1e-7
     S_ev(4)     6e-11   8e-11   1e-12   3e-19    4e-33
  beta_t = 0.4:  kappa 1.799, 1.399, 1.058, 1.0011, 1.000000;
     theta 0.172, 0.233, 0.316, 0.3356, 0.3359; rho 0.036, 0.039, 0.012,
     2.6e-4, below 1e-6.
The sector top is simple in every row. All identities of Step 4 hold in
every row (general form of (FLIP)). Reading: at beta_s = 2, beta_t = 0.2
the flux is heavy (E = 2.49 per step), the even gap is m = 10.8, E/m = 0.23,
and kappa - 1 = 0.0013. So (KURT) fails by three orders of magnitude at a
point where the eigenvalue fusion bound theta <= rho^(0.23) still holds. In
discrete time kappa - 1 can be far smaller than E/m (jumps across the nodal
set). (KURT) is strictly stronger than the bound the consumer needs.
Honest note: my first script took "even" to mean even under one flip only.
Then the other flux sector sits in the "even" sector and rho = theta. That
was a script error (Gamma is the full flip group in (S)); the second script
fixes it. The first script's C1 (random chains, one involution) stands.

**7.4 Fact tests, step by step.**
| Step | U(1) Coulomb | Z_2 at beta 5/2 | frozen 2T, Q_8 | Verdict |
|---|---|---|---|---|
| 4.1-4.6, 7.2 (identities) | hold; conclude no gap | hold | hold | group-blind by design; they bound kappa from above or restate it; no claim that could be false in a rival |
| 5.1 (circle through the flip) | applies: kappa >= 3/2, equality for the cosine | does not apply (no circle) | does not apply | gives (KURT) for U(1), where the conclusion "gap" is false: so (KURT) alone is not a confinement input, the seed is |
| 5.2 (transitive multiplet) | d = 2: kappa >= 3/2 | no | no | twin only |
| 6.1, 6.2 (counterexamples) | n/a | 6.2 is a Z_2 model | same structure (ARGUED) | (KURT) is not a class property |
| 3.2 ((KURT) implies m <= C E) | flux-two state gives m <= 4E: true | sector light, kappa -> 1: consistent | same | a proof of (KURT) for a heavy sector proves the fusion bound |
| 3.7 (missing step (HB), below) | no hidden bit; seed fails | hidden bit and gapped even sector: (HB) false, as it must be | same | (HB) has the right profile: it is false exactly where the consumer's conclusion is false |

**7.5 The missing step, named.** (HB) For isotropic Wilson SU(2) (in truth
the first-passage measure) on the seed boxes: if an electric sector has
kappa - 1 <= eta_0 (a hidden centre bit), then the even sector has an
excitation with m a <= M_0, where eta_0 > 0 and M_0 < log(1/s) for the seed
value s. Given (HB), the seed excludes the hidden bit, (KURT) holds with
c_0 = eta_0, and Theorem SQ-F gives the electric part of (F-h).
Why (HB) is plausible (ARGUED): for a connected gauge group the set of
flat connections on the 3-torus is connected and contains U and z U (the
toron valley; the flip has fixed points there, the trace-zero holonomies).
A hidden bit then exists only through a fluctuation-induced barrier, and
the same valley carries slow even modes of energy O(1/a). For Z_2, Q_8, 2T
the flat classes are isolated and the ordered phase is gapped. For U(1) the
valley is a circle of exact symmetries and there is no bit at all (5.1).
Why I do not prove it: it needs control of the vacuum in a deconfined box at
order-one coupling, the same kind of statement as the lane's open Theorem
S1. OPEN. I do not claim this route is the one that closes; it is the one
whose fact-test profile is right.

**7.6 A weaker target than (KURT) for the consumer (PROVED from READ
statements).** (FUSE-E): lambda_chi/lambda_0 <= (lambda_1^+/lambda_0)^g for
the heavy electric sectors (E >= g m), some g > 0. Then, by row 876's
p_chi(a) <= (1 + S_ev(a/2)) theta^(a/2) (READ L489-492) and
S_ev(a) >= rho^a:  p_chi(a) <= (1 + S_ev(a/2)) S_ev(a)^(g/2).
(KURT) implies (FUSE-E) by (SQ). Example 6.1 with theta = rho^g has
(FUSE-E) and kappa = 1, so (FUSE-E) does not imply (KURT). The consumer
needs (FUSE-E) only. It is a statement about two eigenvalue ratios and no
eigenfunction.

## Step 8. Assembly

**8.1 Errata to the steps above (found on my one re-read of each proof).**
- 7.2 needs Gamma to act freely (so that an odd sign function exists on the
  zero set of g). True on SU(2)^E: z U != U for every U.
- 3.1, wording. Log-Sobolev gives an upper bound on Ent(g^2), and
  Ent(g^2) <= log kappa <= kappa - 1 by Jensen. So it gives no lower bound
  on kappa. Hypercontractivity ||P^t f||_4 <= ||f||_2 gives kappa <=
  theta^(-4t). Both go the wrong way for (KURT).
- 4.2: use the general form of 7.1 unless mu(g = 0) = 0.
- 3.6 and 7.5 use recalled physics (crossover sizes, toron valley, string
  and glueball ratios). No source was opened in this run. They are ARGUED or
  GUIDE-level and carry no proof weight.

**8.2 The brief's suggested tools, one line each.**
- Hypercontractivity, log-Sobolev: upper bounds on kappa only (8.1).
- g as a twisted ground state: |g| is theta-subharmonic, theta |g| <= P |g|
  (Kato-type). That is Theorem 4.1 at p = 1. It bounds Var|g| from above.
- Reflection positivity across the flux: gives Cauchy-Schwarz upper bounds
  on mixed terms. A lower bound on kappa from it needs the half-box
  creation input (HC), where row 876 stopped (READ L419-420). I add nothing.
- The twin: (KURT) is a theorem there (5.1, 5.2), for a reason the gauge
  theory lacks (a circle of symmetries through the flip).
- Chapman-Robbins, duality: kappa^(1/4) >= <W, g>/||W||_(4/3) for every odd
  W (Holder). It needs an explicit W with overlap above its own flatness
  ratio (0.87 in norm for a Gaussian W, i.e. overlap squared above 0.757).
  No overlap bound is available. Stops there.

**8.3 Answer to the brief's questions.**
Q1. When must a flux ground state be chi-square close to the vacuum?
A1 (PROVED). Whenever the fused state g^2 - 1 is much heavier than the flux:
kappa - 1 <= (1 - theta^2)/(lambda_bar - (1 - theta^2)) (4.3), and in
Hamiltonian form exactly kappa = 3r/(3r - 2), r = lambda_bar/(2E) (4.4).
In particular when 2E << m (row 876's window). Then every moment is flat
(4.1), g is within eta of a sign function, and the vacuum carries a hidden
centre bit that flips at the rate (1 - theta)/2 up to theta eta/2 (4.5).
Q2. Is that excluded at the seed size by anything proved in the lane?
A2. No. It is not a class property (6.1, 6.2, PROVED). The exclusion for a
heavy sector contains the fusion bound E >= c m itself (3.2, 4.3), which is
the lane's open crux in its eigenvalue form. For SU(2) the hidden bit does
occur below the centre crossover (ARGUED), so no size-free regularity
theorem can exist. What is left is (HB) of 7.5. OPEN.
Q3. Can (KURT) hold at all? A3. Yes, and it does by symmetry in U(1) and in
the O(4) twin (PROVED, kappa >= 3/2 and kappa >= 2). For SU(2) at the seed
size it is expected with kappa near 3 (free fusion, r near 1; ARGUED), and
that is equivalent to lambda_bar <= C E.

**8.4 Status.**
PROVED here (by hand, each proof re-read once by me, unchecked by another):
- Theorem 4.1, moment hierarchy theta^(pt) M_(2p) <= M_p^2 + rho^t (M_(2p)
  - M_p^2), p >= 1; the p = 1 fusion bound 1 - rho <= (1 - theta)/Var|g|.
- Theorem 4.2 with 7.1, the flip identity.
- Theorem 4.3, (KE): (kappa - 1)(lambda_bar - (1 - theta^2)) =
  -Cov(g^2, V), and (KE-ineq).
- Theorem 4.4: kappa = 3r/(3r - 2) for diffusions; (KURT) <=> (KURT-E):
  lambda_bar <= (4/3)(1 + 1/c_0) E; Var Gamma(g) = (1/4)<h,(H - 2E)^2 h>.
- Theorem 4.5 and Corollary 7.2: kappa >= 1/c^2; kappa - 1 >= 2(1 - c) >=
  2 delta; the hidden-bit reading.
- Proposition 4.6: energy-density form; (KURT) from Int Gamma(g)^2 <=
  C_2^2 E^2 with kappa - 1 >= min(1, 1/(9(C_2^2 - 1))).
- Theorems 5.1, 5.2: kappa >= 3/2 when the flip lies on a circle of
  symmetries; kappa >= 3d/(d + 2) for a transitive multiplet. U(1) and the
  O(4) twin satisfy (KURT) at every size and cutoff.
- Examples 6.1, 6.2: (KURT) and (F-h) fail in the class and in a Z_2 gauge
  theory with frozen space-like plaquettes; kappa = 1 exactly, theta any
  value, even sum zero.
- 7.6: (FUSE-E) suffices for the consumer and is strictly weaker than
  (KURT) (given row 876's READ bound p_chi <= (1 + S_ev(a/2)) theta^(a/2),
  itself unchecked; its check is row 883).
GUIDE: 7.3 (identities on 300 random chains; Example 6.2 on 256 states;
kappa - 1 = 0.0013 at E/m = 0.23).
ARGUED: 3.6 (SU(2) below the crossover has kappa -> 1); 7.5 (why (HB) is
plausible); the isotropic Z_2 remark in 6.2; kappa near 3 at the seed size.
OPEN: (KURT) for SU(2) at the seed size; (HB); (FUSE-E); whether an
isotropic model of the lane's class violates "light or kappa >= 1 + c_0";
the top odd level of the twin being the vector multiplet (needed only for
the value 2, not for 3/2).
Not done: the dyonic sectors (magnetic backgrounds); Steps 4-7 apply to
T_(B,m) as they stand because they use only (S), but I did not re-read
(TM-tw). The first-passage action was not opened; nothing here depends on
the form of the action beyond (S).

**8.5 Advice to the lead (my judgement, not a proof).** Do not spend a proof
lane on (KURT) as a regularity statement. It is the fusion bound with the
even gap replaced by the larger number lambda_bar, so it is harder than
what the consumer needs, and it is false below the crossover. If the
squaring route is kept, its target is (FUSE-E) or (HB): "a seed box is not
a hidden-bit box". (HB) is false for Z_2, Q_8, 2T and empty for U(1), so it
has the profile the fact tests ask for. I have no proof of it and no
evidence that it is easier than (E17).

RESULT: Row 886 (Claude Fable 5.2 max, unchecked): (KURT) is NOT proved and NOT refuted for SU(2) at the seed size; it is decided as a statement: PROVED that kappa - 1 <= (1 - theta^2)/(lambda_bar - (1 - theta^2)) and, in Hamiltonian form, exactly kappa = 3r/(3r - 2) with r = (mean energy of the fused state g^2 - 1)/(2E), so (KURT) <=> lambda_bar <= (4/3)(1 + 1/c_0) E, which contains the fusion bound m <= C E and is strictly stronger than the (FUSE-E) the consumer needs; PROVED that (KURT) holds by symmetry when the flip lies on a circle of symmetries (U(1): kappa >= 3/2; O(4) twin: kappa >= 3/2, and >= 2 for the vector multiplet), a mechanism SU(2), Q_8, 2T, Z_2 gauge theories lack; PROVED that it fails in the class (product chain; Z_2 gauge theory with frozen space-like plaquettes: kappa = 1 exactly, flux as heavy as wanted, even sum zero; GUIDE kappa - 1 = 0.0013 at E/m = 0.23); ARGUED that it fails for SU(2) below the centre crossover; so no size-free regularity proof exists, and the open step is (HB): a box with a hidden centre bit (kappa - 1 <= eta_0) has an even excitation with m a <= M_0 below the seed threshold. OPEN: (HB), (FUSE-E), (KURT) at the seed size.
