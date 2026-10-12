# A new test implied by the two fitted response plateaus

Direct parent derivation, 2026-10-12. The two already fitted responses imply
an additional asymptotic force prediction without a new parameter fit. The
calculation assumes a point baryonic mass in a constant Newtonian external
field E, and uses the same supplied QUMOND equation. It is not yet a binary
catalogue comparison or a complete two-body orbit calculation.

Write U=E e_z+GM r_hat/r^2 and Delta Phi=div[N(|U|)U]. Remove the imposed
uniform physical potential to define the decaying internal potential psi.
Set N_e=N(E), K=E N'(E)/N_e. Expanding only in the far region gives

    Delta psi = -2 GM N_e K P2(cos theta)/r^3 + O(r^-5),
    integral_sphere partial_r psi dS -> 4 pi GM N_e (1+K/3).

The flux fixes the monopole rather than extending a linearization through
the nonlinear point-source region. Since Delta[P2/r]=-6 P2/r^3, the leading
solution is

    psi = -(GM N_e/r) [1+(K/2)sin^2(theta)] + o(r^-1).

This known general external-field asymptotic agrees with the primary
[QUMOND analysis, section V.1](https://arxiv.org/html/0911.5464v2#S5.SS1).
Here it is applied to the campaign's particular reconstructed functions.
Differential positivity gives K>-1 at a smooth strict-D point; no new kinetic
or relativistic claim follows.

For both frozen D candidates, E=1.4915242022774435e-10 m/s² lies in an exact
constant-response interval, so K=0. These intervals are obtained by merging
adjacent zero-weight ramp intervals, not just inspecting the one knot cell
containing E. Their lower endpoint is1e-10; their upper endpoints are
1.7782794100389228e-9 (original) and5.623413251903491e-9 (interior).

Consequently the asymptotic internal force has an isotropic enhanced
monopole, GM N_e/r². Relative to a high-acceleration mass calibration where
N=1, the effective monopole mass is N_e M. The leading circular test-particle
speed scale is multiplied by sqrt(N_e). No additional binary observation
was fitted in extracting these consequences of the previously calibrated
galaxy/solar responses.

There is also a finite support fact for the point-source approximation.
Let delta=min(E-A_low,A_high-E)>0 for the constant interval. The reverse
triangle inequality gives ||U|-E|<=GM/r². Thus for

    r > r_star = sqrt(GM/delta),

N(|U|)=N_e everywhere on and outside that sphere. The effective extra source
density then vanishes outside r_star, and Gauss flux gives total effective
mass exactly N_e M. The exterior internal potential is harmonic and has the
above monopole plus decaying multipoles. Those multipoles need not vanish:
r_star is a support bound, not a radius beyond which the force is exactly
central or a finite-radius relative-error guarantee. The leading speed scale
is asymptotic, not an asserted prediction at r_star.

The adjacent checker records N_e, K, the interval, r_star for the supplied
solar GM, and the two speed-scale factors. Its angular surface-flux checks
are numerical consistency tests of the algebra; the triangle and flux
argument supplies the support statement. Values for other masses scale as
sqrt(M/M_sun) in this stipulated source problem.

An actual observational test must now supply a finite-separation field or
multipole error bound, source mass calibration, external geometry and its
spatial variation, trajectories, projection, detection and contamination
model. The inference ge=E N(E) used in the earlier fit is a separate
spherical-parent premise, not fixed by the local uniform-boundary problem.
This candidate consequence does not import a preferred observed wide-binary
result or count any new observation as a successful test.

## Source continuity

This V2 statement clarifies that the response itself was previously fitted
to galaxy velocities and solar/external constraints. Only the additional
binary consequence is unfitted. The original source-bound note, checker
and numerical receipt remain unchanged for reproduction.
