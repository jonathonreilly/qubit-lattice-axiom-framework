# Historic intake: A charge on the pieces of the single cell's least-cost cuttings — Cycle 735

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — cites MINIMAL_AXIOMS_2026-06-29, nearest-neighbour adjacency and proper cubic rotations only

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The region switches of the cell's 15800 least-cost cuttings are NOT independent: free-switch (cube) behaviour occurs 276 times covering 480 cuttings but only ever at dimension 0, 1 or 2, and the obstruction is exhibited — of 273936 co-offered switch pairs, 54912 share a piece. In their place every floor cutting carries a two-sided charge realized as a GF(2) weight on the 192 pieces in play: the 120 region demands have rank 86, are consistent, and adding the demand that six-piece moves keep the charge raises the rank to 87 and cuts the labels to a single partition of sizes 7704 and 8096. All 46128 smallest moves reverse the charge, none of the 31968 six-piece moves does (and reversal at six pieces is provably impossible over GF(2)), while seven- and eight-piece moves are mixed (26880 of 60096 and 28608 of 151704).

Original verdict: The switches cannot be thrown independently, and what the population carries in place of independence is a two-sided piece-borne charge that the smallest move always reverses and the next smallest always keeps.
Scope: Scoped to the single cell of one lattice step and one tick with this adjacency cost and least volume; the group sizes, the dimension-two ceiling, and the two sides 7704/8096 are properties of this population of 15800 cuttings; time enters only as the fourth column and no result depends on an arrow.
Escape conditions (negative claims): Nothing identifies the charge with a physical quantity and nothing says it is conserved by any process; what a charge of this kind would mean for a lattice of many cells is not measured and not claimed. The charge depends on the demand that it be a sum over pieces — dropping that leaves 2^157 labellings. The pool of 192 pieces, the 120 regions and their 5 families are measured by search, not derived from symmetry.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The switches are NOT independent; a two-valued charge with dimension-bounded free behaviour is the obstruction — with the two overclaims self-flagged in place.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_LEAST_COST_CUTTING_PIECE_CHARGE_CYCLE735_NOTE_2026-08-05.md`
- Source commit: `2d1e2c0f8a612ee984d04c31b80c570fe8577e47`
- git blob: `71a0eb0fac7ff62e7e40acf551f9831aafa089fb`
- sha256: `be17fcbb6ef21172213d4429a3245158e0235074f86cfa119d49d8cfd1ec17d0`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3101_PHYSICAL_LEAST_COST_CUTTING_PIECE_CHARGE_CYCLE735_NOTE_2026-08-05.md](../../archive_unlanded/historic_intake_originals/recovery/3101_PHYSICAL_LEAST_COST_CUTTING_PIECE_CHARGE_CYCLE735_NOTE_2026-08-05.md)
- Lines: 230; runners named: none

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Self-flagged: two headline statements (that the charge reverses under all 46128 smallest moves and splits all 120 regions) are checks that the linear solve realized what was demanded, not discoveries — the note explicitly relocates the content elsewhere.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
