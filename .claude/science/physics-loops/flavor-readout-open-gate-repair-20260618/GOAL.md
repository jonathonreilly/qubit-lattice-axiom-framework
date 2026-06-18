# Goal

Repair the landed `audited_renaming` row
`flavor_readout_gate_equals_carrier_identification_2026-05-31` by changing
the source note to the claim it can actually support.

The audit found that the runner verifies real finite algebra, but the
load-bearing row was a relabeling/identification of gate concepts rather than
a retained derivation. This block converts the source boundary to `open_gate`
and hardens the runner to enforce that boundary.
