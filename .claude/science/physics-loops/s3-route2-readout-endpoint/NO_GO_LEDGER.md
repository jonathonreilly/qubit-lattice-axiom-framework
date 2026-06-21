# No-Go Ledger

| Route | Boundary | Evidence |
|---|---|---|
| Restricted Route-2 carrier alone | Leaves `rho_E` free | `frontier_quark_route2_exact_readout_map.py` PASS=11 |
| Conditional time coupling | Exact only after `P_R` is supplied | `frontier_quark_route2_exact_time_coupling.py` PASS=8 |
| Rconn/Fierz direct bridge | `F_adj` not typed as Route-2 center readout | `frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py` PASS=62 |
| Current source-domain typed graph | No `R_conn -> c_TE -> rho_E` path without missing bridge | `frontier_quark_route2_source_domain_bridge_no_go.py` PASS=103 |
| SU(3)-invariant adjoint line | No nonzero invariant traceless vector | block39 runner PASS=15 |
| Color orientation as source | Current source surface treats orientation as gauge/predictively vacuous | color orientation runner PASS=19; block39 text check |
| Color depolarization route | Erases traceless mean instead of selecting line | color depolarization runner PASS=18; block39 text check |
| Fierz/singlet channel route | Gives `1+8`, not a line in `8` | color singlet PASS=7; EW Fierz PASS=31 |
