# Goal

Convert the gauge-vacuum adjacent-word scorecard sync PR from a direct edit
of an already-audited parent note into a source-side post-audit hygiene
companion.

The target issue is narrow: the parent note's verification block still
displays `TOTAL: PASS=25, FAIL=0`, while the current parent runner and
SHA-pinned cache display `TOTAL: PASS=28, FAIL=0` after three reviewer
checks were added. Directly editing the parent note changes audited bytes,
so this branch leaves the parent note unchanged and adds an executable
companion that proves the scorecard freshness discrepancy.

No axiom, audit verdict, row tag, generated audit data, or publication
effective-status surface is edited here.
