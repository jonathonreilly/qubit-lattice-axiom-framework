# Flavor Carrier-Measure Scoring Discriminator

**Date:** 2026-07-02
**Type:** bounded support (discriminator + conditional selection)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.

## Purpose

This note gives a bounded discriminator among the three carrier-measure scoring
rules already named in the parent wall note. It does not add a fourth rule. It
computes each named rule's generation weight on the one-site `hw=1` generation
surface, checks several finite invariance tests, and isolates the extra
readout requirement — no imported frame: the scoring partition must be
definable from the framework-supplied circulant algebra alone — under which
only the generator-channel Hilbert-Schmidt rule survives.

The conclusion is conditional on the named invariance requirement; not a selection theorem on the actual current surface.

## Setting

The generation factor is the `hw=1` subspace, identified here with `C^3` on the
one-site framework surface. Let `U` be the cyclic shift. The supplied circulant
Yukawa form is

```text
Y = a I + b U + conj(b) U^{-1}.
```

The modulus coordinate is

```text
r = |b|^2/a^2,
```

and the Koide functional is the parent note's

```text
Q = 1/3 + (2/3)r.
```

The parent note's generator-channel Hilbert-Schmidt setup is quoted verbatim:

````text
Let `J_N` be the all-ones matrix and let

```text
B_N = J_N - I_N.
```

In the Hilbert-Schmidt form,

```text
||I_N||^2 = N,        ||B_N||^2 = N(N-1),        <I_N, B_N> = 0.
```

If a separate theorem selects equal Hilbert-Schmidt energy across the two
generator channels, then

```text
N a^2 = N(N-1)b^2,
```

and therefore

```text
r = b^2/a^2 = 1/(N-1).
```
````

The parent note's three scoring-rule definitions are quoted verbatim:

```text
| partition | condition | result |
|---|---|---|
| generator channels `I` versus `J-I` | `3a^2 = 6b^2` | `r=1/2` |
| eigenvalue / idempotent content | `(a+2b)^2 = 2(a-b)^2` | `r=17/2 - 6 sqrt(2)` |
| per-mode basis equipartition | `a^2=b^2` | `r=1` |
```

The parent theorem target left open is quoted verbatim:

```text
derive, from the current framework surface, why the physical generation
readout uses generator-channel Hilbert-Schmidt scoring rather than
dimension/per-mode or idempotent/eigenvalue scoring.
```

## D1 - Reproduction

For `N=3`, the generator-channel Hilbert-Schmidt rule gives

```text
r = 1/(N-1) = 1/2,
Q = 1/3 + (2/3)(1/2) = 2/3.
```

The dimension/per-mode rule gives

```text
a^2 = b^2,
r = 1,
Q = 1.
```

The idempotent/eigenvalue rule solves

```text
(1 + 2t)^2 = 2(1 - t)^2,        t = b/a.
```

The positive real root is

```text
t = -2 + (3/2)sqrt(2),
```

so

```text
r = t^2 = 17/2 - 6 sqrt(2),
Q = 1/3 + (2/3)r = 6 - 4 sqrt(2).
```

Runner checks: `D1 S1 generator-channel HS gives r=1/(N-1)`,
`D1 S2 dimension/per-mode gives r=1`, `D1 S3 gives r=17/2-6*sqrt(2)`,
and the three `Q` checks.

## D2 - Invariance Separation

The finite tests are:

| test | S1 generator-channel HS | S2 dimension/per-mode | S3 idempotent/eigenvalue |
|---|---|---|---|
| `C_3` cyclic conjugation | invariant | invariant | invariant |
| registered complement-reading swap | invariant | invariant | invariant |
| global `U(1)` phase dressing of `b` | invariant on `r` | invariant on `r` | invariant on the parent `r` value as a modulus |
| `U(2)` remix of the channel pair (partition provenance) | condition moves under remix, but its partition is algebra-canonical (unit + HS-orthocomplement); no imported frame enters the rule | condition moves; partition requires an imported per-mode basis | condition moves; partition requires `Y`'s own idempotent/eigenvalue frame |

The table states a conditional separation only: conditional on the named invariance requirement; not a selection theorem on the actual current surface.

For `C_3`, the circulant matrix commutes with the cyclic shift:

```text
U (aI + bU + conj(b)U^{-1}) U^{-1}
= aI + bU + conj(b)U^{-1}.
```

All three scalar `r` values therefore survive cyclic relabeling.

For the registered complement-reading swap, the complement-reading equivalence
authority supplies the finite registration fact: the `hw=1` and `hw=2`
complement readings carry the same `C_3` orbit structure and the same supplied
circulant class, and every Record-registrable scalar readout takes the same
value on the two readings. Applying that swap to these scalar scoring values
therefore leaves each value unchanged.

For global phase dressing, `b -> exp(i theta)b` leaves

```text
|exp(i theta)b|^2/a^2 = |b|^2/a^2.
```

Thus the modulus coordinate `r` is inert. The runner checks this on an exact
Gaussian-integer witness and checks the S3 parent root after multiplication by
`i`.

For `U(2)` mixing of the two generator channels, write the channel coefficient
pair as `(c_+, c_-)`. Three exact facts hold (each is a runner witness, using
the Hadamard unitary `H = (1/sqrt(2)) [[1, 1], [1, -1]]`):

1. The total channel energy `|c_+|^2 + |c_-|^2` is invariant under any channel
   unitary. It is the only channel-pair scalar available without a frame.
2. The equal-energy CONDITION is not invariant as a coefficient condition:
   `H` sends the equal-split point `(1/sqrt(2), 1/sqrt(2))` to `(1, 0)`.
   Equal-split is a statement about a particular partition — for every rule.
3. What separates the rules is where their partition comes from. S1's
   partition is algebra-canonical: the unit direction `I` (the algebra
   identity) and its Hilbert-Schmidt orthocomplement inside the circulant
   span — no imported choice. The `H`-mixed pair
   `((I+B)/sqrt(2), (I-B)/sqrt(2))` is not of this form: neither member is
   the algebra unit, and the second is not HS-orthogonal to the unit (runner
   checks). S2's per-mode partition requires an imported distinguished basis
   of `C^3`: `H` sends `(1,1)` to `(sqrt(2),0)`, breaking per-mode equality.
   S3's partition is `Y`-dependent: the same transform applied to the S3
   parent root breaks the idempotent/eigenvalue relation.

So the `U(2)` leg separates the rules by partition provenance: S1 is the
unique parent-named rule whose scoring partition is supplied by the
framework's circulant algebra itself, with no imported per-mode basis and no
`Y`-dependent frame.

## D3 - Record-Additivity Compatibility

The Record axiom surface used here is only:

```text
Only records are readable. For any finite collection of pairwise-disjoint
records, scalar readout `I` is additive, with `I(empty)=0`.
```

Each of the three supplied scoring rules can be represented as a finitely
additive scalar readout once its sector coordinates are supplied:

| scoring rule | additive scalar used in the check | result |
|---|---|---|
| S1 | sum of total generator-channel Hilbert-Schmidt energies | compatible |
| S2 | sum of per-mode squared weights | compatible |
| S3 | sum of supplied idempotent/eigenvalue squared contents | compatible |

This table does not select among the rules. It says Record additivity alone
does not distinguish them, matching the parent wall note's boundary.

The runner checks `I(empty)=0` and `I(A disjoint union B)=I(A)+I(B)` on small
direct sums for S1, S2, and S3.

## D4 - Residual Sharpening

The sharp conditional is:

```text
IF the physical generation readout satisfies
1. C_3 cyclic-conjugation invariance,
2. the registered complement-reading swap invariance on the supplied slot
   model,
3. global U(1) phase-dressing inertness (dependence on b through the modulus
   only),
4. NO IMPORTED FRAME: its channel partition is definable from the
   framework-supplied circulant algebra alone (the unit direction and its
   Hilbert-Schmidt orthocomplement), with no imported per-mode basis and no
   Y-dependent idempotent frame,
5. finite Record additivity over pairwise-disjoint record collections,

THEN, among the three parent-named scoring rules, only generator-channel
Hilbert-Schmidt scoring survives. On the equal-energy locus this gives
r = 1/2 and Q = 2/3.
```

This summary is conditional on the named invariance requirement; not a selection theorem on the actual current surface.

The remaining open bridge is still the parent theorem target:

```text
derive, from the current framework surface, why the physical generation
readout uses generator-channel Hilbert-Schmidt scoring rather than
dimension/per-mode or idempotent/eigenvalue scoring.
```

Two named residuals remain after this note:

1. **The no-imported-frame requirement (item 4).** Deriving, from the current
   authority surface, that the physical generation readout admits no imported
   frame — equivalently, that its partition data is exhausted by the
   framework-supplied algebra (unit + HS-orthocomplement). This note supplies
   the discriminator for that requirement; it does not derive the requirement.
   Its supplier shape — "supplied readout context" — is the same shape the
   `kappa_EW` weighting wall names, so these two residuals are candidate
   wall-merge targets (one supplier could close both).
2. **The equal-channel-energy theorem.** The parent note's own "if a separate
   theorem selects equal Hilbert-Schmidt energy across the two generator
   channels" clause: this note leaves that clause exactly as open as the
   parent states it.

## Hostile Witnesses

Honesty witness against this note's own conditional: the S1 equal-split
condition is itself frame-dependent — `H` maps the equal-split coefficient
point `(1/sqrt(2), 1/sqrt(2))` to `(1, 0)` (runner check). The canonical
partition is therefore load-bearing for S1's rule; the conditional selection
in D4 rests on partition provenance (item 4), not on any claimed invariance of
the equal-split condition. A reader who grants items 1-3 and 5 but allows an
imported frame gets no selection from this note.

The unitary-basis separation is generic, not pointwise. S2 has a hostile special
point:

```text
H (1,0)^T = (1/sqrt(2), 1/sqrt(2))^T.
```

In that mixed basis, both per-mode squares are `1/2`, so S2 can mimic the S1
number at that special point. But the generic witness

```text
H (1,2)^T = (3/sqrt(2), -1/sqrt(2))^T
```

has per-mode squares `(9/2, 1/2)`, so the mimicry fails generically. The runner
checks both facts.

The S3 hostile check uses the parent root

```text
t = -2 + (3/2)sqrt(2)
```

for which `(1+2t)^2 = 2(1-t)^2` before mixing. After Hadamard mixing of the
two generator channels, the idempotent/eigenvalue relation is no longer zero.

## What This Note Does NOT Claim

- It does not derive the physical readout identification.
- It does not close the parent bridge.
- It adds no probability or Born content.
- It introduces no new axiom or primitive.
- It makes a conditional selection only: conditional on the named invariance requirement; not a selection theorem on the actual current surface.

## Load-Bearing Inputs

- `docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md` - parent
  wall note; supplies the three scoring-rule definitions and the open theorem
  target.
- `docs/MINIMAL_AXIOMS_2026-06-29.md` - axiom surface; supplies the Record
  finite-additivity sentence used in D3.
- `docs/ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md`
  - complement-reading equivalence authority; supplies the equality of
  Record-registrable scalar content under the `hw=1`/`hw=2` complement swap on
  the supplied finite slot model.
- `docs/KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md`
  - adjacent negative boundary; used only to keep the block from claiming that
  measure/kernel normalization fixes the occupancy cell.
- `docs/OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`
  - adjacent equipartition surface; used only to keep outcome equipartition
  separate from dictionary or cell discrimination.

## Paired Runner

Paired runner:

```text
scripts/frontier_flavor_carrier_measure_scoring_discriminator_2026_07_02.py
```

Expected terminal line:

```text
TOTAL: PASS=39 FAIL=0
```
