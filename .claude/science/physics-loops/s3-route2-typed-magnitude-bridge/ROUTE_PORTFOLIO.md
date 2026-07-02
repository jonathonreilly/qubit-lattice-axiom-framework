# Route Portfolio

## Selected Route

No-go for current color-only and E-center-blind typed magnitude maps.

Score: 3/3 for route-pruning value.  It targets the hard residual directly and
produces an exact witness family.

## Fan-Out

| Route | Expected movement | Disposition |
|---|---|---|
| Derive magnitude from color scalar alone | Would close magnitude bridge | Pruned: same color scalar, variable Route-2 magnitude |
| Derive magnitude from E-center-blind Route-2 support data | Would avoid a new source/readout theorem | Pruned: same blind signature, different magnitudes |
| Use signed bridge obstruction only | Already known | Not enough after sign split |
| Add a nonblind E-center primitive | Could still work | Left open as next target |
| Directly derive `q_E=15/8` from source/readout | Could bypass color route | Left open as next target |

## Synthesis

Dropping the sign does not solve the typed-domain problem.  The bridge must be
nonblind to the E-center readout or directly compute the E-center lift.
