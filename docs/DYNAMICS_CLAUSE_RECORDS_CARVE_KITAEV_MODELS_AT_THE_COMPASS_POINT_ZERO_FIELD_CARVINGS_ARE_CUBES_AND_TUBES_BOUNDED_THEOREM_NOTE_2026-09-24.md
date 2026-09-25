---
claim_id: dynamics_clause_records_carve_kitaev_models_at_the_compass_point_zero_field_carvings_are_cubes_and_tubes_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "At the compass point (J = D = 0) of the fully soldered dynamics clause of the linked companion construction, with records acting as fields (the linked companion construction), both supplied and not adopted: if every unrecorded site has exactly one unrecorded neighbour along each axis (a carving) and every record touches the unrecorded set along at most two axes, contents orthogonal to those axes cancel every field. The unrecorded generator is then exactly Kitaev's bond-dependent model on the carved graph. Loop operators commute with it, and finite numerical spin ground energies agree with the least auxiliary Majorana ground energy over Z2 gauge configurations (checked on the cube and on 8- and 12-site periodic tubes). On every torus with all sides at least 3, every component of a zero-field carving is either the 2x2x2 cube or a strip one square wide that winds along a face diagonal. At least two of each carved site's three partner squares are closed. The carved sites, partner bonds and closed squares form a surface with Euler characteristic (number of interior sites)/4 >= 0. An interior site forces a closed unit cube, and a strip without interior sites that does not wind would need a reversal, which completes a third square. The complete enumerations through a fixed site on the 4x4x4 and 5x5x5 tori (112 and 1984), and samples on 6x6x6, agree: every finite component found is the 2x2x2 cube, and every winding component is such a strip. Without the zero-field requirement, components winding in three directions occur (32 sites on 4x4x4, 40 on 5x5x5), and each forces a record touching all three axes, whose field breaks loop operators. On the infinite staircase tube the least Majorana ground energy among translation-invariant flux sectors is at pi flux through both plaquette types, -3.35522K (for K>0) per cell, with Majorana gap 2K (for K>0); the zero-flux sector is gapless. No three-direction exactly solvable carving, no other flux configuration and no physical particle identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_carve_kitaev_models_at_the_compass_point_2026_09_24.py
---

# Records carve Kitaev models at the compass point

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** finite numerical results, a general theorem on zero-field carvings, and complete finite enumerations under supplied clauses; unaudited.

## Result and scope

the linked companion construction found that full soldering allows three nearest-neighbour
couplings. One of them is the compass coupling
`K (e.s_x)(e.s_{x+e})`: a bond along an axis couples the two Pauli
components along that same axis. This is exactly the bond-dependent
coupling of Kitaev's exactly solvable model, with bond type equal to axis.
Kitaev's model needs each site to have exactly one bond of each type. On
the cubic lattice each site has two bonds per axis, so the bare compass
model is not of that form.

Records change the graph. By the linked companion construction, a recorded neighbour acts as a
field and removes the bond from the unrecorded dynamics. This note asks
when records can carve the medium into a Kitaev model.

- **Exact reduction.** Suppose every unrecorded site keeps exactly one
  unrecorded neighbour along each axis, and every record's content is
  orthogonal to the axes along which it touches the unrecorded set. Then
  every field vanishes, and the unrecorded generator is exactly Kitaev's
  model on the carved graph.
- **Exactly solvable.** The loop operators commute with it. Its spin ground energy is compared numerically with the auxiliary gauge-sector minimum for the listed finite cases.
  Checked on the cube and on periodic tubes of 8 and 12 sites.
- **Emergent content.** In each sector the carved medium is a set of
  Majorana fermions hopping in a static Z2 gauge field. That is fermions and
  a gauge field made of qubits, in an imported auxiliary Clifford representation, with physical projection constraints still required.
- **Where it applies.** The zero-field requirement is restrictive, and
  this is now a theorem (Theorem 3, parts 2 and 3). A zero-field carving
  is a surface of nonnegative curvature. Every component is either the
  2 x 2 x 2 cube or a strip one square wide winding along a face diagonal (a
  tube). The
  enumerations on the 4 x 4 x 4 and 5 x 5 x 5 tori, and samples on 6 x 6 x 6, find
  only 2 x 2 x 2 cubes and such strips. Carvings that wind in
  all three directions exist, but each has a record touching the medium
  along all three axes. Such a record cannot cancel all its fields, and a
  field breaks loop operators.
- **A gapped tube.** The staircase tube is 2 x 2 plaquettes stacked with a
  one-row shift. Among translation-invariant flux sectors, its least
  Majorana ground energy has pi flux through every plaquette, and there the
  Majorana spectrum has a gap `2K (for K>0)`. The zero-flux sector is gapless.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Lattice, Qubit and
  Record as quoted in the linked companion construction.
- **Supplied, not adopted.**
  - The fully soldered clause of the linked companion construction at `J = D = 0`:
    `H = K sum_bonds (e.s_x)(e.s_{x+e})`.
  - Records as fields: a record with content `q` on a bond along `e`
    exerts `K e (e.q)` on its unrecorded neighbour (the linked companion construction).
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

*Proof.* By the linked companion construction, each bond to a record compresses to the field
`K e (e.q)`. That field is zero when `q` is orthogonal to `e`. A bond
between two records is a constant. The runner checks that the contents
cancel every field on the staircase tube and the cube: the largest residual
is exactly 0. ∎

## Theorem 2 — exact solvability, checked

*Statement.*
- On the cube (8 sites), and on the periodic staircase tubes of 8 and 12
  sites, the loop operators of all 4-cycles commute with the generator and
  with each other.
- The finite numerical spin ground energy agrees with the least auxiliary Majorana ground energy over
  all Z2 gauge configurations: `-4 sqrt(3) K` for K>0 on the cube and on the
  8-site tube, and `-10.12899 K` for K>0 on the 12-site tube.
- A field on one site of the cube breaks two of its six loop operators.

*Proof.* Loop operators and generators are built as sparse operators. The
numerical ground energy comes from diagonalisation, and the Majorana ground
energy is `-(1/2)` times the sum of the positive eigenvalues of `iA`,
minimised over every gauge configuration: `2^12` for the cube, `2^18` for
the 12-site tube. They agree to `1e-9`. ∎

## Theorem 3 — which carvings have zero fields

**Part 1 — enumerations.**
- **Complete enumerations.** On the 4 x 4 x 4 and 5 x 5 x 5 tori there are 112
  and 1984 zero-field carvings containing a fixed site. Every component of
  each is finite or winds in one direction, and one-direction tubes occur.
- **Samples.** 1500 zero-field carvings on 6 x 6 x 6 behave the same way.
- **Without the zero-field requirement.** 101 carvings found on 4 x 4 x 4 and
  5 x 5 x 5 have a component winding in all three directions (32 and 40
  sites). Each has a recorded site touching `U` along all three axes.

*Proof.* The carving and zero-field conditions are clauses for a SAT
solver (python-sat). Solutions are enumerated with blocking clauses until
the solver reports none, which makes the enumeration complete. Component
winding ranks come from breadth-first search in the periodic lift. The
runner reports the counts and ranks. ∎

**Part 2 — the general theorem.** On any torus with all sides at least 3,
every component of a zero-field carving winds in at most one direction. A
component that winds is a strip one square wide.

*Proof.*
- **Partner squares.** Let `u` be a carved site. Its partner along axis
  `a` is `w_a = u + σ_a e_a`, the unique carved neighbour along that axis.
  - For two axes `a, b`, the partner square is
    `{u, w_a, w_b, u + σ_a e_a + σ_b e_b}`. Call it closed when its fourth
    corner is carved.
  - If it is closed from one corner, it is closed from all four, and its
    edges are partner bonds. That corner's partners along `a` and `b` are
    `w_b` and `w_a`, since each is its unique carved neighbour along that
    axis.
- **Two squares at every site.** Let `r = u − σ_a e_a`, the recorded site
  behind `u` along `a`. It touches `U` along `a`.
  - Suppose both squares of `u` that contain axis `a` are open. Then `w_b`'s
    partner along `a` is `w_b − σ_a e_a = r + σ_b e_b`, so `r` touches `U`
    along `b`. Likewise it touches `U` along `c`.
  - Then `r` touches all three axes, which the zero-field condition
    forbids.
  - So for each axis, one of the two squares containing it is closed, and
    at least two of `u`'s three squares are closed.
- **A surface.** Every partner bond lies in one or two closed squares.
  Every site lies in two squares (its neighbourhood is a path: a boundary
  site) or three (a triangle: an interior site). So the carved sites,
  partner bonds and closed squares form a surface with boundary.
- **Counting.** A component with `N` sites, `N_int` of them interior, has
  `3N/2` bonds and `(3 N_int + 2 (N − N_int))/4` squares. Its Euler
  characteristic is `χ = N_int / 4 ≥ 0`.
- **Winding.** Displacements of closed walks factor through the surface's
  first homology, because square boundaries have zero displacement.
  - Compact surfaces with `χ ≥ 0` are:
    - the sphere, disk and projective plane, whose first homology has
      rank 0;
    - the annulus, Möbius band, torus and Klein bottle, with `χ = 0`.
  - A torus or Klein bottle has no boundary, so `N_int = N` and
    `χ = N/4 > 0`, a contradiction.
  - A winding component is therefore an annulus or Möbius band with
    `χ = 0`, so `N_int = 0`. Every site lies in exactly two squares: a
    strip one square wide, with first homology of rank 1.
  ∎

**Part 3 — the complete classification.** Every component of a zero-field
carving is either the 2 x 2 x 2 cube or a strip one square wide that winds
along a face diagonal.

*Proof.*
- **An interior site forces a cube.** Suppose `u` is interior, with all
  three partner squares closed. Its body corner
  `b = u + σ_x e_x + σ_y e_y + σ_z e_z` then has a carved neighbour along
  each axis: the three face corners. If `b` were recorded, it would touch
  `U` along three axes, which zero field forbids. So `b` is carved.
  - All eight corners of the unit cube are then carved.
  - Each corner has a carved neighbour along each axis inside the cube, and
    only one along each axis at all. So all its partners are inside, and
    the cube is a whole component.
- **Every other component is a strip.** It has `N_int = 0`, so every site
  lies in exactly two squares. Those two squares share the site's bond along
  one axis `a`, the rung, and lie in the planes `(a, b)` and `(a, c)`.
  - A square's two rungs are opposite edges. Otherwise a corner would lie
    in three squares.
  - So along the strip all rungs are parallel to `a`. The projected walk
    alternates between steps `±e_b` and `±e_c`.
- **Every strip winds.** A strip that does not wind returns to its start with zero
  displacement, so its `b`-steps include both signs. Somewhere a `b`-step
  and the next `b`-step have opposite signs, separated by one `c`-step:
  steps `+e_b`, `±e_c`, `−e_b`.
  - At the rung after the `c`-step, a site's two non-rung partners span a
    square. That square's fourth corner lies on the rung two steps back,
    at the same height, so it is carved.
  - That square is then complete, and the site is interior. That contradicts
    `N_int = 0`.
  - So every strip winds. With no reversals its walk is monotone, and it
    winds along a face diagonal. ∎

Every enumerated zero-field carving satisfies each step:
- every carved site has at least two closed squares;
- `χ = N_int / 4` on every component;
- every finite component is the cube (8 sites, all interior, `χ = 2`);
- every winding component has no interior site and `χ = 0`.

So the finite components are exactly 2 x 2 x 2 cubes, and the winding ones
are the face-diagonal staircases, such as the staircase tube below. This
also explains why the linked companion construction needs relaxed carvings: a network winding
in two or three directions cannot be carved with zero fields.

The submitted branch preserves additional historical checks; they are not a new certificate in this note.

## Theorem 4 — the staircase tube is a gapped Z2 medium

*Statement.* The staircase tube has four sites per cell (a 2 x 2 plaquette)
and six bonds: two along `x`, two along `y` in the cell, and two along `z`
to the next cell. It has two plaquette types per cell. Among the four
translation-invariant flux sectors, the Majorana ground energy per cell is:
- `-3.35522K (for K>0)` with pi flux through both plaquette types;
- `-3.05534 |K|` with pi flux through one;
- `-2.87198 |K|` with zero flux.

In the pi-flux sector the Majorana spectrum is gapped, with smallest
`|eps|` equal to `2K (for K>0)`. The zero-flux sector is gapless.

*Proof.* The Bloch Hamiltonian is diagonalised on a 4000-point
Brillouin-zone grid for all 64 translation-invariant gauge configurations.
Energies and gaps agree across configurations of the same fluxes, which
shows they are gauge invariant. ∎

"Pi flux" here means that the product of the oriented bond variables
`u_jk` around the plaquette is `-1`, so the product of Majorana hoppings
around it is negative. In spin language that is loop-operator eigenvalue
`W = +1` for the loop operators defined above. The analytic pi-flux dispersion is eps(k)^2=12+8 cos(k), whose positive minimum gives gap2 for that sector. Its energy integral is -(4 sqrt(5)/pi) E(4/5), with E the complete elliptic integral of the second kind. The other sector energies are numerical quadratures, not a comparison with arbitrary nonperiodic flux patterns.

The pi-flux preference matches Lieb's rule for 4-cycles, which is not used
as a premise. Non-translation-invariant flux configurations are not
compared.

## Checks

The runner prints ten checks in four families. All pass in about
twenty seconds.
- **A.** The zero-field classification; each step of the general proof on
  every enumerated carving; and the three-direction networks with their
  forced records.
- **B.** Field cancellation.
- **C.** Loop commutation, the Majorana ground energies, and the loop
  operators broken by a field.
- **D.** Gauge invariance, the ground sector with its gap, and the gapless
  zero-flux sector.

## What this does not do

- It proves the stated strict zero-field carvings wind in at most one direction. Nonzero fields and relaxed valence lie outside that graph theorem; no general obstruction to alternative solvable representations is claimed.
- It classifies zero-field components completely: cubes and
  face-diagonal strips. It does not classify relaxed carvings.
- It works at the compass point. Other Heisenberg and Moriya couplings
  (`J`, `D`) are not classified here.
- The carving, the contents and the sign of `K` are supplied.
- The Majoranas are auxiliary real fermionic variables in the supplied representation. No
  identification with charged matter, with the fermions of the matter notes
  or with a physical gauge field is claimed.

## Decision points recorded

- The compass point of the fully soldered clause.
- The record pattern (a carving) and its contents.

Neither is adopted. The supplied spin Hamiltonian admits an auxiliary Clifford representation with static bond variables. Physical state projection remains necessary; this is not a derivation of physical fermions or gauge dynamics from the axioms.

## Representation and numerical boundary

Numerical values use K=1, with positive-K rescaling only. In Kitaev's enlarged representation the local constraints D_j=1 must be imposed; equality of unprojected vacuum minima and spin ground energies is checked for the listed finite examples, not asserted for all graphs or sectors. “Exact diagonalisation” names a finite-matrix numerical method, not exact arithmetic. The strict zero-field graph theorem concerns individually vanishing record contributions with exactly one retained bond per axis. It is not an impossibility theorem for other free representations or relaxed carvings. The analytic dispersion proves the stated pi-sector gap, while other grid minima remain numerical diagnostics.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [dynamics_clause_records_carve_kitaev_models_at_the_compass_point_2026_09_24.py](../scripts/dynamics_clause_records_carve_kitaev_models_at_the_compass_point_2026_09_24.py). Paired evidence: [current output](../logs/runner-cache/dynamics_clause_records_carve_kitaev_models_at_the_compass_point_2026_09_24.txt).

The auxiliary representation is the mathematical construction of [Kitaev](https://arxiv.org/abs/cond-mat/0506438), with its physical projection, not an adopted framework premise. Numerical topology uses [Fukui, Hatsugai and Suzuki](https://arxiv.org/abs/cond-mat/0503172) where applicable.


## No-Go Discipline Gate

This gate bounds the negative subclaims and does not award an audit grade.

### N1 — Alternative routes

- **ATTEMPTED — Relax valence.** Allow missing kept axes. The linked relaxed carvings wind in three directions, so strict valence is essential.
- **ATTEMPTED — Relax content.** Allow nonzero dangling fields. The strict zero-field classification does not exclude the linked three-direction constructions.
- **ATTEMPTED — Change periodicity.** Compare complete small tori with a capped larger enumeration. The capped enumeration cannot certify all periods; the geometric argument carries the general claim.
- **ATTEMPTED — Change gauge.** Enumerate finite gauges and translation-invariant tube sectors. Their minima do not establish arbitrary infinite-volume flux minimization.
- **ATTEMPTED — Change physical representation.** Compare finite spin spectra with auxiliary Majorana vacuum minima. Agreement on these fixtures does not remove the physical parity projection for other cells.

Successful counterroutes narrow the claim; they are not relabelled as failed physical alternatives.

### N2 — Conditional structure

The supplied dynamics, representation, record pattern and preparation assumptions are joint hypotheses. No independence count of physical obstructions is asserted.

### N3 — Hidden assumptions

The compass Hamiltonian and Majorana representation are supplied mathematics. The axioms do not select them, their gauge sector, physical state or readout. Numerical rank tolerances and finite grids remain explicit limitations.

### N4 — Residual matching

Companion results contribute only their linked conditional identities. Their finite calculations do not close an additional universal formation or dynamics problem.

### N5 — Resolution

- `per_element:` Pauli compression, signed group actions and declared Clifford identities are the element-level checks.
- `per_site:` Local supports and explicit carving-site constraints are checked only under the supplied record rules.
- `per_mode:` Finite Bloch grids and stated optimizers are diagnostics; no certified global band gap is inferred.
- `per_block:` Named finite cells and covariance coefficient spaces are checked with their explicit size and support restrictions.
- `lattice_wide:` General lattice conclusions rely only on displayed conditional arguments; finite searches do not certify physical emergence.

### N6 — Partial closure

The stated model gives conditional conclusions without adding an axiom. No necessity of new physical axioms is established by failure inside this restricted model.

### N7 — Strongest counter-route

Allow missing kept axes. The linked relaxed carvings wind in three directions, so strict valence is essential. The surviving result retains all listed hypotheses and leaves alternatives outside that scope open.

### N8 — Related work

The linked parent notes supply the adjacent covariance, record-compression and carving arguments. Their narrowed scopes govern their use here; historical independent-check narratives are not a current certificate.
