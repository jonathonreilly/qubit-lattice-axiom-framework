lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T12:03Z

# gap-mini-solve-f-fable: the mass gap of four-dimensional SU(2) Yang-Mills

Queue row 1195. Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit 9c5f9600f. Started 2026-11-20T00:03Z.

Labels used below: PROVED (every step written here or in a cited library file), ARGUED (an argument with a named missing step), GUIDE (heuristic or numeric, not a proof step), OPEN.

Status of this file: in progress. Sections are appended one step at a time.

## 0. Log

- 00:03Z. File created. Reading FINISH.md (rules, row 1195), GOAL.md, `parts/gap.md`, and the earlier gap-mini results.
- 00:25Z. Read in full: GOAL.md; FINISH.md L1-84 and L299-356 (rules); row 1195; `parts/gap.md` (all 322 lines); `library/gap-council-brief.md`; `library/gap-council-synthesis.md`; the FINISH RESULT lines of rows 1177-1196. Not read: the other 460 `library/gap-*` files (searched by grep when a statement is used).

## 1. Repo search: where the lane stands (what I rely on, by row)

All of this is prior work of the lane; none of it is mine. Credit: Balaban (ultraviolet renormalization group), Sussman and Alpoge with Claude and Codex (the complete account), the lane's rows as cited.

- Target. Jaffe-Witten for SU(2): a Wightman/OS theory on R^4 with spectrum {0} and [Delta, infinity). Lattice form: Wilson SU(2) on periodic tori along the asymptotically free trajectory (brief, Section 1).
- Consumer side, on file: one seed at one physical box size gives a uniform gap on all larger dyadic boxes and carries to finer cutoffs (Theorems S, SH, rows 697-705; Theorem ZD-c, row 720). The wall (W): bounded Casimir excess (BDD-Delta) together with unbounded size-times-gap (Z-UNB).
- The gap clause alone needs less (rows 731, 1161, 1179 Theorem BP, unchecked in part): the one-cube physical neutral bound (N-phys) plus the continuum datum. By rows 1180 and 1184 (checked by row 1187), (N-phys) is a neutral lattice gap at arbitrarily weak coupling with a lower bound of asymptotic-scaling type.
- Every positive result on file is non-selective (it also holds for compact U(1), a frozen group, or a product with a massless factor). The missing piece is one selective inequality at order-one effective coupling (brief, Section 3).
- The sibling rows with this same plain brief (1188-1190; 1193, 1194 running) screened 12 to 17 standard attacks each and found all on file.

Consequence for this row: a further screening of standard routes has no value. This row picks one mechanism, checks it against the record by grep, and works it to a proof or to its first failing step.
