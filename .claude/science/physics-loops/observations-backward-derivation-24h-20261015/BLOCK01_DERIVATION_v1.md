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
