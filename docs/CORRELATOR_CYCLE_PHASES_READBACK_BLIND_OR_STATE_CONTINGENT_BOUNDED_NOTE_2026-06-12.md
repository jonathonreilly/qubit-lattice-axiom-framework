# Correlator Cycle Phases on the Circulant Surface Are Readback, Blind, or State-Contingent (Bounded)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit any audit-lane-owned
registry, ledger, queue, or publication-status surface.
**Primary runner:** `scripts/frontier_correlator_cycle_phases_dichotomy_2026_06_12.py`
**Status:** source proposal; the audit lane grades. Runner
`PASS=26 FAIL=0`.

## Boundary

This note proves W1-W4 on the supplied three-site Hermitian circulant surface.
It does not close the R-eta derivation question, does not probe
non-circulant surfaces, and does not claim the identification is underivable.
It makes no R-eta claim either way. No fixed value of `r` is used, selected,
or preferred.

State-contingent cycle-phase values are registered state data under the
realized-state interface; they are not universal readout identifications, and
no universality is claimed.

## The supplied surface

Let

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,
```

where `C` is the directed three-cycle shift, `a` is real, and `B > 0`. For a
spectral function `f`, set `G = f(H)`. The directed cycle phase is

```text
phi(delta) = arg(G_01 G_12 G_20).
```

On this circulant surface the three directed edge correlators are equal, so
`phi(delta) = 3 arg g(-1)` modulo the principal branch. The runner checks this
directed-product route and the polar-link route.

## Theorem

**W1 - readback.** For `f(x) = x`, so `G = H`,

```text
G_01 G_12 G_20 = B^3 exp(3 i delta),
```

hence `phi(delta) = 3 delta` exactly on the stated branch. This is a
consistency identity, not an independent derivation of the hopping phase; it
reads the supplied hopping phase back out of the object that already contains
it. Check tags: `W1-symbolic`, `W1-scan`.

**W2 - blind.** For any nonzero band spectral projector on the circulant
family, `phi` is delta-independent. The structural reason is that every
member of the family has the same delta-independent Fourier eigenvectors. The
rank-one projectors are

```text
(P_k)_{xy} = omega^{k(x-y)} / 3,
```

with no `delta` anywhere. All delta-dependence of the family lives in the
eigenvalue multiset, not in the projector entries. Check tags:
`W2-symbolic`, `W2-projector-scan`.

**W3 - state-contingent.** For strictly mixing thermal functions

```text
f_beta(lambda) = 1 / (1 + exp(beta lambda)),  beta in {1, 4},
```

the phase is genuinely `K-ODD`: `phi(-delta) = -phi(delta)` on the wrapped
principal branch. It is also magnitude- and state-class-contingent. At
`delta = 2/9`, the runner prints the `(a,B)` grid spread
`1.3489178109943467` for `beta = 1` and `3.032326580315915` for `beta = 4`;
the cross-`f` spread reaches `1.6551489257862082`. The comparison table at
`delta = 2/9` keeps every tested thermal class farther than `0.1` from the
candidate constants tested by the runner. Per the realized-state interface,
these thermal values are registered state data, not universal readout
identifications. Check tags: `W3-K-odd`, `W3-grid`, `W3-comparison`.

**W4 - no-middleman consequence.** Combine W1-W3 with the
`carrier-class elimination pattern`: the registered symmetric data determine
`|delta|` through the inversion

```text
e_3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta),
cos(3 delta) = (e_3 - a^3 + 3 a B^2) / (2 B^3),
|delta| = arccos(cos(3 delta)) / 3   on (0, pi/3).
```

The coefficient `3` is derived from the three-cycle determinant term and is
reproved here. The dichotomy then removes a state-independent carrier-angle
middleman on this surface: readback phases return the supplied hopping phase;
projector phases are blind; strictly mixing phases are state-contingent
registered data. Any derivation of the R-eta identification must directly
equate the multiset-determined `|delta|` with the fixed-locus arithmetic.
Check tags: `W4-inversion`, `W4-dichotomy`.

## The next paths

WALLS-MOVE: the named wall is the **circulant-carrier phase dichotomy wall**.
The next paths are:

- non-circulant carriers, meaning surfaces where the eigenvectors move with
  the dynamics, including the full staggered lattice realization;
- the direct multiset-to-geometry equation, with no derived-angle middleman.

Both paths remain open and neither is probed here.

## Does NOT

- Does not derive, refute, or grade R-eta.
- Does not set `r`, use a fixed `r`, or move the occupancy-selection question.
- Does not promote state-contingent thermal values to universal readout
  identifications.
- Does not probe non-circulant carriers.
- Does not alter audit status, Tier-A registry text, or publication status.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  - registered-state-data interface used in W3.

## Context

Scope context, not dependency authority:
`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`
is the construction's home;
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
is the determinant-holonomy Hermitian-corner companion;
`UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`
is the carrier-class elimination context whose `cos(3 delta)` inversion is
reproved here;
`KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`
is the R-eta chain context; and
`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
is where the fixed-locus arithmetic lives.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or context note. The independent audit lane is
the sole status authority.
