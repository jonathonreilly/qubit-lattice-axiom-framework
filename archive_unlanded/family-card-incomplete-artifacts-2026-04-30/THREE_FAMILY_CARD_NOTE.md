# Historical Three-Family Card Packet (Retracted)

**Date:** 2026-04-06
**Status:** RETRACTED 2026-04-30 — audit failed; this note is archived under `archive_unlanded/family-card-incomplete-artifacts-2026-04-30/`. Claims below are NOT supported by current runners or current audit lane. See `## Retraction` section.

## Current-surface certificate (2026-06-12 source firewall)

**Actual current-surface status:** archived `audited_failed` / retracted
historical artifact. This file is kept only as audit history for a failed
or inconsistent route. It may not be cited as retained, bounded, conditional,
supporting, or methodological authority for any live framework chain.

## Retraction

- **Date archived:** 2026-04-30
- **Archive directory:** `archive_unlanded/family-card-incomplete-artifacts-2026-04-30/` (the directory name encodes the failure reason: incomplete artifacts behind the family-card claim).
- **Audit verdict_rationale (quoted verbatim from `docs/audit/data/audit_ledger.json`):**

  > Issue: The note claims three families match on all 9 measurable properties, but the table explicitly has Family 3 Distance alpha marked '(not yet)' and the note provides no runner or log artifact to verify the cross-family card. Why this blocks: the load-bearing 9/9 statement is false on the face of the supplied table, and the broader inference that observables are geometry-independent cannot follow from a partial, hand-entered comparison. Repair target: add a runner that recomputes every listed property for all three families, including Family 3 Distance alpha, with explicit <5% assertions and at least one holdout check. Claim boundary until fixed: safe to cite this as a partial comparison of three selected drift/restore rows with eight populated properties and distance-alpha data only for Families 1 and 2; not safe to claim 9/9 three-family equality or geometry-independence.

- **Do not cite warning:** Do NOT cite the numerical results, tables, or threshold values in the original content below as live framework claims. The runners referenced in this note have been superseded or are no longer reproducible at the time of audit. If a future investigation revisits this physics, treat it as starting from scratch rather than as continuation of a "closed no-go".

## 2026-06-16 archive firewall

This archived packet is historical / diagnostic and retired as evidence. The
old title and body claimed a 9/9 three-family match, but the supplied table
itself leaves Family 3 distance alpha uncomputed. This note is not a live
authority for geometry-independence, cross-family equality, or a retained
three-family card.

The only safe residue is the audit boundary already stated above: this is a
partial comparison of three selected drift/restore rows with eight populated
properties and distance-alpha data only for Families 1 and 2.

## Historical sampled families (retracted)

| Family | drift | restore | Distance from center |
| --- | ---: | ---: | --- |
| 1 (center) | 0.20 | 0.70 | — |
| 2 | 0.05 | 0.30 | far (low both) |
| 3 | 0.50 | 0.90 | far (high both) |

## Historical cross-family comparison (partial and retracted)

| Property | Fam 1 | Fam 2 | Fam 3 | Max diff |
| --- | ---: | ---: | ---: | ---: |
| F~M (6 seeds) | 0.990 | 0.993 | 0.994 | 0.4% |
| Born | 0.00e+00 | 0.00e+00 | 1.7e-15 | 0 |
| Gravity TOWARD | 3/3 | 3/3 | 3/3 | 0 |
| MI (bits) | 0.545 | 0.521 | 0.546 | 4.6% |
| d_TV | 0.787 | 0.771 | 0.781 | 2.1% |
| Escape (gamma=0) | 1.027 | 1.028 | 1.028 | 0.1% |
| cx crossover | 3/3→0/3 | 3/3→0/3 | 3/3→0/3 | 0 |
| cx_escape (gamma=0.5) | 0.965 | 0.965 | 0.965 | 0% |
| Distance alpha | -0.962 | -0.947 | (not yet) | 1.6% |

## Historical claim boundary (retracted and narrowed)

The old claim boundary asserted that three independent grown families spanning
the drift/restore range produced quantitatively identical physics on all nine
listed properties. That assertion is retracted because Family 3 distance alpha
is not populated and no runner/log artifact verifies the card.

This packet is not evidence that the physics emerges independently of the
specific geometry. It is only a historical partial table.

Any future repair must recompute every listed property for all three families,
including Family 3 distance alpha, with explicit threshold assertions and a
holdout check before reopening any equality or geometry-independence claim.

## 2026-06-18 live missing-distance bridge

[`docs/THREE_FAMILY_CARD_MISSING_DISTANCE_LIVE_BRIDGE_NOTE_2026-06-18.md`](../../docs/THREE_FAMILY_CARD_MISSING_DISTANCE_LIVE_BRIDGE_NOTE_2026-06-18.md)
packages the current live evidence for the specific missing Family 3 distance
alpha slot. It does not restore the historical 9/9 card, does not claim
geometry independence, and does not provide the all-nine-property recomputation
required for a full card repair.
