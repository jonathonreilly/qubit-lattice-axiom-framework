# Goal

Repair `dimension_selection_lower_bound_bridge_v2_2026-05-20` without adding
axioms and without retagging the audit ledger by hand.

The concrete blocker was that the old lower-bound V2 packet still admitted a
WKB/discrete-to-eikonal bridge for the finite-k normalized centroid sign. The
repo now has a retained bounded finite-k bridge that computes the exact
normalized tangent recursion and parent finite-probe replay, so this block
rewires the older packet to use that retained bridge directly.
