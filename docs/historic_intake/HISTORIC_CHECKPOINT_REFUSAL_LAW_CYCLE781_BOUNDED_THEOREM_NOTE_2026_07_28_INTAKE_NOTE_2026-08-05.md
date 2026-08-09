# Historic intake: The checkpoint law — syndrome completeness achieved, and the guard regress that stops everything after it — Cycle 781

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Builds the best permanence-law candidate the framework's reversible primitives allow — a checkpoint guard compiled purely from X/CNOT/TOF over the landed layout, achieving syndrome completeness where the landed law was blind — and then confirms mechanically that every such guard hits a regress, stating the new-primitive requirement exactly.

Original verdict: LAW_PARTIAL: the construction works but no reversible-primitive guard can finish the job — a new primitive is required.
Scope: REGRESS_CONFIRMED is scoped to the guards constructed and tested (primary's, majority-3, refresh) under arbitrary M2 words, with defeaters exhibited mechanically; the universal statement over all guards is not claimed.
Escape conditions (negative claims): The regress is demonstrated only for the three tested guard families; a guard outside those families, or a new primitive, is the stated escape.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

LAW_PARTIAL permanence result: syndrome-complete checkpoint guard built, and no reversible-primitive guard can close the job (regress demonstrated for three families) — the W4/W5 lane's honest wall.

## Provenance (pinned)

- Original path: `docs/CHECKPOINT_REFUSAL_LAW_CYCLE781_BOUNDED_THEOREM_NOTE_2026-07-28.md`
- Source commit: `72efa390fc444a220719ebd261d367145f1e895a`
- git blob: `de992a4345d4a80cc9d22c4adbecc72e940e99a5`
- sha256: `a4da1b9e418534306caeb62be0884a3462692a91c5b0fed202252c913c2c5066`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/145_CHECKPOINT_REFUSAL_LAW_CYCLE781_BOUNDED_THEOREM_NOTE_2026-07-28.md](../../archive_unlanded/historic_intake_originals/branch01/145_CHECKPOINT_REFUSAL_LAW_CYCLE781_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- Lines: 114; runners named: historic runner (unpinned, not in this packet): `../scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28​.py`; historic runner (unpinned, not in this packet): `../scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28​.py`; historic runner (unpinned, not in this packet): `frontier_cycle781_checkpoint_independent_check_2026_07_28​.py`; historic runner (unpinned, not in this packet): `frontier_cycle781_checkpoint_refusal_law_2026_07_28​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): Answers Cycle 777's specification of the missing permanence law.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
