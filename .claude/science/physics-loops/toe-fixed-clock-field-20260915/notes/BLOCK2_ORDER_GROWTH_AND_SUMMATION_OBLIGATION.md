# What the fixed-order construction costs as the order grows

Personal growth accounting, 2026-09-15. The estimates below are deliberately
loose upper bounds for the stable cut-completion construction. They do not
show that the actual coefficient series diverges or that another summation
method fails.

## 1. A coarse explicit growth class

Fix parameters satisfying g^2/128,b^2/128>log393, a smooth macroscopic
source f and a bounded complex source disk |z|<=R. All constants below
may depend on those fixed objects, but not on n, a or component restrictions.
Let R_(n_e,n_m),a(z) be the subtracted source coefficient in the cut note,
with n=n_e+n_m>=1. The existing construction can be bounded by

    sup_(|z|<=R) |R_(n_e,n_m),a(z)|
        <= a^3 A B^n (n!)^50                          (1.1)

for finite A,B. The exponent 50 is a conservative allowance, not an
optimized order or a lower bound on the coefficient growth.

Here is sufficient bookkeeping. A completed graph has K>=4 source legs,
K<=n+4, and total edge multiplicity M<=3n+2. In the tree-mixture Holder
argument, every spatial edge satisfies

    1-alpha_e >= 1/[8(K-1)M]
                  >= 1/[8(n+3)(3n+2)].               (1.2)

The lattice shell count gives ||kappa||_p<=C max(1,(p-1)^(-1)) for p>1.
Since p=1/alpha, this costs at most C n^2 per spatial edge. There are
at most 3n-2 such edges, so their combined cost is at most C^n n^(6n).

Use (1+m_i+m_j)^4<= (1+m_i)^4(1+m_j)^4 in the spatial filling majorant.
A single odd edge then contributes at most sixth degree in each endpoint
mass; two copies cover an even Coulomb bond. A hard-core bond needs at
most eighth degree at each endpoint across its two spatial copies, which
is smaller. A source leg needs at most second degree in its endpoint mass.
The total mass polynomial degree is consequently at most

    D <= 12 E_spatial + 2K
       = 12M-10K <= 36n-16 <= 40n.                    (1.3)

At n=1 the direct four-source term has degree eight and also fits 40n.
Let tau=min(g^2,b^2)/128-log393>0. For an integer d>=0,

    sum_(m>=1) (1+m)^d exp(-tau m)
       <= d! (4/tau)^d/[exp(tau/2)-1].                (1.4)

Indeed (1+m)^d<=2^d m^d and m^d<=d!(2/tau)^d exp(tau m/2).
Thus all shape sums cost at most C^(D+n) product_i d_i! <= C^n (40n)!,
after absorbing fixed parameters. The normalized cubic marks do not
increase the count. The multinomial theorem gives
(40n)!<=(40^(40))^n (n!)^40.

There are n^(n-2) labeled trees for n>=2 and at most 2^(n-1) choices of
their derivative pieces. At each of at most n completion steps there
are at most n(n-1)/2+n differentiated pair/source choices. Bounding the
entire branching expansion therefore costs at most C^n n^(2n). The
four initial source choices contribute n^4, absorbable into another C^n.
All interpolation measures have bounded total mass as normalized in the
cut note. Finally

    n^(n-2)/(n_e!n_m!) <= (2e)^n,
    n^(8n) <= e^(8n) (n!)^8.

These estimates give an exponent at most 48 with the stated loose mass
bound. Enlarging it to 50 and adjusting A,B handles n=1 and harmless
finite normalizations, establishing (1.1). No fitted constant or computed
coefficient is used in this growth accounting.

## 2. Why this still does not sum the physical law

The majorant in (1.1) is not summable in n at any fixed nonzero activity.
This is a limitation of that majorant, not a proof of divergence of the
original series. A large fixed suppression per component can improve B;
it cannot turn this factorial majorant into a convergent geometric series.
Neither ordinary Borel summability nor reconstruction of the physical
partition function follows from a factorial coefficient bound alone.
Those would require new analyticity, remainder and identification results.

There is also a simple probability example showing why coefficientwise
Gaussian behavior alone is insufficient. For 0<=lambda<=1, take

    mu_(m,lambda)=(1-lambda^m) N(0,1)
                         +lambda^m [delta_(-1)+delta_(1)]/2.

Its characteristic function is

    phi_(m,lambda)(t)=exp(-t^2/2)
         +lambda^m[cos t-exp(-t^2/2)].

For every fixed activity order r, the coefficient of lambda^r in
log(phi_(m,lambda)(t)) agrees with the Gaussian value once m>r, locally
in lambda near zero. But at lambda=1 the law is always the two-point
Rademacher law, with fourth cumulant -2. Both mixture components even
have the same variance. This is an abstract counterexample to an invalid
interchange of quantifiers; it is not a counterexample to the clock model.

## 3. Next work selected by this accounting

The high cost comes from taking absolute spatial norms after cut completion
and from broad filling-moment bounds. The earlier signed sine operator
and cycle estimates address a different norm and might improve this cost,
but their use through the residual interactions remains to be proved.
The new cut construction identifies precisely where signs can be retained
before a divergent absolute norm is introduced. A successful next step
needs a summable bound or a separately controlled nonperturbative remainder,
not more fixed coefficients or a renamed convergence assumption.
