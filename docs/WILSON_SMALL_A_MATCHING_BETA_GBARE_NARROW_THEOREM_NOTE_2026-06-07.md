# Abstract Hermitian Matrix-Trace Deficit Taylor and Global Remainder Theorem

**Date:** 2026-06-07. Abstract-matrix scope repair: 2026-07-18.
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py`](../scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py)
**Cached log:**
[`logs/runner-cache/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.txt`](../logs/runner-cache/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.txt)

## Scope

The earlier version started from a supplied action, a supplied exponential
dictionary, and a supplied continuum coefficient. Its algebra was correct
inside that packet, but those inputs were not derived by the note. This repair
removes every physical identification from the theorem and **withdraws** the
prior conditional physical proposition on this row: the earlier
Wilson-action/continuum reading is superseded, is no longer claimed at any
strength here, and survives only in the row's archived audit history. The
stable filename is kept so existing citations can be repaired in place; the
row's live claim content is solely the native finite-dimensional matrix
theorem below. It has no comparison coefficient, parameter-selection rule, or
interpretation outside the matrix problem defined here.

## Hypotheses and definitions

Let `n >= 1`. Supply a finite family `T_1,...,T_m` in `M_n(C)` satisfying

```text
T_a = T_a^dagger,
Tr(T_a T_b) = delta_ab / 2.
```

Let `f_1,...,f_m` be real and define

```text
A  = sum_a f_a T_a,
F2 = sum_a f_a^2,
D(x) = 1 - (1/n) Re Tr exp(i x A),       x real.
```

The empty family is allowed, in which case `A=0` and `F2=0`. No tracelessness
hypothesis is imposed.

## Theorem

Under exactly those hypotheses:

1. `D(0)=0` and `D'(0)=0`.
2. `D''(0)=Tr(A^2)/n=F2/(2n)`.
3. The quadratic Taylor coefficient is

   ```text
   [x^2]D(x) = D''(0)/2 = F2/(4n).
   ```

4. For every real `x`, globally rather than only asymptotically,

   ```text
   |D(x) - x^2 Tr(A^2)/(2n)|
       <= |x|^4 Tr(A^4)/(24n).
   ```

5. For supplied real scalars `w,s`, rescaling alone gives the homogeneous
   quadratic term

   ```text
   [x^2] w D(sx) = w s^2 F2/(4n).
   ```

   Equivalently, when `m>=1` and `f_a,w,s` are treated as commuting formal
   indeterminates over the reals, the coefficient multiplying the named
   quadratic form `x^2 F2` is

   ```text
   [x^2 F2] w D(sx) = w s^2/(4n).
   ```

Item 5 is only substitution `x -> sx` followed by multiplication by `w`.
It does not compare the resulting coefficient with another expression and
does not select either scalar. For the empty family, the first display is the
zero identity; the separate coefficient-of-`F2` notation is simply omitted.

## Proof

Real coefficients and Hermiticity of every `T_a` make `A` Hermitian. By the
finite-dimensional spectral theorem there is a unitary matrix `U` and real
eigenvalues `lambda_1,...,lambda_n`, with multiplicity, such that

```text
A = U diag(lambda_1,...,lambda_n) U^dagger.
```

Trace invariance and functional calculus therefore give

```text
D(x) = (1/n) sum_j (1 - cos(x lambda_j)).
```

Termwise differentiation of this finite sum yields

```text
D'(x)  = (1/n) sum_j lambda_j sin(x lambda_j),
D''(x) = (1/n) sum_j lambda_j^2 cos(x lambda_j).
```

At zero this proves `D(0)=D'(0)=0` and

```text
D''(0) = (1/n) sum_j lambda_j^2 = Tr(A^2)/n.
```

Only the supplied Gram relation is needed to rewrite this matrix quantity in
component coordinates:

```text
Tr(A^2)
  = sum_ab f_a f_b Tr(T_a T_b)
  = (1/2) sum_a f_a^2
  = F2/2.
```

Dividing the second derivative by `2!` proves the quadratic coefficient.

For the global bound, Taylor's theorem applied to the scalar function
`1-cos y` through degree three gives, for every real `y`,

```text
|1 - cos y - y^2/2| <= |y|^4/24,
```

because its fourth derivative is `-cos y`, whose absolute value is at most
one on the entire real line. Apply this inequality to each
`y=x lambda_j`, sum, divide by `n`, and use
`sum_j lambda_j^4=Tr(A^4)`. This proves item 4. Substitution and scalar
multiplication prove item 5.

## Exact use of the hypotheses

- `n>=1` makes the normalized trace defined; the proof does not require
  `n>=2`.
- Real `f_a` and Hermitian `T_a` are used to make `A` Hermitian. Hermiticity
  supplies the real spectrum and the cosine representation used by the
  derivative and remainder arguments.
- The Gram relation is used only for
  `Tr(A^2)=F2/2` and the resulting component-coordinate coefficients.
- Tracelessness is not used. For any Hermitian `A`, even with
  `Tr(A) != 0`, the real-part derivative vanishes because
  `Re(i Tr A)=0`.
- The real-scalar statement for `w,s` and its formal-polynomial restatement
  use only commuting scalar multiplication; no positivity or invertibility is
  needed.

For comparison with the real-part statement only, the complex deficit

```text
Z(x) = 1 - (1/n) Tr exp(i x A)
```

has `Z'(0)=-(i/n)Tr(A)`, which need not vanish. This observation does not add
a hypothesis to the theorem; it prevents confusing the two deficit
functions.

## Edge cases

The proof already includes the following cases without extra assumptions:

- `A=0`, including an empty family or all-zero coefficients: both sides of
  every displayed identity and the remainder bound vanish;
- rank-deficient `A`: zero eigenvalues contribute zero;
- repeated eigenvalues: multiplicities are included in the finite spectral
  sum;
- negative eigenvalues: cosine and the even spectral moments require no sign
  restriction;
- `n=1`, whenever a supplied family satisfies the Gram relation;
- Hermitian matrices with nonzero complex off-diagonal entries.

## Executable evidence

The runner provides independent proof and falsification routes:

- `normal`: exact matrix derivatives, Gram contraction, the scalar remainder
  mechanism, formal coefficient extraction, and the zero and `n=1` cases;
- `independent`: a separate spectral power-series reconstruction plus a
  numerical complex-off-diagonal Hermitian reconstruction, including the
  rank-deficient/repeated/negative cases, that does not use the normal route's
  expected-value table;
- `hostile`: recomputed mutations for a wrong Gram factor, omitted `1/n`,
  confusion of `D''(0)` with `[x^2]D`, a false fourth-order constant,
  non-Hermitian input, a false complex-deficit linear statement, a wrong
  rescaling power, and an inference of an external target from the native
  coefficient;
- `intentional-failure`: promotes any rejected hostile mutation to a primary
  assertion and must exit nonzero.

The theorem counts contain only computed mathematical checks. Prose
presence, audit-ledger state, and literal pass flags are not evidence.

## Citation boundary

Downstream notes may cite this row only for the displayed matrix derivatives,
quadratic coefficient, global fourth-order bound, and the coefficient
`w s^2/(4n)` of the formally rescaled expression. Any comparison target,
parameter equation, preferred value, or interpretation outside this abstract
matrix packet requires separate authority and remains outside this theorem.

**Downstream-hygiene record (2026-07-18, PR #5502):** direct consumers were
narrowed to the displayed matrix coefficient/remainder scope or had the
dependency removed. Until a separately audited action/plaquette/continuum
bridge exists, this row must not be cited for a physical normalization.

## Verification

```text
python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py --mode normal
python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py --mode independent
python3 scripts/audit_companion_wilson_small_a_matching_beta_gbare_2026_06_07.py --mode hostile
```

Every hostile fixture may also be promoted with
`--mode intentional-failure --inject-failure <fixture>`; each such run is
expected to exit nonzero.
