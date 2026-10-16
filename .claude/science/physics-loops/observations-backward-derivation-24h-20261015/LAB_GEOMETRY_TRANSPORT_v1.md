# Geometry uncertainty without selecting a density profile

Status: conditional-support. This standard kernel estimate addresses the
actual missing finite-body geometry certificate in the laboratory bridge.
It does not infer that certificate from a quoted marginal metrology error.
It extends the earlier density-total-variation bound to mass-preserving
displacements, whose total variation can be large even for small shifts.

Write Jx = z-hat cross x and r=|x-y|. For the scalar torque pair kernel,

`K_m(x,y) = (y dot Jx) h_m(r)`,
`h_m(r) = (1+mr) exp(-mr)/r^3`, `m>=0`.

For a path connecting two geometries assume that every interpolated pair
obeys r>=d>0 and |Jx|<=L. These are uniform geometric premises, including
all angles used to form the measured harmonic. Then

`|gradient_x K| <= Cx = exp(-md)[(1+md)/d^2 + L(md+2)^2/d^3]`,
`|gradient_y K| <= Cy = L exp(-md)(md+2)^2/d^3`.               (1)

To derive this, use |y dot Jx|<=rL, |gradient_x(y dot Jx)|=|Jy|<=L+r,
and |gradient_y(y dot Jx)|=|Jx|<=L. Direct differentiation gives

`h'_m(r) = -exp(-mr)[(mr)^2+3mr+3]/r^4`,
`h_m+r|h'_m| = exp(-mr)(mr+2)^2/r^3`.

Both r h_m and h_m+r|h'_m| decrease with r>0. For the second factor its
logarithmic derivative is `-m + 2m/(mr+2) - 3/r < 0`.
The mean-value integral along the two simultaneous line segments yields

`|K_m(x',y')-K_m(x,y)| <= Cx |x'-x| + Cy |y'-y|`.             (2)

One sufficient path certificate is that all original pairs have gap d0,
each mass element moves at most epsilon_A or epsilon_B, and
d=d0-epsilon_A-epsilon_B>0. An endpoint gap alone does not certify an
arbitrary interpolating path. Linear interpolation bounds the rotating
lever by the maximum of its endpoint values.

For nonnegative equal-mass source measures A,A' of mass M_A and B,B' of
mass M_B, choose mass-preserving transport couplings whose paths satisfy
the geometric certificate. Let their first displacement moments be
D_A=integral |x'-x| dPi_A and D_B=integral |y'-y| dPi_B. Integrating (2)
against the product coupling gives

`|Y_m[A',B']-Y_m[A,B]| <= M_B Cx D_A + M_A Cy D_B`.           (3)

The same bound applies to a normalized complex Fourier coefficient when
the geometry certificate holds uniformly in rotation angle. Real
sine/cosine coefficients and their amplitudes have the additional factor
two. For a Cartesian-product support class where every allowed transport
path satisfies the same d,L certificate, the infimum first transport
moments can be used. One cannot insert unconstrained Wasserstein infima
whose optimizing paths leave the admitted geometry domain.

No density profile is selected by (3). Instead, an independently justified
mass correspondence and displacement bound are required. Different total
masses need additional mass-error terms; signed hole contrasts require
positive/negative transports or total variation, not a net-mass bound.
The kinematic torque axis, angular readout, material response and source
charges are still premises.

## Planned diagnostic, not an experimental bound

The already exposed foil pattern masses motivate a deliberately labeled scale
illustration: take two positive source distributions of masses 0.65749 g and
1.19856 g, L=0.027 m, d0=50 micrometres, and stipulated mass-element movements
epsilon_A=epsilon_B=1 micrometre. These are **not** reconstructed apparatus
error bounds. Compute the complex/real torque envelope for m=0 and
m=20000 per metre, using labeled reference coupling 6.6742e-11 SI and unit
scalar strength. Compare its absolute size only; do not call it a confidence
region or compare its ratio to a chosen measured harmonic as an exclusion.

If this global mass/gap envelope is large, the local route fails to certify
small apparatus corrections. That does not show that actual corrections
are large. Cancellations require actual angular/mass correspondence or a
sharper geometry norm, rather than a silently supplied uniform profile.

Synthetic checks will verify derivatives symbolically, compare direct
kernel changes with (2) for fixed deterministic particle pushforwards,
integrate (3) for source measures and complex harmonics, and retain a
zero-net-mass contrast counterexample. These are support checks, not
empirical validation or a novel theorem.

