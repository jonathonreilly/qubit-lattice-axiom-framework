# Historic intake: Koide Loop Iteration 5 — I5: Single-Rotation No-Go

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

No single Cl(3) bivector rotation with a clean (Q, delta) angle and a retained axis maps V_TBM to V_conj: the exact rotation has angle 0.1682 rad (best candidate sqrt(Q) delta = 0.1814, 7.88% off) and axis (-0.424, 0.753, -0.503) (best retained direction (0,1,-1)/sqrt2 at overlap 0.888), and a 90-candidate grid scan gets no closer than distance 0.109 against the 0.238 baseline.

Original verdict: Theorem-grade negative — the iteration-4 mechanism must be genuinely composite, with the mu-tau anti-diagonal as the dominant component.
Scope: Rules out single-bivector-rotation mechanisms only; 10 angle candidates and 9 axis candidates tested.
Escape conditions (negative claims): The negative is confined to single rotations with retained axes and (Q, delta) angles; composite (two or more rotation) mechanisms remain open and are the named next target.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Theorem-grade negative: no single Cl(3) bivector rotation with clean (Q, delta) angle and retained axis maps V_TBM to V_conj — the I5 mechanism is genuinely composite.

## Provenance (pinned)

- Original path: `docs/KOIDE_PMNS_SINGLE_ROTATION_NOGO_NOTE_2026-04-21.md`
- Source commit: `4055b01ead49ef4f16d856cea0b1a7cd2c4c208d`
- git blob: `a331618ce3a0145a58c2c6626845713548344475`
- sha256: `5cb6071964d601ce3f3483578e1e3b124ed730caae369bd52b8529727675be04`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/887_KOIDE_PMNS_SINGLE_ROTATION_NOGO_NOTE_2026-04-21.md](../../archive_unlanded/historic_intake_originals/branch03/887_KOIDE_PMNS_SINGLE_ROTATION_NOGO_NOTE_2026-04-21.md)
- Lines: 113; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_koide_pmns_single_rotation_nogo​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): Its conclusion is briefly overturned by iteration 11 and then restored by the iteration-12 revision.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
