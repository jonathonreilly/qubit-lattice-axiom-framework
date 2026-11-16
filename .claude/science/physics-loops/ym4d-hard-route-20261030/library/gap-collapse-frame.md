# Gap: collapsing-defect frames and non-stationary pins at the pinned boundary (row 1038)

Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit f3506eec4; checked by nobody.
Started: 2026-11-16T10:07Z. Status: all eight steps written; RESULT line at the end.

## 0. Plan (working memory; one step per response)

1. Read `parts/gap.md`, `library/gap-boundary-q.md`, both checks, `library/gap-sym-reg.md` 7.3-7.4, and the luna reading file if present. Record the exact definitions (Q, H_c, Var(Psi), GR, SIGN, MASS, CUBE, O1, O2, N1, LOC) and the corrections.
2. Literature first: Balaban axial/Landau gauge in blocks, Uhlenbeck gauge, lattice bounds abs(D n) <= C * curvature. Record what is used, with credit.
3. Cube test by hand: lower face pinned, frame transported from one base corner, near the trivial pin. U(1) control.
4. Decision (A) LIP: prove with r and C_r, or prove no such rule exists. Uniform or growing range for the consumer.
5. Decision (B): Q(d lambda) to leading order in the defect; exact (O2) or weak form; what the consumer needs; (N1).
6. Decision (C): non-stationary pin, quadratic form with cross terms M(b); negative semidefinite at one explicit pin or not.
7. Optional small numeric guide run under numeric-lock (refute or guide only).
8. Marks table and the RESULT line.

## Step log

### Step 1 (done 2026-11-16T10:21:12Z): sources read; definitions and corrections fixed

Read in full: `library/gap-boundary-q.md` (row 1036), `library/gap-boundary-q-check-astra.md`, `parts/gap.md`.
Read in part: `library/gap-boundary-q-check-opus.md` (outline, the scope note L143, the quantifier text L149-157);
`library/gap-sym-reg.md` L28-43 and 7.1-7.4; `library/gap-pinned-cell-gauge-max.md` 7.1-7.4 (Lemma FR, (N1)-(N3)) and 4.6;
`library/gap-aligned-frame.md` 7.1 (the consumer); `library/a1-balaban.md` 3.6 (the lane's port of Balaban's axial gauge).
`library/prior/gap-collapse-frame-read-luna.md` (row 1039) was not present at 10:07Z and at 10:20Z. It was not read.

Conventions are those of row 1036 Step 2. SU(2) = unit quaternions, su(2) = Im H = R^3, t = Re, s = Im. Link l = (x -> y).
Gauge: U_l -> g_x U_l g_y^(-1). D_l n = n_x - Ad(omega_l) n_y. Cell action A = sum_p beta_p w_p t_p, all plaquettes of the cell.
F_c = - log Z_c. For a pinned link, N_l = Im(omega_l S_l) and E[N_l] is the gradient of F_c in the pin.
Theorem GR (row 1036 4.1; HOLDS in both checks): for lambda supported on L and V = (d lambda) n,
 A(e^(eps V)(U, omega)) = A(U, omega_eps), omega_eps = (W_l(eps) omega_l), W_l = exp(- eps tau_l n_x) exp(eps tau_l Ad(omega_l) n_y), tau_l = lambda_y;
 Psi_(d lambda) = sum_l tau_l (D_l n) . N_l; Q(d lambda) = - E[(d/d eps)^2 A(U, omega_eps)]; H_c = (d/d eps)^2 F_c(omega_eps) = Q(d lambda) - Var(Psi_(d lambda)).
Corrections used here (from the two checks).
- MASS: hypothesis abs(beta_p w_p) <= b, and abs(beta_p w_p) on the right side.
- GR reading: lambda_head D_l n = 0 on the pinned links is sufficient for a pure gauge move. It is not necessary.
- A covariant cube frame has zero cost only with one common site sign.
- (O2) of row 1034 is existential: one frame, a set of pins of positive measure.
- Turning a pin-only vector on a free link does not change Q (astra comparison item 7).
- Boundary frame values are frozen at the base pin when the move is defined (astra L74-77).
Two facts that this row uses again and again.
- (F1) Q(d lambda) - H_c = Var(Psi) >= 0 always. So Q(d lambda) <= 0 needs H_c <= - Var(Psi).
- (F2) The extension inside is the consumer's choice. Every extension gives a bound >= H_c (Lemma FLOW).
  So the statement without any extension is: H_c(omega; (d lambda) n) <= 0. I call it (O2-min).

### Step 2 (done 2026-11-16T10:21:12Z): literature first

Nothing was downloaded. No paper text is in the repository. Citations below are RECALLED unless a lane file is named.
- **Balaban, axial gauge in a block.** T. Balaban, Commun. Math. Phys. 99 (1985) 75-102, Lemma 1 (pp. 79-80) and
  (1.43)-(1.54): in axial gauge on a block, a link is a product of conjugated plaquettes that fill its rectangle with
  the coordinate tree, at most (d - 1)(L - 1) of them. Source in the lane: `library/a1-balaban.md` 3.6 (a port, with
  page numbers). I rebuild the one inequality I use (Lemma LAD in Step 4). The bound has range of the order of the block
  side. It is not a uniform-range bound.
- **Balaban, Landau gauge.** The same paper (its title names regular configurations and gauge fixing conditions) and
  Balaban's paper on the variational problem and background fields, Commun. Math. Phys. 102 (1985) 277-309 (RECALLED;
  volume and pages not verified in this row): small-field configurations are put in a Landau-type gauge by a
  minimisation over a block, with estimates by the field strength. The gauge is a non-local function of the field.
  Not used in a proof here.
- **Uhlenbeck's gauge.** K. Uhlenbeck, Commun. Math. Phys. 83 (1982) 31-42 (RECALLED): on a ball with small L^(n/2)
  curvature there is a Coulomb gauge with the W^(1,p) norm of A bounded by C times the L^p norm of F. The gauge solves an elliptic
  problem. It is non-local, and the bound is in integral norms, not pointwise per link.
- **Lattice bounds of the form abs(D n) <= C times curvature.** In the lane: Lemma FR of row 1011 7.3 is the opposite
  direction (every frame has sum abs(D n)^2 >= NA(omega)/6). Check 1037 (G1) and astra item 6 give abs(D_l n) <= 2 abs(s(H_l))
  for a frame transported from one base point, H_l the holonomy of a loop of the size of the face. I know no
  published lattice bound with a range independent of the block. Theorem NOLIP (Step 4) shows why.
- Reading of all three sources: the potential is bounded by the field strength only after a gauge choice that reads a
  whole block. That is the same as a frame transported in the block. So the literature supplies the frame of check 1037 (G1),
  with a range that grows with the block, and nothing with a fixed range.

### Step 3 (done 2026-11-16T10:22:28Z): the cube test by hand (lower face pinned)

All of Step 3 is PROVED by hand here unless marked. Nobody checked it.
Cube of row 1036 4.2. Lower sites 000, 100, 010, 110. Pinned links a = (000 -> 100), b = (000 -> 010), l_1 = (100 -> 110),
l_2 = (010 -> 110). Holonomy at 000: h = omega_a omega_1 omega_2^(-1) omega_b^(-1), t = t(h), s = s(h). Z_c = e^(b_0 t) G(t) (CUBE-Z), G > 0 on [-1, 1].
Put kappa(t) := G'(t)/G(t), so F_c = - b_0 t - log G(t), dF_c/dt = - (b_0 + kappa(t)), and kappa(1) is the kappa of row 1036.
A pin is stationary for F_c exactly when (b_0 + kappa(t)) s = 0.
Frame vectors moved to 000: u_0 = n_000, u_1 = Ad(omega_a) n_100, u_2 = Ad(omega_b) n_010, d_i = u_i - u_0. For lambda on the lower
sites: theta_1 = lambda_100 - lambda_110, theta_2 = lambda_010 - lambda_110, v = theta_1 d_1 - theta_2 d_2.

**3.1 Lemma CUBE-H (the response to a boundary gradient, any pin, any frame, closed form).**

  H_c(omega; (d lambda) n) = (b_0 + kappa(t)) { t |v|^2 + 2 s . [ - theta_1^2 u_0 x d_1 + theta_2^2 u_0 x d_2 + theta_1 theta_2 d_1 x d_2 ] } - kappa'(t) (s . v)^2.

It does not contain n_110, and it does not contain lambda_000.
Proof. The move is omega_l -> exp(eps (lambda_x - lambda_y) n_x) omega_l on the four pinned links. Conjugate to 000:
h(eps) = exp(eps (lambda_000 - lambda_100) u_0) exp(eps theta_1 u_1) h exp(- eps theta_2 u_2) exp(- eps (lambda_000 - lambda_010) u_0), and
t(h(eps)) = Re( exp(eps (theta_2 - theta_1) u_0) exp(eps theta_1 u_1) h exp(- eps theta_2 u_2) ). With Re(u q) = - u . Im q and
Re(u u' q) = - (u . u') Re q - (u x u') . Im q for imaginary u, u':
 t'(0) = - s . v,
 t''(0) = - t |v|^2 - 2 s . [ - theta_1^2 u_0 x d_1 + theta_2^2 u_0 x d_2 + theta_1 theta_2 d_1 x d_2 ]
(the bracket uses u_0 x u_i = u_0 x d_i and u_0 x u_1 - u_0 x u_2 + u_1 x u_2 = d_1 x d_2). F_c is a function of t, so
H_c = (dF_c/dt) t'' + (d^2 F_c/dt^2) t'^2. QED
Checks. d_1 = d_2 = 0 gives 0. The trivial pin gives (b_0 + kappa) |theta_1 d_1 - theta_2 d_2|^2, which is row 1036 4.3 (iii) for the
indicator of 110. GUIDE (Step 7): the formulas for t' and t'' agree with finite differences in 200 random cases.

**3.2 The test asked for: the frame transported from the corner 000.**
n_000 = a, n_100 = Ad(omega_a)^(-1) a, n_010 = Ad(omega_b)^(-1) a, n_110 = Ad(omega_a omega_1)^(-1) a, with a any unit vector (it may be a
function of the pin). Then D n = 0 on a, b, l_1, and D_(l_2) n = Ad(omega_b)^(-1) (a - Ad(h)^(-1) a), abs(D_(l_2) n) = 2 abs(s x a). And:
 (i)   H_c(omega; (d lambda) n) = 0 for every pin and every lambda (3.1 with d_1 = d_2 = 0; or: the pin curve of GR is h -> e^(- eps lambda_110 a) h e^(eps lambda_110 a));
 (ii)  Q(d lambda) = Var(Psi_(d lambda)) = lambda_110^2 beta^2 Var_omega( (D_(l_2) n) . Im(omega_(l_2) R_2) ), R_2 the side staple of l_2 (GR (c), (e); the
       lower staple is not random);
 (iii) 0 <= Q(d lambda) <= 4 beta^2 lambda_110^2 abs(s x a)^2, and Q(d lambda) > 0 when lambda_110 != 0 and s x a != 0;
 (iv)  near the trivial pin, Q(d lambda) = 4 (beta xbar - kappa) lambda_110^2 abs(s x a)^2 (1 + o(1)), with beta xbar - kappa > 0
       (row 1036 4.3 (iv) with one delta, and continuity of the law in the pin). GUIDE value (row 1036 4.5): 1.149 at beta = 2.4.
 (v)   The direct term and the force term of GR (d), to leading order: direct = (beta xbar + b_0) abs(D n)^2,
       force = - (b_0 + kappa) abs(D n)^2. The force term removes the whole stiffness of F_c and leaves the variance.
 (vi)  For lambda with lambda_110 = 0 the move is a pure gauge move: Psi = 0, Q = 0, H_c = 0.
Proof of (iii). abs(Im q) <= 1. For the strict sign: for fixed vertical links, R_2 runs over SU(2) with a positive density
when the top link over l_2 runs over SU(2); D . Im(omega R) is not constant in R when D != 0. QED
Proof of (v). At the trivial pin e_l = beta xbar + b_0. c = n x D n, abs(c) = abs(D n) to leading order, and f_l is the gradient of
F_c = F_c(1) + (1/2)(b_0 + kappa) abs(eta)^2 + ..., h = e^eta; with c = - 2 eta_perp (Step 5, proof of LEAD) the term 2 c . f is - (b_0 + kappa) abs(D n)^2. QED
Verdict of the test.
- Exact (O2) in the literal form Q(d lambda) <= 0: FAILS on the cube for this frame at every pin with s x a != 0. The form
  lambda -> Q(d lambda) is positive semidefinite of rank one.
- The weak form holds, with delta(pin) = 4 beta^2 abs(s x a)^2 <= 4 beta^2 abs(s(h))^2, which tends to 0 at pure gauge.
- (O2-min) holds with equality: H_c = 0. Adding the constant - lambda_110 to lambda does not change the boundary rotation and
  gives Q = 0 by (vi). So the best bound of the consumer is 0. This is the U(1) value. There is no gain and no loss.
- A covariant choice of a on the cube is +-s/abs(s) (stabiliser of the pin). Then s x a = 0 and everything is 0. This is the
  common-sign case of the checks.

**3.3 Theorem ONE (cube; the literal form is never negative semidefinite).** Any pin, any unit vectors n on the four
lower sites. For lambda = 1 on the four lower sites:

  Q(d 1) = E[Psi_1^2] = beta^2 Var_omega( sum over the four pinned l of (D_l n) . Im(omega_l R_l) ),   R_l the side staple of l,

and Q(d 1) > 0 unless D_l n = 0 on all four pinned links. So lambda -> Q(d lambda), cross terms M(b) included, is negative
semidefinite only when D n = 0 on the four links, and then it is zero.
Proof. d lambda = 0 on the pinned links, so the pin does not move and H_c = 0. V rotates the vertical link out of z by the
fixed vector n_z. It is a fixed field on free links, so E[V f] = - E[f Psi] and Q = - E[V Psi] = E[Psi^2], E[Psi] = 0.
Psi = sum_l (D_l n) . N_l (GR (c)), and the lower staple gives a constant. For fixed vertical links the map from the four
top links to (R_l) is a bijection of SU(2)^4, and the density is positive. If the variance is 0 then Psi is constant
in each R_l, so D_l n = 0. If the form is negative semidefinite then Q(d 1) = 0, so D n = 0, so every move is a pure
gauge move and the form is 0. QED
Remark. Theorem ONE is about the extension that GR fixes (the free link out of z turns with lambda_z n_z). The consumer may
add a constant to lambda (F2). So Theorem ONE refutes the literal form of (O2) and not (O2-min). Step 6 uses both.

**3.4 Compact U(1) on the cube.** With one common axis, D n = 0 and every value of Step 3 is 0. Zero gain. With site
signs sigma_z (covariance allows them, astra item 8) the frame gradient is not a gradient: the holonomy angle moves by
eps (theta_1 (sigma_100 - sigma_000) - theta_2 (sigma_010 - sigma_000)), and H_c = (d^2 F_c/d phi^2) times its square. There is no force term (u_0 x d = 0).

**Added to Step 2 at 2026-11-16T10:23:24Z: the reading of row 1039.** `library/prior/gap-collapse-frame-read-luna.md` (gpt-6-luna, a
reading, checked by nobody) arrived at 10:22Z and was read in full. It agrees with Step 2 and corrects one point:
Uhlenbeck's bound has a lattice form in the lane, `library/lattice-uhlenbeck.md` (a Coulomb gauge on a box with
sup abs(a) <= C_U times the total L^2 norm of the plaquette logarithms, C_U independent of the side). It is a box-wide
hypothesis and a gauge-fixed potential. Its other findings: the finite-box axial bound (Sussman and Alpoge, with
Claude and Codex, CA-I Lemma 4.12, after Balaban) loses the box diameter; Balaban CMP 99 Theorem 2 bounds a potential
under block-average hypotheses; no source read states a covariant frame with a defect bounded by curvature at a
range uniform in the cell. Its stabiliser argument at the trivial pin is checked here: at the pin 1 every constant g
fixes the pin, covariance gives n = Ad(g) n for all g, and no unit vector has that property. It is correct, and it
says nothing off the pure-gauge orbit. Theorem NOLIP below treats the punctured neighbourhood.

### Step 4 (done 2026-11-16T10:23:24Z): decision (A), LIP

All PROVED by hand here unless marked. Nobody checked it.

**4.1 The transported frame and its tree gauge (definitions; Lemma TG).**
Let Gamma be the graph of pinned sites and pinned links (connected), o a base site, T a spanning tree. For a pinned site x
let P_x be the product of the pin along the tree path from x to o (omega_l for a step along l, omega_l^(-1) against it). Let a(omega) be
a unit vector, covariant at o (a -> Ad(g_o) a), frozen at the base pin. Frame TREE: n_x = Ad(P_x) a.
For a pinned link l = (x -> y) put H_l = P_x^(-1) omega_l P_y, the holonomy at o of the fundamental loop of l. H_l = 1 on tree links.
Lemma TG. (a) n is gauge covariant and pin-measurable. (b) D_l n = Ad(P_x)(a - Ad(H_l) a), so D n = 0 on tree links and
abs(D_l n) = 2 abs(s(H_l) x a) <= 2 abs(s(H_l)). (c) In the gauge g_x = P_x^(-1) the pin is H (1 on the tree), the frame is the
constant a, and the move (d lambda) n is the fixed-colour move (d lambda) a. (d) The pin curve of GR is, in that gauge,
H_l -> exp(- eps lambda_y a) H_l exp(eps lambda_y a); with eta_l := log H_l it is eta_l -> the rotation of eta_l about a by the angle - 2 eps lambda_y.
Proof. P_x -> g_x P_x g_o^(-1). (b): Ad(omega_l) n_y = Ad(omega_l P_y) a = Ad(P_x H_l) a; abs((1 - Ad(H)) a) = 2 abs(s(H) x a) (row 1011 7.3).
(c), (d): W_l omega_l = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y) = P_x exp(- eps lambda_y a) H_l exp(eps lambda_y a) P_y^(-1). Ad(e^(phi a)) is the
rotation about a by 2 phi. QED
Reading. A transported frame is the fixed colour a in the axial (tree) gauge of Balaban. Its boundary gradients are the
fixed-colour gradients of row 1011 4.4 at the tree-gauge pin. The class "collapsing defect" has this one known member.

**4.2 Lemma LAD (ladder form of the lattice Stokes bound; rebuilt, after Balaban CMP 99 Lemma 1).**
Let p_1, ..., p_m be a row of plaquettes, p_j and p_(j+1) sharing one link (a ladder), and gamma its boundary loop based at
a corner. Then the holonomy of gamma is a product of m factors c_j U_(p_j)^(+-1) c_j^(-1), and abs(H_gamma - 1) <= sum_j abs(U_(p_j) - 1).
If a loop is the product of the loops of two ladders with a common base path, the same holds with both sums.
Proof. Induction on m: the loop of m plaquettes is the loop of m - 1 followed by the lasso of p_m; the shared rung
cancels. For unit quaternions abs(u v - 1) <= abs(u - 1) + abs(v - 1), abs(c u c^(-1) - 1) = abs(u - 1), abs(u^(-1) - 1) = abs(u - 1). QED

**4.3 Theorem LIP-TREE (LIP holds with a range of the order of the face; r and C written).**
Pinned face F = a box with sides S_1, S_2, S_3 in {x_4 = 0}, o its corner 0, T the comb tree (all direction-1 links; the
direction-2 links with x_1 = 0; the direction-3 links with x_1 = x_2 = 0). For every link l of F there is a set Sigma_l of at most
S_1 + S_2 plaquettes of F (one ladder in the plane (1, mu) from l back to x_1 = 0, and for mu = 3 one more ladder in the plane
(2, 3) back to x_2 = 0) such that frame TREE has, at every pin,

  abs(D_l n) <= 2 abs(s(H_l)) <= 2 abs(H_l - 1) <= 2 sum over p in Sigma_l of abs(U_p - 1),

and  abs(D_l n) <= 2 sqrt(2) sum over p in Sigma_l of abs(s(U_p))  on the open set of pins with t(U_p) > 0 on F.
So LIP holds with r = S_1 + S_2 and C_r = 2 sqrt(2), on a full neighbourhood of the pure-gauge orbit (where a is defined).
Proof. TG (b); abs(s(H)) <= abs(H - 1); the fundamental loop of l is the loop of the ladders named, so LAD applies; for t >= 0,
abs(U - 1)^2 = 2 (1 - t) <= 2 (1 - t^2) = 2 abs(s)^2. QED
Limits. (i) It is one construction, not one rule at every site: the rule at x reads the tree path to o. (ii) The sum
has up to S_1 + S_2 terms. The defect is bounded by the curvature of a strip as long as the face, not by the curvature
near l. (iii) a must be supplied: a covariant unit vector at o, for instance the axis of a plaquette at o, defined
where that plaquette is not central. It is not defined on the pure-gauge orbit (the stabiliser argument).
(iv) The whole boundary of the 4D cell needs a tree on all faces. The same proof works for any tree whose
fundamental loops bound ladders. It is not written here.

**4.4 Theorem NOLIP (no rule of fixed range collapses on most pins near pure gauge).**
Setting. Gamma as in 4.1. A frame rule n, defined on a set of pins. Sites x, x' and a set N of sites with x in N such that
 (L1) n_x reads only pinned links with both ends in N;
 (L2) n_x' reads no pinned link with both ends in N;
 (L3) n is covariant under gauge transformations that are constant on N.
Let k be the length of a path pi in Gamma from x to x'. For eps > 0 let U_eps be the set of pins with abs(omega_l - 1) < eps on every
pinned link. Let O be a subset of U_eps, of Haar measure more than 3/4 of that of U_eps, on which n is defined at every site.
Then
  sup over omega in O of max over l in pi of abs(D_l n(omega))  >=  sqrt(2/3)/k - 2 eps.
Consequences. (a) No such rule has abs(D_l n) <= C sum over at most R plaquettes of abs(s(U_p)) on such sets O for all small eps:
the left side would be at most 4 C R eps. So LIP fails for every fixed-range rule on every family of sets of density above
3/4 near the trivial pin. (b) The same holds for any modulus: the defect of a fixed-range rule does not tend to 0
at pure gauge on such sets. It is at least about 0.8/k, k of the order of the range. (c) A rule of range r on a face
with sides at least 2 r + 2 has such x, x', N (N = the sites within r of x), with k <= 2 r + 2 along a coordinate axis.
Proof. For a unit quaternion g let rho_g be the map of pins: omega_l -> g omega_l g^(-1) on links with both ends in N, other links fixed.
It preserves U_eps and Haar measure. Take g in {i, j, k} (rotations by pi about the three axes). The four sets
O, rho_i^(-1) O, rho_j^(-1) O, rho_k^(-1) O have measure above 3/4 of U_eps each, so they have a common point omega. On the links that
n_x reads, rho_g omega is the gauge transform of omega by the constant g on N. So n_x(rho_g omega) = Ad(g) n_x(omega) by (L1), (L3), and
n_x'(rho_g omega) = n_x'(omega) by (L2). Let d be the supremum in the claim. For a pin upsilon in O and consecutive sites y, y' of pi:
abs(n_y - Ad(u) n_y') <= d with u = upsilon_l^(+-1), and abs(Ad(u) m - m) = abs(u m - m u) <= 2 abs(u - 1) < 2 eps. So abs(n_x(upsilon) - n_x'(upsilon)) <= k (d + 2 eps).
Apply it to omega and to rho_g omega: abs(n_x(omega) - Ad(g) n_x(omega)) <= 2 k (d + 2 eps) for g = i, j, k. For a unit vector n = (n_1, n_2, n_3):
abs(n - Ad(i) n)^2 = 4 (n_2^2 + n_3^2), and the three squares add to 8. So one of them is at least 8/3:
2 k (d + 2 eps) >= sqrt(8/3). For (a): abs(s(U_p)) <= abs(U_p - 1) < 4 eps on U_eps. QED
GUIDE (Step 7): 2000 random unit vectors gave a minimum 1.6386 against sqrt(8/3) = 1.6330.
What NOLIP does not exclude. Sets of small density. Example (ARGUED, not written as a proof): the plaquette-axis rule
of row 1036 5.3 has range 1, and satisfies LIP on the open set of pins within distance kappa m(omega)^2 of the abelian pins
with all face plaquette angles of one sign, m(omega) the least abs(s(U_p)) on the face: there the axes are smooth with
derivative of order 1/m and D n = 0 on the abelian pins. This open set touches the trivial pin. It is a thin
neighbourhood of the reducible pins. It carries no information beyond D n = 0 there.
Compare Lemma FR (row 1011 7.3): every frame has sum abs(D n)^2 >= NA(omega)/6. FR is a lower bound by the non-abelian part of
the curvature. NOLIP is a lower bound of order 1/range with no curvature in it.

**4.5 Verdict on (A).**
- A pin-measurable gauge-covariant boundary frame with abs(D_l n) <= C_r sum abs(s(U_p)): PROVED to exist with r = S_1 + S_2 and
  C_r = 2 sqrt(2) (LIP-TREE), on a full neighbourhood of the pure-gauge orbit minus the null set where a is not defined.
  It is not one rule at every site.
- One rule of fixed range r at every site: PROVED not to exist on sets of density above 3/4 near the trivial pin,
  for faces with sides at least 2 r + 2 (NOLIP). The tool is the stabiliser of the trivial pin applied to one ball.
  It exists on thin open sets next to the reducible pins (ARGUED), where it says nothing.
- Is a growing range enough for the consumer? For the definition, yes: Lemma FLOW and GR need only that the boundary
  vectors are functions of the pin of the one cell (row 1026 7.1; row 1036 4.1). Uniform (LOC) was a hypothesis of the
  interior statements (SYM), (REG) and Proposition CURL of row 1034, whose constant 4 m^4 k_1 depends on the range.
  For the size of the defect, no (ARGUED): with range S the bound is the curvature of a strip of S plaquettes, so
  abs(D n) is small only when loops of the size of the cell have small holonomy. At coupling b a loop of area a has
  abs(s(H))^2 of order min(1, a/b) (the size estimate of row 1011 7.3), so the defect collapses only for S^2 well below b.
  A tiling adds one more demand (row 1011 7.1 (i)): the frame on a shared face must be one field for both cells, and
  two base points give two frames. That demand is not treated here.

### Step 5 (done 2026-11-16T10:25:00Z): decision (B), the collapsing-defect frame near the pure-gauge orbit

All PROVED by hand here unless marked. Nobody checked it.
Setting. A box cell with all S_mu >= 2, strengths beta_p >= 0, the setting of GR (lambda supported on L). Frame TREE of 4.1 on the
whole pinned graph, with a the axis of H_(l_0) for one non-tree link l_0 (so a is constant along the pin curves of TG (d)).
Tree-gauge pin H_l = e^(eta_l), eta small; eta_l = 0 on tree links. eta_perp := the part of eta orthogonal to a. lambda_l := lambda_head(l).
Constants of the trivial pin (colour symmetry makes each a number times the identity of R^3, see the proof):
 K_0(l, l') = sum_p beta_p w_p xbar_p [p : l][p : l'],    C_0(l, l') delta_ab = Cov_1(N_l^a, N_l'^b),    Hh_0 := K_0 - C_0.
Hh_0 is the Hessian of F_c at the trivial pin: (d/d eps)^2 F_c(e^(eps v)) = sum Hh_0(l, l') v_l . v_l' (the proof of TP in row 1036 5.1 with e^(eps v_l)
in place of W_l gives K_0; the variance of sum v_l . N_l gives C_0).

**5.1 Theorem LEAD (Q(d lambda) = H_c + Var(Psi) to leading order in the defect).** As eta -> 0, uniformly in a and for bounded lambda:
  H_c(omega; (d lambda) n) = - 2 sum over l, l' of Hh_0(l, l') (lambda_l - lambda_l')^2 eta_perp_l . eta_perp_l'  + O(abs(lambda)^2 abs(eta)^3),
  Var(Psi_(d lambda)) = 4 sum over l, l' of C_0(l, l') lambda_l lambda_l' eta_perp_l . eta_perp_l'  + O(abs(lambda)^2 abs(eta)^3),
  **Q(d lambda) = 2 sum over l, l' of [ C_0(l, l') (lambda_l^2 + lambda_l'^2) - K_0(l, l') (lambda_l - lambda_l')^2 ] eta_perp_l . eta_perp_l'  + O(abs(lambda)^2 abs(eta)^3).**
In the terms of GR (d): direct term = 4 sum K_0 lambda_l lambda_l' eta_perp_l . eta_perp_l', force term = - 2 sum Hh_0 (lambda_l^2 + lambda_l'^2) eta_perp_l . eta_perp_l', both of
second order. The constant of the error term is not written (third derivatives of F_c and the Lipschitz constant
of the force covariance on a compact neighbourhood).
Proof. (1) Phi(eta) := F_c(e^eta) is smooth, and Phi(Ad(g) eta) = Phi(eta) for constant g. A bilinear form on R^3 x R^3 that is invariant
under all rotations is a multiple of the dot product. So the Hessian of Phi at 0 is sum Hh_0(l, l') eta_l . eta_l', and the
covariance of the forces at the pin 1 is C_0(l, l') delta_ab. (2) By TG (d) and GR (e), H_c = (d/d eps)^2 Phi(eta(eps)) with
eta_l(eps) = the rotation of eta_l about a by - 2 eps lambda_l: eta' = - 2 lambda_l a x eta_l, eta'' = - 4 lambda_l^2 eta_perp_l. Taylor: Phi = Phi(0) + (1/2) Hh(eta, eta) + O(abs(eta)^3), so
H_c = Hh(eta', eta') + Hh(eta, eta'') + O(abs(lambda)^2 abs(eta)^3) = 4 sum Hh_0 lambda_l lambda_l' eta_perp_l . eta_perp_l' - 4 sum Hh_0 lambda_l'^2 eta_perp_l . eta_perp_l', and the second sum is symmetrised.
((a x u) . (a x u') = u_perp . u'_perp.) (3) Psi = sum lambda_l (D_l n) . N_l in the tree gauge with D_l n = a - Ad(H_l) a = - 2 eta_l x a + O(abs(eta)^2), and the
covariance of the forces at the pin H is that at 1 plus O(abs(eta)). (4) Q = H_c + Var (GR (e)). QED
Checks. Cube: one non-tree link, so the K_0 term is 0 and Q = 4 C_0 lambda_110^2 abs(eta_perp)^2 with C_0 = beta xbar - kappa: this is 3.2 (iv).
lambda constant on all heads: H_c = 0 to this order. Compact U(1): there is no eta_perp. Every term is 0. Zero gain.
Structure. H_c is a graph Laplacian in lambda on the non-tree links, with the signed weights Hh_0(l, l') eta_perp_l . eta_perp_l'.
Var is positive semidefinite. Only the variance has diagonal terms.

**5.2 Corollary BOTH (the 4D cell of row 1036 5.2; one site; both signs on open sets).** z in the relative interior of
the face {x_4 = 0}, lambda the indicator of z, l_1 a non-tree link into z, l_0 not into z.
 (i) There is a non-empty open set of pins, with the trivial pin in its closure, on which Q(d lambda) > 0.
 (ii) If Hh_0(l_1, l') != 0 for some non-tree link l' not into z, there is such an open set on which Q(d lambda) < 0 and
      H_c < 0, and one on which H_c > 0. The hypothesis holds for beta < 3/2 with l_1 = (y, 2), l' = (y + e_3, 2) (comb tree, y_1 > 0).
Proof. (i) Pin: H_(l_0) = e^(delta a_0), H_(l_1) = e^(delta u), u a unit vector orthogonal to a_0, all other H_l = 1. LEAD gives
Q = 4 C_0(l_1, l_1) delta^2 + O(delta^3), and C_0(l_1, l_1) = (beta^2/3) E_1[1 - t_p^2] > 0 for the interior plaquette p of l_1 (row 1036 6.1).
The frame is continuous near this pin, and so is Q. (ii) Pin: H_(l_0) = e^(rho a_0), H_(l') = e^(rho u'), H_(l_1) = e^((rho/M) u),
u, u' orthogonal to a_0 with (u . u') Hh_0(l_1, l') = abs(Hh_0(l_1, l')). LEAD: Q = rho^2 [4 C_0(l_1, l_1)/M^2 - 4 abs(Hh_0(l_1, l'))/M] + O(rho^3) and
H_c = - 4 rho^2 abs(Hh_0(l_1, l'))/M + O(rho^3). Take M large, then rho small. u' -> - u' gives H_c > 0. For the pair named, the only common
plaquette is (y; 2, 3), a boundary plaquette, so K_0 = - beta/2; at the pin 1, N_l = beta Im R_l with R_l the interior
staple, so abs(C_0(l_1, l')) <= beta^2/3. QED
So for this frame Q(d lambda) for one lambda has no sign near pure gauge. This is Proposition SIGN again, now for one covariant
frame whose defect collapses.

**5.3 Theorem ORB (the response to a boundary gradient has no sign along a pin curve).** Frame TREE as above, lambda
supported on L. The pin curve omega_eps of GR is a one-parameter group of maps of pins, the frame at omega_eps is the frame at omega,
and phi(eps) := F_c(omega_eps) is smooth and bounded on R with phi''(eps) = H_c(omega_eps; (d lambda) n). Hence: if H_c <= 0 at every pin of one
curve, then H_c = 0 on that curve. The same holds for >= 0. If phi is not constant, H_c is positive on a non-empty
open set of pins and negative on another.
Proof. TG (d): the tree links and a do not move, and the map is conjugation of H_l by e^(eps lambda_l a). F_c is continuous on a
compact space. A bounded concave function on R is constant. QED
Also (same proof, the torus generated by all lambda): on the closure of each orbit F_c has a maximum, and there
H_c(omega; (d lambda) n) <= 0 for every lambda. So (O2-min) for all lambda holds on a non-empty closed set of pins. Its measure is not
computed. Compact U(1): the curves are points and H_c = 0.

**5.4 Lemma WEAK (the weak form, with its constant).** Frame TREE, strengths with abs(beta_p w_p) <= b, four dimensions:
  abs(Q(d lambda)) <= delta(omega) sum_z lambda_z^2,   delta(omega) := b max over z of sum over pinned l into z of (96 abs(s(H_l))^2 + 24 abs(s(H_l))),
and delta -> 0 at the pure-gauge orbit. Near the trivial pin LEAD gives the better order abs(eta)^2 (constant not written).
On the comb tree of a face, abs(s(H_l)) <= sum over the at most S_1 + S_2 plaquettes of Sigma_l of abs(U_p - 1) (LIP-TREE).
Proof. Lemma MASS of row 1036 6.2 in the corrected form (abs(beta_p w_p)): abs Q <= b sum_l tau_l^2 (24 abs(D_l n)^2 + 12 abs(D_l n)), with TG (b). QED

**5.5 Theorem ONE+ (the literal form of (O2) fails for every frame once constants are admitted).**
Convention (new here, and outside the tail-vector site frames of row 1034): let lambda live on all pinned sites, and let
the move turn a free link at its pinned end: U -> e^(eps lambda_z n_z) U on a free link out of z, U -> U e^(- eps lambda_y n_y) on a free link into y.
(For S_mu >= 2 a free link has at most one pinned end.) Then GR (a)-(e) hold as written, with the same proof: the gauge
transformation e^(eps lambda n) on the pinned sites returns every free link. For lambda = 1: the pin does not move, H_c = 0, and
  Q(d 1) = E[Psi_1^2] = Var( sum over pinned l of (D_l n) . N_l ) >= 0,
with Q(d 1) > 0 if D_l n != 0 on one pinned link l whose interior plaquette has a free link that lies in no other
plaquette with a pinned link (in the 4D cell with S_mu >= 4: every link of a face at distance at least 2 from the
other faces). So Q(d lambda) <= 0 for all boundary lambda fails at every pin, for every pin-measurable frame, unless D n = 0 on
all such links; and D n = 0 on the links of two plaquettes at a site makes their axes parallel (Lemma FR), a null set.
Proof. As Theorem ONE of 3.3. The move is a fixed field of left and right rotations of free links, so it preserves
Haar measure and Q = E[Psi^2]. In the free link named, Psi is beta (D_l n) . Im(omega_l R) plus terms that do not contain it. QED
Reading. The literal statement (O2) of row 1034 7.4, H_c + Var(Psi) <= 0, cannot hold for lambda = constant, where H_c = 0.
What is left of it is a statement modulo the choice of the extension. Its extension-free form is (O2-min).

**5.6 Verdict on (B).**
- Leading order: LEAD. The direct term and the force term are both of second order in the defect, and they combine to
  a signed graph Laplacian in lambda (the response) plus a positive variance.
- Exact (O2), literal form, Q(d lambda) <= 0 for all boundary lambda on a set of pins of positive measure: FAILS for frame TREE on the
  cube (3.2, 3.3), and for every frame in the convention of 5.5 (ONE+). For lambda supported on L in the 4D cell it is not
  decided: by LEAD it is the matrix inequality "4 C_0-part <= the Laplacian part" on the lambda that vanish off L; one-site
  tests give both signs (BOTH). OPEN, and by ONE+ of no use to the consumer in that form.
- Weak form, abs(Q(d lambda)) <= delta(pin) sum lambda^2 with delta -> 0 at pure gauge: PROVED (WEAK), delta written.
- (O2-min), H_c <= 0: for frame TREE it holds with equality on the cube; in the 4D cell H_c has both signs on open sets
  (BOTH, ORB) and no sign along any pin curve where F_c is not constant. So no statement "for almost every pin near
  pure gauge" of this kind is true, in either direction, unless H_c is 0.
- What the consumer needs (ARGUED from row 1011 7.1, 7.4 and row 1034 7.3). The consumer bounds the response of one cell
  to a twist theta with constant field strength f by a curl form with the classical constant. The gradient part of theta is
  not small: the boundary links carry sum theta^2 of order f^2 S^5 against the curl energy f^2 S^4 (row 1034 7.3). So it needs,
  at the pins that carry the measure, H_c(omega; theta n) <= C sum (d theta)^2 + (a term in the gradient part that is at most the
  first). The exact form (the second term <= 0) is what U(1) has. The weak form is enough only if delta(pin) is at most
  of order b/S. With delta of order b abs(s(H_l))^2 and loops of area up to S^2, that is abs(s(H_l))^2 <= 1/S for the loops of the
  cell: a typical-pin statement of the kind (N1), true (ARGUED, by the size estimate of row 1011 7.3) only when S^3 is
  below the order of b. At order-one coupling it is false for typical pins.
- Is the weak form with (N1) enough? No, for two reasons. It needs (N1) with the rate above, which holds only below
  the band. And (N1) is not what is left: ORB and BOTH show that the response on gradients has no sign even where the
  defect is small, and class (C) (Step 6) is not a small-defect statement. This agrees with astra's remark.

### Step 6 (done 2026-11-16T10:26:04Z): decision (C), non-stationary pins

All PROVED by hand here unless marked. Nobody checked it. Cube and notation of Step 3.

**6.1 The literal question.** Can one frame make lambda -> Q(d lambda), cross terms M(b) included, negative semidefinite at a
non-stationary pin of the cube? No: Theorem ONE (3.3). At every pin and for every frame, Q(d 1) > 0 unless D n = 0 on the
four pinned links, and then the form is 0. The proof needs no value of M(b).
The consumer may add a constant to lambda (F2). So the question that matters is the form on the lambda with lambda_110 = 0
(every boundary gradient rotation of the cube has one such lambda). For these, Psi = theta_1 X_a + theta_2 X_b with X_l = (D_l n) . N_l, and
Q(d lambda) = H_c + Var(theta_1 X_a + theta_2 X_b), with H_c from CUBE-H. Neither term contains n_110.

**6.2 Theorem TUNE (cube; at every non-stationary pin a frame makes every boundary gradient cost less than zero).**
Let the pin have s != 0 and b_0 + kappa(t) != 0, sigma := the sign of b_0 + kappa(t). Take a unit vector u_0 orthogonal to s,
w := (s x u_0)/abs(s), an angle alpha in (0, pi/2), and
  n_000 = u_0,   n_100 = Ad(omega_a)^(-1) (cos(alpha) u_0 + sigma sin(alpha) w),   n_010 = Ad(omega_b)^(-1) (cos(alpha) u_0 - sigma sin(alpha) w),   n_110 any unit vector.
Then, exactly,
  H_c(omega; (d lambda) n) = (b_0 + kappa) t [ (theta_1 - theta_2)^2 (1 - cos alpha)^2 + (theta_1 + theta_2)^2 sin^2 alpha ] - 2 abs(b_0 + kappa) abs(s) sin(alpha) [ theta_1^2 + theta_2^2 - 2 (1 - cos alpha) theta_1 theta_2 ],
and for every lambda with lambda_110 = 0:
  H_c <= abs(b_0 + kappa) (theta_1^2 + theta_2^2) [ 4 abs(t) (1 - cos alpha) - 2 abs(s) sin(alpha) cos(alpha) ],
  Q(d lambda) <= 4 sin(alpha/2) (theta_1^2 + theta_2^2) { abs(b_0 + kappa) [ 2 abs(t) sin(alpha/2) - abs(s) cos(alpha/2) cos(alpha) ] + 2 beta^2 sin(alpha/2) }.
So H_c is negative definite in (theta_1, theta_2) when 2 abs(t) tan(alpha/2) < abs(s) cos(alpha), and Q(d lambda) < 0 for all (theta_1, theta_2) != 0 when
  tan(alpha/2) (2 abs(t) abs(b_0 + kappa) + 2 beta^2) < abs(b_0 + kappa) abs(s) cos(alpha).
Both hold for all small alpha > 0. Then every boundary gradient rotation B = (d lambda) n of the cube with (theta_1, theta_2) != 0 has
H_c(omega; B) <= Q < 0, with an extension that has zero curl. (If theta_1 = theta_2 = 0, B is a gauge move at 000 and H_c = Q = 0.)
Proof. u_0 x w = s/abs(s). d_1 = (cos alpha - 1) u_0 + sigma sin(alpha) w, d_2 = (cos alpha - 1) u_0 - sigma sin(alpha) w. So s . d_i = 0 (the kappa' term of CUBE-H
is 0), u_0 x d_1 = sigma sin(alpha) s/abs(s) = - u_0 x d_2, d_1 x d_2 = 2 sigma (1 - cos alpha) sin(alpha) s/abs(s), and abs(theta_1 d_1 - theta_2 d_2)^2 is the first bracket. Insert
in CUBE-H. Bounds: 2 abs(theta_1 theta_2) <= theta_1^2 + theta_2^2 gives the second bracket >= (theta_1^2 + theta_2^2) cos(alpha) and the first <= 4 (theta_1^2 + theta_2^2)(1 - cos alpha).
Variance: abs(D_a n) = abs(d_1) = 2 sin(alpha/2) = abs(D_b n), the random part of N_l is beta Im(omega_l R_l) of length at most beta, so
Var(theta_1 X_a + theta_2 X_b) <= beta^2 (abs(theta_1) + abs(theta_2))^2 4 sin^2(alpha/2) <= 8 beta^2 sin^2(alpha/2) (theta_1^2 + theta_2^2). QED
Non-stationary pins exist: kappa(1) > 0 (row 1036 4.2), so b_0 + kappa(t) > 0 for t near 1, and any h != 1 near 1 is one.
GUIDE (Step 7): the bracket and its bound were compared in 2000 random cases with alpha = phi/2, h = e^(phi i), phi in (0, pi/3]; no
violation, and the bound was negative in all of them.
What TUNE is and is not.
- It answers the open class (G2) of check 1037 on the cube: yes, the force term can beat the direct term for all
  boundary gradients at once, modulo the constant. It is exact, with the cross terms.
- The frame is pin-measurable. It is not gauge covariant, and on the cube it cannot be: a covariant vector at 000 is
  +-s/abs(s) (stabiliser), and TUNE needs u_0 not parallel to s. In a cell with two independent plaquettes at the base
  site a covariant version of u_0 exists off a null set (ARGUED, not written).
- Its defect is not of order one on the links that matter: abs(D n) = 2 sin(alpha/2) on a and b, and alpha must be small against
  abs(s) abs(b_0 + kappa)/beta^2. The defect of order one, 2 abs(s x u_0) = 2 abs(s) on the loop, sits on l_1 or l_2 and is removed by the constant.
  So TUNE is a frame with a small tilt against the gradient of F_c, laid on a transported frame.
- It is the statement that F_c has a descent direction at a non-stationary pin, and that a non-abelian frame can
  give the pin curve an acceleration c = lambda^2 n x D n along it. At a stationary pin it is void: at the trivial pin
  H_c = (b_0 + kappa) abs(theta_1 d_1 - theta_2 d_2)^2 >= 0 for every frame (row 1036 4.3).

**6.3 Covariant frames on the cube, and compact U(1).** A covariant frame on the cube is n_z = sigma_z times the transported
axis s/abs(s), sigma_z = +-1 (astra, verdict 2). Then d_i = (sigma_i - sigma_0) s/abs(s), u_0 x d_i = 0, d_1 x d_2 = 0, and CUBE-H gives, with t = cos phi,
  H_c = [ (b_0 + kappa) t - kappa' abs(s)^2 ] (theta_1 (sigma_100 - sigma_000) - theta_2 (sigma_010 - sigma_000))^2 = (d^2 F_c/d phi^2) (...)^2.
There is no force term. The sign is the convexity of F_c in the class angle. Compact U(1) with site signs gives the
same formula (3.4), and with one common axis it gives 0. So for covariant frames the cube gives SU(2) nothing that
U(1) does not have: zero gain. TUNE has no U(1) form (U(1) has no vector orthogonal to s), and U(1) with a common axis
has H_c = 0 on gradients, not H_c < 0.

**6.4 The lane's 4D cell: not decided (OPEN).** What is known and what stops the same proof.
- One site, one incoming link: Proposition SIGN of row 1036 gives Q < 0 for a tilt against the force. BOTH gives it for
  frame TREE near pure gauge.
- All lambda at once: a frame has two parameters per site. The vector n_x enters the terms of every link at x: up to
  three incoming and three outgoing links in a face. A tilt of n_x against the force on one link is a tilt of the same
  n_x on the others. On the cube each of n_100, n_010 enters one tail term only, and the constant removes the head terms.
- The constant is not available for lambda supported on L (L is not the whole boundary). In the convention of 5.5 it is.
- By Lemma FR, at a pin with non-abelian part NA(omega) of order one per site the defects are of order one on a positive
  fraction of the links, and there the direct term abs(D n)^2 e_l is of order b. Whether the force terms 2 c . E[N_l] can
  cancel it on all links at once is not decided here. No proof and no counterexample.

**6.5 Verdict on (C).**
- Literal form (lambda -> Q(d lambda) negative semidefinite, the extension of GR): FAILS on the cube for every frame at every pin
  (ONE), and in every cell in the convention of 5.5 (ONE+).
- Modulo the constant (the consumer's form on the cube): HOLDS strictly at every non-stationary pin of the cube for
  an explicit pin-measurable frame (TUNE). For covariant frames on the cube the form is (d^2 F_c/d phi^2) times a square,
  the same as in compact U(1).
- 4D cell: OPEN.

### Step 7 (done 2026-11-16T10:26:46Z): the GUIDE run (it proves nothing)

One job under the numeric lock, 2026-11-16T10:21:44Z (`date -u`), under one second, pure Python (`python3 -I`), thread
variables set to 1. The checkout is sparse and has no `scripts/`. As in row 1036, the lock command was run from a copy
of `scripts/lab_ops.py` and `scripts/automation_lock.py` taken with `git show HEAD:` into the scratch folder; acquire
reported "acquired", release "released". Script and output: `/tmp/r1038.PmTW7C/cube_guide.py`, `cube_guide.out` (not committed).
Output, in full:
- max abs error, t' and t'' formulas of CUBE-H against finite differences of the moved holonomy (200 random pins,
  frames and lambda): 9.98e-08;
- tuned frame, alpha = phi/2, phi in (0, pi/3]: cases with the bracket above the bound, or the bound not negative: 0 of 2000;
- minimum over 2000 unit n of max over g in {i, j, k} of abs(n - Ad(g) n): 1.6386 (bound sqrt(8/3) = 1.6330).
Not run: any check of LEAD, BOTH, ORB, WEAK, ONE+ or of the variance bound in TUNE. No integral over the cube was computed.

### Step 8: marks, limits, RESULT

Finished 2026-11-16T10:26:46Z (`date -u`). Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit f3506eec4,
one session, no subagents. Written by hand. One GUIDE job (Step 7). Checked by: nobody. Only this file was written.

| Item | Statement | Mark |
|---|---|---|
| TG (4.1) | a frame transported from one base point is the fixed colour a in the tree (axial) gauge; abs(D_l n) = 2 abs(s(H_l) x a); the pin curve is conjugation of H_l by e^(eps lambda a) | PROVED |
| LAD (4.2) | ladder Stokes bound abs(H - 1) <= sum abs(U_p - 1) (after Balaban CMP 99 Lemma 1) | PROVED |
| LIP-TREE (4.3) | LIP with r = S_1 + S_2, C_r = 2 sqrt(2), comb tree of a face; not one rule per site | PROVED |
| NOLIP (4.4) | no rule of fixed range has defect below sqrt(2/3)/k - 2 eps on sets of density above 3/4 near the trivial pin | PROVED |
| Thin open sets next to reducible pins with LIP at range 1 (4.4) | | ARGUED |
| (A) uniform (LOC) with LIP | on most pins near pure gauge | FAILS (NOLIP) |
| (A) growing range enough for the consumer | for the definition yes; for the size of the defect no | ARGUED |
| CUBE-H (3.1) | closed form of H_c on the cube, any pin, any frame | PROVED |
| Cube test, transported frame (3.2) | H_c = 0; Q = lambda_110^2 times a variance, between 0 and 4 beta^2 lambda_110^2 abs(s x a)^2; leading value 4 (beta xbar - kappa) | PROVED |
| ONE (3.3) | cube: Q(d 1) > 0 unless D n = 0; the literal form is never negative semidefinite | PROVED |
| LEAD (5.1) | Q(d lambda), H_c, Var(Psi) to second order in the defect; error constant not written | PROVED |
| BOTH (5.2) | 4D cell, one site: Q > 0 on an open set; Q < 0 and H_c of both signs on open sets if Hh_0(l_1, l') != 0 (true for beta < 3/2) | PROVED |
| ORB (5.3) | H_c along a pin curve is the second derivative of a bounded function: no sign unless 0 | PROVED |
| WEAK (5.4) | abs(Q(d lambda)) <= delta(pin) sum lambda^2, delta written, delta -> 0 at pure gauge | PROVED (uses MASS of row 1036, corrected) |
| ONE+ (5.5) | with the pinned-end convention on free links, Q(d 1) = Var(Psi_1) > 0 for every frame with a defect on a deep link | PROVED (the convention is new) |
| (B) exact (O2), literal | cube, frame TREE; every frame with constants admitted | FAILS |
| (B) exact (O2), lambda on L, 4D cell, positive measure | | OPEN |
| (B) weak form | | PROVED |
| (B) what the consumer needs; weak form with (N1) enough only for S^3 below the order of b | | ARGUED |
| TUNE (6.2) | cube, every non-stationary pin: an explicit frame with H_c negative definite and Q < 0 on gradients modulo the constant | PROVED |
| Covariant cube frames and U(1) (6.3) | H_c = (d^2 F_c/d phi^2) times a square in both; zero gain | PROVED |
| (C) literal form on the cube | | FAILS (ONE) |
| (C) modulo the constant on the cube | | PROVED (TUNE) |
| (C) in the 4D cell | | OPEN |
| A covariant version of TUNE in a larger cell | | ARGUED, not written |

Limits.
- Nothing here is checked. A same-provider check and a cross-provider check are both open.
- LEAD has no written error constant. BOTH (ii) needs Hh_0(l_1, l') != 0, proved for beta < 3/2 only.
- ONE+ uses a convention for free links into upper-face sites that row 1034 does not use.
- The consumer paragraphs (4.5, 5.6) are readings of rows 1011, 1026 and 1034, with size estimates that are ARGUED.
- Frame TREE is treated on a face with the comb tree; the tree on the whole boundary of the 4D cell is not written.
- A tiling (one frame field on shared faces) is not treated. Upper faces are treated only through the convention of 5.5.
- The literature of Step 2 was not fetched in this row; Balaban CMP 99 is cited through the lane's port and row 1039.

Corrected texts for the lead (no other file was edited).
- `parts/gap.md`, the row 1036 entry: add "row 1038 (unchecked): a transported frame is the fixed colour in axial gauge;
  LIP holds with range of the order of the face and fails for every fixed range on most pins near pure gauge (NOLIP);
  for it the response to a boundary gradient is 0 on the cube and has no sign in the 4D cell (LEAD, BOTH, ORB); the
  literal (O2) fails when constants are admitted (ONE, ONE+); on the cube a tuned frame gives negative cost at every
  non-stationary pin (TUNE), which is a descent direction of F_c and not a stiffness bound."
- Row 1034's O2: "replace by (O2-min), H_c(omega; (d lambda) n) <= 0, the form without an extension (row 1038 F2, 5.5)".

RESULT: Row 1038 (Claude Fable 5.2 medium, laptop background agent, commit f3506eec4; written by hand, checked by nobody; one GUIDE run under the numeric lock that proves nothing). The two classes that rows 1036 and 1037 left open at the pinned boundary are decided in part, and the wall (W) does not move. (A) LIP: PROVED for a frame transported from one base point with r = S_1 + S_2 and C_r = 2 sqrt(2) (Lemmas TG, LAD, Theorem LIP-TREE; it is the fixed colour in Balaban's axial gauge, not one rule per site); PROVED impossible for every rule of fixed range on sets of density above 3/4 near the trivial pin, where the defect stays above sqrt(2/3)/k - 2 eps (Theorem NOLIP, stabiliser of the trivial pin on one ball); a growing range is enough to define the consumer's bound but not to make the defect small (ARGUED). (B) For the transported frame, Q(d lambda) = H_c + Var(Psi) to second order in the defect is a signed graph Laplacian in lambda plus a positive variance (Theorem LEAD); on the cube H_c = 0 and Q = lambda_110^2 Var >= 0, so the literal exact (O2) FAILS there and, with constants admitted, for every frame in every cell (Theorems ONE, ONE+); the weak form abs(Q(d lambda)) <= delta(pin) sum lambda^2 with delta -> 0 at pure gauge is PROVED (Lemma WEAK); the response H_c on boundary gradients has both signs on open sets in the 4D cell (Corollary BOTH, beta < 3/2) and no sign along any pin curve (Theorem ORB), so the extension-free form (O2-min) is neither true nor false for almost every pin; the weak form with (N1) is enough only for S^3 below the order of b (ARGUED), that is below the band. (C) On the cube the form lambda -> Q(d lambda) is never negative semidefinite (ONE), but modulo the constant an explicit pin-measurable frame makes every boundary gradient cost less than zero at every non-stationary pin (Theorem TUNE, closed form from Lemma CUBE-H); this is a descent direction of F_c, void at stationary pins, not covariant on the cube, and not a stiffness bound; covariant cube frames give (d^2 F_c/d phi^2) times a square, the same as compact U(1): zero gain. What changed for the crux: route (ii) at the pinned boundary has no exact curl mechanism in the collapsing-defect class and its remaining positive statement is a typical-pin smallness of cell-size holonomies that holds only at small effective coupling; no selective gain at order-one coupling was found. OPEN: exact (O2) for lambda on L and class (C) in the 4D cell, a covariant TUNE in a larger cell, tilings, the error constant of LEAD, and every check of this file.
