# Historic intake: Exact Staggered Self-Energy Tadpole Integral Sigma_1

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

Computes the 1-loop staggered tadpole to 10 digits: I_stag(4) = 0.619733560924 = 4 * I_Wilson(4), c_latt = 0.6134137604, and identifies Sigma_1 = pi^2 I_stag(4) = 6.1165, which is +1.9% above the previously used estimate 6.0 and shifts v by about 15% through the exponential. Lattice and quadrature methods agree to < 1.4e-7.

Original verdict: Complete: pinning v = 246.22 GeV requires alpha_s(q*) = 0.4897, Z_chi = 0.6822, N_eff = 5.585, which is the standard coupling at the Lepage-Mackenzie scale.
Scope: Periodic L^d lattices L = 8..128 with Richardson extrapolation, cross-checked by scipy nquad; d=3 is IR-divergent and has no infinite-volume limit.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Sigma_1 computed to 10 digits replacing the estimate — WITH the flag that closure then requires alpha_s(q*) = 0.4897 chosen to fit; the hierarchy lane's honest arithmetic.

## Provenance (pinned)

- Original path: `docs/SIGMA1_EXACT_NOTE.md`
- Source commit: `e24b94c6e4efc20c051247c7a257e79f7cbaac17`
- git blob: `9b262c274b7d708fe7b23c2c3c2585415d7909c7`
- sha256: `793a2bc1395ba9f8ddd4e4454e4423c5a95ee127d83f72a6715b03b1cdbc57b7`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1925_SIGMA1_EXACT_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1925_SIGMA1_EXACT_NOTE.md)
- Lines: 141; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_sigma1_exact​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: The hierarchy is closed by choosing alpha_s(q*) = 0.49 to hit the measured VEV, and the error budget attributes ~15% of the v uncertainty to that matching-scale choice; the +1.9% correction to Sigma_1 also revises a previously banked number.
- Supersession (as known at extraction): Replaces the estimated Sigma_1 = 6.0 used in the earlier hierarchy formula with the exact 6.1165.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
