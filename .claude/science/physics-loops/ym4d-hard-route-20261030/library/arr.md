# Arrest machinery: proof lane for complete-account Section 4.27

Provenance: Research text begun 2026-11-05 in the checkout pinned at `907e2acb0`. Source: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, *Yang–Mills LLM experiment*, revision `31a47c543775`, complete account I, Section 4.27, and its outline. Balaban's work is credited wherever used. This note confers no audit or retained status. Proofs must be by hand; source searches and bookkeeping do not discharge mathematical obligations.

## Current checkpoint

This is the sole checkpoint for this lane. The target is the arrest machinery used by the joint induction for T0. The account's restricted conclusions must be distinguished from the stronger conclusions at its stars. In particular, `thm-arrest-theorem` explicitly excludes several raw-stratum members. Proving its room table does not prove those members.

Round 2, at pinned checkout `f414060712ebcceaab028feffd6e0c64bfb2e996`, preserves the round-1 proofs in §§1–13 and continues its Result. The endpoint is still the completion-collar admission lemma. The three new attacks are in §§15–17: prepared geometry and compatible minimizer data; torus transport with the actual label trace; and last-scale integral estimates. Section 18 proves a sufficient quantitative criterion for the collar, including its full physical current and both complex layers. Its seed and layer hypotheses have not been established for every actual completion datum. The frozen results used in this round are compared with those hypotheses in §14.

The exceptional cube move and the completion-consumer covering step remain proved in §§7–8. The later text I:140979–143471 adopts the raised T-datum floor and replaces the raw clause by dated collar allowances. Its displacement and continuation arguments are ported with their hypotheses exposed: its completion-collar corollary is an input, not a proved consequence of its preceding estimates. This is not a proof of the full arrest theorem or T0. No mathematical computation has been used.

## 1. Sources and the port boundary

The round-1 checkout was `907e2acb0e5926a85e72f4d1dd1b37a46aca1cea`. GOAL, FINISH's work rules, `port-map.md` Table 3, and `chain-ca.md` §§3, 7.1 were read first. The repository's science workflow was read from this commit with `git show`; the sparse working tree does not materialize that file. This task writes only this note.

The outline and CA-I were fetched once to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`. CA-II and CA-III were fetched once to `/tmp/arr-research/`. All use revision `31a47c543775` of [Sussman–Alpoge's repository](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775). The authorship credit above applies to every port below. The underlying multiscale spaces and operations are due to Tadeusz Balaban.

| Source | SHA-256 |
|---|---|
| [Outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex) | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex) | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex) | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| [CA-III](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_III.tex) | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

The full-read outline index was searched before source excerpts. The exact CA arrest labels do not occur there. Its closest entries are chunk 16, SA 17433–17459: stopped histories, birth spaces, and matching bare bonds and cube memberships. These outline passages are a sketch and transport requirements, not a completion of the CA raw-stratum argument. The CA full index and the 4.12–4.19 index distinguish operator estimates from application admission. The latter points to CA-I 49495–49547. The earlier reconciliations in `ui.md` and `oc.md` were read as instructions to search for actual proofs, not to trust the heading status.

The textual inventories in `/tmp/arr-research/inventory.txt`, `dependency-labels.txt`, and `*-uses.txt` retain exact label hits and contexts. The statements, their marked steps, and every literal use of the eleven labels in the three parts were read; the combined use-context log is `all-target-uses.txt`. Literal uses occur only in CA-I. This fact alone does not rule out a completion under another name. The later discussion I:139132–140896 and the repair I:140979–143471 were also read, as were the related chain/current passages identified in §§11–12. Searches and read inventories are bookkeeping, not proof evidence.

Most requested blocks have an ordinary proof divided into italic subparagraphs, rather than a separate paragraph headed “Route”. Their actual proposed routes, including the qualifications at the stars, are the routes assessed here. References below identify source arguments by label and bounded line range; no uninspected quotation is used. The supplied Balaban folder does not contain CMP 122a or 122b. For those papers this note ports their statements as formulated in the account; it does not claim an independent check of the originals.

## 2. What the arrest theorem uses

In this section, line numbers are CA-I. The main statement is 137628–137829; its proof runs through 138154. Its assumptions include ten named inputs at 131567–131750 and the hypotheses at 131752 onward. These inputs are premises of the statement, not results created by this note.

| Theorem step | Supplier and exact use | Missing scope |
|---|---|---|
| (A), room and spend table | Frozen-room arithmetic, live-piece increments, stored-term room table, R-layer and T-layer inputs; later `prf-room-regular-zones` and `prf-room-dissolving` supply the detailed rows | The table reads positive-level units. It creates no raw-point margin. |
| (A′)(1), continuation in G1 | Weights/heredity (e4), then (e1)–(e3) and nested cubes | Exceptional C=2 cube enlargement and the completion consumer's cube coverage must be available. |
| (A′)(2), old raw points which enter Ω1 | Raw-stratum heredity and held-raw-points entering estimate | This is a different case from points which stay raw. |
| (A′)(3), unchanged current off Y′ | Density-increase and unheld-raw-points give equality of dated thresholds | No equality at points unheld throughout the birth density in a non-class component, read at a larger density. |
| (A′)(4), gauge on Y′ | The map retains the unitary factor U and its cube gauges | Does not bound the moved A′ or J; completion also requires the index-zero shell. |
| (B), real point | `lem-real-minimiser`, weights (e4) | A′=0 at raw points; the raw gauge and physical-current bounds remain open. |
| (C), legitimate newborn terms | (A) plus the full ambient continuation that (A′) would need | Its stated conclusion is expressly limited by the same two excluded loci. |
| (D), space descent | Frozen room, descent of stage spaces, ambient inclusion | The full ambient rider is a membership premise, not a consequence of the positive-level room. |
| (E), constants | Weights' running maximum/envelope and arrest hypotheses | No later-density replacement of a birth radius is authorized. |

The proof says exactly what is missing at 138062–138095 and 138102–138120. The two locations are (i) the unchanged current on some raw points of Xτ\Y′, and (ii) moved index-zero members on Y′, including re-presentation at completion. The later newborn proof repeats the restrictions at 138824–138850 and 138890. The still later collar construction does address these locations, by changing the raw-domain convention. The distinction matters: the earlier exception is real under its stated dating, while the later convention supplies a different hereditary domain.

## 3. The current probe is already proved

This subsection ports `4.27:lem-current-probe`, I:135723–135840. Its nearby incomplete label describes weights/heredity. The probe uses that lemma's definitions only. It is a complete elementary proof in the source, not a new result here.

Fix a raw bond y, a unit Lie-algebra vector e, and c≥0. Set U=1, A′=0, J(y)=ce, and J=0 elsewhere. All curvature, potential and potential-gradient entries vanish. On Ω1, the current entry vanishes because y is raw. On every cube the identity gauge and zero potential satisfy the gauge clause. At other raw bonds the current is zero. Thus the sole test is

\[
             \eta^3c<T(y).
\]

In K109 with radius γ the corresponding test is η³c≤γ. No divergence condition is imposed on this independent current. Consequently, inclusion of a current ball of threshold T′ into one of threshold T holds exactly when T′≤T. Sufficiency is transitivity of inequalities. If T′>T, choose c=Tη⁻³. This pair passes the new strict bound and fails the old strict bound. Likewise, inclusion into K109's current member holds exactly when T≤γ. If T>γ, choose η³c=(T+γ)/2.

This calculation requires no approximation or enumeration. It is valid for the account's arbitrary complex source, not merely for a physical current J(U). It proves a sharp obstruction to an attempted inference from two radius bounds. It does not establish that the obstructing history or source occurs in a later operation.

## 4. Marked-step ledger

| Requested statement | Marked step and current finding |
|---|---|
| `lem-t-step-layer`, 131633 | 131668–131675: dividing by C_H♯ requires a lower bound. The early repair discussion leaves both choices optional; I:143372 subsequently reads the standing floor at max{C_H♯,1}. Port that later choice explicitly. |
| `lem-weights-heredity`, 132878 | (e3) excludes unheld raw current across density growth; (e4) excludes moved raw members and raw real-point admission. Its positive-level argument also uses the cube lemma. |
| `prf-stage-move-cubes`, 134184 | 134506–134524: the separation estimate alone is insufficient at j+1=k, m=k0+1, C=2. The account's stronger no-creation/no-joining hypothesis supplies the missing property; hand proof in §7. |
| `prf-density-increase`, 135143 | 135403–135435: case (4b) gives a lower bound for the later threshold and an exact equality criterion; it does not prove equality. |
| `prf-index-zero-margin`, 136192 | 136384–136415: moved A′ and J members, completion re-presentation, and raw real-point admission. Equality of source and target thresholds gives no uniform positive room. |
| `prf-ambient-inclusion`, 136490 | 136800–136806: moved raw members remain dependent on §12. The stage-N whole-cube consumer exists for the stated connected-cover domain class, by §8. Its stated (a), full G into K109, is a separate elementary inclusion. |
| `lem-real-minimiser`, 136809 | 137081–137086: index-zero gauge and physical-current bounds. Positive-level regularity and A′=0 do not prove these. |
| `thm-arrest-theorem`, 137628 | The two residual loci and raw real-point clauses listed in §2. |
| `prf-newborn-continuation`, 138485 | Repeats the theorem's two residual loci; no independent completion appears in its proof. |
| `prop-live-piece-bounds`, 138933 | 139078–139085: old raw current outside every live piece at a later density. The positive-level inclusion chain does not supply it. |
| `lem-current-probe`, 135723 | No missing step in its own proof. Ported in §3. |

## 5. Comparison with the closest library arguments

These comparisons were made against the requested statements before treating a local result as a supplier.

| Text | What can be used here | What it does not establish |
|---|---|---|
| [mu](mu.md), §§4–8 | The regular real minimizer, representative and complex continuation in the specified Lemma 4 window; nesting with its hypotheses. | Admission of the completion base on the entire old index-zero collar, uniformly over the completion's complex parameter domain. Being a constrained minimizer alone is insufficient. |
| [oc](oc.md), §§2–4 | The account's earlier own-constant cube proof, using Balaban's CMP 102b minimal-orbit theorem and its admitted real-data radius; transport of a fixed unitary factor under a complex layer. | An arbitrary new real base on an unverified core. Its $B^{(109)}$ is not the $B$ of CMP 119, and its real-data and enlarged-cube hypotheses cannot be omitted. |
| [ui](ui.md), §§1–2 and its port | The later completion of the uniform-increment argument on its specified background charts. | A theorem admitting those charts on the present completion collar. Its differentiated-background inputs, including the printed analytic estimates, remain inputs. |
| [p4-operator](port/p4-operator.md) | The account's A4 operator result on an admitted pair, including independent-current response bounds. | Source or image admission for the R-operation. An operator norm bound does not itself put the base pair in its domain. |
| [p5-induction](port/p5-induction.md) | The A5/A6/A12/A13 induction implications with their stated inputs. | A replacement for the missing arrest-domain implication. Feeding that implication into the induction would be circular here. |
| [pda](pda.md) | Prepared-region geometry, scale conversions and collar placement. | No-joining by itself: that note retains the component-class premises. The generator argument in §7 additionally uses the account's explicit no-joining condition. |
| [dom](dom.md); [st1-r4](st1-r4.md), Lemma 8 and Theorem 14 | Useful ways to distinguish a stopping construction, its admissible frame, and an analytic estimate on that frame. | The exact CA claim. Their GEO/DR, source and roster assumptions, carrier gauges and stage definitions are different. They are not silently substituted for the CA definitions. |

Thus none of these texts proves the whole eleven-statement cluster as used. The strongest appropriate reuse is the account's own later collar construction, supplemented by the two elementary geometric arguments below.

## 6. The T-layer star and the order of constants

### 6.1 The later text makes the proposed repair an actual choice

At I:131668–131680 the proof lists two possible repairs and says neither is yet imposed. At I:143355–143391, specifically 143372, the account subsequently reads the datum floor with
\[
 \widehat C_H:=\max\{C_H^\sharp,1\}
\]
in place of $C_H^\sharp$. This resolves that numerical star **under the later convention**. It is not a proof of the implication from the earlier floor alone.

Here is the missing numerical argument and the rest of its use. Keep the background-layer theorem and the input-pair membership hypotheses of I:131633–131751. With the raised floor,
\[
 \widehat C_H\varpi_k
 \le { (1-\theta_S)\beta\over8}\alpha_{0,k}
 \le {\alpha_{0,k}\over80}.
\]
Since $\widehat C_H\ge1$, $\varpi_k\le\alpha_{0,k}/80\le\varepsilon_\sharp$. The weight
\[
 p(y)=\varpi_k e^{-\delta d^\wedge(y,\mathcal C)}
\]
belongs to the input weight class, equals $\varpi_k$ on the datum support, and gives $\|\mathsf d\|_p\le1$. Apply the Lipschitz layer theorem between $\mathsf d=(0,b)$ and zero, whose layer is zero. It gives
\[
 N_y^\Delta(\mathfrak h)\le B_\sharp p(y).
\]
Since $C_H^\sharp\ge2K_\chi\ge120B_\sharp$, the same floor implies
\[
 2B_\sharp\varpi_k\le {\alpha_{0,k}\over4800}.
\]
This supplies the smallness hypothesis of the recursive-current estimate with cutoff one; hence
\[
 \ell^3|\mathcal J^\sharp[1](y)|\le2K_\chi p(y).
\]
The other moving entries cost at most $3B_\sharp p\le K_\chi p$, and the remaining background-layer entries cost $C_Hp$. Their maximum is $C_H^\sharp p$, exactly the claimed bound. Raising the datum-floor constant does not enlarge the asserted output bound. At real data, constrained criticality gives the vanishing projected current used to identify this layer with Balaban's layer; it does not identify an arbitrary independent source with a physical current.

The proof has not used the full arrest conclusion to establish the pair's admission. Admission is an input to the layer theorem. The later collar induction below is what would supply it at every application.

### 6.2 Constant order retained in every port

Use the account's order, as restated at I:143355–143471:
\[
 L\ \longrightarrow\ \text{profiles}\ \longrightarrow\ \kappa
 \ \longrightarrow\ \kappa_1\ \longrightarrow\ M_1
 \ \longrightarrow\ M\ \longrightarrow\ (q,C)
 \ \longrightarrow\ \gamma .
\]
The fixed response constants, including $C_H^\sharp$, are fixed at their prescribed place before the radius constants and the coupling ceiling. Include the later floor for **both** $C_0^{\rm rad}$ and $C_1^{\rm rad}$. Retain $\mathsf L_0^2\le L/3$, $L\ge8$, $\beta=1/5$, and the original arrest hypotheses. The later raw-collar ceilings include $120\bar\gamma\le1$, $16\bar P^0\le\beta\theta_S$, the response smallness conditions in §10, the real-point ceilings there, and $A_0/A_1\ge c(4,L)$. None is obtained by choosing a constant from the age of an arrest.

For a stored term, membership and its numerical estimate are read at its birth set and birth density. In a floor or ceiling use the account's single-variable envelope, with all functions evaluated at the **same** $t\ge t_\gamma$, followed by one supremum. Replacing a birth radius by the maximum at a later density is not an allowed shortcut. No upper bound on $K$, $N_k$, an arrest age or $\mathsf L_0$ is introduced here beyond the account's stated conditions.

## 7. Hand completion of the exceptional cube move

This fills I:134506–134524 using the account's definitions, rather than strengthening its separation constant. Write
\[
 s=k_0+1,\quad h=k-\check R_k<k_0,\quad
 \xi_i=ML^i\eta,\quad \mathsf S_i=R_i\xi_i.
\]
Let $X$ be the component currently undergoing the operation. All regions in this proof are members of the **retained label in force**, not a union of regions from different historical labels. The precise needed source facts are:

1. The label is nested, and its members above $h$ are produced by the one-step T-construction with no new large-field region inside $X$: I:53737–53831. The no-creation convention means $X\cap\mathcal W_t^\wedge=\varnothing$, not merely absence of a new component with no ancestor: I:49768–49809 and 50316–50408.
2. The arrest setting imposes no joining in this preparatory interval. I:115864–115868 states the condition; I:118394–118406 explicitly reads it as the $N$ preceding density steps and uses it for the retained regions inside the acting component. This is the reading used here.
3. At such a T-step,
   \[
   \Omega_t^c=\bigcup_iG_i^{\sim a_i}\cup\widehat Y^{\sim a_Y},
   \qquad G_i\subset P'\cup Q'\subset\mathcal W_t^\wedge,
   \tag{7.1}
   \]
   where $Y$ is the actual incoming large-field region for that step. At $t\ge2$ the explicit formula is $Q'^{\sim2}\cup P'^{\sim4}\cup\widehat Y^{\sim8}$. Hulls and enlargements distribute over unions and preserve connectedness of a nonempty connected input. Each such enlarged piece contains its input. See I:50145–50313 and 50790–50859.
4. The output $Z_t$ contains $\Omega_t^c$ and $Y$. Enlargements and boxing do not split or erase an input component; their output components contain an input component or a new creation cube. This follows directly from the extensive recursion I:50316–50457 and the component lemmas I:50859–51125.

**Claim.** $\Omega_s^c\cap X$ is empty or one connected component of $\Omega_s^c$.

First, there is at most one component of $Z_s$ inside $X$. Otherwise take two. Under the nested retained sequence each remains inside a unique later component. Both end inside the same component $X\subset Z_k$. At the first level when their containing components coincide, two components have joined inside $X$, contrary to item 2. This argument concerns containment maps of the label in force; it makes no assertion that a completed historical region persists after a reset.

Distribute (7.1) further into the connected sets $c^{\sim a(c)}$, where $c\subset P'\cup Q'$ is a coarse cube, and $\widehat D^{\sim a_Y}$, where $D$ is a component of $Y$. Each of these sets is contained in $\Omega_s^c\subset Z_s\subset Z_k$. If it meets $X$, connectedness puts the whole set in $X$. A piece of the first kind would then put its creation cube $c$ inside $X$, which item 1 forbids. Every remaining piece comes from an incoming component $D\subset X$. There cannot be two such $D$'s in the single $Z_s$-component: that would join them in the T-step generating this very member of the retained label. Thus at most one remains. It is connected, proving the claim.

The account's geometric input says that the components of $\Omega_s^c\cap X$ belonging to these last $N$ steps are rectangular parallelepipeds; this is the input used at I:134487–134495. Consequently the claim makes $\Omega_s^c\cap X$ **one box or empty**. The proof has used both no-creation and no-joining. The size condition on previous components alone would not limit their number.

Now consider the exceptional family $(\mathrm{ii})_s$ at $j=k-1$, with $C=2$. Its old cube $Q$ has side $2\xi_{k-1}$, satisfies $Q\subset\Omega_s$, and holds a cell of $\Omega_{s+1}^c$. Its required new side is $2\xi_k$. The neighbourhood $\mathcal N$ used by the nested-cube lemma lies within $4\xi_k$ of $X$. Distinct $Z_k$-components are at least $\mathsf S_k\ge8\xi_k$ apart, so no other component contributes an excluded cell there. The excluded cells in $\mathcal N$ therefore all belong to the single box just proved. The hypothesis of the nested-cube lemma (a) holds.

For completeness, its elementary geometry is as follows. A cube disjoint from the interior of an axis-aligned box is separated from that box in at least one coordinate. Enlarge the cube in that coordinate away from the box, and enlarge its other coordinate intervals while retaining their old intervals. This produces a cube of the specified larger side containing the old cube and avoiding the box. It stays in the chosen larger neighbourhood, so it meets no other excluded cell. With closed-cell conventions, a common boundary is permitted precisely when no excluded cell interior is shared. If the box is empty, enlargement is immediate. The account's torus and local-cube conventions supply the chart in which this argument is made.

We obtain $Q'\supset Q$, side $2\xi_k$, with $Q'\subset\Omega_s$. It retains the witness cell in $\Omega_{s+1}^c$, hence remains in family $(\mathrm{ii})_s$. Its weight is
\[
 \mathsf L_0^{2(k-s)}
 =\mathsf L_0^2\mathsf L_0^{2(k-1-s)}.
\]
This is exactly the required one-level, one-weight-step enlargement. It does not use the more expensive family $(\mathrm i)_k$.

The rest of the stage-move cube proof, I:134184–134546, now ports without a new hypothesis. Unchanged old families and frozen families use the identical cube. New-shell cores are separated by $11\mathsf S$, greater than the neighbourhood diameter $4.25\xi_{j+1}$. The remaining old-shell cases have $\mathsf S_m\ge C\xi_{j+1}$, or enough separation. The case $C=1,m=s,j+1=k$ uses the aligned-block version of the nested-cube lemma. These alternatives exhaust its listed families. Thus its starred property, and therefore the stated cube-family move, follow on the account's declared retained-label interpretation.

## 8. The completion consumer can contain a whole cube

The missing covering fact at I:136675–136682 is elementary for the class the account states there: $\mathfrak D_m$ consists of connected unions of cubes of the scale-$m$ cover. Stage-$N$ consumer terms are indexed by every such domain meeting the band $Z_k\setminus Z''_k$. The same definition of connected-cover domains appears in the outline at SA:5865–5877; the CA statement is the one used here.

Fix a point $y$ and a whole required cube $Q$, and choose a cell $b$ in the nonempty completion band. Cover $Q\cup\{y,b\}$ by finitely many cover cubes. The cover graph on the ambient torus is connected: a nearest-neighbour cell path gives a finite chain of touching cover cubes between any two chosen cubes. Join each chosen cube to one fixed chosen cube by such a chain. The union $D$ of the finitely many cubes used is connected, contains $Q\cup\{y,b\}$, and meets the band. Hence $D\in\mathfrak D_m$, and $\mathbb C_k^{(N)}(D)$ is a permitted consumer.

This proves existence of an **indexed consumer**, not that its coefficient is nonzero. Nonvanishing is not required by the account's bound for every consumer. No upper bound on the size of $D$ is imposed by the stated class. If a different domain class imposed such a bound, this argument would not apply to it.

The keystone input can now be applied to that consumer. Its gauge on $Q\cap D$ is a gauge on all of $Q$, and is a gauge of the single unitary factor in the presented pair. This fills the positive-level whole-cube use at I:136684–136775, including a cube crossing two of the proof's regions. It does **not** turn a stage space whose clauses start at level one into an index-zero bound on the completion collar.

## 9. What the original weights and density arguments prove

### 9.1 Weight arithmetic and positive-level heredity

Port I:133224–133423. On new shells the weight is $\mathsf L_0^{2(m-k_0)^+}$; on an old shell raised from $m$ to $j$ it is $\mathsf L_0^{2(j-m)}$; untouched shells have weight one. These formulas give
\[
 w_{\mathfrak a}\le w_*(k_a),\qquad
 w_* (j)=\mathsf L_0^{2N_0(j)}\le L^2R_j
 <L^2(L+1)t_j^r.
\]
The declared clock comparison gives $w_*(j)\le\mathsf l(x_n)$ for $n\le j$. With $\mathsf A(t)=Ct^qe^{-t/2}$, $c_\beta=2\log(1+\beta_0)$, and the flow bound $t_m\ge t_j-c_\beta$, differentiation gives
\[
 (\log\mathsf A)'=-\tfrac12+q/t<0,\qquad
 (\log(t^{r+q}e^{-t/2}))'=-\tfrac12+(r+q)/t<0
\]
on the account's chosen range. Therefore
\[
 \bar\alpha_j\le(1+\beta_0)\mathsf A(t_j),\qquad
 \gamma_0^{(k)}=5\max_{j\le k}w_*(j)\bar\alpha_j
 \le5(1+\beta_0)^2L^2(L+1)Ct_k^{r+q}e^{-t_k/2}.
 \tag{9.1}
\]
This tends to zero with the one-variable coupling ceiling. The proof uses the stated flow comparison, not monotonicity of the actual coupling sequence.

At a positive-level point, either the maximum weight is $w_*(k)$ or it belongs to an older piece of density $k_a\le k$. In the first case $5w\alpha_{i,\ell}\le5w_*(k)\bar\alpha_k$; in the second it is at most $5w_*(k_a)\bar\alpha_{k_a}$. This proves the positive-level kernel-radius comparison and $a_\flat\le\gamma_0^{(k)}$. The full ambient rider supplies the raw clauses; they do not follow from these two cases.

For each elementary move, the level rises by $g\ge0$ and the weight ratio is at most $\mathsf L_0^{2g}$. The weakest decay among the direct entries has one inverse power of the local length. Thus for $g\ge1$ the account's radius-ratio input gives
\[
 {w' r_a(\ell+g)\over w r_a(\ell)}
 \le (1+\beta_0)^2\sqrt g\,3^{-g}
 \le {64\over147}<0.436.
 \tag{9.2}
\]
The last inequality uses $\beta_0\le1/7$; $\sqrt{g+1}/(3\sqrt g)<1$, so the maximum is at $g=1$. Curvature, current and gradient have at least this scale decay. At $g=0$ the threshold is unchanged or reduced. Section 7 permits restriction of the later cube gauge to each old cube; the same conversion gives the potential bound and the stronger gradient bound. This proves the positive-level and cube portions of (e1)–(e3), not a bound on the old independent raw current.

### 9.2 The exact raw-current distinction

In the original convention,
\[
 T^d(y)=
 \begin{cases}
 \gamma_0^{(k_{\mathfrak c})},&\text{the oldest live holder is }\mathfrak c,\\
 \gamma_0^{(k)},&\text{no live holder at density }k.
 \end{cases}
\]
The timing lemma ensures that an existing innermost holder persists with its frozen radius while the point stays raw; dissolution puts the point in the averaged region. A point first held at the same density also acquires that density's radius. These facts prove equality of the raw thresholds in the held and same-density cases of the density-increase and unheld-raw-point lemmas (I:135143–135722). On entering the averaged region, the account's scale conversion and held-raw-point lemma give the old raw bound instead.

For a point unheld throughout the earlier density, still raw at a later density, the running maximum only gives $T^{d'}(y)\ge T^d(y)$. Equality holds precisely when no new value in that running maximum exceeds its previous maximum. This is the actual conclusion of case (4b), I:135403–135435. Section 3 proves why the inequality in this direction cannot give the needed inclusion for arbitrary independent currents. No existence claim about a particular RG history is needed, and no counterexample to that history is asserted here.

Likewise, at a point with identical source and target raw thresholds, a bound $|J|<T$ provides no uniform positive displacement allowance: points can approach the boundary. A positive upper bound on an increment is not a proof that an actual increment pushes such a point out, either. The early index-zero-margin proof correctly leaves the moved $A'$, $J$, and re-presentation clauses open. The account's later repair changes the raw domains to reserve actual room. The next section ports that repair explicitly.

### 9.3 Positive-level real admission, including predecessor triples

Here is the port of the nonstarred part of I:136809–137088. Keep its real-point statements off arrested pieces and its real-point assignment theorem with excluded attempts, including that theorem's geometry, data, flow and refinement hypotheses. For a chosen fraction $0<\mathsf m\le1/2$, retain
\[
 C_0^{\rm rad}\ge {2.5A_0\over\varphi_{\rm arrest}},\quad q>p_0,\quad
 1.08{A_0\over C_0^{\rm rad}}t_\gamma^{p_0-q}
       \le\mathsf m\varphi_{\rm arrest},\quad
 K^{\rm own}\varepsilon^{\mathsf l}\le
       \mathsf m\varphi_\flat\alpha_0 .
 \tag{9.3}
\]
All are in the account's order of radius choice and subsequent coupling ceiling.

Off live pieces use the stated real-point inputs. On a live piece at level $\ell$, $A'=0$ makes entries six and seven zero. The retained characteristic functions and CMP 122a (1.24), in the account's formulation, give the reference-background curvature at most $w'\varepsilon_\ell L^{-2\ell}$ with $w'\le w_{\mathfrak a}$. Even the exceptional last-stage multiplier is covered: $3(1-\beta/2)=2.7\le\mathsf L_0^2$. The boundary-response input at its two-layer separation adds at most $(\beta/10)w_{\mathfrak a}\varepsilon_\ell L^{-2\ell}$. Thus entries one and five are at most $1.02w_{\mathfrak a}\varepsilon_\ell L^{-2\ell}$. Their thresholds are at least $\varphi_{\rm arrest}w_{\mathfrak a}\alpha_{0,\ell}L^{-2\ell}$, and their quotient is at most
\[
 {1.08\over\varphi_{\rm arrest}}{A_0\over C_0^{\rm rad}}
      t_\ell^{p_0-q}
 \le \mathsf m.
 \tag{9.4}
\]
For the last inequality use $t_\ell\ge t_\gamma$ and $q>p_0$. At $\mathsf m=1/2$ the radius floor alone suffices because $1.08/2.5<1/2$ and $t_\ell\ge1$.

For the assignment input's other entries, the current determining set has only four kinds of strata: T-strata, completed R-strata, frozen strata, and strata of the running attempt. The account's timing and $N_k>N_0(k)$ put its thin links in the prescribed disjoint blocks. On a block raised by $\nu$ levels, its data estimate is $6\mathsf L_0^{2\nu}\varepsilon_m$; by the weight bound this is covered by $K^{\rm reg}\varepsilon_m^{\mathsf l}$. On the other three kinds use their stated data bounds. Retain the real-averaging smallness condition $3\varepsilon^{\mathsf l}\le c'_2$ and the assignment theorem's flow conditions. Its clause (c), at the last bound in (9.3), now supplies entries two, three and four at fraction $\mathsf m$; its cube clause supplies the actual gauges. The target factor is at least $\varphi_\flat=\varphi_{\rm arrest}$ and its weight is at least one.

For every predecessor triple in $(\Sigma^*)^{\mathfrak a}$, apply the explicitly assumed refinement theorem to $U|_{X'}$ at its own averages. Criticality and uniqueness identify the predecessor minimizer, and its physical current, with gauge copies of these restrictions. The conversion for the second entry is exactly
\[
 L^{-2p}(L^nL^{-p})^{-2}=L^{-2n};
\]
for the fourth entry the extra factor $L^{n-\min\{p,n\}}\ge1$ only enlarges the allowed threshold. Thus the same fraction holds for every such triple; no tail term has been discarded.

The positive-level rider follows directly from these bounds and the cube gauges, without appealing back to clause (B) of the arrest theorem. More generally, the largest enlarged-source factor used in the account is $1.4$, while the rider factor is $5$, giving the stated $5-1.4=3.6$ units of room in weights/heredity (e4). For a local source this verifies the clauses on its own domain; its global extension is supplied by the ambient rider convention, not inferred from local inequalities alone. Nothing in this paragraph proves a raw member. That is the separate port in §10.5.

## 10. Port of the later dated-collar repair

This section concerns I:140979–143471. It proves the implications stated there **with their hypotheses**. In particular, §10.4 identifies where a desired completion estimate is assumed.

### 10.1 The changed domain and the summable reserve

Set
\[
 \Omega_0(\mathfrak B_d)=\Omega_1(\mathfrak B_d)^{\sim},\qquad
 \operatorname{St}(d)=\Omega_0(\mathfrak B_d)\setminus\Omega_1(\mathfrak B_d),
\]
where the enlargement is by one layer of $LM\check R_1$-cubes. A stratum bond has both endpoints in this collar; a pinned plaquette has all four corners there. A bond with an endpoint in $\Omega_1$, or a plaquette with a corner there, belongs to the positive-level part. Use the unscaled entry definitions of I:141019–141045:
\[
 \begin{array}{c|ccccc}
 a&1&3&5&6&7\\ \hline
 Q_a&|\partial\mathbb U-1|&|\mathbb J|&|\partial U-1|&|A'|&|\nabla_UA'|\\
 r_a(0)&\alpha_{0,0}&\alpha_{0,0}\eta^{-3}&\alpha_{0,0}
 &\alpha_{1,0}\eta^{-1}&\alpha_{1,0}\eta^{-2}
 \end{array}
 \tag{10.1}
\]
Each entry is the specified maximum at its attached point. The $Q_7$ stencil is not truncated at the collar boundary: it can read a neighbouring bond in $\Omega_1$. There are no $Q_2,Q_4$ clauses on the raw stratum. The cube clause remains the index-zero instance of CMP 99b (3.35).

For every scaffold date, including dates idle on the particular label, put
\[
 \begin{split}
 c(1;\top)&=0,&c(k;\top)&=\beta2^{-k}\quad(k\ge2),\\
 c(k;l)&=\beta2^{-(h_k+l)},&c(k;L)&={\beta\over4}2^{-(k-1)},\\
 s(d)&=\sum_{e\le d}c(e),&f_0(d)&=4-s(d).
 \end{split}
 \tag{10.2}
\]
Here $h_k=k-\check R_k\ge1$ at an R-site; one class and one window are used per step. The running clock $\check R_k$ is nonincreasing, so the positive integers $h_k$ of distinct R-sites are strictly increasing. The top-date sum is at most $\beta/2$. At each R-site the stage sum is less than $\beta2^{-h_k}$, and summing over distinct $h_k\ge1$ gives less than $\beta$. Completion sites have $k\ge2$, so their total is at most $\beta/4$. Consequently, uniformly in every finite history,
\[
 0\le s(d)<{7\beta\over4},\qquad 3.65<f_0(d)\le4.
 \tag{10.3}
\]
For consecutive dates $d^t<d'$, $f_0(d^t)-f_0(d')=c(d')$. An idle date spends its reserve without changing the label. The raw clause is now
\[
 Q_a(y)<f_0(d)r_a(0)\quad
 (y\in\operatorname{St}(d),\ a=1,3,5,6,7),
 \tag{10.4}
\]
together with the index-zero cube clause. This **replaces** the former raw kernel clause; every stored quantity reads its birth **date**. Positive-level clauses retain their factor five and frozen weights. This is not a derivation of displacement room from the old $T^d(y)$.

### 10.2 The local algebra and scale absorption

The account's left-factor lemma, I:141265–141508, applies to
\[
 e^{i\eta A'_+}U=e^{i\eta h}e^{i\eta A'}U.
\]
On its small logarithm chart, $N_y(h)\le1/40$, $\sup\eta|A'|\le1/80$, and its curvature ceiling $1/10$ give
\[
 |\Delta\partial\mathbb U|\le4N_y(h),\quad
 \eta|A'_+-A'|\le1.06N_y(h),\quad
 \eta^2|\nabla_U(A'_+-A')|\le1.2N_y(h).
 \tag{10.5}
\]
The source proof differentiates the logarithm along $e^{it\eta h}e^{i\eta A'}$, estimates its convergent local power series, and uses the plaquette product rule. The differential remainder costs at most $0.042N_y(h)$; the intermediate gradient and plaquette bounds are $1.11N_y(h)$ and $3.33N_y(h)$. Rounding upward gives (10.5). The unitary factor $U$ and its cube gauges are unchanged. The calculation is on the entire $Q_7$ stencil; it does not paste separately chosen representatives.

The ratio lemma I:141509–141726 gives, for $\lambda\ge1$,
\[
 {\alpha_{i,\lambda}\over\alpha_{i,0}}
 \le(1+\beta_0)^2\sqrt\lambda\le {64\over49}\sqrt\lambda,\qquad
 {r_a(\lambda)\over r_a(0)}
 \le{64\over49}\sqrt\lambda L^{-e_a\lambda},\quad e_a\ge1.
 \tag{10.6}
\]
The last quotient is at most $8/49<0.164$: the ratio of successive $\sqrt\lambda L^{-e_a\lambda}$ is at most $\sqrt2/8<1$.

For a stage at level $j=h_k+l-1\ge1$, the distance from a raw point to the datum crosses at least $j-1$ strata. The contour-price floor gives $\delta\mathsf w_M/4\ge4\log L+1>9$. The scale comparison in that lemma is absorbed by
\[
 3(1+j)2^{j+1}e^{-9(j-1)}\le24.
 \tag{10.7}
\]
At $j=1$ this is equality; each successive ratio is at most $3e^{-9}<1$. Taking the earlier absorption constant $K_\vartheta\ge24C_1/\beta$ gives the useful form
\[
 C_1\delta'_j e^{-\delta d^\wedge/4}
 \le\vartheta\rho_0\alpha_{*,0},\qquad
 \rho_0=\beta2^{-(j+1)},\quad \alpha_{*,0}=\min_i\alpha_{i,0}.
 \tag{10.8}
\]
Using level-zero response and current estimates in the next paragraph is essential. A positive-level estimate would not justify substituting zero.

### 10.3 Stages, averaging, and completion outside the removed collar

For stages, I:141727–142148 explicitly assumes the response theorem, recursive current closure, cutoff and cube-profile estimates, simultaneous-amplitude estimates and their smallness conditions **at level zero**. Port these as inputs. Its constants obey
\[
 K_r=512c_\square c_\vartheta\max\{K_\chi,K_S^bB_\sharp\},
 \quad K_\chi\ge60B_\sharp,\quad
 r\vartheta\le{\beta c_\vartheta\over32K_r},\quad
 R_0\vartheta\le{1\over2K_r}.
 \tag{10.9}
\]
Its response-size estimate and (10.8) yield
\[
 \begin{split}
 N_y(\chi\mathbb H)
 &\le2B_\sharp(20c_\square r+11R_0)C_1\delta'_j
             e^{-\delta d^\wedge/2}\\
 &\le0.0005\rho_0\alpha_{*,0}e^{-\delta d^\wedge/4}.
 \end{split}
 \tag{10.10}
\]
For the second line, substitute (10.9), $c_\square,c_\vartheta\ge1$, $\beta=1/5$ and $K_\chi\ge60B_\sharp$. The coefficient is at most
\[
 {c_\square c_\vartheta/8+11/2\over15360c_\square c_\vartheta}
 \le {45\over122880}<{1\over2000}.
\]
This verifies the source proof's upper rounding by hand. The $120\bar\gamma\le1$ ceiling supplies the chart in (10.5). The recursive-current and cube-profile estimates bound each of the two current contributions by $\rho_0r_3(0)/8$, so their sum costs at most $\rho_0r_3(0)/4$. Equations (10.5) and (10.10) give smaller costs for the other moving entries. The simultaneous-amplitude family has the stronger cost $\mathsf w_0\rho_0/6$. Thus the stage families satisfy
\[
 \Delta_a\le\tfrac14c(d')r_a(0),\quad a=1,3,6,7;
 \qquad\Delta_5=0,
 \tag{10.11}
\]
with the unitary factor and whole-cube gauges retained.

For averaging, port I:142149–142233 and its proof. Section 6 gives the small datum, with the radius floor for both $i=0,1$. The raw-to-datum distance and radius ratio give a factor
\[
 \Lambda_\gamma{(1-\theta_S)\beta\over8}
       \sqrt t\,(2e^{-2})^t2^{-t},\qquad t\ge1.
\]
Its exponential decay absorbs the level quotient. The resulting bound at $d'=(k'+1;\top)$ is
\[
 \Delta_a\le\Lambda_\gamma{(1-\theta_S)\beta\over4}
                  2^{-(k'+1)}r_a(0)
 \le\tfrac18c(d')r_a(0),
 \tag{10.12}
\]
using $\Lambda_\gamma\le1$, $\theta_S\ge1/2$. Again $Q_5$ and the gauges do not move.

At completion, outside the completing components the account represents the pair as identity times layers. It assumes the layer estimate at level zero, the distance
\[
 d_{\rm sc}\ge5R_k+10R_{\min}(k-1-m),\qquad
 e^{-10\delta_1R_{\min}}\le e^{-2},
\]
and the corresponding radius comparison. These turn the far-layer estimate into $\bar P^0 2^{-(k-1)}r_a(0)$, where
\[
 K_W^0=\max\{4,3+18d+2.2K_J\},\quad
 \bar P^0=\bar P\max\{1,K_W^0/K_W\},\quad
 16\bar P^0\le\beta\theta_S .
\]
Thus, on the collar which remains raw after completion,
\[
 \Delta_a\le{\theta_S\over4}c(k;L)r_a(0),\qquad a=1,3,6,7.
 \tag{10.13}
\]
This estimate is linear in each layer's dilation and keeps $Q_5$ and the cube gauges. It concerns the **remaining** collar, not the part re-presented inside a completing component.

### 10.4 The assumed completion-collar corollary

The crucial distinction occurs in hypothesis (e) of the displacement-averaging lemma, I:142269–142291. It assumes a level-zero chain proposition and a collar corollary. The latter says, for every complex parameter point $\varsigma\in\mathfrak P$,
\[
 Q_a(\operatorname{chain}(\varsigma))(y)
 \le {\varphi_\flat\over16}\mathbf r_a(0)
 \quad\left(y\in\bigcup_C\operatorname{Col}(C),\qquad
 a=1,3,5,6,7\right).
 \tag{10.14}
\]
Here $\mathbf r_a(0)$ uses $\alpha_{*,0}$ times the appropriate unit. The chain proposition is assumed to bound entries by functions increasing in the layer sizes $F_s$, with a gauge clause independent of these amplitudes, and to give
\[
 \eta^3|\mathfrak s_{\sigma_s}^{\sharp}[\mathbb H_s](b)|
 \le(3+18d+2.2K_J)F_s(y).
 \tag{10.15}
\]
Hypothesis (f), I:142292–142317, places $\operatorname{Col}(C)\subset Z_{h'}\cap C$ in the core $D_2\setminus B_S$, identifies its base as $(U_2,\mathcal J(U_2))$, and its increments as $\mathbb H_3,\mathbb H_4$. The presentation rotations are trivial there. The proof of conclusion (3) invokes (10.14) at $\mathfrak b_4$; monotonicity in $F_s$ gives it at $\mathfrak b_2,\mathfrak b_3$ and intermediate layer amplitudes. This deduction is valid, but it has **not proved (10.14)**. The rigidity theorem additionally assumes the index-zero cube clause on these same collars at I:142950.

No separately proved supplier of (10.14), with this domain and all these quantifiers, was identified in the checked sources. This reports the source reconciliation, not an impossibility theorem. Section 12 tests three routes to the weaker conclusion actually needed here.

### 10.5 Real points: a separate conditional port

The real-point collar lemma, I:142592–142812, explicitly assumes: the level-zero small-field statement on pinned plaquettes within $2LM\check R_1$ of $\Omega_1$; $A_0/A_1\ge c(4,L)$; the radius comparison; the positive-level real-point bound at fraction $\mathsf m\le1/2$; the physical-current formula; the specified axial cube-gauge estimate; and two coupling ceilings. The local library does not remove these inputs merely by proving existence of a minimizer.

Under them the proof is short. Raw averaging is the identity, so $U=V_0$ on stratum bonds and $A'=0$. The support of the initial characteristic functions gives
\[
 |\partial U-1|<\varepsilon_0
 ={A_0\over C_0^{\rm rad}}t_0^{p_0-q}\alpha_{0,0}
 <0.04\alpha_{0,0}
\]
on pinned plaquettes. The small-field margin also covers a pinned plaquette leaving the operator domain but touching a stratum bond. A nonpinned neighbouring plaquette belongs to level one: the separation from the complement of $\Omega_1$ to $\Omega_2$ exceeds its diameter. Its weight is one since every arrested weight window has $k_0>h\ge1$. Its positive-level bound and (10.6) give
\[
 |\partial U-1|
 \le\tfrac12(1+\beta){64\over49}L^{-2}\alpha_{0,0}
 <0.013\alpha_{0,0}<0.04\alpha_{0,0}.
\]
The covariant divergence defining the physical current has six plaquettes in dimension four. Unitary transport preserves the norm and the traceless projection has norm at most two. Hence
\[
 \eta^3|\mathcal J(U)|\le12(0.04)\alpha_{0,0}
 =0.48\alpha_{0,0},\qquad
 Q_1=Q_5<0.04r_1(0),\quad Q_6=Q_7=0.
 \tag{10.16}
\]
Equation (10.1) fixes the units: $Q_3=|J|$, so $Q_3\le0.48r_3(0)$. The informal description of entry three in the later lemma also mentions $\eta^3|J|$; that factor must not be inserted a second time.

An index-zero cube lies in the source's $B^0(\Lambda_0)\cup B^1(\Lambda_1)$ region (I:142775–142783), so its plaquettes are pinned or of level one. Every plaquette in it therefore has the preceding $0.04\alpha_{0,0}$ bound. The lemma's **assumed** axial-gauge estimate, on cubes of at most $10M$ sites per side, gives
\[
 \eta|A|\le3M\alpha_{0,0},\qquad
 \eta^2|\nabla A|\le6M\alpha_{0,0}.
\]
Its two ceilings $\sup24M\mathsf A\le1$, $\sup6\mathsf A\le\alpha_0^{(99)}$, with the source's offset range for $t$, put these bounds in the index-zero cube class and ensure the smallness needed for that gauge estimate. Thus the real-point inclusion follows **under those inputs**, with at least $3.1r_a(0)$ to spare by (10.3). This proves neither complex completion-base admission from a real bound nor the gauge input on a different, unadmitted base.

## 11. How the collar lemma would close the arrest uses

This is a conditional implication. Keep the original named inputs of the arrest theorem, the later raw-response and real-point inputs specified in §10, and suppose the completion-collar admission lemma in the Result is proved. No conclusion of that lemma is included among these other inputs.

First prove set heredity, before applying a response theorem. The elementary set moves never lower a level. Only completion changes the raw collar. If $Z_L$ is the union of completing components, its one-layer enlargement lies in $Z_L\cup\Omega_1$ by component separation. Distributing enlargement over unions gives
\[
 (\Omega_1\cup Z_L)^\sim\setminus(\Omega_1\cup Z_L)
 =(\Omega_1^\sim\setminus\Omega_1)\setminus Z_L.
 \tag{11.1}
\]
Thus the later collar is contained in the earlier collar, and every removed point enters the averaged part. This is the geometric argument of I:143016–143050.

At points positive at both dates, (9.2) proves threshold monotonicity. At points raw at both dates, (10.3)–(10.4) prove it. A raw point newly averaged by completion has new weight one. Equation (10.6), at its new level $\lambda\ge1$, gives
\[
 5r_a(\lambda)\le {40\over49}r_a(0)
 <3.65r_a(0)<f_0(d)r_a(0).
 \tag{11.2}
\]
Cube heredity uses §7 and the account's index-zero conversion at newly averaged points. Hence, with the later convention,
\[
 \mathfrak G(\mathfrak B_{d'})\subset\mathfrak G(\mathfrak B_d)
 \subset\mathfrak K_{109}(\mathfrak B_d;\gamma_0^{(k)}).
 \tag{11.3}
\]
For the second inclusion, positive-level products are bounded by (9.1). At raw points $f_0\le4$ and $4(1+\beta_0)<5$, so the raw bounds are inside the birth kernel radius even if its running maximum starts at level one rather than zero. The smallness and cube hypotheses are those of the later rigidity theorem; they cannot be dropped from this inclusion. The same comparison gives $a_\flat\le\gamma_0^{(k)}$.

Now apply the displacement estimates. On a point remaining raw for consecutive dates $d^t<d'$,
\[
 \begin{split}
 Q_a(\Phi p)(y)
 &\le Q_a(p)(y)+\Delta_a(y)\\
 &<\bigl(f_0(d')+c(d')\bigr)r_a(0)
 =f_0(d^t)r_a(0).
 \end{split}
 \tag{11.4}
\]
Equations (10.11)–(10.13) spend only a fraction of the available $c(d')$. On the part removed at completion use the Result lemma instead. The stronger assumed corollary (10.14) would suffice since
\[
 (\varphi_\flat/16)\mathbf r_a(0)\le r_a(0)/16<f_0(d^t)r_a(0),
\]
but this much extra room is unnecessary for the raw rider. The index-zero gauge must hold on whole required cubes, including their boundary stencils; pointwise estimates alone do not prove it.

This proves the missing raw part of weights/heredity (e4), of ambient inclusion, and of index-zero margin, on the **later** domains. Real-point admission follows from §10.5. The original raw-current equality of case (4b) is not used or asserted.

The remainder of the main theorem follows by the account's room argument. To make the dependency explicit, its positive-level spend/room ratios, I:137829–138061 and the detailed follow-ups I:139724–140896, are:

| Zone | Operations | Maximum spend/room ratio used |
|---|---|---|
| Z1 | O1, O4; O4′; O2; O3 | $1/2;\ 1/48;\ \theta_S/4;\ 1/8$ |
| Z2 | O2; O3; O4 or O4′ | $1/4;\ 1/8;\ 1/36$ |
| Interior Z2° | Maps with no datum there | $0$ |
| Z3(a) | The account's first dissolving-piece case | $1/12$ |
| Z3(b) | Raised level with frozen factor at least $0.78$ | $(64/147)/0.78<2/3$ |
| Z3 at completion | Completion layer | $1/8$ |
| Z4′ | Re-presented core | $1/16$ |

The frozen-room lemma supplies each denominator. The live-piece increment and stored-term lemmas supply each numerator in the unit of the old clause. In Z3(b), use (9.2) and the factor lower bound before dividing, rather than silently discarding the frozen weight. In Z4′ the core base costs $1/64$ and the three prescribed increments cost $3/64$; their sum is $1/16$. These are positive-level and cube inputs on their stated domains. They were never a substitute for the index-zero estimate.

For (A′), use the global presented field of the operation, together with its retained unitary factor or its one re-presented base. Its agreement with the input off $Y'$ uses the locality and zero-data property invoked at I:136759–136768; it is not inferred from exponential decay and is not obtained by truncating a response field. The cube argument in §8 ensures that a cube crossing the keystone regions has a single consumer gauge. It is not legitimate to paste arbitrary field values across a stencil. The independent current, in contrast, has no derivative or divergence clause in this kernel class. Off the map's domain one can retain the input current on $X_\tau\setminus Y'$ and set it to zero at permitted points off $X_\tau\cup Y'$, exactly as the account's continuation does. Equation (11.3) now controls even the formerly excluded unheld raw points of $X_\tau\setminus Y'$ at the term's birth date. Equation (11.4) and the Result lemma control the moved raw points. The continuation therefore belongs to the full birth rider.

For (C), induction over dates gives legitimacy of every newborn composite: the image lies in the stored term's domain, the map and stored term are holomorphic there, and
\[
 \sup_{\text{new domain}}|\tau\circ\Phi|
 \le\sup_{\text{birth domain}}|\tau|.
 \tag{11.5}
\]
The original numerical bound is retained. Changing the radius occurring in an old bound to a later radius is unnecessary and unjustified. Locality makes the value independent of the chosen extension off $X_\tau$.

For (D), the frozen factor is the ordinary stage factor minus the same sum of range deductions throughout a live piece. In a consecutive-date inclusion these common deductions cancel. Factor positivity and the account's stage descent then give the direct-clause inclusion; (11.3)–(11.4) supply the ambient part. At dissolution use the actual frozen family before the reset and the completion map, not the already reset determining set as its target.

For (E), (9.1) and §6.2 give the single-variable ceilings at the fixed birth density. They introduce no dependence on age. The proposition on live-piece bounds then follows from (11.5) for all terms and from the arrested-source inclusion. It does not imply a bound on ordinary unfrozen spaces: the account explicitly permits $\varphi_\flat\mathsf L_0^4\ge1.5$, so removing the frozen weight can enlarge the domain.

This gives a noncircular order for the conditional proof: geometry and threshold heredity; input admission; response estimates and completion-collar admission; global continuation; composition and preservation of stored bounds. It is the later rigidity argument with its missing supplier exposed.

## 12. Round 1: three attacks on completion-collar admission

The object throughout this section is the same: the actual completion presentation on the old raw collar of a completing component, for every admitted complex source and every parameter in its prescribed domain. The target is the weaker bound in the Result, not the stronger $1/16$ estimate for convenience. These attacks do not purport to be independent proofs.

### Attack 1: transfer the regular real completion base to the old raw units

On the core the chain has real base $(U_2,\mathcal J(U_2))$ and layers $\mathbb H_3,\mathbb H_4$, with trivial rotations after $\mathfrak b_2$. This suggests using mu for the minimizer, oc for its gauge, and the layer bounds to finish.

The useful numerical transfer can be proved. Put $u_a(0)=r_a(0)/\alpha_{i,0}$, with $i=0$ for $a=1,3,5$ and $i=1$ for $a=6,7$. Thus $u_a(0)$ is respectively $1,\eta^{-3},1,\eta^{-1},\eta^{-2}$; this keeps the plaquette entries dimensionless. Suppose, on the **whole read-set required**, a base entry at an admitted positive level $\mu$ has the bound
\[
 Q_a(U_2)\le K_a\varepsilon_\mu u_a(0)L^{-e_a\mu}.
\]
Its own radius is $\alpha_{i,\mu}u_a(0)L^{-e_a\mu}$. Dividing by $r_a(0)=\alpha_{i,0}u_a(0)$ and using the same-index radius comparison gives
\[
 {Q_a(U_2)\over r_a(0)}
 \le {64\over49}K_a{\varepsilon_\mu\over\alpha_{i,\mu}}
                       \sqrt\mu\,L^{-e_a\mu}.
 \tag{12.1}
\]
For $\mu\ge1$ there is uniform scale gain, at least the $8/49$ factor of (10.6). If this is at most some $\epsilon_b<f_0(d^t)$ and the actual chain increments cost at most $\epsilon_h<f_0(d^t)-\epsilon_b$, the triangle inequality proves the entry part of the desired lemma. If the same real base has an oc-admitted gauge on each enlarged cube and the layers retain its unitary factor, the gauge part follows too. Thus this route has a concrete sufficient condition; it does not need a restriction on age.

The attempted application fails at the antecedent, not at (12.1). CA-I 92420–92467 identifies $U_2$ as a constrained minimizer and assumes that the core presentation equals a real order-$h$ configuration independent of the complex source. It does not by that identification prove that its actual datum satisfies the small-field and enlarged-cube hypotheses of mu/oc on this entire old collar. The admission issue is acknowledged nearby at I:94185–94240: the required real-core kernel membership is imposed there, beyond what the cited CMP 122b statement says on the support of its cutoff. Repeating “order $h$” does not establish that membership.

Nor can one use $U=V_0$ from §10.5. That identity is for the minimizer of the determining set that still pins those raw bonds. The completion core uses the new $\mathbf B_2$ constrained problem. The equality with $V_0$ on the old raw collar is not among its stated identities. At an actual index-zero datum (12.1) would also have no positive-level scale gain. The needed conclusion is therefore a quantitative admission statement for this particular base and these whole cubes, plus the actual layer budgets; it is not supplied by uniqueness of a minimizer.

**Exact failure:** the admissible-real-data and whole-cube hypotheses needed to start the transfer have not been established for $U_2$ on $\operatorname{Col}(C)$. This does not refute their truth.

### Attack 2: obtain the missing current bound from criticality and localisation

Use the current-localisation lemma I:92401–92514. Its proof of criticality is valid finite-dimensional linear algebra. If $Q=Q_{\mathbf B_2}$, stationarity against every $\delta A\in\ker Q$ gives
\[
 J_2\in(\ker Q)^\perp=\operatorname{ran}Q^*,\qquad
 J_2=Q^*\lambda_2,\quad
 \lambda_2=(QQ^*)^{-1}QJ_2.
 \tag{12.2}
\]
The cut-localisation argument then writes the propagated current as
\[
 \begin{split}
 \mathbf G''(\sigma)\hat{\mathcal J}^{\mathfrak b_2}
 ={}&\mathbf G''(\sigma)
       [1_{(D_2^\circ)^c}\hat{\mathcal J}^{\mathfrak b_2}+r]\\
 &+[\mathbf G''(\sigma)-\mathbf G''(1)]
       Q''^*(\lambda_2|_{D_2^\circ}),
 \qquad \|r\|_\infty\le C_Q\|J_2\|_\infty .
 \end{split}
 \tag{12.3}
\]
The Green kernel decay and the distance to the cut provide the claimed small response layers in the deep region. This is useful for their increments.

It cannot bound the unpropagated $Q_3=|J_2|$ by itself. Indeed the same input explicitly gives $G''Q''^*=0$. Fix any $\lambda$ with $Q''^*\lambda\ne0$ and set $J_t=tQ''^*\lambda$. Then
\[
 G''J_t=0\quad\hbox{for every }t,\qquad
 \|J_t\|_\infty=|t|\|Q''^*\lambda\|_\infty .
 \tag{12.4}
\]
Thus no bound on $G''J$ controls the constraint-current component. In (12.3) the boundary error bound still contains the very $\|J_2\|_\infty$ one is trying to estimate; the formula for $\lambda_2$ does not remove it. The same defect persists for an independent current even if a physical current is small.

This is an exact obstruction to that proposed inference, not a counterexample to a physical Yang–Mills minimizer: the $J_t$ need not be physical currents of actual admissible configurations. A proof could still bound the multiplier from the admitted real datum or a local action estimate. Neither is provided by the localisation identity.

**Exact failure:** criticality eliminates the current only after projection; the needed raw clause bounds the full current. This route lacks an estimate of the constraint multiplier or a direct base-current estimate.

### Attack 3: continue from real collar data using the analytic charts

Suppose first that all real completion parameters had the desired collar estimate. Try to continue it to the complex parameter domain $\mathfrak P$ using mu, ui and the operator theorem. Those results provide holomorphic maps and quantitative bounds **on their admitted complex charts**. They do not say that the present recursively constructed completion stays on those charts just because its real slice does.

The distinction can be checked without a computation. Let $T_n$ be the Chebyshev polynomial, so $T_n(\cos\theta)=\cos(n\theta)$ and $|T_n(x)|\le1$ on $[-1,1]$. For $r>0$ put $\rho=r+\sqrt{1+r^2}>1$ and $w=i\rho$. Since $(w+w^{-1})/2=ir$,
\[
 T_{2m}(ir)=(-1)^m{\rho^{2m}+\rho^{-2m}\over2}.
 \tag{12.5}
\]
These entire functions are uniformly bounded on the real interval but unbounded at the fixed complex point $ir$ as $m$ increases. A real bound plus holomorphy therefore supplies no uniform complex estimate. An identity theorem concerns equality of functions; it cannot turn the real inequality into a complex norm bound.

The repair would require a uniform complex chart, a bound on that chart and an inclusion of the actual parameter domain in it. Here these are substantive admission hypotheses. CA-I 94185–94240 even requires the real-core hypotheses at perturbed real data. The conditional local-layer estimates do not construct the missing base chart.

I checked the plausible later candidates rather than relying on their headings. CA-III 9458–9565 gives chain slices under its own seed-tube and zone hypotheses. CA-III 18854–18950 explicitly has no zone-zero table clause and uses a standing core regularity hypothesis. CA-III 65662–65825 concerns a different chain of hatted competitors between runs, not the presented configuration on the completing collar. None supplies the desired full complex collar membership. The semantic current-bound occurrences at CA-I 94256 and 94996–95025 concern the local presented increments and their input classes; the constant $3+18d+2.2K_J$ is not, by itself, a proof of (10.14).

Shrinking $\mathfrak P$ after the fact would not complete the requested result: stored terms and later Cauchy estimates read their prescribed birth domains. It would be a different statement, whose compatibility with those uses would still have to be proved.

**Exact failure:** real admission and analytic continuation do not supply the uniform complex-domain inclusion. The applicable chart bounds require the admission being sought. This attack does not show that such an inclusion is false.

## 13. Round-1 disposition of the requested statements

“Conditional” here means a mathematical implication from the enumerated source inputs, with the unresolved input identified. It does not mean that an audit has accepted those inputs.

| Statement | Disposition in this note |
|---|---|
| T-step layer | The numerical star is closed using the later adopted maximum floor (§6). Pair admission remains the layer theorem's hypothesis, supplied in an arrest induction only when the rider argument is available. |
| Weights/heredity | The weight envelope and positive-level/cube clauses are ported (§§7, 9). The original exception for the unheld raw current is preserved. Full heredity on the later domains follows conditionally by §11. |
| Stage-move cubes | The exceptional $C=2$ step is proved from the account's retained-label no-creation/no-joining conditions (§7). No larger separation hypothesis is added. |
| Density increase | The stated held/same-density conclusions and case (4b)'s exact equality criterion are retained (§9.2). The later repair uses monotone dated thresholds instead of claiming the missing equality. |
| Current probe | Complete hand port in §3. Its witnesses test source-space inclusion; they are not asserted to be actual RG outputs. |
| Index-zero margin | The old equal-threshold argument supplies no positive room. The later reserve proves stages, averaging and the remaining completion collar under their listed raw-response inputs (§10); the removed collar is the Result lemma. |
| Ambient inclusion | Full-rider to kernel inclusion is proved at the fixed birth radius; positive-level maps use §§7–8 and the named inputs. Raw image admission at completion is still conditional. |
| Real minimizer | Positive-level admission, all predecessor triples and the margin fraction are ported in §9.3. Its later raw-point proof is ported in §10.5 with the small-field and cube-gauge inputs explicitly retained. It is not an arbitrary-complex-source theorem. |
| Arrest theorem | Its restricted positive-level claims and room table have the dependency proof in §11. A full result on the later collar domains additionally requires the Result lemma and the other explicit later inputs. No unconditional full arrest result is claimed. |
| Newborn continuation | Once the full birth-domain inclusion holds, holomorphic composition and the original supremum bound give the result (§11). The raw completion hypothesis cannot be omitted. |
| Live-piece bounds | The same inclusion preserves old bounds on arrested spaces (§11); it does not allow the ambient rider or frozen weights to be removed. |

The later collar construction is therefore not merely a stale incomplete label followed by an unconditional proof. It is a substantive repair of the domain convention plus a conditional argument whose completion-collar supplier must still be proved. The elementary additions in §§7–8 and the tests in §12 are the hand work in this note. The ported construction and estimates remain credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and to Tadeusz Balaban for the underlying multiscale theory.

Verification limits: source identities were checked against the hashes in §1; bounded source excerpts and literal target uses were inspected. Mathematical arguments here were checked by hand, without simulation, interval calculation, a solver, or a run discharging a step. This note has not received an independent mathematical review. No claim is made to have checked all of T0's imported analytic inputs or the unavailable original CMP 122a/122b texts.

## 14. Round 2: the new inputs and the later-source check

This round read the existing note whole before continuing its Result. The required GOAL/FINISH passages, port map and chain map were read before the new work. The outline index, including neighbouring rows in chunks 9 and 16 and the obligations file, was consulted before the relevant outline excerpts. The 4.12–4.19 index distinguishes the prepared geometry, real-background hypotheses and analytic supply; its CA-I references 45162 and 49495–49546 are particularly relevant here. The already fetched outline and CA-I were reused. CA-II and CA-III were read from copies in the task-created folder /tmp/arr-round2; their hashes agree with §1. References below are to the credited authors' text at the same revision, not to a later revision.

The eleven-statement map in §§2–4 and the conditional closure in §11 are unchanged. The new question is whether the results now available in this checkout supply the single missing collar implication. Their precise contributions are:

| Input now available | What can be used here | Condition still attached |
|---|---|---|
| Frozen [pda.md](pda.md), especially §§4–5 | The specified prepared nests and componentwise stopped prefixes satisfy (A1), including partitions, gaps, gluing and the level-zero hull. In the acting regime \(h\ge1\), \(\Omega''_1=\Omega_1\). | This is a theorem about domains. It supplies neither (A2) nor real datum tests, a gauge, a current estimate or analytic admission. |
| Frozen [mu.md](mu.md), §§4–6 | A uniform complex chart for its window data, real restriction to the inner problem with its own subaverages, uniqueness in Balaban's regular variational class, and the resulting complex identity. | All determining rows, seam rows, the fixed action boundary and chart inclusion must match. The inner datum is the actual average of the outer minimizer; it is not independently prescribed. |
| Frozen [oc.md](oc.md), §§2–5 | The real minimizer has the stated cube gauges with its own small-field constant; a complex left layer retains them because it retains the same unitary factor. | The real datum and enlarged cubes must be in the theorem's class. The theorem does not identify a newly minimized completion field with that minimizer. |
| Checked [p7-torus.md](port/p7-torus.md), A14 | The specified local terms and operations agree under matching complete label traces, local fields, integration variables and footprints, on their admitted analytic domains. | Its H6a completion identity and H6b analytic extension remain inputs. The empty-trace comparison has its stated range; it is not a regularity theorem for arbitrary nonempty traces. |
| Frozen [lsc.md](lsc.md), round-2 Result | Bounds on the vacuum-normalized partition function and its sourced version, uniform in cutoff and physical torus at fixed target coupling and omitted-step prescription. | Its RG representation, real-background and sourced majorant hypotheses remain. The vacuum constant need not be uniform. These are integral bounds, not bounds on each integration datum. |

The distinctions in this table also agree with the supply conditions in [p4-operator.md](port/p4-operator.md), A9: prepared geometry and admitted background are separate hypotheses. The induction in [p5-induction.md](port/p5-induction.md) does not prove its own arrest input. The older comparisons with ui, dom and st1-r4 in §5 are retained at their stated scope.

The later passages were checked for a completion before trying a new proof. In I:142269–142291 the level-zero chain proposition and collar corollary are expressly inputs. At I:142563 the completion proof invokes that corollary. I:142950 again assumes the completion-collar cube clause. The parameter remark I:143355–143424 lists a collar ceiling but also retains the other hypotheses of those statements; listing a ceiling is not a derivation of the field estimate whose supplier is missing.

Two further later candidates do not change this. II:25160–25200 uses a tube statement in a sourced collar estimate. III:18854–18952 concerns a refinement with its own subaverages and standing core regularity, and contains no zone-zero table clause. III:51104–51185 does prove that the collar is empty for aligned labels; that useful restricted conclusion is ported in §16 below. It does not cover all labels in the arrest theorem. Thus the candidates inspected do not turn this particular incomplete step into a stale label of the kind resolved in ui or oc.

## 15. New attack 1: identify the completion seed by prepared geometry and minimizer nesting

Round 1's first attack tried a numerical transfer from a regular positive-level base. The new attempt is to *identify* the actual base with an already admitted one, using the newly proved prepared nests and mu's exact restriction identity. If successful, this would supply the missing antecedent of that transfer.

Write \(V_2(\varpi)\) for the actual real datum of the completion minimizer
\[
 U_2=U_{\mathbf B_2}(V_2(\varpi)),\qquad
 \mathbf B_2=\mathbf B''_k\cup
       \mathbf B_h((\Omega''^{\sim}_{h+1})^c).
 \tag{15.1}
\]
Here \(\varpi\) denotes the real variables retained in the presentation, not an extra complex source. This notation names the datum; it does not assign it a new value. The defining constrained problem is the one in I:92418–92427. The current-step variables include \(B,V''|_{D_2},V_h\) and the inner tree variables; they are left real and unrotated, I:78445–78545. The parameter convention I:93510–93670 explicitly includes \(\operatorname{supp}\Pi\) as a factor of \(\mathfrak P\); a statement for every point of that domain is already uniform in these real variables. In particular, admission of the independent complex source pair is not itself a bound on all these real data.

There are two possible exact identifications to try.

### 15.1 Restrict an admitted ancestor minimizer

Here is the valid implication behind this attempt. Let \(R\) be a real field on the full action domain of (15.1), in its regular uniqueness class. Suppose:

1. \(R\) has exactly the datum \(V_2(\varpi)\) on every determining row of \(\mathbf B_2\), with the prescribed seam convention and root normalization.
2. \(R\) is critical against every constraint-preserving variation for this action, with its actual fixed boundary.
3. The datum and geometry satisfy the hypotheses of the regular minimizer theorem used in mu §5. For an inner restriction, its window and fixed-shell hypotheses also hold.

Then \(U_2\) and \(R\) lie on the same regular critical orbit. If they have the account's common axial normalization, they agree. Curvature and physical current therefore agree on every full stencil contained in the comparison domain. If \(R\) has the required gauges on whole enlarged cubes there, these are gauges of \(U_2\) as well.

**Proof.** Apply the real uniqueness statement ported in mu §5, which is Balaban's uniqueness in the regular variational space. Condition 2 puts \(R\) in that statement, rather than merely in the constraint fibre. The minimizer \(U_2\) is in it by condition 3. Uniqueness gives the orbit equality. The root and tree equations remove the residual gauge exactly as in mu (5.5). The asserted transfers follow from equality of the fields on all bonds they read. If only orbit equality is needed, use the one real gauge on the whole comparison domain; the norms are invariant under it. This proves the implication on that theorem's input class; it does not enlarge mu's class of comparison domains.

Mu supplies conditions 1–2 for a particular construction: the inner data are the outer minimizer's **own** subaverages,
\[
 V_{\rm inner}=M_{\mathcal T}(R|_Z).
 \tag{15.2}
\]
Its refinement is checked on the same outer action domain, and the fixed shell then proves the change-of-action identity in mu (5.4). Its complex chart estimate is
\[
 \|B_{\mathcal T}(D)\|_\infty
 \le C_AK\|D\|_\infty,\qquad
 \delta<r/2,\quad K\delta<a_{98}/2,\quad C_AK\delta<r/2.
 \tag{15.3}
\]
These statements pay for all rows and every inner carrier in that window. They do not replace the inner datum by an arbitrary nearby real datum.

Pda now proves the geometric (A1) part for the *actual* prepared nest and its prefixes. It does not prove the identity
\[
 M_{\mathbf B_2}R=V_2(\varpi)
 \tag{15.4}
\]
for an admitted ancestor \(R\), the corresponding fibre inclusion, or the action-boundary comparison. There is also a distinct determining-set issue: the union sign in (15.1) denotes the graded splice described at I:92516–92532. It must not be treated as the union of two lists of simultaneously imposed constraints. That passage compares the blocks away from the cut and replaces rows in its graded layer. It does not state (15.4).

Even preservation of coarse data does not replace the criticality check. For a hand test, minimize
\[
 E(x,y)=x^2+y^2.
\]
The fine fibre \(x=a,\ y=0\) has minimizer \((a,0)\). It has coarse datum \(x+y=a\), but the minimizer on this latter fibre is \((a/2,a/2)\), since
\[
 E(x,a-x)=2(x-a/2)^2+a^2/2.
\]
At \((a,0)\) the allowed coarse variation \((1,-1)\) has first derivative \(2a\), which is nonzero when \(a\ne0\). The example works for arbitrarily small \(a\). It refutes the proposed inference from compatible data to criticality under changed constraints; it is not a Yang–Mills counterexample or a claim that mu uses this invalid inference. Mu proves the needed fibre inclusion for its particular refinement.

One can try perturbing (15.4) instead. Equations (15.3) give a quantitative route only after every actual completion row is placed in that uniform chart. Pda bounds distances between sets, not the logarithms of \(V_2(\varpi)\) in a compatible gauge. The required bound on those logarithms, uniform over the allowed \(\varpi\), has not thereby been obtained.

### 15.2 Keep the old fine rows

The equality \(\Omega''_1=\Omega_1\) suggests a more local shortcut: on an unchanged level-zero determining row the average is the identity. If every bond in the collar's full read-set is such a row of \(\mathbf B_2\), and its actual datum equals an already controlled \(V_0\), then
\[
 U_2(b)=V_0(b)
 \tag{15.5}
\]
on that read-set, directly from the constraints. The plaquette and current estimates of §10.5 then apply if the same characteristic-function bounds hold on all their stencils. Whole-cube gauges still require the corresponding whole-cube hypothesis.

This conditional shortcut is valid, but pda proves neither of its datum assertions. Keeping \(\Omega_1\) fixed in the prepared nest does not identify all the rows of the subsequently spliced \(\mathbf B_2\), their values, or their cutoff tests. Even on a patch where the rows do agree, I:78445–78545 retains new real integration variables; one must check their actual cutoff bounds rather than substitute the complex source or a previously pinned \(V_0\). The distinction is material at the boundary: a bound only on plaquettes based inside a patch would not bound the neighbouring plaquettes read by the current.

The source's own extension conventions confirm the remaining analytic requirement. I:94185–94229 imposes core membership of the real bases in a kernel class, while explaining that the cited CMP 122b regularity statement is only on its cutoff support. I:94230–94245 requires the analogous membership at perturbed real data. These requirements are not proved by (A1), and an absolute kernel radius small with \(\gamma\) is not automatically the fixed birth-radius estimate in the Result.

**Exact failure of new attack 1.** The geometry is now supplied, but neither an admitted ancestor satisfying (15.4) and the correct criticality, nor the full-row/cutoff identification needed for (15.5), has been established for every actual \(V_2(\varpi)\). Mu and oc consequently cannot yet transfer their estimates to this particular seed. The obstruction is an actual datum and action comparison, not the previously open prepared-nest geometry.

## 16. New attack 2: transport the collar to a regular reference torus

The checked torus port suggests putting the entire collar read-set, including the enlarged cubes, into a sufficiently large reference torus. One might then use oc's regular real minimizer there and transfer its estimates back. Increasing the reference torus to fit the footprints is permissible and does not change a birth radius. The question is what the comparison theorem actually identifies.

P7's trace theorem compares local terms and prescribed operations with **matching complete traces and matching local data**, not arbitrary global minimizers with the same geometry. Its statement is CA-I:58187–58411; the relevant operation proof is port/p7-torus §“Activities, prepared profiles and termwise equality”, using I:59813–59872. Joined-domain analytic extension is H6b, I:58210–58212. The full completion identity for missing action members is H6a. Neither is derived from torus size.

There are two versions of the proposed transplant.

**An empty-trace reference.** Within the completing component, pda gives \(\Omega''_1\cap C=\Omega_1\cap C\). Read \(\Omega_1,Z_1\) from that retained precompletion label. At an old collar point,
\[
 y\in\operatorname{St}(d^t)\cap C
 \subset \Omega_1^c\cap C
 \subset Z_1\cap C.
 \tag{16.1}
\]
The last inclusion is the account's first-step small-field geometry; see also its explicit use at III:51160–51177. A precompletion window containing this point therefore has nonempty first-level large-field trace. It cannot be compared with a window declared to have empty trace. Completion may later heal the region, but the old term is still evaluated on its prescribed birth domain, with the trace data its construction reads.

P7 does identify missing completed action members with whole-lattice members. In its corrected proof C3, that is exactly the **entire-member completion premise H6a**, not a new consequence of geometric healing. Using that identity or its assumed analytic extension to admit the very completion being proved would reuse an input of the desired arrest argument. In addition, clause (iii) is stated after the current step has been completed at every site; it cannot be invoked backwards to supply that step's missing analytic membership.

**A reference with the same nonempty trace.** This version respects (16.1), but must carry the actual \(V_2(\varpi)\), its full averaging carriers and its boundary data as well. Oc supplies a regular reference minimizer only after its own real-data and cube hypotheses are met. No independent reference presentation satisfying those hypotheses and matching all these data has been constructed. Copying them to a larger torus leaves the same admission question. Equality of local action terms, even when proved, is not an exact finite-range identity for the global constrained minimizers; the variation and data comparison in §15 would still be needed.

There is a genuine restricted completion in the later account. For an aligned label, its first large-field index exceeds \(n_c\ge1\), so the first run has no level-one large-field region. Thus
\[
 Z_1=\varnothing,\qquad \Omega_1^c\subset Z_1
 \quad\Longrightarrow\quad
 \Omega_1=\mathbb T,\qquad
 \widetilde\Omega_1\setminus\Omega_1=\varnothing .
 \tag{16.2}
\]
In the second comparison run, the same argument applies to its first step, whose index is zero. The common/aligned condition excludes that region as well. This is the proof at III:51104–51185, credited to the source authors. Its collar assertions are vacuous on aligned labels, as the source says. It gives no bound on a nonempty collar in the full arrest theorem; those labels have not been removed from the statement or its uses.

**Exact failure of new attack 2.** Empty-trace transport fails its trace hypothesis at a nonempty old collar. Same-trace transport lacks an independently admitted reference presentation with the matching actual data and analytic domain. The checked torus theorem transports already admitted objects; its completion and extension inputs do not construct that missing presentation. The empty-collar subcase (16.2) is proved, but it is not the general Result.

## 17. New attack 3: use last-scale stability to control the real seed

The new LSC result supplies a different possible source of information: a uniform lower bound on mass and an upper bound with sources. Try first to turn the mass bound into a variational estimate for the constrained seed, and then to turn source estimates into a pointwise estimate on all real variables used by completion.

Use precisely lsc's corrected convention, not its withdrawn bare reading:
\[
 \widehat Z(0)=e^{-E_{\rm vac}}Z_{\rm bare}(0)
       \ge e^{-C_{\rm low}N^4},\qquad
 |\widetilde Z(w)|=
 |e^{-E_{\rm vac}-\mathcal E(w)}Z_{\rm bare}(w)|
       \le e^{C_+N^4},\qquad \mathcal E(0)=0.
 \tag{17.1}
\]
Here \(C_++C_{\rm low}\) is uniformly bounded in LSC's stated variables, but \(E_{\rm vac}/N^4\) need not be. These are lsc (5a)–(5b) and its round-2 Result, using I:159153–159160 and II:140916–140926.

For any action \(S\) on a probability measure space,
\[
 \int e^{-S}\,d\mu\le e^{-\inf S}.
\]
Even if (17.1) is applied directly to that action, it implies only
\[
 \inf S\le C_{\rm low}N^4-E_{\rm vac}.
 \tag{17.2}
\]
This is an estimate for an unconstrained infimum, with the vacuum term present. It is not an estimate for the minimum on every fibre \(M_{\mathbf B_2}U=V_2(\varpi)\), nor for each plaquette of such a minimizer. A lower bound on the whole integral supplies no uniform lower bound on the conditional mass of every fibre. The cutoffs and real-background hypotheses retained in LSC cannot be discharged by applying LSC to itself.

The source route fails for a separate, exact reason. Here is a hand counterexample to the inference from uniform analytic integral estimates to a deterministic bound. Fix \(\rho>0\). For \(t>0\), let a nonnegative random variable \(X_t\) be \(t\) with probability \(p_t=e^{-2\rho t}\) and zero with probability \(1-p_t\). Its moment generating function is the entire function
\[
 M_t(z)=1-p_t+p_te^{zt},\qquad M_t(0)=1.
 \tag{17.3}
\]
For every complex \(|z|\le\rho\),
\[
 |M_t(z)|\le1+e^{-\rho t}\le2,\qquad
 \mathbb E X_t^n=t^ne^{-2\rho t}
              \le {n!\over(2\rho)^n}\quad(n\ge1).
 \tag{17.4}
\]
The moment inequality follows from the single nonnegative term
\(e^{2\rho t}\ge(2\rho t)^n/n!\).
Even a uniform analytic logarithm does not cure the problem. For
\(t\ge(\log4)/\rho\),
\[
 |M_t(z)-1|\le e^{-\rho t}+e^{-2\rho t}\le5/16<1.
 \tag{17.5}
\]
The logarithm series is therefore valid on this disc and has absolute value at most
\((5/16)/(1-5/16)=5/11\). Cauchy's formula gives uniformly bounded derivatives of every order, hence uniformly bounded cumulants (indeed a bound \(n!\rho^{-n}\) suffices). Nevertheless
\[
 \operatorname*{ess\,sup}X_t=t\longrightarrow\infty .
 \tag{17.6}
\]
Every positive atom is in the support, so replacing “every datum” by “every datum in the support” does not evade this example. It is a counterexample only to the proposed inference; \(X_t\) is not asserted to be a Yang–Mills field or a completion output.

The required arrest statement is pointwise in each permitted real integration datum and each complex completion parameter. LSC bounds normalized integrals and source derivatives. Equations (17.3)–(17.6) show that even stronger uniform scalar analyticity and all-order moment bounds do not provide the missing pointwise bound. Nor is LSC's source disc the completion parameter domain \(\mathfrak P\).

**Exact failure of new attack 3.** The normalized lower bound controls neither all constrained fibres nor their local seed curvature. The sourced upper bound controls averages, not the supremum over the completion data. It supplies no estimate of the required size in the old birth radii. A separate deterministic seed estimate is still needed. This attack does not furnish a counterexample to the collar lemma.

## 18. A sufficient collar criterion proved by hand

The attempts above do not close the actual admission statement. They do permit a useful quantitative reduction: a small *physical* seed current does not require a separate estimate on the constraint multiplier if the seed plaquettes on all its stencils are controlled. Once the two actual layers have their primitive analytic estimates, no further loss of a birth radius is necessary in composing them.

Here is the reduction with explicit constants. It is a conditional lemma, not an assertion that its extra hypotheses hold for the actual completion.

Fix a completing component \(C\), its dates and its old radii. Take the union of the bonds read by the collar entries, the local algebra on their \(\widetilde\Delta(y)\)'s, every plaquette in the physical-current stencils, and every required whole cube and enlarged gauge domain. All hypotheses below concern these complete read-sets, including their boundary bonds. In particular, no derivative or current is evaluated after truncating a field.

Let \(U_2\) be the actual unitary seed on these sets, with one consistent value on overlaps. Suppose it has the required old index-zero gauges on the whole cubes, and put
\[
 \delta=\sup_p|\partial U_2(p)-1|,
 \tag{18.1}
\]
where the supremum includes every plaquette just specified. Let the actual formulas for \(\mathbb H_3,\mathbb H_4\) be defined on their primitive input classes for every prescribed source and every \(\varsigma\in\mathfrak P\). Suppose nonnegative numbers \(F_3,F_4\) bound their *complete local norms*, uniformly over those parameters and every layer segment used by the account:
\[
 \begin{split}
 \sup_y N_y^{\,\mathbb U^{(s-1)}}(t_s\mathbb H_s)&\le F_s,\\
 \sup_y\eta^3
   |\mathfrak s^\sharp_{\sigma_s}[t_s\mathbb H_s](y)|
      &\le K_{\rm cur}F_s,\qquad s=3,4.
 \end{split}
 \tag{18.2}
\]
Here the background in the first line is the actual preceding partial product; in particular the second layer's derivative is not silently computed at \(U_2\). Supremums include all neighbouring local sets needed for the next application. The current increment is the actual one in I:142567–142573. The admissible current-response bound has
\[
 K_{\rm cur}=3+18d+2.2K_J,\qquad K_*=\max\{4,K_{\rm cur}\}.
 \tag{18.3}
\]
In (18.3), \(K_J\) is the current-response constant of I:94996–95025, not LSC's terminal index. We require (18.2) as a hypothesis, on its proper inputs; we are not deriving it by invoking the unproved collar corollary.

Set \(\varepsilon=F_3+F_4\) and \(\alpha_{*,0}=\min\{\alpha_{0,0},\alpha_{1,0}\}\). The following concrete bounds suffice:
\[
 \delta\le{\min\{1,\alpha_{0,0}\}\over24},\qquad
 \varepsilon\le
 \min\left\{{1\over160},{\alpha_{*,0}\over16K_*}\right\}.
 \tag{18.4}
\]
They are uniform inequalities to be established for the actual objects, not instructions to choose a constant depending on a source, a birth date or an arrest age.

**Conditional collar lemma.** Under these hypotheses, the seed and the successive products on the prescribed segments,
\[
 \mathbb U(t_3,t_4)
   =e^{i\eta t_4\mathbb H_4}e^{i\eta t_3\mathbb H_3}U_2,\qquad
 \mathbb J(t_3,t_4)
   =\mathcal J(U_2)+
       \sum_{s=3,4}\mathfrak s^\sharp_{\sigma_s}[t_s\mathbb H_s],
 \tag{18.5}
\]
have a single presentation over \(U_2\) satisfying all five inequalities in the Result and the required whole-cube clauses.

**Proof.** First bound the full seed current. The physical-current formula used in §10.5 and I:142718–142737 is
\[
 \eta^3\mathcal J(U_2)(b)
   =\sum_{p\ni b}\epsilon_{bp}\operatorname{Ad}_{\tau_p}
           \pi\operatorname{Im}U_2(\partial p),
 \qquad \epsilon_{bp}\in\{-1,1\}.
\]
In dimension four the sum has six terms. Each transport \(\tau_p\) is unitary, the traceless projection has norm at most two, and for a unitary matrix \(W\) one has \(|\operatorname{Im}W|\le|W-1|\). Each term is therefore bounded by \(2\delta\), giving
\[
 \eta^3|\mathcal J(U_2)|\le12\delta .
 \tag{18.6}
\]
All six plaquettes are in (18.1); a bound only at the bond's base point would not justify this step. This estimates the entire physical current, including its constraint component.

At each collar centre \(y\), apply the local left-factor algebra I:141265–141508, ported in §10.2, first with \(A'=0\) and then with the potential from the first product. Its three smallness tests are satisfied. The first-layer norm is at most \(1/160<1/40\) and the initial curvature is at most \(1/24<1/10\). At the second application,
\[
 \sup_{\widetilde\Delta(y)}\eta|A'_3|
       \le{1.06\over160}<{1\over80},\qquad
 \max_{p\ {\rm based\ at}\ y}|\partial\mathbb U^{(3)}(p)-1|
       \le {1\over24}+{4\over160}={1\over15}<{1\over10}.
 \tag{18.7}
\]
The second layer's norm is again at most \(1/160\). The local algebra constructs its logarithm, keeps the same \(U_2\), and adds at most \(4F_s\), \(1.06F_s\), and \(1.2F_s\) to the plaquette, dimensionless potential and dimensionless covariant-gradient entries respectively. These statements hold at every collar centre and use its complete local read-set. Consequently,
\[
 \begin{array}{lll}
 Q_1\le\delta+4\varepsilon,&
 \eta^3Q_3\le12\delta+K_{\rm cur}\varepsilon,&
 Q_5\le\delta,\\[2pt]
 \eta Q_6\le1.06\varepsilon,&
 \eta^2Q_7\le1.2\varepsilon.&
 \end{array}
 \tag{18.8}
\]
For \(Q_3\) use (18.6), the second line of (18.2) and the triangle inequality. This does not identify the independent current at later complex parameters with a physical current: only its seed is physical.

Divide by the *old* radii
\[
 (r_1,r_3,r_5,r_6,r_7)(0)
 =(\alpha_{0,0},\alpha_{0,0}\eta^{-3},
   \alpha_{0,0},\alpha_{1,0}\eta^{-1},
   \alpha_{1,0}\eta^{-2}).
 \tag{18.9}
\]
Since \(K_*\ge4,K_{\rm cur}\), (18.4) gives respectively
\[
 {Q_1\over r_1(0)}\le{5\over48},\qquad
 {Q_3\over r_3(0)}\le{9\over16},\qquad
 {Q_5\over r_5(0)}\le{1\over24},\qquad
 {Q_6\over r_6(0)}\le{53\over3200},\qquad
 {Q_7\over r_7(0)}\le{3\over160}.
 \tag{18.10}
\]
Each number is less than \(3.65<f_0(d^t)\), giving the required strict inequalities. The same estimates hold with either layer partially or wholly absent, so they cover \(\mathfrak b_2,\mathfrak b_3,\mathfrak b_4\) and every required segment.

The logarithm in the left-factor algebra is defined bondwise by its convergent principal series in the small matrix neighbourhood. At the first step the potential has the bound in (18.7); at the second it has bound \(1.06\varepsilon\). The same bond therefore receives the same logarithm when read from two overlapping local sets. This gives a consistent potential over the single field \(U_2\). Derivative estimates use its full stencils. The unitary factor never changes, so all the assumed whole-cube gauges are retained. This proves the lemma.

More generally, (18.8) gives the less restrictive sufficient test: its five right sides, divided by (18.9), must be below \(f_0(d^t)\), while the local-algebra smallness tests must hold at each step. The fixed fractions in (18.4) merely exhibit a uniform choice with ample room. They neither change the birth domains nor assert the stronger \(\varphi_\flat/16\) corollary.

This criterion respects the order in §6.2: \(K_{\rm cur}\) is an already fixed analytic constant, \(K_*\) is a fixed maximum, and all remaining numerical fractions are absolute. No earlier \(L,M,\kappa\) or radius constant is reselected. To apply it universally, an estimate of the actual seed and actual layer majorants in the prescribed old units is still needed. Declaring \(\gamma\) small does not prove such an estimate without a uniform bound for those objects. In particular, neither (18.2) nor (18.4) has been inferred from the source's assumed level-zero chain/collar input.

The round-2 hand results are therefore the compatible-data implication in §15.1, the explicit failures of the three proposed inferences, and the conditional collar criterion (18.1)–(18.10). The aligned-label empty-collar proof is a port of the later account. None changes the disposition of the eleven statements in §13. No counterexample to the actual completion-collar statement has been established. Only this research note is changed; no audit, status or scientific ledger is updated.

## Result

**Open lemma**

**Completion-collar admission in the account's fixed birth domains.** Retain the original arrest hypotheses and primitive analytic inputs on their stated input classes; the later conventions I:140979–141189; the parameter order and ceilings I:143355–143471; the actual completion-layer construction and geometry I:142292–142317; and the other stage, averaging, outside-completion and real-point inputs identified in §10, used only on their stated input classes. The frozen pda, mu, oc and lsc results and checked torus port may be used with exactly the hypotheses and scopes in §14. Do **not** assume the level-zero chain/collar conclusion I:142269–142291 or the completion-collar cube admission I:142950.

Let $d'=(k;L)$ be a completion date, $d^t$ its scaffold predecessor, and $C$ a completing component. Put
\[
 \operatorname{Col}(C)
 =\operatorname{St}(d^t)\cap C
 =\bigl(\operatorname{St}(d^t)\setminus\operatorname{St}(d')\bigr)\cap C .
\]
For every source pair $p$ in the prescribed arrested source at $d'$, with its full global rider, and every completion parameter $\varsigma\in\mathfrak P$ (its real coordinates in their prescribed support and its complex coordinates in the full prescribed polydiscs), prove that the actual completion presentation is defined on this collar and, at $\mathfrak b_2,\mathfrak b_3,\mathfrak b_4$ and on every intervening layer segment used by O2 or O5, has a decomposition over the one presented unitary factor satisfying
\[
 Q_a\bigl(\operatorname{chain}_p(\varsigma)\bigr)(y)
 < f_0(d^t)\,r_a(0)
 \quad
 \text{for all }y\in\operatorname{Col}(C),\quad a\in\{1,3,5,6,7\},
\]
and the old index-zero cube clause CMP 99b (3.35) on every required whole cube meeting the collar, with the same field on overlaps and the full prescribed stencils. All constants must be chosen in the account's order, uniformly in the cutoff, density, waiting depth, history and arrest age; neither the source domain nor a stored term's birth domain may be shrunk.

This is weaker than the assumed $\varphi_\flat\mathbf r_a(0)/16$ collar corollary and is exactly the missing raw image membership used in (11.4). Round 1's three attempts remain in §12. The three new attacks in §§15–17 fail respectively at the actual datum/criticality comparison, an independently admitted reference with the matching nonempty trace, and the passage from normalized integral bounds to bounds for every completion datum. Each failure is demonstrated above; none proves the lemma false.

Section 18 proves a sufficient quantitative implication, including the full physical seed current, two complex layers, consistent logarithms and retention of whole-cube gauges. It does not prove its seed, gauge and layer hypotheses for every actual completion. Those bounds are possible means of proving this single open lemma, not extra assumptions added to it. With the lemma and the other explicitly retained source inputs, §11 supplies the full collar part of the repaired arrest argument. Without it, the full arrest proof and T0 remain unproved.
