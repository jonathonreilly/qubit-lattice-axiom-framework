# Repo search

Row 1265. OpenAI Codex (assigned gpt-6.2-astra, max), checking Claude Opus 5.5's row 1258 at `8af5d34eb64a`. This hand check is research text and grants no status. Unqualified line numbers refer to the source under check. [Row 1258](gap-mini-solve-ag-opus.md)

The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. Its closest hit, PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149, gives a positive one-time loop correlation. The present question needs an upper bound uniform over both boundary slices. Main at `8b11ae2bb95e` contains the identical files for Theorems W and SH and their checks under `research/mass-gap/library/`. W supplies the interior TV estimate. SH propagates a thermal seed to larger boxes. The earlier Lemma WS in `gap-crux-exercise2-max.md` 487 concerns time doubling of a flux ratio. Row 1218 records a periodic thermal criterion, an outer-region maximal-correlation criterion and a forest-gauge Wasserstein criterion. These use different quantities from the middle-slice total variation here.

The task-specific prior file is absent. I found no competing row in `library/open-registry.md`, or earlier check of this implication in the targeted label and slab/cross-ratio searches outside this lane on main and PRs 10114, 10133, 10134, 10141 and 10144. Row 1258 supplies the argument being checked. The search conclusion is limited to those sources and terms.

## Plan

1. Check prior coverage, ownership, and the sources named by the repository search.
2. Trace row 1258 against the outline and complete-account indices and the cited source passages.
3. Check Theorem W(A), Lemma WS, and both seed estimates by hand.
4. Check Lemma WS′ and Proposition RR, including the normalization and power of the kernel.
5. Check the passage from a single cutoff to the hypotheses of Lemma FL and Theorem E-N.
6. Check the ARGUED readings against their sources and record the statement verdicts and result.

## Account passages and scope

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the account setting. The locators are outline chunks 01, 04, 06, 22 and 29 and their neighbouring obligation rows. At revision `31a47c543775` the outline defines volume-first limits at 6873–6881, periodic lifts at 24411–24423 and the positive-time scalar space at 6928–6933. Its matched-cutoff estimates at 4226–4239 and 32104–32123 concern separated insertions. They do not furnish a summable error for the two *total log partition functions* needed here. Lines 588–599 and 31871–31882 distinguish polynomial decay from a positive spectral threshold.

Complete account I, 2512–2527 and 2690–2713, states its hypotheses and its joint-diagonal curvature-sector conclusion. Uniqueness of the vacuum and a mass gap lie outside that theorem. The CA-I index for items 4.12–4.19 covers ultraviolet induction. Its entries do not supply a slab cross-ratio estimate. Rows 916–917 and 1225–1232 use the volume-first formulation in the expanded account at `2bc0658f91d2`. I use their checked implications for that formulation, whose order of limits also appears at outline line 6879. The total-variation and cross-ratio arguments under review are row 1258's.

## Lemma WS and the explicit sizes

**Lemma WS, (2.2), (2.3) and the rectangular four-point bound (3.1), lines 63–164 — HOLDS given Theorem W(A).** I use $\epsilon=\log(1/\delta)/(2(R+2))$ for $0<\delta<1$. If (W) holds with zero disagreement bound, apply every positive $\delta$ and take the limit. Row 691, lines 28 and 83–95, and check 693, §1, give the distance between lower endpoints, the full collar and TV on an entire interior set. Write $F(t,B)=\log Z(t,B)$, $\Phi_B(t)=2F(t,B)-F(2t,B)$ and $S(t;B)=\sum_{j\ge1}(\lambda_j/\lambda_0)^t$ for the full excited trace. [Theorem W](gap-ds-gauge.md) · [Check 693](gap-ds-gauge-check.md)

* **Cut and differentiate, lines 71–117.** Half a spatial action on each side of a cut gives one complete action when the slices are glued. Thus the normalized two-slice density is $K_a(C,C')K_a(C',C)/Z(2a,B)$. Inserting $Q=K_a(C,C)K_a(C',C')/[K_a(C,C')K_a(C',C)]$ leaves the two diagonal integrals, giving $\Phi_B=\log\mathbb E Q$. Changing the Wilson convention from $x_p$ to $x_p-1$ adds a volume term to $F$ which cancels. The sign of the telescope (2.4) is correct. As a separate way to check its constant, move **all** $3V$ top links at once along unit-interval minimizing geodesics, where $V=|B|$. Each top edge occurs once in a temporal plaquette immediately below it. In unit-quaternion coordinates the derivative of its real trace coordinate has modulus bounded by the speed, which is at most $\pi$, including for the inverse edge. The top spatial half-action is identical at both bottoms. Compactness and the finite bounded derivative permit differentiation under the integral. The remaining derivative of the log kernel is the conditional mean of a score whose oscillation is at most $6\pi\beta V$.
* **Condition on the middle slice, lines 119–127.** Split the links into three disjoint sets, lower, middle and upper. At line 120 “lower otherwise” must be read on the complement of the middle slice. Literally a spatial edge at the middle meets a plaquette above it. Assign the purely middle plaquettes to either factor once. The conditional upper law given the middle and top is then the same at both bottoms. Taking its conditional mean cannot increase the score oscillation. Integrating the difference of means along the path bounds the four-point log ratio by $6\pi\beta V$ times the supremum of the middle-slice TV. This also verifies the one-link version (2.5) with ${\rm TV}=\sup_A|P(A)-P'(A)|$.
* **Count the collar, lines 129–142 and 157–164.** A contained block has lower time anchor $b\in[1,a-1-R]$. The possible anchors through a spatial link at $t$ run from $t-R$ to $t$, and through a temporal one from $t-R+1$ to $t$. Thus the two interior time ranges in lines 132–133 are exact. The excluded spatial layers give $2R(3V)$, the temporal layers $2RV$, and the exterior consists of two spatial slices, $6V$. The distance from the middle to this collar is at least $\lfloor a/2\rfloor-R$, also with the time period $2a$. The spatial periods are at least $R+4$, so row 691's embedded-block condition holds. The middle is interior for even $a\ge2R+2$ and odd $a\ge2R+3$. Writing $\eta_*$ for the supremum of the absolute four-point log ratio, W(A) gives (3.1), $\eta_*\le 6\pi\beta(8R+6)V^2[\sqrt\delta/(1-\sqrt\delta)]e^{-\epsilon(\lfloor a/2\rfloor-R)}$. Its diagonal specialization is (2.2). For (2.3), use $\sqrt{\delta}\,e^{\epsilon R}\le1$. The Wilson transfer trace gives $g(a)=\log(1+S(a;B))\ge g(2a)\ge0$, hence $\Phi_B=2g(a)-g(2a)\ge g(a)$. Subtracting the row and column of $\log K_a$ through one fixed reference slice gives exactly the remainder bounded in (3.1).

**Corollary WS1, lines 166–177 — HOLDS, including the printed sufficient side.** The thermal threshold $1/1650$ is the two-stage ratio-two row in Theorem SH (row 705, lines 116–125, 165–180, check 707). Here and below put $r=R+2$, $x=\log\max(1,\beta)$, and take $\delta=1/4$. For $A\ge200$, $\log A/A$ is decreasing and $200<2^8$, so $A^6\le2^{6A/25}$. With $A=n/r$, $M=2n$, (2.3) consequently gives

$$
 \Phi_B(n)\le6144\pi\,\beta r^7 A^6 2^{-A/2}
             \le6144\pi\,\beta r^7 2^{-13A/50}.
$$

The integral of $1/t$ from 1 to 2 is greater than $2/3$ by strict convexity. Hence $(13/50)\log2>13/75$, and $(13/75)(5.78,40.4)>(1,7)$ componentwise. At $A\ge100+5.78x+40.4\log r$ the last expression is at most $6144\pi/2^{26}<0.000605$. Finally $\log(1+1/1650)>1/1651>0.000605$. Thus every even $n\ge r\max\{200,100+5.78x+40.4\log r\}$ suffices, including at the printed constants. The decimals in lines 173–175 are rounded. In the example at line 177, 2469 is the ceiling of the real threshold and 2470 the next even integer.

**Corollary WS2, (3.2) and its explicit (SEED-L) size, lines 180–198 — HOLDS.** Here $\Phi_L(N)=L^4 F(N^4)-F((LN)^4)$. For a cycle of $L$ slabs, replacing $K_a(C_i,C_{i+1})$ by $K_a(C_i,C_i)$ under the cyclic density gives $Z(a,B)^L/Z(La,B)$. The row terms cancel within each difference and the column terms sum to zero around the cycle. If $h$ bounds the anchored four-point remainder, the log integrand is at most $2Lh$. In direction $\mu=1,\dots,4$ the transverse volume is $L^{\mu-1}N^3$. The outer telescope weights the one-direction defects by $L^{4-\mu}$. Their coefficients in (3.2) are therefore $L^{4-\mu+1+2(\mu-1)}=L^{3+\mu}$. Nonnegativity follows direction by direction from $\sum_j(\lambda_j^N)^L\le(\sum_j\lambda_j^N)^L$ for the positive Wilson transfer. This proves the general bound with its floor, also for odd $N$.

For integer $L\ge25$, $\sum_{j=4}^7 L^j\le(25/24)L^7$. Set $A=N/r$ and use $\lfloor N/2\rfloor\ge(N-1)/2$, $r\ge3$. Then (3.2) gives

$$
 \Phi_L(N)/L \le 200\pi\,2^{1/6}\,\beta L^6 r^7\,2^{-13A/50}
 \quad (A\ge200).
$$

Now $(13/75)\,34.7>6$, and $49(13/50)-1/6>12+1/2$. Since $\pi<22/7$ and $\sqrt2>4/3$, $200\pi <0.131\,2^{12+1/2}$. It follows that the printed

$$
 N\ \ge\ 1+r\max\{200,\,49+34.7\log L+5.78x+40.4\log r\}
$$

suffices. At $L=25$, one can replace $49+34.7\log25$ by 161. The dependence on $\log\max(1,\beta)$ stays if the coupling varies. Both sizes meet the lower bounds on lattice periods needed by W(A).

## Lemma WS′ and Proposition RR

**Lemma WS′ and (4.1), lines 230–246 — HOLDS for Wilson SU(2), without (W).** The path and conditioning argument above only uses the middle-slice TV until the collar is introduced. For $a=3$ the middle is at 1 and the three top-plaquette entries are in the upper layer at 2. The same reasoning covers every $a\ge3$ and rectangular periodic $B$. For a spatial period one, count the Wilson plaquettes once per base site and coordinate plane. Two temporal sides can then be the same integration variable, but the changed *top* edge still occurs once. The $L^{4-\mu}$ telescope cancels the shape dependence of the coefficient $12\pi\beta L |B_\mu|$. Thus (4.1) bounds the **sum** of the four TVs by $0.131/(12\pi\beta L^3N^3)$. If imposing the same sufficient tolerance on each, use $0.131/(48\pi\beta L^3N^3)$.

**Proposition RR(i), (ii), (iii), lines 344–361 — HOLDS.** For $t=1$, which line 71 had left implicit, $K_1$ integrates the single layer of temporal links between the two boundary copies and includes both spatial half-weights. Identifying the copies gives the one-period partition function with the same plaquette multiplicities. Gluing these one-step kernels gives every $K_t$. For (i) the two-slice integrand $Q$ is a four-point ratio. To check the cyclic bound directly, subtract
$\log K(C_*,C_i)-\log K(C_*,C_{i+1})$ from each log ratio. The subtracted terms telescope to zero and each resulting summand is a four-point difference of modulus at most $\eta_*$. This even gives $L\eta_*$ and implies the printed $2L\eta_*$. Multiplication by $L^{4-\mu}$ gives exactly the four coefficients in line 351. Part (ii) is WS′, with its restriction $a\ge3$.

For (iii) the middle density is $K_t(D,z)K_t(z,E)/K_{2t}(D,E)$ against slice Haar measure. Put $q(z)=K_t(D',z)/K_t(D,z)$. Then $p_{D'}/p_D=q/\mathbb E_{p_D}q$, and $q(z)/q(z')\le e^{\eta_*}$ for every pair. Hence $p_{D'}/p_D\le e^{\eta_*}$ and the integral of its positive excess against $p_D$ is at most $e^{\eta_*}-1$. This implies the printed $e^{2\eta_*}-1$, with the thickness doubled and uniformly in $E$. The argument uses positivity of the kernel and normalization of the conditional density.

## From one cutoff to the continuum statement

**One-cutoff implication, lines 200–214, 241–246 and 260–267 — HOLDS with the base margin in line 261. The “one fixed coupling” wording at lines 22–26 and 45–48 FAILS in general.** Fix $g$, odd $L\ge25$ and a common compatible physical side $\ell$ with both account tori admitted. At the base cutoff the lattice side is $N=\ell L^{K_0}$ for *all* the required couplings. The lattice reindexing $L\ell/a_K=\ell/a_{K+1}$ preserves every bare plaquette and Haar factor, so $F_{K,L\ell,\beta}=F_{K+1,\ell,\beta}$ at fixed $\beta$ (outline 6844–6850, 6863–6869). The first-passage label of this datum is $K$. WS2 applies if its size condition is met at the common base side for each required coupling. Alternatively (4.1) or (6.1) supplies the base defect directly. Write $b_0=\sup_{d_0}\Phi(d_0)$ over the required base data. The precise sufficiency condition is

$$
 b_0+(L^4+1)\sum_{K>K_0}\epsilon_K\ \le\ \phi_*
 <\ c_L,\qquad c_L=\tfrac L2\log(13/10).
$$

The bounds $b_0\le0.131L$ from (4.1) and $b_0\le0.130L$ from (6.1) leave a positive, specified amount of room below $c_L$. Indeed $\log(13/10)/2>3/23+(3/23)^3/3>0.131$. Summability alone at an arbitrarily prescribed base supplies no bound on the size of its tail.

Rows 916–917 require a predecessor at each level, with the *same* $c_d$ on both tori in $F_d(T)-F_{\pi d}(T)=c_d\,{\rm vol}(T)+r_d(T)$, $|r_d(T)|\le\epsilon_K$. Subtracting the two volumes leaves $L^4 r_d(T_\ell)-r_d(T_{L\ell})$. Its telescope gives the displayed condition and covers every chain ending in the tested base set. Test the whole base window to include every datum at $K_0$, or just the reached bases for a conclusion at $K>K_0$. Only the chains of a selected sequence are needed for that sequence. Two disjoint abstract chains with constant defects $0$ and $2\phi_*>0$ and zero comparison errors show exactly why a test of one arbitrary base coupling cannot cover both. This is a counterexample to the quantifier inference. WS itself uses a single coupling in each application. [ONE-K and UNIV-K](gap-chain-ce-opus.md) · [Check 917](gap-chain-ce-check-astra.md)

**Lemma FL and the all-cutoff alternative, lines 205–207, 306 and 371–377 — HOLDS.** As in check 848, lines 150–202, insert $\phi_*<\phi'<c_L$ before using a uniform limsup. Put $s_0=e^{2\phi'/L}-1<3/10$, $s_k=(3.03s_0)^{6^k}/3.03$, and $E=(6L/(L-1))^3$. The seed comparison $g(N;(LN)^3)\le2\Phi_L(N)/L$ starts the ratio-$L$ shape recursion. FL gives $g(b_j/2;b_j^3)\le E\log(1+s_k)\le E s_k$ at $b_j=6^k L\ell/a_j$. Choose one $k$ with $E s_k\le1/6000$. Exponentiating gives $S\le1/5999<1/5041$, the full periodic (SEED-FP) at one physical side. For $\ell=2L^m$ the half-side is integral. If (6.1) itself holds at that common initial $\ell$ for all sufficiently fine required data, the initial limsup is already at most $0.130L$. This proves the direct route without (UNIV-K), for the data covered by that uniform hypothesis.

**Passage through Theorem E-N, lines 207 and 382 — HOLDS AFTER CORRECTION of the omitted aspect change and of the scope of “gap clause”.** Theorem E of rows 916–917 already takes the full half-side seed directly. Theorem E-N of rows 1225–1232 instead takes a *short-time neutral trace*. A half-side upper bound alone on the same cube does not give an upper bound at its $1/512$-time. Row 1161, line 150, gives the needed side enlargement. Choose the FL index $k$ sufficiently large that also $512^3 E s_k\le\log(3/2)$. Set

$$
 u_j=b_j/2,\qquad n_j=256b_j,\qquad P=n_ja_j=256\cdot6^k L\ell.
$$

Shape bound B3 (row 705, lines 74–85) at $p=q=1$ gives

$$
 \log(1+S(u_j;n_j^3))
 \le (n_j/(b_j-u_j))^3\log(1+S(u_j;b_j^3))
 \le 512^3 E s_k .
$$

The unique periodic positive vacuum is invariant under the commuting centre flips. Restricting the excited trace to their neutral subspace can only decrease it. Thus $s_+(u_j;n_j^3)\le1/2$, $3\le u_j=n_j/512$ eventually, $4\mid n_j$, and $n_j\ge2^{70}$ eventually. This is the explicit-aspect (N-phys) of check 1232, lines 51–58, on the single enlarged physical side $P$.

Under E-N's member and account hypotheses, for each covered volume-first limit $S$,

$$
 \ker H=\mathbb C\Omega,\qquad
 {\rm spec}(H|_{\Omega^\perp})\subset[M,\infty),\qquad
 M=\frac{2}{P}\log\frac{2^{18}}{5041}>0
 \quad\text{on }\mathcal H(S).
$$

Indeed the centred plaquette products are invariant under site-centre signs. Member positivity and contraction are those of the restricted lattice space. The matched reflected pairings pass the common bound $\langle v,e^{-tH}v\rangle\le e^{-Mt}\|v\|^2$ to the dense vacuum-subtracted tuple class. A vector with positive spectral weight below $M-\varepsilon$ would violate that bound at large times. Totality excludes this spectral weight on the whole vacuum complement. This is the account's scalar curvature sector with volume taken first. Existence, nontriviality and identification with the full observable theory retain their separate premises. [Check 848](gap-e17phys-check-astra.md) · [Check 1232](gap-en-check-astra.md)

## ARGUED readings and GUIDE examples

**Interpretation at lines 346–347, 363–369 — HOLDS AFTER CORRECTION if read as a two-way statement at the same tolerance.** The condition (RR) is defined by the four-point bound. Anchoring at one fixed row and column gives product approximation with log error $h$. Conversely a log error bounded by $h$ gives a four-point bound $4h$. The matrix with diagonal entries $e^h$ and off-diagonal entries $e^{-h}$ is within log error $h$ of the constant product and has cross-ratio log $4h$. SL and RR imply the *two inequalities* (ii) and (iii), with their sizes and thicknesses as written. The diagonal periodic average has an upper bound by that supremum. The kernel is quantitatively close to a product when the four-point bound is small. Equation (6.1) gives $\Phi_L\le0.130L$ directly.

**Compact-fibre aside, lines 49–50 and 149–151 — HOLDS AFTER CORRECTION.** The derivative proof needs paths of controlled length and the oscillation of the plaquette score, bounded by twice its supremum norm. Even the proposed per-link constant $J\,{\rm diam}$ can fail for a two-point fibre. Take distance one and a temporal plaquette weight depending only on its two spatial edges, with matrix $T=\left(\begin{smallmatrix}1&z\\z&1\end{smallmatrix}\right)$, $0<z<1/64$, and constant spatial weights. Each spatial link gives an independent time chain. The per-link log weight has Lipschitz constant $J=\log(1/z)$. At thickness four, $(T^4)_{11}\ge1$ and $(T^4)_{12}=4z(1+z^2)<8z$. The one-link cross-ratio log exceeds $2\log(1/(8z))>J$, while every TV is at most one. This refutes the claimed per-link substitution at line 150. An endpoint proof works there and on arbitrary compact metric fibres in the same plaquette geometry. If changing one boundary link changes the log weight of its temporal plaquette by at most $Jd$, the multiplier $Y$ lies between $e^{-Jd}$ and $e^{Jd}$. The log of its expectation changes between bottoms by at most $(e^{2Jd}-1)\tau_*$, by the TV bound and the lower bound on the expectation. Thus one can keep the finite-slab implication with a different constant. The spectral interpretation and four-axis application also need the transfer and axis-symmetry premises used above.

**Physical size, lines 178 and 216–226 — the logarithmic loss in this sufficient bound HOLDS. The inference “of order $\xi\log\xi$” at line 178 FAILS.** Row 691, Proposition B, gives $r\ge(\log(1/\delta)/2)\xi_{\rm lat}$. It gives no upper comparison. For example $r=\lceil\xi_{\rm lat}^2\rceil+2$ satisfies that numerical inequality for large $\xi_{\rm lat}$, while $r\log r/(\xi_{\rm lat}\log\xi_{\rm lat})$ is unbounded. This refutes the inference from Proposition B, without asserting a Wilson scaling law. For fixed $\beta$ the displayed WS1 certificate has order $r\log r$ as $r$ grows. With spacing $a_j$, it costs order $a_j r_j[1+\log r_j+\log^+\beta_j]$. If $a_j\xi_j$ stays bounded below by a positive length, this certificate incurs at least a logarithm as $a_j\downarrow0$. An upper comparison to $\xi_{\rm phys}\log(\xi_{\rm phys}/a_j)$ needs corresponding upper control of $r_j/\xi_j$ and of the coupling term. The assumption $a_jR_j\le \ell$ alone does not force divergence. The first true seed can lie below the size certified by (2.3). The two factors of $V$ in that bound come from the score and the collar. Retaining even one factor $V$ in this estimate retains a logarithm when it is inverted.

**Choice of $K_0,\ell$, lines 260–267 — HOLDS AFTER CORRECTION as conditional scale arithmetic.** For example, suppose the error of the *full unnormalized two-torus comparison* is at most $C L^4\ell^4 q^K$, $0<q<1$, on the required chains, uniformly in the sizes being chosen. Then $E(K_0)\le C L^4\ell^4 q^{K_0+1}/(1-q)$. For fixed $L$ and base margin one can take $K_0$ of order $\log\ell$ with a sufficiently large coefficient. An estimate on the regular part alone leaves the vacuum factors, histories and admission of the compared profiles open (917, lines 340–372). Independently, suppose $\tau_\mu\le C_s |B_\mu|e^{-N/(2\xi_K)}$ uniformly in the base data. Inserting the four volumes into (4.1) gives the sufficient inequality

$$
 \frac{\ell}{2a_K\xi_K}\ \ge
 6\log(\ell L^K)+6\log L+\log\beta+O(1).
$$

The constant depends on the target margin and $C_s$. The $\log\beta$ term was omitted at line 264. On the stated first-passage flow $x_0=\beta,\ b_i\le B_\sharp,\ x_K\le g^{-2}+B_\sharp$, hence $\beta\le g^{-2}+(K+1)B_\sharp$ (outline 6854–6861). With a common upper bound on $a_K\xi_K$, the right side grows only logarithmically in $\ell$ at the proposed $K_0$. Thus the two *assumed* rates can be compatible on large admissible sides. Neither rate has been obtained for this application.

**Weak-coupling preference, lines 248–258, 336–340 and 378–380 — HOLDS as a choice of sufficient hypothesis. Its proposed Wilson mechanism is GUIDE only.** Formally summing $r^3\min(1,\sqrt\beta/r^2)$ up to $\xi$ gives order $\sqrt\beta\,\xi^2$ in the stated range. There is no derivation of that disagreement profile. In particular, if lines 251–252 describe a one-link *marginal* in a cube with fixed exterior, that reading FAILS. A gauge transformation at one endpoint of a deep interior link preserves the exterior and multiplies the link by an arbitrary group element. Its marginal is exactly Haar under either choice of exterior. A conditional distribution with every other link frozen is a different object, and its width would not establish a Hamming coupling of the whole block. Likewise a spectral gap in one state gives no uniform per-boundary TV estimate here. A few tens of correlation lengths and the proposed physical-cell size of $\eta_*$ are expectations, without proved constants.

**Uniform versus periodic control, lines 152–153, 269–287 and 363–380 — HOLDS as a distinction.** An elementary example makes the lost information explicit. Take the two-state transfer $T=\left(\begin{smallmatrix}1&e\\e&r\end{smallmatrix}\right)$, $0<r<1,\ 0<e<\sqrt r$, at thickness $2t$, $t\ge2$. As $e\downarrow0$, $\Phi(2t)\to\log[(1+r^{2t})^2/(1+r^{4t})]\le2r^{2t}$. Fix the second state at the top. With that state also at the bottom the middle is in it with probability tending to 1. With the first state at the bottom its probability is $(T^t)_{22}/[(T^t)_{11}+(T^t)_{22}]\to r^t/(1+r^t)$. Thus $\tau_*$ can be near one with an arbitrarily small periodic defect, even for positive definite transfers. Row 975's META gives an obstruction from a set with a large *conditional return probability*. A rare boundary history alone need not have that property. The use of (W) at line 153 excludes a large periodic defect only once the WS bound is small. The Ising droplet scale and the expectation about the Wilson vacuum remain heuristic here. The Ising-cylinder numerics were not rerun.

**Comparisons, lines 27–34, 200–214 and 309–329 — HOLDS with the stated quantities.** The earlier Dobrushin argument in `gap-vmf-lip.md` §4 actually bounds the plaquette-mean difference along the integration interval. The identity in row 913 by itself only demands control of a signed integral, and admits cancellation between intermediate couplings. In row 1218's reading, Bhattacharjee and coauthors' (A-M) tests outer-region maximal correlation, (A-B*) tests the periodic thermal trace and (B-D) tests Wasserstein influence in a forest gauge. Row 1007's reading of OpenAI's two-dimensional $O(3)$ Proposition 2.1(ii) gives a polynomial times an exponential on bounded-aspect rectangles, uniformly for bounded bond strengths. These comparisons supply no four-dimensional Wilson slab estimate. Claude Fable 5.2 supplied W and SH, with checks by Claude Opus 5.5. Row 691 credits Dobrushin and Shlosman for the form of (W). Claude Opus 5.5 gives the swap and middle-slice argument in row 1258. [Row 1218's reading](prior/gap-onebound-read-sol.md) · [Row 1007's reading](prior/gap-2don-proofs-read-opus.md)

RESULT: Row 1265. WS given W(A), both printed seed sizes, WS′ and RR(i)–(iii) HOLD. The route through E-N HOLDS AFTER CORRECTION with the reached base couplings, the full (UNIV-K) tail margin and the enlarged neutral-test cube. The two-sided correlation-length inference FAILS. The weak-coupling slab estimate, (UNIV-K), the account premises and the four-dimensional mass gap remain open.
