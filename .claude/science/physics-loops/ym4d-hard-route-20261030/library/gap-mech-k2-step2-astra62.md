# Repo search

Row 1552, working tree `325e79f87`. The five local refs searched were `origin/main` at `8b11ae2bb95e`, `pr/10114` at `f76f6c649cff`, `pr/10133` at `89faef229ff6`, `pr/10134` at `1e70c7211a2c` and `pr/10141` at `c73ad7b177d9`. Markdown/TeX searches for `K2-STEP`, `PUR-io`, full electric Gram, electric Gram determinant, chromoelectric triad and log-cosh with Gram or determinant returned no hits on those refs. Searches for exponential type with coarse links, zero counting with soft blocks, meromorphic Gram profiles, fixed or identical plaquette traces, and electric volume with Fourier or harmonic also returned no hits. The checkout outside this lane had no target hit. The row-specific prior inventory is absent. FINISH row 1552 has no separate “Repo prior work” entry.

- The soft-route search found `ym4d-existence/EXISTENCE.md`, Proposition $\mathrm{LAP}^S$, and snapshots of it. For $g'_m\le1/2$, $0<r\le1/(2\pi)$, it bounds $\Pr(|V_p-1|<rg'_m\mid U)\le3\pi r\exp[4\kappa(e-1)/(3\sqrt N)]$. Its product-kernel proof treats one plaquette. The present test compares the orientations of three plaquettes at identical elementary traces. The November 8 digest covers earlier UV and witness problems. Registry R10 asks for decay of posterior score covariances at $\beta\in[2,3]$. Neither supplies or owns this profile test. [Soft-route proposition](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md#L1622) · [Prior digest](prior/repo-search-2026-11-08.md) · [Registry](open-registry.md#rows-added-2026-11-25-lead-seed-attacks-rows-1510-1514)
- Row 1468 §§3.2, 4.2–4.3 defines the normalized soft map, the interaction norm and the tube inclusion. Row 1544 excludes globally entire actions for nonconstant gauge-invariant images. For $\kappa=a\beta$ on its untwisted tori with $N\ge4$ time slices, first spatial period divisible by four and other spatial periods at least two, it gives positive conditional mutual information between two spatial bonds separated in time by at least $\lfloor N/2\rfloor-1$, outside a finite set of $\beta$ per torus and $a$. Row 1549 allows an arbitrary function of elementary plaquette traces. Its pair of labelled configurations reads $[B(\sin^2 t)-B(0)]/32$ and yields a positive error per patch for nonconstant polynomials $B$. Its two-atom example realizes $\cosh(c\sin t)$ on a one-link circle. I use its trace cancellation and packing idea, and derive the geometry and the estimates below. Under its UV witness, §9 of `gap-solve2-astra62.md` locates an uncancelled zero or pole of the thermal ratio $Z_T(z)^2/Z_{2T}(z)$ in $|z|\le\beta(1+m^{-1/2})$ at sufficiently fine cutoffs. Its variable is a coupling. [Step design](gap-k2-tool-design-fable.md) · [Entire-action and range exclusions](gap-mech-k2-solve-astra62.md) · [One-link test](gap-mech-k2-step-astra62.md) · [Thermal ratio](gap-solve2-astra62.md)
- Sussman and Alpoge, with Claude and Codex, give the Wilson one-bond multipliers $2e^{-\beta}I_{2l+1}(\beta)/\beta$ in outline GL3, lines 2197–2231. B3, lines 3986–4005, asks for the one-loop increment and controlled errors. CA-II 27042–27075 gives an accumulated law under H7, the correlation-theorem flow and the one-loop lemma. CA-I 872–892 describes Bałaban's Dirac push-forward. These concern a different step or regime. Outline 31870–31884 gives a spectral example with support reaching zero, and CA-I 2706–2710 excludes the gap from the cited conclusion. Source revision supplied for the outline and account is `31a47c543775`. [Index](sa-index/README.md) · [Obligations](sa-index/obligations.md) · [Bałaban source record](lit-balaban.md)

## Plan and choice of test

The initial plan was to check ownership, compare a three-link slice with the exact soft kernel, then test any obstruction against the full tube and wrap allowance. Turning three links $\cos t+v_i\sin t$ with orthogonal imaginary axes gives squared volume $\sin^6 t$. A comparison with coplanar axes cancels a common trace action in a ratio. Rotating the three **colour directions** of traceless links holds that trace action constant throughout the circle. This gives a bound on the density itself and an explicit Fourier test.

**Class excluded.** Take a centre consisting of any summable interaction among elementary plaquette traces, plus the hypercubic average of $\lambda\log\cosh(c\sqrt{J_y})$ at each site, with $c>0$ and real $\lambda\ne0$. At every bounded soft strength the log error of representing a $Q_2$ image by such a centre alone is at least a positive constant times the volume on large untwisted tori. Theorem (8) gives the trade with an additional interaction depending on the full matrices. It also applies to the broader analytic class specified by (5)–(6).

## A circle of fields with constant plaquette traces

Write a coarse $SU(2)$ link as a unit quaternion. For each signed permutation $h$ of the four axes based at $y$, traverse each of its three electric plaquettes first along the distinguished axis and then along a transverse axis. Let $E_i$ be the imaginary parts of the resulting holonomies. Write $J_y^h=\det[E_1,E_2,E_3]^2$. Simultaneous gauge conjugation rotates the three columns. Their lengths are at most one, so $0\le J_y^h\le1$. For a real analytic $B$ on a neighbourhood of $[0,1]$ write
```math
 A_B(V)=\sum_y\frac1{2^4 4!}\sum_h[B(J_y^h(V))-B(0)],
 \qquad E_B(w)=\exp\!\left(-\frac{B(w)-B(0)}{32}\right).
 \tag{1}
```
Here $E_B(0)=1$. Analyticity of $B$ on the physical interval initially gives only a local complex extension.

Use an untwisted coarse torus with all periods $L_\mu>20$. This also puts the ten-bond star inside the diameter cutoff of row 1468. In one time slab at spatial point $x$, mark the three forward time links at $x+e_1,x+e_2,x+e_3$. All spatial links and all unmarked time links equal $1$. In imaginary quaternion space choose a vertical unit $k$ and horizontal unit vectors $h_i=(\cos\phi_i,\sin\phi_i,0)$ at $\phi_i=2\pi i/3$, $i=0,1,2$, in an oriented orthonormal frame with third axis $k$. In order, the three marks are the pure unit quaternions
```math
 v_i(t)=h_i\cos(t+\phi_i)+k\sin(t+\phi_i).
 \tag{2}
```
Each mark has zero real part at all angles. Put a patch in every time slab at each spatial point with coordinates $0,4,\ldots,4(\lfloor L_i/4\rfloor-1)$ in direction $i$. Give these $M=L_0\prod_{i=1}^3\lfloor L_i/4\rfloor$ patches separate angles $t_j$.

Within a patch the spatial bases of any two marks have distance two. Across patches in a slab they differ by at least three in one cyclic coordinate, since the cyclic grid gaps are at least four. Each plaquette thus sees at most one mark and has normalized trace either zero or one, independent of **all** angles. A star with distinguished spatial axis has a trivial spatial plaquette. A time-directed star uses the time link at its spatial centre and three neighbouring time links of a single slab, above or below the base according to its time sign. If the central link is marked, the three neighbours are unmarked and the columns are parallel. Otherwise a nonzero determinant needs three marked neighbours from the same patch. The common neighbours of $x+e_1$ and $x+e_2$ are $x$ and $x+e_1+e_2$, and only $x$ neighbours $x+e_3$. At $x$ the three spatial signs must be positive. For the two possible base times and their corresponding time signs, the $3!$ permutations of the spatial axes give the same squared volume. This proves the multiplicity $2\cdot3!/(2^4 4!)=1/32$ in (1) for each patch.

The oriented horizontal area of $h_i,h_{i+1}$ in cyclic order is $\sqrt3/2$. In expanding the volume only terms with one vertical vector survive. Hence
```math
 \det[v_0(t),v_1(t),v_2(t)]
 =-\frac{\sqrt3}{2}\frac{d}{dt}\prod_{i=0}^2\cos(t+\phi_i)
 =\frac{3\sqrt3}{8}\sin(3t).
```
The product of cosines is $\cos(3t)/4$ by the triple-angle identity. Inversions of marked links leave the squared volume unchanged. With $\alpha=27/64$ and $w(t)=\alpha\sin^2(3t)$, the trace sector is constant on the entire product of circles and
```math
   \exp(-A_B(V(\mathbf t)))=\prod_{j=1}^M E_B(w(t_j)).
 \tag{3}
```

## What the soft kernel allows on this circle

Fix $0<\kappa\le\kappa_*<\infty$ and put $L=3\kappa_*$. The $Q_{2,\kappa}$ image of any nonzero finite positive fine measure has coarse density
```math
 D(V)=\int \exp\!\left(\kappa\sum_e M_e(W)\cdot V_e\right)d\xi(W),
 \qquad |M_e(W)|\le1.
```
Each $M_e$ is the mean of 384 unit contour holonomies. The real part of $M_e V_e^{-1}$ is the Euclidean dot product of the quaternions. Absorbing the reciprocal bond normalizers into the fine measure gives the finite positive measure $\xi$, independent of $V$. [Kernel definition, §3.2](gap-k2-tool-design-fable.md)

Write $dm(t)=dt/(2\pi)$ and normalize $D(V(\mathbf t))\,dm^M$ to a probability $Q$ on the angle torus. For every patch, conditional on earlier patch angles in any fixed ordering, the current angle has a density of the form
```math
 q_\pi(t)=\frac{f_\pi(t)}{\int f_\pi\,dm},\qquad
 f_\pi(t)=\int e^{u\cos t+v\sin t}\,d\pi(u,v),\qquad
 \operatorname{supp}\pi\subseteq\{u^2+v^2\le L^2\}.
 \tag{4}
```
Indeed, (2) is a rotation of an orthonormal pair in the plane spanned by $h_i,k$. Its exponent on one link is a first harmonic whose pair of coefficients has length at most $\kappa$. The three exponents add, so their coefficient pair lies in the radius-$L$ disk. Integrate the remaining positive factors over the fine law and all later angles. The resulting measure is independent of the current angle. Normalizing it and projecting to the coefficient pair gives the probability $\pi$. No independence of the fine contour means is needed.

**Analytic condition.** Set $p_B(t)=E_B(w(t))/\int E_B(w(s))\,dm(s)$. If $p_B=q_\pi$, the germ $E_B$ extends to an entire function and satisfies, for every $R>0$,
```math
 \log\max_{|w|\le R}|E_B(w)|
 \ \le\ \frac L2\big[(3+4R/\alpha)^{1/6}+3\big].
 \tag{5}
```

*Proof.* On $z=e^{it}$ the transform $f_\pi$ is the restriction of
```math
 f(z)=\int \exp\!\left((u-iv)z/2+(u+iv)z^{-1}/2\right)d\pi(u,v)
 \quad (z\ne0).
```
The integral is holomorphic on the punctured plane by uniform convergence on compact annuli, and $|f(z)|\le\exp[L(|z|+|z|^{-1})/2]$. Equality of the real densities gives $f(e^{it})/f(1)=E_B(w(t))$, since $E_B(0)=1$. Rotation of $z$ by $e^{i\pi/3}$ and inversion of $z$ both preserve the right side on the unit circle. The identity theorem extends both symmetries to the punctured plane.

For any complex $w$ solve $\zeta+\zeta^{-1}=2-4w/\alpha$ and take a sixth root $z$ of $\zeta$. The two values of $\zeta$ are reciprocals and the choices of sixth root differ by the rotation just proved. Thus $f(z)/f(1)$ defines a single-valued function of $w$. Local analytic roots make it holomorphic away from $0,\alpha$. The roots stay in compact annuli near both exceptions, so the singularities are removable. On $[0,\alpha]$ this function is the original $E_B$, which identifies its germ. Choose $|\zeta|\ge1$. Then $|\zeta|\le3+4|w|/\alpha$, $|z|^{-1}\le1$ and $f(1)\ge e^{-L}$. These bounds give (5). $\square$

**Profiles excluded by (5).** Let $D_0$ be entire, $D_0(0)=1$, and real positive on $[0,1]$. Every $B=\lambda\log D_0$ with real $\lambda\ne0$ is excluded if
```math
  \limsup_{R\to\infty}R^{-1/6}\log\max_{|w|\le R}|D_0(w)|=+\infty .
 \tag{6}
```
In fact, for $\lambda>0$ every nonconstant such $D_0$ is excluded.

To prove this put $p=-\lambda/32$. An extension $E$ from (5) would satisfy $E'/E=pD_0'/D_0$ as a meromorphic identity, by the equality near zero. At each zero of order $m$ of $D_0$ the residue on the right is $pm$. On the left it must be a nonnegative integer, the order of $E$ there. Away from both discrete zero sets the real function $\log|E|-p\log|D_0|$ is locally constant by the derivative identity. The complement is connected and the constant is zero at the origin. For $p>0$ this gives $\max_{|w|\le R}|E(w)|=(\max_{|w|\le R}|D_0(w)|)^p$, contradicting (6). For $p<0$ a zero of $D_0$ is already impossible. If $D_0$ has no zeros the derivative identity forces $E$ to have none either.

A zero-free entire $E$ satisfying (5) is constant. Indeed $E=e^g$ with $g$ entire, by integrating $E'/E$ and choosing $g(0)=0$. On the circle $|w|=R$, $\operatorname{Re}g$ has mean zero and is bounded above by the right side of (5), so its mean absolute value is at most twice that bound. For $n\ge1$, its $n$th Fourier coefficient is $R^n/2$ times the $n$th Taylor coefficient of $g$. Sending $R$ to infinity kills each such coefficient. A constant $E$ forces $D_0$ constant by the same derivative identity. This proves the assertion for $p<0$.

There is also a restriction on tuning any fixed nonconstant analytic shape $b$. If one nonzero amplitude $\lambda_0 b$ passes the circle test, its normalized weight is nonconstant and entire by (5). It therefore has a zero, of some order $m\ge1$, by the preceding zero-free argument. If $\lambda b$ also passes at any finite strength, the logarithmic derivatives of the two entire weights are in the ratio $\lambda/\lambda_0$. At that zero this forces $m\lambda/\lambda_0$ to be a nonnegative integer. Thus an interval of amplitudes cannot all be exact image profiles, even for shapes outside (6).

In particular $D_0(w)=\cosh(c\sqrt w)$, $c>0$, has a series in integer powers of $w$ and $\log D_0(R)\ge c\sqrt R-\log2$. The same exclusion holds for $D_0(w)=\int\cosh(a\sqrt w)\,d\mu(a)$ for any compactly supported probability on $\mathbb R$ with $\mu(\{0\})<1$. Its series converges locally uniformly and $D_0(R)\ge(m/2)e^{a_0\sqrt R}$ whenever $m=\mu(|a|\ge a_0)>0$. This includes the rules obtained by integrating a bounded symmetric auxiliary variable coupled linearly to signed electric volume.

## The cost in radius and wrap error

Let $S_{\rm tr}$ be any continuous function of all elementary plaquette traces and let $\mathcal R=\sum_X\mathcal R_X$ depend arbitrarily on the full link matrices. Set $\Gamma=\sup_e\sum_{X\ni e}\operatorname{osc}\mathcal R_X$, with oscillation taken over real link fields. Write $V_\Lambda=\prod_\mu L_\mu$ for the site count. For fixed $L,B$ define
```math
 d_{L,B}=\min_\pi\int p_B(t)\log\!\left(\frac{p_B(t)}{q_\pi(t)}\right)dm(t),
 \qquad \pi\text{ a probability on the closed radius-}L\text{ disk}.
 \tag{7}
```
The minimum exists. Probabilities on the compact disk are weakly compact. Weak convergence gives uniform convergence of $f_\pi$ on the circle by pointwise convergence and the common derivative bound $Le^L$. On the real circle $e^{-L}\le f_\pi\le e^L$, so normalization and the integral in (7) are continuous. Relative entropy is nonnegative, with equality only for equal probability densities, by strict convexity of $x\log x$. Here the densities are continuous and positive. Consequently $d_{L,B}>0$ whenever (5) fails. A compact collection of excluded $B$ in $C[0,1]$ has a common positive minimum by the same argument. In particular $\lambda,c$ may range over compact sets avoiding zero. Allowing either parameter to tend to zero can remove the uniform separation, since $q_{\delta_0}=1$ is available and $p_B\to1$ in that limit with the other parameter fixed.

**Theorem.** If an image $D$ as above satisfies, on one untwisted torus of the stated size,
```math
 \big|\log D(V)+eV_\Lambda+S_{\rm tr}(V)+A_B(V)+\mathcal R(V)\big|
 \le\eta\qquad\text{for every }V,
```
with any site constant $e$, then
```math
                       3\Gamma+\frac{2\eta}{M}\ \ge\ d_{L,B}.       \tag{8}
```

*Proof.* Let $P$ have the product angle density $\prod_j p_B(t_j)$, and let $Q$ be the image angle law in (4). By the chain rule for densities,
$D_{\rm KL}(P\|Q)$ is the sum over patches of the mean under the earlier $P$ angles of the conditional relative entropy. Each term is at least $d_{L,B}$ by (4) and independence under $P$. Equivalently, factor the two joint densities into successive conditional densities, take the logarithm of the ratio and integrate under $P$.

In the other direction put $Y(\mathbf t)=\log D(V(\mathbf t))+A_B(V(\mathbf t))$. Then $D_{\rm KL}(P\|Q)=\log\mathbb E_P e^Y-\mathbb E_PY\le\operatorname{osc}Y$, by (3). The site constant and $S_{\rm tr}$ have no angle dependence. Two arbitrary angle configurations can be connected by changing at most $3M$ individual marked links, giving $\operatorname{osc}\mathcal R(V(\mathbf t))\le3M\Gamma$. The two endpoint errors contribute at most $2\eta$. Combining the bounds proves (8). The auxiliary integration tests the pointwise realization required by §4.2. It makes no assumption about the Haar probability of the tested configurations. $\square$

**Application to (K2-STEP).** For a row-1468 tube centred at $S_{\rm tr}+A_B$, an output residual of norm at most $\rho$ at readout $x'\ge1$, rate $r>0$ and weight $\theta$ has
```math
 \Gamma\le C(x',r,\theta)\rho,\qquad
 C(x',r,\theta)=2\sup_{m\ge1}(1+3\theta x'm)e^{-rm}.
```
In a support of $m$ bonds, four bond incidences belong to each contained unoriented elementary plaquette and each bond lies in six plaquettes. Thus the local energy $E_X$ in that norm is at most $2(6m/4)=3m$. Apply $\operatorname{osc}\mathcal R_X\le2\sup|\mathcal R_X|$ to each weighted summand. Each periodized term of diameter below half the shortest period through a specified torus bond lifts through a fixed copy of that bond, so the torus sum obeys the same bound.

Fix a nonempty input tube and $\kappa=ax_k\le\kappa_*$. If, on one untwisted member with shortest period $s$, the output allowance obeys
```math
 3C(x',r,\theta)\rho_{k+1}
   +\frac{2}{M}\left(\eta_k+V_\Lambda e^{-rs/8}\right)<d_{L,B},  \tag{9}
```
then no input image belongs to that output tube. This disproves the required sixteen-torus inclusion for families with such an output level. For spatial periods divisible by four, $M=V_\Lambda/64$. A rule whose entire colour dependence is (1) therefore requires $\eta\ge d_{L,B}V_\Lambda/128$ at these periods. For arbitrary periods above twenty, $\lfloor L_i/4\rfloor\ge L_i/5$ gives $\eta\ge d_{L,B}V_\Lambda/250$. On the larger tori required by the torus-free design, subextensive inherited error and the stated wrap increment cannot meet this cost as $s\to\infty$ at fixed aspect. The same exclusion holds for any fixed positive radius with $3C\rho<d_{L,B}$ in that limit. On a single fixed side, (9) retains the actual error budget. The unknown margin in (C5) supplies no numerical comparison with $d_{L,B}$. [Tube, norm and wrap allowance, §§4.1–4.3](gap-k2-tool-design-fable.md)

## A finite real witness for a profile accepted by the one-link test

Take $B(w)=-32\log\cosh(c\sqrt w)$ with $0<c\le\kappa$, and put $A=c\sqrt\alpha$. On row 1549's one rotating link the required odds are $\cosh(c\sin t)$, realized exactly by equal disk atoms $(0,\pm c)$ against the atom $(0,0)$. The factor $32$ accounts for the hypercubic average. On the new circle the target density is $\cosh(A\sin3t)/I_0(A)$.

For $r\ge0$, the $k$th Fourier coefficient of $e^{r\cos t}$ for $k\ge0$ is
```math
 I_k(r)=\sum_{\ell\ge0}\frac{(r/2)^{k+2\ell}}{\ell!(k+\ell)!}.
```
This follows by multiplying the series for $e^{r e^{it}/2}$ and $e^{r e^{-it}/2}$. For any density (4), rotation of the disk atom of radius $r$ adds a phase to its Fourier coefficient. Since $(k+\ell)!\ge k!\ell!$, $I_k(r)\le (r/2)^k I_0(r)/k!$. Integrating atoms and dividing by their integrated $I_0$ gives $|\widehat q_\pi(k)|\le(L/2)^k/k!$. For $p_B$, averaging the two signs in the cosh keeps the even harmonics and the sine shift gives $\widehat p_B(6n)=(-1)^n I_{2n}(A)/I_0(A)$. In particular, put
```math
 a_n=e^{-A}\frac{(A/2)^{2n}}{(2n)!},\qquad
 (2n+1)^4\ge 2e^A\,\frac{(L/2)^6}{(A/2)^2},\qquad n\ge1.       \tag{10}
```
Such an integer always exists. The first series term and $I_0(A)\le e^A$ give $|\widehat p_B(6n)|\ge a_n$. Using $(6n)!/(2n)!\ge(2n+1)^{4n}$ in the image bound gives $|\widehat q_\pi(6n)|/a_n\le e^A(2e^A)^{-n}\le1/2$.

The expectations of $(-1)^n\cos(6nt)$ under the two laws therefore differ by at least $a_n/2$. For any $|f|\le1$, the log moment generating function of $f$ under $q$ has second derivative a tilted variance at most one. Nonnegativity of relative entropy against the exponential tilt of $q$ gives $D_{\rm KL}(p\|q)\ge t(\mathbb E_p f-\mathbb E_q f)-t^2/2$ for real $t$. Optimizing yields $d_{L,B}\ge a_n^2/8$.

For example choose $2\le\kappa\le3$, $L=9$ and $c=8/(3\sqrt3)$, so $A=1$ and $c\le2$. The choice $n=12$ in (10) works since $8e(9/2)^6<24\cdot5^6<25^4$. Thus one cosine at frequency $72$ gives the explicit bound
```math
                  d_{9,B}>\frac{1}{72(2^{24}\,24!)^2}.           \tag{11}
```
This arithmetic uses $e<3$ from its series. It is a hand bound on the error of the class, with no numerical proof input.

There are nonconstant analytic profiles for which this circle test passes. For $B(w)=-32\log(1+\epsilon w)$ the target is $1-\delta\cos6t$ after normalization, where $\delta=(\epsilon\alpha/2)/(1+\epsilon\alpha/2)$. Take disk atoms at a fixed radius $0<r\le L$ with angular density $1-[\delta I_0(r)/I_6(r)]\cos6\phi$ relative to $dm(\phi)$. This is a probability for sufficiently small $\epsilon>0$ since $I_6(r)>0$. Its normalized transform is exactly the displayed target density by the same Fourier calculation. Realizing a single conditional circle leaves the joint-field inclusion open.

## Selectivity, purity and the outstanding estimate

Use the full Gram matrix of all $d-1$ electric plaquettes for each distinguished direction. In four-dimensional compact $U(1)$ the three imaginary parts lie in a real line. In five-dimensional $SU(2)$ four imaginary parts lie in $\mathbb R^3$. In both cases every full Gram determinant equals zero, even before averaging orientations. The colour factor in (3) is identically one. At fixed plaquette traces its normalized angle density is constant, which the disk mass at the origin realizes. Thus the positive lower bound from this rank test disappears. The rank of the three actual colour vectors in (2) is precisely where the proof distinguishes four-dimensional $SU(2)$. The exclusion uses the uniform realization clause on real fields. It yields no sign for the typical-field stiffness.

For the specified release witnesses put $n=\ell b^K$, $u=n/512$. The seed asks whether $Z_+(2u)/Z_+(u)^2\ge457/625$ for infinitely many calibrated cutoffs at one $\ell,g_0$. Equations (5) and (8) concern normalized angle conditionals within one torus. Multiplying all short-period input densities by $c_u>0$ and all long-period inputs by $c_{2u}>0$ preserves the conditionals and multiplies the purity by $c_{2u}/c_u^2$ in the general class of positive inputs. There is also a Wilson separation at the same box geometry. At fixed $n,u>2$ the sixteen normalized-Haar Wilson masses tend to $1$ as $\beta\downarrow0$, by bounded convergence. At that same box, check 1527(iii) gives $P\asymp_{n,u}\beta^{-3/2}/\log\beta$ as $\beta\to\infty$. For a fixed testing strength the same lower bound (8) holds in both cases. Choosing a coupling separately on each box can thus put purity on either side of the threshold throughout a sequence. Those sequences are uncalibrated. This establishes the distinction between the class test and a seed criterion without making any inference about the value of calibrated purity. [Fixed-box Wilson estimate and its range](gap-agy-seed-approaches-neon-check-astra62.md) · [Seed, §3.1](gap-k2-tool-design-fable.md)

The open positive statement is to find torus-independent centres and $a,r,\delta_0>0$ for which, on all sixteen tori throughout the band,
```math
 Q_{2,ax_k}\mathcal T_k\subseteq\mathcal T_{k+1},\qquad
 x_{k+1}\le x_k-\delta_0,\qquad
 \rho_{k+1}\le\bar\rho(x_{k+1}),\qquad
 \eta_{k+1}\le\eta_k+V_\Lambda e^{-rs/8},
```
from $x_0\in[H,W_*]$ to $\|\Phi_N^*\|+\rho_N\le\varepsilon_E$, with the radius inside the (C5) margin. An excluded profile requires additional colour dependence or enough error to pay (8). At the flat field each electric imaginary part is first order in link perturbations, hence $J$ vanishes to at least sixth order and $B(J)-B(0)$ has zero Hessian there. The missing estimate is a signed decrement for the transverse Hessian in a class also satisfying the radius and wrap bounds. The rank distinction above does not supply that estimate. All new proofs here are by hand. Independent review and Lean checking are outstanding.

RESULT At finite soft strength, arbitrary elementary-plaquette-trace interactions plus any nonzero multiple of the hypercubic log-cosh electric Gram profile cannot satisfy (K2-STEP) with the radius and wrap budgets in (9). With no other colour dependence the required log error is extensive. The general step, (PUR-io) and the mass gap remain open.
