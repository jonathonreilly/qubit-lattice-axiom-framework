# Split constrained-fiber derivative and unlocalized Cauchy-certificate boundary

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_split_derivative_cauchy_certificate_boundary_2026_07_12.py`](../scripts/wilson_staggered_split_derivative_cauchy_certificate_boundary_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_split_derivative_cauchy_certificate_boundary_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_split_derivative_cauchy_certificate_boundary_2026_07_12.txt)

## 0. Result

On every finite regulator, the exact constrained-fiber map has an algebraic
tangent split at each controlled base action. The simultaneous joint-polymer theorem makes its fixed-order
derivatives uniform on the controlled finite-local-source class. Neither that
restricted split nor the existing unlocalized Cauchy estimate is the missing
full interaction-ball theorem.

Use the common even-balanced Banach source domain from the
[simultaneous retained-Grassmann polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md)
and the lift/rescaling identities from the
[declared factor-two RG chart](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md).
For a controlled base action `Phi`, put

```text
Z_Phi=integral_fiber exp(-Phi),
E_Phi[F]=Z_Phi^(-1) integral_fiber exp(-Phi)F.                       (0.1)
```

Products and the inverse in (0.1) are taken in the commutative even-balanced
Grassmann Banach algebra. Direct differentiation gives

```text
D R_Phi[F]=E_Phi[F],
D^n R_Phi[F_1,...,F_n]=(-1)^(n+1) kappa_n^Phi(F_1,...,F_n).          (0.2)
```

In particular, `D^2 R=-Cov_Phi`. Since the exact fiber-constant lift obeys
`E_Phi L=I`, the base-action-dependent operators

```text
C_Phi=L E_Phi,                 Q_Phi=1-C_Phi                        (0.3)
```

are complementary projections and

```text
F=L(E_Phi F)+Q_Phi F,          E_Phi Q_Phi=0.                       (0.4)
```

Thus, algebraically at finite volume and uniformly for each fixed order on the
controlled finite-local-source class, the derivative is split onto the
corresponding local coarse response class and its conditionally centered
summand is killed exactly at first order. As the allowed local coarse sources
vary, the range of `C_Phi` contains an infinite-dimensional family of lifted
coarse interactions, and `C_Phi` depends on the base action. It is not a
finite relevant/marginal projector or a physical coordinate selection. A
bounded extension to the entire anchored interaction space is not asserted.

Conditional centering is also not a nonlinear invariant sector. Already for
one product-Haar surrogate coordinate `h=+/-1` and a coarse function `f`,

```text
E_0[h Lf]=0,                 D^2R_0[hLf,hLf]=-f^2.                  (0.5)
```

The centered kernel is not an ideal: products of centered elements can have a
nonzero conditional mean.

The second result is an exact limitation of the presently available
**certificate**, not of the dynamics. Write the parameters of the simultaneous
polymer theorem as `Lambda,Theta,c`, let

```text
epsilon=c-K_joint>0,          r_src=log(1+epsilon),
A=68 exp(Lambda/2)c.                                               (0.6)
```

For one normalized local source in the theorem's weighted activity class,
Cauchy's estimate gives

```text
sup_(F in S_loc, ||F||_src<=1)
 ||D R_Phi[F]||_(Lambda/2,Theta/2,eta)
 <=Q_C=A/r_src
      =68 exp(Lambda/2)c/log(1+epsilon),                            (0.7)
```

where `S_loc` is the finite-local-source class controlled by the simultaneous
joint-polymer theorem. This is
a normalized-source Cauchy certificate, not a completed operator norm on the
full interaction-space completion.

The output norm is controlled only at chart weights
`lambda=Lambda/2,theta=Theta/2`. Therefore the uniform unit-diameter raw-lift
gain in the composed joint-polymer/RG-chart certificate is `exp(-Lambda/2)`, not
`exp(-Lambda)`. Even if that raw-lift gain is granted to every source response,

```text
exp(-Lambda/2)Q_C
 =68c/log(1+epsilon)>68,                                            (0.8)
```

because `0<epsilon<c` and `log(1+epsilon)<epsilon`. Hence plain source
analyticity plus the raw-lift support factor cannot certify a full derivative
constant below one anywhere in the declared KP region. Equation (0.8) is not a
dynamical noncontraction theorem: it says the absolute, unlocalized estimate
has discarded the small forced-attachment factor needed for the proof.

Finally, any finite-rank projector on the present coefficient space leaves a
nonzero vector in the fixed-support coarse-plaquette character span. Scalar
gauge-invariant Peter--Weyl characters make that slice infinite-dimensional.
At `rho=1`, the exact raw identity then gives, for the declared minimal
plaquette lift,

```text
||(1-P_J)D_(2,1)R[Lf]||/||Lf||
 =exp[-2lambda-4theta].                                             (0.9)
```

This is a positive lower floor strictly below one, not a noncontraction
result. It proves only that finite projection in the present coefficient
space does not make this declared fixed-support tail vanish. A representation-
weighted norm, another support chart, actual fiber smoothing, or a localized
marked-cluster estimate remains live.

The next constructive target is a scale-localized split

```text
E_Phi=E_0+(E_Phi-E_0),                                              (0.10)
```

where `L E_0` has a bounded local section compatible with the shadow norm and
every centered contribution to `E_Phi-E_0` is forced to attach to at least one
base activity. Only after that estimate supplies `q<1` can a base offset `B`
and Hessian bound `M` close

```text
B+q delta+(M/2)delta^2<=delta.                                      (0.11)
```

No axiom-update stop is established.

## 1. Banach-valued derivative and cumulants

On a finite regulator, the positive body of `Z_Phi` is nonzero throughout the
simultaneous joint-polymer source domain. The inverse in (0.1) therefore exists in the finite
even Grassmann algebra. For commuting perturbations `F_i`, differentiation of

```text
R(Phi+tF)=-log integral exp[-Phi-tF]                                (1.1)
```

is ordinary commutative Banach-algebra differentiation. The first two orders
are

```text
D R_Phi[F]=E_Phi[F],
D^2 R_Phi[F,G]
 =-[E_Phi(FG)-E_Phi(F)E_Phi(G)].                                   (1.2)
```

The moment--cumulant recursion gives (0.2) at every order. The simultaneous
joint-polymer theorem's common
Reinhardt domain and uniform marked-cluster convergence make each fixed-order
identity regulator-, hidden-boundary-, and coarse-`V`-uniform for the local
source class proved there. This statement does not silently promote finite
local-source analyticity to a full Fréchet bound on every interaction-ball
direction.

For every coarse interaction `f`, fiber constancy gives `E_Phi[Lf]=f`.
Consequently

```text
C_Phi^2=L E_Phi L E_Phi=L E_Phi=C_Phi,
Q_Phi^2=Q_Phi,
E_Phi Q_Phi=0.                                                       (1.3)
```

At finite volume these are exact algebraic identities. In the uniform local
source class, boundedness of `E_Phi` follows from the marked expansion. A
volume-uniform extension to the whole anchored interaction space is exactly
part of the localized-operator problem, rather than an assumption here.

## 2. Why the centered split is not the RG relevant split

The range of `C_Phi` contains every local coarse gauge function and every
allowed even-balanced coarse Grassmann polynomial. It is therefore
infinite-dimensional even before supports are allowed to grow. It also changes
with `Phi`.

Equation (0.5) shows the nonlinear problem directly. With product measure on
`h=+/-1`, `E_0 h=0` but `E_0 h^2=1`. The first centered insertion vanishes,
while its connected second response is nonzero. If `f` is chosen in the
high-character plaquette tail, `f^2` need not lie in any fixed finite jet.
Thus quotienting by `ker E_0` would erase load-bearing nonlinear covariance.

The quotient norm

```text
||f||_quot=inf_(E_0F=f)||F||                                       (2.1)
```

makes `E_0` contractive by definition, but supplies neither a local bounded
section nor geometric lift control. Conversely the shadow norm
`||f||_sh=||Lf||` gives the desired support comparison only if

```text
||L E_0F||<=C_sec||F||                                              (2.2)
```

with a scale-uniform local constant. The current notes do not prove (2.2).
Moreover `ker E_0` is not an ideal, so the quotient is not automatically a
submultiplicative action algebra for exponentials and polymers.

## 3. Consistent Cauchy and chart weights

Let a normalized local source `F` have weighted source incidence at most one.
Convexity gives

```text
sum_marked [exp(|z| ||F_a||)-1] weight_a
 <=exp(|z|)-1.                                                       (3.1)
```

It fits inside the strict activity margin whenever
`|z|<r_src=log(1+epsilon)`. Across this disk, the non-onsite connected output
has the simultaneous joint-polymer bound `A=68 exp(Lambda/2)c`. Cauchy's integral formula proves
(0.7); the onsite mass is independent of this marked source and is not inserted
into `A`.

At the three displayed joint-polymer points, the unlocalized first-derivative
constants are approximately

| `m` | `Q_C` | `exp(-Lambda/2)Q_C` |
|---:|---:|---:|
| 12 | 276.96 | 276.82 |
| 16 | 631.02 | 630.71 |
| 20 | 329.86 | 329.69 |

The exact inequality (0.8), rather than these examples, proves that parameter
optimization cannot repair this particular black-box certificate. Increasing
`Lambda` increases `A` by precisely the factor canceled by the weakest
diameter-one lift gain in the composed chart.

This does not rule out:

- a forced-base-attachment estimate proportional to `K_joint/c`;
- representation-index smoothing of fixed-support Peter--Weyl tails;
- a block-shadow norm with a proved bounded local section;
- a different gauge-covariant/taste-faithful block;
- a multistep estimate.

## 4. Finite-jet tail and exact raw floor

Let `X` be the four vertices of one coarse plaquette. Its graph diameter is
two. The minimal declared straight factor-two boundary lift has eight vertices,
diameter four, and the same scalar Grassmann degree `p=0`. The coefficient norm
therefore gives the exact weight ratio

```text
exp[lambda*2+theta*4]/exp[lambda*4+theta*8]
 =exp[-2lambda-4theta].                                              (4.1)
```

The scalar class functions on the plaquette holonomy contain the characters
of infinitely many inequivalent `SU(3)` representations. Restrict a finite-
rank `P_J` to their span. Its kernel is nonzero; choose `f` there. The exact
identity `R(Phi+tLf)=R(Phi)+tf` and `P_Jf=0` prove (0.9).

At the displayed joint-polymer points the composed chart has
`lambda=theta=0.0005`, so the floor is `exp(-0.003)=0.997004...`.
Using another declared chart with `lambda=theta=0.001` gives
`exp(-0.006)=0.994017...`. Both are below one. The result forbids neither a
one-step contraction nor a spectral smoothing theorem.

## 5. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_split_derivative_cauchy_certificate_boundary_2026_07_12.py
```

The runner checks Banach-valued expectation/covariance algebra in a nontrivial
dual-number fiber, `E L=1`, projection idempotence, exact annihilation of the
centered linear component, the nonlinear centered-square witness, the three
joint-polymer Cauchy constants with consistent half-weights, a representative finite
plaquette-character jet tail, and the source/dependency contract. The general
cumulant recursion, infinite-dimensional kernel argument, and uniform marked-
cluster statements are analytic.

## 6. No-Go Discipline N1--N8

The certificate boundary and finite-jet tail are negative-shaped statements.
They are deliberately restricted to the estimates actually tested.

### N1 — alternative-route enumeration

| Route | Status | Result |
|---|---|---|
| Unlocalized Cauchy plus raw geometry | `ATTEMPTED` | Equation (0.8) proves this certificate stays above 68. |
| Exact conditional-centering split | `ATTEMPTED` | Equations (0.3)--(0.5) kill the linear kernel but expose a nonzero Hessian. |
| Larger finite local jets | `ATTEMPTED` | Fixed-support plaquette characters leave an infinite tail and the exact floor (0.9). |
| Product-fiber quotient norm | `ATTEMPTED` | Makes `E_0` contractive tautologically but loses a proved local section and nonlinear algebra. |
| Block-shadow/local-section norm | `UNTESTED / LIVE` | No local-section estimate is proved; (2.2) names the live obligation. |
| Forced-attachment marked clusters | `UNTESTED / LIVE` | The missing subtraction is identified in (0.10), but no marked-cluster estimate is executed here. |
| Peter--Weyl/Casimir-weighted smoothing | `UNTESTED / LIVE` | The present norm has no representation-index weight and no weighted replacement is constructed. |

The narrow result closes only the first black-box certificate and the claim
that finite projection alone deletes every tail.

### N2 — wall-independence audit

The downstream conditions are `localized full derivative q<1`, `one invariant
ball including its center defect`, `physical taste/chart identification`, and
`critical trajectory/observable identification`.

| Left | Right | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| localized full derivative | invariant ball | No | No | Yes |
| localized full derivative | physical taste/chart | No | No | Yes |
| localized full derivative | critical trajectory/observable | No | No | Yes |
| invariant ball | physical taste/chart | No | No | Yes |
| invariant ball | critical trajectory/observable | No | No | Yes |
| physical taste/chart | critical trajectory/observable | No | No | Yes |

Once a derivative bound is uniform on a convex ball, its nonlinear Lipschitz
remainder is part of that bound rather than a separately inflated wall.

### N3 — hidden-condition phrase scan

| Phrase or premise | Classification |
|---|---|
| `finite local sector` | Not assumed finite-dimensional; the plaquette gauge slice is explicitly infinite-dimensional. |
| `by construction` | No projector idempotence is promoted to contraction. |
| `background` | `Phi` is an explicit base action and `C_Phi` is explicitly base dependent. |
| `standard RG` | No imported relevance or scaling classification. |
| `field normalization` | `rho` remains a declared chart parameter. |
| uniform source domain | Kept distinct from uniformity on an action-space ball. |
| positive conditional expectation | Used only for the scalar/product illustration; the joint formula is Banach-algebra valued. |

### N4 — citation/residual matching

| Witness | Witness residual | Present use | Match? |
|---|---|---|---:|
| [Simultaneous polymer theorem](WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Joint source domain and half-weight output norm | Derivative existence and Cauchy constant | Yes |
| [Declared RG chart](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Exact raw lifts and declared support/field rescaling | Split identity and raw geometric comparison | Yes |
| Earlier raw norm-one boundary | Unprojected, unrescaled lift | Full projected derivative | No; not used as a no-go witness. |
| Compact-interior continuum boundary | Physical critical scaling | Mathematical derivative estimate | No; context only. |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Finite-volume Banach derivative/cumulants | Yes | Exact identities (0.2). |
| Uniform local marked-source class | Yes | Cauchy certificate (0.7). |
| Arbitrary full interaction ball | No | No Fréchet contraction claim. |
| One fixed plaquette character slice | Yes | Finite-jet tail and floor (0.9). |
| Every non-fiber mode | No | No actual noncontraction claim. |
| Nonlinear centered kernel | Yes, counterexample | It is not invariant in general. |
| Autonomous invariant neighborhood | No | Equation (0.11) is the next test. |
| Critical continuum | No | No existence or impossibility claim. |

### N6 — partial-closure and primitive scan

The split, source norm, support weights, and finite jets are mathematical chart
data. A better local section, marked-tree estimate, representation-weighted
norm, or alternative block is an ordinary constructive route. The registered
scale-reference, kinetic-isotropy, and realized-state primitives neither grant
nor obstruct these estimates. No missing estimate is relabeled as a new axiom.

### N7 — hostile steelman

A hostile reviewer should say that the absolute Cauchy bound throws away the
one fact most likely to make the derivative small: after subtracting the
product-fiber response, every surviving marked cluster must contain a base
activity. Correct. In an ultra-deep wedge that factor can be arbitrarily small.
The present boundary therefore motivates, rather than forecloses, a centered
marked-tree proof. The same reviewer should demand Peter--Weyl smoothing before
calling finite jets insufficient for contraction. Correct: finite jets alone
do not erase the tail, but actual constrained integration may damp it.

### N8 — cross-cycle echo

| Earlier surface | Earlier wall | Later mechanism | Present lesson |
|---|---|---|---|
| Raw unit directions | Full unrescaled norm had unit directions | Declared factor-two support rescaling | Do not turn a failed certificate into a map no-go. |
| Pair Hessian only | No all-order source domain | Two-layer marked-source and simultaneous joint-polymer estimates | Stronger localization machinery can retire method walls. |
| No joint norm | Generated action lacked uniform membership | Simultaneous retained-Grassmann polymer norm | The next gap is an operator estimate, not an axiom. |
| No RG chart | Fine/coarse weights were incomparable | Declared factor-two RG chart | The chart now exposes exact half-weight bookkeeping. |

Several live routes remain. The negative claim is therefore only that the
unlocalized joint-polymer/RG-chart certificate cannot prove `q<1`, and that finite jets do
not delete the fixed-support character tail. No physical contraction route is
declared closed.

**No-Go Discipline status: PARTIAL ATTEMPT.** Several rows identify live norm
or smoothing routes without executing them. They remain untested and do not
count toward an N1 PASS.
