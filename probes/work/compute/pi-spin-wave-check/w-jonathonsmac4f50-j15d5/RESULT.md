pi-spin-wave-check, independent run 1 of 2
worker w-jonathonsmac4f50-j15d5 (claude-opus-5), unit C-pi-spin-wave-check-a1

The reversible law pi(s) proportional to exp(sum_x log Z(S_x)), Z(S) = 4 pi sinh(beta|S|)/(beta|S|), with S_x the
sum of the n records in a symmetric neighbourhood; here n = 7, the light cone {0, +-e_1, +-e_2, +-e_3} in three
space dimensions. Question: do its spin waves reproduce the formation kernel sigma^2/(1 - phi^2)?

(1) THE EXPANSION (exact)
  d/da log Z(a) = beta/tanh(a*beta) - 1/a = beta A(beta a) with A(x) = coth x - 1/x: True
  write s_x = (theta_x, sqrt(1 - |theta_x|^2)), theta in R^2. Then for a symmetric neighbourhood of size n
    |S_x| = n - (1/2) sum_{y in N(x)} |theta_y|^2 + (1/2n) |sum_{y in N(x)} theta_y|^2 + O(theta^4),
  and since |S_x| - n is already second order, only the first derivative of log Z contributes:
    sum_x log Z(S_x) = const + beta A(n beta) sum_x (|S_x| - n) + O(theta^4).
  In Fourier (phi(k) = (1/n) sum_{offsets} e^{i k.delta}, real for a symmetric set) the bracket is
    (1/n)|n phi|^2 - n = -n (1 - phi^2), so  -log pi = (1/2N) sum_k lambda(k) |theta(k)|^2 with
    lambda(k) = beta A(n beta) n (1 - phi(k)^2)    -> the coefficient is beta' = beta A(n beta), not A(n beta)
  The claimed formation kernel is sigma^2/(1 - phi^2) with sigma^2 = A(n beta)/(n beta), i.e. an inverse
  stiffness n beta (1 - phi^2)/A(n beta). Their ratio is
    [1/lambda] / [sigma^2/(1-phi^2)] = 1/A(n beta)^2, the same in every mode,
  and 1/A(x)^2 = 1 + 2/x + O(1/x^2), so the two agree to leading order in 1/(n beta) and differ at the
  relative order 2/(n beta) - the same order as the quartic terms dropped from the expansion.
  exactly A(x) = 1 - 1/x + 2/(e^{2x} - 1): True
  so up to e^{-2x}, 1/A(x)^2 = 1/(1 - 1/x)^2 = 1 + 2/x + 3/x^2 + ... : True
    at n beta = 14: A = 0.928571, 1/A^2 = 1.159763 (1 + 2/(n beta) = 1.142857)
    at n beta = 42: A = 0.976190, 1/A^2 = 1.049375 (1 + 2/(n beta) = 1.047619)

(2) THE SPHERE'S OWN MEASURE
  the uniform measure on the sphere is dtheta/sqrt(1 - |theta|^2), which adds +|theta_x|^2/2 to log pi,
  i.e. subtracts exactly 1 from lambda(k) in the coordinates theta. With it,
    lambda_measure(k) = beta A(n beta) n (1 - phi(k)^2) - 1,
  which matters only where 1 - phi^2 is not small: it is a large-k correction, not a long-wave one.

(3) THE NUMERICAL HESSIAN, MODE BY MODE
  neighbourhood [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)] of size n = 7
  L=4 beta=2.0 without the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.928571, 1/A^2=1.1598
    k=2pi(0, 0, 1)/4: 1-phi^2=0.4898 Hessian lambda=6.36734 expansion=6.36735 (ratio 1.00000) | 1/lambda=0.15705 claimed kernel=0.13542 (ratio 1.15976)
    k=2pi(0, 0, 2)/4: 1-phi^2=0.8163 Hessian lambda=10.61224 expansion=10.61224 (ratio 1.00000) | 1/lambda=0.09423 claimed kernel=0.08125 (ratio 1.15976)
    k=2pi(0, 1, 1)/4: 1-phi^2=0.8163 Hessian lambda=10.61225 expansion=10.61224 (ratio 1.00000) | 1/lambda=0.09423 claimed kernel=0.08125 (ratio 1.15976)
    k=2pi(0, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=12.73470 expansion=12.73469 (ratio 1.00000) | 1/lambda=0.07853 claimed kernel=0.06771 (ratio 1.15976)
    k=2pi(0, 2, 2)/4: 1-phi^2=0.9796 Hessian lambda=12.73470 expansion=12.73469 (ratio 1.00000) | 1/lambda=0.07853 claimed kernel=0.06771 (ratio 1.15976)
    k=2pi(1, 1, 1)/4: 1-phi^2=0.9796 Hessian lambda=12.73469 expansion=12.73469 (ratio 1.00000) | 1/lambda=0.07853 claimed kernel=0.06771 (ratio 1.15976)
    k=2pi(1, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=12.73470 expansion=12.73469 (ratio 1.00000) | 1/lambda=0.07853 claimed kernel=0.06771 (ratio 1.15976)
    k=2pi(1, 2, 2)/4: 1-phi^2=0.8163 Hessian lambda=10.61224 expansion=10.61224 (ratio 1.00000) | 1/lambda=0.09423 claimed kernel=0.08125 (ratio 1.15976)
    k=2pi(2, 2, 2)/4: 1-phi^2=0.4898 Hessian lambda=6.36734 expansion=6.36735 (ratio 1.00000) | 1/lambda=0.15705 claimed kernel=0.13542 (ratio 1.15976)
  L=4 beta=2.0 without the measure term: Hessian/expansion over the 9 modes 0.999999 to 1.000000; (1/lambda)/claimed kernel 1.15976 to 1.15976, against 1/A^2 = 1.15976
  L=4 beta=2.0 with the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.928571, 1/A^2=1.1598
    k=2pi(0, 0, 1)/4: 1-phi^2=0.4898 Hessian lambda=5.36734 expansion=5.36735 (ratio 1.00000) | 1/lambda=0.18631 claimed kernel=0.13542 (ratio 1.37584)
    k=2pi(0, 0, 2)/4: 1-phi^2=0.8163 Hessian lambda=9.61224 expansion=9.61224 (ratio 1.00000) | 1/lambda=0.10403 claimed kernel=0.08125 (ratio 1.28042)
    k=2pi(0, 1, 1)/4: 1-phi^2=0.8163 Hessian lambda=9.61225 expansion=9.61224 (ratio 1.00000) | 1/lambda=0.10403 claimed kernel=0.08125 (ratio 1.28042)
    k=2pi(0, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=11.73470 expansion=11.73469 (ratio 1.00000) | 1/lambda=0.08522 claimed kernel=0.06771 (ratio 1.25859)
    k=2pi(0, 2, 2)/4: 1-phi^2=0.9796 Hessian lambda=11.73470 expansion=11.73469 (ratio 1.00000) | 1/lambda=0.08522 claimed kernel=0.06771 (ratio 1.25859)
    k=2pi(1, 1, 1)/4: 1-phi^2=0.9796 Hessian lambda=11.73469 expansion=11.73469 (ratio 1.00000) | 1/lambda=0.08522 claimed kernel=0.06771 (ratio 1.25860)
    k=2pi(1, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=11.73470 expansion=11.73469 (ratio 1.00000) | 1/lambda=0.08522 claimed kernel=0.06771 (ratio 1.25860)
    k=2pi(1, 2, 2)/4: 1-phi^2=0.8163 Hessian lambda=9.61224 expansion=9.61224 (ratio 1.00000) | 1/lambda=0.10403 claimed kernel=0.08125 (ratio 1.28042)
    k=2pi(2, 2, 2)/4: 1-phi^2=0.4898 Hessian lambda=5.36734 expansion=5.36735 (ratio 1.00000) | 1/lambda=0.18631 claimed kernel=0.13542 (ratio 1.37584)
  L=4 beta=2.0 with the measure term: Hessian/expansion over the 9 modes 0.999999 to 1.000000; (1/lambda)/claimed kernel 1.25859 to 1.37584
  L=4 beta=6.0 without the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.976190, 1/A^2=1.0494
    k=2pi(0, 0, 1)/4: 1-phi^2=0.4898 Hessian lambda=20.08164 expansion=20.08163 (ratio 1.00000) | 1/lambda=0.04980 claimed kernel=0.04745 (ratio 1.04937)
    k=2pi(0, 0, 2)/4: 1-phi^2=0.8163 Hessian lambda=33.46941 expansion=33.46939 (ratio 1.00000) | 1/lambda=0.02988 claimed kernel=0.02847 (ratio 1.04937)
    k=2pi(0, 1, 1)/4: 1-phi^2=0.8163 Hessian lambda=33.46941 expansion=33.46939 (ratio 1.00000) | 1/lambda=0.02988 claimed kernel=0.02847 (ratio 1.04937)
    k=2pi(0, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=40.16329 expansion=40.16327 (ratio 1.00000) | 1/lambda=0.02490 claimed kernel=0.02373 (ratio 1.04937)
    k=2pi(0, 2, 2)/4: 1-phi^2=0.9796 Hessian lambda=40.16329 expansion=40.16327 (ratio 1.00000) | 1/lambda=0.02490 claimed kernel=0.02373 (ratio 1.04937)
    k=2pi(1, 1, 1)/4: 1-phi^2=0.9796 Hessian lambda=40.16326 expansion=40.16327 (ratio 1.00000) | 1/lambda=0.02490 claimed kernel=0.02373 (ratio 1.04938)
    k=2pi(1, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=40.16326 expansion=40.16327 (ratio 1.00000) | 1/lambda=0.02490 claimed kernel=0.02373 (ratio 1.04938)
    k=2pi(1, 2, 2)/4: 1-phi^2=0.8163 Hessian lambda=33.46938 expansion=33.46939 (ratio 1.00000) | 1/lambda=0.02988 claimed kernel=0.02847 (ratio 1.04938)
    k=2pi(2, 2, 2)/4: 1-phi^2=0.4898 Hessian lambda=20.08162 expansion=20.08163 (ratio 1.00000) | 1/lambda=0.04980 claimed kernel=0.04745 (ratio 1.04938)
  L=4 beta=6.0 without the measure term: Hessian/expansion over the 9 modes 0.999999 to 1.000001; (1/lambda)/claimed kernel 1.04937 to 1.04938, against 1/A^2 = 1.04938
  L=4 beta=6.0 with the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.976190, 1/A^2=1.0494
    k=2pi(0, 0, 1)/4: 1-phi^2=0.4898 Hessian lambda=19.08164 expansion=19.08163 (ratio 1.00000) | 1/lambda=0.05241 claimed kernel=0.04745 (ratio 1.10437)
    k=2pi(0, 0, 2)/4: 1-phi^2=0.8163 Hessian lambda=32.46940 expansion=32.46939 (ratio 1.00000) | 1/lambda=0.03080 claimed kernel=0.02847 (ratio 1.08169)
    k=2pi(0, 1, 1)/4: 1-phi^2=0.8163 Hessian lambda=32.46940 expansion=32.46939 (ratio 1.00000) | 1/lambda=0.03080 claimed kernel=0.02847 (ratio 1.08169)
    k=2pi(0, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=39.16329 expansion=39.16327 (ratio 1.00000) | 1/lambda=0.02553 claimed kernel=0.02373 (ratio 1.07617)
    k=2pi(0, 2, 2)/4: 1-phi^2=0.9796 Hessian lambda=39.16329 expansion=39.16327 (ratio 1.00000) | 1/lambda=0.02553 claimed kernel=0.02373 (ratio 1.07617)
    k=2pi(1, 1, 1)/4: 1-phi^2=0.9796 Hessian lambda=39.16326 expansion=39.16327 (ratio 1.00000) | 1/lambda=0.02553 claimed kernel=0.02373 (ratio 1.07617)
    k=2pi(1, 1, 2)/4: 1-phi^2=0.9796 Hessian lambda=39.16326 expansion=39.16327 (ratio 1.00000) | 1/lambda=0.02553 claimed kernel=0.02373 (ratio 1.07617)
    k=2pi(1, 2, 2)/4: 1-phi^2=0.8163 Hessian lambda=32.46938 expansion=32.46939 (ratio 1.00000) | 1/lambda=0.03080 claimed kernel=0.02847 (ratio 1.08169)
    k=2pi(2, 2, 2)/4: 1-phi^2=0.4898 Hessian lambda=19.08162 expansion=19.08163 (ratio 1.00000) | 1/lambda=0.05241 claimed kernel=0.04745 (ratio 1.10437)
  L=4 beta=6.0 with the measure term: Hessian/expansion over the 9 modes 0.999999 to 1.000001; (1/lambda)/claimed kernel 1.07617 to 1.10437
  L=6 beta=2.0 without the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.928571, 1/A^2=1.1598
  L=6 beta=2.0 without the measure term: Hessian/expansion over the 19 modes 0.999996 to 1.000001; (1/lambda)/claimed kernel 1.15976 to 1.15977, against 1/A^2 = 1.15976
  L=6 beta=2.0 with the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.928571, 1/A^2=1.1598
  L=6 beta=2.0 with the measure term: Hessian/expansion over the 19 modes 0.999996 to 1.000001; (1/lambda)/claimed kernel 1.25641 to 1.63333
  L=6 beta=6.0 without the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.976190, 1/A^2=1.0494
  L=6 beta=6.0 without the measure term: Hessian/expansion over the 19 modes 0.999999 to 1.000001; (1/lambda)/claimed kernel 1.04937 to 1.04938, against 1/A^2 = 1.04938
  L=6 beta=6.0 with the sphere measure term: Hessian isotropy residual 0.00e+00, A(n beta)=0.976190, 1/A^2=1.0494
  L=6 beta=6.0 with the measure term: Hessian/expansion over the 19 modes 0.999999 to 1.000001; (1/lambda)/claimed kernel 1.07561 to 1.15561

(4) READING
  The quadratic form of -log pi about the aligned configuration has symbol beta' n (1 - phi(k)^2) with
  beta' = beta A(n beta) - the exact coefficient carries the beta that the task's shorthand omits. The numerical
  Hessian agrees with that expansion to six digits in every mode, on both a 4^3 and a 6^3 torus, at beta = 2 and 6,
  and is isotropic in the transverse plane to machine zero.
  Shape: the reversible law's kernel is proportional to 1/(1 - phi(k)^2) exactly, the same function of k as the
  formation kernel - the per-mode ratio is constant to five digits across all 9 (L=4) and 19 (L=6) modes.
  Constant: that ratio is 1/A(n beta)^2 = 1 + 2/(n beta) + O(1/(n beta)^2), i.e. 1.15976 at beta = 2 and 1.04938
  at beta = 6 for n = 7. It is not 1 at any finite beta, but the deviation is exactly the order in 1/(n beta) that
  the quadratic expansion does not control (the dropped quartic terms move the covariance at relative order
  sigma^2 = A(n beta)/(n beta)), and it falls as beta grows.
  Including the sphere's own measure subtracts exactly 1 from lambda(k), which leaves the long-wave end alone and
  raises the ratio at large k (to 1.376 at L = 4 and 1.633 at L = 6, both at beta = 2, where 1 - phi^2 is largest).
  So the agreement is of the shape exactly and of the normalisation to the accuracy of the expansion, which is what
  the task expects; no HIT. Numbers, not a verdict on the physics.
