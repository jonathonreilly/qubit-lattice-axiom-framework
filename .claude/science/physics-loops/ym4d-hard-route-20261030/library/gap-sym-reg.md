# gap-sym-reg (queue row 1034): (SYM) with (REG) for route (ii), covariant frame moves
Worker: Claude Fable 5.2, medium effort, background agent on the lead's MacBook. Started Mon Nov 16 03:39:30 UTC 2026. Checked by: nobody.

## Plan (at most eight steps; each result is written here before the next step starts)

1. Read FINISH.md rules and row 1034, GOAL.md. Record the exact question.
2. Read the named sources (parts/gap.md; gap-short-step-max 4.1-4.5 and its two checks; gap-aligned-frame and its check). Record the definitions of (SYM), (REG), j, d, Psi.
3. Grep the lane for prior work on covariant frames, curl forms, conserved currents.
4. Test by hand: compact U(1) (must pass with zero gain), one cube, the 3^4 torus with links i, j, k, 1.
5. Decide: attempt the proof of a local covariant frame with conserved square-integrable j - d, or build the counterexample.
6. Write the decided statement with full proof.
7. Write the consumer (curl bound with constants) or the exact scope of the no-go.
8. Final marks and the RESULT line.

Research-stage working state. Nothing here is a public claim. Pinned at commit 49af837cc, branch `claude/ym4d-hard-route`.
Credit: the construction this lane builds on is by Sussman and Alpoge, on Balaban's renormalisation group. Their account has no colour-frame statement (check 1027, Step 1), so nothing is ported here.

## Step log

### Step 1 (done): the brief and the exact question

Read: FINISH.md "How we work", "Working efficiently", "Rules", and row 1034; GOAL.md (no computer-assisted step; marks).
The statement to decide, **(SYM) with (REG)**: on 4D lattice SU(2) at order-one coupling there is a local, gauge-covariant
unit-vector frame n of finite range, whose current j - d is conserved and square integrable, on a set of configurations of
positive Wilson measure, so that the cost of the frame move is a curl form. Two outcomes count: a proof with its consumer (the
curl bound, with constants), or a counterexample.

### Step 2 (done): sources read; definitions fixed

Read in full: `library/gap-aligned-frame.md` (row 1026); `library/gap-aligned-frame-check-opus.md` (row 1027);
`library/gap-short-step-max.md` Section 4 (L213-277); `library/gap-short-step-check-astra.md` items 9-10 and the comparison
table; `library/gap-pinned-cell-gauge-max.md` 3.1-3.2, 4.1-4.3, 7.3-7.4; `parts/gap.md` L1-30, L140-141.

Conventions (row 1011 3.1-3.2). SU(2) = unit quaternions, su(2) = Im H = R^3, t(g) = Re g, s(g) = Im g. A link l = (x -> y)
has tail x and head y. Gauge: U_l -> g_x U_l g_y^(-1). Plaquette (x; mu, nu): U_p = U_1 U_2 U_3^(-1) U_4^(-1). The measure is
mu = e^A dU, A = sum_p beta_p w_p t_p. R_(l,a) f = (d/d eps) f(U_l -> e^(eps e_a) U_l). The force is N_l with R_(l,a) A = - N_l^a.
A frame is a field of unit vectors n_x(U), gauge covariant. j_l = n_tail(l) . N_l. d_l = sum_a R_(l,a) n^a_tail(l).
D_l n = n_tail - Ad(U_l) n_head. The frame move is V_theta = sum_l theta_l n_tail(l) . R_l. Remark JAC of row 1026:
Psi_theta = V A + div V = - sum_l theta_l c_l with c_l := j_l - d_l.
(J): sum_l (d lambda)_l c_l = 0 for every lambda that is zero at pinned sites. (LOC): n_x depends on the links within distance r
of x, by the same rule at every site. (REG) (check 1027): n is smooth off a closed null set, c_l is in L^2, and
E[V f] = - E[f Psi_V] for smooth f.
(SYM) with (REG) = a frame with (J), (LOC), (REG) on a set of positive measure.

### Step 3 (done): repo search (rule "Repo first", rule 0a)

- Grep of this folder for "(SYM)": rows 1026, 1027, 1034 and `parts/gap.md` L141 use it in this sense. The hits in
  `gap-mid-max.md`, `gap-mid-check.md`, `gap-target-max.md`, `gap-afield-a-max.md` are a different "(SYM)" (symmetric states
  of a bootstrap). No row attacks (SYM) with (REG) before this one.
- Grep for "staple", "link frame", "frame current", "Jacobian current": the staple hits are heat-bath conditional laws
  (rows on block criteria and numerics). No hit states the exact link symmetry of Lemma STAPLE below.
- Nearest prior results, all used below with credit: Lemma FLOW, PROJ, FR+, SPLIT (row 1018, Claude Fable 5.2); Lemma FR,
  Lemma CEN, Propositions A, B, B' (row 1011); Remark JAC, Theorem E, the cost identity (row 1026); (REG) and the corner
  frame's infinite cost (check 1027, Claude Opus 5.5); the odd-torus example (gpt-6-astra check of row 1018, item 10).
- A search of origin/main with `git grep` was started and stopped after 120 s without output (the clone fetches blobs
  on demand). So main and the other PR branches were NOT searched by this row. The lead's search for row 1026 found no
  colour-frame text there (as reported in row 1026 and check 1027); I rely on that and say so.

### Step 4 (done): two exact identities, then the hand tests

All of Step 4 is PROVED by hand here unless marked. Nobody checked it.

**4.0 Identity LINK and identity STAR.**

LINK. For every link l with tail x:  c_l = j_l - d_l = - e^(-A) sum_a R_(l,a)(e^A n_x^a).
Proof: R_(l,a) e^A = - e^A N_l^a. QED
So c_l is minus the divergence, for the measure mu, of the single-link field n_x . R_l. The current is defined link by link.
(J) is linear in w_x := e^A n_x; the only non-linear condition is |w_x| = e^A.

STAR. Let z be a free site, out(z) and in(z) its outgoing and incoming links. For a covariant frame, differentiable at U,

  sum over l in out(z) of c_l = - e^(-A) sum over l in in(z) of sum_a R_(l,a)( e^A (Ad(U_l) n_z)^a ).

So (J) at z reads  sum over l in in(z) of sum_a R_(l,a)( e^A (D_l n)^a ) = 0:  the field Y_z = sum over in(z) of (D_l n) . R_l
preserves mu. In the notation of row 1026 this sum equals - e^A rho_z, rho_z = sum over in(z) of (D_l n) . N_l + (div d)(z).
Proof. The gauge generator at z with a fixed axis e_a is G_a = sum_out e_a . R_l - sum_in (Ad(U_l) e_a) . R_l. It is divergence
free for Haar measure (a one-parameter group of isometries) and G_a A = 0. Covariance gives G_a n_z = [e_a, n_z] = 2 e_a x n_z.
So the field sum_a n_z^a G_a has mu-divergence sum_a (G_a n_z)^a = sum_a (2 e_a x n_z) . e_a = 0. Its outgoing part is
sum_out n_z . R_l, with mu-divergence - sum_out c_l by LINK. Its incoming part is - sum_in (Ad(U_l) n_z) . R_l. QED
Consequence: at a site with no incoming link (the corner 000 of a free cube) the outflow sum_out c_l is zero for every
covariant frame. Conservation there costs nothing.

**4.1 Compact U(1) (the control).** One axis, Ad trivial, n constant, D n = 0, d = 0, c = N. The Gauss law is conservation, at
free sites and at boundary sites of a pinned cell. c = d* phi with phi_p = beta sin F_p. Psi_theta = - sum_p (d theta)_p beta sin F_p
and Q(theta) = sum_p beta E[cos F_p] (d theta)_p^2 <= beta sum_p (d theta)_p^2. This is the classical bound: zero gain. Each
statement below is checked against this case: Lemma STAPLE gives the zero field (1 - Ad = 0); Lemmas PRIV and BD conclude
D n = 0, which is true; Proposition CURL gives the constant beta E[cos F]. So U(1) passes trivially and gains nothing.

**4.2 One plaquette (from row 1026 Step 3, checked in 1027).** Axis frame, c = h(phi)(1, 1, -1, -1), h = beta sin phi - 2 cot phi.
So c = d* phi_p with phi_p = h, and (REG) holds (the singular set s = 0 has codimension 3). A plaquette is reducible.

**4.3 One free cube {0,1}^3 (8 sites, 12 links, 6 plaquettes).**
- 000 has no incoming link: conservation there is automatic (STAR).
- 110, 101, 011 have one outgoing link each. Lemma STAPLE (Step 6) gives a covariant unit vector n_110 with c = 0 on the
  link (110 -> 111) identically: rotate about the axis of the plaquette (000; 1, 2) carried to 110, a loop that does not
  use that link. The same at 101 and 011. Then the inflow at 111 is zero, and 111 is conserved. n_111 does not enter.
- The six equations left: at 110, 101, 011 the inflow from two links must vanish; at 100, 010, 001 the outflow on two
  links must equal the inflow on one. The unknowns are n_000, n_100, n_010, n_001: eight functions. Each equation is a
  first-order partial differential equation. I found no closed solution.
- The frames of row 1026 Step 4 (j = 0 on every link) solve none of this: j = 0 forces n_000 = +-(N_1 x N_2)/|N_1 x N_2|,
  and then d_1 = - beta (N_1 . s_r)/|N_1 x N_2| is not square integrable (check 1027, Step 5). So for the cube:
  conservation holds at 000 (automatic) and at 111 (with the STAPLE vectors at 110, 101, 011); the six equations at
  the other sites are OPEN.
- Lemma PRIV (Step 6) on the cube: the link (101 -> 111) lies in one plaquette through the link (100 -> 110) and in no
  other plaquette at 110. If n_110, n_100, n_010 do not depend on it, conservation at 110 forces D n = 0 on (100 -> 110).

**4.4 The 3^4 torus and the odd-torus example (U_1 = i, U_2 = j, U_3 = k, U_4 = 1; astra check, item 10).**

Lemma SING. Let n be a covariant frame of range r on Z_L^4, L >= 2r + 2, defined on a gauge-invariant set. Let U be a
configuration whose links inside the box B of side 2r + 1 around x are gauge equivalent, on B, to links with values +-1.
Then n_x is not defined at U.
Proof. Let U' be that central configuration on B. Every constant g on B fixes U' on B. n_x reads only B, so covariance
gives n_x(U') = Ad(g) n_x(U') for all g in SU(2). No unit vector has this property. n_x(U) = Ad(h_x) n_x(U') would be
defined if n_x(U) were. QED

The example is of this kind on every box that does not wrap: g_x = i^(x_1) j^(x_2) k^(x_3) gives g_(x+mu) = +- g_x U_mu, so
g_x U_mu g_(x+mu)^(-1) = +-1. So **the example lies in the singular set of every local covariant frame.** It tests nothing
about (SYM): its conserved current (zero forces) belongs to no frame of finite range. That set (all local holonomies central)
has large codimension; it does not threaten (REG).

On Z_3^4 itself every box wraps, and a frame can read the winding loops. Test frame: n_x = axis of the direction-1 winding
loop P(x) = U_(x,1) U_(x+1,1) U_(x+2,1). At the example P = i^3 = -i, so n_x = -i at every site. Then
D_(x,1) n = 0 identically (P(x) = U_(x,1) P(x+1) U_(x,1)^(-1)), D_(x,4) n = 0, and D_(x,2) n = -i - Ad(j)(-i) = -2i,
D_(x,3) n = -i - Ad(k)(-i) = -2i. So the frame is not covariantly constant, as the astra check says.
Its Jacobian current: d_(x,1) = 2 cot(phi_P), d = 0 on the other links (the one-plaquette computation with P in place
of U_p). phi_P does not depend on the base point, so div d = 0 identically, and d is in L^2 (the conditional density of P
is bounded and cot^2 phi sin^2 phi is integrable). So (REG) holds and (J) is the alignment condition
sum over mu = 2, 3, 4 of (D_(z-mu,mu) n) . N_(z-mu,mu) = 0. At the example N = 0 and it holds. Near the example it fails:
the frame reads direction-1 links only, so Lemma PRIV applies for mu = 2, 3, and conservation on a set of positive measure
would force D_(z-2,2) n = 0 there; but D_(z-2,2) n is close to -2i near the example. So this frame has j - d conserved at
the example and at no set of positive measure around it. Its range is L, so it is not local in any case.
Verdict of the test: the example gives no frame for (SYM). It shows that zero forces are not a model of a conserved current.

- Mon Nov 16 04:09:14 UTC 2026 (`date -u`). Step 4 written.

### Step 5 (done): the decision

The statement splits into three, and they get three different answers.

1. **Frames that sit on links** (one covariant unit vector n_l per link, in the frame of its tail; finite range; same rule).
   (SYM) with (REG) is TRUE, on almost every configuration, with c_l = 0 on every link (Lemma STAPLE, Proposition LF).
   Its consumer is empty: Psi_theta = 0 for every interior theta, so the move changes no bound. Zero gain.
2. **Frames that sit on sites** (the row's object), in the bulk. Not decided in general. PROVED: conservation on a set of
   positive measure is impossible for every frame that does not read the links parallel to an incoming link across its
   forward plaquettes (Lemma PRIV, Corollary P). This class contains every frame built from the past of its site (the
   frames with d = 0 for a structural reason, where (REG) is free), every frame built from the links of two directions,
   and the winding-loop frame of 4.4. PROVED: no site frame has j = 0 on a set of positive measure in four dimensions
   (Lemma SPAN). OPEN: a site frame that reads those forward links (Lemma O1 in Step 7).
3. **At the pinned boundary of a cell** (where the consumer of row 1026 7.1 acts). FAILS, PROVED: for a site frame
   whose values at boundary sites are functions of the pin, the current is not conserved at any site of a lower face
   unless D n = 0 on the face links, that is on reducible pins only (Theorem BD). So the cost of a boundary rotation
   theta n is invariant under interior gradients only. It is a function of d theta and of theta on the boundary links.
   It is not a curl form in the sense the U(1) bound has.

So I build no frame for the row's statement and no counterexample that covers all site frames. What is proved cuts the
statement down from both sides, and Step 7 states the one lemma left, with the three attacks that failed.

### Step 6 (done): statements and proofs

All PROVED by hand here. Nobody checked them. Each proof uses only: Haar invariance, the product rule, Fubini, and the fact
that an affine function on R^4 that vanishes on a subset of S^3 of positive measure is zero on S^3.

**6.1 Lemma STAPLE (an exact field-dependent symmetry on one link).**
Fix a link l = (x -> y). Write A = Re(U_l S_l) + A', where S_l = sum over the plaquettes p through l of beta_p w_p sigma_p is
the staple sum (each sigma_p is a product of the three other links of p, a path from y to x) and A' does not contain U_l.
Then N_l = Im(U_l S_l). Where kappa_l := |S_l| > 0 put Mh_l := U_l S_l / kappa_l in SU(2), a loop at x.
Let a be an R^3-valued function of the configuration that does not depend on U_l. Put

  b_l := a - Ad(Mh_l) a.

Then (i) b_l . N_l = 0; (ii) sum_c R_(l,c) b_l^c = 0; (iii) b_l . R_l |b_l|^2 = 0. Hence both b_l . R_l and, where b_l is not 0, the
unit field n_l := b_l/|b_l| have c_l = j_l - d_l = 0 with j_l = 0 and d_l = 0: the single-link move along n_l preserves
e^A dU. If a is a covariant vector at x, so are b_l and n_l.
Proof. (i) Ad(Mh) fixes Im Mh, and N_l = kappa Im Mh, so (a - Ad(Mh) a) . Im Mh = 0. (ii) Under U_l -> e^(eps e_c) U_l, Mh ->
e^(eps e_c) Mh, so R_(l,c)(Ad(Mh) a) = [e_c, Ad(Mh) a] = 2 e_c x Ad(Mh) a (a does not depend on U_l), and
sum_c (2 e_c x v) . e_c = 0. (iii) |b|^2 = 2 |a|^2 - 2 a . Ad(Mh) a, so R_(l,c) |b|^2 = - 4 e_c . (Ad(Mh) a x a), and
b . (Ad(Mh) a x a) = 0 because both a and Ad(Mh) a lie in the plane of the cross product's factors. Then
sum_c R_(l,c)(b^c/|b|) = (1/|b|) sum_c R_(l,c) b^c - (1/(2 |b|^3)) b . R_l |b|^2 = 0, and n . N = 0 by (i). QED
Meaning: the flow of b_l is U_l S_l -> e^(s a) U_l S_l e^(-s a), a conjugation of the loop U_l S_l about the axis a; it keeps
Re(U_l S_l) and is an isometry of the link. The flow of n_l is the same rotation at unit speed.

**6.2 Proposition LF ((SYM) with (REG) holds for link frames, and gives nothing).**
For each direction mu choose a plaquette q_mu based at the origin that does not contain the link (0, mu) (for instance
q_1 = (0; 2, 3)), and put a_l := s of the translate of q_mu to the tail of l, for l = (x, mu). Let n_l be the unit field of 6.1.
Then n_l is gauge covariant in the frame of the tail, of range 2, given by the same rule at every link, and defined off the
set Z_l = {kappa_l = 0} or {s_q x N_l = 0}. Z_l is a proper real-analytic subset, so it is closed and null. (Witness for l = (x, 1), q = (x; 2, 3),
homogeneous beta: U_(x + e_1, 2) = exp(phi i), U_(x + e_2, 3) = exp(phi j), all other links 1. Then N_l = beta sin(phi) i,
s_q = sin(phi) j, and kappa_l > 0 for small phi.) On the complement c_l = 0. For every bounded C^1 function f, E[n_l . R_l f] = 0.
So for the link field V_theta = sum_l theta_l n_l . R_l: Psi_theta = 0 for EVERY theta on free links, (J) and (REG) hold with the
current identically zero, and e^(pi n_l) = -1.
Proof of the integration by parts. Fix the other links. The time-s map of n_l is Phi_s: Mh -> e^(tau a) Mh e^(-tau a) with
tau = s/|b_l|. |b_l| is constant on the orbits (6.1 (iii)), the orbits are orbits of a circle group of isometries of S^3, and
Haar measure disintegrates over them with rotation-invariant conditional measures. So Phi_s preserves Haar measure on the
link, and it keeps Re(U_l S_l). Hence Phi_s preserves e^A dU, and 0 = (d/ds) E[f o Phi_s] = E[n_l . R_l f] by dominated
convergence (|n_l . R_l f| <= sup |grad f|). QED
**The consumer is empty.** In Lemma FLOW take the boundary rotation B and the interior extension theta n. Then
Psi_V = - sum over boundary links of B_l . N_l: the interior part adds nothing, Psi_V is the same function as for the extension by
zero, and - E[V Psi_V] = H_c + Var(Psi_V) is the same number. A flow that preserves the measure is a change of variables. It
cannot lower a bound. This is the control result of the row: **conservation in the interior, with (REG) and finite range,
does not by itself give route (ii) anything. All of the content is at the pinned links.**
U(1): 1 - Ad = 0, the field is zero. Passes with zero gain.

**6.3 Lemma SPAN (no site frame with zero projected current).** Lattice Z^4, a box, or a torus with L >= 3; beta_p w_p > 0.
At a site x whose plaquettes are all present, the forces N_(x,1), N_(x,2), N_(x,3) are linearly independent off a null set.
So no unit vector n_x has j = 0 on three outgoing links on a set of positive measure. The mechanism of 6.1 (j = d = 0)
cannot give a site frame.
Proof. For mu = 1, 2, 3 put nu = mu + 1 and Q_mu := the link (x - e_nu, mu). The plaquette (x - e_nu; mu, nu) contains Q_mu and
(x, mu). No other plaquette through an outgoing link of x contains Q_mu (the plaquettes through (x, kappa) are
(x; kappa, lambda) and (x - e_lambda; kappa, lambda); compare their eight links with (x - e_nu, mu)). So
N_(x,mu) = N0_mu + beta w Im(g_mu Q_mu^(-1) h_mu), with N0_mu, g_mu, h_mu and the other two forces independent of Q_mu.
Im(g Q^(-1) h) takes every value in the unit ball. So det(N_1, N_2, N_3), a polynomial in the link entries, is not
identically zero, and its zero set is null. If n . N_mu = 0 for mu = 1, 2, 3 then the determinant is zero. QED

**6.4 Lemma PRIV (a frame that does not read a forward parallel link cannot leak through the link behind it).**
Lattice as in 6.3 (torus: L >= 3; the incidence count below was redone modulo 3). Let z be a free site, mu != nu, l := (z - e_mu, mu), P := the link (z - e_mu + e_nu, mu),
p := the plaquette (z - e_mu; mu, nu), with beta_p w_p > 0 and P a free link. Let Omega = Omega' x SU(2) (the last factor is
U_P) be an open set on which n_z and n_(z - e_kappa), kappa = 1, ..., 4, are C^1 and do not depend on U_P. If rho_z = 0 on a subset
Omega_0 of Omega of positive measure, then D_l n = 0 almost everywhere on Omega_0.
Proof. rho_z = sum over l' in in(z) of (D_l' n) . N_l' + (div d)(z), and (div d)(z) = sum_out R_l' . n_z - sum_in R_l' . n_tail(l').
P is not a link at z, so every derivative here is in a link other than P, of a function that does not depend on U_P.
So (div d)(z) and all D_l' n do not depend on U_P. The plaquettes through P are (y; mu, lambda) and (y - e_lambda; mu, lambda)
with y = z - e_mu + e_nu. Among their links the only incoming link of z is l, in the plaquette p (lambda = nu). So among the
forces at in(z) only N_l contains U_P, and N_l = N0 + beta_p w_p Im(g U_P^(-1) h) with g = U_l U_(z,nu), h = U_(z - e_mu, nu)^(-1).
On each fibre {U'} x SU(2):  rho_z = alpha(U') + beta_p w_p (D_l n)(U') . Im(g U_P^(-1) h).
By Fubini, for almost every point of Omega_0 the fibre through it meets Omega_0 in a set of positive Haar measure. On such
a fibre the right side is an affine function of U_P in R^4 that vanishes on a subset of S^3 of positive measure. So it
vanishes on S^3. Choose U_P with g U_P^(-1) h = +v and then -v, v a unit imaginary quaternion: (D_l n) . v = 0 for all v. QED
The same proof gives: if rho_z is almost surely equal to a constant on Omega_0, then D_l n = 0 there.
U(1): the conclusion D n = 0 is true. Passes.

**6.5 Corollary P (classes of site frames with no conserved current).** Let n be a site frame with a translation-invariant
rule that reads the links x + D. For mu != nu put
  F_(mu nu) := { (- e_mu + e_nu, mu) } and { (e_kappa - e_mu + e_nu, mu) : kappa = 1, ..., 4 }   (five links; mu is the direction).
Suppose that for two directions mu != mu' there are nu, nu' with D disjoint from F_(mu nu) and from F_(mu' nu'). Then (J)
does not hold at all sites on any set of positive measure where n is C^1.
Proof. Lemma PRIV applies at every site for (mu, nu) and (mu', nu'). So D n = 0 on all links of directions mu and mu',
almost everywhere on the set. Take p = (x; mu, mu') and p' = (x + e_mu; mu, mu'). The telescoping identity of Lemma FR
(row 1011 7.3) gives (1 - Ad(U_p)) n_x = 0 and (1 - Ad(U_p')) n_(x + e_mu) = 0, so s_p x n_x = 0 and s_p' x n_(x + e_mu) = 0, and
n_x = Ad(U_(x,mu)) n_(x + e_mu). Hence s_p x Ad(U_(x,mu)) s_p' = 0 on the set. This is a polynomial equation. It fails at the
configuration with U_(x + e_mu', mu) = exp(- phi i), U_(x + e_mu + e_mu', mu) = exp(- phi j), all other links 1 (then U_p = exp(phi i),
U_p' = exp(phi j), s_p x s_p' = sin^2(phi) k). So the set is null. QED
Classes covered.
- (a) **Past frames**: D inside the links with both end points y with y_1 + y_2 + y_3 + y_4 <= 0. Every link of every
  F_(mu nu) has a head with coordinate sum 1 or 2. These frames have d = 0 (they do not read their outgoing links), so
  (REG) is free for them; and their current is never conserved. This includes the plaquette-behind frame of Remark BACK
  (row 1026) and every frame built from backward loops.
- (b) Frames that read links of at most two directions (for instance the axis of one plaquette (x; 1, 2), or of any
  loops in one plane): F_(3 nu) and F_(4 nu) consist of links of directions 3 and 4.
- (c) The winding-loop frame of 4.4 (reads direction 1 only).
- (d) The frame N_(x,1) x N_(x,2) normalised (the bulk analogue of the cube's corner frame): it reads no link of
  F_(3 4) = {(- e_3 + e_4, 3), (e_kappa - e_3 + e_4, 3)} and none of F_(4 3). (Checked against the plaquettes through (x, 1), (x, 2).)
**Necessary condition for a site frame with (J):** for at least three of the four directions mu, and every nu != mu, the
frame reads a link of F_(mu nu). The link (e_nu + e_nu' - e_mu, mu) lies in both F_(mu nu) and F_(mu nu'), and no link lies in three of
the sets, so the frame reads at least two such links in each of three directions: at least six forward links, each
parallel to an incoming link across a forward plaquette (as seen from z or from a backward neighbour of z).

**6.6 Theorem BD (no conservation at a pinned lower face).** Cell c = box with sides S_1, ..., S_4, S_4 >= 2. Let z be a
site in the relative interior of the face {x_4 = 0}, with beta_p w_p > 0 on the plaquettes (z - e_i; i, 4), i = 1, 2, 3. Take a
site frame whose values at z and at z - e_1, z - e_2, z - e_3 are functions of the pin omega only (as in the consumer of row
1026 7.1). Let lambda be the indicator of z and V = (d lambda) n: the boundary rotation on the six face links at z, and n_z on
the interior link (z, 4). Then Psi_V = sum over i = 1, 2, 3 of (D_(z - e_i, i) n)(omega) . N_(z - e_i, i)(U), and if Psi_V is almost
surely constant under the law of the cell with pin omega, then D_(z - e_i, i) n(omega) = 0 for i = 1, 2, 3.
Proof. Psi_V = V A + div V. div V = 0: the only interior link moved is (z, 4), along n_z(omega), a fixed vector. V A =
- sum_out n_z . N_l + sum_in n_tail(l) . N_l, where out(z) is three face links and (z, 4), and in(z) is three face links. The cell
action is gauge invariant at z (pinned links included), so sum_out N_l = sum_in Ad(U_l)^(-1) N_l (Lemma PROJ (ii)), and
V A = sum_in (n_tail - Ad(U_l) n_z) . N_l. Now N_(z - e_i, i) contains the interior plaquette (z - e_i; i, 4), whose link
P_i = (z - e_i + e_4, i) is a free interior link (z is in the relative interior of the face and S_4 >= 2), and P_i is in no other
plaquette through a link of in(z) (the count of 6.4 with mu = i, nu = 4). D n is a fixed vector. So Psi_V is affine in each
P_i with linear part beta w (D_i n) . Im(g_i P_i^(-1) h_i), and the proof of 6.4 gives D_i n = 0. QED
Consequences.
- If D n = 0 on the face links at every such z (S_1, S_2, S_3 >= 3), the face plaquette axes at each site are parallel
  (Lemma FR): a null set of pins. So for almost every pin Psi_(d lambda) is not constant for some boundary lambda.
- By Lemma FLOW, equality H_c = - E[V Psi_V] holds only if Psi_V is constant. So for these gradients
  Q(d lambda) = H_c(omega; (d lambda) n) + Var(Psi_(d lambda)) with Var > 0, while the curl sum of d lambda is 0.
- **The cost of a boundary rotation theta n is invariant under theta -> theta + d lambda only for lambda zero at the pinned
  sites.** So Q is a function of d theta and of theta on the boundary links. Remark JAC's "quadratic form in d theta" holds for
  interior theta only (check 1027 already limits it to a box cell and to theta zero on the boundary; this is the reason).
- The same proof works on each face {x_mu = 0}. The faces {x_mu = S_mu} are not covered: there the private link is an
  incoming link of an interior site, and an interior frame may read it.
- Scope: one unit vector per boundary site, used on the face links and on the interior link out of that site, and
  measurable in the pin. A rotation with a different frozen vector on each boundary link is not covered.
- Not proved: that Q(d lambda) > 0 on a set of pins of positive measure (the curl INEQUALITY would need Q(d lambda) <= 0).
  The exact value is Q(d lambda) = E[direct term of b] - 2 sum over in(z) of (n_tail x Ad(U_l) n_z) . E[N_l], b_l = - D_l n, from
  e^(eps (d lambda) n) U = gauge transform of exp(- eps n_tail) exp(eps Ad(U_l) n_z) U_l on in(z). Its sign depends on the frame.
U(1): D n = 0, Psi = 0, the Gauss law holds at boundary sites. Passes; this is where U(1) and SU(2) differ.
- Mon Nov 16 04:11:33 UTC 2026 (`date -u`). Step 6 written.

### Step 7 (done): the consumer, its limits, and the lemma that stays open

**7.1 Proposition CURL (the curl bound, conditional, with its constant). PROVED given its hypotheses.**
Let W be a set of free links and n a field of unit vectors on W (a site frame or a link frame). Suppose there are functions
phi_p on the plaquettes with
 (a) c_l = sum over p through l of [p : l] phi_p for every l in W ([p : l] = +1 on l_1, l_2 and -1 on l_3, l_4), so that
     Psi_theta = - sum_p (d theta)_p phi_p for theta supported in W;
 (b) phi_p is in L^2 and depends only on links at distance at most R from p;
 (c) (REG) for these functions: E[V_theta phi_p] = - E[phi_p Psi_theta] and E[V_theta Psi_theta] = - E[Psi_theta^2], theta supported in W.
Put m = 2R + 3 and k_1 = sup over p of sum_l |E[n_l . R_l phi_p]|. Then for every theta supported on links at distance more than m
from the complement of W:

  Q(theta) = E[Psi_theta^2] <= 4 m^4 k_1 sum_p (d theta)_p^2.

Proof. By (c) and (a), Q(theta) = sum_p (d theta)_p E[V_theta phi_p] = sum_p (d theta)_p Lambda_p(theta), with
Lambda_p(theta) = sum_l K(l, p) theta_l and K(l, p) = E[n_l . R_l phi_p]. K(l, p) = 0 unless phi_p depends on U_l, so l lies in the box
B_p of m sites per side around p. For lambda supported on the sites of B_p, Psi_(d lambda) = 0 by (a) (d d = 0), so
Lambda_p(d lambda) = - E[phi_p Psi_(d lambda)] = 0. Choose lambda so that theta' = theta - d lambda is zero on the comb tree of B_p (all
direction-1 links; direction-2 links with first coordinate 0; direction-3 links with first two coordinates 0; direction-4
links with first three coordinates 0, coordinates from a corner of B_p). Each other link l of B_p closes a loop with the
tree that bounds a strip Sigma_l of at most 3 m plaquettes, and theta'_l = sum over Sigma_l of +-(d theta)_p'. So
|Lambda_p(theta)| <= sum_p' kappa(p, p') |(d theta)_p'| with kappa(p, p') = sum over l with p' in Sigma_l of |K(l, p)|. The row sums are
at most 3 m k_1. For fixed p' at most 6 m^4 plaquettes p have p' in B_p, and kappa(p, p') <= k_1, so the column sums are at
most 6 m^4 k_1. With |x y| <= (x^2 + y^2)/2: Q(theta) <= (1/2)(3 m + 6 m^4) k_1 sum (d theta)^2 <= 4 m^4 k_1 sum (d theta)^2. QED
Remarks.
- The bound is blind: it uses no decay of correlations. It needs the potential phi, not only conservation. A bound through
  E[phi_p phi_p'] would need a susceptibility; the integration by parts replaces it by the finite-range kernel K.
- Checks. U(1): phi_p = beta sin F_p, K(l, p) = [p : l] beta E[cos F_p], and the first line of the proof gives
  Q = sum_p beta E[cos F_p] (d theta)_p^2 exactly: the classical bound, zero gain. One plaquette (4.2): K = +-E[beta cos phi + 2/sin^2 phi],
  the value of row 1026 Step 3. Link frames (6.2): phi = 0, Q = 0.
- The constant 4 m^4 k_1 is not optimised, and k_1 is not known against beta, because no site frame with a potential is known.

**7.2 From (J) to the potential.**
Lemma FLUX (PROVED). Torus Z_L^4. Let c be a current of range R' (c_(x,mu) depends on links at distance at most R' from x),
L >= 4 R' + 4, conserved almost everywhere, with E[c_l] = 0 (this is (REG) with f = 1). Then for each t the flux
T_t = sum over x with x_4 = t of c_(x,4) is zero almost everywhere.
Proof. Summing conservation over a slab gives T_t = T_t' for all t, t'. Take t' with the two ranges disjoint. The Wilson
measure is equivalent to the product Haar measure, and two functions of disjoint sets of independent variables that are
equal almost everywhere are constant. The constant is E[T_t] = 0. QED
So the closed, non-exact slab field also has Psi = 0: a continuous family of maps that preserve the measure, where the
centre gives only a sign.
Lemma POT (ARGUED, not proved here): a conserved current of finite range with zero fluxes is d* phi with phi of finite
range. This is the local Poincare lemma for difference forms. RECALLED from memory (Hydon and Mansfield, variational
complex for difference equations, 2004); not fetched; used in no proof. With POT, (J) + (LOC) + (REG) give the
hypotheses of 7.1.

**7.3 What the consumer needs beyond (SYM) (reading; the two facts behind it are PROVED in 6.2 and 6.6).**
- A measure-preserving interior flow changes no bound (6.2). The interior moves help only through the cancellation of
  the boundary current sum over pinned links of theta_l n_l . N_l against the interior current. For U(1) the Gauss law at the
  boundary sites gives that cancellation, and Psi = - sum_p (d theta)_p beta sin F_p with p over ALL plaquettes of the cell.
- For SU(2) with a site frame the Gauss law at a pinned lower-face site leaves the defect sum (D n) . N, which the site
  frame cannot remove (6.6; a different vector on the interior link out of the site is outside 6.6). So the curl bound of 7.1 holds, if at all, for interior theta only, and the cost of a boundary
  rotation keeps a term in theta on the boundary links. For the potential of a constant field strength f on a cube of side
  S the boundary links carry sum theta^2 of order f^2 S^5 for every choice of potential (row 1011 4.2, reading), against the
  curl energy f^2 S^4. ARGUED: with a pinned cell and a pin-measurable frame, route (ii) cannot return the
  scale-invariant blind bound that U(1) has, unless D n is small on the boundary, which is statement (N1) of row 1011 7.4
  again (typical smooth pins), not a symmetry.
- So the next obligation of route (ii) is not (SYM) with (REG). It is a boundary statement. In exact form, (O2) below.

**7.4 The two open statements, and the attacks that failed.**

**Lemma O1 (OPEN; the bulk residue of (SYM) with (REG)).** There are a finite set D of links and a map nu from an open
gauge-invariant set of full measure of configurations of D to S^2, covariant at the origin, such that n_x = nu o tau_x
satisfies, at every site z, sum over l in in(z) of sum_a R_(l,a)(e^A (D_l n)^a) = 0, with c_l in L^2 and integration by parts.
By 6.5 such a D meets F_(mu nu) for three directions mu and every nu (at least six forward links). By 6.3 the frame has j not 0.
Three attacks, each failed for a stated reason.
- (A1) Solve link by link, c_l = 0. One link is solved exactly (6.1), and the general solution on one link is large
  (any field on S^3 of unit speed that preserves e^(kappa t) times Haar measure). A site has four outgoing links and one
  vector: four equations for two unknown functions. The class of 6.1 is excluded at a site by Lemma SPAN. I found no
  common solution and no proof that none exists. A count proves neither.
- (A2) Eliminate through an extreme link variable. This is the proof of Lemma PRIV, and it works when no frame in the
  equation reads the variable, because then the equation is affine in it. When a frame reads the variable, (J) is a
  first-order differential equation in it, and far variables enter as free parameters: the axis a of 6.1 is an arbitrary
  function of the other links and does not change c. So locality gives no bound on the range, and no contradiction.
- (A3) Ward identities that remove the unknown frame. Integrating (J) over the star of a site, or conditioning on one
  link, gives identities that hold for every covariant frame (the proof of STAR; the one-link marginal is Haar measure
  and E[n_x | U_l] = 0 by covariance at both ends). They carry no information. Gauge-invariant test functions give (J) back.
Count, for the record: (J) is one equation per site for two unknown functions (row 1026 7.3); on the cube, six equations
for eight functions (4.3). What a decision would change: by 6.2 and 6.6, a positive answer to O1 does not give the
consumer. A negative answer would close the bulk half of route (ii) for site frames.

**Statement O2 (OPEN; what route (ii) needs at the boundary).** For a cell c, a pin-measurable boundary frame and
boundary lambda: H_c(omega; (d lambda) n(omega)) + Var_omega(Psi_(d lambda)) <= 0 on a set of pins of positive measure (this is the
curl inequality on closed boundary fields). By 6.6 the variance is positive off reducible pins, so O2 asks the pinned
free energy to be strictly concave along every such direction. Not attacked beyond the exact formula in 6.6. For the
strength field of row 1011 4.2 (b on boundary plaquettes, 0 inside) one corner term is
b w_p [t_p |D_l n|^2 - 2 (n_x x Ad(U_l) n_z) . s_p], which has either sign.
- Mon Nov 16 04:13:32 UTC 2026 (`date -u`). Step 7 written.

### Step 8 (done): verdicts, repairs, what was not done

Provenance: Claude Fable 5.2, medium effort, background agent on the lead's MacBook, commit 49af837cc, one session, no
subagents. No numeric run; the numeric lock was not taken. Checked by: nobody. Same-provider and cross-provider checks
are both open.

| Item | Statement | Mark |
|---|---|---|
| LINK (4.0) | c_l = - e^(-A) div_l(e^A n_tail); (J) is linear in e^A n | PROVED |
| STAR (4.0) | outflow at z = minus the divergence of the incoming field (Ad(U_l) n_z); (J) at z is "Y_z preserves e^A dU"; automatic at a site with no incoming link | PROVED |
| U(1) control (4.1) | passes every statement; classical bound; zero gain | PROVED |
| Cube (4.3) | conservation holds at 000 (automatic) and at 111 (STAPLE vectors at 110, 101, 011); the six other site equations are open | PROVED / OPEN as stated |
| SING (4.4) | the odd-torus example is in the singular set of every local covariant frame | PROVED |
| Winding-loop frame on Z_3^4 (4.4) | (REG) holds, j - d = 0 at the example, (J) fails on every set of positive measure near it | PROVED |
| STAPLE (6.1) | b_l = a - Ad(Mh_l) a and b_l/|b_l| have j_l = d_l = 0 | PROVED |
| LF (6.2) | (SYM) with (REG) for link frames: true, current identically zero | PROVED |
| LF, consumer (6.2) | a measure-preserving interior flow changes no bound; zero gain | PROVED |
| SPAN (6.3) | three outgoing forces are independent almost surely; no site frame with j = 0 | PROVED |
| PRIV (6.4) | a frame that does not read the link (z - e_mu + e_nu, mu) has D n = 0 on (z - e_mu, mu) wherever (J) holds at z | PROVED |
| Corollary P (6.5) | no conserved current for past frames, two-direction frames, the winding frame, N_1 x N_2 | PROVED |
| Necessary range condition (6.5) | a site frame with (J) reads a link of F_(mu nu) for three directions mu and all nu | PROVED |
| BD (6.6) | at a pinned lower face, conservation at z forces D n = 0 on the face links into z | PROVED |
| BD, consequence | the cost of a boundary rotation is a function of d theta AND of theta on the boundary links | PROVED (exact invariance); the inequality Q(d lambda) <= 0 is not refuted |
| CURL (7.1) | Q(theta) <= 4 m^4 k_1 sum (d theta)^2 for interior theta, given a local potential phi and (REG) | PROVED given its hypotheses |
| FLUX (7.2) | a conserved finite-range current with (REG) has zero flux through every slab | PROVED |
| POT (7.2) | conserved, finite range, zero flux gives a local potential | ARGUED (recalled, not rebuilt) |
| (SYM) with (REG), link frames | | PROVED true; consumer empty |
| (SYM) with (REG), site frames, bulk (Lemma O1) | | OPEN (three attacks failed, 7.4) |
| Curl form of the consumer of row 1026 7.1 on a pinned cell (site frame, pin-measurable on the boundary) | exact curl form | FAILS (BD) |
| Curl inequality on a pinned cell (O2) | | OPEN |
| Route (ii) as a mechanism | interior symmetry is not what it needs; the boundary term is | ARGUED (7.3) |

**Answer to the row.** Neither alternative holds as written. I did not build a site frame with a conserved, square
integrable current, and I did not build a set of positive measure on which every local site frame fails. What is proved:
(1) the statement is true and empty if the frame may sit on links; (2) for site frames, conservation fails for every
frame that misses one forward parallel link in two directions, which removes every frame where (REG) is free; (3) at a
pinned lower face conservation fails for every pin-measurable site frame off reducible pins, so the consumer's cost is
not a curl form in theta even if Lemma O1 is true. So (SYM) with (REG) is not the obligation that decides route (ii).

**Text repairs this implies (for the lead; no other file was edited).**
- `parts/gap.md` L141: replace "its next obligation is (SYM) with (REG)" by "(SYM) with (REG) holds for link frames with
  zero gain (row 1034 6.2); for site frames it is open in the bulk under a necessary range condition (6.5) and its
  consumer loses the curl form at pinned lower faces (6.6); the obligations are Lemma O1 and statement O2 of row 1034".
- `library/gap-aligned-frame.md` 7.3 and Remark JAC: "Q is a quadratic form in d theta" holds for theta zero on the pinned
  links only; with a boundary rotation Q depends on theta on the boundary links (row 1034 6.6).
- `library/gap-short-step-check-astra.md` item 10: the odd-torus example stands as a counterexample to the word
  "exactly"; it is not a model for a local frame (row 1034 4.4).

**Credits.** Lemmas FLOW, PROJ, FR+, SPLIT: row 1018 (Claude Fable 5.2). Lemma FR, Lemma CEN, Propositions A, B, B': row
1011. Remark JAC, Theorem E, the cube frames: row 1026 (Claude Fable 5.2). (REG), the corner frame's Jacobian: check 1027
(Claude Opus 5.5). The odd-torus example and the reopening of route (ii): gpt-6-astra check of row 1018. The underlying
construction: Sussman and Alpoge, on Balaban's renormalisation group; their account has no statement used here. The
staple (heat-bath) form of the one-link law is standard lattice practice (Creutz); the conjugation symmetry of 6.1 is
derived here and I do not know a source for it. Hydon and Mansfield are RECALLED for POT only.

**Not done.**
- No check by any other model. Every PROVED above is "written here, unchecked".
- Lemma O1 and statement O2. Lemma POT is not rebuilt.
- origin/main and the open PR branches were not searched (Step 3).
- The upper faces {x_mu = S_mu} in Theorem BD; boundary rotations with a different vector on each boundary link.
- No numeric guide run. A run could test O2's sign on a small cell for one explicit frame; it could not decide O1.
- Mon Nov 16 04:14:59 UTC 2026 (`date -u`). All steps written.

RESULT: Row 1034 (Claude Fable 5.2 medium, checked by nobody, no numeric run): (SYM) with (REG) is NOT DECIDED for site frames, and it is shown not to be the obligation that decides route (ii). PROVED by hand, unchecked: (1) Lemma STAPLE and Proposition LF: with one covariant unit vector per LINK (rotation of the loop U_l S_l about a plaquette axis, at unit speed) the current j - d is identically zero, of finite range and with (REG), on almost every configuration; so the statement is true for link frames, and its consumer is empty, because a measure-preserving interior flow changes no bound (zero gain, as for U(1)). (2) Lemma PRIV and Corollary P: a SITE frame that does not read the link parallel to an incoming link across a forward plaquette has D n = 0 on that incoming link wherever its current is conserved; so no conserved current on any set of positive measure for past-built frames (the ones with d = 0, where (REG) is free), two-direction frames, the winding-loop frame and N_1 x N_2; a site frame with (J) must read at least six forward links, and by Lemma SPAN it cannot have j = 0. (3) Theorem BD: at a pinned lower face of a cell, conservation at a boundary site forces D n = 0 on the face links for every pin-measurable site frame, so off reducible pins the cost of a boundary rotation theta n is invariant under interior gradients only; it depends on theta on the boundary links and is not a curl form in d theta. (4) Proposition CURL: given a local potential (j - d = d* phi) and (REG), Q(theta) <= 4 m^4 k_1 sum_p (d theta)_p^2 for interior theta, with m = 2R + 3 and k_1 = sup_p sum_l |E[n_l . R_l phi_p]|; Lemma FLUX; U(1) passes every statement with the classical constant and zero gain. Tests: the odd-torus example (i, j, k, 1) lies in the singular set of every local covariant frame (Lemma SING) and gives no frame; on one cube conservation holds at 000 and 111 and six site equations stay open. OPEN: Lemma O1 (a site frame of finite range that reads the forward links, with j - d conserved and in L^2; three attacks failed: link-by-link solution, extreme-variable elimination, Ward identities); statement O2 (the curl inequality for boundary gradients on a pinned cell); Lemma POT (local potential from conservation, ARGUED only); any check by another model.
