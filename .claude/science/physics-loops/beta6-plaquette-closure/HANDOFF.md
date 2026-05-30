# Handoff — β=6 Plaquette Closure Loop

## Where this loop stands (after cycle 2, 2026-05-30)

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

## Resumable next action (CYCLE 3) — CHECKPOINT at the wall

**Do NOT run another coefficient cycle.** The exact-coefficient route has
delivered its decisive in-runway verdict:

- tadpole/geometric ansatz **FALSIFIED** (cycle 2, above);
- d-log-Padé **predictive** test is **out of runway** (it needs {d₅..d₈} = β⁸,
  and β⁸ is at/past the treewidth-29 wall — see below).

So both candidate analytic continuations the harness can test are resolved as
far as exact coefficients can resolve them. β=6 closure now requires a genuinely
NEW dynamical input for ρ_{p,q}(6), which is a `/first-principles` / `/frontier`
research item, NOT a brute extension. Candidate directions (each its own
multi-session item, none a coefficient cycle):

1. **A Münster-style graphical strong-coupling organizer** that sums connected
   SU(3) contributions analytically (avoiding brute cluster enumeration + 3nj
   contraction). This could in principle reach the resummation depth the d-log-
   Padé route needs, but it is a new analytic technique, not an extension of
   this engine.
2. **A rank-aware / tree-decomposition contractor** that defeats the treewidth-29
   wall for the unmarked 3D spatial Wilson environment (the doubly-walled object).
3. **An independent proof of the analytic-continuation class of Δ(β) on (0,6].**
   The geometric/single-pole class is now FALSIFIED, so the surviving hypothesis
   is a complex-pair dominant singularity with no real branch point at β_r < 6.
   If proven, even a short exact series could be d-log-Padé-continued; but the
   analyticity is the unproven premise, not a computation.

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
