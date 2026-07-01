# Minimal Operational Primitive Update Recommendation

**Date:** 2026-07-01
**Claim type:** bounded foundation-update recommendation / bridge-first
decision note.
**Status authority:** independent audit lane and owner governance only. This
note does not set an audit verdict, edit registries, register primitives,
change axioms, or claim terminal closure.
**Primary runner:**
[`scripts/minimal_operational_primitive_update_recommendation_2026_07_01.py`](../scripts/minimal_operational_primitive_update_recommendation_2026_07_01.py)

## Claim

After the current post-axiom bridge stack, no further broad ontology axiom is
justified by the evidence.

The four ontology axioms should remain:

```text
Lattice
Qubit / Local Possibility
Admissibility / Local Constraint
Record
```

The remaining hard gates are operational. Bridge-first work should continue.
If bridge derivations fail or owner governance chooses a foundation update, the
minimal update is not another "dynamics" axiom. It is a small set of approved
operational primitives, each with a named physical job and a narrow boundary.

The collapsed candidate set is:

```text
P_readout_selection
P_record_extension
P_physical_source
P_gauge_sector_measure
P_metric_observable
```

These are fallback primitive candidates, not primitive registrations in this
note.

## Why Not Change The Four Ontology Axioms

The current axioms supply the ontology:

```text
physical lattice locality
local possibility
admissible availability
fixed readable records
```

The open gates do not show that this ontology is internally inconsistent or too
weak as ontology. They show that downstream physics needs operational rules:
which readout is physical, when records occur, which source is physical, which
sector measure is physical, and how record/source quantities become measured
metric observables.

Adding those jobs to Lattice, Qubit, Admissibility, or Record would blur the
ontology/operation boundary and recreate the old laundering problem. If a
foundation update is needed, it should be explicit primitive registration.

## Candidate Primitive Text

### 1. Physical Readout Selection

```text
In a supplied finite record context, a physical scalar readout is selected by a
local covariant map from specified record/context invariants to scalar record
values. The selector must name the context, invariant class, unit convention,
and equivalence boundary.
```

Boundary:

```text
This primitive does not say every invariant is readable, does not produce
records, does not assign probabilities, and does not choose a source/action,
metric, gauge sector, or empirical comparator.
```

First target:

```text
the physical charged-lepton phase readout is the direct local scalar readout of
the selected C3 edge defect.
```

Effect if approved or derived:

```text
P_readout_selection
  + phase-defect normal form
  -> |delta| = L3(1,2) = 2/9
```

### 2. Record Extension / Occurrence

```text
Given a record boundary and available local possibilities, a local composable
record-extension law may lock one available possibility at selected unrecorded
sites while preserving existing records.
```

Boundary:

```text
This primitive must expose activation, selection, and rate/instrument content.
It never overwrites records, never locks unavailable possibilities, and does
not force every site to record.
```

Effect if approved or derived:

```text
P_record_extension
  -> actual record histories, occurrence rates, and empirical frequency
     bridges can be stated without treating availability as production.
```

### 3. Physical Source Selector

```text
On a supplied finite record-facing RN/action surface, a physical source
selector identifies the physical action-exponent direction and unit for a
named source deformation.
```

Boundary:

```text
This primitive does not derive the RN/action algebra, does not produce records,
does not select a metric, and does not by itself identify a measured
observable. It only selects the physical source direction and unit on a named
surface.
```

Effect if approved or derived:

```text
P_physical_source
  + source/action RN factorization
  -> physical source/action coefficients can attach to the record-facing
     source calculus.
```

### 4. Gauge-Sector Measure

```text
On an emergent gauge-sector surface, a physical sector-measure primitive
supplies the integer sector label, the pointwise record-facing sector measure,
and the assembly rule for the joint gauge/mass invariant angle.
```

Boundary:

```text
This primitive does not insert a bare theta slot into the substrate, does not
derive the gauge action, and does not exclude sign-weighted formulations
outside the declared record-facing sector-measure surface.
```

Effect if approved or derived:

```text
P_gauge_sector_measure
  + theta pointwise sector selector
  -> theta = 0 from {0, pi} when odd-sector support is nonzero, and supplies
     the missing theta_bar assembly surface.
```

### 5. Metric / Observable Bridge

```text
Given a supplied causal/record/source-response surface, a physical
metric-observable bridge identifies the clock-rate/conformal factor and maps
record/source quantities to measured observables with units.
```

Boundary:

```text
This primitive does not supply new dimensionless constants, does not derive the
scale-reference primitive, and does not turn every scalar record into a
measured observable.
```

Effect if approved or derived:

```text
P_metric_observable
  + conformal-class / source-response bridges
  -> physical metric scale and measured-observable semantics can attach to
     otherwise dimensionless record/source results.
```

## Priority

The recommended order is:

1. **Physical Readout Selection**: highest leverage for `AC_phi_lambda` because
   the phase-defect normal form has already collapsed the remaining phase gate
   to this atom.
2. **Record Extension / Occurrence**: required for histories, rates,
   frequencies, and measurement events.
3. **Physical Source Selector**: required for source/action coefficients and
   source-normalized predictions.
4. **Gauge-Sector Measure**: required for full theta closure.
5. **Metric / Observable Bridge**: required for measured metric scale and
   observable semantics.

## Audit Consequence If Adopted

If owner governance adopts any candidate, it should be added as an approved
framework primitive with:

- exact primitive wording;
- explicit boundaries;
- a source note;
- a verifier;
- registry entry in `docs/audit/data/axiom_premise_nodes.json`;
- no change to the four ontology axioms unless the project intentionally
  abandons the ontology-only axiom policy.

Until then, downstream claims must treat these as open bridge targets, not
usable as premises until adopted.

## No-Go Discipline Gate

**Status:** PASS for a bounded update recommendation. This is not a terminal
no-go against deriving the bridges. It says only that the current evidence does
not justify a broad ontology axiom and that any foundation update should be one
of the named operational primitive shapes.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| More-ontology route | Add a broad dynamics/process axiom to Lattice/Qubit/Admissibility/Record. | REJECTED FOR NOW: the residuals split into named operational jobs rather than one ontology defect. |
| Readout-selection route | Derive the physical charged-lepton phase readout from the selected C3 defect. | OPEN: #4760 gives the normal form but leaves physical selection. |
| Occurrence route | Derive actual record production from availability/Born interface. | OPEN: local extension-kernel normal form exists, physical kernel/rate remains. |
| Source route | Derive physical source direction/unit on the RN/action surface. | OPEN: RN/action factorization exists, physical source selector remains. |
| Theta route | Derive emergent Q, pointwise sector measure, and theta_bar. | OPEN: pointwise selector exists only after those premises. |
| Metric/observable route | Derive clock rate and measured observable semantics from record/source surfaces. | OPEN: conformal class and weak-field responses are conditional; scale/observable semantics remain. |
| New primitive route | Register narrow operational primitives. | OWNER-GOVERNANCE ROUTE: recommended only if bridge-first derivations fail or are intentionally bypassed. |

### N2 - Wall Independence Audit

Collapsed wall set:

```text
P_readout_selection
P_record_extension
P_physical_source
P_gauge_sector_measure
P_metric_observable
```

These are independent at the current bridge surface. A readout selector does
not produce records. Record occurrence does not choose source direction. Source
direction does not create gauge sectors. Gauge-sector measure does not identify
metric clock rate. Metric/observable semantics do not select the C3 phase
readout.

### N3 - Hidden-Wall Scan

"Primitive" means a future approved framework primitive, not a premise in this
note. "Physical" marks the missing operational selection, not an assumption.
"Supplied" means provided by an independently retained bridge or by explicit
future primitive registration. "Bridge-first" means these candidates should not
be used as premises until adopted.

### N4 - Residual Matching

| Witness | Residual there | Candidate here | Match |
|---|---|---|---|
| `ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM...` | `W_defect_readout_selection` | `P_readout_selection` | yes |
| `LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM...` | physical kernel/rate remains | `P_record_extension` | yes |
| `SOURCE_ACTION_RN_FACTORIZATION...` | physical source direction/unit | `P_physical_source` | yes |
| `THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR...` | emergent Q, sector measure, theta_bar | `P_gauge_sector_measure` | yes |
| `EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS...` | clock-rate/conformal factor | `P_metric_observable` | yes |
| `OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO...` | Record does not choose scalar map | `P_readout_selection` / `P_metric_observable` | yes |

### N5 - Rhetoric Audit

The claim is not that bridge derivations are impossible. It is only that, if
foundation updates are needed, the updates should be explicit operational
primitives rather than hidden content inside the ontology axioms. The statement
is scoped at the audit-dependency level, not as a mathematical impossibility
theorem.

### N6 - Partial-Closure Path Scan

Live bridge-first paths remain:

- derive C3 readout selection from a record-facing covariant phase-readout
  theorem;
- derive occurrence from an instrument, Markov generator, or local transfer
  rule;
- derive physical source direction/unit from same-surface response;
- derive emergent gauge-sector measure from gauge action/scaling;
- derive metric/observable semantics from clock-rate/source-response bridges.

If any path closes, the corresponding primitive candidate should be removed or
reduced before governance action.

### N7 - Steelman

A hostile reviewer can argue that a single future local action principle might
derive occurrence, source/action, probability, metric clock rate, and readout
selection together. That objection is strong. This note does not deny that
possibility; it is why bridge-first remains the recommended policy. The
candidate primitive list is a fallback governance map, not a claim that the
listed primitives are unavoidable.

### N8 - Cross-Cycle Echo

Earlier cycles overclaimed when they folded readout selection, occurrence,
source normalization, or metric semantics into Record or generic dynamics
language. The current stack improved that by splitting the residuals into
typed gates. This note preserves the split and names only the minimum
operational primitive shapes to consider if bridge derivations fail.

## Verification

Run:

```bash
python3 scripts/minimal_operational_primitive_update_recommendation_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=106 FAIL=0
```
