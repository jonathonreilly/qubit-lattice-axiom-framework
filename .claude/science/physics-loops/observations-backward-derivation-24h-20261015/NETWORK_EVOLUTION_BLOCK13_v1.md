# A remaining action normalization in the calibration-independent response class

Root's personal conditional calculation. This explicit family asks what the
four-setting test leaves undetermined; it is not a general impossibility claim.
There are no new empirical inputs. The extra freedom is relevant because
removing an absolute calibration from a test is not the same as deriving its
physical scale.

Take any finite positive mass matrix M and stable stiffness K(u)=K0+(a+b*u)ww^T
on the chosen command interval. Let the physical equation be

    M Q''+K(u)Q=bsource*f,
    y=B+G*cread^T Q.

All matrices, source/readout vectors and the input/output contract are explicit
candidate conditions. G is an unknown common response gain and a,b are unknown
common intervention calibration coefficients, as in the previous probe.
The zero-initial-data transfer is

    T(u,z)=G*cread^T[z^2 M+K(u)]^(-1)*bsource.

For every lambda>0 construct

    Mlambda=lambda*M, K0lambda=lambda*K0,
    alambda=lambda*a, blambda=lambda*b, Glambda=lambda*G.

Keep source/readout vectors, input f and measured time unchanged. Then

    Tlambda(u,z)=T(u,z)

for every command and frequency where the inverse exists. The proof is simply
that the entire dynamical matrix is multiplied by lambda and its inverse by
1/lambda. Stability and graph signs are preserved. Generalized normal-mode
frequencies are unchanged. The four-setting polynomial therefore agrees
identically throughout the full response family, not merely at four points.

This is an existence witness for an unidentified normalization in this specific
measurement contract. It does not say that independently calibrated mass,
force, displacement, gain or work cannot distinguish the family. In particular,
the assumption that G is known would remove the displayed compensating gain
freedom; a nonzero calibrated transfer then distinguishes this lambda family.
Unit kinetic normalization selects coordinates/conventions for the mathematical
model; it is not a measurement of this physical mass/action scale.

For a fixed physical input and zero preparation, Qlambda(t)=Q(t)/lambda, so
the actual work delivered up to a finite timeT obeys

    Wlambda(T)=integral_0^T f(t)*bsource^T Qlambda'(t)dt=W(T)/lambda.

The recorded transfer can stay equal while this independently measured energy
differs. A calibrated nonzero-work channel would supply precisely information
that the gain-independent response identity discarded. That channel requires a
physical force/displacement or energy identification; calling a numerical
Hamiltonian value measured energy would supply the missing bridge by assertion.
For a constant one-mode forceF, massm and stiffnessk, zero initial state gives
Q=F*(1-cos(sqrt(k/m)*t))/k and W=F*Q. Rescaling m,k,G as above preserves the
recorded response but changes W by1/lambda, including positivity for times away
from a complete return. This elementary example realizes the full family.

The action, source identification, gain and intervention calibration are still
conditional. This calculation derives neither a scalar kinetic coefficient nor
Planck's constant nor a universal energy calibration. It shows concretely why
one useful calibration cancellation cannot be counted as a scale derivation.
The next physical route is a second, independently justified work/energy channel
or a calibrated actuator/readout within one unchanged scalar action.
