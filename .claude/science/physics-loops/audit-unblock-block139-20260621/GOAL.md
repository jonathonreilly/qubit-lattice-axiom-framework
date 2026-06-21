# Goal

Regenerate the audit control surfaces from current source notes so the
independent audit/review lanes see the current queue, runner registrations,
and stale-retained invalidation state.

This block is an audit-unblock package. It does not run an audit worker, does
not apply audit verdicts, and does not push to `main`.
