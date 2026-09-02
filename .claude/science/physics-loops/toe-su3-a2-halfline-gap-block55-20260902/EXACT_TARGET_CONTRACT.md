# Exact Target Contract

Let `P = {(p,q): p,q >= 0}` and let `J` be the self-adjoint six-neighbor
character recurrence on `ell^2(P)` with invalid negative-label neighbors omitted.
For `beta >= 0`, set

```text
c_lambda(beta) = <lambda|exp(beta J)|0>,
r_lambda(beta) = c_lambda(beta)/c_0(beta),
T_beta = exp((beta/2)J) diag(r_lambda(beta)) exp((beta/2)J).
```

The target is a uniform half-line spectral statement for the exact infinite
operator, not a finite packet:

```text
there exists delta > 0 such that
lambda_1(T_beta)/lambda_0(T_beta) <= 1-delta
for every beta >= 0.
```

Route 1 may instead close the exact W85 registered sub-obligation by proving,
for a declared active-window size `A`, explicit `beta_0(A)` and `K_W(A)` in

```text
| beta^(-3/2) r_(p,q)(beta)
  - beta^(-3/2) d_(p,q) exp[-3 C2(p,q)/beta] |
<= K_W(A) beta^(-1/2)
```

uniformly for `0 <= p,q <= A sqrt(beta)`, together with the true tail needed
by the operator sandwich.

The compactness bypass counts only if all operators are placed on one precisely
defined Hilbert space (or linked by explicit isometries), convergence is strong
enough to transfer the first two eigenvalues, and no finite-beta interval is
left to numerical extrapolation.
