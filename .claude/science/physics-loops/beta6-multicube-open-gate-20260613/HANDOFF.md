# Beta6 Multi-Cube Handoff

**Date:** 2026-06-13
**Branch:** `physics-loop/beta6-multicube-open-gate-20260613`
**Scope:** source-only open-gate unblock; no audit result or ledger edits.

## What changed

- The note now limits downstream use to the local anchors actually recomputed
  by the runner.
- The note forbids citing this packet as proof of the full order-`beta^9`
  48-support classification, the order-`beta^10` marked-face sector, beta=6
  closure, `<P>(6)`, `Delta(6)`, or sub-6 singularity exclusion.
- The runner now verifies that source-boundary firewall and reports
  `SCORECARD: PASS=13 FAIL=0`.

## Verification

```bash
python3 -m py_compile scripts/frontier_beta6_multicube_resummation_relocation.py
python3 scripts/frontier_beta6_multicube_resummation_relocation.py
python3 scripts/cached_runner_output.py scripts/frontier_beta6_multicube_resummation_relocation.py --check-only
git diff --check
```
