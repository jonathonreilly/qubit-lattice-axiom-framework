# Staggered Scalar-Mass Action Class Accepted-Premise Bridge

**Date:** 2026-06-03
**Status (source-side label):** bounded_theorem; accepted-premise bridge
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/staggered_scalar_mass_class_accepted_premise_runner.py`](../scripts/staggered_scalar_mass_class_accepted_premise_runner.py)
**Cached output:** [`logs/runner-cache/staggered_scalar_mass_class_accepted_premise_runner.txt`](../logs/runner-cache/staggered_scalar_mass_class_accepted_premise_runner.txt)

## Scope

This note supplies the explicit accepted-premise packet requested by the
conditional audit of
[`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md).
It does not change any audit verdict and it adds no new repo-wide axiom.

The single packet is:

```text
P1: Staggered scalar-mass action class
```

where P1 states that the reviewed mass action class is the real scalar line

```text
M = m I,    m > 0,
```

with no pseudoscalar epsilon component. Equivalently, in the diagonal
`{I, epsilon}` mass basis,

```text
M = M_S I + M_epsilon epsilon
```

the packet fixes `M_epsilon = 0` and `M_S` real-positive.

P1 is an accepted-premise packet entry for this row. It is not derived here
from A1/A2 alone, and it is not a global axiom. The purpose of the bridge is to
make the scalar-mass-only action-class boundary audit-visible, because the
determinant phase checks alone do not exclude every mixed/pseudoscalar route.

## Consequences Verified

The runner verifies:

1. Every tested diagonal mass candidate decomposes exactly into the
   `{I, epsilon}` basis.
2. `M = m I`, `m > 0`, lies in P1.
3. `M = m exp(i alpha) I`, with `alpha = pi/4`, has no epsilon component but
   fails the real-scalar phase part of P1.
4. `M = m5 epsilon` and `M = m I + i m5 epsilon` fail P1 because their epsilon
   component is nonzero.
5. On sampled 2x2x2x2 staggered SU(3) operators, the retained structural
   input from
   [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
   is exercised: `D^dag = -D`, `{epsilon, D}=0`, and `det(D+mI)` is
   real-positive on the real scalar line.
6. Non-real scalar phases give nonzero determinant phase on all sampled
   configurations.
7. The two-flavor mass orientation must be written as
   ```text
   arg[det(D + m_u I) det(D + m_d I)] = 0
   ```
   on P1, not as the shorthand `arg det(M_u M_d)` unless that shorthand is
   explicitly defined to mean the product of the two Dirac determinants.
8. The runner records that a mixed mass can pass the determinant positivity
   gate on samples. That is why P1 is an independent scalar-class wall rather
   than a hidden consequence of determinant positivity.

## Use By Strong CP

The Strong CP operator-basis note may consume this bridge as the explicit
accepted bounded-premise record for the scalar-mass-only action class. The
bridge does not prove that the scalar action class is forced by the minimal
framework axioms and does not claim to close the Strong CP parent row by
itself.

## Commands

```bash
python3 scripts/cached_runner_output.py --refresh scripts/staggered_scalar_mass_class_accepted_premise_runner.py --timeout-sec 120 --tail-chars 5000
python3 scripts/cached_runner_output.py --check-only scripts/staggered_scalar_mass_class_accepted_premise_runner.py
```

## References

- [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
- [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
