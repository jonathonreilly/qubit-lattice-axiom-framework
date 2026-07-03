# E-ident Decomposes: Definitional Proportionality, Dictionary Choice, and CTX-match

**Date:** 2026-07-02
**Type:** bounded support (decomposition + exact discharge)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Boundary:** conditional decomposition. `R*`, `D-totality`, `C2`, and
`CTX-match` remain unadjudicated; the equipartition note's inherited conditions
remain inherited.
**Primary runner:** [`scripts/frontier_eident_decomposition_ctx_match_2026_07_02.py`](../scripts/frontier_eident_decomposition_ctx_match_2026_07_02.py)
**Runner output:** [`logs/runner-cache/frontier_eident_decomposition_ctx_match_2026_07_02.txt`](../logs/runner-cache/frontier_eident_decomposition_ctx_match_2026_07_02.txt)

## Purpose

Block06 named `E-ident` as the premise identifying the equipartition note's
registered cells `{s, d}` with the carrier-measure generator channels
`{unit I, doublet complement B}`. This note decomposes that premise.

The result is:

```text
E-ident = component-dictionary stipulation + dictionary choice + CTX-match.
```

The first item is definitional on the equipartition note's own supplied
surface. The second item is the already-isolated `R*` dictionary/scoring
residual. The remaining nontrivial residue is `CTX-match`: the assertion that
the two supplied surfaces are the same `C_3` readout context, not merely two
isomorphic singlet/doublet bookkeepings.

## Supplied Surface Anchors

The equipartition note's supplied Record wording is:

```text
"Given a readout context with a finite central-sector decomposition and a fixed
`K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized
central sector."
```

It then states the registered outcomes:

```text
On the supplied surface, the two registered outcomes are the singlet outcome
`s` and the doublet `K`-orbit outcome `d`.
```

The agreement-conditioned update is:

```text
x' = (p_d^2/Z)/(p_s^2/Z) = (p_d/p_s)^2 = x^2.
```

The two stipulated dictionaries are:

```text
- Component dictionary `(1,2)`: `x = 2r`. The doublet outcome carries two
  components, so `p_d = 2|b|^2` and `p_s = a^2`.
- Slot dictionary `(1,1)`: `x = r`. There is one slot per outcome at equal
  per-slot weight.
```

The Block01 carrier-measure surface supplies the `hw=1` generation model:

````text
The generation factor is the `hw=1` subspace, identified here with `C^3` on the
one-site framework surface. Let `U` be the cyclic shift. The supplied circulant
Yukawa form is

```text
Y = a I + b U + conj(b) U^{-1}.
```
````

It also quotes the generator-channel Hilbert-Schmidt setup:

````text
Let `J_N` be the all-ones matrix and let

```text
B_N = J_N - I_N.
```

In the Hilbert-Schmidt form,

```text
||I_N||^2 = N,        ||B_N||^2 = N(N-1),        <I_N, B_N> = 0.
```
````

Block06 records the `N=3` specialization:

```text
||I||^2 = 3,        ||B||^2 = 6.
```

## T1 - Exact Proportionality

Under the component dictionary's stipulated weights,

```text
(p_s, p_d) = (a^2, 2|b|^2).
```

Under Block01's channel Hilbert-Schmidt energies at `N=3`,

```text
(E_I, E_B) = (3a^2, 6|b|^2).
```

Therefore the two pairs are exactly proportional:

```text
(E_I, E_B) = 3 (p_s, p_d).
```

So

```text
p_s = p_d
iff 3p_s = 3p_d
iff E_I = E_B.
```

Equal registered weight is equal channel energy up to the single overall
normalization `N = 3`, by the dictionary's own stipulation. This is pure exact
algebra. No probability rule, Born rule, physical selector, or new weighting
principle is used.

What would break this discharge: if the equipartition note supplied
`p_s, p_d` as anything other than `p_s = a^2` and `p_d = 2|b|^2`, the
proportionality would no longer be definitional. It does not do that; the
component dictionary quote above is the load-bearing sentence.

## T2 - E-ident Decomposition

Block06 states `E-ident` as:

```text
**Premise E-ident.** On the `C_3` generation surface, the two generator
channels `{unit I, doublet complement B}` correspond to the equipartition
note's two cells `{s (singlet), d (doublet)}` as follows:

- the singlet cell `s` carries the unit-channel registered weight, proportional
  to `N a^2`;
- the doublet cell `d` carries the complement-channel registered weight,
  proportional to `N(N-1)|b|^2`.
```

This decomposes into three parts.

1. **Component-dictionary stipulation.** The equipartition note itself
   stipulates `p_s = a^2` and `p_d = 2|b|^2` under the component dictionary.
   T1 shows that this is exactly proportional to `(3a^2, 6|b|^2)`.

2. **Dictionary choice.** The choice between the component dictionary
   `x = 2r` and the slot dictionary `x = r` is the same residual Block06 T3
   identified with the S1-vs-S2 scoring residual:

   ```text
   The equipartition note's dictionary choice is the same finite residual as Block01's S1-vs-S2 scoring
   ambiguity: generator-channel/component counting versus per-mode/slot counting.
   ```

   Block06 then says `R*` conditionally selects the component dictionary within
   that inherited two-dictionary pair. This note does not adjudicate `R*`.

3. **CTX-match.** The remaining premise is that the equipartition note's
   supplied finite central-sector readout context with cells `{s, d}` and the
   carrier-measure `hw=1` surface with channels `{I, B}` are the same supplied
   `C_3` readout context.

Side by side, the shared formal shape is:

| equipartition surface | carrier-measure surface |
|---|---|
| "Given a readout context with a finite central-sector decomposition and a fixed `K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized central sector." | "The generation factor is the `hw=1` subspace, identified here with `C^3` on the one-site framework surface. Let `U` be the cyclic shift." |
| "the two registered outcomes are the singlet outcome `s` and the doublet `K`-orbit outcome `d`" | `B_N = J_N - I_N`, with `||I_N||^2 = N` and `||B_N||^2 = N(N-1)` |
| component dictionary: `p_s = a^2`, `p_d = 2|b|^2` | at `N=3`: `||I||^2 = 3`, `||B||^2 = 6` |

`CTX-match` asserts more than these quotes share. It asserts that:

- the equipartition central-sector cells and the carrier-measure
  unit/complement cells are cells of one and the same supplied `C_3` readout
  context;
- `s` is the unit-channel cell and `d` is the doublet-complement channel cell;
- the match is not merely an isomorphism of two independent two-cell diagrams.

What would break `CTX-match`: if the two supplied surfaces used different
circulant classes or different `C_3` readout contexts, the algebraic
proportionality in T1 would still be true inside the component dictionary, but
it would not identify the equipartition cells with the carrier-measure
channels. The textual floor in the three read notes is the shared `C_3`
singlet/doublet language plus Block01's supplied circulant form
`Y = a I + b U + conj(b) U^{-1}`. That floor supports the residual question; it
does not by itself derive the context identity.

## T3 - Ladder Update

Given T1 and T2, `E-ident` adds no adjudication content beyond `{R*,
CTX-match}` once the equipartition note's own component-dictionary stipulation
is carried as definitional.

The campaign ladder updates from:

```text
{R*, D-totality, C2, E-ident}
```

to:

```text
{R*, D-totality, C2, CTX-match}
```

`CTX-match` is strictly weaker than `E-ident`. `E-ident` included both a
weight reading and a channel/cell correspondence. T1 removes the weight reading
as exact proportionality under the stipulated component dictionary, and
Block06 T3 assigns the component-vs-slot choice to `R*`. What remains in
`CTX-match` is only the context-matching/bookkeeping identification: the
assertion that the `s/d` outcome cells and the `I/B` channel cells are the same
singlet/doublet split on the same supplied surface.

T3 summary: conditional decomposition; R*, D-totality, C2, CTX-match remain unadjudicated; the equipartition note's conditions remain inherited.

## T4 - Pre-reset Disclosure and Merge Candidate

The equipartition note quotes the pre-reset Record wording:

```text
"Given a readout context with a finite central-sector decomposition and a fixed
`K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized
central sector."
```

This note does not read or use the current `MINIMAL_AXIOMS`. It carries only
the disclosure requested for this block: the 2026-06-29 reset moved
`K`/CPT-orbit outcome content to downstream readout-context content. From the
equipartition note's own quoted wording and Block06's inherited-conditions
list, the present decomposition must therefore be understood as living inside
the supplied-readout-context adjudication family, the same family as `C1/C2`.

Candidate only: a future note may merge `CTX-match` into the `C2` or broader
readout-context supplier specification. This note does not perform that merge.

## Does NOT Claim

- `CTX-match` is not derived.
- No wall is closed.
- Dictionary choice is not adjudicated here; that is `R*`.
- No probability content, Born rule, observed value, fitted selector, or state
  selector is introduced.
- The equipartition note's inherited conditions remain inherited.
- The pre-reset wording caveat is carried, not resolved.
- No new axiom, primitive, normalization, dictionary, or occupancy cell is
  introduced.
- No audit status is set or predicted.

## Load-Bearing Inputs

| path | role | dependency class |
|---|---|---|
| [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md) | Supplies the pre-reset supplied-surface wording, the `s/d` outcome cells, the squaring update, and the component/slot dictionary stipulations. | bounded theorem; inherited conditions not discharged here |
| [`EQUAL_CHANNEL_ENERGY_REDUCES_TO_EQUIPARTITION_SURFACE_DICTIONARY_RESIDUAL_BOUNDED_NOTE_2026-07-02.md`](EQUAL_CHANNEL_ENERGY_REDUCES_TO_EQUIPARTITION_SURFACE_DICTIONARY_RESIDUAL_BOUNDED_NOTE_2026-07-02.md) | Supplies the prior `E-ident` premise and the dictionary-to-scoring residual correspondence. | landed bounded sibling; independent audit-owned; conditional on `E-ident` and `R*` |
| [`FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md`](FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md) | Supplies the `hw=1` carrier-measure surface, the supplied circulant form, the generator-channel Hilbert-Schmidt norms, and the S1/S2 scoring values. | landed bounded sibling; independent audit-owned |

## Paired Runner

Paired runner:

[`scripts/frontier_eident_decomposition_ctx_match_2026_07_02.py`](../scripts/frontier_eident_decomposition_ctx_match_2026_07_02.py)

Cached run:

[`logs/runner-cache/frontier_eident_decomposition_ctx_match_2026_07_02.txt`](../logs/runner-cache/frontier_eident_decomposition_ctx_match_2026_07_02.txt)

Expected terminal line:

```text
TOTAL: PASS=17 FAIL=0
```
