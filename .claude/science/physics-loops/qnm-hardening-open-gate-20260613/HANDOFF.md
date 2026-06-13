# QNM Hardening Handoff

**Date:** 2026-06-13
**Branch:** `physics-loop/qnm-hardening-open-gate-20260613`
**Scope:** source-only open-gate unblock; no audit result or ledger edits.

## What changed

- The QNM note now has a downstream source-boundary firewall.
- The runner asserts that the source forbids promotion to a positive QNM
  spectral law and requires future stable sub-Nyquist peak controls.
- The refreshed cache includes:
  `SOURCE FIREWALL PASS` and `CERTIFICATE PASS`.

## Verification

```bash
python3 -m py_compile scripts/qnm_hardening_stability_certificate.py
python3 scripts/qnm_hardening_stability_certificate.py
python3 scripts/cached_runner_output.py scripts/qnm_hardening_stability_certificate.py --check-only
git diff --check
```
