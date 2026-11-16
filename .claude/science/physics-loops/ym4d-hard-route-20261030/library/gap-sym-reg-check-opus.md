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
