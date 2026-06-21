# Goal

Unblock audit execution by repairing source-side tooling and evidence surfaces.

This block does not audit any claim, apply any audit verdict, or push to
`main`. The narrow target is the runner-breakage inventory guard: the current
inventory still carries `missing_runner_file` rows, but audit prompt tooling can
canonicalize those legacy runner references to checked-in `scripts/*.py` files.

The block adds deterministic guard coverage showing those rows also have fresh
SHA-pinned `status=ok` runner caches on the current source tree.
