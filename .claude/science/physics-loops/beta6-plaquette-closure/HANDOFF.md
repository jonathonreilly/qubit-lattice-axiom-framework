# Handoff — β=6 Plaquette Closure Loop

## Where this loop stands (after cycle 3, 2026-05-30)

- **Cycle 3 characterized the analytic-continuation CLASS of Δ(β)** (the cycle-2
  HANDOFF item 3 — now ANSWERED), shipped as a frontier note + verification
  runner (`scripts/frontier_beta6_delta_analytic_class_2026_05_30.py`,
  PASS=33/FAIL=0; `docs/BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`):
  - **Class — PROVEN at finite L, CONDITIONAL thermodynamic.** Positivity of
    Haar × Boltzmann weight on the compact domain gives `0 < Z_L(β) ≤
    exp(β·N_plaq)` for all real β ⇒ `Z_L` entire with NO real Lee-Yang zero ⇒
    `Δ_L` real-analytic on `[0,6]`, nearest singularity a complex-conjugate
    pair. **Rigorous but finite-volume** (textbook Yang-Lee template; the finer
    half of the retained reduction-existence theorem). The **thermodynamic**
    real-analyticity at β=6 is **conditional** on the standard
    no-real-bulk-transition import (SU(3) smooth crossover; Fisher zeros
    5.54±i0.10 off-axis; SU(N≤4) crossover-only) — finite-L positivity does NOT
    transfer across L→∞ (Yang-Lee pinch). The **location** `|β_c|` is OPEN (the
    ρ_{p,q}(6) lane-killer restated in the β-plane).
  - **Lee-Yang localization (single-plaquette, RIGOROUS):** nearest zero of the
    entire `Z_1plaq` at `β_c = 3.3175 ± 7.5047 i`, `|β_c| = 8.205`, arg 66.15°,
    residual → 1e-34 (genuine zero, stable across truncation D=30..60). β=6 is
    INSIDE the single-plaquette disk (6/|β_c| = 0.73).
  - **Series-asymptotic cross-check:** the single invariant `u = c₂/c₁² = 20/49
    < 1/2` exponent-independently EXCLUDES any positive-real divergent algebraic
    branch point on `(0,6]`; minimal `[0/2]` Padé gives a complex pair (disc =
    −67/144 < 0). (Branch-point-exclusion and complex-pair are NOT independent —
    both functions of the same `u`, disc = c₁²(4u−3); the location is a
    one-parameter family ~0.6..8.8, NOT measured by 3 coefficients.)
  - **d-log-Padé verdict — the decisive cycle-3 finding:** applicable CLASS
    **yes**, controlled closure with the 3 known coefficients **NO**, **β⁸
    (d₅..d₈) STILL REQUIRED to even activate**. A complex pair is a degree-2
    d-log denominator; 3 coeffs of Δ give only 2 of `H=(log h)′`, one short of
    an `[1/1]`. **This β⁸ floor is a CLASS-INDEPENDENT rank constraint —
    proving the class adds ZERO coefficients and cannot relax it.** So item 3
    (below) is ANSWERED but is **NOT a shortcut around the β⁸ wall**: the class
    being (conditionally) the complex-pair class does not let the 3 known
    coefficients reach β=6, and gives no error bound on Δ(6). LY used ONLY to
    characterize the class (honors no-go item 5: LY-as-closure foreclosed).

## Where this loop stood (after cycle 2, 2026-05-30)

- **d₆ = 7/5668704 (cycle 1) and d₇ = 5/17006112 (cycle 2) computed EXACTLY**,
  shipped as bounded notes + audit-companion runner. Reproduce the retained
  anchor d₅ = 1/472392. Per-shell d₇ = 5/68024448 (four identical shells).
  Per-order ratios: **d₆/d₅ = 7/12, d₇/d₆ = 5/21 — NOT constant.**
- **Tadpole/geometric ansatz FALSIFIED (cycle 2).** Harness #2255 with
  `EXACT_HIGHER = {6: 7/5668704, 7: 5/17006112}` reads `[FALSIFY]
  tadpole/geometric`: the single-pole geometric prediction (7/12)·d₆ =
  49/68024448 misses the exact d₇ = 5/17006112 by ~59% (rel 1.45 vs exact) ≫ 5%
  window. The resummation route does NOT reduce to a geometric tail; no closed
  boosting form supported. Forward truncation `<P>(6)_trunc ≈ 0.5789` (gap
  0.0151) is a TRUNCATED partial sum, not a closure.
- **Engine wall BEATEN (cycle 2).** The cycle-1 sympy engine hit a >30min
  3^(2k) wall (one 8-plaquette moment ~270s). Cycle 2's optimized engine
  (`link_tensor_frac` + `_contract_frac` + `_integrate_word_frac` in the same
  runner): (1) per-link integral built SPARSELY from invariant-basis supports
  (not the 3^(2(p+q)) dense grid), (2) pure-int Fraction arithmetic + min-degree
  variable elimination, (3) early-zero on unbalanced links. Worst moment ~0.5s;
  exact d₇ in ~2min. Two-engine agreement (V4b: Fraction reproduces sympy d₅,
  d₆ exactly).
- **Engine (single self-contained artifact):**
  `scripts/frontier_beta6_connected_coefficient_2026_05_30.py` — both the sympy
  reference engine (V0–V4 validation) and the optimized Fraction engine (V4b,
  V5, V5b). To compute d₈, extend `compute_dn_frac` / the multiplicity sum; but
  see the checkpoint below before doing so.

## Resumable next action (CYCLE 4) — CHECKPOINT at the wall

**Do NOT run another coefficient cycle, and do NOT expect the analytic class to
rescue the lane.** The in-runway analytic levers are now ALL resolved:

- tadpole/geometric ansatz **FALSIFIED** (cycle 2);
- analytic-continuation class **characterized** (cycle 3): complex-pair, no real
  branch point on `[0,6]` — PROVEN at finite L, CONDITIONAL thermodynamic;
- d-log-Padé **predictive** test is **out of runway** (it needs {d₅..d₈} = β⁸,
  and β⁸ is at/past the treewidth-29 wall — see below), and cycle 3 showed this
  β⁸ floor is a **class-independent rank constraint** that proving the class
  **cannot** relax.

β=6 closure now requires a genuinely NEW dynamical input for ρ_{p,q}(6), a
`/first-principles` / `/frontier` research item, NOT a brute extension. Candidate
directions (each its own multi-session item, none a coefficient cycle):

1. **A Münster-style graphical strong-coupling organizer** that sums connected
   SU(3) contributions analytically (avoiding brute cluster enumeration + 3nj
   contraction). This could in principle reach the resummation depth the d-log-
   Padé route needs, but it is a new analytic technique, not an extension of
   this engine.
2. **A rank-aware / tree-decomposition contractor** that defeats the treewidth-29
   wall for the unmarked 3D spatial Wilson environment (the doubly-walled object).
3. **[ANSWERED in cycle 3 — analytic class characterized.]** The surviving
   hypothesis (complex-pair dominant singularity, no real branch on `(0,6]`) is
   now PROVEN at finite L and CONDITIONAL in the thermodynamic limit (on the
   no-real-bulk-transition import). **But this does NOT close β=6 and does NOT
   shortcut the β⁸ wall** — proving the class adds no coefficients, and a
   complex pair still needs a degree-2 d-log denominator (≥ d₅..d₈). The genuine
   open residual extracted from cycle 3 is now (3′): a **from-primitives proof
   that SU(3) pure-gauge has no real bulk transition on `[0,6]`** (the L→∞
   clause currently held only by lattice import) — necessary to upgrade the
   thermodynamic class from CONDITIONAL to PROVEN, though even then β⁸ + a
   continuation past the radius remain required.

**Single decisive next step (if forced to pick one runnable item):** the exact
order-β⁸ coefficient `d₈` — it is the β⁸ ACTIVATION coefficient for the
d-log-Padé predictive verdict (first falsifiable test of the complex-pair class
against exact data) AND a clean falsifier of the single-pair hypothesis (a
constant-amplitude single-pair fit to d₅,d₆,d₇ predicts `d₈ ≈ −3.26e-7`). But it
is at/past the treewidth wall (see below), so it needs technique (1) or (2)
first, and even if it lands it only ACTIVATES — it does not close β=6.

## Why β⁸ is past the wall (if anyone is tempted)

d₈ adds 56 multiplicity vectors per shell of 9-plaquette cumulants (Bell(9) =
21147 set partitions each) reaching links with even higher factor counts, and
the distinct-support side reopens at larger area (the GF(3) cycle-space weights
through p₀ resume at 10, 11, 12). Even with cycle 2's optimized engine this is
at/past the practical ceiling, and the depth a genuine resummation needs
(~15–40 coeffs) collides squarely with the retained treewidth-29 infeasibility
(`su3_wigner_l3_treewidth_infeasible_2026-05-04`, audited_conditional 2026-05-29).
The optimized contraction bought exactly one more order (β⁷), which was enough to
deliver the tadpole verdict; it does not change the asymptotic wall.

## Discipline reminders for the next agent

- Verify `effective_status` in `docs/audit/data/audit_ledger.json` before citing
  any status from these notes or from memory.
- Framework PRs land science/fixes only; `git checkout -- docs/audit/` before
  committing if the audit pipeline was run.
- No new vocabulary / tags / meta-framings; mirror existing bounded-theorem
  note templates; no bare "retained"/"promoted"; cite 0.594 only as comparator.
