# Repo search

**READ.** This lane starts at `8fe4764595c22ec0e5106a1b5bea780f6432b596`.
There is no `prior/gap-rtail-astra.md`. The lead's
`prior/repo-search-2026-11-08.md` was read in full. Its five-ref
search concerns earlier RG targets, not this later excess-tail target.
Its useful hits are the rooted-code count and the common-reference
warnings. No claim of exhaustive absence follows from that digest.

**READ.** The nearest sources are `gap-flat-astra.md` (read whole)
and its complete check, `gap-flat-check-opus.md`. Credit Codex
gpt-6-astra for (F1)-(F28), and Claude Opus 5.5 for that check.
They already supply the original-normalization majorant, the Haar
product estimate, the sublinear-excess class and separated cube bumps.
These are inputs, not new results below. `gap-joint-astra.md`
sections 1-3 supplies the exact signed surface representation;
`gap-kappa-order.md:31-74`, by Claude Fable 5.2, supplies the
parity expansion and horizontal area lemma.

**READ.** PR 10114 was fetched at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`. In
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`,
`RD3.md:565-575` and `RD4.md:448-460,687-694` require matched
references and actual overlap factorization. They do not supply an
excess-contour bound. `MASS_GAP_LOCAL_BLOCK_ASTRA.md:1-166`
retains the exterior kernel in a local transfer comparison. Its
positive one-step witness is a different quantity. Credit those
Codex authors; no result below is attributed to an independent copy.

**READ.** Searches of `open-registry.md`, `open-core.md` and
`l17c.md` for RTAIL, gap-flat, gap-joint, J12, E17, wrapping surfaces
and excess contours found no competing owner. FINISH row 823 is
this assignment. Row 817's checked classes are not reopened.

**READ.** Current main is `bb4ec020d5ada57c630dd89acc98a68397ade423`.
Its targeted excess-contour, dressed-surface, wrapping-surface,
one-step-terrace and binary-height search found one unrelated Regge
worldvolume hit. Its provenance note, dated 2026-08-10 under the
September 8 admissibility-cut backlog folder, was read at 598-611;
it supplies no Wilson estimate. PR 10141 was fetched at
`fb99b4dddc7254e6124ac124887d58eeb3a77802`; its
`research/ym4d/library/in1.md:530-538` contains the existing rooted
tree-code bound. That generic count is prior work, not the new
exceptional-link encoding below. The transport literature digest
`prior/gap-lit-transport.md` also records a five-ref search and
Muenster's strong-coupling vortex expansion. Its convergence
endpoint is unspecified there; no endpoint is imported into this note.

# Excess contours for the wrapping-surface remainder

Author: **Codex gpt-6-astra max**, 2026-11-12, FINISH row 823.
Research text, not an audit; this grants no scientific status.
**PROVED** means a written hand argument here, not an independent
check. **READ**, **ARGUED**, **GUIDE** and **OPEN** mark the other
statement types. Definitions inherit their paragraph's label.

**READ.** Credit **Ethan Sussman and Levent Alpoge, with Claude
and Codex as the authors of their text**, for their finite-polymer
machinery. Their two requested sources at `31a47c543775` were
downloaded once each, into the new directory
`/tmp/sa-gap-rtail-astra.pnYcWb/`. Source lookup uses the local
full-read index before bounded source reads. No numerical proof
or numerical search is used in this lane.

## Checkpoint

**PROVED / OPEN — final checkpoint.** At every `0<beta<=1/2`,
hand arguments bound three fully dressed classes by area decay:
all shapes with excess at most A/128; arbitrary one-step terraces,
including degree-four contacts and excess up to 2A; and separated
pillars of arbitrary admissible heights, including excess beyond A.
The first uses an injective exceptional-link code. The second uses
a finite defect-contour polynomial and a joint four-height bound.
The third pays the corrected height-dependent neighbourhood.
The general signed remainder remains open. Section 5 gives the
three failed extensions, and section 6 states the precise remaining
estimate. No new full seed or independent check is claimed.

## 1. Consumer and reused analytic input

**READ.** Keep the notation of (F1)-(F28). The horizontal pair is
`(r,i)`, its area is `A=n_r n_i`, and the transverse size is
`N_perp<=4a^2`. All four periods are at least three. A surface
is a nonempty link-connected closed mod-two plaquette set with
odd pairing with the temporal twist. Its excess is `k=|S|-A`.
The horizontal stack parity gives at least one horizontal face
over every base face. Thus the number `V(S)` of nonhorizontal
faces is at most k.

**READ.** For any surface class F ordered first, (F8)-(F9) give

\[
 u(S)=(\cosh\beta)^{|N(S)\setminus S|}
       \int\prod_{p\in S}|\sinh(\beta x_p)|\,dU_{E(S)},
 \qquad B_F=\sum_{S\in F}u(S),                              \tag{R1}
\]
\[
 |T_m(F)|\le\frac{e^{2B_F}-1}{2},\qquad
 \sum_{S\in F}|D_m(S)|\le B_F e^{2B_F}.                   \tag{R2}
\]

All vacuum decorations remain included, and the denominator is
the original Z_m. The marked-family bound is a product only for
surfaces sharing no links. Within a surface, overlapping defects
must be bounded jointly. We reuse

\[
 u(S)\le q^A\gamma^{k(S)},\qquad
 q=\tfrac12\sinh\beta(\cosh\beta)^8<e^{-1/4},\qquad
 \gamma=(4/3)^9<16,
 \quad 0<\beta\le\tfrac12.                               \tag{R3}
\]

**OPEN.** The sufficient target remains the signed upper bound
`R_m <= C a^p eta_*^(a/2)` from (F27). An absolute class bound
does not bound later surfaces whose decorations meet that class.
Below, enlarging the class means telescoping with the enlarged
class first and defining its remaining signed tail anew.

## 2. An encoding with no arbitrary transverse placement per defect

**PROVED — exploration count.** For any integer K>=0,

\[
 \#\{S:k(S)\le K\}
 \le N_\perp\,16^{4K}
       \sum_{b=0}^{\min(2K,2(A+K))}
                    {2(A+K)\choose b}.                  \tag{R4}
\]

Here and below surfaces satisfy the connectedness and odd-pairing
conditions in section 1. The estimate permits handles, branchings,
overhangs and broad terraces. It imposes no graph or footprint condition.

*Proof.* Fix one base face. Choose as root the first occupied
horizontal face over it, using a fixed order of transverse sites.
There are at most N_perp choices. Fix orders of faces, links and
the six plaquettes incident to each link.

Explore the connected face set from this root. Keep a deterministic
queue of discovered faces. Process their four links in fixed order,
skipping links processed earlier. At a processed link e, specify
the complete subset of its incident plaquettes that belongs to S.
Append newly discovered faces to the queue. The set is recovered
when the queue empties: link-connectedness precludes an undiscovered
component. Periods at least three make each incident face distinct.

If e is horizontal and no nonhorizontal face of S meets it, closure
forces exactly the two horizontal incident faces. This is the
default instruction and costs no label. At every other horizontal
link a binary flag marks an exception. There are at most 2V such
links: a mixed face has two horizontal edges, and a purely transverse
face has none. All transverse links are exceptions automatically;
their direction is already known to the decoder.

Every exceptional link touches a nonhorizontal face. Therefore at
most 4V links need a label, including the automatically exceptional
ones. One incident face is already known, since it caused this link
to be processed. Closure allows an odd subset of the other five
faces, giving at most `5+10+1=16` choices. Record that choice by
one of sixteen symbols. Previous discoveries may exclude choices;
including them only enlarges the code set.

Every used link has at least two incident surface faces. Hence the
number of processed links is at most `2|S|<=2(A+K)`. In particular,
there are at most that many horizontal inspections. Record their
flag string, padded by zeros to length `2(A+K)`, with at most 2K
ones. Record the exception labels in their processing order,
padded by a fixed symbol to length 4K.

Given the root and both strings, the same queue reconstructs all
faces. A horizontal flag determines whether to use the default or
consume a label; a transverse link consumes a label without a flag.
Termination is determined by the queue, so padding adds no ambiguity.
Inconsistent codes are discarded. Thus two surfaces cannot have the
same code. Counting the codes proves (R4). QED.

**PROVED — entropy interpretation.** For fixed positive epsilon,
K<=epsilon A, the logarithm in (R4), apart from log N_perp, is
`O(epsilon A log(1/epsilon)+epsilon A)` as epsilon tends to zero.
The constants do not involve a. For example, for any `0<t<=1`,

\[
 \sum_{b\le2K}{2(A+K)\choose b}
 \le t^{-2K}(1+t)^{2(A+K)}.                              \tag{R5}
\]

This follows term by term from `t^b>=t^(2K)`. Taking
`t=epsilon/(1+epsilon)` gives the stated order, using
`log(1+t)<=t`. Thus the encoding pays relative transverse motion
with exceptional-link labels. It does not assign an independent
transverse location to every defect. The remaining binomial counts
the possible attachment locations during an exploration of area A.

**PROVED — all shapes at a fixed excess fraction.** Set

\[
 K_0=\lfloor A/128\rfloor,\qquad
 \mathcal A_* =\{S:k(S)\le K_0\}.
 \quad B_{\mathcal A_*}\le N_\perp e^{-A/40},
 \qquad 0<\beta\le\tfrac12.                              \tag{R6}
\]

*Proof.* Combine (R3)-(R5) with t=1/256. Since gamma<16,

\[
 B_{\mathcal A_*}
 \le N_\perp\exp\left[-A/4+(A+K_0)/128
                                  +36K_0\log2\right].   \tag{R7}
\]

Indeed `16^(4K) gamma^K <= 2^(20K)` and `t^(-2K)=2^(16K)`.
Also `log2<3/4`, since `1+3/4+(3/4)^2/2>2`. Therefore

\[
 (A+K_0)/128+36K_0\log2
 <\left(\frac{129}{16384}+\frac{27}{128}\right)A
 =\frac{3585}{16384}A<\frac9{40}A.                       \tag{R8}
\]

The last comparison is `143400<147456`. Subtract A/4 to obtain
(R6). For K_0=0 the same bound follows directly. QED.

**PROVED — dressed consequence.** The quantity
`N_perp exp(-A/40)<=4a^2 exp(-a^2/40)` has a finite supremum.
Thus (R2) supplies an absolute area bound for this whole class,
with a uniform constant multiplying `a^2 exp(-a^2/40)`.
This improves the earlier sublinear excess cutoff asymptotically
to a fixed positive fraction. It covers the intermediate window
`K(a)<k<=floor(A/128)` whenever that window is nonempty.
No claim about k greater than A/128 follows from (R6).

**PROVED — other excess fractions.** A more flexible version is
available without the fixed constants. For `0<epsilon<=1`, let

\[
 H(\epsilon)=2(1+\epsilon)\log(1+\epsilon)
                         -2\epsilon\log\epsilon,
 \quad
 \Psi_\beta(\epsilon)=-\log q(\beta)
               -\epsilon\log(16^4\gamma)-H(\epsilon).  \tag{R9}
\]

If `Psi_beta(epsilon)>=tau>0` uniformly on a coupling interval
inside `(0,1/2]`, all surfaces of excess at most epsilon A have
`B<=N_perp exp(-tau A)`. Substitute t=epsilon into (R5), and
use K<=epsilon A in every nonnegative cost. This is a proved
explicit sufficient condition; no numerical choice of its root is used.

## 3. Adjacent bumps: a contour gas for all one-step terraces

**PROVED — class definition.** Relabel the horizontal directions
as 1,2, and fix one signed transverse direction, called +3.
Fix the other transverse coordinate. Let P be the horizontal plane
at height zero, and let D be any subset of its A base faces. Form

\[
 S(D)=P\mathbin\triangle
           \partial\!\left(\bigcup_{f\in D}(f\times[0,1])\right).
                                                                  \tag{R10}
\]

The boundary and symmetric difference are mod two. There is one
horizontal face per base face, at height `h_f=1_D(f)`. Across an
edge between unequal heights there is one vertical face. This
description also follows by cancelling the common faces of adjacent
cubes. Thus S(D) is closed, wraps oddly, and is link-connected:
adjacent base faces lift to faces joined either directly or through
their vertical face. Put `k=|partial D|`, the number of base edges
with unequal adjacent heights. Then `|S(D)|=A+k` and `0<=k<=2A`.
No separation between the selected cubes is required.

At a base vertex, the cyclic list of four heights has zero, two
or four transitions. A vertical link is used exactly when this
number is nonzero. Write v_2,v_4 for these vertex counts, and
`v=v_2+v_4`. Counting ends of boundary edges gives

\[
 2k=2v_2+4v_4,\qquad v=k-v_4.                           \tag{R11}
\]

All horizontal used links have surface degree two. A vertical
used link has degree two or four. The latter case is a checkerboard
of heights around that vertex. These four-way contacts belong to
the class; they are not counted as independent bumps.

**PROVED — the actual neighbourhood.** Let M count base faces
incident to at least one boundary edge of D. Then

\[
 |N(S(D))\setminus S(D)|
       \le8A+4k+M-2v_4\le8A+6k-2v_4.                  \tag{R12}
\]

*Proof.* There are `2A+k` horizontal used links: one over every
base edge, and a second exactly at a height change. The v used
vertical links are at the boundary vertices. Count neighbouring
plaquettes by orientation. Horizontal plaquettes contribute A+M:
the actual horizontal sheet plus the other height at a base face
which touches the boundary. Plaquettes in orientations 13 and 23
contribute at most `4A+k`: two height intervals beside a base edge
with one used horizontal link, three if it has both heights.
Any such face meeting a used vertical link is already counted,
because every base edge has a used horizontal link at height zero
or one. Orientations 14 and 24 contribute `4A+2k`, two per used
horizontal link. Orientation 34 contributes 2v. Their sum is at
most `9A+3k+M+2v`. Subtract `A+k`, use (R11), and use M<=2k.
Periodic coincidences can only reduce this count. All these counts
remain valid at period three. QED.

For one isolated elementary bump, k=4, M=5 and v_4=0. Thus
(R12) returns the checked increment 21 in (F19), rather than
charging an independent 21 to every cube in an overlapping patch.

**PROVED — joint Haar payment for the contacts.** In sections
3-5 only, c abbreviates cosh(beta). Put

\[
 c=\cosh\beta,\qquad h=\tfrac12\sinh\beta,\qquad
 t=h c^6,\qquad R=2c^{-2},\qquad q=h c^8.
 \quad u(S(D))\le q^A t^k R^{v_4}.                       \tag{R13}
\]

*Proof.* The SU(2) moment recursion already proved in (F11) also
gives `integral x^4=1/8`. Apply (F10) with exponent two on every
horizontal face and on vertical faces touching no degree-four link.
Use exponent four on each remaining vertical face. At a degree-four
link all four faces have exponent four. At a degree-two link the
sum of reciprocal exponents is at most one. These are precisely
the conditions of (F10).

The factor per exponent-two face is at most h. The exponent-four
factor is at most `sinh(beta) (1/8)^(1/4)=2^(1/4) h`, using
`|sinh(beta x)|<=sinh(beta)|x|`. At most 4v_4 faces need this
larger factor. Thus the Haar integral in (R1) is at most
`h^(A+k) 2^(v_4)`. Multiply by the bound (R12) for the actual
cosh neighbourhood to obtain (R13). No independence between
touching or overlapping defects has been asserted. QED.

**PROVED — the defect polymer representation.** Regard boundary
edges of D as a subgraph of the base square lattice. Its degrees
are zero, two or four. A contour Gamma is a nonempty connected
even subgraph, with connectivity through vertices. Contours are
compatible exactly when their vertex sets are disjoint. Define

\[
 z(\Gamma)=t^{|E(\Gamma)|}R^{v_4(\Gamma)}.
 \qquad
 \sum_{D\subset P}t^{|\partial D|}R^{v_4(\partial D)}
 =2\!\sum_{\substack{\mathcal C\ {
m compatible}\\
                 [\bigcup\mathcal C]=0}}
                         \prod_{\Gamma\in\mathcal C}z(\Gamma).
                                                                  \tag{R14}
\]

The homology condition is zero in the mod-two first homology of
the base torus. It applies to the union, not to each contour.
To check (R14), every boundary decomposes uniquely into connected
even components. Conversely a mod-two cycle bounds base faces
exactly when its homology vanishes. One direct verification cuts
the torus along its two generators, propagates the face label
across edges, and observes that zero cycle boundary gives local
path independence, while the two zero winding parities give global
path independence. The two choices for the first face yield D
and its complement, and these are the only choices. The k and v_4
counts add over vertex-disjoint components. This proves the identity.

This is an exact finite polymer polynomial for the **dressed
majorant**, with the global homology restriction retained. It is
not a factorization of the signed Wilson integrals themselves.
A four-way junction belongs to one contour. Nearby cubes which
cancel their shared walls are represented by the remaining boundary,
so no factor `w^(number of cubes)` is inserted. Wrapping contours,
holes and nested terrace boundaries are included in (R14).

**PROVED — summing this gas at every defect density.** For all
positive t and R, including the values in (R13),

\[
 \sum_{D\subset P}t^{|\partial D|}R^{v_4(\partial D)}
       \le \left(2+12t^4+2t^8R^4\right)^{A/4}.          \tag{R15}
\]

*Proof.* Give the A height bits independent uniform probability
measure. At each base vertex let d be the number of transitions
in its cyclic list of four adjacent heights, and define
`f=t^(d/2) R^(1_{d=4})`. Each boundary edge has two endpoints,
so the product of all these f is exactly `t^k R^(v_4)`.
Every height bit occurs in four such factors, all distinct since
the periods are at least three. Apply the already proved product
inequality (F10), now on these binary probability spaces,
with exponent four on every vertex factor.

Of the sixteen four-bit patterns, two are constant, two alternate,
and the other twelve have two transitions. Therefore

\[
 \mathbb E f^4=\frac{2+12t^4+2t^8R^4}{16}.
\]

There are A vertices. Multiplying their fourth norms, and then
converting the probability average to the sum by multiplying by
`2^A`, proves (R15), because `16^(A/4)=2^A`. No enumeration
run is used: the count is `2+2+(16-4)=16`, with the nonconstant,
nonalternating patterns having precisely two transitions. QED.

**PROVED — a hand constant through beta one-half.** Uniformly for
`0<beta<=1/2`,

\[
 q^4\left(2+12t^4+2t^8R^4\right)<\frac{599}{600}<1.
                                                                  \tag{R16}
\]

Indeed the left side is

\[
 2h^4c^{32}+12h^8c^{56}+32h^{12}c^{72}.
\]

Use the hand bounds `h<4/15`, `log c<=1/8`, and `e<11/4`
from (F14). The three terms are bounded respectively by

\[
 2(11/15)^4<\frac7{12},\qquad
 \frac{48\,11^7}{15^8}<\frac38,\qquad
 \frac{2048\,11^9}{15^{12}}<\frac1{25}.                  \tag{R17}
\]

The integer comparisons, displayed for hand checking, are

\[
 351384<354375,\qquad
 2494357888<2562890625,\qquad
 120726921779200<129746337890625.
\]

They are respectively `24*11^4<7*15^4`,
`128*11^7<15^8`, and `51200*11^9<15^12`.
Finally `7/12+3/8+1/25=599/600`. This proves (R16).

**PROVED — the full terrace-class bound.** Let H be the union of
the classes (R10) over all translates of the horizontal plane
and all four signed transverse directions. Equations (R13)-(R16) give

\[
 B_{\mathcal H}\le4N_\perp(599/600)^{A/4},
                       \qquad 0<\beta\le\tfrac12.        \tag{R18}
\]

Multiple encodings only enlarge the right side. Equation (R2)
then gives an absolute area bound for the fully dressed class.
This includes arbitrary adjacent and overlapping unit-cube
deformations in one fixed direction per surface, at every available
excess, up to 2A. On even base periods, checkerboard D reaches
k=2A and has degree-four vertical links at every base vertex.
No independent-bump multiplication can describe that example.

## 4. Tall separated pillars, including excess beyond order A

**PROVED — the one-step neighbourhood cannot be reused unchanged.**
Lift one base face through L consecutive unit cubes in direction 3,
with every other base face at height zero. Take periods large enough
to prevent coincidences. This pillar has `k=4L`, no branching links,
and

\[
 |N(S)\setminus S|=8A+29L-8.                              \tag{R19}
\]

Here is the count by orientation. The horizontal neighbours number
`A+5L`: the original plane and, at each height 1 through L, the
pillar face and its four horizontal neighbours. The 13 and 23
neighbours number `4A+12L-8`. Horizontal used edges account for
`4A+4L`; the four pillar corners each have two outward faces
at each of the L-1 higher vertical segments, adding `8(L-1)`.
The 14 and 24 neighbours number `4A+8L`, two per horizontal used
edge. The 34 neighbours number 8L. Their sum is `9A+33L-8`;
subtract the surface area `A+4L` to get (R19).

At L=2, the increment is 50, whereas `6k=48`. Thus extending
the binary-height bound (R12) to arbitrary heights would be false.
The count (R19) remains an upper bound if periodic neighbours
coincide. This is a geometric counterexample to that extension,
not a heavy-weight or RTAIL counterexample.

**PROVED — the corrected pillar payment.** Choose vertex-disjoint
base faces. At each, choose any signed transverse direction j and
an integer `1<=L<=n_j-2`, and attach such a pillar. Let P_* be
the union of these surface classes over translated base planes.
Every surface has degree two at its links and area
`A+4 sum L`. All original plane links remain. For several pillars,
union counting of the added neighbourhoods gives

\[
 |N(S)\setminus S|\le8A+\sum(29L-8),\qquad
 u(S)\le q^A\prod w_L,
 \quad w_L=h^{4L}c^{29L-8}=w_1 v^{L-1},
 \quad w_1=h^4c^{21},\quad v=h^4c^{29}.                 \tag{R20}
\]

The projected disjointness prevents shared surface links even when
pillars use different transverse directions. Their neighbourhoods
may overlap; the union bound is still valid. Apply (F10) with
exponent two on every surface face to obtain (R20). The product
on its right is a joint majorant, not an independence assertion.

Dropping the separation condition in the sum of these majorants,
and extending each height sum to all L>=1, gives, if v<1,

\[
 B_{\mathcal P_*}\le N_\perp
       \left[q\left(1+\frac{4w_1}{1-v}\right)\right]^A.   \tag{R21}
\]

**PROVED — hand constants at beta one-half.** The exponential
series estimate used in (F22) gives
`e^(5/8)<=569/304<15/8`. Together with `e<11/4`, `h<4/15`
and `log c<=1/8`, this yields

\[
 w_1< (4/15)^4(11/4)^2(15/8)=\frac{242}{3375},
 \qquad
 v<(4/15)^4(11/4)^3(15/8)=\frac{1331}{6750}<1.
\]

Hence `w_1/(1-v)<484/5419` and

\[
 q\left(1+\frac{4w_1}{1-v}\right)
 <\frac{11}{15}\left(1+\frac{1936}{5419}\right)
 =\frac{80905}{81285}<1,
 \quad
 B_{\mathcal P_*}\le N_\perp(80905/81285)^A,
 \qquad 0<\beta\le\tfrac12.                              \tag{R22}
\]

All inequalities are uniform down to positive beta. For even base
periods, A/4 vertex-disjoint base faces with common height L have
excess LA. Choosing L growing with a gives excess beyond order A.
Only this separated-pillar geometry is covered at those excesses.
The old separated elementary-bump class is the subcase L=1.

## 5. Why a dilute contour expansion does not finish the argument

**READ.** The full-read index `chunk-01.md:118-145` and
`obligations.md:34-48` lead to outline lines 1150-1375. Those
lines were read. Sussman and Alpoge prove the finite-polymer
connected logarithm and rooted-tree bound under the Kotecky-Preiss
criterion. Their words are: "The estimate on the activities remains
a separate analytic task." The result is a proved implication,
not an estimate for these defects. It is reused as such.

**PROVED — that criterion fails for this particular positive
contour majorant at beta=1/2.** For the contour weights in (R14),
even allowing arbitrary nonnegative criterion weights a_Gamma,
the inequalities

\[
 \sum_{\Gamma'\not\sim\Gamma}
            z(\Gamma')e^{a_{\Gamma'}}\le a_\Gamma        \tag{R23}
\]

cannot all hold. This statement concerns the unrestricted contour
gas obtained by dropping the global homology constraint.

*Proof.* Consider only the A elementary square contours. Each
has weight z=t^4, with no degree-four vertex. Exactly nine of
these squares, including itself, share a vertex with a fixed
square. Their lower-left corners differ by -1,0,1 in each base
direction. These nine positions are distinct at all periods at
least three. Sum (R23) over the elementary roots and omit all
other nonnegative terms. Every elementary activity is counted nine
times. With b the average of their criterion weights, Jensen gives

\[
                  9t^4 e^b\le b.                       \tag{R24}
\]

But `b exp(-b)<=1/e` for b>=0, by differentiation. At beta=1/2,
`h>1/4`, `c>9/8`, and `e>8/3`. The first four terms of the
binomial expansion give

\[
 (9/8)^{24}>1+24/8+276/64+2024/512=785/64>12.
\]

Consequently `9e t^4 > 24*12/256 > 1`, contradicting (R24).
This proves the stated failure of every choice of a_Gamma. QED.

**PROVED / OPEN — scope of this obstruction.** It does not say
the true dressed weights are too heavy: z is an upper majorant.
It does not preclude a different contour representation or criterion.
Indeed (R15)-(R18) already sum this entire majorant after retaining
the flat-plane factor q^A. The useful payment is the joint finite
sum, not convergence of a dilute gas of these contours alone.

**PROVED — the other two attempted extensions have explicit limits.**
First, at beta=1/2, q>1/4 and gamma>1. Thus the criterion (R9)
fails already at epsilon=1/8: its label cost is greater than
`(1/8) log(16^4)=log4`, before its positive binomial entropy.
So the all-shape exploration plus (R3) does not control all
positive-density excesses. This is a loss in an upper bound,
not a lower bound on shape entropy or on Wilson weights.

Second, (R19) shows the failure of the binary neighbourhood
budget for height two. The corrected payment suffices for
separated pillars, but no joint local factorization comparable
to (R13)-(R15) is obtained here for arbitrary multilevel surfaces,
two transverse height directions, overhangs or handles. Their
exceptional-link code exists by (R4); the remaining problem is
paying its high-density joint weight. These are distinct failures
of the global code bound, dilute contour criterion, and binary
geometry extension. None refutes RTAIL.

## 6. The enlarged class and the weakest remaining statement

**PROVED — joint class with the original denominator.** Set

\[
 \mathcal G_* =\mathcal A_*\cup\mathcal H\cup\mathcal P_*,
 \qquad
 \tau=\min\left\{\frac1{40},\frac14\log\frac{600}{599},
                              \log\frac{81285}{80905}\right\}>0.
                                                                  \tag{R25}
\]

Use the smallest available majorant on intersections. From (R6),
(R18) and (R22),

\[
 B_{\mathcal G_*}\le6N_\perp e^{-\tau A}
                         \le24a^2e^{-\tau a^2},
 \qquad
 \sum_{S\in\mathcal G_*}|D_m(S)|
                    \le C_0a^2e^{-\tau a^2},
 \quad C_0=24\exp(48/\tau).                              \tag{R26}
\]

For the second inequality use (R2) and
`a^2 exp(-tau a^2)<=1/tau`, which follows from `exp(x)>=x`.
This explicit constant is deliberately loose. All constants are
uniform in the allowed boxes, crossed pairs and `0<beta<=1/2`.

The old class G of (F27) is contained in G_*. Its elementary
bumps are pillars of height one. Also `100 log(2a)>128` for
a>=3: `e^(4/3)<(11/4)(3/2)=33/8<6`, so `log6>4/3>128/100`.
Thus its cutoff K(a) is at most floor(A/128).

Order the old G first, then G_* minus G, then the remaining odd
surfaces O. With Xi and w as in (J2), define

\[
 R_m^*={1\over2Z_m}\int C(U)
       [\Xi(w_m^{\mathcal G_*};U)-\Xi(w_m^{\mathcal O};U)]\,dU.
 \quad p_m(v)=T_m(\mathcal G_*)+R_m^*.                    \tag{R27}
\]

This is exact telescoping. In the marked-family form (F4), the
tail sums families containing at least one surface outside G_*;
the exterior weights in that form are unflipped. Neither the
individual terms nor R_m^* are asserted positive. The read endpoint
inequality p_m(v)>=0 gives

\[
 R_m^*\ge-C_0a^2e^{-\tau a^2},\qquad
 R_m=R_m^*+T_m(\mathcal G_*)-T_m(\mathcal G),
 \quad |T_m(\mathcal G_*)-T_m(\mathcal G)|
                          \le C_0a^2e^{-\tau a^2}.       \tag{R28}
\]

The last bound sums the corresponding subset of D's in (R26).
The earlier class's telescoped sum is independent of its internal
ordering, by (F2). All equalities therefore use the same original
R_m as the requested task.

**OPEN — weakest remaining statement reached.** On one compact
interval `I subset (0,1/2]`, with particular interest in an interval
above 2/9, prove

\[
 R_m^*\le C a^p\eta_*^{a/2}
 \quad\hbox{uniformly for }\beta\in I,
 \ a\ge3,\ c,d\in\{a,2a\},\hbox{ and the crossed pairs}. \tag{RTAIL*}
\]

Here eta_* is the same fixed consumer constant, with `0<eta_*<1`;
`C>0` and `p>=0` are finite and independent of a, beta and the pair.
Only the upper bound is needed. Equations (R26)-(R28) make this
equivalent in strength to the original RTAIL and to (E17), with
changed constants and polynomial power. Explicitly, for
`kappa=(1/2)log(1/eta_*)`,
`-tau a^2+kappa a<=kappa^2/(4tau)`. This absorbs each proved
area bound into the required exponential rate in a.

The missing surfaces have excess greater than A/128 and lie
outside both the one-step-terrace class and the separated-pillar
class. In particular, arbitrary overlapping multilevel defects,
overhangs, handles and two transverse directions at once remain
uncontrolled at positive excess density. The code (R4) handles
their placement; its present joint Haar payment does not sum them.

**PROVED implication / OPEN premise — an available stronger target.**
A bound of the same required rate for
`B_out=sum_(S in O minus G_*) u(S)` would suffice. Applying (F5)
with all odd surfaces gives
`sum_(S outside G_*) |D_m(S)| <= B_out exp(2(B_G_*+B_out))`.
Both B sums would then be uniformly bounded. This route uses no
positivity of the signed tail and no exact independent defect gas.
No such B_out estimate is proved here at beta=1/2, or on any new
full-trace interval above the checked seed. It is stronger than
(RTAIL*) and might require sharper Haar cancellations.

## 7. Groups and the checked seed

**READ / PROVED — group dependence.** The combinatorics and finite
binary-height sum are group independent. The weight estimates use
the central sign, zero Haar mean, `|x|<=1`, and the moments
`E x^2=1/4`, `E x^4=1/8`, `E x^6=5/64`. The finite subgroup
moment statement in `gap-flat-check-opus.md` section 7, with its
credited (G12) source, supplies the same moments for the binary
icosahedral group. For the fourth moment specifically, its printed
class values give
`[2+40/16+24*(7/16)]/120=1/8`. For its trace pair
`c_+=(1+sqrt(5))/4`, `c_-=(1-sqrt(5))/4`, the squared values
have sum 3/4 and product 1/16. Hence `c_+^4+c_-^4=7/16`.
Thus every new class bound here is group-blind between SU(2) and
that finite group. No degree-twelve distinction or Lie-algebra
transport enters the proof.

For U(1), the second moment is 1/2, and the fourth is 3/8.
For example `cos^2(theta)=(1+cos(2theta))/2` gives the former;
squaring and averaging gives the latter. The factors h and the
branching payment therefore change. The SU(2) constants (R3),
(R16) and (R22) do not transfer unchanged. No U(1) Coulomb-phase
conclusion is claimed. At weak coupling even the SU(2)/finite-group
flat majorant fails: `q(beta)>=sinh(beta)/2>1` for beta>=2.
This is a named failure before any weak-coupling conclusion could
be drawn for either control group or for SU(2).

**READ — existing seed, not recomputed.** Theorem DOB in
`gap-vmf-lip.md:419-594` gives the full excited transfer sum
`S(a;(2a)^3;beta)<1/1650` for sufficiently large a at each fixed
`0<beta<2/9`, and its stated lattice-gap consequence, given the
inherited transfer and shape results. Its checker,
`gap-vmf-lip-check-opus.md:92-125`, confirms both flux sectors
and the stated range. Credit its Codex author and Claude Opus 5.5
checker. These source ranges were read; this note does not check
the inherited transfer construction anew.

**PROVED implication / OPEN continuation.** All the present bounds
retain the seed's original Wilson normalization. If (RTAIL*) is
proved on I, (R27) gives (E17) for the crossed odd-sector ratios.
The consumer `gap-expose-astra.md:574-599` then supplies its flux
criterion: `8 Q_F <= K(a) sqrt(S_ev(a))`, with
`K(a)=8 C a^p`, using the existing `S_ev>=eta_*^a`; also
`Q_F<1/192` for sufficiently large a. This is the precise input
that could be combined with the checked seed and the lane's
continuation argument. This note supplies only the class part of
that input. It does not extend the full seed beyond 2/9, nor turn
the seed at one coupling into a seed at another by addition.

## 8. Source and verification boundary

**READ.** The CA-I 4.12-4.19 index and the outline obligations were
searched for the target's wrapping-surface, vortex, excess-area,
Peierls and defect-contour terms; no supplier was located. The
CA-full index was also consulted. CA-I 2698-2716 was read at the
source: its list of things not asserted includes a mass gap. The
outline's complete combinatorial polymer proof at 1150-1375 is
used with its activity hypothesis, as section 5 specifies. These
are bounded retrieval conclusions, not an absence theorem about
the complete account. No Balaban paper or computed result is a
premise of this note. Credit Sussman, Alpoge, Claude and Codex
as stated above; credit Kotecky and Preiss for the criterion.

**READ — methodology.** The current main workflow map, RULES,
SETTINGS and research procedure were read via git show. The map
now points old physics-loop entries to that procedure. The pinned
worker dispatch controls this one-file output. Planning-branch
AGENTS was read without checkout changes. No planning file,
registry, audit, queue, main science file or public post was changed.

**READ — verification scope.** All new mathematical work is written
by hand. No numerical run, machine enumeration or computer-assisted
certificate was used. The author completed a full self-read,
including the decoder, exception counts, neighbourhood counts,
Haar exponents, contour homology restriction, rational inequalities
and signed telescoping. This is not an independent check. Mechanical
checks cover only file structure and source identity; their final
record is `/tmp/sa-gap-rtail-astra.pnYcWb/file-checks.json`.
No mathematical verdict rests on that script.

**PROVED / OPEN — delivery.** The three class bounds (R6), (R18),
(R22), their joint consequence (R26), and the restricted criterion
failure (R23)-(R24) are author proofs, not yet independently checked.
The full signed tail (RTAIL*) is open. Only this output file was
written in the checkout. It is uncommitted and unpushed on
`research/gap-rtail-astra-20261112`, based on the requested pin.
The next proof obligation is (RTAIL*) for the complementary
positive-density class; another dilute use of (R23) cannot supply
it at beta=1/2 with these activities.

RESULT: PARTIAL — at every 0<beta<=1/2, hand proofs give absolute area bounds with the original Z_m for all wrapping shapes of excess at most A/128, all one-step terraces in a fixed transverse direction, including overlapping bumps and four-way contacts, and all separated pillars of admissible height, including excess beyond order A. The encoding removes the transverse-position log(a) loss; a finite defect-contour sum controls the terrace class. These bounds are group-blind for the binary icosahedral group. General RTAIL remains open; no true-weight heavy-defect lower bound, new full seed above beta<2/9, or scientific status is claimed. Not independently checked.
