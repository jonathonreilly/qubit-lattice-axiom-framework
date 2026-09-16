# Personal mathematical review and evidence

This is an author review, not independent review or an audit verdict.
The four complete arguments were cold-read, including the middle portion
of the combined read that was initially truncated by the display. The
finite source programs and helper were inspected. Their decisive numerical
comparisons use different representations, not targets fitted to outputs.

## Findings and limits

1. A positive physical-time grid fixes the bridge noise coefficient at
   sqrt(2g^2/delta). Using sqrt(2g^2) would represent a different measure.
   The covariance is checked against Brownian bridge conditioning.
2. The original maximum-in-time transport estimate was strengthened by
   the entrywise positive operator |C|D^(-1)|C|*. Both its row and column
   bounds are used. This supplies the all-p Hessian norm and a space-time
   cubic bound, removing the earlier factor2 in the slab-chain constant.
   Previous successful source/output versions remain preserved.
3. The real comparison keeps the actual coupled bridge correction R.
   Only the straight-source scalar potential is extended. Equality is
   restricted to the chosen real-lift small-curl region. Its Gaussian
   magnetic result is not transferred to the compact law.
4. Cold checking retained the temporal interpolation factor
   b(theta)=(2+cos theta)/3. The Gaussian covariance is a magnetic marginal
   after quotienting the actual link nullspace. Replacing b by1 changes
   that covariance, as the independent matrix/Fourier calculation detects.
5. The published discrete Riesz theorem is diagonal. The anisotropic
   diagonal ratios are reduced to it by explicit replicated-coordinate
   pullback. A sharp bound for arbitrary off-diagonal discrete transforms
   is not imported. The separate spatial curl projection needs only a
   finite standard Riesz constant.
6. The first integer checker used a plus sign where the selected dual
   orientation gives d I2(Q)=-I3(boundary Q). The original source, failure
   and explicit unit-face diagnostic are retained. Corrected tests cover
   all six dual plaquette orientations and exact current fillings.
7. Enlarged filling boxes can overlap. The probability proof uses that
   distinct actual bad components are disjoint BEFORE multiplying their
   p powers and dropping constraints in the counting sum. It never infers
   full Bernoulli domination from finite-set intersection bounds.
8. The real lift is a coarse cochain on contractible spacetime. It does
   not recover all Brownian interval windings or torus harmonic sectors.
   Chart multiplicity, domains, normalized weights and source dependence
   remain the main compact-transfer obligation.
9. The first fault harness stopped because a primary program hashes its
   sibling helper and that path had not been copied. This infrastructure
   failure is retained and is not counted as a mathematical rejection.
   The retry includes the exact helper bytes and checks its hash.

## Primary evidence and reproduction

Run the four primary programs from repository root:

```sh
python3 .claude/science/physics-loops/toe-compact-response-20260916/evidence/bridge_cubic_check.py
python3 .claude/science/physics-loops/toe-compact-response-20260916/evidence/convex_carrier_check.py
python3 .claude/science/physics-loops/toe-compact-response-20260916/evidence/integer_filling_check.py
python3 .claude/science/physics-loops/toe-compact-response-20260916/evidence/magnetic_covariance_check.py
```

Each declares a120-second timeout contract. Paired FINAL receipts are
byte copies of the successful current-source raw attempts, not new runs
or canonical audit caches. The convex program imports the bridge helper
and records both source hashes. No primary program reads a scientific
repo result as its expected numerical target.

The bridge program checks20 time-precision cases and18 one-face integrals.
Independent Gaussian-Hermite and Fourier-Bessel third derivatives differ
by at most1.74e-12 in those cases. For two adjacent faces and two interior
time nodes, the mixed third derivative is about-0.000248855607621634;
a finite difference of the independently formed Hessian gives
-0.000248855607583483. The common-face covariance and the physical g
scaling are retained. Quadrature/cutoff comparisons are observed numerical
checks, not rigorous tail enclosures or the continuous-time theorem.

The convex program checks derivative matching of the explicit scalar
extension, its equality region and selected bridge Hessians. Independent
integration of affine time fields agrees with the algebraic and Fourier
quadratic carrier. The stronger cubic coefficient is used in its final
parameter examples.

The integer program verifies1024 coordinate-path edge fillings, twelve
finite signed-current examples, all six dual face orientations and the
actual spatial-cell witness multiplicities. The finite currents are
constructed test objects, not samples from the Hamiltonian measure.
Eighty-digit evaluation with an analytic positive-series tail bound gives
Lambda(1)<0.169 at alpha=pi/3,T=T_balanced,g=.003. The example
alpha=.1,T=.05,g=.0002 fails the sufficient test (Lambda(1)>8.47);
g=.0001 satisfies it with Lambda(1)<2.79e-21. This is not a phase threshold.

The magnetic program independently inverts link quadratic forms of sizes
576 and768 on L=4 spatial tori, with3 and4 time slices. The magnetic
covariance/Fourier differences are below4.16e-14. Three replicated-coordinate
examples give intertwining residuals below2.78e-15. A signed static
response equation challenges the positive majorant with concentrated
space-time inputs. That static equation is explicitly not a stochastic
bridge simulation.

## Formula faults

Run evidence/run_formula_faults.py to reproduce twelve declared formula
perturbations. The successful retry preserves every mutated source and
actual stdout/stderr, and each reaches an AssertionError: cubic cumulant
sign; four-link flux variance; time-grid noise weight; adjacent-face
metric; scalar transition polynomial; interpolation Fourier factor;
integer commutation sign; dual orientation; witness loss exponent;
magnetic matrix carrier; replicated rate; and replacing the absolute
incidence majorant with a signed matrix.

The adjacent-face fault is rejected at the metric identity before the
third-derivative calculation. The witness exponent is rejected against
independently enumerated orientation/multiplicity counts. The signed
majorant fault fails entrywise positivity before the cubic bound.
Those outcomes are not presented as failures of later checks.

## Review and landing priorities

The highest-value independent checks are the stationary source-variation
limit, space-time operator majorant, magnetic marginal and replicated
Riesz use, plus the conditional enlarged-box estimate. The compact
transfer is explicitly unproved; no reviewer should be asked to ratify
it from these finite calculations.

Canonical registration/cache envelopes, any formally applicable N-gate
certificate, independent review and the combined integration pipeline
remain pending. The exact source/receipt identities are bound by the
focused report and manifest. No retained or audit status is written.
