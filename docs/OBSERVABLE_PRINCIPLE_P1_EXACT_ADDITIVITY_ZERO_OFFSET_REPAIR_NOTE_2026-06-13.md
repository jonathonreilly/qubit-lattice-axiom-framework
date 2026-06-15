# Observable Principle Exact-Additivity Zero-Offset Repair

**Date:** 2026-06-13
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not quote, set, or predict audit outcomes.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent audit lane.
**Primary runner:**
[`scripts/frontier_observable_principle_exact_additivity_zero_offset_repair_2026_06_13.py`](../scripts/frontier_observable_principle_exact_additivity_zero_offset_repair_2026_06_13.py)
**Runner cache:**
[`logs/runner-cache/frontier_observable_principle_exact_additivity_zero_offset_repair_2026_06_13.txt`](../logs/runner-cache/frontier_observable_principle_exact_additivity_zero_offset_repair_2026_06_13.txt)

## Boundary

This note proves only the additive-constant repair below. It does not derive
P1, retire P1, derive scalar-generator additivity, reprove
Shannon-Khinchin-Aczel-Daroczy classification theorems, adopt a shifted
composition law, change any axiom, add any primitive, or apply any audit
verdict. The existing Shannon/Khinchin bridge note remains a separate parent
surface:
[`OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md).

## Theorem

Let `r > 0` be the positive multiplicative scalar supplied by a block
factorization context, and let

```text
W_b(r) = c log r + b
```

for real constants `b` and `c`. Under the exact additive composition law

```text
W_b(r_1 r_2) = W_b(r_1) + W_b(r_2)      for all r_1, r_2 > 0,
```

the additive constant is forced to vanish: `b = 0`.

Indeed,

```text
W_b(r_1 r_2) - W_b(r_1) - W_b(r_2)
  = c log(r_1 r_2) + b - (c log r_1 + b) - (c log r_2 + b)
  = -b.
```

Exact additivity for all positive `r_1,r_2` therefore requires `-b=0`.
Equivalently, setting `r_1=r_2=1` gives `W_b(1)=2W_b(1)`, hence
`W_b(1)=0`, and since `log 1=0`, this again gives `b=0`.

The shifted family with `b != 0` satisfies a different law,

```text
W_b(r_1 r_2) = W_b(r_1) + W_b(r_2) - b.
```

That shifted law is a separate normalization convention. It is not the exact
additivity law above and is not adopted by this note.

## Consequence

When the exact-additive representative is written as `c log r + b`, the
permitted exact-additive representative is `c log r`; an arbitrary additive
offset is not available without changing the composition law. This is a repair
to the normalization boundary only. It leaves the substantive open question
unchanged: the framework still needs an independent derivation or accepted
premise for why the physical scalar generator must satisfy exact additivity in
the first place.

## Verification

The runner checks:

- symbolic simplification of the exact-additivity defect for `W_b`;
- symbolic solution of the exact-additivity condition, yielding `b=0`;
- the separate shifted-law identity for the same shifted family;
- rational witness values showing that nonzero offsets fail exact additivity;
- source-note guardrails that prevent this repair from being read as P1
  closure, a shifted-law adoption, an axiom/primitive change, or an audit
  verdict.

Expected runner result: `PASS=9, FAIL=0`.
