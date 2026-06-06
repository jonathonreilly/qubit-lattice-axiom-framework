# No-Go Ledger

## NG-001: Stability bucket to selected dial

Rows in `stability_or_dynamics_selector` may have stable settings under named
maps or flows. That does not select a dial without a selector rule.

## NG-002: Koide/generation bucket to forced value

Rows in `koide_or_generation_selector` require explicit selector/readout
support. The bucket does not force Koide or generation values.

## NG-003: Measure bucket to Record-derived prior

Rows in `measure_weight_normalization` require supplied measure/prior bridges.
Record does not derive them in this block.

## NG-004: Sub-bucket to audit verdict

Sub-buckets are triage only. Independent audit owns verdicts.
