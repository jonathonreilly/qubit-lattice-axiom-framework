# Assumptions And Imports

Load-bearing machinery:

- Live capture packet runner
  `scripts/staggered_backreaction_live_capture_packet_check.py`.
- Capture closure harness and transitive helper sources:
  `scripts/frontier_staggered_backreaction_capture_closure_harness.py`,
  `scripts/frontier_staggered_backreaction_iterative.py`,
  `scripts/frontier_staggered_cycle_battery.py`,
  `scripts/frontier_staggered_layered_backreaction.py`, and
  `scripts/frontier_staggered_backreaction_prototype.py`.

Imports retired or reduced:

- The missing prototype-helper source/certificate blocker is retired by the
  source-packet verifier and fresh cache with `PASS=82 FAIL=0`.

