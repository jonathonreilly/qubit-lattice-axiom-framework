# Handoff

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3014

## What Changed

This block repairs the latest finite-volume Lieb-Robinson audit blocker by replacing the exclusive interaction-graph degree with the inclusive overlap degree `D_I^+`. The theorem constants now use:

```text
lambda = 2 J D_I^+ |t|
v_LR = 2 e J D_I^+ R_0
```

The runner now includes `V9`, an explicit repeated-chain guard:

- minimal two-term graph: exclusive bound fails (`2 > 1`);
- inclusive bound holds (`2 <= 4`);
- 1D bond graph repeated-chain counts are bounded by `D_I^+`.

## Verification

- `PYTHONPATH=scripts python3 -m py_compile scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py`
- `PYTHONPATH=scripts python3 scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py`

## Remaining Blockers

This only repairs the LR commutator-bound proof. Static spatial cluster decomposition still needs a retained finite-volume filter/gap bridge. No audit ledger files were changed.
