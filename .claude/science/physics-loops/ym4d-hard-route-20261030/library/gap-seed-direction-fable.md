lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T16:32Z

# gap-seed-direction-fable (queue row 1515): direction for the physical seed after rows 1510 and 1511

Status: IN PROGRESS. Research-stage working state; nothing here is a public claim. Unchecked.
Pinned at commit c4db00930 on branch claude/ym4d-hard-route. Started 2026-11-25T04:32Z (date -u).

## 0. Plan (written first, per the save protocol of the row)

Task of the row: from the target (PUR-io) and the results of rows 1510 (`library/gap-seed-solve-fable.md`)
and 1511 (`library/gap-seed-solve-astra62.md`), find the attack that could still succeed, or prove that every
attack of an explicitly stated family fails. Decide what kind of input the calibrated obstruction of row 1511
still allows:

- (a) scaling of the action insertion,
- (b) cancellation between signed seam responses,
- (c) rates integrated over shrinking coupling intervals,
- (d) an in-law carry as in row 1510 (PC, REV),

and whether any of these has a first lemma that is not equivalent to a closed line.

Steps, each appended as its own section when done:

1. Read rows 1510 and 1511 in full; restate (PUR-io), the refutation of (W), criterion (3) and the calibrated
   obstruction in the exact form used below, with line anchors.
2. Formalize the family of attacks the obstruction covers, and state precisely what it leaves outside.
3. Test each of (a)-(d) against the obstruction and against the closed lines (grep `library/open-core.md` and
   the FINISH rows before calling anything new).
4. Decisive outcome: one named attack row with its first lemma, or an obstruction theorem over a stated family,
   or the statement that no such row exists on present knowledge, with triggers.
5. Next two rows with their decisive outcomes.

## Status log

- 2026-11-25T04:32Z file created with plan; no reading done beyond the queue row and GOAL.md.

<!-- APPEND-MARKER -->
