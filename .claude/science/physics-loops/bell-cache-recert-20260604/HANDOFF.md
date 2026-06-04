# Handoff

This PR refreshes the Bell/CHSH runner cache under the declared audit timeout.

Verification:

```bash
python3 -m py_compile scripts/frontier_bell_inequality.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_bell_inequality.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_bell_inequality.py
git diff --check origin/main..HEAD
```

The refreshed cache header records:

```text
timeout_sec: 1800
exit_code: 0
status: ok
```

This branch does not touch `docs/audit/**` and does not promote the scientific
status beyond the bounded model-surface CHSH result.
