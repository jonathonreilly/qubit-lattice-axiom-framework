# Structural index of the complete account (CA-I, CA-II, CA-III)

Source: Ethan Sussman and Levent Alpoge, `theorem_0_complete_account_raw_{I,II,III}.tex` at commit `31a47c543775`, text authored with Claude and Codex. Credit them for everything indexed here.

Made 2026-11-05 by the lead (Claude) with `ca_index.py` (in this folder): a text scan of every `\begin{theorem|lemma|proposition|corollary}` with its line, label, heading title, and the status the account itself declares. The account's convention is at CA-I L27-46: no indication = proved in full; a citation with locus = a published theorem quoted by statement; "printed without proof in" = a published sentence used as printed; "Stated; proof incomplete at the step marked (*)"; "Proof outstanding." with a Route paragraph; "Model" = proved only in a model. The scan reads the heading and the 25 lines after it, so a status can be misread (for example a "proof outstanding" phrase in the next statement). Check the source line before relying on any row. This index reads; it proves nothing.

Files:
- `index.tsv`: all 1,647 numbered statements (file, line, kind, label, status, title).
- `leaves.tsv`: the 166 statements whose status is not PROVED.

Counts (as scanned):

| File | Proved | Incomplete | Outstanding | Cited | Printed | Model |
|---|---|---|---|---|---|---|
| CA-I | 553 | 26 | 8 | 10 | 3 | 0 |
| CA-II | 478 | 15 | 11 | 7 | 0 | 48 |
| CA-III | 450 | 24 | 13 | 0 | 1 | 0 |
| Total | 1,481 | 65 | 32 | 17 | 4 | 48 |

Porting rule (owner, 2026-11-05: "if porting means not REDOING their work, then yeah - duh"): a PROVED statement is ported (cited, rebuilt in the repository, checked), never re-derived by another route. Proof work goes to the INCOMPLETE, OUTSTANDING, CITED and PRINTED leaves, and to MODEL statements the T0 chain uses outside their model. Those leaves are also the only places a contribution to Sussman and Alpoge can come from.
