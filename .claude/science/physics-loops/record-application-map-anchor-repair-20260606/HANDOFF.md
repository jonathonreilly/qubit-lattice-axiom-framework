# Handoff

Branch: `physics-loop/record-application-map-anchor-repair-20260606`

This PR repairs the failed `record_axiom_audit_application_map_2026-06-06`
runner/cache. The current audit blocker asked to correct or justify two
`flavor_det_character_selection` anchor phrases and rerun the classifier.

What changed:

- Updated the two flavor-det anchors in
  `scripts/frontier_record_audit_application_map_2026_06_06.py` to current
  source-note language.
- Refreshed
  `logs/runner-cache/frontier_record_audit_application_map_2026_06_06.txt`.

Verification:

- `python3 scripts/frontier_record_audit_application_map_2026_06_06.py`
  reports `SCORECARD: PASS=39 FAIL=0`.
- Cache refresh exits zero.

Boundary:

- This PR does not edit audit data.
- This PR does not promote downstream Record-sensitive rows; the classifier
  still marks real downstream lanes partial when non-Record gates remain.
