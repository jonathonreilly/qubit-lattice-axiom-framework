-rw-r--r--@    1 jonBridger  staff   28684 Nov 25 01:24 gap-r11-thermal-solve-fable.1795587843.gap-r11-thermal-solve-fable.md
-rw-r--r--@    1 jonBridger  staff   28684 Nov 25 01:23 gap-r11-thermal-solve-fable.latest.gap-r11-thermal-solve-fable.md
lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-25T18:09Z

# gap-r11-thermal-solve-fable (row 1522)

Pinned commit cdfa0ee3f, branch claude/ym4d-hard-route. Started 2026-11-25T06:09Z (date -u).
Status: FINISHED (Sections 1 to 8 written). Author run. Nothing below is checked by another model.

## 0. Plan (written before any reading beyond the queue row)

Task (row 1522): the thermal form of (R11') on cold cubes. Prove
D_s G(t; L^3; s) <= C log L * (-t dG/dt) on cold cubes (G < 1e-3), one coupling of order one, Wilson SU(2);
or a first lemma not equivalent to a closed line; or an obstruction over a stated family.
Also owed: (a) how the thermal weighting on cold cubes changes the volume factor of row 710 Theorem B1;
(b) the step at which a correct method must fail for compact U(1) (Corollary FLOOR as corrected in check 1519);
(c) the next two rows with decisive outcomes.

Steps, each appended here as it finishes:
1. Read check 1519 in full (library/gap-r11-tool-design-fable-check-astra62.md).
2. Read row 1517 sections 4-6 (library/gap-r11-tool-design-fable.md).
3. Read row 710 Theorem U, Theorem B1, (BAND-sc) (library/gap-vir-sc.md).
4. Write the thermal inequality in the exact one-box variables of Theorem U; compute the volume factor.
5. Attack / obstruction; U(1) failure step.
6. Novelty greps (library/open-core.md, FINISH rows), next two rows, RESULT line.

## 1. What was read (written 2026-11-25T06:20Z)

Read in full: FINISH row 1522; check 1519 (`gap-r11-tool-design-fable-check-astra62.md`, all 79 lines); row 1517
Sections 2 to 8 (`gap-r11-tool-design-fable.md` L60-384); row 710 (`gap-vir-sc.md`, all); row 708 Sections 4.1
to 4.5 (`gap-mid-max.md` L96-190) and its K7 lines (L48, L357); row 905 formula (R) (`gap-thermdi-astra.md`
L140-175); row 934 L222-234 (`gap-vacsub-max.md`, the two-level picture at a first-order point); FINISH.md L1-84;
the R11 line of `library/open-registry.md` (L1018). Not read: GOAL.md beyond what FINISH quotes (nothing here
touches the target statement); the proofs of Theorem SH and Lemma E'.

Facts used below, with their standing.
- (F1) Lemma 4.2 of row 708 (checked, row 709): at integer t >= 3 and s outside a countable set N_B,
  dG/ds = 6 t |B| (abar_inf - abar_t).
- (F2) Proof of Proposition SUF, row 710 (checked, row 715): at integer t >= 2, G(t; .) is real-analytic and
  dG/ds = (t/(1+S)) sum over i >= 1 of (DD_i - DD_0) rho_i^t, and -t dG/dt = (t/(1+S)) sum over i >= 1 of E_i rho_i^t.
  Here DD_i - DD_0 = -dE_i/ds on a branch.
- (F3) Corollary U' of row 710 (checked): for 0 < s < 4, every unit eigenvector orthogonal to the vacuum with
  eigenvalue lambda > 0 has s (DD - DD_0) <= E/log(4/s) + s |B| c_s, with c_s := 9 + 12/log(4/s).
- (F4) Theorem TR, Remark CH (row 708); Proposition TR2, Remark COLD (row 1517; HOLD in check 1519).
- (F5) Check 1519 (iv): the consumer reads the thermal mean only; (v): Theorem U is an exact one-box identity
  for the ratio and has no box-uniform bound.

Notation. B = L^3, |B| = L^3. S = S(t) = sum over i >= 1 of rho_i^t, G = log(1 + S). Ebar_t := (sum of E_i rho_i^t)/S,
the mean energy of the excited thermal weight. m = E_1. eps_0 := 5.05 x 10^(-4) (the entrance value of TR2).
"Cold" means G < 10^(-3).

## 2. The thermal inequality in exact one-box variables (written 2026-11-25T06:20Z)

### 2.1 Proposition INT (the target has no volume factor; PROVED GIVEN (F1); elementary)

Let t >= 3 be an integer, s outside N_B, u_t := (-dG/dt)/|B| (the thermal energy per site of the spatial cube).
The Gibbs measure of the torus t x L^3 is invariant under translations and under the permutations of the three
axes of length L. So all 3 t |B| time-like plaquettes have one mean action a^tau_t and all 3 t |B| space-like
plaquettes have one mean action a^sigma_t, and abar_t = (a^tau_t + a^sigma_t)/2. Put delta_t := abar_inf - abar_t.
Then by (F1) the inequality of (R11') at (t, L, s) is

    (INT)   6 delta_t <= C log L * u_t.

Both sides are per site. The left side is the shift of the mean action of one plaquette between the torus of
time t and the torus of infinite time. By (F2), 6 |B| delta_t (1 + S) = sum over i >= 1 of rho_i^t (DD_i - DD_0),
and |B| u_t (1 + S) = sum over i >= 1 of rho_i^t E_i.

Reading. The volume factor of Theorem B1 is not in the target. It is in the proof: the only bound on file for
the shift is delta_t <= 2 S/(1+S) per plaquette (each level alone, Corollary U'), and (INT) needs
delta_t <= (C log L/6) Ebar_t S/((1+S) |B|). The loss is the factor |B|/(Ebar_t log L). Row 905 L150 states the
same loss in words ("bounding the two expectations separately leaves a factor |B|"). (INT) is not new; it is
(F1) divided by t |B|.

### 2.2 Proposition CB1 (Theorem B1 in thermal form on a cold cube; PROVED GIVEN (F2), (F3))

Let B be a box with sides at least 3, t >= 4 an integer, 0 < s < 4, S = S(t; B; s) > 0. Then

    dG/ds <= K_th * (-t dG/dt),   K_th := 1/(s log(4/s)) + c_s |B| / Ebar_t.

If S < 1, then Ebar_t >= m >= log(1/S)/t, so K_th <= 1/(s log(4/s)) + c_s t |B|/log(1/S).
On a cold cube (G < 10^(-3), so S < 0.0010006 and log(1/S) > 6.9), with t <= L/2 and s <= 2 (c_s < 26.4):

    K_th <= 1/(s log(4/s)) + 3.83 t L^3 <= 1/(s log(4/s)) + 1.92 L^4.

Proof. Take an orthonormal eigenbasis of T(s) on H_inv. Apply (F3) to each excited eigenvector with lambda_i > 0,
multiply by rho_i^t >= 0 and sum: sum of s (DD_i - DD_0) rho_i^t <= (sum of E_i rho_i^t)/log(4/s) + s c_s |B| S.
(The sums converge: rho_i^t E_i <= rho_i^(t-1) sup over x of x exp(-x), and t - 1 >= 3.) Multiply by t/(s (1+S))
and use (F2): dG/ds <= (-t dG/dt)/(s log(4/s)) + c_s |B| t S/(1+S). The last term is c_s |B| (-t dG/dt)/Ebar_t,
because -t dG/dt = t Ebar_t S/(1+S). Ebar_t is a mean of numbers E_i >= m. S >= rho_1^t = exp(-t m), so
t m >= log(1/S). Arithmetic: 26.4/6.9 < 3.83. QED

**What the thermal weighting changes in the volume factor of Theorem B1, exactly.**
- Theorem B1: K_B = 1/(s log(4/s)) + c_s |B|/m(B; s). The gap m is an unknown of the box.
- Thermal form: m is replaced by Ebar_t, the mean energy of the thermal weight at the time t. Nothing else
  changes. The factor |B| stays.
- On a cold cube the unknown goes away: coldness itself gives m >= log(1/S)/t. So the rate is bounded by
  explicit numbers, c_s t |B|/log(1/S), with no gap hypothesis. So (R11') holds at integer times at every
  coupling below 4 with this rate and no input. It is far from the target: t L^3 against C log L.
- Not covered: real t. (F2) is for integer t. Theorem B1 gets real t from the level form; the thermal form at
  real t needs the s-derivative of Tr T^t at real t, which row 710 did not write and I did not write.

Repo search for CB1: "log(1/S)" hits 12 lane files and one FINISH row; I opened none of them beyond the grep
line, so I do not call CB1 new. It is Corollary U' summed with thermal weights, and the step m >= log(1/S)/t.

## 3. Two consumer-side sharpenings that follow from the proof of Remark COLD (written 2026-11-25T06:20Z)

Both are small. I record them because they change what a producer has to bound.

### 3.1 Remark BAND (PROVED GIVEN Theorem TR's proof and Lemma 4.1 of row 708)

In Theorem TR with Remark CH, let phi(s) := G(t_0 E(s); B; s) and phi(sigma) <= eps_0 < 10^(-3). Assume the
inequality (VIR_K) on the characteristic curve only at the points where eps_0 <= phi(s) < 10^(-3). Then
phi <= eps_0 on the whole interval.

Proof. phi is continuous (Lemma 4.1). Suppose phi(s_2) > eps_0. Put s* := sup of the s in [sigma, s_2] with
phi(s) <= eps_0. Then phi(s*) = eps_0 and phi > eps_0 on (s*, s_2]. By continuity there is s_3 in (s*, s_2] with
phi < 10^(-3) on [s*, s_3]. On [s*, s_3) the curve is in the band, so the hypothesis holds there, and the
computation in the proof of Theorem TR gives an upper right derivative of phi at most 0 at each of these points.
By the argument of that proof (row 708 L131) phi is non-increasing on [s*, s_3]. So phi(s_3) <= eps_0, a
contradiction. QED

So Proposition TR2 needs (R11') only on **lukewarm** cubes: eps_0 <= G(t; L^3; s) < 10^(-3), eps_0 = 5.05 x 10^(-4).
The proof of Remark COLD in row 1517 L194-197 already works at such points only; check 1519 (ii) states the
hypothesis on all of G < 10^(-3). grep "lukewarm": no hit in the lane files or FINISH. I do not call it new; it
is Remark COLD read with its proof.

### 3.2 Corollary ABS (on the band the relative inequality follows from an absolute one; PROVED)

Let eps_0 <= G(t; L^3; s) < 10^(-3) and t >= 4. Then -t dG/dt >= 3.4 x 10^(-3). So on the band the inequality of
(R11') with the constant C follows from

    (ABS)   D_s G(t; L^3; s) <= 3.4 x 10^(-3) * C log L.

Proof. -t dG/dt = t Ebar_t S/(1+S) >= t m S/(1+S) >= log(1/S) S/(1+S). S/(1+S) = 1 - exp(-G) >= G - G^2/2 >=
5.04 x 10^(-4). S < 0.0010006, so log(1/S) > 6.9. The product exceeds 3.47 x 10^(-3). QED

Reading.
- (ABS) is a bound on the slope of s -> G(t; L^3; s) while G crosses the band: the crossing of
  [eps_0, 10^(-3)] takes a coupling interval of length at least about 0.15/(C log L).
- At integer t and outside N_B, (ABS) is: 6 t L^3 (abar_inf - abar_t) <= 3.4 x 10^(-3) C log L.
- (ABS) implies the band form of (R11'). The converse needs t Ebar_t <= const * log L, which is not known.
- The factor log L is not slack here. GUIDE (no proof): if G is about L^3 times a pressure of order
  exp(-t m), the band puts t m near 3 log L, so -t dG/dt is itself about 3 x 10^(-3) log L.
- What it does not change: G near 10^(-3) is still a sum of about L^3 local terms, each exponentially small in
  t m. A bound on its slope to a factor log L is the same relative statement per unit volume. Row 708 4.5
  stands. With Proposition CB1 the proved bound on the band is D_s G <= K_th (-t dG/dt), and the gap to (ABS)
  is the factor t L^3/log L.

## 4. Attacks on the factor t L^3 / log L, and where each stopped (written 2026-11-25T06:21Z)

No attack removed the factor. Four were carried to a statement. None is a proof of (R11') or of (ABS).

### 4.1 Convexity with positivity: Lemma SQ (PROVED; gives a square root, not a logarithm)

Let t >= 3 be an integer, s outside N_B, 0 < h < s, and M >= the supremum over [s - h, s] of the variance of the
total action of the torus t x B (this variance is d^2 F/ds^2, F = log Z). Then dG/ds (s) <= G(s)/h + h M/2.
With h = (2G/M)^(1/2), if that is below s: dG/ds <= (2 M G)^(1/2).

Proof. G = F - t e >= 0 (Lemma A). e is convex and differentiable at s, so e(s - h) >= e(s) - h e'(s). Taylor:
F(s - h) <= F(s) - h F'(s) + h^2 M/2. Subtract: 0 <= G(s - h) <= G(s) - h G'(s) + h^2 M/2. QED

Use. Row 708 Way 3 says convexity gives nothing on the derivative of the difference. With G >= 0 it gives this
much. With the trivial M = (6 t |B|)^2 the result is weaker than Proposition CB1. If the action had a bounded
susceptibility chi (M <= 6 chi t |B|; not proved at any coupling of order one), then on the band
dG/ds <= (0.012 chi t |B|)^(1/2). That is the square root of the volume factor, against C log L in (ABS). The
route stops there: the method cannot see the cancellation in G'' = (variance at time t) - t e'', and that
difference is the second-order form of the same shift.

### 4.2 Proposition HI (only a window of levels needs more than Corollary U'; PROVED GIVEN (F2), (F3))

Let t >= 4 be an integer, 0 < s <= 2, Lambda > 0, pi_t(Lambda) := (sum over E_i >= Lambda of rho_i^t)/S. Assume
every eigenvector with 0 < E_i < Lambda has DD_i - DD_0 <= K_1 E_i. Then

    dG/ds <= [max(K_1, 1/(s log(4/s))) + c_s |B| pi_t(Lambda)/Ebar_t] * (-t dG/dt).

If t is even and S(t/2) <= 1, then pi_t(Lambda) <= exp(-(Lambda - 2m) t/2). So with
Lambda = 2m + (2/t) log(c_s t |B|/log(1/S)) the last term is at most 1; on a cold cube with t <= L/2 this
Lambda is at most 2m + 2 log L + 0.33.

Proof. Levels below Lambda: the assumption. Levels above: (F3). Sum with the weights rho_i^t as in CB1.
pi_t(Lambda) S(t) <= exp(-Lambda t/2) S(t/2) <= exp(-Lambda t/2), and S(t) >= exp(-t m). Then
c_s |B| pi/Ebar_t <= c_s |B| t exp(-(Lambda - 2m) t/2)/log(1/S) = 1. For t >= 4: (2/t) log(3.83 t L^3) <=
(1/2) log(1.92 L^4). QED

Use and limit. This is Proposition SUF of row 710 at any coupling: the extensive error is harmless above
2m + 2 log L. It stops at two points. (1) The consumer gives coldness at t, not S(t/2) <= 1; G at half the
time is on another characteristic curve, and its control needs the same inequality there. (2) Inside the
window it asks for a level bound, which is stronger than the thermal one (check 1519 (iv)). So it is a
localisation in energy of the open statement, not a step of its proof.

### 4.3 The polymer expansion on the band (GUIDE arithmetic with the constants of row 710 Section 6)

On the band at small s, 3 L^3 (s/4)^(4t) is about 10^(-3), so 4t is about (3 log L + 8)/log(4/s). The Cauchy
remainder of row 710 Section 6 has the base 12800 s against s/4. Its ratio to the leading term is about
t^2 51200^(4t) = t^2 L^(32.5/log(4/s)) exp(87/log(4/s)). So on the band the base mismatch costs a power of L with
the exponent 32.5/log(4/s): 2.8 at s = 1/25600, 0.16 at s = exp(-200). The band turns the exponential loss in
t of row 710 into a power of L, because the band fixes t at about log L. It is still not a logarithm. In
Proposition TR2 a rate L^gamma gives steps that sum to a finite reach (row 1517 L205-206).

### 4.4 The ground-state (Markov) form and a Cauchy-Schwarz step (derived; returns to route B1; not a lemma)

With P := psi_0^(-1) (T/lambda_0) psi_0, nu := psi_0^2 and h(x, y) := d/ds log of the kernel of P, the mean of h
given x is 0, and the thermal numerator is t times the mean over a stationary pair of
h(x_0, x_1) k_n(z, x_0) (k_m(z, x_1) - k_(m+1)(z, x_0)), n + m = t - 1, with k_n the excited part of the kernel of
P^n. Cauchy-Schwarz then bounds it by t (vbar S(2n))^(1/2) (sum of rho_i^(2m) (1 - rho_i^2))^(1/2), where vbar is
the conditional variance of h given x, averaged in the excited thermal weight. With vbar of order |B| this is a
rate of order (|B|/m)^(1/2). But h contains phi(y) - phi(x) with phi = d/ds log psi_0, the Poisson corrector of
the slab action. A bound on vbar is a bound on that corrector. This is the vector-field row of table 2.2 of row
1517 (route B1 of row 669) in an averaged form. I did not write it as a lemma and I did not compare it line by
line with (T-avg). It is the fifth record of that return.

## 5. Why the factor cannot go without reading the weight; compact U(1) (written 2026-11-25T06:21Z)

### 5.1 Everything up to Proposition CB1 holds for Wilson compact U(1) (PROVED GIVEN the U(1) transfer facts of check 1519 (iii) and (RK); a transcription)

Changed lines only. Link weight c_s(theta) = exp(-s (1 - cos theta)), Fourier coefficients c_n = exp(-s) J_|n|(s)
with J_n as in Lemma J of row 710 (its part (a)). eta_n := -log c_n = s - log J_|n|. By Lemma J (b), (c):
-s eta_n' = |n| - s (1 - r_|n|), 0 < r_n <= s/(2(n+1)) <= 1 for s <= 2. J_n <= ((s/2)^n/n!) sum over k of
(s/2)^(2k)/(k!)^2 <= (s/2)^n exp(s), so c_n <= (s/2)^|n| and eta_n >= |n| log(2/s); eta_0 >= 0. Lemma C is the
Fourier series on the torus of the links. V_1 = sum over spatial plaquettes of (1 - cos theta_p) lies in
[0, 6 |B|]. lambda_0 >= <1, T 1> >= exp(-6 s |B|) c_0^(3|B|) >= exp(-9 s |B|), because c_0 >= exp(-s). With
N(n) := sum of |n_l| and log(2/s) in place of log(4/s), the proofs of Theorem U, Corollary U' and Proposition
CB1 go through word for word for 0 < s < 2:

    dG/ds <= [1/(s log(2/s)) + (9 + 12/log(2/s)) |B|/Ebar_t] * (-t dG/dt).

Propositions INT and HI, Remark BAND and Corollary ABS do not read the group at all.
So no step up to CB1 can be the step that fails for U(1). A correct method for SU(2) must fail for U(1) at the
one step after CB1: the replacement of c_s t |B|/log(1/S) by C log L.

### 5.2 In the class the form t |B|/log(1/S) is attained at a first-order point (GUIDE; two-family picture; nothing proved)

Row 934 (`gap-vacsub-max.md` L225-230) has the level form: near a first-order point of the box the level above
the vacuum is the other phase, with E = l |B| (s_c - s)-type energy and a slope equal to the latent action of the
whole box, so -E'/E = 1/(s_c - s). The thermal form on a cold cube adds one line. Let the second family have
the weight g exp(-t |B| Delta(s)) in S, with Delta' = -6 l (l > 0 the jump of the mean plaquette action).
Coldness is t |B| Delta >= log(g/S). Where this family carries the thermal weight,

    (dG/ds)/(-t dG/dt) = 6 l |B|/(|B| Delta) = 6 l t |B|/log(g/S).

Compare CB1: c_s t |B|/log(1/S). Same form, and 6 l <= 12 < c_s. So in a member with a first-order point the
cold thermal rate is of the order t |B|, at the couplings where G crosses the band. Members: the mixed SU(2)
weight K7 on its first-order line (RECALLED numerics of Bhanot and Creutz, as in row 708 L48; no theorem). A
rigorous member may be the Potts model with many states (RECALLED: Kotecky and Shlosman; Borgs and Kotecky
for the periodic box; not read, and I did not check that it is in the class of row 705).

Consequence (argued). The step after CB1 cannot be proved from: the group, reflection positivity, positive
link coefficients, the transfer structure of Section 2 of row 710, or anything K7 shares with the Wilson
weight. This is test K7 of row 708 applied to the thermal form. It adds no new exclusion; it shows that the
thermal weighting and the cold condition do not weaken the test.

### 5.3 Compact U(1): the step and the family (GUIDE apart from 5.1)

- The step: 5.1. The proof must break where the shift 6 t |B| delta_t is bounded by C log L times the thermal
  energy, that is, where a thermal excitation is shown to displace an amount of action at most C log L times
  its energy.
- Standing of the hypothesis. Corollary FLOOR for Wilson U(1) is conditional on "no seed at one weak coupling
  for the periodic cosine model", which check 1519 (iii) found unproved on file (rows 784, 786). I add no proof.
- The family, if the transition of the Wilson cosine model is first order (RECALLED numerics; from memory:
  Jersak, Neuhaus and Zerwas; Arnold and others; not fetched): couplings just below the coexistence coupling of
  the torus t x L^3. The second family is the Coulomb phase with its photon gas. With a free photon pressure
  (pi^2/45)/t^4 per site (GUIDE; lattice and coupling corrections ignored), its weight is
  exp(-|B| (t Delta - 0.219/t^3)), its mean energy is |B| (Delta + 0.66/t^4), and coldness needs
  Delta >= 0.219/t^4. So the ratio is at most 6 l t^4/0.88 = 6.8 l t^4, reached at the cold edge. It does not grow
  with L at fixed t. It exceeds C log L on the cold cubes with t above (C log L/(6.8 l))^(1/4). So the violating
  family of Corollary FLOOR would be: L large, (C log L/(6.8 l))^(1/4) < t <= L/2, s at the edge of coldness below
  the coexistence coupling of that torus. This is a guess at the family, not a derivation.
- If the transition were continuous, the family would be the one of the Ising member (row 708 L174).

## 6. Outcome, the exact statement left, the next two rows (written 2026-11-25T06:23Z)

### 6.1 Outcome

None of the three decisive outcomes of the row was reached.
- PROVED: no. The thermal inequality with K <= C log L is not proved at any coupling for large cubes, small
  couplings included (row 710 covers s L^3 <= 1/10 only; Proposition CB1 has the rate t L^3).
- Obstruction: no. I found no cold cube and no level for Wilson SU(2) on which the ratio must exceed C log L.
  The only families with a large ratio are in other members of the class (5.2, 5.3), and they are GUIDE.
- First lemma not equivalent to a closed line: no. The exact statement left is

      (ABS-band)  there are C_1 and L_0 such that for every even L >= L_0, every s in [1/25600, beta_1) and every
                  real t in [4, L/2] with eps_0 <= G(t; L^3; s) < 10^(-3):  D_s G(t; L^3; s) <= C_1 log L.

  By 3.1, 3.2 and Proposition TR2 it gives the seed at every coupling up to beta_1. So it is at least as strong
  as (NOCRIT) on the interval, as row 1517 6.1 found for (R11'). It is a restatement of the trigger in its
  weakest form found, not a lemma below the target. Its buildable components are the ones built here: CB1
  (the rate with t L^3, no hypothesis) and HI (the window). Neither reads the Wilson weight.

What was proved (one author, checked by no one): Propositions INT, CB1, HI, Lemma SQ, Remark BAND, Corollary
ABS, and the transcription 5.1 for U(1).

The two questions of the row.
- Volume factor: Section 2.2. Thermal weighting replaces 1/m by 1/Ebar_t; coldness bounds that by t/log(1/S);
  the factor |B| is untouched. In the class this is the right order at a first-order point (5.2, GUIDE).
- Compact U(1): Section 5. No step through CB1 fails. The failing step is the bound of the action shift by
  C log L times the thermal energy. The family is conditional and guessed (5.3).

### 6.2 For the registry line of R11 (for the lead; I edited no registry)

If the check below confirms: (a) add "needed only on lukewarm cubes, eps_0 <= G < 10^(-3); there it follows
from the absolute bound D_s G <= C_1 log L"; (b) add "proved with no hypothesis at integer times: rate
1/(s log(4/s)) + c_s t L^3/log(1/S) (row 1522 CB1); the open factor is t L^3/log L"; (c) keep "trigger, not a row".

### 6.3 The next two rows and their decisive outcomes

**Row 1, `gap-r11-thermal-solve-fable-check-astra62` (cross-provider check of this file).** Order: (i) CB1: the
sum of Corollary U' with thermal weights, convergence, the step m >= log(1/S)/t, the constants; (ii) BAND:
the first-exit argument at points of the band only; (iii) ABS: the lower bound 3.4 x 10^(-3); (iv) Lemma SQ and
Proposition HI; (v) 5.1: each changed line of the U(1) transcription, and the U(1) transfer facts it reads;
(vi) 5.2: is there a member of the class of row 705 with a proved first-order point (Potts with many states,
Borgs and Kotecky for the periodic box), and does the two-family formula hold there as a theorem.
Decisive outcome: each of (i) to (v) HOLDS or FAILS at a named line; the registry wording of 6.2 is adopted
or not. If (vi) finds a rigorous member, the sentence "the cold thermal rate t |B|/log(1/S) is sharp in the
class" moves from GUIDE to a cited theorem; if not, it stays GUIDE.

**Row 2, `gap-r11-abs-sc` (a proof row at strong coupling; rank low; the lead may skip it).** Prove
(ABS-band) for s in [1/25600, 1/12800] and every large even L. There the expansions converge, and the band
puts t near (3 log L)/(4 log(4/s)). It is the thermal band form of (BAND-sc) of row 710, which is OPEN. The
method must give the base s/4 exactly (4.3: the polymer remainder loses a power L^(32.5/log(4/s))). The known
route is the expansion of the one-plaquette band on the periodic cube (RECALLED names: Schor; O'Carroll, Braga
and Schor; row 711 owns the pages). Decisive outcome: PROVED, with the statement of what the proof reads of
the weight; or the first term that breaks. What it moves: nothing on the gap by itself (the seed is known
there by Theorem DOB). It is the only range where a producer for R11 can be built and tested today. By K7 a
proof there that does not read the log-linear Wilson weight cannot be the tool. That is why I rank it low.

I propose no attack row at a coupling of order one. This row found no entry point there that is not CB1 (the
extensive bound), route B1 (4.4) or the block step of row 708 4.5.

## 7. Searches, labels, credits, what was not done (written 2026-11-25T06:23Z)

### 7.1 Searches

- `library/open-core.md`: no entry for VIR, thermal, R11, BAND-sc (grep, 564 lines).
- FINISH rows and lane files (`library/gap-*.md`, `library/prior/gap-*.md`), counts of files: "lukewarm" 0;
  "intensive" 1; "log(1/S)" 12; "latent" 12 (opened: row 934 L222-234, the two-level picture, credited in
  5.2); "Potts" 27; "Borgs" 52; "interaction measure" 18. I opened only the hits named in Section 1. So no
  statement here is called new. BAND and ABS are not on file under the words searched.
- (BAND-sc) appears in FINISH rows 710, 1517 and 1522 only. No row attacks it.
- Cross-branch and Sussman-Alpoge: not searched in this row. Check 1519 searched main and four PR branches
  for the R11 terms the same day and found the three lane files this row builds on. The Sussman-Alpoge
  account has no statement on a coupling derivative of transfer levels (rows 708, 710, 1517; outline
  4638-4641 as quoted in check 1519). Their GL3 (positive link coefficients) enters through Lemma J of row 710.

### 7.2 Labels

- **Proved here**, not checked: INT, CB1, HI, SQ, BAND, ABS (given the facts (F1) to (F4) as read); 5.1 (given
  the U(1) transfer facts of check 1519 (iii) and (RK), neither rebuilt here).
- **Derived, not written as a lemma**: 4.4.
- **GUIDE or argued**: 4.3; all of 5.2 and 5.3; the reading lines of 3.2; "consequence" in 5.2.
- **Recalled, not read**: Bhanot and Creutz; Kotecky and Shlosman; Borgs and Kotecky; Jersak, Neuhaus and
  Zerwas; the photon pressure; Schor; O'Carroll, Braga and Schor.
- **Guessed**: that (R11') and (ABS-band) are true for Wilson SU(2).

### 7.3 Not done

- No proof of the thermal inequality, at any coupling, beyond the rate t L^3.
- Real times: CB1, HI and SQ are for integer t. The consumer reads real t in [4, L/2].
- No numeric run and no Lean. Nothing here needed one. memory_pressure read 37 percent free at the end of the
  run, below the 50 percent rule; no job was started.
- The attempt with the generator class of check 1519 (iv) (GL12 block generators) was not made. In thermal form
  a commutator has zero trace against any power of the transfer operator (check 1519 (iv)), so a generator
  cannot change the thermal numerator; it can only change which operator inequality is used to bound it.
- I did not compare 4.4 with (T-avg) of row 669 line by line.
- I did not check that the Potts model is in the class of row 705.
- Nothing was committed or pushed. The only file written is this one.

### 7.4 Credit

Row 708 (Claude Fable 5.2 max): Theorem TR, Remark CH, Lemma 4.1, Lemma 4.2, K7, the three ways. Row 710
(Claude Fable 5.2 medium; check row 715, Claude Opus 5.5): Lemma J, Theorem U, Corollary U', Theorem B1,
Proposition SUF, (BAND-sc). Row 1517 (Claude Fable 5.2 high): TR2, COLD, FLOOR, (R11'). Check 1519 (OpenAI
Codex, gpt-6.2-astra): the thermal reading, the corrected FLOOR, the U(1) transfer facts. Row 905
(gpt-6-astra): formula (R). Row 934 (Claude Fable 5.2 max): the two-level picture. Sussman and Alpoge, with
Claude and Codex: GL3, through row 710. Bhanot and Creutz; Kotecky, Shlosman, Borgs; Jersak, Neuhaus, Zerwas;
Schor; O'Carroll and Braga (all recalled). Balaban: not used in this row.

## 8. Result

RESULT: Row 1522 (Claude Fable 5.2 medium, Mac mini worker 1; author only, checked by no one; no numeric run, no Lean, nothing committed). None of the three decisive outcomes: the thermal inequality with K at most C log L on cold cubes is NOT proved for Wilson SU(2) at any coupling, no obstruction was found, and no first lemma below the target was found. Proved by hand: Proposition CB1 (at integer t >= 4 and every s < 4 the thermal rate is at most 1/(s log(4/s)) + c_s |B|/Ebar_t, and on a cold cube at most 1/(s log(4/s)) + c_s t L^3/log(1/S), with no gap hypothesis: thermal weighting replaces the gap m of Theorem B1 by the thermal mean energy, coldness bounds it by log(1/S)/t, and the factor |B| stays); Proposition INT (the target itself is per site: 6 (abar_inf - abar_t) <= C log L times the thermal energy per site); Remark BAND and Corollary ABS (the consumer TR2 needs the inequality only on lukewarm cubes, 5.05e-4 <= G < 1e-3, and there it follows from the absolute bound D_s G <= 3.4e-3 C log L); Lemma SQ (convexity with G >= 0 gives a square-root bound, useless without a susceptibility bound); Proposition HI (above 2m + 2 log L the extensive error is harmless if S(t/2) <= 1); and the transcription of Theorem U through CB1 to Wilson compact U(1) for s < 2. So for compact U(1) no step through CB1 fails, and a correct method must fail at the one step after it, the bound of the action shift 6 t L^3 (abar_inf - abar_t) by C log L times the thermal energy; the violating family is guessed, not derived (cold edge below a first-order coexistence coupling, where a two-family picture gives the rate 6 l t |B|/log(g/S), the same form as CB1). Open: (ABS-band), which with TR2 gives the seed up to beta_1 and so is at least as strong as (NOCRIT); the open factor is t L^3/log L; real times in CB1. Next: a cross-provider check of this file; then, ranked low, (ABS-band) at strong coupling s in [1/25600, 1/12800], the thermal band form of (BAND-sc).
