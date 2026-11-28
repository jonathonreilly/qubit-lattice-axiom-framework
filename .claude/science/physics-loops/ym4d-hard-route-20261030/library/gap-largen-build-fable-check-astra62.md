# Repo search

Row 1715 (requested lane, `gpt-6.2-astra`, xhigh). Codex cross-provider check of Claude Fable 5.2's row 1708 at checkout `99fdc1b75`. Research text only. Line numbers below refer to `library/gap-largen-build-fable.md`.

The lead searched main and PRs 10114, 10133, 10134 and 10141. The November 8 digest concerns other suppliers. Its closest hit, PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149, gives a positive one-step plaquette witness. I checked that passage. A positive correlation at one time gives no decay rate. Row 1715 names no further remote hit. There is no row-specific prior file. The open registry lists no owner for this check.

The closest local calculation is `gap-loop-eq-opus.md` 35–70, checked in `gap-loop-eq-check.md` 64–94. It gives the SU(2) Ward identity with Pauli generators and action coefficient $4\beta$ in the present units. Jafarov's finite-rank master equation and its expansion term are prior work, recorded in `prior/gap-lit-wind.md` and `prior/gap-lit-loops.md`. Row 1710, `prior/gap-largen-lit-luna.md`, supplies the literature record for strong-coupling concentration and the one-plaquette model. **CITED** below means a literature input with its stated scope. **PROVED** marks a written argument. **ARGUED** and **GUESSED** mark proposals of decreasing support. No calculation here relies on an external evaluator or a Lean run.

I checked the outline index, its obligations, and the CA-I 4.12–4.19 index for the master field, loop equations, large rank and log-Sobolev bounds. The relevant neighbouring entries concern the spectral test. The outline at 588–599, 3712–3720 and 31871–31882 distinguishes decay down to zero energy from exclusion of a spectral interval. CA-I 3215–3222 specifies the scope of its reconstruction. Credit to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at `31a47c543775`. These passages give no competing proof of row 1708.

## Checked statements

### 1. Lemma 1, lines 34–91 — HOLDS (PROVED)

Use one representative for each unoriented plaquette in the action. Orient its word from the tail of the chosen link $e$. Both derivatives act there, even for an inverse passage. All pair counts in (SD) are ordered. Assume the six incident plaquettes are ordinary squares. A torus enters a local box argument through an embedded copy of that box.

Here is a check of all coefficients. For $U(N)$ the tensor that contracts two anti-Hermitian insertions is $-\delta_{il}\delta_{jk}$ in the metric $-\mathrm{Tr}(XY)$. This follows by complexifying the orthonormal-basis contraction and using the trace-dual matrix units $E_{ij},-E_{ji}$. Removing the unit central generator $iI/\sqrt N$ adds $\delta_{ij}\delta_{kl}/N$. The diagonal insertions therefore give $-(N-1/N)n_e$. The scalar parts from distinct insertions give $(t_e^2-n_e)/N$. Together they give $-Nn_e+t_e^2/N$. The exchange parts cut one trace or join two. Division by $N$ and normalization of each trace give coefficients $-1$ and $-1/N^2$, times the two signs. Keep $\mathrm{Tr}(I)=N$ until the traces are normalized. Opposite orientations then delete two letters up to a cyclic rotation.

For the drift, let $V$ be the plaquette holonomy and $A$ the loop holonomy based at the insertion. The derivative of the action pairs the loop with $V-V^{-1}$. The exchange gives $\mathrm{tr}(AV^{-1})-\mathrm{tr}(AV)$. The central correction gives $+\mathrm{tr}(A)(\mathrm{tr}(V)-\mathrm{tr}(V^{-1}))$. Both have coefficient $\beta\epsilon_x/2$. Haar integration of the total derivative gives (SD) after summing the occurrences. The second expression has the same loop factor for every $x$, so the sum gives $t_e$. This proves lines 58–64 for every fixed exterior. For $SU(2)$ all plaquette traces are real. For $U(N)$ the two central corrections are absent at every rank.

**Exact rank checks.** A separate single-plaquette calculation checks also the four tests in line 89, at every real $\beta$. Put $q_j=\mathrm{Tr}(V^j)/N$, $q=q_1$, $\bar q=q_{-1}$ and $d=q-\bar q$. Use the following table inside expectations. In each row the identity is $A_N\langle f\rangle=\langle M_N+\beta H\rangle$. The columns list the $SU(2)$ and $SU(3)$ coefficients explicitly.

| $f$ | $A_2$ | $A_3$ | $M_2$ | $M_3$ | $H$ |
|---|---:|---:|---|---|---|
| $q$ | $3/4$ | $8/9$ | $0$ | $0$ | $(1-q_2+qd)/2$ |
| $q_2$ | $1$ | $14/9$ | $-2q^2$ | $-2q^2$ | $q-q_3+q_2d$ |
| $q^2$ | $1$ | $14/9$ | $-q_2/2$ | $-2q_2/9$ | $q(1-q_2)+q^2d$ |
| $q\bar q$ | $2$ | $2$ | $1/2$ | $2/9$ | $[\bar q(1-q_2)+q(1-q_{-2})]/2$ |

To derive the table independently, write $z_j=e^{i\theta_j}$ with $\sum_j\theta_j=0$ modulo $2\pi$. On the torus use the tangent projection $P=I-\mathbf1\mathbf1^t/N$. Weyl integration gives density $J\exp(S)$ with $J=\prod_{i<j}|z_i-z_j|^2$ and $S=N^2\beta(q+\bar q)/2$. Integration of a periodic divergence gives

$$
0=\langle D f+\Gamma(f,S)\rangle,\qquad
D=J^{-1}\operatorname{div}(JP\nabla),\qquad
\Gamma(q_j,q_k)=-\frac{jk}{N}(q_{j+k}-q_jq_k).
$$

The apparent poles at equal angles cancel against $J$. The drift of $\log J$ pairs $(i,j)$ through $\cot((\theta_i-\theta_j)/2)(\partial_i-\partial_j)$. Since $i\cot((\theta_i-\theta_j)/2)(z_i-z_j)=-(z_i+z_j)$, this gives $Dq=-(N-1/N)q$. For $q_2$ the pair contributes $-2(z_i+z_j)^2/N$. Sum the pairs and add the projected second derivative to get $Dq_2=-(2N-4/N)q_2-2Nq^2$. The product rule gives $D(q^2)=2qDq+2\Gamma(q,q)$ and $D(q\bar q)=\bar qDq+qD\bar q+2\Gamma(q,\bar q)$. Substitute the displayed $\Gamma$ for the drift and divide by $N$. These are the four rows.

For $SU(2)$, $q=\cos\theta$ and $d=0$. The first row reduces to the integral of $(\sin^3\theta\,e^{4\beta\cos\theta})'$ on $[0,\pi]$. For $SU(3)$ the last term need not vanish even in a conjugation-even law. At $\beta=0$, center invariance gives $\langle q^2\rangle=0$. Orthogonality of the fundamental character gives $\langle q\bar q\rangle=1/9$. Thus the last term in the first row has derivative $-1/18$ at zero. Dropping or reversing it fails this exact test. The degenerate $SU(1)$ arithmetic in line 89 also agrees. All these checks use hand identities.

### 2. Lemma 2 and Theorem Q, lines 109–142 — HOLDS (PROVED conditional on TPS)

Let $b=|\beta|$, $h=|s|$, $u=a'/a$, and $\Psi=\|\phi-\phi'\|_{m,a'}$ after extension by zero as in line 131. Exclude the empty sequence from the residual rows. The absolute row sums after division by $n_e$ are at most $n_e-1$ for splits, $6b$ for each of the two action terms, and $2n_e$ for $K$. A plaquette insertion adds at most four links and one lattice unit of radius. A split or merger increases neither quantity. Thus the drift difference has same-norm bound $12a^4 e^m|\beta'-\beta|$. Absorption gives line 121. This is an upper bound on a local continuation constant. It gives no differentiability of an unspecified choice of $\kappa(\beta)$, and no continuation for a pair of different norms.

For $s\subset B_{R-1}$ the residual is exactly $N^{-2}K^e(\phi-\phi')$. Its weighted size is at most

$$
\frac{2h}{N^2}\min\{2a^{-h},\ \Psi u^h\}.
$$

For $h\le\ell_N$ the second entry costs at most $\Psi/(2\kappa)$. For $h>\ell_N$ the first costs at most $4\ell_N a^{-\ell_N}/N^2$, since $x a^{-x}$ decreases for $x\ge1/\log a$. All other rows have $r(s)\ge R$ on an integer box. Their weighted size is at most $C_1e^{-mR}$, with $C_1=2/(\mathrm e\log a)+24b$. TPS now bounds $\Psi$ by $\kappa$ times the maximum of the three bounds. If $\Psi>0$, its own half cannot control it. This proves line 127, with room in both constants. It uses agreement of the local actions on the interior and makes no assumption on the exterior.

For $u=1$, use the real cutoff $x=N^2/(4\kappa)$ directly in the decreasing tail. This justifies the floor $2a^{-x}$ even when $x$ is not an integer. For $u>1$, the positive root of $x u^x=N^2/(4\kappa)$ satisfies $x=(2\log N-\log\log N+O(1))/\log u$ at fixed parameters. The floor in line 129 has the stated exponent up to powers of $\log N$. Both floors sit inside the prefactor $a'^{|s_0|}e^{m r(s_0)}$. TPS remains an assumption.

**Corollary Q1 — HOLDS AFTER CORRECTION (PROVED).** Conditioning works for bounded exterior $G$. The printed bound drops the radius factor and changes distance from a box center to distance from a whole support. Center the box at $o$ in the support of $F$. Put $D=\max_{x\in\mathrm{supp} F}\|x-o\|_\infty$. For $R\ge D$, if $G$ is supported at distance greater than $R$ from $F$, it is exterior to $B_R(o)$. The conditional means of $F$ have diameter bounded by line 127 with $r(s_F)=D$. Their unconditional mean lies in their closed convex hull. Multiply that diameter by $\|G\|_\infty$. This proves the covariance bound with $a'^{|s_F|}e^{mD}$. For smaller $R$ a trivial bound suffices after changing the support constant. The support can even be disconnected. A weight anchored on the entire support would need its own TPS estimate.

**Corollary Q2 — HOLDS (PROVED with the stated box error).** In the interior bound the two $K$ terms separately using $|\phi|,|\phi'|\le1$. The result is at most $2(N^{-2}+N'^{-2})/(\mathrm e\log a)$ in the residual norm. The boundary estimate above still holds. This is a Cauchy bound for fixed loop sequences as both ranks and the common interior radius grow. The $O(N^{-2})$ rate applies after the volume limit, or with the displayed boundary error. The limiting sequence moments alone do not give factorization.

**Spectral reading of Q, line 140 — FAILS (PROVED).** A floor $f$ bounds an invariant plateau by $f$. It need not bound all the weight below $m$ by $O(f)$. For $0<\eta<m$, a unit atom at $m-\eta$ has excess over $e^{-mt}$ at most $\eta t e^{-(m-\eta)t}\le\eta/[\mathrm e(m-\eta)]$. Choose $\eta$ small enough that this is at most $f$. The entire unit mass still lies below $m$. More generally one can bound the weight up to a fixed $E<m$ by minimizing $e^{Et}(Ce^{-mt}+f)$. A floor-free estimate on a dense family is needed in the transfer argument below.

### 3. Proposition N, lines 144–153 and 223 — HOLDS (PROVED in the winding sector)

At $\beta=0$ each ordered cut of $p^k$ at two copies of $e$ splits it into $p^j,p^{k-j}$. There are $k$ choices for the first cut for each $1\le j<k$. Total multiplicity at $e$ is $n$, including the other loops. Each cut increases the number of parts by one. The operator is triangular on partitions of fixed $n$. Alternating the residual sign with that number makes every contribution to the inverse add with the same sign. Start with all parts equal to one. This gives exactly the positive recursion in line 147, including $F((n))\ge n$. Cutting off the input at a finite $n_0$ gives a bounded test as required. This proves the restricted obstruction.

The guessed formula in line 151 can be settled by hand. Give each ordered cut weight one before division by $n$. For a cycle of size $k$ let $H_k(t)$ count ordered cut histories, with a history of $h$ cuts weighted by $t^h/h!$. Histories on disjoint cycles interleave, so their generating functions multiply. Conditioning on the first cut gives

$$
H_k(0)=1,\qquad H_k'=k\sum_{j=1}^{k-1}H_jH_{k-j}.
$$

For $G=\sum_{k\ge1}H_k(t)x^k$ this reads $G_t=2xG G_x$, with $G(x,0)=x/(1-x)$. Implicit differentiation verifies $G=x(1+G)e^{2tG}$, and the coefficient recursion is unique. Put $\Phi(u)=(1+u)e^{2tu}$. Coefficient extraction gives $n[x^n]G=[u^{n-1}]\Phi(u)^n$: in the formal residue for $[x^{n-1}]G'$, substitute $x=u/\Phi(u)$. Hence

$$
H_n^{(h)}(0)=\frac1n{n\choose h+1}(2n)^h,\qquad
F((n))=\sum_{h=0}^{n-1}\frac{H_n^{(h)}(0)}{n^h}
       =\frac{3^n-1}{2n}.
$$

The denominator stays $n$ through every split. This also proves the lower threshold $(a'/a)^4\ge3$ for the sector.

In fact the one-cycle row is maximal at each $n$. Label the positions and represent a partition by a permutation $\sigma$ with those cycle lengths. An unordered pair splits a cycle precisely when right multiplication by its transposition shortens the permutation by one in transposition length. Each such pair has two orders. Join the cycles of $\sigma$ by one transposition per join to make an $n$-cycle $\alpha$. Write $|\pi|_T=n-\#\mathrm{cycles}(\pi)$, since one transposition changes that count by one and every cycle can be split into singletons. Then $|\alpha\sigma^{-1}|_T=|\alpha|_T-|\sigma|_T$. For any prefix $\tau$ of $h$ successive cuts of $\sigma$,

$$
|\alpha|_T-h\ \le\ |\alpha\tau|_T\
 \le\ |\alpha\sigma^{-1}|_T+|\sigma\tau|_T=|\alpha|_T-h.
$$

Thus the same ordered history is available from $\alpha$. This bounds every absolute inverse row sum by $F((n))$. The sector estimate holds even at $(a'/a)^4=3$. The author's sufficient bound $5$ also follows from the majorant in line 151, whose generating function has value $1/2$ at $x=1/5$. None of these inverse bounds treats exterior rows.

**Stop at $\beta=3/5$, lines 149–157, 200 and 214 — FAILS.** In the single-plaquette, conjugation-even model, take the stated strong solution $W_1=\beta/2$, $W_k=0$ for $k\ge2$. The $k=1$ equation gives $\delta_2=-2\delta_1/\beta$. The $k=2$ equation gives $\delta_3=-\delta_1-2\delta_2/\beta$. They select the growing mode of the displayed recurrence for $0<\beta<1$ unless $\delta_1=0$. Its growth factor $g=\beta^{-1}+\sqrt{\beta^{-2}-1}$ does equal $3$ at $\beta=3/5$. The problem is the inference to TPS.

* The bound $3$ was proved at zero coupling on partitions. At positive coupling the other five incident plaquettes already take a 4D winding row outside this family. Restricting the outputs of a residual estimate need not restrict its domain to an independent test problem.
* The growing solution is a tangent vector of the **factorised one-plaquette** equation. TPS tests bounded functions of **all 4D sequences**, using every minimum-multiplicity edge. Membership of an unbounded vector in a weighted completion supplies no such counterexample by itself. A cutoff construction would have to make all those residuals small, including at the cutoff and outside the sector.
* No argument enforces the zero-coupling width constraint at the positive coupling of the recurrence. Nor need a proof at two couplings use the same weights. Cao, Nissim and Sheffield use a linear equation to bound areas in their parameter window. Their result supplies no upper limit on the coupling of every linear method. [Theorem 4.1](https://arxiv.org/abs/2505.16585)

Thus the winding example rules out a same-norm sector estimate. The proposed numerical stopping point, the exclusion of all linear methods, and the claim that (LD) is the only possible replacement do not follow.

### 4. Planar stability (PS), lines 91–107 and 159–177 — HOLDS AFTER CORRECTION as a definition. The spectral equivalence FAILS

**PROVED.** Formula 163 is the single-loop equation on a factorising planar limit. Specify a sequence of Wilson states with ranks and volumes tending to infinity, the limiting moments, and the symmetry of the selected state. Positivity implies $W(p^{-1})=\overline{W(p)}$. Charge conjugation, or a separate reality assumption, makes $W(p)$ real. Without it, the derivative in line 171 must also retain $\delta(l)[W(p)-W(p^{-1})]$. The equations on the conjugation-even branch agree for the two groups. Selecting the same solution requires a further argument.

With $a>1$, (PS) is well posed as a lower bound. The unknown is one bounded variation per loop, zero at the empty word. Its image has one residual per incident edge of each loop. A lower bound supplies injectivity and control on that image. To solve for arbitrary sources one needs a compatible source space and a range theorem. A decaying kernel for an inverse is another assertion. The factor $e^{-mr(l)}$ discounts distant residuals when the test is near the origin. It does not measure energy.

The length weight already controls the **upper** bound for the linearised split. Fix the first insertion $x$ in a loop of length $h$. A second insertion cuts off an arc of $j$ letters. At most two occurrences cut at each word boundary, one before a positive letter and one after a negative letter. The two outputs have lengths at most $j$ and $h-j$. Their radii do not increase. With $|W|\le1$, a weighted derivative row costs at most $\sum_j 2(a^{-j}+a^{-(h-j)})\le4/(1-a^{-1})$ after averaging over $x$. Decay of $W$ with raw perimeter is unnecessary for this estimate. In the unreduced words of line 40, arbitrarily many backtracks can leave a holonomy fixed. Any nonzero perimeter claim needs a specified reduced class. None of these upper bounds proves (PS).

There is a genuine **local isolation** consequence. Let $W'$ be another translation-invariant bounded planar solution with $|W'|\le1$. Set $v=W'-W$ and $\eta_K=\sup_{|l|\le K}|v(l)|$. Subtract the equations and their linear part. The residual of $v$ at $W$ consists exactly of products $v(l_1)v(l_2)$ and $v(l)[v(p)-v(p^{-1})]$ with the coefficients in line 163. In the split, bound the first factor by $\eta_K$ when $j\le K$, and by 2 otherwise. Use the weighted norm on the second. The same arc count gives, for $K\ge4$,

$$
\|(I-DF(W))v\|_{\rm rows}\le
\left[\left(\frac{2}{1-a^{-1}}+6|\beta|\right)\eta_K
      +\frac{4a^{-(K+1)}}{1-a^{-1}}\right]\|v\|_{m,a}.
$$

Choose $K$ large, then $\eta_K$ small, so the bracket is less than $1/\kappa$. (PS) forces $v=0$. There are finitely many loop shapes of length at most $K$ up to translation. This proves isolation in a neighbourhood defined by finitely many planar moments. It permits another isolated solution outside that neighbourhood. Even two simple roots of a scalar equation can both have nonzero derivative. Phase coexistence alone cannot disprove this local bound.

**FAILS** at the identification in line 175. At a factorised master field the leading connected correlation of normalized traces is zero at every separation. A nonzero planar fluctuation correlator usually needs a limit of $N^2\mathrm{Cov}$ or a specified connected observable algebra. Row 1708 constructs neither its transfer space nor a response equation with those correlations as solutions. In the other direction a gap in a physical transfer space bounds its spectral measures. It gives no lower bound on every bounded, possibly nonphysical, loop variation in (PS). Even an isolated scalar root can have zero derivative. No equivalence, rate identification, or strong-coupling (PS) theorem follows. A continuation would need a controlled physical branch, a perturbation bound for its derivative, and, where existence uses inversion, a range argument. A finite Newton certificate would also require estimates on the infinite tail. The saddle analogy and the universal exclusion of other auxiliary fields in line 97 remain **GUESSED**.

### 5. Local deviations (LD), lines 179–187 — FAILS for all ranks, already at strong coupling

**PROVED counterexample.** Take $\ell_0\ge8$, $\epsilon=1/4$, and a square $p$ in a cube deep inside the volume. At $\beta=0$ its holonomy is Haar. For $N>2$, multiplication by a center element gives $\mathbb E\,\mathrm{tr}(V)=\mathbb E\,\mathrm{tr}(V^2)=0$. Thus the planar targets for $p,p^2$ are both zero. At $N=2$, every configuration satisfies

$$
q=\mathrm{tr}(V)\in[-1,1],\qquad \mathrm{tr}(V^2)=2q^2-1.
$$

If $|q|\le1/4$, then $|2q^2-1|\ge7/8$. Every cube containing $p$ is bad. For $k=1$ the proposed bound reads $1\le e^{-4c}$, which fails for every $c>0$.

The failure persists at positive strong coupling. For any factorised master field, the single-loop rows for $p,p^2$ give $|W(p)|\le12|\beta|$ and $|W(p^2)|\le|W(p)|^2+12|\beta|$. The first row has no split. The second has the single normalized split $-W(p)^2$. The two action terms have total absolute row sum at most $12|\beta|$. If $0<\beta\le1/192$, the targets have modulus at most $1/16$ and $17/256$. A good cube would require $|q|\le5/16$. Its second moment then differs from $W(p^2)$ by at least $189/256$. This contradicts the same tolerance. This refutes the blanket strong-coupling claim for the parameters above. A coarse tolerance or a shorter list of loops can give a different event.

**CITED inputs.** Shen, Zhu and Zhu use the same $N\beta\sum_p\Re\mathrm{Tr}(U_p)$ convention. Assumption 1.1 gives $K_S=N\alpha$, with $\alpha=1/2-8(d-1)|\beta|$ for $SU(N)$. The window in four dimensions is $|\beta|<1/48$. Theorem 1.4 and Corollary 4.4 give the infinite-volume and finite-torus log-Sobolev bounds. Corollary 1.5 centers each loop at its own expectation. Corollary 1.6 gives spatial covariance decay and allows its rate to depend on $N$. The window is uniform in rank. A rank-uniform spatial rate needs its own estimate. Nissim's Theorem 1.5 for $U(N)$ proves convergence in probability about the rank-dependent mean and factorization. Its proof uses a Poincaré bound for a marginal and a phase comparison. Theorem 1.1 gives small-coupling spatial decay with rank-dependent constants. Neither theorem supplies the event in line 181. [Shen–Zhu–Zhu](https://arxiv.org/abs/2204.12737) · [Nissim](https://arxiv.org/abs/2510.22788)

**HOLDS AFTER CORRECTION around the finite-volume means (PROVED from the log-Sobolev input).** Freezing exterior links preserves the curvature estimate for $SU(N)$. In the product Hilbert–Schmidt metric their tangent vectors are zero. Along a product geodesic the plaquette Hessian in absolute value is bounded by $(\sum_{e\in p}\|X_e\|_{\rm HS})^2$: each differentiated pair costs the product of two Hilbert–Schmidt norms by trace Cauchy–Schwarz. Summing plaquettes costs at most $8(d-1)\sum_e\|X_e\|_{\rm HS}^2$. Together with Ricci curvature $N/2$ this gives the same $K_S$ in the Bakry–Émery criterion for the conditional law.

To restore the center $W$, assume an **additional bias bound**

$$
\sup_{\Delta,l}\big|\mathbb E_{\Lambda,\mathrm{bc},N}\mathrm{tr}(U_l)-W(l)\big|
\le\epsilon/2
$$

for the allowed interiors, loops, ranks and exteriors. Let $M$ be the number of tested words per cube. For one chosen word and one signed real or imaginary part, the gradient norm is at most $\ell_0/\sqrt N$. Each normalized trace insertion costs $1/\sqrt N$ by trace Cauchy–Schwarz. On $k$ disjoint cubes the squared norm of the gradient of their sum is at most $k\ell_0^2/N$. All cubes bad forces one of $(4M)^k$ such centered sums to exceed $k\epsilon/(2\sqrt2)$. The log-Sobolev bound applied to the exponential of half the sum times a real parameter gives $\log\mathbb E e^{t(F-\mathbb EF)}\le t^2\mathrm{Lip}(F)^2/(2K_S)$ by integration in $t$. Optimize in $t$ and take a union bound:

$$
\mathbb P(\text{all bad})\le
\exp\!\left\{ k\log(4M)-\frac{\alpha N^2 k\epsilon^2}{16\ell_0^2}\right\}.
$$

The same proof uses no bias hypothesis if each loop is centered at its finite-volume mean. For the planar center one must control the finite-rank error and the boundary error at the chosen depth. One must also absorb the entropy, for example by taking $N^2\ge32\ell_0^2\log(4M)/(\alpha\epsilon^2)$. Single-cube estimates alone cannot be multiplied under an interacting law.

With a specified $W$, the bad event in (LD) is well defined. A single choice of tolerance and length cutoff controls only that resolution. It yields neither a full rate function nor factorization for every fixed loop to arbitrary accuracy. At coexistence, failure requires that accessible states differ on the tested words by more than the allowed tolerance. Likewise the proposed choice $L\sim m^{-1}\log(1/\epsilon)$ needs a quantitative bound on boundary influence, including its prefactor.

### 6. Theorem T, lines 187–200 — FAILS as an implication proved by this architecture

A route through good and bad regions is **ARGUED**. The threshold and the claimed loss from $m$ to $m/2$ are **GUESSED**. There is no counterexample here to clustering of the actual weak-coupling $SU(N)$ Wilson law. The first missing implication is line 195, even granting (PS) and a version of (LD) for large ranks.

1. **Good cubes.** A cutoff $\chi$ introduces $\mathbb E[\sum_a(d_aW)(d_a\chi)]$ into integration by parts. Its support, size, and normalization after conditioning need bounds. Pinning a fixed list of traces within $\epsilon$ gives an absolute error at most $k\epsilon$ for a product of $k$ unit-bounded factors from that list. It gives no relative error when a planar moment is zero. It gives no estimate for a long word. For a single holonomy, take the full sets of $j$th and $(j+2)$th roots of unity with equal multiplicities within each set, at common rank $j(j+2)$, for odd $j\ge3$. Both matrices have determinant one. Their first $j-1$ normalized power traces agree, yet their $j$th traces are 1 and 0. This illustrates the missing long-word estimate. The coefficient $n_e/N^2$ in a row with many passages persists under pinning.
2. **Response on a good region.** One needs an equation for the change caused by a boundary condition or a second insertion. It must have a source localized at that perturbation and errors bounded by a small multiple of the response. It must hold on regions with holes and with fixed exteriors. (PS) bounds the residual of one single-loop variation about $W$. Neither (PS) nor a fixed-tolerance deviation event estimates the connected product terms of this equation. Q proves decay down to a floor for a different operator. Sending separation to infinity at fixed $N$ leaves the floor. As a diagnostic, variables $X_x=W_x+Z\min(\epsilon/2,1/N)$ with a common symmetric sign $Z$ all stay good and have a constant nonzero covariance. This is a test of the inference from pinning, outside the Wilson model.
3. **Bad regions and boundaries.** Tile by side-$L$ cubes. From a connected set of $j$ interior cubes, a fixed coloring extracts at least $j/q_d$ mutually separated cubes, for a dimension-dependent $q_d$. For instance take block coordinates modulo three in each direction. (LD) bounds the probability that the entire set is bad by $\exp(-cN^2j/q_d)$. This bounds bad paths by a union bound over connected sets. A connected expansion of the *law* also needs factorization or a conditional mixing estimate across good regions, control of signed cutoff terms, and stability under conditioning. Blocks in the exterior collar have no (LD) bound. The claimed conclusion includes observables in that collar.
4. **Count of ranks.** Suppose connected sets cost at most $A_d^j$ in number per root. Suppose, in addition, the construction costs at most $a^{bL^4\ell_0j}$ in loop weights. To retain rate $m/2$ in lattice units, allow also a factor $\exp(b_d m L j)$ for the diameter. A sufficient schematic budget for this sum is

$$
cN^2/q_d>\log A_d+bL^4\ell_0\log a+b_d mL+\text{positive margin}.
$$

The square root in line 189 follows algebraically **if** the assumed length budget dominates and the other costs have been paid. The note bounds neither how often a cube is read nor how many loop letters those reads cost. There can also be a lower rank threshold from the good-region error and the bias bound. The number of loop choices already included in (LD) should not be charged twice. No threshold $C(L^4\ell_0/c)^{1/2}$ has been derived.
5. **Transfer conclusion — HOLDS AFTER CORRECTION (PROVED conditional on floor-free clustering).** Require $C(s)$ to be uniform under translations of a fixed shape and in volume and exterior. Otherwise even $C(s)=2e^{m r(s)/2}$ gives line 191 from boundedness alone. Use a stationary, reflection-positive state with positive transfer operator in the reconstructed sector. For a centered reflected loop vector $v$ the asserted decay would give $\int e^{-tE}\,d\mu_v(E)\le C_v e^{-mt/2}$ for lattice times $t$ (a fixed support offset changes $C_v$). Thus $\mu_v([0,E_0])\le C_v e^{-(m/2-E_0)t}\to0$ for each $E_0<m/2$. The spectral projection vanishes on the closed linear span of these vectors. No uniform bound on $C_v$ over a dense set is needed. For a full gauge-invariant transfer gap, identify that span with the centered physical Hilbert space. On a finite graph, tree gauge reduces the observable algebra to simultaneous conjugation of cycle holonomies. Traces of words and their conjugates separate the resulting unitary orbits: equal word traces give equal characters of the two representations on the compact closure of the paired holonomies, hence unitary equivalence. A scalar adjusts the conjugator to determinant one. Stone–Weierstrass gives density for continuous invariant functions. One still needs the transfer representation and passage to the chosen infinite-volume sector. General time-dependent fixed exteriors need not define a stationary transfer operator.

### 7. The $U(N)$ twin, lines 42–46, 89–107, 175–176 and 202–215 — FAILS at “must”

**PROVED algebra.** The last term has an order-one coefficient. On a charge-conjugation-even factorised state its value is zero. Its derivative can survive on an orientation-odd perturbation through $W(l)[\delta(p)-\delta(p^{-1})]$. It vanishes on even perturbations of that state. This identifies a candidate mechanism. It does not select a common master field, a fluctuation law, or a mass. Jafarov's Theorem 8.1 already displays the finite-rank expansion term with both orientations. Summing the distinguished-loop current $t_1t_e$ over the choice of distinguished loop gives $t_e^2$. [Jafarov](https://arxiv.org/abs/1610.03821)

**FAILS at the first implication in line 176.** (PS) has one loop as unknown. Q requires TPS on sequences. Even Q has a fixed-rank floor and no $N^{-2}$ prefactor in its spatial term. Multiplying it by $N^2$ and taking a planar limit at fixed separation gives no bound on the proposed scaled covariance. A photon comparison would need a weak-coupling result for the *coupled* $U(N)=(SU(N)\times U(1))/\mathbb Z_N$ Wilson law, an observable with nonzero overlap, and control of its residue and of the order of limits. A $U(1)$ result on its own does not give any of these. At fluctuation order the $t_e^2/N^2$ correction can survive rescaling, and the merger supplies sources even though its coefficient is common to the groups. The groups also differ in trace constraints, and physical solution selection may differ. Even a proved difference in their spectra would not locate its cause in a single term. A small-$\beta$ physical gap for both groups does not establish either twin of (PS).

**Endpoint checks.** At $U(1)$ every split and merger preserves the current. Summing their signs moves $t_e^2$ to the left, giving line 204 exactly. Dividing the recurrence by a nonzero charge changes a coefficient only. At $SU(2)$ the real trace kills the last term and the current coefficient is $1/4$. The trace product identity relates the resulting observables. There is no asymptotic small parameter at this fixed rank. The cutoff condition for even $\ell=1$ is $\kappa(a'/a)\le1$. Nothing in the proof computes $N_0$ or forces $N_0>2$ by construction. The proposed bulk transition, monopole estimate and weak photon overlap remain **GUESSED** here. Coexistence detectable by local probes can obstruct uniform mixing over exteriors, while the individual phases can still have isolated, gapped responses.

RESULT: HOLDS for the SU(N) edge identity, conditional Theorem Q, and Proposition N in its winding sector, with exact amplification $(3^n-1)/(2n)$. HOLDS AFTER CORRECTION for Q1 and for local isolation under (PS). FAILS for the $3/5$ cutoff, all-rank (LD), the spectral equivalence, the proposed proof and rank count for T, and the necessary photon mechanism. The weak-coupling gap and the SU(2) purity target remain open.
