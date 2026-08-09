# Historic intake: DM Lane: Nucleation Finding - Detonation Regime

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

The bounce computation gives T_c = 222.6 GeV, T_n = 200.5 GeV, T_n/T_c = 0.90, at which the driving pressure is too large for Boltzmann friction to balance: the force-balance equation has no solution below the Jouguet velocity, pushing the wall into the detonation regime v_w > c_s where diffusion-transport baryogenesis fails.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The nucleation NEGATIVE: no force-balance solution — the wall runs away (detonation problem), conflicting with its same-day sibling; the pair goes to audit together.

## Provenance (pinned)

- Original path: `docs/DM_NUCLEATION_FINDING_NOTE.md`
- Source commit: `81a4efe78660d1bb27dc930c5e7cd8d8f2cc9149`
- git blob: `32567a847a81ec90ed88b4e85e297e794cdb301d`
- sha256: `9830bfa861dad46cb784020eea5ba96483adc39ed4764a8f58333d488c1271fc`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/388_DM_NUCLEATION_FINDING_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/388_DM_NUCLEATION_FINDING_NOTE.md)
- Lines: 71; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_dm_nucleation​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/DM_NUCLEATION_TEMPERATURE_NOTE.md` — The conflicting positive measurement (T_n = 180.6, v/T = 0.80) with MC-calibrated R_NP flagged.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Does not invalidate the DM relic ratio R, but the transport sector has a genuine dynamical issue the earlier v_w range [0.006, 0.048] did not capture; the lane stays BOUNDED on transport.
- Extraction scope (triage compression; may reflect later context): At taste scalar mass m_s = 120 GeV with the 1-loop Daisy high-T potential and nucleation criterion S_3/T = 140 - all four flagged as possible sources of the problem.
- Extraction red flags: Negative finding: the framework does not uniquely predict m_s, and the detonation outcome depends on that undetermined mass; also directly inconsistent with the sibling nucleation-temperature note's T_n/T_c.
- Supersession (as known at extraction): Conflicts with DM_NUCLEATION_TEMPERATURE_NOTE.md (idx 389), which reports T_n/T_c = 0.983 and a subsonic v_w = 0.019 on the same lane.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded
intake_directive: owner_2026-08-05
```

Independent audit still required.
