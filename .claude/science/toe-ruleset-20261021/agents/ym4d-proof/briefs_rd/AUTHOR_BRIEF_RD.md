# Author brief RD: control the actual returned denominator of one RG step

Lead: Claude Opus 5.5, 2026-10-29. One Codex author context runs on the MacBook, and a fresh reviewer follows.
Process: PROCESS_LIGHT.md. Edit only your own files, pre-register numerics, review independently, and rebuild rather than cite.

## Why
HANDOFF "Remaining proof path", step 2, is to produce one usable renormalization step:
- "Repair CX with actual spatial dependence of its fluctuation map/source and control the complete returned denominator."
- "A single-link normaliser's zero-free domain is insufficient."
- "Include holes, reference comparison and failed-return bookkeeping."

CODEX_REVIEW_STEP R11 (around l.194) and item 6 (around l.318) record the state of this:
- the conditional exponential identity is CONFIRMED;
- the full Den_Y logarithmic bound is REFUTED;
- the actual returned denominator is NOT-VERIFIED;
- what is needed is "an independently established analytic exponential representation of the **actual** returned denominator, with nonzero prefactors".

SOFTHARD C2 (around l.165-175) classes this as a soft-specific cost. LIB1.md (R10, landed) proves the nested-hole bookkeeping, and around l.188 it notes that this "is not a bound for a returned denominator with complex sources".

## Do not duplicate active coordinator lanes
HANDOFF "Current assignments" lists three active authors:
- fixed source radius;
- finite-coupling kernel remainder;
- original-law coercivity and tails.

Do not work on those. Where you need one of their outputs, state it as a named input with its exact expected form.

## Target: Theorem RD
State the actual returned denominator, Den_Y or its correct replacement, for one RG step of the soft-kernel chain (decision 4) with complex sources, exactly as STEP55 and CX consume it. Then prove an analytic exponential representation:

Den_Y = 𝒩_Y^{ref} · exp(Σ_X K(X)),

with:
- nonzero, explicitly bounded prefactors;
- polymer activities K(X) analytic in the sources on a stated domain;
- ‖K‖ bounded uniformly in the history, holes, scale and volume.

Include:
- the reference comparison;
- the holes, using LIB1's R10 nested-hole resummation, which you may consume as landed;
- failed-return bookkeeping.

Zero-freeness and the logarithmic bound that CX needs follow from the representation.

Prefer a route through the existing confirmed cluster theorem CX-R (RECOVERY_CLUSTER_ASTRA.md, with its review). Its review says FULL/VAR "still require the exact actual denominator identity and its prefactors". Supplying that identity is exactly this lane.

## Write
- **RD.md**, containing:
  - Theorem RD with its proof, each step marked PROVEN, ARGUED or OPEN;
  - an "Inputs consumed" table (landed results, plus the named inputs taken from the active coordinator lanes);
  - a "Consumers" table: CX, STEP55, HANDOFF step 2, CODEX_REVIEW_STEP R11/item 6;
  - the open residue.
- **RD_LOG.md.**
- **checks/rd_\***, only if you run a numeric check. In that case:
  - write checks/rd_criteria.md first;
  - use nice and BLAS=1;
  - keep each run under 1 GB;
  - require load < 8 and at least 30% memory free;
  - take the lock: `until mkdir /Users/jonreilly/Projects/Physics/.claude/worktrees/ym4d-rd/.locks_numeric 2>/dev/null; do sleep 20; done`, then `rmdir` exactly once.

  The sandbox may block `nice`. If it does, report that and do not weaken the check.

## Rules
- Edit nothing else.
- No commits.
- No audit or ledger files.
- No axiom edits.
- Final message under 300 words.
