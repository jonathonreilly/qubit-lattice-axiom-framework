# Historic intake: Plaquette Open-Surface Hierarchy on the Exact 3+1 Lattice

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

Same-boundary surfaces differ by a closed 2-cycle, the minimal nontrivial closed 2-cycle is the 6-face cube boundary, so the first nonlocal completion has area 1 + 6 - 2 = 5, and on the 3+1 lattice there are exactly 2*(4-2) = 4 such minimal completions. Hence P is an open-surface problem, not a one-cell problem. Runner 6 pass / 0 fail.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The structural explanation of the constant-lift failure (closed 2-cycle area accounting) with the forward route named.

## Provenance (pinned)

- Original path: `docs/PLAQUETTE_OPEN_SURFACE_HIERARCHY_NOTE.md`
- Source commit: `60a264ba93427b648c4c01edb5b2437542b78eb5`
- git blob: `b710f58d012ea2c6255e4f52e4dc0d9890e9087f`
- sha256: `c61b0e827be0b54cd1c8cc89649f2938bf151915b026a3724ba34bff4faa9ae0`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch05/1511_PLAQUETTE_OPEN_SURFACE_HIERARCHY_NOTE.md](../../archive_unlanded/historic_intake_originals/branch05/1511_PLAQUETTE_OPEN_SURFACE_HIERARCHY_NOTE.md)
- Lines: 164; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_plaquette_open_surface_hierarchy​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The constant-lift failure was structural - any real derivation of P must close an open-surface hierarchy rather than dress a one-plaquette block.
- Extraction scope (triage compression; may reflect later context): Exact combinatorics of same-boundary surfaces; does not derive P(beta = 6).
- Extraction escape conditions (negative claims; triage compression): The route forward is named: gauge source identity P = (1/N_plaq) d log Z/d beta, rewrite on the open-surface side, then close the same-boundary hierarchy.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Follows GAUGE_PLAQUETTE_SOURCE_NO_GO_NOTE; its successors are the first-nonlocal-connected-correction note and then the rooted 3-chain engine, which CORRECTS an earlier boundary-shellable undercount and shows directed-cell face-factorized closure already fails at n = 3.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_exact_combinatorial_theorem_and_next_derivation_program_after_the_constant_lift_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
