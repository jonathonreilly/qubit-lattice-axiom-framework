# AC_phi_lambda r=1/2 Recorded-Value Target After The Dirac Bridge

**Date:** 2026-06-30
**Claim type:** source-side reduction map / conditional theorem target.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, adopt a readout bridge, or claim AC_phi_lambda retirement.
**Primary runner:**
[`scripts/acphilambda_r_half_recorded_value_target_2026_06_30.py`](../scripts/acphilambda_r_half_recorded_value_target_2026_06_30.py)

## Claim

The next `AC_phi_lambda` target should not be "force `r = 1/2` everywhere."
That is too strong and wrong for the record ontology.

The correct target is context-local:

```text
If a charged-lepton two-outcome record context exists, and repeated readout of
that record composes by the records-flow update, then a durable recorded value
must be a fixed point of that update. Under the charged-lepton 2-sector
dictionary, the nondegenerate unsigned fixed point is r = 1/2.
```

This respects sparse records. The framework does not say every site is recorded,
that every possibility actualizes, or that every physical context records the
same cell. It says a record, once present, is fixed under repeated readout. The
`r = 1/2` question should therefore be asked as a durable-record question inside
the charged-lepton context, not as a global occurrence law.

## Algebraic Core

Let the two readable charged-lepton outcomes be the singlet outcome `s` and the
doublet-orbit outcome `d`. Write their record-weight ratio as:

```text
x = p_d / p_s.
```

The existing records-flow/Lueders sharpening surface gives:

```text
x -> x^2.
```

Durability under repeated readout means the recorded value is unchanged by
re-reading the record. Therefore a durable recorded value must satisfy:

```text
x = x^2.
```

The finite fixed values are `x = 0` and `x = 1`; the projective endpoint is
`x = infinity`. The charged-lepton lane excludes the endpoints by its own
recorded content:

- `x = 0` is the degenerate no-breaking endpoint;
- `x = infinity` is the signed/projective endpoint, not the unsigned positive
  charged-lepton branch.

So the only nondegenerate unsigned durable value is:

```text
x = 1.
```

On the existing charged-lepton two-sector dictionary,

```text
x = 2r,
```

so the durable recorded value is:

```text
r = 1/2,     Q = 1/3 + (2/3)r = 2/3.
```

This is not a probability derivation. It is fixed-record idempotence applied to
the supplied two-outcome record context.

## What The Dirac Bridge Changes

Before #4748, part of the `r` residual was still entangled with whether the
framework could even reach the first-order staggered/Dirac branch. After the
strict nearest-neighbor composition bridge, that kinetic-order shortage is no
longer the right place to park the `r` blocker.

The remaining `r` problem is sharper:

1. **Kinetic branch:** supplied by strict nearest-neighbor composition if #4748
   is retained.
2. **First-order matter determinant:** supported on the staggered surface by the
   one-component Grassmann/Berezin calculation, but still conditional on the
   statistics/readout surface it names.
3. **Recorded-value selection:** supplied only if the charged-lepton record
   context uses the records-flow durability/readout-idempotence bridge.

Thus the live issue is no longer "find Dirac." It is:

```text
Can Record's repeated-readout invariance, plus the finite Lueders/PEP
compression support, be promoted into the records-flow durability bridge for
this two-outcome context without adding a broad probability or measurement
axiom?
```

If yes, `r = 1/2` becomes a conditional recorded-value theorem for the
charged-lepton context. If no, the exact missing input is the narrow R-D/readout
idempotence bridge, not a broad Dynamics axiom and not a universal `r = 1/2`
law.

## What Is Not Being Claimed

- No claim that all sites are recorded.
- No claim that all available possibilities actualize.
- No claim that every physical context has `r = 1/2`.
- No global exclusion of the `r = 1` sector cell; existing notes already treat
  it as a valid cell in other contexts.
- No derivation of the physical charged-lepton readout context, species bridge,
  R-eta, theta, Born weights, probability, or record-production dynamics.
- No use of PDG masses or fitted values.

## Minimum Remaining Work

For the `r = 1/2` atom, the minimum clean closure path is:

```text
#4747 axioms
  + #4748 strict nearest-neighbor composition
  + retained staggered/Grassmann first-order determinant surface
  + charged-lepton two-outcome record context
  + records-flow durability/readout-idempotence bridge
  -> durable recorded value x = 1
  -> r = 1/2 in the charged-lepton dictionary
```

The only part this note identifies as still bridge-like is the last readout
idempotence step. It is local to recorded contexts. It does not need to force
record occurrence.

## No-Go Discipline Gate

**Status:** PASS for the narrow negative claim only: the target should not be
phrased as universal forcing of `r = 1/2`. This is not a no-go against deriving a
charged-lepton recorded-value theorem.

### N1 - Alternative Route Enumeration

| Route | Marker | Result |
|---|---|---|
| Universal `r = 1/2` law | ATTEMPTED by scope analysis | Too strong: it conflicts with sparse records and with valid non-charged-lepton cells. |
| Realized-state registration | RULED OUT BY PRIOR as full closure | Correctly classifies lane values as registered, but does not explain exact durable placement. |
| Strict-NN/Dirac kinetic bridge | PARTIAL | Removes kinetic-order shortage, but does not supply record readout idempotence or the charged-lepton context. |
| First-order determinant route | PARTIAL | Supports the count-once surface, but prior notes still leave the physical horn/readout bridge open. |
| Records-flow durability route | LIVE | Gives `r = 1/2` conditionally when the two-sector dictionary and readout-idempotence bridge are supplied. |
| R-eta/species routes | NOT THIS ATOM | They remain separate AC_phi_lambda atoms. |

### N2 - Wall Independence

The collapsed residuals for this atom are:

```text
W_context = charged-lepton two-outcome record context / dictionary
W_update  = records-flow durability or readout-idempotence bridge
W_stats   = retained statistics/readout surface for the first-order determinant
```

Closing `W_update` does not supply the context. Closing `W_context` does not
supply the update map. Closing `W_stats` does not supply record idempotence.

### N3 - Hidden-Wall Scan

"Recorded value" means a record already exists; it does not smuggle occurrence.
"Repeated readout" uses the Record axiom's fixedness clause, but the update map
is named as a bridge. "Two-outcome context" is supplied downstream context, not
generic axiom content.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `KOIDE_R_IS_THE_WEIGHTING_PRINCIPLE_DIAL...` | `r` is a weighting dial, not selected by record-preserving dynamics | universal forcing is wrong | yes |
| `OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY...` | fixed outcome ratio needs a dictionary to read as `r` | `W_context` | yes |
| `KOIDE_R_HALF_DURABILITY_STATIONARITY...` | R-D + side conditions gives unique durable `r = 1/2` | `W_update` closure route | yes |
| `KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT...` | first-order determinant reached, horn still open | `W_stats` partial route | yes |
| `OCCUPANCY_NONEXCLUSIVITY...` | no global exclusion of `r = 1` | avoid universal forcing | yes |

### N5 - Rhetoric Audit

The note avoids "the framework derives `r = 1/2`" as a global sentence. The
narrow sentence is: under a supplied charged-lepton record context and
records-flow durability bridge, the nondegenerate unsigned durable recorded
value is `r = 1/2`.

### N6 - Partial-Closure Path Scan

The closure path is a bridge theorem, not a new axiom: derive or approve
readout idempotence for the two-outcome record context using Record fixedness
plus the finite Lueders/PEP compression support. If that fails, the missing item
is named exactly as `W_update`.

### N7 - Steelman

A hostile reviewer can argue that the current note still consumes the
charged-lepton dictionary and Lueders-style update surface, so it has not
retired the Tier-A atom. That objection is correct. This note is a target
reframe and residual localization, not a retirement.

### N8 - Cross-Cycle Echo

Prior Koide `r` cycles repeatedly failed by trying to select a global weight,
static polarization, or sector occupancy directly. The strongest surviving
route is record-local: durable repeated readout fixes an existing record rather
than forcing every possible record to occur.

## Verification

Run:

```bash
python3 scripts/acphilambda_r_half_recorded_value_target_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=57 FAIL=0
```
