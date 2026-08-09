# Historic intake: Hamming-Distance Selection Rule for BZ-Corner Transitions

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Site-phase operators satisfy <X_beta|P_{mu_1}...P_{mu_k}|X_alpha> = delta_{alpha XOR beta, XOR_i e_{mu_i}} by character orthogonality on even L, so the minimum number of insertions connecting two BZ corners equals the Hamming distance - and since the three hw=1 corners are pairwise at distance 2, single site-phase operators cannot mediate hw=1 to hw=1 transitions.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Universal Hamming-distance selection rule by character orthogonality — grind-program exact infrastructure.

## Provenance (pinned)

- Original path: `docs/HAMMING_DISTANCE_SELECTION_RULE_NOTE.md`
- Source commit: `2a002cb80cfebe4b8cf150ef75d4d99bb5c6e111`
- git blob: `70c99df92e8b705d3252e3f52371ee3e29ddef3a`
- sha256: `2b1c0e980ebf1dab0dea47cf8d70caa3ff72d2f288c5e6b297dec5a7ed26301b`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/669_HAMMING_DISTANCE_SELECTION_RULE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/669_HAMMING_DISTANCE_SELECTION_RULE_NOTE.md)
- Lines: 94; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_hamming_distance_selection_rule​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): A universal selection rule for polynomial site-phase operator products on Z_L^3 acting on BZ corners, with at least two insertions required for generation mixing.
- Extraction scope (triage compression; may reflect later context): Explicitly limited to products and linear combinations of the site-phase operators P_mu; non-constant phase profiles need separate analysis.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Batch 1 member of the grind program (idx 654) and an input to the Hadamard/S_3 composition (idx 660).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
