---
claim_id: records_as_beables_under_the_moving_records_reading_bells_jump_law_gives_nearest_neighbour_moves_equivariant_odds_and_bell_correlations_with_nonlocal_odds_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied reading, not adopted: the owner's moving-records reading (a record persists and moves between neighbouring sites), with a supplied guidance law for the memo's open 'physical persistence dynamics' gate. One record per walker, at a site; a unitary wave psi evolves by the walker's Hamiltonian and is never acted on by the records; a record at x moves to a neighbour y at Bell's minimal rate max(0, J_yx)/P(x), J_yx = 2 Im[psi_y^dag H_yx psi_x], with rate 0 where P(x) = 0 (joint configuration and joint wave for several walkers). (T1) For the walker sum_j sin k_j sigma_j in 1D, 2D and 3D the jump law's master equation equals the Schroedinger dP/dt exactly wherever P > 0 (equivariance), with nearest-neighbour jumps only; records distributed as |psi|^2 at one time stay so (the Born distribution is preserved, not derived). (T2) The rate table is covariant under the 24 proper cubic rotations (spin-1/2 coin action). (T3) The records do not act on psi (by construction), so the wave's energy is unaffected by their motion; no energy is assigned to records here. (T4) Two walkers on separate 24-site rings (a 1D comparator, not Z^3), singlet coins, local coin-rotation settings, the walker's own coin-steered motion, records sampled from |psi|^2 at t = 0: the records' outcomes reproduce the |psi|^2 correlations (Monte Carlo, 3000 histories per setting; CHSH 2.81 from records, 2.79 exact from |psi|^2) and, in quantum equilibrium, do not signal. (T5) The rates are nonlocal: after A's record has been steered right (left) with B frozen, B's instantaneous rate from its start site is 0.000 (0.562) to the right and 0.565 (0.000) to the left. Bell's theorem forces some nonlocal element in any single-world record law with free settings; it does not force this mechanism. No sea, no record creation, no interactions, no energy of records; rates not unique; global time."
upstream_dependencies:
  - minimal_axioms
  - dynamics_clause_bell_values_of_record_laws_records_only_formation_stays_at_two_the_dynamics_clause_reaches_two_root_two_bounded_theorem_note_2026-09-24
runner: scripts/records_as_beables_bells_jump_law_for_the_walker_2026_09_27.py
---

# Records as beables under the moving-records reading: Bell's jump law gives nearest-neighbour moves, equivariant odds and Bell correlations, with nonlocal odds

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** exact identities and Monte Carlo on small lattices; a supplied
reading; unaudited. Independent checks are recorded below.

## In one paragraph

Take the owner's picture: a record persists and moves between neighbouring
sites. Add one guidance law: a single wave, which the records never act on,
sets the odds for each move. Then the records keep the wave's statistics once
they have them. The records alone reproduce the Bell correlations, and in
equilibrium they cannot be used to signal. The price is where the odds come
from. They depend on the whole wave, so where one record may move depends on
where a distant record went. In the example here, once one record has gone
right, its partner can only go left. The moves are local; their odds are not.

## Why this question

The landed Bell note shows that records formed locally and causally from
records alone cannot reach the measured correlations. The record-cost note of
the same date shows what records cost if they collapse the quantum state one
site at a time. The panel convened on the viability map pointed to a reading
that avoids a collapse altogether: records as beables. That is John Bell's
1984 lattice model. The actual configuration is a set of records, a wave
guides them, and nothing ever collapses.

This note tests that reading on the campaign's walker, under the owner's
moving-records reading. The literature is reference only: Bell, "Beables for
quantum field theory" (1984); Dürr, Goldstein, Tumulka and Zanghì,
"Bell-type quantum field theories" (2005); Vink (1993), on the
non-uniqueness of the rates.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`), read in full. Two
  points of the memo matter here.
  - Its reading note 2: the Admissibility distribution "concerns which
    possibility a forming record locks, conditional on formation at that
    site".
  - It lists "physical persistence dynamics" as an open gate.
- **The owner's reading** (2026-09-20, not axiom text): records move
  between neighbouring sites when the neighbourhood allows, and a site holds
  at most one record at a time. Here "permanent" means the record persists;
  it does not mean it stays at one site.

  Under the stricter reading "a record stays at the site where it formed",
  a moving marker is not a Record, and this note does not apply.
- **Supplied, not adopted:**
  - **The wave.** `psi` evolves unitarily by the walker
    `H = sum_x sum_j [psi_x^dag (sigma_j/2i) psi_{x+e_j} + h.c.]`.
  - **The records.** One record per walker, at a site.
  - **The guidance law** (content for the persistence-dynamics gate). A
    record at `x` moves to a neighbour `y` at rate `max(0, J_yx)/P(x)`, with
    - `J_yx = 2 Im[psi_y^dag H_yx psi_x]`;
    - `P(x) = |psi_x|^2`;
    - rate 0 where `P(x) = 0`.

    For several walkers, `x` and `y` are joint configurations differing in
    one walker's site, and `psi` is the joint wave.
- **Readout** is from the records' positions. The possibility a record
  locks (its content, the Admissibility distribution) is not modelled here.

## T1 — equivariance

*Statement.* Wherever `P > 0`, the master equation
`dP(y)/dt = sum_x [rate(x->y) P(x) - rate(y->x) P(y)]` equals the Schrödinger
`dP(y)/dt`. So records distributed as `|psi|^2` at one time stay distributed
as `|psi|^2`. The Born distribution is preserved, not derived: the records
must start in it (quantum equilibrium). Every jump is between nearest
neighbours.

*Proof.*
- The continuity equation is `dP(y)/dt = sum_x J_yx`, with `J_xy = -J_yx`.
- `max(0, J_yx) - max(0, J_xy) = J_yx`. ∎

Whether the process exists globally near nodes of `psi` (non-explosion) is
not addressed. It is known to hold for Bell-type processes under mild
conditions (reference).

*Checks.* 1D (8 sites), 2D (`4^2`) and 3D (`3^3`), random waves: the
largest mismatch is `2.9e-17`. The independent referee's own implementation
gives `4.2e-17`, `2.8e-17` and `2.1e-17`.

## T2 — cubic covariance

The rate table of a wave rotated by a proper cubic rotation, with the
spin-1/2 action on the coin, is the rotated rate table.

All 24 rotations were checked on `3^3`: largest mismatch `2.7e-15`
(`2.2e-15` in the referee's implementation).

## T3 — the records do not act on the wave

By construction the records never change `psi`, so the wave's energy is
unaffected by their motion. The runner checks this over 400 steps: 9 record
moves, `|Delta <H>| = 6.9e-16`. This is bookkeeping, not a physical result.
No energy is assigned here to records or to their moving, writing or
reading.

What it does show: under this reading, the sharp lock whose cost the
record-cost note computes never happens. Nothing collapses.

(The setting rotations in T4 act on the wave from outside, as an apparatus
would, and do change `<H>`.)

## T4 — Bell correlations read from records

*Protocol.*
- Two walkers, each on its own 24-site ring. The rings are a 1D
  comparator, not the `Z^3` lattice.
- 1D walker `H = sin k sigma_z`: `σ_z = +1` moves right, `−1` moves left.
- Each position packet has amplitude `exp(-(x-12)^2/(2 x 1.5^2))`, so the
  probability width is `1.06` sites.
- Coins in the singlet. Each wing's setting is a coin rotation
  `exp(-i θ σ_y/2)`, applied at `t = 0`.
- Records are drawn from `|psi|^2` at `t = 0`.
- Joint evolution runs to `t = 8`. Records move by the guidance law, sampled
  in steps `dt = 0.02` with first-order jump probability `rate x dt`.
- Outcome: `+1` if the record's site is `>= 12`, `−1` otherwise.

*Result.* Settings `θ_A ∈ {0, pi/2}`, `θ_B ∈ {±pi/4}`, 3000 record histories
per pair:
- correlations from the records: `-0.696, -0.694, -0.709, +0.713`;
- from `|psi|^2`: `∓0.6977`, within 4σ;
- CHSH from the records: `2.81`; exact from `|psi|^2`: `2.79`. The
  referee's independent exact calculation gives `2.79078`.
- The gap to `2 sqrt 2` is packet overlap, and the value depends on the
  packet width: the referee finds `1.57` at probability width `0.5` and
  `2.55` at `2.0`.

The correlations come from the wave and the setting dynamics. The records
carry them because they are in quantum equilibrium.

*No signalling.* In quantum equilibrium it holds exactly: summing
`|psi(a,b)|^2` over `a` gives B's reduced statistics, which A's local
rotation cannot change. The sampled means of B's outcome
(`-0.001, -0.019` against `+0.003, +0.024`) are consistent with that. Outside
equilibrium, Bell-type rates can signal.

## T5 — the price: nonlocal odds

*Protocol.* The same state at `θ_A = 0`, `θ_B = pi/4`. A's wave evolves alone
for `t = 8` while B is frozen. Then B's instantaneous rate from its start
site is taken, weighted over A's record positions on each side.

| A's record | B's rate to the right | B's rate to the left |
|---|---|---|
| right of start | `0.000` | `0.565` |
| left of start | `0.562` | `0.000` |

(The referee's independent Gaussian toy gives `0.564` against `0`.)

The moves stay nearest-neighbour. Their odds depend on the joint wave, and so
on where a distant record is.

Bell's theorem, under its assumptions (a single world, freely chosen
settings, no retrocausation), requires some nonlocal element in any record
law that reproduces these correlations. It does not force this mechanism.
Other options with the same statistics:
- non-minimal equivariant rates;
- deterministic guidance;
- nonlocal collapse (the record-cost note prices its local version);
- global-boundary or retrocausal laws;
- superdeterminism, if free choice is dropped;
- many worlds, if a single world is dropped.

## What this means for the axioms

- Under the owner's moving-records reading, this reading of records keeps
  the owner's picture: records persist and move between neighbouring sites,
  one at a time. It adds no collapse, and so no lock.
- The dynamics clause becomes "Nothing is ever lost" (a unitary wave), plus
  a guidance law for records.
- The guidance law is content for the memo's open persistence-dynamics
  gate, not a re-reading of the Admissibility axiom.
  - Admissibility's clause concerns what a forming record locks (reading
    note 2), which this note does not model.
  - Motion's odds here are nonlocal.
  - An Admissibility-like rule that made motion's odds depend only on
    neighbouring records would, with a single world and free settings, stay
    within Bell's bound. That is the landed Bell note's result.
  - Adopting this reading therefore means accepting nonlocal odds for
    motion. That is an owner decision.

## What this does not show

- **Seas.** No many-walker sea. Bell's own lattice model uses fermion number
  per site. How "one record per site" relates to Pauli occupation is open.
- **Formation.** No record formation. Number-conserving dynamics conserves
  records, so "records form" needs particle-creating terms.
- **Energy.** No energy of records.
- **Content.** No link from the record's content (the `M_2(C)` possibility
  it locks) to the guidance law.
- **Uniqueness.** The rates are Bell's minimal choice, and other equivariant
  choices exist.
- **Basis.** The site is chosen as the beable by hand. For a free walker,
  the basis its dynamics keeps stable is momentum (the record-cost note's
  T4(h)).
- **Relativity.** The law uses a global time. Bell-type theories need a
  slicing, and recover Lorentz invariance only statistically.

## Independent checks

- **Codex `gpt-5.6-sol` referee**, at xhigh. Another vendor family; it read
  only the axioms memo and this note's first version.
  - **Verdict: "fails".** The mathematical core is sound. The identification
    with the framework's Records and Admissibility did not follow, and
    several physical conclusions were stronger than the calculation.
  - **Reproduced independently:** T1, T2, T4's exact correlations and the
    structure of T5.
  - **Applied in this revision:**
    - the reading is now declared as the owner's moving-records reading plus
      a supplied persistence-dynamics law, not the static "record stays at
      its site" reading;
    - Admissibility is no longer said to be re-read (the guidance law fills
      the persistence-dynamics gate);
    - "no record cost" is replaced by "does not act on the wave;
      bookkeeping";
    - Born statistics are preserved, not derived (quantum equilibrium);
    - the Bell protocol is fully specified, with its width dependence;
    - no-signalling is qualified to equilibrium;
    - the zero-node convention is stated;
    - "first-jump odds" is now "instantaneous rates";
    - Bell's theorem forces some nonlocal element, not this mechanism, and
      the alternatives are listed.
- **Claude Fable 5.1 subagent:** see the PR body.

## Reproduction

```bash
python3 scripts/records_as_beables_bells_jump_law_for_the_walker_2026_09_27.py
```

Expected: `TOTAL: PASS=6 FAIL=0` (about 1 minute).
