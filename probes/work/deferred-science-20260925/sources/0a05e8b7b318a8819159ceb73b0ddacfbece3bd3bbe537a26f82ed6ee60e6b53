---
claim_id: dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_gapped_majorana_fermions_in_a_static_z2_gauge_field_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "At the compass point of the fully soldered dynamics clause (open PR 9040), with records acting as fields (open PR 9041), both supplied and not adopted. Consider relaxed carvings: every unrecorded site has at most one unrecorded neighbour per axis, and each record is orthogonal to every axis along which its unrecorded neighbour keeps a bond. Their generator is quadratic in Majorana operators in every Z2 gauge sector, with fields along bondless (dangling) axes allowed. Two explicit networks on the 4x4x4 torus span all three lattice directions, and with generic record contents every dangling axis carries a field. (i) A 20-site network with one local loop per cell: its 20-qubit exact ground energy -26.0373871085 |K| equals the least free-Majorana energy over its 16 gauge classes; the local flux splits its translation-invariant sectors by 0.111388 |K| per cell; a single flipped local flux in a 2x2x2 supercell costs 0.11139 |K|; doubled cells find no lower pattern; and in the lowest sector two flat Majorana zero-mode bands per cell sit below a dispersive gap of 0.618 |K|. (ii) A 16-site network whose infinite lift is a tree: its loop operators are conserved; its exact ground energy -20.1928732905 |K| equals the least Majorana energy over all 2^18 gauge configurations; and all its flux sectors are degenerate, so its Z2 field is pure gauge. A SAT search finds 9 distinct three-direction networks, each gapped above 2 to 6 flat zero-mode bands per cell. The zero modes make the full spin model's ground state extensively degenerate. No global flux sector, topological classification, charge, chirality or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_2026_09_24.py
---

# Records carve exactly solvable three-dimensional Kitaev networks

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite results with explicit certificates, under supplied clauses; unaudited.

## Result and scope

Open PR 9048 found that at the compass point of the fully soldered
dynamics clause, records can carve the unrecorded medium into Kitaev's
exactly solvable model. There the carving was strict: one bond per axis at
every site, and no fields. In the complete enumerations searched, such
carvings were finite cubes or one-direction tubes.

Kitaev's solution tolerates more. A site may lack a bond along an axis,
which leaves a free Majorana `b^a`. A field along that same axis couples
`b^a` to the site's `c` Majorana, and the Hamiltonian stays quadratic. Only
a field along an axis where the site keeps its bond breaks solvability.

With this relaxation, records carve exactly solvable networks in three
dimensions.

- **Solvable in three dimensions, verified exactly.** Two explicit
  networks on the 4x4x4 torus span all three lattice directions. In each,
  the exact ground energy of the spin model equals the least free-Majorana
  ground energy over its gauge configurations.
  - The 20-site network is checked by matrix-free Lanczos on 20 qubits.
  - The 16-site network is checked over all `2^18` configurations.
- **A genuine Z2 flux.** The 20-site network has one local loop per cell.
  Its flux is gauge invariant:
  - flipping it in every cell costs `0.111 |K|` per cell;
  - flipping it in one cell of a 2x2x2 supercell costs `0.111 |K|`, a gapped
    vison;
  - no doubled cell finds a lower flux pattern.
- **Gapped matter above localized zero modes.** In the lowest sector the
  dispersive Majorana bands are gapped (`0.618 |K|`). Below them lie two
  flat zero-mode bands per cell. These are localized Majorana zero modes of
  the carved network, and they leave the full spin model's ground state
  extensively degenerate.
- **A tree is different.** The 16-site network has no local loop. Its
  infinite lift is a tree, every flux sector has the same energy, and its
  Z2 field is pure gauge. Its Majoranas are free fermions with no gauge
  content.
- **Not an accident.** A SAT search finds nine distinct three-direction
  networks. Each is gapped above 2 to 6 flat zero-mode bands per cell.

So qubits on `Z^3`, one covariant coupling and a pattern of records give,
exactly, a three-dimensional medium with:
- gapped emergent Majorana fermions;
- a static Z2 gauge field with gapped fluxes;
- a few localized zero modes per cell.

No fermion, grading or gauge structure is supplied.

**Correction to the first version of this PR.** Its headline network was
the 16-site network, described as a Majorana medium in a static Z2 gauge
field. That network's lift is a tree, so its Z2 field is pure gauge. Its
"no flat band" count also left out dangling Majoranas that the chosen
contents had decoupled. Both were found by our own catalogue and by an
independent check. The headline is now the 20-site network. Contents are
chosen so that no dangling Majorana is decoupled, and flat zero modes are
counted in the full model.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Lattice, Qubit and
  Record.
- **Supplied, not adopted.**
  - The fully soldered clause of open PR 9040 at its compass point,
    `H = K sum_bonds (e.s_x)(e.s_{x+e})`.
  - Records as fields: `K e (e.q)` on the unrecorded neighbour along `e`
    (open PR 9041).
- **Relaxed carving.** An unrecorded set `U` such that:
  - every site has at most one `U`-neighbour per axis;
  - wherever a site keeps its bond along axis `a`, the record on its other
    side along `a` has content orthogonal to `a`.

  An axis with no `U`-neighbour is *dangling*. A record is *constrained*
  along `a` when its `U`-neighbour keeps a bond along `a`. Such a content
  exists exactly when each record is constrained along at most two axes.
- **Generic contents.** The direction `(1, sqrt 2, sqrt 3)`, projected
  orthogonal to the record's constrained axes and normalised. Its
  components are positive, so the two records on a dangling axis never
  cancel, and every dangling axis carries a field.
- **Kitaev's representation** (a standard mathematical tool): `s^a = i b^a c`
  and bond variables `u_jk = i b^a_j b^a_k`. A loop operator is the product,
  over a cycle's sites, of the Pauli along the axis the cycle does not use
  there.
- **Local loops.** The cycles of a network's torus cell graph (cycle rank
  `beta1`) lift to paths whose displacements span the winding directions.
  The `beta1 - 3` cycles with zero displacement per cell are the local
  loops. Their flux is the gauge-invariant Z2 content of the infinite
  network.

## Theorem 1 — relaxed carvings are exactly solvable

*Statement.* For a relaxed carving, the record-projected generator on `U`
is

`K sum_bonds s^a_j s^a_k + sum_dangling h_{j,a} s^a_j`.

Every bond variable commutes with it. In each gauge sector it is the
quadratic Majorana operator

`sum_bonds K u_jk (i c_j c_k) + sum_dangling h_{j,a} (i b^a_j c_j)`,

up to the sign conventions of the runner.

*Proof.*
- Kept bonds see no field (open PR 9041), so only dangling fields remain.
- A dangling `b^a_j` belongs to no bond variable, so it commutes with
  every `u_jk`.
- A field along a kept axis contains that bond's `b` and does not commute.
  The runner shows such a field breaks loop operators. ∎

## Theorem 2 — two certificates

*Statement.* On the 4x4x4 torus:
- **The 20-site network** (sites listed in the runner) is a relaxed
  carving:
  - one component spanning three directions;
  - 23 bonds, cycle rank 4, one local loop per cell;
  - 14 dangling axes, all carrying fields under the generic contents.
- **The 16-site network** is a relaxed carving:
  - one component spanning three directions;
  - 18 bonds, cycle rank 3, no local loop;
  - 12 dangling axes, all carrying fields.

In both, every field along a kept bond is exactly zero.

*Proof.* Direct check in the runner. ∎

## Theorem 3 — exact solvability, verified

*Statement.*
- **The 20-site network.** The ground energy of the 20-qubit spin model,
  from matrix-free Lanczos, is `-26.0373871085 |K|`. It equals the least
  free-Majorana energy over the network's 16 gauge classes.
- **The 16-site network.**
  - The cycle-basis loop operators commute with the generator, including
    the dangling fields.
  - A field along one kept bond breaks two of them.
  - The ground energy `-20.1928732905 |K|` equals the least Majorana energy
    over all `2^18` gauge configurations.

*Proof.* Exact diagonalisation, and enumeration of gauge configurations. ∎

## Theorem 4 — the 20-site network: flux, visons and gapped matter

*Statement.*
- **Flux sectors.** The translation-invariant flux sectors have two
  energies per cell: `-26.036648 |K|`, and `-25.92526 |K|` with the local
  flux flipped. The local flux costs `0.111388 |K|` per cell.
- **The lowest sector.** It has exactly two flat zero-mode bands per cell.
  Above them the smallest `|eps|` is `0.61787 |K|` on a 16^3 grid.
- **Visons.** In a 2x2x2 supercell of the lowest sector, flipping any of
  the 32 bonds that lie on local loops costs `0.11139 |K|`. Flipping any of
  the other 152 costs exactly 0: those flips are gauge or winding changes.
- **Doubled cells.** Cells doubled along x, y or z (32 sectors each) reach
  no lower energy per cell.

*Proof.* Bloch and supercell diagonalisation of the Majorana matrix
(20 `c` operators plus 14 dangling `b` operators). ∎

The vison cost per flipped local flux equals the per-cell cost of flipping
it everywhere, to five digits. Within these supercells the fluxes do not
interact.

## Theorem 5 — the tree and the search

*Statement.*
- **The 16-site tree.** All 8 translation-invariant sectors of the 16-site
  network have the same energy (spread `7e-15`), as a tree requires. It has
  4 flat zero-mode bands per cell, with gap `1.437 |K|` above them.
- **The search.** A SAT search (python-sat) finds 9 distinct
  three-direction networks on 4x4x4. With generic contents, the lowest
  translation-invariant sector of each of the first eight is gapped above
  its flat zero-mode bands, with gaps `0.62` to `1.74 |K|`.

A wider exploratory scan, outside the runner, gives the same picture:
- 15 distinct networks across four torus shapes;
- random record contents;
- every network gapped above 2 to 6 structural flat zero-mode bands per
  cell;
- no gapless (nodal or Weyl) case found.

*Proof.* The runner reports the tree's sector spread, zero-mode count and
gap, and the search results. ∎

## Checks

The runner prints nine checks in four families. All pass in about four
minutes; most of that is the 20-qubit Lanczos.
- **A.** Two certificates, and their local-loop counts.
- **B.** Exact solvability for both networks.
- **C.** Flux splitting, visons, doubled cells, and the tree's degeneracy.
- **D.** The search.

Independent check, with separate code (see the PR thread), all under the
earlier content rule of this PR's first version:
- the 16-site certificate, its loop conservation, `ED = Majorana` over
  `2^18` (`-17.4885055277`), and its gap;
- the tree structure (cycles span the windings with determinant 1);
- the dangling zero-mode caveat.

The generic-content numbers and the 20-site computations have not been
checked independently.

## What this does not do

- **Flux sectors compared.** Only translation-invariant sectors, doubled
  cells and 2x2x2 supercells are compared. The global ground-state flux
  sector is not determined.
- **The zero modes are not removed.** They are not interpreted as
  particles. They leave the full spin model extensively degenerate.
  Perturbations that would lift them (`J`, `D`, other terms) are not
  treated.
- **No classification.** Nothing about statistics, topology or ground-state
  degeneracy on tori is claimed.
- **The emergent fermions are Majorana.** No U(1) charge, chirality or Weyl
  node is found.
- **Supplied inputs.** The carving and the contents are supplied. How
  records come to form this pattern is not addressed.
- **No physical reading.** Nothing identifies these objects with physical
  matter or forces.

## Decision points recorded

- The compass point of the fully soldered clause.
- The record pattern and its contents.

Neither is adopted.
