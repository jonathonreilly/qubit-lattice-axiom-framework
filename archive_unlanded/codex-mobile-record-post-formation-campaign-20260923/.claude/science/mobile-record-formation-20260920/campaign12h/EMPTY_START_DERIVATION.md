# Primary working derivation: empty-start correlations and delayed motion response

2026-09-21. Conditional mathematics for the specified finite stochastic model.
No force, field, continuum law or rate is identified with physical reality.
This argument was derived personally before the new independent check.

Let H be the unscaled reversible vacancy-hop generator, B the unscaled birth
generator, and L=kappa H+epsilon B, acting on column observables. Row laws act
on the left. The graph is finite and simple, W is positive and symmetric with
every row sum six, and a vacancy has bond weight one. Let w(s) be the product
of occupied-edge weights, N(s) the number of records, b(s)=B N(s) the total
unscaled birth hazard, and delta_0 the initially empty law. The motion proposal
rates can vary across edges provided forward/reverse proposals are symmetric.

## First two birth powers are invariant under motion

The only nonzero components of delta_0 B are its empty-state diagonal -6V
and coefficient one on each one-record configuration. They are stationary for
H, because a single record has w=1 and symmetric hops. Thus delta_0 B H=0.

Row normalization gives b(s)=6(V-1) on every one-record configuration: each
neighboring vacancy sums its single-neighbor weight to six, and each other
vacancy also has hazard six. Therefore delta_0 B^2 has components

```
N=0: 36 V^2,
N=1: -6(2V-1),
N=2: 2 w(s),
N>2: 0.
```

For N=2 the two insertion orders have the same product w(s). On every motion
communication class H is reversible for w. Each displayed stratum is therefore
stationary for H, even if a content-count sector is disconnected. Consequently
delta_0 B^2 H=0. No irreducibility or rare-birth limit is needed.

Successively multiplying on the right now gives the exact identities

```
delta_0 L   = epsilon delta_0 B,
delta_0 L^2 = epsilon^2 delta_0 B^2,
delta_0 L^3 = epsilon^3 delta_0 B^3,
delta_0 L^4 = epsilon^4 delta_0 B^4
                +kappa epsilon^3 delta_0 B^3 H.
```

Thus the full finite distribution agrees with the zero-motion process through
third order in physical time. A motion-conserved observable f, with Hf=0,
agrees through fourth order. This applies to total population and all functions
of the immutable content multiset. It does not assert equality at finite time.

## First possible population correction has a definite sign

The N=3 component of delta_0 B^3 is 6w(s), since each of the six insertion
orders telescopes to w(s). The N=0 and N=1 components are constant within
their motion classes. The N=2 component is

```
-2 w(s) [6(2V-1)+b(s)].
```

Hence delta_0 B^3 H = -2 (w b on N=2) H. Let the unnormalized two-record
Dirichlet form be

```
D_2(b) = - sum_(s:N=2) w(s) b(s) (H b)(s)
       = (1/2) sum_(s,t:N=2) w(s) H(s,t) [b(t)-b(s)]^2 >= 0.
```

The equality uses detailed balance; the diagonal contributes zero. Expanding
one further derivative and using HN=0 gives

```
delta_0 L^5 N - epsilon^5 delta_0 B^5 N
 = kappa epsilon^4 delta_0 B^3 H B N
 = 2 kappa epsilon^4 D_2(b).
```

For each fixed finite model and fixed nonnegative kappa, epsilon, analyticity
of the finite matrix exponential proves

```
E_(kappa)[N_t] - E_(0)[N_t]
 = kappa epsilon^4 D_2(b) t^5 / 60 + O(t^6),  t -> 0.
```

If D_2(b)>0 and kappa,epsilon>0, motion increases expected population for all
sufficiently small positive times. This is the first nonzero coefficient in
that case, not a monotonicity theorem for later times. The coefficient vanishes
precisely when b is constant along all positive-rate motion edges in the
two-record strata. On W=1 it vanishes; the entire population process is already
independent of motion. The exact rational full-generator check gives D_2=14/5
on the three-site path and 224/5 on the four-cycle at raw (3,1,2), normalized
to W=(3/2,1/2,1). The same values occur for the opposite-content-favoring
(1/2,3/2,1) menu. Constant weights and complete two-/three-site graphs give
zero. All sixteen declared graph/menu cases pass the exact checks.

## Two-record reduction to graph geometry

Write c_xy for the number of common neighbors of distinct occupied sites x,y,
and h_ab=(W^2)_ab-6. Every other vacant site's content sum is six unless it is
a common neighbor. Consequently

```
b(x,a;y,b)=6(V-2)+c_xy h_ab.
```

For each undirected proposed hop edge {x,x'}, spectator site y outside that
edge, and moving/fixed contents a,b, put u=W_ab if x is adjacent to y and
u=1 otherwise; put v=W_ab if x' is adjacent to y and v=1 otherwise. There is
one corresponding undirected two-record configuration edge. With unit proposal
rates its conductance is uv/(u+v), so

```
D_2(b)=sum_({x,x'} in E) sum_(y outside {x,x'}) sum_(a,b)
         [uv/(u+v)] h_ab^2 (c_x'y-c_xy)^2.
```

For a d-dimensional periodic hypercubic graph of side L>=6 this reduces to

```
D_2(b)/V = d sum_(a,b) h_ab^2 {
                 2(8d-7) W_ab/(1+W_ab) + (8d^2-14d+7) }.
```

To count it, fix a hop edge and one endpoint. Sites with a nonzero common-
neighbor count lie at graph distance two: 2d axial sites with c=1 and
2d(d-1) diagonal sites with c=2. Their total squared count is 2d(4d-3).
Among these, sites adjacent to the opposite endpoint contribute 1+8(d-1)
=8d-7. The rest contribute 8d^2-14d+7. The two endpoint families do not
overlap for L>=6. Combine the two sides with conductances W/(1+W) and 1/2,
then multiply by d edges per site. Small periodic sizes are excluded from this
count; their D_2 remains computable by the general graph formula.

In d=3 with W=(3/2,1/2,1), h_ab=(1/2) v_a dot v_b, so sum h_ab^2=3 and
sum h_ab^2 W_ab/(1+W_ab)=7/5. Thus D_2/V=2379/5 and the leading density
increment is `(793/100) kappa epsilon^4 t^5`.

For any nonconstant symmetric row-six W the displayed cube coefficient is
strictly positive. Indeed J denotes the all-ones matrix, A=W-J has AJ=JA=0,
and h=W^2-6J=A^2. Hence sum h_ab^2=tr(A^4)>0 whenever A!=0, and every
factor multiplying h_ab^2 in the cube formula is positive. This statement
does not require ferromagnetic contents or a positive vector eigenvalue.

## A conservative remainder bound that is uniform in volume

For unit edge proposals, maximum degree z, u=max(1,max_ab W_ab), define
R_kappa=6 epsilon u^z+z kappa and K=2(z+1). Keep each local difference grouped
as `T_i f(s)=r_i(s)[f(s^i)-f(s)]`. A term is active only if its updated site
or sites intersect the observable's support; merely inspecting that support
through its rate does not make the term active. Each active term changes the
norm by at most twice its rate bound and adds at most K support sites. The
total rate bounds of terms updating support S sum to R_kappa |S| at most.
Apply this bound separately
to each term in the iterated expansion, rather than taking the union of all
possible supports. For a one-site observable f with ||f||_infinity<=1,

```
||L^k f||_infinity <= (2 R_kappa)^k product_(j=0 to k-1) (1+jK).
```

At each step an individual term's support has size at most 1+jK; summing the
norm bounds over its descendants proves the product estimate by induction.
The finite Markov semigroup contracts the supremum norm, so Taylor's integral
remainder through degree five is at most this k=6 bound times t^6/720.
Apply it to n_x in both the moving and immobile processes, then average sites.
With

```
C = [(2R_kappa)^6+(2R_0)^6] product_(j=0 to 5)(1+jK) / 720,
a = kappa epsilon^4 D_2/(60V),
```

the density difference satisfies `|rho_kappa(t)-rho_0(t)-a t^5| <= C t^6`.
The constants do not grow with V. On the above cube family with nonconstant W
and positive kappa,epsilon, a>0 is also volume independent; for 0<t<=a/(2C)
the density increase is at least a t^5/2 on every member of the family. This
bound is deliberately conservative and may certify only extremely short
times. It neither approximates the moderate-density runs nor proves a sign
for all times. It establishes that the startup effect is not caused solely
by a particular finite volume. An infinite-process construction is not needed
for this uniform finite-volume statement and is not claimed here.

## Earliest spatial correlations do not require a supplied seed population

Let chi be centered with W chi=theta chi and nu=(1/6)sum_a chi(a)^2>0;
define chi(0)=0. Starting empty, for distinct sites x,y,

```
E[chi(s_x(t)) chi(s_y(t))]
 = 6 nu theta epsilon^2 t^2 1_(x adjacent y) + O(t^3).
```

At this order there must be two births. The two temporal orders cancel the
Taylor factor 1/2. On an edge the sum of their content products is
chi^T W chi=6nu theta; away from an edge the sum factorizes to zero. Motion
does not enter through this order, as proved above. At each site,

```
E[n_x(t)] = 6 epsilon t - 18 epsilon^2 t^2 + O(t^3),
E[chi(s_x(t))^2] = nu E[n_x(t)] + O(t^3).
```

For a nonzero fixed complex spatial vector u, F_u=sum_x u_x chi(s_x), the
normalized structure factor therefore obeys

```
E[|F_u|^2] / (nu E[sum_x |u_x|^2 n_x])
 = 1 + epsilon theta t (u^* A u)/(u^*u) + O(t^2).
```

On the above cubic family with side L>=6, for Fourier mode k this is
`1 + 2 epsilon theta t sum_i cos(k_i) + O(t^2)`. The unit-vector structure
factor sums three such component identities and has the same normalized
coefficient when all three coordinate functions are eigenfunctions of W with
the same theta, in particular for the j-family with theta=2j.
Positive theta thus creates nearest-neighbor correlations from
an empty initial state without assuming equilibrium or a one-site closure.
This local startup result supplies neither an infinite correlation length nor
a sustained ordered phase. The remainder here is for a fixed finite model;
the separate degree-five population bound above is volume uniform, but this
spectrum remainder has not been quantified here.

## Open verification and next decision

The full rational generator verifies the startup identities and nonzero
witnesses. Check the added geometry reduction and uniform remainder argument,
then compare to the pre-source independent derivation.
Use the spectrum identity as an additional empty-start simulation control.
The earliest-order sign does not settle the sign at finite density or at
matched formation fraction; preserve those as distinct empirical questions.
