# Constrained-fiber Dobrushin control and raw coarse-action unit directions

**Date:** 2026-07-12  
**Type:** bounded_theorem  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/wilson_staggered_constrained_fiber_dobrushin_raw_rg_unit_directions_2026_07_12.py`](../scripts/wilson_staggered_constrained_fiber_dobrushin_raw_rg_unit_directions_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/wilson_staggered_constrained_fiber_dobrushin_raw_rg_unit_directions_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_constrained_fiber_dobrushin_raw_rg_unit_directions_2026_07_12.txt)

## 0. Result

The exact factor-two block map now has its first constrained-fiber control and
its first exact action-space limitation.

Start from the declared straight-link blocking and Schur weight constructed in
the direct dependency,
[exact factor-two gauge blocking and Schur/OS semigroup](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md).
Write the fine one-link interaction majorant as

```text
kappa(m)=14/(m^2+2),
alpha(beta,m)=18beta +(3/2)kappa^2(2-kappa)/(1-kappa)^2.              (0.1)
```

Fixing every coarse straight link `V=B(U)` leaves independent hidden Haar
coordinates. A nonskeleton hidden coordinate controls one fine link. A
skeleton coordinate `A` controls the pair

```text
U_1=A,                    U_2=A^(-1)V.                               (0.2)
```

These one- or two-link footprints partition all fine links. The hidden-system
Dobrushin row therefore satisfies the uniform bound

```text
alpha_fiber<=2alpha.                                                  (0.3)
```

Consequently the **deep constrained-fiber wedge**

```text
alpha(beta,m)<1/2                                                     (0.4)
```

has, for every coarse configuration `V`, one hidden infinite-volume Gibbs
state, boundary-condition convergence, and a positive exponential comparison
weight. The constants are uniform in `V`. Concrete bounds include

```text
m=8:  beta<0.0169782141...,
m=10: beta<0.0238489507...,
beta=0: m>6.5990796748... .                                          (0.5)
```

This closes the first model-specific ingredient that image-measure mixing did
not supply: uniform control of the hard fibers themselves. It does not yet
construct a volume-uniform coarse interaction or a multiscale trajectory.

The second result is exact and independent of smallness. Let `R` denote the
raw constrained-fiber integration step on actions. For any local
gauge-invariant coarse function `f(V)` and its fine lift `L f=f after B`,

```text
R(Phi+t Lf)=R(Phi)+t f.                                               (0.6)
```

Thus raw fiber integration has norm-one directions on fiber-measurable
coordinates in a common unrescaled sup/projective coefficient norm. A strict
contraction on the full unprojected action space is impossible in that norm.
Vacuum/relevant-coordinate extraction, geometric and field rescaling, and a
scale-weighted irrelevant-sector norm are not optional bookkeeping; they are
the next mathematical objects required for a genuine RG contraction theorem.

Equation (0.6) does not forbid contraction after those operations and does not
identify an RG eigenvalue before a scale identification is declared.

No axiom-update stop is established.

## 1. The generated-action coordinate space

For a connected coarse polymer `X`, let `E_X` be its coarse links and let the
local gauge group act jointly on links and retained fermions. The natural
coefficient space is

```text
A_X=[C(SU(3)^(E_X)) tensor
     Lambda_even,balanced(bar psi_X,psi_X)]^(G_X).                    (1.1)
```

Joint invariance is load-bearing. It includes covariant open-line terms such
as `bar psi_x V_gamma psi_y`; taking gauge-invariant link functions and a
separate Grassmann tensor product would incorrectly omit them.

Expand

```text
Phi_X=sum_(p,P,Q; |P|=|Q|=p)
      bar psi_P phi_(X;P,Q)(V) psi_Q.                                (1.2)
```

For a chosen polymer decomposition and positive parameters
`lambda,theta,eta`, define the coefficient norm

```text
||Phi_X||_eta
 =sum_(p,P,Q) eta^(2p)||phi_(X;P,Q)||_infinity                       (1.3)
```

and the anchored interaction norm

```text
||Phi||_(lambda,theta,eta)
 =sup_z sum_(connected X contains z)
   exp[lambda diam X+theta |X|] ||Phi_X||_eta.                        (1.4)
```

Each `A_X` is a closed subspace of a finite-Grassmann extension of continuous
functions and is Banach. The weighted anchored `l1` sum is therefore Banach.
For overlapping polymers, Grassmann multiplication and pointwise coefficient
multiplication land in `A_(X union Y)`; the diameter and size weights are
submultiplicative. Haar integration is coefficient-wise contractive in the
sup norm.

On a finite regulator, a weight with strictly positive body can be written

```text
W=w_0(1+N),
-log W=-log w_0-sum_(j=1)^J (-1)^(j+1)N^j/j,                         (1.5)
```

where `N` is Grassmann-nilpotent and the sum is finite. Thus the exact weight
from the direct dependency belongs to the full finite-volume version of
(1.1), which has room for balanced quartic and higher monomials rather than
forcing a bilinear truncation.

This finite algebraic membership is not the desired locality theorem. Putting
the whole regulator into one polymer makes (1.4) volume dependent. A
volume-uniform connected-polymer decomposition and norm bound remain to be
proved.

## 2. Exact hidden-coordinate footprint bound

Use the disjoint Haar coordinates of the direct dependency. Associate to each
hidden coordinate `h` its fine-link footprint `E_h`:

- `|E_h|=2` for a skeleton pair in (0.2);
- `|E_h|=1` for a nonskeleton link.

The family `{E_h}` partitions the positive-oriented fine links.

Let `q_(e,f)` be the nonnegative interaction-oscillation majorant used in the
fine one-link Dobrushin proof. It obeys

```text
sup_e sum_f q_(e,f)<=alpha.                                          (2.1)
```

Changing hidden coordinate `k` changes only links in `E_k`. The same
likelihood-ratio oscillation lemma gives the hidden influence majorant

```text
q^H_(h,k)<=sum_(e in E_h)sum_(f in E_k)q_(e,f).                      (2.2)
```

Sum over `k` and use the footprint partition:

```text
sum_k q^H_(h,k)
 <=sum_(e in E_h)sum_f q_(e,f)
 <=|E_h|alpha
 <=2alpha.                                                           (2.3)
```

All sup norms are uniform in the fixed products `V`, so (2.3) is uniform over
the entire coarse configuration space. Condition (0.4) now gives Dobrushin
uniqueness and boundary comparison on every constrained fiber.

The determinant-loop interaction has an exponential moment and the Wilson
part is finite range. Substitution (0.2) enlarges supports by a bounded amount.
Strictness of `2alpha<1` and continuity of the weighted row at zero therefore
give some `lambda_H>0` with hidden weighted row below one. This proves a
uniform positive exponential comparison rate. No explicit optimal
`lambda_H(beta,m)` is claimed.

The ordinary strict wedge `alpha<1` alone does not close this inherited
certificate: (2.3) then gives only `alpha_fiber<2`. This is a limitation of
the available footprint majorant, not evidence that fibers outside (0.4) are
non-Gibbsian or nonunique. Block criteria, cancellation, or a sharper
constrained-coordinate estimate can enlarge the region.

## 3. Exact raw-integration unit directions

Let the finite-volume raw effective action be

```text
R(Phi)(V,bar psi,psi)
 =-log integral_(B(U)=V) dH exp[-Phi(U,bar psi,psi)],                 (3.1)
```

with the positive body normalization and finite Grassmann logarithm understood
as in (1.5). Let `f(V)` be any bounded local gauge-invariant coarse function.
Because `Lf(U)=f(B(U))` is constant on each fiber,

```text
integral_(B(U)=V)dH exp[-Phi(U)-tLf(U)]
 =exp[-t f(V)] integral_(B(U)=V)dH exp[-Phi(U)].                     (3.2)
```

Taking the logarithm proves (0.6) without approximation.

For example, let `f` be one coarse plaquette. Its lift is the perimeter of a
fine `2x2` Wilson loop. The raw integration step transmits its coefficient
exactly. In the same unrescaled sup/projective coefficient norm, the
directional Lipschitz ratio is one, so the full raw map cannot have contraction
constant below one.

The support of `Lf` is larger in fine lattice units and becomes unit size only
after geometric rescaling. Therefore (0.6) is not called an eigenvalue-one
statement for an autonomous RG operator. A rescaled, scale-weighted map on a
projected irrelevant complement can still contract.

The vacuum direction has the same lesson: normalization must be extracted
rather than included in a hoped-for strict contraction of every coordinate.

## 4. The remaining constructive theorem

The next map must decompose the exact coarse logarithm into connected
`Phi_X`, extract vacuum and relevant coordinates, rescale, and prove a bound of
the form

```text
||P_irrel R_rescaled(Phi)-P_irrel R_rescaled(Phi')||
 <=q ||Phi-Phi'||,                q<1,                               (4.1)
```

on a volume-uniform neighborhood in (1.4).

The new fiber theorem supplies uniform conditional mixing on (0.4), but a
connected-cumulant/tree estimate in the joint gauge--Grassmann norm is still
missing. In particular, pair covariance decay alone does not automatically
bound every higher cumulant with the combinatorics required by (1.4).

Live routes include a Kotecky--Preiss polymer estimate, a Dobrushin--Shlosman
block norm, a gauge-fixed small-/large-field expansion, an auxiliary-field
enlargement, and a taste-faithful hypercube map. Existing scalar, pure-gauge,
three-dimensional QED, and free-chain RG results are method context only.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_constrained_fiber_dobrushin_raw_rg_unit_directions_2026_07_12.py
```

The runner checks the footprint partition and factor-two row aggregation,
deep-wedge examples, weighted polymer-tail convergence, finite Grassmann-log
generation of a quartic term, exact fiber-constant factorization, the norm-one
unrescaled directional ratio, and the source/N1--N8 boundary. Infinite-volume
Dobrushin comparison and Banach completeness are analytic statements.

## 6. No-Go Discipline N1--N8

The bounded theorem contains a negative full-space-contraction boundary, so
all eight checks are load-bearing.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it remains live outside the claim |
|---|---|---|---|
| Deep constrained-fiber Dobrushin control | `ATTEMPTED` | Equations (2.1)--(2.3) close it for `alpha<1/2`. | Sharper or block estimates can enlarge the region. |
| Full strict-wedge inheritance | `ATTEMPTED` | The available footprint row gives only `2alpha`. | Failure of this majorant is not fiber nonuniqueness. |
| Joint gauge--Grassmann polymer space | `PARTIAL / LIVE` | Section 1 defines the coefficient space and norm but does not execute a uniform decomposition bound. | Its exact coarse interaction still needs that bound. |
| Kotecky--Preiss cluster expansion | `UNTESTED / LIVE` | No coupled constrained-fiber activity row is supplied here. | The new fiber mixing is a usable input to a future activity bound. |
| Relevant-coordinate projection/rescaling | `UNTESTED / LIVE` | Equation (0.6) motivates this route but no projection is executed. | Projection can remove the exact raw unit directions. |
| Auxiliary-field Gaussianization | `UNTESTED / LIVE` | No auxiliary carrier is introduced. | A larger field space can trade higher monomials for conditional bilinears. |
| Taste-faithful hypercube variables | `UNTESTED / LIVE` | No covariant spin--taste reorganization is executed. | A covariant spin--taste multiplet remains live. |
| Balaban/Dimock or block-RG architecture | `UNTESTED / LIVE` | No such architecture is instantiated for this coupled fiber. | Their small/large-field and block methods can be investigated separately. |

### N2 — wall-independence audit

The collapsed open conditions are `uniform connected-polymer/cumulant bound`,
`relevant-coordinate extraction and rescaling`, and `physical critical
trajectory/observable identification`.

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| uniform connected-polymer/cumulant bound | relevant-coordinate extraction and rescaling | No | No | Yes |
| uniform connected-polymer/cumulant bound | physical critical trajectory/observable identification | No | No | Yes |
| relevant-coordinate extraction and rescaling | physical critical trajectory/observable identification | No | No | Yes |

The Banach-space definition, higher-cumulant combinatorics, and uniform
stability estimate are components of the first condition, not separate walls.

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | No hidden background premise. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical` | No unqualified use. |

### N4 — citation/residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Exact factor-two gauge block and Schur/OS semigroup](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact fiber coordinates, coarse weight, and generated-term boundary | Uniform fiber control and raw action-map directions for that same map | Yes | Sole direct dependency. |
| Abstract Banach contraction theorem | Consequences after a norm/map/contraction are supplied | Proving the coupled norm estimate | No | Context only. |
| Pure-gauge polymer floor | Small-coupling Wilson plaquette activities | Coupled determinant and constrained fibers | No | Context only. |
| Free-chain Schur decimation | One-dimensional free fixed-energy downfolding | Four-dimensional coupled action-space map | No | Context only. |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| One hidden skeleton coordinate | Yes | It controls at most two fine links. |
| Every fixed coarse configuration in the deep wedge | Yes | Uniform hidden Dobrushin uniqueness/mixing certificate. |
| Ordinary strict wedge outside `alpha<1/2` | No | No fiber phase or Gibbsianness conclusion. |
| Finite-volume generated Grassmann algebra | Yes | Exact logarithm belongs after positive body normalization. |
| Volume-uniform connected interaction norm | No | Candidate space is defined; membership bound remains open. |
| Raw unrescaled fiber map | Yes | Fiber-measurable coefficient directions pass unchanged. |
| Projected and rescaled irrelevant RG map | No | No contraction or noncontraction claim. |
| Critical continuum trajectory | No | No existence or impossibility claim. |

### N6 — partial-closure and primitive scan

The new input is a declared regulator block map already constructed in the
direct dependency. Everything here is derived interaction and conditional-
measure mathematics. No axiom, probability rule, time law, or framework
primitive is added or enlarged.

The remaining closure path is ordinary: prove the connected-polymer estimate,
define relevant coordinates, rescale, and tune. A labeling convention cannot
supply those estimates, but their absence is not an axiom contradiction.

### N7 — hostile steelman

A hostile reviewer should say that relevant and marginal directions are
expected in Wilsonian RG, so a raw norm-one direction is not an obstruction to
RG. Correct. Equation (0.6) rules out only a strict contraction of the full
unprojected, unrescaled coefficient space in a common norm. It motivates the
standard projection/rescaling architecture and leaves contraction of the
irrelevant complement entirely open. Likewise, the factor-two fiber row is a
sufficient majorant, not an optimal phase boundary.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Lesson here |
|---|---|---|
| Factor-two block/Schur theorem | Exact coarse weight existed without a local action norm | Hard-fiber control is attacked directly rather than inferred from image mixing. |
| Certificate-boundary non-identification | A sufficient majorant has no converse | `2alpha>=1` is no evidence of fiber nonuniqueness. |
| Free-chain Schur decimation | Exact decimation migrated form | The joint generated-action space is enlarged instead of forcing bilinear closure. |
| Abstract Banach contraction scaffold | A contraction theorem needs a supplied map and norm estimate | The present result defines the coordinates and locates the missing estimate. |

No prior route was closed by renaming. The positive deep-fiber theorem and the
raw unit-direction identity both sharpen the next constructive task.

**No-Go Discipline status: PARTIAL ATTEMPT.** All eight bookkeeping sections are answered, but only the routes explicitly exercised above count as attempted; live and partial routes are not an N1 PASS. Two routes
are attempted; the negative boundary is limited to the unprojected raw step; and
no projected RG, continuum route, or axiom family is declared closed.
