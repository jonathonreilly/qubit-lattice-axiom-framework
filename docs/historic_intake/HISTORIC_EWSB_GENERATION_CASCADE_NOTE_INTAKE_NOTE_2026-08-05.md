# Historic intake: EWSB Generation Cascade: Mass Hierarchy from CW Symmetry Breaking

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

The graph-shift selector V_sel = 32 sum_{i<j} phi_i^2 phi_j^2 breaks S_3 -> Z_2 by picking a weak axis, the VEV then breaks the Z_3 generation symmetry (Hessian gives a flat direction plus two 64 v^2 modes), and the Kawamoto-Smit Jordan-Wigner structure splits the residual Z_2, so three distinct masses - hence three generations - follow from EWSB rather than being an input.

Original verdict: Claims to close the generation physicality gate - generations emerge from the same Coleman-Weinberg mechanism that generates the VEV and selects the weak axis.
Scope: Mass ratios are order-of-magnitude only: pure loop suppression gives 1 : 0.0027 : 7.3e-6 against the observed 1 : 0.0073 : 1.3e-5, and the up/top ratio needs large logs or Froggatt-Nielsen suppression.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The generation-cascade mechanism claim (S_3 -> Z_2 -> Z_3 breaking chain) with its gate-closure conflict and the beta_JW model-input flag — the generation-physicality contest's central positive.

## Provenance (pinned)

- Original path: `docs/EWSB_GENERATION_CASCADE_NOTE.md`
- Source commit: `b9c62621a26cb64763c9eba828559be77ec18b53`
- git blob: `380a89b7d22669bc41787e21743ffa39baea3a77`
- sha256: `1fce6b1721de11709cb1a796bb58ec76e0b7bd52e05c6c252332c6fb991183ff`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/448_EWSB_GENERATION_CASCADE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/448_EWSB_GENERATION_CASCADE_NOTE.md)
- Lines: 88; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_ewsb_generation_cascade​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/EWSB_CASCADE_PRECISION_NOTE.md` — Log-enhancement sharpening with double-counting open.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: The JW correction parameter beta_JW = 0.1 is a model input, not derived; the hierarchy is entirely radiative and quantitatively only order-of-magnitude.
- Supersession (as known at extraction): Its 'generation physicality gate closed' claim conflicts with EWSB_CASCADE_PRECISION_NOTE.md (idx 446), which states the gate remains open per review.md.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
