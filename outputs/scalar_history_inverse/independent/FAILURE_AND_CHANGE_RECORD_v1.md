# Failures, recovery and source movement

The original author v1 was replayed unchanged and returned exit 1 with
42 passes and two failures. Its complete stdout, stderr and run metadata
are author_original_v1_attempt01.*. The first failure comes from subtracting
instead of adding the Friedmann residual in the scale-factor variation:
the checker expression is minus twice that residual off the constraint.
The second comes from simultaneous substitution reinserting a free c
through phi=c log(t). V2 fixes those checker operations and adds two
fixed-rho versus fixed-r controls. Its unchanged copy returned 46/0 and
exit 0. Both receipts match their original bytes. The exact code change
is preserved in AUTHOR_V1_TO_V2_DIFF_v1.json.

No independent mathematical control failed or timed out. The 64-control
and 31-control runs each succeeded on their first execution. Their nonempty
stderr files contain deliberate progress lines, not suppressed errors.

Canonical movement was observed and retained:

1. An initial textual view still said “Primary computation:”. The first
   exact byte snapshot already captured “Primary runner:”. No hash is
   asserted for the earlier unbound textual view.
2. CANONICAL_SOURCE_SNAPSHOT_v1.json binds note 4ca2b557..., primary
   d540f1b5... and helper 3709bd34.... The author then added the requested
   r(t) C2 condition and qualified the missing general full-history
   conditioning theorem, clarified fixed numerical units, and moved the
   unchanged obligation table. Snapshot v2 binds note e1cde043...;
   primary/helper were unchanged. CANONICAL_NOTE_CHANGE_v1.json preserves
   the exact UTF-8 diff, byte count and SHA256. No equation changed.
3. The first canonical replay passed 58 controls and 15 integration checks.
   Its output metadata described all repository reads as integrity-only,
   although the helper is imported and executed. The author corrected that
   one string. Snapshot v3 binds primary b0fd9b26..., with note/helper
   unchanged; CANONICAL_PRIMARY_METADATA_CHANGE_v1.json proves the exact
   replacement and preserves the diff losslessly. The final replay passed
   58 controls and 16 integration checks, including the corrected role.
   The old replay and its bindings were not overwritten.

One packaging-only attempt incorrectly remembered the earlier metadata
string. Its presence assertion failed before any file was written.
metadata_snapshot_attempt01.py preserves the executed heredoc; its stdout,
stderr and run record retain the actual traceback and exit 1. The script
was restored verbatim from the executed tool call rather than rerun, and no
unmeasured duration is invented. A following patch-serialization attempt
could not represent its empty stdout file and was rejected before applying;
the exact tool diagnostic is in the same run record. Exclusive file writes
then preserved that evidence. Attempt02 changes only the expected old
string, succeeds under a 120-second bound in 0.028 seconds, and captures the
final snapshot and integration-checker version. These are packaging errors,
not scientific failures. The snapshot scripts are historical one-shot
packaging programs with their absolute source path retained.

A narrow file-discovery command also named two nonexistent directories
(tools and audits) and emitted directory diagnostics. It did not execute
science or alter files; subsequent discovery used the existing docs path.

CANONICAL_SOURCE_SNAPSHOT_v1.json also preserves the author's
mutation_attempt01.json. That record reports one ineffective mutation
choice and one overly broad replacement causing an interrupted driver.
It was inspected as historical failure evidence only; this check does not
claim independent reproduction of that mutation suite.

Earlier frozen proofs, outputs, source snapshots and actual failed attempts
remain byte-identical. No author file, git state, external application or
other worktree was changed by this check.
