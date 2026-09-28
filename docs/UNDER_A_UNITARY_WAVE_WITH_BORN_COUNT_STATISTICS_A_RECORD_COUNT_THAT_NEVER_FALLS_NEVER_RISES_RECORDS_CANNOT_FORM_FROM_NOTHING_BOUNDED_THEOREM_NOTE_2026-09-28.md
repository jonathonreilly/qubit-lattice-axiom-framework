---
claim_id: under_a_unitary_wave_with_born_count_statistics_a_record_count_that_never_falls_never_rises_records_cannot_form_from_nothing_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied reading (records as beables, option C of the viability map), not adopted. A wave psi over record configurations of a finite lattice evolves by a fixed, time-independent Hermitian H; the record count N of the actual configuration has, at every time, the Born distribution of psi_t (count equivariance; Bell's minimal law is one example). (T1) If the count never falls (almost surely), for every initial psi, or just from every initial configuration, then [H, N] = 0, so it never rises either: records cannot form from nothing. Proofs: <i[H, Pi_{N>=n}]> >= 0 for every psi with zero trace forces the commutator to vanish; or, from a configuration c, P_t(N < N(c)) = t^2 ||(1 - Pi) H c||^2 + O(t^3), so H has no count-lowering elements, hence (Hermitian) no count-raising ones. (T2) For one state and a fixed finite H: a non-decreasing almost-periodic count distribution is constant. (T3) Conversely, [H, N] = 0 makes Bell's minimal law count-preserving; if every off-diagonal term of H is a single nearest-neighbour hop, each gain of a record at a site is paired with a neighbour's loss in the same jump. Reading that as the same record arriving needs a record identity, which the owner's moving-records reading supplies and this model does not. Illustration on a ring of 8 hard-core sites with a local formation term: count-lowering jumps are unavoidable (all 300 Bell trajectories destroy a record by t = 30). A statement about option C with a unitary wave, not about the axioms."
upstream_dependencies:
  - minimal_axioms
  - records_as_beables_under_the_moving_records_reading_bells_jump_law_gives_nearest_neighbour_moves_equivariant_odds_and_bell_correlations_with_nonlocal_odds_bounded_theorem_note_2026-09-27
runner: scripts/under_a_unitary_wave_a_record_count_that_never_falls_never_rises_2026_09_28.py
---

# Under a unitary wave with Born count statistics, a record count that never falls never rises: records cannot form from nothing

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** short exact proofs and small-lattice illustrations; a supplied
reading; unaudited. Independent checks are recorded below.

## In one paragraph

Suppose records are real things whose statistics come from a quantum wave:
option C of the viability map, records as beables. Suppose the number of
records keeps the wave's statistics, and the wave evolves in the ordinary
reversible (unitary) way. Then a count that never goes down also never goes
up.

- If the wave could raise the count anywhere, it could lower it somewhere,
  because a reversible rule that creates also uncreates.
- So under option C with a unitary wave, records cannot form from nothing.
- A site can still gain a record when a neighbour loses one. Under the
  owner's reading, which gives records an identity, that is a record moving
  in.
- A count that grows needs something else. The best-known candidate is a
  non-unitary rule, as in collapse ("flash") theories.

## Why this question

The viability map's first decision is what a record is. Option C (records as
beables) fits the owner's moving-records reading:
- records persist;
- they move between neighbouring sites;
- only one is at a site at a time.

That reading also has records forming at empty sites, with the count growing
over time. This note asks what option C allows for the count, once the count
keeps the wave's statistics.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): records form; a site
  carries at most one record; records are permanent. The memo supplies no
  Hamiltonian, Born rule, beable identification, time or formation law.
  Everything below is supplied.
- **The owner's reading** (2026-09-20, not axiom text): records move between
  neighbouring sites; an empty site can form one by the rule; one record per
  site at a time.
- **Supplied, not adopted:**
  - a finite lattice;
  - a wave `psi` over record configurations, evolving by a fixed,
    time-independent Hermitian `H`;
  - an actual configuration whose record count `N` has, at every time, the
    Born distribution `P_t(N = m) = <psi_t|Pi_{N=m}|psi_t>` (count
    equivariance). Bell's minimal jump law is one example; the theorem needs
    only the count.
- **"Destroyed"** here means the total count decreases. The model has no
  record identities, so the destruction of one record paired with the
  creation of another is not distinguished from a move.

## T1 — a count that never falls, for every state, never rises

*Statement.* Suppose the count never falls (almost surely), for every
initial `psi`. Then `[H, N] = 0`, so the count never rises either.

*Proof 1 (every state).*
1. A count that never falls makes `P_t(N >= n)` non-decreasing for every `n`.
2. Its derivative at `t = 0` is `<psi|X_n|psi>`, with the Hermitian operator
   `X_n = i[H, Pi_{N>=n}]`. This is non-negative for every `psi`, so `X_n`
   is positive semidefinite.
3. `X_n` is a commutator, so `tr X_n = 0` in finite dimension. So `X_n = 0`,
   and `N = sum_n Pi_{N>=n}` commutes with `H`. ∎

*Proof 2 (every configuration; due to the Fable check).*
- Start from a single configuration `c`. Then
  `P_t(N < N(c)) = t^2 ||(1 − Pi) H c||^2 + O(t^3)`, with `Pi` the projector
  onto count `>= N(c)`.
- This is positive if `H` has any element lowering the count from `c`. So a
  count that never falls from any configuration forces `H` to have no
  count-lowering elements.
- `H` is Hermitian, so it then has no count-raising elements either. ∎
- This form needs neither the trace nor finite dimension. It is a statement
  about matrix elements of `H`, and holds for a local `H` on an infinite
  lattice.
- It uses only the configurations: the axioms' "state" is a configuration of
  records.

*Checks (runner A).*
- `X_n` is traceless with eigenvalues `±1.13`, `±1.50` and `±1.79` for
  `n = 1, 2, 4`.
- From configurations with 2, 3 and 8 records, the short-time coefficient is
  `0.32`, `0.48` and `1.28`, matching direct evolution.

## T2 — one state over all time

For a single state, a fixed finite `H` makes
`f(t) = <psi_t|Pi|psi_t>` a finite sum of oscillating exponentials, so it is
almost periodic.

A non-decreasing almost-periodic function is constant.
- Suppose `f(t_2) > f(t_1)`.
- There are almost-periods `τ > t_2 − t_1` with `f(t_1 + τ)` within `δ` of
  `f(t_1)`.
- Monotonicity gives `f(t_1 + τ) >= f(t_2)`, a contradiction for small `δ`.

So for one state, a count that never falls has a constant Born distribution.
Then, since a count that never falls has a constant mean, it never changes
on almost every trajectory: never falling already means never rising.

This constrains one orbit, not `H`. It uses recurrence (reference:
Bocchieri and Loinger 1957), which fails for time-dependent or
infinite-volume dynamics.

## T3 — the converse, and what "arrival" needs

- If `[H, N] = 0`, `H` connects only configurations with equal counts.
  Bell's minimal law jumps only along nonzero elements of `H`, so it never
  changes the count.
- This is law-specific. Other equivariant laws could add balanced
  cross-count traffic.
- If every off-diagonal term of `H` is a single nearest-neighbour hop, each
  jump that fills a site empties a neighbour.
- Calling that "the same record arriving" needs a record identity. The
  owner's moving-records reading supplies one; this model does not.
- A count-conserving `H` also allows frozen dynamics, in which nothing moves
  or forms.

*Checks.*
- Runner B: number-conserving random hopping. The largest current between
  different counts is `0`, and the count distribution drifts by `2e-15`.
- Runner D: a Bell trajectory with 44 gains, each paired with a neighbour's
  loss in the same jump.

## Illustration — formation from nothing is followed by destruction

Hard-core records on a ring of 8 sites, with hopping `1` and a local
formation term `0.4 σ^x` at each site, starting with no records:
- the mean count rises: `0.89`, `1.42` and `1.67` at `t = 1, 2, 4`;
- `P(N >= 1)` first falls at `t = 1.5`;
- over `t` in `[30, 60]`, Bell's mean creation and destruction fluxes are
  `0.49` and `0.41` per unit time. The finite system never settles, so their
  ratio depends on the window.
- In a Bell Monte Carlo, 59 % of trajectories destroy a record by `t = 4`,
  and all 300 do by `t = 30`.

A Hermitian formation term also removes records.

## What this means for option C (not for the axioms)

With a unitary wave, count equivariance, and a count that never falls:
- **Records cannot form from nothing.** The count is fixed.
- **Under the owner's moving-records reading**, a site gains a record when a
  neighbour loses one. The reading's record identity makes that an
  arrival.
- **A growing count needs one of the following:**
  1. **A non-unitary rule.** Examples: a quantum-jump dynamics with
     creation-only jumps, or a collapse theory whose "flashes" are permanent
     events that only accumulate (Bell 1987; Tumulka 2006; reference only).
     This is the best-developed option. It pays the record cost that option
     C avoids.
  2. **Count statistics that are not the wave's.** Admissibility assigns the
     wave's distribution to a record's content, not to whether a record
     forms, so Born statistics for the count is a supplied extra.
  3. **Permanence that holds only statistically**, in infinite systems
     prepared in special states. This is not computed here.
  4. **A different beable for "record"**: a history register, or
     apparatus-sized patterns of many elementary records, which can form
     irreversibly in the usual thermodynamic sense.
  5. **Time-dependent driving.** Proof 1 holds at each instant, so driving
     does not help T1. It does undo T2.
- **Prior art (reference only).** Bell (1986) and Dürr, Goldstein, Tumulka
  and Zanghì (2003–2005) built Bell-type quantum field theories with
  equivariant creation and annihilation jumps. They keep Born statistics and
  give up strict permanence, the trade-off shown here. Vink (1993) treats
  the non-uniqueness of the rates.
- **One consequence for the rest of the campaign.** A fixed number of
  records under one-per-site exclusion is a hard-core lattice gas, i.e.
  interacting matter. That ties this option to two other results:
  - the books' loss when records scatter (blocks 137 and 143);
  - the shape-dependence note, where interactions bring back the vacuum's
    sensitivity to the metric's shape.

## What this does not show

- **Identities.** There are no record identities or contents, and no
  worldlines. "Permanent" is tested only through the total count.
- **Infinite systems.** T1's configuration form holds for local `H`. T2 and
  the illustration do not carry over.
- **The axioms.** No statement about the axioms themselves. They supply
  none of the premises above.

## Independent checks

- **Codex `gpt-5.6-sol` referee**, at xhigh. Another vendor family; it read
  only the axioms memo and this note's first version.
  - **Verdict: "fails".**
  - The finite-dimensional results stand, and its independent numbers
    reproduce the note's.
  - The inference did not:
    - conserving the count is not permanence of individual records;
    - "formation is arrival" needs an identity matching;
    - the converse is specific to Bell's law;
    - the conclusion was stated against the axioms, not against the model;
    - missed options (driving, open dynamics, infinite systems, history
      beables) and prior art (Dürr, Goldstein, Tumulka and Zanghì 2005).
  - **Applied:**
    - retitled and re-scoped to the count and to option C with a unitary
      wave;
    - "destroyed" defined as a fall in the count;
    - the arrival reading made conditional on the owner's identity;
    - the converse stated as specific to Bell's law;
    - the options and prior art added.
- **Claude Fable 5.1 subagent**, working from its own code (same vendor
  family, so not a referee).
  - **Verdict: "confirmed with corrections".**
  - Every number reproduced by ODE integration and a 4000-trajectory Bell
    Monte Carlo.
  - **Applied:**
    - the configuration form of T1 (Proof 2), which needs no trace or
      finite dimension;
    - the window dependence of the flux ratio, replaced by mean fluxes and
      trajectory statistics;
    - the non-unitary option named first;
    - the trajectory corollary of T2;
    - prior art.
- A second round is pending.

## Reproduction

```bash
python3 scripts/under_a_unitary_wave_a_record_count_that_never_falls_never_rises_2026_09_28.py
```

Expected: `TOTAL: PASS=4 FAIL=0` (under a minute).
