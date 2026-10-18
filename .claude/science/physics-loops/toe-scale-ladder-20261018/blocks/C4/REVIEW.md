# C4 independent review

Reviewer: Claude (Opus 5.5, model id claude-opus-5-5), spawned as an independent-review subagent.
Provenance: same model family as the author; independence is of *code and route*, not of model.

## Phase A — blind counts (recorded 2026-10-18 21:43:33 UTC, before opening any author log/results table)

Read before this point: NOTE.md lines 56-117 (setup + method), parent stabilizer note on main and
its runner's action definitions (Q(R) for trivial / sign diag(1,s,s) / axis s|R| / full R), the
soldering-menu note. The author's headline counts were also visible in the review task prompt, so
this phase is "blind to logs/code", not blind to the target numbers.

Reviewer code (from scratch, no import or copy of c4lib.py / author scripts):
- review_scripts/rv_common.py — O, the five actions (sign-f = half turn about (0,1,1) on odd R),
  homomorphism check, phased single-site Pauli multiplication, beta_R on signed strings.
- review_scripts/rv_linear.py — covariant F2 space with own bitset Gaussian elimination
  (checked: dim = 2 x 2 x #O-orbits for trivial: 16 on the 27-cell, 40 on the 125-ball).
- review_scripts/rv_classify.py — exhaustive enumeration of W with all symplectic conditions as F2
  quadratic forms (hi/lo split), each survivor re-checked by explicit Pauli-string commutation
  with every overlapping translate, signs fixed by explicit phased multiplication for all 24 R.
- review_scripts/rv_bruteforce.py — completeness cross-check: plain loop over all 2^dim W, explicit
  commutation only.

| action | dim W (27-cell) | unsigned | signed |
|---|---|---|---|
| trivial | 16 | 132 | 528 |
| sign | 16 | 132 | 176 |
| sign-f | 10 | 16 | 32 |
| axis | 7 | 1 (identity) | 1 |
| full | 7 | 1 (identity) | 1 |

Range 2 (125-ball), dim W = 25 for both axis and full: **4 unsigned, 4 signed** each (each
unsigned solution admits exactly the sign choice (+,+)); the identity plus three non-trivial QCAs,
same F2 matrices for axis and full.

Logs: review_scripts/rv_r1.log (TOTAL: PASS=5 FAIL=0), review_scripts/rv_bruteforce.log
(TOTAL: PASS=4 FAIL=0), review_scripts/rv_r2.log (TOTAL: PASS=2 FAIL=0).
