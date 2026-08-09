# Historic intake: Koide Brannen — Callan-Harvey Candidate: Sharpening & Alternate ABSS Route

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

A first version of this note claimed to close the three Callan-Harvey gaps and was refuted by hostile review; the revision concedes all three P0 critiques — the anomaly-to-CP^1 operator map is TRIVIAL (homogeneous Y_q on generation sites Fourier-transforms to Y_q I, and the note had silently substituted the target Berry phase generator), the descent factor Omega = 1 is a chosen anomaly-active sector not a derived theorem, and gap 1 is only numerical consistency after both sides were normalized to 2/9 (|delta_Berry - delta_CH| ~ 1e-13).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The CH-route retraction record: v1 closure refuted by hostile review, all three P0 critiques conceded — pattern documentation the lane needs.

## Provenance (pinned)

- Original path: `docs/KOIDE_BRANNEN_CH_THREE_GAP_CLOSURE_NOTE_2026-04-22.md`
- Source commit: `0009ff9fd09141790e40f399a29ced192123deea`
- git blob: `75e2ebf25eb1a7c4b99219f61c8ae645f88b0425`
- sha256: `d38f55a64e9746e8aa19990fb008462fca967aeafc50726fb1189e905572e04e`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/761_KOIDE_BRANNEN_CH_THREE_GAP_CLOSURE_NOTE_2026-04-22.md](../../archive_unlanded/historic_intake_originals/branch03/761_KOIDE_BRANNEN_CH_THREE_GAP_CLOSURE_NOTE_2026-04-22.md)
- Lines: 459; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_koide_brannen_ch_three_gap_closure​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_koide_brannen_absss_equivariant_descent​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/KOIDE_BRANNEN_PHYSICAL_BRIDGE_DERIVATION_NOTE_2026-04-22.md` — Bridge-CLOSED claim beside its hostile-review context — tension flagged.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The CH route fails the closure bar — a nontrivial CH operator map would require the bulk Y-background to be Z_3-inhomogeneous across generations, which the retained data does not supply.
- Extraction scope (triage compression; may reflect later context): Support-level consistency only; the 16/16 PASS runner is explicitly a numerical consistency harness, not a closure theorem; an alternate ABSS-equivariant-descent route is attempted separately and still leaves the dimensionless-to-radian identification open.
- Extraction escape conditions (negative claims; triage compression): The stated escape from the trivial-operator obstruction is a Z_3-breaking or Z_3-equivariant bulk Y-background with different per-site Y-flux; the alternate route needs either an independent axiom-native characterization of m_* (the open I3 lane) or different structure, since ANOMALY_FORCES_TIME's natural-time convention alone cannot fix 2/9 rad at m_*.
- Extraction red flags: Documents a retracted closure claim and preserves three reviewer P0 critiques verbatim; one earlier internal claim (Q_Sigma = Y_q sigma_3) is stated to be incorrect, with the runner confirming the opposite.
- Supersession (as known at extraction): Revises and retracts the closure claim of its own first version (commit b947506b) after hostile review; targets the three open items of KOIDE_BRANNEN_CALLAN_HARVEY_CANDIDATE_NOTE_2026-04-22 Section 3 and closes none of them.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
