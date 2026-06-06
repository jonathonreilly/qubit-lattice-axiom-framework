# Handoff

## Summary

This block provides an exact finite interface for supplied concentration
certificates over post-record histories and counts.

The runner verifies a positive law-scoped certificate:

```text
iid fair N=4, event |count_A-count_B| >= 4:
P(event) = 1/8 <= 1/4
```

and a wrong-law control:

```text
correlated fair N=4, same event:
P(event) = 1 > 1/4
```

Thus the certificate is valid under the law that supplied it and invalid under
a different law with the same expected counts and one-time marginals.

## Meaning

Post-record histories and counts are valid consumers of concentration
information. The concentration information itself lives in a supplied law,
dynamic-programming enumeration, exact finite calculation, or independently
supplied theorem.

## What it unlocks

- Audit rows can cite a clean certificate interface instead of treating
  expectation as calibration.
- Count-based events can be checked after pushforward from words to counts.
- Wrong-law transport becomes an explicit review failure.
- Stable dial claims remain separate from calibrated p-value claims.

## Files

- `docs/POST_RECORD_SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE_2026-06-06.md`
- `scripts/frontier_post_record_supplied_concentration_certificate_interface_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_supplied_concentration_certificate_interface_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-supplied-concentration-certificate-interface-20260606/`

## Next exact action

Commit, push, open the PR, record PR status, then pivot to the next independent
dynamics lane.
