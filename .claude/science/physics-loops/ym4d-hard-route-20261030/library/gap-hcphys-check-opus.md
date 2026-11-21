lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T12:21Z

# Row 984 `gap-hcphys-check-opus`: line-by-line check of row 982 (`library/gap-hcphys-max.md`)

Checker: Claude Opus 5.5, max reasoning, Mac mini worker 1, pinned at commit 52d3e029c of `claude/ym4d-hard-route`.
Object checked: `library/gap-hcphys-max.md` as it stands at 52d3e029c (written by Claude Fable 5.2, row 982).
Started 2026-11-15T00:21Z. Check item only: no new attack.

## Status log

- 2026-11-15T00:21Z: file created with the plan; inputs not yet read.
- 2026-11-15T00:37Z: Steps 1-8 written (all eight steps of the plan done); the lease may be released.

## Plan (at most eight steps; one step per response; each result appended before the next)

1. Read FINISH.md rules (efficiency, build on published work), GOAL.md, and `gap-hcphys-max.md` in full; record the
   statements to check, with line anchors, and the sources they lean on.
2. Lemma CAP (3.0), with the two end inequalities of Theorem BR (iv) at q = p = 2 and the claim
   Var_(nu_s)(u_s) = F(s) for a mean-zero f.
3. Lemma TEL (3.3).
4. Lemma EE and Lemma COUNT (4.2).
5. Route 2 (a) and the crossed-channel identity.
6. N2's claim that row 978's reduction and row 720's Theorem ZD meet at one object (the thermal sum of the cube between
   the hot end and the cold range).
7. Re-read the account lines quoted in `library/guide/lane982/SOURCES.md`; say whether (P1)-(P4) state them faithfully.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with the line) and the RESULT line.

## Step 1. Inputs read and statements under check (written 00:28Z)

**Read in full or at the anchors.** FINISH.md L1-84 and L299-351, row 984 (line 1061); GOAL.md in full;
`gap-hcphys-max.md` in full (275 lines, the object of the check); `guide/lane982/SOURCES.md`; `gap-fc-max.md`
L121-228 (Theorem BR with objects (B1)-(B5), corollaries 5.3, hand checks 5.4, fact tests 5.5); `gap-ladder-max.md`
L115-136 (Lemma IHC with its remarks) and L180-206 (5.6, 5.7). Row 720's file and the account are read in later steps.

**Statements under check (anchors are lines of `gap-hcphys-max.md` at 52d3e029c).**

| Item | Lines |
|---|---|
| Lemma CAP (a), (a'), (b), (c), its proof, the Reading and the Gaussian hand check | L62-79 |
| Lemma TEL, its proof and its Use paragraph | L105-113 |
| The three forms (U1)-(U3), Lemma EE (a)-(d), Lemma COUNT (a)-(c) and its Reading | L131-153 |
| Route 2 (a) | L189 |
| Crossed-channel identity | L211 |
| N2's claim: row 978's reduction and row 720's Theorem ZD meet at one object | L266, with L163, L209, L217 |
| Port answer (P1)-(P4) against the account lines of `SOURCES.md` | L46-52 |

Kind of work: a check of our own new text (row 982). No new attack is made, so rule 0a has no lemma to match.

## Step 2. Lemma CAP (3.0), the end inequalities of Theorem BR (iv) at q = p = 2, and Var_(nu_s)(u_s) = F(s)

Notation of `gap-fc-max.md` 5.1: g_s the heat kernel of R^N, h_s = g_s * m, s' = 1/beta - s,
nu_s = Z^(-1) h_s h_(s') dy, N_s = g_(s') * (f m), u_s = N_s/h_(s').

**2.1 The two end inequalities at q = p = 2. HOLD.**

- Start end. K(x, dy) = g_eps(x - y) h_(1/beta - eps)(y) dy/h_(1/beta)(x) is a probability kernel, because
  g_eps * h_(1/beta - eps) = h_(1/beta) (B2). K u_eps(x) = h_(1/beta)(x)^(-1) (g_eps * N_eps)(x) = N_0(x)/h_(1/beta)(x) = u_0(x),
  because g_eps * g_(1/beta - eps) = g_(1/beta). nu K = nu_eps, because the integral of g_eps(x - y) m(dx) is h_eps(y).
  Jensen for t -> t^2 (valid for signed u): integral of u_0^2 d nu <= integral of u_eps^2 d nu_eps. Since u_0 = P f on M (B1)
  and nu is carried by M: F(eps) >= ||P f||_2^2.
- Final end. K'(y, dw) = g_eps(y - w) m(dw)/h_eps(y) is a probability kernel on M, u_(1/beta - eps) = K' f, and
  nu_(1/beta - eps) K' = nu, because the integral of h_(1/beta - eps)(y) g_eps(y - w) dy is h_(1/beta)(w). Jensen:
  F(1/beta - eps) <= ||f||_2^2.

Neither end needs delta <= f <= 1/delta. The reduction of a signed bounded f by a constant (L74) is correct but not
needed at q = 2: u_s moves to u_s + c, and ||f + c||^2 - ||P(f + c)||^2 = ||f||^2 - ||P f||^2 because P 1 = 1 and
<P f, 1>_nu = <f, 1>_nu.

**2.2 Var_(nu_s)(u_s) = F(s) for nu-mean-zero f. HOLDS.** Integral of u_s d nu_s = Z^(-1) integral of N_s h_s dy
= Z^(-1) integral of f(w) (g_(s') * h_s)(w) m(dw) = Z^(-1) integral of f h_(1/beta) dm = integral of f d nu. So the
nu_s-mean of u_s is the nu-mean of f, and for a mean-zero f, Var_(nu_s)(u_s) = F(s). (The file's reason, "the kernels
of step (iv) map nu_s to nu", is the same computation with K'_s(y, dw) = g_(s')(y - w) m(dw)/h_(s')(y).)

**2.3 (a), the energy bound. HOLDS.** Step (ii) with q = 2 constant gives F' = integral of |grad u_s|^2 d nu_s. Integrate
over [eps, 1/beta - eps] and use 2.1. The right side is <f, (1 - P^2) f>_nu because P is self-adjoint on L^2(nu).

**2.4 (a'), the energy identity. HOLDS; the two end limits the file leaves unwritten are short.**

- By (B3), u_s(y) = E[f(U_1) | y_s = y]: given y, the conditional law of w is proportional to g_(s')(y - w) m(dw).
  So F(s) = E[E[f(U_1) | y_s]^2] and ||f||^2 - F(s) = E[Var(f(U_1) | y_s)] <= E|f(U_1) - f~(y_s)|^2 for every bounded
  continuous f~ on R^N (the conditional mean is the L^2 projection). Take f~ a bounded continuous extension of f
  (Tietze; M is compact). As s -> 1/beta, y_s - U_1 = (1 - lam)(U_0 - U_1) + (lam (1 - lam)/beta)^(1/2) xi -> 0 in
  probability (lam = beta s). Bounded convergence gives F(1/beta - eps) -> ||f||_2^2.
- As s -> 0, u_s -> u_0 locally uniformly on R^N, |u_s| <= sup |f|, and nu_s -> nu weakly with uniform Gaussian
  tails. So F(eps) -> integral of u_0^2 d nu = ||P f||_2^2.
- The left side of (a) increases to the integral over (0, 1/beta) (monotone convergence). So
  <f, (1 - P^2) f>_nu = integral over (0, 1/beta) of E_(nu_s) |grad u_s|^2 ds.

**2.5 (b), the cap. The inequality HOLDS; the comparison sentence FAILS; HOLDS AFTER CORRECTION.**

- Proof steps checked. f_1 = e^(E_1) P f_1 is continuous (continuous kernel on compact M), real, gauge invariant, of
  mean zero. F(s) >= F(eps) >= e^(-2 E_1) for s >= eps (F' >= 0 and 2.1). The Poincare hypothesis is applied to u_s
  only, which is gauge invariant (B5), bounded, C^1 with bounded gradient (step (i)). Integration and eps -> 0 by
  monotone convergence are correct. So (1/2) integral of gam_s ds <= (e^(2 E_1) - 1)/2.
- **Defect (L70).** "With (BR-gap), E_1 >= (1/2) integral of gam_s ds: the integrated bridge Poincare constant equals
  the gap up to the factor (e^(2 E_1) - 1)/(2 E_1)." Both (BR-gap) (`gap-fc-max.md` L181-183) and (b) are UPPER bounds
  on (1/2) integral of gam_s ds, under the same hypothesis, and (BR-gap) is the sharper one:
  (1/2) integral of gam_s ds <= E_1 <= (e^(2 E_1) - 1)/2. Nothing in the file bounds the bridge constants from below
  by the gap. So "equals the gap up to the factor" is not shown, and (b) is a weaker corollary of (BR-gap).
  The file's own Gaussian check (L79) shows it: (BR-gap) is exact there (omega <= omega), (b) is not.
- Correction: "(b) follows from (BR-gap), which gives the sharper cap (1/2) integral of gam_s ds <= E_1. No lower bound
  of the bridge constants in terms of the gap is proved." The same correction applies to N5 (L272): the fact test for
  a claimed bridge rate is (1/2) integral of gam_s ds <= E_1.

**2.6 (c). HOLDS.** A log-Sobolev inequality Ent(phi^2) <= (2/alpha) integral |grad phi|^2 gives the Poincare inequality
with constant alpha: put phi = 1 + t g, g bounded, gauge invariant, C^1 with bounded gradient, so delta <= phi <= 1/delta
for small t; Ent((1 + t g)^2) = 2 t^2 Var(g) + O(t^3). Only bounded functions (u_s) are fed to the Poincare inequality
in (b), so the class difference (bounded phi in (LSI-br), all phi with bounded gradient in the hypothesis of (b)) does
no harm. A/2 <= (1/(2 beta_0)) sup alpha_s is the length of the interval. Sharper, by (BR-gap) or Lemma RATE (c):
A/2 <= E_1.

**2.7 The Reading (L77) and the hand check (L79). HOLD, with the sharper constant.** By (BR-gap) the average of gam_s
over (0, 1/beta_0) is at most 2 beta_0 E_1 = 2 beta_0 M a_iota exactly, with no factor (1 + o(1)). A proof of (HC-phys)
through Theorem BR needs the average of alpha_s at least 2 beta_0 M_H a_iota. So the conclusion "the bridge constants
are of the order beta_0 a_iota times a physical mass, with the bare coupling" stands. It is a reading of (BR-gap) and
Theorem BR, which `gap-fc-max.md` 5.3 already contains, and not a new bound. Gaussian check: the integral over
(0, 1/beta) of c/(1 + c s) ds = log(1 + c/beta) = omega, doubled by the symmetry s <-> s', so 2 omega. Correct.

**Verdict, Lemma CAP.** (a), (a'), the end inequalities and Var = F: HOLD. (b), (c): HOLD as inequalities; L70 FAILS as
written and HOLDS AFTER CORRECTION (two upper bounds, (BR-gap) the sharper; no two-sided statement). The use of CAP in
T3 (L88: sup_s alpha_s >= 2 beta_0 M_H a_iota is needed) and in Route 1 place 1 (L177) reads only (c) and stands.

## Step 3. Lemma TEL (3.3) (written 00:30Z)

**Statement and proof (L107-111). HOLD.** For the product law of (A_0, ..., A_K), sub-additivity of entropy gives
Ent(G) <= sum over k of E[Ent_(mu_k)(G | A_j, j != k)] for G >= 0 (classical tensorisation, RECALLED in the file;
correct as recalled). With G = g^2, g = f(Y), each conditional section a_k -> f(D_k a_k + c) is C^1 with bounded
gradient, so the log-Sobolev inequality of mu_k applies to it, and grad_(A_k) g = D_k^T grad f(Y). Summing,
Ent(f(Y)^2) <= 2 E <grad f(Y), (sum over k of D_k D_k^T/rho_k) grad f(Y)>, and the second bound is the operator norm of
a positive semidefinite matrix. Integrability: f grows at most linearly and each mu_k has sub-Gaussian tails (Herbst),
so all terms are finite.

**The Use paragraph (L113). The lower bound HOLDS given TEL; the orders of size are ARGUED, as the file marks them.**

- "The law of Y has a log-Sobolev constant at least 1/||sum D_k D_k^T/rho_k||": immediate from TEL.
- The order a_- beta_K L^(-K): with beta_k non-increasing in k up to the unit and ||R_0 D_k||^2 <= c L^k, the sum over k
  of L^k/(a_- beta_k) is at most (L/(L - 1)) L^K/(a_- beta_K). This is correct given the linear count, which the file
  marks ARGUED (the account's minimiser kernels were not read).
- The Gaussian upper bound: for a Gaussian Y with covariance C_Y, a linear test function along the top eigenvector of
  C_Y gives Poincare, hence log-Sobolev, constant at most 1/||C_Y||, and C_Y >= sum D_k D_k^T/(a_+ beta_k). Correct for
  the benchmark. A linear function is not gauge invariant in SU(2); in the abelian benchmark a linear function of the
  field strength is. So "the count is sharp in the benchmark" holds for an abelian Gaussian benchmark.
- Remark, not a verdict (T3, L88, is marked ARGUED and is outside the list of row 984): TEL bounds the slice law of Y.
  Theorem BR reads the bridge laws nu_s, which are Gaussian smoothings of two-slice averages (B3). The step from a
  constant for the slice law to the constants alpha_s of nu_s is not written in the file.

**Paragraph after TEL (L115), first sentence only (the rest is marked ARGUED).** For gauge-invariant f of nu-mean zero,
Var_nu(f)(1 - e^(-2 E_1)) <= <f, (1 - P^2) f>_nu (spectral theorem, spectrum of P^2 on the mean-zero gauge-invariant
space in [0, e^(-2 E_1)]). With Lemma CAP (a') (HOLDS, Step 2.4) the right side is the bridge energy, at most
(1/beta_0) sup_s E_(nu_s) |grad u_s|^2. Correct.

**Verdict, Lemma TEL.** HOLDS (given the classical tensorisation of entropy).

## Step 4. Lemma EE and Lemma COUNT (4.2), with the forms (U1)-(U3)

Setting (L133). The sums S(t) converge for every real t > 0: the transfer operator T = e^(-V/2) K e^(-V/2) (P is
T/lambda_0, conjugated by Omega) with 0 <= e^(-V/2) <= 1 has eigenvalues at most the singular values of the kinetic kernel K, a product over links of Bessel ratios with
super-exponential decay. Only t >= 1 is used. U = -X' is the thermal mean energy and X + t U the thermal entropy of the
state with weights e^(-E_i t)/(1 + S(t)): correct (E_0 = 0, so log of the partition function is X).

**Lemma EE.**

- (a) (U1) => (U2). HOLDS, given Lemma IHC (`gap-ladder-max.md` L119-131; its check is row 981). I re-did the four steps
  for the chain Q = P^T: (i) p_(s + mT)(u, .) = Q^m p_s(u, .) (Chapman-Kolmogorov and symmetry of the densities);
  (ii) ||g||_(q') <= ||g||_1^(1 - theta) ||g||_2^theta with theta = 2(q' - 1)/q' = 1 - tanh(alpha_* m) for
  q' = 1 + e^(-2 alpha_* m); (iii) Jensen for the concave x -> x^theta over u ~ nu; (iv) (5.3) 1 + S(2s) =
  E_u ||p_s(u, .)||_2^2 = trace of P^(2s). (U1) is asked only on g = p_s(u, .) with 2 s = tau_0/a_iota, which is all
  that IHC reads (5.6 (a) there). Needs tau_0/a_iota to be an even integer, as (U1) assumes.
- (b) HOLDS. (log X)' = -U/X <= -kappa a_iota on [tau_0/a_iota, ell/a_iota]; integrate; X(tau_0/a_iota) <= Theta is (TH)
  as restated at L129. X(ell/a_iota) <= log(1 + s_*) gives S <= s_* at the seed time (round n up and use that X is
  non-increasing).
- (c) HOLDS (the same identity, X > 0 because the gauge-invariant space has dimension above one).
- (d) HOLDS. X = log(1 + S) <= S and U >= E_1 S/(1 + S) >= E_1 S/2 where S <= 1; S is non-increasing, so U/X >= E_1/2
  on [t_c, infinity) and X(t) <= X(t_c) e^(-E_1 (t - t_c)/2) <= (log 2) e^(-E_1 (t - t_c)/2).

**The heading of 4.2, "Three forms of the unit inequality, in decreasing strength" (L131). FAILS as written; HOLDS
AFTER CORRECTION.** Lemma EE (a) proves (U1) => (U2). Nothing proves (U2) => (U3). (U2) bounds X at the times
tau_0/a_iota + 2mT from one start; (U3) bounds U/X at every t of the interval. The converse direction does hold on the
interval: (U3)_kappa gives X(tau_0/a_iota + 2mT) <= e^(-2 kappa l_unit m) X(tau_0/a_iota) <= (1 - tanh(alpha_* m)) X(tau_0/a_iota)
with alpha_* = kappa l_unit, for every m with tau_0/a_iota + 2mT <= ell/a_iota (since e^(-2x) <= 2/(1 + e^(2x))). So on
the range the seed reads, (U3) is at least as strong as (U2), not weaker. Correction: "(U1) => (U2) (Lemma EE (a));
(U3) => (U2) on [tau_0, ell]; both (U2) and (U3) give the seed with (TH); the integral condition of
Lemma EE (c), the integral of U/X over [tau_0/a_iota, ell/a_iota] at least log(X(tau_0/a_iota)/log(1 + s_*)), is the seed
itself, so it is no crux."
Consequence for 4.3: (UNIT) is stated in the pointwise form (U3), so (UNIT) is not shown to follow from (HC-phys);
a failure to prove (UNIT) says nothing on (U1) or (U2). Item 3 of 8.1 is worded correctly ("implies its integrated form").

**Lemma COUNT.**

- (a) HOLDS (Markov: N(E) e^(-tE) <= sum over E_i <= E of e^(-t E_i) <= 1 + S(t), t > 0).
- (b) HOLDS as a conditional statement. t = tau + (1/M) log(2 Theta M/E) >= tau iff E <= 2 Theta M; then
  X(t) <= 2 Theta (E/(2 Theta M)) = E/M, and log N(E) <= tE + X(t) = E tau + (E/M)(1 + log(2 Theta M/E)). The
  parenthesis "(the conclusion of Corollary CU)" needs a small correction: Lemma IHC and (TH) give the hypothesis only at
  t_0 + 2m (t_0 the even start); for real t monotonicity of X gives it with tau = t_0 + 2 in lattice units.
- (c) HOLDS (each e^(-E_i t) = e^(-E_i (t - t_c)) e^(-E_i t_c) <= e^(-E_1 (t - t_c)) e^(-E_i t_c) for i >= 1, t >= t_c).
- Reading (L153). "(HC-phys) with (TH) is ... the statement that the box has at most the states of a massive gas":
  only the implication (HC-phys) + (TH) => count is proved; "is" should read "implies". The count is a statement on the
  spectrum alone, and (HC-traj) is not determined by the spectrum, so the converse is not available as stated.

**Verdict.** Lemma EE (a) (given Lemma IHC), (b), (c), (d): HOLD. Lemma COUNT (a), (b), (c): HOLD ((b) with the
corrected parenthesis). Heading of 4.2: HOLDS AFTER CORRECTION ((U3) is not weaker than (U2) on the range). Reading of
COUNT: HOLDS AFTER CORRECTION ("implies", not "is").

## Step 5. Route 2 (a) and the crossed-channel identity

**Route 2 (a) (L189). HOLDS.** For phi = 1_A/nu(A)^(1/2): integral of phi^2 d nu = 1 and Ent_nu(phi^2) = log(1/nu(A)).
E_c(phi) = ||phi||^2 - ||P^T phi||^2 <= 1, and E_c(phi) = (1/2) E|phi(U_0) - phi(U_(2T))|^2 is correct. The functions of the
lane are gauge invariant, so A must be a gauge-invariant set: the law of one plaquette trace under nu has a density
(nu has a density with respect to Haar measure), so gauge-invariant sets {tr u_p in I} of arbitrarily small positive
measure exist, and the argument runs inside the gauge-invariant class. Second sentence: for f >= 0,
e^(-tau (1 - Q)) f = e^(-tau) sum over n of tau^n Q^n f/n! >= e^(-tau) f with Q = P^(2T) Markov, and L^p(nu) is not
contained in L^q(nu) for q > p on a non-atomic space. Correct.

**Crossed-channel identity (L211). HOLDS** (given the axis-permutation symmetry of the Wilson action on the periodic
torus and the trace formula Z(B x t) = trace over gauge-invariant states of T_B^t in each direction). Z((2n)^3 x t) =
lambda_0((2n)^3)^t e^(X(t; (2n)^3)) in the channel of the side t, and = mu_0(B')^(2n) e^(X'(2n; B')) in the channel of a side
2n, with B' = (2n)^2 x t. Taking logarithms gives the identity exactly; X = log Z - t log lambda_0 is (EX) (L123).

## Step 6. N2's claim: row 978's reduction and row 720's Theorem ZD meet at one object (written 00:32Z)

**Read for this step.** `gap-phys-seed.md` (row 720) L249-333: Lemma Z, Lemma Z3, Theorem ZD, Corollary Z2, Theorem
ZD-c with (PHYS-SEED), (PHYS-SEED-Delta), (Z-SEED), (BDD-Delta), (Z-UNB), Corollary Z4. Row 978: Corollary CU and its
(APR) form, the defective form (`gap-ladder-max.md` 5.2, 5.7). Theorem SH, Lemmas Z', E', Corollary S3' and
Proposition Delta were not re-read; they are the named inputs of Theorem ZD.

**The two reductions, side by side.**

- Row 978 (Corollary CU, 5.7): (TH) and (HC-phys) give (SEED-phys). (TH) is X(tau_0/a_iota; cube) <= Theta, extensive
  (Theta = (2 ell/L_0)^3 A from (APR) and Proposition Delta). (HC-phys) must carry X from Theta down to log(1 + s_*)
  by the time ell/a_iota.
- Row 720 (Theorem ZD-c): (PHYS-SEED) is EQUIVALENT to (BDD-Delta) and (Z-UNB) together. Its route reads X of the cube
  at the time b/4 through Proposition Delta, X(b/4; b^3) <= 64 D(b/4) (Lemma Z), and then the gap.

**What holds, as an implication (from Corollary CU of row 978 and Theorem ZD-c of row 720, as stated there; one line).** By Corollary CU,
(TH) and (HC-phys) give the seed at every large half side ell. With l_1 = 2 ell and P = {2^i l_1}, (PHYS-SEED) of
ZD-c holds at l = l_1, given the side condition of ZD-c (l_1/(4 a_j) an integer at least 3 for all large j). By ZD-c,
(BDD-Delta) and (Z-UNB) follow. So **(TH) and (HC-phys) imply (BDD-Delta) and (Z-UNB)**: a proof by row 978's route
contains a proof of row 720's pair, and a refutation of (BDD-Delta) or (Z-UNB) on the family refutes (HC-phys) there
((TH) comes from the account's own stability statements). The converse is not known: (HC-phys) is stronger than the
seed (row 978, 5.2), and ZD-c's pair is equivalent to the seed. So "they are not two independent chances" HOLDS, in
this direction.

**"Meet at one object, the thermal sum of the cube between the hot end and the cold range."** A description, not a
statement, and it fits: both routes bound the same function X(t; cube) on the range from an extensive start to the
time where S <= 1. Row 978 reads it from the start time tau_0/a_iota at a rate; row 720 reads it at the one time b/4
through the Casimir free energy of the symmetric torus (Proposition Delta) and lets the gap finish. The precise form is
the implication above. Verdict: **HOLDS AFTER CORRECTION**: replace "meet at one object" by "(TH) and (HC-phys) imply
(BDD-Delta) and (Z-UNB) through the seed (Corollary CU, Theorem ZD-c); the converse is not known".

**Two loose identifications next to the claim.**

- L163, "a gap M_1 on the cube, and a bounded thermal sum at one time t_c with t_c a_iota bounded. These are (Z-UNB) and
  (BDD-Delta) of row 720": the seed follows from that pair (Lemma COUNT (c): S(ell/a_iota) <= e^(-M_1 (ell - t_c a_iota))
  once S(t_c) <= 1), correct. But they are not (Z-UNB) and (BDD-Delta) term by term. (Z-UNB) asks only that L m(L^3) is
  unbounded along P, which is weaker than a uniform gap M_1; (BDD-Delta) bounds the Casimir free energy of the
  symmetric tori at all large sizes, not S on the cube of side 2 ell at one time. The two pairs are equivalent through
  the seed (ZD-c one way; Theorem S and Corollary S3' with the side comparisons the other way, not re-checked here).
  HOLDS AFTER CORRECTION: "equivalent through the seed", not "are".
- L217, "Each [route] stops at the same object": true of Route 3 (the middle range) and of Route 2 (it returns (U2), a
  statement on X); Route 1 stops at T3 and at a log-Sobolev constant for the unit law in the fine metric, which is not a
  statement on X. Wording only; no verdict rests on it.

**Consequence for N2's advice (L266).** "The statement to keep is (U1) or (U2) in unit steps, or (UNIT-EE)": by Step 4,
(UNIT-EE) in its pointwise form is not implied by (U1) or (U2). Correction: "keep (U1) or (U2); (UNIT-EE) is a sufficient condition for (U2) on [tau_0, ell], not a
weaker form; the integral form of Lemma EE (c) is the seed itself".

## Step 7. The account's lines behind (P1)-(P4) (written 00:35Z)

**Source.** Ethan Sussman and Levent Alpoge, complete account of Theorem 0 (text authored with Claude and Codex),
commit `31a47c543775`, `theorem_0_complete_account_raw_I.tex` (166,711 lines) and `_II.tex` (145,624 lines), fetched
2026-11-15 by the raw URLs of `guide/lane982/SOURCES.md` into a scratch folder outside the repository; line counts
match SOURCES.md. Read: every range of SOURCES.md, plus CA-II 79091-79135 and 79202-79256 (Definition
8.3:not-step-box-window), CA-II 83830-83905 (class data of the class S before Lemma 8.3:lem-correlation-decay),
CA-II 84166-84177, CA-I 2700-2712, CA-I 46035-46127 (Theorem 4.14:thm-operator-theorem), and the account index
`library/sa-index/ca-full/index.tsv` for the declared status.

**(P1) The form bound. Quotes faithful; the summary HOLDS AFTER CORRECTION.**

- CA-II 80164-80170 reads as quoted: "From the operator theorem at free current we take the following hypothesis. At
  each real background configuration of the step, Q is real symmetric and a_- <= Q <= a_+ as forms, ||Q(b, b')|| <=
  a_+ e^(-c_A dist(b, b')) ..., where 0 < a_- <= a_+ and c_A > 0 do not depend on the level, on K, m, the background
  configuration or the volume." The inner-product sentence is at 80156-80159. Lemma 8.2:lem-fluctuation-positivity
  (begins 75164) states the bound Q(U, 0) >= gamma_0/2 "as the antecedent of this lemma". CMP 95 Proposition 1.2 and
  CMP 99b are cited at 75158-75159, for item (iii) of the preceding definition ("the operator theorem at free current").
- **Defect.** "So the account takes the lower bound as a hypothesis from Balaban's operator theorem" (L46; again in
  8.1 item 1, L225) is incomplete. The account states the bound as its own theorem: CA-I 46035,
  Theorem 4.14:thm-operator-theorem ("The operator theorem at free current"), clause (B): "At every point (U, 0) with
  U in U_R, Q is real symmetric with gamma_0/2 <= Q <= gamma_1"; clause (I): gamma_0, gamma_1 "depend on d and L only;
  they are independent of M, k, K, the nest, B, Lambda_t, Z_0, the volume and g". The index of the account lists it as
  PROVED (`index.tsv`, ca_I.tex 46035; also 4.5:thm-operator-bounds, ca_I.tex 19578, PROVED). Its proof was not read
  here. CA-II 8.2 and 8.3 import this theorem as a hypothesis of their own statements. Correction: "CA-II 8.2-8.3 take
  the bound as a hypothesis imported from the account's Theorem 4.14 (B), (I) (CA-I 46035, declared PROVED; the account
  cites Balaban CMP 95 Proposition 1.2 and CMP 99b for it)". For the port this is the better status: the bound is a
  cited input of the account's own text, not an open hypothesis.

**(P2) The norm. HOLDS.** CA-II 80038-80041: the window is a function of the integration variable A "taken in the
rescaled normalisation in which the unscaled fluctuation field is g_k A". CA-II 79202-79212 fixes the variable on
which Q acts: "The integration variable of [CMP 119 (3.25)] is the scaled fluctuation field A ... Let Q := C^* Delta^(k) C
on g^(B+)", and the box law is E_e(dy) = Z_e^(-1) 1_(W_I)(y) e^(-H_e(y)) dy with H_e = (1/2)<y, Q_II y> + <y, J A_O> - P_e(y)
(79248-79256). So the quadratic part is (1/2)<A, Q A> in the scaled variable, and in the unscaled variable g_k A the
lower bound is a_- g_k^(-2) = a_- x_k, as (P2) says. The lattice of level k has unit spacing in level-k units
(79113), and d = 4 (79095): "four-dimensional" is correct. The radius b_k = A_1 (log x_k)^(p_0) of 80032-80033
agrees with b_k = delta_k/g_k of 79126-79131.

**(P3) The class of laws. Quote faithful; the inference HOLDS AFTER CORRECTION (a missing citation).** CA-II 81161-81190
reads as quoted (Hamiltonian on W, "coercive for phi", lambda := lambda_A - eps_0, nu_H = Z_H^(-1) 1_W e^(-H) dy). At
phi = 0, Hess H = A - P'' >= lambda on W: correct. But 81161 is an abstract proposition; it does not say that the
fluctuation laws are coercive with constants free of the level. That link is in the class data before Lemma
8.3:lem-correlation-decay: CA-II 83846-83855 (Q with q_- <= Q <= q_+, q_- > 0; "The smallness condition of the class
gives varpi <= q_-/4"; "In the application, P is holomorphic on a complex tube containing K^+ ..."), with q_- = a_-
from Definition 8.3:def-box-precision. So the conclusion "each small-field fluctuation law is uniformly log-concave on
a convex window, with a constant free of the level" is the account's reading, with Hess >= q_- - varpi >= (3/4) a_-.
Correction: cite CA-II 83846-83855 beside 81161. Where the account verifies varpi <= q_-/4 for the step was not read.

**(P4) What the account derives. Quotes and greps faithful; HOLDS, with one nuance for 8.1 item 1.**

- Labels: 81493 opens Theorem 8.3:thm-density-bound ("Two-sided density bound on the read set"); 81804 opens
  Corollary 8.3:cor-subgaussian-tails; 83869 is Lemma 8.3:lem-correlation-decay, whose statement begins "Assume the
  following statement, the Helffer-Sjostrand covariance representation". CA-II 84184-84185, of the proof of that lemma
  (84176-84177 name it): "It uses no spectral gap of -L, no variance inequality for log-concave measures in terms of the
  inverse Hessian". CA-I 2708 lists "a mass gap" under "Not asserted". All as (P4) says.
- Greps re-run on the fetched files: CA-I, `Sobolev|Bakry|hypercontract` (case-insensitive): 0 lines. CA-II, same
  pattern: one line, 133310 ("the discrete Sobolev norm of q"). CA-II, the wider pattern of SOURCES.md: lines 84184,
  84205, 133310, 135674. Identical to SOURCES.md.
- Nuance (8.1 item 1, L225, "The account states no log-Sobolev, Poincare or hypercontractive inequality"). The
  Helffer-Sjostrand representation that Lemma 8.3:lem-correlation-decay assumes (83870-83876: L_V >= lambda_- on vector
  fields and Cov(F, G) = <grad F, L_V^(-1) grad G>) gives at F = G the Poincare inequality
  Var(F) <= (1/lambda_-) E|grad F|^2 for smooth V on R^N with Hess V >= lambda_-. So a Poincare inequality for globally
  uniformly convex laws is one line from a hypothesis the account states; it is not derived there, and it is not stated
  for the windowed laws. No log-Sobolev or hypercontractive statement is in CA-I or CA-II. Correction to L225:
  "states no log-Sobolev or hypercontractive inequality, and no Poincare inequality for the windowed laws". (P4)'s
  own conclusion (no log-Sobolev inequality for a small-field fluctuation law in the account) stands.

## Step 8. Verdicts, defects, and the RESULT line

Provenance: Claude Opus 5.5, max reasoning, Mac mini worker 1, commit 52d3e029c. One line-by-line reading by one other
model (the author is Claude Fable 5.2). Not an audit. No numeric run; the numeric lock was not taken.

### 8.1 Verdict per statement (lines of `gap-hcphys-max.md`)

| # | Statement | Line | Verdict | Where checked |
|---|---|---|---|---|
| 1 | Theorem BR (iv) at q = p = 2: F(eps) >= \|\|P f\|\|^2, F(1/beta - eps) <= \|\|f\|\|^2 | L74 | HOLDS | Step 2.1 |
| 2 | Var_(nu_s)(u_s) = F(s) for nu-mean-zero f | L75 | HOLDS | Step 2.2 |
| 3 | Lemma CAP (a), energy bound | L66, L74 | HOLDS | Step 2.3 |
| 4 | Lemma CAP (a'), energy identity (marked ARGUED) | L68 | HOLDS; the two end limits are now written | Step 2.4 |
| 5 | Lemma CAP (b), the inequality | L70, L75 | HOLDS | Step 2.5 |
| 6 | L70: "the integrated bridge Poincare constant equals the gap up to the factor ..." | L70 | FAILS as written; HOLDS AFTER CORRECTION | Step 2.5 |
| 7 | Lemma CAP (c) | L72 | HOLDS (sharper: A/2 <= E_1) | Step 2.6 |
| 8 | Reading after CAP; Gaussian hand check | L77, L79 | HOLD (the bound 2 beta_0 M a_iota is exact, no factor 1 + o(1)) | Step 2.7 |
| 9 | Lemma TEL | L107-111 | HOLDS (given classical tensorisation) | Step 3 |
| 10 | TEL, Use paragraph | L113 | lower bound HOLDS; orders of size ARGUED, as marked | Step 3 |
| 11 | Lemma EE (a)-(d) | L141-143 | HOLDS ((a) given Lemma IHC; its four steps re-done for P^T) | Step 4 |
| 12 | Heading of 4.2, "(U1)-(U3) in decreasing strength" | L131 | FAILS as written; HOLDS AFTER CORRECTION | Step 4 |
| 13 | Lemma COUNT (a)-(c) | L145-151 | HOLDS ((b): the parenthesis needs tau = t_0 + 2) | Step 4 |
| 14 | Reading of COUNT: "(HC-phys) with (TH) is ... the count of a massive gas" | L153 | HOLDS AFTER CORRECTION ("implies") | Step 4 |
| 15 | Route 2 (a) | L189 | HOLDS (also inside the gauge-invariant class) | Step 5 |
| 16 | Crossed-channel identity | L211 | HOLDS | Step 5 |
| 17 | N2: row 978's reduction and Theorem ZD "meet at one object", "not two independent chances" | L266 | HOLDS AFTER CORRECTION | Step 6 |
| 18 | "These are (Z-UNB) and (BDD-Delta) of row 720" | L163 | HOLDS AFTER CORRECTION ("equivalent through the seed") | Step 6 |
| 19 | N2's advice: keep "(U1) or (U2) ..., or (UNIT-EE)" | L266 | HOLDS AFTER CORRECTION (keep (U1) or (U2); (UNIT-EE) only as a sufficient condition) | Steps 4, 6 |
| 20 | (P1) quotes; summary "takes the lower bound as a hypothesis from Balaban's operator theorem" | L46, L225 | quotes faithful; summary HOLDS AFTER CORRECTION | Step 7 |
| 21 | (P2) | L48 | HOLDS | Step 7 |
| 22 | (P3) | L50 | quote faithful; HOLDS AFTER CORRECTION (missing citation) | Step 7 |
| 23 | (P4); 8.1 item 1 "no ... Poincare" | L52, L225 | (P4) HOLDS; L225 HOLDS AFTER CORRECTION | Step 7 |

No statement that a PROVED lemma of row 982 rests on FAILS.

### 8.2 Defects, ranked by what each changes

1. **(UNIT) is stated in a form that (HC-phys) is not shown to imply (L131, L139, L157).** Only (U1) => (U2) is
   proved. On [tau_0, ell] the pointwise (U3) implies (U2) with alpha_* = kappa l_unit, not the converse. So a failure
   to prove (UNIT) does not bear on (U1) or (U2). Repair (unproved as a crux): state the inequality left at the unit as (U2), which (U1) implies and which with
   (TH) gives the seed; (U3) is one sufficient condition for (U2) on the range, not a weaker form. The integral
   condition of Lemma EE (c) is the seed itself, written through U/X, and is no crux.
2. **(P1) and 8.1 item 1 understate the account's status of the form bound.** The account proves it, by its own
   declaration, as Theorem 4.14:thm-operator-theorem (B) with uniformity (I) (CA-I 46035; index status PROVED); CA-II
   8.2-8.3 import it. For a port the bound is then a cited input of the account, not an open hypothesis. Its proof
   was not read here.
3. **Lemma CAP (b) adds nothing to (BR-gap) (L70, L272).** Both are upper bounds on the integrated bridge constant;
   (BR-gap) gives the sharper (1/2) integral of gam_s ds <= E_1. The fact test of N5 should use E_1. The Reading after
   CAP stands, with the exact bound 2 beta_0 M a_iota.
4. **N2's "one object" claim is a description (L266, L163).** The precise statement that holds: (TH) and (HC-phys)
   imply (BDD-Delta) and (Z-UNB), through the seed and Theorem ZD-c (with ZD-c's side condition); the converse is not
   known. The pair at L163 is equivalent to ZD's pair only through the seed.
5. **(P3) cites the abstract proposition only (L50).** The account's link to the fluctuation laws (class S, q_- = a_-,
   varpi <= q_-/4, "In the application") is CA-II 83846-83855.
6. **L225, "no ... Poincare inequality".** A Poincare inequality for globally uniformly convex V on R^N is one line from
   the Helffer-Sjostrand hypothesis of Lemma 8.3:lem-correlation-decay (CA-II 83870-83876); none is stated for the
   windowed laws; no log-Sobolev or hypercontractive statement exists in CA-I or CA-II.
7. **Wording (L153, L145 parenthesis).** "is" should read "implies"; COUNT (b)'s hypothesis comes from Lemma IHC with
   tau = t_0 + 2 in lattice units.

### 8.3 Not checked here

- T3 and the roughness exponent (L88, L115 after its first sentence), T1-T10 otherwise, Routes 1 and 3 beyond the
  crossed-channel identity, Route 2 (b)-(e), (EX)/(PQ-EX), (TR-LF): outside the list of row 984.
- Lemma IHC itself (its check is row 981; I re-did its four steps only as used in Lemma EE (a)).
- The inputs of Theorem ZD (Theorem SH, Proposition Delta, Lemmas Z', E', Corollary S3'), and the proof of CA-I
  Theorem 4.14 and where the account verifies varpi <= q_-/4 for the step.

### 8.4 What this moves

The direction verdict on N2 (row 982, 8.1 items 1-3) stands with the corrections: the port gives level-free uniform
log-concavity below the unit, now with the account's own theorem behind the form bound; Lemma CAP (c), checked here,
is the exact reason a fine-lattice proof through Theorem BR needs bridge constants of order beta_0 a_iota M with the
bare coupling. The statement to keep at the unit is (U1) or (U2); the pointwise (UNIT-EE) is a sufficient condition for (U2) on
the range, not a weaker form, and the integral form of Lemma EE (c) is the seed itself.

RESULT: Row 984 (Claude Opus 5.5 max, Mac mini worker 1; one line-by-line check of row 982 by another model, not an audit; no numeric run). HOLDS: the end inequalities of Theorem BR (iv) at q = p = 2, Var_(nu_s)(u_s) = F(s) for mean-zero f, Lemma CAP (a), (a') (end limits now written), (b) and (c) as inequalities, Lemma TEL, Lemma EE (a)-(d) (given Lemma IHC), Lemma COUNT (a)-(c), Route 2 (a), the crossed-channel identity, (P2), (P4). HOLDS AFTER CORRECTION: L70 (CAP (b) is weaker than (BR-gap), which gives (1/2) integral gam_s ds <= E_1; no two-sided statement), the 4.2 heading ((U3) implies (U2) on [tau_0, ell], not the converse, so (UNIT) is not implied by (HC-phys); keep (U1) or (U2)), COUNT's reading ("implies"), N2's "one object" claim (precise form: (TH) and (HC-phys) imply (BDD-Delta) and (Z-UNB) through the seed and Theorem ZD-c; converse unknown) and L163, (P1) (the form bound is the account's own Theorem 4.14 (B), (I), CA-I 46035, declared PROVED, imported as a hypothesis by CA-II 8.2-8.3), (P3) (cite CA-II 83846-83855), L225 (Poincare nuance). FAILS: two sentences as written (L70, L131); no proved lemma of row 982 fails. Still OPEN: (UNIT), (U1), (U2), (HC-phys), (PQ-EX), (TR-LF), T3 and the roughness exponent (ARGUED, not checked here); not checked: Lemma IHC (row 981), the inputs of Theorem ZD, the proof of CA-I Theorem 4.14.
