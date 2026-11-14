# Repo search

**READ.** The checkout is pinned at
`b9dabda264dd5a026c5c3b163fc69d7d30942a40`. There is no
`prior/gap-sos-astra.md`. The lead's `prior/repo-search-2026-11-08.md`
concerns earlier RG targets. It supplies no SOS estimate. Its closest
method hits require common references and actual overlap factorization.
PR 10114 was fetched at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
In `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`,
`RD3.md:560-580` and `RD4.md:448-460,687-694` were read at source.
Credit their Codex authors. These are normalization warnings and
conditional RG estimates, not the requested surface sum.

**READ.** Current main is `bb4ec020d5ada57c630dd89acc98a68397ade423`.
A targeted search for solid-on-solid, multilevel surfaces, dressed
surfaces, wrapping surfaces, RTAIL and height functions found three
unrelated hits. Their source passages were read: the August 10 Regge
worldvolume provenance note, lines 598-611; the archived PR5962 spatial
block dissection note, lines 74-96; and
`outputs/neutral_continuation4_review_2026_10_18/proofs/STATIC_NEUTRAL_RESPONSE_PROOF.md:1-20`.
They concern Regge null modes, polytope dissections and a spin-system
response. None supplies a Wilson SOS estimate. Ref searches are retrieval
checks, not an absence theorem.

**READ.** The same targeted search was completed after fetching PRs
10114, 10133, 10134, 10141 and 10144. Their heads were respectively
`f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c`, `fb99b4dddc72`, and
`1f20846b8057`. Each returned only those same three false positives,
whose blobs agree with main. Full hashes, paths, queries and downloaded
source hashes are in `/tmp/sa-gap-sos-astra.wULIhJ/source-record.json`.
The lane folder was excluded from this outside-lane search; its nearest
results are identified below.

**READ.** The nearest prior work is `gap-rtail-astra.md`, read whole,
by Codex gpt-6-astra max. Its (R12)-(R18) treat all binary terraces;
(R19)-(R22) treat separated pillars. Its (RTAIL*) explicitly leaves
overlapping multilevel surfaces open. These results are reused, not
reproved. Row 826's check is absent at this pin. The checked analytic
inputs are `gap-flat-astra.md` sections 1-3, read with
`gap-flat-check-opus.md`, by Claude Opus 5.5. They retain the original
denominator and give the product Haar inequality. No competing SOS owner
was located in `open-registry.md`, `open-core.md` or `l17c.md`.
FINISH row 827 is this assignment.

# Solid-on-solid wrapping surfaces

Author: **Codex gpt-6-astra max**, 2026-11-12, FINISH row 827.
Research text, not an audit; this grants no scientific status.
**PROVED** means a written hand proof here, not an independent check.
**READ**, **ARGUED**, **GUIDE**, and **OPEN** mark the other statement types.
Definitions inherit the label of their paragraph.

**READ.** Credit **Ethan Sussman and Levent Alpoge, with Claude and
Codex as the authors of their text**, for their finite-polymer machinery.
The requested sources at `31a47c543775` were downloaded once each into
the new empty directory `/tmp/sa-gap-sos-astra.wULIhJ/`.
The outline index README, neighbouring chunk-01 rows 112-148, and
obligations rows 34-49 were read before outline lines 1150-1375.
They prove the combinatorial theorem under the activity criterion;
"The estimate on the activities remains a separate analytic task."
The CA-I 4.12-4.19 index and CA-full index contain no hit for the
specific surface terms above. CA-I 2698-2716 explicitly does not assert
a mass gap. No Balaban result is a premise here.

## Checkpoint

**PROVED / OPEN — final checkpoint.** Equations (S5)-(S9) give the actual
height-dependent neighbourhood and a joint Haar payment. The translated
comb-tree Hölder bound (S10) sums all pinned integer heights. It proves
absolute area decay, with the original Z_m and every decoration, for
the full admissible SOS class at `0<beta<=5/11`, without an excess cutoff.
At beta=1/2 the coarser majorant itself grows exponentially, by the
three-height argument (S20)-(S22). This is not a true-weight obstruction.
The sharper SOS sum above 5/11, and the complementary overhang/handle/
two-transverse-direction tail (RTAIL-SOS), remain open. The next useful
decision is a joint majorant for that complement, or a sharper use of
(S5) at one-half. No numerical proof or independent check is claimed.

## 1. Inherited consumer

**READ.** Write `c=cosh(beta)`, `s=sinh(beta)/2`, and `q=s c^8`.
For a link-connected closed odd surface S, put

\[
 u(S)=c^{|N(S)\setminus S|}
       \int\prod_{p\in S}|\sinh(\beta x_p)|\,dU_{E(S)}.
                                                        \tag{S1}
\]

For any chosen class F, set `B_F=sum_(S in F) u(S)`.
Equations (F8)-(F9) of `gap-flat-astra.md` give, when F is ordered first,

\[
 |T_m(F)|\le (e^{2B_F}-1)/2,\qquad
 \sum_{S\in F}|D_m(S)|\le B_F e^{2B_F}.                   \tag{S2}
\]

These include every decoration and keep the original Z_m. Within one
surface no independence of defects is available. The sufficient new
target is `B_SOS <= C a^p rho^A`, with `rho<1` uniformly on a stated
coupling interval. Here A is the base area and `a^2<=A<=4a^2`.
This controls the SOS part of (RTAIL*); it does not control its complement.

## 2. The actual neighbourhood at arbitrary heights

**PROVED — geometry and domain.** Call the base directions 1,2 and the
chosen transverse direction 3. Fix coordinate 4. The base torus has
`m n=A` faces, with `m,n>=3`. For an integer function h on its faces,
put one horizontal face above f at height h_f. Above a base edge e
between f and g, insert the consecutive vertical faces between h_f
and h_g. Put

\[
 d_e=|h_f-h_g|,\qquad k=\sum_e d_e,\qquad |S(h)|=A+k.     \tag{S3}
\]

First this construction is in the cylinder with integer height. For the
finite transverse period `n_3`, admit every projection with
`d_e<n_3` at every edge. Thus no wall repeats a plaquette. This includes
all height functions in one fundamental slab, and also globally taller
lifts satisfying these local inequalities. The estimates below sum over
*all* pinned integer functions, so no height or density cutoff enters
the cylinder sum. The finite-torus conclusion uses the stated local
admissibility condition. A full-period wall can create a degree-four
horizontal link where its roof heights coincide modulo the period.
Longer walls repeat plaquettes. Those projections require different
geometry and belong to the remaining general-surface problem.

Let P be the reference plane and C_h the mod-two union of the columns
between height zero and h_f, including downward columns for negative h_f.
Then `S(h)=P triangle boundary(C_h)`. Cancellation of common column
faces gives exactly the roofs and walls above. Since P is closed and
a boundary has zero boundary, S(h) is closed and has P's wrapping parity.
Adjacent roofs are joined by their wall, or directly when their heights
agree, so S(h) is link-connected.

**PROVED — an exact set formula, including periodic coincidences.**
For a base edge e, let I_e be the integer levels in the closed interval
between its endpoint face heights. These are precisely its used horizontal
links. At a base vertex v, let J_v be the union of the half-open integer
intervals `[min(h_f,h_g),max(h_f,h_g))` for its four incident edges.
These are precisely the lower endpoints of its used vertical links.
For the finite torus take all these sets modulo `n_3` *before* counting.
Let b count vertical links with four incident surface faces. Then

\[
 H:=\sum_e|I_e|=2A+k,\qquad
 L:=\sum_v|J_v|=k-b,\qquad |E(S)|=2A+2k-b.               \tag{S4}
\]

Every used horizontal link has degree two: two roofs, a roof and a wall,
or two consecutive wall faces. A vertical link has degree two or four.
There are exactly 2k wall incidences at vertical links, so
`2k=2L+2b`. These statements also hold after the admissible projection.
In particular `0<=b<=k/2`.

Define

\[
 F_f=\bigcup_{e\subset\partial f}I_e,\qquad
 K_e=I_e\cup(I_e-1)\cup J_v\cup J_w
 \quad(e\text{ has endpoints }v,w).
\]

The exact neighbourhood count is

\[
 |N(S)\setminus S|
 =\sum_f|F_f|+\sum_e|K_e|+2H+2L-(A+k).                  \tag{S5}
\]

Indeed the first sum counts orientation 12. The second counts orientations
13 and 23: a plaquette touches a used horizontal link at either endpoint
height, or a used vertical link at either base endpoint. Orientations
14 and 24 contribute 2H; orientation 34 contributes 2L. The two faces
in direction 4 are distinct since its period is at least three.
These orientation classes are disjoint and exhaust N(S). Subtract (S3).
This is an actual set count, not a sum of isolated bump neighbourhoods.

**PROVED — the height dependence on the cylinder.** Write

\[
 r_f=\max_{g\in\{f\}\cup\operatorname{nbr}(f)}h_g
          -\min_{g\in\{f\}\cup\operatorname{nbr}(f)}h_g,
 \qquad r=\sum_f r_f.
\]

For an edge e between f,g and endpoints v,w, put
`a_e=min(h_f,h_g)`, `z_e=max(h_f,h_g)`. Let `a_e^*` and `z_e^*`
be the minimum and maximum over all faces meeting v or w. Define

\[
 T=\sum_e\left[(z_e^*-z_e-1)_+
                         +(a_e-a_e^*-1)_+\right].
\]

Let `b_lift` count four-way vertical contacts before projection. Then

\[
 |N(S)\setminus S|=8A+4k+r+T-2b_{\rm lift}              \tag{S6}
\]

on the cylinder. It is an upper bound after projection; (S5) remains
the exact finite-torus formula. The b in (S4) is the *projected* count
and need not equal `b_lift`.

To prove (S6), the intervals I_e around f all contain h_f. Their union
has size `1+r_f`. At v, the union of wall intervals is the interval
from the minimum to the maximum of its four heights, excluding the
top endpoint. At every level between those extremes the cyclic binary
threshold pattern has a transition, which proves this assertion.
The union K_e is therefore an interval of size

\[
 d_e+2+(z_e^*-z_e-1)_++(a_e-a_e^*-1)_+.
\]

Substitute these counts and (S4) into (S5). For a projected graph,
the projection of this lifted neighbourhood covers its neighbourhood;
surface faces remain distinct by the local admissibility condition.
Thus subtracting the same `A+k` gives the asserted upper bound.

**PROVED — consistency with the height-two obstruction.** For a single
pillar of height ell on a flat plane, before periodic coincidences,
`k=4 ell`, `r=5 ell`, `T=8(ell-1)`, and `b_lift=0`.
Formula (S6) gives `8A+29 ell-8`, exactly (R19).
For binary heights, T vanishes, r is the number of base faces touching
a height-change edge, and (S6) gives (R12)'s first expression.
The new term T is the part that a binary-height budget misses.

**PROVED — a uniform consequence that keeps the contact saving.**
Each used link has six incident ambient plaquettes. Counting incidences
and subtracting the four incidences of every surface face gives

\[
 M:=|N(S)\setminus S|
 \le6|E(S)|-4|S|=8A+8k-6b.                              \tag{S7}
\]

An outside face can have several used links, so this is an upper bound.
It holds for every admissible graph, including periodic coincidences.
Unlike the binary budget it pays every intermediate height. Unlike a
plain `8|S|` estimate it retains a saving for four-way contacts.

## 3. A joint Haar bound

**PROVED.** At every positive beta, define

\[
 q=s c^8,\qquad
 t=\max\{s c^8,\;2^{1/4}s c^{13/2}\}.
 \qquad u(S(h))\le q^A t^k.                              \tag{S8}
\]

More precisely, with M given exactly by (S5),

\[
 u(S(h))\le s^{A+k}c^M\,
                    2^{\min(k,4b)/4}.                  \tag{S9}
\]

*Proof.* The moment recursion of (F11) gives `E x^4=1/8`, in addition
to `E x^2=1/4`. In (F10), use exponent four on every vertical face
touching a degree-four link. Use exponent two on all other faces.
At a branching link the four reciprocal exponents sum to one. At every
other used link their sum is at most one. No horizontal face touches
a branching link. At most `min(k,4b)` faces need the larger exponent.

The exponent-two norm of `sinh(beta x)` is at most s; the exponent-four
norm is at most `2^(1/4)s`, by convexity of sinh and the two moments.
This proves (S9) for the *joint* Haar integral, without separating defects.
Combining (S9) with (S7) gives

\[
 u(S(h))\le q^{A+k}c^{-6b}2^{\min(k,4b)/4}.
\]

For `b<=k/4` the last factor is `(2c^{-6})^b`; for `b>=k/4`
it is `2^(k/4)c^{-6b}`. Its maximum on `0<=b<=k/2` is at most
`max(1,(2c^{-6})^(k/4))`. This is (S8). The case k=0 is included.
QED.

## 4. Summing every integer height

**PROVED — a finite-volume height-sum inequality.** Pin one base face
f_0 at height zero. For `0<t<1`, put

\[
 Z_{m,n}^{\rm ht}(t)=\sum_{h:\ h_{f_0}=0}t^{\sum_e|h_f-h_g|},
 \qquad K(u)=\sum_{j\in\mathbb Z}u^{|j|}=\frac{1+u}{1-u}.
\]

The height sum is over all integers, without a gradient restriction.
Then

\[
 Z_{m,n}^{\rm ht}(t)
 \le K\!\left(t^{2A/(A-1)}\right)^{A-1}
 \le K(t^2)^{A-1},\qquad A=mn.                          \tag{S10}
\]

*Proof.* Regard the base faces as the vertices of their adjacency graph.
It has A vertices and 2A edges. Construct a horizontal comb tree T_H:
in each row remove one horizontal wrap edge, leaving a path; connect
these n paths by a vertical path at one fixed column. It has A-1 edges
and is a spanning tree. Average its mn translates. Every horizontal
edge has inclusion probability `(m-1)/m`; every vertical edge has
probability `(n-1)/(mn)`. The transposed comb T_V has probabilities
`(m-1)/(mn)` and `(n-1)/n`, respectively.

Mix the translated T_H and T_V families with respective total weights
lambda and `1-lambda`, where

\[
 \lambda=\frac{mn-2m+1}{2(m-1)(n-1)}.                   \tag{S11}
\]

Both weights are positive for m,n>=3. The numerator is `m(n-2)+1`;
the denominator minus the numerator is `n(m-2)+1`. Substitution gives
the same inclusion probability at every edge:

\[
 r_0=\frac{A-1}{2A}.
\]

Write w_T for these finitely many tree weights, whose sum is one.
If `E_T(h)=sum_(e in T)|h_f-h_g|`, their edge probabilities give
`sum_T w_T E_T(h)=r_0 k(h)`. Therefore, with `u=t^(1/r_0)`,

\[
 t^{k(h)}=\prod_T\left(u^{E_T(h)}\right)^{w_T},\qquad
 \sum_h t^{k(h)}
 \le\prod_T\left(\sum_h u^{E_T(h)}\right)^{w_T}.          \tag{S12}
\]

The inequality is ordinary Hölder with exponents `1/w_T`. First apply
it to a finite height box. Each sum on the right is at most the sum
over all pinned heights. On a tree, orient edges away from f_0. The
edge increments are arbitrary integers and determine every height
uniquely. Thus that tree sum is exactly `K(u)^(A-1)`. This is finite
for t<1. Monotone convergence of the finite height boxes proves the
first inequality in (S10). Since `2A/(A-1)>2` and K increases, the
second follows. QED.

This argument pins the common height translation once. No height-range
factor appears in (S10). Correlated height differences need not be
independent; only increments on each individual tree are freely summed.

**PROVED — SOS area criterion.** Let F_SOS contain the admissible graphs
in either one of the two transverse directions, with all translations
and with heights of either sign. If

\[
 t<1,\qquad \rho(\beta):=q\frac{1+t^2}{1-t^2}<1,         \tag{S13}
\]

then

\[
 B_{\rm SOS}\le2N_\perp q^A
          K\!\left(t^{2A/(A-1)}\right)^{A-1}
          \le2N_\perp\rho(\beta)^A.                    \tag{S14}
\]

For a chosen transverse direction, choose the root height modulo its
period and the other transverse coordinate. There are N_perp choices.
Subtract the root height from every integer lift, then use (S8) and
(S10). Extending the admissible height sum to all pinned integer
functions only increases it. There are two choices of transverse
direction; negative heights already include the opposite sign.
Different encodings of a surface only increase the upper bound.
Finally `K(t^2)>=1` allows the exponent A-1 to be replaced by A.

## 5. An explicit coupling interval

**PROVED — explicit constants.** Uniformly on `0<beta<=5/11`,

\[
 q<\frac8{15},\qquad t<\frac6{11},\qquad
 \rho(\beta)<\rho_*:=\frac{1256}{1275}<1.                \tag{S15}
\]

*Proof.* Both entries defining t, and q, increase with beta. At
`x=5/11`, the successive-term ratios of the sinh and cosh series give

\[
 s\le\frac{x}{2(1-x^2/6)}=\frac{165}{701},\qquad
 c\le1+\frac{x^2}{2(1-x^2/12)}
       =\frac{1577}{1427}<\frac{21}{19}.                 \tag{S16}
\]

The cosh comparison is `29963<29967`. For its series use the ratio
bound only from the quadratic term onward. The constant term is kept
separately as displayed. The following small integer comparisons give
the powers needed below:

\[
 2\,21^4=388962<390963=3\,19^4,\qquad
 3\,21^5=12252303<12380495=5\,19^5.
\]

Thus `c^4<3/2`, `c^5<5/3`, and
`c^13=c^8 c^5<15/4<(31/16)^2`, the last comparison being `960<961`.
Also `2^(1/4)<25/21`, since `2*21^4=388962<390625=25^4`.
Consequently

\[
 q<\frac{165}{701}\frac94=\frac{1485}{2804}<\frac8{15},
\]
\[
 2^{1/4}s c^{13/2}
 <\frac{25}{21}\frac{165}{701}\frac{31}{16}
 =\frac{42625}{78512}<\frac6{11}.                        \tag{S17}
\]

The cross-products are `22275<22432` and `468875<471072`.
Since `8/15<6/11`, both entries defining t are below 6/11. Therefore

\[
 \rho(\beta)
 <\frac8{15}\frac{1+36/121}{1-36/121}
 =\frac8{15}\frac{157}{85}=\frac{1256}{1275}.
\]

Every comparison is displayed rational arithmetic; no numerical run
decides the endpoint. QED.

**PROVED — fully dressed SOS class theorem.** Set
`tau_S=log(1275/1256)>0`. For every box in the consumer, every crossed
pair, and `0<beta<=5/11`,

\[
 B_{\rm SOS}\le2N_\perp e^{-\tau_S A}
                    \le8a^2e^{-\tau_S a^2},             \tag{S18}
\]
\[
 \sum_{S\in F_{\rm SOS}}|D_m(S)|
 \le8e^{16/\tau_S}a^2e^{-\tau_S a^2}                   \tag{S19}
\]

when this class is first in the ordering. Equation (S19) follows from
(S2) and `a^2 exp(-tau_S a^2)<=1/tau_S`. It bounds |T_m(F_SOS)|
as well. All decorations and the original Z_m are retained. Heights,
their total variation, overlaps between terraces, and four-way contacts
have no density restriction. This does not extend the full trace seed.

## 6. Growth of the coarser majorant at beta one-half

**PROVED — a three-height lower bound.** The positive majorant obtained
by summing (S8), with one root and transverse position fixed, obeys

\[
 q^A Z_{m,n}^{\rm ht}(t)
 \ge\frac1{2\sqrt2\,t}
             \left(2\sqrt2\,q t^{3/2}\right)^A.          \tag{S20}
\]

To prove this, retain only heights -1,0,1. Keep the root at zero.
Give each other height probabilities `1/4,1/2,1/4`, independently.
Call their product probability P. Two free neighbouring heights have
expected difference 3/4: difference one has probability 1/2 and
difference two has probability 1/8. An edge at the root has expected
difference 1/2. Thus `E k=(2A-4)(3/4)+4(1/2)=3A/2-1`.
The entropy of P is `(A-1)log(2 sqrt(2))`. Jensen applied to
`exp(k log(t)-log(P))` gives

\[
 \sum_{h\in\{-1,0,1\},\ h_{f_0}=0}t^{k(h)}
 \ge t^{3A/2-1}(2\sqrt2)^{A-1}.
\]

Multiply by q^A. These graphs are admissible at every transverse
period at least three. No large height or winding multiplicity is used.

**PROVED — exponential growth at beta=1/2.** At this endpoint,
`c^6>(9/8)^6>2`, since `531441>524288`. Hence t=q in (S8).
Also `s>25/96` and `c>9/8`. The first five terms of the binomial
expansion give

\[
 q>\frac{25}{96}
 \left(1+1+\frac{28}{64}+\frac{56}{512}+\frac{70}{4096}\right)
 =\frac{131275}{196608}>\frac23.                         \tag{S21}
\]

The squared exponential factor in (S20) is therefore

\[
 8q^5>8(2/3)^5=\frac{256}{243}>1.                        \tag{S22}
\]

Thus the sum of the *coarser upper weights* `q^A t^k` grows exponentially
with A at beta=1/2. It cannot have any area-decay bound there, even if
the Hölder summation were replaced by an exact sum. More generally,
the same obstruction holds whenever `8q^2 t^3>1`.

This is not a lower bound for u(S), (S9), D_m(S), or the signed tail.
An upper majorant may grow while the quantity it bounds decays.
Nor is it a theorem about SOS roughening: fixed-volume pinned height
sums are finite for every t<1 by (S10). At beta=1/2, `t=q<11/15`
by the checked (F14). The failure is exponential growth with the
base area, already in a bounded three-height alphabet. The exact
neighbourhood in (S5)-(S6) retains savings which (S7) loses.

**OPEN.** Area decay of the sharper majorant (S9), or of the actual
SOS activities, throughout `5/11<beta<=1/2` is not established here.
The present interval is sufficient for part (a); its endpoint is not
claimed optimal. Any attempt to reach one-half must retain more of
(S5)-(S6), improve the joint Haar estimate, or use signed cancellation.

## 7. Overhangs, two transverse directions, and the remaining tail

**PROVED implication from the READ earlier class bounds.** Let G_* be
the class in (R25) of `gap-rtail-astra.md`, and enlarge it to

\[
 G_{**}=G_*\cup F_{\rm SOS},\qquad
 \tau=\min\left\{\frac1{40},\frac14\log\frac{600}{599},
               \log\frac{81285}{80905},\log\frac{1275}{1256}\right\}>0.
\]

Using (R26) for its existing classes and (S18) for the new class,

\[
 B_{G_{**}}\le8N_\perp e^{-\tau A}
                         \le32a^2e^{-\tau a^2},
 \qquad 0<\beta\le5/11.                                \tag{S23}
\]

Use the smaller majorant where classes overlap. Ordering G_* first,
then its new SOS members, and then the complement, (S2) gives

\[
 \sum_{S\in G_{**}}|D_m(S)|
       \le C_0 a^2e^{-\tau a^2},\qquad
 C_0=32e^{64/\tau}.                                    \tag{S24}
\]

This union statement uses row 823's author proofs. Their check was
not available at the pin; (S3)-(S22) do not use those unchecked
geometric bounds. Their analytic input is the checked (F8)-(F11).

**PROVED — exact remainder.** With the finite polynomial Xi and
sign-flipped activities of (F2), define

\[
 R_m^{**}=\frac1{2Z_m}\int C(U)
      [\Xi(w_m^{G_{**}};U)-\Xi(w_m^{\mathcal O};U)]\,dU.
 \qquad p_m(v)=T_m(G_{**})+R_m^{**}.                     \tag{S25}
\]

The latter identity is exact telescoping. In its marked-family form,
the remainder contains every compatible marked family with at least
one member outside G_{**}; it can also contain members inside that
class. All unmarked exterior weights in that form are unflipped.
Neither the remainder nor its individual terms are asserted positive.

**OPEN — weakest sufficient statement reached.** For one compact
interval `I subset (0,5/11]`, preferably above 2/9, prove

\[
 R_m^{**}\le C a^p\eta_*^{a/2},                         \tag{RTAIL-SOS}
\]

uniformly for `beta in I`, `a>=3`, the remaining periods in `{a,2a}`, and all
the consumer's crossed pairs. Here `0<eta_*<1` is the same fixed
consumer constant, and C,p are finite and independent of beta,a,pair.
Only an upper bound is needed. From (S24),
`R_m^*-R_m^{**}=T_m(G_{**})-T_m(G_*)` is area-small. With
`kappa=(1/2)log(1/eta_*)`, the inequality
`-tau a^2+kappa a<=kappa^2/(4tau)` absorbs that difference into the
required rate. Thus (RTAIL-SOS) and (RTAIL*) have the same strength
on I, up to constants and polynomial powers. No full-trace estimate
has been inferred from the new class bound alone.

**PROVED scope / OPEN estimate.** What remains outside G_{**} has
excess greater than A/128 and is neither a separated-pillar surface
nor an admissible scalar-height graph in one transverse direction.
The one-step terraces are already contained in F_SOS. In particular:

- Overhangs can have several horizontal faces above the same base face.
  There is no single h_f. The counts H=2A+k and |S|=A+k in (S3)-(S4),
  and the tree-increment parametrization in (S12), no longer apply.
- General handles and branchings outside the graph class have extra
  sheets or transverse faces. Extra projection multiplicity is not
  paid by a scalar total variation. Such objects at excess <=A/128
  remain covered by the earlier all-shape theorem, not by (S18).
- Simultaneous transverse motion requires an edge path in a
  two-dimensional transverse lattice and consistent fillings at base
  vertices. Two heights alone do not determine these choices. Links
  can have degree six; branchings can touch horizontal faces. The
  exponent-four assignment and the geometric saving used in (S8)
  then fail to supply this bound. The general (F10)-(F13) estimate
  still exists, but its high-density entropy has not been paid.
- Height winding without a global integer lift, and projections of
  walls that traverse a full transverse period or repeat plaquettes,
  are not the graph class specified in section 2. A different
  parametrization and its joint weight are required for those sets.

These are the precise points at which the scalar-height proof stops.
No factorization into independent overhangs, separate coordinate-height
gases, or an independent decoration vacuum has been used. A sufficient
stronger next target is a decaying sum of u(S) over this complement;
the signed statement (RTAIL-SOS) asks less. A new contour criterion
would also need new activities: row 823 already proves failure of its
particular dilute contour criterion at one-half.

## 8. Group dependence and verification boundary

**READ / PROVED — group blindness.** The geometry and tree sum use no
group. The normalization step uses a central sign, Haar invariance,
zero mean of x and `|x|<=1`. The new Haar step uses only
`E x^2=1/4` and `E x^4=1/8`. The binary icosahedral group has these
same moments. The class values read in `gap-flat-check-opus.md`
section 7 give, with `a=(1+sqrt(5))/4`, `b=(1-sqrt(5))/4`,
`a^2+b^2=3/4`, `a^2 b^2=1/16`, hence `a^4+b^4=7/16` and

\[
 \mathbb E x^4=\frac{2+40/16+24(7/16)}{120}=\frac18.
\]

The same class sum gives its already checked second moment 1/4.
Therefore (S3)-(S22) are group-blind between SU(2) and that finite
group. No distinction at a higher representation moment enters.
For U(1), `x=cos(theta)` has moments 1/2 and 3/8, so (S8)'s constants
do not transfer. No Coulomb-phase conclusion follows. At weak coupling,
even the flat majorant q exceeds one for beta>=2. These estimates
cannot produce a weak-coupling gap for either control group or SU(2).

**READ / OPEN — relation to the seed.** Row 823 records the checked
full seed from `gap-vmf-lip.md` for each `0<beta<2/9`. This note
does not recheck or strengthen that full statement. Its new class
interval extends above 2/9. Combining it with the full-seed continuation
route still requires (RTAIL-SOS) on the proposed higher interval and
the existing consumer's transfer hypotheses. Adding a partial class
estimate to a seed at another coupling is not such a continuation.

**READ — verification.** All mathematical steps above are hand arguments.
No numerical run, machine enumeration, interval certificate or Lean run
was used. The labelled proofs require an independent check; the author's
self-read is not one. Mechanical checks only concern the output file,
source revisions, and accidental whitespace or conflict markers;
their record is `/tmp/sa-gap-sos-astra.wULIhJ/file-checks.json`.
Only this assigned output file is changed in the checkout.

**READ — delivery and recovery.** The source pin and downloaded revisions
are recorded above. The current branch is
`research/gap-sos-astra-20261112`; this output is uncommitted and unpushed.
No registry, queue, audit, planning file, main science file or public post
was changed. The next reader should check (S5), the periodic case of
(S4), the contact payment (S8), the translated-tree weights (S11), and
the three-height lower bound (S20). Repeating a dilute contour argument
or summing the same coarse majorant more sharply cannot remove (S22).

RESULT: PARTIAL — hand proofs give the actual SOS neighbourhood, a joint Haar bound, and an absolute area bound with all decorations and the original Z_m for every admissible integer-height graph at 0<beta<=5/11, at every density. The coarser height majorant grows exponentially at beta=1/2 already on three heights; this does not refute the sharper majorant or true Wilson weights. The estimates are group-blind for the binary icosahedral group. Overhangs, general handles, simultaneous transverse motion and the signed remainder (RTAIL-SOS) remain open. No full seed extension, independent check or scientific status is claimed.
