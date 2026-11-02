# dc55_1 — locator audit for DICT55.md (criteria written before the script)

Written: 2026-10-29 (UTC time printed by `date -u` in the worker's shell immediately before this file: see DICT55.md §6).
Author: Opus 5.5 worker (claude-opus-5-5). Writes only checks/dc55_1_* .

## What is checked
DICT55.md cites every definition and alias by (file, locating string). The script reads a tab-separated list
`checks/dc55_1_locators.tsv` (columns: entry-id, file name relative to the lane directory, locating string) and, for each row,
tests whether the locating string occurs as an exact substring of at least one LINE of that file, decoding the file as UTF-8
(no normalisation, no case folding, no whitespace collapsing). Line-wise matching is used so that every locator is
findable with `grep -F`.

## Pre-registered verdicts
- **PASS** iff (i) every row of dc55_1_locators.tsv is found in its file, AND (ii) every control below behaves as stated.
- **FAIL** otherwise; every missing row is printed with its entry-id, and DICT55.md must then correct or withdraw that entry.

## Controls (must fire; if any control does not behave as stated the whole check is void, not PASS)
- C1 (mutation): for every row, the string with the suffix "§§DC55-NOT-THERE" appended must NOT be found in its file.
- C2 (wrong file): for every row, the same string must be searched in one fixed unrelated file, `checks/dc55_1_criteria.md`
  itself excluded; rows whose string also occurs in that unrelated file are listed (informational only; not a failure),
  so that a string too generic to locate anything is visible. The unrelated file is `HANDOFF.md`.
- C3 (missing file): a synthetic row naming a non-existent file must be reported as an error, not as found.

## Scope limits (stated in advance)
- A PASS shows only that the cited strings exist in the cited files at the time of the run. It does not show that the string
  denotes the object DICT55 says it does — that is the human/Codex reading the entry asks for.
- Files change concurrently in this lane; the run time is recorded in the output file.
