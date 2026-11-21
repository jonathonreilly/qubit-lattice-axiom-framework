# Four-dimensional clustering and the vacuum space
Provenance: Codex (GPT-6; exact runtime variant unavailable), max effort requested (runtime setting unavailable); checkout `94ef5f4b8ae4f2a20d90cf29d7599fc7f4fcff93`; Sussman–Alpoge commit `31a47c543775`. Research text, not an audit; grants no status.

## 1. Sources and premises

Credit throughout: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. SA denotes their [YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex). Y3 denotes their [YM3_I manuscript](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex). Both sources have the commit above. The arguments below rebuild the specified steps by hand.

This addresses queue row 184 and skeleton nodes S12–S14. It uses **S1g**, the Result of `am1-port.md`, as an input. Every periodic Wilson DLR state on \(a\mathbb Z^4\) is translation and \(W_4\) invariant. It is reflection positive on bounded Borel functions of either closed coordinate or diagonal half-space. That input is a research proof, not independently checked here.

The continuum passage assumes **S3** (SA 4179–4194, 4541–4564). For a common centering state \(\nu_j\), write \(Z_j(f)=\mathcal O_j(f)-\nu_j(\mathcal O_j(f))\). Uniformly over periodic states \(\rho\), spacings and test positions,
\[
 |\rho Z_j(f)|\le C_1(R)\|f\|_\sharp,\qquad
 |\kappa_n^\rho(Z_j(f_1),\ldots,Z_j(f_n))|
 \le C_n(\delta;R)\prod_i\|f_i\|_\sharp\quad(n\ge2).
\tag{1}
\]
Each support lies in a radius-\(R\) ball; distinct supports have distance at least \(\delta>0\). The same bounds hold for separated reflected copies. S3 is a named premise, not proved here. No bound on an individual uncentered mean is assumed.

Here \(\mathcal O_j(f)=\sum_p f(x(p))a_p\), where \(a_p=1-\tfrac12\operatorname{tr}U_p\) and \(x(p)\) is the plaquette barycenter. There is one term per unoriented plaquette.

## 2. Transfer operators and their carrier

Sources: Y3 77017–77207; SA 3259–3427. Let \(\nu\) be any translation-invariant lattice law with S1g's mirror properties. Sections 2–5 do not use DLR. Set \(a=1\) until Section 5. In coordinate picture \(\mu\), complete the bounded local positive-half functions for
\[
 \langle[F],[G]\rangle_\mu=\nu(\overline{\theta_\mu F}G).
\]
S1g gives positivity and reflection invariance. Thus \(\|[F]\|\le\|F\|_2\le\|F\|_\infty\). Normal translation is symmetric. Iterated Cauchy–Schwarz gives
\[
 \|[\tau_{e_\mu}F]\|
 \le\|[F]\|^{1-2^{-k}}\|[\tau_{2^ke_\mu}F]\|^{2^{-k}}
 \le\|[F]\|^{1-2^{-k}}\|F\|_\infty^{2^{-k}}.
\]
Let \(k\to\infty\). Translation preserves null vectors and defines a self-adjoint contraction \(T_\mu\). RP at \(x_\mu=-1/2\) gives \(T_\mu\ge0\). Tangential translations preserve the form and have inverses. They define commuting unitaries \(U_{\mu,\lambda}\), also commuting with \(T_\mu\). Hence
\[
 \langle[F],T_\mu^sU_\mu^w[G]\rangle
 =\nu(\overline{\theta_\mu F}\tau_{se_\mu+w}G),\qquad s\ge0.
\tag{2}
\]
The joint spectral theorem applies to these bounded commuting normal operators. Write their variables as \(t=e^{-E}\in[0,1]\) and \(e^{i\eta_\lambda}\), with principal angles \(\eta\in(-\pi,\pi]^3\). The value \(t=0\) means \(E=\infty\).

**Disc lemma.** If a finite positive measure \(m\) on the closed unit disc satisfies
\[
 \int|p|^2\,dm\le C_0\sup_{[0,1]}|p|\sup_{|z|=1}|p|
\tag{3}
\]
for every polynomial, then \(m\{|1+z|^2<4|z|\}=0\). Set
\[
 L(\zeta)=\operatorname{Log}\frac{1+\zeta}{1-\zeta},\quad
 g_s(z)=\cos(sL(\sqrt z)),\quad \varphi(z)=|\operatorname{Im}L(\sqrt z)|.
\]
The Cayley transform has positive real part. Thus \(L\) is holomorphic and odd, with \(\varphi<\pi/2\). Evenness of cosine removes the square-root choice. Apply (3) to Taylor approximations of \(g_s(qz)\), \(0<q<1\). Its modulus is at most one on \([0,1]\) and at most \(\cosh(s\pi/2)\) on the disc. Since \(|\cos(u+iv)|^2\ge\sinh^2v\), Fatou as \(q\uparrow1\) gives
\[
 \int\sinh^2(s\widetilde\varphi)\,dm\le C_0\cosh(s\pi/2).
\]
The radial values are \(\widetilde\varphi=\pi/2\) on the circle except at \(1\), where we set zero. Letting \(s\to\infty\) excludes \(\widetilde\varphi\ge\pi/4+\epsilon\) for each \(\epsilon>0\). For \(z=\zeta^2\) inside the disc,
\[
 \tan\varphi=\frac{2|\operatorname{Im}\zeta|}{1-|\zeta|^2},\qquad
 |1+\zeta^2|^2-4|\zeta|^2=(1-|\zeta|^2)^2-4(\operatorname{Im}\zeta)^2.
\]
These identities identify the excluded set. On the circle it consists of every point except \(1\). This proves the lemma.

Fix \(\lambda\ne\mu\) and a local positive-half function \(F\). Choose an integer \(R\ge1\) with \(0\le x_\mu\le R\), \(|x_\lambda|\le R\) on its support. Let \(\theta'\) reflect at \(x_\mu+x_\lambda=R\). Both \(B=\theta'\theta_\mu F\) and \(F_0=\tau_{2Re_\mu}F\) lie above this diagonal mirror. In its reflection space, translation by \(d_+=e_\mu+e_\lambda\) gives a positive contraction \(T_+\). Translation by \(d_-=e_\mu-e_\lambda\) gives a unitary \(V_-\). The preceding construction applies; positivity uses the parallel mirror one height unit behind. Equation (2) in the two pictures gives
\[
 \langle[F],T_\mu^{2R+k+l}U_{\mu,\lambda}^{k-l}[F]\rangle
 =\langle[B]',T_+^kV_-^l[F_0]'\rangle,\qquad k,l\ge0.
\]
Both sides have displacement \(2Re_\mu+kd_++ld_-\). Push \(t^{2R}d\langle[F],\mathsf E_\mu[F]\rangle\) forward by \(z=te^{i\eta_\lambda}\). Polynomial expansion makes the left side of (3) equal to
\[
 \langle[B]',p(T_+)\overline p(V_-)[F_0]'\rangle,
\]
where the bar conjugates coefficients. The operator norm bound proves (3). Since \(t^{2R}>0\) for \(t>0\), the disc lemma and density of local classes imply
\[
 (1-t)^2\ge t|1-e^{i\eta_\lambda}|^2,\qquad
 \cosh E+\cos\eta_\lambda\ge2,\qquad
 E\ge\kappa|\eta|_\infty,\quad
 \kappa=\frac2\pi\log(1+\sqrt2).
\tag{4}
\]
Indeed, \(E\ge2\operatorname{arsinh}\sin(|\eta_\lambda|/2)\). The derivative of this last function is \(\cos(u/2)/\sqrt{1+\sin^2(u/2)}\), decreasing on \([0,\pi]\). Its graph lies above its endpoint chord. Intersect the three tangential carriers. At \(t=0\) the operator inequality holds without a restriction on momentum.

This comparison takes place in one coordinate plane. Changing dimension only adds the third tangential direction.

## 3. Identification of the plateau

Sources: Y3 77208–77294; SA 3429–3474. Let \(\Pi_\mu=1_{\{E=0\}}\). Spectral convergence gives \(T_\mu^s\to\Pi_\mu\). Equation (4) gives \(U_\mu^w\Pi_\mu=\Pi_\mu\). Let \(P_\mu\) condition on the completed invariant field \(\mathcal I_\mu\) of the single normal translation. Cesaro averaging (2) gives
\[
 \langle[F],\Pi_\mu[G]\rangle=\langle\theta_\mu F,P_\mu G\rangle_{L^2(\nu)}.
\tag{5}
\]
For completeness, split \(L^2\) into fixed vectors and the closure of \((1-\tau_{e_\mu})L^2\). Cesaro averages vanish on the second space by telescoping and contraction. This proves the mean ergodic step.

Reflection is a unitary involution on \(L^2(\mathcal I_\mu)\). Approximate any vector there by bounded local functions, then translate those approximants into the positive half. Their errors stay unchanged. RP and \(L^2\) convergence imply \(\langle\theta_\mu J,J\rangle\ge0\) on this invariant space. A positive involution has zero negative eigenspace, so it is the identity. Equation (5) therefore equals \(\langle P_\mu F,P_\mu G\rangle\).

Thus \(\Pi_\mu[F]\mapsto P_\mu F\) extends to an isometry onto \(L^2(\mathcal I_\mu)\). Its range is dense by the shifted local approximations just used. It intertwines tangential translations, which act trivially on \(\Pi_\mu\). Hence \(\mathcal I_\mu=\mathcal I\) modulo null sets, where \(\mathcal I\) is invariant under all translations. Therefore
\[
 \langle[F],\Pi_\mu[G]\rangle
 =\nu\bigl(\overline{E[F\mid\mathcal I]}E[G\mid\mathcal I]\bigr).
\tag{6}
\]
Conditional expectation here is unchanged by translations or coordinate reflections. This proof is independent of dimension.

## 4. The positive filter and momentum density

Sources: Y3 77295–77466; SA 3476–3648. For \(Q_r=[-r,r]^4\), \(r\in\mathbb N\), \(r\ge1\), set
\[
 \Phi_A^\mu=[\tau_{re_\mu}A]_\mu,\qquad
 \mathcal N_r(A)=\max_{1\le\mu\le4,\ \gamma\in\Gamma_{16}}\|\Phi_{\gamma A}^\mu\|^2.
\tag{7}
\]
Here \(\Gamma_{16}\) consists of coordinate sign changes. Translation invariance gives
\(\|\Phi_A^\mu\|^2=\nu(\overline{\theta_\mu A}\tau_{2re_\mu}A)\).
Thus \(\mathcal N_r^{1/2}\) is a sign-invariant seminorm bounded by \(\|\cdot\|_\infty\).

Use the periodic triangle \(b(u)=8(1-4|u|/\pi)_+\) on \([-\pi,\pi]\). Convolving two interval indicators gives its Fourier coefficients
\[
 b_0=1,\qquad b_m=\left(\frac{\sin(m\pi/8)}{m\pi/8}\right)^2.
\]
Let \(z_m\) be the even period-four sequence \((0,1,-2,1)\), and define
\[
 q(u)=\sum_{m\in\mathbb Z}z_mb_me^{imu},\qquad
 \Psi(t)=2\sum_{m\ge1}z_mb_mt^{m-1}.
\]
Both series converge absolutely. Since \(|z_m|=1-\cos(m\pi/2)\), their absolute coefficient sum is \(b(0)-b(\pi/2)=8\). Also
\[
 q(u)=\tfrac12b(u+\pi/2)+\tfrac12b(u-\pi/2)-b(u+\pi).
\]
Consequently \(q(u)=0\) for \(\operatorname{dist}(u,2\pi\mathbb Z)\le\pi/4\), and \(\Psi(1)=q(0)=0\).

The required lower bound is
\[
 0\le\Psi\le8,\qquad
 \Psi(e^{-x})\ge c_\Psi\tanh x\ (x>0),\qquad
 c_\Psi=(1+\sqrt2)^{-1}.
\tag{8}
\]
To prove it, use the Poisson kernel \(P_t(u)=(1-t^2)/(1-2t\cos u+t^2)\). Its geometric series and \(z_0=0\) give
\[
 t\Psi(t)=\frac1{2\pi}\int b(v)
 [\tfrac12P_t(v-\pi/2)+\tfrac12P_t(v+\pi/2)-P_t(v-\pi)]\,dv .
\]
On the support of \(b\), \(\cos v\ge1/\sqrt2\). With \(s=1+t^2\), the bracket is at least
\[
 (1-t^2)\left(\frac1s-\frac1{s+\sqrt2t}\right).
\]
Indeed, the average of \((s\pm2t\sin v)^{-1}\) is at least \(1/s\). Since \(b\) has mean one,
\[
 \Psi(t)\ge\frac{1-t^2}{1+t^2}\frac{\sqrt2}{1+t^2+\sqrt2t}
 \ge c_\Psi\frac{1-t^2}{1+t^2}.
\]
The upper bound follows from the absolute coefficient sum. The endpoint is \(\Psi(0)=2b_1>0\). This proves (8) without numerical evaluation.

First take \(\theta_\mu A=\epsilon A\), \(\epsilon=\pm1\), and let \(\Phi=\Phi_A^\mu\). For tangential \(w\in\mathbb Z^3\), put
\[
 g(s,w)=\epsilon\nu(\overline A\tau_{se_\mu+w}A),\qquad
 K(w)=\sum_m z_mb_mg(2rm,w).
\]
Reflection and translation give \(g(-s,w)=g(s,w)\) and \(g(s,-w)=\overline{g(s,w)}\). For \(s\ge2r\), (2) gives \(g(s,w)=\langle\Phi,T_\mu^{s-2r}U_\mu^w\Phi\rangle\). Pairing \(m,-m\), with \(z_0=0\), yields
\[
 K(w)=\langle\Phi,\Psi(T_\mu^{2r})U_\mu^w\Phi\rangle
      =\int e^{i\eta\cdot w}\,dM_A(\eta),\qquad |K(w)|\le8\mathcal N_r(A).
\tag{9}
\]
Here \(M_A\) is the momentum image of the **positive** measure
\(\Psi(e^{-2rE})\,d\langle\Phi,\mathsf E_\mu(E,\eta)\Phi\rangle\).

If \(|w|_\infty\ge2r\), choose a maximal tangential coordinate \(\lambda\). Conjugating allows \(w_\lambda>0\). In picture \(\lambda\), (2) instead writes \(g(s,w)\) as
\[
 \epsilon\langle\Phi_{\theta_\lambda A}^{\lambda},
 T_\lambda^{w_\lambda-2r}U_{\lambda,\mu}^{s}
 \prod_{\lambda'\ne\lambda,\mu}U_{\lambda,\lambda'}^{w_{\lambda'}}
 \Phi_A^\lambda\rangle .
\]
Summing in \(s=2rm\) inserts \(q(2r\eta'_\mu)\). Nonzero values require \(|\eta'_\mu|>\pi/(8r)\); other periodic copies of the zero set do not weaken this implication. The carrier (4) therefore gives, with \(c=\kappa\pi/8\),
\[
 |K(w)|\le8\mathcal N_r(A)e^{-c(|w|_\infty-2r)/r}.
\tag{10}
\]
There are at most \(64r^3\) interior points and exactly \(24k^2+2\) points on the shell \(|w|_\infty=k\), \(k\ge1\). For \(h=c/r\),
\[
 \sum_{j\ge0}e^{-hj}\le1+h^{-1},\qquad
 \sum_{j\ge0}j^2e^{-hj}\le
 \int_0^\infty(x+1)^2e^{-hx}\,dx=2h^{-3}+2h^{-2}+h^{-1}.
\]
Use \(k=2r+j\) in (10). These inequalities give \(\sum_w|K(w)|\le Cr^3\mathcal N_r(A)\). All constants \(C\) hereafter are numerical consequences of \(c,c_\Psi\) and these displayed bounds.

Thus the absolutely convergent Fourier series
\[
 h_A(\eta)=(2\pi)^{-3}\sum_wK(w)e^{-i\eta\cdot w}
\]
is continuous and bounded by \(Cr^3\mathcal N_r(A)\). Its measure and \(M_A\) have the same Fourier coefficients. Trigonometric polynomials are dense in continuous torus functions, so these measures agree. Positivity gives
\[
 M_A=h_A(\eta)\,d\eta,\qquad 0\le h_A\le Cr^3\mathcal N_r(A).
\tag{11}
\]
This is a weighted density, not a density assumption on the original spectral measure. In \(d=3\) the tangential shells have \(8k\) points and give \(Cr^2\). Equation (11) is the first dimensional change in the estimate.

## 5. PL3, IV-31-51, and closedness

Sources: Y3 77470–77560; SA 3650–3750. The density in (11) has no atom at \(\eta=0\). By (8), the original spectral measure therefore has no mass at \(0<E<\infty,\eta=0\). The weight is zero at \(E=0\), so this conclusion removes no plateau. Energy infinity contributes zero to \(T_\mu^n\), \(n\ge1\).

The function \(e^{-nE}/\tanh(2rE)\) decreases for \(E>0\). Using (4), (8), (11), and \(\coth u\le1+1/u\), we obtain
\[
 \begin{aligned}
 \langle\Phi,T_\mu^n(1-\Pi_\mu)\Phi\rangle
 &\le Cr^3\mathcal N_r(A)\int_{\mathbb T^3}
   \frac{e^{-n\kappa|\eta|_\infty}}{\tanh(2r\kappa|\eta|_\infty)}\,d\eta\\
 &\le Cr^3\mathcal N_r(A)\int_0^\infty
   u^2e^{-n\kappa u}(1+(2r\kappa u)^{-1})\,du\\
 &\le C\mathcal N_r(A)[(r/n)^3+(r/n)^2].
 \end{aligned}
\tag{12}
\]
The cube shell volume is \(24u^2du\). The two integrals are \(2/(n\kappa)^3\) and \(1/(n\kappa)^2\), by integration by parts. This replaces the \(d=3\) shell \(8u\,du\), and changes the leading power from \(r/n\) to \((r/n)^2\).

For arbitrary complex \(A\), split \(A=A_++A_-\), \(A_\pm=(A\pm\theta_\mu A)/2\). The seminorm gives \(\mathcal N_r(A_\pm)\le\mathcal N_r(A)\). Positivity of \(D_n=T_\mu^n(1-\Pi_\mu)\) gives its quadratic form on a sum at most twice the sum of the two forms. Thus (12) holds for every \(A\), after increasing \(C\).

Choose \(y_\mu=|y|_\infty>0\), and \(n=|y|_\infty-2r\ge1\). The cube identity is
\[
 \nu(\overline A\tau_yB)=
 \langle\Phi_{\theta_\mu A}^\mu,T_\mu^nU_\mu^{y_\perp}\Phi_B^\mu\rangle.
\]
Equation (6) identifies its \(\Pi_\mu\) term. Cauchy–Schwarz for \(D_n\), commuting with \(U_\mu^{y_\perp}\), bounds the remainder by (12). A negative maximal coordinate follows by conjugating and exchanging \(A,B\). Restoring spacing \(a\) gives precisely
\[
 \boxed{\;
 |\nu(\overline A\tau_yB)-\operatorname{Pl}_\nu(A,B)|
 \le C[(r/n)^2+(r/n)^3]\mathcal N_r(A)^{1/2}\mathcal N_r(B)^{1/2},
 \quad n=|y|_\infty/a-2r\ge1 ,
 \;}
\tag{PL3}
\]
where \(A,B\) use bonds in \(a[-r,r]^4\), and
\(\operatorname{Pl}_\nu(A,B)=\nu(\overline{E[A\mid\mathcal I]}E[B\mid\mathcal I])\).
At spacing \(a\), definition (7) uses \(\Phi_A^\mu=[\tau_{rae_\mu}A]_\mu\), and its reflection moments have shift \(2rae_\mu\).
The constant is independent of \(a,\beta,\nu,r\). If \(|y|_2\ge8ra\), then \(|y|_\infty\ge|y|_2/2\ge4ra\). Hence the right side is at most
\[
 C(ra/|y|_2)^2\mathcal N_r(A)^{1/2}\mathcal N_r(B)^{1/2}.
\tag{13}
\]
This is IV-31-51 in four dimensions. The Euclidean threshold changes from \(4\sqrt3\,ra\) to \(8ra\). For ergodic \(\nu\), the plateau is \(\overline{\nu(A)}\nu(B)\). S3 was not used.

At fixed spacing the invariant RP class is weakly closed. Continuous local positivity inequalities pass to a weak limit, as does reflection invariance. Continuous half-space cylinder functions are dense in the corresponding \(L^2\) space. Ordinary Cauchy–Schwarz therefore extends RP to bounded Borel half-space functions.

Its ergodic subset is also closed. If ergodic \(\nu_j\to\nu\), pass PL3 for continuous local \(A,B\) to the limit, bounding \(\mathcal N_r\) by supremum norms. The limit still clusters to \(\overline{\nu(A)}\nu(B)\). Cesaro averages along \(ke_\mu\), with \(A=B\), give
\(\|E_\nu[A\mid\mathcal I_\mu]\|_2^2=|\nu(A)|^2\).
This conditional expectation is therefore constant. Density of continuous local functions makes \(\mathcal I_\mu\), hence \(\mathcal I\), trivial. No assumption of closedness of extreme states entered the proof.

## 6. Conditional kernels on compact spaces

Source: SA 30875–31135; compare Y3 79627–79708. Let \(K\) be compact metric, \(\mu\) a Borel probability, and \(\mathcal H\) a sigma-field satisfying
\[
 \mathcal N_\mu\subset\mathcal H\subset\overline{\mathcal B(K)}_\mu .
\]
Here \(\mathcal N_\mu\) denotes all subsets of Borel \(\mu\)-null sets.
There is a Borel, \(\mathcal H\)-measurable map \(k:K\to\mathcal P(K)\) such that
\[
 kf=E_\mu[f\mid\mathcal H]\quad\mu\text{-a.s.}
\tag{14}
\]
for each bounded Borel \(f\). Two such probability-valued maps agree off one Borel null set.

Here is the construction. Distances to a countable dense set generate a countable rational unital algebra and lattice \(D\subset C(K;\mathbb R)\). It separates points, so Stone–Weierstrass makes it uniformly dense. Project each \(f\in D\) onto \(L^2(\mathcal H,\mu)\). Testing against \(1_H\), \(H\in\mathcal H\), gives the defining conditional integral identity, positivity, and the supremum norm bound. Choose Borel representatives: replace each rational level set by a Borel set modulo a Borel null set. Such replacement preserves \(\mathcal H\)-measurability because \(\mathcal H\) contains all null subsets.

Outside one Borel null set, the countably many representatives preserve \(1\), rational linear relations, and positivity on every nonnegative member of \(D\). At each remaining point \(x\), they define a positive unital rational-linear functional \(L_x\). For rational \(r>\|f\|_\infty\), positivity of \(r\pm f\) gives \(|L_x(f)|\le r\). Uniform extension gives a positive real-linear functional on \(C(K)\). Riesz representation supplies \(k(x)\in\mathcal P(K)\). On the exceptional set choose one fixed point mass.

The coordinate map \(\rho\mapsto(\rho(f))_{f\in D}\) embeds \(\mathcal P(K)\) in a countable product. Its image is compact: any coordinate-convergent subsequence extends to a positive unital functional and hence a probability by the same argument. Uniform density identifies its coordinate topology with the weak topology. The inverse on the compact image is continuous. Therefore the constructed \(k\) is both Borel and \(\mathcal H\)-measurable as a probability-valued map.

Uniform approximation proves (14) for continuous functions. The functions satisfying its integral identity against every \(1_H\) form a vector space closed under bounded increasing limits. The functional monotone-class theorem extends (14) to all bounded Borel functions, since continuous functions generate the Borel field. Finally, uniqueness of conditional expectations on the countable set \(D\) gives equality of two kernels on all continuous functions simultaneously. Riesz uniqueness gives equality of their probability measures off one null set.

This does not assert pointwise properness on every conditioning event. Nor does it select a universal version for an uncountable family of preassigned conditional expectations. The kernel, its barycenter, and its law are unambiguous modulo null sets. This construction has no dimension-dependent step.

## 7. Fixed-spacing DLR decomposition

Sources: SA 31180–31245; Y3 79580–79749. Put \(\Omega_a=\mathrm{SU}(2)^{\mathcal B_a}\). Let \(\mathcal G_{a,\beta}\) contain all translation-invariant Wilson DLR states, with kernels \(\gamma_W\) for finite bond sets \(W\). The kernels integrate finite Haar products against their normalized positive Wilson density. They preserve continuous local functions and have supremum norm at most one.

The countable product \(\Omega_a\) is compact metric. Invariance and DLR are closed affine equations on its probability measures. Cubic torus laws have weak limit points. Each finite DLR equation holds once its interaction neighbourhood embeds without wrapping, and passes to such a limit. Thus \(\mathcal G_{a,\beta}\) is nonempty compact convex. S1g gives its mirror properties.

**Invariant densities preserve DLR.** For bounded invariant \(h\), approximate \(h\) in \(L^1(\nu)\) by bounded continuous local \(h_m\). Translate \(h_m\) so its bond support misses \(W\). Translation invariance preserves the approximation error, and DLR gives
\[
 \nu(h_m\gamma_WF)=\nu(\gamma_W(h_mF))=\nu(h_mF).
\]
Each replacement error is at most \(\|h-h_m\|_1\|F\|_\infty\). Hence \(\nu(h\gamma_WF)=\nu(hF)\). For \(h\ge0\), \(\nu(h)>0\), the normalized law \(h\nu/\nu(h)\) belongs to \(\mathcal G_{a,\beta}\).

Apply Section 6 to the completed translation-invariant field \(\mathcal I\). Write \(\nu^\omega(F)=E_\nu[F\mid\mathcal I](\omega)\). Testing the preceding identity with \(h=1_I\), \(I\in\mathcal I\), gives
\[
 \nu^\omega(\gamma_WF)=\nu^\omega(F),\qquad
 \nu^\omega(\tau_vF)=\nu^\omega(F)
\]
almost surely. Impose these equations on one countable dense family of continuous local functions, all finite \(W\), and all translations \(v\). A single null set suffices. Uniform approximation and contraction of \(\gamma_W\) extend the equations to all continuous tests. The monotone-class theorem extends them to bounded Borel tests. Thus \(\nu^\omega\in\mathcal G_{a,\beta}\) almost surely, and S1g applies to it.

PL3 proves these conditional laws ergodic. For continuous local \(A\), integrate the limit along \(ke_\mu\):
\[
 \int\operatorname{Pl}_{\nu^\omega}(A,A)\,d\nu(\omega)
 =\operatorname{Pl}_\nu(A,A)
 =\int|\nu^\omega(A)|^2\,d\nu(\omega).
\tag{15}
\]
The limits are bounded by \(\|A\|_\infty^2\), so dominated convergence applies. For each conditional state the difference between the two integrands is nonnegative. It is the variance of its own invariant conditional expectation of \(A\). Thus it vanishes almost surely. Impose this on a countable dense local family; density in each \(L^2(\nu^\omega)\) makes its invariant subspace constant.

Let \(\mathcal E_{a,\beta}\) be the ergodic states. They are precisely the extreme points of \(\mathcal G_{a,\beta}\). A nontrivial invariant event gives a nontrivial convex decomposition by the invariant-density argument. Conversely, densities of summands in a convex decomposition are bounded and invariant. Ergodicity makes them constant, so both summands equal the original state. Section 5 makes \(\mathcal E_{a,\beta}\) closed, hence compact.

The law \(D_\nu=(\omega\mapsto\nu^\omega)_*\nu\) is supported on \(\mathcal E_{a,\beta}\) and has barycenter \(\nu\). It is the unique such law. Indeed, for any law on \(\mathcal E_{a,\beta}\), PL3 identifies every mixed moment of local state evaluations with successive far-translation limits of its barycenter. Each step separates one factor from the fixed remaining product; the error tends to zero uniformly over states. Evaluations of continuous local functions separate this compact state space. Their polynomial algebra is uniformly dense by Stone–Weierstrass, so equal mixed moments give equal laws. This includes uniqueness independently of the conditional-kernel version.

No part of Sections 6–7 depends on the number of lattice directions. Dimension enters through S1g and the already proved uniform decay.

## 8. Canonical continuum components, conditional on S3

Sources: SA 31142–31178, 31247–31378; Y3 77560–78231. Let \(a_j\downarrow0\), with couplings for which S3 holds. Keep the same centering laws \(\nu_j\) throughout. For a separated tuple \(F=(f_1,\ldots,f_k)\), put \(F_j=\prod_i Z_j(f_i)\); the empty tuple gives \(1\). Tests are real \(C_c^1(\mathbb R^4)\), and
\(\|f\|_\sharp=\max(\|f\|_\infty,c_M\|\nabla f\|_\infty)\), with fixed \(c_M>0\).

**Uniform moments.** Set \(b_1=C_1(R)\), \(b_m=C_m(\delta;R)\) for \(m\ge2\), and
\[
 M_k(\delta;R)=\sum_{\pi\in\operatorname{Part}(\{1,\ldots,k\})}
                  \prod_{J\in\pi}b_{|J|},\qquad M_0=1.
\]
Differentiating the exponential of the cumulant generating function once in each variable gives this partition formula. Singleton factors are differences of means; larger factors are unchanged by centering. Thus S3 gives, uniformly over \(\rho\in\mathcal G_{a_j,\beta_j}\),
\[
 |\rho(F_j)|\le B(F):=M_k(\delta;R)\prod_i\|f_i\|_\sharp .
\tag{16}
\]
Telescoping two products, with corresponding supports in fixed separated containers, gives
\[
 |\rho(F_j-F'_j)|
 \le M_k(\delta;R)\sum_i\|f_i-f'_i\|_\sharp
                 \prod_{l\ne i}\max(\|f_l\|_\sharp,\|f'_l\|_\sharp).
\tag{17}
\]
These arguments use only bounded variables at each fixed spacing. Put \(\delta(F)=\infty\) for tuples of length at most one, and \(B(\varnothing)=1\).

**Uniform clustering before taking a limit.** Choose a physical cube \((-R_0,R_0)^4\) containing \(F,G\), with positive margin \(\epsilon\). Set \(r_j=\lceil R_0/a_j\rceil\). For sufficiently fine spacing, all plaquette bonds used by \(F_j,G_j\) lie in \(a_j[-r_j,r_j]^4\). A plaquette endpoint is within \(a_j/2\) in supremum norm of its barycenter.

Every expression in \(\mathcal N_{r_j}(F_j)\) consists of two reflected copies of \(F\), separated by at least \(2\epsilon\). Equation (16), at order \(2k\) and separation \(\min(\delta(F),2\epsilon)\), bounds it by a constant \(N(F;R_0)\). This constant is independent of \(j,\rho\). S1g ensures covariance also for the common centering. Hence (13) gives, for every pure lattice state \(\rho\),
\[
 |\rho(F_j\,\tau_{v_j}G_j)-\rho(F_j)\rho(G_j)|
 \le C(F,G)|v_j|_2^{-2}
\tag{18}
\]
once \(|v_j|_2\) exceeds a fixed physical threshold. The constants are uniform in \(j,\rho\). Here \(r_ja_j\le R_0+a_j\), so the lattice-to-physical conversion is uniform. Supremum norms of \(F_j\) do not enter.

**Countable coordinates and existence.** Take finite unions \(Q\) of rational closed boxes. The \(C^1\) functions supported in \(Q\) form a separable space: embed them by their value and four derivatives in \(C(Q)^5\). Choose a countable dense set in each such space, and all separated tuples from their union. Call the resulting family \(\mathfrak F\). Any separated tuple can be approximated in fixed separated containers: enclose each support in rational boxes inside those containers, then use the corresponding dense set.

Diagonal extraction using (16), followed by (17), gives a subsequence with \(\nu_j(F_j)\to\sigma(F)\) for every separated tuple. From now on use any such converging sequence. Set
\[
 \mathsf K=\prod_{F\in\mathfrak F}[-B(F),B(F)],\quad
 e_j(\rho)=(\rho(F_j))_F,\quad
 \lambda_j=(e_j)_*D_{\nu_j}.
\]
Each \(e_j\) is continuous on the compact pure-state space from Section 7. Thus \(\lambda_j\) is a probability on compact metric \(\mathsf K\).

All its mixed coordinate moments converge along this full converging sequence. To see this, fix \(F^1,\ldots,F^q\) and an error tolerance. Choose \(v_q\) first, then \(v_{q-1},\ldots,v_2\). At each choice, separate the new tuple from the fixed remaining union. Equation (18) then compares
\[
 \rho(F^1_j\,\tau_{v_{2,j}}F^2_j\cdots\tau_{v_{q,j}}F^q_j)
 \quad\text{with}\quad \prod_i\rho(F^i_j)
\]
within that tolerance, uniformly over pure \(\rho\) and sufficiently large \(j\). Errors are multiplied only by the bounds (16). Constants may depend on already fixed outer translations. Choose each new distance after those constants are fixed. Round each physical translation to \(a_j\mathbb Z^4\). Equation (17) makes the rounding error tend to zero, since \(C^1\) translation is continuous in \(\|\cdot\|_\sharp\).

Integrate over \(D_{\nu_j}\). The first expression becomes a moment of \(\nu_j\), which converges at this fixed configuration. The mixed coordinate moments are therefore Cauchy. Coordinate polynomials separate \(\mathsf K\) and contain constants. Stone–Weierstrass and compactness now give one weak limit \(\lambda\), along the full sequence.

**Every support point is a component.** Put \(X=\operatorname{supp}\lambda\). For \(\xi\in X\), each finite-coordinate open neighbourhood has positive \(\lambda\) measure. Weak convergence gives positive \(\lambda_j\) measure eventually. Along a shrinking countable neighbourhood base choose pure states \(\rho_j\) with \(e_j(\rho_j)\to\xi\). This can be done for all sufficiently large \(j\), by keeping each neighbourhood until the next one is available. Equation (17) extends convergence to every tuple:
\[
 \sigma_\xi(F)=\lim_j\rho_j(F_j).
\]
The same bound makes this limit independent of those choices. It approximates each evaluation uniformly in \(\xi\) by coordinate evaluations. Therefore \(f_F(\xi):=\sigma_\xi(F)\) is continuous, and the evaluations separate points of \(X\).

Barycenters give \(\sigma(F)=\int_X\sigma_\xi(F)\,d\lambda(\xi)\). Bounds (16)–(17), multilinearity, reality, and symmetry pass to every component. Cumulants are finite polynomials in subtuple moments, so the S3 cumulant bounds pass too. Translation invariance and \(W_4\) invariance pass by rounding and (17). Coordinate and diagonal RP pass on each finite Gram matrix: place all positive-half supports strictly inside that half, choose admissible lattice mirrors approaching the continuum mirror, and pass each separated reflected moment to the limit. Reflection invariance passes by the same moving-test argument. No new moment at coincident supports is used.

Passing (18) to these pure-state limits gives
\[
 \boxed{\quad
 \sup_{\xi\in X}|\sigma_\xi(F\,\tau_vG)-\sigma_\xi(F)\sigma_\xi(G)|
 \le C(F,G)|v|_2^{-2}
 \quad}
\tag{19}
\]
for all sufficiently large real \(v\). Rounding and (17) justify arbitrary real translations. The distance threshold and constant are independent of \(\xi\).

**Intrinsic moments and uniqueness.** Uniform clustering now gives
\[
 \int_X\prod_{i=1}^q\sigma_\xi(F^i)\,d\lambda(\xi)
 =\lim_{|v_q|\to\infty}\cdots\lim_{|v_2|\to\infty}
   \sigma(F^1\,\tau_{v_2}F^2\cdots\tau_{v_q}F^q).
\tag{20}
\]
Take the innermost limit first. With the later translations fixed, (19) separates \(F^2\) from their union. Equation (16) permits the limit through the integral. Repeat for \(F^3,\ldots,F^q\). This proves existence of each intermediate limit; it asserts no unrestricted simultaneous limit.

For another compact full-support representation with continuous point-separating evaluations and (20), embed both spaces by all tuple evaluations. Their images are compact in the same Hausdorff product. Coordinate polynomials separate their compact union. Equation (20) and Stone–Weierstrass give equal image measures. Full support makes each image the support of its measure. The images coincide, so the embeddings give a unique measure-preserving homeomorphism preserving all evaluations. This is the canonical decomposition.

Common centering is retained: \(\sigma(f)=0\), while individual \(\sigma_\xi(f)\) can differ. The extra dimension changes \(C(Q)^4\) to \(C(Q)^5\), the lattice symmetry group to \(W_4\), and the decay in (18). The compactness and uniqueness arguments otherwise do not change.

## 9. PV4: the zero-energy space

Sources: SA 31380–31508; Y3 78232–78324, Theorem IV-36-25. The Hilbert space here is generated by separated tuples strictly inside \(x_4>0\). This specifies the density hypothesis needed for PV4.

First construct its time evolution. For complex finite sums of such tuples, use
\[
 \langle[F],[G]\rangle=\sigma(\overline{\theta F}\,G),\qquad \theta:x_4\mapsto-x_4.
\]
Every matrix entry is separated; the lattice RP limits of Section 8 make this form positive. Quotient its null space and complete. On representatives put \(T_t[F]=[\tau_{te_4}F]\), \(t\ge0\). Translation invariance makes this map symmetric in the form. Moreover
\[
 \langle[F],T_t[F]\rangle=\|[\tau_{te_4/2}F]\|^2\ge0.
\]
For each fixed finite sum \(F\), (16) bounds \(\|[\tau_{se_4}F]\|\) uniformly for \(s\ge0\). Internal separations remain fixed, and the reflected halves only move farther apart. The iterated Cauchy–Schwarz argument of Section 2 therefore proves contraction and preservation of null vectors. The resulting \(T_t\) are commuting positive self-adjoint contractions with \(T_{t+s}=T_tT_s\).

Equation (17) gives \(\|T_t[F]-[F]\|\to0\) as \(t\downarrow0\): expand the squared norm into three reflected moments and translate tests in fixed separated containers. Contraction extends this continuity to the completion. The operator \(T_1\) is injective. Indeed, \(T_1v=0\) implies \(T_{1/2^m}v=0\), because a positive operator and its positive integer powers have the same kernel. Strong continuity then gives \(v=0\). Functional calculus defines \(H=-\log T_1\ge0\). Uniqueness of positive roots gives \(T_t=e^{-tH}\) at rational \(t\), and continuity gives it for every \(t\ge0\). Thus
\[
 \langle[F],e^{-tH}[G]\rangle=\sigma(\overline{\theta F}\,\tau_{te_4}G).
\tag{PV3}
\]
The same construction applies to each \(\sigma_\xi\). It uses no extension to coincident supports.

Let \(P_0=1_{\{0\}}(H)\). The spectral theorem gives \(e^{-tH}\to P_0\) strongly. The barycenter identity, component reflection invariance, and (19) imply
\[
 \begin{aligned}
 \langle P_0[F],P_0[G]\rangle
 &=\lim_{t\to\infty}\int_X
       \sigma_\xi(\overline{\theta F}\,\tau_{te_4}G)\,d\lambda(\xi)\\
 &=\int_X\overline{f_F(\xi)}f_G(\xi)\,d\lambda(\xi).
 \end{aligned}
\tag{21}
\]
Uniform clustering also holds for finite sums by addition. Therefore \(P_0[F]\mapsto f_F\) is well defined and isometric. These vectors are dense in \(\ker H\), since \([F]\) are dense and \(P_0\) is bounded. Its extension has closed range.

To prove surjectivity, let \(V\) be the span of \(f_F\) for positive-time tuples. It contains \(1\) and is closed under conjugation. Translating any tuple into positive time leaves its evaluation unchanged, so \(V\) separates points of \(X\). For large \(t\), \(F\,\tau_{te_4}G\) is still an admitted positive-time tuple, and (19) gives
\[
 f_{F\,\tau_{te_4}G}\longrightarrow f_Ff_G
 \quad\hbox{uniformly on }X.
\]
Thus the uniform closure of \(V\) is an algebra: extend first to finite sums, then to uniform limits using bounded approximants. Stone–Weierstrass makes this closure \(C(X)\). Continuous functions are dense in \(L^2(X,\lambda)\); hence the isometry has dense and closed range. We have proved
\[
 \boxed{\quad U:\ker H\xrightarrow{\;\cong\;}L^2(X,\lambda),
       \qquad UP_0[F]=f_F,\qquad U[1]=1.\quad}
\tag{PV4}
\]
The rule determines \(U\) uniquely. Applied to a single clustering component, (21) makes \(P_0\) the rank-one projection onto \([1]\). Thus each component has a unique vacuum in this Hilbert space.

If \(X\) has \(m<\infty\) points, full support makes all their masses positive, so \(\dim\ker H=m\). If \(X\) is infinite, arbitrarily many distinct points have disjoint open neighbourhoods of positive measure. Their indicators give arbitrarily many orthogonal vectors. Compact metrizability makes \(L^2(X,\lambda)\) separable, so its dimension is countably infinite. Neither assertion gives a spectral gap. The Hilbert argument is dimension-independent; the normal coordinate changes from \(x_3\) to \(x_4\).

## Result

Under S1g, Sections 2–7 give the four-dimensional IV-31-51, PL3, closedness of the ergodic RP class, and the unique fixed-spacing decomposition into ergodic Wilson DLR states. The lattice bound uses reflection sizes and has rate \(|v|^{-2}\), with a retained invariant plateau for mixtures.

Under the named S3 premise, Section 8 gives subsequential separated limits and their canonical compact component measure. Every component clusters at rate \(|v|^{-2}\), with common constants and common centering. Section 9 constructs the separated-tuple time semigroup and proves PV4, including a one-dimensional vacuum space in each component.

The dimensional changes are explicit in Sections 2, 4, 5, 8, and 9: three tangential variables, \(r^3\) density, cube shell \(24u^2du\), inverse-square decay, sixteen sign changes, four derivatives, and the time coordinate \(x_4\). All other steps use compactness, positivity, or Hilbert-space arguments independent of dimension.

These are research proofs by Codex, not yet checked by the other model. S1g remains an input; S3 is not discharged. This supplies conditional text for S12–S14, not an unconditional Yang–Mills existence theorem, full \(O(4)\) invariance, factorial growth, or a mass gap. No computation discharged a step. No status is granted.
