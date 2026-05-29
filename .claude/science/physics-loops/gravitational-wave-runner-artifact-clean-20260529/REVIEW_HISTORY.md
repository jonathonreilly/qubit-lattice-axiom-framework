# Review History

Local checks:

```text
python3 -m py_compile scripts/frontier_grav_wave_post_newtonian.py
PYTHONPATH=scripts python3 scripts/frontier_grav_wave_post_newtonian.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_grav_wave_post_newtonian.py --force --push-mode none --allow-non-main --concurrency 1
bash docs/audit/scripts/run_pipeline.sh
```

Pipeline result: `gravitational_wave_probe_note` reset to `unaudited`,
`effective_status: unaudited`, `ready: true`.
