lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T02:57Z

# Row 1474: the missing tool T2, a representation for an order-one block step

Worker file of queue row 1474 (`gap-k2-t2-representation-fable`), pinned at commit a3c24b36f on
`claude/ym4d-hard-route`. Started 2026-11-24T14:57Z (date -u). Research-stage working state; nothing here is a
public claim. Every statement is marked proved, sketched or guessed. Nothing is committed or pushed from this
machine.

## 0. Plan (written first, per the save protocol)

1. Read the record the row names: rows 1460, 1461, 1466, 1468, 1470, 1471 and their checks;
   `library/gap-k2-tool-design-fable.md` sections 4-6, `library/gap-k2-floor-sizing-opus.md`,
   `library/gap-k2-end-class-fable.md`. Record which representations are already closed and why (cost or closure).
2. State T2 as a precise problem: a class C of local rules, a map S (the Q2 step or another exact self-similar
   map), with (a) S(C) inside C at order-one coupling, (b) the inclusion a finite check of bounded size,
   (c) selectivity under the filter t1-t6 (rows 1386, 1442).
3. Attack: candidate representations not on the closed list; for each, size of one step's check at beta about 2.3.
4. If no candidate survives for a stated class, prove the obstruction for that class.
5. End with the next two rows and their decisive outcomes, and one RESULT line.

Free memory at start: 37 percent (memory_pressure), below the 50 percent bar for a numeric job; no numeric job
is started unless that changes.

(Sections follow as the steps are done.)
