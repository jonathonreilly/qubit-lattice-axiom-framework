# Uniform source coercivity and cancellation of common determinant tilts

Personal derivation, 2026-09-14. This concerns the supplied Gaussian source
family, not a selected native state, a massless theorem or retained status.

## A local Hodge estimate that survives pinning and the fold

Restrict to the released helper's cubic-plaquette construction on an even
spatial width and a temporal cover length divisible by four. The latter
ensures that translation by the half-cover preserves the selected 2x2
differential tiling, including nonzero temporal coefficient. The actual
T_cover=12 fixture and the T_cover=16 challenge satisfy this condition.

Supply volumes v in [5/6,13/6] and shears |s|<=3/5, with the source's local
plaquette Hodge entries

    nu=v,    mu=1/v,    a=v/(1-s^2),    b=-vs/(1-s^2).

Each plaquette contributes one quarter of diag(nu,[[a,b],[b,a]],mu).
Each lattice scalar occupies each of the four plaquette positions once.
Using 2|xy|<=|x|^2+|y|^2 in each off-diagonal pair, its lower row margin
is bounded by

    gamma=(5/6+6/13+2(5/6)/(1+3/5))/4=243/416 > 1/2.

The upper absolute row sum is at most

    Gamma=(13/6+6/5+2(13/6)/(1-3/5))/4=71/20.

The source pin replaces the odd block by v I, so it respects these same
bounds. Antiperiodic folding is restriction to the half-translation's minus
subspace under the normalized isometry x -> (-x,x)/sqrt(2). The Hodge and
selected differential commute with that half-translation in the stated
domain, so its quotient is the corresponding compression. Consequently

    gamma I <= Hq <= Gamma I

on every such cover. Possible edge identifications or cancellations at small
covers reduce the absolute off-diagonal row sum and do not invalidate the
quadratic form bounds. The argument is local; no size fit is involved.

The connection Kq=i(Hd+d*H) after restriction is anti-Hermitian. Thus
q=m Hq+Kq, m>0, has Hermitian part S=mHq and

    Re(x*q x)>=m gamma ||x||^2,
    ||q^-1||<=1/(m gamma).

For c=m/2 or m/3, the source signed-edge Gram factor exists on the full
union edge roster. Its onsite residuals obey

    S_ii-c-sum_(j!=i)|S_ij| >= m gamma-c > 0.

Columns for edges absent from a particular arm are simply zero. Hence
BB*=S-cI exactly throughout this disclosed family. This does not select
the factorization from the axioms or supply a periodic physical source map.

## Uniform coercivity of the joint likelihood precision

The joint target covariance is

    C0=[[W,D],[D*,I]],   W=Re(q^-1),   D=q^-1 B.

It satisfies W-DD*=c q^-1 q^-*>0 and ||W||<=1/(m gamma). Therefore

    (x,y)*C0(x,y)
       <= (sqrt(||W||)||x||+||y||)^2
       <= (1+1/(m gamma)) (||x||^2+||y||^2).

This proves the dimension-independent lower bound

    Q0 >= [m gamma/(1+m gamma)] I.

At m=1 the bound is 243/659, much stronger than the finite trace bound used
in the first likelihood probe. It applies to both c choices and every arm
in the stated Hodge range. It degenerates as m->0, and is not a massless
phase estimate. The direct full-matrix checks use varied cover, width, shear
sign and mass, and independently compare C0 with the action precision.

## Determinant comparisons should cancel common bulk factors

For positive Q_j>=m0 I, define the finite-alpha logarithmic tilt

    g_j(alpha)=log det(Q_j+alpha I)-log det Q_j.

The derivative formula and resolvent identity give

    g_j(alpha)-g_k(alpha)
      = integral_0^alpha Tr[(Q_j+tI)^-1-(Q_k+tI)^-1] dt.

If Delta=Q_j-Q_k has rank at most r and norm at most delta, then

    |g_j-g_k| <= r delta alpha/[m0(m0+alpha)].

Indeed the inverse difference has rank at most r and norm at most
delta/(m0+t)^2; integrate its trace bound. This is uniform in dimension
when the perturbation rank, size and m0 bounds are uniform. The input
localized-perturbation hypotheses must be checked for a chosen source family;
the current finite runner does not certify them for arbitrary DK covers.

For exact finite arm tilts t_j=exp(-g_j) in [a,b], normalized reweighting
of any prior menu w has the sharp universal bound

    TV(w_j t_j/E_w t,w_j) <= (sqrt(b)-sqrt(a))/(sqrt(b)+sqrt(a))
                         = tanh(log(b/a)/4).

To prove it, put mu=E_w t. Convexity bounds E|t-mu| by the chord joining
its values at a,b. Dividing by 2mu gives
(b-mu)(mu-a)/(mu(b-a)), whose maximum occurs at mu=sqrt(ab).
This proves the bound for every menu, without knowing the detailed prior.
It is attained by a two-point endpoint distribution with that mean.

Combining with the preceding local resolvent bound gives

    TV <= tanh(r delta alpha/[4m0(m0+alpha)])

when all pairwise perturbations meet the stated r,delta bounds. This avoids
bounding each extensive determinant separately. It is a conditional stability
estimate, not a determinant-selection principle.

The finite likelihood runner uses its exact rational determinant ratios to
calculate a,b and this tighter bound for the actual four-arm menus. It does
not infer a volume-uniform numerical bound from those finite ratios.
