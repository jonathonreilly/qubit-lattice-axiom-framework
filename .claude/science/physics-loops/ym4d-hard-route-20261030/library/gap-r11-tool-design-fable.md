lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T17:03Z

# Row 1517, gap-r11-tool-design-fable: the missing tool for trigger (R11)

Worker: Claude Fable 5.2, high effort, Mac mini worker 1. Pinned commit 3cd437195 on `claude/ym4d-hard-route`.
Not checked by another model. Research-stage working state; nothing here is a public claim.

## Status log (times from `date -u`)

- 2026-11-25T05:03Z: file created. Plan below. Nothing proved yet.
- 2026-11-25T05:04Z: read the row, FINISH rule sections, GOAL.md, row 708 Sections 1-5 (`gap-mid-max.md` L21-216), row 710 Sections 2-4, 6-9 (`gap-vir-sc.md`), row 1515 in full (`gap-seed-direction-fable.md`), registry lines R10-R12, W-CUBE-23. Section 1 written.
- 2026-11-25T05:21Z: Section 2 written. First candidate (a conjugated operator inequality with the vacuum transport as generator) derived blind, then found on file: route B1 of row 669, row 913 3d, row 1356 Ways 1 and 3. Not presented as new. Memory 37 percent free: no numeric job in this row.
- 2026-11-25T05:25Z: Sections 3 and 4 written (the trace-anomaly clause needs a volume term; Proposition TR2: restarted transport, any constant C in K <= C log L, cold boxes only; Corollary FLOOR).
- 2026-11-25T05:28Z: re-read of the proved items done (Lemma CONJ, Proposition VOL, Proposition TR2 against Theorem SH, the table line r = 4 and Lemma E2 remark (i), Remark COLD, Corollary FLOOR): one wording fix (real part in CONJ (b)), one anchor added. Cross-branch search done. Sections 5-8 written. Finished.

## 0. Plan

1. Read the row, the rules, row 708 Section 4 (`library/gap-mid-max.md`), row 710 (`library/gap-vir-sc.md`),
   rows 1510, 1511, 1515 and check 1514 (statements only), and the registry entry (R11).
2. State the exact output of the tool and its consumer (Theorem TR, Corollary TR1 of row 708).
3. Design: one candidate tool; show it is not one of row 708's three failed ways, not (BAND-sc), not another
   closed registry line; show where it fails for the Ising member and for compact U(1).
4. Build the first component: full proof, or a finite statement for an exact Lean-checked computation.
   Or: an obstruction theorem over a stated family of tools.
5. Next two rows with decisive outcomes. RESULT line.

## 1. What the tool must output, and what is on file (read; nothing new here)

Labels used in this file: **proved** (a written proof is in this file), **read** (read in a row, not re-derived),
**argued**, **guessed**, **guide** (heuristic size, never a proof step).

### 1.1 The output and the consumer (read: row 708, `gap-mid-max.md` L50-59, L118-158, L172)

- Box B = b^3 (spatial, periodic), T_B(s) the Wilson transfer operator at coupling s, levels
  E_i(s) = log(lambda_0/lambda_i), G(t; B; s) = log(1 + sum_i e^(-t E_i)).
- **(VIR_K)**: D_s G(t; B; s) <= -K(s) t (dG/dt)(t; B; s) (upper right derivative on the left).
  In row 1515's notation: R_v(t) <= -K v (d/dv) log(1 + s(v; t)).
- **Consumer.** Theorem TR (L120-132): (VIR_K) on [beta_0, beta_1] at the times t_0 E(s), E = exp(int K), gives
  G(t_0 E(s); B; s) <= G(t_0; B; beta_0). Remark CH (L134): only the characteristic curve is used.
  Corollary TR1 (L150-156): beta_0 <= 1/25600, b >= 256 even, int K <= log(b/(2 ceil(log_2 b))) gives the
  seed at beta_1 and m(L^3) >= 0.12/b for L >= 32 b. Remark LEV (L136-140): the level form (LEV_K),
  -dE_i/ds <= K E_i for every ordered level, implies it.
- **(VIR-log)** (L172) is the exact open statement. Trigger (R11) (registry L1018) asks for it at one coupling of
  order one, K growing more slowly than log n, by a method that fails for Ising across its transition and for
  compact U(1); "or a lattice identity playing the part of the trace anomaly with relative error of order one".

### 1.2 What is closed (read)

- Row 708 4.4, three ways: Way 1 pointwise operator inequality (K = 1/s; false by the published scaling values,
  K about 3.3 against 1/s about 0.4); Way 2 locality (K <= 12 |B|/m; proved as Theorem B1 of row 710; the
  gap-dependent stability form ends at a finite coupling); Way 3 convexity (the Ising member has every class
  property and fails).
- Row 710: Theorem U (L67-77): for every level of every box and 0 < s < 4, with the electric number N,
  s d log lambda/ds = <N>_w - s <R>_w - s <V_1>_psi <= (-log lambda)/log(4/s). The vacuum subtraction is the
  obstruction (L80, L112, L156). (BAND-sc) (L177-182) is the open statement at strong coupling. Its Section 8
  item 4 (L200) names the anisotropy response (Karsch coefficients) as the candidate second identity and
  judges it "a statement of the same kind as (VIR_K) for the two-coupling family".
- Row 708 4.5 (L184): "It needs an identity that produces the ratio ... The lattice has no dilation. Its
  substitute is ... one block step of a renormalization map at a coupling of order one, with ... relative
  errors of order one."
- Row 1515: Lemma B, WIN, (UV-TS), (VIR-top); verdict that the forced form is relative.

## 2. The single-box frame: every tool is a conjugation (written 2026-11-25T05:21Z)

### 2.1 Lemma CONJ (proved; first-order perturbation theory, not new)

Setting. T(s) is the transfer operator of the box B on the gauge-invariant space, self-adjoint, 0 <= T, with
simple top eigenvalue lambda_0(s) and analytic eigen-branches (input (RK) of row 710, `gap-vir-sc.md` L61-63).
Put That = T/lambda_0, so 0 <= That <= 1, and Phi(r) = r log(1/r) on [0, 1]. For a bounded operator A put

    D_A := That' - [A, That],   That' = T'/lambda_0 - (lambda_0'/lambda_0) That.

(a) For every analytic branch (r, psi) of That, |psi| = 1, and every bounded A: r' = <psi, D_A psi>.
(b) If for one A the form inequality Re <phi, D_A phi> <= K <phi, Phi(That) phi> holds for all phi, then every
    branch has r' <= K r log(1/r), that is -E' <= K E for E = -log r. This is (LEV_K) at s.
(c) Let psi_0, ..., psi_n be eigenvectors at s with distinct eigenvalues r_0 > ... > r_n. Put
    A_n := sum over i != j <= n of |psi_i> <psi_i, That' psi_j> <psi_j| / (r_j - r_i). Then A_n is bounded and
    skew-adjoint, and <psi_i, D_(A_n) psi_j> = delta_ij r_i' for i, j <= n. So on the span of these levels the
    form inequality of (b) is equivalent to (LEV_K) for them.

Proof. (a) r' = <psi, That' psi> (row 710, consequence (1) of (RK), L63). <psi, [A, That] psi> =
<psi, A That psi> - <That psi, A psi> = r <psi, A psi> - r <psi, A psi> = 0, because That is symmetric.
(b) Take phi = psi in (a); <psi, Phi(That) psi> = Phi(r). (c) <psi_i, [A_n, That] psi_j> = (r_j - r_i)
<psi_i, A_n psi_j> = <psi_i, That' psi_j> for i != j, and 0 for i = j. (A_n)* has the entries
conj(<psi_j, That' psi_i>)/(r_i - r_j) = -<psi_i, That' psi_j>/(r_j - r_i), so A_n is skew-adjoint. QED

Reading. A "relative transport bound" for one box at one coupling is a choice of a generator A and a form bound
for D_A. With all A allowed the statement is (LEV_K) itself ((c); the generator is the adiabatic one). So a
tool is defined by a **restricted class of generators** in which the form bound can be proved without knowing
the eigenvectors. (For vector fields A is unbounded; (a) holds for smooth psi in its domain.)

### 2.2 The map of the classes, with the registry line of each (read; nothing new)

| Class of A | The form bound that is needed | On file | Standing |
|---|---|---|---|
| A = 0 | That' <= K Phi(That): electric and magnetic deficit each bounded | row 708 4.4 Way 1; row 710 Theorem U (exact for unsubtracted levels), Corollary U' (the vacuum term s abs(B)) | false with K = 1/s by the scaling values; the vacuum moves |
| A arbitrary, bound by norms and locality | abs(<psi, That' psi> - vacuum) <= 12 abs(B) | row 708 Way 2; row 710 Theorem B1 | K <= 12 abs(B)/m; with stability theorems K <= C m^(-p), ends at a finite coupling (row 677 Proposition B) |
| A = quasi-adiabatic generator | needs the gap as input | `gap-outside-box-max.md` L153 (I14) | "the gap is the hypothesis ... not its conclusion" |
| A = a vector field X + (1/2) div X that transports the vacuum measure | one-sided bound on the strain sym(grad X): for X = grad of the Poisson corrector, Hess phi >= -c | row 669 route B1, crux (T) (`gap-skeleton-max.md` L107-111, 1.D L220-255); row 913 3d (`gap-target-max.md` L149); row 1356 Proposition TR, (LIP), Setting H (`gap-mini-mneutral-fable.md` L172, L196); for the Wilson operator Way 3, Lemma JF, L418-466; (HS-sup) row 677 (`gap-zf-box-x.md` L183) is the first-order form | supremum form: not proved, "probably false" (row 669 L111), a large-field problem in the infrared; averaged form (T-avg) (L240): necessary and sufficient, "the conclusion in differential form" (L317) |
| A = all | (LEV_K) | 2.1 (c) | equivalent to the target |

I derived the vector-field row blind in this session (the level velocity equals twice the strain of the vacuum
transport field averaged in the kinetic measure of the level) and then found it at the anchors above. It is
the lane's B1. I do not present it as a step. This is the fourth record of that return (row 913 3d.2 counts
three).

## 3. The trace-anomaly clause of (R11): a single box cannot carry it (written 2026-11-25T05:25Z)

### 3.1 Proposition VOL (proved as a chain rule; the scaling hypothesis is a definition, not a lattice fact)

"Trace anomaly with relative error of order one" must mean a scaling law for the box levels. Write it exactly:

    (SCAL)  E_i(s; b) = a(s) eps_i(b a(s))   for the levels of the cube b^3, with a > 0 decreasing and C^1 in s,
            and eps_i C^1 in the physical side L = b a(s).

Under (SCAL), with kappa(s) := -a'(s)/a(s) > 0 and sigma_i := (d log eps_i / d log L)(b a(s)):

    (V1)  -(d/ds) log E_i(s; b) = kappa(s) (1 + sigma_i).
    (V2)  With G a function of (t a(s), b a(s)) and b read as a real variable:
          dG/ds = -kappa (t dG/dt + b dG/db).

Proof. log E_i = log a + log eps_i(b a); d/ds log eps_i(b a(s)) = sigma_i a'/a. (V2): G = sum-type function of
the products t E_i = (t a) eps_i(b a). QED

Reading (argued; the sizes are guide values).
- The ratio (action deficit)/(energy) of a level is kappa (1 + sigma_i). It is **not** the same for all levels
  of one box. Examples: a massive particle at rest in a large box, sigma about 0; one unit of momentum,
  sigma = -(2 pi/L)^2/eps^2 in (-1, 0); a pair of torelons in the neutral sector, sigma about 1; the levels of
  a small box, eps proportional to 1/L up to logarithms, sigma about -1 (the level in lattice units depends on
  b only, and its velocity vanishes to leading order).
- So no identity on one box with one coefficient can "produce the ratio". The exact scaling statement has
  three variables, (V2). On the lattice b is an integer, and the discrete form of (V2) compares the box b at s
  with the box b' at s': one block step. That is the statement of row 708 4.5 (L184), the Q2 chain and (CAS)
  (row 708 L64-67, 5.2). All are closed lines.
- For the consumer the volume term has a sign: (VIR_K) with K = kappa holds under (SCAL) if and only if
  dG/db >= 0 (V2), and (LEV_K) holds with K = kappa (1 + sup sigma_i). So a single-box tool must prove two
  things at once: a bound for kappa (the lattice beta function, read from the box, is bounded away from
  zero; row 708 L176), and a bound for the volume slopes. At a transition the first one fails: kappa is the
  logarithmic derivative of the correlation length.
- The published lattice sum rules (Michael; Rothe; Karsch's anisotropy coefficients) are the
  Hellmann-Feynman identity plus (SCAL); so I recall them, and row 711's digest read abstracts only
  (`prior/gap-vir-lit.md` L23-33). They assume the scaling law. They do not supply it.

Verdict on the clause "a lattice identity that plays the part of the trace anomaly": on one box it does not
exist in the form the trigger names; on two boxes it is a block step at order-one coupling, a closed line. This
is row 708 4.5 with the reason made explicit ((V1): the level-dependent slope). Not a new line.

## 4. The consumer accepts more than (VIR-log): restarted transport (written 2026-11-25T05:25Z)

### 4.1 Proposition TR2 (proved given the inputs listed; one author, unchecked)

Inputs, read as statements and not re-derived: Theorem TR (row 708, `gap-mid-max.md` L120-132); the start in
the proof of Corollary TR1 (L156: for beta_0 <= 1/25600, g(t_0; 256^3; beta_0) < 3.7 x 10^(-4), t_0 = 8); from
`gap-seed-shape.md` (row 705, checked by Claude Opus 5.5, row 707): the line "r = 2, two stages" (L138:
S(a; (2a)^3) <= 1/1650 gives S(a; (4a)^3) <= 0.0396), Theorem SH (i) for the pair (a, (4a)^3) with j = 2 and
K_SH = 22.2 (L89-99; table line r = 4, step (2, 2, 3), threshold 1/25, L123; the constants used in the proof of TR1), and Lemma E' in the form used in
the proof of SH (ii) (L108; Lemma E2 remark (i), L70): for an integer L >= 2^k 4a, g(2^k a; L^3) <= (L/(3 2^k a))^3 log(1 + s_k), with
s_k := S(2^k a; (2^k 4a)^3).

**Statement.** Let 0 < beta_0 <= 1/25600 < beta_1 and C >= 1. Assume

    (VIR-Clog)  there is L_0 such that for every even L >= L_0 there is a continuous K_L on [beta_0, beta_1]
                with 0 <= K_L <= C log L and (VIR_(K_L)) on the cube L^3 for every s in [beta_0, beta_1) and
                every real t in [4, L/2].

Then for every s in [beta_0, beta_1] there is an even L with S(L/2; L^3; s) < 5.1 x 10^(-4) < 1/1650. So the
conclusions of Corollary TR1 hold at every such s (seed, gap of all large cubes).

**Proof.** Put delta := 1/(2C) and eps_0 := 5.05 x 10^(-4).

Step. Let sigma in [beta_0, beta_1) and let a >= 4 be an integer with S(a; (2a)^3; sigma) < 5.1 x 10^(-4). Then
for every sigma' in [sigma, min(sigma + delta, beta_1)] there is an even L with S(L/2; L^3; sigma') < 5.1 x 10^(-4),
and L/2 >= 4.
- By the two-stage line, s_0 := S(a; (4a)^3; sigma) <= 0.0396, and theta := 22.2 x 0.0396 < 0.88. By SH (i),
  s_k <= theta^(2^k)/22.2 for every k >= 0.
- Put A := 2^k a and L := 4 A^2 (even, L >= 16 A > 2^k 4a). By Lemma E', at the integer time A >= 4:
  G(A; L^3; sigma) = g(A; L^3; sigma) <= (4A/3)^3 theta^(2^k)/22.2. The right side is (64/27) a^3 8^k theta^(2^k)/22.2,
  which tends to 0 as k grows. Fix k so large that it is at most eps_0 and L >= L_0.
- Theorem TR on the cube L^3, on [sigma, sigma'], with t_0 = A and K = K_L. Its factor is
  E(sigma'') <= exp(delta C log L) = L^(1/2) = 2A for sigma'' in [sigma, sigma']. So the times it reads lie in
  [A, 2A^2] = [A, L/2], inside [4, L/2]. It gives G(A E(sigma''); L^3; sigma'') <= eps_0.
- G is non-increasing in t and L/2 >= A E(sigma''). So G(L/2; L^3; sigma'') <= eps_0 and
  S(L/2; L^3; sigma'') <= e^(eps_0) - 1 < 5.1 x 10^(-4). L/2 = 2A^2 is an integer >= 4.

Start. At beta_0, G is non-increasing in t and 8 <= 128, so S(128; 256^3; beta_0) < e^(3.7 x 10^(-4)) - 1 <
5.1 x 10^(-4). This is the hypothesis of the Step with a = 128.

Induction. sigma_0 = beta_0, sigma_(j+1) = min(sigma_j + delta, beta_1). The Step at sigma_j, with a the half
side of the cube found for sigma_j, covers [sigma_j, sigma_(j+1)]. After at most 2C (beta_1 - beta_0) + 1 steps
the interval is covered. QED

**Remark COLD (proved).** The hypothesis is needed only on cold boxes: (VIR_(K_L)) at the pairs (t, s) with
G(t; L^3; s) < 10^(-3). Proof: in Theorem TR put phi(s) = G(t_0 E(s); s), continuous, phi(sigma) <= eps_0. If
phi exceeded eps_0 somewhere, let s* be the last point before it with phi <= eps_0 on [sigma, s*]; phi(s*) =
eps_0 < 10^(-3), so by continuity (VIR) holds along the curve on a right neighbourhood of s*, where the proof of
TR makes phi non-increasing; a contradiction. (Remark CH of row 708 already restricts to the curve.)

**What TR2 changes.** Row 708's (VIR-log) and trigger (R11) ask for an integral of K below
log(b/(2 ceil(log_2 b))) on the whole interval, "K growing more slowly than log n". TR2 accepts
**K <= C log L with any constant C**, on cold boxes only. The price is the size of the cube: the half side
goes from a to about 2 (2^k a)^2 at each of about 2C (beta_1 - beta_0) steps. I did not find the restart on file
(grep "restart", "interleav", "any constant", "sub-interval" in `gap-mid-max.md`, `gap-mid-check.md`,
`gap-vir-sc.md`, `gap-seed-direction-fable.md`: no hit; (DEF_K), L162, says "at most c log b" with no
statement on c). It is a consumer-side weakening. It does not make the tool: a growth of K like (log L)^p
with p > 1 is not covered (the steps delta_j then shrink too fast), and the failure modes of row 708 L174
(K like b at a critical point or with two phases) are far above both thresholds.

### 4.2 Corollary FLOOR (the step where any tool fails for the Ising member and for compact U(1))

Proved given TR2 and, for each named model, the two recalled facts in brackets.

Let a model of the class have the start of TR2 at one coupling s_0 and no seed at s_1 > s_0 (no even L with
S(L/2; L^3; s_1) < 5.1 x 10^(-4)). Then (VIR-Clog) fails on [s_0, s_1] for every C: for every C and every L_0
there are an even L >= L_0, a coupling s in [s_0, s_1) and a real time t in [4, L/2] with
G(t; L^3; s) < 10^(-3) and

    D_s G(t; L^3; s) > - C log L * t (dG/dt)(t; L^3; s).

(If not, the constant K_L = C log L would serve in TR2 with Remark COLD.) In words: somewhere on the way the
thermal sum of a cold cube rises faster than at the logarithmic rate C log L, for cubes of unbounded side.
- Ising member of row 708 4.4 (`gap-seed-shape.md` 4.1) [a seed at small J by the high-temperature
  expansion; none at large J, two phases; both recalled as in row 708]. The cold cube whose sum rises is the
  one in which the tunnel splitting appears (row 708 L174: K_b like b).
- Compact U(1) [strong-coupling seed; no gap at weak coupling: Guth; Frohlich and Spencer; recalled as in
  row 708 L58]. The constants of the start differ from 1/25600 and are not computed here.

So for every tool the failing step is its last inequality, read on one cold cube at one coupling inside the
crossing interval. In the frame of Section 2 that inequality is the form bound for D_A: for a vector-field
generator it is the strain bound, and the strain of every vacuum transport on some cold cube exceeds
(C/2) log L in the kinetic measure of the thermal state.

## 5. The design requirements of the row, one by one (written 2026-11-25T05:28Z)

1. **Exact output and consumer.** Output, in the weakest form the consumer accepts (Section 4):

       (R11')  There are C and L_0 such that for every even L >= L_0, every s in [1/25600, beta_1) and every
               real t in [4, L/2] with G(t; L^3; s) < 10^(-3):
               D_s G(t; L^3; s) <= - C log L * t (dG/dt)(t; L^3; s).

   At integer t and outside a countable set of couplings (row 708 Lemma 4.2) the left side is
   6 t L^3 (abar_(inf) - abar_t), the shift of the mean plaquette action between infinite and finite time, and
   the right side is C log L times t times the thermal mean of the energy. Consumer: Proposition TR2 with
   Remark COLD (this file), then Theorem TR, Corollary TR1 and Theorem SH (rows 708, 705). (R11') on
   [1/25600, beta_1] gives the seed at every coupling up to beta_1.
2. **Not one of the three failed ways, not (BAND-sc), not a closed line.** Not met. By Lemma CONJ a single-box
   method is a class of generators with a form bound. Every class I could state is on file (table 2.2): A = 0
   is Way 1; norm and locality bounds are Way 2; the vector fields are route B1 with (T) (supremum over
   fields: no proof, a large-field problem) and (T-avg) (the conclusion in differential form); the
   quasi-adiabatic generator needs the gap. Way 3 (convexity) has no generator and is refuted by the Ising
   member. (BAND-sc) is the form bound for A = 0 on the lowest band at small s. Two more methods that are not
   conjugations by construction, with their lines:
   - complex couplings: if the thermal sum S(t; L^3; .) is analytic with positive real part on a disc of
     radius rho about s, then abs(dS/ds) <= 2 S/rho (Harnack's inequality for a positive harmonic function),
     a relative bound with no gap in it. With TR2 the radius may shrink like 1/(t E_1 log L). This is Route Z
     in the dominance form (rows 670, 677, 680: `gap-skeleton-max-b.md` L302-330, `gap-skeleton-final.md`
     L356). The width that perturbation theory gives is m/abs(B), which is Way 2 again. (Argued; I did not
     write the Harnack step as a lemma, because its hypothesis has no source.)
   - two boxes: Section 3; a block step at order-one coupling.
3. **Where it fails for the Ising member and for compact U(1).** Corollary FLOOR: for each of them the output
   inequality itself fails on some cold cube inside the crossing interval, by more than any C log L. Inside a
   tool the failing line is the form bound for D_A. No generator class in table 2.2 has a form bound whose
   proof reads the group; that is why none of them is a tool.
4. **Build.** No first component of a tool was built. Built instead, on the consumer side: Proposition TR2 and
   Remark COLD (the output may lose a factor C log L, any C, and is needed on cold cubes only); and two
   statements that close parts of the trigger: Lemma CONJ with table 2.2, Proposition VOL.

## 6. Decisive outcome, triggers, next two rows (written 2026-11-25T05:28Z)

### 6.1 Outcome: of the third kind

**The first component that could not be built is the selective form bound**: a class of generators A for the
cube L^3 and a proof, which reads the Wilson weight and the group, of

    Re <phi, (That' - [A, That]) phi> <= C log L <phi, Phi(That) phi>

on a set of phi that contains the cold thermal states, in a norm that is neither a supremum over all fields
(closed: (T), (HS-sup), kind (W)) nor the eigenvectors themselves (equivalent: (T-avg), Lemma CONJ (c)). In
the words of row 669 (L107, L111): a bound on the strain of the vacuum transport on a set that the flow does
not leave, with exceptional sets; "the same large-field problem as in the existence proof, moved to the
infrared". I found no first lemma of that theory at order-one coupling that is not (W), (TILT-COV-sup) or (FL)
of row 1510.

No obstruction theorem over all tools is claimed. What is proved is narrower: the frame (CONJ), the
restart (TR2, COLD), the floor at a transition (FLOOR, given recalled facts), and the chain rule (VOL). The
statement "every generator class is on file" is a judgment over the classes in table 2.2.

Equivalence, as the lead's rule asks: (R11') on [1/25600, beta_1] implies the seed of bare Wilson at every
coupling up to beta_1, which is (NOCRIT) up to beta_1 (row 708 5.1). I cannot show that it is weaker than
that, and I cannot show the converse. So (R11') is at least as strong as a closed target on the bare lattice,
and it stays a trigger, not a row.

### 6.2 Change proposed to trigger (R11) (for the lead; I did not edit the registry)

Replace "K growing more slowly than log n" by "K at most C log n for one constant C, on cold cubes
(G below 10^(-3)) only" if check Row 1 below confirms TR2. Add to its last clause: "an identity on one box
cannot play the part of the trace anomaly ((V1): the ratio depends on the level through its volume slope); a
two-box identity is a block step". The clause "by a method that fails for Ising and compact U(1)" has the
exact form of Corollary FLOOR.

### 6.3 The next two rows and their decisive outcomes

I propose no attack row and no build row.

**Row 1, `gap-r11-tool-design-fable-check-astra62` (cross-provider check of this file; gpt-6.2-astra).** Order:
(i) Proposition TR2: the two-stage line, Theorem SH (i) at r = 4 with step (2, 2, 3) and K = 22.2, Lemma E' in
three directions from the side 2^k 4a to L = 4 (2^k a)^2, the time range [A, L/2], the factor L^(1/2), the
start at 256^3, the count of steps; (ii) Remark COLD; (iii) Corollary FLOOR: which class lemmas the Ising
member and compact U(1) really satisfy, and the start constants for U(1); (iv) Lemma CONJ and whether a
generator class outside table 2.2 exists; (v) Proposition VOL and whether the lane holds a single-box
identity that it rules out. Decisive outcome: TR2 HOLDS, and the registry wording of (R11) changes as in 6.2;
or FAILS at a named line, and (R11) keeps the wording of row 1515. If (iv) names a class, that class is the
next design row.

**Row 2, `gap-r11-coldrate-guide` (a guide run, not a proof step; Opus or Codex runner under the numeric
lock; only if the lead wants a kill test of (R11') itself).** Measure the two sides of (R11') at integer
times for Wilson SU(2) on cubes L = 8, 12, 16 at beta = 2.2, 2.3, 2.4: the plaquette shift
6 t L^3 (abar_inf - abar_t), with abar_inf from the longest time, against t times the thermal energy from the
ratio Z(t+1)/Z(t) by a coupling-integration or snake method. Written pass and fail before the run: the ratio
K_L of the two sides, with its statistical error, stays below 6 log L at every point (pass, consistent with
the scaling value near 3.3 of row 708 L158); or it grows faster than log L between L = 8 and 16 at fixed
t E_1 (fail: (R11') is in doubt and (R11) is retired). A pass proves nothing and moves no node. I rank it
low: the cold condition G < 10^(-3) needs times that are costly at these sizes, and no outcome supplies a
method. The lead may skip it.

## 7. Repo search, labels, credits, what was not done (written 2026-11-25T05:28Z)

### 7.1 Repo search

- Local (`FINISH.md`, `library/open-core.md`, `library/gap-*.md`, `library/prior/gap-*.md`): "Lipschitz
  transport" 6 files, "transport map" 13, "Kim-Milman" 4, "quasi-adiabatic" 2, "HS-sup" 11, "virial
  identity/theorem" 11, "vacuum transport" 0, "conformal vector/Killing" 1 (unrelated). The hits that bind
  this file are cited in table 2.2. `library/open-core.md` has no entry for (VIR), the trace anomaly or the
  transport along the coupling. "restart", "interleav", "any constant", "sub-interval" in the row-708 family
  (`gap-mid-max.md`, `gap-mid-check.md`, `gap-vir-sc.md`, `gap-vir-sc-check.md`, `gap-phys-seed.md`,
  `gap-skeleton-final.md`, `gap-crux-fp.md`, `gap-seed-direction-fable.md`) and "VIR ... restart" in
  `FINISH.md`: no hit. So TR2 is not on file under these words; it is elementary and I do not call it new.
- Cross-branch (bare blob-less fetch in my own /tmp scratch folder): pattern "VIR-log, VIR_K, relative
  transport, restarted transport, adiabatic gauge, volume slope, trace anomaly, lattice beta function,
  LEV_K" on the 83 mass-gap `.md` files of main and on 7 files of PR 10114 (`MASS_GAP*.md`, `RTARGET.md`).
  Main: 16 files, all landed copies of this lane's notes (the row-708 family and `ROWS.md`). PR 10114: no
  hit. PRs 10133, 10134, 10141, 10144 were not searched.
- Sussman-Alpoge (with Claude and Codex): not searched again in this row. Rows 708, 710, 711, 1511 and 1515
  record that the account and the outline hold no statement on the gap or on a coupling derivative of
  levels (outline 4638-4641; CA-I 2699-2713). No statement of theirs is used in a proof here.

### 7.2 Labels

- **Proved here** (one author, checked by no one): Lemma CONJ (first-order perturbation theory; not new);
  Proposition VOL (a chain rule under the hypothesis (SCAL), which is a definition and not a lattice fact);
  Proposition TR2 and Remark COLD, given the statements read in rows 705 and 708; Corollary FLOOR, given TR2
  and the recalled facts in its brackets.
- **Read**, not re-derived: Theorem TR, Remark CH, Corollary TR1 and its start, Lemma 4.1, Lemma 4.2 (row
  708; checked by Claude Opus 5.5, row 709); Theorem SH, the table of thresholds, Lemma E2 with remark (i)
  (row 705; checked by Claude Opus 5.5, row 707); Theorem U and (RK) (row 710; checked, row 715); everything
  cited from rows 669, 677, 680, 913, 1356, 1510, 1511, 1515.
- **Argued**: the reading under Proposition VOL; the Harnack remark in Section 5; "what TR2 changes".
- **Guessed**: that no generator class outside table 2.2 has a provable form bound; that (R11') is true.
- **Guide numbers only**: the slopes sigma_i in 3.1; the value 3.3 and the bound 6 log L in Row 2.

### 7.3 Not done

- No tool was designed and no component of a tool was built. (PUR-io), the seed and the gap are not moved.
- No numeric run (memory read 37 percent free; nothing here needed one). No Lean.
- The start constants of Corollary FLOOR for compact U(1) and for the Ising member were not computed.
- I did not read the proofs of Theorem SH, Lemma E2 or Theorem TR again line by line; I used their
  statements and the checks on file.
- The checks of rows 1510 and 1515 (rows 1513, 1516) were not on file at the pinned commit.

### 7.4 Credit

Row 708 (Claude Fable 5.2 max) for Theorem TR, Corollary TR1, (VIR_K), (LEV_K), (DEF_K), (VIR-log) and the
verdict on the lattice trace anomaly; check row 709 (Claude Opus 5.5). Row 705 (Claude Fable 5.2 medium) for
Theorem SH and Lemma E2; Codex gpt-6-astra (row 699) for Lemma E'. Row 710 for Theorem U and (BAND-sc).
Row 669 (route B1, (T), (T-avg)), rows 913 and 1356 (the transport forms; E. Milman's observation on
contracting maps, as credited there), rows 670, 677, 680 (Route Z, (HS-sup), dominance form). Row 1511
(gpt-6.2-astra) and row 1515 for the reduction to (R11). Kato and Rellich for analytic perturbation theory.
Harnack. Michael, Rothe and Karsch for the lattice sum rules (recalled; abstracts read in row 711). Guth;
Frohlich and Spencer (recalled). Sussman and Alpoge, with Claude and Codex, for the account and the outline;
Balaban for the block method; neither is used in a proof here.

## 8. Result

RESULT: Row 1517 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; no numeric run, no Lean, nothing committed). Outcome of the third kind: no tool for (R11) was designed and no component of one was built; (PUR-io), the seed and the gap are not moved. Proved by hand: Lemma CONJ (every single-box relative bound is a generator A with a form bound for That' - [A, That]; with all A allowed it is (LEV_K) itself); Proposition TR2 with Remark COLD (restarting Theorem TR on cubes of growing side, with Theorem SH and Lemma E' as read, the consumer accepts K at most C log L for any one constant C, and only on cold cubes with G below 10^(-3); not found on file, elementary); Corollary FLOOR (given TR2 and recalled facts: in the Ising member and in compact U(1) the output inequality fails on some cold cube inside the crossing interval by more than any C log L); Proposition VOL (under an exact scaling law the ratio of action deficit to energy of a level is kappa (1 + volume slope), so no identity on one box plays the part of the trace anomaly, and a two-box identity is a block step, a closed line). Found again, not new: the one candidate I derived blind (conjugation by the vacuum transport, level velocity = strain in the kinetic measure) is route B1 of row 669 with (T) and (T-avg), also rows 913 and 1356; the complex-coupling (Harnack) form is Route Z. Every generator class I could state is one of row 708's ways, B1, or needs the gap (a judgment over a table, not a theorem). First component that could not be built: a selective form bound for a class of generators on cold thermal states, in a norm that is neither a supremum over fields nor the eigenvectors; in row 669's words a transport theory with exceptional sets at order-one coupling. Open: (R11') (the exact output, Section 5), at least as strong as the seed of bare Wilson on the interval; whether it is weaker is not shown. Proposed: reword trigger (R11) to "K at most C log n, any C, cold cubes" after a check. Next: a cross-provider check of this file (TR2 first); then, optional and low, a guide measurement of the cold rate K_L on cubes 8 to 16.
