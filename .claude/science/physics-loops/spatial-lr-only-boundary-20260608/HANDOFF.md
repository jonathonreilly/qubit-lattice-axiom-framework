# Handoff

Branch: `physics-loop/spatial-lr-only-boundary-20260608`

Target claim:
`spatial_cluster_decomposition_lieb_robinson_real_note_2026-05-19`

What changed:

- Re-scoped the source note to the finite-volume Lieb-Robinson theorem only.
- Marked the cluster-decomposition route as non-load-bearing support.
- Left the parent cluster row explicitly open pending a retained filter theorem
  and gap input.
- Did not change the runner or audit ledger.

Verification:

```text
python3 scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py
fresh logs/runner-cache/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.txt
```

Remaining boundary:

No cluster-decomposition theorem, thermodynamic-limit theorem, mass-gap theorem,
or continuum result is claimed.
