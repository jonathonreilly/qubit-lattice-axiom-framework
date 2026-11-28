# Check of row 1714: gap-largen-loopeq-build-astra62.md

lead: anthropic/claude-opus-5-5 laptop subagent

Started Sat Nov 28 18:27:30 UTC 2026. Checked by Claude Opus 5.5; author of the checked file gpt-6.2-astra max.

FINISH row 1725. Cross-provider check.

## Plan

1. Read the checked file in full.
2. Check each item line by line: Lemma 1, Lemma 2, contraction, range and boundary, master equation and uniqueness, connected loops and volume limit, coefficient 144 b^2 + 32 b^2 < 1/2, b = 1 counterexample, U(1) and dimension remarks, SU(2) specialisation, coupling table.
3. Use small exact computations (python3 -I, fractions or sympy) as guides only.
4. Give a verdict and a label per item. End with a RESULT line.

## Progress

- Read the checked file in full (267 lines, at the lane folder as of this check).
- Ran exact guides in the scratchpad: `chk1725.py` (fractions: rectangle constants, coefficients, entropy constants, SU(2) numbers) and `lie_guide.py` (floats, guide only: su(N) identities for N = 3, 4). No sympy on this machine; the integrals were done by hand and the results checked with fractions.

## Conventions used in this check

Action $Nb\sum_p{\rm ReTr}\,U_p$, one orientation per square. $D=2(d-1)=6$. Metric $|X|^2=-{\rm Tr}X^2$. $c=N-1/N$, $r=N/c$, $k=4\sqrt{D/3}$. I keep the file's notation.

## Item 1. Lemma 1 (the SU(N) trace correction)

**1a. Centre rotation and Jensen. HOLDS. PROVED.** $e^{i\theta}I\in SU(N)$ for $\theta=2\pi/N$. The density ratio $\rho(e^{i\theta}Q)/\rho(Q)=\exp(Nb[(\cos\theta-1){\rm ReTr}(QH)-\sin\theta\,{\rm ImTr}(QH)])$ has $E_h$-mean one by Haar invariance. Jensen gives $E_h[\log(\text{ratio})]\le 0$. With $\pm\theta$ this is $\pm\sin\theta\,E_hY\le(1-\cos\theta)E_h{\rm Re\,tr}(QH)$. Since $(1-\cos\theta)/\sin\theta=\tan(\pi/N)$ and $|{\rm Re\,tr}(QH)|\le D$, $|E_hY|\le D\tan(\pi/N)$. $N\ge3$ gives $\sin\theta>0$.

**1b. Ricci $N/2$ in the unscaled HS metric. HOLDS. PROVED.** For $X=i\,{\rm diag}(x_j)$, each real off-diagonal unit vector at $(j,k)$ gives $|[X,T]|^2=(x_j-x_k)^2$. The sum is $2\sum_{j<k}(x_j-x_k)^2=2N\sum x_j^2$ when $\sum x_j=0$. One quarter of that is $(N/2)|X|^2$. Float guide for N = 3, 4: ratio 1.000. Second derivative of ${\rm ReTr}(e^{tX}QH)$ is ${\rm ReTr}(X^2e^{tX}QH)$, bounded by ${\rm Tr}(-X^2)\|H\|_{\rm op}\le D|X|^2$. Right translates of one-parameter subgroups are geodesics, so this is the Hessian. Hence ${\rm Ric}-{\rm Hess}\,S_h\ge N/2-NbD=N\delta$. The multipliers $s_p\in[0,1]$ and fixed exterior links keep $\|H\|_{\rm op}\le D$.

**1c. Bochner and Lipschitz steps. HOLDS. PROVED (standard Bakry–Emery; could be CITED).** The sign of the drift term is right for the law $e^{S}dU$. The pointwise gradient bound $|\nabla P_tf|\le e^{-\kappa t}P_t|\nabla f|$ is the standard consequence; the file states only the Lipschitz form, which is what it uses. ${\rm Var}_hF=2\int_0^\infty E_h|\nabla P_tF|^2dt\le{\rm Lip}(F)^2/\kappa$. ${\rm Lip}(Y)$: $|N^{-1}{\rm Im\,Tr}(XQH)|\le N^{-1}|X|\,|QH|_{\rm HS}\le D|X|/\sqrt N$. Then $E_h|Y|\le D\tan(\pi/N)+D/\sqrt{N\cdot N\delta}=m_N$. This matches the definition of $m_N$ exactly.

**1d. Covariance formula and (1). HOLDS. PROVED.** ${\rm Cov}_h(F,G)=\int_0^\infty E_h\langle\nabla P_tF,\nabla G\rangle dt$ follows from $F-E_hF=-\int_0^\infty L_hP_tF\,dt$ and integration by parts. With $G=|v|^2$, $|\nabla|v|^2|\le2|v||\nabla v|$ (Kato), and ${\rm Lip}(P_t|Y|)\le e^{-N\delta t}D/\sqrt N$, the covariance is at most $\frac{2D}{N^{3/2}\delta}E_h|v||\nabla_hv|$. Adding $E_h|Y|\,E_h|v|^2\le m_NE_h|v|^2$ gives (1) with the stated constant. The smoothing $F=(Y^2+\epsilon^2)^{1/2}$ is fine.

## Item 2. Lemma 2 (the plaquette Hessian in the quadratic form)

**2a. The 16 trace terms and $|C(V,W)|\le|V||W|$. HOLDS. PROVED.** The product curve $(e^{tA_e}Q_e)_e$ with frozen $A$ is a product geodesic, so its second derivative is ${\rm Hess}\,S(\alpha,\alpha)$ at that point. Inverse links give $-A_e$ after $Q_e^{-1}$; the square of $-A_e$ is $A_e^2$. Cyclicity and HS Cauchy–Schwarz give the bound, also for $e=f$.

**2b. Formula (3). HOLDS. PROVED.** For $h\notin\{e,f\}$ the trace is real-linear in $Q_h$ (each link occurs once in a simple square; periodic side at least 5 makes this true). Exact check of $-\sum_aT_a^2=cI$: trace $N^2-1$ and conjugation invariance; float guide for N = 3, 4 agrees. Write $c\,C=-\sum_aC_{aa}=-\sum_aX_a[C_a(A_e,A_f)]+\sum_a[C_a(X_aA_e,A_f)+C_a(A_e,X_aA_f)]$, then integrate $X_a$ by parts against $e^S\,dU$ (right-invariant fields are Haar divergence free). This gives (3) with the signs shown.

**2c. Differentiated slots. HOLDS. PROVED.** The partner of $X_aA_e$ is $U_1T_aU_2A_fU_3$ (or $A_f$ before $T_a$). $\sum_a|\cdot|^2=c|A_f|^2$ in either order. Cauchy–Schwarz over $a$ gives $\sqrt c\,|\nabla_hA_e|u_f$.

**2d. Score. HOLDS. PROVED.** $X_aS=Nb\,{\rm ReTr}(T_aM)$ with $M=Q_hH$. So $\sum_a(X_aS)T_a=-Nb[{\rm skew}(M)-i\,{\rm Im\,tr}(M)I]$, the traceless projection of $-Nb\,{\rm skew}(M)$. Operator norm at most $Nb(D+|Y_h|)$. One operator-norm slot and two HS slots give $Nb(D+|Y_h|)u_eu_f$.

**2e. Weights and counts. HOLDS. PROVED.** With $t=s_p/(4-|\{e,f\}|)$: for fixed $(p,e)$, $f=e$ gives $3\cdot\frac13=1$ and the three $f\ne e$ give $3\cdot2\cdot\frac12=3$. Total 4 per $(p,e)$, at most $D$ squares per edge: $4DA^2$. For fixed distinct $(e,h)$ there is at most one common square; $f=e$ gives $\frac13$, the two other $f$ give $\frac12$ each: $\frac43$. So each differentiated sum is at most $\sqrt{4/3}\,B\sqrt{4D}\,A=kAB$. The $|Y_h|$ count: apply (1) at $h$ with $v=A_e$ (a fixed-space vector function of $Q_h$, since $e\ne h$), and the same for $A_f$; average the two. This gives the displayed $4Dm_NA^2+\frac{2Dk}{N^{3/2}\delta}AB$.

**2f. Assembly into (2). HOLDS. PROVED.** I redid the algebra. $(Nb/c)\cdot Nb\cdot4D(D+m_N)=N\cdot4Db^2r(D+m_N)$. $(Nb/c)\cdot2\sqrt c\,k=2\sqrt N\,bk\sqrt r$. $(Nb/c)\cdot Nb\cdot\frac{2Dk}{N^{3/2}\delta}=2\sqrt N\,bk\cdot\frac{bDr}{N\delta}$. These are the three terms of (2).

Note (not an error): the pointwise version of the same count, $|{\rm Hess}\,S|\le4DNb$, against Ricci $N/2$ gives $b<1/(8D)=1/48$. This is the Shen–Zhu–Zhu window quoted in the table, so the table's SZZ number is internally consistent with the file's own constants. The gain of Lemma 2 is that the Hessian enters at order $b^2$, not $b$.

## Item 3. The contraction with finite propagation

**3a. $\|K\|\le q$ and $H_1\ge N\eta$. HOLDS. PROVED.** With $x=\sqrt{N/2}A$, $y=B$: $NvA^2+2\sqrt NuAB=2vx^2+2\sqrt2\,uxy$. The matrix $\begin{pmatrix}2v&\sqrt2u\\\sqrt2u&0\end{pmatrix}$ has top eigenvalue $q=v+\sqrt{v^2+2u^2}$; the entries are nonnegative, so the bound for $x,y\ge0$ is the top eigenvalue. $q<1\iff2u^2<1-2v\iff\eta>0$. Completing the square, $2\sqrt NuAB\le B^2+Nu^2A^2$, gives $H_1\ge N\eta$.

**3b. Intertwining $d(-L)=H_1d$ and (6). HOLDS. PROVED (standard Witten Laplacian on one-forms).** For the law $e^{-V}$ the one-form operator is $\nabla^*_\mu\nabla+{\rm Ric}+{\rm Hess}V$; here $V=-S$, so the minus sign in (5) is right. Ricci of the product is $N/2$ per factor. $H_1=H_0^{1/2}(I-K)H_0^{1/2}$ gives (6).

**3c. Edge-index propagation and (7). HOLDS. PROVED.** The product connection preserves each edge subbundle, and $\nabla^*_\mu$ contracts only the derivative index. So $H_0$ commutes with each edge projection, and so does $H_0^{-1/2}$. The $(e,h)$ block of ${\rm Hess}\,S$ vanishes unless $e,h$ share a square. So the degree-$j$ term in the Neumann series pairs to zero with $df$ when $j<R$. $\|H_0^{-1/2}\|^2\le2/N$ and $\sum_{j\ge R}q^j=q^R/(1-q)$ give (7). The constant is exact.

## Item 4. Range and boundary

**4a. Range (8). HOLDS. PROVED.** As $N\to\infty$: $r\to1$, $m_N\to0$, $bDr/(N\delta)\to0$. So $v\to4D^2b^2=144b^2$, $u^2\to k^2b^2=\frac{16D}3b^2=32b^2$, $\eta\to\frac12-176b^2$. $352=16\cdot22$, so $b_*=1/(4\sqrt{22})\approx0.0533$. There $6b_*\approx0.320<\frac12$, so $\delta>0$. Monotonicity in $b$ and in $N$ holds term by term ($r$, $\tan(\pi/N)$, $1/(N\sqrt\delta)$, $bDr/(N\delta)$ all decrease in $N$; all losses increase in $b$). So the first $N$ with $\eta_N(b_0)>0$ works for all larger $N$ and all $b\le b_0$.

**4b. The explicit rectangle $N\ge1024$, $b\le1/20$. HOLDS. PROVED (exact fractions at the worst corner).** Results of `chk1725.py`: $\delta=1/5$; $r<1001/1000$; $m_N\le6\cdot11/1024=33/512<1/12$; $bDr/(N\delta)\approx0.00146<1/500$; $v<0.3639<11/30$; $u^2<0.0803<13/160$ (using $\sqrt r\le r$); $\eta>\frac12-\frac{11}{30}-\frac{13}{160}=\frac5{96}>\frac1{20}$; $(11/12)^2-2\cdot\frac{11}{30}\cdot\frac{11}{12}-2\cdot\frac{13}{160}=\frac1{180}$ exactly. The root $q$ decreases when $v,u$ decrease, so $q<11/12$. Note: $v<11/30$ has small slack (0.3639 against 0.3667).

**4c. Fixed exterior links. HOLDS. PROVED.** For a coordinate box, a square through an active edge has its other two vertices both inside or both outside, since they share the transverse coordinate. So it has four active edges or one. Count with full squares: $\sum_e4d_eEu_e^2=4DA_i^2$. The $\frac43B^2$ count is unchanged. The score at $h$ still uses all squares at $h$, with $\|H\|_{\rm op}\le D$, so (1) still applies. Boundary squares give a diagonal Hessian bounded by $Nb\,u_e^2$, at most $D-d_e$ of them: total $NbDA_o^2$. In the block variables the ratio is at most $\max(q,2bD)$ and $H_1/N\ge\min(\eta,\delta)$. On the rectangle $2bD=3/5$ and $\delta\ge1/5$, so $\bar q\le11/12$, $\bar\eta\ge1/20$.

## Item 5. The finite-rank master equation and its uniqueness class

**5a. Coefficient identity and $L\mathcal W\subset\mathcal W$. HOLDS. PROVED.** $\sum_a(T_a)_{ij}(T_a)_{kl}=-\delta_{il}\delta_{jk}+N^{-1}\delta_{ij}\delta_{kl}$: the U(N) completeness relation minus the $iI/\sqrt N$ component. Float guide for N = 3, 4 agrees to $2\cdot10^{-16}$. $S$, $\Delta S$ and $|dS|^2$ are loop polynomials, so $LF\in\mathcal W$.

**5b. (9). HOLDS. PROVED.** $dP_tF=e^{-tH_1/N}dF$ from 3b, and $H_1/N\ge\eta$.

**5c. $P_tJ\subset J$ and $C^2$ approximants. HOLDS. PROVED.** The Haar Laplacian keeps total length, so the span $V_m$ of loop products of length at most $m$ is a finite-dimensional invariant subspace of a self-adjoint operator, hence reducing. Ground-state conjugation: I recomputed $e^{S/2}(-L)e^{-S/2}=-\Delta+\frac12\Delta S+\frac14|dS|^2$; the sign in the file is right. The bounded potential and $e^{\pm S/2}$ preserve $J$; the Dyson series preserves $J$. The spectral cutoff $\mathbf 1_{[0,M]}(-\Delta)$ maps loop polynomials to loop polynomials, has finite-dimensional range, so the image of $J$ lies in the image of the loop polynomials. Sobolev tails go to zero for smooth $F$. All steps are correct.

**5d. Uniqueness. HOLDS AFTER CORRECTION. PROVED.** The argument is correct: $\nu(LP_tF)=0$ by the $C^2$ approximants and uniform continuity of $\nu$; so $\nu(P_tF)=\nu(F)$; $P_tF\to\mu F$ uniformly; $\nu(1)=1$. **Correction.** Nothing in this argument uses $b<b_*$ or large $N$. In a finite box the generator has a positive gap for every $b\ge0$ and every $N\ge2$ (compact connected product, smooth positive density). So finite-volume uniqueness in this class holds at all couplings and ranks. The Result paragraph ("for all sufficiently large finite N ... has a unique normalized solution") ties uniqueness to the range; it should say that uniqueness holds for all $b,N$ in finite volume and that the range and rank condition give only the volume-uniform rate (9) and the decay (7), (10). Also, since the class contains all finite-rank trace identities, this uniqueness is the uniqueness of the stationary law of $L$ on $\mathcal W$; it is not progress on its own (brief: "Equivalent is not progress"). No uniqueness for the $N=\infty$ (limiting) master equation is proved; the brief allowed either, and the file states the finite-rank form, so this is not an error.

**5e. Dual-norm contraction. HOLDS. PROVED.** $|(\nu-\nu')(P_1F)|\le\|\nu-\nu'\|_*e^{-\eta}\|F\|_\nabla$. It is meaningful only for non-solutions, since all solutions equal $\mu$.

## Item 6. Connected loops and the volume limit

**6a. $\|dW_\ell\|_\infty\le|\ell|/\sqrt N$ and (10). HOLDS. PROVED.** The $T_a$ are a complex orthonormal basis of the traceless matrices, so Bessel gives $\sum_a|N^{-1}{\rm Tr}(T_aV)|^2\le|V|_{\rm HS}^2/N^2=1/N$. The triangle inequality over visits and $\sum_en_e^2\le|\ell|^2$ give the bound. Then $N^2\cdot\frac2{N(1-q)}\cdot\frac{|\ell||\ell'|}N=\frac{2|\ell||\ell'|}{1-q}=24|\ell||\ell'|$ at $q=11/12$. Exact.

**6b. Volume limit (11) and Gibbs uniqueness. HOLDS. PROVED.** The gradient of $Nb\,{\rm ReTr}(Q_eV)$ has norm at most $Nb\sqrt N$ (Bessel). Each boundary square sits at graph distance at least $R$ from the support. The bound (7) with $\bar q$ holds uniformly in $t\in[0,1]$ and the exterior field (item 4c). $|\partial P|=O(L^{d-1})$ against $\bar q^{cL}$ goes to zero. For a Wilson product the prefactor is $2b|\ell|/(1-\bar q)$, uniform in $N$. The Gibbs-uniqueness argument (condition two Gibbs laws on the outside of the same cube) is the standard one and is correct.

**6c. Nonzero local variance (12). HOLDS. PROVED.** I checked each constant. $c\,\mu W_p=\mu\sum_a(X_aS)X_aW_p$ holds since $\Delta_eW_p=-cW_p$ at a single visit. $|\mu W_p|\le br(D+m_N)<0.304<1/3$ (exact fractions). The single-visit identity $\sum_a|X_aW_p|^2=(1-|W_p|^2)/N$ is the exact traceless projection. Poincare with gap $N\eta$: ${\rm Var}\le4/(N^2\eta)$. So $E|W_p|^2<1/9+80/1024^2<1/4$ and $\|dW_p\|_2^2>3/N$. Hessian blocks: Bessel in $a$, then $N^2-1$ values of $b$: $(N^2-1)/N^2\le1$; the same-link block is a symmetrised average, so the triangle inequality gives the same bound. $\langle dW,H_0dW\rangle\le16+2$, $H_1\le(1+\bar q)H_0$, $(23/12)\cdot18=34.5\le36$. Then ${\rm Var}\ge(3/N)^2/36=1/(4N^2)$.

**6d. Transfer-matrix remark (rate $\log(12/11)$ as an energy bound). HOLDS AFTER CORRECTION. Label should be ARGUED, not PROVED.** The step needs reflection positivity of the Wilson action and a transfer representation (CITED: Osterwalder–Seiler; the file names no theorem). It also needs the identification of "the centered Wilson sector" with the cyclic subspace generated by the Wilson observables used in (10). These are standard but not proved in the file.

## Item 7. The coefficient $144b^2+32b^2<1/2$ and the claimed range

**HOLDS. PROVED.** $4D^2=144$ and $k^2=16D/3=32$ at $D=6$. Sum 176. $176b^2<1/2\iff b<1/\sqrt{352}=1/(4\sqrt{22})$. Dimension table: $D=4$ gives $64+64/3=256/3$; $D=6$ gives $176$; $D=8$ gives $256+128/3=896/3$. All three match. The claim that $6b<1/2$ has slack at $b_*$ holds ($0.320$).

Consistency check (mine, not in the file): the lower bound of item 8a gives $\|K\|\ge bD|p_b|$. At small $b$ and large $N$, $p_b\approx b$, so the lower bound is about $6b^2$, below the upper bound $\approx176b^2$. No contradiction.

## Item 8. The $b=1$ entropy trial-law counterexample

**8a. $\|K\|\ge bD|p_b|$. HOLDS. PROVED.** For a right-frame-constant one-form $X$ at one edge, $|X|=1$: connection energy $\frac14\sum_a|[T_a,X]|^2=N/2$ (the Ricci sum), plus $N/2$, so the $H_0$ form is $N$. The expected Hessian is $Nb\sum_{p\ni e}{\rm Re\,Tr}(X^2E[U_p^{(x)}])$, and vertex gauge invariance makes $E[U_p^{(x)}]$ scalar with real part $p_b$. So it equals $-NbDp_b$. Reality of $E\,{\rm tr}U_p$ is not needed, since only the real part enters.

**8b. Convexity. HOLDS. PROVED.** $(\log Z)'(b)=N^2|P|p_b$, $\log Z(0)=0$, convexity gives $\log Z(b)\le bN^2|P|p_b$. $|P|=6V$ in 4D.

**8c. Trial law entropy $h_N$. HOLDS. PROVED.** Weyl integration: the randomly labelled Haar U(N) angles have density $\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2/N!$ relative to iid uniform angles. The trial angles have density $(\pi/a)^N$ on the arc. Both U-laws are pushforwards of (angle law) times (Haar conjugation) by the same map, so data processing gives ${\rm Ent}\le\log N!+N\log(\pi/a)+N(N-1)I_a$. The map $U\mapsto e^{-i\arg\det U/N}U$ is left-SU(N)-equivariant, so it pushes Haar U(N) to Haar SU(N). The bound on $h_N$ is right. $|z_N-t|\le\pi/N$ since $|\arg\det U|\le\pi$.

**8d. Constants. HOLDS. PROVED (recomputed).** $\int_0^12(1-s)\log s\,ds=2(-1+\frac14)=-\frac32$, so $E\log|\theta-\phi|=\log(2a)-\frac32$. $E(\theta-\phi)^2=2a^2/3=32/75$. $\log(\sin x/x)\ge-x^2/5$ on $[0,1]$: $\sin x\ge x-x^3/6$ and $-\log(1-y)\le y/(1-y)\le\frac65y$ for $y\le\frac16$. Here $x=|\theta-\phi|/2\le a<1$. So $I_a\le\frac32-\log\frac85+\frac{a^2}{30}$, and $a^2/30=8/375$ exactly. With $\log\frac85\ge\frac{6}{13}$: $I_a\le\frac{10333}{9750}\approx1.0598<\frac{16}{15}$. $t\ge1-a^2/6=67/75$; $(67/75)^2>19/24$; $(67/75)^4>5/8$. All exact.

**8e. Gauge fixing and the trial integral. HOLDS. PROVED.** Temporal links off one seam form a forest of $(1-1/L)V$ links; the remaining $(3+1/L)V$ links get iid $\tau_N$. Spatial squares: $3V$, mean $|z_N|^4$. Off-seam temporal squares: $3V(1-1/L)$, mean $|z_N|^2$. Seam squares: four distinct independent links, mean $|z_N|^4\ge0$. Gibbs variational inequality, divide by $N^2\cdot6V$: the display is right, with entropy weight $(3+1/L)/6=\frac12+\frac1{6L}$. Limit: $\frac12(t^4+t^2-I_a)>\frac12(\frac58+\frac{19}{24}-\frac{16}{15})=\frac12\cdot\frac{7}{20}=\frac7{40}$. Then $\liminf\|K\|\ge6\cdot\frac7{40}=\frac{21}{20}$; the strict inequality holds since the bounds are strict. Exact.

**8f. Scope. HOLDS.** The file states the scope correctly: the test direction has a negative Hessian, so it pushes $K$ below $-1$ and does not threaten $H_1>0$. It refutes only the Neumann-series route on the full one-form space. The damped series $(48I+K)/49$ needs only an upper-edge bound $K\le1-\epsilon$; $\|K\|\le8Db=48$ at $b=1$ is right. The GUESSED label on a gap at $b=1$ is right.

## Item 9. U(1) and dimension remarks

**9a. U(1). HOLDS. PROVED (elementary).** Charge-$j$ derivative $|j|$, Laplacian eigenvalue $j^2$, Ricci zero, parallel form $d\theta$ in the kernel of the Haar $H_0$: all correct. Mean zero and variance one for $e^{ij\theta_p}$ under Haar: correct. Comment: the same flat direction (the centre $\mathfrak u(1)$) is present in U(N). So the method as written does not cover U(N), and the U(N) rows of the table are not like-for-like comparisons. The file does not claim U(N), so this is not an error.

**9b. Dimension. HOLDS. PROVED.** $D=2(d-1)$ enters through the staple norm, the $4D$ count and $k$. The "at most one common square" count holds in every $d$. No running coupling is used.

## Item 10. SU(2) specialisation

**HOLDS AFTER CORRECTION. PROVED.** $Y_h=0$ for every SU(2) staple, also with multipliers and fixed SU(2) exterior links, since each ${\rm Tr}(Q_hV_p)$ is real. $c=3/2$, $r=4/3$. Exact: $4D^2r+\frac{16D}3r=192+\frac{128}3=\frac{704}3$, so $\eta=\frac12-\frac{704}3b^2$ and $b<\sqrt{3/1408}\approx0.0462$; also $\delta>0$ there. The card's action $\beta(1-{\rm Tr}U_p/2)$ equals a constant minus $\frac\beta2{\rm Tr}U_p$, and $Nb\,{\rm ReTr}=2b\,{\rm Tr}$, so $\beta=4b$. $16\cdot3/1408=3/88$, so $\beta<\sqrt{3/88}\approx0.185$.

**Correction.** Lemmas 1 and 2 are stated for $N\ge3$. For $N=2$ Lemma 1 is not needed (since $Y=0$), and Lemma 2 holds with $m_N=0$ and without the derivative cost from (1). The file says this in words; the lemma statement should include $N=2$ with these changes.

**Comment (not an error).** The SU(2) interval $\beta<0.185$ is below the in-lane Theorem A interval $\beta<1/4$ of `gap-mixed-opus.md` §3 (an invariant Langevin gap, a different conclusion). The file says Theorem A exists; it should also say that its own interval is smaller, so that the gain is only the form of the conclusion (direct spatial covariance decay), not the range. Against the pointwise Bakry–Emery bound for SU(2) ($b<1/48$, $\beta<1/12$) it is an improvement.

## Item 11. Coupling-comparison table (no web access; internal consistency only)

| Row | Internal check | Needs a source check |
|---|---|---|
| SZZ, $|b|<1/48$ | Consistent: pointwise $|{\rm Hess}\,S|\le4DNb=8(d-1)Nb$ against Ricci $N/2$ gives $b<1/(16(d-1))=1/48$. | That SZZ sum over one orientation per square (else their $\beta$ is $b/2$); the theorem and corollary numbers; that Cor 1.5/1.6 are the large-rank and covariance statements. |
| Nissim, U(N), $\widetilde b(4)\le10^{-24}$ | Arithmetic $10^{-6d}=10^{-24}$ is right. | Theorem numbers, the formula for $\widetilde b(d)$, and its location before Prop 3.20. U(N), so not like-for-like (item 9a). |
| CNS dynamical, $b<1/24$ | $1/24=1/(8(d-1))$ at $d=4$. The file says the curvature estimate is for a conditioned system in one fewer dimension; with the SZZ form in $d-1=3$ one would get $1/32$, so the stated reason and the number do not obviously match. | The threshold, the convention, Definition 1.4 and Theorem 1.6. The conclusion is an area law, not covariance decay. |
| CNS expanded, $b\le10^{-40}/(2N)$ | $b=2t/N$ from $2t\,{\rm ReTr}=Nb\,{\rm ReTr}$; $t\le10^{-40}/4$ gives $b\le10^{-40}/(2N)$. Right. | The conditions $N\ge10^{10}d^{10}$, $t\le10^{-10d}/d$; Theorems 1.2 and 4.1. |
| CPS, $b=2\beta_{\rm CPS}$ | Consistent if CPS sum over both orientations of each square with weight $N\beta$. | Equation (1.2) and Theorems 5.7 and 1.8. |

**Verdict on the comparison claim. HOLDS AFTER CORRECTION. CITED, source check pending.** "$1/24<b\le1/20$ lies past both numerical SU(N) thresholds" is true relative to the two listed numbers. Correction: only SZZ ($1/48$) is a covariance-decay threshold; the $1/24$ is an area-law threshold, a different conclusion. The table also omits other uniform-in-$N$ strong-coupling results for SU(N) and SO(N) Wilson theory that I know of (Chatterjee 2015 for SO(N); Jafarov 2016 for SU(N), cited elsewhere in the file for the identity only; Basu–Ganguly 2016; Chatterjee–Jafarov on the 1/N expansion) and the classical cluster expansions. I cannot check their thresholds or whether any gives covariance decay at $b>1/20$ without the sources. The "beyond the known windows" statement must wait for that check.

## Item 12. Purity remark

**HOLDS. ARGUED (label correct).** $(1+Ma^{2u})/(1+Ma^u)^2\to0$ as $M\to\infty$, roughly like $1/M$. A fixed-$b$ small-coupling gap gives no passing cutoff. The crux stays open; the file says so.

## Summary

| Item | Verdict |
|---|---|
| 1 Lemma 1 (centre Jensen, Ricci $N/2$, Bochner, Lipschitz, covariance, (1)) | HOLDS |
| 2 Lemma 2 ((3), slot costs, score, counts $4D$ and $4/3$, (2)) | HOLDS |
| 3 Contraction, (6), finite propagation, (7) | HOLDS |
| 4 Range (8), rectangle, fixed exterior | HOLDS |
| 5 Master equation; uniqueness | HOLDS AFTER CORRECTION: uniqueness holds for all $b$, $N$ in finite volume; the range gives only the uniform rate |
| 6 (10), (11), Gibbs uniqueness, (12) | HOLDS; transfer remark HOLDS AFTER CORRECTION (ARGUED, needs cited RP) |
| 7 $144b^2+32b^2<1/2$ | HOLDS |
| 8 $b=1$ trial law, $\|K\|>21/20$ | HOLDS (constants recomputed exactly) |
| 9 U(1), dimension | HOLDS |
| 10 SU(2), $\beta<\sqrt{3/88}$ | HOLDS AFTER CORRECTION: state Lemma 2 for $N=2$; the range is below in-lane Theorem A ($\beta<1/4$) |
| 11 Coupling table | HOLDS AFTER CORRECTION: $1/24$ is an area-law threshold; omitted large-N strong-coupling results; all theorem numbers need a source check |
| 12 Purity | HOLDS (ARGUED) |

What was checked: every displayed estimate and constant in the file, by hand, by Claude Opus 5.5. Constants were recomputed with exact fractions (`chk1725.py`); su(N) identities were checked by a float guide (`lie_guide.py`, not a proof). Not done: Lean verification; any source check of the cited papers (no web access). This is one cross-provider reader; it is not an independent derivation of the estimates.

Substance (my reading): the new content is a volume-uniform Helffer–Sjostrand covariance bound with the Hessian paid at order $b^2$ via one integration by parts per square. The master-loop framing adds the invariance $P_tJ\subset J$; the uniqueness part alone is not progress.

RESULT: Row 1714 HOLDS with no FAILS, checked line by line by Claude Opus 5.5. Lemma 1, Lemma 2, (2), the contraction (6)-(7), range b < 1/(4 sqrt 22), rectangle constants (q < 11/12, eta > 1/20), (10)-(12), 144b^2+32b^2, and the b = 1 trial law (norm > 21/20) all recomputed exactly. Corrections: finite-volume uniqueness holds at every b and N, so it carries no range content; the transfer energy remark is ARGUED; Lemma 2 must be stated for N = 2; the SU(2) range beta < sqrt(3/88) is below in-lane Theorem A (1/4); 1/24 is an area-law threshold, and the table omits other large-N strong-coupling results. All citations need a source check.
