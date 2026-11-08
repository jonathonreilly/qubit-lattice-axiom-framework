# Live-region geometry: joining and the single-predecessor repair

Ethan and Levent,

Your live-region block, [CA-I 85575–85644](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85575-L85644), is headed “Proof outstanding” and states its clauses as hypotheses.
On your account's stated geometric class, the core in (g) need not be a box.
Under your outlines' single-predecessor, no-joining and closed-endpoint rule, every geometric clause (a)–(i2) follows.
Clause (a) has the domain \(i\ge m\).

The definitions, the statement of the construction rules, and the arguments cited here are yours.
The large-field method, the T rule and the preparation geometry are Tadeusz Bałaban's.
Your account identifies the T rule as his definition rewritten, [CA-I 50226–50229](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50226-L50229).
It cites CMP **119** (1988), §3, for T, and CMP **122** (1989), pp. 175–202, §1, for preparation.
Your quiet-box construction and conditional collar and vertex arguments are used below with their premises stated.
Your observation that no creation does not exclude joining is already explicit at [CA-I 118402](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L118402), [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) and [N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684).
The counterexample applies that observation to both definitions of your core.

Codex (gpt-6-astra) wrote the proofs and this note. Claude (Opus 5.5) checked each proof line by line, and its repairs are applied.
This is a proposed proof for your review. It is research text, not an audit.
No computation supplies a proof step.

**Sources.** **I** means your [complete account, Part I][account], at commit `31a47c543775`.
**SA** means your [YM4_sketch_500.tex][old-outline] at that commit.
**N** means your [YM4_1400.tex][new-outline] at commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
All source line references use these fixed revisions.

## 1. Outcomes, clause by clause

The first class is the one defined at [CA-I 45984–46032](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45984-L46032).
The second uses your rule at [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) and [N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684), also stated at [N 73101–73110](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L73101-L73110).
Its three admission conditions are written in §8.1 below.
Both conclusions retain the stated preparation, whole-component transitions, parameter floors and admissible nonwrapping charts.
“Proved” means a written implication from those rules for every finite history, at each applicable site.
It does not assert positive Wilson-field weight for an arbitrary assignment of test outcomes.

| Clause | Geometric assertion | Your account's stated class | Your outlines' rule |
|---|---|---|---|
| (a), \(i\ge m\) | \(s_i(Y)\le(101\check R_m-1)L^{-(i-m)}\le101\check R_i\) | Proved, (3) | Same proof |
| (b) | Meeting cells have level \(\le m\) and lie in the strip; strips are disjoint; cell ownership is unique | Proved, §5 | Same proof |
| (c) | Birth collar \(5\check R_m/2\), its cell ceiling and containment in the own component at every \(i>m\) | Proved, §§3–5, including \(h=m\) | Proved; \(h=m\) is excluded |
| (d) | T-site distance \(\operatorname{dist}_i(Y^\sharp,\Omega_{i+1})\ge7\check R_i\) | Proved, §5 | Same proof |
| (e) | At P and L, an untreated strip lies in its own component, at distance \(\ge\check R_k\) from the running treated region | Proved, §§5–6 | Same proof |
| (f) | \(\widetilde\Lambda_C\) is a box, sides \(\le112\), distance from \(Z^c\) at least \(9\check R_k\) | Not established here for the whole class; your conditional calculation requires a single predecessor | Proved, §8.4; sides in fact \(\le90\) |
| (g), level | \(m\le h\) | Proved, §§3, 5 | Proved with \(m<h\), §8.2 |
| (g), box | Both printed forms of \(\mathsf C_C\) give one box | False in §7: both give two separated cubes | Proved, §8.5; both forms agree |
| (g), cells and size | The core is a union of cells of levels \(\le h\), with sides \(\le104L\check R_{h+1}\) in level-\(h\) units | No general conclusion here beyond your conditional arguments; verified in §7's example | Proved, §8.5 |
| (g), strip and margin | \(Y^\sharp\subset\mathsf C_C\), with distance to its exterior \(\ge(\check R_h+1)/2\) | No general conclusion here; verified in §7's example | Proved, §8.5, with margin \(\ge\check R_h\) |
| (g), touching cubes | Every cube of level \(\le k\) touching the strip lies in \(\Lambda_C\) | No general conclusion here; verified in §7's example | Proved, §8.5 |
| (h) | P-collar distances \(5\check R_{h+1}/2\) when treated and \(\check R_k\) when untreated; no P integration bond on a strip | Proved, §§5–6 | Same proof |
| (i1) | A probe meeting a strip has level \(\le m\) | Not established here in general | Proved, §8.6, from \(\operatorname{dist}_n(Y^\sharp,\Omega_n)\ge3\) for every \(n>m\) |
| (i2) | A probe meets at most \(2^d\) live strips | Your vertex argument applies conditional on (i1); no general conclusion here | Proved, §8.7 |
| From [CA-I 85644](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85644) onward | Contour, cell and summation hypotheses | Not covered | Not covered |

Your partial proof at [CA-I 63772–63933](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63772-L63933) supplies conditional calculations for clauses (e)–(i) of your Lemma 4.21.
Its invocation of retained-strip containment is supplied by §§2–6 here.
Its core-box assertion needs the additional premise isolated in §§7–8.
In (c), a domain is tested only after its level exists.
At R at step \(k\), an old live strip has \(m<k\); a new second-class output enters the next cycle.

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

## 7. A joining allowed by your account

### 7.1. History and class tests

Use the units of §2 and write \(R_i=\check R_i\), \(a_i=R_i u_i\).
For a box \(B\), \(B^{[s]}\) means closed sup-norm enlargement by physical distance \(s\).
Write \(E_r\) for removing \(r\) boxing-cell layers.
Your defining core at [CA-I 78969](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L78969) and [CA-I 93532](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L93532) is
\[
 \mathsf C_C:=((\Omega''_{h+1})^{\sim2})^c\cap C
 =E_2(Z''_{h+1})\cap C,
\]
where \(\Omega''_{h+1}=(Z''_{h+1})^c\), [CA-I 63883–63887](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63883-L63887).
Your other form at [CA-I 63870](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63870) is \((Z'_h)^{\sim}\cap C\).
We compute both, without assuming the identity asserted at [CA-I 78969](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L78969).
The hull is a union of meeting cubes, [CA-I 50046–50054](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50046-L50054); it is not the rectangular hull of a disconnected set.
Your boxing map fills small connected components separately, [CA-I 50054–50095](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50054-L50095).

**Result.** Clause (g)'s core-box assertion fails for your account's stated geometric construction rules.
The failure occurs before localisation, while the two old second-class regions are live.
It is a counterexample to the implication from these geometric rules, not to a Yang--Mills existence theorem.

We specify the grids, the label transitions, the class test and the preparation.
The domain is finite histories of the stated geometric rules, as in §§2–6.
No claim about the nonzero weight of a particular Wilson-field branch is needed or made.
If one restricts the class further by such a support condition, that restriction must be justified separately.

Choose an odd \(L\ge103\), above any other fixed lower floors.
Choose a constant allowed radius \(R_j=R=L^p\), \(p\ge1\), over the finite window.
Take the fixed waiting depth \(N=R\), as required by [CA-I 49762–49765](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L49762-L49765), with
\[
 N_0=p+1<N=R,
 \qquad h>N+1,\qquad k=h+N.
 \tag{C7}
\]
Set \(k_0=k-N_0\). These satisfy the geometric scale conditions in [CA-I 45827–45858](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45827-L45858) and 53762--53774.
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
 \tag{C8}
\]
They are small boxing-cell boxes. Each side is \(21R\) native level-\(h\) units.
Their gap is \((20L-21)a_h>a_h\).
The whole-component second-class rule gives their flat level-\(h\) labels and marks at \(h\), [CA-I 64479–64495](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L64479-L64495).
Their fixed strips use the birth enlargement of [CA-I 63523–63544](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63523-L63544).

The size in (C8) is compatible with the preceding quiet recursion.
A centred box of side \(21a_j\) lies strictly inside the central next-grid cell, since \(21<L\).
Its next-grid hull is that cell. Eight layers and then two layers produce side \(21a_{j+1}\).
For the geometric prehistory, put \(b=h-N\).
Start with two isolated small creations at \(b\), each placed inside the corresponding central level-\((b+1)\) boxing cell.
Any box of at most 100 boxing cells per side fits strictly inside that cell, with this choice of \(L\).
Choose its grid translation accordingly. Both copies use the same translation pattern.
The first quiet step produces the centred box of side \(21a_{b+1}\).
The preceding calculation then gives the boxes (C8) after the \(N\) quiet steps.
For \(b<t\le h\), their gap is \((20L^{h+1-t}-21)a_t\ge(20L-21)a_t>a_t\).
At \(b\), even side \(100a_b\) leaves gap at least \((20L^{N+1}-100)a_b>a_b\).
Thus all these components are boxes with 1--100 cells per side, separated by at least one cell.
This checks admissible geometry fact (1), [CA-I 63547–63551](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63547-L63551), before the joining.
A creation at \(b\), the bottom of the birth waiting window, is allowed; the intervening steps have empty creation sets.
For \(b\le t<h\), one has \(t-b<N=R\), so that creation prevents eligibility by [CA-I 51178–51189](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L51178-L51189).
At \(h\), \(h-b=N=R\), so the waiting rule's requirement \(h-b\ge R\) holds.
The creation at \(b=h-R\) lies outside \((h-R,h]\), the excluded window in [CA-I 49785–49800](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L49785-L49800).
Each component is small, its preceding steps create nothing, and no earlier operation left a mark.
Thus each passes (i), (ii-a), and (ii-b) at \(h\). The whole-component second-class outcome gives (C8).
This checks the geometric birth and waiting rules. It does not infer field support from chosen test labels.

For the step \(h\to h+1\), set every new seed and growth-test set to empty.
These are the no-creation transitions of [CA-I 50196–50229](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50196-L50229) and 50342--50372.
Let
\[
 Q_0=[-a/2,a/2]^d,
 \qquad Q_{20}=20ae_1+Q_0.
\]
Since \(21a_h<a\), the actual union-of-cubes hull is
\[
 Z'_h=\widehat{Y_0\cup Y_1}=Q_0\cup Q_{20}.
 \tag{C9}
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
 \tag{C10}
\]
The boxing map fixes the second box.
It is one component, with sides \(41a,21a,\ldots,21a\), all below the cutoff \(100a\).
The two old components have joined. No creation set was used.
This is the joining mechanism already identified in [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) and [N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684).

At step \(h+2\), the box in (C10) lies strictly inside the central boxing cell of side \(La\).
Indeed its largest coordinate magnitude is \(61a/2<La/2\), since \(61<L\).
Every subsequent no-creation step therefore has
\[
 \Omega_i^c=[-17a_i/2,17a_i/2]^d,
 \qquad Z_i=[-21a_i/2,21a_i/2]^d
 \quad(h+2\le i\le k).
 \tag{C11}
\]
Induction proves (C11): the preceding box again fits inside the central next-grid cell.
All predecessors remain small. Earlier label entries stay unchanged.

For \(h<t<k\), the marks at \(h\) lie in \((t-N,t)\).
Condition (ii-b) forbids an operation on their containing component.
At step \(k\), the exclusion interval is \((h,k)\); it contains neither mark.
The component \(C=Z_k\) satisfies all three class conditions in [CA-I 45992–46000](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45992-L46000):

- **(i).** Each side of \(C\) is \(21a_k<100a_k\), or \(21R<100R\) native level-\(k\) units.
- **(ii-a), no creation.** All seed and growth-test sets in the steps \(h\to h+1,\ldots,k-1\to k\) are empty.
  The joining in (C10) therefore introduces no creation set.
- **(ii-a), earlier sizes.** Each level-\(h\) component has side \(21a_h\).
  The joined level-\((h+1)\) component has sides \(41a\) and \(21a\).
  Every later component has side \(21a_i\); the prehistory components were checked above.
  Each separate region fits its own \(100a_i\) cube. Every component also satisfies admissible geometry fact (1).
- **(ii-b).** Only the operations at \(h\) leave large-field marks. Their level lies outside \((k-N,k)=(h,k)\).
  No intervening operation is eligible, since \(t-N<h<t\) for \(h<t<k\).

[CA-I 55350–55418](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L55350-L55418) allows retained regions from an operation at \(s=h\) inside \(Z_h\cap C\).
Its reading of condition (ii) at levels \(h+1,\ldots,k\) also passes here.
Indeed, \(Z_{h+1}\cap C\) is the single \(41a\)-by-\(21a\) box, and each later \(Z_i\cap C\) is a \(21a_i\) cube.
[CA-I 118402](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L118402) states why the two level-\(h\) components need not satisfy one common size bound.
The second clause bounds each previous component. The first forbids creation but not “the joining of components”.

The class therefore treats \(C\). Each \((Y_r,h)\) remains live at its preparatory site.
The containing component has not yet passed through localisation, the death event in [CA-I 63540–63544](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63540-L63544).

### 7.2. Both cores and the prepared sequence

The old level-\(h\) entry in \(C\) is still \(Y_0\cup Y_1\).
First use the defining form at [CA-I 78969](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L78969) and 93532.
[CA-I 53783](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53783) gives \(Z''_{h+1}=(\Omega_{h+1}^{\sim5})^c\cap C\).
The two \(17a\) cubes in (C10) are separated, so removing five layers shrinks each separately to side \(7a\).
Thus \(Z''_{h+1}=N_3(Q_0)\cup N_3(Q_{20})\).
Removing two more layers gives two cubes of side \(3a\).
The other form at [CA-I 63870](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63870) adds one layer to each hull cube and gives the same set:
\[
 \begin{aligned}
 \mathsf C_C
 &=E_2\bigl(N_3(Q_0)\cup N_3(Q_{20})\bigr)\cap C\\
 &=N_1(Q_0\cup Q_{20})\\
 &=[-3a/2,3a/2]^d
 \cup\bigl([37a/2,43a/2]\times[-3a/2,3a/2]^{d-1}\bigr).
 \end{aligned}
 \tag{C12}
\]
Both boxes lie in \(C\), so intersection with \(C\) removes nothing.
They have a gap of width \(17a\) in the first direction.
In particular, \(0\) and \(20ae_1\) belong to \(\mathsf C_C\), but their midpoint \(10ae_1\) does not.
Every rectangular box containing the first two points contains their midpoint.
Thus \(\mathsf C_C\) is not a box under either form. This contradicts the box sentence of (g) at [CA-I 85629](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85629).
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
 \tag{C13}
\]
These are two \(7a\) cubes with gap \(13a\). Each contains its component of (C12), with two layers to spare.
Each also contains its old \(Y_r\), with margin \((7-21/L)a/2>a/R=u_{h+1}\).
For the remaining lower indices \(h+2\le i\le k_0\), (C11) gives
\(Z''_i=[-7a_i/2,7a_i/2]^d\).
These sets are nested, including the bottom union, since \(L\ge103\).
If this lower range is nonempty, its first gap is \((7L-47)a/2>La=a_{h+2}\).
Every later lower gap is \(7(1-1/L)a_i/2>a_i\).
Thus these gaps exceed the required native-cube sides.

At the change of scale, \(k_0+1\ge h+2\) by (C7), and \(a_{k_0+1}=u_k\).
Consequently \(\Omega_{k_0+1}^c\) is the cube of side \(17u_k\) in (C11).
At these upper levels the input is one quiet box.
Use [N 63778–63825](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63778-L63825)'s explicit completion as an instance of [CA-I 53776–53785](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53776-L53785)'s upper rules:
\[
 Z''_i=Q_*^{[3u_k-w_i]},\qquad
 Q_*=[-u_k/2,u_k/2]^d,\qquad k_0<i\le k,
 \tag{C14}
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
If \(k_0=h+1\), the preceding union reaches \(47u_k/(2L)\), by (C13).
Its gap is \((3-47/L)u_k/2>u_k\), since \(L>47\).
This checks the upper one-layer gaps as well as the lower ones.

In particular, the definitions at [CA-I 53783–53804](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53783-L53804) give the centred boxes
\[
 \operatorname{side}(Z''_k)=7u_k,\qquad
 \operatorname{side}(\Lambda_C)=9u_k,\qquad
 \operatorname{side}(\widetilde\Lambda_C)=11u_k.
 \tag{C15}
\]
Since \(Z=C\) has side \(21Ru_k\),
\[
 \operatorname{dist}_k(\widetilde\Lambda_C,Z^c)
 =\frac{21R-11}{2}\ge9R.
 \tag{C16}
\]
The last inequality is \(3R\ge11\), which follows from \(R\ge103\); also \(11\le112\).
Thus even clause (f) holds in this example. Its main box does not repair the different core in (C12).

The strips are also harmless here.
Their half-side is \(21a_h/2+q_hu_h\), with \(q_h=\lfloor(R-1)/2\rfloor\).
This is less than \(11a_h=11a/L\).
Each strip lies well inside its respective component of (C12).
Its distance to that component's exterior exceeds
\[
 \frac32a-\frac{11a}{L}>a
 =LRu_h\ge\frac{R+1}{2}u_h.
 \tag{C17}
\]
Since \(a=La_h\) and \(L\) is odd, the core boundaries lie on level-\(h\) boxing-cell faces.
For each \(Q\in\{Q_0,Q_{20}\}\), the boundary of \(N_1(Q)\) lies in \(N_1(Q)\setminus Q\).
This set lies outside \(Z_h\) and inside \(Z''_{h+1}\).
This moat is in \(\Lambda_h\cap(\Omega''_{h+1})^c\subset\Omega_h\setminus\Omega''_{h+1}\), hence in zone \(h\).
The core lies in \((\Omega''_{h+1})^c\), so its cells have level at most \(h\).
Its aligned boundaries make it a union of these cells, as in [CA-I 63879–63892](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63879-L63892).
The two strips lie in separate components of (C12), so they are disjoint.
Finally, \(Y_r^\sharp\subset Z''_{h+1}\subset Z''_k\).
Any cube of level at most \(k\) has side at most \(u_k\).
If it touches a strip, it lies in the one-layer enlargement \((Z''_k)^{(1)}=\Lambda_C\).
There is no failure of unique cell ownership or of the persistent birth collar.
Only the assertion that this core is one box has been contradicted.

### 7.3. Endpoints and the first invalid sentence

Your account's open endpoint permits the two marks at \(m=h\) in (C8).
Replacing only \((h,k)\) by \([h,k)\) excludes that particular history.
It does not remove the joining obstruction.

For the closed-endpoint variant, put both births at \(m=h-1\), with side \(21a_{h-1}\) and the same centres.
The no-creation step to \(h\) produces precisely the two boxes of side \(21a_h\) used in (C9).
For every \(m<t<k\), the mark at \(m\) belongs to the closed window \([t-N,t)\).
Indeed \(t\le k-1=m+N\), so \(t-N\le m<t\).
No intervening operation can consume it.
At \(k\), the window starts at \(h=m+1\) and excludes the old mark.
Equations (C9)--(C16) are unchanged, and the fixed old strips are smaller.
Thus (C12) remains a counterexample when only the endpoint is changed.

Your full rules at [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) and [N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684) also exclude joining throughout this window.
They exclude both examples because \(C\cap Z_h\) has two components and the step at \(h+1\) joins them.
Your quiet-box construction at [N 63749–63834](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63749-L63834) is therefore consistent with the counterexample.
It applies to a stricter class.

Your account itself adds a no-joining condition in later sections.
[CA-I 115866](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L115866) says “We assume moreover” before requiring that no components join inside \(Z\) during the window.
[CA-I 125168](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L125168) assumes this throughout its section. [CA-I 143731](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L143731) adds it as hypothesis (a).
Each is an added assumption of a later section.
None is part of Definition 4.14's class, Definition 4.22's live-region hypotheses, or the proof at [CA-I 63772–63935](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63772-L63935).
Imposing that condition would exclude the example; [CA-I 118394](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L118394) uses it to obtain one previous component.
The route remark at [CA-I 85716–85718](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85716-L85718) does mention nesting.
Here we read “nesting” at [CA-I 85717](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85717) as inclusion, consistent with \(Z_{j'+1}\subset Z_{k-1}\) at [CA-I 91947](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L91947).
Reading it as no joining would add that premise to the route remark.
The example satisfies inclusion. Inclusion does not prohibit joining.

The first invalid sentence in your account's core argument is [CA-I 63870–63871](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63870-L63871):
after defining \(\mathsf C_C=(Z'_h)^{\sim}\cap C\), it asserts that this set is rectangular.
The sentence at [CA-I 63872](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63872) is also false in this example, not merely unsupported:
\[
 \operatorname{span}_1(Z_h\cap C)
 =20a+21a_h=(20L+21)a_h>100a_h.
\]
So \(Z_h\cap C\) cannot lie in one cube of side \(100\check R_h\) in level-\(h\) units.
Condition (ii-a) bounds each previous region separately.
It does not identify their union with one region.

For comparison, separation \(6a\) does not refute both box assertions.
At that separation, \(E_2(Z''_{h+1})=[-3a/2,15a/2]\times[-3a/2,3a/2]^{d-1}\), a single box.
The other form, \(N_1(Q_0\cup Q_6)\), has two components with gap \(3a\), where \(Q_6=6ae_1+Q_0\).
Thus the equality asserted at [CA-I 78969](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L78969) can itself fail under joining.
The separation \(20a\) makes both forms equal and refutes your box claim directly.

This negative result has one witness and one scope: the core-box assertion for the printed geometric transition class.
It claims no impossibility for repaired rules, no failure of a field integral, and no audit conclusion.
The joining mechanism is your prior observation, [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575), [N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684) and [CA-I 118402](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L118402).
The construction above matches it to both forms of your core.

## 8. Full geometric proof under your outlines' rule

### 8.1. The admission rule and retained construction

At an attempted operation of level \(k\), put \(h=k-N_k\ge1\).
Let \(C\) be a component of the input \(Z_k=\Lambda_k^c\), and put \(G_i=C\cap Z_i\).
Retain your account's geometric parameter and size requirements.
Impose your outlines' admission rule, with the explicit small-box cutoff of 100:

1. For every \(h\le i\le k\), \(G_i\) is one nonempty component contained in a cube of side \(100R_i\) in native level-\(i\) units.
2. For \(h<i\le k\), there is no creation and no absorbed second component: \(G_i=\Phi_i(G_{i-1})\).
3. No operation acts on this lineage at a level in \([h,k)\). In particular, no surviving mark has a level in that interval.

The small-component boxing rule makes these small components boxes, as used at [N 63751–63760](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63751-L63760).

[SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) says “single component”, “does not absorb a second component”, and “the lower end point included”.
[N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684) repeats that rule. [N 73101–73110](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L73101-L73110) requires “single-box traces” and quarantine “including its lower endpoint”.
[SA 17440](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17440) states “Marks wait” and \(s<t_\flat\).
These quotations distinguish both restrictions: no joining, and a closed lower endpoint.

[SA 17415–17449](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17415-L17449) also fixes the transitions used here.
Healing removes the whole component. An island retains the component with a flat top label.
An interruption retains its prepared prefix and a standing mark.
The determining sequence uses the retained prefix; the action sequence keeps the formation label.
We use the determining sequence for cells and distances, as in §§2–6.
Your account's extra retained raise on the variable-change exit remains covered by that prior proof.

This admission rule restricts [CA-I 45992–46000](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45992-L46000) on the same input history.
Its first condition supplies (i) and the preceding-window size bounds in (ii-a).
Its second condition excludes exactly the creations forbidden in (ii-a), and excludes joining as well.
Its third condition excludes all the marks forbidden by (ii-b), including the additional level \(h\).
The window comparison is also stated at [CA-I 46024–46027](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L46024-L46027).
This is a restriction of eligibility on a fixed label; it does not equate the two dynamic runs.
Joining outside an admitted window remains possible.

**Geometric construction retained.**

Write \(u_i\) for the physical side of a native cube of \(\pi_i\), so \(u_{i+1}=Lu_i\).
Write \(R_i=\check R_i\), \(a_i=R_i u_i\), and \(q_i=\lfloor(R_i-1)/2\rfloor\).
The boxing grid has side \(a_i\); current cells have native sides \(u_i\).
These are different grids, [CA-I 62735–62788](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L62735-L62788) and 53737–53743.
Use the source inputs \(L\ge3\) odd, \(R_i\ge38\), and \(R_i/R_{i+1}\in\{1,L\}\).
In particular, \(R_i\le LR_{i+1}\).
Operation boxes and their stated enlargements use the admissible nonwrapping charts of [SA 17583](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17583).

The strip is the fixed birth box \(S=Y^\sharp=Y^{(q_m)}\), [CA-I 63523–63544](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63523-L63544).
It lives until its containing component passes localisation.
An interrupted preparation before localisation does not kill it.

We use the published prepared construction, not just an arbitrary nest with one-layer gaps.
[N 63749–63834](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63749-L63834) supplies its explicit quiet-box realization.
In particular, its first upper member and its terminal member are specified boxes.
[CA-I 63685–63692](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63685-L63692) and 63788–63799 state these same endpoint constructions.
The proof below retains them. No claim is made for a different upper selector specified only by nesting.

### 8.2. The previously proved clauses survive

Apply the transition induction in §§2–6 with this stronger admission rule.
Every T transition and every retained preparation prefix is still one of its transitions.
Declining an attempt forbidden by the stronger rule leaves that component unchanged and preserves the invariant.
Whole-component healing and island outcomes are unchanged.
Thus its induction supplies (a)–(e) and (h), with their original constants.
Clause (a) retains its stated domain \(i\ge m\).

More precisely, a live birth at \(m\) carries a standing mark until its consuming localisation.
An island carries a mark: [SA 17433](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17433) calls islands and drop-outs the marked components.
If its component is treated with lower index \(h\), closed-endpoint quarantine gives
\[
 m<h. \tag{J1}
\]
The prior proof gives \(Y\subset Z_i\) for \(i\ge m\), and \(S\subset Z_i\) for \(i>m\).
Consequently, at this treatment,
\[
 S\subset G_h. \tag{J2}
\]
The prior induction's exceptional case \(h=m\) is now empty.
Every later preparation on this lineage leaves \(\Omega_{m+1}\) unchanged while the pocket lives.
Foreign operations do not alter its protected collar. Localisation ends the assertion for that pocket.
Thus no new persistence proof is needed for those clauses.
The stronger estimate in every probe scale is proved in §8.6 below.

### 8.3. Your quiet boxes and their preparation

This is your construction, [N 63718–63834](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63718-L63834), in native cube units.
It supplies the single-box premise that fails on the larger class in §7.
For a box \(B\), write \(B^{[r]}\) for its closed sup-norm enlargement by physical distance \(r\).
Set \(H_i=\widehat{G_{i-1}}\), using the boxing grid of side \(a_i\).

First identify the surviving inputs.
An earlier-label point in \(G_i\) remains in one top component at each intermediate step.
A healing would remove it from that earlier label.
An island at a later level would do the same.
An interruption would leave a mark in \([h,k)\), unless a later completed operation removed the point.
Both alternatives contradict survival or quarantine.
Whole-component transitions therefore leave the entire predecessor, and its step buffer, intact.
This is the tracing argument at [N 63718–63746](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63718-L63746).

The admission rule makes \(G_h\) one small boxed component.
The hull of a box is a box: in each coordinate, take all meeting grid intervals.
Its endpoints extend by at most \(a_i\) on each face, so
\[
 G_{i-1}\subset H_i\subset G_{i-1}^{[a_i]}.
\]
No creation or joining contributes another input in this window.
The eight-layer T complement and the ten-layer large-field output are therefore
\[
 O_i:=\Omega_i^c\cap C=H_i^{[8a_i]},\qquad
 G_i=H_i^{[10a_i]},\qquad h<i\le k. \tag{J3}
\]
Boxing fixes these boxes. Induction proves (J3) on the retained input label.
These are [N 63749–63771](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63749-L63771)'s equalities, also printed at [SA 17578–17583](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17578-L17583).
Unlike your account's unrestricted class, this argument has one predecessor at every step.

Let \(k_0=k-N_0\), with
\[
 a_{k_0+1}=u_k,\qquad h+1\le k_0\le k-2. \tag{J4}
\]
This is the preparation scale choice, [CA-I 53762–53774](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53762-L53774) and [N 63773–63777](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63773-L63777).
Write \(H_*=H_{k_0+1}\), and \(D_i=Z''_i\cap C\).
The explicit preparation at [N 63778–63825](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63778-L63825) is
\[
 D_i=
 \begin{cases}
 H_i^{[3a_i]},&h<i\le k_0,\\
 H_*^{[3u_k-w_i]},&k_0<i\le k,
 \end{cases} \tag{J5}
\]
where
\[
 w_{k_0+1}=2u_k,\qquad w_k=0,\qquad
 w_i=\sum_{q=i+1}^{k}u_q\quad(k_0+2\le i<k).
\]

Here is the geometric verification of these formulas.
Eroding \(O_i=H_i^{[8a_i]}\) by five boxing layers leaves \(H_i^{[3a_i]}\).
Each face of \(O_i\) borders its complement inside \(G_i\); the latter extends two more layers.
Thus this erosion uses the actual distance to \(\Omega_i\), not a distance to an artificial boundary.
At upper levels the prescribed erosion distance is \(5u_k+w_i\), giving the second line of (J5).
Its faces lie on the native level-\(i\) grid: \(H_*\) is made of \(\pi_k\)-cubes and \(w_i\) is a multiple of \(u_i\).
The lower boxes are made of their boxing cells, hence also of native cubes.

For consecutive lower members, \(D_i\subset G_i\subset H_{i+1}\).
The next member adds three layers of side \(a_{i+1}\), which exceed the required native layer.
At the change of scale, \(D_{k_0}\subset G_{k_0}\subset H_*\), and the next member adds \(u_k\).
For upper pairs after the first one, the gap is \(w_i-w_{i+1}=u_{i+1}\).
At the first upper pair, if its second index is \(k\), the gap is \(2u_k\).
Otherwise,
\[
 w_{k_0+2}\le\sum_{r=0}^{\infty}L^{-r}u_k
 =\frac{L}{L-1}u_k\le\frac32u_k.
\]
The gap is then at least \(u_k/2\ge u_{k_0+2}\), since \(k_0+2<k\) and \(L\ge3\).
Thus (J5) realizes the grid, nesting and one-layer requirements in [CA-I 53776–53814](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53776-L53814).
No computed estimate is used.

The two endpoint boxes deserve emphasis:
\[
 D_{k_0+1}=H_*^{[u_k]},\qquad D_k=H_*^{[3u_k]}.
 \tag{J6}
\]
The first is also the one-layer formula at [CA-I 63685–63686](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63685-L63686).
The second is the five-layer erosion at [CA-I 63788–63792](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63788-L63792), using (J3).
For probe separation, only (J6), the lower formula, and nesting will be needed.
Thus the proof also covers other intermediate upper completions with these same endpoints and nesting.

### 8.4. The enlarged integration box: clause (f)

Use your calculation at [CA-I 63788–63857](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63788-L63857), now with the single-box premise supplied by (J3).
The actual boxes are
\[
 \Lambda_C=D_k^{[u_k]}=H_*^{[4u_k]},\qquad
 \widetilde\Lambda_C=\Lambda_C^{[u_k]}=H_*^{[5u_k]}.
 \tag{J7}
\]
They are unions of native level-\(k\) cubes.
The first equality is the one-layer construction at [CA-I 53786–53804](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53786-L53804).

The small-box bound at level \(k_0+1\) and (J3) give
\[
 \operatorname{side}(G_{k_0+1})
 =\operatorname{side}(H_*)+20u_k\le100u_k
\]
in each coordinate. Hence
\[
 \operatorname{side}(H_*)\le80u_k,\quad
 \operatorname{side}(D_k)\le86u_k,\quad
 \operatorname{side}(\Lambda_C)\le88u_k,\quad
 \operatorname{side}(\widetilde\Lambda_C)\le90u_k\le112u_k.
 \tag{J8}
\]
This is [N 63827–63834](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63827-L63834)'s \(88M\) integration-box bound, followed by one native layer.
Its level-\(k\) lattice unit has cube side \(M\); I's native cube unit divides these lengths by \(M\).
The stronger bound 90 therefore implies your account's requested bound 112.

Also, \(\Lambda_C\subset G_{k_0+1}\subset G_{k-1}\subset H_k\), by (J4).
Since \(C=G_k=H_k^{[10a_k]}\),
\[
 \operatorname{dist}(\Lambda_C,C^c)\ge10a_k.
\]
Let \(Z\) be the running union of treated components at this site, so \(C\subset Z\).
Enlarging \(\Lambda_C\) by \(u_k\) yields
\[
 \operatorname{dist}_k(\widetilde\Lambda_C,Z^c)
 \ge10R_k-1\ge9R_k. \tag{J9}
\]
This is the ten-layer distance argument of [CA-I 63837–63857](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63837-L63857).
It applies while the component is treated and its integration boxes are attached.
Thus all of (f) holds.

### 8.5. The core and touching cubes: clause (g)

Use your calculation at [CA-I 63861–63906](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63861-L63906). Equation (J1) strengthens its level inequality to \(m<h\).
The specified core, using the same component restriction as the preparation, is
\[
 \mathsf C_C=(Z'_h)^{\sim}\cap C
 =H_{h+1}^{[a_{h+1}]}. \tag{J10}
\]
Indeed, \(G_{h+1}=H_{h+1}^{[10a_{h+1}]}\subset C\), so intersection with \(C\) clips nothing.
Every other component \(A\) of \(Z_h\) stays in a different component of \(Z_k\), since \(C\cap Z_h=G_h\).
Its enlarged hull lies inside its ten-layer step output in \(Z_{h+1}\), so it cannot reach \(C\).
The hull and layer are boxes. This is precisely where no joining excludes the disconnected core in §7.

Now check the defining form at [CA-I 78969](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L78969) and 93532.
By [CA-I 63883](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63883), \(\Omega''_{h+1}=(Z''_{h+1})^c\).
Put \(H=H_{h+1}\) and \(a=a_{h+1}\). Equation (J5) gives \(Z''_{h+1}\cap C=D_{h+1}=H^{[3a]}\).
Since \(C\supset G_{h+1}=H^{[10a]}\), this box has distance at least \(7a\) from \(C^c\).
Thus only \(C\setminus D_{h+1}\) contributes to the complement's two-layer enlargement inside \(D_{h+1}\).
Adding two layers of \(a\)-cubes to that complement removes two layers from the grid box \(H^{[3a]}\).
Hence
\[
 (\Omega''^{\,\sim2}_{h+1})^c\cap C
 =H^{[a]}=(Z'_h)^{\sim}\cap C.
\]
Both defining forms give the same box as [CA-I 63870](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63870). The identity at [CA-I 78969](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L78969) holds under the no-joining rule.

The hull adds at most \(a_{h+1}\) at each face of \(G_h\).
The final layer adds the same amount again.
Thus each core side, in level-\(h\) units, is at most
\[
 100R_h+4LR_{h+1}\le104LR_{h+1}. \tag{J11}
\]
This is the source's size calculation, [CA-I 63872–63877](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63872-L63877).

The core lies inside \(O_{h+1}=H_{h+1}^{[8a_{h+1}]}\) before preparation.
It lies inside \(D_{h+1}=H_{h+1}^{[3a_{h+1}]}\) after that member is prepared.
It therefore stays in \(\Omega_{h+1}^c\) at every applicable P or L site before localisation.
No current cell of level above \(h\) can meet its interior.
Its faces lie on the level-\(h\) native grid, since \(a_{h+1}/u_h=LR_{h+1}\) is an integer.
A cell of level at most \(h\) cannot straddle such a face.
The core is consequently a union of whole current cells, all of levels at most \(h\).
Boundary ownership uses the fixed convention of §2; distances use closed carriers.
This supplies the cell-union conclusion of [CA-I 63879–63892](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63879-L63892) without assuming that the inner cells have one level.

By (J2), \(S\subset G_h\subset H_{h+1}\).
Consequently
\[
 S\subset\mathsf C_C,\qquad
 \operatorname{dist}_h(S,\mathsf C_C^c)
 \ge LR_{h+1}\ge R_h\ge\frac{R_h+1}{2}. \tag{J12}
\]
This is [CA-I 63898–63900](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63898-L63900)'s \(m<h\) branch.
Its separate \(m=h\) subtraction is unnecessary on the present class.

Finally, \(S\subset D_{h+1}\subset D_k\).
Let a native cube of level \(j\le k\) touch \(S\), and take a contact point \(y\).
Every point of that cube is within sup-distance \(u_j\le u_k\) of \(y\).
The entire cube lies in \(D_k^{[u_k]}=\Lambda_C\).
This is the touching-cube argument of [CA-I 63905–63906](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63905-L63906), including boundary contact.
It completes every part of (g).

### 8.6. Separation in the probe's own units: clause (i1)

The source's probe argument, [CA-I 63919–63924](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63919-L63924), needs an estimate in level-\(n\) units for every \(n>m\).
Dividing clause (c)'s birth collar by \(L^{n-m}\) does not provide it.
We supply its persistent input using the published boxes (J5)–(J6).

**Lemma.** For every finite history of these rules, every live strip \(S=Y^\sharp\), and every existing level \(n>m\),
\[
 \operatorname{dist}_n(S,\Omega_n)\ge3. \tag{J13}
\]
This holds on the determining labels, including every retained preparation prefix.
The distance to an empty domain is interpreted as infinity.

**Proof.** Induct over steps and component operations, including their intermediate stages.
At a strip's birth, no higher level has yet been formed, so there is nothing to check.
The earlier-level domains are unchanged by a T step.
It remains to check a newly formed \(\Omega_n\), and the changes made by R.

At T from level \(n-1\) to \(n\), the eight-layer rule surrounds the hull of \(Z_{n-1}\).
This is Bałaban's T rule in your eight-layer form, [CA-I 50196–50229](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50196-L50229), with two further layers at [CA-I 50342–50368](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L50342-L50368).
If \(m<n-1\), the prior invariant puts \(S\subset Z_{n-1}\), and the distance is at least \(8R_n\).
If \(m=n-1\), only \(Y\subset Z_m\) is used, and the strip reaches \(q_m u_m\) further.
Then
\[
 \operatorname{dist}_n(S,\Omega_n)
 \ge8R_n-\frac{q_m}{L}
 \ge8R_n-\frac{R_m}{2L}
 \ge\frac{15}{2}R_n\ge3. \tag{J14}
\]
Extra failures or boxing enlarge the large-field side, so cannot reduce this distance.

Now consider R at level \(k\ge n\).
First suppose it acts on a component different from the one containing the strip.
Since \(k\ge n>m\), the prior invariant puts the entire strip in its own top component.
Distinct top components have distance at least \(a_k\).
Every changed point is inside the operated component.
Its distance from the strip, in level-\(n\) units, is at least
\[
 \frac{a_k}{u_n}=R_k L^{k-n}\ge38.
\]
Unchanged points of \(\Omega_n\) retain (J13). Thus foreign operations preserve the estimate.
The same reasoning covers siblings already removed from the running class.

Suppose instead that R treats the component containing the strip.
Until localisation the strip remains live.
By (J1)–(J2), \(m<h\) and \(S\subset G_h\).
If \(n\le h\), its domain is unchanged.
For \(n>h\), a replacement changes the domain inside \(C\) to \(C\setminus D_n\).
We bound its distance directly.

For \(h<n\le k_0\),
\[
 S\subset G_h\subset G_{n-1}\subset H_n,\qquad
 D_n=H_n^{[3a_n]}.
\]
Hence \(\operatorname{dist}_n(S,D_n^c)\ge3R_n\ge3\).

For \(k_0<n<k\), use the first upper box and nesting:
\[
 S\subset G_h\subset G_{k_0}\subset H_*,\qquad
 D_n\supset D_{k_0+1}=H_*^{[u_k]}.
\]
It follows that
\[
 \operatorname{dist}_n(S,D_n^c)
 \ge\frac{u_k}{u_n}=L^{k-n}\ge L\ge3. \tag{J15}
\]
At \(n=k\), the terminal box gives
\[
 \operatorname{dist}_k(S,D_k^c)\ge3,\qquad D_k=H_*^{[3u_k]}.
 \tag{J16}
\]
Outside \(C\), the domain is unchanged and retains the inductive estimate.
Each changed member therefore satisfies (J13); each unreplaced member retains it.
Any interrupted prefix, including the extra retained raise before an omitted integral, has the same property.
A later attempt is covered afresh by the same argument, without adding any loss.
When localisation occurs, the old pocket dies and its assertion ends.
A new second-class output starts a new induction at its own birth level.
These cases exhaust the transitions. This proves (J13). \(\square\)

Equations (J15)–(J16) supply the missing all-label use of the source's upper preparation.
They also explain why the narrow gaps between adjacent upper strata are harmless here.
The distance is measured from the retained old box inside \(H_*\), not between consecutive stratum boundaries.
[CA-I 63953–63959](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63953-L63959) suggests the same lower/upper split for its related core estimate.
This induction supplies the persistent estimate needed for your probe argument.

Now apply your implication at [CA-I 63919–63924](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63919-L63924).
A probe \(Q\) of level \(n\) has an anchor cell \(\Delta_n\subset\Omega_n\) and satisfies
\[
 \Delta_n\subset Q\subset
 \{x:\operatorname{dist}_n(x,\Delta_n)\le2\},
 \qquad \operatorname{side}_n(Q)\le5.
 \tag{J17}
\]
This is the definition at [CA-I 62779–62788](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L62779-L62788).
If \(n>m\), (J13) gives \(\operatorname{dist}_n(S,\Delta_n)\ge3>2\).
No point of \(S\) belongs to \(Q\).
Therefore every probe meeting \(Y^\sharp\) has level at most \(m\), which proves (i1).

### 8.7. How many strips a probe meets: clause (i2)

This is your vertex argument, [CA-I 63926–63933](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63926-L63933).
The new input is (i1), proved above for the present histories.

Let \(Q\) have level \(n\), and let it meet a live strip born at \(m\).
By (i1), \(n\le m\).
Its side in birth units is at most \(5L^{n-m}\le5\).
Every side of the birth component, and hence of its strip, is at least \(R_m\ge38\).
This lower bound comes from the boxed birth geometry, [CA-I 63547–63562](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L63547-L63562) and 63650–63661.
It does not follow from clause (a)'s upper bound.

For completeness, consider one coordinate of an intersecting axis-parallel strip and probe in their local chart.
The strip interval is longer than the probe interval.
If it contained neither endpoint of the probe interval, intersection would force it strictly inside that interval.
That would contradict the length inequality.
Choose one contained endpoint in each coordinate.
Their product is a vertex of \(Q\) contained in the strip.
Admissible nonwrapping charts identify these vertices with the vertices of the original probe on the torus.

Distinct live strips are disjoint closed sets by the prior clause (b).
They cannot contain the same vertex of \(Q\).
Since \(Q\) has \(2^d\) vertices, it meets at most \(2^d\) live strips.
This proves (i2), including strips from different birth levels.
Only \(5<38\) is used; the source's unnecessary intermediate inequality \(5/L\le1\) is not used.

## 9. Suggested repair and scope

The smallest textual repair is to make your existing outline rule an explicit premise of this geometric block.
Insert it immediately before “Geometric hypotheses” at [CA-I 85598–85600](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85598-L85600).
Alternatively, adopt it in your class definition at [CA-I 45984–46000](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45984-L46000), retaining the existing depth and parameter requirements.
Use the rule from [SA 17575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17575) = [N 63684](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63684), with the explicit cutoff 100 from [N 63763–63764](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L63763-L63764):

> At an operation of level \(k\), put \(h=k-N_k\ge1\).
> For each admitted component \(C\), require that \(C\cap Z_i\) is one nonempty small component for every \(h\le i\le k\).
> Its size bound is \(100\check R_i\) in native level-\(i\) cube units.
> For \(h<i\le k\), require no creation and no absorbed second component:
> \(C\cap Z_i=\Phi_i(C\cap Z_{i-1})\).
> Require quarantine from operations on this lineage at levels in \([h,k)\), including the lower endpoint.
> Keep the prepared construction specified above.

Your single-box and quarantine requirements also appear at [N 73101–73110](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L73101-L73110); the mark condition is at [SA 17440](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L17440).
This is a restriction of your account's stated class, not a consequence of its present condition (ii-a).
Changing only the endpoint of (ii-b) does not suffice: §7.3 gives the same obstruction with births at \(h-1\).
Your later no-joining assumptions at [CA-I 115866](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L115866), [CA-I 125168](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L125168) and [CA-I 143731](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L143731) are consistent with this repair.
They are additional hypotheses in those sections; they do not already amend [CA-I 45984–46000](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45984-L46000) or [CA-I 85575–85644](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85575-L85644).
Your explanation at [CA-I 118402](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L118402) identifies exactly the distinction the repair makes explicit.

Under this premise, §§2–6 and §8 prove all geometric clauses (a)–(i2), with (a) restricted to \(i\ge m\).
The formulas for the core and integration boxes are unchanged.
The proof uses your published preparation, including its lower member and first and terminal upper boxes.
It does not assert the result for an arbitrary upper sequence specified only by nesting.
The constants are independent of age, attempt count and test outcomes.

Adopting this restriction in the class definition changes eligibility and therefore the dynamic histories.
This note does not verify that downstream waiting, rarity or summation arguments survive that change.
Adding it only as a hypothesis of this block makes the geometric conclusion conditional on supplying that rule wherever used.
Neither option by itself proves a Yang–Mills existence theorem.

The contour hypothesis beginning at [CA-I 85644](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85644), the cell hypothesis beginning at [CA-I 85650](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L85650),
and the later reader and summation hypotheses are not covered.
No contour, analytic norm, quantum-measure or positive-support conclusion is claimed.
The main integration can meet a live strip; clause (h) excludes only P integration bonds.
Localisation ends that strip's lifetime, as required in the proofs above.

[account]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex
[old-outline]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex
[new-outline]: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex
