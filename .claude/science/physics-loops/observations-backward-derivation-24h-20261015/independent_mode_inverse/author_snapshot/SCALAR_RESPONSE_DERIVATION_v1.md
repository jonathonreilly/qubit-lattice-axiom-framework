# From metric and matter records to a scalar response

Root's personal support derivation, 2026-10-16. This follows the matter-clock
compatibility calculation. No observations are fitted, no new force is detected,
and the canonical conformal action remains a premise. These standard
perturbation and source-elimination identities are kept commits-only.

## Primitive observation and conditional class

Galaxy positions, redshifts, shapes, velocities and local clocks are instrument
records. A reconstructed gravitational slip or growth function already uses
geometry, tracer/selection, source and calibration assumptions. The pinned
Amendola et al.1210.0439v2 analysis explicitly retains these conditions and
normalization/initial-condition limitations. We therefore derive the equations
for such a reconstruction before identifying any fitted pole with a potential
curvature. Nothing below declares those functions measured in this campaign.

Use the same action as MATTER_CLOCK_DERIVATION_v1.md: one canonical scalar,
Einstein coefficient M^2/2, universally conformal pressureless particles with
mass m A(phi), and gJ=A^2 gE. The spatially flat homogeneous solution satisfies
both Einstein equations, scalar KG and bare-number conservation. Let

    v=dot(phi), alpha=A_phi/A, r=A rho,
    Fforce=V_phi+rho A_phi=-dot(v)-3H v,
    mu=V_phiphi+rho A_phiphi,

where field derivatives hold bare proper density rho fixed. All time derivatives
in the next sections use Einstein proper background time. These definitions
do not assume a density minimum. Background quantities are real and regular,
with M,A>0. We work at nonzero comoving Fourier wave number and first order
in scalar perturbations. No quasistatic approximation is made initially.

In Newtonian gauge write

    dsE^2=-(1+2Psi)dt^2+a^2(1-2Phi)dx^2,
    u=delta phi, S=A delta rho, K2=k_com^2/a^2.

Delta rho is the perturbation of the bare proper number/mass density in this
gauge, not a coordinate-volume density. There is no anisotropic stress from
canonical scalar plus dust at this order, so Psi=Phi=P for nonzero modes.

## Direct action and constraint equations

Expanding the metric volume and inverse gives

    sqrt(-g)=a^3(1+Psi-3Phi), g^00=-1+2Psi,
    delta(Box phi)=-ddot(u)-3H dot(u)-K2 u
       +v[dot(Psi)+3dot(Phi)]+2Psi[dot(v)+3Hv].

The scalar equation Box(phi)-V_phi-rho A_phi=0 therefore gives exactly

    ddot(u)+3H dot(u)+(K2+mu)u
      =-alpha S+4v dot(P)-2Fforce P.                    (1)

The energy perturbation is

    delta epsilon=S+v dot(u)-v^2 P+Fforce u.

This includes delta r=S+alpha r u. The ADM Hamiltonian constraint provides
an independent geometric route: the perturbed spatial curvature is
delta R3=4 nabla^2 Phi/a^2, and the perturbation of
Ktrace^2-Kij K^ij is -12H(dot(Phi)+H Psi). Consequently

    K2 P+3H[dot(P)+H P]
       =-[S+v dot(u)-v^2 P+Fforce u]/(2M^2).            (2)

The signs here use Fourier nabla^2=-k_com^2. Neglecting the lapse terms or
identifying delta r with S changes the mass that appears after elimination.

For clarity, (1),(2) alone are not the full mode-evolution system. Define a
dust velocity potential U by physical peculiar velocity vpec_i=partial_i U/a,
and theta=div(vpec)/a=-K2 U. Bare-number conservation and the particle action
give

    delta=delta rho/rho=S/r,
    dot(delta)=3dot(P)-theta,
    dot(theta)+(2H+alpha v)theta=K2(P+alpha u).          (3)

The friction term follows by differentiating the particle momentum
m A a^2 dot(x_i); it includes dot(A)/A=alpha v. The momentum constraint is

    dot(P)+H P=[v u+r theta/K2]/(2M^2).                 (4)

It follows from the ADM momentum divergence and
delta T^0_i=partial_i(r U-v u). The remaining Einstein spatial equation,
or equivalently constraint preservation with the full matter equations, must
also hold. The source-elimination identity below is a necessary identity of
that complete system, not a replacement dispersion relation or proof of mode
existence. Initial perturbation states and dust response have not disappeared.

## Eliminating the unmeasured bare-density source

Solving (2) for S and substituting in (1), without dropping derivatives, gives

    ddot(u)+(3H-alpha v)dot(u)+(K2+mu-alpha Fforce)u
      =2M^2 alpha K2 P+(6M^2 alpha H+4v)dot(P)
       +(6M^2 alpha H^2-alpha v^2-2Fforce)P.            (5)

Thus the coefficient mu of the fixed-bare-density scalar equation is not
automatically the fitted denominator of a metric/matter response. The identity
contains dust elimination, metric mixing, off-minimum force and time
derivatives. A pole of the complete time-dependent system requires the other
equations and defined boundary/initial conditions; it cannot be read merely
from one algebraic coefficient.

Conformal transformation with background d tau=A dt yields

    PsiJ=P+alpha u, PhiJ=P-alpha u.

Where P!=0, the reconstructed ratio is

    Cobs=(PsiJ-PhiJ)/(PsiJ+PhiJ)=alpha u/P.

Its Weyl denominator is 2P, but a lensing record is a line-of-sight weighted
quantity with its own inversion. At alpha=0, this ratio can vanish despite a
propagating scalar, and it cannot be divided by alpha to recover u.

Set b=M alpha and define

    B=6b^2 H^2-alpha^2 v^2-2alpha Fforce,
    T=(6b^2 H+4alpha v)dot(P)/P
       -(alpha/P)[ddot(u)+(3H-alpha v)dot(u)].

Equation (5) gives the exact identity

    (K2+mu-alpha Fforce) Cobs=2b^2 K2+B+T.              (6)

Neither mu>0 nor K2 large alone supplies a quantitative bound on T. The
frequencies, mode amplitudes and time evolution must be controlled. The
frequently used expression 2b^2 K2/(K2+mu) requires the omitted B,T and
alpha Fforce to be negligible in a specified error budget. In particular,

    (K2+mu) Cobs-2b^2 K2=alpha Fforce Cobs+B+T.         (7)

If |K2+mu|>=d>0 and separately registered bounds on those terms exist, then
the difference from that expression is at most
(|alpha Fforce| |Cobs|+|B|+|T|)/d. This is conditional error propagation;
the campaign does not have those bounds for actual cosmological data.

## What the matter-clock inverse would require

Use h,x,b,kappa from MATTER_CLOCK_DERIVATION_v1.md. Then

    K2=A^2 kJ^2, mu=A^2 kappa,
    Fforce/A^2=-M[x'+3h x-2b x^2],
    (mu-alpha Fforce)/A^2
       =kappa+b x'+3b h x-2b^2 x^2=:d_eff,
    B/A^2=2b x'+6b h x+6b^2 h^2-12b^3 h x
                       +(6b^4-5b^2)x^2=:s_eff.        (8)

Even if the derivative remainder T could be neglected, the response is

    Cobs=(2b^2 kJ^2+s_eff)/(kJ^2+d_eff),

not generally the expression obtained by replacing mu with A^2 kappa in a
bare Yukawa law. Both extra coefficients depend on the scalar history being
reconstructed. A finite set of response amplitudes could constrain these
combinations; it does not independently supply kappa without further work.
The exact remainder T/A^2 must still be retained when justified derivative
control is absent. No quasistatic or frozen-background fit is performed here.

This identifies a useful next research route: combine matter-clock background
compatibility with source/velocity/lensing response constraints at the equation
level, solving for the compatible histories jointly. Preserve initial modes,
normalizations and observation operators. Do not provide an assumed scalar
state, set force to zero, or install an empirical pole as kappa to close the
inverse. The present result eliminates an unjustified identification, while
the action class, response extraction, absolute normalization and environmental
correspondence remain open assumptions.
