## Physics-loop PR230 Block127

This stacked block wires the Block126 matched top-side packet into the W/Z
mass-fit response-row builder without weakening the W/Z strict-output gates.

Artifacts:

- Note: `docs/YT_PR230_BLOCK127_WZ_BUILDER_BLOCK126_TOP_PACKET_ADAPTER_NOTE_2026-05-17.md`
- Builder: `scripts/frontier_yt_wz_mass_fit_response_row_builder.py`
- Runner: `scripts/frontier_yt_pr230_block127_wz_builder_block126_top_packet_adapter.py`
- Certificate: `outputs/yt_pr230_block127_wz_builder_block126_top_packet_adapter_2026-05-17.json`
- Loop pack: `.claude/science/physics-loops/pr230-retained-closure-campaign-20260517/`

Result:

- W/Z builder now defaults to the Block126 top-side packet.
- The packet is recognized as complete top-side support: 1008 matched tau1
  rows, 23 complete tau slices, selected mass `0.75`, and preserved
  `numba_gauge_seed_v1` metadata.
- Strict W/Z output is still refused.
- No strict measurement rows are written.

Claim boundary:

This is bounded support only.  It does not supply same-source W/Z rows,
matched top-W/Z covariance, strict non-observed `g2`, accepted same-source
EW/Higgs action, or canonical-Higgs/source-overlap authority.  No retained or
`proposed_retained` closure is claimed.

Validation:

```sh
python3 scripts/frontier_yt_wz_mass_fit_response_row_builder.py
python3 scripts/frontier_yt_wz_mass_fit_response_row_builder.py --scout
python3 -m py_compile scripts/frontier_yt_wz_mass_fit_response_row_builder.py scripts/frontier_yt_pr230_block127_wz_builder_block126_top_packet_adapter.py scripts/frontier_yt_pr230_campaign_status_certificate.py scripts/frontier_yt_pr230_assumption_import_stress.py
python3 scripts/frontier_yt_pr230_block127_wz_builder_block126_top_packet_adapter.py
python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
python3 scripts/frontier_yt_pr230_assumption_import_stress.py
python3 scripts/frontier_yt_retained_closure_route_certificate.py
python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py
python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py
python3 scripts/frontier_yt_fh_lsz_target_timeseries_full_set_checkpoint.py
python3 scripts/frontier_yt_pr230_schur_higher_shell_chunk_checkpoint.py --chunk 63
```

Results:

- W/Z builder current: `PASS=10 FAIL=0`
- W/Z builder scout: `PASS=9 FAIL=0`
- Block127 runner: `PASS=10 FAIL=0`
- Campaign status: `PASS=445 FAIL=0`
- Assumption/import stress: `PASS=128 FAIL=0`
- Retained route: `PASS=325 FAIL=0`
- Full positive assembly: `PASS=200 FAIL=0`
- Completion audit: `PASS=79 FAIL=0`
- Target-timeseries full set: `PASS=9 FAIL=0`
- Chunk063 higher-shell checkpoint: `PASS=15 FAIL=0`
