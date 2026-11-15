lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T10:14Z

# Check of row 1021 (`gap-registry-after-checks-max`), work item W1

Row 1023, queued 2026-11-15 22:13Z. Checker: Claude Opus 5.5 max, Mac mini worker 2.
Source under check: `library/gap-registry-after-checks-max.md` at commit f6c0017dc
(written by Claude Fable 5.2 max; same provider as this checker, so this is not an
independent cross-provider check). Started 2026-11-15 22:14Z (from `date -u`).

No subagents. No commit, no push. Numeric runs only to refute or guide, under the
numeric lock, and none is planned.

## Plan (at most eight steps; revised after reading W1)

1. Read W1 (source 7.7, L797-808) and the FINISH rules. Done; W1 copied below.
2. Read source Section 6 (L508-735) in full; run tests (a)-(e) first, as W1 orders.
3. Lemma EL and Corollary NS, redone by hand (most care; test (c)).
4. Lemma KL (i)-(iii) and (K1)-(K3), redone by hand (most care; tests (a), (b), (e)).
5. Lemma S1 and Proposition FR, redone by hand (test (d)).
6. Section 6.5: Lemma LIFT and Lemma NB.
7. W1 (i): Section 4 rows A1, A2, B5, B6, B7, B8, B10, B13, C1, C8 against the cited
   check files at the cited lines. W1 (iv): 6.4 items 1-4, the verdict on T3, and the
   ARGUED reading on (ABS-flow) in 5.2.
8. Verdict table and RESULT line.

Stop rule (W1): stop at the first WRONG in Lemma KL or Lemma EL and report it; no new attack.

## W1 as written (source L797-808, copied verbatim)

> W1, check (a model that did not write this file; another provider if possible; high effort). Read
> `library/gap-registry-after-checks-max.md` at the commit that holds it. (i) Section 4: for the rows A1, A2,
> B5, B6, B7, B8, B10, B13, C1, C8 open the cited check file at the cited lines and say whether the status
> word is the check's own verdict. (ii) Section 6.3: redo by hand Lemma S1, Proposition FR, Lemma EL, Lemma
> KL (i)-(iii) and (K1)-(K3). (iii) Section 6.5: Lemma LIFT, Lemma NB. Test first: (a) sigma^2 = 1/(2 beta sinh
> omega) against `gap-fc-max.md` L193-197 and L510; (b) in KL (ii), (1 - e^(-omega))/sinh omega = 2/(e^omega + 1);
> (c) in Lemma EL, that the law of the whole path is invariant under time-independent gauge transformations,
> and that side 3 is enough; (d) whether (E1) is used for gauge-invariant f only; (e) whether (K3) is a fair
> reading of (P1) (CA-II 80163-80172 as quoted in `gap-hcphys-max.md` L46). (iv) Judge 6.4 items 1-4 and the
> verdict on T3; judge the ARGUED reading on (ABS-flow) in 5.2. Verdict per statement: ADVANCE,
> CORRECT-NO-ADVANCE or WRONG with the failing line. Stop rule: stop at the first WRONG in Lemma KL or Lemma
> EL and report it; no new attack. Output `library/gap-registry-after-checks-check-<model>.md`.

Report format (FINISH, Rules): one provenance line, then a verdict per statement (ADVANCE,
CORRECT-NO-ADVANCE, WRONG), then only the defects that break something, each with its explicit failure.

## Progress

- Step 1 done (2026-11-15, after 22:14Z). Next: Step 2, read source Section 6 and run tests (a)-(e).
