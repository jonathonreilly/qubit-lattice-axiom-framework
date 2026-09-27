---
claim_id: records_as_beables_bells_jump_law_gives_the_walkers_records_nearest_neighbour_moves_born_odds_and_bell_correlations_at_no_record_cost_with_nonlocal_odds_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied reading, not adopted: records are beables. One record per walker sits at a site and moves only to a nearest-neighbour site; a unitary wave psi evolves by the walker's Hamiltonian and is never acted on by the records; a move x -> y happens at Bell's minimal rate max(0, J_yx)/P(x), J_yx = 2 Im[psi_y^dag H_yx psi_x] (joint configuration and joint wave for several walkers). (T1) For the walker sum_j sin k_j sigma_j in 1D, 2D and 3D the jump law's master equation equals the Schroedinger dP/dt exactly (equivariance), and every jump is between nearest neighbours. (T2) The rate table is covariant under the 24 proper cubic rotations (spin-1/2 coin action). (T3) The records never act on psi, so <H> is exactly conserved and a record costs nothing. (T4) Two walkers on separate rings with singlet coins, settings as local coin rotations and the walker's own coin-steered motion: outcomes read from the records alone reproduce the |psi|^2 correlations (Monte Carlo, 3000 runs per setting) with CHSH 2.79 (2 sqrt 2 up to packet overlap) and no signalling. (T5) The odds are nonlocal: after A's record has been steered right (left), B's first-jump rate from its start site to the right is 0.000 (0.562) and to the left 0.565 (0.000). Single- and two-walker waves only; no sea, no record creation, no interactions; the jump rates are Bell's minimal choice, not unique; the jump law uses a global time."
upstream_dependencies:
  - minimal_axioms
  - dynamics_clause_bell_values_of_record_laws_records_only_formation_stays_at_two_the_dynamics_clause_reaches_two_root_two_bounded_theorem_note_2026-09-24
runner: scripts/records_as_beables_bells_jump_law_for_the_walker_2026_09_27.py
---

# Records as beables: Bell's jump law gives the walker's records nearest-neighbour moves, Born odds and Bell correlations at no record cost, with nonlocal odds

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** exact identities and Monte Carlo on small lattices; unaudited;
independent checks recorded below.

## In one paragraph

Keep the owner's picture. Records sit at sites and move one site at a time,
and a single wave tells the odds for every move. Then what experiments demand
comes out:
- the right statistics;
- the Bell correlations, with no signalling;
- a record that costs nothing, because it never pushes on the wave.

The price is where the odds come from. They depend on the whole wave, so where
one record may jump can depend on where a distant record went. In the example
here, once one record has gone right, its partner can only go left. The moves
are local; the odds are not.

## Why this question

The landed Bell note shows that records formed locally and causally from
records alone cannot reach the measured correlations. The record-cost note of
the same date shows that records which collapse the quantum state one site at
a time cost the lattice's own energy scale. The panel convened on the
viability map (foundations lens) pointed to a third reading that avoids both:
records as beables, John Bell's 1984 lattice model. The actual configuration
is a set of records, a wave guides them, and nothing ever collapses.

That reading matches the owner's own ones clause for clause:
- records move between neighbouring sites;
- one record at a time;
- the possibility shifts with the neighbourhood;
- records are permanent, in the sense of permanent histories.

This note tests it on the campaign's walker. The literature is reference only:
Bell, "Beables for quantum field theory" (1984); Dürr, Goldstein, Tumulka and
Zanghì, "Bell-type quantum field theories" (2005); Vink (1993) on the
non-uniqueness of the rates.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`), read in full.
- **Supplied, not adopted:**
  - **The wave.** `psi` evolves unitarily by the walker
    `H = sum_x sum_j [psi_x^dag (sigma_j/2i) psi_{x+e_j} + h.c.]`.
  - **The records.** One record per walker, at a site.
  - **The jump law.** A record at `x` moves to a neighbour `y` at rate
    `max(0, J_yx)/P(x)`, where
    - `J_yx = 2 Im[psi_y^dag H_yx psi_x]` is the probability current along
      the bond;
    - `P(x) = |psi_x|^2`.

    For several walkers, `x` and `y` are joint configurations that differ in
    one walker's site, and `psi` is the joint wave.
- **Readout.** An outcome is read from the records' positions alone.

## T1 — the records keep the wave's statistics (equivariance)

*Statement.* The master equation
`dP(y)/dt = sum_x [rate(x->y) P(x) - rate(y->x) P(y)]` equals the Schrödinger
`dP(y)/dt` at every instant. So records distributed as `|psi|^2` at one time
stay distributed as `|psi|^2`, which is the Born rule for positions. Every
jump is between nearest neighbours, because `H` has only nearest-neighbour
bonds.

*Proof.*
- The Schrödinger continuity equation is `dP(y)/dt = sum_x J_yx`, with
  `J_xy = -J_yx`.
- `max(0, J_yx) - max(0, J_xy) = J_yx`. ∎

*Checks.* 1D (`8` sites), 2D (`4^2`) and 3D (`3^3`), random waves: the
largest mismatch is `2.9e-17`, and every nonzero rate lies on a bond.

## T2 — cubic covariance

*Statement.* Rotating the wave by a proper cubic rotation, with the spin-1/2
action on the coin, rotates the rate table. The jump law is as covariant as
the walker.

*Check.* All 24 rotations on `3^3`: the largest mismatch is `2.7e-15`.

## T3 — no back-action, no record cost

*Statement.* The records never change `psi`, so `<H>` is exactly conserved
however the records move. The lock cost of the record-cost note is zero in
this reading.

*Check.* 400 steps on a 12-site ring; 9 record moves; `|Delta <H>| = 6.9e-16`.

## T4 — Bell correlations from records alone

*Setting.*
- Two walkers, each on its own 24-site ring.
- Coins in the singlet; positions in Gaussian packets at the ring's centre.
- Each wing's setting is a coin rotation `R_y(θ)`.
- The walker's own motion then steers the coin into position: `σ_z = +1`
  moves right, `−1` moves left.
- After time 8 the outcome is read from the record: right or left of centre.

*Result.* Settings `θ_A ∈ {0, pi/2}`, `θ_B ∈ {±pi/4}`, 3000 Monte Carlo
record histories per setting pair:
- correlations from the records: `-0.696, -0.694, -0.709, +0.713`;
- the `|psi|^2` values: `∓0.6977`, within 4σ;
- CHSH from the records: `2.81`; from `|psi|^2`: `2.79`. The gap to
  `2 sqrt 2 = 2.83` is the overlap of the finite packets.
- No signalling: B's mean outcome is `-0.001, -0.019` with `θ_A = 0` and
  `+0.003, +0.024` with `θ_A = pi/2`. The differences are within statistical
  error.

## T5 — the price: nonlocal odds

*Statement.* Let A's coin steer A's record first, with B frozen. Then B's
first-jump odds from its start site depend on which side A's record went:

| A's record | B's rate to the right | B's rate to the left |
|---|---|---|
| right of start | `0.000` | `0.565` |
| left of start | `0.562` | `0.000` |

The moves are nearest-neighbour. The odds of a move depend on the joint wave,
and so on where a distant record is. This is the form Bell's theorem forces
on any single-world record law with freely chosen settings. The landed Bell
note shows that odds depending on local records alone stay at CHSH = 2.

## What this means for the axioms

- **The Record axiom read as beables** keeps the owner's moving-records
  picture and avoids both failures found elsewhere:
  - the classical bound of local-causal records;
  - the lattice-scale cost of collapse.
  The dynamics clause becomes "Nothing is ever lost", a unitary wave with no
  collapse, plus a guidance law for the records.
- **The Admissibility axiom's sentence** "the probability distribution ... is
  determined by, and varies with, the nearest-neighbor conditions" would
  then describe the moves (nearest-neighbour), not the odds. The odds depend
  on the wave's values at the neighbouring configurations, and the wave is
  global.
  - That is not a defect of this reading. Bell's theorem requires it of any
    single world of records with freely chosen settings.
  - Stating it plainly is part of the owner's decision.

## What this does not show

- **Seas.** No many-walker sea. Bell's own lattice model uses fermion number
  per site as the beable. How "one record per site" relates to Pauli
  occupation (two coin states per site) is open.
- **Formation.** No record formation. With number-conserving dynamics the
  records are conserved. "Records form" would need particle-creating terms,
  as in Bell-type field theories.
- **Uniqueness.** The rates are Bell's minimal choice, and other equivariant
  choices exist. Nothing here selects one.
- **Basis.** Position (site) is chosen as the beable by hand. For a free
  walker, the basis its dynamics keeps stable is momentum (the record-cost
  note's T4(h)). Interactions would have to make position the natural record
  basis.
- **Relativity.** The jump law uses a global time. Bell-type theories need a
  time slicing, and recover Lorentz invariance only in their statistics. On
  the tick surface of the one-light-cone note, the tick would be that
  slicing.

## Independent checks

To be recorded after the independent checks return (see the PR body).

## Reproduction

```bash
python3 scripts/records_as_beables_bells_jump_law_for_the_walker_2026_09_27.py
```

Expected: `TOTAL: PASS=6 FAIL=0` (about 1 minute).
