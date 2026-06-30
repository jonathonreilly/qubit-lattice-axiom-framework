# Record Occurrence Gate Factorization From Local Availability

**Date:** 2026-06-30
**Claim type:** bounded theorem / open-gate localization.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, or add a record-production axiom.
**Primary runner:**
[`scripts/record_occurrence_gate_factorization_from_local_availability_2026_06_30.py`](../scripts/record_occurrence_gate_factorization_from_local_availability_2026_06_30.py)

## Claim

On the 2026-06-29 axiom surface, plus the Record/Born interface bridge, the
record-production blocker narrows to one missing physical law:

```text
W_occurrence =
  a local record-extension law that says which unrecorded sites, if any, lock
  which available possibilities as records.
```

The current axioms supply:

```text
local possibilities
nearest-neighbor availability constraints
fixed records
finite additive readout of records
```

The Record/Born interface bridge supplies:

```text
supplied selective write interface + effect additivity
  -> Born trace weights and repeatable selective readout.
```

Neither layer supplies occurrence. Availability says what a site may record.
Record says what is fixed after recording. The Born interface says what weights
must look like once a selective measurement/effect interface is supplied. None
of those determines whether a site records, nor which available possibility is
locked in a particular extension.

## Factorization

A record-production theorem must supply three pieces, or derive them from a
stronger retained bridge:

1. **Activation:** which currently unrecorded sites, if any, are extended by a
   new record.
2. **Selection:** which available possibility is locked at each activated site.
3. **Preservation:** already fixed records remain fixed, and new records must
   respect admissibility.

The axioms supply the target type for item 3. They do not supply items 1 or 2.
That is the exact occurrence gate.

## Finite Witness

Use a three-site line with binary local possibilities `{0,1}` and the local
availability rule:

```text
a value is available at a site iff it differs from every neighboring record.
```

If the left neighbor has record `0` and the right neighbor is unrecorded, then
the middle site's available set is `{1}`. Two record extensions are still
consistent with the same axioms and the same availability rule:

```text
no activation:       middle site remains unrecorded
activation + select: middle site records 1
```

Admissibility has narrowed the possible value from `{0,1}` to `{1}`. It has
not forced the record to occur.

If both neighbors are unrecorded, the middle site's available set is `{0,1}`.
Again, several extensions are consistent:

```text
no activation
activation + select 0
activation + select 1
```

This is not a probabilistic ambiguity. It is a structural underdetermination:
the record-extension law has not been supplied.

## Relation To Born Weights

The Record/Born interface bridge narrows the probability side correctly. If a
selective interface supplies normalized effect-additive weights over a readout
context, the qubit algebra forces Born trace weights and repeatable selective
readout.

That still does not produce the occurrence token. A weight vector over available record values is not itself a realized durable record. It must feed a
record-extension law, an instrument, or another production mechanism that
actually locks one available possibility, or leaves the site unrecorded.

Thus the remaining wall is not "derive probability" in the broad sense. It is
the physical occurrence/activation law that converts an admissible possibility
surface, optionally with weights, into durable records.

## Minimum Bridge Shape

The clean minimum downstream bridge is not a broad Dynamics axiom. It is a
record-extension law with this shape:

```text
Given a finite record boundary and the current local possibility domains, a
local composable rule may extend the record set by locking available
possibilities at selected unrecorded sites. It never overwrites records and
never locks unavailable possibilities.
```

For physics use, a successful version must also say whether the rule is
deterministic, weighted, or instrument-based; how it composes across disjoint
regions; and what, if anything, normalizes occurrence rate. Those are bridge
targets, not hidden axiom content.

If the project wants this at the foundation level, the minimal axiom update
would be an **Occurrence / Record Extension** axiom of exactly this type. If the
project keeps the axiom base ontological, the same content should be built as a
retained bridge theorem rather than as an axiom.

## Audit Consequence If Retained

The record-production blocker should be restated from

```text
derive record production / probability / measurement dynamics
```

to the sharper gate:

```text
availability and Born-form interface are insufficient by themselves;
derive or supply a local record-extension law that activates sites and selects
available possibilities while preserving fixed records.
```

This gives downstream rows a precise dependency target. Rows that only need available values, Born-form weights, repeatable readout, or post-record counts
should not be blocked on occurrence. Rows that need actual new records, rates, stable production, or physical histories must cite the occurrence law.

## What This Does Not Claim

- It does not derive record occurrence.
- It does not derive a Hamiltonian, transfer operator, Markov generator, clock,
  rate, thermodynamic cost, or reset law.
- It does not derive Born weights from Record; it relies on the separate
  Record/Born interface bridge for the probability-form narrowing.
- It does not say all sites record, or that every available possibility is
  eventually recorded.
- It does not add a new axiom or primitive.
- It does not consume measured values, fitted constants, lattice-MC values, or
  beta=6 values.

## No-Go Discipline Gate

**Status:** PASS for the bounded boundary. This is not a terminal no-go against
record production. It is a factorization theorem plus an open-gate
localization.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Availability route | Use admissibility to force occurrence. | ATTEMPTED here: fails because the same available set admits no-activation and activation extensions. |
| Record durability route | Use fixed records to force future records. | RULED OUT BY TYPE: durability preserves existing records; it does not activate new ones. |
| Post-record count route | Use append/count grammar to produce the next atom. | RULED OUT BY PRIOR: post-record grammar consumes supplied atoms. |
| Born-interface route | Use Born trace weights to produce the actual token. | PARTIAL: weights are forced once the interface is supplied, but a weight vector is not the realized token. |
| Controlled-copy route | Use a finite pointer model to write records. | PARTIAL BY PRIOR: sufficient under bounded controlled-copy/fresh-fragment hypotheses, not axiom-level occurrence. |
| Total-record route | Declare every site recorded. | REJECTED BY TARGET: the framework allows some sites to remain unrecorded; total locking is a special production law, not ontology. |

### N2 - Wall Independence Audit

The collapsed residual is:

```text
W_occurrence = local activation + selection of available possibilities.
```

Availability does not imply activation. Activation without selection does not
pick a value when more than one possibility is available. Selection without
activation is not a record. Preservation is supplied only after records exist.

### N3 - Hidden-Wall Scan

"Activation" means extending the record set at a previously unrecorded site.
"Selection" means locking one available possibility. "Local" means controlled by
the neighborhood/record boundary declared by the bridge. None of those is read
back into Admissibility or Record.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `MINIMAL_AXIOMS_2026-06-29.md` | Admissibility is not record production | occurrence law remains | yes |
| `RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE...` | Born form closes only after supplied interface; occurrence remains | same `W_occurrence` | yes |
| `RECORD_PRODUCTION_KERNEL_BOUNDARY...` | post-record append/count does not identify producer | occurrence law remains | yes |
| `RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO...` | supplied context/generator/rate cannot be dropped | occurrence law needs generator/instrument if physical | yes |
| `RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED...` | baseline does not force record formation | same non-forcing boundary | yes |
| `RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT...` | finite controlled-copy suffices only under explicit hypotheses | possible bridge supplier, not axiom content | yes |

### N5 - Rhetoric Audit

The claim is not "records never occur" and not "probability is excluded." The
tested resolution is narrower: local availability plus fixed-record ontology
does not determine the record-extension relation.

### N6 - Partial-Closure Path Scan

This note identifies the import-retirement path:

```text
availability rule
  + selective interface / instrument
  + local activation-selection law
  -> produced durable record
  -> post-record history/readout
  -> audit review
```

No axiom expansion is required if the activation-selection law is later derived
as a bridge theorem.

### N7 - Steelman

A hostile reviewer can argue that the word "available" already implies a
transition opportunity, and a sufficiently strong reading of Admissibility
could include a record-extension relation. That would close this gate only by
changing the meaning of Admissibility. The current axiom memo explicitly says
Admissibility is not a dynamics axiom and does not provide a record-production
process, so the bridge must remain explicit unless the axiom is amended.

### N8 - Cross-Cycle Echo

Earlier record cycles repeatedly separated pre-record kernels, realized atoms,
and post-record counts. The Record/Born interface bridge narrowed the
probability-form side, but preserved occurrence as a named residual. This note
keeps that same layer split and turns the residual into the specific local
activation-selection gate.

## Verification

Run:

```bash
python3 scripts/record_occurrence_gate_factorization_from_local_availability_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=87 FAIL=0
```
