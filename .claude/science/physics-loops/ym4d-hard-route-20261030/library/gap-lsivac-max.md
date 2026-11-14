lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T18:25Z

# gap-lsivac-max (FINISH row 941): (LSI-vac) / (HC-vac) for the SU(2) vacuum slice law on one box

Author: Claude Fable 5.2 max, Mac mini worker 2. Pinned at commit f529763f2, branch `claude/ym4d-hard-route`.
Research-stage working state. Nothing here is a public claim. No statement below is checked by another model yet (check row 943).

Status words: PROVED, CONDITIONAL (on named inputs), GUIDE (a run or heuristic; refutes or guides only), OPEN.

## Plan (at most eight steps; one step per response; each step is appended before the next starts)

0. Read: FINISH/GOAL (done), `library/gap-direction-max.md` in full, `library/prior/gap-lit-hcvac.md`, `library/gap-etohc-opus.md`, check row 938, row 936 (CUT-TYP). Duplicate check against `library/open-core.md` and the FINISH rows. Write the exact target and what is already covered.
1. Fix the objects: the vacuum slice law nu, (LSI-vac)_alpha, (HC-vac)_alpha, Proposition HC, the numbers. Restate in one self-contained block.
2. Fact tests before any proof: U(1), frozen Q_8 and 2T, SMALL-BOX, the ceilings. Each as a statement with its computation.
3. First attack (to be fixed after Step 0).
4. Second attack.
5. Third attack.
6. If not closed: the smallest unproved inequality and one solvable-model test that could refute it.
7. RESULT line.

## Step log

### Step 0: inputs read, duplicate check, the target with the checks' corrections (written 2026-11-14T06:50Z)

**Read in full (READ = read at the pinned commit, not re-proved):** FINISH.md (opening, How we work, Working
efficiently, Rules, rows 931-943), GOAL.md, `library/gap-direction-max.md` (row 931), its check
`library/gap-direction-check-astra.md` (row 938, Codex gpt-6-astra), `library/prior/gap-lit-hcvac.md` (row 939),
`library/gap-etohc-opus.md` (row 940, Claude Opus 5.5, unchecked; check row 942 not on disk),
`library/gap-cuttyp-max.md` (row 936, unchecked).

**Duplicate check (rule 0a).** `grep -n -i -E "LSI-vac|HC-vac|SG-step|log-Sobolev|hypercontract|ground.state"` on
`library/open-core.md`: no hit. Same terms on `library/l17c.md` and `library/open-registry.md`: no hit. FINISH rows
with the terms: 931 (names the lemma), 939 (reading), 940 (the implication (E-to-HC), proved there), 941 (this
row), 943 (its check). No other row attacks (LSI-vac) or (HC-vac). I proceed. I stay off (CUT-TYP), (TYP-1),
(EVEN-PI), (OD) (row 936), (VAC-SUB) (row 934), (E-to-HC) (row 940).

**Repo search.** This clone holds only `claude/ym4d-hard-route` (row 940 records the same), so origin/main and the
PR branches are not searched here. Check 938 and row 939 ran that search for the same terms on the laptop: no
owner, nearest prior text `gap-skeleton-max.md` B11 (hypercontractivity named as a route, citation from memory).

**The target, with the corrections of check 938 and the constant of row 940.**
- Chain: P = Omega^(-1) (T/lambda_0) Omega on L^2(nu), nu = Omega^2 dU, T the Wilson transfer operator of the
  periodic spatial box B, gauge-invariant functions.
- Proposition HC (row 931; HOLDS in check 938 for integer times): (HC-vac)_alpha' gives
  X(2m + 2; B) <= 72 beta |B| e^(-2 alpha' m) for integer m >= 0.
- Seed on B = (24a)^3, a even: X(a; B) <= x_* = log(22/17) once
  alpha' (a - 2) >= log(72 beta 24^3/x_*) + 3 log a. The constant is below 16.0 at beta 2.3 and about 16.12 at 2.6
  (check 938). This is the SH seed. For the two numbers of Form W on the same box use log(20/19) for x_*: the
  constant is then about 17.61 at beta 2.3 (check 938).
- Row 940 (unchecked): (LSI-vac)_alpha and (SG-step)_sigma give (HC-vac)_alpha' with
  alpha' = (1/2) log(1 + alpha/sigma^2). So the target of this row is the pair (LSI-vac), (SG-step) on the one box,
  or (HC-vac) directly.
- Size of the claim (GUIDE, recalled lattice numbers, no proof weight): alpha' <= E_1 (Proposition HC), and E_1 is
  near 1.3 at beta 2.3 and near 0.5 at beta 2.6 (lightest glueball in lattice units). So a is at least about 20 at
  beta 2.3 and about 60 at 2.6, and the box side 24a is 500 to 1400 lattice units.

**Plan, revised after the reading (still at most eight steps).**
1. Objects in ambient form: the chain without gauge projection, the exponential-family structure of the one-step
   law, the convex function Lambda with log Omega = Lambda(beta .) - const on the slice space. Exact formulas.
2. Fact tests, before any proof: U(1), frozen Q_8 and 2T, SMALL-BOX, ceilings, for the target and for the handles
   of Step 1.
3. Attack A: curvature (Bakry-Emery) of the slice law nu and of the mid-slice law eta, in closed form.
4. Attack B: averaged forms through Gaussian domination (no supremum over the conditioning slice).
5. Attack C: where the box size enters (two-scale or block form), if A and B leave room.
6. The smallest unproved inequality and one solvable-model test.
7. Result table and RESULT line.

### Step 1: the objects in ambient form (PROVED, by hand; identities, no estimate)

Credit. Transfer frame: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (outline
(GL8), as located by checks 927, 933, 938). The chain P, Proposition HC, Theorems V and E: row 931. (E-to-HC),
Lemma SGC, Theorem HC1: row 940. What is new in this step: the chain is written without gauge projection, and the
one-step law is read as an exponential family. Every formula below follows from that.

**Notation.** B a periodic box of side at least 3, L = 3|B| links, M = (S^3)^L inside R^N, N = 4L. A link variable
is a unit quaternion; <a, b> is the R^4 inner product, so (1/2) tr(a b^(-1)) = <a, b>. <x, w> = sum over links.
V(x) = -beta sum over spatial plaquettes of (1/2) tr x_p. dx is the product Haar measure on M.

**(A1) The chain without gauge projection.** T_0(x, w) := e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2) (temporal links
set to 1). T = T_0 Pi_G = Pi_G T_0 with Pi_G the gauge average. T_0 has a strictly positive kernel and commutes
with gauge transformations, so its top eigenfunction is unique, hence gauge invariant, hence it is Omega, with the
same lambda_0. On gauge-invariant functions T_0 = T and P_0 := Omega^(-1) (T_0/lambda_0) Omega = P. The kernel
e^(beta <x, w>) is positive definite (power series), so T_0 >= 0.
Put rho(dx) := e^(-V(x)) dx, phi_0 := e^(V/2) Omega, m := phi_0 rho. Then nu = phi_0^2 rho, and the one-step law is
  pi_x(dw) = e^(beta <x, w>) m(dw) / (lambda_0 phi_0(x)).
The two-slice law is J(dx, dw) = e^(beta <x, w>) m(dx) m(dw)/lambda_0, symmetric, with both marginals nu.

**(A2) The convex function Lambda.** For theta in R^N put Lambda(theta) := log of the integral of e^(<theta, w>) m(dw),
and pi_theta(dw) := e^(<theta, w> - Lambda(theta)) m(dw). Lambda is real-analytic and convex on R^N,
grad Lambda(theta) = E_(pi_theta) w, Hess Lambda(theta) = Cov_(pi_theta)(w). The eigenvalue equation reads
  lambda_0 phi_0(x) = e^(Lambda(beta x)),   so   log Omega(x) = -V(x)/2 + Lambda(beta x) - log lambda_0   on M,
and pi_x = pi_(beta x). Lambda is invariant under gauge transformations (they act on R^N by orthogonal maps and
preserve m).
Reading. Row 931's first stop was "log Omega is not known to be local". The exact statement is: log Omega is a
local term plus the restriction to M of a convex function of the ambient coordinates, whose Hessian is beta^2
times the covariance of the next slice given the present one. The non-locality of log Omega is a conditional
covariance of the local 4D measure.

**(A3) Gradient of P (row 931 (5.1) in this form).** For bounded f and a tangent vector z at x:
z . grad (P_0 f)(x) = beta Cov_(pi_x)(<z, w>, f). (The score of the family is beta w, and the mean term is free of w.)

**(A4) Renyi divergence along chords.** For theta_0, theta_1 in R^N and lambda > 1, with theta_s := theta_0 + s(theta_1 - theta_0):
  log E_(pi_(theta_0))[ (d pi_(theta_1)/d pi_(theta_0))^lambda ] = Lambda(theta_lambda) - lambda Lambda(theta_1) - (1 - lambda) Lambda(theta_0)
  = integral over [0, lambda] of k(s) Var_(pi_(theta_s))(<theta_1 - theta_0, w>) ds,
with k(s) = (lambda - 1) s on [0, 1], k(s) = lambda - s on [1, lambda]; k >= 0 and its integral is lambda(lambda - 1)/2.
Proof. The first equality is the definition of Lambda. The second is Taylor's formula with integral remainder for
s -> Lambda(theta_s) at 0, used at s = lambda and s = 1. QED
Consequence. Put kbar := sup over theta in R^N of the largest eigenvalue of Cov_(pi_theta)(w). Since the chord
|x - y| is at most the geodesic distance d(x, y) on M, row 940's bound (RD) holds for P_0 with sigma^2 = beta^2 kbar:
  (COV)_kbar  implies  E_(pi_y)[(d pi_x/d pi_y)^lambda] <= exp(lambda(lambda - 1) beta^2 kbar d(x, y)^2/2).
So in row 940's Theorem HC1, (SG-step) may be replaced by the covariance bound (COV). (Row 940's proof of
Lemma RD is not needed for this family; its Lemma H, Lemma BGL and Theorem HC1 are used as READ, unchecked.)
One Gaussian mode: kbar = 1/(beta e^omega), sigma^2 = beta e^(-omega), as in rows 931 and 940.

**(A5) Elitzur at zero field.** Cov_m(w) = (1/4) Id_N exactly (m normalised).
Proof. m is gauge invariant. For one link, a gauge transformation at one endpoint makes the law of w_l invariant
under right multiplication, so it is Haar: mean 0 and second moment (1/4) Id_4. Two distinct links of a box of
side at least 3 do not have the same endpoints; the central transformation -1 at a site that is an endpoint of
one and not of the other changes the sign of E[w_l (x) w_l']. QED
So kbar >= 1/4 for every group size and coupling, and sigma^2 >= beta^2/4 in (A4).

**(A6) Curvature of the slice law.** nu = e^(-Phi) dx with Phi = V - 2 Lambda(beta .) + const. For x in M and a
tangent vector v = (v_l):
  (Ric + Hess Phi)(v, v) = 2|v|^2 + Hess_M V(v, v)
       + 2 beta [ sum_l E_(pi_x)<w_l, x_l> |v_l|^2 - beta Var_(pi_x)(<v, w>) ],
  Hess_M V(v, v) = beta sum_l ( sum over spatial p containing l of (1/2) tr x_p ) |v_l|^2 + (terms mixing two links).
Proof. For F smooth on R^N, Hess_M(F|M)(v, v) = D^2F(v, v) - sum_l <grad_l F, x_l> |v_l|^2 (a geodesic of the unit
sphere has acceleration -|v_l|^2 x_l). Apply it to F = 2 Lambda(beta .) with (A2), and to V, which is linear in
each link variable, so that D^2 V has no diagonal block and <grad_l V, x_l> is the sum of the plaquette terms at
l. Ric = 2 on the unit S^3. QED
Check by hand: one link, V = 0. Then pi_x is von Mises-Fisher with parameter beta x, E<w, x> = A(beta) :=
I_2(beta)/I_1(beta) and the tangential variance is A(beta)/beta, so the bracket vanishes and the tensor is 2 = Ric:
nu is Haar. In one flat Gaussian mode the same formula reads Phi'' = V'' + 2 beta (1 - e^(-omega)) = 2 beta sinh(omega),
with V'' = beta (2 cosh(omega) - 2): the vacuum precision of rows 931 and 940.

**(A7) The mid-slice law.** e^(-beta|x - w|^2/2) is, up to a constant, the integral over y in R^N of
e^(-beta|x - y|^2) e^(-beta|y - w|^2). So (x, y, w) with density m(dx) e^(-beta|x - y|^2) e^(-beta|y - w|^2) m(dw) dy
(normalised) has (x, w) distributed by J; x and w are independent given y, each with law pi_(2 beta y); and y has
a law eta on R^N with
  Hess( -log (d eta/dy) )(y) = 4 beta ( Id - 2 beta Cov_(pi_(2 beta y))(w) ).
With (B g)(y) := E[g(w) | y], B maps L^2(nu) to L^2(eta) and P_0 = B^* B.
Proof. The density of eta is the square of psi(y) = integral of e^(-beta|y - w|^2) m(dw), and
Hess log psi = -2 beta + 4 beta^2 Cov(w | y); on M, |w| is constant, so the law of w given y is pi_(2 beta y).
B^* B g(x) = E[E[g(w) | y] | x] = E[g(w) | x] by the conditional independence. QED

### Step 2: fact tests, before any proof (each is a necessary condition; none is evidence for the target)

Quantifiers follow check 938. "Fails" means: the statement with the constants the seed needs is false in the rival.

- **FT-U1 (U(1), the Gaussian model FP of row 929; PROVED given that model's mode list, READ).** nu is Gaussian,
  mode by mode, with precision 2 beta sinh(omega_k). So the best constant in (LSI-vac) is alpha = 2 beta sinh(omega_min),
  the best sigma^2 is beta e^(-omega_min), and row 940's alpha' is omega_min exactly (row 940 Step 2(e)). On the box
  (24a)^3 the lowest mode has 2 sinh(omega/2) = 2 sin(pi/(24a)), so omega_min < 2 pi/(24a) < 0.27/a and
  alpha' (a - 2) < 0.27 for every a, against 16 + 3 log a. FP fails by a factor above 59 at every size. In the
  compact model the toron level gives E_1 <= 1/(2 beta b) (check 938), so alpha' (a - 2) <= 1/(48 beta) < 0.01.
  In the form of Step 4 below: the ratio alpha_c/sigma^2 = e^(2 omega_min) tends to 1. The carrier is the soft mode.
- **FT-FROZEN (Q_8, 2T).** No gradient form exists, so (LSI-vac) is not defined. (HC-vac) is defined and gives
  E_1 >= alpha'. On each fixed box E_1 tends to 0 as beta grows (degenerate flat vectors; check 938, fixed box,
  beta large enough). So no beta-uniform alpha' exists on a fixed box. This is not a statement at one finite beta
  for all boxes (check 938).
- **SMALL-BOX (conditional, as check 938 corrected it).** Premise, not proved here: for SU(2) Wilson on a fixed
  lattice box, E_1 tends to 0 as beta grows. Given the premise, alpha' <= E_1 forbids every proof whose rate does
  not depend on beta at fixed lattice size. So each input below must degrade as beta grows at fixed size. For
  Theorem C of Step 4 this reads: alpha_c/sigma^2 tends to 1. GUIDE (recalled lattice values, no proof weight): at
  beta 2.3 the box (a; (24a)^3) is deconfined for a <= 4, so a proof at beta 2.3 must fail for a <= 4, and the
  true seed size is near a = 20.
- **FT-CEIL.** The ceilings 1/3, 2/3, 0.775, 4 G_3 are caps on named sup-type criteria (check 938 Section 4).
  A hypothesis of this file that is a supremum over a conditioning slice is of that kind and is marked "sup form"
  where it occurs: (COV) in (A4), and (C1), (C2) in Step 4. No cited ceiling refutes them. None of them is proved.
- **New method ceilings in the time direction (PROVED here; they cap methods, they refute no target).**
  (i) Pointwise Bakry-Emery for nu fails for every beta > 1 on every box. Take x = 1 on all links except one
  link l_0 with x = -1, and v supported on l_0. The four spatial plaquettes at l_0 equal -1, so by (A6)
  (Ric + Hess Phi)(v, v) <= (2 - 4 beta + 2 beta)|v|^2 = (2 - 2 beta)|v|^2.
  (ii) The mid-slice law eta is not log-concave for beta > 2: at y = 0, (A5) and (A7) give
  Hess(-log eta) = 4 beta (1 - beta/2) Id. For U(1) the same computation gives 4 beta (1 - beta) Id.
  (iii) A log-Sobolev constant above 2 beta for the slice given both time neighbours (the Otto-Reznikoff form in the
  time direction, RECALLED) is impossible for beta >= 3/2: if the neighbours are antipodal on a link, the field on
  it vanishes, and the linear test function gives a Poincare constant at most 3 there (variance 1/4, gradient 3/4).
  All three caps lie below the window 2.3 to 2.6, and all three come from one link whose time neighbours do not
  pin it. They are group-blind: for U(1) the same three computations give the caps 0, 1 and 1/2.

### Step 3: attack A, curvature of a slice law (Bakry-Emery). Result: dead below the window, for a named reason

Aim. A positive lower bound on the tensor of (A6) for nu, or on the Hessian of (A7) for eta, would give a
log-Sobolev inequality at once (Bakry and Emery, RECALLED). Both tensors are now in closed form, so the attack
can be judged exactly.

**A.1 The slice law nu.** By (A6) the tensor is 2 + Hess_M V + 2 beta [mean temporal plaquette - beta times the
one-step variance]. The bracket is exactly zero for independent links and it is the only place where the 4D
dynamics enters. The term Hess_M V is the obstruction: it is -4 beta on a link whose four spatial plaquettes are
-1. Death: Step 2 (i), every beta > 1.

**A.2 The mid-slice law eta (Theorem MID; CONDITIONAL on the flat-space form of row 940's Lemma BGL, which is
Bobkov-Gentil-Ledoux's own setting, RECALLED; not rebuilt, because the hypothesis is refuted below).**
Put chi_mid := 2 beta sup over y in R^N of the largest eigenvalue of Cov_(pi_(2 beta y))(w). If chi_mid < 1, then:
(a) eta satisfies a log-Sobolev inequality with constant 4 beta (1 - chi_mid) (by (A7) and Bakry-Emery on R^N);
(b) the half-step operator B obeys row 940's Harnack inequality with sigma'^2 = 2 beta chi_mid (by (A4) with
    theta = 2 beta y);
(c) so B is a contraction from L^p(nu) to L^Q(eta) with Q - 1 = (p - 1)(2 - chi_mid)/chi_mid, B^* has the same
    gain by duality, and P = B^* B satisfies (HC-vac) with alpha' = log((2 - chi_mid)/chi_mid).
Check by hand, one Gaussian mode. The law of w given y has precision beta (e^omega + 1), so chi_mid =
2/(e^omega + 1), eta has precision 4 beta tanh(omega/2) = 4 beta (1 - chi_mid), and (2 - chi_mid)/chi_mid = e^omega:
alpha' = omega, Nelson's exponent. The attack is sharp where it applies.
No term Hess V occurs here: the mid-slice variable lives in flat space, and the spatial action enters only
through the conditional covariance. This is the gain over A.1.
Death (PROVED): Step 2 (ii). At y = 0 the links are free and Cov = Id/4 by Elitzur's argument (A5), so
chi_mid >= beta/2. The hypothesis fails for every beta >= 2, on every box, for SU(2). (For one free link,
chi_mid = beta/2 exactly, and Theorem MID is a true statement about the rotor chain for beta < 2.)

**A.3 What attack A leaves.** A curvature criterion in the time direction cannot reach beta 2.3: the cap is a
single link that its time neighbours fail to pin, and it is the same for U(1). The useful output is the
closed form (A6), (A7): every curvature-type quantity of a slice law is a conditional covariance of the next
slice in a linear external field. What must be shown about SU(2) is therefore a bound on such covariances.

### Step 4: attack B, from the one-step conditional laws to the vacuum (Theorem C, Proposition W; PROVED implications)

Idea. Do not ask for an inequality for nu. Ask for inequalities for the one-step laws pi_x, and let stationarity
carry them to nu. No curvature is used, and Lambda enters only through pi_x.

Definitions (sup form: each is a supremum over the conditioning slice x in M). A tangent vector at x is
horizontal if it is orthogonal to the gauge orbit through x.
  (C1)_(alpha_c): Ent_(pi_x)(h) <= E_(pi_x)[ |grad h|^2/h ]/(2 alpha_c) for every x and every smooth positive
     gauge-invariant h.
  (C2)_sigma: for every x and every unit horizontal z at x, beta (<z, w> - E_(pi_x)<z, w>) is sub-Gaussian under pi_x
     with variance proxy sigma^2.
  gamma_c: Var_(pi_x)(f) <= E_(pi_x)|grad f|^2/gamma_c for every x and smooth gauge-invariant f.
  kbar_h: Var_(pi_x)(<z, w>) <= kbar_h for every x and every unit horizontal z at x.
(C1) gives gamma_c >= alpha_c (linearise), and (C2) gives beta^2 kbar_h <= sigma^2.

**Proposition W (variance level).** Put kappa_W := beta (kbar_h/gamma_c)^(1/2). Then for smooth gauge-invariant f:
  |grad P f|^2 <= kappa_W^2 P(|grad f|^2)   pointwise.
If kappa_W < 1: every eigenvalue r of P on non-constant gauge-invariant functions has |r| <= kappa_W, so
E_1 >= log(1/kappa_W); and nu has the Poincare constant gamma >= gamma_c (1 - kappa_W^2).
Proof. P f is gauge invariant, so grad P f(x) is horizontal. By (A3) and Cauchy-Schwarz, for unit horizontal z:
z . grad P f(x) = beta Cov_(pi_x)(<z, w>, f) <= beta (kbar_h Var_(pi_x) f)^(1/2) <= kappa_W (E_(pi_x)|grad f|^2)^(1/2).
If P f = r f with f not constant (f = P f/r is smooth), integrate against nu and use stationarity:
r^2 E_nu|grad f|^2 <= kappa_W^2 E_nu|grad f|^2. For the Poincare constant: Var_nu(f) = sum over k < n of
E_nu Var_(pi_x)(P^k f) + Var_nu(P^n f) (row 931 (5.2), iterated), each term is at most
kappa_W^(2k) E_nu|grad f|^2/gamma_c, and Var_nu(P^n f) tends to 0 (the kernel is bounded below on M x M). QED

**Theorem C (entropy level).** Assume (C1)_(alpha_c) and (C2)_sigma with sigma^2 < alpha_c. Then
  (LSI-vac)_alpha holds with alpha = alpha_c - sigma^2.
Proof. Let g_0 >= delta > 0 be smooth and gauge invariant, g_k := P^k g_0, F_k := |grad g_k|^2/g_k, I_k := E_nu F_k.
(i) Chain rule with stationarity: Ent_nu(g) = E_nu[Ent_(pi_x)(g)] + Ent_nu(P g). So
Ent_nu(g_0) = sum over k < n of E_nu[Ent_(pi_x)(g_k)] + Ent_nu(g_n).
(ii) By (C1) and stationarity, E_nu[Ent_(pi_x)(g_k)] <= E_nu E_(pi_x)[F_k]/(2 alpha_c) = I_k/(2 alpha_c).
(iii) Let z be the unit vector along grad g_(k+1)(x); it is horizontal. By (A3) and Lemma SGC (row 940; it is
row 931's Theorem E step (ii), which HOLDS in check 938): |grad g_(k+1)(x)|^2 = beta^2 Cov_(pi_x)(<z, w>, g_k)^2
<= 2 sigma^2 g_(k+1)(x) Ent_(pi_x)(g_k) <= (sigma^2/alpha_c) g_(k+1)(x) E_(pi_x)[F_k]. Divide by g_(k+1)(x) and
integrate: I_(k+1) <= (sigma^2/alpha_c) I_k.
(iv) g_n tends to E_nu g_0 uniformly (the kernel is bounded below), so Ent_nu(g_n) tends to 0. Sum the series:
Ent_nu(g_0) <= I_0/(2 (alpha_c - sigma^2)). Let delta tend to 0. QED

**Corollary C' (CONDITIONAL on row 940's Theorem HC1, READ, unchecked).** If (C2) holds for every unit tangent z
(not only horizontal ones), then with (A4) or with row 940's Lemma RD, Theorem HC1 gives (HC-vac) with
  alpha' = (1/2) log(1 + (alpha_c - sigma^2)/sigma^2) = (1/2) log(alpha_c/sigma^2).
If (C1) holds for all smooth functions, Herbst's argument (RECALLED) gives sigma^2 <= beta^2/alpha_c, and then
alpha' >= log(alpha_c/beta). (ARGUED, not written out: horizontal z suffice in HC1 for gauge-invariant functions,
because the Hopf-Lax minimiser can be taken at the nearest point of its gauge orbit, and the geodesic to it is
horizontal.)

**Checks by hand.**
- One Gaussian mode: pi_q is Gaussian with precision beta e^omega, so alpha_c = gamma_c = beta e^omega, kbar =
  1/(beta e^omega), sigma^2 = beta e^(-omega). Proposition W: kappa_W = e^(-omega) = r_1 and gamma = 2 beta sinh(omega).
  Theorem C: alpha = beta e^omega - beta e^(-omega) = 2 beta sinh(omega). Corollary C': alpha' = omega. All three are
  the exact values. So Theorem C is the vacuum log-Sobolev inequality of the free field, with the exact constant,
  derived from the one-step law alone.
- One free SU(2) link (V = 0; nu is Haar; r_1 = A(beta) := I_2(beta)/I_1(beta)). pi_x is von Mises-Fisher and
  kbar_h = A(beta)/beta. Proposition W asserts A^2 <= kappa_W^2 = beta A/gamma_c, that is gamma_c <= beta I_1/I_2 =
  4 + beta I_3/I_2 (recurrence I_1 - I_3 = (4/beta) I_2). Independent bound: a coordinate y orthogonal to x has
  -L y = (3 + beta <x, w>) y, so gamma_c <= 3 + beta I_3/I_2. Consistent at every beta, with margin exactly 1.
  Corollary C' asserts alpha_c/sigma^2 <= e^(2 E_1) = (I_1/I_2)^2. With alpha_c <= gamma_c and sigma^2 >= beta A(beta)
  the left side is at most (3 + beta I_3/I_2)/(beta I_2/I_1): 3.80/1.10 = 3.45 at beta 2.3 against 4.36; for large
  beta the sides are 1 + 2/beta and 1 + 3/beta; for small beta, 12/beta^2 and 16/beta^2. No contradiction.
  (Bessel values at 2.3 by the recurrence from I_0 = 2.8296, I_1 = 2.0978: I_2 = 1.0054, I_3 = 0.3493.)

**What attack B achieves.** The pair (LSI-vac), (SG-step) of rows 931 and 940 is replaced by statements about
one object, the law of the next slice given the present one:
  (C1)_(alpha_c) and (C2)_sigma with sigma^2 < alpha_c   give   (LSI-vac), (HC-vac) with alpha' = (1/2) log(alpha_c/sigma^2),
  kappa_W < 1   gives   E_1 >= log(1/kappa_W)   (gap only).
The threshold is strict and exact: the conditional law must relax faster than the temporal coupling feeds in
(sigma^2 is beta e^(-omega) for a free mode). This is where a mass enters: alpha_c/sigma^2 = e^(2 omega).
The box does not occur in Theorem C; it enters only through Proposition HC.
