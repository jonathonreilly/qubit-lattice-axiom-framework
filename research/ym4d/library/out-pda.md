# Geometric admissibility after one prepared large-field operation

This note proves **old (A1) implies prepared (A1)** for one large-field operation, including every componentwise stopped prefix.
It gives an explicit choice (C) for the intermediate sets in your `4.14:prop-prepared-data-admissible`.
All account references below refer to commit `31a47c543775`. CA-I denotes your complete account, volume I.

**Old-label premise.** The label before the operation must satisfy (A1).
Your proposition leaves this inductive premise implicit. Balaban's representation, CMP 119, (2.18), as your account cites it, sums over admissible sequences. Your later assertion about the produced nests concerns the whole history.
This note assumes admission of the old label. It proves admission after one operation.
See [CA-I 4224–4226](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4224-L4226) and [CA-I 45557–45634](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45557-L45634).

**The second endpoint.** Put $`s=k-N_0+1`$.
Your [CA-I 51712](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L51712) says that the two members defined in Balaban's (1.10) are $`Z''_k`$ and $`Z''_{k-1}`$. Your [CA-I 45600](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45600) and the quotation at [CA-I 92015](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92015) name $`Z''_k`$ and $`Z''_s`$. Your quotation of Balaban's (1.10) at CA-I 92015 defines $`Z''_{k-N_0+1}`$. The construction below uses $`Z''_s`$ as the second endpoint. The two readings agree only when $`N_0=2`$. If (1.10) defines exactly the two end members, 51712 would read: "The two end members $`Z''_k`$ and $`Z''_{k-N_0+1}`$ are defined in (1.10)." CMP 122a was not available to check whether (1.10) also defines $`Z''_{k-1}`$.
For each operated component $`X`$, the endpoints are

```math
Z''_k\cap X=X\setminus\Omega_s^{(+5M)},\qquad
Z''_s\cap X=X\setminus\Omega_s^{(+7M)}. \tag{E}
```

The first formula appears at [CA-I 48781–48783](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48781-L48783) and [CA-I 53774–53782](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53774-L53782).
The second is your quotation of Balaban's (1.10) at [CA-I 92012–92016](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92012-L92016).
The index $`k-1`$ of that reading and the index $`s`$ in (E) coincide only when $`N_0=2`$. Adoption of this proof requires the $`s`$-endpoint reading.

**Limits.** This is one operation step. It does not prove (A2), admission of all produced nests, or the initial old-label premise.
In particular, it does not prove the next domain's $`6M`$ margin or its level-$`k`$ $`LM`$-cube partition.
Your text keeps (A2) separate at [CA-I 45589–45591 and 45622–45624](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45589-L45624).
The analytic supply conditions at [CA-I 49495–49546](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L49495-L49546) also remain outside this proof.
Your account also cites CMP 122a, pp. 178–179, for other content at CA-II 145579 and CA-III 21303, 53328, 111073 and 111311, for example constant conditions and a point count. This note does not cover those uses.
No gauge bound, field-domain inclusion, holomorphic extension, or operator theorem follows here.

**Retained geometry.** We retain your compatible grids, cell geometry above the unchanged levels, and ten-layer margin.
We also retain your agreement of metric and cell-layer enlargements, and the endpoints (E).
These are account inputs, not conclusions of this note. They are stated precisely below.
Your account reads the cell and alignment inputs from Balaban's text and does not prove them ([CA-I 53816–53831](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53816-L53831), [48164–48168](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48164-L48168), [92012](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92012)). The same holds for the endpoint quotation at [92015](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92015). This note does not prove them either.
The eight-layer collar estimate is already proved in your account from Tadeusz Balaban's CMP 119, (3.5).
We reuse that argument. Balaban's CMP 122a, pp. 178–179, supplies the prepared construction through your quotations.
CMP 122a was not available to the checker. Neither this version nor the model reading of its proof independently inspects that paper.

## Data and statement

Measure lengths in level-$`k`$ units. Write

```math
\ell_i=L^{i-k},\qquad m_i=M\ell_i,\qquad
\sigma_i=MR_i\ell_i,\qquad h=k-N_k,\qquad s=k-N_0+1.
```

Each $`R_i`$ is a nonnegative integer power of $`L`$. The operation regime has $`k>N_k>N_0`$ and $`R_k>1`$.
Retain your floors, including odd $`L\ge8`$, and your order of choice.
See [CA-I 45669–45687](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45669-L45687) and [CA-I 45803–45863](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45803-L45863).
Your scale argument gives

```math
1\le h<s-1,\qquad s\le k-1,\qquad
\sigma_s=M,\qquad \sigma_i\le M\ (i\le s),\qquad
\sigma_i\le\sigma_{i+1},\qquad \sigma_k\ge LM. \tag{1}
```

Indeed, $`R_i\le(L+1)R_{i+1}`$ and power-of-$`L`$ quantization give $`R_i/R_{i+1}\le L`$.
Thus $`\sigma_i\le\sigma_{i+1}`$, with every increasing ratio a nonnegative power of $`L`$.
The definition of $`N_0`$ gives $`\sigma_s=M`$; the other bounds follow from the operation regime.
These are your conventions and their proof at [CA-I 48141–48261](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48141-L48261).

All cube partitions belong to one compatible $`L`$-adic family.
All sets are regular closed carriers. Complements and differences below mean their regularized versions.
For a set $`A`$, let $`A^{(+r)}=\{x:d_\infty(x,A)\le r\}`$.
Use the periodic maximum-norm distance when working on a torus.
These conventions are those of [CA-I 45236–45281](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45236-L45281) and [CA-I 48149–48168](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48149-L48168).

Assume the old label has

```math
\Omega_i\supset\Lambda_i^{119}\supset\Omega_{i+1}\quad(1\le i<k),\qquad
\Omega_k\supset\Lambda_k^{119},\qquad
Z_i=(\Lambda_i^{119})^c\quad(1\le i\le k).
```

The superscript distinguishes the small-field regions of CMP 119 from your operator layers.
This is the label in force at [CA-I 53755–53763](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53755-L53763).
Assume old (A1):

```math
\Omega_0\supset\Omega_1\supset\cdots\supset\Omega_k,\qquad
d_\infty(\Omega_i^c,\Omega_{i+1})\ge m_i\quad(1\le i<k). \tag{2}
```

Each $`\Omega_i`$, $`i\ge1`$, is a union of closed $`m_i`$-cubes from the compatible partitions.
Also, $`\Omega_0`$ is the prescribed Dirichlet hull of $`\Omega_1`$.
These are exactly the four clauses of your (A1).

Let $`X`$ be any component operated on at level $`k`$.
Retain the following geometric inputs on every such component.

- $`Z_k`$ is a union of aligned $`\sigma_k`$-cubes. Each $`X`$ is a connected component of that union.
  For $`h<i\le s`$, the old carrier $`\overline{\Omega_i^c}\cap X`$ is made of $`\sigma_i`$-cubes.
  The enlargements read inside $`X`$ agree with the metric enlargements by $`n\sigma_i`$.
  These are the cell and alignment readings at [CA-I 53816–53831](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53816-L53831), [CA-I 48164–48168](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48164-L48168), and [CA-I 92012](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92012).
- The old step geometry gives
  $`d_\infty(Z_i\cap X,\Omega_{i+1}\cap X)\ge8\sigma_{i+1} \quad(h\le i<k). \qquad(3)`$
  Your proof of `4.4:lem-collar-avoidance(b)` gives this from Balaban's CMP 119, (3.5).
  The complement of $`B^{i+1}(P^1_{i+1})`$ contains five layers around $`Z'_i\supset Z_i`$.
  Formula (3.5) adds three more layers.
  Each layer has side $`LMR_{i+1}`$ in level-$`i`$ units, hence side $`\sigma_{i+1}`$ here.
  See [CA-I 12181–12225](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L12181-L12225).
  Only this eight-layer consequence enters; the other conclusions of the collar lemma are not needed.
- The top margin contains the open $`10\sigma_k`$-neighbourhood of $`Z_{k-1}`$ in $`Z_k`$:
  $`\{x:d_\infty(x,Z_{k-1})<10\sigma_k\}\subset Z_k. \qquad(4)`$
  This is the ten-layer input at [CA-I 53820–53825](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53820-L53825).

No cell alignment is assumed for the unchanged members at levels $`i\le h`$.
In particular, the extra hypothesis (G) at [CA-I 53836–53838](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53836-L53838) is not used.

Write $`D_i=Z''_i\cap X`$ for $`i>h`$.
Choose the upper members explicitly by

```math
\begin{gathered}
a_k=5M,\qquad
a_i=5M+\sum_{r=i+1}^{k}m_r\quad(s<i<k),\qquad a_s=7M,\\
D_i=X\setminus\Omega_s^{(+a_i)}\quad(s\le i\le k).
\end{gathered} \tag{C}
```

For the lower members, use the prescribed formula

```math
D_i=X\setminus\Omega_i^{(+5\sigma_i)}\quad(h<i<s). \tag{5}
```

This is [CA-I 51718–51727](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L51718-L51727).
Formula (C) leaves both endpoints (E) fixed.
It makes the intermediate choice requested at [CA-I 45608–45611](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45608-L45611).
We read “separated by one layer” as **at least one layer**.
Exact equality at every junction cannot generally span the prescribed difference $`7M-5M=2M`$.
The sum of all later-level cube sides is less than $`ML/(L-1)<2M`$.

On each operated component set $`\Omega''_i\cap X=X\setminus D_i`$ for $`i>h`$.
Elsewhere keep $`\Omega''_i=\Omega_i`$, and keep all members at $`i\le h`$ unchanged.
These are your replacement rules at [CA-I 48779–48800](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48779-L48800).

**Claim.** These domains satisfy (A1), with $`\Omega''_0=\Omega_0`$.
The claim also holds when each component stops at any prefix $`p(X)\in\{h,\ldots,k\}`$.
For that version, replace only the members with $`h<i\le p(X)`$.
No new constant or coupling ceiling is required.

## Proof

**Grid operations and component boundaries.** Suppose a set is a union of aligned cubes of side $`q`$, where $`q/p`$ is an integer.
Subdivide into $`p`$-cubes. Enlargement by an integer multiple $`r`$ of $`p`$ preserves this grid.
Indeed, it replaces each coordinate interval $`[b,b+p]`$ by $`[b-r,b+p+r]`$, whose endpoints remain on the grid.
Regularized complementation gives the same conclusion for erosion.
Unions, intersections, and regularized differences also preserve a common grid.
On a torus, apply the argument to periodic lifts and project back.

Distinct components of $`Z_k`$ have distance at least $`\sigma_k`$.
Touching closed cubes belong to the same component, even at a corner.
Thus cubes from different components have an index difference at least two in some coordinate.
Their coordinate gap is at least $`\sigma_k`$. The periodic version follows from the same argument on lifts.

For $`i<k`$, put $`E_i=\overline{\Omega_i^c}\cap X`$.
Old nesting gives $`E_i\subset\overline{Z_{k-1}}\cap X`$.
By (4), the open ball of radius $`10\sigma_k`$ about any point of $`E_i`$ lies in $`Z_k`$.
The ball is connected and meets $`X`$, so it lies in that component. Hence

```math
d_\infty(E_i,X^c)\ge10\sigma_k. \tag{6}
```

The same reasoning applies to $`Z_i\cap X`$ for $`i<k`$.
Consequently (3) holds with the full $`\Omega_{i+1}`$, not just its trace in $`X`$.
Points outside $`X`$ are at distance at least $`10\sigma_k\ge8\sigma_{i+1}`$.

For $`h<i\le s`$, $`E_i`$ uses the $`\sigma_i`$-grid by the retained alignment.
The component uses a compatible coarser grid, since $`\sigma_k/\sigma_i`$ is a nonnegative power of $`L`$.
If $`r<10\sigma_k`$, erosion of $`E_i`$ in the whole lattice equals $`X\setminus\Omega_i^{(+r)}`$, after regularization.
To verify this, the complement of $`E_i`$ consists of the old small-field carrier and the outside of $`X`$.
Equation (6) prevents the outside from contributing at radius $`r`$.
Thus the component boundary introduces no additional cut.
This permits local cell alignment even when older thin layers occur elsewhere.

**Upper interpolation.** For $`s<i<k`$, $`a_i`$ is a multiple of $`m_{i+1}`$, hence of $`m_i`$.
Every term $`m_r/m_{i+1}=L^{r-i-1}`$ in its sum is an integer.
Both endpoints $`5M,7M`$ are multiples of every finer $`m_i`$.
Also, $`a_i\le7M<10\sigma_k`$, by the finite-sum bound below.
Since $`E_s`$ uses the $`M`$-grid, the grid argument makes every upper $`D_i`$ a union of $`m_i`$-cubes.
It also makes $`D_{i-1}`$ a union of $`m_i`$-cubes for $`s<i\le k`$.
Thus each shell $`D_i\setminus D_{i-1}`$ has that grid too.
This agrees with your shell description at [CA-I 121772–121777](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L121772-L121777).

For $`s<i<k`$, formula (C) gives $`a_i-a_{i+1}=m_{i+1}`$.
If $`s=k-1`$, the remaining difference is $`2M\ge m_k`$.
Otherwise,

```math
\begin{aligned}
a_s-a_{s+1}
&=2M-\sum_{r=s+2}^{k}m_r\\
&\ge2M-\frac{LM}{L-1}
=\frac{L-2}{L-1}M
\ge\frac M2\ge m_{s+1}.
\end{aligned} \tag{7}
```

The last bound uses $`s+1\le k-1`$ and $`L\ge3`$.
For the sum bound, multiply the finite sum $`1+L^{-1}+\cdots+L^{-n}`$ by $`1-L^{-1}`$.
The product is $`1-L^{-n-1}\le1`$. This also proves $`a_i\le7M`$.

Distance to a nonempty set is 1-Lipschitz, by the triangle inequality in both directions.
For $`x\in D_i`$ and $`y\in X\setminus D_{i+1}`$, the closed-carrier conventions give

```math
d_\infty(x,\Omega_s)\ge a_i,\qquad
d_\infty(y,\Omega_s)\le a_{i+1}.
```

Therefore

```math
D_i\subset D_{i+1},\qquad
d_\infty(D_i,X\setminus D_{i+1})\ge m_{i+1}
\quad(s\le i<k). \tag{8}
```

If a set in a distance is empty, its distance is $`+\infty`$.
If $`\Omega_s`$ is empty, every upper $`D_i=X`$, and (8) follows directly.
Finally, $`D_i\subset\Omega_s^c\cap X\subset\Omega_i^c\cap X`$.
Thus each upper replacement enlarges the old small-field domain.

**Lower members and the two junctions.** For $`h<i<s`$, (5) erodes $`E_i`$ by $`5\sigma_i<10\sigma_k`$.
It therefore makes $`D_i`$ a union of $`\sigma_i`$-cubes, hence of $`m_i`$-cubes.
It also gives $`D_i\subset\Omega_i^c\cap X\subset Z_i\cap X`$.

Fix $`h\le i<s-1`$.
At $`i=h`$, take $`x\in\Omega_h^c\cap X`$; otherwise take $`x\in D_i`$.
In either case $`x\in Z_i\cap X`$.
A point $`y`$ of the next prepared small-field domain inside $`X`$ lies in $`\Omega_{i+1}^{(+5\sigma_{i+1})}`$.
Use (3) in its full-domain form and the triangle inequality to obtain

```math
|x-y|_\infty\ge(8-5)\sigma_{i+1}
=3\sigma_{i+1}\ge m_{i+1}. \tag{9}
```

One may take a closest point in $`\Omega_{i+1}`$, or a sequence approaching the defining distance.
If that domain is empty, there is no such $`y`$.
This proves the unchanged-to-prepared junction without any cell alignment at level $`h`$.

At $`i=s-1`$, the next domain instead uses the seven-layer endpoint.
Since $`\sigma_s=M`$, the same argument gives

```math
|x-y|_\infty\ge(8-7)M=M\ge m_s. \tag{10}
```

This proves the lower-to-upper junction, including the case $`h=s-2`$.
Equations (8)–(10) give all within-component gaps and nesting.
Equation (9) also holds for every $`x\in Z_h\cap X`$; thus $`Z_h\cap X\subset D_{h+1}`$.

**Global gluing.** Glue the replacements on any union of operated components, retaining the old domains elsewhere.
Every component uses $`\sigma_k`$-cubes, which subdivide into every $`m_i`$-grid used here.
The old domains and the new pieces therefore give compatible closed $`m_i`$-cube unions globally.
The local inclusions just proved give

```math
\Omega_i\subset\Omega''_i\quad(1\le i\le k). \tag{11}
```

Fix $`1\le i<k`$, $`x\in(\Omega''_i)^c`$, and $`y\in\Omega''_{i+1}`$.
There are three cases.

1. If $`y\in\Omega_{i+1}`$, (11) puts $`x\in\Omega_i^c`$.
   Old (A1) gives $`|x-y|_\infty\ge m_i`$.
2. Otherwise $`y`$ is newly added in an operated component $`X`$.
   If $`x\in X`$, (8), (9), or (10) gives $`|x-y|_\infty\ge m_{i+1}\ge m_i`$.
3. If $`x\notin X`$, old nesting and (11) give $`x\in\Omega_i^c\subset Z_i\subset Z_k`$.
   It lies in another component. The component gap gives $`|x-y|_\infty\ge\sigma_k\ge M\ge m_i`$.

The cases cover unoperated components and multiple operated components.
Taking closures includes boundary faces. Therefore

```math
d_\infty((\Omega''_i)^c,\Omega''_{i+1})\ge m_i\quad(1\le i<k). \tag{12}
```

Its positive lower bound also proves $`\Omega''_{i+1}\subset\Omega''_i`$.
If the old gap is $`m_{i+1}`$, the proof preserves that stronger gap.
Use it in case 1; cases 2 and 3 already give it.

Since $`h\ge1`$, we have $`\Omega''_1=\Omega_1`$.
Keep its old Dirichlet hull as $`\Omega''_0`$.
This proves all four clauses of (A1).

**Componentwise stopped prefixes.** Choose each $`p(X)`$ independently in $`\{h,\ldots,k\}`$.
Replace only the levels $`h<i\le p(X)`$ inside $`X`$.
The grid argument and (11) remain valid.
Whenever $`y`$ is newly added at level $`i+1`$, that component was also prepared at level $`i`$, unless $`i=h`$.
Thus cases 2 and 3 above still apply, with (9) covering $`i=h`$.
At a stop $`i=p(X)<k`$, the next member inside $`X`$ is old, so case 1 applies there.
A newly added point in another component still falls under cases 2 or 3 for that component.
Hence (12), nesting, partitions, and the unchanged Dirichlet hull hold for every prefix assignment.
These are the stage and componentwise nests at [CA-I 48507–48523](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48507-L48523) and [CA-I 48759–48770](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48759-L48770). $`\square`$

## Who wrote and read this

Codex wrote the proof and this note. Claude (Opus 5.5) read the proof and this note line by line, and its repairs are applied. CMP 122a was not available to the checker, who used your quotations and definitions.
These are model readings of research text, not human review or an audit. They grant no scientific status.
