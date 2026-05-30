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

## CYCLE 2 — run harness #2255 to a tadpole verdict + d-log-Padé forward test

- **Run** `scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py` with
  `EXACT_HIGHER = {6: Fraction(7, 5668704)}` (and d₇ once exact). The tadpole/
  geometric ansatz predicts d₇ from {d₅,d₆}: ρ = d₆/d₅ = 7/12, so predicted
  d₇ = (7/12)·d₆. Drop in the exact d₇ → read the SUPPORT/FALSIFY line. This
  is the cheapest decisive falsifier of the one not-yet-blocked analytic route.
- **d-log-Padé:** its PREDICTIVE verdict needs {d₅..d₈} (= β⁸, at/past the
  wall); only its FORWARD <P>(6) sensitivity test is in-runway now.
- **Deliver:** a bounded note recording the tadpole predictive verdict (the
  exact d₇ either is or is not within the harness's 5% support window of the
  geometric prediction) + the forward <P>(6) band. Audit-shippable either way.

## CHECKPOINT — the treewidth-29 wall

- A genuine resummation closing <P>(6) would need ~15–40 exact coefficients
  (the d-log-Padé route's depth). The exact connected-coefficient engine grows
  ~μⁿ (μ≈8) in cluster count, and each high-multiplicity / large-area cluster's
  exact SU(3) Haar integral is a per-link 3^(2k) contraction (the same
  treewidth-flavored barrier as the L_s≥3 contraction). β⁷–β⁸ is the practical
  ceiling.
- **At the wall, STOP brute extension.** Closure then requires a genuinely NEW
  dynamical input, e.g.: (i) a Münster-style graphical strong-coupling organizer
  that sums connected SU(3) contributions analytically rather than by brute
  cluster enumeration + 3nj contraction; (ii) a rank-aware contractor defeating
  the treewidth wall; (iii) an independent proof that Δ(β) is real-analytic on
  (0,6] with a complex-pair dominant singularity (no real branch point at
  β_r < 6) — the analyticity premise the d-log-Padé route rests on.
- None is a brute-force extension; each is its own multi-session research item.
  This checkpoint is where the loop hands back to first-principles work.

## Parked / do-not-reopen

The 20 ruled-out routes + the 5 dead analytic routes are in `NO_GO_LEDGER.md`.
Do not regenerate them. The double-wall (ρ_{p,q}(6) under-determined + treewidth
infeasible) is the binding constraint; no opportunity here re-attempts it.
