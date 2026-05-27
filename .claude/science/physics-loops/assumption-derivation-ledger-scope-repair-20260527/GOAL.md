# Goal

Repair `assumption_derivation_ledger` after its audited conditional verdict.

The prior source was a package-wide status ledger, but the row declared only
one direct dependency, `rconn_derived_note`. Under restricted-packet audit, the
only one-hop authority available here is the R_conn/F_adj note. This loop
therefore narrows the ledger row to the exact `F_adj = 8/9` authority slice and
keeps physical `R_conn`, `K_EW = 9/8`, and all other package status rows outside
the binding claim.

No axiom, selector, fit, or audit verdict is added.
