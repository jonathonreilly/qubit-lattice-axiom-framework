# Flavor Gauge-Representation Generation-Uniform Core

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py`](../scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/flavor_gauge_representation_generation_uniform_core_2026_06_18.txt`](../logs/runner-cache/flavor_gauge_representation_generation_uniform_core_2026_06_18.txt)

## Claim

On the retained three-generation observable surface, any gauge action that
acts through a shared generation-carrier scalar is degree-zero inert on the
Koide ratio

```text
r = |b|^2/a^2.
```

If the singlet coefficient `a` and doublet coefficient `b` are both multiplied
by the same gauge-sector scalar `s`, then

```text
r' = |s b|^2 / |s a|^2 = |b|^2/a^2 = r.
```

Equivalently, `r = |b|^2/a^2 is invariant` under any such
generation-uniform scalar action.

Thus a generation-uniform carrier action cannot select or change the sector
ratio. Moving `r` would require a non-uniform action that distinguishes the
singlet and doublet coefficients, which is not supplied by the shared retained
generation-carrier surface.

## Retained Inputs

The core uses:

- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  and
  [`THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the retained `M_3(C)` generation surface;
- [`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md)
  for the no-proper-generation-quotient boundary;
- [`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md)
  and
  [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
  for the finite circulant form and `r = |b|^2/a^2` readout.

## What This Splits From The Parent

The parent no-go
`FLAVOR_GAUGE_REPRESENTATION_CHANNEL_CANNOT_SOURCE_THE_SECTOR_R_SPREAD_NARROW_NO_GO_NOTE_2026-06-15.md`
has two layers:

1. the framework-native generation-uniform core above; and
2. a physical sector-representation premise: the standard assignment of
   charged leptons, neutrinos, up quarks, and down quarks to SM colour/weak
   representations.

This note isolates only layer 1. It does not derive the SM sector
representation assignment, the electroweak doublet structure, hypercharge,
right-handed representation data, or the physical readout that ties sector
labels to the framework carrier.

## Conditional Counting Context For The Parent

Under the parent note's standard sector-representation premise, functions of
the non-abelian colour representation distinguish only the colourless class
from the coloured class. They do not split `u` from `d` inside a weak doublet,
or `nu` from `e` inside a lepton doublet.

That conditional counting statement is useful as a no-go test for the proposed
colour-representation escape route. It is not a derivation of the SM sector
representation assignment from the framework.

## What This Does Not Close

- Does not derive the allowed SM sector representation assignment.
- Does not derive hypercharge, `T3`, electroweak partner structure, or
  right-handed representation data.
- Does not derive a physical sector-to-carrier/readout bridge.
- Does not derive or force any value of `r`.
- Does not close the abelian/electroweak or within-sector measure channel.
- Does not change the audit status of the parent row.

## Runner Certificate

The runner checks:

- retained-grade status for the generation and Koide-ratio dependencies;
- exact invariance of `r` under uniform scalar multiplication of `a` and `b`;
- a discriminating non-uniform control that would move `r`;
- the conditional two-class colour-representation count under the parent
  premise;
- parent citations and firewalls preserving the open SM representation
  assignment and parent audit status.

Expected result: `SCORECARD PASS=9 FAIL=0`.
