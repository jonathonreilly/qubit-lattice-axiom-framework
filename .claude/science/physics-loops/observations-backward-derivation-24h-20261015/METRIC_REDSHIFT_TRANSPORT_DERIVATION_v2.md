# Conditional redshift-to-force transport on repeated cones

Root's extension of the metric-readout block. The pre-control v1 is preserved;
v2 adds the independently requested origin-domain qualification.
This is a kinematic inverse inside the same linear metric, photon and tracer
premises. It is not a solution of the full scalar/dust field equations and
does not establish physical non-identifiability of the action inverse.

Let u=eta_o, r be a registered comoving source radius, eta=u-r, and
v=grad_x Vv. The matter Euler equation implies

    Psi=-(partial_u+Hc)Vhat,
    v_r=(partial_r+partial_u)Vhat,

after fixing the spatially constant velocity-potential freedom. Hc=Hc(u-r).
Lensing supplies P only in its calibrated angular subspace. Suppose its
repeat-time derivative, the source/observer registration, and all endpoint
terms in the redshift formula have been determined. Define the corrected
source residual

    Rz = epsilon-Psi_o+n.v_o+2 int_0^r P_eta(u-s,s n) ds.

Here epsilon is the fractional redshift perturbation relative to the scale
factor ratio at the actual emission/reception times, not simply relative to
the background distance-redshift relation. Then the photon energy formula
gives Rz=-Psi+v_r, hence

    (partial_r+2 partial_u+Hc)Vhat = Rz.                 (T1)

This is a transport equation for a velocity potential, rather than an
algebraic identification of redshift with acceleration. It would give
Psi=-(partial_u+Hc)Vhat and J=Psi-P if its boundary information were fixed.

For c=u-2r, a characteristic has u=c+2r and eta=c+r. An integrating factor is
a(eta), so the general solution on a characteristic from radius rb is

    a(c+r)Vhat(c+2r,r,n)
      = B(c,n) + int_rb^r a(c+s) Rz(c+2s,s,n) ds,

where B(c,n) is the value of a Vhat at the chosen boundary. It is not chosen
to vanish. In particular a homogeneous ambiguity is

    delta Vhat = a(eta)^-1 F(u-2r,n),
    delta Psi = delta v_r = -a(eta)^-1 partial_c F(c,n).

Keeping P fixed while changing Phi=2P-Psi gives identical corrected radial
redshifts and Born lensing in this kinematic class. The velocity field can be
completed as grad_x delta V on the r>0 annular chart, so the full vector Euler equation holds by
construction. Continuity can determine a tracer density after an initial
tracer density is supplied. No assertion is made that these arbitrary
metrics/densities satisfy the canonical scalar, Einstein constraints or the
same common action. That is a separate decisive check, still required.

Even the scalar-force form retains a transport boundary. Applying
partial_u+Hc to the residual and using radial Euler gives

    (partial_r+2 partial_u+Hc)Psi
      = -(partial_u+Hc)Rz.                            (T2)

The commutator with the coefficient Hc is handled by the identities
partial_r Hc=-partial_eta Hc and partial_u Hc=partial_eta Hc. A guessed
local acceleration formula that drops the partial_r term is not equivalent.

The arbitrary F(c,n) family above is annular, not generally regular through
the observer. At r=0, continuity of a scalar potential requires F(eta,n) to
be angle independent on the relevant time interval; even an isotropic
nonconstant F gives a radial cusp unless its time derivative vanishes there.
The P2 example therefore does not demonstrate a globally regular, observer-
inclusive ambiguity. A boundary B placed at the observer must satisfy
regularity and the endpoint data; it is not an arbitrary angular function.

If a regular boundary is supplied at the observer r=0, the characteristic entering (u,r) reaches
it at u_b=u-2r. A finite current observing window need not contain that
boundary time. Thus a local observer value cannot simply supply the entire
remote characteristic history. For a strip u in [u0,u1], observer-boundary
coverage requires u-2r in [u0,u1]. This is a statement about this transport
construction, not an obstruction to every possible observational method.

## Source-time registration

For fixed registered endpoints and the same first-order scalar metric, the
radial null condition gives

    eta_s = u-r + delta eta_s,
    delta eta_s = 2 int_0^r P(u-s,s n) ds.

Deflection changes this travel-time result only at higher order under the
stated Born/weak-field conditions. Relative to a(u)/a(u-r), rather than to
a_o/a(eta_s), the fractional redshift perturbation is

    epsilon_bg = epsilon-Hc_s delta eta_s.

Consequently the residual constructed using a registered background radius
must include +Hc_s delta eta_s in addition to the terms in Rz above. The
observed redshift alone does not supply r. Observer clock perturbations,
source/observer trajectories and distance calibration are still external
obligations; a full-sky projection can remove observer monopole/dipole terms
but does not by itself establish the distance or source-time map.

## Constructive next discriminator

The missing function B(c,n) has an explicit origin. It may be constrained
by an independently measured transverse velocity channel, a boundary
measurement, or the complete scalar/dust/metric residuals with a single
common action. Choosing B=0, a growing mode, or a potential curve is not a
derivation. Test the full field residuals before promoting the kinematic
ambiguity to a physical counterexample. Conversely, a synthetic transport
recovery with a supplied B is only a conditional reconstruction.

## Control protocol frozen before execution

Use a(eta)=exp(2 eta) as a nonconstant positive clock scale, a smooth arbitrary
velocity-potential polynomial times exp(-2 eta), and a nontrivial angular
factor P2(cos theta). Verify T1/T2, the integrating factor, the homogeneous
family, the full radial/angular Euler components, and source-time sign using
exact symbolic operations. For the homogeneous family use F(c,n)=c^3 P2.
For a forced solution use B(c)=1+c^2 and a Rz=(c+2r)^2+r, integrate in r and
substitute back. Check a deliberately omitted partial_r term is nonzero.
These are constructed metric/tracer controls, not scalar-action solutions.
No observational files are accessed and no empirical pass/fail is defined.


The full fixed-action field constraints may further remove the annular
kinematic family. That is the separate root candidate in
METRIC_FIXED_ACTION_CLOSURE_DERIVATION_v1.md. No same-action counterexample
is asserted by this transport note.
