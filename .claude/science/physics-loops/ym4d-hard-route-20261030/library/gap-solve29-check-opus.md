lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:11Z

# Check of row 1254 (`library/gap-solve29-astra62.md`)

Queue row 1261, `gap-solve29-check-opus`. Cross-provider check: the author
of row 1254 is gpt-6.2-astra max (Mac mini Codex runner); this checker is
Claude Opus 5.5 max on the Mac mini Claude worker 3. Started 2026-11-20T11:11Z
(date -u). Source file read at commit f2d7eba78.

Verdict labels: HOLDS, HOLDS AFTER CORRECTION, FAILS, each with the line of
the checked file. Every step below is checked by hand. No numeric run is a
proof step here.

## Plan (at most eight steps)

1. Read the checked file in full; inventory its labelled statements with line
   numbers; read FINISH.md rules and the earlier rows it cites.
2. Check the same-torus Wilson cube comparison (37) line by line.
3. Check the local-source criterion (32)-(33) line by line.
4. Check the remaining PROVED statements, in order.
5. Check the ARGUED, GUIDE and OPEN statements and the RESULT line.
6. Restatement question: is (37) a restatement of an earlier row? Grep
   `library/open-core.md`, the FINISH rows and the earlier `gap-solve*` files.
7. Read each cited earlier statement and its proof where a step depends on it.
8. Verdict table and RESULT line.

## Progress

(Steps are appended below as they finish.)
