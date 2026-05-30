# β=6 Plaquette Closure — Opportunity Queue

Finite-runway plan. Each cycle is a self-contained, audit-shippable increment
on retained primitives. None claims β=6 closure. The runway ends at the
treewidth-29 wall, after which closure needs a genuinely new dynamical input.

## CYCLE 1 — exact order-β⁶ (+β⁷ if reached) connected coefficient  [THIS PR]

- **Deliver:** exact d₆ of Δ(β) = P_full − P_1plaq, via the extended
  mixed-cumulant connected-cluster enumeration with exact SU(3) single-link
  Haar integrals. Attempt d₇.
- **Result:** d₆ = 7/5668704 (exact). Per-shell d₆ = 7/(12·18⁵); per-shell
  ratio d₆/d₅ = 7/12. Finite-geometry finding: zero order-β⁶ distinct supports
  are GF(3)-closable, so d₆ comes only from the four cube shells via order-6
  multiplicity.
- **Feeds:** activates the **tadpole/geometric** predictive verdict in harness
  #2255 (`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`):
  {d₅,d₆} predicts d₇ = (d₆/d₅)·d₆. Exact d₇ then SUPPORT/FALSIFY-tests it.
- **Status:** d₆ shipped exact. d₇: see HANDOFF (cluster-contraction cost).

## CYCLE 2 — exact d₇ (beat the contraction wall) + tadpole verdict  [DONE]

- **Deliver:** exact order-β⁷ connected coefficient via an optimized contraction
  that beats the prior cycle's 3^(2k) wall, then run harness #2255 to the tadpole
  SUPPORT/FALSIFY verdict.
- **Result:** **d₇ = 5/17006112 (exact)**, per-shell 5/68024448, four identical
  shells. **d₇/d₆ = 5/21**, which ≠ d₆/d₅ = 7/12 — the per-order ratio is NOT
  constant. **Optimized engine** (sparse invariant-basis link integral + Fraction
  arithmetic + variable-elimination + unbalanced-link pruning) drops the worst
  8-plaquette moment from ~270s to ~0.5s; exact d₇ in ~2min. **Two-engine
  agreement** (Fraction reproduces sympy d₅, d₆ exactly + sampled moments to
  size 8).
- **Verdict:** harness #2255 with `EXACT_HIGHER = {6: 7/5668704, 7: 5/17006112}`
  reads **`[FALSIFY] tadpole/geometric`** (predicted (7/12)·d₆ = 49/68024448
  misses exact d₇ by ~59%; rel 1.45 >> 5% window). The resummation route does
  NOT reduce to a geometric tail; no closed boosting form supported. Forward
  truncation `<P>(6)_trunc ≈ 0.5789` (gap 0.0151 to comparator) is a truncated
  partial sum, NOT a closure.
- **d-log-Padé:** PREDICTIVE verdict needs {d₅..d₈} (= β⁸, at/past wall) — out of
  runway. Only its forward sensitivity test ran.
- **Note:** `docs/BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`.

## CHECKPOINT — the treewidth-29 wall  [NOW ACTIVE: the next step]

- A genuine resummation closing <P>(6) would need ~15–40 exact coefficients
  (the d-log-Padé route's depth). The exact connected-coefficient engine grows
  ~μⁿ (μ≈8) in cluster count, and each high-multiplicity / large-area cluster's
  exact SU(3) Haar integral is a per-link 3^(2k) contraction (the same
  treewidth-flavored barrier as the L_s≥3 contraction). β⁷–β⁸ is the practical
  ceiling.
- **At the wall, STOP brute extension.** The exact-coefficient route has now
  delivered its decisive **in-runway** verdict: the tadpole/geometric ansatz is
  **FALSIFIED** (d₇/d₆ = 5/21 ≠ 7/12; cycle 2), and the d-log-Padé predictive
  test is **out of runway** (needs β⁸, past the wall). So both of the harness's
  candidate continuations are resolved as far as exact coefficients can resolve
  them; further coefficients (β⁸+) hit the treewidth-29 wall.
- Closure then requires a genuinely NEW dynamical input, e.g.: (i) a Münster-style
  graphical strong-coupling organizer that sums connected SU(3) contributions
  analytically rather than by brute cluster enumeration + 3nj contraction;
  (ii) a rank-aware contractor defeating the treewidth wall; (iii) an independent
  proof of the analytic-continuation class of Δ(β) on (0,6] (the geometric/single-
  pole class is now FALSIFIED, so the surviving candidate is a complex-pair
  dominant singularity with NO real branch point at β_r < 6 — but that is an
  unproven premise, not an in-runway computation).
- None is a brute-force extension; each is its own multi-session research item.
  **This checkpoint is where the loop hands back to /first-principles and
  /frontier work — NOT another coefficient cycle.**

## Parked / do-not-reopen

The 20 ruled-out routes + the 5 dead analytic routes are in `NO_GO_LEDGER.md`.
Do not regenerate them. The double-wall (ρ_{p,q}(6) under-determined + treewidth
infeasible) is the binding constraint; no opportunity here re-attempts it.
