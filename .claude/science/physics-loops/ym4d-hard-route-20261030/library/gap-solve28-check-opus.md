lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:50Z

# Check of row 1246 (`library/gap-solve28-astra62.md`), queue row 1253

Checker: Claude Opus 5.5, max effort, Mac mini worker 3, started 2026-11-20T09:50Z
(date -u). Repository commit fd73d8c6a on branch `claude/ym4d-hard-route`.
Cross-provider check: the author of row 1246 is gpt-6.2-astra (max), Codex runner.
This check is by hand; no numeric run is a step of any verdict.

## Plan (at most eight steps)

1. Read FINISH.md rules (queue row 1253, efficiency, build-on-published-work) and
   the whole of `library/gap-solve28-astra62.md`; list its statements with labels and lines.
2. Check positive claim A: cyclicity of spatial plaquette histories for the
   finite-cutoff centre-neutral sector (statement, proof, cited rows).
3. Check positive claim B: the fixed-depth slab with a temporal mean on each cut
   detects the exact spectral edge (statement, proof, cited rows).
4. Check every remaining statement of the file, line by line.
5. Read the earlier rows the steps depend on (cited statements and their proofs);
   decide whether the main comparison is a restatement of an earlier row
   (grep `library/open-core.md`, FINISH rows, earlier `gap-solve*` files).
6. Check the published-work credits (`library/prior/gap-onebound-read-sol.md`,
   Sussman-Alpoge account) where the file relies on them.
7. Verdict table: HOLDS / HOLDS AFTER CORRECTION / FAILS per statement, with line.
8. RESULT line.

## Status

Step 1 in progress.
