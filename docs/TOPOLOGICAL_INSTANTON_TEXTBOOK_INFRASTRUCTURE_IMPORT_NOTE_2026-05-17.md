# Topological-Instanton Infrastructure

**Date:** 2026-05-17 (framework-local repair: 2026-05-27)
**Claim type:** bounded_theorem
**Status:** bounded framework-local instanton-infrastructure certificate;
external Yang-Mills topology references are parallel literature citations, not
load-bearing retained imports.
**Runner:** `scripts/topological_instanton_framework_certificate.py`
**Status authority:** independent audit lane only.

## Purpose

This packet replaces the former named-import umbrella with a direct certificate
for the parts of the instanton infrastructure that can be checked inside the
repository without adding axioms:

- 4D Hodge-star algebra on two-forms;
- the Bogomolny square-completion bound and self-dual/anti-self-dual saturation
  in the normalized local action/topological-pairing convention;
- the BPST radial density normalization giving `8 pi^2`;
- twisted `T^4` flux arithmetic giving fractional charge `Q = k/N`.

Full global Atiyah-Singer, Luescher admissibility/gradient-flow, and existence
theorems for all smooth bundles remain parallel mathematical context unless a
separate retained authority packet is built.

## Local Algebraic Certificate

Let `F` be a real 2-form on oriented Euclidean `R^4`, represented in the basis

```text
01, 02, 03, 12, 13, 23.
```

The Hodge star satisfies `*^2 = 1` on two-forms and splits

```text
F = F_+ + F_-,    *F_+ = F_+,    *F_- = -F_-.
```

Therefore

```text
||F||^2 = ||F_+||^2 + ||F_-||^2,
<F,*F> = ||F_+||^2 - ||F_-||^2,
```

so

```text
||F||^2 >= |<F,*F>|
```

with equality exactly on self-dual or anti-self-dual fields. With the standard
instanton normalization `Q = (1/8 pi^2) int tr(F wedge F)`, this is the finite
algebraic core of the Bogomolny action bound

```text
S_E >= (8 pi^2/g^2) |Q|.
```

The runner verifies the Hodge star, the inequality on random two-forms, and
equality on projected self-dual/anti-self-dual components.

## BPST Normalization

For the standard BPST charge-density profile, the radial integral reduces to

```text
int_{R^4} 48 rho^4 / (r^2 + rho^2)^4 d^4x
  = 2 pi^2 int_0^infty 48 rho^4 r^3/(r^2+rho^2)^4 dr
  = 8 pi^2.
```

The runner evaluates this normalization for several `rho` values and confirms
that the charge/action normalization is scale-independent.

## Twisted-Torus Fractional Charge

For an antisymmetric integer flux matrix `n_{mu nu}` on `T^4`, the cup-product
integer

```text
k = n_01 n_23 - n_02 n_13 + n_03 n_12
```

gives the fractional charge sector

```text
Q = k/N  mod Z
```

for the usual `Z_N` twist arithmetic. The runner checks representative
`SU(2)`, `SU(3)`, and `SU(5)` examples, including the `SU(2)` half-charge
case `Q = 1/2`.

## Runner Certificate

[`scripts/topological_instanton_framework_certificate.py`](../scripts/topological_instanton_framework_certificate.py)
reports:

```text
PASS=3 FAIL=0
```

It covers:

- Hodge star and Bogomolny inequality;
- BPST radial `8 pi^2` normalization;
- twisted `T^4` `k/N` charge arithmetic.

## Literature Citations In Parallel

The classical literature remains the source of the global smooth-bundle and
field-existence context:

- Belavin, Polyakov, Schwartz, and Tyupkin (1975) for the BPST instanton;
- Bogomolny (1976) for the square-completion stability bound;
- Atiyah-Singer (1968 series) for the global chiral index theorem;
- Luescher (2001, 2010) for lattice admissibility and Wilson flow;
- 't Hooft (1979) and van Baal (1984) for twisted-torus flux sectors.

Those references are cited in parallel. The retained-target content here is
only the finite algebra and arithmetic checked by the runner.

## Boundary

This packet does not claim:

- a framework-native proof of the full Atiyah-Singer theorem;
- a proof that every lattice admissibility/gradient-flow hypothesis holds in
  the framework;
- existence and uniqueness of all smooth BPST/twisted solutions;
- closure of any downstream external narrow theorem.

It does provide a bounded, auditable replacement for the previously hidden
mathematical imports that were actually used numerically: the action bound
normalization and the fractional charge arithmetic.
