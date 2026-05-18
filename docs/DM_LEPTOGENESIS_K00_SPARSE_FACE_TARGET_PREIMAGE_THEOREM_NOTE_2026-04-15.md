# DM Leptogenesis `K00`-Sparse-Face Target-Preimage Theorem

**Date:** 2026-04-15 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded constructive-preimage theorem — adopting the target-
independent scalar quotient section `K00 = 0` and the exact sparse face
`y2 = 0`, the observed live DM-neutrino point admits a constructive
preimage on the fixed native `N_e` seed surface.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding theorem module.
**Primary runner / module:** `scripts/frontier_dm_leptogenesis_k00_sparse_face_target_preimage_theorem.py`

## Purpose

This wrapper note documents the `K00`-sparse-face target-preimage theorem
so downstream notes (notably the
gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1
reduced-packet complex-Givens selector theorem) can register it as a
one-hop dependency in the citation graph.

## Theorem

After adopting the target-independent scalar quotient section `K00 = 0`
and the exact sparse face `y2 = 0`, the active Hermitian block becomes

```
H = [[x1^2 + y1^2,   x2 y1,            x1 y3 e^{-i delta}],
     [x2 y1,         x2^2,             0                  ],
     [x1 y3 e^{i delta},  0,           x3^2 + y3^2        ]].
```

The observed live DM-neutrino point admits a constructive preimage on the
fixed native `N_e` seed surface under this sparse face.

## What this module provides

- The sparse-face constraint `y2 = 0` and its consequence for the
  active Hermitian block.
- A constructive preimage routine for the observed DM-neutrino point on
  this sparse face.
- Boundary conditions and witness constants used downstream by the
  reduced-packet complex-Givens selector theorem.

## Boundary

This wrapper note records the bounded-theorem character of the
sparse-face preimage theorem. It does not claim:
- a framework-level derivation of `K00 = 0` (target-independent scalar
  quotient section; see
  [DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md](DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md));
- uniqueness across alternative sparse-face choices beyond `y2 = 0`;
- closure of the DM-leptogenesis chain.

Its only function is to provide a citeable one-hop authority for the
sparse-face preimage construction so downstream notes can register it
cleanly.

## Upstream authority

- [DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md](DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md) — `K00 = (K_mass)00` target-independent scalar quotient section.
