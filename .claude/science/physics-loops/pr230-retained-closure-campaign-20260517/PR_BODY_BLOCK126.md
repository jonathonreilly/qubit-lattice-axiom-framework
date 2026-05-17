## Physics-loop PR230 Block126

This stacked block adds the matched top-side additive-subtraction packet for
PR #230.

Artifacts:

- Note: `docs/YT_PR230_BLOCK126_MATCHED_TOP_ADDITIVE_SUBTRACTION_PACKET_NOTE_2026-05-17.md`
- Runner: `scripts/frontier_yt_pr230_block126_matched_top_additive_subtraction_packet.py`
- Certificate: `outputs/yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json`
- Loop pack: `.claude/science/physics-loops/pr230-retained-closure-campaign-20260517/`

Result:

- 63/63 completed raw production files consumed.
- 1008 same-configuration tau1 rows built for `T_total=dE_top/ds`,
  `A_top=dE_top/dm_bare`, and `T-A`.
- 23 tau slices have complete same-configuration matching.
- Tau1 means: `T_total=1.245693776284446`,
  `A_top=1.2732143441892123`, `T-A=-0.02752056790476608`.
- Tau1 `corr(T,A)=0.9905564447030847`.

Claim boundary:

This is bounded support only.  It does not treat `dE/dm_bare` as `dE/dh`, does
not supply W/Z response rows, does not supply matched top-W/Z covariance, does
not supply strict non-observed `g2`, and does not supply accepted same-source
EW/Higgs action.  No retained or `proposed_retained` closure is claimed.

Validation:

```sh
python3 -m py_compile scripts/frontier_yt_pr230_block126_matched_top_additive_subtraction_packet.py scripts/frontier_yt_pr230_campaign_status_certificate.py scripts/frontier_yt_pr230_assumption_import_stress.py
python3 scripts/frontier_yt_pr230_block126_matched_top_additive_subtraction_packet.py
python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
python3 scripts/frontier_yt_pr230_assumption_import_stress.py
```

Initial results:

- Block126 runner: `PASS=10 FAIL=0`
- Campaign status: `PASS=444 FAIL=0`
- Assumption/import stress: `PASS=127 FAIL=0`
