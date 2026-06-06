# Handoff

This branch repairs `record_prerecord_instrument_kernel_gate_2026-06-06`.

The prior audit blocker said the packet used a supplied projective instrument
and Born trace rule with no cited retained authority. The branch now cites the
retained-bounded LSP canonical `K_r = P_r` note and the Lueders trace-normalized
branch note, and the runner verifies those anchors.

Verification:

```text
python3 scripts/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.py
SCORECARD: PASS=33 FAIL=0

python3 scripts/cached_runner_output.py scripts/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.py --check-only
fresh logs/runner-cache/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.txt

git diff --check
clean
```

Boundary:

- No audit files are edited.
- No new axiom is introduced.
- No bare retained status is claimed.
- The physical readout context remains supplied.
