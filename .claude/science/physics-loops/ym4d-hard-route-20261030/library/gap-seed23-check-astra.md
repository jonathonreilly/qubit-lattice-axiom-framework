# Repo search

The lead's 2026-11-08 search covered main and PRs #10114, #10133,
#10134 and #10141. Its digest concerns earlier RG obligations, not this
periodic seed. The closest named hit is
`pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`.
I fetched that PR at `f76f6c649cff7dffbab664d8976e680e8f287fe9` and read
lines 1–42 and 106–149. It gives a different strong-coupling endpoint
(beta at most 1/32) and a one-step plaquette witness. Neither supplies
the periodic seed at beta below 1/3. Credit that prior Codex/Astra work;
its proof is not redone here.

The target-specific prior note is absent at the pinned commit. FINISH rows
835 and 840 contain no additional “Repo prior work” paths. Searches of
`open-registry.md` for this target, Dobrushin, forest gauges, thermal sums
and the glue half found no competing owner. This is the requested check
of row 835, not a new attack on its already proved inputs.

The SA index points to outline 240–278 for the finite Wilson law,
588–599 for the distinction between clustering and a gap, and 7660–7681
for the tree-gauge Haar identity. I read those passages after their index
rows and neighbours. The last is existing work behind Lemma G, not a new
result here. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text, at revision `31a47c543775`. No continuum gap is
imported. The CA-I items 4.12–4.19 index was consulted; no result from that
part of the account is used as a premise.

## Check boundary and checkpoint

Checked by OpenAI Codex, dispatched as gpt-6-astra xhigh, against commit
`287ff98f971db4b719bd859f68a6dd976dc0e413`. Author: Claude Opus 5.5, max.
This is research text, not an audit, and grants no status. Source line
numbers below refer to `library/gap-seed23-opus.md` at that commit.
Main's workflow map and check procedure were read at
`bb4ec020d5ada57c630dd89acc98a68397ade423`; this dispatch's output path and
verdict vocabulary govern this report.

The two requested SA sources were downloaded once each into the new
directory `/tmp/sa-gap-seed23-check-astra.U6dNsG/`. No computer-assisted
proof or machine enumeration is used. All checks below are written arguments.
The supplied V1, transfer, cut and shape theorems remain named inputs;
their required statements and applications are checked here, not their
entire upstream proof closures. No Balaban estimate enters this proof.

Checkpoint: all eleven requested statements are checked below. MG needs
the proved hypothesis repair (C1+); AVG's consequence needs the stated
endpoint/scope restriction. Theorems T and F retain their conclusions.
Only this report is changed; no source correction or status update is made.

## Lemma HR — HOLDS

Lines 103–115. For the long torus, condition first on all spatial links.
The selected time slabs have both faces in the retained half. Their product
conditional kernel therefore depends only on retained spatial links.
Taking conditional expectation again over the omitted spatial links leaves
that same kernel. Integrating the selected time links gives the same
function F_f for both measures. No assertion about equality of the spatial
marginals follows or is needed.

## Proposition NG and its application — HOLDS

Lines 120–146. A separate resolvent argument checks the threshold. If
rho(M)<1, solve `(I-M)w_H=1` with positive w_H. Put
`w_V=G C_VH w_H + epsilon G 1`. Then
`((I-C)w)_V=epsilon 1` and
`((I-C)w)_H=1-epsilon C_HV G 1>0` for small positive epsilon.
Thus Cw<w with w>0, which forces rho(C)<1. The contrapositive is NG.
The author's Perron argument also has the correct inequality direction.

For the uniform majorant C=(s/4)A, horizontal rows have 14 horizontal
and 4 vertical partners; vertical rows have 12 horizontal and 6 vertical
partners. Its eliminated row sum is
`7s/2 + 3s^2/(1-3s/2)`. For `s<2/3`, subtracting this from one and
multiplying by the positive denominator gives
`1-5s+9s^2/4=(1-s/2)(1-9s/2)`. The threshold is exactly 2/9.
For `s>=2/3` the required slab Neumann series itself fails. Replacing s/4
by s gives 1/18. The obstruction concerns this uniform majorant and
Neumann comparison, not every possible use of slab independence.

## Lemma G — HOLDS

Lines 150–166. On each rooted tree the displayed recursion fixes one
vertex variable at a time, including inversely oriented edges. Once U_F
is fixed, every remaining link undergoes a fixed left and right Haar
translation. Fubini removes the normalized integral over U_F. This proves
the unnormalized identity, then equality of Z and normalized invariant
expectations. No determinant or residual gauge-volume factor appears.
Disconnected trees and isolated vertices cause no change. This is the
forest version of the cited SA Proposition 1a.3.3.

## Lemma DC' — HOLDS

Lines 169–198. The row bound must include columns in D, as stated.
Let I=Lambda minus D, A=C_II and B=C_ID. Updating only I contracts its
total coordinate seminorm by `1-(1-alpha)/|I|`. The increments of P^t f
have a summable uniform bound, so their limit h exists and depends on D
alone. Both laws preserve these updates, hence have expectations mu_k(h).
The accumulated D-seminorms are bounded by
`delta_D(h) <= B^T (I-A^T)^(-1) delta_I(f)`.
Multiplication by the chord diameter 2 gives exactly the first displayed
bound in DC'. The term A^n B describes n+1 edges, and has row sums at
most alpha^(n+1). Terms shorter than d vanish, giving the second bound.
This checks the transpose and the first power alpha^d independently of a
full-volume comparison theorem. Empty I, empty D, zero influences and no
connecting path give the constant or zero cases directly.

## Lemma MG — HOLDS AFTER CORRECTION

Lines 200–228. Part (a) is false under (C1) alone. The first failing step is
lines 224–225: (C1) does not ensure the asserted agreement of staples after
projection to E(n) minus F. Parts (b) and (c) have their stated elementary
arguments; the defect is the conditional-law assertion in (a).

Here is a hand counterexample. Take n=(4,4,4,4), n'=(8,4,4,4). Choose
two perpendicular spatial links k and l based at time 1 and at the same
spatial site. Put F={k}, F'=empty and D=D_cut union {k}. Both are forests,
and (C1) holds. The law mu_2 on E(n) minus F integrates out k, which is
free in the long torus. At all other retained links equal to 1, the six
plaquettes through either k or l lie entirely in Lambda_0. Exactly one
contains both. Write x=Re(U_l) and z(r)=integral exp(r Re(h)) dh.
In mu_1 the conditional density of U_l is proportional to exp(6s x).
In mu_2 it is proportional to

`exp(5s x) integral exp(s[5 Re(h)+Re(U_l^(±1) h^(±1))]) dh`.

The ratio of the density at U_l=1 to its value at U_l=-1 is
`exp(12s)` for mu_1 and `exp(10s) z(6s)/z(4s)` for mu_2.
For s>0, `z(6s)<exp(2s)z(4s)`, since Re(h)<1 Haar almost everywhere.
Thus the ratios differ. The conditional densities are continuous and
positive, so the discrepancy persists on an open set of the other links;
it is not merely a choice of a conditional version on a null set.

**Corrected hypothesis (C1+).** Keep (C1) and add
`F subset r(F' intersect Lambda_0)`, where r reduces time modulo a.
Equivalently, every link discarded as F-fixed must also be F'-fixed in
the retained half. Extra F'-fixed links are permitted in D.

Under (C1+), no variable integrated out by the projection appears in an
off-D staple. Every F-link already equals 1 in the long measure; every
extra F'-fixed link is retained as a coordinate equal to 1 under mu_2.
Consequently the short-torus kernel, evaluated on those retained
coordinates, is exactly the long-torus kernel. Its six plaquettes are
internal by Lemma M. Conditioning down gives (a). Changing a free partner
changes one staple by its chord distance, so V1 gives s/4 in (b).
Lemma G and the coordinate marginal give (c).

This proves the repair rather than proposing it. It covers both gauges
actually used: F' restricted to the first half equals F plus the time
cut links that the respective forest pattern contains. Those extra links
are coordinates in D, fixed to 1 under mu_2. No theorem conclusion below
needs the false generality of the original (C1).

## Theorem T — HOLDS

Lines 232–264, using the repaired MG just proved. In the first half,
F' fixes exactly F plus all time links from a-1; (C1+) holds. A free
spatial link at time 1 through a-2 has four spatial plaquettes, each
with three other free links. Its two temporal plaquettes have their time
links fixed and contribute one spatial partner each. These are distinct
for sides at least 3: `4*3+2=14`, giving q=7 beta/2.

Use circular time midpoints. Every influence step moves time by at most
one. The chosen plaquettes are separated from the cut positions
`{0,a-1,a-1/2}` by at least `min(j-1,a-1-j)=j-1`.
For a>=4 they avoid D. Spatial plaquettes have seminorm sum at most 4;
temporal plaquettes have at most 2. Their equally weighted comparison
constant is `(2*4+2*2)/2=6`. Translation invariance is used only before
gauge fixing or through Lemma G; no gauge-fixed translation invariance
is assumed. At a=3 the difference of mean actions is at most 2, giving
the stated trivial bound. Integration gives 12*6=72; on B=(2a)^3 it
gives 72*8=576. The seed-to-gap arithmetic is checked with F below and
depends only on the same threshold. Thus the statement, including beta
below 2/7 and the absence of a parity requirement, holds unchanged.

## Lemma LF — HOLDS

Lines 268–300. Each direction condition is independent of its own
coordinate and selects four parity classes. The six pairwise
incompatibilities in (a) are valid. Thus the conditions partition all
16 classes. Each vertex has precisely one incoming and one outgoing
chosen link in the same direction. Components are straight lines.

For (c), the sum of the two indicators for the mu-edges of a
(mu,nu)-plaquette depends only on its two other parities. Directly
eliminating p_nu from the direction condition gives this complete table.
E denotes equal remaining parities and N denotes unequal ones.

| Plane | Remaining coordinates | Number of chosen mu-edges | Number of chosen nu-edges |
|---|---|---|---|
| (0,1) | (2,3) | 1_E | 1_N |
| (0,2) | (1,3) | 1_E | 1_N |
| (0,3) | (1,2) | 1_E | 1_N |
| (1,2) | (0,3) | 1_N | 1_E |
| (1,3) | (0,2) | 1_E | 1_N |
| (2,3) | (0,1) | 1_N | 1_E |

Every row sums to one. For example, in plane (1,3), the two 1-edges
require p0=p2 and opposite p3 values, so exactly one is chosen iff
p0=p2. The two 3-edges require p0!=p2 and opposite p1 values, giving
the complementary case. The table records all six eliminations; in each
row the two indicators are complementary. No search result is used.

## Theorem F — HOLDS

Lines 304–355, with (C1+) in place of the erroneous general MG hypothesis.
The statement and all its constants remain unchanged.

**Forest and matching.** Even side lengths make parity descend to each
torus. Each line component is one coordinate circle. Removing its single
wrap edge makes a path, so F and F' are forests. In the first half their
spatial seam removals coincide. Their only difference is that F' also
fixes K_time, the time-line edges from a-1. Hence (C1+) holds.
Every plaquette containing a removed spatial seam edge has all its links
in D by definition. Every plaquette containing a removed time edge lies
in the cut slab and has all its links in D_cut. Therefore every plaquette
through a free link outside D has one fixed link and two other free links.
The six plaquettes have distinct partners: the exact count is 12.

**Distance, including all seams.** Work with each midpoint coordinate on
its own circle. One influence edge moves any coordinate by at most one.
The selected links have time coordinates in `[j-1,j]`, while the time
cut has coordinates `{0,a-1,a-1/2}`. The circular separation is at least
j-1. Write b_i=2c_i. The selected i-coordinates lie in `[c_i-1,c_i]`.
Every link in a plaquette containing an i-seam edge has i-coordinate in
`[b_i-1,b_i]` modulo b_i. The two closest circular separations are
`c_i-1` and `b_i-1-c_i=c_i-1`, both at least j-1.
Distance to the union D is thus at least j-1. Deleting fixed coordinates
from the influence graph cannot shorten it. For a=4 the distance bound
is one, so none of the chosen plaquettes touches D even in the smallest
allowed box. Spatial positions in other coordinates do not weaken this
argument: a seam target need only be separated in its own coordinate.

**Comparison and free energy.** The six selected plaquettes each have
three free links and coordinate seminorms at most one. With row sums
`12s/4<=q=3 beta`, DC' gives `6 q^(a/2-1)/(1-q)` per plaquette.
Translation invariance of the ungauged laws permits a different chosen
position for each orientation. Lemma G and repaired MG identify those
expectations with the two gauge-fixed laws. This proves (17F), uniformly
for `0<=s<=beta`, without a volume factor in the local bound.

There are `6t|B|` plaquettes, so
`dF(t,B;s)/ds=-6t|B| abar_(t,B)(s)`. Integrating the difference from zero
gives (18F) with coefficient `12*6=72`. From the transfer trace,
`Phi_B=2 log(1+S(a;B))-log(1+S(2a;B))`.
Since `S(2a;B)<=S(a;B)`, this lies above `log(1+S(a;B))>=0`.
For B=(2a)^3 the coefficient becomes `72*8=576`. Under (19F),

`S(a;(2a)^3) <= exp(3/5000)-1 <= 3/4997 < 1/1650`,

using the exponential series and `3*1650=4950<4997`. The strict threshold
is preserved even when (19F) holds with equality. For a=2n the ratio of
successive terms n^4 q^n tends to q<1. Thus an even admissible a exists
at every fixed beta in (0,1/3), without numerical selection.

**Theorem SH and the gap constant.** I read the corrected SH, its
enlargement inputs, and the ratio-4 specialization in
`gap-seed-shape.md:53–144`, plus the downstream arithmetic in
`gap-vmf-lip.md:549–582`. The enlargement from sides 2a to 4a at time a
has three factors 4, hence total exponent 64. With s0<1/1650,

`s1=S(a;(4a)^3) < exp(32/825)-1 <= 32/809 < 1/25`.

Here `exp(x)-1<=x/(1-x/2)` for 0<=x<2 follows from
`n!>=2^(n-1)`. The same rational estimate verifies SH's constant without
its decimal approximations. At ratio 4, j=p=2 and q_SH=3 give
`Pi=64`, `C=42`, and
`phi(x)=(1+x^2)^8(1+x^3)^336-1`.
For 0<=x<=1/25, its exponent is at most
`u=8x^2+336x^3 <= (536/25)x^2 <= 536/15625`.
Therefore

`phi(x) <= [335000/15357] x^2 < (111/5)x^2`.

The last comparison is `1675000<1704627`. Take K=111/5;
`K/25=111/125<1`, and `E=(8/3)^3=512/27<K` since 2560<2997.
Furthermore

`K s1 < 3552/4045 < 22/25`,
`log(1/(K s1)) > 3/25 + 9/1250 = 159/1250 > 1/8`.

The log inequality follows by integrating `1/(1-u)>=1+u` from
0 to 3/25. For L>=64a the SH index based on side 4a is at least 4.
Its loss is at most `2^(-4) log(eE/K)<1/16`. Thus
`m(L^3)>1/(16a)>3/(50a)`. If s1=0 the spectral statement is immediate.
No parity requirement remains on L. The finitely many smaller cubes
have a positive gap by the supplied positive compact transfer operator
with simple top eigenvalue. This proves volume uniformity at fixed beta.

**Both halves.** The supplied centre flips preserve the positive simple
ground state. In the joint spectral decomposition let S0 be the excited
sum in zero flux and S_perp the sum in the other sectors. Then
`S=S0+S_perp` and `U=S_perp/(1+S)`. Consequently
`S0<=S<1/1650` and `U<=S/(1+S)<1/1651`.
All quantities use the original transfer operator; gauge fixing was used
only for invariant plaquette expectations. No electric-flux sector was
discarded to obtain the seed or the gap.

**Independent hand check of the example.** For beta=1/4 and a=282,
the left side of (19F) is `576*282^4*(3/4)^140`.
Use a different grouping from the author's fifth powers:
`(4/3)^7>7`, because `16384>7*2187=15309`.
Thus `(3/4)^140<7^(-20)`. Since `282<7^3` and `576<2*7^3`,
the whole expression is less than `2/7^5=2/16807<3/5000`
(10000<50421). The author's fifth-power estimate is also correct.
Finally `3/(50*282)=1/4700` and `64*282=18048`.

## Corollary F2 — HOLDS

Lines 357–365. Axis permutation gives
`F(t,a,c,d)=F(a,t,c,d)` and likewise with 2a. Lemma K(a), read at
`gap-crux-restate.md:178–180`, yields

`2e(a,c,d)-e(2a,c,d) = lim_(t even -> infinity) Phi_(t,c,d)(a)/t`.

For every even t>=a the hypotheses of F hold. Its bound divided by t
is `72a cd beta q^(a/2-1)/(1-q)`. Multiplication by a proves the
stated bound for Delta. Nonnegativity follows both from these nonnegative
Phi values and from Lemma K(b). No interchange of limits with an
unbounded integral is used. The weighted combination has coefficient
`72[4+2*2+4]=864` times a^4. The temporal-gauge variant follows from T
in the same way, without parity assumptions and with c,d>=3.

## Lemma AVG — HOLDS AFTER CORRECTION of the consequence's scope

Lines 374–394. The mean-degree assertion and the stated finite spectral
inequality both hold. Let M=4N-|F| be the number of free links. Counting
ordered pairs within each plaquette gives

`sum_l deg(l)=sum_p (4-f_p)(3-f_p)`
`=72N-36|F|+sum_p f_p(f_p-1) >= 72N-36|F|`.

Here each fixed link belongs to six plaquettes, and no two distinct
links share two plaquettes when all sides are at least 3. Since
`|F|<=N-1`, division by M gives
`mean deg >=36(N+1)/(3N+1)=12+24/(3N+1)>12`.

For the consequence, let d be the number of free links removed by D.
Deleting them loses at most 36d in the ordered adjacency sum. If
|D|<N, its remaining sum is at least `12M-36d>0`. Rayleigh's quotient
with the constant vector on the remaining free links is therefore at least

`(12M-36d)/(M-d) >= 12-36d/M >=12(1-|D|/N)`.

If |D|>=N the claimed lower bound is nonpositive and follows from
nonnegativity of the spectral radius (zero for an empty remaining graph).
Thus the inequality holds for every D. Any positive weighted strict
contraction off D would imply rho((s/4)A_II)<1. Consequently it is
impossible when `3s(1-|D|/N)>=1`, as stated. NG also applies to further
Neumann elimination within I.

**Correct scope.** For each fixed s>1/3, this rules out such contractions
along seeds with |D|/N tending to zero. It says nothing decisive at s=1/3:
the displayed lower bound is then `1-|D|/N`, below one for nonempty D.
It also does not exclude choices with nonvanishing boundary fraction, or
influence estimates better than the uniform s/4 majorant. The source's
“passes 1/3” is valid as an asymptotic upper ceiling in this restricted
family. The use in lines 425–432 over the whole interval `[1/3,2/3)`
must instead say `(1/3,2/3)` for this obstruction. The endpoint seed is
still open; this counting proof does not establish its impossibility.
No part of Theorem F, which assumes beta<1/3, changes.

## Proposition NP — HOLDS

Lines 396–413. Let V=|B|. Perfect spatial plaquettes in each of the two
slices force `4|E_t|=4|E_(t+1)|=3V`. Perfect plaquettes between them
then force `6|tau|+|E_t|+|E_(t+1)|=3V`, hence |tau|=V/4.
If V is not divisible by four, the assumed perfection is already
impossible. Otherwise each tau vertex is isolated in E_t: every incident
spatial edge belongs to a temporal plaquette already occupied by its
tau edge. The forest E_t has `V-|E_t|=V/4` components, exactly the number
of those isolated vertices. Yet there are `3V/4>0` other vertices,
which must belong to additional components. This is the contradiction
in step (iv). It uses neither a numerical case check nor an assumption
that the torus itself is a tree. The spatial seams in F are consistent
with this necessary defect in every two-slice slab.

## Disposition and limits

| Statement | Verdict |
|---|---|
| HR | HOLDS |
| NG, including its uniform-majorant application | HOLDS |
| G | HOLDS |
| DC' | HOLDS |
| MG | HOLDS AFTER CORRECTION: add (C1+) |
| T | HOLDS with the proved MG repair, satisfied by its forests |
| LF | HOLDS |
| F, example, both halves and SH constants | HOLDS with the proved MG repair, satisfied by its forests |
| F2 | HOLDS |
| AVG | HOLDS AFTER CORRECTION of the consequence's endpoint/scope; both counts hold |
| NP | HOLDS |

The substantive failed assertion is MG(a) under (C1) alone; its explicit
counterexample and adequate repair are above. The fixed-coupling seed and
periodic-cube gap at beta<1/3 survive. The broader endpoint obstruction
is not proved. The remaining task for the source owner is to apply these
two corrections; the checked source has not been edited.

Read dependencies: `gap-vmf-lip.md` Theorem V statement, V1, DC, INF and
426–582; `gap-arealaw-opus.md` 59–75 and 186–248; `gap-mid-max.md`
219–224 and 256–274; `gap-seed-shape.md` 53–144 and 161–177;
`gap-crux-restate.md` 172–195; `gap-crux-fp.md` its finite-model and
axis-symmetry conventions; `gap-seed-check.md` 30–38 for the transfer
statement on unequal boxes. These existing results are credited to their
named authors, especially Claude Fable 5.2's cut and shape lemmas and
Codex/Astra's chord comparison. The comparison method is Dobrushin's.
This check does not re-prove the entire transfer or V1 closure, certify
the literature comparisons to Bhattacharjee and Bhattacharya et al.,
check the separate beta<2/3 flux extension, or use either GUIDE script.
It proves no continuum, intermediate-coupling or new physical-identification
claim. No mathematical tests, numerical runs or formal proof checker were run.

RESULT: HR, NG, G, DC', T, LF, F, F2 and NP HOLD; MG HOLDS AFTER CORRECTION by (C1+), with its original (a) refuted explicitly; AVG's counts HOLD and its consequence HOLDS AFTER CORRECTION to an asymptotic obstruction for fixed beta>1/3 and |D|/N tending to zero. The full periodic seed, both flux halves, and m(L^3)>=3/(50a) for L>=64a at every fixed 0<beta<1/3 survive with all stated constants; no status is granted.
