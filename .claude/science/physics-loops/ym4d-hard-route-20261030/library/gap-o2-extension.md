# Row 1046: the literal (O2) with an admissible extension

Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit 594d6491b; checked by nobody.

Started: 2026-11-16T12:00:16Z (from `date -u`).

Status: all eight steps written; the last line is the RESULT line. Finished 2026-11-16T12:18:25Z (`date -u`).

Note on the save protocol: the first tool call created this file with its header. The row text was read in the second call. The plan below was added in the third call. This is a small deviation: the plan was not in the first call, because the row text was not yet read.

## Plan (eight steps)

1. Read the row sources: `parts/gap.md`; rows 1042, 1044, 1045; `gap-boundary-q.md` (GR, FLOW extension); `gap-short-step-max.md` 4.1-4.2; `gap-sym-reg.md` 7.3-7.4. Record the exact statements used.
2. Cube test by hand (CUBE-COUL): closed form of Var(Psi) for the FLOW extension on the cube with its lower face pinned.
3. U(1) control: compact U(1) must give zero gain.
4. Decision (A): the literal (O2) with an admissible extension at the pins of EXIST.
5. Decision (B): the consumer inequality and the wall (W).
6. Decision (C): upper-face gradients.
7. Numeric guide run under the numeric lock, if one is needed. It can refute or guide only.
8. Marks table and the RESULT line.

## Step log

### Step 1 (in progress, 2026-11-16T12:00:34Z): read so far `library/gap-coulomb-frame.md` L1-416 and `parts/gap.md` in full.
- 2026-11-16T12:01:00Z: also read `gap-coulomb-frame.md` L415-543, `gap-boundary-q.md` L16-168 (GR, CUBE-Z, CUBE), `gap-short-step-max.md` 4.1-4.2, `gap-sym-reg.md` 6.6 and 7.1-7.4, `gap-pinned-cell-gauge-max.md` (row 1011) Section 2, 3.1-3.5, 7.1-7.5, and check 1045 (`gap-coulomb-frame-check-astra.md`) in full.
- 2026-11-16T12:07:20Z: read check 1044 (`gap-coulomb-frame-check-opus.md`) L82-140 and L212-460 (CG, COUL, UNIQ, cube Q, LEAD-C, HIER, EXIST, LOOP, SQ, CURL-P, U(1), verdicts, corrected texts). Not read: its L1-81 and L142-211 (hand tests, LIP-C, CUBE-C, CUBE-COUL re-derivations).
- 2026-11-16T12:10:44Z: read row 1038 Theorem LEAD (`gap-collapse-frame.md` L255-277), check 1041 section 4 (remainder constants, `gap-collapse-frame-check-astra.md` L205-265), row 1036 7.3 (limits).

### Step 1 result (done 2026-11-16T12:10:44Z, `date -u`): statements used, and the corrections in force

Conventions: row 1036 Step 2 and row 1042 Step 1. SU(2) = unit quaternions, t = Re, s = Im. Link l = (x -> y), head y = h(l).
R_(l,a) f = (d/d eps) f(U_l -> e^(eps e_a) U_l). N_l = Im(U_l S_l), R_(l,a) A = - N_l^a. D_l n = n_x - Ad(omega_l) n_y. F_c = - log Z_c.

Statements used below, each as it stands after its checks.
- FLOW (row 1018 4.1). For a smooth flow field V (fixed rotation B on the pinned links, a smooth field on the free
  links): Psi_V = V A + div V, and H_c(omega; B) = Q_V - Var_omega(Psi_V) with Q_V := - E_omega[V Psi_V]. Existence of a field with
  Psi_V constant is ARGUED there (elliptic theory, not rebuilt).
- GR (row 1036 4.1). For lambda supported on L and V_0 = (d lambda) n (lambda_z n_z on the free links out of z in L): div V_0 = 0,
  Psi_0 = sum over pinned l of lambda_h(l) (D_l n) . N_l, H_c = (d/d eps)^2 F_c(omega_eps), omega_eps,l = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y).
  I call V_0 "the GR extension". The row text calls it the FLOW extension.
- CG, LEAD-C, HIER, EXIST, SQ, CURL-P (row 1042), with these corrections:
  K1 (check 1044). EXIST has a continuous covariant frame on Omega_12 (pins whose two chosen tree-gauge holonomies are
     non-central with non-parallel axes; open, gauge invariant, full Haar measure) and the strict sign on a non-empty
     open gauge-invariant set P' inside P. No ARGUED step remains.
  K2 (check 1045). A Borel covariant selector on every irreducible pin (first non-parallel pair, countable dense set of
     gauges, least index into the interior of B). Either K1 or K2 serves below; I use K1.
  K3 (checks 1044, 1045). UNIQ holds with the constant 28 in the proof (margin 1/8 at eps_G). Not used below.
  K4 (check 1044; check 1045). CURL-P covers co-exact boundary fields plus gradients d lambda with lambda constant on U. The
     missing gradients are those with lambda not constant on U.
  K5 (check 1045). EXIST gives a strictly negative Hessian of the full torus function f_H. It does not give an exact
     critical point or an exact maximum of f_H. HIER maximises the quadratic model only. I do not call it a maximum of F_c.
  K6 (check 1045). Literal (O2) needs an extension: the variance of the GR score is of the same order rho^2 as H_c.
  K7 (check 1041 section 4, C8). LEAD on a fixed cell, ball abs(eta)_2 <= r_0 <= 1: remainder 6 M_3 Lambda^2 r^3 for H_c and
     (4 L_C + 8 B_C) Lambda^2 r^3 for Var(Psi_0), with M_3 = sup abs(D^3 Phi), L_C = sup abs(D CC), B_C = abs(CC(0)), CC(eta) the covariance
     matrix of the pinned forces at the pin e^eta. No size-uniform constant.
  K8 (C3, C13). (O2-min) is extension-free. Negatives are stated per frame, extension, coupling and pin set.
  K9 (checks 1044, 1045). COUL does not minimise the defect. HIER needs c_min := 1 when all c_ij are 0. CG (d): a is fixed
     by every constant c that commutes with all H_l. Not used in a proof below.
- (O2) as first stated (row 1034 7.4): for a pin-measurable boundary frame and boundary lambda,
  H_c(omega; (d lambda) n) + Var_omega(Psi_(d lambda)) <= 0 on a set of pins of positive measure, with Psi of the site-frame extension
  (one vector per boundary site, used on the free link out of that site). This is the GR extension.
- The consumer: row 1011 Section 2 (M1)-(M8), 7.1, 7.4 (N1)-(N3); row 1034 7.1 (Proposition CURL), 7.3.

Three classes of extension are kept apart below.
- (E-GR): the GR extension (one site-frame vector on the free links at a boundary site).
- (E-FROZEN): a frozen vector c_l(omega) on each free link (a function of the pin; no dependence on U), or the right
  rotation - Ad(U_l) c on a free link into a boundary site. Divergence free.
- (E-FLOW): any smooth field b_l(U, omega) on the free links. This is the class of Lemma FLOW and of the row text.

### Step 2 (done 2026-11-16T12:11:45Z, `date -u`): the cube test by hand (lower face pinned, frame COUL)

All of Step 2 is PROVED by hand here unless marked. Nobody checked it. Cube and notation of row 1042 Step 3: pinned links
a = (o -> A), 1 = (A -> C), b = (o -> B), 2 = (B -> C), with o = 000, A = 100, B = 010, C = 110; h = e^(phi u), 0 < phi < pi; Coulomb
gauge H_a = H_1 = q, H_b = H_2 = q^(-1), q = e^((phi/4) u); colour a = cos(gamma) u + sin(gamma) e, f := u x e; c := cos(phi/2);
theta_1 = lambda_A - lambda_C, theta_2 = lambda_B - lambda_C; T(theta) := (1 + 2c)(theta_1^2 + theta_2^2) - 2 c theta_1 theta_2 (positive definite).
CUBE-COUL (row 1042 3.3; HOLDS in checks 1044, 1045): t'(0) = 0 and H_c = - 2 (b_0 + kappa(cos phi)) sin^2(gamma)(1 - c) T(theta).
Also Z_c = e^(b_0 t) G(t) (CUBE-Z, row 1036 4.2), kappa(t) = G'(t)/G(t), and with five strengths the side plaquettes have
xbar(t) := E_omega[t(side plaquette)] = sum_d d u_d' u_d^4 U_(d-1)(t) / sum_d d u_d^5 U_(d-1)(t), the same for the four sides.

**2.1 Lemma TAN (a boundary move tangent to the gauge orbit has an exact extension with zero variance).** Any cell, any
pin omega. Let psi be an su(2)-valued function on the pinned sites (frozen), and B_l := psi_x - Ad(omega_l) psi_y on the pinned links.
Extend by the field V of class (E-FROZEN): psi_z on a free link out of a pinned site z; - Ad(U_l) psi_z on a free link into
a pinned site z; psi_x - Ad(U_l) psi_y if both ends are pinned. Then div V = 0, Psi_V = 0 identically, so
  Var(Psi_V) = 0,   E[Psi_V] = 0 (F_c is stationary along B),   Q_V = H_c(omega; B) = 2 sum over pinned l of (psi_x x Ad(omega_l) psi_y) . E_omega[N_l].
Proof. V is the first-order generator of the gauge map g_x = exp(eps psi_x) on pinned sites, g = 1 on free sites:
g_x U_l g_y^(-1) = exp(eps psi_x) exp(- eps Ad(U_l) psi_y) U_l. The action is gauge invariant, so V A = 0 at every U. A fixed left rotation
and a right rotation by a fixed vector both keep Haar measure, so div V = 0 (directly: sum_a R_(l,a) (Ad(U_l) c)^a = sum_a 2 (e_a x Ad(U_l) c)^a = 0).
FLOW gives Q_V = H_c + 0. Value: with X = psi_x, Y = - Ad(omega_l) psi_y, exp(- eps X) exp(eps (X + Y)) exp(- eps Y) = 1 - (eps^2/2)[X, Y] + O(eps^3)
(the terms of order eps cancel; order eps^2: X^2/2 + (X + Y)^2/2 + Y^2/2 - X(X + Y) - (X + Y) Y + X Y = (Y X - X Y)/2). So e^(eps B) omega is the gauge
transform by g of the pin exp(eps^2 c_l + O(eps^3)) omega_l, c_l = - [X, Y]/2 = psi_x x Ad(omega_l) psi_y, and (d/d eps) F_c(e^(eps v) omega_l) = v . E[N_l]. QED
Reading. For such moves the response is a force term only (the acceleration of C11). The frame does not enter.
U(1): psi_x x psi_y = 0. Every value is 0.

**2.2 Theorem CUBE-EXT (the cube: literal Q(d lambda) = H_c exactly, with the extension written).** Cube with its lower face
pinned, any b_0 >= 0, any pin with h != +-1, frame COUL with any colour a, every lambda on the four lower sites. In the Coulomb
gauge put, for x in {o, A, B, C},
  psi_x := cos(gamma) lambda_x u + Re(w_x) e + Im(w_x) f,
  w_C := sin(gamma) [ theta_1 (1 - e^(i phi/2)) - theta_2 (1 - e^(- i phi/2)) ] / (2 i sin(phi)),
  w_A := sin(gamma) theta_1 + e^(i phi/2) w_C,   w_B := sin(gamma) theta_2 + e^(- i phi/2) w_C,   w_o := sin(gamma)(lambda_o - lambda_A) + e^(i phi/2) w_A.
Then (d lambda)_l a = psi_x - Ad(H_l) psi_y on the four pinned links. Extension: the frozen vector Ad(g_x)^(-1) psi_x on the vertical free
link out of x, and 0 on the four top links. With it Psi = 0 identically and
  Q(d lambda) = H_c(omega; (d lambda) n) = - 2 (b_0 + kappa(cos phi)) sin^2(gamma)(1 - c) T(theta).
So Q(d lambda) <= 0 for every lambda, with Q < 0 unless theta_1 = theta_2 = 0, at every pin with b_0 + kappa(cos phi) > 0 and sin(gamma) != 0.
Proof. Ad(q) is the rotation about u by phi/2: it fixes u and multiplies the complex coordinate of the (e, f) plane by
e^(i phi/2). Along u the four equations read cos(gamma)(lambda_x - lambda_y) = psi^u_x - psi^u_y: true. In the plane they read
  w_o - e^(i phi/2) w_A = sin(gamma)(lambda_o - lambda_A),  w_A - e^(i phi/2) w_C = sin(gamma) theta_1,  w_o - e^(- i phi/2) w_B = sin(gamma)(lambda_o - lambda_B),  w_B - e^(- i phi/2) w_C = sin(gamma) theta_2.
The second, fourth and first hold by definition. The third: eliminate w_o; it is (e^(i phi) - e^(- i phi)) w_C = sin(gamma)[theta_1 - theta_2 + e^(- i phi/2) theta_2 - e^(i phi/2) theta_1],
which is the definition of w_C (2 i sin(phi) != 0). Now TAN, and CUBE-COUL for the value. QED
Remarks.
- The extension is of class (E-FROZEN) and is not (E-GR): on the vertical link out of x it uses psi_x, which is lambda_x a plus the
  transverse vector with coordinate w_x - sin(gamma) lambda_x. This is the freedom named in row 1036 4.4 Example A and in check 1035.
  Theorem BD (row 1034 6.6) is about one vector per site and does not apply.
- w_C stays bounded at phi -> 0: w_C -> - sin(gamma)(theta_1 + theta_2)/4.
- Only the Coulomb frame is used: for a general frame on the cube, (d lambda) n is tangent to the gauge orbit exactly when
  t'(0) = 0 (for h != +-1 the orbit is the level set of t(h), and its tangent space is the kernel of dt).
- The colour off the axis is not covariant on the cube (row 1042 3.3 (i)). For the covariant colour sin(gamma) = 0 and Q = H_c = 0.

**2.3 The GR extension on the cube: exact variance (the closed form the row text names).** Same setting. For the GR extension,
with Lam := lambda_A^2 + lambda_B^2 + 2 lambda_C^2 (the sum of lambda_h(l)^2 over the four pinned links), kappa = kappa(cos phi), xbar = xbar(cos phi):
  Var(Psi_GR) = 2 sin^2(gamma)(1 - c) { kappa T(theta) + [ beta xbar - 2 kappa c (1 + c) ] Lam },
  Q_GR(d lambda) = 2 sin^2(gamma)(1 - c) { - b_0 T(theta) + [ beta xbar - 2 kappa c (1 + c) ] Lam }.
Proof. Q_GR = - E[(d/d eps)^2 A(U, omega_eps)] (GR (d)). The pinned plaquette gives - b_0 t''(0), exactly, with
t''(0) = 2 sin^2(gamma)(1 - c) T(theta) (CUBE-COUL: H_c = - (b_0 + kappa) t''(0) because t'(0) = 0). The side plaquette over l is beta Re(W_l omega_l R_l) and
Re(W_l''(0) omega_l S) = - tau^2 abs(D_l n)^2 Re(omega_l S) + 2 tau^2 (n_x x Ad(omega_l) n_y) . Im(omega_l S) (GR, proof of (d)), tau = lambda_h(l). Expectations: E[Re] = xbar(t) per unit
beta; E[N_l] = (b_0 + kappa)[p_0 : l] s(h_l) (the gradient of F_c = - b_0 t - log G(t); h_l the holonomy based at the tail of l), of which
b_0 [p_0 : l] s(h_l) is the pinned plaquette, so the side part has mean kappa [p_0 : l] s(h_l) = kappa [p_0 : l] sin(phi) u in the Coulomb gauge.
abs(D_l n)^2 = 4 sin^2(phi/4) sin^2(gamma) = 2 (1 - c) sin^2(gamma), and (a x Ad(q^(+-1)) a) . u = +- sin^2(gamma) sin(phi/2), so [p_0 : l](n x Ad n) . u = sin^2(gamma) sin(phi/2)
on all four links. Side part of Q_GR: sum_l tau_l^2 sin^2(gamma) [2 (1 - c) beta xbar - 2 kappa sin(phi) sin(phi/2)], and sin(phi) sin(phi/2) = 2 c (1 - c)(1 + c).
Var = Q_GR - H_c. QED
Check against row 1042 3.4 at phi -> 0 (c -> 1, 1 - c -> phi^2/8, T -> 3 theta_1^2 + 3 theta_2^2 - 2 theta_1 theta_2 = 4 Vv, Lam = Vv + 4 lbar^2):
Var -> (phi^2/4) sin^2(gamma) [beta xbar Vv + 4 (beta xbar - 4 kappa) lbar^2]. This is 3.4's value (abs(xi_perp)^2 = phi^2 sin^2(gamma)/16). Agrees.

**2.4 Verdict of the cube test.**
- The GR extension is not the best one on the cube. With b_0 = 0 it has Q_GR = Var(Psi_GR) >= 0 (exact, 2.3), while H_c < 0.
- The extension of 2.2 has Var = 0 and Q = H_c exactly, for every b_0 >= 0, every pin with h != +-1 and every lambda. So on the
  cube the literal Q(d lambda) <= 0 holds wherever (O2-min) holds, with an extension of class (E-FROZEN).
- The cube is special: the pin space has one gauge-invariant coordinate, so "F_c stationary along B" is the same as
  "B tangent to the gauge orbit". In the 4D cell the first is one equation and the second is many. Step 4 uses
  another argument there.

**2.5 GUIDE run for Step 2 (it proves nothing).** One job under the numeric lock, 2026-11-16T12:12:37Z to 12:12:39Z (`date -u`), 1.64 s,
16 MB, pure Python (`python3 -I`), OPENBLAS_NUM_THREADS = OMP_NUM_THREADS = 1. The checkout is sparse and has no `scripts/`. I copied
`scripts/lab_ops.py` and `scripts/automation_lock.py` with `git show HEAD:` into `/tmp/r1046.H6hjw3/scripts/` and ran the lock from there;
acquire reported "acquired", release "released". Script and output: `/tmp/r1046.H6hjw3/cube_ext_guide.py`, `cube_ext_guide.out` (not
committed). Output, in full:
- G1, max abs residual of the four equations for psi (200 random cases): 8.882e-16;
- G1, max abs Psi for the extension of 2.2 (central difference of the action, step 1e-4, 200 random configurations, b_0 in {0, 1.2}): 2.299e-07;
- G1, max abs Psi for the GR extension on the same configurations (not small, as expected): 2.773;
- G2, max abs difference between TAN's force formula divided by (b_0 + kappa) and - t''(0) = - 2 sin^2(gamma)(1 - c) T(theta): 1.776e-15;
- G3, beta = 2.4, phi = 1.10, gamma = 0.90, lambda = (0.3, 1.0, - 0.6, 0.4) on (o, A, B, C): Var(Psi_GR) by Monte Carlo 0.35747 (mean of Psi - 0.00374,
  120000 weighted samples), closed form of 2.3: 0.35813, with kappa(t) = 0.11302, xbar(t) = 0.50772;
- G3, beta = 2.4, phi = 2.30, gamma = 1.30, lambda = (0, 0.7, 0.7, 0.7): Monte Carlo 2.12784 (mean 0.00780), closed form 2.12075, kappa(t) = 0.12391, xbar(t) = 0.46987.
The Monte Carlo fixes the vertical links to 1 by the gauge at the top sites, samples the four side variables from e^(beta t) and
weights by the top plaquette. It does not use CUBE-Z. The closed form uses the Bessel form of u_d (recalled; GUIDE only).
Not run: any numeric test of Steps 4 to 6. No integral over the 4D cell was computed.

### Step 3 (done 2026-11-16T12:14:13Z, `date -u`): the U(1) control

PROVED (each line is the U(1) reading of a statement of this file; nobody checked it). One axis, Ad trivial, n constant, D n = 0.
- GR: the pin curve is constant, Psi_GR = 0, Q_GR(d lambda) = H_c = 0 for every boundary lambda (row 1036 7.1; check 1045).
- TAN and CUBE-EXT (Step 2): every boundary gradient is tangent to the gauge orbit, with psi = lambda. The extension of TAN is
  the GR extension. Psi = 0, Q = H_c = 0. The cross products in TAN's value vanish. 2.3: sin(gamma) = 0, Var = 0.
- Theorem EXT (Step 4): the statement and its proof hold for compact U(1) word for word (polynomials in the two real
  coordinates of each link; the vector field of a rotation is linear). It says that the least cost over smooth
  extensions equals H_c. For U(1) gradients this is 0 = 0, and for a general theta it returns H_c, which the classical
  bound beta sum_p w_p (d theta)_p^2 already bounds. EXT is blind to the group. It carries no gain for any group.
- HIER+ and Theorems O2-GR, O2-GR+ (Steps 4 and 6): there is no transverse z, all b_j, c_ij and gamma_ij are 0, the hypothesis of
  HIER+ fails, and the strict conclusion is false for U(1) (there Q = 0). They are statements about Ad != 1 only.
- CURL-Q (Step 6): for U(1) the mixed terms with gradients vanish and the classical constant stands. SQ is not needed.
Zero gain: no statement of this file gives compact U(1) more than its classical curl bound, and none gives SU(2) a bound
with the classical constant. Site-sign frames for U(1) (C12) are outside this control, as in check 1045.

### Step 4 (done 2026-11-16T12:15:15Z, `date -u`): decision (A), the literal (O2) with an admissible extension in the 4D cell

All of Step 4 is PROVED by hand here unless marked. Nobody checked it. Cell: the lane's 4D box, all S_mu >= 2, homogeneous beta > 0,
weights of row 1011 3.1; all boundary links pinned; N pinned links; n_f free links; UU := SU(2)^(free links) with Haar probability dU.
a_0 := beta sum over all plaquettes of w_p, so abs(A) <= a_0. abs(N_l) <= 6 beta.

**4.1 Lemma POLY (the Haar Laplacian is onto the mean-zero polynomials).** Let PP_d be the space of functions on UU that are
restrictions of real polynomials of degree at most d in the 4 n_f real quaternion coordinates of the free links. Let
Delta := sum over free l and a = 1, 2, 3 of R_(l,a)^2. Then:
 (a) R_(l,a) maps PP_d into PP_d; PP_d has finite dimension; A is in PP_4 and every component of every N_l is in PP_3.
 (b) int R_(l,a) F dU = 0 for every smooth F. So int (Delta p) q dU = - sum_(l,a) int (R_(l,a) p)(R_(l,a) q) dU: Delta is symmetric on PP_d for the L^2(dU) inner product.
 (c) If p is in PP_d and Delta p = 0, then p is constant.
 (d) For every p in PP_d with int p dU = 0 there is exactly one v in PP_d with int v dU = 0 and Delta v = p. Write v = G_d p. G_d is linear.
Proof. (a) U_l -> e^(eps e_a) U_l is a linear flow on the R^4 of link l that keeps UU. Its generator is a linear vector field,
and the derivative of a polynomial of degree at most d along a linear vector field has degree at most d. Quaternion
products and conjugates are polynomial, a plaquette has at most four free links and a staple at most three.
(b) Haar measure is invariant under left translation; differentiate int F(e^(eps e_a) U_l) dU = int F dU. Apply it to F = (R p) q and
use the product rule. (c) By (b), sum int (R_(l,a) p)^2 = 0, so every R_(l,a) p = 0 (continuity), so p(e^(theta w) U_l) = p(U_l) for all unit w and theta;
every element of SU(2) is e^(theta w). (d) The L^2(dU) form is positive definite on PP_d (continuous functions, Haar measure of
full support). A symmetric operator on a finite-dimensional inner product space maps onto the orthogonal
complement of its kernel. By (c) the kernel is the constants. QED
This is linear algebra on a finite-dimensional space. No elliptic theory is used.

**4.2 Theorem EXT (the least cost over smooth extensions is the response; the field and the constant written).**
Any pin omega, any rotation field B on the pinned links. Let V_0 be an extension of B with div V_0 = 0 and with Psi_0 := V_0 A in PP_3
(examples: the extension by zero, Psi_0 = - sum_l B_l . N_l; the GR extension for B = (d lambda) n, Psi_0 = sum_l lambda_h(l) (D_l n) . N_l). Put
  c := E_omega[Psi_0],  f := Psi_0 - c,  E_n := sum over k <= n of A^k/k!,  r_n := sum over k > n of a_0^k/k! <= a_0^(n+1) e^(a_0)/(n + 1)!,
  g_n := - f E_n (in PP_(4n+3)),  gbar_n := int g_n dU,  v_n := G_(4n+3)(g_n - gbar_n),
  W_n := the field on the free links with components (W_n)_l^a = e^(-A) R_(l,a) v_n, frozen at the base pin,   V_n := V_0 + W_n.
Then V_n is a smooth flow field of class (E-FLOW), and
  Psi_(V_n) = c + e^(-A) [ f (e^A - E_n) - gbar_n ],    sup over U of abs(Psi_(V_n) - c) <= 2 e^(a_0) r_n sup abs(f) <= 4 e^(a_0) r_n sup abs(Psi_0),
  H_c(omega; B) <= Q_(V_n) = H_c(omega; B) + Var_omega(Psi_(V_n)) <= H_c(omega; B) + 16 e^(2 a_0) r_n^2 (sup abs(Psi_0))^2.
The map B -> V_n is linear when B -> V_0 is. So Q_(V_n) is a quadratic form in B. In particular
  inf over extensions of class (E-FLOW) of Q_V = H_c(omega; B)     for every pin and every B.
Proof. For a field W = e^(-A) X on the free links: W A + div W = e^(-A) sum (X_l^a)(R_(l,a) A) + sum R_(l,a)(e^(-A) X_l^a) = e^(-A) sum R_(l,a) X_l^a. With X_l^a = R_(l,a) v
this is e^(-A) Delta v. Psi is linear in the field and div V_0 = 0, so Psi_(V_n) = Psi_0 + e^(-A)(g_n - gbar_n) = c + f - e^(-A) f E_n - e^(-A) gbar_n. Next
int f e^A dU = Z_c E_omega[f] = 0, so gbar_n = int f (e^A - E_n) dU, and abs(e^A - E_n) <= r_n. e^(-A) <= e^(a_0). FLOW gives the identity for Q. QED
Remarks.
- EXT proves the infimum form of the sentence that row 1018 4.1 left ARGUED ("the response equals the least cost over
  all flows"). It does not prove that a minimiser exists. An exact minimiser needs Delta v = - f e^A with a smooth v
  (ARGUED: Fourier series on the compact group; not rebuilt; not used).
- The rule omega -> W_n is continuous where omega -> V_0 is (G_d is a fixed linear map; the coefficients of A, f, E_n are continuous
  in the pin). It is gauge covariant when V_0 is (Delta and Haar measure are invariant under gauge maps of UU).
- EXT is blind: it holds for every pin, every field B, and every compact group in place of SU(2) (Step 3).
  It moves information from nowhere. It says the extension is never the obstruction in class (E-FLOW).

**4.3 Corollary A-FLOW (decision (A) in class (E-FLOW), at the pins of EXIST).** Setting and conclusion of Theorem EXIST with K1:
frame n continuous and covariant on Omega_12, open set P', H_c(omega; (d lambda) n) <= - m_0 sum over y in Y of lambda_y^2 for every lambda on L. Take V_0 = the GR
extension. Then sup abs(Psi_0) <= 6 beta sum_l abs(lambda_h(l)) abs(D_l n) <= 12 beta sqrt(N) (sum_l lambda_h(l)^2)^(1/2) <= 24 beta sqrt(N) abs(lambda)_2 (at most four pinned links
have a given head). Choose n with
  r_n <= sqrt(m_0) / (136 beta sqrt(N) e^(a_0))        (for example by a_0^(n+1) e^(a_0)/(n + 1)! at most that number).
Then for every pin of P' and every lambda supported on L:
  Q_(V_n)(d lambda) = H_c + Var(Psi_(V_n)) <= - m_0 abs(lambda)^2 + 16 . 576 beta^2 N e^(2 a_0) r_n^2 abs(lambda)^2 <= - (m_0/2) sum over y in Y of lambda_y^2.
So the answer to (A) is yes: Var(Psi) <= (m_0/2) sum lambda^2 with the extension V_n = (GR extension) + e^(-A) grad v_n, and the literal
Q(d lambda) <= 0 holds on P' with a strict margin. The extension depends on the pin and on the free links, as the row
text allows. (16 . 576 = 9216 = 96^2, and 96 sqrt(2) < 136.)
The opposite alternative of the row text ("every admissible extension has Var(Psi) above m_0 sum lambda^2") is false in class
(E-FLOW) at every pin, by EXT.

**4.4 Lemma HIER+ (HIER with a second form).** Hypotheses of Lemma HIER (row 1042 5.3; c_min := 1 if all c_ij are 0, K9).
Let gamma_ab (1 <= a, b <= k) be bounded continuous real functions of vartheta with gamma_ab = gamma_ba, and Gamma_r(vartheta) := the matrix (r_a r_b gamma_ab(vartheta)).
Then there are r in (0, infinity)^k and vartheta* with grad E(vartheta*) = 0, Hess E(vartheta*) negative definite, and
Hess E(vartheta*) + Gamma_r(vartheta*) negative definite.
Proof. HIER's induction, with the statement S_j: E_j has a critical point vartheta^(j) at which Hess E_j and
M_j := Hess E_j + (r_a r_b gamma_ab) over a, b <= j are both negative definite. j = 1: Hess = - r_1 abs(b_1) and M_1 = - r_1 abs(b_1) + r_1^2 gamma_11 < 0 for
r_1 < abs(b_1)/(1 + sup abs(gamma_11)). Step: HIER's implicit-function branch gives a critical point of E_j that tends to
(vartheta^(j-1), arg g_j) as r_j -> 0, with Hess E_j negative definite for small r_j (HIER). At it, M_j has the blocks
  M_(j-1)(vartheta^(j-1)) + o(1),     r_j (v + (r_a gamma_aj)_a),     - r_j (abs(g_j) + o(1)) + r_j^2 gamma_jj
(the first by continuity of gamma and of Hess E_(j-1); the entries of Hess E_j in row j carry the factor r_j). The first block
is negative definite for small r_j, and the Schur complement is - r_j abs(g_j)(1 + o(1)) + O(r_j^2) < 0. Take r_j below these
thresholds and below HIER's own (r_j <= q r_(j-1)). QED

**4.5 Theorem O2-GR (the literal (O2) of row 1034 7.4, with the plain GR extension, on an open set of pins).**
Hypothesis (CONN) of EXIST at the coupling beta (true for 0 < beta < 3/2 and for beta > 0 outside the discrete set D). Then there are a
non-empty open gauge-invariant set P_2 of pins, inside Omega_12 and inside any given neighbourhood of the pure-gauge orbit,
a number m_2 > 0, and a frame n on the pinned sites, continuous and gauge covariant on Omega_12, such that for every pin of
P_2 and EVERY lambda supported on L, with the GR extension (lambda_z n_z on the free links out of z):
  Q_GR(d lambda) = H_c(omega; (d lambda) n) + Var_omega(Psi_GR) <= - m_2 sum over y in Y of lambda_y^2.
Hence also H_c <= - m_2 sum lambda_y^2 there. This is (O2) as row 1034 7.4 states it, existential form, with a strict sign.
Proof. Notation of row 1042 5.1 and 5.4. (1) Choose z_G and the patterns zeta_j as in EXIST (1). For z = z_G + sum_j r_j zeta_j and lambda in R^Y put
  VV_z(vartheta)[lambda, lambda] := sum over pinned l, l' of C_0(l, l') lambda_l lambda_l' Re( conj(z_l) z_l' e^(i (vartheta_h(l') - vartheta_h(l))) ) = sum over i, j of lambda_i lambda_j r_i r_j gamma_ij(vartheta),
  gamma_ij(vartheta) := Re( e^(i (vartheta_j - vartheta_i)) sum over l in in(y_i), l' in in(y_j) of C_0(l, l') conj(zeta_i,l) zeta_j,l' )
(lambda = 0 on the heads of G). The gamma_ij are bounded and continuous. VV_z is positive semidefinite, because C_0 is a covariance
matrix. (2) HIER+ gives r, vartheta* and mu_2 > 0 with (Hess E_z + VV_z)(vartheta*) <= - mu_2 on R^Y. (3) Let eta := z, H* := T_(theta*) e^(rho eta), theta* := - vartheta*/2. The
logarithm of H* has transverse part rho e^(i vartheta*_h(l)) z_l and norm rho abs(eta). LEAD-C: Hess f_(H*)(0)[lambda, lambda] <= 4 rho^2 Hess E_z(vartheta*)[lambda, lambda] + 6 M_3 rho^3 abs(eta)^3 abs(lambda)^2.
K7 in the coordinates H = e^eta: Var_(H*)(sum_l lambda_h(l) (a - Ad(H*_l) a) . N_l) <= 4 rho^2 VV_z(vartheta*)[lambda, lambda] + (4 L_C + 8 B_C) rho^3 abs(eta)^3 abs(lambda)^2 (the leading term is
4 sum C_0(l, l') lambda_l lambda_l' eta_perp_l . eta_perp_l' at the pin H*). So the sum is at most (- 4 mu_2 rho^2 + (6 M_3 + 4 L_C + 8 B_C) rho^3 abs(eta)^3) abs(lambda)^2 <= - 2 mu_2 rho^2 abs(lambda)^2 for
rho <= 2 mu_2/((6 M_3 + 4 L_C + 8 B_C) abs(eta)^3) and rho abs(eta) <= r_0. (4) The matrix of the form QQ_H[lambda, lambda] := Hess f_H(0)[lambda, lambda] + Var_H(sum_l lambda_h(l) (a - Ad(H_l) a) . N_l) is
continuous in H. Take a closed ball B_2 around H* with QQ_H <= - m_2 := - mu_2 rho^2 on B_2. (5) Frame and pin set as in K1 with B_2 in
place of B: g(omega) := g* gamma(omega), n_x := Ad(g_x)^(-1) i, P_2 := {omega in Omega_12 : omega^(g(omega)) in int B_2}. For omega in P_2: H_c(omega; (d lambda) n) = Hess f_(omega^g)(0)[lambda, lambda] (CG (c)), and
Var_omega(Psi_GR) = Var_(omega^g)(sum_l lambda_h(l) (a - Ad(H_l) a) . N_l) (GR (c); the law and the forces are gauge covariant, a = i). GR (e): Q_GR = QQ_(omega^g)[lambda, lambda]. QED
Remarks.
- The mechanism. In HIER the sizes fall fast: r_1 >> r_2 >> ... . The response at the site y_j is of order - r_j abs(g_j), a product of
  r_j with a larger size. The variance of the GR score at y_j is of order r_j^2. So a steep hierarchy puts the variance
  below the response. K6 is right that both are of order rho^2; the ratio is set by the hierarchy, not by rho.
- Quantifiers: there EXIST one frame and one open pin set such that FOR ALL lambda on L the literal cost is negative.
- P_2 is built with the sizes of HIER+. It is not shown that the set P' of row 1042 (built with HIER's sizes, which are not
  fixed there) has Var(Psi_GR) <= m_0 sum lambda^2. That statement is OPEN for P' and is not needed: 4.3 covers P' in class (E-FLOW).
- m_2, mu_2, rho are not numbers. beta in 2.3 to 2.6 is not named. Nothing is uniform in S. K5 applies: a negative Hessian, not a maximum.

**4.6 Verdict on (A).**
- Class (E-FLOW): YES at every pin of P' (4.3), constant m_0/2, extension written. More: in this class the extension is
  never the obstruction, at any pin (EXT). Literal (O2) in class (E-FLOW) follows from strict (O2-min); it implies (O2-min).
- Class (E-GR), the wording of row 1034 7.4: YES on the open set P_2 (4.5). OPEN on P' itself.
- Class (E-FROZEN): YES on the cube, with Var = 0 exactly (2.2). In the 4D cell (E-GR) is a subclass, so P_2 serves.
- No negative is proved. In particular I did not prove a lower bound for Var(Psi_GR) on any pin set of the 4D cell.

### Step 5 (done 2026-11-16T12:16:00Z, `date -u`): decision (B), the consumer

**5.1 The inequality that (O2) feeds (from the record; nothing new).** Route (ii) is the gauge form of the 2D chain (M1)-(M8) of
row 1011 Section 2. Its first link is the start bound (M2)-(M3). In the form of row 1011 7.1, row 1018 4.1 and row 1034 7.1, 7.3:

  (S)   H_c(omega; theta_bd n(omega)) <= Q_V(theta) <= C sum over plaquettes p of the cell of w_p (d theta)_p^2      for every link field theta of the cell,

for the cells c of a tiling and the pins omega that the ring law produces, with one frame rule n, one linear extension rule
theta -> V, and a constant C that is the classical one (beta) times a blind factor. The left inequality is FLOW. The right one
is the obligation. For theta inside the cell it is Proposition CURL given a potential (Lemma O1, OPEN). At the boundary its
restriction to closed fields theta = d lambda, lambda on the pinned sites, has right side 0. That restriction is (O2): Q(d lambda) <= 0.
After (S), the route needs: (N1) (S) on the pins that carry the measure, with the rare cells controlled; (N2) the
controlled cancellation of the mass-like term; (N3) the gain, a lower bound on a variance through the bracket of
Proposition W, which lowers the constant of (S) by a fixed amount per scale. Only (N3) is a selective step. A gain at
every scale of the band is (T-pin) of row 1018, and with it (CAS) with theta < 1, which gives (W) (row 708).
The gauge form of (M4), the exact Hessian of the ring action as a sum of cell stiffnesses, is not on record as a theorem
for field-dependent frames. I do not state one.

**5.2 Proposition EQ (what literal (O2) is, in class (E-FLOW); PROVED from EXT).** Fix a cell, a pin, a frame n frozen at the pin,
and a linear space Lam of potentials lambda on the pinned sites.
 (i)  If some linear extension rule of class (E-FLOW) has Q_V(d lambda) <= 0 for all lambda in Lam, then H_c(omega; (d lambda) n) <= 0 for all lambda in Lam.
 (ii) If H_c(omega; (d lambda) n) <= - m abs(lambda)^2 for all lambda in Lam with m > 0, then for every delta in (0, m) there is a linear extension rule of class
      (E-FLOW), written in 4.2, with Q_V(d lambda) <= - (m - delta) abs(lambda)^2 for all lambda in Lam.
 (iii) More generally, for every boundary field theta and every delta > 0 there is a linear rule with H_c(omega; theta n) <= Q_V(theta) <= H_c(omega; theta n) + delta abs(theta)_2^2.
Proof. (i) FLOW. (ii), (iii) EXT with the base extension by zero or GR, and n large. QED
So in class (E-FLOW) the cost Q carries no information beyond the response: (S) is the statement
  (S')   H_c(omega; theta n(omega)) <= C sum_p (d theta)_p^2
about the Hessian of F_c along frame directions, up to an arbitrarily small mass term delta abs(theta)^2. Literal (O2) in that class
is (O2-min) with a strict margin. K8 stands for narrower classes: for one named extension (E-GR), (O2-min) is
necessary only. But the open item "(O2) needs an admissible extension" (K6) is closed positively by Step 4.

**5.3 What a positive-measure (O2) gives.** On the pin set where it holds (P' or P_2, and P_3 of Step 6):
- the cell bound (S') on closed boundary fields with the constant 0, and by Lemma SQ the curl bound for the fields of
  CURL-P (K4), with C = (A_0 + 16 A_0^2/m_0)/mu_1; with Step 6, for every boundary field on P_3 (Corollary CURL-Q);
- nothing at any other pin.
Lemma AVG (PROVED, one line). Let GG be a measurable set of pins with probability p under a law of pins, on which
H_c(omega; theta n) <= C sum_p (d theta)_p^2 for the fields of a class Th. Then for theta in Th: E[H_c(omega; theta n)] <= p C sum_p (d theta)_p^2 + (1 - p) A_0 abs(theta)_2^2,
with A_0 = 24 beta + 36 beta^2 N (CURL-P (a)). Proof: split the expectation; abs(H_c) <= A_0 abs(theta)^2 everywhere. QED
The second term is a mass term. With this bound alone it is below c sum_p (d theta)_p^2 on (ker d)-perp only if (1 - p) A_0 <= c mu_1, mu_1 the
least non-zero eigenvalue of d^T d (of order S^(-2); ARGUED order, as in check 1044). So the route needs p within c mu_1/A_0 of 1.
That is (N1). For the sets P', P_2, P_3: each is one open set inside a rho-neighbourhood of the pure-gauge orbit on the
whole boundary of a fixed cell, with rho small and not written as a number. Its probability under the ring law at
order-one coupling is positive (Haar-positive open set, positive density) and is not estimated. I expect it to be
very small (ARGUED: all boundary plaquettes must be within order rho of 1). No bound on it is proved in either direction.
With p small or unknown, AVG returns the trivial mass bound A_0 abs(theta)^2. So a small-measure (O2) gives the consumer nothing.

**5.4 Lemma MEAN (the sign on a torus orbit has mean zero; PROVED).** Fix a pin H in a frozen gauge and the colour a. The function
f_H(theta) = F_c(T_theta H) on R^(heads) has period pi in every coordinate (e^(pi a) = - 1 is central, so T_(pi e_y) is the identity map). Hence for
every lambda:  the integral over [0, pi]^(heads) of Hess f_H(theta)[lambda, lambda] d theta is 0.
So along the orbit {T_theta H}, with the frame "colour a in this gauge" carried along, the response H_c to the gradient d lambda is
either zero at every point or positive on a non-empty open set of theta. Proof: the integral of the second derivative
of a smooth periodic function along a fixed direction over a period cell is 0 (Fubini and the fundamental theorem). QED
Reading and scope. The strict negative sign of EXIST and O2-GR at H* is paid for by a positive response elsewhere on
the same torus orbit, for the same frozen frame. T keeps Haar measure, so for the lab frame n = a (not covariant) the
Haar mean of H_c(omega; (d lambda) a) over all pins is 0 for each lambda. MEAN says nothing about a covariant frame at other pins: the
frames of EXIST and O2-GR are not carried by T (the gauge g(omega) is not T-equivariant), and the law of the model is not
Haar. It is the precise form of "a descent, not a stiffness" (C11, K5) for this construction. U(1): f_H is constant.

**5.5 Does any item of the wall (W) move? No. The step that fails.**
(W): there are a bound (L_0, D_0) of (BDD-Delta) and L in P with L >= 4 L_0 and z^-(L) > 256 D_0 + 30 (`parts/gap.md` L21-23). Its forms on
record: (BDD-Delta) with (Z-UNB); (CAS) with theta < 1 and an extensive base. Route (ii) reaches (W) only through a gain at every
scale of the band ((N3), then (T-pin) or (CAS)). Item by item:
- (BDD-Delta), (Z-UNB), (CAS), (TH): none is touched. No statement here reads a physical size, a doubling, or the trajectory.
- (S) at the pins that carry the measure, (N1): not touched. First failing step: from "(O2) on one open set of pins near the
  pure-gauge orbit" to "(S) with ring probability near 1". Lemma AVG shows what is lost, and 5.3 says why p is not near 1
  by anything proved.
- The classical constant in (S): not obtained. On the pin sets C = (A_0 + 16 A_0^2/m_0)/mu_1 with m_0 = mu rho^2 -> 0 at the pure-gauge orbit.
- (N2): on the pin sets the mass-like term is negative on gradients (more than a cancellation there). Elsewhere: nothing.
- (N3): not touched. A negative response on gradients is not a variance lower bound, and by MEAN it has mean zero on torus orbits.
- (O1), tilings (one frame for two cells on a shared face): not touched.
What did change for route (ii): the boundary obligation is now one statement, (S'), about H_c alone (Proposition EQ). The
extension is no longer a separate open item. The existential (O2) of row 1034 7.4 is decided positively (Step 4), also
for upper-face gradients (Step 6). Neither moves (W).

### Step 6 (done 2026-11-16T12:17:21Z, `date -u`): decision (C), upper-face gradients

All of Step 6 is PROVED by hand here unless marked. Nobody checked it. Cell of Step 4. Y+ := the pinned sites other than the
corner 0. Y+ is the set of heads of pinned links (every boundary site except 0 has a pinned link into it, and 0 has
none: row 1042 Step 5 for L, and for y in U a face link (y - e_mu, mu); check 1044 Step 6, fact (F1)). U as in row 1042.
The cube has no upper pinned site, so it tests (A) only. Its one lesson for (C): there is no ground on the cube, and
the constant on {A, B, C} is an exact null direction (row 1042 5.2). The same happens below on the whole boundary.

**6.1 Lemma GR+ (gauge return on the whole boundary).** Let n be unit vectors on the pinned sites (frozen at the pin), lambda any
real function on the pinned sites (not only on L), B = (d lambda) n. Extend B by the field V+ on the free links:
  V+_l := lambda_x n_x - lambda_y Ad(U_l) n_y   for a free link l = (x -> y),   with lambda n := 0 at free sites.
(On a free link out of z this is lambda_z n_z, GR's choice. On a free link into z in U it is the right rotation - lambda_z Ad(U_l) n_z.) Then:
 (a) div V+ = 0;
 (b) Psi+ := V+ A = sum over pinned l of lambda_h(l) (D_l n) . N_l;
 (c) H_c(omega; (d lambda) n) = (d/d eps)^2 F_c(omega_eps), omega_eps,l = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y), for every such lambda. So CG (c) holds with theta on all of Y+:
     H_c(omega; (d lambda) n) = Hess f_H(0)[lambda, lambda], f_H(theta) = F_c(T_theta H), T acting through the heads;
 (d) Q+ := - E[V+ Psi+] = H_c + Var(Psi+).
Proof. Let G be the generator of the gauge map g_x = exp(eps lambda_x n_x) on pinned sites, g = 1 on free sites: G_l = lambda_x n_x - lambda_y Ad(U_l) n_y on every
link. On a pinned link G_l = (d lambda)_l n_x + lambda_y D_l n. So V+ = G - (lambda_h(l) D_l n on the pinned links, 0 on the free links). G A = 0 by gauge
invariance, and R_(l,v) A = - v . N_l. This is (b). (a): fixed left rotations and right rotations by fixed vectors (2.1).
(c): (omega_eps)^g has the links exp(eps lambda_x n_x) exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y) exp(- eps lambda_y n_y) = exp(eps (d lambda)_l n_x) omega_l, and Z_c(omega^g) = Z_c(omega) for every g on the sites of the
cell (row 1011 3.1). (d): FLOW. QED
Remarks.
- GR (e) of row 1036 was stated for lambda on L. Its first equality needs only the gauge covariance of Z_c, so it holds on the
  whole boundary. The restriction to L was needed for GR's fixed-vector extension, not for the response. Row 1042's
  sentence "GR does not treat them" (7.3) is right about the extension and too narrow about H_c.
- As a site-frame move, V+ on a free link into z in U is theta_l n'_x with theta_l = - lambda_z and n'_x := Ad(U_l) n_z, the transport of n_z to the
  free tail. This is the case that row 1034 6.6 left out ("an interior frame may read it").
- lambda -> lambda + const on Y+ (any value at 0): the same boundary field up to a move at the corner, which is an exact gauge move
  (CURL-P (b)). T_(const) is a constant gauge map, so f_H(theta + const) = f_H(theta) exactly. The extension V+ does depend on the constant.

**6.2 LEAD-C and connectivity on all heads.**
- LEAD-C (row 1042 5.1) holds with R^Y replaced by R^(Y+): its proof reads the heads of the pinned links and uses no
  property of L (the rotation R_theta turns z_l by - 2 theta_h(l); the Taylor step is that of K7).
- (CONN+): the graph on Y+ with y ~ y' when Hh_0(l, l') != 0 for some l in in(y), l' in in(y') is connected. For 0 < beta < 3/2 this is
  what checks 1044 (Step 6 (5), "the boundary minus 0, with the off-axis pinned links, is connected") and 1045 ("the whole
  boundary minus 0 connects through the stated edges") prove before they collapse U to the ground. For beta outside D
  the same pairs have Hh_0 != 0. So (CONN+) holds exactly where (CONN) is proved.

**6.3 Theorem O2-GR+ (literal (O2) for every boundary gradient, upper faces included, on an open set of pins).**
(CONN+) at beta (true for 0 < beta < 3/2 and for beta > 0 outside D). Fix y_1 in U, for example y_1 = (1, 1, 1, S_4). Then there are a non-empty open
gauge-invariant set P_3 of pins, inside Omega_12 and inside any given neighbourhood of the pure-gauge orbit, m_3 > 0, and a
frame n continuous and covariant on Omega_12, such that for every pin of P_3 and EVERY real lambda on the pinned sites, with the
extension V+ of the normalised potential lambda - lambda_(y_1):
  Q+(d lambda) = H_c(omega; (d lambda) n) + Var_omega(Psi+) <= - m_3 sum over y in Y+ of (lambda_y - lambda_(y_1))^2.
Hence H_c(omega; (d lambda) n) <= - m_3 sum over Y+ of (lambda_y - lambda_(y_1))^2. The right side is 0 only if lambda is constant on Y+, an exact gauge direction.
Proof. Order Y+ minus {y_1} as y_2, ..., y_k by breadth-first search from y_1 in the graph of (CONN+). Take in(y_1) as the ground:
choose z_G on in(y_1) and patterns zeta_j on in(y_j) with the non-vanishing of EXIST (1). On {vartheta_(y_1) = 0}, E_z is the E of HIER plus a constant,
and gamma_ij is defined as in 4.5 (1). HIER+ gives r, vartheta* (with vartheta*_(y_1) = 0) and mu_3 > 0. For lambda with lambda_(y_1) = 0 the steps (3)-(5) of 4.5 apply word for
word, with LEAD-C on R^(Y+), with GR+ (b)-(d) in place of GR (c), (e), and with a ball B_3: Q+ <= - m_3 abs(lambda)^2, m_3 := mu_3 rho^2. For a
general lambda, d lambda = d(lambda - lambda_(y_1)) on the pinned links, so H_c is the same, and the extension is taken for lambda - lambda_(y_1). The value at the
corner 0 enters neither Psi+ (0 is not a head) nor H_c. QED
Remarks.
- For lambda supported on L (so lambda_(y_1) = 0) this is the conclusion of O2-GR and of EXIST, on the pin set P_3.
- Quantifiers: there EXIST one frame and one open pin set P_3 such that FOR ALL boundary lambda the literal cost is at most
  - m_3 times the squared distance of lambda from the constants. It is not a statement about P' or P_2: on those sets the
  sign of H_c for lambda not constant on U is OPEN (their construction grounds all of U and controls no direction inside U).
- In class (E-FLOW) the same holds on P_3 with any base extension and the correction of 4.2 (EXT covers every boundary
  field at every pin). So the answer to "does the same extension work for upper-face gradients" is yes for the
  extension; the sign of H_c on those gradients is the content, and it is supplied by P_3, not by P'.

**6.4 Corollary CURL-Q (a curl bound for the cost itself, on P_3).** Pin in P_3, frame of 6.3. For a boundary field theta = theta_c + d lambda with theta_c
orthogonal to ker d and lambda a potential on the pinned sites, normalised by lambda_(y_1) = 0, extend theta_c by zero and d lambda by V+. Let
Q(theta) := H_c(omega; theta n) + Var(Psi_theta) be the cost of this linear rule. Then
  H_c(omega; theta n) <= Q(theta) <= C_Q sum over boundary plaquettes of (d theta)_p^2,    C_Q := (A_1 + B_1^2/m_3)/mu_1,   A_1 := A_0 + 36 beta^2 N,   B_1 := 4 A_0 + 144 beta^2 N.
Proof. abs(H_c(omega; theta n)) <= A_0 abs(theta)^2 (CURL-P (a)). sup abs(Psi_(theta_c)) <= 6 beta sqrt(N) abs(theta_c), sup abs(Psi+) <= 24 beta sqrt(N) abs(lambda) (4.3). So Q(theta_c) <= A_1 abs(theta_c)^2 and the mixed
term is at most (A_0 abs(d lambda) + 144 beta^2 N abs(lambda)) abs(theta_c) <= B_1 abs(theta_c) abs(lambda) for lambda_0 = 0 (abs(d lambda) <= 4 abs(lambda)). The corner value lambda_0 changes neither H_c
nor any mixed term (CURL-P (b)) nor Psi. Q(d lambda) <= - m_3 abs(lambda)^2 by 6.3. Lemma SQ in the variables (theta_c, lambda), then the definition of mu_1. QED
The class (ker d)-perp + {d lambda : lambda on the pinned sites} contains every gradient. It is all boundary fields if every closed
boundary field is a gradient (check 1044 Step 7 states this, the boundary being a 3-sphere; I did not re-prove it).
C_Q is not the classical constant: m_3 = mu_3 rho^2 is small and not a number, and mu_1 depends on S.

**6.5 Verdict on (C).** YES, existentially. The response to upper-face gradients needs no new idea: the gauge return holds
on the whole boundary (GR+), the hierarchy is grounded at one site y_1 instead of at U, and the only null direction is
the exact one. The literal cost with the extension V+ is negative on the open set P_3 for every boundary gradient
(O2-GR+), and a curl bound for Q with a non-classical constant follows there (CURL-Q). OPEN: the same on P' or P_2.

### Step 7 (done 2026-11-16T12:18:25Z, `date -u`): numeric guide

One GUIDE run was made, for Step 2 only. It is recorded in 2.5 (numeric lock from copies of the two scripts in
`/tmp/r1046.H6hjw3/scripts/`; BLAS thread variables 1; pure Python; 1.64 s). It agrees with 2.1, 2.2 and 2.3. It proves nothing.
No run was made for Steps 4, 5 or 6: POLY, EXT, HIER+, O2-GR, GR+, O2-GR+, CURL-Q, AVG and MEAN have no numeric test. No download was made.

### Step 8 (done 2026-11-16T12:18:25Z, `date -u`): marks, scope, limits, RESULT

Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit 594d6491b; checked by nobody.
One session, no subagents. Written by hand. Only this file was written (plus scratch files in `/tmp/r1046.H6hjw3/`).
Save protocol: the first tool call created the file; the plan was added in the third call, after the row text was read.

| Item | Statement | Mark |
|---|---|---|
| TAN (2.1) | a boundary move tangent to the gauge orbit, B = psi_x - Ad(omega_l) psi_y, has the gauge extension with Psi = 0; Q = H_c = 2 sum (psi_x x Ad(omega_l) psi_y) . E[N_l] | PROVED |
| CUBE-EXT (2.2) | cube, frame COUL, any b_0 >= 0, h != +-1: explicit psi, extension of class (E-FROZEN), Var = 0, Q(d lambda) = H_c = - 2 (b_0 + kappa) sin^2(gamma)(1 - c) T(theta) | PROVED (uses CUBE-COUL) |
| Cube Var of the GR extension (2.3) | Var(Psi_GR) = 2 sin^2(gamma)(1 - c){kappa T + [beta xbar - 2 kappa c (1 + c)] Lam}, exact; Q_GR >= 0 for b_0 = 0 | PROVED (uses CUBE-Z, CUBE-COUL) |
| POLY (4.1) | the Haar Laplacian maps PP_d onto its mean-zero part | PROVED |
| EXT (4.2) | every pin, every boundary field: H_c <= Q_(V_n) <= H_c + 16 e^(2 a_0) r_n^2 (sup abs(Psi_0))^2, V_n = V_0 + e^(-A) grad v_n; inf over (E-FLOW) of Q = H_c | PROVED given FLOW |
| Existence of an exact minimiser (Psi constant) | | ARGUED (not used) |
| (A), class (E-FLOW), pins P' of EXIST (4.3) | Q <= - (m_0/2) sum lambda^2 for all lambda on L, with r_n <= sqrt(m_0)/(136 beta sqrt(N) e^(a_0)) | PROVED given EXIST with K1 |
| HIER+ (4.4) | HIER with a second bounded continuous form | PROVED |
| O2-GR (4.5) | (CONN): one frame, one open pin set P_2, Q_GR(d lambda) = H_c + Var(Psi_GR) <= - m_2 sum lambda^2 for all lambda on L, plain GR extension | PROVED given LEAD-C, K7, K1 |
| (A), class (E-GR), on P' itself | Var(Psi_GR) <= m_0 sum lambda^2 on the set of row 1042 | OPEN |
| "Every admissible extension has Var above m_0 sum lambda^2" | | FAILS in class (E-FLOW), every pin (EXT) |
| EQ (5.2) | in class (E-FLOW), literal (O2) on a space of potentials follows from strict (O2-min) and implies (O2-min) | PROVED |
| AVG (5.3) | E[H_c] <= p C sum (d theta)^2 + (1 - p) A_0 abs(theta)^2 | PROVED |
| Measure of P', P_2, P_3 under the ring law | positive; no estimate; expected very small | OPEN (the expectation is ARGUED) |
| MEAN (5.4) | the mean of Hess f_H(theta)[lambda, lambda] over a torus orbit is 0 | PROVED |
| (B) an item of (W) moves | none; first failing step (N1) | the absence of a proof, not a refutation |
| GR+ (6.1) | gauge return, score and response for lambda on all pinned sites; extension V+ | PROVED |
| LEAD-C on all heads; (CONN+) (6.2) | | PROVED given LEAD-C and the graph proof of checks 1044, 1045 |
| O2-GR+ (6.3) | one frame, one open pin set P_3: Q+(d lambda) <= - m_3 sum over Y+ of (lambda_y - lambda_(y_1))^2 for every boundary lambda | PROVED given the same inputs |
| CURL-Q (6.4) | on P_3: H_c <= Q(theta) <= C_Q sum (d theta)_p^2 on (ker d)-perp + gradients | PROVED given 6.3 |
| "Every closed boundary field is a gradient" | used only to read the class of 6.4 as all boundary fields | cited from check 1044, not re-proved |
| (C) on P' or P_2 | sign of H_c for lambda not constant on U | OPEN |
| A named beta in 2.3 to 2.6; numbers for m_0, m_2, m_3; uniformity in S; the classical constant; typical pins; (N1), (N2), (N3), (O1); tilings | | OPEN, unchanged |
| U(1) (Step 3) | every statement gives 0 or the classical bound; zero gain | PROVED |

Scope of each negative or limiting statement (K8).
- "Q_GR >= 0 for b_0 = 0": the cube, frame COUL, the GR extension, pins with h != +-1 (exact, 2.3). Not for another extension: 2.2 has Q < 0 there.
- "The alternative 'Var above m_0 sum lambda^2 for every admissible extension' FAILS": class (E-FLOW) only. For (E-GR) on P' nothing is proved.
- "A small-measure (O2) gives the consumer nothing": through Lemma AVG, which is an upper bound only. No lower bound on
  E[H_c] is proved, and no theorem says the measure of the pin sets is small.
- "No item of (W) moves": no step toward (W) is proved here. This is not a proof that route (ii) cannot reach (W).
- MEAN: one frozen gauge and colour on one torus orbit; Haar mean for the lab frame. Nothing about covariant frames at other pins.
- "OPEN on P' or P_2" (4.5, 6.3): absences of proof for those sets, not refutations.
- No statement of this file excludes a curl mechanism, a stiffness or a gain for any frame, extension, coupling or pin set.

Limits.
- Nothing here is checked. A same-provider check and a cross-provider check are both open.
- Inputs used as on record: FLOW (row 1018 4.1); GR (row 1036 4.1); CUBE-Z, CUBE-COUL; CG, LEAD-C, HIER, EXIST with K1; CURL-P (a), (b);
  SQ; the graph proof of (CONN) in checks 1044 and 1045; the remainder K7. I did not re-derive them.
- K7 was written by check 1041 for the tree gauge. I use it in the coordinates H = e^eta of any gauge near 1. Its proof uses only
  d_l = lambda_l (a - Ad(e^(eta_l)) a) and the smoothness of the force covariance on the ball (C10; row 1042 3.4 used it the same way, and
  checks 1044 and 1045 accepted that). A checker should confirm this reading.
- HIER+ is HIER's induction with one more matrix. The order of the choices of r_j is as in HIER. Not checked.
- The sets P_2, P_3 are new sets. They are not P'. Each is built for one fixed cell and one beta.
- The polynomial degree 4n + 3 in EXT grows with a_0, so with the size of the cell. The extension is explicit up to the
  inverse of one finite symmetric matrix. No size-uniform statement is made.
- The order S^(-2) of mu_1 and the smallness of the measure of the pin sets are ARGUED.
- Not read: check 1044 L1-81 and L142-211; `gap-short-step-max.md` outside 4.1-4.2; `gap-sym-reg.md` outside 6.6-7.4; `gap-boundary-q.md` Steps 5-8
  except 7.3. Rows 1038 and 1011 were read in the parts named in Step 1 only.
- Repo search: none was made beyond the files of the reading list. Whether POLY, EXT or GR+ is on record elsewhere in the lane is not checked.

Corrected texts for the lead (no other file was edited).
- `parts/gap.md`, row 1042 entry: after "literal (O2) still needs an extension, since the score variance can cancel at the same
  order" add "row 1046 (unchecked): it has one; in the class of Lemma FLOW the least cost over extensions equals H_c at every
  pin (Theorem EXT, group-blind), so literal (O2) is strict (O2-min) there; with the plain site-frame extension the
  literal (O2) of row 1034 7.4 holds on an open pin set for a steep hierarchy (Theorem O2-GR), and for every boundary
  gradient, upper faces included, on another open set (Theorem O2-GR+, by the gauge return on the whole boundary); on
  the cube the extension is exact with zero variance (CUBE-EXT). The wall does not move: the pin sets have no
  measure estimate (Lemma AVG), the constant is not classical, and the sign has mean zero on torus orbits (Lemma MEAN)."
- Row 1042 7.3, first bullet: "For them hh is not bounded by 7.2 at all" should read "GR's extension does not treat them; the
  response itself returns to the pin for every boundary lambda (row 1046, Lemma GR+)".
- Row 1018 4.1: the sentence "the response equals the least cost over all flows" is PROVED as an infimum by Theorem EXT of
  row 1046 (unchecked). Existence of a minimiser stays ARGUED.

Finished: 2026-11-16T12:18:25Z (`date -u`).

RESULT: Row 1046 (Claude Fable 5.2 medium, background agent on the lead's MacBook, commit 594d6491b; written by hand, checked by nobody; one GUIDE run on the cube under the numeric lock that proves nothing). Cube first, by hand: for frame COUL every boundary gradient is tangent to the gauge orbit, so the gauge extension psi_x on the vertical links (written in closed form) has Psi = 0 and Q(d lambda) = H_c = - 2 (b_0 + kappa) sin^2(gamma)(1 - c) T(theta) exactly, for every b_0 >= 0 (Lemma TAN, Theorem CUBE-EXT, PROVED), while the GR extension has the exact variance 2 sin^2(gamma)(1 - c){kappa T + [beta xbar - 2 kappa c (1 + c)] Lam} and Q_GR >= 0 at b_0 = 0. (A) YES, PROVED: in the class of Lemma FLOW the least cost over smooth extensions equals the response at every pin and for every boundary field, with the field V_0 + e^(-A) grad v_n written (v_n a polynomial from inverting the Haar Laplacian on a finite-dimensional space, Lemma POLY) and Var(Psi) <= 16 e^(2 a_0) r_n^2 (sup abs(Psi_0))^2 (Theorem EXT; it also proves row 1018's ARGUED infimum; it is blind to the group); so at the pins P' of EXIST Q(d lambda) <= - (m_0/2) sum lambda^2 for all lambda on L once r_n <= sqrt(m_0)/(136 beta sqrt(N) e^(a_0)), and the alternative "every admissible extension has larger variance" FAILS in that class; with the plain site-frame (GR) extension the literal (O2) of row 1034 7.4 holds with a strict sign on one open pin set P_2 near pure gauge, one frame, all lambda on L, for beta below 3/2 and beta outside D (Theorem O2-GR with Lemma HIER+: in a steep hierarchy the response at a site is of order r_j times a larger size and the score variance of order r_j^2); for the GR extension on P' itself it is OPEN. (B) The consumer is the start bound (S): H_c(omega; theta n) <= Q(theta) <= C sum_p (d theta)_p^2 with a classical C at the pins that carry the ring measure, then (N3); by EXT the cost Q carries no information beyond H_c in the FLOW class (Proposition EQ), so the boundary obligation is one statement about H_c alone; a positive-measure (O2) gives the cell bound on its pin set only, and with probability p the average is bounded by p C sum (d theta)^2 + (1 - p) A_0 abs(theta)^2 (Lemma AVG), a mass term unless p is within about mu_1/A_0 of 1; the measure of the pin sets is not estimated, the constant is of order A_0^2/(m mu_1), and the sign has mean zero on every torus orbit (Lemma MEAN); no item of the wall (W) moves, and the first failing step is (N1). (C) YES existentially, PROVED: the gauge return holds on the whole boundary (Lemma GR+), so with the hierarchy grounded at one upper-face site there are one frame and one open pin set P_3 with Q+(d lambda) <= - m_3 sum over Y+ of (lambda_y - lambda_(y_1))^2 for every boundary lambda, upper faces included, and a curl bound for the cost with a non-classical constant on all gradients plus co-exact fields (Theorem O2-GR+, Corollary CURL-Q); on P' and P_2 the upper-face sign is OPEN. Compact U(1): every statement gives 0 or the classical bound, zero gain. What changed for the crux: the item "literal (O2) needs an extension" is closed positively and the upper-face gap of CURL-P is closed on a new pin set, but both are descents of F_c at special pins near pure gauge with no measure estimate, so the wall (W) does not move; route (ii) still needs (N1), (N2), (N3), the classical constant, (O1) and tilings. No negative is claimed for any class of frames. OPEN: every check of this file, a named beta in 2.3 to 2.6, numbers for m_0, m_2, m_3, the GR extension on P', the measure of the pin sets.
