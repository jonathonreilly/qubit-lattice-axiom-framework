# Independent derivation for the frozen expansion block

Reviewer: direct_field_check. This checks the supplied model and observation map;
it introduces no new candidate or empirical fit. Units are c=1. Let H denote H_*,
v=dot(phi), zeta=alpha.phi, A=exp(zeta), and a=alpha^T K^-1 alpha. K is constant
positive definite, alpha is constant, and G_*>0. Densities in the Einstein field
equations are Einstein-frame densities.

For the supplied scalar action with kinetic term -2 K_AB partial(phi^A)
partial(phi^B) inside the Einstein-action normalization, the homogeneous scalar
energy is v^T K v/(8 pi G_*), with equal energy density and pressure. Dust has
T_*=-rho_m and radiation has zero trace. With the supplied mostly-plus metric,
Box(phi)=-ddot(phi)-3H dot(phi). Thus the scalar equation
Box(phi)=-4 pi G_* K^-1 alpha T_* implies

    dot(v)=-3Hv-4 pi G_* K^-1 alpha rho_m.

At fixed physical particle rest mass, the Einstein particle mass is proportional
to A. Conserved comoving particle number gives rho_m proportional to A R_*^-3;
therefore dot(rho_m)=(-3H+dot(zeta))rho_m. Radiation obeys rho_r proportional to
R_*^-4. These signs are mutually required: differentiating

    3H^2=8 pi G_*(rho_m+rho_r)+v^T K v

cancels the matter/scalar exchange terms and gives
dot(H)=-4 pi G_*(rho_m+4rho_r/3)-v^T K v. Reversing just the scalar source sign
leaves a nonzero exchange defect. The independent symbolic control checks this
without using the author helper functions.

The physical clock is dt_J=A dt_* and R_J=A R_*. Direct differentiation gives

    H_J=(H+dot(zeta))/A,
    dot_J(H_J)=A^-2[dot(H)+ddot(zeta)-H dot(zeta)-dot(zeta)^2].

Consequently

    q_J=-[dot(H)+H^2+H dot(zeta)+ddot(zeta)]/(H+dot(zeta))^2.

Write y=dot(zeta)/H and fractions m,r,s for matter, radiation and scalar kinetic
energy. Then m+r+s=1, q_* = m/2+r+2s, and ddot(zeta)=-3H^2 y-4 pi G_* a rho_m.
The physical deceleration follows:

    (1+y)^2 q_J = 1/2+3a/2+2y+(3/2)(1-a)s+(1/2)(1-3a)r.

This is the expanded form of the author's equation (2). Cauchy-Schwarz in the
positive K inner product gives y^2 <= 3as. It uses the complete scalar velocity,
including its component perpendicular to K^-1 alpha. In particular, a=0 implies
alpha=0 and y=0 but does not imply s=0.

For 0<a<1/3, set b=(1+a)/[2(1-a)] and s=y^2/(3a)+s_perp, with s_perp>=0. The
polynomial coefficients of (1+y)^2(q_J-b), after this substitution, are

    coefficient of y^2: (1-3a)/[2a(1-a)],
    coefficient of y:   (1-3a)/(1-a),
    constant:           a(1-3a)/[2(1-a)]
                        +(3/2)(1-a)s_perp+(1/2)(1-3a)r.

The first three terms complete the square (y+a)^2. Every remaining term is
nonnegative. Also |y|<=sqrt(3as)<=sqrt(3a)<1, so multiplication or division by
(1+y)^2 does not hide a contracting or zero-H_J branch. At a=0 the direct result
q_J=1/2+3s/2+r/2 supplies the limiting inequality. The frozen weak-coupling range
is a supplied earlier calibration boundary; the present data do not determine it.

Sharpness is dynamical. Equality at positive a requires y=-a, r=0, s=a/3 and
v/H=-K^-1 alpha. The equation for x=v/H is

    x'=(q_*-2)x-(3/2)K^-1 alpha m,  prime=d/d ln(R_*).

At the stated equality values q_*=(1+a)/2 and m=1-a/3, the right side vanishes.
Along this solution

    A proportional to exp(-aN),
    H_* proportional to exp[-(3+a)N/2],
    dt_J/dN proportional to exp[(3-a)N/2],
    R_J proportional to exp[(1-a)N].

Eliminating N gives R_J proportional to (t_J-t_origin)^[2(1-a)/(3-a)] and the
claimed q_J=b. No stability or global-attractor statement is required. The
Einstein H exponent (3+a)/2 must be distinguished from the physical H_J exponent;
my first added equality oracle confused them. Its preserved eight failed checks
are reviewer error, not an author error. The corrected oracle agrees with the
independent numerical evolution.

The independent evolution uses scalar momenta and fluid densities rather than
the author's H-normalized velocities and evolved log(H). Choosing 8 pi G_*=1,
H is reconstructed from the constraint at every evaluation. With N as the
integration coordinate, its state equations are

    phi'=v/H,
    v'=-3v-alpha rho_m/(2H),
    rho_m'=(-3+alpha.v/H)rho_m,
    rho_r'=-4rho_r,
    t_J'=exp(alpha.phi)/H,
    H=sqrt[(rho_m+rho_r+v.v)/3] for the two-field K=I fixtures.

A Radau implicit integrator independently reproduces all six fixtures and all
108 recorded author states across the two refinements. The dust and radiation
first integrals are checked separately. Physical acceleration is computed from
dot(H), dot(zeta) and ddot(zeta), rather than calling the author's q function.
Additional exact rational tests use a non-diagonal positive three-field K.

For the optical result, the assumptions are flat physical geometry, transparency,
distance duality and a bound q_J(z)>=q_c throughout [0,z], not only at z=0. Set
w=(1+z)^(-1-q_c), j=(1+z)^(1+q_c)/H_J and B=integral_0^z w. Then

    d ln(j)/dz=(q_c-q_J)/(1+z)<=0,
    T(z)=(integral_0^z w(u)j(u)du)/B(z),
    T'(z)=w(z)[j(z)-T(z)]/B(z)<=0.

An arbitrary normalization of H multiplies T by a positive constant, preserving
the ordering. In the supplied observation convention the heliocentric factor
cancels in the residual to the comparison curve, leaving an unknown constant
plus 5 log10 T(zHD). Disjoint ordered redshift groups with positive within-group
weights therefore have high-minus-low mean <=0. This statement concerns the
model's mean, not an absolute bound on a noisy realization. Negative weights
could violate the implication; an explicit synthetic example is preserved.

The statistical transfer formula can also be derived without using an intercept
posterior. Let L=C_LL, T=C_TT, F=C_TL, Q=L^-1,

    u=Q1/(1^T Q1), B=FQ, v=1-B1, K_pred=B+v u^T.

Partitioning observations as calibration then transfer, the residual operator
is W=[-K_pred,I]. Since K_pred 1=1, W removes the unknown intercept exactly.
For d=m-g, the transfer residual is Wd and its covariance is

    W C W^T = T-FQF^T+(u^T L u) v v^T.

The last coefficient is 1/(1^T Q1). This reproduces the flat-prior marginalization
formula. It also shows why both cross-covariance and intercept uncertainty must
remain. The covariance between the calibration residual (I-1u^T)d_L and Wd
vanishes. Under the stipulated fixed Gaussian summary model, calibration and
transfer residual quadratic forms therefore have ranks |L|-1 and |T|. A global
whitened intercept projection yields their sum, but is not needed to construct
the reserved prediction and does not refit its intercept on transfer data.

The contrast variance can be evaluated independently as

    Var(mean_H-mean_L)=sum(C_HH)/n_H^2+sum(C_LL)/n_L^2
                       -2 sum(C_HL)/(n_H n_L).

This retains duplicate-light-curve correlations and systematic covariances.
It is equivalent to c^T C c with sum(c)=0. For an added standardized-magnitude
term beta log10(1+z), the predicted contrast increases by beta times the
high-minus-low log-redshift mean. Subtracting that term from the observations
therefore changes the reported contrast with the minus sign used by the runner.
A free beta removes this one scalar diagnostic; it neither establishes an actual
luminosity law nor removes all transfer residuals by theorem.
