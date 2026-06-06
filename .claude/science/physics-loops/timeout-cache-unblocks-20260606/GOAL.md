# Goal

Unblock audit rows whose only current executable blocker is a stale timeout
cache, without changing audit results or source-note status surfaces.

This block repairs:

- `kernel_vs_gravity_note`
- `shapiro_five_family_portability_note`

Both runners completed successfully when given a source-declared timeout just
above the old default budget.
