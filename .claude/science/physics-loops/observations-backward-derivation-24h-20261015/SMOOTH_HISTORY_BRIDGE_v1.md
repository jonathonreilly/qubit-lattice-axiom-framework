# Smooth-history test after independent force calibration

Status: exploratory conditional-support. Root continuation of the physical-port bridge and PR9634, not a new empirical result. Goal: replace an ideal rectangular coordinate pulse by a directly evaluated smooth-history consistency test, while exposing the extra moving-force calibration obligation.

## Exact target and premises

Assume an independently calibrated conjugate source and visible-coordinate chart x. The corrected interaction readout is R(t)=J(t)-N(t), where N is the visible inertial/dissipative/actuator load excluded from R. For example a separately adopted visible kinetic term M(x) xdot^2/2 and damping D(x) require N=M xddot+M'(x) xdot^2/2+D xdot. A raw holding-current formula is insufficient during motion. The source port, N and their uncertainty must be calibrated independently of the candidate compatibility fit, or retained explicitly as unresolved premises.

The candidate class remains
tau w''+gamma w'+Cw=-b(x),
R=u(x)+a(x)w,
with tau,C>0, gamma>=0 and common coefficients. The functions and response class are not derived by the algebra below. Arbitrary finite hidden starting states may differ across histories.

Let a_r!=0 and Delta_b!=0 be fixed normalizations, A(x)=a(x)/a_r,
B(x)=[b(x)-b0]/Delta_b, and
m(x)=u(x)-a(x)b(x)/C.
A and B are relative functions reconstructed/calibrated on exposed development inputs; finite clamped samples alone do not identify their continuum extensions. m is a calibrated force-offset function, not a silently assigned zero.

## 1. Extract the offset without waiting for relaxation

At a fixed x, sample the corrected clamped response f0,f1,f2 at common interval Delta. Let s,p be the independently inferred common homogeneous discrete recurrence coefficients. Since f_n=m+r_n and r_(n+2)=s r_(n+1)-p r_n,

m=(f2-s f1+p f0)/(1-s+p),                               (1)

provided d=1-s+p!=0. This removes arbitrary homogeneous preparation without requiring a steady-state wait or a damping-selected initial state. It is elementary affine recurrence algebra, not a new equilibrium theorem.

If |s|<=S, |p|<=P, |f_n|<=M_f and sample errors are bounded by e_f, coefficient errors by e_s,e_p, define e_d=e_s+e_p and
e_n=(1+S+P)e_f+M_f(e_s+e_p)+e_f(e_s+e_p).
For |d|>=d_min>e_d, a valid bound is

|m_hat-m| <= e_n/(d_min-e_d)
       +(1+S+P)M_f e_d/[d_min(d_min-e_d)].                (2)

The same uncertainty may be correlated across all samples. At an undamped full-period sampling alias, s=2,p=1 and d=0; equation1 cannot identify the offset. A near-zero d is ill-conditioned and must not be inverted as exact data. The common recurrence itself still needs calibration and uncertainty.

## 2. Smooth response identity in the regular chart

On a tested history with |A(x(t))| bounded away from zero, set

H(t)=[R(t)-m(x(t))]/A(x(t)),
Gamma=gamma/tau, Omega2=C/tau, K=a_r Delta_b/C.

Then H=a_r[w+b(x)/C]. Direct substitution cancels the static b term:

H''+Gamma H'+Omega2 H = K B''+K Gamma B'.                (3)

No instantaneous coordinate step appears. All finite ramps are evaluated through their actual history. There is no reset, prepared hidden state, equilibrium wait or continuous-frequency alias selection in this identity. This does not remove the independently calibrated moving-force correction N.

For any test function phi with phi=phi'=0 at its two support endpoints, integration by parts gives

int H phi'' - Gamma int H phi' + Omega2 int H phi
 -K int B phi'' + L int B phi'=0,   L=K Gamma.            (4)

The recorded force/coordinate functions are not differentiated. The known test functions are differentiated. Quadrature/timing and calibration errors still need bounds.

Rows X=(-int H phi', int H phi, -int B phi'', int B phi')
and y=-int H phi'' give X theta=y for theta=(Gamma,Omega2,K,L).
If the measured feature matrix has column rank4, the exact coefficient tuple is unique for these rows. This is conditional identification from data, not a derivation of numerical coefficients from axioms. A physical member must additionally satisfy

Gamma>=0, Omega2>0, K!=0, L=Gamma K,                      (5)

and agree with the separately calibrated s,p via exp(A_hidden Delta). A common four-coefficient linear fit that fails L=Gamma K is not the stipulated non-derivative-forcing model. Unknown coefficients must be frozen from development histories before reserved histories and test functions are examined.

The continuous parameters obtained through equation4 can be compared with all discrete aliases. We do not choose an arbitrary Nyquist branch. A finite passing collection of weak tests remains insufficient to certify the differential equation on all histories; the prior campaign's finite-span blindness example still applies.

## 3. Test reciprocal interaction instead of selecting it

The separate candidate potential condition a=lambda b_x for constant lambda>0 is equivalent to B_x=kappa A for constant nonzero kappa, with kappa=a_r/(lambda Delta_b). Hence

K kappa = a_r^2/(lambda C)>0.                            (6)

The independently reconstructed function relation and the fitted common K can therefore test shape and sign without using an instantaneous pulse-end sign or choosing an action normalization. It does not uniquely identify u, lambda, C, tau, a_r or Delta_b separately, nor establish a global potential outside the calibrated interval.

## 4. Deterministic error control

If |A|>=a_min>e_A, |Y|=|R-m|<=M_Y, and errors in R,m,A are bounded by e_R,e_m,e_A, then

e_H=(e_R+e_m)/(a_min-e_A)
        +M_Y e_A/[a_min(a_min-e_A)]                      (7)

bounds the quotient error. For fixed candidate coefficients and B error e_B, the change in the equation4 residual is bounded by

e_H (||phi''||1+|Gamma| ||phi'||1+Omega2 ||phi||1)
+|K| e_B (||phi''||1+|Gamma| ||phi'||1).                   (8)

Equation8 uses L=Gamma K. If an unconstrained four-parameter fit is being checked instead, replace |K Gamma| by |L| in the B phi' term. These are deterministic envelopes, not Gaussian significance levels. Include numerical quadrature, timing, continuum function error and N uncertainty in their respective budgets; estimates that omit them are not certified.

## 5. Division-free necessary form at coupling zeros

A regular-chart quotient is optional for a necessary test when A crosses zero. Put Y=R-m and let A denote A(x(t)); primes on A now mean time derivatives. Define

L0=A^2 phi''+6AA' phi'+(6A'^2+3AA'')phi,
L1=-A^2 phi'-3AA'phi,
L2=A^2 phi.

Multiplying the classical equation for Y/A by A^3 and integrating by parts gives

int Y L0+Gamma int Y L1+Omega2 int Y L2
 -K int AB L0-K Gamma int AB L1=0.                       (9)

It extends as a polynomial identity through zeros for smooth true candidate histories. Direct identities (A^3 phi)''=A L0 and -(A^3 phi)'=A L1 verify the source terms. This form needs A' and A'' calibration; it does not remove derivative uncertainty. If A vanishes identically on an interval, every weight is zero there and the test is blind. Necessary does not mean sufficient, and multiplying through zeros does not establish hidden-state observability.

## Computation and separation

The author controls verify the offset, weak-form coefficients, error bounds, variable-mass load term and division-free identity. A synthetic model uses different hidden preparations and smooth coordinate histories. Development rows estimate one theta; separate synthetic histories/test windows challenge that frozen tuple. A derivative-forcing alternative retains the same clamped offset but violates L=Gamma K. A deliberately omitted moving-force correction is also tested. These are numerical mechanism controls, not new physical observations or an independent empirical test.

This is a useful continuation of known system-identification and integration-by-parts methods. No stand-alone novelty claim or immediate new PR is warranted without a substantive physical test. The source port construction, smooth-history residual and explicit correction obligations will be carried together into an actual calibrated record if one is available. Neither a chosen fitting basis nor a selected calibration law counts as a derived scalar action or physical scale.

