# Goal

Repair the post-audit source/cache scorecard mismatch for
`record_prerecord_instrument_kernel_gate_2026-06-06`.

The audit found the physics algebra correct but blocked clean handling because
the source note displayed `PASS=36 FAIL=0` while the committed runner/cache
displayed `PASS=38 FAIL=0`.

