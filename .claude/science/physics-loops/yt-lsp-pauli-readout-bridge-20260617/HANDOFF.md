# Handoff

This PR repairs the Y_T/LSP signed-record source-readout support packet by
constructing the signed source-record space as the joint spectral outcome set
of local Pauli projectors.

What changed:

- The note now replaces the old compatibility-only boundary with an exact
  source-readout edge.
- The runner now checks current minimal axioms, canonical LSP `K_r=P_r`, the
  retained-bounded source-action packet, joint spectral projector algebra, RN
  source-score identity, and firewalls.
- The JSON output and runner cache were refreshed.

What remains open:

- neutral EW/Higgs source/action authority;
- canonical `O_H`;
- scalar LSZ normalization;
- strict response rows or W/Z bypass;
- matching/running, `m_t`, and `y_t`;
- independent audit.

Verification:

```text
python3 scripts/frontier_yt_lsp_signed_record_source_readout_support.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_yt_lsp_signed_record_source_readout_support.py
```

Both pass with `RESULT: PASS=66 FAIL=0` for the target runner.
