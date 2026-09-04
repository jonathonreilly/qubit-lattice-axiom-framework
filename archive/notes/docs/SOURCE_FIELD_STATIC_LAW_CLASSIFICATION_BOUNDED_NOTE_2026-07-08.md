# Periodic-Lattice Laplacian, Compact Zero Mode, And Yukawa Response

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** Exact Fourier-symbol identities for the nearest-neighbor
periodic lattice Laplacian, together with finite-lattice numerical checks of
its compact zero mode, mean-subtracted Green functions, and the screened
`-Delta+mu^2` response.

**Primary runner:**
[`scripts/source_field_static_law_classification_2026_07_08.py`](../scripts/source_field_static_law_classification_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/source_field_static_law_classification_2026_07_08.txt`](../logs/runner-cache/source_field_static_law_classification_2026_07_08.txt)

## Operator Class

On a periodic nearest-neighbor lattice, the runner studies

```text
L_mu = -Delta + mu^2,
lambda(k) = sum_i 2(1-cos(k_i)).
```

This is a declared linear operator class. No source, field, or physical
interpretation is selected by the calculation.

## Exact Structural Facts

1. `lambda(k)>=0`, and on a connected periodic lattice its only zero is the
   constant Fourier mode `k=0`.
2. `L_0 1=0`, while `L_mu 1=mu^2 1` for `mu>0`.
3. On a compact periodic lattice, `L_0 phi=rho` is solvable only if the zero
   Fourier coefficient of `rho` vanishes. The pseudoinverse therefore solves
   the mean-subtracted equation.
4. Along a lattice axis, the screened pole obeys

   ```text
   2(cosh(1/xi)-1)=mu^2,
   xi=1/(2 asinh(mu/2)).
   ```

These facts classify the zero-mode and screening behavior of the displayed
operator. They do not establish uniqueness among broader operator classes.

## Finite-Lattice Checks

- In dimensions one, two, and three at sizes `64`, `32^2`, and `16^3`, the
  computed zero-mode multiplicity is one.
- A unit point source has zero-mode inconsistency `1.0` for `mu=0`; after mean
  subtraction the maximum residual is `1.8e-15`. For `mu=0.3`, the
  unsubtracted residual is `3.3e-16`.
- On a 64-site ring, the mean-zero Green function agrees with

  ```text
  -|x|/2 + x^2/(2L) + constant
  ```

  to `3.2e-14`.
- The three-dimensional finite-volume Green function approaches the local
  `1/(4*pi*r)` form over the printed window when the lattice grows from
  `16^3` to `24^3`.
- At `mu in {0.2,0.5}`, fitted axis decay lengths agree with the lattice
  Yukawa relation within the printed `0.1-0.5%` range.

## Boundaries

- The `d=3` radial and Yukawa comparisons are numerical finite-volume
  measurements, not exact continuum statements.
- The result does not identify an energy source, gravitational potential,
  Newtonian limit, gauge sector, or physical field.
- It does not prove that the displayed class is forced or unique among local,
  nonlinear, higher-derivative, retarded, or non-translation-invariant laws.
- Audit classification and verdict remain the responsibility of the
  independent audit lane.

## Dependencies

No prior source note is load-bearing. The lattice operator and numerical
comparisons are defined in this note and implemented by the paired runner.
