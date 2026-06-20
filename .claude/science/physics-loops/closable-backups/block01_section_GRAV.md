# block01 section GRAV — gravity generator-shift eikonal bridge

**Date:** 2026-06-20
**Lane:** closable-backups block01
**Outcome:** partial / named-premise (NOT a clean bounded_theorem closure)

## Target row (located)

- claim_id: `gravity_premise4_refractive_index_from_dispersion_bounded_theorem_note_2026-06-07`
- status: `audited_conditional`, `chain_closes=false`, leaf
- deps: `self_consistency_forces_poisson_note`,
  `lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07`,
  `gravity_clean_derivation_note`
- open residual (MISSING_DERIVATION_PROMPTS ~L3502 + missing_derivation_difficulty.json):
  `missing_bridge_theorem: add a retained one-hop derivation of H->H+phi and the
  WKB/Fermat identification n=k/k0 ...`

## What was attempted

Derive the additive scalar generator shift `H_s = H_0 + s*I` (sign +,
normalization coefficient exactly 1) from the weak-field action/propagator
surface — the upstream `H -> H + phi` half of the blocker. The downstream
phase-count algebra `n = k_s/k0` is already closed in the premise4 note (scoped
as such by the orchestrator).

## Result

Runner `scripts/gravity_generator_shift_bridge_2026_06_20.py`
(cache `logs/runner-cache/gravity_generator_shift_bridge_2026_06_20.txt`):
`TOTAL: PASS=14 FAIL=0`. Recomputed in-tree:

- (A) retained `H_0 = -Delta_lat` (sym, PSD, 1 zero mode);
- (B) symmetric Lie-Trotter step `exp(-dtau V/2)exp(-dtau H_0)exp(-dtau V/2)`
  has generator `H_0 + V + O(dtau^2)`; coefficient on V is exactly 1 (c=1.00006),
  residual O(dtau^2) (ratio 3.97);
- (C) uniform shift `s*I` moves spectrum by exactly +s (1e-14); sign +; control
  c=2 rejected;
- (D) normalization forced by retained action weight `exp(-dtau s)`: c=1 matches,
  c=0.5 fails;
- (E) `(H_0+sI)` fixed-energy reading reproduces premise4 axis map
  `k(phi)=arccos(1-(E-phi)/2)`, `n=1-phi/(2E)`, slope -1/(2E) numerically
  confirmed (-25.04 vs -25.0 at E=0.02).

## Honest call (promotion value gate)

NOT promoted to a clean bounded_theorem row:

1. The operator-shift sub-step is **standard-math completion** of an already-
   retained action coupling (textbook discrete-time path-integral <-> transfer-
   matrix). The audit lane could complete it from retained primitives + standard
   math, so the gate forbids claiming it as new derivational content. The
   legitimate contribution is the in-tree recomputation fixing sign + norm.
2. The **WKB/Fermat `n=k/k0`** half of the blocker remains a genuinely admitted
   geometric-optics premise, not closable by standard algebra over the retained
   primitives. It stays the load-bearing open residual.

Net: upstream half moves from "supplied stipulation" to "recomputed-in-tree from
retained coupling (sign +, norm 1)"; downstream half remains a named premise.
Parent row stays audited_conditional / chain_closes=false. No new axiom/primitive.

## Deliverables

- note: `docs/GRAVITY_GENERATOR_SHIFT_BRIDGE_CLOSURE_NOTE_2026-06-20.md`
- runner: `scripts/gravity_generator_shift_bridge_2026_06_20.py`
- cache: `logs/runner-cache/gravity_generator_shift_bridge_2026_06_20.txt`
