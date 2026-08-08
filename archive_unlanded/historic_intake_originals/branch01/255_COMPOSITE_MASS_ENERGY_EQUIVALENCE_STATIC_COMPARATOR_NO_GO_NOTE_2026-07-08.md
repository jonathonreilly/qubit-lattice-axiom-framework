# Composite Mass-Energy Equivalence Fails for Every Static Comparator -- Sum Rule, No-Go, and the Mediator Requirement

**Date:** 2026-07-08
**Type:** bounded_theorem (with one class-level no-go on the declared
comparator class)
**Claim type:** bounded_theorem
**Claim scope:** On the 1D reduction of the two-step surface with two
distinguishable species and ANY momentum-independent (static/instant-form)
relative interaction, this note proves an exact sum rule: the composite
inertial mass is a kinetic-band functional of the bound state, into which
the binding energy never enters additively. Consequences, runner-verified:
a Kohn-type exactness statement on truly quadratic bands, its failure on
any band with varying curvature, and the class-level no-go that
mass-energy equivalence `M_comp = E_2(0)` fails by at least the
binding-energy scale for every static comparator, persisting into the
scaling window. The mediator requirement this leaves is stated as the
next derivation target; nothing here derives an interaction, closes an EP
row, or sets an audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/composite_mass_energy_equivalence_static_comparator_2026_07_08.py`](../scripts/composite_mass_energy_equivalence_static_comparator_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/composite_mass_energy_equivalence_static_comparator_2026_07_08.txt`](../logs/runner-cache/composite_mass_energy_equivalence_static_comparator_2026_07_08.txt)

## Why This Note Exists

Under the owner-selected scaling-window reading of weak equivalence, the
source-reduction companion note leaves one leading window residual: the
composite's inertial mass must track its total energy (mass-energy
equivalence), because in nature it is mass-energy equivalence that absorbs
the binding energy into both sides of the equivalence principle. This note
decides where that equivalence can and cannot come from on the declared
surface: it cannot come from any static interaction, however tuned; it
requires the binding to be carried by a dynamical mediator.

## Imports And Premises

Inherited by citation: the composite-additivity companion note's I-1D /
I-DIST surface and P-block construction. The comparator class here
generalizes I-INT to **I-INT-CLASS**: any momentum-independent relative
interaction `V(r)` (the runner sweeps the contact well and an
exponential-range well). All results are stated for this class; V remains
a comparator import, never a derived interaction.

## Statement

Let the two species have band `E(p)` with the composite P-block
`H_P = K_P + V`, `K_P(q) = E(alpha P + q) + E((1-alpha) P - q)` for any
center-of-mass split `alpha`.

**T1 - kinetic-functional sum rule (exact).** For any P-independent `V`,
Feynman-Hellmann plus second-order perturbation theory at `P = 0` give,
for the even bound state `phi`,

```text
    1/M_comp = <phi| A_alpha |phi>
               - 2 sum_{n != 0} |<n| B_alpha |phi>|^2 / (E_n - E_2),

    A_alpha = alpha^2 E''(q) + (1-alpha)^2 E''(-q),
    B_alpha = alpha E'(q) + (1-alpha) E'(-q),
```

with the total split-invariant. At the symmetric split `alpha = 1/2` the
second-order term vanishes identically (`B_{1/2} = 0` by oddness of `E'`),
leaving

```text
    1/M_comp = (1/2) <phi| E''(q) |phi>.
```

Composite inertia is the bound-state average of the constituents' band
curvature. The interaction and the binding energy enter only through the
wavefunction; they never enter as an additive energy term. Runner: sum
rule vs direct band fit agree to `9.3e-10` across three splits, two
masses, two couplings, with split-invariance to `2.3e-14`; the symmetric
split's second-order term is exactly `0`.

**T2 - Kohn exactness and its boundary (control).** On an exactly
quadratic band (`E'' = 1/m` constant) the sum rule is bound-state
independent: `M_comp = 2m` exactly, for every static `V`, every strength,
every range -- the Galilean/Kohn statement made manifest (runner:
first-order term exact to `< 1e-12`; the zone-edge artifact of embedding a
non-periodic band is bounded at `2.8e-5` and printed). On the
lattice-cosine band the curvature varies and Kohn exactness fails in the
sum-rule-predicted way (`M_comp = 2m / <cos q>_phi`; runner validates the
sum rule against the band fit on this second family to `1.3e-11`).
Observed context, not gated: for the pure contact well on the cosine band
the deviation obeys `M_comp - 2m = E_B` to all printed digits.

**T3 - class-level mass-energy-equivalence no-go (measured, size-valid).**
For the framework band, with the binding fraction matched at
`E_B / E_2(0) = 5%` across both interaction shapes: the mass-energy
mismatch is

```text
    M_comp - E_2(0) = 9.1 E_B   (contact),
    M_comp - E_2(0) = 7.5 E_B   (exponential well),
```

shape-consistent within a factor `1.2`, and it persists into the scaling
window (`m = 0.05`, `E_B/E_2(0) = 2%`, `kappa_L = 10.1`, `L = 1024`:
`M_comp - E_2(0) = 3.2 E_B`). Equivalence would require
`M_comp = E_2(0)`; the static class misses by the binding scale plus the
bandwidth-domination excess, and by T1 this is structural: a static `V`
has no channel through which `-E_B` could enter the inertia.

## Corollary - The Mediator Requirement

Window composite weak equivalence at order `E_B / E` requires the binding
energy to appear in the composite's inertial response. By T1 that is
impossible for any momentum-independent interaction: the inertia is a
kinetic-band functional. The binding must therefore be carried by a
degree of freedom that contributes to the center-of-mass kinematics -- a
momentum-dependent, retarded, field-mediated interaction.

On this framework's surface, the record-preservation dynamics-form
theorem already forces the lawful interaction class to be exactly that:
gauge-covariant hopping through link variables. The structure the Record
axiom forces for dynamics is the structure weak equivalence requires for
binding. The derivation target this defines -- composite mass-energy
equivalence on the gauged/interacting transfer surface -- is named for a
future campaign; it is not attempted here.

## No-Go Discipline (class-level negative)

- Routes enumerated: contact and finite-range static wells swept (shapes,
  strengths, masses, window point); the escape route is named in the
  corollary (momentum-dependent mediator), not closed.
- Steelman: "some static V could be tuned so that M_comp = E_2(0) at one
  point." True pointwise -- T1 permits accidental crossings -- but the
  tuning is configuration-dependent (the source-reduction companion's
  witness shows equal rest energies with 47% different inertias), so no
  static class satisfies equivalence as an identity. The claim is scoped
  to the identity, not to isolated points.
- The negative is bounded to the declared 1D comparator class; it says
  nothing about the gauged surface, which is exactly the named escape.

## Boundaries

- 1D reduction; distinguishable species; equal masses in the gated legs.
- I-INT-CLASS is a comparator class import; no interaction is derived.
- T3's constants are measurements with the printed size-validity
  discipline (`kappa_L >= 8`); T1/T2 are exact up to the printed
  zone-edge artifact of the quadratic control.
- No WEP row is closed; no gravitational dynamics is derived; the
  mediator requirement is a named derivation target, not a claim of
  closure.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md`](COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md)
  -- P-block construction, bandwidth domination, composite comparator.
- [`WEP_SOURCE_REDUCTION_FINITE_SPACING_BOUNDARY_SCALING_WINDOW_BOUNDED_NOTE_2026-07-08.md`](WEP_SOURCE_REDUCTION_FINITE_SPACING_BOUNDARY_SCALING_WINDOW_BOUNDED_NOTE_2026-07-08.md)
  -- window residual this note addresses; the same-rest-energy witness
  used by the steelman response.
- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  -- the forced covariant-hopping interaction class cited by the
  corollary's convergence statement.

## Runner And Cache

Primary runner:
[`scripts/composite_mass_energy_equivalence_static_comparator_2026_07_08.py`](../scripts/composite_mass_energy_equivalence_static_comparator_2026_07_08.py)

Runner cache:
[`logs/runner-cache/composite_mass_energy_equivalence_static_comparator_2026_07_08.txt`](../logs/runner-cache/composite_mass_energy_equivalence_static_comparator_2026_07_08.txt)

Current local runner result:

```text
TOTAL: PASS=5 FAIL=0
```

Load-bearing residuals from the cached run: sum rule vs band fit `9.3e-10`
with split-invariance `2.3e-14` and exactly vanishing symmetric-split
second-order term; quadratic-control first-order Kohn term exact to
`< 1e-12` with the zone-edge artifact bounded at `2.8e-5`; cosine-family
sum-rule validation `1.3e-11`; mass-energy mismatches `9.1 / 7.5 / 3.2`
binding energies at the matched-binding and window points, all extractions
size-valid.

## Changelog

- **2026-07-08.** Initial note. The first runner draft's Galilean control
  wrongly used the lattice-cosine band as if Kohn-exact; the worker
  correctly refused to pass it, and the control was replaced by the
  manifest quadratic-band statement with the cosine family kept as a
  second sum-rule validation and a bandwidth-domination exhibit. Local
  runner result `TOTAL: PASS=5 FAIL=0`.
