# Generation Record Arrow Measure Selector

**Date:** 2026-06-05
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note does not set, predict, or propose an
audit outcome.
**Primary runner:** [`scripts/generation_record_arrow_measure_selector_2026_06_05.py`](../scripts/generation_record_arrow_measure_selector_2026_06_05.py)
(sympy exact algebra; **SCORECARD 21 PASS / 0 FAIL**).
**Cached log:** [`logs/runner-cache/generation_record_arrow_measure_selector_2026_06_05.txt`](../logs/runner-cache/generation_record_arrow_measure_selector_2026_06_05.txt).

## Scope and honesty

This note attacks the remaining arrow/measure gate after the Record reset.

Given the generation two-sector Record alphabet:

```text
singlet letter       dimension 1
faithful doublet     dimension 2
```

the measure/arrow choice can be represented by a one-parameter prior

```text
pi_gamma(letter) proportional to dim(letter)^gamma.
```

Then:

```text
gamma=0  -> equal record-letter / block-count prior
gamma=1  -> dimension / Born prior
```

The theorem proves that relative-entropy ascent toward `pi_gamma` stabilizes
the exact generation dial at

```text
s = gamma.
```

Therefore:

```text
gamma=0 -> s=0 -> r=1/2 -> Q=2/3
gamma=1 -> s=1 -> r=1   -> Q=1
```

This is a positive classifier, not a physical value derivation. It does **not**
derive that charged leptons choose `gamma=0`. It isolates that as the remaining
arrow/measure premise:

```text
charged-lepton record dynamics uses record-letter/block-count prior rather
than dimension/Born prior.
```

## Inputs

- [`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md):
  the supplied generation readout context has two K/CPT-orbit sectors, with
  dimensions `1` and `2`.
- [`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05`](GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md):
  the exact dial is `r(s)=2^(s-1)`, with block-count endpoint `s=0` and
  dimension/Born endpoint `s=1`.
- [`KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05`](KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md):
  the Koide observable on the circulant generation carrier is
  `Q=1/3+(2/3)r`.

Related no-go context:

- [`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`](FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md):
  objectivity fixes the record basis/alphabet, not the weights.
- [`FLAVOR_TRACIAL_REFERENCE_DOES_NOT_SELECT_Q23_NO_GO_NOTE_2026-06-02`](FLAVOR_TRACIAL_REFERENCE_DOES_NOT_SELECT_Q23_NO_GO_NOTE_2026-06-02.md):
  the tracial/Born route gives dimension weights and lands at `Q=1`, not
  `Q=2/3`.

This note preserves both no-go boundaries. It supplies the exact arrow grammar
that explains how each prior stabilizes its endpoint.

## Dial coordinates

Let the two record letters have positive readouts

```text
w0 = singlet readout
w1 = doublet readout.
```

Define the sector ratio

```text
rho = w1/w0 = 2^s.
```

For the generation circulant power ratio,

```text
r = |b|^2/a^2 = rho/2 = 2^(s-1).
```

Therefore

```text
Q(s) = 1/3 + (2/3) 2^(s-1).
```

The endpoints are:

```text
s=0 -> rho=1 -> r=1/2 -> Q=2/3
s=1 -> rho=2 -> r=1   -> Q=1.
```

## Theorem

For the two-letter alphabet with dimensions `(1,2)`, define a prior

```text
pi_gamma = (1, 2^gamma)/(1+2^gamma).
```

The record-letter distribution at dial coordinate `s` is

```text
p(s) = (1, 2^s)/(1+2^s).
```

Use the relative-entropy arrow

```text
maximize  -D_KL(p(s) || pi_gamma).
```

The runner verifies the exact derivative

```text
d/ds[-D_KL] =
  -(s-gamma) (log 2)^2 2^s / (1+2^s)^2.
```

Thus the unique stationary point is

```text
s = gamma,
```

with negative curvature

```text
-(log 2)^2 2^gamma / (1+2^gamma)^2 < 0.
```

So relative-entropy ascent toward the supplied `dim^gamma` prior stabilizes

```text
s* = gamma,
r* = 2^(gamma-1),
Q* = 1/3 + (2/3) 2^(gamma-1).
```

## Endpoint meanings

### `gamma=0`: record-letter / block-count arrow

The prior is

```text
pi_0 = (1/2, 1/2).
```

This treats the two durable Record letters equally. The stable point is

```text
s=0, rho=1, r=1/2, Q=2/3.
```

This is the Koide setting as a stable equilibrium of the equal-record-letter
arrow.

### `gamma=1`: dimension / Born arrow

The prior is

```text
pi_1 = (1/3, 2/3).
```

This weights the two letters by their Hilbert/real dimensions `(1,2)`. The
stable point is

```text
s=1, rho=2, r=1, Q=1.
```

This is the tracial/Born endpoint.

## Discrete relaxation form

The same selector can be written as a one-step relaxation map

```text
s' = s + lambda(gamma-s).
```

It fixes `s=gamma` and has multiplier

```text
1-lambda.
```

For example, half-step relaxation has multiplier `1/2` and stabilizes either
endpoint depending on the supplied prior:

```text
gamma=0 -> s' = s/2
gamma=1 -> s' = (s+1)/2.
```

Again, stability follows from the supplied prior. The physical prior is not
derived by this theorem.

## What this unlocks

This note makes the remaining gate exact:

```text
gamma = 0  versus  gamma = 1.
```

The prior blocks can now be staged as:

1. **Partition gate:** the native Record alphabet is the singlet/doublet
   two-letter alphabet.
2. **Arrow/measure gate:** choose the prior on that alphabet.
3. **Dynamics result:** entropy/relative-entropy ascent stabilizes the dial at
   the prior's `gamma`.

The partition and dynamics algebra are now finite and auditable. The only
remaining physics premise for charged-lepton `Q=2/3` is:

```text
the charged-lepton record arrow is record-letter/block-counting (`gamma=0`),
not dimension/Born (`gamma=1`).
```

## What this does not close

- It does not derive the physical charged-lepton prior.
- It does not refute the Born/dimension endpoint; it classifies it as
  `gamma=1`.
- It does not derive Born probability from Record.
- It does not supply a source/action or time metric.
- It does not promote the charged-lepton Koide value beyond bounded support.

## Runner coverage

The runner verifies:

- `rho=2^s`, `r=rho/2=2^(s-1)`, and `Q(s)`;
- `gamma=0` prior is equal record-letter/block-count weighting;
- `gamma=1` prior is dimension/Born weighting;
- the relative-entropy derivative and negative curvature at `s=gamma`;
- endpoint consequences for `Q=2/3` and `Q=1`;
- gradient-flow signs around both endpoints;
- discrete relaxation map fixed point and multiplier;
- the firewall: both `gamma=0` and `gamma=1` are valid supplied stable arrows,
  so the theorem leaves physical `gamma` selection open.

## Net

This is the clean arrow/measure result: once the Record alphabet is two letters,
the stable dial point is exactly the prior exponent `gamma`. Koide is the
stable point of the record-letter prior; Born is the stable point of the
dimension prior. The next unresolved physics question is why charged-lepton
record dynamics should use the former rather than the latter.
