lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T18:17Z

# gap-sepinput-max (row 996): the separating input

Worker: Claude Fable 5.2, max effort, Mac mini worker 1, pinned at commit 9b1fee9fb.
Kind of result: direction item. Nothing here is checked by another model. Nothing here is a public claim.

Goal of the row: an input that tells the isotropic Wilson SU(2) trajectory from the K7 endpoint family
beyond first passage, in a form that an exact tool of the lane can use.

## Status log (times from `date -u`)

- 06:17Z start. Output file created. No earlier run of this item exists at the pinned commit.
- 06:23Z Step 1 written. 06:37Z Step 2. 06:47Z Steps 3 and 4. 06:51Z Section 5.0 to 5.4.
- 06:50Z and 06:52Z two numeric runs under the lock (holder row996-sepinput, memory 71 percent free, each under 1 minute).
- 06:54Z correction: the last two bullets of 5.4 were replaced. The three-face control showed that the tilt supremum is
  not attained on the homogeneous axis; Lemma SHEET (5.5) then showed that it is unbounded in the volume.

## Plan (eight steps, one per response)

1. Read only the definition of K7 (row 708). Write my own candidate separating properties from the object alone.
2. Read the consumer statements ((U1)/(U2), Corollary Z4, the ceilings, "first passage"). For each candidate:
   true at Wilson SU(2)? false at K7, U(1), Q_8, 2T, the ceilings? consumer?
3. Read `library/prior/gap-sepinput-read-opus.md` (row 995). Grep rows 697-720, 859, 876, 962, 970, 988 and
   the gap-brainstorm files for each candidate. Mark each NEW or FOUND with the row.
4. Choose the best NEW candidate that has a consumer. Run the duplicate check (open-core.md, FINISH rows).
5. Attack, stage 1: state the consuming lemma exactly and prove its first half, or find the failing line.
6. Attack, stage 2: finish the proof, or give the exact line where it fails.
7. Self-check of every statement marked PROVED or ARGUED (a second derivation where one exists).
8. Summary table, credits, what stays open, RESULT line.

Marks used: PROVED (written argument, every step, unchecked by another model), ARGUED (argument with a named
gap), OPEN, FAILS (with the failing line). GUIDE marks a numeric observation; it proves nothing.

## 1. Step 1: my own candidates, written from the object alone

Read before this section: GOAL.md, FINISH.md lines 1-84, row 996, and the definition of K7 only
(`gap-mid-max.md` L48: the one-plaquette weight exp(beta_F x + beta_A (4 x^2 - 1)/3), x = (1/2) tr U_p, on its
first-order line, which ends near (beta_F, beta_A) = (1.5, 0.9)). No route file was read. Statements marked
RECALLED are from memory and are not verified here.

Notation. SU(2) = S^3 = unit quaternions in R^4, <.,.> the inner product of R^4, x = <1, U>. The Wilson weight is
w_W(U) = exp(beta x). Put c = 4 beta_A / 3, so the K7 weight is exp(-beta_A/3) exp(beta_F x + c x^2).

**Three exact facts about the two weights (each is a one-line computation).**

- (F-LIN) A plaquette variable is U_p = U_1 U_2 U_3^* U_4^* and the quaternion product is bilinear. So x_p is affine
  (in fact linear) in each of its four links, as a function on R^4. The Wilson action is linear in each link. The K7
  action is quadratic in each link.
- (F-MIX) exp(c x^2) = E exp(s x) for s Gaussian with mean 0 and variance 2c. So
  w_K7(x) = exp(-beta_A/3) E_s exp((beta_F + s) x), and on every finite lattice
  Z_K7 = exp(-beta_A abs(P)/3) E_s Z_W({beta_F + s_p}), with independent s_p of law N(0, 8 beta_A/3), one per plaquette.
  K7 is the Wilson model with annealed, independent, Gaussian plaquette couplings. At (1.5, 0.9) the couplings have
  mean 1.5 and standard deviation 1.55; negative couplings have positive weight.
- (F-CONV) (log w_W)'' = 0 in x. (log w_K7)'' = 8 beta_A/3 > 0. Every mixture of Wilson weights is log-convex in x
  (Hoelder). The Wilson weight is an extreme ray of the cone of such mixtures.

**Candidates.** Each is a property P with "P holds for Wilson SU(2)" exact or expected, and "P fails at K7".

- **B1, vMF link law (from F-LIN).** Given all other links, one Wilson link has the von Mises-Fisher law
  exp(<U, h>) dU on S^3, with the single field h = beta S in R^4, S the sum of the six staples, abs(h) <= 6 beta.
  The link integral is exact: int exp(<U,h>) dU = Psi(abs(h)^2), Psi(z) = sum_k z^k / (4^k k! (k+1)!) =
  2 I_1(sqrt z)/sqrt z = product over k of (1 + z / j_(1,k)^2), with j_(1,k) the zeros of J_1. So Psi has the
  Lee-Yang property in z, and log Psi is concave in z >= 0. At K7 the link law is a Fisher-Bingham law: it reads the
  staples through S and through the 4 x 4 matrix sum of V_p V_p^T, and it can have two antipodal modes.
- **B2, no hidden plaquette field (from F-MIX).** Wilson is the point mass in (F-MIX). A statement about Wilson that
  holds for all inhomogeneous couplings {beta_p} in R^P and survives a positive mixture holds at K7. So a separating
  input must use that the coupling is the same number on every plaquette (or lies in a short interval). In cumulant
  form: K7 has a transition only if Lambda(s) = log Z_W(beta_F + s) - log Z_W(beta_F), s in R^P, beats the Gaussian
  weight sum s_p^2 / (4c). A sub-Gaussian bound Lambda(s) <= <m, s> + (sigma^2/2) abs(s)^2 with 2 c sigma^2 < 1 is the
  matching "no transition" input. It implies a bounded plaquette susceptibility.
- **B3, log-concavity in x.** P: (log w)'' <= 0 on [-1, 1]. Wilson has equality. K7 fails with 8 beta_A/3.
  Weaker forms: w monotone in x; w has one local maximum on the group. K7 fails both on its first-order line if
  beta_A > 3 beta_F / 8 there (true at the endpoint: 0.9 > 0.5625), because then U_p = -1 is a second local maximum.
  But I expect these weaker forms to be useless: van Enter and Shlosman (RECALLED, CMP 2005) prove a first-order
  transition for gauge weights exp(beta ((1 + x)/2)^p) at large p. Those weights are monotone in x, unimodal,
  absolutely monotone in 1 + x, and have positive characters. At p = 1 they are Wilson. They are log-convex in x.
  So within that family log-concavity in x is the first property that singles out p = 1.
- **B4, total positivity of the Fourier sequence.** On the maximal torus w_W = sum_n I_n(beta) e^(i n theta), with
  generating function exp((beta/2)(t + 1/t)). By the Aissen-Schoenberg-Whitney-Edrei theorem (RECALLED) a two-sided
  sequence is totally positive exactly when its generating function is C t^k exp(a t + b/t) times a product of
  factors (1 + alpha_i t), (1 + beta_i / t), 1/(1 - gamma_i t), 1/(1 - delta_i / t). So (I_n(beta))_n is totally
  positive. The K7 generating function is exp((beta_F/2)(t + 1/t) + (beta_A/3)(t^2 + 1/t^2)), which is not of
  that form. The SU(2) character coefficients are c_j = I_(2j+1)(beta)/I_1(beta), a subsequence. The heat-kernel
  weight also has the property (Jacobi triple product). So does Wilson U(1).
- **B5, conditional rotor structure (from F-LIN).** Given the spatial links, the temporal links of one time slab are
  an O(4) rotor model on Z^3 with a bilinear action sum over (x,i) of beta <U_0(x), B U_0(x+i) A^*> in a background
  SO(4) connection (A, B the two spatial links). So the tools of bilinear rotor models apply slab by slab: the
  random-walk representation with positive local-time weights and holonomy factors, and exact Gaussian-type
  integrals. At K7 the slab action is quartic.
- **B6, observable inputs (hypotheses, not properties of the weight).** (a) The plaquette susceptibility
  chi_P = sum_q <x_p; x_q> is bounded on [2.3, 2.6], uniformly in the volume. It diverges at the K7 endpoint
  and is a point mass on the K7 line (RECALLED physics). (b) Z_Lambda(beta) has no zero in a complex neighbourhood of
  [2.3, 2.6] of fixed width, uniformly in Lambda. False on the K7 line and at its endpoint. (c) Uniqueness of the
  Gibbs state: true at the K7 endpoint, so it does not separate.
- **B7, against the other groups.** Q_8 and 2T carry the same function exp(beta x), so the weight cannot separate
  them: only the Lie structure can (integration by parts on the group, a continuous orbit of the staple field).
  U(1) Wilson has (F-LIN) in R^2, (F-CONV) and B4. What it lacks: Ricci curvature 2 of S^3, a finite centre, a
  trivial fundamental group.

**First ranking, before any reading.** (F-MIX) is the sharpest statement I have: it says what K7 is in Wilson terms.
B1 and B5 are the forms an exact tool can use. B3 is the cheapest to test against other families. B4 is exact but I
see no consumer in four dimensions yet. B6 is the honest form of "what is true of Wilson", and it is as hard as the
gap.

## 2. Step 2: each candidate against Wilson, the comparison models, and a consumer

Read for this step (statements only): (U1), (U2) and Route 3 in `gap-unit-max.md` L33-56, L231-262, L348-357;
Theorem D and Corollary D2 (`gap-crux-restate.md` L90-123); Lemma Z to Corollary Z4 (`gap-phys-seed.md` L253-327);
Lemma REG and Proposition V (`gap-crux-fp.md` L342-358); the ceilings (`gap-status-1113.md` L68, L110, L112, L341).

**What "beyond first passage" means (from row 988).** The account's flow is defined up to the first passage of
the unit coupling into its window (CA-I 631-683). Beyond it the coupling is of order one. The comparison is with
the mixed-action endpoint: cubes with light levels at order-one coupling.

**What a consumer is.** The lane's exact tools read partition functions of periodic tori. The seed is
Phi(n) = 16 F(n^4) - F((2n)^4) <= 1.9 x 10^(-4) at one n (Theorem D (b), Theorem S). Theorem D (f) is an identity:
Phi(n; beta) = 96 n^4 int_0^beta (abar_2n(s) - abar_n(s)) ds. Corollary Z4: with D bounded, either every cube of
side b has a level within (256 D_0 + 29.64)/b of its ground level, or there is a seed. So a consumer needs one of:
(SEED) at one size; a bound on the finite-size shift of the mean plaquette along the whole path [0, beta]
(Theorem D (f)); b m(b^3) > 256 D_0 + 29.64 at one b (Corollary Z4); a zero-free neighbourhood of the path (Route Z);
a bounded logarithmic rate along the coupling ((VIR_K), row 708 C-A).

**Two observations that order the table (both are short arguments, PROVED at the level of this note).**

- (O-THERMAL) The seed is thermal: 1 + S(n; B) = Tr T^n / lambda_0^n counts every level of the box in every
  sector. A flux level of the periodic box is invisible to local observables. So an input about local correlations
  at the one coupling beta cannot give the seed. Test models: Q_8 and 2T in their frozen phase and U(1) in its
  Coulomb phase have summable plaquette correlations (RECALLED: gapped local sector for the finite groups, decay
  r^(-8) for the photon) and no seed. Such an input can separate K7 only, where the light level is a scalar that
  couples to the plaquette.
- (O-PATH) Each comparison model has a point of non-analyticity of f on the real path from the strong-coupling
  region to the coupling where its seed fails: the first-order line or the endpoint for K7, the transition for
  U(1), Q_8 and 2T (RECALLED numerics: 2T freezes near beta 2.2, Q_8 lower). Wilson SU(2) is expected to have none
  on [0, 2.6]. So the inputs that separate all five models at once are path statements: (ZF), (VIR_K), and the
  finite-size shift of Theorem D (f). All three are in the lane. A structural property of the weight separates
  K7 only if the Wilson weight is on the boundary of the property.

**Additions to the list, found while judging (still before the digest was read).**

- **B8, heat-kernel mixture.** The Wilson weight is itself a mixture: I_n(beta)/I_1(beta) = int exp(-(n^2 - 1) t/2)
  eta~_beta(dt), with eta~_beta the Hartman-Watson law tilted by exp(-t/2) (RECALLED: Hartman and Watson 1974, the
  von Mises-Fisher law is a mixture of Brownian laws on the sphere; Kent 1977, the mixing law is infinitely
  divisible). So c_j = I_(2j+1)/I_1 is a mixture of heat-kernel coefficients exp(-2 t j(j+1)), and the kinetic
  factor of the transfer operator is K = exp(-sum over links of psi_beta(-Delta_link)) with psi_beta a Bernstein
  function: a Levy semigroup at time one. Consequence for B2: Wilson is extreme among mixtures of Wilson weights,
  and not extreme among mixtures of heat kernels. "Being a point mass" is relative. Also, for every c > 0,
  exp(beta x) = E_s exp((beta + s) x - c x^2): Wilson is a Gaussian mixture of negative-adjoint weights.
- **B9, Turan inequality.** c_1 <= c_(1/2)^2, and k -> c_(k/2) is log-concave, for Wilson at every beta
  (I_n^2 >= I_(n-1) I_(n+1); RECALLED, Thiruvenkatachar and Nanjundiah 1951, Amos 1974). A mixture of a flat part
  and a peaked part reverses it: with coefficients rho (1 - eps C_2(j)), rho < 1, the ratio c_1/c_(1/2)^2 is about
  1/rho > 1. So it should fail for the van Enter-Shlosman weights at coexistence. Value at K7: not computed yet.
- **B10, Gaussian domination in the time direction (from F-LIN).** In a gauge with unit temporal links on a
  slab, a temporal Wilson plaquette is 1 - (1/2) abs(U_i(x, t+1) - U_i(x, t))^2. That is the Froehlich-Simon-Spencer
  form, so shifts h of the difference are dominated: Z(h) <= Z(0) (ARGUED; the reflection step is standard, the
  gauge fixing on a torus leaves one slab of holonomies). Gauge averaging removes every cross term at second order.
  What is left is the one-plaquette bound <1 - x_p> <= 2/beta and a sub-Gaussian tail for one plaquette. No
  information on correlations. At K7 the plaquette term is quartic and the argument has no start.

**Table.** T = true (theorem or exact computation), E = expected, F = false, n/a = does not apply.

| Candidate | Wilson SU(2) | K7 | U(1) Wilson | Q_8, 2T | Consumer |
|---|---|---|---|---|---|
| F-MIX / B2: point mass among Wilson mixtures | T (exact) | F (Gaussian mixture) | T | T | none as an input; gives a no-go test (below) |
| B1: vMF link law, Psi in the Lee-Yang class | T (exact) | F (Fisher-Bingham) | T (in R^2, I_0) | F (finite sum, not a function of abs(h)) | none found: worst-case link response is the 1/3 ceiling; (ZF) is not implied |
| B3: log-concave in x | T (equality) | F | T | T | none; no theorem "log-concave gives a seed" |
| B3 weak: monotone in x, unimodal | T | F on the line if beta_A > 3 beta_F/8 | T | T | none; van Enter-Shlosman weights have it |
| B4: totally positive Fourier sequence | T (Edrei) | F (Edrei) | T | n/a | none in four dimensions |
| B5: bilinear slab rotor | T | F (quartic) | T | T | the lane uses it as an obstruction (4 G_3) |
| B6a: bounded plaquette susceptibility at beta | E | F at the endpoint | T in the Coulomb phase | T frozen | none (O-THERMAL) |
| B6b: zero-free neighbourhood of [0, beta] | E | F | F | F | Route Z (in the lane) |
| B7: Lie structure, Ricci 2, finite centre | T | T | F (flat, centre U(1)) | F (finite) | none alone: K7 has all of it |
| B8: heat-kernel mixture, K a Levy semigroup | T (given the sources) | not known | T (Hartman-Watson) | n/a | none found |
| B9: Turan, c_1 <= c_(1/2)^2 | T | to compute | T | T | none at beta 2.3 (u = 0.48, no convergent expansion) |
| B10: time-direction Gaussian domination | T (ARGUED) | F | T | T | none: collapses to one plaquette |
| (VIR_K): bounded logarithmic rate on the path | E | F | F | F | Theorem TR (in the lane) |
| finite-size shift of abar on [0, beta] | E | F | F | F | Theorem D (f); it is the seed |

**The no-go test that (F-MIX) gives (Lemma MIX, stated here, proved in Section 4 if it is NEW).** Let H be a
hypothesis on the unnormalised Wilson measure with plaquette-dependent real couplings (beta_p). If H holds for
every coupling field, and if H is preserved by positive mixtures over coupling fields, then H holds at K7. So no
such H can enter a proof of the seed. Every per-plaquette statement that is linear in the weight is of this
kind: positivity of characters, reflection positivity, Lemma A, the vMF link law given the couplings, the bilinear
slab structure given the couplings. The separating content must sit in the equality of the couplings.

**Verdict of Step 2.** Among the properties of the weight, none has a consumer. The inputs with a consumer are
the three path statements, and they are the lane's own. What I add so far is (F-MIX), B8, and the two observations.

## 3. Step 3: the digest of row 995 and the grep of the lane; NEW or FOUND

Read: `library/prior/gap-sepinput-read-opus.md` Sections 1, 3.1 (consequence), 4.4, 5.2, 6 (reading), 8. Grepped in
`library/gap-*.md` and `library/prior/gap-*.md`: annealed, mixture, Hubbard, Hartman, infinitely divisible, von Mises,
Lee-Yang, totally positive, Edrei, log-concave, log-convex, Gaussian domination, bootstrap, Bianchi, density of
states, microcanonical, elliptope, coupling field, plaquette tilt.

| Candidate | Mark | Where it already is |
|---|---|---|
| F-LIN, the action is linear in each link as a vector of R^4 | FOUND | row 859, idea 41 (c) (`gap-brainstorm-max.md` L329); row 708 (`gap-mid-max.md` L357: "the one-link law is fixed by one vector, the sum of the staples") |
| B1, vMF link law | FOUND | 61 files; worst-case link responses are the ceilings 1/3 and 0.775 (rows 835, 836) |
| B1, Lee-Yang property of the link or plaquette integral | FOUND | row 670 (`gap-skeleton-max-b.md` L581): the one-plaquette integral has it, the Bianchi-constrained system does not (zeros of one 3-cube in the right half-plane, GUIDE) |
| B3, log-linear in x; the separating property is a number, not a quality | FOUND | row 708 (`gap-mid-max.md` L48, L357), row 712 (`gap-crux-fp.md` L363); van Enter-Shlosman is Proposition V there |
| B5, bilinear slab rotor | FOUND | the 4 G_3 obstruction (rows 834, 839) |
| B6a, B6b, (O-PATH) | FOUND | Lemma REG (row 712); Route Z (row 670); the continuity method (M5) of row 737 (`gap-means-max.md` L108): "the set G is open and not closed" in the class |
| B8, Hartman-Watson mixture | FOUND for the Villain form | `gap-tu-retry.md` L477; heat kernel as idea 17 of row 876 (`gap-brainstorm2-max.md` L164). The SU(2) form (heat kernels on S^3, Levy semigroup) is not there; I found no consumer, so I do not pursue it |
| B9, Turan, log-concave character coefficients | FOUND | row 995, 5.2, with the K7 values: c_1 - c_(1/2)^2 = +0.02 at (1.48, 0.90), +0.07 at (1.2, 1.25). Row 995 left the consumer to this row. My answer: none (Section 4) |
| B10, Gaussian domination in the time direction | FOUND | row 712 (`gap-crux-fp.md` L302), with the same bound 1 - 2/beta |
| (O-THERMAL) | FOUND in substance | row 737 (`gap-means-max.md` L29): the even seed (ES) is the form with no flux sector, and it is still thermal |
| Plaquette tilts keep the Wilson family | FOUND as an idea | row 859, idea 4 (`gap-brainstorm-max.md` L280, L353): "needs a bound on the plaquette covariance operator along the path, with random inhomogeneous couplings (some negative)". No statement or number there |
| **F-MIX: K7 is Wilson with annealed Gaussian plaquette couplings** | **NEW** | no hit for it in the lane or in row 995 |
| **Lemma MIX (the no-go test)** | **NEW** | no hit |
| B4, totally positive Fourier sequence | NEW, no consumer | no hit. Not pursued |
| The x-picture: Wilson is a linear tilt of the joint law of the plaquette traces; K7 is an anti-Gaussian tilt | NEW (found in Step 4) | no hit for density of states of plaquette traces, elliptope |

Two facts from row 995 that change the numbers below. The 1981 endpoint (1.48, 0.90) is not a bulk endpoint on
large lattices; bulk coexistence is supported only for beta_A above about 1.3, and the endpoint is near (1.2, 1.25)
(Gavai 1996, Mathur-Gavai, as read in row 995, 3.1). In the variable of (F-MIX), v = 8 beta_A / 3, this is
v* between 3.3 and 4. The earlier value 2.4 belongs to (1.48, 0.90).

## 4. Step 4: the choice, and the duplicate check

**Duplicate check (rule 0a).** `library/open-core.md` (564 lines): no line with K7, mixed action, separating input,
mixture, Turan or density of states. FINISH rows: 995 is the reading for this row; 859 idea 4 is the nearest idea and
was not attacked as a statement; (U1)/(U2) attacks are rows 982, 988 and are not repeated here.

**Turan (row 995's question): no consumer. The exact line.** Log-concavity of n -> c_(n/2) is a property of the
bare one-plaquette weight. A lemma could use it in one place only: to bound the weight of a plaquette of spin j by
c_(1/2)^(2j) inside a sum over spin assignments. Every such sum in the lane is a convergent expansion, and those
stop at beta 0.775 or below (u = I_2/I_1 below 0.19), while u = 0.48 to 0.52 on [2.3, 2.6]. Beyond the expansions
the lane's tools read partition functions of tori, in which the coefficients c_j of one scale never appear alone;
row 995 notes that decimation does not keep the property. So the first line of any consuming lemma, "expand in
characters and bound term by term", already fails in the window. Mark: FAILS as an input in the window. It stays a
correct label of the weight.

**The candidate I attack: (F-MIX).** It is NEW, exact, and it has consumers of two kinds.

- (i) The lane's fact test (iv), "the candidate must fail at K7". With (F-MIX) the test becomes mechanical for a
  class of hypotheses (Lemma MIX, Section 5.1).
- (ii) Row 859's idea 4 and every criterion of the kind "a covariance bound that is uniform in the tilt". For
  plaquette tilts K7 is exactly the Gaussian mixture of the tilted Wilson measures. So such a criterion can be
  tested at K7 with a number (Proposition TILT, Section 5.2).

What (F-MIX) cannot be: an input that gives the Wilson seed. Wilson is the member v = 0 of the family. To get
anything at v = 0 from the mixture identity one must start at a negative v (a negative adjoint term) and know the
tilt-uniform covariance there. Section 6 states that as a property of the joint law of the plaquette traces, proves
it for three faces, and shows that it fails for four.

Plan change for Steps 5 to 8: Step 5 proves Lemma MIX, Proposition TILT and its corollaries. Step 6 is the
x-picture, with the exact line where the Wilson-side input fails. Step 7 is the self-check. Step 8 is the summary.

## 5. Step 5: the mixture identity as an exact tool (Identity MIX, Proposition TILT)

### 5.0 Setting

Lambda is a finite torus, L its links, P its plaquettes. For a coupling field b in R^P and a real v:

 mu_(b,v)(dU) = Z(b,v)^(-1) exp( sum_p ( b_p x_p + (v/2) x_p^2 ) ) dU, F(b,v) = log Z(b,v), C(b,v) = Cov_(mu_(b,v))(x), a P x P matrix.

Wilson at beta is mu_(beta 1, 0). K7 at (beta_F, beta_A) is mu_(beta_F 1, v) with v = 8 beta_A/3 (the constant
exp(-beta_A/3) per plaquette cancels). Hess_b F = C. Put

 Sigma^2(v) := sup over b in R^P of lambda_max(C(b,v)), R(v) := 1/Sigma^2(v).

On a finite torus 0 < Sigma^2 <= abs(P), because abs(x_p) <= 1. Both depend on Lambda.

### 5.1 Identity MIX (PROVED)

Let w > 0 and gamma_w = N(0, w) on each plaquette, independent. Then:

- (a) Z(b, v + w) = int gamma_w(ds) Z(b + s, v).
- (b) Draw s from pi(ds) := gamma_w(ds) Z(b+s, v)/Z(b, v+w), then U from mu_(b+s, v). The law of U is mu_(b, v+w). Given U, the
  s_p are independent with law N(w x_p(U), w). So s = w x(U) + sqrt(w) xi, with xi standard Gaussian, independent of U.
- (c) pi has the density proportional to exp(-H(s)), H(s) = abs(s)^2/(2w) - F(b+s, v), and Hess H(s) = 1/w - C(b+s, v).

Proof. For one real x, int gamma_w(ds) e^(s x) = e^(w x^2/2). All integrands are positive and abs(x_p) <= 1, so Fubini
applies. The joint density of (U, s) is proportional to exp(-abs(s)^2/(2w) + sum_p (b_p + s_p) x_p + (v/2) sum_p x_p^2).
Integrate over s: (a) and the first half of (b). Integrate over U: (c). Complete the square,
-s^2/(2w) + s x = -(s - w x)^2/(2w) + w x^2/2: the second half of (b). QED

With v = 0 and b = beta_F 1 this is (F-MIX): K7 is the Wilson model with annealed Gaussian plaquette couplings of
variance 8 beta_A/3. In the direction of the adjoint coupling the partition function obeys the heat equation in the
plaquette couplings: d Z/dv = (1/2) sum_p d^2 Z/d b_p^2.

**Remark MIX (the mechanical form of the K7 test).** (1) A statement about the unnormalised measures
exp(sum b_p x_p) dU that holds for every b in R^P and is kept by positive mixtures holds at K7. (2) A statement
"for every coupling field b, a bound on mu_(b,0)" reaches K7 only through the hidden field s, and by (c) the hidden
field is uniformly log-concave exactly when w Sigma^2(0) < 1. Item (2) is made exact in 5.2.

### 5.2 Proposition TILT (PROVED GIVEN the Brascamp-Lieb inequality)

Let v be real and w > 0 with w Sigma^2(v) < 1. Then for every b in R^P, as matrices,

 C(b, v + w) <= ( Sigma^2(v) / (1 - w Sigma^2(v)) ) 1. So R(v + w) >= R(v) - w.

Proof. By 5.1 (c), Hess H >= kappa := 1/w - Sigma^2(v) > 0 on all of R^P. Brascamp and Lieb (J. Funct. Anal. 22, 1976,
Theorem 4.1; RECALLED, not rebuilt here): for a probability density proportional to e^(-H) on R^n with H twice
differentiable and Hess H > 0, Var(g) <= E <grad g, (Hess H)^(-1) grad g>. For g(s) = <a, s> this gives
Var_pi(<a, s>) <= abs(a)^2/kappa. By 5.1 (b), Cov_pi(s) = w^2 C(b, v+w) + w 1. So

 w^2 <a, C(b, v+w) a> <= abs(a)^2 (1/kappa - w) = abs(a)^2 w^2 Sigma^2(v)/(1 - w Sigma^2(v)),

since 1/kappa = w/(1 - w Sigma^2(v)). The supremum over b gives the second claim. QED

### 5.3 Corollaries (PROVED from 5.2)

- **LIP.** v -> R(v) + v does not decrease on the real line. (If R(v) <= w the claim R(v+w) >= R(v) - w is empty.)
- **K7-A.** Let 0 <= v < R(0). On the torus Lambda, for every beta_F, the matrix C(beta_F 1, v) is at most
  Sigma^2(0)/(1 - v Sigma^2(0)). In particular the specific heat (1/abs(P)) d^2 F/d beta_F^2 = <1, C 1>/abs(P) has this
  bound. If Sigma^2_Lambda(0) <= S for all tori, then for every v < 1/S the limit free energy of K7 is C^(1,1) in
  beta_F on the whole line: no first-order point and no divergent specific heat.
- **K7-B.** If lambda := lambda_max(C(beta_F 1, v)) at some beta_F and v > 0, then Sigma^2(0) >= lambda/(1 + v lambda).
  (If v Sigma^2(0) >= 1 this is immediate. Otherwise invert K7-A.) So at a point of the K7 plane where the variance of
  the total plaquette sum grows faster than the volume (coexistence, or a divergent specific heat),
  Sigma^2_Lambda(0) >= 1/v - o(1) as the torus grows.

**Reading.** Row 712 asked for "a bound on a number (how far log w is from a linear function of x)". The number has
an exact form. The distance is the noise variance v = 8 beta_A/3. The Wilson-side quantity that bounds it is R(0), the
inverse of the largest eigenvalue of the plaquette covariance over all real coupling fields: no transition of the
mixed family at beta_A < (3/8) liminf R_Lambda(0). And the flow law LIP holds on the whole adjoint line, negative
adjoint couplings included.

### 5.4 Numbers (GUIDE) and scope

- One plaquette (exact quadrature, script `/tmp/sep996/scripts/faces.py`, run 06:50Z under the numeric lock, memory 71
  percent free, under 10 s): Sigma^2(0) = 1/4 at b = 0. sup_b Var at v = 1, 2, 3, 3.9 is 0.283, 0.320, 0.360, 0.399;
  the bounds of 5.2 are 0.333, 0.5, 1.0, 10. R(v) + v at v = -3, -1, 0, 1, 2, 3 is 2.77, 3.53, 4, 4.53, 5.12, 5.77:
  it increases, as LIP says. The one-plaquette bound is not sharp.
- On the homogeneous axis lambda_max(C(beta 1, 0)) >= <1, C 1>/abs(P) = d<x_p>/d beta. The published mean
  plaquettes (RECALLED, not re-read: 0.5692 at 2.2, 0.6023 at 2.3, 0.6300 at 2.4) give a slope of about 0.33 near the
  crossover. So R(0) <= about 3, and K7-A can at best exclude a transition of K7 below beta_A of about 1.1. Row 995
  reports no bulk transition at beta_A = 1.25 on 16^4 and an endpoint near (1.2, 1.25), v = 3.3. The two are
  consistent, and K7-B adds nothing to the axis value there (1/3.3 = 0.30 < 0.33). At the retracted endpoint
  (1.48, 0.90), v = 2.4, K7-B would have given Sigma^2(0) >= 0.42.
- Scope (corrected at 06:54Z after the three-face control below; the first version of this bullet called the
  question open). Sigma^2(0) is a supremum over all real coupling fields. It is NOT bounded as the torus grows:
  Lemma SHEET (5.5) gives Sigma^2_Lambda(0) >= (n - 1)/4 on a torus with a side n. So R_Lambda(0) tends to 0 for
  Wilson SU(2) and for every other group, and 5.2 and 5.3 are true and empty on large tori. The remark above
  "if the supremum were attained on the axis" is void: it is not attained there.
- Consumer. Row 859's idea 4 names this bound ("a bound on the plaquette covariance operator, with inhomogeneous
  couplings, some negative") and says that it is needed along typical paths only. Lemma SHEET shows that the form
  with all coupling fields is false, with an explicit field. A form with typical fields is not proved here.

### 5.5 Lemma SHEET: the tilt supremum grows with the torus (PROVED)

**Lemma SHEET.** Let the torus have a side n >= 3 in direction 3, and let 1 <= m <= n - 2. Fix a site x and the stacked
plaquettes p_i = (x + i e_3; 1, 2), i = 0, ..., m. Let Q be the 4m side plaquettes of the m cubes between them, and let
b^(B) be the coupling field with b = B on Q and b = 0 elsewhere. Then

 lim as B -> infinity of Cov(x_(p_i), x_(p_j)) = 1/4 for all i, j, so liminf lambda_max(C(b^(B), 0)) >= (m + 1)/4, and Sigma^2_Lambda(0) >= (n - 1)/4.

Proof. Only the links of the tube enter the weight: the four horizontal links h(i) = (h_1, ..., h_4)(i) around p_i,
i = 0, ..., m, and the four vertical links V(i) of the cube between p_i and p_(i+1), i < m. A side plaquette has the
holonomy k = h(i) V' h(i+1)^* V^*, with V, V' the two vertical links at its ends. For fixed h(i) and V(i), the map
h(i+1) -> k is a bijection of SU(2) that keeps the Haar measure (an inversion and two translations). The change
of variables is triangular in the level i. So in the variables (h(0), all V, all k) the weight is the product of
exp(B x(k)) over the 4m side plaquettes: h(0) and V are Haar, the k are independent with the law proportional to
exp(B x(k)) dk, and everything is independent. U_(p_0) is a product of four independent Haar links, so it is Haar:
E x_(p_0) = 0 and Var x_(p_0) = int x^2 (2/pi) sqrt(1 - x^2) dx = 1/4. Solving for h(i+1) = V^* k^* h(i) V' gives
U_(p_(i+1)) = V_0^* k_1^* h_1 k_2^* h_2 h_3^* k_3 h_4^* k_4 V_0, which is conjugate to U_(p_i) when the four k are 1.
As B grows each k tends to 1 in probability. So x_(p_i) - x_(p_0) tends to 0 in probability, and in L^2 because it
is bounded by 2. Hence Cov(x_(p_i), x_(p_j)) tends to Var x_(p_0) = 1/4, and Var(sum_i x_(p_i)) tends to
(m+1)^2/4. The Rayleigh quotient of C with the indicator vector of {p_0, ..., p_m} is Var(sum_i x_(p_i))/(m+1). QED

Remarks. (1) The proof uses a class function with positive variance and nothing else: it holds for every group. A
two-dimensional sheet of parallel plaquettes gives a bound of order n^2 in the same way. (2) The frozen side
plaquettes turn the stack into one variable. No property of the weight can prevent this, because the coupling
field is free. (3) GUIDE control (run 06:52Z, script `/tmp/sep996/scripts/cube.py`, 400,000 Haar samples): for three
faces g_1, g_2, g_1 g_2 the largest eigenvalue of the tilted covariance rises from 0.25 at b = 0 to 0.435 at
b = (5.2, 0, 0) and tends to 1/2, the value of two identified faces.

**Consequence: the exact line where the tool fails.** Proposition TILT needs Hess H >= kappa > 0 at every s in R^P.
By Lemma SHEET, lambda_max(C(b + s, 0)) exceeds 1/w for s in a set of fields that freeze a tube longer than 4/w.
That set has a positive, very small Gaussian weight. So H is not convex on R^P once n - 1 > 4/w, and the
Brascamp-Lieb step has no start. Mark: Proposition TILT is PROVED and is empty on large tori; "a tilt-uniform bound on
the plaquette covariance" FAILS for every group.

**What survives: the one-dimensional form (Proposition MF, PROVED GIVEN the Brascamp-Lieb inequality in dimension one).** Take one
global shift s for all plaquettes, with law N(0, w/abs(P)). Then E_s exp(s E) = exp(w E^2/(2 abs(P))), E = sum_p x_p:
the mixture is the Wilson model with a mean-field coupling of the total energy to itself. The hidden variable has
H(s) = abs(P) s^2/(2w) - F(beta + s), a function of one variable, and only the homogeneous axis enters. Let
X_Lambda := sup over real beta of F''(beta)/abs(P), the largest specific heat on the axis. If w X_Lambda < 1, the same
three lines as in 5.2 give Var(E)/abs(P) <= X_Lambda/(1 - w X_Lambda) for the mean-field model, at every beta. Conversely, a
double peak of E in the mean-field model at some w forces X_Lambda >= 1/w - o(1). So "the specific heat is bounded on
the whole Wilson axis, uniformly in the torus" is the same statement as "Wilson is stable under a small mean-field
energy coupling". It is expected for SU(2), false for Z_2, Q_8, 2T (first order on the axis; RECALLED) and it is
B6a: FOUND as the conclusion of Lemma REG, with no converse. The K7 direction is the local form of the same
coupling, and for the local form the axis is not enough: that is the content of Lemma SHEET.

## 6. Step 6: the Wilson-side input in trace variables, and the exact line where it fails

**6.1 The picture.** Let rho_Lambda be the law of the vector x = (x_p) under the Haar measure on the links. It is
a probability measure on [-1, 1]^P and it does not depend on any coupling. The law of x under mu_(b,v) is
proportional to exp(<b, x> + (v/2) abs(x)^2) rho_Lambda(dx). So in trace variables Wilson is a linear tilt of rho_Lambda,
a negative adjoint term is a Gaussian tilt, and K7 is an anti-Gaussian tilt. This is the exact form of "the Wilson
weight is log-linear in x" for the whole lattice, not for one plaquette.

**6.2 The input that would make 5.2 work from the Wilson side (DOS-kappa).** "rho_Lambda has a density exp(-phi) on a
convex set, with Hess phi >= kappa >= 0." If it held with kappa > 0, Brascamp-Lieb would give C(b, v) <= 1/(kappa - v)
for every b and every v < kappa: a tilt-uniform bound, R(0) >= kappa, and no transition of K7 below v = kappa.
One plaquette has it with kappa = 1: rho_1 = (2/pi) sqrt(1 - x^2), -(log rho_1)'' = (1 + x^2)/(1 - x^2)^2 >= 1.
Plaquettes whose based loops are part of a free basis of the loop group (no closed surface) are independent Haar
elements, so they have it with kappa = 1 too.

**6.3 Proposition ELL (three faces; PROVED).** Let g_1, g_2 be independent Haar elements of SU(2) and
x = (Re g_1, Re g_2, Re(g_1 g_2)). Then x is uniform on the elliptope
E_3 = {x in [-1,1]^3 : 1 + 2 x_1 x_2 x_3 - x_1^2 - x_2^2 - x_3^2 >= 0}, with density 2/pi^2.
Proof. Write g_i = cos theta_i + sin theta_i n_i with n_i a unit imaginary quaternion. Under Haar, x_i = cos theta_i
has the density (2/pi) sqrt(1 - x_i^2), n_i is uniform on the 2-sphere, and all four are independent.
Re(g_1 g_2) = x_1 x_2 - s_1 s_2 (n_1 . n_2), s_i = sqrt(1 - x_i^2), and n_1 . n_2 is uniform on [-1, 1] (Archimedes).
So given (x_1, x_2), x_3 is uniform on [x_1 x_2 - s_1 s_2, x_1 x_2 + s_1 s_2], with density 1/(2 s_1 s_2). The joint
density is (2/pi)^2 s_1 s_2/(2 s_1 s_2) = 2/pi^2 on {(x_3 - x_1 x_2)^2 <= (1 - x_1^2)(1 - x_2^2)}, which is E_3. QED
E_3 is the set of 3 x 3 correlation matrices, a convex body. So three faces with one relation have (DOS-kappa) with
kappa = 0 exactly: log-concave, and not strictly.

**6.4 Proposition 4F (four faces; PROVED by hand).** Let g_1, g_2, g_3 be independent Haar elements and
x = (Re g_1, Re g_2, Re g_3, Re(g_1 g_2 g_3)), theta_i = arccos x_i. Then x has the density
rho_4(x) = (2/pi^3) abs(J(theta)), where J is the interval
[max(abs(theta_1 - theta_2), abs(theta_3 - theta_4)), min(theta_1 + theta_2, 2 pi - theta_1 - theta_2, theta_3 + theta_4, 2 pi - theta_3 - theta_4)]
(empty if the ends cross). rho_4 is not log-concave.
Proof. Put h = g_1 g_2 and y = Re h = cos delta. By conjugation invariance the law of (x_3, x_4) given (g_1, g_2)
depends on y only and equals the law of the last two coordinates of Proposition ELL given the first one equal to y.
So rho_4(x) = int rho_3(x_1, x_2, y) rho_3(y, x_3, x_4)/rho_1(y) dy = (2/pi^2)^2 (pi/2) int dy/sqrt(1 - y^2) over the y that
lie in both elliptopes. In the variable delta the two conditions are the two intervals whose intersection is J, and
dy/sqrt(1 - y^2) = d delta. Now take theta = (0.5, 0.4, 0.4, 0.4). Then J = [0.1, 0.8], and for theta_1 in (0.4, 1.2) with
the other three fixed, abs(J) = 1.2 - theta_1 = 1.2 - arccos x_1 =: l(x_1). l' = 1/sin theta_1, l'' = cos theta_1/sin^3 theta_1, and
(log l)'' = (l cos theta_1 - sin theta_1)/(l^2 sin^3 theta_1). At theta_1 = 0.5: l = 0.7, cos = 0.8776, sin = 0.4794,
0.7 x 0.8776 - 0.4794 = 0.1349 > 0. So log rho_4 is strictly convex along the x_1 axis at this point
((log l)'' = 2.498). QED
Control: the character form rho_k = (2/pi)^k sum_n n^(2-k) prod_i sin(n theta_i) gives the same density and the same
second derivative 2.49802 (run 06:50Z, closed form against a 20,000-term series).

**6.5 The cube (GUIDE).** By a shelling of the five-face disc, five of the six plaquette loops of a cube, with base
paths, form a free basis and the sixth is the inverse of their ordered product. So the six traces of one cube have
the law of (Re g_1, ..., Re g_5, Re(g_1 ... g_5)), with density rho_6 = (2/pi)^6 S_6,
S_6 = -(1/64) sum over signs eps in {+1,-1}^6 of (prod eps_i) C_4(sum eps_i theta_i), C_4(phi) = pi^4/90 - pi^2 phi^2/12 +
pi phi^3/12 - phi^4/48 for phi in [0, 2 pi], continued with period 2 pi. Finite differences of this closed form: of 3,923 random
interior points, 27 have a positive eigenvalue of the Hessian of log rho_6 in x. The largest is +0.4449 at
theta = (0.4549, 2.3264, 2.5543, 0.2898, 2.9478, 2.9907), direction (0.203, -0.920, -0.336, 0, 0, 0); the second difference
is 0.44489, 0.44486, 0.44486, 0.44485, 0.44485 at steps 4, 2, 1, 0.5, 0.25 times 10^(-3). No violation was found
along a coordinate axis at round points. So rho_6 is not log-concave either, in a small part of its support.
The marginal of a log-concave measure is log-concave (Prekopa), and rho_6 is a marginal of rho_Lambda. So
rho_Lambda is not log-concave on a hypercubic torus (GIVEN the GUIDE evaluation; a hand proof is a finite
computation with a piecewise polynomial of degree four and is not done here).

**6.6 Verdict of the attack.** (DOS-kappa) with kappa > 0 uniform in the torus is false by Lemma SHEET alone (PROVED):
it would give R(0) >= kappa. Plain log-concavity (kappa = 0) holds for one, for independent, and for three faces, and
fails at four faces (PROVED) and for one cube (GUIDE). With a defect, Hess phi >= -kappa_1, Brascamp-Lieb applies only
for v < -kappa_1 and gives nothing at v = 0. So the mixture identity cannot be turned into an input for the Wilson
axis by convexity in trace variables. The first failing line is "rho_Lambda is log-concave".
What is left of the picture in one dimension: the density g_Lambda(E) of the total sum E = sum_p x_p. "g_Lambda is
log-concave" says that no torus shows a double peak of the action at any beta. A uniform strict form is the bounded
specific heat of Proposition MF. Both are B6a.
