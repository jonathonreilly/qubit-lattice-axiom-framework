# Handoff

## Summary

This branch repairs the alpha_s derived narrow row by removing the stale
EW-color-projection CMT dependency and citing the retained
tadpole-improvement algebra theorem instead.

## Verification

- `python3 scripts/frontier_alpha_s_derived_narrow_retained_algebra_repair.py`
  - `SUMMARY: PASS=15 FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete
- `git diff --check`
  - clean

## Pipeline Result

- Target row: `unaudited`, `positive_theorem`, ready for audit.
- Direct dependency: `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`
  (`retained` on current main).
- Runner: `scripts/frontier_alpha_s_derived_narrow_retained_algebra_repair.py`.

## Residuals

- Broad `ALPHA_S_DERIVED_NOTE.md` remains unaudited/open for its numerical and
  running surfaces.
- No plaquette, CMT, n_link, or SM-readout claim is promoted here.

## PR

PR URL: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2092
