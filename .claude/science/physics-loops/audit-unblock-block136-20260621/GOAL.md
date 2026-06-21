# Goal

Apply the source-graph repair tooling introduced by block135 to remove live
dependency edges that the audit queue already marks as non-load-bearing
cycle citations.

This block does not audit claims, change verdicts by hand, or assert retained
status. It moves named cite-only links into
`## Cross-references (non-load-bearing)` sections and regenerates deterministic
audit support surfaces.
