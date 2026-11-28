# Repo search

OpenAI Codex, FINISH row 1513 (assigned gpt-6.2-astra, max), checking Claude Fable's row 1510 at `824b9e1cf9b44eaf899db7698406d82311afe470`. Research text only. This check grants no status. [Row 1510, the text checked](gap-seed-solve-fable.md)

Searched Markdown and TeX on `origin/main` (8b11ae2bb), `pr/10114` (f76f6c649), `pr/10133` (89faef229), `pr/10134` (1e70c7211) and `pr/10141` (c73ad7b17). The initial label search hit unrelated background-vertex Theorems NB-4/5 in `ym4d-proof/NBG_A.md`. The method search included `384 contours`, `sixteen (twisted )?masses`, `weighted Poincar`, `Efron.{0,2}Stein`, `posterior score`, Poincaré near `block kernel` or `image measure`, `TILT-COV-sup` and `(LOC-COV)`. It returned 32 lines across the five refs. The distinctive contour, mass and tilt labels gave no hits.

- On all five refs, `docs/GAUGE_WILSON_COMPACT_CUBE_ALL_COUPLING_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md` lines 102–123 and its archived PR 8022 derivation give $\mathrm{gap}(H_{\rm phys})\ge(16/a)(\min\phi/\max\phi)^2$ via $\phi^2dU$ on one cube. This is a ground-state density comparison. On PRs 10114/10133, `ym4d-existence/EXISTENCE.md` lines 2297–2301, its session snapshots and `LOG.md` leave a depth-uniform Efron–Stein influence bound for polar averages open.
- On the same two PRs, `ym4d-proof/MANUSCRIPT_RG.md` lines 1251–1259 use a finite Neumann Poincaré constant on a compact rectangle. Lines 1962–1980 express the derivative of a cap expectation as covariance with its own posterior score and bound it for the insertions $F_S$ in (CC13). On main, `parts/nonlinear-chart-response.md` in the SU(2) gauge-aligned response lane, lines 49–66, has the same derivative on its restricted two-step chart. The main two-region note, `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md` lines 504–529, proves exponential boundary response (34) under the small-coupling criterion (33). These supply precedents for the identity in REV and for restricted response estimates.
- In this lane, row 1460's LD-1/LD-2 gives the posterior score variance in the Hessian and an **upper** stiffness bound. Row 1468 defines Q2 and preserves each mass. Row 1497(i) proves the suffix implication used below. Row 1512 found no order-one Wilson supplier for (H2) in its literature search. The target-specific prior file was absent. The November 8 digest treats other targets, and the registry search found no other owner of this check. [LD-1/LD-2](gap-crux-direction-fable.md) · [Row 1512](prior/gap-inlaw-two-scale-lit-luna.md) · [November 8 digest](prior/repo-search-2026-11-08.md)

The index (chunks 01, 07, 09, obligations and CA entries) led to Sussman and Alpoge's sources with Claude and Codex at `31a47c543775`. Outline 396–416 distinguishes mass preservation from transport of observables. Lines 7943–7987 define odd-side, ordered paths and a logarithmic block map. CA-I 105513–105534 gives a Gaussian conditional precision. CA-II 74322–74350 treats a regular small-field insertion. CA-III 97224–97244 identifies Bałaban's propagator on a constant abelian background as a conditional covariance. None supplies (FL) on the compact Wilson posterior.

## Verdict

**HOLDS AFTER CORRECTION.** (F4), PC, NF, NB as stated in lines 158–165, and the conditional REV inequality hold. The first wrong literal wording is **line 156**, “weak steps erase the shape.” The first false numerical inference is **line 176**, and the first wrong inference about the open selectivity question is **line 179**. The comparison with the named bridge criterion at line 240 also needs correction.

## (i) The 384 contours — HOLDS

Use the corner-based Q2 in row 1468, lines 128–145. An offset $\xi\in\{0,1\}^4$ and an axis order $\pi\in S_4$ label each contour, including repetitions. Take the outgoing steps with $\xi_i=1$ in order $\pi$, two straight steps along the bond, then the translated outgoing leg in reverse. Count a reversed traversal on its underlying positive link. Keep backtracking traversals.

Here is an exhaustive enumeration by the **rank of the traversed axis**. Fix an outgoing link of direction $j$. Its start has even $j$-coordinate. Let $E$ be its set of odd coordinates on the other axes, $k=|E|$. If $s$ axes precede $j$ in $\pi$, their set must contain $E$. Their offset bits are forced to be the indicator of $E$, and $\xi_j=1$. The $3-s$ later bits are free. Thus each table entry is $\binom{3-k}{s-k}s!(3-s)!2^{3-s}$ for $s\ge k$, and zero otherwise. This counts each labelled pair using that link once.

| $k$ | $s=0$ | $s=1$ | $s=2$ | $s=3$ | Pairs for this link |
|---:|---:|---:|---:|---:|---:|
| 0 | 48 | 24 | 12 | 6 | 90 |
| 1 | 0 | 8 | 8 | 6 | 22 |
| 2 | 0 | 0 | 4 | 6 | 10 |
| 3 | 0 | 0 | 0 | 6 | 6 |

Write $N_k$ for the last column. The incoming leg gives the same table. Four coarse bonds start and four end at the associated corner. Each of the two straight-step positions determines a unique offset and coarse base modulo the period, for all 24 permutations. Thus every fine link receives 48 straight traversals. For even $x_j$ the row total is $48+8N_k$ and for odd $x_j$ it is 48. Its maximum is $768/384=2$ after normalization. Translations by two preserve these counts on every admitted torus. Twisted identifications multiply link matrices by central signs, which preserve tangent norms.

For $|\xi|=h$, the length is $2+2h$, with multiplicity $24\binom4h$. At lengths $2,4,6,8,10$ the multiplicities are $24,96,144,96,24$. This gives $2304/384=6$ for each column sum. The product rule, unit left/right multiplication and inversion on $S^3$ bound $\|D_\ell M_c\|$ by the number of traversals divided by 384, including repeated visits.

A separate integer walk traversed every path for each of the four prototype bonds. It recorded the lower endpoint of every positive or reversed step modulo two. The 64 rows had traversal counts $48,96,128,224,768$ with multiplicities $32,4,12,12,4$. Their sum was $9216=4\cdot2304$, or 24 after division by 384. Recording reversed traversals at departure instead preserved lengths but failed the leg comparison. The rank table and length count give the written proof. The Python cross-check and logs are in `/tmp/ym4d-row1513.joEbkpLD/` (`contours.py`, `contours.log`, `control.log`, `repo-methods.log`). Lean was unavailable. The walk completed under the shared numerical lock at ordinary process priority because the sandbox declined the priority adjustment.

## (ii) Proposition PC — HOLDS

1. **Lines 82–88 and 109–115.** Haar symmetry gives mean zero and second moment $I_4/4$. Jensen gives $Z_c(t)\ge1$, so $\sigma^2(t)\le e^t/4$. Comparing the maximum and minimum densities with Haar costs $e^{2t}$ in the variance-to-energy ratio. With the round unit $S^3$ Haar gap 3, $\rho(t)^{-1}\le e^{2t}/3$. Differentiating $\log\int e^{\langle h,v\rangle}dv$ gives $m(h)$, including at $h=0$. These estimates use the gap convention of lines 84–87.
2. **Lines 118–119.** Fix $W$, and write $E_c$ for integration in factor $c$ alone. Expose the independent coarse links in any order. The $c$th martingale increment is the expectation of $g-E_cg$ over the later links, with the first $c$ links fixed. Its squared $L^2$ norm is at most $E_K[(g-E_cg)^2]$ by Jensen. Orthogonality of the increments gives $\operatorname{Var}_K(g)\le\sum_c E_K\operatorname{Var}_c(g)$. Applying each factor's Poincaré inequality gives line 119 with coefficient one.
3. **Lines 120–125.** Fix a unit tangent $\zeta$ at fine link $\ell$ and set $u_c=\kappa D_\ell M_c[\zeta]$. At fixed $W$ the differentiated log density is $\sum_c\langle u_c,V_c-m_c\rangle$. The compact smooth kernel permits differentiation under the integral, so $Kg$ is a valid test for the fine inequality. Independence and centering give

   $$
   D_\ell(Kg)[\zeta]
     =\sum_c E_{-c}\operatorname{Cov}_c(g,\langle u_c,V_c\rangle).
   $$

   Here $E_{-c}$ integrates the other factors. In vector form, $\nabla_\ell(Kg)=\kappa\sum_c(D_\ell M_c)^*E_{-c}\operatorname{Cov}_c(g,V_c)$. Conditional Cauchy–Schwarz bounds the directional covariance by $\sigma(t_c)|u_c|\sqrt{E_c|\nabla_cg|^2/\rho(t_c)}$. Jensen on the other factors, then the supremum over unit tangents at this fixed $W$, gives $|\nabla_\ell Kg|\le\sum_c\alpha_{\ell c}\sqrt{G_c}$ with $G_c=K(|\nabla_cg|^2)(W)$.
4. **Lines 125–128.** Weighted Cauchy–Schwarz gives $(\sum_c\alpha_{\ell c}\sqrt{G_c})^2\le(\sum_d\alpha_{\ell d})(\sum_c\alpha_{\ell c}G_c)$. Multiplication by $w_\ell(W)$ and summation give exactly $\sum_cb_c(W)G_c(W)$. Total variance adds the product-law term. Taking conditional expectation given $V$ places $\rho(t_c)^{-1}+b_c(W)$ against $|\nabla_cg(V)|^2$. This is the asserted $w'_c(V)$, including for nonnegative weights with an infinite right-hand side.

## (iii) Corollary NF — HOLDS

Because $|M_c|\le1$, PC and (F4) give $\alpha_{\ell c}\le \kappa e^{3\kappa/2}p_{\ell c}/\sqrt{12}$. With $w_\ell=1/\rho_0$ the convolution in $b_c$ costs at most $6\cdot2=12$. The bound is uniform in $V$, giving $1/\rho'\le e^{2\kappa}/3+\kappa^2e^{3\kappa}/\rho_0$.

For $x=1/2,3/4$, sum the first four Taylor terms of $e^x$. The tail starts at $x^4/24$ and each later ratio is at most $x/5$. Thus

$$
e^{1/2}\le \frac{79}{48}+\frac5{1728}=\frac{2849}{1728}<\frac{33}{20},
\qquad
e^{3/4}\le \frac{269}{128}+\frac{135}{8704}=\frac{18427}{8704}<\frac{53}{25}.
$$

The positive cross-product differences are 44 and 637. Also $53\cdot15=795<800=2\cdot400$. At $\kappa=1/4$ the one-step bound is therefore $y'\le a+by$, with $y=1/\rho$, $a=11/20$ and $b=2/15$. Iteration gives $y_j\le(33/52)(1-b^j)+b^j y_0$. Finally $33/52+1/32=277/416<2/3$ since $831<832$. The $33/52$ in the row's result line is the fixed point of the rational **upper bound**. At general strength, $\kappa e^{3\kappa/2}<1$ makes the coefficient of the initial inverse gap contract.

## (iv) Theorem NB — HOLDS. Its consequences need correction

**Lines 158–165.** Write $M_{z,t}=\int D_{z,t}$, $A_t=\tfrac18\sum_z M_{z,t}$ and $P=A_{2v}/A_v^2$. Lemma TW preserves each mass separately. NF applies to each normalized law on its product of links, with the least of the sixteen initial gaps as a common lower bound. This proves both clauses for every available $j$. Multiplying the eight $2v$ densities by $c>0$ multiplies $P$ by $c$ and preserves every normalized law. By row 1497's suffix argument, every member at any level with a valid suffix to END must meet the terminal purity threshold. Thus on the unrestricted cone of positive families, a nonempty class specified solely by normalized laws cannot by itself serve at **any** such level. [TW and K2, §§3.2–3.3](gap-k2-tool-design-fable.md) · [Row 1497, §(i)](gap-k2-direction-checkpoint-check-astra62.md)

**What is free, lines 173–178.** NB gives the single Poincaré threshold $3/2$ once the required steps fit. Line 173's “such a property” requires this restriction. A log-Sobolev bound and spatial decay would each need their own argument.

The line-156 heading says weak steps “erase the shape,” echoed on line 312. Take $g$ to be the real part of a coarse plaquette holonomy on an untwisted side-eight fine torus. Start with all fine links equal to 1. Flip the eight fine links crossing the interface of the two cells for one bond of this plaquette. Every contour for that bond crosses its interface once. The other three bonds cross their own interfaces. The four means change from $(1,1,1,1)$ to $(-1,1,1,1)$. By conditional independence, $H=Kg$ takes the two values $\pm m_\kappa^4$, where $m_\kappa=E_{\nu_{\kappa\mathbf1}}\operatorname{Re}V>0$ by pairing $v$ with $-v$. Endpoint gauge covariance makes $H$ gauge invariant. The smooth densities $1\pm\epsilon(H-\int H)$ therefore give image means of $g$ differing by $2\epsilon\operatorname{Var}_{\rm Haar}H>0$. For small $\epsilon$ both initial gaps exceed 2 by comparison with product Haar. At $\kappa=1/4$, NF gives both image inverse gaps at most $11/20+1/15=37/60<2/3$. Thus even within the asserted Poincaré class a weak step preserves a measurable difference in shape.

The first false numerical comparison is **line 176, “fewer than the $\log_2 n$ halvings”**. Set $b=2/15$. The proven sufficient depth is

$$
j_* = \max\!\left(0,\left\lceil\frac{\log(32/\rho_0)}{\log(15/2)}\right\rceil\right).
$$

For instance, take $n=2^{12}$ and $A=8/3<\log_2(15/2)$. At the allowed lower bound $\rho_0=n^{-A}=2^{-32}$, even $b^{12}>2^{-36}>\rho_0/32$. This falsifies the comparison of the sufficient depths. Whether an individual law reaches the threshold earlier is a separate question. For a dyadic sequence with enough admissible halvings, $A<\log_2(15/2)$ gives the claimed comparison **eventually**. An arbitrary even side can have just one factor of two. K2 also needs both time lengths to admit every step. Row 1468 writes the actual budget as $l=512\,2^N v_E$ with $v_E\ge4$.

**Consequence 3, lines 179–183 — FAILS as an inference.** Line 179 changes “cannot suffice on its own” to “cannot carry any part.” Suppose a separate input fixes $D_{z,t}(W^*_{z,t})=a^{N_t}$ at reference fields for one $a>0$, with $N_{2v}=2N_v$. For normalized densities $p_{z,t}$, $M_{z,t}=a^{N_t}/p_{z,t}(W^*_{z,t})$. The powers of $a$ cancel in $P$. For example, $p_{z,2v}(W^*_{z,2v})\le1\le p_{z,v}(W^*_{z,v})$ for every $z$ implies $P\ge1$. The reference condition alone allows different purities. For a common Wilson action path $D_s=e^{sL}$ there is also the exact identity $d\log M/ds=E_{\mu_s}L$ with $M(0)=1$ on each torus. A normalized energy estimate could enter a comparison of those masses. Row 1497(i) remains open for such mixed proofs.

The signed constant-mode calculation in §3.5 also checks. Sum the linearized contours for one coarse direction. The translated incoming legs cancel the outgoing legs. The straights leave $Q^*\mathbf1_\mu=\mathbf1_\mu/8$ on fine links. Applying $Q$ gives $2/8=1/4$ on that coarse mode. The proposed weak-coupling sign on lines 194–196 remains heuristic.

## (v) Lemma REV — HOLDS as a conditional implication

For almost every $V$, let $F(V)=E[f(W)\mid V]$. The numerator $\int fK\,d\mu$ and the strictly positive denominator $\int K\,d\mu$ are smooth in $V$ by compactness. In a tangent direction at $V_c$ only the $c$th numerator of the product kernel varies. Its log gradient is

$$
S_c=\kappa\big(M_c-\langle M_c,V_c\rangle V_c\big),\qquad
\nabla_c F=E_{\mu^V}[f S_c]-F E_{\mu^V} S_c.
$$

The second term comes from differentiating the **posterior denominator**. This recovers the posterior-score response used in the earlier chart and cap estimates. Total variance gives $E\operatorname{Var}(f\mid V)+\operatorname{Var}_{\mu'} F$. Apply (H1) to the first term. Apply the coarse weighted inequality and then (H2) to the second. All terms are nonnegative, so conditioning their sum on $W$ gives exactly $w_\ell(W)=E[u_\ell+\sum_c w'_c(V)\gamma_{c\ell}\mid W]$.

In each unit tangent direction $a$, $\operatorname{Var}_{\mu^V}\langle a,S_c\rangle\le\kappa^2$. Cauchy–Schwarz, the supremum over $a$, and (H1) give the admissible choice $\gamma_{c\ell}=\kappa^2u_\ell$. This choice gives no decay in $d(c,\ell)$. At line 245 the posterior gap is (H1). A bound on covariance with the score alone, (H2), need not control posterior variance for every test.

## (vi) What (FL) weakens

**Lines 240–242 — correction required.** By REV, (H2) controls $|\nabla_c E[f\mid V]|^2$ on the Q2 posterior. A deterministic version of (H2) with coefficients $C e^{-m d(c,\ell)}$ immediately gives (FL). For a test supported on $\ell$ with $\|\nabla_\ell f\|_\infty\le1$, (FL) yields $E_{\mu'}|\operatorname{Cov}_{\mu^V}(f,S_c)|^2\le C e^{-m d(c,\ell)}$. It allows large responses on rare coarse fields.

An exact one-score example separates those two formulations in general. At separation $r$, take $W$ Haar on $S^3$ and an independent observed flag $B$ of probability $e^{-r}$ of being one. Given $W,B$, draw $V$ from $k(BW,V)$. Condition on $(B,V)$. For $B=0$ the score vanishes. For $B=1$ the posterior of $W$ is $\nu_V$ and the score is the tangent projection of $W$. By (F2) and Cauchy–Schwarz, $\gamma=e^2B/3$ works for every smooth $f$ and $E\gamma=e^{2-r}/3$. On the positive-probability event $B=1$, choose unit $a\perp V$ and $f(W)=\langle a,W\rangle$. Then $\|\nabla f\|\le1$ and $\operatorname{Cov}(f,\langle a,S\rangle)=\operatorname{Var}_{\nu_V}(f)\ge e^{-2}/4$, by tangent symmetry and the density lower bound. Any deterministic coefficient for this link must be at least $e^{-4}/16$ for every $r$. This separates average and uniform coefficients for conditional scores. It makes no assertion about which estimate Wilson satisfies.

The **actual** (TILT-COV-sup) in row 968, lines 128–137 and 158–160, bounds $\operatorname{Var}_{J_{b_t,\phi}}\langle z,x/s+w/s'\rangle\le\bar k_{s,t}|z|^2$ for all bridge tilts $\phi$ and horizontal $z$. Its law is a tilted pair of time slices. Its tests are linear and its conclusion is an operator-norm bound. (FL) uses the four-dimensional Q2 posterior at $\kappa=\beta\in[2,3]$, all smooth fine tests and link-resolved exponential decay. Even on one law, a uniform covariance norm alone contains no distance estimate. A Gaussian pair at sites $r$ apart can have unit variances and covariance $1/2$ under every linear tilt, with covariance norm $3/2$ at every $r$.

Row 968's (LOC-COV) bounds the horizontal Hessian of the bridge potential by a diagonal form with exceptional sets. Its Proposition AVG identifies two integrated **curvature** tests with a pointwise Hessian bound and a bridge Poincaré bound. Neither identification applies to a squared posterior score covariance. Thus the cited rows give neither the claimed implication at line 240 nor an equivalence with an already settled criterion. Strictness is proved above only against uniform local (H2) for a common conditional experiment. The ordering of (FL) and the named bridge hypothesis for Wilson remains unproved. [Row 968, §§3.1–3.3, 5.4, 6.3](gap-avgcurv-max.md) · [Row 970, §§6–7](gap-avgcurv-check-astra.md)

(FL) itself remains open. Even if supplied, it would bound the score term in one reverse step. REV also needs (H1), a coarse weighted inequality, and, on iteration, control of the products of the random weights. None of the six checks yields a bound on the sixteen masses of the Wilson family.
