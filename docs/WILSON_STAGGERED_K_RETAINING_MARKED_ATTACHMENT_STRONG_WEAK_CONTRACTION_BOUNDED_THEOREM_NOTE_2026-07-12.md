# K-retaining marked attachment and one-step strong-to-weak contraction

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_k_retaining_marked_attachment_strong_weak_contraction_2026_07_12.py`](../scripts/wilson_staggered_k_retaining_marked_attachment_strong_weak_contraction_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_k_retaining_marked_attachment_strong_weak_contraction_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_k_retaining_marked_attachment_strong_weak_contraction_2026_07_12.txt)

## 0. Result

The exact constrained-fiber derivative now has an explicit localized
forced-attachment bound. In an ultra-deep massive region it is a strict
one-step contraction from a strong split source norm to the weak coarse
interaction norm.

Use the factor activities and simultaneous even-balanced source algebra from
the
[retained-Grassmann joint-polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md)
and the exact product-centered derivative split from the
[split-derivative certificate boundary](WILSON_STAGGERED_SPLIT_DERIVATIVE_AND_UNLOCALIZED_CAUCHY_CERTIFICATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md).
Write

```text
v_a=||f_a||_eta exp[(Theta+2c)|S_a|+Lambda ell(S_a)],
K=sup_h sum_(a:h in S_a) v_a<c.                                    (0.1)
```

The earlier rooted-tree proof replaced the actual row `K` by its allowance
`c`. Retaining `K` gives the sharper hidden connected-action row

```text
||Gamma_base||_hidden<=K                                            (0.2)
```

at weights `(Theta,Lambda)`. After the established hidden-to-coarse support
conversion, the non-onsite base defect obeys

```text
B_weak<=68 exp(Lambda/2)K.                                         (0.3)
```

Let `E_0` be product hidden-Haar expectation and let

```text
C_0=L E_0,                  Q_0=1-C_0.                              (0.4)
```

For a centered mark `F^o=Q_0F`, the mark-alone activity vanishes. Every
surviving connected response must contain a base factor. Put

```text
s=c-K,
d(s)=sup_(n integer>=1) n exp(-s n),
tau=K d(s),
a_0(K,c)=sup_(n integer>=1) exp(-cn)[exp(Kn)-1].                    (0.5)
```

If `tau<1`, unique marked-path rerooting through both layers gives the full
anchored constant

```text
A_att(K,c)
 =[a_0(K,c)+tau/(1-tau)]/(1-tau).                                  (0.6)
```

Consequently

```text
||(E_Phi-E_0)F^o||_(Lambda/2,Theta/2,eta)
 <=68 exp(Lambda/2) A_att(K,c)||F^o||_mark.                         (0.7)
```

This is the scale-localized improvement missing from the absolute Cauchy
certificate. It is `O(K)` as `K` tends to zero with fixed `c`.

For the raw lifted part use the factor-two chart at
`lambda=Lambda/2,theta=Theta/2,rho=1` and remove diameter zero with `P_0`.
Define the one-step strong split norm

```text
||F||_strong
 =||C_0F||_(Lambda/2,Theta/2,eta; fine lift)
  +||Q_0F||_mark(Theta+2c,Lambda,eta).                              (0.8)
```

For

```text
T=(1-P_0)D_(2,1)R,                                                  (0.8a)
```

the projected/rescaled derivative from (0.8) to the weak coarse norm obeys

```text
q_sw<=max{exp(-Lambda/2),
          68 exp(Lambda/2)A_att(K,c)}.                              (0.9)
```

At

```text
m=10000, beta=0, c=0.001, Theta=10^(-6),
Lambda=1, eta=10^(-10),                                             (0.10)
```

the exact series give

```text
K=2.113419745763... 10^(-12),
tau=7.774836766753... 10^(-10),
A_att=1.554967354342... 10^(-9),
68 exp(Lambda/2)A_att=1.743321271597... 10^(-7),
q_sw=exp(-1/2)=0.606530659713...<1,
B_weak<=2.36941926036... 10^(-10).                                 (0.11)
```

Thus the non-fiber derivative problem has a strict positive one-step answer in
one declared strong-to-weak chart. This is not an autonomous invariant ball:
the present theorem does not prove that the weak coarse output returns to the
same strong split norm at the next dyadic level. It also does not control a
running relevant center or prove a same-norm Hessian bound.

No physical fixed point, taste carrier, critical trajectory, or propagating
continuum follows from this ultra-massive point. No axiom-update stop is
established.

## 1. Retaining the actual activity row

The two-layer proof starts with local factors `f_a` in the commutative
even-balanced coefficient algebra. Define

```text
u_a=||f_a||_eta
    exp[(Theta+c)|S_a|+Lambda ell(S_a)].                             (1.1)
```

For a finite truncation, the rooted first-layer tree recursion is

```text
T_a^(0)=u_a,
T_a^(r+1)=u_a exp[sum_(b:S_b intersects S_a)T_b^(r)].               (1.2)
```

If

```text
T_b^(r)<=||f_b||_eta
          exp[(Theta+2c)|S_b|+Lambda ell(S_b)],                     (1.3)
```

the overlap sum is bounded by `K|S_a|`, because one chooses an intersection
coordinate in `S_a` and applies (0.1). Hence

```text
T_a^(r+1)
 <=u_a exp[K|S_a|]
 <=||f_a||_eta exp[(Theta+2c)|S_a|+Lambda ell(S_a)].                (1.4)
```

Rooting at a hidden coordinate and summing (1.4) gives the first-layer row

```text
sup_h sum_(Gamma:h in Y_Gamma)
 ||w_Gamma||_eta
 exp[(Theta+c)|Y_Gamma|+Lambda ell(Y_Gamma)]
 <=K.                                                               (1.5)
```

The hard-core Kotecky--Preiss exclusion allowance remains `c|Y|`, because
`K<c`. Rooting the logarithmic cluster at a polymer and applying the standard
exclusion bound does not replace its pinned root sum by `c`; summing roots
containing `h` in (1.5) leaves `K`. Monotone convergence proves (0.2).

The prior coarse-shadow map has multiplicity 68 and obeys
`diam X(Y)<=ell(Y)+1`, `|X(Y)|<=2|Y|`. At weak weights
`(Lambda/2,Theta/2)`, it converts (0.2) to (0.3). The hidden-independent onsite
mass is separately extracted and is not included in `B_weak`.

## 2. Centered mark and first-layer rerooting

Let a mark `O_T` be normalized in the strong marked weight

```text
m_T=||O_T||_eta
    exp[(Theta+2c)|T|+Lambda ell(T)].                               (2.1)
```

For `O_T=Q_0O_T`, product Haar gives `integral O_T=0`. In the first factor-to-
polymer layer, the component containing only the mark therefore vanishes.
Every surviving marked component contains at least one base factor connected
to `T` by support overlap.

### 2.1 Output anchor inside the mark

Off-path base subtrees exponentiate to at most `exp(K|T|)`. Removing the empty
base collection leaves `exp(K|T|)-1`. The first `c` reserve in (2.1) gives

```text
exp(-c|T|)[exp(K|T|)-1]<=a_0(K,c).                                 (2.2)
```

### 2.2 Output anchor in a base descendant

Use the unique path in a rooted spanning tree from the mark to the factor
containing the output anchor. At a distinguished path vertex of support size
`n`, there are at most `n` choices of the overlap coordinate leading to the
next vertex. Off-path children use the actual row `K` and cost `exp(Kn)`.
The unused support reserve is `s=c-K`, so one path step is bounded by

```text
K n exp(-s n)<=K d(s)=tau.                                         (2.3)
```

Summing positive path lengths gives

```text
sum_(j>=1)tau^j=tau/(1-tau),                                       (2.4)
```

provided `tau<1`. Combining (2.2)--(2.4), the anchored marked-polymer row at
intermediate weights `(Theta+c,Lambda)` is bounded by

```text
[a_0+tau/(1-tau)] ||O||_mark.                                      (2.5)
```

Dummy syntactic supports and fiber-constant base factors may enlarge `K`, but
cannot make this upper bound too small. Their exact contributions cancel in
the normalized response; no cancellation is needed for the safe estimate.

## 3. Second layer and coarse conversion

If the output anchor lies in the marked first-layer polymer, (2.5) applies.
Otherwise reroot the hard-core cluster along its unique marked path. The
base-polymer row is again at most `K`; the second `c` reserve gives the same
path step `tau`. Summing zero or more second-layer steps gives

```text
sum_(j>=0)tau^j=1/(1-tau).                                         (3.1)
```

Multiplying (2.5) by (3.1) proves (0.6). The `Lambda` tree-span weight remains
available throughout. The established coarse-shadow conversion pays output
anchors, exposed link endpoints, balanced Grassmann coefficients, and the
factor 68, proving (0.7).

The integer suprema have continuous maximizers

```text
n_d^*=1/(c-K),
n_a^*=-log(1-K/c)/K,                                                (3.2)
```

so each exact integer supremum is attained at one of the two adjacent positive
integers. Useful envelopes are

```text
d(s)<=1/(e s),
a_0<=r(1-r)^((1-r)/r),       r=K/c.                                (3.3)
```

The displayed witness uses the exact integer suprema.

## 4. Strong-to-weak derivative

For every perturbation in the split class,

```text
F=C_0F+Q_0F,
E_Phi[C_0F]=E_0[C_0F],
E_0[Q_0F]=0.                                                        (4.1)
```

The lifted part of the projected/rescaled derivative gains the exact raw
factor `exp(-Lambda/2)` after `P_0`, while the centered part is bounded by
(0.7). Triangle inequality with the `l1` split norm (0.8) gives (0.9).

The centered marked norm is strong: it spends the full
`(Theta+2c,Lambda)` activity weights. The codomain is weak: it is the coarse
`(Theta/2,Lambda/2,eta)` interaction norm. Equation (0.9) is a real one-step
operator bound, but not an endomorphism bound on one Banach ball.

A nonquotient direct-sum algebra can retain centered covariances. If `L` is a
unital algebra section and `E_0` a bimodule conditional expectation, then

```text
N(F)=||E_0F||_coarse+||(1-L E_0)F||_fine                            (4.2)
```

obeys `N(FG)<=3N(F)N(G)` under the natural product and module bounds, so `3N`
is submultiplicative. This does not prove that the weak output of (0.9) has a
next-level `3N` bound small enough for contraction. A block-saturated local
section or a genuinely multiscale norm is still needed.

## 5. Nonlinear feasibility diagnostic

The ultra-deep point has source radius

```text
r_src=log(1+c-K)=0.000999500331... .                                (5.1)
```

If a future same-norm handoff preserves (0.3) and (0.9), a two-mark Cauchy
envelope on a ball of radius `delta<r_src` is

```text
M_delta=2[68 exp(Lambda/2)c]/(r_src-delta)^2.                       (5.2)
```

At `delta=10^(-8)`, the runner finds

```text
B_weak+q_sw delta+(M_delta/2)delta^2
 =6.313473008... 10^(-9)<delta.                                    (5.3)
```

This proves scalar parameter feasibility only. It is not an autonomous
invariant ball because the same-norm handoff and running-center control are not
supplied.

## 6. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_k_retaining_marked_attachment_strong_weak_contraction_2026_07_12.py
```

The runner independently evaluates the activity series, verifies the `c` to
`K` base-bound sharpening at all three prior strict points, evaluates the exact
integer suprema and `tau`, checks both path resolvents against (0.6), verifies
`q_sw<1` and the weak base defect, and records the conditional scalar ball
diagnostic. The infinite rooted-tree rerooting and thermodynamic limit are
analytic statements.

## 7. No-Go Discipline N1--N8

The theorem has a named strong/weak autonomy boundary. These checks prevent
that boundary from becoming a same-norm or physical no-go.

### N1 — alternative-route enumeration

| Route | Status | Executed result |
|---|---|---|
| Retain the actual base row `K` | `ATTEMPTED` | Equations (1.1)--(1.5) sharpen the connected action from `c` to `K`. |
| Mark-rooted forced attachment | `ATTEMPTED` | Centering removes the empty base collection and gives `a_0`. |
| First-layer output-anchor rerooting | `ATTEMPTED` | The unique marked path gives `tau/(1-tau)`. |
| Second hard-core rerooting | `ATTEMPTED` | A second unique path gives the final `1/(1-tau)`. |
| Strong split source norm | `ATTEMPTED` | Raw lifts and centered marks give the strict one-step bound (0.9). |
| Nonquotient direct-sum algebra | `ATTEMPTED` | Equation (4.2) retains centered products with algebra constant three, but no small next-level handoff. |
| Absolute Cauchy plus raw geometry | `ATTEMPTED` | Reapplying the direct dependency's exact inequality leaves the unlocalized certificate above 68. |
| Present Peter--Weyl-unweighted coefficient norm | `ATTEMPTED` | Fixed-support characters receive no representation-index damping; a weighted refinement remains live. |

No alternative block, multistep, or representation-weighted route is declared
closed.

### N2 — wall-independence audit

The collapsed downstream conditions are `autonomous localized-operator
package`, `center-defect/invariant self-map`, `physical taste/chart
identification`, and `critical trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| autonomous localized-operator package | center-defect/invariant self-map | No | No | Yes |
| autonomous localized-operator package | physical taste/chart identification | No | No | Yes |
| autonomous localized-operator package | critical trajectory/observable identification | No | No | Yes |
| center-defect/invariant self-map | physical taste/chart identification | No | No | Yes |
| center-defect/invariant self-map | critical trajectory/observable identification | No | No | Yes |
| physical taste/chart identification | critical trajectory/observable identification | No | No | Yes |

The local section, marked derivative, and same-norm Hessian are components of
the first condition rather than inflated independent walls.

### N3 — hidden-condition phrase scan

| Phrase or premise | Classification |
|---|---|
| `autonomous` | Explicitly not proved; strong domain and weak codomain differ. |
| `local section` | The algebra section exists; its scale-uniform next-level norm bound remains open. |
| `forced attachment` | Proved by subtraction and the unique marked-path calculation, not syntax alone. |
| `base activity` | The safe total `K` includes dummy-supported terms; no hidden cancellation is used. |
| `same norm` | No same-norm contraction is claimed. |
| `background` | `Phi` is an explicit controlled base action. |
| `canonical` | Only the declared dyadic relabeling is used; no physical chart selector. |
| `relevant` | `P_0` is a declared diameter-zero extraction, not a physical scaling classification. |
| `by construction` | No proof-substitute use. |
| `uniform` | Restricted to the displayed marked source/interaction norms. |
| `standard RG` | No imported model theorem. |
| `standard exclusion bound` | The linked joint-polymer dependency proves the hard-core bound; Section 1 reruns its root sum while retaining `K`. |
| `natural product and module bounds` | Explicit hypotheses only for the auxiliary direct-sum observation (4.2); they do not support `q_sw` or the scalar feasibility diagnostic. |

### N4 — citation/residual matching

| Witness | Witness residual | Present use | Match? |
|---|---|---|---:|
| [Retained-Grassmann joint-polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Actual factor row and two-layer support conversion | `K`-retaining and marked rerooting inputs | Yes |
| [Split-derivative certificate boundary](WILSON_STAGGERED_SPLIT_DERIVATIVE_AND_UNLOCALIZED_CAUCHY_CERTIFICATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Product-centered split and failed absolute certificate | Decomposition (4.1) and target comparison | Yes |
| Raw local Hessian theorem | Fixed local bosonic second response | Same-norm joint Hessian | No; not used. |
| Compact-interior ultralocal theorem | Physical scaling interpretation | Mathematical contraction | No; context only. |
| Banach fixed-point theorem | Consequences after a self-map | Present strong-to-weak map | No; no fixed-point conclusion. |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Finite rooted factor/polymer systems | Yes | Exact `K` and marked-path majorants. |
| Regulator-uniform anchored marked source class | Yes | Bound (0.7). |
| One controlled base action | Yes | Strong-to-weak derivative `q_sw<1`. |
| One weak coarse output | Yes | Base defect (0.3). |
| Same strong norm at the next level | No | No autonomous self-map. |
| Uniform nonlinear ball and running center | No | Equation (5.3) is conditional feasibility only. |
| Physical taste carrier | No | No carrier identification. |
| Critical continuum trajectory | No | No existence or impossibility claim. |

### N6 — partial-closure and primitive scan

The factor row, marked-tree resolvent, split norm, and dyadic support chart are
constructive mathematics. A block-saturated local section, multiresolution
norm, or same-norm Hessian would be further model theorems, not new axioms.
The registered scale-reference, kinetic-isotropy, and realized-state
primitives neither grant nor obstruct them. No primitive nonsupply is treated
as a wall.

### N7 — hostile steelman

A hostile reviewer should say that the weak output may admit a block-saturated
decomposition whose next-level split norm costs only a fixed constant.
Increasing `Lambda` in a deeper massive wedge could then beat that constant,
while the attachment term remains `O(K)`. Correct. The same-norm route is
serious and untested here. A representation-weighted norm, multistep estimate,
or taste-faithful block can also improve the spectrum. The theorem therefore
stops at a one-step strong-to-weak contraction.

### N8 — cross-cycle echo

| Earlier surface | Earlier residual | Later mechanism | Present lesson |
|---|---|---|---|
| Raw unit directions | Unrescaled unit ratio | Declared geometric chart | Coordinate walls can be retired constructively. |
| Pair Hessian only | No all-order source domain | Two-layer marked sources | Local response can be promoted with explicit combinatorics. |
| No simultaneous joint norm | Grassmann degrees treated separately | Banach-valued polymer row | Algebra design can close a genuine gap. |
| Unlocalized derivative certificate | Absolute bound above 68 | `K`-retaining marked-path resolvent | The localized derivative now contracts strong-to-weak. |

The remaining autonomy question is another constructive norm/self-map target.
It is not an axiom contradiction and not a physical continuum no-go.

**No-Go Discipline status: PASS.**
