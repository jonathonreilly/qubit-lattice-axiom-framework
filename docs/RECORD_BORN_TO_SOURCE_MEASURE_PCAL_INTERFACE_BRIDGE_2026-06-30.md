# Record/Born To Source-Measure P-Cal Interface Bridge

**Date:** 2026-06-30
**Claim type:** positive theorem candidate / bounded bridge theorem.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, or claim full source/action or Y_T closure.
**Primary runner:**
[`scripts/record_born_to_source_measure_pcal_interface_bridge_2026_06_30.py`](../scripts/record_born_to_source_measure_pcal_interface_bridge_2026_06_30.py)

## Claim

The Record/Born interface bridge supplies exactly the probability surface that
the source-measure P-cal stack needs:

```text
supplied selective record-writing interface + effect additivity
  -> Born trace weights on a finite sharp-record context
  -> finite record-facing probability law
  -> smooth source interventions are RN/log-normalizer interventions
  -> P-cal algebra closes at the record-facing interface layer.
```

This does not prove that a physical source/action deformation is that
record-facing probability intervention. It narrows the remaining source/action
wall to the physical identification:

```text
W_source_action =
  the physical source/action deformation is the record-facing RN/Fisher source
  coordinate, with the chosen physical source direction and action unit.
```

So the P-cal blocker is no longer an algebraic mystery once the measurement
interface is supplied. The remaining question is whether the physical source is
represented by that interface.

## Finite Theorem

Let `{P_r}` be a supplied finite sharp record context on the one-qubit carrier.
The Record/Born interface bridge gives

```text
p_r = Tr(rho P_r),     p_r >= 0,     sum_r p_r = 1.
```

For any full-support finite context and any record-facing source score `s(r)`,
define

```text
Z(h) = sum_r p_r exp(h s(r)),
P_h(r) = p_r exp(h s(r)) / Z(h),
R_h(r) = P_h(r) / p_r.
```

Then

```text
E_0[R_h] = 1,
log R_h(r) = h s(r) - log Z(h),
d log R_h(r)/dh |_(h=0) = s(r) - E_0[s],
W(h) = log Z(h)
```

and independent record contexts multiply their RN densities while their log
densities add.

If the score is centered and Fisher-unit normalized,

```text
E_0[s] = 0,     E_0[s^2] = 1,
```

then `W''(0) = 1`. A scaled source `lambda s` has Fisher norm `lambda^2`.
Thus the source-measure algebra selects the unit source only after the physical
source-unit identification is supplied; the finite RN calculus itself keeps
the scale visible.

## Relation To Existing Source-Measure Work

This bridge composes the new Record/Born interface with the existing
source-measure stack:

- `SOURCE_MEASURE_RECORD_INTERVENTION...` proves that finite sharp-record
  record-facing sources are smooth probability-law interventions.
- `SOURCE_MEASURE_PCAL_RN_COCYCLE...` proves the RN cocycle/log normalizer
  route.
- `SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS...` proves that `log Z` generates
  connected finite source responses.
- `SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE...` proves the Fisher tangent
  normalization surface.
- `SOURCE_MEASURE_LOG_SELECTION_BOUNDARY...` correctly says the physical unit
  scale is not fixed by finite record probability algebra alone.

The new contribution is the interface attachment:

```text
Record/Born finite weights are enough to instantiate the source-measure
probability surface.
```

The algebraic P-cal machinery therefore attaches at the supplied measurement
interface without adding probability to the axioms and without using
post-record counts as probability.

## Audit Consequence If Retained

The source/action blocker should split:

```text
closed at bounded interface layer:
  supplied Record/Born interface -> finite sharp-record probability law
  -> RN/log-normalizer source-measure calculus.

still open:
  identify the physical source/action deformation with that record-facing
  RN/Fisher source coordinate and with the physical source direction/unit.
```

Rows that only need the finite record-facing P-cal algebra can cite this
bridge plus the source-measure stack. Rows that need a physical top source,
source/action coefficient, action unit, pole-row response, metric readout, or
observable identification still need the physical source/action bridge.

## Relation To Record Occurrence

This theorem does not require a record to occur in a particular run. It is an
interface theorem about the probability law over possible records once a
selective record-writing interface is supplied.

Actual samples, histories, frequencies, and production rates still require the
occurrence gate:

```text
local activation + selection of available possibilities.
```

Thus P-cal at the interface layer is upstream of empirical frequency claims and
does not bypass record production.

## What This Does Not Claim

- It does not derive the selective record-writing interface.
- It does not derive record occurrence, IID trials, empirical frequencies, or
  convergence.
- It does not derive the physical source/action deformation.
- It does not identify the physical top source, top/W response, Higgs pole row,
  source direction, action unit, metric readout, or observable bridge.
- It does not derive Y_T, `y_33`, `y_t`, `m_t`, `v`, `g_2`, or running bridges.
- It does not use PDG values, fitted selectors, lattice-MC values, beta=6
  values, plaquette/u0 inputs, or a new primitive.

## No-Go Discipline Gate

**Status:** PASS for the bounded boundary. This is a positive interface bridge
with a named residual; it is not a no-go against source/action closure.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Post-record count route | Use realized counts to derive P-cal/probability. | RULED OUT BY PRIOR: counts are post-record data, not the pre-record law. |
| Record/Born interface route | Use supplied selective interface plus effect additivity to produce finite probabilities. | ATTEMPTED here: succeeds as the source-measure probability surface. |
| RN source route | Use smooth finite probability interventions to force log normalizer. | RULED OUT AS NEW WORK BY PRIOR / CONSUMED: existing source-measure theorem supplies it. |
| Raw `Z^p` route | Keep multiplicative raw powers as source generators. | RULED OUT BY PRIOR for connected/unit source response; scale remains visible until unit is supplied. |
| Planck/action route | Identify one physical action unit with the RN/Fisher coordinate. | OPEN: a possible physical source/action bridge, not supplied here. |
| Strict top/W response route | Fix source unit through same-source physical response. | OPEN: downstream physical-source route. |

### N2 - Wall Independence Audit

Collapsed residual after this note:

```text
W_source_action =
  physical source/action deformation = record-facing RN/Fisher coordinate
  with a physical source direction and unit.
```

This is independent of the algebraic RN/log-normalizer machinery. Closing the
interface algebra does not identify the physical source. Conversely, a physical
source/action theorem would consume this interface rather than replace it.

### N3 - Hidden-Wall Scan

"Supplied selective interface" means the interface of the Record/Born bridge.
"Record-facing" means operationally visible only through probabilities of
sharp record outcomes. "Physical source/action" is not assumed; it is the named
residual.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE...` | Born form after supplied interface; occurrence remains | supplies finite probability law | yes |
| `RECORD_OCCURRENCE_GATE_FACTORIZATION...` | occurrence remains activation + selection | preserved; not needed for interface algebra | yes |
| `SOURCE_MEASURE_RECORD_INTERVENTION...` | record-facing sources are probability interventions | consumed interface theorem | yes |
| `SOURCE_MEASURE_PCAL_RETIREMENT_SYNTHESIS...` | P-cal reduces to physical source bridge | same residual after interface attachment | yes |
| `SOURCE_MEASURE_LOG_SELECTION_BOUNDARY...` | finite RN algebra does not fix physical unit alone | physical unit residual preserved | yes |
| `SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT...` | Planck/action unit route is conditional | possible downstream bridge, not consumed as closure | yes |

### N5 - Rhetoric Audit

The claim is not "source/action is derived" and not "Y_T is closed." The tested
resolution is the supplied finite record-facing probability interface. The
physical source/action deformation remains outside the theorem.

### N6 - Partial-Closure Path Scan

This note identifies the import-retirement path:

```text
Record/Born interface
  + source-measure RN/log-normalizer stack
  + physical source/action identification
  -> source/action coefficients on the selected physical source surface.
```

No axiom expansion is required by the interface bridge.

### N7 - Steelman

A hostile reviewer can say this bridge merely rephrases the existing
source-measure theorem after assuming a measurement interface. That objection
is partly right: the RN/log-normalizer algebra is not new. The new claim is
the precise attachment point after the axiom reset and Record/Born bridge. It
keeps source/action physical identification as a residual instead of claiming
that record probability algebra alone closes it.

### N8 - Cross-Cycle Echo

Earlier source/action cycles overclaimed when they treated finite probability
normalization, Planck scale, or record additivity as the physical source unit.
This bridge preserves the corrected layer split: Record/Born supplies the
probability interface; source-measure algebra supplies log/RN calculus; physical
source/action identification remains an explicit downstream bridge.

## Verification

Run:

```bash
python3 scripts/record_born_to_source_measure_pcal_interface_bridge_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=78 FAIL=0
```
