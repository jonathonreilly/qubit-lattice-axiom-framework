# Handoff

This PR covers the two audited-conditional rows that had no ready PR coverage
after the latest main scan:

- `koide_taste_cube_cyclic_source_descent_note_2026-04-18`
- `wilson_corrected_v_taste_tree_level_bounded_note_2026-05-08`

Koide repair:

- Splits the exact finite `C^8` cyclic-descent theorem from the downstream
  staggered-Dirac realization gate.
- Adds runner checks that the note states the gate is not load-bearing, that
  `T_1` charged-sector language is not physical charged-lepton labeling, and
  that the abstract taste-cube toolkit is audited clean.

Wilson repair:

- Adds `WILSON_STAGGERED_MINIMAL_BLOCK_SPECTRUM_BRIDGE_NOTE_2026-06-13.md`
  and runner `frontier_wilson_staggered_minimal_block_spectrum_bridge_2026_06_13.py`.
- The bridge constructs the APBC minimal-block combined operator
  `O_n = 2r hw(n) I_2 + [[0,-2u0],[2u0,0]]`, derives `2rk +/- 2iu0` with
  `binomial(4,k)` multiplicities, and recovers the Wilson `V_taste` product.
- The existing Wilson formula note/runner now consumes that bridge.

Verification:

```bash
python3 scripts/frontier_koide_taste_cube_cyclic_source_descent.py
PYTHONPATH=scripts python3 scripts/frontier_wilson_corrected_v_taste_tree_level.py
python3 scripts/frontier_wilson_staggered_minimal_block_spectrum_bridge_2026_06_13.py
python3 scripts/precompute_audit_runners.py --allow-non-main --push-mode=none --force --concurrency=3 --runners scripts/frontier_koide_taste_cube_cyclic_source_descent.py,scripts/frontier_wilson_corrected_v_taste_tree_level.py,scripts/frontier_wilson_staggered_minimal_block_spectrum_bridge_2026_06_13.py
```

Non-claims:

- No audit ledger edits.
- No new axioms.
- No physical Koide or Higgs closure.
