# Historic intake: Dimensional Scaling Law: Revisited

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pack_science_family
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Retracts the alpha=(d-1)/2 law: with unified matched parameters alpha is 0.13/0.35/0.64/0.44 for d=1..4 against the predicted 0.0/0.5/1.0/1.5, so the exponent is graph-density dependent, not a pure function of d. What survives is that alpha increases monotonically with spatial dimension and can reach F~M at 3 spatial dimensions under tuned parameters (connect_radius=4.5, gap=5).

Original verdict: PARTIALLY CONFIRMED - monotonic trend HIGH confidence, exact formula LOW and disowned.
Scope: Unified d=1-4 comparison at matched graph parameters; 5D unreliable due to sparsity.
Escape conditions (negative claims): The (d-1)/2 pattern could still emerge in a continuum limit if connect_radius/gap/nodes_per_layer are scaled together; not testable on finite discrete graphs here.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Retraction on the record: with unified matched parameters alpha runs 0.13/0.35/0.64/0.44 for d=1..4 against the predicted (d-1)/2, killing the exact law while keeping the monotonic trend HIGH-confidence. Pulled as a set with the retracted headline so audit sees both sides.

## Provenance (pinned)

- Original path: `.claude/science/analyses/dimensional-scaling-law-2026-04-01.md`
- Source commit: `ad7c6e4e8db2afb50d625703fb16b0368c9ffe9e`
- git blob: `056d8dbfb1a42c49b720af23e6f8b40fb172acba`
- sha256: `3b0f5f26e82f69b6f1eafa9d14060801e2f07ce9df153eb6a214316a5fcd398c`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci01/10001_dimensional-scaling-law-2026-04-01.md](../../archive_unlanded/historic_intake_originals/packsci01/10001_dimensional-scaling-law-2026-04-01.md)
- Lines: 82; runners named: historic runner (unpinned, not in this packet): `scripts/dimensional_scaling_law​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/analyses/dimensional-progression-2026-04-01.md` — The retracted headline claim (alpha=(d-1)/2 dimensional progression, self-marked CONFIRMED, parameter-tuned); evidence on the retraction wrapper.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: None beyond the retraction it carries; note is honest about parameter dependence.
- Supersession (as known at extraction): Corrects the headline claim of idx 10000 (dimensional-progression, same date).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_correction
intake_directive: owner_2026-08-05
```

Independent audit still required.
