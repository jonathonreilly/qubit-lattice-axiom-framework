# Handoff

Branch: `codex/flavor-interacting-core-split-20260618`

Target row: `flavor_interacting_matter_build_note_2026-05-30`

What changed:

- The source note now says the auditable claim is the executable
  `epsilon`/`C3`/`Q(r)` finite-algebra core.
- The reported interacting builds, critical coupling, `b!=0` branch, and
  continuous `r(g)` curve are context only.
- The runner now checks the exact finite obstruction instead of printing it as
  prose: epsilon is constant on `hw=1`, the epsilon shift leaves the triplet,
  invariant diagonal generation operators are scalar, a non-scalar diagonal
  splitter breaks `C3`, and `Q=1/3+(2/3)r` holds for the contextual r-values.

Verification:

- `python3 scripts/flavor_interacting_matter_build_2026_05_30.py`
- `python3 scripts/cached_runner_output.py scripts/flavor_interacting_matter_build_2026_05_30.py --timeout-sec 120`
- `git diff --check`

Remaining blocker:

The packet still lacks a first-principles matter-action derivation of the
nonperturbative branch, critical coupling, channel ratio, and `r(g)` curve.

PR: pending
