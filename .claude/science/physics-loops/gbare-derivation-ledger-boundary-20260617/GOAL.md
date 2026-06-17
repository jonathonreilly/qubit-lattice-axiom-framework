# Goal

Repair the `g_bare_derivation_note` runner/cache boundary so current audited-conditional dependency rows are reported as an open parent gate, not as failure markers.

This PR does not audit the row, retag the ledger, or close the g_bare parent theorem. It keeps the runner useful for re-audit by separating exact algebra checks from audit-gate status reporting.
