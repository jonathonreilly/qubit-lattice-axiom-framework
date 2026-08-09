# Historic intake: Z_3 Cyclic-Subgroup Commutant on C^8

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

Proves C^8 = (C^2)^{tensor 3} decomposes under Z_3 = <sigma> (cyclic permutation of the three taste-cube axes) as 4.1 + 2.chi_omega + 2.chi_omega^2 with Hamming-weight blocks 1/regular/regular/1, giving dim End(C^8)^{Z_3} = 4^2+2^2+2^2 = 24 by Schur's lemma. Runner 20/20 PASS, including a direct solve of the 64-dimensional commutator system [sigma, M] = 0 recovering kernel dimension 24.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Airtight Z_3 taste-algebra decomposition theorem (4.1 + 2.chi + 2.chi-bar, five independent verifications) — grind-grade exact infrastructure.

## Provenance (pinned)

- Original path: `docs/Z3_CYCLIC_COMMUTANT_NOTE.md`
- Source commit: `87375536ab5e9396c80358f285464b73f64bbbdd`
- git blob: `ab8536d6d66d70c1dbde502ba3c3d922ead9eb72`
- sha256: `cff8d7bda0ea7e567f0dcd77c7b038812d36faec6fc1853ae2a2c87d3ed8c6dd`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch08/2503_Z3_CYCLIC_COMMUTANT_NOTE.md](../../archive_unlanded/historic_intake_originals/branch08/2503_Z3_CYCLIC_COMMUTANT_NOTE.md)
- Lines: 89; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_z3_cyclic_commutant​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Airtight (self-described) pure-algebra theorem verified five independent ways by the runner.
- Extraction scope (triage compression; may reflect later context): Representation-theoretic decomposition and commutant dimension of the Z_3 cyclic action on the taste cube; classical inputs are Schur's lemma and cyclic-group representation theory.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Sharpens the Batch 2 C_3 Cyclic Action theorem (orbit structure 1+3+3+1) to full representation content; flagged as reusable for CP-phase / omega-label operators preserving Z_3 but not S_3.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
