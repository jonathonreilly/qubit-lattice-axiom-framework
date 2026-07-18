# Defined Matrix-Trace Taylor and Formal Coefficient-Matching Theorem

**Date:** 2026-06-07. Dependency-free scope repair: 2026-07-16.
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py`](../scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py)
**Cached log:**
[`logs/runner-cache/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.txt`](../logs/runner-cache/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.txt)

## Purpose and repair

The earlier version started from a supplied action, a supplied exponential
dictionary, and a supplied continuum coefficient. Its algebra was correct
inside that packet, but those inputs were not derived by the note. This repair
removes every physical identification from the theorem and **withdraws** the
prior conditional physical proposition on this row: the earlier
Wilson-action/continuum reading is superseded, is no longer claimed at any
strength here, and survives only in the row's archived audit history. The
stable filename is kept so existing citations can be repaired in place; the
row's live claim content is solely the formal matrix theorem below, and every
direct consumer was synchronized in the same change so that no live surface
cites the withdrawn physical reading.

The result below is an ordinary finite-dimensional matrix theorem. The symbols
`beta` and `g` are formal positive real parameters. They are not a lattice
action coefficient or a physical coupling unless a separate authority proves
such a dictionary.

## Definitions

Let `n >= 2` and let `T_1,...,T_m` be Hermitian traceless matrices in
`M_n(C)` satisfying the explicitly supplied algebraic hypotheses

```text
Tr(T_a T_b) = delta_ab / 2.
```

For real coefficients `f_a`, set

```text
A = sum_a f_a T_a,
F2 = sum_a f_a^2,
D(x) = 1 - (1/n) Re Tr exp(i x A),          x real.
```

For formal parameters `beta > 0` and `g > 0`, define two scalar coefficients

```text
C_left(beta,g,n) = beta g^2 / (4 n),
C_right           = 1/2.
```

These definitions are all the data used by the theorem. In particular, the
labels do not carry an action, plaquette, continuum, gauge-field, or coupling
interpretation.

## Theorem

Under the definitions above:

1. `D(0) = 0` and `D'(0) = 0`.
2. `D''(0) = Tr(A^2)/n = F2/(2n)`.
3. The even Taylor coefficient is therefore

   ```text
   [x^2] D(x) = D''(0)/2 = F2/(4n).
   ```

4. For every real `x`, the second-order remainder obeys

   ```text
   |D(x) - x^2 Tr(A^2)/(2n)|
       <= |x|^4 Tr(A^4)/(24n).
   ```

5. Consequently the coefficient of `x^2 F2` in the **defined** expression
   `beta D(gx)` is `C_left = beta g^2/(4n)`. Equality with the separately
   **defined** coefficient `C_right = 1/2` holds exactly when

   ```text
   C_left = C_right
       <=> beta g^2/(4n) = 1/2
       <=> beta g^2 = 2n
       <=> beta = 2n/g^2.
   ```

This last line is a formal coefficient equivalence between two defined
quadratic expressions. It is not a derivation of a physical normalization.

## Proof

Because `A` is Hermitian, the spectral theorem gives real eigenvalues
`lambda_1,...,lambda_n` and

```text
D(x) = (1/n) sum_j (1 - cos(x lambda_j)).
```

Differentiating this finite sum gives `D(0)=D'(0)=0` and

```text
D''(0) = (1/n) sum_j lambda_j^2 = Tr(A^2)/n.
```

The supplied Gram relation gives

```text
Tr(A^2)
  = sum_ab f_a f_b Tr(T_a T_b)
  = (1/2) sum_a f_a^2
  = F2/2,
```

which proves items 1--3. Taylor's theorem for the real scalar function
`1-cos y` has fourth derivative `-cos y`, whose absolute value is at most
one. Thus

```text
|1 - cos y - y^2/2| <= |y|^4/24.
```

Apply this inequality to every `y=x lambda_j`, sum, divide by `n`, and use
`sum_j lambda_j^4 = Tr(A^4)` to obtain item 4. Substituting `gx` for `x`
and multiplying by `beta` gives item 5 by exact scalar algebra.

### Tracelessness and the linear term

The real-part deficit has `D'(0)=0` for **every Hermitian** `A`, even if
`Tr(A) != 0`, because `Re(i Tr A)=0`. Tracelessness instead removes the
linear term of the complex deficit

```text
Z(x) = 1 - (1/n) Tr exp(i x A),
Z'(0) = -(i/n) Tr(A).
```

The runner tests this distinction explicitly. It rejects a nontraceless
fixture because it violates the theorem hypotheses and produces a nonzero
complex linear term; it does not falsely claim that nontracelessness makes
`D'(0)` nonzero.

## Independent executable routes

The runner provides four selectable modes:

- `normal`: exact Gram-contraction and matrix-derivative checks;
- `independent`: a separate spectral/power-series reconstruction;
- `hostile`: single-field mutations of the hypotheses, derivative
  normalization, and formal coefficient equation, plus an interface
  fail-closed contract check;
- `intentional-failure`: promotes one rejected hostile mutation to a primary
  assertion and must exit nonzero.

The hostile set covers wrong trace normalization, a nontraceless complex
linear term, a non-real (complex) coefficient, omission of `1/n`, confusion
of `D''(0)` with its half-sized Taylor coefficient, replacement of
`C_right=1/2` by `1/4`, the wrong product `beta g^2=n`, the wrong solve
`beta=2n/g`, an actual `beta` inconsistent with the proposed formulas, and a
false `1/48` fourth-order remainder constant. Each coefficient fixture
mutates exactly one field of the canonical packet, so each rejection is
attributable to its named false claim. The final hostile item is an
interface contract check: the module's only physical-inference entry point
refuses every request by construction. That is a fail-closed API contract,
not a repository-wide detection scan; the claim-boundary policing for
consumers lives in the Boundary section below and in each consumer's own
runner. The independent route also checks a complex off-diagonal `n=4`
basis, while the normal route checks the zero-matrix edge case and the
exact fourth-derivative mechanism.

## Boundary and downstream citation rule

This theorem does **not** derive or select:

- a Wilson or any other lattice action;
- a plaquette/exponential dictionary for a gauge field;
- a Yang--Mills or other continuum coefficient;
- a trace convention as a framework fact (the Gram relation is an explicit
  finite-dimensional hypothesis here);
- a physical meaning or value for `beta` or `g`;
- a continuum limit, running coupling, observable, or comparator;
- an audit verdict or effective-status promotion.

Downstream notes may cite this row for the matrix Taylor identities and the
formal equivalence `C_left=C_right <=> beta g^2=2n`. They may not cite it as
authority for an action surface, a physical matching demand, a coupling
dictionary, or a value such as a chosen normalization point. Any such bridge
must be supplied and audited separately.

## Verification

```text
python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py --mode normal
python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py --mode independent
python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py --mode hostile
```

Every hostile fixture may also be promoted with
`--mode intentional-failure --inject-failure <fixture>`; each such run is
expected to exit nonzero.
