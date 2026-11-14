# Repo search

The lead's `prior/repo-search-2026-11-08.md` concerns earlier RG obligations,
not the surface-tail code. Its main/PR hits supply no stated result on this
target. The task-specific prior note does not exist at the pinned commit.
FINISH row 833 assigns the proof to Claude Opus 5.5; row 847 assigns this
check. Searches of `open-registry.md`, `open-core.md` and `l17c.md` for
RTAIL and the source filenames found no competing owner. The local prior
results are the explicitly credited inputs in gap-flat, gap-rtail, gap-sos,
gap-joint and gap-expose; they are inputs to check, not new results here.
The refreshed search used `RTAIL|rtailsos|Kraft|peeling|icosahedral|degree.two
surface`, outside this lane, on main `bb4ec020d5ad` and PRs 10114
`f76f6c649cff`, 10133 `89faef229ff6`, 10134 `1e70c7211a2c`, 10141
`fb99b4dddc72`. Its full log is `repo-search.txt` in the scratch directory
below. There was no exact RTAIL, rtailsos or degree-two-surface hit.
The meaningful neighbouring hits, read at source, were:

| Source and lines | What exists; distance from this target |
|---|---|
| main: `docs/GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md:35–88` | Haar integration at a private link gives exact factorization. This is a related mechanism, for a trace/3 cumulant problem; it neither handles closed surfaces without private links nor supplies the Kraft bound. Credit this existing Haar argument. |
| PR 10141: `research/ym4d/library/in1.md:530–538` | The existing spanning-tree count is D^(2(N−1)). It is prior rooted-code work, not the discovery count 5^(n−1). |
| PR 10114: `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/HW.md:722–745`, `ARS_BIND.md:270–294` | A conditional RG mismatch peel with spectator weights and its dependency diagnosis. Different measure and premise; no Wilson surface-tail bound. |
| Same PR/folder: `RD3.md:565–575`, `RD4.md:448–460,687–694` | Existing same-reference and overlap-factorization requirements. These are credited precautions; F6–F8 below provide the specific finite identity needed here. |

These are bounded retrieval checks, not an exhaustive novelty claim. The
other filename hits concern Fock-space peeling, geometric shellings or
different models. No other row owns this requested check. Later seed rows
835–836 have different outputs; a seed result does not count these surfaces.

The SA index was searched first for every target label and method above,
including F26/E17/J12, odd surfaces and binary icosahedral moments. It has
no target supplier. The neighbouring mass-gap rows in `chunk-29.md` and
`obligations.md` lead to outline 31858–31884 and 32480–32490, read directly.
They leave a spectral gap separate from scalar reconstruction. CA-I and
the 4.12–4.19 index supply no premise used in this check; CA-I was downloaded
as requested, but no unrelated CA proof was read or claimed checked.

## Record and checkpoint

Checker: OpenAI Codex, gpt-6-astra, xhigh, as dispatched in row 847.
Author checked: Claude Opus 5.5, max. Source revision:
`bff94f194d047ab8e32509252c8d03fdc4da9d06`.
This is research text, not an audit; it grants no status.
Line references without a filename refer to `gap-rtailsos-opus.md` at that
revision. No numerical run discharges any statement.
Coverage: every named proof statement in the assigned note, its displayed
endpoint arithmetic, and the finite expansion through E17/J12 and the
three remainders. The old S23 class bound remains a cited input to the
reductions above 6/25. The transfer construction, the witness's earlier
proof, the FQ-to-seed continuation and the author's GUIDE runs are not
rechecked. No mathematical computation or simulation was run in this check.

Downloads, each fetched once, are in the newly created directory
`/tmp/sa-gap-rtailsos-check-astra.xy0cTd/`: the outline and CA-I at
`31a47c543775`. Credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text. No Balaban estimate is imported here.
The local surface representation and consumer algebra are credited to
their named Codex authors, as the source note does.

Checkpoint: the assigned check is complete. T1–T6 retain their stated
intervals. Proposition L's universal strict-count impossibility fails;
the narrower direct-certificate restriction holds. The next decision
belongs to the author: correct that auxiliary limitation and the minor
equalities/domain wording listed below. No source note, registry, queue,
ledger or audit file is changed.

## 1. Discovery and peeling

**Lemma K1 (lines 120–138): HOLDS.** At each processed link every incident
plaquette of S is discovered. Consequently no later discovery can use an
earlier processed link. A link-connected path from the root to any missing
plaquette contradicts termination. This also proves injectivity: the
deterministic state transition reconstructs the set from its labels.
There are finitely many links, and every step processes a new one.

**Lemma K2 (lines 140–147): HOLDS.** Regard the decoder as a finite tree,
with the remaining number of unprocessed links as its depth bound. The
total weight at depth zero is at most one; replacing a node by its children
cannot increase total weight. Distinct encoded surfaces occupy distinct
terminal nodes. A dead state contributes zero, not a spurious surface.
Empty labels consume a step, so their weight one causes no infinite run.

**Corollary C5 and its closing-link count (lines 149–159): HOLDS.** On a
degree-two surface only (D,j)=(1,1),(2,0) occur. There are n−1 discoveries.
The incidence identity 4n=2|E(S)| gives n+1 closing links. Assigning weights
1/5 and 1 gives total surface weight 5^(1−n), with state sums at most one.
Thus the stronger summability statement, and not just the individual
5^(n−1) count, follows. This argument permits singular vertices and does
not assume that the surface is a graph.

**Lemma P (lines 469–488): HOLDS, including branching.** An equivalent
induction removes each plaquette at its *first processed incident link*.
For all plaquettes still present at a link, condition on every other link.
Each individual holonomy is Haar under this one link integration. Hölder
therefore bounds k surviving factors by the common kth moment N_k,
independently of the conditioned links and of their mutual correlations.
The removed factors are replaced by a constant; subsequent integrations
create no new dependence. The root is removed at e_1. Every other
plaquette is removed exactly when discovered, by K1. Therefore k_1=1+j_1
and k_i=j_i for i>1. The case k_i=0 contributes N_0=1. This proves the
first inequality; N_(j+1)≤sinh(beta)N_j proves the second.

**Odd SU(2) moments and P1 (lines 490–500): HOLDS.** With Haar trace density
2 sqrt(1−x²)/pi on [−1,1], integration of
d[x^(2l)(1−x²)^(3/2)] gives (2l+3)I_(2l+1)=2l I_(2l−1).
Thus M_1=4/(3pi), M_3=8/(15pi), M_5=32/(105pi).
Also sum_e(6−d_e)=6|E|−4n≤8n because d_e≥2. Combining this with P gives P1.
Free closing links mean no remaining Haar factor; they still appear in
the incidence and neighbourhood accounts in T4/T6.

## 2. T6 and every endpoint constant

**Theorem T6, including (L) and the endpoint (lines 548–584): HOLDS.**
Write alpha=7/10 for its code parameter, to distinguish it from the box
side a. At a state (D,j), there are at most binom(6−D,j) labels. Give each
the weight c^(6−D−j) M_j alpha^((D+j)/2) V^j. The allowed parity gives
exactly the six sums L1–L6. The sums of D+j and j along a surface are
4n and n−1. Its code weight therefore dominates
u(S)(alpha² V/sinh(beta))^n/V. K2 proves the displayed root sum.
This derivation includes closing links with D=2,4,6 and j=0; their
weights are c^4 alpha, c² alpha² and alpha³, respectively. They are
not discarded from (L).

Here is a rational check of the endpoint. All finite decimals below
denote exact rationals. The elementary bounds used are

    sinh x ≤ x/(1−x²/6)  (0≤x<sqrt(6)),
    cosh(x)^r ≤ exp(r x²/2)  (r≥0),
    exp(u) ≤ H(u) := 1+u+u²/[2(1−u/3)]  (0≤u<3).

The last follows term by term from n!≥2·3^(n−2) for n≥2; no
floating-point enclosure is an input. At beta=6/25 they give:

| Quantity | Exact bound and comparison |
|---|---|
| sinh(beta) | 150/619 < 0.2423264; multiplying the latter by 619 gives 150.0000416. |
| c² | H(36/625)=1+36/625+648/383125 < 1.059292. The last comparison is 648 < 0.001692·383125=648.2475. |
| c^4 | H(72/625)=1+72/625+2592/375625 < 1.122101. Here 2592 < 0.006901·375625=2592.188125. |
| M_1 | 400000/942477 < 0.424414; cross-product surplus 433478 at denominator 10^6. |
| M_3 | 800000/4712385 < 0.169766; surplus 2751910. |
| M_5 | 3200000/32986695 < 0.097010; surplus 39281950. |
| alpha V, alpha², alpha³ | 357/1000, 49/100, 343/1000. |
| V²,V³,V^4,V^5 | 0.2601, 0.132651, 0.06765201 < 0.067653, 0.0345025251 < 0.034503. |

The moment comparisons use pi>314159/100000. A short hand certificate,
if a decimal bound for pi is not taken as known, is Machin's identity:

    pi = 16 arctan(1/5) − 4 arctan(1/239)
       > 16(1/5−1/375+1/15625−1/546875)−4/239
       = 1231847548/392109375 > 314159/100000.

The last cross-product surplus is 65659375. The identity follows from
tan(4 arctan(1/5))=120/119 and the tangent subtraction formula; the
angle lies in (0,pi/2). Alternating-series remainders give the inequality.

Substituting those rational upper bounds into each term gives exactly
the safe outward bounds printed in the source:

| Row | Termwise upper bounds | Total upper bound |
|---|---|---|
| L1 | 0.85009, 0.11689, 0.00115 | 0.96813 < 0.9682 |
| L2 | 0.785471, 0.202510, 0.002901 | 0.990882 < 0.9909 |
| L3 | 0.33705, 0.00773 | 0.34478 < 0.345 |
| L4 | 0.519054, 0.022305 | 0.541359 < 0.542 |
| L5 | 0.424414·0.343·0.51 | < 0.0743 |
| L6 | 0.343 | 0.343 |

These are multiplication comparisons of the fractions in the preceding
table. For example the L2 middle upper product is exactly
1.5·1.059292·0.127449=0.202508559162<0.202510.
A coarser hand certificate also suffices: substitute
(c^4,c²,M_1,M_3,M_5)<(9/8,53/50,17/40,17/100,1/10).
It gives L1<0.972, L2<0.994, L3<0.346, L4<0.542,
L5<0.075, L6=0.343. Thus the proof does not depend on a marginal
rounding decision in any printed state sum.

Finally alpha²V=2499/10000. The rate satisfies the exact comparison

    sinh(6/25)/(alpha² V) ≤ 1500000/1546881 < 9697/10000,
    9697·1546881 − 15000000000 = 105057 > 0.

All relevant expressions increase with beta. Rooting above one fixed
base face and using n≥A proves
B_O≤(51/100)N_perp(9697/10000)^A throughout (0,6/25].
Here 51/100 is the Kraft prefactor V, not a fitted normalization.
The area and root input was checked in Claude Fable 5.2's Proposition SC
and Lemma M, `gap-kappa-order.md:37–66`: even link incidence propagates
the same odd parity between neighbouring horizontal stacks. Every stack
therefore contains a horizontal face, giving n≥A and N_perp root choices.

## 3. The normalized consumers

**Use of F8, F9 and F26 (lines 70–78, 579–598): HOLDS.** Read and
checked the finite algebra in `gap-flat-astra.md:77–238,488–511` and
`gap-joint-astra.md:97–156`. Expanding sign changes marks a compatible
family H with coefficient (−2)^|H|. Its unflipped exterior integral
is W_m(H). In F6 the far plaquettes use no marked links. Conditional
Jensen gives Z_m≥Z_far,m, since each removed plaquette has zero mean
under the marked links. Different marks use disjoint link sets.
Consequently |W_m(H)|≤product u(S), with the *original* Z_m.
Summing the other marks costs at most product(1+2u(S))≤exp(2B_O).
This proves F26 at L=0 for any ordering using the new B_O. The old
small-beta estimate F25 is not a premise of this algebraic inequality.

**J12: HOLDS.** For the consumer boxes, A≥a² and N_perp≤4a².
Put rho=9697/10000 and tau=−log rho. Then tau≥303/10000>1/34.
Since x exp(−tau x)≤1/(e tau), B_O<(51/25)34/e<26; the partial
series e>65/24 already suffices. Hence for every ordering

    sum_(S in O) |D_m(S)| ≤ (51/25)e^52 a² exp(−tau a²).

A rooted subsum is smaller. For any fixed kappa>0,
−tau a²+kappa a≤kappa²/(4tau)<9kappa². Thus J12 holds with
b=2 and C_1=(51/25)exp(52+9kappa²), including its required
kappa≥(1/2)log(1/eta_*). J12 itself was read at
`gap-joint-astra.md:325–363`.

**E17: HOLDS.** Exact telescoping gives p_m(v)=sum D_m(S), so its
absolute value has the same bound. Taking
kappa_*=(1/2)log(1/eta_*) proves exactly

    Q_F ≤ (51/25)exp(52+9kappa_*²) a² eta_*^(a/2).

This holds for each fixed eta_* in (0,1), uniformly in beta≤6/25
and the stated boxes and crossed pairs. Read E16–E17 at
`gap-expose-astra.md:575–600`. Applying its FQ consumer also needs
that eta_* be a valid *lower* witness for S_ev. The witness in
`gap-fusion-astra.md:95–135` is positive at each fixed beta and
on compact positive coupling intervals. No positive common witness
on the entire interval approaching beta=0 is asserted here.

**RTAIL, RTAIL*, RTAIL-SOS and B_out: HOLDS, two-sided.** The exact
remainders were read at `gap-flat-astra.md:600–649`,
`gap-rtail-astra.md:641–713`, and `gap-sos-astra.md:513–575`.
For each of their specified first classes F⊂O,
|T_m(F)|≤B_F exp(2B_F)≤B_O exp(2B_O).
The identity R=p_m(v)−T_m(F) therefore gives

    |R| ≤ 2 B_O exp(2B_O)
        ≤ (102/25)exp(52+9kappa_*²) a² eta_*^(a/2).

In fact F26 bounds the complementary D subsum directly, saving the
factor two. The source's looser constant is valid. B_out≤B_O.
These conclusions require no new check of the separate SOS majorant:
the all-surface bound already controls every subset. All decorations
remain in W_m(H); no intermediate signed partition function is divided by.
The seed continuation beyond FQ is outside this check, as in the source.

## 4. T4 and T5

**Theorem T4 and its interval (lines 502–540): HOLDS.** Its six state
sums are obtained by deleting c^(6−D−j) from T6's weight and replacing
V by Z. With alpha=3/4 and Z=8/15, alpha Z=2/5 and alpha²Z=3/10.
The exact sums are

    J1 = (8/3+512/1125+884736/159468750)/pi < 3.1274/pi < 1,
    J2 = 3/4+6/25+8/1875 = 7457/7500,
    J3 = (6/5+64/1875)/pi < 0.40,
    J4 = 9/16+27/900 < 0.60,
    J5 = 3/(10pi) < 0.1,   J6 = 27/64.

**The printed J3 equality (line 519): HOLDS AFTER CORRECTION.** Replace
`J3=(6/5+0.0342)/pi` by
`J3=(6/5+64/1875)/pi < (6/5+0.0342)/pi`.
Indeed 64/1875=0.0341333… is not 0.0342. The upper bound and all
uses of J3 are valid.

At beta=7/30, sinh(beta)≤1260/5351 and

    c^8 ≤ H(49/225)
        = 1+49/225+2401/93900
        = 1+49/225+1620675/63382500 < 1.24335.

Then q<783.3105/5351<0.146386 since
5351·0.146386=783.311486. Multiplying by 20/3 gives a number
below 0.9760. The source's prefactor 8/15 and interval follow.
For its downstream constants tau_4≥0.024>1/42 and
B_O<(32/15)42/e<33. The finite expansion therefore costs e^66.
Also 1/(4tau_4)<42/4<11, which verifies its E17 constant.
The elementary lower bound e>163/60, obtained through 1/5! in
the exponential series, proves both this <33 and T1's <14 below.

**Theorem T5 (lines 542–546): HOLDS.** A degree-two code has n−1
one-plaquette discoveries and no other positive discovery size. Thus
P1 reads u(S)≤(2q)^n M_1^(n−1). Multiply C5 by
(10M_1q)^A/(5M_1), using n≥A and 10M_1q≤1. This gives the exact
prefactor 1/(5M_1)=3pi/20 and rate 10M_1q=40q/(3pi).
At beta=3/10 a sharper rational version of the source's same bounds is

    s≤30/197<0.152285,
    c^8≤H(9/25)=1577/1100<1.43364,
    q≤4731/21670<0.218321.

The last cross multiplication is 21670·0.218321=4731.01607.
For the rate, (0.9267)(3)(3.14159)/40=0.218348358975>0.218321.
Therefore the claimed strict rate <0.9267 and endpoint 3/10 hold.
Multiplying the two rounded bounds 0.152285 and 1.43364 alone
would be too coarse for the printed q<0.218321; the exact fractions
above supply that intermediate inequality. No correction to T5 is needed.

## 5. The binary icosahedral comparison

**Class counts, odd moments and transfer of T4–T6 (lines 649–659): HOLDS.**
Read `gap-tree-astra.md:288–346` for the credited icosahedral count
and invariant-space calculation. The 60 rotations have counts
1,15,20,12,12, and each has two lifts. For
b_+=(1+sqrt(5))/4 and b_-=(sqrt(5)−1)/4,
b_++b_-=sqrt(5)/2 and b_+b_-=1/4. Their odd power sums are
sqrt(5)/2, sqrt(5)/4 and 5sqrt(5)/32. Consequently the exact moments are

    M_1(2I)=(22+12sqrt(5))/120,
    M_3(2I)=(7+6sqrt(5))/120,
    M_5(2I)=(13+15sqrt(5))/480.

The identity and half-trace classes contribute 22, 7 and 13/4
before division by 120; the other classes contribute 24 times
the displayed power sums. This checks every multiplicity in lines
653–656. Since (223607/100000)^2=5.0000090449>5, these give
M_1(2I)<0.4070, M_3(2I)<0.1702, M_5(2I)<0.0970.
The even moments agree with SU(2). The table in G13 has zero
invariant multiplicity for spins 1 through 5; the center excludes
half-integer spins. Averaging is projection onto the invariant
subspace, so the tensor agreement through degree eleven used for
Lemma B follows, rather than being inferred from scalar moments alone.

Using the three rational upper bounds above in the odd state sums
gives J1<0.97, J3<0.38 and J5<0.1. Using them with the c²,c^4
bounds of Section 2 gives L1<0.934, L3<0.331 and L5<0.072.
For the tightest of these, the upper product for L3 is

    3·1.059292·0.407·0.2499 + 0.1702·0.045499293
    < 0.330964 < 0.331.

J2,J4,J6 and L2,L4,L6 use only even moments and are unchanged.
For T5, M_1(2I)<M_1(SU(2)); replacing the former by the latter
in t^n M_1^(n−1) proves the very same SU(2) prefactor and rate.
The upper bound pi<22/7, or the upper alternating Machin truncation,
already gives M_1(SU(2))>14/33>0.407.

**The all-unit-vector Haar wording (lines 645–646): HOLDS AFTER
CORRECTION for the finite-group application.** For SU(2) the wording
is correct. For 2I replace “every unit W” by “W corresponding to
a group element, as every conditioned plaquette remainder does”.
Left or right translation by that element preserves uniform measure
on 2I, so P transfers. Uniform measure on 2I is not invariant under
arbitrary rotations of S³; the unconditional all-unit-vector assertion
would be false for its odd absolute moments. No such rotation is used.

The U(1) comparison M_1=2/pi, M_2=1/2, and the weak-coupling
observation q≥sinh(beta)/2>1 for beta≥2 both HOLD. They prove no
U(1) interval and no weak-coupling estimate.

## 6. The superseded Finner route

**Lemma U (lines 163–184): HOLDS.** At most 6−d_e outside faces meet
each used link. For h_p=max_(e in p)d_e, the Finner reciprocal sums
are at most one. Its one-face norms are bounded by s times
g(2)=1, g(4)=2^(1/4), g(6)=5^(1/6). The factor g(h_p) is one of
the four factors in product_(e in p)g(d_e); the others are ≥1.
Distributing s in fourth roots gives precisely phi(2), phi(4), phi(6).
The two ratios are 2c^(−6) and 5c^(−12). This confirms the
overcounting direction as well as both branching penalties.

**Theorem T1, its rational choice and its consumers (lines 188–247):
HOLDS.** The weight phi(D+j)X^((D+j)/2)y^j, with X=P/phi(2),
has the six binomial sums K. Its surface product is
product phi(d_e)·(P²y/q)^n/y. Using U and K2 proves T1a and T1b.
At P=7/12,y=2/7, P²y=7/72, the six sums in their printed order are

    2630/2646, 698/756, 131/216, 1316/1728, 490/1728, 1715/1728.

Each fraction is correct and below one. In particular the three
terms of K1 are 5/6,10/63,5/2646; those of K2 are
7/12,1/3,5/756. The source's less reduced numerator/denominator
forms at lines 222–223 give the same fractions.
At beta=1/6, s≤18/215 and c^8≤9/8, hence q≤81/860 and
(72/7)q≤1458/1505. Also

    log(1505/1458)≥47/1505>1/33  (47·33=1551>1505).

Thus B_O<(8/7)33/e<14 and the source's e^28 cost follows.
Completing the square costs at most 33kappa_*²/4. This proves
every constant in T1c,T1d and the displayed E17 estimate.
The remainder bounds follow from the same finite algebra as Section 3.

**Theorem T2, interval and class scope (lines 255–278): HOLDS.** U and
C5 give the factor 1/5 and rate 5q exactly. At beta=1/4 the stated
rate 16/19 follows from s≤12/95 and c^8≤4/3. At beta=7/25,

    s≤525/3701<0.14186,
    c^8≤H(196/625)=1+196/625+57624/1049375<1.3686,
    5·0.14186·1.3686=0.97074798<0.9708.

This verifies the endpoint and its rate. The only geometric
restriction is link degree two. Overhangs, handles, singular vertices
and movement in either transverse direction introduce no additional
condition if that restriction holds. An SOS graph with a four-way
contact is not silently included.

**Lemma B and Corollary B1 (lines 286–352): HOLDS.** Quaternion Haar
moments are O(4)-invariant. At orders four and six the coefficients
are 1/24 and 1/192; the six-vector pairing count is 1+6+8=15.
The two AM–GM splits therefore give the stated nonnegative
branch-link polynomials. The isolation hypothesis makes their
plaquette families disjoint and makes all W_p independent of every
branch variable. After those variables are integrated, a remaining
link belongs to at most two surviving factors, including the
branch polynomials' individual terms. Finner with exponent two
therefore applies to each expanded term.

Distinct plaquettes at one link share no other link on these tori.
Their remainders W_i are independent Haar. Thus the norms needed
are 1/2, sqrt(E x^4)=2^(−3/2), and
sqrt(E|c_12|²|c_23|²)=1/4. This gives exactly

    T_4=(1+1/sqrt(2))/24,
    T_6=(1+6·2^(−3/2)+2)/192=(1+1/sqrt(2))/64.

Multiplying by 2^4 and 2^6 produces g4 and g6. The rational
bounds follow from 2·99²=19602>19600=140². Combining the
moment and neighbourhood products proves B1. Neither this proof
nor T3 applies Lemma B to adjacent branching links.

**Theorem T3 and its endpoint (lines 354–382): HOLDS.** Substitution
of phi_iso gives K at kappa=239/210, lambda=239/140 as an upper
bound. K2 may sum all valid codes while the analytic bound is used
only on the isolated-branching subset. This distinction is sound.
At P=11/14,y=2/9, the source's fractions, before its decimal bounds,
are exactly

| Row | Exact sum |
|---|---|
| K1 | 55/63 + 2313520/30005640 + 10179488/22684263840 |
| K2 | 11/14 + 28919/138915 + 1272436/630118440 |
| K3 | 173514/370440 + 2544872/280052640 |
| K4 | 28919/41160 + 1272436/31116960 |
| K5 | 636218/3457440 |
| K6 | 318109/384160 |

The denominators come from 14²,14³ and 9²,…,9^5; the common
numerators are 239·121=28919 and 239·1331=318109. They give,
respectively, the stated upper bounds 0.9506,0.9960,0.4775,
0.7435,0.1841,0.8281, all below one. This also checks the
intermediate reduction 694056/3333960=28919/138915.
At beta=2/9,

    s≤27/241,
    c^8≤H(16/81)=1+16/81+62208/2978694<1.218416,
    q<32.897232/241<0.1365033,
    (882/121)·0.1365033<0.99502.

For the last two comparisons, 241·0.1365033=32.8972953,
882·0.1365033=120.3959106 and 121·0.99502=120.39742.
The factor P²y=121/882 and prefactor 2/9 are therefore correct.
T6 supersedes this bound on its whole stated interval.

## 7. Limits of the method and the remaining reductions

**Proposition L, first sentence (lines 388–389): HOLDS.** From
K1≥5Py and K2≥P, one gets 5P²y≤K1 K2≤1. Thus the rate in
the displayed T1/T3 family is at least 5q. The individual code
weight bound w_1^(n−1)w_2^(n+1)≤5^(1−n) also HOLDS: the first
link permits five one-face labels, and every single label weight
is at most one.

**Proposition L, universal strict-count claim (lines 389–396): FAILS.**
The first failing inference is line 396, which says K2 can certify
“at best” N_2(n)≤5^(n−1), interpreted as ruling out strict inequality.
C5, with the very same weights depending only on (D,j), already
proves strict inequality. A unit cube boundary through p_0 has six
faces and degree two. A flat coordinate torus through p_0 has
m≥9 faces and degree two. For any n choose one of these with area
k≠n. C5 gives

    N_2(n)5^(1−n) + 5^(1−k) ≤ 1,
    N_2(n) ≤ 5^(n−1)(1−5^(1−k)) < 5^(n−1).

Both witnesses exist with periods at least three. On a 3^4 torus
one can use k=9 for n=6, giving an especially small explicit example.
This refutes the asserted impossibility, not C5 or a surface count.

**Corrected restriction: HOLDS AFTER CORRECTION.** Replace that
sentence by: “The direct conversion of K2's upper bound one using
only the individual code weight cannot improve the exponential
base five.” The inequality for w_1,w_2 proves this narrower
statement. Our strict prefactor improvement does not supply a
smaller exponential base. Lines 619–622 must retain that same
restriction; they do not rule out a sharper accounting of the
decoder tree or weight reserved for other surface sizes.
Also write `40/(3pi)≈4.244`, not the literal equality at line 619.

**The hand comparison at beta=1/3 (lines 399–402,627–630): HOLDS
within those displayed certificates.** Since s≥55/324 and the first
four binomial terms of c^8 are at least 1123/729,
q≥61765/236196>0.2614. With pi<22/7 this makes 40q/(3pi)>1.10
and the corresponding required entropy 5(3pi/40)/q<4.51.
This comparison supplies no lower bound on actual surface numbers
or Wilson weights. The asserted GUIDE optima and the 56 percent
penalty are not proved optimality statements and were not rerun.

**BR-SEQ implication, supersession and class-remainder reductions
(lines 424–461,586–616): HOLDS as implications.** If BR-SEQ held,
the very same isolated constants would apply to every surface;
T3 would then bound the full tail on (0,2/9]. This implication
does not prove BR-SEQ. T6 makes that premise unnecessary below
6/25. For any enlargement F⊂F'⊂O ordered first,
T_m(F')−T_m(F) is the corresponding D subsum and is controlled
by F9 for F'. Thus the source's reductions to RTAIL-ADJ and
RTAIL-BR follow from the indicated class bounds. With the read
S23 and the checked T5, the reduction to RTAIL-BR on
(6/25,3/10] is valid. It leaves that signed estimate open.
The reductions above 6/25 use S23 as an existing input; this
check does not repeat the independent SOS geometry proof.

The strict endpoint comparisons 6/25>7/30>2/9 and 3/10>7/25
are correct. The earlier estimates remain valid on their original
domains. T6 supplies E17, not a verified continuation to a full
seed or a continuum mass gap.

## 8. Disposition

| Statement | Verdict |
|---|---|
| K1, K2, C5 and the n+1 free closings | HOLDS |
| P, its odd SU(2) moments, P1 | HOLDS |
| T6, all six Kraft constraints, 51/100, 0.9697 and 6/25 | HOLDS |
| F26 application, J12, E17, RTAIL, RTAIL*, RTAIL-SOS, B_out | HOLDS |
| T4 and its endpoint 7/30 | HOLDS |
| T4's printed rounded J3 equality | HOLDS AFTER CORRECTION |
| T5 and its endpoint 3/10 | HOLDS |
| Binary icosahedral moments and T4–T6 transfer | HOLDS |
| All-unit-vector wording when applied to 2I | HOLDS AFTER CORRECTION |
| U, T1, T2, B, B1, T3 | HOLDS |
| Proposition L: P²y≤1/5 and the individual code-weight bound | HOLDS |
| Proposition L: no such Kraft proof of N_2(n)<5^(n−1) | FAILS |
| Replacement restricted to the direct bound using only one code weight | HOLDS AFTER CORRECTION |
| BR-SEQ implication and signed class-enlargement reductions | HOLDS, with their stated inputs |

There are three correction groups: the auxiliary impossibility claim,
the finite-group Haar domain wording, and the two literal equalities
using rounded decimals (J3 and 40/(3pi)). None changes a T1–T6 interval.
The source's ARGUED adjacent-branch calculation, proposed next steps and
GUIDE optima are not promoted to proofs. In particular, no claim of
global optimality, a seed past the stated consumer, or a continuum gap
follows from this report.

RESULT: T6 and its normalized two-sided tail consequences HOLD on 0<beta≤6/25 with prefactor 51/100 and rate 0.9697; T1–T5 and the binary icosahedral transfer HOLD, with the displayed minor arithmetic/domain corrections; Proposition L's universal prohibition of a strict count improvement FAILS by C5's own weighted sum, while its narrower direct-certificate restriction holds. No seed continuation or scientific status is granted.
