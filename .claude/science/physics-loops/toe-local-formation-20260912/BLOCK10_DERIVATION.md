# Static Regge compatibility and the missing force-balance equation

Author conditional derivation,2026-09-13. This is supplied Euclidean length
Regge calculus on the unit4D path complex, not a selected axiom law. The
source convention is stated below. Same-author exact coefficient extractions
and a different nonlinear distance-Gram implementation agree. Independent
source review and further scope stress testing remain pending.

## 1. A local necessary equation that the scalar family survives

Let q denote squared-edge variations. A full-hyperdiagonal triangle in one
cube is (0,u,1111), with m=|u|. Its flat area is sqrt(m(4-m))/2. Write
c=q_full-q_(0,u)-q_(u,1111). At flat background both its deficit and its area
derivative with respect to q_full vanish. To quadratic order the full equation is

E_hyper^(2)=-sum_(sigma,m=1..3) c_(sigma,m) W_(sigma,m)/[8m(4-m)],       (1.1)

where W=ni^T H nj-(ni.nj)(ni^T H ni/ni^2+nj^T H nj/nj^2)/2,
and i,j are the two omitted internal vertices. This follows directly from
A'_full=-c/(16A)+O(q^2) and delta^(1)=sum W/(2A). All triangle stars here
lie inside this cube. The72terms are a local incidence identity, not a
large-volume or momentum limit.

Use eight static scalar corner values f_0,...,f_7 in binary spatial order
000,001,010,011,100,101,110,111. Let xi_a have eight such values for each
component a=0,1,2,3, where these component indices mean spatial x,y,z and
Euclidean time respectively. For each edge displacement v define its tangent by

q_edge=(v_time-v_x-v_y-v_z)(Phi_start+Phi_end)
       +2v.(xi_end-xi_start)+lambda if the edge is the full hyperdiagonal,

with no lambda term on other edges. The last clause means an additive excess,
not that the preceding expression is restricted to that edge. The first part
is the supplied endpoint-mean scalar field; the second is the exact flat
vertex-displacement tangent. Substitution into(1.1) gives

E_hyper^(2)=lambda[3lambda+L_Phi+L_xi]/8,                     (1.2)
L_Phi=f_1+f_2+f_3+f_4+f_5+f_6-3f_0-3f_7.

The four rows of the coefficient matrix for L_xi are

    -3  1  1  1 -1 -1 -1  3
    -3  1 -1 -1  1  1 -1  3
    -3 -1  1 -1  1 -1  1  3
    -3 -1 -1  1 -1  1  1  3.

This table and(1.1) specify every coefficient without a fitted value.
L_Phi is minus the sum of the six mixed second differences on spatial faces.
In particular lambda=0 solves this necessary equation for every static Phi
and every static displacement field. A putative scalar-source obstruction
from this equation alone is false. This preserved surviving branch is an
important boundary on the separate pure-hyperdiagonal exclusion.

For fields depending only on x, let adjacent values be A,B and let
xi_(n+1)-xi_n=d. Then L_Phi=0 and L_xi=4(d_y+d_z+d_time).

## 2. The complete local cubic action from geometry

Here coefficients A_1,A_2 and theta_1,theta_2 denote coefficients of epsilon
and epsilon^2, rather than second derivatives. For a simplex metric I+epsilon H,
fix a hinge with normals ni,nj and put a=ni^2,b=ni.nj,c=nj^2,D=ac-b^2.
Let P be its flat tangent-plane projector, and define

u=ni^T H ni/a, v=nj^T H nj/c,
U=ni^T H^2 ni/a, V=nj^T H^2 nj/c,
B_1=ni^T H nj, B_2=ni^T H^2 nj,
s_1=(u+v)/2,
s_2=3(u^2+v^2)/8+uv/4-(U+V)/2,
W=B_1-b s_1, Z=-b s_2+B_1 s_1-B_2,
t=tr(PH), c_A=t^2/8-tr(PH PH)/4.

Expansion of -ni^T(I+epsilon H)^(-1)nj divided by the two normal lengths
first gives the cosine coefficients. Differentiating acos then gives

A_0 theta_1=-W/2,
A_0 theta_2=-Z/2+bW^2/(4D),
A_1=A_0 t/2, A_2=A_0 c_A.                                  (2.1)

Schlaefli implies S'=sum A' deficit. At the flat background this yields
S_3=-sum_simplex,hinge(A_1 theta_2+2A_2 theta_1)/3. Thus each local hinge
contributes the rational cubic

t Z/12-t bW^2/(24D)+c_A W/3.                                 (2.2)

Reconstruct H from its ten squared-edge variations by the same ordinary
polarization identity used in Block7; sum all24ordered path simplices.
For the plane-symmetric family in section1 the result per cube is

S_3,cell=[2(A+B)+d_x](B-A)^2
         +lambda^2(d_y+d_z+d_time)/4+lambda^3/8.              (2.3)

The sum of(2.2) is explicit finite algebra with rational coefficients.
Cube inversion interchanges A,B and preserves d; constant A=B is a flat
metric plus hyperdiagonal family. These facts independently constrain the
form to a multiple of(B-A)^2 times a linear expression, plus the displayed
hyperdiagonal terms. The24-cell coefficient sum fixes the coefficients2,1,
1/4 and1/8. No numerical coefficient fitting is used.

Equation(2.3) is a local decomposition of the global periodic cubic action.
A bare one-cube angle-area action can differ by boundary allocation terms;
the separate nonlinear check sums a complete periodic x cycle before comparing.

## 3. A necessary longitudinal balance condition

Take a finite periodic4D complex with all periods at least3. The first tangent
is independent of y,z,time and has the form in section1 with periodic real
Phi_n, periodic displacements xi_n, and arbitrary real hyper excess lambda_n.
For now no additional constant flat-metric tangent is included. All higher
order corrections may be arbitrary, including loss of plane symmetry.

The external source has components only on temporal-axis edges at every
amplitude; equivalently its work vanishes for every static longitudinal
vertex-displacement variation. This includes a supplied source potential
linear in temporal squared edges, with any amplitude-dependent coefficients.
It also includes source potentials depending only on those temporal edges.
A physical matter action with spatial dependence is outside this source class.

Let q(epsilon)=q_flat+epsilon v+o(epsilon) be a differentiable family of
stationary configurations for that source. For a flat static displacement
G eta, the Regge Hessian annihilates G eta, and source work on G eta is zero.
Projecting stationarity along this fixed q-coordinate variation therefore
kills the full linear term, including any o(epsilon) higher correction.
The leading epsilon^2 term is the derivative of S_3 at v in direction G eta.
Analyticity near the nondegenerate flat geometry makes the remaining projected
term o(epsilon^2). No C2 or convergent power-series assumption is required.

Set g_n=Phi_(n+1)-Phi_n. The longitudinal part of(2.3) gives

sum_n (eta_(n+1)-eta_n) g_n^2=0 for every periodic eta,
so g_n^2=g_(n-1)^2 for every n.                              (3.1)

The positive transverse/time volume factor cancels. Neither lambda nor any
of the first-order plane displacement choices enters(3.1). It is a necessary
condition, not sufficient nonlinear existence.

For an odd x period, a real periodic sequence with constant g_n^2 must have
g_n=0: otherwise each g_n is +/-a for a>0, and an odd sum cannot vanish,
contradicting sum_n g_n=0. Thus a nonconstant real Phi in this specified tangent
family cannot belong to a differentiable stationary family with the temporal-
only source. This remains true if constant geometric modes are fixed, because
periodic displacement variations have zero average in every edge class.
The theorem does not require higher-order corrections to share the symmetry.

At an even period, constant-magnitude gradients with equally many plus and
minus signs survive this one necessary condition. They are not claimed to
solve the other nonlinear equations. A constant Phi also survives, as it must.
Boundary forces, spatial stresses, time dependence, a different first-order
background or wider first-tangent families are outside this exclusion.

## 4. Interpretation and a concrete repair obligation

Put rho_n=Phi_(n+1)-2Phi_n+Phi_(n-1)=g_n-g_(n-1). Then

rho_n*(Phi_(n+1)-Phi_(n-1))/2=(g_n^2-g_(n-1)^2)/2.           (4.1)

Thus the condition is the exact centered discrete force balance rho grad Phi=0
for this supplied static source. This is an interpretation of the displayed
lattice identity, not a newly selected physical mass density or clock.
The linear Poisson identity remains true. It alone does not provide the
stress/support or motion needed for a nonlinear static source.

A source correction must supply longitudinal virtual work proportional to
sum_n(eta_(n+1)-eta_n)g_n^2 at this order, or change the prescribed static
family. The next task is to construct that correction variationally from a
specified matter/support action and check the other null projections. Adding
an arbitrary labelled stress only to this one equation is not full closure.
No axiom revision follows from this bounded source-family restriction.

## 5. Checks and provisional status

Exact source extractions are preserved separately from the derivation. The
first general hyperdiagonal probe showed the scalar quadratic term vanishes;
this contrary-to-a-possible-wall outcome is preserved. The full cubic rational
calculation gives(2.3) in one fixed cell, using(2.1)-(2.2).

A separate implementation starts from all simplex squared distances, forms
Gram matrices based at a simplex vertex, and computes angles by projecting
literal legs off the hinge plane. It uses no barycentric-normal derivatives.
At65digits, two-step odd-part extrapolation on a three-cell periodic ring
checks cubic coefficients36,27,25.5 for scalar, longitudinally displaced and
mixed-hyper rays. Errors are below6.8e-10. Two unrelated eight-corner static
fixtures check E_hyper quadratic coefficients0 and0.95, with errors below
1.6e-9. These5checks passed in4.17seconds; they are finite-step diagnostics,
not interval remainder bounds or an independent reviewer verdict.

The complete negative-family scope stress test, cold source pass, constant-
metric extension and force-balanced repair remain open. Do not report this as
a general no-go, a physical graviton failure or an axiom-forcing wall.

## 6. Constant modes and a proposed second-order source completion

The coefficient extraction for the ten constant-metric directions at a pure
scalar tangent gives the per-cell projections

(d/dH_xx,d/dH_yy,d/dH_zz,d/dH_tt)S3
   =(B-A)^2(1,-1,-1,3)/2,
(d/dH_ab)S3=0 for every a!=b.                                (6.1)

This agrees with the orthogonal-background scaling derivative: the scalar
quadratic stiffness at diagonal background G is proportional to
(G_yy+G_zz-G_tt)/sqrt(G_xx G_yy G_zz G_tt). Its negative derivative gives
exactly the four coefficients in(6.1). This scaling comparison is a check
of the diagonal normalization, not an independent nonlinear theory.

There is also an analytical extension of(3.1) to an arbitrary added constant
flat-metric tangent. The cubic cell polynomial is invariant under cube
inversion, which sends A<->B and leaves that metric and d fixed. Its terms
involving d_x are therefore even in g=B-A. At g=0 the configuration is a
constant flat metric plus hyper excess; the cubic term is lambda^3/8 plus
lambda^2 times the sum of off-diagonal metric entries/4. Its derivative along
d_x, a diagonal metric direction, is zero. A homogeneous degree-two derivative
can therefore only be a multiple of g^2, already fixed to one by(2.3).
The longitudinal balance and odd-period exclusion survive that extension.

If constant metric moduli are free, the stronger uniform H_xx projection in
(6.1) already excludes any nonconstant pure scalar tangent with temporal-only
source, at any period. The odd-period displacement result is useful because
it survives fixing those constant modes. These are separate quantified facts.

A candidate external correction is explicit. For a chosen leading Phi with
g_n=Phi_(n+1)-Phi_n, prescribe at order epsilon^2 only axis-edge components

J2_x(n)=g_n^2/2, J2_y(n)=-g_n^2/2,
J2_z(n)=-g_n^2/2, J2_t(n)=3g_n^2/2.                         (6.2)

Take the leading source J1_t=Delta_lat Phi and the pure endpoint-mean tangent
v, with zero gauge and hyper excess. Equation(2.3) shows that(6.2) matches
all four plane displacement projections of the quadratic force. Equation(1.2)
sets the hyper projection to zero. Equation(6.1) shows that its averages match
all ten constant metric projections as well. Every other Fourier component
of the residual is zero by plane symmetry. The full flat Hessian kernel
therefore annihilates J2-grad S3(v), so a finite real second coefficient
w exists satisfying Qw=J2-grad S3(v). This uses the exact Block7 kernel
classification, provisionally within the same candidate argument.

Then q=q_flat+epsilon v+epsilon^2 w obeys
E_Regge(q)=epsilon J1+epsilon^2 J2+O(epsilon^3).
This is second-order consistency only. It does not establish an exact
stationary branch at all orders. The extra axis stress and mean temporal
source are supplied using the chosen Phi. They arise from the explicit
external potential -sum(epsilon J1+epsilon^2 J2)q, but are not derived from
native matter; their dependence on an inverse-Poisson-selected Phi can be
nonlocal in the prescribed leading density. The construction prices the
missing source work and prevents a false axiom necessity claim.

The all-projection argument and explicit finite solution still need a complete
source/force check before this candidate repair is treated as established.
