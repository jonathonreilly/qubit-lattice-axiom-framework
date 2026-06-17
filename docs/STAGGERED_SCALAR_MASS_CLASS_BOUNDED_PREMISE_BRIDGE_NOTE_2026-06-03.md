# Staggered Scalar-Mass Action Class Bounded-Premise Bridge

**Date:** 2026-06-03
**Scope label:** row-local bounded-premise bridge
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/staggered_scalar_mass_class_bounded_premise_runner.py`](../scripts/staggered_scalar_mass_class_bounded_premise_runner.py)

## Source boundary (2026-06-12)

**Boundary:** renaming / bounded-premise support only. Effective status is
audit-derived; this source records only the claim boundary.

The runner verifies consequences after the scalar-mass action class is
introduced; it does not derive that action class from baseline framework
inputs.

This note may be cited only for the row-local premise `M = m I`, `m > 0`,
`M_epsilon = 0`, and the determinant-phase consequences under that premise.
It may not be cited as a derivation of the scalar-mass-only class, a global
axiom, a Tier-A admission, or a closure of all mixed/pseudoscalar mass routes.

Promotion beyond bounded-premise support requires deriving the scalar-mass
action class from retained inputs rather than introducing it locally.

## Scope

This note supplies the explicit row-local bounded premise requested by the
conditional audit of
`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`.
It does not change any post-landing verdict and adds no new repo-wide axiom,
framework primitive, or Tier-A admission.

The bounded premise is:

```text
Staggered scalar-mass action class
```

where the reviewed mass action class is the real scalar line

```text
M = m I,    m > 0,
```

with no pseudoscalar epsilon component. Equivalently, in the diagonal
`{I, epsilon}` mass basis,

```text
M = M_S I + M_epsilon epsilon
```

the premise fixes `M_epsilon = 0` and `M_S` real-positive.

This is a row-local bounded premise for this bridge. It is not derived here
from the Lattice / Quantum / Record baseline alone, and it is not a global
axiom, framework primitive, or Tier-A admission. The purpose of the bridge is
to make the scalar-mass-only action-class boundary review-visible, because the
determinant phase checks alone do not exclude every mixed/pseudoscalar route.

## Consequences Verified

The runner verifies:

1. Every tested diagonal mass candidate decomposes exactly into the
   `{I, epsilon}` basis.
2. `M = m I`, `m > 0`, lies in the scalar-mass action class.
3. `M = m exp(i alpha) I`, with `alpha = pi/4`, has no epsilon component but
   fails the real-scalar phase part of the premise.
4. `M = m5 epsilon` and `M = m I + i m5 epsilon` fail the premise because
   their epsilon component is nonzero.
5. On sampled 2x2x2x2 staggered SU(3) operators, the structural input from
   [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
   is exercised: `D^dag = -D`, `{epsilon, D}=0`, and `det(D+mI)` is
   real-positive on the real scalar line.
6. Non-real scalar phases give nonzero determinant phase on all sampled
   configurations.
7. The two-flavor mass orientation must be written as
   ```text
   arg[det(D + m_u I) det(D + m_d I)] = 0
   ```
   on this premise, not as the shorthand `arg det(M_u M_d)` unless that
   shorthand is explicitly defined to mean the product of the two Dirac
   determinants.
8. The runner records that a mixed mass can pass the determinant positivity
   gate on samples. That is why the scalar-class wall is independent rather
   than a hidden consequence of determinant positivity.

## Use By Strong CP

The Strong CP operator-basis note may consume this bridge as the explicit
row-local bounded-premise record for the scalar-mass-only action class. The
bridge does not prove that the scalar action class is forced by the minimal
framework axioms and does not claim to close the Strong CP parent row by
itself.

## Commands

```bash
python3 scripts/staggered_scalar_mass_class_bounded_premise_runner.py
```

## References

- [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
- Consumer context: `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`
