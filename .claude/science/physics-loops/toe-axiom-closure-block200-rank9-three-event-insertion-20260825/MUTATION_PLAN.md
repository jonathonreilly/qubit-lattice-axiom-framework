# Mutation Plan

Every registered mutation must fail a dedicated gate:

| mutation | gate |
|---|---|
| `swap_effect_for_lueders_operation` | T1/T2 type split |
| `identify_nonselective_lueders_with_identity` | T1/T5 |
| `drop_identity_operation_direction` | T5 |
| `inflate_rank9_to_64_controls` | T5/T6 |
| `use_indefinite_M_as_probability` | T3 |
| `swap_pointer_character_sigma_for_s_or_t` | T3 |
| `omit_triple_port_selector` | T4 |
| `fit_b_after_reading_action` | T4 |
| `replace_nonwrapped_lag_by_wrapped_lag` | T0/T3 |
| `infer_semigroup_from_hankel_order_two` | T6 |
| `inject_free_boundary_state_or_phase` | T2/T6 |
| `change_schur_cut_without_disclosure` | T0 |
| `swap_boundary_and_complement_order` | T0 |
| `reverse_berezin_differential_order` | T1/T2 |
| `drop_doubled_conjugation` | T5 |
| `replace_F_alpha_by_gaussian_proxy` | T2 |
| `accept_DPP_without_contraction` | T1 |
| `erase_H_composition_residual` | T1 |
| `break_exactly_one_outcome_per_crossing` | T2/T4 |
| `break_normalization` | T3/T4 |
| `break_lower_cylinder_marginal` | T4 |
| `drop_one_event_branch` | T3/T4 |
| `break_reflection_label_map` | T2/T4 |
| `break_proper_cubic_context_covariance` | T2/T4 |
| `claim_identity_from_effect_coarse_graining` | T3/T5 |
| `claim_process_from_euclidean_cylinder` | T6 |
| `smuggle_source_into_unsourced_insertion` | T2/T5 |
| `test_symmetry_representatives_only` | T4 |

The independent checker must use a disjoint implementation and reject the
same semantic families even if its mutation names differ.
