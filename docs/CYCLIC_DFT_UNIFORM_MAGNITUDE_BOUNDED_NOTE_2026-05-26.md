# Cyclic DFT Uniform Magnitude -- Bounded Note

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/cyclic_dft_uniform_magnitude_runner.py`](../scripts/cyclic_dft_uniform_magnitude_runner.py)

## Scope

This note lands only the finite cyclic-character algebra supported by
the submitted runner. It does not claim a PMNS prediction, a
dynamics-lane bridge, a K-theory derivation, or a retained framework
residual.

## Claim

For the cyclic group `Z_N`, let

```text
omega_N = exp(2 pi i / N),
F_N[j,k] = omega_N^(j k) / sqrt(N),        j,k in {0,...,N-1}.
```

Then every entry of the normalized character table / DFT matrix has

```text
|F_N[j,k]|^2 = 1/N.
```

Equivalently, the overlap between the position basis and the character
basis of `Z_N` is uniform. At `N=3`, every overlap magnitude-squared is
`1/3`.

## Proof

Each `omega_N^(j k)` is a unit complex number. Therefore

```text
|F_N[j,k]|^2
  = |omega_N^(j k)|^2 / N
  = 1 / N.
```

The Schur orthogonality statement for the one-dimensional irreducible
characters of `Z_N` is the same normalized character-table fact in
inner-product form.

## Boundaries

This note does **not**:

- identify any PMNS matrix column with a `Z_N` character vector;
- derive a framework PMNS residual symmetry;
- import or prove K-theoretic machinery;
- connect this value to any dynamics-lane invariant;
- use empirical inputs;
- introduce a new axiom, admitted premise, or theory lane.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/cyclic_dft_uniform_magnitude_runner.py
```

Expected:

```text
TOTAL: PASS=19 FAIL=0
VERDICT: cyclic DFT uniform magnitude theorem holds.
```
