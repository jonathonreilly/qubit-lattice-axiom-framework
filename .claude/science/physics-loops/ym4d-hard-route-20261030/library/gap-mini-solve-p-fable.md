lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T16:12Z

# gap-mini-solve-p-fable: the mass gap of four-dimensional SU(2) Yang-Mills (row 1220)

Provenance: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit 7ec64b498. One session, no subagents.
Continued from 2026-11-20T04:12Z (date -u) by Claude Opus 5.5, max effort, same Mac mini worker, pinned at commit 3065cacc7
(the Mini account reached its Fable weekly limit; the lead note of row 1220 moves the row to Opus 5.5). Sections 0-1 up to
the line marked below are Fable's text, kept unchanged; everything after it is Opus 5.5's.
This is research-stage working state. It grants no status. Nothing here is a public claim.

Labels: PROVED (argument written in full here), ARGUED (argument with a named gap), GUIDE (numeric or heuristic,
never a proof step), OPEN.

## 0. Status log

- 2026-11-20T03:52Z (date -u): file created. Plan: (1) read the row's new input, `library/prior/gap-onebound-read-sol.md`
  (row 1218), and the lane's state map `parts/gap.md`; (2) per the lesson of rows 1188-1198 (blind candidate
  lists are exhausted for this model family), start from an OPEN lemma with a consumer in the newest chain rows
  and from the new published input, not from a candidate list; (3) grep the registry before calling anything new;
  (4) attack one statement to closure, appending after each step.
- 2026-11-20T04:00Z (date -u): read FINISH.md rule sections, GOAL.md, row 1220 (this row), `library/prior/gap-onebound-read-sol.md`
  in full, `parts/gap.md` L1-104, and the RESULT lines of rows 1186-1218. Section 1 written from these.

## 1. Repo search and how the attack was chosen

**Repo search (this folder; cross-branch hits taken from row 1218's table, not searched again).** The row's
one new input is row 1218's reading of three published texts. Credit: (A) D. Bhattacharjee, U. Bhattacharya,
J. M. Lockwood, T. Romanov, I. J. Sessford, S. Singha Roy, "The Yang-Mills Mass Gap from One Bound at One Scale"
(Preprints.org 202611.1282); (B) Bhattacharjee, Bhattacharya, Lockwood, Romanov, "One Cube Estimate Implies the
Yang-Mills Mass Gap" (Hexagon 2610.00341v7); (C) Zeng Chunping, Hexagon 2611.00543v1 and 2611.00492v1. All are
read here through row 1218's digest unless a section below says a primary passage was read.

State of the lane taken as given (not re-derived):

- The Jaffe-Witten gap clause follows from the neutral one-cube bound (N-phys) and the matched continuum datum
  (row 1161 `gap-solve9-astra62.md` L146-148; row 1179). (N-phys) is the crux lemma (GLUE-FP)_sigma of rows 895
  and 920 with other constants (row 1184). Rows 1186-1215 restate it five ways: two-slice information (26), the
  binary test (28), the probability ratio of row 1192, the mass detector Q of row 1204, the wall test of row 1211.
  Each check (rows 1191, 1203, 1210, 1214) confirms the restatement and that the Wilson estimate is OPEN.
- Fifteen plain-brief rows of this model family (1188-1202, letters a to l) each generated candidate attacks
  from the target and found every one on the lane's map. The lesson recorded after row 1198: do not start from a
  candidate list again.

**How the attack was chosen.** Two questions decide the row.

1. Does the new published input supply, or shorten the way to, the missing Wilson estimate? Section 2 answers
   this with proofs, not by reading alone: for (B)'s weak-coupling theorem the answer is no, and the reason is
   exact (Lemma NULL below).
2. Which open statement with a consumer is attacked? Chosen in Section 3, after Section 2.

---- (end of the Fable 5.2 text; Opus 5.5 continues below) ----

- 2026-11-20T04:19Z (date -u): Opus 5.5 took over the row. Re-read FINISH.md rule sections (L1-84, L299-356), GOAL.md, row 1220,
  `library/prior/gap-onebound-read-sol.md` in full, `parts/gap.md` L1-104, RESULT parts of rows 1199-1219, and row 1215's
  straight-transport paragraphs (`gap-solve23-astra62.md` L445-474). Fable's Lemma NULL (named in Section 1, never written)
  is rebuilt below from these sources; its exact text is lost, so Section 2 is Opus's own statement and proof.
- 2026-11-20T04:24Z (date -u): fetched B's public PDF (hexagonmath.org/pdf/2610.00341v7, 385 pp.) into a scratch folder and read
  pp. 4-5 (overview), p. 83 (Remark 155), p. 85 (summary of Sections P-Q), p. 87 (Theorem 164, Corollaries 165-166).
  Registry grep: "near-Haar", "straight holonom", "Corollary 166", "BP(n", "convolution damping" have no hit in
  library/open-core.md; the near-Haar mechanism is on file as row 1145 (1)-(4) (`gap-solve2-astra62.md` L15-53,
  checked HOLDS by row 1146) and row 1215 L468-474 (check row 1221 pending). Section 2 written from these.

## 2. Does the new published input shorten the way to the missing Wilson estimate?

Short answer: no. For B's weak-coupling theorem this is proved below (2.1-2.4), and B already says the main part
of it in its own Remark 155. For A and C it is a reading (2.5).

### 2.1 What B proves at weak coupling (read in B, v7, pp. 4-5, 83-87)

Credit: D. Bhattacharjee, U. Bhattacharya, J. M. Lockwood, T. Romanov, "One Cube Estimate Implies the Yang-Mills
Mass Gap", Hexagon 2610.00341v7. Quoted facts, page by page:

- p. 85-87, Section Q "Smoothing along the paths": a block variable of the straight-path map is the product of
  the b fine links of its path; given the links off the paths, the interior links of all paths are independent
  ("every Wilson factor contains at most one link of I", p. 87). Convolution with a one-link Wilson density
  contracts every nontrivial representation by q_W = 4 beta_W/(4 beta_W + 1) (Lemma 158). A product of m such
  independent links has a density within eta_m = 48 (1 + 6 beta_W)^2 q_W^(m-2) of 1 (Theorem 160). The law of the
  block variables is a mixture of product laws, each factor within eta_(b-2) of Haar (Theorem 164, display (19)).
- p. 87, Corollary 166: k >= 12, b = 2^k, 0 <= beta_W <= k + 2, n >= 2, L even, 2n + 4 <= L <= e^(2^k/(17k)); then
  the law mu^c of the block variables of SU(2) Wilson on Lambda_(bL) under the straight-path map satisfies BP(n, 1/2).
  B proves it through a column sum of mixed derivatives (Corollary 165), not through a density comparison.
- p. 83, Remark 155 (B's own words, abridged): (H1) "concerns only the law of the block variables at the spacing
  a_0; it is independent of (H2) (Proposition 132), and the product of the Haar measures, the law towards which the
  straight-path maps randomise the coarse links, satisfies BP(n,1) (Proposition 67(ii))"; "the route of this
  subsection, completed, would prove (H1) and nothing about the gap: ... the gap has to come from the non-abelian
  structure, and through Corollary 102 it has to enter (H2)". p. 85 lists as not proved: (H1) along the tuning
  (every torus size), (H1) for U(1), BP along the tuning, the mass gap.

So the non-selectivity of the coarsest-scale input is B's own statement. Sections 2.2-2.4 add three small items to
it, each with a full proof: a two-line route from the mixture-of-products form to a Corollary-166-type bound, the
same bound for the Villain U(1) theory (which B lists as not proved, in its every-torus form), and a statement of
what (H2) must contain at the steps where the block variables are near Haar.

### 2.2 Proposition H (near-Haar laws satisfy BP). PROVED.

Setting (B's Definition 62, read through row 1218): mu a probability law on G^E, E the links of an even torus
Lambda_L, V_x the links based in x + [0,n)^4, P_x f = E_mu[f | links off V_x], E_n(f) = n^(-4) sum_x mu(|f - P_x f|^2);
BP(n, w) means w Var_mu f <= E_n(f) for all real gauge-invariant f.

**Statement.** Let lambda be product Haar on G^E. If mu has a density p with 1 - delta <= p <= 1 + delta (delta < 1),
then mu satisfies BP(n, ((1 - delta)/(1 + delta))^2) for every n with 2n <= L, for all f in L^2 (gauge-invariant or
not). In particular BP(n, 1/2) holds when delta <= 1/6.

**Proof.** (i) lambda satisfies BP(n, 1) for all f (this is B's Proposition 67(ii); a proof for completeness): write
the Hoeffding (ANOVA) decomposition f = sum_S f_S over subsets S of E. Then f - E_lambda[f | links off V] =
sum_(S meets V) f_S, an orthogonal sum, so lambda(|f - P_x f|^2) = sum_(S meets V_x) ||f_S||^2. A link based at y lies
in V_x exactly for the n^4 points x in y - [0,n)^4, so every nonempty S meets at least n^4 of the cubes. Hence
E_n(f) >= sum_(S nonempty) ||f_S||^2 = Var_lambda f.
(ii) Var_mu f = inf_c mu((f - c)^2) <= (1 + delta) Var_lambda f.
(iii) Fix the links omega off V_x. The conditional law mu(. | omega) has density p(., omega)/int p(., omega) d lambda
with respect to product Haar on V_x, and this ratio lies in [(1 - delta)/(1 + delta), (1 + delta)/(1 - delta)]. With
the infimum form of the variance, Var_mu(f | omega) >= ((1 - delta)/(1 + delta)) Var_lambda(f | omega). The marginal of
mu off V_x has density in [1 - delta, 1 + delta] with respect to Haar. So
mu(|f - P_x f|^2) = mu(Var_mu(f | .)) >= (1 - delta)^2/(1 + delta) lambda(Var_lambda(f | .)).
(iv) Sum over x and use (i), (ii): E^mu_n(f) >= ((1 - delta)^2/(1 + delta)) Var_lambda f >= ((1 - delta)/(1 + delta))^2 Var_mu f.
For delta <= 1/6 the constant is at least (5/7)^2 > 1/2. QED. (This is the Holley-Stroock comparison; Holley and
Stroock, J. Stat. Phys. 46 (1987), recalled, the argument is written in full above.)

**Corollary H1 (a Corollary-166-type bound by density comparison). PROVED given B's Theorem 160, or given row 1145 (3).**
Let M = 4 L^4 be the number of coarse links. By B's (19) with Theorem 160 (or row 1145 (3), checked by row 1146) the
law mu^c has density between (1 - eta)^M and (1 + eta)^M with eta = eta_(b-2) (B) or eta = eta((b-2)/(1 + 6 beta_W))
(row 1145 (2)). Since (1 + eta)^M - 1 <= e^(M eta) - 1 and 1 - (1 - eta)^M <= M eta, Proposition H gives BP(n, 1/2)
for every n with 2n + 4 <= L as soon as M eta <= log(7/6), that is
  4 L^4 * 48 (1 + 6 beta_W)^2 q_W^(b-4) <= 0.154.
With b = 2^k, beta_W <= k + 2 and log(1/q_W) = log(1 + 1/(4 beta_W)) >= 1/(4 beta_W + 1), this holds for
L <= c_0 (1 + 6 beta_W)^(-1/2) exp((2^k - 4)/(4 (4k + 9))), c_0 = (0.154/192)^(1/4). The exponent 2^k/(16k + 36)
is of the same form as B's 2^k/(17k) (larger for k > 36, smaller below). So Corollary 166 is, up to the constant in
the torus range, the statement "the block law is within o(1) of product Haar in relative density".

### 2.3 Proposition U (the same bound for the Villain U(1) theory). PROVED.

**Statement.** Villain U(1) lattice gauge theory on Lambda_(bL), d = 4, weight prod_p V_beta(theta_p),
V_beta(x) = sum_(n in Z) exp(-(beta/2)(x + 2 pi n)^2). (a) Given all other links, the law of one link angle theta is a
mixture of wrapped normal laws of variance 1/(6 beta); so its Fourier coefficients obey |c_m| <= exp(-m^2/(12 beta)).
(b) For the straight-path map with b >= 5, the block law has density between (1 - eta_U)^M and (1 + eta_U)^M with
respect to product Haar, eta_U = 2 sum_(m >= 1) exp(-m^2 (b - 2)/(12 beta)) <= 4 exp(-(b - 2)/(12 beta)) once
(b - 2) >= 12 beta log 2. (c) Hence the block law satisfies BP(n, 1/2) for every n with 2n + 4 <= L as soon as
16 L^4 exp(-(b - 2)/(12 beta)) <= 0.154.

**Proof.** (a) The link lies in six plaquettes; in each, theta_p = +-theta + phi_i with phi_i fixed by the other
links. Write a_i = phi_i' + 2 pi n_i (after the sign change theta -> -theta in a term if needed, absorbed into the
sign of phi_i' and n_i). Then sum_i (theta + a_i)^2 = 6 (theta + abar)^2 + sum_i (a_i - abar)^2, abar the mean. The
second term depends on n = (n_1, ..., n_6) only through its class modulo the diagonal shift n -> n + k(1, ..., 1),
and that shift moves abar by 2 pi k. Summing over k inside each class gives sum_k exp(-3 beta (theta + abar + 2 pi k)^2),
a wrapped normal density of variance 1/(6 beta). So the conditional density is a convex combination of wrapped
normals with this variance; the m-th Fourier coefficient of each has modulus exp(-m^2/(12 beta)).
(b) As in B p. 87 and row 1145 (3): the interior links of all paths (first and last link of each path dropped) lie
in no common plaquette, so given all other links they are independent; a block variable is a fixed angle plus the sum
of b - 2 independent angles, whose m-th coefficient has modulus at most exp(-m^2 (b - 2)/(12 beta)). Fourier inversion
on U(1) bounds the deviation of each conditional density from 1 by eta_U; the M block variables are conditionally
independent; average over the conditioning. (c) Proposition H with delta <= e^(M eta_U) - 1, M = 4 L^4. QED.

**Reading (GUIDE for the cited part).** The 4D Villain U(1) theory has a massless photon at large beta (Guth 1980;
Frohlich and Spencer 1982; RECALLED, the same citation as `prior/gap-2don-proofs-read-opus.md` L92 and as Lemma PT's
"Villain U(1) at beta at least 2^14"). So at a fixed large beta, the bounded-torus coarsest-scale bound of
Corollary 166 holds in a massless theory once b >= 12 beta (log(16 L^4/0.154)) + 2. This realises B's Remark 155 on
bounded tori. It does not prove B's (H1) for U(1), which asks for BP on tori of every size at fixed k.

### 2.4 Lemma NULL (what the ascent must contain at a near-Haar step). PROVED.

**Statement.** Fix one level of the straight-path tower: fine law mu on G^E (any compact G with the single-link
contraction of 2.2-2.3), block variables c = (c_e) on M coarse links. Choose on each coarse path a set of k interior
links at distance at least 2 from the coarse sites; let I be their union and W the other links. Suppose that, given
W, the c_e are independent with densities within eta of Haar, and put delta = e^(M eta) - 1 < 1. Then for every
f in L^2(sigma(W)):
  Var(E[f | c]) <= (delta/(1 - delta))^2 Var f,   so   mu(Var(f | c)) >= (1 - (delta/(1 - delta))^2) Var f.
Consequently, if the split inequality (S) of B's Corollary 102 holds at this step with constant C_A, then
  (1 - (delta/(1 - delta))^2) Var f <= C_A E'_(n')(f)   for every gauge-invariant f in L^2(sigma(W)):
the finer-level BP inequality itself, restricted to functions of W, with constant 1/C_A; the coarse term of (S)
gives nothing on these functions.

**Proof.** The joint law of (W, c) is mu_W(dW) p(c | W) lambda(dc) with (1 - delta) <= p <= 1 + delta (product of M
factors in [1 - eta, 1 + eta]). So E[f | c] = int f p(c | W) d mu_W / pbar(c), pbar(c) = int p(c | W) d mu_W in
[1 - delta, 1 + delta]. Since int (f - mu f) d mu_W = 0, E[f | c] - mu f = int (f - mu f)(p(c | W) - 1) d mu_W / pbar(c),
of modulus at most (delta/(1 - delta)) mu|f - mu f| <= (delta/(1 - delta)) (Var f)^(1/2). Square and integrate; then
Var f = mu(Var(f | c)) + Var(E[f | c]). The last claim drops the non-negative coarse term of (S). QED.

**What it means (ARGUED).** The block law tends to product Haar as soon as b_j >> beta log M_j (B's q_W, row 1145 (1)),
that is at a physical length b_j a ~ beta log(L/a) a (a the fine spacing), which tends to zero along the tuning. Every level of the tower
above that length is a near-Haar level; there, BP of the block law is free (Proposition H), and the split inequality
can only pass a physical slow mode f (a smeared field strength, approximable inside sigma(W) by dropping the few
plaquettes that touch I) by proving the finer-level Poincare inequality for it, with all its constant in C_A. So the
physical content of B's route sits in C_A at the first near-Haar step and in the steps below it, at a vanishing
physical length, where the straight-path variables still carry the smooth field. B's own tools also change behaviour
at that length: its Theorem 140 and Corollaries 141-142 (p. 5: gauge covariance bounds the Dobrushin-type sum of
single-link coefficients below by two minus four times the normalised spread) exclude its Dobrushin-sum method for BP
at every level whose single-link conditional laws are concentrated, and Proposition 143 says the obstruction is absent
at the coarsest (spread-out) level. This is consistent with Remark 155 and adds where the gap must enter: not at any
fixed physical scale of the tower.

### 2.5 A and C (reading; no new proof)

- A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy, "The Yang-Mills Mass Gap from One Bound at
  One Scale", read through row 1218 only): its seed A-B* is a full periodic thermal bound on a window of shapes at one
  physical time scale, the same kind of datum as the lane's full periodic seed (row 720 Theorem ZD-c, `gap-phys-seed.md`
  L311; Corollary Z4 L322), and its ascent Theorem 7.56 plays the role of the lane's Theorem S (`gap-crux-restate.md` 3.4).
  Row 1218 records that A's weak-coupling seed is open and that A's own Theorem 7.59 excludes a fixed lattice T_0. So A
  moves the open item to a statement at least as strong as (N-phys) (row 1218 reason 1). No shortening.
- C (Zeng Chunping, Hexagon 2611.00543v1, 2611.00492v1, read through row 1218 only): COH, TUN and SPEC are named
  hypotheses with no Wilson certificate. Remark (elementary, PROVED for any single-link heat-bath or Langevin Dirichlet
  form whose Poincare constant at beta = 0 is finite): SPEC cannot hold as an identity at all couplings, since at
  beta = 0 the transfer operator is the rank-one projection on constants (log gap infinite) while the product-Haar
  Poincare constant is finite. So SPEC can only be a weak-coupling hypothesis, as Zeng uses it. No shortening.

**Verdict of Section 2.** None of A, B, C supplies or shortens the missing Wilson estimate. B's weak-coupling theorem
is the near-Haar property of long straight transports (B's own Section Q; the lane's row 1145 (1)-(4)); it holds in
the massless Villain U(1) theory on bounded tori (Proposition U), and by Lemma NULL the content of B's route must enter
its split inequality at the scale where the straight transports stop carrying the smooth field, which shrinks to zero
in physical units. The row's attack therefore goes back to the lane's own open statement (Section 3).
