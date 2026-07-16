# Declared factor-two RG chart and geometric suppression of raw lifted directions

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_declared_rg_chart_raw_lift_geometric_contraction_2026_07_12.py`](../scripts/wilson_staggered_declared_rg_chart_raw_lift_geometric_contraction_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_declared_rg_chart_raw_lift_geometric_contraction_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_declared_rg_chart_raw_lift_geometric_contraction_2026_07_12.txt)

## 0. Result

The exact one-step joint action now has an explicit family of mathematical RG
charts. In those charts, the raw unit directions identified previously split
cleanly into a finite zero-diameter sector and geometrically suppressed
extended directions.

Use the joint action space and analytic one-step neighborhood from the
[simultaneous retained-Grassmann polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the exact raw lift identity from the
[constrained-fiber raw unit-direction theorem](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md).

This note declares, rather than physically selects, three chart ingredients:

1. a factor-two dilation support `H_2(X)` containing the doubled sites and
   straight two-link representatives of every link in `X`;
2. the projector `P_0` onto translation/symmetry-invariant diameter-zero
   interaction coordinates;
3. a positive field-coordinate parameter `rho` with
   `bar psi'=rho bar psi`, `psi'=rho psi`.

They obey the exact norm identity

```text
||D_rho Phi||_(lambda,theta,eta)=||Phi||_(lambda,theta,eta/rho),     (0.1)
```

and, at `rho=1`, every raw lifted interaction in `(1-P_0)` obeys

```text
||(1-P_0) D_(2,1) R L Phi||_(lambda,theta,eta)
 <=exp(-lambda)||(1-P_0)L Phi||_(lambda,theta,eta).                 (0.2)
```

Here `R L Phi=Phi` is the exact fiber-constant identity and `D_(2,rho)` means
factor-two support relabeling followed by `D_rho`. More generally, the norm
ratio of a pure balanced pair-degree `p` term on `X` is bounded by

```text
ratio_(X,p)<=rho^(-2p) exp[-lambda diam X]
              exp[-theta(|H_2(X)|-|X|)].                            (0.3)
```

for the declared support representative. Equation (0.2) retires the concern
that the infinite family of raw unit directions automatically forbids every
rescaled contraction. It proves contraction only on the extended
fiber-constant lifted subspace, not on the full derivative.

Any finite set of local Berezin/Peter--Weyl coefficient modes also defines a
bounded finite-rank coordinate projector. Different finite jet sets and every
`rho>0` give legitimate, generally inequivalent charts for the same exact
coarse functional. The existing science does not select one as the physical
relevant/marginal sector or choose a physical field normalization.

The theorem does not establish an invariant neighborhood, a full irrelevant
Lipschitz constant below one, nonlinear stability, a fixed point, a physical
beta function, taste selection, or a critical continuum trajectory.

No axiom-update stop is established.

## 1. Joint interaction space and local coordinate projectors

An element is a chosen connected interaction decomposition

```text
Phi={Phi_X},
||Phi||_(lambda,theta,eta)
 =sup_z sum_(X contains z)
   exp[lambda diam X+theta|X|]||Phi_X||_eta.                         (1.1)
```

For the translation- and supplied-symmetry-invariant subspace, retain every
diameter-zero coefficient in

```text
P_0 Phi={Phi_X:diam X=0}.                                           (1.2)
```

There are no link variables internal to a one-site polymer. With three color
components and balanced even Grassmann degree, the invariant local algebra is
finite-dimensional. Therefore `P_0` is a finite-rank idempotent on the
symmetry-invariant interaction space and

```text
||P_0||<=1,                    ||1-P_0||<=1                          (1.3)
```

for the fixed coefficient decomposition.

More elaborate declared jets are also available. Choose finitely many local
jointly gauge-invariant basis elements `e_j`, such as an onsite bilinear, a
symmetry-averaged shortest covariant bilinear, or a plaquette character. Their
Berezin coefficient and normalized Haar/Peter--Weyl coefficient maps are
bounded linear functionals `ell_j` in the sup/projective norm. After replacing
the basis by its finite Gram-dual if necessary,

```text
P_J Phi=sum_(j in J) ell_j(Phi)e_j,
P_J^2=P_J,                  rank P_J<infinity.                       (1.4)
```

This is coordinate extraction, not a relevance theorem. Vacuum, onsite,
short-bilinear, and plaquette labels acquire physical meanings only after a
fixed point, normalization condition, carrier, and observable bridge are
supplied.

One useful fixed-background tangent check is already explicit. Introduce a
declared hopping coordinate `t` in the Schur kernel,

```text
S_t=mI-t^2 A(mI+tM_II)^(-1)B.                                      (1.5)
```

With `||A||,||B||,||M_II||<=4` and `m>4`, differentiation at `t=1` gives

```text
||partial_m S||<=1+16/m^2,
||partial_t S||<=32/m+64/m^2.                                      (1.6)
```

After `D_rho`, both bilinear bounds acquire `rho^(-2)`. These are bounded
coordinate tangents, not RG eigenvalues. The eliminated-determinant response
also produces scalar loop coordinates and is not hidden inside (1.6).

## 2. Declared factor-two support chart

For each connected coarse polymer `X`, declare `H_2(X)` on the fine lattice to
contain the doubled sites `2X` and the straight fine paths representing its
coarse links. Then

```text
diam H_2(X)>=2 diam X,
|H_2(X)|>=|X|.                                                       (2.1)
```

The first inequality is exact because the two doubled endpoints realizing a
diameter pair remain in the support. The second follows from the injection
`x->2x`. This declaration fixes a common fine/coarse support convention that
the preceding notes intentionally had not selected.

Let `L Phi` be the fiber-constant lift to `H_2(X)`. The exact factorization
argument extends coefficient-wise to every even balanced retained polynomial:

```text
R(Psi+t L Phi)=R(Psi)+t Phi,
DR_Psi[L Phi]=Phi,                                                   (2.2)
```

and all mixed higher derivatives containing `L Phi` vanish. The original raw
unit ratio was measured before comparing the fine and coarse support weights.

For an anchored output term, use the doubled anchor `2z` in the input norm.
Equations (2.1)--(2.2) give

```text
exp[lambda diam X+theta|X|]
 /exp[lambda diam H_2(X)+theta|H_2(X)|]
 <=exp[-lambda diam X].                                             (2.3)
```

Every term in `(1-P_0)` has integer graph diameter at least one. Summing at the
anchor proves (0.2). Thus a finite projector is not being claimed to remove
the infinite raw-lift family; all extended members are paid by the declared
geometric weight.

## 3. Field-rescaling torsor

For `rho>0`, define

```text
(D_rho Phi)(V,bar psi',psi')
 =Phi(V,rho^(-1)bar psi',rho^(-1)psi').                             (3.1)
```

A balanced pair-degree `p` coefficient is multiplied by `rho^(-2p)`.
Substitution in (1.1) proves (0.1) exactly. Consequently `D_rho` is an
isometry from the `eta/rho` chart to the `eta` chart. If `rho>=1`, it is also
nonexpansive at fixed `eta`; for `rho<1`, no volume-uniform fixed-`eta` bound
over unbounded degree is asserted.

Combining (2.3) with the degree factor gives (0.3). The onsite mass coordinate,
for example, changes by `rho^(-2)`. Choices `rho=1` and `rho=2` therefore give
different numerical mass coordinates while representing the same polynomial
after the corresponding variable change.

No condition in the direct dependencies fixes `rho`. The convergence weight
`eta` is not a physical field normalization. The kinetic-isotropy primitive
would equate declared temporal and spatial kinetic forms only; it does not
choose their common coefficient, a taste carrier, or `rho`.

## 4. What remains for a full contraction

For a declared finite jet projector `P_J`, the desired map would be

```text
T_(J,rho)= (1-P_J)D_(2,rho)R.                                      (4.1)
```

A full theorem still requires all three of the following on one explicit ball:

```text
T_(J,rho)(B_delta) subset B_delta,
sup_(Phi in B_delta)||DT_(J,rho)(Phi)||<1,
uniform nonlinear remainder control.                               (4.2)
```

The prior complex joint source domain proves that derivatives exist and have
cluster bounds. It does not compare every non-fiber input support with its
rescaled output support, prove (4.2), or show that the output returns to the
same ball. Equation (0.2) verifies the complete raw lifted part of that test;
the non-fiber directions remain open.

A contraction proved in the present high-mass/small-coupling domain would
most naturally describe a massive ultralocal basin. It would not by itself
provide the boundary-tuned critical trajectory required for a propagating
continuum.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_declared_rg_chart_raw_lift_geometric_contraction_2026_07_12.py
```

The runner checks `P_0` idempotence, factor-two diameter/size inequalities,
the anchored `exp(-lambda)` suppression on a nontrivial interaction, the exact
field-rescaling norm identity, two inequivalent `rho` charts, coefficient-wise
joint raw factorization, a nested finite-jet family, and the source/dependency
contract. The general anchor comparison and bounded finite Gram-dual
construction are analytic statements.

## 6. No-Go Discipline N1--N8

The note contains a narrow nonselection statement—existing science does not
choose `P_J` or `rho`—but no impossibility theorem. The full N1--N8 packet is
therefore load-bearing.

### N1 — alternative-route enumeration

| Route | Status | Executed test | Outcome |
|---|---|---|---|
| Zero-diameter coefficient projection | `ATTEMPTED` | Equations (1.2)--(1.3) and runner. | Exact finite-rank chart component. |
| Finite Berezin/Peter--Weyl jets | `ATTEMPTED` | Equation (1.4) constructs bounded finite Gram-dual projectors. | Many finite choices exist; none is promoted physically. |
| Taylor/background jets | `ATTEMPTED` | Compared with Haar coefficient extraction. | Requires a declared background and is not used. |
| Factor-two support dilation | `ATTEMPTED` | Equations (2.1)--(2.3) and runner. | Extended raw lifts contract by `exp(-lambda)`. |
| Field normalization | `ATTEMPTED` | Equations (3.1) and (0.1). | Exact `rho>0` torsor; no selector found in dependencies. |
| Direct derivative from joint analyticity | `ATTEMPTED` | Section 4 separates existence from a scale-weighted operator bound. | Does not yet prove the non-fiber part of (4.2). |
| Enlarged finite jet space | `ATTEMPTED` | Runner compares nested jet sets. | Changes coordinates but does not select one. |
| Alternative norm/block kernel | `ATTEMPTED` | The direct dependencies were scanned for an autonomous support norm or selected block; neither supplies one. | Remains live for the full derivative. |

### N2 — wall-independence audit

The downstream conditions are `declared projected/rescaled chart`, `invariant
self-map neighborhood with q<1`, `physical taste-carrier identification`, and
`critical trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| declared projected/rescaled chart | invariant self-map neighborhood with q<1 | No | No | Yes |
| declared projected/rescaled chart | physical taste-carrier identification | No | No | Yes |
| declared projected/rescaled chart | critical trajectory/observable identification | No | No | Yes |
| invariant self-map neighborhood with q<1 | physical taste-carrier identification | No | No | Yes |
| invariant self-map neighborhood with q<1 | critical trajectory/observable identification | No | No | Yes |
| physical taste-carrier identification | critical trajectory/observable identification | No | No | Yes |

The derivative, ball invariance, and nonlinear remainder are components of the
second condition rather than inflated separate walls.

### N3 — hidden-condition phrase scan

| Phrase | Classification |
|---|---|
| `canonical` | No physical canonicality claim; the support and chart are declared. |
| `physical mass` | No hit. |
| `kinetic term` | Short-bilinear coordinate is not identified physically. |
| `gauge coupling` | Plaquette mode is not identified with a renormalized coupling. |
| `standard RG` | No hit. |
| `field normalization` | Explicitly a nonselected chart parameter. |
| `engineering dimension` | No imported dimension assignment. |
| `by construction` | No proof-substitute hit. |
| `we assume` | No hidden premise. |

### N4 — citation/residual matching

| Witness | Witness residual | Present use | Match? |
|---|---|---|---:|
| [Raw unit directions](WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Unit ratio before projection/rescaling | Exact factorization in the declared support chart | Yes |
| [Joint polymer norm](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | One-step membership, no self-map | Domain for coordinate projectors and analytic derivatives | Yes |
| Abstract Banach contraction theorem | Consequences after a self-map and `q<1` | Neither hypothesis is imported | No; context only |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Coordinate projector existence | Yes | Declared finite-rank charts exist. |
| Field-rescaling family | Yes | Exact norm transformation and nonselection. |
| Raw lifted extended directions | Yes | `exp(-lambda)` contraction in the declared chart. |
| Full derivative at one action | Partly | Exists; no operator norm below one. |
| Invariant neighborhood/nonlinear iteration | No | No contraction theorem. |
| Physical relevance/taste/beta function | No | No physical RG identification. |
| Critical continuum trajectory | No | No existence or impossibility claim. |

### N6 — partial-closure and primitive scan

The support dilation, finite jets, and `rho` are mathematical chart data. They
do not add an action, probability, time, taste, scale, state, or field-
normalization premise. The registered primitives neither supply nor obstruct
the full estimate. The nonselection of a chart is not an axiom contradiction.

### N7 — hostile steelman

A hostile reviewer should object that a finite projector cannot remove the
infinite raw unit-direction family. Correct; equation (2.3) pays every extended
member geometrically and removes only diameter zero.

A second should object that `exp(-lambda)` depends on a support convention.
Correct; `H_2` is declared explicitly here. The theorem does not pretend that
the earlier notes had already fixed a common autonomous fine/coarse norm.

A third should say that another `rho`, jet set, norm, or taste-faithful block
could close the full derivative. Correct; all remain live.

### N8 — cross-cycle echo

| Earlier surface | Earlier residual | Present treatment |
|---|---|---|
| Raw unit directions | Full unrescaled contraction impossible | Extended lifts gain the exact declared geometric factor; onsite terms are projected. |
| Joint polymer membership | No RG chart | Finite jets, support dilation, and field torsor are now explicit. |
| Compact deep-wedge continuum boundary | Massive interior is ultralocal | Any future contraction here is not mislabeled critical. |
| Taste-blocking bridge attempts | Imported contraction constants lacked a map/norm | No external constant is imported; the remaining inequality is displayed. |

No route is closed by relabeling, no physical beta function is claimed, and no
axiom update is requested.
