# Check of row 1038 `library/gap-collapse-frame.md` (row 1040)

Provenance: Claude Opus 5.5, max effort, background agent on the lead's
MacBook, commit 1a4ecc662; same provider as the author (Claude Fable 5.2
medium). This is not an independent provider check. Row 1041 (gpt-6-astra)
is the cross-provider check; I did not read its file.

Started 2026-11-16 10:29Z (from `date -u`).

## Plan (at most eight steps; each step appends its result below)

1. Read the file under check in full, and the background: row 1036
   `gap-boundary-q.md`, its two checks, `gap-sym-reg.md` 7.3-7.4, the luna
   read (row 1039), `parts/gap.md`.
2. Hand tests: H_c = 0 on the cube for the transported frame; the NOLIP
   constant sqrt(2/3)/k - 2 eps; one TUNE value at an explicit
   non-stationary pin.
3. Lemmas TG, LAD and Theorem LIP-TREE (r = S_1 + S_2, C_r = 2 sqrt(2)).
4. Theorem NOLIP; Lemma CUBE-H and the cube test (H_c = 0, Q = lambda_110^2
   times a variance).
5. Theorems ONE and ONE+ (pinned-end convention for free links; is it
   admissible for the consumer); Theorem LEAD (second order; no error
   constant).
6. Corollary BOTH (beta below 3/2), Theorem ORB, Lemma WEAK (MASS of row 1036
   as corrected), Theorem TUNE (closed form; descent direction, not a
   stiffness), covariant-cube and U(1) controls.
7. Judge the ARGUED meanings: (a) the weak form with (N1) is enough only for
   S^3 below the order of b; (b) route (ii) at the pinned boundary has no
   exact curl mechanism in the collapsing-defect class.
8. Verdict table and one RESULT line.

Scratch folder for any small numeric guide: a new empty folder under /tmp.
A numeric run proves nothing here; it can only refute or guide.

## Step results

### Step 1 (done 2026-11-16 10:31Z): sources read

Read in full: `library/gap-collapse-frame.md` L1-479 (the object; "L" below means its line);
`library/gap-boundary-q.md` (row 1036) L1-391; `library/gap-boundary-q-check-opus.md` L1-210;
`library/gap-boundary-q-check-astra.md` L1-508; `library/prior/gap-collapse-frame-read-luna.md` L1-53.
Read in part: `library/gap-sym-reg.md` L288-375 (7.1-7.4: CURL, O1, O2); `parts/gap.md` L130-147 (entries of
rows 1016-1038); `library/gap-pinned-cell-gauge-max.md` (row 1011) L440-501 (7.1-7.4: Lemma FR, the ARGUED size
estimate, (N1)-(N3)).

Definitions this check uses (row 1036 GR, as the object restates at L27-39). Quaternion conventions: for imaginary
u, v, u v = - u . v + u x v; Re(u q) = - u . Im q. Pinned link l = (x -> y), D_l n = n_x - Ad(omega_l) n_y. For lambda on L,
the curve omega_eps = (W_l(eps) omega_l), W_l = exp(- eps lambda_y n_x) exp(eps lambda_y Ad(omega_l) n_y); Psi = sum lambda_y (D_l n) . N_l;
Q(d lambda) = - E[(d/d eps)^2 A(U, omega_eps)]; H_c = (d/d eps)^2 F_c(omega_eps) = Q - Var(Psi). The frame values are frozen at
the base pin (astra L74-77).

Corrections carried from checks 1037 and astra (the object lists them at L33-39; I confirmed each against the
check texts): MASS needs abs(beta_p w_p) <= b with abs(beta_p w_p) on the right side (astra comparison item 1); the
GR "iff" is only "if" (astra L109-124); covariant cube frames carry a sign per site (both checks); O2 of row
1034 is existential, one frame and a set of pins of positive measure (gap-sym-reg L369-372); turning a pin-only
vector on a free link does not change Q (astra comparison item 7: E[N_l] = 0 for a free link by Haar
invariance).

What the row asks me to test against (row 1040 text): LIP-TREE with r = S_1 + S_2 and C_r = 2 sqrt(2); NOLIP with
density 3/4 and the constant sqrt(2/3)/k - 2 eps; CUBE-H and the cube test (H_c = 0, Q = lambda_110^2 times a
variance); ONE and ONE+ and the admissibility of the pinned-end convention; LEAD (second order, no constant);
BOTH (beta < 3/2) and ORB; WEAK (MASS as corrected); TUNE (closed form; descent direction, not stiffness);
controls; two ARGUED meanings.

### Step 2 (done 2026-11-16 10:50Z): the three hand tests. All three PASS

All by hand, from the definitions. No numeric run. I write â for the unit vector that the object calls a.

**Test (a): H_c = 0 on the cube for the transported frame (object L95-106). PASSES.**
- The move on the four pinned links is omega_l -> exp(eps (lambda_x - lambda_y) n_x) omega_l. I wrote out the moved
  holonomy factor by factor and moved every exponential to 000 with omega e^v = e^(Ad(omega) v) omega. Result:
  h(eps) = e^(eps (lambda_000 - lambda_100) u_0) e^(eps theta_1 u_1) h e^(- eps theta_2 u_2) e^(- eps (lambda_000 - lambda_010) u_0). The two exponentials
  in n_110 cancel inside the word, so n_110 never enters; lambda_000 drops out of t by cyclicity. This is L85-86.
- Transported frame: u_0 = u_1 = u_2 = â. Then t(h(eps)) = Re(e^(eps theta_2 â) h e^(- eps theta_2 â)) = t(h) for every eps.
  F_c is a function of t(h) alone (CUBE-Z, which both checks of row 1036 confirmed). So F_c(omega_eps) is constant and
  H_c = 0 for every pin, every lambda and every â (also a pin-dependent â, frozen at the base pin). On the GR curve the
  same computation gives h -> e^(- eps lambda_110 â) h e^(eps lambda_110 â), as L98 says.
- D n: D_a n = D_b n = D_(l_1) n = 0 by construction, and D_(l_2) n = Ad(omega_b)^(-1)(â - Ad(h)^(-1) â), so abs(D_(l_2) n) = 2 abs(s(h) x â).
- Q = Var(Psi): Psi = lambda_110 (D_(l_2) n) . N_(l_2) (only tau_(l_2) = lambda_110 meets a non-zero defect). N_(l_2) = (pin-only lower part)
  + beta Im(omega_2 R_2). So Q = H_c + Var = lambda_110^2 beta^2 Var((D_(l_2) n) . Im(omega_2 R_2)). This is (ii). (iii) follows from
  abs(Im q) <= 1; the strict sign holds because, for fixed vertical links, R_2 has a positive continuous density on SU(2).
- (iv): at the pin 1, Cov(N_(l_2)) = (beta xbar - kappa) times the identity (row 1036 4.3 (iv) with delta_1 = 0, and isotropy).
  The covariance is continuous in the pin, so Q = 4 (beta xbar - kappa) lambda_110^2 abs(s x â)^2 (1 + o(1)). HOLDS.
- (v) (direct and force terms): I recomputed the force term in the frame at 000. f_(l_2) = - (b_0 + kappa) s(h_010), n x D n = 2 eta_perp
  for h = e^eta, so 2 c . f = - 4 (b_0 + kappa) lambda_110^2 abs(eta_perp)^2 = - (b_0 + kappa) lambda_110^2 abs(D n)^2. The total
  direct + force = (beta xbar - kappa) lambda_110^2 abs(D n)^2 agrees with (iv). HOLDS. Notation only: L110 has the signs of c and f
  both flipped against "h = e^eta"; they are right for eta = log H_(l_2) (TG: H_(l_2) = h^(-1) for this tree). The product is
  the same.
- (vi) and the constant: lambda_110 = 0 gives b = 0 on all four links, so a pure gauge move. On the cube L is all four
  lower sites, so adding the constant - lambda_110 stays inside GR's class. HOLDS.

**Test (b): the NOLIP constant sqrt(2/3)/k - 2 eps (object L196-218). PASSES.**
- Path step: for l = (y -> y') the defect bound gives abs(n_y - Ad(upsilon_l) n_y') <= d; for l = (y' -> y) apply Ad(upsilon_l)^(-1).
  abs(Ad(u) m - m) = abs(u m - m u) = abs((u - 1) m - m (u - 1)) <= 2 abs(u - 1) < 2 eps for a unit m. So each step costs at most
  d + 2 eps, and abs(n_x - n_x') <= k (d + 2 eps).
- rho_g conjugates the links with both ends in N and fixes the rest. It preserves U_eps (abs(g omega g^(-1) - 1) = abs(omega - 1))
  and Haar measure. Four sets of relative measure above 3/4 have complements of total relative measure below 1, so
  they meet. On the links that n_x reads, rho_g omega equals the gauge transform by G = g on N, 1 off N; (L1) and (L3) give
  n_x(rho_g omega) = Ad(g) n_x(omega); (L2) gives n_x'(rho_g omega) = n_x'(omega). So abs(n_x - Ad(g) n_x) <= 2 k (d + 2 eps).
- Ad(i) is the rotation by pi about the first axis: abs(n - Ad(i) n)^2 = 4 (n_2^2 + n_3^2). The three squares add to 8, so
  the largest is at least 8/3. Hence d >= sqrt(8/3)/(2 k) - 2 eps = sqrt(2/3)/k - 2 eps. The constant is sharp for this
  step: n = (1, 1, 1)/sqrt(3) gives 8/3 for each g. So the GUIDE minimum 1.6386 of L219 is consistent.
- Consequence (a): on U_eps, abs(U_p - 1) < 4 eps for a face plaquette and abs(s(U_p)) <= abs(U_p - 1). HOLDS. Consequence (c):
  if "range r" means "reads links with an end within r", take N = the ball of radius r + 1; then x, x' at distance 2 r + 2
  on an axis satisfy (L1)-(L2). This is why k <= 2 r + 2. HOLDS.
- Sanity check against LIP-TREE: frame TREE escapes NOLIP because every n_x' reads the base plaquette at o, so (L2)
  fails for every x' when o is in N. Consistent.

**Test (c): one TUNE value at an explicit non-stationary pin (object L355-375). PASSES.**
- Pin: omega_a = e^(phi i), the other three pinned links 1, so h = e^(phi i), t = cos(phi) = 4/5, s = (3/5) i. The pin is
  non-stationary when b_0 + kappa(4/5) != 0; take sigma = +1 (the case b_0 + kappa(4/5) > 0; sigma = -1 is below).
- Frame: u_0 = j, w = (s x u_0)/abs(s) = k, tan(alpha/2) = 1/4, so cos(alpha) = 15/17, sin(alpha) = 8/17. Then
  n_000 = j, n_100 = Ad(omega_a)^(-1)(cos(alpha) j + sin(alpha) k), n_010 = cos(alpha) j - sin(alpha) k, n_110 free.
- Direct computation for theta = (1, 0) (lambda_100 = 1, the rest 0). The moved holonomy is h(eps) = e^(- eps j) e^(eps u_1) h. With
  j u_1 = - cos(alpha) + sin(alpha) i and d_1 . i = 0:
  t(eps) = [1 - sin^2(eps)(1 - cos alpha)] cos(phi) + sin^2(eps) sin(alpha) sin(phi), so t'(0) = 0 and
  H_c = - (b_0 + kappa) t''(0) = (b_0 + kappa) [2 (1 - cos alpha) cos(phi) - 2 sin(alpha) sin(phi)] = (b_0 + kappa) (16/85 - 48/85) = - (32/85)(b_0 + kappa).
  The closed form of L360 gives the same: (b_0 + kappa) t . 2 (1 - cos alpha) - 2 abs(b_0 + kappa) abs(s) sin(alpha).
- The same direct computation for theta = (1, 1) gives (b_0 + kappa)[4 sin^2(alpha) cos(phi) - 4 sin(alpha) cos(alpha) sin(phi)] = - (416/1445)(b_0 + kappa),
  and for theta = (1, - 1) it gives (b_0 + kappa)[4 (1 - cos alpha)^2 cos(phi) - 4 sin(phi) sin(alpha)(2 - cos alpha)] = - (1760/1445)(b_0 + kappa).
  Both equal the closed form. Three values fix a quadratic form in (theta_1, theta_2), so the closed form of L360 is
  verified in full at this pin. In units (b_0 + kappa)/1445 the form is - 544 theta_1^2 + 672 theta_1 theta_2 - 544 theta_2^2: negative
  definite (544^2 > 336^2).
- The bound of L362 at theta = (1, 0) is - (176/1445)(b_0 + kappa); the true value - (544/1445)(b_0 + kappa) lies below it. The
  sufficient condition of L364, 2 abs(t) tan(alpha/2) < abs(s) cos(alpha), reads 0.4 < 0.529 here. It holds.
- sigma = - 1 (w = - k): the same computation gives H_c = (b_0 + kappa) . 2 [(1 - cos alpha) cos(phi) + sin(alpha) sin(phi)] = - (64/85) abs(b_0 + kappa),
  again equal to the closed form. So the test does not need the sign of kappa(4/5), which I did not determine by hand.
- Q at this pin was not given a number: its sign needs beta^2 against abs(b_0 + kappa(4/5)) in L365. I checked only the
  algebra of L363 (Step 6).

### Step 3 (done 2026-11-16 10:51Z): Lemmas TG, LAD and Theorem LIP-TREE (object L155-194). TG and LAD HOLD; LIP-TREE HOLDS on one face

**TG (L155-168). HOLDS.**
- (a) P_x -> g_x P_x g_o^(-1) and a -> Ad(g_o) a give n_x -> Ad(g_x) n_x. With a = the axis of H_(l_0), H_(l_0) -> g_o H_(l_0) g_o^(-1), so a is
  covariant at o. Pin-measurable: yes.
- (b) Ad(omega_l) n_y = Ad(omega_l P_y) a = Ad(P_x H_l) a, so D_l n = Ad(P_x)(a - Ad(H_l) a). Ad(H) is the rotation about s(H) by twice the
  class angle, so abs((1 - Ad(H)) a) = 2 abs(s(H) x a) <= 2 abs(s(H)).
- (c) The gauge g_x = P_x^(-1) sends omega_l to H_l and n_x to a (P_o = 1).
- (d) W_l omega_l = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y) = P_x e^(- eps lambda_y a) H_l e^(eps lambda_y a) P_y^(-1). On a tree link H_l = 1, so
  the link does not move; hence P_x does not move. I add one fact that ORB needs: a does not move either, since
  conjugation by e^(eps lambda a) fixes the axis a of H_(l_0).
- The reading L167-168 ("the fixed colour a in the axial gauge") is correct. The sentence "The class 'collapsing
  defect' has this one known member" is too strong after the row 1039 reading: a constant colour in a Coulomb-type
  gauge (the lane's `library/lattice-uhlenbeck.md`, which the object itself cites at L142) is a second candidate. It is
  a box-wide 4D statement, so it is a candidate, not a written boundary frame. Neither is excluded by NOLIP (both read
  the whole box). This matters for Step 7.

**LAD (L170-175). HOLDS.**
- For unit quaternions: abs(u v - 1) = abs((u - 1) v + (v - 1)) <= abs(u - 1) + abs(v - 1); abs(c u c^(-1) - 1) = abs(u - 1);
  abs(u^(-1) - 1) = abs(u^(-1)(1 - u)) = abs(u - 1).
- The ladder induction is the standard lattice Stokes step: the boundary of m + 1 plaquettes is the boundary of the
  first m followed by the lasso of the last one, and the shared rung is traversed twice in opposite directions.
- Credit: the object rebuilds it and credits Balaban CMP 99 through the lane's port. I did not check the citation.

**LIP-TREE (L177-194). HOLDS on one face; the "boundary frame" wording of 4.5 needs "on one face".**
- The comb tree is a spanning tree: it has S_1 (S_2 + 1)(S_3 + 1) + S_2 (S_3 + 1) + S_3 = (number of sites) - 1 links and joins
  every site to o.
- Non-tree link (x, 2), x_1 > 0: the fundamental loop, based at (0, x_2, x_3), is the boundary of the ladder
  ((j, x_2, x_3); 1, 2), j = 0, ..., x_1 - 1; the rest of the loop is a common tail. So x_1 <= S_1 plaquettes.
- Non-tree link (x, 3), (x_1, x_2) != (0, 0): based at (0, 0, x_3), the loop is (a1 beta a1^(-1)) gamma, with beta the boundary of
  the ladder in the plane (1, 3) from x back to x_1 = 0 (x_1 plaquettes), gamma the boundary of the ladder in the plane
  (2, 3) at x_1 = 0 (x_2 plaquettes), a1 the tree path (0, 0, x_3) -> (0, x_2, x_3). I checked the word: inserting the vertical
  link at (0, x_2) and its inverse splits the loop into these two. So x_1 + x_2 <= S_1 + S_2 plaquettes, and LAD's
  second clause applies.
- Chain: abs(D_l n) <= 2 abs(s(H_l)) <= 2 abs(H_l - 1) (abs(H - 1)^2 = (1 - t)^2 + abs(s)^2) <= 2 sum over Sigma_l of abs(U_p - 1). For
  t(U_p) >= 0: abs(U_p - 1)^2 = 2 (1 - t) <= 2 (1 - t^2) = 2 abs(s(U_p))^2. So C_r = 2 sqrt(2), with at most S_1 + S_2 plaquettes,
  all within distance S_1 + S_2 of l. Both displays HOLD.
- Scope. The theorem is stated and proved for one face F with its comb tree. L229 (4.5) and the RESULT say "a boundary
  frame ... PROVED to exist". For the whole boundary of the 4D cell this is not written: limit (iv) at L193-194 says so.
  Correction to 4.5, first bullet: "PROVED on one face (comb tree), with r = S_1 + S_2 and C_r = 2 sqrt(2); a tree on the whole
  boundary with ladder loops is not written". The first bound holds wherever a is defined; the second needs
  t(U_p) > 0 on F, an open neighbourhood of the pure-gauge orbit. a is undefined on the orbit itself (luna's stabiliser
  argument), as limit (iii) says.

### Step 4 (done 2026-11-16 10:52Z): NOLIP; CUBE-H and the cube test. All HOLD; two summary lines need their qualifier

**NOLIP (L196-226). HOLDS.** The proof is checked line by line in Step 2, test (b). Further points.
- (L3) is weaker than full covariance and is used only at x in N. (L2) is used only through "rho_g does not change what
  n_x' reads". Nothing else about n is used. Correct.
- The measure is Haar measure on U_eps, a neighbourhood of the trivial pin. By covariance the same holds near every
  pure-gauge pin. The pin law of the surrounding model has a continuous positive density, so "density above 3/4"
  transfers up to a factor 1 + o(1) as eps -> 0. The object does not claim more.
- Meaning, stated exactly: for every c < sqrt(2/3)/k - 2 eps, the pins of U_eps where max over pi of abs(D n) >= c have relative
  measure at least 1/4. The 4.5 bullet (L232-233) says this correctly.
- "What NOLIP does not exclude" (L220-224) is marked ARGUED and feeds no proof. Not checked.

**CUBE-H (L79-93). HOLDS.** I re-derived it in general.
- With X = - eps theta_2 u_2, Y = eps (theta_2 - theta_1) u_0, Z = eps theta_1 u_1: t(h(eps)) = Re(e^X e^Y e^Z h). To second order
  e^X e^Y e^Z = 1 + (X + Y + Z) + (X^2 + Y^2 + Z^2)/2 + X Y + X Z + Y Z. X + Y + Z = eps v. The real part of the second-order terms is
  - abs(X + Y + Z)^2/2 = - eps^2 abs(v)^2/2. The imaginary part is X x Y + X x Z + Y x Z = eps^2 [- theta_1^2 u_0 x u_1 + theta_2^2 u_0 x u_2
  + theta_1 theta_2 (u_0 x u_1 - u_0 x u_2 + u_1 x u_2)], and the bracket is d_1 x d_2 (expand (u_1 - u_0) x (u_2 - u_0)).
- Re(P h) = Re(P) t - Im(P) . s gives t'(0) = - s . v and t''(0) = - t abs(v)^2 - 2 s . [...], as L88-89.
- F_c = F(t) with F = - b_0 t - log G, F' = - (b_0 + kappa), F'' = - kappa'. G > 0 and smooth on [-1, 1] (CUBE-Z). The chain rule gives L81.
- Checks L92-93: at the trivial pin, theta_1 = theta_2 = - 1 (lambda the indicator of 110) gives (b_0 + kappa) abs(n_100 - n_010)^2, which
  is row 1036 4.3 (iii). Correct. The GUIDE line is not a premise.

**The cube test, 3.2 (L95-118). HOLDS** (the computations are in Step 2, test (a)). The verdict bullets:
- "Exact (O2) ... FAILS on the cube for this frame at every pin with s x a != 0": correct, with its qualifier.
- Weak form with delta = 4 beta^2 abs(s x a)^2: correct (Q <= 4 beta^2 lambda_110^2 abs(s x a)^2 <= delta sum lambda^2).
- (O2-min) with equality and the constant: correct (Step 2).
- The covariant choice a = +-s/abs(s): correct; on the cube a covariant a at 000 must be fixed by the stabiliser circle
  of the pin (rotations about s at 000, extended along the four links; they fix the pin because they commute with h).
- Qualifier dropped later: 5.6 (L324-325) says the literal (O2) "FAILS for frame TREE on the cube (3.2, 3.3)". For frame
  TREE with the covariant a = +-s/abs(s), D n = 0 and Q = 0 for every lambda. Correction: "for frame TREE with a not
  parallel to s(h), that is a non-covariant a; the covariant a gives the zero form".

**Compact U(1) on the cube, 3.4 (L136-138). HOLDS.** With phases and site signs sigma_z, the four link angles move by
eps (lambda_x - lambda_y) sigma_x. Their oriented sum is eps [theta_1 (sigma_100 - sigma_000) - theta_2 (sigma_010 - sigma_000)] (I used
lambda_010 - lambda_100 = theta_2 - theta_1). The curve is linear in the class angle, so H_c = (d^2 F_c/d phi^2) times its square, and
there is no acceleration term.

### Step 5 (done 2026-11-16 10:53Z): Theorems ONE, ONE+ and LEAD. All three HOLD; ONE's title and two verdict lines need "unless the form is zero"

**ONE (L120-134). HOLDS** as stated in its body (L125-126). Title and summaries HOLD AFTER CORRECTION.
- lambda = 1 on the four lower sites is supported on L. d lambda = 0 on the pinned links, so the pin does not move and
  H_c = 0. V = n_z on the four vertical links, a fixed field: div V = 0, E[Psi] = 0, Q = - E[V Psi] = E[Psi^2].
- Psi = sum over the four pinned l of (D_l n) . N_l. I re-derived this without GR: the gauge transformation e^(eps n) at the four
  lower sites is a left rotation by n_z on each vertical link and moves each pinned link by D_l n to first order;
  gauge invariance of A gives V A = sum_l (D_l n) . N_l.
- Positivity: each side staple R_l contains exactly one top link, a different one for each l. For fixed vertical links
  the map from the four top links to (R_l) is a bijection of SU(2)^4 by left and right translations, with a positive
  continuous density. A non-zero D_l n makes Psi non-constant in R_l. So Var(Psi) > 0 unless D n = 0 on all four links.
- Correction (title L120, L349, L409, table L445): the form is negative semidefinite exactly when it is identically zero,
  which happens exactly when D n = 0 on the four pinned links (for example the common-sign axis frame of 3.2). So
  "never negative semidefinite" should read "never negative semidefinite unless it is zero", and L349 "No" should read
  "only the zero form, when D n = 0 on the four pinned links". This does not change any use: the zero form is the U(1)
  value with no gain.

**ONE+ (L306-319). HOLDS. The convention is admissible as an extension; it is not binding on the consumer.**
- At most one pinned end for S_mu >= 2: a free link (x, mu) has 0 < x_kappa < S_kappa for kappa != mu, so both ends on the boundary
  force x_mu = 0 and x_mu = S_mu - 1. Correct.
- GR (a) in the convention: with g = e^(eps lambda n) on the pinned sites, g_z^(-1) e^(eps lambda_z n_z) U = U on a free link out of z,
  and U e^(- eps lambda_y n_y) g_y = U on a free link into y. Pinned links as before. (b)-(e) are unchanged. Left and right
  translations by pin-only elements preserve Haar measure, so div V = 0, and Q(d 1) = E[Psi_1^2]. Correct.
- Positivity: for a face link l = (x, mu), mu in {1, 2, 3}, at distance at least 2 from the other faces and S_mu >= 4, the free link
  (x + e_4, mu) lies in one plaquette with a pinned link, p = (x; mu, 4), and l is the only pinned link of p. So that free
  link enters Psi only through beta (D_l n) . Im(omega_l R_p), and the conditional variance is positive. The null-set step:
  D n = 0 on all links of two face plaquettes at a deep site forces their axes to be parallel to n_x (Lemma FR), which
  is a null set of pins. Correct.
- Admissibility (the question of row 1040). (1) Lemma FLOW and GR accept it: it is a fixed field of left and right
  translations of free links, so H_c <= Q holds for it as for every extension. (2) It is mostly inside row 1034's class:
  U e^(- eps lambda_y n_y) = e^(- eps lambda_y Ad(U) n_y) U, so on a free link l = (x -> y) into an upper face it is the tail move of a
  site frame whose interior value is n_x = Ad(U_l) n_y, a field-dependent value that reads U_l. At an interior site with
  two links into upper faces it is a link frame. So L307 "outside the tail-vector site frames of row 1034" is true
  only at such edge sites. (3) It is not forced: for lambda = 1 the boundary rotation is 0 and the extension V = 0 gives
  Q = 0. So ONE+ refutes "Q(d lambda) <= 0 for all boundary lambda" in this convention (and in row 1034's convention with
  this interior choice); it does not refute row 1034's O2 with other interior values, and it says nothing about
  (O2-min). The object's own Reading (L318-319) draws the right conclusion.

**LEAD (L247-272). HOLDS** (asymptotic; no error constant, as the object says).
- (1) Phi(Ad(g) eta) = Phi(eta) for constant g. Each 3 x 3 block of the Hessian commutes with SO(3), so it is c times the
  identity (an antisymmetric part would be a cross product with a fixed vector, which no rotation group fixes).
  The same holds for the force covariance at the pin 1. The identification Hh_0 = K_0 - C_0 follows TP's proof: the
  expected second variation of A along e^(eps v) is the K_0 form (TP Step 3), and Var(A') is the C_0 form.
- (2) eta_l(eps) = R_a(- 2 eps lambda_l) eta_l gives eta' = - 2 lambda_l a x eta_l and eta'' = - 4 lambda_l^2 eta_perp,l. grad Phi(0) = 0 (the trivial pin
  is stationary). Then H_c = Hh(eta', eta') + Hh(eta, eta'') + O(abs(lambda)^2 abs(eta)^3) = 4 sum Hh_0 lambda_l lambda_l' (eta_perp,l . eta_perp,l')
  - 4 sum Hh_0 lambda_l'^2 (eta_perp,l . eta_perp,l'); symmetrising gives - 2 sum Hh_0 (lambda_l - lambda_l')^2 (...). Correct.
- (3) D_l n = a - Ad(H_l) a = - 2 eta_l x a + O(abs(eta)^2) and Cov at H = C_0 times the identity + O(abs(eta)) give the Var line. Correct.
- (4) Q = H_c + Var: - 2 (K_0 - C_0)(lambda - lambda')^2 + 4 C_0 lambda lambda' = 2 C_0 (lambda^2 + lambda'^2) - 2 K_0 (lambda - lambda')^2. Correct.
- Direct and force split (L259): -E[M(b)] and the diagonal e_l give 4 sum K_0 lambda lambda' (...); c_l = - 2 lambda_l^2 eta_perp,l in the tree
  gauge and f_l = (Hh_0 eta)_l + O(abs(eta)^2) give - 2 sum Hh_0 (lambda^2 + lambda'^2)(...). Their sum is Q. Correct.
- Cube check (L269): one non-tree link, so Q = 4 C_0 lambda_110^2 abs(eta_perp)^2 with C_0 = beta xbar - kappa. Agrees with Step 2.
- Remark (no defect): LEAD's proof uses only that a is a unit vector frozen at the base pin. The choice "a = axis of
  H_(l_0)" is needed only for ORB.

### Step 6 (done 2026-11-16 10:54Z): BOTH, ORB, WEAK, TUNE and the controls. All HOLD; BOTH's beta < 3/2 must travel with every use

**BOTH (L274-287). HOLDS for beta < 3/2 (part (ii)); part (i) for every beta > 0.**
- Tree: the comb tree of the face extends to a spanning tree of the whole pinned graph by adding links with at least
  one end off the face, so l_1, l', l_0 stay non-tree links. In tree gauge the non-tree links are free coordinates, so
  the pins of (i) and (ii) exist.
- (i): eta_perp is delta u on l_1 and 0 elsewhere (eta_(l_0) is parallel to a = a_0). LEAD: only (l_1, l_1) contributes, and its K_0 term
  has (lambda - lambda)^2 = 0. So Q = 4 C_0(l_1, l_1) delta^2 + O(delta^3), lambda_(l_1) = lambda_z = 1. At the pin 1 the four boundary
  staples of l_1 are real, so N_(l_1) = beta Im R_p and C_0(l_1, l_1) = (beta^2/3) E_1[1 - t_p^2] > 0. Frame TREE and Q are continuous where
  s(H_(l_0)) != 0. Correct.
- (ii): with eta_perp = (rho/M) u on l_1, rho u' on l', lambda_(l_1) = 1, lambda_(l') = 0, I get the (l_1, l_1) term 4 C_0(l_1, l_1) rho^2/M^2, the
  two mixed terms 4 [C_0(l_1, l') - K_0(l_1, l')] (u . u') rho^2/M = - 4 abs(Hh_0(l_1, l')) rho^2/M, and the (l', l') term 0. The error is O(rho^3)
  with a constant free of M >= 1. H_c has only the mixed terms. So Q < 0 and H_c < 0 for M large, then rho small; u' -> - u'
  gives H_c > 0. Correct.
- beta < 3/2: (y; 2, 3) is the only plaquette with both l_1 = (y, 2) (as l_1, sign +) and l' = (y + e_3, 2) (as l_3, sign -); it lies in
  the face {x_4 = 0} only (its links span x_3 in {z_3, z_3 + 1}), so K_0 = beta (1/2)(1)(- 1) = - beta/2. abs(C_0(l_1, l')) <= beta^2 (1/3) by
  Cauchy-Schwarz and isotropy. So Hh_0 <= - beta/2 + beta^2/3 < 0 for beta < 3/2. Correct.
- Scope that must travel: the lane's bare couplings 2.3-2.6 (the range check 1037 Step 5 cites from row 1018) are outside
  beta < 3/2. So at those couplings the row proves BOTH (i) only, which is about Q with the GR extension and says
  nothing about H_c. 5.6 (L329-330, "in the 4D cell H_c has both signs on open sets (BOTH, ORB)") drops the
  hypothesis; the RESULT keeps it. Correction to L329: add "(beta < 3/2)". (A remark for the lead, not checked by
  anyone and not used in any verdict here: Hh_0(l_1, l') is a real-analytic function of beta that is non-zero on (0, 3/2),
  so it vanishes at most on a discrete set of beta.)

**ORB (L289-298). HOLDS.**
- Along the GR curve of frame TREE the tree links do not move (Step 3), so P_x does not move; a does not move (Step 3).
  So n(omega_eps) = n(omega). Then the GR curve from omega_eps with its own frame is delta -> omega_(eps + delta): on each link,
  e^(- delta tau n_x) e^(- eps tau n_x) omega_l e^(eps tau n_y) e^(delta tau n_y). So phi''(eps) = H_c(omega_eps). F_c is continuous on a compact space, so phi
  is bounded. A bounded concave (or convex) function on R is constant. If phi is not constant, phi'' takes both signs,
  and continuity of H_c where a is defined gives the two open sets. Correct.
- The torus paragraph: conjugations of the H_l by e^(theta_head(l) a) commute and have period 2 pi, so the group is a compact
  torus; F_c has a maximum on each orbit, and there phi''(0) <= 0 for every lambda. Correct. Precision: the set of orbit
  maxima is closed relative to the open set where a is defined, not closed in the whole pin space.
- Haar measure is invariant under these maps (for fixed tree links and l_0, each non-tree link is multiplied on the
  left and right by fixed elements). The pin law of the surrounding model need not be. The object does not use either.

**WEAK (L300-304). HOLDS** with MASS in its corrected form (abs(beta_p w_p) <= b, and abs(beta_p w_p) on the right; astra
comparison item 1). Per plaquette (sum over at most four pinned links)^2 <= 4 sum of squares; at most six plaquettes per
link: 24 and 12. TG (b): abs(D_l n) <= 2 abs(s(H_l)), so 24 abs(D n)^2 <= 96 abs(s)^2 and 12 abs(D n) <= 24 abs(s). Grouping by heads gives
delta(omega) sum_z lambda_z^2. delta -> 0 at the pure-gauge orbit (H_l -> 1 in tree gauge). Correct. Note for Step 7: for small abs(s(H_l)) the
linear term 24 b abs(s(H_l)) dominates delta; it comes from the crude bound abs(E[N_l]) <= 6 b of MASS.

**TUNE (L355-387). HOLDS** (closed form: Step 2, test (c), and the general line below).
- u_0 x w = u_0 x (s x u_0)/abs(s) = s/abs(s) for u_0 orthogonal to s. d_1, d_2 lie in the span of u_0 and w, so s . d_i = 0 and the kappa' term
  vanishes. u_0 x d_1 = sigma sin(alpha) s/abs(s) = - u_0 x d_2. (d_1) x (d_2) = - 2 (cos alpha - 1) sigma sin(alpha) u_0 x w = 2 sigma (1 - cos alpha) sin(alpha) s/abs(s). CUBE-H
  then gives L360, with sigma (b_0 + kappa) = abs(b_0 + kappa). Correct.
- Bounds L362-365: (theta_1 -+ theta_2)^2 <= 2 (theta_1^2 + theta_2^2) and (1 - cos alpha)^2 + sin^2(alpha) = 2 (1 - cos alpha) give the first bracket
  <= 4 (theta_1^2 + theta_2^2)(1 - cos alpha); - 2 (1 - cos alpha) theta_1 theta_2 >= - (1 - cos alpha)(theta_1^2 + theta_2^2) gives the second bracket >= cos(alpha)(theta_1^2 + theta_2^2).
  abs(D_a n) = abs(D_b n) = abs(d_1) = 2 sin(alpha/2). The random part of N_a, N_b is beta Im(omega R) with norm at most beta, so the
  variance is at most 8 beta^2 sin^2(alpha/2)(theta_1^2 + theta_2^2). With 1 - cos alpha = 2 sin^2(alpha/2) and sin(alpha) = 2 sin(alpha/2) cos(alpha/2) the sum is L363,
  and dividing by 4 sin(alpha/2) cos(alpha/2) gives L364-365. Correct.
- The extension: lambda_110 = 0 is a member of GR's class on the cube (L is the four lower sites), and d lambda on all links is a
  gradient, so the curl is 0. theta_1 = theta_2 = 0 with lambda_110 = 0 leaves only lambda_000: a gauge move at 000. Correct.
- Not covariant: a covariant n_000 is fixed by the stabiliser circle of the pin, so it is +-s/abs(s); TUNE needs u_0
  orthogonal to s. Correct. Defect: by Lemma FR, abs(D n) summed over the four links is at least 2 abs(s x u_0) = 2 abs(s); with
  abs(D_a n) = abs(D_b n) = 2 sin(alpha/2), the rest sits on l_1, l_2, where tau = lambda_110 = 0. Correct.
- "A descent direction of F_c and not a stiffness" (the question of row 1040). It HOLDS in this exact form. The pin
  curve's velocity is tangent to the level set of F_c: t'(0) = - s . v = 0, so dF_c/d eps = 0. The negative part of H_c is
  2 (b_0 + kappa) s . (bracket). Its diagonal terms are exactly GR's force terms 2 c_l . f_l (I checked: c_a = - theta_1^2 u_0 x d_1 and
  f_a = (b_0 + kappa) s in the frame at 000; for b the inverse link turns c into - c). So the negative part is linear in
  abs(grad F_c) = abs(b_0 + kappa) abs(s) and of first order in alpha. The term (b_0 + kappa) t abs(v)^2, the second derivative along the
  velocity, is of second order in alpha and is >= 0 when t >= 0 and b_0 + kappa > 0. So the cost is negative because the
  curve's acceleration points down the gradient of F_c, not because F_c is concave. Wording correction to L385:
  "the velocity is tangent to the level set; the acceleration c = lambda^2 n x D n points down the gradient" (the velocity
  itself is not a descent direction). It is void at stationary pins: there f = 0.

**Covariant cube frames and compact U(1), 6.3 (L389-395). HOLDS.** Covariant n_z = sigma_z s(h_z)/abs(s(h_z)) moved to 000 is
sigma_z s/abs(s), so d_i = (sigma_i - sigma_0) s/abs(s), all cross products vanish and v = m s/abs(s) with m = theta_1 (sigma_100 - sigma_000) - theta_2 (sigma_010 - sigma_000).
CUBE-H gives [(b_0 + kappa) t - kappa' abs(s)^2] m^2. With t = cos(phi): d^2 F(cos phi)/d phi^2 = F''(t) sin^2(phi) - F'(t) cos(phi) = - kappa' sin^2(phi) + (b_0 + kappa) cos(phi).
Equal. The U(1) formula of 3.4 has the same form (Step 4). Zero gain: correct. Other U(1) controls: GR (D n = 0 for one
axis), LEAD (no eta_perp), ORB (the curves are points for one axis). All correct.

### Step 7 (done 2026-11-16 10:56Z): the two ARGUED meanings. Both FAIL as written; both HOLD AFTER CORRECTION in a narrower form

**(a) "The weak form with (N1) is enough only for S^3 below the order of b" (L336-342, RESULT).**
The chain is L332-339. I list the links that do not hold as written.
- L333-334: "The gradient part of theta is not small: the boundary links carry sum theta^2 of order f^2 S^5". The cited
  fact (row 1034 7.3) is about the whole boundary restriction of theta, not its gradient part. No line of the row says
  what the gradient part of the consumer's twist is.
- L336-337: "The weak form is enough only if delta(pin) is at most of order b/S". This compares delta sum_z lambda_z^2 with
  b f^2 S^4 and so takes sum_z lambda_z^2 of order f^2 S^5. WEAK bounds by the values lambda_z, not by d lambda. A gradient part with
  abs(d lambda) of order f S per link has lambda up to order f S^2 on a face of side S, so sum lambda^2 can be larger by S^2.
- L337: "delta of order b abs(s(H_l))^2". WEAK's delta has the term 24 b abs(s(H_l)), which dominates when abs(s(H_l)) is small (Step 6).
  "Of order b abs(s)^2" needs a force estimate finer than MASS's abs(E[N_l]) <= 6 b. That estimate is not in the row.
- **First failing line: L337, "loops of area up to S^2".** For frame TREE the loop of H_l bounds ladders of at most
  S_1 + S_2 plaquettes (LIP-TREE; Step 3). With the size estimate min(1, a/b) and a <= S_1 + S_2, the condition
  abs(s(H_l))^2 <= 1/S of L337 needs S^2 below b, not S^3. (The proved LIP-TREE bound with Cauchy-Schwarz gives abs(s(H_l))^2 up to
  order S^2/b, which gives S^3; but that is an upper bound, and an upper bound cannot give "only".) L238-240 has the same
  slip: "a strip of S plaquettes" and then "S^2 well below b".
- "Only" is a necessity claim. WEAK and MASS are upper bounds, and no lower bound on the cost at typical pins is
  proved. So the statement can only be about this tool, given ARGUED typical sizes.
- What holds. The error term of the weak form is small only if delta(pin) is small, that is only if the holonomies
  of the fundamental loops (ladders as long as the face) are small; by the ARGUED Gaussian size estimate this needs
  b at least of the order of a positive power of the cell side S, the regime of small effective coupling at the cell
  scale; at order-one coupling and large S it fails for typical pins.
- Verdict: FAILS as written (the exponent 3; first failing line L337). HOLDS AFTER CORRECTION with this text: "ARGUED:
  the weak form turns (N1) into the consumer's bound only when the holonomies of face-length ladder loops are
  small at typical pins, which by the Gaussian size estimate needs b above a positive power of S (the power is not
  fixed here); at order-one coupling it fails for typical pins."

**(b) "Route (ii) at the pinned boundary has no exact curl mechanism in the collapsing-defect class" (RESULT L479;
the same reading in `parts/gap.md` L147).**
- What is proved, all for frame TREE: in the 4D cell near pure gauge, for lambda the indicator of z and beta < 3/2,
  H_c < 0 on one non-empty open set and H_c > 0 on another (BOTH (ii)); along every torus orbit where F_c is not
  constant, H_c has both signs (ORB); the literal O2 fails once the extension admits constants (ONE, ONE+); the weak
  form holds (WEAK). Fixed-range covariant rules cannot collapse on sets of density above 3/4 (NOLIP).
- What is not proved. (1) Other members of the class. The object treats one frame and says the class has "this one
  known member" (L168). A constant colour in another gauge (Coulomb type, row 1039's `lattice-uhlenbeck.md`), or frames
  from several base points, are not treated; ORB's group property used that frame TREE does not change along its
  own curves, and that is not known for them. (2) The lane's couplings: BOTH (ii) needs beta < 3/2; at beta 2.3-2.6 the
  row proves no sign change of H_c for frame TREE (Step 6). (3) The quantifier. BOTH and ORB refute (O2-min) at almost
  every pin near pure gauge. They do not refute row 1034's existential form (one set of pins of positive measure):
  ORB itself gives a non-empty set (orbit maxima) where (O2-min) holds for every lambda, measure not computed. (4) The
  cube: there frame TREE gives the exact U(1) value 0 on every boundary gradient (Step 2), which is an exact mechanism
  with zero gain.
- **First failing line: L479 (RESULT), "in the collapsing-defect class".** The proofs reach one frame of the class.
- Verdict: FAILS as written. HOLDS AFTER CORRECTION with this text: "For frame TREE, the one written member of the
  collapsing-defect class, in the 4D cell: (O2-min) is false on a non-empty open set of pins near pure gauge when
  beta < 3/2 (BOTH), and it has no sign along any torus orbit where F_c is not constant (ORB); so it does not hold at
  almost every pin near pure gauge. On the cube the same frame gives the U(1) value 0. Other members of the class, the
  couplings beta >= 3/2, and the existential form of O2 are open."

**The proposed texts for the lead (L471-477).**
- `parts/gap.md`: "fails for every fixed range on most pins near pure gauge (NOLIP)" overstates NOLIP. NOLIP shows the
  bound cannot hold on any set of density above 3/4; the failure set has density at least 1/4, not "most". Replace by
  "cannot hold on any set of pins of density above 3/4 near the trivial pin (NOLIP)". "LIP holds with range of the
  order of the face" needs "on one face". "has no sign in the 4D cell" needs "(near pure gauge for beta < 3/2;
  along non-constant orbits)". The same three changes apply to the row 1038 entry already in `parts/gap.md` L147.
- Row 1034's O2 replaced by (O2-min): correct as the extension-free necessary form, since every FLOW bound is at least
  H_c (F1, F2). It is not sufficient for a FLOW-based blind bound: that still needs one extension V with
  Var(Psi_V) <= - H_c. The quantifier must be written: "at almost every pin" (refuted for frame TREE near pure gauge,
  beta < 3/2) or "on a set of positive measure" (weak; see (3) above).

### Step 8 (done 2026-11-16 10:58Z): verdicts, limits, RESULT

Provenance: Claude Opus 5.5, max effort, background agent on the lead's MacBook, commit 1a4ecc662; same provider as the
author (Claude Fable 5.2 medium), so this is not an independent check. One session, no subagents, by hand. No numeric
run: no verdict needed one. Only this file was written. Not an audit.

Change of HEAD during the check. After Step 7 (10:56Z) I found the working copy's HEAD at 027013828, two commits after 1a4ecc662
(subjects: "Codex lane output, gap-collapse-frame-check-astra" and "record cross-provider check 1041 of row 1038").
`git diff --stat 1a4ecc662 027013828` shows no change to the object or to any library file I read; it shows a
one-line change to `parts/gap.md`. I read only the two commit subjects. I did not open the astra file or the changed
line. My citations of `parts/gap.md` L147 are to its text at 1a4ecc662.

| Item (object lines) | Verdict |
|---|---|
| Test (a): H_c = 0 on the cube, transported frame | PASSES (direct: t(h(eps)) = t(h) for every pin, lambda, â) |
| Test (b): NOLIP constant sqrt(2/3)/k - 2 eps | PASSES (and sharp for its step) |
| Test (c): TUNE at h = e^(phi i), sin(phi) = 3/5, tan(alpha/2) = 1/4 | PASSES (H_c = - (32/85)(b_0 + kappa(4/5)) at theta = (1, 0); the whole form equals L360) |
| TG (L155-168) | HOLDS; "one known member" (L168) too strong (Coulomb-type candidate) |
| LAD (L170-175) | HOLDS |
| LIP-TREE (L177-194), r = S_1 + S_2, C_r = 2 sqrt(2) | HOLDS on one face; L229 and the RESULT need "on one face" |
| NOLIP (L196-226) | HOLDS |
| CUBE-H (L79-93) | HOLDS |
| Cube test 3.2 (L95-118): H_c = 0, Q = lambda_110^2 beta^2 Var | HOLDS (L110: sign notation only) |
| ONE (L120-134) | HOLDS; title, L349, L409, L445 HOLD AFTER CORRECTION ("unless the form is zero") |
| U(1) on the cube 3.4 (L136-138) | HOLDS |
| LEAD (L247-272) | HOLDS (asymptotic; no error constant, as stated) |
| BOTH (L274-287) | HOLDS; (ii) for beta < 3/2 only; L329 HOLDS AFTER CORRECTION (add "beta < 3/2") |
| ORB (L289-298) | HOLDS (the maxima set is closed relative to the domain of a) |
| WEAK (L300-304) | HOLDS (MASS with abs(beta_p w_p) in hypothesis and bound) |
| ONE+ (L306-319) | HOLDS; the convention is an admissible FLOW extension, mostly a row-1034 site frame with interior value Ad(U_l) n_head; not binding on the consumer |
| 5.6 literal (O2) "FAILS for frame TREE on the cube" (L324-325) | HOLDS AFTER CORRECTION ("for a not parallel to s(h)") |
| TUNE (L355-387) | HOLDS; "descent, not stiffness" HOLDS with L385 reworded (velocity tangent to the level set, acceleration down the gradient) |
| Covariant cube frames and U(1), 6.3 (L389-395) | HOLDS |
| (A) verdict 4.5 (L229-242) | HOLDS AFTER CORRECTION ("on one face"); L238-240 has the S vs S^2 slip of Step 7 |
| ARGUED (a): weak form with (N1) enough only for S^3 below b | FAILS as written, first failing line L337; HOLDS AFTER CORRECTION (Step 7 text) |
| ARGUED (b): no exact curl mechanism in the collapsing-defect class | FAILS as written, first failing line L479; HOLDS AFTER CORRECTION (Step 7 text, frame TREE only) |
| Proposed `parts/gap.md` text (L472-476) | HOLDS AFTER CORRECTION ("most pins" -> "no set of density above 3/4"; "on one face"; BOTH's scope) |
| Proposed O2 -> (O2-min) (L477) | correct as the extension-free necessary form; write the quantifier; not sufficient for a FLOW bound |

Defects that break something, ranked (each repair is a narrowing; none needs a new proof):
1. RESULT L479 and `parts/gap.md` L147: "no exact curl mechanism in the collapsing-defect class" is proved for frame
   TREE only, near pure gauge, for beta < 3/2, in the almost-every-pin form.
2. L337 (and L240): the exponent S^3 rests on "loops of area up to S^2"; the loops are ladders of at most S_1 + S_2
   plaquettes, and WEAK bounds by lambda values, not by theta.
3. L329: BOTH's hypothesis beta < 3/2 is dropped; the lane's couplings 2.3-2.6 lie outside it.
4. Proposed `parts/gap.md` text: "fails ... on most pins" overstates NOLIP (density above 3/4 is excluded; the failure
   set has density at least 1/4).
5. L229 and the RESULT: LIP-TREE is proved on one face, not on the whole boundary.
6. L120, L349, L409, L445: the zero form is negative semidefinite; L324: frame TREE on the cube fails only for a
   non-covariant a.
7. Wording only: L385 ("descent direction"), L307 ("outside" the site frames), L168 ("one known member"), L110 (signs).

Not checked: the object's literature citations (Step 2; page numbers of Balaban CMP 99 and CMP 102, Uhlenbeck); its
GUIDE run and the row 1036 GUIDE value 1.149; the ARGUED thin-set example (L220-224) and the covariant TUNE in a larger
cell (L380-381). Not read: row 1026 7.1, row 1011 4.2, row 1034 Theorem BD; for FLOW and the frame class I relied on the
two checks of row 1036. OPEN, as the object says: exact (O2) for lambda on L and class (C) in the 4D cell, a tree on the
whole boundary, tilings, the error constant of LEAD.

RESULT: Row 1040, check of row 1038 (`library/gap-collapse-frame.md`, unchanged from 1a4ecc662 to 027013828) by Claude Opus 5.5 max on the lead's MacBook, commit 1a4ecc662; same provider as the author (Claude Fable 5.2 medium), so not independent; by hand, no numeric run. Tests PASS: H_c = 0 on the cube for the transported frame at every pin and every lambda (direct computation, t(h(eps)) = t(h)); the NOLIP constant sqrt(2/3)/k - 2 eps (sharp for its step); TUNE at h = e^(phi i) with sin(phi) = 3/5 and tan(alpha/2) = 1/4 gives H_c = - (32/85)(b_0 + kappa(4/5)) at theta = (1, 0), and the whole quadratic form equals the closed form. HOLDS: Lemmas TG, LAD, CUBE-H, WEAK (with MASS as corrected), Theorems NOLIP, LEAD (asymptotic, no constant), ORB, ONE+, TUNE, the cube test (H_c = 0, Q = lambda_110^2 beta^2 times a variance), the covariant-cube and U(1) controls (zero gain); LIP-TREE on one face with r = S_1 + S_2, C_r = 2 sqrt(2); BOTH (ii) for beta < 3/2; ONE+'s pinned-end convention is an admissible FLOW extension (mostly a row-1034 site frame with interior value Ad(U_l) n_head) but not binding on the consumer, so it refutes (O2) only in that convention and says nothing on (O2-min); TUNE's negative cost is the force term along the curve's acceleration with the velocity tangent to the level set, so "a descent direction of F_c, not a stiffness" holds. HOLDS AFTER CORRECTION: ONE's title and L349, L409, L445 ("never negative semidefinite unless the form is zero"); L229 and the RESULT's LIP claim ("on one face"); L324 ("for a non-covariant a"); L329 (add "beta < 3/2"); the proposed parts/gap.md text ("most pins" overstates NOLIP, which excludes density above 3/4); (O2-min) as the replacement of O2 needs its quantifier and is necessary, not sufficient, for a FLOW bound. FAILS as written: the ARGUED "weak form with (N1) is enough only for S^3 below b", first failing line L337 (loops of area up to S^2 against LIP-TREE's ladders of at most S_1 + S_2 plaquettes; WEAK bounds by lambda values), corrected to "only when face-length ladder holonomies are small at typical pins, which needs b above a positive power of S; fails at order-one coupling"; the ARGUED "route (ii) at the pinned boundary has no exact curl mechanism in the collapsing-defect class", first failing line L479, corrected to frame TREE only ((O2-min) false on an open set near pure gauge for beta < 3/2 and without sign along non-constant orbits; the existential form, beta >= 3/2 and other members such as constant-colour frames in a Coulomb-type gauge stay open). Not checked: the object's literature citations, its GUIDE run, its ARGUED thin-set and covariant-TUNE remarks.
