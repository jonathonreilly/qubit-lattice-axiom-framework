# Independent derivation from the neutral contract

This argument and the fixtures below precede any reading of the listed author
note, runners, controls or recovery record. The neutral contract is separately
preserved. No prior campaign conclusion is used as authority. This is a local
conditional inverse problem, not a claim that its inputs are measured.

## 1. Equations, density and reconstruction

Use Einstein proper time and signature (-,+,+,+). Put v=phi_dot and
r=A rho, where rho=rho_* a^-3 is conserved bare dust density. Varying the
canonical scalar and pressureless particle action gives

    3 M^2 H^2 = v^2/2 + V + r,
    -2 M^2 H_dot = v^2+r,
    v_dot+3 H v+V_phi+alpha r = 0,
    r_dot+3 H r = alpha v r.                         (I)

The last equation follows directly by differentiating A rho; scalar and dust
energy exchange cancel in the total continuity equation. Treating r as a
conserved a^-3 density when alpha v is nonzero would be wrong.

Define Q=-2 M^2 H_dot and J=Q_dot+3 H Q. Every allowed history requires Q>0
and 0<v^2<Q throughout the connected open interval. Raychaudhuri fixes
r=Q-v^2, and dust conservation then fixes the first-order velocity flow

    v_dot = F(t,v)
          = J/(2v) - 3 H v/2 - alpha Q/2 + alpha v^2/2.       (II)

For any candidate satisfying (II) and the open domain, set

    a(t)=a0 exp(integral H dt), rho=rho_* a^-3,
    phi(t)=phi0+integral v dt,
    A(phi(t))=(Q-v^2)/rho,
    V(phi(t))=3 M^2 H^2-Q+v^2/2.                    (III)

Since v never vanishes, phi is invertible on its image. These are positive A
and C2 action functions on that image under the supplied regularity. Equation
(II) makes (log A)_dot=alpha v. Differentiating the Friedmann value in (III)
gives V_phi=-v_dot-3 H v-alpha r, so the scalar equation follows without a
remaining force integration constant. The potential value is fixed by
Friedmann, rather than by integrating its second derivative alone.

## 2. Fixed-density mass versus the derivative along the history

The force S=V_phi+rho A_phi=V_phi+alpha r obeys

    S_dot = (V_phiphi+rho A_phiphi) v - 3 H alpha r
          = mu v-3 H alpha r.                         (IV)

The density held fixed in the definition of mu is the bare rho. It is not
held fixed while differentiating along the expanding history. Thus the
second compatibility equation is

    v_ddot+3 H v_dot+(3 H_dot+mu)v-3 H alpha(Q-v^2)=0.  (V)

Necessity follows by differentiating the actual scalar equation. Sufficiency
uses (III), for which the scalar equation already holds: differentiating it
and using (V) gives precisely the supplied fixed-rho curvature. Therefore
(II), (V), and the domain are a necessary and sufficient description of
histories and local action restrictions for the neutral contract.

If one instead only differentiates a putative scalar equation, its residual
can be an arbitrary constant. Integrating mu leaves an affine potential
ambiguity. In the exact fixture below, replacing V by V+c phi+d leaves
V_phiphi and hence mu unchanged, but gives scalar residual c and Friedmann
residual -c phi-d. Enforcing (III) excludes both constants. A constant energy
shift is not an unfixed freedom once H, M, r and v are fixed.

## 3. Algebraic compatibility and its limits

Substituting (II) into (V) gives R(t,v)=0, where

    R=F_t+F_v F+3 H F+(3 H_dot+mu)v-3 H alpha(Q-v^2).

Multiplication by 4v^3 is reversible on the stated domain. The anticipated
polynomial, to be checked independently by symbolic differentiation, is

    P=2 alpha^2 v^6+(2 alpha_dot+9 H alpha)v^5
      +(6 H_dot-9 H^2+4 mu-2 alpha^2 Q)v^4
      +(-2 alpha_dot Q-alpha Q_dot-12 H alpha Q)v^3
      +(2 J_dot+6 H J)v^2+alpha Q J v-J^2.             (VI)

One must solve the first-order flow AND this algebraic constraint. Selecting
a root independently at each time is insufficient, even if it is smooth.
F is C1 on v!=0 and hence locally Lipschitz in v. A specified signed v(t0)
has at most one compatible history; existence across the whole requested
interval and satisfaction of (VI) are separate requirements. Distinct
solutions cannot meet at an interior time.

If P is not identically zero as a polynomial at any one time, there are at
most six admissible histories on the whole interval, counted by their
distinct velocities at that time. This is only an upper bound, not a claim
of six realizations. If alpha is identically zero and the constraint is
nontrivial, the polynomial is even of degree at most four, giving the
corresponding upper bound four. Spurious roots and boundary roots can reduce
either count.

An infinite set of distinct histories would supply infinitely many distinct
roots at every time. Consequently P must vanish identically in v at every
time. Its leading and constant coefficients force alpha=0 and J=0; the
remaining condition is

    mu=(9 H^2-6 H_dot)/4.                             (VII)

Conversely, when these relations and Q>0 hold throughout the interval, (II)
reduces to v_dot=-3 H v/2 and Q_dot=-3 H Q. All constant ratios

    v^2/Q=eta, 0<eta<1,

with either fixed sign of v give allowed histories on the interval. Thus
this exceptional class has a continuous one-parameter history ambiguity
(plus sign and the scalar-origin convention). This is not only an isolated
point at which a polynomial loses degree.

## 4. Independent exact nonzero-coupling fixture and a false root

Use numerical units M=1, reference time t_*=1 and rho_*=1 with a(1)=1;
all following time powers are powers of t/t_* in those fixed units. On t>0,

    a=t, H=1/t, phi=log t, v=1/t,
    rho=t^-3, A(phi)=exp(phi), r=t^-2,
    V(phi)=3 exp(-2 phi)/2, alpha=1, mu=7/t^2.         (VIII)

The scalar fixed-rho mass has separate contributions 6/t^2 from V and
1/t^2 from rho A_phiphi. In contrast S=-2/t^2 and S_dot/v=4/t^2. The
3/t^2 difference directly tests the density term in (IV).

Putting x=t v, the polynomial constraint in this fixture is

    t^6 P(t,x/t)=2x^6+9x^5+9x^4-20x^3+4x-4.          (IX)

For a constant x, the flow requires

    t^2(v_dot-F)=-(x-1)(x^2-2)/(2x).

The polynomials in (IX) and (x-1)(x^2-2) have only x-1 as common factor.
There is also a root of (IX) between -3/4 and -1/2, inside the allowed domain
0<x^2<2, which does not obey the velocity flow. This supplies a smooth
pointwise compatibility-root counterexample, rather than a root-switching
artifact. Since (IX) has finitely many constant roots, any continuous
compatible x(t) must be one of those constants; only x=1 survives. The
fixture therefore has a unique allowed velocity history despite the extra
algebraic root. Symbolic factor/gcd and interval checks will test this claim.

## 5. Explicit continuous family with identical supplied inputs

For dimensional clarity retain M, a reference time t_*>0 and rho_*>0 with
a(t_*)=1. For any nonzero lambda with lambda^2<4 M^2/3, take

    H=2/(3t), a=(t/t_*)^(2/3), rho=rho_* (t/t_*)^-2,
    phi=phi0+lambda log(t/t_*), v=lambda/t,
    r=(4 M^2/3-lambda^2)/t^2,
    A=(4 M^2/3-lambda^2)/(rho_* t_*^2),
    V(phi)=lambda^2/(2 t_*^2) exp[-2(phi-phi0)/lambda]. (X)

Every member has the same H, signed alpha=0, and mu=2/t^2, while obeying all
four equations (I). The ratio of dust to scalar kinetic energy changes with
|lambda|, as do the constant conformal factor and canonical potential slope.
Different |lambda| are not scalar-origin translations or canonical field
reflections. Fixed rho_* and a normalization do not select lambda from the
three input functions. In units M=t_*=rho_*=1, lambda=1/2 and lambda=1 give
A=13/12 and A=1/3, respectively. The excluded endpoints lambda=0 and
lambda^2=4 M^2/3 violate the v!=0 and r>0 assumptions.

## 6. Calibration, labels, regularity and physical scope

For a chosen history, known rho_* and a normalization fix the absolute A in
(III). If the bare-density normalization is unspecified, rescaling rho by
1/c and A by c leaves r, alpha and mu unchanged; this is an additional
normalization freedom, not a measured scale. A supplied A(t0)>0 together
with rho(t0) fixes v(t0)^2=Q(t0)-A(t0)rho(t0), leaving at most two signs
before compatibility is checked. A supplied signed v(t0) leaves at most one
history. A scalar origin phi0 is a field-label convention; reflection is
likewise indistinguishable in the uncoupled alpha=0 family unless orientation
is fixed by additional information. This argument does not count translations
as distinct physical histories.

M fixes the gravitational normalization; with mass units, phi and M have
dimension mass, H has inverse-time dimension, v has mass/time, r and V have
mass^2/time^2, alpha has inverse-mass dimension, and mu has inverse-time^2
dimension. The fixed-rho derivative has these dimensions. No absolute scale
or initial condition is derived merely by differentiating an equation.

H C3, alpha C1 and continuous mu suffice for the displayed flow and
compatibility expressions. No derivative of mu is required. Boundaries
v=0 or r=0, a turning scalar, disconnected intervals, other matter species,
spatial curvature and noncanonical kinetic terms lie outside the contract.
The inverse fixes action functions only on the traversed open scalar range;
global extension, stability and cosmological history outside the interval
are separate. The defined fixed-rho mu is not automatically an observed
normal-mode mass of a coupled scalar/dust/gravity perturbation system.
No measurement procedure for Einstein-frame H, alpha or mu is supplied here.

## 7. Frozen controls before code or author exposure

The independent implementation will: derive the dust flow and polynomial by
symbolic differentiation; verify reconstruction identities; test all field
and dust equations and fixed-rho derivatives for (VIII) and (X); test exact
domain inequalities and excluded endpoints; prove the spurious-root and
uniqueness statements by rational polynomial/gcd/root-interval operations;
test the affine-potential residuals and the density-normalization freedom;
and test the exceptional polynomial identically zero conditions directly.
Numerical evaluation, if needed, is synthetic and subordinate to these exact
identities. Every owned execution is bounded at 120 seconds, with bytecode
disabled and full stdout/stderr preserved. Actual failures will remain in
the evidence rather than being overwritten. Only after independent outputs
are frozen will the author note, code and results be opened.
