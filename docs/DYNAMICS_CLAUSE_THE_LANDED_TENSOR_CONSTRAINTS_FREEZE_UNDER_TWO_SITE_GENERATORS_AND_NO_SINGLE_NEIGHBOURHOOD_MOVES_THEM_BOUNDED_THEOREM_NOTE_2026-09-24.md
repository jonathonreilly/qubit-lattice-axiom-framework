---
claim_id: dynamics_clause_the_landed_tensor_constraints_freeze_under_two_site_generators_and_no_single_neighbourhood_moves_them_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: For the supplied commuting tensor-electric slots and vector stencil, nearest-neighbour two-site generators preserving every row freeze each slot. Exact Smith factors obstruct integer and odd-N static-charge moves in a single closed neighbourhood; even-N clocks have a six-face half-period exception. Explicit ten-slot planar kernel moves and radius-two coefficient-bound-four anchor-one MILP minima are retained. No box-free minimum theorem or gravitational phase is established.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_tensor_constraints_freeze_under_two_site_generators_2026_09_24.py
---

# Tensor-electric freeze, neighbourhood obstructions and explicit planar moves

**Type:** bounded_theorem

**Date:** 2026-09-24
**Status:** conditional-support; supplied-model mathematics, unaudited.

## Setting and structural freeze

Use the commuting electric slots and integer vector stencil from the
[landed tensor note](LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md).
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select this model.
There are three independent diagonal slots at each coarse vertex x and one
off-diagonal slot on each ij face. They have a common product eigenbasis;
this is not a statement about arbitrary noncommuting on-site observables.

    (Gp)_j(x)=p_jj(x+e_j)-p_jj(x)
              +sum_(i!=j)[p_ij(x)-p_ij(x-e_i)].

In doubled coordinates the diagonal slots lie at 2x, the face slots at
2x+e_i+e_j and each row at 2x+e_j. A row uses exactly the six neighbours
of its link site. Slot sites are never adjacent. Each diagonal slot enters
two different link rows; each face slot enters four.

For a nearest-neighbour two-site matrix element, only one site can carry
electric slots. Its other site can compensate a charge at at most one
link-row site. If a vertex's several slots change, each changed diagonal
component enters its own pair of rows, so at least one uncompensated row
still changes. A changed face likewise leaves an uncompensated row.
Commutation of the TOTAL generator with every row therefore makes the
corresponding total matrix element vanish, even if individual bond terms
would cancel. The total generator commutes with each electric slot.
The same selection rule holds after compression to a fixed constraint
sector. Charges at link sites may be dynamical in this two-site statement.
The argument extends to spectral decompositions of commuting slots;
unbounded operators additionally require a common invariant domain.

The Z2 window is supplementary: three vertex slots, two link charge qubits
and one face give invariant operator-span rank 27, all commuting with the
four electric-slot observables. It does not replace the selection-rule proof.

## Exact closed-neighbourhood obstruction

For this statement charges are static. Restrict G to the electric slots
in a vertex, link, plaquette or cube site's closed neighbourhood, imposing
every row that touches those slots. The exact integer Smith factors are:

| Centre | Slots | Nonzero Smith factors |
|---|---:|---|
| Vertex | 3 | 1,1,1 |
| Link | 10 | ten copies of 1 |
| Plaquette | 1 | 1 |
| Cube | 6 | 1,1,1,1,1,2 |

There is no integer kernel. Modulo odd N all factors are invertible, so
there is again no kernel. For even N the six cube faces can all shift by
N/2: each affected row sees two such changes, zero modulo N. Thus the
obstruction is not an all-N clock theorem. Translation and cubic symmetry
reduce all closed neighbourhoods to these four representatives.

## Constructive planar moves and bounded optimization

In the ab plane around c, the following change is in ker G:

- -2 on p_aa(c) and p_bb(c);
- +1 on p_aa(c±e_b) and p_bb(c±e_a);
- coefficients -1,+1,+1,-1 on the ab faces based at
  c,c-e_a,c-e_b,c-e_a-e_b.

Direct substitution cancels every row. The ten changed slots lie on nine
sites, with doubled-coordinate extent (0,4,4) up to permutation. Summing
the three planar pieces gives the parent's scalar-gauge pattern S^T delta_c.
On a periodic torus a constant shift of p_jj along an entire j line is
also in the kernel; it winds and is not a bounded local move.

The primary MILP searches only coarse cells in [-2,2]^3, coefficients
bounded by four, and a selected diagonal or face anchor fixed to +1.
It reports support ten in both restricted problems and validates each
integer witness against every touching row. The solver's floating-point
optimality report is a computational result for this finite class, not
an exact box-free certificate. Fixing the anchor to one excludes vectors
whose chosen anchor has another nonzero magnitude. An alleged historical
box-free search is not supplied in the PR; its global lower bound is deferred,
with the original branch preserved. The explicit planar witnesses survive
without that missing result.

These results constrain moves of the electric slots. The parent's C2 terms
are functions of those slots and can fit in a link or cube neighbourhood;
they are not ruled out. No statement about native gravitational dynamics,
photons, nonlinear collective fields or a selected ground-state phase follows.

## Evidence and negative-claim discipline

The [primary](../scripts/dynamics_clause_tensor_constraints_freeze_under_two_site_generators_2026_09_24.py)
and [receipt](../logs/runner-cache/dynamics_clause_tensor_constraints_freeze_under_two_site_generators_2026_09_24.txt)
retain placement, operator-span, exact Smith, explicit-kernel and restricted
optimization controls. Current review is not an independent audit verdict.

### N1
Examined classes are nearest-neighbour two-site operators, four closed
neighbourhoods, integer or modular slots and the specified bounded search.

### N2
The two-site and static-charge neighbourhood obstructions have different
charge assumptions; neither implies global minimal support.

### N3
Commuting slots, the stencil, geometry and constraint sector are supplied.
They are not new axioms or derived physical degrees of freedom.

### N4
The actual tensor parent supplies the constraint complex. Historical
box-free checker summaries do not supply missing proofs.

### N5
Five resolutions are retained: product-basis selection proves freeze;
Smith factors replace numerical-rank inference; the even-N cube is a
successful counterroute; planar witnesses survive the global-minimum gap;
winding shifts remain outside the finite-support claim. Runner stdout
records these resolutions without pretending every route failed.

### N6
Box-free minimum support, altered constraints, moving charges beyond the
two-site class and native finite-qubit realization remain open.

### N7
Multiple commuting slots at a vertex are allowed; arbitrary noncommuting
Paulis cannot be substituted for them. The even-N counterexample prevents
overextending the integer result.

### N8
The construction specializes the existing tensor complex. It establishes
neither a graviton nor a matter coupling, and makes no priority claim.
