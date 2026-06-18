# Goal

Add an audit-consumable runner/cache pair for `scale_reference_primitive` so
the independent audit lane can re-audit the high-load meta primitive without
guessing whether it supplies dimensionless physics.

This block does not audit the row, retag the ledger, or change effective
status. It only packages source evidence.
