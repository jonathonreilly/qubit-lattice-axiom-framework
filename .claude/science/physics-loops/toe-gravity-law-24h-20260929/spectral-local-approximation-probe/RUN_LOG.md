# Actual centered-difference diagnostic

Executed at 2026-09-30T03:16:06.732843+00:00. Exit0; elapsed 14.854384s, peak RSS 106938368 bytes, under30s alarm/150MB price. Parent author engine reused with the literal centered stencil; this is not an independent computation.

Original-H complex-step gradient agrees with separately varied SBP expression within 2.3245e-16.

| n | state error | state error / spacing² | final C | final Jx |
|---:|---:|---:|---:|---:|
| 17 | 1.58290218e-06 | 1.1587565e-05 | 4.2281267e-06 | 0.000218178387 |
| 33 | 4.9798189e-07 | 1.37366772e-05 | 1.33017096e-06 | 6.12711474e-05 |
| 65 | 1.34321509e-07 | 1.43751551e-05 | 3.58789296e-07 | 1.60424392e-05 |
| 129 | 3.45064547e-08 | 1.4545211e-05 | 9.21709906e-08 | 4.09332334e-06 |
| 257 | 8.71993888e-09 | 1.45888128e-05 | 2.32920306e-08 | 1.03263911e-06 |

The initial nonzero finite Jx is retained in local_flow.json. Jy/Jz vanish identically by the actual diagnostic symmetry; they were not separately numerically evolved. Ratios approach a finite constant, as a second-order diagnostic predicts. No certified time, interval enclosure, exact finite first-class algebra or theorem from samples is asserted.
