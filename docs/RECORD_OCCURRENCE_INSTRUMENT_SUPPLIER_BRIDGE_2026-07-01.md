# Record Occurrence Instrument Supplier Bridge

**Date:** 2026-07-01
**Claim type:** bounded bridge theorem / occurrence supplier normal form.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
that physical record production is derived from the ontology alone.
**Primary runner:**
[`scripts/record_occurrence_instrument_supplier_bridge_2026_07_01.py`](../scripts/record_occurrence_instrument_supplier_bridge_2026_07_01.py)

## Claim

The occurrence wall has a clean positive bridge surface.

Given:

```text
a finite record boundary,
an unrecorded site with available possibilities A_x,
and a supplied finite record-writing instrument with outcomes
  {no record at x} union {record v at x : v in A_x},
```

the instrument supplies exactly the local record-extension kernel required by
the occurrence normal form:

```text
activation a_x = probability that the instrument writes a record,
selection p_x(v) = conditional probability of value v given activation,
preservation = existing records are not overwritten and unavailable values are
not written.
```

Thus a retained physical instrument or trigger would close the activation and
selection duties of `W_occurrence` on its declared site/context. What remains
open is not the kernel algebra. It is the physical derivation or approval of
the record-writing instrument, trigger, pointer/readout, and any clock or rate
normalization.

This is a bridge theorem, not an ontology update.

## Finite Theorem

Let `rho` be a finite pre-record state and let a supplied local instrument have
positive effects

```text
E_bot,  {E_v : v in A_x}
```

with

```text
E_bot + sum_{v in A_x} E_v = I.
```

The probability kernel over possible record-extension outcomes is

```text
K_x(bot) = Tr(rho E_bot),
K_x(v)   = Tr(rho E_v).
```

Completeness gives normalization, positivity gives nonnegativity, and the
declared outcome set prevents unavailable values from being written.

Define

```text
a_x = sum_{v in A_x} K_x(v) = 1 - K_x(bot).
```

If `a_x > 0`, define

```text
p_x(v) = K_x(v) / a_x.
```

Then the kernel has the occurrence normal form:

```text
K_x(bot) = 1 - a_x,
K_x(v)   = a_x p_x(v).
```

If `a_x = 0`, no record is written and no selection distribution is used. If
`A_x` is empty, the only admissible instrument surface is `E_bot = I`, so
`a_x = 0`.

For disjoint sites with independent supplied instruments, the joint kernel is
the product of the local kernels. This preserves fixed records sitewise and
does not write unavailable values at any site.

## Explicit Lazy-Instrument Witness

On a two-value available set `A_x = {0,1}`, take

```text
rho = diag(3/5, 2/5),
q = 1/4,
E_bot = (1 - q) I,
E_0   = q |0><0|,
E_1   = q |1><1|.
```

Then

```text
K(bot) = 3/4,
K(0)   = 3/20,
K(1)   = 1/10.
```

So

```text
a = 1/4,
p(0) = 3/5,
p(1) = 2/5.
```

The same construction has a deterministic-recording special case at `q = 1`
and a no-record special case at `q = 0`. A one-value available set, for
example `A_x = {0}`, uses

```text
E_bot = I - q |0><0|,
E_0   = q |0><0|
```

and writes only value `0`; value `1` is not an outcome and cannot be locked.

## Relation To The Pointer Record Bridge

The finite pointer/non-demolition theorem supplies a bounded example of a
record-writing instrument under explicit hypotheses: a conserved pointer,
nonzero controlled-copy coupling, local fragments, and a recording time or
fresh/idle fragment condition. On that supplied surface, the instrument is not
merely a probability table; it writes a durable pointer record.

This note composes that supplier shape with the newer occurrence normal form.
It does not derive the pointer, the coupling, the physical trigger, or the
clock from the four ontology axioms.

## What Moves

| Prior residual | Effect of this bridge |
|---|---|
| occurrence as an unspecified production layer | reduced to a supplied finite instrument/trigger surface |
| activation `a_x` | supplied by the total non-`bot` instrument probability |
| selection `p_x(v)` | supplied by conditional instrument outcome weights |
| unavailable-value risk | blocked by the declared instrument outcome set `A_x` |
| preservation of records | enforced by applying the write only to unrecorded sites |
| disjoint-region composition | inherited from product composition of independent local instruments |

## What Remains

The framework still needs a physical bridge that derives or supplies:

- which local record-writing instrument is physical;
- which pointer/readout the instrument records;
- the trigger or activation parameter;
- a clock or rate normalization, if rates or histories per unit time are
  claimed;
- redundant broadcast or local objectivity, if multi-observer objective
  records are required.

Those are physical instrument/production questions. They are not solved by
the kernel algebra alone.

## Audit Consequence If Retained

Rows that need actual record production can use the following dependency
shape:

```text
local record-extension kernel normal form
  + supplied physical record-writing instrument/trigger
  -> activation + conditional selection + preservation.
```

Rows that have only availability, record durability, Born conditional weights,
or post-record history grammar still must keep `W_occurrence` explicit. Rows
that cite a retained physical instrument may reduce the local occurrence wall
to the instrument's own premises and rate/objectivity boundaries.

## Non-Claims

This note does not claim:

- the ontology axioms derive a physical instrument;
- records always occur;
- every available possibility eventually records;
- every site records;
- Born weights are excluded;
- the pointer/non-demolition bridge is unconditionally derived;
- local objectivity, decoherence, time, rate, metric, source/action,
  theta, or observable semantics are closed;
- measured constants, fitted values, lattice-MC values, or a new primitive are
  used.

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this theorem.

If bridge-first routes fail, the minimum foundation update remains the narrow
operational primitive candidate already isolated by the primitive-update
recommendation:

```text
P_record_extension:
  Given a record boundary and available local possibilities, a local
  composable record-extension law may lock one available possibility at
  selected unrecorded sites while preserving existing records.
```

This bridge shows what such a primitive or theorem must supply operationally:
a physical instrument/trigger whose kernel exposes activation, conditional
selection, preservation, and any rate or objectivity content claimed.

## No-Go Discipline Gate

**Status:** PASS for bounded wall localization inside a positive bridge. This
is not a terminal no-go and not a claim that a physical record-writing
instrument cannot be derived. It says only that the finite instrument algebra
closes the occurrence kernel once the instrument/trigger is supplied.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Availability-only route | Use admissibility to produce the record. | RULED OUT BY PRIOR: availability supplies support, not activation. |
| Born-weight route | Use conditional Born weights as the whole occurrence law. | PARTIAL: this bridge can use them as selection weights, but activation still comes from the instrument/trigger. |
| Post-record history route | Use append/count grammar to make the next record. | RULED OUT BY PRIOR: append/count consumes supplied atoms. |
| Supplied-instrument route | Use a finite record-writing instrument to produce a kernel and realized atom. | ATTEMPTED here: succeeds as a bounded bridge once the instrument is supplied. |
| Controlled-copy pointer route | Use non-demolition pointer dynamics to supply such an instrument. | PARTIAL BY PRIOR: sufficient under explicit finite hypotheses, not derived from ontology alone. |
| Markov/transfer route | Derive the same kernel from a local generator or transfer step. | OPEN: possible future supplier of the instrument/trigger and rate. |
| New primitive route | Register occurrence as an approved operational primitive. | OWNER-GOVERNANCE ROUTE: available only if bridge-first routes fail or are intentionally bypassed. |

### N2 - Wall-Independence Audit

Collapsed residual after this bridge:

```text
W_record_instrument =
  physical selection or derivation of the record-writing instrument/trigger,
  including pointer/readout and any rate or objectivity content claimed.
```

Once that wall is closed for a declared site/context, activation and selection
are not independent residuals: they are the non-`bot` mass and conditional
weights of the same instrument kernel. Rate and objectivity remain separate
only when the downstream row claims rates or multi-observer records.

### N3 - Hidden-Wall Scan

"Supplied instrument" is an explicit bridge input, not hidden axiom content.
"Physical" marks the remaining supplier wall, not an assumption made by this
note. "Pointer/readout" is inherited only if a retained pointer or instrument
theorem supplies it. "Local" means the declared site or disjoint site family
and its available possibility set.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30` | physical kernel values/rules remain. | instrument supplies kernel values once retained. | yes |
| `RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01` | activation not derived from availability/Born weights. | activation comes from supplied instrument trigger. | yes |
| `RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05` | supplied instrument gives probability kernel and realized atom interface. | same supplier type. | yes |
| `RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05` | produced record needs realized atom and durability. | preserved as instrument/pointer boundary. | yes |
| `RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT...` | controlled-copy forms records under explicit finite hypotheses. | bounded supplier route. | yes |
| `RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30` | Born form after supplied interface; occurrence remains. | Born weights can be selection, not trigger. | yes |
| `MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01` | `P_record_extension` is fallback, not registered. | same fallback if instrument bridge fails. | yes |

### N5 - Rhetoric Audit

The negative boundary is narrow: instrument algebra is not physical
instrument derivation. It is tested at the finite one-site and disjoint-site
product-kernel resolutions. The note does not say records never form, and it
does not claim that Markov, transfer, source/action, pointer, or instrument
routes fail.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive the physical instrument/trigger from a local Markov or transfer
  generator;
- derive it from a retained controlled-copy or pointer broadcast theorem;
- derive it from a source/action or metric/observable response theorem;
- accept a bounded instrument for a named experimental/record context;
- explicitly approve and register `P_record_extension` if owner governance
  chooses primitive occurrence rather than bridge-first derivation.

The primitive-registry check confirms that no current approved primitive
already grants a physical record-writing instrument or trigger.

### N7 - Steelman

A hostile reviewer can say this theorem is still only interface algebra:
given an instrument, every measurement text can define a probability kernel,
so the real physics is entirely in deriving the instrument, pointer, and
trigger. That objection is correct and preserved. The value of this bridge is
that it removes activation/selection ambiguity once a physical instrument is
available; it does not pretend to derive the instrument.

### N8 - Cross-Cycle Echo

Prior record-dynamics notes repeatedly separated kernels from tokens, post-
record histories from production, and pointer non-demolition from actual
record formation. This note keeps that split: the instrument supplies the
kernel and can produce an atom only on its declared physical surface, while
the ontology axioms and generic Born weights still do not produce records by
themselves.

## Verification

Run:

```bash
python3 scripts/record_occurrence_instrument_supplier_bridge_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=114 FAIL=0
```
