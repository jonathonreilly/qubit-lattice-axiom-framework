# Historic intake: Lorentz and CPT Violation from Lattice Structure

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

The cubic Z^3 lattice breaks SO(3,1) to O_h with leading correction delta(E^2) = -(a^2/12) sum p_i^4; at a = l_Planck this is a^2/12 = 5.60e-40 GeV^-2, generating only dimension-6 CPT-even SME coefficients c^(6)_(I)00 ~ 3.4e-40 and c^(6)_(I)40, c^(6)_(I)44 ~ 4.5e-40 GeV^-2, with all j=1,2,3 components and all CPT-odd coefficients (a_mu, b_mu, e_mu, f_mu, g_lmn) identically zero. Direction dependence gives a factor-of-3 anisotropy between [100] (f_4 = 1.000) and [111] (f_4 = 0.333).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Clean classification: dim-6 Lorentz violation YES, CPT violation NO (all SME-odd coefficients zero) — with the Greenberg-converse argument.

## Provenance (pinned)

- Original path: `docs/LORENTZ_VIOLATION_NOTE.md`
- Source commit: `5b723e41720e159fa261b4cbbf23d32ad30f09c4`
- git blob: `14f75e6dbd5739e9b8c9fdcb42ec2bc7fc12c1a6`
- sha256: `741e7d6b83b107b75f01599358329d491a6893b5be1e2800663737113d00c7fe`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1122_LORENTZ_VIOLATION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch04/1122_LORENTZ_VIOLATION_NOTE.md)
- Lines: 183; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_lorentz_violation​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Lorentz violation YES (dim-6, a^2 p^4), CPT violation NO — all CPT-odd SME coefficients identically zero, which is the strong falsifiable prediction: any detection of CPT-odd Lorentz violation would falsify the cubic lattice framework.
- Extraction scope (triage compression; may reflect later context): Predictions at Planck lattice spacing; suppression (E/E_Pl)^2 ~ 1e-38 at 1 GeV, below all current bounds by at least 6 orders, closest approach ~2 orders in photon birefringence at TeV.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Argues the Greenberg (2002) theorem's converse fails here because the framework is not a continuum local QFT, so LV without CPT violation is consistent.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis_prediction_summary
intake_directive: owner_2026-08-05
```

Independent audit still required.
