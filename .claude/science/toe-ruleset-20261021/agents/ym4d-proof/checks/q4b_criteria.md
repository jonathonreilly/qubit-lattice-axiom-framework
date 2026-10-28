# q4b criteria (lane G session 4; POST HOC to q4; written 2026-10-28 before checks/q4b_newton.py exists)

Label: POST-HOC re-run of q4 (checks/q4_kernel_ids.py), written after q4's recorded FAIL (K3) and after REVIEW_SQ_S3's
diagnosis (S3-8). q4's FAIL stands as recorded; q4b does not replace it.

Change from q4 (the only one): W_0(M) for SU(3) is computed by Newton's method on the SU(N) stationarity condition
F(W) := the traceless anti-Hermitian part of W⁻¹M = 0 (start: the determinant-normalised polar factor; update
W ← W·exp(X), X ∈ su(N) solving J X = -F with J the derivative of X ↦ F(W e^X) at 0, computed by central differences;
stop when |F|_HS ≤ 1e-15 or after 30 steps). SU(2): unchanged (exact polar factor). Same seed, same instance generation,
same random-number consumption order, same h = 1e-5, same thresholds.

- **P0 (precondition, the one q4 did not meet).** max over all W_0 evaluations of |F(W_0)|_HS ≤ 1e-13.
- **K1-K6** exactly as in q4_criteria.md (same thresholds: K1 1e-12, K2 1e-7, K3 1e-8, K4 1e-7, K5 1e-8, K6 0.05).
- Reported (no criterion): max ||W_Newton - W_BFGS||_op over the SU(3) instances (q4's BFGS routine re-run on the same M).

PASS = P0 and K1-K6. Resources: < 2 min, < 200 MB; under the numeric lock; nice 10, threads 1.
