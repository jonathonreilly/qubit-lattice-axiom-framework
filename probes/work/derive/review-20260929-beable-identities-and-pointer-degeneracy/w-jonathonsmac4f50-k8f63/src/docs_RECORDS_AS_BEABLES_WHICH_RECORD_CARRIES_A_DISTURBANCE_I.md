---
claim_id: records_as_beables_which_record_carries_a_disturbance_is_a_choice_of_identity_hop_following_records_lag_a_laplace_identity_travels_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied reading, not adopted: records as beables (Bell's minimal jump law) on a one-mode-per-site free-fermion sea (the axioms' qubit read as one fermion mode), antiperiodic closed shells; one particle added at the origin. Bell's law moves unlabelled occupations; a record's identity is an extra rule. Two rules on the same trajectories: hop-following (the record that jumps keeps its identity) and a Laplace identity (occupation i carries the added particle with weight |A_i0 (A^-1)_0i|^2, a per-time assignment; no nearest-neighbour process realising it is built). (T1) Method validated against full Fock-space evolution. (T2) Hop-following, 1D: the tagged record stays within about 1/(2 nu) sites (about one at half filling) while the excess density spreads ballistically; ratio of RMS displacements at t = L/4 (when the fastest front first reaches the seam) 0.20, 0.10, 0.05 on rings of 16, 32, 64. (T3) Hop-following, 2D (dt = 0.005) up to t = L/4, when the fastest front first reaches the seam: after an early peak the ratios fall, to 0.226 +- 0.008 on 12x12 at t = 3 and 0.206 +- 0.014 on 16x16 at t = 4; the record lags, and the pre-registered 0.3 decision at the pre-registered time t = L/2 (after wrapping) is not made. (T4) The Laplace identity with the added orbital projected off the sea (canonical): ratio 0.99 (ring 32) and 1.02 (12x12) at the latest time; the same wave written with the added column plus ten times an occupied orbital gives 1.27 -> 0.63 on 12x12, so this identity too is a choice of representation. (T5) Dilute ring (nu = 1/8): hop-following carries about 3.8 sites, ratio 0.16 at t = 16 against 0.05 at half filling. Free hopping only; one equivariant law; no interactions; no 3D (an independent check reports 3D behaves like 2D)."
upstream_dependencies:
  - minimal_axioms
  - records_as_beables_under_the_moving_records_reading_bells_jump_law_gives_nearest_neighbour_moves_equivariant_odds_and_bell_correlations_with_nonlocal_odds_bounded_theorem_note_2026-09-27
  - under_a_unitary_wave_with_born_count_statistics_a_record_count_that_never_falls_never_rises_records_cannot_form_from_nothing_bounded_theorem_note_2026-09-28
runner: scripts/records_as_beables_which_record_carries_a_disturbance_is_a_choice_of_identity_2026_09_28.py
---

# Records as beables: which record carries a disturbance is a choice of identity; hop-following records lag, a Laplace identity travels

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
- **Follow the wave's Laplace bookkeeping.** That is, the term of the wave's
  determinant that carries the added particle, written in canonical form.
  Then the tagged record's spread matches the disturbance's at late times.
  But the same wave written differently gives a different answer, so even
  this is a choice.

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
    with weight `|A_i0 (A^-1)_0i|^2`, normalised. These are the squared
    terms of the Laplace expansion of the amplitude determinant along the
    added orbital's column. It is an assignment made afresh at each time. No
    nearest-neighbour process realising it is built here.
    - The weights depend on how the added column is written: adding occupied
      orbitals to it leaves every amplitude unchanged but changes them.
    - The canonical choice projects the added orbital off the sea.
- **Measures:** the tagged record's RMS displacement, against the RMS spread
  of the excess density `<n_x>(t) − N0/n` about the origin.
- **Pre-registered** by the foundations lens:
  - the literal picture PASSES if the ratio is at least `0.7`, FAILS if at
    most `0.3`;
  - it was set at `t = L/2`. At that time the excess has wrapped around the
    lattice, which makes the comparison a finite-ring interference effect.
  - As applied here, at `t = L/4`, when the fastest part of the front first
    reaches the seam.
  - That change was made after seeing the data. So in 2D the pre-registered
    decision is **not made**; the results below say how far the record
    lags. On rings the result fails the literal picture at either time.

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

## T3 — hop-following, two dimensions: the record lags

With `dt = 0.005` (the fraction of steps whose total jump probability exceeds
`0.5` is at most `0.03`), up to `t = L/4`:

| torus (density) | times | ratios | error at the end |
|---|---|---|---|
| `8x8` (0.38) | `0.5, 1, 1.5, 2` | `0.35, 0.44, 0.40, 0.38` | `0.02` |
| `12x12` (0.42) | `0.75, 1.5, 2.25, 3` | `0.33, 0.33, 0.25, 0.23` | `0.008` |
| `16x16` (0.41) | `1, 2, 3, 4` | `0.35, 0.29, 0.23, 0.21` | `0.014` |

- The tagged record's displacement grows slowly (`1.5` sites by `t = 4` on
  `16x16`), while the excess spreads ballistically (`7.3`).
- After an early peak (`t ~ 1`) the ratio falls: steadily on `12x12` and
  `16x16`, and only slightly on `8x8` (`0.44` to `0.38`).
- The Fable check reports `0.145` at `t = 5` on `20x20`, falling like
  `t^-0.7`, and the same pattern in 3D (`8x8x8`: `0.22`).
- The other-vendor referee's multi-jump integration gives `0.195 ± 0.006`
  and `0.211 ± 0.012` on `16x16`. An earlier version used `dt = 0.02` there,
  which let more than one jump fall in a step too often.
- **Reading:** the record lags, clearly. Whether this fails the literal
  picture by the pre-registered rule is not decided, because that rule's
  time is after wrapping.

## T4 — the Laplace identity travels, and is itself a choice

On the same trajectories:

| | Laplace ratios over time (canonical) | hop-following |
|---|---|---|
| ring 32 | `0.87, 0.94, 0.96, 0.99` | `0.22, 0.17, 0.13, 0.10` |
| `12x12` | `0.90, 0.97, 1.00, 1.02` | `0.33, 0.33, 0.25, 0.23` |

- With the added orbital projected off the sea, the Laplace identity's
  spread matches the excess.
- The other-vendor referee's independent sampling gives `1.022 ± 0.013` and
  `1.038 ± 0.006`.
- **It is a choice of representation.** Write the same wave with the added
  column plus ten times an occupied orbital. Every amplitude is unchanged,
  yet on `12x12` the Laplace ratio runs `1.27, 0.93, 0.73, 0.63`.
- So on identical trajectories the answer to "does the record travel?" runs
  from about `0.2` to `1.0`, depending only on how identity is assigned.
  Even the Laplace identity is not unique.

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
  - *The Laplace bookkeeping, canonical form:* the tagged record travels
    with the particle. But it depends on how the wave is written, and no
    local jump process for it is built here. It may require identity to pass
    between distant records.
- **Under the owner's reading**, records move between neighbouring sites.
  That favours hop-following, and with it the pattern picture.
- **Whether everyday records are patterns of many carriers** (the
  foundations lens's two-tier reading) is consistent with this. No stable
  pattern is simulated here, so it is not shown.

## No-Go Discipline Gate

Recorded per `docs/ai_methodology/skills/no-go-discipline/SKILL.md`. The
negative part: under hop-following, the tagged record lags the disturbance.
It fails the literal picture on rings; in 2D the pre-registered decision is
not made.

- **N1 — routes to the literal picture:**
  1. *Another identity rule* — ATTEMPTED (T4). The canonical Laplace
     identity passes; an altered representation does not. So the negative
     claim is only for hop-following.
  2. *A dilute sea* — ATTEMPTED (T5). It passes only as `ν -> 0`.
  3. *Larger sizes and 3D* — ATTEMPTED to `16x16` in the runner, plus the
     independent check to `20x20` and `8x8x8`.
  4. *Other equivariant laws* (non-minimal, longer jumps) — NOT ATTEMPTED.
  5. *Interactions* — NOT ATTEMPTED.
- **N2 — independence (pairwise).**

  | pair | does one close the other? |
  |---|---|
  | identity rule / law | no: each changes which record is tagged independently |
  | identity rule / density | no: T5 varies density under a fixed rule |
  | identity rule / interactions | no |
  | law / density | no |
  | law / interactions | no |
  | density / interactions | no: dilute and interacting are separate limits |
  | size or dimension / identity rule | no: the rule's effect appears at every size tested |
  | size or dimension / law | no |
  | size or dimension / density | no: T5 is at one size, T2 and T3 at several |
  | size or dimension / interactions | no |

  The walls are independent, so none collapses.
- **N3 — hidden-wall scan.** Three declared walls:
  - the comparison time (moved to `t = L/4` after seeing data);
  - the integrator (one jump per step, controlled by `dt = 0.005` and the
    large-step fraction);
  - the statistics (bootstrap errors).

  The single-file mechanism is load-bearing in 1D and is stated.
- **N4 — residual matching.** No external witness is used.
- **N5 — rhetoric audit.** "Hop-following records lag" is tested per site
  and per block, in 1D and 2D. It is not claimed for all laws or identity
  rules.
- **N6 — primitive scan.** No registered primitive supplies an identity
  rule.
- **N7 — steelman.**
  - *The case against.* Identity for identical fermions has no physical
    content, so neither result says anything about the world.
  - *Reply.* That is the note's conclusion. The owner's moving-records
    reading gives identity content, and then the rule matters.
- **N8 — cross-cycle echo.** Probe 7 and the records-as-beables note are
  this result's neighbours.
- **Outcome.** `partial-attempt-with-named-untested-routes`:
  - the scoped findings stand (hop-following lags; the Laplace identity
    travels but is representation-dependent; the rule decides);
  - routes 4 and 5 are untested;
  - in 2D the pre-registered decision is not made.

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
- **Codex `gpt-5.6-sol`, second round.**
  - Resolved: the 1D core.
  - Not or partly resolved:
    - the 2D decision: the time was changed after seeing data, and the
      one-jump-per-step integrator was biased at `dt = 0.02`;
    - "the wave's own" identity is representation-dependent (its test:
      `1.038 -> 0.633`);
    - the wrapping endpoint;
    - Monte Carlo uncertainty;
    - the gate outcome, N2 and N3.
  - **Applied:**
    - `dt = 0.005` with a large-step diagnostic;
    - bootstrap errors;
    - the canonical and altered Laplace representations (T4);
    - the 2D decision marked "not made";
    - the wrapping endpoint restated;
    - the gate demoted, with an N2 table and N3 walls.
- **Codex `gpt-5.6-sol`, third round.**
  - Resolved: the 2D decision and integration, the identity interpretation,
    and the Monte Carlo evidence.
  - Partly resolved: a stale "before the first wrap" in the scope, the N2
    table missing the size route, and T3's monotonicity wording. All three
    are now fixed.
- **Codex `gpt-5.6-sol`, fourth round: "CONFIRMED AS REVISED".**

## Reproduction

```bash
python3 scripts/records_as_beables_which_record_carries_a_disturbance_is_a_choice_of_identity_2026_09_28.py
```

Expected: `TOTAL: PASS=5 FAIL=0` (about 3 minutes).
