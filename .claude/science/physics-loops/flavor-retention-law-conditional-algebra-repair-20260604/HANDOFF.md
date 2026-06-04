# Handoff

This branch repairs the conditional audit on
`docs/FLAVOR_RETENTION_LAW_IS_A2PLUS_NOTE_2026-05-31.md`.

Main changes:

- Removes the hard-coded runner assertion that A2/source-locality status is
  closed by the packet.
- Narrows the source note to executable conditional algebra.
- Keeps the useful checks: onsite `C3` scalar forcing, `Q(0)=2/3`,
  `Q(-1/3)=1`, `Z/S_Q1` coefficients, diagonal/circulant intersection, and
  diagonal compression erasing off-diagonal circulant data.
- Explicitly leaves the A2-to-source-locality theorem open.

Verification commands:

```bash
python3 scripts/flavor_retention_law_is_A2plus_2026_05_31.py
python3 scripts/cached_runner_output.py --check-only scripts/flavor_retention_law_is_A2plus_2026_05_31.py
python3 -m py_compile scripts/flavor_retention_law_is_A2plus_2026_05_31.py
git diff --check
```

Expected runner result: `SCORECARD PASS=4 FAIL=0`.
