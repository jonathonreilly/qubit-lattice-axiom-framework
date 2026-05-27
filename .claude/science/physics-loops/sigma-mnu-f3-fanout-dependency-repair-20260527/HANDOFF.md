# Handoff

## What Moved

The Sigma F3 stuck-fanout row now has a visible dependency packet and a
companion runner that verifies the packet plus the decisive cross-bound
arithmetic.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_sigma_mnu_f3_stuck_fanout_dependency_repair.py`
  - `TOTAL: PASS=40, FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/SIGMA_MNU_F3_STUCK_FANOUT_SYNTHESIS_NOTE_2026-04-28.md scripts/frontier_sigma_mnu_f3_stuck_fanout_dependency_repair.py`
  - clean
- `git diff --check`
  - clean
- `bash docs/audit/scripts/run_pipeline.sh`
  - target row reset to `unaudited`, `claim_type=no_go`, no open dependency paths

## Remaining Blockers

Numerical `Sigma m_nu` retention still requires new science outside this
dependency-edge repair.

## PR

Draft PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2115
