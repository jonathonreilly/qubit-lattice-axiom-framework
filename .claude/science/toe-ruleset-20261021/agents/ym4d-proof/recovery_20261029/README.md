# Recovery checkpoint, 29 October 2026

The coordinator recovered the pending work from Claude session
`a931aaa3-5369-4512-9e8d-b8590010706c`, on branch head
`46dc04b05c5842a03ae3af64caa77628f099128f`. That head already matched
`origin/claude/ym4d-proof-draft`; the missing work was in the working tree.

`manifest.json` records the exact SHA-256 and byte length of **28 recovered
files**: eight completed Codex reviews, eight interrupted Claude deliverables
(two partial derivations and six pre-stated plans), and twelve check files
(three scripts, three criteria files, three stdout files and three stderr
files). The recovered bytes are preserved. Earlier commentary estimated 29;
the explicit file inventory corrects that count to 28.

The manifest also preserves the eight failure notifications' task IDs and
timestamps, and the model/effort/session metadata extracted from all eight
Codex runtime banners: `gpt-6-astra`, `max`. These are provenance facts, not
mathematical certification. The Claude workers stopped on the weekly usage
limit; the reviews completed afterward.

`briefs/` contains byte-preserved copies of the eight interrupted assignments
and their shared rules. Absolute scratch paths inside them are historical.
The current lane directory is this directory's parent; the named worker files
and reviews are there. The original shared `REVIEW_BRIEF_55.md` is now beside
the task briefs. Use the current [handoff](../HANDOFF.md) and late reviews to
correct their stale premises before resuming. These archived briefs do not
override the user's current instruction to continue with Astra max workers.

`reruns/` records fresh executions of the three recovered scripts. Their JSON
receipts distinguish matching historical stdout from mathematical validation.
A same-script replay is not an independent proof. Original criteria and
outputs under `../checks/` are untouched.

The original files' source preimages also have a local backup outside Git at
`/private/tmp/ym4d-recovery-20261029/originals/`. The Git payload is sufficient
without that backup. Full conversations, tool logs and downloaded third-party
papers are not copied into this PR.

Current scientific status and review dispositions are maintained in
[HANDOFF.md](../HANDOFF.md), [PROOF.md](../PROOF.md) and
[SESSION25_RESULTS.md](../SESSION25_RESULTS.md), not inferred from this
preservation inventory. No existence or mass-gap theorem is certified here.

All three recovered scripts replayed successfully with matching stdout.
`validation.json` records the scope. Whole-index whitespace checking reports
blank final lines and trailing spaces in preserved original evidence/logs;
those bytes are deliberately untouched. The newly authored status surfaces
pass their focused whitespace check. The original a3 stderr contains timing
and resource metadata with exit 0, rather than a failed calculation.
