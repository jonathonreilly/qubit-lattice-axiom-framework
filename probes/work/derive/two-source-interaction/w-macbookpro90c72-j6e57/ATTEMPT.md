# two-source-interaction, attempt 2 (worker w-macbookpro90c72-j6e57, model grok-4.6)

Independent of other attempts (none on the branch at claim time). Setting: symmetric light-cone formation in 3+1 (README §8, problem `lightcone-formation`). The record at \((t+1,x)\), \(x\in\mathbb{Z}^3\), is formed from the seven records \((t,x)\) and \((t,x\pm e_j)\). Linear gain-one model: \(\phi(k)=1-E(k)/7\), \(E(k)=\sum_j 2(1-\cos k_j)\). Backward (asymmetric) cone is used only as the contrast the task names.

## (1) The statement attempted

**(a)** The symmetric 7-point automaton in level time is a Gaussian AR(1) with *real* \(\phi\). It is reversible in stationarity (joint covariance of \((\theta_t,\theta_{t+1})\) is symmetric). The naive equilibrium FDR “static response = covariance” is **false**: \(\chi=1/(1-\phi)=7/E\) and \(C=\sigma^2/(1-\phi^2)=7\sigma^2/(2E(1-E/14))\) satisfy \(\chi=C(1+\phi)/\sigma^2\) with \(1+\phi=2-E/7\) not constant. Both are \(\sim 1/k^2\) in the IR, hence both \(\sim 1/r\) in three dimensions. On the *backward* cone \(\phi\) is complex, the chain is not reversible, \(\chi\) is not real, and the response is a forward-cone multinomial (no isotropic \(1/r\)).

**(b)** Persistent field \(h\) at every level: stationary mean \(m=(I-P)^{-1}h\), Fourier \(7\hat h(k)/E(k)\) (zero mode excluded). Persistent pin \(\theta(0)=\alpha\) of the stationary Gaussian is the same profile times \(\alpha/C(0)\) in the mean-zero subspace. Exact values on the \(L=4\) torus (in \(\mathbb{Q}\)): \(\chi(0)=10619/7680\), \(\chi(e_1)=1799/7680\), \(C(0)=18179/15360\), \(C(e_1)=539/15360\).

**(c)** Two Gaussian pins of amplitudes \((a,b)\) at distance \(r\): \(-\log\) density \(=\frac12(a,b)C_2^{-1}(a;b)+\frac12\log\det C_2\), \(C_2=\bigl(\begin{smallmatrix}C(0)&C(r)\\C(r)&C(0)\end{smallmatrix}\bigr)\). Amplitude-dependent interaction: like pins \((a,a)\) shift \(-\log\) by \(1/(C(0)+C(r))-1/C(0)\), unlike \((a,-a)\) by \(1/(C(0)-C(r))-1/C(0)\). Whenever \(C(r)>0\) (nearest neighbour on \(L=4,8\)) like is attractive and unlike repulsive. The IR coefficient of \(C(r)\) is \(7\sigma^2/(8\pi r)\) and of \(\chi(r)\) is \(7/(4\pi r)\) (continuum Fourier of \(1/k^2\); ASSUMED as that standard transform). On \(L=4\), \(C(1,1,1)<0\) by wrapping (lattice sign change, not IR).

**(d)** Mass = source amplitude \(h\) or pin value \(\alpha\). Linear interaction \(U=h_1 h_2\cdot 2\chi(r)\) (field picture) is pairwise: no three-body term in the quadratic form. Superposition of means is exact. It fails for the sphere (\(|s|=1\) saturates) and for the \(r\)-dependent \(\log\det C_2\) (amplitude-independent, entropic).

## (2) Steps

**Step 1 — symbols (PROVED; CHECKED as E1, E6).** \(\phi=(1+2\sum_j\cos k_j)/7=1-E/7\). Then \(1-\phi=E/7\), \(1-\phi^2=(2E/7)(1-E/14)\), \(\chi=7/E\), \(C=7/(2E(1-E/14))\) at \(\sigma^2=1\). Modewise on \(L=16,32\).

**Step 2 — FDR (PROVED; CHECKED as E1, E3, E7).** Discrete-time reversible Gaussian AR: \(\chi=C(1+\phi)/\sigma^2\). Equilibrium “\(\chi\propto C\)” would need \(1+\phi\) constant, false (\(1+\phi\in\{2/7,\ldots,12/7\}\) on \(L=4\)). Joint covariance \(\begin{psmallmatrix}C&\phi C\\\phi C&C\end{psmallmatrix}\) is symmetric iff \(\phi\) is real.

**Step 3 — backward cone is the no-go (PROVED; CHECKED as E2).** \(\phi=(1+e^{ik_1}+e^{ik_2})/3\) has \(\mathrm{Im}\,\phi\neq0\), \(\mathrm{Im}\,\chi\neq0\), \(C\) real, \(\chi/C\) not real. Response support is the forward multinomial cone (previous derivation, re-checked here at one mode).

**Step 4 — torus Green functions (CHECKED as E3, E5).** \(L=4\): DFT over \(\mathbb{Q}(i)\), \(\chi,C\) real and mean-zero, nn positive, \(\chi\neq C\). \(L=8\): same signs at \(e_1\) in \(\mathbb{Q}(\sqrt{2})\).

**Step 5 — two pins (PROVED as Gaussian algebra; CHECKED as E4, E5).** Formulae of (c). Like attractive / unlike repulsive on every tested \(r\) with \(C(r)>0\).

**Step 6 — 7-point pairing for the nonlinear automaton (PROVED; CHECKED as E8).** \(S_x=s_x+\sum_{\pm e}s_{x\pm e}\) still satisfies \(\sum_x s'_x\cdot S_x(s)=\sum_x s_x\cdot S_x(s')\), so the *nonlinear* synchronous plane kernel is reversible w.r.t. \(\pi\propto\prod_x Z(\beta|S_x|)\) (same argument as re-recording, 7-stencil). That Gibbs measure has equilibrium FDR; its large-\(\beta\) Hessian is not computed here (ASSUMED to share the \(1/E\) IR with the linear \(\chi\)).

**Step 7 — mass and superposition (PROVED; CHECKED as E9).** Cross term \(2\chi(r)\); three-source quadratic has no \(h_0 h_1 h_2\).

## (3) First failing step, if any

The linear theory does not fail. Not proved: the continuum \(1/(4\pi r)\) coefficient as a theorem on \(\mathbb{Z}^3\) (Poisson summation remainder); the sphere \(O(1/\beta)\) kernel of \(\pi\propto\prod Z\); nonlinear two-pin (Ising/sphere) at finite \(\beta\).

## (4) What would finish it

Watson’s integral / large-\(L\) expansion of the lattice Green function at \(r=e_1\) and along a ray, with an explicit \(7/(4\pi r)+O(1/r^3)\) remainder; the Hessian of \(\sum_x\log Z(\beta|S_x|)\) at an aligned plane, to confirm the \(1/E\) IR for the nonlinear automaton; a two-pin Monte Carlo on the sphere law at large \(\beta\).
