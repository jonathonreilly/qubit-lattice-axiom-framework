# Repo search

**READ.** The checkout is pinned at `212b961a13aa6fb2e4bf39db0e06830873ee8099`.
There is no `prior/gap-flat-astra.md`. The lead's
`prior/repo-search-2026-11-08.md` was read in full. It searches main
and PRs 10114, 10133, 10134 and 10141 for earlier RG targets. It
does not report a search of this later almost-flat-surface target.
Its closest relevant hits are the soft-route local transfer comparison
and the warnings about keeping a common reference.

**READ.** PR 10114 was fetched at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`. In its folder
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`, I read
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–166`, `RD3.md:565–575` and
`RD4.md:448–460,687–694`. Credit their Codex authors. They retain
the exterior kernel, require the same reference, and require actual
overlap factorization. They do not bound the present wrapping class.
Current main, `bb4ec020d5ada57c630dd89acc98a68397ade423`, was searched
for almost-flat, excess-area, dressed-surface, odd-sector-trace and
wrapping-surface terms. These are retrieval checks, not an absence theorem.
The three main hits were screened at their source: a one-qubit
environment cost (`docs/NATIVE_ENVIRONMENT_COST_NOTE_2026-10-18.md:1–28`),
a fitted mass-response plot (`docs/ASYMMETRY_PERSISTENCE_MASS_SCALING_NOTE.md:41–60`),
and a Regge worldvolume route table (the August 10 admissibility-cut
note in the September 8 backlog provenance folder, lines 598–611).
None concerns the Wilson surface sum. The local targeted follow-up
found only row 811's proposed almost-flat class and an unrelated
bounded excess *free energy* in `gap-crux-restate.md`.

**READ.** The close local sources are `gap-joint-astra.md` (read whole),
`gap-block-astra.md` sections 6–7, and `gap-kappa-order.md:31–74`.
Credit Codex gpt-6-astra for (J4), (J12), and (B32), and Claude
Fable 5.2 for Proposition SC and its area lemma. These are reused.
The row-816 check is absent at the pinned commit. Searches of
`open-registry.md`, `open-core.md` and `l17c.md` found no other
owner under the specific almost-flat, excess-area, J12 or E17 terms.
This work is FINISH row 817; it does not take over row 816.

# Almost-flat wrapping surfaces with their decorations

Author: **Codex gpt-6-astra max**, 2026-11-12, FINISH row 817.
Research text, not an audit; this grants no scientific status.
**PROVED** labels a hand proof here, not an independent check.
**READ**, **ARGUED**, **GUIDE**, and **OPEN** retain their literal meanings.
Definitions are labelled with their surrounding statements.

**READ.** Credit **Ethan Sussman and Levent Alpoge, with Claude and
Codex as the authors of their text**, for the finite-polymer and
Wilson-convolution machinery. Index lookup preceded bounded source
reads. Their outline and complete account I at `31a47c543775` were
downloaded once each to the new directory
`/tmp/sa-gap-flat-astra.03F6tg/`. No download enters the checkout.
The outline's 1150–1375 proves its combinatorial convergence theorem
while leaving activity estimates separate. Its 2195–2244 and
2313–2381 supply (GL3), (GL4), (GL8), (GL10). CA-I 2698–2716
explicitly excludes a mass gap from the asserted theorem. No indexed
almost-flat vortex estimate was located. No Balaban result is used.

## Checkpoint

**PROVED / OPEN — final checkpoint.** (F4) and (F6) retain all
decorations and the original denominator. Jensen and product Haar
Hölder estimates prove (F17)–(F18) for every surface with excess
at most `A/(100 log(2a))`, and (F21)–(F23) for separated cube
bumps even at positive excess density, uniformly at `beta<=1/2`.
The general tail (RTAIL) remains open there. Three failed extensions
and their missing inputs are in section 6; no class-heavy lower
bound is claimed. Full summation works here at `beta<=1/500`,
which is weaker than the existing full-seed range. The next decision
is a contour bound for overlapping deformations. Sources and open
obligations are recorded in this note. No independent check or
scientific-status change is claimed.

## 1. Setting and exact class resummation

**READ.** Use (J1)–(J4) of `gap-joint-astra.md`. Periods are
`n=(a,a,c,d)`, `a>=3`, `c,d in {a,2a}`. Fix a temporal pair `(r,i)`
and its twist `v`. Put `A=n_r n_i`, `N_perp=prod_(j notin {r,i}) n_j`,
and `N_p=6a^2cd`. Thus `a^2<=A<=4a^2`, `N_perp<=4a^2`,
`N_p<=24a^4`. Spatial `m` is one of the consumer's crossed pairs.
Write `Z_m=int prod_p exp(beta eta_(m,p)x_p) dU`, with
`x_p=tr(U_p)/2`. The harmless common action constant is omitted.

**PROVED — definitions and exact grouping (F1).** Let `O` be the
link-connected closed mod-two surfaces with `v(S)=1`. Branchings
and singular vertices are allowed. The area lemma gives `|S|>=A`.
Define the excess `k(S)=|S|-A` and, for any integer `K>=0`,

\[
 \mathcal A_K=\{S\in\mathcal O:k(S)\le K\}.                 \tag{F1}
\]

This includes every flat plane and every bump, handle or branching
with the stated total excess. It does not impose a small footprint:
a broad terrace with small boundary also belongs when its excess fits.
It can include other topology. This enlargement is intentional.

Use `C,w_m,Xi` from (J2). For a class `F subset O`, let `w^F` change
the signs of exactly its polymer variables. Order F before its
complement in (J4), and define

\[
 T_m(F)=\sum_{S\in F}D_m(S)
       ={1\over2Z_m}\int C[\Xi(w_m)-\Xi(w_m^F)]\,dU.       \tag{F2}
\]

The first equality follows by telescoping exactly the first block
of sign changes. This is a signed contribution, not a probability.
Changing the order inside F leaves its sum unchanged.

For a nonempty compatible marked family `H subset O`, put
`Q=union_(S in H) S`, and define

\[
 W_m(H)={1\over Z_m}\int C\prod_{S\in H}w_m(S)\,
             \Xi_{\mathrm{comp}(H)}(w_m)\,dU .             \tag{F3}
\]

The exterior weights here are unflipped. Multiaffinity gives

\[
 T_m(F)=\sum_{\substack{\varnothing\ne H\subset F\\H\ {m compatible}}}
              (-1)^{|H|+1}2^{|H|-1}W_m(H).               \tag{F4}
\]

Indeed substitute `w(S)-2w(S)` at each variable in F and expand.
Choosing the `-2w(S)` part marks S; the residual polynomial excludes
every polymer incompatible with a mark. This also proves, for the
first-block ordering,

\[
 D_m(S)=\sum_{\substack{H\subset F_{<S}\\H\cup\{S\}\ {m compatible}}}
                (-2)^{|H|}W_m(H\cup\{S\}).               \tag{F5}
\]

All sums are finite. Integer spins, attached decorations and all
compatible unmarked parity surfaces remain inside each W, against
the original `Z_m`. No cluster convergence assumption is made.

## 2. Removing the exterior without changing the denominator

**PROVED — local comparison (F6).** Let `E(Q)` be the set of links
of the marked surfaces, `N(Q)` all faces touching those links,
and `P_far=P\\N(Q)`. The sign-change argument of Proposition SC
gives the following exact version of (J14):

\[
 Z_m W_m(H)=\int
  \prod_{p\in Q}\sinh(\beta\eta_{m,p}x_p)
  \prod_{p\in N(Q)\setminus Q}\cosh(\beta x_p)
  \prod_{p\in P_{\rm far}}e^{\beta\eta_{m,p}x_p}\,dU.      \tag{F6}
\]

Expand the far exponential into sinh and cosh. As Q is closed,
only closed far parity sets survive link sign averaging. Their
components are exactly the polymers compatible with H in (F3).
This proves the identity with all signs retained.

Let `Z_far,m` be the integral of the last product in (F6).
At any fixed exterior to `E(Q)`, every face in N(Q) contains a
Haar link integrated exactly once in its plaquette word. Therefore
its mean `x_p` is zero. Jensen's inequality, applied to the whole
sum of removed actions, yields

\[
 \int dU_{E(Q)}\exp\!\left(\beta\sum_{p\in N(Q)}
                          \eta_{m,p}x_p\right)\ge1,
 \qquad Z_m\ge Z_{{\rm far},m}>0.                        \tag{F7}
\]

This is a lower bound on the actual denominator. It neither replaces
it by a product vacuum nor requires positivity of the marked integral.
Periods at least three ensure distinct links in each face word.

For each surface S, every used link has degree at least two.
There are at most `2|S|` such links and six plaquettes at a link.
Counting the outside incidences gives
`|N(S)\\S|<=6(2|S|)-4|S|=8|S|`. For compatible H, the same
argument gives `|N(Q)\\Q|<=8|Q|`. Also
`|N(Q)\\Q|<=sum_(S in H)|N(S)\\S|`. Since different marks share
no links, (F6), (F7), and `cosh(beta x)<=cosh(beta)` imply

\[
 |W_m(H)|\le\prod_{S\in H} u(S),\qquad
 u(S)=(\cosh\beta)^{|N(S)\setminus S|}
           \int dU_{E(S)}\prod_{p\in S}|\sinh(\beta x_p)|. \tag{F8}
\]

The far integral factors after the displayed pointwise bound and
cancels by (F7). Hence (F8) is uniform in volume, twist and shape.
The exponent can always be enlarged to `8|S|`; retaining the actual
neighbourhood will improve the bump estimate in section 5.

**PROVED — class bound (F9).** Any positive majorants `b(S)>=u(S)`
give, with `B_F=sum_(S in F)b(S)`,

\[
 |T_m(F)|\le{e^{2B_F}-1\over2},\qquad
 \sum_{S\in F}|D_m(S)|\le B_F e^{2B_F}.                  \tag{F9}
\]

For the first inequality use (F4), drop incompatibility and bound
the k-mark sum by `B_F^k/k!`. For the second use (F5), bound
the sum over earlier marks by `prod_(T in F)(1+2b(T))<=e^{2B_F}`,
and sum `b(S)`. No positivity of an intermediate polynomial is used.

## 3. Haar moments pay area, including a controlled branching cost

**PROVED — the product estimate (F10).** Suppose nonnegative functions
`f_p` depend on independent link variables. Choose `h_p>=1` such that
`sum_(p containing e)1/h_p<=1` at every link. Then

\[
 \int\prod_p f_p\le\prod_p\left(\int f_p^{h_p}\right)^{1/h_p}.
                                                                  \tag{F10}
\]

To prove this, integrate one link. Apply Hölder to the incident
factors with exponents h_p, inserting a constant factor when their
reciprocals sum to less than one. Replace each incident function
by its conditional h_p norm. Repeat for the remaining links.
Taking the h_p power at the next integration cancels the previous
root. Fubini leaves exactly the full h_p norm on the right.
All measures are probability measures and all functions here are bounded.

**PROVED — the required SU(2) moments.** For `x=tr U/2`, Haar
measure has density `(2/pi)sqrt(1-x^2)` on `[-1,1]`. If
`M_l=int x^(2l)dU`, integrating the derivative of
`x^(2l-1)(1-x^2)^(3/2)` gives
`(2l+2)M_l=(2l-1)M_(l-1)`. Thus

\[
 \int x^2={1\over4},\qquad \int x^6={5\over64},\qquad
              (5/64)^{1/6}<2/3.                         \tag{F11}
\]

The last inequality is `3645<4096`. Convexity on `[0,1]` gives
`|sinh(beta x)|<=|x|sinh(beta)`.

**PROVED — excess controls the number of branching faces (F12).**
Call a face bad if it touches a link of S with degree four or six.
At a link, at most two faces have orientation `(r,i)`. Thus each
branching link touches a nonhorizontal face. If V is the number
of nonhorizontal faces, there are at most `4V` such links and
at most `8V` bad horizontal faces. Adding the nonhorizontal faces
bounds the total bad faces by `9V`. The area lemma counts at
least A horizontal faces, so `V<=k(S)` and

\[
 B(S):=\#\{\hbox{bad faces}\}\le\min(9k(S),|S|).          \tag{F12}
\]

Use `h_p=2` on good faces and `h_p=6` on bad ones in (F10).
At a branching link every incident face is bad. At every other
used link there are exactly two faces. These choices therefore
satisfy (F10), including at singular vertices. Equations (F8)–(F12)
give the explicit majorant

\[
 u(S)\le q(\beta)^{|S|}(4/3)^{B(S)}
       \le q(\beta)^{A+k(S)}\gamma^{k(S)},\quad
 q(\beta)={\sinh\beta\over2}(\cosh\beta)^8,
 \quad\gamma=(4/3)^9<16.                                \tag{F13}
\]

Also `u(S)<=q_6(beta)^|S|`, where
`q_6=(5/64)^(1/6)sinh(beta)(cosh(beta))^8`.
No spin-network sign or transfer-operator comparison enters this estimate.
For surfaces with no branching links, the factor gamma is absent.

**PROVED — order-one constants by hand (F14).** Uniformly for
`0<=beta<=1/2`,

\[
 q(\beta)<11/15<e^{-1/4},\qquad q_6(\beta)<44/45<1.       \tag{F14}
\]

Here `log cosh t<=t^2/2`, since its derivative is `tanh t<=t`.
Also `sinh(1/2)<8/15`: after the term `1/48`, the successive
ratios of its series are at most `1/80`, so
`sinh(1/2)<=1/2+(1/48)/(1-1/80)<8/15`.
The exponential series gives `e<11/4`; for example its tail from
`1/4!` is at most `(1/24)/(1-1/5)=5/96`.
Thus `q<(4/15)e<11/15` and `q_6<(2/3)(8/15)e<44/45`.
Finally `e^(1/4)<=4/3<15/11` by its geometric-series majorant.
No decimal evaluation is used.

**PROVED — dressed flat planes (F15).** For the class `F=A_0`
of translated flat planes, `B_F<=N_perp q^A`. Hence

\[
 \sum_{S\in\mathcal A_0}|D_m(S)|
       \le N_\perp q^A\exp(2N_\perp q^A).               \tag{F15}
\]

This is a full-normalization upper bound, for this class-first
ordering. It does not assert `D_m(S)<=r_(1/2)^A`.
The bare weight `r_(1/2)^A` in (B32) and the dressed lower
bound (J13) are compatible with (F15). No part of (J13)'s
positive-transfer proof is needed here.

## 4. All bounded-excess shapes, without a footprint assumption

**PROVED — a shape count (F16).** For integers `0<=K<A`,

\[
 |\mathcal A_K|\le (N_\perp+1)
               \sum_{v=0}^K4^v\binom{N_p}{v}
       \le(N_\perp+1)(K+1)(4N_p)^K.                    \tag{F16}
\]

Choose the v nonhorizontal faces first; `v<=K` by the area lemma.
In a fixed transverse slice, the boundary of the remaining
horizontal two-chain is now prescribed. Two solutions differ by
a horizontal two-cycle. Such a cycle is empty or the whole plane:
at each link its two adjacent faces have the same coefficient,
and these equalities propagate around the connected two-torus.
There are therefore at most two solutions on each affected slice.

A nonhorizontal face has horizontal boundary links in at most two
transverse slices. At most `2v` slices are affected. On every other
slice the horizontal set is empty or a full plane. Since
`|S|<=A+K<2A`, at most one unaffected full plane can be present.
There are at most `N_perp+1` ways to choose it, including none.
This gives `2^(2v)(N_perp+1)` completions. Closure in the other
directions, connectivity and the required odd pairing only reduce
the count. Summing over the chosen nonhorizontal sets proves (F16).

**PROVED — bounded-excess class theorem (F17).** For `0<beta<=1/2`,
`0<=K<A`, and the ordering with `A_K` first, put

\[
 U_K=(N_\perp+1)(K+1)(4N_p\gamma)^K(11/15)^A.
 \quad
 \sum_{S\in\mathcal A_K}|D_m(S)|\le U_K e^{2U_K}.        \tag{F17}
\]

Indeed (F13), `q<1`, and (F16) bound `B_(A_K)` by U_K;
then use (F9). For every fixed K this is polynomial times
exponential decay in A, uniformly in beta and m and in the
allowed geometries with `A>K`.
It includes all handles and branchings allowed by the excess bound,
not just isolated elementary bumps.

There is a growing range as well. Set

\[
 K(a)=\left\lfloor{A\over100\log(2a)}\right\rfloor.
 \qquad U_{K(a)}\le25a^4e^{-7A/40}.                     \tag{F18}
\]

To check it, `96 gamma<2048=2^11` and `a>=3` imply
`log(96 gamma a^4)<=4 log(2a)+7 log 2<=(15/2)log(2a)`.
Thus the K-dependent factor costs at most `exp(3A/40)`.
The area factor is at most `exp(-A/4)` by (F14).
Also `(N_perp+1)(K+1)<=25a^4`, since `K<=A<=4a^2`.
This proves (F18), including when the floor is zero.

The right side of (F18) has a finite supremum over `a>=3`.
For example the elementary exponential series bounds any fixed
power of a by a constant times `exp(A/80)`. Hence the factor
`exp(2U_K)` is uniformly bounded, and (F17) is area-small.
The sum for any chosen root is no larger than the displayed full
class sum. This proves the class's part of (J12), with any fixed
required rate in a after enlarging its constant.

**ARGUED — limit of this count.** For `K=epsilon A`, (F16) costs
`exp(O(epsilon A log a))`. It cannot prove a fixed positive-density
window from (F13). This is a loss in this encoding, not a lower
bound on the true entropy. Broad terraces explain why replacing
excess by the number of changed faces would also be unjustified.

## 5. A positive-density bump family is also small at beta one-half

**PROVED — elementary bumps with all their decorations (F19).**
Fix a translated flat `(r,i)` plane P. Choose base plaquettes
which share no vertices with each other. At each chosen face,
choose one of the four signed transverse directions. Replace
the base face by the other five faces of its adjacent cube.
Call the resulting family of surfaces `B(P)`, including P itself.
Every such surface is an embedded torus with degree two at its
links. With b bumps, `|S|=A+4b`.

There is a better neighbourhood count than `8|S|` here:

\[
                  |N(S)\setminus S|\le8A+21b.            \tag{F19}
\]

Here is the local count, including its constants. All original
plane links remain, since every base edge also borders an unremoved
plane face. A bump adds four top edges and four transverse edges.
Outside `N(P)`, the new neighbourhood has at most 25 plaquettes:
the top horizontal face and its four horizontal neighbours (5),
the four faces continuing from the top edges in the bump direction
(4), the eight top-edge faces in the other transverse direction
(8), and the eight faces in both transverse directions meeting
the new transverse edges (8). The other mixed faces at those
transverse edges already touch original plane links and lie in `N(P)`.
These cases exhaust the six faces at each new edge.

Thus `|N(S)|<=9A+25b`. Subtract `A+4b` to obtain (F19).
Periodic coincidences only lower the count. The disjoint-vertex
condition ensures all added links are distinct and each has degree two.
For several bumps, union counting gives the same upper bound even
when their neighbourhoods overlap.

Set

\[
 h={\sinh\beta\over2},\qquad q=h(\cosh\beta)^8,
 \qquad w=h^4(\cosh\beta)^{21}.                         \tag{F20}
\]

The proof of (F8), now using (F19), gives the majorant
`b(S)=q^A w^b`. The same product majorant holds for compatible
marked families. All decorations are still present in W.
Dropping the restriction between base faces only enlarges the
encoding sum. Consequently, for `B=union_P B(P)`,

\[
 B_{\mathcal B}\le N_\perp q^A(1+4w)^A
                =N_\perp\rho_{\rm bump}^A,
 \qquad \rho_{\rm bump}=q(1+4w)<1
                \quad(0<\beta\le1/2).                 \tag{F21}
\]

Multiple encodings of a surface cause only overcounting. The four
choices are its signed transverse directions, not spin labels.

For a wholly rational upper bound on the last inequality, (F14)
gives `h<4/15`, and
`cosh(1/2)^21<=e^(21/8)<16`. To check the latter, the exponential
tail estimate
`e^x<=1+x+x^2/[2(1-x/3)]`, valid for `0<=x<3`, gives
`e^(5/8)<=569/304<2`. Together with `e<11/4`, it gives
`e^(21/8)=e^2 e^(5/8)<121/8<16`. Therefore

\[
 w<{4096\over50625},\qquad
 \rho_{\rm bump}<{11\over15}
       \left(1+{16384\over50625}\right)
       ={737099\over759375}<1.                         \tag{F22}
\]

This pays the bump entropy, after its attached decorations have
been summed. It allows b proportional to A: on even base periods,
the faces at even-even base sites give `A/4` disjoint-vertex choices.
Taking them all has excess A. Thus excess of order A by itself
does not force the class to be too heavy.

**PROVED — one combined resummed class.** Put
`G_K=A_K union B` and order this union first. Choose the smaller
available majorant for surfaces in the intersection. Then (F9)
applies with

\[
 B_{\mathcal G_K}\le U_K+N_\perp\rho_{\rm bump}^A.        \tag{F23}
\]

For fixed K, or for K(a) in (F18), the right side is bounded
and area-small, uniformly at `0<beta<=1/2`. This gives an exact
class containing every bounded-excess almost-flat surface and a
family with positive excess density. Its rooted absolute sum is
area-small. A lower bound showing this particular class is too
heavy at beta one-half is excluded by this upper bound.

**READ / PROVED — the bare weights are smaller, but are different
objects.** The sewing calculation in (B32) gives `r_(1/2)^(A+4b)`
for the fundamental-spin term on a b-bump torus. Each bump costs
`r_(1/2)^4`; an orientable handle also supplies the Euler factor
`2^(-2)` when all face spins remain one-half. This follows from
the same face, edge and vertex factors, `d^(F-E+V) r^F`, used
in the cited torus calculation. It is not a positivity assertion
about the other spin assignments.

The read coefficient bound (GL4) gives `r_(1/2)<=beta/4<=1/8`.
Even allowing all four bump choices independently, the bare sum
is at most `N_perp[r_(1/2)(1+4r_(1/2)^4)]^A`, which is less
than `N_perp(1/4)^A` at beta one-half. This familiar bare
calculation cannot be used as a dressed bound. Equations (F19)–(F23)
are what supply the missing normalization and decoration control
for the specified bump family.

## 6. The general excess tail: a small-beta bound and the remaining failure

**PROVED — a group-blind complete bound (F24).** Discarding the
Haar-moment gain in (F8) gives, at every beta,

\[
 u(S)\le t_0^{|S|},\qquad
 t_0=\sinh\beta(\cosh\beta)^8,\qquad \rho=400t_0.        \tag{F24}
\]

Use the connected-set count already proved in (B30): at most
`N_p 400^(n-1)` connected n-face sets. If `rho<1`, write

\[
 B_{\rm all}\le {N_p\over400}{\rho^A\over1-\rho},\qquad
 B_{\ge L}\le {N_p\over400}{\rho^{A+L}\over1-\rho}.       \tag{F25}
\]

These bounds sum the majorants over all odd surfaces, and over
those with excess at least the integer L. Formula (F5), now with
F equal to all odd surfaces, holds for any ordering. Therefore

\[
 \sum_{S:k(S)\ge L}|D_m(S)|
          \le B_{\ge L}e^{2B_{\rm all}}.                \tag{F26}
\]

This is a genuine excess-area bound for the whole remainder in
its stated range. It includes handles, branchings and all decorations.

An explicit sufficient range is `0<beta<=1/500`. Indeed
`sinh beta<=beta cosh beta` and `log cosh beta<=beta^2/2` give
`rho<=400 beta exp(9 beta^2/2)<9/10` there. For the last
inequality, `9/(2*500^2)<1/9` and `e^x<=1/(1-x)` give the
factor `e^(9/(2*500^2))<9/8`. The area bound in (F25) makes
`B_all` uniformly bounded over the allowed aspect ratios.
Taking `L=0` proves (J12) and hence (E17) on each compact
positive interval contained in this small-beta range.
Taking `L=ceil(epsilon A)` gives the additional `rho^L` payment
for the positive-density excess tail.

**READ — relation to prior ranges.** This elementary marked-family
argument widens row 811's displayed `beta<=1/2400` area-bound
range. It does not improve the repository's full-seed range:
Theorem DOB in `gap-vmf-lip.md:419–467` already gives the seed
for `beta<2/9` by a different method. No order-one full seed is
inferred from (F26).

**ARGUED / OPEN — why the order-one remainder is not bounded.**
At beta one-half, three different bounds leave concrete deficits:

1. **Counting nonhorizontal defects.** The complete reconstruction
   count (F16) works at fixed excess and at (F18). For
   `K=epsilon A`, it charges arbitrary transverse locations to each
   defect and loses `exp(O(epsilon A log a))`. A connected contour
   encoding with only exponential cost in the defects is missing.
2. **Counting arbitrary connected surfaces.** The volume-free
   analytic estimate exists: (F13), or `q_6^|S|`. But neither pays
   the connected-set count 400. In fact `sinh(1/2)>1/2` implies
   `400q(1/2)>100`, already before adding the branching penalty.
   The series used in (F25) therefore gives no decaying tail.
   An upper estimate exceeding one is not a heavy-surface lower bound.
3. **Local geometric surgery.** Keeping the actual neighbourhood
   cost, rather than `8|S|` for every increment, succeeds for the
   complete separated-cube class in section 5. A general surface
   need not admit those disjoint surgeries. Adjacent plateaux,
   handles and branching networks can share links. Their counts
   and neighbourhood gains cannot be multiplied as `w^b` by the
   argument given. The bounded-excess theorem covers them only
   up to K(a); no all-density surgery decomposition is proved.

No failed route here rules out a more accurate contour sum or
signed cancellation in the remaining low-spin surfaces. The bare
Euler factors in section 5 do not control attached integer spins.
The high-spin and commutator routes already tested in row 811 are
not repeated, and no new conclusion is extracted from their failures.

## 7. Binding control groups

**PROVED / READ — which steps distinguish groups.** The exact
identities (F2)–(F7), the exterior comparison (F8), and the
small-beta proof (F24)–(F26) use only a central sign, Haar
invariance, zero Haar mean for x, and `|x|<=1`. They are
group-blind: they apply to Wilson U(1) with `x=cos theta`, and
to the binary icosahedral subgroup in its defining representation.

The moments in (F11) use SU(2). However, they still do not
distinguish SU(2) from the binary icosahedral group. Lemma 2,
(G12)–(G13), of `gap-tree-astra.md:288–346` was read here and
is credited to its Codex author. It proves equality of their
unweighted Haar tensors through degree eleven. Taking traces
gives equality of the moments of x through degree six. Thus
the entire bound for `G_K`, including (F22), also holds for that
finite group at `beta<=1/2`. Its proof inserts no degree-twelve
filter and uses no small noncommuting Lie-algebra directions.

For U(1), `int cos^2 theta=1/2`, not `1/4`, so the factor 1/2
per good face in (F13) becomes `1/sqrt(2)`. The SU(2) constants
(F14) and (F22) do not transfer with the same proof. This is
an exact change of a moment, not a confinement test at beta one-half.

**PROVED — named failure at weak coupling.** The full-surface
proof for either control stops at **`rho=400 sinh(beta) cosh(beta)^8<1`
in (F25)**. This condition fails already at `beta=1/2` and
continues to fail at larger beta. Even the nearly-flat payment
`q<1` fails for SU(2) and Gamma when `beta>=2`, since
`q>sinh(beta)/2>beta/2>=1`. The U(1) version is larger.
Thus these estimates yield no weak-coupling (E17) for either
control, and also no weak-coupling conclusion for SU(2).
The successful small-beta range is shared by the controls.

**READ — scope of the Coulomb test.** The lane's
`prior/gap-lit-u1.md` records the sufficiently-large-beta
Fröhlich–Spencer result, with the printed Villain proof, the
claimed Wilson extension, and a separate periodic-torus issue.
That literature is context, not an input of this note. No numerical
transition value is used and no infinite-volume loop result is
silently substituted for the exact torus trace ratio. The failure
at (F25) occurs before any such transfer could be invoked.

## 8. Weakest sufficient statement left and final checkpoint

**PROVED — exact remainder (F27).** Choose `K=K(a)` from (F18),
put `G=G_K` first, and set

\[
 R_m={1\over2Z_m}\int C[\Xi(w_m^{\mathcal G})-
                                \Xi(w_m^{\mathcal O})]\,dU,
 \qquad p_m(v)=T_m(\mathcal G)+R_m.                     \tag{F27}
\]

Equivalently, R_m is the sum in (F4) over compatible marked
families containing at least one surface outside G. All decorations
and the signs of the earlier class stay in that exact expression.
In particular the remainder is not asserted to be a positive gas.

By (F18), (F22), (F23), and (F9), there are absolute `C_0,tau>0`
such that, uniformly for `0<beta<=1/2` and the admissible pairs,

\[
 \sum_{S\in\mathcal G}|D_m(S)|\le C_0a^4e^{-\tau a^2},
 \qquad R_m\ge-C_0a^4e^{-\tau a^2}.                    \tag{F28}
\]

For example choose
`tau=min(7/40,log(759375/737099))`. The bound for `B_G` is
`29a^4 exp(-tau a^2)`; its finite supremum supplies the constant
in (F9). The lower bound for R_m follows from `p_m(v)>=0`.

**OPEN — RTAIL, the weakest remaining estimate used here.** On
one compact interval `I subset (0,1/2]`, for example `[1/4,1/2]`,
prove constants C,p independent of a, beta, aspect ratio and
crossed pair such that

\[
       R_m\le C a^p\eta_*^{a/2},\qquad\beta\in I,        \tag{RTAIL}
\]

where eta_* is the consumer's fixed witness constant. Only an
upper bound is required. Together with (F28) it implies (E17).
Conversely (E17) implies this upper bound, with a changed constant
and polynomial power, because (F28) controls the removed class.
Thus RTAIL has the strength of the remaining signed trace problem;
it is not a claimed easier theorem. A rooted absolute bound for
the remaining D's would suffice but is stronger than necessary.

To verify the comparison of rates explicitly, for any fixed
`kappa>0`, `-tau a^2+kappa a<=kappa^2/(4tau)`.
Therefore the class bound in (F28) beats `exp(-kappa a)` with
a uniform constant. Take `kappa=(1/2)log(1/eta_*)`.

**ARGUED — next decision.** The flat planes, bounded-excess
handles and branchings, and separated elementary bumps do not
cause a large absolute class sum at beta one-half. The next useful
producer is an excess-contour encoding and a joint bound for
overlapping low-spin deformations, with the actual neighbourhood
or cancellations retained. The scalar (RTAIL) identifies exactly
what it must deliver. It must cover excess between K(a) and
positive density, as well as the general order-A and larger tail.
No new task ownership or scientific status is assigned here.

**READ — verification and delivery.** Every new mathematical bound
above is a hand argument. No numerical run, enumeration, interval
certificate or computer-assisted proof was used. The source and
file checks are mechanical only. Display delimiters, equation tags,
the single final RESULT line and file hygiene passed text checks;
the log is `/tmp/sa-gap-flat-astra.03F6tg/file-checks.txt`.
The full file diff was read. The author checked the marked-family
coefficients, the direction of Jensen's comparison, the link
degrees in Hölder, the horizontal-slice count, and the 25-face
bump neighbourhood. This is not an independent check.
The pinned row-816 report was unavailable; no claim depends on
its outcome or on (J13)'s positive-transfer lower bound.

**READ — instruction boundary.** Platform skill instructions caused
one methodology read outside the requested source roots:
`/Users/jonBridger/.codex/skills/physics-loop/SKILL.md`. Current
methodology was then read from `origin/main` without checkout changes.
Scientific-source searches stayed within the specified source scope.

Only `library/gap-flat-astra.md` was changed. It is local,
uncommitted and unpushed on `research/gap-flat-astra-20261112`.
No audit, registry, FINISH, main-branch, PR or public-post action
was performed. The generic skill's campaign and PR packaging
were not run: this dispatch specifies one pinned research file.

RESULT: OPEN FOR THE FULL ORDER-ONE TRACE — by hand, the fully dressed class of all excess-at-most-A/(100 log(2a)) wrapping surfaces, plus all disjoint-vertex elementary cube bumps, has an absolute area bound at beta<=1/2 with the original Z_m. The general excess tail remains RTAIL; (J12) and (E17) are proved here only for beta<=1/500, a group-blind range which does not improve the prior beta<2/9 full seed. No too-heavy lower bound, mass-gap claim or scientific status; not independently checked.
