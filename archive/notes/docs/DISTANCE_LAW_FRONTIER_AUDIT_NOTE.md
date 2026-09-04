# Distance Law Frontier Audit

**Date:** 2026-04-05 (status line rephrased 2026-04-28 per audit-lane verdict)
**Type:** meta
**Status authority:** independent audit lane only.
**Status:** metadata/support index over cited retained-bounded distance-law inputs; no runner registered; not a tier-ratifiable summary on its own.

## 2026-05-28 Audit Repair (reframed as metadata/support index)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The cited distance-law inputs are now retained_bounded, so the summary direction is plausible as metadata. The source itself remains support-level, contains stale unaudited-input status wording, and has no registered runner or explicit rank"*

with repair: *"runner_artifact_issue: if a retained frontier summary is desired, update the stale support note and register a runner or explicit artifact that reproduces the frontier-ranking criteria over the retained bounded distance-law inputs."*.

The auditor's repair allows reframing this row as metadata/support rather than a
retained theorem. This revision takes that path:

- This note is a **metadata / support index** over the cited retained-bounded
  inputs. Its summary direction / frontier-ranking / synthesis rows are
  **non-load-bearing pointers**, not an independently certified result.
- It does **not** register a runner-backed retained theorem. Any stale
  "proposed retained" / "unaudited-input" status wording is superseded by this
  metadata framing; authoritative status for each cited input lives in that
  input's own retained row.

No new axiom, import, or retained bridge is introduced. The note is a pointer
surface; nothing here is load-bearing beyond the cited inputs' own authorities.

## Question

What is the smallest honest distance-law claim now retained on `main`, after
the later independent wide-lattice replay?

This audit originally compared:

- the retained compact grown-geometry `h = 0.25` tail transfer already on
  `main`
- the branch-side wide-lattice `h^2+T` continuation as a reference only

## Earlier mainline evidence

The retained mainline distance-law companions already say:

- [`docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
- [`docs/GATE_B_H025_DISTANCE_LAW_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/GATE_B_H025_DISTANCE_LAW_NOTE.md)

Frozen compact-family readout:

- exact grid: `20/20` TOWARD, tail `b^(-0.90)`, `R^2 = 0.855`
- grown `drift = 0.2`: `20/20` TOWARD, tail `b^(-0.83)`, `R^2 = 0.884`

Frozen finer-spacing replay:

- exact grid: `10/10` TOWARD, tail `b^(-0.42)`, `R^2 = 0.855`
- grown `drift = 0.2`: `10/10` TOWARD, tail `b^(-0.54)`, `R^2 = 0.948`

Safe read from the retained family:

- the distance-law tail transfers to the retained grown geometry
- the `h = 0.25` replay remains positive and declining
- this is a bounded refinement companion, not a full continuum theorem

## Status update
The later independent replay has now landed on `main`:

- [`docs/WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md)

That means the frontier has moved.

The safe current stack is now:

- compact grown-geometry distance-law transfer remains retained
- wide-lattice ordered `h^2+T` far-tail replay is also retained
- neither result is yet a full continuum theorem

## Final Verdict

The compact grown-geometry far-field tail transfer is still a retained
frontier result.

But it is no longer the whole frontier by itself.

The independently replayed wide-lattice `h^2+T` far-tail result is now also
retained on `main`.

So the honest current frontier is:

- compact grown-geometry transfer
- plus wide-lattice ordered `h^2+T` far-tail replay

## What This Means

The right near-term move is still not to broaden into a full continuum theory.
It is to keep both retained frontier pieces in view and only promote the
distance-law lane further if a stronger asymptotic statement earns its own
artifact chain on `main`.

## Audit boundary (2026-04-28)

Audit verdict (`audited_conditional`, leaf criticality):

> Issue: the note claims the compact grown-geometry and wide-lattice
> distance-law pieces are the retained current frontier, but it
> provides no runner and depends entirely on three unaudited
> proposed-retained source notes. Why this blocks: an audit-lane
> retained summary cannot outrank its inputs; until the cited
> distance-law notes are audited clean, this note can only summarize
> proposed frontier candidates.

The note has been re-tiered to `support`.

## What this note does NOT claim

- A tier-ratifiable retained-frontier summary.
- That the cited Gate B grown, Gate B `h = 0.25`, and wide-lattice
  `h^2 + T` notes are audit-clean dependencies.
- A registered runner output for the summary.

## What would close this lane (Path A future work)

A retained frontier summary would require auditing the three cited
upstream distance-law notes to clean status, and registering a
runner that reproduces the frontier-ranking criteria.
