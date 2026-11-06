lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T04:55Z

# FC: the current identification and the complex frame change for library/stage-claude.md

Row 392 (`fc`). Pinned at commit 7796b75f1. Work in progress; sections are written as they are finished.
Proved by Claude (Mini worker), not yet checked by the other model.

Moves: the two BLOCKs of `gates/stage-gate.md` on `library/stage-claude.md` Theorem S (FINISH row 388), that is, AD-ST(2) (registry row `AD-ST(2)`, owner `stage-claude`), inside H-STAGE, the first input of A10 on the T0 chain.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, checkout at 7796b75f1 (branch `claude/ym4d-hard-route`). Research text, not an audit; grants no status. Written arguments only. Sources: CA-I, CA-II (`theorem_0_complete_account_raw_{I,II}.tex`) and SA (`YM4_sketch_500.tex`) at `31a47c543775`, fetched into a scratch folder; Balaban CMP 109 pp. 272-273 read from the PDF page images in `~/ym4d-papers/`.

Credit: Tadeusz Balaban for the substitution CMP 109 (3.10)-(3.18) and the operators of CMP 99b, 102b. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account at `31a47c543775`: the response chart (CA-I 4.5), its diagonal exactness, nested criticality (CA-I 4.26), and 5.2:cor-response-dilation. Codex for `gates/stage-gate.md` and `library/prior/fc.md`.

## 0. Duplicate check (rule 0a)

Searched `library/open-core.md`, `library/l17c.md`, `library/open-registry.md` and the FINISH rows for: shift-map, stage-response-identification, AD-ST, PAIR, frame change, FC, nested criticality, second slot, partner current.

* **Match, named.** Registry row `stage-response-identification` ("Their identification and uniform bounds on the complete stage family remain unproved", `library/shift-map.md:1661`, owner `shift-map`, FINISH row 261, lane finished, open). The gate (`gates/stage-gate.md` §6, last paragraph) places the *partner-current match* inside this bridge. `library/shift-map.md` §18 Attack C (lines 1632-1640) already found that equality on the physical current graph does not fix the extension in the independent current. So this note does **not** attack the identity "actual current = chart current 𝔍(b) at independent J" as a proof target, and does not attack the layer match (M-chart).
* **Not covered elsewhere.** Row 392's second branch, the weakest replacement that every consumer of AD-ST(2) accepts, is not in shift-map's statement (shift-map's open lemma is Lemma R, the returned-pair velocity (67)). Section 1 takes that branch: it bounds the actual current increment directly, given the layer match that (M-chart) already assumes.
* The frame change (item 2) is listed only as the open lemma FC of `library/stage-claude.md:275` (owner `stage-claude`, this row's lineage). The open-core seven (CM, CR, CA, CW, CH, CO, CV) do not contain it. FC-test, FC-mean-match and FC6 (FCON, ST1) are different statements that share the letters.
