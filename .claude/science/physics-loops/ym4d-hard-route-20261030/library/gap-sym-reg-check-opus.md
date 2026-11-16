lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T16:15Z

# Check of row 1034 (`library/gap-sym-reg.md`): queue row 1035, `gap-sym-reg-check-opus`

Started 2026-11-16T04:15Z on Mac mini worker 3, Claude Opus 5.5 max, at commit 9b65b9d6c of
`claude/ym4d-hard-route`. Checks a text written by Claude Fable 5.2 medium (same provider,
so this is not an independent check in the sense of the working rules: a different model
of the same provider, reading by hand). No new attack (row 1035). Verdicts per statement:
HOLDS, HOLDS AFTER CORRECTION, FAILS (with the first failing line).

## Plan (at most eight steps; each step is written here before the next)

1. Read `library/gap-sym-reg.md` in full and the definitions it consumes (`library/gap-aligned-frame.md`
   Theorem E and the cost identity; `library/gap-aligned-frame-check-opus.md` (REG);
   `library/gap-short-step-max.md` 4.1-4.5; `library/gap-short-step-check-astra.md` items 9-10).
   Fix the notation (n, D n, j, d, theta, Psi, Q) used in the check.
2. Lemma STAPLE and Proposition LF (link frames have j - d = 0; consumer empty).
3. Lemma PRIV and Corollary P, with the one-cube test by hand.
4. Lemma SPAN.
5. Theorem BD, and whether "pin-measurable site frame" is the class route (ii) needs.
6. Proposition CURL (sign, count, the constant 4 m^4 k_1) and Lemma FLUX.
7. Lemma SING with the odd-torus test (links i, j, k, 1), and the U(1) control.
8. Verdict table and the RESULT line.

## Step log

(Each step appends below.)

### Step 1 (done 2026-11-16T04:25Z): sources read, notation fixed, overlap

Read in full: `library/gap-sym-reg.md` (440 lines, the text under check). Read the parts it consumes:
`library/gap-aligned-frame.md` Step 2 (Remarks LIN, JAC, BACK) and Step 7 (7.1-7.4);
`library/gap-aligned-frame-check-opus.md` L224-252 and the RESULT ((REG)); `library/gap-short-step-max.md` 4.1-4.5
(FLOW, PROJ, FR+, SPLIT, sizes); `library/gap-short-step-check-astra.md` items 9-10 and L374;
`library/gap-pinned-cell-gauge-max.md` 3.1-3.2 (conventions, Proposition A) and 7.3-7.4 (Lemma FR, (N1)-(N3)).
FINISH.md "How we work", "Working efficiently", "Rules"; GOAL.md.

Overlap (rule 0a): this row checks; it attacks no open lemma, so no open-core grep is owed. Prior work on the
objects: the Sussman-Alpoge index (`library/sa-index/`) and `~/ym4d-papers` (Balaban CMP 89-122 text dumps) have no
hit for "staple", "colour frame" or "color frame" (grep, this step). This agrees with row 1034 L16 and check 1027 Step 1:
their account has no colour-frame statement, so nothing is ported and nothing of theirs is checked here.

Notation used in this check (that of row 1011 3.1 and row 1034 Step 2; restated so each verdict can be re-read).
- SU(2) = unit quaternions; su(2) = Im H = R^3; for imaginary u, v: uv = - u.v + u x v, [u, v] = 2 u x v.
  Ad(g) v = g v g^(-1); Ad(e^(s a)) is the rotation about the unit vector a by the angle 2s.
- R_(l,a) f = (d/d eps) f(U_l -> e^(eps e_a) U_l). These fields are Killing fields of the bi-invariant metric, so they are
  divergence free for Haar measure. A = sum_p beta_p w_p t_p with t_p = Re U_p; R_(l,a) A = - N_l^a.
- For a field V = sum_l b_l . R_l (b_l in R^3, functions of U): div V = sum_l sum_a R_(l,a) b_l^a (Haar divergence), and
  Psi_V = V A + div V is the divergence of V for mu = e^A dU (up to sign: E[V f] = - E[f Psi_V] when V is regular).
- Site frame: n_x(U) unit, n_x(U^g) = Ad(g_x) n_x(U). j_l = n_tail(l) . N_l; d_l = sum_a R_(l,a) n^a_tail(l); c_l = j_l - d_l;
  D_l n = n_tail - Ad(U_l) n_head. Move V_theta = sum_l theta_l n_tail(l) . R_l: then Psi_theta = - sum_l theta_l c_l.
  Check of the sign: V_theta A = - sum theta_l n_tail . N_l = - sum theta_l j_l, div V_theta = sum theta_l d_l. Holds.
- (J): sum_l (d lambda)_l c_l = 0 for every lambda zero at pinned sites, with (d lambda)_l = lambda_tail - lambda_head;
  equivalently rho_z := sum over l with tail z of c_l - sum over l with head z of c_l = 0 at every free site z.
  Row 1034 L74-75 writes the same condition as an identity in rho_z of row 1026 7.1; Step 2 of this check re-derives it.
- (REG) (check 1027 L239): n smooth off a closed null set; c_l in L^2; E[V f] = - E[f Psi_V] for smooth f.
- Lemma FR (row 1011 7.3), the identity used in Corollary P: n_x - Ad(U_p) n_x = D_(l_1) n + Ad(U_1) D_(l_2) n
  - Ad(U_1 U_2 U_3^(-1)) D_(l_3) n - Ad(U_p) D_(l_4) n for p = (x; mu, nu), U_p = U_1 U_2 U_3^(-1) U_4^(-1).
  Re-derived here by telescoping along x -> x + mu -> x + mu + nu -> x + nu -> x. Holds.

What the check has to decide, per row 1035: line-by-line verdicts on STAPLE, LF, PRIV, Corollary P, SPAN, BD, CURL
(sign, count, constant), FLUX, SING with the odd-torus test, and the U(1) control; and whether BD's class
"pin-measurable site frame" is the class route (ii) needs.

### Step 2 (done 2026-11-16T04:40Z): identities LINK and STAR; Lemma STAPLE; Proposition LF and "the consumer is empty"

**LINK (L65-68). HOLDS.** sum_a R_(l,a)(e^A n_x^a) = e^A (sum_a (R_(l,a) A) n_x^a + d_l) = e^A (- j_l + d_l) = - e^A c_l.

**STAR (L70-81). HOLDS** (re-derived). At a free site z, G_a = sum_out e_a . R_l - sum_in (Ad(U_l) e_a) . R_l generates
g_z = e^(eps e_a): an out link moves by U_l -> e^(eps e_a) U_l, an in link by U_l -> U_l e^(- eps e_a) = e^(- eps Ad(U_l) e_a) U_l.
G_a is Haar divergence free and G_a A = 0. Covariance gives G_a n_z = 2 e_a x n_z and G_a n_x = 0 for x != z. So
W := sum_a n_z^a G_a = sum_out n_z . R_l - sum_in (Ad(U_l) n_z) . R_l has mu-divergence sum_a (2 e_a x n_z) . e_a = 0. With LINK,
sum_out c_l = - e^(-A) sum_in sum_a R_(l,a)(e^A (Ad(U_l) n_z)^a). Subtracting sum_in c_l (LINK at the tails of in links):
  sum_out c_l - sum_in c_l = e^(-A) sum_in sum_a R_(l,a)(e^A (D_l n)^a).
So (J) at z is "Y_z = sum_in (D_l n) . R_l has zero mu-divergence", as L74 says. The same computation for Haar measure gives
sum_out d_l = sum_in sum_a R_(l,a)(Ad(U_l) n_z)^a, hence the sum above equals - e^A rho_z with rho_z of row 1026 7.1
(rho_z = sum_in (D_l n) . N_l + (div d)(z)). L75 holds. The sign of rho_z is opposite to the outflow; only "= 0" is used.
Consequence at a site with no incoming link (L80-81): holds, provided the gauge transformation at z is a symmetry of
the action there (true at the corner 000 of a free cube: every link at 000 is an integration variable).

**Lemma STAPLE (6.1, L163-180). HOLDS.**
- The split A = Re(U_l S_l) + A' holds: for a plaquette that uses l as l_3 or l_4, use Re g = Re g^(-1) and the cyclic
  invariance of Re to bring U_l to the front, uninverted. Then R_(l,a) A = Re(e_a U_l S_l) = - e_a . Im(U_l S_l), so
  N_l = Im(U_l S_l) (L166). Under a gauge transformation U_l S_l -> g_x U_l S_l g_x^(-1): a loop at x, as stated.
- (i): N_l = kappa Im Mh and Ad(Mh) fixes Im Mh and is orthogonal, so (Ad(Mh) a) . Im Mh = a . Im Mh. Holds.
- (ii): U_l -> e^(eps e_c) U_l sends Mh -> e^(eps e_c) Mh and leaves kappa fixed; a does not move. So
  R_(l,c) b = - 2 e_c x Ad(Mh) a and sum_c (e_c x w) . e_c = 0. Holds.
- (iii): |b|^2 = 2 |a|^2 - 2 a . w with w = Ad(Mh) a; R_(l,c) |b|^2 = - 4 a . (e_c x w) = - 4 e_c . (w x a); and
  b . (w x a) = (a - w) . (w x a) = 0. Holds. The unit field: sum_c R_c(b^c/|b|) = 0 - (1/(2 |b|^3)) b . R |b|^2 = 0. Holds.
- Covariance of b_l and n_l when a is covariant at x: b -> Ad(g_x) a - Ad(g_x) Ad(Mh) Ad(g_x)^(-1) Ad(g_x) a = Ad(g_x) b. Holds.
- The flow (L179-180): with a fixed, the curve Mh(s) = e^(s a) Mh e^(- s a) has derivative (a - Ad(Mh(s)) a) Mh(s) = b(s) Mh(s),
  which is the left-multiplication field b . R_l. So the flow of b . R_l is conjugation of the loop by e^(s a). Holds.
  In the variable U_l it is U_l -> e^(s a) U_l (S_l e^(- s a) S_l^(-1)): a left and a right translation at fixed s.

**Proposition LF (6.2, L182-201). HOLDS.**
- q_mu does not contain (0, mu), so a_l does not depend on U_l, as 6.1 needs. Covariance at the tail: holds (above).
- Singular set: given kappa_l > 0, b_l = 0 exactly when a commutes with Mh, that is a x Im Mh = 0, that is s_q x N_l = 0.
  So Z_l = {kappa_l = 0} union {s_q x N_l = 0}, a real-analytic subset of the connected analytic manifold SU(2)^links;
  it is proper (witness below), hence closed and null. Holds.
- Witness (L186-188), re-derived: l = (x, 1), q = (x; 2, 3). U_q = U_(x,2) U_(x+e_2,3) U_(x+e_3,2)^(-1) U_(x,3)^(-1) = e^(phi j),
  so s_q = sin(phi) j. Of the six plaquettes through l, only (x; 1, 2) contains U_(x+e_1,2); it uses l as l_1 and has
  U_p = e^(phi i). No plaquette through l contains U_(x+e_2,3). So N_l = beta sin(phi) i, S_l = beta (5 + e^(phi i))
  (U_l = 1), kappa_l > 0, and s_q x N_l = - beta sin^2(phi) k != 0 for 0 < phi < pi. Holds.
- Integration by parts (L191-195): |b_l| is constant on the orbits of the circle s -> conjugation by e^(s a) (it is the
  fixed-point-free part of the orbit structure; the set b = 0 is the fixed-point set and is invariant). The n-flow is the
  b-flow at the orbit-constant speed 1/|b_l|. The map U_l -> Mh is a right translation, so it suffices that the n-flow
  preserves Haar measure in Mh. The circle acts on S^3 by isometries that preserve Haar measure, so the conditional
  measures on orbits are rotation invariant, and an orbit-dependent rotation preserves each of them. Re(U_l S_l) is
  kept, other links do not move, so e^A dU is preserved. The difference quotients of f o Phi_s are bounded by
  sup |grad f| because the flow has unit speed; dominated convergence gives E[n_l . R_l f] = 0. Holds.
  A shorter route to the same identity, for the record: off Z_l the mu-divergence of n_l . R_l is d - j = 0 (6.1),
  and Z_l is null, closed and invariant; the flow argument is what handles Z_l, so the text's route is the right one.
- Psi_theta = 0 for every constant theta on free links: V_theta A = - sum theta_l n_l . N_l = 0 and div V_theta =
  sum theta_l sum_c R_(l,c) n_l^c = 0 (each n_l is differentiated only in its own link). Holds. e^(pi n) = -1: holds.
- **"The consumer is empty" (L196-200). HOLDS, and it holds in a stronger form.** Psi is linear in the field. If W is
  any interior field with E[W f] = 0 for smooth f (a mu-preserving field, such as the link-frame field), then
  Psi_(V_0 + W) = Psi_(V_0) and E[(V_0 + W) Psi] = E[V_0 Psi]. So - E[V Psi_V] = H_c + Var(Psi_V) is the same number
  for the zero extension V_0 and for V_0 + W. This uses only LF's integration by parts, not the flow of V_0 + W, which
  the text does not construct (the link fields depend on each other's links, so the joint flow is not a product of
  the single-link flows; the text's conclusion does not need it). For pinned cells: n_l may read pinned links through
  S_l and a; STAPLE needs only that a and S_l do not contain U_l, so the same holds with the cell action.
- Scope note (no defect): the row's object is a SITE frame (row 1018 4.2, "unit vectors n_x at the sites"). LF is
  outside it, as row 1034 L140-143 says. LF answers the literal statement only if the frame may sit on links.
- U(1) (L201): Ad = 1, so b = 0 and the field is zero. Passes, zero gain. Holds.

Verdicts of Step 2: LINK HOLDS; STAR HOLDS; STAPLE HOLDS; LF HOLDS; LF consumer (zero gain) HOLDS.

### Step 3 (done 2026-11-16T04:55Z): Lemma PRIV (with the one-cube test), Corollary P, the classes, the range condition

**Test first: PRIV on the free cube {0,1}^3, by hand. HOLDS.** z = 110, mu = 2, nu = 3. Then l = (100 -> 110),
P = (101 -> 111), p = (100; 2, 3) with links (100 -> 110), (110 -> 111), (101 -> 111) as l_3, (100 -> 101).
The cube has two plaquettes through P: p, and (001; 1, 2) (links 001 -> 101, 101 -> 111, 011 -> 111, 001 -> 011),
whose vertices 001, 101, 111, 011 do not include 110. in(110) = {(010 -> 110), (100 -> 110)}. N_(010 -> 110) reads the
plaquettes (000; 1, 2) and (010; 1, 3): no P. N_(100 -> 110) reads (000; 1, 2) and p, and p uses (100 -> 110) as l_1, so
N_(100 -> 110) = N0 + beta Im(g U_P^(-1) h) with g = U_(100->110) U_(110->111), h = U_(100->101)^(-1). If n_110, n_100, n_010 do
not read U_P, every other term of rho_110 = sum_in (D n) . N + (div d)(110) is free of U_P (the d terms differentiate
n_110 in (110 -> 111), n_010 in (010 -> 110), n_100 in (100 -> 110)). So rho_110 is affine in U_P, and conservation on
a set of positive measure forces D_(100->110) n = 0 there. This is L104-105 of row 1034. Holds.
Remark (no defect): the cube frame of row 1034 4.3 does not meet PRIV's hypothesis, since its STAPLE vector at 110
reads the staple of (110 -> 111), which contains U_P through p. Row 1034 states the cube use of PRIV conditionally,
so nothing is claimed for that frame.

**Lemma PRIV (6.4, L214-229). HOLDS.**
- Incidence (L221-223), re-derived on Z^4: the plaquettes through P are (y; mu, lambda) and (y - e_lambda; mu, lambda),
  y = z - e_mu + e_nu, lambda != mu. The vertices of the first are z + {- e_mu + e_nu, e_nu, - e_mu + e_nu + e_lambda,
  e_nu + e_lambda}; none is z. The vertices of the second are z + {- e_mu + e_nu - e_lambda, e_nu - e_lambda, - e_mu + e_nu,
  e_nu}; only e_nu - e_lambda can vanish, at lambda = nu, which is p. p meets z in l (incoming) and (z, nu) (outgoing).
  So among the forces on in(z) only N_l reads U_P. Holds.
- Torus (L215): every offset above has entries in {-1, 0, 1, 2} with at most one entry 2 (at lambda = nu); it is 0 mod L
  only if it is 0, for L >= 3. Holds.
- N_l = N0 + beta_p w_p Im(U_l U_(z,nu) U_P^(-1) U_(z-e_mu,nu)^(-1)) (p uses l as l_1): g, h as stated. Holds.
- Independence of the rest: D_l' n reads n_(z - e_kappa), n_z, U_l' with l' != P; (div d)(z) differentiates n_z in the out
  links of z and n_(z - e_kappa) in the in links; a derivative in a link other than P of a function that does not read U_P
  does not read U_P. Holds (it needs independence on the open set Omega, which the statement assumes).
- Fubini and the affine step: the Wilson measure has a positive density against product Haar measure; Im(g U_P^(-1) h) is
  real-linear in U_P in R^4; a non-zero affine function on R^4 vanishes on S^3 only on a sphere of dimension at most 2
  or a point, a null set; so the coefficients vanish, alpha = 0, and choosing g U_P^(-1) h = v (U_P = h v^(-1) g) gives
  (D_l n) . v = 0 for every unit imaginary v. Needs beta_p w_p != 0, which is assumed. Holds.
- The variant "rho_z almost surely constant on Omega_0" (L228): the constant joins alpha. Holds.
- U(1) (L229): the conclusion D n = 0 is true for the constant frame. Holds.

**Corollary P (6.5, L231-241). HOLDS.**
- F_(mu nu) is exactly the set of offsets of P from z and from z - e_kappa (P - z = (- e_mu + e_nu, mu);
  P - (z - e_kappa) = (e_kappa - e_mu + e_nu, mu)). So "D disjoint from F_(mu nu)" is PRIV's hypothesis at every site. Holds.
- PRIV at every head z gives D n = 0 a.e. on all links of direction mu, and likewise mu' (countably many null sets). Holds.
- p = (x; mu, mu') and p' = (x + e_mu; mu, mu') have all links in directions mu, mu'. Lemma FR's identity (Step 1) gives
  (1 - Ad(U_p)) n_x = 0, so s_p x n_x = 0; likewise s_p' x n_(x + e_mu) = 0; and n_x = Ad(U_(x,mu)) n_(x + e_mu). So s_p and
  Ad(U_(x,mu)) s_p' are both parallel to the unit vector n_x (or zero), and s_p x Ad(U_(x,mu)) s_p' = 0. Holds.
- Witness (L240-241), re-derived: U_p = U_(x,mu) U_(x+e_mu,mu') U_(x+e_mu',mu)^(-1) U_(x,mu')^(-1) = e^(phi i);
  U_p' = U_(x+e_mu,mu) U_(x+2e_mu,mu') U_(x+e_mu+e_mu',mu)^(-1) U_(x+e_mu,mu')^(-1) = e^(phi j); U_(x,mu) = 1; so the product is
  sin^2(phi) (i x j) = sin^2(phi) k != 0. A real-analytic function that is not identically zero has a null zero set. Holds.
- Scope: the corollary uses (J) only at the heads of the links of p and p'; it is stated for all sites, which is weaker
  as a hypothesis set and fine.

**Classes (L242-251). All HOLD.**
- (a) Past frames: the links of F_(mu nu) have tails with coordinate sum 0 or 1 and heads with sum 1 or 2, so they are not
  in D for any mu, nu. The out links of x have heads with sum 1, so d = 0. (REG) is free for them in the strong sense:
  if n_tail(l) does not read U_l, E[n_tail(l) . R_l f] is computed by Haar integration by parts in U_l alone, for any
  bounded measurable frame, so E[V f] = - E[f Psi_V] with Psi_V = - sum theta_l j_l and c = j bounded. The plaquette-behind
  frame (x; - mu, - nu) has vertices of sum 0, -1, -2, -1: a past frame. Holds.
- (b) A frame reading two directions misses F_(mu nu) for the other two mu (F_(mu nu) has only direction-mu links). Holds.
- (c) The winding-loop frame reads direction 1 only. Holds (it is C^1 where Im P != 0).
- (d) N_(x,1) x N_(x,2): its direction-3 links have tails at x + {0, e_1, e_2, - e_3, e_1 - e_3, e_2 - e_3}, its
  direction-4 links at x + {0, e_1, e_2, - e_4, e_1 - e_4, e_2 - e_4}. Every direction-3 offset of F_(3 4) has e_4-component
  +1 or +2 and every direction-4 offset of F_(4 3) has e_3-component +1 or +2. Disjoint. Holds.

**Necessary range condition (L252-255). HOLDS.** It is the contrapositive of Corollary P. The two-set membership of
(e_nu + e_nu' - e_mu, mu) holds (kappa = nu' in F_(mu nu), kappa = nu in F_(mu nu')). No triple membership: an element of
F_(mu nu) is - e_mu + e_nu + w with w in {0, e_1, ..., e_4}; e_nu + w = e_nu' + w' forces w = e_nu', w' = e_nu, so two sets
meet only in e_nu + e_nu' - e_mu, which is not in a third F_(mu nu''). Entries of e_nu + w lie in {0, 1, 2}, so on a torus with
L >= 3 there are no extra coincidences. Three sets per direction, at most two per link: at least two links per direction,
six over three directions. Holds.

Verdicts of Step 3: PRIV HOLDS (cube test passed); Corollary P HOLDS; classes (a)-(d) HOLD; range condition HOLDS.

### Step 4 (done 2026-11-16T05:05Z): Lemma SPAN (6.3, L203-212)

**Lemma SPAN. HOLDS, with one scope precision.**
- The plaquette (x - e_nu; mu, nu) has l_1 = (x - e_nu, mu) = Q_mu and l_3 = (x, mu). Holds.
- Uniqueness of Q_mu among the plaquettes through the out links of x, re-derived. A plaquette through (x, kappa) that
  contains a direction-mu link lies in a plane containing mu. If kappa = mu: the direction-mu links are (x, mu),
  (x + e_lambda, mu) (plaquette (x; mu, lambda)) and (x - e_lambda, mu), (x, mu) (plaquette (x - e_lambda; mu, lambda)); only
  lambda = nu gives Q_mu. If kappa != mu: the plaquettes (x; kappa, mu) and (x - e_mu; kappa, mu) have direction-mu links at
  x, x + e_kappa, x - e_mu, x - e_mu + e_kappa, none equal to x - e_nu. On a torus with L >= 3 the offsets differ mod L too.
  So Q_mu enters only N_(x,mu), only through that plaquette, and not the two other forces. Holds.
- The form of the term: with U_3 = U_(x,mu), Re U_p = Re(U_3 sigma), sigma = U_2^(-1) Q_mu^(-1) U_4 (a path from x + e_mu to x).
  So N_(x,mu) = N0_mu + beta w Im(U_(x,mu) U_2^(-1) Q_mu^(-1) U_(x-e_nu,nu)): g_mu = U_(x,mu) U_(x-e_nu+e_mu,nu)^(-1),
  h_mu = U_(x-e_nu,nu). The text writes the same with g, h unnamed. Holds.
- Non-vanishing of the determinant: as (Q_1, Q_2, Q_3) vary with all else fixed, (N_1, N_2, N_3) ranges over a product of
  three closed balls of radius beta w > 0 (centres N0_mu), each N_mu moving with its own Q_mu. det is a non-zero polynomial
  on R^9, so it does not vanish on that product of balls (a product of open balls is open). Hence det(N_1, N_2, N_3), a
  real-analytic function of the configuration, is not identically zero, and its zero set is null. Holds.
- The conclusion: a unit n with n . N_mu = 0 for mu = 1, 2, 3 is a non-zero kernel vector, so det = 0. Holds.
- Scope precision (not a defect for the row's use, which is in the bulk): in a pinned box, Q_1, Q_2, Q_3 must be
  integration variables; "all plaquettes present" does not ensure that near the boundary.
- What SPAN excludes, read exactly: j = 0 on three out links of a site. It does not exclude a site frame with c_l = 0 on
  each out link through j_l = d_l != 0. The text claims only the first (L203, L206, L356). Holds as stated.

Verdict of Step 4: SPAN HOLDS (scope: the three links Q_mu free).

### Step 5 (done 2026-11-16T05:25Z): Theorem BD (6.6, L257-285) and its frame class

**Theorem BD, the statement (L257-269). HOLDS.**
- Geometry: z on {x_4 = 0} with 0 < z_i < S_i (i = 1, 2, 3). Links at z: out (z, i) and in (z - e_i, i), i = 1, 2, 3, all in
  the face, so pinned; out (z, 4), interior (it leaves the face and x_4 = 1 < S_4); no (z - e_4, 4). Holds.
- V = (d lambda) n with lambda = 1_z: n_z(omega) on (z, i) and (z, 4), - n_(z-e_i)(omega) on (z - e_i, i). div V = 0, since the only
  interior link carries the fixed vector n_z(omega). Holds.
- Gauss law at z with pinned links included: the gauge generator at z annihilates A_c (each t_p is invariant), so
  sum_out N_l = sum_in Ad(U_l)^(-1) N_l. Then V A = - n_z . sum_out N_l + sum_in n_tail . N_l = sum_in (D_l n) . N_l. Holds.
- Private links: p_i = (z - e_i; i, 4) has links (z - e_i, i), (z, 4), P_i = (z - e_i + e_4, i), (z - e_i, 4). P_i is interior:
  it sits at x_4 = 1 < S_4, and its head z + e_4 has 0 < z_j < S_j, so it lies in no face {x_j = 0} or {x_j = S_j}
  (if z_i = 1 its tail has x_i = 0, but its head does not). By the incidence of Step 3, p_i is the only plaquette through
  P_i with z as a vertex, and its only in-link of z is (z - e_i, i). So Psi_V is affine in each P_i, with linear part
  beta w (D_i n)(omega) . Im(g_i P_i^(-1) h_i). Fubini (the cell law has a positive density against Haar measure) and the
  affine step of PRIV give D_i n(omega) = 0 if Psi_V is almost surely constant. Holds.
  (Remark: l_4 = (z - e_i, 4) is pinned when z_i = 1. It enters only g_i, h_i. No effect.)

**Consequence 1 (L271-272): a null set of pins. HOLDS** (with S_1, S_2, S_3 >= 3). Lemma FR needs D n = 0 on the four links
of a face plaquette. For y = (1, 1, 1, 0) (corner offset) and i, j in {1, 2, 3}, the links of (y; i, j) have heads y + e_i,
y + e_j, y + e_i + e_j, which are relative-interior face sites when S >= 3. So s_p x n_y = 0 for the three face plaquettes
at y; their axes are parallel; that is a non-trivial polynomial condition on the pin (witness as in Corollary P). Holds.

**Consequence 2 (L273-274): Q(d lambda) = H_c(omega; (d lambda) n) + Var(Psi_(d lambda)) with Var > 0. HOLDS** (FLOW's
identity with Q := - E[V Psi_V]; Var > 0 is BD off the null set of Consequence 1).

**Consequence 3 (L275-277; table L399; RESULT clause (3)): "the cost is invariant under theta -> theta + d lambda only for
lambda zero at the pinned sites ... PROVED (exact invariance)". FAILS as written; HOLDS AFTER CORRECTION.**
First failing line: L399, "PROVED (exact invariance)". What BD gives is a statement about Psi, not about Q.
- Q is quadratic, so Q(theta + d lambda) = Q(theta) for all theta iff Q(d lambda) = 0 and Q(theta, d lambda) = 0 for all theta.
- Q(d lambda) = H_c(omega; (d lambda) n) + Var(Psi_(d lambda)). H_c, the Hessian of the pinned free energy, has no sign. So
  Var > 0 does not give Q(d lambda) != 0: Q(d lambda) = 0 exactly when H_c(omega; (d lambda) n) = - Var(Psi_(d lambda)).
- The text's own table (same line L399) says "the inequality Q(d lambda) <= 0 is not refuted", and its O2 asks for
  Q(d lambda) <= 0. Q(d lambda) = 0 lies inside that unrefuted case. So invariance along the ray of d lambda is not excluded.
- For interior theta (theta zero on boundary links), polarizing FLOW gives Q(theta, d lambda) = Cov(Psi_theta, Psi_(d lambda));
  BD does not show that this is non-zero for some theta.
Correction: "At a pinned lower face, Psi_(d lambda) is not almost surely constant (BD), so the boundary gradient move is not
a symmetry of the pinned law, the JAC route to invariance (Psi_(d lambda) = 0 implies Q(theta + d lambda) = Q(theta)) fails
there, and FLOW's bound along d lambda is strict: Q(d lambda) > H_c(omega; (d lambda) n). Whether Q itself is invariant under
boundary gradients, that is whether Q(d lambda) = 0 and Cov(Psi_theta, Psi_(d lambda)) = 0, is not decided; Q(d lambda) = 0 is
the equality case of O2." The same correction applies to L150-153 ("It is not a curl form"), L411-414 ("the consumer's
cost is not a curl form in theta even if Lemma O1 is true") and RESULT clause (3) ("it depends on theta on the boundary
links and is not a curl form in d theta"). The repair proposed for `library/gap-aligned-frame.md` (L420-421) should read
"Q is shown to be a form in d theta for theta zero on the pinned links only".

**The exact value (L283-284). HOLDS** (re-derived). V is a fixed field here, so Psi_V = X(B) and Q(d lambda) = - E[V(V A)] =
E[direct term of B] (Proposition A (i)). Gauge transform by g_z = e^(- eps n_z): out links return to U_l, and each in link
becomes e^(- eps n_tail) e^(eps Ad(U_l) n_z) U_l = exp(eps b_l - eps^2 (n_tail x Ad(U_l) n_z) + O(eps^3)) U_l with b_l = - D_l n
(BCH: [u, v]/2 = u x v). The second derivative of A along exp(eps b + eps^2 c) U is - direct(b) - 2 sum c_l . N_l. Hence
Q(d lambda) = E[direct(b)] - 2 sum_in (n_tail x Ad(U_l) n_z) . E[N_l], as stated. "Its sign depends on the frame" is not
proved in the text; it is a remark, and nothing rests on it.

**Scope lines (L278-281). HOLD as scope statements.** Upper faces: the in link (z - e_4, 4) is interior with an interior
tail, whose frame may read the private link (z - e_i - e_4, i). Different vectors per boundary link: outside 6.6.

**Test asked by row 1035: is "pin-measurable site frame" the class route (ii) needs? Answer: it is the class of the
consumer as written (row 1026 7.1), and it is narrower than route (ii) as a strategy.**
- Forced: the boundary rotation B must be a function of the pin, because H_c(omega; B) is the Hessian of F_c along a
  curve of pins. So the boundary values n_z, n_(z - e_i) used on pinned links must be pin-measurable. BD assumes no more there.
- Not forced: BD also puts the pin vector n_z on the interior link (z, 4). That comes from the site-frame form b_l = theta_l
  n_tail(l) (the tail of (z, 4) is the boundary site z). Lemma FLOW allows any interior field. Computation (this check,
  unchecked by another model): with a vector m(U, omega) on (z, 4) in place of n_z, the Gauss law gives
  Psi_V = sum_i (D_i n) . N_(z-e_i,i) + (n_z - m) . N_(z,4) + sum_a R_((z,4),a) m^a. P_i also enters N_(z,4), through the same
  plaquette p_i, with the term beta w Ad(U_(z-e_i,i))^(-1) s_(p_i). If m does not read P_1, P_2, P_3, the linear part in P_i is
  beta w (n_(z-e_i) - Ad(U_(z-e_i,i)) m) . s_(p_i), and constancy of Psi_V forces n_(z-e_i) = Ad(U_(z-e_i,i)) m for i = 1, 2, 3.
  So BD's conclusion moves from n_z to m: the three transports of the boundary frame into z must agree. If m reads a
  P_i, no affine argument applies; that is the boundary form of the bulk residue O1. The text's L339 already says
  "a different vector on the interior link out of the site is outside 6.6". Its ARGUED conclusion L342-344 ("route (ii)
  cannot return the scale-invariant blind bound") holds only for the site-frame consumer, as its own scope line says.
- So BD answers the consumer of row 1026 7.1, not every frame-move consumer of route (ii). No defect in BD; a precision
  for the lead's use of it.

**U(1) (L285). HOLDS.** D n = 0 for the constant frame, Psi = 0 (Gauss law at boundary sites).

Verdicts of Step 5: BD statement HOLDS; Consequences 1, 2 HOLD; Consequence 3 ("exact invariance", "not a curl form")
FAILS as written at L399, HOLDS AFTER CORRECTION (above); exact value HOLDS; scope lines HOLD; class: the consumer's
class, narrower than route (ii) (field-dependent vector on the links out of boundary sites not covered).

### Step 6 (done 2026-11-16T05:40Z): Proposition CURL (7.1, L290-318), Lemma FLUX and Lemma POT (7.2, L320-332)

**Test first: the sign. HOLDS.** By (a), Psi_theta = - sum_l theta_l c_l = - sum_p phi_p sum_(l in p) [p : l] theta_l = - sum_p (d theta)_p phi_p,
with (d theta)_p = theta_1 + theta_2 - theta_3 - theta_4 (theta = 0 off W). By (c), Q(theta) = E[Psi_theta^2] = - E[V_theta Psi_theta] =
+ sum_p (d theta)_p E[V_theta phi_p]. U(1) control: A = sum_p beta cos F_p gives N_l = sum_p [p : l] beta sin F_p, so phi_p = beta sin F_p,
V_theta phi_p = beta cos F_p (d theta)_p, and Q = sum_p beta E[cos F_p] (d theta)_p^2 >= 0: the classical form, with the right sign.
One plaquette (L316-317): phi = h(phi) = beta sin phi - 2 cot phi, moved along its own axis, gives K = [p : l] E[beta cos phi + 2/sin^2 phi];
the second term is finite because the Haar density of the class angle is proportional to sin^2 phi. Holds.

**Test first: the count. HOLDS** (Schur test, re-derived).
- Lambda_p(d lambda) = E[V_(d lambda) phi_p] = - E[phi_p Psi_(d lambda)] = 0 by (c) and d d = 0. This needs d lambda supported in W,
  which the distance condition (more than m from the complement of W) ensures for every p with (d theta)_p != 0. Holds.
- Links with one end point in B_p: phi_p does not read them when B_p has m = 2R + 3 sites per side, so K = 0 there, and
  Lambda_p(theta) = Lambda_p(theta - d lambda). Holds (the margin of 2R + 3 over the needed 2R + 2 covers it).
- Comb tree: a non-tree link of direction 2, 3 or 4 closes a loop through one, two or three strips, each of fewer than m
  plaquettes, in the planes (1, 2); (1, 3), (2, 3); (1, 4), (2, 4), (3, 4). So |Sigma_l| <= 3m, and theta'_l = sum over Sigma_l of
  +-(d theta)_p' (Stokes on the tree loop; d theta' = d theta). Holds.
- Row sums: sum_p' kappa(p, p') = sum_l |K(l, p)| |Sigma_l| <= 3m k_1. Column sums: p' lies in B_p for at most m^4 base points
  times 6 orientations, and kappa(p, p') <= sum_l |K(l, p)| <= k_1, so at most 6 m^4 k_1. Holds.
- Q <= sum_(p, p') kappa(p, p') |x_p| |x_p'| <= (1/2)(3m + 6m^4) k_1 sum x^2, and 3m/2 + 3m^4 <= 4m^4 because m^3 >= 3/2
  (m >= 3). The constant 4 m^4 k_1 holds. Holds.

**Proposition CURL. HOLDS given its hypotheses (a)-(c).** One precision on the hypotheses (no defect in the proof):
(c) asks integration by parts for phi_p and for Psi_theta, which are only L^2; (REG) of check 1027 asks it for smooth f.
So (c) is a strengthening of (REG), and the text says "(REG) for these functions" (L296), which is accurate. The
RESULT's wording "given a local potential (j - d = d* phi) and (REG)" should read "and (REG) extended to phi_p and Psi_theta".
Remark (no defect): by (c) with theta = 1_l, K(l, p) = E[phi_p c_l]. So the finite range of K says E[phi_p c_l] = 0 for l
outside B_p. That is an exact consequence of (c), not an extra decay assumption; the "blind" label (L313) holds.

**Lemma FLUX. HOLDS.**
- Summing conservation over the sites of the slice x_4 = s: the direction-1, 2, 3 terms cancel by periodicity in the slice,
  and the direction-4 terms give T_s - T_(s-1) = 0. Holds.
- T_t reads links within R' of the slice x_4 = t. With L >= 4R' + 4 there is t' whose slice is at distance at least 2R' + 2
  from t in both directions round the circle, so T_t and T_t' read disjoint sets of links. Holds.
- The Wilson measure has a positive bounded density against product Haar measure, so the two measures have the same
  null sets. If f(X) = g(Y) almost surely for independent X, Y, then by Fubini f is almost surely constant. Holds.
- E[c_l] = 0 is (REG) with f = 1 (E[V_theta 1] = 0 = - E[Psi_theta]). Holds.
- The slab field theta = 1 on the direction-4 links at height t is closed ((d theta)_p = 1 - 1 = 0 on the (mu, 4) plaquettes at
  height t, and 0 elsewhere) and not exact on the torus; Psi_theta = - T_t = 0. Holds. The words "a continuous family of
  maps that preserve the measure" (L327-328) need the flow of V_theta to exist; that is a remark, not used.

**Lemma POT (L329-332). ARGUED, as labelled. The sentence "With POT, (J) + (LOC) + (REG) give the hypotheses of 7.1"
(L332) HOLDS AFTER CORRECTION.**
- POT would give (a) and the finite range in (b). It does not give phi_p in L^2, nor the integration by parts (c) for
  phi_p and Psi_theta. Those are further conditions on phi.
- The cited source (Hydon and Mansfield, recalled, not fetched) treats the variational complex of difference
  equations: identities between functions of finitely many shifted variables. Here conservation holds almost surely
  for measurable functions on a product probability space. The fit of the citation is not checked here, and the
  text uses POT in no proof. The ARGUED label is right.
Correction: "With POT, (J) + (LOC) give (a) and the range in (b); (b)'s L^2 bound and (c) are further conditions on phi."

Verdicts of Step 6: CURL HOLDS (sign and count verified; constant 4 m^4 k_1 verified); FLUX HOLDS; POT ARGUED (agree);
L332 HOLDS AFTER CORRECTION.

### Step 7 (done 2026-11-16T05:50Z): Lemma SING, the odd-torus test (links i, j, k, 1), the cube count, the U(1) control

**Lemma SING (4.4, L109-114). HOLDS.** L >= 2r + 2 keeps the box B of side 2r + 1 from wrapping, so "n_x reads only B" is
a statement about a box. Let U' be +-1 on B. A constant gauge transformation g fixes U' on B (the values are central)
and changes links outside B only; n_x does not read them, so n_x(U'^g) = n_x(U'), while covariance gives Ad(g) n_x(U').
No unit vector is fixed by every rotation. For U gauge equivalent to U' on B (U = U'^h on B, h extended arbitrarily),
U^(h^(-1)) agrees with U' on B, so n_x is undefined there, and a gauge-invariant domain then excludes U. Holds.

**The odd-torus example is in that set (L116-117). HOLDS** (re-derived). With g_x = i^(x_1) j^(x_2) k^(x_3) on a box that
does not wrap: j^(x_2) k^(x_3) i = +- i j^(x_2) k^(x_3), so g_(x+e_1) = +- g_x U_1, and the same for directions 2, 3
(Ad(i) j = - j, Ad(i) k = - k, Ad(j) k = - k); g_(x+e_4) = g_x U_4. Hence g_x U_mu g_(x+e_mu)^(-1) = +-1. Holds.
"Large codimension, no threat to (REG)": every plaquette holonomy in B central is a closed condition of positive
codimension. Holds.

**The winding-loop frame on Z_3^4 (L121-131). HOLDS.**
- P(x) = U_(x,1) U_(x+e_1,1) U_(x+2e_1,1); on Z_3, P(x) = U_(x,1) P(x + e_1) U_(x,1)^(-1), so n_x = Ad(U_(x,1)) n_(x+e_1) and
  D_(x,1) n = 0 wherever n is defined. At the example P = i^3 = - i and n = - i. Ad(j)(- i) = i and Ad(k)(- i) = i, so
  D_(x,2) n = D_(x,3) n = - 2i; U_4 = 1 gives D_(x,4) n = 0 at the example. Holds.
- Jacobian: for n = Im P/|Im P| moved by P -> e^(eps e_a) P, the a-component of the derivative is cot(phi)(1 - (n^a)^2);
  the sum over a is 2 cot(phi). n_x reads no other out link of x, so d = 0 there; on the in links of direction 2, 3, 4,
  n_(z - e_mu) does not read the link. P(z) and P(z - e_1) are conjugate, so (div d)(z) = 2 cot(phi) - 2 cot(phi) = 0. Holds.
- d in L^2: cot^2(phi) sin^2(phi) = cos^2(phi) is integrable and the law of P has a bounded density. The integration by
  parts across {Im P = 0} (codimension 3) holds by a tube cut-off whose boundary term vanishes with the tube's radius.
  Holds; the text asserts it without this line.
- (J) reduces to sum over mu = 2, 3, 4 of (D_(z - e_mu, mu) n) . N_(z - e_mu, mu) = 0; it holds at the example (N = 0) and fails on
  every set of positive measure near it by PRIV (the frame reads direction 1 only; D_(z - e_2, 2) n is near - 2i). Holds.
- The verdict "the example gives no frame for (SYM); zero forces are not a model of a conserved current" holds.

**The cube count (4.3, L92-105). HOLDS.** 000 has no in link (STAR). The STAPLE vector at 110 uses the axis of
(000; 1, 2) carried to 110 along (000 -> 100 -> 110), which is covariant at 110 and does not read (110 -> 111); so
c = 0 on the three links into 111, and 111 is conserved. c_l reads only n_tail(l), so the six remaining equations
involve n_000, n_100, n_010, n_001 only: eight unknown functions. Holds. The claim on the frames with j = 0 cites check
1027 Step 5 (n_000 = +-(N_1 x N_2)/|N_1 x N_2| uses the Gauss law at 000, sum_out N = 0); not re-derived here.

**U(1) control (4.1 and the U(1) line of each statement). HOLDS.** n constant, D n = 0, d = 0, c = N = d* phi with
phi_p = beta sin F_p. Psi_theta = - sum_p (d theta)_p beta w_p sin F_p over all plaquettes of a cell, boundary included,
and Q(theta) = sum_p beta w_p E[cos F_p] (d theta)_p^2 <= beta sum_p (d theta)_p^2: the classical bound. Per statement: STAPLE
gives b = 0 (Ad = 1); LF's field is zero; PRIV and BD conclude D n = 0, which is true; Corollary P's last step needs
non-commuting axes and has no U(1) analogue (the constant frame satisfies (J)), so it is an SU(2) statement and U(1)
does not contradict it; CURL returns the constant beta E[cos F_p]. Zero gain in each case. Holds.

Verdicts of Step 7: SING HOLDS; odd-torus example in the singular set HOLDS; winding-loop frame HOLDS; cube count HOLDS;
U(1) control HOLDS.
