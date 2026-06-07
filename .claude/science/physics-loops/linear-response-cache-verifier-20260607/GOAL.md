# Linear Response Cache Verifier

Goal: remove the operational reproducibility blocker on
`linear_response_derivation_note` without promoting the open-gate heuristic.

The row is already audited-clean as `open_gate`; the remaining issue is that
the default runner cache records a timeout while the source note relies on a
completed frozen 44-family log.
