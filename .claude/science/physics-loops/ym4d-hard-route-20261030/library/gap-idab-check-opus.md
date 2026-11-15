lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T17:04Z

# Check of row 993 (`library/gap-idab-opus.md`): line-by-line, against Balaban's page images and the Sussman-Alpoge lines it quotes

Provenance: Claude Opus 5.5, max effort, Mac mini worker 3, branch `claude/ym4d-hard-route` at commit d5eace7be. Queue row 994. Not an audit. The checked note was written by Claude Opus 5.5 high, so this check is same provider and is not independent; a gpt-6-astra check is held for the Codex reset. No commit, no push; the relay copies this file.

Credit: the objects checked come from Balaban (CMP 99, 102, 109, 119) and from Ethan Sussman and Levent Alpoge's complete account (CA-I, CA-II, CA-III at 31a47c543775; text by Claude and Codex). The rebuild under check is by Claude Opus 5.5 high (row 993).

Status: started 2026-11-15T05:04Z.

## Plan (at most eight steps; one step per response, appended before the next)

1. Read the checked note in full. Repo search. List every item the row names, with the note's line and the sources it quotes. Find SA L14091-14107.
2. Lemma C (constants of CMP 119 (3.15) and (3.33): torus-free numbers per bond, site or coordinate), from the page images.
3. Lemma ZB (a)-(d), including z^(k)(c) = L^9 at U = 1 (CMP 109 p. 268, CMP 119 p. 267), from the page images.
4. The E_0^(j) readings and the counterexample (CMP 119 (2.27), wrapping domains).
5. Step 4: the block map identity (CMP 109 (0.3), G(y,x), (0.10)-(0.12) against SA (QC1)-(QC3)) and Lemma LR.
6. Lemmas V, R, GS, PS, QD and MIN (CMP 109 (2.4)-(2.11), CMP 102 (174)).
7. (b2), (b3), the (ID-b) assembly, and whether (r4) can be settled from SA L14091-14107.
8. Verdict table (HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line) and the RESULT line.

## Working log

### Step 1. Inputs, items, sources (05:20Z)

**Repo search.** `grep` for `gap-idab`, `ID-a'`, `(ID-b)` over `library/`, `gates/`, `checks/`: hits only in `gap-iloc-opus.md` (row 990, which poses the items), `gap-det-check-opus.md` (row 989), `gap-idab-opus.md` (the note under check) and this file. `library/open-core.md` and `library/l17c.md`: no hit. No other check of row 993 exists. This is a check item, so no lemma is attacked.

**Note under check.** `library/gap-idab-opus.md` at d5eace7be, 279 lines, read in full. Its header says it was pinned at 0ee089f92; its step times (05:10Z-08:00Z) are wrong per the lead note in row 993 (run 04:44Z-04:59Z). Not relevant to the mathematics.

**Sources fetched (scratch, not committed).** SA outline `YM4_sketch_500.tex` and CA-I `theorem_0_complete_account_raw_I.tex` at 31a47c543775 from github.com/ethanwsussman/Yang--Mills-LLM-experiment into `/tmp/idab-check-994/sa/`. Outline SHA-256 d7f77d4da3eb...4b6f, the hash the note gives (d7f77d4d...). So the note's outline line numbers refer to this file. Balaban's PDFs in `~/ym4d-papers/` (CMP 99 389, 102 277, 109 249, 119 243), rendered page by page to PNG with PyMuPDF in `/tmp/idab-check-994/png/` and read as images. PDF page = journal page - first page + 1 (checked against the note's own pairs: CMP 119 p. 267 = PDF 25, p. 273 = PDF 31).

**Items the row names, with the note's lines.**

| # | Item | Note lines | Sources it quotes |
|---|---|---|---|
| 1 | Lemma C | L91-108 | CMP 119 (3.15) p. 267, (3.33) p. 273; CMP 109 (0.15) p. 255, (2.10) p. 267 |
| 2 | Lemma ZB (a)-(d), value L^9 at U = 1 | L89, L112-120 | CMP 109 (2.4) p. 266, h p. 267, p. 268; CMP 119 p. 267, p. 273; row 990 (QC15)-(QC16) |
| 3 | E_0 readings (i), (ii) and the counterexample | L122-125 | CMP 119 (2.25)-(2.27) p. 259, p. 273; CA-I L104010-104013, L106125-106150 |
| 4 | Step 4: block map identity, Lemma LR | L127-145 | CMP 109 (0.3) p. 252, (0.4)-(0.12) pp. 253-254; SA L7946-7958; CA-I L800-840 |
| 5 | Lemmas V, R, GS, PS | L156-171 | elementary; pr-lay (6)-(7) |
| 6 | Lemma QD | L168, L237-244 | SA L9634, L10139, L10212 |
| 7 | Lemma MIN (and B1) | L186-197, L227-231 | CMP 109 (0.21), (1.5), (2.6)-(2.8); CMP 102 (74)-(102), (174)-(177); CMP 99 p. 394 |
| 8 | (b2), (b3), (ID-b) assembly, (r4) | L199-219, L235 | CMP 109 (0.19), (1.5), (1.8), (2.5), (2.11), p. 268; SA L6854, L7180-7188, L10200-10208, L14091-14107 |

**SA L14091-14118, read now (for item 8, (r4)).** L14091-14107 define, at a regular complex pair P = (U, J), Delta_k(P) = (Q G_1 Q^T)^{-1} - a - E^(2)[H_1^T J] and A(P) = C_V^T (GF^(2)_V + Delta_k(P)) C_V, with "C_V eliminates the pivot bonds", "The many-scale rows Q come from the straightened average", "E^(2) comes from the plain one-step constraint on V". The next paragraph, L14109-14118, says: "At a background pair P_W = (U_+, J(U_+)), the form in (eq:actual-regular-precision) is the Hessian on the fibre of A o U_k + GF_k. ... Thus the Gaussian of the step is C^(k) = A(P_W)^{-1}. Soft gauge fixing supplies the positive quadratic form on the orbit directions". Whether this settles (r4) is decided in Step 7, after the normalizations of Balaban's (2.10)-(2.12) are read from the page images.

