# Summary

Repairs the `single_axiom_hilbert_note` source/runner drift flagged by the
audit backlog.

- Demotes the runner synthesis from stale "single axiom reduction" language to
  admitted-input bounded operational support.
- Updates Test 4 language: the fixed output reports `Locality gradient (near >
  far): False`, so the valid support is the spread/localization contrast only,
  not monotone graph-distance decay.
- Refreshes `logs/runner-cache/frontier_single_axiom_hilbert.txt`.

# Claim Boundary

This is source-side repair only. It does not audit, retag, land to main, or
update generated audit/status surfaces.

Current-surface status proposed in branch-local artifacts: `bounded-support`.
Independent review/audit owns any effective-status movement.

# Checks

```bash
python3 scripts/frontier_single_axiom_hilbert.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_single_axiom_hilbert.py
```

Both pass.
