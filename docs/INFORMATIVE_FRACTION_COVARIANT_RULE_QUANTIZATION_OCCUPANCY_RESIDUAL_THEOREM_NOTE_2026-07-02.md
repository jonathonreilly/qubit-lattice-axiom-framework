# Informative-Step Fraction: Covariant-Rule Quantization and the Occupancy Residual

**Date:** 2026-07-02

**Claim type:** bounded_theorem

**Audit status:** set only by the independent audit lane. This source note does not set, predict, or apply an audit verdict.

**Primary runner:** [`scripts/informative_fraction_covariant_rule_quantization_occupancy_residual_2026_07_02.py`](../scripts/informative_fraction_covariant_rule_quantization_occupancy_residual_2026_07_02.py)

## Purpose

This note asks what the Admissibility axiom's structure implies about the informative-step fraction `p`.

The rule fence is:

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."

It fixes the covariance class of the rule, not the selected rule. The available-subset fence is quoted in the current source wording:

> "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions."

It supplies nearest-neighbor dependence, not a probability measure. The no-weights fence says Admissibility does not supply:

> "transition probabilities or weights"

The bounded answer is: in the recorded-neighborhood baseline, the covariant rule space is finite and exactly classified; under the iid-uniform no-information occupancy baseline, `p` is quantized as `k/64`; the unit-variance point `p*` is off-lattice; and the remaining mismatch is an occupancy residual, quantified by an iid-density deformation.

Neighboring surfaces are named only for orientation: `GAUGE_LINK_BINARY_REGISTRATION_CAPACITY_STEP_KERNEL_PIN_THEOREM_NOTE_2026-07-02.md` - not a citation-graph dependency; `NATIVE_CARRIER_REGISTRATION_KERNEL_RATE_VS_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md` - not a citation-graph dependency; `GAUGE_LINK_PER_RECORD_STEP_RATE_DIAL_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md` - not a citation-graph dependency. The runner recomputes `p*` in-packet from the Haar integral.

## Supplied surfaces (cited at audited scope)

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the covariance clause, available-subset clause, and no-weights clause quoted in the theorems.
- [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md) supplies canonical normalization and the zero-sum logarithm-branch surface for the in-packet `p*` recomputation.
- [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md) is respected: this note makes no dynamics or stationary-measure existence claim.

## The recorded-neighborhood baseline model

The recorded-neighborhood baseline is a named model. The six nearest neighbors are ordered as `+x`, `-x`, `+y`, `-y`, `+z`, `-z`; each carries a binary locked record, so a local neighbor pattern is a word in `{0,1}^6`.

The site's available subset is one of `empty`, `{0}`, `{1}`, `{0,1}`. The informative available subset is `{0,1}`. A rule in this baseline is an orbit-map from binary neighbor patterns to those four available subsets.

Translation covariance removes site labels. Proper cubic rotation covariance makes the rule constant on proper-rotation orbits of the six neighbor slots.

The iid-uniform no-information occupancy baseline is a named model in which each binary recorded-neighbor pattern has probability `1/64`. It is motivated by the no-weights fence, but not derived from the axiom. The iid-density deformation is the one-parameter model in which each neighbor independently carries value `1` with density `q` and value `0` with density `1-q`. That deformation locates the occupancy residual; it does not select a physical `q`.

## Theorem 1 (finite covariant classification)

The covariance clause makes the recorded-neighborhood rule space finite. The proper cubic rotation group has 24 elements, inducing 24 distinct permutations of the six directed neighbor slots.

The 64 binary neighbor patterns split into exactly 10 orbits, with sorted sizes:

```text
[1, 1, 3, 3, 6, 6, 8, 12, 12, 12]
```

The sizes sum to `64`; each orbit has a single Hamming weight. The inventory is:

| size | weight | description |
|---:|---:|---|
| 1 | 0 | empty |
| 6 | 1 | single occupied neighbor |
| 3 | 2 | antipodal pair |
| 12 | 2 | adjacent pair |
| 8 | 3 | octant triple |
| 12 | 3 | axial triple |
| 3 | 4 | complement of antipodal pair |
| 12 | 4 | complement of adjacent pair |
| 6 | 5 | single vacancy |
| 1 | 6 | full |

The Burnside cross-check is exact:

```text
(1/24) sum_g 2^cycles(g) = 10
```

Thus a covariant rule in this model is a map from the 10 orbits to `empty`, `{0}`, `{1}`, or `{0,1}`. This classifies the rule space; it does not select a rule.

## Theorem 2 (quantization under the no-information baseline)

Under iid uniform recorded neighbors, each binary pattern has mass `1/64`. If `k` is the total size of the orbits assigned the informative subset `{0,1}`, then:

```text
p(rule) = k/64
```

The runner enumerates all subset sums of the 10 orbit sizes. Every `k` in `{0,...,64}` is attainable, so:

```text
p in {k/64 : 0 <= k <= 64}
```

The informative fraction is quantized by covariance in this named baseline.

The optional value-flip-covariant refinement identifies a pattern with its global `0<->1` complement. It is not axiom-required. The combined orbit sizes are:

```text
[2, 6, 8, 12, 12, 24]
```

The attainable values are even only. In particular, `26` is attainable, `27` is not attainable, and `28` is attainable.

## Theorem 3 (the unit point is off-lattice)

The runner recomputes the unit-variance point from the Haar integral using the `M = 1600` centered Weyl grid, closed trigonometric Haar density, and zero-sum minimal branch for the principal phases.

```text
<1>_Haar = 1
<s2_min>_Haar = 9.466227112322
p* = 4 / (<s2_min>_Haar + 8/27) = 0.409730132
```

Displayed to theorem-chain precision, `p* = 0.409731`. The incommensurability gate is:

```text
64 p* = 26.222728
```

The distance from the nearest integer is greater than `0.2`. Therefore no covariant rule under the recorded-neighborhood iid-uniform baseline attains the unit-variance point exactly.

The nearest rotation-covariant brackets are:

```text
26/64 = 0.406250
p*    = 0.409730
27/64 = 0.421875
```

The signed gaps are `26/64 - p* = -0.003480132` and `27/64 - p* = +0.012144868`, about `-0.35` and `+1.2` percentage points. With optional value-flip covariance, the brackets are `26/64` and `28/64 = 0.437500`, giving the stated upper gap of about `+2.8` percentage points.

This negative statement is scoped to the named recorded-neighborhood model, iid-uniform baseline, and informative-step reading.

## Theorem 4 (the occupancy residual, located)

Under the iid-density deformation, an orbit of size `s` and weight `w` contributes:

```text
s q^w (1-q)^(6-w)
```

when assigned informative.

The first exhibited rule is:

```text
R26 informative orbits:
  (1,0) empty
  (12,2) adjacent pair
  (12,3) axial triple
  (1,6) full
p_R26(q) = 1 - 6q + 27q^2 - 56q^3 + 51q^4 - 18q^5 + 2q^6
p_R26(1/2) = 26/64
q* = 0.495326251
q* = 0.851530513
```

The second exhibited rule is:

```text
R27 informative orbits:
  (3,2) antipodal pair
  (12,2) adjacent pair
  (12,3) axial triple
p_R27(q) = 15q^2 - 48q^3 + 54q^4 - 24q^5 + 3q^6
p_R27(1/2) = 27/64
q* = 0.276026205
q* = 0.512443603
```

The runner gates sign changes before bisection. Each displayed root is interior to `(0,1)`, reproduces `p*` within `1e-8`, and differs from the uniform baseline `q = 1/2` by at least `1e-3`.

The residual between the axiom-quantized baseline and the unit point is therefore exactly an occupancy-statistics datum in the framework's recognized occupancy/readout admission territory. It is quantified as a fraction-of-a-pattern deviation from uniform neighbor statistics. Nothing selects a rule or a `q`; the dial remains registered, and `p*` and `q*` are located, never forced.

## Boundary

- This note does not derive the admissibility rule. The axiom fixes the covariance class of the rule, quoted above, not the selected rule.
- This note does not derive occupancy statistics or any value of `q`. The no-weights clause is quoted above, and the iid models are named baselines or deformations.
- This note does not claim: the recorded-neighborhood model is the unique reading. Partially-recorded neighborhoods remain an open refinement.
- This note does not claim: it derives `p` or `p*`; the runner locates `p*` and classifies attainable baseline `p` values.
- This note does not claim: the Theorem 3 negative statement holds outside the named baseline, named model, and named reading.
- This note does not claim: a record step occurs. The semigroup boundary is respected.
- This note does not claim: an audit verdict or any effective-status promotion.

Forward surface: derive correlated non-iid occupancy statistics from record-formation dynamics; refine partially-recorded neighborhoods with fewer than six recorded neighbors; treat composite carriers.

## Falsifiers

The runner is deterministic, uses `numpy`, `fractions`, `itertools`, and `pathlib`, and mirrors the theorem chain.

Section A falsifiers:

- proper cubic rotation count is not `24`
- closure or inverse checks fail
- six-slot action does not have `24` distinct proper permutations
- orbit count is not `10`
- sorted orbit sizes differ from `[1, 1, 3, 3, 6, 6, 8, 12, 12, 12]`
- an orbit mixes Hamming weights, the inventory differs from the table, the Burnside count differs from `10`, inversion appears in the proper slot action, or the value-flip orbit sizes differ from `[2, 6, 8, 12, 12, 24]`

Section B falsifiers:

- subset sums of the 10 proper-rotation orbit sizes miss any `k` in `{0,...,64}`
- a value-flip attainable value is odd
- `26`, `27`, and `28` do not have the stated value-flip attainability pattern

Section C falsifiers:

- Haar density mean differs from `1` by more than `1e-9`
- `<s2_min>_Haar` differs from `9.466227112` by more than `1e-8`
- `p*` differs from `0.409731` by more than `5e-6`
- `64 p*` lies within `0.2` of an integer
- `p*` is not bracketed by `26/64` and `27/64`

Section D falsifiers:

- either fixed polynomial fails its exact `q = 1/2` value
- neither exhibited rule has an interior sign-change root
- a found root lies outside `(0,1)`, misses `p*` by `1e-8` or more, or equals the uniform baseline within `1e-3`

Section F source-boundary guards:

- files must exist for this note, the runner, and the three supplied dependency notes
- the axioms dependency must contain the covariance clause
- the axioms dependency must contain the current available-subset clause
- the axioms dependency must contain the no-weights phrase
- the rigidity dependency must contain `no independent scalar-normalization freedom`
- the semigroup dependency must contain `continuous Markov semigroups live on the probability/ensemble`
- this note must preserve `set only by the independent audit lane`
- this note must preserve `recorded-neighborhood baseline`
- this note must preserve `quantized`
- this note must preserve `k/64`
- this note must preserve `off-lattice`
- this note must preserve `occupancy residual`
- this note must preserve `located, never forced`
- this note must preserve `not a citation-graph dependency`
- this note must preserve `does not claim:`
- this note must preserve `an audit verdict or any effective-status promotion`
- this note must preserve `does not derive the admissibility rule`
- this note must preserve `does not derive occupancy statistics`

The runner also checks that forbidden machine-readable needles are absent from both this note and the runner source. Those needles are built in the runner from fragments: `audit_` + `status:`, `effective_` + `status:`, `only` + ` route`, `exhaust` + `ed`, and `closes` + ` the route`.

## Verification

Run:

```bash
python3 scripts/informative_fraction_covariant_rule_quantization_occupancy_residual_2026_07_02.py
```

Expected final line:

```text
TOTAL: PASS=67 FAIL=0
```
