# Historic intake: What a two-cell block costs, pinned at both ends, and why lifting cannot reach the top

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — cites MINIMAL_AXIOMS_2026-06-29 for the lattice, adjacency and proper cubic rotations; no further structure used

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

For the two-cell one-tick box {0,1,2}x{0,1}x{0,1}x{0,1} (24 corners, 17280 minimal pieces in 1080 orbits of size 16, 48-piece dissections), the spatial adjacency cost of a dissection lies in [216, 320] with both ends attained: the floor by an integer certificate of value 110144 at denominator 512 (least slack zero on all 1080 orbits and all 17280 pieces, tight on 30) attained by the stacked monotone stencil, and the ceiling by a certificate of value 15728 at denominator 49 (tight on 53) attained by an exhibited 48-piece dissection. The cost-320 maximiser has sixteen facets carried by a single piece away from the box boundary, so it is not face-to-face and no lift produces it — which explains why the previous cycle's lift-based hill climb stopped at 318.

Original verdict: The cost interval is 216 to 320 with both ends reached, and the maximiser lies outside the reach of lift-based construction by a structural obstruction rather than by search failure.
Scope: Pinned for this box and this charge only; nothing is said about how the interval scales; both certificates are supplied integer data verified rather than searched for, and no claim is made that 512 and 49 are minimal denominators; the charge convention (corner pairs separated by more than one lattice step) and the minimal-piece convention are named as choices not forced by the lattice.
Escape conditions (negative claims): Non-regularity is proved for THIS maximiser, not for maximisers as a class — whether every cost-maximising dissection of every such box is non-liftable is explicitly open. The lift obstruction is specific to face-to-face lower hulls.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Two-cell one-tick cost interval [216,320] both ends attained; maximiser provably non-regular (outside lift-based certificates); corrects predecessor upward twice — the block-level terminal of the dissection program.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_BLOCK_COST_INTERVAL_LIFT_OBSTRUCTION_CYCLE729_NOTE_2026-08-04.md`
- Source commit: `8ca899138d7a5c1370e02cfe30660073b0db6103`
- git blob: `d0933e09b6b7015d810b9894223e21f1ef8dcc88`
- sha256: `340aa16ee7eac96b4d67c13431e51b55ca67310bf1e033af675a29f6e0089f5d`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3095_PHYSICAL_BLOCK_COST_INTERVAL_LIFT_OBSTRUCTION_CYCLE729_NOTE_2026-08-04.md](../../archive_unlanded/historic_intake_originals/recovery/3095_PHYSICAL_BLOCK_COST_INTERVAL_LIFT_OBSTRUCTION_CYCLE729_NOTE_2026-08-04.md)
- Lines: 216; runners named: historic runner (unpinned, not in this packet): `scripts/physical_block_cost_interval_lift_obstruction_cycle729_2026_08_04(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` — Superseded: witness corrected 318->320 and its certificate-shape reading refuted by 3095.

## Flags carried

Three carve-outs named in place: certificate weights/constants/denominators are supplied to the runner rather than derived by it; cross-check counts come from probes not part of the landed artifact; and the values 324 and 256 are quoted from the previous cycle's record, not measured here.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
