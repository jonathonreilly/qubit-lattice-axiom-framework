---
claim_id: dynamics_clause_a_soft_vector_constraint_and_slot_fields_generate_the_landed_tensor_field_s_curvature_moves_at_twelfth_order_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Take the landed tensor slots and vector rows of open PR 9077 (diagonal slots on vertex sites, face slots on plaquette sites, rows (G E)_j = d_i E_ij on link sites), a soft constraint energy U sum_rows (G v)_row^2, where v is the change from a constraint-satisfying configuration, and one-site slot fields -h sum_s (X_s + X_s^dag), with X_s shifting slot s by one. Each row is a one-neighbourhood term on its link site. All of this is supplied, none adopted. (i) The smallest L1 norm of a nonzero integer change with G v = 0 is 12, through a diagonal and through a face slot (mixed-integer programs, radius-2 box). A complete enumeration finds exactly 6 such moves through a diagonal slot and 4 through a face slot, all planar pieces of the landed scalar-gauge pattern. (ii) No monotone partial move satisfies the constraint, so the leading off-diagonal amplitude is the path sum g = A h^12 / U^11 with A = 111150053/31850496 (about 3.490). The same sum for the U(1) plaquette ring gives 5/2, which is open PR 9066's 5h^4/(32U^3) for fields h s^x. (iii) Exact diagonalization on the 2304-state path box gives splittings whose ratio to 2 A (h/U)^12 is 0.985, 0.966 and 0.941 at h/U = 0.1, 0.15 and 0.2, extrapolating to 1.000. (iv) For unbounded (rotor) slots the excitation energies depend only on the change v, so every constraint-satisfying configuration has the same diagonal energy at every order. The leading effective Hamiltonian is therefore a constant minus g times the sum of the planar-piece shifts and their inverses. Each shift is the exponential of the planar curvature stencil of the conjugate slots, d_a^2 q_bb + d_b^2 q_aa - d_a d_b q_ab. (v) Two-level (qubit) slots allow only unit changes. The smallest unit moves have 20 slots (radius-2 and radius-3 boxes), so they appear at order 20, with path sums 0.926 (spatial) and 510.6 (planar). Each slot then flips one way only, and the fourth-order diagonal energy of a 20-slot move's end configurations differs by up to about 3 h^4/U^3 over random surroundings. So generic qubit configurations get potentials far above the move. No gravitational phase, graviton, dispersion, scalar constraint or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_soft_tensor_constraint_generates_curvature_moves_2026_09_24.py
---

# A soft vector constraint and slot fields generate the landed tensor field's curvature moves at twelfth order

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates on a supplied model; unaudited.

## Result

Open PR 9077 found that the landed tensor field, the discretized field of
linearized gravity's vector constraint `∂_i E_ij = 0`, cannot be moved by
the two-site clause or by any single neighbourhood. Its smallest moves are
10-slot planar pieces. Open PR 9066 found how the U(1) link field escapes
the same freeze: a soft vertex Gauss energy with record fields gives the
plaquette ring at fourth order.

The tensor field escapes the same way, at higher order:
- **The leading moves are the planar pieces.** The smallest L1 norm of a
  constraint-respecting change is 12, and the changes that reach it are
  exactly the planar pieces.
- **They are generated at twelfth order.** A soft constraint energy
  `U Σ (G v)²` plus one-site slot fields `h` gives each planar piece an
  amplitude `g = A h¹²/U¹¹`, with `A = 111150053/31850496 ≈ 3.490` exactly.
  Exact diagonalization confirms it.
- **For rotor slots nothing else appears.** Every constraint-satisfying
  configuration has the same diagonal energy at every order. So the
  leading effective Hamiltonian is a sum of planar-curvature cosines of
  the conjugate slots, and nothing more.
- **Qubit slots are harder.** They allow only unit changes, whose smallest
  moves have 20 slots and appear at order 20. Fourth-order diagonal
  potentials then dwarf them.

So in the ladder of the synthesis, the tensor field needs dynamics beyond
one neighbourhood, and one-neighbourhood terms generate that dynamics.
- **The photon ring** comes at order 4, with path sum 5/2.
- **The tensor moves** come at order 12. At equal `h/U` they are smaller by
  about `1.4 (h/U)⁸`.

## Setting and decision points

- **The landed tensor model** (landed
  `LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`,
  as placed by open PR 9077):
  - diagonal slots on vertex sites and face slots on plaquette sites;
  - the vector row `(G p)_j(x) = p_jj(x + e_j) − p_jj(x) + Σ_{i≠j}[p_ij(x) − p_ij(x − e_i)]`
    on the link site of the `j` edge at `x`.
- **A soft vector constraint (supplied).** `U Σ_rows (G v)_row²`, where `v`
  is the change of the slots from a constraint-satisfying configuration.
  Each row involves exactly its link site's six neighbours, so each term is
  a one-neighbourhood term. It is the tensor analogue of open PR 9066's
  soft vertex Gauss energy.
- **Slot fields (supplied).** `−h Σ_s (X_s + X_s†)`, where `X_s` raises slot
  `s` by one.
  - For qubit slots these are record fields `h s^x`, as in open PR 9066.
    Their one-step matrix element is `h/2`.
  - For rotor slots they are one-site shift terms.
- **The slot type (supplied).** Rotor (unbounded integer) slots, or
  two-level (qubit) slots.

None is adopted.

## Theorem 1 — the leading moves are the planar pieces

- **Order.** A change `v` needs `Σ_s |v_s|` single steps, its L1 norm.
  Mixed-integer programs in a box of radius 2 cells find the smallest L1
  norm of a nonzero integer `v` with `G v = 0` to be 12, through a diagonal
  slot and through a face slot.
- **Completeness.** Enumerating every solution of L1 norm at most 12, by
  adding a cut that excludes each solution found, gives:
  - exactly 6 moves through a diagonal slot, all positive there;
  - exactly 4 through a face slot.

  All are planar pieces (open PR 9077). A diagonal slot `E_aa(0)` lies in
  3 pieces in each of its two planes. A face slot lies in the 4 pieces of
  its plane around it. ∎

## Theorem 2 — the twelfth-order amplitude

Take a planar piece `δ`, with its two coefficients of size 2 and eight of
size 1. Its monotone partial changes `v` form a box of
`3 · 3 · 2⁸ = 2304` states.
- **No shortcuts.** No partial change other than `0` and `δ` satisfies the
  constraint. So no lower-order move and no return to the constraint
  surface enters.
- **So the leading amplitude is a path sum.** In degenerate perturbation
  theory it is

      g = A h¹² / U¹¹,   A = Σ_paths Π_k 1 / |G v_k|²,

  over the 11 intermediate partial changes of each monotone path.
- **Exactly**, `A = 111150053/31850496 ≈ 3.4897`.
- **A check on the method.** The same sum for the U(1) plaquette ring
  gives `5/2`. With the record fields `h s^x = (h/2) σ^x` of open PR 9066
  that is `(5/2)(h/2)⁴/U³ = 5h⁴/(32U³)`, the ring element found there. ∎

## Theorem 3 — exact diagonalization confirms it

On the path box, `H = U|G v|² − h T`, where `T` is the step operator. The
box is symmetric under `v → δ − v`, so the two constraint-satisfying
states split by exactly `2|g_eff|`. The ratio of that splitting to
`2 A (h/U)¹²` is:

| `h/U` | 0.1 | 0.15 | 0.2 |
|---|---|---|---|
| ratio | 0.9847 | 0.9660 | 0.9408 |

It approaches 1 quadratically. A quadratic fit in `(h/U)²` extrapolates to
1.0000. ∎

## Theorem 4 — rotor slots: the curvature cosine and nothing else

For unbounded slots, the energy of a change is `|G v|²`, which depends
only on `v`, not on the configuration it changes. So every
constraint-satisfying configuration has the same excitation spectrum, and
the same diagonal energy at every order. Theorems 1 and 2 then give the
leading effective Hamiltonian:

    H_eff = const − g Σ_{x, planes} (T_piece + T_piece†) + O(h¹⁴).

`T_piece` shifts the slots by one planar piece. In terms of the conjugate
slots `q`, it is `exp(i Σ δ_s q_s)`. In the `ab` plane, `Σ δ_s q_s` is the
lattice stencil of `∂_a² q_bb + ∂_b² q_aa − ∂_a∂_b q_ab`. That is the
linearized curvature of the plane's metric perturbation, with the landed
face convention `q_ab = 2 h_ab`. So the generated term is a sum of planar
curvature cosines. ∎

Nothing depending on `E` appears at any order in this model. So the
generated dynamics is purely magnetic: an electric energy, such as a
one-site `E²` or the landed `C2` terms, has to be supplied separately.

## Theorem 5 — qubit slots: order 20, and potentials first

- **Unit moves only.** A qubit slot changes by one step at most, so a move
  needs unit coefficients. The planar pieces have coefficients of size 2,
  so they are out.
- **The smallest unit moves have 20 slots.** Mixed-integer programs
  through a diagonal slot and through a face slot find this in boxes of
  radius 2 and 3. So they appear at order 20.
  - Two shapes occur: spatial ones, with path sum 0.926, and a planar one
    in one lattice plane, with path sum 510.6.
  - No partial move satisfies the constraint.
- **Potentials come first.** Each qubit slot can flip only one way. Its
  direction depends on its current value.
  - So the fourth-order diagonal energy depends on the configuration,
    through the pairs of slots that share a row.
  - Between the two end configurations of a 20-slot move, it changes by
    between −2.95 and 2.54 `h⁴/U³` (unit step) over 100 random
    surroundings.
  - That is far above the move's `h²⁰/U¹⁹`.
  - Open PR 9066 found no fourth-order diagonal term for the U(1) ring with
    equal fields. Here the diagonal energy does change across a move. ∎

## What this means for the lanes

- **Gravity lane.**
  - The landed tensor field's smallest moves need no new dynamics beyond
    one neighbourhood. A soft vector constraint of Admissibility shape and
    one-site slot fields generate them at twelfth order.
  - For rotor slots the generated term is a planar-curvature cosine of the
    conjugate slots.
  - Whether a phase with gapless tensor modes follows is not settled. That
    needs an electric energy, the scalar constraint, and a phase analysis.
- **The ladder of the synthesis.** The photon ring comes at fourth order
  and the tensor moves at twelfth. For qubit slots, unit moves come at
  twentieth order, behind fourth-order potentials.
- **Qubit slots.** The framework's sites are qubits. With qubit slots and
  an integer constraint, the tensor field's moves are both high-order and
  dominated by potentials. Only unbounded slots are free of diagonal
  potentials at every order. Bounded slots get them at an order set by how
  close the slots sit to their bounds.
- **Prior art.** Lattice tensor gauge theories with emergent gravitons
  include Gu and Wen (2006), Xu (2006), Xu and Hořava (2010) and Pretko
  (2017). They are cited as prior art, not as premises.

## Checks

The runner has 5 checks and all pass in about 60 s.

| Check | Result |
|---|---|
| Leading moves | Smallest L1 norm 12 through a diagonal and a face slot. The complete enumeration finds 6 and 4 moves, all planar pieces. |
| Path sum | `A = 111150053/31850496` over 2304 partial moves, none constraint-satisfying. The ring gives `5/2`, which is `5/32` in the `(h/2)⁴` form. |
| Exact diagonalization | Two zero-energy configurations. Ratios 0.9847, 0.9660 and 0.9408, extrapolating to 1.0000. |
| Qubit unit moves | Support 20 through a diagonal and a face slot (optimal, spatial), path sums 0.9265. The planar 20-slot move is in the kernel, with path sum 510.6. |
| Qubit potentials | 248 slot pairs across the move's edge. The fourth-order change ranges from −2.95 to 2.54 `h⁴/U³`. |

## What this does not do

- It adopts no tensor model, soft constraint, slot field or slot type.
- It computes the leading order only. The pieces of the off-diagonal
  curvature rows have larger L1 norm and enter at higher order. They are
  not computed.
- The searches use boxes of radius 2, and of radius 3 for the unit moves.
  For the unit moves the whole-lattice minimum is not proved.
- Finite clocks with even `N` have the six-face cube move of open PR 9077,
  which fits in one neighbourhood. A constraint imposed modulo `N` is not
  treated.
- It claims no gravitational phase, graviton, dispersion, scalar constraint,
  matter coupling or physical identification.
