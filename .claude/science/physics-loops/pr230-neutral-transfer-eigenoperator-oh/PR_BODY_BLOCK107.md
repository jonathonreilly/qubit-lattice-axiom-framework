### Block107 checkpoint: source-Higgs time-kernel manifest idle refresh

Refreshed the source-Higgs time-kernel production manifest after the final
chunk workers completed.  The certificate now records `active_process_rows=[]`
and removes the stale "wait for active static chunks" blocker.

What changed:

- `scripts/frontier_yt_pr230_source_higgs_time_kernel_production_manifest.py`
  now emits state-dependent worker/collision text.
- `outputs/yt_pr230_source_higgs_time_kernel_production_manifest_2026-05-07.json`
  records no active workers.
- Added
  `docs/YT_PR230_BLOCK107_TIME_KERNEL_MANIFEST_IDLE_REFRESH_NOTE_2026-05-17.md`
  and refreshed the loop pack.

Validation:

```text
python3 -m py_compile scripts/frontier_yt_pr230_source_higgs_time_kernel_production_manifest.py
python3 scripts/frontier_yt_pr230_source_higgs_time_kernel_production_manifest.py
# SUMMARY: PASS=16 FAIL=0
python3 scripts/frontier_yt_fh_lsz_target_timeseries_full_set_checkpoint.py
# SUMMARY: PASS=9 FAIL=0
python3 scripts/frontier_yt_pr230_schur_higher_shell_wave_launcher.py
# SUMMARY: PASS=11 FAIL=0; active_chunks=[]
python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
# SUMMARY: PASS=427 FAIL=0
python3 docs/audit/scripts/audit_lint.py --strict
# OK: no errors
```

Current replacement/chunk status:

- FH-LSZ target-timeseries packet is complete: 63/63 chunks, replacement queue
  empty, seed control preserved as `numba_gauge_seed_v1`.
- Higher-shell chunk063 checkpoint is complete and the higher-shell wave
  launcher reports no active workers.

Claim boundary:

- no time-kernel rows were launched;
- `support_launch_authorized_now=false`;
- `closure_launch_authorized_now=false`;
- canonical `O_H` or equivalent physical neutral identity remains absent;
- no retained or `proposed_retained` top-Yukawa closure is claimed.
