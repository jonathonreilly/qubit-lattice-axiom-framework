# PR8170 cold adapter confirmation v2

Decision: **CAPTURE_ELIGIBLE** for the exact source and bounded resource plan only. This is not final evidence certification or a landing PASS.

Reviewer session: `/root/review_8170`, same original reviewer. Source tree `3ec7c92b81e9ec8ff85d79af9c982faff5b07aa2`, main/base `8bf464953779b8ada8415208e89a656411f9f525`.

The v2 adapter resolves blocker 8170-cold-1: it preserves the actual runner result externally before the unchanged cache API checks identity, rejects drift and withholds cache publication. The exact embedded wrapper matches the synthetic control. That control exercised the real API with one fake result: live output was deleted, external raw output survived, and no cache or science execution occurred. The original cold-v1 blocker remains in its immutable report.

The separate mutation adapter provides fourteen named, once-only invocations after successful bound primary capture. It checks the expected failed family, nonzero exit, check counts and consistent raw/JSON evidence, preserves failures, and rejects identity drift. It does not rerun baseline.

All draft source/input hashes remain exact, the index matches the accepted tree, and no unstaged changes exist. Prior full proof, recovery and train83 premise acceptance remains bound to cold-v1. The 900-second and 768-MiB limits are unmeasured per-invocation proposals with sampled process-tree monitoring, not benchmark results or hard OS memory reservations.

No primary, mutation, simulation, formal gate or synthetic control was executed by this confirmation; no source was edited or staged. Actual capture evidence and final integrated review remain pending. Exact artifact hashes and detailed bindings are in the companion JSON.
