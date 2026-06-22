# Route Portfolio

## R1: T-Row Shape Selector

Try to derive `beta_T=-alpha_T` from a center/shell row balance.

Result in this block: independent from shell scale. It gives `rho_T=-1` and
`q_T=5/6` if supplied, but leaves `s_TE` movable.

## R2: E/T Shell Scale Selector

Try to derive `alpha_T/alpha_E=-2` from relative shell normalization.

Result in this block: independent from row shape. It gives `s_TE=-2` if
supplied, but leaves `rho_T` and `q_T` movable.

## R3: Common Time-Factor Selector

Try to obtain both T-side entries from the conditional time/slice family.

Result in this block: no-go for this route. The time factor starts after
`P_R` is supplied and cancels from endpoint ratios.

## R4: Full Relative Row Primitive

Future positive route. A primitive selecting the full relative T row
`(alpha_E, alpha_T, beta_T)=(1,-2,2)` would close both T-side entries if it is
not target-importing.
