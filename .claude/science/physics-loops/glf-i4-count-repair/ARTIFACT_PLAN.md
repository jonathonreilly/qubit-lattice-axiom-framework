# Artifact Plan

- Patch the GL(F) source note expected-output count to `PASS=39`.
- Add a changelog entry stating the repair is source-accounting only and leaves
  the matter-functional clause `I-4` open.
- Re-run the GL(F) checker.
- Run basic diff/compile/protected-surface checks.
- Open a ready PR for reviewer extraction.
