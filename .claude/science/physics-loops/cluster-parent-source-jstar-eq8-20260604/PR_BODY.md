## Summary

Direct parent-source repair for
`axiom_first_cluster_decomposition_theorem_note_2026-04-29`.

This PR addresses the live source blockers without touching
`docs/audit/**`:

- replaces the old LR velocity constant
  `v_LR = 2 e J R_int Z_lat` with the conservative finite-range
  constant `v_LR = 2 e J_* R_int D_int`;
- defines `J_* = max_z sum_{X contains z} ||h_X||` and the interaction
  adjacency degree `D_int`;
- removes the false parent equation (8) imaginary-time commutator
  identity as a route to connected-correlator clustering;
- keeps L2 explicitly conditional on retained transfer-gap or spatial
  slab clustering authority;
- updates the parent runner and cache to report the corrected `J_*`
  surface and adds an E5 `J <= J_*` exhibit.

## Handoff

See
`.claude/science/physics-loops/cluster-parent-source-jstar-eq8-20260604/HANDOFF.md`.

## Claim Status

`proposed_promoted` source repair only. This PR does not assert an
effective audit status, does not mark the row retained, and does not
modify audit results. Independent audit remains required before any
status change.

## Verification

```bash
python3 -m py_compile scripts/axiom_first_cluster_decomposition_check.py scripts/frontier_cluster_decomposition_parent_eq8_repair_narrow_verifier.py
python3 scripts/axiom_first_cluster_decomposition_check.py
python3 scripts/frontier_cluster_decomposition_parent_eq8_repair_narrow_verifier.py
python3 scripts/cached_runner_output.py --refresh scripts/axiom_first_cluster_decomposition_check.py
git diff --check
git diff --name-only | rg '^docs/audit/' || true
```

Observed:

- parent runner PASS=5/5;
- companion verifier PASS=27/27;
- no audit-ledger files touched.
