# Kinetic-Isotropy Primitive

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-09
**Type:** meta
**Status:** framework primitive declaration. Registered in
`docs/audit/data/axiom_premise_nodes.json` as
`kinetic_isotropy_primitive`. Explicit owner approval is recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.

## What This Declares

The framework takes one structural graining fact: the emergent evolution tick is
grained on the same footing as the spatial lattice edge. Concretely, the matter
kinetic normalization is space-time isotropic,

```text
    c_t = c_s,
```

equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are
computed is hypercubic-symmetric (the Osterwalder-Schrader OS0 kinetic
normalization). One tick is one edge in **form**, not only in spacing.

This is a structural statement about the regulator geometry, the time-direction
analogue of the `LATTICE` axiom's spatial **cubic adjacency** `a_x = a_y = a_z`.
It carries no dimensionless dynamical content: no mass ratio, coupling, mixing
angle, phase, selector, readout bridge, or empirical fit is supplied by it. It
is not a fourth spatial dimension, not a new dynamics, and not a re-axiomatization
of time: the framework's time remains emergent and derived (the single-clock
codimension-1 evolution theorem); this primitive fixes only the one dimensionless
graining ratio relating that emergent time to space.

## Why It Is A Primitive

The framework baseline `Lattice + Quantum + Record`, together with the emergent
single-clock evolution and reflection positivity, does **not** fix the kinetic
isotropy `c_t = c_s`. This is not merely unestablished but **independent**: a
positive-transfer reflection-positive evolution with `H >= 0` exists for every
value of `c_t/c_s`, so reflection positivity, the single-clock theorem, the scale
reference, and the records' causal order are all blind to it (a Robinson/Vaught
independence result; see the dependencies). Because `c_t = c_s` is itself the
emergent-Lorentz output, no derivation of it from those structures is possible
without circularity.

The two adjacent quantities are *not* the open one and are recorded for contrast:

- the **absolute** time scale `a_tau` is set by the single approved
  scale-reference primitive (`a^{-1} = M_Pl`);
- the **spacing** ratio `a_tau / a_s` is already derived from the `LATTICE`
  axiom's no-diagonal clause plus the retained reachability theorem (one record
  tick reaches exactly one nearest-neighbor edge).

What remains genuinely free is the kinetic **form** ratio `c_t / c_s`. A theory
that grains space but leaves the kinetic form temporally anisotropic is the
lopsided surface on which radiative corrections regenerate a species-dependent
marginal Lorentz violation (the Collins naturalness problem); the isotropic
choice `c_t = c_s` is the symmetric completion under which that violation is
forbidden to all orders, representation-blind. This is the same category of
dimensionless **structural** premise the framework already accepts at axiom grade
for space (cubic adjacency), supplied here for the emergent time direction. It is
irreducible by the independence result above, exactly as the dimensionful scale
reference is irreducible by dimensional analysis.

## What This Does Not Do

- It does not add or amend an axiom. The minimal framework baseline is the three
  named axioms in `MINIMAL_AXIOMS_2026-06-05.md`: Lattice, Quantum, and Record.
- It does not re-axiomatize time. The emergent single-clock evolution remains
  derived; this primitive normalizes only the one graining ratio `c_t / c_s`.
- It does not supply any dimensionless dynamical quantity. No mass ratio,
  coupling, mixing angle, phase, or selector is supplied; dimensionless physics
  must still derive from the framework baseline or be recorded as a bounded
  Tier-A admission.
- It does not supply the absolute scale (`scale_reference_primitive`) or the
  spacing ratio (derived from the no-diagonal clause); it supplies only the
  kinetic-form isotropy.
- It does not change any audit verdict. Audit status remains set only by the
  independent audit lane.

## Audit-Pipeline Treatment

The machine-readable distinction is:

- `docs/audit/data/axiom_premise_nodes.json` lists framework axioms and
  explicitly approved framework primitives. These dependencies chain-satisfy
  without bounding downstream rows.
- `docs/audit/data/tier_a_admissions.json` lists non-axiom derivation-target
  admissions. These dependencies chain-satisfy only at `retained_bounded`
  until the relevant admission is retired by a retained derivation.

The structural purity guard `docs/audit/scripts/check_axiom_premise_clean.py`
keeps this source note inside the approved-premise boundary (no framework-rule or
ratification clauses).

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the three-axiom
  baseline whose spatial cubic adjacency this primitive parallels in the time
  direction.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the
  sibling primitive supplying the single dimensionful anchor; together they state
  "spacetime is grained at one scale, isotropically."
- [MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)
  — derives the spacing ratio `a_tau/a_s` (the adjacent, already-derived freedom).
- [AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
  — the emergent derived time this primitive normalizes (it does not replace it).
- [COLLINS_MATTER_GEOMETRIC_CONE_SURFACE_RESOLUTION_NOTE_2026-06-09.md](COLLINS_MATTER_GEOMETRIC_CONE_SURFACE_RESOLUTION_NOTE_2026-06-09.md)
  — the surface-resolution and structural no-go showing `c_t = c_s` forbids the
  marginal Lorentz violation to all orders and that no other route can.
