# Review History

Local pre-review only; the user asked for the reviewer to own the actual
review-loop and landing.

Checks before PR:

- runner must pass with `FAIL=0`;
- runner must compile;
- cache must match runner output;
- `git diff --check` must pass;
- no audit, publication, queue, status, or ledger files may be edited.
