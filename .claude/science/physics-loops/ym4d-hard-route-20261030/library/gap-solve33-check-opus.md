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
