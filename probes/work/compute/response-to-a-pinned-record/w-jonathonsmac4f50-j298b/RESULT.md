response-to-a-pinned-record, independent run 2 of 2
worker w-jonathonsmac4f50-j298b (claude-opus-5), unit C-response-to-a-pinned-record-a2

The linear gain-one formation model on Z^(d+1), d = 2 and 3: one record at the origin is pinned to theta = 1 and
the mean is propagated, theta(x) = average of the d+1 predecessors {0, e_1, ..., e_d} one level down.
  overlap disclosure: I also ran C:two-point-function-response-table:a1, which measured this response in
  the sphere law by coupled pairs; here everything is the exact mean propagation and is independent of it.

(1) THE RESPONSE IS THE MULTINOMIAL (exact)
  d=2: propagating the mean to level 12 reproduces n!/(a_0! prod a_i!) (d+1)^-n at all 455 points exactly: True; every level sums to 1: True
  d=2: the support is the forward cone a_i >= 0 with sum a_i = n, i.e. 91 points at level 12; the response is zero everywhere else, at every level
  d=3: propagating the mean to level 12 reproduces n!/(a_0! prod a_i!) (d+1)^-n at all 1820 points exactly: True; every level sums to 1: True
  d=3: the support is the forward cone a_i >= 0 with sum a_i = n, i.e. 455 points at level 12; the response is zero everywhere else, at every level
  The propagation is the definition of the walk's n-step law, so the response at level n and plane position
  y = (a_1, ..., a_d) is P(S_n = y) with a_0 = n - sum_i a_i the number of held steps.

(2) ASYMPTOTICS (exact constants)
  the step is uniform on {0, e_1, .., e_d}: mean mu = (1,..,1)/(d+1), second moment I/(d+1),
  covariance Sigma = I/(d+1) - J/(d+1)^2, whose eigenvalues are 1/(d+1)^2 along (1,..,1) and 1/(d+1)
  with multiplicity d-1, so det Sigma = (d+1)^{-(d+1)}.
  d=2: det Sigma = 1/27 = (d+1)^-(d+1): True; local limit peak at y = n mu is (2 pi n)^(-d/2) (d+1)^((d+1)/2) = 3*sqrt(3)/(2*pi) n^(-2/2) = 0.826993 n^(-2/2)
  d=2: widths about the axis: sqrt(n/(d+1)) = 0.5774 sqrt(n) across it (multiplicity 1), sqrt(n)/(d+1) = 0.3333 sqrt(n) along it
  d=3: det Sigma = 1/256 = (d+1)^-(d+1): True; local limit peak at y = n mu is (2 pi n)^(-d/2) (d+1)^((d+1)/2) = 4*sqrt(2)/pi**(3/2) n^(-3/2) = 1.015898 n^(-3/2)
  d=3: widths about the axis: sqrt(n/(d+1)) = 0.5000 sqrt(n) across it (multiplicity 2), sqrt(n)/(d+1) = 0.2500 sqrt(n) along it
  d=2 exact multinomial at y = n mu against the constant: n=60: 1.363094e-02 vs 1.378322e-02 (ratio 0.9890)  n=120: 6.853432e-03 vs 6.891611e-03 (ratio 0.9945)  n=240: 3.436247e-03 vs 3.445806e-03 (ratio 0.9972)  n=480: 1.720512e-03 vs 1.722903e-03 (ratio 0.9986)  
  d=3 exact multinomial at y = n mu against the constant: n=60: 2.140804e-03 vs 2.185865e-03 (ratio 0.9794)  n=120: 7.648118e-04 vs 7.728199e-04 (ratio 0.9896)  n=240: 2.718137e-04 vs 2.732331e-04 (ratio 0.9948)  n=480: 9.635125e-05 vs 9.660249e-05 (ratio 0.9974)  
  The exact multinomials approach the local-limit constant from below, the ratio reaching 0.9986 (d = 2) and
  0.9974 (d = 3) at n = 480, consistent with the 1/n correction of the local limit theorem.

(3) THE EQUAL-LEVEL COVARIANCE
  d=2: 1 - u(k) = k^T M k + O(k^4) with M = Sigma (the same matrix): True
  d=2: C(x) = -(sigma^2/(2 pi sqrt(det M))) log sqrt(x^T M^-1 x) + const, det M = 1/27, coefficient 3*sqrt(3)/(2*pi) = 0.826993 sigma^2 (a logarithm: no finite C(infinity))
  d=3: 1 - u(k) = k^T M k + O(k^4) with M = Sigma (the same matrix): True
  d=3: C(x) = sigma^2/(4 pi sqrt(det M) sqrt(x^T M^-1 x)) with det M = 1/256, so C(x) -> 4/pi sigma^2/sqrt(x^T M^-1 x) = 1.273240 sigma^2/sqrt(x^T M^-1 x)

(4) HOW THE TWO DIFFER, AND WHY NO CONSTANT RELATES THEM
  support: the response is zero unless every a_i >= 0 (the forward cone); the covariance is supported on
  the whole plane and satisfies C(x) = C(-x), because its symbol |phi|^2 is even. One is one-sided in
  level time, the other is inversion symmetric: they differ before any constant is chosen.
  decay: the response at level n decays like n^(-d/2) with a Gaussian profile of width sqrt(n) about the
  drifting centre n mu; the equal-level covariance decays like log(1/r) (d = 2) or 1/r (d = 3) in space.
  no constant: summed over levels the response has symbol 1/(1 - phi) and the covariance sigma^2/(1-|phi|^2),
  so response = lambda covariance would force (1 - |phi(k)|^2)/(1 - phi(k)) = lambda sigma^2 at every k.
  d=2: that ratio takes the values k=(pi,pi) -> 2/3, k=(pi,0,..) -> 4/3, k=(pi/2,0,..) -> 2/3 - 2*I/3; all equal: False -> no single lambda can work (the fluctuation-response relation fails)
  d=3: that ratio takes the values k=(pi,pi,pi) -> 1/2, k=(pi,0,..) -> 3/2, k=(pi/2,0,..) -> 3/4 - 3*I/4; all equal: False -> no single lambda can work (the fluctuation-response relation fails)
  The ratio being complex at k = (pi/2, 0, ..) is already decisive: a real constant cannot equal a complex number,
  and the two real values (2/3 against 4/3 in d = 2, 1/2 against 3/2 in d = 3) settle it without any numerics.

(5) NUMERICAL FITS
  least squares over the forward cone: the best lambda in R = lambda C, and the spread of R/C
  d=2 (L=256, 72 points inside the cone): best lambda = 0.2336, relative residual 30.3%, R/C ranges 0.0976 to 0.3679 (a factor 3.8)
  d=2: the covariance at the mirrored points is 1.2642 to 3.4387 and C(x) - C(-x) is at most 6.66e-16 (inversion symmetric to machine precision), while the response at a fixed level n < L is exactly zero there - see the next line. Summed over all levels on a torus the cone wraps after L levels, so only the fixed-level statement is one-sided.
  d=2: at the single level n=8, best lambda = 0.0081 with relative residual 81.4%, and the response at the mirrored points is exactly 0.0e+00 against a covariance of 1.2642 or more
  d=3 (L=64, 520 points inside the cone): best lambda = 1.3919, relative residual 51.6%, R/C ranges 0.1586 to 24.0356 (a factor 151.5)
  d=3: the covariance at the mirrored points is 0.0022 to 0.4367 and C(x) - C(-x) is at most 5.55e-17 (inversion symmetric to machine precision), while the response at a fixed level n < L is exactly zero there - see the next line. Summed over all levels on a torus the cone wraps after L levels, so only the fixed-level statement is one-sided.
  d=3: at the single level n=8, best lambda = 0.0707 with relative residual 86.7%, and the response at the mirrored points is exactly 0.0e+00 against a covariance of 0.0022 or more

(6) READING
  The response to a pinned record is the multinomial law of the forward walk: supported on the forward cone,
  peaked on the drifting axis n(1,..,1)/(d+1), decaying as n^(-d/2) with width sqrt(n/(d+1)) across the axis and
  sqrt(n)/(d+1) along it. The equal-level covariance is the plane's Green function - a logarithm in d = 2, a 1/r
  law in d = 3 - supported everywhere and inversion symmetric to machine precision.
  They differ in support, in symmetry and in decay law, and the exact Fourier ratio (1 - |phi|^2)/(1 - phi) is not
  constant (it is not even real), so no lambda makes response = lambda x covariance. The best least-squares lambda
  leaves 30 percent (d = 2) and 52 percent (d = 3) residual over the cone, and 81 and 87 percent at a single level.
  The equilibrium fluctuation-response relation fails, which is what the task expects; no HIT.
