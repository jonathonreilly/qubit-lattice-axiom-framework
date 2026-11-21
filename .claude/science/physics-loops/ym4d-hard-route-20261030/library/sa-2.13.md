# Obligation 2.13: loaded labels, literal histories and normalization
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed; queue row 112 requests max); checkout `9d399292b560c526dc79baf97ecd28cc7b8952c4`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, granting no status.

**Outcome: STOPPED at the session budget.** The conditional summation and two one-sided normalization estimates below are proved; the bound for the actual histories is neither proved nor refuted.

## 1. Task and source convention

The target is queue row 112: the actual loaded-label/history sum used at SA L17820 and developed at L18944–19406, including the literal-history entropy argument at L18672. A proof of a conditional forest sum alone does not prove that the actual operations have its hypotheses. An explicit failure of an intermediate assertion is distinguished from a counterexample to the final Yang–Mills bound.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the construction and arguments in [the outline at the specified revision](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex). `SA Lx–y` refers to its literal TeX lines, fetched once to `/tmp/sa_ym4.tex`. Balaban's CMP 109 (1987), 249–301, and CMP 119 (1988), 243–285, are read in the supplied paper folder; their statements carry no proved standing here merely by citation. Local note references are relative to this loop folder and frozen at the checkout above.

Only this file is edited. Source retrieval, bounded text reads and bookkeeping are not proof computations. No numerical or computer-assisted argument, audit, delegation, commit, push, PR or post is used. The workflow file is absent from the sparse filesystem but is read from this same commit with `git show`; no branch is fetched or substituted.

## 2. Literature first: what transfers, and what does not

The existing search record is `library/lit-balaban.md`, Sections 0 and 3. The following conclusions use the supplied papers themselves, not that record's secondary quotations.

| Source statement | Possible use for 2.13 | Required change / standing |
|---|---|---|
| Balaban, CMP 109, Theorems 1 and 3, pp. 259 and 264; (0.28)–(0.30) | Subtract the vacuum value and the marginal quadratic action before summing regular effective activities over scales. The irrelevant power then offsets the number of fine-scale cells. | These are small-field statements conditional on a small running coupling. A uniform bound for the actual separated, collared histories and their complex read domains must still be supplied. Imported analytic statement, unchecked here. |
| CMP 109, Theorem 2 and (0.31), p. 259 | Would supply the running-coupling hypothesis. | The paper defers its proof. It cannot be used to close 2.13; retain the frame/coupling hypotheses explicitly. |
| Balaban, CMP 119, (2.18)–(2.23), pp. 257–259 | Ordered operations on disjoint variable sets, with the retained Wilson weight, Gaussian terms, gauge factors and boundary terms still present. | Factorization of operations is not factorization of their evaluations at a background depending on all variables. The SA inside-integral common majorant is a stronger requirement. Mixed terms transferred to the boundary action must be paid there. |
| CMP 119, Theorem 1, pp. 262–263 | Preservation of an inductive effective-density description, conditional on the running couplings and the prescribed R-operation properties. | At pp. 244–245 Balaban explicitly leaves the construction of R for later work and assumes its properties in this paper. This theorem is not a construction of SA's modified R, its literal genealogy, or its complex weighted masses. |
| CMP 119, Theorem 2, (2.43)–(2.49), pp. 263–264; (3.40)–(3.42), (3.65)–(3.67), pp. 275, 283 | Use a partition of unity to assign local regular activities and their quadratic counterterms to the same sites. Subtract the same vacuum values; keep logarithmic normalization costs and the Wilson action. | Replace the regular domain by each actual determining layer; prove that deleting/redrawing a site changes precisely its assigned local number. SA's multiscale read domains, complex supremum, and source reserve are additional hypotheses, not consequences of these displayed estimates. |
| CMP 119, Corollary 3, (2.50), p. 264 | Predecessor for stability after vacuum normalization and large-field summation. | The constants there may depend on the final coupling, and the proof appeals to earlier combinatorics. It does not give the loaded total-variation sum, the new ownership convention, or a uniform-in-final-coupling assertion verbatim. The positive-label floor is a separate issue (SA L19400–19406). |

The useful exact algebra is this. If the full-torus vacuum number at step $j$ is $N_j e_j$, and a label uses that very number on $A_j\subseteq T_j$, their difference is $(N_j-|A_j|)e_j$, plus any explicitly redone-site terms. If $|e_j|\le C_0+C_1\log\theta_{j-1}$, its absolute cost is at most that price times the number of missing sites. This is a finite subtraction, valid with either sign of $e_j$. Replacing $e_j$ by an unrelated number known only to have the same bound would leave an error on every unchanged site. Balaban's p. 279 vacuum subtraction and SA L19066–19085 use the former algebra. No theorem about the actual identity of those numbers is proved by the algebra alone.

## 3. The 2.8 consumer: a smaller normalization statement can be proved

`library/sa-2.8-terms.md` (1.3) and its gate give a conditional **real** signed-action estimate, with the enlarged core cutoff and the full positive form

\[
 Q(B_i,B_o)=\tfrac12\|C_iB_i+C_oB_o\|^2.
\]

They do not give $C_i=0$, a relative-Hessian bound, or scalar independence of the reference denominator. Retain these factors. The following one-sided bound is sufficient to price a **real** reference denominator logarithmically; it needs neither a relative-Hessian estimate nor a Schur factorization.

**Lemma 3.1 (product-ball denominator, conditional on chart admission).** Let $m$ be the number of free SU(2) bonds after the reference tree delta functions have been integrated, and put $d=3m$. In physical Lie-algebra coordinates $u=(u_e)$, suppose the actual reference background exists on the complex polydisc $\max_e|u_e|<r$, with $r>0$ independent of the history, and

\[
 F(u)=A(\chi,U_{k,X}(e^{iu}V_\Lambda)),\qquad
 |F(u)|\le C_F K
 \tag{3.1}
\]

there. On real $u$, $F$ is real. Here $K$ counts the level-$k$ sites supporting the truncated reference action; it need not equal $d$. Let $x=g^{-2}$, $0<g\le1$, and suppose the actual cutoff admits every free-bond ball $|u_e|<a g^2$, where $0<a\le\min(r/4,1/2)$ is fixed. Assume that the real integral is defined on its entire cutoff support. Normalize Haar measure to total mass one. Then, for

\[
 \widehat D(S)=\int\delta_{\rm ax}\chi(\Lambda^{\rm pr})
              e^{-g^{-2}(F(u)-F(0))}\prod_e dU_e,
\]

\[
 \widehat D(S)\ge(c_Ha^3)^m g^{6m}e^{-C_FK},\qquad
 -\log\widehat D(S)\le d\log x+C_a d+C_FK.
 \tag{3.2}
\]

The constant $C_a$ is fixed; a larger $C_F$ can be used without changing any conclusion.

*Proof.* Fix a nonzero real $u$ in that product of balls, put $s=\max_e|u_e|$, and consider $h(z)=F(zu/s)$. It is holomorphic for $|z|<r$ and bounded by $C_FK$. The Cauchy coefficients about zero satisfy $|h_n|\le C_FK r^{-n}$: apply the Cauchy integral on each radius $r'<r$ and let $r'\uparrow r$. Therefore

\[
 |F(u)-F(0)|\le C_FK\sum_{n\ge1}(s/r)^n
     \le 2C_FKs/r\le (C_F/2)K g^2.
\]

The case $u=0$ is immediate. Enlarging the harmless constant gives $g^{-2}(F(u)-F(0))\le C_FK$ on this product set. This directional argument has no factor $d$ in its radius.

In the coordinates $U=\cos|u|\,1+i\sin|u|\,\widehat u\cdot\sigma$, normalized SU(2) Haar measure is $(2\pi^2)^{-1}(\sin|u|/|u|)^2d^3u$. For $0\le t\le1/2$, integrating $\cos s\ge1-s^2/2$ gives $\sin t\ge t-t^3/6\ge t/2$. Thus each radius-$a g^2$ ball has Haar measure at least $c_H(a g^2)^3$, for example $c_H=1/(6\pi)$. Tree delta functions set tree bonds to the identity with unit mass; each remaining bond carries its own normalized Haar measure. Multiply these $m$ lower bounds and the lower bound $e^{-C_FK}$ for the integrand. Taking logarithms, with $6m\log g^{-1}=d\log x$, proves (3.2). For $m=0$, the empty product has mass one and the inequality still holds. All estimates are written inequalities, not numerical checks. ∎

**Match to this consumer.** SA L17604–17610 cuts off $|u_e|<M_0gP_k$, so the small product balls are admitted once $ag\le M_0P_k$. Also impose $M_0gP_k<r$, so the entire cutoff is admitted. Both conditions hold at one fixed ceiling: for fixed $p$, the logarithmic derivative of $e^{-\ell/2}\ell^p$ is $-1/2+p/\ell\le-1/4$ for $\ell\ge4p$, so this expression tends to zero. The tree is explicitly fixed, including its external anchoring bond. In the convention of `sa-2.8-terms.md` Section 7(a),

\[
 D_X=e^{-xF(0)}\widehat D(S).
\]

The factor $e^{xF(0)}$ from $D_X^{-1}$ is the one already present in the exact 2.8 cancellation. Equation (3.2) prices the remaining inverse denominator directly; it does not replace it by a scalar. If $db$ denotes Lebesgue measure with $u=gb$, the $g^d$ and the Haar Jacobian must be retained. The proof above uses the actual Haar measure and already includes both.

Hypothesis (3.1) is supplied **conditionally** by the full complex regularity/admission package I2 for the healed reference chart: on the support of $\chi$, the background is at level $k$, each bare plaquette action is bounded by $C\eta^4$, and at most $CK\eta^{-4}$ bare plaquettes occur. For completeness, if $W=1+E\in\mathrm{SL}(2,\mathbb C)$, then $\operatorname{tr}E=-\det E$ and $|1-\tfrac12\operatorname{tr}W|\le\tfrac12\|E\|^2$. Thus the curvature estimate gives the stated $C\eta^4$ even at complex fields. Summing over the counted plaquettes gives $CK$, independent of depth. The gate's repaired count is $K\le(n_XMR_k)^4$; the bounded reference box has $d\le12(C_\Lambda M)^4$. Hence (3.2) costs at most $C(1+\ell_k)(MR_k)^4$, the allowed price of an owned level-$k$ cell. These are the *stated* I2/GEO inputs, not newly discharged background theorems. The proof does not use I4's claimed Hessian lower bound. It proves real positivity with a quantitative price wherever that admitted chart exists; it proves no nonvanishing statement for a denominator evaluated at complex data.

The prior product-ball argument in `library/sa-2.8.md` Section 7 proves only a finite-cutoff lower bound $h_r^m e^{-2xN_\chi}$. Lemma 3.1 uses the cancellation of $F(0)$ and a dimension-independent directional Cauchy bound to replace that bare-volume price by $d\log x+CK$. The Haar argument is the same elementary mechanism, credited here to that earlier Codex note.

## 4. Literal addresses: the depth count closes

Use the cell grid of SA L17334: $R_j$ is a power of $L$, the grids are nested, and between consecutive levels their physical cell side changes by a factor $L$ or $1$. Join same-level cells whose closures touch, and join each cell to its unique parent. After identifying periodic neighbors this graph has degree at most

\[
 D=L^4+3^4+2.
 \tag{4.1}
\]

A size-drop level has one child per parent; an ordinary level has at most $L^4$. Periodic identifications cannot increase these bounds. The cutoff selects a finite subgraph of a graph with this same degree bound.

**Lemma 4.1 (address entropy).** For any graph of degree at most $D\ge2$, any fixed root $z$, and any integer $N\ge1$, the number of connected $N$-vertex sets containing $z$ is at most $D^{2N-2}$.

*Proof.* Fix an ordering of the neighbors at every vertex. For each set, construct its rooted spanning tree by depth-first search using this ordering on the induced graph. Record the neighbor number of each edge traversal, including each return traversal. The word has exactly $2N-2$ symbols, each in an alphabet of size at most $D$. Starting at the fixed root, the word determines the visited vertices, which are exactly the original set. Thus the map from sets to words is injective. For $N=1$ the empty word represents the root alone. ∎

For a retained component, use all cells of every uncut node of its outer genealogy as the active set. Each same-level node is connected. The coarsening/hull/enlargement rules include the parent images of every surviving predecessor in its successor. Consequently their union in the address graph is connected. Cutting at an inner island leaves its root vertex set present and removes only its descendants. Keeping a drop-out keeps its old nodes, without inserting a new copy at every subsequent level. These facts concern the specified genealogy; they are not a claim that the entire bare-kernel history, including already healed components, is one connected record. Earlier healed histories have been absorbed into activities and require the separate 2.10 identity.

This excludes free choice of birth depth as a counterexample to the address count. A birth $a$ levels below its fixed root requires at least $a+1$ vertices on its address path. Changing the birth level changes that path; it is not an additional free integer attached to a fixed $N$-vertex record. Its cost is already in (4.1). A set of unrelated birth sites without these paths would not be the active set being counted.

### Outcome codes and the exact remaining geometric premise

Let $s(v)=(MR_{j(v)})^4$, $\ell_j=\log\theta_j\ge1$, and $V(A)=\sum_{v\in A}\ell_{j(v)}s(v)$. Suppose every test address read by an outer record can be assigned to these cells with at most $J s(v)$ addresses assigned to $v$, where $J$ is fixed. Suppose there are at most $q$ elementary binary tests per such address, at most $J$ additional finite-state records per cell, and at most $J$ integers in $\{0,\ldots,R_j\}$ per cell. The finite-state alphabet has size $q_0$. Frame choices have their literal normalized weights. With $R_j\le C_R(1+\ell_j)^r$, there is a fixed $b$ such that the normalized number of outcome records over a fixed $A$ is at most $e^{bV(A)}$.

Here is the complete count. Write all binary outcomes in a fixed address order, including a dummy symbol for an unread test if necessary; use an alphabet of size three for pass, fail, unread. Their number is at most $3^{qJ\sum s(v)}$. The other symbols have at most

\[
 q_0^{J|A|}\prod_{v\in A}(R_{j(v)}+1)^J
\]

choices. Since $\log(R_j+1)\le C+r\log(1+\ell_j)\le C'\ell_j$, and $s(v)\ge1$, the logarithm of their product is at most $bV(A)$. For each non-frame skeleton with $f$ frame slots, allowing all frames gives exactly $|W_4|^f$ choices weighted by $|W_4|^{-f}$. Restrictions can only reduce this normalized count. The root frame is handled in precisely the same way. This argument still works if the skeleton and its test-address choices depend on the frames: take the uniform code bound at each complete assignment, then average it.

An injective decoding uses the deterministic time order, the active sets, the test outcomes and the frames to replay the discrete moves. Continuous reference/gauge draws are the stored integration variables, not extra discrete outcomes. There is no sum over permutations of commuting components: one fixes their address order. Without fixing that order, arbitrarily inserting all $n!$ schedules would change the definition of a history sum.

The explicit outer procedure supports this code: ordinary step tests have finitely many types; collar/rim rounds inspect previously unread addresses (SA L17356–17368); and a preparation stops at its first failed stage. Thus previous stages have forced successful outcomes, while the failing stage and its outcome locations are recorded. The stage number costs $\log(R_j+1)$, not $R_j$ bits at every site. Main-step tests have a fixed number of types. This settles the discrete coding *provided the stated bounded ownership of their read addresses holds*. It does not prove the uniform read-collar assignment for all the actual prepared/determining sequences. That is the geometric premise in SA L18449–18470 and L19044–19063.

Choose $c_e\ge b+2\log D+\log2$. For any class with the address/ownership properties just specified, $V(A)\ge|A|$, and the entire normalized entropy sum is

\[
 \begin{split}
 \sum_{\omega^\circ}|W_4|^{-1-f(\omega^\circ)}e^{-c_eV(\omega^\circ)}
 &\le\sum_{N\ge1}D^{2N-2}e^{-(c_e-b)N}\\
 &\le D^{-2}\sum_{N\ge1}2^{-N}=D^{-2}\le1.
 \end{split}
 \tag{4.2}
\]

Every inequality is uniform in the root's height and the torus. Infinite classes follow by increasing finite sums of nonnegative terms. This proves the entropy implication, including its constant at most one; no enumeration was run.

## 5. Retaining creation credit: the scalar argument closes conditionally

Here are the precise hypotheses and proof of the reserve used below. Let a finite rooted genealogy have a level $n(u)$ and a nonempty cell set $C(u)$ at each node. Write $n_t^{\rm cr}$ and $n_t^{\rm mk}$ for creation and renewed-mark counts, excluding the root's own prospective mark. Let $T_t,r_t\ge0$ be non-increasing. Assume the geometric estimate

\[
 \sum_u r_{n(u)}|C(u)|\le C_2\sum_tT_tr_t
                       (n_t^{\rm cr}+n_t^{\rm mk}).
 \tag{5.1}
\]

It is SA's genealogy-count, L18580–18608, whose actual hypotheses include the skeleton/reach bound, compulsory admission after a quiet wait and the terminal-torus rule. It is not inferred from address entropy. If all costs, including entropy and the requested extra load, satisfy $c_t\le r_t$, and the available *unspent* creation/mark credits obey

\[
 G_t\ge2P_t+C_2T_tr_t,\qquad P_t\ge C_2T_tr_t,
 \tag{5.2}
\]

then direct subtraction gives

\[
 \begin{split}
 \sum_tG_tn_t^{\rm cr}+\sum_tP_tn_t^{\rm mk}
              -\sum_uc_{n(u)}|C(u)|
 &\ge\sum_t(G_t-C_2T_tr_t)n_t^{\rm cr}
       +\sum_t(P_t-C_2T_tr_t)n_t^{\rm mk}\\
 &\ge2\sum_tP_tn_t^{\rm cr}.
 \end{split}
 \tag{5.3}
\]

Thus the ledger does not spend the entire creation payment. One may retain one $P_t$ per creation and still retain the other $P_t$, or keep their sum. Renewed-mark credit pays the new wait only. This proof needs the credits after action has already been reserved for the integrable envelope; counting the same action share in both places would violate its hypothesis.

The hierarchy admits (5.2) uniformly. Suppose $T_t\le C_TR_t$, $r_t\le C_rc_1M^4R_t^5$, $R_t\le C_R\ell_t^r$, $P_t=A_0\ell_t^p$, $p\ge6r+1$, and $G_t=c_GP_t^2$, with every constant positive and fixed. Put $B=C_2C_TC_rC_R^6M^4$. Then $C_2T_tr_t\le Bc_1\ell_t^{6r}$. Choose the common floor so that

\[
 \ell_t\ge1,\quad
 \ell_t^{p-6r}\ge 2Bc_1/A_0,\quad
 c_GA_0\ell_t^p\ge4.
 \tag{5.4}
\]

The first relevant inequality gives $C_2T_tr_t\le P_t/2$, and the second gives $G_t\ge4P_t\ge2P_t+C_2T_tr_t$. For example it suffices to take the floor larger than $1+2Bc_1/A_0+(4/(c_GA_0))^{1/p}$; no constant is selected from a particular depth. If $P_t\ge P_i/(1+\beta_0)$ for $t\le i$, any nonempty genealogy has a creation leaf, and (5.3) retains at least $2P_i/(1+\beta_0)$.

If a live root is propagated quietly for $q$ further levels before the next event or completion, apply (5.3) to that extended genealogy. No event count changes. Subtracting its new cell costs shows that the old balance already reserves those costs. One cannot append arbitrary quiet levels past the stipulated admission time; doing so invalidates (5.1), not the subtraction above.

The proposed repeated-drop-out counterexample therefore has two distinct outcomes. Counting all old nodes anew at each drop-out would overcharge the volume and does fail (SA L17831 already gives that warning). In the specified recursive volume, every uncut node occurs once and a clearing node at most twice, as an outer leaf and an inner root. Inductively expanding the finite recursion proves $V\le v^\natural\le2V$. Merely retaining a drop-out introduces no third copy. This is why the counterexample does not apply to that volume. Whether a later read can always be charged to this volume is the separate ownership premise in Section 4.

### Derivation of the geometric count used in (5.1)

This spells out the count from SA L18472–18608. Its discrete premises are: a step adds at most a fixed cell reach $A$ to the images of the old and newly created cells; boxing is applied only to sets of bounded cell diameter; every two levels coarsen by at least $L$; all components satisfying the stated size, quietness, depth and quarantine tests are treated. These are rules of the specified algorithm, not analytic small-field conclusions. Use only a terminal interval on which the cell partition remains defined, as in the admissible-torus construction.

Let $O(u)$ be the images at the node's level of all its ancestral creation cells; at a cut island include its bounded set of cut cells. Each addition at an earlier level has current reach at most $A L^{-\lfloor a/2\rfloor}$ after $a$ levels. Summing gives a fixed reach $e\le2A/(1-L^{-1})$, after enlarging $A$ for initial collars and boxing. Boxing does not invalidate this estimate: every added box has bounded diameter and contains a cell of the component being boxed; if several such boxes merge, their union has the same bounded-distance property relative to their predecessors. If boxing repeats while the merged component still qualifies, its entire bounding box has bounded diameter; if it ceases to qualify, no further bounding rectangle is added.

It follows that $O(u)\subset C(u)\subset O(u)^{[e]}$. Project a nearest-neighbor path in $C(u)$ to nearest points of $O(u)$. Consecutive projected points are at distance at most $h_0=2e+1$, so $O(u)$ is $h_0$-connected. Also $|C(u)|\le C_e|O(u)|$ with $C_e=(2\lceil e\rceil+1)^4$.

An $h_0$-connected $N$-cell set has a spanning-tree walk of length at most $2h_0(N-1)$. After coarsening by ratio $q$, divide this walk into segments of length at most $q$. Each segment, with a fixed coarse collar, meets at most a dimension-dependent fixed number of coarse cells: its coordinate diameter is at most $q$. Hence its coarse image has at most $C_0(1+h_0N/q)$ cells. Choose $s_0$ so that $L^{\lfloor s_0/2\rfloor}\ge8C_0h_0$, and choose $\nu_*\ge4C_0$. A node with $|O|>\nu_*$ then has at most half as many occupied cells after $s_0$ quiet levels. A light node, with $|O|\le\nu_*$, contributes only a fixed number. New cells born during this interval contribute at most a fixed multiple of their number; mergers take unions and do not increase their sum. Thus, putting nonexistent levels equal to zero,

\[
 o_n\le\tfrac12o_{n-s_0}+C_1 l_{n-s_0}
              +C_1\sum_{n-s_0<t\le n}n_t^{\rm cr},
 \qquad o_n=\sum_{u:n(u)=n}|O(u)|.
 \tag{5.5}
\]

For non-increasing $r_n$, sum after multiplying by $r_n$. The shifted first sum is at most half the original sum. The shifted light-node sum is at most $\sum_n r_nl_n$. Each creation contributes at most $s_0$ times, each time with weight at most $r_t$. Therefore

\[
 \sum_n r_no_n
 \le2C_1\sum_n r_nl_n+2C_1s_0\sum_t r_tn_t^{\rm cr}.
 \tag{5.6}
\]

A quiet chain has no creations, mergers or renewed marks. Once light, its skeleton has bounded diameter and remains light under coarsening. The side recursion $\alpha_{n+2}\le L^{-1}\alpha_n+2A$ implies
$\alpha_{n+2b}\le L^{-b}\alpha_n+2A/(1-L^{-1})$.
The stipulated small-box threshold lies strictly above this fixed point, so a fixed $b_0$ makes the entire subsequent quiet trace small. After a further $N_t+1$ levels, where $t$ starts the chain, the preparation window lies beyond that initial transient and every earlier event. This uses $N_n\le N_t$. All class conditions hold, and compulsory treatment ends the chain, by healing or by a new mark. The light segment consequently has at most $T_t=b_0+N_t+3\le C_TR_t$ nodes. If the interval ends first, the count only decreases. On a torus with bounded side in cell units there are only a bounded number of further admissible coarsenings, since every two levels shrink that side by $L$; these can be included in $b_0$.

A chain starts at a creation, after a mark, or at a merger. For each merger select a non-first predecessor and then descend through first predecessors to a leaf. Distinct mergers select distinct leaves. For incomparable mergers their subtrees are disjoint. If one is below the other and lies on its selected descent, that descent takes the lower merger's first predecessor, whereas the lower merger selects a non-first predecessor. Hence their selected leaves differ. Each leaf contains a creation cell, which can pay for its own chain and at most one merger chain. A mark pays for its following chain. Monotonicity of $T_tr_t$ makes payment at the earlier assigned event no smaller. Thus

\[
 \sum_n r_nl_n
 \le2\sum_t T_tr_t n_t^{\rm cr}
       +\sum_t T_tr_t n_t^{\rm mk}.
 \tag{5.7}
\]

Combine (5.6), (5.7), $T_t\ge1$ and $|C(u)|\le C_e|O(u)|$. Equation (5.1) follows with $C_2=2C_eC_1(s_0+2)$, increased if necessary for the fixed cut-cell convention. This proves the geometric implication with all constants independent of height. It does not establish that cut cells or renewed marks possess the *analytic* witness payments in (5.2).

## 6. A direct bound for the visible determining-bond load

There is a useful improvement over treating every background read as a new site. Write $\Omega_j^a$ for the action sequence and $\Omega_j^d$ for the determining sequence of the current label. The interrupted-stage rule of SA L17418–17446 fills part of an old hole: its remaining prepared box lies in the old $\Omega_j^c$. Consequently

\[
 \Omega_j^a\subseteq\Omega_j^d,\qquad
 (\Omega_j^d)^c\subseteq(\Omega_j^a)^c\subseteq Z_j^a.
 \tag{6.1}
\]

The last inclusion follows from $\Lambda_j^a\subseteq\Omega_j^a$ and $Z_j^a=(\Lambda_j^a)^c$. Healing and island creation make the same replacements in both sequences outside later interrupted windows. At any fixed location the windows of standing nested marks are disjoint: if a level-$s$ mark lies inside an eligible level-$t$ component, quarantine requires $s<t-N_t$. Thus (6.1) is preserved under the successive replacements; it is not an assumption that the two sequences coincide.

Use the actual definition at SA L5613–5623: a bond of $\Gamma_j$ has at least one endpoint in $\Omega_j^d$ and neither endpoint in $\Omega_{j+1}^d$. For $j<k$, assign it to such an endpoint. By (6.1) that endpoint lies in $Z_{j+1}^a$. At most eight oriented nearest-neighbor bonds select one site. A level-$(j+1)$ cell contains at most $(L+1)^4(MR_{j+1})^4$ level-$j$ sites, including its boundary. Counting boundary sites in every adjacent cell only increases this bound. Hence, with a fixed $C_L$,

\[
 |\Gamma_j|\le C_L\#_{j+1}(Z_{j+1}^a)^+\quad(j<k),
 \qquad |\Gamma_k|\le8N_k,
\]

and therefore

\[
 \sum_{j\le k}|\Gamma_j|
 \le8N_k+C_L\sum_{t\le k}\#_t(Z_t^a)^+.
 \tag{6.2}
\]

The enlargement $+$ covers any boundary-cell convention. A one-cell enlargement of a union of cells has at most $3^4$ times as many cells: assign every enlarged cell to one original cell at cell-distance at most one. If preparation has clipped a visible region into smaller $M$-boxes, first cover it by its owning original $MR_t$-cells and apply this enlargement bound to that cover. No assertion that a prepared box itself is an $MR_t$-cell is needed. This proves the necessary bounded collar price without a separation estimate. The argument also covers the bare determining layer if it is included in the sum. The only top-layer contribution is $8N_k$, once.

Each visible action cell at time $t$ belongs to the component node which carried it at that time. Its current visible part is a subset of that node's original cell set. If retained inside an outer mark, assign it to that mark's local history, at time $t$; otherwise assign it to the outer genealogy. Components at a fixed time are disjoint. Cutting at an island permits two copies of its boundary node, already included in $v^\natural\le2V$. An erased healed component has no visible old slot. Thus these assignments give

\[
 \sum_t\ell_t\#_t(Z_t^a)^+
 \le J_0\left(V_{\rm outside}+\sum_{X\text{ outer mark}}v^\natural(\omega_X)\right)
 \tag{6.3}
\]

with fixed $J_0$ (the cell collar and coordinate-convention factors). This statement counts the *current visible action slots*, not the read regions of all local activities ever formed. Those latter reads are an analytic-envelope issue. In particular (6.3) does not bound a union retaining all earlier healed collars after their components have been erased.

Bounded adjacent frame increments and a common large floor give $\log\theta_{t-1}\le2\ell_t$. Substituting (6.2)–(6.3) into the load at SA L19033–19041 proves

\[
 \mathscr L_c(\mathcal S)
 \le8cN_k+\lambda_c\left(V_{\rm outside}
                      +\sum_Xv^\natural(\omega_X)\right),
 \tag{6.4}
\]

where $\lambda_c$ is fixed and affine in $c$. In particular $c^\sharp=c+\lambda_c$ pays the visible load inside a drop-out from its **volume weight**, leaving its already-spent creation gains alone. This establishes the visible-label incidence implication from the specified set replacements. It does not establish the stronger uniform read-region assertion needed for every factor in a component's analytic envelope.

## 7. The full mixed $Q$: a second one-sided consumer estimate

**Lemma 7.1 (bounded coordinates).** Let $B=(B_1,\ldots,B_d)$ be actual free scalar coordinates with $|B_a|\le H_a$, and let $Q(B)\ge0$ on this real domain. For any nonnegative integrand bounded by

\[
 e^{-\Gamma+AV}\,e^{-Q(B)}\prod_{a=1}^d J_a
 \quad\text{with}\quad
 \sum_a\log\max\{1,2H_aJ_a\}\le BV,
\]

its integral is at most $e^{-\Gamma+(A+B)V}$. The $J_a$ are nonnegative uniform bounds; if later variables remain fixed, the displayed bound is uniform in them. Here $\Gamma$ is an already extracted witness payment, not another use of $Q$.

*Proof.* Drop $e^{-Q}\le1$, enlarge the integration set to the coordinate box, and integrate each constant $J_a$ over its interval. The resulting product is at most $e^{BV}$. If a triangular coordinate change was used, its actual inverse-Jacobian factors must be included in the $J_a$; translation alone has unit Jacobian. Normalized Haar variables can instead be integrated with upper bound one. ∎

For the main-step variables of SA L17598 and L17642, $H_a\le A_1p_1(g_i)$. Since $\log p_1(g_i)=\mathfrak p_1\log\ell_i\le C\ell_i$, the box cost is logarithmic per coordinate. The main operation uses one scaling $g_i$ on shells at earlier levels $j$; bounded-error monotonicity gives $\ell_i\le C\ell_j$, so it can be charged to each coordinate at its original level. Powers of $g_i$ from the measure or scalar factors also have this price. In particular the real mixed form $Q(B_i,B_o)$ may be kept in its entirety and then discarded for this **upper** integration estimate. No statement that the inner and outer Gaussian factors separate is required. This does not bound an unverified elimination determinant or a field-dependent inverse normalizer: they have to satisfy the displayed $J_a$ bound. Lemma 3.1 supplies the price for the real reference denominator under its chart hypothesis.

This establishes the proposed smaller statement rather than leaving a Schur-complement problem as the only route. It does not prove the full complex-pair majorant of SA L18045–18105. In particular a real lower bound for a denominator cannot be analytically continued as a lower bound for its modulus.

## 8. The precise conditional loaded-sum theorem

The following proves the summation mechanism, including an explicit retained creation tilt. It is stated at the level of *unsummed* retained records, so it cannot conceal the desired label sum in an assumption. Let all volumes be counted with the ownership convention above. Fix $c\ge0$ and $\kappa\ge0$ before choosing the coupling ceiling. Assume:

1. **Geometry and code.** Every nonempty final connected record is rooted at a specified site of the last lattice, with an active address graph and outcome code satisfying Section 4. Its volume $V$ bounds its final site count up to a fixed factor. The genealogy satisfies (5.1), with the uniform hierarchy in (5.4). Records hidden inside a mark are expanded or integrated once, never duplicated. Their visible labels obey (6.4).
2. **Unsummed analytic certificate.** After allocating disjoint witness shares, each complete connected record $h$, with normalized frame weight $w_h$, has a nonnegative Borel envelope $G_h$ on its actual free coordinates satisfying

   \[
   |I_h(\xi)|\le w_h e^{A V(h)-\Gamma(h)}G_h(\xi),\qquad
   \int G_h\,d\mu_h\le e^{B V(h)},\qquad
   \Gamma(h)=\sum_tG_t n_t^{\rm cr}(h)+\sum_tP_t n_t^{\rm mk}(h).
   \tag{8.1}
   \]

   The same envelopes dominate simultaneous later reads, before any supremum or integration is interchanged; different final records use disjoint coordinate groups. The credited witnesses exclude the action share used for $G_h$. A complete record here includes the local histories under its marks. If (8.1) is established recursively, integrating the outer variables at fixed inner variables and using a *uniform* conditional integral bound gives its second inequality by induction; a separate fixed-exterior bound is insufficient.
3. **Exact normalized assembly.** After the common vacuum normalization and the legitimate healed-history summation, each label term is dominated by a sum over compatible forests of these records, each forest assigned once, times $e^{C_0N_k}$. All remaining local prices are bounded by $AV$ after increasing $A$. The identity of unchanged vacuum slots is the exact one in Section 2. The determining-bond and logarithmic defect load have the assignment (6.4). In particular this is a hypothesis about the actual exponent and measures, not a definition of a substitute density.

Every constant $A,B,C_0,J_0$ is fixed at a preliminary coupling ceiling, remains valid when it is lowered, and is independent of depth, cutoff, volume and the last coupling. The geometric/code hypotheses concern the specified discrete rules; the analytic and assembly hypotheses are the substantive uncompleted applications discussed below.

**Theorem 8.1.** Under these hypotheses there is one coupling ceiling, depending on $c,\kappa$ and the fixed construction constants only, for which

\[
 \sum_{\mathcal S}|e^{\mathcal E_k(\mathcal S)}|
       \tau^{\rm abs}_{\mathcal S,c}(\mathcal V_k)
                      e^{\mathscr L_c(\mathcal S)}
 \le e^{C(c,\kappa)N_k}.
 \tag{8.2}
\]

More precisely, before forgetting which history produced a label, its positive majorant can be multiplied by

\[
 \exp\left\{\sum_{h\text{ in the forest}}\mathcal C(h)
                 +\kappa\sum_{h\text{ in the forest}}\#_k C_h\right\},
 \qquad \mathcal C(h)=\sum_tP_t n_t^{\rm cr}(h),
 \tag{8.3}
\]

and still has the bound in (8.2). Thus creation credit has been retained, not just silently consumed to make a finite sum. If one wants a charge depending on the label alone, take the infimum of the displayed charge over its realizing records. Creation sets are not determined by labels.

*Proof.* First absorb the part $8cN_k$ of (6.4) into $C_0N_k$. Put all the other requested prices into one per-volume coefficient $K$: it contains $A+B$, the stored weight $c$, the load coefficient $\lambda_c$, the fixed multiple of $\kappa$ needed for the final site count, and $c_e$. Fix this coefficient once. The hierarchy (5.4) then permits the scalar reserve with this enlarged cell price; it gives, for each record,

\[
 \Gamma(h)-K V(h)\ge2\mathcal C(h).
 \tag{8.4}
\]

Equation (8.1), multiplied by the stored/load weights and the final-site tilt, is consequently at most $w_h e^{-2\mathcal C(h)-c_eV(h)}$ after integration. Multiplying also by $e^{\mathcal C(h)}$ leaves

\[
                 w_h e^{-\mathcal C(h)-c_eV(h)}.
 \tag{8.5}
\]

The reserve constants can absorb the factor two in the recursively counted volume by increasing $K$ before the ceiling is selected. No old creation is charged again merely because its component remains stored.

Sum (8.5) over all records with a fixed root $z$. Discarding $e^{-\mathcal C(h)}\le1$, Section 4 bounds this sum by one. Denote the integrated tilted record weights by $a_h\ge0$. Assign each nonempty final component its least site in a fixed ordering of the last torus. There are at most $N_k$ roots, so

\[
 \sum_h a_h\le N_k.
 \tag{8.6}
\]

This slightly weaker root count suffices and does not require divisibility by $M$. When an exact periodic $M$-partition is given, SA's sharper $N_k/M^4$ is available.

For a finite set of possible records, summing over all subsets rather than just compatible forests gives

\[
 \sum_{\mathfrak F\text{ compatible}}\prod_{h\in\mathfrak F}a_h
 \le\prod_h(1+a_h)
 \le\exp\!\left(\sum_h a_h\right)
 \le e^{N_k}.
 \tag{8.7}
\]

The middle inequality follows from $\log(1+t)\le t$, obtained by integrating $1/(1+t)\le1$ from zero. The empty forest contributes one. For a countable representation take the increasing union of finite record sets; positivity proves the same bound by monotone convergence. Multiplication by $e^{(C_0+8c)N_k}$ proves the tilted bound, and removing the nonnegative tilts proves (8.2). Tonelli applies to the Borel envelopes on the disjoint variable groups. This proof never multiplies merely fixed-exterior integral bounds. ∎

For a nonempty record rooted at level $k$, the retained charge in (8.5) is at least $P_k/(1+\beta_0)$ when its uncut genealogy has a creation leaf and the stated frame comparison holds. Together with the explicit final-site tilt, this is the claimed per-component rarity/volume decay. If records are instead cut at outer marks, the inner creation sums must first be retained inside their weighted masses; they cannot be counted again as outer payments. Formulation (8.3) avoids this ambiguity by retaining credit before that regrouping.

**Sources.** There is also a complete implication for the source reserve. Suppose each newly formed local term $\psi_f$, on its assigned owned carrier $R_f$, satisfies

\[
 \sum_{f:x\in R_f}\frac{\sup|\psi_f|}{|R_f|}\le F
 \tag{8.8}
\]

on the whole required source/data domain, including its value at the reference pair. Then double counting gives $\sum_f\sup|\psi_f|\le F\#\{\text{owned sites}\}$. Expand the finite source recursion: every new term belongs to one node and every child history enters once. Its total is bounded by $F n^\sharp\le2Fv^\natural/\ell_{\min}$. Adding this coefficient to $c$ in the preceding proof pays the source at every depth. If the terms are holomorphic and supports/measures are fixed at their unsourced values, the resulting summable common envelope permits Fubini on each complex triangle; the integral around each triangle is zero, so Morera gives holomorphy of the integrated sum. This does not prove (8.8) for actual formed activities; in particular an oscillation estimate alone would not bound their scalar reference values.

## 9. Attack on the last analytic shortcut

The real denominator estimate cannot supply a complex-pair envelope by analytic continuation alone. Here is an explicit counterexample to that *smaller inference*. Give $u\in[-h,h]$ normalized Lebesgue measure, put $F_z(u)=zu$, $x=g^{-2}$ and $h=gP$, with $P\ge1$. Then

\[
 D(z)=\frac1{2h}\int_{-h}^h e^{-xzu}\,du
     =\frac{\sinh(xhz)}{xhz},\qquad D(0)=1.
 \tag{9.1}
\]

The equality follows by integrating the exponential; its apparent singularity at zero is removable by its power series. For real $z$, pairing $u$ and $-u$ gives $D(z)\ge1$. The action is entire and bounded on every fixed polydisc in $(u,z)$. Nevertheless

\[
 D\!\left(\frac{i\pi g}{P}\right)=0.
 \tag{9.2}
\]

These zeros approach the real center as $g\downarrow0$. This is a counterexample to deriving a uniform complex inverse-normalizer bound from holomorphy and a uniform real lower bound. It is **not** a Yang–Mills history or a counterexample to 2.13: it does not satisfy the additional critical-reference and complete-action structure the actual construction would have to use. That structure needs a proof when a complex inverse denominator is consumed. Keeping all source kernels frozen at their real unsourced values avoids complexifying their measures, but it does not, by itself, prove SA's separate complex-pair mass norm.

I also followed the actual witness allocation through SA L18154–18415. It excludes the last failed test from a drop-out's own mass, puts its later witness outside the old floor, and uses the real carrying field on the compatible fibre. These rules defeat the proposed double-spending example at the bookkeeping level. The fluctuation/collar witness, however, explicitly uses the lower bound for the **actual complete precision and actual cut conditional form** (stored-schur), not positivity of the main-step curl square $Q$. Lemma 7.1 removes a Gaussian-factorization requirement for integrating bounded $B$; it cannot supply that witness lower bound. SA L17557–17564 identifies the actual kept form as a truncated series, whose lower bound is not inherited from the genuine Schur complement. No explicit admitted configuration violating that lower bound was obtained.

## 10. Recovery checkpoint and outcome

Completed results are Lemma 3.1 (real inverse-denominator price from the stated chart hypothesis), Lemma 4.1 and (4.2) (address and outcome entropy under the stated ownership/code conditions), (5.1)–(5.7) (the discrete genealogy/reserve implication), (6.4) (visible-label load from the specified set replacements), Lemma 7.1 (full mixed-$Q$ upper integration), and Theorem 8.1 (the conditional extensive sum with creation credit retained). Equation (9.2) refutes the attempted real-to-complex normalization shortcut only. These are written arguments; no machine search or computation discharged a step.

Source check: the outline SHA-256 is d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f. The GOAL, FINISH, ledger, histories, 2.8 terms/gate, earlier 2.8 note and literature map still match the pinned commit by Git blob identity. Relevant outline read coverage includes L17318–17450, L17490–17573, L17575–17655, L17794–19407, the 2.6 count excerpts, L5613–5623, and the cited source/regular-activity excerpts. Paper coverage is the bounded introductory, theorem, renormalization and stability passages identified in Section 2; neither whole paper is represented as re-proved. Only this output file changed; no editable prompt file changed. These are source/format checks, not mathematical validation.

The counterexample attempts were: free birth-depth/address entropy; recopying old volume at successive drop-outs; spending the old creation gains again on visible labels; and promoting the real denominator lower bound to the complex pair domain. The first is excluded by the graph encoding, the second is excluded by the specified recursive volume, the third is avoided by (6.4), and the fourth fails by (9.2). None is an actual Yang–Mills counterexample. No independent check has been performed.

**STOPPED at the session budget; actual 2.13 is not closed.** The exact remaining task is to establish (8.1) for the literal operations: the all-compatible creation/renewed-mark witnesses of 2.5, including the actual complete/cut precision bounds; the uniform Jacobian/normalizer and complex-pair remainder bounds in the common envelope (SA L18029–18105, L18719–18876); and hypothesis 3's exact normalized assembly from 2.10 and the formed regular activities. The real 2.8 ten-term result remains a conditional input with I1–I5/GEO/EXT/FLOW and its gate's repairs; it supplies neither that complex envelope nor the actual determinant bounds. The next decisive step is the actual envelope, keeping the full $Q$ and the field-dependent denominator; another abstract forest count would not advance the item.
