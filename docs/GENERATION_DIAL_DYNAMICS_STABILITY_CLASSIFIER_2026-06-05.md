# Generation Dial Dynamics Stability Classifier

**Date:** 2026-06-05
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note does not set, predict, or propose an
audit outcome.
**Primary runner:** [`scripts/generation_dial_dynamics_stability_classifier_2026_06_05.py`](../scripts/generation_dial_dynamics_stability_classifier_2026_06_05.py)
(sympy + finite map checks; **SCORECARD 26 PASS / 0 FAIL**).
**Cached log:** [`logs/runner-cache/generation_dial_dynamics_stability_classifier_2026_06_05.txt`](../logs/runner-cache/generation_dial_dynamics_stability_classifier_2026_06_05.txt).

## Scope and honesty

This note implements the dynamics reframing that the charged-lepton/generation
lane now needs:

```text
Dynamics does not need to force Koide.
Dynamics should classify stable settings on the exact generation dial.
```

The exact dial is imported from
[`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05`](GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md):

```text
r(s) = 2^(s-1),        Q(s) = 1/3 + (2/3) r(s).
```

Thus:

```text
s=0  <=>  r=1/2  <=>  Q=2/3   (block-count / two-sector balanced setting)
s=1  <=>  r=1    <=>  Q=1     (Born/dimension / real-mode balanced setting)
```

Two sibling scaffold notes isolate the reusable parts:

- [`RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05`](RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md)
  gives finite additive readout-vector algebra from Record, without promoting
  it to probability or dynamics.
- [`GENERATION_DIAL_LOCAL_STABILITY_GRAMMAR_2026-06-05`](GENERATION_DIAL_LOCAL_STABILITY_GRAMMAR_2026-06-05.md)
  gives the local map/flow stability grammar on the positive ratio dial.

The contribution here is not value selection. It is a classifier for dynamics
classes on this dial:

- two-sector entropy ascent stabilizes `s=0`;
- the supplied reverse/thermalizing branch `r -> sqrt(r/2)` stabilizes `s=0`;
- Lueders/record sharpening `r -> 2r^2` makes `s=0` repelling;
- real-mode entropy ascent stabilizes `s=1`;
- the supplied heat-kernel path `r(t)=tanh(t)^4` crosses `s=0` as a transit,
  not as an attractor.

Therefore `Q=2/3` is an exact stable setting for named dynamics classes, but it
is not forced by Lattice, Quantum, and Record alone. The remaining physical gate
is the selection of the record partition and arrow/functional.

## Adopted inputs

- **Record axiom.** Given a supplied finite central-sector decomposition and
  fixed `K`/CPT conjugation, the record names the realized `K`/CPT orbit and the
  scalar readout `I` is finitely additive over disjoint records. Record does not
  supply probability, Born weights, a time metric, a source/action, decoherence,
  or dynamics.
- **Two-sector generation readout.** Imported from
  [`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md):
  singlet sector real dimension `1`, faithful doublet sector real dimension
  `2`.
- **Exact Koide/dial algebra.** Imported from
  [`KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05`](KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md)
  and
  [`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05`](GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md):
  `Q=1/3+(2/3)r` and `r(s)=2^(s-1)`.

No physical evolution law is imported as established. Each map or entropy
functional below is a supplied dynamics class whose stability properties are
checked exactly.

## Theorem: stability classifier on the exact dial

Let `s` be the exact generation-dial coordinate, `r(s)=2^(s-1)`.

### 1. Two-sector entropy stabilizes `s=0`

On the two-record-sector simplex, the normalized sector fractions are

```text
p0(s) = 1/(1+2^s),          p1(s) = 2^s/(1+2^s).
```

The two-sector entropy

```text
S2(s) = -p0 log p0 - p1 log p1
```

has derivative

```text
dS2/ds = -s (log 2)^2 2^s / (1+2^s)^2.
```

Hence `s=0` is the unique stationary point and

```text
S2''(0) = -(log 2)^2/4 < 0.
```

So the continuous flow `ds/dtau = dS2/ds` stabilizes `s=0`. In the generation
dial this is exactly

```text
s=0 <=> r=1/2 <=> Q=2/3.
```

Interpretation: if the physical record arrow is an entropy-increasing flow on
the two-isotype-sector partition, the Koide setting is a stable equilibrium on
the dial.

### 2. Real-mode entropy stabilizes `s=1`

On the three resolved real modes, the normalized fractions are

```text
[1, r, r] / (1+2r)
    =
[1/(1+2^s), 2^s/(2(1+2^s)), 2^s/(2(1+2^s))].
```

The real-mode entropy `S3` has derivative

```text
dS3/ds = (log 2) 2^s log(2/2^s) / (1+2^s)^2,
```

so its stationary point is `s=1`, with

```text
S3''(1) = -2 (log 2)^2/9 < 0.
```

Thus real-mode entropy ascent stabilizes the Born/dimension endpoint `s=1`,
not the Koide setting `s=0`. This is the same distinction as block-count
(`det_C`) versus dimension/Born (`det_R`) weighting.

### 3. Lueders sharpening repels `s=0`

The earlier record-sharpening map

```text
r' = 2r^2
```

becomes, in the exact `s` coordinate,

```text
s' = 2s.
```

It fixes `s=0` but has multiplier `2`, so `s=0` is repelling. This does not
contradict the stable-setting claim above; it says sharpening is the wrong
arrow if the target is stabilization at the two-sector balanced point.

### 4. Reverse branch stabilizes `s=0`

The supplied reverse/thermalizing branch

```text
r' = sqrt(r/2)
```

becomes

```text
s' = s/2.
```

It fixes `s=0` with multiplier `1/2`, so `s=0` is stable. This is the cleanest
map-level expression of the user's point: Koide need only be a stable setting
on the dial, not a universally forced endpoint.

### 5. Heat-kernel transit is not attraction

The supplied path

```text
r(t) = tanh(t)^4
```

crosses `r=1/2` at

```text
t = atanh(2^(-1/4)),
```

and the crossing derivative is positive:

```text
dr/dt = 2^(1/4) (2 - sqrt(2)) > 0.
```

So this path supplies a transit through the Koide setting, not an attracting
selection of it.

## Dynamics proposal for the framework

The dynamics push should avoid a new "force Koide" target. The more audit-safe
target is:

```text
Build retained dynamics as record-function stability/admissibility results.
```

Concretely:

1. **Use record functions, not hidden probability.** For a supplied finite
   record decomposition, let the record function be the finite vector of
   additive scalar readouts on record sectors. Ratios like `r` and dial
   coordinates like `s` are valid structural observables. Calling them
   probabilities requires a separate Born/normalization gate.
2. **Classify dynamics by partition and arrow.** The same dial has different
   stable settings depending on the chosen coarse-graining and entropy
   functional: two-sector entropy selects `s=0`; real-mode entropy selects
   `s=1`; sharpening repels `s=0`; the reverse branch attracts it.
3. **Make the physical gate explicit.** The open charged-lepton question is
   not "derive `Q=2/3` from nothing." It is: derive why the charged-lepton
   record uses the two-isotype-sector partition and an entropy-increasing
   arrow in that partition.
4. **Promote only classifier facts until the gate closes.** Exact algebra,
   finite-sector additivity, dial identities, and local stability classifications
   are candidates for bounded or retained theorem rows after audit. Physical
   value selection remains bounded until a native arrow/partition derivation
   exists.
5. **Use dynamics to sort the backlog.** Old rows that tried to force a value
   should be rewritten as one of:
   `stable under two-sector entropy`, `repelling under sharpening`,
   `Born/dimension endpoint`, `transit path`, or `requires source/action gate`.

This lets the Record axiom unlock the repo without laundering dynamics through
Record. Record supplies additive finite readout. Dynamics then says which
record-function settings are stable under which admissible arrows.

## Retained-unbounded route

The plausible retained-unbounded path is not a single giant dynamics axiom. It
is a sequence of small rows whose conclusions remain true without supplied
numerical inputs:

1. **Record-function algebra:** finite record readouts form additive sector
   vectors; ratios and normalized coordinates are structural observables when
   denominators are nonzero.
2. **Dial geometry:** the generation weight dial is exact and monotone,
   `r(s)=2^(s-1)`, with named endpoints `s=0` and `s=1`.
3. **Local stability grammar:** for a map `s' = F(s)`, a fixed setting is stable
   when `|F'(s*)|<1`; for a flow `ds/dtau=f(s)`, it is stable when
   `f'(s*)<0`.
4. **Partition-specific entropy theorems:** two-sector entropy ascent
   stabilizes `s=0`; real-mode entropy ascent stabilizes `s=1`.
5. **No-laundering wall:** choosing which partition and arrow is physical is a
   separate theorem or axiom candidate, not an implication of Record.

Rows 1 and 3 are now split into sibling scaffold artifacts; rows 2 and 4 are
covered here and in the generation weight-dial note. Row 5 prevents
overpromotion. The charged-lepton `Q=2/3` identification should stay bounded to
the two-sector entropy/arrow gate until that gate is proven natively.

## Runner coverage

The runner verifies:

- exact dial endpoints and `Q(s)`;
- two-sector probabilities, entropy derivative, stationary point, and negative
  curvature at `s=0`;
- real-mode probabilities, entropy derivative, stationary point, and negative
  curvature at `s=1`;
- exact coordinate transforms `r->2r^2` gives `s' = 2s`, and
  `r->sqrt(r/2)` gives `s' = s/2`;
- finite local-map classifier: stable, repelling, neutral;
- reverse-map contraction and sharpening-map expansion under iteration;
- heat-kernel crossing is monotone transit;
- generic continuous-flow stability grammar.

## Net

The dynamics program should treat `Q=2/3` as a stable balanced setting on a
record-function dial, not as a value forced by the minimal axioms. That is the
right target after the Record axiom: retained algebra and stability classifiers
first; physical arrow/partition selection only when the repo has an actual
native derivation.
