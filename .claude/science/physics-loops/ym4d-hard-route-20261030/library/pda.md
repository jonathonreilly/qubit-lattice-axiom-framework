# Admissibility of the prepared large-field data

Provenance: Codex (GPT-6), research at repository commit `c86830eb5a7d96960a21636d6f8168d434783ead`, 2026-11-05, on Proposition `4.14:prop-prepared-data-admissible` in the complete account of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, pinned upstream at `31a47c543775`; the account attributes the printed sentence to Balaban, CMP 122a, pp. 178–179. This note uses the account's quotation and definitions, not an independently inspected copy of CMP 122a. Research text only; no audit or retained status is granted.

## Scope and source identities

CA-I denotes [theorem_0_complete_account_raw_I.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) at the upstream revision above. SA denotes [YM4_sketch_500.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) there. Their local copies have SHA-256 values

- CA-I: `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.
- SA: `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`.

The proof target is **geometric** admission, not admission of fields to an analytic domain. CA-I:45557–45596 asserts (A1) for the prepared nest. It requires compatible closed level-\(j\) \(M\)-cube unions, a Dirichlet hull at level zero, and
\[
 \Omega''_{j+1}\subset\Omega''_j,\qquad
 \operatorname{dist}_\infty((\Omega''_j)^c,\Omega''_{j+1})
 \ge M\ell_j,\qquad \ell_j=L^{j-k},\quad 1\le j<k.       \tag{PDA}
\]
The separate condition (A2) concerns the next step's region \(\Omega_t\), its level-\(k\) \(LM\)-cube partition and its \(6M\) margin. The target's last sentence does not assert (A2). CA-I:45622–45624 explicitly keeps it separate. The operator theorem assumes both at CA-I:46044–46046. Its port retains this distinction in [P4](port/p4-operator.md), under **P4-H-prepared**.

The passage immediately after the target, CA-I:45598–45634, quotes Balaban's requested completion and asserts a stronger produced-nest margin. It does not prove either. There is no paragraph headed **Route** attached to this proposition in the pinned CA-I. The preceding Route, CA-I:45228–45234, concerns `4.13:lem-own-constant`; it is not a route for this proposition. Here the route is the quoted completion between the prescribed endpoints, followed by the five-layer formula and componentwise gluing.

## Comparison with the frozen texts

| Text | Exact relation to the target |
|---|---|
| [DOM](dom.md), definitions, Theorem 1, Result | Its RUN-low result supplies an existence bound for the stopping integer under its frame assumptions. Its remaining conclusions concern analytic rosters. It assumes the relevant geometry and does not construct this prepared nest. |
| [ST1](st1-r4.md), §1 (3), Theorem 14 | It starts with separated determining sequences and assumes GEO. Its separation uses \(M_1\)-cubes and \(\rho_0\), and its stage theorem concerns analytic substitution. Neither is the CA-I geometric statement for the specified \(\Omega''_j\). |
| [GEOH](geoh.md), Input P and Result | It assumes a nest selector and P-gap. It imports the upper prepared gaps and leaves the lower enlargement convention explicit. Thus its nesting and counting proofs cannot prove the missing existence of this selector. Its closed-endpoint quarantine rule is stronger than CA-I's rule; it will not be substituted here. |

These are related results, not an already frozen proof or an identified equivalent version of (PDA). This agrees with [port-map](port-map.md), Table 3, and [chain-ca](chain-ca.md), §§3, 7.1. The analytic stage and drop-out obligations in the [CA index README](sa-index/ca-4.12-4.19/README.md) remain separate.

## The geometric data actually used

Write \(s=k-N_0+1\), \(h=k-N_k\), \(m_i=M\ell_i\), and \(\sigma_i=MR_i\ell_i\). CA-I:48141–48261 fixes these units and the compatible grids; it gives \(h<s-1\), \(\sigma_s=M\), and \(\sigma_i\le M\) for \(i\le s\). For one operated component \(X\), the endpoint formulas are
\[
 D_k=X\setminus\Omega_s^{(+5M)},\qquad
 D_s=X\setminus\Omega_s^{(+7M)}.                         \tag{E}
\]
The first is CA-I:48781–48783 and 53774–53782. The second is quoted explicitly at CA-I:92012–92016. The sentence at CA-I:51712 instead calls the second prescribed endpoint \(Z''_{k-1}\); that differs from CA-I:45600 and the displayed quotation at 92015. The construction here follows the latter explicit endpoint formula. For \(h<i<s\), CA-I:51718–51727 and 53783–53785 give
\[
 D_i=X\setminus\Omega_i^{(+5\sigma_i)}.                  \tag{L}
\]
The metric meaning of the tilde is stated at CA-I:48157–48167, and the account quotes its grid at 92012. Below and at \(h\), the domains are unchanged.

The upper completion is
\[
 a_k=5M,\qquad
 a_i=5M+\sum_{r=i+1}^{k}m_r\quad(s<i<k),\qquad a_s=7M,
 \qquad D_i=X\setminus\Omega_s^{(+a_i)}.                 \tag{C}
\]
The account leaves this completion to be chosen. Formula (C) makes that choice; it does not replace either prescribed endpoint. A one-layer separation below means **at least** one layer. That is the inequality used by (A1) and its consumers.

Here are the inputs to this construction, separated from its conclusion.

1. The old label is an admitted input label: \(\Omega_i\supset\Lambda_i^{119}\supset\Omega_{i+1}\), with \(Z_i=(\Lambda_i^{119})^c\), compatible grids, and old (A1). These are the input sequences, not the new sequence whose admission is at issue. See CA-I:4224–4226, 45248–45265, 53755–53763. Old admission is the inductive premise; admission of this operation's output is the conclusion. No prepared-gap assertion is used as an input.
2. Above \(h\), the old members read inside \(X\) are the cell-made members of the one-step construction. The cell side is \(\sigma_i\), not \(m_i\). See CA-I:53816–53831. In particular the enlarged \(\Omega_i^{\sim n}\) are made of \(\sigma_i\)-cubes on the portion read in \(X\), as quoted at 92012 and specified at 48157–48167. At \(s\), this is the grid of side \(M\). This is the alignment supplied by the construction, not an assumption about the new upper completion.
3. The one-step collar estimate is
   \[
   \operatorname{dist}_\infty(Z_i\cap X,\Omega_{i+1}\cap X)
       \ge8\sigma_{i+1}\quad(h\le i<k).                 \tag{T8}
   \]
   This is the cell geometry of the old one-step members in item 2. It is the input proved in `4.4:lem-collar-avoidance(b)`, CA-I:12103–12130, 12181–12233. Its proof reads the construction of CMP 119 (3.5): the complement of \(B^{i+1}(P^1_{i+1})\) contains five layers around \(Z'_i\supset Z_i\), and (3.5) adds three more. Its cubes have side \(LMR_{i+1}\) in level-\(i\) units, hence side \(\sigma_{i+1}\) here. CA-I:91991–92019 also spells out this eight-layer arithmetic at the first prepared junction. We port this proved input. We do not use CA-I:45626–45634, which asserts admission of the produced nests.
4. The top one-step region has
   \[
       (Z_{k-1})^{(+10\sigma_k)}\subset Z_k.             \tag{T10}
   \]
   The open-neighbourhood version suffices; take closures for distances. This is the ten-layer rule in the prepared-data definition, CA-I:53820–53825. The construction adds two layers to the small-field complement before forming the large-field region; its later union and boxing operations only enlarge that region (50342–50428). Thus the eight old layers yield ten. Distinct components of \(Z_k\) are separated by at least \(\sigma_k\). Indeed, \(Z_k\) is a union of its aligned \(\sigma_k\)-cubes, and touching cubes, including corner contact, belong to one component. Cubes in different components have an index difference at least two in some coordinate, hence a coordinate gap at least \(\sigma_k\). This argument also covers a component across a periodic seam.

Items 2–4 specify the old geometry that the account uses in defining a prepared operation. They do not assume its new domains are admissible. We use neither the optional old-core cell hypothesis (G), CA-I:53836–53838, nor the outline's stronger no-merger or closed-endpoint quarantine rules. Sets below \(h+1\) may have earlier thin layers.

Inside \(X\), \(\Omega''_i=X\setminus D_i\) for \(i>h\). Outside the operated components, \(\Omega''_i=\Omega_i\). For \(i\le h\), they agree everywhere. These are the domain rules used at CA-I:51726–51728, 48779–48800. Complements and differences are regularized as in CA-I:45279–45281. Thus a shared face belongs to both closed carriers when needed; it does not alter the infimum distances below.

### Order of choice

Retain the account's order (CA-I:45803–45825):
\[
 d,L\ \longrightarrow\ M_1\ \longrightarrow\ M_1^\sharp
 \ \longrightarrow\ (d,L)\text{-constants}\ \longrightarrow\kappa_1
 \ \longrightarrow\ M\ \longrightarrow\text{layer couplings}
 \ \longrightarrow\text{radii}\ \longrightarrow\ g .    \tag{O}
\]
The account already imposes odd \(L\ge8\), hence \(L\ge3\), and compatible power-of-\(L\) sizes (CA-I:45242–45245, 45669–45687). Its operation regime requires \(k>N_k>N_0\), \(R_k>1\), and existence of \(N_0\) (45827–45863). Its proof at 48209–48261 gives
\[
 \sigma_i\le\sigma_{i+1},\quad
 \sigma_s=M,\quad s\le k-1,\quad h<s-1,\quad
 \sigma_k=MR_k\ge LM.                                  \tag{S}
\]
For clarity, the monotonicity uses only
\(R_i\le(L+1)R_{i+1}\) and power-of-\(L\) quantization: their ratio is at most \(L\), so
\(R_i\ell_i\le R_{i+1}\ell_{i+1}\). We use that proof, not DOM's different frame-based radius rule.

There is no new constant to choose, coupling ceiling to impose, or smallness estimate to obtain. The integers 5, 7, 8 and 10 are the account's existing layer counts. Formula (C) is defined after the operation's levels are known and works uniformly in their number. No operator constant depends on this choice.

## Hand proof

### 1. Grid operations and the component boundary

Let \(\mathcal P_q\) be an aligned cube partition of side \(q\), and let \(p\mid q\). If \(E\) is a union of its cubes and \(r\) is a nonnegative integer multiple of \(p\), its closed maximum-norm enlargement is a union of \(p\)-cubes. To see this, subdivide each \(q\)-cube into \(p\)-cubes. Enlarging one such cube replaces each coordinate interval \([b,b+p]\) by \([b-r,b+p+r]\). Its endpoints remain in the \(p\)-grid. Take the union over the original cubes. Regularized complementation gives the corresponding claim for erosion. Finite unions, intersections and regularized differences of sets in one grid remain in that grid. The same proof works on a compatible periodic grid, by projection from its periodic lift.

For \(i<k\), put
\[
 E_i=\overline{\Omega_i^c}\cap X.
\]
Nesting gives \(E_i\subset\overline{Z_{k-1}}\cap X\). By (T10), the open ball of radius \(10\sigma_k\) about each of its points lies in \(Z_k\). Such a ball is connected and meets \(X\), so it belongs to that same component. Therefore
\[
 \operatorname{dist}_\infty(E_i,X^c)\ge10\sigma_k.         \tag{B}
\]
This also shows that (T8) holds with the full \(\Omega_{i+1}\) in place of its trace. Points of \(\Omega_{i+1}\) outside \(X\) are at distance at least \(10\sigma_k\) from \(Z_i\cap X\), since \(i\le k-1\). By (S), \(10\sigma_k\ge8\sigma_{i+1}\).

For \(h<i\le s\), \(E_i\) is a union of \(\sigma_i\)-cubes by the old cell alignment. Intersecting with \(X\) preserves this grid: \(X\) uses \(\sigma_k\)-cubes and \(\sigma_k/\sigma_i\) is a nonnegative power of \(L\). For every radius used below, (B) exceeds that radius. Thus eroding \(E_i\) relative to the whole lattice gives exactly
\[
 X\setminus\Omega_i^{(+r)}
\]
after regularization. Indeed, the complement of \(E_i\) consists of the old small-field set and the outside of \(X\); the outside cannot contribute to the erosion at radius \(r<10\sigma_k\). This proves that a boundary of \(X\) cannot introduce a spurious cut in the new domains. It also justifies using the local cell alignment when \(\Omega_i\) elsewhere has older thin layers.

### 2. Complete the upper levels

Use (C). For \(s<i<k\), \(a_i\) is an integer multiple of \(m_{i+1}\), hence of \(m_i\). The endpoints \(5M,7M\) are multiples of every finer \(m_i\). Since \(E_s\) uses the \(M\)-grid and \(a_i\le7M<10\sigma_k\), §1 proves that every \(D_i\), \(s\le i\le k\), is a union of level-\(i\) \(M\)-cubes. It also proves the stronger grid property used in the shell description: \(D_{i-1}\) is a union of \(m_i\)-cubes for \(s<i\le k\). Consequently \(D_i\setminus D_{i-1}\) is a union of such cubes. This matches CA-I:121772–121777.

The radii strictly decrease with \(i\). For \(s<i<k\),
\[
 a_i-a_{i+1}=m_{i+1}.                                  \tag{U1}
\]
At the remaining junction, if \(s=k-1\), the difference is \(7M-5M=2M\ge m_k\). If \(s<k-1\), the finite geometric sum gives
\[
 \begin{split}
 a_s-a_{s+1}
 &=2M-\sum_{r=s+2}^{k}m_r\\
 &\ge 2M-\frac{LM}{L-1}
 =\frac{L-2}{L-1}M
 \ge\frac M2\ge m_{s+1}.
 \end{split}                                           \tag{U2}
\]
The last inequality uses \(s+1\le k-1\) and \(L\ge3\). The bound on the finite sum follows by multiplying \(1+L^{-1}+\cdots+L^{-n}\) by \(1-L^{-1}\); no numerical evaluation or infinite-sum theorem is needed.

Distance to a fixed nonempty set is 1-Lipschitz: the triangle inequality gives \(d(x,A)\le |x-y|_\infty+d(y,A)\), and interchange of \(x,y\) gives the reverse bound. If \(x\in D_i\) and \(y\in X\setminus D_{i+1}\), the regularized closed-carrier versions give
\[
 d(x,\Omega_s)\ge a_i,\qquad d(y,\Omega_s)\le a_{i+1}.
\]
Hence
\[
 D_i\subset D_{i+1},\qquad
 \operatorname{dist}_\infty(D_i,X\setminus D_{i+1})
       \ge a_i-a_{i+1}\ge m_{i+1}\quad(s\le i<k).        \tag{U3}
\]
If either set in a distance is empty, the inequality has its usual value \(+\infty\). If \(\Omega_s\) is empty, then \(D_i=X\) and \(X\setminus D_{i+1}=\varnothing\), so the same conclusion holds without using its distance function.

Finally, \(D_i\subset\Omega_s^c\cap X\subset\Omega_i^c\cap X\). Thus each replacement enlarges the small-field domain; it does not remove old small-field points.

### 3. The lower levels and both junctions

For \(h<i<s\), define \(D_i\) by (L). Because \(5\sigma_i\) is a multiple of \(\sigma_i\), §1 makes \(D_i\) a union of \(\sigma_i\)-cubes and therefore of \(m_i\)-cubes. Also \(D_i\subset\Omega_i^c\cap X\subset Z_i\cap X\).

First take \(h\le i<s-1\). At \(i=h\), take \(x\in\Omega_h^c\cap X\); at \(i>h\), take \(x\in D_i\). Both choices lie in \(Z_i\cap X\). A point \(y\) of the next new small-field domain inside \(X\) belongs to \(\Omega_{i+1}^{(+5\sigma_{i+1})}\). Choose points of \(\Omega_{i+1}\) attaining, or approaching, this enlargement distance. The triangle inequality and (T8) give
\[
 |x-y|_\infty\ge(8-5)\sigma_{i+1}
                    =3\sigma_{i+1}\ge m_{i+1}.          \tag{L1}
\]
This includes the unchanged-to-prepared junction \(h,h+1\). It assumes no cell alignment of \(\Omega_h\) or \(Z_h\).

For \(i=s-1\), the next domain is instead \(\Omega_s^{(+7M)}\cap X\). Since \(\sigma_s=M\), the same argument gives
\[
 |x-y|_\infty\ge(8-7)M=M\ge m_s.                        \tag{L2}
\]
This is the lower-to-upper junction. It uses the prescribed second endpoint of (E), not a movable endpoint. The case \(h=s-2\) is included: there is one lower prepared level and both estimates still apply.

Equations (L1), (L2), and (U3) prove all new within-component gaps. In particular they prove nesting at each junction. They also give \(Z_h\cap X\subset D_{h+1}\), the core containment asserted in CA-I:53793–53796, since (L1) holds with any \(x\in Z_h\cap X\).

### 4. Glue the prepared components to the old domains

Let \(\mathsf Z\) be any union of the operated components. For \(i>h\) define the global domain by the account's rule
\[
 \Omega''_i\cap X=X\setminus D_i\quad(X\subset\mathsf Z),
 \qquad \Omega''_i\setminus\mathsf Z=\Omega_i\setminus\mathsf Z.
                                                               \tag{G}
\]
For \(i\le h\), set \(\Omega''_i=\Omega_i\). All sets are regularized. Each \(X\) is a union of \(\sigma_k\)-cubes, which subdivide into every \(m_i\)-grid used here. The old domains and the new pieces therefore give compatible \(m_i\)-cube unions globally.

We have already proved
\[
 \Omega_i\subset\Omega''_i.                              \tag{G1}
\]
Fix \(1\le i<k\), \(x\in(\Omega''_i)^c\), and \(y\in\Omega''_{i+1}\). We check every possible location.

- If \(y\in\Omega_{i+1}\), (G1) puts \(x\in\Omega_i^c\). Old (A1) gives \(|x-y|_\infty\ge m_i\).
- Otherwise, \(y\) is a newly added point in some operated component \(X\). If \(x\in X\), the corresponding estimate (L1), (L2), or (U3) gives \(|x-y|_\infty\ge m_{i+1}\). This case only occurs above the unchanged levels.
- If \(x\notin X\), (G1) and old label nesting give \(x\in\Omega_i^c\subset Z_i\subset Z_k\). It lies in a different component of \(Z_k\). The component gap gives \(|x-y|_\infty\ge\sigma_k\ge M\ge m_i\).

The cases include unoperated components, several operated components, and their boundary faces by passage to closures. Thus
\[
 \operatorname{dist}_\infty((\Omega''_i)^c,\Omega''_{i+1})\ge m_i.
                                                               \tag{G2}
\]
The strict positivity of \(m_i\) implies \(\Omega''_{i+1}\subset\Omega''_i\). If the old input has the stronger gap \(m_{i+1}\), the same proof preserves it: replace the first case's bound by that gap, and use \(\sigma_k\ge M\ge m_{i+1}\) in the third case. No stronger old gap was needed for (PDA).

Because \(h\ge1\), \(\Omega''_1=\Omega_1\). Retain its old Dirichlet hull as \(\Omega''_0\); equivalently, form the hull prescribed in (A1). It contains \(\Omega''_1\) and satisfies precisely the required level-zero clause. This completes (A1), including its hull, partitions, nesting and constants. At levels where the operation's regime fails there is no operation, by CA-I:45853–45854; no exceptional prepared nest must be admitted.

### 5. Geometric stage uses

The same argument allows each component \(X\) to stop at its own prefix \(p(X)\), \(h\le p(X)\le k\). Use (G) only for \(h<i\le p(X)\). At its upper junction, \(i=p(X)\), the next domain is old and (G1) gives the old gap. All other cases in §4 remain the same. This proves the geometric (A1) claim for the componentwise stage nests used at CA-I:48507–48523, 48759–48770, 48841–48863. An earlier thin layer below \(h+1\) is simply part of the admitted old input.

These are geometric implications for the specified component and prefix rules. They prove no gauge bound, current bound, holomorphic inclusion, measure identity, or later analytic-space extension. Those are the separate conditions of `4.14:rem-supply-scope`, CA-I:49495–49546. In particular neither the operator theorem itself nor its (A2) premise is inferred from (PDA).

## Source and use ledger

The index was used to locate each object before relying on its source argument. Relevant outline rows are in `sa-index/chunk-16.md` and `obligations.md` at SA:17398–17447, 17575–17591. Those source passages sketch the geometry and use a stronger class rule. They supply no premise of the proof above. Relevant CA index rows are in chunks 03, 07, 08 and 09 of `sa-index/ca-4.12-4.19/`, and the `ca-full/index.tsv` row for `4.4:lem-collar-avoidance` with its neighbouring rows.

The following accounts for every occurrence in CA-I of the target's proposition label or its displayed-condition labels, apart from their definitions at 45557–45634. These use ranges were read in the source. Exact-label searches in the existing CA-II and CA-III copies returned no occurrences.

| CA-I use | What it reads |
|---|---|
| 46035–46156 | The operator theorem assumes both (A1) and (A2). |
| 46242–46263 | Reading hulls use the (A1) separation with the previously chosen \(M/M_1^\sharp\) floor. |
| 46476–46482 | The unit-frame remark uses (A2). Its attribution to the printed proposition does not enlarge that proposition's last sentence. |
| 46800–46865 | Local balls use aligned cubes and a weighted layer-crossing cost at least \(M\). |
| 47253–47293, 47608–47685 | Form assembly and coercivity retain the geometric hypotheses; the explicit use list distinguishes (A1) from (A2). |
| 47736–47754 | Unit-lattice positivity needs the separate (A2) margin. |
| 47991–48048 | Core regrouping uses (A2); local-ball admission uses (A1). |
| 48131–48140 | The final operator-theorem implication assumes the conditions throughout its history. |
| 48337–48387 | The hull-cube lemma requires exactly the (A1) partition, nesting and gap properties. |
| 48507–48523, 48759–48770, 48841–48863 | Gauge-family classification and componentwise stage bookkeeping assume geometric (A1). Section 5 supplies it for prefixes of this prepared operation. |
| 52544–52589 | The cube-class argument uses the closed, compatible cube structure of \(\Omega_1\). |
| 52670–52794 | Lowest-level regularity assumes (A1), along with separate analytic and geometric hypotheses. |
| 52796–52822 | Shell subdivision uses the compatible partitions. |
| 53041–53066 | The weight argument uses positive separation of nonadjacent shells. |

The defining input passages are 45236–45294 (units and regularization), 45557–45634 (target), 45669–45687 and 45803–45879 (order and operation regime), 45962–46034 (class), 48141–48261 (grids and scales), 48774–48800 and 51707–51728 (replacement rules), 53737–53839 (prepared data), 91991–92022 (explicit endpoint and layer grid), and 121746–121808 (the later frozen-shell reading). The ported one-step collar argument is 12103–12257; the monotone large-field enlargement is 50316–50428. No assertion of prepared admission in these passages was used to prove itself.

Source excerpts and the exact label-occurrence list are saved in `/tmp/pda-work/source-excerpts.txt`; source identities and local comparison-file hashes are in `/tmp/pda-work/manifest.txt`. These files are retrieval records only. The proof uses no numerical run, enumeration, or computer-assisted discharge. The quoted CMP 122a page itself was not inspected. The checkout has no `docs/ai_methodology/SCIENCE_WORKFLOW.md`; no workflow, audit or planning process was run, and no editable prompt file was changed.

## Result

**Proof**

For the prepared large-field data of CA-I `4.14:prop-prepared-data-admissible`, with the old input geometry and endpoint definitions specified above, the intermediate sets can be chosen by (C). The resulting \(\Omega''_1,\ldots,\Omega''_k\), with their prescribed Dirichlet hull, satisfy **(A1) exactly as stated**. The proof also preserves any inherited later-level gap and proves geometric (A1) for every componentwise stopped prefix.

This fills the printed-without-proof completion and admission step attributed to **Tadeusz Bałaban**, using the text of **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. The account's already proved one-step collar argument is ported, not replaced. The separate (A2) premise and the analytic supply conditions remain separate. This proof has not yet been checked by another model; it grants no audit or retained status.
