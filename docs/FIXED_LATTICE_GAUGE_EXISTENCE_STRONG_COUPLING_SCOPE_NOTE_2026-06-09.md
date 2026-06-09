# Fixed-Lattice Gauge Existence and Strong-Coupling Gap Scope

**Date:** 2026-06-09
**Claim type:** bounded_theorem (fixed-lattice/literature-scope support)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_fixed_lattice_gauge_gap_scope_2026_06_09.py`](../scripts/frontier_fixed_lattice_gauge_gap_scope_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_fixed_lattice_gauge_gap_scope_2026_06_09.txt`](../logs/runner-cache/frontier_fixed_lattice_gauge_gap_scope_2026_06_09.txt)

## Claim Under Review

This note is a scope repair for the Yang-Mills mass-gap question in a framework
with a fixed lattice spacing. It does **not** solve the Clay Yang-Mills problem,
does **not** prove a physical `SU(3)` gap at `beta=6`, and does **not** treat the
scale-reference primitive as a Planck-scale physical import.

The durable content is narrower:

1. On any finite fixed lattice, a compact-gauge Wilson pure-gauge partition
   function is a finite positive integral. The runner verifies this directly for
   representative `SU(2)` and compact `U(1)` one-plaquette factors at `beta=6`.
2. Standard lattice-gauge literature proves area-law/gap behavior in controlled
   strong-coupling regimes. The runner checks the corresponding leading
   one-plaquette area-law diagnostics for representative `SU(2)` and compact
   `U(1)` strong-coupling values.
3. These facts reframe the continuum-construction wall: a fixed-lattice theory
   has a different constructive burden than a continuum `a -> 0` Clay problem.
   This is a scope distinction, not a proof of the physical color mass gap.

## Scope

The scale-reference primitive supplies only a dimensionful unit reference for
the lattice spacing. It does not assert `a = l_P`, provide a Yang-Mills action,
prove a mass gap, set `beta`, supply `Lambda_QCD`, or import observed spectrum
data. The fixed-lattice premise used here is the repo's discrete lattice
setting plus a non-continuum-limit scope choice.

The kinetic-isotropy primitive supplies only the structural `c_t = c_s` kinetic
form. It does not provide Osterwalder-Seiler reflection positivity, transfer
matrix positivity, confinement, or a gauge action.

## What The Runner Verifies

- the representative compact one-plaquette `SU(2)` and compact `U(1)` Wilson
  integrals are finite and positive at `beta=6`;
- the strong-coupling leading factors satisfy `0 < factor < 1`, hence
  `sigma = -log(factor) > 0`, in the tested strong-coupling range;
- the leading Wilson-loop diagnostic is area-law algebra,
  `log W(R,T) = -sigma R T`, not a perimeter-law diagnostic;
- the leading factors move monotonically toward one as `beta` increases, which
  is a diagnostic of weakening strong-coupling confinement, not a proof of
  all-coupling `SU(3)` confinement.

## What This Does Not Establish

- No Clay Yang-Mills existence-and-mass-gap solution.
- No continuum `a -> 0` construction or uniform continuum bound.
- No rigorous `SU(3)` mass gap at the framework's `beta=6` surface.
- No proof that the strong-coupling `SU(N)` area law reaches the scaling region.
- No derivation of `Lambda_QCD << a^{-1}` or dimensional transmutation from the
  axioms/primitives.
- No physical `SU(3)_c` identification, observed glueball spectrum, massless
  photon theorem, or "matches reality" claim.
- No fermion determinant positivity theorem or staggered-matter realization.
- No new axiom, primitive, action-form premise, gauge-weight premise, coupling,
  normalization, probability rule, or Record readout claim.

## Dependencies

- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
  supplies the unit reference for a fixed lattice spacing only.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies the structural kinetic-form isotropy premise only.
- Standard lattice-gauge literature supplies the strong-coupling area-law
  context: Osterwalder-Seiler, Guth, Frohlich-Spencer, and Münster are cited as
  external/literature support, not framework-native derivations.

## Honest Status

This is useful as a bounded scope note: it separates finite fixed-lattice
well-definedness and strong-coupling literature support from the still-open
physical `SU(3)`/`beta=6` mass-gap target. It does not promote, demote, or set
the audit status of any dependency. The independent audit lane is the only
status authority.
