# Generation Koide data reduces to a single derived modulus per sector

**Date:** 2026-06-05
**Type:** bounded_theorem — derivation
**Claim type:** bounded_theorem — theorem (conditional on the supplied generation carrier and
readout context).
**Status authority:** independent audit lane only. This note does not set or
predict the ledger outcome.
**Runner:** `scripts/generation_dial_occupancy_free_input_2026_06_05.py`
(SUMMARY: PASS=48 FAIL=0).
**Cached log:** `logs/runner-cache/generation_dial_occupancy_free_input_2026_06_05.txt`

## Statement (positive)

For a `C3`-equivariant, `K/CPT`-real generation mass operator
`Y = a*I + b*C + conj(b)*C^2` (`a` real, `b` complex, `C` the `C3` shift), the
generation Koide observable is governed by **exactly one real modulus**.

Concretely: up to an overall scale, `Y` carries two real parameters — the
modulus `r = |b|^2/a^2` and the phase `theta = arg(b)` — and the Koide ratio
`Q = 1/3 + (2/3) r` depends on `r` **alone** (`theta` is a flat direction;
`dQ/dtheta = 0`, companion
[`KOIDE_CIRCULANT_VALUE_DERIVATION`](KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md)). Therefore:

> The per-sector generation Koide data is **derived to be a one-parameter
> family** on the dial `Q = 1/3 + (2/3) r`, parameterised by a single real
> modulus `r` on a derived axis with three distinguished settings
> `r = 0, 1/2, 1` (`Q = 1/3, 2/3, 1`).

This is a conditional dimensional reduction: given the cited generation carrier,
`C3`-equivariance, and the supplied `K`/CPT-real readout context, the
`Q`-relevant data reduce to the one-modulus form. The remaining freedom is
exactly one real number per sector — the modulus `r` — versus the Standard Model,
which leaves the full per-sector Yukawa matrix free. The calculation isolates
the *structure* and the single residual flavor parameter.

## Why this is the positive companion to the Koide value theorem

Treated exactly like the Koide value
([`KOIDE_CIRCULANT_VALUE_DERIVATION`](KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md)):
the value `r` is **not fixed**, but the *structure* around it is derived under
the supplied carrier/readout hypotheses. The positive content is the
**reduction**: generation flavor collapses to a single modulus on the derived
Koide axis. "The modulus is free" means the current assumptions leave exactly
one parameter; it is the honest residual input, not a closed prediction.

## Proof (verified exactly in the runner, 48/48 PASS)

1. **One modulus controls `Q`.** `Q = 1/3 + (2/3)(|b|^2/a^2)` is invariant under
   overall scaling of `Y` and under `theta = arg(b)`; the only `Q`-relevant datum
   is `r = |b|^2/a^2`.
2. **Every dial value is realised.** The map `(a, |b|) -> r = |b|^2/a^2` is onto
   `[0, infinity)`: for any target `r0 >= 0` take `|b| = a*sqrt(r0)`. (Runner:
   explicit preimages for `r0 in {0, 1/2, 1, 2, 4, 7/13, 1000, generic}`.) So the
   one-parameter family is genuinely one-dimensional and fully populated.
3. **The supplied structure fixes the *form*, not the *value*.** Given the cited
   generation carrier, `C3`-equivariance makes `Y` circulant; the adopted
   `K`/CPT-real readout condition fixes `a` real and the two-block readout
   (see
   [`RECORD_GENERATION_READOUT_TWO_SECTORS`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md)).
   Lattice, Quantum, and Record do not constrain the magnitude ratio `|b|/a`;
   Record explicitly supplies no weighting or occupancy rule. (Runner: each
   structural predicate holds flavor-blind across the whole family; additivity
   never fixes the ratio.)
4. **Reduction.** Hence the per-sector generation Koide data = one real modulus
   `r` on the derived dial. Companion no-go surfaces such as
   [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md) and
   [`ACTION_NORMALIZATION_NOTE.md`](ACTION_NORMALIZATION_NOTE.md) track the same weight/normalization freedom;
   this note does not assert their audit status.

## Scope

This is the *parameter-count* companion to the value theorem: it derives that the
residual generation freedom is **one real modulus per sector** on the derived
axis. It does not assign a value to any sector's modulus (that is the input it
isolates). No measured masses are used.
