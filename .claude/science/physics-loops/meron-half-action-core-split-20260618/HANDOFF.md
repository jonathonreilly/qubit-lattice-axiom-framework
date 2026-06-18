# Handoff

Branch: `codex/meron-half-action-core-split-20260618`
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4386

This source-side PR repairs the latest conditional audit result for `meron_half_instanton_4pi2_over_g2_external_narrow_theorem_note_2026-05-16` by splitting the closed half-action algebra core from the still-open boundary construction.

Verification:

- `PYTHONPATH=scripts python3 scripts/meron_half_action_core_split_2026_06_18.py`
  - `TOTAL: PASS=19 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.py`
  - `TOTAL: PASS=32 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/meron_half_action_core_split_2026_06_18.py`
  - cache status `ok`
  - runner sha `7cc21632493672c0b378a80b1724f7c6686976618d5d9c8a10b311ec09df402b`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.py`
  - cache status `ok`
  - runner sha `7e9ee6a6f94664a1161843eeac83f26d265c7b1ca9052ed23cf274baa1348167`

Forbidden-surface expectation: no audit ledger, queue, publication, repo status, lane registry, or active review queue files should be changed by this branch.

Next action: reviewer may run review-loop and landing cleanup. If accepted, independent audit can decide whether the bounded-support core changes the parent conditional row.
