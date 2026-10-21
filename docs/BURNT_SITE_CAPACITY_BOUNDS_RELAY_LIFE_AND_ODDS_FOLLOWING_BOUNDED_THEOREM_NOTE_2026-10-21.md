---
claim_id: burnt_site_capacity_bounds_relay_life_and_odds_following_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Given that a site records once and a relay forms one record per tick, N relays confined to S unburnt sites record for at most S/N ticks, exact odds-following lasts at most n / max P ticks per block of n sites, and counting at coarser rungs never raises this above sites / relays; on a supplied 1D ring walk the register's step law alone strands relays that still have unburnt sites elsewhere, while three supplied fallbacks for an all-used-up neighbourhood reach the counting bound with no double records, and the nearest-unused-block fallback has the shortest jumps and exact block-translation covariance; finite estimates of the burnt fraction for measured densities and ages are far below 1 except for a neutron-star core held still in the lattice frame. The lattice spacing, block size, relays per nucleon and rest frame are supplied. No fallback rule is adopted and no physical effect of site exhaustion is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/burnt_site_capacity_bounds_relay_life_and_odds_following_2026_10_21.py
---

# Burnt-site capacity bounds relay life and odds-following

Claim type: bounded_theorem.
Primary runner: `scripts/burnt_site_capacity_bounds_relay_life_and_odds_following_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. In that register a relay forms one record per tick in a neighbouring block, and a site records once. This note asks what that counting forces and what happens when every neighbouring block is used up. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the Record axiom; the walk models below are supplied. The main result is that no measured regime estimated here comes near exhausting sites, so measurement cannot tell the fallback rules apart.

## Statement

1. Lifetime (pigeonhole). N relays held in S unburnt sites can record for at most S/N ticks.
2. Odds-following. Following the odds exactly needs sum_t P_t(X) <= n for every block X of n sites. Exact following therefore lasts at most n / max_X P ticks. For the supplied standing wave with n = 4 this is 44.7 ticks, against nL = 64. Every fallback rule must leave the odds after this time.
3. Coarser rungs. Counting at coarser rungs raises the capacity time (44.7, 46.7, 57.8, 64, 64 for rungs 0 to 4), but never above sites / relays.
4. Ring walk with L = 16 blocks.
   - The step law alone strands relays early (median life 56 of 63 for n = 4, and 238 of 255 for n = 16). Most stuck relays still have unburnt sites elsewhere.
   - Three fallbacks were tested for an all-used-up neighbourhood: a fixed-partition ladder, relay-centred doubling, and the nearest unused block. None records a site twice. Each stops a relay only when every unburnt site is in its own block, so each reaches the counting bound.
   - The nearest-unused fallback has the shortest mean jump.
   - Doubling and nearest are exactly block-translation covariant. The fixed ladder is not: it favours its own partition boundaries.
5. Burnt fraction. With block spacing b = 2a, a = 2 Planck lengths, 8 sites per block and 3 relays per nucleon, beta = (relays per site) x (ticks) is far below 1 for the Sun, white dwarfs, nucleosynthesis and recombination. Only a neutron-star core held still in the lattice frame exceeds 1. Any motion above about 5e-12 m/s relative to the lattice removes that, and galactic acceleration alone exceeds it within a fraction of a second.

## Derivation

Each record burns one unburnt site and no site records twice, so N relays in S sites make at most S records and last at most S/N ticks. If the occupation equals the odds at every tick, the expected number of records in block X over T ticks is sum_t P_t(X). This cannot exceed the n sites of X, which gives item 2. A coarser rung pools blocks, so its max P is an average of finer ones and the capacity time rises. It is still bounded by item 1 applied to the whole region.

## Checks

The runner prints 26 PASS lines, and its output ends `TOTAL: PASS=26 FAIL=0`.

- `T1` max life 63 against nL - 1 = 63, with 127950 records equal to 127950 burnt sites and 0 double records.
- `T2` the standing wave is stationary (1.5e-16) with max P 0.0895 (uniform 0.0625), giving T_cap 44.7.
- `T3` the rung table above.
- `R1` (n = 4 and n = 16) the step law alone strands relays. Only 0.222 and 0.121 of stuck relays had nothing fresh outside their own block.
- `R2` (three rules each at n = 4 and n = 16): median life 63 and 255, with full reach.
- `R3` mean jumps of 3.50, 3.29 and 2.92 blocks (ladder, doubling, nearest) at n = 4, and 3.36, 3.43 and 2.95 at n = 16.
- `R4` current/odds of 0.995 and 0.999 before the first used-up target.
- `R5` the fraction of worlds that change under a one-block shift is 0.595 for the ladder and 0.000 for doubling and nearest.
- `R6` standing wave: total variation from the odds is 0.028 at n = 200, which is sampling noise. At n = 4 it is 0.069 before tick 18, when 0.64 of worlds have already hit a used-up target under the register's existing redraw clause, and 0.237 (0.231 for nearest) after T_cap.
- `R7` drifting packet with the nearest rule: no relay is stranded. The check passes, but at n = 2 the realised current falls to 0.466 of the odds' current, with 2.8 fallbacks per relay. It recovers to 0.969 at n = 4 and 0.999 at n = 8.
- `D1` a supplied persistent 3D walk with uniform odds. At n = 8 a used-up target occurs 6.0e-5 per step and the fallback is never needed. Only n = 1 needs the fallback, at 2.5e-4 per step.
- `P1` to `P7` the burnt-fraction estimates:
  - Sun core over 4.6 Gyr: beta = 7.5e-12;
  - a pinned proton lasts 1.67e8 yr, and 5.7e15 yr when spread over its thermal size in the Sun;
  - white-dwarf core: beta = 1.0e-7;
  - neutron-star core held still: beta = 71, life 1.4e8 yr, with beta = 1 at a = 0.24 Planck lengths;
  - the same star moving at 100 km/s: trailing-edge beta = 5.4e-17;
  - nucleosynthesis: 2.7e-23, and recombination: 8.2e-31;
  - black holes, conditional on sites counting coordinate volume inside the horizon: 6.1e8 yr (10 solar masses), 6.6e9 yr (33 solar masses), 2.6e26 yr (M87*).

## What is supplied and the boundary

Supplied: the ring and 3D walk models, the standing wave, the three fallback rules, and the conversion constants (a = 2 Planck lengths, blocks of 8 sites, 3 relays per nucleon, and the worst case of a body at rest in the lattice frame). The burnt fraction scales as (a / Planck length)^2. The black-hole figures rest on an unfixed assumption about sites inside a horizon.

Not established: an adopted fallback rule, and any physical effect of site exhaustion. The nearest-unused-block rule uses only block adjacency and equal probability, and it gives one answer on Z^3 with finitely many burnt sites. Its jumps are two or more blocks per tick, which is faster than the top speed, so they would put a deposit on a spacelike step. One supplied choice remains open: what to do when the new block's odds are all zero. Matter at nuclear density held still in the lattice frame for about 1e8 yr is an untested prediction, not a measured constraint.
