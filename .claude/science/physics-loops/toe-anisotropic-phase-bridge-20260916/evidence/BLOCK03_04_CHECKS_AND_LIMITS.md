# Phase-corrector and local-density checks

These are personal author checks. They are not independent review or a
thermodynamic phase computation. The full arguments are in working notes
BLOCK03 and BLOCK04; all assertions use those stated finite carriers.

## Actual block03 failure and repair

The first source, preserved as `block03_phase_corrector_check.ATTEMPT1.py`,
has SHA256 `6120226859f1ea3e1a81c78a3561e990a355d31e4cb67ba30a34bc5001a07b7e`.
It exited1 when the direct subtraction `denominator-norm2-covariance_part`
exceeded an absolute1e-13 check at g=3. The diagnostic source and stdout
preserve the actual values: denominator4199.441335023202,
norm2 approximately0.4, covariance4199.041335023201, residual9.094947e-13.
The error is at the scale of one floating-point spacing of the large terms.

The replacement evaluates the analytically cancelled mean-gradient term
with compensated summation and checks that term against the separately
constructed squared norm. It also reports the raw large-term subtraction.
This is an arithmetic reformulation of the identity check, not new evidence
that the cancelled identity needs a physical correction. Its scope changed
from a direct large-term subtraction to the cancelled algebraic expression;
the original failure and both evaluations remain available. No phase claim
or large-volume estimate is inferred from either.

Attempt2 passed. Attempt3 changes only the explanatory comment to describe
that reformulation accurately and is the current source/output pair. The
attempt2 source remains preserved. The one-plaquette harmonic-mean identity
agrees with the independently computed electric inverse spectrum to about
1.1e-15 absolute in the stated samples. Character variational bounds increase
toward the finite spectral response as the test family grows. At two-square
g=0.6, the1/2/3-radius bounds are approximately0.94239,0.98776,0.99472,
below the finite-cutoff response0.99759. These values concern two plaquettes,
not a growing three-dimensional lattice. The parent block02 documents its
electric-cutoff comparison.

The cube calculation realizes an exactly closed real plaquette field using
link angles, checks the gradient of the sine combination by finite
differences, and finds a strictly positive nonlinear gradient along the
linear cube-kernel direction. The proof uses positivity on an open set, not
an expectation reconstructed from these few sample configurations.

## Block04 checks

`block04_local_heat_and_orthogonality_check.py` passed on its first recorded
run. That exact source is preserved as `.ATTEMPT1.py`. Attempt2 adds the
principal cube-charge open-set check and also passes. Its source SHA256 is
`b44b81c44689f4833b7b2d8f9f854af2746eda96895052a6db3ff7833398e5b4`.
The4096 corner configurations all have principal charge1 and raw charge0
within4e-16; the event floor follows from the analytic neighborhood and local
density argument, not from treating these corners as random samples.

 A two-angle,81-dimensional finite-difference Hamiltonian checks both
sides of the positive-kernel sandwich directly with matrix exponentials,
and checks the same inequalities on its positive ground vector. This
structural comparison model is declared explicitly; it is not silently used
as the three-dimensional gauge theory.

Actual cubic cochain matrices for2^3,3^3 and4^3 vertex boxes verify the local
support counts and exact character orthogonality. Product-Haar integration
is computed by integer Fourier-frequency arithmetic, not random sampling.
The stated13-link and52-touching-plaquette upper bounds hold in these
examples; the general bounds follow from at most four plaquettes per link.
The analytic circle-heat bounds are also compared with a positive wrapped
Gaussian evaluation. Their sufficient local constant is intentionally very
small: at g=0.7,t=1 its log is about-692.74. It supplies a strict uniform
method restriction, not a useful finite-size phase threshold.

## Checks not performed

No independent reviewer, certified infinite-dimensional numerical error
bound, infinite-volume state computation, growing-loop response construction,
canonical runner registration, or formal audit is present. The finite
calculations challenge factors, signs, geometry and comparison directions.
The local-density and finite-template conclusions rely on the written
Feynman-Kac and Haar-orthogonality argument. The full susceptibility and
fixed-coupling phase remain open.
