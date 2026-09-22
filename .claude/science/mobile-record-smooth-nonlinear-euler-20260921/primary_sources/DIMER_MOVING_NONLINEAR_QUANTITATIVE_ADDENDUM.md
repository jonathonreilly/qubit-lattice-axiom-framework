# Quantitative entropy and empirical bounds for moving nonlinear color waves

**Status:** proposed corollary; independent reconstruction pending.
**Date:** 2026-09-21.

Use exactly the hypotheses and process of
DIMER_MOVING_GEOMETRY_SMOOTH_NONLINEAR_EULER.md. This adds a sufficient
convergence bound; it does not change the law, preparation or continuum
solution. Constants below depend on the fixed positive C3 profile, time
interval, rates and test, but not on N, the initial geometry law or block
size. No useful finite-size accuracy threshold or optimal exponent is
asserted.

## 1. The previously checked cube gap applies to the owner blocks

Section2 of DIMER_ROUTED_QUANTITATIVE_EULER_BOUND.md proves a comparison
for a cube of side L and the owners of all its sites. The proof there
uses an odd centered cube for that application, but its combinatorial
argument only requires an embedded rectangular cube. For the even-sided
translated cubes here, choose one inside representative of each pair.
Distinct pairs have distinct representatives, m>=L^3/2.

Coordinate-ordered physical paths have length at most3(L-1), and an edge
at cut a is used by at most2a(L-a)L^2<=L^4/2 ordered paths. Contract matching
edges and erase loops. An edge between two pairs has at most two physical
representatives. The endpoint transposition word has at most6L steps,
using each routed edge at most twice. Thus, in the same unit-rate
Dirichlet convention,

    D_all <=12L^5 D_simple,
    Var(f) <=(2/m)D_all <=48L^2 D_simple.           (1)

The complete-transposition inequality is proved by the elementary
permutation conditioning argument in Section2 of
DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md and holds in every multiset
count sector. The current owner-cube form D_C retains all internal
physical-edge multiplicities, so D_simple<=D_C. Consequently the minimum
gap used in the moving nonlinear proof may be taken as

    g_L >=1/(48L^2).                                (2)

This reuses the proved comparison with its hypotheses, not a spectral-gap
assumption or a fitted relaxation law.

## 2. Track the block dependence

In the extension's conditional-current bound, the normalized observable
is uniformly bounded: rates and displacements are fixed, and at most
O(m_z) channels occur in a block. All conditional Poincare dependence is
g_L^-1/2. Summing internal forms has multiplicity O(L^3), and total
conditional entropy dissipation is O(K/N). The integrated replacement
error per pair is therefore

    C_T sqrt(L^3/(N g_L)) <= C_T L^(5/2)/sqrt N.    (3)

The other constants in that proof have no hidden block-growth dependence.
The canonical four-draw error is O(L^-3), boundary losses and the local
tensor remainder are O(L^-1), smooth coefficient translations are O(L/N),
and the product mean shift contributes O(L^2/N^2). The fixed
alpha=1/1792 keeps the coefficient multiplying relative entropy independent
of L. Hence its Gronwall inequality gives

    sup_(t<=T) h_N(t)/K
      <= C_T[ h_N(0)/K +1/L+L^(5/2)/sqrt N
                    +L/N+L^2/N^2+1/N ],            (4)

for even L>=16 and N>10L. The smaller L^-3 term is absorbed into1/L.
Take L as an even integer within a fixed factor of N^(1/7), for all
sufficiently large N. Define

    r_N=h_N(0)/K+N^(-1/7).

Then

    sup_(t<=T) h_N(t)/K <= C_T r_N.                 (5)

For exactly product-prepared colors conditional on any geometry law,
h_N(0)=0 and this is an O(N^-1/7) entropy-density upper bound.
It concerns entropy per pair, not full microscopic total variation or
a norm of a quantum state. The initial law may instead have any specified
vanishing entropy density, whose actual size remains in r_N.

## 3. Empirical mean-square bounds

For a fixed color and smooth real test phi with |phi|<=B, write

    Z_N(t)=K^-1 sum_u phi(u/N) I_(u,a)(t)
                          -integral phi(x)p_a(t,x)dx.

The case B=0 is trivial. Under the product comparison law, let W be the
same empirical average centered at its discrete deterministic mean.
Independent bounded-variable Hoeffding gives

    P(|W|>=z)<=2 exp(-2Kz^2/B^2),
    E exp(K W^2/B^2)<=3.

The geometry marginal is immaterial because that reference color marginal
is the same product law for every M. Entropy inequality and the O(N^-1)
Riemann-sum error yield

    E_mu |Z_N(t)|^2
       <= (2B^2/K)[h_N(t)+log3]+C/N^2.

Together with (5) and K=N^3/2, this proves

    sup_(t<=T) E |Z_N(t)|^2 <= C_T r_N.             (6)

A separate time-mesh argument controls the expectation of the time supremum.
Let M_N be the empirical martingale, with M_N(0)=0. Its bracket is
O_T(1/(NK)), hence E sup_t |M_N(t)|^2<=C_T/(NK).
The remainder R_N(t)=Z_N(t)-M_N(t) is uniformly Lipschitz in time:
the empirical generator drift is bounded, and the supplied target profile
has bounded time derivative. On a mesh of spacing delta,

    E sup_t |R_N(t)|^2
       <= C_T[(r_N+1/(NK))/delta+delta^2].

This uses at most T/delta+2 fixed-time second moments, with no assumed
independence between times. For sufficiently large N with r_N<=1 choose
delta=r_N^(1/3); the small bracket term is absorbed. Thus

    E sup_(t<=T) |Z_N(t)|^2 <= C_T r_N^(2/3).       (7)

For exact profile-product preparation the sufficient rates are
O(N^-1/7) in (5),(6), and O(N^-2/21) in (7). They refer to different
quantities. Neither exponent is inferred from finite-volume simulations.
Birth-generated nonuniform preparation, shocks, the geometric Gauss
field's nonlinear dynamics and quantum completion remain outside the result.

