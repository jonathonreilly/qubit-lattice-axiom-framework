lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T18:14Z

# Row 1356, gap-mini-mneutral-fable: attack on (M-neutral)

Worker: Claude Fable 5.2 (max effort) on the Mac mini, pinned at commit 30a300a5c of branch
`claude/ym4d-hard-route`. Research-stage working state; nothing here is a public claim. Every statement below
carries one of the labels PROVED, ARGUED, GUIDE, OPEN. A "PROVED" here means proved in this file and not yet
checked by anyone else.

## 0. Status log (times from `date -u` in the command that wrote the line)

- 2026-11-21T06:14Z: file created (save protocol). Nothing read yet beyond the queue row, GOAL.md and my navigation notes.
- 06:32Z: read the row, GOAL.md, the rule sections of FINISH.md, row 1353's file in full, the sibling file of row 1354, parts/gap.md L8-104, Theorem ZD-c, Identity I1, row 1168 (19)-(21), the route tables of rows 1180 and 1184; registry grep run; Section 1 written.

## 1. Repo search and inputs (written 06:32Z, `date -u`)

Rule 0a and "Repo first". Before any derivation I searched `library/open-core.md`, every `library/gap-*.md`,
`library/prior/gap-*.md`, `parts/gap.md` and the `FINISH.md` rows with `/usr/bin/grep -l -i -F` for the terms of
each statement I considered. `library/open-core.md` has no line on (M-neutral), (N-phys) or a rank-one test.
Cross-branch search (main and the open YM4D pull requests): not repeated; rows 1351 and 1353 record it for the
same statement on the same day (`gap-blockstep4-astra62.md` L3), with no proof of the neutral seed found.

Inputs read. In full: `library/gap-mini-neutral-step-fable.md` (row 1353; its check, row 1355, has no file at
this pin, so its statements are "unchecked at this pin"); the file of the sibling row 1354 as far as it exists at
this pin (`library/gap-mini-nphys-fable.md`, Steps 0-2). In part: `GOAL.md`; `FINISH.md` L1-84, L320-351 and the
RESULT lines of rows 1326, 1331, 1332, 1335, 1340, 1342, 1349, 1351, 1352; `parts/gap.md` L8-104;
`library/gap-phys-seed.md` L283-327 (Lemma Z3, Theorems ZD and ZD-c, Corollaries Z2 and Z4);
`library/gap-compress-opus.md` L28-60 (Identities I1, I2); `library/gap-solve11-astra62.md` L286-320 (row 1168,
(19)-(21)); the route tables of rows 1180 and 1184 (`library/gap-mini-neutral-fable.md` L134-200,
`library/gap-mini-neutral2-fable.md` L109-200).

What the target is, on file. (M-neutral) is (N-phys) up to the choice of times (row 1353, Corollary BT2).
(N-phys) is the crux lemma (GLUE-FP)_sigma of rows 895 and 920 with other constants, and its consumer is row 1161
(7). Rows 1180, 1184 and 1353 are three earlier attacks by this model on the same statement. Their route tables
hold about 25 routes, each with its first failing step. I do not repeat them.

Matches for every form of the target that I derived again in this session (none is called new below):

| Form (my words) | On file | Verdict |
|---|---|---|
| The squared Hilbert-Schmidt distance to rank one is the excited trace at twice the time; chi-square mutual information of two slices of the vacuum chain | Identity I1, `gap-compress-opus.md` L36-46 (row 839); Lemma BT of row 1353 | on file |
| Purity: (N-phys) says Tr rho^2 >= 2/3 for the neutral thermal state; Renyi-2 and min-entropy forms | Identity I2, `gap-compress-opus.md` L48-58; `gap-skeleton-max.md` L264; row 1354 Step 1.1 | on file |
| Trial vectors: the test holds if and only if some unit vector phi has <phi, P_0 T^w phi>^2 >= (21/25) Tr (P_0 T^(2w)); two-period form Z_+(2w)^2/Z_+(4w) | Lemma TP of row 1342 (`gap-seed-audit-fable.md` L159); row 1168 (19) (the trial vector there is the square root of the slice marginal) | on file |
| Hellinger or total-variation independence of the two opposite slices of the periodic torus gives the neutral count; local readings on collars suffice | row 1168, `gap-solve11-astra62.md` (19)-(21), L286-316 ("The same upper bound 1/32 with H = G gives the periodic neutral excited count s(u) <= 1/2"); mutual information also suffices there | on file, PROVED there, checked by row 1169 |
| Gap plus count: the operator-norm form of the test (gap of the cube in units of 1/L above 256 D_0 + 30) together with a bounded torus excess | Theorem ZD-c and Corollary Z4, `gap-phys-seed.md` L311-322 (row 720); Lemma G5 of row 895 | on file |
| Thermal pressure, rotated frames, Casimir energy of a periodic direction | Lemma Z, Lemma Z', Proposition Delta (`gap-ladder-max.md` 5.7); Lemma CD of row 1259; rows 1180 R2, 1184 route 4 | on file |
| Operator inequalities against the electric operator (min-max, Golden-Thompson) | Lemma R4 of row 1180 (`gap-mini-neutral-fable.md` L208); `gap-constraints-max.md` B6 | on file: loses the vacuum energy |
| The vacuum chain is the electric product channel tilted by a positive function; link refresh | row 1135 (link-refresh model), row 1132 statement (A), row 1206 Theorem 2.3 (`gap-agy-solve2-argon.md` L104) | on file |
| Coupling integration, monotones, rigidity, thin twisted tori, Bakry-Emery curvature | rows 1180 R3, R5-R9; row 1184 routes 3, 6, 8, 9 | on file |

Two items had no match and are used below.

- The sharp constant of the rank-one test (Section 2, Lemma M1). `grep` for "Mirsky": 0 files; "Eckart": 1 file
  (`gap-solve32-check-opus.md` L310, about another operator); "4/21": no relevant hit. It changes a constant only.
- Lipschitz transport with comparison of ALL eigenvalues (E. Milman's observation). `grep` for "Milman": 3 files,
  all saying "not tried" (`gap-transport-check.md` L183, row 915; `gap-afield-a-max.md` L188 and L341, row 1031,
  item F6: "not tried, needs a bounded perturbation; blind"; `gap-target-max.md` L156). "Caffarelli", "Brenier",
  "curvature-dimension": 0 files. Section 3 takes this route, because it is the one tool I know that gives the
  gap and the count together, in the law of the model, with no supremum over boundary values.

Credits. K. Wilson (the action and the transfer operator); K. Osterwalder and E. Seiler, M. Luscher (transfer
operator, reflection positivity); T. Balaban; E. Sussman and L. Alpoge with Claude and Codex as authors of their
text (the account, the trajectory); G. 't Hooft, G. Mack and V. Petkova (twists, flux sectors, centre split);
L. Mirsky and C. Eckart, G. Young (singular value inequalities); E. Milman (eigenvalue comparison under
contracting maps), L. Caffarelli, Y.-H. Kim and E. Milman, D. Mikulincer and Y. Shenfeld (Lipschitz transport
maps); M. Luscher (trivializing maps). In this lane: gpt-6.2-astra (rows 1161, 1168: the neutral consumer and the
Hellinger test); Claude Opus 5.5 (Identity I1); Claude Fable 5.2 (rows 1180, 1184, 1342, 1353).
