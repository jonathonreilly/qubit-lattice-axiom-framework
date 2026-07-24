# Finite Retained-Counter And Co-Registration Identities

**Date:** 2026-07-24

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Primary runner:**

[`scripts/finite_retained_counter_coregistration_identities_2026_07_24.py`](../scripts/finite_retained_counter_coregistration_identities_2026_07_24.py)

**Runner cache:**

[`logs/runner-cache/finite_retained_counter_coregistration_identities_2026_07_24.txt`](../logs/runner-cache/finite_retained_counter_coregistration_identities_2026_07_24.txt)

**Receipt:**

[`outputs/finite_retained_counter_coregistration_identities_receipt_2026_07_24.json`](../outputs/finite_retained_counter_coregistration_identities_receipt_2026_07_24.json)

## Scope

This packet is a self-contained finite arithmetic lemma. Conditional on the
complete supplied fixture below, the displayed retained-counter decoder has
the following exact properties on the enumerated finite streams:

1. decoded positions equal the number of supplied tick crossings preceding
   each co-registration label under the declared tie convention;
2. decoded integer intervals telescope on every ordered label triple;
3. reversing the supplied stream order negates every decoded interval while
   preserving the corresponding exact rational count ratios;
4. one supplied bank reset between `S2` and `S3` leaves every marked position
   and interval unchanged when the carry count persists;
5. deleting `S2` makes queries using `S2` undefined (`None`) while leaving the
   `S1`-to-`S3` interval unchanged;
6. decoded counts telescope across the supplied piecewise slope change; and
7. the supplied finite cross-order predicate accepts the ordinary fixture and
   refuses the declared injected inversion.

These are statements only about the finite definitions and fixtures executed
by the runner. The decoder used throughout is

```text
P(S) = K * carry_count(S) + rotor(S),
Delta(S_i,S_j) = P(S_j) - P(S_i).
```

The interval is defined only when both labels exist and predecessor traversal
connects the later-index endpoint to the earlier-index endpoint; otherwise it
is `None`. These formulas do not identify a decoded count or ordering marker
with any physical quantity.

## Complete Supplied Fixture

| Item | Supplied value or convention |
|---|---|
| Generator span | Exact rational coordinate interval from `0` to `4096` |
| Piecewise split | Coordinate `2048` |
| Co-registration labels | `S1=512`, `S2=1500`, `S3=2600`, `S4=3800` |
| Signed tick slopes | `A=-296/625`, `B=-5/16`, `C=-287/1250`, `D_first=-296/625`, `D_second=-5/16` |
| Crossing convention | Positive integer crossings of accumulated absolute slope; segment upper endpoints excluded |
| Tie convention | Tick before label forward; label before tick after reversal |
| Counter | Rotor modulus `K=16`; persistent integer `carry_count` on each wrap |
| Position decoder | `P(S)=K*carry_count(S)+rotor(S)`; a missing label returns `None` |
| Interval decoder | `Delta(S_i,S_j)=P(S_j)-P(S_i)` only when both labels exist and the later-index-to-earlier-index predecessor traversal connects them; otherwise `None` |
| Large control bank | Capacity `1,000,000,000`; reset allowance zero |
| Reset-test bank | Capacity `700`; exactly one reset allowed |
| Label operation | Snapshot rotor and carry state without consuming a bank slot |
| Reset operation | Restore the supplied bank capacity and reset `bank_slot`; retain rotor and `carry_count` |
| Cell topology | Each cell index is its zero-based list position; every noninitial predecessor is the preceding cell index and the initial predecessor is `None` |
| Lineage convention | Endpoint order uses `cell.index`; predecessor traversal must connect them |
| Missing-label value | `None`, not zero |
| Floating diagnostic tolerance | `2/min(abs(nonzero decoded segment count))`; infinity when no nonzero count exists |
| Cross-order devices | Three labels: `A`, `B`, and `C` |
| Cross-order initial state | Every device position is zero; shared-snapshot list is empty |
| Cross-order local operation | `append_local(d)` increments only device position `d` by one |
| Cross-order predicate | For current snapshot `s`, accept iff every prior shared snapshot `p` satisfies `p[d] < s[d]` for every device `d` |
| Acceptance mutation | Increment every device position by one, append the pre-increment snapshot, and return `accepted` |
| Refusal mutation | Return `refused_inverted` without changing any position or the shared-snapshot list |
| Ordinary cross-order row | Increment every device twice, then call the supplied predicate four times |
| Adversarial row | Increment every device four times; accept once; append prior snapshot `A=1`, `B=9`, `C=1` without applying the predicate; call the predicate once |

The canonical JSON serialization of this inventory has SHA-256
`49ffc9256366b787cd38d71c3c0348514b833b21549826468ebd7214b7ae0cc2`, also
printed in the receipt. No external runner, receipt, ledger row, or off-branch
artifact supplies executable state.

## Exact Results And Controls

The runner uses Python integers and `fractions.Fraction` for the exact checks.
It checks 12 telescoping rows and 18 reversed intervals. The piecewise count is

```text
969 + 640 = 1609.
```

The reset-test chain uses one reset at cell index `702`, between the `S2` and
`S3` labels, and matches the large-bank control on every marked position and
all six label-pair intervals. A carry-erasure mutation changes a cross-reset
interval, so persistence of the supplied carry count is load-bearing.

The ordinary cross-order fixture ends with device positions `(6,6,6)` and
pre-increment shared snapshots `(2,2,2)` through `(5,5,5)`. The first
adversarial acceptance changes `(4,4,4)` to `(5,5,5)` and stores `(4,4,4)`.
After the supplied `(1,9,1)` prior snapshot is injected, refusal leaves both
the device positions and the shared-snapshot list exactly unchanged.

Mutating every stored `bank_slot` and generator-coordinate value leaves the
displayed decoder output unchanged. Breaking the predecessor link at `S3`
makes the `S1`-to-`S3` query undefined. Thus this packet does not make a broad
metadata-independence claim: integer cell indices and predecessor lineage
remain explicitly load-bearing.

## Floating Diagnostic

One separate check converts exact finite count ratios to binary floating point.
It compares their three-segment spread with the disclosed tolerance
`2 / min(abs(decoded segment count))`:

| Ratio | Observed spread | Tolerance |
|---|---:|---:|
| `B/A` | `0.0021490558918582092` | `0.006493506493506494` |
| `C/B` | `0.004454847478103319` | `0.00881057268722467` |

This is a finite floating diagnostic, not an exact identity or continuum-rate
result. The exact claims in this packet are the integer and rational identities
listed above.

## Boundaries

- The tick streams, slopes, generator span, co-registration coordinates,
  decoders, crossing and tie conventions, counter modulus, bank capacities,
  reset behavior, predecessor topology, missing-label convention, floating
  tolerance, and complete cross-order predicate are all supplied.
- The generator coordinate only orders the fixture; the decoder does not read
  it.
- The one-reset identity does not construct or select a reset mechanism. It is
  conditional on the displayed reset procedure and persistent carry count.
- “Retained” in the title means only that `carry_count` is unchanged through
  the one supplied refill. It is neither audit retained status nor a claim of
  physical persistence.
- The cross-order result executes a supplied finite predicate. It does not
  derive or select that predicate.
- Co-registration labels are bookkeeping markers in these finite chains.
- No tick, count, coordinate, label order, or decoded interval is identified
  with physical time, elapsed duration, a time metric, causal order,
  chronology, evolution, or an update law.
- The finite counter is not a physical clock. No count or count ratio is a
  clock rate, frequency, calibration, detector observable, or empirical
  measurement.
- No label, snapshot, cell, rotor, or carry count is a framework `Record`.
  This packet constructs no Record formation, locking, permanence, readout, or
  realized-history mechanism.
- No encoding into physical `M_2(ℂ)` sites is supplied. This packet is not a
  physical-site compiler and establishes no resource overhead, noise,
  leakage, deletion, held-out-size, or scaling result.
- No covariance, matter, or empirical calibration is supplied or inferred.
- These are construction-scope boundaries, not route-independent
  impossibility claims. Physical time, clock, Record, causal, and site-level
  bridges remain open downstream; this packet asserts no axiom pressure.
- Authority remains none and audit remains unset. The pipeline and independent
  audit process determine any later standing.

## Dependencies

There are no repository or scientific-authority dependencies. The runner reads
no repository artifact. Its complete executable import inventory is
`__future__.annotations`, `copy`, `dataclasses.dataclass`,
`fractions.Fraction`, `hashlib.sha256`, `itertools.combinations`, `json`,
`math`, `pathlib.Path`, `sys`, `typing.Iterable`, and `typing.Sequence`, all
from the Python standard library. The note links only its runner, cache, and
receipt for reproduction.
