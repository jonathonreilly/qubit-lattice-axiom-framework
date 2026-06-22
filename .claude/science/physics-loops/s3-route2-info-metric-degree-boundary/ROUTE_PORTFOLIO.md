# Route Portfolio

1. Fisher/Rao metric on supplied probabilities.
   - Result: no-go for endpoint. Coefficient `1/w` gives degree `-1`.
2. Local KL quadratic form.
   - Result: no-go for endpoint. Same coefficient `1/(2w)`.
3. Shannon/Boltzmann convex entropy Hessian.
   - Result: no-go for endpoint. Hessian of `w log w` is `1/w`.
4. Log-barrier Hessian `-log w`.
   - Result: remains positive target. Hessian is `1/w^2`.
5. Ray-quotient scale-invariant Hessian.
   - Result: remains positive target and matches Block107.
