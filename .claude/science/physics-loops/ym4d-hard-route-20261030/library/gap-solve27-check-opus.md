lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:06Z

# Row 1245: check of row 1236 (`library/gap-solve27-astra62.md`)

Queue row 1245 (FINISH.md line 1326): a line-by-line check by hand, cross-provider, of
`library/gap-solve27-astra62.md` (row 1236), positive claims first: the static-pair threshold (25),
the multiplicity comparison (27), the physical-energy estimate (33); then everything else. Also: is
the main comparison a restatement of an earlier row? Verdict per statement: HOLDS, HOLDS AFTER
CORRECTION, FAILS, with the line. A numeric run may guide only.

Provenance: Claude Opus 5.5 (max reasoning), Mac mini worker 1, started 2026-11-20T09:06Z (date -u),
checkout pinned at commit 3a45c201f on `claude/ym4d-hard-route`. The checked file was written by a
different provider (astra62), so this check is cross-provider; it is still one check by one model.

## Plan (at most eight steps; one step per response, result appended after each)

1. Read FINISH.md rules (head, efficiency rules, Build on published work), GOAL.md, and the checked
   file in full; list every numbered display and statement of the checked file with its line.
2. Check the static-pair threshold (25) with the rows it cites.
3. Check the multiplicity comparison (27) with the rows it cites.
4. Check the physical-energy estimate (33) with the rows it cites.
5. Check everything else, line by line, in file order.
6. Restatement question: grep `library/open-core.md` and the FINISH rows for the main comparison.
7. Optional numeric guide (under the numeric lock, only at 50 percent memory free or more).
8. Verdict table (statement, line, verdict) and the RESULT line.

## Status log

- 09:06Z step 0: file created with the plan.
- 09:20Z step 1 done: rules, GOAL.md and the checked file read in full (475 lines); inventory below.

## Step 1. Inventory and dependency map

The checked file (pinned `b71c9f52a` in its own header; read here at `3a45c201f`) has 35 tagged
displays and 55 PROVED paragraphs (lines 26-471), one ARGUED paragraph (L241), GUIDE paragraphs and
two OPEN paragraphs (L15, L473). Its RESULT (L475) claims three positive results: (25), (27), (33).

Cited earlier rows and their checks (all read from `RESULT` lines at `3a45c201f`):

| Row | File | Used for | Check row, verdict |
|---|---|---|---|
| 1143 | `gap-solve-astra62.md` | (8) open-line isometry and formula | 1144, all HOLD |
| 1145 | `gap-solve2-astra62.md` | (1) one-link adjoint mean, (16)-(18) static charges | 1146, HOLDS |
| 1149 | `gap-solve4-astra62.md` | (16) Bessel-ratio monotonicity | 1150, HOLDS |
| 1151 | `gap-solve5-astra62.md` | (21)-(24) dissemination, pressure, open boxes | 1152, HOLDS |
| 1155 | `gap-solve7-astra62.md` | (9) moments of sqrt(beta)abs(1-U_p) | 1156, HOLDS |
| 1163 | `gap-solve10-astra62.md` | (13)-(14) rectangular source (hypothesis only) | 1164, HOLDS |
| 1231 | `gap-solve26-astra62.md` | (1)-(2) radius comparison, (4)-(5), (8)-(9) | 1235, HOLDS (some items given PL3, PL5) |
| 860 | `gap-hs-max.md` | Lemma OS (electric spin insertion) | to read |

Dependency map of the three positive claims (my reading; to be verified in Steps 2-4):

- (25) = lower bound (24) + upper bound from ribbons. (24) uses the score inequality (23) (self-contained),
  the slow-band plaquette bound (20) (which uses row 1151 (21)-(22a)), the ribbon trial r_xy >= 1 - O(1/beta)
  (row 1143 (8) and a half-tilt bound), and the resistance limit (L328). The upper bound uses the open-line
  formula W(gamma,s) <= r_xy^s (row 1143 (8)), the fixed-loop weak-coupling limit (26) (row 1231 (8)-(9),
  row 1151 (24), row 1155 (9), nested-projection coupling of row 1231 (1)), and the Fejer limit (L344).
- (27) = (24) + the ribbon estimate (28) in every slow state + min-max through the open-line isometry.
  (28) uses Schatten-Holder slab dissemination (L366), the box upper bound of (22) (L276-280) applied to a
  ribbon array (L368-373), and kernel domination for the clipping (L375).
- (33) = the Schur complement (30), the separation (29) (a refinement of (23)), (25), (28), the return-time
  coefficients (31), the self-energy exhaustion (32), then the resolvent identity.

A first quick reading (to be confirmed): the free-field constants are consistent. With SU(2), w = tr/2 and
Gaussian curvature of covariance P_ex/beta per colour, beta(1 - W) -> (3/2)<j, P_ex j> for a fixed loop;
(3/2)R(z) = 3[G_3(0) - G_3(z)] is beta times the Coulomb static energy g^2 C_F [G_3(0) - G_3(z)] with
g^2 = 4/beta, C_F = 3/4; R(e_1) = 1/3 because the three directional integrands sum to one; one plaquette
has <p, P_ex p> = 1/2 (rank 3 of 6 orientations), so c_1 = 3/4 and c_1 - c = 1/4 at a nearest neighbour.
