lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T18:47Z

# gap-sgstep-opus (queue row 944): the one-step sub-Gaussian score (SG-step) for the SU(2) Wilson slice chain

Started 2026-11-14T06:47Z on the Mac mini worker, Claude Opus 5.5 at max effort, as AUTHOR. Pinned at commit
a90db3999 on branch claude/ym4d-hard-route. Research-stage working state; no status is granted by this file.
Labels: PROVED, CONDITIONAL (on named inputs), GUIDE (a run or a heuristic; refutes or guides only), OPEN.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Inputs. Read `library/gap-direction-max.md` Steps 5-7, `library/gap-etohc-opus.md` (definition of (SG-step),
   Corollary HC2) and `library/gap-etohc-check-astra.md` (the SGC correction). Record the exact statement of
   (SG-step)_sigma, the slice chain, pi_u, the score, and which form (supremum over u, averaged, normalized z)
   Proposition HC and (E-to-HC) really consume. Duplicate check: grep `library/open-core.md` and the FINISH rows.
2. Structure of the score. Write phi_(u,z) explicitly for the Wilson slice chain on (24a)^3: a sum over the links
   of the slice of bounded one-link forces, coupled through the spatial plaquettes of the next slice. Fact test on
   the free photon (sigma^2 = beta e^(-omega) at most beta per mode).
3. Key question. Is sigma necessarily volume-free? Decide whether sub-Gaussianity at a volume-free sigma follows
   from compactness and the one-link bound alone (Hoeffding type plus a decoupling or martingale argument), or
   fails; if it fails, give the volume growth and say whether a normalized z or the averaged form repairs it.
4. Attack. Prove the strongest form reachable (supremum form, or the averaged form, or the pair of Corollary HC2),
   with sigma explicit; or isolate the exact missing input.
5. Fact tests. U(1) and the frozen groups: (SG-step) is group-blind, so it must hold for them and must not imply a
   gap on its own.
6. GUIDE run if memory allows (one job, machine lock): sample the score on a small box to test the constants.
7. Literature and credit: Sussman-Alpoge account and library on the Mini, and any published inequality used.
8. Verdicts, what stays open, RESULT line.

## 1. Inputs and the exact statement (step 1; READ at a90db3999)

Read: FINISH.md (opening, How we work, row 944), GOAL.md, `library/gap-direction-max.md` Steps 5-7 (row 931),
`library/gap-etohc-opus.md` in full (row 940), `library/gap-etohc-check-astra.md` (check 942: main implication,
seed consumer, fact tests, disposition), `library/gap-lsivac-max.md` Step 0 (row 941, in progress).

**Duplicate check (rule 0a).** `grep -i -E "SG-step|sub-?Gaussian|SG~|score"` on `library/open-core.md` and
`library/l17c.md`: no hit. FINISH rows with "SG-step": 931 (names it), 940 (uses it as a hypothesis), 942 (check
of 940), 944 (this row), 945 (check of this row). Row 941's file (line 52) names "the pair (LSI-vac), (SG-step)"
as its target, but its revised plan attacks (LSI-vac) only (Bakry-Emery for nu, averaged forms through Gaussian
domination, box-size dependence), and row 944 says "(LSI-vac) is under attack by row 941". So (SG-step) is this
row's. I stay off (LSI-vac) and off the weighted log-Sobolev inequality of Corollary HC2 (an LSI for nu, row 941's
object), off (E-to-HC) (row 940, done), and off (CUT-TYP), (VAC-SUB).

**Setting (row 931 Step 5, row 940 Step 1; notation fixed here).** B = periodic spatial box with |B| = (24a)^3
sites; N := 3|B| spatial links. M := SU(2)^N, each factor the unit sphere S^3 in R^4 = quaternions, with the
round metric; <x, y> is the Euclidean product in R^4, so (1/2) tr(x y^*) = <x, y> on SU(2). For u, w in M:
- V(u) := beta * sum over spatial plaquettes p of (1 - (1/2) tr U_p(u)) (the magnetic term of one slice);
- k(u, w) := prod over links l of exp(beta <u_l, w_l>) (temporal plaquettes in temporal gauge; the constant
  e^(-beta N) is dropped, it only rescales T);
- K(u, w) := integral of k(u, g.w) dg over g in SU(2)^|B| (Haar), (g.w)_l = g_x w_l g_(x+l)^* (gauge average);
- T(u, w) := e^(-V(u)/2) K(u, w) e^(-V(w)/2); Omega > 0 its ground state, lambda_0 its top eigenvalue;
- nu := Omega^2 dU, p(u, w) := T(u, w)/(lambda_0 Omega(u) Omega(w)), pi_u := p(u, .) nu.
Gauge transformations act on M by isometries; V, K, T, Omega, p are gauge invariant in each argument.

**(SG-step)_sigma (row 931 Step 6; row 940 Step 1).** For every u in M and every unit z in T_u M, the score
phi_(u,z)(w) := d_u log p(u, w)[z] satisfies E_(pi_u) exp(lambda phi_(u,z)) <= exp(lambda^2 sigma^2/2) for all real
lambda. (Row 931 writes "almost every u". Check 942: with a positive continuous density of full support, a.e.
and every are the same here.) E_(pi_u) phi_(u,z) = 0, since the integral of p(u, .) d nu is 1.
Local proxy: sigma(u, z)^2 := sup over lambda != 0 of 2 log E_(pi_u) e^(lambda phi_(u,z)) / lambda^2, and
sigma(u)^2 := sup over unit z. Then (SG-step)_sigma means sup_u sigma(u)^2 <= sigma^2.

**What consumes it, exactly.**
- (E-to-HC) (row 940; HOLDS AFTER CORRECTION, check 942): (LSI-vac)_alpha + (SG-step)_sigma give
  ||P g||_Q <= ||g||_p with Q - 1 = (p - 1)(1 + alpha/sigma^2), hence (HC-vac) with alpha' = (1/2) log(1 + alpha/sigma^2).
  It uses the SUPREMUM form: Lemma RD integrates (SG-step) along a whole geodesic between any two slices (row 940
  Step 3 Remark (iv); check 942 item 2: "A merely averaged score bound does not enter this argument").
- Corollary HC2 (HOLDS conditionally, check 942 item 7): any smooth gauge-invariant metric g~ with
  log E_(pi_x) exp(d_x log p(x, .)[v]) <= |v|_(g~)^2/2 for all x, v, plus Ent_nu(f^2) <= (2/kappa) E_nu |grad f|_(g~)^2,
  gives alpha' = (1/2) log(1 + kappa). With g~ = s(x)^2 g, s a smooth gauge-invariant envelope of sigma(x), only a
  pointwise envelope is needed, and the cost moves into a weighted LSI for nu.
- Proposition HC (row 931, HOLDS for integer times, check 938) consumes only (HC-vac). The seed needs
  alpha' (a - 2) >= log(72 beta 24^3/x_*) + 3 log a, with x_* = log(22/17) (thermal threshold) or x_* = log(20/19)
  (both clauses of Form W) (check 942, "Kernel and seed consumer").
- So sigma enters only through alpha/sigma^2. If sigma^2 grows like the number of links, sigma^2 >= c N =
  3c (24a)^3, then alpha' <= alpha/(2 sigma^2) is of order a^(-3) for box-free alpha, and alpha' (a - 2) -> 0: the
  seed condition fails at every a. **A box-free sigma (more exactly: sigma^2 <= C alpha with C box-free) is
  necessary for this route.**

**Already PROVED (row 931 Step 7, row 940 Step 2(a)).** In the free photon (one Gaussian mode of frequency
omega) phi is exactly N(0, beta e^(-omega)), so sigma^2 = beta e^(-omega) <= beta on every mode.

**Plan, refined after the reading (steps 2-8 of Section 0 stay; their content is now):**
2. Exact structure: (TG) the projected score is a conditional expectation of a LINEAR statistic of the
   temporal-gauge next slice; (EF) that law is an exponential family whose log-partition function, on M, is
   log Omega + V/2 + log lambda_0; (HO) the Hoeffding bound from compactness; the photon test.
3. Key question: volume growth from compactness alone; an abstract counterexample; normalized z; averaged form.
4. Attack: reduce (SG-step) at a box-free sigma to one inequality on Omega (uniform semiconcavity of log Omega),
   prove the reduction, and test that inequality.
5. Fact tests: free photon, compact U(1), frozen groups, SMALL-BOX. 6. GUIDE run (if memory allows).
7. Literature and the Sussman-Alpoge account. 8. Result.

## 2. Exact structure of the score (step 2; all PROVED by hand, by Claude, not yet checked)

**Lemma TG (temporal-gauge reduction).** For u in M put R(w) := e^(-V(w)/2) Omega(w) and
  pi~_u(dw') := e^(-V(u)/2) k(u, w') R(w') dw' / (lambda_0 Omega(u))      (dw' = product Haar measure on M).
For z in T_u M put psi_(u,z)(w') := beta <z, w'> - E_(pi~_u)[beta <z, w'>] (z_l is a vector of R^4 orthogonal to
u_l). Then pi~_u is a probability measure, and for every convex Phi: R -> R,
  E_(pi_u) Phi(phi_(u,z)) <= E_(pi~_u) Phi(psi_(u,z)).
In particular sigma(u, z)^2 <= sigma~(u, z)^2 := the sub-Gaussian proxy of psi_(u,z) under pi~_u.
Proof. Let G = SU(2)^|B| with Haar measure dg, and put on G x M
  rho_u(dg, dw) := e^(-V(u)/2) k(u, g.w) e^(-V(w)/2) Omega(w) dg dw / (lambda_0 Omega(u)).
The integral over g of k(u, g.w) is K(u, w), so the w-marginal of rho_u is T(u, w) Omega(w) dw/(lambda_0 Omega(u)),
which is pi_u (nu = Omega^2 dU). Its mass is 1 by T Omega = lambda_0 Omega. Map (g, w) -> (g, w' := g.w). For
fixed g this map preserves dw (left and right Haar invariance on each link), and V, Omega are gauge invariant.
So the image of rho_u is dg x pi~_u(dw'): under rho_u, w' has law pi~_u (and g is Haar, independent of w').
Next, log p(u, w) = -V(u)/2 + log K(u, w) - log Omega(u) + (terms free of u). Differentiate under the integral (k is
smooth, G is compact): d_u log K(u, w)[z] = E_(rho_u)[ d_u log k(u, g.w)[z] | w ], because the conditional law of g
given w under rho_u is k(u, g.w) dg / K(u, w). And d_u log k(u, w')[z] = beta sum_l <z_l, w'_l>: the differential of
the restriction of the linear map u_l -> <u_l, w'_l> is that linear map on the tangent vector. Hence
phi_(u,z)(w) = E_(rho_u)[ beta <z, w'> | w ] + c, with c free of w. As E_(pi_u) phi_(u,z) = 0, c = -E_(pi~_u) beta <z, w'>.
So phi_(u,z) = E_(rho_u)[ psi_(u,z) | w ], and conditional Jensen gives Phi(phi) <= E[Phi(psi) | w]. Integrate. QED
Reading. pi~_u is the law of the next slice in temporal gauge, the gauge being fixed by the boundary slice u.
Write w'_l = h_l u_l and z_l = xi_l u_l with xi_l purely imaginary (z_l orthogonal to u_l). Right multiplication
by u_l is an isometry of R^4, so <z_l, w'_l> = <xi_l, h_l> = <xi_l, E_l>, E_l := Im h_l in R^3, |E_l| <= 1. So the
statistic is beta sum_l <xi_l, E_l>: a linear functional of the colour-electric field of the first time step,
with |z|^2 = sum_l |xi_l|^2. For z tangent to the gauge orbit of u, phi_(u,z) = 0 (p is gauge invariant in u);
only horizontal z carry content.

**Lemma EF (exponential family).** For y in R^(4N) put A(y) := log of the integral over M of e^(beta <y, w'>) R(w') dw',
and mu_y(dw') := e^(beta <y, w'> - A(y)) R(w') dw'.
(i) A is finite, smooth and convex on R^(4N); grad A(y) = beta E_(mu_y) w', Hess A(y) = beta^2 Cov_(mu_y)(w').
(ii) For u in M: mu_u = pi~_u and A(u) = log lambda_0 + log Omega(u) + V(u)/2.
(iii) For u in M, z in T_u M and real lambda: log E_(pi~_u) e^(lambda psi_(u,z)) = A(u + lambda z) - A(u) - lambda <grad A(u), z>.
Proof. (i) Differentiation under the integral over a compact set; a covariance matrix is positive semidefinite.
(ii) The density of pi~_u is e^(beta <u, w'>) R(w') e^(-V(u)/2)/(lambda_0 Omega(u)) and its mass is 1.
(iii) E_(pi~_u) e^(lambda beta <z, w'>) = e^(A(u + lambda z) - A(u)) by (ii); the mean of beta <z, w'> is <grad A(u), z>. QED
Consequences. With F := log Omega + V/2 = A|_M - log lambda_0 (the log-partition function on M):
  beta^2 Var_(pi~_u)(<z, w'>) = Hess A(u)(z, z) <= sigma~(u, z)^2 <= beta^2 sup over t in R of Var_(mu_(u + t z))(<z, w'>)   (2.1)
(left: lambda -> 0 in (iii); right: Taylor's formula with integral remainder, A(u + lambda z) - A(u) - lambda <grad A, z>
= integral over [0, lambda] of (lambda - t) Hess A(u + t z)(z, z) dt).

**Identity HV (variance = Hessian of log Omega, up to beta).** For u in M and z in T_u M (Hess_M the Riemannian
Hessian of M):
  beta^2 Var_(pi~_u)(<z, w'>) = Hess_M F(u)(z, z) + beta sum_l E_(pi~_u)[<u_l, w'_l>] |z_l|^2,  F = log Omega + V/2.   (2.2)
Hence |beta^2 Var_(pi~_u)(<z, w'>) - Hess_M F(u)(z, z)| <= beta |z|^2.
Proof. For the geodesic c_l(t) = cos(t|z_l|) u_l + sin(t|z_l|) z_l/|z_l| of each sphere, c''(0) = -(|z_l|^2 u_l)_l. So
Hess_M(A|_M)(u)(z, z) = (d/dt)^2 A(c(t)) at 0 = Hess A(u)(z, z) - sum_l <grad_l A(u), u_l> |z_l|^2, and
<grad_l A(u), u_l> = beta E_(pi~_u) <w'_l, u_l> by Lemma EF (i), (ii). Use F = A|_M - log lambda_0 and (i). QED
Reading. Up to beta |z|^2, the score variance in temporal gauge IS the Hessian of log Omega + V/2. The Hessian of V
is local: |Hess V(u)(z, z)| <= c_V beta |z|^2 with c_V box-free (each plaquette term has a bounded Hessian, each
link meets 4 spatial plaquettes; c_V is fixed in Section 4). So, at the variance level, a box-free sigma in
temporal gauge is the same as a box-free upper bound on Hess_M log Omega.

**Lemma HO (Hoeffding: what compactness and the one-link bound give).** For u in M and z in T_u M:
  sigma(u, z)^2 <= sigma~(u, z)^2 <= beta^2 ||z||_1^2,   ||z||_1 := sum_l |z_l|.
So sigma(u, z)^2 <= beta^2 N_z |z|^2 (N_z = number of links where z_l != 0), and sigma(u)^2 <= beta^2 N.
Proof. On M, |<z_l, w'_l>| <= |z_l|, so beta <z, w'> lies in an interval of length D = 2 beta ||z||_1. Hoeffding's
lemma: a centred X with values in an interval of length D has L(lambda) := log E e^(lambda X) <= lambda^2 D^2/8 (L(0) =
L'(0) = 0, and L''(lambda) is the variance of X under the tilted law, at most D^2/4 for a variable in that interval).
So sigma~^2 <= D^2/4. Then Lemma TG, and Cauchy-Schwarz ||z||_1^2 <= N_z |z|^2. QED
Reading. The one-link force is bounded: |grad_(u_l) log k(u, w')| <= beta. For z on few links this is box-free.
For a spread unit z (|z_l| = N^(-1/2) on all links) it is beta^2 N = 3 beta^2 (24a)^3: volume growth.

**Free photon (fact test, PROVED).** One Gaussian mode: k(q, q') = e^(-beta (q - q')^2/2) has the linear term
beta q q', and the rest is Gaussian. Then A(y) is quadratic, Hess A = beta^2 Var(q') is constant, and (2.1) is an
equality: sigma^2 = beta^2 v = beta e^(-omega) with v = 1/(beta e^omega) (row 940 Step 2). Lemma TG is an
equality (no gauge average in one mode). Consistent with row 931.

## 3. Key question: is sigma necessarily box-free? (step 3)

**Answer.** No. Compactness and the one-link bound give exactly Lemma HO, sigma(u, z)^2 <= beta^2 ||z||_1^2, which is
beta^2 N for a spread unit z. Example DW below shows that nothing better follows from them, even with every
structural hypothesis of row 940 (positive smooth symmetric kernel, reversible, stationary, the exponential-family
form of Lemma EF with the same one-link force). A box-free sigma for the Wilson chain needs a property of the
coupling R = e^(-V/2) Omega (Section 4 names it exactly). A constant renormalization of z does not repair this
(Proposition CONS), and the averaged form is not what (E-to-HC) consumes.

**Lemma RS (every R is realized by a reversible slice chain; PROVED).** Let M = (S^3)^N, beta > 0, and R > 0
smooth on M. Put (kR)(u) := integral of e^(beta <u, w>) R(w) dw, S := (R/kR)^(1/2), T(u, w) := S(u) e^(beta <u, w>) S(w).
Then T is symmetric, positive and smooth; Omega := S kR is a positive eigenfunction, T Omega = Omega (so it is
the ground state, lambda_0 = 1, by Perron-Frobenius for a positive kernel), and the slice chain of row 940 has
pi_u(dw) = e^(beta <u, w>) R(w) dw/(kR)(u).
Proof. (T Omega)(u) = S(u) integral of e^(beta <u, w>) S(w)^2 (kR)(w) dw = S(u) (kR)(u) = Omega(u), since S^2 kR = R.
pi_u(dw) = T(u, w) Omega(w) dw/Omega(u) = e^(beta <u, w>) S(w) Omega(w) dw/(kR)(u), and S Omega = S^2 kR = R. QED
So the structure "score = beta <z, w'> - mean, under e^(beta <u, w'>) R(w') dw'" holds for every R; the box-free
question is a question about R alone.

**Example DW (double well; PROVED).** Take a, b in M with <a_l, b_l> = 0 for all l (for instance a_l = 1,
b_l = i), and R_eps(w) := exp(-|w - a|^2/eps) + exp(-|w - b|^2/eps) (Euclidean norm of R^(4N)); build the chain by
Lemma RS. Let u_l := (a_l + b_l)/sqrt 2 and z_l := (a_l - b_l)/sqrt(2N). Then z is a unit tangent vector at u, and
  Var_(pi_u)(phi_(u,z)) = beta^2 Var_(pi_u)(<z, w>) >= beta^2 c_eps^2 N/2,
  c_eps := A_4(r) (2/eps)/r,  r := |beta u_l + (2/eps) a_l| = (beta^2 + 4/eps^2 + 2 sqrt2 beta/eps)^(1/2),
A_4(r) = I_2(r)/I_1(r) the mean length of the von Mises-Fisher law on S^3 (density proportional to e^(<kappa, w>),
|kappa| = r). c_eps does not depend on N and tends to 1 as eps -> 0. Hence sup_u sigma(u)^2 >= beta^2 c_eps^2 N/2,
against the upper bound beta^2 N of Lemma HO: Lemma HO is sharp up to the factor 2 c_eps^(-2).
Proof. |w - a|^2 = 2N - 2 <w, a> on M, so each term of R_eps is a product of von Mises-Fisher densities, and
pi_u is proportional to Q_a + Q_b with Q_a := prod_l e^(<beta u_l + (2/eps) a_l, w_l>) (same for b). The reflection
of each R^4 in the hyperplane orthogonal to a_l - b_l fixes u_l and swaps a_l, b_l; it is an isometry of S^3, so
Q_a and Q_b have the same mass and pi_u = (Q_a + Q_b)/2 after normalization. Under the normalized Q_a the links are
independent and E <z_l, w_l> = A_4(r) <z_l, beta u_l + (2/eps) a_l>/r = A_4(r) (2/eps)/(r sqrt(2N)) (as <z_l, u_l> = 0,
<z_l, a_l> = 1/sqrt(2N)); under Q_b it is the negative. A mixture with weights 1/2 of two laws with means +m and -m
has variance at least m^2; here m = N A_4(r)(2/eps)/(r sqrt(2N)) = c_eps sqrt(N/2). No gauge average: phi = psi. QED
Number: eps = 1/beta, beta = 2.3 gives r = 2.80 beta = 6.44, A_4(6.44) about 0.77 (A_4(r) ~ 1 - 3/(2r)), c_eps about
0.55, so sigma(u)^2 >= 0.15 beta^2 N.
Mechanism. Two macroscopically different "phases" of the next slice with equal weight at u: the score in the
direction that separates them is of size beta sqrt(N). Any R with a phase coexistence of this kind (a local R
included, e.g. an Ising-like anisotropy in d >= 2 under a symmetric field; ARGUED, Peierls) gives volume growth.

**Decoupling and martingales (what they give; ARGUED, not used).** Order the links and write psi as a sum of Doob
martingale differences D_l under pi~_u. Azuma-Hoeffding gives sigma~^2 <= sum_l ||D_l||_inf^2, and
||D_l||_inf <= beta |z_l| + beta sum over l' after l of |z_l'| c_(l'l), where c_(l'l) bounds the influence (total
variation) of w'_l on the conditional law of w'_l'. If the influence matrix C has ||C||_(2->2) <= theta < 1 uniformly
in u, then sigma~^2 <= beta^2/(1 - theta)^2: box-free. This is a Dobrushin-type weak-dependence hypothesis on the
half-space Wilson measure, uniform in the boundary slice. It holds only at small beta (the conditional law of one
link depends on 6 plaquettes of coupling beta; Dobrushin's sum is of order 18 beta), not at beta 2.3-2.6.
pi~_u is not even a local Gibbs measure on the slice (Omega is non-local), so the influences must be taken in the
half-space system. Example DW is the case theta >= 1.

**Proposition CONS (renormalizing z does not repair; PROVED).** (i) Constant rescaling. In Corollary HC2 take
g~ = c g. (SG~) holds iff c >= sigma^2, and the LSI constant of nu in g~ is kappa = alpha/c. So the rate
(1/2) log(1 + kappa) is at best (1/2) log(1 + alpha/sigma^2): a box factor in sigma^2 moves into kappa unchanged.
(ii) l1-normalization. Lemma HO is box-free in the l1 norm: log E e^(lambda phi_(u,z)) <= lambda^2 beta^2 ||z||_1^2/2. Lemmas
SGC, RD, H of row 940 hold for the l1 path distance d_1 (their proofs use (SG-step) only along a curve, with the
proxy times the squared speed). But Lemma BGL in d_1 needs the dual-norm inequality
Ent_nu(f^2) <= (2/alpha_inf) E_nu (max_l |grad_l f|)^2, and alpha_inf carries the box factor: already for nu = a product of
N copies of one law rho on S^3 (the best case), the test f = sum_l c(u_l) with |grad c| <= 1 and Var_rho(c) = v > 0
gives, through the Poincare inequality implied by that LSI, N v <= 1/alpha_inf, so alpha_inf <= 1/(N v). (For the
Wilson nu the same test with f = sum over plaquettes of (1/2) tr U_p gives alpha_inf <= 16/Var_nu(f); the action
variance is extensive whenever the specific heat is positive: ARGUED.) A Riemannian g~ that dominates the l1 bound
is no better: a quadratic form Q on T_u M with Q(z) >= ||z||_1^2 for all z satisfies, averaging over sign changes
of the link components of a spread z, trace Q >= N^2 on a space of dimension 3N, so the mean eigenvalue of Q is at
least N/3 (PROVED); that this moves the box factor into kappa as in (i) is ARGUED.

**Averaged form (PROVED as a reading; the alternative is OPEN).** Lemma RD needs (SG-step) at every point of the
geodesic between the two slices it compares, and Lemma H and Theorem HC1 apply it to all pairs (x, y), y the
Hopf-Lax minimizer for x. A bound on E_nu sigma(u)^2 does not enter. Geodesics between nu-typical slices pass
through slices that are not typical (the per-link midpoint of two independent typical slices has a smaller mean
plaquette), so even a supremum over a typical set does not feed Lemma RD. Row 931's Theorems V and E do hold in
averaged forms (row 931 Step 7), but they give a gap and an entropy contraction, not the count. An implication
(LSI-vac) + averaged (SG-step) => (HC-vac) would need a new argument: OPEN, not attempted here.

**What remains for the Wilson chain.** Whether sup_u sigma(u)^2 is box-free is not decided by compactness. It is
decided by whether the half-space Wilson measure with boundary slice u can show a coexistence of macroscopically
different next slices. Section 4 makes this exact: a box-free sigma follows from, and at the variance level in
temporal gauge is equivalent to, a box-free upper bound on the Hessian of log Omega.

## 4. Attack: the Hessian route, and the one open inequality (step 4)

**Lemma HSS (lower Hessian bound gives the score bound; PROVED).** Suppose that for some H >= 0 and all u, w in M,
Hess_u log p(u, w) >= -H g (Riemannian Hessian in the first argument). Then (SG-step)_sigma holds with sigma^2 = H.
Proof. Fix u, a unit z in T_u M and real t; let u(s) = exp_u(s z), a unit-speed geodesic (M is complete). Taylor's
formula along it: log p(u(t), w) = log p(u, w) + t phi_(u,z)(w) + integral over [0, t] of (t - s) Hess_u log p(u(s), w)(u', u') ds
>= log p(u, w) + t phi_(u,z)(w) - H t^2/2. So e^(t phi_(u,z)(w)) <= e^(H t^2/2) p(u(t), w)/p(u, w). Multiply by p(u, w),
integrate in nu(dw), and use that the integral of p(v, .) d nu is 1 for every v: E_(pi_u) e^(t phi_(u,z)) <= e^(H t^2/2). QED
(This is the converse direction of row 940's Lemma RD: there the score bound gives a Renyi bound; here a
one-sided Hessian bound gives the score bound. Herbst-type; no box enters.)

**Theorem SC (the reduction; PROVED by hand, by Claude, not yet checked).** Let F := log Omega + V/2 on M. If
  (SC)  Hess_M F(v) <= C_F g  for every v in M,
then (SG-step)_sigma holds with sigma^2 = C_F + beta. Since Hess_M(V/2) <= 8 beta g, the hypothesis
  (SC-Omega)  Hess_M log Omega(v) <= C_Omega g  for every v in M
gives (SG-step) with sigma^2 = C_Omega + 9 beta.
Proof. log p(u, w) = -V(u)/2 + log K(u, w) - log Omega(u) + (terms free of u), so
Hess_u log p(u, w) = Hess_u log K(u, w) - Hess_M F(u). With mu = mu_(u,w)(dg) = k(u, g.w) dg/K(u, w),
  Hess_u log K(u, w)(z, z) = E_mu[ Hess_u log k(u, g.w)(z, z) ] + Var_mu( d_u log k(u, g.w)[z] ),           (4.1)
(differentiate log of an integral twice), and Hess_u log k(u, w')(z, z) = -beta sum_l <u_l, w'_l> |z_l|^2 (on the unit
sphere the Hessian of x -> <x, a> is -<x, a> g). So Hess_u log K >= -beta g, Hess_u log p >= -(C_F + beta) g; Lemma HSS.
Hessian of V: write a plaquette as f_p = (1/2) tr(c_1 c_2 c_3^* c_4^*) along geodesics c_j(t) = u_j e^(t X_j), |X_j| = |z_j|;
the second t-derivative of the product of four unit quaternions has norm at most (sum_j |X_j|)^2 <= 4 sum_j |z_j|^2, and
|(1/2) tr Y| <= |Y|. Each link lies in 4 spatial plaquettes, so |Hess V(z, z)| <= beta * 4 * 4 |z|^2 = 16 beta |z|^2. QED

**Converse in temporal gauge (PROVED).** By Identity HV (2.2), beta^2 Var_(pi~_u)(<z, w'>) >= Hess_M F(u)(z, z) - beta |z|^2,
and sigma~(u, z)^2 >= beta^2 Var_(pi~_u)(<z, w'>). So
  sup_u sigma~(u)^2 is box-free  <=>  (SC) holds with a box-free C_F,
with C_F - beta <= sup_u sigma~(u)^2 <= C_F + beta. Upper bound: Lemma HSS applied to the temporal-gauge kernel
p~(u, w') := e^(beta <u, w'> + log R(w') - A(u)) with reference measure dw' (its integral in w' is 1 for every u in M,
its score is psi_(u,z), and Hess_u log p~(u, w')(z, z) = -beta sum_l <u_l, w'_l> |z_l|^2 - Hess_M F(u)(z, z) >= -(C_F + beta)|z|^2).
Lower bound: (2.2). A free lower bound: Hess_M F >= -beta g always, by (2.2).
In words: (SC) is a box-free bound on the susceptibility of the first-step electric field of the half-space Wilson
measure, uniform in the boundary slice: sup_u ||Cov_(pi~_u)(E)||_op <= (C_F + beta)/beta^2.

**Lemma CEN (the projected score vanishes at central slices; PROVED).** If u_l is in {1, -1} for every l, then
phi_(u,z) = 0 for every z in T_u M: sigma(u) = 0.
Proof. The constant gauge transformation g_x = c fixes u (u central) and acts on T_u M by z_l = xi_l u_l -> (c xi_l c^*) u_l.
p is gauge invariant in u, so the linear form L(xi) := d_u log p(u, w)[(xi_l u_l)_l] obeys L(Ad_c xi) = L(xi) for all c.
Average over Haar c: L(xi) = L(E_c Ad_c xi) = L(0) = 0, as the adjoint action of SU(2) on R^3 fixes no non-zero vector. QED
More generally d_u log p(u, w) is fixed by the stabilizer of u: at an abelian slice (all u_l in one U(1)) only the
Cartan components of z carry score.
Consequence. sigma <= sigma~ can be very lossy. At a central slice sigma = 0, while sigma~ is the variance of pure
gauge fluctuations: by (4.1) the term Var_mu, which Theorem SC drops, is exactly what cancels there
(Var_(pi_u)(phi) = Var_(pi~_u)(psi) - E_(pi_u) Var_mu(psi), law of total variance). So (SC) is SUFFICIENT for (SG-step)
but may fail where (SG-step) holds: if the temporal-gauge electric field at a central slice orders in colour
(an SO(3)-breaking pattern, invariant under the stabilizer only as a mixture), then C_F grows like N there, while
sigma(u) = 0. Section 6 tests exactly this (GUIDE).

**Relation to row 941 (PROVED implication).** Bakry-Emery CD(kappa, infinity) for nu = Omega^2 dU on M (Ric_M = 2 g on
unit spheres) reads 2 g - 2 Hess log Omega >= kappa g, i.e. Hess log Omega <= (1 - kappa/2) g. So any proof of
Bakry-Emery for nu (row 941, Attack A) gives (SC-Omega) with C_Omega = 1 and, by Theorem SC, (SG-step) with
sigma^2 <= 1 + 9 beta. (SC-Omega) asks only for SOME box-free C_Omega, so it is much weaker than Bakry-Emery.

**Status of (SC) for SU(2) at beta 2.3-2.6: OPEN.** What is known here:
- small beta: a uniform Dobrushin condition on the half-space measure (Section 3) gives a box-free susceptibility,
  hence (SC) (RECALLED route, beta below about 1/18; not rebuilt, not on the chain);
- classical picture (ARGUED): log Omega ~ -W_cl, W_cl(u) = least half-space action with boundary u. W_cl is a
  minimum over extensions, so it has concave kinks where two extensions tie; there log Omega ~ log(e^(-W_1) + e^(-W_2))
  has Hessian ~ |grad(W_1 - W_2)|^2/4 in the direction of the jump. With the per-link gradient bound |grad_l F| <= beta
  (PROVED: grad F is the tangential part of grad A = beta E w'), this is at most beta^2 times the number of links where
  the two extensions differ at the boundary. So (SC) fails exactly if some boundary slice makes two extensions tie
  that differ on a number of links growing with the box (a boundary-induced coexistence). Instantons do not do this
  (the jump of a size-rho instanton is of order beta rho^(-1/2), ARGUED); frustrated slices might;
- (SG-step) itself (the projected score) can survive a failure of (SC) located at slices with a large stabilizer
  (Lemma CEN). A failure of (SG-step) needs a coexistence in GAUGE-INVARIANT data of the next slice at a slice u
  whose stabilizer does not average it out.

**Identity EXP (the exact content of (SG-step); PROVED).** For u in M, a unit z in T_u M, real t, the geodesic
u(s) = exp_u(s z), and h(s, w) := Hess_u log p(u(s), w)(u'(s), u'(s)):
  E_(pi_u) e^(t phi_(u,z)) = E_(pi_(u(t))) exp( -I_t ),   I_t(w) := integral from 0 to t of (t - s) h(s, w) ds.
Proof. Taylor along the geodesic: t phi_(u,z)(w) = log p(u(t), w) - log p(u, w) - I_t(w). Exponentiate, multiply by
p(u, w), integrate in nu(dw). QED (For t < 0, I_t is the integral over [t, 0] of (s - t) h(s, w), again a positive
weight.) So (SG-step)_sigma holds iff E_(pi_(u(t))) e^(-I_t) <= e^(sigma^2 t^2/2) for all u, unit z, t. Lemma HSS is the
pointwise case h >= -H. By (4.1), -h(s, w) = Hess_M F(u(s))(u', u') + beta sum_l E_mu <u_l(s), (g.w)_l> |u'_l|^2
- Var_mu(beta <u'(s), g.w>) with mu = mu_(u(s),w): the Hessian of F is compensated, in exponential mean under the endpoint
law, by the variance of the gauge fluctuation of the score given w. At a central slice the compensation is exact
(Lemma CEN). So the weakest exact form of the open input is an exponential-moment bound on
Hess_M F - Var_mu along geodesics; (SC) is the case where Var_mu is simply dropped.

**Where this leaves the target.** (SG-step) at a box-free sigma is reduced to (SC) (sufficient), and in temporal
gauge (SC) is exact. Neither (SC) nor (SG-step) is proved for SU(2) at beta 2.3-2.6. The exact open inequality
handed on is
  (SC)  sup over v in M of the largest eigenvalue of Hess_M(log Omega + V/2)(v) <= C_F, C_F box-free,
or the weaker, projected form Hess_u log p(u, w) >= -H for all u, w (Lemma HSS), or, weakest, (SG-step) itself.

## 5. Fact tests (step 5)

- **Free photon (PROVED).** One mode: T(q, q') = exp(-(beta/2)(q - q')^2 - (beta/2)(m^2/2)(q^2 + q'^2)), cosh omega = 1 + m^2/2.
  The coupling term is beta q q'; V(q)/2 = (beta/2) cosh(omega) q^2; Omega = exp(-(beta/2) sinh(omega) q^2). So
  F = log Omega + V/2 = (beta/2) e^(-omega) q^2 and Hess F = beta e^(-omega). On R the coupling beta q q' has zero
  Hessian in q, so Lemma HSS gives sigma^2 <= beta e^(-omega): EXACT (the extra beta in Theorem SC is the curvature of
  S^3). Identity HV: beta^2 Var(q') = beta e^(-omega), Var(q') = 1/(beta e^omega) = v. The photon is gapless (omega_min -> 0)
  and has sigma^2 <= beta on every mode, so **(SG-step) at a box-free sigma does not imply a gap (PROVED).**
- **Compact U(1).** Lemmas TG, EF, HO, HV, HSS and Theorem SC hold verbatim with S^1 in place of S^3 (the Hessian
  of x -> <x, a> on the unit circle is -<x, a>; the plaquette Hessian bound and 4 plaquettes per link are unchanged).
  Lemma CEN gives nothing (constant U(1) gauge transformations act trivially). Its Gaussian (spin-wave) part has
  sigma^2 <= beta. Whether compact U(1) Wilson meets (SC) or (SG-step) with a box-free sigma is the same open question
  as for SU(2). Either way U(1)'s failure is carried by (LSI-vac) (alpha <= 2 beta sinh omega_min -> 0; rows 931, 940,
  check 942), not by (SG-step).
- **Frozen Q_8, 2T.** M is finite: no tangent vectors, so (SG-step), (SC), Lemma HSS and Theorem SC are not
  defined. This row asserts nothing for them (domain exclusion, as in check 942). Nothing here can carry a rival's
  failure.
- **SMALL-BOX (row 931).** (SG-step) and (SC) assert no gap. On a fixed box at large beta the chain is near-Gaussian
  and (SG-step) with sigma^2 of order beta is consistent with E_1 -> 0. No conflict. (That (SC) holds at large beta on
  a fixed box is NOT claimed: the kinks of W_cl in Section 4 sharpen as beta grows.)
- **FT-CEIL.** The 1/3, 2/3 and 0.775 ceilings cap worst-case single-link and block criteria: the Dobrushin route of
  Section 3 is of that type, which is why it stops at small beta (consistent). Check 870 S5 (READ, items 9-10)
  refutes environment-uniform conditional parity bounds, the environment being the SO(3) parts of ALL links (at the
  identity environment the conditional object is Z_2 gauge theory at beta, deconfined above 2.191 by Peierls).
  (SG-step) and (SC) condition on ONE slice and integrate the future, so that refutation does not apply as stated.
  (SC) is still a supremum over the conditioning slice and carries the same kind of risk: a boundary slice that
  induces ordering in the next slice. Section 6 tests one such slice. (In a deconfined Z_2-like regime a fixed
  boundary slice pins the next slice's flux, which is rigidity, not coexistence: ARGUED.)
- **Group-blindness.** Lemmas TG, EF, HO, HV, HSS, Theorem SC and Example DW are group-blind (any compact connected
  group with a bi-invariant metric; only the plaquette Hessian constant changes). Lemma CEN is not: it uses that the
  adjoint representation of SU(2) fixes no vector (true for SU(N), false for U(1)). So the only SU(2)-specific fact
  proved here is that the score vanishes at central slices; it costs no rival anything.

## 6. GUIDE run: does (SC) fail at a central frustrated slice? (step 6; criteria written before the run)

Decides nothing; it can only refute or guide. Target: (SC), not (SG-step) (by Lemma CEN the projected score is 0 at
any central slice, so this run cannot touch (SG-step) itself).
Model. Half-space Wilson SU(2) in temporal gauge: spatial box L^3 (periodic, L even), slices t = 0..T, slice 0 fixed
= u, all temporal links = 1 (complete gauge fixing, Haar, no Jacobian). Weight exp(beta sum_{t<T} sum_l <w_l(t), w_l(t+1)>
+ beta sum_{t=1..T} c_t sum_p (1/2) tr U_p(t)), c_t = 1 for t < T and 1/2 for t = T. As T -> infinity the law of slice 1 is
pi~_u (Lemma TG; the last slice's 1/2 is the e^(-V/2) of the last kernel, Omega replaced by 1). Heat bath: each link has a
von Mises-Fisher conditional law on S^3 (Wood's sampler), checkerboard by direction and parity of x + y + z + t.
Slices: u_pi (central, every spatial plaquette -1: u_x = 1, u_y = (-1)^x, u_z = (-1)^(x+y)) and the control u = 1.
Measured: E_l = Im(w_l(1) u_l^*). For central u the law of E is SO(3)-invariant and translation-invariant (Z_2 gauge
transformations leave E unchanged), so the one-colour covariance H' is diagonal in momentum:
Lambda(k) := (1/(3 L^3)) sum_a E[Ehat^a(k) Ehat^a(k)^dagger] (3 x 3 in directions), lambda(L) := max_k lambda_max(Lambda(k)) =
the top eigenvalue of H'. By (2.2), lambda_max(Hess F(u)) >= beta^2 lambda(L) - beta. Also v_1 := mean of E[(E_l^a)^2].
Criteria (fixed now). G := lambda(10)/lambda(4) at u_pi, beta 2.3, T 6, cold start.
- G >= 4 with lambda increasing in L: GUIDE says (SC) FAILS at u_pi (box-growing susceptibility; with exact SO(3)
  symmetry this is colour ordering of the first-step field). Then Theorem SC's route is dead for SU(2), and the
  projected form (Lemma HSS, or (SG-step) itself) must be used.
- G <= 1.3: no growth seen at u_pi ((SC) survives this one slice; establishes nothing).
- otherwise: inconclusive.
Controls: u = 1 must give G <= 1.3 (else the method is suspect); hot and cold starts must agree within 15 percent
(else "not equilibrated"); T = 4, 6, 8 at L = 6 must agree within 15 percent (else the truncation of Omega matters).
Script `/tmp/gap-sgstep-944/scripts/slab_E.py`, log `/tmp/gap-sgstep-944/slab_E.log`; numeric lock, nice, one thread.

## 7. Literature and credit (step 7)

**Sussman-Alpoge account (READ at 31a47c543775; outline and CA-II fetched to `/tmp/gap-sgstep-944/sa/`).** Search of
`library/sa-index/` (all chunks and `ca-full/index.tsv`) for sub-Gaussian, Hoeffding, Brascamp, log-concave,
semiconcave, ground state, temporal gauge; row 940 searched hypercontract, log-Sobolev, Harnack, Hopf-Lax (none).
Hits, all in the small-field Gaussian setting of their RG, none on a transfer chain:
- SA GCB20-GCB21 (`gcb:linear-moment-domination`, `gcb:linear-subgaussian`, L27495-27529, proved in detail): for
  their cutoff Gaussian law, even log-concave conditional weights and the sign symmetry Z -> -Z give
  nu[e^(tL)] <= e^(t^2 v(L)^2/2) for every linear statistic L, v(L)^2 = l^T Gamma l (Gaussian domination).
- CA-II Corollary 8.3:cor-subgaussian-tails (L81804-81850, PROVED; with Proposition 8.3:prop-lipschitz-stability,
  L81162-81190): for a Hamiltonian H = (1/2)<y, A y> + <h, y> - P(y) on a bounded product of convex sets, coercive
  with constant lambda, a linear observable F = <l, .> has nu_H(e^(s(F - nu_H F))) <= e^(s^2 |l|^2/(2 lambda)). Their proof
  tilts the linear term (h -> h - s l stays in the class) and bounds the drift of the mean along the tilt by the
  Lipschitz stability of the Gibbs mean.
Credit: Lemma EF (iii) and (2.1) are this tilt argument (Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text), moved to the slice chain, where the boundary slice enters exactly as a linear term
beta <u, w'>. What does not transfer is their hypothesis: coercivity (convexity) or even log-concavity. The compact
slice law at beta 2.3-2.6 has neither (Bakry-Emery for nu needs Hess log Omega <= 1, Section 4). Theorem SC replaces it
by the one-sided Hessian bound (SC), which is a susceptibility bound, not a convexity bound. The transfer frame
(outline (GL8), L2331) is theirs, as rows 931 and 940 record. The account has no slice-conditioned score bound and
no bound on the Hessian of the log ground state.

**Published results (RECALLED unless marked; credited, not used as unproved steps).**
- Hoeffding, "Probability inequalities for sums of bounded random variables", J. Amer. Statist. Assoc. 58 (1963)
  13-30: Hoeffding's lemma, rebuilt in Lemma HO (two lines). Azuma (1967) for the martingale remark of Section 3
  (not used).
- Herbst's argument (Davies-Simon 1984; Ledoux, "The concentration of measure phenomenon", AMS 2001): Lemma HSS is a
  one-step variant (a lower Hessian bound on log p(., w) in place of a log-Sobolev inequality); proved in full above.
- Brascamp and Lieb, J. Funct. Anal. 22 (1976) 366-389: log-concavity of ground states for convex potentials and
  the variance inequality. Not used: the slice law is not log-concave. (SC) is the semiconcavity analogue of
  their log-concavity, with a box-free constant in place of 0.
- Dobrushin's uniqueness condition and concentration under it (Kulske, Comm. Math. Phys. 239 (2003) 29-51): the
  small-beta route of Section 3. Not rebuilt, not on the chain.
- Mack and Petkova (centre/SO(3) split), through check 870 S5 (READ): used only in the FT-CEIL test.
- The identity E[score score^T] = -E[Hess log p] (Fisher information) is classical; Identity HV and (4.1) are its
  exponential-family and gauge-averaged forms, proved above.
Repo credit: the chain, (SG-step) and Theorem V/E are row 931 (Claude Fable 5.2); (E-to-HC), Lemma RD and Corollary
HC2 are row 940 (Claude Opus 5.5), checked by check 942 (Codex gpt-6-astra).
