# Deep-fiber coarse-gauge Gibbsianness for the factor-two Wilson--staggered map

**Date:** 2026-07-12  
**Type:** bounded_theorem  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/wilson_staggered_deep_fiber_coarse_gauge_gibbsianness_2026_07_12.py`](../scripts/wilson_staggered_deep_fiber_coarse_gauge_gibbsianness_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/wilson_staggered_deep_fiber_coarse_gauge_gibbsianness_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_deep_fiber_coarse_gauge_gibbsianness_2026_07_12.txt)

## 0. Result

The exact factor-two gauge image now has an infinite-volume action
representation throughout the controlled hard-fiber region.

Use the same straight-link block map, hidden Haar coordinates, and interaction
majorant as the direct dependency,
[constrained-fiber Dobrushin control and raw action-map directions](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md).
Write

```text
kappa(m)=14/(m^2+2),
alpha(beta,m)=18 beta +(3/2)kappa^2(2-kappa)/(1-kappa)^2.             (0.1)
```

Whenever

```text
alpha(beta,m)<1/2,                                                    (0.2)
```

the infinite-volume coarse gauge image has a specification `gamma^c` with
three uniform properties:

1. every finite-link kernel has a strictly positive continuous density with
   respect to product `SU(3)` Haar measure;
2. the densities are uniformly non-null for each fixed finite region;
3. exterior coarse configurations that agree through radius `R` change a
   fixed local conditional density by at most `C_Delta exp(-lambda_c R)` in
   logarithmic ratio, for some `lambda_c>0`.

Thus the exact coarse specification is exponentially quasilocal and has no
hidden non-Gibbsian pathology in (0.2). The Gibbs-representation theorem for
compact product alphabets then supplies at least one absolutely summable
coarse gauge interaction `Psi^c`:

```text
for every e:  sum_(X contains e) ||Psi^c_X||_infinity < infinity.      (0.3)
```

This is the first infinite-volume absolutely summable coarse-action
representation for the declared coupled block map. The representation theorem does not by itself
give the exponentially weighted, connected, translation-adapted joint
gauge--Grassmann polymer norm requested in the previous block. In particular,
the selected norm-summable representative is not necessarily translation-covariant
or termwise gauge invariant. The coarse specification
it represents is gauge covariant and block-translation covariant.

No axiom-update stop is established.

## 1. Coarse image specification

Let `mu` be the unique infinite-volume gauge marginal in the strict fine
Dobrushin wedge and let

```text
nu=B_* mu                                                            (1.1)
```

on the positive-oriented coarse links. The single-link alphabet is compact
`SU(3)` with normalized Haar reference measure.

Equivalently, group the four positive outgoing links at each coarse site into
the compact single-site alphabet `SU(3)^4`; this is the ordinary product-lattice
form used by the Gibbs-representation theorem.

For a finite coarse-link set `Delta`, fix the exterior coarse products and
use the exact disjoint hidden-coordinate chart. Finite-box conditional
densities are ratios of constrained hidden partition functions. Condition
(0.2) gives a hidden influence row below one uniformly in every complete
coarse configuration. The weighted version gives a common positive
comparison rate `lambda_H`.

The constrained finite-box kernels therefore form a uniform Cauchy family as
the box grows. Their limits define `gamma^c_Delta`. Uniform convergence
preserves normalization and the finite-box consistency identity, so
`gamma^c` is a proper specification and `nu gamma^c_Delta=nu`.

This construction conditions on the actual coarse products. It does not
infer a local action merely from decay of correlations of `nu`.

## 2. Uniform non-nullness

Choose a reference value `v_*` for the links in `Delta` and use the same
hidden Haar coordinates for `v` and `v_*`. Replacing `v_*` by `v` changes only
the associated skeleton representatives. If `G_(v,v_*)` is the resulting
relative fine interaction, only terms meeting the changed skeleton links can
contribute. The finite-range Wilson part and the absolute moment of the massive
determinant interaction give

```text
sup_(v,v_*,omega,h) |G_(v,v_*)(h;omega)| <= C_Delta < infinity.       (2.1)
```

The constant depends on `Delta,beta,m`, not on volume or the exterior coarse
configuration `omega`; explicitly one may bound it by twice the absolute
interaction norm of all terms meeting those links. Interpolation between the
two constrained energies gives

```text
exp(-C_Delta)
 <= Z_Delta(v|omega)/Z_Delta(v_*|omega)
 <= exp(C_Delta).                                                     (2.2)
```

Normalization against probability Haar measure then yields

```text
exp(-C_Delta) <= p_Delta(v|omega) <= exp(C_Delta).                    (2.3)
```

Enlarging `C_Delta` if necessary covers the harmless choice of reference
chart. Equations (2.2)--(2.3) pass to the uniform infinite-volume limit.
There are no hard exclusions or zero conditional densities.

## 3. Exponential quasilocality

The determinant terms can be anchored at a fine site with order-`n` norm at
most `3 r^n/(2n)`, where

```text
r=16/(m^2+16)<1.                                                      (3.1)
```

Their support diameter is linear in `n`; the number of possible anchors at a
fixed link is polynomial in `n`. Hence there is `lambda_F>0` for which the
fine interaction has a finite exponential moment. The Wilson part is finite
range. The factor-two coordinate substitution changes diameters by only a
fixed factor.

Suppose exterior coarse configurations `omega,omega'` agree on the coarse
`R`-neighborhood of `Delta`. Compare the logarithmic partition-function ratio
in (2.2) under these two boundaries. Split `G_(v,v_*)` into a near part and a
tail. The direct tail is at most

```text
C_Delta exp(-lambda_F R).                                            (3.2)
```

For the near part, interpolate the hidden Hamiltonians,
`H_t=(1-t)H_(v_*)+tH_v`; no convex interpolation inside `SU(3)` is used. Every
interpolated hidden interaction obeys the same oscillation majorant: convex
energy interpolation cannot increase the row used in the likelihood-ratio
estimate. Weighted Dobrushin comparison therefore bounds the change of its expectation by

```text
C'_Delta exp(-lambda_H R).                                           (3.3)
```

Integrating the interpolation derivative first controls every reference ratio
`log[Z(v|omega)/Z(v_*|omega)]`. Haar normalization changes the resulting bound
by at most a factor two. Combining (3.2)--(3.3) therefore gives, after absorbing
that factor into the constant and with `lambda_c=min(lambda_F,lambda_H)>0`,

```text
sup_v |log p_Delta(v|omega)-log p_Delta(v|omega')|
 <= C''_Delta exp(-lambda_c R).                                      (3.4)
```

The same estimate holds uniformly along the finite regulators, so no
volume-dependent locality constant is hidden in the limit.

## 4. Gibbs representation and exact scope

The Gibbs-representation theorem used here is the compact-alphabet version of
the Kozlov--Sullivan characterization: a specification relative to a product
reference measure is generated by an absolutely summable interaction when it
is quasilocal and uniformly non-null. A directly matching formulation is
Theorem 2.12 of van Enter, Fernandez, and Sokal, *Journal of Statistical
Physics* **72** (1993), 879--1167. This is external mathematical machinery,
not a physical premise or a sector-specific law.

Sections 1--3 verify its hypotheses for `gamma^c`, so (0.3) follows. The
interaction generates the exact infinite-volume coarse specification; it is
not a fitted surrogate and is not restricted to the original Wilson action
family.

Three distinctions are load-bearing:

- sitewise absolute summability in (0.3) is not a uniform anchored supremum
  and is not an exponentially weighted polymer estimate;
- existence of one norm-summable representative does not provide a canonical,
  translation-covariant, or termwise gauge-invariant coordinate choice;
- this theorem concerns the positive gauge body after the fermions are
  integrated. Coefficients of the retained Grassmann variables require
  uniform source analyticity and all-order connected-cumulant bounds.

The transformed measure is therefore Gibbsian in the controlled wedge, but a
closed autonomous RG map on the full joint action space is not yet proved.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_deep_fiber_coarse_gauge_gibbsianness_2026_07_12.py
```

The runner checks nonempty deep-wedge examples, a positive massive fine
exponential moment, the normalized non-nullness lemma, combination of the
direct and comparison tails, and a finite exact `Z_3` block-image analogue.
It also checks the source boundary and direct dependency. The infinite-volume
comparison and Gibbs-representation steps are analytic statements.

## 6. Honest boundary and next theorem

The result closes coarse-gauge Gibbsianness, not the full constructive RG
program. The immediate remaining theorem is a uniform complex/source
neighborhood for the constrained fibers. Its derivatives must produce
factorial/tree bounds for all connected cumulants of the exponentially local
Schur coefficients and place the exact joint logarithm in a connected,
exponentially weighted gauge--Grassmann polymer norm.

Only after that theorem is it meaningful to declare relevant coordinates,
factor-two geometric and field rescaling, a complementary irrelevant norm,
and a contraction test on an invariant neighborhood. Neither (0.3) nor the
raw unit directions determine a beta function or a physical critical
trajectory.

## 7. No-Go Discipline N1--N8

The theorem names representation and joint-sector walls, so all eight checks
are included.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it remains live |
|---|---|---|---|
| Constrained-fiber image specification | `ATTEMPTED` | Sections 1--3 prove non-null exponential quasilocality in (0.2). | Sharper fiber criteria can enlarge the region. |
| Kozlov norm-summable representation | `ATTEMPTED` | Section 4 verifies the exact hypotheses. | More constructive representatives may preserve additional structure. |
| Sullivan covariant representation | `UNTESTED / LIVE` | Not used. | A symmetry-adapted variation-summable action can be studied separately. |
| Dobrushin--Shlosman complete analyticity | `UNTESTED / LIVE` | Ordinary weighted comparison is not a test of complete analyticity. | A block condition can supply all-order source control. |
| Kotecky--Preiss joint polymer expansion | `UNTESTED / LIVE` | No coupled activity row is supplied. | A deeper small-coupling/high-mass region may close it directly. |
| Dependency-graph cumulant bounds | `UNTESTED / LIVE` | Pair comparison is not an execution of this route. | A uniform source neighborhood can provide the missing factorial/tree estimate. |
| Taste-faithful hypercube blocking | `UNTESTED / LIVE` | No covariant spin--taste block is constructed. | A covariant spin--taste multiplet remains live. |
| Projected/rescaled irrelevant map | `UNTESTED / LIVE` | No projection or rescaling is declared here. | Raw unit directions can be removed from the tested complement. |

### N2 — wall-independence audit

The open conditions are `joint all-order polymer bound`, `symmetry-adapted
action coordinates`, `projected/rescaled contraction`, and `physical critical
trajectory`.

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| joint all-order polymer bound | symmetry-adapted action coordinates | No | No | Yes |
| joint all-order polymer bound | projected/rescaled contraction | No | No | Yes |
| joint all-order polymer bound | physical critical trajectory | No | No | Yes |
| symmetry-adapted action coordinates | projected/rescaled contraction | No | No | Yes |
| symmetry-adapted action coordinates | physical critical trajectory | No | No | Yes |
| projected/rescaled contraction | physical critical trajectory | No | No | Yes |

Coarse-gauge Gibbsianness is closed by Sections 1--4 and is not counted again
as an open wall.

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | Fine gauge background is a mathematical variable, not a hidden premise. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical` | Used only in a denied coordinate-choice claim. |

### N4 — citation/residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Constrained-fiber Dobrushin and raw directions](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Uniform hidden comparison; no volume-uniform coarse action | Coarse gauge specification and summable representation | Yes | Sole direct repository dependency. |
| Kozlov--Sullivan Gibbs representation | Quasilocality plus uniform non-nullness imply a summable interaction | Verifying those properties for this exact image | Yes | External mathematical theorem. |
| Dobrushin--Shlosman complete analyticity | All-order/complex-neighborhood control under stronger hypotheses | Joint source cumulants | No | Live context only. |
| Kotecky--Preiss criterion | Polymer convergence after an activity row is verified | Coupled activity row | No | Live context only. |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Every fixed finite coarse region in (0.2) | Yes | Uniformly non-null exponentially quasilocal kernel. |
| Infinite coarse gauge image | Yes | Exact Gibbs specification and an absolutely summable representative. |
| Translation-/gauge-adapted norm-summable representative | No | Specification symmetry only. |
| Uniform anchored supremum over coarse links | No | Not supplied by the selected noncovariant representative. |
| Exponentially weighted connected gauge potential | No | Not claimed. |
| Retained gauge--Grassmann action | No | All-order source theorem remains open. |
| Projected/rescaled RG map | No | No contraction or noncontraction claim. |
| Critical continuum trajectory | No | No existence or impossibility claim. |

### N6 — partial-closure and primitive scan

This block uses the previously declared regulator map and external Gibbs-field
mathematics. It adds no action axiom, probability rule, time law, field
content, or framework primitive. The coarse action is derived from the exact
image specification. Nonuniqueness of its interaction representation is a
mathematical coordinate freedom, not a request for a new physical axiom.

### N7 — hostile steelman

A hostile reviewer can object that pair mixing is weaker than complete
analyticity. That objection is correct and is why no joint all-order cumulant
claim appears. The present result instead uses weighted boundary comparison
only to prove continuity of finite conditional density ratios, then invokes
the precisely matched Gibbs-representation theorem.

A second hostile reviewer can object that an unspecified norm-summable
potential is not a usable autonomous RG coordinate. That is also correct. The
result removes the non-Gibbsianness wall for the coarse gauge body; it does not
remove the source-analyticity, symmetry-adapted-coordinate, or contraction
walls.

### N8 — cross-cycle echo

| Earlier cycle | Earlier residual | Present treatment |
|---|---|---|
| Spatial DLR accumulation | Fine gauge interaction was quasilocal and summable | Its exponential moment is used locally inside constrained fibers. |
| Dobrushin uniqueness | Fine state was unique and mixing | Uniform constrained comparison is applied to conditional density ratios. |
| Factor-two block map | Exact image measure existed without a local action | The image specification now has a summable interaction representation. |
| Raw unit directions | Full-space raw contraction was excluded | No projected/rescaled conclusion is inferred. |

No wall is retired by relabeling and no axiom update is requested.

**No-Go Discipline status: PARTIAL ATTEMPT.** The constrained-fiber and
Kozlov representation routes are executed. The six alternatives labeled
`UNTESTED / LIVE` are inventory only and do not count toward an N1 PASS.
