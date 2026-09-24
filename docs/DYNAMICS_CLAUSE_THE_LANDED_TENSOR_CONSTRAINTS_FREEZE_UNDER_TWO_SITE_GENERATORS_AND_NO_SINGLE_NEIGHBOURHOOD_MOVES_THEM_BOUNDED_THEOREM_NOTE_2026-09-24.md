---
claim_id: dynamics_clause_the_landed_tensor_constraints_freeze_under_two_site_generators_and_no_single_neighbourhood_moves_them_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "For the vector constraint of the landed finite-clock tensor note, (G p)_j(x) = p_jj(x + e_j) - p_jj(x) + sum_{i != j}[p_ij(x) - p_ij(x - e_i)], placed in doubled coordinates (diagonal slots at vertex sites, off-diagonal slots at face sites, rows at link sites). (i) Every row involves exactly the six neighbours of its link site, with coefficients +-1. Every slot enters rows at two or more distinct link sites, and slot sites are never adjacent. So, by the counting of open PR 9066, every sum of nearest-neighbour two-site terms that commutes with every row commutes with every slot, whatever the local Hilbert spaces and with static or link-site charges. A Z2 window checks the operator statement. (ii) With static charges, no nonzero integer (or Z_N with N odd) change of the slots that preserves every row lies within any single site's closed neighbourhood (vertex, link, plaquette or cube). For even N, shifting the six faces of a cube by N/2 preserves every row, so the statement needs integer or odd-N slots. (iii) In a box of radius 2 coarse cells, a mixed-integer program finds the minimum support of a nonzero integer change preserving every row to be 10 slots on 9 sites, through a diagonal slot and through a face slot. The optimum is planar, with coefficients 1 and 2, and is one planar piece of the landed scalar-gauge pattern S^T delta_x, which is the sum of the three pieces. An independent exhaustive search, with no box, finds no move of 9 or fewer slots, so 10 is the minimum on the whole lattice. On a torus, a constant shift along a whole line is also invariant but winds. The landed model and its constraint are supplied, and the dynamics clause is a supplied decision point. No gravitational phase, graviton or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_tensor_constraints_freeze_under_two_site_generators_2026_09_24.py
---

# The landed tensor constraints: frozen by two-site generators, and no single neighbourhood moves them

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** structural theorem with finite certificates on a supplied model; unaudited.

## Result

The landed
`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`
supplies a tensor model with a vector constraint `∂_i E_ij = 0`, the
constraint of linearized gravity. Its slots sit on doubled coordinates:
- diagonal slots `E_jj` at vertex sites;
- off-diagonal slots `E_ij` at face sites;
- the vector constraint at link sites.

For that constraint, this note shows:
- **The two-site clause cannot move the tensor field.** The counting of
  open PR 9066 applies unchanged. Slot sites are never adjacent, and every
  slot enters the constraint at two or more link sites. So every
  nearest-neighbour two-site generator that respects the constraint leaves
  every slot conserved.
- **No single neighbourhood can either.** With static charges and integer
  (or odd-N) slots, no change of the slots that respects the constraint
  fits inside one site's closed neighbourhood. The U(1) ring of open PR
  9066 does fit inside one plaquette site's neighbourhood; the tensor
  field has no analogue. For even-N clocks, a cube's six faces shifted by
  N/2 is an exception.
- **The smallest local moves** have 10 slots on 9 sites: a planar pattern
  around a vertex, with coefficients 1 and 2. Each is one planar piece of
  the landed note's scalar-gauge pattern.

So in this supplied discretization, with integer slot shifts and static
charges, moving the constrained tensor field needs dynamics at least two
steps across. That is further than a photon needs, and far beyond the one
dynamics clause.

## Setting

- **The model.** From the landed note, with no change:
  - three diagonal slots at each site `x`;
  - one off-diagonal slot on each `ij` face;
  - the vector row `(G p)_j(x)` on the `j` edge at `x`.
- **Doubled coordinates.**
  - Diagonal slots sit at `2x`.
  - Face slots sit at `2x + e_i + e_j`.
  - The row sits at the link site `2x + e_j`.
- **The dynamics clause.** Open PR 9040 (D-dyn). The argument allows any
  local Hilbert spaces and any two-site terms.

## Theorem 1 — the freeze

- **Placement.** Every row involves exactly the six neighbours of its link
  site: the two end vertices (`p_jj`) and the four faces around the edge
  (`p_ij`). All coefficients are ±1.
  - A diagonal slot enters the rows at the two `j` links of its vertex.
  - A face slot enters four rows.
  - Slot sites (roles 0 and 2) are never adjacent.
- **Freeze.** Take a matrix element of a two-site generator that changes a
  slot. The slot's value enters rows at two or more distinct link sites. The
  term's other site is a link site or a cube site, and it can compensate
  the row at one link site at most. So some row changes, and the matrix
  element must vanish. As in open PR 9066, this holds for the symmetric and
  compression forms and for charges on the link sites. ∎

A Z2 window checks the operator form: a vertex's three slots, two links
with charge qubits, and one face. The invariant operator span has rank 27,
and every element commutes with every slot.

## Theorem 2 — no single neighbourhood moves the field

Take a vertex, link, plaquette or cube site. Its closed neighbourhood
contains 3, 10, 1 and 6 slots respectively. Restrict the rows to those
slots, with every other slot held unchanged. The restricted rows have full column
rank. So with static charges, no nonzero change inside one neighbourhood
preserves every row. ∎

## Theorem 3 — the smallest moves are planar curvature pieces

Consider a box of radius 2 coarse cells, with every row that touches it
imposed. A mixed-integer program minimizes the support of a nonzero integer
change `δ` with `G δ = 0`, starting from a diagonal slot or from a face slot
(scipy, HiGHS). Both optima have:
- 10 slots on 9 sites;
- a planar shape, spanning 3x3 cells in one lattice plane;
- coefficients 1 and 2.

The optimum around a vertex `c` in the xy plane has:
- `∓2` on `E_xx(c)` and on `E_yy(c)`;
- `±1` on `E_xx(c ± e_y)` and on `E_yy(c ± e_x)`;
- `±1`, alternating, on the four xy faces at `c`.

That is one planar piece of the landed scalar-gauge pattern
`S^T δ_c`. That pattern is the landed scalar gauge shift
`E → E + (ΔI − Hessian) β` at `β = δ_c`, and it is the sum of three such
pieces, one per lattice plane. Each piece is in the kernel of `G`, as is their sum. On a
torus, a constant shift of `E_jj` along a whole `j` line is invariant too.
It winds, so it is not a local move.

## What this means for the lanes

- **Gravity lane.** The landed tensor model's E-slot moves (its `R2`
  kind) cannot come from the two-site clause, nor from a clause on one
  neighbourhood (integer slots).
  - Its `C2` terms are functions of the E slots alone. They commute with
    the vector constraint, and each row fits inside one cube or link
    site's neighbourhood. So `C2` is a one-neighbourhood term.
  - The theorems here cover only moves of the E slots.
- **Minimal move.** The smallest gauge-respecting move is a planar
  curvature piece spanning a vertex's in-plane second neighbourhood.
- **Compared with the photon.** The photon's ring fits in one plaquette
  site's neighbourhood (open PR 9066). So the campaign's decision points
  grow with the target:
  - two-site terms for the quantum-probability sector and the Z2 fields;
  - one neighbourhood for U(1);
  - larger for the tensor field.
- **What this does not settle.** Whether some other native mechanism,
  nonlinear or collective, moves a gravitational field without these
  stencils.

## Checks

The runner has 4 checks and all pass in about 45 s.

| Check | Result |
|---|---|
| Placement | 192 rows on the L = 4 torus. Each uses exactly its link site's six neighbours, with coefficients ±1. Each slot enters at least 2 link sites (diagonal 2, face 4). No adjacent slot sites. |
| Freeze (Z2 window) | Invariant operator span of rank 27; largest `|[H, X_slot]|` 0. |
| No single neighbourhood | Vertex 3 slots, link 10, plaquette 1, cube 6. Null dimension 0 each. |
| Smallest moves | Support 10 on 9 sites through a diagonal slot and through a face slot, with doubled extent (0, 4, 4). The solver reports optimality. The three planar pieces are in the kernel and sum to `S^T δ`. The face-slot optimum is a planar piece. |

## What this does not do

- It adopts no tensor model, constraint or clause. The landed model is used
  as supplied.
- It treats only the vector constraint. The scalar constraint and the
  dynamics of the conjugate slots are not treated.
- It claims no gravitational phase, graviton or matter coupling.
- It uses static charges and integer (or odd-N) slots in Theorems 2 and 3.
  Charges on link sites, and even-N clocks, change which moves are
  possible.
- It says nothing about linearized gravity outside this supplied
  discretization.

## Independent check

A separate checker wrote its own code without reading this runner.
- **Confirmed.**
  - The placement.
  - The absence of neighbourhood moves for integers, with integer
    reduction factors 1 except the cube's (1,1,1,1,1,2).
  - The 10-slot planar optimum, both in a box and by exhaustive search
    with no box.
  - The planar pieces summing to `S^T δ`.
- **Flagged, now corrected.**
  - The even-N cube exception.
  - That `C2` terms fit in one neighbourhood.
  - That the gravity statement is specific to this discretization.
