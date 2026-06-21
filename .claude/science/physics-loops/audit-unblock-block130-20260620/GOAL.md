# Goal

Unblock audit maintenance by making runner-cache orphan cleanup safe for
nested runner paths.

This block does not audit any claim, apply any verdict, or promote any row.
It only prevents `scripts/precompute_audit_runners.py --cleanup-orphans` from
deleting cache files whose cache header points at a runner that still exists.

The immediate target is the false-positive class observed in dry run:

- `logs/runner-cache/yt_p1_delta_r_corrected_bound_memsafe.txt`
- `logs/runner-cache/yt_p1_fermion_regulator_verification_memsafe.txt`

Both cache headers name existing runners under `scripts/corrections/`, while
the pre-fix cleanup code only checked `scripts/<stem>.py`.
