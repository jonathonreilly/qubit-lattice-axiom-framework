# No-Go Ledger

## Centered Segment Is Not Literal Geometry

The centered finite-path surrogate assumes a centered interaction segment. The
actual harness has a static mass at `x_src ~= 5`, full beam path
`x in [0, 14.75]`, regularizer `r+0.1`, and detector-centroid readout.

## Short-Path Regime Prediction Fails

At `T_phys=7.5`, the surrogate predicts a steep short-path slope near
`-1.7336`. The measured `H=0.25` slope is about `-1.4356`, essentially the same
as the `T_phys=15` slope. That falsifies the surrogate's regime-transition
claim.
