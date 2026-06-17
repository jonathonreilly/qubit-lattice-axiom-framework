# Plaquette Beta=6 Wilson Normalization Native Import Repair

**Date:** 2026-06-17
**Claim type:** exact support theorem
**Type:** exact support theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:**
[`scripts/frontier_plaquette_beta6_wilson_normalization_native_import_repair_2026_06_17.py`](../scripts/frontier_plaquette_beta6_wilson_normalization_native_import_repair_2026_06_17.py)

**Cached runner output:**
[`logs/runner-cache/frontier_plaquette_beta6_wilson_normalization_native_import_repair_2026_06_17.txt`](../logs/runner-cache/frontier_plaquette_beta6_wilson_normalization_native_import_repair_2026_06_17.txt)

## Targeted Audit Unlock

The audited conditional row
[`PLAQUETTE_BETA6_PERTURBATIVE_DERIVATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-27.md`](PLAQUETTE_BETA6_PERTURBATIVE_DERIVATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-27.md)
listed four runner-local admitted inputs:

```text
W1: NSPT coefficient packet
W2: beta=6 Wilson normalization
W3: MC comparator 0.5934
W4: F2 comparator
```

This note retires only W2 as a hidden runner-local import. On current main,
[`NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP_BOUNDED_NOTE_2026-06-12.md`](NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP_BOUNDED_NOTE_2026-06-12.md)
proves the exact Wilson-beta relationship used by the native transfer lane
and the physical plaquette lane. Therefore the diagnostic's normalization

```text
N_c = 3, beta = 6, g_bare^2 = 2 N_c / beta = 1,
alpha_bare = g_bare^2 / (4 pi) = 1 / (4 pi)
```

can be cited through that native relationship note instead of being treated as
a hidden runner-local import.

## Statement

Assume the Wilson-beta relationship and object-separation fences of
`NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP_BOUNDED_NOTE_2026-06-12.md`.
For `N_c = 3` and the beta=6 Wilson row:

```text
beta = 2 N_c / g_bare^2
g_bare^2 = 2 N_c / beta = 6 / 6 = 1
alpha_bare = g_bare^2 / (4 pi) = 1 / (4 pi).
```

This is exact rational algebra plus the native Wilson-beta relationship. It
does not derive `<P>(beta=6)`, the NSPT coefficients, the MC comparator, the
F2 comparator, a physical mass gap, or a non-perturbative plaquette value.

## What Changes For The Old Diagnostic

The perturbative diagnostic may keep using `beta = 6`, `N_c = 3`,
`g_bare^2 = 1`, and `alpha_bare = 1/(4 pi)` as its Wilson normalization,
but downstream users should cite this repair note plus the native beta
relationship note for that normalization.

The diagnostic itself remains conditional runner-local route pruning because
these inputs are still not retired here:

- W1: the NSPT coefficient packet `w_1..w_16`;
- W3: the MC comparator `<P>_MC = 0.5934`;
- W4: the F2 comparator;
- the claim that the finite perturbative/Pade envelope says anything about
  the actual non-perturbative beta=6 plaquette surface.

## Downstream Citation Rule

Rows that need only the Wilson normalization at `N_c=3`, `beta=6` should cite
this repair and the native beta relationship note. Rows that need a plaquette
value, perturbative coefficient packet, MC comparison, F2 comparison, or
physical-environment bridge must not cite this repair for those claims.

## Boundary

This is a partial import-retirement note. It is not a plaquette derivation,
not a physical mass-gap bridge, not a non-perturbative theorem, not an audit
verdict, not a new axiom, and not a new comparator authority.

