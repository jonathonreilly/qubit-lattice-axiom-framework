# Historic intake: PMNS Selector Iter 7: Symbolic det(H) Derivation - Informative Partial

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

det(H) = E2 does not reduce: under delta q_+ = 2/3 the closure equation is an irreducible cubic in m over Q(sqrt2, sqrt3, sqrt6) with no clean factorization, and at the closure point only the two IMPOSED cuts hit below 1e-4 (delta_c q_+c within 4.5e-7 of 2/3, det within 1.6e-6 of sqrt8/3) while m_c and Tr(H_c) are 6.4e-3 from 2/3. Runner 1 PASS, 0 FAIL.

Original verdict: No third simple-value retained identity is manifest - det(H) = E2 is itself the identity at the polynomial level, not derived from simpler ones.
Scope: Symbolic derivation attempt plus a scan of all natural scalars at the closure point.
Escape conditions (negative claims): Iter 8 directions named: non-scalar operator-valued cuts, A-BCC axiomatic derivation, variational on the 1-D curve, or graceful acceptance of the 2-retained + 1-observational structure.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The informative failure: no third simple identity is manifest and Tr(H) misses 2/3 by 6.4e-3 at the iter-6 point — DIRECTLY contradicting the later iter-10 adoption.

## Provenance (pinned)

- Original path: `docs/PMNS_SELECTOR_ITER7_SYMBOLIC_DET_H_DERIVATION_NOTE_2026-04-21.md`
- Source commit: `aa15faa0271373e2cd0ff01343443184fd74599d`
- git blob: `54c8e8c089f4c460a9c0cab576589dbe6506cef5`
- sha256: `b208a688c12a8786c7efc816aaa85ffbb0080d314cf5981952c3f29818e3e1db`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch05/1590_PMNS_SELECTOR_ITER7_SYMBOLIC_DET_H_DERIVATION_NOTE_2026-04-21.md](../../archive_unlanded/historic_intake_originals/branch05/1590_PMNS_SELECTOR_ITER7_SYMBOLIC_DET_H_DERIVATION_NOTE_2026-04-21.md)
- Lines: 130; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_pmns_selector_iter7_symbolic_det_H_derivation​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Records that at the iter-6 closure point Tr(H) misses 2/3 by 6.4e-3, yet iter 10 adopts Tr(H) = 2/3 as the third exact retained identity by moving the point.
- Supersession (as known at extraction): Directly contradicts the later iter-10 claim, since it records Tr(H_c) = 6.4e-3 away from 2/3 at the two-cut closure point - i.e. the third identity is not satisfied there.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_informative_partial
intake_directive: owner_2026-08-05
```

Independent audit still required.
