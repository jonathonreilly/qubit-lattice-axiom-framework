# Historic intake: Static-Source NR Coulomb Current-Surface No-Go

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

Registered as a bounded registration of a historical negative claim; no live no-go is asserted by this wrapper — no-go discipline applies at audit adjudication.

## The claim (as stated by the original, supervisor-compressed)

Narrowed claim: current surfaces do not supply STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED; five inputs are missing (STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED, ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED, HARTREE_SCALE_MAPPING_RATIFIED, owner ratification, audit acceptance). Structural target: epsilon_n = -1/(2 n^2), E_n = E_H epsilon_n, E_H = m_e alpha(0)^2, Rydberg = E_H/2; kernel support G(r) -> 1/(4 pi |r|), V_lat(r) = -4 pi g G(r) -> -g/|r|, and V(r) = -C g_bare^2 G(r) -> -C alpha/|r| with alpha := g_bare^2/(4 pi).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Static-source NR Coulomb terminal: five inputs missing; the displayed equations are support, not proof inputs.

## Provenance (pinned)

- Original path: `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md`
- Source commit: `a750e4fdb1b4e8a0296a90db1cb51b74cf51b903`
- git blob: `cdeea1bd8c4f335935260cad51e28fbe51a50963`
- sha256: `374ea978a161dc579558003220cf846f16ad20e43be648f867f31664ee374819`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch08/2703_ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md](../../archive_unlanded/historic_intake_originals/branch08/2703_ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md)
- Lines: 313; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_current_surface_no_go​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_CURRENT_SURFACE_NO_GO_2026-07-05.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_RATIFICATION_DECISION_PACKET_2026-07-05.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` — Static-source ladder member.
- `docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` — Static-source ladder member.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Support-only non-supply boundary; the displayed equations are support and not proof inputs.
- Extraction scope (triage compression; may reflect later context): The final structural input of the static-source Rydberg lane.
- Extraction escape conditions (negative claims; triage compression): Ratify the static-source linear-response readout, the one-body NR physical-unit limit and the Hartree-scale mapping, then obtain owner ratification and audit acceptance.
- Extraction red flags: none recorded
- Supersession (as known at extraction): TERMINAL for the static-source NR Coulomb limit; packets 2704/2702/2705 feed it; it consumes m_e (Lane 6 terminal 2694) and alpha(0) (Lane 2 terminal 2509).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
