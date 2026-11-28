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

## Step 5 (written 2026-11-20T16:15Z): everything else, part A, L54-L131

**L63-L67, $\|P_{\exp(\beta A_e/2)}\|\le C_0$.** The insertion halves the coupling on $e$; the mass-one convolution at
$\beta/2$ is below the one at $\beta$ (character multipliers $I_d(\kappa)/I_1(\kappa)$ increase with $\kappa$), times
$z_{\beta/2}/z_\beta\le C$. So $0\le T'\le CT$ on $L^2(\text{Haar})$, and $P'=\lambda^{-1}M_\psi^{-1}T'M_\psi$ is unitarily
$\lambda^{-1}T'$; $\lambda=\|T\|$ on the unprojected space because the Perron-Frobenius vector is unique, positive and
hence invariant. **HOLDS.**

**L69, (5).** $\beta A^2\le C\beta^{-1}e^{\beta A/2}$ on $[0,2]$ ($x^2e^{-x/2}\le16/e^2$); pointwise domination of nonnegative
kernels gives $\|P_B\|\le Ck/(\beta u)=b_0$. $p=\mathbb E[\bar f(X)(f(X)-f(Y)){\bf1}_B]+\langle f,P_Bf\rangle\le\sqrt{2\delta p}+b_0$
with $\mathbb E|f(X)-f(Y)|^2=2\langle f,(I-P)f\rangle\le2\delta$; solving the quadratic gives $\sqrt p\le\sqrt{b_0}+\sqrt{2\delta}$.
**HOLDS.**

**L56-L61 and L75, (4).** $|W_e|^2=(1+X_e\cdot Y_e)/2=1-A_e/2$; $1-s_e=A_e/(2(1+s_e))\le A_e/2$, so
$\sum(1-s_e)^2\le u/(4\beta)$ on $B^c$ and $|s-t|^2/\sigma^2\le(u/\beta)\cdot4\beta=4u$; the Gaussian $\chi^2$ is
$e^{|s-t|^2/\sigma^2}-1$, data processing to radii, joint convexity of $\chi^2$ for the mixture $\bar Q$;
$J(B^c)\ge1-b_0\ge1/2$ gives $\|b\|_{L^2(\bar Q)}\le\sqrt2$; good part $\le\sqrt2\sqrt{e^{4u}-1}\le C\sqrt u$, bad part
$\le(1+\sqrt2)\sqrt p$; $u=\sqrt{k/\beta}$ makes both $C(k/\beta)^{1/4}$. The $K$-band version: $g=RP^{-1/2}f$ with
$RP^{-1/2}$ unitary between the bands, so $\langle g,b\rangle_\eta=\mathbb E[(P^{-1/2}f)(X)b(R_I)]$ with
$\|P^{-1/2}f\|\le(1-\delta)^{-1/2}$. **HOLDS.**

**L77, forest extension.** Haar vertex averaging fixes the triple law and $f(X)$; on a tree, exposing a root frame and
then each child frame makes the edge directions independent uniform given the radii; conditional expectation does not
raise the $L^2$ norm. **HOLDS.**

**L81-L104, single-probe cyclicity.** (6): $\mathbb E\,e^{-t|W+\sigma G|^2}=(1+2t\sigma^2)^{-2}e^{-t|W|^2/(1+2t\sigma^2)}$ in
$\mathbb R^4$ with $2t\sigma^2=t/(2\beta)$ and $|W|^2=(1+X\cdot Y)/2$; the new coefficient of $X\cdot Y$ is
$\beta-t\beta/(2\beta+t)=\beta/(1+t/(2\beta))$; the insertion sits between $R^*$ and $R$, and
$R^*M_bRf(x)=\mathbb E[f(Y)\mathbb E[b(Z)|X,Y]\,|\,X=x]$ by conditional independence. **HOLDS.** $l_d$ (L90): the
$SU(2)$ multiplier of $e^{\kappa\mathrm{Re}u}/\int e^{\kappa\mathrm{Re}u}$ on dimension $d$ is $I_d(\kappa)/I_1(\kappa)$
($\int e^{\kappa\cos\theta}\chi_d\,d\mu=(2d/\kappa)I_d(\kappa)$); $l_{d+1}/l_d<1$ because $I_{d+1}/I_d$ increases strictly and
$\beta'<\beta$. **HOLDS.** L94: $B$ and $B^*$ injective, polar part unitary;
$U(B^*L_eB)U^*=(BB^*)^{1/2}L_e(BB^*)^{1/2}$; $K_\epsilon=F^{1/2}(F+\epsilon)^{-1/2}\to I$ strongly and
$K_\epsilon L_eK_\epsilon\to L_e$ strongly; the same with $C^{1/2}(C+\epsilon)^{-1/2}$ recovers $M_v^2$, and $\log$ gives $V$.
**HOLDS.** (7), L96-L102: $-1$ acts as $(-1)^{d-1}$; $S_\xi VS_\xi^*$ multiplies $w_{p'}$ by $\prod_{\partial p'}\xi$; the
weighted average kills the constant and every $p'\ne p$ (distinct edge sets for $n\ge4$). **HOLDS.** L104: $B\psi=U\psi$
since $|B|\psi=\psi$; $C^{1/2}B\psi=CM_v\psi/\sqrt\lambda=\sqrt\lambda M_v^{-1}\psi$ from $M_vCM_v\psi=\lambda\psi$. The algebra
contains $C$, $M_v$ (so $T$), every $M_{w_p}$ and every single-link spin projection, i.e. all generators of row 1246
(4) (`gap-solve28-astra62.md` L84-L90), whose "in fact" clause gives every bounded invariant multiplication; that
statement was checked as S9 HOLDS in `gap-solve28-check-opus.md` L48, L134 (same provider as this check). Cyclicity
follows. **HOLDS.** L106 OPEN: the stated implication (a common decay rate for all centered words bounds the neutral
spectral edge, by cyclicity) is correct at fixed cutoff; the bound itself is OPEN.

**L110-L120, the noise threshold $\tau\ge1/(4\beta)$.** (8): $|z-(x+y)/2|^2=|z|^2-z\cdot x-z\cdot y+(1+x\cdot y)/2$ for unit
$x,y$, so the marked factor is $e^{z\cdot x/(2\tau)}e^{(\beta-1/(4\tau))x\cdot y}e^{z\cdot y/(2\tau)}$ times a scalar in $z$.
At or above threshold: positive-definite middle convolution (GL3), identical real end multipliers, nonnegative
reading: positive semidefinite. Below: at $z=0$ the convolution is $e^{|\gamma|(-x)\cdot y}$, multiplier
$(-1)^{d-1}I_d(|\gamma|)/I_1(|\gamma|)$, negative at $d=2$; $w_p$ has pure spin 1/2 on its four edges, so
$\langle v^{-1}w_p,\cdot\,v^{-1}w_p\rangle<0$; continuity in $z$ and a small ball finish. Positivity is a congruence
property, so it is the same on $L^2(\nu)$. **HOLDS** (both directions).

**L122, exact rank-one cut.** Pins at threshold delete electric factors (factor 1 at $z=0$). On invariant functions
$\Pi_S\otimes C_{S^c}$ has range in invariant functions of $S^c$ links: constants if $S^c$ is a forest (transitive
gauge action), and the operator is then $|1\rangle\langle1|$ since $C1=1$; a cycle in $S^c$ gives the adjoint loop
character, centre blind, eigenvalue $\prod c_3>0$, so rank $\ge2$. $|S|\ge3n^3-(n^3-1)=2n^3+1$. **HOLDS.**

**L124-L129, (9).** The pinned step is $c|v\rangle\langle v|$; one pin in period $j$:
$c\langle v,T^{j-1}v\rangle/\mathrm{Tr}T^j$; two pins at separation $j$ in period $2j$: $c^2\langle v,T^{j-1}v\rangle^2/\mathrm{Tr}T^{2j}$;
the ratio is $(\mathrm{Tr}T^j)^2/\mathrm{Tr}T^{2j}$. **HOLDS.** L131 OPEN is a fair statement of what (4)-(5) do not give.

Step 5 verdicts: L56-L61 (4) HOLDS; L63-L67 HOLDS; (5) L69 HOLDS; L75 HOLDS; L77 HOLDS; L81 HOLDS (given row 1246 (4),
checked); (6) L83-L92 HOLDS; L94 HOLDS; (7) L96-L102 HOLDS; L104 HOLDS; L110 HOLDS; (8) L112-L118 HOLDS; L120 HOLDS;
L122 HOLDS; (9) L124-L129 HOLDS. OPEN items L106, L131 correctly labelled.

## Step 6 (written 2026-11-20T16:19Z): everything else, part B, L133-L231

**(10), L135-L143, a fixed patch has vanishing overlap with the slow band; proof L145-L180.**
- L145-L154: gauge averaging keeps the pairing with invariant $f(X)$ and lowers the norm; in temporal gauge with the
  lower tree gauge, $(gZ)_e=1+(D_e+(gG)_e/2)/\sqrt\beta$ since $\sigma=1/(2\sqrt\beta)$, and $gG$ has the law of $G$. **HOLDS.**
- (11), L156-L163: $|D_e|\le\sqrt\beta[\sum_{p}|U_p-1|+\sqrt{A_e/2}]$ over a fixed word of lower-box plaquettes, so
  $|D|>H$ forces $\beta(1-w_p)>c_IH^2$ on one of finitely many plaquettes. Electric ones: $1_E\le e^{\beta A_e/2-c_IH^2/2}$
  and the argument of (5). Spatial ones: $\mathrm{Tr}(({\bf1}_EU^2{\bf1}_E)^l)/\mathrm{Tr}U^{2l}$ is the probability of $E$ on
  $l$ alternate slices, $\le C^le^{-cul}$ by row 1155 (9); $\|A\|^l\le\mathrm{Tr}A^l$ for $A\ge0$ and
  $\mathrm{Tr}U^{2l}\to1$ give $\|{\bf1}_EU^2{\bf1}_E\|\le Ce^{-cu}$; for $\varphi$ in the band,
  $\|{\bf1}_E\varphi\|^2=\|{\bf1}_EU\varphi'\|^2\le\|{\bf1}_EU^2{\bf1}_E\|(1-\delta)^{-2}$ with $\varphi'=U^{-1}\varphi$. **HOLDS.**
- L165: the law of $D+G/2$ has density $\ge c_Ie^{-2(|u|+H_0)^2}$; Cauchy-Schwarz against it bounds $a_\beta$ and
  $\nabla a_\beta$ on $|d|\le H+1$ (integrand $\sim e^{-4|u-d|^2+2(|u|+H_0)^2}$, integrable); Arzela-Ascoli gives $a_H$;
  the clipping error is $|\mathbb E[\bar f(1-\chi_H(D))b]|\le$ (11). **HOLDS.**
- L167-L171, Gaussian limit of the readings: the double telescoping bound
  $|\prod U_k-1-\sum(U_k-1)|\le\sum_{l<k}|U_l-1||U_k-1|$ is right, and $\sqrt\beta\,\mathbb E|U_l-1||U_k-1|\le C\beta^{-1/2}$. The
  comparison rests on row 1151 (24) and the density bound in its proof (`gap-solve5-astra62.md` L300-L318: the true
  density relative to product open-box Wilson measures is $\le\exp(CV\Delta_b)$, chart exit $\le e^{-c\beta/b^8}$ by row
  1143's shelling, Gaussian Lipschitz concentration), and on row 1231 (1), (8), (9) (`gap-solve26-astra62.md` L24, L91,
  L99). Row 1151 states (24) for plaquette **radii**; row 1290 uses four-component based loops in box frames. The
  extension is argued in two sentences (L169, L171). I re-traced it: the density bound is on the full tree-gauge
  coordinates, the readings $a_H$ are invariant under the common root conjugation, so each can be computed in the
  frame of the tiling box that contains its window, and a product of two clipped readings is again bounded Lipschitz in
  the linear curls. $h=\lceil\beta^{1/16}\rceil$ satisfies row 1151's constraint $\gamma<1/12$, and $\beta_j\le B\log n_j$ gives
  $\Delta_h=(\log\beta)(1/h+h/n)\to0$. **HOLDS**, as an implication from rows 1151 and 1231 (both checked: row 1151 (4),
  (6) HOLD in `gap-solve5-check-opus.md` L558, L562).
- L173: window covariances are Fourier coefficients of a bounded symbol, so they vanish at large time separation
  (Riemann-Lebesgue); Gaussian characteristic functions factor; Cesaro variance $\to0$. **HOLDS.**
- L175-L180: stationarity, $\mathbb E|f(X_s)-f(X_0)|^2=2\langle f,(I-P^s)f\rangle\le2s\delta_j$, Cauchy-Schwarz against the
  variance of the $m_0$-average, then $m_0\to\infty$, then $H\to\infty$. The order of quantifiers is right: the subsequence
  and $a_H$ may depend on $H$, the bound $C_Ie^{-c_IH^2}$ does not. **HOLDS.**
- (10) as a whole: **HOLDS** (implication from the cited rows' weak-coupling comparison). L182 OPEN is correct: (10) is
  about one fixed patch; a physical cube has a growing number of patches.

**(12), L188-L200, coupling change by a radial mark, and its impossibility at large variance.**
$\mathbb E e^{-t|W+\sqrt\tau G|^2}=(1+2t\tau)^{-2}e^{-t|W|^2/(1+2t\tau)}$ and $t/(2(1+2t\tau))=\kappa$ give $t=2\kappa/(1-4\kappa\tau)$;
$e^{-\kappa(1+X\cdot Y)}$ lowers the coupling by $\kappa$. At $\tau=1/(4\kappa)$ the density at zero is $\propto e^{-2\kappa|W|^2}$. The
converse: $h(se_1)$ is entire (the marginal density $\ge(2\pi\tau)^{-2}e^{-(|z|+1)^2/(2\tau)}$ makes $b\phi_\tau(\cdot-se_1)$
integrable locally uniformly in $s$); on the neutral space, plaquette characters of every spin on $e$ fix the central
one-link kernel, so $h=ce^{-2\kappa|w|^2}$ on $0<|w|<1$ and by analyticity everywhere; then
$e^{-y^2/(2\tau)}h(iye_1)=\int b\phi_\tau e^{iyz_1/\tau}\to0$ (Riemann-Lebesgue, $b\phi_\tau\in L^1$) contradicts
$ce^{(2\kappa-1/(2\tau))y^2}$ for $\tau\ge1/(4\kappa)$. **HOLDS.**

**L202-L217, (13).** $s=t_x(-1)^{y+z}$: every transverse bond and the two longitudinal cross sections at $x=0|1$ and
$x=n-1|0$ have unequal signs, $k=2n^3+2n^2$, complement = paths $x=1..n-1$ plus the isolated vertices at $x=0$. Multiplying
the cut's temporal links by the central signs $s$ maps $w_e\to s_us_vw_e$, reversing exactly the $S$ terms, so
$\mathbb E[L^2|\text{spatial}]=1$. $L\ge e^{-\beta k}$ pointwise; deletion in mass-one convention gives $\le e^{-\beta k}z_\beta^{-k}$;
$\log(\mathbb EL^2/(\mathbb EL)^2)=-2\log\mathbb EL\in[2\beta k+2k\log z_\beta,2\beta k]$. Conditional Jensen for noisy estimators.
**HOLDS.**

**L219-L228, (14).** Numerator: leaves of the retained forest integrate to $e^\beta z_\beta$ each, isolated vertices to 1;
denominator $e^{\beta m}I_\beta$; so $H=e^{-\beta k}z_\beta^r/I_\beta$. $H\le(\mathbb E[L^2|X,Y])^{1/2}=1$. **HOLDS.** With (14), the
ratio (9) is $\mathbb E_{2j}[B_0B_j]/(\mathbb E_jB_0)^2$ up to the cancelling deterministic factors, so the clipping remark
under (24) (step 4) applies to (9) as stated. L230 OPEN is correctly labelled.

**L186 (GUIDE).** Attribution of the empty-diagram identity to row 1151 (26); not load-bearing; not checked further.

Step 6 verdicts: (10) L135-L143 HOLDS (with L145-L180 each HOLDS); (11) HOLDS; (12) L188-L200 HOLDS; L202-L208 HOLD;
(13) HOLDS; (14) HOLDS.

## Step 7a (written 2026-11-20T16:21Z): everything else, part C, L378-L427

**L380-L386 (GUIDE), (25) endpoints.** $I_\beta(X,Y)=I_\beta(Y,X)$ ($g\to g^{-1}$, $a(u)=a(u^{-1})$). With the closing kernel
$v\,z_\beta^{-m}I_\beta\,v$: $\mathrm{Tr}T^j=Z_{\rm slab}z_\beta^{-m}\mathbb E_\mu K$ and
$\mathrm{Tr}T^{2j}=Z_{\rm slab}^2z_\beta^{-2m}\mathbb E_{\mu\otimes\mu}[K(X_1,Y_2)K(X_2,Y_1)]$, so the slab and $z_\beta$ factors cancel
and $J(1)=\log[(\mathrm{Tr}T^j)^2/\mathrm{Tr}T^{2j}]$, $J(0)=0$. **HOLDS.**

**L388, $|J(u)|\le Cuv_3[\beta^{1/3}+\log(1+\beta)]$.** $K\le1$ gives $\log\mathbb E K^u\le0$; Jensen gives
$\log\mathbb EK^u\ge u\,\mathbb E\log K=-u\,\mathbb E\log B$; so $J(u)\in[-2u\,\mathbb E_\mu\log B,\ u\,\mathbb E_{\mu\otimes\mu}(\log B_{12}+\log B_{21})]$.
$\mathbb E_\mu\log B=\mathbb E_Q\log B$ is (23); the crossed pairs need (23) for ends of independent slabs, which its
proof covers (one-end marginals only, L366). Neutral kernel: concavity of $\log$ over the eight twists. **HOLDS.**

**L390-L412, loss of positivity of $K^u$.**
- (26), L392-L398: $I_\beta=e^{-\beta m}\int_\Gamma e^{\beta x\cdot\gamma y}d\gamma$ since $\mathrm{Re}(X_eg_yY_e^{-1}g_x^{-1})=X_e\cdot(g_xY_eg_y^{-1})$;
  $x(\bar t)=\overline{x(t)}$ (real Taylor coefficients) and $\int\gamma^{\otimes\ell}=\mathrm{Proj}_\Gamma$ real symmetric give
  $K(t,\bar t)=e^{-\beta m}\sum\beta^\ell\|\mathrm{Proj}_\Gamma x(t)^{\otimes\ell}\|^2/\ell!\ge e^{-\beta m}$. **HOLDS.**
- L400-L404, $F$ entire with $|F(c)|\le C_{n,\beta}e^{C_\beta\sqrt{1+|c|}}$: global conjugation by $a_2$ is in $\Gamma$, fixes the
  identity configuration and sends $l\to-l$; an even entire function of $l$ is entire in $l^2$; $F(c)=G(c,1-c^2)$. The
  spherical average of $e^{\beta q\cdot w}$ is $\sum_r\beta^{2r}\mathbb Eq_1^{2r}(w\cdot w)^r/(2r)!$, of modulus
  $\le e^{\beta\sqrt{|w\cdot w|}}$; with $B_1=g_{z'}$, $B_2=a_1g_{z'}$ orthonormal and $c^2+l^2=1$,
  $w\cdot w=|A|^2+1+2cA\cdot B_1+2lA\cdot B_2$, $|l|\le C(1+|c|)$. **HOLDS.**
- L406, nonconstancy: $\int q_1e^{\beta q\cdot v}dq=(1\cdot v)\int q_1e^{\beta q_1}$ for unit $v$; the power expansion has
  nonnegative coefficients and nonnegative sphere moments; the plaquette term with one common coordinate at four
  vertices is strictly positive; flat twists have sign one around a plaquette. So $\int F(\mathrm{Re}U)\mathrm{Re}U\,dU>0$,
  impossible for constant $F$. **HOLDS.**
- L408: no zero $\Rightarrow F=e^G$, $|G'(c_1)|\le2[\sup_{|c-c_1|=R}\mathrm{Re}G-\mathrm{Re}G(c_1)]/R\to0$, contradiction; $F>0$ on
  $[-1,1]$ puts $c_*$ off $[-1,1]$, so $\sin t_*\ne0$ and the order is kept. **HOLDS.**
- L410-L412: PSD of $K^u$ on invariant $L^2$ gives PSD real-point Gram matrices (invariant bump approximations, continuity);
  Taylor coefficient matrices at real points are PSD; Cauchy bounds give a holomorphic Gram map; (26) gives a positive
  conjugate diagonal, hence branches with a common radius along a compact path; $f(t)=\langle v(t),v(0)\rangle$ obeys
  $K(t,0)f'=u\,\partial_tK(t,0)f$ by continuation; at a zero of order $k$ the leading terms give $\mathrm{ord}f=uk$, not an
  integer for irrational $u$ or $0<u<1/k$. If the path meets an earlier zero of $K(\cdot,0)$, the same contradiction
  arises there. **HOLDS.**

**(27), L416-L423.** $\frac{d}{du}\log\mathbb EK^u=\mathbb E[K^u\log K]/\mathbb EK^u$, with $\log K$ bounded at fixed cutoff. **HOLDS.**
The attribution to row 1151 (28) is GUIDE.

**L425 (OPEN) and L427 (RESULT).** Correctly labelled: (22) and (24) bound truncation costs, (27) is unestimated, (3)
needs the OPEN Poincare bound of L52. The cited threshold $J(1)\le y_0V(s)/(2(96T_0)^3)$ is read in step 7b.

Step 7a verdicts: L386 HOLDS; L388 HOLDS; L390 HOLDS (proof L392-L412, each HOLDS); (26) HOLDS; (27) HOLDS.

## Step 7b (written 2026-11-20T16:24Z): cited thresholds and scope, and the restatement question

**L425, the required threshold.** Row 1218's reading (`prior/gap-onebound-read-sol.md` L84-L101) states A-B** as
$Z(s,T_0)^2\le e^{\gamma V(s)}Z(s,2T_0)$ for $2T_0\le s_i<48T_0$, $\gamma=y_0/(2(96T_0)^3)$, on the full gauge-invariant slice
space. With $j=T_0$ and $J(1)=\log[(\mathrm{Tr}T^j)^2/\mathrm{Tr}T^{2j}]$ this is exactly $J(1)\le y_0V(s)/(2(96T_0)^3)$, and for
these shapes $\gamma V(s)\in[8y_0/(2\cdot96^3),\,48^3y_0/(2\cdot96^3))$, of order one. **HOLDS** (citation and arithmetic).

**GUIDE citations of the Sussman-Alpoge texts, fetched at `31a47c543775` into a scratch folder.** Outline L31858-L31882:
the reconstructed scalar sector does not identify a full Yang-Mills algebra, and "Nor does polynomial clustering
establish a mass gap" with the $Ee^{-E}dE$ example. Complete account I L2704-L2712: "Not asserted: ... a mass gap".
Outline L2195-L2213 is GL3 ($c_l=(2e^{-\beta}/\beta)I_{2l+1}(\beta)>0$), L2313-L2335 the positive trace-class transfer, L1733-L1762
the exact projection symbol. Each GUIDE statement of row 1290 that cites them (L7, L17, L171) is accurate, and the
credit to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is given. The repo-search
paragraphs L3-L5 about PR branches and main were not re-checked (GUIDE, not load-bearing).

**Is the main comparison a restatement of an earlier row?** The note's main comparison is the one-period against the
two-period deletion first moment, i.e. the thermal ratio $J(1)=\log[(\mathrm{Tr}T^j)^2/\mathrm{Tr}T^{2j}]$ in its three forms: pin
densities (9), scalar orbit integrals (14) with (25), and the signed interpolation (27). **Yes, in substance it is a
restatement, and row 1290 discloses it.**
- (9) is row 1151's empty-diagram identity (26), $e^{-J}=p(0)^2/\Pi(0,0)$ (`gap-solve5-astra62.md` L338-L342): the empty
  diagram is complete deletion of the seam, which is rank one. Row 1290 rewrites it with Gaussian pin densities and
  needs only a spanning-tree complement. L129 and L186 credit row 1151 (26), Theorem ZD-c and row 1218.
- The ratio itself is the thermal-doubling quantity of Theorem ZD-c and of A-B** (Bhattacharjee, Bhattacharya,
  Lockwood, Romanov, Sessford and Singha Roy, as read in row 1218).
- (27) is the analogue of row 1151's signed coupling interpolation (28) (L411-L416), along the power $u$ of the orbit
  kernel instead of the plaquette couplings. L423 credits it.
- The deletion tilt $Q$ is row 1151 §3's open cylinder ("the actual Wilson cylinder with the temporal seam open, with both
  spatial boundary weights included", L41). Row 1151 also already noted that the ratio of the two very small deletion
  probabilities needs relative control (L344-L346) and that clipping complete-deletion moments needs a large cap
  (L354-L356).

**What is not a restatement** (grep of `library/`, `library/open-core.md` and the FINISH rows; only rows 1290 and
1297 match): the quantitative control of the gauge-integrated deleted cut, i.e. (15) with the $(p-1)^3$ rate, (21),
(22), (23), (24); the noise threshold with the minimum pin count $2n^3+1$ (L110-L122); (12) and its converse; the loss
of positivity of $K^u$ (L390-L412); the total-gradient route (1)-(3) with the reduction at L52. Row 1151's (23) is an
exponential moment past complete deletion for **sparse** one-class face sets with an $e^{C_0|S|}$ bound; row 1290's
(15) is about the complete cut after integrating the temporal gauge, where the higher moments grow like
$e^{c(p-1)^3\beta n^3}$. The two statements are consistent and different.

**Earlier rows the steps depend on** (statement and proof read, re-derived where used): row 941 (A7); row 947 (B3); row
1149 (16) (Bessel-ratio ordering, used through rows 1151 and 1155); row 1151 (4), (6) and (24); row 1155 (9); row 1231
(1), (8), (9) (statements only, used inside the weak-coupling comparison of (10)); row 1246 (4); row 1283 (38). The Opus
checks of rows 1151, 1155, 1246 and 1283 record these as HOLDS (`gap-solve5-check-opus.md` L558, L562;
`gap-solve7-check-opus.md` L464; `gap-solve28-check-opus.md` L48; `gap-solve32-check-opus.md` L528). Those checks are by
the same provider as this one, so they are not an independent confirmation.

## Step 8 (written 2026-11-20T16:25Z): verdict table, defects, result

Every `**PROVED**` paragraph of `gap-solve33-astra62.md` (61, found with `grep -n '^\*\*PROVED'`) has one row.

| S | Line | Statement | Verdict |
|---|---|---|---|
| S1 | L25 | $P=R^*R$; equal nonzero spectra of $K,P$; symmetries intertwine | HOLDS (restates row 941 (A7); add credit) |
| S2 | L27-L42 | (1) variance splitting; (2) Hermite series on $\omega$ | HOLDS |
| S3 | L44-L50 | (3) total-gradient bound $\int\|\nabla h\|^2d\omega\le4\beta\delta$ (positive claim 1) | HOLDS |
| S4 | L56-L61 | (4) radial readings against the slow band; $K$-band version | HOLDS |
| S5 | L63-L67 | half-coupling kernel bound $\|P_{\exp(\beta A_e/2)}\|\le C_0$ | HOLDS |
| S6 | L69-L73 | (5) mass of a slow state on the exceptional set | HOLDS |
| S7 | L75 | proof of (4) ($\chi^2$ of radial Gaussians, mixture) | HOLDS |
| S8 | L77 | (4) for all functions of forest links | HOLDS |
| S9 | L81 | single-probe words have dense vacuum span | HOLDS (given row 1246 (4)) |
| S10 | L83-L92 | (6); $l_d$ strictly decreasing | HOLDS |
| S11 | L94 | algebra contains $L_e$, $C$, $M_v^2$, $V$ | HOLDS |
| S12 | L96-L102 | (7) plaquette multipliers by sign averaging | HOLDS |
| S13 | L104 | cyclicity of the transformed vacuum | HOLDS |
| S14 | L110 | noise threshold $\tau\ge1/(4\beta)$ for positivity | HOLDS |
| S15 | L112-L118 | (8); positivity at or above threshold | HOLDS |
| S16 | L120 | failure below threshold | HOLDS |
| S17 | L122 | rank one iff the complement is a forest; $2n^3+1$ pins minimum | HOLDS |
| S18 | L124-L129 | (9) pinned-density ratio $=(\mathrm{Tr}T^j)^2/\mathrm{Tr}T^{2j}$ | HOLDS |
| S19 | L135-L143 | (10) a fixed patch has vanishing overlap with the slow band | HOLDS (implication from rows 1151, 1231) |
| S20 | L145-L154 | gauge average and the variables $D$ | HOLDS |
| S21 | L156-L161 | (11) tail of $\|D\|$ under $\|f\|^2\nu$ | HOLDS |
| S22 | L163 | $\|{\bf1}_EU^2{\bf1}_E\|\le Ce^{-cu}$ | HOLDS |
| S23 | L165 | precompactness; clipping error | HOLDS |
| S24 | L167 | moments of readings converge to the Gaussian curl | HOLDS |
| S25 | L169 | tiling, good boxes, linearization | HOLDS |
| S26 | L171 | entropy comparison; extension to based loops | HOLDS (extension argued in two sentences; re-traced) |
| S27 | L173 | decorrelation in the Gaussian law | HOLDS |
| S28 | L175-L180 | conclusion of (10) | HOLDS |
| S29 | L188-L193 | (12) coupling change by a radial mark | HOLDS |
| S30 | L195-L200 | no $L^2$ mark for $\tau\ge1/(4\kappa)$ | HOLDS |
| S31 | L202-L206 | sign pattern, $k=2n^3+2n^2$, forest complement | HOLDS |
| S32 | L208-L217 | $\mathbb E[L^2\mid\text{spatial}]=1$; (13) | HOLDS |
| S33 | L219-L228 | (14) deletion amplitude $H=e^{-\beta k}z_\beta^r/I_\beta$ | HOLDS |
| S34 | L234-L245 | (15) first versus higher moments | HOLDS |
| S35 | L247 | first-moment bound | HOLDS |
| S36 | L249-L262 | (16) orbit-distance lower bound | HOLDS |
| S37 | L264-L272 | (17) localized history | HOLDS |
| S38 | L274 | Haar-preserving insertion | HOLDS |
| S39 | L276 | typical input boxes | HOLDS |
| S40 | L278-L292 | cost and payoff; lower bound of (15); neutral trace | HOLDS |
| S41 | L294 | lower rate $c(p-1)^3$ | HOLDS |
| S42 | L298-L303 | (18) curvature controls orbit distance | HOLDS |
| S43 | L305-L317 | random gauge construction | HOLDS |
| S44 | L319 | sum of path errors | HOLDS |
| S45 | L321-L325 | (19) collar estimate | HOLDS |
| S46 | L327 | $Q$ is the open-slab law | HOLDS |
| S47 | L329-L334 | (20) collar exponential moment | HOLDS |
| S48 | L336-L344 | (21) critical tilt | HOLDS |
| S49 | L346-L360 | (22) cubic onset of higher moments (positive claim 2) | HOLDS |
| S50 | L362-L366 | (23) better first derivative | HOLDS |
| S51 | L368-L374 | (24) relative truncation at the first moment (positive claim 3) | HOLDS |
| S52 | L376 | smaller cap, error $O(1/A_\beta)$ | HOLDS |
| S53 | L388 | $\|J(u)\|\le Cuv_3[\beta^{1/3}+\log(1+\beta)]$ | HOLDS |
| S54 | L390 | $K^u$ not positive for irrational or small $u$ | HOLDS |
| S55 | L392-L398 | (26) conjugate diagonal $\ge e^{-\beta m}$ | HOLDS |
| S56 | L400-L404 | $F$ entire, growth $e^{C\sqrt{1+\|c\|}}$ | HOLDS |
| S57 | L406 | $F$ nonconstant | HOLDS |
| S58 | L408 | $F$ has a zero off $[-1,1]$ | HOLDS |
| S59 | L410 | holomorphic Gram map | HOLDS |
| S60 | L412 | continuation; order $uk$ | HOLDS |
| S61 | L416-L423 | (27) signed interpolation | HOLDS |

Labelled OPEN and GUIDE text: L52 (the implication HOLDS; the Poincare bound is OPEN), L106, L131, L182, L230, L425 are
correctly labelled; the threshold cited at L425 matches A-B**. GUIDE L7, L17, L19-L23, L171 (Sussman-Alpoge
citations, setup) and L380-L386 ((25) endpoints) HOLD; L3-L5 and L186 not re-checked (not load-bearing).

**Defects.** None breaks a statement. Two notes, ranked:
1. L25 restates row 941 (A7) ($P_0=B^*B$, `gap-lsivac-max.md` L141-L149) without crediting row 941; row 947 is
   credited. Citation addition only.
2. L169-L171 extend row 1151 (24) from plaquette radii to four-component based loops in box frames in two sentences. I
   re-traced the extension (the density bound in row 1151's proof is on full tree-gauge coordinates, and the readings
   are invariant under the common root conjugation), and it holds. A written lemma would make (10) easier to reuse.

**Restatement question.** The main comparison (the thermal ratio as one-period against two-period deletion first
moments, (9), (14), (25), (27)) restates row 1151 (26) and (28), Theorem ZD-c and A-B**; row 1290 says so at L129,
L186 and L423. The deleted-tilt estimates (15), (21)-(24), the noise threshold with minimum pin count, (12) with its
converse, the positivity loss L390 and the total-gradient bound (3) are not in earlier rows (step 7b).

**What this check does not show.** It is one reading by one model, not an audit. No numeric run was made: no step
needed one, so memory was not sampled. The positive claims are lattice statements; none bounds the order-one quantity
$J(1)$ that A-B** needs, none gives the Poincare bound of L52, and the continuum construction and the mass gap stay
OPEN, as row 1290 itself states.

RESULT: Row 1297 (Claude Opus 5.5 max, Mac mini worker, cross-provider check of row 1290 gpt-6.2-astra, started 16:01Z, last step at 16:25Z): all 61 PROVED statements of `library/gap-solve33-astra62.md` HOLD (0 HOLDS AFTER CORRECTION, 0 FAILS), including the three positive claims: the total-gradient bound (3) L44-L50, the cubic onset (22) L346-L360 and the relative truncation (24) L368-L374, which are new in the lane by grep; one credit addition (row 941 (A7) at L25); the main comparison (thermal ratio via deletion first moments) restates row 1151 (26)/(28), Theorem ZD-c and A-B**, as row 1290 discloses; OPEN: the Poincare bound of L52, the order-one thermal bound $J(1)\le y_0V(s)/(2(96T_0)^3)$, the continuum construction and the mass gap.
