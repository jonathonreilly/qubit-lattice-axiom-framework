lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T02:04Z

# Row 1468: design of the missing K-II tool

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, fresh session at commit b6b622f51. Research-stage
working state. Not an audit, no status. Every item below is marked proved, sketched or guessed.

Started 2026-11-24T14:04Z (date -u).

## 0. Plan (written first, before reading the inputs)

Task (FINISH row 1468): design the K-II tool, a renormalization step at order-one coupling that carries a sign.

1. Read the rule sections of FINISH.md and GOAL.md (done), then the RESULT parts of rows 1326, 1332, 1386, 1418-1437,
   1442, 1460-1467 and the statements they point to. Log one line per source in Section 1.
2. Repo search and registry grep (open-core.md, FINISH rows) for each candidate statement before calling it new.
3. Section 3: the block map and the exact one-step statement (what is carried, the sign, the iteration to (M-io-exists)).
4. Section 4: filter tests t1-t6 against U(1), Villain U(1), 5D.
5. Section 5: sizing of the finite computation and whether Lean `decide` / `norm_num` can check it.
6. Section 6: the first buildable component and its decisive outcome.
7. Section 7: an obstruction for a stated class, if the step cannot exist.
8. Section 8: the next two rows and their decisive outcomes. RESULT line.

Status log (one line per step, times from date -u):

- 2026-11-24T14:04Z file created, plan written.
- 14:04Z read FINISH rules, GOAL.md, rows 1326, 1332, 1386, 1442, 1460-1467 (RESULT text). Target = (M-io-exists); missing input = K-II (or K-I local); release floor above 2^2800 (row 1464, unchecked); LOSS for the plain kernel (row 1460, check 1463).
- 14:04Z read rows 1418-1437 (RESULT text): tensor-network step sized and rejected by cost and by filter (1418); one-link and two-cycle signed terms cancel or are tiny (1421-1431); Lean kernel replays exist (lean/glue, lean/ring, lean/haar); heat-factor class closed (1434).
- 14:05Z read row 1386 4.1-4.5 (STEP, Remark PAIR, requirements (a)-(i), K-I/K-II/K-III, t1-t5), row 1442 4.2 (t6), row 1332 Section 6 (Proposition CH, END, steps OPEN), row 1460 Sections 2-3 (LD-1, LD-2, LD-3, SE, LOSS, RANGE).
