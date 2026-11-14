lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-11T01:24Z

# geo-apply (FINISH row 644): apply the READY edits of `library/geo-repairs.md`

Provenance: Claude Opus 5.5, medium effort, Mac mini worker 2, branch `claude/ym4d-hard-route` at f97619bdd, 2026-11-10. This is text application only, with no new proof. The repairs are from `library/geo-repairs.md` (row 631, Claude Opus 5.5). They come from `library/h-geo-check.md` (row 615) and `library/rim-scale-check.md` (row 613). The repaired files are Claude Fable 5.2's (rows 614, 609). Y lines are lines of Sussman and Alpoge's `YM4_1400.tex` (their text names Claude and Codex as authors), as cited in row 631. I did not re-read Y for this row.

Method. `library/h-geo.md` and `library/rim-scale.md` are unchanged between 5529d4f26 and f97619bdd (`git diff` empty). I found each place by its exact old text and checked that the text occurs exactly once before the replacement. Each edit was then made verbatim with the new text of row 631. A scratch script did the replacement (`/tmp/geoapply-scripts/apply.py`); it is string substitution, not a proof by computer. The diff is 27 insertions and 22 deletions over the two files. I changed no other text.

Repo search: this is not an open lemma, so there is no attack. Registry line 1002 (H-GEO) names this row as the apply step. No other row applies these edits.

## Log, `library/h-geo.md`

| Edit | Place (section, at 5529d4f26 line) | Status |
|---|---|---|
| A1-a | section 0, line 13 (`M >= L^4 M_1' >= ...`) | APPLIED |
| A1-b | section 0 table, row "seam to tower", line 23 | APPLIED |
| A1-c | section 1, new paragraph after item 2, line 41 (Notation: `M_1` vs `M_1'`) | APPLIED. Written as an indented continuation of item 2 (new line 42), so that the numbered list stays intact |
| A1-d | Fact 1.1, line 49 | APPLIED |
| A1-e | Fact 1.2, line 51 | APPLIED |
| A1-f | section 3, second rule, line 99 | APPLIED |
| A1-g | section 3, `mu`-tower, line 100 | APPLIED |
| A1-h | Lemma 3.1 statement, line 102 (`mu = M_1'`; consumer tower is first or second rule, Y 132180-132210) | APPLIED |
| A1-i (3 replacements, 4 places) | proof of Lemma 3.1, line 104 | APPLIED |
| A1-j | note on Y 12993-12996, line 106 | APPLIED |
| A1-k | Theorem, line 116 (`mu = M_1'`) | APPLIED |
| A1-l | order of constants, section 5 | APPLIED |
| A1-m | RESULT line, line 160 | APPLIED |
| A1 at lines 43, 45, 153 (quotes of Y in Y's letter) | section 1 items 4 and 6; section 6 item 2 | NOT APPLIED: row 631 status NOT APPLIED (which `M_1` Y means there is unsettled) |
| A1 at line 154 | section 6 item 3 | NOT APPLIED: row 631 leaves it (it holds in both readings) |
| A2-a | Theorem lead-in, line 116 (adds Y 28271) | APPLIED |
| A2-b | Theorem, new clause (H0) before (H1) | APPLIED |
| A2-c | Theorem, new clause (H5) after (H4) | APPLIED |
| A2-d | proof of Theorem, line 125, proofs of (H0) and (H5) before `square` | APPLIED |
| A3-a | Lemma 2 (d), line 87 (`O_h := Omega_h^c cap X`; Y 61983-61986, Y 62103-62125) | APPLIED |
| A3-b | section 2 setting, line 55 (box form at `i = h`) | NOT APPLIED: row 631 status NOT APPLIED (not named by the repair; suggestion only) |

## Log, `library/rim-scale.md`

| Edit | Place (section, at 5529d4f26 line) | Status |
|---|---|---|
| R-a-1 | section 3, definition of `lambda(p)`, line 56 | APPLIED |
| R-b-1 | 6.2 input (I2), line 141 (`K_w`) | APPLIED |
| R-b-2 | section 8 item 3, line 219 | APPLIED |
| R-c-1 | proof of Theorem 6.2, line 156 (cites Y 63760-63765 for the outer two layers) | APPLIED |
| R-d-1 | Corollary 6.3, last sentence of statement, line 166 | APPLIED |
| R-d-2 | proof of Corollary 6.3, line 168, location of `P` before `square` | APPLIED |
| R-e-1 | 7.2 class-M paragraph, line 209 (`r = 6 frakM xi_n`; `a_flat >= 7 C frakM rho`) | APPLIED |
| R-e-2 | section 8 item 5, line 221 (adds `36 frakM^2 rho <= eps_*`) | APPLIED |
| R-f-1 | head of 7.2, line 199 (hypothesis `R_1 >= 42 L`; floor `R_1 >= L` of Y 650 does not give it) | APPLIED. No proof changed |

## Fit after the edits

I read the changed statements against their proofs once. Row 631 recorded the same reading. I found nothing new:

- h-geo: every statement that uses `M_1 >= R_1 frakM` now uses `M_1'`. The remaining unprimed `M_1` (lines 13 in a parenthesis, 42, 44, 46, 101, 107, 156, 157 of the new file) are quotes or reports of Y's letter, as A1 intends.
- Two points stay open, as row 631 records. First, R-d-2's profile case uses (I2), which needs `R(U_X) <= a_c`; the file does not state this, but the location claim does not depend on it. Second, the hypothesis `R_1 >= 42 L` of 7.2 is stated, but the 7.2 proof does not yet use it (fit (i) is still "Not checked"). Section 8 item 1 does not list the new floor.
- The status lines of both files (h-geo section 6 item 5 "Not checked by another model"; rim-scale section 6.4) are unchanged, because no repair names them.

No numeric job was run, and none was needed.

RESULT: All 29 READY edits of `library/geo-repairs.md` are APPLIED: 20 to `library/h-geo.md` (A1-a to A1-m, A2-a to A2-d, A3-a) and 9 to `library/rim-scale.md` (R-a to R-f). Each old text was found exactly once. Row 631's NOT APPLIED items stay NOT APPLIED: A1 at Y-quotes (lines 43, 45, 153), line 154, and A3-b. Open: `R(U_X) <= a_c` in R-d-2's profile step; the 7.2 proof does not yet use `R_1 >= 42 L` (fit (i)); the meaning of Y's `M_1` at Y 13450, 16102, 62436, 63183; and no cross-model check of the repaired files.
