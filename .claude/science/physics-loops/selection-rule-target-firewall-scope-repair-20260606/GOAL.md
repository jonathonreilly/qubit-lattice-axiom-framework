# Goal

Repair `post_record_selection_rule_target_vector_firewall_2026-06-06` without
depending on an unaudited broad Record target-vector no-go.

The current audit gave two repair paths: include retained Record authority plus
selection-rule authority, or narrow to the finite supplied-rule witness. The
Record schema is not yet clean in the current ledger, so this block takes the
honest narrowed path and adds the clean supplied-selection interface authority.
