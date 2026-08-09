# Historic intake: The adjacency cost of a cell dissection is 108 plus the number of its pieces outside one fixed list

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — cites MINIMAL_AXIOMS_2026-06-29 admissibility content as the structural analogue

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

An exhibited floor certificate at denominator 216 has slack spectrum exactly {0, 216} over all 2672 minimal pieces, which turns the bound into an exact formula: the adjacency cost of any 24-piece cell dissection equals 108 plus the number of its pieces outside the certificate's support (38 orbits). Consequences: every dissection contains at least 4 pieces inside the support and one attaining cost 128 contains exactly 4; the ceiling admits no such indicator reading, blocked by an exact integer identity (five of 57 orbit rows carry a dependency with coefficients summing to zero whose charge combination is nonzero), and a complete sweep finds 185 minimal-support five-element dependencies, all of coefficient sum zero, 49 with nonzero charge combination.

Original verdict: The cost of a dissection is a count — a fixed baseline plus a count of pieces failing one fixed local test — so the optimum is computed locally rather than merely certified locally, and the excess is a defect density.
Scope: Measures the single cell only; sample points certify bounds and covers and are not a proof device for regularity, face-to-face structure, or any block statement; the locality reading is offered as a structural echo of the admissibility form in MINIMAL_AXIOMS_2026-06-29, explicitly not a derivation of it.
Escape conditions (negative claims): The 'no ceiling indicator' claim rests on the positive integer identity, not on the exhibited ceiling certificate's slack spectrum (which is recorded as a measurement of one certificate and nothing more, since negative properties of a single certificate do not survive perturbation). The identity-perturbation sweep reaches only the 31 orbits occurring in the four exhibited dissections. The five-orbit relation is not unique and is not claimed to be. The floor denominator 216 is a carrier with no minimality claim (unlike the ceiling's 3, shown least by divisibility).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Zero-slack floor certificate turns the bound into an exact formula: adjacency cost = baseline + count of pieces failing one fixed local test — cost as a count.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md`
- Source commit: `7d067735492c0775eebb02e2e9b0db29e059a0c6`
- git blob: `f279b9c2aa096619252882ecb295350623eb73bb`
- sha256: `6ff14a265fb97744da85889f47921d40fb1fa7579908bc6e4815280fb248a752`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3097_PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md](../../archive_unlanded/historic_intake_originals/recovery/3097_PHYSICAL_COST_IDENTITY_INDICATOR_CERTIFICATE_CYCLE731_NOTE_2026-08-04.md)
- Lines: 223; runners named: historic runner (unpinned, not in this packet): `scripts/physical_cost_identity_indicator_certificate_cycle731_2026_08_04​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md` — The base one-cell bracket the exact formula refines.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Self-stated: validity of the floor rows taken alone is weak (lowering a live entry or doubling the denominator preserves validity while destroying the value); the six-suffice/five-do-not support claim is scoped to forced completions, not to all cost-108 dissections; the receipt is transcribed from output rather than written by the runner.
- Supersession (as known at extraction): Builds on Cycle 725 (cell cost interval 108 to 128, both ends attained) and Cycle 730 (zero-gap certificate membership test).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
