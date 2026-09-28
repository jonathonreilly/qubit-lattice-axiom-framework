---
claim_id: records_as_beables_a_disturbance_moves_as_a_pattern_the_record_that_carries_it_barely_moves_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied reading, not adopted: records as beables (Bell's minimal jump law) on a one-mode-per-site sea (the axioms' qubit read as one fermion mode), free nearest-neighbour hopping, antiperiodic closed shells; a record's identity is 'the occupation that jumped'. One particle is added at the origin of the sea's ground state; the record at the origin is tagged. Pre-registered (second panel, foundations lens): the literal picture passes if the tagged record's RMS displacement is >= 0.7 of the excess density's RMS spread at t = L/2 (before wrapping in 2D), fails if <= 0.3. (T1) Method validated: Slater-determinant amplitudes with row-replacement ratios reproduce full Fock-space evolution (excess spread 4.9710 vs 4.9708 on a ring of 16) and Monte Carlo densities match |psi|^2. (T2) One dimension, rings of 16, 32, 64: the tagged record moves about one site (RMS 0.9-1.2) whatever L while the excess spreads ballistically; ratio at t = L/2: 0.23, 0.13, 0.07 (fails, and falls with L). (T3) Two dimensions, 8x8 and 12x12 closed shells up to t = 2: ratios 0.2-0.45, falling after t = 1; at 12x12 0.30 and 0.26 at t = 2 (at or just below the fail line). Free hopping only; no interactions, no three dimensions, no other identity rule or equivariant law."
upstream_dependencies:
  - minimal_axioms
  - records_as_beables_under_the_moving_records_reading_bells_jump_law_gives_nearest_neighbour_moves_equivariant_odds_and_bell_correlations_with_nonlocal_odds_bounded_theorem_note_2026-09-27
  - under_a_unitary_wave_with_born_count_statistics_a_record_count_that_never_falls_never_rises_records_cannot_form_from_nothing_bounded_theorem_note_2026-09-28
runner: scripts/records_as_beables_a_disturbance_moves_as_a_pattern_the_tagged_record_barely_moves_2026_09_28.py
---

# Records as beables: a disturbance moves as a pattern; the record that carries it barely moves

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a pre-registered numerical test; a supplied reading; unaudited.
Independent checks are recorded below.

## In one paragraph

Add one particle to a sea of records. Under the beables reading (records
move by Bell's jump law, with odds from the wave), does the record that
started where the particle was added travel with the disturbance? In one
dimension it does not. The disturbance spreads out at the speed of the waves.
The record that started it moves about one site and stops, however large the
ring. In two dimensions it moves more, but still only about a quarter to a
third as far as the disturbance, and the fraction falls with time.

So in this reading a moving particle is a pattern passing through records,
not a record travelling. That is the two-tier picture the second panel's
foundations lens proposed:
- carriers (the records) stay nearly put;
- what moves is the pattern they form.

## Why this question

The owner's reading says records move between neighbouring sites. Probe 7
showed that, under a unitary wave, the number of records is fixed, so a
record forms at a site by arriving. The foundations lens asked whether
"records move" is literal: does a record travel with a disturbance, or does
the disturbance travel through records? It pre-registered this test.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): one qubit per site;
  records form, one per site, permanent. The memo supplies no dynamics.
- **Supplied, not adopted:**
  - **The site.** The qubit is read as one fermion mode (occupied or
    empty). This is the one-mode-per-site sea Bell used in 1984, not the
    campaign's two-component walker.
  - **The sea.** Free hopping `H = −sum (c^dag_x c_y + h.c.)` on rings and
    square tori, with antiperiodic boundaries so the sea is a closed shell.
    The sea is the ground state of `N0` particles.
  - **The disturbance.** `psi = c^dag_0 |sea>`: one particle added at the
    origin.
  - **Beables.** Bell's minimal jump law. Each jump moves one occupation to
    a neighbouring site.
  - **Identity.** The record that jumps keeps its identity; the tagged
    record is the one at the origin. The fermions are identical, so identity
    is a rule, and this is the natural one for single-hop jumps.
- **Measures.**
  - The RMS displacement of the tagged record.
  - The RMS spread of the excess density `<n_x>(t) − N0/n` about the origin.
- **Pre-registered** by the foundations lens:
  - the literal picture PASSES if the ratio is at least `0.7` at `t = L/2`;
  - it FAILS (the pattern reading is forced) if the ratio is at most `0.3`;
  - in between, double `L`.

## T1 — the method

- **Amplitudes.** The wave is a Slater determinant. The added orbital
  evolves as `e^{−iht} e_0`, and the sea's orbitals by phases.
- **Rates.** Bell's rates need only ratios of amplitudes between neighbouring
  configurations. Replacing one row of the orbital matrix gives them from one
  matrix inverse per step.
- **Initial records** are sampled from `|psi|^2` by Metropolis.
- **Validation** on a ring of 16:
  - the excess spread at `t = 4` is `4.9710` from determinants and
    `4.9708` from full Fock-space evolution;
  - the Monte Carlo density deviates from `|psi|^2` by at most `0.052`,
    sampling error for 300 histories.
- An earlier full Fock-space Bell simulation on the same ring gave a tagged
  RMS of `0.89`, against `0.92` here.

## T2 — one dimension: the record stays, the pattern travels

| ring | excess spread at `t = L/8, L/4, 3L/8, L/2` | tagged RMS | ratio at `t = L/2` |
|---|---|---|---|
| 16 | `3.0, 5.0, 5.3, 4.1` | `0.8–1.1` | `0.23` |
| 32 | `5.8, 10.5, 10.4, 8.3` | `1.05–1.15` | `0.13` |
| 64 | `11.5, 21.7, 20.8, 16.4` | `1.09–1.16` | `0.07` |

- The tagged record's displacement stays about one site, whatever `L`.
- The excess spreads ballistically, until it wraps around the ring.
- The ratio is below `0.3` and falls with `L`. **The literal picture fails
  in one dimension.**
- The reason is single file. A record can hop only into an empty
  neighbouring site, so records cannot pass one another on a line.

## T3 — two dimensions: more motion, still mostly pattern

Compared before the excess wraps (`t <= 2`):

| torus (sea density) | ratio at `t = 0.5, 1, 1.5, 2` |
|---|---|
| `8x8` (0.38) | `0.33, 0.43, 0.39, 0.37` |
| `8x8` (0.62) | `0.19–0.26` |
| `12x12` (0.42) | `0.27, 0.37, 0.35, 0.30` |
| `12x12` (0.58) | `0.22, 0.30, 0.28, 0.26` |

- Records can go around one another in 2D, and the tagged record moves
  more: about 1.2 sites by `t = 2`.
- The excess still outruns it: 4 sites by `t = 2`.
- The ratio falls after `t = 1`. At the largest size it is at or just below
  the fail line (`0.30`, `0.26`). The denser sea gives the smaller ratio.
- By the pre-registered rule, `8x8` was "in between". So `L` was increased
  to 12, where the result sits at the fail line and still falls with time.
- **Two dimensions is borderline, leaning to the pattern reading.**
  Three dimensions and longer times are not tested.

## What this means for the records reading

Under option C with the natural identity rule, a travelling particle is a
pattern in the records, not a travelling record. That fits the two-tier
reading the foundations lens proposed:
- **carriers:** the fixed-count records of probe 7;
- **records in the everyday sense:** stable patterns of many carriers.

The owner's "records move" then holds for carriers over short distances,
while things that travel far are patterns. This bears on the owner's
question "can the number of records in a sealed box go up?". Under this
reading, what forms and moves at large scale is a pattern, and patterns can
form while the number of carriers stays fixed.

## No-Go Discipline Gate

Recorded per `docs/ai_methodology/skills/no-go-discipline/SKILL.md`.
The negative claim: under the stated reading, the literal picture fails in
one dimension, and is borderline-failing in two at the sizes tested.

**N1 — routes that could rescue the literal picture:**
1. *A different identity rule*: for example, the tag follows the excess
   density's centre, or an optimal matching. NOT ATTEMPTED. Identity for
   identical fermions is a rule, and another rule can give another answer.
   This is the largest open route.
2. *Other equivariant laws* (non-minimal rates, possibly longer jumps) — NOT
   ATTEMPTED. Longer jumps would break single file.
3. *Larger two-dimensional sizes and three dimensions* — ATTEMPTED at `8x8`
   and `12x12`; 3D not attempted.
4. *Interactions* (a record gas with repulsion or binding) — NOT ATTEMPTED.
5. *Lower sea density* (dilute records) — partly ATTEMPTED (densities
   0.38–0.62). The ratio grows as the density falls, so a dilute sea may
   pass.

Five families. Routes 1, 2, 4 and dilute seas are open. The claim is scoped
to the minimal law, the natural identity and these densities.

**N2 — independence.** Identity rule, law and density are independent
premises. Each could change the answer on its own.

**N3 — hidden-wall scan.** "Natural" (identity rule) is flagged as a choice
in the premises. No other scanned phrase is load-bearing.

**N4 — residual matching.** No external witness is used. The single-file
mechanism is standard (reference only) and is not load-bearing.

**N5 — rhetoric audit.** "A disturbance moves as a pattern": tested at
per_site (tagged hops), per_block (rings and tori) and per_mode (the sea's
orbitals). It is not claimed lattice-wide for all identity rules, laws or
dimensions.

**N6 — partial-closure paths.** No registered primitive supplies a record
identity rule. The owner's moving-records reading could supply one (a
reading, not physics). This note's result is conditional on the natural
rule.

**N7 — steelman.**
- *The case against.* The identity rule is the whole story. For identical
  fermions, "which record moved" has no physical content. A rule that
  passes the tag to whichever record is nearest the excess's centre would
  make the literal picture pass by construction. So the test measures a
  convention, not the world.
- *Reply.* The test is conditional on the one rule a single-hop Bell law
  singles out. Under that rule the owner's picture is either literal or not.
  Another rule is a different reading, and the note says so.

**N8 — cross-cycle echo.** Probe 7 (formation is arrival) and the
records-as-beables note (T6: the vacuum's records are at rest) are this
result's neighbours. No earlier wall of this shape was retired.

**Outcome:**
- **PASS** as scoped: one dimension decisive; two dimensions borderline at
  the sizes tested.
- The broad reading "records never carry disturbances" is not claimed.

## What this does not show

- **Dynamics.** Free hopping only. There are no interactions, no
  two-component walker, and no three dimensions.
- **Identity and law.** Only one identity rule and one equivariant law are
  used.
- **Length of runs.** Short runs in 2D (`t <= 2`), set by the torus size.

## Independent checks

Pending: a codex `gpt-5.6-sol` referee.

## Reproduction

```bash
python3 scripts/records_as_beables_a_disturbance_moves_as_a_pattern_the_tagged_record_barely_moves_2026_09_28.py
```

Expected: `TOTAL: PASS=3 FAIL=0` (about 2 minutes).
