"""R19-25 s3b (07:06Z): exact vs approximate solutions of the sourced weak condition (G+ - rho) psi = 0 in s3's quartet.
 G+ is nilpotent, so no exact solution exists for rho != 0 (proved); the smallest singular value measures the best
 approximate solution (truncated coherent-type state). Print it in scientific notation vs d and rho."""
import numpy as np
for kind in ['HP', 'trunc']:
    for d in [3, 5, 9, 17]:
        S = (d - 1)/2; A = np.zeros((d, d))
        for n in range(1, d): A[n-1, n] = np.sqrt(n*(2*S - n + 1)/(2*S)) if kind == 'HP' else np.sqrt(n)
        I = np.eye(d); Gp = np.kron(A, I) - np.kron(I, A)
        row = [np.linalg.svd(Gp - rho*np.eye(d*d), compute_uv=False).min() for rho in (0.1, 0.3, 1.0)]
        print(f"{kind:5s} d={d:2d}: min sing.val of (G+ - rho) for rho = 0.1, 0.3, 1.0: " + ", ".join(f"{x:.2e}" for x in row))
