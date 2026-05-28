# PMNS TM2 Magnitudes Conditional Matrix -- Bounded Note

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/pmns_tm2_magnitudes_conditional_runner.py`](../scripts/pmns_tm2_magnitudes_conditional_runner.py)

## Scope

This is a conditional algebra lemma. It does not claim that the
framework has already derived the PMNS residuals or the value of
`sin^2(theta_13)`.

Assume a PMNS magnitudes-squared matrix satisfies:

1. the second column is trimaximal:
   ```text
   |U_e2|^2 = |U_mu2|^2 = |U_tau2|^2 = 1/3;
   ```
2. the mu and tau rows have equal moduli:
   ```text
   |U_mu i|^2 = |U_tau i|^2       for i = 1,2,3;
   ```
3. the row and column sums are unitary stochastic sums;
4. `s^2 := |U_e3|^2 = sin^2(theta_13)`.

## Claim

Under those assumptions, the whole magnitudes-squared matrix is

```text
|U|^2 = ( 2/3 - s^2      1/3      s^2        )
        ( 1/6 + s^2/2    1/3     (1 - s^2)/2 )
        ( 1/6 + s^2/2    1/3     (1 - s^2)/2 )
```

The matrix is doubly stochastic and mu-tau democratic. Its entries are
nonnegative for `0 <= s^2 <= 2/3`.

## Proof

The electron row gives

```text
|U_e1|^2 = 1 - |U_e2|^2 - |U_e3|^2 = 2/3 - s^2.
```

The third column, together with mu-tau equality, gives

```text
|U_mu3|^2 = |U_tau3|^2 = (1 - s^2)/2.
```

The first column, together with mu-tau equality, gives

```text
|U_mu1|^2 = |U_tau1|^2
          = (1 - |U_e1|^2)/2
          = (1/3 + s^2)/2
          = 1/6 + s^2/2.
```

The second column is fixed by the trimaximal assumption. Row and column
sums of the displayed matrix are then all `1`, which proves the closed
form.

## Boundaries

This note does **not**:

- derive the residual assumptions from the framework;
- identify an audited upstream PMNS residual authority;
- predict or import a value of `sin^2(theta_13)`;
- use empirical PMNS fits as derivation input;
- claim sub-leading corrections, neutrino masses, or phases;
- introduce a new axiom, admitted premise, or theory lane.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/pmns_tm2_magnitudes_conditional_runner.py
```

Expected:

```text
TOTAL: PASS=41 FAIL=0
VERDICT: conditional TM2 magnitudes matrix holds.
```
