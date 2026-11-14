# GEOH: actual-history geometry

Provenance: Codex, Pass 2 distillation of Claude's `geoh-draft.md`, checkout `ee837f4f89ce914c210ea1578e309056d0a8cdad`, 2026-11-05. Research text; not an audit; grants no status; not yet refereed. Material from the pinned Sussman–Alpoge texts is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

SA denotes `YM4_sketch_500.tex`; CA-I, CA-II and CA-III denote `theorem_0_complete_account_raw_{I,II,III}.tex`; Y3 denotes `YM3/YM3_I.tex`, all at [31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775). Their region, preparation, counting and coordinate constructions follow Tadeusz Bałaban. The local consumers are [IN1](in1.md), [AG1](ag1.md), [ST1](st1-r4.md) and [CLS](cls.md). This manuscript concerns assembly critical-path item 3, LF1(2). Every proof below is a hand argument. Source retrieval and hashes are bookkeeping only.

## 1. Definitions and geometric inputs

**Definition 1 (scales and cells).** Fix odd \(L\ge27\), \(r\ge2\), and the IN1 frame
\[
 \theta_j\ge X_0>e,\qquad
 \underline\lambda(j-i)-c_5\le\theta_i-\theta_j\le\overline B(j-i),
 \qquad |x_j-\theta_j|\le\theta_j/4.
\]
Put \(m_j=\min_{i\le j}\theta_i\), \(R_j=\lceil(\log m_j)^r\rceil_{L^{\mathbb N_0}}\), \(N_j=R_j\), and \(\ell_j=1+\log x_j\). The later choice \(M\ge1\) is an aligned power of \(L\). At observation level \(t\), a level-\(i\) lattice spacing is \(\xi_i=L^{i-t}\), an \(M\)-cube has side \(m_i^{M}=M\xi_i\), and a **cell** has side \(s_i=R_im_i^{M}\); write \(\rho_i=s_i/s_{i-1}\). These are three different lengths. Cell partitions are aligned. Assign boundary sites by a fixed half-open convention; use closed carriers for distances and touching. Cells are adjacent when their carriers touch, including corners. \(N_a\) denotes cell-index sup-neighbourhood of integer radius \(a\), on the stated level. Metric neighbourhoods are written \(N^{\rm met}_a\). Counting below uses cells, not lattice sites.

SA 17334 uses the actual running coupling in the scale rule; IN1 uses the frame. The conclusions apply to either sequence when that sequence obeys the displayed increment bound. A tube bound alone does not give bounded adjacent increments for \(x\). On IN1's constructed central run \(x=\theta\); no such identification is made for an arbitrary point of its tube.

**Input R (the discrete history rule).** The initial live region is empty. At step \(t\), write \(Y\) for the preceding live region. In level-\(t\) cells set
\[
 A_t:=\Omega_t^c=N_2Q'_t\cup N_4P'_t\cup N_8\widehat Y,
 \quad Z^{[0]}=\mathsf{bx}(N_2A_t\cup N_1R'_t),
 \quad Z^{[a+1]}=\mathsf{bx}(Z^{[a]}\cup N_1F_a).
 \tag{1}
\]
Here \(R'_t\) is a failure set, unrelated to the scalar \(R_t\). The final region is \(Z_t^{\rm m}\). The creation set \(W_t\) comprises \(P'_t,Q'_t,R'_t\) and the cells of all collar/rim failures \(F_a\). A fixed round rule examines each test object at most once. Boxing repeatedly fills the bounding box of a component contained in a cube of \(b\) cells, for a fixed integer \(b\); it never boxes an arbitrarily large component. Fix its schedule, the cell hull convention and all geometric selectors. These are the rules of SA 17317–17367. Initially \(\Omega_0=\Omega_1^\sim\); the history does not assume that \(\Omega_0\) is the whole torus.

**Definition 2 (ancestry, class and operations).** A node \((t,C)\) is a component of \(Z_t^{\rm m}\), before its operation. Healing removes the whole node from the live region \(\mathcal Z_t^{\rm m}\); an island or drop-out keeps it. An unhealed node is a predecessor of the next-level component containing its hull. All genealogies in (14) are these **as-made** genealogies. Cut an outer genealogy at each first inner island, retaining the island as a leaf. Count all its cells as artificial creations there; do not replay its interior record.

For \(h=t-N_t\ge1\), the class consists of components whose traces from \(h\) through \(t\) are single small components, of side at most \(b_{\rm cl}=100\) cells; whose evolution on \((h,t]\) has no creation or merger and is \(\mathsf{bx}(N_{10}\widehat{\cdot})\); and whose ancestral components have not been operated on at a level in \([h,t)\). Operate on every qualifying component. The number 100 is the fixed size choice in CA-I 53747–53753; SA 17575 specifies an unspecified fixed size. The proofs below require a cutoff at least 69.

The last clause is the **ancestral reading of quarantine** used here. It includes an operation on an old standing mark contained in the trace. It is not a prohibition on every former operation at an overlapping spatial location: SA 17449 explicitly allows a healed location to be covered again. SA 17575 expressly includes the lower endpoint \(h\), and SA 17449's window lemma uses that inclusion for marks. In contrast, CA-I 45996–46032 fixes the open exclusion window \((h,t)\) and distinguishes the stronger reading including \(h\). The CA rule alone therefore yields at most \(s\le h\), not frozen GEO-mark's \(s<h\); it cannot replace SA's closed-endpoint rule here.

The draft's claim that “no standing recent mark” is the only possible reading, or is equivalent to the whole quarantine clause, is withdrawn. **Outstanding — quarantine identification:** the revised operation must adopt the stated ancestral, closed-endpoint rule or prove that its class decisions imply the same consequences. Neither the different CA rule nor the word “quarantine” establishes that match. This is the only quarantine interpretation used in the waiting theorem.

**Input P (preparation and label updates).** In a class component \(X\), let \(D_i=Z''_i(X)\), \(C=X\cap Z_h\). Fix a deterministic nest selector, with
\[
 D_h=C,\qquad C\subset D_{h+1}\subset\cdots\subset D_t,
 \qquad D_i\subset X\cap\Omega_i^{\circ c}.                 \tag{2}
\]
The circle means the label immediately before this operation. For the full stage-level comparison below, retain the local metric input
\[
 N^{\rm met}_{m_i^M}(D_{i-1})\cap X\subset D_i
 \quad\text{for open neighbourhoods},\qquad h<i\le t.       \tag{P-gap}
\]
This is the local nest gap in `geo-5.md` (3.1), also used by `geo5c-count.md`; its use is separate from any global nesting theorem. CA-I 53779–53782 supplies this reading for \(i>k_0\), that is for every \(i\in I_M=\{k_0+1,\dots,k\}\), so the pair \((k_0,k_0+1)\) is included, where \(k_0=t-N_t^0\) and \(L^{N_t^0-1}=R_{k_0+1}\). Below that range CA-I writes \(D_i=(\Omega_i^{\sim5})^c\cap X\). It does **not** say, at 53742–53743, that every such tilde denotes level-\(i\) \(M\)-cube layers, as the draft claims. **Outstanding — lower preparation convention:** to obtain all of P-gap solely from that formula, supply its layer grid. If each of its five layers has width at most \(s_i\), quiet padding gives the gap: a point of \(\widehat{X\cap Z_{i-1}}\) is at least \(8s_i\) from \(\Omega_i\) (from \(\Omega_i\cap X\) by quiet padding, and from \(\Omega_i\setminus X\) by the clause \(N_{10}H_i\subset X\) of (8)); the five layers, with at most one cell of boundary rounding, leave at least \(2s_i\ge m_i^M\). This proves the implication under that explicit grid convention. The exclusion of the cp12 configuration below needs only the upper, final gap.

The main-step box has the supplied geometry
\[
 \Lambda^{\rm pr}=(\Omega_{k_0+1}^{\sim4})^c\cap X
 \subset \Omega_{k_0+1}^{\circ c}\cap X,
 \quad N^{\rm met}_{M}(D_t)\cap X\subset\Lambda^{\rm pr}
 \subset\overline{N^{\rm met}_{M}(D_t)}.                    \tag{3}
\]
The first neighbourhood is open. These are CA-I 53786–53804 and its explicit final-level interpretation at 53858–53884. We import the nest and box specification, not a theorem about analytic backgrounds.

Healing fills \(\Omega_i,\Lambda_i\) and clears \(S_i\) inside \(X\) for every \(i\le t\). An island does the same except that \(\Lambda_t\) is unchanged. A drop-out after \(n\le N_t\) stages sets \(\Omega_i\cap X=X\setminus D_i\) for \(h<i\le h+n\), and sets \(\Lambda_i\cap X=X\setminus D_i\), \(S_i\cap X=\varnothing\) at those levels with \(i<t\); other entries are unchanged. In particular its top \(\Lambda_t\) is unchanged even if \(n=N_t\). Marks persist until swallowed by healing or an island. Their recorded completed count is fixed while they stand. The action choice restores pre-operation entries at drop-out windows; the determining choice keeps all completed replacements. Intermediate stopping choices use a prefix of those replacements. These are SA 17415–17447 and R21, 6095–6115.

## 2. Basic geometry and marks

**Lemma 1 (scale estimates).** Put \(K_R=L2^{r-1}(1+r^r\overline B)\). For sufficiently large \(X_0\), adjacent \(R\)'s have ratio 1 or \(L\), two drops cannot be consecutive, and
\[
 R_i\le L^{\lceil(j-i)/2\rceil}R_j,\qquad R_{t-N_t}\le K_RN_t.
 \tag{4}
\]
The floors depend only on \(L,r,\overline B\).

*Proof.* Running minima satisfy \(m_{a+2}\ge m_a-2\overline B\). Choose \(X_0\ge4\overline B\) with
\((1-4\overline B/(X_0\log X_0))^{-r}<L\). Then
\(\log m_{a+2}\ge\log m_a-4\overline B/m_a\); their logarithmic powers have ratio less than \(L\). A skipped rounded power, or two successive drops, would give \(R_a/R_{a+2}\ge L^2\), forcing the unrounded ratio to exceed \(L\). The one-step version gives the same adjacent bound at a history endpoint. This proves the first assertions and the first bound. For \(h=t-N_t\), choose an index attaining \(m_t\). If it is after \(h\), the frame gives \(m_h\le m_t+\overline BN_t\); otherwise the minima agree. For \(y\ge0\), \(\log(1+y)\le r y^{1/r}\): their derivatives have this order because \(y^{1-1/r}\le1+y\). Thus
\[
 R_h\le L2^{r-1}\{(\log m_t)^r+r^r\overline BN_t\}\le K_RN_t.
\]
Only integration of the displayed scalar derivative inequality is used. ∎

**Lemma 2 (what outcome independence means).** For fixed frame, grid, selectors, test schedule and complete geometric outcome record, the regions, classes, fates and nests are determined. The same record gives the same geometry under a change of analytic test formulas which leaves these discrete rules unchanged.

*Proof.* Induct over the finite ordered record. Equation (1) determines the next regions from the old live set and listed failures. Class membership reads these regions and ancestral operation records. The fixed selector gives the nest. The listed fate and completed count give the label update. Each is determined before the next induction step. ∎

This repairs draft Lemma 2.0. Geometry generally **does depend on which tests pass**. Descent's fixed-region Y3 replacement, Tq0's radii, intrinsic domains and Amendment CV do not themselves prove that a changed construction uses the same selectors or outcome record. ST1 L41 expressly permits changed passing tests; descent L7 and L188 concern fixed regions. Our geometric conclusions quantify over every record satisfying R, P and the class rule. **Outstanding — realization:** compatibility of the revised analytic operation with these rules and the coding/read interfaces in Theorem 1 is a separate input. No equality of the old and new passing branches is asserted.

**Lemma 3 (boxing, ancestry and ANC).** For any cell set \(B\),
\(B\subset\mathsf{bx}(B)\subset N_bB\); each output component contains an input component. The same reach holds relative to the union of all unboxed inputs of one step, regardless of the number of rounds. An unhealed node has one successor when the next step exists; predecessors have level one less; an ordinary leaf has an own-level creation. AG1's (ANC) holds: if a cell is live at levels \(j-1,j\), its first live component is contained in its second.

*Proof.* Each current component contains an original cell. When a component fits in a cube of side \(b\), its new bounding-box cells lie within \(b\) of an original cell in that component. Merging does not remove that witness. Induct through all boxings and inserted failure sets; finiteness terminates each strictly growing sequence. This proves the reach without adding a cost for each round. Equation (1) contains \(N_{10}\widehat Y\). The hull of a connected input component is connected, so lies in one output component. Its successor is unique. If a component has no predecessor, its unboxed ancestors come from failure neighbourhoods; each such neighbourhood meets its failure set. Boxing cannot create an unattached component, so the node contains a creation. Levels decrease along predecessors, giving a finite tree.

For ANC let \(A\) be the old live component containing the cell. It lies in one pre-operation component \(B\). The operation either removes all of \(B\) or keeps all of it. Since the cell survives, \(B\) is kept. Hence \(A\subset B\). Along \(E_z^{(n)}(q)\), iteration puts \(z\) in every ancestral lineage \(\mathsf Z_j(C_q)\). This is precisely the as-made reading defined in AG1 L35–47; no second meaning of AG1's live regions is needed. ∎

**Lemma 4 (current labels and GEO-mark).** For each fixed consistent stopping vector, the current complements \(Z_i=\Lambda_i^c\) are nested. Under the ancestral class rule, all six GEO-mark clauses hold: a pre-existing standing mark \((s,Y)\subset X\) in a class component at \(t\) satisfies \(s<t-N_t\); windows of overlapping standing marks are disjoint; disappearance requires swallowing by healing or an island; completed counts never decrease; islands supply no remake levels; and at each operation level a point lies in at most one class component.

*Proof.* Nesting starts with Lemma 3 at each new top. Filling a component removes the same set from every earlier complement; an island retains only its top complement. In a prefix replacement, the lower splice is \(Z_h\cap X=D_h\subset D_{h+1}\), the internal pairs are nested by (2), and the upper splice follows from \(D_i\subset\Omega_i^{\circ c}\cap X\subset Z_i^\circ\subset Z_{i+1}^\circ\). Outside \(X\) nothing changes. This also preserves the alternating label inclusions \(\Omega_{i+1}\subset\Lambda_i\subset\Omega_i\). If several standing windows are present, the induction below makes them disjoint before any new prefix is installed.

An old standing mark persists as a whole connected component at its birth-level entry. At a later operation, nesting puts any mark that meets the new component wholly inside it. Its birth operation is an operation on that component's ancestry. Quarantine therefore excludes \(t-N_t\le s<t\). This proves the strict inequality, including its lower endpoint. When a new mark is formed, every older overlapping standing mark is contained in it and has top below its window's bottom. Induction from the empty record proves both laminarity of standing marks and disjointness of their windows, and justifies the prefix nesting used above.

Disappearance and constancy of the recorded count are the update rule. Interpolated structures must also be compared componentwise with nondecreasing stopping counts; arbitrary stopping vectors are not ordered transitions. An island's entries do not depend on a stopping parameter, so it contributes no remake levels. Distinct class components at one level are disjoint. These prove the remaining clauses. ST1's stage indices are \(h,\ldots,h+n-1\), the window indices shifted by minus one; their disjointness follows by this common translation, not by claiming that \(h\in(h,t]\). ∎

## 3. The IN1 geometry contract

**Definition 3 (occupied cells and events).** For an outer node \(u=(n,C)\), let \(O(u)\) be the level-\(n\) cell images of all creations in its rooted subtree, including at \(u\) and at artificial cut leaves. Put \(o(u)=|O(u)|\). At level \(n\), sum these counts to obtain \(o_n\); let \(l_n\) count nodes with \(o(u)\le C_{\rm geo}\). Let \(n_t^{\rm cr}\) count creations and \(n_t^{\rm mk}\) non-root marks. An event is an own-level creation, a merger, or the successor of a mark. Counts before the initial level are zero. The symbol \(C_{\rm geo}\) is IN1's \(C_g\); it is unrelated to ST1's formation \(C_g\), here called \(C_{\rm form}\).

**Lemma 5 (both inequalities (14)).** Set
\[
 e=32+3b,\quad h_0=2e+1,\quad C_{\rm geo}=h_0^4,
 \qquad s_0=2\lceil\log_L(256h_0)\rceil.
\]
For every outer genealogy,
\[
 |C(u)|\le C_{\rm geo}(1+o(u)),\qquad
 o_n\le\tfrac12o_{n-s_0}+C_{\rm geo}l_{n-s_0}
                  +\sum_{n-s_0<t\le n}n_t^{\rm cr}.        \tag{14}
\]
Thus IN1's version, with coefficient \(C_{\rm geo}\) on the last sum, follows.

*Proof.* A creation's successive parent cells lie in its successor nodes. Hence \(O(u)\subset C(u)\). Put \(E=2(11+b)\). Inductively the reach from \(O(u)\) to \(C(u)\) is at most \(E\) at a nondrop, and at most \(E+10+b=e\) at a drop. Indeed a step adds at most ten cells to a predecessor hull or six cells to a new failure, followed by boxing reach \(b\). Coarsening by \(\rho\in\{1,L\}\) replaces reach \(a\) by at most \(\lceil a/\rho\rceil\). At a drop the preceding step is a nondrop. At a nondrop,
\(\lceil e/L\rceil+10+b\le e/L+11+b\le E\) for \(L\ge27\). Ordinary leaves have reach at most \(6+b\); cut leaves have reach zero. Mergers take the maximum. Thus \(C(u)\subset N_eO(u)\), giving the first inequality. Also \(O(u)\) is \(h_0\)-connected: a partition at distance greater than \(2e+1\) would disconnect its two \(e\)-neighbourhoods and hence \(C(u)\).

For an \(h_0\)-connected set of \(N\) cells, traverse a spanning tree twice. Split its at most \(2(N-1)\) edges into pieces of \(\lfloor q/h_0\rfloor\) edges, where \(q\ge2h_0\). A piece spans at most \(q\) indices in each coordinate, hence meets at most \(2^4\) coarse cells. There are at most \(1+4h_0N/q\) pieces, so
\( |\pi_q O|\le16+64h_0N/q\).
Across \(s_0\) steps the ratio is at least \(L^{s_0/2}\ge256h_0\). A heavy node therefore contributes at most \(16+o/4\le o/2\), since \(o>C_{\rm geo}\ge64\); a light one contributes at most \(C_{\rm geo}\). Every older creation passes through one level-\((n-s_0)\) node; each newer creation has one level-\(n\) image. Sum these bounds. The same argument works across periodic seams; image identification can only decrease counts. ∎

**Lemma 6 (the waiting rule and cut leaves).** Put
\[
 A_*=h_0C_{\rm geo}+2e+2,\quad
 b_0=2\lceil\log_L A_*\rceil,\quad C_T=b_0+2,\quad
 N_{\rm cut}=100^4.
\]
Assume the torus is admissible for lifts of every light-node box of side \(A_*\) cells and every subsequent class read box. A stretch starting at \(t\), whose first node may be an event and whose subsequent nodes have exactly one predecessor, no own-level creation and no preceding mark, has at most \(C_TR_t\) light nodes. Every outer leaf contains a creation; every cut leaf has at most \(N_{\rm cut}\) cells.

*Proof.* With no creations, occupied counts cannot increase. From its first light node at \(a\), the skeleton bound gives a containing lifted box of side at most \(A_*\): a spanning tree has at most \(C_{\rm geo}-1\) edges of length \(h_0\), and the extra reach is \(e\) at each end. On a chain with one predecessor, boxing does not enlarge the bounding box. Its sides satisfy
\(\alpha_{i+1}\le\alpha_i/\rho_{i+1}+22\), hence
\(\alpha_{i+2}\le\alpha_i/L+44\).
After \(b_0\) steps the side is at most \(1+44L/(L-1)<47\). Applying the two-step bound separately to the even subsequence and bounding the intervening step by 22 keeps every later side below 69.

If the history reaches \(k=a+b_0+R_a\) on this chain, then \(k-N_k\ge a+b_0>t\). Throughout its class window the trace is a single component of side below 100, with no creation or merger. No ancestor there was operated on: healing would end the chain, and either other fate would mark it. All three class conditions hold, so the operation must occur. This ends the unmarked chain. There were at most \(b_0+R_a+1\le C_TR_t\) light nodes. A terminal history only shortens it. Ordinary leaves were treated in Lemma 3; cut leaves carry their artificial creations and fit in a 100-cell box. ∎

The extra light-node torus requirement is explicit. The draft's reference only to class-box admissibility did not by itself justify lifting a potentially much larger light skeleton. A sufficient uniform floor is given in Theorem 4 below.

**Lemma 7 (volume and a sufficient literal code).** Define the active addresses \(\mathcal A=\{(n,c):c\subset C(u),\ u\text{ outer at }n\}\), join neighbouring same-level cells and parent cells, and root at a fixed cell of the root component. Then \(\mathcal A\) is connected, its graph degree is at most \(D=L^4+83\), and
\[
 V^\circ=\sum_{(n,c)\in\mathcal A}\ell_n(MR_n)^4\ge|\mathcal A|,
 \qquad \mathsf V\le v^\natural\le2\mathsf V.               \tag{5}
\]
Here \(v^\natural=V^\circ+\sum_yv^\natural(\omega_y)\), as in IN1 (6), and \(\mathsf V=\sum_{u\in\mathcal G}\ell_{n(u)}(MR_{n(u)})^4|C(u)|\) counts every full-genealogy node once.

For coding, require the following **local record interface**, with integers fixed before \(\kappa\). At an owning address with \(v_n=(MR_n)^4\) sites there are at most \(K_sv_n\) outcome slots of an alphabet of size \(K_o\), at most \(v_n\) storage/seam slots of size \(K_{\rm st}\), one creation bit, and, at a designated component address, at most \(3K_f(R_n+1)^p\) operation choices. Selectors and schedules read these data and fixed frame choices only; together they reconstruct the outer record. Continuous stored coordinates are integration variables, not discrete codes. Every free frame has its factor \(w^{-1}\). Then a fixed active set has at most \(\exp(b_{\rm code}V^\circ)\) non-frame codes, with
\[
 c_R=\log(2^{r+1}L)+r,\qquad
 b_{\rm code}=\log2+K_s\log K_o+\log K_{\rm st}+\log(3K_f)+pc_R.
 \tag{6}
\]

For a root \((i,X)\), let \(\#_j\) count level-\(j\) sites, \(Z_j^{\rm a}\) denote its current action-label holes, \(n^\sharp\) count stored/read sites with their actual charge multiplicities, and \(\ell_{\min}=\min_{j\le i}\ell_j\ge1\). Require an **ownership interface**: every charged site has an owning genealogy cell at its level and lies in the site box obtained by adjoining \(c_{\rm rd}\) layers of \(M\)-cubes, with fixed integer \(c_{\rm rd}\ge1\). Count this box with the half-open convention; increase \(c_{\rm rd}\) by one if a closed read boundary needs it. For each cell occurrence in the recursive sum \(v^\natural\), each site is charged at most \(\mu_{\rm rd}\) times, with fixed \(\mu_{\rm rd}\ge1\). If \(R_n\ge2c_{\rm rd}/(2^{1/4}-1)\), then
\[
 V_{\rm in}:=\sum_{j<i}\ell_j\#_j(Z_j^{\rm a}\cap X)\le v^\natural,
 \qquad n^\sharp\le2\mu_{\rm rd}v^\natural/\ell_{\min}.     \tag{7}
\]
Consequently an actual reserve volume satisfying \(v\le a_vV_{\rm in}+b_vn^\sharp\) has \(v\le C_vv^\natural\), \(C_v=a_v+2\mu_{\rm rd}b_v\), for fixed nonnegative \(a_v,b_v\).

*Proof.* Each node's cells are connected, and parent edges join each predecessor to its successor. The degree is bounded by 80 neighbours, one parent and at most \(L^4\) children; the displayed bound leaves slack and agrees with SA 18680. Distinct same-level nodes are disjoint. Cutting a tree duplicates only an island node, once as a leaf and once as its own root. A drop-out duplicates no earlier node. This proves (5).

The code has logarithmic size at most
\(\log2+v_n(K_s\log K_o+\log K_{\rm st})+\log(3K_f)+p\log(R_n+1)\)
per address. The tube gives \(\log\theta_n\le\log x_n+\log(4/3)\le2\ell_n\), so \(R_n\le L2^r\ell_n^r\) and \(\log(R_n+1)\le c_R\ell_n\). Since \(\ell_n,v_n\ge1\), summation proves (6). Node components and their parent links are recovered from the slices of \(\mathcal A\); the stated interface recovers the remaining record. Normalized frame summation costs at most one per non-frame code, even if only some frame choices give that active set.

Action-label entries retain the as-made holes except for fillings. A later filling either contains a whole surviving earlier component or misses it, by the unique-successor property; a previously healed component is never restored at its old label level. Thus each site counted by \(V_{\rm in}\) belongs to a node of this genealogy, counted at least once in \(v^\natural\). One owning cell with its read collar has at most \((MR_n+2c_{\rm rd}M)^4\le2(MR_n)^4\) sites. Sum with the stated multiplicities to prove (7), then apply the reserve-volume inequality. ∎

**Outstanding — the remaining actual H-G identification.** SA 18692–18701 sketches a finite local code; it does not supply the revised operation's complete selector/schedule/ownership specification. The draft's G9 conditions alone do not select a unique intermediate nest. Nor does SA 18450–18473 verify every enlarged analytic read of the revised construction. These are the two interfaces just stated, to be checked for the actual operation. IN1 does not define its reserve \(v\) to be \(\max(V_{\rm in},n^\sharp)\). The draft's choice of that new definition, and hence its unconditional \(C_v=2\), does not discharge IN1's source-volume clause. If that maximum is separately the specified \(v\), (7) gives \(C_v=2\mu_{\rm rd}\), and gives 2 when each site has one charge per owning cell occurrence.

**Theorem 1 (the complete H-G implication).** Under R, P's nested label updates (no P-gap needed), the ancestral class rule, the scale and admissible-torus floors, and Lemma 7's actual record/ownership and reserve-volume interfaces, IN1 H-G holds with (14), light threshold \(C_g=C_{\rm geo}\), waiting bound \(T_t=C_TR_t\), leaves and cut leaves as above, volume (6) of IN1, and constants (5)–(7). All predecessors have lower levels and successors are unique. One may take
\(c_{\rm ent}=b_{\rm code}+2\log D+\log2\).
Under IN1's separately supplied H-C, its Lemma 8 then uses
\(C_{\rm cnt}=2C_{\rm geo}(5C_{\rm geo}+1)+4C_{\rm geo}^2s_0\).

*Proof.* Lemmas 3 and 5–7 supply each stated clause. A connected address set of size \(a\) has a canonical spanning-tree walk of length \(2(a-1)\), so has at most \(D^{2(a-1)}\) possibilities. Multiply by the non-frame code bound, sum normalized frames, and use \(V^\circ\ge a\); the entropy sum is at most \(\sum_{a\ge1}2^{-a}=1\). This is exactly the input of IN1 Lemma 9. The geometry supplies no failed-test action credit; H-C remains required for Lemma 8. ∎

Determining labels must not replace as-made genealogies in this theorem. Their cells may be fewer, but this does not preserve a recurrence whose right-hand side also shrinks, nor its light-node classification. Draft D1(c)'s stronger transfer claim is removed.

## 4. The main-step box

**Lemma 8 (quiet padding).** In a class component at \(t\), for \(h<i\le t\) put \(H_i=\widehat{X\cap Z_{i-1}^\circ}\). Then
\[
 X\cap\Omega_i^{\circ c}=N_8H_i,
 \qquad N_{10}H_i\subset X\cap Z_i^\circ\subset X,
 \qquad d_\infty(X\cap\Omega_i^{\circ c},X^c)\ge2s_i.        \tag{8}
\]
For a sufficiently large scale floor there is a prepared depth with \(2\le N_t^0\le N_t-1\) and \(s_{k_0+1}=M\).

*Proof.* A failure whose neighbourhood meets this component belongs to it and would be a creation there. There is none. No second predecessor joins it. Equation (1) therefore reduces to the two displayed neighbourhoods; boxing can only enlarge the second. Quarantine prevents a change to these window entries by an intervening ancestral operation. A cell of \(N_8H_i\) is two full cell widths from the complement of \(N_{10}H_i\). This proves (8), including the metric units.

Let \(N=N_t\). By (4), \(s_{h+1}/M\le K_RNL^{1-N}\), which is less than one for all sufficiently large \(N\). Meanwhile \(s_t/M=R_t>1\). The sides in units of \(M\) are powers of \(L\), with consecutive ratios 1 or \(L\). Hence some \(q\), \(h+1<q<t\), has \(s_q=M\). Choose the largest such \(q\) and put \(N_t^0=t-q+1\). Then \(q=k_0+1\), the required equality holds, and \(2\le N_t^0\le N-1\). This gives the range used in CA-I 53765–53774 without assuming that range lemma. Existence of the floor follows from \(N L^{1-N}\to0\), for example by the ratio bound \((N+1)/(LN)\le2/L<1\). ∎

**Definition 4 (the specified loop family and source reach).** For a healed component \(X\), let \(\mathcal B_t(X)\) consist of output datum loops whose complete formation test stencils, including their corners, lie in \(\Lambda^{\rm pr}\); take their union over healed components. This refines the draft's corner-only family because ST1 L669 takes the minimum exponent over the complete stencil. Define the *direct row source* as the output rows reading main-step changed coordinates in that box. Let \(r_{\rm bx}\) be an early bound, in level-\(t\) lattice units, on their endpoint/double-block/stencil reach. Include incident boundary bonds in this bound. Identification of this direct source with the source in the actual BOX response is part of the main-step coordinate/source supply. At a point with no old layer, use the low-layer exponent case only if the specified initial/unfinished formation supply assigns it that case; this is an additional base-formation input, not an inference from nesting.

**Theorem 2 (GEO-box, with its precise split).** Under R, the class rule, (3), that coordinate/source supply, and \(M\ge r_{\rm bx}+1\), every corner of a loop in \(\mathcal B_t\) lies in the old \(\Omega_{k_\sharp+1}^{c}\), with \(k_\sharp=k_0\), and is newly healed to output layer \(t\). The source carrier satisfies
\[
 S_{\rm bx}\subset N^{\rm met}_{r_{\rm bx}}(\Lambda^{\rm pr})\subset X,
 \qquad d_\infty(S_{\rm bx},X^c)\ge2M-r_{\rm bx}\ge M.       \tag{9}
\]
Its entire carrier is therefore in the top output layer, with the fixed enlargement allowed by ST1 Lemma B2. If old layers exist at every stencil point, or the base-formation input just stated applies, ST1 Lemma 10's exponent on \(\mathcal B_t\) is \(\mathcal E=N_t^0-1\).

*Proof.* Inclusion (3) places every chosen stencil point outside the old \(\Omega_{k_0+1}\). Nesting excludes every old layer at least \(k_0+1\); wherever the old layer exists, it is at most \(k_0\). Healing fills \(X\) through the top determining member \(t\). The row read bound gives the first inclusion in (9). Equation (8) at \(i=k_0+1\), whose cell side is \(M\), gives its clearance. Finally ST1 L654–660 defines the healing exponent as \(e_{t-1}+1\); its low-layer case gives \((t-1-k_0-1)+1=N_t^0-1\) at every stencil point, hence also for their minimum. ∎

**Outstanding — BOX-bg and actual source matching.** For every loop outside this specified family, including loops straddling its boundary, ST1 L149 still requires its inherited test (58), converted to output levels. Choosing a smaller \(\mathcal B_t\) does not prove this analytic assertion. Nor does an invariant marginal outside the box alone identify a nonlinear response source. The coordinate/source and base-formation supplies in Definition 4 and the background, current, transport and analytic response clauses of BOX remain inputs. For ST1 B2, the output sequence must also obey its metric layer separation (3), supplied through ST1 GEO and its preparation hypotheses. Equation (9) does not prove that entire hypothesis.

The draft's claim that the four layers have width \(4M/R_{k_0+1}\) in output units is withdrawn. CA-I explicitly makes the final added layer have width \(M\). The source supplies (3); it cannot support that purported thin-margin counterexample. Theorem 2 uses only (3) and quiet padding, so does not need an interpretation of those four layers' width.

## 5. GEO-slot: relative bonds and the outer interface

**Definition 5 (relative bond sets).** Fix one stage enlarging member \(j+1\), and write
\[
 S=\Omega_{j+1}^{\rm old},\qquad
 Y=(S^c\setminus D_{j+1})\cap X,\qquad
 \Omega_{j+1}^{\rm new}=S\cup Y.
\]
Let \(B_i(A)\) be the level-\(i\) bonds incident to the site region \(A\), with one fixed orientation per unoriented bond, and let \(B_i^0\) be all level-\(i\) bonds with both endpoints in \(\Omega_0\). Write
\[
 E=(B_j(Y)\setminus B_j(S))\cap B_j^0,\quad
 C_+=(B_{j+1}(Y)\setminus B_{j+1}(S))\cap B_{j+1}^0,
 \quad F=E\setminus p(C_+),                                \tag{10}
\]
where \(p(c)=b_0(c)\) is the middle fine bond, with the same orientation and transport convention as ST1 F2. CH, including distinct supported pivots, is imported. Use ST1's aligned blocks and its separation, sufficient to keep added-row double blocks in the preceding member. Omit the superscript 0 only when the whole relevant bond star lies in \(\Omega_0\); \(\Omega_0=T\) is not a standing hypothesis.

**Lemma 9 (the removed and added rows).** Under those stage hypotheses, \(E=\Gamma^{\rm rm}\), \(C_+=\Gamma^{\rm ad}\), and \(|F|=|E|-|C_+|\).

*Proof.* At the first stage \(D_{h+1}\supset Z_h\cap X\), so \(Y\subset\Lambda_h\subset\Omega_h\). At subsequent stages the preceding member in \(X\) is \(X\setminus D_j\), which contains \(Y\). Thus \(Y\subset\Omega_j\) in every case. An old level-\(j\) row has an endpoint in \(\Omega_j\) and no endpoint in \(S\); it is removed exactly when an endpoint enters \(Y\). This is \(E\). An added level-\((j+1)\) row has an endpoint in \(Y\), none in \(S\), and both in \(\Omega_0\). It has none in \(\Omega_{j+2}\subset S\), so is exactly a member of \(C_+\). Rows at other levels do not change. CH supplies one distinct pivot in \(E\) per added row. Removing them proves the cardinality identity. ∎

**Theorem 3 (S-flat: conditional outer-interface counterexample).** Suppose \(Y,S\) are unions of aligned \((j+1)\)-blocks, their stage bond stars lie in \(\Omega_0\), and their outer interface is nonempty. Interpret the star at CA-I 74315 with CA-I 159071–159075's incident-bond convention:
\[
 F_{\rm all}=B_j(Y)\setminus p(B_{j+1}(Y)).
\]
Let \(I_i\) be the bonds joining a site in \(Y\) to a site in \(S\). Then
\[
 F_{\rm all}=F\ \dot\cup\ (I_j\setminus p(I_{j+1})),
 \qquad |F_{\rm all}|-|F|=(L^3-1)|I_{j+1}|>0.              \tag{11}
\]
Consequently the literal identity \(F_{\rm all}=F\) in ST1 L153 and `f-meas.md` L40 is false under that reading. This is a geometric conditional counterexample; no assertion of a positive-measure history is needed.

*Proof.* Since \(Y\cap S=\varnothing\), the incident bonds of \(Y\) decompose as \(E\dot\cup I_j\), and the coarse incident bonds decompose as \(C_+\dot\cup I_{j+1}\). For odd centred blocks the middle bond of a coarse crossing lies across that same block interface; the pivot of a noncrossing coarse bond does not cross it. Pivots are distinct. Subtract these two pivot sets to obtain the disjoint union in (11).

One coarse interface bond corresponds to one shared three-dimensional face of two blocks. For each of the \(L\) fine positions in each transverse coordinate there is one crossing fine bond, hence exactly \(L^3\) such bonds. Different faces give disjoint crossing bonds. Therefore \(|I_j|=L^3|I_{j+1}|\), and one pivot is removed per coarse interface bond. This proves (11). A single flat face already gives the positive difference. Count coarse **faces**, not boundary sites: a corner block can have several interface faces. ∎

The convention check does not rely on the draft's exactness shortcut. The CA index directs the small-field bond question to CA-I 45283–45292: the free set on \(\Omega_t\) removes the middle pivots, while both-endpoint, incident and crossing sets on \(\Lambda_t\) are distinguished. CA-I 4334–4373, 4752–4759 and 46065–46076 describe integration over a subset of the free bonds and retention of its complement. CA-I 12721–12723 uses incident bonds for region towers. Bałaban CMP 119, (1.9), independently states the incident convention (local transcription `cmp119.txt` L259–266); CA-I 46959–46962 specifies the middle pivot. Thus the premise in (11) is a real printed convention. It is still necessary to distinguish **the complement of a bond set** from **the incident bonds of a complementary site region** at CA-I 74315. They are different at precisely this interface.

In particular, it is false that the small-field step has already integrated *every* bond incident to \(S\): stored rim variables remain. The draft's Attack 3 cannot resolve the ambiguity by exactness. A both-endpoint convention on \(Y\) is not a repair either; it omits fine removed rows crossing from \(Y\) into \(D_{j+1}\). Formula (10) includes that inner interface and excludes the outer one.

**Corrected GEO-slot (the consumer contract).**

1. **SLOT-ST.** For a specified stored Haar/delta stage, its independent collar slots are exactly \(F\) in (10). Its separately recorded rim slots are exactly those integrated at that stage, disjoint from these collar slots. Every slot has its orientation, level units, initial site and stored transport; all other coordinates are fixed parameters. The constraint equations, pivot assignment and reference are those of ST1 F2. Every physical coordinate is retained or integrated once. This is a statement about the specified stage, with no CA notation in its definition.
2. **SLOT-CA.** To compare a CA presentation, supply a bijection from its actual independent collar and rim coordinates to that disjoint partition, carrying the fixed parameters, transports, constraints and pivots with it. In particular its collar must use the relative set \((B_j(Y)\setminus B_j(S))\setminus p(C_+)\), or explicitly account for the extra coordinates in (11). If an outer-interface coordinate is reassigned to a rim slot, it must be removed from its other occurrence and its original integrand must be carried along. This is more than a change of name.

**Lemma 10 (FM6 and Corollary 14′ with the corrected contract).** Assume SLOT-ST and CH on F2's common admitted constraint chart, with retained rows fixed and real in-fibre reference \(V\). Import F2's bounds \(\|u\|<r_u\), \(\|a\|<r_{\rm sol}\); \(\mathsf C_V\) and \(\Psi_V\) are its linear inclusion and nonlinear constraint chart. Then the intrinsic free coordinate is \(B=u/g_j\), with ST1's positive scale factor \(g_j\), and the full raw logarithm is \(\Psi_V(\mathsf C_Vg_jB)\). Under SLOT-CA the CA coordinate is the same, as FM6 requires. A change of reference uses FM5 on a common chart. Neither contract identifies densities or quadratic forms.

Theorem FM's rewrite additionally imports its complete specified Haar/delta integrand, nonnegative Borel or absolutely integrable, and its passing-chart support, supplied there by ST-test and F4. In Corollary 14′ replace the intrinsic-stage GEO-slot premise by SLOT-ST, retaining **every other declared input of that corollary**, including CI, initial/unfinished base formation, the main-step coordinate/source supply and admitted complex domains. For its separately fixed CA presentation add SLOT-CA and FM-match. For its conditional contours retain ST-test\(^{\rm hol}\), FC-mean-match, FC-test and FC2's uniform analytic majorant.

*Proof.* On the free slots the logarithm is \(u\). On each pivot the prescribed equations are the same small nonlinear equations as F2. Its uniqueness makes their solution \(a_V(u)=\Psi_V(\mathsf C_Vu)\). Under SLOT-CA this also identifies the CA reconstruction; these are exactly FM6's uses of GEO-slot. With the additional measure hypotheses, the supplied coordinate partition permits F3's exact local coarea change in the full stored integrand, with rim variables as parameters before their own integration. Corollary 14′ uses that specified stage, F4's admitted datum, and Theorem FM. Replacing its slot premise as stated supplies those same objects; all its other premises remain imports. ∎

**Outstanding — actual slot matching.** The geometric rows (10) are proved, and (11) rules out one proposed literal identification. Neither the draft nor the cited lines specifies the required disjoint rim correspondence for the revised operation. SLOT-ST's actual storage match and SLOT-CA's boundary reconciliation remain to be supplied. Theorem FM for an already specified intrinsic stage remains a conditional result. The corrected contract does not convert CA-I 81735–81756 or 81829 into a density identity: those lines give the coordinate construction and free-coordinate restriction only. No frozen consumer file is changed here.

## 6. Torus Lift

**Definition 6 (geometric Lift).** A read set has a local lift if it is contained in the image of a coordinate box on the covering lattice of side strictly less than half the torus side, including its entire declared margin. Use one such box for every collection whose coordinates are compared. Projection is injective there and preserves sup-distances. A consistent family of these lifts, where the argument requires overlap consistency, is CLS's geometric Lift. This is distinct from ST1's radius multiplier \(\lambda_\tau=1\), and from equality of companion functions on common lifted regions across different tori. Existence of a local chart proves neither of those function identities.

**Theorem 4 (a sufficient Lift criterion and its limit).** Let the final-level torus side be \(\ell\), at level \(K\). Suppose each required local read set at level \(j\) is contained in a supplied lifted coordinate box of side at most \(A_{\rm rd}MR_j\), with its margin included. Then
\[
                   \ell>2A_{\rm rd}MR_K                  \tag{12}
\]
makes every such box project injectively and preserve its internal sup-distances at every \(j\le K\). For the light skeletons of Lemma 6 take \(A_{\rm rd}>A_*\). For CLS hubs, members and fixed read collars, its lifted side bounds suffice with
\[
 A_{\rm loc}=2C_{\rm isl}L+8+2c_{\rm col}+2c_{\rm rd}.
 \tag{13}
\]
Choose \(A_{\rm rd}\) larger than both these values and the class read-box constant when these are the required local sets.

*Proof.* In level-\(j\) units the torus side is \(\ell L^{K-j}\). Equation (4) gives \(R_j\le L^{K-j}R_K\); thus (12) makes each specified box shorter than half that side. Any two points in it differ by less than half a period in each coordinate, which proves both assertions. A light skeleton has an \(h_0\)-spanning tree; lift it from its root along shortest coordinate increments. The total coordinate span is at most \(h_0(C_{\rm geo}-1)\). Add its \(e\)-neighbourhood. Under (12) this is a box of side at most \(A_*\) cells, so no periodic ambiguity or wrapping remains. This proves the additional requirement of Lemma 6.

For CLS, the hub side is \(C_{\rm isl}LR_j+6\) and the member side is \(2C_{\rm isl}LR_j+6\), in \(M\)-cubes. Adding \(c_{\rm col}+c_{\rm rd}\) cubes on each side is bounded by (13) times \(R_j\), since \(R_j\ge1\). Apply the preceding box argument. ∎

**Outstanding — full CLS Lift.** The theorem is deliberately a criterion on supplied lifted boxes. CLS Lemma 4 itself uses Lift; citing its side estimate cannot prove its own lifting premise. To remove this circularity, one must either supply lifted hub boxes and carry the recursive member construction inside their enlarged charts, or prove those chart spans independently. Moreover CLS Amendment 2 row 10 requires constructed carriers and **complete** read margins as well. Their spans are not bounded by the hub/member side estimates. Arbitrarily long tree carriers on a finite torus need not have a local lift, however large a fixed multiple of \(MR_K\) is chosen. For a finite actual family, (12) applies with a bound for that family's lifted spans; a uniform early \(A_{\rm rd}\) for the full consumer remains an import. This corrects the draft's claim to have established all of Lift from local size bounds alone. No claim about ambient versus in-domain tree lengths is needed for this criterion.

## 7. Action levels inside drop-outs

**Lemma 11 (quiet reach from the core).** In a class window, set \(a=11+b\) and \(C=X\cap Z_h^\circ\). For \(h<l\le t\),
\[
 X\cap\Omega_l^{\circ c}\subset X\cap Z_l^\circ
 \subset\{x:d_\infty(x,C)\le\tau_l\},\qquad
 \tau_l=a\sum_{i=h+1}^ls_i<2aR_hm_l^M.                   \tag{14a}
\]

*Proof.* A cell hull extends a set by at most one cell side; ten layers add ten sides. Lemma 3 adds at most \(b\) more for boxing. Quiet evolution therefore extends the preceding set by at most \(as_i\). Iterate. Since \(R_i\le R_h\) and \(\sum_{i=h+1}^lm_i^M<m_l^M L/(L-1)<2m_l^M\), the last strict inequality follows. ∎

**Proposition 12 (corrected D3).** Suppose a drop-out \((t,X)\), with \(n\) completed stages, stands at time \(k\ge t\). Assume P-gap for the whole window. Define
\[
 w_t=\lceil\log_L(2aR_h)\rceil,\qquad h=t-N_t.
\]
For \(h<j\le h+n\) and \(p\in X\setminus D_j\), the pre-operation membership satisfies \(p\in\Omega_l^\circ\) for every existing \(l\le j-w_t\). If \(j=j_{\rm d}(p)\), then the current action and determining levels satisfy
\[
 j_{\rm a}(p)\ge j_{\rm d}(p)-w_t,
 \qquad n_{\rm a}(p)\le n_{\rm d}(p)+w_t,
 \qquad w_t\le1+\log_L(2aK_R)+\log_LN_t.                 \tag{15}
\]
Here \(j_{\rm a}(p)=\max\{q:p\in\Omega_q^{\rm a}\}\), \(j_{\rm d}(p)=\max\{q:p\in\Omega_q^{\rm d}\}\), and \(n_{\rm a,d}=k-j_{\rm a,d}\). The points in this proposition lie in \(\Omega_h\), so these maxima exist. Points, including plaquette midpoints, use one consistent carrier membership; if the specified carrier is a whole plaquette, apply the point assertion to each of its points.

*Proof.* P-gap and \(C\subset D_{j-1}\) imply \(N^{\rm met}_{m_j^M}(C)\cap X\subset D_j\). If \(j-l\ge w_t\), then
\(m_j^M=L^{j-l}m_l^M\ge2aR_hm_l^M>\tau_l\).
Lemma 11 puts every old hole at level \(l>h\) inside \(D_j\), so \(p\) is outside that hole. For \(l\le h\), use \(D_j\supset C\supset X\cap\Omega_h^{\circ c}\) and label nesting.

To pass to current action entries, consider all other standing marks at \(p\). Older marks inside \(X\) have top below \(h\) by Lemma 4. They lie in \(C\), hence cannot contain this \(p\). A younger mark overlapping \(X\) contains it and has its window bottom strictly above \(t\), so changes no level at most \(j\). Thus only this drop-out can distinguish the two sequences here. Subsequent swallowing is excluded because the mark still stands. This proves the two level inequalities, including the case \(j-w_t<0\), when the lower bound is trivial. If \(j_{\rm d}(p)\) lies outside the drop-out's window, the two sequences agree at \(p\) by the same argument, so \(j_{\rm a}=j_{\rm d}\) and (15) holds with room. The bound for \(w_t\) follows from (4). ∎

**Corollary 13 (cp12's extreme configuration is excluded).** The configuration in `cp12-draft.md` Proposition 8.6 cannot occur above a fixed scale floor under (2), the class rule (Lemma 11, inside a class window) and the **final** gap alone. Full P-gap at lower levels is unnecessary for this conclusion.

*Proof.* Choose an integer \(N_{\rm crit}\) such that for every \(N\ge N_{\rm crit}\),
\[
 N-1\ge1+\log_L(2aK_R)+\log_LN.                         \tag{16}
\]
Such an integer exists: \(N-\log_LN\) is strictly increasing for \(N\ge1\), \(L\ge27\), and tends to infinity. For \(N=N_t\) the right side bounds \(w_t\). If \(n=N\) and \(p\notin D_t\), the final gap implies
\(N^{\rm met}_{M}(C)\cap X\subset D_t\), since \(C\subset D_{t-1}\).
By Lemma 11,
\[
 \tau_{h+1}<2aR_hM L^{1-N}\le2aK_RNM L^{1-N}<M,
\]
where (16) even leaves a factor \(L\) of slack. Therefore \(X\cap\Omega_{h+1}^{\circ c}\subset D_t\), and \(p\notin D_t\) forces \(p\in\Omega_{h+1}^{\circ}\). This contradicts Proposition 8.6's other hypothesis \(p\in\Omega_h^\circ\setminus\Omega_{h+1}^\circ\). The floor \(R_t\ge N_{\rm crit}\) follows from \((\log X_0)^r\ge N_{\rm crit}\). ∎

Proposition 8.6 remains a valid conditional calculation on its stated data. It does not refute the literal H-prof on histories satisfying the geometry above. Neither (15) nor Corollary 13 proves literal H-prof: a logarithmic discrepancy may still be unbounded. The proposed sharpening of a profile estimate additionally reads cp12's profile plateau, bounded increments and global sequence identification; it is not a conclusion of geometry alone. The only genealogy used in Theorem 1 remains as made, and a drop-out contributes only its own mark and code, with no repeated charge for its entire past.

## 8. Constants and supplied definitions

The order is part of every implication above. A requirement on a later choice never defines an earlier constant.

| IN1 position | Choices used here |
|---|---|
| Rows 1–3, before \(\kappa\) | Fix \(r\), the layer numbers, boxing cutoff \(b\), class cutoff 100, selectors and finite record types. Choose odd \(L\ge27\) with IN1's other floors. Then fix the frame constants, \(K_R\), \(e,h_0,C_{\rm geo},s_0,A_*,b_0,C_T,N_{\rm cut},D\). Fix the uniform local interface constants \(K_s,K_o,K_{\rm st},K_f,p,c_{\rm rd},\mu_{\rm rd},r_{\rm bx},a_v,b_v\), and hence \(b_{\rm code},C_v,c_{\rm ent},C_{\rm cnt}\), after any row-3 constants they read. Their dependence on \(L\) is allowed. CLS's \(C_{\rm isl},c_{\rm col}\) precede \(\kappa\); form \(A_{\rm loc}\) and the local torus constant afterwards. An early constant for the additional complete carrier family is not supplied here. |
| Rows 4–7 | Choose \(\kappa\), then \(\bar\kappa\) and the other prescribed rates, then aligned \(M\), including \(M\ge r_{\rm bx}+1\) and the consumers' locality/separation floors. BOX amplitudes may depend on \(M\); they are not geometry constants. IN1 row 7 may list already fixed geometry/code constants without changing them. H-C's gain constants and action allocation remain separate. |
| Row 9 | Increase \(X_0\) for Lemma 1, \(R_j\ge N_{\rm crit}\), the read-collar floor in Lemma 7, and the prepared-depth crossing in Lemma 8, uniformly at all levels. Also retain all IN1/ST1/CLS ceilings. The integer \(N_{\rm crit}\) is chosen from earlier constants; \(w_t\) is a history-dependent quantity, not a fixed constant. |
| Row 10 | Choose the admissible torus with (12) for the specified family and all additional actual read sets. This is a condition on the torus, not an inference from a set's periodic diameter. |

Thus every returned structural constant is fixed before \(\kappa\) and independent of \(M\) and \(\bar\kappa\), **provided the stated local interfaces have that uniformity**. Their existence for the revised construction is among the explicit Outstanding matches, not a consequence of placing them in this table. The floor may depend on later amplitudes. This preserves IN1's rule that a constant precedes each choice it bounds.

The definitions supplied or made explicit in this distillation are: (i) half-open site ownership versus closed metric carriers; three length units and two neighbourhood notations; (ii) as-made nodes, live regions and their distinction from current action/determining labels; (iii) the ancestral quarantine reading and fixed geometry selectors/schedules; (iv) artificial cut-leaf creations, occupied cells, events and the common light threshold; (v) active addresses, the discrete code alphabet, site counts and read-site ownership with charge multiplicity, including the actual reserve-volume comparison coefficients; (vi) the complete-stencil loop family, direct source and its reach; (vii) oriented incident and relative bond sets, outer interface faces, and the disjoint slot contracts; (viii) local covering boxes with complete margins and the full family to which Lift is applied; and (ix) consistent point/carrier membership, action/determining levels and their depths. P-gap and the low-layer base-formation case are exposed **inputs**, not definitions that prove separation or formation. None of these definitions proves analytic realization, a density identity or a new physical premise.

## 9. Source checks and corrections to consumer readings

The complete 506-line pass-1 draft was read. The outline index README, relevant chunk rows and neighbours, and the matching obligations entries were used before source excerpts. The CA 4.12–4.19 index located its bond conventions and preparation statements. These are the load-bearing source checks; a quoted hypothesis remains a hypothesis.

| Checked source ranges | What they supply; disposition here |
|---|---|
| SA 6017–6038, 6095–6140, 17317–17367, 17398–17460, 17494, 17575–17610 | Definitions of the step, fates, marks and class; analytic realization and the meaning of quarantine are separated in §§1–2. The deterministic rules do not imply equality of changed passing branches. |
| SA 17719–17762, 18416–18574, 18576–18603, 18672–18718 | The cut-volume, skeleton, contraction, waiting and entropy arguments. Lemmas 3, 5–7 give explicit hand versions; the literal-code/read interfaces remain named. Cut creations are a geometric convention; their payment is H-C. |
| SA 18877–18888, 23322–23329 | Complete move reads include whole background boxes and class windows; surviving cells follow live ancestry. These support the read qualification and ANC, respectively. |
| CA-I 53735–53892 | Prepared scales, nest, final box and stage updates. The final margin is in level-\(t\) \(M\)-cubes. The low-level tilde convention is not specified as asserted in the draft. The printed margins at 53820–53831 use Bałaban's auxiliary region and are not substituted for SA's \(N_8H_i\) rule. |
| CA-I 4334–4373, 4752–4759, 12721–12723, 45283–45292, 46065–46076, 46959–46962 | Small-field bond sets, conditional integration, retained coordinates and middle pivots. They defeat the “all outer bonds already integrated” argument. |
| CA-I 45962–46032 | The operation class uses an open quarantine window and expressly distinguishes the stronger closed-endpoint reading. SA's stricter mark conclusion cannot be imported from this CA clause. |
| CA-I 74300–74322, 80918–80930, 159060–159090 | Stage collar/rim labels, the strip-change bond set and the incident-bond star convention. The outer-interface theorem is conditional on applying that convention at the stage notation; it is not a finding of failure of the full CA construction. |
| CA-I 81735–81765, 81820–81840 | The scaled free coordinate and nonlinear reconstruction used in FM6. They do not identify a complete stored measure. |
| CA-II 16013–16045; CA-III 3510–3530, 12276–12292 | CLS's cited relative tree lengths do require a tree in the domain. They provide no uniform lift of an arbitrary constructed carrier. |
| Y3 46302–46330, 49131–49168, 52582–52589 | Local pivot/coarea and supported-walk methods cited by the consumers. They do not identify four-dimensional stage slots or supply the missing full read spans. No three-dimensional analytic estimate is imported into a geometry proof here. |

The corresponding consumer passages checked include IN1 L1–90, L145–160, L220–241 and Lemmas 8–9; AG1 L35–72 and L398–418; ST1 definitions, **all of §2**, M2, Lemmas 10, 12, F2–F4, B1–B2, FM1–FM6, Theorem FM and Corollary 14′; CLS §§1–4 and Amendment 2; f-meas L30–46; NL1-L L128–140 and L685–694; geo5c-count in full, its nest-gap premises and the relevant geo-5 arguments; geo-gate and geo5c-gate in full; and cp12 L228–295. The older geometry gates concern supplied formation data. Their verdicts do not establish the unprovided convention matches in this manuscript.

The requested corrections to frozen texts have these dispositions:

* **ST1 L153 and f-meas L40:** the draft's objection is right under the incident-star reading, with the face count (11). A global unconditional claim about CA-I is too strong. Use SLOT-ST for intrinsic stages and SLOT-CA plus FM-match for a CA identification; the rim match stays Outstanding.
* **AG1 L72:** the pointer correction is right. Its surviving-cell use is L414–415, not L412–413. The actual ANC is proved in Lemma 3 on AG1's as-made live regions.
* **The \(C_g\) clash:** the draft is right. IN1's geometry threshold and ST1's formation comparison constant have distinct roles. They are \(C_{\rm geo}\) and \(C_{\rm form}\) here.
* **The three Lift uses:** the distinction is right. Torus embedding, the radius multiplier and common-lift equality of companion functions are different requirements; \(\lambda_\tau=1\) removes no embedding requirement.
* **GEO-box and BOX-bg:** the draft's proposed division is a valid conditional division of work, not a proof of BOX-bg for the loops excluded from its chosen family. For its exponent assertion the full stencil must be controlled, with base formation supplied where the old layer is undefined. Its thin-layer argument is wrong and is removed.

## Result

This text proves (14), the waiting/counting geometry under its explicit class and torus conditions, ANC, and the six GEO-mark clauses under ancestral quarantine with SA's closed lower endpoint. It proves the complete H-G **implication** with explicit local code, source-ownership and reserve-volume interfaces, and GEO-box for a specified complete-stencil loop family with its coordinate/source supply; the exponent also uses the stated base-formation input where needed. It proves a conditional outer-interface counterexample to literal GEO-slot and gives the corrected contracts used by FM6 and Corollary 14′. It proves a local torus-Lift criterion. Under the local nest gaps it proves the logarithmic D3 bound; the exclusion of cp12 Proposition 8.6's extreme configuration uses only the final gap.

Imports are the frame and tube, the adopted step/fate/class rules and selectors, the stated preparation geometry, admissible covering charts, uniform local code/read ownership with charge multiplicity, the actual reserve-volume definition, and, for stage matching, ST1's aligned geometry and CH. The measure/contour and Corollary 14′ imports are retained explicitly in Lemma 10. BOX's analytic inputs, the actual source and base-formation matches and consumer admission/separation remain separate. **Outstanding:** revised-operation realization and quarantine matching; complete actual code/read ownership and reserve matching; the lower preparation convention when deriving P-gap from CA-I alone; actual rim/collar matching and CA boundary reconciliation; BOX-bg/source identification and the needed base formation; and uniform Lift for CLS's full constructed-carrier/read family. No formal scientific status is changed.

Corrections made to the draft are: condition outcome independence on fixed discrete inputs; replace the claimed quarantine equivalence by its explicit ancestral reading and distinguish SA's closed endpoint from CA's open one; retain \(\Omega_0\) endpoint restrictions; expose the missing nest selector and code/read interfaces, including charge multiplicity; avoid redefining IN1's reserve volume; use the tube in the logarithmic code bound; give a sufficient light-node torus floor; remove the determining-count transfer; correct the shifted stage-window explanation; use SA's degree bound \(L^4+83\) (the draft's \(L^4+82\) is a valid bound, but not SA's printed number); remove the unsupported thin-layer calculation; control complete loop stencils and preserve the initial-entry formation obligation; separate full D3 from its final-gap corollary and justify other standing marks; treat \(w_t\) as variable; avoid circular and overbroad Lift claims; count slot discrepancies by interface faces and remove the incorrect small-field exactness shortcut. The pre-\(\kappa\) placement is conditional on uniform interfaces and preserves any earlier analytic dependencies. The five specifically requested consumer corrections have the dispositions above. Frozen consumers and editable prompt files were not modified.

The new work is a check and repair of the pass-1 manuscript, with explicit proofs of steps sketched in SA and a conditional convention counterexample. It is **not yet refereed**. It is research text, not an audit, and grants no status.

## Change log (freeze, 2026-11-05)

Refereed line by line by a fresh Claude session ([geoh-gate](../gates/geoh-gate.md)): first failing step none, 4 findings, all repairable. Applied by the lead (Claude):

1. P-gap distance: the part of \(\Omega_i\) outside \(X\) is covered by the clause \(N_{10}H_i\subset X\) of (8), now cited. This closes the Lemma D0 gap named in cp12-gate.
2. CA-I 53774–53782 gives the one-layer separation for every \(i\in I_M=\{k_0+1,\dots,k\}\); the pair \((k_0,k_0+1)\) is now stated as included.
3. Corollary 13 uses the class rule (Lemma 11), not the quiet rule. Wording only.
4. Proposition 12: the case where \(j_{\rm d}(p)\) lies outside the window (\(j_{\rm a}=j_{\rm d}\)) is now written.

Consumer actions filed by the lead: ST1 Amendment GS (st1-r4.md change log: GEO-slot at L153 is replaced by SLOT-ST, with SLOT-CA plus FM-match for a CA-I identification, as Lemma 10 states); f-meas L40 is read the same way; cp12 Amendment 1 (its H-prof mark updated from Corollary 13 and Proposition 12).

Referee observation, not a defect: Theorems 1–2 and Section 7 also hold under CA-I's open window; only GEO-mark's strict inequality \(s<h\) needs SA's closed rule.

Status: **frozen.** All seven Outstanding marks stand as placed.

