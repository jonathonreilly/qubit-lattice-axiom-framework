# Historic intake: Poisson Uniqueness Theorem

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

On Z^3 with nearest-neighbour coupling the graph Laplacian is the unique translation-invariant self-adjoint operator whose Green's function decays as 1/r and is attractive: the zero-mode condition forces c_0 = -6 c_1, Taylor expansion gives L_hat(k) = -c_1|k|^2 + O(|k|^4), the bracket 3 - cos k_1 - cos k_2 - cos k_3 vanishes only at k = 0, and attraction forces c_1 > 0. Corollary: adding a mass term makes the Green's function Yukawa, ruling out massive gravitons in this class.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Poisson uniqueness within the stated class — WITH the EXACT-header-vs-3/5-numerical-FAILs flag on the record.

## Provenance (pinned)

- Original path: `docs/POISSON_UNIQUENESS_THEOREM_NOTE.md`
- Source commit: `01fcc3c83d644fb34bb42cbc881565cd3b4d7e3f`
- git blob: `46114a36df713f04767281651acfa9f11bd2447e`
- sha256: `987e8ea34d882f6d9320c0f9c829884b9be9290b175c0c8a825e4cc102349150`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch05/1605_POISSON_UNIQUENESS_THEOREM_NOTE.md](../../archive_unlanded/historic_intake_originals/branch05/1605_POISSON_UNIQUENESS_THEOREM_NOTE.md)
- Lines: 166; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_poisson_uniqueness_theorem​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Exact - the 5/5 algebraic steps are the proof; three of five numerical checks FAIL from finite-size artifacts and are explicitly not load-bearing.
- Extraction scope (triage compression; may reflect later context): Explicit assumptions: translation invariance, nearest-neighbour connectivity, self-adjointness and exact 1/r decay; the proof is on infinite Z^3, with finite-lattice numerics as consistency checks only.
- Extraction escape conditions (negative claims; triage compression): The uniqueness bites only within the stated operator class - beyond nearest-neighbour or beyond exact 1/r decay it says nothing.
- Extraction red flags: Header advertises EXACT while the same runner reports 3/5 numerical checks FAILING; the note argues these are finite-size artifacts, but a reader scanning runner output would see failures.
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_exact_algebraic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
