# R17-10 certification method (fixed 2026-10-13 ~01:21Z, before any certification run; after the runner rechecks only)

1. Target (per condition): sup over the relaxation superset of
   - K6 problem:  -<K6/e^7>/128 subject to Xi_Eg = Xi_T2g = 0  (equivalently face1 at the axis zeros),
     and the stronger form sup face1 subject to Xi_Eg >= 0, Xi_T2g >= 0;
   - mu_E problem: inf mu_E subject to Xi_Eg = Xi_T2g = 0 (Xi_Eg, Xi_T2g >= 0),
   U vertex, E1, m in [0.01, 0.1], continuous b, lo, hi, s_min.
2. Relaxation: R16-9 Lemma R_U per-level (M, P, Q) extended by R = int s^6 dk, with the truncated
   Hausdorff conditions on u = s^2 in [0,1], coarea+Cauchy-Schwarz (M P >= |A|^2), sigma <= k tail, total mass pi - b.
3. Certified method: interval branch-and-bound with outward rounding (mpmath.iv), or a verified moment-SOS
   certificate with rational data. Only installed packages; no SDP solver is installed (checked), so SOS is not available.
4. Tolerance: ZERO for the certificate. A CERTIFIED-CONFLICT needs a bound whose every floating-point step is enclosed
   (outward-rounded intervals for the t-quadrature, the level-bin placement and the optimization bound) and whose
   enclosed upper bound for face1 (lower bound for K6, mu_E) has the strict sign. Anything else (local optimizers,
   node-placed bins, non-enclosed quadrature) is "checked" numerics, never a certificate.
5. Numerical (non-certified) gap test first: local multistart SLSQP on the node-placed relaxation, quadrature
   tolerance ~1e-6 relative (700 log-t nodes, as R16-9), to see whether the relaxation's optimum keeps the sign
   with margin (a precondition for any certificate on this relaxation).
