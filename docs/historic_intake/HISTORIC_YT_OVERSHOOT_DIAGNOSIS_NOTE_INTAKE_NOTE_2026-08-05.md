# Historic intake: y_t Overshoot Diagnosis: Where Does the 6.5% Come From?

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

Decomposes the 184 vs 173 GeV overshoot into competing effects: a 1-loop baseline at +1.1%, the 1-loop to 2-loop RGE step at +9.2 GeV (+5.3%), and threshold corrections from n_f decoupling at -7.0 GeV (-4.1%), leaving a net +4.2 GeV (+2.4%). The full 6.5% appears only when 2-loop running is used without thresholds — an inconsistent approximation.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The overshoot decomposition: the widely quoted 6.5% figure came from inconsistent scheme use — corrective accounting of the 184-vs-173 gap.

## Provenance (pinned)

- Original path: `docs/YT_OVERSHOOT_DIAGNOSIS_NOTE.md`
- Source commit: `6edb0c838aa3ed8873a055e88ea5cc40a43620fa`
- git blob: `787aa3dc61a4632d620c7ac95fd39919d8bda045`
- sha256: `f218a7dbed8e8b6e23d10cf3d519446ac47e581a401df19f96f8b8f4d711a7f7`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2357_YT_OVERSHOOT_DIAGNOSIS_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2357_YT_OVERSHOOT_DIAGNOSIS_NOTE.md)
- Lines: 118; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_overshoot_diagnosis​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The overshoot is not a single source, and the best consistent estimate is a residual 2.4% rather than 6.5%.
- Extraction scope (triage compression; may reflect later context): Diagnostic, 9 PASS 0 FAIL; the boundary condition itself contributes 0% error.
- Extraction red flags: Shows that the widely quoted 6.5% figure came from an inconsistent approximation (2-loop running without thresholds).
- Supersession (as known at extraction): Reduces the headline gap that idx 2334, 2335, 2337 all try to close by matching, and that idx 2142 instead closes by re-scheming.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_result
intake_directive: owner_2026-08-05
```

Independent audit still required.
