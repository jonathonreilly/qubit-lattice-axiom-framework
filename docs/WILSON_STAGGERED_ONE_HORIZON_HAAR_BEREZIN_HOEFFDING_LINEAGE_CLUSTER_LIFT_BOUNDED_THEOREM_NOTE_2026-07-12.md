# One-horizon Haar--Berezin Hoeffding lineage cluster lift

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_one_horizon_hoeffding_lineage_cluster_lift_2026_07_12.py`](../scripts/wilson_staggered_one_horizon_hoeffding_lineage_cluster_lift_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_one_horizon_hoeffding_lineage_cluster_lift_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_one_horizon_hoeffding_lineage_cluster_lift_2026_07_12.txt)

## 0. Result

The complete current bare residual factor family has an exact, regulator-
uniform, one-horizon decorated Haar--Berezin cluster lift. Forgetting the
decoration evaluates exactly to the ordinary residual action. This supplies
genuine factor/cluster provenance, but not yet a scale-to-scale tag-density or
autonomous-norm theorem.

Use the exact residual Wilson/determinant/Schur factor grammar and two-layer
cluster lemma from the
[simultaneous retained-Grassmann theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md),
including its
[syntactic-support source theorem](WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the K-retaining output conversion from the
[marked-attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the shortest-center/atom algebra from the
[Gaussian-adapted quadratic-center theorem](WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md).

For each independent hidden Haar coordinate and each retained endpoint site,
use respectively its normalized Haar expectation and the onsite three-color
Gaussian expectation at `eta=m^(-1/2)`. Put

```text
r_*=1+sqrt(2),                 C_*=r_*^2=3+2sqrt(2).                (0.1)
```

If a factor `f_a` depends on `n_a` such product coordinates, its canonical
Hoeffding components obey

```text
f_a=sum_(T subset J_a) Delta_T f_a,
sum_T r_*^|T| ||Delta_T f_a||
 <=C_*^n_a ||f_a||.                                                (0.2)
```

After extracting the full shortest quadratic center, every residual Schur
length is even and at least four. The safe coordinate counts are

```text
n_a<=4                  for a Wilson plaquette,
n_a<=r                  for an eliminated-determinant word of length r,
n_a<=r+2                for a Schur word of length r.              (0.3)
```

The last two coordinates are the two retained endpoint sites; treating all
three colors at one site as one Gaussian tensor factor avoids a spurious
color-multiplicity charge.

Let `h=4/m`, `L=Theta+2c+Lambda`,
`x_r=9 eta^2 2^(-r)m^(-(r-1))`, and `g(x)=(exp(x)-1)/x`. A safe black-box
tagged activity majorant is

```text
K_W^tag=12 [exp((3 beta/4)C_*^4)-1] exp(4L),                      (0.4)

K_I^tag=(3/2)sum_(even r>=4)
          C_*^r h^r g(3C_*^r h^r/r) exp(rL),                      (0.5)

K_S^tag=18 eta^2 sum_(even r>=4)
          C_*^(r+2) r h^(r-1) g(C_*^(r+2)x_r) exp(rL),            (0.6)

K_tag=K_W^tag+K_I^tag+K_S^tag.                                   (0.7)
```

At

```text
m=10000, beta=0, c=0.001, Theta=10^(-6), Lambda=1,
eta=0.01,                                                           (0.8)
```

the exact series give

```text
q_hop^tag=h C_* exp(L)=0.006350016695825...,
K_I^tag=2.438980005374... 10^(-9),
K_S^tag=9.942623258493... 10^(-7),
K_tag=9.967013058547... 10^(-7)<c.                                 (0.9)
```

Thus both factor-to-polymer grouping and the hard-core logarithm converge in
the decorated coefficient algebra. Their K-retaining coarse conversion gives

```text
||Gamma_hat_res||_(Lambda/2,Theta/2,eta;lineage)
 <=68 exp(Lambda/2)K_tag
 =1.11743219758... 10^(-4).                                       (0.10)
```

The residual marked-source formulas remain below one:

```text
q_centered^tag=0.082322896477...,
q_split^tag=max{exp(-1/2),q_centered^tag}=0.606530659713... .       (0.11)
```

The base defect in (0.10) is too large for the old scalar Cauchy ball
certificate at this point. More importantly, (0.11) is still a one-horizon
decorated estimate. It does not prove that lineage tags become next-scale
canonical atoms or occur with density proportional to coarse support.

## 1. Canonical factor atoms

Let `J_a` contain the declared hidden Haar coordinates in the syntactic
support of `f_a` and, for a Schur factor, its at-most-two retained endpoint
sites. For `i in J_a`, let `E_i` be the corresponding tensor-factor
expectation and `Q_i=1-E_i`. Define

```text
Delta_T=product_(i in T)Q_i product_(i in J_a minus T)E_i.          (1.1)
```

Three labels remain distinct throughout:

- `Sigma_a=J_a` is the nonminimal syntactic carrier used for overlap geometry;
- `T_a` is a genuine nonzero canonical atom subset;
- `mathcal L` is the formal nonquotient list of original factor/atom choices.

The previously declared `ell(Sigma_a)` is the support-tree span and is never a
lineage label.

The even coordinate maps commute, so

```text
sum_(T subset J_a)Delta_T=product_i(E_i+Q_i)=1.                    (1.2)
```

Every `E_i` is contractive and `||Q_i||<=2`. Therefore

```text
||Delta_T f_a||<=2^|T| ||f_a||,
sum_T r_*^|T| ||Delta_T f_a||
 <=sum_T(2r_*)^|T| ||f_a||
 =(1+2r_*)^n_a ||f_a||
 =C_*^n_a ||f_a||.                                                 (1.3)
```

This is a black-box upper bound. If a syntactic coordinate is dummy after an
`A A^(-1)V` cancellation, its `Q_i` component is exactly zero. Charging it by
`C_*` is safe overcount, not evidence of a genuine tag.

The retained-body geometry is sharper than the black-box count. A determinant
word lies entirely in the eliminated `I-I` graph. No skeleton fine link can
occur because every skeleton link has a retained `K=(2Z)^4` endpoint. A Schur
word has exactly two skeleton boundary links; all internal `I-I` links are
nonskeleton. Thus skeleton-to-future-`V` transfer is a Wilson/Schur issue, not
an eliminated-determinant issue.

If the two Schur boundary occurrences use the same skeleton coordinate, the
exact Haar split is

```text
E_A[A M A^(-1)V]=(Tr M/3)V,
Q_A[A M A^(-1)V]=[A M A^(-1)-(Tr M/3)I]V.                         (1.4)
```

For `M=I`, only the empty atom remains; for `Tr M=0`, the word is pure `Q_A`;
generically both sectors occur. Atomization must be applied to the actual
activity, not merely its primitive transporter. For example, if
`B=bar psi A psi`, the factor `exp(B)-1` has `E_A B=E_A B^2=0` but a generally
nonzero `E_A B^3`, because the `SU(3)` three-fundamental Haar integral contains
the epsilon--epsilon singlet. Determinant exponentials likewise acquire empty
atoms from invariant channels in their powers. This is why (0.4)--(0.6) use
the black-box potential-level algebra bound rather than a pure-`Q` shortcut.

An explicit residual `r=4` Schur path makes the distinction unavoidable:

```text
K0 --A--> z --H--> w --H^(-1)--> z --A^(-1)V--> K1.               (1.5)
```

Its transporter reduces to `V`. Its declared syntactic carrier contains
`{A,H}`, but its genuine current Haar atom is empty. The evaluated extended
quadratic must be extracted into a fuller center or atomized after the next
coarse-link pullback; current dummy charges cannot provide a downshift gain.

The evaluated split/Hoeffding algebra has constant one because
`r_*^2=1+2r_*` pays the local fusion `Q_iQ_i -> E_i+Q_i`. Separately, the
decorated coefficient algebra is the weighted `l1` free direct sum of atom
lineages. A lineage records the original factor label and its actual nonzero
subset `T`; multiplication concatenates lineages rather than quotienting equal
evaluated coefficients. Its tensor-projective `l1` product has constant one
directly. Evaluation performs all fusion only after summing the exact
coefficients.

## 2. Exact decorated cluster lift and evaluation

For an overlap-connected original factor set `Gamma`, choose one atom subset
`T_a subset J_a` for every `a in Gamma` and define

```text
w_hat_(Gamma,{T_a})
 =integral product_(a in Gamma) Delta_(T_a)f_a dH_(Y_Gamma).        (2.1)
```

The retained Gaussian expectations in (1.1) are formal coefficient
decompositions only; the physical current bare fiber integral in (2.1) is the
same product Haar integral as before. Finite reconstruction and linearity give

```text
sum_({T_a}) w_hat_(Gamma,{T_a})
 =integral product_(a in Gamma)f_a dH_(Y_Gamma)
 =w_Gamma.                                                         (2.2)
```

Run the second hard-core logarithm without merging decorated labels. A
decorated logarithmic cluster consists of its original hard-core cluster,
every original factor label, and every selected atom subset. Let `ev` forget
those subsets and sum their coefficients. Absolute convergence permits
Fubini/reconstruction term by term, proving

```text
ev(Gamma_hat_res)=Gamma_res.                                       (2.3)
```

Equation (2.3) is load-bearing. Ordinary nonempty Hoeffding atoms do not
survive full expectation:

```text
E_all Delta_T=0,                   T nonempty.                      (2.4)
```

Products of centered atoms can nevertheless have nonzero expectation. The
decoration that survives is therefore formal cluster lineage with the exact
evaluation map (2.3), not the ordinary Hoeffding decomposition of the coarse
output.

Normalized Haar expectations and the onsite color-scalar Gaussian expectation
intertwine coarse gauge transformations. Blocked translations and proper
cubic rotations permute coordinate slots; the compatible reflection permutes
or dualizes them. Therefore atom subsets and lineages transform in symmetry
orbits, while every evaluated coefficient in (2.3) remains jointly gauge
invariant, even-balanced, and compatible with the declared symmetries.

## 3. Tagged activity criterion

The residual factors have the coordinate counts (0.3). For the safest
potential-level bound, first apply (1.3) to each Wilson potential,
determinant potential, or Schur bilinear, then use submultiplicativity of the
constant-one atom algebra to exponentiate. This gives (0.4)--(0.6). No claim
that a general determinant or Schur activity is pure centered in every
coordinate is used.

The tagged first-layer rooted-tree recursion is the same nonnegative
majorant, with each scalar/Banach activity norm replaced by its decorated
`l1` norm. If `K_tag<c`, the actual tagged root row remains `K_tag`, while the
two copies of `c` still pay connected grouping and hard-core exclusion. This
proves regulator-uniform convergence and (0.10).

For a decorated mark whose evaluated coefficient is `Q_0`-centered, every
formal endpoint-atom projection remains Haar-centered because the coordinate
maps commute. Its mark-only first-layer coefficient therefore vanishes under
the physical product-Haar integral. The free-lineage `l1` norm is
submultiplicative, so both marked-path rerooting arguments apply with `K`
replaced by `K_tag`, proving (0.11).

At beta zero, the Wilson row vanishes. Solving `K_tag<c` with (0.4) gives the
strict nonzero interval

```text
0<=beta<1.7476907... 10^(-9)                                      (3.1)
```

at the other parameters in (0.8). This is a mathematical neighborhood, not a
phenomenological gauge-coupling region.

## 4. What the lineage does not yet do

The lift is exact for the complete current bare residual action and uniform in
the finite regulator. It is one RG horizon only.

- A nonempty current hidden tag can disappear under Haar integration; its
  formal lineage does not automatically become a next-scale cancellation tag.
- Empty-tag lineages and extended coefficients are not automatically vacuum,
  center, or raw lifted coordinates; every lineage still records its original
  factor label.
- Dummy syntactic support may be charged in (1.3), but cannot supply tag
  density or a scale-shift gain.
- The theorem does not decompose dependence on future coarse links into
  canonical future atoms or prove a tag-update cocycle.
- The correlated running Gaussian still needs its own covariance-locality and
  marked-attachment theorem.

Consequently there is no same-norm self-map, invariant ball, fixed point,
critical trajectory, or continuum result. No axiom-update stop is established.

The exact next-horizon algebraic rule is nevertheless clear: retain and
evaluate the full coarse coefficient, substitute the next skeleton chart
`V_1=A'`, `V_2=A'^(-1)W`, and only then perform the next product-Haar
Hoeffding decomposition. A coarse support is an upper carrier, not a tag:
`V_1V_2=W` can erase the next `A'` atom. Boolean lineage metadata without the
full evaluated coefficient is therefore insufficient for iteration.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_one_horizon_hoeffding_lineage_cluster_lift_2026_07_12.py
```

The runner checks the exact `r_*` identities, canonical finite-product
Hoeffding reconstruction, the black-box atom bound, dummy-coordinate
annihilation, nonzero products of centered atoms, decorated factor-collection
evaluation, the tagged activity series and beta interval, marked constants,
and the source/dependency contract. The two infinite cluster recursions use
the displayed analytic KP majorant.

## 6. No-Go Discipline N1--N8

The result is constructive. The boundary packet prevents formal provenance
from being mislabeled as autonomy.

### N1 — alternative-route enumeration

| Route | Status | Executed result |
|---|---|---|
| Canonical product-coordinate Hoeffding atoms | `ATTEMPTED` | Equations (1.1)--(1.3) instantiate the actual factor grammar. |
| Black-box `C_*` charging | `ATTEMPTED` | Equations (0.4)--(0.9) give a strict tagged KP row. |
| Direct survival of nonempty atoms | `ATTEMPTED` | Equation (2.4) shows individual nonempty atoms are annihilated. |
| Decorated lineage lift | `ATTEMPTED` | Equations (2.1)--(2.3) give exact evaluation equality. |
| Syntactic supports as genuine tags | `ATTEMPTED` | The dummy and `r=4` cancellation witnesses have zero `Q_i` components despite nonempty carriers. |

Essential-support atomization, future-coordinate tags, tag-update cocycles,
correlated-Gaussian clusters, Peter--Weyl smoothing, and taste-faithful blocks
remain live and are not labeled attempted.

### N2 — wall-independence audit

The four conditions are `future-tag update/spatial handoff`, `correlated
Gaussian attachment/running gap`, `physical taste/chart identification`, and
`critical trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| future-tag update | correlated Gaussian attachment | No | No | Yes |
| future-tag update | physical taste/chart | No | No | Yes |
| future-tag update | critical trajectory/observable | No | No | Yes |
| correlated Gaussian attachment | physical taste/chart | No | No | Yes |
| correlated Gaussian attachment | critical trajectory/observable | No | No | Yes |
| physical taste/chart | critical trajectory/observable | No | No | Yes |

### N3 — hidden-condition phrase scan

| Phrase | Classification |
|---|---|
| `canonical atoms` | Canonical only relative to the declared product reference. |
| `lineage` | Formal nonquotient metadata with evaluation (2.3). |
| `actual residual action` | The current bare one-step residual only. |
| `uniform` | Regulator-uniform at one horizon, not horizon-uniform. |
| `support` | Syntactic support is an overcount and never promoted to genuine tag density. |
| `same norm` | Explicitly absent. |
| `autonomous` | Explicitly absent. |
| `by construction` | No proof-substitute use. |

### N4 — citation/residual matching

| Dependency | Exact use | Match? |
|---|---|---:|
| [Retained-Grassmann theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Residual factors, Banach coefficient norm, incidence rows | Yes |
| [Syntactic-support source theorem](WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Two-layer lemma, dummy-support and coarse conversion | Yes |
| [Marked attachment](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | K-retaining output and optional marked constants | Yes |
| [Gaussian-adapted center](WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md) | `r=2`/odd extraction and product-coordinate atom algebra | Yes |

### N5 — rhetoric and resolution audit

The factor grammar is complete for the current bare one-step action after
shortest-center extraction. The decorated convergence is uniform in regulator
size. Neither statement covers a ball of generated actions, multiple RG
horizons, correlated covariance integration, or physical continuum scaling.

### N6 — partial-closure and primitive scan

Hoeffding projections, direct-sum lineage, and cluster evaluation are
mathematical bookkeeping on declared regulator variables. They neither add
nor require a physical action, probability, time, scale, taste, or state
primitive. The missing tag-update/covariance theorem is not an axiom issue.

### N7 — hostile steelman

A hostile reviewer should object that formal tags can persist even when their
evaluated coefficient loses all dependence on the tagged coordinate. Correct;
that is why no shift contraction follows. Another should demand future coarse-
coordinate atomization and correlated-covariance locality before iteration.
Correct; both are the next live routes.

### N8 — cross-cycle echo

Earlier syntactic supports were safe for convergence but unsafe as genuine
minimal supports. This theorem preserves that distinction: they bound the
black-box atom cost, while only nonzero canonical components enter lineage.
The resulting one-horizon lift is progress toward, not a relabeling of, an
autonomous RG norm.

**No-Go Discipline status: PASS.**
