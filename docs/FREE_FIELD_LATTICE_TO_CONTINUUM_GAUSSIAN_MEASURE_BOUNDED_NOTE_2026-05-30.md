# Free Dirac Gaussian Measure From Smeared Covariance (Bounded Support)

**Date:** 2026-05-30
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not quote, set, or predict audit outcomes.
**Primary runner:** [`scripts/free_field_lattice_to_continuum_gaussian_measure_2026-05-30.py`](../scripts/free_field_lattice_to_continuum_gaussian_measure_2026-05-30.py)

## 0. Scope

This note records a narrow free-field measure-convergence reduction for the
massive free Dirac Gaussian/quasi-free theory. It is intended as bounded support
for later free-sector reconstruction work, not as a reconstruction theorem.

The load-bearing covariance input is the free staggered-Dirac two-point from
[`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md):

```text
S_a(p) = (m 1 - i sum_mu gamma_mu sin(p_mu a)/a) / Delta_a(p),
Delta_a(p) = m^2 + sum_mu (sin(p_mu a)/a)^2,
S(p) = (m 1 - i gamma.p) / (m^2 + |p|^2),
```

with fixed `m > 0`, Euclidean Hermitian gamma matrices, pointwise
`S_a(p) -> S(p)` at fixed physical momentum, and taste appearing as a four-fold
spectral multiplicity in the cited covariance packet.

The note proves/reduces two bounded statements:

1. For a specified free fermionic Gaussian/quasi-free state, convergence of the
   smeared covariance pairings `<f, S_a g> -> <f, S g>` for Schwartz spinor tests
   implies convergence of every fixed finite Schwinger function, because the
   fermionic Wick/Pfaffian map is polynomial in the covariance entries. This is
   textbook Gaussian/quasi-free rigidity, not a derivation of the statistics
   choice.
2. For the covariance above, the pointwise convergence upgrades to the smeared
   Schwartz-test sense by dominated convergence. The explicit bound is

```text
||S_a(p)||_F^2 = 4 / Delta_a(p),
||S_a(p)||_F <= 2 / sqrt(Delta_a(p)),
Delta_a(p) >= m^2.
```

For every fixed Schwartz pair `f,g`, the integrand is bounded by
`(2/m) |f(p)| |g(p)|`, which is integrable. On the central Brillouin-zone half,
Jordan's inequality also gives the sharper envelope
`2 / sqrt(m^2 + (2/pi)^2 |p|^2)`.

No one-dimensional transfer-matrix bridge is used in this reduction. The
separate lattice reflection-positivity transfer-matrix note is corroborating
context for free-lattice positivity, not a load-bearing dependency for the
measure-convergence step proven here.

## 1. Gaussian/quasi-free rigidity

For a free fermionic Gaussian/quasi-free state, the even Schwinger functions are
Pfaffians of the antisymmetric two-point matrix:

```text
<chi_i1 ... chi_i(2n)> = Pf(S_[i_a,i_b]).
```

The map from the two-point entries to any fixed `2n`-point function is a finite
polynomial. Hence if the smeared two-point matrix entries converge, the
corresponding fixed finite Schwinger functions converge. Equivalently, the
Grassmann generating functional for a quasi-free state is fixed by the two-point
form.

This is a conditional statement inside the free fermionic Gaussian category. It
does not select fermionic CAR statistics over a bosonic Gaussian alternative; the
statistics choice is a separate input/open problem in the free-sector program.
The runner's finite Pfaffian checks are sanity checks for the polynomial
continuity, not a substitute for the textbook quasi-free theorem.

## 2. Pointwise-to-smeared upgrade

OS reconstruction consumes Schwinger functions as tempered distributions, so the
relevant two-point convergence is smeared:

```text
<f, S_a g> = integral d^4p  fbar(p) S_a(p) g(p)  ->  <f, S g>
```

for Schwartz spinor tests `f,g`. The cited covariance packet supplies pointwise
convergence of `S_a(p)` to `S(p)` at fixed physical momentum. For fixed `m > 0`,
the Frobenius norm obeys

```text
||S_a(p)||_F^2 = 4 / Delta_a(p),    Delta_a(p) >= m^2,
```

so

```text
|fbar(p) S_a(p) g(p)| <= (2/m) |f(p)| |g(p)|.
```

The right-hand side is integrable because `f` and `g` are Schwartz. Dominated
convergence therefore permits the `a -> 0` limit to pass through the momentum
pairing and yields the required smeared covariance convergence. This is the only
analysis step beyond pointwise covariance convergence.

The runner also checks the sharper central-zone inequality
`Delta_a(p) >= m^2 + (2/pi)^2 |p|^2` when `|p_mu a| <= pi/2`, but the simple
`2/m` Schwartz-weighted envelope is enough for fixed positive mass.

## 3. Taste and non-triviality checks

The runner checks a 16-dimensional reduced staggered object built from canonical
hypercube phase matrices. It verifies that `M_a(p)^dag M_a(p)` has scalar
spectrum `Delta_a(p)` with multiplicity divisible by four and that
`Delta_a(p) -> m^2 + |p|^2`. This is a spectrum/multiplicity statement only; it
does not introduce or use a finite-`a` taste-flat operator.

The runner also compares against a deliberately wrong covariance sequence with a
fixed mass offset. The correct sequence's smeared error decays under refinement,
while the wrong sequence plateaus and remains far from the target. This is a
sanity check that the convergence is not a tautology of the numerical setup.

## 4. What This Claims

- For fixed `m > 0`, the free staggered-Dirac covariance from the cited note
  converges to the continuum free Dirac covariance in the smeared Schwartz-test
  sense.
- Within the free fermionic Gaussian/quasi-free category, smeared covariance
  convergence implies convergence of every fixed finite Schwinger function and
  the corresponding Grassmann generating functional.
- The free-field measure-convergence step does not require the separate
  one-dimensional transfer-matrix bridge.
- Taste enters this covariance packet as four-fold spectral multiplicity, not as
  a finite-`a` taste-flat operator.

## 5. What This Does Not Claim

- It does not prove the abstract OS-to-Wightman reconstruction theorem.
- It does not prove spin-statistics or select CAR statistics from the framework.
- It does not prove boost covariance, microcausality, emergent Lorentz symmetry,
  or an interacting `SU(3)`/`U(1)` result.
- It does not treat the massless limit or uniformity as `m -> 0`.
- It does not add an axiom, Tier-A admission, new vocabulary, fitted value,
  measured input, or audit status.
- It does not claim any downstream free-sector program gap is unconditionally
  closed.

## 6. Runner

```bash
python3 scripts/free_field_lattice_to_continuum_gaussian_measure_2026-05-30.py
```

Expected result: `SCORECARD PASS=6 FAIL=0`.

The runner checks:

- Pfaffian polynomial identities for finite fermionic Gaussian moments.
- Gaussian/quasi-free covariance-to-functional continuity on finite test data.
- Smeared convergence of `S_a` to `S`, and induced convergence of a finite
  Pfaffian four-point.
- Four-fold spectral multiplicity of the reduced staggered spectrum.
- A non-converging mass-offset control.
- The dominated-convergence envelope `||S_a||_F^2 = 4/Delta_a`.

## 7. Load-Bearing Dependency

- [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  supplies the covariance formula, pointwise continuum limit, and taste
  multiplicity input used here.

Textbook methodology used as non-graph context: standard fermionic Wick/Pfaffian
quasi-free-state rigidity, Gaussian characteristic/generating-function
continuity, Schwartz-test dominated convergence, and the OS convention that
Schwinger functions are consumed as tempered distributions.
