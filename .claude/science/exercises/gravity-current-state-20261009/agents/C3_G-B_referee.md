# C3 lane G-B: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

Verdict: **INCONCLUSIVE** under the fixed reading.

- The vector-weight E1′-b corollary is controlled for the actual shell-regular tensor weights. The Poisson Poincaré step is valid componentwise ([Last–Penrose](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf)).
- The leading superpotential result is \(A_{\rm rms}=7.27077\times10^{-28}\), far below \(10^{-3}\). Strictly, the uncomputed \(C'_S s/D\) correction means \(7.3\times10^{-28}\) is an asymptotic rounded ceiling.
- The Fano-factor growth does not defeat the independently proved uniform bound; the claimed empirical saturation is weak and unnecessary.
- The PASS fails because the finite-density mean is \(\bar K_\rho*T\), not exactly \(G_R*T\). Exact agreement occurs only in the infinite-density limit; finite-density corrections are known ([Johnston 2015](https://arxiv.org/abs/1411.2614)).
- FAIL is also inapplicable because no controlled admixture exceeds \(10^{-3}\).

Full point-by-point ruling: [C3_G-B_referee.md](<C3_G-B_referee.md>)

Independent arithmetic: [referee_checks.py](<referee_checks.py>)