lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-16T11:55Z

# gap-aligned-frame (row 1026): decide the aligned frame left open by check 1022

Pinned at commit fe79776a6, branch `claude/ym4d-hard-route`. Started 2026-11-15T23:55Z (from `date -u`).
Research-stage working state. Nothing here is a public claim.

## Plan (at most eight steps; one step per response, result appended before the next)

1. Read the sources the row names: `parts/gap.md`, `library/gap-short-step-max.md` 4.1-4.5,
   `library/gap-short-step-check-opus.md` L220-290 (D2), Lemma FR of
   `library/gap-pinned-cell-gauge-max.md` 7.3. Fix the exact definitions: frame n, heads, N_l, projected
   current, cost, curl form, "order-one response". Grep `library/open-core.md` and FINISH rows for overlap.
2. State the open statement precisely (AF) in the notation of the sources.
3. Hand test: one plaquette.
4. Hand test: one cube.
5. Hand test: 3^4 torus (structure, counting of equations against unknowns).
6. Decide: obstruction on an open set of positive Wilson measure, or a construction with cost form and consumer.
7. Optional numeric guide or refutation, under the numeric lock, only if memory is 50 percent free or more.
8. Verdict table with marks PROVED, ARGUED, OPEN, FAILS, credits, and the RESULT line.

## Step log

(steps are appended below as they finish)

### Step 1 (done 2026-11-16, first response): sources read, overlap check

Read in full: `library/gap-short-step-max.md` Section 4 (L213-277: Lemmas FLOW, PROJ, FR+, SPLIT, sizes 4.5);
`library/gap-short-step-check-opus.md` L215-292 (D2 at L224 and L273); `library/gap-pinned-cell-gauge-max.md`
3.1-3.2 (conventions, Proposition A) and 7.3-7.4 (Lemma FR, (N1)-(N3)); `parts/gap.md` L1-60 and L137.
Overlap grep (`aligned`, `orthogonal to the forces`, `conserved pathwise`, `projected current` in
`library/open-core.md`, `FINISH.md`, `parts/gap.md`): the only matches are row 1022 (the check that opened this
item), this row, and `parts/gap.md` L137 (which records the item as open). No other row covers it. Row 1016 plan
step 7 (reopen condition (ii) of row 1013 in general) is the neighbour named by row 1018; it is not this statement.

### Step 2: the statement, in exact form

Notation of row 1011 3.1-3.2 and row 1018 4.2. Lattice Lambda (a finite 4D torus with V sites, or a cell). Links are
oriented x -> x + mu. X(b) = (d/d eps) A(e^(eps b) U) = - sum_l b_l . N_l, so N_l in su(2) = R^3 sits in the frame of
the tail of l. Gauss law (PROJ (ii)): M_z := sum_(tail z) N_l = sum_(head z) Ad(U_l)^(-1) N_l.
A frame is a unit-vector field n_x(U), gauge covariant: n_x(U^g) = Ad(g_x) n_x(U). j_l = n_tail(l) . N_l.
(div j)(z) = sum_(tail z) j_l - sum_(head z) j_l = - sum_(head z) (D_l n) . N_l (PROJ (iii)).

**(AF-1), pathwise alignment.** At the configuration U: div j = 0 at every free site.
**(AF-2), the cost.** The cost form of the moves theta n is zero on gradients theta = d lambda, and is bounded by a
constant times beta sum_p (d theta)_p^2 at order-one response.

Three exact remarks that fix what has to be decided (each PROVED, one line).

**Remark LIN.** At fixed U the current is linear in n. Put P_x(lambda) = sum over l with tail x of
(lambda_x - lambda_head(l)) N_l in R^3. Then sum_l (d lambda)_l j_l = sum_x n_x . P_x(lambda). So (AF-1) says:
n is orthogonal in (R^3)^V to the subspace PP(U) = {P(lambda)}, of dimension at most V - 1 on a torus. Without the
unit-length condition the solutions form a linear space K(U) of dimension at least 2V + 1. (AF-1) asks for a point
of K(U) on the product of spheres (S^2)^V: V - 1 linear equations for 2V angles. No count excludes it; no count
gives it (K = {v_1 = 2 v_2} has codimension 3 and no unit point, and missing (S^2)^V is an open condition on K).

**Remark JAC (the further point of D2, made exact).** For a field-dependent frame the move V = theta n has
div V = sum_l theta_l d_l with d_l(U) = sum_a (derivative of n^a_tail(l) in direction a of link l). So in Lemma FLOW

  Psi_(theta n) = - sum_l theta_l (j_l - d_l).

The cost is zero on gradients if and only if the current jt = j - d is conserved almost surely. Then the fields
V_lambda = (d lambda) n are infinitesimal symmetries of the measure e^A dU, and for lambda zero on the pinned sites
E[V_lambda f] = - E[f Psi_lambda] = 0; so Q(theta) = - E[V_theta Psi_theta] satisfies Q(theta + d lambda) = Q(theta):
it is a quadratic form in d theta. That is the meaning of "curl form" in PROJ (iv). It is NOT yet a bound by
beta sum_p (d theta)_p^2: a form C(d theta, d theta) with a long-range kernel C (for instance the transverse
projector, a mass term for the transverse part of theta) is also zero on gradients.

**Remark BACK (a cleaner divergence-free class than tree transport).** If n_x does not depend on the four links with
tail x, then d = 0 and theta n is divergence free for every theta. Gauge-covariant examples: the axis of a
plaquette (x; -mu, -nu), whose loop x -> x - mu -> x - mu - nu -> x - nu -> x uses no link with tail x.
The forces N_(x,mu) do depend on the links with tail x, so a frame solving (AF-1) is in general not of this class.

### Step 3: one plaquette, by hand (PROVED)

Sites x, x + mu, x + nu, w = x + mu + nu, all free; gauge U_1 = U_2 = U_3 = 1, U_4 = g^(-1), g = U_p = cos phi + s,
|s| = sin phi. Then N_1 = N_2 = beta s, N_3 = N_4 = - beta s (transported). (AF-1): n_(x+mu) . s = n_x . s = n_(x+nu) . s
(n_w is free: w has no outgoing link). A gauge-covariant vector at x is a function of g that is fixed by the
stabiliser of g, so n_x = + or - s/|s|: the only covariant frame is the axis, D n = 0. A plaquette is reducible; this
is the trivial case. Cost, with the Jacobian: d_l = 2 cot phi (1, 1, -1, -1) (the divergence of the field d/d phi for
the Haar density sin^2 phi), so jt = (beta sin phi - 2 cot phi)(1, 1, -1, -1) is conserved and

  Psi = - (d theta)_p (beta sin phi - 2 cot phi),      Q(theta) = E[Psi^2] = (d theta)_p^2 E[beta cos phi + 2/sin^2 phi].

Checks: beta = 0 gives 2 E[1/sin^2 phi] = 4; large beta gives about beta + 2 beta = 3 beta (in the Gaussian limit
E[1/r^2] = 1/sigma^2 in three dimensions). So the frame's singularity at s = 0 is integrable, and the Jacobian term
is of the same order beta as the action term: on one plaquette the form is a curl form with constant about 3 beta
against beta for U(1).

### Step 4: one cube (open, 8 free sites), by hand (PROVED)

Each site has at most 3 outgoing links. At the corner 000 there is no incoming link, so the Gauss law gives
N_1 + N_2 + N_3 = 0: the three outgoing forces are coplanar. At a site with two outgoing links they span a plane; with
one, a line. So at every site with an outgoing link there is a unit n_x orthogonal to all outgoing forces at x
(unique up to sign when the span is a plane), for instance n_000 = N_1 x N_2 / |N_1 x N_2|. With it **j = 0 on every
link**, so (AF-1) holds. It is gauge covariant because the forces are. The three plaquette holonomies at 000 do not
commute for almost every U, so the cube is non-reducible almost surely, and D n is not 0 (Lemma FR).
So: **on one cube an aligned frame exists on almost every configuration, and almost every configuration is
non-reducible.** Sentence L275 of row 1018 ("exists exactly on reducible configurations only") is false there.
What the cube does not show: its frame is of the kind "j = 0", which needs outgoing forces in a plane at each site.
In the bulk of a 4D lattice a site has 4 outgoing links with the single relation M_x = (incoming sum), and the four
forces span R^3 for almost every U, so j = 0 is not available. (In two dimensions it is: n = N_1 x N_2 normalised.)
With j = 0 the move theta n keeps the action to first order for every theta, and Psi = sum_l theta_l d_l is all Jacobian.

### Step 5: the 3^4 torus (and L^4, L >= 3). Structure by hand; GUIDE run

**Count.** V sites, 2V angles, V - 1 independent equations (the V equations sum to zero). Each site has 4 outgoing
forces with the one relation M_x = incoming sum, so j = 0 is not available and the cube's frame has no analogue.
Greedy solving fails for a reason worth recording: solving the equation at z for n_z needs
|sum_(head z) n_tail . N_l| <= |M_z|, and summing "strict inequality at every site" over z contradicts
sum_mu |m_x . N_(x,mu)| >= |M_x| (m_x = M_x/|M_x|). So no site-by-site scheme works; the system is global.
No topological argument forces a solution either: the map n -> div j is odd, but the antipodal index of (S^2)^V
is 2, and V - 1 > 2.

**GUIDE run** (2026-11-16T00:04Z by the lock record; `python3 scripts/lab_ops.py numeric-lock acquire` succeeded;
memory 66 percent free; script `/tmp/gap-aligned-frame-w2/af.py`, log `run1.log`, not committed; peak 40 MB).
3^4 torus, forces checked against a finite difference (5.558283 against 5.558285) and the Gauss law (6e-15).
Unit points of K(U) by Gauss-Newton from random starts: found on 3 of 3 Haar-random configurations and on 3 of 3
Metropolis configurations at beta = 2.4 (plaquette mean 0.65), residual below 4e-14 in 6 to 9 iterations, rank of the
system 80 = V - 1 each time, sum_l |D_l n|^2 between 577 and 670 (324 links: these frames are far from
covariantly constant). The run did not refute existence; it suggests aligned frames exist at typical
configurations, in a family of dimension V + 1. That is a guide, not a proof.

### Step 6: Theorem E (aligned frames exist on an open set of the 4D torus). PROVED by hand

**Lemma RANK.** On the torus Z_L^4, L >= 3, for a real link field f put (T_f h)(x) = sum_mu f_(x,mu) (h_(x+mu) - h_x).
Define f* by: numbers c1(u) (u in Z_L^3), c2(v) (v in Z_L^2), c3(t), psi_t (t in Z_L), all non-zero, with
sum_u c1 = sum_v c2 = sum_t c3 = 0 and S := sum_t c3(t)/(psi_t psi_(t-1)) not 0; and
  f*_(x,1) = c1(x_2, x_3, x_4),
  f*_(x,2) = [x_1 = 0] c2(x_3, x_4),
  f*_(x,3) = [x_1 = 0][x_2 = 0] (c3(x_4) + (psi_(x_4) - psi_(x_4 - 1)) [x_3 = 0]),
  f*_(x,4) = [x_1 = 0][x_2 = 0] psi_(x_4) ([x_3 = 1] - [x_3 = 0]).
(For instance c1 = 1 except one value -(L^3 - 1); c2 = 1 except one value -(L^2 - 1); c3 = (1, ..., 1, -(L - 1));
psi = (1, ..., 1, 2); then S = 1/2 + (L - 2) - (L - 1)/2 = (L - 2)/2.) Then
(a) f* is conserved and f* = d* phi* for an explicit two-form phi*;
(b) the kernel of T_(f*) is the constants, so T_(f*) has rank V - 1.

Proof of (b). Sites with x_1 not 0 carry only f_1 = c1 not 0: h(x + e_1) = h(x) for x_1 = 1, ..., L - 1, so h is
constant on every line in direction 1: h = eta(x_2, x_3, x_4). At a site with x_1 = 0 the direction-1 term is then
zero. If x_2 is not 0 the equation is c2 (eta(u + e_2) - eta(u)) = 0, so eta = zeta(x_3, x_4). At x_1 = x_2 = 0 the
equation is the two-dimensional one, G_3 (zeta(v + e_3) - zeta(v)) + G_4 (zeta(v + e_4) - zeta(v)) = 0 with
G_3 = f*_3, G_4 = f*_4 as functions of v = (x_3, x_4) = (s, t). Columns s = 2, ..., L - 1: c3(t)(zeta(s + 1, t) -
zeta(s, t)) = 0, so zeta(2, t) = ... = zeta(L, t) = zeta(0, t) =: a_t. Put b_t = zeta(1, t), e_t = b_t - a_t. Then
  column 0:  (c3(t) + psi_t - psi_(t-1)) e_t = psi_t (a_(t+1) - a_t),
  column 1:  c3(t) e_t = psi_t (b_(t+1) - b_t).
Subtracting, psi_t e_(t+1) = psi_(t-1) e_t, so psi_(t-1) e_t = m does not depend on t. Summing column 1 divided by
psi_t over t in Z_L: 0 = sum_t (b_(t+1) - b_t) = m S. So m = 0, e = 0, b is constant, a = b. QED (b).
Proof of (a). Conservation: direction 1 and direction 2 contribute c - c = 0 at each site; in directions 3, 4 at
(0, t): c3 + psi_t - psi_(t-1) - psi_t - c3 + psi_(t-1) = 0; at (1, t): c3 + psi_t - c3 - (psi_t - psi_(t-1)) -
psi_(t-1) = 0; elsewhere c3 - c3. With (d* phi)_(x,mu) = sum_(nu not mu) (phi_(mu nu)(x) - phi_(mu nu)(x - e_nu)):
a function g on the 3-torus transverse to direction mu with sum 0 is a sum of three backward differences
(g minus its average in one direction, and so on), g = sum_nu (chi_nu - chi_nu(. - e_nu)); put phi_(mu nu) = chi_nu.
This gives the first two lines. For the last two, phi_34(x) = [x_1 = 0][x_2 = 0] (Phi(x_4) + psi_(x_4) [x_3 = 0])
with Phi(t) - Phi(t - 1) = c3(t). QED
Control (GUIDE, script `fstar.py` in the same scratch folder): rank 80 of 81, 255 of 256, 624 of 625 for
L = 3, 4, 5 with the example values; divergence 0, flux 0. A random abelian configuration also gave rank V - 1.

Remark (why the construction has this shape). T_f h = 0 says h is constant along the flow of f. Straight lines
alone leave one free constant per line, and the reduction from d to d - 1 dimensions (lines plus a current on one
slice) is exact; it ends in one dimension, where a co-exact current is zero. So the last step must be truly
two-dimensional. In the 2D continuum the kernel is all functions of the stream function; on the lattice the
identity psi_(t-1) e_t = m with S not 0 removes it.

**Theorem E.** Torus Z_L^4, L >= 3, any beta > 0. There is a non-empty open, gauge-invariant set GG of
configurations and, near each of its points, a smooth map U -> n(U) in (S^2)^V with div j(U, n(U)) = 0. Almost every
point of GG is non-reducible, and there D n is not 0. GG has positive Wilson measure.

Proof. (1) Abelian point. For a real link field a put U_l = exp(a_l e), e a fixed unit vector. Then every
plaquette is exp(F_p e), F = d a, A = beta sum_p cos F_p, and N_l = f_l e with f = (sign) beta d* sin(d a); the sign
convention does not matter below. (2) Choice of a. By linear algebra im d* = d*(im d + ker d*) = im(d* d), so there
is a_0 with d* d a_0 = f* (Lemma RANK (a)). Let mm be a (V - 1)-minor of T_f with mm(f*) not 0; it is a homogeneous
polynomial of degree V - 1 in f. Since sin y = y + O(y^3), mm(f(eps a_0)) = (beta eps)^(V-1) mm(f*) + O(eps^V), not
0 for small eps > 0. Fix such an eps: U_0 = exp(eps a_0 e), f_0 its force field, rank T_(f_0) = V - 1.
(3) A solution at U_0. For |c| < 1 and unit m_x orthogonal to e, n_x = c e + sqrt(1 - c^2) m_x has j = c f_0,
conserved. (4) Transversality. Phi(U, n) = div j is polynomial in (U, n) with values in R^V_0 (sum zero). Its
derivative in n at (U_0, n) along delta n_x = g_x (e - c n_x)/(1 - c^2) (tangent, with delta n_x . e = g_x) is
g -> div(g f_0), whose transpose is - T_(f_0). So it has rank V - 1 and is onto R^V_0. (5) Implicit function theorem:
for U in a neighbourhood UU of U_0 there is a smooth n(U) with Phi(U, n(U)) = 0. (6) If n solves at U then Ad(g) n
solves at U^g, so GG = the gauge orbit of UU is open and gauge invariant. Open and non-empty gives positive Wilson
measure (the density e^A is positive). Reducible configurations lie in the zero set of the polynomial
|s_p x s_q|^2 for two plaquettes at one site, which is not identically zero; so they are a null set, and on a
non-reducible configuration every frame has D n not 0 (Lemma FR). QED

Not proved: that GG has full measure (the GUIDE run found a frame on 6 of 6 typical configurations); a globally
smooth gauge-covariant selection on GG (locally it exists by the theorem; ARGUED that it can be made covariant by
choosing n on a local slice of the gauge action and extending by Ad(g)).

**Consequence for D2.** The repair proposed in check 1022 ("elsewhere only if a frame with D n orthogonal to the
forces in this summed sense exists (OPEN)") is settled: such frames exist, on an open set of positive measure
(PROVED), on almost every configuration of one cube (PROVED), and at every typical configuration tried (GUIDE).
Sentence L275 of row 1018, for the conserved-current half, is false. The first alternative of the row (no frame on
an open set of positive measure) is not available as the general statement; whether some other open set has no
frame is OPEN and was not found (0 failures in 6).
