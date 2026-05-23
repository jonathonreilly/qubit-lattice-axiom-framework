# DM Leptogenesis `dW_e^H` Even-Split Transfer-Layer Theorem

**Date:** 2026-04-19 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded transfer-layer theorem identifying the unsymmetrized
even column split on the compressed charged projected-source codomain.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding theorem module.
**Primary runner / module:** `scripts/frontier_dm_leptogenesis_dweh_even_split_transfer_layer.py`

**Suggested decoration parent (for audit-graph hygiene):** This row's
canonical decoration parent in the retained graph is
[`KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md`](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md). The audit lane
may convert this row from `audited_renaming` to
`decoration_under_koide_dweh_cyclic_compression` on the next re-pass, which would correctly
make this row a non-chain-closure handle. Source-side metadata only;
audit lane owns the verdict.

## Purpose

This wrapper note documents the `dW_e^H` even-split transfer-layer theorem
so downstream notes (notably the
gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1
reduced-packet complex-Givens selector theorem) can register it as a
one-hop dependency in the citation graph.

## Question and answer

On the compressed charged projected-source codomain

```
dW_e^H = Schur_Ee(D_-)
```

what is the exact unsymmetrized even column split that remains relevant for
Blocker 3, and how does it descend to the sparse-face live source readout?

On the exact projected Hermitian response pack `(R11, R22, R33, S12, A12,
S13, A13, S23, A23)`, the unsymmetrized even column split is the pair
`(S12, S13)`. This pair is the load-bearing input for the downstream
sparse-face live source readout `TARGET`.

## What this module provides

- `TARGET` — the live DM target on the retained slice (used by the
  reduced-packet complex-Givens selector theorem).
- Definitions and verification routines for `(S12, S13)` as the
  even-column split on `dW_e^H`.

## Boundary

This wrapper note records the bounded-theorem character of the
even-split transfer-layer. It does not claim:
- a framework-level derivation of the Schur projection;
- uniqueness across alternative column splits;
- closure of any downstream gauge-vacuum-plaquette theorem.

Its only function is to provide a citeable one-hop authority for
`TARGET` and the `(S12, S13)` even-column split so downstream notes can
register them cleanly.
