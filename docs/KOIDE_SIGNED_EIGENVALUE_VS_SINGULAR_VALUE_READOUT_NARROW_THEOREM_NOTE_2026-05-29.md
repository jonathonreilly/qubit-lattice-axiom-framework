# Signed-Eigenvalue and Modulus-Vector Koide Functionals: Narrow Algebraic Theorem

**Date:** 2026-05-29

**Type:** positive_theorem

**Claim scope:** exact identities, inequalities, phase cells, and explicit
samples for two scalar functionals of the real spectrum of an abstract
`C_3`-circulant Hermitian matrix.

**Primary runner:**
[`scripts/frontier_koide_signed_vs_singular_value_readout_narrow.py`](./../scripts/frontier_koide_signed_vs_singular_value_readout_narrow.py)

This note concerns only the algebra defined below. The quantities `λ_k²` are
component squares. Species, mass, Yukawa, and other physical-observable
interpretations are outside the claim scope. The value `r = 1/2` is an explicit
hypothesis rather than a selected parameter. Empirical and framework-readout
identifications are likewise outside the claim scope.

## Definitions

Let `C` be the standard `3×3` cyclic permutation matrix,
`ω = exp(2πi/3)`, `a ∈ ℝ_{>0}`, and `b ∈ ℂ`. Choose `θ ∈ ℝ` such that
`b = |b| exp(iθ)`; when `b = 0`, `θ` may be chosen arbitrarily. Define

```text
H = aI + bC + b̄C².                                                            (1)
```

The three real eigenvalues are

```text
λ_k = a + bω^k + b̄ω^{-k}
    = a + 2|b| cos(θ + 2πk/3),                 k = 0,1,2.                     (2)
```

Set

```text
S := (λ_0, λ_1, λ_2),             V := (|λ_0|, |λ_1|, |λ_2|),
Q(w) := (Σ_k w_k²)/(Σ_k w_k)²,    r := |b|²/a².                              (3)
```

For phase-cell statements define the centered distance

```text
d(θ) := min_{n∈ℤ} |θ - 2πn/3|,        0 ≤ d(θ) ≤ π/3.                        (4)
```

This definition removes the ambiguity of an unsigned ordinary remainder near
the right endpoint of a `2π/3` period.

## Theorem

The following statements hold for every `a > 0`, `b ∈ ℂ`, and compatible `θ`
chosen as above.

1. The signed-vector functional is phase-independent:

   ```text
   Q(S) = (a² + 2|b|²)/(3a²) = (1 + 2r)/3.                                  (5)
   ```

   In particular, `Q(S) = 2/3` when `r = 1/2`.

2. The two vectors have the same component-square sum:

   ```text
   Σ_k |λ_k|² = Σ_k λ_k² = 3a² + 6|b|².                                     (6)
   ```

3. The modulus-vector functional satisfies

   ```text
   Q(V) = (3a² + 6|b|²)/(Σ_k |λ_k|)² ≤ Q(S),                                (7)
   ```

   with equality exactly when every `λ_k ≥ 0`. The zero-component boundary is
   included in the equality case.

4. At `r = 1/2`, `Q(V)` is nonconstant in `θ`. Exact values include

   ```text
   Q(V)(0)   = 2/3,
   Q(V)(π/3) = 6/(9 + 4√2),
   Q(V)(π/2) = 6/(7 + 2√6).                                                   (8)
   ```

   Numerical illustrations are `Q(V)(0.4) ≈ 0.565798` and
   `Q(V)(0.9) ≈ 0.415985`.

5. At `r = 1/2`, the phase cells are

   ```text
   every λ_k > 0             ⇔ d(θ) < π/12,
   Q(V) = Q(S) = 2/3         ⇔ d(θ) ≤ π/12,
   Q(V) < Q(S) = 2/3         ⇔ d(θ) > π/12.                                 (9)
   ```

   At each endpoint `d(θ) = π/12`, one eigenvalue is zero and the other two
   are positive.

6. On any region with exactly one negative eigenvalue `λ_min`,

   ```text
   Σ_k |λ_k| = 3a - 2λ_min,
   Q(V) = (3a² + 6|b|²)/(3a - 2λ_min)² < Q(S).                              (10)
   ```

   The specialization `r = 1/2` gives `Q(V) < 2/3`. The hypothesis matters:
   `a = 1`, `b = 19/20 - i√3/20` gives the spectrum
   `(29/10, 1/5, -1/10)` and the exact values
   `Q(V) = 423/512 > 2/3`, `Q(S) = 47/50`.

## Proof

The root-of-unity identities

```text
Σ_k cos(θ + 2πk/3) = 0,
Σ_k cos²(θ + 2πk/3) = 3/2
```

give

```text
Σ_k λ_k = 3a,
Σ_k λ_k² = 3a² + 6|b|².                                                       (11)
```

Substitution into `Q(S)` proves (5), and realness of each `λ_k` proves (6)
term by term.

For (7), `a > 0` gives `Σ_k λ_k = 3a > 0`. The real triangle inequality gives

```text
Σ_k |λ_k| ≥ |Σ_k λ_k| = 3a.                                                   (12)
```

Equality in (12) holds exactly when all three summands are nonnegative: an
all-nonpositive triple would have nonpositive sum, contrary to `3a > 0`.
Squaring (12) and using the shared numerator proves (7) and its equality
condition.

For (8), set `a = 1`, `|b| = 1/√2`; scale invariance permits this
normalization. The three spectra at `θ = 0, π/3, π/2` have modulus sums
`3`, `1 + 2√2`, and `1 + √6`, respectively, while the shared square sum is
`6`. This gives the three displayed values, which are pairwise distinct.

For (9), write the spectrum at `r = 1/2` as

```text
λ_k/a = 1 + √2 cos(θ + 2πk/3).                                                (13)
```

On the centered fundamental interval `[-π/3, π/3]`, the first zero crossings
occur at `θ = ±π/12`, because the limiting mode has cosine `-1/√2` there.
Continuity and the absence of any other zero in the interval give strict
positivity inside and one negative component outside. Periodicity by `2π/3`
then yields the centered-distance classification in (9). Equation (7) supplies
the corresponding equality and strict-inequality statements.

Finally, with exactly one negative component,
`Σ|λ_k| = Σλ_k - 2λ_min = 3a - 2λ_min`, proving (10). For the displayed
counterexample, direct character evaluation reproduces
`(29/10, 1/5, -1/10)`; substitution gives `423/512` and `47/50` exactly. ∎

## Scope boundary

The theorem establishes two different scalar functions on one abstract real
eigenvalue triple. Operator-to-observable maps, species assignments, parameter
selectors, and physical preferences between `S` and `V` are outside its
premises. In particular, a physical interpretation of a nonnegative square
root would use `|λ_k|`; a negative `λ_k` is only a signed algebraic component
here.

## Runner coverage

The paired runner declares this note through `AUDIT_INPUT_PATHS`. It checks the
matrix/eigenvalue formulas and phase-independent identities symbolically, and
it checks the displayed exact values, boundary representatives, and rational
counterexample directly. The universal inequality, equality condition, and
complete centered phase-cell classification are proved above; the runner's
finite phase samples are witnesses and regression checks, not an exhaustive
enumeration of the continuous parameter domain.

The canonical cache is valid only when both the runner hash and declared-input
fingerprint match the final reviewed bytes.
