# Kinetic-Isotropy Primitive Irreducibility Support

**Date:** 2026-06-09
**Claim type:** bounded_theorem — support / primitive-boundary witness
**Type:** support
**Status authority:** independent audit lane only. This source note does not set,
predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_primitive_irreducibility_support_2026_06_09.py`](../scripts/kinetic_isotropy_primitive_irreducibility_support_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/kinetic_isotropy_primitive_irreducibility_support_2026_06_09.txt`](../logs/runner-cache/kinetic_isotropy_primitive_irreducibility_support_2026_06_09.txt)

---

## What this supports

The approved
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
declares only the structural OS0 kinetic-form isotropy

```text
c_t = c_s.
```

This note records the runner-backed reason that boundary is real: the current
framework baseline and the standard adjacent structures do not determine the
dimensionless kinetic ratio `xi := c_t / c_s`. Positive transfer, reflection
positivity / spectrum positivity, the single-clock product `a_tau * H`, and the
six-nearest-neighbor reachability relation all admit a family of kinetic forms
with different `xi`.

That is support for treating `c_t = c_s` as an explicitly approved primitive,
not as a hidden consequence of Lattice, Quantum, Record, scale, reflection
positivity, or the single-clock theorem. It is not a new axiom, not a Tier-A
admission, and not a bounded-status source. Dependencies on the registered
primitive chain-satisfy through `docs/audit/data/axiom_premise_nodes.json`
without making downstream rows `retained_bounded`.

## Runner scope

The runner uses a free Euclidean lattice scalar as a minimal marginal carrier.
That carrier is a witness family, not a claim that the full framework dynamics
has been derived. Within that witness family it checks:

- **Positive-transfer family:** for `c_t/c_s` in `{0.5, 1, 2, 5}`, the transfer
  eigenvalues are positive contractions and `H >= 0`.
- **Clock-rate distinction:** rescaling `a_tau` changes all mode energies by a
  constant factor, while changing `c_t/c_s` reshapes the dispersion in a
  momentum-dependent way.
- **Reachability limitation:** the `Z^3` six-nearest-neighbor reachability front
  is the L1 diamond, not a round L2 cone with a unique aperture.
- **Two-model witness:** models with `xi = 1` and `xi = 2.5` both satisfy the
  shared checks above and differ on the kinetic isotropy sentence.
- **Spatial comparison:** a spatially anisotropic witness can also satisfy the
  bare positivity checks, but the spatial and temporal cases differ in kind:
  the cubic spatial symmetry group is resident in the Lattice axiom, while the
  time-space exchange generator is not.
- **Cl(3) root check:** `M_2(C) ~= Cl(3,0)` has no fourth anticommuting Pauli
  generator; the pseudoscalar is central. This supports, but does not by itself
  derive, the claim that the time direction is not supplied as a fourth
  Clifford/edge axis.

The safe conclusion is model-family non-fixation: the listed structures do not
fix `xi`. A formal theorem about every possible future dynamics would require a
formalized dynamics class and is not claimed here.

## Boundary

This note supplies no dynamics, Lorentz-closure theorem, absolute scale,
spacing-ratio theorem, mass ratio, coupling, mixing angle, phase, selector,
readout bridge, probability rule, normalization rule, or empirical match. It
also does not promote any conditional Lorentz result or demote any existing row.

The primitive itself remains exactly the narrower registered premise:
space-time kinetic-form isotropy `c_t = c_s`, with the emergent tick grained on
the same footing as the spatial edge. Consequences for marginal Lorentz
violation, radiative stability, or full Lorentz restoration remain separate
theorem/support claims.

## No-Go Discipline Gate

This section applies the no-go discipline to the narrowed negative claim:
"the listed current structures do not fix `xi`."

- **N1 alternative routes:** reflection positivity/OS1, single-clock evolution,
  scale reference, six-nearest-neighbor reachability, Record/readout, and cubic
  spatial symmetry were considered. Each leaves `xi` unfixed under the runner
  witness or the primitive registry boundary.
- **N2 wall independence:** this support note has one residual, kinetic-form
  isotropy. Absolute scale, spacing ratio, dynamics, and empirical matching are
  separate surfaces and are not counted as this residual.
- **N3 hidden-wall scan:** the free scalar is explicitly only a witness carrier;
  reflection positivity and emergent time are hypothesis-side structures for
  the witness, not axioms silently added to the framework baseline.
- **N4 residual matching:** the cited anisotropy gate names the same
  `c_t = c_s` residual; the single-clock and minimum-time-step notes match only
  the clock/product and reachability subclaims and are not used as proof of the
  full primitive.
- **N5 rhetoric audit:** the result is limited to `c_t/c_s` non-fixation. It is
  not a no-go for future dynamics, not a Lorentz-closure claim, and not a
  `delta v = 0` claim.
- **N6 partial-closure scan:** the owner-approved closure path now exists: the
  `kinetic_isotropy_primitive` is registered as an approved primitive, not a
  Tier-A admission and not a bounded import.
- **N7 steelman:** a future retained dynamics could derive the same kinetic
  isotropy and retire the primitive. This would defeat a universal
  non-derivability claim, so the landed claim is narrowed to the current listed
  structures.
- **N8 cross-cycle echo:** the scale-reference primitive shows the same
  governance pattern: when a genuinely primitive premise is owner-approved and
  registered, it chain-satisfies without bounding downstream rows, while its
  consequences remain separately audited.

## Dependency links

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
- [MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)

## No-promotion statement

This note does not set any audit status. It preserves only a support result:
the listed current structures leave the kinetic-form ratio unfixed, which is why
the approved kinetic-isotropy primitive must remain explicit unless a later
retained derivation retires it.
