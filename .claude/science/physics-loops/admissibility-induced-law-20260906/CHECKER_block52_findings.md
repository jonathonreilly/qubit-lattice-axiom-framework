# Block 52 — refuting pass and findings (2026-09-21)

1. Disjoint machinery (`specs/supervisor_control_block52_refuter.py`): W1 symbolic content; W2 symbolic expansion; W3 Monte Carlo of captures in a two-content gas (biased walk `0.2006, −0.3997, 0`; forward hops `0.0662, −0.4669, 0`); W4 three records, 17550 ordered configurations, flows balanced; W5 the share of hops against the content. All pass.
2. Findings folded: an empty `sum()` (the integer 0) divided by two, and `(3 − 1)/6` with Python integers, each gave a floating-point number inside an exact comparison (runner E2; refuter W5). Both now start from exact numbers. The campaign has met this four times; the runner's self-scan looks for floating-point literals and cannot see it.
3. Finding folded: the mutation `capture_weighted_by_content` as first written added and subtracted the same term and did not bite; rewritten to use the forward clause's weight.
4. The prediction (equal winds in the three classes) preceded the control's result (`1.006 ± 0.019`).
5. Stated limits: second order in gradients; one `α`, one density, one scattering rate; no forces under the clause.
