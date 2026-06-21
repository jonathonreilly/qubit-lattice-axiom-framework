# Goal

Complete the safe orphan runner-cache cleanup after the block130 and block131
safety guards.

This block deletes only the 8 cache files that remained after cleanup learned
to preserve:

- caches whose headers point at existing nested runners;
- caches still referenced elsewhere in the repository.

No audit verdicts, claim statuses, or ledger rows are changed.
