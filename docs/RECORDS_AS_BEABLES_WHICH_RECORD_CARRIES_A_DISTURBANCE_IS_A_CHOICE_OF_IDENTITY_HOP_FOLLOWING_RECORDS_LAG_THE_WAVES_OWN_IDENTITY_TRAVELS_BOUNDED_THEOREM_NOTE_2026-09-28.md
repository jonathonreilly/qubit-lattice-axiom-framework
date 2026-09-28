---
claim_id: records_as_beables_which_record_carries_a_disturbance_is_a_choice_of_identity_hop_following_records_lag_the_waves_own_identity_travels_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied reading, not adopted: records as beables (Bell's minimal jump law) on a one-mode-per-site free-fermion sea (the axioms' qubit read as one fermion mode), antiperiodic closed shells; one particle added at the origin. Bell's law moves unlabelled occupations; a record's identity is an extra rule. Two rules on the same trajectories: hop-following (the record that jumps keeps its identity) and the wave's own Laplace identity (occupation i carries the added particle with weight |A_i0 (A^-1)_0i|^2, a per-time assignment; no nearest-neighbour process realising it is built). (T1) Method validated against full Fock-space evolution. (T2) Hop-following, 1D: the tagged record stays within about 1/(2 nu) sites (about one at half filling) while the excess density spreads ballistically; ratio of RMS displacements at t = L/4 (before the first wrap) 0.20, 0.10, 0.05 on rings of 16, 32, 64. (T3) Hop-following, 2D before wrapping: ratios fall with time, to 0.24 on 12x12 at t = 3 and 0.20 on 16x16 at t = 4. (T4) Laplace identity on the same trajectories: ratio 1.02 (ring 32) and 1.04 (12x12) at the latest time (0.7-0.8 at early times, where the excess includes the sea's static correlation hole). (T5) Dilute ring (nu = 1/8): hop-following carries about 3.8 sites, ratio 0.16 at t = 16 against 0.05 at half filling. Free hopping only; one equivariant law; no interactions; no 3D (an independent check reports 3D behaves like 2D)."
upstream_dependencies:
  - minimal_axioms
  - records_as_beables_under_the_moving_records_reading_bells_jump_law_gives_nearest_neighbour_moves_equivariant_odds_and_bell_correlations_with_nonlocal_odds_bounded_theorem_note_2026-09-27
  - under_a_unitary_wave_with_born_count_statistics_a_record_count_that_never_falls_never_rises_records_cannot_form_from_nothing_bounded_theorem_note_2026-09-28
runner: scripts/records_as_beables_which_record_carries_a_disturbance_is_a_choice_of_identity_2026_09_28.py
---

# Records as beables: which record carries a disturbance is a choice of identity; hop-following records lag, the wave's own identity travels

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a pre-registered numerical test, revised after two independent
checks; a supplied reading; unaudited.

## In one paragraph

Add one particle to a sea of records moving by Bell's jump law. Which record
carries the disturbance? The dynamics does not say. Bell's law moves
occupations that carry no labels, so "which record" is a rule you add.

- **Follow the record that hops.** The record that started at the origin
  lags far behind the disturbance. On a line it moves about one site however
  far the disturbance goes. On a square grid it moves a fifth to a third as
  far, and the fraction keeps falling.
- **Follow the wave's own bookkeeping.** That is, the term of the wave that
  carries the added particle. Then the tagged record's spread matches the
  disturbance's at late times.

So "does a particle travel as a record, or as a pattern through records?" is
not settled by this dynamics. It is a choice of identity, and the owner's
"records move" reading makes it a choice for the owner.

## Why this question

The owner's reading says records move between neighbouring sites. Probe 7
showed that, under a unitary wave, the number of records is fixed, so a
record forms at a site by arriving. The second panel's foundations lens asked
whether "records move" is literal: does a record travel with a disturbance?
It pre-registered this test. The first version of this note answered "no"
under one identity rule. Both independent checks showed that the answer
depends on the rule.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): one qubit per site;
  records form, one per site, permanent. The memo supplies no dynamics.
- **Supplied, not adopted:**
  - the qubit read as one fermion mode;
  - free hopping `H = −sum (c^dag_x c_y + h.c.)` on rings and square tori,
    with antiperiodic closed shells;
  - the sea is the ground state of `N0` particles;
  - `psi = c^dag_0 |sea>`;
  - beables follow Bell's minimal jump law.
- **Identity rules** (both extra to Bell's law):
  - **Hop-following:** the record that jumps keeps its identity. This is a
    nearest-neighbour process.
  - **Laplace:** at each time, occupation `i` carries the added particle
    with weight `|A_i0 (A^-1)_0i|^2`. These are the squared terms of the
    Laplace expansion of the amplitude determinant along the added orbital's
    column. It is an assignment made afresh at each time. No
    nearest-neighbour process realising it is built here.
- **Measures:** the tagged record's RMS displacement, against the RMS spread
  of the excess density `<n_x>(t) − N0/n` about the origin.
- **Pre-registered** by the foundations lens:
  - the literal picture PASSES if the ratio is at least `0.7`, FAILS if at
    most `0.3`;
  - it was set at `t = L/2`. As applied: at the latest time before the
    excess wraps around the lattice (`t = L/4`). At `L/2` the excess has
    wrapped, which makes the comparison a finite-ring interference effect
    (a point the other-vendor referee made).

## T1 — the method

- **Amplitudes.** Slater determinants: the added orbital evolves as
  `e^{−iht} e_0`, and the sea's orbitals by phases.
- **Rates.** Bell's rates come from row-replacement ratios, with one inverse
  and one matrix product per step.
- **Initial records** by Metropolis: single-occupation moves to random
  sites, `40n` attempts from a random well-conditioned start, one fresh chain
  per history.
- **Validation** on a ring of 16:
  - the excess spread at `t = 4` is `4.9710` from determinants and
    `4.9708` from full Fock-space evolution;
  - the Monte Carlo density deviates from `|psi|^2` by at most `0.052` (300
    histories).
- The excess spread is a one-body quantity. So it validates the arithmetic;
  the Monte Carlo density check is what validates the Bell sampler.

## T2 — hop-following, one dimension: the record stays

| ring (half filling) | excess spread at `t = L/16 … L/4` | tagged RMS | ratio at `t = L/4` |
|---|---|---|---|
| 16 | `2.0, 3.0, 4.1, 5.0` | `0.45 → 1.00` | `0.20` |
| 32 | `3.5, 5.8, 8.4, 10.5` | `0.76 → 1.07` | `0.10` |
| 64 | `6.3, 11.5, 16.9, 21.7` | `1.06 → 1.14` | `0.05` |

- The tagged record stays within about one site at half filling, while the
  excess spreads ballistically.
- The ratio falls with `L`.
- The cause is single file: records cannot pass one another on a line. The
  independent check found the tagged record's range is about `1/(2 ν)`
  sites for filling `ν`. It keeps creeping slowly on short rings after
  wrapping; it does not stop.

## T3 — hop-following, two dimensions: the record lags more and more

Before wrapping:

| torus (density) | times | ratios |
|---|---|---|
| `8x8` (0.38) | `0.5, 1, 1.5, 2` | `0.37, 0.42, 0.40, 0.37` |
| `12x12` (0.42) | `0.76, 1.5, 2.24, 3` | `0.37, 0.34, 0.26, 0.24` |
| `16x16` (0.41) | `1, 2, 3, 4` | `0.30, 0.30, 0.23, 0.20` |

- The tagged record's displacement grows slowly (`1.4` sites by `t = 4` on
  `16x16`), while the excess spreads ballistically (`7.3`).
- The ratio falls with time and is at the fail line on the largest torus.
- The Fable check reports `0.145` at `t = 5` on `20x20`, falling like
  `t^-0.7`, and the same pattern in 3D (`8x8x8`: `0.22`).
- The earlier "borderline" reading came from stopping at `t <= 2`.

## T4 — the wave's own identity travels with the disturbance

On the same trajectories:

| | Laplace ratios over time | hop-following |
|---|---|---|
| ring 32 | `0.76, 0.92, 0.96, 1.02` | `0.22, 0.17, 0.13, 0.10` |
| `12x12` | `0.71, 0.91, 0.99, 1.04` | `0.37, 0.34, 0.26, 0.24` |

- At the latest times the Laplace identity's spread matches the excess.
- At early times it is lower, because the excess includes the sea's static
  correlation hole around the origin.
- The Fable check found the same, within 2 %, at every size, density and
  dimension it tried, using the projected added orbital.

So on identical trajectories the answer to "does the record travel?" runs
from `0.05` to `1.0`, depending only on the identity rule.

## T5 — a dilute sea carries further under hop-following

On a ring of 64 with 8 particles (`ν = 1/8`):
- the tagged record carries about `3.8` sites (`1/(2ν) = 4`);
- the ratio is `0.46, 0.29, 0.20, 0.16` over time, against `0.05` at half
  filling.

The literal picture holds only over the carrying length `~1/(2ν)`, and passes
only as `ν -> 0`.

## What this means for the records reading

- **Bell's law does not fix which record is which.** "Does a record travel
  with a particle?" is decided by the identity rule, not by the dynamics.
  - *Hop-following*, the rule a nearest-neighbour jump law suggests: records
    stay near home and particles are patterns passing through them.
  - *The wave's own bookkeeping:* the tagged record travels with the
    particle. But no local jump process for that identity is built here. It
    may require identity to pass between distant records.
- **Under the owner's reading**, records move between neighbouring sites.
  That favours hop-following, and with it the pattern picture.
- **Whether everyday records are patterns of many carriers** (the
  foundations lens's two-tier reading) is consistent with this. No stable
  pattern is simulated here, so it is not shown.

## No-Go Discipline Gate

Recorded per `docs/ai_methodology/skills/no-go-discipline/SKILL.md`. The
negative part: under hop-following, the tagged record fails the literal
picture (1D decisively, 2D at the sizes tested).

- **N1 — routes to the literal picture:**
  1. *Another identity rule* — ATTEMPTED (T4). The Laplace identity passes.
     So the negative claim is only for hop-following.
  2. *A dilute sea* — ATTEMPTED (T5). It passes only as `ν -> 0`.
  3. *Larger sizes and 3D* — ATTEMPTED to `16x16`, plus the independent
     check to `20x20` and `8x8x8`.
  4. *Other equivariant laws* (non-minimal, longer jumps) — NOT ATTEMPTED.
  5. *Interactions* — NOT ATTEMPTED.
- **N2 — independence.** The identity rule, law, density and interactions
  are independent premises.
- **N3 — hidden-wall scan.** The time choice (before wrapping) and the
  identity rule are declared. The single-file mechanism is load-bearing in
  1D and is stated.
- **N4 — residual matching.** No external witness is used.
- **N5 — rhetoric audit.** "Hop-following records lag" is tested per site
  and per block, in 1D and 2D. It is not claimed for all laws or identity
  rules.
- **N6 — primitive scan.** No registered primitive supplies an identity
  rule.
- **N7 — steelman.**
  - *The case against.* Identity for identical fermions has no physical
    content. So neither result says anything about the world, only about
    conventions.
  - *Reply.* That is the note's conclusion. The owner's moving-records
    reading gives identity content, and then the rule matters.
- **N8 — cross-cycle echo.** Probe 7 and the records-as-beables note (T6:
  the vacuum's records are at rest) are this result's neighbours.
- **Outcome:**
  - PASS for the scoped claims (hop-following lags; the Laplace identity
    travels; the choice decides).
  - The earlier broad claim ("a disturbance moves as a pattern") is
    withdrawn.

## What this does not show

- Free hopping only. There are no interactions, no two-component walker,
  and no 3D in the runner.
- There is no local jump process for the Laplace identity.
- No stable many-record pattern is simulated.

## Independent checks

- **Codex `gpt-5.6-sol` referee**, on the first version.
  - **Verdict: "stands with corrections".**
  - 1D was reproduced (`0.219`, `0.133`).
  - Its findings:
    - the 2D classification did not follow the pre-registered time;
    - the identity lift is not physical;
    - "stops" is wrong;
    - the Metropolis details were missing;
    - the two-tier reading and the gate overreached.
  - All applied.
- **Claude Fable 5.1 subagent**, working from its own code (same vendor
  family, so not a referee).
  - **Verdict: "confirmed with corrections".**
  - Every number was reproduced by full Fock-space Bell and an independent
    determinant sampler. It also:
    - went to `20x20` and 3D;
    - found the Laplace identity (ratio `1.00`) and the dilute-sea law
      `1/(2ν)`;
    - showed the centre-following steelman was wrong, because the excess's
      centre never moves.
  - All applied. This revision's title and conclusion follow from its
    identity-rule finding.
- A second round on this revision is pending.

## Reproduction

```bash
python3 scripts/records_as_beables_which_record_carries_a_disturbance_is_a_choice_of_identity_2026_09_28.py
```

Expected: `TOTAL: PASS=5 FAIL=0` (about 2 minutes).
