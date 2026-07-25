# Artifact Plan — audit-unlock-toe-20260724

Per-block artifact contract (lane B): exactly one source-only triple per unit —

1. one note in `docs/` (bounded_theorem class, honest Boundary section,
   geometric-labels disclaimer where CP/chirality vocabulary appears, exactly
   the intended markdown-link dependency edges, no grade authorship);
2. one paired class-A runner in `scripts/` printing `TOTAL: PASS=N FAIL=0`
   (platform-stable prints: bounded statements for noise-scale floats, 3 sig
   digits for structural floats, integers for ranks/dims; discriminating
   gates — wrong-value rejectors, never construction-tautologies);
3. one cache in `logs/runner-cache/` (regenerated via `scripts/runner_cache.py`
   at review time).

Branch naming: `physics-loop/<slug>-blockNN-YYYYMMDD` (KCPT lane retains its
established `kcpt-*` branch names for chain continuity). All branches off
fresh `origin/main`, from dedicated worktrees.

## In-flight artifacts

- **Block 1 (= KCPT Unit 20):** note
  `docs/KCPT_DIRAC_SYMMETRY_ALGEBRA_BICOMMUTANT_DIMENSION_992_BOUNDED_THEOREM_NOTE_2026-07-24.md`
  + runner `scripts/kcpt_dirac_symmetry_algebra_bicommutant_dimension_992_2026_07_24.py`
  (PASS=26) + cache. Status: planner review clean; adversarial-verification
  pass in flight; lands on clean synthesis.

## Planned artifacts (design order per OPPORTUNITY_QUEUE)

- **Block 2 (= KCPT Unit 21):** obligation-facing continuation on the landed
  U19/U20 surface; exact object chosen after U20 lands (candidates in
  ROUTE_PORTFOLIO B-R2).
- **Block 3 (candidate):** unit-singlet physical-consumer projection repair
  (fix-class triple per the audit-unlock fix-class pattern).

## Weaving

No science results are woven through README, LANE_REGISTRY.yaml,
LANE_STATUS_BOARD.md, or publication matrices from this campaign; any proposed
weaving is recorded in HANDOFF.md for a dedicated pass.

## Forbidden outputs (science branches)

`docs/audit/data/` (anything), `docs/audit/AUDIT_LEDGER.md`, `AUDIT_QUEUE.md`,
`MISSING_DERIVATION_PROMPTS.md`, `docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md`,
`PUBLICATION_AUDIT_DIVERGENCE.md`.
