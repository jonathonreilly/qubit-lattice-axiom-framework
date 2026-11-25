lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T17:03Z

# Row 1517, gap-r11-tool-design-fable: the missing tool for trigger (R11)

Worker: Claude Fable 5.2, high effort, Mac mini worker 1. Pinned commit 3cd437195 on `claude/ym4d-hard-route`.
Not checked by another model. Research-stage working state; nothing here is a public claim.

## Status log (times from `date -u`)

- 2026-11-25T05:03Z: file created. Plan below. Nothing proved yet.
- 2026-11-25T05:04Z: read the row, FINISH rule sections, GOAL.md, row 708 Sections 1-5 (`gap-mid-max.md` L21-216), row 710 Sections 2-4, 6-9 (`gap-vir-sc.md`), row 1515 in full (`gap-seed-direction-fable.md`), registry lines R10-R12, W-CUBE-23. Section 1 written.
- 2026-11-25T05:21Z: Section 2 written. First candidate (a conjugated operator inequality with the vacuum transport as generator) derived blind, then found on file: route B1 of row 669, row 913 3d, row 1356 Ways 1 and 3. Not presented as new. Memory 37 percent free: no numeric job in this row.

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

