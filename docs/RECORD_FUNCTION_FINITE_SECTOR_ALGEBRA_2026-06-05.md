# Record Function Finite Sector Algebra

**Date:** 2026-06-05
**Claim type:** positive_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note does not set, predict, or propose an
audit outcome.
**Primary runner:** [`scripts/record_function_finite_sector_algebra_2026_06_05.py`](../scripts/record_function_finite_sector_algebra_2026_06_05.py)
(sympy + finite subset checks; **SCORECARD 32 PASS / 0 FAIL**).
**Cached log:** [`logs/runner-cache/record_function_finite_sector_algebra_2026_06_05.txt`](../logs/runner-cache/record_function_finite_sector_algebra_2026_06_05.txt).

## Scope and honesty

This note isolates the algebra that follows from the 2026-06-05 **Record**
axiom:

```text
Given a supplied finite record-sector decomposition, scalar readout is
finitely additive over disjoint records.
```

The resulting object is a finite **record function**: a sector readout vector.
This is useful because many downstream claims need ratios, normalized
coordinates, coarse-grainings, and stability coordinates. But this note does
not turn record readout into Born probability, dynamics, source/action,
occupancy, or a value selector.

## Theorem

Let a supplied finite record decomposition have sectors

```text
R_0, ..., R_(n-1)
```

and scalar readouts

```text
v_i = I(R_i).
```

Then the record function is the finite vector

```text
v = (v_0, ..., v_(n-1)).
```

For any finite union of sectors `A`, with indicator vector `chi_A`,

```text
I(A) = chi_A . v.
```

If `A` and `B` are disjoint, then

```text
I(A union B) = I(A) + I(B).
```

The runner verifies this for all `81` ordered disjoint pairs of subsets of a
four-sector test decomposition.

## Coarse-graining

A finite coarse-graining is an incidence matrix `C`. The coarsened record
function is

```text
w = C v.
```

If the coarse-graining is a partition of the original sectors, each original
sector appears in exactly one coarse block, equivalently

```text
1_m C = 1_n.
```

Then total readout is preserved:

```text
sum_j w_j = sum_i v_i.
```

Repeated coarse-graining composes associatively:

```text
D(Cv) = (DC)v.
```

This is the finite algebraic content that Record makes available for later
dynamics. It is not yet a probability calculus.

## Ratios and normalized coordinates

For a two-sector record function

```text
v = (u, d),     u+d != 0,     u != 0,
```

the normalized coordinates

```text
p_0 = u/(u+d),     p_1 = d/(u+d)
```

sum to one and are invariant under global readout scaling. The raw ratio

```text
rho = d/u
```

is also scale-invariant under a nonzero global scale. These are structural
readout coordinates. Calling them probabilities requires a separate
normalization/Born gate.

Finite additivity leaves the normalized coordinate arbitrary: for any supplied
`p` in `(0,1)`, choosing

```text
d = p u / (1-p)
```

gives `d/(u+d)=p`. Thus Record alone cannot select a value.

## Conditional abstract `C3` two-block coordinate

This specialization is conditional. Supply:

1. a real `C3` spectrum `lambda` obtained from an abstract
   Hermitian-circulant element `H(a,b)`; and
2. an identification of two scalar record coordinates with one third of the
   trivial and doublet Fourier-projection powers of that spectrum.

Neither supplied input follows from Record. In particular, this note does not
select a physical carrier, identify the coordinates with generations, supply
a `K`/CPT readout context, or construct a registered-mass functional.

The
[Abstract Hermitian-Circulant Fourier Invariant Theorem](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
establishes the first algebraic input: with `C` the cyclic shift,
`omega = exp(2 pi i/3)`, and
`f_k = (1, omega^k, omega^(2k))^T/sqrt(3)` satisfying `C f_k = omega^k f_k`,

```text
Herm_circ(3) = { H(a,b) = a I + b C + conjugate(b) C^2 : a in R, b in C },
lambda_k     = a + b omega^k + conjugate(b) omega^(-k),
```

and those `lambda_k` "are real for all `a in R` and `b in C`". The `f_k` are
orthonormal, `f_0` carries the trivial character and `(f_1,f_2)` carry the
two-dimensional block, so the readout power splits over the two isotypic
sectors as

```text
|<f_0, lambda>|^2                     = 3a^2,
|<f_1, lambda>|^2 + |<f_2, lambda>|^2 = 6|b|^2.
```

Under supplied input 2, dividing out the common factor `3` defines the two
record coordinates:

```text
singlet readout = a^2,
doublet readout = 2|b|^2.
```

For `a != 0`, define

```text
r = |b|^2/a^2,
rho = doublet/singlet,
```

we have

```text
rho = 2r.
```

When also `b != 0`, `rho>0` and the logarithmic dial coordinate is

```text
s = log2(rho) = log2(2r).
```

At `b=0`, `rho=0`; the logarithmic dial is absent and `arg(b)` has no defined
phase. For `b != 0`, write `theta = arg(b)`. The real spectrum then has the
equivalent character form

```text
lambda_k = a + 2|b| cos(theta + 2 pi k/3),     k=0,1,2.
```

For `a != 0`, so that `sum_k lambda_k = 3a != 0`, define the structural
three-slot coordinate

```text
Q = (sum_k lambda_k^2) / (sum_k lambda_k)^2.
```

The `C3` character sums give, exactly,

```text
sum_k lambda_k     = 3a,
sum_k lambda_k^2   = 3a^2 + 6|b|^2.
```

Therefore this packet derives the displayed abstract coordinate formula
before substituting endpoints:

```text
Q = (3a^2 + 6|b|^2)/(3a)^2 = 1/3 + (2/3)r.
```

Equivalently, in the two-block record-function notation above,

```text
Q = (singlet readout + doublet readout)/(3 singlet readout).
```

The
[Registered Positive Mass Triple: Exact C3 Fourier Coordinates and Koide Identity](CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)
independently establishes the same Fourier reconstruction and `Q` identity
when a strictly positive real triple `z_j = sqrt(m_j)` is already supplied.
In that domain `a>0`, and its phase is defined only when its nontrivial Fourier
coefficient is nonzero. That theorem does not construct the physical
registered-mass readout or supply the Record-to-power identification assumed
here.

This is therefore an abstract structural coordinate under two explicit
inputs, not a probability, dynamics, occupancy selector, generation
assignment, or measured-mass assertion.

The named endpoints are:

```text
rho=1 -> s=0 -> r=1/2 -> Q=2/3    (interior coordinate)
rho=2 -> s=1 -> r=1   -> Q=1      (formal real-spectrum endpoint)
```

The `Q=1` value is not attained by a strictly positive triple because

```text
(sum_k lambda_k)^2 - sum_k lambda_k^2
  = 2 sum_(i<j) lambda_i lambda_j > 0.
```

It is a nonnegative-closure value, for example at a permutation of
`(3a,0,0)`, or a formal value of the unrestricted real-spectrum algebra. The
runner verifies the identities and domains exactly and verifies that `rho`
remains a free readout ratio until a weighting or dynamics gate is supplied.

## What this unlocks

This is the small reusable row that the dynamics push needs:

1. Record gives finite additive sector vectors.
2. Coarse-grainings are incidence matrices.
3. Ratios and normalized coordinates are valid structural coordinates.
4. No probability or dynamics is implied.

Downstream dynamics claims can now cite this instead of smuggling in a hidden
Born or source/action premise. It also gives a clean basis for rewriting older
observable-principle rows: if a row only needs finite additive sector readout,
it can depend on record-function algebra; if it needs weights, probability, or
time evolution, that extra gate must be named.

## Runner coverage

The runner verifies:

- finite additivity over all ordered disjoint subset pairs in a four-sector
  model;
- singleton decomposition and empty-union readout;
- coarse-graining by incidence matrix;
- total preservation for partition coarse-grainings;
- associative composition of coarse-grainings;
- scale invariance of normalized coordinates and ratios;
- arbitrariness of two-sector normalized coordinates under Record alone;
- the conditional abstract `C3` specialization `rho=2r`,
  `s=log2(rho)`, and the domains and status of the two named endpoints;
- the finite real-`C3` power-sum definition of `Q`, deriving
  `Q = 1/3 + (2/3)r` before endpoint substitution;
- that both cited authority notes exist, that this note links to each of them,
  and that each one's live sharded ledger row remains dependency-eligible as a
  pipeline compatibility check, not a proof of semantic scope;
- exactly, from `lambda_k = a + b omega^k + conjugate(b) omega^(-k)`: reality
  of every `lambda_k`, the equivalent character form
  `a + 2|b| cos(theta + 2 pi k/3)`, orthonormality of the `f_k`, the isotypic
  power split `3a^2 : 6|b|^2`, the power sums `3a` and `3a^2 + 6|b|^2`, their
  agreement with `3 (singlet + doublet)`, and `Q = 1/3 + (2/3)r`;
- a discriminating rejector: the alternative assignment `doublet = |b|^2`
  is not the same polynomial identity for nonzero `b`, while both assignments
  correctly coincide at the degenerate boundary `b=0`;
- two distinct supplied update maps preserve finite additivity, so Record does
  not select dynamics.

## Net

Record-function algebra is a retained-candidate scaffold, not a physical
selection principle. It is exactly the algebra needed to talk cleanly about
record-sector dials and dynamics without overclaiming probability or value
selection.
