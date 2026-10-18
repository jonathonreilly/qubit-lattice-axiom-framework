# UV-1 PREREG: is the overlap's RP failure a grid-scale effect?

Written 2026-10-14 ~21:35-21:50Z (`date -u` at start of writing: 21:33:53Z), BEFORE any UV-1 run. Agent: Claude Opus 5.5
(same family as K2/K2b/K2c/NT-2 and the supervisor; nothing here is independent). Only pre-run action: a numpy timing
benchmark on random matrices (0.30 / 0.51 / 0.89 ms per overlap determinant at N = 48 / 64 / 80), used for the cost plan.

Read first: packet `SUMMARY.md`, `ROUTES.md` (full), `TESTS.md` (UV-1 at :64-67 and the UV-1 amendment at :125-131);
`docs/MINIMAL_AXIOMS_2026-06-29.md` (full, 233 lines); `kills/K2c/K2c_REPORT.md` (full) and `PREREG.md` (power wording);
`ref_K2c/REFEREE_VERDICT.md`; `panel_D/qinfo/statement.md:276-281` (runner-up test); `next/NT2/REPORT.md`;
`panel_D/lattice/statement.md:93-98,268-269` (triangle weight is positive type; torus triangle W-matched run).
Code reused (copied unchanged into `scripts/`): K2's `lat2d.py`, K2b's `k2b_lib.py`, K2c's `k2c_lib.py`.

## 0. FIXED readings (TESTS.md:64-67 and amendment :125-131), copied, not changed

UV-1 setting: 2D U(1), vector-like overlap, K2c code; β_g > 0 (≥ 3 values, e.g. 1, 4, 8); W-matched witnesses restricted
to test functions supported at distance ≥ t₀ from the reflection plane (t₀ = 1, 2, 3, 4); tori Lt = 12-20.
- **UV-ONLY:** at every β_g, the negativity vanishes (PSD at power) for t₀ ≥ t* with t* ≤ 3 lattice spacings.
- **PERSISTS:** a quadrature-converged negative eigenvalue at t₀ ≥ 3 for some β_g.
- **OPEN:** otherwise.
Amendment: two arms, readings applied to each separately; the **primary arm decides the headline**.
- **Primary arm:** positive-type triangle (Fejér) profile with the same support (isolates the overlap determinant).
- **Secondary arm:** the hard support, as originally registered.

## 1. Model (K2c conventions, unchanged except β_g)

- 2D U(1), Lx = 2. Torus: periodic x, antiperiodic t (K2c `Geom(2, T, True, 1)`). Open time (supplementary proxy only):
  antiperiodic x, open t ends (`Geom(2, T, False, -1)`). Link reflection θ: t → 1 − t, Θ = θ∘conj (K2 conventions).
- Overlap: Neuberger, M = 1, m = 0.05 (K2 `logdet_batch` / K2b `logdet_op` 'O'). Controls: Wilson r = 1, m = 0.05
  ('W') and pure gauge ('PG').
- Gauge weight on EVERY plaquette p (δ = 0.6):
  - primary: w_tri,β(p) = (1 − |p|/δ)₊ · exp(β_g (cos p − 1));
  - secondary: w_hard,β(p) = 1(|p| < δ) · exp(β_g (cos p − 1)).
  - **Choice stated (NT-2, amendment):** the triangle profile is used because NT-2 showed the hard bound is itself not RP
    in 3D (and for odd Lx in 2D); the triangle has Fourier coefficients ∝ (1 − cos nδ)/n² ≥ 0 and exp(β cos p) has
    coefficients I_n(β) ≥ 0, so their product is positive type for every β ≥ 0 (proved, elementary: product of
    positive-type functions = convolution of nonnegative sequences). Hence the primary-arm PG and Wilson kernels are RP
    (Osterwalder–Seiler), and any primary-arm negativity is the overlap determinant's.
- β_g values: **0 (reference = K2c), 1, 4, 8.** Reading (not a claim about Lx = 2 physics): continuum Schwinger mass
  m_S = 1/√(π β_g) = 0.56, 0.28, 0.20 lattice units at β_g = 1, 4, 8.
- Bulk plaquettes inside the test-function region enter as positive diagonal factors and drop out after normalization
  (diagonal congruence preserves inertia). Plaquettes in the buffer and crossing gaps are integrated with w.

## 2. Depth-t₀ test functions (definition)

- A depth-t₀ test function depends only on links with both ends at time ≥ t₀ (and, on the torus, ≤ T + 1 − t₀, i.e.
  distance ≥ t₀ from BOTH reflection planes; T = Lt/2). It is gauge-averaged; as in K2c the witnesses are point
  configurations (referee: legitimate via smooth bumps, `ref_K2c/REFEREE_VERDICT.md:3`).
- Kernel entry K_t₀(a, b) = ∫ (buffer links, both sides) ∫ (crossing links) det D_ov · Π w(plaquettes in buffer and
  crossing gaps). Buffer t-links fixed to 1 (temporal gauge, by Haar invariance and gauge invariance of integrand and
  of the test functions); one crossing link per plane fixed as in K2c; buffer x-links parametrized by the buffer-gap
  plaquettes (unit Jacobian): u_t(x) = u_{t+1}(x) + q_t(x).
- **W-matched:** every pool member has Wilson line W = 0 at slice t₀ (torus: also W at slice T + 1 − t₀ matched to a
  common value), by holonomy shift (plaquettes unchanged). Then the gauge flux Φ through each buffer+crossing region is
  0 for every pair, and the hard/triangle pure-gauge factor is constant (no cusp masking).
- Monotonicity (proved, trivial): a depth-t₀′ test function is also a depth-t₀ test function for t₀′ > t₀, so a negative
  direction at depth t₀′ implies one at depth t₀; PSD for ALL depth-t₀ functions implies PSD at every t₀′ > t₀.

## 3. Feasibility (stated before running) and what is computed

Integration dimension per kernel entry (Lx = 2): open, one plane: 4t₀ − 3; torus, two planes + Polyakov variable:
8t₀ − 5 (t₀ = 1: 3; t₀ = 2: 11; t₀ = 3: 19). The crossing/buffer weights have kinks (triangle at 0, support ends) that
lie along non-coordinate hyperplanes after the Stokes constraint, so plain product rules converge only algebraically.
At 0.3-0.9 ms per determinant, an 11-dim product rule with two convergence levels is out of budget (≥ 10⁷ evaluations
per entry at the second level). Therefore:

- **Stage A (torus, the FIXED geometry), t₀ = 1:** Lt = 12 and 16 (Lt = 20 if time), β_g ∈ {0, 1, 4, 8}, both arms.
- **Stage B (open-time proxy, supplementary), t₀ = 1 and 2:** Lt = 12, β_g ∈ {0, 1, 4, 8}, both arms. t₀ = 2 is a 5-dim
  integral done by nested kink-aligned Gauss quadrature (§4). t₀ = 3, 4 (9, 13 dims) are not attempted.
- **Torus t₀ ≥ 2 is NOT computed with a convergence check.** (Optional, only if time remains: a single coarse torus
  t₀ = 2 level, labelled descriptive; it cannot enter any reading.)
- Consequence, registered now: unless something unexpected makes torus t₀ ≥ 2 computable, the FIXED reading for each
  arm will be **OPEN, reason "torus t₀ ≥ 2 not computable at power within budget"**. The open-proxy results are reported
  with their own supplementary labels (§6) and cannot by themselves give UV-ONLY or PERSISTS (the FIXED setting is tori).

Shared-determinant trick (checked identity, no approximation): the determinant at a quadrature node does not depend on
β_g or on the arm; only the weight does. Nodes are built with breakpoints at the union of all kinks of both arms, so
one determinant pass per (pool, level, op) gives all β_g and both arms.

## 4. Quadrature and error estimate

- **t₀ = 1 (torus and open):** crossing variable d₀ per plane, Gauss–Legendre on pieces of [max(−δ, Φ−δ), min(δ, Φ+δ)]
  split at {0, Φ} (both arms), n points per piece; torus Polyakov variable by trapezoid with nw points (K2c's node
  layout, `lat2d.py:198-207`, with shared breakpoints). Levels (n, nw): lo (4, 4), hi (6, 6), third (8, 8) on 24 random
  pairs + all diagonals (open: nw unused; lo 8, hi 12, third 16).
- **t₀ = 2 (open):** variables: buffer plaquettes q (2 per side, 4 total), then d₀ innermost. Nested 1D Gauss–Legendre
  with n points per piece, each variable's interval split at its own weight kinks {−δ, 0, δ} and at every point where
  the residual flux R − q (R = Φ − sum of outer q's) hits a kink of the inner integrated function, i.e. R − q ∈ {jδ :
  |j| ≤ (number of remaining plaquettes)}. On each piece the integrand is analytic, so convergence is exponential.
  Levels: n = 2 (lo), n = 3 (hi); third level n = 4 on 6 random off-diagonal pairs + their diagonals.
  Cost cap: if the hi level exceeds 4·10⁶ determinant evaluations for the pool, k is reduced (k = 6 → 5 → 4) before
  running; the reduction is logged.
- **Error estimate** (K2c's, `K2c_REPORT.md:131-133`): E = k · max(q, q₃) + 1e-13, q = largest entry change lo → hi,
  q₃ = largest change hi → third on the subset. Quadrature-converged negative: λ_min < −10E (on the hi-level kernel).
  E is an a-posteriori estimate (referee wording: "quadrature-converged", not "certified").
- Cleanliness: min |eig H_W| > 0.1 at every evaluated overlap point; pool bulk plaquettes ≤ 0.55 (margin).

## 5. Pools (fixed now)

Stage A (torus, depth 1, W-matched both planes):
- A12h: K2c `pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz` (k = 24).
- A12t: lattice panelist's `pool_K2c_wgsearch_tri_O_torus_Lt12_seed4412.npz` (k = 24).
- A16h: K2c `pool_K2c_wgsearch_hard_O_torus_Lt16_seed4416.npz` (k = 16).
- A12s8 (new, power at β > 0): K2c's `wgsearch`-style greedy W-matched search on the torus Lt = 12 under the PRIMARY
  weight at β_g = 8 (objective: λ_min of the lo-level overlap kernel; 4 random + 4 perturbation candidates per step,
  start k = 8, end k = 16, seed 8812), using my β-aware node code. Same at Lt = 20 (A20s8, seed 8820, k = 12) if time.
- Validation V0 (must pass before anything else is read): my shared-node code on A12h at β = 0, hard arm, reproduces
  K2c's λ_min = −1.4728e-4 to 4 digits; and on A12t at β = 0, triangle arm, the panelist's −1.4335e-4.

Stage B (open Lt = 12, W-matched at slice t₀):
- B-sel: from K2c `pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz` (k = 20), compute the β = 0 hard depth-1 kernel and
  take the k_B = 6 configurations with the largest |component| in the λ_min eigenvector (k_B reduced per the cost cap).
  - Depth 1 = these configurations as they are (slices 1..6).
  - Depth 2 = the same configurations moved one slice deeper: their slices 1..5 (x-links and t-links between them)
    placed on slices 2..6; slice 1 and the t-link 1→2 become the integrated buffer. W at slice 2 = old W₁ = 0
    (matched). This compares identical witnesses at depth 1 and depth 2.
- B-rand (if time): 6 random margin-admissible W-matched (at slice 2) configurations at depth 2, seed 2602.

## 6. Readings

**FIXED readings, per arm (torus data only):** exactly §0. Operationally:
- PERSISTS needs a quadrature-converged negative torus kernel at t₀ ≥ 3 for some β_g (not computable here, §3).
- UV-ONLY needs PSD-at-power torus kernels at every β_g for all t₀ ≥ t*, t* ≤ 3 (needs torus t₀ ≥ 2, not computable).
- Hence OPEN for each arm unless torus t₀ ≥ 2 becomes computable with a convergence check. The headline is the primary
  arm's reading.

**PSD at power** (used in all supplementary labels): λ_min ≥ −10E AND 10E ≤ 0.1·|λ_min^ref|, where λ_min^ref is the
quadrature-converged negative λ_min at depth 1 for the same arm, β_g and configurations (the method would have seen a
violation ten times smaller than the depth-1 one). If depth 1 is itself not negative at that (arm, β_g), there is no
power reference and the cell is "no reference".

**Supplementary labels (not FIXED; reported per cell):**
- Stage A (torus depth 1, per arm, β_g, pool): TORUS1-NEG (λ_min < −10E) / TORUS1-PSD (λ_min ≥ −10E) — this describes
  how the grid-scale negativity depends on β_g; it says nothing about depth by itself.
- Stage B (open depth 2, per arm, β_g): PROXY-NEG(2) (λ_min < −10E) / PROXY-PSD-at-power(2) / PROXY-UNRESOLVED(2).
  - If PROXY-NEG(2) at some β_g in the primary arm: reported as "open-time proxy: negativity survives one buffer
    slice" (suggested evidence toward PERSISTS, not the reading).
  - If PROXY-PSD-at-power(2) at every β_g in the primary arm: "open-time proxy: depth-1 witnesses lose their negativity
    one slice deeper" (suggested evidence toward UV-ONLY, not the reading; note it is a statement about these witnesses,
    not about all depth-2 test functions).
- Ratio diagnostic (descriptive): ρ(β_g) = λ_min(depth 2)/λ_min(depth 1) on B-sel, both normalized as min/max.

**Controls (must hold, otherwise the cell is OPEN-BUG):**
- Primary arm, every stage: W and PG kernels PSD within 10E (proved RP, §1).
- Secondary arm: PG PSD within 10E (Lx = 2: K_PG = Σ ĉ_n² e^{inΔW}, squares; W-matched: constant). W + hard on W-matched
  pools PSD at β = 0 (K2c §2(d)); at β > 0 reported descriptively.
- At β = 0 the depth-1 numbers must equal K2c / panelist values (V0).

## 7. Memory and process

- Cap 0.4 GB per run: every run goes through `scripts/capped.sh` (copy of NT-2's watchdog with the limit set to
  400000 KB); one process at a time; OMP/OPENBLAS/MKL threads = 2.
- Array estimates: largest batch = 32 points × N² complex × ~6 temporaries; N = 64 (Lt = 16): 32·64²·16 B·6 ≈ 13 MB;
  N = 80: 20 MB. Node arrays at depth 2: ≤ 2·10⁵ nodes × (4 links + weights) × 8 B ≈ 10 MB per entry. Expected peak
  RSS ≈ 120-200 MB (K2c's largest was 234 MB).
- Nothing left running at return.

## 8. Labels

proved (my argument, unrefereed) / checked (a run here) / suggested / reading / comparator. Every number cites its
`.out` file and line.

---

## Follow-up F1 (dated 2026-10-14 21:41Z; written after the first Stage-A run started and after a 3-config smoke test of the
## depth-1 code on the open pool (β barely moved λ_min there: −1.101e-5 → −1.098e-5 relative, β = 0 → 8), BEFORE any
## run of the item below). Nothing above is edited.

**F1-a. β_g → ∞ limit comparator on the tori, t₀ = 1..4 (new, labelled comparator; cannot by itself give a FIXED reading).**
- Reason (reading): as β_g grows at FIXED lattice depth t₀, the buffer/crossing plaquettes are pinned (width ~ β^{-1/2}),
  so the buffer smooths LESS, not more. For both arms w_β/∫w_β → δ(p) (both profiles equal 1 at p = 0 and are continuous
  there), so the normalized depth-t₀ kernel converges, as β_g → ∞, to
  K_∞^{(t₀)}(a, b) = ∫ dw/2π det D_ov(a_ext, flat crossing A, Polyakov w on crossing B, Θ b_ext),
  where a_ext continues the witness flatly through the buffer (buffer x-links = copy of slice t₀ / slice T+1−t₀,
  buffer t-links 0), and W-matching makes the flat crossings consistent (Φ_A = Φ_B = 0). Corrections: O(1/β) (hard),
  O(β^{-1/2}) (triangle, |p| term) — suggested (Laplace asymptotics), not proved here.
- Consequence used in the report (reading, not a FIXED reading): if K_∞^{(t₀)} is quadrature-converged negative at
  t₀ ≥ 3 on a torus, then the fixed-lattice-depth negativity cannot vanish for all sufficiently large β_g; UV-ONLY in the
  literal fixed-t₀ sense would then be excluded at large β_g, and the physically meaningful variable is t₀·m_S
  (qinfo :277-279), which → 0 at fixed t₀ as β_g → ∞.
- Runs: tori Lt = 12, 16, 20; t₀ = 1, 2, 3 (Lt = 12) and 1..4 (Lt = 16, 20); test region slices t₀..T+1−t₀ (both
  planes). Pools: W-matched (W = 0 at slice t₀, common W at slice T+1−t₀), margin 0.55; greedy search with objective
  λ_min of K_∞ (start 8 random, 4 random + 4 perturbation candidates per step, end k = 16; seeds 7000 + 100·Lt + t₀).
  Levels: Polyakov trapezoid nw = 8 (lo), 12 (hi), 16 (third, all entries). E as in §4. Controls: Wilson K_∞ and PG.
- Labels: INF-NEG(t₀) (λ_min < −10E) / INF-PSD(t₀) (λ_min ≥ −10E; "at power" only if INF-NEG(1) at the same Lt with
  10E ≤ 0.1·|λ_min(t₀ = 1)|).
- Open-time cross-check: K_∞ at depth 1 and 2 on the Stage-B witnesses, to compare with finite-β depth-2 values.

---

## Follow-up F2 (dated 2026-10-14 21:53Z; written AFTER seeing Stage A (torus depth 1, all β, both arms: negative,
## β-insensitive), the F1-a β = ∞ runs (negative at t₀ = 1..3 on Lt = 16 and t₀ = 1..4 on Lt = 20, falling by ~10-150×
## per slice; the 2-slice witness families at Lt = 12 t₀ = 3 and Lt = 16 t₀ = 4 PSD), and after a bookkeeping bug in the
## depth-2 code was caught by its own V-B0 check (killed before any kernel was computed; fixed; V-B0 then exact).
## Nothing above is edited.)

Note on F1 header: its time stamp "21:41Z" was typed ahead; `date -u` right after appending it read 21:40:25Z.

**F2-a (robustness of the β = ∞ depth signal).** Second seed and a longer search for the deepest powered cells:
Lt = 16 t₀ = 3 and Lt = 20 t₀ = 3, 4 with K = 24, seeds 7500 + 100·Lt + t₀. Same labels as F1-a. A cell counts as
"robust INF-NEG" only if both seeds give λ_min < −10E.

**F2-b (descriptive, locality of the free overlap in time).** Free field (all links 1), torus Lt = 20, Lx = 2: the
largest block norm ‖D_ov(x, t; x′, t′)‖ as a function of |t − t′|; fitted decay rate ν per lattice spacing. Used only to
compare with the per-slice decay of the β = ∞ depth signal (reading).

**F2-c (classification rule for "exponentially small but nonzero", registered before the depth-2 finite-β result
is seen).** The FIXED readings do not separate "vanishes" from "falls exponentially with depth at a lattice-scale rate".
The report will state the literal reading (OPEN per §3/§6, unless torus finite-β depth ≥ 3 data exist) and, separately,
the reading the β = ∞ data support: "PERSISTS-at-fixed-lattice-depth for large β_g (existence, by continuity), with
size falling ~e^{−κ t₀}"; κ is quoted from the Lt = 20 β = ∞ cells. This second reading is a comparator, not FIXED.

**F2-d (dated 22:05Z, bug hunt, before running).** V-INF: recompute K_∞ on the saved β = ∞ pools Lt = 20 t₀ = 4 (seed 9004)
and Lt = 16 t₀ = 3 (seed 8603) with K2c's independent explicit-link torus builder (`k2c_v6_torus_verify.py:9-31`,
copied verbatim; overlap via X(X†X)^{-1/2}), flat crossings set from explicit plaquettes, Polyakov trapezoid nw = 12.
Pass: λ_min agrees with the main code to 1e-3 relative and the crossing plaquettes are 0 to 1e-12. Fail → those F1-a
cells are reported as unverified.
(F2 header time "21:53Z" was typed ahead; `date -u` right after appending F2 read 21:52:23Z.)
