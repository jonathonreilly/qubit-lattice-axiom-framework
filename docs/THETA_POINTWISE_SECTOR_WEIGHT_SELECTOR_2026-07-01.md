# Theta Pointwise Sector-Weight Selector

**Date:** 2026-07-01
**Claim type:** bounded theorem / conditional selector bridge.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, refresh generated ledgers, register a
primitive, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_pointwise_sector_weight_selector_2026_07_01.py`](../scripts/theta_pointwise_sector_weight_selector_2026_07_01.py)

## Claim

The existing theta bridge work leaves a precise surface:

```text
if an emergent integer sector functional Q is supplied, real
conjugation-invariant weighting confines the effective angle to {0, pi}.
```

That result does not choose between `0` and `pi`, and the prior theta no-go
correctly says that reality or partition-function positivity alone does not
force `theta = 0`.

This note adds one narrower conditional selector. If the emergent sector
weighting is required to be a pointwise nonnegative record-facing probability
measure over sectors, then within the already-narrowed set `{0, pi}`:

```text
theta = 0
```

is the only allowed member whenever at least one odd-`Q` sector has nonzero
weight.

The reason is finite and exact. `theta = pi` multiplies sector `Q` by
`(-1)^Q`. Every odd sector therefore receives a negative pointwise weight.
That can leave the total partition sum positive, so it is not ruled out by
partition positivity alone. It is ruled out only by the stronger pointwise
nonnegativity premise.

If no odd-`Q` sector has nonzero weight, this selector cannot distinguish
`0` from `pi`.

## Finite Theorem

Let the emergent sector surface have finite sector weights

```text
Z_Q >= 0,   Z_Q = Z_-Q.
```

Assume the prior theta weighting bridge has already confined the effective
angle to the CP-even set `{0, pi}`.

Define the sector-weighted contribution

```text
W_theta(Q) = exp(i theta Q) Z_Q.
```

For `theta = 0`,

```text
W_0(Q) = Z_Q >= 0
```

for every sector.

For `theta = pi`,

```text
W_pi(Q) = (-1)^Q Z_Q.
```

If some odd integer `Q` has `Z_Q > 0`, then `W_pi(Q) < 0`. Therefore
`theta = pi` is incompatible with pointwise nonnegative sector weights.

The theorem is silent when all nonzero support is even-sector support, because
then `(-1)^Q = 1` on the supported sectors and both `0` and `pi` give the same
nonnegative sector weights.

## Relation To Prior Theta Notes

This note preserves the prior boundaries.

- The substrate note says there is no theta carrier on the supplied lattice
  gauge substrate and relocates the gauge-side wall to the emergent-`Q` bridge.
  This note does not derive `Q`.
- The emergent-`Q` weighting note gives the conditional CP-even set `{0, pi}`.
  This note starts only after that narrowing.
- The reality/positivity/CPT no-go says partition-function positivity does not
  force `theta = 0`. This note agrees: a positive total partition sum can
  coexist with negative odd-sector contributions at `theta = pi`.
- The Wilson real-positive surface supplies a related real-positive action
  convention on a bounded single-plaquette surface. This note does not claim
  that convention has been derived for the emergent sector action.
- The Record/Born interface supplies record-facing probabilities after a
  selective interface. This note does not derive that the emergent theta
  sector weighting is such a probability measure.

## What Moves

| Prior residual | Effect of this bridge |
|---|---|
| 0-vs-pi ambiguity after real conjugation-invariant weighting | conditionally narrowed to `0` under pointwise nonnegative sector weights plus odd-sector support |
| partition positivity confusion | separated from pointwise positivity by explicit counterexample |
| theta selector target | restated as a physical sector-measure premise, not a generic record axiom issue |

## What Remains

The remaining theta wall is not closed by this note. The framework still needs:

- an emergent integer sector functional `Q`;
- nonzero odd-sector support if this selector is to distinguish `0` from `pi`;
- a physical bridge requiring the emergent sector weighting to be pointwise
  nonnegative as a record-facing probability measure;
- the gauge-action or scaling-limit bridge that supplies that sector surface;
- joint gauge/mass `theta_bar` assembly, including the physical quark-sector
  determinant and any chiral/anomaly bookkeeping needed for the invariant
  angle.

## Audit Consequence If Retained

The theta blocker should be restated from:

```text
choose 0 rather than pi on the real conjugation-invariant emergent-Q surface
```

to:

```text
derive an emergent integer Q with odd-sector support and a pointwise
nonnegative record-facing sector measure; then the finite selector chooses
theta = 0 from {0, pi}.
```

Rows that need only the conditional `0` selector may cite this bridge if its
premises are independently retained. Rows that need full Strong-CP closure
still need the emergent-`Q`, gauge-action, sector-measure, mass-side, and
joint-invariant bridges.

## Non-Claims

This note does not claim:

- `theta_gauge = 0` unconditionally;
- Strong-CP closure or Tier-A retirement;
- derivation of the emergent integer sector functional `Q`;
- proof that odd sectors exist or have nonzero physical weight;
- derivation of pointwise sector-measure positivity from the axioms;
- exclusion of sign-problem formulations outside the record-facing
  probability-measure surface;
- exclusion of spontaneous CP violation;
- derivation of the physical gauge action, quark determinant, anomaly
  Jacobian, metric scale, or observable bridge;
- use of PDG values, fitted constants, lattice-MC values, beta=6 values, or a
  new primitive.

## No-Go Discipline Gate

**Status:** PASS for bounded wall localization. This is not a terminal no-go.
It is a positive finite selector theorem with explicit conditional premises.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Reality-only route | Use real conjugation-invariant weights to force `theta = 0`. | RULED OUT BY PRIOR: the weighting bridge gives `{0, pi}`, not `0`. |
| Partition-positivity route | Use positivity of the total `Z(theta)` to select `0`. | RULED OUT BY PRIOR and reproven here by counterexample: `Z(pi)` can remain positive while odd-sector point weights are negative. |
| Pointwise sector-positivity route | Require each sector contribution to be a nonnegative record-facing probability weight. | ATTEMPTED here: succeeds conditionally when odd-sector support is nonzero. |
| Substrate no-carrier route | Use finite-lattice substrate connectedness and per-plaquette action class to make theta vacuous. | PARTIAL BY PRIOR: it removes the substrate carrier but relocates the wall to emergent `Q`. |
| Gauge-action minimality route | Derive a gauge action class that never leaves the real-positive/no-topological-slot surface. | OPEN: possible downstream route, not supplied by this note. |
| Determinant-reality transfer route | Transfer the mass-side K-real determinant mechanism to the gauge angle. | RULED OUT BY PRIOR: `theta_gauge` is a topological coupling, not a determinant phase. |
| New primitive route | Register pointwise sector-measure positivity or a theta selector as primitive. | OWNER-GOVERNANCE ROUTE: not used here because a bridge route remains live. |

### N2 - Wall-Independence Audit

Collapsed residual after this bridge:

```text
W_theta_sector =
  emergent integer Q with odd-sector support
  + physical pointwise nonnegative record-facing sector measure
  + joint gauge/mass theta_bar assembly.
```

The pieces are independent. An emergent `Q` does not by itself require
pointwise nonnegative theta-weighted sectors. Pointwise sector positivity does
not create `Q` or odd-sector support. Selecting the gauge-side member inside
`{0, pi}` does not assemble the invariant `theta_bar` with the mass side.

### N3 - Hidden-Wall Scan

"Pointwise nonnegative" is an explicit physical sector-measure premise, not an
axiom consequence. "Record-facing probability measure" means a later bridge has
identified the sector weights with record-readable probabilities. "Odd-sector
support" means at least one odd integer `Q` sector has positive weight. "CP-even
set `{0, pi}`" is inherited from the prior weighting bridge and is not reproven
as a universal continuum theorem here.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q...` | emergent `Q` remains open | preserved as part of `W_theta_sector` | yes |
| `THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE...` | `{0, pi}` remains open | this note attacks only the 0-vs-pi selector | yes |
| `STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT...` | partition positivity does not force `0` | preserved; pointwise positivity is stronger | yes |
| `STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION...` | gauge/mass invariant assembly remains open | preserved | yes |
| `WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE...` | real-positive action convention is bounded and scoped | related premise, not silently imported | yes |
| `RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE...` | probabilities arise after supplied selective interface | related probability surface, not silently imported | yes |

### N5 - Rhetoric Audit

The negative phrase is narrow: `theta = pi` is incompatible with pointwise
nonnegative sector weights when odd sectors have positive weight. This is a
sector-level statement, not a claim about the total partition function, every
continuous theta angle, every gauge-action formulation, or every possible
non-probability sign-weighted representation.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive emergent `Q` and odd-sector support from the scaling/gauge-action
  bridge;
- derive pointwise sector-measure positivity from a record-facing
  probability/instrument bridge;
- derive a gauge action surface that excludes topological sign weighting
  before the selector is needed;
- assemble the mass-side and gauge-side bridges into the invariant
  `theta_bar`;
- owner-promote a sector-measure or theta-selector primitive only if bridge
  routes fail and governance chooses that path.

### N7 - Steelman

A hostile reviewer can argue that this bridge is mostly a formal probability
surface choice: continuum theta formulations commonly tolerate complex or
sign-changing Euclidean weights, and `theta = pi` can be a meaningful CP-even
theory despite a sign problem. That objection is accepted as the boundary.
This note does not exclude sign-weighted formulations; it only says that if
the framework's emergent theta sector is required to be a pointwise
nonnegative record-facing probability measure, then `pi` is not admissible
when odd sectors have nonzero weight.

### N8 - Cross-Cycle Echo

Earlier theta notes overclaimed when they treated reality or positivity as
`theta = 0`. This bridge avoids that echo by separating total partition
positivity from pointwise probability positivity. The shape also matches the
recent record and source/action stack: broad dynamics language was split into
typed bridges, and only the finite part that actually follows is claimed.
