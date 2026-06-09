# Claim Status Certificate

- Audit authority remains the independent audit lane.
- This PR does not edit `docs/audit/**`.
- This PR does not retag the ledger.
- This PR does not add axioms.
- The retained candidate surface is narrowed to the exact abelian
  `Z_N`/`U(1)` Wilson temporal-gauge plane-kernel bridge.
- Nonabelian reconstruction remains open pending a matrix-coefficient
  Peter-Weyl or explicitly projected class-kernel theorem with reconstruction
  and Gram-normalization checks.

Verification commands:

```bash
python3 scripts/frontier_rp_gauge_half_wilson_temporal_bridge.py
python3 scripts/cached_runner_output.py scripts/frontier_rp_gauge_half_wilson_temporal_bridge.py
python3 -m py_compile scripts/frontier_rp_gauge_half_wilson_temporal_bridge.py
git diff --check
git diff --name-only -- docs/audit
```
