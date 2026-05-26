# Gauge-Vacuum Plaquette Compressed Rim-Evaluation Theorem

**Date:** 2026-04-17 (bounded finite-sector rescope 2026-05-26)
**Status:** bounded finite-sector compressed-boundary support on the plaquette
PF lane. The full local rim functional `B_beta(W)` and the physical
untruncated Wilson-environment coefficient vector remain open, but after
compression to the marked finite class sector the `W`-dependence is explicit
through the canonical Peter-Weyl evaluation vector.
**Type:** bounded_theorem
**Runner:** `scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py`

## Question

Can any part of the rim functional actually be derived now, rather than only
named as the missing local object `B_6(W)`?

## Answer

Yes, after compression to the marked finite class-function sector.

The full local rim functional on the orthogonal-slice Hilbert space is still
not derived. But the `W`-dependence of the compressed boundary data is already
exact and canonical.

Within the retained-bounded spatial-environment transfer packet, the compressed
finite-sector coefficients satisfy

`z_(p,q)^env(beta) = <chi_(p,q), (S_beta^env)^(L_perp-1) eta_beta>`.

Define the class-sector coefficient vector

`v_beta = sum_(p,q) z_(p,q)^env(beta) chi_(p,q)`.

Then for every marked holonomy `W`, the central boundary class function is
exactly

`Z_beta^env(W) = <K(W), v_beta>`,

where

`K(W) = sum_(p,q) d_(p,q) conj(chi_(p,q)(W)) chi_(p,q)`

is the canonical Peter-Weyl evaluation vector on the marked class sector.

So after finite-sector compression:

- the `W`-dependence is already explicit,
- the remaining unknown is only the beta-dependent vector `v_beta`,
- equivalently the coefficients `z_(p,q)^env(beta)` or `rho_(p,q)(beta)`.

That is a genuine bounded derivation step. It is not a derivation of the full
untruncated physical Wilson environment.

## Setup

From the exact spatial-environment transfer theorem already on `main`:

- the environment boundary class function is a boundary amplitude of one
  explicit positive transfer operator,
- its class-sector coefficients are exact matrix elements
  `z_(p,q)^env(beta)`.

From the exact character-measure theorem:

- `Z_beta^env(W)` is a central class function of the marked holonomy `W`.

So the class-sector problem is exactly in the setting of Peter-Weyl
decomposition on central functions.

## Theorem 1: bounded finite-sector compressed boundary-evaluation functional

Let

`v_beta = sum_(p,q) z_(p,q)^env(beta) chi_(p,q)`.

Define

`K(W) = sum_(p,q) d_(p,q) conj(chi_(p,q)(W)) chi_(p,q)`.

Then by the exact character expansion of the boundary class function,

`Z_beta^env(W)
 = sum_(p,q) d_(p,q) z_(p,q)^env(beta) chi_(p,q)(W)
 = <K(W), v_beta>`.

So the finite-sector compressed boundary functional is explicit and canonical.

## Corollary 1: the finite-sector compressed `W`-dependence is no longer open

After compression to the marked finite class sector, the missing datum is not
the finite-sector evaluation map `W -> K(W)`.

The `W`-dependence is already explicit in `K(W)`.

What remains unknown is only:

- the beta-dependent coefficient vector `v_beta`,
- equivalently `z_(p,q)^env(beta)`,
- equivalently `rho_(p,q)(beta)`.

## Corollary 2: what remains open is the full local rim functional and physical environment, not the finite-sector evaluation map

This theorem does **not** derive the full local rim functional on the slice
Hilbert space.

It derives only the compressed class-sector boundary functional.

So the current local rim-coupling boundary theorem remains correct:

- the full local map `B_beta(W)` is still open,
- but after compression its `W`-dependence is already canonical.

## What this closes

- bounded derivation of the compressed finite class-sector boundary functional
- bounded clarification that the finite-sector `W`-dependence is not part of
  the remaining compressed unknown
- bounded reduction of the finite-sector compressed boundary problem to one
  beta-dependent coefficient vector

## What this does not close

- explicit full-slice rim functional `B_beta(W)`
- explicit `B_6(W)`
- explicit `K_6^env`
- explicit `S_6^env`
- explicit framework-point plaquette PF data
- the full untruncated physical Wilson-environment coefficient vector

## Why this matters

This is a bounded finite-sector derivation step on the rim side.

The branch no longer has to treat the entire compressed boundary family as
unknown. After compression, the `W`-dependence is explicit and canonical.

So the remaining plaquette PF construction problem is narrower:

- full local derivation of `B_6(W)` on the slice Hilbert space,
- and the beta-dependent coefficient vector it induces after compression.

## 2026-05-26 bounded rescope for re-audit

The 2026-05-25 audit verdict correctly objected that the previous
`positive_theorem` framing was too broad: the packet does not derive the full
untruncated physical Wilson-environment transfer or character-measure data.
The source claim is therefore narrowed to the exact surface checked by the
runner and supported by the three declared retained-bounded dependencies:

```text
finite marked class sector + retained-bounded transfer/character packets
=> explicit Peter-Weyl evaluation map Z_beta^env(W)=<K(W), v_beta>
```

This row no longer claims a full physical rim theorem. It claims only the
bounded finite-sector evaluation-map identity and records that the remaining
physical coefficient vector / full local rim problem is outside this row.
Independent audit still owns the ledger verdict and any effective-status
change.

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links for
the two upstream theorems consumed by the compressed rim-evaluation
construction (spatial-environment transfer theorem; exact character-
measure theorem). It does not promote this note or change the audited
claim scope.

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md) — spatial-environment transfer theorem supplying the compressed coefficients `z_(p, q)^env(beta) = <chi_(p, q), (S_beta^env)^(L_perp - 1) eta_beta>` consumed in the Setup.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md) — exact character-measure theorem establishing `Z_beta^env(W)` as a central class function of the marked holonomy `W`, supplying the Peter-Weyl normalization (the `d_(p, q)` factor in `K(W) = sum_(p, q) d_(p, q) conj(chi_(p, q)(W)) chi_(p, q)`).
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md) — narrow companion strengthening the character-measure realization uniqueness on the finite-box convolution surface.
