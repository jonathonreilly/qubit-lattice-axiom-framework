# Two-layer source-polymer control for constrained Wilson--staggered gauge fibers

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_constrained_fiber_two_layer_kp_source_polymer_2026_07_12.py`](../scripts/wilson_staggered_constrained_fiber_two_layer_kp_source_polymer_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_constrained_fiber_two_layer_kp_source_polymer_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_constrained_fiber_two_layer_kp_source_polymer_2026_07_12.txt)

## 0. Result

The positive fermion-integrated gauge-body fiber now has an explicit
all-order complex-source region and a connected coarse gauge-body polymer
action.

Use the same real constrained fiber and hidden-coordinate graph as the direct
dependency,
[raw constrained-action response and exponentially local Hessian](WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_BOUNDED_THEOREM_NOTE_2026-07-12.md).
For positive parameters `c,theta,lambda`, set

```text
kappa=14/(m^2+2),
L=theta+2c+lambda,
q=kappa exp(2L).                                                       (0.1)
```

Define `g(t)=(exp(t)-1)/t`, continuously extended by `g(0)=1`, and

```text
K_(theta,lambda)(c)
 =12[exp(3 beta/4)-1] exp(4L)
  +(3/2)sum_(n>=2) kappa^n
       g(3 kappa^n/(2n)) exp(2nL).                                   (0.2)
```

Whenever

```text
q<1,                         K_(theta,lambda)(c)<c,                   (0.3)
```

the following hold uniformly in the finite regulator, hidden boundary, and
complete coarse configuration `V`:

1. the hidden partition function has an absolutely convergent two-layer
   connected-polymer logarithm;
2. bounded local complex gauge-body sources have a common zero-free domain,
   hence a uniform complex-source domain,
   controlled by the strict margin `epsilon=c-K_(theta,lambda)(c)`;
3. every finite-order local connected cumulant is the derivative of that
   common logarithm and obeys a factorial marked-cluster bound with
   exponential connected-span decay;
4. after hidden integration, the exact coarse gauge-body logarithm belongs to
   the `p=0` sector of the generated coarse action space with positive size and
   diameter weights.

Three explicit points with `theta=lambda=0.001` are

| `m` | `beta` | `c` | `K` | `epsilon` | `q` |
|---:|---:|---:|---:|---:|---:|
| 10 | 0.0005 | 0.12 | 0.1080982377 | 0.0119017623 | 0.2227031671 |
| 12 | 0.0020 | 0.15 | 0.1164294085 | 0.0335705915 | 0.1754240151 |
| 16 | 0.0035 | 0.14 | 0.1125456219 | 0.0274543781 | 0.0953784845 |

This is a deliberately deep high-mass/small-coupling subwedge. It is not the
whole `alpha(beta,m)<1/2` Dobrushin region.

The theorem is gauge body only. It does not yet place the retained
gauge--Grassmann logarithm in the simultaneous all-degree norm, define a
projected/rescaled RG contraction, select a physical taste carrier, or produce
a critical continuum trajectory.

No negative theorem is shipped. No axiom-update stop is established.

## 1. Exact interaction-factor expansion

For fixed `V`, write the real hidden gauge-body energy, after extracting only
`V`-independent scalar constants, as

```text
H_V(H)=sum_(a in I) psi_a^V(H_(S_a)).                                (1.1)
```

The label set contains fine Wilson plaquettes and the reverse-paired closed
paths in the exact massive determinant logarithm. Each `S_a` is the declared
**syntactic hidden footprint** of the label: every fine-link occurrence charges
the hidden coordinate from whose one- or two-link block-map footprint that
link is obtained. This support is deliberately not minimized after the
substitution `U_1=A,U_2=A^(-1)V`. Thus an algebraic cancellation such as
`A A^(-1)V=V` retains the `A` coordinate in `S_a`, even when the resulting
factor is independent of `A`. Every nonconstant label consequently has a
nonempty declared support, and any coarse link `V` exposed by cancellation is
still charged to its skeleton coordinate and both coarse endpoints. With
product hidden Haar measure,

```text
exp(-H_V)=product_a [1+f_a],
f_a=exp(-psi_a^V)-1,              b_a=||f_a||_infinity.              (1.2)
```

Over-supporting a factor does not change the integral or the exact component
factorization: dummy Haar coordinates integrate to one. It can only add
overlaps to the polymer majorant. The incidence estimates below already count
fine-link occurrences, so they apply to this syntactic footprint without
change. Every bound is independent of `V`: substituting a skeleton pair
`U_1=A,U_2=A^(-1)V` preserves unitarity and Haar measure.

### 1.1 Wilson factors

The exact `SU(3)` range is

```text
-3/2<=Re Tr U<=3.                                                     (1.3)
```

For `psi_p=-(beta/3)Re Tr U_p`, subtracting the midpoint `-beta/4`
leaves

```text
||psi_p+beta/4||_infinity<=3 beta/4,
b_p<=exp(3 beta/4)-1.                                                 (1.4)
```

The subtraction is an extractable vacuum constant. A hidden coordinate has a
one- or two-link fine footprint; each fine link meets six four-dimensional
plaquettes. Thus at most twelve plaquette labels meet one hidden coordinate.
Each has `|S_p|<=4` and connected-tree span `ell(S_p)<=4`.

### 1.2 Determinant path factors

The nonbacktracking two-hop expansion has absolute row radius

```text
kappa=14/(m^2+2).                                                     (1.5)
```

At determinant order `n>=2`, the sum of potential norms incident on one fine
link is at most `3 kappa^n/4`. Aggregating the at-most-two-link hidden
footprint gives

```text
sup_h sum_(a: order n,h in S_a)||psi_a||_infinity
 <=(3/2)kappa^n.                                                      (1.6)
```

An individual reverse-paired term is bounded by

```text
t_n=3 kappa^n/(2n).                                                   (1.7)
```

Therefore `exp(x)-1<=x g(t_n)` for `0<=x<=t_n` gives

```text
sup_h sum_(a: order n,h in S_a)b_a
 <=(3/2)kappa^n g(t_n).                                              (1.8)
```

The path traverses `2n` fine-link occurrences, so
`|S_a|<=2n` and `ell(S_a)<=2n`. The absolute word entropy is already included
in `kappa`; no second lattice-animal factor is inserted.

## 2. The two-layer cluster lemma

Expanding (1.2) does not immediately give a hard-core gas of the original
factors because overlapping factors can occur together. First group every
finite factor set into connected components under hidden-support overlap.
For a connected label set `Gamma`, put

```text
Y_Gamma=union_(a in Gamma) S_a,
w_Gamma(V)=integral product_(a in Gamma) f_a dH_(Y_Gamma).            (2.1)
```

Disjoint components factor exactly under product Haar, and

```text
|w_Gamma(V)|<=product_(a in Gamma)b_a.                               (2.2)
```

The original partition function is therefore exactly a hard-core polymer gas
of the connected `Gamma`, with incompatibility defined by overlap of
`Y_Gamma`.

Here is the model-independent sufficient condition used below:

```text
sup_h sum_(a:h in S_a)
 b_a exp[(theta+2c)|S_a|+lambda ell(S_a)] < c.                       (2.3)
```

The first layer is a rooted-tree domination of connected factor collections.
Give a factor the weight

```text
u_a=b_a exp[(theta+c)|S_a|+lambda ell(S_a)].                         (2.4)
```

For a root `a`, the sum of possible child weights with their remaining
rooted-tree allowance is at most

```text
sum_(b:S_b intersects S_a)
 b_b exp[(theta+2c)|S_b|+lambda ell(S_b)]
 <=c|S_a|.                                                           (2.5)
```

For completeness, this implication can be obtained without a separate animal
count. In a finite truncation let `T_a^(0)=u_a` and recursively majorize rooted
labelled trees by

```text
T_a^(r+1)
 =u_a exp[sum_(b:S_b intersects S_a) T_b^(r)].                      (2.6)
```

Induction using (2.5) gives

```text
T_a^(r)<=u_a exp[c|S_a|]
 =b_a exp[(theta+2c)|S_a|+lambda ell(S_a)].                         (2.7)
```

Every finite overlap-connected factor set containing `a` has a spanning tree
rooted at `a`, so its product weight occurs at least once in this nonnegative
tree majorant. Moreover, for an overlap-connected collection,

```text
|union_a S_a|<=sum_a |S_a|,
ell(union_a S_a)<=sum_a ell(S_a).                                  (2.8)
```

The second inequality follows by joining the support trees along the overlap
tree. Rooting a collection that meets `h` at any one of its labels containing
`h`, applying (2.7), and then (2.3) yields

```text
sum_(Gamma:h in Y_Gamma)
 |w_Gamma| exp[(theta+c)|Y_Gamma|+lambda ell(Y_Gamma)] <=c.         (2.9)
```

The bounds are uniform in the finite truncation, so monotone convergence of
the nonnegative majorant removes it. The second layer uses the remaining
`c|Y|` as the exclusion function in the Kotecky--Preiss condition:

```text
sum_(Gamma' incompatible Gamma)
 |w_(Gamma')| exp[theta|Y_(Gamma')|+lambda ell(Y_(Gamma'))]
               exp[c|Y_(Gamma')|]
 <=c|Y_Gamma|.                                                      (2.10)
```

Thus the hard-core polymer logarithm is absolutely convergent. The two copies
of `c` in (2.3) are load-bearing: one pays for connected-factor grouping and
one pays for the final polymer exclusion sum.

The external abstract convergence theorem is R. Kotecky and D. Preiss,
*Cluster expansion for abstract polymer models*, Communications in
Mathematical Physics **103** (1986), 491--498, DOI
`10.1007/BF01211762`. Equations (1.3)--(2.10), rather than that citation alone,
verify its hypotheses for this continuous `SU(3)` fiber.

## 3. Explicit model criterion and examples

Substituting (1.4) and (1.8) into (2.3) gives exactly (0.2). Absolute
convergence of its determinant series follows from `q=kappa exp(2L)<1`.
A convenient closed upper envelope is

```text
K_F
 <=(3/2)exp(3 kappa^2/4) q^2/(1-q).                                 (3.1)
```

The runner evaluates the actual series, not only (3.1), at the three displayed
points. Their positive `theta,lambda` prove a genuine size- and distance-
weighted domain rather than bare free-energy convergence.

These constants are intentionally conservative. Reverse-pair trace centering,
closed-loop cancellations, sharper incidence enumeration, or a
Fernandez--Procacci criterion can enlarge the region; none is used.

## 4. Uniform complex sources and all-order cumulants

For bounded local real gauge-body observables `O_i` with hidden supports
`T_i`, sizes `s_i`, spans `d_i`, and sup norms `M_i`, add complex sources
`z_i O_i`. They enter (2.3) as marked factor activities. The same expansion is
valid whenever

```text
S(z)=sup_h sum_(i:h in T_i)
 [exp(|z_i|M_i)-1]
 exp[(theta+2c)s_i+lambda d_i] < epsilon,                            (4.1)

epsilon=c-K_(theta,lambda)(c)>0.                                    (4.2)
```

For one source this gives the explicit uniform radius

```text
r_O=M^(-1)log[1+epsilon exp(-(theta+2c)s-lambda d)].                 (4.3)
```

At the three points of Section 0, the norm-one radii for `(s,d)=(1,0)` are
respectively `0.00930943`, `0.02454123`, and `0.02051691`; for `(4,2)` they
are `0.00451961`, `0.01000061`, and `0.00886481`.

Kotecky--Preiss convergence is uniform throughout the complete Reinhardt
domain (4.1), so the partition function is zero-free there and its connected
logarithm uses one common branch. Differentiation at the origin gives

```text
D^n R=(-1)^(n+1) kappa_n.                                           (4.4)
```

The marked connected-cluster series is absolutely convergent. For every
fixed `n` it supplies a volume-, boundary-, and `V`-uniform factorial bound;
because every cluster carrying all marks has connected hidden union, the
`lambda` weight also gives

```text
|kappa_n(O_1,...,O_n)|
 <=n! C_n product_i M_i
       exp[-lambda tau(T_1,...,T_n)],                                (4.5)
```

where `tau` is the minimum hidden connected-tree span joining the marked
supports and `C_n=C_n(c,theta,lambda;{s_i,d_i})<infinity` is the pinned
marked-cluster majorant at any fixed strict sub-polydisc of (4.1). The theorem
claims uniform finiteness and tree decay, not an optimized closed form for
`C_n`.

Equation (4.5) is an all-order extension of the prior real Hessian theorem in
this stricter KP region. It is not obtained by renaming pair covariance decay
as complete analyticity. The classic Dobrushin--Shlosman formulation is
finite-spin and finite-range; it is method context, not an imported theorem
for the present compact continuous, exponentially decaying fibers.

## 5. Coarse gauge-body polymer norm

Assign each positive fine-link hidden coordinate to the coarse cell containing
its starting site. The two links of a skeleton coordinate have the same coarse
anchor. Consecutive fine-path links map to equal or nearest-neighbor coarse
cells. For a connected hidden polymer `Y`, let `X(Y)` contain every anchor and,
for each skeleton coordinate in the declared syntactic footprints, both
endpoints of its coarse link. This deliberately over-supports any factor that
became hidden-independent after an `A A^(-1)` cancellation and therefore keeps
every resulting `V` dependence inside `X(Y)`. Then

```text
X(Y) is connected,
|X(Y)|<=2|Y|,
diam X(Y)<=ell(Y)+1.                                                  (5.1)
```

There are at most `4*2^4=64` positive fine-link anchors in one factor-two
coarse cell and at most four incoming skeleton endpoints. Hence at most 68
hidden coordinates can charge one coarse anchor in the conversion.

Group all hidden clusters with the same coarse support and use triangle
inequality. The pinned two-layer bound then gives the `p=0` coarse interaction

```text
sup_z sum_(connected X contains z)
 exp[(lambda/2)diam X+(theta/2)|X|] ||Phi_X^g||_infinity
 <=68 exp(lambda/2)c.                                                (5.2)
```

Haar integration and the gauge-invariant plaquette/closed-loop factors make
each coefficient coarse-gauge invariant. Thus (5.2) is genuine membership of
the exact gauge body in the gauge-only sector of the generated action space,
not merely quasilocality of the image measure.

## 6. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_constrained_fiber_two_layer_kp_source_polymer_2026_07_12.py
```

The runner checks Wilson centering, hidden plaquette incidence, all three
strict KP points, the determinant geometric envelope, source radii, an exact
finite factor-to-polymer regrouping identity including a factor with an
over-assigned dummy hidden coordinate, the coarse-anchor Lipschitz map, the
68-coordinate multiplicity, and the source/dependency contract.
The rooted-tree and marked KP bounds are analytic statements.

## 7. Honest boundary and next theorem

This theorem closes the complex-source and all-order connected-polymer problem
for the positive gauge body in the explicit region (0.3). It does not close
the retained gauge--Grassmann action.

The next theorem must couple one simultaneous Banach-algebra-valued source to
the exponentially local Schur coefficients, preserve balanced degree and
joint gauge covariance, and prove that the sums over endpoints, paths,
supports, and all Grassmann degrees fit the `eta`-weighted norm. Individual
coefficient source disks are not enough.

Only after that lift is it meaningful to define symmetry-adapted relevant
coordinates and test a projected/rescaled irrelevant-map contraction. A
failure of this particular KP inequality would be a limitation of the
expansion, not evidence that the axioms require amendment.

## 8. No-Go Discipline N1--N8

No negative theorem or route foreclosure is shipped. The boundary sentences
are scope disclaimers. The eight checks are retained conservatively and N1
records proof routes actually executed for the positive theorem.

### N1 — alternative-route enumeration

| Route | Status | Executed test | Role |
|---|---|---|---|
| Interaction-factor decomposition | `ATTEMPTED` | Section 1 constructs Wilson and determinant factors. | Exact starting identity. |
| Wilson midpoint centering | `ATTEMPTED` | Equation (1.4) and the runner verify `3 beta/4`. | Reduces the gauge activity without cancellation. |
| Determinant loop incidence | `ATTEMPTED` | Equations (1.6)--(1.8) sum every path word. | Includes word entropy and footprint factor two. |
| Two-layer connected regrouping | `ATTEMPTED` | Section 2 and a finite exact runner model verify factor-to-polymer equality. | Prevents treating overlapping factors as compatible. |
| Rooted-tree majorant | `ATTEMPTED` | Equations (2.3)--(2.5) spend the first `c`. | Controls connected-factor entropy. |
| Hard-core KP exclusion | `ATTEMPTED` | Equation (2.10) spends the second `c`. | Produces the zero-free log. |
| Marked complex sources | `ATTEMPTED` | Section 4 derives and evaluates positive radii. | Supplies all-order cumulants. |
| Hidden-to-coarse geometry | `ATTEMPTED` | Section 5 and the runner verify the anchor map and multiplicity. | Places the gauge body in the coarse norm. |

### N2 — wall-independence audit

The collapsed open conditions are `joint Grassmann projected/rescaled
contraction theorem` and `physical critical trajectory/observable
identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| joint Grassmann projected/rescaled contraction theorem | physical critical trajectory/observable identification | No | No | Yes |

The simultaneous Grassmann norm is included in the first condition because a
contraction theorem on that joint space presupposes that the map is defined
there.

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Hidden boundary and fixed coarse configurations are mathematical variables. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical` | No unqualified use. |

### N4 — citation/residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Raw constrained-action Hessian](WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Real second-order response only | Uniform complex/all-order gauge-body response | Yes | Sole direct repository dependency. |
| Kotecky--Preiss 1986 | Abstract polymer convergence after an activity inequality | Verify the two-layer model-specific inequality | Yes | External mathematical theorem. |
| Dobrushin--Shlosman 1987 | Complete analyticity in its declared framework | Continuous infinite-range constrained fiber | No | Context only; not imported. |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Every finite hidden regulator and boundary at the three points | Yes | Uniform zero-free source domain. |
| Arbitrary finite local gauge-body source family satisfying (4.1) | Yes | Common connected logarithm and all-order cumulants. |
| Infinite-volume fixed local gauge-body cumulants | Yes | Uniform limits of pinned clusters. |
| Coarse gauge-body interaction | Yes | Weighted `p=0` polymer membership. |
| Retained Grassmann coefficients, one at a time | No | Not claimed. |
| Simultaneous all-degree gauge--Grassmann norm | No | Next theorem. |
| Projected/rescaled joint RG map | No | No contraction claim. |
| Physical critical trajectory | No | No existence or impossibility claim. |

### N6 — partial-closure and primitive scan

The parameters `c,theta,lambda` and source radii are mathematical convergence
coordinates, not new physical premises. The Wilson--staggered regulator and
factor-two block map were already declared. No action, probability, time,
source, or RG axiom is added. The approved scale-reference,
kinetic-isotropy, and realized-state primitives neither supply nor obstruct
this cluster estimate.

The remaining Grassmann and contraction steps are ordinary mathematical
construction routes. No convention-only reframe or pending primitive proposal
is being mislabeled as a physics wall.

### N7 — hostile steelman

A hostile reviewer should insist that the present wedge is grossly
conservative: midpoint-centering the reverse-paired determinant traces gives
another `3/4` improvement, and Fernandez--Procacci criteria improve the
abstract polymer bound. Correct. Those routes can enlarge the region, so the
paper makes no optimality or outside-wedge claim. They do not invalidate the
positive strict points proved here.

A second hostile reviewer should reject any statement that the scalar marked
expansion automatically proves the retained Grassmann theorem. Correct. A
Banach-algebra activity bound with simultaneous degree counting is still
required and is the next target.

### N8 — cross-cycle echo

| Earlier surface | Earlier residual | Retired? | Mechanism applies here? | Present treatment |
|---|---|---:|---:|---|
| Constrained-fiber Dobrushin control | Pair comparison only | Yes, for real pair response | Partly | KP supplies the missing complex/all-order step only in a deeper region. |
| Raw-action Hessian | Second derivative only | Yes, in (0.3) | Yes | Marked clusters extend it to all fixed orders. |
| Coarse-gauge Gibbsianness | Sitewise summable, noncanonical potential | Yes, for gauge-body existence | Yes | The explicit expansion now supplies a weighted connected representative. |
| Generated-action space | Finite-volume joint algebra only | No | Partly | Only its `p=0` gauge sector is closed here. |

No prior partial closure is inflated into the simultaneous Grassmann or
continuum theorem, and no axiom update is requested.
