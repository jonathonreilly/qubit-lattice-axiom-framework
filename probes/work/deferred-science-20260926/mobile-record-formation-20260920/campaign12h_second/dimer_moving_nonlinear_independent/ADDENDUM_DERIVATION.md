# Independent quantitative addendum reconstruction

This addendum was read only after the qualitative extension's independent
pre-comparison seal was fixed. It is bound by `ADDENDUM_SOURCES.json` at
SHA-256 `0671866c54f6f1865e3c63b8b4377800c85bf27303b7f28eca8a7d425b76c1ed`.
The two specified prerequisite Section2 arguments were read at their
previously checked whole-source identities. No author moving-nonlinear or
quantitative checker/results were accessed before this reconstruction.

**Assessment:** no actionable gap found. The stated sufficient rates follow
from the displayed comparison and the already reconstructed entropy proof.
They are conservative asymptotic upper bounds, not accuracy forecasts or
simulation-based exponents.

## 1. The cube comparison does not depend on odd centering

Inside any embedded physical cube of side L, choose a distinct inside
representative of each owner pair. The number m of owners is at least
L^3/2. Coordinate-ordered physical paths stay in the cube and have length
at most 3(L-1). A given physical edge at coordinate cut a is traversed
by exactly `2 a(L-a)L^2` ordered all-site paths, at most L^4/2. This count
uses only rectangular coordinates, not a center vertex or the parity of
L. Choosing one order for each unordered owner-representative pair uses
a subset of these ordered paths.

Contract matching edges and erase loops. No new edge is introduced and
the path cannot lengthen. Between two owners there are at most two
nonmatching physical edges: one from the first pair's black endpoint to
the other's white endpoint, and one in the opposite direction. This uses
the supplied nearest-neighbor bipartite simple graph, including the stated
large-period condition. Therefore a simple contracted edge is used by at
most L^4 chosen owner paths.

For a simple path of r edges, the forward word followed by the reverse
word omitting the final edge has length 2r-1<=6L. It swaps only the two
endpoint labels and uses each path edge at most twice. Cauchy-Schwarz
along that word, followed by invariance of the uniform count-sector law
under each intermediate permutation, yields

    D_all <= (6L)(2L^4) D_simple =12L^5 D_simple.

Both forms use `(1/2)sum E(diff)^2`, so there is no extra factor of two.
The complete-transposition inequality `Var <=(2/m)D_all` applies to every
color multiset by lifting to distinct permutations. Its elementary
conditioning induction has slack `2/[m^2(m-1)]` at the induction step;
it is a nonsharp sufficient inequality, as stated in its source.

Together with m>=L^3/2 this gives

    Var <=48L^2 D_simple <=48L^2 D_C.

The last inequality retains, rather than drops, physical-edge
multiplicities in D_C. These are bare unit-rate forms. The actual rate
floor enters the global entropy dissipation separately and is not counted
twice. The same argument applies to even translated owner cubes, uniformly
over matching patterns. It proves g_L>=1/(48L^2) in precisely the convention
needed by the extension.

## 2. No remaining hidden block-growth factor

The normalized displacement-weighted current has a fixed uniform bound:
there are O(m_z) channels, their rates/displacements are bounded, and it
is normalized by m_z. The centered version changes this bound only by a
constant factor. The corresponding plaquette sum is similarly bounded.
Conditional Cauchy-Schwarz over geometry introduces no factor counting
matchings, because the actual marginal rho has total mass one.

The internal-form coverage is O(L^3). Its time integral is controlled by
the O(K/N) conditional entropy dissipation. Hence the replacement error
per pair is

    C_T sqrt[L^3/(N g_L)] <= C_T L^(5/2)/sqrt(N).

All other L dependence can be counted directly: bounded-width boundary
strips and the local tensor error give O(1/L); four-draw sampling gives
O(L^-3); smooth coefficient/coverage translations give O(L/N); and the
product mean shift gives O(L^2/N^2). The overlap coloring and fixed
alpha=1/1792 keep the coefficient of h/K in Gronwall independent of L.
The fixed profile's C3 bounds and positive lower probability bound are
independent of L by hypothesis. Thus the qualitative proof's constants
have been sufficiently controlled to choose L depending on N.

Writing L of order N^a, the two dominant error exponents are -a and
(5a-1)/2. They agree at a=1/7 and equal -1/7. The other exponents are
-6/7,-12/7,-1. Taking an even L within a fixed factor of N^(1/7) meets
L>=16 and N>10L eventually. This is an asymptotic statement; the first
admissible sizes for a literal small factor can be very large, and the
source does not promise a useful finite-size threshold.

Consequently, with r_N=h_N(0)/K+N^(-1/7),

    sup_(t<=T) h_N(t)/K <= C_T r_N.

Only when the conditional initial color law is exactly the supplied
profile product does h_N(0)=0 remove the initial entropy term. A slower
vanishing initial entropy remains explicitly in the result.

## 3. Fixed-time empirical mean square

For real test weights phi_u bounded in absolute value by B, the variable
phi_u I_(u,a) has range length |phi_u|, not 2B; its two possible values
are zero and phi_u, including negative phi_u. Independence under the
comparison color marginal therefore gives, for the discrete-mean-centered
average W,

    P(|W|>=z) <=2 exp(-2K z^2/B^2).

Set Y=K W^2/B^2. Integrating `P(Y>s)<=2 exp(-2s)` yields E exp(Y)<=3.
Entropy inequality then gives `E_mu W^2<=B^2(h+log3)/K`. Adding the
deterministic O(1/N) Riemann error by the square inequality gives the
displayed factor two in the bound for Z. Since K=N^3/2 and r_N>=N^-1/7,
the O(1/K) and O(1/N^2) terms are absorbed, uniformly in t:

    sup_t E|Z_N(t)|^2 <= C_T r_N.

The nonstationary geometry marginal has no effect on this concentration
calculation because the comparison color marginal is the same spatial
product for every M. This is an entropy bound on a classical empirical
observable, not a statement about the total-variation distance of full
microscopic configurations.

## 4. Expectation of the time supremum is a different estimate

The actual empirical martingale M starts at zero and satisfies
`E sup_t |M_t|^2<=C_T/(N K)`. The remaining process R=Z-M equals its
random initial value plus an integral whose integrand is uniformly
bounded; it is pathwise Lipschitz with a fixed constant. On a mesh of
spacing delta,

    E sup_t |R_t|^2
      <= C_T[(r_N+1/(N K))/delta+delta^2].

This follows from bounding a maximum by a sum of fixed-time second
moments, and uses no independence between mesh times. With
delta=r_N^(1/3), r_N<=1 eventually, and 1/(N K)=2N^-4<=2r_N, all terms
are bounded by C_T r_N^(2/3). Adding the martingale supremum gives the
source's separate time-supremum estimate. For exact product preparation
the resulting exponent is 2/21, distinct from 1/7.

A useful outside-model control explains this loss. Let U be uniform on
the time circle and R_U(t)=(d-dist(t,U))_+ for d<1/2. These paths are
1-Lipschitz and have zero martingale part. Every fixed-time second moment
equals 2d^3/3, while the expected supremum square is d^2. Thus an O(r)
time-supremum conclusion cannot follow from fixed-time O(r) and bounded
Lipschitz drift alone. The stated O(r^(2/3)) argument is consistent with
this example; it is not a counterexample to the record-process theorem.

## 5. Independent controls and boundary

The addendum checker enumerates all ordered physical paths in even cubes
of sides2,4,6 and checks the exact cut counts. On a separate irregular
owner cube it constructs every selected endpoint path, contracts and
loop-erases it, verifies the actual endpoint-only permutation, and counts
path loads, word uses and weighted comparison congestion. The proof of
the inequality for every size remains the combinatorial argument above.

Exact algebra checks the permutation-induction slack, rate balance, all
five error exponents and the rounded-even-size feasibility on formal
N=L^7 examples. Those enormous formal N values are arithmetic only; no
production at those volumes is claimed. A six-site nonidentical product
with signed weights directly checks the exponential-square bound and an
arbitrary correlated tilt checks its entropy consequence. The triangular
bump calculation separates the two time statements.

The result remains restricted to the supplied smooth interior profile,
fixed rates, autonomous geometry and conditional entropy preparation. It
does not supply preparation by births, shocks, a nonlinear geometric-Gauss
law, quantum dynamics, or an optimal convergence exponent.
