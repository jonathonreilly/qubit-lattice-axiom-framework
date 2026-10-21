# C6 WORKLOG (2026-10-18)

- Read SCIENCE_WORKFLOW.md section 2, no-go-discipline SKILL.md, the SCALE_LADDER_MAP C6 entry, and the five 2026-10-17 code notes (edge BKSF, six-direction, MPD, spinful MPD, corner) plus their runners.
- Wrote c6_lib.py: int-bitset Pauli/GF(2) tools and builders F1-F5. The corner builder is transcribed from the repo runner.
- Exploration: k(L) for L = 2..4. Found MPD/spinful k = 2 at odd L, and π-flux sectors frustrated at odd L. Bug in the first logical scan (the basis was polluted with logical candidates) gave a spurious "strings in S"; fixed it and re-ran.
- Derived Lemma 1 (homological TQO) by hand before the box certificates. The odd-L k = 2 parity explanation is post hoc.
- Runner c6_tqo_runner.py, full mode: 79 s, PASS=18 FAIL=0. The homology check (a different path for (T1)/(T2)) gave PASS=3 FAIL=0. Combined log: PASS=21 FAIL=0.
- No network, so the BHM constants and theorem wording are cited from memory (flagged in the NOTE).
- Not done: a general-L proof of frustration-freeness; corner-code distance bound; an explicit J0; independent re-implementation.
- Single core; no git operations.
- Review pass (REVIEW.md): applied every finding to NOTE.md and appended "Review dispositions". Added c6_ff_general_L.py, which proves frustration-freeness for F1–F4 at every L (FF iff L even or f = 0) using the reviewer's relation basis, an eventual-periodicity argument and a full-period exact check (6/6). Added lazy builders to c6_lib.py. Re-ran all runners; the combined total is in logs/C6_SUMMARY.log.
