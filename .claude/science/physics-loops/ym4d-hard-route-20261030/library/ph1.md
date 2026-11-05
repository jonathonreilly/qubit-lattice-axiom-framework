# PH1 — Phases, components and clustering

Provenance: Codex, Phase A pass 2 (distil), 2026-11-05; source checkout a456311fd37ebcc1811c1180cff145d7d2b91570. Research text, not an audit; grants no status. Sources attributed to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, are pinned at 31a47c543775.

## Definitions and imports

This part distils `cluster-port.md`, read whole, with `gates/cluster-check.md`, read whole. The gate's Part A checked that note line by line by Claude, first failing step none, subject to its centering clarification. That check does not referee this assembled part. The target is PH1 in `ym4-assembly.md` §§4–5; `assembly-status.md` records that the part had not yet been distilled.

**Lattice definitions.** Let \(\mathcal B_a\) contain one orientation of every nearest-neighbour bond of \(a\mathbb Z^4\). Put \(\Omega_a=\mathrm{SU}(2)^{\mathcal B_a}\), with its compact product topology; reversing a bond inverts its matrix. For an unoriented plaquette \(p\), set \(a_p=1-\tfrac12\operatorname{tr}U(\partial p)\). The Wilson kernel \(\gamma_W\), for finite \(W\subset\mathcal B_a\), integrates those bonds against normalized Haar density
\[
 \exp\left[-\beta\sum_{p:p\cap W\ne\varnothing}a_p\right],\qquad \beta>0,
\]
holding the other bonds fixed. Its denominator is positive. A DLR state satisfies \(\rho\gamma_W=\rho\) for every finite \(W\). Let \(\mathcal G_{a,\beta}\) be the translation-invariant DLR class. LG1 identifies the periodic Wilson class used here with this class.

A local observable is a bounded complex Borel bond function. The algebra \(\mathfrak A(S)\) uses bonds with both endpoints in \(S\). Translations move supports by their subscript; isometries act by linear pullback, without conjugation. Write \(W_4\) for signed coordinate permutations, \(\Gamma_{16}\) for coordinate sign changes, and \(\theta_\mu\) for reflection at \(x_\mu=0\). Reflection positivity (RP) means \(\rho(\overline{\theta F}F)\ge0\) on the indicated half-space algebra. The completed invariant field \(\mathcal I\) consists of events invariant modulo \(\rho\) under every lattice translation. A lattice state is **ergodic** if \(\mathcal I\) is trivial. Here **pure** means extreme in \(\mathcal G_{a,\beta}\); Lemma 7 proves its equivalence to ergodicity. Extremality among noninvariant DLR states is not asserted.

For integer \(r\ge1\) and \(A,B\in\mathfrak A(a[-r,r]^4)\), define
\[
 \mathcal N_{\rho,r}(A)=\max_{1\le\mu\le4,\ \gamma\in\Gamma_{16}}
 \rho(\overline{\theta_\mu\gamma A}\,\tau_{2rae_\mu}\gamma A),\qquad
 \operatorname{Pl}_\rho(A,B)=\rho\bigl(\overline{E_\rho[A\mid\mathcal I]}E_\rho[B\mid\mathcal I]\bigr).
\]
In the maximum, \(\mu\in\{1,2,3,4\}\) independently of \(\gamma\). We suppress \(\rho\) in \(\mathcal N_r\) when fixed.

**Continuum definitions.** A separated tuple \(F=(f_1,\ldots,f_k)\) has real \(C_c^1(\mathbb R^4)\) entries with pairwise disjoint supports. Include the empty tuple \(1\), and use finite complex linear combinations of tuples; conjugation conjugates their coefficients. Concatenate tuples only when the resulting supports are separated. Write
\[
 \|f\|_\sharp=\max(\|f\|_\infty,c_M\|\nabla f\|_\infty),\quad
 \mathcal O_j(f)=\sum_p f(x(p))a_p,\quad
 Z_j(f)=\mathcal O_j(f)-\nu_j(\mathcal O_j(f)),\quad
 F_j=\prod_i Z_j(f_i),
\]
where \(c_M>0\) is fixed and \(x(p)\) is the plaquette barycenter. There is one summand per unoriented plaquette. A **volume-first limit** here is \(\sigma(F)=\lim_j\nu_j(F_j)\), after infinite-volume DLR states have been obtained at each spacing. The same \(\nu_j\in\mathcal G_{a_j,\beta_j}\) centers every component. This is the correction required by gate A3.

A **canonical phase representation** is a compact metrizable space \(X\), a full-support Borel probability \(\lambda\), and forms \(\sigma_\xi\) whose continuous evaluations separate points, with barycenter \(\sigma\) and mixed moments (20). Its isomorphisms preserve the measure and every evaluation. Continuum “ergodic components” means the clustering correlation forms constructed below, with a unique OS vacuum; no probability law on pointwise continuum fields is assumed. For positive-time tuples, all supports lie strictly inside \(x_4>0\). Their RP quotient completion is \(\mathcal H(\sigma)\), with \(\Omega=[1]\), time generator \(H\), and \(P_0=1_{\{0\}}(H)\).

Let \(\Delta_n=\bigcup_{i<j}\{x_i=x_j\}\). The space \(\mathcal S_{\Delta,n}\) consists of Schwartz functions flat to every order on \(\Delta_n\); use \(\mathbb C\) at \(n=0\). Its positive-time subspace is flat also on the complement of \(\{x_{i,4}>0\ \forall i\}\). Set
\[
 p_m(\varphi)=\max_{|\alpha|\le m}\sup_x(1+|x|^2)^{m/2}|\partial^\alpha\varphi(x)|.
\]

The named imports are:

- **LG1:** every periodic Wilson DLR state is invariant under all lattice translations and \(W_4\), and invariant and RP on either closed side of every coordinate site, coordinate bond and diagonal mirror. At spacing one these mirrors are \(x_\mu=c\), \(c\in\tfrac12\mathbb Z\), and \(x_\mu\pm x_\lambda=c\), \(c\in\mathbb Z\). This is S1g in the checked note. Lemmas 2–5 use only these measure properties.
- **SR1, S3:** for every \(\rho,\nu_j\in\mathcal G_{a_j,\beta_j}\), each support in its own radius-\(R\) ball, and separation at least \(\delta>0\),
  \[
  |\rho Z_j(f)|\le C_1(R)\|f\|_\sharp,\qquad
  |\kappa_n^\rho(Z_j(f_1),\ldots,Z_j(f_n))|
  \le C_n(\delta;R)\prod_i\|f_i\|_\sharp\quad(n\ge2).\tag{1}
  \]
  The cumulant is the mixed derivative at zero of the logarithm of the joint exponential moment. Constants are independent of states, cutoff and support positions, including separated reflected copies. No bound on an individual uncentered mean is used.
- **SR1(3)–(4), for growth:** the all-state graded moment bound is \(B(R)^n(n!)^k\max(1,\delta^{-5n})\prod_i\|f_i\|_\sharp\), with \(B(R)=C(R+1)^4\), \(C,C_E>0\) and fixed integer \(k\ge1\). The extension theorem for any separated limit of this class gives \(|\sigma_n(\varphi)|\le C_E^n(n!)^{k+32}p_{20n}(\varphi)\), unique diagonal-flat extensions and constrained tensor density, also at the time boundary. S3 alone does not give this conclusion.
- **CL1:** a chosen sequence of admissible first-passage data at fixed \(g\), with \(a_j=L^{-K_j}\to0\) and centering states as above, has convergent centered moments on every separated tuple. Its regularity is a distribution of locally finite order off the diagonals. The positive-time Hilbert completion and its diagonal-flat completion agree. We rederive its time-semigroup identity in Lemma 9. Its cone is not needed for PH1.

The elementary functional-analysis imports are the joint spectral theorem for commuting bounded normal operators, spectral functional calculus, Hilbert projection, Riesz representation on compact metric spaces, Stone–Weierstrass, and the bounded monotone-class theorem. Their hypotheses are checked at each use. The mean-ergodic step is proved below.

## Order of constants

Upstream choices are those of `in1.md`, **Constant order**, rows 1–10, including Amendment 1. PH1 makes no new choice inside that induction. In that order: (1) reserve, rarity loss, margins and power-count exponents; (2) geometry, then odd \(L\), including \(L>L_0^\natural\), then flat/averaging and weak flow constants; (3) gauges, inverses, propagator/profile/walk rates, local walk size, reset scale, gap, seam and tower bounds; (4) early matrix and Gaussian constants, \(W_0\), then \(\kappa\ge\kappa_0^\natural(L)\), \(\Theta\), \(\lambda\); (5) decay floors \(\bar\kappa,\kappa_1\), response length and radii, preparation constants, then \(M\); (6) post-\(M\) comparison constants, tilt, \(A_1\) before \(A_0\), \(C_0\) before \(C_1\), absolute radii and age constants; (7) list constants and boundary/volume costs, certificate constants before \(c_G\), envelope/coding constants before entropy, then reserve costs and \(c_1\); (8) remaining prepared-source, label, floor, flow-error and tube constants; (9) enlarge \(X_0\), set \(\gamma=X_0^{-1/2}\), then determine \(\varsigma,\lambda_\sharp,B_\sharp\); (10) choose \(0<g\le\gamma\), admissible grids and bare \(\beta\ge g^{-2}+B_\sharp\). Internal dependencies and all inequalities remain exactly those of IN1's table. Its actual-construction obligations remain imports, not conclusions here.

After these choices retain the uniform SR1 constants \(c_M,C_n,B,k,C_E\) at this \(g\), before selecting the limiting sequence or components. The plateau proof uses independent numerical constants \(\kappa_{\rm PL}=2\log(1+\sqrt2)/\pi\), \(c_\Psi=(1+\sqrt2)^{-1}\), then \(c=\kappa_{\rm PL}\pi/8\), then one numerical \(C_{\rm PL}\) dominating the displayed shell and integral bounds. Its \(r\) is a lattice support radius, not IN1's power-count exponent. For fixed tuples choose separated containers and their radius/separation bounds, then a physical enclosing cube and positive margin, then moment and clustering constants, then the large-distance threshold. Choose distances in a mixed-moment approximation in the order \(v_q,\ldots,v_2\), after the constants depending on the already fixed union. Only then take the cutoff limit; the successive infinite-distance limits in (20) take \(v_2\) first. No constant depends on \(\xi\), the chosen state, cutoff or volume-first subsequence at this \(g\).

## Theorem 1 (PH1)

Assume LG1, SR1 and CL1 with the definitions and order above. Then:

1. **Lattice plateau (G3).** For every \(\nu\in\mathcal G_{a,\beta}\), mixtures included, \(A,B\in\mathfrak A(a[-r,r]^4)\), and \(y\in a\mathbb Z^4\) with \(n=|y|_\infty/a-2r\ge1\),
   \[
   |\nu(\overline A\tau_yB)-\operatorname{Pl}_\nu(A,B)|
   \le C_{\rm PL}[(r/n)^2+(r/n)^3]\mathcal N_{\nu,r}(A)^{1/2}\mathcal N_{\nu,r}(B)^{1/2}.
   \]
   The numerical constant is independent of \(a,\beta,\nu,r,n,A,B\).
2. **Lattice decomposition.** Compact-metric conditional probabilities admit Borel versions with simultaneous probability-valued uniqueness. They give the unique decomposition of \(\mathcal G_{a,\beta}\) into ergodic DLR states. The pure set is closed.
3. **Canonical decomposition.** Every centered volume-first limit has a canonical representation \((X,\lambda,\sigma_\xi)\), unique up to the isomorphism defined above. Every component is a limit of pure lattice states with the common centering. It has translation and \(W_4\) invariance, coordinate and diagonal RP, symmetry, reality, regularity and SR1's growth and bounds with the same constants. Its one-point form is \(\mathfrak c_\xi\int f\), with continuous bounded real \(\mathfrak c_\xi\) and \(\int_X\mathfrak c_\xi\,d\lambda=0\). Any Euclidean isometry preserving \(\sigma\) permutes components by a measure-preserving homeomorphism. Additional symmetries of the mixture need not fix individual components; full \(O(4)\) covariance requires RO1 for each component.
4. **Clustering.** For fixed compact separated tuples \(F,G\), or finite sums of them,
   \[
   |\sigma_\xi(F\cdot\tau_vG)-\sigma_\xi(F)\sigma_\xi(G)|
   \le C(F,G)|v|_2^{-2}\quad(|v|_2\ge r(F,G)),
   \]
   uniformly in \(\xi\) and over the volume-first limits at \(g\). This numerical rate is asserted on this test domain.
5. **Vacuum (PV4).** The rule \(P_0[F]\mapsto(\xi\mapsto\sigma_\xi(F))\) extends to a unitary \(\ker H\to L^2(X,\lambda)\), sending \(\Omega\) to \(1\). Each component has \(\ker H_{\sigma_\xi}=\mathbb C\Omega_{\sigma_\xi}\). The identity (PV3) is derived from bounds, RP and translation invariance. SR1's density identifies these completions with the diagonal-flat completions.

Lemmas 2–10 prove these clauses. The qualifications in clauses 3–5 specify the scope of the checked notes; they are necessary readings of the skeleton.

## Lemma 2. Transfer operators and their spectral carrier

**Source:** `cluster-port.md` §2; `gates/cluster-check.md` A1–A2; SA 3260–3427.

**Statement.** The coordinate reflection spaces carry positive self-adjoint contractions and commuting tangential unitaries satisfying (2) and the carrier (4).

**Proof.** Let \(\nu\) be any translation-invariant lattice law with LG1's mirror properties. Lemmas 2–5 do not use DLR. Set \(a=1\) until Lemma 5. In coordinate picture \(\mu\), complete the bounded local positive-half functions for
\[
 \langle[F],[G]\rangle_\mu=\nu(\overline{\theta_\mu F}G).
\]
LG1 gives positivity and reflection invariance. Thus \(\|[F]\|\le\|F\|_2\le\|F\|_\infty\). Normal translation is symmetric. Iterated Cauchy–Schwarz gives
\[
 \|[\tau_{e_\mu}F]\|
 \le\|[F]\|^{1-2^{-k}}\|[\tau_{2^ke_\mu}F]\|^{2^{-k}}
 \le\|[F]\|^{1-2^{-k}}\|F\|_\infty^{2^{-k}}.
\]
Let \(k\to\infty\). Translation preserves null vectors and defines a self-adjoint contraction \(T_\mu\). RP at \(x_\mu=-1/2\) gives \(T_\mu\ge0\). Tangential translations preserve the form and have inverses. They define commuting unitaries \(U_{\mu,\lambda}\), also commuting with \(T_\mu\). Hence
\[
 \langle[F],T_\mu^sU_\mu^w[G]\rangle
 =\nu(\overline{\theta_\mu F}\tau_{se_\mu+w}G),\qquad s\in\mathbb N_0,\quad w\in\mathbb Z^3.
\tag{2}
\]
The joint spectral theorem applies to these bounded commuting normal operators. Write their variables as \(t=e^{-E}\in[0,1]\) and \(e^{i\eta_\lambda}\), with principal angles \(\eta\in(-\pi,\pi]^3\). The value \(t=0\) means \(E=\infty\).

**Lemma 2.1 (disc measure; same sources).** If a finite positive measure \(m\) on the closed unit disc satisfies
\[
 \int|p|^2\,dm\le C_0\sup_{[0,1]}|p|\sup_{|z|=1}|p|
\tag{3}
\]
for every polynomial, then \(m\{|1+z|^2<4|z|\}=0\).

**Proof of Lemma 2.1.** Set
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
These identities identify the excluded set. On the circle it consists of every point except \(1\). This proves Lemma 2.1. \(\square\)

**Completion of Lemma 2.** Fix \(\lambda\ne\mu\) and a local positive-half function \(F\). Choose an integer \(R\ge1\) with \(0\le x_\mu\le R\), \(|x_\lambda|\le R\) on its support. Let \(\theta'\) reflect at \(x_\mu+x_\lambda=R\). Both \(B=\theta'\theta_\mu F\) and \(F_0=\tau_{2Re_\mu}F\) lie above this diagonal mirror. In its reflection space, translation by \(d_+=e_\mu+e_\lambda\) gives a positive contraction \(T_+\). Translation by \(d_-=e_\mu-e_\lambda\) gives a unitary \(V_-\). The preceding construction applies; positivity uses the mirror at height \(R+1\), with \(\theta_{R+1}\tau_{d_+}=\theta_R\). Equation (2) in the two pictures gives
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
 E\ge\kappa_{\rm PL}|\eta|_\infty,\quad
 \kappa_{\rm PL}=\frac2\pi\log(1+\sqrt2).
\tag{4}
\]
Indeed, \(E\ge2\operatorname{arsinh}\sin(|\eta_\lambda|/2)\). The derivative of this last function is \(\cos(u/2)/\sqrt{1+\sin^2(u/2)}\), decreasing on \([0,\pi]\). Its graph lies above its endpoint chord. Intersect the three tangential carriers. At \(t=0\) the operator inequality holds without a restriction on momentum.

\(\square\)

## Lemma 3. The invariant plateau

**Source:** `cluster-port.md` §3; `gates/cluster-check.md` A2; SA 3429–3476.

**Statement.** Zero energy is the completed translation-invariant field, with inner product (6).

**Proof.** Let \(\Pi_\mu=1_{\{E=0\}}\). Spectral convergence gives \(T_\mu^s\to\Pi_\mu\). Equation (4) gives \(U_\mu^w\Pi_\mu=\Pi_\mu\). Let \(P_\mu\) condition on the completed invariant field \(\mathcal I_\mu\) of the single normal translation. Cesaro averaging (2) gives
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
Conditional expectation here is unchanged by translations or coordinate reflections.

\(\square\)

## Lemma 4. A positive filter with bounded momentum density

**Source:** `cluster-port.md` §4; `gates/cluster-check.md` A1–A2; SA 3478–3651.

**Statement.** The filter (8) yields, for reflection-parity observables, the positive momentum measure (9) and density bound (11).

**Proof.** For \(Q_r=[-r,r]^4\), \(r\in\mathbb N\), \(r\ge1\), set
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
Summing in \(s=2rm\) inserts \(q(2r\eta'_\mu)\). Nonzero values require \(|\eta'_\mu|>\pi/(8r)\); other periodic copies of the zero set do not weaken this implication. The carrier (4) therefore gives, with \(c=\kappa_{\rm PL}\pi/8\),
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
This is a weighted density, not a density assumption on the original spectral measure.

\(\square\)

## Lemma 5. Uniform lattice plateau and closedness

**Source:** `cluster-port.md` §5; `gates/cluster-check.md` A1–A2; SA 3653–3751.

**Statement.** The bound (PL3) holds for all bounded local complex observables. The invariant all-mirror RP class and its ergodic subset are weakly closed.

**Proof.** First assume \(\theta_\mu A=\pm A\) and put \(\Phi=\Phi_A^\mu\). The density in (11) has no atom at \(\eta=0\). By (8), the original spectral measure therefore has no mass at \(0<E<\infty,\eta=0\). The weight is zero at \(E=0\), so this conclusion removes no plateau. Energy infinity contributes zero to \(T_\mu^n\), \(n\ge1\).

Since \(\coth u=1+2/(e^{2u}-1)\le1+1/u\), the inverse filter is integrable in three momentum variables. The function \(e^{-nE}/\tanh(2rE)\) decreases for \(E>0\). Using (4), (8), (11), and \(\coth u\le1+1/u\), we obtain
\[
 \begin{aligned}
 \langle\Phi,T_\mu^n(1-\Pi_\mu)\Phi\rangle
 &\le Cr^3\mathcal N_r(A)\int_{\mathbb T^3}
   \frac{e^{-n\kappa_{\rm PL}|\eta|_\infty}}{\tanh(2r\kappa_{\rm PL}|\eta|_\infty)}\,d\eta\\
 &\le Cr^3\mathcal N_r(A)\int_0^\infty
   u^2e^{-n\kappa_{\rm PL} u}(1+(2r\kappa_{\rm PL} u)^{-1})\,du\\
 &\le C\mathcal N_r(A)[(r/n)^3+(r/n)^2].
 \end{aligned}
\tag{12}
\]
The cube shell volume is \(24u^2du\). The two integrals are \(2/(n\kappa_{\rm PL})^3\) and \(1/(n\kappa_{\rm PL})^2\), by integration by parts.

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
For ergodic \(\nu\), the plateau is \(\overline{\nu(A)}\nu(B)\). S3 was not used.

At fixed spacing the invariant RP class is weakly closed. Continuous local positivity inequalities pass to a weak limit, as does reflection invariance. Continuous half-space cylinder functions are dense in the corresponding \(L^2\) space. Ordinary Cauchy–Schwarz therefore extends RP to bounded Borel half-space functions.

Its ergodic subset is also closed. If ergodic \(\nu_j\to\nu\), pass PL3 for continuous local \(A,B\) to the limit, bounding \(\mathcal N_r\) by supremum norms. The limit still clusters to \(\overline{\nu(A)}\nu(B)\). Cesaro averages along \(ke_\mu\), with \(A=B\), give
\(\|E_\nu[A\mid\mathcal I_\mu]\|_2^2=|\nu(A)|^2\).
This conditional expectation is therefore constant. Density of continuous local functions makes \(\mathcal I_\mu\), hence \(\mathcal I\), trivial. No assumption of closedness of extreme states entered the proof.

\(\square\)

## Lemma 6. Compact-metric conditional kernels

**Source:** `cluster-port.md` §6; `gates/cluster-check.md` A2; SA 30875–31105.

**Statement.** Let \(K\) be compact metric, \(\mu\) a Borel probability, and \(\mathcal H\) a sigma-field satisfying
\[
 \mathcal N_\mu\subset\mathcal H\subset\overline{\mathcal B(K)}_\mu .
\]
Here \(\mathcal N_\mu\) denotes all subsets of Borel \(\mu\)-null sets.
Here \(\mathcal P(K)\) has its weak topology, and \(kf(x)=\int f\,dk(x)\). There is a Borel, \(\mathcal H\)-measurable map \(k:K\to\mathcal P(K)\) such that
\[
 kf=E_\mu[f\mid\mathcal H]\quad\mu\text{-a.s.}
\tag{14}
\]
for each bounded Borel \(f\). Two such probability-valued maps agree off one Borel null set.

**Proof.** Distances to a countable dense set generate a countable rational unital algebra and lattice \(D\subset C(K;\mathbb R)\). It separates points, so Stone–Weierstrass makes it uniformly dense. Project each \(f\in D\) onto \(L^2(\mathcal H,\mu)\). Testing against \(1_H\), \(H\in\mathcal H\), gives the defining conditional integral identity, positivity, and the supremum norm bound. Choose Borel representatives: replace each rational level set by a Borel set modulo a Borel null set. Such replacement preserves \(\mathcal H\)-measurability because \(\mathcal H\) contains all null subsets.

Outside one Borel null set, the countably many representatives preserve \(1\), rational linear relations, and positivity on every nonnegative member of \(D\). At each remaining point \(x\), they define a positive unital rational-linear functional \(L_x\). For rational \(r>\|f\|_\infty\), positivity of \(r\pm f\) gives \(|L_x(f)|\le r\). Uniform extension gives a positive real-linear functional on \(C(K)\). Riesz representation supplies \(k(x)\in\mathcal P(K)\). On the exceptional set choose one fixed point mass.

The coordinate map \(\rho\mapsto(\rho(f))_{f\in D}\) embeds \(\mathcal P(K)\) in a countable product. Its image is compact: any coordinate-convergent subsequence extends to a positive unital functional and hence a probability by the same argument. Uniform density identifies its coordinate topology with the weak topology. The inverse on the compact image is continuous. Therefore the constructed \(k\) is both Borel and \(\mathcal H\)-measurable as a probability-valued map.

Uniform approximation proves (14) for continuous functions. The functions satisfying its integral identity against every \(1_H\) form a vector space closed under bounded increasing limits. The functional monotone-class theorem extends (14) to all bounded Borel functions, since continuous functions generate the Borel field. Finally, uniqueness of conditional expectations on the countable set \(D\) gives equality of two kernels on all continuous functions simultaneously. Riesz uniqueness gives equality of their probability measures off one null set.

This does not assert pointwise properness on every conditioning event. Nor does it select a universal version for an uncountable family of preassigned conditional expectations. The kernel, its barycenter, and its law are unambiguous modulo null sets.

\(\square\)

## Lemma 7. The fixed-spacing decomposition

**Source:** `cluster-port.md` §7; `gates/cluster-check.md` A2; SA 31129–31143, 31180–31250.

**Statement.** Every invariant Wilson DLR state has a unique probability decomposition on the compact set of translation-ergodic Wilson DLR states. These are exactly the extreme points of the invariant DLR class.

**Proof.** The Wilson kernels defined above preserve continuous local functions and have operator norm at most one in the supremum norm.

The countable product \(\Omega_a\) is compact metric. Invariance and DLR are closed affine equations on its probability measures. Cubic torus laws have weak limit points. Each finite DLR equation holds once its interaction neighbourhood embeds without wrapping, and passes to such a limit. Thus \(\mathcal G_{a,\beta}\) is nonempty compact convex. LG1 gives its mirror properties.

**Invariant densities preserve DLR.** For bounded invariant \(h\), approximate \(h\) in \(L^1(\nu)\) by bounded continuous local \(h_m\). Translate \(h_m\) so its bond support misses \(W\). Translation invariance preserves the approximation error, and DLR gives
\[
 \nu(h_m\gamma_WF)=\nu(\gamma_W(h_mF))=\nu(h_mF).
\]
Each replacement error is at most \(\|h-h_m\|_1\|F\|_\infty\). Hence \(\nu(h\gamma_WF)=\nu(hF)\). For \(h\ge0\), \(\nu(h)>0\), the normalized law \(h\nu/\nu(h)\) belongs to \(\mathcal G_{a,\beta}\).

Apply Lemma 6 to the completed translation-invariant field \(\mathcal I\). Write \(\nu^\omega(F)=E_\nu[F\mid\mathcal I](\omega)\). Testing the preceding identity with \(h=1_I\), \(I\in\mathcal I\), gives
\[
 \nu^\omega(\gamma_WF)=\nu^\omega(F),\qquad
 \nu^\omega(\tau_vF)=\nu^\omega(F)
\]
almost surely. Impose these equations on one countable dense family of continuous local functions, all finite \(W\), and all translations \(v\). A single null set suffices. Uniform approximation and contraction of \(\gamma_W\) extend the equations to all continuous tests. The monotone-class theorem extends them to bounded Borel tests. Thus \(\nu^\omega\in\mathcal G_{a,\beta}\) almost surely, and LG1 applies to it.

PL3 proves these conditional laws ergodic. For continuous local \(A\), integrate the limit along \(ke_\mu\):
\[
 \int\operatorname{Pl}_{\nu^\omega}(A,A)\,d\nu(\omega)
 =\operatorname{Pl}_\nu(A,A)
 =\int|\nu^\omega(A)|^2\,d\nu(\omega).
\tag{15}
\]
The limits are bounded by \(\|A\|_\infty^2\), so dominated convergence applies. For each conditional state the difference between the two integrands is nonnegative. It is the variance of its own invariant conditional expectation of \(A\). Thus it vanishes almost surely. Impose this on a countable dense local family; density in each \(L^2(\nu^\omega)\) makes its invariant subspace constant.

Let \(\mathcal E_{a,\beta}\) be the ergodic states. They are precisely the extreme points of \(\mathcal G_{a,\beta}\). A nontrivial invariant event gives a nontrivial convex decomposition by the invariant-density argument. Conversely, densities of summands in a convex decomposition are bounded and invariant. Ergodicity makes them constant, so both summands equal the original state. Lemma 5 makes \(\mathcal E_{a,\beta}\) closed, hence compact.

The law \(D_\nu=(\omega\mapsto\nu^\omega)_*\nu\) is supported on \(\mathcal E_{a,\beta}\) and has barycenter \(\nu\). It is the unique such law. Indeed, for any law on \(\mathcal E_{a,\beta}\), PL3 identifies every mixed moment of local state evaluations with successive far-translation limits of its barycenter. Each step separates one factor from the fixed remaining product; the error tends to zero uniformly over states. Evaluations of continuous local functions separate this compact state space. Their polynomial algebra is uniformly dense by Stone–Weierstrass, so equal mixed moments give equal laws. This includes uniqueness independently of the conditional-kernel version.

\(\square\)

## Lemma 8. Canonical components and uniform clustering

**Source:** `cluster-port.md` §8; `gates/cluster-check.md` A1–A3; SA 31142–31178, 31252–31380.

**Statement.** The centered limit has the canonical compact representation described in Theorem 1(3), with intrinsic moments (20), lattice-state realizations for every support point, and the uniform clustering bound (19).

**Proof.** Keep the prescribed sequence and common centering throughout.

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

Every expression in \(\mathcal N_{r_j}(F_j)\) consists of two reflected copies of \(F\), separated by at least \(2\epsilon\). Equation (16), at order \(2k\) and separation \(\min(\delta(F),2\epsilon)\), bounds it by a constant \(N(F;R_0)\). This constant is independent of \(j,\rho\). LG1 ensures covariance also for the common centering. Hence (13) gives, for every pure lattice state \(\rho\),
\[
 |\rho(F_j\,\tau_{v_j}G_j)-\rho(F_j)\rho(G_j)|
 \le C(F,G)|v_j|_2^{-2}
\tag{18}
\]
once \(|v_j|_2\) exceeds a fixed physical threshold. The constants are uniform in \(j,\rho\). Here \(r_ja_j\le R_0+a_j\), so the lattice-to-physical conversion is uniform. Supremum norms of \(F_j\) do not enter.

**Countable coordinates and existence.** Take finite unions \(Q\) of rational closed boxes. The \(C^1\) functions supported in \(Q\) form a separable space: embed them by their value and four derivatives in \(C(Q)^5\). Choose a countable dense set in each such space, and all separated tuples from their union. Call the resulting family \(\mathfrak F\). Any separated tuple can be approximated in fixed separated containers: enclose each support in rational boxes inside those containers, then use the corresponding dense set.

Use the converging sequence specified in CL1. Bounds (16)–(17) apply to that sequence and to every pure-state realization below. Set
\[
 \mathsf K=\prod_{F\in\mathfrak F}[-B(F),B(F)],\quad
 e_j(\rho)=(\rho(F_j))_F,\quad
 \lambda_j=(e_j)_*D_{\nu_j}.
\]
Each \(e_j\) is continuous on the compact pure-state space from Lemma 7. Thus \(\lambda_j\) is a probability on compact metric \(\mathsf K\).

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

Common centering is retained: \(\sigma(f)=0\), while individual \(\sigma_\xi(f)\) can differ.

\(\square\)

## Lemma 9. Time evolution and the vacuum space

**Source:** `cluster-port.md` §9; `gates/cluster-check.md` A2, A4; SA 31386–31527.

**Statement.** On the completion generated by positive-time separated tuples, (PV3) follows from the moment bounds, RP and translations. The map (PV4) is unitary, and each component has a one-dimensional vacuum space.

**Proof.**

First construct its time evolution. For complex finite sums of such tuples, use
\[
 \langle[F],[G]\rangle=\sigma(\overline{\theta F}\,G),\qquad \theta:x_4\mapsto-x_4.
\]
Every matrix entry is separated; the lattice RP limits of Lemma 8 make this form positive. Quotient its null space and complete. On representatives put \(T_t[F]=[\tau_{te_4}F]\), \(t\ge0\). Translation invariance makes this map symmetric in the form. Moreover
\[
 \langle[F],T_t[F]\rangle=\|[\tau_{te_4/2}F]\|^2\ge0.
\]
For each fixed finite sum \(F\), (16) bounds \(\|[\tau_{se_4}F]\|\) uniformly for \(s\ge0\). Internal separations remain fixed, and the reflected halves only move farther apart. The iterated Cauchy–Schwarz argument of Lemma 2 therefore proves contraction and preservation of null vectors. The resulting \(T_t\) are commuting positive self-adjoint contractions with \(T_{t+s}=T_tT_s\).

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

If \(X\) has \(m<\infty\) points, full support makes all their masses positive, so \(\dim\ker H=m\). If \(X\) is infinite, arbitrarily many distinct points have disjoint open neighbourhoods of positive measure. Their indicators give arbitrarily many orthogonal vectors. Compact metrizability makes \(L^2(X,\lambda)\) separable, so its dimension is countably infinite. Neither assertion gives a spectral gap.
\(\square\)

## Lemma 10. One-point forms, inherited growth and isometries

**Source:** `cluster-port.md` §8 and its common-centering observation; `gates/cluster-check.md` A3–A4 and B3–B4. The following explicit completion of the skeleton uses SR1(3)–(4). Compare SA 25375–25391, 25715–25734 and 25905–25958, read at the pinned revision. The one-point and symmetry arguments below are additions to the distilled text, not separately checked by that gate.

**Statement.** The representation of Lemma 8 has all the additional properties in Theorem 1(3). Its diagonal-flat RP completion is the completion used in Lemma 9.

**Proof.** Fix a real \(f_0\in C_c^1\) with \(\int f_0=1\), and set \(\mathfrak c_\xi=\sigma_\xi(f_0)\). This is continuous and bounded by \(C_1(R_0)\|f_0\|_\sharp\). For a pure-state realization of \(\xi\), LG1 makes
\[
 d_j=\rho_j(a_p)-\nu_j(a_p)
\]
independent of the plaquette. There are six unoriented plaquette orientations per site. Put
\[
 R_j(f)=\frac{a_j^4}{6}\sum_p f(x(p)),\qquad c_j=6a_j^{-4}d_j.
\]
Then \(\rho_j Z_j(f)=c_jR_j(f)\) exactly. Each of the six shifted grid sums in \(R_j\) converges to \(\int f\). Indeed, on each cube of side \(a_j\), replacing the integral by the sampled value costs at most \(2a_j\|\nabla f\|_\infty\) times its volume. Only cubes meeting a fixed enlargement of the support contribute; their total volume is bounded. The total error tends to zero. Thus \(R_j(f_0)\to1\), and convergence at \(f_0\) gives \(c_j\to\mathfrak c_\xi\). Consequently
\[
 \sigma_\xi(f)=\mathfrak c_\xi\int f.
\]
The barycenter and \(\sigma(f_0)=0\) give \(\int_X\mathfrak c_\xi\,d\lambda=0\).

Apply SR1's graded bound to the two states \(\rho_j,\nu_j\). The pure-state realization in Lemma 8 passes it to every \(\sigma_\xi\), with the original constants. SR1's extension theorem therefore applies to each component with the same \(C_E,k\). It gives
\[
 |\sigma_{\xi,n}(\varphi)|\le C_E^n(n!)^{k+32}p_{20n}(\varphi),
 \qquad \varphi\in\mathcal S_{\Delta,n}.
\]
On any fixed compact set away from the diagonals the weight is bounded; this is a distribution of finite order there. Tensor density gives uniqueness, symmetry, reality, and covariance of the extension from their identities on separated smooth tensors. Signed permutations preserve the displayed seminorm, and translations act continuously on the test space. Coordinate or diagonal RP passes by density from finite matrices of compact positive-half tuples. The tensor \(\overline{\theta f}\otimes g\) is diagonal-flat: internal diagonals are killed by the factors, and a cross coincidence forces both time coordinates to zero, where the factors are flat. Tensor multiplication is continuous in Schwartz seminorms. Thus approximating finite positive-time sequences by the constrained tensors makes their RP squared distances tend to zero. Conversely smooth compact separated tuples approximate compact \(C^1\) tuples in fixed separated positive-time containers by (17). The two quotient completions coincide isometrically, for the mixture and each component. This establishes the stated scope of PV4 on the extended domain. It does not extend the inverse-square rate to arbitrary completed vectors.

The same uniform extension estimate makes each extended evaluation a uniform limit on \(X\) of finite sums of compact tuple evaluations. It is therefore continuous. The barycenter identity extends by the same approximation and bounded convergence. No different centering is introduced.

Finally let \(h(x)=Qx+b\), \(Q\in O(4)\), preserve \(\sigma\). On the same compact phase space define \(\widetilde\sigma_\xi(F)=\sigma_\xi(hF)\). These evaluations remain continuous and separate points, since \(h\) bijects the separated tuples. They have barycenter \(\sigma\). Since \(h\tau_v=\tau_{Qv}h\), their uniform clustering and iterated moment identities follow from (19)–(20). In particular their intrinsic mixed moments are those of \(\sigma\). The uniqueness argument of Lemma 8 gives a measure-preserving homeomorphism \(\pi_h:X\to X\) with
\[
 \sigma_{\pi_h(\xi)}(F)=\sigma_\xi(hF).
\]
For translations and \(W_4\), inherited component invariance makes this permutation the identity, since evaluations separate points. For another symmetry of \(\sigma\), the argument proves a permutation; it does not prove that every component is fixed. \(\square\)

**Proof of Theorem 1.** Lemmas 2–5 prove clause 1, including mixtures and the numerical constant. Lemmas 6–7 prove clause 2. Lemma 8 proves the canonical representation, every support-point realization, uniqueness and clause 4. Lemma 10 supplies the one-point, growth, regularity and isometry assertions completing clause 3. Lemma 9 proves clause 5 on the separated positive-time completion, and Lemma 10 identifies the extended completion. All estimates used for (18)–(19) depend only on the fixed imports and tuple geometry. This gives uniformity over every admitted sequence at the chosen \(g\). \(\square\)

## Result

PH1 proves the lattice plateau law, compact conditional kernels, the unique lattice ergodic decomposition, the canonical continuum component representation, inverse-square clustering on compact separated tuples, and the vacuum-space unitary. It is an implication from **LG1, SR1 and CL1**, with IN1's order of constants through those imports. S3 gives the component construction; SR1's graded bound and constrained extension are additionally required for factorial growth and the extended Hilbert domain. The upstream actual-construction obligations remain open wherever their source parts leave them open. No internal **Outstanding** step remains in the displayed conditional argument.

Corrections and explicit completions made in this distillation:

1. Required the common centering states to lie in \(\mathcal G_{a_j,\beta_j}\), as gate A3 requires. Every component retains this centering.
2. Defined purity only within the invariant DLR class. Continuum components are correlation forms, not an assumed continuum probability disintegration.
3. Restricted the quantitative clustering assertion to the compact separated test domain of the checked proof. Identified the extended Hilbert completion using SR1 density; did not infer a rate for arbitrary Hilbert vectors.
4. Distinguished inherited component symmetries from extra symmetries of the mixture. The latter permute phases; full rotational covariance is an additional RO1 conclusion.
5. Made the graded SR1 input explicit for growth, retained gate A4's PV3 domain, and supplied the one-point calibration and isometry proofs in Lemma 10.
6. Kept the diagonal-mirror identity at height \(R+1\) from gate A2, retained the positive-energy zero-momentum exclusion before removing the filter, and separated \(\kappa_{\rm PL}\) and the support radius from IN1's constants. Corrected the source endpoints to include the complete arguments.

Definitions supplied explicitly: the oriented bond configuration space and Wilson DLR kernel; the invariant DLR class, local algebra, pullback convention, mirror and sign groups, completed invariant field and purity; reflection size and plateau; separated tuples, admissible concatenation, empty tuple and finite-sum domain; common centering and volume-first limit; canonical full-support representation and its isomorphisms; continuum component terminology; positive-time quotient, vacuum and zero-energy projection; diagonal-flat/time-flat test spaces and seminorms; the calibration \(R_j,c_j,\mathfrak c_\xi\). Auxiliary definitions carried over with their proofs are the reflection operators and spectral variables, filter and weighted measure, conditional kernel, partition bounds, countable coordinates, evaluation laws and evaluation functions.

**Source verification.** SA denotes `YM4_sketch_500.tex` at `31a47c543775`, credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The index README, relevant rows and neighbours of chunks 03, 04, 23, 28 and 29, and the phase obligations were used before reading the raw passages. The proof-bearing excerpts checked here are SA 3195–3751, 4179–4194, 4486–4567, 25375–25391, 25715–25734, 25905–25958 and 30866–31527. These contain detailed conditional proofs, not a new phase construction supplied by this part. SA's PV4 section explicitly assumes PV3; Lemma 9 retains the checked note's derivation of PV3. For comparison, YM3_I 77468–77559 and 78224–78323 were read: the former has the three-dimensional inverse-distance rate, and the latter the same vacuum-density argument. Neither substitutes for the four-dimensional estimates above. CA-I was fetched as requested. No CA-I/II/III theorem is imported or quoted here; the skeleton's broad CA-II range is not used to discharge a step. Raw sources were fetched once into `/tmp`; none was read whole. No computer-assisted step or run discharged a proof.

This assembled part is **not yet refereed as a whole part**. The earlier check of `cluster-port.md` remains attributed to Claude; Lemma 10 and the present assembly are not covered by that earlier check. This is research text, not an audit, and grants no status.
