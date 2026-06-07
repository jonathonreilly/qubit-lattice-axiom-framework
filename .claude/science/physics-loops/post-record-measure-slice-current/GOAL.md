# Goal

Repair the measure/weight subdivision runner-artifact issue by making the
current ledger slice exact and visible.

The current `origin/main@d07efaa31` recomputation gives 45 rows, not the older
44-row table. This branch updates the expected counts and prints every row in
the slice.
