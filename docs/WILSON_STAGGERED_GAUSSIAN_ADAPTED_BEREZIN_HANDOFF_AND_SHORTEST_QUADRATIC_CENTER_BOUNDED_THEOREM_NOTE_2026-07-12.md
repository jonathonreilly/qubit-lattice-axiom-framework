# Gaussian-adapted Berezin handoff and shortest quadratic center

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_gaussian_adapted_berezin_quadratic_center_2026_07_12.py`](../scripts/wilson_staggered_gaussian_adapted_berezin_quadratic_center_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_gaussian_adapted_berezin_quadratic_center_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_gaussian_adapted_berezin_quadratic_center_2026_07_12.txt)

## 0. Result

The fixed-gap Gaussian-reference coefficient-norm explosion has an exact
positive repair. Independently, the shortest Schur activity can be extracted
as a running quadratic center rather than treated as an irrelevant interaction;
it is the dominant Schur activity at the displayed witness.

Use the exact factor-two block and Schur identity from the
[gauge-block theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the simultaneous coefficient norm and path row from the
[retained-Grassmann polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the field-coordinate torsor from the
[declared RG chart](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the forced-base response formulas from the
[K-retaining marked-attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the current-`eta` boundary from the
[next-scale handoff theorem](WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md).

For an invertible quadratic hidden block with
`sigma_min(A_II)>=m>0`, normalized Gaussian
Berezin expectation contracts a balanced hidden `p`-pair monomial by a
`p`-by-`p` covariance minor. Since `||A_II^(-1)||_2<=m^(-1)`, every such minor
has magnitude at most `m^(-p)`. Therefore in the coefficient `l1` norm,

```text
||G_(A_II)||_(eta -> eta)
 <=max_(0<=p<=3|I|)(m eta^2)^(-p).                                 (0.1)
```

At the Gaussian-adapted value

```text
eta_m=m^(-1/2),                                                     (0.2)
```

the operator norm is exactly one for any number of eliminated sites. In
particular, the fifteen-site norm is `1`, not the `10^720` obtained in the
old `eta=10^(-10)` chart. Product hidden-Haar averaging remains contractive,
so the combined Haar--Berezin reference expectation is contractive as well.

There is also an exact finite-horizon provenance algebra. For independent
tensor-factor Haar expectations and onsite-product Gaussian pair expectations
`E_i`, put
`Q_i=1-E_i` and

```text
r_*=1+sqrt(2),
Delta_S=product_(i in S)Q_i product_(i not in S)E_i,
||F||_prov=sum_S r_*^|S| ||Delta_S F||_pi.                         (0.2a)
```

Because `r_*^2=1+2r_*`, this is a Banach-algebra norm with constant one.
Partial conditional expectations and their atom-complements have norm at most
one. With level weights `r_a=r_*R^a`, a downshift of every nonempty
cancellation tag gains at most `R^(-1)`. This finite-horizon multi-index
construction removes the algebraic one-index martingale counterexample: a
fine detail modulated by a coarse atom retains both tags. It does not yet prove
that the complete Wilson--staggered RG range has a uniformly bounded tagged
decomposition at every scale. A general coupled covariance satisfying (0.1)
is a separate contractive reference; it is not claimed to factor into these
local coordinate expectations.

The Schur paths have another exact simplification. Both retained endpoints
lie in `K=(2Z)^4`; nearest-neighbor hopping flips bipartite parity, so every
odd total path length vanishes. At total length two, the only paths are a
backtrack or two straight steps along one axis. The former is the identity and
the latter is exactly the declared coarse link `V`. Consequently the complete
length-two kernel is hidden-fiber constant:

```text
S^(2)(V)
 =(m+2/m)I
  -(1/(4m))sum_mu[V_(X,mu) shift_(+mu)
                  +V_(X-mu,mu)^dagger shift_(-mu)].                (0.3)
```

Equivalently,

```text
S^(2)=mI-m^(-1)M_KI M_IK=mI+m^(-1)M_KI M_KI^dagger>=mI.           (0.4)
```

It is a gauge-covariant, blocked-translation/proper-cubic/reflection-
compatible finite-range quadratic coordinate. Because all even Grassmann
bilinears commute, its exponential can be extracted exactly from the Schur
factor product. This is declared running-center data, not a selected physical
mass or kinetic term.

After extracting (0.3), the Schur interaction row begins at even `r=4`:

```text
K_res
 =K_W+K_I
  +18 eta_m^2 sum_(even r>=4)
     r h^(r-1)g(9 eta_m^2 2^(-r)m^(-(r-1))) exp(rL),               (0.5)
```

with `h=4/m`, `L=Theta+2c+Lambda`, and the earlier definitions of `K_W,K_I`.
At

```text
m=10000, beta=0, c=0.001, Theta=10^(-6), Lambda=1,
eta_m=0.01,                                                         (0.6)
```

For the current bare one-step factor family after exact `r=2` extraction, the
exact rows are

```text
K_(S,2)=1.068290846710377... 10^(-5),
K_(S,even>=4)=2.536105198800462... 10^(-11),
K_I=2.113419744695058... 10^(-12),
K_res=2.747447173269967... 10^(-11).                               (0.7)
```

The marked-attachment formulas applied to the residual row give

```text
A_att=2.021458733802326... 10^(-8),
q_centered=2.266318968338462... 10^(-6),
q_split=max{exp(-1/2),q_centered}=0.606530659712633...,
B_res<=3.080246724392693... 10^(-9).                               (0.8)
```

The old scalar Cauchy diagnostic is now feasible without an ultra-small
Grassmann weight: at `delta=10^(-8)` its left side is
`9.156776063580995... 10^(-9)<delta`.

This closes the fixed-gap Gaussian-reference tensor-norm explosion and
extracts the leading quadratic center. It does not prove that the exact next RG range returns to a
strong spatial provenance norm, that the running quadratic gap persists on a
ball, or that the same-norm Hessian estimate holds. Hence (0.8) is not yet an
autonomous invariant ball. No axiom-update stop is established.

## 1. Covariance-adapted Gaussian expectation and provenance atoms

Let `I` be any finite set of hidden sites with three colors per site and let

```text
Q_I=bar zeta A_II zeta,          sigma_min(A_II)>=m>0.             (1.1)
```

Normalized Berezin expectation is

```text
G_(A_II)[F]
 =(det A_II)^(-1) integral dbar zeta dzeta exp(-Q_I)F.             (1.2)
```

On an ordered balanced monomial with hidden barred indices `P` and unbarred
indices `Q`, `|P|=|Q|=p`, Wick expansion gives, up to the ordering sign,

```text
G_(A_II)[bar zeta_P zeta_Q]
 =det[(A_II^(-1))_(Q,P)].                                         (1.3)
```

Every singular value of a submatrix is at most `||A_II^(-1)||_2`; Hadamard's
inequality therefore bounds (1.3) by `m^(-p)`. The input monomial pays
`eta^(2p)` and its retained part has the same remaining weight, proving
(0.1). The constant term shows the operator norm is at least one, so it is
exactly one whenever `m eta^2>=1`.

The choice (0.2) is the smallest coefficient weight with that property and
therefore the most favorable one for the Schur activity row. Tensoring over
fifteen sites does not multiply a constant greater than one. If the quadratic
block depends on hidden Haar variables but retains the uniform gap (1.1), the
bound is pointwise in those variables; normalized Haar averaging preserves it.

With the unital embedding `L` of retained coefficients, put

```text
E_m=E_H G_(A_II),       C_m=L E_m,       Q_m=1-C_m.                (1.4)
```

Then `E_m L=1` and `E_m Q_m=0`. For one coordinate use the weighted split norm

```text
N_(m,r)(F)=||E_mF||+r||Q_mF||.                                    (1.5)
```

The bimodule property, coefficient-norm submultiplicativity, and
`||Q_m(F^oG^o)||<=2||F^o||||G^o||` give

```text
N_(m,r)(FG)<=N_(m,r)(F)N_(m,r)(G)
whenever r^2>=1+2r.                                                (1.6)
```

The smallest positive solution is `r_*`. For the atom construction, specialize
to independent product-Haar coordinates and independent onsite scalar Gaussian
pair expectations at `eta_m`; these even tensor-factor maps commute. Iterating
(1.6) over any finite family of them gives (0.2a) in the
tensor-projective coefficient norm. Coordinate integrations remove all atoms
containing their `Q_i`, while leaving the others unchanged, hence have norm at
most one. A level downshift changes `r_a` to `r_(a-1)=r_a/R`, so an atom with
nonempty tag set `S` gains `R^(-|S|)`.

For the current-chart martingale witness, `h_j` carries tag `{j}` and
`conj(h_j)g_k` carries `{j,k}`. The coarse component `a_hg_k` therefore obeys

```text
||a_hg_k||_prov
 /( ||h_j||_prov ||conj(h_j)g_k||_prov )
 <=a_h/r_j^2,                                                       (1.7)
```

independently of the modulation level `k`. The missing modulation tag was the
one-index defect. For the explicit all-nonskeleton Wilson family, every
contour coordinate is genuinely tagged. Taking `R=2`, its former per-site
weak-to-strong growth is replaced by

```text
q_loop<=[exp(Lambda/2+Theta/2+2c)/2]^|X|
       =(0.826011419447...)^|X|                                   (1.8)
```

at (0.6). General actual-range membership is stronger: a large polymer with
only one genuine cancellation tag need not satisfy (1.8). That tagged cluster
theorem remains open.

## 2. Exact shortest quadratic center

Write the exact Schur complement as

```text
S=mI-M_KI(mI+M_II)^(-1)M_IK.                                     (2.1)
```

For `m>4`, expanding the inverse gives paths of total length `r=n+2`.
Staggered nearest-neighbor hopping changes site parity at every step. Since
both endpoints belong to `(2Z)^4`, every odd `r` coefficient is identically
zero. This is stronger than the safe all-`r` majorant used previously.

At `r=2`, a cross-axis second step leaves two odd coordinates and cannot land
in `K`. There are eight backtracks and eight straight two-step paths. The
staggered sign is unchanged along a straight direction. A backtrack has
`M_(x,z)M_(z,x)=-1/4`, while a straight pair has transporter `V` and product
coefficient `+1/4` before the Schur minus. Summing gives (0.3).

The coordinate-free expression (0.4) proves positivity and the uniform gap.
It also proves gauge covariance directly. Straight coarse links intertwine
the declared blocked translations, proper cubic rotations, and compatible
time reflection. No hidden Haar coordinate occurs in (0.3), so extracting it
does not consume a cancellation estimate.

Let `P_2` denote coefficient extraction of the vacuum and the full kernel
(0.3), not merely its onsite scalar part. The centered interaction is

```text
V^o=(1-P_2)Gamma.                                                   (2.2)
```

Calling only `m+2/m` the center would leave the nearest-neighbor coarse
quadratic term in the interaction and would not achieve (0.5). The full
gauge-covariant shortest kernel is load-bearing.

## 3. Field and running-center chart

For two positive gap coordinates `m,m'`, the exact field torsor obeys

```text
||D_rho Phi||_(eta(m'))=||Phi||_(eta(m')/rho),
rho=eta(m')/eta(m)=sqrt(m/m').                                    (3.1)
```

Hence `D_rho` is an isometry from the `m`-adapted coefficient chart to the
`m'`-adapted chart, and an onsite coefficient `m` transforms to
`rho^(-2)m=m'`. This is a chart identity, not a dynamical equation selecting
`m'`.

Without applying `D_rho`, the identity map between two mass-adapted charts on
a polymer `X` obeys

```text
||Phi_X||_(eta(m'))
 <=exp[3|X|(log(m/m'))_+]||Phi_X||_(eta(m)).                       (3.2)
```

There are at most three balanced pairs per site, so a controlled relative
mass decrease can be paid by an explicit size-weight reserve. A future
autonomous theorem must derive the center update, prove its gap and reserve,
and fix `rho` by a declared normalization condition.

## 4. Residual activity and conditional ball diagnostic

The even-length restriction applies to both determinant loops and Schur paths;
`K_I` already sums even `r>=4`. Extraction of the commuting `r=2` bilinear
factors changes the Schur row to (0.5). It is exact factor regrouping, not a
subtraction from a norm bound.

The current bare constrained-fiber derivative still uses the product-Haar
reference while leaving retained Grassmann variables external. For that map,
the complete `r=2` kernel is fiber constant and its exact extraction changes
the base activity to (0.5). The K-retaining forced-attachment formulas
therefore apply to this current bare residual row, giving (0.7)--(0.8).

This does not extend those marked-attachment constants to the combined
expectation (1.4). A general covariance Gaussian can couple hidden sites;
contractivity and `E_mQ_m=0` alone do not provide the local product
factorization used by the marked-tree proof. A covariance locality/cluster
theorem and a next-factor activity row are still required.

For the source radius `r_src=log(1+c-K_res)`, retain the prior Cauchy envelope

```text
M_delta=2[68 exp(Lambda/2)c]/(r_src-delta)^2.                      (4.1)
```

The runner evaluates

```text
B_res+q_split delta+(M_delta/2)delta^2<delta                        (4.2)
```

at `delta=10^(-8)`. Equation (4.2) is conditional scalar feasibility. The
spatial strong-norm handoff, actual-range factor row, running gap, and same-
norm two-mark bound are still required before Banach contraction applies.
This is not yet an autonomous invariant ball.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_gaussian_adapted_berezin_quadratic_center_2026_07_12.py
```

The runner checks exact Gaussian monomial contractions, old versus adapted
fifteen-site norms, the `r_*` split-algebra inequality on a finite exterior
algebra, multi-index shift and modulation-tag bounds,
the dyadic two-hop classification and parity rule, the shortest-kernel gap,
field-chart identities, the exact residual activity/attachment constants,
the conditional scalar ball inequality, and the source/dependency contract.
The arbitrary-volume covariance-minor bound and infinite factor rows are
analytic.

## 6. No-Go Discipline N1--N8

The theorem is positive. Its boundary statements remain narrow because it
repairs one half of a prior no-go-sensitive autonomy problem.

### N1 — alternative-route enumeration

| Route | Status | Executed result |
|---|---|---|
| Keep `eta=10^(-10)` | `ATTEMPTED` | The prior exact fifteen-site norm is `10^720`. |
| Onsite Gaussian adaptation | `ATTEMPTED` | Equations (0.1)--(0.2) make every tensor depth contractive. |
| Leave all Schur paths in the interaction | `ATTEMPTED` | At (0.6), `K_(S,2)` dominates and the base defect exceeds the old source radius. |
| Extract only the onsite scalar | `ATTEMPTED` | Does not achieve (0.5): the straight `r=2` coarse-link bilinear is equally fiber constant. |
| Extract the full shortest quadratic kernel | `ATTEMPTED` | Equations (0.3)--(0.8) give the exact residual row and feasible scalar diagnostic. |
| Odd Schur paths | `ATTEMPTED` | Bipartite parity makes them identically zero between retained endpoints. |
| Finite-horizon multi-index Haar--Berezin atoms | `ATTEMPTED` | Equations (0.2a), (1.6)--(1.8) give the algebra, expectation, shift, and explicit Wilson-family handoff constants. |

Full covariance centers, multiscale provenance atoms, Peter--Weyl smoothing,
taste-faithful hypercube blocks, and small/large-field decompositions remain
live; they are not labeled attempted here.

### N2 — wall-independence audit

The four remaining conditions are `spatial actual-range provenance handoff`,
`running quadratic gap/normalization`, `physical taste/chart identification`,
and `critical trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| spatial provenance handoff | running quadratic gap | No | No | Yes |
| spatial provenance handoff | physical taste/chart | No | No | Yes |
| spatial provenance handoff | critical trajectory/observable | No | No | Yes |
| running quadratic gap | physical taste/chart | No | No | Yes |
| running quadratic gap | critical trajectory/observable | No | No | Yes |
| physical taste/chart | critical trajectory/observable | No | No | Yes |

### N3 — hidden-condition phrase scan

| Phrase | Classification |
|---|---|
| `Gaussian-adapted` | Exact norm condition (0.2), not a physical vacuum claim. |
| `running center` | Declared extracted coordinate; no selected flow equation. |
| `mass` | Gap/chart coordinate, not a derived physical mass. |
| `kinetic` | No physical kinetic normalization is assigned to (0.3). |
| `same norm` | Explicitly still absent spatially. |
| `autonomous` | Explicitly not established. |
| `by construction` | No proof-substitute use. |
| `standard RG` | No hit. |

### N4 — citation/residual matching

| Dependency | Exact use | Match? |
|---|---|---:|
| [Factor-two Schur theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Block geometry, hopping signs, exact Schur identity, covariance | Yes |
| [Retained-Grassmann polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Coefficient norm and determinant/Schur activity rows | Yes |
| [Declared RG chart](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact field-coordinate torsor | Yes |
| [K-retaining marked attachment](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Residual-row attachment and scalar Cauchy formulas | Yes |
| [Current-chart handoff boundary](WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Fifteen-site problem and running-center route | Yes |

### N5 — rhetoric and resolution audit

The Gaussian operator theorem holds for every finite hidden set under the
explicit quadratic gap. The local atom factorization separately uses the
onsite-product Gaussian reference. The numerical residual row is one bare ultra-massive
factor family after exact `r=2` extraction. It is not the factor row of every
action in a ball or every later scale. The atom algebra is finite-horizon and
the Wilson calculation uses one tag per contour coordinate; neither proves a
uniform tagged decomposition of the full actual RG range. The scalar inequality is not an
invariant-ball theorem. No fixed point, criticality, or continuum claim is
made. Extending forced attachment to the correlated Gaussian reference needs
a separate covariance-locality/cluster theorem and remains open.

### N6 — partial-closure and primitive scan

Quadratic coefficient extraction, covariance-weighted Berezin integration,
and field coordinates are regulator mathematics. The registered primitives
do not select the center, `rho`, physical mass, or taste. No missing
constructive estimate is reclassified as an axiom.

### N7 — hostile steelman

A hostile reviewer should insist that the next exact action is not purely
quadratic and that its quadratic center need not retain the gap (0.4). Correct;
the full interaction is retained, and persistence of a chosen running center
is open. Another should insist that Gaussian adaptation does not repair the
Wilson-loop support counterfamily. Correct; the spatial provenance handoff is
the next independent target. These live routes defeat any broader autonomy
claim.

### N8 — cross-cycle echo

Raw lifted unit directions were repaired by geometric rescaling; the
unlocalized derivative certificate was repaired by forced attachment. Here
the Grassmann tensor explosion is repaired by its covariance norm and the
dominant apparent interaction is moved to its exact quadratic coordinate.
The remaining spatial handoff is not an axiom-update signal.

**No-Go Discipline status: PARTIAL ATTEMPT.** The listed rows include
sequential construction steps and boundary controls rather than five
independent route families; no N1 PASS or route foreclosure is claimed.
