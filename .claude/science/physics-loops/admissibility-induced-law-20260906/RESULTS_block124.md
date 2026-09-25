# Block 124 — results (2026-09-24)

- **Runner.** `scripts/admissibility_rule_blindness_to_coin_rotations_that_vary_in_time_leaves_exactly_block_62s_two_kinetic_numbers_and_no_ratio_makes_a_transverse_relabelling_in_time_a_symmetry_2026_09_24.py`: `TOTAL: PASS=12 FAIL=0` (~4 s). Six mutations, each failing in its own family.
- **T1.** A rotation shifts the lowered rate by an arbitrary antisymmetric matrix, and sym(gV) = −ġ/(2w). So c₁I₁ + c₂I₂ + c₃I₃ is blind iff c₁ = c₂, which leaves exactly (det e/w)[α tr(g⁻¹ġg⁻¹ġ) + β(tr g⁻¹ġ)²] for every frame.
- **T2.** c_k = 12α + 36β. For α > 0 it is negative iff β < −α/3. At β = −α it is −24α.
- **T3.**
  - A transverse relabelling in time changes the Lagrangian by 4αζ̇ ξ·ḣ·p + 2αp²|ξ|²ζ̇². Its variational derivative is not zero, so it is a symmetry at no ratio.
  - The gradient relabelling is a symmetry iff β = −α (as in block 112 T2).
- **T4.**
  - M(ppᵀ, 2αX/K) = 2(α + β)Xp²(δ, 0).
  - The transverse directions are null only at X = 0 and drift uniformly.
  - α/K is untouched by either demand.
- **T5** (supervisor's own addition; same family, not refereed by another family).
  - In block 62's cube family, the gradient relabelling in time is a symmetry iff (M₁, M₂, M₃) = (0, c, −c), the rotation-invariant member at β = −α.
  - The transverse one is a symmetry iff (M, 2M, 0), with α = 0.
  - Both together hold only for zero.
