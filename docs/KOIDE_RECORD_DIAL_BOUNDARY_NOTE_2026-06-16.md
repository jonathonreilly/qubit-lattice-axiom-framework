# Koide Record Dial Boundary Note

**Date:** 2026-06-16
**Lane:** Charged-lepton Koide / Record / scalar measure choice
**Claim type:** exact boundary theorem
**Status:** exact negative boundary for the Record-plus-`SO(2)` route, with
bounded support for the selected-endpoint consequences. This note does not
derive a physical choice of the block-count endpoint and does not promote
operator-side Koide closure. It proves that Record finite additivity and
`SO(2)` phase erasure leave a one-parameter sector-weight family unless an
additional independent weighting selector is supplied.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_koide_record_dial_boundary_2026_06_16.py`](../scripts/frontier_koide_record_dial_boundary_2026_06_16.py)

---

## 1. Boundary Statement

Let the `Herm_circ(3)` scalar carrier be reduced to the two positive
block-total energies

```text
E_+ = 3 a^2,          E_perp = 6 |b|^2.
```

The `SO(2)` action on the real doublet rotates `(Re b, Im b)` and therefore
preserves `E_perp`. It also leaves `E_+` fixed. Hence every log-law

```text
S_s(E_+, E_perp) = log E_+ + 2^s log E_perp
```

is `SO(2)`-invariant. At fixed total `E_+ + E_perp`, its stationary point obeys

```text
E_+ / E_perp = 2^(-s),
kappa := a^2 / |b|^2 = 2 E_+ / E_perp = 2^(1-s).
```

Thus:

| selector | `s` | weights on `(E_+, E_perp)` | `kappa` |
|---|---:|---|---:|
| block-count / one scalar per isotype slot | `0` | `(1, 1)` | `2` |
| dimension / Born / determinant carrier | `1` | `(1, 2)` | `1` |
| unsupplied position | free | `(1, 2^s)` | `2^(1-s)` |

The Record axiom supplies finite scalar additivity once a readout context and
finite central-sector decomposition are supplied. It explicitly supplies no
weighting, normalization, probability, dynamics, within-sector data, or
occupancy rule. Therefore Record additivity can add the sector readouts but
cannot choose `s`.

This is a boundary, not a closure theorem: `s = 0` remains the exact
block-count endpoint that gives `kappa = 2`, but the endpoint is selected only
when a block-count scalar-carrier rule is independently supplied.

## 2. Relation to the Existing Koide Stack

This note is the source-side wiring layer between:

- [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md),
  which verifies the finite block-total algebra and the `d = 3` multiplicity
  pattern;
- [`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`](GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md),
  which computes the one-parameter sector-weight dial `r(s) = 2^(s-1)`;
- [`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`](CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md),
  which identifies the remaining charged-lepton value as the block-count vs
  dimension counting bit;
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md), whose Record
  axiom allows finite scalar additivity but withholds the weighting selector.

The consequence is narrower and cleaner than the older "derive the `SO(2)`
quotient" phrasing: the `SO(2)` quotient is not by itself the missing selector.
It removes the doublet phase, leaving a radial doublet scalar. The unsupplied
object is the sector-weight position `s`, equivalently the choice between
block-count and dimension weighting.

## 3. Proof

Write `b = x + i y`. The doublet rotation

```text
(x, y) |-> (cos theta x - sin theta y, sin theta x + cos theta y)
```

preserves `x^2 + y^2`, so it preserves `E_perp = 6(x^2 + y^2)`. The singlet
energy `E_+ = 3a^2` is independent of `(x, y)`, hence also invariant. Any
function of `(E_+, E_perp)` therefore factors through the `SO(2)` quotient;
the family `S_s` above is only one such family.

For `X = E_+ > 0`, `Y = E_perp > 0`, maximize

```text
log X + 2^s log Y
```

subject to `X + Y = T`. The Lagrange equations give

```text
1 / X = lambda,
2^s / Y = lambda,
```

so `X / Y = 2^(-s)`. Since `X/Y = E_+/E_perp = a^2/(2|b|^2)`, the operator
ratio is `kappa = a^2/|b|^2 = 2 X/Y = 2^(1-s)`.

The endpoints `s=0` and `s=1` are both `SO(2)`-invariant and both compatible
with finite scalar additivity. They differ only by the weighting convention.
The Record axiom states that it supplies no such weighting or normalization,
so the selection of `s` is not derivable from Record additivity alone.

## 4. What This Repairs

The parent block-total theorem can safely retain its finite algebra:

- if the block-count endpoint is selected, the equal-weight law gives
  `kappa = 2`;
- if the dimension endpoint is selected, the determinant/Born law gives
  `kappa = 1`;
- without an independently accepted endpoint selector, the physical scalar-lane
  value remains open.

This removes two overclaim traps:

1. `SO(2)` invariance is not a unique-measure theorem, because every `S_s`
   factors through the same quotient variables.
2. Record finite additivity is not a hidden measure axiom, because it supplies
   no weighting or normalization rule.

## 5. Runner

Expected output:

```text
TOTAL: PASS=20 FAIL=0
```

The runner checks the `SO(2)` invariance, the Lagrange stationary family, the
two endpoints, the Record axiom boundary text, the parent Koide boundary text,
and the June 5 dial/one-bit source links.
