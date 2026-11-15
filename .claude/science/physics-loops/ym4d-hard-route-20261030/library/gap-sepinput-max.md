lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T18:17Z

# gap-sepinput-max (row 996): the separating input

Worker: Claude Fable 5.2, max effort, Mac mini worker 1, pinned at commit 9b1fee9fb.
Kind of result: direction item. Nothing here is checked by another model. Nothing here is a public claim.

Goal of the row: an input that tells the isotropic Wilson SU(2) trajectory from the K7 endpoint family
beyond first passage, in a form that an exact tool of the lane can use.

## Status log (times from `date -u`)

- 06:17Z start. Output file created. No earlier run of this item exists at the pinned commit.

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
