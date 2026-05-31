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

## CYCLE 3 — exact d₈ (beat the β⁸ wall via octahedral collapse) + single-pair verdict  [DONE]

- **Deliver:** the exact order-β⁸ connected coefficient — the cycle-2 HANDOFF
  flagged this as "past the wall" (56 multiplicity vectors/shell of 9-plaquette
  cumulants, Bell(9) = 21147). Beat it.
- **Result:** **d₈ = 5/272097792 (exact, POSITIVE)**, per-shell 5/1088391168,
  four identical shells. **d₈/d₇ = 1/16**; bracket c₃ = 5/576. The naive
  56-vector wall is BEATEN by the closed cube's octahedral O_h symmetry: the
  joint free-Haar cumulant is invariant under any face permutation, so it depends
  only on the multiset of density multiplicities (the "value shape"). The 56
  order-8 vectors collapse to **3 value-shapes** — exactly the "Münster-style
  graphical organizer" the cycle-2 checkpoint named. Shape-collapse engine:
  ~5 min single-thread. The 3 shape cumulants match the closed-form law κ₅/6ᵏ
  ((1,1,1,2,2,2) = +1/408146688, (1,1,1,1,2,3) = 0, (1,1,1,1,1,4) = −5/408146688).
- **Two-engine:** all 3 shape cumulants match the closed-form law (engine-
  independent); sympy invariant-projector tensor == Fraction link tensor at every
  order-8 per-link degree incl the busiest (4,1)/(1,4) (V7, exact); Fraction-
  engine octahedral shape-invariance self-check. Full sympy 9-plaquette
  joint_cumulant hits the ~270s/word wall (recorded offline, not gated).
- **Single-complex-pair verdict:** a constant-amplitude single dominant complex-
  conjugate pair (the d-log-Padé premise) fixed by d₅,d₆,d₇ predicts a SIGN
  CHANGE at d₈ ([0/2] bracket discriminant −67/144 < 0; predicted d₈ < 0). Exact
  d₈ = +1.84e-8 is POSITIVE → **single-complex-pair ansatz FALSIFIED** (no sign
  change). Corroborates + extends the cycle-2 tadpole falsification.
- **d-log-Padé:** d₅..d₈ ACTIVATE the [1/1] predictive test (H₀ = 7/12, H₁ =
  −1/16, H₂ = −1/54), but the [1/1] returns a spurious REAL pole (β_c ≈ 3.375)
  and a non-physical Δ(6) ≈ 1.19 (⟹ ⟨P⟩(6) ≈ 1.62, far from 0.594). The
  activation coefficient CONTRADICTS the [1/1]'s single-pole premise; [1/1] is
  too low-order to localize the physical complex pair. NOT a closure.
- **Note:** `docs/BETA6_PLAQUETTE_D8_COEFFICIENT_AND_SINGLE_PAIR_VERDICT_BOUNDED_NOTE_2026-05-30.md`.

## CHECKPOINT — the lane-killer (ρ_{p,q}(6))  [NOW ACTIVE: the next step]

- A genuine resummation closing <P>(6) would need ~15–40 exact coefficients
  (the d-log-Padé route's depth). Cycle 3 showed the octahedral collapse beats
  the naive β⁸ wall, so d₉/d₁₀ are reachable in principle — BUT d₉ is NOT pure
  cube-shell: the GF(3) certificate reopens 80 new weight-10 distinct supports at
  d₉ (new non-octahedral objects, heavier 10-plaquette integrals), so the two-tier
  collapse is special to d₆/d₇/d₈; d₉+ needs fresh new-support enumeration.
- **At the wall, STOP brute extension.** The exact-coefficient route has now
  delivered every **in-runway** verdict: tadpole/geometric **FALSIFIED** (cycle
  2), single-complex-pair **FALSIFIED** (cycle 3), and the d-log-Padé predictive
  test **ACTIVATED** by d₅..d₈ with its lowest-order [1/1] **self-contradicting**.
  All three candidate continuations the harness can test are resolved; further
  coefficients (d₉+) reopen new geometry and STILL cannot close <P>(6) (retained
  infinite-hierarchy no_go: no finite-order truncation closes the thermodynamic
  value; closest literature precedent failed past the radius even at 14–21 orders).
- Closure then requires a genuinely NEW dynamical input, e.g.: (i) extend the
  octahedral-collapse organizer to d₉/d₁₀ (the cube part is cheap; the cost is
  enumerating + integrating the new weight-10 supports) — a sharper d-log-Padé
  input only, still not a closure; (ii) a rank-aware contractor defeating the
  treewidth wall for the unmarked 3D spatial Wilson environment; (iii) an
  independent proof of the analytic-continuation class of Δ(β) on (0,6] (BOTH
  the geometric/single-pole AND the single-complex-pair classes are now
  FALSIFIED by the exact coefficients, so the surviving candidate is a
  multi-pair / richer complex singularity structure with NO real branch point at
  β_r < 6 — an unproven premise, not an in-runway computation).
- None is a brute-force extension; each is its own multi-session research item.
  **This checkpoint is where the loop hands back to /first-principles and
  /frontier work — NOT another coefficient cycle.**

## Parked / do-not-reopen

The 20 ruled-out routes + the 5 dead analytic routes are in `NO_GO_LEDGER.md`.
Do not regenerate them. The double-wall (ρ_{p,q}(6) under-determined + treewidth
infeasible) is the binding constraint; no opportunity here re-attempts it.
