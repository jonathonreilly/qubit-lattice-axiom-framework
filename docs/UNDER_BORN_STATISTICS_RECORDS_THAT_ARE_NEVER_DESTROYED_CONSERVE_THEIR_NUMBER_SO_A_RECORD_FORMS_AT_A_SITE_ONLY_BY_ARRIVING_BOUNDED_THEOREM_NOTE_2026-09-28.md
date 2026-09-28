---
claim_id: under_born_statistics_records_that_are_never_destroyed_conserve_their_number_so_a_record_forms_at_a_site_only_by_arriving_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Finite lattice; records are the beables of a supplied equivariant law (any stochastic law whose configuration distribution is |psi_t|^2 at every time, psi evolving by a Hermitian H; Bell's minimal jump law is one). (T1) If records are never destroyed, for every initial psi, then H commutes with the record number N (proof: permanence makes P(N >= n) non-decreasing for every state; its derivative is <i[H, Pi_{N>=n}]>, a traceless Hermitian operator, which is then positive semidefinite with zero trace, hence zero). (T2) For one state over all time: its Born count distribution is almost periodic, so if non-decreasing it is constant. (T3) Conversely, if [H, N] = 0, Bell's law never changes N, and a site gains a record only by an arrival along a nonzero matrix element of H (from a neighbour for a nearest-neighbour H). Illustrations on a ring of 8 hard-core sites: with a local formation term, records formed from nothing are destroyed again (P(N >= 1) falls at t ~ 1.5; late creation/destruction flux ratio 1.20). No infinite systems, no content, no apparatus-level (macroscopic) records."
upstream_dependencies:
  - minimal_axioms
  - records_as_beables_under_the_moving_records_reading_bells_jump_law_gives_nearest_neighbour_moves_equivariant_odds_and_bell_correlations_with_nonlocal_odds_bounded_theorem_note_2026-09-27
runner: scripts/under_born_statistics_permanent_records_conserve_their_number_2026_09_28.py
---

# Under Born statistics, records that are never destroyed conserve their number, so a record forms at a site only by arriving

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a short exact proof and small-lattice illustrations; a supplied
reading; unaudited. Independent checks are recorded below.

## In one paragraph

Suppose records are real things whose odds come from a quantum wave (the
beables reading of the records-as-beables note). The wave's statistics say
how many records there are. Records are permanent. Can new records then
appear? Not from nothing.

- If the wave allows the count of records to change, some state has its
  count going down. The records in that state must then disappear, so they
  would not be permanent.
- So permanent records under Born statistics keep a fixed number. A site
  gains a record only when one arrives from a neighbour.
- In that reading, "a record forms here" means "a record moved in".

## Why this question

The viability map's first decision is what a record is. Option C (records as
beables) fits the owner's moving-records reading: records persist, and move
between neighbouring sites. The owner's reading also has records forming at
empty sites, with the count growing over time. This note asks whether option
C can carry both "formation" and "permanence" once the records keep the
wave's statistics.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Records form; a site
  carries at most one record; records are permanent.
- **The owner's reading** (2026-09-20, not axiom text).
  - Records move between neighbouring sites.
  - An empty site can form one by the rule.
  - Only one record is at a site at a time.
- **Supplied, not adopted: the beables reading.**
  - A wave `psi` over record configurations evolves by a Hermitian `H`
    (finite lattice, finite dimension).
  - The actual configuration follows any stochastic law that is
    *equivariant*: its distribution equals `|psi_t|^2` at every time.
  - Bell's minimal jump law is one example. The theorem does not depend on
    which law is used.
- **Record number** `N`: the number of occupied sites. `Pi_{N>=n}` is the
  projector onto configurations with at least `n` records.

## T1 — never destroyed, for every state, forces a conserved number

*Statement.* If, for every initial `psi`, no record is ever destroyed along
any trajectory, then `[H, N] = 0`.

*Proof.*
1. If records are never destroyed, the actual count never decreases. So
   `P_t(N >= n)` is non-decreasing in `t`, for every `n`.
2. By equivariance, `P_t(N >= n) = <psi_t|Pi_{N>=n}|psi_t>`. Its derivative
   at `t = 0` is `<psi|X_n|psi>`, with `X_n = i[H, Pi_{N>=n}]`, a Hermitian
   operator. This holds for every `psi`, so `X_n` is positive semidefinite.
3. `X_n` is a commutator, so `tr X_n = 0`. A positive semidefinite operator
   with zero trace is zero. So `[H, Pi_{N>=n}] = 0` for every `n`, hence
   `[H, N] = 0`. ∎

*Check (runner A).* With hopping and a local formation term, `X_n` is
traceless with eigenvalues `±1.13`, `±1.50` and `±1.79` for `n = 1, 2, 4`.
Its most negative eigenvector loses records at those rates at once.

## T2 — one state over all time

For a single state on a finite lattice, `f(t) = <psi_t|Pi|psi_t>` is a
finite sum of oscillating exponentials, so it is almost periodic.

A non-decreasing almost-periodic function is constant.
- Suppose `f(t_2) > f(t_1)`.
- Almost periodicity gives arbitrarily large `τ` with `f(t_1 + τ)` within
  `δ` of `f(t_1)`.
- Monotonicity gives `f(t_1 + τ) >= f(t_2)`.
- These contradict each other for small `δ`.

So if a state's records are never destroyed, its Born count distribution
never changes.

## T3 — conversely, conserved number means formation is arrival

If `[H, N] = 0`, then `H` connects only configurations with the same count.
Bell's law jumps only along nonzero matrix elements of `H`, so it never
changes `N`: records are permanent. A site gains a record only in a jump
that moves one there. With nearest-neighbour hopping, that record comes from
a neighbour.

*Checks.*
- Runner B: number-conserving random hopping; the largest current between
  different counts is `0`, and the count distribution drifts by `2e-15`.
- Runner D: a Bell trajectory with 44 gains, every one an arrival from a
  neighbour that lost its record in the same jump.

## Illustration — records formed from nothing are destroyed again

Hard-core records on a ring of 8 sites, with hopping (`1`) and a local
formation term (`0.4 σ^x` at each site), starting with no records:
- the mean count rises: `0.89`, `1.42` and `1.67` at `t = 1, 2, 4`;
- `P(N >= 1)` first falls at `t = 1.5`;
- at late times (`t` from 30 to 60), Bell's destruction flux is comparable
  to its creation flux (ratio `1.20`).

Any equivariant law must destroy records here. A Hermitian formation term
also unforms.

## What this means for the axioms

Under option C, with the records keeping Born statistics:
- **"Records are permanent" and "records form" hold together exactly when
  formation means arrival.**
  - The number of records is fixed. A record forms at a site by moving in.
  - This matches the owner's moving-records reading of motion and
    exclusion.
  - It does not match "an empty site forms a new record, and the count
    grows".
- **A growing count** would need one of the following:
  - a count whose statistics are not the wave's, so Born statistics fail
    for the number of records;
  - permanence that holds only statistically, in large systems prepared in
    special states. The illustration shows destruction as frequent as
    creation once the system settles.
  - reading "record" at the level of apparatus-sized patterns, which can
    form irreversibly in the usual thermodynamic sense while the elementary
    records only move.
- **A conserved number of records under one-per-site exclusion is a
  hard-core lattice gas: interacting matter.** That connects to two other
  results:
  - the campaign's books, exact for free walkers and lost once records
    scatter (blocks 137 and 143);
  - the shape-dependence note of the same campaign, where interactions bring
    back the vacuum's sensitivity to the metric's shape.

## What this does not show

- **Size.** Finite lattices only. In infinite systems, special initial
  states can grow their count for long times. How long, and at what
  destruction rate, is not computed.
- **Content.** Content (the `M_2(C)` possibility a record locks) is not
  modelled.
- **Uniqueness.** Bell's law is one equivariant law. The theorem covers them
  all, but only under equivariance for the count.
- **Scale.** Macroscopic records (patterns of many elementary records) are
  not treated.

## Independent checks

Pending: a Claude Fable 5.1 subagent from its own code, and a codex
`gpt-5.6-sol` referee.

## Reproduction

```bash
python3 scripts/under_born_statistics_permanent_records_conserve_their_number_2026_09_28.py
```

Expected: `TOTAL: PASS=4 FAIL=0` (a few seconds).
