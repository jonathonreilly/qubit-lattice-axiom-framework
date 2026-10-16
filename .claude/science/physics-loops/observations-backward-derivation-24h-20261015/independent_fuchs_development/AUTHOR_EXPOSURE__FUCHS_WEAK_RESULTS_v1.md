# First weak-record diagnostic: limits before refinement

All results in FUCHS_DEVELOPMENT_RESULTS_v1.json are exposed development
diagnostics. No force, scalar strength or action has been fitted. Device
wiring, source phase/force correspondence, channel filters and moving-support
response are not independently established.

The frozen 24-case calculation completed. Under receiver2/source3 and the unit
phasor input, the full weak equation gives the following descriptive results:

| Window, s | gamma, per s | modulus b, V/s | relative RMS residual | late development residual |
| ---: | ---: | ---: | ---: | ---: |
| 600 | 1.94508014e-5 | 2.84626048e-7 | 0.598827 | 0.649237 |
| 1200 | 1.51651660e-5 | 1.91708111e-7 | 0.757259 | 0.861485 |
| 2400 | 1.67773254e-5 | 1.67572420e-6 | 0.683709 | 1.147116 |

The b estimates vary substantially with window duration. The reverse channel
hypothesis produces negative fitted damping throughout the declared grid.
These are limits of these candidate descriptions; noise covariance and
instrument transfer are unknown, so there is no calibrated statistical
rejection of the physical oscillator or the experiment. In particular, a
smaller numerical residual does not identify a physical receiver.

Column-normalized conditions near unity do not establish accurate absolute
forcing inference: an oscillatory source can nearly integrate to zero in a
long unmodulated window. Raw column norms/singular values are also needed.
Small quadrature-thinning changes do not bound measurement or model errors.
The inferred frequency digits likewise are numerical fit outputs, not
measurement accuracy.

The next mathematical refinement is to add compact test functions modulated
near the measured source-phase slope. This changes only the observation
functionals, not the physical operator. Freeze the slope rule and probe grid
before that calculation; retain all original failures and do not tune against
the other seven unopened records. Repeated functionals of the same samples
must not be treated as independent observations.
