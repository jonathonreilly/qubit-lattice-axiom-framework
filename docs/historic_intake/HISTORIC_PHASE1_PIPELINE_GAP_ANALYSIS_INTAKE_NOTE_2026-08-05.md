# Historic intake: Phase 1C — Pipeline gap analysis: what the toolchain does and does NOT check

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: meta
Stratum: pack_science_family
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

audit_lint​.py on origin/main reports 0 errors, 23 warnings, 441 notices — every defect the campaign was opened over passes clean. Seven defect classes, 7 of 7 NOT CAUGHT: runner-bearing note with no claim_id/row (350 graph nodes; 401 in review_feedback/ alone); runner referenced by no claim-bearing note (1569, of which 1161 have no graph node at all); prose status contradicting the live ledger (199 lines / 90 rows / 110 targets, not-caught BY DESIGN); mutual retained-assertion between unaudited notes; obligation registry omitting a binding conjunct (1 of 3); named gate with no node/row/criterion (8 memo bullets vs 7 registry nodes, :170 unregistered); note-linked runner with missing cache (16 primary + 80 helper, 56 `ready` rows affected). Ledger universe: 3872 rows, 4506 graph nodes, 5243 scripts, 3740 cache files.

Original verdict: VERDICT (c) PIPELINE GAPS is the root cause, (a) MISSING REGISTRATION is the dominant symptom at ~62% of affected surfaces, (b) is ~16% by volume and ZERO verdicts at risk, (d) is ~2% by volume but 3 verdicts at risk — matching the supervisor's pre-recorded prediction. Three independently sufficient structural facts: check_staged_claim_typing​.py:51-54 makes 'no ledger row' the PASSING condition; docs/work_history/** is line 19 of the exclusion file and should_gate_node runs before claim-typing so 401 of 450 review_feedback/ notes reference an existing runner and 0 have a row; and CI never runs on a PR or push (audit.yml:22-25) — the whole pipeline is a nightly cron.
Scope: origin/main at f865c14cd4, measured in a detached read-only worktree; nothing committed or edited.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

SYSTEMIC INTEGRITY MEASUREMENT (repo-state-scrub): audit_lint​.py on origin/main reports 0 errors while ALL SEVEN defect classes the campaign was opened over pass clean (7/7 uncaught); 401 of 450 review_feedback/ runner-gated notes have ZERO ledger rows; 1569 orphan runners; seven lint rules L1-L7 designed with a seven-batch priority order. Root cause verdict: (c) pipeline gaps with (a) missing registration dominant. Charter and lane diagnosis attached.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/repo-state-scrub-20260725/phase1_pipeline_gap_analysis.md`
- Source commit: `7d1b60b2f9648ee299fa050079afba04638cdcd3`
- git blob: `5849e5e76d5682fe28dff0dde8b5f7163946b542`
- sha256: `a9d1748ec240deb1388bcdab7c2467e9cc8be05f853d719851b0ac06b602d631`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci03/10831_phase1_pipeline_gap_analysis.md](../../archive_unlanded/historic_intake_originals/packsci03/10831_phase1_pipeline_gap_analysis.md)
- Lines: 994; runners named: historic runner (unpinned, not in this packet): `scripts/audit_lint​.py`; historic runner (unpinned, not in this packet): `scripts/audit_model_family_normalization_guard​.py`; historic runner (unpinned, not in this packet): `scripts/build_citation_graph​.py`; historic runner (unpinned, not in this packet): `scripts/check_staged_claim_typing​.py`; historic runner (unpinned, not in this packet): `scripts/check_staged_runner_ownership​.py`; historic runner (unpinned, not in this packet): `scripts/compute_audit_queue​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/physics-loops/repo-state-scrub-20260725/CAMPAIGN.md` — Campaign charter, opened at owner direction after two consecutive science campaigns each burned a wave REDISCOVERING repo content; 438-439 no_go rows with ZERO retained no-gos repo-wide; supervisor's pre-registered prediction recorded.
- `.claude/science/physics-loops/repo-state-scrub-20260725/phase1_A_registration_draft.md` — Diagnoses exactly why four runner-gated 2026-07-14 surfaces were invisible (excluded_sources listing et al.); decisively (c) for this lane.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: MAJOR: 401 of 450 review_feedback/ notes are runner-gated science with zero ledger rows; 1569 orphan runners; the only per-change ratchet treats 'no ledger row' as passing; CI is nightly cron only
- Supersession (as known at extraction): Designs seven lint rules L1-L7 and a seven-batch prioritized repair plan with an explicit 'Explicitly NOT recommended' section.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_tooling_audit_lint_rule_designs
intake_directive: owner_2026-08-05
```

Independent audit still required.
