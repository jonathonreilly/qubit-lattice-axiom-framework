# Goal

Repair the audited-failed post-record dynamics closeout index by reconciling
the source note with the runner/cache summary counts.

The failed audit blocker was exact: the note cited stale `PASS=60` and
`PASS=47` summaries while the runner/cache verified `PASS=64` and `PASS=52`.
This branch aligns the source text and adds runner checks for the note-side
summary inventory.
