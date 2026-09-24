---
claim_id: dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_gapped_majorana_fermions_in_a_static_z2_gauge_field_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "At the compass point of the fully soldered dynamics clause (open PR 9040) with records acting as fields (open PR 9041), both supplied and not adopted, consider carvings in which every unrecorded site has at most one unrecorded neighbour per axis and every record is orthogonal to each axis along which its unrecorded neighbour keeps a bond. The unrecorded generator is then quadratic in Majorana operators in every Z2 gauge sector, with fields along bondless (dangling) axes allowed. An explicit 16-site network on the 4x4x4 torus is a single component whose closed walks span all three lattice directions, with 18 bonds, 12 dangling axes and 6 dangling fields. On its 16-qubit torus the cycle-basis loop operators commute with the generator, and the exact ground energy -17.4885055277 |K| equals the least free-Majorana ground energy over all 2^18 gauge configurations. On the infinite periodic network, the lowest of its 8 translation-invariant flux sectors has no flat zero band and Majorana gap 0.6091 |K| on a 16^3 grid. A SAT search finds 5 distinct three-direction components on 4x4x4 (16 to 22 sites), each gapped above its flat bands in its lowest translation-invariant sector. The global ground-state flux sector, topological classification, charge and physical identification are not claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_carve_exactly_solvable_three_dimensional_kitaev_networks_2026_09_24.py
---

# Records carve exactly solvable three-dimensional Kitaev networks

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite results, with an explicit certificate, under supplied clauses; unaudited.

## Result and scope

Open PR 9048 found that at the compass point of the fully soldered
dynamics clause, records can carve the unrecorded medium into Kitaev's
exactly solvable model. The carving there was strict: every unrecorded site
keeps exactly one bond per axis, and every record exerts no field. In the
complete enumerations it searched, such carvings were finite cubes or
one-direction tubes.

Kitaev's solution is more tolerant than that. A site may lack a bond along
some axis. That leaves a free Majorana operator `b^a`. A field along that
same axis couples `b^a` to the site's `c` Majorana, and the Hamiltonian
stays quadratic. The only fields that break solvability are those along
axes where the site keeps its bond.

With that relaxation the picture changes:
- **Three-dimensional networks exist.** An explicit 16-site network on the
  4x4x4 torus is one component whose closed walks span all three lattice
  directions. Every one of its records can be given a content that exerts
  no field along any kept bond.
- **Exactly solvable, and checked.** On its 16-qubit torus:
  - the loop operators of a cycle basis commute with the generator,
    including the dangling fields;
  - the exact ground energy, `-17.4885055277 |K|`, equals the least
    free-Majorana ground energy over all `2^18` Z2 gauge configurations.
- **A gapped Majorana medium in three dimensions.** On the infinite
  periodic network, the lowest translation-invariant flux sector has a
  gapped Majorana spectrum, with gap `0.609 |K|` and no flat zero band.
- **Not an accident.** A SAT search finds five distinct three-direction
  networks on 4x4x4. In each, the lowest translation-invariant sector is
  gapped above any flat bands.

So from qubits on `Z^3`, one covariant coupling and a pattern of records,
the unrecorded medium becomes exactly a three-dimensional system of massive
Majorana fermions coupled to a static Z2 gauge field. No fermion, grading
or gauge structure is supplied.

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
  - wherever a site `u` keeps its bond along axis `a`, the recorded
    neighbour of `u` along `a` has content orthogonal to `a`. Such a content
    exists exactly when each record has at most two such axes.

  An axis along which `u` has no `U`-neighbour is *dangling*. Fields along
  it are allowed.
- **Kitaev's representation** (a standard mathematical tool). Each site
  has four Majorana operators with `s^a = i b^a c`, and bond variables are
  `u_jk = i b^a_j b^a_k`. A loop operator is the product, over a cycle's
  sites, of the Pauli along the axis the cycle does not use there.
- **Winding rank.** The rank of the net displacements of closed walks of a
  component in the periodic lift. Rank 3 means the network spans all three
  directions.

## Theorem 1 — relaxed carvings are exactly solvable

*Statement.* For a relaxed carving, the record-projected generator on `U`
is

`K sum_{bonds} s^a_j s^a_k + sum_{dangling (j, a)} h_{j,a} s^a_j`.

Every bond variable `u_jk` commutes with it. In each gauge sector it
equals the quadratic Majorana operator

`sum_bonds K u_jk (i c_j c_k) + sum_dangling h_{j,a} (i b^a_j c_j)`,

up to the sign conventions fixed in the runner.

*Proof.*
- A kept bond's recorded partner exerts no field (open PR 9041), so only
  dangling fields remain.
- A dangling `b^a_j` belongs to no bond variable. So `h s^a_j = h i b^a_j c_j`
  commutes with every `u_jk`.
- A field along a kept axis contains the `b` of that bond and would not
  commute with it. The runner shows such a field breaks loop operators. ∎

## Theorem 2 — a certificate in three dimensions

*Statement.* The 16 sites
(0,0,2) (0,1,1) (0,1,2) (0,2,1) (1,1,2) (1,1,3) (2,0,3) (2,1,0)
(2,1,3) (2,2,0) (3,0,2) (3,0,3) (3,2,0) (3,2,1) (3,3,1) (3,3,2)
of the 4x4x4 torus form a relaxed carving:
- at most one neighbour per axis, degrees 2 and 3;
- one component of winding rank 3;
- 18 bonds and 12 dangling axes.

Each record takes the last axis not constrained by a kept bond. These
contents cancel the field along every kept bond and leave nonzero fields
on 6 dangling axes.

*Proof.* Direct check in the runner. ∎

## Theorem 3 — exact solvability, verified on the 16-qubit torus

*Statement.* On the finite 16-qubit torus of Theorem 2:
- the three loop operators of a cycle basis commute with the generator,
  including the dangling fields;
- adding a field along one kept bond breaks two of them;
- the exact ground energy is `-17.4885055277 |K|`, equal to the least
  free-Majorana ground energy over all `2^18` gauge configurations.

*Proof.* Sparse diagonalisation, and enumeration of every gauge
configuration of the finite graph. ∎

## Theorem 4 — a gapped Majorana medium in three dimensions

*Statement.* On the infinite periodic network of Theorem 2, the 8
translation-invariant flux sectors are those of the 3 non-tree bonds per
cell. The sector of least Majorana ground energy per cell
(`-17.4858 |K|`, shared by a partner sector) has:
- no flat zero band;
- smallest `|eps| = 0.6091 |K|` on a 16^3 Brillouin-zone grid.

*Proof.* Bloch diagonalisation of the `22 x 22` Majorana matrix (16 `c`
operators plus 6 coupled dangling `b` operators) at every grid point. ∎

## Theorem 5 — five distinct networks, all gapped

*Statement.* A SAT search (python-sat) for relaxed carvings on 4x4x4, with
every unrecorded site keeping at least two bonds, finds 5 distinct
components of winding rank 3, with 16, 19, 20, 22 and 22 sites. With the
same content rule, the lowest translation-invariant sector of each is
gapped above its flat bands, with gaps `0.609, 0.788, 1.146, 0.306, 0.776
|K|` on a 6^3 grid.

*Proof.* The runner enumerates the SAT solutions, extracts rank-3
components, and diagonalises each sector. Some networks keep a few flat
zero bands. Those are Majorana zero modes tied to dangling axes, and the
gap is measured above them. ∎

## Checks

The runner prints six checks in four families. All pass in about 13
seconds.
- **A.** The carving certificate, and the field cancellation.
- **B.** Loop conservation with its negative control, and exact
  diagonalisation equal to the Majorana minimum.
- **C.** The band gap of the infinite network.
- **D.** The five networks.

An independent checker with separate code reproduced the Majorana
construction and ground energies of the strict carvings of open PR 9048,
and their complete enumeration. The three-dimensional results of this note
have not yet been checked independently.

## What this does not do

- **Only translation-invariant flux sectors on the given cell are
  compared.** The global ground-state sector is not determined.
- **No classification.** No topological classification is made, and no
  statistics or braiding of excitations are computed.
- **The emergent fermions are Majorana and gapped.** No U(1) charge,
  chirality or gapless (Weyl) case is found. None is claimed.
- **Exact solvability needs the pure compass point.** The Heisenberg and
  Moriya couplings are not treated.
- **Supplied inputs.** The carving and the record contents are supplied.
  How records come to form this pattern is not addressed.
- **No physical reading.** Nothing identifies these fermions or this
  gauge field with physical matter or forces.

## Decision points recorded

- The compass point of the fully soldered clause.
- The record pattern and its contents.

Neither is adopted. What is shown is that a three-dimensional system of
fermions coupled to a gauge field can be exactly the dynamics of qubits,
records and one covariant coupling.
