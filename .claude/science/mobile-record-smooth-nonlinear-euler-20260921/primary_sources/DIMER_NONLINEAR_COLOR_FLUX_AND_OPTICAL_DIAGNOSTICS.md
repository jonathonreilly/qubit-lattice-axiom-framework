# Nonlinear color flux, convex entropy, and optical diagnostics

**Status:** proposed exact flux/PDE identities with author controls and
independent check pending. **Date:** 2026-09-21.

This returns to the existing permanent-color routed process. Its homogeneous
product-law current is exact. Applying that current to a spatially varying
local-equilibrium profile gives a candidate thirteen-component conservation
law. The calculations below prove algebraic properties of that candidate;
they do not establish its inhomogeneous hydrodynamic limit from the
microscopic process. The earlier stationary Gaussian Euler theorem is a
different, smaller-amplitude result.

## 1. Exact homogeneous current and the candidate conservation law

Use the same six axis colors A, with e=+/-e_i,b=0, and eight cube colors B,
with e=0,b in {+/-1}^3. For strictly positive probabilities p_a summing to
one, put X=sum_a p_a e_a and Y=sum_a p_a b_a. Take gamma!=0 when discussing
propagating speeds; the algebraic flux identities also hold at gamma=0.
The current already derived in
`DIMER_ROUTED_RECORD_TRANSPORT.md` is

    F_a(p)=gamma p_a[e_a cross Y+X cross b_a-2 X cross Y]. (1)

All spatial components use this same vector formula; sum_a F_a=0. The
candidate continuum equation is

    partial_t p_a + div F_a(p)=0.                    (2)

No assumption that arbitrary microscopic profiles remain product measures
is made. A proof of local replacement, control of entropy, and a smooth-time
hydrodynamic limit for the routed process would still be required to identify
(2) with a microscopic limit. Shocks or positive-density fluctuations are
not covered by the stationary linear theorem.

## 2. A complete moment representation

Define D_i=sum_A p_a e_(a,i)^2, so rho_A=sum_i D_i and rho_B=1-rho_A.
For i<j set Z_ij=sum_B p_a b_i b_j, and w=sum_B p_a b_1 b_2 b_3. Along
with the six means X,Y, the three D_i, three Z_ij and w are thirteen
independent real coordinates on the probability simplex. The exact inverse is

    p_(A,i,sigma)=(D_i+sigma X_i)/2,
    p_(B,b)=[rho_B+b.Y+sum_(i<j) b_i b_j Z_ij
                         +b_1 b_2 b_3 w]/8.        (3)

Positivity means precisely that all fourteen numerators in (3) are positive.
No closure approximation is used to obtain these coordinates. Set the
symmetric matrix M_B by (M_B)_ii=rho_B and (M_B)_ij=Z_ij for i!=j, and let
r=(Z_23,Z_13,Z_12). For each variable below its vector flux is exactly

    F_(D_i)=gamma[X_i e_i cross Y-2D_i X cross Y],
    F_(X_i)=gamma[D_i e_i cross Y-2X_i X cross Y],
    F_(Y_i)=gamma[X cross (M_B e_i)-2Y_i X cross Y],
    F_(Z_ij)=gamma[X cross (Y_j e_i+Y_i e_j+w e_k)
                                      -2Z_ij X cross Y],
    F_w=gamma[X cross r-2w X cross Y],               (4)

where k is the third index in the Z_ij line. In particular,

    F_(rho_A)=gamma(1-2rho_A)X cross Y.              (5)

Thus the seven additional population coordinates cannot generally be held
fixed in a finite-amplitude version of the wave equations. At an orbit-
isotropic rest profile X=Y=Z=w=0, D and Z have quadratic sources in
the vector fields; w is driven through the generated Z variables at the next
order. This order statement concerns that background, not arbitrary w or Z.

## 3. Convex entropy and real characteristic speeds

For a spatial direction n define a real symmetric fourteen-by-fourteen
matrix

    K^(n)_ab=n.[e_a cross b_b+e_b cross b_a].

Let v=Kp, M=p^T Kp, eta(p)=sum_a p_a log p_a. The directional flux from
(1) is gamma[diag(p)Kp-pM]. On the tangent space sum_a u_a=0 its Jacobian is
the restriction of

    A=gamma[diag(v-M)+diag(p)K-2p v^T].             (6)

The Hessian of eta is diag(1/p_a). For tangent vectors u,z,

    u^T Hess(eta) A z
       =gamma u^T[diag((v-M)/p)+K]z,                (7)

because the last term contains u^T 1=0. The right matrix is symmetric, and
the restricted entropy Hessian is positive definite for p_a>0. Hence every
directional Jacobian on the thirteen-dimensional simplex tangent space is
similar to a real symmetric matrix: all characteristic speeds are real and
the principal part is symmetrizable. This is an algebraic property on the
interior simplex, not a proof of global smooth solutions or shock selection.

An entropy flux can also be written explicitly. For each spatial component,
or equivalently after contraction with n, set

    q_eta^(n)=gamma[sum_a p_a log p_a (Kp)_a
                       -eta M-M/2].               (8)

Differentiating (8) along a tangent variation gives
grad eta dot A times that variation. Therefore every smooth interior
solution of (2) obeys partial_t eta+div q_eta=0. The minus-M/2 term is
necessary. Convexity and symmetrization do not imply that the microscopic
entropy production or a nonsmooth entropy solution has already been derived.

## 4. Rest profiles and a precise birefringence test

At a constant rest profile X=Y=0, let D=diag(D_1,D_2,D_3) and B=M_B.
Strictly positive color probabilities make D and B positive definite. The
six vector perturbations close linearly:

    X_dot=gamma D curl Y,
    Y_dot=-gamma B curl X.                          (9)

They conserve the positive quadratic integral
[X^T D^-1 X+Y^T B^-1 Y]/2. Their conserved divergence combinations are
div(D^-1 X) and div(B^-1 Y); assigning the unweighted divergences the same
role would generally be wrong at anisotropic rest profiles.

For a wavevector along e_1, the two squared propagation speeds are

    c_+/-^2 = (gamma^2/2)[rho_B(D_2+D_3)
       +/- sqrt(rho_B^2(D_2-D_3)^2+4D_2D_3 Z_23^2)]. (10)

This follows by restricting -D[e_1 cross]B[e_1 cross] to its transverse
two-by-two matrix. Analogous formulas hold cyclically. Positivity implies
both speeds are positive. Their equality on this axis holds exactly when
D_2=D_3 and Z_23=0. Equality on all three coordinate axes consequently holds
exactly when

    D=(rho_A/3)I,              B=rho_B I.            (11)

Under (11) the two speeds agree in every direction, with
c=|gamma|sqrt(rho_A rho_B/3), as in the stationary wave theorem. This is
an exact criterion within the stated rest-profile family; it is not a
theorem against different record laws, other encodings or general metrics.

For a concrete positive profile take D_i=1/7, rho_B=4/7, Z_23=1/14 and
Z_12=Z_13=w=0. Equation (3) gives positive probabilities. Along e_1 the two
squared speeds are gamma^2/14 and 9gamma^2/98, whereas the e_2 and e_3 axes
have coincident squared speeds 4gamma^2/49. Thus positive homogeneous
stationarity alone does not select the common isotropic optical branch.

Conversely, a nonzero w with X=Y=Z=0 and D_i=rho_A/3 does not alter (9).
For example w=1/14 at rho_A=3/7,rho_B=4/7 is still strictly positive and has
the same six-vector linear optical spectrum as w=0. It changes higher color
moments and other components of the full population response. Optical
isotropy of these six means is therefore not full isotropy of the color law.

## 5. Use in the campaign

Equations (3)-(8) provide a finite, explicit nonlinear continuation of the
exact homogeneous current, with a strictly convex entropy and real
characteristic speeds. Equations (10)-(11) supply a diagnostic for which
rest populations retain the common two-polarization branch. They make
finite-amplitude feedback and anisotropy testable without assigning a
gravitational interpretation to every coefficient change.

The missing microscopic inhomogeneous-limit proof is explicit. No quantum
generator, Born readout, matter coupling, spacetime metric, or TOE follows
from this candidate PDE. The useful next test is whether the actual routed
process follows these nonlinear currents for controlled slowly varying
profiles before shocks, and which preparation/dynamics select the required
background and perturbation regime.
