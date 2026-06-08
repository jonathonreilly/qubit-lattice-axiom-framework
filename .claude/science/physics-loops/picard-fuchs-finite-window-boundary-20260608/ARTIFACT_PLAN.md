# Artifact Plan

Completed artifacts:

- Rewrite the historical all_order source note as a finite-window boundary
  packet.
- Correct nearby consumer wording that said the route was fully solved
  all-order.
- Update the source-packet manifest verifier so it expects finite-window
  boundary output and explicitly checks that all-order/minimality are false.
- Refresh primary certificate cache/output and source-packet manifest
  cache/output.
- Add this loop pack for reviewer handoff.

Verification artifacts:

- `logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt`
- `outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json`
- `logs/runner-cache/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.txt`
- `outputs/su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.json`
