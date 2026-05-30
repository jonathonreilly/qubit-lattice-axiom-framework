# Family Companion Compare Note

**Date:** 2026-04-06 (status line rephrased 2026-04-28 per audit-lane verdict)
**Claim type:** meta
**Status:** support / cross-family comparison card pointing to other notes for the fixed-companion weak-field law; static summary only, no audit-registered dependency chain, no runner that recomputes controls and `F~M` values.

## Artifact Chain

- [`scripts/FAMILY_COMPANION_COMPARE.py`](/Users/jonreilly/Projects/Physics/scripts/FAMILY_COMPANION_COMPARE.py)
- [`logs/2026-04-06-family-companion-compare.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-06-family-companion-compare.txt)
- retained source notes:
  - [`archive_unlanded/grown-transfer-stale-runners-2026-04-30/GROWN_TRANSFER_BASIN_NOTE.md`](/Users/jonreilly/Projects/Physics/archive_unlanded/grown-transfer-stale-runners-2026-04-30/GROWN_TRANSFER_BASIN_NOTE.md)
  - [`docs/ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md)
  - [`docs/SECOND_GROWN_FAMILY_COMPLEX_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/SECOND_GROWN_FAMILY_COMPLEX_NOTE.md)

## Question

Do the retained grown-family, alternative connectivity family, and second-family slices share the same fixed-companion weak-field law at a review-safe level?

## Comparison (declared observable surface)

The retained, alternative-connectivity, and second-family slices each
discuss a fixed-companion weak-field law on their own observable surface
(signed-source for the first two; `gamma = 0` baseline plus crossover for
the second-family complex anchor). The cross-family `F~M` values and the
zero/neutral controls are sourced from notes whose upstream authority is
not registered in the audit graph, and the present runner only renders
summary rows. Those rows have therefore been narrowed out of this
meta-comparison (see the 2026-05-18 repair section below); the
remaining cross-family discussion is restricted to qualitative
surface-shape observations.

## Safe Read

- each cited family discusses a fixed-companion weak-field law on its own
  declared observable surface, but the cross-family numeric `F~M` values
  and zero/neutral controls require a registered upstream authority and a
  runner that recomputes them — neither is in place at this note
- the sign-law slices (retained grown-transfer basin and alternative
  connectivity family) declare the same signed-source observable surface
  in their own notes; this meta-card no longer asserts the numeric
  cancellation result on their behalf
- the second-family complex anchor declares a different comparison
  surface (`gamma = 0` baseline plus crossover) in its own note; this
  meta-card no longer asserts the numeric `F~M` value on its behalf

## Surface-shape mismatch (qualitative)

- the sign-law families declare a zero/neutral signed-source observable
  surface in their own notes
- the second-family complex lane declares a `gamma = 0` baseline plus
  crossover surface in its own note
- as a meta-observation, those declared surfaces are not the same; any
  shared weak-field statement across these families would have to
  recompute on a common surface in a registered runner

## Final Verdict

**support-tier meta-comparison only: declared observable surfaces noted per family; cross-family numeric `F~M` and zero/neutral control claims have been narrowed out pending a registered upstream authority and a recomputation runner**

## Audit boundary (2026-04-28)

Audit verdict (`audited_conditional`, leaf criticality):

> Issue: the retained cross-family comparison rests on a static
> summary of source notes, not on an audit-registered dependency
> chain or a runner that recomputes the controls and F~M values.
> Why this blocks: a hostile referee cannot accept a retained
> shared-law claim while two cited families are still unaudited
> proposed_retained and the second-family complex branch is
> compared by gamma=0/crossover rather than the same zero/neutral
> signed-source observable.

The note has been re-tiered to `support` (cross-family comparison
card).

## What this note does NOT claim

- A retained shared-law theorem.
- That the cited families are audit-clean dependencies.
- That the second-family complex branch was compared on the same
  zero/neutral signed-source observable.

## What would close this lane (Path A future work)

A retained shared-law theorem would require auditing or registering
the cited grown-transfer / second-family / connected-family
authorities, plus a runner that recomputes controls and `F~M`
values on the same signed-source observable.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links for
the in-docs family-card authorities so the audit citation graph can
track them. It does not promote this note or change the audited
claim scope.

- [ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md](ALT_CONNECTIVITY_FAMILY_BASIN_NOTE.md) — alternative-connectivity family basin row supplying `F~M = 0.999994` on the full tested drift sweep.
- [SECOND_GROWN_FAMILY_COMPLEX_NOTE.md](SECOND_GROWN_FAMILY_COMPLEX_NOTE.md) — second-family complex anchor row supplying `F~M = 1.000` on the `gamma = 0` baseline.
- [ALT_CONNECTIVITY_FAMILY_FM_TRANSFER_NOTE.md](ALT_CONNECTIVITY_FAMILY_FM_TRANSFER_NOTE.md) — alt-family `F~M` transfer evaluation supplying the precise `0.999994` weak-field linearity value on the alt-connectivity slice. The original grown-transfer basin authority is currently archived under `archive_unlanded/grown-transfer-stale-runners-2026-04-30/`, so it is not wired as an in-`docs/` one-hop edge here.

## 2026-05-18 audit-conditional repair: narrowed to declared observable surface

Per the 2026-05-17 audit verdict, the grown-transfer basin authority is
not registered, and the runner only renders summary rows rather than
recomputing controls or F~M values. This revision narrows the meta-comparison
to the declared observable surface — removing the grown-row F~M=1.000 and
zero/neutral control rows. Those are queued as out-of-scope follow-ups
awaiting (a) registration of the grown-transfer basin authority and
(b) a recomputation runner on the same observable surface.

Concretely narrowed out of this note (still discussed in the cited source
notes, which carry their own audit verdicts):

- the retained grown-transfer basin row asserting `F~M = 1.000` on
  signed-source with exact zero/neutral cancellation
- the alternative-connectivity row asserting the precise `0.999994`
  weak-field value with exact zero/neutral cancellation
- the second-family complex anchor row asserting `F~M = 1.000` on the
  `gamma = 0` baseline plus crossover surface
- the "Exact Mismatch" cross-surface conclusion that depended on those
  three rows being recomputed at this meta-card

What is retained at this meta-card: the declared observable surface for
each family (signed-source vs `gamma = 0`-plus-crossover) and the
qualitative observation that those surfaces are not the same. No numeric
`F~M` value and no zero/neutral control claim is carried at this note
until both (a) the grown-transfer basin authority is audit-registered
and (b) a runner recomputes the controls and `F~M` values on a common
declared observable surface.
