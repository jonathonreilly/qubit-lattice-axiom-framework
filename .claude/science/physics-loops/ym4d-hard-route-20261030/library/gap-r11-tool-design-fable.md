lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T17:03Z

# Row 1517, gap-r11-tool-design-fable: the missing tool for trigger (R11)

Worker: Claude Fable 5.2, high effort, Mac mini worker 1. Pinned commit 3cd437195 on `claude/ym4d-hard-route`.
Not checked by another model. Research-stage working state; nothing here is a public claim.

## Status log (times from `date -u`)

- 2026-11-25T05:03Z: file created. Plan below. Nothing proved yet.
- 2026-11-25T05:04Z: read the row, FINISH rule sections, GOAL.md, row 708 Sections 1-5 (`gap-mid-max.md` L21-216), row 710 Sections 2-4, 6-9 (`gap-vir-sc.md`), row 1515 in full (`gap-seed-direction-fable.md`), registry lines R10-R12, W-CUBE-23. Section 1 written.

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

