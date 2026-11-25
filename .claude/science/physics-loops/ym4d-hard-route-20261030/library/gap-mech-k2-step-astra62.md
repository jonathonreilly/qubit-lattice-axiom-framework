# Repo search

Row 1549, checkout `7439be50a1c2`. The row-specific prior file and a separate “Repo prior work” entry are absent. I searched Markdown and TeX on `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). Searches for `K2-STEP`, `PUR-io`, ferromagnetic loop actions, chromoelectric triads, electric Gram determinants, identical plaquette traces and ratios of soft-block densities found no statement of the target or the obstruction below. The checkout outside the lane produced no target hit. The nearest sources were as follows. [November 8 search](prior/repo-search-2026-11-08.md)

- On PRs 10114 and 10133, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (11) gives $C_F(a)\geq e^{-68\beta}/[16(1+1/(4r_f^4))]$ for a centred fundamental plaquette of $SU(2)$, $r_f=I_2(\beta)/I_1(\beta)$. `EXISTENCE.md`, Proposition LAP$^{S}$, gives $\Pr(|V_p-1|<rg'_m\mid U)\leq3\pi r\exp[4\kappa(e-1)/(3\sqrt N)]$ for $g'_m\leq1/2,\ 0<r\leq1/(2\pi)$ in its kernel. Each concerns one plaquette. [Transfer witness](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L149) · [Soft-plaquette bound](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md#L1622)
- In the lane, Lemma V gives the one-link moment $\mathbb E[(v\cdot q)^2]\geq |v|^2/(4+t)$ at concentration $t$. I use it in (1). Row 1434 finds residual character coefficients of both signs infinitely often after extracting one positive plaquette-character term from a straight-product marginal. Row 1544 excludes entire $Q_2$ actions and, off a finite coupling set on each torus, fixed temporal range. Its check supplies the comparison kernels. Registry R10 concerns decay of posterior score covariances. None of these statements controls the change of colour axes at fixed elementary plaquette traces. [Lemma V](gap-pag-grow-astra.md) · [Row 1434](gap-mech-candidate-astra62.md) · [Row 1544](gap-mech-k2-solve-astra62.md) · [Check 1548](gap-mech-k2-solve-astra62-check-opus.md) · [Registry](open-registry.md)
- Sussman and Alpoge, with Claude and Codex, derive positive one-bond multipliers in outline GL3, lines 2197–2231. B3, lines 3986–4005, requests a controlled one-loop increment. CA-II 27042–27075 proves its accumulated law given H7, the correlation-theorem flow and the one-loop lemma. CA-I 872–892 defines a Dirac push-forward for Bałaban's map. The present step uses the normalized soft kernel of row 1468 at order-one coupling. The outline's example at 588–599 and 31870–31884 has spectral support down to zero. CA-I 2706–2710 expressly lists “a mass gap” among the conclusions outside Theorem 0. [Outline index and obligations](sa-index/README.md) · [Outline](../../../../../../sa/YM4_sketch_500.tex) · [CA-I](../../../../../../sa/theorem_0_complete_account_raw_I.tex) · [CA-II](../../../../../../sa/theorem_0_complete_account_raw_II.tex) · [Bałaban source record](lit-balaban.md)

## Test chosen

The initial plan was to test signs of infinitely many loop couplings. Row 1434 already treats a related sign obstruction, and the one-link growth bound by itself also applies in the comparison models. The selected class keeps interactions among plaquette angles at arbitrary range. A local polynomial in the squared volume of the electric colour vectors supplies information about their relative orientations while preserving the quadratic readout. Equations (3) and (7) give the minimum error or radius this rule requires. Equation (9) tests a larger class when the rule strongly penalizes that volume. These are hand arguments for a research row.

At strength $\kappa=a x_k$, the image on one coarse torus is

$$
 D(V)=\int D_{\rm in}(W)\prod_c
 \frac{\exp\{\kappa M_c(W)\cdot V_c\}}
      {\int_{S^3}\exp\{\kappa M_c(W)\cdot q\}\,dq}\,dW .
$$

Here the integrals use normalized Haar measure for each link. The quaternion $M_c$ is the mean of the $16\cdot4!$ side-two contour transports, so $|M_c|\leq1$. The kernel preserves the mass of each incoming torus density. [Definition and twist carry, §3.2](gap-k2-tool-design-fable.md)

## A selective bound on three electric plaquettes

Use unit quaternions, with the imaginary quaternions identified with Euclidean three-space. Fix a coarse site $y$ and an oriented time axis 0. For $i=1,2,3$ let $P_i$ be the holonomy of the $0i$ unit plaquette based at $y$, traversed first in direction 0. Set

$$
 E_i=\operatorname{Im}P_i,\qquad
 J_y=\det[(E_i\cdot E_j)_{1\leq i,j\leq3}]
     =\det[E_1,E_2,E_3]^2,\qquad 0\leq J_y\leq1.
$$

Simultaneous gauge conjugation rotates all three vectors by the same orthogonal matrix. In dimension $d$ use all $d-1$ plaquettes transverse to the chosen axis in the Gram determinant. Write $G_y$ for its average over the signed permutations of the $d$ coordinate axes based at $y$. This gives a hypercubic, nonnegative local action term. In four dimensions its Taylor expansion at the identity starts in degree at least six.

**Moment bound.** On a torus with periods at least four, every normalized $Q_{2,\kappa}$ image of a positive fine density in four-dimensional $SU(2)$ satisfies

$$
                 \mathbb E J_y\ \geq\ m_\kappa,\qquad
                 \mathbb E G_y\ \geq\ m_\kappa,\qquad
                 m_\kappa=\frac{6}{(4+\kappa)^3}.
\tag{1}
$$

The bound for each oriented determinant also holds conditional on the fine field and all coarse links except the three spatial edges opposite its base time slice. A local lift of a twisted configuration changes some link signs, which are orthogonal transformations of the quaternion and preserve the Gram determinant.

Indeed, for the displayed orientation leave $V(y+\hat0,i)$, $i=1,2,3$, free. Given the fine field, the coarse links are independent. With the other coarse links fixed, each $P_i$ is a left and right translate of one of the three free links, with inversion allowed for a reversed orientation. Its conditional quaternion law has density proportional to $\exp(t h\cdot q)$ on $S^3$, where $|h|=1$ and $0\leq t\leq\kappa$. The three laws are independent. The checked one-link moment estimate gives $\mathbb E [(v\cdot q)^2]\geq |v|^2/(4+t)$ for every $v\in\mathbb R^4$, including imaginary vectors. This is an uncentered second moment. [Lemma V, lines 418–450](gap-pag-grow-astra.md) · [Check, §6](gap-pag-grow-check-opus.md)

Let $S_i=\mathbb E[E_i E_i^\mathsf{T}]$ in these conditional laws. For the alternating tensor $\epsilon_{abc}$ in three dimensions, independence gives
$\mathbb E J_y=\langle\epsilon,(S_1\otimes S_2\otimes S_3)\epsilon\rangle$.
Each $S_i\succeq(4+\kappa)^{-1}I_3$. Diagonalizing each factor gives the product lower bound, and $\|\epsilon\|^2=6$. Integration and averaging orientations give (1). In particular the probability that $J_y\geq m_\kappa/2$ is at least $m_\kappa/(2-m_\kappa)$, by $J_y\leq1$.

For a large-volume probability bound, take $m$ forward stars with disjoint bonds, for example at coordinates spaced by four in all directions with the same spacing across the periodic seam. Conditional on the fine field, the $m$ indicators of $J_y\geq m_\kappa/2$ are independent, each with probability at least $p=m_\kappa/(2-m_\kappa)$. For their sum $N_g$, $\mathbb E[2^{-N_g}\mid W]\leq(1-p/2)^m$. Hence the probability of $N_g<pm/2$ is at most $\exp[-(1-\log 2)pm/2]$, under any incoming law.

In four-dimensional compact $U(1)$ the three electric plaquettes have imaginary parts in a one-dimensional Lie algebra. In five-dimensional $SU(2)$ the four electric plaquettes have imaginary parts in a three-dimensional Lie algebra. Their full spatial Gram determinant is identically zero in both cases. This comparison uses the same definition in each dimension. The positive side of (1) measures a feature of the actual coarse law even at order-one strength.

## An obstruction with arbitrary interactions among plaquette traces

Let $\tau_p(V)=\tfrac12\operatorname{tr}V_p$. For a real polynomial $B$, put

$$
 A_B(V)=\sum_y \frac{1}{|H_4|}\sum_{h\in H_4}
                   \big[B(J_y^h(V))-B(0)\big],
$$

where $H_4$ is the group of signed axis permutations and $J_y^h$ uses the oriented plaquettes specified by $h$. The linear case $B(u)=\lambda u$ gives $\lambda\sum_yG_y$. Consider local rules with action

$$
           S(V)=S_{\rm tr}((\tau_p(V))_p)+A_B(V)+R(V).
\tag{2}
$$

Here $S_{\rm tr}$ can contain arbitrary summable interactions among any number of plaquette traces, with either sign and unbounded range. The finite-torus theorem allows any continuous joint function of all the traces. For centres with a transverse readout, restrict to rules with the required Hessian at the flat field. The remainder $R=\sum_X R_X$ can depend on the full link matrices. Write

$$
             \Gamma=\sup_e\sum_{X\ni e}\operatorname{osc} R_X,
 \qquad \operatorname{osc} f=\sup f-\inf f ,
$$

for its per-bond oscillation on the torus. Define $V_\Lambda=|\Lambda|$ to count coarse sites. A torus constant is unrestricted.

The class contains smooth rules at a prescribed readout $x'$ with genuine tails. For example, start $S_{\rm tr}$ with the Wilson action at $x'$ and add the sum of $e^{-j^2}w(\tau_p)w(\tau_{p+j\hat\mu})$ over plaquettes, signed axes and $j\geq1$, where $w(t)=(1-t)/(2+t)$. Include a straight connecting path in the support, averaging over symmetry-related choices if needed. These supports have size $O(j)$, the interaction has finite weighted norm at each fixed $r$, and each product starts in degree four at the flat field. The added $A_B$ also preserves the readout. The free trace sector can therefore have both non-entire dependence and unbounded temporal range.

**Theorem.** Fix $0<\kappa<\infty$ and a nonconstant real polynomial $B$. There is $d_{\kappa,B}>0$, defined in (5), independent of the input and torus. Let the periods $L_\mu$ of an untwisted coarse torus be at least four and $M=L_0\prod_{i=1}^3\lfloor L_i/4\rfloor$. If a positive $Q_{2,\kappa}$ image density $D$ satisfies

$$
        |\log D(V)+eV_\Lambda+S(V)|\leq\eta\quad\hbox{for all }V ,
$$

then

$$
                         \boxed{\quad \Gamma+\frac{2\eta}{M}\ \geq\ d_{\kappa,B}.\quad}
\tag{3}
$$

On the seed geometries with spatial periods divisible by four, $M=V_\Lambda/64$. With $R=0$, (3) then requires $\eta\geq d_{\kappa,B}V_\Lambda/128$ already on the untwisted member. Arbitrary trace interactions plus $A_B$ alone therefore cannot give one such step with subextensive log error on arbitrarily large fixed-aspect tori. This includes non-entire trace functions and interactions of unbounded temporal range.

**A test that keeps every plaquette trace fixed.** Fix one site $y$. Set all links to the identity except the three forward temporal links based at $y+\hat e_1,y+\hat e_2,y+\hat e_3$. In that order give them the quaternions

$$
 \begin{array}{c|ccc}
  &1&2&3\\ \hline
  A&{\bf i}&{\bf j}&\cos t+{\bf k}\sin t\\
  B_0&{\bf i}&{\bf i}&\cos t+{\bf k}\sin t .
 \end{array}
$$

Write $B_0$ for the second configuration. Any elementary plaquette meets at most one marked link, since the marks are parallel and their spatial bases have pairwise distance two. Thus the two configurations have identical elementary plaquette traces for every $t$. In $B_0$ the plaquette holonomies have imaginary parts spanning at most two colour directions everywhere. In $A$ a nonzero determinant needs all three distinct marks. Its distinguished axis must be temporal, since the spatial plaquettes are trivial. If the common temporal link were marked, its spatial neighbours would all be unmarked and all three columns would be parallel. The three marks must therefore occupy the three spatial neighbours selected by the star. Their only common nearest neighbour is the spatial position of $y$. The first two marks have common neighbours $y$ and $y+\hat e_1+\hat e_2$ in the spatial slice, and only the former neighbours the third. All three spatial signs must be positive. There is one allowed time sign at $y$ and its reverse at $y+\hat0$. At either base the three spatial axes can be permuted freely, giving $3!/(2^4 4!)=1/64$ of the signed permutations. Each surviving $J$ equals $\sin^2 t$. Hence the action difference contributed by $A_B$ is exactly

$$
                    H(t)=\frac{B(\sin^2t)-B(0)}{32}.
\tag{4}
$$

Place patches in every time slab, at spatial base coordinates $0,4,\ldots,4(\lfloor L_i/4\rfloor-1)$ in direction $i$. The cyclic gaps between distinct bases in each coordinate are at least four. Marks from different patches in the same slab differ by at least three in a spatial coordinate, since their offsets in that coordinate are zero or one. A star with temporal distinguished axis sees one slab and spatial sites at pairwise distance at most two. A star with a spatial distinguished axis has two identity spatial plaquettes and zero determinant. Thus the marked slabs add without cross terms, including at the time seam. All plaquette traces on the marked configurations depend only on the $M$ angles $t_j$. The term $A_B$ is exactly $\sum_{j:\sigma_j=A}H(t_j)$ for the binary choices $\sigma_j$.

**One-link likelihoods.** Let $\pi$ be any probability measure on the closed disk of radius $\kappa$ in $\mathbb R^2$, and define
$f_\pi(t)=\int \exp(u\cos t+v\sin t)\,d\pi(u,v)$.
Varying just the third marked link in one patch of a $Q_2$ image gives a positive constant times $f_\pi(t)$. At fixed fine field the two coordinates are projections of $\kappa M_c$ onto $1,{\bf k}$, so their Euclidean norm is at most $\kappa$. All remaining factors and the bond normalizer are independent of $t$. A positive sum of such slices has the same representation after adjusting the constant.

Let $\mathcal P_\kappa$ consist of

$$
       q(t)=\frac{b f_\pi(t)}{b f_\pi(t)+f_\nu(t)},\qquad
       e^{-2\kappa}\leq b\leq e^{2\kappa},
$$

with independent choices of probability measures $\pi,\nu$ on that disk. This is compact in the uniform topology. Probability measures on the compact disk are weakly compact, and the integrands and their real $t$-derivatives are uniformly bounded, so weak convergence gives uniform convergence of the transforms. Denominators stay bounded below. With $h(t)=(1+e^{H(t)})^{-1}$, define

$$
 d_{\kappa,B}=\min_{q\in\mathcal P_\kappa}
      \int_0^{2\pi} D_{\rm KL}\big({\rm Bern}(h(t))\,\|\,{\rm Bern}(q(t))\big)\,
                      \frac{dt}{2\pi}.
\tag{5}
$$

The integral is continuous on this compact set and vanishes only for equality at every real $t$.

To prove the minimum is positive, suppose $h=q$. Equality of odds gives
$b f_\pi(z)=e^{-H(z)}f_\nu(z)$ on the entire complex plane by continuation. Each transform satisfies $|f_\pi(t+is)|\leq \exp(\kappa\cosh s)$, and $f_\pi(t)\geq e^{-\kappa}$ on the real axis. Its log modulus $u_\pi(t,s)$ has horizontal mean at least $-\kappa$ for every $s$. The horizontal mean of $\tfrac12\log(|f_\pi|^2+\varepsilon)$ is convex in $s$ because its second derivative is the mean of the nonnegative Laplacian. The horizontal second derivative integrates to zero by periodicity. The mean is even by conjugation. Its minimum occurs at zero. Decreasing $\varepsilon$ to zero preserves the lower bound by monotone convergence applied after subtraction from a fixed upper bound on each horizontal line. Thus the mean of $|u_\pi|$ is at most $2\kappa\cosh s+\kappa$, also in the presence of zeros.

Let $a_j$ be a nonzero Fourier coefficient of $H$ with $j\geq2$. For $n=\deg B\geq1$, the top frequency $2n$ in $B((1-\cos 2t)/2)$ has nonzero coefficient. The $j$-th coefficient of $\operatorname{Re}H(t+is)$ is $a_j\cosh(js)$, since $H$ is real on the real axis. Taking log moduli in the entire identity and using the two mean bounds gives $|a_j|\cosh(js)\leq4\kappa\cosh s+2\kappa$. The factor $b$ contributes only at frequency zero. Letting $s$ increase is a contradiction. This proves (5) is strictly positive for each fixed nonconstant polynomial, allowing both image slices to have complex zeros. If the colour coupling tends to zero with the torus size, the choice $b=1,\pi=\nu$ in (5) shows that the separation can tend to zero. Row 1544 A supplies the growth-bound method on a link circle. Taking a ratio here cancels the unconstrained trace action. [Row 1544, Theorem A](gap-mech-k2-solve-astra62.md)

**Why a wrap error must pay for each patch.** Fix all $t_j$. Assign probability to the $2^M$ label choices by normalizing the values $D_\sigma(t)$ on this finite set. Denote this law by $Q_t$. The comparison law $P_t$ has independent labels with $P_t(\sigma_j=A)=h(t_j)$. All trace terms and the site constant take a single value on this set. Flipping one label varies only the second marked link of its patch, so it changes $R$ by at most $\Gamma$. The log of the unnormalized likelihood ratio between the two laws therefore has oscillation at most $M\Gamma+2\eta$. Normalization shifts this logarithm by a constant and its range contains zero, giving $D_{\rm KL}(P_t\|Q_t)\leq M\Gamma+2\eta$.

Order the patches. For fixed earlier labels and fixed angles other than $t_j$, write the conditional odds under $Q_t$ by summing $D_\sigma(t)$ over all later labels separately for $A$ and $B_0$ at patch $j$. Each sum is a positive constant times a disk transform in $t_j$. Removing the $t_j$-dependent bond exponential leaves two positive masses whose ratio is in $[e^{-2\kappa},e^{2\kappa}]$. Term by term the only change is the second marked link, and its log kernel changes by at most $2\kappa$. All normalizers depend only on the fine field. Thus the conditional probability of $A$, as a function of $t_j$, belongs to $\mathcal P_\kappa$, with arbitrary dependence on the fixed data.

Expand the log likelihood ratio as a sum of the log conditional ratios for successive labels, and take expectation in $P_t$. The $j$-th term is the conditional Bernoulli divergence averaged over the earlier $P_t$-labels. Integrate all angles with independent uniform measures. The weights of the earlier labels under $P_t$ depend only on the earlier angles. Consequently (5) bounds the integrated $j$-th term below by $d_{\kappa,B}$. Summing proves (3). This relative entropy compares labels on test configurations for a uniform action bound. Equation (8) below uses the normalized image law on link fields.

**An explicit finite-torus exclusion.** At a common angle $t$ compare the configuration with all labels $A$ to that with all labels $B_0$. For each fine field the logarithms of their kernel weights differ by at most $M\sqrt2\,\kappa$, since only the second marked link of each patch changes and $|{\bf i}-{\bf j}|=\sqrt2$. The same bound holds after positive integration. Equations (2) and (4) then give

$$
        \Gamma+\frac{2\eta}{M}
        \ \geq\ \frac{1}{32}\max_{0\leq u\leq1}|B(u)-B(0)|-\sqrt2\,\kappa .
$$

For $B(u)=192u$, $2\leq\kappa\leq3$, $\Gamma\leq1$ and $\eta\leq1/100$, this already contradicts inclusion on each allowed torus. The right side is at least $6-3\sqrt2>3/2$, whereas the left side is at most $51/50$. For arbitrarily small nonzero polynomial coefficients, (3) gives a strictly positive separation even where this elementary right side is negative.

**Radius and wrap in the proposed step.** In the norm of row 1468 §4.2, a residual of size $\rho$ at readout $x'$, rate $r>0$ and weight $\theta$ has

$$
       \Gamma\leq A(x',r,\theta)\rho,\qquad
       A(x',r,\theta)=2\sup_{m\geq1}(1+12\theta x'm)e^{-rm}.
\tag{6}
$$

Indeed a set of $m$ bonds in four dimensions has at most $6m$ incident unoriented elementary plaquettes counted with repetitions, and each plaquette energy is at most two. Bound each supremum by its weighted summand multiplied by $(1+12\theta x'm)e^{-rm}$ and use $\operatorname{osc}R_X\leq2\sup|R_X|$. For the periodized terms of diameter below half the shortest period, a term through a fixed torus bond lifts through a chosen copy of that bond, giving the same bound.

For example, take $B(u)=u$ at one nonterminal output level, permit **every** trace-only centre term of finite weighted norm, and add a ball of radius $\rho$ in the full interaction norm. Use one connected ten-bond support per oriented star in the centre. Apply the tube test on tori where these supports survive the diameter cut, for instance whenever the shortest side exceeds twenty. Equation (3) applies directly at any of its stated sizes if the finite-torus action has form (2). At bounded band strength $\kappa\leq\kappa_*$, (3) excludes this output class whenever

$$
               A(x',r,\theta)\rho+\frac{2\eta}{M}<d_{\kappa_*,B}.
\tag{7}
$$

The disk and intercept intervals for $\kappa$ are contained in those for $\kappa_*$. Any family requiring a nonempty tube to map to such an output fails inclusion on the sixteen tori. One untwisted member already excludes every input image. In particular, for any finite choice of $a$ and bounded band of $x$, a zero-radius colour remainder and $\eta=o(V_\Lambda)$ are excluded uniformly in side for this choice of $B$. Positive radii below (7) are excluded as well. On a single specified torus (7) retains the actual inherited allowance $\eta$. In the torus-free application, a subextensive inherited error plus $V_\Lambda e^{-rs/8}$ stays subextensive as the shortest side $s$ grows at fixed aspect. A larger inherited error must be compared with (7) at its actual value.

## Suppressing full colour rank in the physical law

A second consequence allows arbitrary signed, colour-dependent tails. On an untwisted torus with $V_\Lambda$ sites let $H_\Lambda$ be normalized product Haar, and let $\nu$ have density proportional to
$\exp[-\lambda\sum_y G_y-S_0]$ with $\lambda>0$ and $\operatorname{osc}S_0\leq CV_\Lambda$. For example $S_0$ can be any summable interaction with the indicated oscillation budget, including a Wilson term fixing the desired transverse readout. Let $\mu$ be any normalized $Q_{2,\kappa}$ image on the same torus. For $0<h<1/4$, put $\alpha(h)=\frac2\pi\int_0^h\sin^2t\,dt$, the Haar probability of a geodesic link ball of radius $h$. Then

$$
 \frac{D_{\rm KL}(\mu\|\nu)}{V_\Lambda}
       \ \geq\ \lambda\,[m_\kappa-(4h)^6]-C-4\log(1/\alpha(h)).
\tag{8}
$$

Indeed on the event that every link is in that ball around the identity, the angle of every plaquette is at most $4h$ by bi-invariance and the triangle inequality. The Gram determinant is at most the product of the three squared column norms, hence at most $(4h)^6$. This event has Haar probability $\alpha(h)^{4V_\Lambda}$. Restrict the normalizing integral of $\nu$ to the event and bound $S_0$ there by its supremum. In the relative-entropy identity use $D_{\rm KL}(\mu\|H_\Lambda)\geq0$, (1) and $\mathbb E_\mu S_0\geq\inf S_0$. These bounds give (8).

If the image realizes the proposed action up to a site constant and an error of absolute value at most $\eta$, then $D_{\rm KL}(\mu\|\nu)\leq 2\eta$. With $h=(m_\kappa/2)^{1/6}/4$, (8) therefore rules out every output with

$$
                \lambda>\frac{2}{m_\kappa}
                   \big[C+4\log(1/\alpha(h))+2\eta/V_\Lambda\big].
\tag{9}
$$

This finite-volume test needs no smallness or trace restriction on individual terms of $S_0$ beyond their total oscillation budget. A large positive coefficient favours plaquettes whose electric colours span fewer dimensions. It can be varied without changing the quadratic readout, since $G_y$ vanishes to sixth order at the flat field. The proof bounds its admissible size using a property of the normalized coarse ensemble.

**A bound that survives arbitrarily strong ties.** On an untwisted torus assume that changing one fine link changes the incoming log density by at most $K_{\rm in}$, uniformly in the other links. The order-one bare Wilson action has $K_{\rm in}\leq12\beta$, from its six staples. Let $\epsilon=1/64$, $u_f=\epsilon/100$ and

$$
 m_{\rm in}=\tfrac14
       [e^{-K_{\rm in}}\alpha(u_f)]^{336}\,\alpha(\epsilon/2)^{10}>0.
\tag{10}
$$

For these inputs $\mathbb E G_y\geq m_{\rm in}$ for every $\kappa>0$. Equations (8) and (9) may thus use $\max(m_\kappa,m_{\rm in})$. A bounded local energy in the fine law gives positive probability of full rank already for the normalized contour means, before applying soft noise.

To see this, prescribe the ten coarse bonds of three incident temporal plaquettes as in configuration $A$ at $t=\pi/2$. Their three imaginary parts form an orthonormal basis. The star meets eight coarse vertices. In their eight fine $2^4$-cells prescribe every interior link to be the identity. For each of the ten coarse bonds, prescribe the eight fine links crossing its face to equal that coarse bond. These prescriptions are compatible. They use at most $8(4\cdot2^3)+10\cdot2^3=336$ fine bonds. Every contour of row 1468 has both legs inside the respective cells and its straight two-link segment uses exactly one crossing. At the prescription, all 384 holonomies for each coarse bond equal its prescribed value.

Conditional on the other fine links, the density on the prescribed set relative to its product Haar law is bounded below by $e^{-336K_{\rm in}}$ after normalization, by changing the links successively. With probability at least $[e^{-K_{\rm in}}\alpha(u_f)]^{336}$ every prescribed bond lies in its radius-$u_f$ ball. Each contour of length at most ten then has chordal error at most $10u_f$, as does its mean. Normalizing that mean gives chordal error at most $20u_f$. The geodesic error is at most $10\pi u_f<\epsilon/2$. The exponential bond kernel assigns a ball of radius $\epsilon/2$ about this mean direction probability at least $\alpha(\epsilon/2)$, since its density decreases with angle. Independence supplies the tenth power in (10). On that event all ten output links are within $\epsilon$ of their prescriptions. Each electric column differs from its prescribed column by at most $4\epsilon$. Telescoping the determinant, using column norms at most one, bounds its change by $12\epsilon<1/2$. Hence $J_y\geq1/4$. For other signed orientations, reflect or permute the prescribed coarse star and store the inverse of a negatively oriented bond on its positive representative. The eight-cell construction then gives the same estimate. Averaging gives (10). In (10) a cutoff-uniform conclusion needs a cutoff-uniform incoming oscillation bound. The bare bound $12\beta_K$ grows on the calibrated trajectory.

## Separation from purity and the open step

For compact $U(1)$ take the same $16\cdot4!$ contours and the normalized cosine tie. For five-dimensional $SU(2)$ take the $32\cdot5!$ analogous contours and the normalized quaternion tie. In both models the full spatial Gram determinant vanishes. Thus $A_B=0$ for every configuration. In (4) the colour cost is identically zero, the reference probability is $1/2$, and (5) admits $b=1,\pi=\nu$ with zero divergence. Equation (8) also loses its strictly positive coefficient from the physical law. Selecting three of the four spatial directions in five dimensions would test a different rank condition. These facts identify exactly where the exclusion uses four-dimensional $SU(2)$. They give no closure theorem in either comparison model.

There are explicit functions outside the polynomial conclusion. For $0<c\leq\kappa$, the two disk atoms $(0,c),(0,-c)$ with weights $1/2$ give $f(t)=\cosh(c\sin t)$. The atom at the origin gives $g(t)=1$. Thus on this slice $\log(f/g)=\log\cosh(c\sqrt{\sin^2t})$, a nonpolynomial analytic function of the squared volume with a nonzero linear term. The one-link test accepts this profile. Realizing it simultaneously on all fields and controlling its readout require additional estimates.

For the release witnesses $b,g_0$, put $n=\ell b^K$, $u=n/512$ and $Z_+(v)=\tfrac18\sum_z Z^z(v)$. The seed requires $P_K=Z_+(2u)/Z_+(u)^2\geq457/625$ at infinitely many $K$ for one $\ell\in1024\mathbb N$ and one calibration level. The obstruction uses normalized slice ratios. Multiplying an incoming torus density by a positive constant leaves the normalized law in (1) and the label odds in (5) unchanged. Within the Wilson family itself, hold a seed geometry and soft strength fixed. As $\beta\downarrow0$, each of the sixteen Haar integrals tends to one, so $P\to1$. At the same fixed geometry $P\to0$ as $\beta\to\infty$ by check 1527(iii). Fixing the strength gives the same $d_{\kappa,B}$ at both ends. On a sequence of growing seed boxes one may choose positive couplings in the two regimes separately on each box. Those choices do not follow the calibrated trajectory. This separates the class test from a purity criterion. [Check 1527(iii)](gap-agy-seed-approaches-neon-check-astra62.md) · [Fixed-box estimate](gap-solve-astra62.md)

**What remains open.** With the release witnesses fixed, the positive route still needs an orbit-independent family of rules with summable, colour-dependent interactions, or another class outside the exclusion. At each band level it must satisfy

$$
 Q_{2,a x_k}\mathcal T_k\subseteq\mathcal T_{k+1},\qquad
 x_{k+1}\leq x_k-\delta_0,\qquad
 \rho_{k+1}\leq\bar\rho(x_{k+1}),\qquad
 \eta_{k+1}\leq\eta_k+|\Lambda|e^{-rs/8}
$$

on all sixteen tori, with fixed $a,r,\delta_0>0$, $x_0\in[H,W_*]$, the (C5) radius margin, and stopping when $\|\Phi_N^*\|+\rho_N\leq\varepsilon_E$. Equation (1) measures full electric rank in the coarse law. The readout uses the transverse Hessian at the flat field, where the rank term has zero Hessian. I have no estimate transferring (1) into a decrement or bounding the radius of a viable centre. No sufficient condition for the seed is claimed. The proofs are written by hand. Independent checking and Lean formalization have not been performed. [Exact step and stopping rule, §4.3](gap-k2-tool-design-fable.md)

RESULT A nonconstant polynomial in the full electric Gram determinant, added to arbitrary interactions among elementary plaquette traces, cannot close the four-dimensional SU(2) soft block with a radius and wrap error below (7). Both comparison models have identically zero determinant. The general (K2-STEP), (PUR-io) and the mass gap remain open.
