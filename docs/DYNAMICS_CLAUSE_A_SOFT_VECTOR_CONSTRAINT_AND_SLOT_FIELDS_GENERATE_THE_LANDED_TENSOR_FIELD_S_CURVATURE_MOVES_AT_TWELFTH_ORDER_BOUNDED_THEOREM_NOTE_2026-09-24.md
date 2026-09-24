---
claim_id: dynamics_clause_a_soft_vector_constraint_and_slot_fields_generate_the_landed_tensor_field_s_curvature_moves_at_twelfth_order_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: the landed tensor slots and vector rows of open PR 9077 (diagonal slots on vertex sites, face slots on plaquette sites, rows (G E)_j = d_i E_ij on link sites); a soft constraint energy U sum_rows (G v)_row^2, where v is the change from a constraint-satisfying configuration; and one-site slot fields -h sum_s (X_s + X_s^dag), with X_s shifting slot s by one. Each row is a one-neighbourhood term on its link site. (i) The smallest L1 norm of a nonzero integer change with G v = 0 is 12, through a diagonal and through a face slot. The changes that reach it are exactly the planar pieces of the landed scalar-gauge pattern: 6 through a diagonal slot and 4 through a face slot (mixed-integer programs in a radius-2 box; an independent box-free search agrees). (ii) No monotone partial move satisfies the constraint, so the leading off-diagonal amplitude is the path sum g = A h^12 / U^11, with A = 111150053/31850496 (about 3.490). The same sum for the U(1) plaquette ring gives 5/2, which is open PR 9066's 5h^4/(32U^3) for fields h s^x. (iii) Exact diagonalization on the 2304-state path box gives splittings whose ratio to 2 A (h/U)^12 is 0.985, 0.966 and 0.941 at h/U = 0.1, 0.15 and 0.2, extrapolating to 1.000. (iv) For unbounded (rotor) slots with an integer constraint, the excitation energies depend only on the change v, so every constraint-satisfying configuration has the same diagonal energy at every order. The leading effective Hamiltonian is therefore a constant minus g times the sum of the planar-piece shifts and their inverses, with nothing depending on E. Each shift is the exponential of the stencil d_a^2 q_bb + d_b^2 q_aa - d_a d_b q_ab of the conjugate slots, which equals -2 R_abab if q is read as a metric perturbation with q_ab = 2 h_ab (not adopted). (v) Two-level (qubit) slots allow only unit changes. The smallest unit moves have 20 slots (boxes of radius 2 and 3; box-free independently), at order 20, with path sums 0.926 (spatial) and 510.6 (planar). On zero-charge surroundings the fourth-order diagonal energy changes across the planar move by exactly (201/960) dN_A h^4/U^3 (unit step), where N_A counts rows whose two diagonal slots differ. dN_A takes even values including 0. (vi) With a supplied one-site electric energy (J/2) E^2, the Gaussian spectrum of the rotor model has three branches with omega^2 = J g lambda(k), lambda of order |k|^4. One branch vanishes on the coordinate planes k_a = 0, and the landed scalar constraint leaves two. (vii) Modulo 2 the face slots and rows form the dual lattice's Z2 gauge structure, with the six-face cube move as its star. No gravitational phase, graviton, scalar constraint dynamics or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_soft_tensor_constraint_generates_curvature_moves_2026_09_24.py
---

# A soft vector constraint and slot fields generate the landed tensor field's curvature moves at twelfth order

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates on a supplied model; unaudited.

## Result

Open PR 9077 found that the landed tensor field cannot be moved by the
two-site clause or by any single neighbourhood. That field is the
discretized field of linearized gravity's vector constraint `∂_i E_ij = 0`.
Its smallest moves are 10-slot planar pieces. Open PR 9066 found how the
U(1) link field escapes the same freeze: a soft vertex Gauss energy with
record fields gives the plaquette ring at fourth order.

The tensor field escapes the same way, at higher order.
- **The leading moves are the planar pieces.** The smallest L1 norm of a
  constraint-respecting change is 12, and the changes that reach it are
  exactly the planar pieces.
- **They are generated at twelfth order.** Add a soft constraint energy
  `U Σ (G v)²` and one-site slot fields `h`. Each planar piece then gets an
  amplitude `g = A h¹²/U¹¹`, with `A = 111150053/31850496 ≈ 3.490` exactly.
  Exact diagonalization confirms it.
- **For rotor slots nothing else appears.** With unbounded slots and an
  integer constraint, every constraint-satisfying configuration has the
  same diagonal energy at every order.
  - So the leading effective Hamiltonian is a sum of cosines of a planar
    curvature stencil of the conjugate slots, with no electric term.
  - With a supplied electric energy it has three branches with
    `ω² ∝ k⁴`.
- **Qubit slots are harder.** They allow only unit changes, whose smallest
  moves have 20 slots and appear at order 20. Fourth-order diagonal
  potentials, `(201/960) ΔN_A h⁴/U³`, split most of the configurations such
  a move connects.
- **Modulo 2 it is a Z2 gauge field.** With a parity constraint on qubit
  slots, the face slots carry the dual lattice's Z2 gauge structure.

So in the ladder of the synthesis, for rotor slots with an integer
constraint, one-neighbourhood terms generate the tensor field's dynamics.
- **The photon ring** comes at order 4, with path sum 5/2.
- **The tensor moves** come at order 12. At equal one-step matrix element
  they are smaller by about `1.40 (h/U)⁸`.

## Setting and decision points

- **The landed tensor model** (landed
  `LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`,
  as placed by open PR 9077).
  - Diagonal slots sit on vertex sites, and face slots on plaquette sites.
  - The vector row
    `(G p)_j(x) = p_jj(x + e_j) − p_jj(x) + Σ_{i≠j}[p_ij(x) − p_ij(x − e_i)]`
    sits on the link site of the `j` edge at `x`.
- **A soft vector constraint (supplied).** `U Σ_rows (G v)_row²`, where `v`
  is the change of the slots from a constraint-satisfying configuration.
  Each row involves exactly its link site's six neighbours, so each term is
  a one-neighbourhood term. It is the tensor analogue of open PR 9066's
  soft vertex Gauss energy.
- **Slot fields (supplied).** `−h Σ_s (X_s + X_s†)`, where `X_s` raises slot
  `s` by one.
  - For qubit slots these are record fields `h s^x`, as in open PR 9066,
    with one-step matrix element `h/2`.
  - For rotor slots they are one-site shift terms.
- **The slot type (supplied).** Rotor (unbounded integer) slots, or
  two-level (qubit) slots.
- **An electric energy (supplied, Theorem 6 only).** A one-site
  `(J/2) Σ_s E_s²`.

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
- **All planar pieces.** Every one is a planar piece (open PR 9077). A
  diagonal slot `E_aa(0)` lies in 3 pieces in each of its two planes. A
  face slot lies in the 4 pieces of its plane around it.
- **Box-free.** An independent search from a single slot, branching only
  on unbalanced rows, confirms both statements with no box. It finds the
  next moves at L1 norm 16. ∎

## Theorem 2 — the twelfth-order amplitude

Take a planar piece `δ`, with two coefficients of size 2 and eight of size
1. Its monotone partial changes `v` form a box of `3 · 3 · 2⁸ = 2304`
states.
- **No shortcuts.** No partial change other than `0` and `δ` satisfies the
  constraint. So no lower-order move and no return to the constraint
  surface enters.
- **So the leading amplitude is a path sum.** In degenerate perturbation
  theory it is

      g = A h¹² / U¹¹,   A = Σ_paths Π_k 1 / |G v_k|²,

  over the 11 intermediate partial changes of each monotone path.
- **Exactly**, `A = 111150053/31850496 ≈ 3.4897`.
- **A check on the method.** The same sum for the U(1) plaquette ring
  gives `5/2`. With the record fields `h s^x = (h/2) σ^x` of open PR 9066,
  that is `(5/2)(h/2)⁴/U³ = 5h⁴/(32U³)`, the ring element found there.
- **The comparison.** At equal one-step matrix element `h` the tensor
  amplitude is smaller than the ring's by `(3.490/2.5)(h/U)⁸ ≈ 1.40 (h/U)⁸`.
  Against open PR 9066's normalization, `h s^x` on the links, the factor is
  about `22.3 (h/U)⁸`. ∎

## Theorem 3 — exact diagonalization confirms it

On the path box, `H = U|G v|² − h T`, where `T` is the step operator. The
box is symmetric under `v → δ − v`, so the two constraint-satisfying
states split by exactly `2|g_eff|`. The ratio of that splitting to
`2 A (h/U)¹²` is:

| `h/U` | 0.1 | 0.15 | 0.2 |
|---|---|---|---|
| ratio | 0.9847 | 0.9660 | 0.9408 |

It approaches 1 quadratically: a quadratic fit in `(h/U)²` extrapolates to
1.0000. At leading order the box is exact, since any 12-step path from 0 to
`δ` stays inside it. ∎

## Theorem 4 — rotor slots: planar-curvature cosines and nothing else

For unbounded slots with an integer constraint, the energy of a change is
`|G v|²`. It depends only on `v`, not on the configuration it changes. So
every constraint-satisfying configuration has the same excitation spectrum
and the same diagonal energy at every order. With Theorems 1 and 2, the
leading effective Hamiltonian is

    H_eff = const − g Σ_{x, planes} (T_piece + T_piece†) + O(h¹⁴).

- **The operator.** `T_piece` shifts the slots by one planar piece. In terms
  of the conjugate slots `q` it is `exp(i Σ δ_s q_s)`. In the `ab` plane,
  `Σ δ_s q_s` is the lattice stencil of `∂_a² q_bb + ∂_b² q_aa − ∂_a∂_b q_ab`.
- **A reading, not adopted.** If `q` is read as a metric perturbation with
  `q_ab = 2 h_ab`, that stencil is `−2 R_abab`, the linearized curvature of
  the `ab` plane. So in that reading the generated terms are planar
  curvature cosines. ∎

Nothing depending on `E` appears at any order in the rotor model. The
generated dynamics is purely magnetic: an electric energy, such as a
one-site `E²` or the landed `C2` terms, has to be supplied separately.

## Theorem 5 — qubit slots: order 20, and potentials first

- **Unit moves only.** A qubit slot changes by one step at most, so a move
  needs unit coefficients. The planar pieces have coefficients of size 2,
  so they are out.
- **The smallest unit moves have 20 slots.** Mixed-integer programs
  through a diagonal slot and a face slot find this in boxes of radius 2
  and 3. An independent box-free search confirms it, with 32 moves through
  a diagonal slot and 28 through a face slot, forming 2 symmetry orbits.
  - So these moves appear at order 20.
  - The two shapes have path sums 0.926 (spatial) and 510.6 (planar).
  - No partial move satisfies the constraint.
- **Potentials come first.** Each qubit slot can flip only one way, with
  the direction set by its current value. So the fourth-order diagonal
  energy depends on the configuration.
  - On zero-charge surroundings, sampled by a SAT solver on a `6³` torus,
    the planar move changes it by exactly `(201/960) ΔN_A h⁴/U³` (unit
    step). Here `N_A` counts rows whose two diagonal slots differ.
  - `ΔN_A` takes even values. The samples give −8 to 4, and an independent
    search finds every even value from −16 to 16.
  - Where `ΔN_A ≠ 0` this is far above the move's `h²⁰/U¹⁹`. Where
    `ΔN_A = 0` the move is not split at fourth order.
  - Open PR 9066 found no fourth-order diagonal term for the U(1) ring with
    equal fields. ∎

## Theorem 6 — with an electric energy, three quadratic branches

Add a supplied one-site electric energy `(J/2) Σ_s E_s²` to the rotor
model, and expand the cosines to second order. The physical modes live on
the constraint-respecting subspace `ker G(k)`, which is three-dimensional.
There `ω² = J g λ(k)`, with `λ` the eigenvalues of
`Σ_planes v_p(k) v_p(k)†`, where `v_p` is the Fourier image of the planar
piece.
- **Gauge invariance.** The pieces annihilate the gauge directions, to
  2e-15.
- **Three branches.** All three branches are nonzero at generic momenta.
  At small `k`, `λ/|k|⁴` stays between 0 and 1, so `ω ∝ k²`.
- **A soft branch.** The lowest branch vanishes on the coordinate planes
  `k_a = 0`. It is 3e-17 there and 5e-4 just off them. The planar pieces fix
  only the diagonal curvature components. Whether the off-diagonal
  curvature rows, of higher L1 norm, lift it is not computed.
- **The scalar constraint.** Adding the landed scalar constraint leaves two
  branches.

A quadratic dispersion of this kind is known from lattice tensor gauge
theories (prior art: Xu and Hořava 2010; Pretko 2017). ∎

## Theorem 7 — modulo 2 it is a Z2 gauge structure

With a parity constraint on qubit slots, read the rows modulo 2, here on a
torus of side 3.
- **The dual lattice.** Every row meets exactly 4 face slots, and every face
  slot sits in exactly 4 rows. That is the incidence of dual plaquettes and
  dual links.
- **The moves.** The face-slot moves form a 29-dimensional space: the 26
  independent six-face cube moves, which are the dual stars, plus 3
  windings.
- **The diagonal slots.** A planar piece modulo 2 is an 8-slot move through
  diagonal slots.

So with a parity constraint the face slots carry the three-dimensional
toric code's Z2 gauge structure on the dual lattice (prior art: Kitaev
2003). The cube move fits in one cube site's neighbourhood, but the tensor
structure is lost. ∎

## What this means for the lanes

- **Gravity lane.**
  - For rotor slots with an integer constraint, the landed tensor field's
    smallest moves need no new dynamics beyond one neighbourhood. A soft
    vector constraint of Admissibility shape and one-site slot fields
    generate them at twelfth order, as planar curvature cosines of the
    conjugate slots.
  - With a supplied electric energy, the generated model has three
    branches with `ω ∝ k²`.
  - Whether a gapless tensor phase follows is not settled. That needs the
    electric energy, the scalar constraint and a phase analysis.
- **The ladder of the synthesis.**
  - The photon ring comes at fourth order.
  - The rotor tensor moves come at twelfth order.
  - The qubit tensor moves come at twentieth order, behind fourth-order
    potentials where `ΔN_A ≠ 0`.
  - Modulo 2, the tensor field is a Z2 gauge field.
- **Qubit slots.** The framework's sites are qubits.
  - With qubit slots and an integer constraint, the tensor field's moves
    are high-order and mostly split by potentials.
  - With a parity constraint they lose the tensor structure.
  - Among the slot types treated here, only unbounded slots are free of
    diagonal potentials at every order. The landed model's N-level clocks
    with a modular constraint are not treated, beyond `N = 2`.
- **Prior art.** Lattice tensor gauge theories with emergent gravitons
  include Gu and Wen (2006), Xu (2006), Xu and Hořava (2010) and Pretko
  (2017). They are cited as prior art, not as premises.

## Checks

The runner has 7 checks and all pass in about 2 minutes, peak about 0.6 GB.

| Check | Result |
|---|---|
| Leading moves | Smallest L1 norm 12 through a diagonal and a face slot. The enumeration finds 6 and 4 moves, all planar pieces. |
| Path sum | `A = 111150053/31850496` over 2304 partial moves, none constraint-satisfying. The ring gives `5/2`, which is `5/32` in the `(h/2)⁴` form. |
| Exact diagonalization | Two zero-energy configurations. Ratios 0.9847, 0.9660 and 0.9408, extrapolating to 1.0000. |
| Qubit unit moves | Support 20 through a diagonal and a face slot; path sums 0.9265 (spatial) and 510.6 (planar). |
| Qubit potentials | 192 slot pairs across the planar move. On 12 SAT-sampled zero-charge surroundings the change equals `(201/960) ΔN_A` to 5e-16, with `ΔN_A` from −8 to 4. |
| Electric energy | Gauge invariance 2e-15; three branches with `ω²/(Jg|k|⁴)` in 0–0.19, 0.26–0.96 and 0.56–0.98; the lowest vanishes on the coordinate planes; two branches with the scalar constraint. |
| Modulo 2 | Every row meets 4 face slots and each face slot 4 rows. Face-slot moves 29 = 26 cube moves + 3 windings. A planar piece modulo 2 is an 8-slot move. |

## Independent check

A separate checker wrote its own code without reading this runner.
- **Confirmed.**
  - A box-free search finds exactly 6 and 4 moves at L1 norm 12, and the
    next at 16.
  - `A` is exact, summed over all 119,750,400 paths.
  - The box diagonalization at 50-digit precision gives 0.99614 at
    `h/U = 0.05` and 0.99938 at 0.02.
  - The rotor argument is sound: the Hamiltonian commutes with shifts by
    any kernel element.
  - A box-free search finds exactly 20 slots as the smallest unit moves, in
    two symmetry orbits, with the stated path sums.
- **Flagged, now addressed.**
  - The first version computed the qubit potentials on surroundings that
    broke the zero-charge constraint. They are now computed on
    SAT-sampled zero-charge surroundings, with the exact formula
    `(201/960) ΔN_A`.
  - The curvature identification is now marked as a reading, not adopted.
  - The comparison factor now states its normalization.
  - The rotor-only scope is now explicit.
  - Box-free searches are cited alongside the boxes.

## What this does not do

- It adopts no tensor model, soft constraint, slot field, slot type or
  electric energy.
- It computes the leading order only. The pieces of the off-diagonal
  curvature rows have L1 norm 16 or more and enter at higher order.
- It treats N-level clocks with a modular constraint only for `N = 2`
  (Theorem 7).
- It claims no gravitational phase, graviton, scalar-constraint dynamics,
  matter coupling or physical identification.
