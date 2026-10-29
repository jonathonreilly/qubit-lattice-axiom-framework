# Euclidean rotation import: pre-stated falsification criteria

Recorded before the independent geometry/analytic diagnostics, 2026-10-29.
Author scope: EUCLIDEAN_ROTATION_IMPORT_ASTRA.md and checks/euclidean_rotation_import_* only.
Root owns the campaign, lock, git, review requests and authority surfaces.

Primary candidate source: ethanwsussman/Yang--Mills-LLM-experiment,
commit 1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310;
RPM1.tex blob 86d31273743ea0b3dc2b99090058ce3b930fba5a.
This is tentative primary work, not an established theorem by attribution.

1. Actual Wilson diagonal geometry. Enumerate elementary four-dimensional
plaquettes near each plane x_j +/- x_k=0. A straddling plaquette must be
reflection-fixed as an unoriented loop and split at two plane vertices into
two reflected two-edge paths. Failure of any geometric condition refutes
that proposed positivity factorization. Verify matrix-entry factorization
independently on noncommuting SU(2) matrices; reversing the wrong path and
using a negative Wilson coefficient are mutation controls expected to fail.

2. Half-space locality. Reflection covariance of blocking alone is insufficient.
Enumerate complete fine footprints of centered coarse blocks and their
boundary-crossing paths. Exhibit or rule out coarse objects on a diagonal
positive half whose fine footprints enter the negative half. A crossing
invalidates direct pullback of the positive algebra at that placement. Test
an explicit buffer rule separately; only shrinking physical buffers can be
removed for compact tests strictly inside the continuum half-space.

3. Analytic hypotheses. Compare the source's global all-real-source
exponential bound with local analytic/cumulant bounds using independent
probability examples. A variable with every finite moment and local analytic
Laplace transform but finite Laplace radius refutes the claimed implication.
Check exact cumulants or Laplace singularity, not a fitted numerical tail.
Bounded cutoff observables count only if the controlling constant is cutoff
uniform after the actual physical normalization.

4. Source proof. Reconstruct every logical stage from RPM1.tex, including
spectral comparison, analytic positivity, slab estimate, point insertion,
angular growth, and Fourier elimination. A hidden use of rotation invariance,
unsupported operator domain, unjustified analytic continuation or wrong
growth/positivity quantifier is a material unresolved proof obligation.
No missing source step is silently repaired by a new physical premise.

5. Import match. A source theorem requiring a real random tempered field on
all Schwartz sources cannot be applied solely from a collision-flat partial
moment hierarchy. Scalar conclusions do not establish the full gauge-invariant
algebra. Check integrated coarse variables separately from fixed coarse
fields. The full four-dimensional existence and physical continuum mass-gap
targets remain OPEN unless all their own obligations are independently met.

The checks are finite/exact structural diagnostics and counterexamples to
specific implications, not a certificate of Yang--Mills existence, continuum
rotation invariance, an infinite-volume measure or a physical mass gap.

Additional geometry criterion, recorded after reading the full RPM1 proof
and before running geometry code: distinguish a reflection-symmetric free
box from the lane's standard periodic hypercubic torus. For the latter test
the complement of the fixed diagonal and explicit wrapping plaquettes.
If the fixed set does not separate the torus, or a wrapping straddler lacks
the reflected two-path factorization, the local free-box proof does not
establish diagonal RP of that periodic regulator. This is a test of the
proposed proof transfer, not a claim that every torus RP inequality fails.
An optional massive Gaussian torus Gram calculation may serve only as a
separate-model counterexample to importing diagonal positivity from square
symmetry alone; it cannot refute Yang--Mills positivity.

Additional analytic discriminator, pre-stated before its calculation:
let phi be the massive scalar Gaussian free field on R^4 and set
F=(sum_j partial_j^4)phi, still declared a scalar. The differential map
preserves supports and commutes with all signed coordinate permutations, so
the standard free-field reflection form should transfer to every required
mirror. Test whether its covariance multiplier
(sum_j p_j^4)^2/(|p|^2+m^2) has a genuinely noncontact rotational defect,
using a rational 3/5,4/5 planar rotation and divisibility by |p|^2+m^2.
If it does, even entire Gaussian source analyticity and ordinary all-order
Schwartz moment bounds cannot replace RPM1's specific global L1+L2 bound.
This counterexample concerns that proposed weakened theorem only; it is
not a Yang--Mills model and does not exclude stronger matched estimates.
