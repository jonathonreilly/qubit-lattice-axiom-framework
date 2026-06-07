# Assumptions And Imports

No new axioms are introduced.

The repair uses only repo-native authority artifacts already present on
`origin/main`:

| PR | role | note | runner/cache certificate |
| --- | --- | --- | --- |
| #2850 | exact-support authority | `docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md` | `frontier_post_record_directed_certificate_examples_2026_06_06`: PASS=64 FAIL=0 |
| #2853 | no-go authority | `docs/POST_RECORD_DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL_2026-06-06.md` | `frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06`: PASS=52 FAIL=0 |
| #2856 | exact-support authority | `docs/POST_RECORD_SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE_2026-06-06.md` | `frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06`: PASS=39 FAIL=0 |
| #2858 | no-go authority | `docs/POST_RECORD_SELECTION_RULE_TARGET_VECTOR_FIREWALL_2026-06-06.md` | `frontier_post_record_selection_rule_target_vector_firewall_2026_06_06`: PASS=36 FAIL=0 |
| #2861 | exact-support authority | `docs/POST_RECORD_ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE_2026-06-06.md` | `frontier_post_record_admitted_sample_target_vector_interface_2026_06_06`: PASS=30 FAIL=0 |
| #2864 | exact-support authority | `docs/POST_RECORD_DYNAMICS_AUTHORITY_STACK_MAP_2026-06-06.md` | `frontier_post_record_dynamics_authority_stack_map_2026_06_06`: PASS=52 FAIL=0 |
| #2868 | exact-support authority | `docs/POST_RECORD_DYNAMICS_CAMPAIGN_CLOSEOUT_INDEX_2026-06-06.md` | `frontier_post_record_dynamics_campaign_closeout_index_2026_06_06`: PASS=46 FAIL=0 |
| #2871 | exact-support authority | `docs/POST_RECORD_RETAINED_UNBOUNDED_DYNAMICS_GATE_2026-06-06.md` | `frontier_post_record_retained_unbounded_dynamics_gate_2026_06_06`: PASS=54 FAIL=0 |
| #2874 | no-go authority | `docs/POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md` | `frontier_post_record_finite_to_unbounded_family_lift_nogo_2026_06_06`: PASS=43 FAIL=0 |
| #2875 | bounded-support authority | `docs/POST_RECORD_SUPPLIED_FAMILY_LIFT_CERTIFICATE_INTERFACE_2026-06-06.md` | `frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06`: PASS=39 FAIL=0 |

Open imports after this repair: none for the runner-artifact discrepancy.

This PR does not assert audit-retained status. Independent audit remains
required before any ledger movement.
