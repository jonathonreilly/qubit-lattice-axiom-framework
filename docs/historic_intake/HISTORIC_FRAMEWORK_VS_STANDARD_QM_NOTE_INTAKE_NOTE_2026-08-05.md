# Historic intake: Framework vs Standard QM: Hydrogen and Helium

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

An honest three-level comparison: the framework reproduces hydrogen level ratios to within ~5% at N = 60 (E_2/E_1 = 0.25857 vs 0.25, E_3/E_1 = 0.11132 vs 0.11111, E_6/E_1 = 0.02896 vs 0.02778) with the Bohr radius emerging as r_0 = 2/g = 2.00 sites, while conceding a standard finite-difference SE solver would do as well or better on the same grid.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Honest comparison: numerically no better than a textbook solver; the framework's actual added content stated precisely.

## Provenance (pinned)

- Original path: `docs/FRAMEWORK_VS_STANDARD_QM_NOTE.md`
- Source commit: `63defc0de0b06b24cf681f7bb727406882c852f9`
- git blob: `668d3d762bc23acea7a691c24817c11e169e6d7b`
- sha256: `5e1c4678696b682dc1a16b23a7cf961e136419eb957f779697aa300800d5527f`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/510_FRAMEWORK_VS_STANDARD_QM_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/510_FRAMEWORK_VS_STANDARD_QM_NOTE.md)
- Lines: 292; runners named: historic runner (unpinned, not in this packet): `scripts/hydrogen_from_graph_dynamics​.py`; historic runner (unpinned, not in this packet): `scripts/helium_hartree_scf​.py`; historic runner (unpinned, not in this packet): `scripts/helium_jastrow_vmc​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The framework's added content is that the kinetic operator and Coulomb potential emerge together from one algebraic structure, whereas standard QM takes them as separate inputs; what it loses is the connection to SI units.
- Extraction scope (triage compression; may reflect later context): Level ratios only; the framework cannot predict E_1 in eV without alpha_EM and m_e, which is called a genuine deficit.
- Extraction red flags: Explicitly concedes the numbers are no better than a textbook SE solver and names the absolute-energy failure as a genuine deficit.
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
