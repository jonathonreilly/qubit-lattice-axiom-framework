# PMNS TM2 Residual Consequence -- Stipulated-Hypothesis Bounded Algebra Note

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/pmns_tm2_residual_consequence_runner.py`](../scripts/pmns_tm2_residual_consequence_runner.py)

## Scope

This note lands only the algebraic implication supported by the submitted
runner. The residual statements below are theorem hypotheses, not upstream
framework conclusions and not hidden dependencies. It does **not** claim that
the framework has already derived the needed PMNS residual conditions.

> If a PMNS matrix satisfies a trimaximal second-column residual and a
> mu-tau modulus residual, then the leading-order TM2 sum rule and
> maximal atmospheric mixing follow. On the nonsingular phase chamber
> `c12*s12*s13 != 0`, the maximal-CP consequence also follows.

The upstream identification of those residuals with retained
framework physics remains separate. Any downstream use as a framework PMNS
prediction must cite retained residual-derivation authorities; this bounded
row only certifies the finite algebra once those hypotheses are stipulated.

## Stipulated Hypotheses

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

3. `c12*s12*s13 != 0` when interpreting the Dirac phase. Under the
   TM2 sum rule this excludes the phase-degenerate endpoints, including
   `sin(theta_13) = 0` and `sin^2(theta_13) = 2/3`.

These are stipulated hypotheses of this bounded algebra theorem, not
conclusions and not framework-derived residual authorities.

## Claim

Under the assumptions above:

1. `sin^2(theta_23) = 1/2`.
2. `3 sin^2(theta_12) cos^2(theta_13) = 1`.
3. If `c12*s12*s13 != 0`, then `cos(delta_CP) = 0`, so
   `delta_CP` lies in `{pi/2, 3pi/2}` modulo `2pi`.

The audited claim surface is only this implication from the stipulated
hypotheses. The note does not assert that the hypotheses hold in the framework.

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

On the nonsingular phase chamber `c12 s12 s13 != 0`, division by this
factor is valid. Hence `cos(delta_CP) = 0`.

The endpoint `sin^2(theta_13) = 2/3` is explicitly outside this chamber.
There `c13^2 = 1/3`, so the TM2 sum rule gives `s12^2 = 1` and
`c12 = 0`. Equation (3) then reduces to `2/3 = 2/3` independently of
`delta_CP`, so maximal CP is not forced at that endpoint.

## Boundaries

This note does **not**:

- derive the trimaximal or mu-tau residuals from the framework;
- identify which retained framework rows may serve as upstream
  authorities for those residuals;
- allow downstream PMNS-prediction rows to cite this algebraic implication
  without separately closing the residual hypotheses;
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
TOTAL: PASS=22 FAIL=0
VERDICT: stipulated-hypothesis TM2 algebraic consequence holds.
```
