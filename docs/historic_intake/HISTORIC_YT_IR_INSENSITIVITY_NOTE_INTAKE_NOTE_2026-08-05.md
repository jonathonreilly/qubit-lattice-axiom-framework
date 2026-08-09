# Historic intake: y_t IR Insensitivity: Does the Quasi-Fixed Point Kill the Gauge Crossover?

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

Registered as a bounded registration of a historical negative claim; no live no-go is asserted by this wrapper — no-go discipline applies at audit adjudication.

## The claim (as stated by the original, supervisor-compressed)

Tests whether the IR quasi-fixed point y_t/g_3 -> sqrt(2/9) makes m_t insensitive to g_3(M_Pl), which would render the gauge crossover irrelevant; REFUTED — varying g_3(M_Pl) over [0.5, 2.0] gives a 55% spread in m_t against a <5% insensitivity criterion, with only a factor-0.71 focusing.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Refutes the QFP-insensitivity escape: m_t varies materially with g_3(M_Pl) — the crossover blocker is real.

## Provenance (pinned)

- Original path: `docs/YT_IR_INSENSITIVITY_NOTE.md`
- Source commit: `1acae9ddc79350f95fd765194918ebb169a36c88`
- git blob: `c5da1507e114bb393c36b327c72e3e632f776a09`
- sha256: `95f488ca805cf5070ec20e380a4158884673069332b2f821d8c41226632a2807`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2322_YT_IR_INSENSITIVITY_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2322_YT_IR_INSENSITIVITY_NOTE.md)
- Lines: 143; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_ir_insensitivity​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The gauge crossover remains a genuine blocker.
- Extraction scope (triage compression; may reflect later context): SM 2-loop RGEs with the framework boundary y_t(M_Pl) = g_3/sqrt(6) and g_3 varied freely; the gauge trajectory still comes from the observed alpha_s(M_Z).
- Extraction red flags: Refutes an insensitivity claim that, had it held, would have removed the lane's main blocker.
- Supersession (as known at extraction): Refutes an escape hypothesis for the crossover blocker documented at idx 2312; complements the fixed-point mismatch at idx 2300.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
