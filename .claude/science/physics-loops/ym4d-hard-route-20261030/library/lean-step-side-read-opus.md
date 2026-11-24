lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T01:31Z

# lean-step-side-read-opus: what in the SA YM4 Lean release needs block side 2^40, and where the floor H is chosen

Queue row 1464 (next row 2 of row 1460). Started 2026-11-24T13:31Z on Mac mini worker 3. Read only, no proof, no build.
Source: Sussman-Alpoge YM4 Lean release at `~/ym4d-papers/sa-ym4-lean-full`, commit 3932084a9b82 (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text).

## Plan

1. Confirm the release commit; find `IsUnitMeshStepParameters` and its side hypothesis (side_ge / side_gt / 2^40).
2. List every lemma in `YangMills/Construction/ClusterExpansionOfAStep` and `YangMills/Construction/TotalDensitiesGiveASystem` that reads the side hypothesis, with the inequality each needs; then their direct consumers.
3. Find where the coupling ceiling/floor H of the calibration is chosen, and how it relates to the side.
4. Decide (a) explicit floor H(L) and smallest admissible side, with numbers, or (b) side bound structural, no small-block step.

## Results (written step by step)

