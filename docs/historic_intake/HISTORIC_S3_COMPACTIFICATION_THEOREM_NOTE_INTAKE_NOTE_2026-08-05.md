# Historic intake: S^3 Compactification / Cap-Map Uniqueness — Honest Audit

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

Audit that DOWNGRADES the S^3 claim from 'structural/derived' to BOUNDED, finding two formal gaps: G1, Hamiltonian homogeneity is imported not derived (the prior claim that identical local Hilbert-space factors force regularity is stated to be incorrect), and G2, that closure preserves simple connectivity is unproved. Also flags that no cubic lattice embedding of S^3 exists (the natural periodic closure of Z^3 is T^3).

Original verdict: BOUNDED (near-structural): S^3 is a strong conjecture supported by exact results and reasonable assumptions, not a derived theorem.
Scope: Audit of the finite-H -> regular graph -> closed -> simply connected -> Perelman chain; runner PASS=10 FAIL=2.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The honest S^3 downgrade: 'structural/derived' -> BOUNDED with two formal gaps named (homogeneity imported; prior regularity argument incorrect) — retraction on record.

## Provenance (pinned)

- Original path: `docs/S3_COMPACTIFICATION_THEOREM_NOTE.md`
- Source commit: `ccab562ebde768c686cd884f8c8429266485f466`
- git blob: `f69491b658c87720b001ac453f7517718dd55428`
- sha256: `ad197f0b7249a7e42d85c437173fc81fa4c6c80a927bae18d7d6480d62954f62`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1852_S3_COMPACTIFICATION_THEOREM_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1852_S3_COMPACTIFICATION_THEOREM_NOTE.md)
- Lines: 140; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_s3_compactification​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Explicitly retracts a previously claimed structural result and calls a prior note's regularity argument incorrect; also quotes RP^3 ratio 2.40, disagreeing with both 0.920 (idx 1848) and 2.45 (idx 1840).
- Supersession (as known at extraction): Directly corrects the prior 'ALL TESTS PASS / structural' framing of S3_COMPACTIFICATION_NOTE (idx 1850) and its Argument A.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
