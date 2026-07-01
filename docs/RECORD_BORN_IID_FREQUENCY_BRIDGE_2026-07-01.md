# Record/Born IID Frequency Bridge

**Date:** 2026-07-01
**Claim type:** bounded bridge theorem / frequency-interface normal form.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
that occurrence, IID reset, physical instruments, or observed frequencies are
derived from the ontology alone.
**Primary runner:**
[`scripts/record_born_iid_frequency_bridge_2026_07_01.py`](../scripts/record_born_iid_frequency_bridge_2026_07_01.py)

## Claim

The record/probability/measurement blocker has a clean frequency bridge once
two already-isolated inputs are supplied:

```text
selective record-writing interface with Born trace weights
  + supplied IID reset/preparation of that interface
  -> multinomial history weights and finite frequency concentration.
```

This bridge does not derive probabilities from post-record counts. It does the
opposite: it keeps the pre-record model and post-record data separate.

Given a finite outcome set `A`, a probability kernel `p(v)` on `A`, and an IID
reset/preparation model for `N` repetitions of the same record-writing
interface, a record history

```text
w = (w_1, ..., w_N) in A^N
```

has product weight

```text
P(w) = product_i p(w_i).
```

The empirical frequency of value `v`,

```text
F_v(w) = #{i : w_i = v} / N,
```

satisfies

```text
E[F_v] = p(v),
Var(F_v) = p(v)(1 - p(v)) / N.
```

Therefore, for any `epsilon > 0`,

```text
P(|F_v - p(v)| >= epsilon)
  <= p(v)(1 - p(v)) / (N epsilon^2).
```

So the supplied IID model gives the ordinary finite frequency route from Born
weights to empirical frequencies. The remaining physical wall is not
frequency algebra. It is the supplier:

```text
W_iid_frequency =
  physical reset/preparation/independence for repeated trials,
  plus occurrence/instrument/rate content for the records being counted.
```

## Finite Theorem

For a binary context with `p(1)=p` and `p(0)=1-p`, product histories have

```text
P(w) = p^n (1-p)^(N-n),
```

where `n` is the number of ones in `w`. Summing over histories with the same
count gives the binomial law

```text
P(n) = C(N,n) p^n (1-p)^(N-n).
```

The standard finite identities are:

```text
sum_n P(n) = 1,
E[n] = Np,
Var(n) = Np(1-p).
```

Dividing by `N` gives the frequency identities in the claim.

For a general finite outcome set `A`, the same calculation gives the
multinomial law. For each value `v`, the indicator variable

```text
X_i^v = 1 if w_i = v, else 0
```

is Bernoulli with mean `p(v)`, and independence gives

```text
F_v = (1/N) sum_i X_i^v,
E[F_v] = p(v),
Var(F_v) = p(v)(1-p(v))/N.
```

This is a theorem about a supplied repeated-trial model. It is not a theorem
that record histories by themselves supply that model.

## Load-Bearing Reset/Independence

The IID condition is real content.

For two binary records, the correlated model

```text
P(00) = 1 - p,
P(11) = p,
P(01) = P(10) = 0
```

has the same one-trial marginals as the IID model:

```text
P(w_1=1) = P(w_2=1) = p.
```

But the empirical frequency is either `0` or `1`, so

```text
Var(F_1) = p(1-p),
```

not `p(1-p)/2`. The same Born one-record weights do not by themselves give
the IID frequency law. Reset/preparation/independence is the load-bearing
bridge input.

## Relation To Existing Record/Born Work

The record/Born selective-write bridge supplies the pre-record trace weights
and repeatable sharp readout after a supplied instrument/effect interface. The
occurrence-instrument bridge supplies an activation/selection kernel after a
supplied record-writing instrument or trigger. The older frequency boundary
correctly says finite record counts do not derive the probability model.

This note composes those layers without collapsing them:

```text
Born-form weights describe the supplied interface.
Occurrence/instrument content says which records are actually written.
IID reset/preparation says repeated trials use the same independent kernel.
Finite histories then have multinomial weights and frequency concentration.
```

## What Moves

| Prior residual | Effect of this bridge |
|---|---|
| finite counts do not derive probabilities | unchanged and preserved |
| Born weights have no frequency semantics by themselves | narrowed: supplied IID reset gives frequency concentration |
| measurement semantics as one broad wall | split into interface, occurrence, reset/independence, and rate/objectivity |
| empirical sample handling | exact finite multinomial model once repeated trials are supplied |
| probability axiom pressure | reduced: no new ontology axiom is needed for frequency algebra |

## What Remains

The framework still needs physical bridges or approved premises for:

- the record-writing instrument or trigger;
- occurrence of records in individual runs;
- reset/preparation between repeated trials;
- independence or exchangeability assumptions;
- clock/rate normalization if rates per unit time are claimed;
- local objectivity or redundant broadcast if multi-observer records are
  claimed;
- the physical context and observable being sampled.

Those are operational measurement questions, not failures of the finite
frequency algebra.

## Audit Consequence If Retained

Rows that need empirical frequencies should use the dependency shape:

```text
selective record/Born interface
  + record occurrence or instrument supplier
  + IID reset/preparation of repeated trials
  -> multinomial record histories
  -> finite frequency concentration around Born weights.
```

Rows that cite only record counts or only one realized finite history still
must not claim a Born-frequency law. Rows that cite Born trace weights but no
reset/independence surface must keep `W_iid_frequency` explicit.

## Non-Claims

This note does not claim:

- post-record counts derive probabilities;
- finite frequencies equal probabilities in any given run;
- IID reset/preparation is derived from the four ontology axioms;
- record occurrence is derived;
- every possible record is eventually written;
- every site records;
- a clock, rate, reset cost, instrument coupling, source/action coefficient,
  theta sector, metric, or measured observable is derived;
- measured constants, fitted values, lattice-MC values, beta=6 values, or a
  new primitive are used.

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this theorem.

If bridge-first work fails, the minimum foundation target is not a generic
probability axiom. It is a narrow operational supplier, for example:

```text
P_iid_measurement_run:
  In a named finite record context with a supplied record-writing instrument,
  repeated trials are reset/prepared so that the same finite record kernel is
  sampled independently, with any claimed rate or objectivity content stated
  explicitly.
```

This is not proposed as a registered primitive here. It is the smallest
fallback shape exposed by the theorem.

## No-Go Discipline Gate

**Status:** PASS for bounded wall localization inside a positive frequency
bridge. This is not a terminal no-go against deriving reset, occurrence, or a
physical measurement model. It says only that IID/reset is the exact supplier
needed to turn Born weights into frequency concentration.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Count-only route | Derive probabilities from finite realized histories. | RULED OUT BY PRIOR: many finite histories with different frequencies are compatible with the same grammar. |
| Born-interface route | Use the selective write/effect interface to supply trace weights. | PARTIAL BY PRIOR: supplies `p(v)`, not repeated-trial reset or occurrence. |
| Occurrence-instrument route | Use a supplied writing instrument to create actual record atoms. | PARTIAL BY PRIOR: supplies a local kernel once the instrument/trigger is supplied, not IID repetition. |
| IID reset route | Supply repeated independent preparations of the same kernel. | ATTEMPTED here: succeeds as multinomial frequency algebra. |
| Correlated-run route | Keep one-trial Born marginals but allow trial correlations. | ATTEMPTED here as a negative control: same marginals do not give IID variance. |
| New primitive route | Register repeated-trial/reset semantics as an operational primitive. | OWNER-GOVERNANCE ROUTE: not used here while bridge derivations remain live. |

### N2 - Wall-Independence Audit

Collapsed residual after this bridge:

```text
W_iid_frequency =
  reset/preparation/independence for repeated trials,
  plus whatever occurrence, rate, and objectivity content the downstream row
  claims.
```

Born trace weights do not imply reset. Reset does not imply record occurrence.
Occurrence does not imply independence between repetitions. Rate and objectivity
are separate only when the row claims rates or multi-observer records.

### N3 - Hidden-Wall Scan

"Supplied IID reset/preparation" is an explicit bridge input, not hidden axiom
content. "Born weights" means trace weights on a supplied record/effect
interface. "Frequency" means the empirical count ratio in a finite repeated
history. "Concentration" means the finite variance/Chebyshev bound under the
supplied product model, not equality in a finite run.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05` | finite counts do not derive probability or IID. | IID/reset is supplied here, not derived from counts. | yes |
| `RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30` | Born trace weights after supplied interface; occurrence and IID remain. | consumes trace weights and preserves occurrence/reset. | yes |
| `RECORD_OCCURRENCE_INSTRUMENT_SUPPLIER_BRIDGE_2026-07-01` | instrument supplies local kernel once physical trigger is supplied. | repeated-trial frequency needs IID reset of such kernels. | yes |
| `RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01` | activation is not derived from availability/Born weights. | occurrence remains outside frequency algebra. | yes |
| `OPERATIONAL_PREMISE_GAP_MAP_2026-07-01` | measurement/frequency needs occurrence plus instrument/reset structure. | this bridge narrows the reset/frequency layer. | yes |

### N5 - Rhetoric Audit

The negative boundary is narrow: finite record histories alone do not supply
the IID probability model. The positive theorem is tested at the finite
binary and finite multinomial repeated-history resolutions. The note does not
claim that no physical reset theorem can be derived.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive reset/preparation/independence from a concrete instrument cycle;
- derive it from a Markov or transfer law with a stationary preparation
  surface;
- derive occurrence and reset together from a source/action or
  metric/observable measurement theorem;
- accept a bounded experimental protocol for a named record context;
- explicitly approve a narrow operational repeated-trial primitive if owner
  governance chooses that route.

The primitive-registry check confirms that no current approved primitive grants
IID reset, occurrence, probability frequencies, or measurement-rate semantics.

### N7 - Steelman

A hostile reviewer can say this bridge is mathematically standard and shifts
all real physics into the reset/preparation and occurrence supplier. That is
correct and preserved. The value is not novelty of the multinomial theorem;
the value is audit hygiene: once the interface and IID supplier are present,
frequency semantics are no longer a vague measurement wall, and without that
supplier no finite-count argument may pretend to derive Born frequencies.

### N8 - Cross-Cycle Echo

Earlier record cycles overclaimed by treating counts, kernels, Born weights,
or append grammar as if they already gave physical measurement frequencies.
This bridge keeps the split explicit: weights are pre-record interface
content, records are produced atoms, repeated trials require reset and
independence, and empirical frequencies are post-record statistics.

## Verification

Run:

```bash
python3 scripts/record_born_iid_frequency_bridge_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=87 FAIL=0
```
