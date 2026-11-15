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

