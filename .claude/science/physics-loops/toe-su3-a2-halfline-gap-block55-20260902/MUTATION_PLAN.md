# Mutation Plan

The definitive test must reject at least:

- omission of the Weyl `rho=(1,1)` shift;
- a wrong reflection sign or a missing Weyl image;
- the square-lattice rather than triangular-lattice covariance;
- the wrong exponent `p^2+q^2` in place of `p^2+pq+q^2`;
- a fixed path/mode cutoff masquerading as a `sqrt(beta)` window;
- replacement of exact coefficients by the saddle coefficients;
- a finite-packet Perron gap presented as the infinite-operator gap;
- strong convergence presented as operator-norm/eigenvalue convergence without
  collective compactness or an equivalent theorem.

## Result

- missing `rho`, all-positive signs, a deleted image, square covariance, and a
  fixed Taylor cutoff are directly rejected by the verifier;
- the exact Bessel evaluator is retained as an independent support comparison,
  not replaced by the saddle;
- finite spectral rows are labeled support only;
- common-space convergence is upgraded through Hilbert-Schmidt factor norm
  convergence and then trace norm, rather than asserted from bare strong
  semigroup convergence.
