# Route Portfolio

## R1: Repair M5 Normalization

Status: executed.

Replace the incorrect legacy one-loop formula with the plaquette-deficit
normalization `W = c_1 / beta`, `c_1 = (N^2-1)/4`. This directly addresses the
auditor blocker and preserves the bounded fan-out conclusion.

## R2: Promote To Retained Closure

Status: rejected for this block.

The MC comparator and epsilon target remain imported comparator-only inputs, so
the row cannot honestly be promoted to retained by this repair alone.

## R3: Claim L_s>=3 Exact Route

Status: demoted.

The branch leaves L_s>=3 as a planning pointer only. No retained predecessor in
this block supports making that route load-bearing.
