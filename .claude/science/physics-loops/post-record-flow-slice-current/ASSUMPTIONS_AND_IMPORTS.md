# Assumptions And Imports

Allowed current-surface inputs:

- `docs/POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md`
- `docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md`
- `docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md`
- `docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md`
- `scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py`
- `docs/audit/claims-ledger.jsonl`, read-only

No observed target values, fitted selectors, or new axioms are used.

Open imports:

- The artifact does not derive a selector rule. It preserves the firewall that
  a stable setting is not a selected dial.
- The branch does not assert effective retained status. Independent audit must
  re-check whether the refreshed packet resolves the ledger blocker.
