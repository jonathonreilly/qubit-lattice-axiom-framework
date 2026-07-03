# Equal-Channel Energy Reduces to the Equipartition Surface; the Dictionary Residual Is the Scoring Residual

**Date:** 2026-07-02
**Type:** bounded support (reduction + exact correspondence)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Boundary:** conditional bounded support. The reduction is conditional on the
named identification premise `E-ident`, the registrability reading `R*`, and
the inherited conditions of the equipartition note. Sibling dependency classes
remain independent-audit owned.

## Purpose

This note records an exact finite correspondence between the outcome-dictionary
residual of the equipartition note and the S1/S2 carrier-measure scoring
residual. It is not an unconditional equal-channel-energy theorem.

The reduction is:

```text
equal registered weight on the two equipartition cells
  + E-ident
  + R* selecting the component dictionary within the two-dictionary pair
=> generator-channel equal Hilbert-Schmidt energy
=> r = 1/2, Q = 2/3.
```

`E-ident` is a named identification premise. It is supported by the exact
structural parallel that both sides are the `C_3` singlet/doublet split, but
this note does not derive that the equipartition note's registered weights are
the Hilbert-Schmidt channel energies.

## Inherited Equipartition Surface

The inherited boundary is quoted verbatim:

```text
This note proves the four statements below on the supplied 2-outcome
registered surface. It does not discriminate the fork, select a cell, fix `r`,
correct any landed note, or resolve the dictionary. The `(1,2)` and `(1,1)`
weightings are both stated as supplied bookkeeping conventions.

FIREWALL: no fork branch or occupancy cell is discriminated or selected here.
The conditioned-flow route cannot by itself discriminate between them; `r` is
never fixed by the route alone. The landed R-D chain is sharpened by making its
conditionality explicit, not contradicted; this is not a correction. The
occupancy binary stays open. This is a sharpening, not a correction.
```

The invariant-selection statement is quoted verbatim:

````text
**Invariant selection.** For any bookkeeping dictionary
`x = phi(r)` with `phi` a strictly monotone bijection on the relevant domain,
the flow in `r`-coordinates is

```text
r -> phi^{-1}(phi(r)^2).
```

The fixed-point equation is `phi(r) = phi(r)^2`, so the outcome-space fixed
values are `phi(r) in {0,1}`. The interior fixed point is therefore
`r* = phi^{-1}(1)`. The invariant selection is `x = 1`, i.e. outcome
equipartition: equal registered weight on `s` and `d`. This statement is
independent of the dictionary. `[checks 1-4]`
````

The two explicit dictionaries are quoted verbatim:

```text
For the two explicit dictionaries, the maps are:

- `x = 2r`: `r -> (2r)^2/2 = 2r^2`, with finite fixed set `{0, 1/2}`.
- `x = r`: `r -> r^2`, with finite fixed set `{0, 1}`.
```

The dictionary-as-atom paragraph is quoted verbatim:

```text
**Dictionary-as-atom.** Under the component dictionary `x = 2r`,
the invariant selection `x = 1` reads `r* = 1/2`, the orbit cell. Under the
slot dictionary `x = r`, the same invariant selection reads `r* = 1`, the
sector cell. Re-solving in each coordinate gives exactly `{0, 1/2}` versus
`{0, 1}`, with the projective doublet endpoint represented by `s = 1/r = 0`
in both charts. The two occupancy cells are the two dictionaries' readings of
the same outcome-space selection. `[checks 5-6]`
```

The tri-guise identity is quoted verbatim:

```text
**Tri-guise identity on the supplied labels.** The dictionary choice is the
same two-label bookkeeping choice written three ways:

- Supplied kernel-normalization bookkeeping: the doublet Berezin block scales as
  `det(lambda K) = lambda^k det(K)`, so the two block conventions carry the
  lambda-exponent pair `{2, 1}` for `2x2` versus `1x1` blocks.
- Supplied corner mode-set bookkeeping: the two doublet weights are `Z_d = 2pi/g` and
  `Z_d = pi/g`.
- Supplied flow coordinate: the dictionary pair is `x = 2r` and `x = r`.

The pairwise bijections are explicit. The supplied rho-map orientation is
`rho = (pi/g)/Z_d`, `r = 1/(2 rho)`. Thus `Z_d = pi/g` gives `rho = 1` and
`r = 1/2`, matching the component dictionary's fixed-point reading
`x = 2r`; `Z_d = 2pi/g` gives `rho = 1/2` and `r = 1`, matching the slot
dictionary's fixed-point reading `x = r`. The kernel exponent labels map to
the same two dictionary labels by block size. The composed maps agree with the
direct maps, so the three two-element descriptions form the same binary, not
three independent binaries. `[checks 7-8]`
```

The inherited Does NOT section is quoted verbatim:

```text
- Does not discriminate either fork branch.
- Does not select either occupancy cell.
- Does not fix `r`.
- Does not correct any landed note.
- Does not contradict the landed R-D chain.
- Does not resolve the dictionary.
- Does not close the occupancy binary; the occupancy binary stays open.
```

## Parent Equal-Energy Clause

The parent clause is quoted verbatim:

````text
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

For `N=3`, the parent gives `r=1/2` and

```text
Q = 1/3 + (2/3)r = 2/3.
```

The Block01 sibling records the same values:

```text
r = 1/(N-1) = 1/2,
Q = 1/3 + (2/3)(1/2) = 2/3.
```

It also records the S2 per-mode values:

```text
a^2 = b^2,
r = 1,
Q = 1.
```

The Block03 sibling supplies the conditional `R*` exclusion of S2-class
imported-basis scorings:

```text
So the same supplied `Y`, expressed in two imported bases in the same choice
orbit, gives different S2 per-mode verdicts: equal in the first basis and
non-equal in the Hadamard-mixed basis. Therefore S2-class imported-basis
scorings are not R*-registrable.
```

and the S1 compatibility:

````text
For `N=3`,
with `B = J - I`, the supplied Hilbert-Schmidt data are:

```text
||I||^2 = 3,   ||B||^2 = 6,   <I, B> = 0.
```
````

## T1 - E-ident: Channel/Cell Correspondence

**Premise E-ident.** On the `C_3` generation surface, the two generator
channels `{unit I, doublet complement B}` correspond to the equipartition
note's two cells `{s (singlet), d (doublet)}` as follows:

- the singlet cell `s` carries the unit-channel registered weight, proportional
  to `N a^2`;
- the doublet cell `d` carries the complement-channel registered weight,
  proportional to `N(N-1)|b|^2`.

At `N=3`, Block01/Block03 verify the normalization:

```text
||I||^2 = 3,        ||B||^2 = 6.
```

Thus the E-ident reading is:

```text
p_s proportional to 3a^2,
p_d proportional to 6|b|^2 = 2N|b|^2 at N=3.
```

Equivalently,

```text
x = p_d/p_s = 6|b|^2/(3a^2) = 2r.
```

This is the component dictionary. The exact structural parallel is the shared
`C_3` singlet/doublet split. The derivation of E-ident is not supplied here and
is flagged for audit adjudication.

## T2 - Equal Weight Equals Equal Energy Under E-ident

Under E-ident with component counting, the equipartition note's invariant
selection

```text
equal registered weight on s and d
```

reads exactly:

```text
3a^2 = 6|b|^2.
```

This is exactly the parent equal-Hilbert-Schmidt-energy condition at `N=3`.
Therefore

```text
r = |b|^2/a^2 = 1/2,
Q = 1/3 + (2/3)(1/2) = 2/3.
```

The fixed-point algebra is exact:

```text
r -> 2r^2,
r = 2r^2,
r(1 - 2r) = 0,
r in {0, 1/2}.
```

So the component dictionary fixed point `r* = 1/2` is exactly the Block01 S1
value, and its `Q` value is exactly `2/3`.

Under slot counting, the same invariant selection is read through the slot
dictionary:

```text
x = r = |b|^2/a^2.
```

Equal registered weight `x = 1` gives exactly:

```text
a^2 = |b|^2,
r = 1,
Q = 1/3 + (2/3)(1) = 1.
```

The fixed-point algebra is exact:

```text
r -> r^2,
r = r^2,
r(1 - r) = 0,
r in {0, 1}.
```

So the slot dictionary fixed point `r* = 1` is exactly the Block01 S2
per-mode value, and its `Q` value is exactly `1`.

## T3 - The Dictionary Residual Is the Scoring Residual

Within the two-dictionary pair of the equipartition note, the correspondence is
one-to-one:

| equipartition dictionary | fixed-point readout | Block01 scoring rule | Block01 value |
|---|---:|---|---:|
| component dictionary `x = 2r` | `r = 1/2` | S1 generator-channel Hilbert-Schmidt | `r = 1/2`, `Q = 2/3` |
| slot dictionary `x = r` | `r = 1` | S2 per-mode basis equipartition | `r = 1`, `Q = 1` |

This is an exact value match, not an analogy. The equipartition note's
dictionary choice is the same finite residual as Block01's S1-vs-S2 scoring
ambiguity: generator-channel/component counting versus per-mode/slot counting.

Therefore Block03's `R*`, which excludes imported-basis/per-mode S2-class
scorings, conditionally selects the component dictionary within the inherited
two-dictionary pair. This selection is conditional on both `R*` and `E-ident`.
It does not exclude S3-class `Y`-dependent partitions in general.

## Hostile Check - S3 Stands Outside the Pair

Block01's third scoring value is:

```text
r = 17/2 - 6 sqrt(2).
```

The equipartition note's two fixed sets contain only:

```text
{0, 1/2} and {0, 1}.
```

Thus the dictionary correspondence covers exactly the two-dictionary pair
`x = 2r` and `x = r`. The S3 value has no corresponding dictionary in that
pair. S3 stands outside this reduction and remains handled by the Block03 and
Block05 sibling logic.

## T4 - Ladder Collapse

Conditional on `{R*, E-ident, the equipartition note's own bounded conditions}`
and with D-totality not needed for this leg, the parent's equal-channel-energy
clause is discharged by the equipartition surface:

1. the conditioned flow supplies equal registered weight on `s` and `d`;
2. E-ident reads that equal registered weight as equal Hilbert-Schmidt channel
   energy;
3. R* selects the component dictionary within the two-dictionary pair;
4. the component branch gives `r = 1/2` and `Q = 2/3` on the S1 partition.

T4 summary: conditional reduction; E-ident and R* are named unadjudicated
premises; the equipartition note's own conditions are inherited, not
discharged.

The campaign ladder therefore reduces from

```text
{R*, D-totality, C2, equal-channel-energy}
```

to

```text
{R*, D-totality, C2, E-ident}.
```

Equal-channel-energy is no longer an independent unknown inside this bounded
leg. It is a consequence of the already-banked equipartition surface plus
E-ident, after R* selects the component dictionary. What remains open is:

- `R*` adjudication;
- `D-totality` adjudication;
- `C2` weighting/readout-context adjudication;
- `E-ident` adjudication;
- the equipartition note's own bounded conditions quoted above;
- all sibling dependency classes and independent audit outcomes.

T4 summary: conditional reduction; E-ident and R* are named unadjudicated
premises; the equipartition note's own conditions are inherited, not
discharged.

## Does NOT Claim

- No unconditional equal-energy theorem is proved.
- E-ident is not derived.
- No wall is closed.
- No probability content, Born rule, observed target value, fitted selector, or
  state-selection content is introduced.
- No occupancy cell or fork branch is selected by the flow alone.
- No audit status is set or predicted.
- S3 is not folded into the two-dictionary correspondence.
- Sibling dependency classes remain unaudited.
- The equipartition note's conditions are inherited verbatim:
  - Does not discriminate either fork branch.
  - Does not select either occupancy cell.
  - Does not fix `r`.
  - Does not correct any landed note.
  - Does not contradict the landed R-D chain.
  - Does not resolve the dictionary.
  - Does not close the occupancy binary; the occupancy binary stays open.

## Load-Bearing Inputs

| path | role | dependency class |
|---|---|---|
| [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md) | Supplies the bounded equipartition surface, the two dictionaries, the dictionary-as-atom paragraph, the tri-guise identity, and inherited boundary/Does-NOT conditions. | bounded theorem; inherited conditions not discharged here |
| [`FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md`](FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md) | Supplies S1/S2/S3 scoring values, `Q` values, and the S1-vs-S2 residual shape. | landed bounded sibling; independent audit-owned |
| [`C1_FRAME_COMPONENT_FROM_RECORD_REGISTRABILITY_PARTIAL_BOUNDED_NOTE_2026-07-02.md`](C1_FRAME_COMPONENT_FROM_RECORD_REGISTRABILITY_PARTIAL_BOUNDED_NOTE_2026-07-02.md) | Supplies `R*`, the S2-class imported-basis exclusion, and S1 compatibility. | landed bounded sibling; independent audit-owned; conditional on R* |
| [`FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md`](FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md) | Supplies the parent equal-Hilbert-Schmidt-energy clause and the carrier-measure residual. | parent boundary note; equal-energy clause was open before this conditional reduction |

## Paired Runner

Paired runner:

[`scripts/frontier_equal_channel_energy_equipartition_reduction_2026_07_02.py`](../scripts/frontier_equal_channel_energy_equipartition_reduction_2026_07_02.py)

Cached run:

[`logs/runner-cache/frontier_equal_channel_energy_equipartition_reduction_2026_07_02.txt`](../logs/runner-cache/frontier_equal_channel_energy_equipartition_reduction_2026_07_02.txt)

Expected terminal line:

```text
TOTAL: PASS=16 FAIL=0
```
