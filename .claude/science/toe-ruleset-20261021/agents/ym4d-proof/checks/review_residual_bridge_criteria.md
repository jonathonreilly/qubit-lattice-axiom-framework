# Pre-stated lattice bridge review criteria

UTC: 2026-10-29T14:04:06.018574+00:00

Frozen commit: 9761471ab46e659ce856e2b9c7c10fef2b06cf5c. Complete bridge note: checks/residual_det_lattice_bridge_working.md, SHA256 bb67ad564747c4c9954ae93f88aa3f43a806c88b0aefedd5ef54a945e1512c6b, 245 lines. Review includes its frozen manifest and residual_det_03.*. The prior reviewed model unit is retained unchanged. Current-main methodology remains ca2bc7ddf64790da96cd43d42017d000fbfe4808. Do not consume the active vertex files.

## Scientific criteria

1. Derive the actual augmented null rows from separate fine/h stationarity, with V fixed despite a nonzero coarse gradient. Pin real charged-root multiplicities, Cartan background restrictions, compatible twists, common domains and invertibility. No neutral-sector, generic colour/background, or periodic quotient result follows by naming a regulator.
2. Reconstruct both point and harmonic shears and every determinant/Gram factor, including Delta_int, H_h, G_c and the level normalization. Test nontrivial harmonic lifts and omitted-factor controls by independent exact matrix elimination. A random compatible matrix is an algebra test, not the actual lattice Hessian.
3. Derive the 72I Gram and its scaling, mean-zero nonlocal correction, point-lift quartic Rayleigh quotient, volume-independent fixed-depth Dirichlet gap and inverse locality. Keep the quartic failed inference and every required limit explicit.
4. Derive the complete alias S symbol and normalization; the free Hodge Gram/factorization; the all-mode simple-pole estimate; and A7 with high-alias minimization. No special-vector Rayleigh quotient certifies every mode. Read newly needed actual S4-prime definitions and distinguish free from off-shell vertices.
5. Independently build the actual one-step d=4, L=3 root contour map from all order-averaged paths (not from an author helper). At fixed kappa=3/2, verify Qd=d_c ev and the normalized constant-field map, then test the harmonic operator numerically on prespecified rays. Use t=0.04,0.02,0.01 and directions e1 and (1,2,-1,3)/sqrt(15). Algebra/covariance residuals must be <=1e-10. Principal-matrix norm error must be <=2t; the last error must be <0.7 times the previous unless both <1e-10. This finite sampling is a control, not a proof of a continuum or all-mode limit.
6. A direct all-alias finite Bloch Laplacian at K=(pi,pi,0,0) will be solved by exact elimination and compared to the independently counted alias spectrum [1,4,1] in the first two directions and [0,3,3] in the last two. Check the full root Green normalization, not only the main alias. A real two-component version must expose the conjugate-root determinant multiplicity.
7. Deliberate controls: omit high-alias minimization, Delta_int, one S power, a one-form Gram or the null-column premise; retain any failure and its diagnosis. Source claims are accepted only on their explicitly quantified finite/free domains. Actual residual/background vertices and all regulator/volume/infrared interchanges remain open unless proved in these frozen bytes.

After freezing this review, review MASS_GAP_TARGET.md separately; do not conflate its criterion with an achieved infrared estimate or with this free gauge-sector calculation.

## Adaptive diagnostic, declared before running review_residual_bridge_03

The first numerical run completed 45/45 predicates, but NumPy emitted divide/overflow/invalid warnings at `slogdet` despite returning finite consistent determinants. Preserve that stdout/stderr unaltered. Independently reconstruct the same non-real scalar Bloch Laplacian by a Kronecker sum, establish positivity, and obtain both complex and real-pair log determinants from Cholesky diagonals. Require agreement with the saved first-run values and the factor of two to 1e-10. Capture, rather than suppress, any warning or exception from an isolated repeat of `slogdet`. This is a numerical diagnostic, not new scientific evidence for off-shell claims.
