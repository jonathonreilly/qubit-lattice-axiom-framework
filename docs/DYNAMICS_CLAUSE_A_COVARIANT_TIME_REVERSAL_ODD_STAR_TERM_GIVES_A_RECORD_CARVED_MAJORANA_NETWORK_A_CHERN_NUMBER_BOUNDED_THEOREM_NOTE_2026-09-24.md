---
claim_id: dynamics_clause_a_covariant_time_reversal_odd_star_term_gives_a_record_carved_majorana_network_a_chern_number_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: the compass point of the fully soldered dynamics clause (open PR 9040), records acting as fields (open PR 9041), a record carving with record contents, and a covariant time-reversal-odd star term. (i) A 19-site relaxed three-direction network on the 4x4x4 cell (from open PR 9097's zero-field search) has no record touching unrecorded sites along all three axes. Each record points along the last axis that avoids its unrecorded neighbours, with sign (-1)^(x+y+z), so every field on an unrecorded site vanishes. (ii) Covariant odd star terms under full soldering, built as signed orbits of the 24 proper rotations, span 37 dimensions at weights 1 and 3 (matching open PR 9088) and 325 at weights 1, 3, 5 and 7. (iii) Pauli strings on the carving, with records replaced by their values, are mapped exactly to Kitaev's Majoranas, inserting the physical constraint where needed. The map reproduces the network's bond matrix, and on three-site clusters with bonds, Kitaev's pattern and dangling fields the spin spectrum equals one parity sector of the Majorana spectrum to 5e-15. (iv) The covariant terms whose every reduced string is a free Majorana bilinear form a 41-dimensional subspace on this carving. The projection onto it of the weight-5 orbit s^x_{+x} s^y_{-x} s^y_{+y} s^z_{-y} s^z_{+z} (five neighbours of a centre) is a covariant term of weights 5 and 7. Its non-free reduced strings cancel exactly (1e-15), and its free ones include 27 same-class bilinears. (v) The compass-point bonds plus lambda times that term, at lambda = 1, 2 and 4: the lowest flux sectors, 8 of 16 and degenerate, each have 12 exact zero modes per cell and a gap above them (0.019, 0.035, 0.017). Their weak Chern numbers are (-1, 0, 0) on four k_x planes, and 0 on the k_y and k_z planes checked. (vi) On a slab 12 cells thick, open along z (lambda = 2, k_x = 1), the in-gap states sit on the surfaces, and as k_y winds once they cross energies -0.01 and 0.01 once upward on the top surface and once downward on the bottom: one chiral Majorana mode per surface. So covariant ingredients give the carved Majoranas a Chern number: record values supply the orientation signs that covariance denies Kitaev's weight-3 pattern. The term and the carving are specific: freeness depends on the carving and its record contents. The zero modes leave the spin model's ground state extensively degenerate, the gap is small, and (vii) the phase needs exactly zero dangling fields: dangling fields of 0.1 couple the 12 zero modes in and remove the Chern number, and with generic record contents no covariant odd star term stays free on this carving. No charged or Weyl fermion, no chiral phase of the full lattice and no physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_covariant_star_term_gives_carved_majoranas_a_chern_number_2026_09_24.py
---

# A covariant time-reversal-odd star term gives a record-carved Majorana network a Chern number

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied decision points; unaudited.

## Result

The chirality lane of this campaign had reached a precise gap.
- Open PR 9088 found no covariant time-reversal-odd star term of weight at
  most three that keeps a carving's Majoranas free.
- Open PR 9097 found that record fields keep the carved Majoranas
  sublattice-symmetric, so they give no Chern number.
- It also found that a gapless start plus Kitaev's pattern gives a Chern
  number, but that pattern is not covariant.
- No covariant weight-three term, reduced by records, gives the needed
  same-class coupling.

This note finds the missing ingredient at higher weight.
- **The ingredient exists.** Covariant odd star terms of weight 5 and 7,
  with their factors on recorded sites replaced by the record values,
  reduce on a realizable carving to free Majorana bilinears, including
  same-class ones. Their Majorana images include Kitaev's pattern at the
  carving's corners. The record values carry the orientation signs that
  covariance denies the weight-three pattern.
- **It makes the Majoranas chiral.** One such term, added to the
  compass-point bonds, opens a gap with weak Chern numbers `(−1, 0, 0)`.
  - This holds in every lowest flux sector, at `λ = 1, 2` and 4.
  - The chiral bands sit above 12 decoupled zero modes per cell.
  - A slab shows one chiral Majorana mode on each surface, with opposite
    chirality.

So a star term, one Admissibility neighbourhood wide, plus realizable
records gives the carved medium chiral Majorana bands. Every ingredient is
covariant under full soldering. This is the first chiral content the
campaign has found from covariant ingredients.

## Setting and decision points

- **The clause.** The compass point of the fully soldered clause (open PR
  9040; D-dyn, D-sold), with records acting as fields (open PR 9041).
- **The carving (D-pattern).** A 19-site relaxed network on the 4x4x4 cell,
  spanning all three directions, from open PR 9097's zero-field search:

      (0,0,0) (0,0,1) (0,1,0) (0,1,3) (0,2,3) (1,0,1) (1,0,2) (1,1,2)
      (1,1,3) (1,3,1) (2,1,2) (2,2,1) (2,2,2) (2,3,0) (2,3,1) (3,0,0)
      (3,2,3) (3,3,0) (3,3,3)

  It has 22 bonds, one local loop per cell and three windings.
- **The record contents (D-pattern).**
  - Each record points along the last axis that avoids its unrecorded
    neighbours. That is possible because none touches them along all three
    axes.
  - Its sign is `(−1)^(x+y+z)`, staggered.
  - Every field on an unrecorded site vanishes.
- **The star term (D-chir, extended to weight at most seven).** A covariant
  odd star term under full soldering: a sum over lattice sites of Pauli
  strings on the site and its six neighbours, invariant under the 24 proper
  rotations acting on positions and spins together.
- **Kitaev's representation** (prior art: Kitaev 2006).
  - `σ^a = i b^a c`, with the physical constraint `b^x b^y b^z c = 1`.
  - So `σ^a = −i b^{a+1} b^{a+2}` on the physical space.
  - Bonds pair into gauge fields, `b_j b_k = −i u_jk`.

None is adopted.

## Theorem 1 — the carving and its zero-field records

The network is connected with winding rank 3, and keeps at most one bond
per axis at each site. Every record touches unrecorded sites along at most
two axes. With the stated contents, the field of every record on every
unrecorded neighbour, `q_r^a` along the bond axis `a`, is exactly 0. ∎

## Theorem 2 — covariant odd star terms as signed orbits

Under full soldering a proper rotation maps a Pauli string on the star to
plus or minus another. So the covariant terms are the orbit sums with
consistent signs, and an orbit whose stabilizer reverses a sign vanishes.
The runner builds them directly:
- weights 1 and 3 give 37 dimensions, open PR 9088's full-soldering count;
- weights 1, 3, 5 and 7 give 325. ∎

## Theorem 3 — exact Majorana images

For each Pauli string on the carving, the runner inserts the physical
constraint on a subset of its sites and pairs every `b` on a kept bond with
its partner. What remains is a free term if at most two Majoranas are left:
`c`'s and dangling `b`'s. The runner tracks every sign.
- **Bonds.** The map reproduces the network's bond matrix exactly.
- **Clusters.** On 12 random three-site clusters, the spin spectrum equals
  one parity sector of the Majorana spectrum to 5e-15. Each cluster has
  bonds, Kitaev's pattern with a random coefficient, and random dangling
  fields.
- **Free and not free.** Kitaev's pattern is a free same-class bilinear. A
  kept-axis field is not free. ∎

## Theorem 4 — a covariant term with same-class images

Place every covariant term at every lattice site, and replace its factors on
recorded sites by the record values.
- **The free subspace.** The terms whose reduced strings are all free form
  a 41-dimensional subspace of the 325.
- **The term.** Project onto it the orbit of the weight-5 string
  `σ^x_{+x} σ^y_{−x} σ^y_{+y} σ^z_{−y} σ^z_{+z}`, on five neighbours of a
  centre. The projection is a covariant term built from 23 orbits of
  weights 5 and 7.
  - Its non-free reduced strings cancel exactly, to 1e-15.
  - Its free reduced strings include 27 same-class bilinears. These are
    Kitaev's pattern at corners of the carving, with coefficients fixed by
    the record values. ∎

## Theorem 5 — the chiral phase

Add `λ` times that term to the compass-point bonds. In each of the 16 flux
sectors the model is free Majoranas; the sector energy includes the term's
pure-gauge parts.

| `λ` | lowest sectors | next sector | zero modes per cell | gap above them | weak Chern numbers |
|---|---|---|---|---|---|
| 1 | 8 of 16 | +0.0120 | 12 | 0.0190 | (−1, 0, 0) |
| 2 | 8 of 16 | +0.0242 | 12 | 0.0351 | (−1, 0, 0) |
| 4 | 8 of 16 | +0.0388 | 12 | 0.0174 | (−1, 0, 0) |

Details of the table:
- The Chern number on planes normal to `x` is −1 in every lowest sector.
- In the first lowest sector it is −1 on four `k_x` planes, and 0 on four
  `k_y` and four `k_z` planes.
- The gaps are refined minima over the Brillouin zone of the bands above
  the exact zero modes.

So the gapped bands carry a weak Chern number. ∎

## Theorem 6 — chiral surface modes

Cut the lattice into a slab 12 cells thick, open along `z`, at `λ = 2` in
the first lowest sector, and keep `k_x = 1` and `k_y` as good momenta. Scan
`k_y` over 121 values.
- **Localization.** The in-gap states, between the zero modes and 0.8 of the
  bulk gap, sit on the two surfaces: 64 top-surface and 31 bottom-surface
  states against 4 others.
- **Chirality.** As `k_y` winds once, the top-surface states cross the
  energies −0.01 and 0.01 once each, upward. The bottom-surface states cross
  them once each, downward.

So each surface carries one chiral Majorana mode, with opposite chirality
on the two. That is what a Chern number of magnitude 1 in the `k_x`
planes requires. ∎

## Theorem 7 — the phase needs zero dangling fields

The 12 zero modes per cell sit entirely on dangling `b` Majoranas, which
the zero-field records leave decoupled.
- **Adding dangling fields.** Give every dangling axis a field of size
  about 0.1 through the clause, with random signs, and keep the star term
  as reduced by the zero-field contents. That couples the `b`'s in, and 2
  exact zero modes per cell remain. The negative bands' Chern number on
  the `k_x` planes becomes 0.
- **Generic contents.** Open PR 9054's generic contents, a fixed direction
  projected orthogonal to kept axes, leave fields on the dangling axes.
  With them, no covariant odd star term of weight at most seven stays free
  on this carving: the free dimension is 0.

So the chiral phase needs the zero-field contents. They are realizable,
but they are a fine-tuned choice among record contents. ∎

## Exploratory scans, not certified here

- **The route into the phase.** At `λ = 0` the zero-field network is gapped
  (0.78, above 16 zero modes) and non-chiral.
  - Between `λ = 0.1` and 0.8 the gap vanishes somewhere. The `k_x = π`
    plane already has Chern number −1 while `k_x = 0` has 0.
  - At `λ = 0.5` the dispersive gap vanishes on every `k_x` slice from 0.39
    to 2.36. So the zero-energy set spreads over a range of `k_x`, as a
    Majorana Fermi surface would, not at isolated Weyl points.
  - From `λ = 0.9` the phase is gapped with `(−1, 0, 0)`, as the
    certified window at 1 to 4 shows.
- **Other carvings.** A coarse-grid survey covered the 16 realizable
  networks of open PR 9097, under four coherent record rules, with every
  single-orbit projection at `λ = 2`. It found candidates with nonzero
  plane Chern numbers on 5 networks. Refined checks of several showed a
  gap that vanishes somewhere, with Chern numbers that differ between
  planes. The 19-site case here is the one verified fully gapped.

## What this means for the lanes

- **Chirality lane.** Covariant ingredients now give chiral Majorana bands.
  They are:
  - the soldered compass clause;
  - a realizable carving with zero-field, staggered records;
  - a covariant star term of weight 5 and 7.

  The record values carry the orientation signs that covariance denies
  Kitaev's weight-three pattern.
- **The ladder of the synthesis.** Time-reversal-odd chiral content needs a
  star term of weight at least five under soldering, plus a zero-field
  carving. That is one Admissibility neighbourhood, like the photon's ring.
- **What stays open.**
  - The chiral fermions here are neutral Majoranas in a Z2 gauge field, not
    charged Weyl fermions.
  - The spin model's ground state is extensively degenerate, from the 12
    decoupled zero modes per cell.
  - The gap is small, 0.02 to 0.035 of `|K|`.
  - The term is one member of a carving-specific free subspace.
  - The phase needs exactly zero dangling fields. Records tilted to give
    fields of 0.1 remove the Chern number (Theorem 7).
- **Prior art.**
  - Kitaev (2006): a time-reversal-odd three-spin term gaps his model into
    a chiral phase.
  - Hermanns, O'Brien and Trebst (2015): three-dimensional Kitaev models
    with Majorana Weyl nodes and chiral surface modes.

  Both are cited as prior art, not as premises.

## Checks

The runner has 7 checks and all pass in about a minute.

| Check | Result |
|---|---|
| The carving | Connected, winding rank 3, 22 bonds; records touch at most 2 axes; largest field on an unrecorded site 0. |
| Covariant terms | 37 at weights 1 and 3 (open PR 9088's count), 325 at weights 1 to 7. |
| Majorana images | Bond matrix exact; 12 three-site clusters match the spin spectrum to 5e-15. |
| The term | Free subspace 41; projected term uses 23 orbits of weights 5 and 7; non-free strings cancel to 1e-15; 27 same-class free bilinears. |
| The chiral phase | The table above. |
| Surface modes | 12-cell slab open along `z`: 64 top and 31 bottom in-gap surface states, 4 others; signed crossings of ±0.01, top +1, bottom −1. |
| Zero fields needed | Zero modes all on dangling `b`'s; with dangling fields of 0.1, 2 zero modes per cell remain and the Chern numbers on two `k_x` planes are 0; with generic contents the free covariant dimension is 0. |

## What this does not do

- It adopts no clause, carving, record content or star term.
- It treats one carving, one assignment of record contents and one covariant
  term.
- It claims no chiral phase of the full lattice. The carving and its
  records are a supplied pattern.
- It claims no charged or Weyl fermion or physical identification.
