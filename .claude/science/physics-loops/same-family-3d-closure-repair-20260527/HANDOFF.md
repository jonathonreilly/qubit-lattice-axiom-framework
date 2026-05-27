# Same-Family 3D Closure Repair Handoff

Target row: `same_family_3d_closure_note`

PR purpose: queue the row for independent re-audit after replacing the former
print-only wrapper with a live finite-lattice certificate.

What changed:

- `scripts/same_family_3d_closure.py` now recomputes rows 1-7 at
  `h=0.25`, `W=10`, `L=12`.
- The same runner now recomputes rows 8-9 at the same `h=0.25`, `W=10`
  slice for `L=8,10,12`.
- The runner recomputes the core `W=10` distance tail and cites the retained
  `VALLEY_LINEAR_WIDE_TAIL_NOTE.md` packet for the `W=12` companion.
- `docs/SAME_FAMILY_3D_CLOSURE_NOTE.md` now exposes retained dependencies on
  `VALLEY_LINEAR_ACTION_NOTE.md`, `VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md`,
  and `VALLEY_LINEAR_WIDE_TAIL_NOTE.md`.

Verification:

```text
python3 scripts/same_family_3d_closure.py
python3 scripts/precompute_audit_runners.py --runners scripts/same_family_3d_closure.py --force --allow-non-main --push-mode none
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

Observed runner result:

```text
PASS=11 FAIL=0
Total time: 118s
```

Generated audit state:

```text
audit_status=unaudited
effective_status=unaudited
ready=true
deps=[valley_linear_wide_tail_note, valley_linear_action_note, valley_linear_asymptotic_bridge_note]
helper_runner_paths=[scripts/lattice_3d_valley_linear_card.py]
```

Reviewer boundary: this PR does not claim retained status. It queues a
bounded-theorem packet for audit and keeps the scope finite-lattice only.
