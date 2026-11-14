lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T17:51Z

# gap-etohc-opus: does (LSI-vac) plus (SG-step) give (HC-vac)?

Queue row 940 (FINISH.md). Author: Claude Opus 5.5, max effort, Mac mini worker 2.
Branch `claude/ym4d-hard-route`, pinned at db49e67f2. Started 2026-11-14T05:51Z.
Research-stage working state; nothing here is a public claim.

Labels: PROVED (written argument, checkable by hand), CONDITIONAL (on named inputs),
GUIDE (numerics, may refute or guide only), OPEN.

## Plan (at most eight steps; one per response)

1. Read row 931 (`library/gap-direction-max.md` Steps 5-7) and the FINISH rules; grep
   `library/open-core.md` and the FINISH rows for (E-to-HC); record the exact statements of
   (LSI-vac), (SG-step), (HC-vac) and what Proposition HC consumes.
2. Gaussian fact test: one mode (AR(1) / Ornstein-Uhlenbeck chain). Compute what (LSI-vac),
   (SG-step) and (HC-vac) are there, and Nelson's exponent q - 1 = e^(2 omega m).
3. Counterexample attack: a reversible kernel with both inputs and no hypercontractivity
   (if the lemma is false as stated, this is the answer).
4. Smallest extra hypothesis: what link between the Dirichlet form of P and the gradient form
   of (LSI-vac) makes it true; prove (E-to-HC) under it (discrete-time Gross argument, or
   continuous-time embedding).
5. Check whether the vacuum slice chain from the Wilson transfer operator satisfies that
   extra hypothesis (or what it would take).
6. GUIDE check on row 931's rotor chain (only if memory allows, under the numeric lock).
7. Literature/credit: Sussman-Alpoge account, Gross 1975, Diaconis-Saloff-Coste 1996,
   Miclo, Mossel et al. (discrete-time hypercontractivity); credit and statement map.
8. Final statement with labels and RESULT line.

## Progress log

(appended step by step below)

### Step 1: inputs, duplicate check, exact statements (READ at db49e67f2)

Read: FINISH.md (opening, How we work, Working efficiently, Rules, rows 931 and 938-943),
GOAL.md, `library/gap-direction-max.md` Steps 4-8 and Result (row 931, Claude Fable 5.2 max,
checked by no one; check row 938 is not on disk at this commit). Row 939's reading
(`library/prior/gap-lit-hcvac.md`) is not on disk at this commit.

Duplicate check (rule 0a). `grep -i -E "E-to-HC|HC-vac|LSI-vac|SG-step"` over
`library/open-core.md` and `library/l17c.md`: no hit. FINISH rows: 931 (names the lemma, does
not attack it), 939 (reading only), 940 (this row), 941 (attacks (LSI-vac)/(HC-vac) for SU(2),
not the implication), 942 (check of this row). No other row attacks (E-to-HC). Proceed.

Setting (row 931 Step 5, READ). M = SU(2)^(3|B|), the links of one time slice, with the product
of unit-S^3 metrics (compact, connected; gauge transformations act by isometries). T(u, w) > 0
the gauge-invariant Wilson transfer kernel, symmetric, real-analytic; Omega > 0 its ground
state, lambda_0 its top eigenvalue. nu = Omega^2 dU. p(u, w) := T(u, w)/(lambda_0 Omega(u) Omega(w))
is the density of pi_u := P(u, .) with respect to nu; p is symmetric, so P is nu-reversible and
nu is stationary. P g(u) = integral of p(u, w) g(w) nu(dw).
The centred score: grad_u log p(u, w) = G(u, w) - E_(pi_u) G(u, .), G = grad_u log T(u, .)
(the pi_u-mean of grad_u log p(u, .) is grad_u of 1, which is 0).

- (LSI-vac)_alpha: Ent_nu(f^2) <= (2/alpha) E_nu |grad f|^2 for gauge-invariant f
  (row 931's form Ent_nu(h) <= E_nu[|grad h|^2/h]/(2 alpha) with h = f^2).
- (SG-step)_sigma: for every u and unit z in T_u M, phi_(u,z) := z . grad_u log p(u, .)
  satisfies E_(pi_u) exp(lambda phi_(u,z)) <= exp(lambda^2 sigma^2/2) for all real lambda.
  (Row 931 says "almost every u"; for a continuous kernel this is the same, by continuity of
  u -> E_(pi_u) exp(lambda phi_(u,z)) in a continuous local frame and Fatou.)
- (HC-vac)_alpha': for every integer m >= 0, ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha' m).
- (E-to-HC): (LSI-vac)_alpha and (SG-step)_sigma imply (HC-vac)_alpha', alpha' = c(alpha, sigma) > 0.

Row 931's stop (quoted, Step 6): "at fixed q > 1 the telescoping gives a fixed per-step factor
on a quantity that starts at exp(extensive) ... the gain of Proposition HC needs q to grow along
the chain, and in discrete time the Dirichlet form of P is not the gradient form of (LSI-vac)."

Approach chosen (after the reading, before Step 2). Do not go through the Dirichlet form of P.
Put the continuous time in the Hopf-Lax (inf-convolution) semigroup on M instead, where the
gradient form of (LSI-vac) is the natural one, and carry the one-step smoothing of P by a
Harnack inequality in the metric of M. Three lemmas:
  (RD) Renyi bound from (SG-step): E_(pi_y)[(dpi_x/dpi_y)^lambda] <= exp(lambda(lambda-1) sigma^2 d(x,y)^2/2).
  (H)  Harnack from (RD) by Hoelder: (P g)(x)^p <= P(g^p)(y) exp(p sigma^2 d(x,y)^2/(2(p-1))).
  (BGL) Hopf-Lax hypercontractivity from (LSI-vac): ||e^(Q_s F)||_(1 + alpha s) <= ||e^F||_1.
Together: ||P g||_Q <= ||g||_p with Q - 1 = (p - 1)(1 + alpha/sigma^2), hence (HC-vac) with
alpha' = (1/2) log(1 + alpha/sigma^2). Credit for the method: F.-Y. Wang's dimension-free
Harnack inequality (1997) and Bobkov, Gentil and Ledoux (2001), RECALLED, rebuilt below.

### Repo search (rule "Repo first")

`grep -r -l -i -E "hypercontract|hopf-lax|inf-convolution|bobkov|Harnack"` over this target
folder: hits in `library/prior/gap-lit-geom.md` (survey: Gross 1975, Simon and Hoegh-Krohn,
Bauerschmidt et al., Gross 2024; all continuous-time Dirichlet-form statements, no discrete-time
Harnack route), `library/gap-compress-opus.md` Section (1) (entropy-contraction route; it says
"one needs in addition a hypercontractive estimate for P that excludes rare slow modes"),
`library/gap-skeleton-max.md` B11, `library/gap-kurt-max.md` (attack B, hypercontractivity
assumed), `library/gap-crux-exercise-astra.md` L2, and complex-analysis Harnack uses
(`gap-zf-box-s.md`, `gap-zero-transport-check.md`, `gap-skeleton-max-b.md`) that are unrelated.
No note derives hypercontractivity of the slice chain from a log-Sobolev input. The
Sussman-Alpoge statement index `library/sa-index/` has no hit for hypercontract, log-Sobolev or
Harnack. A whole-repository `git grep` (origin/main and other paths) was started; its result is
recorded in Step 7 if it returns.

### Step 2: Gaussian fact test, one mode (PROVED, by hand)

Model (row 931 Step 5, one photon mode of FP): nu = N(0, s^2) on R with s^2 = 1/(2 beta sinh omega);
pi_q = N(e^(-omega) q, v), v = 1/(beta e^omega). (Stationarity: e^(-2 omega) s^2 + v = s^2.)
Here M = R is not compact; the test checks the constants, and each lemma below is checked on
this model by direct computation.

(a) (SG-step). log p(q, q') = log pi_q(q') - log nu(q'), so grad_q log p(q, q') =
beta (q' - e^(-omega) q). Under pi_q this is N(0, beta^2 v) = N(0, beta e^(-omega)). Exact
sub-Gaussian proxy: sigma^2 = beta e^(-omega).
(b) (LSI-vac). Gaussian log-Sobolev (Gross): Ent(f^2) <= 2 s^2 E|f'|^2, sharp. So
alpha = 1/s^2 = 2 beta sinh omega.
(c) The claimed exponent. 1 + alpha/sigma^2 = 1 + 2 sinh(omega) e^omega = e^(2 omega). So the claim
is Q - 1 = e^(2 omega) (p - 1) for one step and alpha' = (1/2) log(1 + alpha/sigma^2) = omega.
This is Nelson's exponent: P is the Ornstein-Uhlenbeck semigroup at time omega in units where
its gap is 1, and ||P||_(p -> Q) <= 1 holds if and only if Q - 1 <= e^(2 omega)(p - 1) (Nelson,
RECALLED; the "only if" is the test f = e^(c q) with c -> 0 and c -> infinity, by direct
Gaussian integrals). So the claim is sharp here: no larger alpha' is true.
(d) (RD) on this model. pi_x and pi_y are Gaussians with the same variance v and means differing
by delta = e^(-omega)(x - y). E_(pi_y)[(dpi_x/dpi_y)^lambda] = exp(lambda(lambda - 1) delta^2/(2v)),
and delta^2/v = beta e^(-omega)(x - y)^2 = sigma^2 d(x, y)^2. So (RD) holds with EQUALITY.
(e) Product of modes (FP): directions z = sum z_k e_k with |z| = 1 give a centred Gaussian score
of variance sum z_k^2 beta e^(-omega_k) <= beta e^(-omega_min), and alpha = min_k 2 beta sinh omega_k
(LSI tensorizes) = 2 beta sinh omega_min. So alpha' = omega_min = E_1. Sharp again.
(f) Consistency with Theorem E (row 931). Its contraction factor is rho = Theta_H/(1 + Theta_H)
with Theta_H = sigma^2/alpha, so rho = 1/(1 + alpha/sigma^2) and the claim reads Q - 1 = (p - 1)/rho.
Letting p -> 1 in ||P g||_Q <= ||g||_p for a density g (||g||_p = 1 + (p - 1) Ent(g) + o(p - 1))
gives Ent(P g) <= rho Ent(g): Theorem E is the p -> 1 end of the claim, with the same constant.

Fact tests passed by the claim: U(1) (alpha <= 2 beta sinh omega_min -> 0, so alpha' -> 0: the
implication cannot make U(1) pass, its input fails); frozen Q_8, 2T (no gradient: the inputs
are not defined); SMALL-BOX (the claim is an implication; it asserts no slice-law inequality for
SU(2)); ceilings (the claim needs sigma finite, not small; no supremum threshold enters).

### Step 3: Lemma RD, the Renyi bound from (SG-step) (PROVED, by hand; not yet checked)

**Standing hypotheses (K).** M is a compact connected Riemannian manifold without boundary, d its
distance, nu a Borel probability measure on M. p: M x M -> (0, infinity) is continuous; for each w,
x -> p(x, w) is C^1, and (x, w) -> grad_x p(x, w) is continuous on M x M; and the integral of
p(x, w) nu(dw) is 1 for every x. Write pi_x := p(x, .) nu, P g(x) := integral of p(x, w) g(w) nu(dw),
and L := sup over (x, w) of |grad_x log p(x, w)| (finite: continuity, positivity, compactness).
L is used only qualitatively; no bound below depends on it.
For the slice chain: M = SU(2)^(3|B|), p = T/(lambda_0 Omega x Omega). T is positive and real-analytic;
Omega = T Omega/lambda_0 is positive and C^1 (differentiate under the integral). So (K) holds.

**Lemma SGC (sub-Gaussian covariance; PROVED; this is row 931's Theorem E step (ii)).** Let pi be a
probability measure, phi a function with E_pi e^(theta phi) <= e^(theta^2 sigma^2/2) for all theta > 0,
and h >= 0 bounded with m := E_pi h > 0. Then E_pi[h phi] <= sqrt(2 sigma^2 m Ent_pi(h)).
Proof. Gibbs inequality: for a pi-density g and E_pi e^psi finite, E_pi[g psi] <= Ent_pi(g) +
log E_pi e^psi (Jensen for the probability g pi applied to log of e^(psi - log g) on {g > 0}).
Take g = h/m, psi = theta phi: theta E_pi[h phi]/m <= Ent_pi(h)/m + theta^2 sigma^2/2. If Ent_pi(h) > 0
put theta = sqrt(2 Ent_pi(h)/(m sigma^2)); if Ent_pi(h) = 0 let theta -> infinity (bound 0). QED

**Lemma RD.** Assume (K) and (SG-step)_sigma at every x in M (only theta > 0 is used). Then for all
x, y in M and lambda > 1:
  (RD)  E_(pi_y)[ (p(x, .)/p(y, .))^lambda ] <= exp( lambda (lambda - 1) sigma^2 d(x, y)^2 / 2 ).
Equivalently, the Renyi divergence of order lambda obeys D_lambda(pi_x || pi_y) <= lambda sigma^2 d^2/2.

Proof. If x = y there is nothing to prove; let d := d(x, y) > 0. Take a minimizing geodesic
gamma: [0, 1] -> M from y to x with |gamma'| = d (Hopf-Rinow); x_t := gamma(t), z_t := gamma'(t)/d.
Put R_t(w) := p(x_t, w)/p(y, w). Then d/dt log R_t(w) = d phi_t(w), phi_t := <grad_x log p(x_t, w), z_t>,
so |log R_t(w)| <= L d t, and R_t pi_y = pi_(x_t). Define on [0, 1] x (1, infinity)
  Lambda(t, lambda) := log of the integral of R_t^lambda d pi_y.
Lambda is C^1 (differentiate under the integral; integrands and their partial derivatives are
continuous and bounded on compact sets of (t, lambda), uniformly in w), with
  d_t Lambda = lambda d E_(pi_(x_t))[R_t^(lambda - 1) phi_t] e^(-Lambda),
  d_lambda Lambda = e^(-Lambda) times the integral of R_t^lambda log R_t d pi_y.
(a) Differential inequality. Apply Lemma SGC with pi = pi_(x_t), phi = phi_t (sub-Gaussian by
(SG-step) at x_t, direction z_t), h = R_t^(lambda - 1). Then m = e^Lambda and
Ent_(pi_(x_t))(h) = (lambda - 1) times the integral of R_t^lambda log R_t d pi_y, minus e^Lambda Lambda,
= e^Lambda Y with Y := (lambda - 1) d_lambda Lambda - Lambda >= 0. Hence
  d_t Lambda <= lambda d sqrt(2 sigma^2 Y).
For every eps > 0 (AM-GM): lambda d sqrt(2 sigma^2 Y) <= eps Y + lambda^2 d^2 sigma^2/(2 eps). So
  d_t Lambda <= eps (lambda - 1) d_lambda Lambda - eps Lambda + lambda^2 d^2 sigma^2/(2 eps).     (3.1)
(b) Characteristics. Fix lambda_1 > 1. For t in (0, 1] put lambda(t) := lambda_1/t, psi(t) := Lambda(t, lambda(t)),
eps(t) := lambda_1/(t (lambda_1 - t)) > 0. Then eps(t)(lambda(t) - 1) = lambda_1/t^2 = -lambda'(t), so
(3.1) at (t, lambda(t)) gives psi'(t) <= -eps(t) psi(t) + s(t), s(t) := lambda_1 (lambda_1 - t) d^2 sigma^2/(2t).
With E(t) := t/(lambda_1 - t), E' = eps E, so (E psi)' <= E s = lambda_1 d^2 sigma^2/2. For 0 < t_0 < 1:
  psi(1)/(lambda_1 - 1) <= E(t_0) psi(t_0) + lambda_1 d^2 sigma^2 (1 - t_0)/2.
(c) The endpoint term vanishes. The integral of R_(t_0) d pi_y is 1 and R_(t_0) <= e^(L d t_0), so
psi(t_0) <= (lambda_1/t_0 - 1) L d t_0 <= lambda_1 L d, and E(t_0) psi(t_0) <= t_0 lambda_1 L d/(lambda_1 - t_0) -> 0.
Letting t_0 -> 0: Lambda(1, lambda_1) = psi(1) <= lambda_1 (lambda_1 - 1) sigma^2 d^2/2. QED

Remarks. (i) The characteristic lambda t = const is the one along which the Gaussian is extremal
(it makes AM-GM an equality on the Gaussian solution Lambda = lambda(lambda - 1) t^2 d^2 sigma^2/2);
along it the a-priori bound, which depends on L (volume-sized for the slice chain), is multiplied
by E(t_0) -> 0. So (RD) carries no volume and no dimension. (ii) Equality in the Gaussian mode
(Step 2(d)). (iii) lambda -> 1 gives KL(pi_x || pi_y) <= sigma^2 d(x, y)^2/2 (log-Harnack input).
(iv) The supremum form of (SG-step) is used: (SG-step) is needed at every point of a geodesic.
An averaged form (row 931 Step 7) does not enter this proof.

### Step 4: Lemma H (Harnack) and Lemma BGL (Hopf-Lax hypercontractivity) (PROVED, by hand; not yet checked)

**Lemma H (dimension-free Harnack inequality for one step).** Assume (K) and (RD). For p > 1,
g >= 0 in L^p(nu), and all x, y in M:
  (P g(x))^p <= P(g^p)(y) exp( p sigma^2 d(x, y)^2 / (2(p - 1)) ).
Proof. P g(x) = E_(pi_y)[g R] with R = p(x, .)/p(y, .). Hoelder with p and p* = p/(p - 1) > 1:
P g(x) <= (P(g^p)(y))^(1/p) (E_(pi_y) R^(p*))^(1/p*), and by (RD) with lambda = p*,
(E_(pi_y) R^(p*))^(1/p*) <= exp((p* - 1) sigma^2 d^2/2) = exp(sigma^2 d^2/(2(p - 1))). Raise to the power p. QED
(Form and name: F.-Y. Wang's dimension-free Harnack inequality, RECALLED; the proof here is
Hoelder plus Lemma RD. In the Gaussian mode it is sharp: Step 2(d) and equality in Hoelder for
g = e^(c q).)

**Hopf-Lax semigroup.** For F: M -> R Lipschitz (constant L_F) and s > 0, Q_s F(x) := min over y
of [F(y) + d(x, y)^2/(2s)]. D := diam M.
(R1) The minimum is attained (compactness), F - L_F^2 s/2 <= Q_s F <= F (take y = x; and
F(y) >= F(x) - L_F r with min over r >= 0 of (r^2/(2s) - L_F r) = -L_F^2 s/2). So Q_s F -> F
uniformly as s -> 0, and -sup|F| <= Q_s F <= sup|F|.
(R2) x -> Q_s F(x) is Lipschitz with constant D/s: with y a minimizer at x,
Q_s F(x') - Q_s F(x) <= (d(x', y)^2 - d(x, y)^2)/(2s) <= d(x, x') 2D/(2s), and symmetrically.
(R3) For 0 < s_0 <= s < s': 0 <= Q_s F(x) - Q_(s') F(x) <= D^2 (s' - s)/(2 s_0^2) (y' a minimizer
at (x, s'): Q_s F(x) <= F(y') + d(x, y')^2/(2s) = Q_(s') F(x) + d(x, y')^2 (s' - s)/(2 s s')).
(R4) If Q_s F is differentiable at x, then limsup over h -> 0+ of (Q_(s+h) F(x) - Q_s F(x))/h
<= -|grad Q_s F(x)|^2/2.
Proof. Let y minimize at (x, s), r := d(x, y). First, Q_(s+h) F(x) <= F(y) + r^2/(2(s + h))
= Q_s F(x) - r^2 h/(2s(s + h)), so the limsup is at most -r^2/(2 s^2). Second, for every x',
Q_s F(x') - Q_s F(x) <= (d(x', y)^2 - r^2)/(2s) <= d(x, x')(2r + d(x, x'))/(2s). If
v := grad Q_s F(x) is not 0, put x' = exp_x(tau v/|v|), tau -> 0+: tau |v| + o(tau) <= tau (2r + tau)/(2s),
so |v| <= r/s and -r^2/(2 s^2) <= -|v|^2/2. QED
(R5) (Rademacher, applied in charts) a Lipschitz function on M is differentiable at almost every
point for the Riemannian volume, hence nu-almost everywhere when nu has a density.
(R6) If a group of isometries of M leaves F invariant, it leaves Q_s F invariant
(Q_s F(kx) = min over y of [F(ky) + d(kx, ky)^2/(2s)] = Q_s F(x)). Gauge transformations act on M
by isometries, so gauge-invariant F give gauge-invariant Q_s F.

**Lemma BGL (Bobkov-Gentil-Ledoux at exponent 1).** Let nu have a continuous positive density
with respect to the volume of M, and satisfy (LSI-vac)_alpha for Lipschitz gauge-invariant f
(Ent_nu(f^2) <= (2/alpha) E_nu |grad f|^2, with grad the almost-everywhere gradient). Then for every
gauge-invariant Lipschitz F and every s > 0:
  || e^(Q_s F) ||_(1 + alpha s) <= E_nu e^F.
Proof. Put b(s) := 1 + alpha s, u_s := Q_s F, Z(s) := E_nu e^(b(s) u_s), H(s) := log Z(s)/b(s).
Fix 0 < s_0 < s_1. By (R1) and (R3), s -> b(s) u_s(x) is Lipschitz on [s_0, s_1] uniformly in x, and
Z >= e^(-b sup|F|) > 0; so H is Lipschitz there, differentiable at almost every s, and
H(s_1) - H(s_0) is the integral of H'. Fix s where H (hence Z = e^(bH)) is differentiable. With
Delta_h := b(s + h)(u_(s+h) - u_s) + alpha h u_s, (Z(s + h) - Z(s))/h = E_nu[e^(b u_s)(e^(Delta_h) - 1)/h],
and |Delta_h| <= C h by (R3), so the integrands are bounded uniformly in h in (0, 1]. At every x
where u_s is differentiable (nu-almost every x by (R2), (R5)), (R4) gives limsup Delta_h/h <=
-b |grad u_s|^2/2 + alpha u_s, and (e^Delta - 1)/Delta -> 1. Reverse Fatou:
  Z'(s) <= E_nu[ e^(b u_s) (alpha u_s - b |grad u_s|^2/2) ].
So H'(s) = -alpha log Z/b^2 + Z'/(b Z) <= (alpha/(b^2 Z)) Ent_nu(e^(b u_s)) - E_nu[e^(b u_s) |grad u_s|^2]/(2Z).
Apply (LSI-vac) to f = e^(b u_s/2), which is Lipschitz and gauge invariant by (R2), (R6), with
|grad f|^2 = (b^2/4) e^(b u_s) |grad u_s|^2 almost everywhere: Ent_nu(e^(b u_s)) <=
(b^2/(2 alpha)) E_nu[e^(b u_s) |grad u_s|^2]. Hence H'(s) <= 0, and H(s_1) <= H(s_0). Let s_0 -> 0:
u_(s_0) -> F uniformly (R1), b(s_0) -> 1, so H(s) <= log E_nu e^F. QED
Fact test (by hand): nu = N(0, 1) on R (alpha = 1), F(y) = c y: Q_s F(x) = c x - c^2 s/2, and both
sides equal e^(c^2/2) when the exponent is 1 + s. So the exponent 1 + alpha s cannot be raised.

**Smooth to Lipschitz in (LSI-vac).** Row 931 states (LSI-vac) for smooth gauge-invariant
functions. For Lipschitz gauge-invariant f put f_n := e^(tau_n Delta) f, Delta the Laplace-Beltrami
operator of M, tau_n -> 0. Delta commutes with isometries, so f_n is smooth and gauge invariant;
f_n -> f uniformly; and grad f_n -> grad f in L^2(vol), because f is in W^(1,2)(M) and
||grad(e^(tau Delta) f - f)||^2 = sum over k of lambda_k (1 - e^(-tau lambda_k))^2 |f_k|^2 -> 0 (eigenfunction
expansion, dominated convergence). With the density of nu bounded, both sides of (LSI-vac)
converge. (Textbook facts used: Rademacher's theorem, the spectral decomposition of the
Laplace-Beltrami operator on a compact manifold, Lipschitz functions are in W^(1,2) with the
a.e. gradient as weak gradient.) PROVED modulo these textbook theorems.

### Step 5: Theorem HC1 and the lemma (E-to-HC) (PROVED GIVEN (LSI-vac), (SG-step); by hand; not yet checked)

**Theorem HC1 (one-step hypercontractivity of the slice chain).** Assume (K); stationarity (the
integral of p(x, w) nu(dx) is 1 for every w; it holds since p is symmetric); a group of isometries
of M (the gauge group) leaves nu invariant and p(kx, w) = p(x, w); nu has a continuous positive
density; (LSI-vac)_alpha; (SG-step)_sigma at every x, with sigma > 0. Then for every p in (1, infinity)
and every g in L^p(nu):
  || P g ||_Q <= || g ||_p,   Q := 1 + (p - 1)(1 + alpha/sigma^2).
Proof. First let g >= 0 be bounded and not nu-a.e. 0. Then P(g^p)(x) >= (min p) E_nu g^p > 0, P(g^p)
is C^1 with |grad P(g^p)| <= L P(g^p), so F := log P(g^p) is Lipschitz, and F is gauge invariant
because p is gauge invariant in its first argument. By Lemma H, for all x, y:
p log P g(x) <= F(y) + d(x, y)^2/(2s) with s := (p - 1)/(p sigma^2). Minimize over y:
(P g)^p <= e^(Q_s F) pointwise. By Lemma BGL and stationarity,
  || P g ||_(p(1 + alpha s))^p = || (P g)^p ||_(1 + alpha s) <= || e^(Q_s F) ||_(1 + alpha s) <= E_nu P(g^p) = E_nu g^p.
And p(1 + alpha s) = p + alpha (p - 1)/sigma^2 = Q. For general g: |P g| <= P|g|, and
min(|g|, n) increases to |g|, so monotone convergence gives ||P g||_Q <= ||P |g| ||_Q <= ||g||_p. QED

**Corollary (E-to-HC), the lemma of this row.** Under the hypotheses of Theorem HC1 put
  alpha' := (1/2) log(1 + alpha/sigma^2) = (1/2) log(1 + 1/Theta_H) = (1/2) log(1/rho)
(Theta_H = sigma^2/alpha and rho = Theta_H/(1 + Theta_H) are row 931's Theorem E constants). Then
(i) ||P^m g||_(Q_m) <= ||g||_p with Q_m - 1 = (p - 1) e^(2 alpha' m), for all m >= 0 and p > 1;
(ii) (HC-vac)_alpha': ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha' m), for every m >= 0 and every h;
(iii) ||P^m||_(2 -> q) <= 1 with q - 1 = e^(2 alpha' m) (Nelson-Gross form; P is self-adjoint on
L^2(nu), and the dual exponent of q' is q).
Proof. (i) Induction on m with Theorem HC1. (ii) Put p = q' in (i): Q_m = 2. (iii) Duality. QED
So c(alpha, sigma) = (1/2) log(1 + alpha/sigma^2) > 0 for every alpha > 0 and finite sigma. It does not
depend on the box, the dimension or the group. In the Gaussian mode it equals omega (Step 2):
Nelson's exponent, the best possible. Row 931's Theorem E is the p -> 1 end of Theorem HC1
(Step 2(f)) and is not used.

**Where row 931's stop is passed.** Row 931 sought a Gross argument for the chain itself and
found that the Dirichlet form of P is not the gradient form. The proof above never uses the
Dirichlet form of P. The continuous time is the Hopf-Lax time s of Lemma BGL, where the
gradient form of (LSI-vac) is the natural one; the one-step smoothing of P enters only through
the metric Harnack inequality (Lemma H), and the moving exponent is p -> p(1 + alpha s).

**Consequence for the seed (Proposition HC of row 931, READ; with alpha' above).** For every
m >= 0, X(2m + 2; B) <= 72 beta |B| (1 + alpha/sigma^2)^(-m) and E_1 >= alpha'. So Form W on the box
(a; (24a)^3) at beta = 2.3 follows from (LSI-vac)_alpha and (SG-step)_sigma on that one box as soon as
  (1/2) log(1 + alpha/sigma^2) (a - 2) >= 16.0 + 3 log a.
(Row 931's numbers; 16.0 = log(72 beta 24^3/x_*) at beta = 2.3, not re-derived here.)

**Hypotheses used beyond row 931's statements, and whether the slice chain meets them.**
(1) (K): continuity, positivity, C^1 in the first variable. Holds (T positive, real-analytic;
Omega positive, C^1). (2) (SG-step) at every point, in the supremum form row 931 states; an
averaged form does not enter Lemma RD. (3) (LSI-vac) for Lipschitz gauge-invariant functions;
implied by the smooth form (Step 4). (4) Gauge invariance of p in its first argument: T is the
gauge-projected transfer kernel. No other hypothesis. So no counterexample kernel exists in
the class of row 931 (any kernel meeting (K) and both inputs is hypercontractive with alpha').
