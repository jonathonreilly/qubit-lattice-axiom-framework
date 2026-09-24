---
claim_id: dynamics_clause_records_carve_kitaev_models_at_the_compass_point_zero_field_carvings_are_cubes_and_tubes_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "At the compass point (J = D = 0) of the fully soldered dynamics clause of open PR 9040, with records acting as fields (open PR 9041), both supplied and not adopted: if every unrecorded site has exactly one unrecorded neighbour along each axis (a carving) and every record touches the unrecorded set along at most two axes, contents orthogonal to those axes cancel every field. The unrecorded generator is then exactly Kitaev's bond-dependent model on the carved graph. Loop operators commute with it, and the exact ground energy equals the least free-Majorana ground energy over Z2 gauge configurations (checked on the cube and on 8- and 12-site periodic tubes). In the complete enumerations of zero-field carvings through a fixed site on the 4x4x4 and 5x5x5 tori (112 and 1984) and in 1500 samples on 6x6x6, every component is finite or winds in one direction. Without the zero-field requirement, components winding in three directions occur (32 sites on 4x4x4, 40 on 5x5x5), and each forces a record touching all three axes, whose field breaks loop operators. On the infinite staircase tube the least Majorana ground energy among translation-invariant flux sectors is at pi flux through both plaquette types, -3.35522 |K| per cell, with Majorana gap 2|K|; the zero-flux sector is gapless. No three-direction exactly solvable carving, no other flux configuration and no physical particle identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_carve_kitaev_models_at_the_compass_point_2026_09_24.py
---

# Records carve Kitaev models at the compass point

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite results and complete finite enumerations under supplied clauses; unaudited.

## Result and scope

Open PR 9040 found that full soldering allows three nearest-neighbour
couplings. One of them is the compass coupling
`K (e.s_x)(e.s_{x+e})`: a bond along an axis couples the two Pauli
components along that same axis. This is exactly the bond-dependent
coupling of Kitaev's exactly solvable model, with bond type equal to axis.
Kitaev's model needs each site to have exactly one bond of each type. On
the cubic lattice each site has two bonds per axis, so the bare compass
model is not of that form.

Records change the graph. By open PR 9041, a recorded neighbour acts as a
field and removes the bond from the unrecorded dynamics. This note asks
when records can carve the medium into a Kitaev model.

- **Exact reduction.** Suppose every unrecorded site keeps exactly one
  unrecorded neighbour along each axis, and every record's content is
  orthogonal to the axes along which it touches the unrecorded set. Then
  every field vanishes, and the unrecorded generator is exactly Kitaev's
  model on the carved graph.
- **Exactly solvable.** The loop operators commute with it. Its exact
  ground energy is a free-Majorana ground energy in a Z2 gauge sector.
  Checked on the cube and on periodic tubes of 8 and 12 sites.
- **Emergent content.** In each sector the carved medium is a set of
  Majorana fermions hopping in a static Z2 gauge field. That is fermions and
  a gauge field made of qubits, with no fermion or gauge structure
  supplied.
- **Where it applies.** The zero-field requirement is restrictive. In
  complete enumerations on the 4x4x4 and 5x5x5 tori, and in samples on
  6x6x6, every zero-field carving component is either finite (for example
  the 2x2x2 cube) or winds in one direction (a tube). Carvings that wind in
  all three directions exist, but each has a record touching the medium
  along all three axes. Such a record cannot cancel all its fields, and a
  field breaks loop operators.
- **A gapped tube.** The staircase tube is 2x2 plaquettes stacked with a
  one-row shift. Among translation-invariant flux sectors, its least
  Majorana ground energy has pi flux through every plaquette, and there the
  Majorana spectrum has a gap `2|K|`. The zero-flux sector is gapless.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Lattice, Qubit and
  Record as quoted in open PRs 9040 and 9041.
- **Supplied, not adopted.**
  - The fully soldered clause of open PR 9040 at `J = D = 0`:
    `H = K sum_bonds (e.s_x)(e.s_{x+e})`.
  - Records as fields: a record with content `q` on a bond along `e`
    exerts `K e (e.q)` on its unrecorded neighbour (open PR 9041).
- **Carving.** An unrecorded set `U` in which each site has exactly one
  `U`-neighbour along each axis.
  - It is **zero-field** when every recorded site touches `U` along at most
    two axes.
  - For a zero-field carving, a content orthogonal to the touched axes
    exists for each recorded site.
- **Winding rank.** The rank of the net displacements of the closed walks
  of a component, in the periodic lift of a torus: 0 for a finite
  component, 1 for a tube, 3 for a network spanning all directions.
- **Kitaev's representation.** `s^a = i b^a c` on each site, with bond
  variables `u_jk = i b^a_j b^a_k` (a standard mathematical tool). On a
  4-cycle the loop operator is the product, over its sites, of the Pauli
  along the bond that leaves the cycle.

## Theorem 1 — zero-field carvings are exactly Kitaev models

*Statement.* For a zero-field carving with the orthogonal contents, the
record-projected generator on `U` is `K sum_{bonds in U} s^a_j s^a_k`,
where `a` is the bond's axis, plus a constant. Every site has one bond of
each type. So this is Kitaev's model on the `U`-graph.

*Proof.* By open PR 9041, each bond to a record compresses to the field
`K e (e.q)`. That field is zero when `q` is orthogonal to `e`. A bond
between two records is a constant. The runner checks that the contents
cancel every field on the staircase tube and the cube: the largest residual
is exactly 0. ∎

## Theorem 2 — exact solvability, checked

*Statement.*
- On the cube (8 sites), and on the periodic staircase tubes of 8 and 12
  sites, the loop operators of all 4-cycles commute with the generator and
  with each other.
- The exact ground energy equals the least free-Majorana ground energy over
  all Z2 gauge configurations: `-4 sqrt 3 |K|` on the cube and on the
  8-site tube, and `-10.12899 |K|` on the 12-site tube.
- A field on one site of the cube breaks two of its six loop operators.

*Proof.* Loop operators and generators are built as sparse operators. The
exact ground energy comes from diagonalisation, and the Majorana ground
energy is `-(1/2)` times the sum of the positive eigenvalues of `iA`,
minimised over every gauge configuration: `2^12` for the cube, `2^18` for
the 12-site tube. They agree to `1e-9`. ∎

## Theorem 3 — which carvings have zero fields

*Statement.*
- **Complete enumerations.** On the 4x4x4 and 5x5x5 tori there are 112
  and 1984 zero-field carvings containing a fixed site. Every component of
  each is finite or winds in one direction, and one-direction tubes occur.
- **Samples.** 1500 zero-field carvings on 6x6x6 behave the same way.
- **Without the zero-field requirement.** 101 carvings found on 4x4x4 and
  5x5x5 have a component winding in all three directions (32 and 40
  sites). Each has a recorded site touching `U` along all three axes.

*Proof.* The carving and zero-field conditions are clauses for a SAT
solver (python-sat). Solutions are enumerated with blocking clauses until
the solver reports none, which makes the enumeration complete. Component
winding ranks come from breadth-first search in the periodic lift. The
runner reports the counts and ranks. ∎

This is a finite result on the stated tori. No general theorem excluding
zero-field networks that wind in two or three directions is claimed.

## Theorem 4 — the staircase tube is a gapped Z2 medium

*Statement.* The staircase tube has four sites per cell (a 2x2 plaquette)
and six bonds: two along `x`, two along `y` in the cell, and two along `z`
to the next cell. It has two plaquette types per cell. Among the four
translation-invariant flux sectors, the Majorana ground energy per cell is:
- `-3.35522 |K|` with pi flux through both plaquette types;
- `-3.05534 |K|` with pi flux through one;
- `-2.87198 |K|` with zero flux.

In the pi-flux sector the Majorana spectrum is gapped, with smallest
`|eps|` equal to `2|K|`. The zero-flux sector is gapless.

*Proof.* The Bloch Hamiltonian is diagonalised on a 4000-point
Brillouin-zone grid for all 64 translation-invariant gauge configurations.
Energies and gaps agree across configurations of the same fluxes, which
shows they are gauge invariant. ∎

The pi-flux preference matches Lieb's rule for 4-cycles, which is not used
as a premise. Non-translation-invariant flux configurations are not
compared.

## Checks

The runner prints nine checks in four families. All pass in about
eighteen seconds.
- **A.** The zero-field classification, and the three-direction networks
  with their forced records.
- **B.** Field cancellation.
- **C.** Loop commutation, the Majorana ground energies, and the loop
  operators broken by a field.
- **D.** Gauge invariance, the ground sector with its gap, and the gapless
  zero-flux sector.

## What this does not do

- It does not find an exactly solvable carving that winds in two or three
  directions. With nonzero fields, three-direction carvings are not
  exactly solvable in this sense. Their phases are not computed.
- It works at the compass point. The Heisenberg and Moriya couplings
  (`J`, `D`) break exact solvability. They are not treated.
- The carving, the contents and the sign of `K` are supplied.
- The emergent Majoranas are real fermions with a Z2 gauge field. No
  identification with charged matter, with the fermions of the matter notes
  or with a physical gauge field is claimed.

## Decision points recorded

- The compass point of the fully soldered clause.
- The record pattern (a carving) and its contents.

Neither is adopted. What this note shows is conditional: fermions and a
gauge field need not be supplied as such. Qubits, one covariant coupling
and a pattern of records produce them exactly, in finite clusters and
tubes.
