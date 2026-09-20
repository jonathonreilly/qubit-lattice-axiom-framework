# Block 36 — results (2026-09-20)

- Runner: `scripts/admissibility_rule_re_recording_at_every_tick_static_law_stationary_bilayer_ferromagnet_long_range_order_green_function_response_2026_09_20.py`, `TOTAL: PASS=24 FAIL=0`; nine mutations, each failing in its own family (B, B, C, C, D, D, E, F, F).
- T1: detailed balance of one-site re-recording with the static law on the four-cycle at (3,1,2) and (5,2,4), exhaustively; the conditional of a parity class is the product of the rule's kernels; the synchronous step maps the class marginals into each other.
- T2: detailed balance with `Π Z_x` for all 256 pairs (two-valued menu) and 400 random pairs (six axes); the layer marginal of the pair law; the doubled graph onto the bilayer for `L = 4, 6`, edge for edge; reflections and their cover on `L = 4`.
- T3: bands `E`, `14 − E`; the infrared bound verified exactly on the doubled 4- and 6-cycle with two-valued records at `e^β = 2` (largest ratio to the bound `0.318`); `I₂ ∈ (0.1409314, 0.1409316)`; `β₀ < 0.5914` given block 22; `G₄ = 1517/7680`, `H₄ = 127/896`.
- T4: symbols; exact `3³` propagation of the mean around a source and of the covariance.
- Controls (`specs/supervisor_control_block36_*`): plateau `0.016` (β = 0.5), `0.415` (0.6), `0.767/0.763/0.762` (β = 1, L = 16/32/48); source potential ratio `0.964` (β = 1), `0.992` (β = 6), symmetric; backward lattice `0.970`, one-sided. Refuter: chain against equilibrium sampler within `0.001` at three couplings for both stencils.
- The clause contradicts the axioms memo; nothing adopted.
