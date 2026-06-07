# Assumptions And Imports

Allowed current-surface inputs:

- `gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note`: retained_bounded source-sector diagonal factorization.
- `gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10`: retained temporal-gauge linkwise factorization.
- `su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10`: retained SU(3) diagonal-convolution dictionary.
- `wilson_su3_gauge_transfer_kernel_positivity_bounded_note_2026-05-30`: retained_bounded Wilson one-link coefficient nonnegative expansion.

New in-branch derivation:

- For each SU(3) dominant weight `(p,q)`, the tensor product
  `V_(1,0)^tensor p tensor V_(0,1)^tensor q` contains `V_(p,q)`.
- Hence `m_(p,q)^(p+q) >= 1` in
  `(chi_(1,0)+chi_(0,1))^(p+q)`.
- Therefore the `n=p+q` term in the Wilson exponential coefficient is
  strictly positive for `beta>0`, and `a_(p,q)(beta)>0`.

Forbidden/non-consumed inputs:

- No new axiom.
- No observed values, fitted selectors, or unit conventions.
- No full all-weight `L^2` class-function convergence for `Z_beta^env`.
- No normalized `kappa_(0,0)=1` residual-environment premise.
