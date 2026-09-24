# Block 106 — results (2026-09-23)

- **Runner.** `scripts/admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_2026_09_23.py`: `TOTAL: PASS=11 FAIL=0` (~12 s). Six mutations, each failing in its own family.
- **T1.** The weight of the fall is ∂p̄/∂k_j: cos k, cos 2k, and 1 − k⁴/6 for the fourth-order stencil. It has zero zone mean, so no local momentum falls with weight one.
- **T2.** f_j = d_jφ(x)ε_j(x) + d_jφ(x−e_j)ε_j(x−e_j), with the logarithmic-mean factor. It is not a function of the energy density (the sublattice state), and it is parity-even while the energy density is odd.
- **T3.**
  - Curl ledgers have no rate term, so they demand no force.
  - The volume member with the upwind transport carries the rates.
  - Waves with equal energy density and current get forces 0 and nonzero.
- **T4.** The two-step bond form; weight cos 2k (plane waves on 8³).
