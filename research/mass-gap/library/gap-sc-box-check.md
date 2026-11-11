# Repo search

Codex checker; requested profile gpt-6-astra/high; source commit
`ce823f882e85a7ab1b7f24e3218dbff10cc6e52a`. This is research text, not an
audit, and grants no status. Claude Opus 5.5 wrote `gap-sc-box.md`; I wrote
none of that source. All source line numbers below refer to that pinned file.

The task-specific prior note `prior/gap-sc-box-check.md` is absent.
The lead supplied the completed row 683 and requested this check as row 694.
The general digest `prior/repo-search-2026-11-08.md` records searches of main
and PRs 10114, 10133, 10134 and 10141. Its targets are earlier RG obligations,
not SC_B; it is not evidence that SC_B was searched exhaustively.

Supplemental searches located the main boundary-response note below and
refreshed the four requested PR heads. PRs 10114, 10133 and 10134 remain
at `f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`89faef229ff6e6bde42baad15ed8270c2f4087d8` and
`1e70c7211a2cdbc39001e619f1dd89db45e25851`. Two broader exact-target
grep attempts did not finish promptly and were stopped. The first output
was empty; the second had 38 inspected lines about L^(4k) block counts
and other unrelated RG expressions on PR 10114. Neither establishes
absence from the requested refs. Their partial logs are
`/tmp/gap-sc-box-check-ce823f882/target-search.txt` and
`/tmp/gap-sc-box-check-ce823f882/scoped-target-search.txt`.
The relevant prior hits were instead opened directly as listed below.

Relevant prior work checked directly:

- The digest's rooted-set count in PR 10141,
  `research/ym4d/library/in1.md:530-538`, is the same
  degree-to-the-power-`2(n-1)` counting argument used at source line 134.
  Fetched PR head `fb99b4dddc7254e6124ac124887d58eeb3a77802` preserves it.
  Credit that existing lane argument; the count is not new here.
- Current main `3b6e5c0baf4295645a07cbfc99813501c8c08c63`,
  `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md`,
  has the same Wilson convention and a finite-product comparison method.
  It concerns real boundary response, not this complex covering difference.
- `open-registry.md` has no SC_B/sc-box owner; its GEOH-O6 winding-carrier
  row concerns RG reads, not this finite plaquette problem. The consumer
  `gap-zf-box-x.md:10` assigns SC_B to row 683 and its other inputs elsewhere.
  This report checks row 683 only; it does not take over those inputs.

I used the SA index README, matching chunk rows and neighbouring rows,
and `obligations.md` before reading bounded source excerpts. Ethan Sussman
and Levent Alpoge, with Claude and Codex as authors of their text, already
give an abstract finite-polymer convergence/nonvanishing theorem:
`YM4_sketch_500.tex` at `31a47c543775`, lines 1150-1174 and 1271-1347.
They say, “The estimate on the activities remains a separate analytic task.”
Their lines 4693-4713 give a normalized Schwarz/logarithm lemma as well.
These are related general tools, not the SC_B activity estimate or its
four-plaquettes-per-slab covering identity. Source line 12 overlooks the
general polymer theorem when describing its index hits; replace its broad
account description by this bounded comparison. No claim of global absence
from their account is needed or established here. Both requested source
files were fetched once. CA-I was searched at anchors, not read whole.
Its abstract-polymer definition at CA-I 21900-21951 was also read;
it defines the general gas and states that convergence is proved later.
No theorem from that later proof is imported here. The requested
CA-4.12-4.19 index search located no SC_B supplier under the target terms.

No new abstract polymer proof is proposed. The task explicitly requests a
check of Claude's existing elementary proof, including its particular
induction and constants. Historical attributions to Osterwalder-Seiler,
Dobrushin and Kotecky-Preiss remain the author's credited recollections;
their primary papers were not read in this check.

## 1. Setting, Haar independence and cumulants (points 1 and 2)

**HOLDS.** Source lines 21-22 and 41-66.

Use one positively oriented variable per geometric link; reverse traversal
uses its inverse. For a spatial plaquette, the four vertices of its unit
square are distinct in Z^3. Opposite links are distinct and perpendicular
links have different directions. Removing sites cannot identify links.
For a time-like plaquette over `{x,y}`, its two spatial links occur at
different times, and its time links have distinct spatial bases `x,y`.
Spatial and time links have different types. For m >= 3, the cyclic time
edges themselves are distinct even as unoriented geometric edges. Thus all
four variables are distinct. A small B either contains such a square/link
or lacks the corresponding plaquette; there is no extra small-B case.

Lemma 2.1(a,c): condition on every variable except the exclusive link l.
The trace is `tr(U_l^epsilon V)` by cyclicity, with V fixed under this
conditioning. Inversion and right translation preserve Haar measure on
SU(2). The conditional distribution of s_p is therefore fixed and does not
depend on any conditioned variable. Integrating bounded test functions
gives exactly line 56. This proves independence, not just zero covariance.
Part (b) follows from disjoint product coordinates. Repeated occurrences
of a variable in a tuple do not change either independence assertion.

K1 is immediate from the moment generating function. For K2, independence
factorizes that function into factors using disjoint parameter sets.
The logarithm splits near zero; a derivative using both sets is zero.
For K3, each operator `d/dt_r` becomes `d/du_(p_r)`, including repetitions.
The sum of all ordered derivatives of the diagonal restriction is exactly
the sum in line 45. Bounded variables justify differentiation to every
finite order and a complex analytic germ at zero.

In Lemma 2.2, a tuple `(p,...,p)` contributes the one-variable cumulant
c_n. K2 cannot remove it: there is no nonempty independent other family.
For two or more distinct plaquettes, partition positions by connected
components, or by all occurrences of the plaquette with an exclusive
link. In the latter case I contains every repeated occurrence of p and J
is nonempty. Lemma 2.1(c) then applies to the whole repeated vector.
These are precisely the alternatives in lines 65-66. For n=1 there are no
good tuples and the full sum is N_m c_1. Haar symmetry V -> -V also gives
c_1=0, although cancellation below does not require that value.

## 2. Slab count (point 3; independent route)

**HOLDS.** Lemma 2.3, lines 70-73. The following is a separate short
edge-count proof, in place of the source's longest-path/cycle proof.

A time link based at x in slab t can occur only in a time-like plaquette
over a spatial edge incident to x, in that same slab. No spatial plaquette
contains it. Distinct slabs give distinct time links for m >= 3. In
particular a plaquette in the preceding slab does not cover this time link.

Form the graph H whose edges are the spatial edges carrying M's
time-like plaquettes in slab t. Coverage forces degree at least two at
every nonisolated vertex. Pick an edge ab. There is an edge ab' with b' != b
and an edge a'b with a' != a. Parity of the Z^3 coordinate sum is a
bipartition, so a,a' lie in one part and b,b' in the other. These are four
distinct vertices. Vertex b' needs a second edge, distinct from all three
already named (none of those other two is incident to b'). Thus H has at
least four edges. Each is a distinct plaquette in this slab. Different
slabs have disjoint plaquette sets, giving |M| >= 4j.

The source's cycle argument also holds: in a finite longest simple path,
the last vertex's second neighbour lies earlier than its predecessor.
That closes a simple cycle of length at least three. Bipartiteness makes
its length even, hence at least four. Finiteness and free-wall embedding
in Z^3 suffice. B need not be connected, rectangular, simply connected,
or contain a spatial square. If B's induced graph has no cycle, the
premise of a covered set meeting this slab is impossible.

## 3. Covering and Taylor cancellation (points 4 and 5)

**HOLDS AFTER CORRECTION** for F1-F3 and Lemma 2.4 as stated for q >= 1.
The first false assertion is F1 at line 85, caused by line 82's definition
at q=1; its proof at line 86 makes the same error.
W_0 then equals the whole cyclic time set. Both endpoints of every slab
belong to it, including slab t_0. Hence its stated G_0 is P_k, rather
than R(t_0). For example take B consisting of two adjacent sites, k=3,
q=1, t_0=0. G_0 has three time-like plaquettes and R(0) has two.
The assertion in line 86 that there are k-1 slabs with both endpoints in
W_0 is false. This is a definition defect, not a counterexample to SC.

**Correction and proof.** Handle q=1 first: pi is the identity, each good
tuple has exactly one good preimage with the same joint law, and D=0.
For F1-F3 and their window proof assume q >= 2. Equivalently one can define
the interior slabs explicitly as the reductions of the integers
`t_0+jk+1,...,t_0+(j+1)k-1`; this gives the intended G_j even for q=1.

For q >= 2 the displayed windows have k distinct times, are disjoint,
and partition the time circle. Exactly their k-1 interior slabs have
both endpoints in the same window. Reduction modulo k maps those slabs
onto all residues except t_0. Spatial links are identified by spatial
edge and time; time links by spatial site and slab. Reduction is injective
on each such collection and preserves their types. It maps every
plaquette boundary, with signs and ordering, to its downstairs boundary.
This proves both bijections in F1 and the reverse incidence implication
of line 88, even if some spatial links are absent from L(G_j).

Every lifted plaquette avoiding residue t_0 belongs to exactly one G_j.
Two different windows share no plaquette link: their spatial-link times
and their time-link slabs are disjoint. This proves F2 and F3. Sharing a
vertex without a link does not count as adjacency.

For a good n-tuple upstairs with n<4k, the distinct support has fewer
than 4k plaquettes. Lemma 2.3 bounds its occupied slabs by fewer than k,
so at least one residue modulo k is missing. F3 places the entire
connected support in one window. The incidence bijection preserves
distinctness, connectivity and coverage. The same ordered words in
bijectively indexed independent Haar variables have the same joint law;
thus every cumulant, including repeated positions, agrees.

Conversely fix one missing slab of a good downstairs tuple. Each of the
q windows gives one lift by F1. Each lift is good and the lifts are
distinct. Any good preimage lies in the preimage of this fixed R(t_0);
F3 puts it in one window and injectivity forces that window's lift.
Choosing a different missing slab cannot add lifts, since this argument
already counts every preimage using one fixed cut. Thus the map is
exactly q to one, with equal joint laws.

**Proposition 2.5: HOLDS AFTER CORRECTION** of the covering proof. There is
one constant tuple for each plaquette, contributing c_n, not n! c_n.
There are exactly m P_s spatial plaquettes and m L_s time-like plaquettes.
Thus N_(qk)=q N_k for every finite B. K3, Lemma 2.2 and the good-tuple
bijection give the stated identity at each 1 <= n < 4k. At n=1 the good
sum is empty, so this includes that case without a covering argument.

**Corollary 2.6: HOLDS.** On a zero-free disc the branch is uniquely fixed
by log Z(0)=0. Locally it is `-beta N_m+H_m(beta)` by equality on a real
interval and analytic continuation. Its n-th Taylor coefficient is
`kappa_n(S_m)/n! - N_m [n=1]`. The constants at zero cancel. At order one
both the Haar mean and the action shift scale by q; at orders 2 through
4k-1 the cumulants scale by q. No principal logarithm of the full Z is
being assumed. In line 112's winding description, read "every slab" as
every base slab, that is, every residue modulo k for an upstairs support.
It need not meet every one of the qk upstairs slabs. The precise result
used below is the proved low-order cancellation; no converse saying that
every all-slab set contributes is used.

## 4. Local estimates and polymer counting (point 6)

**HOLDS.** Lemmas 3.1-3.3, lines 118-134.

For y=|beta|<=1/4 and |z|<=y,
`|exp(z)-1| <= exp(y)-1 <= y/(1-y) <= 4y/3`.
The middle inequality follows from `exp(-y)>=1-y>0`, including y=0.
Averaging gives `|c_0-1|<=4y/3<=1/3`, hence `|c_0|>=2/3`.
The numerator of g is at most `8y/3`; division gives `|g|<=4y`.
The Haar integral of the entire exponential is entire, by compact
domination on bounded beta sets. Its denominator stays away from zero
on this disc, so g is analytic in its interior. The principal Log c_0
used later is valid since c_0 lies within distance 1/3 of 1.

In Lemma 3.2 expand the finite product over plaquettes. The connected
components of each chosen subset share no link, so their expectations
factor under product Haar measure. Conversely a compatible family is
exactly the components of its union: each member is connected, and
different members cannot be joined by a plaquette adjacency edge.
Self-incompatibility rules out repeated polymers. This proves the exact
partition polynomial, with the empty subset contributing 1. Taking
absolute values inside the finite Haar integral gives `(4y)^|X|`.
Analyticity follows from uniform compact domination on each smaller disc.
No mean-zero property of g or cluster-convergence theorem is being used.

A spatial link in direction i has at most two spatial plaquettes in each
of the two other spatial directions, hence at most four. It has exactly
the two possible time-like plaquettes in slabs t and t-1, if present.
These are distinct at m>=3. A time link has one possible plaquette per
incident spatial edge, at most six. A plaquette has four distinct links;
each is in at most five other plaquettes. Thus its number of distinct
neighbours is at most `4*5=20`. Multiple shared links can only reduce that
upper bound. Free walls delete candidates and do not add any.

For n=1 there is one connected set through p_0. For n>1 fix an ordering
on the finite graph and choose a spanning tree and a traversal
deterministically for each set. The traversal has length `2(n-1)`;
its visited vertices recover the set. Different sets cannot have the same
walk, so the number of sets is at most the number of such walks,
`20^(2(n-1))=400^(n-1)`. This spells out the injection implicit in line 134.
It is the existing rooted-set argument credited in Repo search above.

## 5. Finite-gas induction and logarithm (point 7)

**HOLDS.** Lemma 3.4 and Corollary 3.5, lines 136-150.

Induct simultaneously on nonvanishing and all one-polymer removal ratios
for sets of size s. The empty partition polynomial equals 1. For X in a
nonempty S, splitting compatible families by membership of X gives line
142, including its self-exclusion because X belongs to N[X]. Every set
in the removal chain T_i has size below s; all denominators are nonzero
by the induction hypothesis. Its removal inequalities multiply to
`|Xi_(S\N[X])/Xi_(S\{X})| <= exp(sum_(Y incompatible X,Y!=X) c(Y))`.
The sum on the right may include polymers outside S, which only enlarges
it. This gives the first bound on u. Condition (D) gives the second.
As c(X) is finite, `1-|u|>=exp(-c(X))>0`. The triangle inequality proves
both nonvanishing and the inverse ratio bound for S, completing the
induction for every X. If c(X)=0 then (D) forces w(X)=0 and u=0; there is
no exceptional case.

The product in Corollary 3.5 telescopes exactly. Each factor 1+u_i lies in
the open right half-plane, since |u_i|<1. Its principal logarithm is
well defined. The convergent series gives

```math
|\operatorname{Log}(1+u_i)|
\le -\log(1-|u_i|)
\le \frac{|u_i|}{1-|u_i|}
\le |w(X_i)|\exp\!\left(\sum_{Y\not\sim X_i}c(Y)\right).
```

The final factor `exp(c(X_i))` comes from bounding the reciprocal
`1/(1-|u_i|)`. Thus the last inner sum must include Y=X_i, exactly as
lines 147-148 say. Taking the sum proves the stated bound. This log is a
sum of principal logs of factors, not necessarily the principal log of
the product Xi. With the stated fixed c on an open set, the ratios are
analytic and remain in that half-plane; their finite sum is analytic and
exponentiates to Xi. No simple-connectivity assertion is needed for this
finite, explicitly factored construction.

## 6. Proposition 3.6 (point 8; arithmetic and independent route)

**Arithmetic HOLDS. Analyticity HOLDS AFTER CORRECTION of the application
at line 164:** use a fixed majorant on the disc, as specified below.
No constant or conclusion needs to change.

First check the source's arithmetic, with a=|X|>=1 and
`0<=x=4|beta|<=1/3200`. Its count gives

```math
\sum_{Y\not\sim X}c(Y)
\le 24a\sum_{n\ge1}400^{n-1}(4x)^n
=\frac{96xa}{1-1600x}
\le192xa\le\frac{3a}{50}.
```

Indeed `1600/3200=1/2` and `192/3200=3/50=0.06`.
This includes Y=X, hence also bounds the smaller sum in (D).
Since `4x<=1/800<1`, `c(X)=(4x)^a<=1/800<=1`.
For c>=0, `exp(-c)<=1-c+c^2/2`: the difference has derivative
`-1+c+exp(-c)`, whose derivative is `1-exp(-c)>=0`, and both vanish at
zero. Therefore `1-exp(-c)>=c-c^2/2>=c/2` when c<=1.
The right side of (D) is consequently at least

```math
\frac12(4x)^a e^{-3a/50}
=\frac12(4e^{-3/50})^a x^a
\ge\frac{2^a}{2}x^a\ge x^a\ge |w(X)|,
```

because `4 exp(-3/50)>=4(1-3/50)=94/25>2`.
This verifies lines 158-160, including a=1 and x=0.
At x=0 all activities and c's vanish, Xi=1, and (D) reads 0<=0.

For the logarithm bound, overcount each polymer by choosing a plaquette
it contains. Lemma 3.3 gives

```math
|\log\Xi|\le N\sum_{n\ge1}400^{n-1}(x e^{3/50})^n.
```

Here `exp(3/50)<=1/(1-3/50)=50/47<2`, again from
`exp(-t)>=1-t`. Thus the series ratio is at most
`800x<=1/4`, and its first term is at most 2x. The sum is at most
`(8/3)xN=(32/3)|beta|N`. This supplies the elementary justification of
the exponential bound implicit at line 163; no decimal evaluation occurs.

**Independent arithmetic route.** Count by the closed adjacency
neighbourhood of each plaquette of X, instead of its four links. That
neighbourhood has at most 21 plaquettes, including itself. Every
incompatible Y contains one of these plaquettes, so

```math
\sum_{Y\not\sim X}c(Y)
\le21a\frac{4x}{1-1600x}
\le168xa\le\frac{21a}{400}.
```

Use `1-exp(-c)>=c exp(-c)`, which follows from `exp(c)>=1+c`.
The right side of (D) is at least

```math
c(X)\exp\!\left(-\sum_{Y\not\sim X}c(Y)\right)
\ge x^a(4e^{-21/400})^a
\ge x^a\left(\frac{379}{100}\right)^a
\ge x^a.
```

The zero case is direct as above. This verifies (D) by a different
incidence count and a different lower bound, without the source's factor
1/2. Also `exp(21/400)<=400/379<2`, so the same geometric-series estimate
gives the source's `32/3` logarithm constant. This independent check is
not an additional claimed result or an optimized replacement theorem.

**Fixed-majorant correction and proof.** Line 155 chooses c depending
on |beta|, whereas the analytic clause of Corollary 3.5 explicitly uses
one fixed c. For that clause put
`x_*=1/3200`, `c_*(X)=(4x_*)^|X|=(1/800)^|X|`.
For every |beta|<=R, `|w_beta(X)|<=x_*^|X|`. The arithmetic just checked
at x_* proves (D) throughout the disc with this one c_*.
Apply Lemma 3.4 to every partial gas. For a fixed enumeration the ratios
u_i(beta) are analytic on |beta|<R, since their polynomial denominators
never vanish. Their modulus is uniformly below 1 by c_*. Their principal
logs therefore give an analytic log Xi throughout the disc.

For the sharper pointwise bound, apply the estimates at
`x=4|beta|` to those same ratios and that same finite sum of principal
logs. Their values do not depend on which majorant proved their bounds.
Thus the estimate proportional to |beta| is for this analytic branch.
At zero, g=0, all w=0, Xi=1 and log Xi=0. For real beta the ratios are
real and |u_i|<1, so every Log(1+u_i) is real. Also c_0>0 there.
Consequently `-beta N+N Log c_0+log Xi` has all properties claimed in
Proposition 3.6. Nonvanishing also holds on |beta|=R by (D) there.
For each fixed finite lattice, compactness of that closed disc and
continuity give a slightly larger zero-free neighbourhood; the branch
can thus be interpreted on the closed disc as asserted in Theorem SC(i).

## 7. Assembly and the constants (point 9)

**HOLDS AFTER CORRECTION**, using the covering and analytic-branch repairs above.
Source lines 170-177 prove the stated Theorem SC with its original constants.

The factors `-beta N_m` and `N_m Log c_0` cancel between m=k and m=qk,
because N_(qk)=qN_k and the same analytic Log c_0 is used. No unidentified
multiple of 2 pi i remains: all logs have value zero at beta=0.
The triangle inequality and Proposition 3.6 give

```math
|D(\beta)|\le\frac{32}{3}|\beta|
  \left(N_k+\frac{N_{qk}}q\right)
=\frac{64}{3}|\beta|N_k.
```

Assign each spatial edge to its lower endpoint; at most three are assigned
per site. Assign each spatial square to its lower corner and its pair of
directions; again at most three are assigned per site. Thus
`L_s+P_s<=6|B|`, regardless of holes or disconnected components. Hence

```math
|D(\beta)|\le\frac{64}{3}\frac1{12800}\,6|B|k
=\frac{128}{12800}|B|k=\frac{|B|k}{100}=:M.
```

Corollary 2.6 makes `h(beta)=D(beta)/beta^(4k)` analytic after removing its
singularity at zero. For any |beta|<r<R the maximum modulus principle on
the closed radius-r disc gives `|h(beta)|<=M/r^(4k)`. Let r increase to R
and multiply by |beta|^(4k). At beta=0 the inequality holds directly.
This proves

```math
|D(\beta)|\le\frac{|B|k}{100}(12800|\beta|)^{4k}.
```

The argument uses analyticity on the open disc and a bound on every smaller
circle; it does not assume a boundary Schwarz theorem. It is uniform in B
and the positive integers k>=3 and q>=1. For q=1, D=0 from the outset.
Although line 21 initially says nonempty B, the theorem's empty-B case
also holds by the empty-product convention: Z=Xi=1 and both sides vanish.
No division by M is needed, including when M=0.

For `2r_0=theta R`, `0<theta<1`, the *closed* radius-2r_0 disc lies strictly
inside the proven disc. Substitution gives `theta^(4k)=exp(-kappa_0 k)`
with `kappa_0=4 log(1/theta)`. In particular

```math
R=\frac1{12800},\qquad c=12800,\qquad C_0=\frac1{100},
\qquad r_0=\frac1{51200},\qquad 2r_0=\frac R2,
\qquad \kappa_0=4\log2.
```

All numerical comparisons above are displayed rational inequalities;
no numerical or symbolic run was used to establish them.

## 8. Match to the consumers (point 10)

**HOLDS.** Theorem SC with the corrected proof supplies exactly (SC_B),
with the constants just displayed. This is an input match, not a check of
the transport theorem or its other hypotheses.

| Feature | Source and consumer comparison |
|---|---|
| Spatial boundary | Source line 21 and `gap-zero-transport.md` Section 6, lines 84-88, use every spatial edge with both endpoints in B and every unit square with its four corners in B. No fixed exterior links or boundary gauge values are added. |
| Time geometry | Both use B times a time circle. Each spatial edge carries one time-like plaquette in every slab. Source permits k>=3 and all integer q>=1; SC_B asks only k>=4. |
| Coupling | Both use Haar probability and `Z=integral exp(-beta A)`, `A=sum_p(1-(1/2)Re tr U_p)`. On SU(2), tr U_p is real, so the source's omission of Re changes nothing, even for complex beta. There is no beta-to-g or factor-of-two conversion. `gap-zf-box-x.md:14-17` uses exactly this convention. |
| Logarithm | Source normalizes log Z(0)=0 and proves it real on the real segment. Since Z is positive for real beta, this is precisely the consumer's real branch. It need not equal the principal log of Z at nonreal beta. |
| Disc and bound | For every abs(beta)<=2r_0=1/25600, the source gives nonvanishing and `abs(g_q)<= (card(B)k/100)2^(-4k)`, including the circle. This is `C_0 card(B)k exp(-kappa_0 k)` with constants independent of B,k,q. |

The corrected Theorem ZB at `gap-zero-transport-check.md:94-98` keeps
(SC_B) unchanged. Its extra connectedness condition (C), explained at
lines 74-76, is what identifies the disc branch with the branch on D:
their difference is locally a constant integer multiple of 2 pi i, zero
at beta=0, hence zero throughout the connected overlap. Theorem SC does
not assert that arbitrary D satisfies (C) or (ZF_B).

For `gap-zf-box-x.md:142-151`, the initial small disc is centred at r_0
and has radius at most r_0/4 in the induction. It lies in |beta|<=2r_0,
so the input bound applies. Each disc's branch is normalized to be real
at its positive real centre. Overlaps of consecutive discs contain a
positive real interval. On that interval both logs are the real log of
the same positive partition function, so their analytic continuations
agree on the connected disc overlap. Thus the chain reads the same g_q;
there is no additional branch choice in supplying SC_B.

The values in source line 28 meet both consumers exactly. No assertion
about their transport, transfer-operator, harmonic-measure or continuation
arguments is imported into the proof of SC.

## 9. Verdict table

The source was read in full once and its mathematical steps checked line
by line by Codex. The first false assertion is F1 at line 85 for q=1,
caused by the window definition at line 82.
The corrected proof above has no remaining failing step identified in
this check. These are research-check verdicts only.

| Requested point | Source lines / statement | Verdict | Reason or correction |
|---|---|---|---|
| 1 | 49-57, Lemma 2.1 | HOLDS | Four distinct link variables; conditional Haar law proves (a,c), disjoint coordinates prove (b). |
| 2 | 41-45, 61-66, K1-K3 and Lemma 2.2 | HOLDS | Keep all repeated copies of one plaquette on the same side of K2; singleton tuples give c_n. |
| 3 | 70-73, Lemma 2.3 | HOLDS | Same-slab incidence and bipartiteness; independently checked by a four-edge argument. No rectangular-B requirement. |
| 4a | 79-101, F1-F3 and Lemma 2.4 | HOLDS AFTER CORRECTION | At q=1, line 82 includes the cut slab. Treat q=1 as the identity cover or use the explicit interior slab list. |
| 4b | 103-104, Proposition 2.5 | HOLDS AFTER CORRECTION | Use corrected Lemma 2.4. N_(qk)=qN_k and the singleton contribution are exact. |
| 5 | 106-110, Corollary 2.6 | HOLDS | Normalized analytic branches; orders zero and one cancel explicitly. |
| 6 | 118-134, Lemmas 3.1-3.3 | HOLDS | Constants 4/3, 4, 6, 20 and 400^(n-1) all checked. |
| 7 | 136-150, Lemma 3.4 and Corollary 3.5 | HOLDS | Induction uses smaller sets; the log bound correctly includes Y=X. |
| 8a | 155-163, Proposition 3.6 arithmetic | HOLDS | All rational inequalities checked; separate closed-neighbourhood count also proves (D). |
| 8b | 164-166, analytic log in Proposition 3.6 | HOLDS AFTER CORRECTION | Invoke Corollary 3.5 with fixed c_*; retain the pointwise c for the sharper bound. |
| 9 | 170-179, Section 4 and Theorem SC | HOLDS AFTER CORRECTION | Inherits the two proof corrections; Schwarz step and all constants unchanged. |
| 10 | 24-30, 166; SC_B consumers | HOLDS | Same free-wall object, coupling, normalized branch and closed radius-2r_0 disc. |

## 10. Status and unchecked work

- **Result:** Theorem SC HOLDS AFTER CORRECTION. This report supplies the
  corrections with proofs; it does not edit Claude's source. The exact
  SC_B input follows with `r_0=1/51200`, `C_0=1/100`, `kappa_0=4 log 2`.
- **Checked:** all mathematical steps in source Sections 1-4, including
  degenerate finite B, repeated plaquettes, k=3, q=1, beta=0, the boundary
  of the zero-free disc, every displayed constant, and the consumer input
  comparison. The separate slab and (D) checks are marked above.
- **Not checked:** the full proofs of Theorem ZB, its earlier check,
  Theorem ZB-chain or its corollaries; (TM_B), (ZF_B) outside this disc,
  harmonic measure, limiting theories or a mass gap. Reading consumer
  statements does not establish those results. No status in the tree,
  registry, queue or audit system is changed.
- **Source limits:** no primary Osterwalder-Seiler, Dobrushin,
  Kotecky-Preiss or Balaban paper was read. The SA excerpts were checked
  for the stated scope comparison only, not subjected to another full
  proof check. No exhaustive absence theorem about their texts or the
  repository is claimed.
- **Method:** no computer-assisted proof step, numerical experiment,
  symbolic calculation or enumeration was run. Tools fetched and read
  texts, located prior work, and wrote this report. This is not a Lean
  formalization, human review or audit.
- **Handoff:** the source owner can incorporate the q=1 covering correction
  and the fixed-majorant paragraph. The original constants and consumer
  statement need no change. Only this report is written. No remote post,
  push, source edit or scientific-status mutation was performed.
  The report is uncommitted and unpushed on local branch
  `check/gap-sc-box-ce823f882` in the supplied checkout.
