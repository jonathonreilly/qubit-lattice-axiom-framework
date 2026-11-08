# A finite-history invariant for live strips

Ethan and Levent,

Your complete account leaves the live-region clauses at [CA-I 85575–85644](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85575-L85644) headed
“Proof outstanding”. It uses them as hypotheses. This note supplies the
finite-history persistence argument for clauses (a), (b), (c), (d), (e), and (h).
For (g), it supplies only \(m\le h\). The restrictions are listed below.
The searches in §8 found uses and geometric ingredients in your revised outline,
but no proof there of this invariant through all the stated moves.

The definitions, the statement of the construction rules, and the arguments cited here are yours.
The large-field method, the T rule and the preparation geometry are Tadeusz Bałaban's.
Your account cites his CMP **119** (1988), §3, for T, and CMP **122** (1989),
pp. 175–202, §1, for preparation. We use the rules as your account states them.

Codex (gpt-6-astra) wrote the proof and this note. Claude (Opus 5.5) checked the proof line by line, and its repairs are applied.
This is a proposed proof for your review. It is research text, not an audit.
No computation supplies a proof step.

**Sources.** **I** means your [complete account, Part I][account], at commit
`31a47c543775`. **SA** means your [YM4_sketch_500.tex][old-outline] at that commit.
**N** means your [YM4_1400.tex][new-outline] at commit
`2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
All line references below use these fixed revisions.

## 1. The target clauses and what this note proves

At [CA-I 85575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85575) the heading is:

> Geometry and counting of live large-field regions. Proof outstanding

At [CA-I 85598](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85598) you say:

> The following statements are used in this chapter as hypotheses.

Here are the geometric clauses at [CA-I 85600–85642](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85600-L85642), with the TeX rendered.
Their notation and mathematical statements are unchanged.

> **(a)** The number \(s_i(Y)\) satisfies
> \[
> s_i(Y)\le (101\,\check{R}_m-1)\,L^{-(i-m)}\le101\,\check{R}_i.
> \]
>
> **(b)** A cell meeting \(Y^{\sharp}\) has level at most \(m\) and lies in \(Y^{\sharp}\).
> The strips of distinct live large-field regions are disjoint, and a cell lies in at most one of them.
>
> **(c)** For the current small-field region \(\Omega_{m+1}\),
> \(\operatorname{dist}_m(Y^{\sharp},\Omega_{m+1})\ge\tfrac52\check{R}_m\).
> Every cell at \(\operatorname{dist}_m\)-distance less than \(\tfrac52\check{R}_m\) from \(Y^{\sharp}\)
> has level at most \(m\), and, for every \(i>m\), this neighbourhood of \(Y^{\sharp}\)
> lies in the component of \(\Lambda_i^c\) containing \(Y\). This is the region's own collar.
> The collar made by the operation \(\mathbf T\) is wider; after an interrupted preparation
> whose index \(h_1\) equals \(m\) only the width \(\tfrac52\check{R}_m\) is left,
> and clause (c) claims no more than this width.
>
> **(d)** At the site \((\mathrm T)\) of the step from level \(i\) to level \(i+1\),
> \(\operatorname{dist}_i(Y^{\sharp},\Omega_{i+1})\ge7\check{R}_i\).
>
> **(e)** At the site \((\mathrm L)\) or \((\mathrm P)\) of \(\mathbf R_k\), let \(C''\)
> be the component of \(\Lambda_k^c\) containing \(Y\). If \(C''\) is not treated, then
> \(Y^{\sharp}\subset C''\) and \(\operatorname{dist}_k(Y^{\sharp},Z)\ge\check{R}_k\).
>
> **(f)** Let \(C\) be the component of \(\Lambda_k^c\) containing \(Y\) (the component
> written \(C''\) in (e)), and let \(\Lambda_C\) and \(\widetilde\Lambda_C\) be the two sets
> attached to \(C\) by the large-field operation \(\mathbf R_k\). The set
> \(\widetilde\Lambda_C\) is a box whose sides are at most \(h_\sharp=112\), measured at
> level \(k\), and \(\operatorname{dist}_k(\widetilde\Lambda_C,Z^c)\ge9\check{R}_k\).
>
> **(g)** Let the component \(C\) containing \(Y\) be treated at \(\mathbf R_k\), and
> let \(h\) denote the level attached to this treatment. Then \(m\le h\).
> The set \(\mathsf C_C\) is a box, a union of cells of levels at most \(h\), with sides
> of at most \(104L\check{R}_{h+1}\) units of level \(h\). Moreover
> \(Y^{\sharp}\subset\mathsf C_C\) and
> \[
> \operatorname{dist}_h(Y^{\sharp},\mathsf C_C^c)\ge\tfrac12(\check{R}_h+1).
> \]
> A cube of any level at most \(k\) touching \(Y^{\sharp}\) lies in \(\Lambda_C\).
>
> **(h)** At the site \((\mathrm P)\) of \(\mathbf R_k\): if the component containing
> \(Y\) is treated, then \(\operatorname{dist}_{h+1}(Y^{\sharp},R_\nu)\ge\tfrac52\check{R}_{h+1}\)
> for every collar \(R_\nu\); if it is not treated, then
> \(\operatorname{dist}_k(Y^{\sharp},R_\nu)\ge\check{R}_k\) for every collar \(R_\nu\).
> No integration bond of \((\mathrm P)\) lies on a strip.
>
> **(i1)** A probe meeting \(Y^{\sharp}\) has level at most \(m\).
>
> **(i2)** A probe meets the strips of at most \(2^d\) live large-field regions.

The contour hypothesis starts at [CA-I 85644](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85644) and continues through [CA-I 85648](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85648):

> **Contour hypothesis.** Let \(\mathsf c_\wedge>0\) be the zone weight of the weighted
> contour distance \(d^\wedge\). Then \(d^\wedge\) obeys the triangle inequality.
> A contour pays at least \(\mathsf c_\wedge\) for each zone it crosses.
> On a set all of whose cells have level at most \(n\), a contour pays at least
> \(\mathsf c_\wedge\) for each level-\(n\) unit of its Euclidean length.
> Payments on disjoint arcs add.

| Clause | Result of this proof | Location below |
|---|---|---|
| (a) | Proved for \(i\ge m\); no assertion on arbitrarily finer grids | (3) |
| (b) | Proved: level ceiling, cell saturation, disjoint strips, unique cell ownership | §5 |
| (c) | Proved: birth collar, cell ceiling in the collar, containment in the same component | (9)–(12), §5 |
| (d) | Proved: T-site distance at least \(7\check R_i\) | §5 |
| (e) | Proved at P and L for an untreated component, including an exited sibling | §§5–6 |
| (f) | Not touched | — |
| (g) | Partly proved: only \(m\le h\) | §§3, 5 |
| (h) | Proved: both collar bounds and exclusion of every P integration bond | §§5–6 |
| (i1), (i2) | Not touched | — |
| Contour hypothesis | Not touched | — |

Here “proved” means a written implication from the construction rules below.
In (c), a domain is tested only after its level exists.
At R at step \(k\), an old live strip has \(m<k\).
A new second-class output enters the next cycle.

### Construction rules used below, as your account states them

| Input | Source and use |
|---|---|
| Your nested cube grids, native cells, touch and meet conventions | [CA-I 62735–62780](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L62735-L62780). Native cells have side one in their own cube units. |
| Your fixed birth strip and its lifetime | [CA-I 63523–63544](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63523-L63544). An interrupted attempt is not a new second-class strip. |
| Your component size and separation at birth | [CA-I 63547–63562](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63547-L63562); the fixed-grid strip calculation is [CA-I 20441–20468](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L20441-L20468). |
| Your adjacent radius ratios and scale comparison | [CA-I 63563–63569](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63563-L63569); telescoping proof at [CA-I 63643–63649](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63643-L63649); radius floor at [CA-I 63621–63623](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63621-L63623). |
| Bałaban's T rule in your eight-layer form, followed by two further layers and monotone boxing | [CA-I 50196–50229](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50196-L50229) and [CA-I 50342–50368](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50342-L50368). Your T-buffer proof is [CA-I 12187–12265](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L12187-L12265). |
| Your open exclusion window and whole-component eligibility | [CA-I 45985–46032](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45985-L46032). Operations at the lower endpoint are allowed. |
| Bałaban's five-layer lower preparation | [CA-I 53783](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53783); its layer side is given at [CA-I 63703–63716](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63703-L63716). |
| Bałaban's upper prepared gap | [CA-I 53778–53781](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53778-L53781), including the change of scale. It is an input rule, not inferred from N's quiet-box formulas. |
| Bałaban's nested prepared members, main box, and stage collars | [CA-I 53786–53819](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53786-L53819); \(N>N_0\ge2\) and \(h+1\le k_0\) at [CA-I 53773](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53773) and [CA-I 63590–63592](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63590-L63592). |
| Your completed whole-component outcomes | [CA-I 64479–64497](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64479-L64497). A completed localisation consumes the old pocket. |
| Your frozen partial preparations, including \(n^+=n+1\) | [CA-I 64417–64442](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64417-L64442) and [CA-I 64527–64535](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64527-L64535). Arrested attempts are defined at [CA-I 64796–64847](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64796-L64847). |
| Your integration coordinates and incident-bond convention | [CA-I 74309–74320](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L74309-L74320) and [CA-I 159058–159075](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L159058-L159075). |
| Your late exits and timing of a later attempt | [CA-I 132008–132026](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L132008-L132026) and [CA-I 132162–132176](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L132162-L132176). |

Use periodic sup-distances on the torus. The local birth and operation boxes
have the admissible nonwrapping charts supplied with these rules.
No lift of every recursive carrier is assumed or proved.

Your earlier partial proof at [CA-I 63772–63800](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63772-L63800) explicitly starts with clauses (e)–(i) of your Lemma 4.21
and takes connectedness and retained-strip containment as input.
The treated-collar subtraction at [CA-I 63908–63916](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63908-L63916) is already yours.
We supply the finite-history retention needed by that subtraction, not a new subtraction formula.
We do not use the invocation of live-region geometry at [CA-I 64468–64472](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64468-L64472) as an input.

## 2. The actual strip and the cell convention

Write \(u_j\) for the physical side of a cube of \(\pi_j\).
Thus \(u_i/u_m=L^{i-m}\).
Write \(q_j=m_\sharp(j)=\lfloor(\check R_j-1)/2\rfloor\).
Use your parameter floors: odd \(L\ge3\), \(M\ge1\), and \(\check R_j\ge38\).
The radii are powers of \(L\), with \(\check R_j/\check R_{j+1}\in\{1,L\}\).
They are scale inputs, as specified at [CA-I 63563–63569](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63563-L63569) and 63621–63623.
Local birth and operation boxes use their supplied admissible torus charts.

A live pocket is a second-class region \((Y,m)\) created by \(\mathbf R_m\).
Its strip is the fixed set
\[
 S_Y=Y^\sharp=Y^{(q_m)}.
 \tag{1}
\]
The enlargement uses \(\pi_m\)-cubes, once, at birth.
It is not recomputed on the current grid.
These are your definitions, [CA-I 63523–63544](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63523-L63544).
An interruption before localisation does not kill the old pocket.
A later localisation of its containing component does kill it, whichever class follows.
An arrested attempt is a separate mark, [CA-I 64796–64847](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64796-L64847).
It does not create another second-class strip around the containing component.
Otherwise nested arrests would create overlapping copies of the very object being counted.

Two cell notions must stay distinct.
Your boxing cells used in T have side \(\check R_j u_j\).
The native cells in [CA-I 62763–62769](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L62763-L62769) have side \(u_j\).
The current determining sequence assigns each native cell its level.
Clause (b) concerns these native cells.
It does not require one large strip to fit inside a single native cell.
The clause's ownership assertion assigns each current cell to at most one live strip.

For precision, assign boundary points by a fixed half-open grid convention.
Use the closed carriers for distance and touching.
Meeting means sharing a cube on one grid, or an interior point on different grids.
This is the convention of [CA-I 62740–62748](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L62740-L62748), with boundary ownership made explicit.
Once cell saturation and strip disjointness are established, define
\[
 \operatorname{owner}(\Delta)=
 \begin{cases}
 (Y,m),&\Delta\text{ meets }S_Y,\\
 \varnothing,&\text{no live strip meets }\Delta.
 \end{cases}
 \tag{2}
\]
Formula (2) does not itself prove that its first case is single-valued.

The birth size bound is your calculation.
If the birth component has side at most \(100\check R_m u_m\), then
\[
 s_i(Y)=s_m(Y)L^{-(i-m)}
 \le(100\check R_m+2q_m)L^{-(i-m)}
 \le(101\check R_m-1)L^{-(i-m)}\le101\check R_i.
 \tag{3}
\]
The first bound is the birth component specification in [CA-I 63547–63562](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63547-L63562).
The last is the proved radius comparison in [CA-I 63643–63649](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63643-L63649).
The identity uses the fixed strip, not a succession of enlargements.
For simultaneous births, separated boxing cells give
\(\operatorname{dist}_m(S_Y,S_{Y'})\ge \check R_m-2q_m\ge1\).
This is your same-level calculation at [CA-I 20441–20468](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L20441-L20468).
It does not establish separation between two different birth levels.

## 3. The lower prepared member on the same history

Put \(a_j=\check R_j u_j\). This is a boxing-cell side, not a native-cell side.
For a set of boxing cells, \(N_r\) means adjoining \(r\) cell layers.
For \(t\ge2\), the T rule is
\[
 (\Omega_t^{T})^c
   =N_2Q'_t\cup N_4P'_t\cup N_8\widehat{Z_{t-1}},
 \qquad Z_t^{T}\supset N_2(\Omega_t^{T})^c.
 \tag{4}
\]
Boxing and subsequent failures only enlarge the second set.
This is Bałaban's T rule in the eight-layer form your account derives at [CA-I 50196–50229](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50196-L50229), with the two further layers and monotone boxing at [CA-I 50342–50368](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50342-L50368).
[SA 17317–17332](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17317-L17332) prints the same construction.
Thus new failures and joining cannot reduce either buffer in (4).
The T-buffer argument is already proved in [CA-I 12187–12265](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L12187-L12265); we use it here.
That lemma's coupling argument is unnecessary because the present radius comparison is already available.
The first step has its separate tests and no incoming pockets, [CA-I 50231–50300](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50231-L50300).
No first-step version of (4) is needed for a live strip.

For an attempt on \(C\) at step \(k\), put \(h=k-N_k\) and \(D_i=Z''_i\cap C\).
The lower preparation uses five layers of the boxing grid of level \(i\).
Its layer side is \(a_i\), for \(h<i\le k_0\).
The five-layer rule is [CA-I 53783](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53783); the layer side is specified at [CA-I 63703–63716](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63703-L63716).
[N 63773–63812](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63773-L63812) makes the lower construction explicit for its quiet-box special case.
The first member has \(h+1\le k_0\), since \(N_k>N_0\).
The upper members use their prescribed native grids.
They are nested and obey
\[
 D_i\subset D_{i+1},\qquad
 \operatorname{dist}(D_i,D_{i+1}^{c})\ge u_{i+1}
 \quad(h<i<k).
 \tag{5}
\]
Distances here are inside the operation box, with its exterior margin retained.
The upper gap is the stated one-layer rule at [CA-I 53778–53781](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53778-L53781).
[N 63798–63825](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63798-L63825) gives quiet-box formulas for the special case without joining; those formulas are not used for the broader class here.
We use that existing preparation; we do not replace its grid or selector.
In the lower range, its gap follows directly from (4) and (6), applied at consecutive levels.
The next hull contains \(Z_i\cap C\), which contains \(D_i\).
Its three added layers give distance at least \(3a_{i+1}\ge u_{i+1}\).
The upper range uses the one-layer rule quoted at [CA-I 53778–53781](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53778-L53781).
This proof does not use the statement at [CA-I 64468–64472](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64468-L64472) that live-region geometry already applies.

**Lower-member calculation.** On the actual label at this attempt,
\[
 N_3 H_{h+1}\subset D_{h+1},
 \qquad H_{h+1}:=\widehat{Z_h\cap C}
       \quad\text{on the level-}(h+1)\text{ boxing grid}.
 \tag{6}
\]
Here is the endpoint check needed to use the published calculation.
Your account's exclusion interval is \((h,k)\), at [CA-I 45992–46032](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45992-L46032).
An earlier standing second-class region in \(C\) therefore has birth level \(m\le h\).
A standing arrest in \(C\) has step at most \(h\), by the same rule.
The closed lower endpoint of [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) is stronger and is not used here.

Trace a surviving component of the current \(Z_h\cap C\) back to step \(h+1\).
Each intervening T step leaves the earlier entries unchanged.
An intervening completed operation on that component would remove its level-\(h\) entry.
An intervening interruption would leave a standing mark in \((h,k)\).
If that mark later disappeared, a completed operation would again remove the entry.
The first alternative contradicts survival; the second contradicts eligibility.
Operations on other components cannot cut this component or its connected buffer.
They act on whole top components.
Thus the eight-layer buffer made at step \(h+1\) survives in the current \(\Omega_{h+1}^c\).
In particular,
\[
 N_8H_{h+1}\subset\Omega_{h+1}^c\cap C.
 \tag{7}
\]
This uses your surviving-component argument at [N 63718–63771](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63718-L63771), with its endpoint use stated explicitly.
Only steps strictly above \(h\) occur in this argument.
An operation at \(h\) is already included in the input to T at \(h+1\).
No prohibition of that operation is needed.
Joining may add other predecessors. It does not invalidate the inclusion (7).

Now remove five layers from the eight-layer buffer.
In cell indices, a cell within three steps of \(H_{h+1}\) is at least six steps from any exterior cell.
Five layers added to that exterior cannot reach its interior.
The retained closed carriers give (6).
This also proves the inclusion for a union of hull cells; no box equality is needed.
For a box, it is exactly your erosion calculation, [N 63785–63812](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63785-L63812).
All its sets lie in \(C\), since (4) also supplies the ten-layer buffer.
The same tracing and erosion apply at every lower index \(h<i\le k_0\).
They give \(N_3\widehat{Z_{i-1}\cap C}\subset D_i\) on that index's boxing grid.
This justifies the lower gaps used in (5), including when the retained lower label contains an older arrest.

Consequently, for any old live \((Y,m)\) in \(C\),
\[
 Y\subset Z_h\cap C,\qquad
 \operatorname{dist}_{h+1}(Y,D_{h+1}^c)\ge3\check R_{h+1}.
 \tag{8}
\]
The first inclusion uses retention of \(Y\) and label nesting.
It does not assert that the larger strip already lies in \(Z_h\) when \(h=m\).

## 4. The critical interrupted cycle

Fix one actual history with a live pocket \((Y,m)\).
Suppose its containing component \(C\) is attempted at step \(k\), with \(h=k-N_k=m\).
Include a standing interrupted mark \(\mathfrak a=(A,m,n,n^+,e)\) in \(C\).
At step \(m\), \(A\) and \(Y\) were different components with different outcomes.
Later T steps may join their descendants.
Your account's class permits this joining and the mark at its lower endpoint, [CA-I 45992–46032](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45992-L46032).
The lower index is shared; the earlier interiors and their determining cells need not be flat.
In (6), retain all of \(Z_m\cap C\), including the interrupted component.
Replacing that set by \(Y\) would discard the history that must be checked.
All sets in this section belong to this history and its current determining label.
We do not infer existence of a field configuration by assigning arbitrary test outcomes.
The argument covers every actual branch with these data.

The strip extends beyond \(Y\) by \(q_m u_m\).
Equation (8), converted to birth units, gives
\[
 \begin{aligned}
 \operatorname{dist}_m(S_Y,D_{m+1}^c)
 &\ge3L\check R_{m+1}-q_m\\
 &\ge3\check R_m-\frac{\check R_m-1}{2}
   =\frac52\check R_m+\frac12.
 \end{aligned}
 \tag{9}
\]
The worst radius comparison is \(\check R_m=L\check R_{m+1}\).
When the hull adds no extra width, this calculation leaves exactly the displayed lattice margin.
The contract uses only \(5\check R_m/2\).
It does not require equality with that weaker number.

Set
\[
 B_Y:=\{x:\operatorname{dist}_m(x,S_Y)<5\check R_m/2\}.
 \tag{10}
\]
Equation (9) puts \(B_Y\) inside the first prepared member.
The same member contains \(A\), since the standing mark remains in \(Z_m\cap C\).
Thus the old interruption is not integrated by a preparatory collar of this attempt.
Every later prepared member contains it by (5).
Stopping after any prefix therefore leaves it outside the current \(\Omega_{m+1}\).
Stopping before any relabelling leaves the wider T buffer instead.

One branch needs separate care.
At the exit corresponding to Bałaban's (1.55), the variable change is performed but its fluctuation integral is not.
The retained geometry has \(n^+=n+1\), not \(n\).
This is [CA-I 64420–64442](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64420-L64442) and 64527–64535; the variable description is [CA-I 81735–81756](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L81735-L81756).
For \(n=0\), it already retains \(D_{m+1}\).
Thus (9) applies even when no fluctuation integral was completed.
For \(n>0\), every additionally retained member contains \(D_{m+1}\).
The same bound applies.
The stopped component stays in the top large-field region, and its mark stands.

Now perform the next complete cycle, T at \(k+1\) followed by R at \(k+1\).
The old strip lies in the stopped top component of \(Z_k\).
Equation (4) therefore gives
\[
 \operatorname{dist}_k(S_Y,\Omega_{k+1}^{T})
       \ge8L\check R_{k+1}\ge8\check R_k>7\check R_k.
 \tag{11}
\]
The step changes no earlier domain, including \(\Omega_{m+1}\).
New failures may join this component to others. Its existing buffer remains.

R at \(k+1\) cannot treat the resulting component.
Its standing mark has step \(k\), strictly inside \((k+1-N_{k+1},k+1)\), since \(N_{k+1}\ge3\).
Every treated component is consequently different from this component.
Distinct top components are separated by at least \(a_{k+1}\).
All their preparation collars and their main integration regions stay inside those components.
Thus every such region is at distance at least \(\check R_{k+1}\) from \(S_Y\), in level-\(k+1\) units.
Their integration bonds cannot bridge that gap; section 6 gives the bond check.
No operation in this cycle changes the old strip or its birth collar.

If a still later attempt on this lineage occurs at step \(b\), its lower index satisfies \(h_b\ge k\).
This is the open-window timing rule, proved in [CA-I 132162–132176](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L132162-L132176).
Hence \(h_b>m\).
Its preparation leaves \(\Omega_{m+1}\) unchanged.
The narrow birth collar is never charged a second loss.
The next completed localisation removes the old pocket; it does not leave a damaged live strip.

## 5. Induction over all moves

**Theorem.** Use the printed T rule, whole-component outcomes and prepared sequence specified above.
For every finite history of these rules, the following assertions hold at every applicable read site.
No test outcome, field value, age, stage count or number of components enters the constants.

1. For \(i\ge m\), the fixed strip satisfies (3).
2. Distinct live strips are disjoint. Every current native cell meeting \(S_Y\) lies in it and has level at most \(m\).
3. Once level \(m+1\) exists, \(B_Y\subset\Omega_{m+1}^c\). Every cell at birth-distance less than \(5\check R_m/2\) has level at most \(m\).
4. For every existing \(i>m\), \(B_Y\) lies in the component of \(\Lambda_i^c\) containing \(Y\).
5. The T-site bound is \(\operatorname{dist}_i(S_Y,\Omega_{i+1}^{T})\ge7\check R_i\).
6. At P and L, an old strip in an untreated component has distance at least \(\check R_k\) from the treated region.
7. At P, the treated-strip bound is \(\operatorname{dist}_{h+1}(S_Y,R_\nu)\ge5\check R_{h+1}/2\).
   The untreated-strip bound is \(\operatorname{dist}_k(S_Y,R_\nu)\ge \check R_k\).
   No P integration bond meets a live strip.

Here an old strip at R at step \(k\) has \(m<k\).
New second-class outputs of that operation enter the next cycle.
The size assertion also uses \(i\ge m\), as in [CA-I 63567](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63567) and [N 81388–81390](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L81388-L81390).
It does not assert the displayed bound on arbitrarily finer grids.

**Proof.** Order the moves by step, then by preparation stage and component decision.
Initially there are no pockets.
At a birth, retain the old pockets until their containing component is localised.
Remove those pockets at that localisation.
Insert its new second-class pocket only if the final class decision supplies one.
This is the lifetime rule of [CA-I 63524–63545](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63524-L63545) and the whole-component rule of [CA-I 64479–64497](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64479-L64497).
Thus a new pocket never coexists with its consumed ancestors.

First prove retention of the set \(Y\), without using strip disjointness.
At birth, \(Y\subset Z_m\).
T leaves earlier entries alone and surrounds the current top component.
For any later attempt containing \(Y\), the birth factor and the exclusion rule give \(h\ge m\).
Preparation changes only levels above \(h\), so it leaves \(Z_m\) unchanged.
Another component cannot change points of \(Y\).
A completed operation on its own component ends its life.
Induction gives \(Y\subset Z_m\subset Z_i\) for every existing \(i\ge m\) while it lives.
This establishes the retention used in (8).

Next prove the birth collar.
Immediately after birth, every native cell has level at most \(m\).
There is no higher domain yet to check.
At T at \(m+1\), (4) and the strip's reach give
\[
 \operatorname{dist}_m(S_Y,\Omega_{m+1}^{T})
 \ge8L\check R_{m+1}-q_m
 \ge\frac{15\check R_m+1}{2}>\frac52\check R_m.
 \tag{12}
\]
Hence (10) lies outside \(\Omega_{m+1}\).

Suppose this collar survives up to a later move.
T does not change \(\Omega_{m+1}\).
For R, nesting gives \(B_Y\subset\Omega_{m+1}^c\subset Z_i\) at every existing \(i>m\).
The set \(B_Y\) is connected and contains \(Y\).
It therefore belongs to the same top component as \(Y\).
An operation on another component changes no part of it.
An operation on its own component has \(h\ge m\).
If \(h>m\), it leaves \(\Omega_{m+1}\) unchanged throughout preparation.
If \(h=m\), (9) protects \(B_Y\) after the first replacement.
Later replacements are nested, and an interruption freezes a prefix, including the extra raise when applicable.
Thus every incomplete branch preserves the collar.
If localisation completes, this pocket dies and the assertion ends.
This proves assertions 3 and 4 by induction.
The proof uses the determining sequence. It does not substitute the action sequence for it.

A native cell of level \(n>m\) has its interior in \(\Omega_n\subset\Omega_{m+1}\).
It cannot have an interior point in \(B_Y\).
If its closed carrier had distance less than \(5\check R_m/2\) from \(S_Y\), nearby interior points would lie in \(B_Y\).
That is impossible.
This proves the collar's cell-level assertion.
In particular, a cell meeting \(S_Y\) has level at most \(m\).
The strip is a union of \(\pi_m\)-cubes, and the grids are nested.
A finer cell whose interior meets it lies wholly in one of those cubes.
At equal levels, meeting already means having the same cube.
Thus every meeting cell lies wholly in \(S_Y\).

We can now prove mixed-birth disjointness.
Old strips do not move under T, joining or an interrupted operation.
Consider a new birth at step \(k\) on component \(C\).
An old pocket in \(C\) has been removed by localisation.
Any remaining old strip lies wholly in a different top component \(C'\), by assertion 4.
Before the operations, top components are disjoint unions of boxing cells of side \(a_k\).
Their closed carriers have distance at least \(a_k\).
The new strip extends beyond \(C\) by only \(q_k u_k\).
Hence
\[
 \operatorname{dist}_k(S_Y,S_{\rm new})
 \ge \check R_k-q_k\ge(\check R_k+1)/2>0.
 \tag{13}
\]
For two new births, your stronger same-level calculation after (3) gives distance at least one.
Healing deletes pockets; it creates no strip.
This completes the disjointness induction.
Cell saturation now makes (2) single-valued.

For the T-site bound, let the input level be \(i\).
Use your T-buffer argument at [CA-I 12187–12265](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L12187-L12265).
If \(m<i\), assertion 4 puts \(S_Y\) inside the input \(Z_i\).
Equation (4) gives distance at least \(8L\check R_{i+1}\ge8\check R_i\).
If \(m=i\), subtract the birth reach \(q_i\), as in (12).
Both cases give assertion 5.
Failure rounds and boxing add sets, so the bound survives creation and joining.

At R at level \(k\), an untreated old strip lies in its own top component \(C'\).
Every treated component is different from \(C'\).
The same boxing-grid separation gives distance at least \(\check R_k\), proving assertion 6.
It holds throughout P and at L, because those sites act inside the selected components.
If one selected component has already exited, treating it as untreated for later integrations only removes integration sites.

Finally suppose the containing component is treated.
By (8), its first prepared member has three layers beyond \(Y\).
In units of level \(h+1\), the strip's additional reach is at most
\[
 q_m L^{-(h+1-m)}\le\tfrac12 \check R_{h+1}.
\]
The radius comparison is the one used in (3).
Every collar \(R_\nu\) lies outside \(D_{h+1}\), by nesting.
Subtracting this reach from (8) gives assertion 7's treated bound.
This is the conditional argument already printed at [CA-I 63909–63915](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63909-L63915).
The induction above now supplies its retained-strip premise.
For an untreated component, \(R_\nu\) is inside the treated region, so assertion 6 gives the other bound.
The remaining bond assertion is checked next. \(\square\)

## 6. Every integration site

**Preparatory collar and rim.** At stage \(n+1\), put \(j=h+n\).
[CA-I 74309–74320](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L74309-L74320) gives the two actual coordinate sets:
\[
 (\Omega_{j+1}^c\setminus D_{j+1})^{(j)*},
 \qquad (Z_{j+1}\cap\Omega_{j+1})\cap C.
 \tag{14}
\]
Both lie in the complement of \(D_{j+1}\) inside the treated component.
The first carries \(B_j\); the second carries the rim variables \(A_j\).
Use the incident-bond convention, which is the larger convention.
[CA-I 159058–159075](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L159058-L159075) counts bonds with at least one endpoint in the coordinate set.
Removing pivots can only reduce this set.
A level-\(j\) bond has length \(u_j/M\le u_j\).

For the first stage, (8) and the strip-reach subtraction give
\[
 \operatorname{dist}(S_Y,D_{h+1}^c)
       \ge\tfrac52\check R_{h+1}u_{h+1}>u_h.
 \tag{15}
\]
For a later stage, \(j>h\), the strip lies in \(D_j\).
The prepared gap (5) gives distance at least \(u_{j+1}=Lu_j>u_j\) from either set in (14).
An incident bond of length at most \(u_j\) cannot reach the strip.
This treats every stage, including the coarse stages where the birth-unit bound alone would not control a bond length.

For a foreign strip in an untreated component, assertion 6 gives distance \(\check R_k u_k\).
Every stage has \(j<k\), so its bonds are shorter than this distance.
Its rim bonds are covered by the same estimate.
An exited sibling has no subsequent integration on its own component.
The additional variable change on the (1.55) exit uses the same separated coordinate set.
It introduces no integration bond on a strip.

**Main integration and localisation.** This is a different site.
The main box contains \(D_k\), by [CA-I 53786–53804](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53786-L53804).
For an old pocket in the treated component, \(S_Y\subset D_{h+1}\subset D_k\).
Thus the main integration can meet its strip.
Clause (h) excludes integration bonds only at P; it does not exclude this main integration.
The completed localisation consumes the old pocket, by the lifetime definition.
Its output either heals the component or assigns a new birth level to a second-class component.
An early exit has no main integration.
A late exit retains the prepared label; its first member still protects the birth collar.
The late exits and their retained coordinates are listed at [CA-I 132008–132026](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L132008-L132026).
In particular, the last two exits may include the main integration.
They must not be misreported as P integrations or as new strip births.

For a foreign pocket, the entire main box stays in another top component.
Assertion 6 and the bond-length bound again exclude contact.
This checks every integration site in the cycle of section 4 and in the induction.

## 7. Endpoints and scope

The theorem is a finite-history geometric invariant on your account's stated rules.
The constants do not depend on a pocket's age or the number of attempts.
The proof covers joining, interrupted preparations, and the next complete T/R cycle.
Its narrowest retained birth collar is (9), including the extra raise before the (1.55) exit.

Your account uses the open interval \((h,k)\), at [CA-I 45997–46000](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45997-L46000) and [CA-I 46022–46032](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L46022-L46032).
Your older outline uses the stronger closed-endpoint convention.
The passage [SA 17435–17440](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17435-L17440) describes the partial determining sequence; at [SA 17440](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17440),
“Marks wait” gives \(s<t_\flat\). [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) explicitly excludes operations in
\([k_\flat,k)\), with the lower endpoint included.
[N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684) uses this same closed-endpoint class and also excludes joining in its quiet window.
Thus the critical \(h=m\) case in §4 is allowed by I but absent from that stricter class.
The same bounds hold when that case is absent. The sets of admissible histories are not identical.

The proof supplies no contour, norm, probe, or measure claim.
It does not prove the box assertions in (f), or the box, margin, and touching assertions in (g).
It does not prove (i1), (i2), the contour hypothesis, or any following reader or summation hypothesis.
The main integration can meet an old strip. Only the P integrations are excluded by (h).
A completed localisation ends that pocket's life; a late exit retains the prepared collar.
Nothing here proves an interacting estimate or a Yang–Mills existence theorem.

## 8. Search record for the revised outline

These searches ran on all of your revised outline N at the stated commit. Source reads were bounded excerpts.
They are retrieval evidence, not proof steps. The search did not locate a proof of the
finite-history invariant elsewhere in this revision. It found uses of the invariant,
conditional consequences, and the construction ingredients used above.
This finding concerns the specified revision only.

We first read [SA 6055–6115](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L6055-L6115), 17317–17449 and 17575 onward, and [CA-I 45985–46032](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45985-L46032) and [CA-I 53765–53819](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53765-L53819). We then ran the searches below on all of N.

Commands, with `N` denoting your `YM4_1400.tex` at the stated commit:

```sh
rg -n -i 'live[- ]strips?|strip|proof outstanding|collar|101|5/2|7[[:space:]]*R' N
rg -n -i -o 'live[- ]strips?|proof outstanding' N
rg -n -F -e '101\' -e '\tfrac52' -e '\frac52' -e '\frac{5}{2}' -e '5/2' -e '7\check' -e '7 \check' -e '7R_' -e '7 R' N
rg -n -i 'birth.collar|old.strip|strip.*(disjoint|level|geometr|preserv|induct|separat)|disjoint.*strip|strip.*7|7.*strip' N
rg -n -F -e 'Y^\sharp' -e 'Y^{\sharp}' -e 'C^\sharp' -e 'C^{\sharp}' -e 'px:level-barrier' -e 'live-region-geometry' -e 'strips-geometry' -e 'strip invariant' -e 'strip geometry' -e 'birth collar' N
rg -n -i -F -e 'strip geometry' -e 'strip invariant' -e 'live-region-geometry' -e 'strips-geometry' -e 'proof outstanding' N
rg -n '7[[:space:]]*(\\[,;! ]|\\,)*[[:space:]]*(\\check|R_)|5[[:space:]]*\\check|101' N
```

| Search | Hits and disposition |
|---|---|
| `live[- ]strips?` | All hits: 81316, 81692, 85125, 85127, 85136, 85142, 85145, 85175, 85184, 85204, 85214, 127474, 127475, 127624, 127627, 127648, 129088. These concern stored terms, read counts, or filing. |
| `Proof outstanding` (case-insensitive) | No hit in N. The quoted heading belongs to I, not N. |
| `101` | All hits: 81387, 81388, 85138, 85173, 100889, 127775, 136629. The first four use side or reach bounds; 127775 uses pocket packing. The other two are a source-line comment and a bibliography DOI. |
| Literal `5/2` | All hits: 15142, 16601, 19971, 25190, 117883, 126935, 127756. Only 127756 concerns this strip geometry. |
| `\tfrac52`, `\frac52` | Relevant hits: 127519, 127536, 127542, 127762, 127768. They use collar separation in analytic counts. |
| The bound written `5\check R/2` with subscripts | 85186, 127523, 127784, 128550, 129325. These are uses of the birth or screened collar. The broader search also returns unrelated exponential factors at 127375, 127384, 127397. |
| `7 R`, `7R_`, `7\check`, `7 \check`, and the displayed spacing variant | No matching \(7\check R_i\) clause found. The search for a line containing both `7` and `strip` also finds unrelated constants and source references. |
| `strip invariant`, `live-region-geometry`, `strips-geometry`, `birth collar` | No literal hit. The hyphenated birth-scale collar is at 85185–85186. |
| `strip geometry` | 128549, in “near-strip geometry”; it invokes a corridor lower bound. |
| Broad `strip`, `collar`, and actual \(Y^\sharp,C^\sharp\) notation | Many unrelated analytic strips and local collars. The relevant candidates and their bounded reads are listed below. The broad-hit list is not a list of proved invariants. |

| Source ranges read | What the passage supplies |
|---|---|
| [N 62080–62132](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L62080-L62132) | Nested regions, small prepared gaps, three whole-component outcomes, and waiting marks. No induction of the fixed birth-strip collar or mixed-birth disjointness. |
| [N 63678–63834](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63678-L63834) | Quiet class, component restriction, surviving-component tracing, and explicit prepared boxes. These are your proved geometric ingredients for the stricter class. The formulas use no joining and the closed endpoint. |
| [N 81302–81405](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L81302-L81405), especially 81378–81393 | Uses the scaled side bound and disjoint-pocket packing to sum stored terms. |
| [N 81680–81702](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L81680-L81702) | Uses the strip count for a leaf difference; it does not supply strip persistence. |
| [N 85115–85235](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L85115-L85235), especially 85170–85188 | Uses separation, the probe ceiling, the birth collar, and native cell levels for read and depth counts. |
| [N 85288–85312](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L85288-L85312) | Starts with prescribed disjoint strips about separated components, then files terms. This is a conditional filing argument. |
| [N 97282–97310](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L97282-L97310) | Uses separation for removal and insertion root counts. |
| [N 127465–127550](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L127465-L127550) | Uses birth separation and the \(5\check R_m/2\) collar to pay kept-term counts. |
| [N 127615–127660](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L127615-L127660) | Defines a union of enlarged live-strip covers and proves a conditional persistence fact for blindly filed stored domains. It does not prove the native strip invariant. |
| [N 127675–127705](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L127675-L127705) | Uses the old-strip buffer to pay crossing length. |
| [N 127745–127810](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L127745-L127810) | Uses collar separation and disjoint strips for fine/coarse root counts; also uses screened-core geometry. |
| [N 128482–128565](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L128482-L128565) | Uses treated and untreated corridors, including the \(m=h\) collar, in analytic estimates. |
| [N 129078–129103](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L129078-L129103); 129312–129337 | Uses foreign live-strip parameters, then the birth collar and native separation for a kept-term pile. |
| [N 48083–48103](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L48083-L48103); 68854–68873 | The symbol \(Y^\sharp\) denotes an ordinary coarse collar or stored formation support here. These are different objects. |
| [N 17922–17947](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L17922-L17947); 133520–133539 | The `px:level-barrier` hit is a layered-metric crossing estimate. Its later use concerns a shrinking boundary strip, not a live second-class birth strip. |

In I, the partial proof is already explicit at 63772–63916: it starts with clauses (e)–(i) of your Lemma 4.21,
uses retained-strip containment for (e), and gives the treated-collar subtraction for (h).
This is why the new contribution is the persistence induction, especially the open-endpoint interruption.
The geometric rules and the existing conditional calculations remain yours.

[account]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex
[old-outline]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex
[new-outline]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex
