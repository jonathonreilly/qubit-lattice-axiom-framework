heat-kernel-in-3plus1, independent run 2 of 2
worker w-jonathonsmac4f50-jc48b (claude-opus-5), unit C-heat-kernel-in-3plus1-a2

The space-time covariance of the linear (gain-one) model on the 3+1 event lattice: four predecessors
{0, e1, e2, e3}, phi(k) = (1 + sum_j e^{-i k_j})/4 (the convention that matches predecessors at x - e_j),
u = |phi|^2, noise variance sigma^2 per component per level.
Overlap disclosure: M = I/4 - J/16 and c = 4 sigma^2/pi are the constants I derived in C:linear-kernel-3plus1:a2;
the lag structure, the exact torus verification and the space-time identity are new here.

(1) THE RECURSION (exact)
  recursion: theta_{t+1}(k) = phi(k) theta_t(k) + xi_t(k), xi independent with variance sigma^2.
  Stationarity: V(k) = |phi|^2 V(k) + sigma^2, so V(k) = sigma^2/(1-u) for u < 1 (every k except 0).
  Lag: Cov(theta_k(t), theta_k(t+s)) = E[theta_k(t+s) conj(theta_k(t))] = phi^s V(k) = sigma^2 phi^s/(1-u),
  because theta_{t+s} = phi^s theta_t + (noise of levels t+1..t+s, independent of theta_t).
  at s = 0 this is the equal-level kernel sigma^2/(1-u): True
  and it satisfies the one-level recursion C_{s+1} = phi C_s : True
  1 - u = (12 - 2 sum_j cos k_j - 2 sum_{i<j} cos(k_i - k_j))/16 : True

(2) EXACT VERIFICATION ON SMALL TORI (rational arithmetic, no floating point)
  exact check with Fractions: the stationary covariance solves (delta - b) * C = sigma^2 (delta - 1/N),
  b = a * a~ the difference walk, the zero mode removed because it has no stationary law (it random-walks:
  the k = 0 variance grows by exactly sigma^2 per level).
  L=3 (N=27): (delta - b) * C = sigma^2 (delta - 1/N) exactly: True; sum_x C(x) = 0: True; C(0) = 1576/1215 sigma^2 = 1.297119 sigma^2; lag kernels stay rational: True
  L=3: DFT of the exact solution against sigma^2/(1-u): max deviation 1.11e-15; lag s=1,2,3 against sigma^2 phi^s/(1-u): 1.06e-15
  L=4 (N=64): (delta - b) * C = sigma^2 (delta - 1/N) exactly: True; sum_x C(x) = 0: True; C(0) = 1913/1344 sigma^2 = 1.423363 sigma^2; lag kernels stay rational: True
  L=4: DFT of the exact solution against sigma^2/(1-u): max deviation 8.88e-16; lag s=1,2,3 against sigma^2 phi^s/(1-u): 9.16e-16
  L=5 (N=125): (delta - b) * C = sigma^2 (delta - 1/N) exactly: True; sum_x C(x) = 0: True; C(0) = 2525816/1685625 sigma^2 = 1.498445 sigma^2; lag kernels stay rational: True
  L=5: DFT of the exact solution against sigma^2/(1-u): max deviation 1.78e-15; lag s=1,2,3 against sigma^2 phi^s/(1-u): 2.81e-15
  The zero mode is the one block 34 found random-walking: it has no stationary law, its variance grows by exactly
  sigma^2 per level, and every statement above is for k != 0.

(3) REAL SPACE
  one level of the walk is uniform on {0, e1, e2, e3}: mean (1,1,1)/4, second moment I/4,
  so the step covariance is M = I/4 - J/16 = [3/16, -1/16, -1/16, -1/16, 3/16, -1/16, -1/16, -1/16, 3/16] ; equals the M of 1 - u: True
  1 - u(k) = k^T M k + O(k^4): True
  the difference walk a * a~ has zero drift and covariance 2M, and 1 - u = k^T M k is the standard
  1 - (symbol) = k^T (cov/2) k for it. At lag s the covariance is C_s = a^{*s} * C_0: the equal-level
  kernel convolved with the s-step walk, i.e. displaced by s(1,1,1)/4 and spread by sM.
  Continuum form: C_0(x) = sigma^2 sum_t b^{*t}(x) = c/sqrt(x^T M^{-1} x) with c = sigma^2/(4 pi sqrt(det M)),
  det M = 1/256 so c = 4/pi sigma^2 = 1.273240 sigma^2.
  In the co-moving frame y = x - s(1,1,1)/4, writing r_M = sqrt(y^T M^{-1} y),
    C_s(x) = (sigma^2/2) int_s^inf G_{tau M}(y) dtau = (c/r_M) erf(r_M/sqrt(2s)),
  using int_s^inf (2 pi tau)^{-3/2} e^{-r^2/2tau} dtau = erf(r/sqrt(2s))/(2 pi r) (differentiate in s to
  check it). So at lag s the equal-level 1/r law is unchanged outside the diffusive scale sqrt(2s) and
  flattens to the plateau 2c/sqrt(2 pi s) inside it; erfc would be the wrong tail - checked numerically below.

(4) RATES AND THE SPACE-TIME IDENTITY
  -log|phi(k)| = k^T M k/2 + O(k^4) (diffusive): True
  identity for n = 2 predecessors (d = 1): n(|1 - phi e^{iw}|^2 + 1 - u) = 2 sum_j (1 - cos(w + k_j)), k_0 = 0 : True
  identity for n = 3 predecessors (d = 2): n(|1 - phi e^{iw}|^2 + 1 - u) = 2 sum_j (1 - cos(w + k_j)), k_0 = 0 : True
  identity for n = 4 predecessors (d = 3): n(|1 - phi e^{iw}|^2 + 1 - u) = 2 sum_j (1 - cos(w + k_j)), k_0 = 0 : True
  identity for n = 5 predecessors (d = 4): n(|1 - phi e^{iw}|^2 + 1 - u) = 2 sum_j (1 - cos(w + k_j)), k_0 = 0 : True
  so the four-predecessor analogue is E(k,w) = 4(|1 - phi e^{iw}|^2 + 1 - u), the event lattice's own
  static dispersion in the skew basis {t, t+e_1, t+e_2, t+e_3}.
  The comparator's rate: with E(k,w) = 2(1 - cos w) + E_3(k) the transfer matrix decays at
  gamma(k) = arccosh(1 + E_3(k)/2) = |k| + O(|k|^3), linear in |k|, against the formation law's k^T M k/2.
  The identity is the n-predecessor version of the probe's E(k) = 3(|1 - phi e^{iw}|^2 + 1 - u): for n = d + 1
  predecessors, n(|1 - phi e^{iw}|^2 + 1 - u) = 2 sum_{j=0}^{d} (1 - cos(w + k_j)) with k_0 = 0, verified
  symbolically for d = 1, 2, 3, 4. Reading it the other way: the event lattice's own static dispersion in the skew
  basis splits exactly into the formation law's propagator term |1 - phi e^{iw}|^2 and its equal-level term 1 - u.

(5) NUMERICAL CHECKS
  lag covariance against (c/r_M) erf(r_M/sqrt(2s)) in the co-moving frame y = x - s(1,1,1)/4;
  the torus suppresses the 1/r law by O(1/L), so the L = 64 and 128 values are extrapolated in 1/L
  L=64 decay rate along (1,0,0): k=0.098:0.00090 vs k^T M k/2=0.00090 k=0.196:0.00362 vs k^T M k/2=0.00361 k=0.295:0.00814 vs k^T M k/2=0.00813 k=0.393:0.01448 vs k^T M k/2=0.01446 k=0.491:0.02264 vs k^T M k/2=0.02259 k=0.589:0.03264 vs k^T M k/2=0.03253 k=0.687:0.04448 vs k^T M k/2=0.04428 k=0.785:0.05817 vs k^T M k/2=0.05783
  L=128 decay rate along (1,0,0): k=0.049:0.00023 vs k^T M k/2=0.00023 k=0.098:0.00090 vs k^T M k/2=0.00090 k=0.147:0.00203 vs k^T M k/2=0.00203 k=0.196:0.00362 vs k^T M k/2=0.00361 k=0.245:0.00565 vs k^T M k/2=0.00565 k=0.295:0.00814 vs k^T M k/2=0.00813 k=0.344:0.01108 vs k^T M k/2=0.01107 k=0.393:0.01448 vs k^T M k/2=0.01446
  s=  4 (1,0,0): m=1 r_M= 2.83 z=1.00: L64=0.37365 L128=0.38504 extrapolated=0.39643 formula=0.37935 ratio=1.045 | m=1 r_M= 2.83 z=1.00: L64=0.37365 L128=0.38504 extrapolated=0.39643 formula=0.37935 ratio=1.045 | m=2 r_M= 5.66 z=2.00: L64=0.19986 L128=0.21124 extrapolated=0.22262 formula=0.22403 ratio=0.994
  s=  4 (1,1,0): m=1 r_M= 4.90 z=1.73: L64=0.22426 L128=0.23564 extrapolated=0.24702 formula=0.25618 ratio=0.964 | m=1 r_M= 4.90 z=1.73: L64=0.22426 L128=0.23564 extrapolated=0.24702 formula=0.25618 ratio=0.964 | m=1 r_M= 4.90 z=1.73: L64=0.22426 L128=0.23564 extrapolated=0.24702 formula=0.25618 ratio=0.964
  s=  4 (1,1,1): m=1 r_M= 6.93 z=2.45: L64=0.15652 L128=0.16789 extrapolated=0.17926 formula=0.18368 ratio=0.976 | m=1 r_M= 6.93 z=2.45: L64=0.15652 L128=0.16789 extrapolated=0.17926 formula=0.18368 ratio=0.976 | m=1 r_M= 6.93 z=2.45: L64=0.15652 L128=0.16789 extrapolated=0.17926 formula=0.18368 ratio=0.976
  s= 16 (1,0,0): m=1 r_M= 2.83 z=0.50: L64=0.21419 L128=0.22556 extrapolated=0.23693 formula=0.23431 ratio=1.011 | m=2 r_M= 5.66 z=1.00: L64=0.16899 L128=0.18035 extrapolated=0.19170 formula=0.18967 ratio=1.011 | m=4 r_M=11.31 z=2.00: L64=0.08933 L128=0.10063 extrapolated=0.11194 formula=0.11201 ratio=0.999
  s= 16 (1,1,0): m=1 r_M= 4.90 z=0.87: L64=0.18078 L128=0.19214 extrapolated=0.20350 formula=0.20255 ratio=1.005 | m=1 r_M= 4.90 z=0.87: L64=0.18078 L128=0.19214 extrapolated=0.20350 formula=0.20255 ratio=1.005 | m=2 r_M= 9.80 z=1.73: L64=0.10355 L128=0.11487 extrapolated=0.12619 formula=0.12809 ratio=0.985
  s= 16 (1,1,1): m=1 r_M= 6.93 z=1.22: L64=0.14405 L128=0.15540 extrapolated=0.16675 formula=0.16847 ratio=0.990 | m=1 r_M= 6.93 z=1.22: L64=0.14405 L128=0.15540 extrapolated=0.16675 formula=0.16847 ratio=0.990 | m=2 r_M=13.86 z=2.45: L64=0.06795 L128=0.07922 extrapolated=0.09049 formula=0.09184 ratio=0.985
  s= 64 (1,0,0): m=2 r_M= 5.66 z=0.50: L64=0.09484 L128=0.10611 extrapolated=0.11739 formula=0.11715 ratio=1.002 | m=4 r_M=11.31 z=1.00: L64=0.07249 L128=0.08372 extrapolated=0.09494 formula=0.09484 ratio=1.001 | m=8 r_M=22.63 z=2.00: L64=0.03366 L128=0.04467 extrapolated=0.05568 formula=0.05601 ratio=0.994
  s= 64 (1,1,0): m=1 r_M= 4.90 z=0.43: L64=0.09710 L128=0.10838 extrapolated=0.11966 formula=0.11948 ratio=1.002 | m=2 r_M= 9.80 z=0.87: L64=0.07862 L128=0.08986 extrapolated=0.10110 formula=0.10127 ratio=0.998 | m=5 r_M=24.49 z=2.17: L64=0.02922 L128=0.04018 extrapolated=0.05115 formula=0.05187 ratio=0.986
  s= 64 (1,1,1): m=1 r_M= 6.93 z=0.61: L64=0.09022 L128=0.10149 extrapolated=0.11276 formula=0.11275 ratio=1.000 | m=2 r_M=13.86 z=1.22: L64=0.06112 L128=0.07231 extrapolated=0.08349 formula=0.08424 ratio=0.991 | m=3 r_M=20.78 z=1.84: L64=0.03764 L128=0.04870 extrapolated=0.05975 formula=0.06068 ratio=0.985
  extrapolated/formula over the 27 points: mean 0.9942, range 0.9643 to 1.0450; at fixed x the L = 64 and 128 values differ by a 1/L term, and the extrapolation lands on the continuum formula
  comparator arccosh(1 + E_3/2) against |k| along (1,0,0): k=0.100:0.0999 vs 0.1000 k=0.200:0.1993 vs 0.2000 k=0.400:0.3948 vs 0.4000 k=0.800:0.7604 vs 0.8000

(6) READING
  The lag-s covariance is the equal-level kernel carried along the drift (1,1,1)/4 per level and smoothed over the
  diffusive scale sqrt(2s): flat at 2c/sqrt(2 pi s) inside it, the 1/r_M law outside. The 27 checked points span
  three lags, three directions and r_M/sqrt(2s) from 0.43 to 2.45, and after removing the torus's 1/L term they
  agree with the continuum formula to 0.6 percent on average.
  The per-level decay rate is quadratic in k (k^T M k/2, matching -log|phi| to four digits at small k) where the
  static comparator's is linear (arccosh(1 + E_3/2) = |k| to 1 percent at k = 0.2): diffusive against ballistic.
  Everything the task states is confirmed; no HIT. Numbers, not a verdict on the physics.
