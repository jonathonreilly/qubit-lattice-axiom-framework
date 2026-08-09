# Historic intake: Hamming-Weight Parity Conservation Under Site-Phase Polynomials

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

For site-phase operators P_mu on C^{L^3} (L even), a monomial of order n has nonzero matrix elements only when H(alpha XOR beta) = n mod 2, so even-order polynomials preserve the hw-parity split C^8_even + C^8_odd (each dimension 4) and odd-order ones swap them; explicit projectors are Pi_± = (1 ± T_1 T_2 T_3)/2.

Original verdict: AIRTIGHT — combinatorial argument plus the Hamming-distance selection rule, runner 68/68 PASS.
Scope: BZ-corner operators built from site-phase products on an even-L cubic lattice.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Airtight Hamming-parity selection rule (68/68) — even-order polynomials preserve hw-parity.

## Provenance (pinned)

- Original path: `docs/HW_PARITY_CONSERVATION_NOTE.md`
- Source commit: `ddf443b4096131717a086480abb7a6a3150a7741`
- git blob: `15fbf97a4896bb7b8fe10c41cb68cd5a7cce47e3`
- sha256: `953f3570309a50d9330fef184d0fe058e9e79cfebaad36063fe891b8a641a9e1`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/718_HW_PARITY_CONSERVATION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch03/718_HW_PARITY_CONSERVATION_NOTE.md)
- Lines: 87; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_hw_parity_conservation​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): Composition result strengthening the translation-eigenvalue theorem and the Hamming-distance selection rule.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
