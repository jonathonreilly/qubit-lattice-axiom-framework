# Uniform infrared remainder and a second coefficient derivation

This completes the proposed asymptotic step in BLOCK05_DERIVATION.md before
its finite challenges. The model is the free arithmetic lapse family, fixed
zeta in[1/2,1), with the thermodynamic susceptibility defined by(S9)'s integral.
The limit is q->0 after that integral; no finite-box power fit is used.

Define for nonzero p,p+t

    f(p,t)=[(|p+t|-|p|)^2/(4(|p+t|+|p|))]
                              [1-p.(p+t)/(|p||p+t|)].

It is nonnegative. The bound f<=(|p|+|p+t|)/2 extends it boundedly across
the exceptional points in any bounded region. For |t|<=|p|/2, write r=|p|,
u=p/r. Homogeneity gives f(p,t)=r f(u,t/r). On the compact set |u|=1,
|t/r|<=1/2, all derivatives through order5 in t/r are bounded. Moreover,

    |p+t|-r=u.t+O(|t|^2/r),
    1-u.(p+t)/|p+t|=|t-u(u.t)|^2/(2r^2)+O(|t|^3/r^3).

The denominator is8r+O(|t|). Multiplication gives the uniform estimate

    | f(p,t) - (u.t)^2[|t|^2-(u.t)^2]/(16r^3) |
                         <= C |t|^5/r^4.                  (IR1)

The compact derivative bound justifies the constant uniformly over all
directions, including u.t=0. No division by a directional scalar is used.

At each simple node k*, d is a diffeomorphism in a fixed neighborhood.
Use a fixed p-ball |p|<delta in its image and its inverse k(p). For all small q,

    t(p,q)=d(k(p)+q)-p=V_* q+R(p,q),
    |R(p,q)|<=C(r|q|+|q|^2),
    |det Dk(p)|=1/|det V_*|+O(r).                        (IR2)

These follow from the bounded second derivatives of d and bounded first
derivatives of k(p). Choose a fixed A large enough that r>=A|q| implies
|t|<=r/2. Inside r<A|q|, the bound on f and(IR2) gives f<=C|q| and the
volume is O(|q|^3); this entire part is O(q^4).

On A|q|<=r<=delta apply(IR1). Its error is C|q|^5/r^4. Replacing t by
Q_*=V_*q in the quartic numerator changes it by at most
C|q|^3|R|/r^3 <= C(|q|^4/r^2+|q|^5/r^3).
The latter term is bounded by a constant times |q|^4/r^2 on this annulus.
Replacing the Jacobian by |det V_*|^-1 contributes another C|q|^4/r^2.
After multiplying by the spherical measure r^2dr, the integrated errors are

    C |q|^4 integral_(A|q|)^delta dr
    + C |q|^5 integral_(A|q|)^delta dr/r^2 = O(|q|^4).    (IR3)

The region outside the fixed node p-balls is compact and bounded away from
zero energy; its integrand is O(q^4). These fixed regions partition the
original Brillouin zone, so no omitted moving-cutoff term is required.
The leading node integral is

    |Q_*|^4/[240 pi^2 |det V_*|]
                        log(delta/(A|q|)).                (IR4)

For fixed invertible V_*, log|Q_*|-log|q| is uniformly bounded on the unit
q-sphere. Replacing the logarithm by log(1/|Q_*|) changes only O(q^4).
Both native nodes have |det V_*|=sqrt(1-zeta^2) and the same |Q_*|, proving

    chi_A(q)=-|Q|^4/[120 pi^2 sqrt(1-zeta^2)]
                              log(1/|Q|)+O(|q|^4).

The estimates prove a bounded fourth-order remainder, not an analytic one.
No uniform constants at the merging-node endpoint are asserted.

## A separate exact cone integral

For one exactly linear cone in p coordinates, let Q=|Q_*|>0 and use the
prolate spheroidal variables with foci0 and-Q_*:

    u=(E+E')/Q in[1,infinity), v=(E'-E)/Q in[-1,1],
    E=Q(u-v)/2, E'=Q(u+v)/2,
    1-n.n'=2(1-v^2)/(u^2-v^2),
    d^3p=Q^3(u^2-v^2)du dv dphi/8.

Substitution into the arithmetic integrand gives the exact product

    f d^3p = Q^4 v^2(1-v^2)du dv dphi/(16u).

With the DECLARED ellipsoidal cutoff E+E'<=Lambda, Lambda>Q, angular and v
integration yields exactly

    integral f d^3p/(2pi)^3
                    =Q^4 log(Lambda/Q)/(240pi^2).         (IR5)

Division by |det V_*| gives the anisotropic cone coefficient independently
of the Taylor expansion. This auxiliary cutoff is a check of the logarithmic
coefficient. It is not the actual Brillouin-zone integral and does not fix its
fourth-order constant or any induced Newton coefficient. In particular,
continuum unbounded Dirac sea traces and their contact terms cannot be moved
cyclically as finite traces without a regulator. The complete second-order
arithmetic/congruence comparison is made on the finite lattice in(S16)-(S18),
where all such operations are legitimate.
