# Handoff — β=6 Plaquette Closure Loop

## Where this loop stands (after cycle 3, 2026-05-30)

- **d₆ = 7/5668704 (cycle 1), d₇ = 5/17006112 (cycle 2), and d₈ = 5/272097792
  (cycle 3) computed EXACTLY**, shipped as bounded notes + audit-companion
  runner. Reproduce the retained anchor d₅ = 1/472392. Per-shell d₈ =
  5/1088391168 (four identical shells). Per-order ratios:
  **d₆/d₅ = 7/12, d₇/d₆ = 5/21, d₈/d₇ = 1/16 — decreasing super-geometrically.**
- **The cycle-2 "d₈ is past the wall" checkpoint was WRONG; cycle 3 BEAT it.**
  d₈'s per-shell sum is 56 multiplicity vectors of 9-plaquette cumulants
  (Bell(9) = 21147 set partitions each). But the closed cube has octahedral
  automorphism group O_h (order 48); the joint free-Haar cumulant is invariant
  under any face permutation, so it depends only on the multiset of density
  multiplicities (the "value shape"). At order 8 the 56 vectors collapse to
  exactly **3 value-shapes**, so the 56 distinct 9-plaquette cumulants reduce to
  3 evaluations. The shape-collapse engine computes d₈ in **~5 min single-thread**
  — exactly the "Münster-style graphical organizer" the cycle-2 HANDOFF named as
  the way past the wall (the octahedral symmetry IS that analytic organizer).
- **Single-complex-pair ansatz FALSIFIED (cycle 3).** A constant-amplitude single
  dominant complex-conjugate pair (the d-log-Padé premise) fixed by d₅,d₆,d₇
  predicts a SIGN CHANGE at d₈ (the [0/2] bracket discriminant 4c₂−3c₁² =
  −67/144 < 0 → complex pair; predicted d₈ < 0, ≈ −7.7e-8 by the [0/2]
  recurrence, ≈ −3.26e-7 by a pure-oscillation fit). The exact d₈ = +1.84e-8 is
  **POSITIVE** (no sign change) → the series is NOT controlled by a single
  dominant complex pair. This independently corroborates + extends the cycle-2
  tadpole falsification.
- **d-log-Padé ACTIVATED but self-contradicting at [1/1].** d₅..d₈ are the four
  contiguous coefficients (= the β⁸ rank floor): H = (log h)′ now has H₀ = 7/12,
  H₁ = −1/16, H₂ = −1/54. The [1/1] d-log-Padé returns a spurious REAL pole
  (β_c ≈ 3.375) and a non-physical Δ(6) ≈ 1.19 (⟹ ⟨P⟩(6) ≈ 1.62, far from the
  0.594 comparator). So the activation coefficient d₈ contradicts the [1/1]'s
  own single-pole premise; the [1/1] is far too low-order to localize the
  physical complex pair. **This ACTIVATES the test; it does NOT close β=6.**
- **Engine (single self-contained artifact):**
  `scripts/frontier_beta6_connected_coefficient_2026_05_30.py` — sympy reference
  engine (V0–V4), optimized Fraction engine (V4b, V5/V5b for d₇), and the
  shape-collapse engine (V7/V7b/V7c for d₈). Run with `maxorder=8`. New helpers:
  `support_contrib_frac_shapecollapse` (self-validating octahedral collapse),
  `joint_cumulant_shape_sympy` (offline sympy 9-plaquette cross-check).

## Two-engine status (honest)

- d₅, d₆: Fraction == sympy EXACTLY (V4b).
- d₇: Fraction engine; sympy reproduces moments through 8-plaquette words.
- d₈: (a) all 3 shape cumulants match the closed-form law κ₅/6ᵏ (engine-
  independent); (b) sympy invariant-projector tensor == Fraction link tensor at
  every order-8 per-link degree incl the busiest (4,1)/(1,4) (V7, ~2s, exact);
  (c) Fraction-engine shape-invariance self-check. A full sympy joint_cumulant
  on a 9-plaquette word hits the documented ~270 s/word wall (worse at 9 plaq);
  it is exposed behind a `deep` flag (`python3 ... 8 deep`) as the one-time
  publication-grade 9-plaquette confirmation, **not gated in the default run**.
  The Möbius cumulant assembly is identical set-partition combinatorics in both
  engines (validated at order ≤ 6); the order-8 novelty is the link integrals,
  validated exactly at the per-link level.

## Resumable next action (CYCLE 4) — still a CHECKPOINT at the lane-killer

**The exact-coefficient route has now delivered every in-runway verdict it can:**
- tadpole/geometric ansatz **FALSIFIED** (cycle 2);
- single-complex-pair ansatz **FALSIFIED** (cycle 3);
- d-log-Padé predictive test **ACTIVATED** by d₅..d₈, and its lowest-order [1/1]
  **self-contradicts** (spurious real pole, garbage Δ(6)).

So all three candidate analytic continuations the harness can test are now
resolved. d₈ proved the shape-collapse engine can push past the naive wall, so a
few more orders (d₉, d₁₀) ARE in principle reachable — BUT:

1. **d₉ is NOT pure cube-shell.** The GF(3) cycle-space certificate shows 80 new
   weight-10 distinct supports reopen at d₉; these are new non-octahedral
   geometric objects (no ÷4 collapse), with heavier 10-plaquette integrals.
   d₉/d₁₀ need a fresh enumeration + integration of the new support class on top
   of the cube's order-9 multiplicity. The two-tier octahedral collapse is
   special to d₆/d₇/d₈ (the regime where dₙ is purely the 4 cube shells).
2. **More coefficients still do NOT close β=6.** Per the retained no_go
   (`gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note`), no
   finite-order truncation closes thermodynamic ⟨P⟩(6); and the closest
   literature precedent (2D O(N), arXiv:hep-lat/9602011) failed past the
   convergence radius even at 14–21 orders. Closing ⟨P⟩(6) still requires a
   genuinely NEW dynamical input for ρ_{p,q}(6) (under-determined by local data
   + treewidth-29 infeasible at L_s ≥ 3), NOT another brute coefficient.

Candidate directions (each its own research item, none a pure coefficient cycle):

- **d₉ via shape-collapse + new-support enumeration** (the cube part is cheap;
  the new weight-10 supports are the cost). Useful only as a sharper d-log-Padé
  input — still cannot close β=6, and the [2/2] would need d₅..d₁₂.
- **A rank-aware / tree-decomposition contractor** that defeats the treewidth-29
  wall for the unmarked 3D spatial Wilson environment (the doubly-walled object).
- **An independent proof of the analytic-continuation class of Δ(β) on (0,6].**
  Both the geometric/single-pole AND the single-complex-pair classes are now
  falsified by the exact coefficients; the surviving hypothesis is a multi-pair
  / richer complex singularity structure with no real branch point at β_r < 6.

## Discipline reminders for the next agent

- Verify `effective_status` in `docs/audit/data/audit_ledger.json` before citing
  any status from these notes or from memory.
- Framework PRs land science/fixes only; `git checkout -- docs/audit/` before
  committing if the audit pipeline was run.
- No new vocabulary / tags / meta-framings; mirror existing bounded-theorem
  note templates; no bare "retained"/"promoted"; cite 0.594 only as comparator.
- The single-pair PREDICTED magnitude is fit-convention-dependent (−3.26e-7,
  −7.7e-8 across conventions); the robust falsifiable feature is the SIGN CHANGE
  to negative, which the exact POSITIVE d₈ falsifies regardless of magnitude.
