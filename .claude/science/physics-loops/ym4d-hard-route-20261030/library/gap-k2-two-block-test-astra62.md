## Repo search

**Proved as a search record.** Row 1495, checkout `52ccf516890e`. The named prior file is absent. I searched Markdown and TeX on `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). The precursor names, “903-dimensional Gaussian”, “301 free links”, “unsplit cold cut/mark/coefficient” and “49 link indices” returned no lines on those refs. The same search in the working checkout located row 1492. A second five-ref search for “squared cold mark”, second moments of cold factors or private crossings, and antipodal crossing flips returned no hits. Row 1492 supplies the single private-link Haar argument used below.

- In the soft-route `ym4d-proof/RD4.md`, lines 448–460 on PRs 10114 and 10133, exact overlap-component factorization with common local references and a mixed majorant imply the connected log bound (L7). The search for “mixed majorant” also found `MIXSMALL.md` 61–73, whose MS3 requires a weighted row at most $1/4$ and factorization on the MS2 reference. `RETAINED_RETURN_CONSTRUCTION_ASTRA.md` 586–595 identifies an outside-score covariance even after the conditional fibres factor. `REVIEW_RD4.md` 63 and `checks/rd4_review.md` 203–209 confirm the conditional log implication. `checks/mixsmall_hole_analysis.md` 556 requires the actual joint events and a common law for its mixed-jet bound. The November 8 digest §9 records its joint-reference requirement. [Prior search](prior/repo-search-2026-11-08.md)
- A capped “coarse Fourier / Bloch symbol or matrix / Gaussian Schur complement” search hit main’s `su2-gauge-aligned-response-20261108/gates/forest-flat-check.md`. Its flat check at lines 54–61 treats a two-step Hessian with intermediate links. Periodic block trees give finite Bloch matrices, and the inverse Schur precision is the restricted covariance. The side-two pin here has a different precision.
- Row 1480 defines the 384 labelled paths and the one-colour precision $H=d^*d+Q^*Q$. Its earlier Haar-polynomial moment construction prices compact-posterior insertions. The present hybrid integral also has the exterior Gaussian. Row 1490 gives the stripe stationary point and Hessian. Row 1492 gives the exact mark, the 301-link support, and the large-$x$ cubic limit. Its endpoint test is explicitly open. FINISH assigns row 1494 the check of those reductions. The registry search found H-SF and H-LF, both more general, and no owner for this endpoint calculation other than row 1495 in FINISH. [Row 1480](gap-k2-integrated-activity-astra62.md) · [Row 1490](gap-k2-nonlinear-pin-astra62.md) · [Row 1492](gap-k2-nonlinear-activity-astra62.md) · [Registry](open-registry.md)

**Published inputs, proved as a statement of scope.** The outline index, chunks 01, 02, 05 and 07 and the obligations list, point to the rooted criterion and its analytic inputs. Outline lines 1271–1279 and 1357–1373 require the incompatibility sum before applying the tree bound. Lines 5468–5479 assume a common majorant for the relative logarithm. QC1–QC3 at 7945–7987 define the odd-block logarithmic map. CA-II 3521–3556 gives a resummed decay bound for potentials satisfying Bałaban’s cutoff and smallness conditions. In the local quotations, CMP 109, p. 259 and CMP 122, p. 185 require sufficiently small parameters. The sources are the supplied `31a47c543775` bundle of Ethan Sussman and Levent Alpoge, written with Claude and Codex. Credit Tadeusz Bałaban for the renormalization method and Roman Kotecký and David Preiss for the rooted criterion. [Index](sa-index/README.md) · [Obligations](sa-index/obligations.md) · [Bałaban record](lit-balaban.md) · [Quotations](gap-k2-floor-sizing-opus.md)

## Result for row 1495

**Proved by hand, endpoint open.** For the specified pair at $x=100$ I obtain $2^{-20642}-1< J_{BD}/J_B^2-1 <2^{21136}-1$. This full-domain interval crosses both decision boundaries. The radial denominators can be approximated uniformly with relative cost below $2^{-55}$ in the ratio. A direct variance bound has right side above $2^{5440}-1$, even with every plaquette cold.

**Sketched as formal computation.** The $\mathbb Q(i)$ Fourier solve, its real-space column check and the cubic contraction give $3267474411/10^{11}< A_1/100<3267474412/10^{11}$. This prices the leading term. Deciding the endpoint still requires a signed remainder bound or a sharper joint integration. The finite arithmetic was replayed outside Lean. This is research text by Codex and grants no scientific or audit status.

## Plan saved at creation

1. [Sketched] Read the prior-work inventory, owner rules, index and cited definitions. Identify the pair, normalization and unresolved test.
2. [Sketched] Check the full-repository refs and the open registry before deriving anything.
3. [Sketched] Use exact arithmetic to reduce the specified two-block integral. Retain the radial factors, the joint cold cut and all covariance directions.
4. [Sketched] Seek a certified comparison with \(1/(81e)\). Record the trusted base and Lean source for any deciding kernel check.
5. [Sketched] Verify the scope of the result and give the next two rows with decisive outcomes.

## Fourier marginal at the endpoint

**Proved by finite Fourier transformation.** Take $B=0$, $D=e_1$, $a=1$, $t=0$, $x=100$. Write $Y=10Z$. Index the free link types by $(b,\mu)$ in lexicographic order, $b\in\{0,1\}^4$, $1\le\mu\le4$. Skip an edge if $b_\mu=0$ and $b_j=0$ for every $j<\mu$. The skipped edges form the root-to-site comb in order $4,3,2,1$. In a path, replace a free positive edge of type $j$ with tail in block $u$ by $i^{k\cdot u}e_j^T$. A reversed edge uses the negative of the row at its positive tail. Put these signed sums in the 96 rows of $d(k)$. For the four rows of $Q(k)$, average the signed sums over *all* 384 labelled paths in row 1480. A block mode is $Y(u)=i^{k\cdot u}y$, $k\in(\mathbb Z/4)^4$. Its one-colour precision and the read covariance are
$$
 H(k)=d(k)^*d(k)+Q(k)^*Q(k),\qquad
 C_{(u,j),(v,l)}=\frac1{256}\sum_k i^{k\cdot(u-v)}H(k)^{-1}_{jl}.
$$
The formula follows by applying character orthogonality to the quadratic action. Row 1480 supplies strict positivity on the tree slice. Conjugate frequencies give a real rational $C$. Restrict this matrix to the 301-link union in row 1492. The three colours of $Z$ have independent copies of $C/100$. The shared 29 links have a single integration variable each.

**Sketched as formal computation.** I evaluated all 256 frequencies by conjugation from 136 representatives. I formed $q=192Q$ with Gaussian integer entries. The top-left inverse block of
$$
 \begin{pmatrix}d^*d&q^*\\q&-192^2 I_4\end{pmatrix}
$$
is $H^{-1}$ by elimination of the four auxiliary variables. Fraction-free elimination produced $X_k/s_k$ with Gaussian integer $X_k$ and positive integer $s_k$. For every representative, a separate integer matrix multiplication gave
$$
 (192^2d^*d+q^*q)X_k=192^2s_k I_{49}.
$$
The inverse transform used the quarter turns $1,i,-1,-i$ and covered 46 relative shifts. In block-then-link lexicographic order the resulting one-colour $301\times301$ covariance has least common denominator
$$
 L=35320839146592706051799300150263357111702055251004620800 .
$$
An example is the covariance between the direction-4 links with tail bits $(0,0,0,1)$ in $B,D$. In $Y$ units the computation gives
$$
 231985376683736116329825075637519428970269657967
 \;/\;4485272496255509446252080059229506031316674969600 .
$$
For reproduction, the SHA-256 is `be9578db0f13df95ecdbd29a89b6902904e8ba56149d7966b1fbf42aa291a591`. Hash the decimal $L$ and a newline, then all rows as signed decimal integers separated by single spaces, each with a final newline. The arithmetic used integers throughout. The replay below also applies the real-space plaquette and pin stencils to a full covariance column and recovers the point source exactly. Peak RSS in the initial marginal calculation was 103 MiB. The complete replay extracted from this note used 147,865,600 bytes at peak and exited successfully.

## Size of the first pair coefficient

**Proved contraction identity.** Let $u_I$ be the coefficient of the oriented triple of links $I$ in $-U_B$ of row 1492. Its Wilson part adds the signed wedge of each ordered triple along each plaquette. For each pin the addition is the three-form $q\wedge A$. Here $q$ is the averaged signed path row and $A$ is the average of $\sum_{h<l}v_h\wedge v_l$ over the same labelled paths. Antisymmetry removes repeated link indices. Since colours are independent with the same covariance, Wick contraction gives
$$
 A_1=\mathbb E[U_BU_D]=6\sum_{I,J}u_Iu_J\det C_{I,J+e_1}.
$$
To obtain the factor six, expand both colour determinants and pair each colour once across the two determinants. Each relative permutation has six copies. With $T=C_{B,D}$, a pin three-form on $D$ transforms to $(Tq)\wedge(TAT^T)$ when $A$ is stored as its skew matrix. The two overall minus signs cancel.

**Sketched as formal computation.** Integer weights $384^2 u_I$ gave 215 nonzero Wilson triples and 22,796 nonzero triples after adding the pins. Multiplying with the rational Fourier covariance gave
$$
 3267474411/10^9 < A_1 < 3267474412/10^9 .
$$
The exact fraction from the integer calculation was

```text
64146219731483676675553051962889190146478363222861622699103455650736912396032989267124320749027814287229798355217041967330768196226747827121873379671383917757/19631743559566812735302110135874192099000776278757666369171420320478644930539519409394787948284075288693915192812565510418294257019815123590213707759616000000
```

**Proved implication with an open finite remainder.** If the displayed computation is kernel-checked and $z(100)=J_{BD}/J_B^2-1$ satisfies $z(100)\ge A_1/100-7/250$, it follows that $z(100)>1/(81e)$. Indeed $A_1>3267/1000$ gives $A_1/100-7/250>467/100000>1/216$, and $e>1+1+1/2+1/6=8/3$. Row 1492 establishes the limit of $xz(x)$. The tolerance $7/250$ here concerns a single finite coupling. It requires control of the full unsplit cut integral and all higher-order terms. For a rational price of the KP threshold, let $E=\sum_{j=0}^{16}1/j!$. Its series gives $E<e<E+18/(17\cdot17!)$. Cross multiplication gives $4541721495/10^{12}<1/(81e)<4541721496/10^{12}$.

## The actual finite-coupling integral

**Proved.** For $T=\{B\}$ or $\{B,D\}$, let $m=165$ or $301$ and let $C_T$ denote the corresponding restriction of the one-colour $Y$ covariance. Form $A_T$ by summing $d_p^*d_p$ and $Q_c^*Q_c$ for the assigned plaquettes and pins. Set $K_T=C_T^{-1}-A_T$. To see $K_T\succeq0$, minimize the full quadratic energy over the exterior links with the read links fixed. The marked quadratic terms are fixed during this minimization. The remaining minimum is nonnegative.

Put $V=4\pi^4/3$, the volume of the three-ball of radius $\pi$, and let $\nu$ be uniform probability on the product of the $m$ such balls. Write $W_p$ for the ordered group plaquette and $M_c$ for the quaternion path mean. The strict cut is $\operatorname{Re}W_p>7/8$, since $|1-W_p|^2=2(1-\operatorname{Re}W_p)$. With $F(s)=\int_{S^3}e^{s q_0}\,dq$ for normalized Haar measure, define
$$
 b_c(z)=e^{-100(1-\operatorname{Re}M_c)}\frac{F(100)}{F(100|M_c|)}.
$$
This equals the exact phase times $h(100)/h(100|M_c|)$ of row 1492, also at $M_c=0$. The density after cancellation of the marked quadratic is
$$
 w_T(z)=e^{-50\sum_{\alpha=1}^3 z_\alpha^T K_T z_\alpha}
 \prod_{e\text{ assigned}}\operatorname{sinc}^2|z_e|\,
 \prod_{p\text{ assigned}}e^{-100(1-\operatorname{Re}W_p)}
 \prod_{c\text{ assigned}} b_c(z).
$$
Set $I_T=\int w_T\prod_p {\bf1}_{\{\operatorname{Re}W_p>7/8\}}\,d\nu$. Gaussian marginalization gives
$$
 J_T=V^m(100/(2\pi))^{3m/2}(\det C_T)^{-3/2}I_T .
$$
Every factor of $w_T$ is in $[0,1]$. For the pin, $|M_c|\le1$, $\operatorname{Re}M_c\le |M_c|$, and $h(s)=e^{-s}F(s)$ is decreasing for $s\ge0$.

**Proved. Uniform relative enclosure of all eight radial denominators.** For $0\le v\le1$ set
$$
 P(v)=\sum_{j=0}^{128}\frac{(2500v)^j}{j!(j+1)!},\qquad \delta=2^{-59}.
$$
The Haar density of $q_0$ is $2\sqrt{1-q_0^2}/\pi$. Its even moments are $(2j)!/(4^j j!(j+1)!)$, by integration by parts. The resulting power series for $F(100\sqrt v)$ has positive terms. From index 99 onwards their successive ratios are at most $2500/(100\cdot101)<1/4$. The omitted sum is at most $(4/3)4^{-30}$ times term 99. Thus
$$
 P(v)\le F(100\sqrt v)\le (1+\delta)P(v).
$$
The constant $F(100)^8$ cancels in $R=J_{BD}/J_B^2$. Replacing each denominator by $P(|M_c|^2)$ in that ratio gives $\widehat R$ with
$$
 (1+\delta)^{-8}\widehat R\le R\le(1+\delta)^8\widehat R .
$$
The cut and all Haar factors remain inside these integrals. The relative enlargement in either direction is below $2^{-55}$, since $(1+\delta)^8\le 1+255\delta$ in general for $\delta\le1$, and the sharper binomial bound $1+8\delta+247\delta^2<1+16\delta$ applies here.

**Proved. Uniform precision bound for these integrals.** One plaquette has four edge occurrences and one link belongs to six plaquettes. Thus $\|d\|_2^2\le4\cdot6$. The absolute row sum of $Q$ is at most the average path length $2+2\mathbb E|b|_1=6$. For a fixed internal edge, at most eight coarse bonds have an offset leg in its block. Each such leg uses it only when the offset has a one in the edge direction, which has probability $1/2$. The straight segments contribute a total of $1/8$ to the column sum. For an internal edge this is $1/16$ from each of the two possible tail blocks. For a crossing it is $1/8$ from its unique tail block, with no leg contribution. Deleting tree edges can only decrease the absolute incidence bound. Consequently $\|Q\|_2^2\le6(4+1/8)$ and $H\preceq49I$. Testing the exterior minimization at zero gives $0\preceq K_T\preceq49I$.

**Proved. Weighted boundary-strip price at $x=100$.** Let $p$ be any assigned plaquette. It has a free assigned edge. If either of the two positive edges at its base crosses a block face, that edge works. Otherwise opposite tails also lie in the base block, and the tree cannot contain all four edges of a square. Fix the other links. The selected edge occurs once, so its Haar variable sends $W_p$ to Haar by multiplication and possibly inversion. The sinc squared of that edge converts its uniform-ball measure to $3/(2\pi^2)$ times normalized Haar. All other factors of $w_T$ are at most one. For any $h>0$,
$$
 \int w_T\,{\bf1}_{\{|\operatorname{Re}W_p-7/8|\le h\}}\,d\nu
 \le\frac{3}{2\pi^2}\frac{4h}{\pi}<h/4 .
$$
The last step uses $\pi>3$. A simultaneous inner or outer approximation of all cuts within $h$ in real part therefore costs at most $48h$ in $I_{BD}$ or $24h$ in $I_B$. This estimate prices integration error at the literal threshold. The activity still uses the product of the unsplit cold indicators. The estimate is absolute in uniform-ball normalization.

**Proved. Size of the smooth variation.** Write $\eta=\max_e|z_e-z'_e|$. The quaternion exponential is 1-Lipschitz on imaginary vectors by its integral derivative and unitarity. A Wilson factor costs at most $400\eta$ and a pin at most $2000\eta$. For the pin, $|(\log F)'|\le1$, the norm is 1-Lipschitz and the mean of paths of length at most ten changes by at most $10\eta$. Both positive factors are at most one, so a log bound is also an additive bound. The squared sinc costs at most $\eta$ using $\operatorname{sinc}(s)=\int_0^1\cos(ts)\,dt$. Finally, the Euclidean gradient of the exterior factor is bounded by $10\sqrt{\|K_T\|}\le70$, since $r e^{-50r^2}\le1/10$ for $r\ge0$. Converting to the maximum link norm costs $\sqrt m<18$. Telescoping the factors gives $|w_T(z)-w_T(z')|<95000\eta$ for $\eta>0$, for either integral. In a cell of diameter $\eta$ in this norm each plaquette real part varies by at most $4\eta$. Thus a point rule with exact cell masses has absolute error at most $(95000+4\cdot48)\eta$ in $I_{BD}$, and the same bound works for $I_B$. Indeed a misclassified point lies in the priced strip. One can charge its true $w_T$ and bound the smooth variation once.

## Endpoint bounds and their precision

**Proved, full-domain enclosure.** Write $t_T=|T|$. On $|z_e|\le1/32$ for every read link, the joint cut holds since every plaquette chord is at most $4/32$. The Wilson energy per plaquette is at most $8/32^2$. Every pin obeys $b_c\ge e^{-100(1-\operatorname{Re}M_c)}$, since $F$ is increasing on $[0,\infty)$. Its energy $1-\operatorname{Re}M_c$ is at most $50/32^2$ by the same chord bound on each transporter. All assigned squared sinc factors together exceed $1/2$ by $\operatorname{sinc}^2 r\ge1-r^2/3$ here and $49t_T\le98$. The exterior exponent costs at most $50\cdot49m/32^2 <5m/2$. The ball restriction has $\nu$-mass $(32\pi)^{-3m}>2^{-21m}$. With $100(96\cdot8+4\cdot50)/32^2<95$ and $e<4$, this gives
$$
 2^{-26m-190t_T-1}<I_T\le1.
$$
By row 1490 and the precision bound above, $I/49\preceq C_T\preceq108900 I$ in matrix order. The normalizing multiplier of $I_T$ in $J_T$ lies between $2^{-15m}$ and $2^{24m}$. Indeed $2^6<V<2^9$, $100/(2\pi\,108900)>2^{-14}$ and $4900/(2\pi)<2^{10}$. Substituting the two dimensions yields the rational endpoint enclosure
$$
                 2^{-20642}-1 < z(100) < 2^{21136}-1 .
$$
Both signs and both sides of the KP threshold lie in this interval.

**Sketched as formal computation, Gaussian normalization isolated.** For the uniform-ball integrals defined above write $R=J_{BD}/J_B^2=G I_{BD}/I_B^2$. Exactly,
$$
 G^2=\left(\frac{9}{2000000\,\pi^5}\right)^{29}
                \frac{(\det C_B)^6}{(\det C_{BD})^3}.
$$
The integer calculation encloses $G$ between $1355475454308\,2^{-474}$ and $1355475454309\,2^{-474}$. I used lower triangular integer factors $P$ at scale $s=2^{128}$. For each read matrix the exact row sums gave $49\|PP^T/s^2-C_T\|_\infty<2^{-112}$. The lower bound $C_T\succeq I/49$ converts this to a relative quadratic-form error. Determinants are then bounded using the powers $m$ of $1\pm2^{-112}$ and $\det(PP^T/s^2)=(\prod_j P_{jj}/s^m)^2$. For the squared prefactor, the total determinant exponent is $6\cdot165+3\cdot301=1893$. Thus $(1-2^{-112})^{1893}\ge1-1893\,2^{-112}>1-2^{-97}$. The reciprocal bounds the upward factor. Machin's identity and alternating arctangent sums at $1/5,1/239$ with 40 and 12 terms bound $\pi$ on both sides. All endpoint comparisons were squared before integer comparison.

**Proved limitation of a variance estimate for this pair.** For its upper test, Cauchy–Schwarz gives $|z(100)|\le\mathbb E F_{B,C}^2/J_B^2-1$. The right side exceeds $2^{5440}-1$ on this very torus. The large second moment comes from fields that pass the unsplit cold cut.

Take $s=25/8$ and a fixed unit imaginary quaternion. Use scalar logs in that direction. Start from the gradient of the fine potential constant on each block, equal to $-s$ on $B$ and zero elsewhere. Every outgoing crossing of $B$ has log $s$. Change the sign of its four crossings at the fine tail $(1,1,1,1)$. Call the read vector $z^*$. Each changed link occurs only in plaquettes and pins assigned to $B$, as in the private-link argument of row 1492. Extend by the original gradient outside the read set. All unmarked curls vanish. Only the four incoming pins have nonzero unmarked quadratic energy, a total $2s^2<20$. Hence $E_0(z^*)=\tfrac12\sum_\alpha(z^*_\alpha)^TK_Bz^*_\alpha<20$.

Restrict all 165 read links to balls of radius $\epsilon=1/1024$ about $z^*$. They are inside the principal chart. For each ordered pair $\mu\ne\nu$ the plaquette in directions $\mu,\nu$ with base $(1,1,1,1)-e_\nu$ contains exactly one changed link. These twelve plaquettes have additive curl of length $2s$ at the centre and length greater than $6$ on the balls. Thus the *marked quadratic* $G_B=\tfrac12\sum_\alpha z_\alpha^TA_B z_\alpha$ exceeds $216$. The triangle inequality for the seminorm $\sqrt{E_0}$ and $K_B\preceq49I$ give $\sqrt{E_0(z)}<\sqrt{20}+\sqrt{49\cdot165/2}/1024<5$. In the group, the starting field was flat. Reversing one of the four logs changes its group element by $2\sin s<2/56$. A plaquette reads at most two changed links. Its chord on the balls is less than $4/56+4/1024<1/8$. Every cut passes. The total Wilson energy is at most $96/128$, and $\sum_c(1-\operatorname{Re}M_c)\le8$.

For the elementary angle bounds one can use $157/50<\pi<22/7$, from $\pi=16\arctan(1/5)-4\arctan(1/239)$ by the first two and three alternating terms at $1/5$ and the first one and two at $1/239$. Thus $\pi-s-\epsilon>1/100$. Each assigned sinc exceeds $1/800$ on the balls. On $[0,1]$ it exceeds $1/2$, and on $[1,\pi-1/100]$ use $\sin r\ge\sin(1/100)>1/200$ and $r<4$.

In the squared moment, cancellation against the Gaussian leaves the multiplier $\exp[100(G_B-E_0)]$. The exact squared pins are bounded below by $e^{-200\sum_c(1-\operatorname{Re}M_c)}$. Together with the squared Wilson weights the exponential is greater than $e^{100(216-25-18)}=e^{17300}$. The 49 fourth powers of the sinc contribute more than $2^{-1960}$. The product balls have $\nu$-mass greater than $2^{-5940}$. Write $N_B=J_B/I_B<2^{3960}$. The squared moment has the same Gaussian multiplier $N_B$, and $J_B\le N_B$. Hence
$$
 \frac{\mathbb E F_{B,C}^2}{J_B^2}
 > e^{17300}2^{-1960-5940-3960}>2^{5440}.
$$
For two distinct marks the Gaussian leaves the positive exterior quadratic $K_{BD}$ and the two physical weights. The extra $+G_B$ in the square arose because the same quadratic was inserted twice. The trial therefore measures the loss in Cauchy–Schwarz. It leaves the signed pair comparison open.

## Two attempts to tighten the endpoint enclosure

**Proved error bound, sketched direct quadrature.** A cell rule can use rational masses even for the full principal balls. For each link write
$$
 z=\pi r\,(\sqrt{1-u^2}\cos(2\pi v),\sqrt{1-u^2}\sin(2\pi v),u).
$$
Under $\nu$ the radial CDF is $r^3$. The variables $u,v$ are independent uniform on $[-1,1]$ and $[0,1]$. Use $n,n^2,n$ equal intervals respectively for $r,u,v$. Each cell has rational mass, from a difference of cubes and two interval lengths. Its link diameter is below $64/n$ by $|\sqrt{1-u^2}-\sqrt{1-u'^2}|\le\sqrt{2|u-u'|}$. Products of these cells cover all read variables. Evaluate the smooth part to absolute precision $\eta=64/n$ at one representative and the real parts of its plaquettes to the same precision. Enclose an ambiguous indicator by $[0,1]$. An erroneous or ambiguous classification can affect only points within $6\eta$ of the threshold. The smooth variation and strip estimates above give an error below $2^{17}\eta$ on each side of either moment $I_T$. The bound includes the smooth evaluation error. Rational bisection bounds square roots. The sine and cosine power series, with the next term bounding the tail after terms decrease, suffice for the link exponential. For the scalar exponential one may divide its argument by a power of two to enter $[-1,1]$, bound the Taylor tail by $3/(k+1)!$ there, then square intervals. For $F$ the positive series can be continued to any required precision. These rules cover zero norms by the sinc series.

For example $n=2^{8260}$ gives error below $2^{-8237}$. The lower bounds above give $I_{BD}>2^{-8207}$ and $I_B>2^{-4481}$. This would control the relative error of each moment to $2^{-30}$. The pair rule at this specified mesh has $n^{4\cdot301}>2^{9,000,000}$ cells. I did not evaluate that sum. It gives an explicit cost for this rule, with no lower bound on the cost of other rules.

**Proved conditional integration step.** A crossing link in direction $\mu$ with tail in coarse block $u$ can be read by $u$ and by $u-e_\nu$ for the transverse directions $\nu$ where its tail bit vanishes. The latter reads come from a plaquette whose transverse step enters $u$. A contour reads crossings only on its own coarse bond. Internal links occur on the ordered legs, including legs of pins from negative neighbours. Consequently the four crossings of tail bits $(1,1,1,1)$ in each marked block are private to their own block. Three more in $D$, in directions $2,3,4$ with tail bits $(0,1,1,1)$, are read by $B,D$ alone. All eleven have zero row and column in $K_{BD}$, since the unmarked action reads none of them. Their sinc factors convert to Haar exactly. Conditional on all other links this leaves a compact eleven-link group integral and 870 outer real coordinates.

For one all-ones crossing in each block, the two conditional group integrands factor. In a given crossing variable $q$ every incident plaquette real part is a linear functional of its four quaternion coordinates. The sole pin has an affine mean, and its linear part has norm at most $1/8$ since exactly 48 of the 384 paths use the crossing once. Use $q=(u_0,u_1,r\cos\theta,r\sin\theta)$ with $r^2=1-u_0^2-u_1^2$. Under Haar, $(u_0,u_1)$ is uniform on the unit disk, and $\theta$ is uniform on the circle. This follows by writing the two coordinate pairs in polar form on $S^3$. The squared radius of the first pair is uniform on $[0,1]$. At fixed disk point the six cold tests are literal circle inequalities of the form $a\cos\theta+b\sin\theta>c$. Their intersection is a union of arcs, possibly empty. Angle-independent inequalities are tested directly. Keep their intersection in the angular integral.

On every allowed arc the log of the positive weight has Lipschitz constant at most $6\cdot100+200/8=625$ in $\theta$. The exterior quadratic never reads this variable. On subarcs of length at most $2^{-20}$, weighting midpoint values by the actual subarc lengths costs at most $625\,2^{-21}$ in the log of this conditional integral when nonzero. An empty set gives zero exactly. The positivity of the remaining integration propagates this multiplicative bound. Applying it to one angle per block costs at most $1250\,2^{-20}<1/800$ in the log of the final ratio, including both copies of the singleton. This estimate holds even for arbitrarily short allowed arcs. The arc endpoints can be enclosed by solving the corresponding line-circle intersections and bounding their angles. The remaining outer integrals have not been enclosed to decision precision.

## Reproduction and proof basis

**Proved as a run record.** The standalone Python source below reproduces the marginal, the cubic fraction and the Gaussian prefactor. It uses integer matrix products, rational scalar arithmetic and integer square roots. The real-space column check uses the forward path rows and their transpose. The reported numerical values use exact arithmetic throughout. The replay ran single-threaded under the machine numeric lock using the lock helper from the named full repository’s local `origin/main`. The sandbox declined the requested process priority change. No Lean executable was available on the search path or at the installation path named in FINISH. I did not obtain kernel output or an axiom report. The machine-dependent numbers are candidate certificates. The hand enclosures and second-moment proof do not use them.

<details>
<summary>Exact-arithmetic replay for the Fourier and Gaussian calculations</summary>

```python
# Python 3, NumPy. Every matrix entry is a Python integer.
from collections import Counter
from fractions import Fraction as Rat
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd, isqrt, lcm, prod
import os
import resource
import sys
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS"):
    os.environ[name] = "1"
import numpy as np

def check_memory():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    if rss > 1850 * 2**20:
        raise MemoryError("RSS guard")

def zeros(shape):
    return np.zeros(shape, dtype=object)

axes = range(4)
zero = (0,) * 4
unit = [tuple(int(a == b) for a in axes) for b in axes]
bits = list(product(range(2), repeat=4))
modes = list(product(range(4), repeat=4))
types = [(b, a) for b in bits for a in axes if b[a] or any(b[:a])]
type_id = {v: j for j, v in enumerate(types)}

def shift(u, v, sign=1):
    return tuple(a + sign*b for a, b in zip(u, v))

def path(x, moves):
    result = []
    for a, sign in moves:
        z = shift(x, unit[a], sign)
        tail = x if sign == 1 else z
        key = (tuple(t % 2 for t in tail), a)
        if key in type_id:
            result.append(((tuple(t // 2 for t in tail), type_id[key]), sign))
        x = z
    return result

plaq = [path(b, [(a, 1), (c, 1), (a, -1), (c, -1)])
        for b in bits for a, c in combinations(axes, 2)]
pins = []
for a in axes:
    paths = []
    for b in bits:
        for order in permutations(axes):
            leg = [i for i in order if b[i]]
            moves = ([(i, 1) for i in leg] + [(a, 1)]*2
                     + [(i, -1) for i in reversed(leg)])
            paths.append(path(zero, moves))
    pins.append(paths)
families = [[p] for p in plaq] + pins
rows = []
read = {(zero, j) for j in range(49)}
for family in families:
    c = Counter()
    for p in family:
        for link, sign in p:
            c[link] += sign
            read.add(link)
    rows.append(c)
B = sorted(read)
D = [(shift(b, unit[0]), j) for b, j in B]
union = sorted(set(B) | set(D))
assert (len(types), len(plaq), len(B), len(set(B) & set(D)), len(union)) == (49,96,165,29,301)
den = 384 // gcd(384, *(v for c in rows[96:] for v in c.values()))
assert den == 192
taps = {}
for i, c in enumerate(rows):
    for (b, j), v in c.items():
        if b not in taps:
            taps[b] = zeros((100, 49))
        taps[b][i,j] = v if i < 96 else v // (384 // den)

def phase(b, k):
    return sum(a*c for a, c in zip(b, k)) % 4

def inverse_mode(k):
    rr, ri = zeros((100,49)), zeros((100,49))
    for b, a in taps.items():
        h = phase(b, k)
        if h == 0: rr += a
        elif h == 1: ri += a
        elif h == 2: rr -= a
        else: ri -= a
    d, f, q, v = rr[:96], ri[:96], rr[96:], ri[96:]
    a, b = d.T @ d + f.T @ f, d.T @ f - f.T @ d
    J = np.eye(49, dtype=object)
    A = np.block([[a,q.T],[q,-den**2*np.eye(4,dtype=object)]])
    T = np.block([[b,-v.T],[v,zeros((4,4))]])
    x = np.concatenate([A, np.vstack([J,zeros((4,49))])], axis=1)
    y = np.concatenate([T, zeros((53,49))], axis=1)
    perm = list(range(53))
    prev = 1
    for j in range(53):
        if not x[j,j]:
            l = next(h for h in range(j+1,53) if x[h,h])
            for ar in (x,y):
                ar[[l,j],:] = ar[[j,l],:]
                ar[:,[l,j]] = ar[:,[j,l]]
            perm[l],perm[j] = perm[j],perm[l]
        pivot = x[j,j]
        assert y[j,j] == 0
        xr, yr = x[:,j+1:], y[:,j+1:]
        u, w = x[:,j:j+1], y[:,j:j+1]
        X = pivot*xr - u*xr[j] + w*yr[j]
        Y = pivot*yr - u*yr[j] - w*xr[j]
        X[j], Y[j] = prev*xr[j], prev*yr[j]
        xr[:], yr[:] = X//prev, Y//prev
        prev = pivot
    idx = np.argsort(perm)[:49]
    x, y = x[idx,53:], y[idx,53:]
    div = (1 if prev > 0 else -1)*gcd(prev,*x.flat,*y.flat)
    s, x, y = prev//div, x//div, y//div
    h = den**2*a + q.T @ q + v.T @ v
    t = den**2*b + q.T @ v - v.T @ q
    assert np.array_equal(h @ x - t @ y, den**2*s*J)
    assert not np.any(h @ y + t @ x)
    return s, x, y

def neg(k):
    return tuple(-v % 4 for v in k)

def difference(b, h):
    return tuple((x-y) % 4 for x,y in zip(b,h))

inv = [(k,*inverse_mode(k)) for k in modes if k <= neg(k)]
common = lcm(*(s for k,s,r,i in inv))
modes_scaled = []
for k,s,r,i in inv:
    f = common//s * (1 if k == neg(k) else 2)
    modes_scaled.append((k, f*r, f*i))
check_memory()

def transform(u, column=None):
    w = zeros((49,49) if column is None else 49)
    for k,r,i in modes_scaled:
        ph = phase(u,k)
        a = r if ph % 2 == 0 else i
        if column is not None: a = a[:,column]
        if ph in (0,3): w += a
        else: w -= a
    return w

groups = {}
for j,(b,i) in enumerate(union):
    groups.setdefault(b,[]).append((j,i))
blocks = {difference(b,h) for b in groups for h in groups}
blocks = {u:transform(u) for u in blocks}
C = zeros((301,301))
for b,bs in groups.items():
    ii,aa = zip(*bs)
    for h,hs in groups.items():
        jj,bb = zip(*hs)
        C[np.ix_(ii,jj)] = blocks[difference(b,h)][np.ix_(aa,bb)]
assert np.array_equal(C,C.T)
lcd = 256*common
div = gcd(lcd,*C.flat)
C, lcd = C//div, lcd//div
digest = sha256((str(lcd)+"\n").encode())
for r in C:
    digest.update((" ".join(map(str,r))+"\n").encode())
print("covariance",lcd,digest.hexdigest(),flush=True)

# A separate real-space stencil check of the first covariance column.
col = {v:transform(v,0) for v in modes}
out = {v:zeros(49) for v in modes}
for v in modes:
    active = [(difference(v,neg(b)),a) for b,a in taps.items()]
    vals = sum((a @ col[h] for h,a in active), start=zeros(100))
    vals[:96] *= den**2
    for h,a in active:
        out[h] += a.T @ vals
out[zero][0] -= 256*common*den**2
assert all(not np.any(v) for v in out.values())
print("real-space column identity checked",flush=True)
check_memory()

idx = {v:i for i,v in enumerate(B)}
def wedge_weight(bank,i,j,k,v):
    if i != j and j != k and i != k:
        sign = -1 if ((i>j)+(i>k)+(j>k)) % 2 else 1
        bank[tuple(sorted((i,j,k)))] += sign*v

weights = Counter()
for p in plaq:
    for (i,a),(j,b),(k,c) in combinations(p,3):
        wedge_weight(weights,idx[i],idx[j],idx[k],a*b*c*384**2)
wilson = {k:v for k,v in weights.items() if v}
pin_forms = []
for family in pins:
    q, A = Counter(), Counter()
    for p in family:
        path_ids = [(idx[i],a) for i,a in p]
        for i,a in path_ids: q[i] += a
        for (i,a),(j,b) in combinations(path_ids,2):
            if i < j: A[i,j] += a*b
            elif j < i: A[j,i] -= a*b
    for i,u in q.items():
        for (j,k),v in A.items():
            wedge_weight(weights,i,j,k,u*v)
    pin_forms.append((q,A))
triples,w = zip(*[(k,v) for k,v in weights.items() if v])
ii,jj,kk = np.array(triples,dtype=np.intp).T
w = np.array(w,dtype=object)
bids = [union.index(b) for b in B]
dids = [union.index(d) for d in D]
X = C[np.ix_(bids,dids)]
total = 0
for (i,j,k),v in wilson.items():
    a,b,c = X[:,i],X[:,j],X[:,k]
    determinants = (a[ii]*(b[jj]*c[kk]-b[kk]*c[jj])
                  + a[jj]*(b[kk]*c[ii]-b[ii]*c[kk])
                  + a[kk]*(b[ii]*c[jj]-b[jj]*c[ii]))
    total += v*(w @ determinants)
for q,A in pin_forms:
    u = sum((v*X[:,i] for i,v in q.items()),start=zeros(165))
    h = zeros(X.shape)
    for (j,k),v in A.items():
        h[:,k] += v*X[:,j]
        h[:,j] -= v*X[:,k]
    h = h @ X.T
    total += w @ (u[ii]*h[jj,kk] + u[jj]*h[kk,ii] + u[kk]*h[ii,jj])
alpha = Rat(6*total,384**4*lcd**3)
print("Wilson and total triples",len(wilson),len(w))
print("cubic",alpha,flush=True)
check_memory()

def root_det_bound(N):
    s = 2**128
    m = len(N)
    P = zeros((m,m))
    target = N*s**2//lcd
    for j in range(m):
        rem = target[j:,j]-P[j:,:j] @ P[j,:j]
        P[j,j] = isqrt(rem[0])
        P[j+1:,j] = rem[1:]//P[j,j]
    diff = abs(lcd*(P @ P.T)-N*s**2)
    assert 49*max(diff.sum(axis=1))*2**112 < lcd*s**2
    return Rat(prod(P.diagonal()),s**m)

def atan_bounds(a,n):
    v = sum((Rat((-1)**j,(2*j+1)*a**(2*j+1)) for j in range(n)),Rat(0))
    w = v+Rat((-1)**n,(2*n+1)*a**(2*n+1))
    return min(v,w),max(v,w)

sb,sp = root_det_bound(C[np.ix_(bids,bids)]),root_det_bound(C)
l,u = atan_bounds(5,40)
v,w = atan_bounds(239,12)
pi_lo,pi_hi = 16*l-4*w,16*u-4*v
g2 = Rat(9,2000000)**29 * sb**12/sp**6
loss = 1-Rat(1,2**97)
lo,hi = loss*g2/pi_hi**145, g2/(loss*pi_lo**145)
a,b = 1355475454308,1355475454309
assert Rat(a,2**474)**2 <= lo <= hi < Rat(b,2**474)**2
print("Gaussian prefactor",a,b,"in units of 2^-474",flush=True)
check_memory()
```

</details>

**Sketched Lean leaf checks.** These statements check the printed fraction against its proposed rational interval, the price of $1/(81e)$ from the two series bounds, and the arithmetic margins. The hypothesis that the printed fraction represents the cubic contraction still needs the matrix and Wick computations checked in Lean. A deciding theorem would also need bounds on the finite integral. The intended trusted base for these leaves is the Lean kernel with `Init`. The source includes the axiom queries for replay.

```lean
import Init

namespace TwoBlock1495

def cubicNum : Nat := 64146219731483676675553051962889190146478363222861622699103455650736912396032989267124320749027814287229798355217041967330768196226747827121873379671383917757
def cubicDen : Nat := 19631743559566812735302110135874192099000776278757666369171420320478644930539519409394787948284075288693915192812565510418294257019815123590213707759616000000

theorem cubicInterval :
    3267474411 * cubicDen < 1000000000 * cubicNum ∧
    1000000000 * cubicNum < 3267474412 * cubicDen := by decide +kernel

theorem eIntervalPrice :
    (4541721495 : Nat) * 81 * 2348085347268533 < 1000000000000 * 863812325376000 ∧
    (1000000000000 : Nat) * 20922789888000 < 4541721496 * 81 * 56874039553217 := by decide +kernel

theorem margin : (100000 : Nat) < 467 * 216 := by decide +kernel

theorem squareBudget :
    (1960 + 5940 + 3960 + 5440 : Nat) ≤ 100 * (216 - 25 - 18) := by decide +kernel

#print axioms cubicInterval
#print axioms eIntervalPrice
#print axioms margin
#print axioms squareBudget

end TwoBlock1495
```

## Next two rows and their decisive outcomes

1. **Sketched. Enclose the two positive moments at 100 after private-link integration.** Use the eleven Haar variables of the pair, the four of the singleton and the unsplit cuts. Carry rational upper and lower errors through the remaining integrals and the Gaussian prefactor. A certified interval for $z(100)$ in either exterior component of $[-1/(81e),1/(81e)]$ refutes the common KP bound for these 81 translates. An interval strictly inside removes this pair obstruction. The one-sided remainder allowance $7/250$ is sufficient for the positive exterior result once the cubic computation is kernel-checked.
2. **Sketched. Price the connected cold and hot marks with their joint denominator.** If the pair survives, use row 1492 (1)–(2) with the same normalized Gaussian and its full cold event. The decisive positive outcome is a uniform rooted sum on $|t|\le\arcsin(1/4)$, $x\ge100$. One unsplit coefficient exceeding its multiplicity budget refutes that statement. An exterior result in the first row already supplies this negative outcome for the current activity.
