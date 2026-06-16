# Handoff

## Summary

This branch tightens the perturbative-validity runner check for
`wilson_m_h_tree_at_extremum_leading_order_in_r_bounded_note_2026-05-08`.

The audit blocker asked for more than square-root positivity. Part 8 now
compares the closed form `sqrt(1-x)` to the first Taylor truncation `1-x/2`
for small `x = 3r^2/u_0^2`, requiring the error to be controlled by the next
`x^2/8` scale.

## Changed Files

- `docs/WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`
- `scripts/frontier_wilson_m_h_tree_at_extremum_leading_order_in_r.py`
- `logs/runner-cache/frontier_wilson_m_h_tree_at_extremum_leading_order_in_r.txt`

## Boundary

This does not derive the uniform `N_taste=16` Higgs-channel readout or the
Wilson coefficient normalization. Those remain separate science blockers.
