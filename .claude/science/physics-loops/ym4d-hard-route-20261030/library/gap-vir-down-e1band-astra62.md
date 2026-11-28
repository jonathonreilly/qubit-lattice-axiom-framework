# Repo search

Research text for row 1636 at `cfa849ab6ca5`. This note grants no status. The target-specific prior file was absent. The five refs searched were `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). The Markdown and TeX search for VIR-down, observed slope response, spin-cut form, hidden adverse trace and cold points of a characteristic returned no hits. Searches for a heat bridge or Gaussian midpoint giving a virial or slope, and for a one-step loop correlation, found pointers under main's `research/mass-gap/library/` in `gap-fp-astra.md`, `gap-sh-astra.md` and `gap-transfer-check.md`. The pinned working files outside this lane returned no literal target hit. Files of the concurrent E1-band attempts were excluded.

**ON FILE (PR 10114, local-block note (7)–(8)).** For a simple loop of length $p$ with centered trace $F$, the normalized local convolution dominates $(1+v_N/\rho)^{-1}|F\rangle\langle F|$, where $\rho=(I_2/I_1)^p$ and $v_2=1/4$. This bounds a one-step correlation at fixed coupling. The November 8 digest points to the same note on PRs 10114 and 10133. Main's transfer check also locates PR 10114's `MASS_GAP_CONSTRUCTION_ASTRA.md` (6)–(9), which gives the reversible law $\Omega^2 dx$ and the finite-box minorization $r\le1-e^{-2\beta L}$, with $L$ spatial links. Neither result controls the coupling slope at physical time. [November 8 digest, §11](prior/repo-search-2026-11-08.md)

**ON FILE (rows 941, 947, 1290 and check 1297).** The in-lane search for Gaussian midpoint, conditional replicas, heat bridge, gradient, Fisher information and slope found the Wilson representation used below. Row 941 (A7) gives the conditional independence of two slices given a Gaussian midpoint. Row 947 (B1)–(B5) gives the whole bridge and its squared-norm dissipation at fixed coupling. Row 1290 (1)–(3) bounds the gradient of a *Gaussian-averaged* eigenfunction on the arithmetic midpoint. I use those results to differentiate the observed Wilson multiplier in the original coupling. [Midpoint](gap-lsivac-max.md) · [Bridge](gap-fc-max.md) · [Gradient and check](gap-solve33-check-opus.md)

**ON FILE (outline index row 244).** Sussman and Alpoge, with Claude and Codex, supply the positive one-link Bessel multipliers in GL3 and the gauge-projected transfer and its periodic trace in GL8 (outline 2197–2243, 2315–2335, supplied revision `31a47c543775`). The outline at 3717–3720 leaves the spectral gap open. CA-I at 2703–2711 excludes it from Theorem 0. No estimate from Balaban is needed for the finite-box calculation. [Outline index](sa-index/README.md) · [Chunk 02](sa-index/chunk-02.md) · [Obligations](sa-index/obligations.md)

**ON FILE (VIR-DOWN, rows 1617, 1624, 1628, 1631 and checks 1630, 1634).** At $\kappa_0=1/16$ fix $b,g_0,L_h$ and the window depth $d$ before $K$. Put $\ell=L_h b^d$ and use $t=(n/512)e^{(\beta-\beta_K)/16}$. The required comparison is $N=\sum_{r<1}r^t\operatorname{Tr}(J_r b_r)\ge(1/16+\epsilon)W_t$ at **every** point with $G(t)=\sum_{0<r<1}r^t\operatorname{rank}F_r\le1/2$ on $[\beta_K,\beta_{K+d}]$, with the same $\epsilon>0$ for the specified infinitely many $K$ with $K+d\in E'$. Here $m=-\log r$, $W_t=\sum_{0<r<1}m r^t\operatorname{rank}F_r$ and $J_r$ projects onto the span of the projections of $\Omega{\bf1}_C$ into $F_r$ for the prescribed flowed-loop cells. Row 1628 (19)–(20) separately charges the hidden adverse trace. Check 1630 §1.3(d) also requires the running budget for the transport. Row 1631 (6) controls the replacement $N\mapsto N_q$ by $o(1) W_{\rm obs}$, where $W_{\rm obs}$ uses $\operatorname{rank}J_r$ in place of $\operatorname{rank}F_r$. Check 1634 finds no estimate of the retained sign. The adjacent LEV-FAIL row concerns a bound on *all individual* slopes. [Registry](open-registry.md) · [Two-sided tests](gap-vir-down-twoside-astra62.md) · [Window and E1](gap-vir-down-twoside-check-opus.md) · [Spin cut](gap-vir-down-e1-astra62.md) · [Check 1634](gap-vir-down-e12-check-opus.md)

## The observed response at a Wilson midpoint

I test the sign on the actual visible eigenvectors. The calculation keeps the spatial action, the vacuum normalization and the joint law of successive Wilson slices. The question is how much of the response can come from the change of the Gaussian time connecting the two slices.

**PROVED.** Fix any finite Wilson box in the question and $\beta>0$. Write $L=3n^3$, $D=4L$, $x\in(S^3)^L\subset\mathbb R^D$, $V(x)=\sum_p(1-W_p(x))$, $M=e^{-\beta V/2}$ and $\pi(dx)=\Omega(x)^2dx$ with Haar probability $dx$. Choose any real unit vector $\psi=\Omega f$ in an excited eigenspace at $r\lambda_0$. Write $b_\psi=\langle\psi,T'\psi\rangle/(r\lambda_0)-\lambda'_0/\lambda_0$ for the quadratic form of the compressed slope. Then $\int f^2\,d\pi=1$ and $\int f\,d\pi=0$. Set $a(dx)=M(x)\Omega(x)\,dx$. Take $X,Y$ from the stationary one-step pair with joint law proportional to
$$
 a(dx)a(dy)e^{-\beta|x-y|^2/2}.
$$
The unprojected temporal-gauge kernel acts as the projected one on these invariant vectors. Its positive simple Perron vector is gauge and centre invariant. Equivalently, in the projected pair integral sample the averaging transformation $h$ and use $hy$ as the second endpoint. Haar invariance and invariance of $M,\Omega,f$ give precisely the displayed pair law for the transported endpoints. With $W=(X+Y)/2$, $Z=W+\sigma G$ for an independent standard Gaussian $G$ in $\mathbb R^D$ and $\sigma^2=1/(4\beta)$, put
$$
 \eta=\operatorname{Law}(Z),\qquad
 g(z)=\frac{\mathbb E[f(X)\mid Z=z]}{\sqrt r},\qquad
 H(z)=\mathbb E[|z-X|^2\mid Z=z].
$$
Here $H$ is a scalar statistic of the vacuum Wilson pair. Then $\int g^2d\eta=1$ and the **actual normalized multiplier slope**, including the vacuum subtraction, is
$$
 \boxed{\quad b_\psi=\frac1{2\beta^2}\int |\nabla g|^2\,d\eta
    -2\operatorname{Cov}_\eta(g^2,H)-\operatorname{Cov}_\pi(f^2,V).\quad}       \tag{1}
$$
The gradient is taken on the auxiliary Euclidean space. Its contribution is strictly positive for every excited vector, including each vector in $\operatorname{ran}J_r$.

*Proof.* Write $p_s(v)=(2\pi s)^{-D/2}e^{-|v|^2/(2s)}$, $\tau=1/\beta$, $h_s=p_s*a$ and $k_s=p_s*(fa)$. At $s=\tau/2$ abbreviate these by $h,k$. Completing the square gives conditionally independent endpoints given $Z$ with common distribution $p_s(z-x)a(dx)/h(z)$, and $d\eta=h^2dz/\int h^2$. Thus $k/h=\sqrt r\,g$. The semigroup identity gives $\int k^2/\int h^2=r$ by the eigenvalue equation. It also gives $\int g\,d\eta=0$ by the vacuum marginal. This uses the on-file midpoint of row 941.

Differentiate the Rayleigh quotient for $\psi$ at the anchor holding its vector fixed. The same operation for $\Omega$ subtracts the vacuum derivative and defines $b_\psi$ even at a crossing. Each exterior factor contributes $-V/2$, giving $-\operatorname{Cov}_\pi(f^2,V)$ after both are differentiated. For the temporal factor keep $a$ and $f$ fixed during differentiation. The Gaussian normalization $(2\pi\tau)^{D/2}$ cancels in the difference of logarithmic derivatives. The remaining logarithmic derivative is that of $\int k_{\tau/2}^2/\int h_{\tau/2}^2$. For either heat extension $v$, one has $d\int v_{\tau/2}^2/d\tau=-\tfrac12\int|\nabla v_{\tau/2}|^2$. Multiplication by $d\tau/d\beta=-1/\beta^2$ gives the positive sign in (1). Dividing $k$ by $\sqrt r$ for the calculation at the anchor gives $hg$. Integration by parts gives
$$
 \int|\nabla(hg)|^2=\int h^2|\nabla g|^2-\int g^2 h\Delta h,\qquad
 \frac{\Delta h}{h}=-2\beta D+4\beta^2 H .
$$
Subtract the same expression at $g=1$. This proves (1). Every eigenvector with $r>0$ is smooth on the compact slice by its kernel equation and the vacuum is strictly positive. The heat extensions have Gaussian tails. The conditional-mean formula bounds $g$ and its derivatives at each fixed box since the endpoint coordinates and $f$ are bounded. These facts justify the integrations. If the gradient vanished in $L^2(\eta)$, the smooth $g$ would be constant on the connected ambient space with everywhere positive density. Its mean zero and norm one exclude that case. $\square$

**PROVED (direct field check of the mark).** Put $q(z)=\mathbb E[X\mid Z=z]$. Differentiating the conditional density gives $\nabla g=2\beta(\mathbb E[Xf(X)\mid Z]/\sqrt r-gq)$. In the original one-step kernel the temporal derivative inserts $X\cdot Y-L$. Conditional independence therefore gives the temporal slope directly as
$$
 \mathbb E_\eta\big|gq+\nabla g/(2\beta)\big|^2-\mathbb E_\eta |q|^2 .
$$
The constant $-L$ cancels because $\mathbb E[f(X)f(Y)]=r$. In this formula $\nabla\log(d\eta/dz)=4\beta(q-z)$ and $\operatorname{div}q=2\beta(L-|q|^2)$ by differentiating the same conditional law and using $|X|^2=L$. Integrating the cross term by parts gives
$$
 -\frac{1}{2\beta}\,\frac{\operatorname{div}(q\,d\eta/dz)}{d\eta/dz}
     =-L-|q|^2+2z\cdot q .
$$
This expression has mean zero. Expanding the square therefore gives $\int|\nabla g|^2d\eta/(4\beta^2)+2\operatorname{Cov}_\eta(g^2,z\cdot q)$ for the temporal slope.

There is a direct check using the unit length of every link. For $B(z)=\int e^{2\beta z\cdot x}a(dx)$ both $B$ and $Bg$ solve $\Delta_{z_e}v=4\beta^2 v$ separately on each link, by $|x_e|=1$. The one-link exponential identity also occurs in check 790 of row 785. [One-link calculation](gap-vmf-lip-check-opus.md)

Since $\nabla\log B=2\beta q$ and $d\eta/dz\propto B^2 e^{-2\beta |z|^2}$, this gives
$$
 (\Delta_{z_e}+\nabla_{z_e}\log(d\eta/dz)\cdot\nabla_{z_e})g
       =-4\beta z_e\cdot\nabla_{z_e}g .
$$
Integrate first against $g$ and then integrate $z_e\cdot\nabla_{z_e}(g^2)$ by parts against $\eta$. Since $\int g^2d\eta=1$, subtract the constant test $g=1$ to get
$$
 \frac1{4\beta^2}\int|\nabla_{z_e}g|^2\,d\eta
   =2\operatorname{Cov}_\eta\big(g^2,\ |z_e|^2-z_e\cdot q_e(z)\big)\ \ge 0 .       \tag{2}
$$
Thus the temporal slope equals $2\operatorname{Cov}_\eta(g^2,|Z|^2)$, also obtained directly from $2|W|^2=L+X\cdot Y$ by integrating the independent noise conditional on $X,Y$. Substitution of $H=|z|^2+L-2z\cdot q$ and (2) reproduces (1), including the factor two. Equation (2) fixes a sign of a particular radial field response in the true observed state at every coupling. The non-strict link signs sum strictly. The sign of the total radius covariance for isotropic Wilson remains open. The radius reading itself occurs in row 1290 and in the midpoint-radius analysis. [Midpoint-radius analysis](gap-seed2-astra62.md)

## How much of the observed slope a change of Gaussian time can supply

**PROVED.** Keep all spins and all excited energies. For $s_0=\tau/2\le s\le s_1=3\tau/4$ let $s'=\tau-s$ and define
$$
 d\nu_s=\frac{h_s h_{s'}}{\int h_s h_{s'}}dz,\qquad
 u_s=\frac{k_{s'}}{h_{s'}},\quad F(s)=\int u_s^2d\nu_s,\quad
 B_s=\nabla^2\log h_{s'}-\nabla^2\log h_s .
$$
Here $u_s$ predicts the right endpoint $f(Y)$ from the bridge at $s$. Write $\mathcal L_s=\Delta+\nabla\log(d\nu_s/dz)\cdot\nabla$, $\alpha_s=F'(s)/F(s)$, and define
$$
 C_s(f)=\frac{\int\nabla u_s^{\mathsf T}B_s\nabla u_s\,d\nu_s}{F(s)},\qquad
 D_s(f)=\frac{\int|\mathcal L_s u_s+\alpha_s u_s|^2\,d\nu_s}{F(s)} .
$$
With $S_\psi=-2\operatorname{Cov}_\eta(g^2,H)-\operatorname{Cov}_\pi(f^2,V)$, the per-state response is
$$
 b_\psi=S_\psi+
 \underbrace{\frac{2}{\beta}\log\!\frac{F(s_1)}{r}}_{A_\psi}
 +\frac{2}{\beta}\int_{s_0}^{s_1}(s_1-s)\,[C_s(f)-D_s(f)]\,ds ,
 \qquad 0\le A_\psi\le\frac{2m}{\beta}.                                      \tag{3}
$$
The integrated square subtracted in (3) is strictly positive for every finite-box Wilson excitation. The estimate applies to the low-energy eigenvectors used in row 1631, with their full Wilson weights.

*Proof.* The positive joint density of $X,Z_s,Y$ is proportional to $a(dx)p_s(z-x)p_{s'}(z-y)a(dy)dz$. This gives $F(s_0)=r$ and $F(s)\le1$ by conditional Jensen. Write $v_s=\nabla\log h_{s'}$. Differentiating the two heat extensions gives
$$
 (\partial_s+\tfrac12\Delta+v_s\cdot\nabla)u_s=0,\qquad
 \partial_s\nu_s=\tfrac12\Delta\nu_s-\operatorname{div}(v_s\nu_s)
$$
in density notation. Differentiation and integration by parts yield row 947's identity $F'=\int|\nabla u_s|^2d\nu_s$. Differentiating it once more, the operator on the left applied to $|\nabla u_s|^2$ gives $\|\nabla^2u_s\|_{\rm HS}^2-2\nabla u_s^{\mathsf T}(\nabla^2\log h_{s'})\nabla u_s$. All times are separated from the singular endpoints. The extension formulas and compact endpoint support bound all derivatives used here by a polynomial in $|z|$ times a fixed-box constant under a Gaussian tail.

For a smooth test $u$, integration by parts first gives $\int(\mathcal L_s u)^2d\nu_s=-\int\nabla u\cdot\nabla\mathcal L_s u\,d\nu_s$. In component $i$, commute the derivative past $\mathcal L_s$, giving $\mathcal L_s\partial_i u+\sum_j\partial_{ij}\log(d\nu_s/dz)\partial_j u$. A second integration gives
$$
 \int(\mathcal L_s u)^2d\nu_s=
 \int\{\|\nabla^2u\|_{\rm HS}^2-
       \nabla u^{\mathsf T}\nabla^2\log(d\nu_s/dz)\nabla u\}\,d\nu_s .
$$
Use $\log(d\nu_s/dz)=\log h_s+\log h_{s'}+\mathrm{const}$ and $\int u_s\mathcal L_su_s\,d\nu_s=-F'$. Completing the square gives the exact identity $(\log F)''=D_s(f)-C_s(f)$. At $s_0$, $\nu_{s_0}=\eta$ and $u_{s_0}=\sqrt r\,g$, hence $\alpha_{s_0}=\int|\nabla g|^2d\eta$. Integrate $(\log F)''$ with weight $s_1-s$. The coefficient of $\alpha_{s_0}$ in the Taylor formula is $s_1-s_0=1/(4\beta)$. Equation (1) now gives (3). Monotonicity $F'\ge0$ and $F(s_1)\le1$ give its upper bound with $m=-\log r$, at *every* energy.

To check strictness, $D_{s_0}=0$ would imply $\mathcal L_{s_0}g=-\alpha_{s_0}g$ pointwise by smoothness and the positive density. Summing the link identities above (2) would then give $z\cdot\nabla g=(\alpha_{s_0}/(4\beta))g$. Along each ray this implies $g(Rz)=R^{\alpha_{s_0}/(4\beta)}g(z)$ for every $R>0$. Excitation gives $\alpha_{s_0}>0$ by (1)'s strict-gradient argument, while $g$ is bounded on all of $\mathbb R^D$ by $\|f\|_\infty/\sqrt r$. Thus $g=0$, contrary to its unit norm. Continuity gives strictly positive integrated loss in a right neighbourhood of $s_0$. No cutoff-uniform lower bound for this loss has been used. $\square$

## A bound for the entire retained trace

**PROVED.** The following version of (3) gives a basis-independent measure of the Wilson fields sampled by the bound. Include every excited $r$ for which $k_r=\operatorname{rank}J_r>0$. At fixed $r$ use a real orthonormal basis of its visible subspace, with predictions $u_{s,j}$. In (3) apply the proof to the vector $(u_{s,1},\ldots,u_{s,k_r})/\sqrt{k_r}$ and its squared Euclidean norm. Write $\mathcal F_r(s)=k_r^{-1}\sum_j\int u_{s,j}^2d\nu_s$ for their averaged squared norm. Put
$$
 Y_r(s,z)=k_r^{-1}\sum_j\nabla u_{s,j}(z)\nabla u_{s,j}(z)^{\mathsf T},\qquad
 d\Gamma_t(r,s,z)=k_r r^t\,\frac{\operatorname{tr}Y_r(s,z)}{\mathcal F_r(s)}\,d\nu_s(z)\,ds .
$$
For a symmetric matrix $B$ let $[B]_Y=\operatorname{tr}(YB)/\operatorname{tr}Y$ when the denominator is positive and zero elsewhere. Write $S(t)=\sum_{r,j}r^t S_{\psi_j}$. Then
$$
 \begin{split}
 \|\Gamma_t\|&=\sum_r k_r r^t\log\frac{\mathcal F_r(s_1)}r\ \le W_{\rm obs},\\
 Q_+(t)&=\int\frac2\beta(s_1-s)\big([B_s]_{Y_r}\big)_+\,d\Gamma_t,\qquad
 N(t,\beta)< S(t)+\frac2\beta W_{\rm obs}+Q_+(t).
 \end{split}                                                                \tag{4}
$$
All three quantities are invariant under the basis choice. To verify (4), the differentiation and two integrations by parts in (3) apply component by component before taking the logarithm of the averaged squared norm. The resulting square uses the common scalar $\mathcal F_r'/\mathcal F_r$. Vanishing at the midpoint would force each component to be homogeneous of the same positive degree, contradicting boundedness as above. Dropping the square and taking the scalar positive part gives (4). The partition has at least one visible excitation. With all other links set to the identity, varying one boundary link of a specified square gives traces in the interiors of two different bins. Their open neighbourhoods have open inverse images under the finite-time flow and positive vacuum probability. At least one centered cell indicator is nonzero and has a projection onto a positive excited eigenspace by injectivity of the transfer (rows 1617, 1624 and 1628).

The matrices in (4) have a direct field meaning. Let $\Sigma_v(z)$ be the covariance of the entire endpoint link vector under $p_v(z-x)a(dx)/h_v(z)$. Differentiation gives $\nabla^2\log h_v=-I/v+\Sigma_v/v^2$. In particular,
$$
 B_s=(1/s-1/s')I+\Sigma_{s'}/(s')^2-\Sigma_s/s^2,\qquad
     Q_+(t)\le 2\int [\Sigma_{s'}(z)]_{Y_r}\,d\Gamma_t .                     \tag{5}
$$
Indeed $1/s-1/s'\le0$ and $\Sigma_s$ is positive semidefinite. With $x=\beta s$ the coefficient of $\Sigma_{s'}$ after the time weighting is $2(3/4-x)/(1-x)^2\le2$ for $1/2\le x\le3/4$, since $(1-x)^2-(3/4-x)=(x-1/2)^2$. The integral in (5) measures conditional variance in the directions in which the observed endpoint predictions vary. The normalization $\|\Gamma_t\|\le W_{\rm obs}$ costs no volume factor and applies even when the thermal trace is very small.

At a fixed box $\|\Sigma_v\|\le L$, and $v\ge\tau/4$ in the interval used, so the signed curvature term and its positive part are absolutely integrable against $\Gamma_t$. Also $H(z)\le 2(|z|^2+L)$. By conditional Jensen, $r\int g^2 H\,d\eta\le\mathbb E[f(X)^2 H(Z)]$. Conditional on the two endpoints, $\mathbb E |Z|^2=|W|^2+D/(4\beta)\le L+D/(4\beta)$, so the latter bound is finite uniformly in the chosen unit eigenvector at this box. The spatial insertion is bounded. Hence $S(t)$ converges absolutely for $t>2$ by trace class. Equation (1) or the bound $|\operatorname{Cov}(X,f\mid Z)|^2\le L\operatorname{Var}(f\mid Z)$ from Cauchy–Schwarz also gives absolute summability of the kinetic term. These bounds justify summing the strict finite-block estimates and retaining at least one strict loss.

**PROVED (consequence for the spin-cut target).** On every cold window point of check 1630, row 1631 (6) and (4) give
$$
 N_q\le S(t)+Q_+(t)+(2/\beta+\eta_K)W_{\rm obs},\qquad \eta_K\longrightarrow0
                                                                            \tag{6}
$$
uniformly in the window. Thus even the full observed spectrum can contribute at most $2W_{\rm obs}/\beta$ through $A_\psi$ in (3) (or its block version). This bound holds before imposing any spin, energy or slab-action cutoff. For (E1) itself one necessarily has
$$
 S(t)+Q_+(t)>(1/16+\epsilon)W_t-2W_{\rm obs}/\beta .
$$
For example, at any sufficiently late such point with $S(t)\le0$, (E1) would force $2\int[\Sigma_{s'}]_{Y_r}d\Gamma_t>(1/16+\epsilon-2/\beta)W_t$. This requires an order-one directional variance per unit of the gradient measure, even if all individual link marginals have small variance. The sum of signed scalar action covariances is a separate way to pay the bound. Neither one is known to have the necessary size. Formula (3) by itself is an identity. The sign, the uniform upper bound and the measured necessary condition (4)–(6) use additional inequalities.

## Which change in the conditional field law can contribute

**ON FILE (row 947 §5.6, Stage 2).** Its formula for the derivative of $\int|\nabla u_s|^2d\nu_s$ contains the conditional variance of the endpoint in direction $\nabla u_s$. Its proposed COV-dir is an upper bound on that variance sufficient, with endpoint control, for a gradient-contraction estimate. The first differentiation in the proof of (3) uses this earlier calculation. The logarithm, the difference of the two Hessians, the strictly subtracted square and the weight bounded by $W_{\rm obs}$ in (4) concern the coupling slope. The marginal-Hessian identity used next also occurs for a different kernel in the [convex maximal-correlation note, lines 39–52](convex-maximal-correlation.md). Searches of the five refs in the YM directories for COV-dir, Gaussian midpoint, Hessian contrast and a heat frequency function found no further matching item. [Bridge and COV-dir](gap-fc-max.md) · [Check and endpoint qualifications](gap-fc-check-astra.md)

**PROVED (a fixed-resolution conditional covariance estimate).** In (5) the part of the conditional variance constant in the applied field can itself be removed. For $s_0<s\le s_1$ put $v=s'$, $\delta=s-v$, and let
$$
 K_z(dy)=p_\delta(z-y)h_v(y)\,dy/h_s(z),\qquad
 q_v(y)=\mathbb E[X\mid y\text{ at variance }v].
$$
This is the law at the earlier time $v$ conditional on the position $z$ at $s$ on the same Wilson bridge. Use $K_z A$ for the integral of a matrix function $A$ against this probability. Then
$$
 v^2 B_s(z)
   =\Sigma_v(z)-K_z\Sigma_v
       -\operatorname{Cov}_{K_z}\big(q_v(y)-y\big) .
                                                                            \tag{7}
$$
Indeed $h_s=p_\delta*h_v$. Differentiate in translated coordinates, moving both derivatives onto $h_v$. Division by $h_s$ gives $\nabla^2\log h_s=K_z\nabla^2\log h_v+\operatorname{Cov}_{K_z}(\nabla\log h_v)$. The heat kernel gives $\nabla\log h_v(y)=(q_v(y)-y)/v$ and $\nabla^2\log h_v(y)=-I/v+\Sigma_v(y)/v^2$. Substitution proves (7). All the integrals converge by the same Gaussian bounds as (3).

Consequently the last term of (4) satisfies the stronger all-level estimate
$$
 Q_+(t)\ \le\ 2\int
    \big([\Sigma_v(z)-K_z\Sigma_v]_{Y_r}\big)_+\,d\Gamma_t .                \tag{8}
$$
The coefficient two is the same time-weight bound proved in (5). The signed matrix difference compares susceptibilities at the **same** resolution $v$. The last covariance in (7) always subtracts. The variation in (8) can also be read on the link fields. For a fixed unit direction $w$ and $z_\theta=y+\theta(z-y)$, differentiation of the tilted probability $p_v(z_\theta-x)a(dx)/h_v(z_\theta)$ gives
$$
 w^{\mathsf T}\big(\Sigma_v(z)-\Sigma_v(y)\big)w
  =\frac1v\int_0^1
    \mathbb E_{v,z_\theta}\!\left[
       \big(w\cdot(X-q_v)\big)^2\big((z-y)\cdot(X-q_v)\big)\right]\,d\theta .       \tag{9}
$$
Here $q_v$ is evaluated at $z_\theta$. In the derivative of the centered square the derivative of its mean multiplies a centered first moment and vanishes. Diagonalizing the positive matrix $Y_r/\operatorname{tr}Y_r$ averages this identity over its directional weights. Thus (8) only charges a positive change of conditional variance, measured by a centered third moment of the actual tilted endpoint law. An elementary conditional variance bound on the individual links would not control this collective contraction. Equation (8) is an upper bound on a possible contribution to (E1).

**PROVED (testing the sign on the Wilson measure).** The two Hessians have neither pointwise ordering on the observed directions. For *every* finite box in the question, every $\beta>1$, every $s_0<s\le s_1$ and every nonzero excited visible block, both $\{[B_s]_{Y_r}>0\}$ and $\{[B_s]_{Y_r}<0\}$ have positive measure for the spatial density $\operatorname{tr}Y_r\,d\nu_s/\mathcal F_r(s)$. This tests the sign after restricting the directions to the observable, including an arbitrarily small spectral overlap.

At $z=0$ the conditional endpoint law is proportional to $a(dx)$ for both resolutions since $|x|^2=L$. Its covariance is $I/4$ on the full link vector. A vertex rotation makes the single-link marginal Haar, and flipping a vertex incident to just one of two distinct links kills the cross moment. The torus sizes here have distinct unordered pairs of endpoints for distinct links. These are row 941 (A5) and its check. At zero the matrix in (5) is therefore
$$
 B_s(0)=(1/s'-1/s)\big((1/s+1/s')/4-1\big)I>0 ,
$$
using $1/s+1/s'\ge4\beta$. Continuity gives an open set with strictly positive definite $B_s$. In the other direction fix any link configuration $x_*$ and let $z=R x_*$ with $R\to\infty$. At either variance the density on the slice is proportional to $e^{R x_*\cdot x/v}a(dx)$, with unique maximizer of the tilt at $x=x_*$. Outside any neighbourhood of $x_*$ the exponent per $R$ is separated below its maximum. Integrating on a smaller neighbourhood with positive $a$-mass proves concentration at $x_*$ and therefore convergence of both covariance matrices to zero at this fixed box. Thus $B_s(Rx_*)\to(1/s-1/s')I<0$, giving an open set with negative definite contrast.

For any nonconstant basis vector $f$, its conditional mean $u_s(z)$ is a ratio of real analytic exponential integrals with positive denominator. It cannot be constant on an open set. Constancy there gives constancy everywhere by analyticity. Then all moments of the signed measure $(f-c)a$ vanish by differentiating the tilt at zero, and polynomials are dense on the compact product of spheres, forcing $f=c$. Thus $\operatorname{tr}Y_r$ is positive on a nonempty open subset of each region. The bridge density is strictly positive there. This proves the two signs. The check of row 947 §5.5 tests the zero-field curvature of the sum of the two log densities. The difference tested here has both signs after weighting by a particular visible eigenspace. The open-set lower bounds can shrink relative to $W_t$ as $K$ grows. [Check of row 947](gap-fc-check-astra.md)

## A same-group test at the prescribed cutoffs

**ON FILE (rows 710, 843, 1325 and 1619).** Row 710 Proposition EL diagonalizes the model with the spatial plaquette term deleted and bounds its level rate for $0<\beta\le2$. Row 1619 §3.0 gives numerical guides for its weak-coupling rate, including examples above $1/\beta$. Row 843 and row 1617 (12) identify each adjacent Bessel ratio as a tilted mean. Row 1325 (19), checked in 1327, proves the decay of the electric multipliers with spin and $-\log(I_2/I_1)\sim3/(2\beta)$. A search for the electric-only purity, cold-window slope and an all-order Bessel logarithmic-slope bound in the lane and the five refs' YM sources gave no supplier for the comparison below. [Proposition EL](gap-vir-sc.md) · [Rate guide](gap-vir-down-fable.md) · [Bessel moments](gap-vir-down-astra62.md) · [Check 1327](gap-solve40-check-opus.md)

**PROVED.** For every integer $j\ge1$ and $\beta>0$, put $R_j=I_{j+1}(\beta)/I_j(\beta)$ and $a_j=-\log R_j$. Then
$$
 0<(\log R_j)'\le\frac{a_j}{\beta\log 2}.                                   \tag{10}
$$
In fact under density proportional to $e^{\beta x}(1-x^2)^{j-1/2}$ on $(-1,1)$ the mean is $R_j\in(0,1)$ and $R_j'$ is the variance, by the Bessel moment formula. The recurrence gives $R_j/\beta=1/(2(j+1)+\beta R_{j+1})$, a decreasing function, so $\beta R'_j\le R_j$. For a second bound put $y=\beta(1-x)$. Its density is proportional to $e^{-y}y^{j-1/2}(2-y/\beta)^{j-1/2}$ on $(0,2\beta)$. Increasing $\beta$ increases the likelihood ratio with $y$ on the common support, since the ratio of the two factors $2-y/\beta$ is increasing, and adds weight only to its right. The normalized densities therefore cross from smaller to larger at most once, proving that the mean $\beta(1-R_j)$ is nondecreasing. This gives $\beta R'_j\le1-R_j$. Put $y_0=(1-R_j)/R_j$. For $y_0\le1$ concavity gives $\log(1+y_0)\ge y_0\log2$. For $y_0\ge1$ monotonicity gives $\log(1+y_0)\ge\log2$. Thus $\min(1,y_0)\le a_j/\log2$, which proves (10).

As a check on the inequality $\beta R'_j\le R_j$, integrating the derivative of $e^{\beta x}(1-x^2)^{j+1/2}$ gives $R_j/\beta=\mathbb E(1-x^2)/(2j+1)$. Its derivative is nonpositive since $\operatorname{Cov}(x^2,x)\ge0$. Indeed, conditional on $|x|=u$, the mean of $x$ is $u\tanh(\beta u)$ and both this and $u^2$ increase with $u$. Their covariance is half the expected product of their differences on independent copies. This check uses the tilted integral in place of the adjacent-ratio recurrence.

**PROVED (bound directly on the interacting spin cut).** In row 1631's electric placement take $w_{\psi}=C^{1/2}M\psi/\sqrt{r\lambda_0}$, with $r=1$ for the vacuum. For its cut $q$ put
$$
 d_j(t)=\sum_{r,h}r^t\sum_e
  \left\{\Pr_{w_{\psi_h}}(k_e\ge j)-\Pr_{w_\Omega}(k_e\ge j)\right\},
 \qquad M_q(t)=\sum_{r,h}r^t B_M^{[q]}(\psi_h)
$$
using only the visible basis vectors. Row 1631 telescopes the clamped electric score as $\sum_{j=1}^q(\log R_j)' d_j(t)$. Since its coefficients are positive, (10) yields
$$
     N_q\le M_q(t)+\frac1{\beta\log2}\sum_{j=1}^q a_j(d_j(t))_+ .           \tag{11}
$$
These are the retained spins of the actual Wilson eigenvectors. In particular, if $M_q\le0$ at a late cold point satisfying (E1), the positive excess of cumulative electric-spin probabilities, weighted by their electric energy increments $a_j$, must be at least $\beta\log2\{(1/16+\epsilon)W_t-\eta_K W_{\rm obs}\}$. The estimate charges only differences in the observed and vacuum spin laws. A bound on the bare one-link multipliers alone does not supply this difference or the signed coherences in $M_q$.

**PROVED (purity and E1 separate on a four-dimensional SU(2) comparison).** Keep the lattice, centre projection, coupling numbers, times and loop observation of the task. Set only the *transfer's* spatial potential to zero, so $T=C$ on the invariant space. On a link with label $k=2j_{\rm spin}$ the normalized multiplier is $\prod_{j=1}^kR_j$. Its energy is $\sum_{j=1}^k a_j$ and its log slope is $\sum_{j=1}^k(\log R_j)'$. Products over links add both. The preceding proof gives $0\le b_r\le (m/(\beta\log2))I$ as a quadratic-form bound on every eigenspace, including coincidences of products with different spin labels. Thus *every* observation satisfies
$$
       0\le N(t,\beta)\le W_{\rm obs}/(\beta\log2)\le W_t/(\beta\log2).
                                                                            \tag{12}
$$
There are excited neutral states, for example the character of an elementary spatial plaquette, so $W_t>0$. Equation (12) violates (E1) at every point with $\beta>1/(\kappa_0\log2)$ for any fixed $\kappa_0>0$.

These comparison windows are genuinely cold. At $\beta=1$, the Bessel series gives $R_j(1)\le1/[2(j+1)]\le1/4$. Monotonicity of $\beta(1-R_j)$ gives $a_j\ge1-R_j\ge3/(4\beta)$ for all $j\ge1,\ \beta\ge1$. Before projection the normalized trace at $t$ is the product of $L$ one-link sums with multiplicity $(k+1)^2$ at label $k$. Thus
$$
 1+G(t)\ \le\left(1+\sum_{k\ge1}(k+1)^2e^{-3kt/(4\beta)}\right)^L=1+o(1).
$$
Indeed for $y=e^{-3t/(4\beta)}\le1/2$ the sum is bounded by $y\sum_{k\ge1}(k+1)^2\,2^{1-k}$. On every fixed-depth window $t\ge n/512$ and $\beta=O(\log n)$, so $Ly\to0$ uniformly. Projection preserves the constant vacuum and decreases the trace. At $u=n/512$ the purity $(1+G(2u))/(1+G(u))^2$ tends to one. The seed's numerical bound therefore holds for all large $K$ in this comparison, while (E1) fails at **every** point of **every** sufficiently late window. This is a separation with the same gauge group, centre, dimension and bare sequence. The specified $\beta_K$ are used as coupling numbers in this finite-transfer comparison. Calibration of the modified action would be a separate problem. The step in (12) that fails for isotropic Wilson is the use of the product-spin eigenvectors and constant vacuum. The magnetic half-weights change both of the state laws in (11).

## Checks and selectivity

**PROVED (Gaussian check by direct integration).** In one real transverse oscillator of frequency $\omega>0$, take the temporal weight $e^{-\beta(x-y)^2/2}$ and spatial action $V(x)=(\cosh\omega-1)x^2$. The dilation $x\mapsto\sqrt\beta\,x$ leaves all normalized eigenvalues fixed. Completing the square gives the vacuum $\Omega\propto e^{-\beta\sinh(\omega)x^2/2}$, boundary measure $a$ of precision $c=\beta(e^\omega-1)$, and first normalized endpoint eigenfunction $f(x)=\sqrt{2\beta\sinh\omega}\,x$ with $r=e^{-\omega}$. Indeed the conditional mean of the next endpoint given $x$ is $e^{-\omega}x$. At the bridge time $s$, $u_s(z)=\sqrt{2\beta\sinh\omega}\,z/(1+cs')$, and the variance of $z$ is $(1+cs)(1+cs')/[c(2+c\tau)]$. Thus
$$
 F(s)=r\,\frac{1+cs}{1+cs'},\qquad
 \alpha_s=\frac{c}{1+cs}+\frac{c}{1+cs'},\qquad
 B_s=\frac{c}{1+cs}-\frac{c}{1+cs'}\le0 .
$$
Here $\mathcal L_s u_s=-\alpha_s u_s$ so the square in (3) is zero. Direct differentiation gives $(\log F)''=-\alpha_s B_s$, precisely the sign and weight in (3). For a direct check on the scalar terms, put $a_*=\tanh(\omega/2)$. Under $\pi$, $f=x/\sqrt{\mathbb E x^2}$, so $\operatorname{Cov}_\pi(f^2,V)=2(\cosh\omega-1)\mathbb E x^2=a_*/\beta$. At the midpoint $g=z/\sqrt{\mathbb E z^2}$, $\mathbb E z^2=1/(4\beta a_*)$, and $H(z)=\operatorname{Var}(X\mid z)+a_*^2 z^2$ with constant conditional variance. The Gaussian fourth moment therefore gives $2\operatorname{Cov}_\eta(g^2,H)=a_*/\beta$. Together they cancel the positive midpoint term $\alpha_{s_0}/(2\beta^2)=2a_*/\beta$ as required by the independently fixed spectrum. For a Gaussian endpoint measure of any positive precision, $\Sigma_v$ is independent of $z$, so the excess in (8) vanishes exactly. This checks the upper bound on a law with nonzero midpoint response. The Gaussian bridge precision itself is on file in row 947 §5.4. Formula (2) and its strict-square argument used fixed link length and bounded predictors. The oscillator's linear predictor is unbounded.

**ON FILE (rows 1618, 1626, 1628 (22), check 1630).** For the full transverse photon every normalized energy is independent of $\beta$ in rescaled coordinates. In the zero-monopole, zero-magnetic-flux compact Gaussian U(1) comparison the positive even electric-rotor slopes have $Q\ne0$ and all the contractible-loop predictions lie in $Q=0$. Thus $N=0$ for every period, including a cold one, whereas $W_t>0$. This uses both the flat-shift symmetry and the photon law. Evaluating the bridge on the observed photon factor gives zero excess in (8) and $S(t)\le0$ by (1). [Gaussian transfer](gap-vir-down-neon.md) · [Observed-sector test](gap-vir-down-twoside-astra62.md)

**PROVED (weak cosine U(1) and five-dimensional SU(2)).** For the compact U(1) *Wilson cosine* weight, use each link as a unit vector in $\mathbb R^2$. The temporal weight is the same Euclidean Gaussian restricted to the product of circles. Equations (1)–(9), including both signs on the measured directions, go through. At zero the covariance is $I/2$ by gauge invariance, making the origin test positive for $\beta>1/2$. For the Fourier multipliers $I_k/I_0$, (10) treats every adjacent ratio except $R_0$. For that ratio the $y=\beta(1-x)$ density has power $-1/2$. Its moments through order two converge to those of the density proportional to $e^{-y}y^{-1/2}$. Indeed, on $0<y<\beta$ use domination by $e^{-y}y^{j-1/2}$ for moment $j$, and the integral over $(\beta,2\beta)$ is bounded by a constant times $e^{-\beta}\beta^{j+1/2}$ by rescaling $y/\beta$. Integration by parts in the limiting integrals gives mean and variance $1/2$. Hence $-\log R_0\sim1/(2\beta)$ and $R'_0=\operatorname{Var}(x)\sim1/(2\beta^2)$, so (10) also covers this ratio at all sufficiently late couplings. For five-dimensional Wilson SU(2) use $L=4n^4$ and its six spatial plaquette orientations in $V$. The unit-quaternion midpoint, the origin covariance $I/4$, the Bessel bound and the two-sign argument all persist. With the same imposed time and bare-coupling scalings, the electric-only comparison in either cosine U(1) or five-dimensional SU(2) still has a cold trace since a polynomial link count times $e^{-c n/\log n}$ tends to zero. The compact Gaussian calculation of $N=0$ uses a different law and does not determine $N$ in either interacting Wilson comparison.

**ARGUED (where the selective estimate is missing).** The field inputs left by (4) and (8) are the observed-minus-vacuum spatial action and midpoint displacement in $S(t)$, and a change in endpoint covariance in the directions that predict the flowed loops. Their weights come from the actual two-slice Wilson law at the prescribed $n,\beta,t$. Both signs found on open sets are compatible with vanishing total weight there as $K$ increases. An order-one weighted excess in four dimensions and its absence in five dimensions do not follow from those sign tests. The four-dimensional electric-only example shows that the same gauge algebra, centre and dimension allow the purity threshold together with failure of (E1). For the isotropic Wilson family the comparison supplies no converse between the seed and (E1). [Lemma ALG, row 1553](gap-mech-direction4-fable.md)

**PROVED (scope of the signed bounds, using the spectator of rows 1553 and 1631).** Tensor an arbitrary Wilson box with an unobserved neutral oscillator of normalized multipliers $e^{-j/n}$, $j=0,1,\ldots$, fixed in $\beta$. A loop cell times the product vacuum has only the oscillator ground component. Its projection onto any product eigenspace therefore gives exactly the visible Wilson projection tensored with that ground component, even at a coincidence of multipliers. All the observed terms of (1)–(5) remain the Wilson terms. Product coldness implies Wilson coldness for the use of (6). At $u=n/512$ the extra factor in the purity is $(1-x)/(1+x)$ with $x=e^{-1/512}>1/2$, by the two geometric trace sums. The resulting purity is below $1/3$ at every cutoff. Thus the signed bounds are compatible with failure of the numerical seed as well. [Spectator test in row 1631](gap-vir-down-e1-astra62.md)

**PROVED (quantifier for using this as an obstruction).** Fix the release parameters, positive rate and depth. If at **each** sufficiently late eligible $K$ there were a cold window point with $(S(t)+Q_+(t))/W_t\le\kappa_0+o(1)$ uniformly along those choices, (4) would exclude every fixed $\epsilon>0$ and every infinite subsequence for that choice of parameters. No such points have been proved for isotropic Wilson. Rates, other choices of release parameters and the running budget would still have to be treated for a general disproof. All proofs and comparison checks are by hand. No numerical computation, Lean run or separate reader was used.

**RESULT (d), a non-tail piece of the observed Wilson slope.** **PROVED** the linkwise sign (2), the all-energy bound $\sum_{r,h}r^t A_{\psi_h}\le2W_{\rm obs}/\beta$ with a strictly subtracted square, and the spin-cut bound (6).  
**PROVED** (7)–(9) charge positive bridge curvature only to a change in a conditional covariance at fixed resolution. Both curvature signs have positive observed-gradient measure on every late finite Wilson box.  
**PROVED** (10)–(11) bound the retained electric response by the positive, energy-weighted change of its spin probabilities. In the four-dimensional electric-only SU(2) comparison purity tends to one while (E1) fails throughout every late cold window.  
The necessary weighted field estimates for interacting four-dimensional SU(2) and their separation from five-dimensional SU(2) remain open. This gives neither (E1) nor its refutation for the isotropic Wilson action, and establishes no seed or mass gap.
