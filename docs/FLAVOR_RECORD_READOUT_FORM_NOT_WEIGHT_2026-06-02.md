# Flavor Record Readout Fixes Form Not Weight

**Date:** 2026-06-02
**Type:** open_gate
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not set, predict, or edit any audit outcome.
**Primary runner:** [`scripts/flavor_record_readout_form_not_weight_2026_06_02.py`](../scripts/flavor_record_readout_form_not_weight_2026_06_02.py)
**Runner cache:** [`logs/runner-cache/flavor_record_readout_form_not_weight_2026_06_02.txt`](../logs/runner-cache/flavor_record_readout_form_not_weight_2026_06_02.txt)
**No-promotion statement:** This source note creates no promotion, no registry
edit, no audit verdict, and no downstream status change; status remains owned
by the independent audit lane.

This source note translates the earlier qubit-to-record proposal into the
approved Lattice, Quantum, Record framework. It does not add or rename an
axiom. It records a form/weight separation.

## Result

The Record axiom supplies additive scalar record readout when a finite
record-readout surface has been specified. Conditional on a positive
multiplicative amplitude `Z` for independent subsystems, additive readout
selects a logarithmic form: `f(Z_A Z_B) = f(Z_A) + f(Z_B)`.

That is a form statement, not a Koide value statement and not a determinant
amplitude derivation. The Record axiom does not supply `Z = det(D + J)`,
Born weights, normalization, measurement dynamics, arbitrary observable
identification, or the within-`C^3` singlet/doublet measure.

For the Koide value, genuine `log|det H|` counts eigenvalue multiplicity:

```text
log|det H| = log|lambda_triv| + 2 log|lambda_doublet|.
```

The doublet is counted twice because it is two-dimensional. That is the
dimension-weighted `r=1` side. The `r=1/2` block-count reading instead needs
the multiplicity-stripped functional

```text
log|lambda_triv lambda_doublet|.
```

That is a different functional. Record additivity alone does not choose it.

## Consequence

Record readout can support the additive/log form gate once the multiplicative
amplitude and observable surface are supplied. It does not close the Koide
measure residual. The honest residual is still the reference-state or
block-measure choice: dimension count `(1:2)` versus sector count `(1:1)`.

## 2026-06-13 Downstream Boundary Alignment

The downstream occupancy-independence theorem
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
sharpens the Record boundary used here. Record supplies additive scalar form
only after a readout surface and multiplicative amplitude have been specified;
the live Record axiom also explicitly declines weighting, normalization,
probability, and occupancy-rule supply. The downstream theorem then exhibits
two consistent models:

- sector occupancy, which counts the doublet as two real slots and gives
  `r = 1`; and
- orbit occupancy, which counts the K/CPT orbit as one complex slot and gives
  `r = 1/2`.

Thus this row's open-looking "form not weight" residual is the same explicit
occupancy/slot-degree atom, not a second independent Record gate. The runner
checks this downstream alignment directly and still makes no adoption or
status claim.

## Dependencies

- [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
  (downstream occupancy/slot-degree boundary; bounded support).
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (Record axiom boundary and scope reference).

## No-Go Discipline Gate

This gate applies only to the narrow negative statement: Record readout does
not force the `r=1/2` Koide sector weight.

### N1 - Alternative route enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Additivity route | Use record additivity to force the full Koide value. | Narrows to form only: additivity selects log form after `Z` is supplied. |
| Genuine determinant route | Use `log|det H|` as the record functional. | Gives dimension multiplicity `(1:2)`, not block count `(1:1)`. |
| Block determinant route | Strip multiplicity and count each sector once. | Gives the desired block count but is a distinct functional. |
| Born coexistence route | Use pre-record normalization to settle post-record weights. | Does not select block count; pre/post-record ledgers can coexist. |
| Record axiom route | Treat Record as arbitrary observable identification. | Rejected by the approved axiom text; Record supplies additive scalar readout only. |
| Owner-admission route | Approve a block-measure or reference-state admission. | Possible future route, but not derived here. |

### N2 - Wall Independence

The collapsed residual for the Koide value is one measure/reference choice.
Log form and sector weighting are independent pieces; closing form does not
close weight.

### N3 - Hidden-Wall Scan

"Record" is used only as additive scalar readout. The note does not smuggle
log-det, determinant amplitude, Born weights, or block-measure selection into
the Record axiom.

### N4 - Residual Matching

The runner checks the actual residual: `log|det|` versus the
multiplicity-stripped block determinant. It does not claim to derive `Z`, the
physical source/action, or a reference state.

### N5 - Rhetoric Audit

The negative statement is restricted to the Koide weight. Record readout can
still be useful for additive/log form once the other gates are supplied.

### N6 - Partial-Closure Path Scan

A block-measure admission, a reference-state theorem, or an import-retirement
derivation could close the residual. Approved axioms and primitives
chain-satisfy dependencies but must not be cited as grade sources for that
closure.

### N7 - Steelman

A hostile reviewer can argue that records should count distinguishable record
labels rather than Hilbert-space multiplicity. That is a plausible block-count
principle, but it is an extra principle beyond additive scalar record readout.

### N8 - Cross-Cycle Echo

Prior flavor notes repeatedly split form gates from value gates. This note
keeps that split explicit: Record supports form, while the Koide measure
choice remains open.

**Gate result:** pass for the narrow form/weight separation only.
