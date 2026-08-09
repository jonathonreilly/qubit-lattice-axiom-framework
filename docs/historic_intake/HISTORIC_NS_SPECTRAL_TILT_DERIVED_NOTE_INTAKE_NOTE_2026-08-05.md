# Historic intake: Primordial Spectral Tilt n_s Derived from Cl(3) on Z^3

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

For d-dimensional lattice growth, n_s = 1 - 2/N_e - (d-3)/(d N_e^2) + O(1/N_e^3), so the sub-leading correction vanishes exactly at d=3, making n_s = 1 - 2/N_e exact to all orders in the graph-growth slow-roll expansion; with N_e = (1/3) ln(N_obs) and N_obs ~ 1e78 this gives n_s = 0.9667, within 0.43 sigma of Planck 2018.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

n_s = 1 - 2/N_e exact to all computed orders precisely at d=3 — an exact structural selection.

## Provenance (pinned)

- Original path: `docs/NS_SPECTRAL_TILT_DERIVED_NOTE.md`
- Source commit: `ec720017167b9f6d2ca09eb596f3c83b5fcff7c5`
- git blob: `5a54d5cf390c15b160f45144b88c9c9a1c55487e`
- sha256: `ab6b17d0326d6c76075214a1fba171546e18c3a41e8ad521b2f2858112c3cd90`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1221_NS_SPECTRAL_TILT_DERIVED_NOTE.md](../../archive_unlanded/historic_intake_originals/branch04/1221_NS_SPECTRAL_TILT_DERIVED_NOTE.md)
- Lines: 108; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_ns_derived​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): A bounded cosmological consistency check plus an exact structural selection for d=3; explicitly not paper-safe to say the framework derives the Planck spectrum from first principles or that r is predicted small.
- Extraction scope (triage compression; may reflect later context): The numerical match is BOUNDED (depends on N_obs ~ 1e78); the vanishing at d=3 is EXACT.
- Extraction red flags: none recorded
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded
intake_directive: owner_2026-08-05
```

Independent audit still required.
