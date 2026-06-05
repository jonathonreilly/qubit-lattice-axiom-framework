# Generation Koide data reduces to a single derived modulus per sector

**Date:** 2026-06-05
**Type:** derivation
**Claim type:** theorem
**Proposed status:** proposed_retained (exact; independent audit sets ledger
status). Status authority: audit lane only.
**Runner:** `scripts/generation_dial_occupancy_free_input_2026_06_05.py`
(SUMMARY: PASS=50 FAIL=0).
**Cached log:** `logs/runner-cache/generation_dial_occupancy_free_input_2026_06_05.txt`

## Statement (positive)

For a `C3`-equivariant, `K/CPT`-real generation mass operator
`Y = a*I + b*C + conj(b)*C^2` (`a` real, `b` complex, `C` the `C3` shift), the
generation Koide observable is governed by **exactly one real modulus**.

Concretely: up to an overall scale, `Y` carries two real parameters — the
modulus `r = |b|^2/a^2` and the phase `theta = arg(b)` — and the Koide ratio
`Q = 1/3 + (2/3) r` depends on `r` **alone** (`theta` is a flat direction;
`dQ/dtheta = 0`, companion `KOIDE_CIRCULANT_VALUE_DERIVATION`). Therefore:

> The per-sector generation Koide data is **derived to be a one-parameter
> family** on the dial `Q = 1/3 + (2/3) r`, parameterised by a single real
> modulus `r` on a derived axis with three distinguished settings
> `r = 0, 1/2, 1` (`Q = 1/3, 2/3, 1`).

This is a derived dimensional reduction: the `C3`-equivariance (A2 carrier) and
`K/CPT`-reality (A3 readout) **force the one-modulus form**. The remaining
freedom is exactly one real number per sector — the modulus `r` — versus the
Standard Model, which leaves the full per-sector Yukawa matrix free. The
framework explains the *structure* and isolates the *single* residual flavor
parameter.

## Why this is the positive companion to the Koide value theorem

Treated exactly like the Koide value (`KOIDE_CIRCULANT_VALUE_DERIVATION`): the
value `r` is **not forced**, but the *structure* around it is derived. The
positive content is the **reduction** — the framework derives that generation
flavor collapses to a single modulus on a derived axis. "The modulus is free" is
the statement "the framework leaves exactly one derived parameter," which is the
reduction, not a gap.

## Proof (verified exactly in the runner, 50/50 PASS)

1. **One modulus controls `Q`.** `Q = 1/3 + (2/3)(|b|^2/a^2)` is invariant under
   overall scaling of `Y` and under `theta = arg(b)`; the only `Q`-relevant datum
   is `r = |b|^2/a^2`.
2. **Every dial value is realised.** The map `(a, |b|) -> r = |b|^2/a^2` is onto
   `[0, infinity)`: for any target `r0 >= 0` take `|b| = a*sqrt(r0)`. (Runner:
   explicit preimages for `r0 in {0, 1/2, 1, 2, 4, 7/13, 1000, generic}`.) So the
   one-parameter family is genuinely one-dimensional and fully populated.
3. **The axioms fix the *form*, not the *value*.** A1/A2 force `Y` circulant
   (`C3`-equivariance); A3's `K/CPT`-reality fixes `a` real and the two-block
   readout; none of A1/A2/A3 constrains the magnitude ratio `|b|/a` — A3
   explicitly supplies no weighting/occupancy rule. (Runner: each axiom predicate
   holds flavor-blind across the whole family; additivity never fixes the ratio.)
4. **Reduction.** Hence the per-sector generation Koide data = one real modulus
   `r` on the derived dial. (Independent confirmation: the isotype weight ratio
   is unconstrained — `koide_frobenius_isotype_split_uniqueness`,
   `action_normalization`, both `retained_no_go` on main.)

## Scope

This is the *parameter-count* companion to the value theorem: it derives that the
residual generation freedom is **one real modulus per sector** on the derived
axis. It does not assign a value to any sector's modulus (that is the input it
isolates). No measured masses are used.
