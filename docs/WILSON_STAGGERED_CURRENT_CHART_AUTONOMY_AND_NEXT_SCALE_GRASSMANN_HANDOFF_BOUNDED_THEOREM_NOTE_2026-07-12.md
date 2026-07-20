# Current-chart autonomy and next-scale Grassmann handoff boundary

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_current_chart_autonomy_grassmann_handoff_2026_07_12.py`](../scripts/wilson_staggered_current_chart_autonomy_grassmann_handoff_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_current_chart_autonomy_grassmann_handoff_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_current_chart_autonomy_grassmann_handoff_2026_07_12.txt)

## 0. Result

The one-step strong-to-weak contraction does not yet iterate in its present
chart for two independent reasons. Both are exact chart boundaries, not
dynamical or axiomatic no-go results.

Use the exact dyadic block/Schur map from the
[factor-two gauge-block theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the weak joint norm from the
[retained-Grassmann joint-polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the strong/weak norms from the
[K-retaining marked-attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md).

First, the current weak coarse norm cannot be embedded into the same next-step
strong centered norm by a support-only retagging with a finite scale-
independent constant. Let `X_L` be the vertices of the explicit simple
Wilson-loop family below and `T_L` its next-fiber hidden-coordinate support.
Every contour link is nonskeleton and occurs exactly once, so
`|T_L|=|X_L|`, `ell(T_L)>=diam(X_L)`, and product-Haar centering is exact.
For this family,

```text
||F_(X_L)||_strong/||F_(X_L)||_weak
 >=exp[(Lambda/2)diam X_L+(Theta/2+2c)|X_L|].                       (0.1)
```

A translated/reflected orbit sum of these long loops gives centered fixed-
representation interactions at arbitrarily large `X_L`. Equation (0.1)
diverges. Thus there is no finite
scale-independent handoff constant on the whole weak completion certified by
the current theorem.

This is not a model noncontraction theorem. It does not show that the narrower
actual RG range lacks stronger hidden
provenance. It shows that the half-weight weak certificate by itself does not
supply it.

Second, the product reference `E_0` used in the one-step split averages hidden
Haar variables coefficientwise while leaving every retained Grassmann
variable external. At the next factor-two step, fifteen of the sixteen coarse
fermion sites in a hypercube must instead be Berezin-integrated. The same
`E_0` is therefore not the next-scale conditional expectation on the full
generated action algebra.

For normalized one-site, three-color Gaussian Berezin expectation of mass
`m`, a balanced `p`-pair monomial has contraction `m^(-p)`. In the current
coefficient norm its input weight is `eta^(2p)`, so the exact operator ratio is

```text
C_p=(m eta^2)^(-p),             0<=p<=3.                            (0.2)
```

At the ultra-deep point `m=10^4,eta=10^(-10)`, the one-site norm is
`10^48`; a tensor product over fifteen eliminated sites has norm `10^720`.
This is no scale-uniform handoff in the present `eta` chart.

The exact straight support hierarchy itself is sound. For `q=2^k`, let
`H_q` replace each coarse link by its length-`q` straight path. Then

```text
H_(qr)=H_q after H_r,
diam H_q(X)>=q diam X,
|X|<=|H_q(X)|<=[1+4(q-1)]|X|.                                     (0.3)
```

It is gauge covariant, translation covariant under the declared blocked
translations, proper-cubic covariant, and reflection compatible. Full
origin-cell saturation is not an automatic repair: already in one dimension,
`Sat({0})={0,1}` fails reflection covariance because its reflected set is
`{0,-1}`.

Finally, on the ambient product-Haar coefficient algebra, a naive one-index
martingale norm cannot simultaneously make the level shift contractive and
remain a uniform Banach algebra. Shift contraction forces weights
`w_(j+1)>=w_j/q`. For a centered detail `h_j` with
`E(h_j)=0,E(|h_j|^2)=a_h>0` and an arbitrarily coarser modulation `g_k`, both
`h_j` and `conj(h_j)g_k` live at level `j`, while their product has coarse
projection `a_h g_k`. Hence

```text
C_alg>=a_h w_k/w_j^2 -> infinity,          a_h>0.                  (0.4)
```

This ambient-algebra witness is not by itself a boundary for the gauge-
invariant balanced subalgebra. The positive next route is a provenance-preserving multi-index
Haar--Berezin norm with Gaussian-adapted Grassmann weights and a running onsite
mass center. No axiom-update stop is established.

## 1. Exact dyadic support hierarchy

For a coarse link `(X,mu)`, define

```text
B^(k)(U)_(X,mu)
 =product_(r=0)^(2^k-1) U_(2^k X+r e_mu,mu).                        (1.1)
```

Straight path concatenation proves `B^(j+k)=B^j after B^k` after relabeling.
The corresponding support map `H_q` contains the sites `qX` and each declared
straight representative. Endpoint cancellation proves gauge covariance;
translations, proper cubic rotations, and the compatible time reflection
intertwine the same paths. The inequalities (0.3) follow because doubled
diameter endpoints remain and each of at most `4|X|` positive links adds at
most `q-1` interior sites.

This declared hierarchy is regulator chart data, not a physical block or taste
selector.

## 2. Current weak-to-strong spatial boundary

The strong centered mark in the direct dependency pays

```text
exp[(Theta+2c)|X|+Lambda diam X],                                  (2.1)
```

whereas its weak output certificate pays

```text
exp[(Theta/2)|X|+(Lambda/2)diam X].                                (2.2)
```

Fix two coordinate directions `mu,nu` and fix a third spectator coordinate to
an odd value. Let `C_L` be a simple `L`-by-`L` rectangular contour in the
`mu,nu` plane and let `W_L=(1/3)Tr product_(e in C_L)U_e` in the fundamental
representation. A skeleton link has all coordinates transverse to its
direction even. The fixed odd spectator therefore makes every link of `C_L`
nonskeleton. The contour is simple, so each hidden coordinate occurs exactly
once, its hidden support `T_L` has one coordinate per vertex of `X_L`, and
`ell(T_L)>=diam(X_L)`. Integrating any one contour coordinate against Haar is
zero; equivalently, multiplication of that link by an `SU(3)` center element
multiplies `W_L` by that element. Thus `E_0 W_L=0`.

Averaging `W_L` over the declared blocked translations, proper-cubic images,
and reflected image gives a nonzero centered scalar orbit interaction;
distinct supported terms retain the same coefficient lower bound. These
symmetries preserve the odd-spectator construction. Applying the strong marked
weight to `T_L` and the weak weight to `X_L` now gives (0.1). Increasing `L`
makes both diameter and size unbounded, proving that the identity/support-retag
map from the full weak completion to the next strong centered completion is
unbounded.

The earlier nonminimal syntactic supports are safe upper-bound devices for
membership. They cannot be used to inflate the strong denominator here.
Equation (0.1) uses the matched intrinsic supports `T_L` and `X_L`; their
cardinalities agree for this explicit family rather than by dummy padding.

Even an algebraically optimistic parent-shadow collapse does not repair the
size reserve: for an even straight chain with `|X|=N`, `|sigma X|=N/2`, its
size-weight cost contains `exp(cN)` and diverges for every `c>0`.

## 3. Next-scale Grassmann expectation

After one decimation, every retained site is a site of the coarse lattice. To
repeat the same block, only its even sublattice remains external and the other
fifteen sites per `2^4` cell are integrated. The exact one-step action contains
balanced quartic and higher monomials, so this is not a bilinear-only detail.

For one site with three colors,

```text
Z_m=integral dbar chi dchi exp[-m bar chi chi]=m^3.                 (3.1)
```

Normalized expectation contracts a balanced `p`-pair coefficient with
`m^(-p)` times the color antisymmetric contraction. The projective coefficient
`l1` norm makes this contraction sharp on a single ordered color monomial,
while the input monomial has weight `eta^(2p)`. This proves (0.2). Tensor
products over independent eliminated sites multiply operator norms, giving
the displayed `10^720` block value.

Choosing `eta` proportional to `m^(-1/2)` would normalize (0.2), but `eta` is
currently a one-step convergence coordinate. Turning that choice into an
autonomous rule requires a running mass center, field-coordinate flow, and
proof that the marked-polymer domain survives.

## 4. Ambient one-index martingale algebra boundary

Let `P_j` be the product conditional expectation through level `j` and
`Delta_j=P_j-P_(j+1)`. A norm

```text
N_w(F)=sum_j w_j||Delta_jF||+||P_infinity F||                       (4.1)
```

has a shift ratio at most `q<1` only if `w_(j+1)>=w_j/q`. Work first in the
ambient product-Haar coefficient algebra and choose a normalized nontrivial
Haar matrix coefficient as `h_j`; Schur orthogonality gives
`P_(j+1)h_j=0`. Normalize it in the coefficient sup norm and put
`a_h=P_(j+1)(|h_j|^2)>0`. For `h(U)=Tr(U)/3`, one has `a_h=1/9`. If `g_k` is
measurable at a much coarser level `k`, the usual detail-module property makes
both `h_j` and `conj(h_j)g_k` level-`j` details, while their product has
`a_h g_k` as a level-`k` component. With the base coefficient norm normalized
on `h_j` and multiplicative on the separated modulation, submultiplicativity would
require

```text
a_h w_k<=C_alg w_j^2.                                               (4.2)
```

For fixed `j` the left side grows at least as `q^(-(k-j))`, proving (0.4).
A bare link coefficient need not belong to the gauge-invariant scalar
subalgebra. Therefore (4.2) rules out the naive one-index construction on the
ambient algebra only; it does not rule out its restriction or a separately
constructed invariant norm. A multi-index atom norm that records both
cancellation and coarse modulation can also avoid this counterexample; model
membership in such a norm remains open.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_current_chart_autonomy_grassmann_handoff_2026_07_12.py
```

The runner checks straight-path semigroup composition on all four axes, the
support size/diameter bounds, the origin-cell reflection failure, an explicit
all-nonskeleton simple-loop family and its Haar-center zero, exponential weak/strong growth, the exact
one-site and fifteen-site Gaussian ratios, the martingale algebra lower-bound
growth, and the source/dependency contract. Infinite-family conclusions are
analytic.

## 6. No-Go Discipline N1--N8

The two boundaries concern the present chart/completion only.

### N1 — alternative-route enumeration

| Route | Status | Executed result |
|---|---|---|
| Direct current-norm identity handoff | `ATTEMPTED` | Equation (0.1) is unbounded on the explicit centered all-nonskeleton long-loop family. |
| Parent-shadow size payment | `ATTEMPTED` | The optimistic chain collapse still costs `exp(cN)`. |
| Full origin-cell saturation | `ATTEMPTED` | The runner gives an exact reflection-covariance failure. |
| Straight-path dyadic supports | `ATTEMPTED` | Equation (0.3) gives an exact compositional hierarchy but does not close the norm gap. |
| Product-Haar-only iteration | `ATTEMPTED` | It omits the next-scale Berezin elimination. |
| Haar--Gaussian product expectation | `ATTEMPTED` | Equation (0.2) gives the exact current-`eta` norm explosion. |
| Ambient one-index Haar martingale | `ATTEMPTED` | Equation (0.4) proves its ambient-algebra constant diverges; the invariant restriction remains open. |

Peter--Weyl heat weights, multi-origin covers, repeated forced attachment, and
taste-faithful blocks remain live and are not declared closed.

### N2 — wall-independence audit

The four conditions are `spatial weak/strong embedding`, `next-scale
Grassmann conditional expectation`, `physical taste/chart identification`,
and `critical trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| spatial weak/strong embedding | next-scale Grassmann expectation | No | No | Yes |
| spatial weak/strong embedding | physical taste/chart | No | No | Yes |
| spatial weak/strong embedding | critical trajectory/observable | No | No | Yes |
| next-scale Grassmann expectation | physical taste/chart | No | No | Yes |
| next-scale Grassmann expectation | critical trajectory/observable | No | No | Yes |
| physical taste/chart | critical trajectory/observable | No | No | Yes |

### N3 — hidden-condition phrase scan

| Phrase | Classification |
|---|---|
| `minimal support` | Equation (0.1) uses the same intrinsic support; dummy padding is forbidden. |
| `block saturated` | Tested origin-cell saturation is not promoted because reflection covariance fails. |
| `canonical origin` | The dyadic origin is declared regulator data, not physically selected. |
| `natural handoff` | No such handoff is assumed; the current identity handoff is disproved. |
| `identify scales` | Only the fixed dyadic relabeling is used. |
| `same norm` | Explicitly absent. |
| `translation invariant` | Only translations intertwined by the declared block are claimed. |
| `autonomous` | Not established. |
| `relevant` | No physical relevance classification. |
| `by construction` | No proof-substitute use. |
| `uniformly equivalent` | No equivalence is assumed. |
| `retag` | Support-only retagging is exactly the tested unbounded map. |

### N4 — residual matching

| Dependency | Exact use | Match? |
|---|---|---:|
| [Factor-two gauge-block theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Dyadic geometry and the one-even-site retained pattern giving the fifteen-site next-step count | Yes |
| [Joint-polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Weak all-degree output norm | Yes |
| [Marked-attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Strong centered norm and strong/weak boundary | Yes |

No raw-unit or critical-continuum result is used as an autonomy witness.

### N5 — rhetoric and resolution audit

The spatial counterfamily tests the full certified weak completion, not the
unknown actual RG range. The Gaussian calculation tests one site and its exact
fifteen-site tensor product, not a redesigned running-`eta` norm. The
martingale boundary tests the ambient product-Haar algebra with one-index
weights, not the gauge-invariant restriction or multi-index/paraproduct norms.
No actual model noncontraction, invariant-ball impossibility, or continuum
impossibility is claimed.

### N6 — partial-closure and primitive scan

Support grammars, conditional expectations, Gaussian-adapted field norms,
running centers, and martingale tags are constructive chart mathematics. The
registered primitives neither grant nor obstruct them. No missing handoff is
reclassified as an axiom.

### N7 — hostile steelman

The actual cluster output may carry strong support and cancellation provenance
discarded by the half-weight estimate. A multi-index Haar--Berezin atom norm
with `eta_j` tied to the running mass could retain that provenance, remain an
algebra, and inherit the small marked-attachment constant. This live route
defeats any broader autonomy no-go.

### N8 — cross-cycle echo

Raw unit directions were controlled by geometric rescaling; the failed
absolute Cauchy certificate was repaired by forced attachment. The same pattern
supports another constructive norm refinement here. The current-chart
boundary is not an axiom-update signal.

**No-Go Discipline status: PARTIAL ATTEMPT.** The listed calculations are
executed boundary checks, not five independent closures of the autonomy wall;
no N1 PASS or route foreclosure is claimed.
