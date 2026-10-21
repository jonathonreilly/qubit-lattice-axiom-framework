# DM Wilson Direct-Descendant Constructive Transport Plateau Theorem

**Claim type:** bounded_theorem

**Date:** 2026-04-19; numerical-scope correction 2026-10-21
**Status:** finite numerical support on a supplied transport fixture; no audit
status assigned. Four distinct constructive interior candidates share the
reported value `eta_1 = 1.052220313052...` to numerical precision. This is
evidence of a nearly level sampled region, not a proof of multiple exact
global extrema or a source-independent cap. Physical endpoint selection
remains open. The legacy filename is retained for traceability.

**Primary runner:**
`scripts/frontier_dm_wilson_direct_descendant_constructive_transport_plateau_theorem_2026_04_19.py`
(`PASS=17 FAIL=0`).

## Question

The same-day canonical-path theorem gave a real selector-law candidate:

> choose the unique `eta_1 = 1` point on the aligned-seed ->
> constructive-witness affine path.

But that still left a natural next question:

Can the constructive endpoint itself be made canonical just by appealing to the
already-known transport result?

More sharply:

- the constructive projected-source theorem already proved that the
  constructive sign chamber reaches the current transport-extremal value;
- does maximizing `eta_1` inside that constructive sign chamber uniquely pick
  the constructive witness?

## Observed finite result

Local refinement from the four supplied anchors returns distinct constructive
interior candidates with the same displayed transport value and small
stationarity residuals. Finite precision and local optimization do not prove
exact equality, extrema, or exhaustive global coverage.

## The four numerical constructive candidates

The branch now has at least the following four constructive interior
transport candidates:

### `W0` (the original constructive witness)

```text
x = (1.17416156, 0.46254435, 0.05329409)
y = (0.75874142, 0.02690430, 0.13435428)
delta = 1.882595756164
eta = (0.92932093, 1.05222031, 0.80149003)
(gamma, E1, E2) = (0.15014724, 0.29656285, 1.98640744)
```

### `W1`

```text
x = (0.90533908, 0.34108481, 0.44357611)
y = (0.77562148, 0.00429993, 0.14007859)
delta = 2.248936000000
eta = (0.74569694, 1.05222031, 0.87957312)
(gamma, E1, E2) = (0.09875887, 0.12204367, 1.34544744)
```

### `W2`

```text
x = (1.10861499, 0.41991159, 0.16147342)
y = (0.83443268, 0.00372167, 0.08184565)
delta = 1.480589000000
eta = (0.82166028, 1.05222031, 0.69287680)
(gamma, E1, E2) = (0.09036640, 0.24289064, 1.99942908)
```

### `W3`

```text
x = (1.13210268, 0.52825826, 0.02963906)
y = (0.48423456, 0.18550120, 0.25026425)
delta = 2.930589000000
eta = (1.01405294, 1.05222031, 1.03502767)
(gamma, E1, E2) = (0.05933995, 0.39139937, 1.31153236)
```

All four sit on the same fixed native seed surface. All four are strictly
constructive. All four share the displayed `eta_1` to numerical precision.

## Numerical scope

The four supplied witnesses share the displayed value to the runner
precision on this fixed transport fixture. These checks exhibit distinct numerical candidates; they do not prove an exact source-independent cap or global
optimization over all admissible source data. The physical source-selection
law remains open.

## Consequence and remaining obligations

The sampled calculation does not justify treating the selected path endpoint
as a uniquely established transport extremizer. It also does not prove that
no exact unique extremizer can exist. A rigorous conclusion needs certified
stationarity/extremality and global coverage or an analytic degeneracy proof.

The aligned-seed-to-witness path remains a supplied path; the separate path
crossing calculation does not select its endpoint physically. A finer source
law, physical identification and the DM flagship closure remain open.

## Cross-references

- [`docs/DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_PROJECTED_SOURCE_SELECTOR_THEOREM_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_PROJECTED_SOURCE_SELECTOR_THEOREM_NOTE_2026-04-16.md)
- [`docs/DM_WILSON_DIRECT_DESCENDANT_CANONICAL_PATH_SELECTOR_THEOREM_NOTE_2026-04-19.md`](DM_WILSON_DIRECT_DESCENDANT_CANONICAL_PATH_SELECTOR_THEOREM_NOTE_2026-04-19.md)
- [`docs/DM_WILSON_DIRECT_DESCENDANT_LOCAL_OBSERVABLE_COORDINATE_THEOREM_NOTE_2026-04-19.md`](DM_WILSON_DIRECT_DESCENDANT_LOCAL_OBSERVABLE_COORDINATE_THEOREM_NOTE_2026-04-19.md)

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_wilson_direct_descendant_constructive_transport_plateau_theorem_2026_04_19.py
```

Expected:

- `PASS=17 FAIL=0`
