lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T15:27Z

# core-gaps-check: line-by-line check of `library/core-gaps.md` (FINISH row 640)

Provenance: Claude Fable 5.2, effort medium, Mac mini worker 1, branch claude/ym4d-hard-route at 042dcfaca. One reading by a model that did not write the proof (the proof is by Claude Opus 5.5 high). Same provider, so this is not the cross-provider check of FINISH rule 2. Not an audit. Source: Sussman and Alpoge (with Claude and Codex as authors of the text), YM4_1400.tex at commit 2bc0658f91d2, fetched by URL to a private scratch folder (136,637 lines). "Y n" = line n of that file. No computation was run.

Kind of result: check of our own new text (`core-gaps.md`), which is a proof of a statement that Y prints with a citation and no proof (`prop:large-field-2-3`, display Y 62082-62087).

## Verdict

**`core-gaps.md` checked line by line by Claude Fable 5.2, first failing step none.** Theorem 6 and Corollary 7 hold as implications from the [Y] inputs that the file names. No item FAILS. Seven small repairs are given as text (R1 to R7). None changes a statement of a lemma; one (R1) fixes the order of the induction so that a [Y] input is not circular.

| item | verdict |
|---|---|
| (1) the two rules, the unit of `~`, the hat | HOLDS WITH REPAIR (R2: cite the sup-layer convention) |
| (2) Lemma 0 | HOLDS |
| (3) Lemma 1 | HOLDS |
| (4) Lemma 2, reading (R1) | HOLDS |
| (5) Lemma 3 | HOLDS WITH REPAIR (R1: order of the induction) |
| (6) Lemma 4 | HOLDS WITH REPAIR (R3: one grid; R4: second reading for the pair (0,1)). No breaking history exists. |
| (7) Lemma 5 | HOLDS (R5: reading (R3) is Y's explicit rule) |
| (8) Theorem 6 | HOLDS WITH REPAIR (R1) |
| (9) Corollary 7 | HOLDS WITH REPAIR (R6: unit wording) |
| (10) section 5, constants | HOLDS WITH REPAIR (R7: `Rcheck_i >= 1` is not one line of Y) |
| (11) eight more quotes | HOLDS, one wrong line number (in R7) |

## Repo search

- `library/open-core.md`: no row for `core-gaps`, CORE-GAPS or `prop:large-field-2-3` (grep, no hit). This item is a check, not an attack on an open lemma. FINISH rows 615, 616, 621, 631 are named in row 640 as not duplicates.
- Read: `core-gaps.md` in full; `h-geo.md` sections 1, 2 and 6; `h-geo-check.md` verdict (2) ("Lemma 2, the nest gaps: HOLDS AS WRITTEN", with one citation added in (d)); `prior/core-read.md` section 2; `geo-5.md` lines 28-84. I did not check `h-geo.md` again.
- Credit: the induction is Codex's (`geo-5.md` 3.2-3.3), ported by Claude Opus 5.5; the rules and box formulas are Sussman and Alpoge's.

## (1) The two rules, the unit, the hat: HOLDS WITH REPAIR

- Initial rule. Y 61973 reads: "A label's sequence starts at $\Omega_0=\Omega_1^\sim$, the first region enlarged by one layer of level-$1$ cells, and not at $T_\ell$". The quote of section 2.1 is exact.
- Step rule. Y 61983-61987 and Y 61990 read as quoted: $\Omega_t^c=Q_t'^{\sim2}\cup P_t'^{\sim4}\cup H_t$, $H_t=\widehat Y^{\sim8}$ ($t\ge2$), $P_0'^{\sim5}$ ($t=1$); $Z^{[0]}=\mathsf{bx}((\Omega_t^c)^{\sim2}\cup R_t'^\sim)$; $Z^{[n+1]}=\mathsf{bx}(Z^{[n]}\cup(\ldots)^\sim)$; "The set $Z_t=\Lambda_t^c$ is the final $Z^{[n]}$". Y 71099-71100 reads "The pre-operation region $Z_h$ contains $(\Omega_h^c)^{\sim2}$". Exact.
- Unit. The last sentence of Y 61973 is: "Hulls ($'$, $\widehat{\cdot}$) and layers are taken in level-$t$ cells." So the layers in $(\Omega_t^c)^{\sim2}$ and in $\widehat Y^{\sim8}$ are level-$t$ cells of side $a_t=M\check R_tL^t$ (Y 62096: cells "are $M\check R_t$-cubes of level $t$"). The unit is not smaller. Lemmas 1 and 2 have the unit they need, and no changed bound is required.
- The hat. Y 646-648: "A hull is the smallest union of cubes of the named partition containing the set." So $\widehat Y$ is the union of the level-$t$ cells that meet $Y$ in interior points, and $Y\subset\widehat Y$. The prime is the same hull for a failure set.
- One convention is used and not cited. Section 2.2 puts $A^{\sim r}=A^{[ra_t]}$, the sup-norm neighbourhood. Lemma 1 needs it: with layers added through faces only, $e^{\sim2}$ would not contain the cell at offset $(1,1,1,0)$ in four dimensions, and the bound $2a_t$ would fail. Y fixes the sup-norm reading: Y 63684 defines $B^{[r]}$ as "the box $B$ with each face pushed outward by $r$ such cells" and writes the step output on a quiet component as $\Omega_i^c\cap X=H_i^{[8]}$ (display Y 63686-63690); Y 63750-63763 writes it as $H_i^{[8a_i]}$ with "enlargement by a distance $s$ in the sup norm". The step rule gives this set as $\widehat Y^{\sim8}$ restricted to the component (Y 63694-63711). So eight layers of a box are the sup-norm enlargement by $8a_i$.

**R2 (text for section 2.2, after "a union of level-$t$ cells").** "Layers are sup-norm layers: Y 645-648 defines $Y^{\sim n}$ as the addition of $n$ layers of the named partition, and Y 63684-63690 with Y 63750-63763 identifies the eight layers of the step rule on a box $H$ with $H^{[8a_i]}$, the sup-norm enlargement."

## (2) Lemma 0: HOLDS

Each step holds. The open ball of radius $g-d(p,a)$ about $p$ lies in $A^{[g]}$ by the triangle inequality of the periodic sup distance. The ball meets $\operatorname{int}f$ because $p$ is in the closure of $\operatorname{int}f$. A point of $\operatorname{int}f$ in a closed cube $f'$ has a neighbourhood in $\operatorname{int}f$ that meets $\operatorname{int}f'$. Cubes of one grid have disjoint interiors, so $f=f'$.

No-wrap. The proof uses only that the grid tiles the torus, so that its cubes are closures of disjoint open sets. This holds when the torus side is a multiple of the cube side with at least one cube per side. Y 61911 gives far more: $\ell L^{K-j}\ge2L^{11}M\check R_j$, at least $2L^{11}$ cells of level $j$ per side. So the remark in brackets at the end of the proof is true and stronger than needed. A lift is needed only in Lemma 3, for the box formula.

## (3) Lemma 1: HOLDS

- $\mathsf{bx}$ only adds cubes: Y 61980, "replaces each component contained in a cube of $O(1)$ cells by its bounding box, and repeats this"; a bounding box contains its component. So $Z^{[0]}\supset(\Omega_t^c)^{\sim2}$.
- Later rounds only add cubes: $Z^{[n+1]}=\mathsf{bx}(Z^{[n]}\cup\ldots)\supset Z^{[n]}$. $\Omega_t$ is fixed before the rounds (Y 61973: $P_t,Q_t$ "determine $\Omega_t$"; the rounds enlarge $Z$ only, Y 62035). So $Z_t\supset(\Omega_t^c)^{\sim2}$ for the label just after step $t$.
- $e^{\sim2}=e^{[2a_t]}$ is a box of $5^4$ cells with $e$ at the centre, so it is connected under any convention and lies in $K_e$. $K_e$ is a union of level-$t$ cells. Lemma 0 with $B=K_e$, $A=e$, $g=2a_t$ gives $d(f,e)\ge2a_t$ for each cell $f\not\subset K_e$. The cells of another component are such cells.

The lemma is symmetric in use: it serves both cross cases of `geo-5.md` 3.3 (new small-field point in $X$ against an old hole outside; retained hole in $X$ against a new point in another component). `core-gaps.md` case 2a covers both, because it starts from the hole $c$ and its cell $e$.

## (4) Lemma 2 and reading (R1): HOLDS

- $\Lambda_t\subset\Omega_t$: from $Z_t\supset(\Omega_t^c)^{\sim2}\supset\Omega_t^c$.
- $t\ge2$: $Z_{t-1}=Y\subset\widehat Y$ (hull contains the set), $\widehat Y^{[8a_t]}=\widehat Y^{\sim8}\subset\Omega_t^c$, and $\Omega_t^c$ is a union of level-$t$ cells. Lemma 0 with $B=\Omega_t^c$, $A=\widehat Y$, $g=8a_t$ gives $d(f,\widehat Y)\ge8a_t$ for each level-$t$ cell $f$ of $\Omega_t$.
- $t=1$: $\Omega_0=\Omega_1^{[a_1]}$; Lemma 0 with $B=\Omega_0$, $A=\Omega_1$, $f$ a level-1 cell of $\Omega_0^c$.
- (R1). Y 61973: step $t=k+1$ acts on "a term of $\rho_k$ whose live region is $Y=\mathcal Z_k$", and $\rho_k=(\mathbf R\mathbf T)^k\rho_0$ (Y 61911), so $\mathcal Z_k$ is taken after the operation of level $k$. Y 1586: "let $\mathcal Z_k(h)$ be the live region after healing". Y 62106: an island "$X\subset Z_t$ remains"; Y 62107: a drop-out "$X$ remains in $Z_t$". Y 63695-63696 calls the step's input "its input region" for "the final region $Z_i$", and Y 63741-63742 says "the step's input restricted to $G_i$ is $G_{i-1}$" with $G_{i-1}=Z_{i-1}\cap X$. So $Y=Z_{t-1}(\mathcal S_{t-1})=\Lambda_{t-1}^c$, with all islands and drop-outs of level $t-1$. Islands and drop-outs of earlier levels $s<t-1$ lie in $Z_s$, and $Z_s\subset\widehat{Z_s}^{\sim8}\subset\Omega_{s+1}^c\subset Z_{s+1}$ at each later step, so they are in $Z_{t-1}$ too. The reading holds, and only $Z_{t-1}\subset\widehat Y$ is used.
- For a stopping vector, the top region $Z_{t-1}$ is the same set (Lemma 5 (a)); Y 62140-62142 says the same: "the recursion uses the recorded step data and the top stored region from level $s-1$. Changing the stage index leaves that region fixed."

## (5) Lemma 3: HOLDS WITH REPAIR

- Form used. `h-geo.md` Lemma 2 (a)-(d) gives $g_q$ for the holes $D_q=X\setminus A_q$, with $D_q=Z''_q(X)$ for $h<q$ and the old hole at $q=h$. `core-gaps.md` puts $D_h=G_h$, which contains the old hole $O_h$ of `h-geo.md` (d). The proof in the file does not lean on (d); it re-derives the case: $G_h\subset H_{h+1}$ (hull), $h+1\le k_0$, $D_{h+1}=H_{h+1}^{[3a_{h+1}]}\supset G_h^{[3a_{h+1}]}$. I recomputed each case of the file: $h<l<k_0$ gives $7a_l+3a_{l+1}$; $l=k_0$ gives $u_t+7a_{k_0}\ge u_{k_0+1}$; $l=k_0+1$ gives $2u_t$ if $k_0+2=t$, else $2u_t-\sum_{q=k_0+3}^tu_q>u_t\frac{L-2}{L-1}\ge u_t/L\ge u_{k_0+2}$ (as $L^2-3L+1\ge0$ for $L\ge3$ and $k_0+2\le t-1$); $k_0+2\le l<t$ gives $w_l-w_{l+1}=u_{l+1}$, also at $l=t-1$ where $w_t=0$. Y states the same separations at Y 63819-63826.
- Base identity $D_h(X)=Z'_h\cap X$. It is a definition in the file, and it matches Y: the stages run "for $j=k_\flat,\dots,k-1$" and integrate "the outer shell of $Z_{j+1}\cap X$"; "At the innermost position lies the core $C_{k_\flat}=X\cap Z_{k_\flat}$" and "the core operation ... is at no point unfolded" (Y 63835). The drop-out rule changes levels $l>t_\flat$ only (Y 62110-62111). So $Z_h\cap X$ stays $G_h$.
- Inclusion $D_l\subset Z'_l\cap X$. Y gives more: "$H_i\subset Z''_i(X)\subset O_i\subset G_i$" (Y 63813-63814) and "The boxes remain inside $O_{k_0+1}$, which itself is contained in all later $O_i$" (Y 63816-63817), where $O_i=\Omega_i^c\cap X$. This is the sentence of Y 62103 ("increasing boxes in $\Omega_l^c\cap X$"). The file proves the weaker $D_l\subset G_l$, which is what (F1) uses. Its chain for $l>k_0$ holds: $3u_t-w_l\le3u_t\le8u_t=8a_{k_0+1}$, then $G_{k_0+1}\subset H_{k_0+2}\subset G_{k_0+2}\subset\cdots$.
- Alignment. Y 63804-63809: first box a union of level-$i$ cells, second a union of $M$-cubes of level $i$ ($L$ odd). $X$ is a union of level-$t$ cells. So $X\setminus D_{l+1}$ is a union of $M$-cubes of level $l+1$, and Lemma 0 applies with $A=D_l$, $B=D_{l+1}$.
- Order of the induction (the repair). The quiet-box input [Y] is proved in Y by "Tracing an eligible component", and that proof opens with "We use the nesting of `prop:large-field-2-3` on these labels" (Y 63715-63716). Theorem 6 proves that proposition. Used as a free-standing input, the quiet boxes are circular. They are not circular inside the induction: Y's tracing for a class component of level $k$ uses nesting only on the labels $\mathcal S'_s,\mathcal S_s$ with $s<k$ and on $\mathcal S'_k$ (Y 63714-63741), and that the earlier operations only shrink $Z_i$ (Y 63717-63720, which is (F1) for earlier operations). All of these are moments before the operation of level $k$.

**R1 (text for the proof of Theorem 6, operation case, before "So $\mathcal L^{\boldsymbol\nu}(h)$ satisfies (N), (G)").** "Order: Y's proof of the quiet boxes at level $t$ (Y 63714-63766) uses the nesting (N) and the monotonicity (F1) only for the determining labels of the moves before the operation of level $t$. These are induction hypotheses here. So the quiet boxes at level $t$ are available at this step, and the induction is joint: (N), (G) for all moves up to step $t$, then the quiet boxes at level $t$, then Lemma 3, then Lemma 4."

- The case $l=k_0+1$ of row 640: checked above; `h-geo-check.md` (2) agrees. The existence of $k_0$ with $h<k_0\le t-2$ stays a [Y] input (section 7 item 2 of the file says so).

## (6) Lemma 4: HOLDS WITH REPAIR

(F1). Healed: $\Lambda_l\cup X$ for $l\le t$. Island: the same for $l<t$, and $\Lambda_t$ unchanged. Stopped: $Z_l\cap X=D_l\subset G_l=Z'_l\cap X$ in the window, $l<t$; $Z_t\cap X=X$ unchanged. So $Z_l\subset Z'_l$ for all $l\le t$. Holds.

(F2). Entries change only inside $\bigcup X_i$; each $X_i$ is a union of level-$t$ cells; a cube $f$ of a finer nested grid is inside one $X_i$ or has no interior point in any. Holds.

(N), first part: checked for each fate, including $l=t$ with $m=\mathsf N_t$ ($\Lambda_t\cap X=\emptyset\subset X\setminus D_t$).

(G), cases.

- Case 1 ($f$ old): $c\subset Z_l\subset Z'_l$, old gap. This covers the upper splice $l=t_\flat+m$, $l+1$ outside the window, where $Z_l\cap X=D_l\subset G_l$ and $\Omega_{l+1}$ is unchanged. It covers $m=0$ fully (no entry changes).
- Case 2 ($f$ new, $f\subset X$): $c\subset Z'_l\subset\Omega_t'^c$ by (N) of $\mathcal L'$ iterated ($Z'_l\subset\Omega_{l+1}'^c\subset Z'_{l+1}\subset\cdots\subset\Omega_t'^c$). The cell $e\supset c$ lies in $\Omega_t'^c\subset Z'_t$, so $K_e$ exists.
- 2a ($K_e\ne X$): Lemma 1, $2a_t\ge2u_t\ge u_{l+1}$. Holds for every fate of $X$ and of $K_e$.
- 2b ($K_e=X$): healed or island have $Z_l\cap X=\emptyset$ for $l<t$. Stopped: $f$ new forces $t_\flat<l+1\le t_\flat+m$, so $l\ge t_\flat$; then $c\subset D_l$ (for $l=t_\flat$ by the base identity), $f\subset X\setminus D_{l+1}$, and Lemma 3 gives $u_{l+1}$. The levels $l=t_\flat$ and $l+1=t$ (with $m=\mathsf N_t$, pair $(t-1,t)$: $D_{t-1}$ against $X\setminus D_t$, gap $w_{t-1}-w_t=u_t$) are both inside this case.

Healed component that swallows older marks. All entries $l\le t$ become $X$ on $X$. New cubes of $\Omega_{l+1}$ appear in $X$ at every level $l+1\le t$, also at $l+1\le t_\flat$ where an old mark's nest was. After the operation $Z_l\cap X=\emptyset$ for $l<t$, so the old nest is gone and every hole $c$ of level $l$ lies outside $X$. It lies in $\Omega_t'^c$, in a cell $e$ with $K_e\ne X$. Case 2a gives $2a_t$.

Attempt at a breaking history (two operations, one swallowed mark). Operation at level $s$: a drop-out $X_o$ after $n$ stages keeps the nest $D_l(X_o)$, $s_\flat<l\le s_\flat+n$. Steps $s+1,\dots,t$. A class component $X\supset X_o$ of level $t$ (so $s<t_\flat$). I tried the four ways to bring a new small-field cube within $u_{l+1}$ of a hole:

1. $X$ healed, hole in $X_o$: there is none after the operation (above).
2. $X$ healed, hole in another component $X'$ (a standing mark of any level, or an unmarked live component): the hole is in $\Omega_t'^c\cap X'$, two level-$t$ cells inside $X'$ in the sense of Lemma 1; distance $\ge2a_t$.
3. $X$ a drop-out after $m$ stages: levels $\le t_\flat$ in $X$ do not change, so the old nest of $X_o$ meets no new cube at its own levels ($s<t_\flat$). New cubes are at levels $l+1\in(t_\flat,t_\flat+m]$, and the holes of level $l\ge t_\flat$ in $X$ are $D_l(X)$; the old mark does not act at these levels. Case 2b.
4. Two class components $X,X'$ operated at the same level, $X'$ healed next to a hole retained in $X$: the hole is in $\Omega_t'^c\cap X$; case 2a with $K_e=X\ne X'$.

No history breaks (G). Case 2a stops ways 1, 2 and 4; case 2b with "marks wait" stops way 3. The reason is the one the lead names: every hole of a level below $t$ sits in $\Omega_t'^c$, two cells inside its component.

Pair (0,1) and (R2). With (R2) the argument is the one above with $Z_0=\Omega_0^c$. A stop never touches levels 0 and 1 ($t_\flat\ge1$). Holds.

**R3 (text for the first line of the (G) proof).** Replace "a level-$l$ unit cube $c\subset Z_l$ and a cube $f\subset\Omega_{l+1}$ of the grid of $\Omega_{l+1}$" by "an $M$-cube $c$ of level $l$ with $c\subset Z_l$ and an $M$-cube $f$ of level $l+1$ with $f\subset\Omega_{l+1}$. Every entry of level $i$ is a union of $M$-cubes of level $i$: step regions and healed or island fillings are unions of cells, and window entries are $X\setminus D_i$ (Lemma 3). So the pairs $(c,f)$ exhaust $Z_l\times\Omega_{l+1}$, and $\Omega'_{l+1}$ is a union of cubes of the grid of $f$, as (F2) needs." (The word "unit cube" could be read as a cube of side $L^l$; the argument is the same, but one grid should be named.)

**R4 (text for section 2.3, (R2)).** Add: "A second reading gives the pair $(0,1)$ as well: if $\Omega_0$ is defined at every moment as $\Omega_1^\sim$ (Y 61973 read as a standing rule), then after healing $\Omega_0=(\Omega_1\cup X)^\sim\supset\Omega_0\cup X$, and Lemma 0 gives $d(\Omega_0^c,\Omega_1)\ge a_1$ directly. Only the reading in which $\Omega_0$ is frozen at step 1 and not filled by healing breaks the pair $(0,1)$." I found no sentence of Y that decides between the readings (searched Y 61900-66000 for $\Omega_0$: Y 61973, 62078, 62245, 63032, 63039, 63374; none states the healing rule at $l=0$).

## (7) Lemma 5: HOLDS

- Definition. Y 62124-62125 gives $\Omega^{\boldsymbol\nu}_l\cap X$ as the file uses it. For $\Lambda$: Y 62121 "and likewise $\Lambda^\circ_l,S^\circ_l$"; Y 62169-62171: "For $l<s$ the same rule holds for $\Lambda_l$ with $\Lambda_l(\mathcal S'_s)$ in the second line. At $l=s$ the drop-out keeps $q$ outside $\Lambda_s$."
- (a), first claim: a mark of level $s$ never changes $\Lambda_s$; so the top $Z$ is fixed. Just after step $t$ all marks have level $<t$. Holds. Second claim: $X_o\subset Z_s\subset Z'_t$ by (N) iterated, $X_o$ connected, so $X_o\subset X$; "marks wait" (Y 62128; it is the quarantine clause of the class, Y 63684) gives $s<t_\flat$; the window $(s_\flat,s]$ is below $t_\flat$. Holds. The (N) used is for the label $h'$ that ends with step $t$, an induction hypothesis in Theorem 6.
- (b): Y 62174, "At a step, the earlier entries and standing marks are copied." Holds.
- (c): Y 62175-62180: "a healed component or an island overwrites the older entries on its region, and any mark it swallows ceases to stand. Outside the class no entries change. On a drop-out the new entries through stage $m$ are the complements of the corresponding prepared boxes, and the earlier rule supplies all entries outside its window." This is the cube-by-cube comparison of the file. Holds.
- The remark on $\Omega_s\cap X_o$ at $n=\mathsf N_s$. It is true that this entry depends on $\boldsymbol\nu$. I listed every later place that reads a level-$s$ entry in $X_o$: (i) step $s+1$ reads $Z_s$ only (Y 62140-62142); (ii) the pair $(s,s+1)$ reads $Z_s$; (iii) the pair $(s-1,s)$ is proved inside Lemma 4 for the stage count $\boldsymbol\nu(X_o)$ itself; (iv) a later class component $X\supset X_o$ of level $t$ reads entries of levels $\ge t_\flat>s$ (Lemma 3) and the top entries (Lemma 1); (v) a later healing or island overwrites the entry. No later step reads $\Omega_s\cap X_o$ as an input. Confirmed.

**R5 (text for section 2.3, (R3)).** Replace "(R3) ... follows the same rule" by: "(R3) is not a reading: Y 62169-62171 states the rule for $\Lambda_l$, $l<s$, and that at $l=s$ the drop-out stays outside $\Lambda_s$."

## (8) Theorem 6: HOLDS WITH REPAIR (R1)

- Display. Y 62082-62087: $\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM$, $\Omega_{j+1}\subset\Lambda_j^{\sim-1}$, $Z_j^\sim\cap\Omega_{j+2}=\emptyset$, "(level-$j$ units; layers of $M$-cubes of level $j$)". The file's display is the same. $LM$ level-$j$ units are $ML^{j+1}=u_{j+1}$ bare units.
- Induction. Base: Lemma 2 at $t=1$. Step: Lemma 5 (b), (a) and Lemma 2; older pairs are copied. Operation: Lemma 5 (c) and Lemma 4, whose hypotheses are (N), (G) (induction), rule (b) (top entries just after step $t$), distinct components (Y 63684: "A component $X$ of $Z_k$ belongs to the class when"), and the nests (Lemma 3, with R1 for the order). A component not yet treated during the operation is a stop with $m=0$. Holds with R1.
- First statement: (G). Second: $\Lambda_j^{\sim-1}$ is the removal of one layer (Y 645-646), that is $((Z_j)^\sim)^c$ as a union of $M$-cubes of level $j$. A level-$j$ $M$-cube $q\subset\Omega_{j+1}$ inside $Z_j^{[u_j]}$ would have $d(Z_j,q)\le u_j<u_{j+1}$. Holds. Third: $\Omega_{j+2}\subset\Omega_{j+1}$ by (N), so it follows from the second with margin $u_{j+1}-u_j>0$. Holds. (In this reading the third statement of Y adds nothing to the second and the nesting.)
- The Remark (equality at the active indices): in a prepared nest $D_j$ and $D_{j+1}$ are enlargements of one box by amounts that differ by $u_{j+1}$, and $D_{j+1}\subset O_{k_0+1}\subsetneq X$, so the distance is exactly $u_{j+1}$. Holds; matches Y 62089-62094.

## (9) Corollary 7 against `h-geo.md` section 6 item 1: HOLDS WITH REPAIR

- Sets. `h-geo.md` section 2: $A_q\cap X=\Omega_q\cap X$ for $q\le h$ ("old label"), $D_q=X\setminus A_q$, $g_q=\operatorname{dist}_\infty(D_q,X\setminus D_{q+1})$. Corollary 7 has $d(X\setminus\Omega_q,X\cap\Omega_{q+1})$ for $0\le q<h$. The same sets. The pair $q=h$ is Lemma 2 (d) of `h-geo.md`, not CORE.
- Distance. `h-geo.md` measures in the lift of $X$; the corollary gives the periodic distance, which is not larger. So the bound passes to the lift.
- Unit. CORE asks $g_q\ge LM\xi_q$, and `h-geo.md` writes $u_{q+1}=LML^q$ in bare units (its Fact 1.1), so $\xi_q=L^q$ bare. The corollary's $u_{q+1}$ is the same bare length. The words "(level-$m$ units)" in the display are wrong as written, since $u_{q+1}$ is defined in bare units in section 2.2.
- History. CORE asks "every admissible earlier history, including nests kept by older drop-outs". Theorem 6 gives every history and every stopping vector. Holds.

**R6 (text for Corollary 7).** In the display replace "$\ge u_{q+1}=LM\xi_q\ \text{(level-}m\text{ units)}$" by "$\ge u_{q+1}=LM\xi_q$, with $\xi_q=L^q$, in bare units".

## (10) Section 5, constants: HOLDS WITH REPAIR

- `geo-5.md` line 45 lists $M>\rho\ge2$, $\mu\ge\rho$, $M\ge80\mu$, $L\ge27$, $\theta\min(M,\rho)\ge64\log L$. I read `geo-5.md` 3.2-3.3 (lines 47-84): it uses only $2s_t$ and $8s_t$ against $M\xi_i$, and (3.1). I read every line of `core-gaps.md` sections 3-4: the only numerical facts used are $a_t\ge u_t$ (Lemmas 1, 2, 3), $u_{l+1}\le u_t$ for $l<t$, $(L-2)/(L-1)\ge1/L$ for $L\ge3$ (Lemma 3), $L$ odd (alignment, Y 63807), nested grids (Y 62001), and no-wrap of a class box (Y 61911, Y 63770-63771). No constant of line 45 is used. Neither $\rho$ of Y is used. Confirmed.
- $\check R_i\ge1$. Y has no line that says "$\check R_i\ge1$". Y 62001 defines $\check R_k$ as "the smallest power of $L$ that is not less than $(\log\min_{i\le k}x_i)^r$, with $r\ge2$". With $g_j=x_j^{-1/2}$ (Y 83084; table at Y 136041) and $g_j\le\gamma$ (Y 61911), $x_i\ge\gamma^{-2}\ge e$ for $\gamma\le e^{-1/2}$, so $(\log\min x_i)^r\ge1$ and $\check R_k\ge1$. Also $\mathsf N_t=\check R_t$ is a number of stages (Y 62195, Y 63882) and $k_\flat=k-\mathsf N_k$ (Y 63684). The file's line reference for "$\mathsf N_t=\check R_t$" is wrong: Y 62001 does not contain it; Y 62195 does ("since $\mathsf N_t=\check R_t$ is non-increasing").

**R7 (text for section 2.1, last paragraph, and section 5 table).** Replace '"$\mathsf N_t=\check R_t$", "Because it is a power of $L$, all partitions are nested" (Y 62001)' by '"$\mathsf N_t=\check R_t$" (Y 62195, Y 63882); "Because it is a power of $L$, all partitions are nested" (Y 62001)'. In the table row for $a_t\ge u_t$ add: "$\check R_t\ge1$ is not one line of Y; it follows from Y 62001 and $x_i=g_i^{-2}\ge\gamma^{-2}\ge e$ (Y 61911, Y 83084)."

## (11) Eight more quoted passages: HOLDS

Compared word by word with Y:

1. Y 61980, the boxing map: exact.
2. Y 62174, "At a step, the earlier entries and standing marks are copied.": exact.
3. Y 62128, "Marks wait: a mark of level $s$ lying inside a class component of level $t$ satisfies $s<t_\flat$. Hence standing marks that share a part are nested, their windows $(s_\flat,s]$ are disjoint": exact.
4. Y 63684, "$k_\flat=k-\mathsf N_k\ge1$": exact.
5. Y 62001, "Because it is a power of $L$, all partitions are nested": exact. ("$\mathsf N_t=\check R_t$" is not on this line; see R7.)
6. Y 1586, "let $\mathcal Z_k(h)$ be the live region after healing": exact.
7. Y 62121 "likewise $\Lambda^\circ_l$" and Y 62169 "For $l<s$ the same rule holds for $\Lambda_l$": exact.
8. Y 63760-63766 (quiet boxes), Y 63776-63779 ($k_0$, "$h<k_0\le k-2$"), Y 63783-63784 ($w$), Y 63798-63803 (prepared boxes), Y 63804-63809 (alignment, $L$ odd at Y 63807), Y 63770-63771 ("at most $100$"): the formulas in Lemma 3 are these, with $k$ written $t$.
9. Y 62089-62094 (equality at the active indices; $w_j-w_{j+1}$ at $j=k_0+1$): as the Remark says.
10. Y 638-639, Y 650-652, Y 14938-14942, Y 49962 (the two $\rho$): as section 5 says.
11. Y 63714 ($\mathcal S'_s$, $\mathcal S_s$), Y 62105-62115 (fates), Y 62124-62125 (stopping vectors), Y 61911 (torus floor): as quoted.

## What this check does not show

- It is one reading by one model of the same provider as the author. FINISH rule 2 asks for another provider before the node counts as closed.
- The [Y] inputs stay inputs: the quiet boxes (Y 63714-63766; non-circular only in the order of R1), the prepared-box formula and the existence of $k_0$ with $h<k_0\le t-2$ (Y 63774-63809; `geoh.md` 186-190), "marks wait" (Y 62128). I read Y's reasons for each and found no failure, but I did not rebuild them.
- (R2), the rule for $\Omega_0$ under healing, stays a reading; it matters only for the pair $(0,1)$, which Corollary 7 uses at $q=0$ and Y's display does not.
- Out of scope, as in section 7 item 4 of the file: the gaps $cM\check R_j$ at step regions, the cell-union sentence, the identity of Y 62131.

RESULT: `library/core-gaps.md` checked line by line by Claude Fable 5.2 (medium), first failing step none: items (2), (3), (4), (7), (11) HOLD; items (1), (5), (6), (8), (9), (10) HOLD WITH REPAIR (R1 joint order of the induction so the quiet-box input of Y 63715-63716 is not circular; R2 cite the sup-norm layer convention; R3 name one grid in Lemma 4; R4 second reading for the pair (0,1); R5 (R3) is Y 62169-62171; R6 unit wording in Corollary 7; R7 `Rcheck >= 1` derived from Y 62001 and `g <= gamma`, and the line of `N_t = Rcheck_t` is Y 62195). Y's layers are level-t cells and the hat is the level-t hull, so no bound changes; no history with two operations and a swallowed mark breaks (G) (case 2a, or case 2b with "marks wait"). Open: a cross-provider check; the [Y] inputs (quiet boxes, prepared boxes with `k_0`, marks wait) are not rebuilt; reading (R2) for the pair (0,1) only.
