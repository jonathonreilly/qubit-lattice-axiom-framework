# Repo search

**ON FILE (rule 9, row 1626).** The working tree is pinned at `f33444063689`. I searched `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`) in Markdown and TeX. The target search across all five refs returned no matches for VIR-down, coarse-loop domination, positive coarse-loop contribution, within-cell prediction, buffered slab score, diffusion distance, one-step secant, secant rate ceiling or excited heat trace root. A wider bounded search included leading plaquette eigenmodes, coarse-grained Dirichlet estimates and rank-one estimates. It also hit finite-carrier algebra and linearized curvature records on main.

- **ON FILE (main).** `research/mass-gap/library/gap-transfer-check.md:106–114` gives $0<\lambda_1/\lambda_0\le1-e^{-24\beta n^3}$ for the spatial gauge-invariant transfer at positive coupling and identifies the rank-one endpoint at zero. It gives neither the order-four neutral kernel coefficient nor the signed comparison. In `docs/GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md:146–152` a supplied two-slice SU(3) cube at zero temporal coupling has $D_{s,0}=|g_s\rangle\langle g_s|$. The neighbouring `docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md` applies small-perturbation stability to an electric-dominated SU(3) link Hamiltonian. Its small-$av$ gap applies to that Hamiltonian.
- **ON FILE (PRs 10114, 10133).** Under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` gives the simple-loop convolution eigenvalue $r_f^{|C|}$, with $r_f=I_2(\beta)/I_1(\beta)$ for SU(2). The centered loop $F$ gives the quadratic-form minorant $(1+v_N/r_f^{|C|})^{-1}|F\rangle\langle F|$. The November 8 [repo digest](prior/repo-search-2026-11-08.md) identifies the same one-step witness.
- **ON FILE (PRs 10114, 10133).** The companion `REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md:162–189` gives half-slab influence row sum $14\beta$ and one-step oscillation contraction $\beta/[1-12\beta-\beta^2/(1-14\beta)]$ in its small-coupling range. Neither bound compares the two Jordan parts in (15).
- **ON FILE (rows 244, 1611, 1624).** Sussman and Alpoge with Claude and Codex, outline revision `31a47c543775`, [index chunk 02](sa-index/chunk-02.md) and [obligations](sa-index/obligations.md), lines 2315–2393 of the outline. GL8 identifies $Z_s(0)=\operatorname{Tr} L^s$. GL9–GL11 bound a trace with sparse contraction insertions by $\operatorname{Tr} L^s$ and give a nonpositive mean for their logarithmic source. The two-step mark here has both signs. In this lane row 1611, [character check after (11)](gap-direction7-astra62.md), already identifies the degree-four neutral networks on the spatial torus as the fundamental squares and their normalized electric convolution multiplier as $(\beta/4)^4+O(\beta^6)$. I use that result below.
- **ON FILE (registry and row 1624).** [VIR-DOWN](open-registry.md) is open and has no owner. LEV-FAIL owns a result about individual high levels. The [tool note](gap-vir-down-tool-astra62.md) proves that the buffered signed kernel is $P^k S P^k$, that (15) implies a thermal rate, and that changing which bit is observed can reverse (15) while preserving the whole spectrum. Its Wilson inequality is labelled GUESSED. The task-specific prior file was absent.

**GUESSED (row 1624, calibrated target).** Fix the release witnesses $b,g_0$, an allowed $\ell$, $n=\ell b^K$ and $u=n/512$. The concrete test takes $\kappa=8/3$, $t=u\exp[\kappa(\beta-\beta_K)]$ from $u$ to $n$, and $k=\lfloor t/8\rfloor$. At every point with $G(t)\le1/2$ it asks that the positive contribution measured by the fixed flowed loops pay the complete negative cost, for infinitely many $K$. Below, (1) and (14) give necessary tests valid on this band. The counterexamples (7) and (15a) use other bare couplings on actual Wilson boxes.

**ON FILE (rows 1610, 1613, 1617–1623).** TR-down uses the fixed-time coupling derivative on the cold part of a characteristic and an independent hot-end estimate. Row 1617 (10) and check 1621 §3 estimate discarded electric spins and the vacuum replacement. Row 1619 §3.3 identifies the full action deficit with a squared-force excess. Row 1618 Theorem 2 and check 1622 §2 retain the even electric rotors in the compact Gaussian model. Check 1620 concerns neutral projection in a different ring test. The literature search in row 1623 found no bound of the required size. Additional searches for within-cell variance, Jordan cost, trace of the positive part and flat shifts of contractible loops found the variance decomposition in row 1624 (13) and the flat-shift observation in [gap-solve14-astra62.md](gap-solve14-astra62.md). The five-ref search also included a Jordan decomposition of prediction cost, secant obstruction, and a characteristic for the root of the excited heat trace. No result from Balaban is used here.

## A necessary condition independent of the buffer

**ON FILE (1624 (1)–(3), (7), (15)–(16)).** Fix one coupling and one spatial Wilson box. Work in real centre-neutral $L^2(\pi)$, where $P$ is the self-adjoint vacuum Markov operator, $P1=1$, with strictly positive excited multipliers $r_i=e^{-m_i}<1$. Let $Q$ project off the constant and $E$ be conditional expectation onto the fixed flowed-loop partition. On this space $E$ is an orthogonal projection and $E1=1$. Relative to $\pi\otimes\pi$ the central signed kernel is
$$
 S=S^0+2\kappa(P-P^2),\qquad
 S^0=-Q U^{-1}(A_\beta^2)'UQ ,
$$
where $A_\beta=T_{+,\beta}/\lambda_0(\beta)$, $U f=\Omega_\beta f$ is held fixed in the derivative, and $S1=0$. Use $G(t)=\sum_{i>0}r_i^t$, $Z(t)=1+G(t)$, $X(t)=\log Z(t)$ and $\bar E_t=Z(t)^{-1}\sum_{i>0}m_i r_i^t$. The invariant probability is $\pi(dx)=\Omega_\beta(x)^2 dx$ for product Haar $dx$, and $p_s(x,z)$ denotes the transition density of $P^s$ relative to $\pi$. The full prediction cost $D_s(x,y)$ is the squared $L^2(\pi)$ distance between $p_s(x,\cdot)$ and $p_s(y,\cdot)$. Project the two densities by $E$ before taking that distance to obtain $L_s(x,y)$. Row 1624 bins the traces of spatial squares of side $n/32$ on the $n/32$ grid after flow time $(n/128)^2$.

The outer signed measure $\mu_k$ has kernel $P^k S P^k$. Write $v=\lfloor t/2\rfloor$, $j=v-k-1\ge1$ and $h=2k+2$. These choices include $k=\lfloor t/8\rfloor$ for all late cutoffs. Let $\mu_k^\pm$ be the positive measures in its Jordan decomposition. Row 1624 (15) asks for $\mathcal M_k=\int L_{j+1}\,d\mu_k^+-\int D_j\,d\mu_k^-\ge0$.

**PROVED (a lower bound for the omitted fluctuations).** Put $H=I-PEP$, a positive contraction, and set
$$
 V=-2\operatorname{Tr}(E P^v S P^v),\qquad
 B=H^{1/2} P^{v-1} S P^{v-1} H^{1/2}.
$$
On every such box, simultaneously for all admissible buffers and observations,
$$
 \mathcal M_k\ \le\ V-2\operatorname{Tr}(B_+).                         \tag{1}
$$
Here $B_+$ is the spectral positive part of the self-adjoint operator. Thus one strictly negative right side excludes every buffer at this $t,\beta$. Both terms use the unbuffered two-step insertion. Row 1624 (16) gave buffer independence for the **complete** signed thermal contrast. Equation (1) retains the particular observed loops and charges a part of the cost they miss.

*Proof.* Let $d_s(x,y)$ be the vector $p_s(x,\cdot)-p_s(y,\cdot)$ in $L^2(\pi)$. Then $d_{j+1}=P d_j$ and
$$
 D_j-L_{j+1}=\|H^{1/2}d_j\|^2 .
$$
Adding and subtracting $\int L_{j+1}\,d\mu_k^-$ gives the equality
$$
 \mathcal M_k=\int L_{j+1}\,d\mu_k-\operatorname{Tr} N_- ,\qquad
 N_\pm=\int |H^{1/2} d_j\rangle\langle H^{1/2} d_j|\,d\mu_k^\pm .       \tag{2}
$$
The positive operators $N_\pm$ have finite trace since $d_j$ is bounded in norm on each compact box. For any real $f$, $\langle d_j,f\rangle=P^jf(x)-P^jf(y)$. In integrating its square against $\mu_k$, the two one-end terms vanish by the zero marginals. The mixed term gives $-2\langle P^j f,P^k S P^k P^j f\rangle$. Applying this to $H^{1/2}f$ proves $N_--N_+=2B$, because $k+j=v-1$. Applying the same calculation to an orthonormal basis of the cell constants with $j+1$ in place of $j$ gives $\int L_{j+1}\,d\mu_k=V$, because $k+j+1=v$. If $J$ is the positive spectral projection of $B$, then $2\operatorname{Tr}B_+=\operatorname{Tr}(J N_-)-\operatorname{Tr}(J N_+)\le\operatorname{Tr}N_-$. This proves (1). In particular no diagonalization of the Jordan density, and no assumption that $E$ commutes with $P$, enters the bound.

**PROVED (a rate ceiling from the observed loops).** Whenever $E$ contains a nonconstant neutral function, set
$$
 a_E=\operatorname{Tr}(E P^{2v+1}(I-P))>0.
$$
In an eigenbasis of $P$ this is the sum of $r_i^{2v+1}(1-r_i)\|E f_i\|^2$. Injectivity on the neutral space and the nonconstant cell function make at least one term positive. Cyclicity in the finite-rank trace gives $V= -2\operatorname{Tr}(E P^v S^0P^v)-4\kappa a_E$. Passing (15) at a positive rate therefore requires
$$
 \kappa < \frac{-\operatorname{Tr}(E P^v S^0P^v)}{2 a_E}.                \tag{3}
$$
The strict inequality follows from (2). By row 1624 (14) and its buffered extension both signs have positive mass, and $D_{j+1}-L_{j+1}>0$ almost everywhere for the specified finite observation. More generally $D_j>D_{j+1}$ almost everywhere by row 1624 (7) and a nonconstant analytic eigenfunction. Thus $\operatorname{Tr}N_->0$. The numerator of (3) is a signed sum of two-step action measurements of observed predictors by row 1624 (5). It can rule out a rate before estimating the complete negative part. Sufficiency would require a bound for that cost.

## Which energies can affect the comparison on the band

**ON FILE (1161 (19), check 1162 S25, 1619 TRUNC, 1624 (21)).** There is an absolute $C_*$ with $m_1\le C_*$ on the late Wilson boxes at every $\beta\ge1$. Take $k=1$ in the neutral plaquette count of [row 1161](gap-solve9-astra62.md). That bound is stronger here than the elementary one-plaquette witness on PR 10114. Row 1619 bounds $G(1)\le e^{12\beta n^3}$. Row 1624 gives $\|S\|\le s_n=24n^3+\kappa/2$. Its two-sided smoothing estimate bounds individual operator matrix elements. A Jordan cost also involves the number of modes and the endpoint weights.

**PROVED (cutoff-uniform error for the signed observed response).** Put $d=\operatorname{rank}(EQ)$, bounded by $16^{3\cdot32^3}$ for the specified observation. Write $W_t=Z(t)\bar E_t=\sum_{i>0}m_i r_i^t$. For $L\ge0$ let $F$ project onto excited energies $m_i\le m_1+L/v$, and let $V_F=-2\operatorname{Tr}(E P^v F S F P^v)$. At every cold point $G(t)\le1/2$ on these boxes,
$$
 |V-V_F|\le 4d s_n r_1^{2v}e^{-L}
       \le \frac{4d s_n t e^{2C_*}}{\log 2}\,e^{-L} W_t .                 \tag{4}
$$
Indeed $R=P^vQ$ has norm $r_1^v$, and $\|(I-F)R\|\le r_1^ve^{-L}$. Expanding $RSR-FRSRF$ by replacing the two factors $R$ in order costs at most $2s_n r_1^{2v}e^{-L}$ in operator norm. Taking the trace on the $d$ nonconstant cell directions proves the first bound. Coldness gives $tm_1\ge\log 2$, so $W_t\ge (\log2)r_1^t/t$, and $0\le t-2v<2$. This proves the second bound. At even integer $t$ the factor $e^{2C_*}$ can be replaced by one. For fixed bounded rates, $u\le t\le n$, and tolerance $0<\eta\le1$, it takes an additive energy window of width $O((1+\log n+\log(1/\eta))/t)$ above $m_1$ to control $V$ to $\eta W_t$. Although the number of loop cells can be very large, it is independent of the cutoff. There is no assumption on the multiplicity of the first level or on the gap to the next.

**PROVED (error in removing the high-energy part of the complete negative cost).** Keep the actual Jordan measure. For any $a\ge0$ let $D_{j,\ge a}$ consist of the terms $m_i\ge a$ in row 1624 (7). With $b_n=24n^3$ and $c_n=3b_n+2\kappa$,
$$
 \int D_{j,\ge a}\,d\mu_k^-\le 4c_n e^{-(2j-1)a}G(1).                  \tag{5}
$$
Write $q_s=p_s\,\pi\otimes\pi$, let $A$ be the central two-step shifted Wilson action with stationary mean $\bar a$, and put $g(x)=\mathbb E[A-\bar a\mid X_0=x]$ at its initial end. Condition the mark in row 1624 (20) on the outer pair. The signed measure is $(\mathbb E[A\mid x,y]-\bar a)q_h-(P^kg(x)+P^kg(y))\pi\otimes\pi-2\kappa q_h+2\kappa q_{h-1}$. Since $0\le A\le b_n$ and $|g|\le b_n$, its negative part is dominated by $(b_n+2\kappa)q_h+2b_n\pi\otimes\pi$. Either marginal is dominated by $c_n\pi$. Hence the negative cost of the $i$-th predictor is at most $4c_n r_i^{2j}$, using $(f_i(x)-f_i(y))^2\le2f_i(x)^2+2f_i(y)^2$ and $\|f_i\|_2=1$. Sum and spend one power on $G(1)$ to prove (5). Consequently the part above
$$
 a=\frac{12\beta n^3+tC_*+\log(4c_n t/(\eta\log2))}{2j-1}
                                                                            \tag{6}
$$
costs at most $\eta W_t$, uniformly at the cold points. This time the projection is on the **negative-side predictors**, after the pointwise negative part has been taken. It needs no bound on their individual sup norms, no probability floor for an observation cell, and no truncation of the signed mark. For $k=\lfloor t/8\rfloor$, (6) is of order $\beta n^2$ at $t\asymp n$ and fixed tolerance. This leaves a much larger range than (4). In particular the relative estimate for the signed loop response does not control the cost of unobserved modes just above its narrow window. The scalar heat-trace tail estimate used in (5) is the one from row 1619 TRUNC. Its application to the full pointwise negative part uses the marginal bound above.

## Finite cold SU(2) Wilson boxes where (15) fails

**PROVED (strong-coupling counterexample).** For every fixed $1024\mid n$ with $u=n/512\ge8$ there exist $\epsilon_n>0$ and $K_n<\infty$ such that for all $0<\beta<\epsilon_n$, all $u\le t\le n$, every admissible $k$, every finite neutral observation and **every** trial rate $\kappa\ge0$,
$$
 0\le
 \frac{\int L_{j+1}\,d\mu_k^+}{\int D_j\,d\mu_k^-}
       \le K_n\beta^8<1 .                                                   \tag{7}
$$
The denominator is strictly positive. The bound even holds if the numerator uses the complete $D_{j+1}$. These are the Wilson magnetic and electric weights on all the links of the given box. The temperature and coupling limits in this section are at fixed $n$.

*Proof of the kernel expansion.* Use product Haar probability $dx$. Let $F_4$ be the Haar orthogonal projection onto the span of the fundamental plaquette characters $\chi_p$ (one per unoriented elementary square). Each has Haar norm one. Integrating a link belonging to exactly one of two different squares kills the cross term, proving orthonormality. Define $a=(\beta/4)^4$. Dividing the projected electric convolution by its constant multiplier gives
$$
 C_\beta=|1\rangle\langle1|+a F_4+O_n(\beta^5) .                            \tag{8}
$$
Here and below a kernel error is in the uniform norm on the compact pair of slices. The coefficient and absence of lower nonconstant degrees are the character check of row 1611, using Sussman–Alpoge GL3 (outline 2197–2243). To justify the norm in (8), the gauge- and centre-averaged product of link exponentials is analytic in $\beta$ with a uniformly convergent Taylor expansion near zero, even after the scalar normalization. Each Taylor coefficient of order $q$ has total representation degree at most $q$ by the tensor product rule for fundamental matrices. Projecting its endpoints leaves only the neutral networks of those degrees. The constant eigenvalue is identically one. Row 1611's degree-four eigenvalue therefore gives the entire displayed nonconstant kernel coefficient.

Let $M_\beta=e^{-\beta V_{\rm sp}/2}=1+O_n(\beta)$ denote multiplication by the spatial half-weight (also write $M_\beta$ for the function). The normalized transfer $A_\beta$ is $M_\beta C_\beta M_\beta$ divided by its top eigenvalue $\lambda=1+O_n(\beta)$ in this normalization. The normalized real vacuum $\Omega_\beta=1+O_n(\beta)$ and the top eigenvalue are analytic near zero. Indeed the kernel is analytic and at zero the transfer is the constant rank-one projection. Its resolvent on a small circle about one has a convergent Neumann expansion. Apply the resulting projection to 1 and normalize in Haar norm to get an analytic $L^2$ eigenvector. Its own kernel equation gives analyticity in the uniform norm. Write $Q_\beta=I-|\Omega_\beta\rangle\langle\Omega_\beta|$. Applied to $\Omega_\beta$, (8) in the magnetic sandwich gives $\lambda\Omega_\beta=M_\beta\langle M_\beta,\Omega_\beta\rangle+O_n(\beta^4)$ uniformly. The scalar product tends to one, hence $Q_\beta M_\beta=O_n(\beta^4)$. Compress the magnetic sandwich by $Q_\beta$. The rank-one term now costs $O_n(\beta^8)$. The compression of $M_\beta F_4 M_\beta$ is $F_4+O_n(\beta)$ because $F_4 1=0$. This proves
$$
 A_\beta-|\Omega_\beta\rangle\langle\Omega_\beta|
       =a F_4+O_n(\beta^5).                                                 \tag{9}
$$
Raising (9) to a fixed positive integer $s$ and dividing its kernel by $\Omega_\beta(x)\Omega_\beta(y)$ gives $p_s-1=a^s(F_4+O_{n,s}(\beta))$, since $F_4^2=F_4$. In particular, uniformly on endpoint pairs,
$$
 a^{-2s}D_s(x,y)\longrightarrow
 D^{(4)}(x,y)=\sum_p(\chi_p(x)-\chi_p(y))^2.                                \tag{10}
$$
The integration in $D_s$ uses $\pi_\beta=\Omega_\beta^2dx\to dx$ uniformly in density. The right side is positive for Haar-almost every pair. A single plaquette holonomy is Haar under $dx$ by integrating one edge. Its SU(2) trace has no atoms, by the class angle density proportional to $\sin^2\theta$.

*Proof of the bound for both signs.* At fixed $k$, the Haar-pair density of $\mu_k$ has the form $s_0(\beta)+\kappa s_1(\beta)$, with both coefficient functions mean zero and real analytic in $\beta$ near zero as continuous kernels. Indeed they come from the derivative of $A_\beta^2$, the vacuum compression and the duration difference, followed by $k$ propagations on each side. Uniform kernel analyticity follows from the preceding vacuum construction, products of kernels on a probability space, and division by $\Omega_\beta$ bounded away from zero. This reasoning includes $k=0$ and uses fixed Haar coordinates for the densities.

Here is the uniformity in the trial rate, including rates tuned to cancel the leading coefficient. For two curves real analytic at zero in $C(X)$ on a compact probability space of full support, the unit $L^2$ vectors in their linear spans have uniformly convergent subsequences as $\beta\downarrow0$. To prove this, discard an identically zero curve. Divide the first by its first nonzero power of $\beta$, then by its $L^2$ norm. This gives an analytic unit vector with a nonzero continuous limit, since its squared norm is analytic and has positive limit. From the second curve subtract its projection onto the first unit vector. If the residual is not identically zero, do the same division and normalization to obtain a second unit vector orthogonal to the first. The coefficients of any unit combination lie on a compact sphere, and the limiting basis is orthonormal. This proves the assertion. Every limiting combination in our application has zero integral and unit norm with respect to the *fixed* Haar-pair probability.

The density being normalized is nonzero for every $\beta>0$ and $\kappa\ge0$. To check this on the finite Wilson box, its diagonal on $f_i$ in $L^2(\pi)$ is $2r_i^{2k+1}[\kappa(1-r_i)-d_i]$, where $d_i=\langle\psi_i,A'_\beta\psi_i\rangle$. Row 1617 (2), checked in 1621 §1.2, gives $(d_i/r_i)\sim m_i/(\beta\log m_i)$ as $m_i\to\infty$ on this box. There are infinitely many such neutral levels. Thus $d_i>0$ eventually and $d_i\to0$. The displayed diagonal is nonzero eventually for either $\kappa=0$ or any fixed positive value at this anchor. This step excludes exact cancellation. The compact-sphere argument handles arbitrarily close cancellation.

Normalize the density to $L^2(dx\,dy)$ norm one, calling it $s$. Then $\int s_+\,dx\,dy\le1$. For all sufficiently small positive $\beta$, $\int (D_j/a^{2j}) s_-\,dx\,dy$ has a positive lower bound independent of $\kappa$. Otherwise take a sequence tending to zero. By compactness just proved and (10), the limit is $\int D^{(4)} s_{*,-}\,dx\,dy$. A real mean-zero unit vector has negative part of positive integral, and $D^{(4)}>0$ almost everywhere, a contradiction. On the positive side $D_{j+1}\le C_{n,j}a^{2j+2}$ uniformly by (10). Cancelling the density normalization gives (7) for fixed $j,k$. There are only finitely many admissible integer pairs for $t\in[u,n]$ at this fixed $n$. Take the maximum of their constants and decrease $\epsilon_n$ to make the last bound strictly less than one. This proves (7). If the numerator uses $D_{j+1}$, applying the same compactness argument to $s_+$ at time $j+1$ and the uniform upper bound (10) on the denominator gives a positive $n$-dependent lower bound times $\beta^8$ as well. Thus the extra prediction step alone costs this power even with the full observation.

**PROVED (the same boxes pass the thermal test).** At fixed $n$ as above the purity at $u$ tends to one as $\beta\downarrow0$, and, uniformly for real $u\le t\le n$,
$$
 \frac{\partial_\beta X(t)}{t\bar E_t}
   =\frac{4/\beta+O_n(1)}{4\log(4/\beta)+O_n(1)}
   \longrightarrow+\infty .                                                \tag{11}
$$
Thus the pointwise thermal inequality at rate $8/3$ holds on the very boxes where (15) fails even at rate zero.

*Proof.* Write the left side of (9) as $a J_\beta$. Then $J_\beta=F_4+O_n(\beta)$ and $J'_\beta=O_n(1)$ in Hilbert–Schmidt norm by the analytic kernel expansion. For $\beta>0$, $J_\beta$ is positive semidefinite. Its eigenvalues $z_i$ lie in $[0,2]$ for small $\beta$, their squared sum is bounded, and at least one exceeds $1/2$. Hence $T_t=\operatorname{Tr}J_\beta^t$ is bounded above and below by positive $n$-dependent constants in the indicated time range. Also $\sum_{z_i>0}z_i^t|\log z_i|$ is bounded there, because $z^{t-2}|\log z|$ is uniformly bounded for $0<z\le2$ and $8\le t\le n$. Now $G(t)=a^t T_t$. The fixed-time trace derivative gives
$$
 \frac{\partial_\beta G}{tG}
   =\frac4\beta+\frac{\operatorname{Tr}(J_\beta^{t-1}J'_\beta)}{T_t},
 \qquad
 \frac{W_t}{G}=-\log a-\frac{\sum_{z_i>0}z_i^t\log z_i}{T_t}.
$$
The first remainder is bounded by Hilbert–Schmidt Cauchy–Schwarz. For real $t$ the trace derivative used here is the fixed-Hilbert-space formula of check 1613, §3, regularity (R). It also follows here by writing $J^t=J^2 f(J)$ and approximating $f(z)=z^{t-2}$ and its derivative uniformly on $[0,2]$ by polynomials with their derivatives. Cyclic differentiation of the polynomial traces gives the candidate derivative. Its error is bounded by a constant times the uniform approximation error times $\|J\|_{\rm HS}\|J'\|_{\rm HS}$. Integrating the polynomial identities over a small coupling interval and passing to the limit proves the derivative formula. These equations give (11). As $G(u)\to0$, $Z(2u)/Z(u)^2\ge(1+G(u))^{-2}\to1$, and this purity is at most one by squaring the nonnegative weights. In particular the boxes are cold.

**PROVED (a second sign check at the prescribed positive rate).** From $A_\beta-\Pi_\beta=aJ_\beta$, where $\Pi_\beta=|\Omega_\beta\rangle\langle\Omega_\beta|$, every excited diagonal satisfies $|d_i|=O_n(\beta^3)$ uniformly in $i$, since differentiating $\Pi_\beta^2=\Pi_\beta$ gives $Q_\beta\Pi'_\beta Q_\beta=0$. Also $r_i=O_n(\beta^4)$. For any **fixed** $\kappa>0$ one therefore has $d_i<\kappa(1-r_i)$ on every excited state once $\beta$ is small enough. Row 1624 (10), (16) now makes even the complete signed contrast strictly negative, for every buffer. This verifies failure at $8/3$ by a spectral test which never splits the endpoint density into signs. At $\kappa=0$ the same complete signed contrast is strictly positive by (11), whereas (7) still reverses the Jordan comparison. This last failure isolates the asymmetric use of $j+1$ and $j$ in (15).

## What the comparisons read

**PROVED (test in the sector containing the observation).** Let $J$ be an orthogonal projection commuting with $P$ whose range contains the cell functions. Choose an orthonormal eigenbasis of $P$ adapted to $J$, and let $I_J$ index its excited vectors in that range. Then for all buffers,
$$
 \mathcal M_k\ \le 4\sum_{i\in I_J}r_i^t\big[d_i/r_i-\kappa(e^{m_i}-1)\big].                \tag{12}
$$
Indeed $L_{j+1}=\|E d_{j+1}\|^2\le\|J d_{j+1}\|^2$. By the spectral expansion of row 1624 (7),
$$
 L_{j+1}\ \le\ D_{*,J}:=\sum_{i\in I_J}r_i^{t-h}(f_i(x)-f_i(y))^2
           \ \le\ D_j .
$$
These inequalities follow from $2j\le t-h<2j+2$, with no sign assumption on the mark. Substitution in the two Jordan integrals bounds $\mathcal M_k$ above by $\int D_{*,J}\,d\mu_k$. The zero marginals and the excited diagonals used in (7) give (12) term by term. Domination by $D_j$ justifies the sum on the compact Wilson box. For the Gaussian comparison below the integrability bound of row 1624 (18) applies to the same $D_j$. This argument tests all predictors in one symmetry sector and needs no derivative of $E$ or $J$.

**PROVED (compact Gaussian U(1) with the actual loop observation).** In the zero-monopole, zero-magnetic-flux law of row 1618 and check 1622, (15) fails for **every** $\kappa>0$ at every admissible $t$, for every buffer, when the observation consists of contractible flowed loops. This extends row 1624 (18), which excludes $\kappa\ge1/\beta$ for arbitrary observations. Work in that row's Gaussian comparison coordinates. Multiplication by a flat abelian field is an isometry and preserves every spatial plaquette. It therefore preserves the gradient vector field and commutes with spatial flow. The value of every contractible loop is invariant under the shift. Each cell function thus belongs to the sector of **zero integer electric charge**, even though the full thermal trace keeps every even charge vector. The transfer in this sector is the transverse photon transfer. Its excited energies are independent of $\beta$, so $d_i=0$ there. Equation (12) gives
$$
 \mathcal M_k\le-4\kappa\sum_{i\in I_{\rm ph}}e^{-tm_i}(e^{m_i}-1)<0 .     \tag{13}
$$
There is at least one transverse mode. For the pure transverse photon use the entire sector in (12), which gives the same strict failure for every observation and every positive speed.

**PROVED (zero speed in the compact Gaussian comparison).** At $\kappa=0$ the right side of (13) is zero. The negative part of $\mu_k$ is still nonzero. For example the real even-rotor mode $f(\Phi)=\sqrt2\cos(2\Phi_1)$ has $m=2/(\beta n)$ and $d_i/r_i=m/\beta>0$, so its signed-kernel diagonal is nonzero. The signed measure has zero total mass and both signs are absolutely continuous with respect to the product stationary law, by the smooth rotor transition and the Gaussian transitions in row 1624 (18). The missing negative cost obeys $D_j-D_{*,J}\ge e^{-2jm}(f(\Phi_x)-f(\Phi_y))^2$ for this hidden rotor and the photon projection $J$. Haar holonomy makes the square positive almost everywhere. This turns the inequality at zero into $\mathcal M_k<0$. In particular the coarse test can fail at *every* rate in a model where the full cold thermal rate exceeds $9/(10\beta)$ by row 1618 Theorem 2. The visibility of a contractible loop is a symmetry fact. The coupling-independent transverse spectrum and the rotor response used for the strict deficits are facts about the transfer law. For the pure photon at zero speed the signed measure in the rescaled coordinates vanishes.

**ON FILE / PROVED given the periodic Villain input (interacting weak 4D compact Wilson U(1), rows 1573, 1579, 1613, 1617, 1624).** With the three half-turns, the periodic Villain comparison and positive offset mixture in [row 1573, lines 131–150](gap-band-neutral-astra62.md) give $G_{\rm even}(u)\ge 2d_\gamma^4>1$ at sufficiently weak cosine coupling. The lower bound is on the masses of the $\pm2$ electric sectors. On any window of width $w>0$ ending at $G(t_h)\le4/21$, row 1617 (13) and its preceding mean-value estimate locate an interior cold point with $t(\partial_\beta X/t-\kappa\bar E_t)\le-\log[(3/2)/(1+4/21)]/w$. Substituting the complete sector in (12) and using $e^m-1\ge m$ puts the deficit in (15) at that **same** point at least $4Z(t)\log[(3/2)/(1+4/21)]/(tw)$, for every buffer and observation. This conditional conclusion reads a quantitative property of the weak cosine law. The fibre symmetry alone gives no such size, and no estimate here extends the free dispersion in (13) to the interacting zero-charge sector. Projection by the entire continuous centre removes the two witnesses used in the cosine argument.

**ON FILE / ARGUED (five dimensions and Lemma ALG, rows 1386, 1553, 1613, 1617).** The operator and marginal estimates above work in other dimensions with their corresponding action and level-count bounds. If a five-dimensional Wilson box has a centre-neutral mode with $um<\log2$, the same last-crossing argument forces failure somewhere on any HOT window. To exclude every passing subsequence this way would require the starting obstruction eventually at every allowed side and calibration. That spectral premise for interacting weak 5D SU(2) remains GUESSED. The four-dimensional Wilson law times a coupling-independent light neutral oscillator supplies a concrete comparison with the SU(2) factor retained, as in row 1617. A single oscillator with $um<\log 2$ makes $G(u)>1/2$ there, regardless of the loop law on the Wilson factor. The product keeps the SU(2) bracket and the spacetime dimension while changing the thermal law. The same four-dimensional SU(2) algebra also occurs in the failing cold boxes (7).

**ON FILE / ARGUED (relation to the seed).** A positive answer to (15) on the entire prescribed cold characteristic, together with an independently supplied HOT on infinitely many calibrated boxes, implies (PUR-io) after the allowed fixed enlargement by rows 1610, 1613 and 1624. [Consumer, row 1468 §3.1](gap-k2-tool-design-fable.md). The four-state interchange in row 1624 proves that even a passing long-window thermal response and purity do not force the fixed-observation domination on positive transfer families. Equation (7) separates same-box Wilson purity from (15) when the coupling can be chosen at fixed volume. Neither example reverses the quantifiers on the *calibrated pure Wilson* sequence. I cannot decide its converse or claim strictness there. CA-I 2703–2711 expressly leaves a mass gap outside Theorem 0.

## A fixed coupling interval with a violation at every large size

**PROVED (a necessary endpoint inequality for the calibrated band as well).** Follow any cold characteristic $t'=\kappa t$ starting at time $u$. Write $q=G(t;\beta)^{1/t}$ and $Y=(t/u)(1-q)$. On a finite Wilson box $G>0$. At every cold point, for every buffer and observation,
$$
 Y'\le-\frac{t q}{u}\,\Delta,\qquad
 \mathcal M_k\le4G\Delta,\qquad
 \Delta=\frac{\partial_\beta G}{tG}
             -\kappa\sum_{i>0}\frac{r_i^t}{G}(e^{m_i}-1).                   \tag{14}
$$
In particular (15) throughout a cold interval requires $Y$ to be nonincreasing there. This conclusion uses the one-step secant in row 1624. TR-down by itself only bounds $G$ along the characteristic.

*Proof.* Put $y=-\log q\ge0$, and average with excited weights $p_i=r_i^t/G$. Their entropy is $-\sum p_i\log p_i=t(\langle m\rangle-y)\ge0$. All averages converge, since $t\ge 8$ and the one-step transfer is trace class. Differentiating at fixed box along the characteristic, using the fixed-time derivative for the coupling, gives
$$
 y'=-\Delta-\kappa\big[\langle e^m-1-m\rangle+y\big]
      \le-\Delta-\kappa(e^y-1).
$$
The inequality uses convexity and monotonicity of $e^m-1-m$ for $m\ge0$ and $\langle m\rangle\ge y$. It gives $q'\ge q\Delta+\kappa(1-q)$, which proves the first part of (14). The second is (12) on the full space, using the trace derivative of check 1613. The proof differentiates $G$, so changes in the integer buffers as $t$ varies cause no boundary terms.

**PROVED (uniform finite Wilson counterexample off the calibrated band).** Fix $b_*=1/128$, $I=[b_*/4,b_*]$, $\kappa=8/3$ and $t(\beta)=u\exp[\kappa(\beta-b_*/4)]$. Then for all sufficiently large $1024\mid n$, every point of this same interval has $G(t(\beta);\beta)\le4/21$, and there exists $\beta_n$ in the interior of $I$ such that, simultaneously for **every** buffer and observation,
$$
                    \mathcal M_k(t(\beta_n),\beta_n)
                         \le -c\,G(t(\beta_n);\beta_n),\qquad c>0 .        \tag{15a}
$$
The constant $c$ and the interval do not depend on $n$. This fixes the coupling interval before sending the box size to infinity. The size of the unnormalized deficit can shrink with $G$.

*Proof, coldness.* Use the ordinary gauge-invariant slab of integer duration $s=\lceil\sqrt n\rceil$. Row 1573 (4), from row 1568 Theorem E, gives $\sup |D_xD_y\log K_s|\le18(3n^3)\beta^2\sum_{r\ge s-2}(r+1)(9\beta/2)^r$, for simultaneous pin velocities of at most one per link. This bound times $\pi^2$ is $\delta_n=o(1)$ uniformly on $I$ since $9b_*/2<1$. Integrating at both ends along componentwise geodesics gives $e^{-\delta_n} f(x)f(y)\le K_s(x,y)\le e^{\delta_n} f(x)f(y)$, with $f(x)=K_s(x,x_*)/\sqrt{K_s(x_*,x_*)}$. This is the pin factorization used in row 1611's small-coupling benchmark. Here it bounds the **shorter-period trace**. By the Rayleigh quotient on $f$, $\lambda_0^s\ge e^{-\delta_n}\|f\|_2^2$. Also the squared Hilbert–Schmidt error to $f\otimes f$ is at most $(e^{\delta_n}-1)^2\|f\|_2^4$ and at least $\sum_{i>0}\lambda_i^{2s}$ for the ordinary transfer. The latter bound follows by expanding the square and using $\langle f,K_s f\rangle\le\lambda_0^s\|f\|_2^2$. The ordinary vacuum is centre invariant by uniqueness, so removing charged states only decreases the excited trace in this estimate. Therefore $G(2s)\le e^{2\delta_n}(e^{\delta_n}-1)^2=o(1)$ uniformly on $I$. For large $n$, $2s\le u\le t(\beta)$, which proves coldness throughout.

*Proof, the hot-end bound on $q$.* On PRs 10114 and 10133 the cited `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, (23)–(26), gives for $0<\beta\le1/32$
$$
 r_1\le r(\beta)=\frac{\beta}{1-12\beta-\beta^2/(1-14\beta)} .
$$
It applies to the neutral sector since it bounds every nonvacuum physical multiplier. One can see the eigenvalue implication by applying the summed link-oscillation contraction to a nonconstant continuous eigenfunction. At $b_*$ the denominator exceeds $3/4$, so $r(b_*)<4b_*/3$. At $t_h=ue^{2b_*}$,
$$
 G(t_h;b_*)\le r(b_*)^{t_h-2s}G(2s;b_*),\qquad
 \limsup_{n\to\infty}q(b_*)\le r(b_*).
$$
Thus $Y(b_*)\ge1+\delta$ for all sufficiently large $n$, where $\delta=[e^{2b_*}(1-4b_*/3)-1]/2>0$. Positivity follows already from $(1+2b_*)(1-4b_*/3)>1$ for $0<b_*<1/4$. At the starting end $Y(b_*/4)\le1$. The mean value theorem supplies an interior point with $Y'\ge\delta/(3b_*/4)$. There $t/u\le e^{2b_*}$ and $q\le1$. Equation (14) proves (15a) with $c=4e^{-2b_*}\delta/(3b_*/4)$. The point is selected from the full thermal trace, which explains the simultaneous statement for all buffers and all loop observations. This sign check does not use the fixed-$n$ expansion (8)–(10).

**ARGUED (boundary of the inference).** The fixed interval here has integrated speed $2b_*$. The prescribed long calibrated window has integrated speed $\log512$ and starts at $\beta_K\to\infty$. The oscillation and pin bounds used to force $Y(b_*)>Y(b_*/4)$ have small-bare-coupling hypotheses. I have no corresponding violation of $Y$ monotonicity on the calibrated band. Success of that necessary monotonicity test there would still leave the negative cost in (2).

**PROVED (what the endpoint test distinguishes).** On the long calibrated window, HOT and a passing (15) on its cold points would keep the entire window cold by the last-crossing implication of rows 1610/1613. Equation (14) would then require
$$
 G(n;\beta_h)^{1/n}\ge 1-\frac{1-G(u;\beta_K)^{1/u}}{512}.                \tag{16}
$$
For a check of the extra restriction, take a positive two-state Markov transfer with entries $(1+rxy)/2$ on $x,y=\pm1$ and multiplier $r(\beta)=\exp[-a/t(\beta)]$, $a>\log(21/4)$, with strictly increasing $t$ at the prescribed speed. Its excited sum on the characteristic is the constant $e^{-a}$, so the exact thermal rate and HOT hold. The derivative of $t(1-e^{-a/t})$ is $1-e^{-a/t}(1+a/t)>0$. Thus (16) fails even if both states are perfectly observed. This separates the secant restriction itself from the thermal implication.

**PROVED (Wilson purity on the counterexample sequence).** At the uncalibrated starting coupling $b_*/4$ the shorter-period bound in the proof of (15a) gives $G(u;b_*/4)\to0$, hence $Z(2u)/Z(u)^2\to1$. This holds also along $n=\ell b^K$ for any allowed fixed side and block factor $b>1$. Extending that window at rate $8/3$ all the way to $t=n$ preserves its failing interior point, independently of the later couplings. Thus on an infinite sequence of genuine Wilson boxes both the starting purity and the obstruction can be verified. Fixing the starting bare coupling here is precisely where this example leaves the release trajectory.

RESULT (d) for the calibrated target. PROVED the buffer-independent bound (1), the necessary observed rate ceiling (3), the relative energy truncations (4)–(6) and the characteristic test (14).
PROVED that (15) fails on finite cold SU(2) Wilson boxes at every trial rate for sufficiently small bare coupling at fixed size, even while the thermal rate exceeds $8/3$.
PROVED a deficit of at least $cG(t)$ at rate $8/3$ on every sufficiently large Wilson box somewhere in the fixed interval $[1/512,1/128]$, where the starting purity tends to one.
PROVED failure at every positive rate for contractible loops in compact Gaussian U(1), including rates below $1/\beta$. The interacting cosine comparison uses the on-file Villain hypothesis.
GUESSED that the positive coarse-loop contribution pays the complete negative cost on the calibrated band. Whether (PUR-io) forces (15) on that trajectory, failure for interacting weak 5D SU(2), calibrated HOT and the mass gap remain open here. Author hand proofs and checks, with no numerical or Lean proof step and no status change.
