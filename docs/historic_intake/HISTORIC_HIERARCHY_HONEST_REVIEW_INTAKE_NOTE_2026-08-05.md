# Historic intake: Hierarchy Derivation: Honest Top-to-Bottom Review

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

Three errors invalidate the v = 226 GeV match: (1) Sigma_1 ~ 6.0 has no lattice-integral basis (exact I_stag(4) = 0.619734, d*I_stag = 2.479; the needed 3.81 corresponds to nothing known); (2) with framework GUT-normalized couplings at M_Pl (g_2 = 0.65, sin^2 theta_W = 3/8) the CW coefficient flips to B > 0 so EWSB does not trigger (|B_gauge/B_top| = 1.37); (3) the chain derives y_t = 0.439 but step 6 silently uses the SM y_t = 0.9369, without which v = 45 GeV not 226 GeV.

Original verdict: v is NOT derived — the framework gets the right order of magnitude via a legitimate mechanism, but the exact match was an artifact of mutually compensating errors.
Scope: Top-to-bottom review of the hierarchy derivation chain at M_Pl; corrects three specific inputs and recomputes v under each.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Erratum-grade: v = 226 GeV is NOT derived — three errors identified including a smuggled observed input; the honest kill of the hierarchy lane's numeric headline.

## Provenance (pinned)

- Original path: `docs/HIERARCHY_HONEST_REVIEW.md`
- Source commit: `5cccd784f8f9f31507dbcd617fd7191e2c9a7703`
- git blob: `b1fef4b6e7182cfe09666687d3cceaca525ddf78`
- sha256: `92e04a29cfe4c17c77e88f89799ebaa4a7e5c79121245f7a7372cc697ecf755a`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/696_HIERARCHY_HONEST_REVIEW.md](../../archive_unlanded/historic_intake_originals/branch03/696_HIERARCHY_HONEST_REVIEW.md)
- Lines: 246; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_sigma1_exact​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/HIERARCHY_SOLUTION_SUMMARY.md` — The v=226 claim; refuted by its own family's honest review.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Erratum-grade: explicitly identifies a smuggled observed input (y_t = 0.9369) and a fabricated constant (Sigma_1 ~ 6.0 attributed to a Luscher-Weisz value it does not have).
- Supersession (as known at extraction): Retrospective correction of the earlier hierarchy derivation chain (v = 226 GeV claim); includes a claim/status/corrected table.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
