---
claim_id: the_members_action_on_the_approved_tick_surface_is_unique_beta_equals_minus_alpha_and_alpha_equals_k_over_four_follow_from_symmetry_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Real quadratic forms Q(h,k) in a symmetric 4x4 tensor h (the member's field, with lapse h_00 and shift h_0i), homogeneous of degree two in the Euclidean 4-momentum k: the dimension-4 part of any lattice action's small-k expansion. Exact rational counts. (T1) Under the cubic group of the three space axes with time reversal, 26 forms are invariant and 2 of them are invariant under linearised relabellings h -> h + k xi^T + xi k^T; in block 101's 3+1 read-off every such form has beta/alpha = -1 and its transverse-traceless speed is free. (T2) Under the hyperoctahedral group of Z^4 (the surface of the approved kinetic_isotropy_primitive), 9 forms are invariant and exactly 1 is relabelling-invariant: the Euclidean Fierz-Pauli (linearised Einstein) form, which is O(4)-invariant; its read-off has beta/alpha = -1 and transverse-traceless speed 1, the speed every field has on that surface, i.e. K = 4 alpha at wbar = 1. Linear order in h only; lattice relabelling invariance beyond linear order, reflection positivity of a lattice member action and block 105's clock tension are not treated."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
runner: scripts/member_action_on_the_approved_tick_surface_is_unique_2026_09_27.py
---

# The member's action on the approved tick surface is unique: β = −α and α = K/4 follow from symmetry

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** exact counts and identities in rational arithmetic; unaudited;
independent checks recorded below.

## In one paragraph

At long wavelengths the campaign's gravity field (the member) has two numbers
besides its strength:
- how its clock trades against its lengths (`β/α`);
- how fast its waves travel (`K/α`).

Requiring that relabelling points in space and time changes nothing fixes the
first: `β = −α`, as block 112 found. On the surface the campaign now uses,
where time is kept apart from the three space directions, nothing fixes the
second. That is why one light cone needed the separate condition `α = K/4`.

On the surface the framework approved in June, where a tick is grained like
an edge, the second is fixed too. There is exactly one possible action,
Einstein's (linearised), and its waves move at the same speed as everything
else. The campaign's two central conditions become consequences of one
symmetry that the framework has already approved.

## Why this question

Blocks 134–136 found one light cone for the walker and the member iff
`α = K/4`. Block 112 found that the member's constraint algebra closes on
the lattice iff `β = −α`. The fork probe (2026-09-22) listed "two
polarisations, one speed iff `K = 4α`" as unchecked.

The one-light-cone note of the same date shows that, on a surface where time
is not a lattice direction, identities of this kind are tunings that
interactions shift. The June `kinetic_isotropy_primitive` (approved) puts a
tick on the same footing as an edge. The June B4 note shows that this
protects scalar and spinor kinetic terms.

A tensor field is different. Hypercubic symmetry admits 4-index invariants
that full rotations do not; the lattice energy-momentum tensor's split into
two hypercubic irreps is the familiar example. So whether the member's action
is protected is a question, not a corollary. This note answers it at the
level of the dimension-4 kinetic form.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`) and the approved
  `kinetic_isotropy_primitive`.
- **The member** as in block 101 (supplied, not adopted):
  `L = [α tr(ḣ²) + β(tr ḣ)²]/w̄ + K w̄(u R_1 + R_2) − e u`.
  - Its transverse-traceless modes have
    `ω² = K w̄² p²/(4α)`, so their speed is `w̄ sqrt(K/(4α))`.
  - The walker's speed at uniform rate is `w̄`, so one cone means
    `K = 4α`.
- **The forms.** `Q(h,k)`, real, quadratic in the symmetric `4x4` `h` and in
  `k`. In Euclidean form, `k_0` is the frequency. These are the dimension-4
  terms of a lattice action at small momentum. A nearest-neighbour lattice
  action's leading symbol is of this type.
- **Symmetries.**
  - `S3`: all signed permutations of the three space axes, with time
    reversal `k_0 -> -k_0`. This is the campaign's continuous-time or
    level-time surface.
  - `B4`: all signed permutations of the four axes. This is the approved
    primitive's surface.
  - `G`: linearised relabellings `h -> h + k ξ^T + ξ k^T`, the member's gauge
    symmetry; block 112's closure is its lattice expression.
- **Read-off.**
  - Put `h_0μ = 0` and `k = (k_0, 0, 0, 0)`. Then
    `Q = k_0^2 [A Σ h_ij² + B (tr h)²]`, and `β/α = B/A`.
  - The transverse-traceless mode `h_12` with `p` along axis 3 gives the
    spatial coefficient. Its speed squared (in Minkowski signature) is
    spatial over temporal.

## T1 — on the space-cubic surface: β = −α is forced, the wave speed is not

*Statement.* 26 quadratic forms are `S3`-invariant. Exactly 2 of them are
also `G`-invariant, and they are spanned by `v_0` and `v_1`. For
`Q = a v_0 + b v_1` with `a != 0`:
- `β/α = −1`;
- the transverse-traceless speed squared is `−b/(2a)`, which is free.

`v_1` alone is a potential-only form with no kinetic part.

*Proof.* The invariant basis is built from orbit sums. Gauge invariance is a
linear condition on the coefficients, and its null space is computed in
exact rational arithmetic (sympy). ∎

So block 112's closing ratio is a consequence of relabelling invariance
alone. The one-cone ratio `K/α` is not fixed on this surface: it can be any
value, including negative (a wrong-sign spatial term). That is the formal
content of "`α = K/4` is a tuning here".

## T2 — on the approved tick surface the action is unique

*Statement.*
- 9 quadratic forms are `B4`-invariant.
- Exactly 1 is also `G`-invariant. It equals `−16` times the Euclidean
  Fierz–Pauli form

  `(1/2) k² h·h − |h k|² + (k·h·k) tr h − (1/2) k² (tr h)²`,

  the linearised Einstein–Hilbert action.
- It is invariant under an exact rational `O(4)` rotation (a Cayley
  transform), so it is Lorentz-invariant after continuation to real time.
- Its read-off has `β/α = −1` and transverse-traceless speed squared `1`.

*Proof.* The counts are exact, as in T1. The proportionality to Fierz–Pauli
and the `O(4)` invariance are exact symbolic identities. ∎

*Robustness.* The axioms name proper rotations only. With only the proper
subgroups the counts are unchanged:
- the proper cubic group with time reversal: 26 invariant forms, 2
  relabelling-invariant;
- the proper cubic group without time reversal: 30 invariant, still 2
  relabelling-invariant;
- the proper hyperoctahedral group of `Z^4` (192 elements): 9 invariant,
  1 relabelling-invariant.

## What it means

On the approved surface:
- `β = −α` follows from relabelling invariance (T1 and T2);
- `K = 4α`, one light cone for gravity and matter, follows from the
  tick-edge symmetry (T2).

Both are protected. The dimension-4 form is unique, so corrections that
respect the two symmetries can only change the overall coefficient (Newton's
constant), never the speed or the closing ratio.

**The condition for loop corrections to respect relabelling invariance** is
that the member's source be exactly conserved. That is the campaign's "books
balance" programme:
- exact for free walkers (blocks 134–136, 139);
- lost at third order under one record per site (blocks 137, 143, 151,
  152).

So on the approved surface:
- the books' exactness is what keeps gravity's cone protected;
- where the books fail, the protection fails at the same order.

This ties two of the campaign's programmes, the books and one light cone,
into a single condition.

On the surface the campaign currently uses, the one-light-cone note of the
same date shows that the corresponding speeds drift at second order in any
coupling. T1 shows that nothing there fixes the member's speed even at tree
level.

## What it does not say

- Linear order in `h` only. Whether lattice relabelling invariance can hold
  beyond linear order is the campaign's open nonlinear problem (block 150
  T5(d): no finite-range placement closes every pair). It is not addressed
  here.
- It does not construct a lattice member action on `Z^4` with exact
  linearised lattice relabelling invariance and reflection positivity.
  Linearised lattice gravity actions of this kind are standard (reference
  only). The framework's version is not built here.
- It does not resolve block 105's tension: in discrete ticks a local clock is
  exact only for walks that do not move. On the approved surface the clock is
  the component `h_00` of a four-dimensional field, not a separate tick
  count. Whether that dissolves the tension is open.

## Independent checks

To be recorded after the independent checks return (see the PR body).

## Reproduction

```bash
python3 scripts/member_action_on_the_approved_tick_surface_is_unique_2026_09_27.py
```

Expected: `TOTAL: PASS=7 FAIL=0` (under a minute).
