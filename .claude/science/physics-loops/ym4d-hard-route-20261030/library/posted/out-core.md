# A proposed proof of your `prop:large-field-2-3`

Provenance: Claude Opus 5.5 wrote the proof and this note. Claude Fable 5.2 and Codex (GPT-6) each checked the proof line by line. Not an audit.

All rules, symbols and statements used below are yours. The source is `YM4/YM4_1400.tex` at commit `c7fef8b21b58` of ethanwsussman/Yang--Mills-LLM-experiment ([the file](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/c7fef8b21b58/YM4/YM4_1400.tex)). "Line n" means line n of that file.

## 1. Your proposition, and what your text gives for it

Your proposition is at lines 62080-62101. It opens (line 62080): "The regions are nested, $`T_\ell\supset\Omega_1\supset\Lambda_1\supset\dots\supset\Lambda_k`$, with gaps of at least $`cM\check{R}_j`$ in level-$`j`$ units. Every large-field region and every creation set is a union of cells of its own level. Both statements hold for the regions that the steps produce (119, p. 256)."

It continues (line 62080): "Each operation $`\mathbf{R}`$ has stage sequences and prepared sequences [...], and drop-outs keep nests. In these sequences and nests the boxes are only unions of $`M`$-cubes, and the only lower bound on the gaps is one $`M`$-cube of the later level:". The display follows at lines 62082-62087:

```math
\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM,\qquad \Omega_{j+1}\subset\Lambda_j^{\sim-1},\qquad Z_j^\sim\cap\Omega_{j+2}=\emptyset
```

with the words "(level-$`j`$ units; layers of $`M`$-cubes of level $`j`$)". Lines 62089-62094 add: "the first inequality is an equality at the active indices $`k_0(t)+2\le j<t`$ of the upper part of a nest prepared at level $`t`$", and "At $`j=k_0(t)+1`$ the gap is instead $`w_j-w_{j+1}`$ in bare units, which still gives the displayed lower bound but can be larger". The proposition then describes the two kinds of creation (lines 62094-62098). It ends at line 62101.

What your text gives for it:

- Inside the proposition, one reference: "(119, p. 256)". It is attached to "the regions that the steps produce".
- No proof follows. The proposition ends at line 62101, and line 62103 begins the paragraph "Three fates, marked components, two sequences of regions".
- The label `prop:large-field-2-3` occurs at lines 62080, 62128 and 63716 only. Line 62128 says "and so \cref{prop:large-field-2-3} applies to it". Line 63716 says "We use the nesting of \cref{prop:large-field-2-3} on these labels". Both lines use the proposition. Neither proves it.

What this note treats. This note proves the nesting and the display for every history, at every moment of a history, and for every stopping vector (Theorem 6 in section 5). Section 7 lists the sentences of the proposition that this note does not treat.

## 2. Your rules that the proof uses

Each rule is quoted from your text, with its line. The labels (S1)-(S15) are used in section 5.

**(S1) Initial rule.** Line 61973: "A label's sequence starts at $`\Omega_0=\Omega_1^\sim`$, the first region enlarged by one layer of level-$`1`$ cells, and not at $`T_\ell`$".

**(S2) Live region of a step.** Line 61973: "The tests of step $`t=k+1`$ are applied to a term of $`\rho_k`$ whose live region is $`Y=\mathcal{Z}_k`$." Line 1586: "let $`\mathcal Z_k(h)`$ be the live region after healing."

**(S3) Units of hulls and layers.** Line 61973: "Hulls ($`'`$, $`\widehat{\cdot}`$) and layers are taken in level-$`t`$ cells." Lines 645-648: "For a cubical region $`Y`$, $`Y^{\sim n}`$ means addition of $`n`$ layers in the partition currently named; $`Y^{\sim-n}`$ means removal of those layers. A hull is the smallest union of cubes of the named partition containing the set. These operations include their periodic versions."

**(S4) Boxing.** Line 61980: "The boxing map $`\mathsf{bx}`$ replaces each component contained in a cube of $`O(1)`$ cells by its bounding box, and repeats this until nothing changes."

**(S5) Step rule.** Lines 61983-61987:

```math
\Omega_t^c=Q_t'^{\sim2}\cup P_t'^{\sim4}\cup H_t,\qquad H_t=\begin{cases}\widehat{Y}^{\sim8},&t\ge2,\\ P_0'^{\sim5},&t=1,\end{cases}
```

```math
Z^{[0]}=\mathsf{bx}\big((\Omega_t^c)^{\sim2}\cup R_t'^{\sim}\big),\qquad Z^{[n+1]}=\mathsf{bx}\big(Z^{[n]}\cup(\text{cells of the failures of round }n)^{\sim}\big).
```

Line 61990: "The set $`Z_t=\Lambda_t^c`$ is the final $`Z^{[n]}`$". Lines 71099-71100 state the consequence: "The pre-operation region $`Z_h`$ contains $`(\Omega_h^c)^{\sim2}`$".

**(S6) Cells and cubes.** Line 62096: the cells of level $`t`$ "are $`M\check{R}_t`$-cubes of level $`t`$". Lines 643-644: "The partition $`\pi_j`$ consists of the centered, half-open $`M`$-cubes in level-$`j`$ units." Line 63749: "$`a_i=M\check R_iL^i`$, the side of a level-$`i`$ cell". Line 63774: "Let $`u_i=ML^i`$ be the side of an $`M`$-cube at level $`i`$ in bare units."

**(S7) The size $`\check R`$ and nested partitions.** Line 62001: "The size $`\check{R}_k`$ is the smallest power of $`L`$ that is not less than $`(\log\min_{i\le k}x_i)^r`$, with $`r\ge2`$. Because it is a power of $`L`$, all partitions are nested." Line 62195: "since $`\mathsf{N}_t=\check{R}_t`$ is non-increasing". Line 63882: "Since $`\mathsf{N}_k=\check{R}_k\approx(\log x_k)^r`$".

**(S8) Depth and class.** Line 63684: "Let $`k_\flat=k-\mathsf{N}_k\ge1`$ (*depth*)". "A component $`X`$ of $`Z_k`$ belongs to the class when three conditions hold." The third condition: "it has not been acted on by any operation whose level lies in $`[k_\flat,k)`$, the lower end point included (*quarantine*)." Line 63684 also defines the box enlargement: "let $`B^{[r]}`$ be the box $`B`$ with each face pushed outward by $`r`$ such cells". Lines 63750-63752: "For a box $`B`$, write $`B^{[s]}`$ for its enlargement by a distance $`s`$ in the sup norm in its lift."

**(S9) Three fates.** Line 62103: "We set $`t_\flat:=t-\mathsf{N}_t`$. In each component $`X`$ of its class [...], the operation $`\mathbf{R}`$ of level $`t`$ prepares a nest $`Z''_l(X)`$, $`t_\flat<l\le t`$." Line 62105, healed: "$`\Omega_l,\Lambda_l,S_l\mapsto\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X`$ for $`l\le t`$, and $`X`$ leaves the label." Line 62106, island: "the same replacement is made for $`l<t`$ and for $`\Omega_t`$, $`S_t`$, but $`\Lambda_t`$ is left unchanged. Thus $`X\subset Z_t`$ remains". Line 62107, drop-out: "(some test fails after $`n\le\mathsf{N}_t`$ stages): $`X`$ remains in $`Z_t`$". Lines 62110-62115:

```math
\Omega_l\cap X=X\setminus Z''_l(X)\ \ (t_\flat<l\le t_\flat+n),\qquad \Lambda_l\cap X=X\setminus Z''_l(X)\ \ (\text{the same }l,\ l<t),
```

"all other entries unchanged, so $`\Lambda_t\cap X=\emptyset`$."

**(S10) Marks and stopping vectors.** Line 62121: "Islands and drop-outs are the *marked components*. A mark persists until a later healed component or island swallows it." "A drop-out's mark keeps the regions $`\Omega^\circ_l=\Omega_l\cap X`$, and likewise $`\Lambda^\circ_l,S^\circ_l`$, which $`X`$ possessed before the operation. For $`0\le\boldsymbol{\nu}(X)\le n(X)`$ we set" (lines 62124-62125)

```math
\Omega^{\boldsymbol{\nu}}_l\cap X=X\setminus Z''_l(X)\ \ (t_\flat<l\le t_\flat+\boldsymbol{\nu}(X)),\qquad \Omega^{\boldsymbol{\nu}}_l\cap X=\Omega^\circ_l\ \ (t_\flat+\boldsymbol{\nu}(X)<l\le t_\flat+n(X)).
```

Line 62128: "The choice $`\boldsymbol{\nu}=n`$ gives the *determining sequence*", and "each $`\Omega^{\boldsymbol{\nu}}`$ is the geometric label obtained by stopping the operations after $`\boldsymbol{\nu}`$ stages."

**(S11) The rule for $`\Lambda`$.** Lines 62161-62168 give the reindexed-cell formula for $`\Omega`$. Lines 62169-62171: "For $`l<s`$ the same rule holds for $`\Lambda_l`$ with $`\Lambda_l(\mathcal S'_s)`$ in the second line. At $`l=s`$ the drop-out keeps $`q`$ outside $`\Lambda_s`$."

**(S12) Steps copy, operations overwrite.** Lines 62174-62180: "At a step, the earlier entries and standing marks are copied. At an operation, a healed component or an island overwrites the older entries on its region, and any mark it swallows ceases to stand. Outside the class no entries change. On a drop-out the new entries through stage $`m`$ are the complements of the corresponding prepared boxes, and the earlier rule supplies all entries outside its window."

**(S13) Labels before and after an operation.** Lines 63714-63715: "Write $`\mathcal S'_s`$ and $`\mathcal S_s`$ for the labels just before and after the operation of level $`s`$."

**(S14) The torus.** Line 1640: "$`T_\ell=(\mathbb R/\ell\mathbb Z)^4`$". Line 61911: "the torus is admissible up to level $`k`$ [...]; that is, $`\ell L^{K-j}\ge2L^{11}M\check{R}_j`$ for $`j\le k`$". Line 63692: "Hence no cell, no box and no neighbourhood of a box wraps around the torus."

**(S15) The constant $`L`$.** Line 650: "Take $`L\ge13`$ odd".

## 3. Statements taken from your text as stated

The proof takes the following statements from your text as stated. It does not prove them again. Each is a hypothesis of Theorem 6.

**(H1) Layers.** Adding $`r`$ layers of level-$`t`$ cells to a union $`A`$ of level-$`t`$ cells gives a set that contains $`A^{[ra_t]}`$, the set of points at sup distance at most $`ra_t`$ from $`A`$. Your lines 645-648 define the addition of layers. Your line 63684 defines $`B^{[r]}`$ on a box by pushing each face out by $`r`$ cells. Your lines 63686-63690 give the step output on a quiet component as $`\Omega_i^c\cap X=H_i^{[8]}`$, and lines 63760-63763 write the same set as $`H_i^{[8a_i]}`$, with "enlargement by a distance $`s`$ in the sup norm" (line 63751). So your text states (H1) for a box. We use the same sup-norm convention for every union of cells of one level.

**(H2) Quiet boxes.** Let $`X`$ be a class component of level $`k`$ and $`h=k_\flat`$. Lines 63684 and 63756: $`H_i`$ is the hull, in level-$`i`$ cells, of $`G_{i-1}:=X\cap Z_{i-1}`$, and "$`G_{i-1}\subset H_i\subset G_{i-1}^{[a_i]}`$". Lines 63752-63753: "The oldest component $`G_h`$ is a nonempty box". Lines 63760-63766, `eq:elab-history-quiet-boxes`:

```math
O_i:=\Omega_i^c\cap X=H_i^{[8a_i]},\qquad G_i=H_i^{[10a_i]},\qquad G_k=X,
```

for $`k_\flat<i\le k`$, where "$`\Omega_i,Z_i`$ without a label refer to $`\mathcal S'_k`$" (lines 63766-63767).

**(H3) Prepared boxes.** Lines 63775-63777: "let $`k_0+1`$ be the last index with $`a_{k_0+1}=u_k`$, with $`h<k_0\le k-2`$." Lines 63783-63784:

```math
w_{k_0+1}=2u_k,\qquad w_k=0,\qquad w_i=\sum_{q=i+1}^k u_q\quad (k_0+2\le i<k).
```

Lines 63798-63803, `eq:elab-history-prepared-boxes`:

```math
Z''_i(X)=\begin{cases}H_i^{[3a_i]},& h<i\le k_0,\\ H_{k_0+1}^{[3u_k-w_i]},& k_0<i\le k.\end{cases}
```

Lines 63805-63809: "The first box is a union of level-$`i`$ cells. [...] Since $`L`$ is odd, those faces also lie on the grid with side $`u_i`$, and $`3u_k-w_i`$ is a multiple of $`u_i`$. The second box is therefore a union of $`M`$-cubes of level $`i`$."

**(H4) Marks wait.** Line 62128: "a mark of level $`s`$ lying inside a class component of level $`t`$ satisfies $`s<t_\flat`$. Hence standing marks that share a part are nested, their windows $`(s_\flat,s]`$ are disjoint".

**(H5) A standing drop-out stays outside its top entry.** A drop-out $`X_o`$ of level $`s`$ keeps $`\Lambda_s\cap X_o=\emptyset`$ for every stage index, until a later healed component or island swallows it. Lines 62115, 62171 and 62121 state this: "so $`\Lambda_t\cap X=\emptyset`$", "At $`l=s`$ the drop-out keeps $`q`$ outside $`\Lambda_s`$", and "A mark persists until a later healed component or island swallows it."

**(H6) No wrapping.** Line 63692: "no cell, no box and no neighbourhood of a box wraps around the torus." Lines 63770-63771: a class component has "at most $`100`$" cells along each side. We use this so that balls, boxes, and the enlargements of boxes up to the sizes below are those of a lift to $`\mathbb R^4`$.

One remark on order. Your derivation of (H2) begins: "We use the nesting of \cref{prop:large-field-2-3} on these labels" (lines 63715-63716). It uses the nesting, and the fact that "the regions $`Z_i`$ decrease as these labels advance" (lines 63716-63720), only for the labels $`\mathcal S'_s`$, $`\mathcal S_s`$ with $`s<k`$ and for $`\mathcal S'_k`$ (lines 63714-63741). These are moments before the operation of level $`k`$. The proof of Theorem 6 uses (H2) at level $`k`$ only after it has proved the nesting for all those moments. So the use of (H2) is not circular.

## 4. Two readings

The proof uses two readings of your wording. Each is a reading, not a rule that your text states in these words.

**(R1) The live region of step $`t`$.** We read the live region $`Y=\mathcal Z_{t-1}`$ of step $`t`$ (rule (S2)) as $`Z_{t-1}(\mathcal S_{t-1})`$, the region $`Z_{t-1}`$ of the label after the operation of level $`t-1`$. Your text supports this reading. Line 1586: "let $`\mathcal Z_k(h)`$ be the live region after healing". Line 62106: for an island, "$`X\subset Z_t`$ remains". Line 62107: a drop-out "$`X`$ remains in $`Z_t`$". The proof uses only the inclusion $`Z_{t-1}\subset\widehat Y`$.

**(R2) Healing and islands at the entry $`l=0`$.** We read the fate rules "for $`l\le t`$" (line 62105) and "for $`l<t`$" (line 62106) as including the entry $`l=0`$, because "A label's sequence starts at $`\Omega_0`$" (line 61973). So a healed component or an island $`X`$ replaces $`\Omega_0`$ by $`\Omega_0\cup X`$.

(R2) matters for the pair $`(0,1)`$ only. Your display concerns $`j\ge1`$ and does not use it. If healing did not fill $`\Omega_0`$, the pair $`(0,1)`$ would have gap $`0`$ inside a healed component that meets $`\Omega_0^c`$.

A second reading gives the pair $`(0,1)`$ as well. Read line 61973 as a standing rule: $`\Omega_0`$ is $`\Omega_1^\sim`$ at every moment. Then after healing $`\Omega_0=(\Omega_1\cup X)^\sim\supset\Omega_0\cup X`$, and Lemma 0 gives $`d(\Omega_0^c,\Omega_1)\ge a_1`$ directly. Only the reading in which $`\Omega_0`$ is frozen at step $`1`$ and is not filled by healing breaks the pair $`(0,1)`$. We searched lines 61900-66000 for $`\Omega_0`$. It occurs at lines 61973, 62078, 62245, 63032, 63039 and 63374. None of these lines states the rule for $`\Omega_0`$ under healing.

## 5. The proof

### 5.1 Notation

All lengths are in bare units. Put $`u_i=ML^i`$, the side of an $`M`$-cube of level $`i`$, and $`a_i=M\check R_iL^i`$, the side of a level-$`i`$ cell (rule (S6)). Since $`\check R_i\ge1`$ (section 6), $`a_i\ge u_i`$. Also $`u_{i+1}=Lu_i`$, so "$`LM`$ in level-$`j`$ units" is the bare length $`u_{j+1}`$.

A label at top level $`s`$ is the pair of sequences $`(\Omega_l)_{0\le l\le s}`$ and $`(\Lambda_l)_{1\le l\le s}`$. Put $`Z_l:=\Lambda_l^c`$. For uniformity put $`\Lambda_0:=\Omega_0`$ and $`Z_0:=\Omega_0^c`$.

Regions are unions of closed cubes of the nested grids. The complement of a region is the union of the grid cubes that are not in the region. $`d`$ is the periodic sup distance between point sets of $`T_\ell`$. For a set $`A`$ and $`g\ge0`$, $`A^{[g]}=\{x:d(x,A)\le g\}`$. For every set $`A`$ and $`r,s\ge0`$, $`(A^{[r]})^{[s]}=A^{[r+s]}`$, because a sup-ball of radius $`r+s`$ is the sum of sup-balls of radii $`r`$ and $`s`$. On a box this agrees with your $`B^{[s]}`$ of lines 63750-63752.

A history is the alternating sequence step $`1`$, operation $`1`$, step $`2`$, operation $`2`$, ..., with its recorded outcomes. $`\mathcal S'_t`$ and $`\mathcal S_t`$ are the labels just before and just after the operation of level $`t`$ (rule (S13)).

Your text uses the letter $`h`$ for a history and for the depth $`h=t_\flat`$. We keep both uses. In Lemma 3, $`h`$ is the depth. In Lemma 5 and Theorem 6, $`h`$ is a history.

A site set or bond set lies in its closed carrier. So a lower bound on the distance of carriers is a lower bound on the distance of sites. We work with carriers.

### 5.2 Lemma 0 (grid separation)

**Lemma 0.** Let $`\mathcal G`$ be one of the nested grids of closed cubes. Let $`B`$ be a union of $`\mathcal G`$-cubes, $`f`$ a $`\mathcal G`$-cube with $`f\not\subset B`$, $`A`$ a set, and $`g>0`$ with $`A^{[g]}\subset B`$. Then $`d(f,A)\ge g`$.

*Proof.* Suppose that $`d(f,A)<g`$. Then there are $`p\in f`$ and $`a\in A`$ with $`d(p,a)<g`$. By the triangle inequality, the open sup-ball of radius $`g-d(p,a)`$ about $`p`$ lies in $`A^{[g]}`$, hence in $`B`$. The point $`p`$ lies in the closure of the interior of $`f`$, so this ball meets $`\operatorname{int}f`$. So $`\operatorname{int}f`$ meets a $`\mathcal G`$-cube $`f'\subset B`$. A point of $`\operatorname{int}f`$ in the closed cube $`f'`$ has a neighbourhood in $`\operatorname{int}f`$, and this neighbourhood meets $`\operatorname{int}f'`$. Distinct cubes of one grid have disjoint interiors. So $`f=f'\subset B`$, a contradiction. The grid cubes are small against the torus (rule (S14)), so interiors and balls are those of a lift. $`\square`$

### 5.3 Lemma 1 (padding after a step)

**Lemma 1.** Let $`\mathcal S`$ be the label just after step $`t`$. Let $`e`$ be a level-$`t`$ cell with $`e\subset\Omega_t^c`$, and let $`K_e`$ be the component of $`Z_t`$ that contains $`e`$. Then every level-$`t`$ cell $`f`$ that is not in $`K_e`$ has $`d(f,e)\ge2a_t`$. In particular, if $`X\ne K_e`$ is another component of $`Z_t`$, then $`d(e,X)\ge2a_t`$.

*Proof.* First, $`Z_t\supset(\Omega_t^c)^{\sim2}`$. By rule (S5), $`Z^{[0]}=\mathsf{bx}((\Omega_t^c)^{\sim2}\cup R_t'^{\sim})`$. The boxing map replaces a component by its bounding box (rule (S4)), and a bounding box contains its component. So $`\mathsf{bx}(A)\supset A`$ for every $`A`$, and $`Z^{[0]}\supset(\Omega_t^c)^{\sim2}`$. For the same reason $`Z^{[n+1]}\supset Z^{[n]}`$. $`Z_t`$ is the final $`Z^{[n]}`$ (line 61990). So $`Z_t\supset(\Omega_t^c)^{\sim2}`$. Your lines 71099-71100 state the same.

$`\Omega_t^c`$ is a union of level-$`t`$ cells, because hulls and layers are taken in level-$`t`$ cells (rule (S3)). By (H1), $`(\Omega_t^c)^{\sim2}\supset(\Omega_t^c)^{[2a_t]}\supset e^{[2a_t]}`$. So $`e^{[2a_t]}\subset Z_t`$. The set $`e^{[2a_t]}`$ is the box of $`5^4`$ level-$`t`$ cells with $`e`$ at its centre (no wrapping, rule (S14)). It is face-connected and contains $`e`$. So it lies in $`K_e`$, under any convention of connectivity for components.

$`Z_t`$ is a union of level-$`t`$ cells, so $`K_e`$ is a union of level-$`t`$ cells. Apply Lemma 0 with $`\mathcal G`$ the level-$`t`$ cells, $`B=K_e`$, $`A=e`$ and $`g=2a_t`$. It gives $`d(f,e)\ge2a_t`$ for every level-$`t`$ cell $`f\not\subset K_e`$. Distinct components share no cell, so every cell of $`X`$ is such an $`f`$. $`\square`$

### 5.4 Lemma 2 (a step)

**Lemma 2.** Let $`t\ge1`$, and let $`\mathcal L`$ be the label after the operation of level $`t-1`$ (empty for $`t=1`$). The label $`\mathcal L'`$ after step $`t`$ copies the entries $`l\le t-1`$ (rule (S12)) and has new entries $`\Omega_t,\Lambda_t`$, and also $`\Omega_0`$ when $`t=1`$. Then $`\Lambda_t\subset\Omega_t`$, and:

- for $`t\ge2`$: $`d(Z_{t-1},\Omega_t)\ge8a_t\ge u_t`$;
- for $`t=1`$: $`d(\Omega_0^c,\Omega_1)\ge a_1\ge u_1`$.

*Proof.* By Lemma 1, $`Z_t\supset(\Omega_t^c)^{\sim2}`$, and by (H1) this set contains $`\Omega_t^c`$. Taking complements, $`\Lambda_t\subset\Omega_t`$.

Let $`t\ge2`$. By reading (R1), $`Z_{t-1}=Y`$. A hull contains its set (rule (S3)), so $`Y\subset\widehat Y`$. $`\widehat Y`$ is a union of level-$`t`$ cells. By (H1) and rule (S5), $`\widehat Y^{[8a_t]}\subset\widehat Y^{\sim8}=H_t\subset\Omega_t^c`$. $`\Omega_t^c`$ is a union of level-$`t`$ cells. A level-$`t`$ cell $`f`$ of $`\Omega_t`$ is not in $`\Omega_t^c`$. Lemma 0, with $`\mathcal G`$ the level-$`t`$ cells, $`B=\Omega_t^c`$, $`A=\widehat Y`$ and $`g=8a_t`$, gives $`d(f,\widehat Y)\ge8a_t`$. So $`d(Z_{t-1},\Omega_t)\ge8a_t`$.

Let $`t=1`$. By rule (S1), $`\Omega_0=\Omega_1^\sim`$, one layer of level-$`1`$ cells. By (H1), $`\Omega_0\supset\Omega_1^{[a_1]}`$. $`\Omega_0`$ is a union of level-$`1`$ cells, and so is $`\Omega_0^c`$. Lemma 0, with $`\mathcal G`$ the level-$`1`$ cells, $`B=\Omega_0`$, $`A=\Omega_1`$, $`g=a_1`$ and $`f`$ a level-$`1`$ cell of $`\Omega_0^c`$, gives $`d(f,\Omega_1)\ge a_1`$.

Finally $`a_t\ge u_t`$, because $`\check R_t\ge1`$. $`\square`$

### 5.5 Lemma 3 (box gaps in a class component)

**Lemma 3.** Let $`X`$ be a class component of level $`t`$, and $`h=t_\flat=t-\mathsf N_t\ge1`$. Take all regions in $`\mathcal S'_t`$. Let $`G_i`$, $`H_i`$, $`O_i`$ be as in (H2), with $`k=t`$. Let $`k_0`$ and $`w_i`$ be as in (H3), with $`k=t`$, so that $`h<k_0\le t-2`$ and $`a_{k_0+1}=u_t`$. Put $`D_i:=Z''_i(X)`$ for $`h<i\le t`$, as in (H3), and $`D_h:=G_h`$. For $`h\le l<t`$ define $`g_l`$ by the cases below. Then, for $`h\le l<t`$, in the lift of $`X`$,

```math
D_l^{[g_l]}\subset D_{l+1},\qquad g_l\ge u_{l+1},\qquad D_l\subset D_{l+1},\qquad D_l\subset G_l .
```

The cases are:

- (a) $`l=h`$: $`g_h=3a_{h+1}`$.
- (b) $`h<l<k_0`$: $`g_l=7a_l+3a_{l+1}`$.
- (c) $`l=k_0`$: $`g_{k_0}=7a_{k_0}+u_t`$.
- (d) $`l=k_0+1`$: $`g_{k_0+1}=w_{k_0+1}-w_{k_0+2}`$, which is $`2u_t`$ if $`k_0+2=t`$, and is at least $`u_t\tfrac{L-2}{L-1}`$ otherwise.
- (e) $`k_0+2\le l<t`$: $`g_l=w_l-w_{l+1}=u_{l+1}`$.

Two more box facts hold. They are not used below.

- (f) For $`h<i<t`$: $`D_i\subset O_i`$ and $`O_{i+1}\supset O_i^{[2a_i+8a_{i+1}]}`$. Hence, for $`h<j+1<t`$, $`D_{j+1}^{[8a_{j+2}]}\subset O_{j+2}`$.
- (g) $`Z''_t(X)^{[5u_t+2a_t]}\subset X`$.

Consequence: for $`h\le l<t`$, $`d(D_l,X\setminus D_{l+1})\ge u_{l+1}`$.

*Proof.* We use the box formulas (H2) and (H3) with $`k=t`$, and $`(A^{[r]})^{[s]}=A^{[r+s]}`$ (section 5.1). Also $`A\subset B`$ implies $`A^{[s]}\subset B^{[s]}`$. By (H2), $`G_{i-1}\subset H_i`$ for $`h<i\le t`$.

(a) $`l=h`$. $`H_{h+1}`$ is the hull of $`G_h`$, so $`G_h\subset H_{h+1}`$. Since $`h<k_0`$, we have $`h+1\le k_0`$, so $`D_{h+1}=H_{h+1}^{[3a_{h+1}]}`$ by (H3). Hence $`D_h^{[3a_{h+1}]}=G_h^{[3a_{h+1}]}\subset H_{h+1}^{[3a_{h+1}]}=D_{h+1}`$. Your lines 63819-63820 state the same separation: "The separation from $`G_h`$ to the exterior of $`Z''_{h+1}(X)`$ in $`X`$ is at least $`3a_{h+1}`$."

(b) $`h<l<k_0`$. $`D_l=H_l^{[3a_l]}`$, so $`D_l^{[7a_l]}=H_l^{[10a_l]}=G_l\subset H_{l+1}`$. Since $`l+1\le k_0`$, $`D_{l+1}=H_{l+1}^{[3a_{l+1}]}`$. Hence $`D_l^{[7a_l+3a_{l+1}]}\subset H_{l+1}^{[3a_{l+1}]}=D_{l+1}`$.

(c) $`l=k_0`$. Since $`h<k_0`$, $`D_{k_0}=H_{k_0}^{[3a_{k_0}]}`$, and $`D_{k_0}^{[7a_{k_0}]}=G_{k_0}\subset H_{k_0+1}`$. By (H3), $`D_{k_0+1}=H_{k_0+1}^{[3u_t-w_{k_0+1}]}=H_{k_0+1}^{[u_t]}`$, since $`w_{k_0+1}=2u_t`$. Hence $`D_{k_0}^{[7a_{k_0}+u_t]}\subset D_{k_0+1}`$.

(d) $`l=k_0+1`$. Both $`D_{k_0+1}`$ and $`D_{k_0+2}`$ are enlargements of the one box $`H_{k_0+1}`$, by $`3u_t-w_{k_0+1}`$ and by $`3u_t-w_{k_0+2}`$. So $`D_{k_0+1}^{[w_{k_0+1}-w_{k_0+2}]}=D_{k_0+2}`$. If $`k_0+2=t`$, then $`w_t=0`$ and the gap is $`2u_t`$. Otherwise $`k_0+2<t`$, and

```math
w_{k_0+2}=\sum_{q=k_0+3}^{t}u_q=u_t\sum_{s=0}^{t-k_0-3}L^{-s}<u_t\,\frac{L}{L-1}.
```

So $`g_{k_0+1}=2u_t-w_{k_0+2}>u_t\big(2-\tfrac{L}{L-1}\big)=u_t\tfrac{L-2}{L-1}`$.

(e) $`k_0+2\le l<t`$. As in (d), $`D_l^{[w_l-w_{l+1}]}=D_{l+1}`$. If $`l+1<t`$, then $`w_l-w_{l+1}=u_{l+1}`$ by the sum formula. If $`l+1=t`$, then $`w_{t-1}=u_t`$ and $`w_t=0`$, so the difference is $`u_t=u_{l+1}`$.

The bound $`g_l\ge u_{l+1}`$. In (a), $`3a_{h+1}\ge u_{h+1}`$. In (b), $`7a_l+3a_{l+1}\ge a_{l+1}\ge u_{l+1}`$. In (c), $`7a_{k_0}+u_t\ge u_t\ge u_{k_0+1}`$, as $`k_0+1\le t`$. In (d), if $`k_0+2=t`$ the gap $`2u_t`$ exceeds $`u_{k_0+2}=u_t`$. Otherwise $`\tfrac{L-2}{L-1}\ge\tfrac1L`$, because this is $`L^2-3L+1\ge0`$, which holds for $`L\ge3`$. So $`g_{k_0+1}\ge u_t/L=u_{t-1}\ge u_{k_0+2}`$, as $`k_0+2\le t-1`$. In (e) there is equality. In each case we used $`a_i\ge u_i`$.

The inclusion $`D_l\subset D_{l+1}`$ follows from $`D_l\subset D_l^{[g_l]}\subset D_{l+1}`$.

The inclusion $`D_l\subset G_l`$. For $`l=h`$ it is an equality. For $`h<l\le k_0`$, $`H_l^{[3a_l]}\subset H_l^{[10a_l]}=G_l`$. For $`l>k_0`$: first, $`w_l\ge0`$, so $`D_l=H_{k_0+1}^{[3u_t-w_l]}\subset H_{k_0+1}^{[8u_t]}=H_{k_0+1}^{[8a_{k_0+1}]}=O_{k_0+1}`$. Next, for $`h<i<t`$, $`O_i=H_i^{[8a_i]}\subset H_i^{[10a_i]}=G_i\subset H_{i+1}\subset O_{i+1}`$. So $`D_l\subset O_{k_0+1}\subset O_l\subset G_l`$.

(f) $`D_i\subset O_i`$: for $`h<i\le k_0`$, $`3a_i\le8a_i`$; for $`i>k_0`$, this is the chain just shown. Next, $`O_{i+1}=H_{i+1}^{[8a_{i+1}]}\supset G_i^{[8a_{i+1}]}=H_i^{[10a_i+8a_{i+1}]}=O_i^{[2a_i+8a_{i+1}]}`$. Hence $`D_{j+1}^{[8a_{j+2}]}\subset O_{j+1}^{[8a_{j+2}]}\subset O_{j+2}`$.

(g) $`Z''_t(X)=H_{k_0+1}^{[3u_t]}`$, since $`w_t=0`$. Then $`Z''_t(X)^{[5u_t]}=H_{k_0+1}^{[8u_t]}=O_{k_0+1}\subset O_t`$ by the chain above. By (H2), $`X=G_t=H_t^{[10a_t]}=O_t^{[2a_t]}`$. So $`Z''_t(X)^{[5u_t+2a_t]}\subset X`$.

The consequence. All boxes above lie in the lift of $`X`$ (H6). The periodic distance is the minimum over translates. So the inclusion $`D_l^{[g_l]}\subset D_{l+1}`$ in the lift gives the same inclusion on the torus. $`D_{l+1}`$ is a union of $`M`$-cubes of level $`l+1`$: for $`l+1\le k_0`$ it is a union of level-$`(l+1)`$ cells (H3), and each such cell is a union of $`M`$-cubes of level $`l+1`$, because the partitions are nested (rule (S7)); for $`l+1>k_0`$ this is (H3). $`X`$ is a union of level-$`t`$ cells, so it is a union of $`M`$-cubes of level $`l+1`$ (rule (S7)). So $`X\setminus D_{l+1}`$ is a union of $`M`$-cubes of level $`l+1`$, none of them in $`D_{l+1}`$. Lemma 0, with $`\mathcal G`$ the $`M`$-cubes of level $`l+1`$, $`B=D_{l+1}`$, $`A=D_l`$ and $`g=g_l`$, gives $`d(D_l,X\setminus D_{l+1})\ge g_l\ge u_{l+1}`$. $`\square`$

Your lines 63821-63824 state the separations of (b) and (e): "$`Z''_i(X)`$ is separated from the exterior of $`Z''_{i+1}(X)`$ in $`X`$ by at least $`7a_i`$", and "For $`k_0<i<k`$, the separation is $`w_i-w_{i+1}`$."

### 5.6 The invariant

For a label at top level $`s`$ we write:

- (N) $`\Omega_{l+1}\subset\Lambda_l\subset\Omega_l`$ for $`0\le l<s`$, and $`\Lambda_s\subset\Omega_s`$;
- (G) $`d(Z_l,\Omega_{l+1})\ge u_{l+1}`$ for $`0\le l<s`$. For $`l=0`$ this reads $`d(\Omega_0^c,\Omega_1)\ge u_1`$.

Suppose that every entry of level $`i`$ is a union of $`M`$-cubes of level $`i`$, and that $`\Lambda_l\subset\Omega_l`$ and (G) hold. Then $`\Omega_{l+1}\subset\Lambda_l`$. Indeed, an $`M`$-cube of level $`l+1`$ in $`\Omega_{l+1}`$ is a union of $`M`$-cubes of level $`l`$ (rule (S7)). If it were not in $`\Lambda_l`$, one of these cubes would lie in $`Z_l`$, at distance $`0`$ from $`\Omega_{l+1}`$. This contradicts (G).

Iterating (N) gives $`Z_l\subset\Omega_t^c`$ for $`l<t\le s`$: $`Z_l=\Lambda_l^c\subset\Omega_{l+1}^c\subset\Lambda_{l+1}^c=Z_{l+1}\subset\cdots\subset Z_{t-1}\subset\Omega_t^c`$.

### 5.7 Lemma 4 (an operation: all fates, all stage counts)

**Lemma 4.** Let $`\mathcal L'`$ be a label at top level $`t`$, just after step $`t`$. Assume that $`\mathcal L'`$ satisfies (N) and (G), that every entry of $`\mathcal L'`$ of level $`i`$ is a union of $`M`$-cubes of level $`i`$, and that $`Z'_t\supset(\Omega_t'^c)^{\sim2}`$ (rule (S5), as in Lemma 1). Let $`X_1,\dots,X_r`$ be distinct components of $`Z'_t`$. Let each $`X=X_i`$ have a nest $`D_\cdot(X)`$ with the conclusions of Lemma 3, with $`D_h(X)=Z'_h\cap X`$ for $`h=t_\flat`$. Give each $`X`$ one outcome: healed, island, or *stopped after $`m(X)`$ stages*, with $`0\le m(X)\le\mathsf N_t`$. Let $`\mathcal L`$ be the label given by your rules (S9):

- nothing changes outside $`\bigcup_iX_i`$;
- healed: $`\Omega_l\cap X=\Lambda_l\cap X=X`$ for $`l\le t`$;
- island: the same for $`l<t`$ and for $`\Omega_t`$, and $`\Lambda_t\cap X=\Lambda'_t\cap X=\emptyset`$;
- stopped after $`m`$: $`\Omega_l\cap X=X\setminus D_l`$ for $`t_\flat<l\le t_\flat+m`$, and $`\Lambda_l\cap X=X\setminus D_l`$ for the same $`l`$ with $`l<t`$; all other entries are unchanged, so $`\Lambda_t\cap X=\emptyset`$.

Then $`\mathcal L`$ satisfies (N) and (G), and every entry of $`\mathcal L`$ of level $`i`$ is a union of $`M`$-cubes of level $`i`$.

"Stopped after $`m`$" is a drop-out with $`n=m`$, the label after $`m`$ stages, and for $`m=\mathsf N_t`$ the prepared sequence (lines 62080, 62107-62115, 62128). A component that the operation has not yet treated is stopped after $`0`$ stages.

*Proof.* The entries of $`\mathcal L`$ are unions of $`M`$-cubes of the level of the entry. Entries outside $`\bigcup X_i`$ are those of $`\mathcal L'`$. A healed or island filling adds $`X`$, a union of level-$`t`$ cells, hence of $`M`$-cubes of every level $`i\le t`$ (rule (S7)). A window entry is $`X\setminus D_i`$, and $`D_i`$ is a union of $`M`$-cubes of level $`i`$ (proof of Lemma 3).

Two facts.

(F1) $`Z_l\subset Z'_l`$ for every $`l\le t`$. A healed component empties $`Z_l\cap X`$ for $`l\le t`$. An island empties $`Z_l\cap X`$ for $`l<t`$, and leaves $`Z_t\cap X=X`$. A stop replaces $`Z'_l\cap X=G_l`$ by $`D_l\subset G_l`$ (Lemma 3) in its window, and leaves $`\Lambda_t\cap X=\emptyset`$, so $`Z_t\cap X=X`$.

(F2) An $`M`$-cube of level $`l+1`$ that lies in $`\Omega_{l+1}`$ and not in $`\Omega'_{l+1}`$ lies in some $`X_i`$. Indeed entries change only inside $`\bigcup X_i`$. Each $`X_i`$ is a union of level-$`t`$ cells. An $`M`$-cube of level $`l+1\le t`$ lies in one level-$`t`$ cell (rule (S7)). That cell is in one $`X_i`$ or in none.

*(N), the part $`\Lambda_l\subset\Omega_l`$.* Outside $`\bigcup X_i`$ it is (N) for $`\mathcal L'`$. In a healed $`X`$: $`X\subset X`$. In an island: $`X\subset X`$ for $`l<t`$, and $`\Lambda_t\cap X=\emptyset`$. In a stopped $`X`$: in the window the two entries are equal; $`\Lambda_t\cap X=\emptyset`$; elsewhere the old entries, which satisfy (N). The part $`\Omega_{l+1}\subset\Lambda_l`$ follows from (G), by section 5.6.

*(G).* Fix $`0\le l<t`$. Let $`c`$ be an $`M`$-cube of level $`l`$ with $`c\subset Z_l`$, and $`f`$ an $`M`$-cube of level $`l+1`$ with $`f\subset\Omega_{l+1}`$. Every entry of level $`i`$ is a union of $`M`$-cubes of level $`i`$, so these pairs $`(c,f)`$ exhaust $`Z_l\times\Omega_{l+1}`$, and $`\Omega'_{l+1}`$ is a union of cubes of the grid of $`f`$, as (F2) needs. We show $`d(c,f)\ge u_{l+1}`$.

1. $`f\subset\Omega'_{l+1}`$. By (F1), $`c\subset Z'_l`$. (G) for $`\mathcal L'`$ gives $`d(c,f)\ge u_{l+1}`$.
2. $`f\not\subset\Omega'_{l+1}`$. By (F2), $`f\subset X`$ for one $`X=X_i`$. By (F1) and (N) for $`\mathcal L'`$ (section 5.6), $`c\subset Z'_l\subset\Omega_t'^c`$. The grids are nested, so $`c`$ lies in one level-$`t`$ cell $`e`$. $`\Omega_t'^c`$ is a union of level-$`t`$ cells and meets the interior of $`e`$, so $`e\subset\Omega_t'^c\subset Z'_t`$. Let $`K_e`$ be the component of $`Z'_t`$ that contains $`e`$.
   - 2a. $`K_e\ne X`$. The cube $`f`$ lies in a level-$`t`$ cell of $`X`$, which is not in $`K_e`$. Lemma 1 gives $`d(e,X)\ge2a_t`$. So $`d(c,f)\ge2a_t\ge2u_t\ge u_{l+1}`$, as $`l+1\le t`$.
   - 2b. $`K_e=X`$. Then $`c\subset Z_l\cap X`$. If $`X`$ is healed or an island, $`Z_l\cap X=\emptyset`$ for $`l<t`$, which is impossible. If $`X`$ is stopped after $`m`$ stages: $`f`$ is new at level $`l+1`$, so $`t_\flat<l+1\le t_\flat+m`$ and $`f\subset X\setminus D_{l+1}`$. Also $`l\ge t_\flat`$. If $`l>t_\flat`$, then $`l`$ is in the window and $`l<t`$, so $`Z_l\cap X=D_l`$. If $`l=t_\flat`$, the operation does not change level $`l`$ in $`X`$, so $`Z_l\cap X=Z'_{t_\flat}\cap X=D_{t_\flat}`$. In both cases $`c\subset D_l`$, and Lemma 3 gives $`d(c,f)\ge u_{l+1}`$.

The pair $`l=0`$. Put $`Z_0=\Omega_0^c`$ and $`\Lambda_0=\Omega_0`$. By reading (R2), a healed component or an island $`X`$ fills $`\Omega_0`$, so $`Z_0\cap X=\emptyset`$ and (F1) holds at $`l=0`$. A stop never changes the levels $`0`$ and $`1`$, since $`t_\flat\ge1`$. So the same cases apply.

No case subtracts a margin. Each new pair receives either the padding $`2a_t`$ of Lemma 1 or the box gap of Lemma 3. $`\square`$

### 5.8 Lemma 5 (stopping vectors)

**Lemma 5.** Let $`h`$ be a history, and $`\boldsymbol\nu`$ a stopping vector on the drop-outs standing in $`h`$, with $`0\le\boldsymbol\nu(X)\le n(X)`$. Let $`\mathcal L^{\boldsymbol\nu}(h)`$ be the label given by rules (S10) and (S11). $`\mathcal L(h)=\mathcal L^{n}(h)`$ is the determining label. Then:

- (a) The top region $`Z_s`$ of $`\mathcal L^{\boldsymbol\nu}(h)`$ does not depend on $`\boldsymbol\nu`$. Just after a step $`t`$, the entries $`\Omega_t,\Lambda_t`$ do not depend on $`\boldsymbol\nu`$ either. If $`h`$ ends with step $`t`$ and the determining label of $`h`$ satisfies (N), then, inside a class component $`X`$ of level $`t`$, the entries of $`\mathcal L^{\boldsymbol\nu}(h)`$ at levels $`\ge t_\flat`$ do not depend on $`\boldsymbol\nu`$.
- (b) If $`h=(h',\text{step }t)`$, then $`\mathcal L^{\boldsymbol\nu}(h)`$ is $`\mathcal L^{\boldsymbol\nu}(h')`$ followed by step $`t`$, with the recorded new entries $`\Omega_t,\Lambda_t`$ of $`h`$.
- (c) If $`h=(h',\text{operation }t)`$ and (a) holds for $`h'`$, then $`\mathcal L^{\boldsymbol\nu}(h)`$ is obtained from $`\mathcal L^{\boldsymbol\nu'}(h')`$ by the rules of Lemma 4, with the same components, fates and nests, and with stage count $`\boldsymbol\nu(X)`$ on each new drop-out $`X`$. Here $`\boldsymbol\nu'`$ is any extension of $`\boldsymbol\nu`$ to the marks of $`h'`$.

*Proof.* A standing drop-out $`X_o`$ of level $`s`$ changes entries only at cubes of $`X_o`$ and at levels in $`(s_\flat,s]`$ (rules (S9), (S10), (S11)). Its entry $`\Lambda_s\cap X_o`$ is empty for every $`\boldsymbol\nu`$ (H5).

(a) First claim. A mark of level $`s`$ changes $`\Lambda`$ only at levels $`<s`$, and it has $`\Lambda_s\cap X_o=\emptyset`$ for every $`\boldsymbol\nu`$. So the top region is fixed. (The entry $`\Omega_s\cap X_o`$ does depend on $`\boldsymbol\nu`$ when $`n=\mathsf N_s`$ and $`s`$ is the top level. The proof below never uses that entry as an input: step $`s+1`$ reads only $`Z_s`$, as your lines 62140-62142 say: "the recursion uses the recorded step data and the top stored region from level $`s-1`$. Changing the stage index leaves that region fixed.") Just after step $`t`$, every mark has level $`<t`$, so the entries of level $`t`$ are untouched.

Second claim. Let $`X_o`$ be a standing mark of level $`s`$ that meets $`X`$. Then $`X_o\subset Z_s`$ (rules (S9), (H5)). By (N) for the determining label, iterated as in section 5.6, $`Z_s\subset Z_t`$. $`X_o`$ is connected and meets the component $`X`$ of $`Z_t`$, so $`X_o\subset X`$. Marks wait (H4): $`s<t_\flat`$. So all levels at which $`X_o`$ acts are $`\le s<t_\flat`$.

(b) A step copies the earlier entries and the standing marks (rule (S12)) and adds top entries. No mark touches the top entries, by (a).

(c) Compare the entries cube by cube.

- Outside the class components, nothing changes, and the same marks stand.
- In a healed component, every entry of level $`l\le t`$ is $`X`$ in both labels. The same holds in an island for $`l<t`$ and for $`\Omega_t`$. The swallowed marks cease to stand (rule (S12)). The entry $`\Lambda_t`$ of an island is a top entry and is the same in both labels.
- In a new drop-out $`X`$, at a level $`l\in(t_\flat,t]`$: by (a), no older mark acts there. So $`\mathcal L^{\boldsymbol\nu}(h)`$ has $`X\setminus Z''_l(X)`$ for $`l\le t_\flat+\boldsymbol\nu(X)`$, and above that level it has $`\Omega^\circ_l=\Omega_l(\mathcal S'_t)\cap X`$, which by (a) equals $`\Omega^{\boldsymbol\nu'}_l(h')\cap X`$. The same holds for $`\Lambda_l`$ with $`l<t`$ (rule (S11)), and $`\Lambda_t\cap X=\emptyset`$. This is the rule of Lemma 4 with $`m=\boldsymbol\nu(X)`$.
- In a new drop-out $`X`$, at levels $`\le t_\flat`$: the operation changes nothing, and both labels apply the same older marks to the same entries.

$`\square`$

The comparison in (b) and (c) is the one that your lines 62174-62180 state (rule (S12)).

### 5.9 Theorem 6 (your display, and the nesting)

**Theorem 6.** Assume your rules (S1)-(S15), the statements (H1)-(H6), and the readings (R1) and (R2). Assume $`L\ge3`$ odd, every $`\check R_i`$ a power of $`L`$ with $`\check R_i\ge1`$, and the torus admissible (rule (S14)). Let $`h`$ be any history, at any moment: just after a step; during the operation of the top level $`t`$, with any outcome and any stage count $`0\le m(X)\le\mathsf N_t`$ for each class component; or after that operation. Let $`\boldsymbol\nu`$ be any stopping vector on the drop-outs standing in $`h`$. Then the label $`\mathcal L^{\boldsymbol\nu}(h)`$, with top level $`s`$, satisfies (N) and (G), each of its entries of level $`i`$ is a union of $`M`$-cubes of level $`i`$, and, for $`1\le j<s`$,

```math
\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM,\qquad \Omega_{j+1}\subset\Lambda_j^{\sim-1},\qquad Z_j^\sim\cap\Omega_{j+2}=\emptyset\quad(j+2\le s),
```

in level-$`j`$ units, with layers of $`M`$-cubes of level $`j`$. Here $`Z_j^\sim:=Z_j^{[u_j]}`$ and $`\Lambda_j^{\sim-1}:=(Z_j^\sim)^c`$. Also $`d(\Omega_0^c,\Omega_1)\ge u_1`$, and $`T_\ell\supset\Omega_0\supset\Omega_1\supset\Lambda_1\supset\cdots\supset\Lambda_s`$.

*Proof.* Induction on the number of moves of $`h`$, for all $`\boldsymbol\nu`$ at once. A component that the operation has not yet treated counts as stopped after $`0`$ stages, so a moment during an operation is covered by the operation case.

*Base: after step 1.* There are no marks. Lemma 2 with $`t=1`$ gives $`\Lambda_1\subset\Omega_1`$ and $`d(\Omega_0^c,\Omega_1)\ge u_1`$. $`\Omega_1\subset\Omega_0=\Lambda_0`$ by rule (S1). The entries are unions of level-$`1`$ cells, hence of $`M`$-cubes of levels $`0`$ and $`1`$ (rule (S7)).

*Step $`t\ge2`$.* By Lemma 5 (b), $`\mathcal L^{\boldsymbol\nu}(h)`$ is $`\mathcal L^{\boldsymbol\nu}(h')`$, which satisfies (N), (G) by induction, extended by the new top entries. By Lemma 5 (a), $`Z_{t-1}`$ is the same set as in the determining label. Lemma 2 gives $`\Lambda_t\subset\Omega_t`$ and $`d(Z_{t-1},\Omega_t)\ge u_t`$. This is (G) at the new pair $`(t-1,t)`$, and with section 5.6 it gives (N) at the new top. The new entries are unions of level-$`t`$ cells (rules (S3)-(S5)), hence of $`M`$-cubes of level $`t`$.

*Operation $`t`$, including partial stages.* By Lemma 5 (c), $`\mathcal L^{\boldsymbol\nu}(h)`$ comes from $`\mathcal L'=\mathcal L^{\boldsymbol\nu'}(h')`$ by the rules of Lemma 4. We check the hypotheses of Lemma 4.

- (N), (G) and the cube property for $`\mathcal L'`$: by induction.
- $`Z'_t\supset(\Omega_t'^c)^{\sim2}`$: the top entries do not depend on $`\boldsymbol\nu`$ (Lemma 5 (a)), and $`\mathcal L'`$ is the label just after step $`t`$; so this is Lemma 1, first paragraph.
- The class components are distinct components of $`Z'_t`$ (rule (S8)).
- Their nests have the conclusions of Lemma 3. Lemma 3 is about the determining label $`\mathcal S'_t`$. Inside $`X`$, the entries at levels $`\ge t_\flat`$, and so the sets $`G_i`$ for $`i\ge t_\flat`$, are the same in $`\mathcal L'`$ as in the determining label (Lemma 5 (a), which uses (N) for the determining label of $`h'`$, an induction hypothesis). So $`D_h(X)=Z'_h\cap X`$ in $`\mathcal L'`$ too.

Order. Your derivation of (H2) at level $`t`$ (lines 63714-63766) uses the nesting (N), and the fact that earlier operations only shrink each $`Z_i`$ (which is (F1) of Lemma 4), only for the determining labels of the moves before the operation of level $`t`$. These are induction hypotheses here. So (H2) at level $`t`$ is available at this move. The induction is joint: (N) and (G) for all moves up to step $`t`$; then (H2) at level $`t`$; then Lemma 3; then Lemma 4.

Lemma 4 now gives that $`\mathcal L^{\boldsymbol\nu}(h)`$ satisfies (N), (G) and the cube property.

*The display.* Let $`1\le j<s`$.

- The gap. (G) gives $`d(Z_j,\Omega_{j+1})\ge u_{j+1}`$, and $`u_{j+1}`$ is $`LM`$ in level-$`j`$ units.
- The first inclusion. $`\Omega_{j+1}`$ is a union of $`M`$-cubes of level $`j+1`$, hence of level $`j`$ (rule (S7)). Let $`q`$ be such a cube of level $`j`$. If $`q\subset Z_j^{[u_j]}`$, then $`d(Z_j,q)\le u_j<u_{j+1}`$, which contradicts (G). So $`q\subset(Z_j^\sim)^c=\Lambda_j^{\sim-1}`$.
- The second relation. By (N), $`\Omega_{j+2}\subset\Lambda_{j+1}\subset\Omega_{j+1}`$. So $`d(Z_j^{[u_j]},\Omega_{j+2})\ge d(Z_j,\Omega_{j+1})-u_j\ge u_{j+1}-u_j>0`$. The two sets do not meet, even as point sets.

The pair $`(0,1)`$ is (G) at $`l=0`$. The chain $`\Omega_0\supset\Omega_1\supset\Lambda_1\supset\cdots\supset\Lambda_s`$ is (N). $`T_\ell`$ is the whole torus (rule (S14)), so $`T_\ell\supset\Omega_0`$. $`\square`$

**Remark.** Your lines 62089-62094 say that the gap is attained at the active indices $`k_0(t)+2\le j<t`$ of a prepared nest, and is $`w_j-w_{j+1}`$ at $`j=k_0(t)+1`$. Lemma 3 (d) and (e) give the same values for the gaps between consecutive prepared boxes. The proof above uses only the lower bound.

## 6. The constants used

The proof uses these constants and conditions, and no others:

- $`L\ge3`$ and $`L`$ odd. Your line 650 takes $`L\ge13`$ odd. The bound $`L\ge3`$ is used once, in Lemma 3 (d), as $`L^2-3L+1\ge0`$. Oddness is used for the alignment of the prepared boxes (H3), lines 63805-63809.
- Each $`\check R_i`$ is a power of $`L`$ with $`\check R_i\ge1`$. Being a power of $`L`$ is your rule (S7), line 62001; it makes the partitions nested. The bound $`\check R_i\ge1`$ gives $`a_i\ge u_i`$, used in Lemmas 1, 2 and 3. Your text does not state $`\check R_i\ge1`$ in one line. It follows from your lines as follows. $`\check R_k`$ is the smallest power of $`L`$ not less than $`(\log\min_{i\le k}x_i)^r`$ (line 62001). $`g_j=x_j^{-1/2}`$ (line 83084), and $`g_j\le\gamma`$ (line 61911). If $`\gamma<e^{-1/2}`$, as in your definition of a frame at lines 1102-1103, then $`x_i\ge\gamma^{-2}>e`$, so $`(\log\min_{i\le k}x_i)^r>1`$ and $`\check R_k\ge1`$. We state $`\check R_i\ge1`$ as a hypothesis of Theorem 6 so that the proof does not depend on which $`\gamma`$ line 61911 means.
- The torus floor: the torus is admissible (rule (S14)), $`\ell L^{K-j}\ge2L^{11}M\check R_j`$ (line 61911), so that no cell, box or neighbourhood of a box wraps (line 63692). It is used through Lemma 0 and (H6), and for the lift of a class component in Lemma 3.

No other constant is used. $`M`$ enters only through the units $`u_i=ML^i`$ and $`a_i=M\check R_iL^i`$; no inequality on $`M`$ is used. The proof uses neither of your two constants named $`\rho`$, nor $`R_1`$, $`M_1'`$, $`\mathfrak M`$, nor your inequalities $`R_1\ge L`$, $`M_1'\ge R_1\mathfrak M`$, $`M\ge L^4M_1'`$ (lines 650-652).

## 7. What this note does not show

- It does not prove the statements (H1)-(H6). They are taken from your text as stated: the layer convention, the quiet boxes, the prepared boxes and the existence of the index $`k_0`$ with $`h<k_0\le k-2`$, "marks wait", and the rule that a standing drop-out stays outside its top entry. The proof of Theorem 6 uses them in the order stated there.
- It does not decide the readings (R1) and (R2). Only (R2) matters, and only for the pair $`(0,1)`$, which your display does not contain.
- It does not treat the other sentences of your proposition: the gaps of at least $`cM\check R_j`$ for the regions that the steps produce (Lemma 2 gives $`8a_t`$ only at the moment of the step); "Every large-field region and every creation set is a union of cells of its own level"; the decomposition of unity and the two kinds of creation; and the identity $`\Omega^{\boldsymbol\nu_\mu}_l(\mathcal S_t)=\Omega_l(\mathcal S^\mu)\cup Z_{[j,t]}`$ of lines 62130-62133.
- It does not prove the equality of the Remark after Theorem 6 as a statement about your labels; it uses only the lower bound.
- No step uses a computation. Each step is a finite inclusion or distance argument between unions of grid cubes, so that a proof assistant can take it.
