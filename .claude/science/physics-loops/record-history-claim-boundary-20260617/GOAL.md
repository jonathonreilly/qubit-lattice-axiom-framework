# Record History Claim Boundary Repair

Goal: unlock the audit path for the high-load record-history rows by aligning
source claim boundaries with the actual proofs.

Target rows:

- `record_history_monoid_unbounded_retention_2026-06-05`
- `record_history_order_time_rate_firewall_2026-06-05`

Non-goals:

- no audit execution;
- no audit ledger, queue, registry, or publication-status edits;
- no claim that record production, probabilities, IID structure, time/rate
  normalization, or dial selection are derived.
