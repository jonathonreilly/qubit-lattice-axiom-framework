# Positive QUMOND solar quadrupole response

This is a conditional mathematical result for the same supplied QUMOND
candidate. It does not adopt that law or supply its relativistic completion.
The first exploratory kernel protocol is preserved in DERIVATION_TARGET.md.
The solar tension and the earlier two-form numbers were already exposed;
this reformulation and illustrative lower bound are post-test analysis.

## Target and sufficient hypotheses

For the point Sun with a fixed nonzero uniform Newtonian external field,
prove a positive one-dimensional response kernel for the anomalous quadrupole.
Use the root independent Poisson derivation's conventions: acceleration is
minus grad(Phi), rM=sqrt(GM/a0), eta=gN_external/a0>0 and
h=Hzz*rM/a0. The published positive-potential convention is
Q2=-3Hzz/2, so F=Q2*rM/a0=-3h/2.

Supply the QUMOND equation and a C1 response nu(q)>=1, nu'(q)<=0. Sufficient
regularity here is nu-1=O(q^(-alpha)), nu'=O(q^(-alpha-1)) near zero with
0<=alpha<1, and nu-1=O(q^(-n)), nu'=O(q^(-n-1)) at infinity with n>3/2.
These conditions include the campaign's exponential-square-root response.
They permit absolute integrations below and make the anomalous Hessian
regular at the Sun. A discontinuous or more slowly decaying response needs
a separately justified weak-solution/subtraction treatment; it is not
silently included. No galaxy symmetry or Galactic external-field conversion
is used in the kernel theorem itself.

## Reduction of the Poisson Hessian

The independently derived integration-by-parts expression is

h=(3/2) integral dv dc [nu(q)-1]
  [-v^2(3c^2-1)+eta*c(5c^2-3)],
q=sqrt(v^4+eta^2-2eta*v^2*c), v>=0, -1<=c<=1.

Set s=q/eta and t=v^2/eta. Then c=(t^2+1-s^2)/(2t),
|1-s|<=t<=1+s and

h=(3/4) eta^(3/2) integral_0^infinity s[nu(eta*s)-1] K(s) ds,
K(s)=integral_|1-s|^(1+s) t^(-3/2)
 [-t(3c^2-1)+c(5c^2-3)] dt.

The Jacobian is essential: dv*dc=sqrt(eta)*s/(2*t^(3/2)) ds*dt,
while the bracket contributes a further eta. For d=1-s^2 an elementary
antiderivative of K's t integrand is

B(t;s)=-t^(5/2)/20+(3d/4-1)t^(1/2)
 +(d-3d^2/4)t^(-3/2)-5d^3*t^(-7/2)/28.

Differentiation verifies the identity directly. The s=1 singularity of the
resulting K is integrable, with different one-sided signs; no point value of
K is needed. Define

P(s)=4s^4+2s^3+3s^2+2s+4,
R(s)=4s^4-2s^3+3s^2-2s+4,
W(s)=(8/105)[R(s)*sqrt(1+s)-P(s)*sqrt(abs(1-s))].

Direct piecewise differentiation gives W'(s)=-s*K(s), W(0)=0 and
W(infinity)=0. Its endpoint expansions are
W(s)=2s^5/5+11s^7/140+O(s^9) at zero and
W(s)=2/(5sqrt(s))+11/(140s^(5/2))+O(s^(-9/2)) at infinity.
The identity W(s)=s^(9/2)W(1/s) supplies the second expansion from the first.

Integration by parts has vanishing boundary terms under the stated growth
hypotheses. It yields the positive response formula

F(eta)=(9/8) eta^(5/2) integral_0^infinity W(s)[-nu'(eta*s)] ds
      =(9/8) eta^(3/2) integral_0^infinity W(q/eta)[-nu'(q)] dq.   (1)

## Positivity, stable evaluation and a lower bound

P>0; the inequalities 2s^3<=s^4+s^2 and 2s<=s^2+1 give
R>=3s^4+s^2+3>0. Rationalizing the square-root difference gives the exact
stable expression

W(s)=(16/105)*T(s)/[R(s)*sqrt(1+s)+P(s)*sqrt(abs(1-s))],
T(s)=s^5*(16s^4+12s^2+21) for 0<=s<=1,
T(s)=21s^4+12s^2+16 for s>=1.                         (2)

The two polynomial identities follow by expanding the squares. Therefore
W(s)>0 for every finite s>0. Thus F>=0, and F>0 for any nonconstant response
in this smooth monotone class. This is a sign statement about the supplied
law and boundary problem, not a no-go for nonlinear gravity or nature.

For an explicit interval bound it is useful to prove unimodality. Let
p=12s^3-6s^2+s-2 and r=12s^3+6s^2+s+2. Then
K=(4/35)[p/sqrt(s-1)-r/sqrt(s+1)] for s>1;
K=-(4/35)[p/sqrt(1-s)+r/sqrt(1+s)] for 0<s<1.
For s>1, p>0 and p^2(s+1)-r^2(s-1)=2(21s^2+4)>0, so K>0.
For s<1 with p>=0, K<0 immediately. When p<0, p'=(6s-1)^2 and
p(3/4)=7/16>0 imply s<3/4. On 0<=x=s^2<=9/16, the concave polynomial
35+84x-144x^2 is positive at both endpoints, hence positive throughout.
Consequently r^2(1-s)-p^2(1+s)=2s^3(35+84s^2-144s^4)>0, giving K<0.
Thus W increases to s=1 and decreases afterward, with W(1)=8sqrt(2)/15.

For any 0<q1<q2<infinity, (1) gives the rigorous bound

F(eta)>=(9/8) eta^(3/2) min[W(q1/eta),W(q2/eta)]
        *[nu(q1)-nu(q2)].                              (3)

Disjoint intervals may be summed. This links the solar quadrupole to the
amount of response variation on specified acceleration intervals, rather
than to a chosen interpolation formula everywhere. It does not infer nu
from galaxy data by itself: baryonic/source/geometry calibration and the
actual QUMOND disk field remain necessary. A weak or vanishing response
variation simply yields a weak or zero lower bound.

## Numerical protocol and inference boundary

Check exact polynomial/derivative identities; evaluate the stable kernel with
70-digit arithmetic; compare (1) at the already frozen eta={.5,1,2,3,4}
against the two independent Poisson integrals. This is a third implementation
check with known reference values, not a new empirical prediction.
An illustrative q interval [2,5] is selected after seeing the model's solar
tension; its bound is an application of the all-interval theorem, not an
unexposed model-selection test or a parameter fit. The empirical source
conventions and provisional galaxy calibration must accompany any SI value.
The mathematical proof and its finite numerical diagnostics are distinct.
