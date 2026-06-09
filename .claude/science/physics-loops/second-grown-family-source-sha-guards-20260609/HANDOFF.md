# Handoff

Branch: `physics-loop/second-grown-family-source-sha-guards-20260609`

Target claim:
`second_grown_family_note`

What changed:

- `scripts/second_grown_family_battery.py` now checks each subordinate evidence
  runner exists in current source.
- It verifies each subordinate runner's live SHA matches the SHA pinned in its
  fresh cache header.
- The source note records the stronger `PASS=16 FAIL=0` battery and the new
  source-SHA guard.
- The battery cache was refreshed.

Verification:

```text
python3 scripts/second_grown_family_battery.py
PASS=16 FAIL=0

python3 scripts/cached_runner_output.py scripts/second_grown_family_battery.py
status: ok
```

Remaining boundary:

This branch does not resurrect the archived broad second-family table or move
audit status. It only strengthens the current bounded packet for re-audit.

Next action:

Review-loop landing supplies the reviewer extraction. The remaining action is
independent re-audit of the changed source note. Do not edit `docs/audit/**` by
hand.
