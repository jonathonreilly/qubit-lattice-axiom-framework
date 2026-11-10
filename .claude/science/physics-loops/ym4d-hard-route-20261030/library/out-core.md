lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T02:53Z

# A proposed proof of your `prop:large-field-2-3`

Provenance: written by Claude Opus 5.5; checked line by line by Claude Fable 5.2. Not an audit.

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

**(H3) Prepared boxes.** Lines 63776-63779: "let $`k_0+1`$ be the last index with $`a_{k_0+1}=u_k`$, with $`h<k_0\le k-2`$." Lines 63783-63784:

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

**(H6) No wrapping.** Line 63692: "no cell, no box and no neighbourhood of a box wraps around the torus." Lines 63770-63771: a class component has "at most $`100`$" cells along each side. We use this so that balls, boxes and their enlargements up to the sizes below are those of a lift to $`\mathbb R^4`$.

One remark on order. Your derivation of (H2) begins: "We use the nesting of \cref{prop:large-field-2-3} on these labels" (lines 63715-63716). It uses the nesting, and the fact that "the regions $`Z_i`$ decrease as these labels advance" (lines 63716-63720), only for the labels $`\mathcal S'_s`$, $`\mathcal S_s`$ with $`s<k`$ and for $`\mathcal S'_k`$ (lines 63714-63741). These are moments before the operation of level $`k`$. The proof of Theorem 6 uses (H2) at level $`k`$ only after it has proved the nesting for all those moments. So the use of (H2) is not circular.

## 4. Two readings

The proof uses two readings of your wording. Each is a reading, not a rule that your text states in these words.

**(R1) The live region of step $`t`$.** We read the live region $`Y=\mathcal Z_{t-1}`$ of step $`t`$ (rule (S2)) as $`Z_{t-1}(\mathcal S_{t-1})`$, the region $`Z_{t-1}`$ of the label after the operation of level $`t-1`$. Your text supports this reading. Line 1586: "let $`\mathcal Z_k(h)`$ be the live region after healing". Line 62106: for an island, "$`X\subset Z_t`$ remains". Line 62107: a drop-out "$`X`$ remains in $`Z_t`$". The proof uses only the inclusion $`Z_{t-1}\subset\widehat Y`$.

**(R2) Healing and islands at the entry $`l=0`$.** We read the fate rules "for $`l\le t`$" (line 62105) and "for $`l<t`$" (line 62106) as including the entry $`l=0`$, because "A label's sequence starts at $`\Omega_0`$" (line 61973). So a healed component or an island $`X`$ replaces $`\Omega_0`$ by $`\Omega_0\cup X`$.

(R2) matters for the pair $`(0,1)`$ only. Your display concerns $`j\ge1`$ and does not use it. If healing did not fill $`\Omega_0`$, the pair $`(0,1)`$ would have gap $`0`$ inside a healed component that meets $`\Omega_0^c`$.

A second reading gives the pair $`(0,1)`$ as well. Read line 61973 as a standing rule: $`\Omega_0`$ is $`\Omega_1^\sim`$ at every moment. Then after healing $`\Omega_0=(\Omega_1\cup X)^\sim\supset\Omega_0\cup X`$, and Lemma 0 gives $`d(\Omega_0^c,\Omega_1)\ge a_1`$ directly. Only the reading in which $`\Omega_0`$ is frozen at step $`1`$ and is not filled by healing breaks the pair $`(0,1)`$. We searched lines 61900-66000 for $`\Omega_0`$. It occurs at lines 61973, 62078, 62245, 63032, 63039 and 63374. None of these lines states the rule for $`\Omega_0`$ under healing.

