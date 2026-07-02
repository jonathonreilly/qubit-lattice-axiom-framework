# No-Go Ledger

| Route | Boundary | Evidence | Reuse |
|---|---|---|---|
| Exact carrier/readout alone | Does not derive endpoint triple | `frontier_quark_route2_exact_readout_map.py` | Parent obstruction |
| Quadratic `O_h` invariant | Leaves E/T coefficient ratio free | `frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py` | Reused as current-bank boundary |
| CKM gap-only map | `eta^2=5/36` misses Route-2 target | block79 runner | New falsifier |
| Direct `A^2` map | `2/3` misses Route-2 target | block79 runner | New falsifier |
| Single reciprocal-square component maps | `1/4` and `1/9` miss Route-2 target | block79 runner | New falsifier |
| CKM inverse-square as retained Route-2 authority | Not available on current branch; retained-tier authority checks fail in CKM runner | `frontier_ckm_wolfenstein_eta_inverse_square_gap.py` | New firewall |
