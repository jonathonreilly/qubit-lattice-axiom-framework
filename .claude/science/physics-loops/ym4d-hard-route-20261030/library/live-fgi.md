## Repo search

The lead's `prior/repo-search-2026-11-08.md` searched main and PRs #10114, #10133, #10134 and #10141.
Section 6 found no outside-lane proof of the live-strip invariant. PR #10141 contains our own snapshots.
For this repair I read that record and fetched main for the workflow and PR #10141 for its cited hits.
In `research/ym4d/library/`, I checked `in1.md:157--159`, `st1-r4.md:1703--1707` and `open-registry.md:224--228`.
The first retains genealogy as an input. The second concerns integration-slot matching. The third records those separate owners.
None proves the core-box claim. This reuses the lead's search, without repeating a full search.

The prior result in `geoh-live-ab.md`, checked by Claude, supplies (a)--(e), (h), and \(m\le h\) in (g).
Claude's `../gates/live-fgi-check.md` supplies the present repair to separation \(20a\).
`prior/live-fgi-fix.md` is absent at the repair pin `18b2f82f0`; the dated repository-search record is present.
The registry leaves O-live-geometry without another owner. FINISH row 550 assigns this repair here.
Row 549 owns the affirmative proof under no joining. This note does not take that task.

# Live-region boxes and probes

Repair of Claude's FIX in [live-fgi-check.md](../gates/live-fgi-check.md), FINISH row 550.

Codex, 2026-11-08. Original row 537; repair pinned at `18b2f82f0184e59bb66954489428e6f98ab4dd67`.
Research text, not an audit. This text grants no status.
Claude checked the original and the proposed repair; Codex applied it and rechecked sections 3--4 by hand.
The edited text has not had a further independent check.
Only this file is written. No computation supplies a proof step.

Outcome **(b)**: an allowed joining makes the specified core \(\mathsf C_C\) disconnected.
Thus the four clauses cannot all follow from the account's unchanged geometric rules.

## 1. Sources and the remaining question

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the large-field method, the step geometry and the preparation.
Every source port below has its line range. The source keys mean:

- **I:** [complete account, Part I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), commit `31a47c543775`.
- **SA:** [original outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), the same commit.
- **N:** [revised outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.

The target is I 85622--85641, within the definition headed “Proof outstanding” at I 85575.
The definition calls its assertions hypotheses at I 85598.
The outline index, neighbouring rows and obligations led to SA 17440, 17575--17585 and I 45962--46032, 53737--53838.
The account's full index does not index the unfinished remark `4.21:lem-live-region-geometry`.
Searching its source anchors found the conditional arguments at I 63772--63933.
Those arguments are prior work, not new proofs here.

The distinction between the two classes is decisive.
I 45992--46000 requires each previous region to be small and excludes creations and marks in its stated window.
It does not exclude joining.
I 118402 expressly says that condition (ii) bounds each previous component, not their number, and does not forbid joining.
SA 17575 and N 63684 expressly add that exclusion.
They already explain why two small regions can join without a creation.
The calculation below applies that known distinction to the account's particular core \(\mathsf C_C\).

## 2. Ports and their exact scope

Write \(u_j\) for a native cube side and \(a_j=R_j u_j\) for a boxing-cell side.
Here \(R_j=\check R_j\), and \(u_{j+1}=Lu_j\).
Thus the \(88M\) bound in N becomes \(88\) in I's native cube units.
This distinction follows I 62735--62769 and 53737--53743.
Use a common nonwrapping chart for the bounded sets below.

**Quiet boxes.** N 63749--63834 proves the following under its single-predecessor, no-joining class.
Let \(G_i=Z_i\cap C\), and let \(H_i\) be the next-grid hull of \(G_{i-1}\).
With \([s]\) denoting sup-norm enlargement by a physical distance, it obtains
\[
 \Omega_i^c\cap C=H_i^{[8a_i]},\qquad G_i=H_i^{[10a_i]}.
 \tag{1}
\]
Its lower prepared box is \(H_i^{[3a_i]}\).
Its upper boxes are \(H_{k_0+1}^{[3u_k-w_i]}\), with the offsets specified at N 63778--63784.
The cutoff \(\operatorname{side}(G_{k_0+1})\le100u_k\) gives
\[
 \operatorname{side}(H_{k_0+1})\le80u_k,
 \quad\operatorname{side}(Z''_k)\le86u_k,
 \quad\operatorname{side}(\Lambda_C)\le88u_k.
 \tag{2}
\]
This is their written construction. It does not turn a union of predecessors into one predecessor.

**The three boxes in I.** I 53776--53804 and 63788--63835 define
\[
 Z''_k=(\Omega_{k_0+1}^{\sim5})^c\cap C,
 \quad \Lambda_C=(\Omega_{k_0+1}^{\sim4})^c\cap C,
 \quad \widetilde\Lambda_C=\Lambda_C^{(1)}.
 \tag{3}
\]
The enlargements in (3) have side \(u_k\), since \(R_{k_0+1}u_{k_0+1}=u_k\).
I 78969 defines the core by removing two layers from \(Z''_{h+1}\); I 93532 repeats this definition.
With \(E_2\) denoting that removal, write
\[
 H:=Z'_h\cap C=\widehat{Z_h\cap C},
 \qquad
 \mathsf C_C:=\bigl((\Omega''_{h+1})^{\sim2}\bigr)^c\cap C
 =E_2(Z''_{h+1})\cap C.
 \tag{4}
\]
Here \(\Omega''_{h+1}=(Z''_{h+1})^c\), by I 63887.
The hull and the layers use boxing cells of side \(a_{h+1}\).
I 63870 gives the other form, \(\mathsf C_C=H^{\sim}\); I 78969 asserts that the two forms agree.
We compute both forms in section 4, rather than assume their equality under joining.
The hull is the union of meeting cubes, not a rectangular hull.
This is I 50046--50054 and 59496--59501.
The separate boxing map fills each connected small component; see I 50056--50095.
It does not fill space between disconnected components of \(H^{\sim}\).

I 63815--63835 obtains the bound \(112\) from a single small predecessor box.
I 63837--63857 obtains the distance \(10R_k-1\ge9R_k\) from the ten-layer step buffer.
I 63870--63906 obtains the core side and strip margin from a single small \(Z_h\cap C\).
The inequality used for its side is
\[
 100R_h+4LR_{h+1}\le104LR_{h+1}.
 \tag{5}
\]
Its margin calculation splits \(m<h\) from \(m=h\).
The former uses the retained strip inside \(Z_h\); the latter subtracts the birth enlargement.
The resulting lower bounds are \(R_h\) and \((R_h+1)/2\), respectively.
Its touching-cube argument uses \(Y^\sharp\subset Z''_k\) and the last layer in (3).
`geoh-live-ab.md` supplies the retained-strip input. It does not supply a single predecessor box.

**Probes.** I 62779--62788 defines a level-\(n\) probe by
\[
 \Delta_n\subset Q\subset\{x:\operatorname{dist}_n(x,\Delta_n)\le2\},
 \tag{6}
\]
for a current level-\(n\) cell \(\Delta_n\).
It is a cube, made of \(\pi_n\)-cubes, of side at most five.
I 63919--63924 proves (i1) conditional on a stronger separation in the probe's own units:
\(\operatorname{dist}_n(\Delta_n,Y^\sharp)\ge5/2\) for \(n>m\).
The birth-unit collar alone cannot be substituted for that input after rescaling.

I 63926--63933 then proves (i2) conditional on (i1) and disjoint strips.
Every strip side is at least \(R_m\ge38\) in its birth units, by I 63547--63562 and 63621--63623.
For \(n\le m\), every side of \(Q\) is at most five in those units.
An intersecting axis-parallel box with each side longer than the corresponding side of \(Q\) contains a vertex of \(Q\).
Indeed, its coordinate interval contains at least one endpoint of each interval of \(Q\); choose those endpoints.
Disjoint closed strips cannot receive the same vertex. There are \(2^d\) vertices.
This is the account's vertex argument, not the cell-ownership argument.
The intermediate assertion \(5/L\le1\) in I 63928 is unnecessary; \(5<38\) suffices for every odd \(L\ge3\).

N 85170--85189 uses this native-probe count in a reader estimate.
N 127772--127780 instead uses a \(909^d\) packing count for larger pockets against a seven-cell box.
N 127491--127502 counts at most \(2d\) same-level adjacent-strip choices at an anchor cell.
These are different incidence problems. Neither is a supplier of (i1).
Cell ownership remains the already checked clause (b) of `geoh-live-ab.md`.

## 3. A joining allowed by the account

**Result.** Clause (g)'s core-box assertion fails for the account's stated geometric construction rules.
The failure occurs before localisation, while the two old second-class regions are live.
It is a counterexample to the geometric implication requested here, not to a Yang--Mills existence theorem.

We specify the grids, the label transitions, the class test and the preparation.
As in `geoh-live-ab.md`, the domain is finite histories of the stated geometric rules.
No claim about the nonzero weight of a particular Wilson-field branch is needed or made.
If one restricts the class further by such a support condition, that restriction needs its own supplier.

Choose an odd \(L\ge103\), above any other fixed lower floors.
Choose a constant allowed radius \(R_j=R=L^p\), \(p\ge1\), over the finite window.
Take the fixed waiting depth \(N\) with
\[
 N_0=p+1<N\le R,
 \qquad h>N+1,\qquad k=h+N.
 \tag{7}
\]
These satisfy the geometric scale conditions in I 45827--45858 and 53762--53774.
Indeed, constant radii obey \(R_i\le LR_j\) and \(R_j\le(L+1)(i-j)^{\beta_0}R_i\) for \(i>j\).
Also \(L^{-N_0+1}R=1\), \(h>N>N_0\), \(k>N\), and \(R\ge103>38\).
The argument only needs this permitted constant-radius, constant-depth instance of those conditions.
Increasing \(p\) allows any further fixed radius floor.
All sets lie well inside a torus chart; choose its period as a sufficiently large odd multiple of the top grid spacing.

Use compatible centred grids in this chart.
Put \(a=a_{h+1}\), so \(a_h=a/L\).
At step \(h\), take two second-class outputs
\[
 Y_0=[-21a_h/2,21a_h/2]^d,
 \qquad Y_1=20ae_1+Y_0.
 \tag{8}
\]
They are small boxing-cell boxes. Each side is \(21R\) native level-\(h\) units.
Their gap is \((20L-21)a_h>a_h\).
The whole-component second-class rule gives their flat level-\(h\) labels and marks at \(h\), I 64479--64495.
Their fixed strips use the birth enlargement of I 63523--63544.

The size in (8) is compatible with the preceding quiet recursion.
A centred box of side \(21a_j\) lies strictly inside the central next-grid cell, since \(21<L\).
Its next-grid hull is that cell. Eight layers and then two layers produce side \(21a_{j+1}\).
For the geometric prehistory, put \(b=h-N\).
Start with two isolated small creations at \(b\), each placed inside the corresponding central level-\((b+1)\) boxing cell.
Any box of at most 100 boxing cells per side fits strictly inside that cell, with this choice of \(L\).
Choose its grid translation accordingly. Both copies use the same translation pattern.
The first quiet step produces the centred box of side \(21a_{b+1}\).
The preceding calculation then gives the boxes (8) after the \(N\) quiet steps.
For \(b<t\le h\), their gap is \((20L^{h+1-t}-21)a_t\ge(20L-21)a_t>a_t\).
At \(b\), even side \(100a_b\) leaves gap at least \((20L^{N+1}-100)a_b>a_b\).
Thus all these components are boxes with 1--100 cells per side, separated by at least one cell.
This checks admissible geometry fact (1), I 63547--63551, before the joining.
A creation at \(b\), the bottom of the birth waiting window, is allowed; the intervening steps have empty creation sets.
For \(b\le t<h\), one has \(t-b<N\), so that creation prevents eligibility by I 51178--51189.
At \(h\), \(h-b=N\). Each component is small, its preceding steps create nothing, and no earlier operation left a mark.
Thus each passes (i), (ii-a), and (ii-b) at \(h\). The whole-component second-class outcome gives (8).
This checks the geometric birth and waiting rules. It does not infer field support from chosen test labels.

For the step \(h\to h+1\), set every new seed and growth-test set to empty.
These are the no-creation transitions of I 50196--50229 and 50342--50372.
Let
\[
 Q_0=[-a/2,a/2]^d,
 \qquad Q_{20}=20ae_1+Q_0.
\]
Since \(21a_h<a\), the actual union-of-cubes hull is
\[
 Z'_h=\widehat{Y_0\cup Y_1}=Q_0\cup Q_{20}.
 \tag{9}
\]
There is no boundary ambiguity: both birth boxes lie strictly inside their hull cubes.

Write \(N_r\) for adding \(r\) layers of these boxing cells.
The step rule gives \(\Omega_{h+1}^c=N_8(Z'_h)\) and \(Z_{h+1}=\mathsf M N_{10}(Z'_h)\).
The eight-layer cubes have first intervals \([-17a/2,17a/2]\) and \([23a/2,57a/2]\).
Their gap is \(3a\), so \(\Omega_{h+1}^c\) has two components.
The ten-layer intervals are \([-21a/2,21a/2]\) and \([19a/2,61a/2]\).
They overlap in an interval of width \(a\), and their transverse intervals agree.
Consequently
\[
 \begin{aligned}
 \Omega_{h+1}^c
 &= [-17a/2,17a/2]^d\\
 &\quad\cup\bigl([23a/2,57a/2]\times[-17a/2,17a/2]^{d-1}\bigr),\\
 Z_{h+1}
 &= [-21a/2,61a/2]\times[-21a/2,21a/2]^{d-1}.
 \end{aligned}
 \tag{10}
\]
The boxing map fixes the second box.
It is one component, with sides \(41a,21a,\ldots,21a\), all below the cutoff \(100a\).
The two old components have joined. No creation set was used.
This is the joining mechanism already identified in SA 17575 and N 63684.

At step \(h+2\), the box in (10) lies strictly inside the central boxing cell of side \(La\).
Indeed its largest coordinate magnitude is \(61a/2<La/2\), since \(61<L\).
Every subsequent no-creation step therefore has
\[
 \Omega_i^c=[-17a_i/2,17a_i/2]^d,
 \qquad Z_i=[-21a_i/2,21a_i/2]^d
 \quad(h+2\le i\le k).
 \tag{11}
\]
Induction proves (11): the preceding box again fits inside the central next-grid cell.
All predecessors remain small. Earlier label entries stay unchanged.

For \(h<t<k\), the marks at \(h\) lie in \((t-N,t)\).
Condition (ii-b) forbids an operation on their containing component.
At step \(k\), the exclusion interval is \((h,k)\); it contains neither mark.
The component \(C=Z_k\) satisfies all three class conditions in I 45992--46000:

- **(i).** Each side of \(C\) is \(21a_k<100a_k\), or \(21R<100R\) native level-\(k\) units.
- **(ii-a), no creation.** All seed and growth-test sets in the steps \(h\to h+1,\ldots,k-1\to k\) are empty.
  The joining in (10) therefore introduces no creation set.
- **(ii-a), earlier sizes.** Each level-\(h\) component has side \(21a_h\).
  The joined level-\((h+1)\) component has sides \(41a\) and \(21a\).
  Every later component has side \(21a_i\); the prehistory components were checked above.
  Each separate region fits its own \(100a_i\) cube. Every component also satisfies admissible geometry fact (1).
- **(ii-b).** Only the operations at \(h\) leave large-field marks. Their level lies outside \((k-N,k)=(h,k)\).
  No intervening operation is eligible, since \(t-N<h<t\) for \(h<t<k\).

I 55350--55418 allows retained regions from an operation at \(s=h\) inside \(Z_h\cap C\).
Its reading of condition (ii) at levels \(h+1,\ldots,k\) also passes here.
Indeed, \(Z_{h+1}\cap C\) is the single \(41a\)-by-\(21a\) box, and each later \(Z_i\cap C\) is a \(21a_i\) cube.
I 118402 states why the two level-\(h\) components need not satisfy one common size bound.
The second clause bounds each previous component. The first forbids creation but not “the joining of components”.

The class therefore treats \(C\). Each \((Y_r,h)\) remains live at its preparatory site.
The containing component has not yet passed through localisation, the death event in I 63540--63544.

## 4. The core is disconnected, while preparation remains possible

The old level-\(h\) entry in \(C\) is still \(Y_0\cup Y_1\).
First use the defining form at I 78969 and 93532.
I 53783 gives \(Z''_{h+1}=(\Omega_{h+1}^{\sim5})^c\cap C\).
The two \(17a\) cubes in (10) are separated, so removing five layers shrinks each separately to side \(7a\).
Thus \(Z''_{h+1}=N_3(Q_0)\cup N_3(Q_{20})\).
Removing two more layers gives two cubes of side \(3a\).
The other form at I 63870 adds one layer to each hull cube and gives the same set:
\[
 \begin{aligned}
 \mathsf C_C
 &=E_2\bigl(N_3(Q_0)\cup N_3(Q_{20})\bigr)\cap C\\
 &=N_1(Q_0\cup Q_{20})\\
 &=[-3a/2,3a/2]^d
 \cup\bigl([37a/2,43a/2]\times[-3a/2,3a/2]^{d-1}\bigr).
 \end{aligned}
 \tag{12}
\]
Both boxes lie in \(C\), so intersection with \(C\) removes nothing.
They have a gap of width \(17a\) in the first direction.
In particular, \(0\) and \(20ae_1\) belong to \(\mathsf C_C\), but their midpoint \(10ae_1\) does not.
Every rectangular box containing the first two points contains their midpoint.
Thus \(\mathsf C_C\) is not a box under either form. This contradicts the box sentence of (g) at I 85629.
Its total coordinate spans are \(23a\) and \(3a\).
In level-\(h\) units, even the larger span is \(23LR\le104L\check R_{h+1}\).
So exceeding the stated side bound is not the failure.

This failure does not prevent the stated preparation from being formed.
The five-layer removal used above gives explicitly
\[
 Z''_{h+1}
 =[-7a/2,7a/2]^d
 \cup\bigl([33a/2,47a/2]\times[-7a/2,7a/2]^{d-1}\bigr)
 =N_3(Q_0\cup Q_{20}).
 \tag{13}
\]
These are two \(7a\) cubes with gap \(13a\). Each contains its component of (12), with two layers to spare.
Each also contains its old \(Y_r\), with margin \((7-21/L)a/2>a/R=u_{h+1}\).
For the remaining lower indices \(h+2\le i\le k_0\), (11) gives
\(Z''_i=[-7a_i/2,7a_i/2]^d\).
These sets are nested, including the bottom union, since \(L\ge103\).
If this lower range is nonempty, its first gap is \((7L-47)a/2>La=a_{h+2}\).
Every later lower gap is \(7(1-1/L)a_i/2>a_i\).
Thus these gaps exceed the required native-cube sides.

At the change of scale, \(k_0+1\ge h+2\) by (7), and \(a_{k_0+1}=u_k\).
Consequently \(\Omega_{k_0+1}^c\) is the cube of side \(17u_k\) in (11).
At these upper levels the input is one quiet box.
Use N 63778--63825's explicit completion as an instance of I 53776--53785's upper rules:
\[
 Z''_i=Q_*^{[3u_k-w_i]},\qquad
 Q_*=[-u_k/2,u_k/2]^d,\qquad k_0<i\le k,
 \tag{14}
\]
where
\[
 w_{k_0+1}=2u_k,\quad w_k=0,\quad
 w_i=\sum_{q=i+1}^k u_q\quad(k_0+2\le i<k).
\]
These offsets are integer multiples of the appropriate \(u_i\), so all faces lie on their prescribed grids.
For \(k_0+2\le i<k\), the next outward movement is \(w_i-w_{i+1}=u_{i+1}\).
At the first upper pair, \(w_{k_0+2}\le Lu_k/(L-1)\), if that index is below \(k\).
Its gap is therefore at least \((L-2)u_k/(L-1)>u_k/L\ge u_{k_0+2}\).
If that index equals \(k\), the gap is \(2u_k\).
The bottom upper box has half-side \(3u_k/2\).
If \(k_0>h+1\), the preceding box has half-side \(7u_k/(2L)\).
Its gap is \((3-7/L)u_k/2>u_k\).
If \(k_0=h+1\), the preceding union reaches \(47u_k/(2L)\), by (13).
Its gap is \((3-47/L)u_k/2>u_k\), since \(L>47\).
This checks the upper one-layer gaps as well as the lower ones.

In particular, (3) gives the centred boxes
\[
 \operatorname{side}(Z''_k)=7u_k,\qquad
 \operatorname{side}(\Lambda_C)=9u_k,\qquad
 \operatorname{side}(\widetilde\Lambda_C)=11u_k.
 \tag{15}
\]
Since \(Z=C\) has side \(21Ru_k\),
\[
 \operatorname{dist}_k(\widetilde\Lambda_C,Z^c)
 =\frac{21R-11}{2}\ge9R.
 \tag{16}
\]
The last inequality is \(3R\ge11\), which follows from \(R\ge103\); also \(11\le112\).
Thus even clause (f) holds in this example. Its main box does not repair the different core in (12).

The strips are also harmless here.
Their half-side is \(21a_h/2+q_hu_h\), with \(q_h=\lfloor(R-1)/2\rfloor\).
This is less than \(11a_h=11a/L\).
Each strip lies well inside its respective component of (12).
Its distance to that component's exterior exceeds
\[
 \frac32a-\frac{11a}{L}>a
 =LRu_h\ge\frac{R+1}{2}u_h.
 \tag{17}
\]
Since \(a=La_h\) and \(L\) is odd, the core boundaries lie on level-\(h\) boxing-cell faces.
For each \(Q\in\{Q_0,Q_{20}\}\), the boundary of \(N_1(Q)\) lies in \(N_1(Q)\setminus Q\).
This set lies outside \(Z_h\) and inside \(Z''_{h+1}\).
This moat is in \(\Lambda_h\cap(\Omega''_{h+1})^c\subset\Omega_h\setminus\Omega''_{h+1}\), hence in zone \(h\).
The core lies in \((\Omega''_{h+1})^c\), so its cells have level at most \(h\).
Its aligned boundaries make it a union of these cells, as in I 63879--63892.
The two strips lie in separate components of (12), so they are disjoint.
Finally, \(Y_r^\sharp\subset Z''_{h+1}\subset Z''_k\).
Any cube of level at most \(k\) has side at most \(u_k\).
If it touches a strip, it lies in the one-layer enlargement \((Z''_k)^{(1)}=\Lambda_C\).
There is no failure of unique cell ownership or of the persistent birth collar.
Only the assertion that this core is one box has been contradicted.

## 5. Endpoints and the exact scope of the failure

The account's open endpoint permits the two marks at \(m=h\) in (8).
Replacing only \((h,k)\) by \([h,k)\) excludes that particular history.
It does not remove the joining obstruction.

For the closed-endpoint variant, put both births at \(m=h-1\), with side \(21a_{h-1}\) and the same centres.
The no-creation step to \(h\) produces precisely the two boxes of side \(21a_h\) used in (9).
For every \(m<t<k\), the mark at \(m\) belongs to the closed window \([t-N,t)\).
Indeed \(t\le k-1=m+N\), so \(t-N\le m<t\).
No intervening operation can consume it.
At \(k\), the window starts at \(h=m+1\) and excludes the old mark.
Equations (9)--(16) are unchanged, and the fixed old strips are smaller.
Thus (12) remains a counterexample when only the endpoint is changed.

The full rules of SA 17575 and N 63684 also exclude joining throughout this window.
They exclude both examples because \(C\cap Z_h\) has two components and the step at \(h+1\) joins them.
Their quiet-box proof (1)--(2) is therefore consistent with the counterexample.
It applies to a stricter class.

The account itself adds a no-joining condition in later sections.
I 115866 says “We assume moreover” before requiring that no components join inside \(Z\) during the window.
I 125168 assumes this throughout its section. I 143731 adds it as hypothesis (a).
Each is an added assumption of a later section.
None is part of Definition 4.14's class, Definition 4.22's live-region hypotheses, or the proof at I 63772--63935.
Imposing that condition would exclude the example; I 118394 uses it to obtain one previous component.
The route remark at I 85716--85718 does mention nesting.
In this chapter nesting means inclusion, as the use \(Z_{j'+1}\subset Z_{k-1}\) at I 91947 shows.
The example satisfies inclusion. Inclusion does not prohibit joining.

The first invalid sentence in the account's core argument is I 63870--63871:
after defining \(\mathsf C_C=(Z'_h)^{\sim}\cap C\), it asserts that this set is rectangular.
The sentence at I 63872 is also false in this example, not merely unsupported:
\[
 \operatorname{span}_1(Z_h\cap C)
 =20a+21a_h=(20L+21)a_h>100a_h.
\]
So \(Z_h\cap C\) cannot lie in one cube of side \(100\check R_h\) in level-\(h\) units.
Condition (ii-a) bounds each previous region separately.
It does not identify their union with one region.

Claude's check also identifies why the original separation \(6a\) was insufficient.
At that separation, \(E_2(Z''_{h+1})=[-3a/2,15a/2]\times[-3a/2,3a/2]^{d-1}\), a single box.
The other form, \(N_1(Q_0\cup Q_6)\), has two components with gap \(3a\), where \(Q_6=6ae_1+Q_0\).
Thus the equality asserted at I 78969 can itself fail under joining.
The repaired separation \(20a\) makes both forms equal and refutes their box claim directly.

Three possible changes must not be confused with proofs on the present rules.
One could impose the outlines' single-predecessor conditions or the account's later no-joining assumption.
One could replace the core in (4) by the rectangular hull of the union.
One could formulate the conclusion componentwise for a union of cores.
The first changes the class. The other two change the core or its required geometry.
Each needs a separate check of its consumers; none is adopted here.
In particular, the remark calling the core rectangular cannot itself serve as an extra input to prove that claim.

This negative result has one witness and one scope: the core-box assertion for the printed geometric transition class.
It claims no impossibility for repaired rules, no failure of a field integral, and no audit conclusion.
The joining mechanism is Sussman--Alpoge's prior observation, SA 17575, N 63684 and I 118402.
Claude's check supplied the separation repair. Sections 3--4 match it to both forms of the account's core.

## 6. Clause table and first open input

“Prior proof” below refers to `geoh-live-ab.md` and its single Claude check.
“Conditional port” describes a written source argument with the named supplier still required.

| Clause | Result on the account's stated class | Evidence or remaining supplier |
|---|---|---|
| (a), for \(i\ge m\) | Prior proof | `geoh-live-ab.md`, equation (3) |
| (b), including unique cell ownership | Prior proof | Its section 5; this is not probe multiplicity |
| (c), (d), (e), (h) | Prior proof | Its sections 3--6, including the open-endpoint interruption |
| (f): main enlarged box, side \(112\), margin \(9R_k\) | Conditional port; not established here for the entire class | I 63788--63857; N 63749--63834 requires single predecessors. Equations (15)--(16) verify (f) in the counterexample |
| (g): \(m\le h\) | Prior proof | The account's open exclusion window |
| (g): \(\mathsf C_C\) is a box | **False on the stated geometric rules** | The two components and missing midpoint in (12); all class tests checked in section 3 |
| (g): cell union, side bound, strip containment and margin, touching-cube inclusion | Existing conditional arguments; no claim of the full clause | I 63870--63906. Section 4 checks these geometric assertions in the counterexample; they do not imply connectedness |
| (i1): probe level at most birth level | Conditional port; still open here in general | I 63919--63924 uses separation in the probe's own units, not only the proved birth-unit collar |
| (i2): at most \(2^d\) strips per probe | Conditional port given (i1) | I 63926--63933; vertex argument in section 2; disjointness already supplied |
| \(909^d\) pocket packing and \(2d\) adjacent-anchor count | Different counts; not used as substitutes | N 127772--127780 and 127491--127502 |
| Contour, cell-counting and summation hypotheses after I 85644 | Outside this task | No conclusion here |

**First open input:** none for the geometric counterexample, which is stopping outcome (b).
To resume an affirmative proof of the full block, first supply a corrected class/core contract.
The unchanged contract admits (12), so a supplier lemma alone cannot make its box assertion true.
After such a correction, (i1)'s separation in the probe's own units remains to be supplied or matched to an existing proof.
