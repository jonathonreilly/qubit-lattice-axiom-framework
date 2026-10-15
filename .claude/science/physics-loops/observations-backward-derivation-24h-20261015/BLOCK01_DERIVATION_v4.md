# General-action inverse and the missing field-range registration

Author: /root,2026-10-15. Exploratory conditional mathematics. No empirical fit,
new observed metric, selected potential, retained claim or global no-go.
The single-metric inverse is known prior art (Bronnikov, Badalov, Ibadov,
arXiv:2212.04544, section2); it is independently rederived in this convention
for the cross-environment question. Prior campaign #9620 had a fixed revised
potential/kinetic family. Here those functions remain unknown.

## 1. Candidate class and exact local inverse

Signature(-+++), natural units. Take only as a candidate class

 S=int sqrt(-g)[F R/2 - omega(F)(partial F)^2/(2F)-V(F)] + S_m[g,psi].

The physical matter metric is g. Work on a material-vacuum annulus r>0 with
 ds^2=-N(r)^2 dt^2+dr^2/B(r)+r^2 dOmega^2,
N,B>0 smooth. Smoothness is used to avoid claiming minimal regularity. Require
F>0 and a nonconstant F chart. This action class, field count, physical metric,
static symmetry and vacuum are hypotheses, not derived from measurements.
No functional form of omega or V is selected.

Write ell=ln N. The mixed Einstein components are
 Gt=(B-1)/r^2+B'/r,
 Gr=(B-1)/r^2+2B ell'/r,
 Ga=B(ell''+ell'^2+ell'/r)+(B'/2)(ell'+1/r).
Set
 d=B(1/r-ell'),  a=Ga-Gt,  u=a/d,
 H=Gr-Gt-B(u'+u^2)-(B'/2-B ell')u,
 W=-Gt-H/2-B(u'+u^2)-(B'/2+2B/r)u.                  (1)
The theorem chart requires d!=0 and u!=0 throughout its connected interval.

Variation gives, with Z=omega/F,
 F G^mu_nu = Z(partial^mu F partial_nu F
                -delta^mu_nu (partial F)^2/2)
             -V delta^mu_nu+nabla^mu nabla_nu F-delta^mu_nu box F.
The scalar Hessian entries are
 (nabla^t nabla_t F,nabla^r nabla_r F,nabla^theta nabla_theta F)
 =(B ell'F', B F''+B'F'/2, BF'/r).
Their trace is box F=B F''+(B'/2+B ell'+2B/r)F'.

Subtract t from angular: F a=d F'. Hence
 x(r)=int_(r0)^r u(s)ds, F(r)=C exp(x(r)), C>0.       (2)
Subtract t from r, divide by F, then use F''/F=u'+u^2:
 omega(F(r))=H/(B u^2).                              (3)
The t equation fixes V(F(r))/F(r)=W(r).              (4)
Thus omega and V on this monotone F interval are reconstructed, with one
undetermined positive C. This is local reconstruction, not an action-selection
principle. Changing C shifts the argument log F of the reconstructed functions
and scales V; the physical normalization remains unmeasured by these vacuum
equations. Healthy Einstein scalar kinetic sign requires2omega+3>0, not
omega>0. No nonlinear or global stability is inferred from that sign.

Conversely, define F by(2), omega by(3) and V by(4). Since F'!=0, r is a smooth
function of F on the interval. The t equation holds by(4), r by(3), angular
by(2); the fourth angular equation is identical. Diffeomorphism invariance gives
the scalar Euler expression multiplied by F', once the metric equations hold.
Therefore the scalar equation holds on this chart. In direct notation it is
 R/2+Z box F+(Z_F/2)(partial F)^2-V_F=0.              (5)
This is checked separately below rather than counting the Bianchi statement
as a numerical test. Neither arbitrary endpoints nor a continuation through
a chart singularity are supplied by this converse.

## 2. What a common action actually requires

For environment i, geometry determines x_i up to a chosen integration origin
and the two functions
 gamma_i(x_i)=(omega_i(x_i), W_i(x_i)).
It does not determine C_i in F_i=C_i exp(x_i). For an overlap in physical F,
one common action requires
 gamma_1(x)=gamma_2(x+delta), delta=ln(C_1/C_2),       (6)
throughout that overlap, after using a common dimensional reference in log F.
The sign in(6) follows from C_1 exp(x)=C_2 exp(x+delta).
The W component is V/F, so no additional arbitrary vertical rescaling is
allowed in(6). Additive potential constants are not a freedom of the vacuum
metric equations. They change the stress.

On smooth open overlapping charts, equality of both components in(6) is also
sufficient to glue the two reconstructed action functions on their union.
Their derivatives agree because the functions agree on an open interval.
A pair of geometries agreeing only at a point does not provide this condition.
A constant omega can leave delta unidentifiable; repeated/non-injective curves
can admit several deltas. No global unique registration is asserted.

Crucial limitation: arbitrary C_i can move two finite x intervals apart.
Then no common-F overlap test is available. The action may have different
smooth behavior on disjoint F intervals. Choosing overlap or C_1=C_2 would
supply a new physical-state/boundary assumption; it is not import retirement.
The following exact example makes this failure concrete, while making no
claim about one connected universe or global source completion.

## 3. Two positive-kinetic vacuum patches with an explicit common action

Use dimensionless radius1<r<2. Let N=1 and B=b constant with0<b<1.
Direct algebra gives
 c=(1-b)/b, F=C r^c,
 omega=(1-c)/c, W=-b c(c+1)/(2r^2),
 V(F)=-[b c(c+1)/2] C^(2/c) F^(1-2/c).              (7)

Patch A: b=1/2,C=1, c=1, F=r in(1,2), omega=0,
 V=-1/(2F), W=-1/(2r^2).
Patch B: b=1/3,C=4, c=2, F=4r^2 in(4,16), omega=-1/2,
 V=-4, W=-1/r^2.
Both have F>0 and2omega+3>0. They are controlled exact geometries, not observed
metrics. Potentials are negative on these intervals; no global positive energy,
bounded history or stability statement is made.

Let chi(F) be any smooth step equal0 for F<=2 and1 for F>=4, between0 and1.
For example use chi(F)=h((F-2)/2), where h(t)=0 for t<=0, h(t)=1 for t>=1,
and h(t)=exp(-1/t)/[exp(-1/t)+exp(-1/(1-t))] inside(0,1).
On F>0 define one action by
 omega(F)=-chi(F)/2,
 V(F)=-(1-chi(F))/(2F)-4chi(F).                      (8)
It realizes both patches exactly, and2omega+3=3-chi>=2 everywhere.
Only this illustrative action is chosen to prove existence of the two-patch
ambiguity; it is not proposed as the real potential or a completed theory.
Its interpolation is unobserved and unconstrained by these patches.

If one instead sets C_A=C_B=1, their F intervals overlap and the reconstructed
omega values0 and-1/2 disagree. That conditional incompatibility is a result
of the added normalization/state registration. The two metrics alone did not
supply it. A third observation of the same sampled F could constrain(8), but
claiming shared F without a readout/boundary argument repeats the assumption.

## 4. Degenerate charts and observational obligations

At d=0 the un-divided relation F a=dF' requires a=0 for a finite nonzero F.
If both vanish, no division is justified without continuation analysis. At
u=0 the omega quotient is undefined; an isolated turning point needs finite
limits and single-valued action consistency. A constant-field interval has
F'=0, Gt=Gr=Ga; it determines only potential value/gradient constraints, not
a whole kinetic function. More fields or unknown anisotropic matter change
the inverse and are distinct competing classes.

The metric is an ideal input, not a raw observation. Redshift/ranging/orbits
require source geometry, clocks/rulers and uncertainty treatment before they
can supply N and B; differentiation can amplify error. The present proof
uses no fitted metric or empirical parameter. A same-environment calibrated
response, connected-field boundary argument, or another independent probe of
relative F is the missing registration input. The next useful block must try
to derive that input from a measurement map or dynamic material equations,
not add it to the premise list and announce selection.

## 5. Control plan frozen before execution

Use direct four-dimensional Christoffel/Ricci/scalar variation for the two
patches; compare with inverse expressions separately. Verify all independent
metric components and the scalar equation. Test off-shell failures by changing
omega, potential normalization and radial exponent one at a time. Verify the
same-input overlapping charts disagree and disjoint charts fit one smooth
positive-kinetic action. Counts are synthetic mathematical controls, never
independent empirical tests. An independent focused checker should challenge
normalization, converse, coordinate freedoms and the overlap inference.


## 6. Relative field recovery with lower metric derivative requirements

New root calculation after the v1 controls. This addresses the observable-side
conditioning of the missing relative F, not absolute action normalization.
Put y=1/r-ell', so d=By. On a chart where y has a fixed nonzero sign, expand
 a/B=-y'-3y/r+y^2-(B'/2B)y+1/(B r^2).
Thus
 u=-y'/y-2/r-ell'-B'/(2B)+1/(B y r^2),
 log[F(r)/F(r0)]= -log|y(r)/y(r0)|-2log(r/r0)
                 -log[N(r)/N(r0)]-(1/2)log[B(r)/B(r0)]
                 +int_(r0)^r ds/[B(s)y(s)s^2].       (9)
This follows by integration by parts from the same exact metric equation.
It recovers a RELATIVE field profile from N,N',B and one quadrature, without
numerically differentiating N twice or B once. It does not reconstruct omega
or V at this lower regularity, and it is not an inference of C. The smooth
underlying-solution theorem remains; this formula also defines a continuous
functional on the lower-regularity measured inputs in the separated chart.

For two input pairs N,B and Nhat,Bhat over a fixed interval, suppose both
N>=n0>0, B>=b0>0 and both y have the same sign with |y|>=y0>0.
Let uniform absolute errors be eN,eB,ey. A direct mean-value bound gives
 |log[(Fhat(r)/Fhat(r0))/(F(r)/F(r0))]| <= E(r),
 E=2eN/n0+eB/b0+2ey/y0
       +|1/r0-1/r|[eB/(b0^2 y0)+ey/(b0 y0^2)].      (10)
All radii are the same fixed physical-coordinate interval, r,r0>0; radial
coordinate error or unknown areal-radius identification is not included.
The logarithmic endpoint bounds use the positive lower bounds. For the
integral, split1/(Bhat yhat)-1/(B y) into the B and y differences and use
those same lower bounds; int ds/s^2 is the displayed endpoint factor.
If |N'|,|Nhat'|<=M1 and their derivative discrepancy is eNp, then
 ey<=eNp/n0+M1 eN/n0^2.                              (11)
The reconstructed ratio is therefore within exp(+/-E) of the true ratio.
No independent observational confidence level follows from deterministic
input-error bounds. Near y=0 the bound deteriorates; no selected smoothing
prior can be counted as a derived error certificate.

For the family in section3, y=1/r and B=1/(c+1). The endpoint terms
-log(y/y0)-2log(r/r0) reduce to -log(r/r0), the N and B ratios are1,
and the integral is (c+1)log(r/r0). Their sum is c log(r/r0), as required.
The v2 draft mistakenly displayed the endpoint contribution twice before
its own warning; that drafting error is corrected here and v2 is preserved.

The practical next discriminator is whether a connected observed metric can
supply these bounds and relative-field span. Two disconnected environments
still have independent integration constants. Establishing a connected field
or a calibrated local-response normalization remains necessary before using
(6) as an empirical cross-environment test.


## 7. Clock, radial radar and circular-orbit version of the relative inverse

This is a forward measurement map derived from the supplied physical metric,
not a claim that these ideal functions have been measured. Use a static clock
at r0 as reference, identical ideal clocks at r, radial null radar reflection,
and weak geodesic test bodies on circular paths. Areal r and the source's
static spherical vacuum geometry are independently supplied geometric inputs.
Universal clock/light/test-body coupling and calibrated timing remain class
premises. Plasma, reflection delay, pressure forces and moving source corrections
are not set to zero in any real-data analysis by this idealization.

Let R(r)=N(r)/N(r0), obtained from the emitted/received proper frequency ratio
with its direction stated; define rho(r)=c*tau_roundtrip(r)/2, and S=rho'>0.
A radial null ray has c dt=dr/[N sqrt(B)], so
 S=1/[R sqrt(B)], B=1/(R^2 S^2).                     (12)
The half roundtrip is monotone outward (r>=r0); extension inward uses the
signed optical coordinate, not an unsigned elapsed-time derivative.
Let Omega0=dphi/dtau0 be the circular angular frequency expressed in the
reference clock's proper time. The radial geodesic equation gives
 Omega0^2/c^2=R R'/r.
Hence v^2=r^2 Omega0^2/(c^2 R^2)=r ell'.             (13)
This v is the dimensionless speed measured by a local static observer. A
timelike circular geodesic has0<=v^2<1; stability is an additional condition.
The orbit and redshift functions have the independent necessary consistency
 log[R(r)/R(r0)]=int_(r0)^r v(s)^2 ds/s.             (14)
Do not enforce(14) by constructing one data channel from the other and then
count it as a test. R(r0)=1 is a reference convention, not fitted physics.

Use y=(1-v^2)/r and(12) in(9). The common reference lapse cancels:
 F(r)/F(r0)=[S(r)/S(r0)] [r0/r]
             [(1-v(r0)^2)/(1-v(r)^2)]
             *exp{int_(r0)^r R(s)^2 S(s)^2
                              /[s(1-v(s)^2)] ds}.   (15)
This eliminates a chosen scalar profile on a connected chart under the
single-field class assumptions. It supplies neither absolute F(r0) nor the
relative integration constants of disconnected environments, and still does
not select omega or V beyond their reconstructed interval. Equation(15)
uses one derivative of radial radar data and no numerical redshift derivative
when the independent orbital channel supplies v. Error propagation from those
primitive observables still needs its own bounds, including areal-radius error.

For N=r^p, B=b and r0=1, take0<=p<1. Direct null and geodesic equations give
 R=r^p, S=r^(-p)/sqrt(b), v^2=p.
Equation(15) gives r^[1/(b(1-p))-1-p], exactly r^c of the metric inverse,
 c=(b p^2-b+1)/[b(1-p)].
This family is a synthetic consistency control, not observational validation.
The p=0 member has stationary test geodesics and is only the zero-speed limit.
A useful empirical follow-up must determine which measured channels can
actually supply(12)–(14), with noise/calibration and independent-test separation,
before evaluating(15). No effective Newton coefficient is identified with1/F
by assertion.
