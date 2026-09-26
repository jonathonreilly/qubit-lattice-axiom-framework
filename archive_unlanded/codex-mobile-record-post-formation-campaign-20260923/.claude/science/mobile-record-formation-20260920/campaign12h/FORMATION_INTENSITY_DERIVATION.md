# Primary extension: retain the whole motion semigroup at small formation rate

2026-09-21. Personally derived before the new independent calculation.
Working conditional result; direct coefficient computation and a separate
pre-source check now agree (details below). Model, H, B, w, b and the empty row delta_0 are as in
`EMPTY_START_DERIVATION.md`. Physical time t and mobility kappa are now fixed;
the expansion parameter is epsilon. This is a different limit from fixed
formation time tau=6 epsilon t, fixed density, or a rare-birth event index.

## Dyson coefficient with motion treated exactly

The finite matrix exponential has the convergent Dyson expansion in epsilon,
with kth term an ordered time integral of k birth operators separated by
motion semigroups. Since delta_0 H=delta_0 B H=delta_0 B^2 H=0 and HN=0,
the coefficients of E[N] through epsilon cubed are independent of kappa.
At order four, after integrating the first two birth times, the difference
from the immobile process is

```
C_kappa(t) = integral_(0<=u<=v<=t) (u^2/2)
              delta_0 B^3 [exp(kappa (v-u) H)-I] b du dv.
```

Only the nonstationary two-record part of delta_0 B^3 contributes. It is
-2wb after removing terms constant on motion classes. Setting s=v-u gives

```
C_kappa(t) = (1/3) integral_0^t (t-s)^3
                <b,[I-exp(kappa s H)]b>_(w,N=2) ds,

E_kappa[N_t]-E_0[N_t] = epsilon^4 C_kappa(t)+O(epsilon^5).
```

The inner product is an unnormalized sum over every two-record configuration.
In particular, no partition function divides it. Reversibility makes -H
self-adjoint and nonnegative in this inner product, so C_kappa(t)>=0. For
t>0 and kappa>0 it is strictly positive exactly when the two-record hazard is
not constant along allowed hops. As a function of kappa>=0 it is increasing
and concave: each nonzero eigenmode contributes a nonnegative multiple of
1-exp(-kappa s lambda). This assertion concerns the epsilon-four coefficient,
not the full finite-epsilon population for all times.

Let P be the orthogonal projection onto ker H within the two-record strata,
V_2(b)=<b,(I-P)b>_w, and D_2(b)=<b,-H b>_w. Then

```
0 <= C_kappa(t) <= min{kappa t^5 D_2(b)/60, t^4 V_2(b)/12},
lim_(kappa->infinity) C_kappa(t) = t^4 V_2(b)/12.
```

The first upper bound uses 1-exp(-x)<=x. The second uses the projection away
from zero modes. They do not require one connected content-count sector.

Define psi(z)=integral_0^1 (1-x)^3[1-exp(-zx)] dx. Its stable definition is
the integral, with psi(0)=0. For z>0 an algebraic form is

```
psi(z)=1/4-1/z+3/z^2-6/z^3+6(1-exp(-z))/z^4,
psi(z)=z/20-z^2/120+O(z^3) near zero.
```

If -H has eigenvalues lambda_j and b has squared weighted projections a_j,
then C_kappa(t)=t^4 sum_j a_j psi(kappa t lambda_j)/3. Expanding in kappa t
recovers kappa D_2 t^5/60 from the separate short-time derivation.

For completeness, the Dyson series gives a finite-volume remainder: if
beta=||B||_(infinity->infinity)=2 max_s b(s), stochastic contraction of every
motion semigroup bounds the absolute difference remainder by
`2 V exp(epsilon beta t) (epsilon beta t)^5/120`. This is a conservative
finite-model bound and grows with volume. It is not a uniform justification
for a finite-density or infinite-volume approximation.

## Closed three-site witness

On the three-site path at W=(3/2,1/2,1), positions of two records have weights
(g,1,g) for adjacent, separated, adjacent pairs, where g is their pair weight.
The common-neighbor indicator c is (0,1,0). Its centered part is an eigenmode
with decay lambda_g=(1+2g)/(1+g) and squared weighted norm 2g/(1+2g).
Only equal and opposite contents contribute to h_ab=(W^2)_ab-6; each has
h_ab^2=1/4 and six content assignments. Therefore

```
C_kappa(t) = (t^4/3) [ (9/8) psi(8 kappa t/5)
                            +(3/4) psi(4 kappa t/3) ].
```

The short-time coefficient is (7/150) kappa t^5. The fast-motion limit is
5t^4/32. A block-triangular coefficient evolution of the full finite generator
checks this formula without substituting it into the simulator.

## Relative-position reduction on a torus

For a simple translation-invariant nearest-neighbor torus of volume V, with
side at least three and unit symmetric proposals, let r!=0 be the displacement
of the two records. Their relative generator H_g has rate
`2 w_g(r')/[w_g(r)+w_g(r')]` for each nearest-neighbor displacement step
r->r'!=0; w_g(r)=g when r is a nearest neighbor of zero, otherwise one.
The factor two counts motion of either endpoint. Its reversible weight is
w_g. Let c(r) be the number of common neighbors of zero and r. Then

```
C_kappa(t)/V = (1/6) sum_(a,b) h_ab^2 integral_0^t (t-s)^3
                   <c,[I-exp(kappa s H_(W_ab))]c>_(w_(W_ab)) ds.
```

The factor V/2 arises from ordered endpoint representations of each physical
two-record configuration. The primary check compares this reduction with a
full unordered-pair position generator in fifteen graph/weight cases, with
maximum absolute discrepancy 2.78e-16. The separately sealed calculation
covers the fixed-time coefficient and path formula, not this added reduction.

For the j-family W_ab=1+j v_a dot v_b, h_ab=2j^2 v_a dot v_b. The coefficient
therefore contains an explicit j^4 factor, while the relative motion kernel
still depends on j. It is O(j^4) as j->0 at fixed finite graph, t and kappa.
The earliest orientation pair correlation is instead linear in the vector
eigenvalue theta=2j. This is a hierarchy between two observables in the
supplied model; it does not identify a weak physical force or fix a constant.

## First actual order when the two-record coefficient vanishes

The separate checker proposed the following useful extension. The primary
author has reconstructed the weighted-deletion and ordered-integral argument;
the result is not treated as true merely because a checker supplied it.

For a row p write f=p/w, on every configuration. Detailed balance and the
telescoping insertion weight give the weighted row identities

```
(pH)/w=Hf,   (pB)/w=Df-bf,
Df(s)=sum_(occupied x) f(s with the record at x deleted).
```

D maps ker H to ker H. Across an allowed hop, pair the deleted spectator
records; their remaining configurations are connected by the same hop.
Deleting the moving record instead leaves identical parent configurations.
Thus corresponding values of f agree. This argument works on actual motion
classes without identifying them with content-count sectors.

Let m be the first occupancy level with H_m b nonzero, if one exists.
The pure-birth row delta_0 B^j has top-level density j! relative to w, and
zero density above j. Induct using D-b and the class constancy of b below m
to obtain delta_0 B^j H=0 for j<=m. At the next step, the only term outside
ker H is -m! b on level m. The first motion-dependent population coefficient
in epsilon is therefore

```
E_kappa[N_t]-E_0[N_t]=epsilon^(m+2) G_m(kappa,t)+O(epsilon^(m+3)),
G_m=(1/(m+1)) integral_0^t (t-s)^(m+1)
                       <b,(I-exp(kappa s H_m))b>_(w,N=m) ds.
```

The m earlier ordered insertion times give u^m/m!; the m! in the row cancels
that denominator. Integrating u from 0 to t-s gives the displayed factor.
For t,kappa>0 the coefficient is strictly positive and increasing and
concave in kappa. Writing D_m and V_m for the class Dirichlet energy and
centered variance gives

```
G_m <= min{ kappa t^(m+3) D_m/[(m+1)(m+2)(m+3)],
            t^(m+2) V_m/[(m+1)(m+2)] }.
```

Its short-time coefficient is kappa m! D_m/(m+3)!, consistent with the
separate time expansion. If there is no such level, induction keeps every
pure-birth row in ker H and the full finite empty-start law is independent
of kappa at every time. On the 4x4 rook graph m=3 for the neutral j=1/2
menu; the separately checked witness is recorded in the original independent
empty-start report. This extension has a proof and a delayed-level witness;
the fifteen new block-coefficient cases themselves all have three sites.

## Checks and open extensions

`formation_intensity_check.py` compares twelve full-generator coefficient
evolutions with two-record semigroup quadrature and the path formula; maximum
absolute discrepancy is 3.27e-11. Its fifteen relative-coordinate comparisons
have maximum discrepancy 2.78e-16. Exact rational generator construction is
followed by floating matrix exponential and quadrature, not exact real-number
certification. All outputs and declared tolerances are in the results file.

The independent check was sealed on 2026-09-21 at 00:40:59 UTC under
`independent_empty_start/formation_intensity/`. It separately derived the
coefficient before reading this note and checked fifteen full-generator
cases, including unequal edge proposals and a non-axis-symmetric W.
Its largest discrepancy is 5.57e-11 at declared tolerance 2e-8; the elementary
path formula also agrees with a 70-digit integral calculation. Its report
SHA-256 is `1ed67a3f52776551660f78fc8df2358c0e4dfba9a825ecb0fb4bf08fa6bb9a6e`.
The primary author subsequently read its full report and source. This is
separate-context mathematical scrutiny, not an audit or final-source review.

The current claim does not settle a finite-epsilon all-time monotonicity law.
That question requires its own proof or counterexample. A volume-uniform
small-epsilon remainder at fixed physical time would require a local influence
bound; the current norm estimate does not supply one.
