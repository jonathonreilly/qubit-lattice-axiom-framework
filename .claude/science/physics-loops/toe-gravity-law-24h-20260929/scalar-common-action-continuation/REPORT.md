# Coupled scalar evolution and actual compatible analytic data

Author proof candidate, 2026-09-30. Focused independent check pending. This
extends the same changed-law nonlinear approximation unit. The scalar is a
separately supplied canonical field, never a proxy for the original rotor
records or walker and never a claim of their gravitational coupling.

## 1. Exact action, pairing and equations

Use the parent's full odd-grid metric law, density momenta and literal
Christoffel curvature, with positive couplings a,K and s=aK. Add a scalar
coordinate phi and its density momentum w=n^3 W, so {phi(x),w(y)}=n^3 delta_xy.
Products are pointwise; D is either spectral ik or centered
i sin(epsilon k)/epsilon, epsilon=2pi/n. Define

 M(g,w,z)=w^2/(2 sqrt(det g))+(s/2) B^ij(g) z_i z_j,
 z_i=D_i phi, B^ij=sqrt(det g)g^ij,
 C_tot[N]=C_g[N]+mean[N M],
 G_tot[X]=G_g[X]+mean[w X^i D_i phi].                       (1)

This is the massless scalar, with no potential. The first-order canonical
action is integral dt[mean(pi:gdot+w phidot)-C_tot[N]-G_tot[X]] in density
coordinates. We fix N=1,X=0 for the evolution theorem; their role as continuum
multipliers does not imply finite first-class constraints. Variation in the
finite canonical coordinates gives the actual Hamiltonian evolution.

Retain q_l,A=D_l g_A,r_l,ij=D_l B^ij and the parent's V(g,q,r).
The full finite Hamiltonian is exactly mean[T+V+M] by skew summation by parts.
Its equations are

 gdot_A=A_A=T_pA,
 pdot_A=-T_gA-V_gA-M_gA+sum_l D_l V_q_l,A
                          +sum_l,ij B^ij_gA D_l V_r_l,ij,
 phidot=w/sqrt(det g),
 wdot=s sum_i D_i(B^ij z_j),
 qdot_l,A=D_l A_A,
 rdot_l,ij=D_l(sum_A B^ij_gA A_A),
 zdot_i=D_i(w/sqrt(det g)).                                (2)

Ordinary local derivatives M_g keep w,z fixed and include the determinant
and inverse metric. The symmetric six-slot pairing is unchanged; a tensor
offdiagonal pi entry remains p/2. The volume normalization cancels the mean
also in the scalar equations. No finite product rule is used. Time
differentiation preserves q-Dg,r-D B,z-Dphi exactly. The augmented variables
are analysis devices, not additional canonical fields.

Every component is still F0(U)+sum_l P_l(U) D_j Q_l(U), now for
U=(h,p,q,r,phi,w,z), with local algebraic analytic maps on |h|<1.
The centered unit-lapse Hamiltonian has the same radius-one-star density;
scalar terms add only the center and nearest-neighbor phi values. Actual
finite metric/scalar evolution has radius at most two.

## 2. Complete continuum algebra and propagation

Replace D by partial derivatives for this paragraph. The scalar functional
derivatives are delta C_m[N]/delta w=Nw/sqrt(g) and
delta C_m[N]/delta phi=-s partial_i(N B^ij partial_j phi). Hence directly

 {C_m[N],C_m[M]}=G_m[s g^-1(N dM-M dN)].                    (3)

In the mixed gravity-scalar bracket, the gravity curvature has zero bracket
with C_m. The remaining metric pairing of gravity kinetic and scalar terms
has an undifferentiated factor NM, symmetric under N<->M. Its two mixed
orders therefore cancel identically. This cancellation is also true for the
finite functional, since M depends pointwise on g and has no gravity momentum;
it alone does not prove a finite scalar CC identity.

The canonical G_tot generates the ordinary Lie action: g is a covariant
metric, pi its contravariant weight-one momentum, phi a scalar and w a
weight-one density. Thus M is a scalar density and direct integration by
parts gives {G_tot[X],C_tot[N]}=C_tot[X.dN]. The two carriers are independent,
so the scalar momentum map combines with the gravity momentum map to give
{G_tot[X],G_tot[Y]}=G_tot[[X,Y]]. Combining (3), the mixed cancellation and
the parent full continuum gravity bracket yields

 {C_tot[N],C_tot[M]}=G_tot[s g^-1(N dM-M dN)].              (4)

These are exact continuum functional identities, with the field dependence
of the shift retained. Canonical Jacobi holds for the full differentiable
functionals, rather than only for external fixed shifts. Substitution of
(4) includes the brackets acting on g^-1; omitting those terms would not be
this algebra. No finite-grid Jacobi-derived closure is inferred.

The actual densities are C_tot=C_g+M and
J_tot,k=pi^ij partial_k g_ij-2partial_j(g_ik pi^ij)+w partial_k phi.
At unit lapse and zero shift, the same smearing argument as in the checked
parent therefore gives

 Jdot_tot,k=0,   Cdot_tot=partial_j(s g^ij J_tot,i).         (5)

Compatible continuum initial data retain all four zero constraints. Matter
and geometry exchange energy through one Hamiltonian and its metric variation;
a separately fitted stress tensor is not inserted.

## 3. Uniform analytic-time comparison for the actual finite coupled law

Keep the parent's initial |h0|_(2sigma0)<=1/8. Require finite scalar initial
norms |phi0|_(2sigma0), |w0|_(2sigma0), in addition to the finite metric
momentum norm. Increase its M0 by

 |phi0|_(2sigma0)+|w0|_(2sigma0)+|phi0|_(2sigma0)/(e sigma0).

This bounds the actual initial scalar samples and z=Dphi at sigma0.
Recompute the finite local majorants C0,C1,L0,L_P,L_Q,m_P,m_Q on the new
M=2M0+2 ball, including the displayed scalar monomials and their derivatives.
The parent inverse/determinant majorants bound them explicitly. Its metric
velocity bound C_h remains permissible with the new M, since M contains no
gravity momentum. Use these enlarged constants in the same positive T0,T.
The old numerical values of constants, if any, are NOT silently reused.

The shrinking-radius Dini estimate, metric-safe bootstrap, compactness and
ordered Volterra argument now apply componentwise to (2), with exactly their
proved hypotheses. In particular |F|<=C0+C1 N(U), the one-derivative scale
Lipschitz bound, and the strict metric margin are unchanged in form. The
scalar local maps are polynomial in phi,w,z (independent of phi here) and
analytic in g. This proves a common positive analytic time independent of n,
not a Sobolev well-posedness or long-time estimate.

For spectral D, the full sampling commutator retains the parent exponential
factor exp[-sigma0(J+1)/8]. For centered D, use the already checked direct
all-alias bound epsilon^2[3/(e delta)]^3/6. Add phi0 to the numerator of
the parent's initial derivative-mismatch constant, and add the new scalar
P_l,Q_l terms to its consistency constant. The same Volterra estimate gives
the corresponding exponential or O(epsilon^2) augmented-state error in
radius sigma0/4. True finite C_tot and J_tot are obtained from their literal
densities with the chosen D, including w z_k; the one-derivative density
Lipschitz and sampling estimates give the same rate in radius sigma0/8.
With continuum-compatible initial data, (5) converts this into actual finite
constraint bounds. No finite initial defect or later Fourier tail is removed.

## 4. Explicit compatible nonconstant scalar data

The following elementary conformal contraction supplies such data, instead
of assuming an unspecified solution of the constraints. Work on the period2pi
continuum torus, with normalized average denoted by brackets. Take a real
nonconstant trigonometric polynomial f, scalar amplitude b, and write

 phi0=b f, w0=0, g0=psi^4 I,
 pi0^ij=-(2H/a)psi^2 delta^ij.                            (6)

The independent diagonal density momenta equal these pi entries, and all
offdiagonal entries vanish. The full momentum density vanishes exactly:
pi^ij partial_k g_ij=-(24H/a)psi^5 partial_k psi cancels
-2partial_j(g_ik pi^ij)=(24H/a)psi^5 partial_k psi; w0=0.

Let q=sum_i(partial_i f)^2. Direct Christoffel calculation for g=psi^4 I gives
R=-8psi^-5 Delta psi. The kinetic and scalar densities in (1) are respectively
-(6H^2/a)psi^6 and (aK b^2/2)psi^2 q. Thus C_tot=0 is exactly

 Delta psi + lambda q psi - c_H psi^5=0,
 lambda=a b^2/16,       c_H=3H^2/(4aK).                   (7)

The sign-changing gravitational kinetic term is kept. A positive scalar
energy has not been canceled by deleting a mode or replacing its source.
Impose mean psi=1. Set psi=1+u, mean u=0, and

 c(u)=<q(1+u)>/<(1+u)^5>,
 T(u)=-lambda Delta_0^-1[q(1+u)-c(u)(1+u)^5],
 H^2=(a^2 K b^2/12)c(u).                                 (8)

Here Delta_0^-1 is the actual mean-zero inverse, multiplier -1/|k|_2^2
for k!=0 and zero at0. Its Wiener norm is at most one. The bracketed right
side has zero mean exactly, so no scalar equation is lost to this inverse.

All following norms are at rho=2sigma0. Let B=|q|_rho, r=1/128,
R=1+r, d=2-R^5>0, and set the explicit positive constants

 A=R+R^6/d,
 L=1+6R^5/d+5R^10/d^2.

On the complex Wiener ball |u|<=r, the denominator differs from1 by at
most R^5-1, so its modulus is at least d. The analytic algebra product
bound gives

 |q(1+u)-c(u)(1+u)^5|<=B A,
 Lip[q(1+u)-c(u)(1+u)^5]<=B L.                            (9)

For completeness, the quotient term's Lipschitz contributions are
B R^5/d from its numerator, 5B R^5/d from (1+u)^5, and
5B R^10/d^2 from the denominator. Their sum plus B yields L.
No elliptic derivative loss is hidden: Delta_0^-1 is bounded on this norm.

Choose b!=0 small enough that

 lambda B <= min(r/(2A),1/(2L)).                          (10)

Then T maps the radius-r ball into the radius-r/2 ball and is a contraction
with factor at most1/2. Starting u_0=0, u_(m+1)=T(u_m) converges in this
analytic norm to the unique solution in that ball, with explicit error

 |u-u_m|<=2 lambda B A 2^-m.                              (11)

Realness and zero mean are preserved. At real torus points psi>=1-r>0.
Since f is nonconstant, q is nonnegative and not identically zero, so c(u)>0
and H^2>0. Either sign of H may be supplied; it is an initial expansion
branch, not a physically selected cosmological constant. Equations(7)-(8)
prove all four actual continuum constraints. Also

 |g0-I|_(2sigma0)<=3[(129/128)^4-1]<1/8,

and |p0|_(2sigma0)<=6|H|R^2/a, so these data meet section3's hypotheses.
This is an explicit nonempty inhomogeneous-matter class. For b=0 the formula
extends to psi=1,H=0, but the nonconstant source claim is for b!=0.

The scalar profile, couplings, analytic class and mean conformal normalization
are supplied. The theorem solves their constraints and transports their
actual finite approximations. It does not derive these physical inputs from
axioms or records, and it does not solve general conformal data or all matter.

## 5. Context, checks planned and remaining obligations

The conformal strategy is standard. Choquet-Bruhat, Isenberg and Pollack,
arXiv:gr-qc/0610045v2 section2, was read for the Einstein-scalar constraint
and conformal structure, not imported as an all-data existence theorem.
Our coefficients follow (1) directly, and (9)-(11) give a separate small
analytic contraction with its exact normalization. The current repo's
rate-linear curvature-member note concerns a distinct static supplied model.
Its closed static positive-source restriction does not exclude the nonzero
extrinsic curvature in (6). No historical novelty or source-status promotion
is asserted.

Before reuse, independently check the full scalar variation/cross cancellation,
analytic transfer and initial-data contraction. A planned finite diagnostic
will use the literal finite Hamiltonian gradient including scalar metric
variation, then sample the constructed continuum data and report actual
finite constraint residuals. A truncated contraction solve or grid trajectory
is floating evidence unless separately bounded; the proof gives the infinite
analytic solution. The physically important original rotor/walker common
source coupling and record clock remain unresolved and are not renamed scalar.
