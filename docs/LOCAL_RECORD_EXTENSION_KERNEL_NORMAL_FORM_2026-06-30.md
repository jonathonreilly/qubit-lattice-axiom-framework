# Local Record-Extension Kernel Normal Form

**Date:** 2026-06-30
**Claim type:** bounded theorem / occurrence-law normal form.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit the Tier-A registry, register a primitive, refresh generated
ledgers, or claim record production is derived from the axioms.
**Primary runner:**
[`scripts/local_record_extension_kernel_normal_form_2026_06_30.py`](../scripts/local_record_extension_kernel_normal_form_2026_06_30.py)

## Claim

The occurrence gate isolated by
[`RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md`](RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md)
has a clean finite normal form.

For an unrecorded site with available possibilities `A_x`, a one-step local
record-extension kernel has outcome set

```text
{no record at x} union {record v at x : v in A_x}.
```

Every normalized kernel on that set factors uniquely as

```text
activation probability a_x
selection probability p_x(v) over A_x, conditional on activation
```

with

```text
K_x(no record) = 1 - a_x,
K_x(record v) = a_x p_x(v).
```

For pairwise disjoint sites or regions with no shared admissibility boundary,
composability is exactly product composition of these local kernels. Thus the
minimum occurrence law is not a broad dynamics axiom. It is a local
record-extension kernel with three explicit duties:

1. activate some unrecorded sites, possibly none;
2. select only available possibilities at activated sites;
3. preserve all existing records.

The theorem does not supply the physical values of `a_x`, `p_x`, a clock, a
rate, a Hamiltonian, or an instrument. It supplies the normal form any such
local occurrence bridge must satisfy.

## Finite Theorem

Let `A_x` be the finite set of available possibilities at an unrecorded site
`x`. Add a no-event symbol `bot`. A local record-extension kernel is a
probability distribution

```text
K_x on {bot} union A_x
```

such that

```text
sum_o K_x(o) = 1,
K_x(o) >= 0.
```

Define

```text
a_x = 1 - K_x(bot).
```

If `a_x > 0`, define

```text
p_x(v) = K_x(v) / a_x,  v in A_x.
```

If `a_x = 0`, no selection distribution is used. Then

```text
K_x(bot) = 1 - a_x,
K_x(v) = a_x p_x(v).
```

The factorization is unique whenever `a_x > 0`. If `A_x` is empty, the only
admissible kernel has `K_x(bot)=1`.

For disjoint sites `x_1,...,x_n`, composability means the joint extension
kernel is

```text
K(o_1,...,o_n) = product_i K_x_i(o_i).
```

This joint kernel normalizes, never records unavailable values, and preserves
the already-recorded boundary because every local factor is defined only on
`{bot} union A_x`.

## Relation To Availability And Born Weights

Availability supplies the allowed support `A_x`. It does not supply
activation or selection.

The Record/Born interface can supply normalized weights over an available
readout context after a selective interface is given. Those weights can be used
as a candidate `p_x(v)`. They still do not supply `a_x`, the activation
probability that says whether a record occurs at that site in that step.

So the occurrence dependency narrows to:

```text
local activation law
  + selection law over available possibilities
  + preservation of existing records.
```

## What Moves

| Prior residual | Effect of this bridge |
|---|---|
| occurrence as broad "record production dynamics" | narrowed to local extension-kernel normal form |
| activation vs selection ambiguity | split into `a_x` and conditional `p_x` |
| total-recording risk | avoided by the explicit no-record outcome |
| unavailable-value risk | blocked by support restricted to `A_x` |
| composability ambiguity | disjoint local kernels compose by products |

## What Remains

The physical production bridge still has to supply at least one of:

- a deterministic rule for `a_x` and `p_x`;
- a stochastic local kernel;
- an instrument whose effects give `p_x` and whose physical trigger gives
  `a_x`;
- a Hamiltonian/transfer/Markov generator and a clock or rate normalization;
- a local broadcast/objectivity bridge if multi-observer objective records are
  required.

The normal form does not choose among those.

## Audit Consequence If Retained

The record-production blocker should be restated from

```text
derive record occurrence / production dynamics
```

to

```text
derive or supply a local record-extension kernel:
activation probability for unrecorded sites, selection over available
possibilities, and preservation of existing records.
```

Rows that only require "some possible local occurrence law has the correct
type" may cite this normal form. Rows that predict actual histories,
frequencies, rates, objective broadcast, or physical measurement outcomes still
need a physical kernel, instrument, or generator.

## Non-Claims

This note does not claim:

- record occurrence is derived from the axioms;
- every site records;
- every available possibility eventually records;
- Born weights themselves produce an occurrence token;
- a Hamiltonian, transfer operator, Markov generator, clock, rate, or
  decoherence model is derived;
- local objectivity or redundant broadcast is derived;
- measured values, fitted constants, lattice-MC values, beta=6 values, or a new
  primitive are used.

## No-Go Discipline Gate

**Status:** PASS for bounded normal-form localization. This is not a terminal
no-go. It is a positive finite normal-form theorem that leaves the physical
kernel/generator as the remaining bridge.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Availability-only route | Use admissibility to force occurrence. | RULED OUT BY PRIOR: availability restricts support but leaves no-record and activation extensions. |
| Post-record append route | Use history/count dynamics to produce the next atom. | RULED OUT BY PRIOR: append/count consumes supplied atoms. |
| Born-weight route | Use trace weights to produce the realized token. | PARTIAL: weights can supply `p_x`, not activation `a_x`. |
| Instrument route | Use a physical record-writing instrument to supply activation and selection. | OPEN: valid downstream bridge supplier. |
| Markov/generator route | Use a local stochastic generator or transfer rule. | OPEN: valid downstream bridge supplier if locality, preservation, and rates are supplied. |
| Total-record route | Declare all unrecorded available sites activated. | SPECIAL CASE: allowed as a kernel with `a_x=1`, not forced by ontology. |
| New primitive route | Register occurrence as an approved primitive. | OWNER-GOVERNANCE ROUTE: not needed by this normal form before bridge routes are tested. |

### N2 - Wall-Independence Audit

Collapsed residual after this note:

```text
W_occurrence_kernel =
  physical values/rules for activation, selection, and any clock/rate.
```

Activation does not imply selection when multiple possibilities are available.
Selection weights do not imply activation because `a_x=0` remains allowed.
Preservation is a support condition, not a rate law. Local objectivity and
broadcast remain independent of occurrence: a token can be recorded without
being redundantly locally readable.

### N3 - Hidden-Wall Scan

"Local" means scoped to the supplied site or disjoint region and its available
possibility set. "Composability" is explicit product composition over disjoint
sites or regions. "Physical kernel" is the remaining bridge, not assumed here.
"No record" is an explicit outcome, not a failure case.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `RECORD_OCCURRENCE_GATE_FACTORIZATION...` | occurrence = activation + selection | normal form for activation + selection | yes |
| `RECORD_PRODUCTION_KERNEL_BOUNDARY...` | append/count does not determine producer kernel | physical kernel remains | yes |
| `RECORD_PRODUCTION_RESIDUAL_CHECKLIST...` | produced record needs realized atom, not kernel alone | kernel normal form is producer layer only | yes |
| `RECORD_DYNAMICS_LAYER_RECONCILIATION...` | post-record layer consumes atoms | preserved | yes |
| `RECORD_PRODUCTION_INTERFACE_PRINCIPLE...` | pre-record -> production bridge -> atom -> post-record | normal form fills the bridge type | yes |
| `RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED...` | axioms do not force record formation | preserved by explicit no-record outcome | yes |
| `RECORD_FORMATION_POINTER_NON_DEMOLITION...` | finite controlled-copy model is sufficient under explicit hypotheses | possible physical kernel supplier | yes |

### N5 - Rhetoric Audit

The note does not say records never form or that occurrence is impossible. It
says the minimal local occurrence bridge has a finite normal form and that the
physical kernel values remain outside this theorem. The statement is tested at
the one-site and disjoint finite-region levels, not as a universal dynamics
claim.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive `a_x` and `p_x` from a retained physical instrument;
- derive them from a local Markov/transfer generator with a clock or rate;
- use Born-form weights as `p_x` once activation is supplied;
- use a controlled-copy or pointer model as a bounded supplier;
- owner-promote occurrence only if the project chooses a primitive production
  rule instead of a bridge.

No new axiom is requested by this note.

### N7 - Steelman

A hostile reviewer can argue that a normal form is only bookkeeping: every
finite probability law can be decomposed into activation and conditional
selection, so the physical work is still entirely in choosing the kernel. That
objection is correct and is why the note does not claim production closure.
The value is that audit rows can no longer hide occurrence behind "dynamics";
they must supply exactly the activation, selection, preservation, and rate
content they need.

### N8 - Cross-Cycle Echo

Earlier record-production walls shrank when the layers were separated:
post-record append/count became exact consumer grammar, Born weights became an
interface theorem after supplied effects, and occurrence became activation plus
selection. This note continues that split by giving the finite normal form for
the remaining occurrence bridge without promoting it into the axioms.
