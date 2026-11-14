lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T20:51Z

# gap-fc-max (row 947): the Fisher-information contraction (FC)_theta on the seed box

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, pinned at commit f1c3de09b, started 2026-11-14T08:51Z.
Author item. Not checked by another model (check = row 949). Research-stage working state; nothing here is a public claim.
No subagents. No computer-assisted step: any run is labelled GUIDE and can only refute or guide.

Credit. The seed, the slice chain and the hypercontractivity route come from this repository's rows 931-946 (Claude and Codex).
The transfer-matrix and vacuum-slice setting builds on Ethan Sussman and Levent Alpoge's complete account
(CA-I/II/III at commit 31a47c543775, text by them with Claude and Codex) and on Balaban's and Dimock's papers; each use is cited where it occurs.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read row 941 (`library/gap-lsivac-max.md`) in full. Record (A3), (FC)_theta, (GC)_theta, Theorem C0, and the rate Proposition HC needs.
2. Read row 946 (`library/gap-fctest-opus.md`) and check 943. Decide the branch: (FC) refuted at beta 2.3 (then: corrected Dirichlet form) or not (then: attack (FC)).
3. Duplicate check (rule 0a): grep `library/open-core.md`, `library/l17c.md` and the FINISH rows for (FC)/(GC). Outline lookup in the Sussman-Alpoge index.
4. State (FC)_theta with the explicit seed-sized rate (lead note (a)). Fact tests on the statement: U(1) fails THAT rate; SMALL-BOX; frozen groups.
5. Attack the linearisation (GC)_theta: P grad^* grad P at most theta grad^* grad on L^2(nu). One approach per response.
6. Attack (FC)_theta itself, or lift (GC) to (FC).
7. If it does not close: the smallest unproved inequality, and one test that could refute it.
8. Final summary and the RESULT line.

## Status log

- 08:51Z file created. Nothing proved yet.
- about 08:58Z Steps 1-3 written below. Branch decision: row 946 did NOT refute (FC); so (FC) is attacked.
- about 09:00Z Step 4 written. 09:03Z Step 5 (Theorem BR) written. 09:06Z Step 6 criteria written; numeric lock held by row 950 (gap-sc-950) until 09:59Z at the latest; the run waits.
- (Clock times in this log are from `date -u`; the session started 08:51Z.)

## Steps 1-3: inputs read, branch decision, duplicate check (READ; no new claim)

**Read at f1c3de09b.** FINISH.md (opening, How we work, Joining, Working efficiently, Rules, rows 941, 943, 946-951),
GOAL.md, `library/gap-lsivac-max.md` (row 941) in full, `library/gap-fctest-opus.md` (row 946) in full,
`library/gap-lsivac-check-astra.md` (check 943: findings, seed and fact tests, test proposal, locality),
`library/gap-direction-max.md` 300-365 (row 931: Proposition HC, Theorem E, the (E-to-HC) stop).

**Objects (row 941, quoted in short).** B a periodic spatial box, L = 3|B| links, M = (S^3)^L inside R^N, N = 4L.
V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2). Omega its top eigenfunction,
lambda_0 its eigenvalue, nu = Omega^2 dx. m(dw) := e^(-V(w)/2) Omega(w) dw. One-step law
pi_x(dw) = e^(beta <x, w>) m(dw)/(lambda_0 e^(V(x)/2) Omega(x)); P f(x) = E_(pi_x) f; P is self-adjoint on L^2(nu).
(A3): z . grad(P f)(x) = beta Cov_(pi_x)(<z, w>, f). I(g) := E_nu[|grad g|^2/g].
(FC)_theta: I(P g) <= theta I(g). (GC)_theta: E_nu|grad P f|^2 <= theta E_nu|grad f|^2.
(C1-av)_(alpha_c): Ent_nu(g) - Ent_nu(P g) <= I(g)/(2 alpha_c). Theorem C0: (FC) + (C1-av) give (LSI-vac) with alpha_c (1 - theta).
(HC-vac)_alpha (row 931, line 306): ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha m), every integer m >= 0, norms in L^p(nu).
Proposition HC (row 931; HOLDS in check 938): (HC-vac)_alpha gives X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m).
Seed: X(a; (24a)^3) <= x_* once alpha (a - 2) >= C_beta(x_*) + 3 log a, C_beta(x_*) := log(72 beta 24^3/x_*), a even.

**Branch decision.** Row 946 (GUIDE, Claude Opus 5.5, unchecked): no f with R(f) >= 1; every measured
R(f) = E|grad P f|^2/E|grad f|^2 is below 0.23 at beta 2.3 and 2.6 on boxes of side 4 and 6. So (FC) is not refuted
and this row attacks (FC). On lead note (b): row 946 did not use a periodic finite cylinder. It used OPEN time
{0..2K}, K = 6 and 8, with the middle slice frozen and the two halves independent (its (E1)-(E4)). The laws it
samples are nu_K ~ (T^K b)^2 and pi_x^(K) ~ T_0(x, w)(T^(K-1) b)(w), b = e^(-V/2). So there is no extra backward
factor T^N(x, x); the difference from (nu, pi_x) is the open-boundary error, of order e^(-E' K), not quantified
there, with stability shown only for K = 6 -> 8. Its numbers are GUIDE on (nu_K, pi_x^(K)) for boxes of side 4 and
6, not on the vacuum pair of the seed box.

**Duplicate check (rule 0a).** `grep -n -i -E "\(FC\)|\(GC\)|fisher|entropy contraction|data.processing|SDPI|polchinski|de bruijn|hypercontract|log-sobolev|LSI"`
on `library/open-core.md`, `library/l17c.md`, `library/open-registry.md`: no hit. FINISH rows naming (FC)/(GC): 941
(states them), 943 (check), 946 and 948 (GUIDE test and its check), 947 (this row), 949 (its check), 950 and 951
((SC), the other input: worker 1; I do not attack (SC)). Entropy contraction is row 931's Theorem E (given
(LSI-vac), (SG-step)); (E-to-HC) is row 940. No row owns (FC) or (GC) beside this one. I proceed.
For the bridge interpolation of Step 5 below: `grep -n -i -E "polchinski|de bruijn|heat flow|interpolat|brownian"` on
rows 931, 940, 944, 950 and `prior/gap-lit-hcvac.md`: no use of it (one remark on Brownian motion in row 950, line 208).

**Sussman-Alpoge account.** Rows 938-941 and 946 record that `library/sa-index/` has no log-Sobolev, hypercontractive or
Fisher-information statement; I did not repeat those greps. Their account enters through the transfer frame
(outline (GL8), located by checks 927, 933, 938). Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text.

## Step 4: (FC) with the rate the seed needs, and its fact tests (about 09:00Z)

**4.1 The statement (substitution in the arrows of row 941 Step 6; check 943 wrote the same line).**
Put K_a := (C_beta(x_*) + 3 log a)/(a - 2) for even a >= 4. The route (FC) + (C1-av) -> (LSI-vac) -> (HC-vac) -> seed
needs, on the one box B = (24a)^3:

  (FC-seed)_a:  (FC)_theta, (C1-av)_(alpha_c), (COV)_kbar hold on B with  alpha_c (1 - theta) >= beta^2 kbar (e^(2 K_a) - 1).

Equivalently theta <= theta_seed(a) := 1 - (beta^2 kbar/alpha_c)(e^(2 K_a) - 1). "theta < 1" alone gives nothing.
Sizes (hand arithmetic, C_beta = 16 at beta 2.3): K_30 = (16 + 10.21)/28 = 0.936, K_40 = (16 + 11.07)/38 = 0.712,
K_60 = (16 + 12.29)/58 = 0.488. With kbar >= 1/4 (row 941 (A5)) the right side is at least 1.32 (e^(2 K_a) - 1) at
beta 2.3: 7.3, 4.2 and 2.2 for a = 30, 40, 60.

**4.2 Necessary side (PROVED, one line each).** (HC-vac)_alpha gives E_1(B) >= alpha (Proposition HC). So every route
to the seed through (HC-vac) needs E_1(B) >= K_a on B = (24a)^3. With the box side b = 24a:
  b E_1(B) >= 24 a K_a > 384 + 72 log a.
So the seed, on this route, is one inequality for the dimensionless gap b E_1 at ONE box side b.

**4.3 FT-U1 against THAT statement (PROVED given the mode list of FP, read by check 943 at `gap-seam-max.md:88-116`).**
In the photon sector of FP every constant is attained at the lowest mode: alpha_c = beta e^(omega_min),
kbar = 1/(beta e^(omega_min)), theta = e^(-2 omega_min). So beta^2 kbar/alpha_c = e^(-2 omega_min) and (FC-seed)_a reads
omega_min >= K_a. But omega_min = 2 asinh(sin(pi/(24a))) < pi/(12a) < 0.27/a, and K_a > 16/a. So FP fails (FC-seed)_a for
every a, by a factor above 59 (check 943's arithmetic). In the form of 4.2: FP has b omega_min < 2 pi at every box
side, against 384 + 72 log a. FP satisfies (FC)_theta with theta = e^(-2 omega_min) < 1 on every finite box, as the lead
note (a) says; it fails only the rate. Scope: FP is the Gaussian mode model of row 929, not compact Wilson U(1).

**4.4 SMALL-BOX and frozen groups.** Unchanged from row 941 with check 938's quantifiers. (FC-seed)_a contains a,
so a proof must use the box size. Frozen groups have no gradient form; (FC) is not defined for them.

**4.5 What (FC) is not (PROVED by row 941's own run plus one line).** (FC) and (GC) are sufficient conditions
only. Row 941 Run 4 has chains with a gap, hence hypercontractive on their finite state space, where (GC) is
false (double-well rotors, theta_GC = 9.5 and 1.06; GUIDE). So a failure of (FC) does not touch the seed. The
entropy form that IS necessary: for a self-adjoint Markov operator K on L^2(nu) with ||K f||_b <= ||f||_a, 1 < a < b,
  Ent_nu(K g) <= (a/b) Ent_nu(g)   for every density g.
Proof. Put u = K g, psi = log u, r = 1/a. Jensen: e^(r K psi) <= K e^(r psi). So E e^((b/a) K psi) <= E (K u^(1/a))^b
<= (E u)^(b/a) = 1. The entropy inequality E[g phi] <= Ent(g) + log E e^phi with phi = (b/a) K psi, and
E[g K psi] = E[u log u] = Ent(u), give the claim. QED
With (HC-vac)_alpha and its dual, K = P^(2m), a = 1 + e^(-2 alpha m), b = 1 + e^(2 alpha m), a/b = e^(-2 alpha m):
  (EC-nec):  (HC-vac)_alpha  implies  Ent_nu(P^(2m) g) <= e^(-2 alpha m) Ent_nu(g)  for every m >= 1.
So entropy contraction is necessary for the seed route, and Fisher-information contraction is not.

## Step 5: the bridge between two slices (about 09:03Z). Theorem BR: PROVED implication, by hand

Idea. Row 941 (A7) used one mid-slice variable. Here the whole segment between two slices is used: the kernel
e^(beta <x, w>) on M x M is the heat kernel of R^N at time 1/beta. So one step of the slice chain is an ambient
Brownian motion of duration 1/beta, conditioned at both ends. Entropy and L^p norms can be differentiated along it.
This gives (HC-vac) directly. (LSI-vac), (FC), (C1-av), (COV), (SG-step) and (SC) do not occur.

**5.1 Objects.** g_s(v) := (2 pi s)^(-N/2) e^(-|v|^2/(2s)) on R^N. For 0 < s <= 1/beta and y in R^N:
  h_s(y) := integral over M of g_s(y - w) m(dw).
For 0 < s < 1/beta put s' := 1/beta - s and nu_s(dy) := Z^(-1) h_s(y) h_(s')(y) dy on R^N, Z := integral over M of h_(1/beta) dm.
Facts (each one line):
- (B1) On M x M, g_(1/beta)(x - w) = kap e^(beta <x, w>), kap := (beta/2 pi)^(N/2) e^(-beta L) (|x|^2 = |w|^2 = L). So for x in M:
  h_(1/beta)(x) = kap lambda_0 e^(V(x)/2) Omega(x), nu(dx) = h_(1/beta)(x) m(dx)/Z, and
  P_0 f(x) = h_(1/beta)(x)^(-1) integral of g_(1/beta)(x - w) f(w) m(dw).
- (B2) h_s is smooth and positive, d/ds h_s = (1/2) Laplacian h_s, and g_s * h_t = h_(s+t). The integral of h_s h_(s') dy
  is Z for every s (semigroup property). So nu_s is a probability density, and nu_s = nu_(s') (symmetry).
- (B3) nu_s is the law of y = (1 - lam) U_0 + lam U_1 + (lam (1 - lam)/beta)^(1/2) xi, with lam = beta s, (U_0, U_1) two
  consecutive slices of the vacuum chain (law J of row 941 (A1)) and xi a standard Gaussian of R^N, independent.
  (The density of (x, y, w) is m(dx) g_s(x - y) g_(s')(y - w) m(dw) dy/Z; complete the square in y.)
- (B4) -log nu_s(y) = |y|^2/(2s) + |y|^2/(2s') - Lambda(y/s) - Lambda(y/s') + const, Lambda the convex function of row 941 (A2).
  At s = 1/(2 beta) this is the mid-slice law eta of (A7).
- (B5) The gauge group acts on R^N by orthogonal maps that preserve M and m. So h_s and nu_s are gauge invariant.

**5.2 Theorem BR.** Let 0 < eps < 1/(2 beta) and let alpha: [eps, 1/beta - eps] -> [0, infinity) be piecewise
continuous. Assume, for every s in that interval:
  (LSI-br)_s: Ent_(nu_s)(phi^2) <= (2/alpha_s) integral of |grad phi|^2 d nu_s
  for every gauge-invariant phi in C^1(R^N) with delta <= phi <= 1/delta for some delta > 0 and bounded gradient.
Put A := integral over [eps, 1/beta - eps] of alpha_s ds. Then for gauge-invariant f and 1 < p < infinity:
  ||P f||_(L^q(nu)) <= ||f||_(L^p(nu)),   q := 1 + (p - 1) e^A.
Consequently (HC-vac)_alpha holds with alpha = A/2: ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-A m), for every integer m >= 0.

Proof. It is enough to take f continuous, gauge invariant, delta <= f <= 1/delta (then |P f| <= P |f| and density).
(i) The flow. For 0 <= s < 1/beta put N_s(y) := integral over M of g_(s')(y - w) f(w) m(dw) and u_s := N_s/h_(s').
N_s and h_(s') solve the backward heat equation d/ds phi = -(1/2) Laplacian phi. So
  d/ds u = -(1/2) Laplacian u - grad log h_(s') . grad u,   delta <= u_s <= 1/delta,   u_0 = P_0 f on M (by (B1)).
u_s is gauge invariant by (B5). grad log h_(s')(y) = (E[w | y] - y)/s' with |E[w | y]| <= L^(1/2), so all derivatives of u_s
grow at most polynomially, locally uniformly in s in (0, 1/beta), and h_s h_(s') has Gaussian tails. Differentiation
under the integral and integration by parts below are therefore legitimate.
(ii) The derivative. For a C^1 function q(s) > 1 put F(s) := integral of u_s^q(s) d nu_s. Then
  F'(s) = q' integral of u^q log u d nu_s + (1/2) q (q - 1) integral of u^(q-2) |grad u|^2 d nu_s.
Computation. Z F = integral of u^q h_s h_(s') dy. Three terms: (a) q' integral of u^q log u h_s h_(s');
(b) q integral of u^(q-1) (d/ds u) h_s h_(s'); (c) (1/2) integral of u^q (h_(s') Laplacian h_s - h_s Laplacian h_(s')).
(c) = -(1/2) integral of grad(u^q) . (h_(s') grad h_s - h_s grad h_(s')).
(b) = -(1/2) integral of (Laplacian u) q u^(q-1) h_s h_(s') - integral of grad(u^q) . (grad h_(s')) h_s
    = (1/2) q (q - 1) integral of u^(q-2) |grad u|^2 h_s h_(s') + (1/2) integral of grad(u^q) . (h_(s') grad h_s + h_s grad h_(s'))
      - integral of grad(u^q) . (grad h_(s')) h_s
    = (1/2) q (q - 1) integral of u^(q-2) |grad u|^2 h_s h_(s') + (1/2) integral of grad(u^q) . (h_(s') grad h_s - h_s grad h_(s')).
The last term cancels (c).
(iii) Gross's step. d/ds log ||u_s||_(L^q(s)(nu_s)) = (q F)^(-1) [ (q'/q) Ent_(nu_s)(u^q) + (1/2) q (q - 1) integral of u^(q-2) |grad u|^2 d nu_s ].
With phi := u^(q/2): the last integral is (4/q^2) integral of |grad phi|^2 d nu_s >= (2 alpha_s/q^2) Ent_(nu_s)(u^q) by (LSI-br)_s.
Choose q' = -alpha_s (q - 1), that is q(s) - 1 = (p - 1) exp(integral over [s, 1/beta - eps] of alpha). Then the bracket is
at least (Ent/q)(q' + (q - 1) alpha_s) = 0. So s -> ||u_s||_(L^q(s)(nu_s)) is non-decreasing on [eps, 1/beta - eps].
(iv) The ends. K(x, dy) := g_eps(x - y) h_(1/beta - eps)(y) dy/h_(1/beta)(x) is a probability kernel from M to R^N, with
u_0 = K u_eps and nu K = nu_eps (by (B1), (B2)). Jensen: ||u_0||_(L^q(nu)) <= ||u_eps||_(L^q(nu_eps)). In the same way
u_(1/beta - eps)(y) = integral of f(w) g_eps(y - w) m(dw)/h_eps(y), and this kernel maps nu_(1/beta - eps) to nu. Jensen:
||u_(1/beta - eps)||_(L^p) <= ||f||_(L^p(nu)).
(v) For P^m apply the one-step bound m times with p_k - 1 = e^(-A (m - k)): q' = p_0 = 1 + e^(-A m), p_m = 2. QED

**5.3 Corollaries (same proof; PROVED implications).**
- (BR-gap) If Var_(nu_s)(phi) <= (1/gam_s) integral of |grad phi|^2 d nu_s for gauge-invariant phi, then
  ||P f||_2^2 <= exp(-integral of gam_s ds) ||f||_2^2 for gauge-invariant f of nu-mean zero. So
  E_1 >= (1/2) integral over (0, 1/beta) of gam_s ds.   (Take q = 2 constant in (ii): F' = integral of |grad u|^2 d nu_s >= gam_s F.)
- (BR-ent) Under the hypothesis of Theorem BR: Ent_nu(P g) <= e^(-A) Ent_nu(g) for gauge-invariant densities g.
  (Step 4.5 with K = P, a = p, b = 1 + (p - 1) e^A, and p -> infinity.)
- (BR-loss; ARGUED, not used below) With g_s := d(mu_s)/d(nu_s), mu_s the law at time s of the bridge started from
  g nu: d/ds Ent_(nu_s)(g_s) = -(1/2) I_s, I_s := integral of |grad g_s|^2/g_s d nu_s. So the one-step entropy loss is
  (1/2) integral over (0, 1/beta) of I_s ds. In this language (C1-av) reads integral of I_s ds <= I_0/alpha_c, and (FC) reads
  I_(1/beta) <= theta I_0: two statements on the Fisher profile s -> I_s. That profile is not monotone without a
  convexity bound. (LSI-br) asks I_s >= 2 alpha_s Ent_(nu_s)(g_s) at each s instead, and this is what Gross's step uses.

**5.4 Checks by hand.**
- One Gaussian mode (flat model of rows 931, 940, 941; m ~ e^(-c w^2/2) dw with c = beta (e^omega - 1), from
  precision(pi_x) = beta + c = beta e^omega). h_s is Gaussian with precision c/(1 + c s). So nu_s is Gaussian with
  precision A_s = c/(1 + c s) + c/(1 + c s'), and alpha_s = gam_s = A_s. Integral over (0, 1/beta) of c/(1 + c s) ds
  = log(1 + c/beta) = omega. So A = 2 omega: Theorem BR returns alpha = omega (Nelson's exponent), (BR-gap) returns
  E_1 >= omega, (BR-ent) returns e^(-2 omega). All three are the exact values. At s = 1/(2 beta): A_s = 4 beta tanh(omega/2),
  the precision of eta in row 941 (A7).
- Normalisation. The generator in (i) is (1/2) Laplacian + drift, and the rate in (iii) is alpha_s for LSI in the
  form Ent(phi^2) <= (2/alpha) integral |grad phi|^2, for which N(0, 1/A) has alpha = A. The Gaussian check fixes both.
- Free rotor chain on the circle, large beta (asymptotic check). nu is uniform on S^1 in R^2. nu_s is radial,
  within O(beta^(-1/2)) of the unit circle, and its Poincare constant on the first angular mode is 1 + O(1/beta).
  (BR-gap) gives E_1 >= (1/(2 beta))(1 + o(1)); the truth is -log(I_1(beta)/I_0(beta)) = 1/(2 beta) + O(beta^(-2)). Sharp to
  leading order.

**5.5 Fact tests of (LSI-br) with the seed rate.** The seed needs A/2 >= K_a on B = (24a)^3 (Step 4.1 form:
(1/2) integral over (0, 1/beta) of alpha_s ds >= (C_beta(x_*) + 3 log a)/(a - 2)).
- FT-U1 (FP photon sector): A/2 = omega_min < 0.27/a. Fails for every a by the factor above 59, as it must.
- SMALL-BOX: A/2 <= (1/(2 beta)) sup_s alpha_s. Consistent with a rate that vanishes as beta grows at fixed lattice
  size, if sup_s alpha_s stays bounded there (not proved).
- Double wells that one kinetic step jumps (ARGUED; this is where (GC) and (FC) are false, row 941 Run 4). By (B3),
  nu_s for s in the middle third of (0, 1/beta) is the two-slice average smoothed by a Gaussian of variance at
  least 2/(9 beta). Two wells of nu closer than that width merge in nu_s, so gam_s is of order one there, and
  (BR-gap) gives a gap of order one over 3 beta times that constant. Near s = 0 the constant can be small; the
  theorem only needs alpha_s >= 0 there. So the bridge form does not have the defect of (GC). A GUIDE run of
  this claim is Step 6.
- A ceiling if gauge invariance is dropped (PROVED). For a linear phi(y) = <z, y>: Var_(nu_s)(phi) = v_s |z|^2 with
  v_s = (1 - 2 lam (1 - lam)(1 - tau))/4 + lam (1 - lam)/beta, tau := E_J <x_l, w_l> (the mean time-like plaquette), by (B3) and
  Elitzur's argument of row 941 (A5) applied to the pair (U_0, U_1): E[x_l (x) w_l'] = 0 for l != l', and
  E[x_l (x) w_l] = (tau/4) Id_4 because it commutes with SO(4). tau >= 0 since T_0 >= 0. So for beta >= 2,
  v_s >= 1/8 + 1/(4 beta), and a Theorem BR for ALL functions cannot give more than A/2 <= 4/(beta + 2): 0.93 at
  beta 2.3 and 0.87 at 2.6. Linear functions are not gauge invariant, so this does not cap Theorem BR as stated.
  It shows that the restriction to gauge-invariant phi in (LSI-br) carries weight: without it the route needs
  K_a <= 0.93, that is a >= 32 at beta 2.3 (K_30 = 0.936, K_32 = (16 + 10.40)/30 = 0.880).
- Method ceiling carried over (row 941 ceiling (ii), PROVED there): nu_s is not log-concave for beta > 2 (at y = 0,
  Elitzur). So (LSI-br) cannot come from the Bakry-Emery criterion on R^N in the window. It needs an LSI for a
  non-convex measure.

**5.6 Direct attack on (GC) and (FC): three stages, where each stops (written 09:11Z).**
Stage 1, (GC) for a power of P (Lemma MS; PROVED implication, group-blind). Assume kbar_h < infinity (row 941 Step 4) and the
averaged one-step Poincare bound (P1-av): E_nu Var_(pi_x)(f) <= E_nu|grad f|^2/gamma_c. Put kappa_W^2 := beta^2 kbar_h/gamma_c
(no smallness is assumed). Then for every n >= 0 and gauge-invariant f:
  E_nu|grad P^(n+1) f|^2 <= kappa_W^2 r_1^(2n) E_nu|grad f|^2.
Proof. (A3) and Cauchy-Schwarz give |grad P h(x)|^2 <= beta^2 kbar_h Var_(pi_x)(h), and E_nu Var_(pi_x)(h) = ||h||^2 - ||P h||^2.
With h = P^n f: E_nu|grad P^(n+1) f|^2 <= beta^2 kbar_h <f, P^(2n)(1 - P^2) f>. P >= 0 has spectrum in [0, r_1] off the
constants, and p^(2n)(1 - p^2) <= r_1^(2n)(1 - p^2) there. So the right side is at most beta^2 kbar_h r_1^(2n) E_nu Var_(pi_x)(f);
then (P1-av). QED
Reading. The linearised statement (GC) holds for P^k with theta < 1 as soon as k - 1 > log(kappa_W)/E_1. So (GC) contains
the gap E_1 and two one-step constants, and nothing else. Its failure for one step (double wells) is a defect of
the one-step gradient form, not of the chain. Stop: the nonlinear analogue is circular. With row 931 Theorem E
step (iii), I(P^(n+1) g) <= 2 sigma^2 Ent_nu(P^n g), and to return to I(g) one needs (LSI-vac) itself.
Stage 2, (GC) along the bridge (identity PROVED; the estimate it needs is OPEN). For u_s of 5.2 (i) put
G(s) := integral of |grad u_s|^2 d nu_s. Then d/ds ||u_s||^2_(L^2(nu_s)) = G(s), so ||f||^2 - ||P f||^2 = integral over (0, 1/beta) of G, and
  G'(s) = integral of |Hess u_s|^2 d nu_s + (2/s') G(s) - (2/s'^2) E[ Var(<grad u_s(y_s), w> | y_s) ],
because (d/ds + L_s)|grad u|^2 = |Hess u|^2 + 2 Hess(-log h_(s'))(grad u, grad u) and Hess(-log h_(s'))(y) = (Id - Cov(w | y_s = y)/s')/s'.
(GC) asks G to grow from s = 0 to s = 1/beta by the factor 1/theta. So (GC) follows from an AVERAGED bound on the
conditional variance of the next slice in the direction of grad u_s:
  (COV-dir): E[ Var(<grad u_s(y_s), w> | y_s) ] <= k_s G(s), with integral of (2/s')(1 - k_s/s') ds >= log(1/theta).
One Gaussian mode: Var(w | y_s) = s'/(1 + c s'), the integral is 2 omega, theta = e^(-2 omega): exact. Stop: (COV-dir) is
group-blind and unproved; near s' = 0 it needs the tangential structure of M (there (A3) is the exact form).
I did not find a way to bound the conditional variance for SU(2) in the window. Every sup form of it is capped by
Elitzur's value 1/4 at zero field (row 941 (A5)).
Stage 3, entropy instead of Fisher information: Theorem BR (5.2). It removes (FC), and it moves the SU(2) input to
(LSI-br). Stop: (LSI-br) for SU(2) on the seed box. Not attempted beyond the fact tests of 5.5; reasons in Step 7.

**5.7 The property that the Gaussian rival lacks, at the exact step (PROVED for the named step only).** In FP the
functions that defeat the rate are the linear ones, phi(y) = <z, y> with z a smooth transverse wave:
Var_(nu_s)(phi)/|z|^2 = 1/A_s(omega) is unbounded as omega -> 0. For SU(2), by 5.5 (Elitzur for the pair of slices),
every linear function has Var_(nu_s)(phi)/|z|^2 = v_s <= 1/4 + 1/(4 beta), on every box; and no linear function is gauge
invariant. The property is: the centre element -1 acts on one link alone. FP has no such symmetry. Compact
Wilson U(1) has it too, so this step does not separate SU(2) from compact U(1); for gauge-invariant functions
of degree two and more nothing is proved here, for either group. The lowest gauge-invariant polynomials of the
bridge field are |y_l|^2 (one link) and the plaquette quartic Re(y_1 y_2 conj(y_3) conj(y_4)).

**5.8 Relation to row 936.** Its Propositions Q and RARE-P (read: statements only, `gap-cuttyp-max.md` 268-283, 344-362,
423-428) bound an odd-sector Poincare constant of a cut law by an even gap plus a rarity input. For f odd under
a cut flip J, (GC) and (BR-gap) are one-step forms of (TYP-1). J acts on R^N by a sign change of coordinates that
preserves M and m (V and Omega are J-invariant), so nu_s is J-invariant and (LSI-br), (PI-br) split into J-even and J-odd parts. I did not transfer
RARE-P to nu_s; no implication between the two rows is proved here.

## Step 6: GUIDE run on the flat line chain (criteria written 09:06Z, before the run)

Purpose. Guard Theorem BR against an error of normalisation, and test the double-well claim of 5.5. Refute or
guide only. Model: x in R on a grid, T_0(x, w) = e^(-V(x)/2) e^(-beta (x - w)^2/2) e^(-V(w)/2), the flat chain of rows
931, 940 and 941. P, nu, r_1, theta_GC as in row 941 Run 4. m has density psi = e^(-V/2) Omega; h_s = g_s * psi;
nu_s ~ h_s h_(1/beta - s); gam_s := Poincare constant of nu_s (second eigenvalue of the stiffness problem).
The integral over (0, 1/beta) is a midpoint rule with 40 nodes. Script: `/tmp/gap-fc-947/scripts/br_guide.py`
(not committed; its full text is short and is reproduced at the end of this step).
Criteria:
- K1: r_1^2 <= exp(-integral of gam_s ds), within 2 percent of the exponent. This is (BR-gap). A violation means an
  error in Theorem BR or in the code; then stop and re-derive.
- K2: Gaussian V: equality within 1 percent, both equal to e^(-2 omega).
- K3: where theta_GC >= 1 ((GC) false): report E_BR/E_1 with E_BR := (1/2) integral of gam_s ds. The claim "the bridge
  form does not have the defect of (GC)" is supported (GUIDE) iff E_BR/E_1 >= 0.25 in those cases, and refuted as a
  general claim by one case with theta_GC >= 1 and E_BR/E_1 < 0.05.
Cases: two Gaussians (beta 1, kappa 1; beta 2.3, kappa 0.5); double wells V = h (x^2 - a^2)^2 with
(beta, a, h) = (1, 0.5, 40), (1, 0.6, 60), (1, 1.0, 8), (1, 1.5, 4), (2.3, 0.33, 400), (2.3, 0.5, 100), (2.3, 0.8, 30).

## Step 7: the two-slice form, the smallest unproved inequality, and one test (written 09:20Z-09:30Z)

**7.1 Lemma J (PROVED given the Gaussian log-Sobolev inequality, Gross 1975, RECALLED, not rebuilt).** Let J be the
two-slice vacuum law on M x M (row 941 (A1)). Assume
  (LSI-J)_(alpha_J): Ent_J(Phi^2) <= (2/alpha_J) E_J[ |grad_x Phi|^2 + |grad_w Phi|^2 ]
for smooth Phi on M x M, bounded above and below, invariant under the gauge group acting on both slices at once
(tangential gradients). Then (LSI-br)_s holds with
  1/alpha_s <= lam (1 - lam)/beta + (1 - 2 lam (1 - lam))/alpha_J,   lam = beta s.
Proof. By (B3), given (x, w) the bridge point y is N(mu, sig^2 Id), mu = (1 - lam) x + lam w, sig^2 = lam (1 - lam)/beta.
Chain rule: Ent_(nu_s)(phi^2) = E_J[Ent(phi^2 | x, w)] + Ent_J(Psi), Psi(x, w) := E[phi(y)^2 | x, w].
First term: at most 2 sig^2 E_(nu_s)|grad phi|^2 (Gaussian log-Sobolev inequality). Second term: Psi is invariant
(the group acts by orthogonal maps and phi is invariant), so (LSI-J) applies to Psi^(1/2). For a tangent vector z
at x: z . grad_x Psi = (1 - lam) E[2 phi(y) grad phi(y) . z | x, w], so |grad_x Psi|^2 <= 4 (1 - lam)^2 Psi E[|grad phi|^2 | x, w]
(Cauchy-Schwarz), that is |grad_x Psi^(1/2)|^2 <= (1 - lam)^2 E[|grad phi|^2 | x, w]. The same in w with lam^2. Add. QED
The same proof with variances: 1/gam_s <= lam (1 - lam)/beta + (1 - 2 lam (1 - lam))/gam_J, gam_J the Poincare constant of J.

**7.2 Corollary BR-J (PROVED implication, given 7.1 and Theorem BR).** Put rho := beta/alpha_J and
Xi(rho) := integral over (0, 1) of d lam/(rho + (1 - 2 rho) lam (1 - lam)). Then (LSI-J)_(alpha_J) gives (HC-vac)_alpha with alpha = Xi(rho)/2.
(Let eps -> 0 in Theorem BR; A = Xi(rho).) Since lam (1 - lam) <= 1/4: Xi >= 1/rho if rho >= 1/2, and Xi >= 4/(1 + 2 rho) if rho <= 1/2. So
  alpha >= alpha_J/(2 beta)            if alpha_J <= 2 beta,
  alpha >= 2 alpha_J/(alpha_J + 2 beta)   if alpha_J >= 2 beta   (then alpha >= 1).
Closed form for rho < 1/2: Xi = 4 (1 - 4 rho^2)^(-1/2) artanh(((1 - 2 rho)/(1 + 2 rho))^(1/2)), so alpha = log(alpha_J/beta) + O(1) for large alpha_J.
The variance form: E_1 >= Xi(beta/gam_J)/2.
Checks in one Gaussian mode (J has precision matrix [[beta + c, -beta], [-beta, beta + c]], so alpha_J = gam_J = c = beta (e^omega - 1)):
omega = 3: rho = 0.0524, Xi/2 = 2.97 <= 3. omega = 0.5: Xi/2 >= (e^0.5 - 1)/2 = 0.324 <= 0.5. Small omega: Xi/2 -> (pi/4) omega.
Consistent, and sharp for large omega. FP: alpha_J = beta (e^(omega_min) - 1), so alpha <= 0.79 omega_min (1 + o(1)) < 0.22/a: fails the rate.
What 7.2 changes in the chain. Rows 931-941 used (LSI-vac) and (SG-step) (sup form; row 944: not automatic; row 950: (SC)).
7.2 uses one inequality for one fixed measure, with no supremum over a conditioning slice. (LSI-J) implies (LSI-vac)
with the same constant (functions of one slice). It is lossy: unlike Theorem BR it inherits every barrier of nu.

**7.3 The smallest unproved inequality (OPEN).** In decreasing strength; each implies the next; the last gives the seed.
  (LSI-J-seed)_a: on B = (24a)^3, one even a >= 30: (LSI-J) with alpha_J >= 2 beta K_a, K_a = (C_beta(x_*) + 3 log a)/(a - 2).
     (For a >= 30, K_a <= 1 at beta 2.3 to 2.6, and 7.2 gives alpha >= K_a.) At beta 2.3: alpha_J >= 3.3, 2.3, 1.4, 0.75 for a = 40, 60, 100, 200.
  (LSI-br-seed)_a: on the same box, gauge-invariant log-Sobolev constants alpha_s of the bridge marginals nu_s with
     (1/2) integral over (0, 1/beta) of alpha_s ds >= K_a.
  (HC-vac)_(K_a) on the same box, hence the seed X(a; (24a)^3) <= x_* (Proposition HC).
First instance (Poincare level): (PI-br-seed)_a, (1/2) integral of gam_s ds >= K_a. It gives E_1(B) >= K_a, which every route
through (HC-vac) needs (4.2).
Why this one and not (FC). (a) (FC), (GC) are not necessary and are false for jumpable double wells; entropy
contraction is necessary (4.5) and Theorem BR delivers it. (b) One input replaces (FC), (C1-av), (COV) and (SG-step)/(SC).
(c) It is exact in every Gaussian mode. (d) U(1)/FP fails it only through the rate, by the same factor above 59.
What is NOT achieved. Nothing here bounds alpha_J, alpha_s or gam_s for SU(2) at beta 2.3 to 2.6. That is a lower bound on
the mass gap at intermediate coupling on a box of side at least 720 (b E_1 >= 384 + 72 log a), and a log-Sobolev
form of it. I know no method that reaches it: the curvature criteria are capped below the window (row 941 and
5.5), the strong-coupling range is beta below 1/4 (row 931), and nu_s, J have no known local specification
(m contains Omega). Three group-blind attempts (5.6) stop at conditional-covariance bounds of the same kind.

**7.4 One test that could refute (LSI-J-seed) (not run).** For gauge-invariant Phi on two consecutive slices put
  R_J(Phi) := Var_J(Phi)/E_J[ |grad_x Phi|^2 + |grad_w Phi|^2 ].
(LSI-J) gives the Poincare bound R_J(Phi) <= 1/alpha_J. So one Phi with R_J(Phi) > 1/(2 beta K_a) refutes (LSI-J-seed)_a on the
measured box: thresholds at beta 2.3 are 0.31 (a = 40), 0.45 (a = 60), 0.72 (a = 100), 1.35 (a = 200). The run is a plain
4D Monte Carlo (no frozen slice): measure variances and link-gradient norms of slice observables, as row 946's
`den()` does for the denominators. Candidates: zero-momentum sums of space-like and time-like plaquettes,
winding lines and their cross-section sums, smeared loops, and the worst combination in their span (a generalised
eigenvalue, as row 946's zmvar). Scope: side-4 and side-6 boxes are not the seed box; a violation there refutes
(LSI-J) on that box only. All R_J well below the threshold proves nothing. For (LSI-br) the same test applies to
functions of y of (B3), with thresholds from U(F) := (1/2) integral of ds/R_s(F) < K_a.
Exactly solvable companion (not run): the one-plaquette chain. Compare E_1 (3.56 at beta 2.3, row 941 Run 3) with
Xi(beta/gam_J)/2 and with (1/2) integral of gam_s ds; both must be below E_1, and the gap between them measures the loss.
