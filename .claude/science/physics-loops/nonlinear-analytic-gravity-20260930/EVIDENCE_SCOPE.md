# What the written proof and computation establish

This is an author preparation record. The new composition has no formal
review or audit verdict. Root has cold-read the complete integrated proof and
primary; the separate Astra-low review remains pending. Prior focused checks
are frozen provenance, not independent review of this new authored source.

The note supplies the general theorem: continuum total constraint algebra and
field-dependent Jacobi, full-carrier tree transfer, exact first-order analysis,
uniform analytic existence/uniqueness and sampling/constraint convergence,
centered continuation, and explicit compatible conformal scalar data. The
primary is a diagnostic that can challenge the implementation, not a finite
proof of every grid, mode, datum, time or nonlinear coefficient.

The exact QQ(i) engine is reused author code. Its axial and mixed-direction
fixtures compute CC/GC through degree three and GG through degree two at
J=5,B=1,a=2,K=3,s=6,m^2=5. A separate J=3 fixture computes the displayed
all-zone value 7/4. It does not numerically compute nested Jacobi expressions:
those follow from the written inverse-metric variation and tree argument.

The full variation control uses six symmetric metric and momentum slots in
three dimensions. It compares the literal original curvature energy, via
complex-step differentiation, with the skew-adjoint augmented variation.
At n=3 it checks all 324 coordinate derivatives; at n=5 it checks 24 seeded
dense tangents. The original energy and augmented energy agree independently
of the false chain-rule and omitted-r-adjoint discriminators. This reuses an
earlier independently written control as an author implementation here.

The coupled scalar control computes all 56 canonical directions at n=7 for
each derivative, and 102 local general-symmetric metric-stress directions.
The centered operator has additional matrix-versus-literal-neighbor action
and single-mode symbol checks at n=1,3,7. Its two neighbor contributions
cancel at one site. These controls test normalization separately from a
particular trajectory.

The conformal fixture checks rational sufficient smallness at f=cos x,
b=1/10,sigma0=1/20 and r=1/128. Its 257-point, 16-iteration floating solve
is not interval certification or the proof of the fixed point. Literal
finite constraints are reported on every displayed grid, including the
nonmonotone coarse n=7 spectral value. The broad spectral n=17 residual
tolerance checks normalization; the analytic theorem is proved in the note.

The coupled scalar Kasner fixture has nonzero scalar momentum and its actual
metric stress is included in the Hamiltonian equations. It reports finite
state/constraint errors and energy drift over duration 0.01. That duration
is not certified by the majorant T. The coarse-to-fine factor-four check is
an implementation discriminator, not a derived rate or stability proof.

## Actual mutation coverage

All acceptance assertions remained unchanged while the computed source was
corrupted. Full sources, stdout and stderr are preserved, including failure.

| Mutation | Actual result and scope |
|---|---|
| Delete inverse-series cubic/quartic terms | Vacuum mixed-bracket cubic residual -4581 rejects the altered implementation |
| Scalar gradient coefficient 3 to 2 | Scalar lapse-bracket degree-two residual -14 and degree-three residual -1/2 |
| Inverse-metric shift coefficient 6 to 5 | Vacuum lapse-bracket residual already 5 at degree one |
| Remove circular mode wrapping | The separate alias value check fails |
| Omit the derivative-of-B adjoint | Literal full-Hamiltonian gradient comparison fails |
| Omit scalar metric stress | Coupled canonical gradient comparison fails |
| Double the conformal H-squared coefficient | Literal finest spectral scalar constraint becomes about 0.00250125 and fails |
| Halve centered derivative | Initially survived the trajectory fixture; after repair the direct n=3 action comparison fails with error 0.11936620731892152 |

The first seven detections are preserved against the initial source bytes.
The final change affects centered normalization controls and output scope,
not those seven computations or assertions. The repaired centered mutation
is rerun against the final primary. The surviving initial mutation is a real
coverage failure retained in historical/initial-freeze, not silently replaced
by a green record. Repeating unchanged broad tests is unnecessary; the entire
final primary is rerun because its source/input-bound cache must be fresh.

Resource metrics are actual Darwin measurements, where ru_maxrss is in bytes.
All runs use one numerical thread. No graph build, full audit pipeline,
staging, commit, push, PR mutation or formal audit occurs in this preparation.
