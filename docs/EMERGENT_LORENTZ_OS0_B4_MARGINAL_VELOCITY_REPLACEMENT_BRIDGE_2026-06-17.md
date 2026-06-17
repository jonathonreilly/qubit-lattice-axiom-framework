# Emergent Lorentz OS0 B4 Marginal-Velocity Replacement Bridge

**Date:** 2026-06-17
**Claim type:** exact support theorem
**Type:** exact support theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:**
[`scripts/frontier_emergent_lorentz_os0_b4_replacement_bridge_2026_06_17.py`](../scripts/frontier_emergent_lorentz_os0_b4_replacement_bridge_2026_06_17.py)

**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_os0_b4_replacement_bridge_2026_06_17.txt`](../logs/runner-cache/frontier_emergent_lorentz_os0_b4_replacement_bridge_2026_06_17.txt)

## Targeted Audit Unlock

This note gives downstream audit rows a clean OS0 route for marginal
velocity protection that does not consume the supplied one-loop velocity-RG
packet in
[`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md).

It does not promote that older row. The older row remains the
continuous-time/non-isotropic horn: it studies a supplied one-loop RG model
and its physical anomalous-dimension and power-divergent-coefficient gates
remain conditional.

The replacement bridge is only:

```text
kinetic_isotropy_primitive
+ supplied B4-symmetric OS0 regulated action and measure
+ all-orders B4 marginal-protection theorem
-> no independent marginal c_t != c_s velocity coefficient on the OS0 branch.
```

Thus an OS0 downstream consumer that only needs marginal velocity protection
does not need to cite the supplied one-loop RG flow, physical fixed-point
gamma, or hierarchy-suppression estimate from the older conditional packet.

## Statement

On the OS0 kinetic-form surface supplied by
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
assume the supplied regulator/action/measure package of
[`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md).

Then the diagonal marginal kinetic coefficient vector

```text
(c_0, c_1, c_2, c_3)
```

is fixed by the signed-permutation action of `B4` only on the one-dimensional
subspace

```text
c_0 = c_1 = c_2 = c_3.
```

Equivalently, the operator

```text
c_t p_t^2 + c_s (p_x^2 + p_y^2 + p_z^2),  c_t != c_s,
```

is not an invariant marginal operator on the OS0 branch. The all-orders B4
theorem supplies the path-integral step: a manifest finite lattice symmetry
of the regulated action and measure is inherited by the perturbative
effective action order by order, so the coefficient of the B4-non-invariant
marginal velocity operator is zero on that branch.

## Proof

1. With only spatial `O_h` and a separately supplied time coefficient, the
   diagonal marginal kinetic coefficients have the invariant form
   `(c_t, c_s, c_s, c_s)`. The invariant space has dimension two.
2. With `B4`, every axis can be permuted with every other axis. The invariant
   diagonal coefficient vector must be constant across all four axes. The
   invariant space has dimension one.
3. The all-orders B4 theorem supplies the non-combinatorial step: on the
   supplied OS0 B4-symmetric regulator, the action and measure are exactly
   invariant, and the perturbative effective action preserves that finite
   symmetry. Therefore a B4-non-invariant marginal coefficient is not
   generated on this OS0 branch.
4. The supplied one-loop velocity-RG equations, the physical fixed-point
   anomalous dimension, and the hierarchy-suppression estimate in the older
   conditional packet are not proof inputs for this OS0 conclusion.

## Import Retirement

Retired for the OS0 marginal-protection branch:

- supplied one-loop velocity-RG dynamics;
- supplied physical fixed-point anomalous dimension;
- supplied Planck-to-IR hierarchy damping estimate;
- Collins-gate reduction through canonical continuous time.

Still open outside this bridge:

- the continuous-time/non-isotropic horn studied by the older conditional row;
- non-perturbative effects outside the all-orders perturbative B4 theorem;
- per-single-taste or taste-breaking surfaces not covered by the supplied B4
  regulator;
- physical Standard-Model Extension bound comparison;
- any absolute Lorentz-closure theorem beyond marginal OS0 protection.

## Downstream Citation Rule

Rows that need OS0 marginal velocity protection should cite this bridge plus
the all-orders B4 theorem directly. They should not cite the older supplied
one-loop RG packet as a retained authority for that purpose.

Rows that need continuous-time, non-OS0, physical anomalous-dimension, or
bound-comparison content must keep those premises exposed. This bridge does
not close those gates.

## Dependencies

- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies the OS0 kinetic-form premise. Consumed, not derived here.
- [`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md)
  supplies the all-orders perturbative B4 action/measure symmetry theorem.
- [`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  supplies the one-loop OS0 predecessor.
- [`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
  is the conditional row being bypassed for OS0 marginal-protection uses, not
  promoted.

## Boundary

This is exact support for an OS0 branch replacement. It is not a bare retained
Lorentz theorem, not an audit verdict, not a new axiom, not a new primitive,
and not a physical LV-bound comparison.

