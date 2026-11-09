# Independent check of integrated global chart-sector ratios

2026-11-09. Research signal **advance** for the frozen sixth draft, after one
verified wording correction. No unresolved material mathematical defect was
found. The argument does cancel the common global all-chart normalization in
the stated sector ratios without assuming factorization. This is a research
gate, not a landing decision, audit verdict, retained status, or a connected
spatial logarithm estimate.

## Frozen source and disposition

Source root:
`/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics`.
Pack: `.claude/science/physics-loops/su2-gauge-aligned-response-20261108`.
The entire 269-line `parts/global-chart-sector-ratio.md` was read at initial
SHA-256 `90f64b65b1f36010128868d114084d3532f46aa070bca4a1c616cee59e9a5e81`.

The coordinator then changed only the normalization wording at lines 206–207
from “The source-only normalization of any original q_u” to “A
source-independent normalization of the original q_u.” The affected window
was reread. Reversing exactly that text change reproduces the initial hash,
confirming that no other source byte changed. The final checked SHA-256 is
`b757aa5ddbec0a1a96cb61d2ee531a4e6571712d97eab53bfae09703c596cede`.

| Input | SHA-256 |
|---|---|
| arbitrary-boundary-interior-moments.md | c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11 |
| buffered-core-conditional-ratio.md | 204f48f463fb69eebb6b309996c663698dadd5969728f2a311176e21b53b42c7 |
| nonlinear-chart-response.md | 5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1 |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |

These exact inputs were already independently checked in this same session;
their matching source-specific coverage is reused. The base/main pins remain
`55fd670ff8995427b24617b2273bd3f78b7559d9` and
`1e0d3b58dcda7f83152b0bb51729260247454d65`. Applicable instructions and the
inherited supervising model/effort are unchanged. No model substitution,
numerical job, source edit, Git/network mutation, formal verification or status
operation was performed by this reviewer. Only this additional gate was
written; the previous four reports remain immutable. No editable prompt changed.

For method attribution only, the primary Harvey–Vondrak manuscript was opened
at pp. 1–3: its equation (1) is the conditional nonneighbor-avoidance premise,
and Claim 3 supplies the corresponding event-removal inequality. This matches
the draft's method credit. The finite proof below was checked directly, without
using that paper to establish any SU(2) premise or connected-response result.
[Harvey–Vondrak, arXiv:1711.06797](https://arxiv.org/pdf/1711.06797).

| Severity | Finding |
|---|---|
| Critical / high | None found. The avoidance induction covers all conditioning sets, and the exact sector ratio uses the same global density in both integrals. |
| Medium | None found. No hidden volume factor, disconnected-sector factorization, omitted orbit term, or derivative of a varying event was found. |
| Low, resolved | The original “source-only” normalization wording could suggest a source-dependent factor was label-independent. The verified final wording says “source-independent,” matching the displayed integrals. A source-dependent common factor would still cancel from the ratio but should be removed before applying its raw-integral derivative formula. |

## 1. Cartesian chart, chord implication and measurable conditioning

The logarithm cube lies strictly within the injectivity ball because
`sqrt(3) delta_ch < pi`. If a principal logarithm has norm less than
delta_ch, all three components have absolute value less than delta_ch, so
the link lies inside the cube. Contraposition gives norm at least delta_ch
for a chart-bad link. At -I every principal choice has norm pi and gives the
same conclusion. On `[0,pi]` the chord function `2 sin(theta/2)` is increasing,
which proves the stated chart-bad implication with
`delta_*=2 sin(delta_ch/2)>0`. This uses the actual Cartesian cube; no radial
ball is substituted for its good event.

Each E_x reads only retained coordinates owned by x. Their complements
intersect to exactly the product chart, with boundary faces immaterial for
the integrals. A product cap strictly inside the chart has positive Haar
mass and positive model weight, so every G_J has positive probability before
any induction. The actual all-chart probability need not be uniformly large.

The chart-bad joint event is contained in the buffered supplier's chord-rough
joint event. Its all-exterior bound therefore gives (H) at the same fixed
radius h and positive rate a for every deterministic nonempty S. If J is
outside N_h(S), G_J is measurable with respect to the conditioned exterior
sigma algebra. Taking the conditional expectation of (H) under the exterior
law conditioned on G_J gives (L_S), and its singleton instance gives (L).
This is a tower-property argument using pointwise exterior uniformity, not
an independence statement.

As an adversarial control, ordinary all-set rare-event bounds alone would
not justify this step. Consider a finite abstract law with probability e of
no bad event and probability 1-e of exactly one bad event, uniformly located
among n sites. Then each bad-event probability is eta=(1-e)/n, every joint
bad event of size at least two has probability zero, and all avoidance events
have positive probability. Yet
`P(E_i | all other events avoided)=eta/(e+eta)` can be arbitrarily close to
one. The new proof excludes this failure through (H); it does not infer (L)
from the weaker unconditioned rare-set bound.

## 2. Complete finite avoidance induction

I reconstructed the induction keeping the conditioned event in numerator and
denominator. For J not containing i, split J into its neighbors of i and
the remaining nonneighbors. Since the latter indices are outside N_h(i),

```
P(E_i | G_J)
  = P(E_i intersect G_Jnear | G_Jfar) / P(G_Jnear | G_Jfar)
  <= eta / P(G_Jnear | G_Jfar).
```

Order the k near indices. Each factor of the denominator is a good-event
conditional with a conditioning set of cardinality at most |J|-1 and excluding
the tested index. Thus the induction hypothesis applies to every factor,
even if the already conditioned indices have arbitrary neighbor relations
among themselves. The product is at least `(1-x0)^k`, with k<=D. The assumed
`eta<=x0(1-x0)^D` gives the desired upper bound x0. If k=0, the original
nonneighbor bound applies directly, avoiding circular use of the induction
at cardinality |J|. The empty conditioning set is its valid base case.

Ordering any A disjoint from B then gives
`P(G_A | G_B)>= (1-x0)^|A|`. No positivity denominator is supplied by an
unproved hypothesis: positivity was established by the compact cap. Periodic
identifications can only reduce the degree from the fixed bound `B_h-1`.

For disjoint S,J, split J into indices inside and outside N_h(S). Dropping
the inside avoidance restriction from the joint-bad numerator gives (L_S),
while the just-proved avoidance product bounds the denominator. At most
`|N_h(S)|<=B_h |S|` inside indices can occur. Hence

```
P(all E_x, x in S | G_J)
    <= eta^|S| (1-x0)^(-B_h |S|).
```

This verifies (9), including its sign and its conditioning set. The empty S
case is handled separately with value one. The proof neither conditions on
specific neighboring fields nor assumes joint bad events are independent.

## 3. Exact integrated sector and release ratios

Every configuration has a unique set S of chart-bad owner cells, so the
sector indicators are disjoint and sum to one. They are fixed Borel events
in the same global quotient product space, and all kernels, radial factors
and Haar orbit variables remain in the common density W. Thus the exact
sector decomposition requires no interaction factorization.

For a fixed S, divide both sector and all-good probabilities by
`P(G_(Lambda\S))>0`. This gives

```
Z_S/Z_empty
  = P(all E_x, x in S | G_(Lambda\S))
       / P(G_S | G_(Lambda\S)).
```

The numerator costs at most the joint-bad bound just checked, and the
denominator costs at most the inverse of `(1-x0)^|S|`. The resulting rate is
exactly `epsilon=eta(1-x0)^(-B_h-1)`. The global all-chart normalizer has
therefore canceled through two conditional probabilities whose additional
cost involves |S| only. It was not assumed to have a volume-uniform lower
bound, and its surrounding exterior is still integrated under its actual
law conditioned on good events.

The release integral imposes only G_(Lambda\A). Its ratio to Z_empty is
exactly `1/P(G_A | G_(Lambda\A))`, giving (11). Summing the exact sectors
also gives the independent upper bound `(1+epsilon)^|Lambda|`; this binomial
sum uses bounds on individual sector integrals, not products of sector
activities. Both global comparisons may grow exponentially with volume.

As a consistency check, independent bad events of probability p would have
`Z_S/Z_empty=[p/(1-p)]^|S|`, while the all-good probability is `(1-p)^n`.
Thus volume-independent fixed-sector bounds are compatible with vanishing
global all-good probability. No thermodynamic all-good-event approximation
is hidden in the new comparison.

Taking x0=2eta is legitimate after a fixed lower-u threshold makes
`2eta<1` and `(1-2eta)^D>=1/2`; D=0 also works. A further fixed threshold
makes `(1-2eta)^(B_h+1)>=1/2`, proving the stated `epsilon<=2 exp(-a u)`.
All exponents and degree constants are fixed by the chart and buffered
supplier, not the volume. The O(eta |A|) release logarithm follows from
`-log(1-2eta)<=4eta` once eta<=1/4, an allowed further fixed threshold.

## 4. Original sources and the mixed quotient jets

In the displayed integrals, W has no source dependence and all source factors
are kept as `exp(sF(U(a,h))+tG(U(a,h)))` before orbit integration. This retains
the conditional orbit covariance for gauge-variant original sources. The
events and forest reconstruction do not move with the parameters.

At the base point, the four first log-weight insertions are F,G,A_c,A_d.
The actual mean has norm at most one, so each score has the stated sup bound
`kappa u |v|`. The radial normalizer has no terminal-output dependence but
remains in the measure. Different terminal outputs occur in different kernel
factors; with each derivative label used at most once, all cross derivatives
of the log-weight insertions vanish. Thus each raw integral derivative is
the integral of the product of its selected insertions. Its absolute value
is bounded by the same positive sector integral times their sup norms.

This remains valid with a discontinuous sector indicator because the indicator
is fixed and bounded; compact dominated differentiation introduces no boundary
term. A common source-independent normalization of q_u is irrelevant. Any
additional source-dependent common factor would first be canceled from the
ratio, as distinct from treating it as label-independent.

I checked the quotient recurrence by differentiating the identity
`Z_S=R_S Z_empty` directly. Among its subset terms, the K=I term is
`(D_I R_S) Z_empty`; all other terms have fewer ratio derivatives. Dividing
by Z_empty and using the raw-integral bounds yields

```
C_0=1,
C_k=1+sum_(j=0)^(k-1) binom(k,j) C_j.
```

The successive values are `2`, `1+1+4=6`, `1+1+6+18=26`, and
`1+1+8+36+104=150`. Each derivative label contributes its norm once, so the
mixed source-two/terminal-two bound has exactly the displayed u^2 factor.
The small sector weight is applied only at the final base point; no uniform
rarity neighborhood in terminal V or complex sources is assumed.

The recurrence never divides by Z_S. A zero-measure sector has zero raw
integral and zero derivatives at all parameters, while S empty gives the
identically one ratio and zero nonempty jets. Distinct terminal labels commute;
repeated-link derivatives would produce the excluded score-derivative terms.

## Exact conclusion and remaining boundary

The proof establishes an integrated ratio of each exact compact sector to
the common all-chart sector, a local release comparison, and its complete
distinct-label mixed ratio jets under the stated buffered conditional rarity
premise. The positivity and normalization checks do not assume disconnected
factorization. The quantity in (15) is a derivative of R_S, not of a connected
activity or of `log(Z_full/Z_empty)`.

No spatially weighted connected logarithm norm, multiplicative sector
representation, full-posterior cumulant decay, arbitrary fixed-exterior
all-chart denominator comparison, further-depth estimate or physical gap is
provided by this gate. A different coarse conditional denominator retains its
own response subtraction. The separate next proof mentioned by the coordinator
has not been reviewed here. Reopen this gate if the frozen source, conditional
uniformity, chart/ownership events, denominator, or derivative-label convention
changes.
