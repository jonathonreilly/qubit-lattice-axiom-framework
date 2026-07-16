# Wilson Real-Positive Measure Surface Bounded-Premise Bridge

**Date:** 2026-06-03
**Scope label:** row-local bounded-premise bridge
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/wilson_real_positive_measure_bounded_premise_runner.py`](../scripts/wilson_real_positive_measure_bounded_premise_runner.py)

## Scope

This note supplies the explicit row-local bounded premise requested by the
conditional audit of
`WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md`.
It does not change any post-landing verdict; no new repo-wide axiom,
framework primitive, or Tier-A admission is added.

The bounded premise is:

```text
Wilson real-positive measure surface
```

with these row-local components:

- **Canonical Wilson matching surface.** The Wilson single-plaquette
  action is evaluated with `beta = 2 N_c / g_bare^2`, `N_c = 3`,
  `g_bare^2 = 1`, hence `beta = 6`. The generator normalization and
  no-rescaling convention are supplied by
  [`CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md).
- **Real-positive Euclidean measure branch.** The action surface is the
  branch on which `S[U]` is real-valued and `exp(-S[U])` is positive
  configuration-wise.
- **Bounded-below finite-product branch.** On finite products of SU(3)
  plaquette variables, the Wilson action is required to be bounded below so
  that the finite-volume Boltzmann measure is finite.

This is a row-local bounded premise for this bridge. It is not derived here
from the Lattice / Qubit / Admissibility / Record baseline alone, and it is
not promoted into a global axiom, framework primitive, or Tier-A admission.
The point of this bridge is to make the Wilson real-positive measure surface
review-visible, not to hide it as prose in downstream notes.

## Consequences Verified

The runner verifies the following bounded consequences.

1. Exact rational arithmetic gives `beta = 6` and `beta/N_c = 2` at
   `N_c = 3`, `g_bare^2 = 1`.
2. For sampled SU(3) plaquette variables, `Re Tr U_P` lies in `[-N_c, N_c]`.
   Therefore
   ```text
   S_W[U] = (beta/N_c) sum_P (N_c - Re Tr U_P)
   ```
   is real-valued and non-negative on the sampled finite products.
3. `exp(-S_W[U])` is real-positive and finite on those finite products.
4. The CP-odd proxy
   ```text
   Q_lat[U] = sum_P (Tr U_P - Tr U_P^dag)/(2i) = sum_P Im Tr U_P
   ```
   is real. The action term `i theta Q_lat[U]` is therefore imaginary for
   nonzero real `theta`, and generically makes
   `exp(-S_W[U] - i theta Q_lat[U])` complex.
5. The runner explicitly guards the prior V7 drift: the wrong expression
   `i theta (Tr U_P - Tr U_P^dag)/2` equals `-theta Im Tr U_P`, a real
   action term, and is not the imaginary P4-violating theta slot. The correct
   form is
   ```text
   i theta (Tr U_P - Tr U_P^dag)/(2i)
   ```
   or equivalently `i theta Im Tr U_P`.

## Use By The Wilson Selector

The Wilson selector note may consume this bridge as the explicit row-local
bounded-premise record for:

- beta=6 Wilson matching on the canonical Wilson surface;
- P4 real-valued action / positive Boltzmann branch;
- P5 bounded-below finite-volume Wilson branch.

The selector note still owns its separate bounded theorem: within the canonical
leading-beta single-plaquette surface, the real-positive branch selects
`Re Tr U_P` and rejects the imaginary `i theta Im Tr U_P` slot.

## Use By Strong CP

The Strong CP operator-basis note may consume this bridge only as the
real-positive Wilson measure surface premise. This bridge does not derive the
scalar-mass-only action class and does not claim to close the Strong CP parent
row by itself.

## Commands

```bash
python3 scripts/wilson_real_positive_measure_bounded_premise_runner.py
```

## References

- [`CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
- Consumer context: `WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md`
