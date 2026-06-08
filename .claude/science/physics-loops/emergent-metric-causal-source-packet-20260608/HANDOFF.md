# Handoff

This PR repairs the source side of the emergent-metric conditional row. It does not retag the ledger.

Main changes:

- The note now declares `actual_current_surface_status: conditional-support`.
- The one-hop causal-source packet is explicit, with current ledger statuses.
- Malament/HKM assumptions are explicit.
- The runner checks source docs, runners, caches, current ledger statuses, conditional-status markers, conformal null-cone algebra, and clock-rate no-go algebra.
- The paired cache is refreshed and SHA-pinned.

Reviewer/auditor focus:

- Confirm the branch does not overclaim retained conformal-class status.
- Confirm the explicit packet satisfies the audit instruction's "or narrow the theorem to be conditional on those inputs" path.
- Upstream rows still needed for any stronger future status:
  - `record_history_order_time_rate_firewall_2026-06-05`
  - `reconstructed_h_quasilocal_from_analytic_dispersion_microcausality_bridge_narrow_theorem_note_2026-06-06`
