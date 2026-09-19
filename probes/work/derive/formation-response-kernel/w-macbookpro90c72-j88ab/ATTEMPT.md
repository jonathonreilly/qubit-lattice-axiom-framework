# formation-response-kernel, attempt 2 (worker w-macbookpro90c72-j88ab, model grok-4.6)

Independent of the a3 attempt printed at claim time. Route: 3D embedding of the causal generating function, exact infinite-plane Green function, eight-corner symbol as a rational function of \(e^{iq_j}\). Definitions from block 35 (PR #8180), the linearized law of blocks 26 and 34 (PRs #8170, #8178), and the eight corners of block 09 (PR #8139).

## (1) The statement attempted

Objects (block 35, restated). On the periodic \(L\times L\) level plane, the linearized sphere formation law is the real AR(1)
\[
\theta_t = P\theta_{t-1} + \xi_t + h_t,
\]
\(P\) the average of the three predecessors of \((i,j)\), namely \((i,j)\), \((i-1,j)\), \((i,j-1)\) on the level below; \(\phi(k)=(1+e^{ik_1}+e^{ik_2})/3\), \(u=|\phi|^2\), \(\mathrm{Var}(\xi)=\sigma^2\) per component. A mode of \(\mathbb{Z}^3\) with wavevector \(q\) and level coordinates \((k,w)\) given by \(q=(w+k_1,w+k_2,w)\) is used when a 3D reading is required. The eight corners \(\kappa\in\{\pm1\}^3\) of block 09 have predecessors \(x-\kappa_j e_j\).

**Statement.** For this linear model:

**(a)** The causal response to a source in the convention \(\theta_t=\phi\,\theta_{t-1}+h_t\) is
\[
R(k,w)=\frac{1}{1-\phi(k)e^{iw}}=\frac{3}{3-e^{iq_1}-e^{iq_2}-e^{iq_3}}.
\]
The static plane response is \(R(k,0)=1/(1-\phi(k))\) on the nonzero modes; it is the Fourier multiplier of \((I-P)^{-1}\) on mean-zero functions of the torus. The identity
\[
E(q)=2\sum_{j=1}^3(1-\cos q_j)=3\bigl(|1-\phi e^{iw}|^2+1-u\bigr)
\]
holds identically, so \(1/E\) is not a multiple of \(|R|^2\) or of \(R\).

**(b)** The impulse response on the infinite plane is the multinomial
\[
G_t(n,m)=3^{-t}\frac{t!}{n!\,m!\,(t-n-m)!}\qquad(n,m\ge0,\,n+m\le t),
\]
else \(0\). In the co-moving frame \(y=x-t(1,1)/3\) the one-step covariance is exactly \(C=(1/9)\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\), and the quadratic characteristic function has Gaussian
\[
\frac{3\sqrt{3}}{2\pi t}\exp\bigl(-3(y_1^2+y_2^2+y_1 y_2)/t\bigr)
\]
(leading local-CLT term). The static Green function of a persistent source at the origin on the infinite plane is exactly
\[
G(n,m)=\sum_{t\ge0}G_t(n,m)=\frac32\binom{n+m}{n}2^{-(n+m)}\qquad(n,m\ge0),
\]
and \(G=0\) off the forward quadrant. Pinning \(\theta(0)=\alpha\) on the infinite plane is \(m=\alpha\,G/G(0)\) with \(G(0)=3/2\).

**(c)** None of the listed channels is the isotropic three-dimensional Newtonian kernel \(1/r\) (Fourier \(1/E\sim1/|q|^2\)):

| channel | exact object | decay |
|---|---|---|
| static plane response | \(G(n,m)\) above | \(0\) off the forward quadrant; \(G(n,0)=3/2^{n+1}\) exponential on the axis; \(G(n,n)=(3/2)\binom{2n}{n}4^{-n}\sim(3/2)/\sqrt{\pi n}=O(r^{-1/2})\) on the diagonal |
| time-integrated covariance | \(\sigma^2/\|1-\phi\|^2\) | IR \(1/(\mu\cdot k)^2\) in 2D, not \(1/E\) |
| co-moving impulse | 2D heat kernel above | \(O(1/t)\) at the peak, Gaussian off it |
| eight-corner visit kernel | \(G_\kappa(x)=3^{-\|n\|_1}\|n\|_1!/(n_1!n_2!n_3!)\) in octant \(\kappa\) | \(G_{\mathrm{sym}}(n,0,0)=3^{-n}/2\) exponential; one-corner \(G(n,n,n)=3^{-3n}(3n)!/(n!)^3\sim\sqrt{3}/(2\pi n)=3/(2\pi r)\) along the eight body-diagonal spines only |
| eight-corner static symbol | \(R_{\mathrm{sym}}(q)=\frac18\sum_\kappa 3/(3-\sum_j e^{-i\kappa_j q_j})\) | \(R_{\mathrm{sym}}(\lambda,0,0)=3/2\) for every \(\lambda\not\equiv0\pmod{2\pi}\); body-diagonal IR limit \(7/2\); neither is \(1/E\sim1/\lambda^2\) |

**(d)** The process is not equilibrium (\(P\neq P^*\) on an open set of modes). The static susceptibility \(\chi=1/(1-\phi)\) is not proportional to the equal-level covariance \(C=\sigma^2/(1-u)\): \(\chi\sigma^2/C=(1-u)/(1-\phi)\) is not equal to \(1-\phi^*\) and is not a real constant.

Finite claims are verified by `check.py` (fractions, Gaussian rationals on \(L=4\), cyclotomic on \(L=3\), sympy identities).

## (2) Steps

**Step 1 — generating function of the causal walk (PROVED; CHECKED as E2).** Each step of \(P\) is \((0,0)\), \((1,0)\) or \((0,1)\) with probability \(1/3\). After \(t\) steps the occupation of \((n,m)\) is the multinomial displayed in (b). The multinomial theorem gives \(\sum_{n,m}G_t(n,m)X^n Y^m=((1+X+Y)/3)^t\). Substituting \(X=e^{ik_1}\), \(Y=e^{ik_2}\) yields \(\widehat{G}_t(k)=\phi(k)^t\). Summing the geometric series in time with \(z=e^{iw}\) gives (a):
\[
R(k,w)=\sum_{t\ge0}\phi(k)^t e^{iwt}=\frac{1}{1-\phi(k)e^{iw}}.
\]
`check.py` expands the multinomial theorem through \(t=6\) as a polynomial identity and matches \(\phi^t\) to the finite-support DFT on every \(L=4\) mode for \(t<4\) (no wrap).

**Step 2 — 3D embedding and the \(E\)-identity (PROVED; CHECKED as E1).** With \(q_1=w+k_1\), \(q_2=w+k_2\), \(q_3=w\),
\[
e^{iw}\phi(k)=\frac{e^{iq_1}+e^{iq_2}+e^{iq_3}}{3},
\]
hence \(R=3/(3-\sum_j e^{iq_j})\). Expanding both sides of the claimed \(E\)-identity as trigonometric polynomials in \((k_1,k_2,w)\) gives zero (sympy `expand_complex`/`trigsimp`). Independently, \(1-u=(6-2\cos k_1-2\cos k_2-2\cos(k_1-k_2))/9\). Consequently
\[
\frac1E=\frac{|R|^2}{3\bigl(1+(1-u)|R|^2\bigr)},
\]
not a multiple of \(R\) or of \(|R|^2\).

**Step 3 — static \((I-P)^{-1}\) on the torus (PROVED; CHECKED as E3, E9).** On \((\mathbb{Z}/L)^2\), \(I-P\) annihilates constants and is invertible on the mean-zero subspace. For \(h=\delta_0-1/L^2\), \(\hat h(k)=1\) off zero, so \(\hat m(k)=1/(1-\phi_P(k))\) with \(\phi_P\) the eigenvalue of the real-space average under the DFT \(\hat m(k)=\sum_x m(x)e^{-ikx}\) (this is \(\phi(-k)\) of the note; the two conventions are conjugates). Gaussian elimination over \(\mathbb{Q}\) on \(L=4\) matches this DFT identically on all 15 nonzero modes. On \(L=3\) the same identity holds in \(\mathbb{Q}(\omega)\), \(\omega=e^{2\pi i/3}\). Real-space values on \(L=4\) are not a function of Euclidean \(r\) and are asymmetric under \((1,0)\leftrightarrow(-1,0)\) (wake).

**Step 4 — small-\(k\) jets and the co-moving Gaussian (PROVED as formal series / walk moments; CHECKED as E4; local CLT remainder ASSUMED).** One-step mean \(\mu=(1,1)/3\), covariance \(C=(1/9)\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\) (block 35's \(M\)), \(\det C=1/27\), \(C^{-1}=\begin{pmatrix}6&3\\3&6\end{pmatrix}\). Formal Taylor:
\[
1-\phi=-i(k_1+k_2)/3+(k_1^2+k_2^2)/6+O(k^3),\qquad 1-u=k^T Ck+O(k^4),
\]
and with \(\phi_{\mathrm{cm}}(k)=\phi(k)e^{-i(k_1+k_2)/3}\),
\[
1-\mathrm{Re}\,\phi_{\mathrm{cm}}=(k_1^2-k_1k_2+k_2^2)/9+O(k^3).
\]
The Fourier transform of \(\exp(-\tfrac12 k^T(tC)k)\) is exactly \((2\pi)^{-1}(\det(tC))^{-1/2}\exp(-\tfrac12 y^T(tC)^{-1}y)=3\sqrt{3}/(2\pi t)\exp(-3(y_1^2+y_2^2+y_1 y_2)/t)\). Identification of this with \(G_t(\mu t+y)\) at leading order is the local CLT for a finite-span lattice walk (ASSUMED as the standard local-CLT remainder \(o(t^{-1})\); not used for any finite identity).

**Step 5 — infinite-plane static Green function (PROVED; CHECKED as E8).** Spatial generating function of \(G=\sum_{t\ge0}G_t\):
\[
\sum_{n,m\ge0}G(n,m)X^n Y^m=\frac{1}{1-(1+X+Y)/3}=\frac{3}{2-X-Y}=\frac{3/2}{1-(X+Y)/2}.
\]
The binomial theorem expands the last as \(\frac32\sum_k 2^{-k}(X+Y)^k\), hence \(G(n,m)=\frac32\binom{n+m}{n}2^{-(n+m)}\) for \(n,m\ge0\) and \(G=0\) otherwise. Equivalently the negative-binomial sum \(\sum_p\binom{N+p}{p}(1/3)^p=(3/2)^{N+1}\) recovers the same formula. Thus \(G(0,0)=3/2\), \(G(n,0)=3/2^{n+1}\), \(G(n,n)=\frac32\binom{2n}{n}4^{-n}\). On the infinite plane \((I-P)G=\delta_0\), so a persistent bias of mass \(h\) at the origin produces \(m=hG\), and a pin \(\theta(0)=\alpha\) produces \(m=\alpha G/G(0)\). On a finite torus the only \((I-P)\)-harmonics are constants, so a Dirichlet pin is the constant field (CHECKED on \(L=4\)).

**Step 6 — time-integrated covariance (PROVED; CHECKED as E6).** Stationary \(C_s=\sigma^2\phi^s/(1-u)\) for \(s\ge0\) and \(C_{-s}=\sigma^2(\phi^*)^s/(1-u)\) (block 35 T1). The two-sided sum is
\[
\sum_{s\in\mathbb{Z}}C_s=\frac{\sigma^2}{1-u}\Bigl(\frac{1}{1-\phi}+\frac{\phi^*}{1-\phi^*}\Bigr)=\frac{\sigma^2}{|1-\phi|^2}.
\]
At \(w=0\), \(E=3(|1-\phi|^2+1-u)\), so the ratio of this channel to \(1/E\) is \(3(1+(1-u)/|1-\phi|^2)\), which takes at least three distinct rational values on the \(L=4\) modes (9, \(9/2\), and the \(w=0\) slice of \(1/E\) itself is not a constant multiple of \(C_0=1/(1-u)\) either: E10).

**Step 7 — fluctuation-response (PROVED; CHECKED as E7).** \(P\) is not self-adjoint: \(\mathrm{Im}\,\phi\neq0\) on 10 of 16 modes of \(L=4\). The static susceptibility is \(\chi(k)=1/(1-\phi(k))\), complex. The covariance is real, \(C(k)=\sigma^2/(1-u)\). The ratio \(\chi\sigma^2/C=(1-u)/(1-\phi)\) is not identically \(1-\phi^*\) (that would require \(\mathrm{Re}\,\phi=|\phi|^2\)). On \(L=4\) it is not a real constant, and \(|\chi|^2/C\) is not constant. Even a reversible discrete-time AR(1) (real \(\phi\)) would have \(C=\sigma^2\chi/(1+\phi)\), still \(k\)-dependent. There is no equilibrium FDR identifying \(\chi\) with \(C\).

**Step 8 — eight corners (PROVED; CHECKED as E5, E10).** Corner \(\kappa\) has \(\phi_\kappa(q)=\frac13\sum_j e^{-i\kappa_j q_j}\) and static symbol \(R_\kappa=1/(1-\phi_\kappa)=3/(3-\sum_j e^{-i\kappa_j q_j})\). Along a coordinate axis \(q=(\lambda,0,0)\), \(R_\kappa=3/(1-e^{-i\kappa_1\lambda})\), independent of \(\kappa_2,\kappa_3\). Averaging the two signs of \(\kappa_1\) gives \(3/2\) identically:
\[
\frac12\Bigl(\frac{3}{1-z^{-1}}+\frac{3}{1-z}\Bigr)=\frac32\qquad(z=e^{i\lambda}\neq1).
\]
Hence \(R_{\mathrm{sym}}(\lambda,0,0)=3/2\) for every axial lattice momentum. Meanwhile \(E(\lambda,0,0)=2(1-\cos\lambda)\), so \(1/E=1/(4\sin^2(\lambda/2))\) diverges as \(\lambda\to0\) and is never \(2/3\). The 3D Fourier of an isotropic \(c/|x|\) would diverge as \(c'/|q|^2\) along every path to the origin; a function whose Fourier transform tends to \(3/2\) along an axis cannot be \(c/|x|+o(1/|x|)\) with \(c\neq0\). Real-space: four of eight corners reach \((n,0,0)\) by \(n\) steps of \(\pm e_1\), each with amplitude \(3^{-n}\), so \(G_{\mathrm{sym}}(n,0,0)=3^{-n}/2\). Along the body diagonal the series of \(R_{\mathrm{sym}}(\lambda,\lambda,\lambda)\) at \(\lambda=0\) is the finite value \(7/2\) (CHECKED). The one-corner occupancy of \((n,n,n)\) is \(3^{-3n}(3n)!/(n!)^3\); Stirling's leading term \(\sqrt{3}/(2\pi n)=3/(2\pi r)\) (ASSUMED as Stirling with remainder; the exact factorial form is CHECKED for \(n=1..5\)) is a \(1/r\) peak along that ray only.

**Step 9 — no channel is isotropic \(1/r\) (PROVED from Steps 5–8; CHECKED as E10).** A 3D Newtonian potential is positive in every direction and has Fourier \(1/E\sim1/|q|^2\) along every path to \(q=0\).

- Static plane \(G\): identically zero on three quadrants; exponential on the forward axes; \(O(r^{-1/2})\) on the forward diagonal (central binomial). Replacement: a sharp causal wake in the predecessor cone, not \(1/r\).
- Time-integrated \(C\): a 2D symbol \(\sigma^2/|1-\phi|^2\sim9/(\mu\cdot k)^2\), not \(1/E\). Replacement: 2D directional \(1/k_\parallel^2\) (homogeneous of degree \(-2\) in two dimensions), whose real-space form is not \(1/r\) in three dimensions.
- Co-moving impulse: 2D heat kernel, peak \(O(1/t)\), Gaussian transverse. Replacement: diffusion, \(r^2\sim t\).
- Eight-corner visit kernel: exponential on the axes; \(1/r\) only as the 2D heat-kernel peak on the eight body-diagonal spines, exponentially small at any fixed angle off those spines (large-deviation rate of the multinomial). Replacement: eight directed heat spines, not an isotropic Coulomb kernel.
- Eight-corner static symbol: \(3/2\) on every axis, \(7/2\) along the body diagonal in the IR; not \(1/k^2\).

On \(L=4\), \(C_0/(1/E)\) and \(|R|^2/(1/E)\) each take at least three distinct rational values among the nonzero modes.

## (3) First failing step, if any

The route does not fail for the linear model. What is not proved: the local-CLT remainder in Step 4 (the exact Gaussian is the Fourier of the quadratic jet, not a bound on \(G_t-\)Gaussian); Stirling's remainder for \(G(n,n,n)\sim\sqrt{3}/(2\pi n)\); any nonlinear (sphere-menu) response; what a gravity-lane *construction* returns when this kernel is substituted for \(1/E\) (block 35's stated obligation of that lane).

## (4) What would finish it

A local-CLT expansion of \(G_t(\mu t+y)\) with explicit \(O(t^{-3/2})\) remainder (characteristic-function split, or Stirling on the multinomial with a Berry–Esseen bound on \(\mathbb{Z}^2\)); the same for \(G(n,n)\) and \(G(n,n,n)\). An exact description of the eight-corner *static plane* Green functions as eight copies of Step 5 in the eight coordinate frames, summed. The gravity node's construction run on \(R(k,w)\) or on \(G(n,m)\) in place of \(1/E\). The nonlinear sphere response at finite \(\beta\) (block 35 measured the covariance, not the sourced response).
