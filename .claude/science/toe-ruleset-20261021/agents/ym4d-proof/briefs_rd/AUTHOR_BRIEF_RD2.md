# Author brief: RD pass 2, the exact identity for the actual returned denominator

You are a fresh Codex author context on the MacBook. Follow PROCESS_LIGHT.md: edit RD.md in place (git keeps the history), pre-register any numerics, and rebuild rather than cite.

## Read first
- RD.md, RD_LOG.md and REVIEW_RD.md. The review's binding list is B1-B3, at roughly l.208-240.
- The consumer statements:
  - RECOVERY_CLUSTER_ASTRA.md l.344-357. Its full-factor conclusion *supposes* an exact identity for the intended denominator.
  - CODEX_REVIEW_STEP.md R11 (around l.194) and item 6 (around l.318).
  - STEP55's quotient.
- LIB1.md (R10, landed and CONFIRMED twice). You may use it as a landed input.
- HANDOFF "Current assignments". Do not do the active coordinator lanes: source radius, kernel remainder, coercivity/tails. Anything you need from them goes in as a named input with its exact expected form.

## Primary target: B1
Construct the **actual** returned denominator of one soft-kernel RG step (decision 4). Pin down, explicitly:
- the actual effective density;
- the legal history family;
- the integration and collar variables;
- the cuts;
- the reference.

Then prove an **exact** representation that covers the whole operation:
- how inherited terms enter;
- joint histories;
- every failed return;
- chart and contour complements.

RD's equation (17) cannot be assumed for this object. The success-only factor in (12) cannot stand in for it.

This is the identity the cluster theorem presupposes. Producing it, even with no bounds yet, is the main deliverable.

## Secondary targets, if reachable

**B2: bounds on that identity.** Supply:
- common source and coarse-field domains;
- nonzero reference bounds;
- local prefactor budgets;
- uniform interaction and failure majorants.

The review points out a defect in the current approach. A hard indicator that reaches zero has ‖Θ−1‖_∞ = 1, so a tail-probability bound does not control it. Use a different expansion: for example, smooth the cut, or treat the failed region as its own polymer type with its own activity. Prove whichever expansion you use.

**B3: induction closure.**
- Carry the reference comparison through the remaining integration and sum.
- Preserve the full source norm across holes.
- Close the effective-level/history induction.
- Match the result, prefactor by prefactor, to corrected CX-R and to STEP55's quotient.

## Status and records
- Mark each part PROVEN, ARGUED or OPEN. For anything still open, state the precise remaining sub-lemma. Never claim it as done.
- Update RD.md in place and log the changes in RD_LOG.md.
- Numerics are optional. If you run any:
  - write checks/rd2_criteria.md first;
  - lock with `until mkdir /Users/jonreilly/Projects/Physics/.claude/worktrees/ym4d-rd/.locks_numeric 2>/dev/null; do sleep 20; done`, then `rmdir` once;
  - stay under 1 GB, with load < 8 and at least 30% memory free.

## Rules
- Edit only RD.md, RD_LOG.md and checks/rd2_*.
- No commits.
- Final message under 300 words.
