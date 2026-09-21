# Independent empty-start time expansion

2026-09-20. Independently derived and checked before access to new author
calculations. This is a bounded mathematical check, not an audit or landing
review. All expansions concern the actual finite process at fixed physical
time and fixed rates, starting at the completely empty configuration.

**Result.** Motion can first affect the full law at order t^4 and the expected
population at order t^5. Both orders occur on a three-site path. The leading
population correction is nonnegative. More strongly, if these first possible
coefficients vanish, the first *actual* nonzero population correction is still
positive: its coefficient is another Dirichlet energy at the first occupancy
level with a motion-dependent birth hazard. There may be no motion effect at
any time from this particular initial condition.

## Definitions and the first coefficients

Let n be the number of vertices. Write w(s) for the product of W over occupied
bonds, u_(x,a)(s) for the local insertion product, and

\[
b(s)=\sum_{x\text{ vacant}}\sum_{a=1}^6u_{x,a}(s).
\]

The unscaled birth generator is B, the unscaled vacancy-hop generator is H,
and L=kappa H+epsilon B. Edge proposals in H are fixed and symmetric; the
positive heat-bath rates give detailed balance for w on every motion class.
No assumption that content counts identify those classes is needed.

Let delta_0 denote the empty-state row. Then

\[
p_\kappa(t)=\delta_0e^{tL}
=\sum_{j\ge0}\frac{t^j}{j!}\delta_0L^j.
\tag{1}
\]

In particular b_0=6n, and every one-record state has b_1=6(n-1). Write
f_j(s)=(delta_0 B^j)(s)/w(s). The first pure-birth row coefficients are:

| N(s) | f_1 | f_2 | f_3 |
|---|---|---|---|
| 0 | -b_0 | b_0^2 | -b_0^3 |
| 1 | 1 | -(b_0+b_1) | b_0^2+b_0 b_1+b_1^2 |
| 2 | 0 | 2 | -2[b_0+b_1+b(s)] |
| 3 | 0 | 0 | 6 |
| >=4 | 0 | 0 | 0 |

The factor w(s) is essential. Each ordered insertion history telescopes to
its child's product weight, giving j!w(s) on level j. Diagonal holding-rate
terms give the other entries. The corresponding coefficients of the *actual*
process through order three are exactly epsilon^j w(s)f_j(s)/j!:

\[
\delta_0H=\delta_0BH=\delta_0B^2H=0.
\tag{2}
\]

For example, the single-record coefficient is uniform in position and H is
reversible for that uniform law. The two-record coefficient is proportional
to w(s) within every motion class. Symmetry of the edge proposals suffices;
graph regularity and equal proposal rates are unnecessary.

The first possible motion term follows from the nonconstant hazard in f_3:

\[
\bigl(\delta_0B^3H\bigr)(s)
=-2\,1_{N(s)=2}\,w(s)(Hb)(s).
\tag{3}
\]

Consequently, with p_0(t) denoting the law with kappa=0,

\[
p_\kappa(s,t)-p_0(s,t)
=-\frac{\kappa\epsilon^3t^4}{12}
1_{N(s)=2}w(s)(Hb)(s)+O(t^5).
\tag{4}
\]

All big-O statements here hold at fixed finite graph, weights and rates.
They are not uniform in a diverging motion intensity or graph volume.

## Population: first possible term and its sign

Because HN=0 and BN=b, every motion term in E[N] through degree four
vanishes. At degree five the only surviving motion word is
delta_0 B^3 H B N. Define the *unnormalized* level-two Dirichlet energy

\[
\mathcal E_2(b)
=-\sum_{s:N(s)=2}w(s)b(s)(Hb)(s)
=\frac12\sum_{s:N(s)=2}\sum_t
w(s)H(s,t)[b(t)-b(s)]^2.
\tag{5}
\]

It is nonnegative, and zero exactly when b is constant along every allowed
two-record hop. Equations (3) and (5) give

\[
E_\kappa N(t)-E_0N(t)
=\frac{\kappa\epsilon^4}{60}\mathcal E_2(b)\,t^5+O(t^6).
\tag{6}
\]

The factor 1/60 is 2!/5!; dividing the energy by a partition function would
be incorrect for this empty-start expansion.

The motion-independent population coefficients through degree three also
have a compact graph expression. If T is the number of triangles, then

\[
E_\kappa N(t)
=6n\epsilon t-18n\epsilon^2t^2
+[36n+T(\operatorname{tr}W^3-216)]\epsilon^3t^3
+\frac{\epsilon^4t^4}{24}\delta_0B^4N
+t^5\left[\frac{\epsilon^5}{120}\delta_0B^5N
+\frac{\kappa\epsilon^4}{60}\mathcal E_2(b)\right]+O(t^6).
\tag{7}
\]

To check the triangle term, with two records b,c at y,z, the total hazard is

\[
b(s)=6(n-2)+c(y,z)[(W^2)_{bc}-6],
\tag{8}
\]

where c(y,z) counts their common neighbors. These neighbors are all vacant
in a two-record state. Summing the correction over nonadjacent pairs gives
zero by the row sums. An adjacent pair contributes tr(W^3)-216; the sum of
c(y,z) over edges is 3T. Inserting the factor two in f_2 and dividing the
third derivative by 3! proves (7). No triangle-free hypothesis is used.

## When the first possible term vanishes

There is a universal answer for the first *nonzero* correction, not only for
the t^5 coefficient. Let m be the smallest occupancy level on which Hb is
not identically zero. If it exists, then 2<=m<=n-1. Define E_m(b) by (5),
replacing level two by level m. Then

\[
p_\kappa(s,t)-p_0(s,t)
=-\frac{\kappa\epsilon^{m+1}m!}{(m+2)!}
t^{m+2}1_{N(s)=m}w(s)(Hb)(s)+O(t^{m+3}),
\tag{9}
\]
\[
E_\kappa N(t)-E_0 N(t)
=\frac{\kappa\epsilon^{m+2}m!}{(m+3)!}
\mathcal E_m(b)t^{m+3}+O(t^{m+4}).
\tag{10}
\]

Here E_m(b)>0. Thus for epsilon>0, any fixed increase of kappa gives a
strictly positive leading population difference, if motion affects this
empty-start process at all. This is an initial-time statement, not a theorem
of monotonicity for every time or of nonnegative higher Taylor coefficients.

**Proof including possible disconnected motion classes.** For an arbitrary
row p(s)=w(s)f(s), detailed balance and insertion/deletion counting imply

\[
(pH)(s)=w(s)(Hf)(s),\qquad
\frac{(pB)(s)}{w(s)}=(\mathcal D f)(s)-b(s)f(s),
\quad
(\mathcal Df)(s)=\sum_{x\text{ occupied}}f(s\setminus x).
\tag{11}
\]

The deletion sum D preserves ker H. Indeed, for one allowed hop, pair the
deleted sites before and after the hop. Deleting the moving record gives
the same parent configuration. Deleting another record gives two parent
configurations related by the same allowed hop. If f is constant on every
parent motion class, all paired values agree. Positivity of W keeps that
parent hop available. A finite generator's kernel consists precisely of
functions constant on its motion classes; no count-sector replacement is
made here.

Inductively, f_j lies in ker H for j<=m. Its top occupied level j has value
j!. At the next step, the only part that can leave ker H is multiplication
of the level-m constant m! by -b(s). Therefore

\[
Hf_{m+1}=-m!\,1_{N=m}Hb.
\tag{12}
\]

This proves the first surviving motion word and (9). To evaluate N, a final
H kills N, so one additional B is required. Detailed balance then gives
delta_0 B^(m+1) H B N=m! E_m(b), proving (10). Its strict positivity follows
from a nonconstant hazard across an edge of some motion class.

If m does not exist, multiplication by b also preserves ker H, so (11)
keeps every f_j in ker H. Every word containing H then vanishes from the
empty-start expansion. Finite-state analyticity proves that the full law is
independent of kappa for all t. This last assertion concerns the empty start;
it does not hold for arbitrary initial distributions.

## Exact witnesses and controls

**Three-site path, first possible orders attained.** Use unit edge proposals
and W=3/2 for equal, 1/2 for opposite, and 1 for orthogonal contents. For
ordered contents a,b along the path, put g=W_(ab) and Delta=(W^2)_(ab)-6.
The three possible position pairs form two motion edges, each with
conductance g/(1+g). Thus

\[
\mathcal E_2(b)=2\sum_{a,b}\frac{W_{ab}}{1+W_{ab}}
[(W^2)_{ab}-6]^2=\frac{14}{5}.
\]

The all-identical adjacent state (0,0,vacant) has coefficient -1/40 for
kappa epsilon^3 t^4; the separated state (0,vacant,0) has coefficient 1/20.
Exact full-generator multiplication gives

\[
E_\kappa N(t)=18\epsilon t-54\epsilon^2t^2+108\epsilon^3t^3
-\frac{649}{4}\epsilon^4t^4
+\left(\frac{984}{5}\epsilon^5+\frac7{150}\kappa\epsilon^4\right)t^5
+O(t^6).
\tag{13}
\]

Already at the next order the motion coefficients are -19 kappa epsilon^5/45
and -79 kappa^2 epsilon^4/6750. This demonstrates why (10) must not be stated
as positivity of every motion coefficient. It is not a counterexample to a
finite-time monotonicity theorem; no such theorem is established here.

**Delayed first effect.** In the 4x4 rook graph, vertices are pairs (i,j),
adjacent when one coordinate agrees. Every distinct pair has exactly two
common neighbors. Equation (8) therefore makes b motion-invariant on level
two for every content pair. With the same W as above, place three identical
contents at (0,0),(0,1),(0,2). Its hazard is 159/2. The allowed hop from
(0,2) to (1,2) gives hazard 81, heat-bath rate 4/13, and one undirected
Dirichlet contribution 243/104. Thus m=3: the actual first orders are t^5
for the distribution and t^6 for population. The code checks all 4,320
two-record configurations and this three-record construction; it does not
claim a full 7^16-state enumeration or compute the complete level-three
energy.

**No-effect controls.** For W=1, b=6(n-N), so m does not exist on any graph.
On a complete graph, general W gives
b=(n-N)sum_a product_b W_(ab)^(C_b), which is fixed by motion as well.
The full-state checks include the triangle with unequal proposal rates and
the uniform-weight path. They find no motion coefficients through order six;
the all-time assertions follow from (11), not from the finite cutoff.

## Reproduction, limitations, and source identities

`python3 check.py > RUN.log` uses only the Python standard library and exact
rational arithmetic. It builds both actual generators from every state,
checks insertion weight ratios and motion detailed balance, and multiplies
the noncommuting generator polynomial through degree six. The four cases
enumerate 343, 343, 343 and 2,401 states; the fourth uses a general positive
row-six W and unequal proposals on a four-site path. All polynomial,
Dirichlet, factorial, triangle, individual-state and control checks pass.
`RESULTS.json` records every population polynomial. `SEAL.json` pins this
report, code, outputs and the pre-source-access boundary.

For epsilon=0, or when there are no effective hops, the empty-start process
has no motion dependence. The empty graph is trivial. For n<=2 the first
varying-hazard level cannot occur. No connectivity, regularity, equilibrium
entrance, or rare-birth assumption was used. This work does not control a
finite observation interval, an epsilon-to-zero limit at fixed event index,
an intensity diverging with t, or a growing-volume limit.

Only the already-known supplied model at commit
`689941783bea870e08458e079ddb208257d0083d` was used:

* `docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md`:
  SHA-256 `8cc06519d7f3acc088b1e450c151f0870ab21d2987ef2b0224d40ba6a5e7e4e2`.
* `docs/MOBILE_RECORDS_FINITE_RATE_CONTROL_AND_SPATIAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-20.md`:
  SHA-256 `423eba32f704e510331bfbb6dba78ea0a35db129854547b155fd76f27248d917`.

The unchanged methodology instructions were reused. No new campaign author
source or result message was consulted, no external result was imported,
and no path outside this assigned independent directory was modified.
