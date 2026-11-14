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
