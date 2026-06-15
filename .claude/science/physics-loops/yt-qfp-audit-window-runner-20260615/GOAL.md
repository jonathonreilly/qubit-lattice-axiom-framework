# Goal

Repair the live-runner timeout blocker for `yt_qfp_insensitivity_support_note`
without changing audit verdicts or promoting the claim.

The source-side move is narrow: make the default runner produce the same
bounded-support certificate inside the audit window, while keeping the dense
historical ODE sweep available via `--full-sweep`.
