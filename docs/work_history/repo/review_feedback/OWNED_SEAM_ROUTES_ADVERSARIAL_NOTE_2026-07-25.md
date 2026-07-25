# Owned-seam routes adversarial note

**Type:** meta

**Date:** 2026-07-25

**Reviewed commits:** `16a550601d`, `1f75a79e4f`

**Authority:** none

**Audit:** unset

**Status:** transition constructions positive; advertised full physical compositions open

## Comparative verdict

Both repairs contain substantial positive work. The direct-ROM route removes
the old decoder self-award and derives conflict-free projector--Pauli
descriptors. The sparse route goes further on the chart-cocycle transition: it
executes an exact 224-CZ correction as a 378-factor nearest-neighbor word and
returns dirty transit M2 exactly.

Neither runner executes its advertised full physical all-eleven update on the
common encoding. This is an equivalent-gap disposition, not a no-go.

| Obligation | Direct ROM `16a550601d` | Sparse route `1f75a79e4f` |
| --- | --- | --- |
| Old source-XOR decoder self-award removed | closed | not used |
| Physical transition descriptors / routed transition | closed as finite descriptors | closed as 378-factor word |
| Transition order | not assembled | closed: correction must precede seams |
| Work return | membership argument per descriptor | closed for both dirty center M2 |
| All eleven signed physical seams applied on common `E` | open | open |
| Shared q-chart preservation after complete word | open | open |
| Physical-word covariance | open | open |
| Direct common-code intertwiner/leakage residual | open | open |

## Direct-ROM route

### Source-pair rekey attack passes

The new descriptor conflict check keys rows by `(owner, source_observation,
source_pair, target_pair)`, while the claimed projector control uses physical
observations. Removing the two hidden ray-pair fields does not expose a conflict
on the enumerated domain:

- 46,306 hidden-key directed rows remain 46,306 distinct physical directed
  `(owner, source_observation, target_observation)` rows;
- none has more than one Pauli transition;
- the 23,153 unordered observation pairs contain exactly the expected two
  reverse orientations.

Thus `source_pair` is redundant on this finite enumeration; it is not hiding a
projector conflict. This positive result should be retained.

### Coefficient-to-transition association is absent

`complex_givens_unprepare` and `local_carrier` collect a flat sequence of 24
complex Givens coefficients per cell. In contrast,
`physical_two_level_primitive_audit` stores only
`(target_observation, phase, x_word, z_word)` in each descriptor. It never reads
`givens_coefficients`, records no Givens stage/order, and never multiplies the
projector--Pauli primitives with their complex rotations. A unit-norm check on
the detached coefficient list does not prove that the right coefficient is
applied to the right physical transition in the right order.

### Support count is not a locality-diameter result

The reported maximum transition support is 26 M2 and the maximum
control-plus-transition support is 65 M2. The audit computes Hamming support
only; it assigns no geometric locations to those factors and measures no graph
or lattice diameter. Consequently it does not establish a bounded-range local
law.

### The 46,306 rows are not yet a supplied autonomous ROM

The descriptor dictionary is reconstructed on the host by iterating all 2,629
logical labels and their physical branch histories separately at each tested
volume. It is discarded after returning its row count; no rows, digest,
coefficient tags, or fixed reversible lookup circuit are supplied. The returned
`physical_M2_primitive_supplied` boolean is simply
`descriptor_conflicts == 0`.

This is a valid finite synthesis inventory. It is not yet an explicit fixed ROM
word or an autonomous volume-independent local rule. The all-eleven result also
remains `11 * max(local residual)` in `composed_update_controls`; no common
physical product is applied.

## Sparse routed-transition route

### The routed correction is genuinely executed

The route contains 33 same-cell, 114 neighbor-cell, and 77 distance-two CZ
terms. Every distance-two term is realized as `SWAP-CZ-SWAP`. The runner checks
all 616 local dirty-transit truth-table cases and all 10,516 combinations of the
2,629 `n <= 2` columns with two arbitrary center-transit bits. Data, phase, and
both transit bits return exactly. Sequential reuse of the two center M2 across
all 77 macros is therefore closed for the transition word.

The order is also substantive. `candidate_stream @ transition` equals the
target exactly, whereas moving the correction after the signed seam product
leaves 100 mismatched columns with raw residual 2.

### `factorized_intertwiner` is a Gram-isometry identity

The claimed same-encoding check does not accept a physical word. It computes

```text
logical @ (I - E_refresh^dag E_refresh)
```

and its left-handed analogue. Therefore every logical matrix passes whenever
`E_refresh` is an isometry. An adversarial nontrivial diagonal unitary unrelated
to the target update also returns only roundoff residual. This checks the Gram
matrix, not
`U_physical E_refresh - E_refresh G` or physical code leakage.

### The eleven seam words are resource-counted, not composed

`signed_seam_resources` calls `signed_carrier_census` independently for each of
the 11 edges. It checks coefficient preparation and clean local qutrit/matcher
resources, but it never calls the local seam matrices or applies an eleven-seam
product. `same_encoding_certificate` then invokes only the Gram identity above.
The logical `candidate_stream` correctly represents the intended signed seam
product, but it is not the product of the physical signed-carrier words.

Accordingly, the initial `E_refresh` shared-copy equality result is positive but
does not demonstrate preservation or correct update of shared q-chart registers
after the composed transition/seam/contact word.

### Covariance is geometric plus logical, not physical-word covariance

The 24-frame test rotates the tuple of routed endpoint/midpoint labels and
checks its distance-class census. The 576-product test checks functorial tuple
transformation. Separately, Route C checks covariance of the logical
`target_update`. No test rotates or compares an executed physical routed-plus-
seams operator on `E_refresh`. The physical covariance obligation remains open.

The macro deletion residuals do not add such evidence: the 224 values are
created as the literal tuple `2.0 for _term in ROUTED_TERMS`.

## Exact missing executed objects

For the direct route, supply an ordered row
`(owner, stage, source/target physical observations, Pauli transition, complex
Givens coefficient)` either as a hashed fixed ROM or as an executed autonomous
local generator. Measure its geometric diameter, apply all eleven owners on one
common encoding, and compute the direct intertwiner and leakage.

For the sparse route, construct one actual `U_physical` on the 59,941-row
`E_refresh` ambient that composes the supplied free coin, routed 224-CZ
transition, all eleven signed-carrier seams, shared-chart updates, contact, and
clean return. Then compute

```text
||U_physical E_refresh - E_refresh G_target||
```

and common-code leakage at L5 and held L6, followed by the corresponding
rotated-physical-word covariance residual. This is target-equivalent to the
current full-physical terminal claim.

## Reproduction

```bash
PYTHONPATH=scripts:<route-b-scripts>:<route-c-scripts> \
  python3 scripts/frontier_owned_seam_routes_adversary_2026_07_25.py
```

The companion terminates with
`OWNED_SEAM_TRANSITIONS_POSITIVE_FULL_PHYSICAL_COMPOSITIONS_OPEN` when all
adversarial controls behave as reconstructed.
