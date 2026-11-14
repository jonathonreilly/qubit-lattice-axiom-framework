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

Plan as followed (recorded at the end): Steps 1-4 as planned. Step 5 became the bridge theorem (5.1-5.5), with the
direct attack on (GC) and (FC) in 5.6 and the named property in 5.7. Step 6 holds the GUIDE runs. Step 7 holds the
two-slice form, the smallest unproved inequality and the test. The Result is at the end.

## Status log

- Status: FINISHED 2026-11-14T09:59Z. The target (FC) is NOT proved; see Result at the end.
- 08:51Z file created. Nothing proved yet.
- about 08:58Z Steps 1-3 written below. Branch decision: row 946 did NOT refute (FC); so (FC) is attacked.
- about 09:00Z Step 4 written. 09:03Z Step 5 (Theorem BR) written. 09:06Z Step 6 criteria written; numeric lock held by row 950 (gap-sc-950) until 09:59Z at the latest; the run waits.
- (Clock times in this log are from `date -u`; the session started 08:51Z.)
- 09:34Z section 5.7 rewritten (Lemma INV; an earlier wording on the centre element was wrong and is removed). 09:43Z GUIDE Run 2 (rotor). 09:51Z-09:58Z rotor rerun with row 941's sign and GUIDE Run 3 (SU(2) boxes). 09:59Z Result updated. FINISHED 09:59Z.
- 09:11Z sections 5.6-5.8 written. 09:13Z Step 7 written. 09:16Z provisional Result written. 09:17Z GUIDE run of Step 6 done (lock acquired 09:17:34Z, released 09:17:36Z); results in Step 6.

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
  b E_1(B) >= 24 a K_a > 24 C_beta(x_*) + 72 log a   (24 C_beta is 384.0 at beta 2.3, C_beta being just below 16, and about 386.9 at 2.6).
So the seed, on this route, is one inequality for the dimensionless gap b E_1 at ONE box side b.

**4.3 FT-U1 against THAT statement (PROVED given the mode list of FP, read by check 943 at `gap-seam-max.md:88-116`).**
In the photon sector of FP every constant is attained at the lowest mode: alpha_c = beta e^(omega_min),
kbar = 1/(beta e^(omega_min)), theta = e^(-2 omega_min). So beta^2 kbar/alpha_c = e^(-2 omega_min) and (FC-seed)_a reads
omega_min >= K_a. But omega_min = 2 asinh(sin(pi/(24a))) < pi/(12a) < 0.27/a, and K_a > 16/a. So FP fails (FC-seed)_a for
every a, by a factor above 59 (check 943's arithmetic). In the form of 4.2: FP has b omega_min < 2 pi at every box
side, against about 384 + 72 log a. FP satisfies (FC)_theta with theta = e^(-2 omega_min) < 1 on every finite box, as the lead
note (a) says; it fails only the rate. Scope: FP is the Gaussian mode model of row 929, not compact Wilson U(1).

**4.4 SMALL-BOX and frozen groups.** Unchanged from row 941 with check 938's quantifiers. (FC-seed)_a contains a,
so a proof must use the box size. Frozen groups have no gradient form; (FC) is not defined for them.

**4.5 What (FC) is not (PROVED by row 941's own run plus one line).** (FC) and (GC) are sufficient conditions
only. Row 941 Run 4 has chains with a gap where (GC) is
false (double-well rotors on a finite grid, theta_GC = 9.5 and 1.06; GUIDE; a finite irreducible chain with a gap has
hypercontractive powers). So a failure of (FC) does not touch the seed. The
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
grow at most polynomially, locally uniformly in s in (0, 1/beta), and h_s h_(s') has Gaussian tails. Also
grad u_s(y) = Cov(w, f(w) | y_s = y)/s' is bounded, so phi = u_s^(q/2) is in the class of (LSI-br)_s. Differentiation
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
- Free rotor chain on the circle, large beta (asymptotic check; the GUIDE Run 2 of Step 6 agrees: ratio 0.998 at beta 8). nu is uniform on S^1 in R^2. nu_s is radial,
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
  (BR-gap) gives E_1 >= gam/(6 beta), with gam a lower bound for gam_s on the middle third. Near s = 0 the constant can be small; the
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
G(s) := integral of |grad u_s|^2 d nu_s. Then d/ds ||u_s||^2_(L^2(nu_s)) = G(s) on (0, 1/beta), so ||f||^2 - ||P f||^2 >= integral over (0, 1/beta) of G (Jensen at the two
ends as in 5.2 (iv); equality needs continuity at the ends, not written out), and
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

**5.7 The property that the Gaussian rival lacks, at the exact step (PROVED for degrees one and two only; rewritten 09:34Z).**
In FP the functions that defeat the rate are polynomials of low degree in the bridge field. Degree one:
phi(y) = <z, y> with z a smooth transverse wave has Var_(nu_s)(phi)/E|grad phi|^2 = 1/A_s(omega), unbounded as omega -> 0.
Degree two: phi = <z, y>^2 - const has ratio 1/(2 A_s(omega)) (Gaussian moments: Var = 2 v^2, E|grad phi|^2 = 4 v, v = 1/A_s).
For SU(2) on a box of side at least 3 (Lemma INV, PROVED): a polynomial of degree at most two on R^N is gauge
invariant only if it is c_0 + sum over links of c_l |y_l|^2.
Proof. The gauge map -1 at one site changes the sign of the six links at that site. A linear form <z, y> is
then invariant only if z_l = 0 for every link. For a quadratic form y^T Q y: two distinct links do not have the
same pair of end sites, so -1 at a site of one and not of the other gives Q_(l l') = 0; and Q_(l l) commutes with
the maps q -> g q h^(-1), which are all of SO(4), so it is a multiple of Id_4. QED
So gauge invariance removes every degree-one function and every degree-two function except the ultralocal
radial sums. For those, by (B3), Var(sum c_l |y_l|^2) is a sum of time-like plaquette covariances plus a local term,
and the ratio is bounded exactly when the time-like plaquette susceptibilities are (chi_t of 7.4 and its
versions at non-zero momentum).
What this does and does not give. It names the step: FP fails through functions of degree one and two that are
not gauge invariant for SU(2). It holds for compact Wilson U(1) too in degree one (the centre argument), so it
does not separate SU(2) from compact U(1). It proves nothing in degree four, where the first non-local
invariants appear (the plaquette quartic Re(y_1 y_2 conj(y_3) conj(y_4)); in perturbation theory: two-gluon
states). There a perturbative SU(2) box has soft functions (SMALL-BOX), so only an argument that uses the box
size can exclude them. I have none.

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

**Run (GUIDE; 09:17:34Z-09:17:36Z under the numeric lock, holder gap-fc-947, acquired after row 950 released it;
71 percent memory free; one thread, nice; peak RSS 206 MB; log `/tmp/gap-fc-947/logs/br_guide.log`, not committed).**
Grid [-8, 8], spacing 0.02. E_1 = -log r_1, E_BR = (1/2) integral of gam_s ds.

| case | r_1^2 | theta_GC | exp(-integral gam_s) | E_1 | E_BR | E_BR/E_1 | min gam_s | gam at mid | K1 |
|---|---|---|---|---|---|---|---|---|---|
| Gaussian, beta 1, kappa 1 | 0.14590 | 0.1459 | 0.14592 | 0.9624 | 0.9624 | 1.000 | 1.789 | 1.789 | PASS |
| Gaussian, beta 2.3, kappa 0.5 | 0.25000 | 0.2500 | 0.25001 | 0.6931 | 0.6931 | 1.000 | 3.067 | 3.067 | PASS |
| double well, beta 1, a 0.5, h 40 | 0.04116 | 0.1155 | 0.05230 | 1.5951 | 1.4753 | 0.925 | 2.142 | 2.666 | PASS |
| double well, beta 1, a 0.6, h 60 | 0.10666 | 13.76 | 0.15062 | 1.1191 | 0.9465 | 0.846 | 0.0746 | 2.079 | PASS |
| double well, beta 1, a 1.0, h 8 | 0.52432 | 39.34 | 0.59777 | 0.3228 | 0.2573 | 0.797 | 0.0083 | 0.757 | PASS |
| double well, beta 1, a 1.5, h 4 | 0.94657 | 5.9e5 | 0.95595 | 0.0275 | 0.0225 | 0.820 | 0.0000 | 0.098 | PASS |
| double well, beta 2.3, a 0.33, h 400 | 0.04978 | 0.6127 | 0.07009 | 1.5001 | 1.3290 | 0.886 | 1.748 | 5.893 | PASS |
| double well, beta 2.3, a 0.5, h 100 | 0.23110 | 6.723 | 0.29669 | 0.7325 | 0.6075 | 0.829 | 0.181 | 3.419 | PASS |
| double well, beta 2.3, a 0.8, h 30 | 0.77590 | 1238 | 0.81847 | 0.1269 | 0.1002 | 0.790 | 0.0002 | 0.809 | PASS |

Exact e^(-2 omega): 0.14590 (kappa 1) and 0.25000 (kappa 0.5).
Verdicts by the criteria written before the run.
- K1: PASS in all nine cases. (BR-gap) is not violated.
- K2: PASS. Both Gaussians return e^(-2 omega) to four digits, so the normalisation of Theorem BR (generator
  (1/2) Laplacian, duration 1/beta, rate alpha_s) is confirmed on this model.
- K3: (GC) is false (theta_GC >= 1) in five cases, with theta_GC from 6.7 to 5.9e5. In each of them E_BR/E_1 is
  between 0.79 and 0.85. The claim of 5.5 is supported: where the one-step gradient form fails, the bridge form
  keeps about four fifths of the true rate, and the small values of gam_s sit near the ends of (0, 1/beta) as argued.
What the run does not show. It is a one-variable flat model on a grid. It proves nothing about SU(2), about
log-Sobolev constants (only Poincare constants were computed), or about a box. The values of theta_GC above 1 are
grid numbers of an ill-conditioned form and are used only through "theta_GC >= 1".

Script (full text of `br_guide.py`, so that row 949 can rerun it under the lock; about 2 seconds):

```python
# GUIDE run for library/gap-fc-max.md Step 6 (row 947). Refutes or guides only; proves nothing.
# Flat line chain: T_0(x,w) = exp(-V(x)/2) exp(-beta (x-w)^2/2) exp(-V(w)/2) on a grid of R.
# Criteria (written before the run, also in the note):
#  K1: r_1^2 <= exp(-int_0^{1/beta} gam_s ds) up to 2 percent of the exponent (BR-gap). A violation = error in Theorem BR or code.
#  K2: Gaussian V: equality within 1 percent, and both equal exp(-2 omega).
#  K3: where theta_GC >= 1 (GC false), report E_BR/E_1 with E_BR = (1/2) int gam_s ds; "bridge form survives" iff E_BR/E_1 >= 0.25.
import sys, resource, numpy as np
from scipy.linalg import eigh
def run(beta, V, X=8.0, dx=0.02, ns=40):
    x = np.arange(-X, X + dx/2, dx); n = len(x)
    k = np.exp(-0.5*beta*(x[:, None]-x[None, :])**2)
    b = np.exp(-0.5*V(x))
    T = (b[:, None]*k*b[None, :])*dx
    lam, vec = np.linalg.eigh(T)
    lam0 = lam[-1]; Om = np.abs(vec[:, -1]); r1 = lam[-2]/lam0
    I = Om > 1e-9*Om.max(); xi = x[I]; Omi = Om[I]
    nu = Omi**2; nu /= nu.sum()*dx
    P = (T[np.ix_(I, I)]*Omi[None, :]/Omi[:, None])/lam0
    def stiff(dens):
        wmid = 0.5*(dens[1:]+dens[:-1]); m = len(dens)
        K = np.zeros((m, m)); idx = np.arange(m-1)
        K[idx, idx] += wmid/dx; K[idx+1, idx+1] += wmid/dx; K[idx, idx+1] -= wmid/dx; K[idx+1, idx] -= wmid/dx
        return K
    D = stiff(nu); A = P.T @ D @ P
    w = nu*dx
    th = eigh(A, D + np.outer(w, w), eigvals_only=True)[-1]
    psi = b*Om                                  # density of m on the full grid
    def h(s): return (np.exp(-0.5*(x[:, None]-x[None, :])**2/s)/np.sqrt(2*np.pi*s)*dx) @ psi
    S = 1.0/beta; integ = 0.0; gmin = 1e99; gmid = None
    for j in range(ns):
        s = (j+0.5)*S/ns
        d = h(s)*h(S-s); d /= d.sum()*dx
        J = d > 1e-12*d.max(); dj = d[J]
        g = eigh(stiff(dj), np.diag(dj*dx), eigvals_only=True)[1]
        integ += g*S/ns; gmin = min(gmin, g)
        if j == ns//2: gmid = g
    return r1, th, integ, gmin, gmid
cases = [("gauss b1 k1", 1.0, lambda x: 0.5*1.0*1.0*x**2), ("gauss b2.3 k0.5", 2.3, lambda x: 0.5*2.3*0.5*x**2),
         ("dw b1 a0.5 h40", 1.0, lambda x: 40*(x**2-0.25)**2), ("dw b1 a0.6 h60", 1.0, lambda x: 60*(x**2-0.36)**2),
         ("dw b1 a1.0 h8", 1.0, lambda x: 8*(x**2-1.0)**2), ("dw b1 a1.5 h4", 1.0, lambda x: 4*(x**2-2.25)**2),
         ("dw b2.3 a0.33 h400", 2.3, lambda x: 400*(x**2-0.1089)**2), ("dw b2.3 a0.5 h100", 2.3, lambda x: 100*(x**2-0.25)**2),
         ("dw b2.3 a0.8 h30", 2.3, lambda x: 30*(x**2-0.64)**2)]
print("case | r1^2 | theta_GC | exp(-int gam) | E_1 | E_BR | E_BR/E_1 | min gam_s | gam_mid | K1")
for name, beta, V in cases:
    r1, th, integ, gmin, gmid = run(beta, V)
    E1 = -np.log(r1); EBR = 0.5*integ
    k1 = "PASS" if 2*E1 >= integ*(1-0.02) else "FAIL"
    print(f"{name} | {r1**2:.5f} | {th:.4f} | {np.exp(-integ):.5f} | {E1:.4f} | {EBR:.4f} | {EBR/E1:.3f} | {gmin:.4f} | {gmid:.4f} | {k1}")
    if name.startswith("gauss"):
        kap = 1.0 if "k1" in name else 0.5
        om = np.arccosh(1+kap/2); print(f"   exact exp(-2 omega) = {np.exp(-2*om):.5f}")
print("peak RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
```

**Second GUIDE run, embedded geometry (criteria written 09:19Z, before the run).** The flat model has M = R^N, so it
does not exercise (B1)-(B3) (M inside R^N, the ends of the bridge). Model: row 941's rotor chain, the circle in R^2,
V(u) = h1 cos u + h2 cos 2u, kernel e^(beta cos(u - u')). nu_s is a density on R^2; gam_s is computed on a polar grid
(160 x 64 cells, finite volumes), 24 midpoint nodes in s. Script `/tmp/gap-fc-947/scripts/br_rotor.py`, not committed.
Criteria: K0, r_1^2 equals row 941's table (Run 1, 2) within 1 percent. K1', r_1^2 <= exp(-integral of gam_s ds) within
3 percent of the exponent in every case; a violation means an error in the embedded form of Theorem BR or in the
code. K3', in row 941's two double-well rotors ((1, 0, 4) and (2.3, 0, 1.5), where its theta_GC is 9.5 and 1.06) the
claim of 5.5 is supported iff E_BR/E_1 >= 0.25.
Cases (beta, h1, h2): (0.3, 0, 0), (1, 0, 0), (2.3, 0, 0), (8, 0, 0), (2.3, 1, 0.5), (4, 2, 1), (1, 0, 4), (2.3, 0, 1.5).

**Run 2 (GUIDE; 09:43:03Z-09:43:25Z under the numeric lock, holder gap-fc-947, after row 950 released it; 70 percent
memory free; one thread, nice; peak RSS 259 MB; log `/tmp/gap-fc-947/logs/br_rotor.log`, not committed).**

| (beta, h1, h2) | r_1^2 here | r_1^2 row 941 | exp(-integral gam_s) | E_1 | E_BR | E_BR/E_1 | min gam_s | gam at mid | K0 | K1' |
|---|---|---|---|---|---|---|---|---|---|---|
| (0.3, 0, 0) | 0.0220 | 0.0220 | 0.0276 | 1.9083 | 1.7950 | 0.941 | 0.893 | 0.893 | PASS | PASS |
| (1, 0, 0) | 0.1993 | 0.1993 | 0.2256 | 0.8066 | 0.7444 | 0.923 | 1.068 | 1.589 | PASS | PASS |
| (2.3, 0, 0) | 0.5496 | 0.5496 | 0.5623 | 0.2992 | 0.2878 | 0.962 | 1.029 | 1.498 | PASS | PASS |
| (8, 0, 0) | 0.8747 | 0.8747 | 0.8749 | 0.0670 | 0.0668 | 0.998 | 1.007 | 1.107 | PASS | PASS |
| (2.3, 1, 0.5), sign as coded here | 0.5230 | 0.1382 | 0.5353 | 0.3241 | 0.3125 | 0.964 | 1.142 | 1.609 | FAIL | PASS |
| (4, 2, 1), sign as coded here | 0.7400 | 0.1075 | 0.7427 | 0.1506 | 0.1487 | 0.988 | 1.016 | 1.300 | FAIL | PASS |
| (1, 0, 4), double well | 0.5362 | 0.5362 | 0.6165 | 0.3116 | 0.2419 | 0.776 | 0.0026 | 0.747 | PASS | PASS |
| (2.3, 0, 1.5), double well | 0.9086 | 0.9086 | 0.9203 | 0.0479 | 0.0415 | 0.867 | 0.039 | 0.340 | PASS | PASS |

Verdicts by the criteria written before the run.
- K0: PASS in six cases, FAIL in two. Cause (found after the run, by hand): a sign convention. This script uses the
  weight e^(-V) with V = +h1 cos u + h2 cos 2u. With both h1 and h2 non-zero the two signs are different models
  (u -> u + pi maps (h1, h2) to (-h1, h2), not to (-h1, -h2)); with one of them zero they agree, which is why the
  other six cases match row 941 to four digits. Row 941 calls (2.3, 1, 0.5) a one-well case, which is the sign
  V = -(h1 cos u + h2 cos 2u). So the two FAIL rows are valid cases of a different potential (minima at u = 2 pi/3
  and 4 pi/3), not row 941's. The rerun with the other sign is below.
- K1': PASS in all eight cases. (BR-gap) is not violated in the embedded geometry (M a circle in R^2).
- K3': in the two double wells of row 941 (its theta_GC 9.5 and 1.06), E_BR/E_1 = 0.78 and 0.87. Supported.
Rerun with row 941's sign (09:51:27Z, same lock session as Run 3 below; `br_rotor2.py` = `br_rotor.py` with the case
list replaced by (2.3, -1, -0.5) and (4, -2, -1); log `br_rotor2.log`):

| (beta, h1, h2) | r_1^2 here | r_1^2 row 941 | exp(-integral gam_s) | E_1 | E_BR | E_BR/E_1 | min gam_s | gam at mid | K0 | K1' |
|---|---|---|---|---|---|---|---|---|---|---|
| (2.3, -1, -0.5) | 0.1382 | 0.1382 | 0.1516 | 0.9895 | 0.9432 | 0.953 | 3.632 | 4.315 | PASS | PASS |
| (4, -2, -1) | 0.1075 | 0.1075 | 0.1098 | 1.1152 | 1.1044 | 0.990 | 8.170 | 8.170 | PASS | PASS |

So K0 holds in all eight of row 941's cases once the sign is matched, and K1' holds in all ten models run.
Reading (GUIDE). For free rotors the bridge bound is within 8 percent of the true rate at beta 0.3 to 2.3 and
within 0.2 percent at beta 8. So Theorem BR loses little in the embedded geometry. It proves nothing about SU(2)
on a box.

Script (full text of `br_rotor.py`; about 20 seconds):

```python
# GUIDE run 2 for library/gap-fc-max.md Step 6 (row 947): rotor chain on the circle in R^2. Refutes or guides only.
# Criteria K0, K1', K3' are in the note (written before the run).
import resource, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import eigsh
def run(beta, h1, h2, nu_=256, nr=160, nphi=64, ns=24):
    u = (np.arange(nu_)+0.5)*2*np.pi/nu_; du = 2*np.pi/nu_
    V = h1*np.cos(u)+h2*np.cos(2*u); b = np.exp(-0.5*V)
    T = b[:, None]*np.exp(beta*np.cos(u[:, None]-u[None, :]))*b[None, :]*du
    lam, vec = np.linalg.eigh(T); r1 = lam[-2]/lam[-1]; psi = b*np.abs(vec[:, -1])
    S = 1.0/beta; rmax = 1+6*np.sqrt(S/4); dr = rmax/nr; dphi = 2*np.pi/nphi
    r = (np.arange(nr)+0.5)*dr; phi = (np.arange(nphi)+0.5)*dphi
    wx, wy = np.cos(u), np.sin(u)
    def h(s, rr, pp):                      # h_s on a polar mesh (rr, pp arrays of the same shape)
        yx, yy = rr*np.cos(pp), rr*np.sin(pp)
        d2 = (yx[..., None]-wx)**2+(yy[..., None]-wy)**2
        return (np.exp(-0.5*d2/s)/(2*np.pi*s)) @ (psi*du)
    R, PH = np.meshgrid(r, phi, indexing="ij")
    Re, PHe = np.meshgrid(r[:-1]+dr/2, phi, indexing="ij")          # radial edges
    Ra, PHa = np.meshgrid(r, phi+dphi/2, indexing="ij")             # angular edges
    idx = np.arange(nr*nphi).reshape(nr, nphi)
    integ = 0.0; gmin = 1e99; gmid = None
    for j in range(ns):
        s = (j+0.5)*S/ns
        dens = lambda rr, pp: h(s, rr, pp)*h(S-s, rr, pp)
        d = dens(R, PH); cut = 1e-12*d.max(); keep = d > cut
        M = (d*R*dr*dphi)
        we = dens(Re, PHe)*Re*dphi/dr; wa = dens(Ra, PHa)*dr/(Ra*dphi)
        i1 = idx[:-1, :].ravel(); i2 = idx[1:, :].ravel(); ce = we.ravel()
        ok = keep[:-1, :].ravel() & keep[1:, :].ravel(); i1, i2, ce = i1[ok], i2[ok], ce[ok]
        a1 = idx.ravel(); a2 = np.roll(idx, -1, axis=1).ravel(); ca = wa.ravel()
        ok = keep.ravel() & np.roll(keep, -1, axis=1).ravel(); a1, a2, ca = a1[ok], a2[ok], ca[ok]
        I = np.concatenate([i1, a1]); Jx = np.concatenate([i2, a2]); C = np.concatenate([ce, ca])
        n = nr*nphi
        K = sp.coo_matrix((np.concatenate([C, C, -C, -C]), (np.concatenate([I, Jx, I, Jx]), np.concatenate([I, Jx, Jx, I]))), shape=(n, n)).tocsr()
        kk = np.flatnonzero(keep.ravel()); K = K[kk][:, kk]; Mk = sp.diags(M.ravel()[kk])
        scale = Mk.diagonal().sum()
        ev = eigsh(K/scale, k=3, M=Mk/scale, sigma=-1e-3, which="LM", return_eigenvectors=False)
        g = np.sort(ev)[1]
        integ += g*S/ns; gmin = min(gmin, g)
        if j == ns//2: gmid = g
    return r1, integ, gmin, gmid
ref = {(0.3,0,0):0.0220, (1,0,0):0.1993, (2.3,0,0):0.5496, (8,0,0):0.8747, (2.3,1,0.5):0.1382, (4,2,1):0.1075, (1,0,4):0.5362, (2.3,0,1.5):0.9086}
print("case | r1^2 | row941 r1^2 | exp(-int gam) | E_1 | E_BR | E_BR/E_1 | min gam_s | gam_mid | K0 | K1'")
for (beta, h1, h2), rr in ref.items():
    r1, integ, gmin, gmid = run(beta, h1, h2)
    E1 = -np.log(r1); EBR = 0.5*integ
    k0 = "PASS" if abs(r1**2/rr-1) < 0.01 else "FAIL"; k1 = "PASS" if 2*E1 >= integ*(1-0.03) else "FAIL"
    print(f"({beta},{h1},{h2}) | {r1**2:.4f} | {rr:.4f} | {np.exp(-integ):.4f} | {E1:.4f} | {EBR:.4f} | {EBR/E1:.3f} | {gmin:.4f} | {gmid:.4f} | {k0} | {k1}", flush=True)
print("peak RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
```

## Step 7: the two-slice form, the smallest unproved inequality, and one test (written 09:13Z)

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
Consistent, and sharp for large omega. FP: alpha_J = beta (e^(omega_min) - 1), so the output of 7.2 is about 0.79 omega_min < 0.22/a (the true rate of FP is omega_min < 0.27/a): it fails the rate.
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
the mass gap at intermediate coupling on a box of side at least 720 (b E_1 > 24 C_beta + 72 log a, about 384 + 72 log a), and a log-Sobolev
form of it. I know no method that reaches it: the curvature criteria are capped below the window (row 941 and
5.5), the strong-coupling range is beta below 1/4 (row 931), and nu_s, J have no known local specification
(m contains Omega). Three group-blind attempts (5.6) stop at conditional-covariance bounds of the same kind.

**7.4 One test that could refute (LSI-J-seed) (run here on small boxes only: Run 3 below; not run on the seed box).** For gauge-invariant Phi on two consecutive slices put
  R_J(Phi) := Var_J(Phi)/E_J[ |grad_x Phi|^2 + |grad_w Phi|^2 ].
(LSI-J) gives the Poincare bound R_J(Phi) <= 1/alpha_J. So one Phi with R_J(Phi) > 1/(2 beta K_a) refutes (LSI-J-seed)_a on the
measured box: thresholds at beta 2.3 are 0.31 (a = 40), 0.45 (a = 60), 0.72 (a = 100), 1.35 (a = 200). The run is a plain
4D Monte Carlo (no frozen slice): measure variances and link-gradient norms of slice observables, as row 946's
`den()` does for the denominators. Candidates: zero-momentum sums of space-like and time-like plaquettes,
winding lines and their cross-section sums, smeared loops, and the worst combination in their span (a generalised
eigenvalue, as row 946's zmvar). Scope: side-4 and side-6 boxes are not the seed box; a violation there refutes
(LSI-J) on that box only. All R_J well below the threshold proves nothing. For (LSI-br) the same test applies to
functions of y of (B3), with thresholds from U(F) := (1/2) integral of ds/R_s(F) < K_a.
Simplest instance (PROVED inequality; measured on small boxes in Run 3 below). Phi := sum over links of t_l, t_l := <x_l, w_l>, the
time-like plaquette in temporal gauge. Phi is gauge invariant, |grad_(x_l) Phi|^2 = |grad_(w_l) Phi|^2 = 1 - t_l^2, and
Var_J(Phi) = L chi_t with chi_t := sum over l' of Cov_J(t_l, t_l'), the time-like plaquette susceptibility inside one time
layer. So R_J(Phi) = chi_t/(2 (1 - E t^2)), and
  (LSI-J)_(alpha_J)  implies  chi_t <= 2 (1 - E t^2)/alpha_J;   (LSI-J-seed)_a  implies  chi_t <= (1 - E t^2)/(beta K_a) <= 1/(beta K_a).
A measured chi_t above (1 - E t^2)/(beta K_a) on the seed box refutes (LSI-J-seed)_a. Both sides are standard lattice
observables. It also caps the OUTPUT of Corollary BR-J (not the true rate): alpha_J <= 2 (1 - E t^2)/chi_t, so the output is at most Xi(beta chi_t/(2 (1 - E t^2)))/2.
Small-box run of this test (GUIDE; criteria written 09:21Z, before the run). Lattice and updates of row 946
(`library/guide/lane946/fct.py`: open time 13 slices, K = 6, heat bath plus 2 overrelaxation passes, transported
slices); the two middle slices play (x, w), so the law is the open-time J_K, not J. Functions: f1 = sum of
space-like plaquettes of x, f2 = the same for w, f3 = sum of the time-like plaquettes t_l between them (all at zero
momentum), and the worst combination in their span (top generalised eigenvalue of covariance against the gradient
Gram matrix; exact tangent gradients). Runs: 4^3 at beta 2.3 and 2.6, 6^3 at beta 2.3; 16 (8 on 6^3) independent
chains, 250 measurements each, 4 sweeps apart; jackknife over chains. Script `/tmp/gap-fc-947/scripts/rj_guide.py`,
not committed. Verdict rules: REFUTES (LSI-J-seed)_a on the run's box iff some R_J - 3 err > 1/(2 beta K_a) (at beta 2.3:
0.31, 0.45, 0.72, 1.35 for a = 40, 60, 100, 200). Otherwise NOT REFUTED on that box, which proves nothing; then the
run reports the cap alpha_J <= 1/max R_J for that box. Sanity only: E c_p near 0.60 at beta 2.3 (recalled value).
Run 3 (GUIDE; lock holder gap-fc-947-rj, 09:51:27Z-09:58:11Z; 71 percent memory free; one thread, nice; peak RSS
143 MB; logs `/tmp/gap-fc-947/logs/rj_L4_b2.3.log`, `rj_L4_b2.6.log`, `rj_L6_b2.3.log`, not committed). A first batch at 09:43Z
ran only its smoke test (3^3, 4 measurements, exit 0): the three production commands failed on a shell
word-splitting error in the runner and produced no number. The batch below is the corrected rerun, same script.

| quantity | 4^3, beta 2.3 | 6^3, beta 2.3 | 4^3, beta 2.6 |
|---|---|---|---|
| R_J(f1), space-like sum on x | 0.0573 +- 0.0010 | 0.0627 +- 0.0017 | 0.0409 +- 0.0008 |
| R_J(f2), space-like sum on w | 0.0574 +- 0.0015 | 0.0581 +- 0.0021 | 0.0407 +- 0.0008 |
| R_J(f3), time-like sum | 0.1545 +- 0.0041 | 0.1519 +- 0.0033 | 0.1108 +- 0.0013 |
| top of the 3-span | 0.1547 +- 0.0041 | 0.1525 +- 0.0034 | 0.1117 +- 0.0011 |
| one space-like plaquette, Var(c_p)/(4 (1 - E c_p^2)) | 0.0419 | 0.0424 | 0.0335 |
| one time-like plaquette, Var(t)/(2 (1 - E t^2)) | 0.0844 | 0.0848 | 0.0673 |
| chi_t | 0.1677 +- 0.0044 | 0.1652 +- 0.0036 | 0.1075 +- 0.0012 |
| E c_p, E t, E t^2 | 0.6058, 0.6049, 0.4575 | 0.6030, 0.6031, 0.4560 | 0.6711, 0.6706, 0.5149 |

Errors: jackknife over 16 (6^3: 8) independent chains; lag-1 autocorrelation of the time-like sum 0.016, 0.028, 0.006.
Sanity: E c_p = 0.603 to 0.606 at beta 2.3, against the recalled 0.60. Internal check: chi_t/(2 (1 - E t^2)) = 0.1545 at
4^3, beta 2.3, equal to the directly measured R_J(f3).
Verdict by the rules written before the run. The largest R_J + 3 err is 0.167, 0.163 and 0.115. Every threshold
1/(2 beta K_a) for a >= 40 is at least 0.31 at beta 2.3 and 0.27 at beta 2.6. So (LSI-J-seed)_a is NOT REFUTED on these
boxes, which proves nothing. Readings (GUIDE): (a) the worst function in the span is the time-like plaquette sum;
(b) no growth from side 4 to side 6 at beta 2.3 (0.155, 0.152); (c) caps for these boxes: alpha_J <= 6.5 (beta 2.3) and
9.0 (beta 2.6), so the output of Corollary BR-J is at most Xi(beta/alpha_J)/2 = 1.24 and 1.40 (closed form of 7.2);
with K_22 = 1.26 and K_24 = 1.16 at beta 2.3: if the same cap held on the seed box, Corollary BR-J could not deliver K_a below a = 24;
(d) the necessary condition chi_t <= (1 - E t^2)/(beta K_a) reads chi_t <= 0.33 at a = 40, beta 2.3, against 0.17 measured.
Limits: the law is the open-time J_K with K = 6 on boxes of side 4 and 6, not J on the seed box; three test
functions only; a Poincare ratio bounds alpha_J from above, never from below.

Script (full text of `rj_guide.py`; it imports row 946's `fct.py` by path; run as
`python3 rj_guide.py --fct <path to lane946/fct.py> --L 4 --beta 2.3 --B 16`, about 2 minutes):

```python
# GUIDE run 3 for library/gap-fc-max.md Step 7.4 (row 947): Poincare ratios R_J of the two-slice law for
# zero-momentum plaquette sums, SU(2) Wilson, small boxes, open time (row 946's lattice and updates).
# Refutes or guides only. Criteria are in the note (written before the run).
import sys, importlib.util, resource, argparse, numpy as np
from scipy.linalg import eigh
ap = argparse.ArgumentParser(); ap.add_argument("--fct"); ap.add_argument("--L", type=int); ap.add_argument("--K", type=int, default=6)
ap.add_argument("--beta", type=float); ap.add_argument("--B", type=int, default=16); ap.add_argument("--ntherm", type=int, default=300)
ap.add_argument("--nsep", type=int, default=4); ap.add_argument("--nmeas", type=int, default=250); ap.add_argument("--seed", type=int, default=947)
a = ap.parse_args()
spec = importlib.util.spec_from_file_location("fct", a.fct); fct = importlib.util.module_from_spec(spec); spec.loader.exec_module(fct)
sp = fct.spatial_box(a.L); lat = fct.Lat4(sp, a.K); rng = np.random.default_rng(a.seed)
pidx = np.array([[j for (j, s) in P] for P in sp["plaqs"]]); psg = np.array([[s for (j, s) in P] for P in sp["plaqs"]])
lneg = psg < 0; lmul = fct.cmult(lneg); B = a.B; nsl = lat.nsl; npl = len(pidx)
def slice_obs(x):
    c = fct.loop_prod(x, pidx, lmul)[..., 0]                    # (B, npl) space-like plaquettes
    G = fct.loop_grads(x, pidx, lneg, lmul)                     # (B, npl, 4, 4) tangent gradients
    g = np.zeros((B, nsl, 4))
    for k in range(4):
        np.add.at(g, (slice(None), pidx[:, k]), G[:, :, k])
    return c, g
U = np.zeros((B, lat.nl, 4)); U[..., 0] = 1.0
for i in range(a.ntherm): fct.sweep_su2(U, lat.tab_all, a.beta, rng, 2)
F = np.zeros((B, a.nmeas, 3)); D = np.zeros((B, a.nmeas, 3, 3)); loc = np.zeros((B, a.nmeas, 4))
for r in range(a.nmeas):
    for i in range(a.nsep): fct.sweep_su2(U, lat.tab_all, a.beta, rng, 2)
    x, w, _ = fct.slices_su2(lat, U)
    cx, gx = slice_obs(x); cw, gw = slice_obs(w)
    t = (x*w).sum(-1)                                           # (B, nsl) time-like plaquettes
    F[:, r, 0] = cx.sum(1); F[:, r, 1] = cw.sum(1); F[:, r, 2] = t.sum(1)
    D[:, r, 0, 0] = (gx**2).sum((1, 2)); D[:, r, 1, 1] = (gw**2).sum((1, 2)); D[:, r, 2, 2] = 2*(1-t**2).sum(1)
    D[:, r, 0, 2] = D[:, r, 2, 0] = (gx*w).sum((1, 2)); D[:, r, 1, 2] = D[:, r, 2, 1] = (gw*x).sum((1, 2))
    loc[:, r] = np.stack([cx.mean(1), (cx**2).mean(1), t.mean(1), (t**2).mean(1)], 1)
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e9 > 2.0: sys.exit("RSS above 2 GB")
def est(sel):
    f = F[sel].reshape(-1, 3); C = np.cov(f.T); Dm = D[sel].reshape(-1, 3, 3).mean(0)
    R = np.diag(C)/np.diag(Dm); top = eigh(C, Dm, eigvals_only=True)[-1]
    m = loc[sel].reshape(-1, 4).mean(0)
    Rc = (m[1]-m[0]**2)/(4*(1-m[1])); Rt = (m[3]-m[2]**2)/(2*(1-m[3]))
    chi_t = C[2, 2]/nsl
    return np.array([R[0], R[1], R[2], top, Rc, Rt, chi_t, m[0], m[2], m[3]])
full = est(np.ones(B, bool)); jk = np.array([est(np.arange(B) != b) for b in range(B)])
err = np.sqrt((B-1)/B*((jk-jk.mean(0))**2).sum(0))
ac = np.mean([np.corrcoef(F[b, :-1, 2], F[b, 1:, 2])[0, 1] for b in range(B)])
names = ["R_J(sum c_p(x))", "R_J(sum c_p(w))", "R_J(sum t_l)", "top of 3-span", "R(one c_p)", "R_J(one t_l)", "chi_t", "E c_p", "E t", "E t^2"]
print(f"L={a.L} K={a.K} beta={a.beta} B={B} ntherm={a.ntherm} nsep={a.nsep} nmeas={a.nmeas} links/slice={nsl} lag-1 autocorr of sum t: {ac:.3f}")
for n_, v, e in zip(names, full, err): print(f"  {n_:18s} {v:.5f} +- {e:.5f}")
print("  peak RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, flush=True)
```

Exactly solvable companion (not run): the one-plaquette chain. Compare E_1 (3.56 at beta 2.3, row 941 Run 3) with
Xi(beta/gam_J)/2 and with (1/2) integral of gam_s ds; both must be below E_1, and the gap between them measures the loss.

## Result (written 09:16Z; updated 09:59Z after the three GUIDE runs)

| Statement | Label |
|---|---|
| Branch: row 946 did not refute (FC); its laws are the open-time pair (nu_K, pi_x^(K)), K = 6, 8, boxes of side 4 and 6 | READ; GUIDE on a nearby measure |
| (FC-seed)_a: the rate form alpha_c (1 - theta) >= beta^2 kbar (e^(2 K_a) - 1) on (24a)^3 | restatement (substitution; same line as check 943) |
| Every route through (HC-vac) needs E_1(B) >= K_a, that is b E_1 > 24 C_beta + 72 log a (about 384 + 72 log a) at box side b = 24a | PROVED (from Proposition HC) |
| FP fails (FC-seed)_a for every a by a factor above 59, and satisfies (FC)_theta with theta < 1 on each finite box | PROVED given FP's mode list (READ) |
| (EC-nec): (HC-vac)_alpha implies Ent_nu(P^(2m) g) <= e^(-2 alpha m) Ent_nu(g); (FC), (GC) are not necessary | PROVED (hand); the non-necessity rests on row 941's GUIDE Run 4 |
| Theorem BR: log-Sobolev constants alpha_s of the bridge marginals nu_s (gauge-invariant functions) give (HC-vac)_alpha with alpha = (1/2) integral of alpha_s ds | PROVED implication (hand); exact in a Gaussian mode (Nelson's exponent) |
| (BR-gap): E_1 >= (1/2) integral of gam_s ds. (BR-ent): Ent_nu(P g) <= exp(-integral of alpha_s ds) Ent_nu(g) | PROVED implications (hand) |
| (BR-loss): one-step entropy loss = (1/2) integral of the bridge Fisher information | ARGUED; not used |
| Ceiling without gauge invariance: Cov_(nu_s)(y) = v_s Id (Elitzur for two slices), so alpha <= 4/(beta + 2) for all functions | PROVED (hand) |
| nu_s is not log-concave for beta > 2 | PROVED in row 941 (ceiling (ii)); carried over |
| Lemma MS: (GC) for P^(n+1) with theta = kappa_W^2 r_1^(2n), from kbar_h and (P1-av), no smallness | PROVED implication (hand); group-blind |
| Bridge identity for G(s) = integral of abs(grad u_s)^2 d nu_s, and (COV-dir) implies (GC) | identity PROVED; (COV-dir) OPEN |
| Lemma J and Corollary BR-J: (LSI-J)_(alpha_J) for the two-slice law gives (HC-vac)_alpha, alpha = Xi(beta/alpha_J)/2 >= min(alpha_J/(2 beta), 1) | PROVED given the Gaussian log-Sobolev inequality (RECALLED) |
| chi_t <= 2 (1 - E t^2)/alpha_J under (LSI-J) | PROVED (one test function) |
| Lemma INV: for SU(2) on a box of side at least 3 the gauge-invariant polynomials of degree at most two in the bridge field are c_0 + sum of c_l abs(y_l)^2; FP's failing functions have degree one and two | PROVED (hand) |
| Small-box run of the test of 7.4 (SU(2), 4^3 and 6^3 at beta 2.3, 4^3 at beta 2.6, open time): max R_J = 0.155, 0.152, 0.112; chi_t = 0.168, 0.165, 0.107 | GUIDE; (LSI-J-seed)_a not refuted on these boxes; caps alpha_J <= 6.5 and 9.0 there |
| Double wells that one step jumps: the bridge form keeps a rate where (GC) fails | ARGUED; GUIDE (Step 6): in five flat double wells with theta_GC >= 1, E_BR/E_1 is 0.79 to 0.85, and in row 941's two double-well rotors 0.78 and 0.87; (BR-gap) not violated in 19 models (9 flat, 10 rotor); exact in two Gaussians; within 8 percent for free rotors |
| (FC)_theta, (GC)_theta with the seed rate, for SU(2) Wilson at beta 2.3 to 2.6 on the seed box | OPEN; not proved; not necessary for the seed (GUIDE: chains with a gap where (GC) fails) |
| (LSI-br-seed)_a, (LSI-J-seed)_a, (PI-br-seed)_a for SU(2) Wilson at beta 2.3 to 2.6 | OPEN; no bound on alpha_s, alpha_J, gam_s for SU(2) is proved here |
| (HC-vac) on the seed box; the seed | OPEN |

Limits. Every proof is by hand, by Claude Fable 5.2 (max), checked by no other model; the check is row 949.
All PROVED statements are group-blind implications or identities, except the Elitzur covariance of 5.5 and Lemma INV of 5.7,
which use the gauge map -1 at one site (the degree-one part holds for compact U(1) too). No statement here bounds a
log-Sobolev or Poincare constant for SU(2) in the window. Recalled and not rebuilt: the Gaussian log-Sobolev
inequality (used in Lemma J only), lattice numbers (GUIDE). Row 936 was read for statements only. origin/main and the
PR branches are not on this clone and were not searched. Credit: the slice chain, (A1)-(A7), Theorems C, C0 and
the test design are row 941's; Proposition HC and Theorem E are row 931's; the transfer frame is Ethan Sussman
and Levent Alpoge's, with Claude and Codex as authors of their text; method names: Gross (log-Sobolev and
hypercontractivity), Nelson, Elitzur, Ahlswede and Gacs (entropy and hypercontractivity), Bauerschmidt and
Bodineau (log-Sobolev inequalities through a Gaussian decomposition; recalled, not used in a proof step).
Nothing here is a seed at order one, a mass gap, or a public claim.

RESULT: Row 947 (Claude Fable 5.2 max, author, checked by no one): (FC)_theta with the seed rate for SU(2) Wilson at beta 2.3-2.6 is NOT proved and stays OPEN; row 946 did not refute it (GUIDE on open-time laws, boxes of side 4 and 6). PROVED (hand, unchecked): (FC)/(GC) are not necessary for the seed, while entropy contraction is (EC-nec); Theorem BR: one step of the vacuum slice chain is an ambient Brownian bridge of duration 1/beta, and log-Sobolev constants alpha_s of its fractional-time marginals nu_s (gauge-invariant functions) give (HC-vac) directly with alpha = (1/2) integral_0^(1/beta) alpha_s ds, exact in every Gaussian mode, with no use of (LSI-vac), (FC), (C1-av), (COV), (SG-step) or (SC); Corollary BR-J: a log-Sobolev inequality for the two-slice vacuum law J with constant alpha_J gives (HC-vac) with alpha >= min(alpha_J/(2 beta), 1) (given the Gaussian log-Sobolev inequality, recalled); Lemma MS ((GC) holds for a power of P from the gap and two one-step constants); Lemma INV (gauge invariance removes FP's failing functions of degree one and two; it does not separate SU(2) from compact U(1), and nothing is proved in degree four); the rate statement (FC-seed) and the necessary size b E_1 > 24 C_beta + 72 log a (about 384 + 72 log a); FP fails every form only through the rate (factor above 59). GUIDE (refute only): (BR-gap) is not violated in 19 solvable chains, is exact in Gaussians, within 8 percent for free rotors, and keeps 0.78 to 0.87 of the true rate in seven double wells where (GC) is false; on SU(2) boxes 4^3 and 6^3 at beta 2.3 and 4^3 at 2.6 the two-slice Poincare ratios are at most 0.155 +- 0.004 (time-like plaquette sum), below every seed threshold (0.31 and more), so (LSI-J-seed) is not refuted there. SMALLEST UNPROVED INEQUALITY: (LSI-br-seed)_a, (1/2) integral alpha_s ds >= K_a = (C_beta + 3 log a)/(a - 2) on (24a)^3 for one even a, or its simpler sufficient form (LSI-J-seed)_a, alpha_J >= 2 beta K_a (a >= 30); nothing here bounds these constants for SU(2) from below, which is an intermediate-coupling mass-gap statement with no known method. TEST: R_J(Phi) = Var_J(Phi)/E_J|grad Phi|^2 for gauge-invariant two-slice observables, first instance chi_t <= (1 - E t^2)/(beta K_a); run here on small boxes only (not refuted); one violation on the seed box would refute (LSI-J-seed)_a.
