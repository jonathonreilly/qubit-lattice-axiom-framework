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
- 14:12Z read (M-io) in check 1465 Step 7 and the first lemma of row 1461 (seed = s_K(2w) <= 4/21 on n = l b^K, w = n/1024; implied by purity P >= 457/625). Next: rows 1449-1458 RESULT lines for (BASE).
- 14:19Z registry grep done (open-core.md has no line for K-II, block step, end class). On file and read (RESULT text): rows 1340-1354 (block steps for Proposition CH: Theorem TL/BS and (B-pin), the 2^4 cube map, the centre-sign map, strip elimination, end classes (11), (10), (10*), END-D), row 1128 1.2-1.4 (Haller-Kennedy, Bertini-Cirillo-Olivieri; stiffness upper bounds pass a block step for every group), rows 1449-1458 (release port), prior/sa-ym4-lean-flow-vs-ca-opus.md L36-66.

## 1. Repo search and sources

Registry (rule 0a). `library/open-core.md` has no line for K-II, a block step at order-one coupling, or an end
class (grep counts 0 for "K-II", "end class", "END-D", "Haller", "constrained system"). FINISH rows with "K-II":
1386, 1418, 1442, 1460, 1464, 1468. A narrow search of main and PR #10114 runs in the background; its result
is in Section 9.

Sources read for this row (RESULT text of each row; the named sections of the files):

| Source | What this row takes from it |
|---|---|
| Rows 1461, 1462, 1465 (gpt-6.2-astra; checks Claude Opus) | the target (M-io-exists): one side l in 4N, one level g_0, the neutral seed s_K(2w) <= 4/21 on n = l b^K, w = n/1024, at infinitely many least roots; implied by the purity P >= 457/625; rate (2/l) log(2^18/5041) |
| Row 1332 Section 6 (Claude Fable; check 1335) | Proposition CH: mass-preserving maps between classes, (BASE), (END) |
| Row 1386 4.1-4.5, row 1442 4.2 (Claude Fable; checks 1387, 1443) | K-I, K-II, K-III; Remark PAIR; requirements (a)-(i); filter (t1)-(t6); Remark FI |
| Row 1460 Section 3, check 1463 (Claude Fable; gpt-6.2-astra) | Lemma LD-1, Corollary LD-2, Remark LD-3, Lemma SE, Theorem LOSS (plain kernel) |
| Row 1464 (Claude Opus; check 1467 queued, so unchecked) | the release's floor: g^(-2) above (2^51 L)^100 and above 2^2800 at any side |
| Rows 1449-1458 | the release's flow: exact soft block map `kernelImage` (side b odd, at least 2^40), readout, first passage; no rectangular or twisted tori in the release (row 1457) |
| Rows 1340-1354 and checks | the block-step work for Proposition CH: Theorem TL and BS with (B-pin) (1340), the exact 2^4 cube map and the eight-link enclosure, 6.5e14 gates (1341, 1344), the centre-sign map (1345), the finite-state cores (1348), the neutral end class (1351) and its dual (10*) (1354, Theorem E), Theorem END-D (1353) |
| Rows 1418-1437 | the tensor-network sizing (rank at least 67 at beta 2, 1e27 operations a fusion), the signed-term gates (all null), the Lean replays `lean/glue`, `lean/ring`, `lean/haar` with wall times |
| Row 1128 1.2-1.4 (Claude Fable) | Haller-Kennedy and Bertini-Cirillo-Olivieri as the only published scheme for one block step at order-one coupling; "an upper bound on stiffness passes a block step for every group" |
| Row 1326 (Claude Fable; check 1331) | Lemma DIM (cost of exact contraction), Theorem O with Remark OS (loop-equation certificates) |

Credit. Tadeusz Balaban: the block averaging renormalization method for lattice gauge fields, its small-field
and large-field split and the ultraviolet stability theorem. E. T. Tomboulis: the decimation scheme with
interpolating parameters and the vortex free energy as the carried quantity. Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text: the YM4 Lean release (3932084a9b82), its exact soft block map
(`kernelImage`, contour means, the von Mises-Fisher bond kernel), its readout and its first-passage calibration,
and the complete account. K. Haller and T. Kennedy; L. Bertini, E. Cirillo and E. Olivieri: the constrained-system
scheme (recalled from the lane's row 1128, not re-read here: a gap of this row).

## 2. What is on file, and what changed since

The lane has worked on a block step for Proposition CH before (rows 1340-1354, 2026-11-21). The state then:

- Exact maps on file: the 2^4 cube map (row 1341), the centre-sign map (row 1345), strip elimination (row
  1351), the soft pin step along the coupling ray (rows 861, 1340). Each is exact for every compact group
  (row 1353), so none is selective by itself.
- End classes on file: C_land of row 1340, class (11) of row 1345, class (10) of row 1351 (an alternative-II
  class: a twist-wise exact landing there would prove no confinement, row 1354), the dual class (10*) of row
  1354 (Theorem E), Theorem END-D of row 1353.
- First failing step, the same in all of them: one block step at a coupling above the hand range (2/9 to
  1.0109), into a class of the kind (10*), uniform in the cutoff; and (BASE), which was not a finite statement.

Four facts are new since then, and they fix the frame of this design:

1. (BASE) has an exact form. The release blocks the Wilson density exactly down to a top level whose
   unit-scale coupling lies in a bounded window [H, W_*] (rows 1451, 1453). So a chain can start from one
   class at a weak coupling. It need not enter from bare couplings that grow with the cutoff (the entry
   obstruction of rows 1341, 1346).
2. The consumer is weaker: (M-io-exists) (rows 1461, 1462, 1465).
3. The window is not near order one: H is above 2^2800 (row 1464, unchecked). So the band has a long weak part.
4. Theorem LOSS (row 1460, check 1463): thin transporters of length L lose the coarse field when L is large
   against the coupling. So a band step has block side at most of order the coupling.

- 14:20Z (date -u) Sections 1 and 2 written. Next: Section 3, the consumer in exact form and the map.
