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
(b) If for one A the form inequality <phi, D_A phi> <= K <phi, Phi(That) phi> holds for all phi, then every
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
K_SH = 22.2 (L89-99; these constants are the ones used in the proof of TR1), and Lemma E' in the form used in
the proof of SH (ii) (L107): for an integer L >= 2^k 4a, g(2^k a; L^3) <= (L/(3 2^k a))^3 log(1 + s_k), with
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

