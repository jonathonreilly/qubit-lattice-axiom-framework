# Goal

Repair a source-side metadata dependency error that left seven audited-clean
rows in `retained_pending_chain` only because their notes linked to
`KEY_TERMINOLOGY.md`.

The glossary links were not load-bearing scientific dependencies. Removing
them changes note hashes, so the rows are queued for independent re-audit
rather than directly retagged.
