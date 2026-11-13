# Actual compact rough-cell density at two steps

Author derivation, checked in fresh context as recorded in
`../gates/forest-flat-check.md`. This uses the deterministic
energy inequality in `compact-energy-coercivity.md`, with its explicit
fixed-depth, fixed-L, fixed-kappa, terminal V=I hypotheses. It gives an
actual full-compact posterior bound. It does not give a connected
rough-component activity estimate or the desired full response decay.

## 1. Exact measure and counts

Use the same periodically translated terminal-block trees as the flat
two-step proof. Let M be the number of terminal blocks. The numbers of
remaining compact links and of normalized kernel factors per block are

 n_L=3L^8+1+4L^4,       k_L=4L^4+4.

Indeed the fine forest has L^8-1 edges per block; there are 4L^8 fine
positive links, 4L^4 intermediate links, and four terminal links per block.
All compact reference Haar measures have mass one. Put s(a)=1-w(a).
In exact quotient coordinates the full posterior density is

 p_u(a)=exp[-u E(a)] product_(h,c) H(kappa u r_(h,c)(a)),
 H(z)=exp(z)/Z(z),
 E=W0+kappa sum gamma0+kappa sum gamma1,
 pi_u=p_u da/Z_u.                                           (R1)

There is no hard field cutoff in (R1). Both kernel families and every
fine-field-dependent normalizer are retained. The forest orbit has already
been integrated by the exact probability-Haar disintegration.

Let c_E(L,kappa)>0 be the deterministic constant satisfying

 E(a)>=c_E sum_(all remaining e) s(a_e).                     (R2)

All constants below may depend on L,kappa and the chosen fixed chart size,
but not on M or u>=1. They are existence constants, not evaluated numbers.

## 2. Uniform radial estimates and the partition function

The Haar variable X=1-w(q) has density (2/pi)sqrt(x(2-x)) on [0,2].
The elementary integral estimates in the nonlinear chart proof give
positive a_H,b_H such that, for all z>=0,

 a_H(1+z)^(3/2) <= H(z) <= b_H(1+z)^(3/2).                 (R3)

For completeness, for z>=1 the Laplace integral 1/H(z) is bounded below
by integrating 0<=x<=1/z and above by replacing sqrt(2-x) by sqrt(2)
and extending to infinity. Both bounds are constant multiples of z^(-3/2).
For 0<=z<=1 the positive continuous integral has upper and lower bounds.
This proves (R3), including z=0; it is not an asymptotic approximation.

Choose b>0 small enough that the coordinate cube |a_e,r|<=b has
r_(h,c)>=1/2 for every kernel, using the contour-length bound. E is
smooth there, E(0)=0 and grad E(0)=0. The bounded local Hessian and
finite incidence give E(a)<=C_E sum_e |a_e|^2 on this cube, uniformly
in volume. This is an upper bound in a small neighborhood, distinct
from the global lower bound (R2).

Restrict the partition integral only for a lower estimate to the smaller
product cube |a_e,r|<=b/sqrt(u). There E<=3C_E b^2 n_L M/u.
Each compact Haar cube has measure at least c_b u^(-3/2), since its
exponential-coordinate Haar density is bounded below on the fixed cube.
Each of the k_L M normalizer factors is at least
a_H(kappa u/2)^(3/2). Thus some A_->0 satisfies

 Z_u >= A_-^M u^((3/2)(k_L-n_L)M),    u>=1.                (R4)

No estimate of the probability of the small cube was used. Restricting
an unnormalized integral is legitimate here because all factors are positive.

For 0<=theta<=1/2 let

 Z_u^(theta)=int exp[-(1-theta)u E(a)] product H(kappa u r) da.

Since r<=1, (R3) bounds each H from above by B_kappa u^(3/2).
Using (R2) factorizes an upper bound into compact one-link Haar integrals:

 Z_u^(theta) <= [B_kappa u^(3/2)]^(k_L M)
          [int_SU2 exp[-(1-theta)u c_E s(a)]da]^(n_L M).

The last integral is 1/H((1-theta)u c_E). By (R3), it is at most
C_E' u^(-3/2), uniformly for theta<=1/2. Hence some A_+<infinity gives

 Z_u^(theta) <= A_+^M u^((3/2)(k_L-n_L)M).                (R5)

The powers of u match exactly in (R4),(R5). Omitting kernel normalizers
or the forest removal would change this count and the argument.

## 3. Full-compact energy and rough-density bounds

Set C_0=log max(1,A_+/A_-). Dividing (R5) by (R4) at theta=1/2 yields

 E_pi exp[(u/2)E] <= exp(C_0 M).

Jensen's inequality and (R2) consequently prove

 E_pi E <= 2C_0 M/u,
 E_pi sum_e s(a_e) <= 2C_0 M/(c_E u).                     (R6)

Use, if necessary, an enlarged C_0>0 so the statement includes trivial
degenerate constant bounds without interpreting C_0=0 as an evaluated claim.
These estimates are uniform in the finite volume and use the actual
posterior, including all compact fields. They do not condition on a
good-history event or postulate concentration.

Translation by a terminal block preserves the measure, trees and the
tail-block assignment of every remaining positive link. Thus for each
terminal block X,

 E_pi sum_(tail(e) in X) s(a_e) <= 2C_0/(c_E u).           (R7)

Fix 0<delta<pi/sqrt(3), with the cube in the principal exponential chart.
Call X rough if at least one of its remaining links lies outside that
coordinate cube. Outside the cube the principal angle r is at least
delta (including the -I cut point), so that link has
s(a)>=epsilon_delta=1-cos(delta)>0. Markov's inequality gives

 pi_u(X rough) <= min(1, 2C_0/(c_E epsilon_delta u)).       (R8)

For a prescribed finite collection S of terminal blocks, the union bound
therefore gives pi_u(some X in S rough)<=C_delta |S|/u. This is a bound
for a local marginal, with the rest of the compact system fully integrated.
It is valid at the homogeneous terminal field V=I. It is not asserted
uniformly in arbitrary V, u-dependent L, or depth.

## 4. What the attempted response extension still needs

(R8) controls density, not the joint spatial arrangement of rough cells.
For a specified set S required to be rough, (R2) gives E>=c_E epsilon_delta
|S|. The proved global moment estimate would only give

 pi_u(all X in S rough)
   <= exp[C_0 M-(u c_E epsilon_delta/2)|S|].               (R9)

The volume M in this bound cannot be replaced by |S| using (R4),(R5).
Those bounds deliberately compare two bulk integrals; their constants
need not cancel outside S. In particular (R9) does not supply a local
polymer weight or connected-support estimate in the thermodynamic limit.

One must control a localized normalized integral with the same exterior,
retaining all boundary normalizers and source insertions, so that only
the readers of the rough component and its necessary collar are paid.
The fixed-chart covariance proof supplies the good-region response when
its collar is controlled, and (R8) supplies an actual compact rough-density
estimate. A proof that composes these into the requested supported
two-source response is still absent. Neither these inequalities nor
their combination establish the Yang--Mills mass gap.
