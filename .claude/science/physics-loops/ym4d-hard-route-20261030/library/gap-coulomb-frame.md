# gap-coulomb-frame (row 1042)

Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit 4a2884358; checked by nobody.
Started: Mon Nov 16 11:00:33 UTC 2026 (from `date -u`).

Status: all eight steps written; the last line is the RESULT line. Finished 2026-11-16T11:29Z (`date -u`).

Note on the save protocol. The worker's first tool call read the row text in `FINISH.md`. The second call created this file.

## Plan (eight steps)

1. Read the sources: `parts/gap.md`, rows 1038, 1040, 1041, 1036 (GR, TP4, H4), 1039, `library/lattice-uhlenbeck.md`, and row 1043's reading if present. List every correction in force.
2. Define the frame: gauge condition on the pinned face, colour a, Gribov copies, measurability.
3. Cube test by hand (CUBE-H, lower face pinned): closed form of the Coulomb frame on the 2D face.
4. (A) Defect bound abs(D_l n) by the face curvature: range, constant, uniformity in S.
5. (B) Sign of H_c(omega; (d lambda) n) for lambda on L in the 4D cell at beta at least 3/2.
6. U(1) control: zero gain.
7. (C) Mixed terms and the full curl bound; what route (ii) still needs (O1, N2, N3).
8. Scope of every negative claim; marks; RESULT line.

## Step log

### Step 1 (done 2026-11-16T11:01Z, time from `date -u` at the last read): sources read; corrections in force

Read in full: `library/gap-collapse-frame.md` (row 1038), `library/gap-collapse-frame-check-opus.md` (check 1040),
`library/gap-collapse-frame-check-astra.md` (check 1041), `library/gap-boundary-q.md` (row 1036; GR, CUBE-Z, CUBE, TP, TP4, H4, MASS),
`library/prior/gap-collapse-frame-read-luna.md` (row 1039).
Read in part: `parts/gap.md` L1-40 and L125-147; `library/lattice-uhlenbeck.md` L1-45 (setting, Lemma U, Steps 1-4).
`library/prior/gap-coulomb-frame-read-luna.md` (row 1043) was not present at 11:00:56Z. It was not read.

Conventions are those of row 1036 Step 2 and row 1038 Step 1. SU(2) = unit quaternions, t = Re, s = Im. Link l = (x -> y), head y.
Gauge: omega_l -> g_x omega_l g_y^(-1). D_l n = n_x - Ad(omega_l) n_y. F_c = - log Z_c. For lambda supported on L (row 1036 4.1) and
V = (d lambda) n: Theorem GR gives the pin curve omega_eps,l = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y), Psi = sum_l lambda_y (D_l n) . N_l,
H_c(omega; (d lambda) n) = (d/d eps)^2 F_c(omega_eps) at 0 = Q(d lambda) - Var(Psi). The frame is frozen at the base pin.

Corrections in force (each one is used below).
- C1 (1040 item 1; 1041 section 9). No theorem of row 1038 closes route (ii) for a class. Negatives hold for frame TREE only.
- C2 (1040 item 3). BOTH (ii) needs beta < 3/2. For beta of 3/2 or more row 1038 proves no sign change of H_c.
- C3 (1041 section 7). (O2-min), H_c <= 0, is a necessary extension-free test. It is not a replacement of (O2).
  ONE and ONE+ are about named extensions only.
- C4 (1041 section 9). WEAK bounds by sum lambda^2, not by sum (d lambda)^2. No S^3 threshold. A full curl bound must control
  mixed terms: 2xy vanishes on the y-axis and is not at most C x^2.
- C5 (1040 item 5). LIP-TREE is proved on one face. The radius S_1 + S_2 bounds the curvature stencil, not all reads.
- C6 (1040 item 4; 1041 section 2). NOLIP excludes sets of density above 3/4 near the trivial pin, for equivariant local
  evaluation maps on invariant domains. It does not say "most pins".
- C7 (1041 section 3; 1040 item 6). On the cube the form Q(d lambda) is zero for the covariant axis frame. "Never negative
  semidefinite" must read "unless it is zero".
- C8 (1041 section 4). LEAD holds for a fixed finite cell, fixed strengths and fixed tree, with remainder constants
  6 M_3 (for H_c), 4 L_C + 8 B_C (for Var), on a ball of radius r_0 <= 1. No size-uniform constant.
- C9 (1041 section 5). BOTH needs an axis-defining link distinct from l_1 and l'. ORB is orbitwise, for frame TREE with its
  invariant axis.
- C10 (1040 Step 5). LEAD's proof uses only that a is a unit vector frozen at the base pin, and TG (c), (d).
- C11 (1041 section 8). TUNE's decrease is by acceleration: the velocity is tangent to the level set of F_c.
- C12 (1036 checks). MASS needs abs(beta_p w_p) <= b. GR's "pure gauge exactly when D n = 0" is "if". Covariant cube frames
  carry one sign per site. (O2) of row 1034 is existential: one frame, one set of pins of positive measure.
- C13 (lead, row text). Existential and universal quantifiers are kept apart. Each negative is stated for its frames,
  extensions, couplings and pin sets only.

### Step 2 (done 2026-11-16T11:24Z): the frame

All of Step 2 is PROVED by hand here unless marked. Nobody checked it.

**2.1 Lemma CG (a constant colour in any gauge; this is TG (b)-(d) of row 1038 without the tree).**
Let Gamma be the graph of pinned sites and pinned links. Let g = (g_x) be a function of the pin with values in SU(2) on the
pinned sites, a a unit vector (a function of the pin), both frozen at the base pin. Put
  H_l := g_x omega_l g_y^(-1)   (the pin in the gauge g),      n_x := Ad(g_x)^(-1) a.
Then:
 (a) D_l n = Ad(g_x)^(-1) (a - Ad(H_l) a), so abs(D_l n) = 2 abs(s(H_l) x a) <= 2 abs(s(H_l)) <= 2 abs(H_l - 1).
 (b) In the gauge g the pin curve of GR for lambda on L is H_l -> exp(- eps lambda_y a) H_l exp(eps lambda_y a), y the head of l.
     Write T_theta for the map H_l -> exp(- theta_y a) H_l exp(theta_y a) on SU(2)^(pinned links), theta a real function on the pinned sites.
     T is an action of the additive group of such theta. It keeps Haar measure. It commutes with gauge transformations
     that are rotations about a at every site.
 (c) H_c(omega; (d lambda) n) = (d/d eps)^2 F_c(T_(eps lambda) H) at eps = 0. So H_c is the Hessian at theta = 0 of f_H(theta) := F_c(T_theta H),
     evaluated on lambda. It reads the pin only through the representative H.
 (d) Every frame n has this form: take g_x with Ad(g_x) n_x = a. The gauge g is fixed by n up to rotations about a.
     If n is gauge covariant, then H, as a function of the pin, is constant on gauge orbits up to
     rotations about a at the sites, and a is fixed by the stabiliser of H (constant elements that commute with all H_l).
     Conversely, if g(omega^k) = g(omega) k^(-1) up to rotations about a, then n is covariant (direct).
Proof. (a) Ad(omega_l) n_y = Ad(omega_l g_y^(-1)) a = Ad(g_x^(-1) H_l) a. abs((1 - Ad(H)) a) = 2 abs(s(H) x a) (row 1011 7.3; check 1041 section 1).
(b) By GR the curve is omega_l -> exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y). Conjugate with g: g_x exp(- eps lambda_y n_x) g_x^(-1) = exp(- eps lambda_y a).
(c) GR (e) and the gauge invariance of F_c. (d) If n is covariant, n(omega^k) = Ad(k) n(omega), then g(omega^k) = g(omega) k^(-1) up to
rotations about a, so H(omega^k) = H(omega) up to these. If k fixes omega then Ad(k_x) n_x = n_x; in the gauge g this is
Ad(c) a = a for the constant c = g_x k_x g_x^(-1), which commutes with all H_l. QED
Reading. The words "constant colour in a gauge" do not select a class of frames: by (d) every frame is one. The
class is selected by the gauge condition. Frame TREE is the tree gauge. This row takes the Coulomb condition.

**2.2 Definition (frame COUL).** Let Gamma' be a connected set of pinned links (the face F = {x_4 = 0} of the 4D cell, or all
pinned links), V its number of sites, N its number of links, d its largest degree, o a base site.
Gauge condition: the maximal-trace (lattice Landau) functional on Gamma',
  M_omega(g) := sum over l in Gamma' of t(g_x omega_l g_y^(-1)),     g a maximiser,     H^C := the pin in the gauge g.
On a face of the 4D cell this is a Coulomb-type condition (the face is a three-dimensional slice). At a maximiser
  sum over links l out of x of s(H^C_l) - sum over links l into x of s(H^C_l) = 0   at every site x of Gamma'    (zero lattice divergence).
(Vary g_x -> e^(eps v) g_x: the derivative is - v . (sum out) + v . (sum in).)
Frame: n_x := Ad(g_x)^(-1) a for one colour a. I state which facts need which a.
- The maximiser is fixed only up to a constant c on the left (M(c g) = M(g)). So "one fixed colour a" is not defined
  on gauge classes. The class must carry a as extra data: a unit vector with a(c H^C c^(-1)) = Ad(c) a(H^C). With g_o = 1
  this is a covariant unit vector at the base site o. Examples: the axis of the Coulomb-fixed holonomy of one
  plaquette; a normalised sum of such axes. Each is defined off a null set.
- No such a exists on the pure-gauge orbit (the stabiliser argument of row 1039). At a reducible pin, a must lie on
  the common axis (CG (d)); then s(H_l) x a = 0 and the frame has D n = 0. The cube is this case (Step 3).
- A non-covariant a (a fixed vector with g_o = 1) is also used below, and is named as such. It is pin-measurable.

**2.3 Gribov copies.**
Lemma UNIQ (no copies near the pure-gauge orbit). Let eps_G := 1/(32 d V^3 sqrt(N)). If the pin has a gauge in which
abs(omega_l - 1) <= eps_G on all links of Gamma', then the maximiser of M with g_o = 1 (in that gauge) is unique, it has
abs(g_x - 1) <= V (sqrt(N) + 1) eps_G, and it is a continuous function of the pin on this set.
Proof. Work in that gauge; eps := eps_G. M(g) >= M(1) and t = 1 - abs(. - 1)^2/2 give sum_l abs(K_l - 1)^2 <= N eps^2 for K_l := g_x omega_l g_y^(-1).
So abs(g_x - g_y) <= abs(K_l - 1) + abs(omega_l - 1) <= (sqrt(N) + 1) eps, and along a path from o: abs(g_x - 1) <= delta := V (sqrt(N) + 1) eps.
Let g, g' be two maximisers with g_o = g'_o = 1. Write g'_x = e^(v_x) g_x, v_o = 0. abs(e^v - 1) = 2 sin(abs(v)/2) >= (2/pi) abs(v), so abs(v_x) <= pi delta.
phi(t) := M(e^(t v) g) has phi'(0) = phi'(1) = 0. With K_l(t) := e^(t v_x) K_l e^(- t v_y):
  phi''(t) = sum_l Re( v_x^2 K_l(t) - 2 v_x K_l(t) v_y + K_l(t) v_y^2 ) <= - sum_l abs(v_x - v_y)^2 + sum_l abs(K_l(t) - 1) (abs(v_x) + abs(v_y))^2
(the value at K = 1 is - abs(v_x - v_y)^2). abs(K_l(t) - 1) <= sqrt(N) eps + 2 pi delta <= 16 V sqrt(N) eps. With v_o = 0 and a path of at most V links,
abs(v_x)^2 <= V sum_l abs(v_x - v_y)^2, so sum_l (abs(v_x) + abs(v_y))^2 <= 2 d sum_x abs(v_x)^2 <= 2 d V^2 sum_l abs(v_x - v_y)^2. Hence
phi'' <= - (1 - 32 d V^3 sqrt(N) eps) sum_l abs(v_x - v_y)^2. This is negative unless v = 0, and it contradicts phi'(0) = phi'(1). A unique
maximiser of a continuous family on a compact space is continuous. QED
Away from this neighbourhood the maximiser need not be unique. On the cube it is unique for h != - 1 (Step 3).
Selection (ARGUED from a standard fact, not rebuilt): the set of maximisers is compact and depends upper
semicontinuously on the pin; the lexicographic minimum in fixed coordinates is a Borel selection; on the classes
with trivial stabiliser a covariant version is obtained from the canonical representative of 5.4. This is enough
for (O2), which asks for a pin-measurable frame on a set of positive measure. Nothing below uses copies: every
statement about frame COUL in this row is on the cube (closed form) or inside the neighbourhood of UNIQ.

### Step 3 (done 2026-11-16T11:24Z): the cube test by hand (lower face pinned), closed forms

All of Step 3 is PROVED by hand here unless marked. Nobody checked it. Cube and notation of row 1038 Step 3:
pinned links a = (000 -> 100), b = (000 -> 010), l_1 = (100 -> 110), l_2 = (010 -> 110); h = omega_a omega_1 omega_2^(-1) omega_b^(-1) = e^(phi u),
0 <= phi <= pi, t = cos(phi), s = sin(phi) u; Z_c = e^(b_0 t) G(t), kappa(t) = G'(t)/G(t), dF_c/dt = - (b_0 + kappa(t)).
theta_1 = lambda_100 - lambda_110, theta_2 = lambda_010 - lambda_110.

**3.1 Lemma CUBE-C (the Coulomb gauge of one plaquette, closed form).** For h != 1 and h != - 1, the maximisers of
M over the four lower sites are exactly the gauges with
  H_a = H_1 = q,   H_b = H_2 = q^(-1),   q := e^((phi/4) u')   (u' the axis of the holonomy in that gauge),
up to one constant. The maximum is 4 cos(phi/4). With g_000 = 1: u' = u, g_100 = q^(-1) omega_a, g_010 = q omega_b, g_110 = q^(-2) omega_a omega_1.
For h = 1 all H_l = 1. For h = - 1 the axis is free: a two-parameter family of copies (a null set of pins).
Proof. Let phi_i in [0, pi] be the class angles of the four factors H_a, H_1, H_2^(-1), H_b^(-1); their product has class angle
phi. The class angle is the distance from 1 on the 3-sphere, so phi <= sum phi_i. The sum of traces is sum cos(phi_i). Cos
decreases on [0, pi], so at a maximum sum phi_i = phi (lower one angle otherwise). For x + y <= pi:
cos x + cos y = 2 cos((x + y)/2) cos((x - y)/2) <= 2 cos((x + y)/2). Use it for (phi_1, phi_2), for (phi_3, phi_4), then for the two
means (their sum is phi/2): sum cos(phi_i) <= 4 cos(phi/4), with equality only for phi_i = phi/4 (cos(phi/4) > 0). Equality in
the triangle inequality with sum phi_i = phi <= pi puts the four factors on one geodesic from 1, in the same
direction: all four equal e^((phi/4) u'). The g are solved link by link; H_2 = q h^(-1) q^2 = q^(-1). QED
GUIDE (Step 3.6): trace, zero divergence and 12000 random gauges agree with this.
So frame COUL on the cube is: n_000 = a, n_100 = Ad(omega_a^(-1) q) a, n_010 = Ad(omega_b^(-1) q^(-1)) a, n_110 = Ad((omega_a omega_1)^(-1) q^2) a.
Moved to 000: u_0 = a, u_1 = Ad(q) a, u_2 = Ad(q^(-1)) a. Ad(q) is the rotation about u by phi/2.

**3.2 Defect on the cube.** Let gamma be the angle between a and u. Then abs(D_l n) = 2 sin(phi/4) sin(gamma) on each of the four links
(CG (a) with abs(s(q)) = sin(phi/4)). Sum of squares: 16 sin^2(phi/4) sin^2(gamma). Frame TREE has 2 sin(phi) sin(gamma) on one link and
0 on three: sum of squares 4 sin^2(phi) sin^2(gamma), four times larger at small phi. The defect is bounded by the curvature
of the one face plaquette: abs(D_l n) = 2 sin(phi/4) sin(gamma) <= 2 sin(phi/4), phi the class angle of U_p, and sin(phi/4) <= sin(phi) = abs(s(U_p))
for phi <= 4 pi/5. So abs(D_l n) <= 2 abs(s(U_p)) on the pins with phi <= 4 pi/5, range 1, constant 2. Near phi = pi, s(U_p) -> 0 and the
defect does not; there the bound is by abs(U_p - 1): abs(D_l n) <= 2 sin(phi/4) <= 2 sin(phi/2) = abs(U_p - 1) for all phi.

**3.3 Theorem CUBE-COUL (the response to every boundary gradient, exact).** For frame COUL on the cube, any pin with
h != +-1, any colour a at angle gamma to the axis u, c := cos(phi/2), and every lambda on the four lower sites:

  H_c(omega; (d lambda) n) = - 2 (b_0 + kappa(cos phi)) sin^2(gamma) (1 - c) [ (1 + 2 c) (theta_1^2 + theta_2^2) - 2 c theta_1 theta_2 ].

The bracket is positive definite in (theta_1, theta_2): its eigenvalues are 1 + c and 1 + 3 c, and c >= 0. So:
 (i)   a parallel to u (the only covariant choice on the cube): H_c = 0 for every lambda. D n = 0. The form is zero.
 (ii)  a not parallel to u and b_0 + kappa(t) > 0 (true for t near 1: kappa(1) > 0, row 1036 4.2):
       H_c <= - 2 (b_0 + kappa) sin^2(gamma) (1 - c) (1 + c) (theta_1^2 + theta_2^2) < 0 for every (theta_1, theta_2) != 0.
 (iii) a not parallel to u and b_0 + kappa(t) < 0: H_c > 0 for every (theta_1, theta_2) != 0. (Whether such t exist is not decided here.)
 (iv)  theta_1 = theta_2 = 0: the move is a constant on the three sites 100, 010, 110 plus a move at 000; H_c = 0.
Near the trivial pin: H_c = - (b_0 + kappa(1)) sin^2(gamma) (phi^2/4) (3 theta_1^2 + 3 theta_2^2 - 2 theta_1 theta_2) (1 + O(phi)).
Proof. Lemma CUBE-H of row 1038 (HOLDS in checks 1040 and 1041) with u_0 = a, d_1 = Ad(q) a - a, d_2 = Ad(q^(-1)) a - a. Write a = cos(gamma) u + sin(gamma) e,
e a unit vector orthogonal to u, f := u x e, psi := phi/2. Then d_1 = sin(gamma) [(cos psi - 1) e + sin(psi) f], d_2 = sin(gamma) [(cos psi - 1) e - sin(psi) f].
So s . d_i = 0: the kappa' term of CUBE-H is 0 and t'(0) = 0. With u x e = f, u x f = - e, e x f = u:
  s . (a x d_1) = sin(phi) sin^2(gamma) sin(psi) = - s . (a x d_2),     s . (d_1 x d_2) = 2 sin(phi) sin^2(gamma) (1 - cos psi) sin(psi),
  abs(theta_1 d_1 - theta_2 d_2)^2 = sin^2(gamma) [ (theta_1 - theta_2)^2 (1 - cos psi)^2 + (theta_1 + theta_2)^2 sin^2(psi) ].
CUBE-H: H_c = (b_0 + kappa) sin^2(gamma) { cos(phi) [ (theta_1 - theta_2)^2 (1 - cos psi)^2 + (theta_1 + theta_2)^2 sin^2(psi) ] - 2 sin(phi) sin(psi) [ theta_1^2 + theta_2^2 - 2 (1 - cos psi) theta_1 theta_2 ] }.
Coefficient of theta_1^2 (and of theta_2^2): 2 (1 - c) cos(phi) - 2 sin(phi) sin(psi) = 2 (1 - c) [ (2 c^2 - 1) - 2 c (1 + c) ] = - 2 (1 - c) (1 + 2 c),
using (1 - c)^2 + sin^2(psi) = 2 (1 - c), sin(phi) sin(psi) = 2 c (1 - c)(1 + c). Coefficient of theta_1 theta_2:
2 cos(phi) [ sin^2(psi) - (1 - c)^2 ] + 4 sin(phi) sin(psi) (1 - c) = 4 (1 - c) [ c cos(phi) + sin(phi) sin(psi) ] = 4 (1 - c) cos(phi - psi) = 4 c (1 - c). QED
Relation to row 1038. For a orthogonal to u this is the frame of Theorem TUNE with u_0 = a, sigma = + 1 and the tilt alpha = phi/2.
TUNE left alpha free and small. The Coulomb condition fixes it by the pin. For b_0 + kappa > 0 the two closed forms agree.
So the cube value is the mechanism of TUNE (C11): the velocity of the pin curve is tangent to the level set of F_c
(t'(0) = 0), and the acceleration lowers F_c. It is not a stiffness. It needs a colour that is not covariant on the cube.

**3.4 The cost Q(d lambda) on the cube, to leading order, with the constant chosen by the consumer.**
From LEAD (row 1038 5.1, C8, C10) in the Coulomb gauge: eta_a = eta_1 = xi, eta_b = eta_2 = - xi, xi = (phi/4) u, so [p_0 : l] eta_l = xi on all four links;
Hh_0(l, l') = (b_0 + kappa) [p_0 : l][p_0 : l'], C_0(l, l') = - kappa [p_0 : l][p_0 : l'] for l != l', C_0(l, l) = beta xbar - kappa (from row 1036 4.3 (iv)).
With lambda_l := lambda_head(l), lbar := (1/4) sum_l lambda_l, Vv := sum_l (lambda_l - lbar)^2 (four links; values lambda_100, lambda_010, lambda_110, lambda_110):
  H_c = - 16 (b_0 + kappa) abs(xi_perp)^2 Vv + O(phi^3),     Var(Psi) = 4 abs(xi_perp)^2 [ beta xbar Vv + 4 (beta xbar - 4 kappa) lbar^2 ] + O(phi^3),
with abs(xi_perp)^2 = (phi/4)^2 sin^2(gamma). (Vv = (3 theta_1^2 + 3 theta_2^2 - 2 theta_1 theta_2)/4: the first line agrees with 3.3.)
beta xbar - 4 kappa >= 0 because the variance is not negative for constant lambda. Adding a constant to lambda does not change the
boundary rotation on the cube (row 1038 3.2 (vi)). The best constant is - lbar, and then
  Q(d lambda) = 4 abs(xi_perp)^2 Vv [ beta xbar - 4 (b_0 + kappa) ] + O(phi^3).
So with b_0 = beta/2 (the lane's weight 1/2 on the face plaquette): Q(d lambda) < 0 near the trivial pin for every boundary
gradient with Vv != 0, since 2 beta + 4 kappa > beta xbar. With b_0 = 0: Q(d lambda) >= 0 to this order for this extension, since 4 kappa <= beta xbar.
Scope. This is for the extension of GR with the best constant, for a non-covariant colour, on the cube, near the
trivial pin, error constant of C8. GUIDE values at beta = 2.4 (row 1036 4.5): beta xbar = 1.2576, 4 kappa = 0.4339.

**3.5 Verdict of the cube test.**
- Frame COUL with a covariant colour is the common-sign axis frame: D n = 0, zero form (C7), the compact U(1) value.
- Frame COUL with a colour off the axis: (O2-min) holds strictly at every pin with b_0 + kappa(t) > 0 and h != +-1, for
  all boundary gradients at once, with the exact value of 3.3. The literal Q(d lambda) <= 0 holds near the trivial pin
  modulo the constant when b_0 = beta/2 (3.4). This is TUNE with the tilt fixed by the Coulomb condition.
- The same frame at pins with b_0 + kappa(t) < 0, if any, has H_c > 0 on all boundary gradients.
- Difference from frame TREE: TREE puts the whole holonomy on one link and has H_c = 0. COUL spreads it evenly, and the
  transverse parts of the four link potentials are aligned around the plaquette. A relative rotation about a lowers
  the curvature of that plaquette. This alignment is the thing to look for in the 4D cell (Step 5).

**3.6 GUIDE run (it proves nothing).** One job under the numeric lock, 2026-11-16T11:21:38Z (`date -u`), under one second, pure
Python (`python3 -I`), OPENBLAS_NUM_THREADS = OMP_NUM_THREADS = 1. The checkout is sparse and has no `scripts/`. The lock command
was run from copies of `scripts/lab_ops.py` and `scripts/automation_lock.py` taken with `git show HEAD:` into `/tmp/r1042.Kv8pjv/scripts/`;
acquire reported "acquired", release "released". Script and output: `/tmp/r1042.Kv8pjv/cube_coulomb_guide.py`, `cube_coulomb_guide.out`
(not committed). Output, in full:
- max abs error, t'(0) against 0 and t''(0) against the closed form of 3.3 (H_c = - (b_0 + kappa) t''), finite differences of
  the moved holonomy, 300 random pins, colours and lambda: 5.457e-06;
- max abs error, trace of the gauge-fixed face against 4 cos(phi/4): 1.776e-15;
- max abs lattice divergence of s(H) in the closed-form gauge: 3.220e-15;
- max over 12000 random gauges of (trace - closed-form trace): - 0.3142 (no random gauge is above the closed form).
Not run: any check of 3.4, of UNIQ, or of Steps 4 to 7. No integral was computed.

**Added to Steps 1 and 2 at 2026-11-16T11:25Z: the reading of row 1043.** `library/prior/gap-coulomb-frame-read-luna.md` (gpt-6-luna, a reading,
checked by nobody) arrived during Step 3 and was read in full. I fetched none of its sources; the citations below
are through that reading. What this row takes from it:
- The functional of 2.2 is the minimal (absolute) Landau gauge of the lattice literature: D. Zwanziger, Nucl. Phys. B 364
  (1991) 127-161, on a periodic lattice; stationary points are transverse; an absolute maximum exists by compactness
  and lies in the fundamental modular region; an orbit with two distinct maxima is exhibited there. Credit for the
  gauge condition goes to that literature. So global uniqueness is false in general, as 2.3 assumes. Lemma UNIQ is
  the elementary statement that a neighbourhood of the pure-gauge orbit has no copies (compare van Baal, Nucl. Phys. B 369
  (1992) 259-275: the interior of the fundamental region has none). I proved UNIQ here by hand; I did not find it stated
  with a constant in a source.
- Singer (Commun. Math. Phys. 60 (1978) 7-12) forbids a continuous global section over S^3 and S^4 in the continuum. The
  reading says it is not directly a no-go for a finite lattice face. This row needs only a Borel section on a set of
  positive measure, which no such theorem forbids (a tree gauge is a continuous section on a finite graph).
- Balaban, Commun. Math. Phys. 99 (1985) Theorem 2 bounds a Landau potential under multiscale regularity and axial
  hypotheses. No source read there states a pinned-face colour frame with a defect bounded by local curvature. Step 4
  below gives what I can prove, and it is not uniform in the size of the face.

### Step 4 (done 2026-11-16T11:25Z): decision (A), the defect

All PROVED by hand here unless marked. Nobody checked it.

**4.1 Theorem LIP-C (the Coulomb frame minimises the defect in mean square; range and constant written).**
Gamma' = F, a face box with sides S_1, S_2, S_3, frame COUL of 2.2 with any unit colour a (covariant or not), any maximiser. Then
 (i)   sum over l in F of abs(H^C_l - 1)^2 <= sum over l in F of abs(H_l - 1)^2 for the pin H in every other gauge (this is the definition:
       abs(H - 1)^2 = 2 (1 - t(H)));
 (ii)  sum over l in F of abs(D_l n)^2 <= 4 sum_l abs(s(H^C_l))^2 <= 4 sum_l abs(H^C_l - 1)^2 <= 4 C_F sum over plaquettes p of F of abs(U_p - 1)^2,
       C_F := (S_1 + S_2)(S_1 + 1) S_2;   and abs(U_p - 1)^2 <= 2 abs(s(U_p))^2 where t(U_p) >= 0;
 (iii) for each link, abs(D_l n) <= 2 (C_F sum over all p of F of abs(U_p - 1)^2)^(1/2).
Proof. (ii): CG (a), then (i) with the comb-tree gauge of row 1038 4.3. There abs(H^T_l - 1) <= sum over p in Sigma_l of abs(U_p - 1) with at most
S_1 + S_2 plaquettes (LIP-TREE, C5), so abs(H^T_l - 1)^2 <= (S_1 + S_2) sum over p in Sigma_l of abs(U_p - 1)^2. A plaquette lies in Sigma_l for at
most (S_1 + 1) S_2 links l: a (1, 2) or (1, 3) plaquette for at most S_1 links, a (2, 3) plaquette at x_1 = 0 for the 3-links
with larger x_2 and any x_1 (the ladders named in check 1040 Step 3). QED
Range and uniformity.
- The rule is not of fixed range. g_x reads every link of F (it is a global maximiser), and a reads the base
  site. So (L1), (L2) of Theorem NOLIP fail, and NOLIP (C6) says nothing about frame COUL. There is no conflict.
- The proved bound is in mean square over the face, with the whole face as stencil and a constant C_F that grows
  like S^3. It is not uniform in S. The same mean-square bound holds for frame TREE (it is the middle term);
  COUL is the minimiser of the left side of (i), and this proof shows no better constant for it.
- A bound sup_l abs(D_l n) <= C (sum_p abs(theta_p)^2)^(1/2) with C independent of S, on pins with small total face curvature, is the
  form of the lane's Lemma U (`library/lattice-uhlenbeck.md`: a four-dimensional box, the gauge delta a = 0 for a = log U,
  not the maximal-trace gauge, marked "not reviewed" in that file). For the three-dimensional face and the
  maximal-trace gauge it is OPEN in this row. I did not derive it.
- A bound by the curvature within a fixed distance of l, uniform in S: not proved, and I expect it to be false
  for every gauge of this kind (the Coulomb potential of a far plaquette loop decays by a power only; ARGUED).
- On the cube the defect is exact: 2 sin(phi/4) sin(gamma) on each link (3.2).

**4.2 Verdict on (A).** PROVED: for frame COUL on a face, sum abs(D_l n)^2 <= 4 C_F sum abs(U_p - 1)^2 with C_F = (S_1 + S_2)(S_1 + 1) S_2, stencil
the whole face; no copies and a continuous gauge on the neighbourhood of UNIQ. Not uniform in S. OPEN: a sup bound
with a constant independent of S (the Uhlenbeck form) for this gauge on a face. NOLIP does not apply to COUL.
The frame is in the collapsing-defect class in this sense: on the set of UNIQ, abs(D_l n) <= 2 abs(H^C_l - 1) -> 0 at the pure-gauge
orbit, for every choice of a.

### Step 5 (done 2026-11-16T11:26Z): decision (B), the sign of H_c for lambda on L in the 4D cell

All PROVED by hand here unless marked. Nobody checked it.
Setting. The lane's cell: a 4D box, all S_mu >= 2, homogeneous beta > 0, weights w_p of row 1011 3.1 (1 inside, 1/2 on a plaquette
of one 3-face, 1/4 on a plaquette of a 2-face of the cell). All boundary links are pinned. L as in GR. U := the sites in the
relative interiors of the upper faces (the pinned sites not in L). Y := L without the corner 0. Every site of Y has
a pinned link into it; 0 has none (if y != 0 lies on the face kappa and y_mu >= 1 for some mu != kappa, the link (y - e_mu, mu) lies in that
face; otherwise y = S_kappa e_kappa and the link (y - e_kappa, kappa) lies in a lower face). lambda is supported on L; lambda_0 never enters.
G := the pinned links with head in U ("ground": no lambda moves them). in(y) := the pinned links with head y.

**5.1 Lemma LEAD-C (LEAD for any gauge; the response as the Hessian of an XY energy).**
Fix a := i. For eta = (eta_l) on all pinned links write eta_l = eta_par,l i + z_l, with z_l in the plane orthogonal to i, read as a complex number.
Hh_0, K_0, C_0, Phi, M_3 as in row 1038 5.1 and check 1041 section 4 (fixed cell and beta; ball abs(eta)_2 <= r_0 <= 1). For vartheta in R^Y put
  E_z(vartheta) := (1/2) sum over l, l' of Hh_0(l, l') Re( conj(z_l) z_l' exp(i (vartheta_h(l') - vartheta_h(l))) ),    vartheta := 0 on heads outside Y.
Then for H = e^eta, abs(eta)_2 <= r_0, every theta in R^Y and every lambda in R^Y:
  abs( Hess f_H(theta)[lambda, lambda] - 4 Hess E_z(- 2 theta)[lambda, lambda] ) <= 6 M_3 abs(lambda)_2^2 abs(eta)_2^3.
At theta = 0:  4 Hess E_z(0)[lambda, lambda] = - 2 sum over l, l' of Hh_0(l, l') (lambda_l - lambda_l')^2 Re(conj(z_l) z_l') = - 2 sum over pairs of heads y, y' of W(y, y') (lambda_y - lambda_y')^2,
  W(y, y') := Re sum over l in in(y), l' in in(y') of Hh_0(l, l') conj(z_l) z_l'    (heads in U are one node with lambda = 0).
Proof. T_theta e^eta = e^(R_theta eta), where R_theta turns eta_l about i by - 2 theta_h(l): z_l -> e^(- 2 i theta_h(l)) z_l, eta_par unchanged. Hess f_H(theta)[lambda, lambda] is
(d/d eps)^2 Phi(R_(theta + eps lambda) eta). The point R_theta eta has the same norm. Now the Taylor step of check 1041 section 4 at that point:
D Phi(0) = 0, abs(D^2 Phi(eta) - Hh_0) <= M_3 r, abs(D Phi(eta) - Hh_0 eta) <= M_3 r^2/2, abs(eta') <= 2 Lambda r, abs(eta'') <= 4 Lambda^2 r, Lambda <= abs(lambda)_2. The quadratic part
is the second derivative of (1/2) Hh_0(R eta, R eta) = const + E_z(- 2 theta - 2 eps lambda). No tree and no property of the gauge is used (C10). QED
So, in any gauge in which the pin is near 1, (O2-min) at leading order is the statement: the "signed graph Laplacian" of the
weights W(y, y') is positive semidefinite, that is theta = 0 is a local maximum of F_c on the torus orbit to second order.
One site: for lambda the indicator of y, 4 Hess E_z(0) = - 4 Re Hh_0(z outside in(y), z on in(y)).

**5.2 The cube (decided).** Theorem CUBE-COUL (3.3), exact at every pin. In the terms of 5.1: Hh_0(l, l') = (b_0 + kappa)[p_0 : l][p_0 : l'], and in
the Coulomb gauge [p_0 : l] z_l is the same on the four links, so every W(y, y') >= 0. There is no ground on the cube; the
constant on {100, 010, 110} is an exact symmetry.

**5.3 Lemma HIER (an XY energy with a connected coupling graph has a non-degenerate maximum for suitable sizes).**
Let k >= 1, complex numbers b_j (1 <= j <= k) and c_ij (1 <= i < j <= k), such that for every j the list (b_j, c_1j, ..., c_(j-1)j) is not
zero. For r in (0, infinity)^k put
  E(vartheta) := sum_j r_j Re( e^(- i vartheta_j) b_j ) + sum over i < j of r_i r_j Re( c_ij e^(i (vartheta_j - vartheta_i)) ).
Then there are r and a point vartheta* with grad E(vartheta*) = 0 and Hess E(vartheta*) negative definite.
Proof. Let c_max := max abs(c_ij) (1 if all are 0), c_min the least non-zero abs(c_ij), b_min the least non-zero abs(b_j). Take
q := min(1/2, c_min/(4 c_max)) and r_1 <= b_min/(4 c_max), and always r_(j+1) <= q r_j. Then sum over i > m of r_i <= 2 q r_m.
E_j := the terms with indices <= j. E_j = E_(j-1) + r_j Re( e^(- i vartheta_j) g_j ), g_j := b_j + sum over i < j of r_i conj(c_ij) e^(i vartheta_i).
If b_j != 0: abs(g_j) >= abs(b_j) - 2 r_1 c_max >= b_min/2. If b_j = 0, let m be the least i with c_ij != 0: abs(g_j) >= r_m c_min - 2 q r_m c_max >= r_m c_min/2.
So g_j != 0 for all values of the angles. Induction on j. j = 1: E_1 = r_1 abs(b_1) cos(vartheta_1 - arg b_1), and b_1 != 0. Step: let vartheta' be a
non-degenerate maximum point of E_(j-1). The map (vartheta', vartheta_j; r_j) -> ( grad E_(j-1) + r_j grad' Re(e^(- i vartheta_j) g_j), Im(e^(- i vartheta_j) g_j) ) is smooth,
vanishes at r_j = 0, vartheta_j = arg g_j(vartheta'), and its Jacobian there is block triangular with blocks Hess E_(j-1) and - abs(g_j). By the
implicit function theorem there is a zero for small r_j > 0, and it is a critical point of E_j. Its Hessian has the
blocks A + O(r_j), r_j v, - r_j (abs(g_j) + o(1)); A + O(r_j) is negative definite, and the Schur complement
- r_j abs(g_j)(1 + o(1)) - r_j^2 v^T (A + O(r_j))^(-1) v is negative for small r_j. Take r_j small and at most q r_(j-1). QED

**5.4 Theorem EXIST (existential (O2-min) with a strict sign, in the 4D cell, for one frame built from orbit maxima).**
Hypothesis (CONN) at the coupling beta: the graph on the nodes Y and one node "ground", with an edge y ~ y' when
Hh_0(l, l') != 0 for some l in in(y), l' in in(y') (and y ~ ground when Hh_0(l, l') != 0 for some l in in(y), l' in G), is connected.
Claim. If (CONN) holds, there are a non-empty open gauge-invariant set P of pins, a number m_0 > 0, and a frame n on all
pinned sites, Borel and gauge covariant on P minus the reducible pins (a null set), such that for every pin of that
set and EVERY lambda supported on L:
  H_c(omega; (d lambda) n) <= - m_0 sum over y in Y of lambda_y^2.
The frame has abs(D_l n) <= 2 abs(H_l - 1) with H the representative below, and P can be taken inside any neighbourhood of the
pure-gauge orbit. An open set has positive Haar measure and positive measure in the law of the surrounding model.
(CONN) holds for every beta in (0, 3/2), and for every beta > 0 outside a set D that has no accumulation point in (0, infinity);
D does not meet (0, 3/2). So it holds for all but finitely many beta in [2.3, 2.6]. I cannot name one beta of that
interval at which it holds: no value of Hh_0 is computed.
Proof. (1) Order Y as y_1, ..., y_k by breadth-first search from ground. Choose a field z_G on G and patterns zeta_j on in(y_j)
such that b_j := sum over l in in(y_j), l' in G of Hh_0(l, l') conj(zeta_j,l) z_G,l' and c_ij := sum over l in in(y_i), l' in in(y_j) of Hh_0(l, l') conj(zeta_i,l) zeta_j,l' are not zero
whenever the block of Hh_0 is not zero (each is a non-zero bilinear form; finitely many proper algebraic sets are
avoided). By (CONN) and the order, the hypothesis of HIER holds. For z = z_G + sum_j r_j zeta_j, E_z of 5.1 is the E of HIER
plus a constant. HIER gives r and vartheta* with Hess E_z(vartheta*) <= - mu on R^Y, mu > 0.
(2) Let eta_l := z_l (no component along i), rho > 0, H* := T_(theta*) e^(rho eta), theta* := - vartheta*/2. By 5.1 at H = e^(rho eta):
Hess f_(H*)(0)[lambda, lambda] = Hess f_H(theta*)[lambda, lambda] <= - (4 mu rho^2 - 6 M_3 rho^3 abs(eta)^3) abs(lambda)^2 <= - 2 mu rho^2 abs(lambda)^2 for rho <= mu/(3 M_3 abs(eta)^3), rho abs(eta) <= r_0.
The Hessian is continuous in H. So there is a closed ball B around H* in SU(2)^(pinned links) with Hess f_H(0) <= - m_0 := - mu rho^2 on B.
(3) P := the set of pins with a gauge transform in the interior of B. It is open, gauge invariant and not empty. By
CG (c), a frame n = Ad(g)^(-1) i with omega^g in B has H_c(omega; (d lambda) n) = Hess f_(omega^g)(0)[lambda, lambda] <= - m_0 abs(lambda)^2.
(4) Measurable covariant choice of g (ARGUED from standard facts; not rebuilt line by line). Fix a spanning tree and
two non-tree links. On the pins whose two tree-gauge holonomies have non-parallel axes (an open set of full measure,
all irreducible), put the pin in tree gauge and turn it by the one constant that sends the first axis to i and the
second into the half plane spanned by i and + j. This canonical representative omega^ is a continuous function of
the gauge class, and omega = (omega^)^(k(omega)) with k unique up to the centre. The set {g : (omega^)^g in B} is compact and its graph is closed;
its lexicographic minimum psi(omega^) in fixed coordinates is Borel. Since omega^g = (omega^)^(g k), put g(omega) := psi(omega^) k(omega)^(-1) (site by site) and n_x := Ad(g_x)^(-1) i. The centre
acts trivially on n. So n is Borel and covariant.
(5) (CONN). Let l != l' be pinned links in one boundary plaquette p. It is their only common plaquette, and xbar_p = 1,
so K_0(l, l') = +- beta w_p. If p lies in a 2-face of the cell, its links have only boundary plaquettes (a link (x, mu) has
only boundary plaquettes exactly when two of its three transverse coordinates are on the boundary), so N_l is a
function of the pin, C_0(l, .) = 0 and Hh_0(l, l') = +- beta/4 != 0 for every beta. Otherwise w_p = 1/2, and a link of a 3-face that is
not in a 2-face has exactly one plaquette with free links, of weight 1, so at the trivial pin abs(N_l) <= beta and
C_0(l, l) <= beta^2/3 (isotropy); then abs(C_0(l, l')) <= beta^2/3 and abs(Hh_0(l, l')) >= beta/2 - beta^2/3 > 0 for beta < 3/2 (the estimate of BOTH, C2).
Edges: for a boundary link (y, nu) that is not on a coordinate axis through 0 there are mu not nu and a boundary
plaquette (y - e_mu; mu, nu) (if the link lies in the face kappa_0: take mu outside {nu, kappa_0} with y_mu >= 1; or mu = kappa_0 when y_kappa_0 = S_kappa_0 and another
transverse coordinate is on the boundary; both fail only for y = t e_nu). Its links (y - e_mu, mu) and (y, nu) have heads y and
y + e_nu. So y ~ y + e_nu, or one of them is in U and the other is joined to ground. The boundary sites other than 0, with
the boundary links off the four axes, form a connected graph: in a 3-face, the sites with two or more non-zero
face coordinates are joined to each other by links between such sites (raise zero coordinates to 1, then
lower to (1, 1, 1)), an axis site t e_nu, t >= 1, has a link to t e_nu + e_mu, and the eight faces overlap in 2-faces. U is not
empty (S_mu >= 2). So (CONN) holds for beta < 3/2.
(6) Other beta. Z_c and its derivatives in the pin at the trivial pin are entire functions of beta, and Z_c > 0 for real
beta. So each Hh_0(l, l'; beta) is real analytic on the real line. Those used in (5) are not zero on (0, 3/2), so the zeros
of each have no accumulation point in (0, infinity). D := the union over the finitely many pairs. QED
What EXIST is, and its limits (C1, C3, C13).
- Quantifiers: there EXISTS one frame and one open set of pins such that FOR ALL lambda on L the response is negative.
  This is the existential form of (O2-min) that checks 1040 and 1041 left open, now with a strict sign.
- The frame is not frame COUL. By CG (d) it is the constant colour i in the gauge that brings the pin into B. B is
  built at a strict maximum of F_c on a torus orbit (to second order). Row 1038 Theorem ORB noted such maxima for frame
  TREE without a measure; here the set is open because the maximum is non-degenerate, and all frames are admitted.
- The mechanism is that of TUNE and of 3.3 (C11): at these pins a boundary gradient rotation lowers F_c. It is not a
  stiffness and not a curl bound. It gives no statement for pins outside P, and P is a small set near the
  pure-gauge orbit whose measure is not estimated. m_0 = mu rho^2 is not written as a number.
- (O2-min) is necessary only (C3). The literal (O2), Q <= 0 with one admissible extension, is NOT proved by EXIST:
  Q(d lambda) = H_c + Var(Psi) for the extension of GR, and Var(Psi) = 4 rho^2 C_0(Lambda z, Lambda z) + O(rho^3) is of the same order as H_c.
- The selection step (4) is ARGUED. The value beta in [2.3, 2.6] is not named. The cell is fixed: nothing is uniform in S.

**5.5 Frame COUL in the 4D cell (not decided; what is proved).**
Take Gamma' = all pinned links (or the face F for lambda supported on F: all pinned links into sites of F lie in F), a covariant
colour, a pin in the neighbourhood of UNIQ, H^C = e^eta. Then eta is transverse up to third order (zero divergence of s(H^C)).
By 5.1, with z the part of eta orthogonal to a:
 (i)  Criterion. If some transverse eta has the Laplacian of W(z) positive definite on R^Y, then frame COUL has H_c < 0 for all
      lambda on L on a non-empty open set of pins. If for every transverse eta that Laplacian has a negative direction, frame
      COUL has no open set of pins near the pure-gauge orbit on which H_c <= 0 for all lambda, to second order. Neither
      alternative is decided here for any beta. The maximum point of HIER is not transverse in general, and the
      Coulomb slice is not invariant under T.
 (ii) Proposition LOOP (one site, negative, beta < 3/2). Let p = (x; mu, nu) and p_ref be two disjoint plaquettes deep in the
      face F, a_0 and xi orthogonal unit vectors, and the pin H_l = e^(rho [p_ref : l] a_0) on p_ref, e^(rho [p : l] xi) on p, 1 elsewhere. It has
      zero divergence, so for small rho it is its own Coulomb representative (the maximiser is unique in the ball
      of UNIQ and g = 1 is critical there; the proof of UNIQ applies to two critical points). Take a := the axis of
      the Coulomb-fixed holonomy of p_ref; a = a_0 at this pin and a is continuous near it. For lambda the indicator of
      y = x + e_mu + e_nu:  H_c = - 4 rho^2 sum over i in {1, 4}, j in {2, 3} of Hh_0(l_i, l_j)[p : l_i][p : l_j] + O(rho^3) <= - 16 rho^2 (beta/2 - beta^2/3) + O(rho^3) < 0
      for beta < 3/2, and on an open set of pins around it. This is the aligned plaquette of the cube.
 (iii) A positive value (ARGUED; small beta only). On three columns and three rows of (1, 2)-plaquettes deep in F take the
      loop coefficients psi = 1, 2, 2 by row, the same in each column, direction xi, and p_ref as in (ii). The 1-links then
      carry 1, 1, 0, - 2 by row and the 2-links carry -+ (1, 2, 2) on the two outer columns only. For l the middle 1-link of
      the second row and lambda the indicator of its head y: in(y) carries z only on l; the only link that shares a
      plaquette with l and carries z is the parallel 1-link one row below, with K_0 = - beta/2; the other 21 units of abs(z)
      enter through C_0 only. So H_c >= 4 rho^2 (beta/2 - 7 beta^2) + O(rho^3) > 0 for beta < 1/14. Not written: the third-order correction
      that makes the pin exactly Coulomb. At beta of 3/2 or more I have no witness of either sign for frame COUL.
 (iv) Why (iii) is the typical case (ARGUED; not a theorem). If Hh_0 were a local curl energy, c sum_p abs((d z)_p)^2, then by 5.1
      4 Hess E_z(0)[lambda, lambda] = - 2 c sum_p sum over links i, j of p of Re(conj(zeta_i) zeta_j)(lambda_i - lambda_j)^2 with zeta_i = [p : l_i] z_l_i. For a potential that
      varies slowly on the lattice scale, opposite links of a plaquette have zeta_3 near - zeta_1, and the sum is
      + 4 c sum_p abs(d lambda wedge z)_p^2 >= 0: the mass term of a rotation about a in a background with a potential
      transverse to a. It is negative only where the link potentials are aligned around plaquettes, which needs
      a potential of the size of its own curl (the cube; LOOP). In a face of side S the Coulomb potential of a
      field of strength f is of size f S. So for smooth pins in a large cell I expect H_c > 0 for frame COUL on most
      gradients. The true Hh_0 = K_0 - C_0 is not local and its entries are not known at beta >= 3/2.

**5.6 Verdict on (B).**
- Cube: decided. Frame COUL with a covariant colour gives the zero form. With a colour off the axis it gives
  H_c < 0 on all boundary gradients at every pin with b_0 + kappa(t) > 0, exact value in 3.3.
- 4D cell, existential (O2-min), one frame, one open pin set, all lambda on L: PROVED for beta < 3/2 and for all beta outside
  the set D (Theorem EXIST), with the selection step ARGUED. In particular at all but finitely many beta of
  [2.3, 2.6], none of them named. The frame is built from orbit maxima of F_c; it is not frame COUL.
- 4D cell, frame COUL: OPEN at every beta for the all-lambda statement. One-site values: negative on an open set for
  beta < 3/2 (LOOP, PROVED); positive on an open set for beta < 1/14 (ARGUED). No value at beta >= 3/2.
- Nothing here says that (O2-min) holds at almost every pin, for any frame. Row 1038 ORB and BOTH (frame TREE; beta < 3/2 for
  BOTH) and (iii) above (frame COUL; beta < 1/14; ARGUED) are the only statements against that, each for its frame.

### Step 6 (done 2026-11-16T11:28Z): compact U(1), zero gain

PROVED (each line is the U(1) reading of a statement above; nobody checked it). One axis, Ad trivial.
- CG: D n = 0 for one common axis; T_theta is the identity map; f_H is constant; H_c = 0 for every pin, gauge and lambda.
- Frame COUL exists for U(1) (the Landau gauge of the angles), and the frame it defines is the constant axis. CUBE-C holds
  with the four angles equal to phi/4. CUBE-COUL: sin(gamma) = 0, the form is zero. 3.4: xi_perp = 0, Q = 0.
- LIP-C: the left side is 0. LEAD-C: there is no z; E_z = 0. HIER's hypothesis cannot hold (all b_j, c_ij are 0), and the
  strict conclusion of EXIST is false for U(1), where H_c = 0. So EXIST is a statement about Ad != 1 only.
- Section 7: for U(1) the response to a boundary rotation depends on d theta alone, the mixed terms with gradients
  vanish identically, and the curl bound with the classical constant beta stands (row 1036 7.1). Lemma SQ is not needed.
Zero gain: no statement of this row gives compact U(1) more than its classical curl bound, and none gives SU(2) a
bound with the classical constant. The strict negative values for SU(2) (3.3, LOOP, EXIST) are descents by
acceleration at special pins. They have no U(1) form because U(1) has no direction orthogonal to its axis.
With site signs (C12) the U(1) frame is not constant; that case is row 1038 3.4 and is not repeated.

### Step 7 (done 2026-11-16T11:28Z): decision (C), mixed terms and the full curl bound

**7.1 Lemma SQ (a strict sign on gradients controls the mixed terms; PROVED, two lines).** Let q be a real quadratic form,
X and Y subspaces, with q(x) <= A abs(x)^2 on X, abs(q(x, y)) <= B abs(x) abs(y), and q(y) <= - m abs(y)^2 on Y, m > 0. Then q(x + y) <= (A + B^2/m) abs(x)^2.
Proof. q(x + y) <= A abs(x)^2 + 2 B abs(x) abs(y) - m abs(y)^2, and 2 B abs(x) abs(y) <= (B^2/m) abs(x)^2 + m abs(y)^2. QED
This is the exact answer to the remark of check 1041 (C4): 2xy has m = 0. A form that is only <= 0 on gradients, with
a kernel, gives nothing for the mixed terms unless they vanish there for another reason (they do for U(1), and
for exact gauge directions).

**7.2 Proposition CURL-P (what follows on the pin set of EXIST; PROVED given EXIST).** Cell, P, n, m_0 of 5.4; N := the number of pinned
links. For a real field theta on the pinned links let hh(theta) := H_c(omega; theta n) = (d/ds)^2 F_c(exp(s theta n) omega) at 0, a quadratic form in theta. Then:
 (a) abs(hh(theta)) <= A_0 abs(theta)_2^2, A_0 := 24 beta + 36 beta^2 N (each plaquette: abs of the second derivative of t_p at most (sum of abs(theta_l))^2; six
     plaquettes per link; Var(A') <= E[A'^2]; weights at most 1).
 (b) hh(d lambda) <= - (m_0/16) abs(d lambda)_2^2 for lambda in R^Y (abs(d lambda)^2 <= 2 . 8 . sum lambda_y^2; a boundary site has at most 8 boundary links). The corner
     value lambda_0 adds an exact gauge move at 0 (every link at 0 has tail 0 and turns about the one vector n_0), so it
     changes neither hh nor any mixed term.
 (c) For every theta = theta_c + d lambda with lambda supported on L and theta_c any field:  H_c(omega; theta n) <= (A_0 + 16 A_0^2/m_0) abs(theta_c)_2^2.
 (d) If theta_c is orthogonal to the kernel of d (the curl on boundary plaquettes), then abs(theta_c)^2 <= (1/mu_1) sum_p (d theta)_p^2, mu_1 the least
     non-zero eigenvalue of d^T d on boundary link fields. So on the space (ker d)-perp + {d lambda : lambda on L}:
       H_c(omega; theta n) <= C sum over boundary plaquettes of (d theta)_p^2,     C := (A_0 + 16 A_0^2/m_0)/mu_1.
Proof. (a) is the bound of F_c'' = - E[A''] - Var(A') along the curve; (b) is EXIST; (c) is SQ with B = A_0; (d) is the definition of mu_1. QED
This is a bound on the response H_c itself. It needs no interior extension, so (C3) does not enter.

**7.3 Does a curl bound follow for every boundary theta? No. What is missing.**
- The gradients d lambda with lambda not zero on U (the relative interiors of the upper faces) have zero curl and are not in
  the space of (d). GR does not treat them (row 1036 7.3), and neither does this row. For them hh is not bounded
  by 7.2 at all. So "for every boundary theta" is OPEN, also on P.
- The constant C is not the classical one. It is of order A_0^2/(m_0 mu_1), with m_0 = mu rho^2 small and not written as a
  number, and mu_1 of order S^(-2). The consumer wants the classical constant times a blind factor (row 1011 7.1).
- The pin set P is one small open set near the pure-gauge orbit, for one fixed cell. Its measure is not
  estimated. Nothing is known at typical pins; by 5.5 (iv) (ARGUED) the sign there is expected to be the other one
  for frame COUL.
- For frame COUL in the 4D cell (B) is not decided, so (C) has no input for that frame. On the cube, SQ applies to
  frame COUL with a colour off the axis (four links: three gradient directions, one of them an exact gauge
  direction, and one curl direction), again with a constant of order A_0^2/m and no classical constant.
What route (ii) still needs (the names are those of row 1011 7.4 and row 1034 7.4).
- (N1): a frame with the sign or the smallness at the pins that carry the measure, with the rare cells
  controlled. EXIST gives a positive-measure set only. This is unchanged.
- (N2): the controlled cancellation of the mass-like term. On P the term is negative (a descent), which is more
  than a cancellation there and says nothing elsewhere. Unchanged at typical pins.
- (N3): the gain. Not touched. A negative response on gradients is not a lower stiffness on curls.
- (O1): the bulk site frame with a conserved current. Not touched; the frames of this row are boundary frames
  that read the whole boundary, and 7.2 does not use an interior frame.
- New small items: gradients on upper faces; one frame for both cells on a shared face (tilings); a named beta.

### Step 8 (done 2026-11-16T11:28Z): marks, scope of the negatives, limits, RESULT

Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit 4a2884358; checked by nobody.
One session, no subagents. Written by hand. One GUIDE job under the numeric lock (3.6). Only this file was written.
The row's save protocol was followed with one deviation, stated at the top (the first tool call read the row text).

| Item | Statement | Mark |
|---|---|---|
| CG (2.1) | every frame is a constant colour in a gauge; abs(D_l n) = 2 abs(s(H_l) x a); H_c is the Hessian of F_c along the torus action T at the representative H | PROVED |
| Frame COUL (2.2) | maximal-trace gauge on a connected pinned set; the colour a is extra data, a covariant unit vector at the base site; none on the pure-gauge orbit; on the axis at reducible pins | definition; PROVED remarks |
| UNIQ (2.3) | no Gribov copies and a continuous gauge where a gauge has abs(omega_l - 1) <= 1/(32 d V^3 sqrt(N)) | PROVED |
| Borel covariant selection off that set (2.3, 5.4 (4)) | lexicographic minimum on a canonical representative | ARGUED (standard, not rebuilt) |
| CUBE-C (3.1) | Coulomb gauge of one plaquette: H_a = H_1 = q, H_b = H_2 = q^(-1), q = h^(1/4); maximum 4 cos(phi/4); unique for h != - 1 | PROVED |
| Cube defect (3.2) | 2 sin(phi/4) sin(gamma) on each of the four links | PROVED |
| CUBE-COUL (3.3) | H_c = - 2 (b_0 + kappa) sin^2(gamma)(1 - c)[(1 + 2c)(theta_1^2 + theta_2^2) - 2 c theta_1 theta_2], c = cos(phi/2); zero for the covariant colour; negative definite for a off the axis where b_0 + kappa > 0 | PROVED (uses CUBE-H of row 1038) |
| Cube Q with the best constant (3.4) | Q = 4 abs(xi_perp)^2 Vv [beta xbar - 4 (b_0 + kappa)] + O(phi^3); negative for b_0 = beta/2, not negative for b_0 = 0 | PROVED to leading order (uses LEAD with C8) |
| LIP-C (4.1) | sum abs(D_l n)^2 <= 4 (S_1 + S_2)(S_1 + 1) S_2 sum abs(U_p - 1)^2 on a face; stencil the whole face; not uniform in S | PROVED |
| (A) a sup bound with a constant independent of S for COUL on a face | the Uhlenbeck form | OPEN |
| (A) NOLIP and COUL | NOLIP's hypotheses fail for COUL; no conflict | PROVED (by inspection of (L1), (L2)) |
| LEAD-C (5.1) | Hess f_H(theta) = 4 Hess E_z(- 2 theta) up to 6 M_3 abs(lambda)^2 abs(eta)^3, any gauge; XY energy E_z | PROVED (fixed cell; C8) |
| HIER (5.3) | connected coupling graph: sizes r exist with a non-degenerate maximum | PROVED |
| EXIST (5.4) | 4D cell, (CONN): one frame, one open pin set, H_c <= - m_0 sum lambda^2 for all lambda on L | PROVED given step (4); step (4) ARGUED |
| (CONN) for beta < 3/2 and for beta outside a set D without accumulation point | | PROVED (graph connectivity sketched in (5)) |
| (B) at one named beta of 2.3 to 2.6 | all but finitely many beta there, none named | OPEN as a named value |
| (B) for frame COUL in the 4D cell, all lambda | criterion 5.5 (i) | OPEN, every beta |
| LOOP (5.5 (ii)) | frame COUL, one site, H_c < 0 on an open set, beta < 3/2 | PROVED |
| 5.5 (iii) | frame COUL, one site, H_c > 0 on an open set, beta < 1/14 | ARGUED |
| 5.5 (iv) | smooth pins in a large cell: the mass term abs(d lambda wedge z)^2, positive | ARGUED (model Hessian; not a theorem) |
| Literal (O2), Q <= 0 with an admissible extension, 4D cell | | OPEN |
| U(1) (Step 6) | every statement gives 0; zero gain | PROVED |
| SQ (7.1) | a strict sign on gradients controls the mixed terms, constant A + B^2/m | PROVED |
| CURL-P (7.2) | on P: H_c(omega; theta n) <= C sum (d theta)_p^2 on (ker d)-perp + {d lambda, lambda on L}, C = (A_0 + 16 A_0^2/m_0)/mu_1 | PROVED given EXIST |
| (C) a curl bound for every boundary theta | upper-face gradients not covered | OPEN |
| (C) the classical constant; typical pins; (N1), (N2), (N3), (O1) | | OPEN, unchanged |

Scope of each negative or limiting statement (C13).
- "The form is zero for frame COUL with a covariant colour": the cube only (all its pins are reducible).
- "H_c > 0 on all gradients where b_0 + kappa(t) < 0": the cube, frame COUL with a colour off the axis; no such pin is exhibited.
- "Q >= 0 to leading order for b_0 = 0": the cube, frame COUL, the extension of GR with any constant, near the trivial pin.
- "Not uniform in S": the proved bound LIP-C. No lower bound on the defect of COUL is proved.
- "EXIST does not give (O2), a classical constant, typical pins or upper faces": these are absences of proof, not refutations.
- "H_c > 0 for frame COUL": one lambda, an open set near one pin, beta < 1/14, ARGUED. 5.5 (iv) is a model statement.
- No statement of this row excludes a curl mechanism for any class of frames, at any coupling.

Limits.
- Nothing here is checked. A same-provider check and a cross-provider check are both open.
- EXIST rests on LEAD's Taylor step (C8, C10), on the estimate abs(C_0) <= beta^2/3 of BOTH, on the analyticity of Hh_0 in beta, and on
  the graph fact in (5), which is written as a sketch. Its Borel selection is ARGUED. m_0, mu, rho, D are not numbers.
- CUBE-COUL rests on CUBE-H and CUBE-Z of rows 1036 and 1038. The sign of b_0 + kappa(t) away from t = 1 is not known to me.
- 3.4 uses the constants of the cube from row 1036 4.3 and LEAD without a written error constant beyond C8.
- Frame COUL is treated on the cube, and in the 4D cell only inside the neighbourhood of UNIQ and at one-site level.
- Lemma U of `library/lattice-uhlenbeck.md` was read in its statement and first steps only. It is not used in a proof.
- Row 1043's sources were not fetched by me. Zwanziger, van Baal, Singer and Balaban are cited through that reading.
- Tilings, upper faces, non-homogeneous strengths and typical pins are not treated.

Corrected texts for the lead (no other file was edited).
- `parts/gap.md`, the row 1038 entry: after "(O2-min) is a necessary extension-free test only" add "row 1042 (unchecked): the
  existential 4D (O2-min) for lambda on L holds with a strict sign for one frame on one open pin set near pure gauge,
  for beta below 3/2 and for all beta outside a set without accumulation point (Theorem EXIST; the frame sits at
  non-degenerate maxima of F_c on torus orbits; selection ARGUED; no beta of 2.3 to 2.6 named); on the cube the
  Coulomb frame with a colour off the axis is TUNE with tilt phi/2 and has H_c negative definite where b_0 + kappa > 0
  (Theorem CUBE-COUL), and it is the zero form for the covariant colour; for the Coulomb frame in the 4D cell the
  all-lambda statement is OPEN; a strict sign on gradients controls mixed terms (Lemma SQ) but gives no classical
  constant, no typical pins and no upper-face gradients."
- Row 1038's line "the class 'collapsing defect' has this one known member": by Lemma CG every frame is a constant colour
  in some gauge; the classes are gauge conditions.

RESULT: Row 1042 (Claude Fable 5.2 medium, background agent on the lead's MacBook, commit 4a2884358; written by hand, checked by nobody; one GUIDE run under the numeric lock that proves nothing; row 1043's reading used, its sources not fetched). Frame: every frame is a constant colour in some gauge (Lemma CG), so the class is the gauge condition; frame COUL takes the maximal-trace (lattice Landau, Coulomb-type on a face) gauge on a connected pinned set with a colour a that must be carried as extra data (a covariant unit vector at the base site; none on the pure-gauge orbit; on the axis at reducible pins); no Gribov copies and a continuous gauge where some gauge has abs(omega_l - 1) <= 1/(32 d V^3 sqrt(N)) (Lemma UNIQ, PROVED), a Borel selection elsewhere (ARGUED). (A) PROVED on a face: sum abs(D_l n)^2 <= 4 (S_1 + S_2)(S_1 + 1) S_2 sum_p abs(U_p - 1)^2, stencil the whole face, not uniform in S (Theorem LIP-C); NOLIP's hypotheses fail for COUL, so there is no conflict; a sup bound with a constant independent of S is OPEN. Cube, by hand first: the Coulomb gauge of the pinned plaquette is the even split H_a = H_1 = q, H_b = H_2 = q^(-1), q = h^(1/4) (Lemma CUBE-C), the defect is 2 sin(phi/4) sin(gamma) on each link, and exactly H_c = - 2 (b_0 + kappa(cos phi)) sin^2(gamma) (1 - c) [(1 + 2c)(theta_1^2 + theta_2^2) - 2 c theta_1 theta_2], c = cos(phi/2) (Theorem CUBE-COUL): the zero form for the covariant colour (the U(1) value), negative definite on all boundary gradients for a colour off the axis wherever b_0 + kappa > 0; it is Theorem TUNE with the tilt phi/2 fixed by the gauge, a descent by acceleration and not a stiffness; with the best constant Q(d lambda) < 0 near the trivial pin for b_0 = beta/2 and Q(d lambda) >= 0 to leading order for b_0 = 0. (B) 4D cell: the response is the Hessian of an XY energy on the torus orbit (Lemma LEAD-C), and existential (O2-min) is PROVED with a strict sign, one frame, one non-empty open set of pins near pure gauge, H_c <= - m_0 sum lambda^2 for every lambda on L, for every beta below 3/2 and every beta outside a set without accumulation point, hence at all but finitely many beta of 2.3 to 2.6, none of them named (Theorem EXIST with Lemma HIER; the frame sits at non-degenerate maxima of F_c on torus orbits and is not frame COUL; its Borel selection is ARGUED; m_0 is not a number); for frame COUL in the 4D cell the all-lambda statement is OPEN at every beta, with one-site values negative on an open set for beta below 3/2 (Proposition LOOP, PROVED) and positive for beta below 1/14 (ARGUED), and an ARGUED expectation of a positive mass term abs(d lambda wedge z)^2 at smooth pins. (C) A strict sign on gradients controls the mixed terms, q(x + y) <= (A + B^2/m) abs(x)^2 (Lemma SQ, the answer to the 2xy remark), so on the pin set of EXIST H_c(omega; theta n) <= C sum_p (d theta)_p^2 on the fields (ker d)-perp + {d lambda, lambda on L} with C = (A_0 + 16 A_0^2/m_0)/mu_1, A_0 = 24 beta + 36 beta^2 N (Proposition CURL-P); a curl bound for every boundary theta does NOT follow (upper-face gradients are not covered), C is not the classical constant, and the pin set is one small open set of unestimated measure. Compact U(1): every statement gives 0, zero gain. What changed for the crux: the existential 4D (O2-min) that checks 1040 and 1041 left open is now settled positively for generic beta, but by a descent of F_c at special pins near pure gauge and not by a stiffness, so it does not move the wall (W); route (ii) still needs (N1) the sign or smallness at the pins that carry the measure, (N2), (N3), the classical constant, upper-face gradients, and (O1) is untouched; no negative claim is made for any class of frames. OPEN: the literal (O2) with an extension in the 4D cell, frame COUL in the 4D cell, a named beta in 2.3 to 2.6, a size-uniform defect bound, and every check of this file.
