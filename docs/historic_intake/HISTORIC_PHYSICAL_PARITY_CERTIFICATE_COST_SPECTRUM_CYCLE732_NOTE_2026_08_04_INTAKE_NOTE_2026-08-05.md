# Historic intake: The adjacency cost of a cell dissection is always even, and its spectrum is exactly the eleven even integers from 108 to 128

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — inputs are the lattice adjacency of MINIMAL_AXIOMS_2026-06-29 and nothing else

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Of the twenty-one integers in the known bracket [108, 128] exactly eleven — the even ones — are realised, and evenness is forced by an exhibited hand-checkable object: a set of 228 sample points meeting every least-volume piece in a number of points congruent mod 2 to that piece's adjacency charge, with 228 even. The parity argument carries no constant term, so it never appeals to piece count or volume. A complete sweep of all 98 subgroups of the cell's 48 symmetries shows exactly one of the 12 subgroups of order at least 12 admits an invariant certificate (order 12), so the symmetry given up is index 4 exactly; and 2 is the sharp modulus by two independent routes — the eleven costs have gcd of differences 2, and mod 3 no certificate exists due to an exhibited local obstruction common to the cell.

Original verdict: The cost spectrum is exactly the eleven even integers from 108 to 128, with the parity forced rather than observed.
Scope: About this single cell only, proved by exhibiting a certificate for its 2672 pieces; says nothing about any other object; inputs are the lattice adjacency of MINIMAL_AXIOMS_2026-06-29 and nothing else.
Escape conditions (negative claims): An earlier cycle's attempt at a parity law ACROSS objects was refuted and is not revived. The certificate was found by elimination and is not claimed unique or smallest. The mod-3 non-existence rests on an exhibited local obstruction rather than a failed search. The floor 108 and ceiling 128 are inherited from earlier cycles and re-verified, not re-derived. The eleven dissections are exhibited, not classified — the note does not say how many realise each cost.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The realised cost spectrum is exactly the eleven even integers in [108,128], parity FORCED by a hand-checkable 228-point object.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_PARITY_CERTIFICATE_COST_SPECTRUM_CYCLE732_NOTE_2026-08-04.md`
- Source commit: `c1e6e249073a1b9b909228545bbff199b6dfc4f9`
- git blob: `5e8ddac6e8a66d8256cc15313480f0f6b42fff22`
- sha256: `e56bb2cd7e9654255d1469bbb4315d92ca5dd3461d837df67386a9e492216b09`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3103_PHYSICAL_PARITY_CERTIFICATE_COST_SPECTRUM_CYCLE732_NOTE_2026-08-04.md](../../archive_unlanded/historic_intake_originals/recovery/3103_PHYSICAL_PARITY_CERTIFICATE_COST_SPECTRUM_CYCLE732_NOTE_2026-08-04.md)
- Lines: 224; runners named: historic runner (unpinned, not in this packet): `scripts/physical_parity_certificate_cost_spectrum_cycle732_2026_08_04(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
