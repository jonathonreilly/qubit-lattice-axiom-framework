# Review History

## 2026-07-15 iteration 1

- Code/runner: risk. Potential-support coverage did not instantiate realized
  histories, and `assert` checks could be disabled by optimized Python.
- Physics claim: open pending typed map domains, corrected DAG/self-edge
  wording, and explicit quantifiers.
- Imports/governance: fix. Shared randomness was misclassified as a
  normalization; loop records treated an archived verdict as a live blocker;
  negative-scope guards were written too broadly.
- Audit compatibility: blocked because the live retained row requires
  independent re-audit after source-hash drift.

## 2026-07-15 iteration 2

- Code/runner: pass after adding direct exhaustive realized-difference checks
  for every Boolean local truth table through predecessor arity three and an
  optimization-safe `require` check.
- Physics claim: the narrow finite combinatorial theorem boundary passes local
  physics review.
- Imports/support: clean. No measured, fitted, observational, literature, unit,
  or physical-identification input is load-bearing.
- Repo governance: pass. The loop now describes upstream hardening of an
  already-audited theorem, and the negative entries are explicit non-claim
  scope guards.
- No-go discipline: not applicable; this block proves no negative theorem.
- Audit compatibility: blocked pending independent re-audit of the changed
  note and runner hashes. No audit verdict or generated audit data is authored
  by this block.

## Independent math check

An implementation separate from the runner enumerated all 512 directed graphs
on three vertices, all eight source subsets, and horizons zero through three.
All 16,384 graph/source/horizon cases obeyed exact-path support containment in
cumulative reachability, with equality when every self-edge permits path
padding. A separate reviewer exhaustively enumerated Boolean state pairs and
local truth tables and independently confirmed the realized one-step lemma.

## 2026-07-15 iteration 3

- Review scope: `STATE.yaml`, `REVIEW_HISTORY.md`, `HANDOFF.md`, and
  `PR_BACKLOG.md`.
- Governance finding: the initial checkpoint text pre-recorded its own result,
  used grade language reserved to the audit lane, and described review-loop as
  a ratifier.
- Applied fix: record the actual four-file scope, describe the local theorem
  boundary without an authored grade, and reserve ratification to the
  independent audit lane.
- Re-review requested for these record-only fixes; the independent re-audit
  provenance gate remains blocked by design.
