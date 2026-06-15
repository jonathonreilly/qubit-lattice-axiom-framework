# Artifact Plan

- Source note: make the existing exact runner parser-visible with `Runner:`.
- Runner caches: refresh both cited caches with `cached_runner_output.py`.
- Verification: prove parser extraction and cache freshness locally.
- Audit outputs: regenerate only for local measurement, then restore before
  commit.
