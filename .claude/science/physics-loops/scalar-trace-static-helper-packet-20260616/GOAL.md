# Goal

Repair the source-side audit blocker for `scalar_trace_tensor_no_go_note`
without changing audit verdicts or adding axioms.

The 2026-06-15 audit accepted the algebraic no-go conditional on the imported
scalar functional, probe families, and Einstein-residual evaluator, but it
could not inspect those helpers through the dynamic `_frontier_loader` packet.
This branch makes those helper edges static and supplies the missing helper
cache.
