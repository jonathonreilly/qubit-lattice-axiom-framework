## Summary

Repairs `audited_symmetry_synthesis_note` by converting the remaining
rank-1/CLT and sector-preservation mechanism language into explicit
non-binding interpretation. The binding claim is now only the finite-surface
synthesis over the already retained-bounded one-hop authorities.

## Trace Gate

- Trace class: `direct_blocker_closure`
- Audit blocker: mark rank-1/CLT and sector-preservation mechanism language as
  non-binding, or provide a retained mechanism theorem.
- Repair path: mechanism firewall plus rewritten synthesis bullets using
  finite-window diagnostic language.

## Verification

- `python3 scripts/frontier_audited_symmetry_synthesis_scope_repair.py`
  - `SUMMARY: PASS=20 FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/AUDITED_SYMMETRY_SYNTHESIS_NOTE.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete
- `git diff --check`
  - clean

## Boundaries

- Does not add a rank-1/CLT theorem.
- Does not add a sector-preservation family theorem.
- Does not promote asymptotic or unified grown-lane claims.
- No new axioms.
