# Two-horizon skeleton pullback with canonical re-Hoeffding intertwining

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_two_horizon_skeleton_pullback_reatomization_2026_07_12.py`](../scripts/wilson_staggered_two_horizon_skeleton_pullback_reatomization_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_two_horizon_skeleton_pullback_reatomization_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_two_horizon_skeleton_pullback_reatomization_2026_07_12.txt)

## 0. Result

The complete present Wilson--staggered bare residual factor system has an
exact two-horizon skeleton-pullback/re-Hoeffding lift. The construction keeps
the full factor coefficients, substitutes the next straight skeleton, and
only then forms canonical atoms in the future gauge/endpoint provenance
coordinates. Future-tag
creation and erasure relative to current coefficients are both handled by an
evaluation-commuting two-level intertwining identity; no Boolean tag-survival
rule is assumed.

Use the exact straight factor-two disintegration from the
[gauge-block/Schur theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the support and field chart from the
[declared RG-chart theorem](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the full current residual factor grammar and decorated cluster algebra
from the
[one-horizon lineage theorem](WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Write the current and next skeleton substitutions as

```text
U_1=A,       U_2=A^(-1)V,
V_1=B,       V_2=B^(-1)W.                                         (0.1)
```

The current integration coordinates `J_a^0` are hidden fine Haar links. The
future provenance coordinates `J_a^1` include the first members `B` of future
skeleton pairs, every coarse `V` link outside those pairs, and the at-most-two
fixed-`m` onsite Gaussian endpoint factors of a Schur word. Moving the endpoint
projections from the current decoration to the future decoration is permitted
because they remain external to current Haar integration; they are not
duplicated as a second Gaussian layer. All distinct coordinate expectations
commute. With

```text
r_*=1+sqrt(2),                   C_*=r_*^2=3+2sqrt(2),              (0.2)
```

define the exact two-level factor atoms

```text
Delta_(T,S)^(0->1) f_a
 =Delta_S^1 Delta_T^0 [f_a(A,R_2(Y_1,W))].                          (0.3)
```

Then

```text
f_a(A,R_2(Y_1,W))=sum_(T,S) Delta_(T,S)^(0->1)f_a,                 (0.4)

sum_(T,S) r_*^(|T|+|S|)||Delta_(T,S)^(0->1)f_a||
 <=C_*^(n_a^0+n_a^1)||f_a||.                                      (0.5)
```

The safe actual-factor coordinate counts after shortest-center extraction are

```text
(n_a^0,n_a^1)<=(4,4)       for a Wilson plaquette,
(n_a^0,n_a^1)<=(r,0)       for a determinant word of length r,
(n_a^0,n_a^1)<=(r,4)       for a residual Schur word of length r.  (0.6)
```

The zero in the determinant row is exact: an eliminated `I-I` word contains
no current skeleton fine link. A Schur word has only its two skeleton boundary
links available to carry future `V` dependence.

Let `h=4/m`, `L=Theta+2c+Lambda`,
`x_r=9 eta^2 2^(-r)m^(-(r-1))`, and `g(x)=(exp(x)-1)/x`. Applying (0.5) at
the factor level before either cluster grouping gives

```text
K_W^(2)=12[exp((3beta/4)C_*^8)-1]exp(4L),                          (0.7)

K_I^(2)=(3/2)sum_(even r>=4)
          C_*^r h^r g(3C_*^r h^r/r)exp(rL),                       (0.8)

K_S^(2)=18eta^2 sum_(even r>=4)
          C_*^(r+4)r h^(r-1)g(C_*^(r+4)x_r)exp(rL),               (0.9)

K_2=K_W^(2)+K_I^(2)+K_S^(2).                                     (0.10)
```

At

```text
m=15000, beta=0, c=0.001, Theta=10^(-6), Lambda=1,
eta=m^(-1/2),                                                       (0.11)
```

the exact series give

```text
q_hop=0.004233344463883...,
K_I^(2)=4.817630355648... 10^(-10),
K_S^(2)=6.671509288145... 10^(-6),
K_2=6.671991051180... 10^(-6)<c.                                  (0.12)
```

The two-layer cluster conversion lands the pulled-back base residual in the
weak coarse spatial norm with canonical future provenance atoms:

```text
||Gamma_res after R_2||_(Lambda/2,Theta/2,eta;future-atoms)
 <=B_2:=68exp(Lambda/2)K_2
 =7.480172423521... 10^(-4)<c.                                    (0.13)
```

For a current-product-Haar-centered input mark normalized in the double-
decorated strong source norm, the same algebra gives

```text
q_centered^(2)=0.555188304219...,
q_split^(2)=max{exp(-1/2),q_centered^(2)}
           =0.606530659713...<1.                                  (0.14)
```

There is also a strict interval

```text
0<=beta<1.505860908679... 10^(-12)                                (0.15)
```

with all other parameters fixed as in (0.11). Equations (0.13)--(0.14) are a
two-horizon canonical-atom weak membership and one-mark strong-to-weak
estimate, not a return to the next strong spatial weights, an invariant ball,
or an autonomous RG contraction.

## 1. Exact pullback and commuting atom projections

For each coarse link, the second equality in (0.1) is the same exact Haar
coordinate change as at the first scale:

```text
dB d(B^(-1)W)=dB dW.                                               (1.1)
```

The current and future skeleton paths are link-disjoint within their own
scales, and the exact blocking semigroup identifies the second pullback with
straight path concatenation. Coarse links outside the future skeleton remain
future hidden Haar coordinates unchanged. The complete coordinate change is
surjective, so it preserves the factor sup norm.

For `i in J_a^k`, put `Q_i^k=1-E_i^k` and

```text
Delta_T^k=product_(i in T)Q_i^k product_(i in J_a^k minus T)E_i^k.
                                                                         (1.2)
```

The current Haar coordinates and the future gauge/endpoint provenance
coordinates act on distinct variables. The fixed-`m` endpoint atom is
projected once, at the future level, rather than projected twice.
Consequently

```text
Delta_S^1 Delta_T^0=Delta_T^0 Delta_S^1,                           (1.3)
sum_(T,S)Delta_S^1 Delta_T^0=1.                                   (1.4)
```

For each level, `||Q_i^k||<=2`. Applying the one-level bound twice gives
(0.5). Equivalently, the two-level re-atomization intertwining is the exact
identity

```text
Delta_S^1 [sum_T Delta_T^0(f_a after R_2)]
 =sum_T Delta_S^1 Delta_T^0(f_a after R_2).                        (1.5)
```

Here `R_2(Y_1,W)` includes unchanged future nonskeleton links as well as the
skeleton substitutions in (0.1). Let `E_0` denote the physical current
hidden-link Haar integration. It leaves
all future hidden links and retained endpoint variables external, hence

```text
E_0 Delta_S^1=Delta_S^1 E_0.                                     (1.6)
```

Equations (1.5)--(1.6), rather than inherited Boolean labels, are the
tag-update law.

Two opposite exact witnesses explain why the full coefficient is necessary.
The residual length-four path from the previous theorem can reduce to `V` and
have only the empty current atom. After (0.1), either `V=B` or
`V=B^(-1)W`; its fundamental `B` dependence has a nonempty future atom. Thus
an empty current tag can become a future tag. Conversely,

```text
V_1V_2=B B^(-1)W=W,                                                (1.7)
```

so two individually future-tagged coefficients can multiply to an empty
future atom. The evaluated Hoeffding algebra performs both fusions exactly.

## 2. Two-horizon decorated cluster evaluation

For an overlap-connected current factor collection `Gamma`, choose current
and future atom subsets `(T_a,S_a)` for every factor and define

```text
w_hat_Gamma^(2)({T_a,S_a};Y_1,W)
 =integral dH_0 product_(a in Gamma)
   Delta_(T_a,S_a)^(0->1)f_a.                                    (2.1)
```

Here `dH_0` is exactly the current physical hidden Haar integration, and
`Y_1` comprises future skeleton-first and nonskeleton hidden links together
with the retained endpoint variables. The fixed-`m` endpoint atoms are part
of the future coefficient provenance. Future atoms are coefficient
decompositions, not an early integration over `Y_1`.
Finite reconstruction, (1.6), and Fubini give

```text
sum_({T_a,S_a})w_hat_Gamma^(2)
 =w_Gamma after R_2.                                               (2.2)
```

Run both the connected factor grouping and the hard-core logarithm in the
free two-level lineage algebra. Its product concatenates original factor
labels and both atom subsets. Let `ev_1` multiply and fuse future atoms in the
actual Hoeffding algebra, sum all decorations, and forget the formal lineage.
The coordinatewise `r_*` split algebra has product constant one, so `ev_1` is
contractive from the free double-lineage projective `l1` norm to the evaluated
canonical future-atom norm. Absolute convergence under (0.10) permits
evaluation term by term:

```text
ev_1(Gamma_hat_res^(2))=Gamma_res after R_2.                        (2.3)
```

Applying an actual future projection after evaluation gives the genuine
canonical output atoms:

```text
Delta_S^1(Gamma_res after R_2)
 =Delta_S^1 ev_1(Gamma_hat_res^(2)).                               (2.4)
```

No individual formal lineage is identified with the left side of (2.4).
Lineages may fuse into a different atom subset, including the empty subset.

Normalized Haar expectations and the fixed-`m` onsite color-scalar Gaussian
expectations intertwine gauge transformations, while blocked translations,
proper cubic rotations, and the compatible reflection permute or dualize
coordinate slots. Therefore the two-level atom algebra is equivariant and
(2.3) remains jointly gauge invariant and compatible with the declared
lattice symmetries.

## 3. Actual-factor activity and canonical future-weak output

The Wilson row in (0.6) pays at most four current and four future hidden link
coordinates. A coarse `V` occurrence costs one future coordinate whether it
is a skeleton-first/second link or a nonskeleton hidden link. Determinant paths
pay only their current `r` eliminated-link coordinates. Residual Schur paths
pay `r` current link coordinates; their future provenance pays two retained
endpoint-site factors and at most two hidden gauge coordinates inherited from
their boundary `V` links.
For each primitive potential or bilinear `psi`, the constant-one double-atom
algebra gives

```text
||exp(psi)-1||_(2atom)
 <=exp(||psi||_(2atom))-1
 <=exp(C_*^(n_a^0+n_a^1)||psi||)-1.                               (3.1)
```

Applying this safe potential-level majorant before the two cluster groupings
gives the black-box factors in (0.7)--(0.9).

Because the double-lineage coefficient algebra has a projective weighted
`l1` product with constant one, the existing rooted-tree and hard-core
recursions apply with scalar activity replaced by the double-decorated
activity. If `K_2<c`, they yield (0.13). This is an actual-range atomization
statement for the complete present bare residual factor grammar pulled back
through the next skeleton, but its spatial weights remain the weak output
weights `(Lambda/2,Theta/2)`.

For a mark `O` centered under the full current hidden product-Haar expectation,
`E_0 O=0`, every future atom projection commutes with `E_0`. Thus
`E_0 Delta_S^1 O=0`, and its mark-only current fiber integral still vanishes.
When `O` is measured in the double-decorated strong source norm, the two
marked-path rerootings apply with `K=K_2`, giving (0.14) into the canonical-
future-atom weak output norm. No uncharged embedding of a generic undecorated
strong mark is asserted. This statement also does not replace current product
Haar centering by the correlated Gaussian center.

The strict inequalities `K_2<c`, `B_2<c`, and `q_split^(2)<1` at (0.11) show
that the base residual has controlled canonical future atoms in the weak
coarse norm and give a one-step double-decorated-strong to future-atom-weak
marked estimate represented in the two-adjacent-horizon atom packet. Upgrading
to the next strong spatial
weights would require a density/downshift estimate for nonempty future atoms
and a separate treatment of the empty future atom. Equation (1.7) proves that
empty future atoms really occur. A ball additionally requires the perturbation
factor grammar, a two-mark/same-norm Hessian, center-update and gap control,
and the correlated-reference attachment theorem.

## 4. Scope and remaining wall

This theorem closes the exact algebraic gauge-tag update route for the
complete current bare residual and one next skeleton pullback. It does not
establish a horizon-uniform factor grammar for arbitrary generated actions or
a new correlated-Gaussian endpoint chart.

- The cost `C_*^(n_a^0+n_a^1)` is a two-level black-box cost; no all-scale
  bound is inferred.
- Current and future atom labels are canonical only relative to the declared
  product references and skeleton chart.
- The fixed-`m` onsite endpoint atoms are projected in `J_a^1` and inherited
  through the gauge pullback; changing the Gaussian center requires a separate
  covariance/chart theorem and is not hidden in this fixed reference.
- Equation (0.13) controls the base residual, not every perturbation in a
  radius-`c` ball, and does so only at weak coarse spatial weights.
- Equation (0.14) uses a current product-Haar-centered mark. The correlated
  Gaussian `G_(A_II)` still couples sites and lacks a local marked-cluster
  attachment theorem in this campaign.
- The extracted quadratic center has not yet been proved to update with a
  uniform gap, and no normalization condition selects its running coordinate.

Thus there is no invariant ball, fixed point, tuned critical trajectory,
Lorentz/QFT continuum, Standard Model limit, gravity limit, or axiom-update
conclusion. No axiom-update stop is established.

The next exact targets are (i) a strong-spatial handoff splitting nonempty
future atoms from the genuine empty-atom/raw-lift sector and (ii) a covariance-
local cluster representation for the normalized correlated Berezin
expectation, with a marked-source estimate uniform under the displayed gap.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_two_horizon_skeleton_pullback_reatomization_2026_07_12.py
```

The runner checks nested atom reconstruction and the double `C_*` bound,
projection commutation, current-integration/future-atom commutation, exact tag
creation and erasure witnesses, finite decorated factor/logarithm evaluation,
representative grammar-derived coordinate-count fixtures, the activity and
marked rows, the strict beta interval, and the source/dependency contract. The
general coordinate-count proof and infinite cluster convergence use the
displayed analytic grammar and nonnegative KP majorant.

## 6. No-Go Discipline N1--N8

The theorem is constructive. This packet prevents a two-level identity from
being advertised as all-scale autonomy.

### N1 — alternative-route enumeration

| Route | Status | Executed result |
|---|---|---|
| Propagate current Boolean tags | `ATTEMPTED` | The `V` and `V_1V_2=W` witnesses show both tag creation and erasure, so this route fails exactly. |
| Substitute the next skeleton and re-atomize full coefficients | `ATTEMPTED` | Equations (1.3)--(1.6) prove the exact two-level intertwining. |
| Re-atomize only after current cluster evaluation | `ATTEMPTED` | Equations (2.3)--(2.4) give the exact output atoms, while the pre-integration lift supplies the activity bound. |
| Charge syntactic support as genuine tag density | `ATTEMPTED` | Equation (1.7) again gives an empty future atom despite two nonempty carriers. |
| Double-decorated KP output | `ATTEMPTED` | Equations (0.7)--(0.15) give a strict canonical-future-atom weak base row and one double-decorated-strong to future-atom-weak mark row. |

Strong-spatial tag-density/empty-atom handoff, correlated-Gaussian clusters,
all-generated-factor closure, center-update normalization, same-norm two-mark
bounds, Peter--Weyl smoothing, and taste-faithful blocking remain live and are
not labeled attempted.

### N2 — wall-independence audit

The five remaining conditions are `strong-spatial tag-density/empty-atom
handoff`, `correlated Gaussian attachment/running gap`, `generated-ball
Hessian/invariance`, `physical taste/chart identification`, and `critical
trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| strong-spatial handoff | correlated Gaussian attachment | No | No | Yes |
| strong-spatial handoff | generated-ball invariance | No | No | Yes |
| strong-spatial handoff | physical taste/chart | No | No | Yes |
| strong-spatial handoff | critical trajectory/observable | No | No | Yes |
| correlated Gaussian attachment | generated-ball invariance | No | No | Yes |
| correlated Gaussian attachment | physical taste/chart | No | No | Yes |
| correlated Gaussian attachment | critical trajectory/observable | No | No | Yes |
| generated-ball invariance | physical taste/chart | No | No | Yes |
| generated-ball invariance | critical trajectory/observable | No | No | Yes |
| physical taste/chart | critical trajectory/observable | No | No | Yes |

### N3 — hidden-condition phrase scan

| Phrase | Classification |
|---|---|
| `canonical re-Hoeffding` | Canonical only for the declared product reference and skeleton chart. |
| `intertwining` | The exact two-level projection identity (1.5), not a three-level composition or dynamical cocycle. |
| `actual range` | The complete present bare residual after one future pullback, canonically atomized only at weak spatial weights. |
| `future atoms` | Canonical coefficient atoms at the second horizon; they do not restore the next strong spatial weights. |
| `uniform` | Regulator-uniform for two horizons; never horizon-uniform. |
| `membership` | Base-point weak norm membership (0.13), not return to the next strong norm or invariance of a neighborhood. |
| `contraction` | Used only for the one-step double-decorated-strong to future-atom-weak mark number (0.14); no generic-source, same-norm, or autonomous-map claim. |
| `by construction` | No proof-substitute use. |

### N4 — citation/residual matching

| Dependency | Exact use | Match? |
|---|---|---:|
| [Gauge block/Schur theorem](MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact straight skeleton, Haar disintegration, semigroup, and determinant/Schur grammar | Yes |
| [Declared RG chart](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Fine/coarse support chart used with the half-weight output; the one-horizon dependency supplies the strong/weak boundary | Yes |
| [One-horizon lineage theorem](WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Complete residual factors, atom algebra, KP conversion, marked reuse, and current-tag witnesses | Yes |

### N5 — rhetoric and resolution audit

The factor grammar is complete only for the present bare residual after the
already extracted shortest center. The exact intertwining spans two adjacent
coordinate layers, while the converted spatial norm remains weak. The theorem
does not say that all generated perturbations have the same grammar, that the
strong-spatial handoff closes, that the center remains gapped, or that the
displayed massive point lies on a critical continuum trajectory.

### N6 — partial-closure and primitive scan

The result closes the two-level coefficient tag-update wall, but not the
strong-spatial handoff wall. It uses the already declared skeleton and product
expectations and adds no physical action, time, probability, carrier, taste,
scale, or state primitive. The remaining spatial, covariance, and invariant-
ball work is constructive analysis, not evidence that an axiom is missing.

### N7 — hostile steelman

A hostile reviewer should demand an example where current tags fail to predict
future tags; both directions are explicit in (1.7) and its preceding `V`
witness. They should also object that a finite two-level factor bound may grow
under further iteration and says nothing about perturbation closure. Correct;
the theorem claims neither horizon uniformity nor a ball. Finally, they should
demand the missing spatial half-weight restoration before calling (0.13) a
strong return, and correlated-Gaussian attachment before calling (0.14) a
running-center result. Correct; neither claim is made.

### N8 — cross-cycle echo

The prior block proved that formal lineage survives while ordinary tags need
not. This block does not rename lineage as support. It evaluates the full
coefficient through the next skeleton and recomputes canonical atoms. The
result repairs the coefficient tag-update wall while preserving the strong-
spatial, covariance, center, invariant-ball, and continuum walls.

**No-Go Discipline status: PARTIAL ATTEMPT.** These rows are executed checks
within one two-horizon construction, not five independent closures of the
iteration residual; no N1 PASS or route foreclosure is claimed.
