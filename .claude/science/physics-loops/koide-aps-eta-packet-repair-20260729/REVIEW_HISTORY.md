# Review History

Initial diagnostic:

- the source note and runner source were complete;
- cached stdout was clipped by the cache reader's legacy 6,000-character
  default despite the audit runner's 20,000-character policy;
- the 12,320-byte named authority was clipped by the generic 10,000-character
  cap.

Pre-review validation:

- focused regression: 3 tests passed;
- Python compilation: passed;
- `git diff --check`: passed.

Repo-native review-loop disposition: `PASS`, ready for independent audit.

- Physics/scope: no mathematical statement changed; P1--P3 and both explicit
  exclusions remain visible. The N1--N8 gate passes for scope boundaries only,
  not for an impossibility claim.
- Code/runner: the authority override is exact to one claim/dependency pair;
  cached stdout uses the already-declared 20,000-character policy; the existing
  teleportation override remains green.
- Evidence: the real restricted packet contains the byte-complete authority
  and full SHA-verified cache body with no load-bearing clipping marker.
- Audit compatibility: the dated transport record changes the target note
  itself. A full validation pipeline detected exactly one audited-row hash
  change and placed this target in the ordinary queue with `ready: true`.
- Pipeline: completed with no lint errors; strict lint also reported no errors.
  Generated audit/status outputs were restored and are not part of the branch.
- Tests: 22 focused packet/cache tests passed; the primary runner reports
  `PASS=41, FAIL=0`; cache freshness reports 1 fresh, 0 stale.
- Extended diagnostic: 164/172 orchestrator tests passed. Six containment
  tests could not execute because the managed sandbox denies `ps`; two
  clean-main tests saw the deliberately dirty repair worktree. These failures
  are environment/precondition-specific and do not exercise the changed cache
  excerpt or authority-limit paths.
- Freshness/lock limitation: `git fetch` and the shared lock path were denied
  by managed host permissions. Local `HEAD` and `origin/main` both resolved to
  `880f00b551830938bcbc2097137c822f4e1b2347`; a branch-local lock protected the
  work block.
