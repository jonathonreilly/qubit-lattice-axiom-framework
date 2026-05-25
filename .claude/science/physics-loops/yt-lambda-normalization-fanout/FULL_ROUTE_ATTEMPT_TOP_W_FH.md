# Full Route Attempt: Same-Source Top/W FH Ratio

Date: 2026-05-25

This block tries the top-ranked route from the lambda-normalization fanout:

```text
same source h
  -> M_t(h), M_W(h)
  -> [dM_t/dh] / [dM_W/dh]
  -> y_t = (g_2 / sqrt(2)) [dM_t/dh] / [dM_W/dh]
```

Result:

- Algebra closes exactly.
- Source-coordinate rescaling cancels exactly.
- The retained EW Higgs gauge-mass theorem supplies the W denominator formula.
- Current Y_T source-action lane does not yet provide physical same-source EW/Higgs authority
  or strict top/W response rows.
- Current v-scale `g_2` authority is not retained.

Artifact:

- `docs/YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md`
- `scripts/frontier_yt_fh_top_w_response_ratio_gate.py`
- `outputs/yt_fh_top_w_response_ratio_gate_2026-05-25.json`

Next positive target:

Build strict same-source top/W response rows or prove the Y_T source-action
surface is the accepted neutral EW/Higgs action surface.
