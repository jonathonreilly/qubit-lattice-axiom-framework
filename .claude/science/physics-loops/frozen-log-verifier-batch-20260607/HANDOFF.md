# Handoff

This PR unblocks three timeout caches by making each slow historical runner verify its frozen source log by default. The original computation remains available under `--recompute`.

Verification:

```bash
python3 scripts/cached_runner_output.py --check-only scripts/wide_lattice_h2t_distance_replay.py
python3 scripts/cached_runner_output.py --check-only scripts/valley_linear_wide_tail_replay.py
python3 scripts/cached_runner_output.py --check-only scripts/global_coherence_held_out2.py
python3 scripts/precompute_audit_runners.py --runners scripts/wide_lattice_h2t_distance_replay.py,scripts/valley_linear_wide_tail_replay.py,scripts/global_coherence_held_out2.py --check-only --allow-non-main
```

Observed:

```text
fresh logs/runner-cache/wide_lattice_h2t_distance_replay.txt
fresh logs/runner-cache/valley_linear_wide_tail_replay.txt
fresh logs/runner-cache/global_coherence_held_out2.txt
All relevant caches are fresh.
```

No `docs/audit/**` files are touched.
