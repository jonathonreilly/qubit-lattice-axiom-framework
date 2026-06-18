# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Bessel determinant convention | Defines `c_(p,q)(beta)` and `(0,0)` normalization | computed lattice input | existing Wilson determinant runners/notes | yes | yes | already repo-native | reused |
| Scalar Gaussian core `g_k(t)` | Leading scalar local-CLT entry | framework-derived scalar support | scalar local-CLT note | yes | yes for H_det_core | already checked upstream | reused |
| Gaussian determinant mode sum `G_(p,q)` | New determinant-core object | computed lattice input | new runner/cache | yes | yes for this block | exact runner/log route | added |
| Exact Bessel scalar corrections | Difference between true Wilson determinant and Gaussian core | open theorem/computation | not closed here | no for H_det_core; yes for full H_det(A) | exact remainder/tail theorem | open residual |
| Determinant-mode and representation-weight tails | Uniform tail needed for `K_W(A)` | open theorem/computation | not closed here | no for H_det_core; yes for full H_det(A) | exact tail theorem | open residual |
| `H_spec` reduced spectral domination | Route A reduced A2 comparison | open theorem/computation | not closed here | no for H_det_core; yes for assembly closure | reduced spectral theorem | separate open residual |
