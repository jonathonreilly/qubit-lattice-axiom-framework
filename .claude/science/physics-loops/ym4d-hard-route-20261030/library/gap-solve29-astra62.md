# Repo search

**GUIDE.** Row 1254 at `7fc2b2235`. The lead’s November 8 search points to PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149, where a one-step contraction holds up to parameter $1/32$. I also checked Grok’s PR 10133 crossover reduction, lines 77–86, which assumes clustering and source transport, PR 10134’s `mass-gap-interface.md`, which distinguishes an excitation from a positive spectral threshold, and PR 10141’s `fp1.md`, lines 299–315, which treats a constrained classical minimizer.

**GUIDE.** On main at `8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md`, lines 305–329, requires both spectral and state-counting estimates. Row 1246, (27), identifies the finite-cube neutral spectral edge and leaves its uniform physical decay open. Row 1218 supplies the published coarse-path estimate used below. The row-specific prior file is absent at the pinned revision. I found no open-registry assignment for the fine-cube comparison (37).

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish the scalar observable sector, the block resolvent, and the infrared spectral question. I followed their outline index to lines 581–599, 773–780 and 31858–31882 at `31a47c543775`. CA-I lines 2704–2712 and 3213–3222 expressly exclude a mass-gap assertion. I use their scope distinction.

## What the scale comparison gives

**PROVED.** On the same fine Wilson torus, if a side-$s$ cube update has normalized Poincaré constant $v_s$, a side-$t$ update has constant at least $2^{-20}\min(1,(t/s)^2v_s)$ for $2\le s\le t$ and $2t+4\le N$. Equations (17)–(19) and (37) prove this using an inverse of the smaller-cube generator and the commutation of separated updates.

**OPEN.** On a diagonal of spacings $a_j$, a lower bound $v_{s_j}\ge c(a_js_j)^2$ would suffice if the local Wilson correlations converged to those of a nontrivial Yang–Mills theory on a dense set of states. Equations (30)–(33) allow some slow modes. For bounded functions of the straight-path transports, (36) verifies the condition, but the centered continuum vectors all vanish. The lower bound on surviving observables and the continuum construction are the outstanding steps.

## One periodic torus at each cutoff

**GUIDE.** Row 1218, `prior/gap-onebound-read-sol.md`, records the thermal-seed argument of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy, under their construction assumptions. The cube-dynamics paper by the first four authors gives a block Poincaré criterion for the fine law and a weak-coupling bound for the induced law of straight paths on a finite range of torus sizes.

**GUIDE.** Write B for Bhattacharjee, Bhattacharya, Lockwood and Romanov, *One Cube Estimate Implies the Yang–Mills Mass Gap*, v7. In the authors' TeX, lines 5850–6077 prove the finite-torus covariance estimate below. Lines 6078–6129 take a thermodynamic limit at each cutoff. Lines 12137–12144 and 12185–12200 explain the finite range of Corollary 166 and propose a finite-transfer-gap bridge for a joint limit. Row 1224 already read the finite-speed argument in the companion paper. Row 1222, `gap-solve24-astra62.md`, uses reflection interpolation after local sweeps. Here I apply that idea directly to the symmetric finite tori of B. The object to bound is a surviving local spectral measure.

**PROVED, conditional on the stated finite-torus input and matching.** Let the fine Wilson law at spacing $a_j$ be on a periodic $N_j^4$ lattice, $N_j$ even, $a_j\downarrow0$, $a_jN_j\to\infty$. Take integers $n_j\ge2$ with $N_j\ge2n_j+4$ and $a_j n_j\le\ell<\infty$. Suppose B's cube Poincaré inequality with a common constant $v>0$ holds on this one fine torus at each $j$. Its form is
\[
 v\operatorname{Var}(f)\le n_j^{-4}\sum_x\|f-P_x f\|_2^2 ,
 \tag{1}
\]
where $P_x$ conditions on the links outside the cube of base points $x+[0,n_j)^4$. The tests in (1) are real gauge-invariant functions. For each member of a total family of positive-time continuum vectors suppose there are matched bounded gauge-invariant insertions $F_j$ supported in a fixed physical box, with fine link supports $S_j$, such that
\[
 \log(2+\|F_j\|_\infty)+\log(2+|S_j|)=o(N_j/n_j).                 \tag{2}
\]
Matching means that the centered reflected two-insertion forms on this very diagonal converge at every positive physical padding to $C(t)=\langle u,e^{-tH}u\rangle$ for the corresponding vacuum-subtracted vector. Assume $H\ge0$ and that the centered vectors span densely in $\Omega^\perp$. Then on $\Omega^\perp$,
\[
                       H\ge \frac{16v}{625e^2\ell}.                    \tag{3}
\]

**PROVED.** Set $A_j=F_j-\mu_j F_j$ and $C_j(s)=\mu_j((\theta\overline{A_j})\tau_s A_j)$, with site reflection through time zero. Write $w_j=O(1/a_j)$ for the temporal extent from the plane. For nonnegative integers $r,t$ with $w_j+\max(r,t)<N_j/2$, reflection positivity gives a Gram matrix with entries $C_j(r+t)$. This follows by translating both entries of the inner product for $\tau_r A_j,\tau_t A_j$ by $r$. The even entries $C_j(2r)$ are nonnegative. Cauchy–Schwarz gives $C_j(2r)^2\le C_j(2r-2)C_j(2r+2)$. Therefore, for even $u\le s\le T$ in this range,
\[
 C_j(s)\le C_j(u)^{1-\alpha} C_j(T)^\alpha,\qquad
                    \alpha=(s-u)/(T-u).                              \tag{4}
\]
Here $u<T$. Zero values follow by adding a positive constant to the Gram kernel and letting it tend to zero.

**PROVED, using B's finite-volume covariance theorem as a cited input.** Choose $T_j=2\lfloor N_j/8\rfloor$. Eventually $w_j=o(N_j)$, so the wrapped distance between the two supports at $T_j$ is at least $T_j-O(1)$. In B's theorem let $k=\lfloor(d+2)/n_j\rfloor-2$ and $q_n=(2+1/n)^4\le625/16$. The absolute covariance is at most
\[
 4\|F_j\|_\infty^2
 \left(e+\frac{k|S_j|^2}{64e^2}\right)
                  \exp[-v k/(e^2q_{n_j})].
\]
The factor four allows complex insertions. The centered correlation is precisely this covariance. We have $k\ge T_j/n_j-O(1)$, $k=O(T_j/n_j)$ and $T_j/n_j\to\infty$. By (2) the logarithm of the prefactor is bounded above by $o(T_j/n_j)$. Consequently $\limsup_j (a_jT_j)^{-1}\log C_j(T_j)\le-16v/(625e^2\ell)$, allowing $\log 0=-\infty$.

**PROVED.** Choose even $u_j,s_j$ with $a_ju_j\to\epsilon$, $a_js_j\to t$, where $0<\epsilon<t$. In (4), $\alpha_j\to0$ and $\alpha_j a_j T_j\to t-\epsilon$. The matched $C_j(u_j)$ have a finite limit. Thus $C(t)\le C(\epsilon)\exp[-16v(t-\epsilon)/(625e^2\ell)]$. If the spectral measure of $u$ gave positive weight to $[0,E]$ for $E<16v/(625e^2\ell)$, that weight times $e^{-tE}$ would contradict this inequality for large $t$. Taking the closure of the span of the centered vectors proves (3) and simplicity of the vacuum in this representation.

**PROVED.** For example, let $a_j=a_0 2^{-j}$, $n_j=n_0 2^j$, $N_j=2^j L_j$, and take $L_j$ to be the least even integer at least $j^2$. Polynomially bounded insertions in fixed physical boxes satisfy (2), since their logarithmic price is $O(j)$ and $N_j/n_j=L_j/n_0$. Eventually $2n_0+4\le L_j\le\exp(2^j/(17j))$, because $\log(j^2+2)=o(2^j/j)$. For $0\le\beta_{W,j}\le j+2$ these tori are within B's straight-path range. Equation (3) would apply if the fine estimate were supplied and the continuum observables matched on this diagonal. Its proof gives a bound on the continuum spectrum. It makes no assertion about invisible eigenvectors of each finite-time torus. [B, v7](https://hexagonmath.org/2610.00341v7)

## Conditioning the fine Wilson law on specified path products

**GUIDE.** B, lines 11959–12014 and 12039–12079, integrate the interiors of long straight paths. Row 1222, (4), already compares polynomially bounded observables after prescribing the path products. I use the same conditional law. The issue here is an inequality for every square-integrable test of the fine cube dynamics, including functions concentrated on sets of arbitrarily small probability.

**PROVED (comparison of marginal laws).** Work on a fine periodic $(bL)^4$ torus with $b\ge4$ and $L\ge3$. For each of the $M=4L^4$ straight coarse links let $C_e$ be the ordered product of its $b$ fine links. Let $I$ consist of the $b-2$ interior links on every path. Write $W$ for the array of all other fine links. Denote its marginal under the Wilson law $\mu$ by $\zeta$. At any specified coarse field $c$, denote the canonical constrained law by $\mu_c$ and its $W$-marginal by $\zeta_c$. B's path-interior lemma shows that, given $W$, the individual links of $I$ are independent. The product densities $p_e(g\mid W)$ relative to probability Haar obey
\[
 1-\eta\le p_e\le1+\eta,\qquad
 \eta=48(1+6\beta_W)^{3/2}
       \left(\frac{4\beta_W}{1+4\beta_W}\right)^{b-4}.                \tag{5}
\]
Only the range $b>4$, $\eta<1$ will be used. The estimate follows in B by bounding the first and last convolution factors in $L^2$ and contracting the mean-zero part through each intervening factor. Their one-link character calculation agrees with the Wilson convolution in Sussman and Alpoge, outline GL3. Conditional independence gives
\[
 \frac{d\zeta_c}{d\zeta}(W)
       =\frac{\prod_e p_e(c_e\mid W)}{\int\prod_e p_e(c_e\mid W')\,d\zeta(W')},
 \qquad
 \frac{\inf(d\zeta_c/d\zeta)}{\sup(d\zeta_c/d\zeta)}
       \ge \theta:=\left(\frac{1-\eta}{1+\eta}\right)^M .            \tag{6}
\]
The infimum and supremum may be essential. Conditional path laws at every $c_e$ can be defined by solving for one interior link and using Haar invariance. All normalizers are positive. Under $\mu_c$ and given $W$, the interior arrays of the different paths are still independent. Each path law then depends only on its endpoints' links, its staples in $W$, and its specified product.

**PROVED (eliminating private variables in a cube estimate).** For a law $\rho$ and cube side $m$, write $\mathcal E_m^\rho(f)=m^{-4}\sum_z\|f-\mathbb E_\rho[f\mid\text{links outside }V_m(z)]\|_2^2$. For a law on $W$ only retain the $W$ links outside the cube when taking this conditional expectation. Let $g=\mathbb E_\rho[f\mid W]$, $\pi=\rho_W$, and take $m=s+2r$ below half the torus side. Then
\[
 \mathcal E_m^\rho(f)\ \ge \gamma\|f-g\|_{L^2(\rho)}^2+(s/m)^4\mathcal E_s^\pi(g) .              \tag{7}
\]
For the unconditioned Wilson law take $r=1$, $\gamma=1$. For $\rho=\mu_c$ take $r=b+2$, $\gamma=1-b/m$. No bound on the size of $f$ other than $f\in L^2(\rho)$ is required.

**PROVED.** In the first case regard each interior link as one group. In the second take all private links on one path as one group. Given $W$ the groups form a finite product. For an outer cube $V_m(z)$ let $D$ be the sigma-field of $W$ and the complete groups that are not contained in this cube. It contains the fine exterior. Put $B=V_s(z+(r,r,r,r))$. A group with a private link outside the outer cube has its conditional law determined by $W$ outside $B$. Indeed each staple of a single link uses base points at distance at most one. In the path case all links and all staples needed for its conditional law lie within base-point distance $b+2$ of each of its private links. Product disintegration now implies conditional independence of the visible private exterior links and $W$ inside $B$, given $W$ outside $B$.

**PROVED.** The vectors
\[
 f-\mathbb E[f\mid D],\qquad
 h=g-\mathbb E_\pi[g\mid W\text{ outside }B]
\]
are orthogonal. Each is in the kernel of projection onto the fine exterior. For the second assertion about $h$, condition first on $W$ outside $B$ and use the preceding conditional independence. Both vectors have inner product with $f$ equal to their own squared norms. The squared fine-cube residual therefore dominates the sum of these two squared norms.

**PROVED.** On each product fibre over $W$, let $Q_i$ integrate group $i$. The projections $Q_i$ commute. Expanding $\prod_i[Q_i+(1-Q_i)]$ breaks $f$ into orthogonal terms indexed by the set of factors $1-Q_i$. The constant term is $g$. A nonconstant term contributes to the first squared norm above whenever $V_m(z)$ contains at least one group from its index set. Every single link belongs to $m^4$ cubes. A path's private links occupy $b-2$ consecutive base points on one line. At least $m^3(m-b)$ cubes contain the whole group. Summing over $z$, dividing by $m^4$, and integrating over $W$ gives the first term in (7). Each inner cube is counted once as $z$ varies. This gives the second term.

**PROVED (gauge averaging for the fine heat bath).** If the full Wilson law satisfies (1) on the invariant subspace at side $s\ge2$, its cube inequality on *all* $L^2$ functions has constant at least
\[
                        \min\{v,(1-1/s)^4\}.                            \tag{8}
\]
For every vertex $y$ let $G_y$ average the gauge rotation at $y$ with Haar measure. These are commuting orthogonal projections. Their product $G$ projects onto the invariant functions. Every exterior projection commutes with $G$ since the Wilson law and the exterior sigma-field are gauge invariant. Hence the cube form splits on the range and kernel of $G$. If $y\in z+\{1,\ldots,s-1\}^4$, all incident links are inside the cube. The exterior is pointwise fixed by rotations at all such vertices. Its squared residual dominates that for the product of their $G_y$. Expand in the joint projections $G_y,1-G_y$ as above. Each nonempty vertex index set meets the interior of at least $(s-1)^4$ cubes. This proves (8) after summation. The argument uses gauge invariance of the original law.

**PROVED (two directions for the actual Wilson cube gaps).** Fix any $c$, for instance all straight-path products equal to the identity. A “constant $v$ at side $s$” means a lower bound in the Poincaré inequality with variance on the left and $\mathcal E_s$ on the right. In both directions all displayed cubes fit with side below half the period.

1. If $\mu_c$ has constant $v$ at side $s$ on restrictions of full-gauge-invariant functions of $W$, then the ordinary Wilson law has constant
\[
         \min\{1,\ \theta (s/(s+2))^4 v\}                             \tag{9}
\]
at side $s+2$ on all gauge-invariant functions of the fine lattice.
2. Conversely, if the ordinary Wilson law has invariant constant $v$ at side $s$, then $\mu_c$ has constant
\[
 \min\{1-b/m,\ \theta(s/m)^4\min(v,(1-1/s)^4)\},\qquad
                        m=s+2(b+2),                                    \tag{10}
\]
on all its $L^2$ functions. Both constants are uniform in the prescribed field $c$.

**PROVED.** For a test depending on $W$, the fine exterior supplies at least the information in the $W$-exterior. Thus $\mathcal E_s^\rho(g)\le\mathcal E_s^\pi(g)$. A cube inequality for $\rho$ passes to its marginal on the indicated tests. If $l\pi\le\pi'\le u\pi$, any cube inequality for $\pi'$ transfers to $\pi$ with loss $l/u$. Indeed both variance and each conditional variance are infima of mean square error over constants or exterior-measurable functions. The same loss works in the reverse direction. Use (6) for $l/u$. For (9), $g=\mathbb E_\mu[f\mid W]$ for invariant $f$ is invariant. One can average a representative over the compact gauge group, and (6) makes exceptional $W$ sets negligible under either marginal. Use the transferred marginal inequality in (7) at $r=1$ and add the two orthogonal variances of $f$. For (10) first apply (8). The original marginal inequality then holds on all tests. Transfer it to $\zeta_c$ and apply (7) at $r=b+2$ to the constrained law.

**PROVED.** On the entire window $b=2^j$, $\beta_W\le j+2$, $L\le\exp(b/(17j))$, the factor $\theta$ tends to one uniformly as $j\to\infty$. In fact
\[
 \log(M\eta)\le O(\log(2+j))+
         \frac{4b}{17j}-\frac{b-4}{4j+9}.
\]
Here $\log(1-x)\le-x$ applies to (5). For $j\ge72$, $1/(4j+9)-4/(17j)=(j-36)/(17j(4j+9))\ge1/(170j)$. Hence $M\eta\to0$ and $|\log\theta|\le4M\eta$ eventually. For $s\ge c b$, with fixed $c>0$, the comparison constants in (9)–(10) stay positive for a common input $v>0$. When $ab$ is bounded, the increase in physical update size in (10) is at most $2ab+4a$. This covers $s=n_0b$ with fixed $n_0\ge2$ on the diagonal above. For $s/b\to0$, the displayed proof of (10) loses the factor $(s/m)^4$.

## Relaxation of the pinned path interiors

**PROVED.** Even for $m\ll b$, the part of the constrained law corresponding to the private links has a uniform cube estimate. Put $r=\lceil12(1+6\beta_W)\rceil$. For $m\ge8r+8$, $m<N/2$ and $N=bL$, every $c,W$ satisfies
\[
 \frac{1}{m^4}\sum_z
 \mathbb E\!\left[\operatorname{Var}
   (f\mid W,c,I\text{ outside }V_m(z))\mid W,c\right]
       \ \ge\ \tfrac12\operatorname{Var}(f\mid W,c).                   \tag{11}
\]
The left side uses the conditional fine law. Therefore the ordinary constrained cube form $\mathcal E_m^{\mu_c}(f)$ dominates $\tfrac12\|f-\mathbb E_{\mu_c}[f\mid W]\|_2^2$. The size in (11) counts fine links. The estimate holds for every coupling and every length of the prescribed paths.

**PROVED.** For one path, given $W$, the $d=b-2$ independent increments have densities given by left or right translates of Wilson one-link factors with parameters in $[0,6\beta_W]$. Fixing their product gives a bridge with fixed endpoints. Use the partial products as its $d-1$ internal site variables. The transition kernels preserve Haar in both directions. Row 1145, (1)–(2), bounds the density of the product of any $r$ consecutive increments between $1-\delta$ and $1+\delta$, where
\[
 \delta=\sum_{h\ge1}(h+1)^2 e^{-hr/(1+6\beta_W)}
 \le \sum_{h\ge1}(4e^{-12})^h < 1/128 .                                \tag{12}
\]
The same bound applies to the reversed kernels. That row uses the normalized GL3 of Sussman and Alpoge and a Bessel-ratio inequality. Successive fixed translations between central densities only translate the convolution. [Row 1145](gap-solve2-astra62.md)

**PROVED.** Resampling a consecutive interval of increments with the others and the total product fixed resamples its internal sites conditional on the two endpoint sites. Suppose only the left endpoint changes and that the interval has length $d'\ge r$. In the bridge density for the sites from step $r$ through the last internal site, only the transition density through the first $r$ steps and its normalizer depend on the left endpoint. Use as reference a Haar site at step $r$ followed by the remaining transitions conditioned on the given right endpoint. The reference is normalized since the kernels preserve Haar. Both densities lie between $(1-\delta)/(1+\delta)$ and $(1+\delta)/(1-\delta)$. They can be sampled equal with probability at least $1-4\delta/(1-\delta)$, by drawing from their common density minimum first. The case $d'=r$ has an empty tail and needs no coupling. Complete the first $r-1$ sites by their conditional laws. The expected number of newly differing internal sites is at most $r+4\delta d'/(1-\delta)$. For $d'<r$ the trivial count is enough. Reversing the bridge gives the same bound for a changed right endpoint.

**PROVED.** Choose one of the $N$ possible length-$m$ intervals of the containing coordinate circle uniformly. Intersect it with the private line segment. Since $b+m<N$, every nonempty intersection is one interval. Use Hamming distance on the internal sites. For two configurations differing at just one internal site, $m-1$ starts update it as an internal site and erase the difference by a common sample. Exactly two starts have it as an endpoint. Only those can create new differences. Therefore expected distance after one step is at most
\[
 1-\frac{m-1-2r-8\delta m/(1-\delta)}{N}
                         \ \le\ 1-\frac{m}{2N}.                         \tag{13}
\]
For the last inequality, $2r\le m/4-2$ and $8\delta/(1-\delta)<1/8$. A bounded function is Lipschitz in Hamming distance. The estimate for one differing site and a telescoping sequence of single-site replacements contract the Lipschitz seminorm by the right side of (13). Every internal tuple is allowed, since the increment densities are strictly positive. Iteration bounds the oscillation by the initial Lipschitz seminorm times the finite path diameter times $(1-m/(2N))^t$.

**PROVED.** The random-interval operator is an average of conditional projections, hence positive and self-adjoint. For a bounded centered test, its $L^2$ norm after $t$ steps is at most its oscillation. Its spectral measure cannot charge any closed interval above $1-m/(2N)$, by taking $t$th roots. Bounded centered tests are dense. Thus the one-path form normalized by $1/m$ has gap at least $1/2$. This calculation also covers a path with no internal degrees of freedom, for which the variance vanishes.

**PROVED.** Given $c,W$, the different path bridges are independent. A cube update projects by the tensor product of the corresponding interval projections. Decompose into the constant and centered subspaces of every path. Each cube preserves every such tensor subspace. In a subspace with at least one centered path, fix one such path $e$. The residual $1-\bigotimes_i P_{i,z}$ dominates $(1-P_{e,z})\otimes1$, since these projections commute on different factors. Each longitudinal start for $e$ occurs for $m^3$ transverse starts containing its line. Summing and dividing by $m^4$ gives at least $1/2$ on that subspace. This proves (11). The remaining part of the variance is $\operatorname{Var}_{\zeta_c}(\mathbb E[f\mid W,c])$, which (11) does not bound.

## Reducing the added width of a pinned update

**PROVED.** Let $B_z$ be the inner cube of side $s$, with an outer cube $V_m(z)$ of side $m=s+2h$, where $h\ge6$, $m<N/2$, and $m$ satisfies (11). For $g=\mathbb E_{\mu_c}[f\mid W]$ and centered $f$, put
\[
 d_h=\sum_{k\ge1}(k+1)^2e^{-k(h-3)/(1+6\beta_W)},\quad
 D_h=\frac{1+d_h}{1-d_h},\quad e_h=D_h^{2M}-1
\]
when $d_h<1$. Then
\[
 \sqrt{\mathcal E_m^{\mu_c}(f)}\ge
 \sqrt{\tfrac12\|f-g\|_2^2+(s/m)^4\mathcal E_s^{\zeta_c}(g)}
                       -e_h(N/m)^2\|f\|_2.                            \tag{14}
\]
Here $h$ may be much smaller than the path length $b$. In particular the extra physical update width in the reverse comparison can tend to zero even when $ab$ stays positive.

**PROVED.** Fix $z$. Denote the fine exterior sigma-field by $X$, the $W$-exterior of $B_z$ by $Y$. We first prove that for a function $u(W)$ with $\mathbb E[u\mid Y]=0$,
\[
                        \|\mathbb E[u\mid X]\|_2\le e_h\|u\|_2.         \tag{15}
\]
Given $W$, the visible private variables on different paths are independent. Call a path affected if an endpoint link or a private-link kernel on it can read $W$ inside $B_z$. Its line then has a path base point within one site of $B_z$. If any private link of this path lies outside the outer cube, exit must be longitudinal, since the transverse coordinates are constant. Between the base point just identified and the first such exit lie at least $h-3$ consecutive private links inside the outer cube. This bound allows one site for a staple and both endpoint links. Periodic wrapping causes no second crossing interval, since $b+m<N$.

**PROVED.** Given $W$, initially omit the product constraint on that path. The product law of its visible increments then depends only on $Y$. To restore the constraint, multiply their density by the density of the required product conditional on those visible increments, divided by the unconditional product density at that same value. Both lie between $1-d_h$ and $1+d_h$ by the convolution estimate (12) with $h-3$ steps. Extra independent increments and fixed left and right translations preserve these bounds. On untouched paths use the actual conditional law of the visible increments, which depends only on $Y$. Paths with no visible private links require no factor. Thus conditional on $W$ the private exterior has density between $D_h^{-M}$ and $D_h^M$ relative to a probability depending on $Y$ alone. Mixing over $W$ at fixed $Y$ preserves the bounds. Bayes' formula gives the posterior law of $W$ given $Y$ and the private exterior relative to its law given $Y$ with density ratio in $[D_h^{-2M},D_h^{2M}]$. Center $u$ at fixed $Y$ and apply Cauchy–Schwarz. This bounds its conditional mean in magnitude by $e_h(\mathbb E[|u|^2\mid Y])^{1/2}$. Projection back to $X$ gives (15).

**PROVED.** Put $D=\sigma(W,X)$, $k_z=\mathbb E[f\mid D]-\mathbb E[f\mid X]$ and $u_z=g-\mathbb E[g\mid Y]$. Then
\[
 \|u_z\|^2=\langle f,u_z\rangle
     \le(\|k_z\|+e_h\|f\|)\|u_z\|,
 \qquad
 \|f-\mathbb E[f\mid X]\|^2=\|f-\mathbb E[f\mid D]\|^2+\|k_z\|^2 .
\]
Use the real part for complex functions. The first bound uses (15) and $u_z\in L^2(D)$. In the sum normalized by $m^{-4}$, (11) pays for the first term on the right in the norm identity. The triangle inequality in the sum over $z$ bounds $(s/m)^2\sqrt{\mathcal E_s^{\zeta_c}(g)}$ by $(m^{-4}\sum_z\|k_z\|^2)^{1/2}+e_h(N/m)^2\|f\|$. Applying the Euclidean triangle inequality to these two variance terms gives (14).

**PROVED.** For example on the polynomial-size diagonal $a_j=a_0 2^{-j}$, $N_j=2^j L_j$ with $L_j$ the even side of order $j^2$ used above and $\beta_{W,j}=O(j)$, take $h_j=\lceil j^3\rceil$. Then $\log N_j=O(j)$, $M\le4N_j^4$, $d_{h_j}\le C\exp(-c j^2)$ and $e_{h_j}N_j^2\to0$. The last two assertions follow from the geometric sum in (12) and $\log D_h\le4d_h$ for $d_h\le1/2$. One can thus transfer a common positive marginal bound at $s_j$ with $a_js_j\to\ell_0>0$ to the full constrained law at side $s_j+2h_j$ with the same limiting physical size. This is uniform in the chosen product values. It still requires a positive marginal bound for the $W$ variables.

**PROVED (necessary width for the exterior-uniform claim).** The order $1+\beta_W$ in (11) cannot be reduced to $o(\beta_W)$ uniformly in the exterior. Take $W=1$, $c=1$, let $\beta_W\to\infty$ and $d=b-2$ with $d/\beta_W\to\infty$. Every private increment has six identity staples before imposing the product, so the path is the bridge of the homogeneous class kernel with parameter $B=6\beta_W$. For $2\le m=o(\beta_W)$ the conditional cube gap on this fibre is at most $C(m/\beta_W)^2$.

**PROVED.** Write $w(U)=\tfrac12\operatorname{tr}U$ and $\lambda=I_2(B)/I_1(B)$. We need $1-\lambda\le C/B$. In radial angle $t$ the Haar density is proportional to $\sin^2t$ on $[0,\pi]$. After removing $e^B$, the normalizer is at least $c B^{-3/2}$ by integrating $0\le t\le B^{-1/2}$, using $\sin t\ge2t/\pi$ there. The numerator for $1-\lambda$ is at most $C\int_0^\infty t^4e^{-2Bt^2/\pi^2}\,dt=C'B^{-5/2}$, since $2t^2/\pi^2\le1-\cos t\le t^2/2$ on $[0,\pi]$. In the stationary chain of partial products the first site is Haar, $Kw=\lambda w$ and $\int w^2=1/4$ by character orthogonality. Site covariance at distance $k$ is $\lambda^k/4$.

**PROVED.** Use $F=\sum_{d/3\le i\le2d/3}w(Z_i)$ on one path and call the number of summands $J$. On the segment from $\lceil d/5\rceil$ through $\lfloor4d/5\rfloor$ the bridge law is between $1/2$ and $2$ times the stationary segment law for all sufficiently large $d/\beta_W$. Its relative density is the incoming kernel times the outgoing kernel divided by the full bridge kernel at its endpoint. By (12) with the corresponding lengths, all three tend uniformly to one. This compares variances through the infimum over constants. The stationary sum has variance at least $c J\beta_W$ by retaining separations up to $c'\beta_W$ for which $\lambda^k\ge1/2$ and using $J/\beta_W\to\infty$.

**PROVED.** A length-$m$ move that touches the sum has a fixed left boundary site $Z_u$ in the comparison segment. Predict each updated summand by $w(Z_u)$ and keep the exterior summands. The mean square prediction error is at most
\[
 2m\sum_{k=1}^{m-1}\mathbb E_{\rm stat}|w(Z_{u+k})-w(Z_u)|^2
      =m\sum_{k=1}^{m-1}(1-\lambda^k)\le C m^3/\beta_W .
\]
Only $O(J)$ longitudinal starts affect $F$. The one-path form divides their sum by $m$. Dividing by the variance above gives the claimed upper bound. This test concerns the conditional law used in (11). Averaging over the physical exterior is a further operation.

## Testing a noncommuting exterior

**GUIDE.** Row 1141, `gap-crux2-astra62.md`, (4)–(8), already uses two plaquettes to control arbitrary adjoint color frames on typical Wilson fields. Its estimate is probabilistic in the ordinary measure. I use its loop telescoping argument on a different object, a specified constrained measure admissible in (9). This tests whether control of color transport can supply the missing inequality on $W$.

**PROVED.** In quaternion notation prescribe constant coarse links by direction,
\[
 c_1=\mathbf i,\qquad c_2=\exp(\pi\mathbf j/4),\qquad
 c_3=\exp(\pi\mathbf k/4),\qquad c_4=1.
\]
For *every* fine configuration on this fibre, with $v_x\in\mathfrak{su}(2)$,
\[
 \sum_x |v_x|^2\le16 b^5\sum_{(x,y)}
           |v_x-\operatorname{Ad}(U_{xy})v_y|^2.                       \tag{16}
\]
The fine-edge sum uses each positive link once. The power of $b$ is optimal uniformly over the fibre.

**PROVED.** At a coarse site the $12$ and $13$ plaquette products are the commutators $-\mathbf j$ and $-\mathbf k$. Their adjoints are half-turns about orthogonal axes. The sum of their two squared displacements of $v$ is at least $4|v|^2$. Telescoping a transported difference around each $4b$-edge loop and applying Cauchy–Schwarz bounds its square by $4b$ times the sum of fine-edge energies on that loop. Each fine edge lies in at most four of these loops as the base site varies. Thus the sum of $|v_y|^2$ over coarse sites is at most $4b$ times the full energy. Partition fine sites into half-open side-$b$ cubes at these sites. A coordinate path from $y$ to any $x$ in its cube uses at most $4b$ fine edges. The triangle inequality gives $|v_x|^2\le2|v_y|^2+8b\sum_{e\in[y,x]}|\nabla_U v(e)|^2$. Summing over at most $b^4$ sites per cube proves (16).

**PROVED.** For the other inequality, assign the shortest constant $b$th root of $c_\nu$ to each fine edge on the corresponding coarse path. Give the other edges value one. This is a configuration on the prescribed fibre. A constant unit color changes by at most $\pi/b$ on a path edge and has zero difference elsewhere. There are $4bL^4$ path edges and $(bL)^4$ sites. Its Rayleigh quotient for the adjoint site Laplacian is at most $4\pi^2 b^{-5}$. This fixes the worst-case order in (16).

**PROVED.** For example, take $a_j=a_0 2^{-j}$, $N_j=2^j L_j$ with even $L_j$ of order $j^2$, $\beta_{W,j}\le Cj$, and $b_j$ the least power of two at least $j^3$. Eventually $b_j$ divides $2^j$. The log of the number $4(N_j/b_j)^4$ of prescribed products is $O(j)$, while $\eta$ from (5) is at most $C'j^{3/2}e^{-c j^2}$. Hence (6) has $\theta\to1$. On this admissible fibre the bottom of the adjoint *site* Laplacian in physical units is at least $1/(16a_j^2 b_j^5)\to\infty$. If the fine $W$-variance estimate at a fixed physical radius could be deduced from this coercivity, (9) and (3) would apply to a matched limit.

**PROVED (failure of pointwise convexity on the same fibre).** For $b\ge16$ choose a fine link in the centre of a coarse cell at distance at least three from every straight path. Set it equal to $-1$, its plaquette neighbours equal to one, and keep the prescribed path products. In the $W$-marginal density only its six original plaquettes read this link. No integrated private staple or product density reads it. Vary the link as $-\exp(t\mathbf i)$ with the others fixed. The part of the negative log density that varies is $6\beta_W\cos t$ up to a constant. Its second derivative is $-6\beta_W$ at zero. The smooth positive marginal density gives positive measure to open neighbourhoods of such exteriors. All configurations still satisfy (16). Thus (16) supplies no pointwise convex Hessian estimate of the required kind. For a smooth gauge-invariant function the derivative along a vertex gauge orbit vanishes identically. The gradient of a nonconstant plaquette trace can therefore be horizontal even when the adjoint site Laplacian is coercive. A lower bound on the variance form for these gauge-invariant functions remains to be found.

## Enlarging the resampling cube on the fine lattice

**GUIDE.** B's comparison at lines 6520–6574 loses the fourth power of the side ratio in the upward direction. Their sharpness result for comparison of the two forms concerns arbitrary tests in both forms. Here the input is a *spectral gap* of the smaller-cube dynamics. The inverse of that dynamics can then be used in a dual estimate. The use of commuting projections for separated cubes and weighted counts of overlapping patches is related to Knabe's method and to the companion paper's Appendix G, read in row 1224. The estimate below runs from one global gap to a gap for larger updates on the same torus.

**PROVED.** For the fine Wilson law on an even $N^4$ torus write $v_s$ for the optimal constant in (1) at side $s$, on gauge-invariant functions. Let $2\le s\le t$ with $2t+4\le N$, put $k=t-s+1$, and take any integer $1\le w\le k/4$. If $v_s>0$, then
\[
 v_t\ \ge
 \left(\frac{k-2w}{t}\right)^4
 \left(1+\frac{32(2+1/s)^4s^2}{k w v_s}\right)^{-1}.                 \tag{17}
\]
The argument also applies to any closed mean-zero subspace preserved by the cube projections, using a lower bound and testing the conclusion on that subspace. Only finite-range conditional independence is used in addition to the spectral bound.

**PROVED.** Let $D_x=1-P^{(s)}_x$ and $H_s=s^{-4}\sum_xD_x$. This is the auxiliary Gibbs sampler generator. For a centered test $f$ in the stated subspace set $g=H_s^{-1}f$. It exists there and $\langle g,H_sg\rangle\le\|f\|^2/v_s$. If two small-cube origins are more than $s$ apart in periodic maximum distance, no plaquette reads links of both cubes. Given their joint exterior they are independent. Their conditional projections commute, so $\operatorname{Re}\langle D_x g,D_y g\rangle=\|D_xD_y g\|^2\ge0$ for such $x,y$.

**PROVED.** Take a nonnegative real weight $p$ on the origins $\{0,\ldots,k-1\}^4$ of small cubes inside one side-$t$ cube, extended by zero on the torus. Write $A=\sum p$, $B=\sum p^2$, and
\[
 L_z=s^{-4}\sum_x p(x-z)D_xg .
\]
Projection onto the exterior of $V_t(z)$ kills $L_z$, by nested conditional expectation. Since $\sum_z L_z=A f$, Cauchy–Schwarz gives
\[
 A^2\|f\|^4\le t^4\mathcal E_t(f)\sum_z\|L_z\|^2 .                    \tag{18}
\]
Write $B_{xy}=\sum_zp(x-z)p(y-z)$. Then $0\le B_{xy}\le B$ and $B-B_{xy}=\|p-\tau_{x-y}p\|_2^2/2$, using counting measure for weights. Suppose $B-B_{xy}\le\epsilon B$ for all pairs at distance at most $s$. On expanding the sum of squares in (18), comparison with $B\|H_s g\|^2$ can increase the result only for pairs at distance at most $s$, since more distant cross terms are nonnegative. For each remaining pair bound the absolute cross term by $(\|D_xg\|^2+\|D_yg\|^2)/2$. There are at most $(2s+1)^4$ possible partners per $x$. Hence
\[
 \sum_z\|L_z\|^2
 \le B\left(\|f\|^2+\epsilon(2+1/s)^4\langle g,H_sg\rangle\right).    \tag{19}
\]
In this last term $s^{-4}\sum_x\|D_xg\|^2=\langle g,H_sg\rangle$ supplies one power of the normalization.

**PROVED.** Choose $p$ to be the product of four copies of the one-dimensional weight $u(i)=\min(1,(i+1)/w,(k-i)/w)$ for $0\le i<k$, zero elsewhere. Then $\sum u^2\ge k-2w\ge k/2$, $\sum(u(i+1)-u(i))^2\le2/w$, and $(\sum u)^2/\sum u^2\ge\sum u\ge k-2w$. A one-coordinate unit shift of $p$ has difference norm at most $2\sqrt B/\sqrt{kw}$. At most $4s$ such shifts give any near-pair displacement. Thus $\epsilon=32s^2/(kw)$ suffices, and $A^2/B\ge(k-2w)^4$. Substitution in (18)–(19) proves (17).

**PROVED (physical scale of the comparison).** Put $u=\lceil s/\sqrt{\min(v_s,1)}\rceil$. If $4096u\le t$ and $2t+4\le N$, then $v_t\ge1/2$. Indeed $k\ge4095u$, $w=u$ is admissible, $(2+1/s)^4<40$, and the denominator in (17) is at most $1+1280/4095<4/3$. The numerator is at least $(1-3/4096)^4\ge1-12/4096>2/3$. More generally (17) tends to one from below as $t/u\to\infty$. A single elementary plaquette trace gives the matching upper bound $v_t\le1+2/t$ by counting cube origins that hit its three distinct base points, as in B's cube comparison. Thus on sequences with $t/u\to\infty$ and $t\to\infty$ the optimal constants tend to one.

**PROVED (a microscopic sufficient condition).** On the diagonal of (3), suppose $a_js_j\le L_0$ and
\[
                   v_{s_j}\ge c\,(a_j s_j)^2,\qquad c>0.               \tag{20}
\]
Take $t_j=4096\lceil s_j/\sqrt{\min(v_{s_j},1)}\rceil$. Then $a_jt_j\le4096(\max(L_0,c^{-1/2})+a_j)$ and eventually $2t_j+4\le N_j$. Apply (17) and (3) at $t_j$. It suffices that the source logarithms in (2) be $o(a_jN_j)$, which implies (2) for these $t_j$. This establishes a continuum spectral bound conditional on (20) and the same matching hypotheses. On a volume-first construction B's own Theorem 66 gives the corresponding implication if (20) holds uniformly on an unbounded set of tori at each cutoff. Choose $t_j$ there using the common lower bound in place of the optimal constant, so it is independent of the torus. This compares gaps on the fine Wilson law. B's Haar example at lines 7302–7355 saturates the fourth-power loss for the ratio of two forms on a high-degree test, with both spectral gaps positive. It is consistent with (17).

**PROVED (a form version).** With $p,A,B,\epsilon$ as in (18)–(19), on any invariant subspace,
\[
 H_t\ \ge\ \frac{A^2}{t^4 B}
           \frac{H_s}{H_s+\epsilon(2+1/s)^4}.                          \tag{21}
\]
Take $\epsilon>0$. For general $f,g$, the proof of (18)–(19) bounds $|\langle f,H_sg\rangle|^2$ by $(t^4 B/A^2)\mathcal E_t(f)$ times $\langle g,(H_s^2+\epsilon(2+1/s)^4 H_s)g\rangle$. Substituting $g=(H_s+\epsilon(2+1/s)^4)^{-1}f$ gives (21), including the kernel by continuity. This is why a high-degree test with a very large small-cube form cannot contradict the comparison.

## A continuous-gradient attempt on the remaining estimate

**GUIDE.** Row `gap-gamma2-astra.md`, lines 390–447, obtains a fixed-spacing transfer implication from a configuration-space Poincaré inequality by propagating a gradient in stochastic time. Here I test a weaker size of the required constant by localizing the inverse of the continuous generator. This uses the actual mixed derivatives of the Wilson action and needs no pointwise lower Hessian bound.

**PROVED.** Equip each $\mathrm{SU}(2)$ with the round metric on the unit quaternions. Let $\rho>0$ be a Poincaré constant for $\sum_e\int |\nabla_e g|^2\,d\mu$ on gauge-invariant functions of the fine Wilson torus. For $2t+4\le N$ and integer $1\le w\le t/4$,
\[
 v_t\ \ge\ (1-2w/t)^4\left(1+\frac{576\beta_W}{tw\rho}\right)^{-1}.   \tag{22}
\]
In particular, $v_t\ge1/2$ if $t\ge2048\lceil\max(1,\sqrt{\beta_W/\rho})\rceil$. Therefore
\[
                         \rho_j\ge c\,\beta_{W,j}a_j^2                 \tag{23}
\]
on one suitable fine torus per cutoff is another sufficient input for (3), under the same source growth and matching as in (20). All generators and constants in (20) and (23) refer to auxiliary sampling of the Euclidean Wilson measure.

**PROVED.** Let $V=-\beta_W\sum_p w(U_p)$ with $w(U)=\tfrac12\operatorname{tr}U$. For orthonormal left-invariant derivatives $D_e^a$, set $L_e=\sum_a(D_e^a)^*D_e^a$ in $L^2(\mu)$, $L=\sum_e L_e$. Integration by parts gives $(D_e^a)^*=-D_e^a+D_e^aV$. For different links, derivatives commute, so on smooth functions
\[
 \operatorname{Re}\langle L_e g,L_f g\rangle
 =\sum_{a,d}\|D_e^aD_f^d g\|^2+
   \operatorname{Re}\int\sum_{a,d}\overline{D_e^a g}
              (D_e^aD_f^d V)D_f^d g\,d\mu .                             \tag{24}
\]
Indeed differentiate $(D_f^d)^*D_f^d g$ in $e$ and integrate by parts in $f$. The mixed Hessian has operator norm at most $J_{ef}=\beta_W$ times the number of plaquettes containing both links. For unit imaginary quaternions, inserting one at each of two positions in a plaquette trace changes the absolute bilinear coefficient by at most one. Inverse orientations only conjugate or negate the insertions. Each link belongs to six plaquettes, each with three other links, so $\sum_{f\ne e}J_{ef}\le18\beta_W$. Such pairs have base points at maximum distance at most one.

**PROVED.** In (18) use $f=Lg$, $L_z=\sum_e p(\operatorname{base}(e)-z)L_e g$ and the weight with $k=t$. A link inside the cube has zero conditional integral of $L_e g$ against every exterior test, by integration by parts. The terms with identical links cancel in the comparison with $B\|Lg\|^2$. For distinct links use (24). The squared mixed derivatives have favorable sign. The possible increase is at most
\[
 B\frac{32}{tw}\sum_{e\ne f}J_{ef}
       \frac{\|\nabla_e g\|_2^2+\|\nabla_f g\|_2^2}{2}
 \le B\frac{576\beta_W}{tw}\langle g,Lg\rangle.
\]
Use the Poincaré bound $\langle g,Lg\rangle\le\|Lg\|^2/\rho$ on centered invariant functions, obtained by Cauchy–Schwarz and the assumed gradient inequality. The estimate for $A^2/B$ is the same as before. This proves (22) on the range of $L$ acting on smooth invariant functions.

**PROVED.** That range is dense in centered invariant $L^2(\mu)$. For details, multiplication by the square root of the positive Wilson density transfers $L$ to the product Haar Laplacian with sign chosen positive, plus the smooth bounded potential $|\nabla V|^2/4-\Delta V/2$, with $\Delta$ the geometric Laplacian of nonpositive spectrum. Product matrix coefficients are a dense eigenfunction core for the Haar Laplacian by Peter–Weyl. A bounded potential preserves its operator core. The smooth functions on the Wilson space are consequently a core after the unitary change of measure. Gauge averaging commutes with $L$ and preserves smoothness. The kernel consists of constants by the energy identity, since the group product is connected and its strictly positive smooth density is bounded above and below at fixed torus. Orthogonality to the smooth range therefore forces a centered invariant vector to vanish. The bounded cube form extends (22) by density. The numerical constants in the last implication of (22) follow by setting $w=\lceil\max(1,\sqrt{\beta_W/\rho})\rceil$.

## Testing the microscopic bound on Wilson fields

**PROVED, using row 1231's Wilson packet estimate.** On the symmetric tori of `gap-solve26-astra62.md`, (35), take $\beta_W\to\infty$, $\beta_W\le B_0\log N$ and $R=\lfloor\beta_W^\delta\rfloor$ for fixed $0<\delta<1/48$. For every fixed $C_0$ and $2\le s\le C_0 R$, the actual optimal constants satisfy
\[
                v_s(R/s)^2\longrightarrow0,\qquad
                \rho R^2/\beta_W\longrightarrow0 .                     \tag{25}
\]
Here $\rho$ is the optimal invariant gradient constant. The earlier input is that $v_m R/m\to0$ for all $m\le C_1R$ with fixed $C_1$. Its proof uses a bounded color-singlet curvature packet whose time covariance on this wavelength has a limiting $t^{-8}$ tail. Its status is recorded in row 1231's cross-provider check. In the first part of (25), if a subsequence had $v_s(R/s)^2\ge\alpha>0$, then $u$ in (17) would be $O_{C_0,\alpha}(R)$. At $t=4096u$ one would have $v_t\ge1/2$ and $t=O(R)$, contradicting that input. In the second part, $\rho R^2/\beta_W\ge\alpha$ would give the same contradiction at $t=2048\lceil\max(1,\sqrt{\beta_W/\rho})\rceil$ by (22). The tori are large enough since $R=o(N)$. This concerns the gap on the invariant subspace. Row 1231's stronger statement about testing a single cyclic subspace is not needed. [Row 1231](gap-solve26-astra62.md) · [Check of its packet estimate](gap-solve26-check-opus.md)

**PROVED, conditional on nontrivial matching.** At a microscopic update side with $a_js_j\to0$, a nontrivial matched diagonal theory with the source growth of (20) requires
\[
 \limsup_j\frac{v_{s_j}}{(a_js_j)^2}<\infty,\qquad
 \limsup_j\frac{\rho_j}{\beta_{W,j}a_j^2}<\infty                       \tag{26}
\]
for strictly positive $\beta_{W,j}$ on the weak-coupling trajectory. If either limsup were infinite, take a subsequence on which its ratio diverges. For every fixed physical $h>0$ one could take $t_j=\lceil h/a_j\rceil$ in (17) or (22) and obtain $v_{t_j}\ge1/2$ eventually. In the first case $v_{s_j}\le1+2/s_j$ handles the cap at one. By (3) the same continuum representation would have a gap at least $8/(625e^2h)$ for every $h>0$ (use any $\ell>h$ and then decrease $\ell$ to $h$). A nonzero centered vector has positive spectral measure in some bounded energy interval, giving a contradiction. The missing direction for the sufficient conditions (20) and (23) is a *lower* bound. The ultraviolet upper estimates in (25) leave room for either outcome.

**PROVED (testing direct comparison with Haar).** The oscillation of the Wilson exponent on the entire even torus is exactly $12\beta_WN^4$. Identity links maximize each of the $6N^4$ plaquette traces simultaneously. At the other extreme set $U_{x,\mu}=(-1)^{\sum_{\nu<\mu}x_\nu}\,1$. Even periods make the assignment periodic. In a $\mu\nu$ plaquette with $\mu<\nu$ only the $\nu$-link sign changes under the $\mu$ step, hence all plaquette products equal $-1$. The ratio-of-densities comparison used in (9) therefore gives only the Haar constant times $e^{-12\beta_WN^4}$ for either form. The cube form at Haar has constant at least one by the centered tensor expansion used in (7). This lower bound is too small for (20) on the stated physical diagonals. Positivity of the finite-volume density leaves its actual relaxation rate undetermined.

**PROVED (testing curvature on an invariant observable).** The checkerboard configuration used in the preceding paragraph is the example of §5.1 in `gap-gamma2-astra.md`. At that configuration every gauge-invariant gradient vanishes, a limitation explicitly noted there. The following local modification gives a smooth gauge-invariant function with a strictly negative *pointwise* Bochner expression, including its positive Hessian-square term, for all sufficiently large $\beta_W$. The construction works for the full Wilson law and for the $W$-marginal with the noncommuting products of (16).

**PROVED.** Take a fine plaquette $p$ well inside a coarse cell of side $b\ge64$. On every plaquette meeting an edge of $p$ use the checkerboard links. Several lattice steps away choose a plaquette $q$ with holonomy $\mathbf j$. Join their roots by a fixed bounded-length path $\gamma$ inside the cell. Both loops and the path stay at least three sites from the prescribed graph. All these assignments are compatible with the path constraints. Define the real test
\[
 F(U)=\langle\operatorname{Im} U_p,\,
        \operatorname{Im}(U_\gamma U_q U_\gamma^{-1})\rangle .
\]
Both entries transform by the same conjugation at the root of $p$. At the chosen field the first entry is zero, so differentiating the second makes no contribution to the gradient. With right or left velocity coordinates on each of the four central edges of $p$, the gradient $X$ has a common imaginary unit axis with the four oriented boundary signs, up to an overall sign. It vanishes on every other link. In particular $|X|^2=4$. Vary the links along the product geodesic with these velocities. Every plaquette $p'$ affected by the variation is initially $-1$ and all varying factors use the same axis. Thus its normalized trace is $-\cos(t\,dX(p'))$, where $dX(p')$ here denotes the signed scalar circulation. In particular $|dX(p)|=4$. For the negative log density $V$ of either law this gives
\[
 \nabla^2 V(X,X)=-\beta_W\sum_{p'}|dX(p')|^2\le-16\beta_W .             \tag{27}
\]
For the marginal all additional integrated factors are independent of the four varied links. The squared Hessian of $F$ is at most an absolute $C$, since $F$ is a fixed smooth function of a fixed finite product of compact groups. The product round metric contributes $\operatorname{Ric}(X,X)=8$. By the pointwise Bochner identity derived in §1 of the same earlier note, $\Gamma_2(F)\le C+8-16\beta_W$ at this field. Strict negativity persists on an open set of positive probability for each sufficiently large coupling. Pointwise curvature on physical test functions therefore cannot supply (23) in this way. The integrated expression still averages this set with its Wilson weight.


## How much of the slow spectrum can a local source see?

**GUIDE.** B's local criterion at lines 6985–6999 and Appendix H asks for a gap on the cyclic subspace of each observable for the random-cube chain. Row 1222, (8)–(9), uses finite propagation of a deterministic sweep. I use a different finite-range update to allow some spectral weight below the proposed rate. The weight can be polynomially small in the cutoff, even on a joint finite-volume diagonal. The proof uses elementary polynomial approximation on an interval.

**PROVED.** Suppose $2s$ divides $N$. For each offset $o$ modulo $2s$ in four dimensions, take all side-$s$ cubes with origins in $o+(2s\mathbb Z)^4$ on the torus. Define
\[
 P_o=\prod_{x\in o+(2s\mathbb Z)^4}P^{(s)}_x,\qquad
 K=(2s)^{-4}\sum_o P_o .                                                \tag{28}
\]
Each product is an orthogonal projection, by the separated-cube independence in (17). The positive self-adjoint contraction $K$ preserves constants and commutes with translations. If $G$ depends on a link set $S$, then $K G$ is supported within base-point distance $s+1$ of $S$ in the periodic maximum norm. Within a layer the cubes missing $S$ can be removed by commutation. Integrating the other cubes reads only their links and the plaquettes incident to them. For any test $F$ outside those updated cubes, $\langle F,P_oG\rangle=\langle F,G\rangle$ by self-adjointness of the remaining projections. Induction proves that if the supports of $F,G$ are at distance greater than $h(s+1)$, then $\langle F,K^r G\rangle=\langle F,G\rangle$ for $0\le r\le h$. In particular $K$ has exact finite propagation for this pairing.

**PROVED.** For $0<\sigma<1$ let $\Pi_\sigma={\bf1}_{(1-\sigma,1]}(K)$. For centered $F,G$ with the separation just stated,
\[
 |\langle F,G\rangle|\le
 \|F\|_2\|\Pi_\sigma G\|_2+
                  2e^{-2h\sqrt{\sigma}}\|F\|_2\|G\|_2 .                \tag{29}
\]
Indeed use the polynomial
\[
 p_h(x)=\frac{T_h(2x/(1-\sigma)-1)}{T_h((1+\sigma)/(1-\sigma))},
 \qquad T_h(\cos t)=\cos(ht).
\]
It has $p_h(1)=1$. Its numerator has absolute value at most one for $0\le x\le1-\sigma$. For $1-\sigma\le x\le1$, the identity $T_h(\cosh t)=\cosh(ht)$ bounds the ratio by one. The denominator is at least $\tfrac12\exp\!\left[h\log\frac{1+\sqrt\sigma}{1-\sqrt\sigma}\right]\ge\tfrac12e^{2h\sqrt\sigma}$. These identities follow from the addition formula and the recurrence for $T_h$. The moment identity for (28) gives $\langle F,G\rangle=\langle F,p_h(K)G\rangle$. The spectral theorem on the two intervals gives (29).

**PROVED (a local sufficient condition).** Use the same reflected matching and density assumptions as in (3), on tori admitting the offsets in (28), and write $A_j=F_j-\mu_jF_j$. Suppose there are thresholds $0<\sigma_j<1$ with
\[
 \liminf_j\frac{2\sqrt{\sigma_j}}{a_j(s_j+1)}\ge\kappa>0 .
\]
Assume that for each source there exist numbers $B_j\to\infty$, $B_j=o(a_jN_j)$, such that for a common $\alpha>0$
\[
 \|A_j\|_2^2\le e^{B_j},\qquad
 \|A_j\|_2\|\Pi_{\sigma_j} A_j\|_2\le e^{-\alpha B_j}.                \tag{30}
\]
Then $H\ge \kappa\alpha/(1+\alpha)$ on $\Omega^\perp$. To prove this, fix $0<\kappa'<\kappa$ and take even padding $T_j$ with $a_jT_j=(1+\alpha)B_j/\kappa'+O(a_j)$. It fits within one quarter of the torus eventually. The separation is at least $T_j-O_F(1/a_j)$, including both supports within fixed physical boxes and the shift of reflected temporal link origins. In (29) use the largest $h$ with $h(s_j+1)$ strictly less than this lower bound. Then $2h\sqrt{\sigma_j}\ge\kappa'a_j T_j-O_F(1)$ eventually, by first bounding $2\sqrt{\sigma_j}/(a_j(s_j+1))$ below by $\kappa'$ before multiplying the separation, and using $\sqrt{\sigma_j}<1$ for integer rounding. Translation commutes with $\Pi_{\sigma_j}$ and reflection preserves the source norm. Equation (29) gives $C_j(T_j)\le O_F(1)e^{-\alpha B_j}$. Now (4), positive-padding matching, and the spectral argument for (3) give the stated result by increasing $\kappa'$ to $\kappa$.

**PROVED.** For example, if $a_jN_j/\log(1/a_j)\to\infty$, $\|A_j\|_2^2\le a_j^{-P}$ with $P>0$, and the second product in (30) is at most $a_j^q$ with $q>0$, one can use $B_j=P\log(1/a_j)$ and $\alpha=q/P$. A common positive lower bound on $q/P$ suffices across the matched family. For bounded norms, mere convergence of that second product to zero suffices. In that case one may take any diverging $B_j$ slower than both $a_jN_j$ and the negative log of the product, with $\alpha=1$. The global gap of $K$ does not enter these conclusions.


**PROVED (testing the local filter on fine Wilson fields).** Use the centered, bounded magnetic packet $f_R$ of row 1231 and its torus and coupling hypotheses in (25). Write $R=\lfloor\beta_W^\delta\rfloor$, and choose $2s\mid N$, $s\le C_0R$. For each fixed $\lambda>0$ such that $\sigma=\lambda((s+1)/R)^2<1$ along the chosen sequence,
\[
            \liminf \|\Pi_\sigma f_R\|_2>0 .                            \tag{31}
\]
Indeed at time separation $\lfloor uR\rfloor$ the two packets have norm at most one and their covariance tends, for each fixed $u$, to $K_{\rm mag}(u)$ with $K_{\rm mag}(u)\asymp u^{-8}$. This is the finite-torus statement following (35) in row 1231. The packets use spatial links on a single time slice. In (29) one can take $h\ge\lfloor uR/(s+1)\rfloor-2$. Since $\sqrt\sigma<1$, the second term is at most $2e^6 e^{-2u\sqrt\lambda}$ eventually. Choose a sufficiently large fixed $u$ that this is less than $K_{\rm mag}(u)/4$. Equation (29) bounds the slow projection norm below by $K_{\rm mag}(u)/2$ for all sufficiently large cutoffs. The test forces actual weight in a shrinking band when $s/R\to0$. The physical band in (30) can be exponentially narrower on the logarithmic coupling trajectory.

**PROVED (attempt by local changes of variables).** A centered source of the form $G=(I-K)g$ with $g$ local has $\|\Pi_\sigma G\|_2\le\sigma\|g\|_2$. This alone cannot furnish a dense set of physical vectors. Its pairing with every test at distance greater than $s+1$ from $\operatorname{supp}g$ is *exactly zero* by (28). In particular, if the primitives $g_j$ have bounded physical support near the source and $a_js_j$ stays bounded, its reflected matched correlation vanishes at every sufficiently large fixed positive padding. The positive continuum spectral representation then forces the matched vector to be zero. A proof of (30) by this device would have to control genuinely nonlocal primitives or a remainder with nonzero physical norm.


**PROVED (the local test for the original Wilson cube generator).** One can also remove the divisibility condition and use $H_s=s^{-4}\sum_x(I-P_x^{(s)})$ itself. Let $D$ be the periodic maximum distance of the base points of two supports, $s\ge2$, $2s+4\le N$. Set
\[
 d=\left\lfloor\frac{D}{2(s+1)}\right\rfloor,\qquad
 h=\lfloor d/10000\rfloor,\qquad
 M_s(S)=s^{-4}\#\{x:V_s(x)\text{ meets }S\}.
\]
For $d\ge1$, $0<\lambda\le\log 2$, $\sigma=1-e^{-\lambda}$, and $J_\lambda={\bf1}_{[0,\lambda)}(H_s)$, all centered local $F,G$ obey
\[
 |\langle F,G\rangle|\le
 \|J_\lambda F\|_2\|J_\lambda G\|_2+
 \|F\|_2\|G\|_2
 \left(2e^{-2h\sqrt{\sigma}}+4M_s(S_G)2^{-d}\right).                  \tag{32}
\]
This argument uses row 1231's Poisson-clock construction of its (36), with polynomial filtering in the elapsed stochastic time.

**PROVED.** Write $S_u=e^{-uH_s}$. Its power series, after extracting the scalar exponential, makes it the average of time-ordered products of the conditional projections with independent rate $s^{-4}$ Poisson clocks at their origins. For one such history start with $S_G$. An update missing the current possible support fixes the function. An update meeting it expands the possible support only by its cube and the plaquette neighbours of that cube. Unless a time-ordered chain from $S_G$ reaches a cube meeting $S_F$, every step either fixes the current function or preserves its inner product with $F$, by self-adjointness. The distance covered by a chain of $k$ updates is at most $2k(s+1)$. There are $s^4M_s(S_G)$ choices for its first origin and at most $(2s+3)^4\le625s^4$ for each later origin. The expected number of occurrences of any specified ordered list of $k$ rings before time $u$ is $(u/s^4)^k/k!$, including repeated origins. This follows by ordering the $k$ distinct times in the Poisson factorial moment, or by conditioning on the total number of rings. A union bound therefore gives probability at most $M_s(S_G)\sum_{k\ge d}(625u)^k/k!$ for the chain. If $u\le h$, this is at most $2M_s(S_G)4^{-d}$ by $k!\ge(k/e)^k$. Every history is an $L^2$ contraction. It follows that $\langle F,S_uG\rangle$ differs from $\langle F,G\rangle$ by at most $4M_s(S_G)4^{-d}\|F\|_2\|G\|_2$. The estimate needs no supremum norm of a source.

**PROVED.** Use the polynomial $p_h$ of (29). The sum of the absolute values of its monomial coefficients is at most $11^h$, since the affine argument of $T_h$ has coefficient sum at most five for $\sigma\le1/2$, and $T_{h+1}(z)=2zT_h(z)-T_{h-1}(z)$. The denominator is at least one. Since $S_1^i=S_i$, $0\le i\le h$, the pairing with $p_h(S_1)$ differs from the original one by at most $4M_s(S_G)2^{-d}\|F\|_2\|G\|_2$, using $11^h4^{-d}\le2^{-d}$. On the slow subspace $J_\lambda$ use the two projected norms and $|p_h|\le1$. On the complementary subspace use the exponential bound in (29). This proves (32).

**PROVED.** On the matched diagonal assume $a_j(s_j+1)\to0$ and take $\lambda_j=c[a_j(s_j+1)]^2$ with $c>0$. Suppose (30) holds with $J_{\lambda_j}$ in place of $\Pi_{\sigma_j}$ and
\[
 \log(2+M_{s_j}(S_j))=o\!\left(\frac{B_j}{a_j(s_j+1)}\right).          \tag{33}
\]
Then (32) implies a continuum physical gap of at least $\sqrt c\,\alpha/(10000(1+\alpha))$. Indeed $2h\sqrt{1-e^{-\lambda_j}}$ is bounded below by $\kappa' a_jT_j-O_F(1)$ for every fixed $\kappa'<\sqrt c/10000$ and large $j$ at the separation used in (30). The second error in (32), including both source norms, has log at most $-(\log 2)d+o(d)$ there by (33) and $B_j=o(d)$. It is smaller than $e^{-\alpha B_j}$ eventually. Translation commutes with $J_{\lambda_j}$ and one can bound the projected norm of the other, reflected insertion by its full norm. The proof of (30) now applies. Exact exclusion from this stochastic band on the cyclic subspace of each matched insertion is sufficient. Polynomial suppression can also suffice. Both versions concern the original fine Wilson cube dynamics.


**PROVED (fine Wilson spectral weight).** For the torus sequences and packets $f_R$ in (31), divisibility is unnecessary for the original cube chain. For any $C_0<\infty$ there are $c_0>0$ and $\eta_0>0$ such that for $0<\eta<\eta_0$ and $2\le s\le C_0R$,
\[
 \liminf_{\beta_W\to\infty}
 \left\|{\bf1}_{[0,\,\eta((s+1)/R)^2)}(H_s)f_R\right\|_2^2
       \ \ge\ c_0\frac{\eta^4}{(1+\log(1/\eta))^8}.                   \tag{34}
\]
The earlier ultraviolet packet theorem cited in (25) is the Wilson input. In particular the slow modes detected by (25) carry strictly positive weight for a bounded gauge-invariant source at each fixed rescaled threshold in (34).

**PROVED.** Put $b'=R/(s+1)\ge1/(C_0+1)$ eventually and $\lambda=\eta/(b')^2\le\log2$ by decreasing $\eta_0$. At time separation $\lfloor uR\rfloor$ one has $d\ge ub'/2-2$ in (32). The packet is on one spatial slice in a box of side $2R+O(1)$. Thus $M_s(S_{f_R})\le C(1+b')^3$, by counting at most $s$ time origins and $O((R+s)^3)$ spatial origins. For fixed, sufficiently large $u$, the last term in (32) is bounded by $C_{C_0}e^{-c_{C_0}u}$ uniformly in $b'$, since the geometric exponential absorbs the cubic factor. Next $\sqrt{1-e^{-\lambda}}\ge\sqrt{\lambda/2}$, so $2h\sqrt{\sigma}\ge c_1u\sqrt\eta-C_1$ for absolute $c_1>0,C_1<\infty$. Both insertions have norm at most one. Their low projected norms are equal by translation, and their covariance tends to $K_{\rm mag}(u)\ge c_2u^{-8}$ for all sufficiently large fixed $u$. Set $u=A\eta^{-1/2}(1+\log(1/\eta))$ with fixed $A$ such that $c_1A>6$. For sufficiently small $\eta$ the two errors are less than $c_2u^{-8}/2$ in total. Take the cutoff limit at this fixed $u$, then use the expression for $u$ to get (34). The ordering of these two parameters uses only the fixed-$u$ convergence proved by row 1231. It provides no uniform approximation of Wilson covariances at physical distances. [Wilson packet and covariance](gap-solve26-astra62.md)

**PROVED (an alternative derivation of the implication (20)).** Formula (32) gives a direct hand proof without using B's finite-volume covariance estimate. For $a_js_j\le L_0$ and the lower bound (20), take $\lambda_j=\xi^2[a_j(s_j+1)]^2$ with $0<\xi\le\min(2\sqrt c/3,\sqrt{\log 2}/(2L_0))$. The centered slow projection in (32) vanishes on every invariant source, since $\lambda_j\le v_{s_j}$. In the endpoint argument at $T_j=2\lfloor N_j/8\rfloor$ the bounds $s_j+1\le3s_j/2$, $\sqrt{1-e^{-\lambda_j}}\ge\sqrt{\lambda_j/2}$ give
\[
 \liminf_j\frac{2h\sqrt{1-e^{-\lambda_j}}}{a_jT_j}
       \ge \frac{\xi}{10000\sqrt2},\qquad
 \liminf_j\frac{d\log 2}{a_jT_j}\ge\frac{\log2}{3L_0}.
\]
The floors disappear because $a_jT_j\to\infty$. With $\log(2+\|A_j\|_2)+\log(2+|S_j|)=o(a_jN_j)$, all prefactors in (32) have negligible log at this endpoint. Apply (4). This proves a positive continuum gap from (20) and the matching assumptions using only the finite Wilson law, elementary locality, and reflection positivity. The same argument works for an exact gap on the cyclic subspace of each matched source with a common $c$. The remaining problem is obtaining such Wilson bounds or the weaker (33) with the slow-weight estimate (30).


**PROVED (removing time-independent slow modes).** There is a further way of satisfying the slow-weight condition on a dense family. It tests the possibility that an arbitrarily slow global variable carries only time-independent information. Let $U_j$ translate the Euclidean Wilson field by one fine time step and set $Z_j=N_j^{-1}\sum_{r=0}^{N_j-1}U_j^r$. This orthogonally projects onto the time-independent functions and commutes with $H_{s_j}$. Fix a physical $\tau>0$ and take positive integers $m_j$ with $a_jm_j\to\tau$. Replace each centered matched source $A_j$ by
\[
                        B_j'=(I-U_j^{m_j})A_j.                           \tag{35}
\]
Assume joint matching of its finite list of time translates as in (3). The resulting continuum vector is $(I-e^{-\tau H})u$. Its finite source has support in a fixed enlarged physical box, $Z_jB_j'=0$, and
\[
 \|B_j'\|_2\le2\|A_j\|_2,\qquad
 \|J_{\lambda_j}B_j'\|_2
       \le2\|(I-Z_j)J_{\lambda_j}A_j\|_2 .
\]
Thus (30), (33) for the right-hand quantities, with harmless fixed factors absorbed by taking any smaller $\alpha$, give the same positive lower bound on the positive-energy space in the limit $\alpha'\uparrow\alpha$. In particular the weight in $Z_jJ_{\lambda_j}$ is completely unrestricted. For the density assertion, the closure of the range of the bounded self-adjoint $I-e^{-\tau H}$ equals $(\ker H)^\perp$ by the spectral theorem. The image of a dense centered span is dense in that range closure. If continuum vacuum uniqueness is among the other inputs, this is $\Omega^\perp$. Without it the argument bounds the spectrum above the full zero-energy eigenspace and leaves its multiplicity open.

**OPEN.** The Wilson action commutes with time translations, which proves the two projections commute. This commutation gives no upper bound on the component $(I-Z_j)J_{\lambda_j}A_j$. For the ultraviolet packet in (34) one can force a genuinely time-dependent slow component as well. Take its difference across $vR$ lattice steps, for fixed $v>0$. To use (34)'s method one needs a lower bound on the separated covariance of that difference. The next calculation makes this test explicitly in the range of the known Wilson limit.


**PROVED (slow weight at nonzero temporal momentum).** Under (34)'s hypotheses one can insert $I-Z$ on its left, with a possibly smaller positive $c_0$. In fact for every sufficiently small fixed $\eta$ one can replace $I-Z$ by the spectral projection of one-step time translation onto eigenphases $|\omega|>q(\eta)/R$ for some $q(\eta)>0$, taking principal eigenphases in $[-\pi,\pi]$.

**PROVED.** Choose constants $c,C$ such that $cu^{-8}\le K_{\rm mag}(u)\le Cu^{-8}$ at large $u$, and take $0<\epsilon<1/2$ with $c\epsilon^{-8}>4C$. For fixed $u$ set $n=\lfloor uR\rfloor$, $m=\lfloor(1-\epsilon)uR\rfloor$, and $g=f_R-U^mf_R$. Its pairing with $U^ng$ tends to
\[
       2K_{\rm mag}(u)-K_{\rm mag}(\epsilon u)-
                          K_{\rm mag}((2-\epsilon)u).
\]
The same packet Fourier limit used after (35) in row 1231 applies when the integer separation divided by $R$ has the specified limit. Its geometric time factor converges at each rescaled momentum, and the same integrable majorant works with either one-step rounding. The displayed expression has magnitude at least $C u^{-8}$ for large $u$. The supports of $g$ and $U^ng$ are separated by at least $\epsilon uR-O(1)$. Each support meets at most twice the previous number of update cubes. Use (32) as in (34), taking $u=A\eta^{-1/2}(1+\log(1/\eta))$ with $A$ sufficiently large also for this $\epsilon$. The two errors are again smaller than half the limiting magnitude, including the norms $\|g\|\le2$. Hence $\liminf\|J_\lambda g\|_2^2\ge c'u^{-8}$. Since $J_\lambda g=(I-U^m)(I-Z)J_\lambda f_R$, the first conclusion follows. On $|\omega|\le q/R$ the multiplier $|1-e^{im\omega}|$ is at most $u q$. On the remaining phases it is at most two. Taking, for example, $q=\sqrt{c'}\,u^{-5}/4$ forces a positive lower limit for the projected norm on the remaining phases. Thus the known fine Wilson slow spectrum has a time-dependent local component on the ultraviolet band. Whether that component enters the much narrower band of (33) is still open.


## Supplying the local estimate on the coarse-path observables

**PROVED.** On the actual fine Wilson law of (5), $s\ge2$, let $P_W$ condition on the variables off the private path interiors. For every centered square-integrable function $A(C)$ of the prescribed straight transports, the spectral projection of the *fine* cube generator obeys
\[
 \|J_\lambda A(C)\|_2
       \le \bigl(\theta^{-1}-1+\sqrt{\lambda}\bigr)\|A(C)\|_2 .          \tag{36}
\]
Here the products $C$ are random under the ordinary Wilson law. Only the paths used by $A$ need be designated. The estimate is uniform in the individual test function, including tests of unbounded character degree.

**PROVED.** From (5) the joint conditional density of $C$ given $W$, relative to its marginal density, lies between $\theta$ and $\theta^{-1}$. Indeed both the conditional and marginal density relative to product Haar lie between $(1-\eta)^M$ and $(1+\eta)^M$. Subtract the mean of $A$ before conditioning and apply Cauchy–Schwarz to get $\|P_W A\|_2\le(\theta^{-1}-1)\|A\|_2$. Independently, $H_s\ge I-P_W$ as forms on the full space. To see this, condition on $W$ as well as the fine exterior in each cube. The private links are independent given $W$ and each belongs to $s^4$ cubes. The orthogonal expansion in (7) therefore pays for every nonconstant private component with coefficient at least one. Consequently every vector $g=J_\lambda g$ has $\|(I-P_W)g\|_2\le\sqrt\lambda\|g\|_2$. Pair $A$ with unit vectors in that band and split both vectors at $P_W$. This proves (36).

**PROVED (what (36) can construct).** For uniformly bounded ordinary $L^2$ norms, (36) proves (30) with $J_\lambda$ for *every* fixed $c>0$ at $\lambda=c[a(s+1)]^2$, provided $\theta\to1$, $a(s+1)\to0$, and the volume/source condition (33) can be arranged. For example take $s=2$, $a=a_0 2^{-j}$, $b=2^j$, even coarse period $L$ of order $j^2$, and $B_j=\sqrt j$ in (30). Equations (5)–(6) make $\theta^{-1}-1=o(2^{-j})$ and any support in a fixed physical box meets at most $O(a^{-4})$ fine links. Thus any such *centered* matched source on this algebra yields the zero physical vector. Indeed (32) and reflection interpolation force its spectral measure above arbitrarily large fixed energies as $c$ varies. The spectral measure of a Hilbert-space vector is countably additive on finite energies.

**PROVED.** There is also a direct test of this obstruction for larger normalizations. If a distant insertion $F$ is exterior to every private link used for $A(C)$, it is $W$-measurable after designating only those paths. Thus $|\langle F,A(C)\rangle|\le(\theta^{-1}-1)\|F\|_2\|A(C)\|_2$. On the displayed diagonal this tends to zero even for polynomial growth of both norms in $1/a$, since $\log(M\eta)\le-c2^j/j+O(\log j)$ for these tori. For a source built out of paths in a fixed positive-time box the condition holds at any fixed sufficiently large reflected physical separation. Any matched vector at such normalizations is therefore null. This uses B's private-path estimate and the earlier conditioning argument of row 1222. The new fine-generator estimate (36) verifies the proposed stochastic bound on an actual algebra, while the separated pairing explains why this algebra cannot supply the needed dense centered span.


## The scale needed from the remaining Wilson input

**PROVED (uniform upward transfer of cube gaps).** A useful form of (17), valid at every intermediate size $2\le s\le t$, $2t+4\le N$, is
\[
 \boxed{\displaystyle
       v_t\ge 2^{-20}\min\{1,(t/s)^2v_s\}.}                             \tag{37}
\]
For $t<8s$, projection off the side-$t$ cube at a given origin has residual at least the side-$s$ residual there. Summing gives $v_t\ge(s/t)^4v_s\ge 8^{-6}(t/s)^2v_s$. For $t\ge8s$ take $w=\lfloor k/4\rfloor$ in (17), so $k\ge7t/8$, $w\ge k/8$ and $(k-2w)^4/t^4\ge(7/16)^4\ge1/64$. Since $(2+1/s)^4<40$, the denominator is at most $1+14000/((t/s)^2v_s)$. Finally $64\cdot14001<2^{20}$. If $v_s=0$ the bound holds by positivity. This proves (37) directly for the original Wilson measure. Equations (17)–(19) give the stronger approach to one at very large side ratios. The part of the upward-transfer question at B, lines 6815–6843 and 7302–7355, that compares optimal gaps on the *same fine law* thus has a scale-independent lower comparison. At weak coupling B supplies its estimate for a different law of straight-path variables. The missing step between these laws is visible in (36).


**PROVED (testing the weak-field region for (23)).** Even requiring *every* Wilson plaquette to have vanishing action per plaquette, together with the adjoint coercivity (16), does not make $\operatorname{Ric}+\nabla^2 V$ positive on gauge-invariant gradients. There are fields on the very fibre of (16) where its Rayleigh quotient in a centre-neutral gradient goes to $-\infty$. Here $V$ may be either the full negative log density or that of the marginal $\zeta_c$. Earlier discussions of constant-flux instabilities and positive curl squares concern other operators. The following computation uses the full second derivative of the Wilson action. [Earlier distinction in P82, test T5](p82-draft.md)

**PROVED.** Take $\beta=\beta_W\to\infty$, $b/\beta\to\infty$, $N=bL$ as in (16). Select $r\in[\beta^{-1/3},2\beta^{-1/3}]$ such that $|\sin(2Nr)|\ge1/2$. This is possible since $N\beta^{-1/3}\to\infty$. Start with homogeneous fine links $e^{r\mathbf i},e^{r\mathbf j},1,1$ in the four directions. On each coarse path use a constant root of the required $c_\nu$ that differs from the starting fine link by round distance at most $\pi/b$. For directions one and two choose the nearest root angle along the original axis. For direction three use $\pi/(4b)$ along $\mathbf k$. The homogeneous $12$ plaquette has trace $1-2\sin^4r$ in our normalization, by conjugating $\mathbf j$ by $e^{r\mathbf i}$. Its round distance to one is $O(r^2)$. Every other homogeneous plaquette equals one. Bi-invariance and the triangle inequality bound the distance of *every* modified plaquette from one by $O(r^2+1/b)$. Thus uniformly in all faces $p$ we have $\beta(1-w(U_p))=O(\beta^{-1/3})$. The products on the prescribed paths are exact.

**PROVED.** In the transverse $34$ plane take a square $D$ of side $R=\lfloor b/4\rfloor$ whose coordinates, including a two-site collar, are strictly between adjacent multiples of $b$ in each direction. Let $\phi$ be the product of the first Dirichlet sine in the two coordinates of $D$, zero off $D$. Give direction-one edges the right velocity $\phi(x_3,x_4)\mathbf i$, direction-two edges the velocity $-\phi(x_3,x_4)\mathbf j$ and all other links zero velocity. Call this vector $X$. Its norm squared is $2N^2\sum_D\phi^2$. No varied link or its incident faces meet a private path. The action on these links is the same for the original law and its pinned marginal. Along the product geodesic at a transverse coordinate $z$, the $12$ plaquette deficit is exactly
\[
        2\sin^2(r+t\phi(z))\sin^2(r-t\phi(z))
          =2\bigl(\sin^2r-\sin^2(t\phi(z))\bigr)^2 .
\]
Each face in planes $13,14,23,24$ affected by the variation instead has deficit $1-\cos(t(\phi(z+e)-\phi(z)))$ for the corresponding transverse step $e$. Summing the derivatives gives the exact quotient
\[
 \frac{(\operatorname{Ric}+\nabla^2 V)(X,X)}{\|X\|^2}
   = 2-4\beta\sin^2r+\beta\,4(1-\cos(\pi/(R+1))).                    \tag{38}
\]
Indeed the sum of the squared transverse differences divided by $\sum\phi^2$ equals $4(1-\cos(\pi/(R+1)))$, by the sine addition formula and summation by parts with zero boundary. Its contribution is $O(\beta/R^2)$. The negative term has magnitude at least $c\beta^{1/3}$.

**PROVED.** To realize this exact tangent by a smooth invariant scalar, use the normalized trace of the square of the holonomy of each complete direction-one or direction-two line through $D$. At this field its gradient on each edge of that line is $-2\sin(2Nr)$ times the unit axis of its direction. Conjugations between different edges leave that axis fixed. Weight the direction-one traces by $-\phi/(2\sin(2Nr))$ and the direction-two traces by the opposite coefficient, with each distinct line included once. Their sum has gradient $X$. Each winding is doubled, so this function is invariant also under centre flips. Its dependence is entirely on $W$. This establishes (38) on an actual invariant gradient with the asserted bounds on all plaquettes. It tests a pointwise tensor argument for the microscopic lower bound. An integrated Bochner proof could still use the Hessian-square term and the probability of these fields.


**PROVED (one finite-time estimate would suffice).** Under the diagonal and source hypotheses of (33), the slow-weight part of (30) can be supplied by a single positive stochastic autocorrelation bound for each matched source. Let $\lambda_j=c[a_j(s_j+1)]^2$, $t_j=B_j/\lambda_j$. It suffices to prove, uniformly with some $\alpha>0$,
\[
 \|A_j\|_2^2\,\langle A_j,e^{-t_j H_{s_j}}A_j\rangle_{\mu_j}
                      \le e^{-(1+2\alpha)B_j}.                         \tag{39}
\]
The scalar inequality $\mathbf{1}_{[0,\lambda_j)}(x)\le e^{B_j}e^{-t_j x}$ gives the required bound after taking a square root. The inner product in (39) is that of the actual fine heat bath in (32). It also equals the covariance of the readings on two histories started at the same equilibrium field, then updated independently for time $t_j/2$. This follows from conditional independence and self-adjointness. Equation (39) gives a concrete remaining Wilson estimate with one stochastic time per cutoff.

**OPEN.** I do not obtain (20), (23), or (39) on a family that creates a dense set of nonzero continuum states. The published coarse-path estimate pays for private-link variance. The unrestricted fine-field variance still contains neutral modes whose weights at physical scales are uncontrolled. The hand bounds above do not construct or identify the nontrivial Jaffe–Witten continuum theory. This is an independently unchecked research note with no numerical proof steps.

RESULT — OPEN for the four-dimensional SU(2) Jaffe–Witten mass gap. The same-torus Wilson cube comparison (37) and the local-source criterion (32)–(33) are proved here. The required weak-coupling estimate for surviving observables and the nontrivial continuum construction remain open.
