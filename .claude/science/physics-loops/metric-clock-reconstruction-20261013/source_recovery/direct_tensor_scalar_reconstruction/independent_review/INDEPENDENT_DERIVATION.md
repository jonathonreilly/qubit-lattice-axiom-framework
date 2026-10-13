# Independent derivation for the frozen tensor-scalar block

This is a checker derivation of the supplied construction, not a new primary
theory or a formal audit. I use signature (-+++), x0=ct, and the author's
normalization of G_* and dimensionless scalar fields. All statements below
remain conditional on the given matter action and weak-source assumptions.

## Variation and exchange

Write beta=alpha_A phi^A, A=exp(beta), and v=K^{-1}alpha. Holding the
Einstein metric fixed gives delta gtilde=2 gtilde alpha_A delta phi^A. With
T_*^{mu nu}=2c (delta S_m/delta g_*mu nu)/sqrt(-g_*), this implies

    delta S_m = integral sqrt(-g_*) alpha_A T_* delta phi^A / c.

The scalar action contributes

    delta S_phi = c^3/(4 pi G_*) integral sqrt(-g_*)
                 K_AB Box_* phi^B delta phi^A.

Its Euler equation is therefore
Box_* phi^A=-(4 pi G_*/c^4) v^A T_*. Varying the inverse metric in the
kinetic term gives precisely twice the usual normalized scalar gradient
stress on the Einstein-equation side:

    G_*mu nu = 2 K_AB phi^A_,mu phi^B_,nu
               -g_*mu nu K_AB phi^A_,rho phi^B,^rho
               +(8 pi G_*/c^4) T_*mu nu.

The divergence of its scalar part is 2 K_AB(Box phi^A) phi^B_,nu. Substitution
of the scalar equation into Bianchi's identity gives
nabla_*mu T_*^{mu nu}=alpha_A T_* partial^nu phi^A, with the sign in the
note. Independently, the matter stress transformation is
T_*^{mu nu}=A^6 Ttilde^{mu nu} and T_*=A^4 Ttilde. Inserting the conformal
connection difference into nabla_tilde Ttilde=0 gives that same exchange
identity. Matter alone is not a conserved flat or Einstein-frame source.

K>0 allows a constant change of variables making the scalar kinetic norm
Euclidean. The transformed charge has squared norm a=alpha^T K^{-1}alpha.
Under phi=S chi, direct substitution gives
(S^T alpha)^T(S^T K S)^{-1}(S^T alpha)=a. Thus a>=0, with equality only
for alpha=0. This proof is independent of scalar count and of the signs of
individual charge components. No such conclusion is supplied for an
indefinite K or nonuniversal charges.

## Full metric symbol and physical energy

For a nonzero covector k, let b_mu=h_mu nu k^nu and h=eta^{mu nu}h_mu nu.
The contracted linear Einstein operator has quadratic form

    Q(h)=h_mu nu G_L^{mu nu}(h)
        =1/2 [k^2(h_mu nu h^{mu nu}-h^2)
              -2 b_mu b^mu+2 h k^mu k^nu h_mu nu].

I formed the ten-variable Hessian of this form, rather than reusing the
author's component Einstein operator. Four independent columns
h_mu nu=k_mu xi_nu+k_nu xi_mu lie in its kernel. The off-null kernel is
exactly these four directions; on a nonzero null covector it has two further
directions represented by spatial transverse, trace-free plus and cross
tensors. The independent exact controls use non-axis null covectors
(-13,3,4,12) and (13,3,4,12), a generic off-null covector, a purely temporal
one and a purely spatial one. Their ranks are 4,4,6,6,6, with gauge rank 4.
Lorentz covariance and the usual transverse basis extend the classification;
these finite ranks are checks rather than its sole proof. k=0 is excluded.

Expanding Einstein-Hilbert to second order about a vacuum solution, with
boundary terms removed, gives -c^3/(32 pi G_*) integral h:G_L[h]. On TT
fields G_L=-Box h/2, hence

    S_TT = c^2/(64 pi G_*) integral dt d^3x
           [h_dot:h_dot-c^2 grad h:grad h].

The TT Hamiltonian has the same positive coefficient multiplying the sum
of the two squares. The scalar action is c^2/(8 pi G_*) integral
[phi_dot^T K phi_dot-c^2 grad phi^T K grad phi], with positive Hamiltonian
for K>0. These are positive energies on the physical vacuum modes, not a
positive form on all ten gauge-dependent metric components or a theorem
about full nonlinear matter binding energy.

The resulting outward wave fluxes are c^3 h_dot:h_dot/(32 pi G_*) and
c^3 phi_dot^T K phi_dot/(4 pi G_*). Both massless sectors have the Einstein
null characteristic. Universally coupled ordinary vacuum Maxwell theory
has the same geometric-optics cone because its metric is conformal. This
does not establish arbitrary microscopic matter dispersion or lattice closure.

## Static force and optical response

For nonrelativistic matter T_*=-rho c^2+..., so
Delta phi^A=(4 pi G_*/c^2) v^A rho. The decaying point-source solution is
phi^A=-G_* M v^A/(c^2 r)=v^A U_*/c^2, not its negative. Combining
2 beta eta with the Einstein metric perturbation yields

    gtilde00=-1-2(1+a)U_*/c^2,
    gtildeij=[1-2(1-a)U_*/c^2]deltaij.

The probe acceleration is -grad[(1+a)U_*], fixing G_N=G_*(1+a). The spatial
to temporal weak-potential ratio is gamma=(1-a)/(1+a), and the scalar share
of that particular attractive force is a/(1+a)=(1-gamma)/2.

The static optical index sqrt(gtilde_spatial/(-gtilde00)) is
1-2U_*/c^2 at this order. Consequently the straight-ray integral is
4G_*M/(c^2 b), equivalently 2(1+gamma)G_N M/(c^2 b). The conformal scalar
changes the massive-body calibration but cancels from this leading null
path. All powers of c are consistent: potentials have units of speed squared,
phi and h are dimensionless, and the angle is dimensionless.

## Why the combined Newtonian stress is necessary

Let U=U_N satisfy Delta U=4 pi G_N rho, with force density -rho grad U.
The tensor

    sigma_ij=[U_,i U_,j-deltaij |grad U|^2/2]/(4 pi G_N)

has divergence rho U_,i. Adding it to the dust momentum flux produces the
Newtonian spatial part of a conserved effective source. The scalar near-zone
stress contributes a times the Einstein Newtonian term expressed in U_*;
their sum is (1+a)/(4 pi G_*) times that quadratic gradient expression.
Since U_N=(1+a)U_* and G_N=(1+a)G_*, it equals sigma above.

There is an independent useful interaction integral. Fourier transformation
of the product of two Newtonian gradients uses the inverse-k^4 kernel
-r/(8 pi). Differentiating it yields

    integral U1_,i U2_,j d^3x
       =2 pi G_N^2 m1 m2 (deltaij/r-r_i r_j/r^3).

Substitution into the cross terms of sigma cancels the isotropic part and
gives integral sigma_ij=-G_N m1 m2 r_i r_j/r^3. No singular self term was
included in this calculation. Together with the continuity equation and
the particle force law, it gives integral tau_ij=I_ij''/2. Its integration
by parts boundary term vanishes for the isolated Newtonian exterior.

The outgoing linearized metric solution therefore gives
h_TT=2G_* Lambda(I'')/(c^4 R). Bare dust alone does not obey the required
Ward identity. For a circular pair its oscillatory stress is half the total
oscillatory stress: omitting sigma halves the tensor amplitude and quarters
the tensor power. Reversing sigma's sign cancels the circular tensor harmonic.
Both consequences were calculated independently from discrete orbital Fourier
coefficients, in addition to the analytic Green-kernel derivation.

This is a conserved leading effective source, not a claim that the exact
particle stress is separately divergence-free, or that a point particle's
self interaction has been solved. The stated self-term subtraction and
zero residual body-dependent sensitivity are substantive extra source limits.

## Circular scalar ordering and physical waveform

With Box=-c^{-2}partial_t^2+Delta, the retarded leading density solution is

    phi^A=-G_* v^A/(c^2 R)
          [M+n_i D_i'/c+n_i n_j I_ij''/(2c^2)+...].

The leading mass monopole is constant; the leading mass dipole vanishes in
the Newtonian COM for universal weak charges. Corrections to the integrated
scalar source can be of quadrupole order. For the conservative circular
system their rotationally invariant monopole is constant by helical symmetry;
the adiabatic radiation-reaction change is beyond the retained order.
A source dipole correction of relative order v^2/c^2 enters its wave with an
extra v/c and is beyond the leading quadrupole. Source corrections to the
quadrupole itself are higher order as well.

This argument justifies the displayed sourced field
phi_rad^A=-G_* v^A n_i n_j I_ij''/(2c^4 R) for this circular family. It
cannot be promoted to generic eccentric motion: an orbital source monopole
may then vary at the retained order. Nor can the leading dipole be discarded
when residual body charges differ. Constant self masses alone do not imply
zero residual charge sensitivity. Independently specified incoming/free
scalar waves are not part of this sourced waveform.

Writing zeta=alpha.phi_rad, linear curvature of h_TT+2 zeta eta gives
c^2 R_0i0j=-h_TTij''/2-zeta''(deltaij-n_i n_j). I checked it by constructing
all relevant second-derivative components of Riemann in two non-axis frames.
Changing the sign of the conformal time perturbation creates a spurious
longitudinal tide and is detected. The small free-arm limit follows by
integrating geodesic deviation, giving h_TT projected on the arm divided by
two plus zeta times its transverse squared length.

For a circular orbit the plus/cross patterns follow by contracting I'' with
p p-q q and p q. The scalar metric amplitude is 2 alpha.phi_rad, so it has
two charge insertions and is proportional to a. The scalar energy instead
contains v^T K v=a and is linear in a. Confusing these two facts would give
the wrong weak-coupling behavior. The source family has two tensor waveform
types and one sourced breathing type, despite there being n propagating
scalar fields in the vacuum theory. Face-on suppression is geometric and
does not remove those fields.

## Power normalization and the linked identity

For trace-free S, direct projector contraction reduces the pointwise TT norm
to S:S-2|Sn|^2+(n^T S n)^2/2. Rotational moments
<n_i n_j>=deltaij/3 and the fourth moment then give

    integral |Lambda(S)|^2 dOmega = (8 pi/5) S:S,
    integral (n^T S n)^2 dOmega = (8 pi/15) S:S.

I also evaluated these exactly using rational monomial sphere averages for
a non-axis trace-free matrix. They imply
P_T=G_* I''':I'''/(5c^5), P_S=G_* a I''':I'''/(30c^5).
For the circular source I''':I'''=32 mu^2 r_0^4 Omega^6. Both powers have
units of energy per time. Tensor and scalar quadratic actions are diagonal;
this absence of inter-sector interference does not discard terms within a
single scalar channel for a different source family.

Comparing with GR on the same specified leading trajectory and G_N gives

    (P_T+P_S)/P_GR = (1+a/6)/(1+a)
                  =1-5[a/(1+a)]/6=(7+5 gamma)/12.

The denominator is essential; comparing at fixed G_* instead would answer a
different calibration question. For a=1 the correct ratio is 7/12, not 7/6.
The mathematical image of gamma in [1249/1250,1] is
a in [0,1/2499], scalar force fraction in [0,1/2500], and circular ratio in
[2999/3000,1]. These are exact rational consequences of the specified
development rectangle, not new observational confidence levels.
