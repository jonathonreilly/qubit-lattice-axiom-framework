# Review of the C6 consolidated note (fresh-context, same model family)

Provenance: fresh-context reviewer, same model family as worker, checker and note writer (Claude Opus 5.5). Not independent of that family. Reviewer code is new and imports nothing from the runner or the campaign scripts.

Verdict: **needs changes**. One substantive error: the note writer's §5.2 "correction" (and its echo under Independent check, New here, and the runner docstring/check wording) is false as stated. Theorems 1–2, Corollaries 3, 4 and 6, and the exact A2 sector statement hold. The other edits are minor precision fixes.

## Runs
- Default runner: `TOTAL: PASS=35 FAIL=0` (24 s). `runner_default.log`.
- `--energetics --full`: `TOTAL: PASS=45 FAIL=0` (574 s under contention). `runner_full.log`.

## Reviewer code (all PASS / as stated)
- `rev_A2.py` (L = 3: 6 conventions; L = 4: 3 conventions). Own corner graph, faces, BKSF, Pauli phases. Uses a direct stabilizer-group test for −I, not the relation basis. In every convention: prod_{C in r} kappa_C = sigma_r on all basis relations; a sector of flux F exists iff F is consistent (0000, 1011, 1111, 1010, 0100, random gauge: yes; 1000, 0010, one flipped face, random F: no, at L = 3). All-bare-+1 is inconsistent in all of these generic conventions.
- `rev_A2_search.py`: a local search over vertex orderings finds orderings in which the all-bare-+1 assignment IS consistent (no −I). Found on L = 3 in 1.6 s and on L = 4 in 5 s.
- `rev_A2_TIsearch.py`: the same holds with translation-invariant orderings, on L = 3 and L = 4.
- `rev_A2_found.py`: checks the found L = 3 ordering from scratch. The BKSF algebra holds on all incident pairs, all 783 bare strings commute, there is no −I, and kappa = sigma. Sign flips then make uniform 1011, 1111 and 0000 each the bare sector.
- `rev_D.py`: 22528 sublattices of index ≤ 32. The O-invariant ones have indices {1, 2, 4, 8, 16, 27, 32}. The commutant of O is 1-dimensional. The 2·D3 basis matrix M (det 16) does not commute with O, and M^-1 R M is integral but ≠ R.

## Findings
See the final hand-back reply for the exact old→new edits.
