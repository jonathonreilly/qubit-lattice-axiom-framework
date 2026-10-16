# Tidal scalar readout with expansion retained

Root candidate before code. Status: conditional-support. The new load-bearing
obligation is the frozen-background approximation in the physical scalar
readout. Here the background expansion is kept exactly at first perturbative
order. This does not supply actual tidal data or select the scalar action.

## Exact linear curvature on the supplied physical background

Use physical cosmic time t and spatially flat Newtonian-gauge metric

    dsJ^2=-(1+2Psi)dt^2+a(t)^2(1-2Phi)delta_ij dx^i dx^j.

The observer is the unit normal to these slices; its orthonormal tetrad is
e0=(1-Psi)partial_t, ei=(1+Phi)partial_i/a at linear order. The recorded
quantity here is Eij=R_hat0_hat i_hat0_hat j in the same Riemann convention as
the frozen readout. Motion relative to that observer requires a separately
calibrated tetrad transformation. Let H=a_dot/a and Q=H_dot+H^2. The
unperturbed value is -Q delta_ij. A direct curvature calculation should give

    delta Eij = (partial_i partial_j Psi)/a^2
          +[Phi_ddot+2H Phi_dot+H Psi_dot+2Q Psi]delta_ij.

An independent analytic route uses lapse N=1+Psi and the isotropic expansion
of the normal congruence h=H-Phi_dot-H Psi. Its electric curvature is
-(N^-1 h_dot+h^2)delta_ij plus the orthonormal Hessian of N. This gives the
same expression. It is linear in potentials but has no short-wavelength or
slow-background approximation. Scalar Fourier sectors and normal-observer
curvature are stipulated; total cosmological curvature is not naively called
a free gravitational wave.

For one comoving spatial mode exp(ikz), with constant nonzero k,

    T=delta Exx=delta Eyy,
    L=delta Ezz=T-(k^2/a^2)Psi,
    Psi=(a^2/k^2)(T-L).

Thus the lapse potential follows algebraically from the anisotropic tidal
part at each time, even though the transverse part mixes lapse and spatial
potential through the changing background.

## A differential scalar readout and its actual kernel

In the specified conformal single-scalar/no-linear-anisotropic-stress sector,
J=(Psi-Phi)/2=delta ln A in Newtonian gauge. Define operators

    M=partial_t^2+2H partial_t,
    Aop=partial_t^2+3H partial_t+2Q.

The exact linear identity is

    M J = (Aop Psi-T)/2.

Two tidal histories determine this derivative of J, not J itself. On a
connected time interval the kernel is

    Jkernel=c1+c2 integral^t a(s)^(-2) ds.

The integration constants may depend on the spatial Fourier label. They must
be supplied by initial/boundary data or another physical channel; they are
not retired assumptions. At the level of the metric observation map,
Psi=0 and Phi=-2 Jkernel have zero delta Eij but can have nonzero spatial
curvature. This is an observation-map example, not a claim that arbitrary
kernel perturbations satisfy the scalar and Einstein field equations.
Imposing those equations to eliminate a kernel must retain their premises.

## Primitive-record weak identity

For a real smooth test lambda with lambda=lambda_dot=0 at time endpoints,
using the flat dt pairing,

    Mdagger lambda=lambda_ddot-2(H lambda)_dot,
    Adagger lambda=lambda_ddot-3(H lambda)_dot+2Q lambda.

Integration by parts yields

    int (Mdagger lambda) J dt = int WT T+WL L dt,
    WT=(a^2/k^2)(Adagger lambda)/2-lambda/2,
    WL=-(a^2/k^2)(Adagger lambda)/2.

Only the test and supplied background are differentiated. For deterministic
primitive error bounds |delta T|<=epsT and |delta L|<=epsL the moment error
is at most epsT int|WT|dt+epsL int|WL|dt. Background, wavenumber, tetrad and
relative calibration errors are separate and cannot be folded into zero.
The formula is an exact weak measurement of filtered J under its premises;
it does not identify its two integration constants or a scalar principal
speed by itself. Signed/complex Fourier amplitudes retain phase; intensity
data are not silently substituted.

## Explicit frozen-inverse remainder

To compare with the earlier frozen formula, use a chosen nonzero constant
temporal carrier omega, Phi=F(t)exp(-i omega t), Psi=G(t)exp(-i omega t).
With instantaneous p=k/a define

    Jfrozen=[(1+p^2/omega^2)T-L]/(2p^2).

Then

    exp(i omega t)(Jfrozen-J)
      =[F_ddot-2i omega F_dot+2H(F_dot-i omega F)
        +H(G_dot-i omega G)+2Q G]/(2omega^2).

This is an exact first-order remainder identity for this carrier/envelope
decomposition. Taking absolute values term by term gives a conditional bound
from supplied envelope and background derivative bounds. It is not small
merely because tensors travel at light speed. In particular a nonzero common
potential contributes through F and G. The exact weak map avoids this
frozen-background approximation, while retaining its own observer,
calibration, spatial-mode and boundary contracts.

## Predeclared controls

Derive coordinate R0i0j directly from the perturbed metric with a formal
epsilon, expand the inverse metric and tetrad consistently to first order,
and compare with the analytic formula. Check the differential identity,
two independent kernel functions, a varying-background polynomial fixture,
weak integration by parts and an explicit nonzero frozen-inverse remainder.
The kernel example is not a full action solution. No numerical observations,
selected scalar speed or action equation are used as expected outputs.
