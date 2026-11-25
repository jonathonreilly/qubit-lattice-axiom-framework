# Repo search

Row 1544, Codex research at 6068cc62c. The target-specific prior file is absent. The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. I checked the one-step plaquette witness on PR 10114, the axial Gaussian block formula on that PR, and the plain-to-straight fibre comparison on PR 10141. On the coordinate axis the earlier rational symbol detects an infinite tail for $a\ne8$ and reduces to a nearest-neighbour symbol at $a=8$. The fibre comparison explains why endpoint gradients drop out. I found no matching obstruction or registry owner in the pinned lane and the YM4D materials searched on those refs. Registry trigger R10 asks for exponential decay of posterior weights. It owns that estimate and does not assert finite support. The parallel row was excluded. [Lead's digest](prior/repo-search-2026-11-08.md) · [Plaquette witness, lines 106–149](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106) · [Axial formula, lines 2096–2128](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MANUSCRIPT_RG.md#L2096) · [Fibre comparison, lines 142–155](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/a2f6a430e251aa47bc3eb4f67a1dca2a88530116/research/ym4d/library/fp1.md#L142)

Row 1468 gives the normalized soft block $Q_2$, its exact masses and its intended class with summable tails. Check 1469 supplies the transverse covariance at arbitrary momentum. Row 1479 and check 1483 give the fixed-torus classical limit and disprove closure on the Wilson shape. Row 1497 leaves the signed order-one step open. Check 1540 concerns straight products. The complex-zero argument in row 1290 uses a single varied link in a sewing kernel. I use its growth-bound method on simultaneous coarse-link circles. [Block design, §§3–4](gap-k2-tool-design-fable.md) · [Transverse covariance](gap-k2-tool-design-check-astra62.md) · [Classical limit](gap-k2-signed-readout-fable.md) · [Fixed-torus qualifications](gap-k2-signed-readout-check-astra62.md) · [Checkpoint](gap-k2-direction-checkpoint-check-astra62.md) · [Straight products](gap-mech-carry-astra62-check-opus.md) · [Earlier complex zero](gap-solve33-astra62.md)

## Two exact closure classes

**A. At every finite positive coupling, the linear exponential soft bond kernel of $Q_2$ cannot return a nonconstant gauge-invariant density with a globally entire action.** A finite sum of Wilson loops or spin networks giving the exact action would have to be constant, whatever their lengths and spins. Even the constant option fails for an exact two-period Wilson step with a common pressure per site.

**B. Fix any $a>0$ and use $Q_2$ at strength $\kappa=a\beta$.** On an untwisted torus with $N\ge4$ coarse time slices and first coarse spatial period divisible by four, there are two coarse spatial bonds at cyclic time distance at least $\lfloor N/2\rfloor-1$ whose conditional mutual information given all other coarse bonds is positive, for every $\beta>0$ outside a **finite** set depending on the torus and $a$. Other coarse spatial periods are at least two. In particular, a sum of potentials of fixed temporal range on the coarse bonds alone cannot represent this step throughout any open order-one coupling interval on the seed geometries. The potentials may be arbitrary functions and may extend across the entire spatial torus. The same distant pair rules out strictly finite temporal support for the posterior score weights, even almost surely under the blocked law.

These exclusions concern exact coarse densities. The signed renormalization step needed for the gap remains open.

The upstream text is by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at 31a47c543775. Outline GL3 and GL8 give the one-bond coefficients and periodic transfer trace. CF5 is the plain-average gradient identity for their centered map. CA-I 49495–49515 states an application condition for a free-current operator theorem. The order-one conclusions below use the corner map of row 1468. [Outline, lines 2197–2231](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2197) · [GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315) · [CF5](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L8474) · [CA-I, scope](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L49495)

## A. Entire coarse actions

Let $E$ be the bonds of a finite coarse graph without self-loops, with independent normalized Haar reference measure. Write $SU(2)$ as the unit quaternions. Consider the unnormalized image

$$
 D(V)=\int \exp\!\left(\sum_{e\in E}\kappa_e M_e(W)\cdot V_e\right)d\eta(W),
 \qquad |M_e(W)|\le1,\quad 0\le\kappa_e<\infty .
$$

Here $\eta$ is a finite nonzero positive measure and the dot denotes the real four-dimensional inner product. For $Q_2$, $M_e$ averages its 384 contour holonomies, the dot is $\operatorname{Re}(M_eV_e^{-1})$, and $\eta$ contains the fine Wilson density and the reciprocal of every bond normalizer. Those normalizers depend only on $W$. The image is invariant under vertex gauge transformations, by extending a coarse gauge change to the fine vertices and changing integration variables. For the theorem only gauge invariance of $D$ is required.

Fix arbitrary real base links $U_e$ and unit imaginary quaternions $X_e$. Put $V_e(\theta)=U_e(\cos\theta_e+X_e\sin\theta_e)$. Complexify the *linear* dot product by bilinear extension. The integral defines an entire function $F(\theta)$ on $\mathbb C^E$, positive on $\mathbb R^E$. Indeed, with $K=\sum_e\kappa_e$ and $C=\log\eta(1)$, it obeys

$$
 |F(\theta)|\le \exp(C+K\cosh R),\qquad \max_e|\operatorname{Im}\theta_e|\le R.       \tag{1}
$$

The real part of each continued $V_e(x+iy)$ is $\cosh(y)V_e(x)$. This gives (1) and compact uniform domination for holomorphy.

Suppose this $F$ has no complex zero. It has an entire logarithm $H$ on the simply connected angle space, real on the real axes. Its $2\pi$-periodicity in each angle follows there from positivity and everywhere by analytic continuation. Let $h_m$ be its Fourier coefficients on the real torus. For $m\ne0$, shift by $iRs$, where $s_e=\operatorname{sgn}(m_e)$. Contour shifting multiplies the $m$-coefficient of $H$ by $e^{-R m\cdot s}$. Since $h_{-m}=\overline{h_m}$, the coefficient of the real part on the shifted torus is $h_m\cosh(R\|m\|_1)$. Its mean remains $h_0$. The nonnegative function $C+K\cosh R-\operatorname{Re}H(\theta+iRs)$ bounds each of its Fourier coefficients in modulus by its mean. Thus

$$
 |h_m|\cosh(R\|m\|_1)\le C+K\cosh R-h_0.                                      \tag{2}
$$

Letting $R$ increase kills every mode with $\|m\|_1>1$. For a remaining nonconstant mode $m=\pm\mathbf e_j$, apply the vertex gauge change $-1$ at one endpoint of bond $j$. This shifts every incident real angle by $\pi$. It preserves the real logarithm and reverses the sign of that mode. Thus $h_{\pm\mathbf e_j}=0$ as well. Fourier uniqueness makes $F$ constant on this real torus.

Any two real link configurations belong to such a product of circles, by the quaternion axis-angle representation on each bond. Consequently every nonconstant gauge-invariant image has a complex zero on at least one such product. An action whose restriction to every complex angle space is entire would give a zero-free exponential there by analytic continuation. Finite spin-network actions have exactly this extension, since representation matrices of $SU(2)$ on link circles have finitely many integral frequencies and contractions and products preserve this property.

**Application to the two periods.** Suppose on the untwisted tori at $v=u,2u$ an exact step returns

$$
 D_v(V)=\exp\{cN_v+H_v(V)\},\qquad H_v(\mathbf1)=0 ,
$$

where the coarse graph has no self-loops, $N_v$ is the number of coarse sites, $c$ is common, and both $H_v$ extend as above and are real on real fields. Part A forces $H_v=0$. Bondwise normalization and Fubini give $\int D_v=Z^0(v)$. Since $N_{2u}=2N_u$, this would give $Z^0(2u)=Z^0(u)^2$.

The Wilson transfer operator gives a strict inequality.

$$
 \bigl(\operatorname{Tr}T^u\bigr)^2-\operatorname{Tr}T^{2u}
       =\sum_{i\ne j}\lambda_i^u\lambda_j^u>0.                                 \tag{3}
$$

On gauge-invariant states the one-step operator is the tensor product of electric convolutions sandwiched by the positive spatial half-weights, up to normalization. Each one-link spin eigenvalue $2e^{-\beta}I_{2j+1}(\beta)/\beta$ is strictly positive by its positive power series. Thus the positive trace-class transfer is injective there. The constant and the real trace of a contractible plaquette are linearly independent states, including in the centre-neutral sector. This proves (3) and also gives $P_K<1$ at finite positive coupling. The contradiction already uses the untwisted pair. An independent scalar for each torus could retain its mass even with a constant field density. A finite character expansion of the *density* is a separate hypothesis from a finite expansion of the action.

## B. Temporal range of the full image

Here $D_\beta=Q_{2,a\beta}\exp(-\beta S_W)$ and $F_\beta=-\log D_\beta$. An action of temporal range $R$ is a sum of functions on sets of coarse bonds whose base times have pairwise cyclic distance at most $R$. One may add any torus-dependent constant. This definition places no smoothness, spin, spatial range, coefficient or translation-invariance restriction on the summands. All coarse bond variables, including the temporal bonds, are kept.

**Fixed-torus input.** Use the fixed-torus part of Proposition L of row 1479 with the qualifications in check 1483. Near $V=\mathbf1$, vacuum-subtracted $F_\beta/\beta$ converges as $\beta\to\infty$ to the classical minimum

$$
 E_a(V)=\min_W\left\{S_W(W)+a\sum_c
           \bigl(|M_c(W)|-M_c(W)\cdot V_c\bigr)\right\},\qquad E_a(\mathbf1)=0 .
$$

Its Hessian has quadratic energy

$$
 \frac12\min_A\{\|dA\|^2+a\|QA-v\|^2\}.                                        \tag{4}
$$

Here $v,A$ are the coarse and fine link variations in one colour, with counting inner products, and $Q$ is the linear contour average. The bond normalizer accounts for $|M_c|$. At the trivial field it cancels the contour dispersion from the quadratic tie. In the block tree gauge a flat field with all coarse transports trivial has trivial torus holonomies and is the identity. In the linear kernel, $dA=0$ and $QA=0$ kill all periods, and the remaining gradient with constant values on coarse bases is removed by the tree gauge. This is the nondegenerate saddle used in (4). Rectangular periods only change the momentum grids and the lengths of the fundamental cycles in this argument. The range obstruction uses pointwise convergence at four fixed real fields. [Proposition L](gap-k2-signed-readout-fable.md) · [Fixed-volume saddle and Hessian](gap-k2-signed-readout-check-astra62.md)

**Two spatial aliases.** Use time direction 0 and spatial directions 1, 2, 3. Take $p=(q,\pi/2,0,0)$, $q=2\pi k/N$, with polarization along direction 2. Set $d=4$ and $\gamma=4/2^d$. In check 1469 the squared straight-average factor for a fine momentum $k'$ over $p$ is $\prod_i |(1+e^{ik'_i})/2|^2$. The endpoint legs contribute a coarse gradient. The transverse projection fixes the chosen polarization since $p_2=0$. The projection also fixes direction 2 after multiplication by the diagonal segment factor. Thus this polarization is an eigenvector of the coarse covariance, including the soft noise $a^{-1}$, and the reciprocal eigenvalue gives the Hessian in (4). In directions 2 and 3 only the zero alias survives. The length-two straight segment gives the numerator $4$ and the Fourier cell volume gives $2^{-d}$. In directions 0 and 1 the possible fine cosines are $\tau c$ and $\sigma/\sqrt2$, where $c=\cos(q/2)$ and $\tau,\sigma\in\{-1,1\}$. Thus the pushforward of the fine covariance along the polarization is

$$
 \begin{aligned}
 G(z)&=\gamma\sum_{\sigma=\pm1}w_\sigma
                 \sum_{\tau=\pm1}\frac{1+\tau c}{2(A_\sigma-2\tau c)}
       =\gamma\sum_{\sigma=\pm1}w_\sigma\,
                 \frac{A_\sigma+1+z}{2(t_\sigma-z)},\\
 z&=\cos q,\quad w_\sigma=(1+\sigma/\sqrt2)/2,\quad
 A_\sigma=4-2\sigma/\sqrt2,\quad t_\sigma=(A_\sigma^2-2)/2 .
 \end{aligned}                                                                     \tag{5}
$$

Indeed the inner sum is $(A_\sigma+2c^2)/(A_\sigma^2-4c^2)$ and $2c^2=1+z$. This evaluates the off-axis formula on file. At spatial momentum zero the same calculation gives $G(z)=(3+z)/(8(1-z))=1/[2(1-z)]-1/8$ in four dimensions, agreeing with the axial result, including its exceptional tuning $a=8$. [Check 1469, transverse symbol](gap-k2-tool-design-check-astra62.md)

The actual Hessian eigenvalue of the classical step is $h(z)=[a^{-1}+G(z)]^{-1}$. Both weights in (5) are positive and $1<t_+<t_-$. Write

$$
 a^{-1}+G(z)=a^{-1}-\gamma/2+
       \sum_{\sigma=\pm1}\frac{r_\sigma}{t_\sigma-z},
 \qquad r_\sigma=\gamma w_\sigma(A_\sigma+1+t_\sigma)/2>0.                      \tag{6}
$$

On $(t_+,t_-)$ the right side increases strictly from $-\infty$ to $+\infty$. Its zero gives a genuine pole of $h$ for **every** $a>0$. On $[-1,1]$ all sampled denominators are positive by the original covariance expression. As a rational function $h$ has numerator and denominator of degree at most two. This pole tests compact temporal support of the classical kernel.

**A finite torus forces a distant pair.** Put $m=\lfloor N/2\rfloor$. Suppose all direction-2 Hessian entries between bonds at time distance greater than $m-2$ vanish. Fourier transformation in space at the specified spatial momentum would then give $h(\cos q)$ as a Laurent polynomial in $e^{iq}$ with frequencies in $[-(m-2),m-2]$ on the temporal grid, by translation invariance of the classical Hessian. Averaging the two expressions at $q,-q$ gives a polynomial in $\cos q$ of degree at most $m-2$, because the samples of $h$ are even. There are $m+1$ distinct samples of $\cos q$. Clearing the denominator of $h$ makes the difference a polynomial of degree at most $m$. It would vanish identically, contradicting (6). Some individual pair of spatial bonds $e,f$ at cyclic time distance at least $m-1$ therefore has a nonzero mixed Hessian entry. This argument permits the coefficients to depend on the torus size.

Vary just $e,f$ in the chosen colour near $\mathbf1$. Choose small fixed real increments with nonzero rectangular difference $\delta=\Delta_{ef}E_a$. Such increments exist by integrating the continuous, nonzero mixed derivative over a sufficiently small rectangle. The difference uses the values at both increments, at each increment separately, and at neither. For the same four coarse configurations let $B(\beta)=\Delta_{ef}F_\beta$. On this fixed torus,

$$
                         B(\beta)/\beta\longrightarrow\delta\ne0.               \tag{7}
$$

For each fixed real coarse field $F_\beta(V)$ is real analytic in $\beta$, including at zero. Around any real $\beta_0$, the bond normalizers $Z_c(a\beta t)$, $0\le t\le1$, stay uniformly away from zero in a small complex neighbourhood, by positivity on the real compact set and continuity. The finite-dimensional integral is holomorphic there, and its positive real value admits a local logarithm. Thus $B$ is a nonzero real analytic function. Its zeros cannot accumulate at zero or at an interior point, and (7) bounds them from above. The exceptional set of positive couplings is finite.

For an action of range $R\le m-2$ every summand misses at least one of $e,f$. Its rectangular difference is zero. Consequently for any such action $L$,

$$
                     \|F_\beta-L\|_\infty\ \ge\ |B(\beta)|/4 .                  \tag{8}
$$

This also holds in essential supremum norm. The same cancellation holds for almost every choice of the common other bonds and the four endpoint values. A neighbourhood of the chosen rectangle has positive product Haar measure and the difference of $F_\beta$ is continuous. On a fixed torus (8) is at least $|\delta|\beta/8$ for all sufficiently large $\beta$.

**How accurately can a finite-range quadratic action approximate (4)?** There is a lower bound with constants independent of the torus. Let $t_*$ be the zero in (6), $w_*=t_*-\sqrt{t_*^2-1}\in(0,1)$, and write $h=U/D$ using

$$
 U(z)=(t_+-z)(t_--z),\qquad
 D(z)=(a^{-1}-\gamma/2)U(z)+r_+(t_--z)+r_-(t_+-z).
$$

Then $D(t_*)=0$ and $U(t_*)\ne0$. For any matrix $H_R$ on coarse bond variations with temporal range $R$, if $N>2R+4$,

$$
 \|D^2E_a(\mathbf1)-H_R\|_{\rm op}
 \ \ge\ C(a)w_*^{R+2},\qquad
 C(a)=\frac{(1-w_*)|U(t_*)|}{\max_{-1\le z\le1}|D(z)|}>0.                    \tag{9}
$$

Use the counting $\ell^2$ norm. Averaging $H_R$ over coarse translations preserves temporal range and can only decrease its error. On the chosen spatial polarization the diagonal matrix element in a unit Fourier vector is then a temporal Laurent polynomial of degree at most $R$. Averaging its values at $q,-q$ gives a polynomial $P(\cos q)$ of degree at most $R$ with grid error at most the original operator error $\epsilon$.

Put $L=R+2$, $J(z)=U(z)-D(z)P(z)$ and $S(w)=w^L J((w+w^{-1})/2)$. The degree of $J$ is at most $L$, so $S$ is an ordinary polynomial of degree at most $2L$. On the $N$th roots of unity its modulus is at most $\epsilon\max_{[-1,1]}|D|$. Since $N>2L$, discrete Fourier inversion expresses every coefficient of $S$ as an average of those values times phases. At $w_*$ this gives

$$
 w_*^L|U(t_*)|=|S(w_*)|
 \le \epsilon\,\max_{[-1,1]}|D|\sum_{j=0}^{2L}w_*^j
 \le \epsilon\,\max_{[-1,1]}|D|/(1-w_*).
$$

This proves (9). By the fixed-box $C^2$ version of Proposition L, (9) also bounds from below the $\liminf_{\beta\to\infty}$ of the distance of $\beta^{-1}D^2F_\beta(\mathbf1)$ from these matrices on each such torus. Only this last statement uses convergence of derivatives. Its order of limits gives no crossover estimate at growing $N$.

**What a typical coarse field retains.** Write $\mu$ for the normalized image and $\mu^V$ for the fine law conditioned on the observed coarse field. Differentiate in direction $V_c\exp(tX)$ for the chosen unit colour $X$, writing $\partial_c$ for this derivative, and put $S_c^X=\kappa M_c(W)\cdot(V_cX)$. For $e\ne f$ the normalized exponential kernel gives

$$
 \partial_e\partial_f F_\beta(V)
       =-\operatorname{Cov}_{\mu^V}(S_e^X,S_f^X).                               \tag{10}
$$

Each derivative of the log integral inserts its score, and the score at $e$ is independent of $V_f$ at fixed fine field. This is the polarized form of LD-1. For any $\beta$ outside the finite exceptional set, integration of the left side over the rectangle in (7) gives $B(\beta)\ne0$. That derivative is real analytic on the connected coarse configuration manifold, hence nonzero almost everywhere. To see the null-set assertion, at any zero a nonidentically zero analytic function has a derivative of least nonzero order. The zero stratum with that choice of order and multi-index lies locally on the regular zero hypersurface of a derivative of one lower order. Countably many coordinate patches, derivatives and local neighbourhoods suffice. Haar volume is smooth there, and $\mu$ has strictly positive density. Thus the covariance in (10) is nonzero for $\mu$-almost every $V$. [Row 1460, LD-1](gap-crux-direction-fable.md)

This rules out the **strictly finite-range version** of the posterior comparison (H2) in registry trigger R10. At each admissible $V$, (H2) bounds $|\operatorname{Cov}_{\mu^V}(g,S_f)|^2$ by $\mathbb E_{\mu^V}\sum_\ell\gamma_{f\ell}|\nabla_\ell g|^2$ for every smooth fine test $g$, where $S_f$ is the tangent score. Take $g=S_e^X$. Its fine gradients are supported on the set $B_e$ of bonds in the contours of $e$. Because $e$ is spatial, each such bond has fine base time $2t_e$ or $2t_e+1$, hence coarse time $t_e$. A contour has at most ten steps. Each occurrence of a varied link contributes at most one to the directional derivative of its holonomy in unit-quaternion norm. Therefore $|\nabla_\ell g|\le10\kappa$, and (H2) would require

$$
 \mathbb E_{\mu^V}\sum_{\ell\in B_e}\gamma_{f\ell}
   \ \ge\ \frac{|\operatorname{Cov}_{\mu^V}(S_e^X,S_f^X)|^2}{100\kappa^2}>0
                  \quad\text{for }\mu\text{-almost every }V.                   \tag{11}
$$

Weights supported within $m-2$ coarse time steps of $f$ violate (11). This includes $a=1$ on the order-one interval $[2,3]$ outside the finite exceptional set for each torus. R10 itself asks for exponential decay of the *mean* weights. Arbitrarily small positive long-distance weights are compatible with (11). [Existing posterior inequality and R10, §§4.1–4.2](gap-seed-solve-fable.md)

For $C$ the collection of bonds other than $e,f$, a positive conditional product density at fixed $C$ has identically zero mixed log derivative. This follows even for a measurable factorization by taking rectangular differences almost everywhere and then using continuity of the actual conditional density. By (10) and Fubini, conditional factorization fails for almost every $C$. Hence $I_\mu(V_e;V_f\mid C)>0$. In particular, for every probability density $\nu$ coming from an action of range $m-2$,

$$
                       D_{\rm KL}(\mu\|\nu)\ \ge\ I_\mu(V_e;V_f\mid C)>0 .
$$

Factor $\nu$ into its marginal on $C$ and its two conditional marginals. Expansion gives the conditional information plus the divergence of the $C$ marginals and the two mean conditional marginal divergences. Neither (10) nor this entropy argument bounds the size of the dependence uniformly in $N$ in an order-one band.

## What these obstructions say about the seed

For the release witnesses $b,g_0$ and $\ell\in1024\mathbb N$, put $n=\ell b^K$ and $u=n/512$. The seed asks for $P_K=Z_+(2u)/Z_+(u)^2\ge457/625$ on infinitely many calibrated cutoffs for one $\ell,g_0$, where $Z_+(v)$ averages the eight centre-twisted masses. At all sufficiently large $K$, both side-two coarse tori satisfy the period assumptions of B. For fixed $a$, their exceptional sets have countable union over $K$. Thus almost every *fixed* coupling in any open order-one interval requires range at least $\lfloor v/4\rfloor-1$ on each of the two images, $v=u,2u$. The exceptional sets can vary with $K$, so B alone makes no such assertion at the particular sequence $\beta_K$. Theorem A applies to each $\beta_K>0$ with any finite soft strength.

The regimes can be separated within pure Wilson theory on these same geometries. For each $K$, the neutral purity tends to one as $\beta\downarrow0$, by continuity of the sixteen finite Haar integrals, all equal to one at zero. It tends to zero as $\beta\to\infty$ with this geometry held fixed, by the fixed-box result in check 1527(iii) from row 1143. For each sufficiently large $K$ one can therefore choose two positive couplings, avoiding the two finite exceptional sets, with $P>1-1/K$ and $P<1/K$, respectively. Both exclusions hold along both sequences. These are deliberately uncalibrated Wilson couplings. They show exactly why an obstruction to these representations cannot serve as a purity criterion. [Fixed-box partition estimate, Eq. (4)](gap-solve-astra62.md) · [Conversion to neutral purity, check 1527(iii)](gap-agy-seed-approaches-neon-check-astra62.md)

For compact $U(1)$ the cosine soft tie has (1) and the vertex transformation $-1$ has the same parity action. In five-dimensional $SU(2)$ both facts still hold. In (5) the free transverse polarization is already abelian. A fifth direction with zero external momentum kills its extra nonzero alias and changes $\gamma$ from $1/4$ to $1/8$. Both residues in (6) stay positive. The flat saddle argument still fixes all torus periods in either comparison model, and the same finite-volume analyticity applies. The two obstructions therefore have **no group or dimension selectivity for a positive mass-gap proof**.

The open step is row 1468, §4.3. For some $a,r,\delta_0>0$, the proposed classes $\mathcal T_k$ of actions with summable interactions must satisfy, throughout the order-one band on all sixteen tori,

$$
 Q_{2,a x_k}\mathcal T_k\subseteq\mathcal T_{k+1},\qquad
 x_{k+1}\le x_k-\delta_0,\qquad
 \rho_{k+1}\le\bar\rho(x_{k+1}),\qquad
 \eta_{k+1}\le\eta_k+|\Lambda|e^{-r s/8}.
$$

Here $x_k$ is the class centre's transverse readout, $\rho_k$ its radius, $\eta_k$ its wrap-error allowance, and $s$ the shortest side of the torus $\Lambda$. The design permits both tails and error. Equations (2) and (7)–(11) give no uniform bound on the contribution of those tails to the two-period ratio and no signed decrement. I cannot establish a selective sufficient condition from them. The new arguments are hand proofs without independent review or Lean verification. No computation is used as a proof step. [Existing step and end conditions](gap-k2-tool-design-fable.md)

RESULT Two classes of exact soft-block closure are excluded. Entire coarse actions force a constant density, and for each fixed strength ratio the side-two Wilson image on a torus of coarse time period $N$ requires temporal range at least $\lfloor N/2\rfloor-1$ outside a finite coupling set for that torus. The selective order-one step, (PUR-io), and the mass gap remain open.
