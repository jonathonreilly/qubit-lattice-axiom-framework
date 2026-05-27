# Handoff

## Summary

This PR repairs the EW OZI row by narrowing it to the bounded disconnected
size-class family already compatible with the retained matching-rule no-go.

## Claim Movement

- Before: the row suggested the physical EW readout uses the connected trace
  up to OZI corrections and treated `9/8` as the canonical package readout.
- After: the row states the exact family
  `K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9)` and leaves `kappa_EW` open.
- Remaining: a separate selector theorem, disconnected-current computation, or
  reviewed convention is required before `kappa_EW = 0` can be used as more
  than a specialization.

## Verification

- `python3 scripts/frontier_ew_current_ozi_scope_repair.py`
- `python3 scripts/vocab_lint.py --report-only docs/EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md .claude/science/physics-loops/ew-ozi-scope-repair-20260527/*.md`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`

## Next Action

Open as a draft PR. If review accepts the scope repair, independent audit can
re-audit the row as bounded support rather than a conditional physical-selector
claim.
