# Gauge Wilson SU(3) All-Weight Positive-Coefficient Formal Bridge

**Date:** 2026-06-07
**Type:** exact-support bridge theorem
**Claim scope:** framework-native bridge for two all-weight facts used by
gauge-vacuum plaquette residual-environment notes:

1. For every `beta > 0` and every dominant `SU(3)` weight
   `(p,q) in P_+`, the one-link Wilson class function
   `w_beta(U) = exp[(beta/6)(chi_(1,0)(U) + chi_(0,1)(U))]` has a
   strictly positive Peter-Weyl character coefficient `c_(p,q)(beta)`.
2. Any all-weight coefficient sequence `(z_(p,q))` defines a formal central
   character distribution on the finite-character test algebra, with
   unnormalized convolution action
   `C_Z chi_(p,q) = z_(p,q) chi_(p,q)` on each basis character. This is a
   formal/distribution statement only; it is not an `L^2`, continuous
   class-function, or bounded-operator closure without a separate decay
   theorem.

**Primary runner:**
[`scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py`](../scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py)

**Status authority:** independent audit lane only. This bridge does not set an
audit verdict and does not edit audit ledger files.

## Statement

Let `V = 3 direct_sum 3bar`, so that

```text
chi_V = chi_(1,0) + chi_(0,1).
```

For `beta >= 0`,

```text
w_beta(U) = exp[(beta/6) chi_V(U)]
          = sum_{n >= 0} (beta/6)^n chi_V(U)^n / n!.
```

The product `chi_V^n` is the character of `V^{tensor n}`. Therefore its
expansion into irreducible `SU(3)` characters has non-negative integer
coefficients: the coefficients are tensor-product multiplicities.

For any dominant weight `(p,q)`, the irrep `V_(p,q)` occurs in

```text
Sym^p(3) tensor Sym^q(3bar) subset V^{tensor (p+q)}
```

as its Cartan highest-weight component. Hence the coefficient of
`chi_(p,q)` in `chi_V^(p+q)` is at least one. When `beta > 0`, the
`n = p+q` term of the exponential contributes a strictly positive amount
to `c_(p,q)(beta)`, and all other terms contribute non-negatively. For
`(p,q)=(0,0)`, the `n=0` term already gives `c_(0,0)(beta) >= 1`.

Therefore:

```text
c_(p,q)(beta) > 0       for every beta > 0 and every (p,q) in P_+(SU(3)).
```

The one-link normalized convolution eigenvalue

```text
a_(p,q)(beta) = c_(p,q)(beta) / (d_(p,q) c_(0,0)(beta))
```

is also strictly positive for every `beta > 0`, because
`d_(p,q) > 0` and `c_(0,0)(beta) > 0`.

## Formal All-Weight Convolution Dictionary

Let `C_fin` be the finite-character test algebra:

```text
C_fin = direct_sum_{(p,q) in P_+} C chi_(p,q).
```

For any all-weight sequence `(z_(p,q))`, define the formal central
character distribution

```text
Z_z := sum_{(p,q) in P_+} d_(p,q) z_(p,q) chi_(p,q)
```

as an element of the algebraic dual of `C_fin`. On basis characters, the
unnormalized central convolution action is defined coefficientwise by the
Schur/Peter-Weyl diagonal rule:

```text
C_(Z_z) chi_(p,q) = z_(p,q) chi_(p,q).
```

This is enough for per-weight identities and all-weight formal diagonal
actions. It does not assert that `Z_z` is an `L^2` class function, a
continuous class function, a positive measure, or that `C_(Z_z)` is a
bounded operator on the completed Hilbert space. Those upgrades require
separate summability/decay hypotheses on `(z_(p,q))`.

## Application To The Plaquette Residual-Environment Row

This bridge supplies two missing authorities for
`GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md`:

- the strict all-weight positivity/nonzero input for the Wilson one-link
  coefficients `a_(p,q)(beta)`;
- the formal all-weight diagonal-convolution object needed when the residual
  sequence `r_(p,q)^env(beta)` has not been proven to satisfy an `L^2` or
  continuous-function decay bound.

The application remains per-weight/formal. It does not close the parent
Perron problem, does not compute framework-point `beta = 6` residual
coefficients, and does not assert full completed-Hilbert-space operator
closure.

## Forbidden Imports Check

- No observed values, PDG inputs, fitted selectors, or admitted unit
  conventions are used.
- No new framework axiom is introduced.
- No textbook theorem is imported as a black box: the strict positivity
  argument is the native tensor-product multiplicity expansion of the Wilson
  class function on the existing `SU(3)` character basis.
- External representation-theory language is parallel context only; the
  load-bearing proof is the Cartan-component occurrence inside finite tensor
  powers of `3 direct_sum 3bar`.

## Validation

The companion runner checks:

1. every sampled weight `(p,q)` has a finite witness tensor length
   `n=p+q`;
2. the strict lower-bound monomial from that witness is positive for
   `beta > 0`;
3. `a_(p,q)(beta)` is positive whenever `c_(p,q)(beta)`, `d_(p,q)`, and
   `c_(0,0)(beta)` are positive;
4. the `beta=0` boundary is not overclaimed for nontrivial weights;
5. arbitrary all-weight coefficient data gives a formal diagonal convolution
   action on finite-character test vectors;
6. the note and the downstream plaquette note expose the formal/distribution
   boundary explicitly.

Expected runner summary:

```text
TOTAL: PASS=38 FAIL=0
```
