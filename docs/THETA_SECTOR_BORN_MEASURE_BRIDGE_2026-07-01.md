# Theta Sector Born-Measure Bridge

**Date:** 2026-07-01
**Claim type:** bounded bridge theorem / sector-measure supplier.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
Strong-CP closure.
**Primary runner:**
[`scripts/theta_sector_born_measure_bridge_2026_07_01.py`](../scripts/theta_sector_born_measure_bridge_2026_07_01.py)

## Claim

The theta pointwise selector needs a pointwise nonnegative record-facing
sector measure. The Record/Born interface supplies exactly that measure once
the emergent integer sector label is supplied as a finite sharp record
context.

Given:

```text
a finite sharp sector-record context {P_Q},
integer labels Q,
a normalized record-facing state rho,
and a supplied selective record-writing/effect interface,
```

the sector weights

```text
Z_Q = Tr(rho P_Q)
```

are pointwise nonnegative, normalized, and additive over disjoint sector
record events. If the supplied sector context has nonzero odd-sector support,
then the theta pointwise selector applies and chooses

```text
theta = 0
```

from the already narrowed CP-even set `{0, pi}`.

This bridge therefore closes the sector-measure subwall on a supplied sharp
`Q` record surface. It does not derive the emergent `Q` sector context, odd
support, the physical gauge action, or the joint gauge/mass `theta_bar`
assembly.

## Finite Theorem

Let a finite sharp sector-record context have projectors

```text
P_Q P_Q' = delta_QQ' P_Q,
sum_Q P_Q = I.
```

For any normalized positive state `rho`,

```text
Z_Q = Tr(rho P_Q)
```

satisfies

```text
Z_Q >= 0,
sum_Q Z_Q = 1.
```

If the sector context is conjugation-paired, `Q -> -Q`, and the record-facing
state has paired weights, then

```text
Z_Q = Z_-Q.
```

The theta pointwise contribution is

```text
W_theta(Q) = exp(i theta Q) Z_Q.
```

On the prior real/conjugation-invariant surface, the effective angle is already
confined to `{0, pi}`. For `theta = 0`,

```text
W_0(Q) = Z_Q >= 0.
```

For `theta = pi`,

```text
W_pi(Q) = (-1)^Q Z_Q.
```

If any odd `Q` sector has `Z_Q > 0`, then `W_pi(Q) < 0` for that sector.
Therefore `theta = pi` is incompatible with pointwise nonnegative
record-facing sector weights, and `theta = 0` is selected.

If all supported sectors are even, this bridge cannot distinguish `0` from
`pi`.

## Explicit Finite Witness

Take a three-sector sharp record context:

```text
Q in {-1, 0, 1},
rho = diag(1/8, 3/4, 1/8),
P_-1 = diag(1, 0, 0),
P_0  = diag(0, 1, 0),
P_1  = diag(0, 0, 1).
```

Then

```text
Z_-1 = 1/8,
Z_0  = 3/4,
Z_1  = 1/8.
```

The weights are nonnegative, normalized, conjugation-paired, and have odd
support. At `theta = 0`, all sector contributions are nonnegative. At
`theta = pi`,

```text
W_pi(-1) = -1/8,
W_pi(0)  =  3/4,
W_pi(1)  = -1/8.
```

The total partition sum remains positive:

```text
sum_Q W_pi(Q) = 1/2.
```

So total positivity is not enough. The extra pointwise sector-measure
requirement is what rejects `pi`.

## What Moves

| Prior residual | Effect of this bridge |
|---|---|
| pointwise nonnegative sector measure | supplied by Record/Born trace weights once `Q` is a sharp record context |
| 0-vs-pi selector | `theta = 0` follows when odd-sector support is nonzero |
| partition-positivity confusion | separated again: total positivity can coexist with negative odd-sector weights |
| generic theta-sector measure primitive | narrowed to a supplied sharp `Q` record interface plus Record/Born |

## What Remains

The remaining theta wall is narrower:

```text
W_theta_Q_context:
  derive or supply an emergent integer Q as a physical sharp sector-record
  context, with nonzero odd-sector support on the relevant surface.

W_theta_bar_assembly:
  assemble the gauge-side sector result with the mass-side determinant,
  anomaly/chiral bookkeeping, and physical quark-sector bridge into the
  invariant theta_bar.
```

This bridge does not derive either wall. It supplies the pointwise
sector-measure part once `W_theta_Q_context` is supplied.

## Audit Consequence If Retained

Rows that need the conditional theta selector should cite:

```text
emergent sharp Q sector-record context with odd support
  + Record/Born sector measure
  + theta pointwise sector selector
  -> theta = 0 from {0, pi}.
```

Rows that need full Strong-CP closure still need the emergent-Q/gauge-action
bridge and the joint `theta_bar` assembly. Rows that only have a sign-weighted
or non-record-facing sector expansion may not cite this bridge as a
probability-measure supplier.

## Non-Claims

This note does not claim:

- Strong-CP closure;
- derivation of the emergent integer `Q`;
- proof of odd-sector support;
- derivation of the physical gauge action or scaling-limit sector surface;
- exclusion of sign-weighted formulations outside a record-facing probability
  measure;
- derivation of `theta_bar` assembly;
- spontaneous CP violation is impossible;
- record occurrence, source/action, metric, observable, or charged-lepton
  readout gates are closed;
- measured constants, fitted values, lattice-MC values, or a new primitive are
  used.

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this theorem.

If bridge-first routes fail, the fallback remains the narrow operational
candidate:

```text
P_gauge_sector_measure:
  On an emergent gauge-sector surface, a physical sector-measure primitive
  supplies the integer sector label, the pointwise record-facing sector
  measure, and the assembly rule for the joint gauge/mass invariant angle.
```

This bridge shows that the pointwise measure portion does not need to be
primitive if the sharp `Q` record interface is derived. The primitive fallback,
if ever approved, should focus on the physical `Q` sector surface and
`theta_bar` assembly that this bridge does not derive.

## No-Go Discipline Gate

**Status:** PASS for bounded wall localization inside a positive bridge. This
is not a terminal no-go. The negative boundary is only that Record/Born sector
weights do not derive the emergent `Q` context or `theta_bar` assembly.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Record/Born sector-measure route | Use a supplied sharp `Q` context to get pointwise nonnegative sector weights. | ATTEMPTED here: succeeds exactly as `Z_Q = Tr(rho P_Q)`. |
| Pointwise theta selector route | Use those pointwise weights plus odd support to choose `0` from `{0, pi}`. | CONSUMED BY PRIOR: the theta pointwise selector supplies this finite step. |
| Reality/conjugation route | Use real conjugation-invariant weighting to select `0`. | RULED OUT BY PRIOR: it gives `{0, pi}`, not `0`. |
| Partition-positivity route | Use positive total partition sum to reject `pi`. | RULED OUT BY PRIOR and witnessed here: total `sum_Q W_pi(Q)` can be positive while odd sector weights are negative. |
| Emergent-Q route | Derive the integer sector context from the gauge/scaling bridge. | OPEN: not supplied by this bridge. |
| Theta-bar route | Assemble gauge and mass sides into invariant `theta_bar`. | OPEN: structured admission keeps this as a separate residual. |
| New primitive route | Register gauge-sector measure as an operational primitive. | OWNER-GOVERNANCE ROUTE: available only if bridge-first routes fail or are intentionally bypassed. |

### N2 - Wall-Independence Audit

Collapsed residual after this bridge:

```text
W_theta_Q_context
W_theta_bar_assembly
```

Once a sharp `Q` record context with odd support is supplied, the pointwise
sector measure follows from Record/Born and is not an independent residual.
Supplying `Q` does not assemble `theta_bar`; assembling `theta_bar` requires
a gauge-side sector object but does not itself prove that the object is a
sharp record-facing probability context with odd support.

### N3 - Hidden-Wall Scan

"Supplied sharp `Q` context" is an explicit bridge input, not hidden axiom
content. "Record-facing probability measure" means the Record/Born interface
has been applied to sector projectors. "Odd support" is a support condition,
not derived by this note. "Pointwise" means each sector contribution, not the
total partition sum.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01` | pointwise sector measure plus odd support selects `0`. | consumed selector after Record/Born supplies measure. | yes |
| `RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30` | Born trace weights after supplied sharp interface. | sector-measure supplier. | yes |
| `THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q...` | emergent `Q` remains open. | preserved as `W_theta_Q_context`. | yes |
| `THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE...` | real weighting narrows to `{0, pi}`; `Q` and 0-vs-pi remain. | supplies prior CP-even set and paired weights. | yes |
| `STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT...` | positivity/reality does not force `0`. | preserved; pointwise probability is stronger than total positivity. | yes |
| `STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION...` | joint gauge/mass invariant assembly remains open. | preserved as `W_theta_bar_assembly`. | yes |
| `MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01` | `P_gauge_sector_measure` is fallback, not registered. | same fallback if bridge-first fails. | yes |

### N5 - Rhetoric Audit

The negative boundary is narrow: Record/Born sector weights do not derive the
sector label or the invariant angle assembly. The positive theorem is tested at
finite sharp-sector context resolution. It does not claim all theta
formulations must be pointwise probability measures, and it does not exclude
sign-weighted representations outside the declared record-facing surface.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive emergent `Q` and odd-sector support from the gauge-action/scaling
  bridge;
- derive a physical sharp-sector readout interface for `Q`;
- derive `theta_bar` assembly with mass-side determinant and anomaly
  bookkeeping;
- derive a gauge action surface that excludes topological sign weighting
  before the sector selector is needed;
- explicitly approve `P_gauge_sector_measure` only if bridge-first routes fail
  or owner governance chooses that route.

The primitive-registry check confirms that no current approved primitive
already grants a gauge-sector measure or `theta_bar` assembly.

### N7 - Steelman

A hostile reviewer can say this theorem is mostly interface plumbing: if `Q`
is already a sharp record with a Born interface, of course the weights are
nonnegative. The hard physics is deriving the emergent topological sector and
showing that the physical theta expansion must be record-facing and
pointwise-probabilistic rather than sign-weighted. That objection is correct
and preserved. This bridge is useful because it removes the measure subwall
once the sharp `Q` interface is supplied; it does not pretend to derive `Q`.

### N8 - Cross-Cycle Echo

Earlier theta cycles overclaimed by treating reality, partition positivity, or
substrate no-carrier results as `theta = 0`. The current stack split those
pieces: substrate carrier, real `{0, pi}` surface, pointwise selector, and now
Record/Born sector-measure supplier. This note keeps the split and leaves the
emergent-Q and `theta_bar` walls explicit.

## Verification

Run:

```bash
python3 scripts/theta_sector_born_measure_bridge_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=114 FAIL=0
```
