# Conformal endpoint matching and the actual scalar charge

Root derivation, 2026-09-30. Conditional research, independently unchecked at
this freeze. The law is the literal continuum definition in provisional
PR9398 at bd6f6e6368d615bfc0437760e2396cd471837cd7, not a native axiom. Mean
below is normalized coordinate integration on the period-2pi three-torus.
All data are smooth, real and periodic; a,K>0. An endpoint construction is
not a time evolution or an event law.

## 1. Literal constraint reduction

For a positive function psi and a spatial constant lambda set

    g_ij=psi^4 delta_ij,  pi^ij=lambda psi^2 delta^ij,
    S=psi^6,  c=3a lambda^2/2.

The density momentum is pi, not an ordinary tensor. The actual gravitational
spatial constraint is

    J_i=pi^jk partial_i g_jk-2 partial_j(pi^jk g_ik).

Its two terms are respectively12 lambda psi^5 partial_i psi and the same
quantity, so J=0. Direct Christoffel contraction gives
R=-8 psi^(-5) Delta psi. Alternatively the general conformal formula follows
by substituting g and its inverse in the literal connection; no lattice
product rule is used. The kinetic density is -c psi^6. Thus with prescribed
coordinate matter energy density rho>0 and j=0, the full scalar constraint is

    rho=c psi^6-8K psi Delta psi,                         (1)

or, dividing by the positive psi,

    -8K Delta psi+F_c(x,psi)=0,
    F_c(x,t)=c t^5-rho(x)/t.                             (2)

This retains all density factors. The results below concern continuum
endpoints; no exact finite-grid constraint statement is inferred.

## 2. Existence and uniqueness for every positive density

For c>0 and 0<rho_min<=rho<=rho_max, let
l=(rho_min/c)^(1/6), u=(rho_max/c)^(1/6).
The constants l,u are sub/supersolutions of(2). On[l,u],

    partial_t F_c=5c t^4+rho/t^2>0.

Choose beta at least the maximum of this derivative on the compact box.
The inverse of L_beta=-8K Delta+beta preserves positivity; explicitly it is
integral_0^infinity exp(-beta t) exp(8Kt Delta) dt, whose periodic heat kernel
is positive. Starting psi_0=l, iterate

    psi_(r+1)=L_beta^(-1)[beta psi_r-F_c(x,psi_r)].         (3)

The bracket is increasing as a function of psi on[l,u]. The sub/supersolution
inequalities therefore give l<=psi_r<=psi_(r+1)<=u. Its right-hand sides are
uniformly bounded. Periodic elliptic estimates for the fixed positive
constant-coefficient L_beta bound psi_r in W^(2,p) for every finite p.
Dominated convergence of the bounded monotone sequence and the smooth
nonlinearity gives strong convergence of the right-hand sides in L^p;
the same inverse estimate then gives convergence in W^(2,p). For p>3 this
implies C^1 convergence, and elliptic bootstrapping gives a smooth solution
of(2). All estimates occur on a positive compact t interval, so no singular
logarithm or zero of psi is being crossed.

Any positive solution lies in[l,u]: evaluate(2) at its minimum and maximum.
If psi_1,psi_2 solve it, subtract the equations, multiply by their difference
and integrate. The gradient term is nonnegative, and the strict increase
of F_c makes the remaining integrand strictly positive wherever they differ.
Consequently the solution is unique. This proves all-size existence and
uniqueness at fixed finite smooth density; it is not a small-amplitude or
sampled-rank claim. The named mathematical inputs are the positive periodic
heat kernel and constant-coefficient elliptic regularity, under their
explicit compact-domain, positive-beta and smooth-coefficient hypotheses.

## 3. Fixed original trace: a global geometric response

Now fix the original lambda!=0 and rho0=c=3a lambda^2/2, and prescribe
rho=rho0+f with f>=0. The solution obeys

    1<=psi<=(1+||f||_infinity/rho0)^(1/6).                (4)

If f is not identically zero, psi>1 everywhere. To prove strictness without
assuming f positive everywhere, put v=psi-1. Subtract F(x,1)=-f to obtain

    -8K Delta v+b(x)v=f,
    b=rho0 sum_(j=0)^4 psi^j+(rho0+f)/psi>0.             (5)

Choose beta>=sup b. Then v=L_beta^(-1)[f+(beta-b)v]. Its source is
nonnegative and nonzero, and the positive heat-kernel representation makes
v strictly positive at every point. In particular a localized f cannot
produce an exactly compact conformal perturbation in this fixed-trace
family. This is a constraint response, not instantaneous signal propagation.

Integrating(1) gives the exact energy identity

    E:=mean f=rho0(mean psi^6-1)+8K mean|grad psi|^2.       (6)

Both terms are nonnegative. There is a geometric escape from the previous
fixed-flat-metric endpoint boundary, with explicit global spatial cost.
For f=0 the unique solution is psi=1. At lambda=0, a nonnegative nonzero
rho=f would force Delta psi=-f/(8Kpsi)<=0 everywhere, impossible on the
periodic torus. For f=0 and lambda=0, every positive constant psi solves
(1). This zero-trace boundary is the standard closed conformal positive-
source obstruction, already represented in the matched main prior art.

For an infinitesimal source t f at the positive background, differentiating
(2) yields

    (-8K Delta+6rho0)v=f,
    vhat(k)=fhat(k)/(8K|k|^2+6rho0).                     (7)

Invertibility and smooth dependence follow from the positive derivative
operator on the compact torus. Equation(7) is a normalization/zero-mode
control; no physical screening law is derived from its supplied constants.

## 4. Matching the actual scalar source exposes a conserved charge

In the supplied massless scalar action, a constant phi has j=w grad phi=0
and density rho=w^2/(2S). Its positive branch at the endpoint is therefore

    w=psi^3 sqrt(2rho),  Q=mean w,
    w_initial=Q0=sqrt(2rho0).                            (8)

At fixed original lambda and nonzero f>=0, equations(4)-(5) give w>w_initial
pointwise. In particular Q>Q0. Writing M=||f||_infinity, one quantitative
bound is

    sqrt(2)E/[sqrt(rho0+M)+sqrt(rho0)] < Q-Q0
                                <=sqrt(2/rho0)E.        (9)

The strict lower bound follows from psi>1 and
sqrt(rho0+f)-sqrt(rho0)=f/[sqrt(rho0+f)+sqrt(rho0)].
For the upper bound use Cauchy-Schwarz,
Q^2<=2 mean(psi^6) mean(rho), followed by(6). Equality in the upper bound
requires constant psi and hence constant f. For constant f it is attained:
psi=(1+f/rho0)^(1/6), w=Q0(1+f/rho0). Equation(7) also gives
Q-Q0=t sqrt(2/rho0) mean f+O(t^2), consistent with this control.

The actual canonical massless scalar equation, for arbitrary smooth supplied
lapse N and shift X on the torus, is

    wdot=aK partial_i(N S g^ij partial_j phi)
                           +partial_i(X^i w).           (10)

It follows directly by varying the gradient energy and spatial generator in
PR9398's action. Thus Qdot=0. A smooth closed solution of that action cannot
connect the initial and fixed-lambda endpoint above while retaining those
source and positive-branch assumptions. This is a conservation obstruction
for this endpoint specification, not a no-go for gravity, a physical record
clock, energy injection in general, or an open reservoir coupling. A rule
that resets the external clock density to (8) changes the input law; it does
not evade the charge equation inside the original closed action.

## 5. Declared extension: one global trace parameter can match the charge

This section deliberately relaxes the fixed-lambda contract and asks a
separate endpoint question. Hold rho=rho0+f fixed, but allow c=3a lambda_c^2/2
in(2) to vary over positive constants. Section2 supplies a unique psi_c for
every c. If c2>c1, their equations and strict monotonicity show
psi_(c2)<psi_(c1) everywhere: subtraction produces a positive elliptic
operator on their difference with a strictly signed source
(c2-c1)psi_(c1)^5. Therefore

    Q(c)=mean[psi_c^3 sqrt(2rho)]

is strictly decreasing. It is continuous by the positive linearized
elliptic inverse, or directly by uniform compact-parameter elliptic bounds
and uniqueness. The barriers imply

    sqrt(2rho_min/c) mean sqrt(rho) <= Q(c)
                  <=sqrt(2rho_max/c) mean sqrt(rho).

Hence Q(c) ranges continuously from infinity to zero. There is exactly one
c_* with Q(c_*)=Q0. If f is nonzero and nonnegative, section4 implies
c_*>rho0. Integrating(1), then Cauchy-Schwarz at Q=Q0, gives

    rho0 < c_* <=(rho0+E)^2/rho0,
    |lambda| < |lambda_*| <= |lambda|(1+E/rho0).         (11)

For the second step, Q0^2<=2 mean(psi^6) mean(rho) implies
mean(psi^6)>=rho0/(rho0+E), while
c_* mean(psi^6)<=rho0+E. Equality is attained for constant f and is strict
at the upper end for nonconstant f because its psi is nonconstant.
The sign of lambda_* may be kept equal to the initial expansion/contraction
branch; its absolute value is fixed by c_*.

This supplies endpoints satisfying all four constraints AND the integrated
scalar charge, after a nonlocal trace adjustment. It does not prove a
trajectory between them, pointwise conservation across an instantaneous
jump, or a physical source mechanism. For nonzero f the charge condition
forces psi<1 somewhere: otherwise w>=sqrt(2rho)>=w_initial and Q>Q0.
If f vanishes on an open exterior region, psi cannot equal1 there, since
(1) with c_*>rho0 and Delta psi=0 would fail. Thus the adjustment is not a
compact local event map. Scalar density redistributes; it is not replaced
by an original rotor record density.

## 6. Premises and remaining consumer

This is an elementary prescribed-density conformal construction and a
Noether-charge check in a supplied continuum model. It uses standard
elliptic mathematics with checked positivity/domain hypotheses. It does
not improve the original staggered exact lattice algebra or convert an
analytic approximation into a finite first-class law. Smooth compact source
data here are not analytic; no application of PR9398's analytic-time theorem
is asserted. Analytic data would require its additional quantitative radius
and small-metric hypotheses before such an application.

The actual missing consumer is a source/event action specifying stress,
scalar charge transfer and energy/work in the same state, whose transitions
preserve the full constraints. Endpoint solvability and integrated charge
matching are necessary checks, not that action. The standard conformal
formula, static positive-source boundary and existence machinery are not
claimed as newly discovered mathematics. The useful campaign distinction is
which previously fixed endpoint assumptions a record-source proposal must
relax or supply. No physical identification, axiom change, review grade or
formal audit is claimed.
