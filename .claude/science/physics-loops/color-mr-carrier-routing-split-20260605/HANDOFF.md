# Handoff

## Result

Added color `MR_color` carrier/routing split.

Files:

- `docs/COLOR_MR_CARRIER_ROUTING_SPLIT_2026-06-05.md`
- `scripts/frontier_color_mr_carrier_routing_split_2026_06_05.py`
- `logs/runner-cache/frontier_color_mr_carrier_routing_split_2026_06_05.txt`

Runner result: `PASS=53 FAIL=0`.

Stacked PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2746

## Main finding

`MR_color` splits into a supported structural carrier-content surface and
three still-open physical realization gates: species naming, color-record
readout, and link-index routing, plus downstream formation/action dynamics.

## Boundaries

- Does not derive physical color.
- Does not derive species names.
- Does not identify color-singlet records as physical records.
- Does not route base-`SU(3)` onto links.
- Does not select couplings, action shape, rates, time, or a dial.

## Next exact action

Continue campaign queue; likely next route is direct link-index routing
attempt or chirality/left-right residual.
