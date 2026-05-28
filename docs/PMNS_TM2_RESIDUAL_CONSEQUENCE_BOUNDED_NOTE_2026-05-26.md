# PMNS TM2 Residual Consequence -- Bounded Algebra Note

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/pmns_tm2_residual_consequence_runner.py`](../scripts/pmns_tm2_residual_consequence_runner.py)

## Scope

This note lands only the algebraic consequence that was supported by
the submitted runner. It does **not** claim that the framework has
already derived the needed PMNS residual conditions. It is a reusable
conditional lemma:

> If a PMNS matrix satisfies a trimaximal second-column residual and a
> mu-tau modulus residual, then the leading-order TM2 sum rule and the
> maximal-CP consequence follow.

The upstream identification of those residuals with retained
framework physics remains separate.

## Assumptions

Let `U` be a unitary PMNS matrix in the standard three-angle,
one-Dirac-phase parametrization, and assume:

1. **Trimaximal second column**
   ```text
   |U_e2|^2 = |U_mu2|^2 = |U_tau2|^2 = 1/3.
   ```

2. **Mu-tau modulus residual**
   ```text
   |U_mu i|^2 = |U_tau i|^2
   ```
   for the relevant mass-index columns, in particular `i = 3`.

3. `sin(theta_13) != 0` when interpreting the Dirac phase. If
   `sin(theta_13) = 0`, the phase is not fixed by the final step.

These are assumptions of this bounded algebra note, not conclusions.

## Claim

Under the assumptions above:

1. `sin^2(theta_23) = 1/2`.
2. `3 sin^2(theta_12) cos^2(theta_13) = 1`.
3. If `sin(theta_13) != 0`, then `cos(delta_CP) = 0`, so
   `delta_CP` lies in `{pi/2, 3pi/2}` modulo `2pi`.

## Proof

The standard parametrization gives

```text
|U_e2|^2 = cos^2(theta_13) sin^2(theta_12).
```

The trimaximal second-column assumption gives `|U_e2|^2 = 1/3`,
hence

```text
3 sin^2(theta_12) cos^2(theta_13) = 1.      (1)
```

The mu-tau modulus residual at column 3 gives

```text
|U_mu3|^2 = |U_tau3|^2.
```

Since `1 - |U_e3|^2 = |U_mu3|^2 + |U_tau3|^2`, this implies

```text
sin^2(theta_23)
  = |U_mu3|^2 / (1 - |U_e3|^2)
  = |U_mu3|^2 / (2 |U_mu3|^2)
  = 1/2.                                      (2)
```

With `theta_23 = pi/4`, the standard parametrization also gives

```text
|U_mu2|^2 =
  (1/2) (c12^2 + s12^2 s13^2 - 2 c12 s12 s13 cos(delta_CP)).
```

The trimaximal second-column assumption says `|U_mu2|^2 = 1/3`, so

```text
c12^2 + s12^2 s13^2 - 2 c12 s12 s13 cos(delta_CP) = 2/3.    (3)
```

From (1),

```text
s12^2 = 1 / (3 c13^2),              c13^2 = 1 - s13^2,
c12^2 = 1 - s12^2 = (2 - 3 s13^2) / (3 (1 - s13^2)).
```

Therefore

```text
c12^2 + s12^2 s13^2
  = (2 - 3 s13^2) / (3 (1 - s13^2))
    + s13^2 / (3 (1 - s13^2))
  = 2/3.
```

Equation (3) reduces to

```text
2 c12 s12 s13 cos(delta_CP) = 0.
```

For `sin(theta_13) != 0`, and away from singular mixing angles,
`c12 s12 s13` is nonzero. Hence `cos(delta_CP) = 0`.

## Boundaries

This note does **not**:

- derive the trimaximal or mu-tau residuals from the framework;
- identify which retained framework rows may serve as upstream
  authorities for those residuals;
- predict a numerical value of `theta_13`;
- provide sub-leading corrections;
- use empirical PMNS fits as derivation input;
- introduce a new axiom, admitted premise, or theory lane.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/pmns_tm2_residual_consequence_runner.py
```

Expected:

```text
TOTAL: PASS=15 FAIL=0
VERDICT: conditional TM2 algebraic consequence holds.
```
