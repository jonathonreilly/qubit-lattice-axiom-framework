---
claim_id: scale_reference_a_inverse_is_not_wick_clock_parameter_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The scale-reference conversion a_sr^{-1}=M_Pl and the Wick clock parameter a_w in k4=i a_w omega are unequal types. The Euclidean OS0 form Q_E=(k4^2+k^2)/4 does not contain a_w; after substitution, omega_coeff(a_w)=-a_w^2/4 and |omega_coeff|/spatial_coeff=a_w^2 is a dimensionless ratio of quadratic coefficients. Scale-reference carries no dimensionless content and cannot select a_w in {1/2,1,2}. Kinetic isotropy is the Euclidean equality c_t=c_s, not a Wick parameter. The shared letter a is not an identification. This note does not install a_w=1, does not replace speed-preservation, and does not claim Lorentz closure."
upstream_dependencies:
  - minimal_axioms
  - scale_reference_primitive
  - kinetic_isotropy_primitive
runner: scripts/scale_reference_a_inverse_is_not_wick_clock_parameter_2026_08_13.py
---

# Scale-Reference `a^{-1}` Is Not The Wick Clock Parameter `a`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact type split between the dimensionful scale-reference conversion
and the dimensionless Wick clock ratio among quadratic coefficients.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/scale_reference_a_inverse_is_not_wick_clock_parameter_2026_08_13.py`](../scripts/scale_reference_a_inverse_is_not_wick_clock_parameter_2026_08_13.py)

## Result Up Front

The framework writes two different objects with the letter `a`. They are not
the same type, and the scale-reference primitive does not fix the Wick clock.

1. **Scale-reference `a_sr` is dimensionful.** The registered primitive is the
   single units conversion `a_sr^{-1} = M_Pl`. It carries no dimensionless
   content.
2. **Wick clock `a_w` is dimensionless.** The linear Wick map is
   `k4 = i a_w omega` with `a_w in Q\{0}`. The Euclidean OS0 form
   `Q_E = (k4^2 + k^2)/4` does not contain `a_w`. After substitution,
   `omega_coeff(a_w) = -a_w^2/4` and
   `|omega_coeff|/spatial_coeff = a_w^2` is a dimensionless ratio of quadratic
   coefficients.
3. **The types are unequal.** A units conversion cannot be identified with a
   ratio of quadratic coefficients. In particular it cannot select
   `a_w in {1/2, 1, 2}`. The value `a_w = 1/2` remains a legal dimensionless
   Wick parameter, with `omega_coeff(1/2) = -1/16`.
4. **Kinetic isotropy is not a Wick parameter.** The registered statement
   `c_t = c_s` is Euclidean coefficient equality. It is already encoded by
   `Q_E` and does not name `a_w`.
5. **This is only a type split.** Speed-preservation among linear Wick maps
   remains extra. The note does not install `a_w = 1`, does not claim that
   Planck units fix the Wick map, and does not claim Lorentz closure.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Fraction algebra on the OS0 quadratic and the registered primitive wordings separates a_sr from a_w; speed-preservation, a_w=1, and Lorentz closure remain unclaimed."
trace_class: negative_route_pruning
target_claim_id: scale_reference_a_inverse_is_not_wick_clock_parameter
target_blocker_text: "do not treat the shared letter a as an identification of the scale-reference conversion with the Wick clock parameter"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the type split and the displayed omega_coeff identities; Wick-parameter selection and Lorentz closure remain open"
hypothetical_axiom_status: "no edit, adoption, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `a_sr` for the scale-reference conversion of
[`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md):

```text
a_sr^{-1} = M_Pl.
```

That note states that this is a units conversion, not a physics axiom, and
that it carries zero dimensionless content.

Write `a_w` for the Wick clock parameter in the linear map

```text
k4 = i a_w omega,    a_w in Q\{0}.
```

The Euclidean OS0 quadratic used here is the `a_w`-free form

```text
Q_E(k4, k) = (k4^2 + k^2)/4.
```

Substitute the Wick map. Because `i^2 = -1`,

```text
Q_E(i a_w omega, k) = (-a_w^2 omega^2 + k^2)/4
                    = omega_coeff(a_w) omega^2 + spatial_coeff k^2,
```

with the exact identities

```text
omega_coeff(a_w) = -a_w^2 / 4,
spatial_coeff    = 1/4,
|omega_coeff(a_w)| / spatial_coeff = a_w^2.
```

The displayed reconstructions used below are

```text
omega_coeff(1/2) = -1/16,
omega_coeff(2)   = -1,
spatial_coeff    = 1/4.
```

The ratio `a_w^2` is a dimensionless rational. The conversion `a_sr` is not.

Kinetic isotropy, from
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
is the Euclidean coefficient equality `c_t = c_s`. In the form `Q_E` that
equality is already the shared prefactor `1/4` on `k4^2` and `k^2`. It is not
a value of `a_w`.

The axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
names Lattice, Qubit, Admissibility, and Record. It does not identify `a_sr`
with a Wick clock parameter and does not install `a_w = 1`.

Identity gates in the companion runner call `omega_coeff(a)` and
`is_dimensionless_ratio`. They do not compare a hardcoded constant to itself.

## Theorem 1 — Unequal Types

`a_sr` is dimensionful: it is the units conversion `a_sr^{-1} = M_Pl`.

`a_w` is a dimensionless ratio of quadratic coefficients: after the Wick
substitution into `Q_E`,

```text
|omega_coeff(a_w)| / spatial_coeff = a_w^2 in Q_{>0}.
```

These are unequal types. Reconstructing the coefficients does not require
choosing a preferred `a_w`:

```text
omega_coeff(1/2) = -1/16,
omega_coeff(2)   = -1,
spatial_coeff    = 1/4.
```

A dimensionful ruler and a dimensionless quadratic ratio cannot be the same
object.

## Theorem 2 — Scale-Reference Cannot Select The Wick Clock

The scale-reference primitive states that it carries no dimensionless
content: no mass ratio, coupling, mixing angle, phase, selector, readout
bridge, or empirical fit is supplied by it.

The legal sample `{1/2, 1, 2}` consists of distinct nonzero rationals. Each
gives a distinct `omega_coeff`:

```text
omega_coeff(1/2) = -1/16,
omega_coeff(1)   = -1/4,
omega_coeff(2)   = -1.
```

A conversion with no dimensionless content cannot select among those values.
In particular it cannot select `a_w = 1`.

## Theorem 3 — Kinetic Isotropy Is Euclidean, Not A Wick Parameter

The kinetic-isotropy primitive states `c_t = c_s`: the Osterwalder-Schrader
OS0 kinetic normalization of the Euclidean regulator. That is equality of
the Euclidean quadratic coefficients of `k4^2` and `k^2`.

`Q_E = (k4^2 + k^2)/4` already encodes that equality and does not contain
`a_w`. The Wick parameter appears only after the substitution
`k4 = i a_w omega`. Therefore `c_t = c_s` is not a selection of `a_w`.

## Theorem 4 — What This Does Not Replace

This type split does not replace speed-preservation among linear Wick maps.
Speed-preservation remains an extra condition, not supplied by `a_sr` and
not supplied by `c_t = c_s`.

This note does not install `a_w = 1`.

This note does not claim Lorentz closure.

This note does not claim that Planck units fix the Wick map.

## Theorem 5 — Shared Letter Is Not Identification

The scale-reference note writes `a^{-1} = M_Pl`. The Wick clock writes
`k4 = i a_w omega`. The shared letter `a` is notation, not a theorem.

Do not treat the shared letter as an identification of `a_sr` with `a_w`.

## Mutation

The predicate "`a_sr` selects `a_w = 1`" must fail. The value `a_w = 1/2`
remains a legal dimensionless Wick parameter, and

```text
omega_coeff(1/2) = -1/16
```

is the exact quadratic coefficient of that legal value.

Any identity gate that reconstructs `omega_coeff` or tests the type of the
quadratic ratio must call `omega_coeff(a)` and `is_dimensionless_ratio`.

## What This Does Not Do

- It does not add or amend an axiom. The axiom memo remains
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
- It does not edit a registered primitive.
- It does not install `a_w = 1` or any other preferred Wick clock value.
- It does not claim that the Planck-mass conversion fixes the Wick map.
- It does not claim Lorentz closure or replace speed-preservation.
- It does not change any audit verdict.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — current
  axiom memo; four named axioms, no Wick-clock identification.
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) —
  dimensionful units conversion `a^{-1} = M_Pl` with no dimensionless content.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) —
  Euclidean OS0 equality `c_t = c_s`, not a Wick parameter.
