# Conditional recovery of a common potential-amplitude drift

Root's additional personally derived probe, after freezing the primary
multi-mode inverse and before reading the focused checker's new-unit results.
This tests one measurement assumption rather than installing a calibration
function. It is part of the same inverse block, not a separate milestone.

The primary inverse uses registered matter-metric potential histories. Suppose
instead the recorded pair is Ptilde=g(tau) P and Jtilde=g(tau) J, with a single
unknown smooth positive gain shared by both potentials and all modes. Known
common time and spatial coordinates, and the relative calibration of the two
potentials, are still premises. Constant nonzero per-mode row multipliers are
also harmless, because both the row and right-hand side scale together.
This is a stipulated measurement class; it does not describe arbitrary survey
bias, convolution, separate sensor gains or observation on a past light cone.

Let s=g'/g. Direct differentiation of the original five-coefficient equation
gives another equation of the same form, with extracted coefficients

    atilde=a-2s,
    ctilde=c-a s-s'+s^2,
    dtilde=d, etilde=e, ftilde=f-d s.                 (1)

At each epoch the map from the original design matrix to the recorded one is
an invertible triangular column transformation times the nonzero gain. Thus
its rank is unchanged. This statement requires the same gain for every row;
it is not implied by having two different observation channels.

On B=etilde/2>0, B!=2/3, define

    L=B'/(2B),
    q=(dtilde-6Bh)/(4-6B),
    s=[3(h-q)-2L-atilde]/2,
    c=ctilde+atilde*s+s^2+s',
    f=ftilde+dtilde*s.                               (2)

These follow from the structural coefficient identities. Inserting c,q into
the primary curvature formula recovers kappa. The inferred gain is
g=g0 exp(integral s d tau), and division by it restores the full background,
Hamiltonian, momentum, scalar and dust checks in the primary construction.
No chosen gain shape or scalar initial state is needed in this restricted
inverse. The remaining g0 and constant per-mode factors rescale linear mode
amplitudes and their reconstructed initial data. They are not A0: the latter
changes the absolute gravitational/matter normalization of the background.

Unlike the calibrated primary inverse, this particular drift-elimination
route excludes B=2/3: the coefficient d then equals 4h and cannot be used in
equation (2). Other full constraints may carry information there; this probe
does not classify that chart. Likewise no all-method impossibility is asserted
for separate gains, rank loss, noisy data or unknown clocks.

The gain itself has not been measured here. Root's control multiplies the
potentials of the original-equation forward witness by a declared nonconstant
gain, extracts the changed coefficients from those corrupted records, and
recovers its logarithmic drift and the physical q,kappa without giving the
gain to the inverse. The exact transformation and inverse are also checked for
arbitrary smooth symbolic functions. This is synthetic equation-level
calibration support, not empirical evidence for the scalar action.
