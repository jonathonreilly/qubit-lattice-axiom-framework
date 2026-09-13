# Nonlinear sourced Regge compatibility: derivation contract

Started 2026-09-13, after Block9. Work personally without agents. The linear
Regge/transfer result is a separate author milestone under review preparation;
no physical consequence is treated as independently retained. This block uses
direct simplex geometry, preserving the provisional source status.

Target: the first nonlinear hyperdiagonal equation for a static endpoint-mean
Newton field on the supplied unit 4D path triangulation, first allowing an
arbitrary hyperdiagonal correction and then genuine displacement directions.
The source couples only to temporal squared edges, so its hyperdiagonal
variation is zero at every order by this supplied source convention. This is
not a physical matter action selected by the axioms.

Analytical route before coefficient evaluation:
E_hyper=sum_t A'_hyper delta_t. At flat background both factors vanish.
For the full-diagonal hinge t=(0,u,1111), m=|u|, put
c_t=q_full-q_(0,u)-q_(u,1111). Then A'_hyper=-c_t/(16 A_t)+O(q^2),
and delta_t^(1)=sum_(simplices in star) W_(sigma,t)/(2A_t).
Consequently the second-order compatibility polynomial is exactly
E_hyper^(2)=-sum_(sigma,m=1..3) c_t W_(sigma,t)/[8m(4-m)].
Each W is the same first inverse-metric angle variation derived locally
from barycentric normals. This expression involves the 65 comparable edges
of one cube and no outside cube. It can be checked by a separate nonlinear
triangle/angle implementation, with stated finite-difference limitations.

First restriction: Phi only depends on one spatial coordinate, with endpoint
values A,B in a cell, and q_edge=(n_t-n_s)(Phi_start+Phi_end), plus hyper
excess lambda. Constant Phi gives an exact constant flat metric tangent.
Cube inversion interchanges A,B and preserves the triangulation. Thus the
quadratic polynomial is expected to be 3lambda^2/8+c(B-A)^2: a linear
lambda(B-A) term would violate this symmetry, and constant-field cross terms
vanish on flat diagonal metric tangents. The coefficient c is deliberately
not predicted. Its sign decides whether a real hyper excess can meet this
necessary equation within this section.

Then include static vertex displacements consistent with a global periodic
mesh. A failed endpoint section alone is not a failure of every sourced
solution. Test its mixed compatibility, preserve any repairing displacement
or nonconstant curved tangent, and distinguish local solvability from global
periodicity and the remaining fifteen equations. Never turn a necessary
second-order condition into sufficient nonlinear existence.

Success: exact analytic compatibility or a surviving repair family with clear
remaining equations. Negative: only the quantified source/section family is
excluded. Inconclusive: more general tangents or matter couplings remain live.
No axiom edit, Lorentzian energy conclusion or formal no-go packet is planned.

First extraction,03:52UTC: the initially unknown g^2 coefficient is zero.
For arbitrary eight static scalar vertex values and all32static displacement
values, E_hyper^(2) factors as lambda times a linear expression. Thus lambda0
satisfies this necessary equation throughout that static subspace. This is a
surviving route, not a wall. A separate nonlinear angle/area check is next.

Next analytical target before coefficient extraction: the full cubic action
on the plane-symmetric family, Phi_n with adjacent values A,B and static
vertex displacement difference d. For each hinge with normals ni,nj write
u=ni Hni/a,v=nj Hnj/c,U=ni H^2ni/a,V=nj H^2nj/c,
s1=(u+v)/2,s2=3(u^2+v^2)/8+uv/4-(U+V)/2,
B=ni Hnj,B2=ni H^2nj,W=B-b*s1,Z=-b*s2+B*s1-B2,D=ac-b^2.
Then A_hinge theta_2=-Z/2+bW^2/(4D), where theta_2 is the coefficient of
epsilon^2. With t=tr(PH), cA=t^2/8-tr(PH PH)/4, the local cubic action
contribution is t Z/12-t bW^2/(24D)+cA W/3. This follows by integrating
S'=sum A' deficit: S3=-sum[A1 theta2+2A2 theta1]/3.

Summing the24 local path simplices is expected by cube inversion and constant
flatness to yield (B-A)^2[c(A+B)+e.d], plus lambda^3/8 and
lambda^2(d1+d2+d3)/4. Coefficients c,e are unknown before extraction.
A nonzero longitudinal e0 would impose constancy of squared adjacent gradients
under the second-order displacement stationarity equations for the supplied
source linear in temporal squared edges. Such a condition would be a static
force-balance restriction, not an axiom obstruction. Keep all source and mesh
assumptions explicit; do not claim sufficient nonlinear existence from it.
