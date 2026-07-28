# Lattice NN High-Precision Note

**Date:** 2026-04-03 (mixed-precision certificate 2026-05-16; bounded
live-comparator repair 2026-07-28)
**Type:** bounded_theorem
**Primary runner:**
[`scripts/lattice_nn_high_precision_raw_certificate.py`](../scripts/lattice_nn_high_precision_raw_certificate.py)
**Canonical raw runner:**
[`scripts/lattice_nn_continuum.py`](../scripts/lattice_nn_continuum.py)
**Comparator runner:**
[`scripts/lattice_nn_deterministic_rescale.py`](../scripts/lattice_nn_deterministic_rescale.py)
**Status:** protocol-specific bounded numerical certificate for one supplied
finite harness at exactly `h = 0.125`; independent audit is required.

## Scoped claim

For the finite nearest-neighbor harness and parameters specified below, the
mixed-precision raw-kernel implementation completes at `h = 0.125` and returns
the full implemented observable row. In particular, its Born residual is
below the declared `10^-10` threshold.

The primary runner also recomputes the deterministic-rescale row live, in the
same process and without rounded or hard-coded target values. At `h = 0.125`,
all six returned quantities—gravity, the `k = 0` control, mutual information,
classical purity, total-variation distance, and Born residual—agree within the
predeclared absolute protocol threshold `10^-12` in the recorded numerical
environment. Both Born residuals separately satisfy the declared `10^-10`
diagnostic threshold.

This is a bounded pointwise numerical certificate for the supplied protocol
and recorded environment. The comparison threshold is an acceptance criterion
for these two implementations, not a forward-error or cross-platform accuracy
bound. The certificate is not an exact or all-spacings step-scale-invariance
theorem, an `h -> 0` continuum theorem, or a derivation of the harness, kernel,
parameter choices, observables, or Born rule from the framework axioms.

## The gate that is closed

The load-bearing open-gate statement was:

> The `h = 0.125` continuation did not complete in a practical runtime window
> and did not produce a retained numerical result.

That statement accurately described the original 2026-04-03 attempt. It is
not a no-go theorem. The current primary runner closes the computational
noncompletion gate by executing the same implemented per-edge raw kernel with
a wider-range amplitude accumulator and returning a checked `h = 0.125` row.
No rescale factor is inserted into this raw propagation.

The source note does not set audit status or grade. Its `bounded_theorem`
classification records the supplied numerical conditions; the independent
audit lane decides whether the claim is accepted.

## Supplied finite harness

The computation reuses the nearest-neighbor family from
[`scripts/lattice_nn_continuum.py`](../scripts/lattice_nn_continuum.py):

- physical width `W = 20`
- physical length `L = 40`
- spacing `h = 0.125`
- `321` layers and `103041` nodes
- three forward edges per interior node
- `k = 5`
- angular-weight coefficient `beta = 0.8`
- field strength `5e-4`
- radial softener `0.1` in the supplied `1 / (r + 0.1)` mass field
- slit position `y = 3`
- mass location `y = 8`
- `8` detector bins
- decoherence-overlay coefficient `lambda = 10`
- the same slit-width and three-slit construction rules as the existing NN
  runners

These are the supplied claim surface. This note does not derive them from
`A_min`, and it does not use an observed target value or fitted selector as a
load-bearing input.

## Mixed-precision raw propagation

The raw per-edge factor is unchanged from the canonical implementation,

```text
exp(i k act) w / L.
```

The implementation is deliberately described as mixed precision:

- lattice geometry, field values, `act`, and the per-edge phase are evaluated
  in float64, as in the canonical raw runner
- amplitude accumulation uses `mpmath.mpc` at `dps = 30`
- no per-step rescale, layer normalization, observable-dependent correction,
  or data-dependent schedule is applied

Thus the certificate concerns the specified implemented kernel. It does not
claim exact-real evaluation of its geometry or phases.

## Live comparator and assertions

The earlier certificate compared the raw row with rounded constants copied
from a cache. That was inadequate for an all-observable equivalence claim:
the targets were low precision, the `k = 0` control and Born residual were not
part of the combined assertion, and the prior common-scalar argument had not
been shown to cover the implemented mixed-depth purity construction.

The repaired runner imports `measure_full` from both the canonical raw runner
and
[`scripts/lattice_nn_deterministic_rescale.py`](../scripts/lattice_nn_deterministic_rescale.py)
and recomputes its comparator rows live. At `h = 0.25`, the mixed-precision row
must agree with both the canonical raw row and the deterministic-rescale row.
At the gate spacing `h = 0.125`, it applies:

```text
for q in {gravity, gk0, MI, pur_cl, dtv, born}:
    abs(raw[q] - rescaled[q]) <= 1e-12

raw[born]      < 1e-10
rescaled[born] < 1e-10
```

It then recomputes the raw `h = 0.125` row at `dps = 40`; every returned
quantity must agree with the primary `dps = 30` row within the separately
predeclared `10^-24` precision-stability threshold. This guard is eight orders
tighter than the raw/rescaled protocol threshold. The Born value is expected
to move with the mpmath cancellation floor, but its absolute change must still
pass that guard.

Every quantity and every guard participates in the exit-code decision. The
comparisons use unrounded returned values; formatting occurs only after the
differences have been computed. The primary runner declares both the canonical
raw and deterministic-rescale sources in `AUDIT_INPUT_PATHS`, so the
content-pinned cache becomes stale if any of those sources changes. Its output
also records Python, mpmath, operating-system, machine, and float-mantissa
provenance. The environment record bounds the cached statement; it does not
claim portability to an untested environment.

## `h = 0.125` result

The 2026-07-28 verification run returned:

| quantity | mixed-precision raw | live deterministic rescale | absolute difference |
|---|---:|---:|---:|
| gravity | `3.44658632356807706405957e-02` | `3.44658632356811545083275e-02` | `3.839e-16` |
| `k = 0` control | `0.0` | `0.0` | `0.0` |
| MI | `9.97190194714790828611629e-01` | `9.97190194714790978380847e-01` | `1.498e-16` |
| classical purity | `5.00005664009480683657072e-01` | `5.00005664009480432774524e-01` | `2.509e-16` |
| `d_TV` | `9.99587635205019284504241e-01` | `9.99587635205019253703540e-01` | `3.080e-17` |
| Born residual | `5.48340895401153988423037e-31` | `5.63436630226487148826411e-16` | `5.634e-16` |

The maximum raw/rescaled difference is below `10^-12`, and both Born residuals
are below the declared `10^-10` diagnostic threshold. The runner exits zero
only when the canonical and rescaled `h = 0.25` regressions, the live
`h = 0.125` all-observable check, and the `dps = 30` versus `dps = 40`
precision-stability check all pass. In the cached precision check, the largest
non-Born absolute change was `4.226e-30`; the Born cancellation-floor change
was `5.483e-31`.

## Derivation chain

1. The original high-precision attempt did not finish, so it supplied no
   `h = 0.125` row and correctly left an open computational gate.
2. The current runner keeps the raw per-edge kernel and does not insert the
   deterministic rescale used by the comparator lane.
3. Replacing only the amplitude accumulator with `mpmath.mpc` supplies enough
   exponent range for the finite propagation to terminate at `h = 0.125`.
4. The runner computes all six observables from that completed raw
   propagation, including the Born residual.
5. At `h = 0.25`, it independently invokes the canonical raw and
   deterministic-rescale implementations as live regressions.
6. At `h = 0.125`, it invokes the deterministic-rescale implementation in the
   same process and compares the unrounded rows observable by observable.
7. A separate `dps = 40` raw recomputation checks stability of the primary
   `dps = 30` row.
8. The live assertions pass with maximum raw/rescaled discrepancy below the
   `10^-12` protocol threshold; each Born residual also passes the `10^-10`
   diagnostic threshold.
9. Therefore the historical noncompletion gate is closed for this specified
   finite numerical surface and recorded environment.

The conclusion follows from an executed finite computation and its explicit
assertions. It does not rely on the unestablished broader premise that every
observable is a homogeneous same-depth amplitude ratio.

## Exact scope boundaries

The certificate does **not** establish:

- a universal exact step-scale-invariance theorem
- exact equality of raw and rescaled rows
- an exact-real or all-mpmath evaluation of geometry and phases
- an unavoidable float64-overflow theorem
- a continuation at spacings finer than `h = 0.125`
- convergence as `h -> 0`
- a continuum field theory, renormalization law, or physical fixed point
- a derivation of the supplied dynamics or observable definitions from
  `A_min`

The commonly quoted loose scale estimate should use the `320` transitions
between `321` layers: `24^320`, of order `10^442`. It is only an upper-bound
warning about potential dynamic range. An upper bound above float64 range is
not a lower-bound proof that every implementation must overflow. The observed
failure of the historical float64 run and the timeout of the original
high-precision attempt are implementation outcomes, not physics no-go claims.

## Comparator scope boundary

A deterministic factor applied once per propagation layer gives a common
factor at a fixed detector layer. Normalized detector probabilities and
fixed-layer centroids therefore have an exact cancellation argument on that
narrow surface.

The implemented classical-purity overlay instead bins and sums amplitudes from
a range of intermediate depths before constructing its decoherence factor.
The existing fixed-layer common-scalar argument has not been shown to cover
that functional. This note makes no negative theorem about whether some other
exact identity exists; depth-resolved conjugacies and alternate exact
identities remain open.

The bounded statement supported here is only that, for the single supplied
`h = 0.125` protocol and recorded environment, the two live implementations
numerically agree within the declared acceptance threshold on every returned
quantity.

## Sibling-consumer sweep

A 2026-07-28 source sweep found historical consumers that still describe a
universal step-scale-invariance theorem: the rescaled continuum-identification,
operator-Cauchy, RG-gravity, reconciliation, and fanout notes, plus their
paired runners. Their current audit rows are all `unaudited`. This bounded note
does not supply the universal premise used by those historical descriptions,
and this repair does not ratify them. They require separate source-side review
before that premise can be reused. The old high-precision closure runner is
therefore not cited below as support for this certificate.

## Historical audit trail

- **2026-05-03:** the original timed-out attempt was correctly classified as
  a clean `open_gate`; no positive extension was promoted.
- **2026-05-07 to 2026-05-10:** an overflow estimate and a limited
  fixed-layer cancellation check did not justify the broader canonical
  equivalence claim.
- **2026-05-16:** the mixed-precision runner completed the raw propagation and
  supplied the positive numerical core, but its comparator assertions used
  rounded hard-coded targets and its prose retained the overbroad exact
  invariance claim.
- **2026-07-25:** re-audit rejected that broader claim and requested a live
  full-value comparator including `k = 0`, Born, and mixed-depth purity, or a
  narrower claim.
- **2026-07-28 repair:** the runner performs the requested live
  all-observable comparison, pins the canonical raw source, records its
  environment, and adds canonical-regression and precision-stability guards.
  This note narrows the result to a protocol-specific bounded certificate.

## Reproduction

Run:

```bash
python3 scripts/lattice_nn_high_precision_raw_certificate.py
```

The checked cache is:

- [`logs/runner-cache/lattice_nn_high_precision_raw_certificate.txt`](../logs/runner-cache/lattice_nn_high_precision_raw_certificate.txt)

Supporting historical artifacts are:

- [`scripts/lattice_nn_high_precision.py`](../scripts/lattice_nn_high_precision.py)
  — the original noncompleted attempt
- [`logs/runner-cache/lattice_nn_deterministic_rescale.txt`](../logs/runner-cache/lattice_nn_deterministic_rescale.txt)
  — historical standalone comparator cache; the primary certificate no longer
  reads values from it

## Re-audit target

Audit only this bounded computational statement: in the cache-recorded
environment, the supplied mixed-precision raw NN implementation completes at
`h = 0.125`, returns the displayed row below the declared Born diagnostic
threshold, passes the `dps = 30` versus `dps = 40` stability guard, and agrees
pointwise with a live deterministic-rescale run on all six implemented
quantities within the predeclared absolute protocol threshold `10^-12`. Do not
audit or infer a universal exact rescale theorem, a cross-platform error bound,
or an `h -> 0` continuum claim from this note.
