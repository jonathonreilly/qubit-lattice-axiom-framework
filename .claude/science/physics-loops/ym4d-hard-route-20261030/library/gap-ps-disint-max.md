lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T00:06Z

# gap-ps-disint-max (queue row 957): Piazza-Shen disintegration against (LSI-J-seed)

Worker file, written section by section. Pinned at commit 5da1cade7 of `claude/ym4d-hard-route`.
Author: Claude Fable 5.2 (max), Mac mini worker 1, as AUTHOR. Not checked by another model.
Labels used: PROVED, CONDITIONAL (on named inputs), GUIDE (numeric, proves nothing), OPEN.

Credit. The new input is Piazza and Shen, arXiv:2610.35286 (Theorem 1.1). The lattice two-slice setting and
the vacuum factors follow the gap lane of this repository, which builds on the account of Ethan Sussman and
Levent Alpoge (with Claude and Codex as authors of their text). Each section names what it takes from whom.

## 0. Plan (at most eight steps; one step per response)

1. Read the target: (LSI-J-seed), Theorem BR, Corollary BR-J and Section 7.3 of `library/gap-fc-max.md` (row 947),
   and the two prior digests (`library/prior/gap-fullread-2.md` Section 1, `library/prior/gap-lit-bridge-lsi.md`).
   Duplicate check against `library/open-core.md` and the FINISH rows. Write the exact statements.
2. Read Piazza-Shen itself (`~/ym4d-papers/dl-2026-11-11/`): the two-scale criterion, the block law, the coarse
   law, and where dimension 2 is used. Write the proof skeleton with line anchors.
3. STEP 1 of the row: which step fails in 3D/4D and why; is the two-slice law J closer to their 2D setting
   (disintegration over temporal links, or over one slice given the other).
4. STEP 2 of the row: fact tests (compact U(1) Coulomb phase, frozen Q_8 and 2T, SMALL-BOX use of the box size,
   the worst-case ceilings 2/3, 0.775, 4 G_3 = 1.0109, the Bakry-Emery ceiling at beta 1 of row 941).
5. STEP 3, stage A: the two-scale disintegration of J written as a real proof attempt; the block conditional
   laws and their LSI constants.
6. STEP 3, stage B: the coarse law at the box size; close it or state the exact obstruction.
7. If it does not close: the smallest unproved inequality, and one GUIDE test (run only under the numeric lock
   and with 50 percent memory free).
8. Verdict table and the RESULT line.

Status log (updated in place):

- 2026-11-14T12:06Z: file created; steps 1-8 not started.
