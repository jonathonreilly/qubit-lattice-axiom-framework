# Audit System Fitness Review — 2026-07-12

**Type:** meta
**Status authority:** process review only; no science claim, no audit verdict,
no registry action. Owner-requested top-to-bottom review of the audit and
review system against the last nine days of lived velocity and science work.

## The question

Is the assurance system fit for purpose, where the purpose is: fast-moving
collaborative science (≈96 PRs merged 2026-07-04 → 2026-07-12; axioms still
occasionally change) whose claims must be RIGHT, with the option of
whole-lane certification at any commit?

## Quantitative state (2026-07-12)

- Ledger: 3,737 rows; 380 retained-grade (10%); 2,947 unaudited (78%) after
  the cross-family regime reset and the 07-12 packet-invalidation incident.
- Landing velocity: ≈12 PRs/day. Audit throughput: ≈16 rows/day at peak,
  with heavy manual orchestration.
- Flagship-lane picture (rolling certification, first run): charged-lepton
  chain 31 blocking of 41; AC retirement basis 2 of 3; rule-universality
  grain 17 of 21; theta 1 of 1 — ≈51 rows to certify all four lanes.

## What demonstrably caught real defects (evidence, this window)

1. **Hostile review-loop passes** before landing: refuted the W2 sector-orbit
   partition theorem (unlabeled-PVM counterexample), corrected the W1a
   eraser-control and repeat-action claims, bound the W1b Candidate-1
   quotation, caught nine findings on one PR.
2. **Independent cross-family re-derivation audits**: found a false displayed
   Pauli-product formula and two hard-coded runner booleans in a foundational
   note that had previously passed twice.
3. **Owner review**: rejected the T1 "non-addition = exclusion" inference.
4. **Content-hash invalidation** (premise-hash resets) after axiom edits.

## What caught nothing real while consuming the budget

Full-universe N6/N8 candidate dispositions (68 → 1,711 candidates/row),
manifest-containment scans on theorem rows, repeated packet re-authoring
against live-rebuilt indexes, and the snapshot set-identity invalidation
sweep (wiped 230 verdicts including doubly-confirmed cleans within hours;
zero restorable due to snapshot schema succession). None of these produced a
single scientific finding in the window.

**Conclusion already enacted (owner-approved):** two-tier assurance
(#5265 + #5280 + #5283) — forensic plumbing at no-go rows and pinned-commit
certification runs; content-bound structural assurance elsewhere; rolling
lane certification instead of scheduled freezes.

## Findings and dispositions

**F1 — Throughput is the binding constraint (CRITICAL).** ≈16 rows/day
against a 2,947-row backlog cannot converge; uniform queue draining is the
wrong shape anyway. Disposition: (a) lane-first targeting is now available
(certification `blocking` lists; ≈51 rows to certify all flagship lanes);
(b) NEEDED: a first-class batch audit orchestrator — parallel restricted-
packet fleets (the pattern run by hand this week: N workers, pinned
manifests, serialized apply+push, delta-completion built in) as a repo
script with a lane argument. Size: 1–2 days infra. Highest-value follow-up.

**F2 — Audit-infra changes need a lane canary (HIGH).** The 07-12 hardening
landed with green unit tests yet closed the lane the same day (unattainable
packets) and wiped 230 verdicts — unit tests validate code, not the
lane. Disposition: review-loop infra reviews MUST run one real row
end-to-end (packet build → auditor-format check → apply → pipeline →
invalidator survival) before landing any change to
apply_audit/no_go_discipline_gate/invalidate_stale_audits. Recorded here as
policy; add to the review-loop skill checklist (follow-up, doc-only).

**F3 — Snapshot/schema succession policy (MEDIUM).** Verdict evidence
schemas will evolve; the 230-row loss shows a bump without a stated
disposition orphans prior verdicts. Disposition: any PR changing packet or
snapshot schemas must state, in the PR body, the disposition of prior-era
verdicts (migrate | grandfather-until-content-change | scheduled re-audit),
and the invalidator must implement that stated disposition rather than
defaulting to hard invalidation. Policy recorded here; enforcement is a
review-loop checklist item (same follow-up as F2).

**F4 — Orchestration sharp edges are now load-bearing knowledge (MEDIUM).**
Learned this window: stdin-close on codex launches; NEVER launch a worker
and wait in one timed shell call (timeout SIGTERM kills the child); monitor
on deliverable size, not existence (placeholder files); spec parentheticals
get copied verbatim into notes (write executed text, review for leaks);
mint transport envelopes seconds before apply; the envelope expires in 2h.
Disposition: partially recorded in the audit-loop skill (#5283) and the
workhorse skill; the remainder recorded here. No code change.

**F5 — Auditor monoculture (MEDIUM, standing risk).** All current passes are
one model family; `cross_family` measures auditor-vs-author, not pool
diversity, so correlated blind spots are unmeasured. The strongest catches
this window included one only the owner made. Disposition: when
collaborators or additional strong model families are available,
flagship-lane terminal cleans should prefer family-diverse pass pairs;
`auditor_reliability.json` already gives the tracking surface. Config knob
is a follow-up; until then owner spot-review of flagship-lane cleans remains
load-bearing and should be treated as part of the process, not a favor.

**F6 — Velocity instrumentation (LOW).** Nothing measured coverage trend or
time-to-terminal. Disposition: an append-only
`lane_certification_history.jsonl` written by the certification step each
pipeline run (lane, certified, blocking count, head SHA, timestamp) — the
per-lane "are we converging" trend line. Lands as a small follow-up commit
to `compute_lane_certification.py` once #5280 merges (the script is in that
PR's review right now).

**F7 — Review-loop stacked-PR and infra briefs (LOW).** Each stacked or
infra review this window needed a hand-written brief (stack awareness,
infra checklists). Disposition: fold both into the review-loop skill as
standing sections (follow-up, doc-only, small).

## Bottom line

Fit for purpose **after** the two-tier calibration, **provided** F1 (batch
orchestrator + lane-first draining) lands promptly — throughput, not rigor,
is now the gating risk to both velocity and rightness (unaudited science is
the actual exposure). The rigor budget is now spent where the evidence says
defects are caught: hostile review at landing, independent re-derivation at
audit, forensic packets at permanent-foreclosure rows and certification
commits, owner eyes on flagship cleans.

## Named follow-ups (sized)

1. `orchestrate_audit_batch.py` — parallel fleet + serialized apply, lane
   argument (1–2 days). F1.
2. Review-loop skill: infra-review checklist incl. lane canary + schema
   succession statement + stacked-PR protocol (doc-only, small). F2/F3/F7.
3. `lane_certification_history.jsonl` append in
   `compute_lane_certification.py` (tiny, after #5280 merges). F6.
4. Family-diversity preference knob for flagship terminal cleans (small,
   after a second strong family is available). F5.
