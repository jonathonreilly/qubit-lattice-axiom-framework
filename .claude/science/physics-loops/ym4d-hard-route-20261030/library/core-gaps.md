lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T14:19Z

# core-gaps: port of the gap induction to Y's rules (FINISH row 621, registry CORE-GAPS)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, branch claude/ym4d-hard-route at 6f0a69b63. Not an audit. Source: Sussman and Alpoge (with Claude and Codex as authors of the text), YM4_1400.tex at commit 2bc0658f91d2, fetched to a private scratch folder (136,637 lines). "Y n" = line n of that file. Credit: the induction ported here is `library/geo-5.md` sections 3.1-3.3; the rule map is `library/prior/core-read.md`.

Repairs R1-R7 of `library/core-gaps-check.md` (Claude Fable 5.2) applied 2026-11-10 by Claude Opus 5.5 medium (FINISH row 641; log `library/core-gaps-apply.md`).


## 0. Result

Stop condition (i): **a complete proof**, from Y's own stated rules. Y does give the two rules that `library/prior/core-read.md` could not find in the ranges it read. Both are at Y 61973-61986, just before the range read there:

- (e) initial rule: "A label's sequence starts at $\Omega_0=\Omega_1^\sim$, the first region enlarged by one layer of level-$1$ cells" (Y 61973).
- (b) step rule: "$\Omega_t^c=Q_t'^{\sim2}\cup P_t'^{\sim4}\cup H_t$, $H_t=\widehat Y^{\sim8}$ ($t\ge2$), $P_0'^{\sim5}$ ($t=1$); $Z^{[0]}=\mathsf{bx}((\Omega_t^c)^{\sim2}\cup R_t'^{\sim})$, $Z^{[n+1]}=\mathsf{bx}(Z^{[n]}\cup(\text{cells of the failures of round }n)^\sim)$ ... The set $Z_t=\Lambda_t^c$ is the final $Z^{[n]}$" (Y 61983-61990). Y restates the consequence at Y 71100: "$Z_h$ contains $(\Omega_h^c)^{\sim2}$".

With these, the induction of `library/geo-5.md` sections 3.2-3.3 transfers to Y's rules. Theorem 6 below proves Y's display (gap, both inclusions) for every history, at every moment (after a step, after any number of stages of each component in an operation, after an operation) and for every stopping vector on the standing drop-outs. None of the constants `M > rho >= 2`, `mu >= rho`, `M >= 80 mu`, `L >= 27`, `theta min(M,rho) >= 64 log L` of `geo-5.md` line 45 is used. The proof uses only `L >= 3` (Y has `L >= 13`), `L` odd and `Rcheck_i` a power of `L` with `Rcheck_i >= 1` (both Y's), and the torus floor of Y 61911, through Y's box formula only. Corollary 7 gives hypothesis CORE of `library/h-geo.md` section 6 item 1.

Inputs taken from Y and not re-derived here (each is Y's stated formula or definition; marked **[Y]** where used): the class definition (Y 63684-63693); the quiet boxes (Y `eq:elab-history-quiet-boxes`, Y 63760-63766) and prepared boxes (Y `eq:elab-history-prepared-boxes`, Y 63798-63803), with Y's index `k_0`, `h<k_0<=k-2` (Y 63776-63779); the three fates (Y 62103-62115); the stopping-vector definition (Y 62121-62128); "marks wait" (Y 62128). Lemma 2 of `library/h-geo.md` already checked the box arithmetic from Y's formula (`library/h-geo-check.md` item (2): holds). Three readings of Y's wording are stated as such in section 2.3; none is a missing rule.

## 1. Repo search

- `library/open-core.md`: no row for this statement. FINISH rows 614-616 and 621-627: row 614 (`h-geo`) uses CORE as a hypothesis; row 615 checks it; row 616 is the reading `library/prior/core-read.md`. None attacks CORE. Registry row CORE-GAPS (`library/open-registry.md` line 1003) names this item.
- `library/geo-5.md` sections 3.1-3.3 (Codex, for the outline `YM4_sketch_500.tex`): the induction ported here. Credit: its crux, "no proof step subtracts a margin per event: every newly exposed pair receives the current box gap or current step padding", is the crux below.
- `library/h-geo.md` Lemma 2 (Claude Fable 5.2) with `library/h-geo-check.md` (Claude Opus 5.5): the local box gaps from Y's box formula. Used for Lemma 3.
- `library/prior/core-read.md` (gpt-6-luna): the rule map. Its two "NOT STATED" rows are corrected in section 2.1.
- Source: Sussman and Alpoge, with Claude and Codex as authors of their text, `YM4_1400.tex` at `2bc0658f91d2`. All rules below are theirs.

## 2. Step 1: Y's rules, quoted, and the map

### 2.1 The six rules of `geo-5.md` 3.2-3.3 in Y

| `geo-5.md` rule | Y | verdict |
|---|---|---|
| (b) after step t the live set contains the two-cell enlargement of $\Omega_t^c$ | $Z^{[0]}=\mathsf{bx}((\Omega_t^c)^{\sim2}\cup R_t'^\sim)$, $Z^{[n+1]}\supset Z^{[n]}$, $Z_t$ the final $Z^{[n]}$ (Y 61986-61990); $\mathsf{bx}$ "replaces each component contained in a cube of $O(1)$ cells by its bounding box" (Y 61980), so $\mathsf{bx}(A)\supset A$. Hence $Z_t\supset(\Omega_t^c)^{\sim2}$; Y says so at Y 71100. | **same, found** (corrects core-read row 1) |
| quiet component $\Omega^c\cap Q=H^{[8]}$, $Q=H^{[10]}$ | Y 63760-63766 | same (core-read) |
| new step: hull plus eight level-t layers in $\Omega_t^c$ | $H_t=\widehat Y^{\sim8}\subset\Omega_t^c$, $t\ge2$, $Y=\mathcal Z_{t-1}$ the live region; "Hulls and layers are taken in level-$t$ cells" (Y 61973, 61983-61984) | same, explicit |
| (e) $\Omega_0=\Omega_1$ plus one level-1 cell layer | "A label's sequence starts at $\Omega_0=\Omega_1^\sim$, the first region enlarged by one layer of level-1 cells, and not at $T_\ell$" (Y 61973) | **same, found** (corrects core-read row 4) |
| three fates | Y 62103-62115 | same (core-read) |
| every stopping choice | Y 62121-62128, and the reindexed-cell formula Y 62136-62190 | same (core-read) |

Also used: "At a step, the earlier entries and standing marks are copied" (Y 62174); "Marks wait: a mark of level $s$ lying inside a class component of level $t$ satisfies $s<t_\flat$. Hence standing marks that share a part are nested, their windows $(s_\flat,s]$ are disjoint" (Y 62128); "$k_\flat=k-\mathsf N_k\ge1$" (Y 63684); "$\mathsf N_t=\check R_t$" (Y 62195, Y 63882); "Because it is a power of $L$, all partitions are nested" (Y 62001).

### 2.2 Notation (Y's symbols)

Bare units. $u_i=ML^i$ (side of an $M$-cube of level $i$), $a_i=M\check R_iL^i$ (side of a level-$i$ cell), so $a_i\ge u_i$ and $u_{i+1}=Lu_i$. "$LM$ in level-$j$ units" is $u_{j+1}$. A label at top level $s$ is $(\Omega_l)_{0\le l\le s}$, $(\Lambda_l)_{1\le l\le s}$; $Z_l:=\Lambda_l^c$. For uniformity put $\Lambda_0:=\Omega_0$, $Z_0:=\Omega_0^c$. Regions are unions of closed cubes of the nested grids; a complement means the union of the grid cubes not in the region. $d$ is the periodic sup distance between point sets. For a set $A$, $A^{[g]}=\{x:d(x,A)\le g\}$; for a union $A$ of level-$t$ cells, $A^{\sim r}=A^{[ra_t]}$, a union of level-$t$ cells. Layers are sup-norm layers: Y 645-648 defines $Y^{\sim n}$ as the addition of $n$ layers of the named partition, and Y 63684-63690 with Y 63750-63763 identifies the eight layers of the step rule on a box $H$ with $H^{[8a_i]}$, the sup-norm enlargement. A history is the alternating sequence step 1, operation 1, step 2, operation 2, ... with its recorded outcomes. $\mathcal S'_t$, $\mathcal S_t$ are the labels just before and after the operation of level $t$ (Y 63714).

Y uses the letter $h$ twice: for a history (Lemma 5, Theorem 6) and for the depth $h=t_\flat$ (Lemma 3, Corollary 7). The context fixes which one is meant.

Site conventions: a site or bond set lies in its closed carrier, so a lower bound on carrier distance is a lower bound on site distance. Nothing is lost by working with carriers.

### 2.3 Two readings and one rule of Y (not missing rules)

- (R1) The live region $Y=\mathcal Z_{t-1}$ of step $t$ is $Z_{t-1}(\mathcal S_{t-1})$: "let $\mathcal Z_k(h)$ be the live region after healing" (Y 1586); islands and drop-outs stay in $Z_t$ (Y 62106-62107). Only $Z_{t-1}\subset\widehat Y$ is used.
- (R2) The fate rules "for $l\le t$" (Y 62105-62106) include the entry $l=0$, since "a label's sequence starts at $\Omega_0$". Used only for the pair $(0,1)$; the display of Y concerns $j\ge1$ and does not need it. (If healing did not fill $\Omega_0$, the pair $(0,1)$ would have gap $0$ inside a healed component that meets $\Omega_0^c$.) A second reading gives the pair $(0,1)$ as well: if $\Omega_0$ is defined at every moment as $\Omega_1^\sim$ (Y 61973 read as a standing rule), then after healing $\Omega_0=(\Omega_1\cup X)^\sim\supset\Omega_0\cup X$, and Lemma 0 gives $d(\Omega_0^c,\Omega_1)\ge a_1$ directly. Only the reading in which $\Omega_0$ is frozen at step 1 and not filled by healing breaks the pair $(0,1)$.
- (R3) is not a reading: Y 62169-62171 states the rule for $\Lambda_l$, $l<s$, and that at $l=s$ the drop-out stays outside $\Lambda_s$. (So for the stopping vectors $\Lambda^{\boldsymbol\nu}_l$, $l<s$, follows the same rule as $\Omega^{\boldsymbol\nu}_l$; Y also says "likewise $\Lambda^\circ_l$", Y 62121.)

## 3. Lemmas

**Lemma 0 (grid separation).** Let $\mathcal G$ be one of the nested grids of closed cubes, $B$ a union of $\mathcal G$-cubes, $f$ a $\mathcal G$-cube not contained in $B$, $A$ a set and $g>0$ with $A^{[g]}\subset B$. Then $d(f,A)\ge g$.

*Proof.* Suppose $p\in f$, $a\in A$, $d(p,a)<g$. The open sup-ball of radius $g-d(p,a)$ about $p$ lies in $A^{[g]}\subset B$. It meets the interior of $f$, since $f$ is the closure of its interior. So $\operatorname{int}f$ meets some $\mathcal G$-cube $f'\subset B$; then $\operatorname{int}f$ meets $\operatorname{int}f'$, and distinct cubes of one grid have disjoint interiors, so $f=f'\subset B$. Contradiction. (Cubes are small against the torus, Y 61911, so interiors and balls are those of a lift.) $\square$

**Lemma 1 (padding; `geo-5.md` (3.2)-(3.3) for Y).** Let $\mathcal S'_t$ be the label just after step $t$, $e$ a level-$t$ cell with $e\subset\Omega_t^c$, and $K_e$ the component of $Z_t$ that contains $e$. Every level-$t$ cell $f$ not in $K_e$ has $d(f,e)\ge2a_t$. In particular, if $X\ne K_e$ is another component of $Z_t$, then $d(e,X)\ge2a_t$.

*Proof.* By rule (b) (section 2.1), $e^{[2a_t]}=e^{\sim2}\subset(\Omega_t^c)^{\sim2}\subset Z_t$. It is a box of level-$t$ cells containing $e$, hence face-connected, hence inside $K_e$ under any connectivity convention for components. Apply Lemma 0 with $\mathcal G$ the level-$t$ cells, $B=K_e$, $A=e$, $g=2a_t$. Distinct components share no cell, so every cell of $X$ is such an $f$. $\square$

**Lemma 2 (step).** Let $t\ge1$ and let $\mathcal L$ be the label after the operation of level $t-1$ (empty for $t=1$). The label $\mathcal L'$ after step $t$ copies the entries $l\le t-1$ (Y 62174) and has new $\Omega_t,\Lambda_t$ (and $\Omega_0$ when $t=1$). Then $\Lambda_t\subset\Omega_t$, and
- for $t\ge2$: $d(Z_{t-1},\Omega_t)\ge8a_t\ge u_t$;
- for $t=1$: $d(\Omega_0^c,\Omega_1)\ge a_1\ge u_1$.

*Proof.* $Z_t\supset(\Omega_t^c)^{\sim2}\supset\Omega_t^c$ gives $\Lambda_t\subset\Omega_t$. For $t\ge2$, by (R1) $Z_{t-1}=Y\subset\widehat Y$, and $\widehat Y^{\sim8}=\widehat Y^{[8a_t]}\subset\Omega_t^c$ (Y 61983-61984). Each level-$t$ cell $f$ of $\Omega_t$ is not in $\Omega_t^c$, so Lemma 0 ($B=\Omega_t^c$, $A=\widehat Y$, $g=8a_t$) gives $d(f,Z_{t-1})\ge8a_t$. For $t=1$, $\Omega_0=\Omega_1^{[a_1]}$ by rule (e); Lemma 0 with $B=\Omega_0$, $A=\Omega_1$ and $f$ a level-1 cell of $\Omega_0^c$. Finally $a_t\ge u_t$ as $\check R_t\ge1$. $\square$

**Lemma 3 (local box gaps; `geo-5.md` (3.1) for Y).** Let $X$ be a class component of level $t$, $h=t_\flat=t-\mathsf N_t\ge1$, all regions in $\mathcal S'_t$, $G_i=Z_i\cap X$, $H_i$ the level-$i$ hull of $G_{i-1}$, and **[Y]** the quiet and prepared boxes $G_i=H_i^{[10a_i]}$ ($h<i\le t$), $G_t=X$, $D_i:=Z''_i(X)=H_i^{[3a_i]}$ ($h<i\le k_0$), $D_i=H_{k_0+1}^{[3u_t-w_i]}$ ($k_0<i\le t$), $h<k_0\le t-2$, $a_{k_0+1}=u_t$, $w$ as in Y 63783-63784. Put $D_h:=G_h$. Then for $h\le l<t$:
$$D_l\subset D_{l+1},\qquad D_l\subset G_l,\qquad D_l^{[g_l]}\subset D_{l+1}\ \text{with}\ g_l\ge u_{l+1}\ \text{(in the lift of }X\text{)},$$
and hence, by Lemma 0 with $\mathcal G$ the $M$-cubes of level $l+1$, $d(D_l,X\setminus D_{l+1})\ge u_{l+1}$.

*Proof.* `library/h-geo.md` Lemma 2 (a)-(d), checked in `library/h-geo-check.md`; restated with $D_h=G_h$. (l=h) $G_h\subset H_{h+1}$ by definition of the hull, and $h+1\le k_0$, so $D_{h+1}=H_{h+1}^{[3a_{h+1}]}\supset G_h^{[3a_{h+1}]}$: $g_h\ge3a_{h+1}$. ($h<l<k_0$) $D_l=H_l^{[3a_l]}\subset H_l^{[10a_l]}=G_l\subset H_{l+1}$, so $g_l\ge7a_l+3a_{l+1}$. ($l=k_0$) $D_{k_0}\subset G_{k_0}\subset H_{k_0+1}$ and $D_{k_0+1}=H_{k_0+1}^{[u_t]}$, so $g_{k_0}\ge u_t\ge u_{k_0+1}$. ($l=k_0+1$) if $k_0+2=t$, $g=3u_t-u_t=2u_t$; else $g=2u_t-\sum_{q=k_0+3}^tu_q\ge u_t(2-\tfrac L{L-1})=u_t\tfrac{L-2}{L-1}\ge u_t/L\ge u_{k_0+2}$ for $L\ge3$. ($k_0+2\le l<t$) $g_l=w_l-w_{l+1}=u_{l+1}$, Y's equality at the active indices. In all cases $a_{l+1}\ge u_{l+1}$. Inclusion $D_l\subset G_l$: for $l\le k_0$, $3a_l\le10a_l$; for $l>k_0$, $D_l\subset H_{k_0+1}^{[8u_t]}=H_{k_0+1}^{[8a_{k_0+1}]}\subset G_{k_0+1}\subset H_{k_0+2}\subset G_{k_0+2}\subset\cdots\subset G_l$. Each $D_{l+1}$ is a union of $M$-cubes of level $l+1$ (Y 63804-63809, using $L$ odd), and $X$ is a union of level-$t$ cells, so $X\setminus D_{l+1}$ is a union of $M$-cubes of level $l+1$. The lift inclusion projects to the torus, where Lemma 0 applies. $\square$

**Invariant.** For a label at top level $s$ write

- (N) $\Omega_{l+1}\subset\Lambda_l\subset\Omega_l$ for $0\le l<s$, and $\Lambda_s\subset\Omega_s$;
- (G) $d(Z_l,\Omega_{l+1})\ge u_{l+1}$ for $0\le l<s$ (for $l=0$: $d(\Omega_0^c,\Omega_1)\ge u_1$).

Given $\Lambda_l\subset\Omega_l$, the inclusion $\Omega_{l+1}\subset\Lambda_l$ follows from (G): a cube of $\Omega_{l+1}$ not in $\Lambda_l$ would contain a level-$l$ cube of $Z_l$, at distance $0$. Iterating (N) gives $Z_l\subset\Omega_t^c$ for $l<t\le s$.

**Lemma 4 (operation, all fates, all stage counts).** Let $\mathcal L'$ be a label at top level $t$, just after step $t$, satisfying (N), (G) and rule (b). Let $X_1,\dots,X_r$ be distinct components of $Z'_t$, each with a nest $D_\cdot(X)$ satisfying the conclusions of Lemma 3 (with $D_h(X)=Z'_h\cap X$), and each given one outcome: healed, island, or *stopped after $m(X)$ stages*, $0\le m(X)\le\mathsf N_t$. Let $\mathcal L$ be given by Y's rules (Y 62105-62115): nothing changes outside $\bigcup X$; healed: $\Omega_l\cap X=\Lambda_l\cap X=X$ for $l\le t$; island: the same for $l<t$ and for $\Omega_t$, with $\Lambda_t\cap X=\Lambda'_t\cap X=\emptyset$; stopped: $\Omega_l\cap X=\Lambda_l\cap X=X\setminus D_l$ for $t_\flat<l\le t_\flat+m$ ($l<t$ for $\Lambda$), all other entries unchanged, so $\Lambda_t\cap X=\emptyset$. Then $\mathcal L$ satisfies (N) and (G).

"Stopped after $m$" is a drop-out with $n=m$, the stage sequence after $m$ stages, and for $m=\mathsf N_t$ the prepared sequence (Y 62080, 62107-62115, 62128).

*Proof.* Two facts. (F1) $Z_l\subset Z'_l$ for every $l\le t$: healed and island empty $Z_l\cap X$ for $l<t$ (and healing also at $l=t$); a stop replaces $Z'_l\cap X=G_l$ by $D_l\subset G_l$ (Lemma 3); $\Lambda_t\cap X$ stays empty. (F2) A cube of $\Omega_{l+1}$ not in $\Omega'_{l+1}$ lies in some $X_i$.

*(N), part $\Lambda_l\subset\Omega_l$:* in each $X$, healed gives $X\subset X$; island gives $X\subset X$ for $l<t$ and $\Lambda_t\cap X=\emptyset$; stopped gives equal entries in the window, $\Lambda_t\cap X=\emptyset$, and old entries elsewhere. The other part of (N) follows from (G).

*(G).* Fix $0\le l<t$, an $M$-cube $c$ of level $l$ with $c\subset Z_l$ and an $M$-cube $f$ of level $l+1$ with $f\subset\Omega_{l+1}$. Every entry of level $i$ is a union of $M$-cubes of level $i$: step regions and healed or island fillings are unions of cells, and window entries are $X\setminus D_i$ (Lemma 3). So the pairs $(c,f)$ exhaust $Z_l\times\Omega_{l+1}$, and $\Omega'_{l+1}$ is a union of cubes of the grid of $f$, as (F2) needs. We show $d(c,f)\ge u_{l+1}$.

1. $f\subset\Omega'_{l+1}$. By (F1) $c\subset Z'_l$, and (G) for $\mathcal L'$ gives the bound.
2. $f\not\subset\Omega'_{l+1}$, so $f\subset X$ for one $X=X_i$ (F2). By (F1) and (N) for $\mathcal L'$, $c\subset Z'_l\subset\Omega_t'^c$. By nesting of the grids, $c$ lies in one level-$t$ cell $e$, and $e\subset\Omega_t'^c$ because $\Omega_t'^c$ is a union of level-$t$ cells and meets the interior of $e$.
   - 2a. $K_e\ne X$. Lemma 1: $d(e,X)\ge2a_t\ge2u_t\ge u_{l+1}$, as $l+1\le t$.
   - 2b. $K_e=X$, so $c\subset Z_l\cap X$. Healed or island: $Z_l\cap X=\emptyset$ for $l<t$, impossible. Stopped after $m$: $f$ is new at level $l+1$, so $t_\flat<l+1\le t_\flat+m$ and $f\subset X\setminus D_{l+1}$; and $l\ge t_\flat$, so $Z_l\cap X=D_l$ (window, $l<t$) or $Z'_{t_\flat}\cap X=D_{t_\flat}$ ($l=t_\flat$). Lemma 3: $d(c,f)\ge u_{l+1}$.

For $l=0$, put $Z_0=\Omega_0^c$, $\Lambda_0=\Omega_0$: by (R2) healed and island fill $\Omega_0$, and a stop never touches levels $0,1$ since $t_\flat\ge1$; the same cases apply. No case subtracts a margin: each new pair gets either Lemma 1's padding $2a_t$ or Lemma 3's box gap. $\square$

**Lemma 5 (stopping vectors).** Let $h$ be a history and $\boldsymbol\nu$ a stopping vector, $0\le\boldsymbol\nu(X)\le n(X)$, on the drop-outs standing in $h$, with $\mathcal L^{\boldsymbol\nu}(h)$ the label of Y 62121-62128 and (R3); $\mathcal L(h)=\mathcal L^{n}(h)$ is the determining label. Then:

- (a) the top region $Z_s$ of $\mathcal L^{\boldsymbol\nu}(h)$ does not depend on $\boldsymbol\nu$, and just after a step $t$ neither do $\Omega_t,\Lambda_t$; and inside a class component $X$ of level $t$, the entries of $\mathcal L^{\boldsymbol\nu}(\mathcal S'_t)$ at levels $\ge t_\flat$ do not depend on $\boldsymbol\nu$;
- (b) if $h=(h',\text{step }t)$, then $\mathcal L^{\boldsymbol\nu}(h)$ is $\mathcal L^{\boldsymbol\nu}(h')$ followed by step $t$ with the recorded new entries $\Omega_t,\Lambda_t$ of $h$;
- (c) if $h=(h',\text{operation }t)$, then $\mathcal L^{\boldsymbol\nu}(h)$ is obtained from $\mathcal L^{\boldsymbol\nu'}(h')$ by Lemma 4's rules with the same components, fates and nests, and stage count $\boldsymbol\nu(X)$ on each new drop-out $X$. Here $\boldsymbol\nu'$ is any extension of $\boldsymbol\nu$ to the marks of $h'$.

*Proof.* A standing drop-out $X_o$ of level $s$ changes entries only at cubes of $X_o$ and levels in $(s_\flat,s]$, and its $\Lambda_s\cap X_o=\emptyset$ for every $\boldsymbol\nu$. (a) First claim: a mark of level $s$ changes $\Lambda$ only at levels $<s$, and has $\Lambda_s\cap X_o=\emptyset$ for every $\boldsymbol\nu$; so $Z_{\rm top}$ is fixed. (Its $\Omega_s\cap X_o$ does depend on $\boldsymbol\nu$ when $n=\mathsf N_s$ and $s$ is the top level; that entry is not used as an input below.) Just after step $t$ every mark has level $<t$, so the level-$t$ entries are untouched. Second claim: a standing mark $X_o$ meeting $X$ lies in $Z_s$, and $Z_s\subset Z_t$ by (N) for the determining label of $h'$ (the induction hypothesis of Theorem 6); $X_o$ is connected, so $X_o\subset X$, and marks wait (Y 62128) gives $s<t_\flat$; its levels are $<t_\flat$. (b) A step copies earlier entries and marks (Y 62174) and adds top entries, which no mark touches. (c) Compare entries cube by cube. Outside the class components, nothing changes and the same marks stand. In a healed component (and an island below $t$, and $\Omega_t$ of an island) every entry is $X$ in both labels, and the swallowed marks cease to stand; an island's $\Lambda_t$ is a top entry. In a new drop-out $X$ at level $l\in(t_\flat,t]$: by (a) no older mark acts there, so $\mathcal L^{\boldsymbol\nu}(h)$ has $X\setminus Z''_l$ for $l\le t_\flat+\boldsymbol\nu(X)$ and $\Omega^\circ_l=\Omega_l(\mathcal S'_t)\cap X=\Omega^{\boldsymbol\nu'}_l(h')\cap X$ above, which is Lemma 4's rule with $m=\boldsymbol\nu(X)$. At levels $\le t_\flat$ in $X$ the operation changes nothing, and both labels apply the same older marks to the same entries. $\square$

This is the content of Y's reindexed-cell formula (Y 62153-62190), restricted to what the geometry uses.

## 4. Step 4: the induction, and the theorem

**Theorem 6 (`prop:large-field-2-3`, display).** Assume Y's rules and inputs of section 2 (marked [Y]), with $L\ge3$ odd, every $\check R_i$ a power of $L$ with $\check R_i\ge1$, and the torus admissible (Y 61911). Let $h$ be any history, at any moment: just after a step, during the operation of the top level $t$ with any outcome or stage count $0\le m(X)\le\mathsf N_t$ for each class component, or after it. Let $\boldsymbol\nu$ be any stopping vector on the drop-outs standing in $h$. Then the label $\mathcal L^{\boldsymbol\nu}(h)$, with top level $s$, satisfies (N), (G), and for $1\le j<s$:
$$\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM,\qquad\Omega_{j+1}\subset\Lambda_j^{\sim-1},\qquad Z_j^\sim\cap\Omega_{j+2}=\emptyset\ (j+2\le s),$$
in level-$j$ units with layers of $M$-cubes of level $j$; $\Lambda^{\sim-1}_j:=((Z_j)^{\sim})^c$ and $Z_j^\sim:=Z_j^{[u_j]}$. Also $d(\Omega_0^c,\Omega_1)\ge u_1$ and $T_\ell\supset\Omega_0\supset\Omega_1\supset\Lambda_1\supset\cdots\supset\Lambda_s$.

*Proof.* Induction on the number of moves of $h$, for all $\boldsymbol\nu$ at once. Base: after step 1, Lemma 2 ($t=1$); there are no marks. Step $t$: by Lemma 5(b), $\mathcal L^{\boldsymbol\nu}(h)$ is $\mathcal L^{\boldsymbol\nu}(h')$, which satisfies (N), (G) by induction, extended by the new top entries. By Lemma 5(a), $Z_{t-1}$ is the same set as in the determining label. Lemma 2 gives $\Lambda_t\subset\Omega_t$ and $d(Z_{t-1},\Omega_t)\ge u_t$, hence (N) and (G) at the new top. Operation $t$ (including partial stages): by Lemma 5(c), $\mathcal L^{\boldsymbol\nu}(h)$ comes from $\mathcal L'=\mathcal L^{\boldsymbol\nu'}(h')$ by Lemma 4's rules. Lemma 4's hypotheses: (N), (G) by induction; rule (b) because top entries are $\boldsymbol\nu$-independent (Lemma 5(a)) and $\mathcal L'$ is the label just after step $t$; the class components are distinct components of $Z'_t$ (Y 63684); and their nests satisfy Lemma 3, because the entries inside $X$ at levels $\ge t_\flat$, so $G_i$ for $i\ge t_\flat$, are those of the determining label (Lemma 5(a)). Order: Y's proof of the quiet boxes at level $t$ (Y 63714-63766) uses the nesting (N) and the monotonicity (F1) only for the determining labels of the moves before the operation of level $t$. These are induction hypotheses here. So the quiet boxes at level $t$ are available at this step, and the induction is joint: (N), (G) for all moves up to step $t$, then the quiet boxes at level $t$, then Lemma 3, then Lemma 4. So $\mathcal L^{\boldsymbol\nu}(h)$ satisfies (N), (G).

The display. The gap is (G), as $u_{j+1}=LM$ level-$j$ units. First inclusion: $\Omega_{j+1}$ is a union of $M$-cubes of level $j+1$ (step regions: level-$(j+1)$ cells; windows: $X\setminus D_{j+1}$, Lemma 3), hence of level $j$ by nesting. For such a cube $q$, if $q\subset Z_j^{[u_j]}$ then $d(Z_j,q)\le u_j<u_{j+1}$, contradicting (G); so $q\subset(Z_j^\sim)^c=\Lambda_j^{\sim-1}$. Second: by (N) $\Omega_{j+2}\subset\Omega_{j+1}$, so $d(Z_j^{[u_j]},\Omega_{j+2})\ge u_{j+1}-u_j>0$; the sets do not meet, even as point sets. $\square$

**Remark.** The gap is attained ($=u_{j+1}$) at the active indices $k_0+2\le j<t$ of a prepared nest (Lemma 3), as Y says (Y 62089-62091); so it cannot be improved to a multiple of a cell. At $j=k_0+1$ it is $w_j-w_{j+1}\ge u_{j+1}$ (Y 62092-62093).

## 5. Step 3: constants

The constants listed at `geo-5.md` line 45 serve its sections 3.4-3.6 (towers, cut meets, weighted paths). Sections 3.2-3.3, and their port above, use none of them:

| `geo-5.md` (line 45) | used in 3.2-3.3 / here? | replaced by |
|---|---|---|
| $M>\rho\ge2$ | no | — |
| $\mu\ge\rho$ | no | — |
| $M\ge80\mu$ | no | — |
| $L\ge27$ | no | — |
| $\theta\min(M,\rho)\ge64\log L$ | no | — |
| implicit: step padding and cell side exceed one later $M$-cube ($s_t\ge LM\xi_{t-1}$) | yes (Lemmas 1, 2) | $a_t\ge u_t$, i.e. $\check R_t\ge1$: $\check R_t$ is a power of $L$ (Y 62001) and $\mathsf N_t=\check R_t$ counts stages (Y 62195, Y 63882). $\check R_t\ge1$ is not one line of Y; it follows from Y 62001 and $x_i=g_i^{-2}\ge\gamma^{-2}\ge e$ (Y 61911, Y 83084; $\gamma<e^{-1/2}$ at Y 1102-1103) |
| implicit: box gap (3.1) | yes (Lemma 3) | $L\ge3$ in the case $l=k_0+1$, from Y's $L\ge13$ (Y 650); $L$ odd for alignment (Y 63807) |

Lemma 0 and Y's box formula need the cubes and the boxes of a class component not to wrap: Y's torus floor $\ell L^{K-j}\ge2L^{11}M\check R_j$ (Y 61911), with class boxes of at most $100$ cells per side (Y 63770-63771), gives it. Y's $R_1\ge L$, $M_1'\ge R_1\mathfrak M$, $M\ge L^4M_1'$ (Y 650-652) are not used. Neither of Y's two constants named $\rho$ is used: not $\rho=R_1\mathfrak M$ (Y 638-639), and not the $\rho$ with $R_1\mathfrak M\ge L^2\rho$ (Y 14938-14942, which Y 49962 writes as $\rho=L^{-2}R_1\mathfrak M$). So the conflict that `core-read.md` section 2 flagged does not touch this statement. The theorem holds for every $M\ge1$.

## 6. Step 5: the form used by `h-geo.md`

**Corollary 7 (CORE).** Let $X$ be a class component of level $m$, $h=m_\flat$, and consider $\mathcal S'_m$ for any history and any stopping vector on its standing drop-outs (action, determining, or intermediate). For $0\le q<h$, the pair $(q,q+1)$ of the sequence $A_q\cap X=\Omega_q\cap X$ of `h-geo.md` section 2 has
$$g_q=d(X\setminus\Omega_q,\ X\cap\Omega_{q+1})\ge u_{q+1}=LM\xi_q,\ \text{with}\ \xi_q=L^q,\ \text{in bare units}.$$
*Proof.* $X\setminus\Omega_q\subset\Omega_q^c\subset Z_q$ by (N), and Theorem 6 gives $d(Z_q,\Omega_{q+1})\ge u_{q+1}$; for $q=0$, $d(\Omega_0^c,\Omega_1)\ge u_1$. $\square$

In one line: **yes**, Theorem 6 gives hypothesis CORE of `library/h-geo.md` section 6 item 1, for every admissible earlier history and with the nests kept by older drop-outs. It gives it in a stronger form, with the $\Lambda$-holes and on the whole torus, not only inside $G_h$. With Lemma 2 of `h-geo.md`, H-GEO then holds without the CORE hypothesis, given the [Y] inputs.

## 7. What stays open, and checks

1. **Checked twice, line by line (2026-11-10):** by Claude Fable 5.2 medium (`library/core-gaps-check.md`; repairs R1-R7 applied) and by Codex, launched as gpt-6-astra max (`library/core-gaps-xcheck.md`; first failing step none, no repair).
2. **[Y] inputs used as stated, not re-derived here:** the quiet boxes, from Y's tracing and restriction paragraphs (Y 63694-63766); the prepared-box formula with the index $k_0$, $h<k_0\le t-2$ (Y 63774-63809; its existence above a scale floor is `library/geoh.md` 186-190, by `h-geo.md` section 6 item 4); "marks wait", from the quarantine condition (Y 62128, Y 63684-63690); and that standing marks keep $\Lambda_s\cap X_o=\emptyset$ until a healing or island swallows them (Y 62107-62128). Each is Y's own statement with Y's reason; the box arithmetic was checked in `h-geo-check.md`.
3. **Readings (R1)-(R3)** of section 2.3. Only (R2), that healing and islands fill $\Omega_0$, matters, and only for the pair $(0,1)$. Y's display ($j\ge1$) does not need it.
4. **Out of scope** (other sentences of the proposition): the gaps $cM\check R_j$ for regions as produced by steps (Lemma 2 gives $8a_t$ at the moment of the step only); "every large-field region and every creation set is a union of cells of its own level"; the decomposition of unity and the creation counts; the identity $\Omega^{\boldsymbol\nu_\mu}_l(\mathcal S_t)=\Omega_l(\mathcal S^\mu)\cup Z_{[j,t]}$ (Y 62128).
5. No computation was run. Each step is a finite set-inclusion or distance argument between unions of grid cubes, suitable for a proof assistant.

RESULT: CORE-GAPS proved (stop (i)). Y's step rule and initial rule exist at Y 61973-61990: $Z_t\supset(\Omega_t^c)^{\sim2}$, $\widehat Y^{\sim8}\subset\Omega_t^c$, and $\Omega_0=\Omega_1^\sim$. With them, `geo-5.md` 3.2-3.3 ports to Y. Theorem 6 proves Y's display of `prop:large-field-2-3` ($\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM$, $\Omega_{j+1}\subset\Lambda_j^{\sim-1}$, $Z_j^\sim\cap\Omega_{j+2}=\emptyset$) and the nesting, for every history, every stage count and fate, and every stopping vector. It uses only $L\ge3$ odd and $\check R\ge1$; none of geo-5's $\rho,\mu,\theta$, $M\ge80\mu$, $L\ge27$. Corollary 7 gives CORE of `h-geo.md`. Open: a cross-provider check; Y's box formula, quiet boxes and "marks wait" are used as stated [Y]; reading (R2) (healing fills $\Omega_0$) for the pair (0,1) only.
