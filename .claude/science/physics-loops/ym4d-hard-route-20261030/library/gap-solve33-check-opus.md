lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T04:01Z

# Row 1297 `gap-solve33-check-opus`: cross-provider check of row 1290 (`gap-solve33-astra62`)

Status log (times from date -u in the same step):

- 2026-11-20T16:01Z: file created (save protocol); reading row 1297, row 1290 and the row-1290 output.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini Claude worker, at commit b003ef32b; one cross-provider
reading of `library/gap-solve33-astra62.md` (row 1290, gpt-6.2-astra max, 427 lines, 76 KB) by hand, line by line. Not an
audit. Verdicts: HOLDS, HOLDS AFTER CORRECTION, FAILS, each with the line of row 1290's file. Line numbers below are those of
`library/gap-solve33-astra62.md` at b003ef32b unless a file is named.

## Plan (at most eight steps; one step per response, appended before the next)

1. Setup and positive claim 1, the total-gradient bound for slow lattice states: L15-L52, statements (1)-(3); the cited
   midpoint identity B3 of row 947 (`gap-fc-max.md` §§5, 7) and row 1236 (11).
2. Inputs of positive claims 2-3: L232-L345, the deleted-cut law (15), the first-moment bound, the collar estimate, the
   open-cylinder exponential moment (19), the critical tilt (20); only what (21)-(23) read.
3. Positive claim 2, the cubic onset of higher moments for the gauge-integrated deleted cut: L346-L361, (21).
4. Positive claim 3, the relative truncation estimate at the first moment: L362-L377, (22)-(23).
5. Everything else, part A: L54-L131 (midpoint radii (4), single radial probe, Gaussian-resolution threshold (6)-(9)).
6. Everything else, part B: L133-L231 (fixed spatial patch (10), thermal ratio (11)-(14)) and the parts of L232-L345 not
   read in step 2.
7. Everything else, part C: L378-L427 (positive interpolation (25), loss of positivity, (26)-(27), the remaining estimate);
   whether the main comparison restates an earlier row (grep `library/open-core.md` and the FINISH rows).
8. Verdict table (statement, line, verdict), defects ranked by what each breaks, RESULT line.

- 2026-11-20T16:02Z: plan written.

## Step 1 (written 2026-11-20T16:03Z): setup and the total-gradient bound (3), L15-L52

**Setup, L17-L23 (GUIDE in the source; I re-derived it).** For unit quaternions $|x_e-y_e|^2=2-2\,\mathrm{Re}(x_e\bar y_e)$
and $\tfrac12\mathrm{tr}(x_ey_e^{-1})=\mathrm{Re}(x_e\bar y_e)$, so the temporal-gauge electric weight is
$\exp[-\beta|x-y|^2/2]$ with spatial plaquettes split half and half into $v=e^{-V/2}$ (L17). The joint law $J$ of L19
has marginal $\nu=\psi^2dx$ because $T\psi=\lambda\psi$. The conditional independence at L23 is the parallelogram
identity $|x-z|^2+|y-z|^2=2|z-\tfrac{x+y}2|^2+\tfrac12|x-y|^2$: with $\sigma^2=1/(4\beta)$ the Gaussian weight
$e^{-2\beta|z-(x+y)/2|^2}$ times $e^{-\beta|x-y|^2/2}$ equals $e^{-\beta|x-z|^2}e^{-\beta|y-z|^2}$. This is row 947 (B3) at
$\lambda=1/2$ (`gap-fc-max.md` L137-L139, which says so: "At s = 1/(2 beta) this is the mid-slice law eta of (A7)") and
row 941 (A7) (`gap-lsivac-max.md` L141-L149). **HOLDS.**

**L25, $P=R^*R$ and equal nonzero spectra of $K=RR^*$ and $P$.** $R^*R f(x)=\mathbb E[\mathbb E[f(X)|Z]\,|\,X=x]
=\mathbb E[\mathbb E[f(Y)|Z]\,|\,X=x]=\mathbb E[f(Y)|X=x]=Pf(x)$, using that $X,Y$ are conditionally i.i.d. given $Z$. The
singular-value statement is standard; gauge and flat centre flips act by orthogonal maps of $\mathbb R^D$ on both slices
and fix $v,\psi$ and the Gaussian, so $R,R^*$ intertwine them. **HOLDS.** It restates row 941 (A7) "$P_0=B^*B$" with
$B=R$ (`gap-lsivac-max.md` L146, L149); row 1290 credits row 947 only. Citation addition, no change of content.

**L27-L42, the splitting (1) and the Hermite expansion (2).** $\langle g,Kg\rangle_\eta=\|R^*g\|_\nu^2=\mathbb E[(\mathbb E[g(Z)|X])^2]$,
so $\mathcal E(g)=\mathbb E\,\mathrm{Var}(g(Z)|X)$. Conditioning further on $(X,Y)$, on which $Z$ depends only through $W$
and the independent $G$, the law of total variance gives (1) with $\mathbb E[g(Z)|X,Y]=Ag(W)$. For (2): from
$Ag(w)=\int g(s)\sigma^{-D}\phi((s-w)/\sigma)ds$ and $\partial^\alpha\phi=(-1)^{|\alpha|}H_\alpha\phi$ one gets
$\partial^\alpha Ag(w)=\sigma^{-|\alpha|}\mathbb E_G[g(w+\sigma G)H_\alpha(G)]$, as stated at L34. Parseval in the orthogonal
basis $H_\alpha/\sqrt{\alpha!}$ (completeness as argued at L35) gives
$\mathrm{Var}_G=\sum_{\alpha\ne0}\sigma^{2|\alpha|}(\partial^\alpha Ag)^2/\alpha!$, and the count of ordered $k$-tuples with
multi-index $\alpha$ is $k!/\alpha!$, so $\sum_{|\alpha|=k}(\partial^\alpha Ag)^2/\alpha!=\|\nabla^kAg\|_{\rm HS}^2/k!$. With
$\mathbb E_G\mathbb E_W$ the first term of (1) is the series in (2), and $W$ has law $\omega$. The integrability remark
(L42): $\mathbb E g(Z)^2<\infty$ gives $\mathbb E_Gg(w+\sigma G)^2<\infty$ for $\omega$-a.e. $w$, which is all (2) needs;
the boundedness of band functions follows from compactness of $P$ (continuous kernel on compact $M$),
$g=r^{-1}R(R^*g)$ for an eigenvalue $r>0$, and $R$ preserving bounded functions. **HOLDS.**

**L44-L50, the total-gradient bound (3) (positive claim 1).** Spectral support of $g$ in $[1-\delta,1]$ for $K$ gives
$\mathcal E(g)\le\delta\|g\|^2=\delta$. Both terms of (1) are nonnegative, so each is $\le\delta$: this is the third bound.
$\mathbb E g(Z)^2=\mathbb E(Ag(W))^2+\mathbb E\,\mathrm{Var}_G$, so $\|h\|_\omega^2=1-(\text{first term})\in[1-\delta,1]$. The
$k=1$ term of (2) gives $\sigma^2\int|\nabla h|^2d\omega\le\delta$, i.e. $\int|\nabla h|^2d\omega\le4\beta\delta$, a sum over all
$D=12n^3$ ambient directions with no volume factor. $\mathbb E\,h(W)=\mathbb E\,g(Z)=0$. The closing GUIDE remarks:
$\delta=1-e^{-aE}\le aE$ is right, so $4\beta\delta\le4a\beta E\to0$ when $a\beta\to0$; the gradient is on $\omega$, not on
$\nu$, as L50 says. **HOLDS.** Nothing in (1)-(3) uses the Wilson weight beyond the midpoint conditional independence: the
same bound holds for any reversible two-step chain factored through a Gaussian midpoint. That is a fact about the
statement's strength, not a defect.

**Novelty of (1)-(3).** Grep of `library/` for "Hermite", "total gradient", "4 beta delta": the Hermite hits
(`gap-solve19/22/23-astra62.md`, `gap-rotgeom-opus.md`) are unrelated uses; row 941 (A7) has the factorisation but not the
variance splitting or the gradient bound. I find no earlier statement of (3) in the lane.

**L52 (OPEN in the source): the sufficient condition.** If $\mathrm{Var}_\omega(h)\le C_a\int|\nabla h|^2d\omega$ for
invariant $h=Ag$, then for centered $g$: $\|g\|^2=\|h\|_\omega^2+T_1$ with $T_1$ the first term of (1), and
$\int|\nabla h|^2d\omega\le4\beta T_1$, so $\|g\|^2\le(1+4\beta C_a)T_1\le(1+4\beta C_a)\mathcal E(g)$. The gap of $I-K$ is then
$\ge(1+4\beta C_a)^{-1}$, and a physical gap $\Delta$ needs $(1+4\beta C_a)^{-1}\ge ca\Delta$, i.e. $C_a=O((a\beta)^{-1})$ as
stated. **The implication HOLDS**; the Poincare inequality itself stays OPEN, as labelled.

Step 1 verdicts: L23 setup HOLDS; L25 HOLDS (restates row 941 (A7) $P_0=B^*B$; add the credit); (1) L27-L31 HOLDS;
(2) L33-L42 HOLDS; (3) L44-L50 HOLDS (new in the lane as far as the grep shows); L52 implication HOLDS, inequality OPEN.

## Step 2 (written 2026-11-20T16:10Z): inputs of positive claims 2-3, L232-L345

Notation as in the source: $B_t=I_\beta(X_t,X_{t+1})^{-1}$ with $I_\beta=\int e^{-\beta D_{XY}(g)}dg$ (L221),
$D_{XY}(g)=\sum_e(1-\mathrm{Re}(\cdot))=\tfrac12\sum_e|g_z-O_eg_{z'}|^2$, $d=\min_gD$, so $1\le B\le e^{2\beta m}$ and
$B\ge e^{\beta d}$. $P$ is the periodic Wilson law (or the neutral mixture), $Q=BP/\mathbb E_PB$.

**L247, first-moment bound $0\le\log\mathbb EB^p\le-pqm\log z_\beta$ ($0\le p\le1$).** The gauge-projected kernel of the
mass-one electric convolution is $z_\beta^{-m}I_\beta$, so multiplying it by $B$ leaves $z_\beta^{-m}$ times the Haar
projection: $z_\beta^{-m}T_0$. The one-link character coefficients of $e^{-\beta(1-\mathrm{Re}u)}/z_\beta$ are positive
with value one on constants, so $\Pi\le C_\beta$ and $0\le T_0\le T$ on invariant (and neutral) functions. One cut:
$\mathrm{Tr}(T^{(N-1)/2}T_0T^{(N-1)/2})\le\mathrm{Tr}T^N$. Two cuts: $0\le A\le T^j$ gives $\lambda_k(A)\le\lambda_k(T^j)$
(Weyl), hence $\mathrm{Tr}A^2\le\mathrm{Tr}T^{2j}$. $p<1$ by Jensen; $B\le e^{2\beta m}$ since $D\le2m$, so
$\log(\mathbb EB^p/(\mathbb EB)^p)\le2q\beta m(p-1)$. $-\log z_\beta=\tfrac32\log\beta+O(1)$. **HOLDS.**
The last sentence of L245 (the deterministic factor $e^{-\beta k}z_\beta^r$ of (14) cancels in the normalized moment)
**HOLDS.**

**(16), L249-L262, orbit-distance lower bound.** With $X=1$, $Y_i=e^{\epsilon a_i}$, the zero-extended form
$\tfrac12\sum_{z,i}|g_{z+\hat i}-g_zY_i|^2$ has Hermitian symbol $3-\cos\epsilon\sum_i\cos k_i+\sin\epsilon\sum_i\sin k_i(iS_i)$,
$S_i$ = right multiplication by $a_i$: real skew, $S_i^2=-I$, pairwise anticommuting ($R_aR_b=R_{ba}$). So
$(\sum_i\sin k_i\,iS_i)^2=\sum_i\sin^2k_i\,I$, and the lowest eigenvalue is $3-\cos\epsilon\sum\cos k_i-\sin\epsilon\sqrt{\sum\sin^2k_i}$.
With $c=\sum\cos^2k_i$: $\cos\epsilon\sqrt{3c}+\sin\epsilon\sqrt{3-c}\le\sqrt{(3\cos^2\epsilon+\sin^2\epsilon)\cdot3}=\sqrt{9-6\sin^2\epsilon}$,
and $3-\sqrt{9-6s}\ge s$ iff $s^2\ge0$. Zero extension adds $\le Cb^2$ edges of energy $1/2$. The helical gauge
$g_z=e^{z_1\epsilon a_1}$ costs $1-\cos\epsilon$ per edge in directions 2, 3, zero in direction 1. **HOLDS.**

**(17), L264-L272, localized history.** For orthogonal axes and $p=e^{\alpha a_i}$, $q=e^{\alpha a_j}$:
$1-\mathrm{Re}(pq\bar p\bar q)=\tfrac12|pq-qp|^2=2|\mathrm{Im}p\times\mathrm{Im}q|^2=2\sin^4\alpha$, as stated. Ramp electric cost
$s\cdot O((\epsilon/s)^2)$ per site, magnetic $O(s\epsilon^4)$, lateral $O(sb^2)$. **HOLDS.**

**L274, Haar-preserving insertion.** In tree gauge the map is $U'_e=(g_z^{U})^{-1}T_eg^U_zU_e$ on complementary edges, a
left translation depending only on the tree links; tree links and boundary tangents (template identity there) are
fixed; a plaquette meeting a box boundary uses only boundary-tangent and outside edges. Note: the time-0 face of each
box is the slice $X_0$ and stays the actual one; it matches the template value $X=1$ only up to $\eta$, on good boxes,
which is what L276 provides. **HOLDS.**

**L276, typical input boxes.** Tree-gauge links are loop holonomies of contractible loops in the box; chord triangle
inequality plus Cauchy-Schwarz gives mean squared distance $\le C_{b,s}\sum\mathbb E(1-w_p)\le C_{b,s}/\beta$ by row 1155 (9)
(`gap-solve7-astra62.md` L130-L134: $\mathbb E\exp\{c\beta\sum_S(1-w_p)\}\le C^{|S|}$ on the periodic torus, rotate-and-halve
proof; Jensen gives the first moment). Markov on the bad fraction, no independence needed. **HOLDS.**

**L278-L292, cost and payoff; (15) lower bound.** On the good event the separate minimization over cores and (16) with
the per-summand $2\eta$ perturbation give $d'\ge[(1-\eta')\sin^2\epsilon-C/b-C\eta]V_b$; the cost bound follows from (17),
$S_{\rm box}(U)\ge0$ and $Csb^3$ on bad boxes. The Haar bijection gives
$\int e^{-\beta S}B^p=\int e^{-\beta S(U')}B(U')^p\ge e^{\beta c'_pn^3}Z\,P(\text{good})$, i.e. $\mathbb EB_0^p\ge\tfrac12e^{c'_p\beta n^3}$;
$p\log\mathbb EB=O(n^3\log\beta)$ is beaten for $\beta\ge\beta_0(p)$ uniformly in $n\ge n_0(p)$. Neutral trace: twisted
traces $\mathrm{Tr}(S_\xi T^N)$ are positive (twisted Wilson weights) and $\le\mathrm{Tr}T^N$, so the untwisted component has
weight $\ge1/8$ and carries $B$ unchanged when the seam is away from the cuts. **HOLDS.** (15) as a whole **HOLDS.**

**L294, rate $c(p-1)^3$.** With $\epsilon=c_0(p-1)$, $s=\lceil1/\epsilon\rceil$: surplus
$(1-\cos\epsilon)[2(p-1)-p(1-\cos\epsilon)]\ge(p-1)\epsilon^2-p\epsilon^4/4$, ramp $C(\epsilon^2/s+s\epsilon^4)\le3C\epsilon^3$; for
$c_0\le\min(1/2,1/(12C))$ the net is $\ge\tfrac12c_0^2(p-1)^3$ before the $b,\eta,\eta'$ losses, which are then taken small
(depending on $p$). **HOLDS** with an absolute $c$ (about $c_0^2/16$ after $V_b\ge n^3/8$).

**(18), L298-L319, curvature controls orbit distance.** I re-derived each step: $|a/|a|-b/|b||\le2|a-b|/|a|$ with $O_e$
orthogonal; regression $U=AH_z+\zeta$, $\mathbb E[|AH|^2/|H|^2]=\|A\|_{\rm HS}^2/4$ (isotropy in $\mathbb R^4$),
$\mathbb E|H|^{-2}=1/(4-2)=1/2$, so $\mathbb E|U|^2/|H_z|^2\le\tfrac12\mathbb E|U|^2$ and $\mathbb E|g_z-O_eg_{z'}|^2\le2\mathbb E|U|^2$;
$\sum_\alpha\phi(z-\alpha)^2=1$ makes $H_z$ standard. Path loop for an edge in direction 1 = two width-one rectangles of
length $\le b$ (one for direction 2), so the holonomy is a product of $\le Cb$ conjugated plaquettes in each of $X,Y$;
$|1-U|^2=2(1-\mathrm{Re}U)$ and translation over $z$ at fixed offset gives $Cb^2S_{\rm mag}$. **HOLDS.**

**(19), L321-L325, collar estimate.** $\sqrt{2d}$ is the orbit distance of the product chord metric under the compact
isometric gauge action, so it obeys the triangle inequality; one temporal layer costs squared chord $2\times$(electric
deficit); Cauchy-Schwarz over $t\le b$ layers gives $d\le bS_{\rm col}$; a depth with magnetic cost $\le S_{\rm col}/b$
exists on each side; (18) at the two chosen slices and $(\sum_1^3x_i)^2\le3\sum x_i^2$ close it. **HOLDS.**

**L327, $Q$ is the open-slab law.** After the temporal links of the cut are integrated, the $P$-weight of the spatial
history carries $I_\beta(X_0,X_1)$ (times constants); $B_0=1/I_\beta$ removes exactly this factor; slices 0 and 1 keep
full spatial weights. **HOLDS.**

**(20), L329-L334, collar exponential moment.** Row 1151's proof under its (6) (`gap-solve5-astra62.md` L87-L93) is
exactly the rotate-and-halve multi-mark bound $\mu\exp[(\beta/2)\sum_A(1-w_p)]\le C_0^{|A|}$ for marks sharing a spatial
direction on the open cylinder (Bessel-ratio ordering, $z_{\beta/2}/z_\beta\le C$, Schatten Holder around the periodic
spatial circle). Nothing in it uses that the marks lie on the end slice, so it covers interior collar faces, as L334
says; every face of a collar has a spatial direction. Holder over three groups and $|A|\le Cbv_3$ give (20); Jensen
gives the mean, and one end gives $\mathbb E_QS_{\rm mag}(\text{end})\le Cv_3/\beta$. **HOLDS.**

**(21), L336-L344, critical tilt.** $D(Q\Vert P)=\mathbb E_Q\log B-\log\mathbb E_PB\le\mathbb E_Q\log B$ and
$D(P\Vert Q)=\log\mathbb E_PB-\mathbb E_P\log B\le\log\mathbb E_PB$ since $B\ge1$. Row 1283 (38) (`gap-solve32-astra62.md`
L493-L503) gives $-\log I_\beta\le\beta d+\tfrac32v_3\log(1+\beta)+Cv_3$; I re-derived an upper bound of this form
independently (restrict $g$ to chord balls of radius $1/\beta$ about a minimizer, split
$(a+r)^2\le(1+\beta^{-1})a^2+(1+\beta)r^2$, Haar volume $(c\beta^{-3})^{v_3}$), which gives $\beta d+Cv_3\log(1+\beta)$ and
suffices. (18) at $b=\lceil\beta^{1/4}\rceil\le n/16$ at the two ends and the single-end mean give
$\mathbb E_Qd\le Cv_3(\beta^{-1/2}+\beta^{1/2}/\beta)$. **HOLDS.**

Step 2 verdicts: L247 HOLDS; (15) L234-L245 HOLDS; (16) HOLDS; (17) HOLDS; L274, L276, L278-L292 HOLD; L294 HOLDS;
(18) HOLDS; (19) HOLDS; L327 HOLDS; (20) HOLDS; (21) HOLDS. No correction needed in this block.

## Steps 3-4 (written 2026-11-20T16:12Z): positive claims 2 and 3, L346-L376

**(22), L346-L360, cubic onset of the higher moments (positive claim 2).**
*Lower bound.* L294 with $p=1+h$, $0<h\le1$: $\log(\mathbb E_PB^{1+h}/(\mathbb E_PB)^{1+h})\ge ch^3\beta v_3$ for
$n\ge n_0(h)$, $\beta\ge\beta_0(h)$, both sectors, one or two cuts (step 2). So $\liminf\ge ch^3$ over any joint passage
$n,\beta\to\infty$. *Upper bound.* $\mathbb E_PB^{1+h}/(\mathbb E_PB)^{1+h}=\mathbb E_QB^h/(\mathbb E_PB)^h\le\mathbb E_QB^h$ since
$\mathbb E_PB\ge1$. Per cut, (38) and (19) give $\log B\le\beta d+Cv_3\log(1+\beta)$ and $d\le C(v_3/b^2+bS_{\rm col})$,
which is the display at L357 (two cuts: add). With $b=\lfloor c_0/h\rfloor\ge c_0/(2h)$ and $Chb\le Cc_0\le c$ of (20),
$S\ge0$ gives $\mathbb E_Qe^{C\beta hbS}\le\mathbb E_Qe^{c\beta S}\le e^{Cbv_3}\le e^{Cc_0v_3/h}$, and
$\beta hv_3/b^2\le4\beta h^3v_3/c_0^2$. Hence $\log\mathbb E_QB^h\le Chv_3\log(1+\beta)+C\beta h^3v_3+Cv_3/h$, and after
division by $\beta v_3$ the first and last terms vanish as $\beta\to\infty$ at fixed $h$. The geometric conditions
($2\le b\le n/8$, slab length $>2b+3$, disjoint collars) hold for $n\ge n_0(h)$. Neutral sector: the twist sits on a
deleted seam (L327), $B$ uses the flipped end field, and (18)-(19) apply after flipping one whole collar, which keeps
every plaquette deficit (L325). **HOLDS.** Grep: no earlier statement of a cubic onset or of $(p-1)^3$ moment rates in
`library/` or in the FINISH rows (only rows 1290 and 1297 match); `library/open-core.md` has no match. New in the lane.

**(23), L362-L366, better first derivative.** For an edge in direction 1 the loop of the two ordered paths and the
edge is the product of two conjugated width-one rectangle loops (planes (1,2) and (1,3), lengths $\le b+1$); one for
direction 2, none for direction 3. With $P^{-1}O_eP$ = left multiplication by the $X$-holonomy and right
multiplication by the inverse $Y$-holonomy, $\|I-L_xR_{y^{-1}}\|_{\rm HS}^2\le2(4|1-x|^2+4|1-y|^2)$ and
$|1-x|^2\le2\sum_R|1-R|^2=4\sum_R(1-w_R)$, so the path part of $\mathbb E|U|^2$ is $C\sum_R[(1-w_R(X))+(1-w_R(Y))]$.
Row 1151 (4) (`gap-solve5-astra62.md` L60-L64) proves $1-\mathbb E w_R\le Cq(R)/\beta$ for $q<n$ at an end of the open
cylinder: the rectangle's long direction as transfer time makes $\mathbb Ew_R$ the $q$-th moment of a nonnegative
variable of mean $\mathbb Ew_{1\times1}$, Jensen gives $\mathbb Ew_R\ge(\mathbb Ew_p)^q$, and the half-tilt gives
$1-\mathbb Ew_p\le C/\beta$. I re-derived both inequalities. Flat flips keep contractible loops. So
$\mathbb E_Qd\le Cv_3/b^2+Cv_3b/\beta$, at $b=\lceil\beta^{1/3}\rceil\le n/16$ this is $Cv_3\beta^{-2/3}$, and (38) gives (23).
**HOLDS.**

**(24), L368-L374, relative truncation at the first moment (positive claim 3).** Take $h=\beta^{-1/4}$,
$b=\lfloor c_0\beta^{1/4}\rfloor$ in the finite-volume estimate above: $\beta hv_3/b^2\le4\beta^{1/4}v_3/c_0^2$,
$bv_3\le c_0\beta^{1/4}v_3$, so $\log\mathbb E_QB^h\le C\beta^{1/4}v_3+C\beta^{-1/4}v_3\log(1+\beta)$. Exponential Markov:
$Q(\log B>K\sqrt\beta v_3)\le\exp[(C+o(1)-K)\beta^{1/4}v_3]$, and
$\mathbb E_P[B{\bf1}_{\log B>t}]/\mathbb E_PB=Q(\log B>t)$. With $K\ge C+2$ this is (24), for $\beta$ large and slab sizes
$\ge C\beta^{1/4}$ (from $b\le n/8$, slab $>2b+3$). Clipping remark: $B_t\ge1$, so if $\min(B_0,M)\min(B_j,M)\ne B_0B_j$
then $B_0B_j>M$; the relative loss of each first moment is $\le\mathbb E_P[B{\bf1}_{B>M}]/\mathbb E_PB$, bounded by (24)
for $B=B_0$ and for $B=B_0B_j$. So each logarithm moves by $O(e^{-c\beta^{1/4}v_3})$. **HOLDS** for the ratio of first
moments; its use in (9) is read in step 6. New in the lane (same grep as for (22)).

**L376, the smaller cap.** Markov on $\log B$ under $Q$ with (23): $Q(\log B>A_\beta v_3[\beta^{1/3}+\log(1+\beta)])\le C/A_\beta$
(two cuts: $2C$). **HOLDS.** The closing sentence ("they leave a two-period expectation of two bounded but collective
spatial observables to evaluate") is a correct description: the truncations bound a cutoff error, not the ratio.

**What the three positive claims do not give.** (3) bounds the ambient gradient of a slow state on the midpoint law
$\omega$; the Poincare inequality that would turn it into a gap is the OPEN item at L52. (22) and (24) are statements
about the exactly deleted tilt $Q$; they control truncation errors in the thermal ratio, not the ratio itself. None of
them is a step of a mass-gap proof by itself, and the source does not claim it is.
