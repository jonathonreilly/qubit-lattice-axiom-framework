# Block 187 — results (2026-09-27)

- **Runner.** `scripts/admissibility_rule_the_free_particle_law_for_every_uniform_metric_2026_09_27.py`: `TOTAL: PASS=15 FAIL=0` in about 4 s. Nine mutations (seven in families A–F and I, two in G), each failing in its own family only.
- **T1–T2.** `∂W/∂g_ab = −¼W_aW_b` has six commuting flows. Its solution is `k = k₀ + ½(g − 1)∇W₀`, `W = W₀ + ¼∇W₀·(g − 1)·∇W₀`, checked for a general symmetric `3 × 3` metric.
- **T3.** On the diagonal this is block 184's rule, and waves at rest keep `W = μ²`.
- **T4.** `1 − v·g·v = (4W₀ − |∇W₀|²)/(4W)`, with `4W₀ − |∇W₀|² = 4Σ sin⁴ + 4μ² ≥ 0`.
- **T5.** The Jacobian is `1 + (g − 1)diag(cos 2k₀)`. The family is smooth exactly while `g`'s eigenvalues lie in `(0, 2)`. A pure shear is smooth iff `|ε| < 1`.
- **T6 (second version).** `F = (1 + CGC)^{1/2} sin k₀` at `k₀(k)` realises the spectrum and is block 184's walk on the diagonal. It is not unique.
- **Review.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error; its corrections are in the second version.
