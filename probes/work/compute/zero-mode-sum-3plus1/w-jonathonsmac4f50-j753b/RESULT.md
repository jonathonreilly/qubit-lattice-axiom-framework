zero-mode-sum-3plus1, independent run 2 of 2
worker w-jonathonsmac4f50-j753b (claude-opus-5), unit C-zero-mode-sum-3plus1-a2

G := (2 pi)^-3 int over [-pi,pi]^3 of dk/(1 - |phi(k)|^2),  phi(k) = (1 + e^{ik1} + e^{ik2} + e^{ik3})/4
(the backward, four-predecessor plane walk of the 3+1 event lattice).

(1) THE SERIES (exact)
  0 <= u = |phi|^2 < 1 off k = 0, so 1/(1 - u) = sum_n u^n and, by Parseval,
      (2 pi)^-3 int u^n = sum_x p_n(x)^2 = P_n,
  the probability that the difference of two independent plane walks (steps 0, e1, e2, e3, each 1/4) is back at the origin
  after n steps.  The difference walk has 16 equally likely steps: 4 null, 6 of the form +-e_j, 6 of the form e_i - e_j.
  Exact values come from
      P_n = (n!)^2 16^-n [t^n] (sum_k t^k/(k!)^2)^4
  computed as one integer polynomial power (n <= 400, exact rationals):
      P_0 = 1
      P_1 = 1/4          (the 4 null steps of 16)
      P_2 = 7/64         (28 two-step returns of 256)
      P_10 = 0.010957
      P_100 = 3.578e-04
      P_400 = 4.485e-05
  partial sum to n = 400: 1.756998

(2) THE TAIL AND THE BRACKET
  Rigorous: P_n <= max_x p_n(x), and Robbins' Stirling bounds at the balanced multinomial give
      max_x p_n(x) <= 16/(2 pi (n - 3))^{3/2}   for n >= 4
  (max_x p_n is non-increasing in n, which covers the non-multiples of 4).  This is checked against every exact P_n.
  Hence sum_{n > 400} P_n <= 0.1020 and
      G in [1.7570, 1.8590]    (rigorous)
  Local limit: n^{3/2} P_n -> 1/((2 pi)^{3/2} sqrt(det Sigma)) with Sigma = 2 Cov(step) = 2M, M = (1/4)I - (1/16)J,
  det Sigma = 1/32, so the constant is 4 sqrt2/(2 pi)^{3/2} = 0.359174.  The exact values give
      n^{3/2} P_n = 0.3452 (n = 10), 0.3578 (n = 100), 0.3588 (n = 400), i.e. -0.09 % at n = 400,
  increasing in n and below the constant on the whole range.  With that,
      0.03584 <= tail <= 0.03592   and   G in [1.79284, 1.79292]
  (numerical, because the monotonicity is verified only on 1 <= n <= 400).  Take G = 1.7929.

(3) THE SPIN-WAVE PLATEAU
  |m| ~ 1 - sigma^2 G with sigma^2 = A(4 beta)/(4 beta), A(x) = coth x - 1/x:
      beta = 1    sigma^2 = 0.1877   |m| = 0.6635
      beta = 1.5  sigma^2 = 0.1389   |m| = 0.7510
      beta = 2    sigma^2 = 0.1094   |m| = 0.8039
      beta = 3    sigma^2 = 0.0764   |m| = 0.8630
      beta = 6    sigma^2 = 0.0399   |m| = 0.9284
      beta = 12   sigma^2 = 0.0204   |m| = 0.9634
  Against the logs (X:formation-3plus1-sphere-memory, four predecessors): only one run is logged,
      beta = 6, L = 32: measured plateau 0.9242 against the spin-wave 0.9284, i.e. -0.45 %.
  That is the expected agreement at beta >= 6.  The other couplings have no logged run yet.

(4) THE 2+1 CONTRAST
  The same sum on the L x L plane, phi = (1 + e^{ik1} + e^{ik2})/3:
      L = 16: 2.6443   32: 3.2186   64: 3.7921   128: 4.3654   256: 4.9386   512: 5.5119
  differences per doubling: 0.8286, 0.8274, 0.8271, 0.8270, 0.8270, i.e. growth 0.827 per log 2, a log L divergence with no
  finite limit (0.827/log 2 = 1.193 per log L).

READING
  The expectation holds: G is finite in 3+1 (1.7929), so the spin-wave plateau 1 - sigma^2 G stays positive at every coupling
  and memory survives, while the same sum in 2+1 grows like log L and the plateau is driven to zero.
  No HIT.
