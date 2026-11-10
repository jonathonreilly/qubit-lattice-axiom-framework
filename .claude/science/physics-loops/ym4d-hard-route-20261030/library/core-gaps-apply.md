lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-11T01:04Z

# core-gaps-apply: the seven repairs of `library/core-gaps-check.md` applied to `library/core-gaps.md` (FINISH row 641)

Provenance: Claude Opus 5.5, effort medium, Mac mini worker 2, branch claude/ym4d-hard-route at 80a859fae. Not an audit. The repair texts R1-R7 are by Claude Fable 5.2 (`library/core-gaps-check.md`, row 640); the proof is by Claude Opus 5.5 high (`library/core-gaps.md`, row 621), ported from Codex's `library/geo-5.md` 3.2-3.3. The rules and line numbers are Sussman and Alpoge's (with Claude and Codex as authors of their text), `YM4_1400.tex` at `2bc0658f91d2` ("Y n" = line n).

Repo search: this row applies repairs; it attacks no open lemma. `library/open-core.md` has no row for CORE-GAPS or `prop:large-field-2-3`. Row 641 names `library/core-gaps.md` and this log as its outputs.

## Log (one line per edit)

Line numbers are those of `library/core-gaps.md` after the edits. Before applying, I re-read each Y line that a repair cites (Y 645-648, 1102-1103, 61911, 61973, 62001, 62169-62171, 62195, 63684-63690, 63714-63720, 63750-63763, 63882, 83084) in a fresh copy fetched by URL. Each says what the repair text says.

- R1, section 4, proof of Theorem 6, operation case, before "So $\mathcal L^{\boldsymbol\nu}(h)$ satisfies (N), (G)" (line 121): APPLIED, word for word.
- R2, section 2.2, after "a union of level-$t$ cells" (line 47): APPLIED, word for word.
- R3, section 3, Lemma 4, first line of the (G) proof (line 96): APPLIED. The old words "a level-$l$ unit cube $c\subset Z_l$ and a cube $f\subset\Omega_{l+1}$ of the grid of $\Omega_{l+1}$" are replaced by the repair text. "Fix $0\le l<t$," and "We show $d(c,f)\ge u_{l+1}$." are kept around it.
- R4, section 2.3, reading (R2) (line 56): APPLIED, word for word, appended after the existing bracket.
- R5, section 2.3, reading (R3) (line 57): APPLIED. The bullet now opens with the repair sentence "(R3) is not a reading: Y 62169-62171 states ...". The old content (that $\Lambda^{\boldsymbol\nu}_l$ follows the rule of $\Omega^{\boldsymbol\nu}_l$, and the Y 62121 quote) is kept in brackets, because Lemma 5 cites "(R3)" for that rule. No statement changed.
- R6, section 6, Corollary 7, display (line 146): APPLIED. "(level-$m$ units)" is replaced by "with $\xi_q=L^q$, in bare units".
- R7a, section 2.1, last paragraph (line 43): APPLIED, word for word: "$\mathsf N_t=\check R_t$" now cites Y 62195, Y 63882; Y 62001 stays for "all partitions are nested".
- R7b, section 5, table row "step padding and cell side" (line 138): APPLIED. The added sentence on $\check R_t\ge1$ is the repair text. One citation is added to it: "$\gamma<e^{-1/2}$ at Y 1102-1103". The step $\gamma^{-2}\ge e$ needs this bound, and the repair text names no line for it. The same row also cited Y 62001 for "$\mathsf N_t=\check R_t$". R7 replaces that citation in section 2.1 and the section 5 table, so it is now Y 62195, Y 63882.
- Provenance, line 8: one line added. It says R1-R7 were applied by this row and names this log. No statement changed.

NOT APPLIED: none of R1-R7.

Not changed, though near the repairs. These are not named by a repair text and are left as they were:
- Section 2.3 heading "Three readings" and section 7 item 3 "Readings (R1)-(R3)". After R5, (R3) is Y's explicit rule, so only two are readings. The lead may change the wording.
- Section 0 line "Three readings ... are stated as such in section 2.3". Same point.
- Section 7 item 1 ("Not checked by another model") and the RESULT line. Row 640's same-provider check is not recorded there. That is a status edit for the lead, not a repair.

## What this does not show

- No new proof step. The edits follow the repair texts of row 640. This log is not a new check of `core-gaps.md`.
- Still open: the cross-provider check (FINISH rule 2, gpt-6-astra when Codex has capacity). The [Y] inputs (quiet boxes, prepared boxes with $k_0$, marks wait) are used as Y states them and are not rebuilt. Reading (R2) of section 2.3 matters for the pair $(0,1)$ only. R4 shows that only the frozen-$\Omega_0$ reading breaks that pair.
- No computation was run. memory_pressure was not needed.

RESULT: all seven repairs R1-R7 of `library/core-gaps-check.md` APPLIED to `library/core-gaps.md` (R1 joint induction order, R2 sup-norm layers, R3 one grid of $M$-cubes, R4 second reading for the pair (0,1), R5 (R3) is Y 62169-62171, R6 bare units in Corollary 7, R7 line Y 62195/63882 for $\mathsf N_t=\check R_t$ and $\check R_t\ge1$ derived, with Y 1102-1103 added for $\gamma<e^{-1/2}$). No statement or proof step changed beyond what the repair texts name. Every cited Y line was re-read and matches. Open: cross-provider check of `core-gaps.md`; the [Y] inputs; reading (R2) for the pair (0,1); the words "three readings" in sections 0, 2.3 and 7 are left for the lead.
