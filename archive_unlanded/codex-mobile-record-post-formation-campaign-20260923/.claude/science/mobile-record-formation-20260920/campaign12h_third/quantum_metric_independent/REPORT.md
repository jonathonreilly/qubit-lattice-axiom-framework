# Independent finite quantum-metric check

**Disposition before author comparison:** the specified necessary CPTP test
fails. At N=2048, k0=11/10, gamma=1 and the supplied product tangent, the exact
microscopic-time derivative per matched pair is

    253943551350785258709380168798915548993408646371
    /3288323073641053210935625659843220349235316654080000

or approximately **+0.0000772258521026651502170470997**. For N-accelerated
Euler time the answer is 2048 times this value. This result was derived and
computed before access to any third-campaign author proof, script or result.

The homogeneous uniform product is stationary for the actual swap generator,
by a route-cycle coboundary, not merely by a zero mean current. Hence any
exact CPTP intertwiner fixes the full-rank product state Sigma. Complete
positivity, a two-by-two operator block matrix and the Schur complement
imply contraction of `Tr Delta Sigma^-1 Delta`; the positive derivative
therefore excludes this exact intertwining for the stipulated encoding and
preparations, already at sufficiently small positive time.

The derivative of the full tensor-product metric reduces exactly to
one-pair marginal derivatives. Correlations created by the classical process
do not require a product closure for this first derivative. The complete
proof, normalizations and exact local metric are in `DERIVATION.md`.

## Independently verified coverage

- Rebuilt the dimension-sixteen states from the stated integer stabilizer
  twirls, verified representative independence, and inverted tau exactly.
- Enumerated all 14^4 four-color words for route balance and reverse rates.
  The actual rates range from 1/20 to 21/20.
- Directly differentiated the actual four-context expectation in forty
  cases, retaining all fourteen current components, and separately verified
  the full fourteen-field marginal stencil across all 2048 coordinate planes.
- Evaluated the spatial sums and metric derivative as rational numbers.
  Constant-profile, gamma-zero, opposite-quadrature and classical-Fisher
  controls check the orientation and normalization. A two-site matrix control
  checks the reduction in the presence of an added zero-marginal correlation.
- `check.py`, `RESULTS.json`, `RUN.log`, `RUN.stderr` and `RUN_RECEIPT.json`
  preserve the complete independent execution. The first execution passed;
  no failed calculation or omitted failing assertion occurred.

`SOURCES.json` binds the complete three allowed definitions: encoding
ab657acc73902c4fe6ce42d0675fc77aeee977af63e4ff04a022238aff814e46;
routed rates dc7bac51a1ffb273e11e9356713778aeb645acbfb280973f927c1f1de007d873;
initial-current source a67bc5a0b8f9a85e0eccba11fc56870e7861410044ff5d6e28d1ddd05d384c78.

## Scope and remaining comparison

This is an exact finite-size compatibility obstruction for the fixed
preparation and the fixed classical process. No large-volume theorem,
hydrodynamic approximation, global-matrix numerical simulation, general
quantum no-go, native-qubit conclusion, publication or audit status is
claimed. Encoding injectivity alone is not operational implementability.
Other encodings or additional input-correlated resources are outside this
test. The author-source comparison remains separate and will be recorded
after the pre-comparison seal; this report and its derivation will then
remain unchanged.
