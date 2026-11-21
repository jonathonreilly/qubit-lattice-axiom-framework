# lane982 (FINISH row 982, gap-hcphys-max): sources and runs

No numeric run was made in this lane. There is no script and no data file. The numeric lock was not taken.

## Source read for the port question

Ethan Sussman and Levent Alpoge, complete account of Theorem 0 (text authored with Claude and Codex), commit `31a47c543775`:

- `https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex` (166,711 lines)
- `https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex` (145,624 lines)

Fetched 2026-11-14 by URL into a scratch folder outside the repository. Not committed. CA-III was not fetched.

## Lines read (CA-II)

| Lines | Statement |
|---|---|
| 75150-75215 | Lemma 8.2:lem-fluctuation-positivity (lower bound of the fluctuation form as antecedent) |
| 80014-80050 | Definition 8.3:def-window-product (window as a product of norm balls; rescaled normalisation) |
| 80152-80200 | Definition 8.3:def-box-precision (a_- <= Q <= a_+, entry decay, taken from the operator theorem at free current) |
| 81161-81215 | Proposition 8.3:prop-lipschitz-stability (the coercive windowed class) |
| 83869-83905 | Lemma 8.3:lem-correlation-decay (Helffer-Sjostrand representation assumed) |
| 84178-84210 | Remark: no spectral gap and no variance inequality used; the window is kept |

## Greps (counts or first hits only)

- CA-I: `Sobolev|Bakry|hypercontract`, case-insensitive: 0 lines.
- CA-II: `log-concav|uniformly convex|strongly convex|Brascamp|Bakry|Sobolev|hypercontract|Poincar`: lines 84184, 84205, 133310, 135674 (none is a log-Sobolev or hypercontractive statement).
- CA-I and CA-II: `unequal sides|equal side|aspect ratio|rectangular tor|anisotropic tor|all four sides|four sides|side lengths`: no statement on tori with unequal sides found. A search that finds nothing does not prove absence.
- Index used to find the statements: `library/sa-index/ca-full/index.tsv`.
