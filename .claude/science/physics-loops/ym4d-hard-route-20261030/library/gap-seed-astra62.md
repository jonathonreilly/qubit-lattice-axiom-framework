# Repo search

**GUIDE.** FINISH row 1367, pinned at `88a9f8f98`. The row-specific prior file is absent. The open registry has no entry under M-neutral, N-phys, neutral seed or mass gap. The prior search (§11) and the main-branch file `research/mass-gap/library/gap-flux-exercise-check.md` point to the soft-route Wilson-loop witness. [November 8 search](prior/repo-search-2026-11-08.md)

**GUIDE.** Searched Markdown and TeX on `origin/main` (`8b11ae2bb`), `pr/10114` (`f76f6c649`), `pr/10133` (`89faef229`), `pr/10134` (`1e70c7211`) and `pr/10141` (`c73ad7b17`). No hits for `(M-neutral)`, `(N-phys)`, neutral Wilson thermal sum/trace/excess, neutral rank-one or twist-averaged seed, or `s(2w)` near `4/21`. Method searches for plaquette frame bounds, spatial differences against a thermal trace, Hellinger increments or chain rules, conditional angular harmonics, staple Fourier moments and twist-averaged staple fluctuations gave no relevant hit. “Rank-one test” also hits unrelated odds tables and local-limit notes.

**GUIDE (closest hits by ref).** On main, `research/mass-gap/library/gap-phys-seed.md`, Theorem ZD-c, equates the periodic seed with a bounded doubling defect and unbounded scaled periodic gap on dyadic sides, given its inputs. On PRs 10114 and 10133, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, (11), gives the one-step centered plaquette correlation a volume-independent lower bound $v_N^2 e^{-68\beta}/(1+v_N/r_f(\beta)^4)$. The physical-time trace needs an upper bound on the sum over all neutral excitations. On Grok's PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md`, Theorem H, requires the open crossover clustering bound (CW), source transport (MG2) and scale matching (H6). On PR 10134, `library/mass-gap-interface.md`, I1–I3, shows that a gap with a nonempty excited sector implies a nonzero Hamiltonian there. The converse fails. On PR 10141, `research/ym4d/library/fp1.md`, lines 297–301, bounds the single-scale classical Landau lift by $\|HB\|_{H^1}\le C\|B\|$. These latter two statements contain no neutral heat-trace estimate.

## The two volume quantifiers

**OPEN (Wilson seed).** On the prescribed trajectory, fix an admissible physical side $L$, put $n_j=L/a_j$, and take $4\mid n_j$, $n_j\ge2^{70}$ at all late cutoffs. Assume $\beta_0\le\beta_j\le B_0\log n_j$. For the zero spatial twist, $P_0$ averages the eight electric centre translations. In its range, let $\lambda_0>\lambda_1\ge\cdots\ge0$ be the Wilson transfer eigenvalues, counted with multiplicity. Write $s_{n,\beta}(t)=\sum_{a\ge1}(\lambda_a/\lambda_0)^t$. The question is whether **some** such $L$ gives $s_{n_j,\beta_j}(2w_j)\le4/21$ at every late cutoff. Monotonicity allows $w_j=\lfloor n_j/1024\rfloor$, the largest permitted integer. Its physical duration $a_jw_j$ tends to $L/1024$. [Row 1356, §2](gap-mini-mneutral-fable.md)

**PROVED (prior implications).** Claude Fable's row 1356 applies the rank-one theorem of Eckart and Young with a free scale. The optimal squared Hilbert–Schmidt error is $s(2w)/(1+s(2w))$, so tolerance $2/5$ gives $4/21$. In the reverse direction from (N-phys), the same-box time cap can increase fourfold. Wilson shape propagation repairs this for existence on some fixed side. In either flux alternative, the resulting seed suffices for the gap clause **given** a matched reflection-positive continuum datum satisfying (P1)–(P4), (H2), and totality (TOT) in the intended Hilbert space. [M1/M2 check, row 1359](gap-mini-mneutral-check-astra.md) · [Time caps, row 1355](gap-mini-neutral-step-check-astra.md) · [Continuum hypotheses, row 1349](gap-seed-audit-check-astra.md)

**GUIDE.** The prior eigenvalue count disposes of simultaneous uniformity in all volumes at one fixed time. On one cube, (2) tests a disproof with a two-point function. Equations (4)–(7) isolate the low angular moments that could prove the seed. Equations (9)–(10) test a direct Wilson estimate for them. The row requests the laptop Codex runner with gpt-6.2-astra at max effort. New PROVED labels cover the following hand arguments, with no independent check or formal computation. This note grants no status.

**GUIDE (published sources).** The outline index and obligations lead to Sussman and Alpoge, with Claude and Codex, at `31a47c543775`. Their outline, lines 588–599, 3712–3720 and 31871–31882, says “the filter weight vanishes linearly near zero energy.” Its example $E e^{-E}\,dE$ has polynomial decay and support down to zero. CA-I 2699–2713 leaves a mass gap outside Theorem 0. The cited Bałaban results concern regular backgrounds and constrained propagators. [Outline index](sa-index/README.md) · [Obligations](sa-index/obligations.md) · [Bałaban source record](lit-balaban.md)

## What the existing Wilson count rules out

**PROVED (prior result and consequence).** Row 1161, [equation (19)](gap-solve9-astra62.md), checked in [row 1162, S25–S26](gap-solve9-check-opus.md), is stronger than the absolute lower bound sought in the first attack. For every sufficiently large admissible $n$ and every $\beta\ge1$, at least $c n^3$ excited, centre-neutral Wilson eigenvalues have $-\log(\lambda_i/\lambda_0)\le C$, with absolute $c,C>0$. It follows directly that

$$
                s_{n,\beta}(2w)\ge c n^3 e^{-2Cw}.                    \tag{1}
$$

For any late cutoff of the asymptotically free trajectory with $\beta_j\ge1$, take the finite lattice time corresponding to a proposed physical time $W>0$. Any admissible dyadic enlargement with $n^3>[4/(21c)]e^{2Cw}$ fails the test. The coupling upper bound continues to hold under enlargement at fixed cutoff. This disposes of simultaneous uniformity in all volumes with a common cutoff floor. It makes no assertion for an order of limits with a cutoff floor depending on the volume. On one fixed physical cube at the maximal test time $w_j=\lfloor n_j/1024\rfloor$, the lower bound tends to zero. The remaining question is that one-cube estimate. The underlying level count belongs to row 1161.

## Testing a physical-scale lower bound

**GUIDE.** An absolute microscopic count loses its force when $w_j$ grows linearly with $n_j$. Instead keep a measurable normalized correlation at the *test time* as the input. The Wilson transfer used below is the one of Osterwalder–Seiler and Lüscher in [row 667, §§1–4, 9.3](gap-transfer.md). The electric coefficients and trace representation are in the Sussman–Alpoge outline 2197–2231 and 2315–2335, indexed in chunk 02. Put $R=T/\lambda_0$.

**PROVED (spatial translates).** Let $W_i=\tfrac12\operatorname{tr}U_{p_i}$ for elementary $23$-plaquettes with the same transverse coordinates, at time zero and $x_1=i$ mod $n$. Put $D_i=W_i-W_{i+1}$, let $\Omega$ be the normalized positive vacuum, and set $v_i=D_i\Omega$. The eight sheet flips fix contractible plaquettes and fix $\Omega$ by uniqueness. Translation invariance gives $v_i\perp\Omega$. Write $g=\|v_0\|^2$. Then $0<g\le4$, since $\Omega>0$, the two loops differ on a Haar-open set, and $|D_i|\le2$.

On the ordinary periodic $n^3\times m$ torus, take direction 1 as transfer direction. The plaquette lies in one slice of that transfer. Write $S$ for the transfer and $W$ for multiplication by the plaquette trace there. For $0\le d\le n$,

$$
 C_m(d)=\mathbb E_m[W_0W_d]
   =\frac{\operatorname{Tr}(S^{n-d}WS^dW)}{\operatorname{Tr} S^n}.
$$

This follows by integrating the links between slices, with the spatial Wilson factors split into their two half-weights. The three transverse periods can differ. In a spectral basis of $S$ the numerator is the sum of $\alpha^{n-d}\gamma^d|W_{\alpha\gamma}|^2$, with multiplicities included. $\alpha,\gamma\ge0$. At $1\le d\le n-1$, the centered second difference of each weight is $\alpha^{n-d-1}\gamma^{d-1}(\alpha-\gamma)^2\ge0$, with a zeroth power equal to one. Finite spectral cutoffs followed by convergence of the three traces justify subtraction. In the original time direction $m\to\infty$ at fixed $n,\beta$ gives $C(d)=\langle\Omega,W_0W_d\Omega\rangle$, by the simple vacuum and trace class. Convexity at those $d$ passes to the limit.

Thus the Gram matrix $G_{ij}=\langle v_i,v_j\rangle$ has diagonal $g$ and off-diagonal entries $2C(d)-C(d-1)-C(d+1)\le0$. Each row sums to zero since $\sum_i v_i=0$. Its absolute row sum is $2g$. The synthesis map $e_i\mapsto v_i$ therefore gives

$$
        \sum_i |v_i\rangle\langle v_i|\ \le\ 2g\,P_{\rm exc},
$$

where $P_{\rm exc}=P_0-|\Omega\rangle\langle\Omega|$ on the physical Hilbert space. This argument allows correlations between every pair of translates. With $R=T/\lambda_0$, tracing against $R^t$ gives the more informative inequality

$$
          s_{n,\beta}(t)\ \ge\ \frac n2\,
              \frac{\langle v_0,R^t v_0\rangle}{g}.                     \tag{2}
$$

**PROVED (test on a fixed physical cube).** A seed there requires the ratio in (2) to be at most $8/(21n)$ at the test time. One may also use every $b$-th plane, $b\mid n$, and a real bounded gauge- and centre-invariant function $F$ of links lying in one plane. Use $S^b$ in the spatial proof and take the difference between consecutive chosen planes. If it has positive variance, the right hand side of (2) then has factor $n/(2b)$. With $k=n/b\ge3$, a ratio greater than $8/(21k)$ at $t=2\lfloor n/1024\rfloor$ rules out that cube at that cutoff, by time monotonicity. This permits plane observables and interplane separations of physical size. Row 1204 uses spatial differences in a continuum operator norm. Equation (2) concerns a finite-box trace and the measured correlation of a specified plane observable.

**OPEN.** The quoted short-distance law does not give such a lower ratio at the maximal time on every proposed side. Row 1161 controls microscopic energies of order one in lattice units. Substitution into (1) loses the bound at times proportional to $n$. A failing cube at a single cutoff would also leave the existential side and late-cutoff quantifiers to address.

## An upper test using one boundary link at a time

**PROVED (prior projected law).** Use the square of the centre-projected kernel from rows 1155 and 1169. The latter already uses its affinity after erasing separated raw links. [Row 1155, following (34)](gap-solve7-astra62.md) · [Row 1169, (15) and kernels](gap-solve13-astra62.md)

Set $w=\lfloor n/1024\rfloor$ at an admissible cube. Use normalized product Haar measure on each entire boundary slice. Let

$$
 B=\frac{P_0T^w}{\|P_0T^w\|_{\rm HS}},\qquad
 J(x,y)=B(x,y)^2,\qquad l(x)=\int J(x,y)\,dy,\qquad Q(x,y)=l(x)l(y).
$$

Here $B$ denotes both the operator and its kernel. It is positive semidefinite, symmetric, and pointwise positive by the Wilson integral and positive centre averaging. $J$ is a probability density. One can realize it with two Wilson slabs with a centre flip averaged **independently on each slab** before gluing. The Wilson weight updates the two summation variables after conditioning on the endpoints. This represents the neutral trace in either flux alternative.

**PROVED (affinity bounds).** Let $\sigma=\|B\|_{\rm op}=(1+s(2w))^{-1/2}$, $A=\int\sqrt{JQ}$, and $D=1-A$. Apply the square-root marginal trial vector from row 1165 to the projected law. [Row 1165, (19)](gap-solve11-astra62.md)

$$
                \sigma^3\ \le\ A=\langle\sqrt l,B\sqrt l\rangle
                            \ \le\ \sigma.                               \tag{3}
$$

For the lower bound, $B\Omega=\sigma\Omega$. Cauchy–Schwarz in the row $B(x,\cdot)$ gives $\sigma\Omega(x)\le\sqrt{l(x)}$. Since $B\ge\sigma|\Omega\rangle\langle\Omega|$ as a quadratic form, this gives $A\ge\sigma\langle\sqrt l,\Omega\rangle^2\ge\sigma^3$. In particular $D\le 1-\sqrt{21}/5$ suffices on the same cube and at the same time. A passing cube must have $D\le1-(\sqrt{21}/5)^3$.

**PROVED (exact sum of losses).** Order the $3n^3$ links of $y$, revealing $x$ first. For a history $z=(x,y_{<i})$ write $J_{<i}, Q_{<i}$ for its densities. Let $p_i(\cdot\mid z)$ and $q_i(\cdot\mid z)$ be the next-link conditional densities for $J,Q$, respectively. Set $d\gamma_i(z)=\sqrt{J_{<i}(z)Q_{<i}(z)}\,dz$. In particular $\int d\gamma_i\le1$. Then

$$
 D=\frac12\sum_i\int d\gamma_i(z)
           \int_{SU(2)}\big(\sqrt{p_i(v\mid z)}-\sqrt{q_i(v\mid z)}\big)^2\,dv. \tag{4}
$$

The affinity of the two histories before revealing $y_i$ decreases by the indicated summand after that link is revealed. This follows by factoring both extended history densities into the history times its conditional density. The initial $x$ marginal is common and the final affinity is $A$. A previous Wilson comparison gives mutual information of order $(n/k)^3$ for the ordinary torus under its short-time hypotheses, including $k\le\beta^\delta$, $0<\delta<1/48$. Its physical duration vanishes. Here the summands refer to successive edges on the two faces at fixed physical separation. [Row 1283, (29)–(32)](gap-solve32-astra62.md) · [Check, row 1289](gap-solve32-check-opus.md)

Reveal a spanning tree of the spatial graph first. Conditional on $x$, the $y$-law is invariant under all vertex gauges at its own boundary. Gauge transformations act transitively on tree configurations by solving for vertex frames outwards from a root. Pushing independent Haar vertex frames through this action gives product Haar on the tree, by successively integrating a leaf frame. Thus the first $n^3-1$ terms in (4) vanish exactly, even with the entire opposite face revealed. The other $2n^3+1$ terms can carry gauge-invariant loop information. In particular the conditional laws after the tree still depend on the earlier links.

**PROVED (removing the high angular modes in (4)).** Identify a link with a unit quaternion $v\in S^3$. In either ensemble, conditional on the other links and the seam signs in a contributing Wilson torus, its density is

$$
             g_h(v)=\exp(h\cdot v)/Z(h),\qquad |h|\le6\beta,\qquad
             Z(h)=\int\exp(h\cdot v)\,dv\ge1 .
$$

A spatial boundary link belongs to four spatial plaquettes and two temporal plaquettes. Gluing adds the two half-weights of the spatial action. Each signed fundamental plaquette contributes a linear form of norm $\beta$ in this link. The other links are held fixed. For $Q$, take two independent draws of a one-face marginal using two independent projected tori. Thus, even conditional on any preceding history, both $p_i$ and $q_i$ are mixtures of the displayed $g_h$, by disintegration. This is the one-link Wilson conditional specification. See the Sussman–Alpoge outline, lines 240–260, 427–434 and 2475–2498 (GL14), and the separated-link version in row 1169. [Index, chunk 01](sa-index/chunk-01.md) · [Index, chunk 02](sa-index/chunk-02.md) · [Local conditional laws](gap-solve13-astra62.md)

Let $\Pi_d$ be the Haar orthogonal projection on the restrictions to $S^3$ of real polynomials of degree at most $d$ in the four link coordinates. Choose $d$ with

$$
 d+1\ \ge\ \max\left\{24 e\beta,\ (6\beta+5\log n)/\log 2\right\}.
$$

For each conditional density $p$ just described, uniformly in its history,

$$
                  \|p-\Pi_dp\|_{L^2(dv)}\le n^{-5}.                     \tag{5}
$$

Indeed, for $s=|h|$, approximate $g_h$ by

$$
       Z(h)^{-1}e^{-s}\sum_{k=0}^{d}(s+h\cdot v)^k/k! .
$$

The pointwise relative remainder is a Poisson tail of mean $u=s+h\cdot v\in[0,12\beta]$. It is zero at $u=0$. Otherwise exponential Markov with parameter $\log((d+1)/u)$ bounds it by $(eu/(d+1))^{d+1}\le2^{-(d+1)}$. Since $g_h\le e^{6\beta}$, the absolute error is at most $n^{-5}$. Mixing the polynomials gives the same uniform bound for the conditional mixture. Best approximation on Haar probability space gives (5). This adapts the positive Taylor estimate of [row 1163, (11)–(12)](gap-solve10-astra62.md), which compresses the whole transfer to a joint polynomial space of exponential dimension.

Write $p^{[d]}=(\Pi_dp)_+$ for the positive part, without renormalizing it. Its coefficients *before clipping* are the conditional expectations of the Haar basis harmonics through degree $d$ on this **one next link**. Since $p\ge0$ and $(\sqrt x-\sqrt y)^2\le|x-y|$,

$$
        \|\sqrt{p^{[d]}}-\sqrt p\|_2^2
              \le\|p^{[d]}-p\|_1\le\|\Pi_dp-p\|_2\le n^{-5}.
$$

Define $D_d$ by (4) with the two conditional densities so clipped and the same exact history measures $\gamma_i$. The tree terms still vanish. Apply the triangle inequality to the direct sum of the remaining $L^2(d\gamma_i\,dv)$ spaces. Since $\int d\gamma_i\le1$,

$$
          |\sqrt{2D_d}-\sqrt{2D}|
                        \ \le\ 2\sqrt{2n^3+1}\ n^{-5/2}.                 \tag{6}
$$

At $\beta\le B_0\log n$, the least allowed degree is $O_{B_0}(\log n)$. There are $\sum_{k=0}^d(k+1)^2$ real basis elements. The homogeneous harmonic polynomials of degree $k$ in four variables have dimension $\binom{k+3}{3}-\binom{k+1}{3}=(k+1)^2$, by splitting off the radius squared times degree $k-2$. Thus the number of moments *at a specified history and link* grows only as $O_{B_0}((\log n)^3)$. The conditioning histories themselves range over whole faces.

**PROVED (physical-side equivalence, using the cited Wilson propagation).** Put $\tau=\sqrt{21}/5$. For a direct sufficient test, it suffices to find one admissible $L$ with

$$
                     \limsup_{j\to\infty}D_{d_j}<1-\tau.                \tag{7}
$$

Choose $w_j=\lfloor n_j/1024\rfloor$. By (6) and the strict margin, $D\le1-\tau$ eventually, so (3) gives $s(2w_j)\le4/21$. Conversely, suppose the one-cube seed holds at any admissible side. Rows 1355 and 1161 (lines 150 and 215, with the Pfaffian propagation in the check) give arbitrarily small cutoff upper limits of the neutral trace excess at any prescribed fixed inverse aspect on a sufficiently large fixed dyadic enlargement. Apply that statement with inverse aspect $2048$. Monotonicity gives the same upper bound at $2\lfloor n/1024\rfloor$. Then $\sigma^3=(1+s(2w))^{-3/2}$ is arbitrarily close to one. Equations (3) and (6) give (7) on an enlarged side. The converse uses the Wilson shape results and may change the physical side. [Row 1355, factor-four correction and enlargement](gap-mini-neutral-step-check-astra.md)

**OPEN.** The sum in (7) still requires a bound on the actual conditional angular moments given the other face and the previously revealed links. Equation (6) pays for the entire high-degree tail and for every tree link at the stated coupling. A bound on the number of low degrees gives no bound on their coefficients.

## Testing whether fewer angular moments suffice

**PROVED (comparison at the physical time).** Fix any slope $b>0$. Take $\beta=b\log n$ and $w=\lfloor n/1024\rfloor$ on growing admissible cubes. There are positive semidefinite transfers on these slice variables, with strictly positive kernels, spatial cubic symmetry, gauge and electric-centre invariance, and the single-link mixture bound $|h|\le6\beta$, for which

$$
    s_{\rm cmp}(2w)\longrightarrow1,\qquad D_{d_n}=0,\qquad
           d_n=\left\lfloor\tfrac12\sqrt b\,\log n\right\rfloor .        \tag{8}
$$

The zero holds exactly in every reveal order. Thus even $o(\log n)$ degrees cannot suffice from those properties alone. Row 1161 already hides a slow neutral state from finitely many tests at a prescribed time. Here the hidden state survives a time proportional to $n$ while satisfying the single-link mixture bound and *all the conditional tests* through a growing degree. The example changes the Wilson action.

**PROVED (the hidden angular mode).** Put $s_0=3\beta$. Let $C_{s_0}$ be normalized Wilson convolution on one copy of $SU(2)$, with kernel proportional to $e^{s_0 z\cdot v}$. Its multiplier on degree $j$ is $r_j=I_{j+1}(s_0)/I_1(s_0)$. Indeed the central Fourier coefficient is proportional to $(I_j-I_{j+2})/(j+1)=2I_{j+1}/s_0$, by the Haar angle formula. Dividing by the constant coefficient gives $r_j$. Choose the least even $k>d_n+2$. Write $\theta$ for the conjugacy angle and put

$$
 f=\epsilon\cos(k\theta),\quad \epsilon=\frac{r_k}{2(k+1)},\quad
 v_f=\int f^2=\epsilon^2/2,\quad a_\pm=(1\pm f)/\sqrt{1+v_f}.
$$

For $\chi_j=\sin((j+1)\theta)/\sin\theta$, the character of dimension $j+1$, one has $2\cos(k\theta)=\chi_k-\chi_{k-2}$. The character $\chi_j$ is a degree-$j$ spherical harmonic on $S^3$, as follows from the radial Laplacian $\partial_\theta^2+2\cot\theta\,\partial_\theta$. Hence $f$ has zero mean. Both $f$ and $f^2-v_f=(\epsilon^2/2)\cos(2k\theta)$ are orthogonal to all polynomials of degree at most $d_n$. They are invariant under the central sign. The functions $1\pm f$ are normalized positive mixtures of kernels of parameter length $s_0$. Indeed their mixing densities are $1\pm C_{s_0}^{-1}f$, where the inverse acts only on the two indicated character spaces. Since $|\chi_j|\le j+1$ and $r_{k-2}\ge r_k$, $\|C_{s_0}^{-1}f\|_\infty\le1/2$.

The recurrence $I_j/I_{j+1}=2(j+1)/s_0+I_{j+2}/I_{j+1}\le1+2(j+1)/s_0$ gives $r_k\ge e^{-k(k+3)/s_0}$ by multiplying for $j=1,\ldots,k$. For monotonicity, $I_{j+2}/I_{j+1}$ is the mean of $t$ under density proportional to $e^{s_0t}(1-t^2)^{j+1/2}$ on $[-1,1]$, by the Bessel integral and integration by parts (row 1359, check of JF). This mean lies between zero and one. Since $2k(k+3)/s_0=(1/6+o(1))\log n$,

$$
                     v_f\ge n^{-1/3}/[8(k+1)^2]
$$

eventually. These are hand bounds on the exact functions.

**PROVED (the transfer).** Use all $M=3n^2$ straight spatial winding loops, one per transverse location in each direction, counting no loop twice. They meet at vertices and have disjoint *links*. Under product Haar their holonomies are independent and Haar. Set

$$
 \Phi_\pm(X)=\prod_\ell a_\pm(U_\ell(X)),\qquad
 T_{\rm cmp}=|\Phi_+\rangle\langle\Phi_+|+|\Phi_-\rangle\langle\Phi_-|.
$$

Conjugation, orientation reversal, and centre changes leave each factor invariant. A translation or cubic rotation permutes loops up to these operations. Each vector has norm one. Their overlap $h=[(1-v_f)/(1+v_f)]^M\le e^{-2Mv_f}$ decays faster than any inverse power of $n$. The nonzero eigenvalues are $1+h,1-h$ on their sum and difference. Thus the entire excited neutral trace is $[(1-h)/(1+h)]^{2w}\to1$.

Every positive integer power of $T_{\rm cmp}$ has a kernel that is a nonnegative linear combination of $\Phi_i(x)\Phi_j(y)$, by multiplication through their two-by-two Gram matrix. Its squared kernel, conditional on $x$, is therefore a mixture of three product laws over the loops of $y$. Their single-holonomy densities are $a_+^2,\ a_-^2,\ (1-f^2)/(1-v_f)$. Marginalizing $x$ gives the same three components with new weights. In each component, a link is exactly Haar if some other link of its loop is still unrevealed. Integrating that other link integrates the entire loop density to one. At the last link the conditional density is the indicated loop density composed with $v\mapsto A v^{\pm1} B'$, a Haar isometry preserving harmonic degree. Previously completed loops only change mixture weights. Each of the three loop densities involves the constant, $f$, and $f^2-v_f$, so its projection through $d_n$ is exactly one. It follows that $\Pi_{d_n}p_i=\Pi_{d_n}q_i=1$ for all histories and edges, proving the second assertion of (8).

Each of the three densities is proportional to a product $a_i a_j$. Multiplying two positive mixtures of $e^{s_0 z\cdot v}$ adds their parameters, of total length at most $2s_0=6\beta$. The Haar isometries preserve the length. Normalizing and partially conditioning preserve this mixture property. The construction has interactions on entire winding loops and a common choice across loops. It tests the attempted inference from one-link regularity at logarithmic coupling. It supplies no counterexample in the local Wilson action.

## Estimating the remaining dependence in the Wilson law

**PROVED (a bound using the six staples).** In the positive Wilson ensemble for $J$, let $H_i$ be the signed sum of the six staples including their factor $\beta$, oriented as in $g_h$. For $v=Y_i$ define $H_i^\top=H_i-(H_i\cdot v)v$. Put

$$
 \Delta_i=\mathbb E_J[H_i^\top\mid X,Y_{\le i}]
                    -\mathbb E_J[H_i^\top\mid Y_{\le i}].
$$

This compares two predictions of the same local force. The first knows the field on the opposite time face. The marginal of $Y$ in $Q$ equals that in $J$. Differentiation of the positive mixtures before revealing $Y_i$ therefore gives
$\nabla_v\log(p_i/q_i)=\Delta_i$ at the sampled link. Indeed the tangent derivative of $g_h$ is $g_h\,h^\top$, and Bayes' rule updates the mixing weights on observing $v$. The bound $|h|\le6\beta$ justifies differentiation under each integral.

For a fixed history write $p=p_i,q=q_i,\ \mathcal A=\int\sqrt{pq}$. A mixture $q$ has $\sup q/\inf q\le e^{12\beta}$ since this pointwise ratio bound holds for each $g_h$. Also $p\le e^{6\beta}$ and $q\ge e^{-12\beta}$. The Poincaré inequality on the unit $S^3$ has Haar constant $1/3$, by the first nonzero spherical harmonic eigenvalue $3$. Comparing the variance about the Haar mean with the $q$-energy gives

$$
  1-\mathcal A^2=\operatorname{Var}_q\sqrt{p/q}
        \le \frac{e^{12\beta}}{12}\int p\,|\nabla\log(p/q)|^2 .
$$

For $r\le K=e^{18\beta}$ one has $r\log r-r+1\le(2+\log K)(\sqrt r-1)^2$. As a function of $u=\sqrt r$, the left side has value and derivative zero at one and second derivative $4+4\log u\le4+2\log K$. Apply this with $r=p/q$. Use $\int(\sqrt p-\sqrt q)^2=2(1-\mathcal A)\le2(1-\mathcal A^2)$. Factoring the joint densities into their conditionals and summing their logarithms then gives

$$
 \log(1+s(2w))\ \le\ D_{\rm KL}(J\|Q)
 \le\frac{(2+18\beta)e^{12\beta}}{6}
                     \sum_{i\ {\rm after\ the\ tree}}\mathbb E_J|\Delta_i|^2 . \tag{9}
$$

For the first inequality, $\log(1+s)=-2\log\sigma\le-2\log A\le D_{\rm KL}(J\|Q)$ by (3) and Jensen under $J$. The tree scores vanish. This use of the Shannon bound follows row 1165, equation (3), on the projected law.

**PROVED (what the direct Wilson integration gives).** Orthogonal projection in $L^2(J)$ gives $\mathbb E|\Delta_i|^2\le\mathbb E|H_i^\top|^2$. At fixed staple $h$, integrate the divergence of $g_h\nabla(h\cdot v)$ on the unit sphere. Since $\Delta_{S^3}(h\cdot v)=-3h\cdot v$, this gives

$$
              \mathbb E|H_i^\top|^2=3\,\mathbb E[H_i\cdot Y_i]\le18\beta .
$$

Row 1161 uses this integration by parts for local angular fluctuations. Replacing each conditional difference in (9) by the whole local fluctuation bounds the sum by $18\beta(2n^3+1)$.

**PROVED (size of that loss in the Wilson law).** At large bare coupling the local fluctuation itself satisfies, uniformly in the admissible box and for each spatial link,

$$
   18\beta-C(1+\log\beta)
      \ \le\ \mathbb E_J|H_i^\top|^2\ \le\ 18\beta.                     \tag{10}
$$

Here the expectation includes the slab interiors and seam signs. The sum in (9) retains the difference between two conditional predictions. Equation (10) measures the cost of dropping it.

To prove (10), glue the two slabs and write $V=2wn^3$ for the number of sites. Denote by $\eta_p$ the centre sign on a temporal twist sheet, and take $\eta_p=1$ elsewhere. Put $\mathcal E=\sum_p(1-\eta_p W_p)$, with $W_p=\tfrac12\operatorname{tr}U_p$. Normalize $Z(\beta)=\int e^{-\beta\mathcal E}$ over product Haar and both uniform seam choices, so $Z(0)=1$. Its normalized boundary marginal is $J$. Keep the two identity seam choices, of prior probability $1/64$. Restrict each of the $4V$ links to geodesic distance $\beta^{-1/2}$ from identity for $\beta\ge1$. Each ball has Haar measure at least $c\beta^{-3/2}$, by the radial density proportional to $\sin^2\theta$. Each of the $6V$ plaquettes then has deficit at most $8/\beta$, by the triangle inequality and $1-\cos x\le x^2/2$. Thus

$$
   -\log Z(\beta)\le \log64+48V+4V\log(\beta^{3/2}/c).
$$

Concavity of $-\log Z$ gives $\beta\mathbb E_J\mathcal E\le-\log Z(\beta)$. This is the Haar-ball estimate from GC2 and row 1283 applied to the projected rectangular torus. [GC2](gap-crux-exercise-astra.md) · [Cubic action estimate](gap-solve32-astra62.md) · [Check of the action cutoff](gap-solve32-check-opus.md)

Let $e_i=\sum_{p\ni i}(1-\eta_pW_p)$. All $3V$ spatial edges have the same $\mathbb E_J e_i$. To see this for the signed action, translating a twist sheet preserves its mod-two homology class. The difference of the two sheets is a boundary of dual three-cells. Multiplying the primal link dual to each such cell by $-1$ changes the plaquette signs on its boundary and preserves Haar. This moves seam representatives while preserving every signed plaquette observable. Spatial cubic rotations permute the uniformly summed twist labels. Each plaquette meets at most four of the spatial edges. Therefore $3V\mathbb E_J e_i\le4\mathbb E_J\mathcal E$. Finally $H_i\cdot Y_i=\beta(6-e_i)$. The integration-by-parts identity gives (10). Along $\beta_j\to\infty$ the sum of the $2n_j^3+1$ whole-link fluctuations is asymptotic to $18\beta_j(2n_j^3+1)$. No improvement of their individual upper bounds could make this substitution sufficient.

**OPEN (first missing estimate in this argument).** A sufficient improvement of (9) would bound that sum by $6e^{-12\beta}\log(25/21)/(2+18\beta)$ at the maximal seed time on one eligible cube for every late cutoff. The less restrictive target of this approach is (7) itself. In (8), a common label survives the full test time despite one-link smoothness and cubic symmetry. Its winding-loop interactions differ from the local Wilson action. The unknown is the influence of $X$ on the low angular moments after the revealed Wilson links are fixed. Neither the marginal plaquette law nor the single-link integration by parts estimates that influence.

RESULT — OPEN. Row 1367. The existing Wilson count excludes one fixed time simultaneously on all spatial volumes at a fixed late cutoff. On the one admissible cube required by (M-neutral), (5)–(7) control the contribution of high angular modes. The remaining estimate is the summed influence of the opposite face on the low conditional moments. Equation (10) shows why a sum of unconditioned local force fluctuations cannot supply it. The Wilson seed and the matched mass-gap conclusion remain open. No step of the cited implication chain was disproved.
