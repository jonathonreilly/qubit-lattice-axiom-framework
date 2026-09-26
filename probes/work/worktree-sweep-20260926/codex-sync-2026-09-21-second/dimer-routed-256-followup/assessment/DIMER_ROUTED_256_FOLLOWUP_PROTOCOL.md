# Declared larger-volume follow-up to the routed dynamic screen

2026-09-21, after inspecting the completed N<=128 aggregate results.
This is an explicitly subsequent study, not part of the original preregistered
960 histories. Those histories and all their finite residuals remain retained.

The initial screen shows substantial damping at every tested size. At N=128,
the mode-averaged half-period propagation residual is about 1.13 on the
irregular geometry and 1.21 on the winding geometry; its asymptotic target is
zero. Cross correlations have the predicted quarter-period sign and the
transverse autocorrelation changes sign by the half period. These observations
motivate a larger-volume check; they do not establish convergence rates.

Run exactly eight independent histories for each of the same two geometry
families at N=256, sixteen histories total. Use the unchanged C++ binary,
gamma=1, k0=11/10, fourteen equiprobable immutable pair colors, and the same
five times and three positive fundamental Fourier modes as the original
protocol. Generate fresh N=256 winding and irregular fixtures using fixed
seeds, with exactly 8N^3 plaquette proposals for the irregular one. No geometry
is selected by its observed correlations. The new fixtures are not asserted
to be equilibrium samples.

Freeze every seed, command, geometry, source and binary hash before dispatch.
Use two concurrent processes on the eight-GB host. Short validation runs may
measure runtime and verify state/geometry properties, but cannot change the
scientific sample count. The existing campaign deadline, 2026-09-22 00:25:55
UTC, remains hard. If fewer than sixteen histories finish, report all completed
and missing histories and do not call it the declared complete study.

Use exactly the original four primary observables and E,B normalization.
Report all directions and their equal-weight average, means and whole-history
standard errors. Use 10,000 whole-history bootstrap draws with fixed seed
202609211900 for pointwise 95% intervals. Eight histories per geometry provide
limited precision; modes and time samples are not independent replicates.
No exponent, damping law or phase boundary will be fitted. The N=256 results
will be displayed as this later follow-up, not pooled as though selected
before observing the N<=128 data.

The independent implementation check on the unchanged simulator transfers
only at its recorded source/binary identities. New production arrays and
derived results require their own authentication. All sources, failures,
partial outputs and commands remain on disk. No microscopic projector
preparation, quantum mechanism or geometric Gauss-wave identity is tested.
