lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T13:03Z

# Check of row 1028 (`library/gap-uv-rigidity-max.md`), FINISH row 1030

Checker: Claude Opus 5.5, max effort, Mac mini worker 3. Author of the checked
file: Claude Fable 5.2 (same provider, so this is not an independent-provider
check). Pinned at commit 85d8dfc6d. No subagents. Started 2026-11-16 01:03Z.

Verdicts used: HOLDS, HOLDS AFTER CORRECTION, FAILS (with the first failing
line). No new attack (row 1030).

## Plan (at most eight steps; one per response, each appended before the next)

1. Read FINISH.md rules (efficiency, build on published work), the checked file
   `library/gap-uv-rigidity-max.md` in full, and the definitions it relies on
   (engine axioms, Proposition OM, Omega, D, (W), (LIOU), (BDD-Delta)) in
   `library/gap-compact-rigidity-max.md` and its checks. Record anchors.
2. Test first: Lemma FV, the count of zero modes on the smallest torus, then the
   whole proof of D(n; beta) >= (3/2) log beta - 59 n^4 - 11 (SU(2), beta >= 16).
3. Test first: Proposition CONST against the engine's axioms as stated in
   `library/gap-compact-rigidity-max.md` (constant c critical iff c = log m,
   m >= 2 an integer), with Proposition FRZ.
4. Test first: the family TS against every kept property.
5. Lemma REC and REC+ (exact definition of uniformly recurrent in Proposition OM).
6. Lemma ALPHA, Corollary KEPT, Proposition A1, Proposition TWO, Lemma EXCL,
   Corollary CR-1, Proposition MON+.
7. The GUIDE-grade correction: U(1) with growing beta and five dimensions in
   branch (II); the remaining controls; work item W1 if the file names one.
8. Verdict table and RESULT line.

## Step log

(Each step's result is appended below as it completes.)
