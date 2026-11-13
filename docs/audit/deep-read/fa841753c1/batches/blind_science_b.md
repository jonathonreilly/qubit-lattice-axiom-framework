## Note 1704
- Path: `docs/FRW_C3_EOS_COMPONENT_LABELS_KINETIC_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md`
- Result: no fix
- Checked: For one equi-norm shell, the three axis-square sums add to `n q`, so each equals `n q / 3` once they are equal. Massless cancellation: `(n q / 3) / sqrt(q) = n sqrt(q) / 3`, hence `3 P_i = rho` and `P_i / rho = 1/3` on a shell and on a positive mixture. Massive ratio: `(1/3) q / E^2 = q / (3 (m^2 + q))` with `E^2 = m^2 + q`. Gap: `1/3 - q / (3 (m^2 + q)) = m^2 / (3 (m^2 + q))`, so `0 < w < 1/3` whenever `q > 0` and `m^2 > 0`. Rest sector: `P_i = 0` and `w_m = 0` when `rho = n m > 0`.
- Finding: The printed ideal-label algebra is right, and the note already keeps it on finite permutation-symmetric massless shells plus a pressureless rest sector. The massive correction is correctly shown to be positive, so the dust label is not extended to moving massive modes. The title’s bounded-support wording matches that limited claim rather than a derivation of the full FRW fluid.
- Open: C1, C2, the full FRW backdrop and Friedmann equations, thermal history and entropy conservation, homogeneity and isotropy of the real cosmological fluid, the bridge from these ideal labels to that fluid, `N_eff` and any observed parameter, the separate `w_Lambda = -1` surface, and independent re-audit.

## Note 1716
- Path: `docs/ALPHA_S_SOMMER_STATIC_POTENTIAL_ROOT_KERNEL_THEOREM_NOTE_2026-06-18.md`
- Result: no fix
- Checked: `d/dR (V0 + sigma R - e/R) = sigma + e/R^2`, so `F(r0) r0^2 = 1.65` rearranges to `sigma (r0/a)^2 + e = 1.65` and `r0/a = sqrt((1.65 - e) / sigma)`. With the printed inputs, `1.65 - 0.284764583881128 = 1.365235416118872` and `(1.365235416118872) / 0.054485636694192124` has square root `5.005676254205750606...`, which rounds to the printed `5.005676254205751`. Anchor conversion: `0.5 / 5.005676254205751 = 0.099886603649187623...`, matching printed `global_a_fm = 0.09988660364918762` at the printed digits. The anchor does not enter the root formula.
- Finding: The dimensionless Cornell–Sommer rearrangement and both printed decimal evaluations are correct at the digits given. The note proves only that lattice root from `sigma` and `e` under the stated force convention. It already says the physical `r0 = 0.5 fm` anchor is not an input to the root and is not derived.
- Open: The physical Sommer anchor `r0 = 0.5 fm`, promotion of `alpha_s(M_Z)`, physical units, QCD running, threshold matching, pure-gauge-to-full-QCD transfer, Wilson-surface normalization, and any scale-setting theorem that converts `r0/a` to physical units without importing that anchor.

## Note 1717
- Path: `docs/ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md`
- Result: no fix
- Checked: `c(n) = 11 - 2n/3 > 0` for integer `n >= 0` holds exactly on `n = 0, ..., 16`: `c(16) = 1/3` and `c(17) = -1/3`. Shift: `c(n-1) - c(n) = 2/3`. Printed values: `c(6) = 11 - 4 = 7`, `c(5) = 11 - 10/3 = 23/3`, `c(4) = 11 - 8/3 = 25/3`, `c(3) = 11 - 2 = 9`. Inverses: `U_{c,L}(T_{c,L}(x)) = x = T_{c,L}(U_{c,L}(x))`. Length additivity: `T_{c,L_2}(T_{c,L_1}(x)) = x - c(L_1+L_2)`. A path of segments `0..m` has markers `0..m-1`, so the jump correction is `sum_{r=0}^{m-1} j_r`.
- Finding: The admissible range, the four displayed coefficients, the affine inverses, and the marker-jump formula are exact rational identities. The note already withdraws the heavy-threshold reading and says the filename is only repository identity, so that physical name is not the claim being made.
- Open: No physical identification is established. A later consumer would still have to supply its own data before `c(n)`, the segments, or the identity carry could be read as a beta coefficient, a flavor threshold, a matching scale, a no-jump condition, a Lambda parameter, or an `alpha_s(M_Z)` value. Effective audit status is left to the independent audit lane.
