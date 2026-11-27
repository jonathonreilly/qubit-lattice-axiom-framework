# Repo search

Row 1617, research at `4f702949c`. The target-specific prior file is absent. The lead’s 8 November digest searched main and PRs 10114, 10133, 10134 and 10141. I fetched the closest soft-route hit, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on PR 10114. Its lines 106–170 bound a one-step plaquette correlation using the positive one-link convolution. Its time separation is one lattice spacing. In the lane, row 708 treats the opposite differential inequality. Row 1610 §3 and check 1613 supply the downward consumer and its fixed-box regularity. The registry entries R11 and TWO-PER ask for upper and two-period estimates, respectively. [Lead’s digest](prior/repo-search-2026-11-08.md) · [Direction](gap-direction7-fable.md) · [Check](gap-direction7-fable-check-astra62.md)

I also searched the mass-gap, YM4D snapshot and soft-route source directories on those five refs for downward transport, high-energy level slopes and electric-spin score estimates. No match supplied this bound. On main at 8b11ae2bb9, the mass-gap copies of rows 708 §4.2 and 710 Theorem U have the upper transport and the raw electric derivative. Main’s periodic finite-clock Villain note, §§3–5, supplies the current expansion used by the compact-circle comparison below. [Main upper transport](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb9/research/mass-gap/library/gap-mid-max.md#L118-L140) · [Soft-route plaquette witness](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649c/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L170) · [Periodic Villain input](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb9/docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md#L160-L295)

**ON FILE (sources and scope).** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the positive one-bond multipliers and their series in outline lines 2197–2243 (GL3–4), and the positive layer transfer and periodic trace in lines 2315–2335 (GL8). Outline lines 588–599 distinguish clustering from the spectral support needed for a gap. CA-I lines 2706–2710 exclude a gap from Theorem 0. I used the chunk and obligations indexes before reading the cited outline lines at 31a47c543775. The CA-I 4.12–4.19 index concerns the multiscale construction. I downloaded each source once. [Outline index](sa-index/README.md) · [GL3–4](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2197-L2243) · [GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [CA-I scope](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2706-L2710)

**ON FILE (closest mathematical precedents).** Row 710, Lemmas J, C and Theorem U, supplies the electric labels and the first-order score of a transfer eigenvector. Its energy estimate is one-sided and its stated rate concerns bare coupling below 4. Row 1180, R4, compares ordered levels to the electric operator. Row 860, HS and DS, bounds high-spin events in a thermal slice. Row 1522 §4.2 and check 1523 bound an upper-response tail given coldness at half the period. Row 998, L4 and §6b, distinguishes a flow across the band from first-passage data. Check 1521(viii) proves differentiation of the projected trace at real periods. The warning about all-level *lower* transport in row 1610 §3.3 uses a momentum model. I found no Wilson high-energy slope asymptotic or relative long-period error for the downward vacuum subtraction in these results. [Row 710](gap-vir-sc.md) · [Row 1180](gap-mini-neutral-fable.md) · [Row 860](gap-hs-max.md) · [Upper-response calculation](gap-r11-thermal-solve-fable.md) · [Check 1521](gap-twoperiod-solve-fable-check-astra62.md)

**ON FILE (consumer, rows 1468, 1610 and check 1613).** Fix the release witnesses, $n=\ell b^K$, $1024\mid\ell$, and $u=n/512$. For the neutral transfer set $r_i=\lambda_i/\lambda_0$, $m_i=-\log r_i$, $G(t)=\sum_{i>0}r_i^t$, $X(t)=\log(1+G(t))$ and $\bar E_t=-\partial_t X(t)$. Coupling derivatives in this note are partial derivatives at fixed $n,t$. The requested inequality is $\partial_\beta X(t)/t\ge\kappa\bar E_t$ along a characteristic ending with $G(t_h;\beta_h)\le4/21$. [Seed and its consumer](gap-k2-tool-design-fable.md)

**PROVED below.** Equation (6) bounds the large-spin error relative to each excited energy. Equation (10) replaces the vacuum subtraction by a finite-period observable with a controlled error in the same thermal units. Equation (14) bounds how much transport the discarded spins can supply across a moving interval. Equation (9) rules out every positive common level dilation. The signed estimate for the remaining observable (12) on the calibrated band is open.

## The electric energy seen by a transfer eigenstate

**ON FILE (rows 667, 710 and check 1613).** Fix a finite spatial torus of side $n\ge4$, with $d=3n^3$ links. Work on the gauge-invariant, centre-neutral Hilbert space. In the shifted Wilson convention, $T=MCM$ with $M=e^{-\beta V/2}$, where $0\le V\le V_*=6n^3$ is the spatial action. The product convolution $C$ acts on link-spin labels $k_e=2j_e$ by the scalar $c_{\mathbf k}=\prod_e [2e^{-\beta}I_{k_e+1}(\beta)/\beta]$. The label projections commute with the gauge and centre averages. The positive compact transfer is injective on this space by injectivity of $C$ and invertibility of $M$. The space is infinite-dimensional since the characters of all spins of one contractible plaquette are linearly independent neutral functions. Thus the positive eigenvalues, with multiplicities, tend to zero.

**PROVED (two tails, at every $\beta>0$).** Take $T\psi=\lambda\psi$, $\|\psi\|=1$, $L=-\log\lambda$, and measure the label in the unit vector $w=C^{1/2}M\psi/\sqrt\lambda$. Write $Y=-\log c_{\mathbf k}$ for its electric energy. For every $x\ge0$,
$$
 \Pr_w(Y>L+x)\le e^{-x},\qquad
 \Pr_w(Y<L-\beta V_*-x)\le e^{-x}.                                      \tag{1}
$$
Indeed $\mathbb E_w e^Y=\|M\psi\|^2/\lambda\le e^L$. Also $w$ is an eigenvector of $C^{1/2}M^2C^{1/2}$ at $\lambda$. The form inequality $C^{1/2}M^2C^{1/2}\ge e^{-\beta V_*}C$ gives $\mathbb E_w e^{-Y}\le e^{\beta V_*-L}$. Apply Markov's inequality to the two random variables. Both estimates apply to every vector in a degenerate eigenspace. The constants in (1) are for this box.

## The coupling slope at high neutral energy

**PROVED.** Write $m=\log(\lambda_0/\lambda)$, $D_\psi=\langle\psi,T'\psi\rangle/\lambda$, and $b_\psi=D_\psi-D_\Omega$, where $\Omega$ is the normalized vacuum. Thus $b_\psi=-m'$ on a differentiable eigenbranch. On each fixed box, uniformly for $\beta$ in each compact $I\subset(0,\infty)$ and for unit vectors in the indicated eigenspaces,
$$
 \lim_{m\to\infty}\frac{\beta b_\psi\log m}{m}=1.                         \tag{2}
$$
In particular the high levels make a strictly positive contribution to the fixed-time coupling derivative. Their response divided by their energy tends to zero.

To prove (2), set $N=\sum_e k_e$. On $I$ the series in GL3 bounds each one-link multiplier between
$$
 e^{-\beta}\frac{(\beta/2)^k}{(k+1)!}
 \quad\hbox{and}\quad
 e^{-\beta}\frac{(\beta/2)^k}{(k+1)!}\exp(\beta^2/4).
$$
The lower bound takes the first term. For the upper bound use $(k+1+h)!\ge(k+1)!$ in the remaining sum over $h$. The elementary integral bounds for $\sum_{j=1}^{k+1}\log j$ give $\log((k+1)!)=k\log(1+k)+O(k+1)$. Convexity of $x\log(1+x)$ gives
$$
 N\log(1+N/d)\le\sum_e k_e\log(1+k_e)\le N\log(1+N).
$$
Therefore $Y=N\log(1+N)+O_{I,d}(N+1)$, uniformly in all labels. In particular $N\le C_{I,d}(1+Y)$, since $Y\ge0$ by the convolution norm bound $\|C\|\le1$. Uniformly as $Y\to\infty$, $N/(Y/\log Y)\to1$. This follows by taking logarithms in $Y/(N\log N)\to1$.

It remains to average this inversion in the *interacting* eigenstate. Fix $0<\delta<1/2$. By (1), the probability of $Y\notin[(1-\delta)L,(1+\delta)L]$ is at most $(1+e^{(\sup I)V_*})e^{-\delta L}$ for large $L$. The lower tail contributes $O_{I,d}((1+L)e^{(\sup I)V_*-\delta L})$ to $\mathbb E_w N$. On the upper tail, integrate the first bound of (1) above $(1+\delta)L$ and use $N\le C_{I,d}(1+Y)$. Its contribution is at most $C_{I,d}(2+(1+\delta)L)e^{-\delta L}$. On the middle event $Y/\log Y$, divided by $L/\log L$, lies between $1-\delta-o(1)$ and $1+\delta+o(1)$. Let $L\to\infty$, then $\delta\downarrow0$. This gives $\mathbb E_w N\sim L/\log L$ uniformly.

Differentiate $MCM$ in the fixed eigenvector. Each half-weight contributes $-\lambda\langle V\rangle_\psi/2$. The term differentiating $C$ is diagonal before the outer half-weights. Differentiating the positive Bessel series gives $\beta I_p'=pI_p+\beta I_{p+1}$ and $0<I_{p+1}/I_p\le\beta/[2(p+1)]$. Hence
$$
 \beta D_\psi
 =\mathbb E_w N+
   \beta\,\mathbb E_w\sum_e\left(\frac{I_{k_e+2}}{I_{k_e+1}}-1\right)
   -\beta\langle V\rangle_\psi .
$$
Absolute convergence follows from factorial decay after insertion of $N+d$, locally uniformly in $\beta$. This is the computation of row 710, Theorem U(ii). Its error from $\mathbb E_w N$ is bounded on every $I$, including above 4, by $(\sup I)[d(1+\sup I/4)+V_*]$. The positive simple $\lambda_0$ and its log derivative are continuous on $I$ by check 1613. Thus $m=L+\log\lambda_0=L+O_{I,n}(1)$, and $D_\Omega=O_{I,n}(1)$. These estimates prove (2).

**PROVED (contribution to the real-time thermal test).** Fix $\beta>0$, this box and $\kappa>0$. There is a finite $\Lambda$ such that for *every* $m_i\ge\Lambda$, $0<b_i\le\kappa m_i/2$. Define $B_{\ge\Lambda}(t)=\sum_{m_i\ge\Lambda}m_i e^{-tm_i}$. For every real $t>1$,
$$
 -\kappa B_{\ge\Lambda}(t)
 <\sum_{m_i\ge\Lambda}(b_i-\kappa m_i)e^{-tm_i}
 \le-\tfrac12\kappa B_{\ge\Lambda}(t)<0 .                                \tag{3}
$$
Use (2) and sum with the actual positive thermal weights. The sums converge since the transfer is trace class and $m e^{-(t-1)m}$ is bounded. The tail contains infinitely many levels. At a crossing one can use any orthonormal basis of the eigenspace in this trace. Multiplication by $t$ gives precisely the contribution to $G_\beta+\kappa tG_t$, by check 1521(viii) for $t>2$ and check 1613 for the other times. Thus a positive-speed thermal witness must have a *strict surplus* from its lower levels at every positive-speed point. Equation (3) neither fixes the total sign nor bounds the fraction of thermal energy in the tail uniformly in $n$.

## A lower bound for the thermal response on a cold Wilson box

The large-*level* cutoff in (3) depends on the box. A different cutoff, on the electric spin of each link, admits a bound uniform in the box with an explicit threshold. The eigenvectors and the action in the following estimates are the original interacting Wilson ones.

**PROVED (joint electric labels in an eigenstate).** Set $\rho_k=c_k/c_0=I_{k+1}(\beta)/I_1(\beta)$, where $c_k$ now denotes the one-link multiplier with integer label $k=2j$. For any set $S$ of spatial links and prescribed labels $k_e$,
$$
 \Pr_{w_i}(k_e\text{ prescribed for all }e\in S)
 \le e^{m_i}\prod_{e\in S}\big(e^{8\beta}\rho_{k_e}\big).                 \tag{4}
$$
There is only one factor $e^{m_i}$, even for adjacent links.

Work temporarily on the full product of link spaces. The unprojected $MCM$ has a strictly positive kernel. Its unique positive top vector is invariant under the vertex gauge group and all centre translations, by their commutation with the transfer. Thus its full norm is the same $\lambda_0$ as in the neutral sector. Put $L_{\rm el}=C^{1/2}e^{-\beta V}C^{1/2}$, the transfer with the temporal convolution split symmetrically. It has the same full norm by the equality of the norms of $B^*B$ and $BB^*$, $B=C^{1/2}M$.

Delete from $V$ all spatial plaquettes touching $S$, to obtain $V_{\rm out}$. At most four plaquettes per link are deleted and each costs at most two. Therefore
$$
 L_{\rm el}\le L_{\rm el}^S:=C^{1/2}e^{-\beta V_{\rm out}}C^{1/2}
       \le e^{8\beta|S|}L_{\rm el} .
$$
The comparison concerns multiplication operators inside a common sandwich. In particular it requires no monotonicity of a vacuum-subtracted trace. Since $V_{\rm out}$ is independent of all the selected links, $L_{\rm el}^S=(\bigotimes_{e\in S}C_e)\otimes L_{\rm out}$. Each $C_e$ has norm $c_0$, by the constant eigenfunction and the integral kernel norm bound. If $P$ projects onto the prescribed spins on $S$, then
$$
 \|P L_{\rm el}^S P\|=\|L_{\rm el}^S\|\prod_{e\in S}\rho_{k_e}.
$$
Finally $L_{\rm el}\ge\lambda_i|w_i\rangle\langle w_i|$ holds on the full space. Compress it by $P$ and use the preceding upper bounds. This gives (4). Taking the full norm was essential to factoring the operator after deletion. Neutrality was used to identify the full vacuum with the one in the denominator.

**PROVED (cost of cutting the electric score).** Define
$$
 g_\beta(k)=\frac{k}{\beta}+\frac{I_{k+2}}{I_{k+1}}-1,\qquad
 d_i^{J}=\mathbb E_{w_i}\sum_e g_\beta(k_e){\bf1}_{k_e\le J}
               -\langle\psi_i,V\psi_i\rangle,\qquad
 b_i^J=d_i^J-d_0^J .
$$
Thus $D_{\psi_i}$ is the same score with $J=\infty$. Fix any $0<c<1$, $a=\log(1/c)$, and $t>1$ with $0<G(t)\le c$. Choose any $0<\delta\le1$. An explicit sufficient integer cutoff is
$$
 J=\left\lceil\max\left\{e^2\beta,\,
             \frac{8\beta+\log(dt/(a\delta))}{\log 2},\,0\right\}\right\rceil .
                                                                            \tag{5}
$$
Then every excited neutral level at this coupling satisfies
$$
 -\frac{\delta}{\beta}m_i\ \le\ b_i-b_i^J
 \le\frac{1+\delta}{\beta}m_i .                                             \tag{6}
$$
The asymmetric error matters for downward transport. The lower error can be made arbitrarily small at logarithmic cost in $1/\delta$.

For the proof set $U_J=\sum_e k_e{\bf1}_{k_e>J}$ and $A=e^{8\beta}\sum_{k>J}(e^k-1)\rho_k$. Expand $e^{U_J}$ as a product of $1+(e^{k_e}-1){\bf1}_{k_e>J}$. Each nonempty subset in its expansion has nonnegative integrand. Sum (4) over its labels to obtain
$$
 \mathbb E_{w_i}e^{U_J}
 \le 1+e^{m_i}\big((1+A)^d-1\big)\le e^{m_i}(1+A)^d.
$$
Hence $\mathbb E_{w_i}U_J\le m_i+dA$ by Jensen. This bound also holds in the vacuum with $m_0=0$. The GL3 series, compared term by term to the series of $I_1$, gives $\rho_k\le(\beta/2)^k/(k+1)!$, since $(k+1+h)!/(1+h)!\ge(k+1)!$. For $k>J$, $k!\ge(k/e)^k$ gives $e^k\rho_k\le 2^{-k}$ by (5). Consequently $dA\le d e^{8\beta}2^{-J}\le a\delta/t$.

For those same labels $0\le g_\beta(k)\le k/\beta$. Indeed $k\ge\beta$ and $0<I_{k+2}/I_{k+1}\le\beta/[2(k+2)]\le1$. Thus the omitted raw score lies between zero and $(m_i+dA)/\beta$ in state $i$, and between zero and $dA/\beta$ in the vacuum. Subtraction gives the lower bound $-dA/\beta$ and the upper bound $(m_i+dA)/\beta$. Since $e^{-t m_i}\le G(t)\le c$, every $m_i\ge a/t$. This proves (6) without a bound at any shorter time and without dividing an absolute error by an unknown small occupation.

**PROVED (real-time consequence).** Write $\bar E_t=\sum_{i>0}m_i e^{-tm_i}/(1+G(t))$ and $X(t)=\log(1+G(t))$. Under (5),
$$
 \frac{\partial_\beta X(t)}{t}
 \ \ge\ \frac{\sum_{i>0}b_i^J e^{-tm_i}}{1+G(t)}
                 -\frac{\delta}{\beta}\bar E_t .                            \tag{7}
$$
The reverse upper estimate has $+(1+\delta)\bar E_t/\beta$. These follow by multiplying (6) by the nonnegative occupation weights and using the trace derivative of check 1613. They hold at every positive coupling, including at late bare couplings in the proposed band whenever the time is cold. For fixed $c,\delta$, $J=O(\beta+\log(dt)+1)$. Where $\beta=O(\log n)$ and $t$ is at most a fixed power of $n$, $J=O(\log n)$. No growth condition on the hot time or the upper coupling is needed for (5)–(7). The operators in (7) still use the full eigenstates, including their spatial magnetic response. A hard cutoff on the transfer matrix itself would change the law.

### Independent checks of the two estimates that affect the consumer

**PROVED (a Wilson integral check of the lower error in (7)).** This proof at late bare couplings $\beta\ge1$ uses one temporal plaquette and requires no simultaneous spin estimate. At any integer period $s\ge3$, the thermal probability of the single-link spin $k$ in the electric placement is $\operatorname{Tr}(P_{e,k}L_{\rm el}^s)/Z_+(s)$, with trace restricted to the neutral space. In the Wilson integral this is the expectation, in the positive neutral twist mixture, of
$$
 \frac{(k+1)c_k\,\chi_{k/2}(U_p^z)}
      {\exp[-\beta(1-\tfrac12\operatorname{tr}U_p^z)]},                   \tag{8}
$$
where $U_p^z$ includes the seam sign. Indeed projection in the electric placement replaces one temporal convolution $C_e$ by $C_eP_{e,k}$, whose Haar kernel is $(k+1)c_k\chi_{k/2}$. Moving the half-weights cyclically through the trace and integrating the temporal gauge links gives (8), including the same centre average in numerator and denominator. This insertion is the one-link version of row 860, Lemma OS. Its integral is nonnegative by the original spectral trace, even though the character has both signs.

The integrand has absolute value at most $e^{2\beta}(k+1)^2 c_k\le e^{2\beta}(k+1)^2\rho_k$. Pass to the vacuum in the probability of each fixed $k$ by taking integer $s\to\infty$ on the fixed box. Indeed $\sum_{i>0}r_i^s\to0$ by dominated convergence and $P_{e,k}$ is bounded. For $k>J$, $k(k+1)^2\le11e^k$, by the exponential series applied to $k^3+2k^2+k$. Using $11e^{2\beta}\le e^{8\beta}$ for $\beta\ge1$ and the sum estimate in (5), the omitted *vacuum* score over all links is at most $d e^{8\beta}2^{-J}/\beta\le a\delta/(\beta t)$. The omitted raw score in any excited state is nonnegative. Subtracting the vacuum and weighting the excited states proves the lower side of (6) and (7) by a field-integral argument, also when the requested $t$ is real. Only the auxiliary period $s$ was integral.

**PROVED (separate kernel check of the upper error at $\beta\ge1$).** In the *one-link* convolution multiply the spin-$k$ eigenvalue by $e^k$ for $k>J$ and by one otherwise. This gives a bounded convolution with real kernel $\widetilde c$. Row 875 cautions that a spin boost can lose pointwise positivity. Only an absolute upper bound is needed here. The character expansion and $|\chi_{k/2}|\le k+1$ give
$$
 |\widetilde c(g)|\le(1+A')c_\beta(g),\qquad
 A'=e^{2\beta}\sum_{k>J}(e^k-1)(k+1)^2c_k ,
$$
using $c_\beta(g)=\exp[-\beta(1-\tfrac12\operatorname{tr}g)]\ge e^{-2\beta}$. For $k>J\ge e^2\beta$,
$$
 (k+1)^2 e^k c_k
 \le (k+1)\left(\frac{e^2\beta}{k}\right)^k 2^{-k}
 \le 2e^2\beta\,2^{-k}.
$$
The first inequality uses $c_k\le\rho_k\le(\beta/2)^k/(k+1)!$ and $k!\ge(k/e)^k$. For the second, the power is at most its base and $(k+1)/k\le2$. Since $2e^2\beta\le e^{6\beta}$ for $\beta\ge1$, $A'\le e^{8\beta}2^{-J}$. These bounds justify absolute convergence of the modified kernel.

Take the product $\widetilde C$ of these one-link convolutions. In the eigenstate of (1),
$$
 \mathbb E_{w_i}e^{U_J}
  =\langle\psi_i,M\widetilde C M\psi_i\rangle/\lambda_i
  \le (1+A')^d\,\langle|\psi_i|,T|\psi_i|\rangle/\lambda_i
  \le (1+A')^d e^{m_i}.
$$
The middle inequality follows by taking absolute values in the full Haar kernel integral, before any gauge projection. The norm in the last bound is the full Wilson norm identified above. Jensen now yields $\mathbb E_{w_i}U_J\le m_i+dA'$ for every eigenstate, including the vacuum. As $dA'\le a\delta/t$, this checks both sides of (6) and hence (7) and (14) at the **same cutoff** by a second route. It uses pointwise comparison of temporal kernels in place of deleting spatial plaquettes. [Earlier spin-boost test, row 875](gap-exc-astra.md)

**PROVED (a direct check on endpoint level transport).** For every finite $n\ge4$ and every $0<\beta_1<\beta_2<\infty$, the ordered neutral energies satisfy
$$
                 \lim_{i\to\infty}\frac{m_i(\beta_1)}{m_i(\beta_2)}=1.     \tag{9}
$$
No eigenbranch continuation is needed. From the factorial bounds used in (2), the electric energies at the two couplings differ by $O_{n,\beta_1,\beta_2}(1+N)$. Since $Y/(N\log N)\to1$ for both, for any $0<\xi<1$ there is $C_\xi<\infty$ such that
$$
 e^{-C_\xi} C(\beta_2)^{1+\xi}
        \le C(\beta_1)\le e^{C_\xi} C(\beta_2)^{1-\xi}
$$
on all labels. Apply the ordered eigenvalue min–max principle on the fixed neutral space. At each endpoint $e^{-\beta V_*}C\le L_{\rm el}\le C$, and $L_{\rm el},T$ have the same positive spectrum there. Thus the ordered electric negative log eigenvalues differ from the $m_i$'s at that endpoint by bounded additive errors (including $\log\lambda_0$). The ordered negative logs tend to infinity. The lower and upper limiting ratios in (9) are consequently bounded by $1-\xi$ from below and $1+\xi$ from above. Let $\xi\downarrow0$.

In particular, for **every** admissible $\ell,g_0$, every cutoff with $n\ge4$, every finite $\beta_h>\beta_K>0$, and every $E>1$, arbitrarily high neutral levels violate $m_i(\beta_K)\ge E m_i(\beta_h)$. This refutes the positive-factor *level* supplier on the actual Wilson trajectory. The argument says nothing against the zero-speed case or the thermal supplier, where low levels can pay the negative tail in (3).

## Finite-period form and the missing sign

**PROVED.** Define $\bar d^J(s)=\sum_{i\ge0}d_i^J r_i^s/(1+G(s))$, $r_0=1$. This is a bounded observable in the two placements of the thermal transfer. For an integer $s\ge3$ it is the following ordinary neutral Wilson expectation. At one time slab, sum (8) over $0\le k\le J$ with coefficients $g_\beta(k)$ for each of its $d$ temporal plaquettes. Subtract the spatial action $V$ of one layer. For real $s>1$ the definition is by the two positive density matrices $L_{\rm el}^s/Z_+(s)$ and $T^s/Z_+(s)$, with $Z_+(s)=\operatorname{Tr}T^s$. This convention does not interpret a noninteger period as a Wilson path integral.

With $c,a,J,\delta$ as in (5), choose $\eta>0$ and put
$$
 B_J=V_*+d(1+J/\beta+\beta/4),\qquad
 v=\max\left\{3,\left\lceil t\left(1+
       \frac{\log^+((1+c)tB_J/(a\eta))}{a}\right)\right\rceil\right\},
 \qquad \log^+x=\max(0,\log x).
$$
For the same $J$ at the two periods, let $H_J(t,v)=\bar d^J(t)-\bar d^J(v)$. The two bounds for the exact consumer are
$$
 H_J(t,v)-(\eta+\delta/\beta)\bar E_t
 \ \le\ \frac{\partial_\beta X(t)}{t}
 \le H_J(t,v)+\big(\eta+(1+\delta)/\beta\big)\bar E_t .                   \tag{10}
$$
In particular at integer $t\ge3$ the middle expression is $a_0-A_t/t$. Both field means in $H_J$ are at finite periods.

Indeed $d_i^J$ lies in $[-V_*-d,\ d(J/\beta+\beta/4)]$ by the Bessel ratio bound, so $|d_i^J-d_0^J|\le B_J$. Since $r_i^t\le c$,
$$
 |\bar d^J(v)-d_0^J|\le B_J G(v)
 \le B_J G(t)e^{-a(v/t-1)},\qquad
 \bar E_t\ge\frac{aG(t)}{t(1+G(t))}.
$$
The choice of $v$ bounds the first quantity by $\eta\bar E_t$, even if $G(t)$ is exceptionally small. Now the sum in (7) is exactly $\bar d^J(t)-d_0^J$. Substitute the finite-period estimate into both sides of (7). This proves (10). For fixed tolerances on a part of the trajectory with $\beta=O(\log n)$, $\beta\ge1$ and polynomial $t$, the extra temporal extent is $O(t\log n)$. Neither the cutoff $J$ nor $v$ is differentiated.

**PROVED (conditional use with HOT).** Fix the release witnesses and a proposed row 1610 characteristic $t(\beta)=u\exp(\int_{\beta_K}^{\beta}\kappa)$ with continuous $\kappa\ge0$. For definiteness use $c=1/2>4/21$ in (5) and (10). It would suffice to prove, wherever $G(t(\beta);\beta)\le1/2$,
$$
 H_J(t,v)\ \ge\ (\kappa(\beta)+\eta+\delta/\beta)\,\bar E_t .             \tag{11}
$$
The parameters $\eta,\delta$ may be chosen positive at each point before taking $J,v$. Equation (10) gives $\partial_\beta X(t)\ge\kappa t\bar E_t$ there. Since $X_t=-\bar E_t$, $X$ is nondecreasing along the characteristic on that portion. HOT puts the right endpoint strictly inside $G<1/2$. If the curve ever reached $1/2$, take the last such point before HOT and integrate from it to the endpoint. This contradicts $G_{\rm hot}\le4/21$. Thus the whole curve is in the cold portion and Theorem TR-down applies. This argument uses a collar above $4/21$ so it also works when HOT is an equality.

**ARGUED (where the estimate stops).** The deletion bound (4) is one-sided in the raw electric probabilities at *each* period. In $H_J$ the two probabilities are subtracted. Using (4) twice gives an upper bound on each, with zero as the available lower bound. It cannot pay a positive multiple of $\bar E_t$. The spatial term is $\langle V\rangle_v-\langle V\rangle_t$, whose sign the same deletion also leaves undetermined. Formula (8) exposes the same issue in the field variables. Character insertions need not be positive pointwise, and separate absolute estimates discard the signed difference between the two period laws. I have no signed lower estimate for (11) in the four-dimensional Wilson measure on the band. In particular (10) is a bound on the error of a specific part of the response. Merely replacing the remaining response by (11) gives no progress on the seed.

**PROVED (the finite signed quantity in terms of probabilities).** In (6)–(11) one may also keep the electric score constant above the cutoff, using $g_\beta(\min(k,J))$ instead of $g_\beta(k){\bf1}_{k\le J}$. In this variant $H_J$ has the form
$$
 H_J(t,v)= \sum_{e=1}^{d}\sum_{q=1}^{J}
       h_q\,[p_{e,t}(q)-p_{e,v}(q)]
           +\langle V\rangle_v-\langle V\rangle_t,                         \tag{12}
$$
where the sum is over the $d$ links and $1\le q\le J$. Here $p_{e,s}(q)$ is the thermal probability that $k_e\ge q$ in electric placement and $\langle V\rangle_s$ is the spatial action mean in magnetic placement. The coefficients $h_q=g_\beta(q)-g_\beta(q-1)=\partial_\beta\log(I_{q+1}/I_q)$ are strictly positive. For the last assertion use the moment identity of row 843, Lemma 3.1. With density proportional to $e^{\beta x}(1-x^2)^{q-1/2}$ on $(-1,1)$, $I_{q+1}/I_q=\mathbb E x>0$, and its derivative is $\operatorname{Var}(x)>0$. The identity follows by expanding the integral for $I_q/\beta^q$ in its power series and differentiating its log, using $\beta I_q'=q I_q+\beta I_{q+1}$. The constant score $g_\beta(0)$ cancels in the difference of the two laws. Summing the positive increments gives (12). For $k>J$ the omitted score now lies in $[0,k/\beta]$ because $g_\beta$ is increasing and $g_\beta(J)\ge0$. The same proof and the field check of the lower error apply. For integer $s\ge3$ one obtains each $p_{e,s}(q)$ by subtracting the sum of (8) over $0\le k<q$ from one. Thus (12) tests actual one-link marginal probabilities and spatial plaquette means of two torus laws. I cannot order those marginals between periods with a surplus that pays for (11). [Bessel moment identity](gap-q8test-opus.md)

## What the comparison theories decide

**ON FILE (free photon, rows 929, 988 and check 1613).** In the free-photon test with coupling-independent normalized spectrum, $G_\beta=0$, whereas $-tG_t>0$. Thus a positive speed fails VIR-down at the point where it is used. Zero speed on the whole interval leaves $t_h=u$. The neutral transverse mode has $m=2\operatorname{arsinh}(\sin(\pi/n))\le2\pi/n$, so $G(u)\ge e^{-2\pi/512}>1/2>4/21$ and HOT fails. The strictly positive asymptotic in (2) also fails for this photon. In (1) the free noncompact Gaussian magnetic potential is unbounded, so the comparison $M^2\ge e^{-\beta V_*}I$ has no finite $V_*$. Its Fourier multiplier also lacks the Wilson factorial tail used in (2). The photon statements use its dispersion and coupling rescaling, both properties of its law. [Free transfer](gap-seam-max.md) · [Check 1613](gap-direction7-fable-check-astra62.md)

**PROVED (what large-spin control does in weak compact $U(1)$).** For the Wilson cosine weight the multiplier of the integer charge $j$ is $e^{-\beta}I_{|j|}$. This follows by Fourier expansion of $e^{\beta\cos\theta}$. Group the two signs into the single projection indexed by $k=|j|$. The deletion proof of (4) applies to this projection because the convolution has the same scalar on its two summands. The Bessel series gives $\rho_k=I_k/I_0\le(\beta/2)^k/k!$. The raw electric score is $k/\beta+I_{k+1}/I_k-1$, with the same bounds $0\le g_\beta(k)\le k/\beta$ for $k>J$. Thus (5)–(7) hold with the same $J$. In (10) use $\beta/2$ in place of $\beta/4$ in $B_J$, by $I_{k+1}/I_k\le\beta/[2(k+1)]$. In the clamped formula $h_q=\partial_\beta\log(I_q/I_{q-1})>0$ by the same moment argument as in (12). The high-energy proof (1)–(2) also applies with $|j|$, since changing $(k+1)!$ to $k!$ leaves the leading $k\log k$ term. Thus none of these spectral estimates distinguishes the two compact Wilson laws.

**ON FILE (the law-dependent input for this comparison).** Row 1573 lines 131–150 and check 1579 item 9, using the periodic Villain comparison and positive offset mixture of rows 1565/1571, give $G_{\rm even}(u)\ge 2d_\gamma^4>1$ at every sufficiently weak Wilson cosine coupling at this aspect. The two nonzero electric charges $\pm2e_1$ survive the three half-turns. The comparison is uniform over the indicated even boxes. Its quantitative bound on their thermal masses is a statement about the measure. Keeping only zero integer charge by projection under the full continuous centre removes both witnesses. I use the on-file result with its periodic input. [Row 1573](gap-band-neutral-astra62.md) · [Check 1579](gap-band-neutral-astra62-check-opus.md)

**PROVED (location of failure in the retained observable, given that input).** For each such compact $U(1)$ box, take *any* finite window of width $w=\beta_h-\beta_K>0$ and continuous nonnegative speed whose endpoint satisfies HOT. Set $c=1/2$ and $D=\log[(1+c)/(1+4/21)]>0$. There is a last point with $G=c$ before HOT. On the closed interval from it to HOT the characteristic is cold. The total change of $X$ is at most $-D$. The mean value theorem gives an interior point where
$$
 t\left(\frac{\partial_\beta X}{t}-\kappa\bar E_t\right)\le-D/w .
$$
The real-period regularity follows by the Hilbert–Schmidt trace argument of check 1521 or by the same factorial multiplier bound as for Wilson $SU(2)$. On the prescribed finite window let $M_*=\max_\beta t(\beta)\bar E_{t(\beta)}>0$, which is finite by that regularity. Choose $\eta=D/(4wM_*)$, $\delta=\min(1,\beta_K D/(4wM_*))$. Using the lower side of (10) at the point just found gives, for the finite observable (12),
$$
                 t(H_J-\kappa\bar E_t)\le-D/(2w).                           \tag{13}
$$
This strengthens the mean-value test of check 1613 by locating a deficit after the large electric spins and the infinite-time vacuum have both been removed with controlled error. The argument does not identify the sign of any one charge contribution or any one plaquette mean. It gives no deficit on the $SU(2)$ trajectory.

**PROVED (dimension and seed tests).** In five-dimensional Wilson $SU(2)$ replace the link count by $d=4n^4$, $V_*$ by $12n^4$, and the deletion cost $8\beta$ by $12\beta$ since a spatial link touches six spatial plaquettes. Every proof from (1) through (12), including the sufficiency implication, then goes through with these constants. The needed surplus in (11) has no proved failure for weak interacting five-dimensional $SU(2)$. A surviving light neutral mode at the starting aspect would again force failure along any HOT path by the preceding argument. Its existence with the required quantitative bound is open here. The factors counting plaquettes change with dimension, but they do not give a dimension-selective sign.

The spin and vacuum error bounds in (6), (7) and (10) are compatible with failure of the seed. There is also a separation on the comparison class with a four-dimensional Wilson factor of row 1553, Lemma ALG. Tensor the Wilson transfer with a neutral, coupling-independent transverse Gaussian oscillator of energy $2\operatorname{arsinh}(\sin(\pi/n))$ and ground eigenvalue one. State $i$ paired with oscillator occupation $h$ has energy $m_i+h\,m_{\rm osc}$, and the same $b_i,b_i^J$ as before. Wherever the product is cold the Wilson factor is cold, so (6) holds also with the larger product energy. The truncated score acts on the Wilson factor, and the product thermal mean energy is larger by the oscillator mean. Equations (7) and (10) consequently still hold (or use the proof with the product gap and the same oscillation bound). Yet with $x=e^{-u m_{\rm osc}}>1/2$ the oscillator purity is $(1-x)/(1+x)<1/3$ by the geometric series. Purities multiply, so the product fails (PUR-io) at every permitted side and every cutoff. This is the massless-factor test of rows 998, 1553 and 1573 applied to the new estimates. The extra oscillator places this transfer outside pure Wilson theory. [Lemma ALG](gap-mech-direction4-fable.md) · [Product test](gap-band-neutral-astra62.md)

**ON FILE (Wilson handoff, check 1613).** With HOT on an infinite passing set, (11) would give the thermal seed at the specified side and (PUR-io) after the fixed enlargement of check 1613.

**ARGUED (scope).** I cannot establish either non-equivalence or equivalence of that sufficient *full* hypothesis to (PUR-io) on the calibrated pure Wilson family. The proved supply here is the error bound and its check. The sign and size of (12) for typical four-dimensional $SU(2)$ fields through the band remain the missing input. The local Wilson weights and the dimension-dependent counts alone cannot supply it.

## How much downward transport the discarded spins can supply

**PROVED (quantified restriction on a proposed band mechanism).** Let $K$ range over any infinite set of cutoffs, fix the release witnesses and side, and take arbitrary subintervals $[\alpha_K,\omega_K]\subset[\beta_K,\beta_h]$ of proposed cold characteristics. Use a common $c<1$ and $0<\delta\le1$. At each point take (5) and define the retained rate
$$
 R_J(\beta)=
 \frac{\sum_{i>0}b_i^J e^{-t(\beta)m_i}}
      {\sum_{i>0}m_i e^{-t(\beta)m_i}} .
$$
If VIR-down holds on the subinterval, then
$$
 \int_{\alpha_K}^{\omega_K} R_J(\beta)\,d\beta
 \ \ge\ \log\frac{t(\omega_K)}{t(\alpha_K)}
             -(1+\delta)\log\frac{\omega_K}{\alpha_K}.                     \tag{14}
$$
Divide the upper side of (6), after thermal averaging, by the positive mean energy. It gives $\kappa\le R_J+(1+\delta)/\beta$. Integrate and use $t'=\kappa t$. The sum defining $R_J$ is a trace with a bounded insertion at each fixed $J$, and (5) is a measurable integer choice bounded on each compact window, so this integration is legitimate.

In particular, for every such sequence with $\omega_K/\alpha_K\to1$, the discarded spins can supply only $o(1)$ of the integrated speed. This includes every uniformly bounded bare-width window since $\alpha_K\ge\beta_K\to\infty$. If a proposed mechanism gives $R_J\le0$ throughout these windows, the stretch satisfies $t(\omega_K)/t(\alpha_K)\le(\omega_K/\alpha_K)^{1+\delta}\to1$. Conversely a stretch bounded away from one requires a positive integrated retained response. This tests a mechanism on the actual Wilson boxes. There is no claim that HOT prescribes a minimum stretch or that the Wilson band has a particular bare width. Without the width assumption the explicit bound (14) still applies.

The new estimates are hand proofs by Codex. The single-plaquette integral checks the lower error, and a temporal-kernel comparison checks both errors independently of spatial deletion. The ordered comparison checks the level obstruction without differentiation. No other reader checked this row. No numerical experiment, Lean computation or new physical premise enters the proofs.

**RESULT — (d), a first component of thermal VIR-down.**
**PROVED.** On every cold finite Wilson box, (6)–(7) control the omitted electric spins relative to thermal energy, with separate field and kernel derivations at late bare coupling.
**PROVED.** Equation (10) replaces the vacuum by one finite period, (12) identifies the remaining signed field observable, and (14) bounds the integrated speed that large spins can supply.
**PROVED.** The high-level slope (2) and ordered limit (9) exclude every positive common level dilation on the calibrated boxes. This obstruction concerns the level form only.
The retained $SU(2)$ response in (11), HOT on a passing trajectory, (PUR-io) and the mass gap remain open. No (a), (b) or (c) for the thermal target.
