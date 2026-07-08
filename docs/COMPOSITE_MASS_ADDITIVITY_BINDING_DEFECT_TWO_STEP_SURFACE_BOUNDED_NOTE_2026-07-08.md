# Composite Mass Additivity and Binding Defect on the Two-Step Surface -- Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem (with declared measured-comparator legs)
**Claim type:** bounded_theorem (with declared measured-comparator legs)
**Claim scope:** On the `1D` reduction of the two-step surface, with
`E(p) = arcsinh(sqrt(m^2 + sin^2 p))`,
`M_I = m sqrt(1 + m^2)`, and `F(x) = (1/2) sinh(2x)`, this note studies two
distinguishable species on a ring. It proves exact free additivity and exact
fixed-total-momentum reduction statements, then records measured comparator
legs for a supplied short-range contact interaction
`-U delta(x_1, x_2)`. The interaction is an imported comparator only; it is
not derived from the framework and is not used as a general interacting
two-particle transfer theorem.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/composite_mass_additivity_binding_defect_2026_07_08.py`](../scripts/composite_mass_additivity_binding_defect_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/composite_mass_additivity_binding_defect_2026_07_08.txt`](../logs/runner-cache/composite_mass_additivity_binding_defect_2026_07_08.txt)

## Why This Note Exists

The mass-observable companion note computes the single-particle rest gap
`m_gap = arcsinh(m)`, the inertial-response coefficient
`M_I = m sqrt(1 + m^2)`, and the universal single-particle source function
`F(m_gap) = M_I` on the two-step surface. The inertial-closure companion note
then shows that `M_I` governs the leading acceleration under the declared
species-blind probe.

Neither note decides how composite matter behaves. A finite-spacing lattice
composite has two distinct questions: whether free constituents add their
energies and inertial-response coefficients, and whether a bound composite
can still be sourced by a rest-energy-only functional. This note supplies the
bounded comparator input for those questions on the `1D` reduction.

## Imports And Premises

- **Inherited companion surface.** The free two-step band, positive
  mass sector, blocked-time normalization, rest-gap/inertial readouts, and
  probe-side inertial closure are inherited by citation from
  [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md)
  and
  [`INERTIAL_CLOSURE_WIDTH_INDEPENDENT_ACCELERATION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](INERTIAL_CLOSURE_WIDTH_INDEPENDENT_ACCELERATION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md).
- **I-1D.** The surface is the `1D` reduction

```text
    E_s(p) = arcsinh(sqrt(m_s^2 + sin^2 p)),
    M_{I,s} = m_s sqrt(1 + m_s^2),
```

  for each species `s`.
- **I-DIST.** The two particles are distinguishable species on a ring. No
  exchange-statistics statement is made.
- **I-INT.** A short-range contact comparator

```text
    V(x_1, x_2) = -U delta(x_1, x_2)
```

  is supplied. It is a comparator import, not a derived interaction and not a
  general interacting transfer construction.
- **Framework separation authorities.** The free localized-packet additivity
  statement cites the framework separation and finite-speed independence
  authorities in
  [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
  and
  [`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md).

## Statement

On the declared `1D` two-step surface, let two distinguishable species have
bands

```text
    E_a(p) = arcsinh(sqrt(m_a^2 + sin^2 p)),
    E_b(p) = arcsinh(sqrt(m_b^2 + sin^2 p)).
```

For fixed total momentum `P`, define the relative-coordinate block

```text
    H_P[r,r']
      = (1/L) sum_q exp(i q (r-r')) (E_a(q) + E_b(P-q))
        - U delta_{r,0}.
```

**T1 - P-block reduction, exact.** The fixed-total-momentum reduction
reproduces the full two-particle sector spectra. The runner verifies the
`L = 12` witness with spectral discrepancy `2.7e-15`.

**T2 - free additivity, exact.** At `U = 0`, the composite rest energy is
exactly additive, with residual `6.7e-16`. For equal masses, the free band
bottom at even total momentum equals

```text
    E_2(P) = 2 E(P/2)
```

to `1e-15`, and the center-of-mass curvature at `P = 0` is exactly

```text
    d^2 E_2 / dP^2 |_{P=0} = 1 / (M_I + M_I),
```

with Richardson residual `4.1e-11`. Thus the free composite inertial mass is
the sum of the constituents' inertial-response coefficients. Localized
packets of distinguishable species are exactly energy-additive regardless of
overlap, with residual `6.7e-16`, and the Gaussian overlap matches

```text
    exp(-d^2 / (8 sigma^2))
```

exactly.

**T3 - bound pair exists for the supplied comparator.** The contact
comparator binds at every tested `(m, U)`. The runner reports binding
energies `E_B` from `2.6e-2` at `(m, U) = (0.5, 0.2)` to `5.6e-1` at
`(m, U) = (1.0, 0.8)`, and each tested bound level is separated from the
continuum edge.

**M1 - bandwidth domination, measured comparator leg.** Binding raises the
composite inertial mass while lowering the rest energy. At `m = 1.0`, the
measured composite inertial mass moves from the free sum `2.83` to `10.8` at
`U = 0.8`, while `E_2(0)` falls from `1.76` to `1.20`. The lattice composite
is not Galilean:

```text
    M_comp != m_1 + m_2 - E_B.
```

The mechanism is band flattening: a tightly bound pair translates by
second-order hopping, so its center-of-mass band narrows even as its rest
energy drops. This is a load-bearing measurement, not an identity.

**M2 - source-functional dichotomy, measured comparator leg.** At the gated
value `U = 0.8`, the singles-exact source `F(rest gap)` from the mass-observable note's T5 is
verified exact for single particles with violation `0.0`, but it fails
composite universality by `0.755` at `m = 0.5` and `0.747` at `m = 1.0`.
The charge-counting `Q`-density source fails by `0.604` and `0.739` on the
same two masses. Even the free composite breaks `F`-universality:

```text
    F(2 m_gap) / (2 M_I) - 1 = 0.50    at m = 0.5,
    F(2 m_gap) / (2 M_I) - 1 = 2.00    at m = 1.0,
```

because `F` is convex while free inertial mass is additive. This is a
load-bearing measurement, not a theorem identity; the weakest-binding
curvature extraction carries the runner-printed `2.8e-2` curvature shift
between quartic and sextic fits, while the `U = 0.8` extractions are
`4e-4` or better.

## Proof Sketch

For T1, translation invariance in the center-of-mass coordinate decomposes
the two-particle Hilbert space into fixed-total-momentum blocks. In a `P`
block, the free two-particle symbol is the sum
`E_a(q) + E_b(P-q)`. The supplied contact comparator is diagonal in the
relative coordinate and contributes only `-U delta_{r,0}`. This gives the
displayed `H_P[r,r']`. The paired runner compares the resulting block spectra
against the unreduced two-particle sector and prints the `L = 12` agreement
to `2.7e-15`.

For T2, setting `U = 0` removes the relative-coordinate contact term, so the
two-particle energy is the sum of the two one-particle band energies. At rest,
this gives exact rest-energy additivity. For equal masses and even total
momentum, symmetry puts the free band bottom at the equal split `q = P/2`,
so the band bottom is `2 E(P/2)`. Differentiating twice in `P` at rest gives
`1/(2 M_I)`, i.e. reciprocal curvature `M_I + M_I`, matching the
companion notes' inertial-response coefficient. The localized-packet leg is
the same free tensor-product additivity stated in position space: overlap
changes the packet inner product, not the additive free Hamiltonian
expectation for distinguishable species.

For T3, the supplied attractive contact comparator lowers one level below the
free two-particle continuum in every tested case. The statement is bounded to
the printed tested grid and to the imported comparator. It is not a derivation
of an interaction from the axioms.

For M1, the measured bound-pair band is flatter than the free center-of-mass
band. Since inertial mass is the reciprocal of the center-of-mass curvature,
band flattening raises `M_comp`. The rest energy simultaneously drops because
the attractive contact lowers the bound level. These two effects have opposite
signs relative to the Galilean formula, so the finite-spacing lattice
composite does not satisfy `M_comp = m_1 + m_2 - E_B`.

For M2, the mass-observable note's T5 fixes the only single-particle exact rest-gap source on
this surface:

```text
    F(x) = (1/2) sinh(2x).
```

For a free equal-mass composite, rest energy adds as `2 m_gap` while inertial
mass adds as `2 M_I`. Convexity of `F` therefore breaks exact composite
universality already at `U = 0`. In the bound case, M1 pushes in the same
direction: binding lowers rest energy while flattening the center-of-mass
band, so a rest-energy-only source moves away from the measured composite
inertial response rather than tracking it.

## Corollary C1 - Source-Side Comparator Input

On this surface, no species-blind source functional of rest energy alone can
give exact finite-lattice-spacing composite universality. Single-particle
exactness forces the source to be `F` by the mass-observable note's T5. Free additivity of
inertial mass plus convexity of `F` already breaks the free composite case.
The bound comparator then breaks the bound case in the same direction because
binding lowers rest energy while bandwidth domination raises the measured
composite inertial mass.

Exact finite-spacing WEP for bound matter therefore requires the source to
couple to the composite's own inertial-response coefficient, a dynamical band
property, not to a rest-energy readout. The printed trend shows that the
violations shrink with weaker binding at fixed `m`; this is the scaling-window
statement. Universality is recovered as a continuum-window statement, not as
an exact finite-lattice-spacing identity. This corollary is only the
comparator input consumed by the source-side companion block (separate science block); it closes no EP row and
sets no audit status.

## Persistence Scope

This lane defines matter persistence as conservation of the mass observable
and one-particle band identity under the realized dynamics, not as
non-spreading of free wave packets; free-packet spreading remains a lattice
fact, and localization-grade persistence is Record content (axiomatic) or
requires an interacting surface not licensed here beyond the declared I-INT
comparator.

## Consequence

The exact part of this note says that free composite rest energy and free
composite inertial response are additive on the declared two-step surface.
The measured comparator part says that a bound lattice composite is governed
by its own center-of-mass band: binding can lower rest energy while raising
the inertial-response coefficient through bandwidth domination.

This is the finite-spacing obstruction the source-side companion block must consume.
Rest-energy-only sourcing is too little data for exact composite universality
on this lattice surface.

## Boundaries

- `1D` reduction only; this is not the full `d = 3` two-particle transfer.
- Distinguishable species only; no exchange-statistics statement is made.
- The contact `I-INT` interaction is a comparator import, never a derived
  interaction.
- The exact theorem legs are T1-T3 only.
- M1 and M2 are measured comparator legs, not identities.
- The weakest-binding extraction carries the printed `3%` curvature
  uncertainty; the `U = 0.8` extractions are `4e-4` or better.
- No WEP claim is supplied.
- No source-side gamma identity is supplied.
- No general source law is supplied.
- No interacting `d = 3` transfer theorem is supplied.
- This note sets no audit status.
- Independent audit is required.

## Dependencies

- [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md)
  supplies the single-particle two-step band, rest gap, inertial-response
  coefficient, and `F(rest gap)` identity used here.
- [`INERTIAL_CLOSURE_WIDTH_INDEPENDENT_ACCELERATION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](INERTIAL_CLOSURE_WIDTH_INDEPENDENT_ACCELERATION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md)
  supplies the probe-side inertial closure inherited by this composite note.
- [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
  supplies the cited framework separation context for treating independent
  localized free packets as separate tensor-product factors in the bounded
  free-packet leg.
- [`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md)
  supplies the finite-speed locality context used as a framework independence
  authority for the same bounded free-packet leg.

## Runner And Cache

Primary runner:
[`scripts/composite_mass_additivity_binding_defect_2026_07_08.py`](../scripts/composite_mass_additivity_binding_defect_2026_07_08.py)

Runner cache:
[`logs/runner-cache/composite_mass_additivity_binding_defect_2026_07_08.txt`](../logs/runner-cache/composite_mass_additivity_binding_defect_2026_07_08.txt)

Current local runner result, supervisor-provided:

```text
TOTAL: PASS=6 FAIL=0
```

Load-bearing residuals from the supervisor-provided run: the `L = 12`
fixed-`P` block spectrum matches the full two-particle sector to `2.7e-15`;
free rest-energy additivity and localized-packet energy additivity both have
residual `6.7e-16`; the equal-mass even-momentum free band bottom matches
`2 E(P/2)` to `1e-15`; the free center-of-mass curvature matches
`1/(M_I + M_I)` with Richardson residual `4.1e-11`; and every tested
contact-comparator pair binds with the printed continuum separation and
measured source-functional violations.

## Changelog

- **2026-07-08.** Initial bounded-theorem note with exact theorem legs T1-T3,
  declared measured-comparator legs M1-M2, and supervisor-provided runner
  result `TOTAL: PASS=6 FAIL=0`.
