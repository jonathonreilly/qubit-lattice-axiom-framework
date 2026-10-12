# A discovered limit in the velocity-to-force interpretation

2026-10-12, direct author follow-up. This check was prompted by the UGC07577
mismatch. It occurs after the shared-response family was frozen and before
any of its fitted weights. It changes the interpretation, not the frozen
galaxy selection, input velocities, numerical output or error rectangles.

The original [Swaters et al. reduction](https://arxiv.org/abs/0901.4222),
Section3.5, explicitly leaves asymmetric-drift corrections unapplied.
UGC7577 is one of three named exceptions to their generally small correction:
its maximum estimated correction exceeds3 km/s. The article also calls its
velocity field regular despite the low rotation amplitude. Table2 lists a
last speed18 km/s at2.29 kpc for distance3.5 Mpc. Our processed source has
18 km/s at1.69 kpc for2.59 Mpc; the radius agrees with distance rescaling.
That endpoint agreement does not establish every intervening reduction step.

The [SPARC source paper](https://arxiv.org/abs/1606.09251), Sections1 and3.2,
notes that pressure support matters near rotation speeds20 km/s. Its quoted
velocity errors include approaching/receding asymmetry as well as a fitted
velocity error; they are not simply independent counting errors. I found no
documented additional UGC07577 pressure correction in the SPARC article.
This last statement is a limit of the inspected documentation, not proof
that no later correction exists anywhere.

Consequently, equating the current table's rotation speed directly with
sqrt(R*g) is a significant premise for this object. The numerical field
comparison remains intact, but its residual alone cannot reject the gravity
mechanism. The actual pressure/dispersion profile and source reduction must
be resolved before making that stronger inference. Nor does this finding
show that pressure support is large enough to explain the calculated excess.
No galaxy was dropped and no correction chosen to erase its residual.

## Reverse reconstruction of the missing readout, under explicit premises

For an axisymmetric steady gas layer with no mean radial flow and isotropic
effective pressure P, radial force balance is

    v_phi^2/R = g_R + (1/rho) dP/dR.

If the scale height is constant with radius and sigma is an isotropic
one-dimensional velocity dispersion, P=rho*sigma^2 and rho is proportional
to gas surface density Sigma. Hence

    v_c^2 - v_phi^2 = -sigma^2 d ln(Sigma*sigma^2)/d ln R,
    v_c^2 = R*g_R.

This is an observation-to-force map with measured velocity dispersion and
density gradients as required inputs. It is not another gravity parameter.
It must not be applied a second time if a source already reports v_c.

Conversely, a stipulated g_R and measured v_phi give the *required* pressure
profile over a measured interval, for a declared outer pressure:

    P(R)=P(R_out)+integral_R^R_out rho(s)
                         [g_R(s)-v_phi(s)^2/s] ds.

An observed dispersion profile can then falsify that required pressure.
Without the density profile, its vertical treatment and the outer pressure,
the inversion is underdetermined. Our fitted positive ring source recovers
a gravitational component curve; its detailed surface-density derivative
has not been independently validated as a gas-pressure tracer. Reusing it
for this derivative without checking the actual H I profile would import
another uncontrolled assumption.

The frozen shared-response program will therefore report only a conditional
comparison with the supplied circular-speed interpretation. Any reconstructed
function remains a candidate, and any finite-family mismatch remains unable
to distinguish wrong gravity from a wrong kinematic readout. A separate
pressure-aware follow-up must use actual dispersion/surface-density evidence
and declare any remaining boundary freedom before fitting it.
