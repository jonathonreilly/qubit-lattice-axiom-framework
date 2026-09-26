# Block 153 — results (2026-09-26)

- **Runner.** `scripts/admissibility_rule_moving_records_at_the_neutral_scale_have_no_long_range_order_at_low_density_and_long_range_order_at_large_beta_and_high_density_2026_09_26.py`: `TOTAL: PASS=16 FAIL=0` (about 3 s). Seven mutations (five in families B, C, D, E and H, two in F), each failing in its own family.
- **T0.** At c0 = 1/cosh(beta) the kernel is 1 + t sigma sigma' (t = tanh(beta), sigma = n s in {-1, 0, 1}).
- **T1.** For every beta and z < 1/320: sum_x <sigma_0 sigma_x> <= p + 6p^2/(1 - 5p), p = 64 z, on every even torus. So there is no long-range order, and the structure factor is bounded uniformly.
- **T2.** The law is reflection positive through planes of sites for every c, beta and z. Given the chessboard estimate (A1) and the torus separation lemma (A2): if P(A, U) <= 1/2704, then <sigma_0 sigma_x> >= 1 - 2[2 eps + 2 eps/(1 - 676 eps)^2] - delta_L. For example, z >= 10^40 with 1 - tanh(beta) <= 10^-8 gives >= 0.998 - o(1).
- **Reading.** At the neutral scale the two-valued law's order depends on density. There is none when records are scarce, at any binding, and there is order when records are dense and bind strongly. This answers block 126's open item N1.3 for the two-valued menu.
- **Not covered.** The window 1/320 <= z < 10^40 at large beta; the sphere menu; proofs of A1 and A2 at this scope.
