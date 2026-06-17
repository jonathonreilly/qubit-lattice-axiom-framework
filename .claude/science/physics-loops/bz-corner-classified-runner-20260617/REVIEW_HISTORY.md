# Review History

- 2026-06-17: Source-side repair prepared. No review-loop or audit-loop run by
  this agent; reviewer owns extraction and landing.

Verification performed:

```text
python3 scripts/probe_bz_corner_decomposition.py
python3 -m py_compile scripts/probe_bz_corner_decomposition.py
python3 scripts/cached_runner_output.py --refresh scripts/probe_bz_corner_decomposition.py
```
