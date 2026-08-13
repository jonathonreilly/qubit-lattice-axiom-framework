---
claim_id: realized_state_primitive_forbids_ensemble_plaquette_as_record_i_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Unit-lock Record readout I is a nonnegative integer domain count with I(empty)=0. The U(1) one-plaquette Haar mean <P>(2)=I_1(2)/I_0(2) obeys 0 < <P>(2) < 8/9 < 1 by remainder-controlled Bessel partial sums, so it is not an integer and is not a Record I. The realized-state primitive forbids identifying that ensemble mean with a pointwise Record readout. The note does not retire June 10, does not import 0.5934, and does not claim 4D <P>*."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
runner: scripts/realized_state_primitive_forbids_ensemble_plaquette_as_record_i_2026_08_13.py
---

# Realized-State Primitive Forbids Ensemble Plaquette Mean as Record I

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** readout type split between unit-lock Record `I` and the U(1)
one-plaquette Haar mean `<P>(2) = I_1(2)/I_0(2)`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/realized_state_primitive_forbids_ensemble_plaquette_as_record_i_2026_08_13.py`](../scripts/realized_state_primitive_forbids_ensemble_plaquette_as_record_i_2026_08_13.py)

## Result Up Front

Unit-lock Record readout is a domain count. For a finite collection of
pairwise-disjoint unit locks, the scalar `I` is a nonnegative integer, and
`I(empty) = 0`. That is the Record sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

The U(1) one-plaquette ensemble mean

```text
<P>(beta) := I_1(beta) / I_0(beta)
```

is used only as a typed contrast. It is not 4D SU(3). Here

```text
I_n(beta) = sum_{k >= 0} 1/(k! (k+n)!) (beta/2)^{2k+n}.
```

At `beta = 2` the remainder-controlled partial sums give
`0 < I_1(2)/I_0(2) < 8/9 < 1`. So `<P>(2)` is not an integer. Record `I`
of any unit-lock pattern is an integer. They are unequal types.

The realized-state primitive
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
supplies no averaging over alternatives and permits only pointwise
evaluation at the realized state. `<P>` is an ensemble mean over Haar.
The primitive forbids identifying `<P>` with a Record readout.

This note does not retire June 10. It does not import 0.5934. It does not
claim 4D `<P>*`. It does not say a later law-level table is impossible.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Certified Bessel bounds show <P>(2) is not an integer; Record I is an integer; the realized-state primitive forbids identifying the Haar ensemble mean with a pointwise Record readout. June 10 and 4D <P>* remain open."
trace_class: negative_route_pruning
target_claim_id: record_i_versus_ensemble_plaquette_mean
target_blocker_text: "do not identify a Haar ensemble mean with unit-lock Record I"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep the readout type split. Do not identify <P> with Record I. June 10 remains open. Do not import 0.5934. Do not adopt axiom text."
hypothetical_axiom_status: "no edit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

A **unit lock** is one record locking exactly one admissible local
possibility. A **unit-lock pattern** is a finite collection of
pairwise-disjoint unit locks. Record readout `I` of that collection is the
domain count: a nonnegative integer. Additivity and the empty case are the
axiom sentences

```text
Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
I is additive, with I(empty)=0.
```

So `I(empty) = 0`, and `I` of `n` unit locks is `n`.

The U(1) contrast uses normalized Haar measure `d theta / (2 pi)` and the
one-plaquette weight `exp(beta cos theta)`. Then

```text
<P>(beta) = int cos theta exp(beta cos theta) d theta / int exp(beta cos theta) d theta
          = I_1(beta) / I_0(beta).
```

That object is an ensemble mean over Haar. It is not a realized unit-lock
pattern, and it is not 4D SU(3).

At `beta = 2`,

```text
I_0(2) = sum_{k >= 0} 1/(k!)^2,
I_1(2) = sum_{k >= 0} 1/(k! (k+1)!),
S0_N = sum_{k=0}^{N} 1/(k!)^2,
S1_N = sum_{k=0}^{N} 1/(k! (k+1)!).
```

The `I_0` term ratio is `t_{k+1}/t_k = 1/(k+1)^2`. For `N >= 1` the tail
admits the geometric majorant

```text
0 <= I_0(2) - S0_N <= t_{N+1} / (1 - 1/(N+2)^2).
```

The same `q = 1/(N+2)^2` majorant applies to the `I_1(2)` tail, because
the `I_1` ratio `1/((k+1)(k+2))` is strictly smaller than `1/(k+1)^2`.

Identity gates call `i0_partial`, `i1_partial`, and `record_I`. Series
coefficients are the Bessel terms only.

## Exact Target And Obligation Graph

**Exact target.** Prove that the U(1) one-plaquette mean at `beta = 2` is
not an integer, that unit-lock Record `I` is an integer, and that the
realized-state primitive forbids identifying the ensemble mean with a
Record readout.

| Obligation | Role | Disposition |
|---|---|---|
| pin unit-lock `I` as a nonnegative integer with `I(empty)=0` | premise | Record axiom, quoted |
| pin the realized-state primitive (no averaging; pointwise) | premise | primitive note, quoted |
| enclose `I_0(2)` and `I_1(2)` by remainder-controlled partial sums | Theorem 1 | Bessel series at `beta=2` |
| split `<P>(2)` from integer Record `I` | Theorem 2 | `0 < <P>(2) < 8/9 < 1` |
| forbid identifying the Haar mean with a Record readout | Theorem 3 | primitive, applied |
| record scoped negatives, including June 10 | Theorem 4 | no retirement, no 4D claim |
| produce 4D `<P>*` or retire June 10 | non-claim | not executed |

## Theorem 1 — Remainder-Controlled Bounds at `beta = 2`

**Claim.** `S0_2(2) = 9/4`, so `I_0(2) >= 9/4`. `S1_1(2) = 3/2`, so
`I_1(2) >= 3/2`. `S1_3 = 229/144 < 2`, and the next-term remainder is
strictly less than `1/2880 / (1 - 1/25) < 1/2000`, so `I_1(2) < 2`.
Hence

```text
0 < I_1(2) / I_0(2) < 2 / (9/4) = 8/9 < 1.
```

**Proof.** At `beta = 2` every factor `(beta/2)^{2k+n}` equals `1`. The
`I_0` terms are `1/(k!)^2`:

```text
k = 0:  1,
k = 1:  1,
k = 2:  1/4,
S0_2 = 1 + 1 + 1/4 = 9/4.
```

All terms are positive, so `I_0(2) >= S0_2 = 9/4`. The consecutive ratio
is `t_{k+1}/t_k = 1/(k+1)^2`. For `N >= 1` and `k >= N+1` one has
`k+1 >= N+2`, hence `t_{k+1}/t_k <= 1/(N+2)^2 < 1`, and the tail is at
most the geometric series named above.

The `I_1` terms are `1/(k! (k+1)!)`:

```text
k = 0:  1,
k = 1:  1/2,
S1_1 = 1 + 1/2 = 3/2,
k = 2:  1/12,
k = 3:  1/144,
S1_3 = 3/2 + 1/12 + 1/144 = 229/144.
```

So `I_1(2) >= 3/2 > 0` and `S1_3 = 229/144 < 2`. The next term is
`t_4 = 1/(4! 5!) = 1/2880`. For `k >= 4` the ratio is
`1/((k+1)(k+2)) <= 1/(5*6) = 1/30 < 1/25 = 1/(N+2)^2` at `N = 3`.
Therefore

```text
0 <= I_1(2) - S1_3 <= (1/2880) / (1 - 1/25) = 25/69120 < 1/2000,
```

and `I_1(2) < 229/144 + 1/2000 < 2`. Combined with `I_0(2) >= 9/4`,

```text
0 < I_1(2) / I_0(2) < 2 / (9/4) = 8/9 < 1.
```

The paired runner recomputes these rationals from `i0_partial` and
`i1_partial`. No 4D Wilson integral is used, and the numeral named by
June 10 is not a series coefficient.

## Theorem 2 — Unequal Types

**Claim.** `<P>(2)` is not an integer. Record `I` of any unit-lock pattern
is an integer. They are unequal types.

**Proof.** Theorem 1 places `<P>(2)` in the open interval `(0, 8/9)`,
which contains no integer. A predicate "`<P>(2)` is an integer" must
fail. That predicate calls `i0_partial` and `i1_partial`.

A unit-lock pattern is a finite collection of pairwise-disjoint unit
locks. Record `I` is the domain count of that collection, so `I` is a
nonnegative integer. In particular `I(empty) = 0` and `I` of one unit
lock is `1`.

A predicate "`I` equals `<P>(2)`" must fail on `I = 0` and on `I = 1`.
That predicate calls `i0_partial`, `i1_partial`, and `record_I`. For
`I = 0` equality would require `I_1(2) = 0`, contradicting
`I_1(2) >= 3/2`. For `I = 1` equality would require `I_0(2) = I_1(2)`,
contradicting `I_1(2) < 2 < 9/4 <= I_0(2)`.

## Theorem 3 — Primitive Forbids the Identification

**Claim.** The realized-state primitive forbids identifying `<P>` with a
Record readout.

**Proof.** The primitive states that derivations may evaluate at the
realized state, pointwise, and that nothing more is supplied: no
averaging over alternatives. `<P>(beta) = I_1(beta)/I_0(beta)` is the
Haar ensemble mean of `cos theta` against the weight
`exp(beta cos theta)`. Forming that mean averages over the Haar
alternatives. Identifying the mean with a unit-lock Record readout would
treat an average over alternatives as the pointwise readout of a realized
state. The primitive forbids that identification.

Theorem 2 already shows the two objects are unequal as numbers at
`beta = 2`. Theorem 3 is the type reason they may not be identified even
before the numerical split: one is an ensemble mean, the other is a
pointwise Record count.

## Theorem 4 — Scoped Negatives

**Claim.** This note does not retire June 10, does not import 0.5934, does
not claim 4D `<P>*`, and does not say a later law-level table is
impossible.

**Proof.** June 10
[`PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md)
names a 4D SU(3) retirement interface. The present object is a 2D U(1)
one-plaquette Haar mean used only as a typed contrast. No 4D enclosure is
produced, so June 10 is not retired.

The series coefficients of `I_n` are
`1/(k! (k+n)!) (beta/2)^{2k+n}`. Feeding `5934/10000` into `I_n` as a
coefficient is rejected: it equals none of those terms at `beta = 2`.
The numeral is not an input.

No 4D configuration is sampled, and no 4D thermodynamic-limit plaquette
mean is claimed. A later law-level table that stayed on the correct type
— a certified 4D object, or a Record readout of a realized unit-lock
pattern — is not ruled out.

No axiom sentence is added or edited.

## Boundary And Non-Claims

The note does not:

- retire June 10, or produce a certified 4D SU(3) enclosure;
- import 0.5934, or feed that numeral into `I_n`;
- claim 4D `<P>*`, or identify the U(1) mean with a 4D Wilson mean;
- say a later law-level table is impossible;
- treat `<P>` as a realized unit-lock pattern;
- edit an axiom, or argue that an axiom update is necessary.

The scope is the readout type split at `beta = 2`.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| Record unit-lock `I`, `I(empty)=0` | premise | quoted from the axiom memo |
| realized-state primitive | premise | quoted; no averaging; pointwise |
| remainder-controlled `I_0(2)`, `I_1(2)` | Theorem 1 | computed here |
| `<P>(2)` not an integer; `I` is an integer | Theorem 2 | computed here |
| primitive forbids identifying `<P>` with Record `I` | Theorem 3 | applied here |
| June 10 4D interface and 4D `<P>*` | residual | live, not derived |

The exact advance is a certified type split. Independent audit remains
required before any effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | An ensemble mean is not a pointwise Record. The note certifies that `<P>(2)` is not an integer and that the realized-state primitive forbids identifying it with unit-lock `I`. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for a landed theorem identifying U(1) `<P> = I_1/I_0` with Record `I`, or forbidding that identification by the realized-state primitive. Hits quote the primitive's "no averaging" sentence or use `I_1/I_0` as a Wilson character ratio or first moment. No landed readout-type split of unit-lock `I` against remainder-controlled `<P>(2)` appears on that commit. |
| V3 | Independently checkable? | Textbook modified Bessel functions give `I_n` and `<cos theta> = I_1/I_0`. The runner recomputes `S0_2 = 9/4`, `S1_1 = 3/2`, `S1_3 = 229/144`, and the `1/2880` tail in exact rationals. |
| V4 | More than a restatement? | Yes. The witnesses `9/4`, `3/2`, `229/144`, `8/9`, and the failed predicates on `I = 0` and `I = 1` are not restatements of the primitive's prose. |
| V5 | One-step relabel? | No. Calling the Haar mean a Record readout would ignore both the integer type of `I` and the primitive's ban on averaging over alternatives. |

## No-Go Discipline Gate (Theorems 2–4 only)

The negative claim is restricted to this: `<P>(2)` is not a Record `I`,
and the realized-state primitive forbids identifying the ensemble mean
with a pointwise Record readout. The gate does not ship a global
non-existence theorem against a later 4D table.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| identify `<P>(2)` with an integer | predicate that the mean is an integer | Theorem 1: `0 < <P>(2) < 8/9 < 1` | **ATTEMPTED** |
| identify `I = 0` with `<P>(2)` | empty unit-lock pattern | Theorem 2: `I_1(2) >= 3/2 > 0` | **ATTEMPTED** |
| identify `I = 1` with `<P>(2)` | one unit lock | Theorem 2: `I_1(2) < 2 < 9/4 <= I_0(2)` | **ATTEMPTED** |
| treat Haar mean as pointwise readout | average over alternatives, then call the average `I` | Theorem 3: primitive forbids averaging | **ATTEMPTED** |
| import `0.5934` | feed `5934/10000` into `I_n` as a coefficient | rejected: coefficients are Bessel terms only | **ATTEMPTED** |
| claim 4D `<P>*` | replace the U(1) contrast by 4D SU(3) | not executed; U(1) only | **ATTEMPTED** |

### N2 — wall independence

Theorems 2 and 3 close only the identification of this U(1) ensemble mean
with unit-lock Record `I`. They do not close June 10, a later 4D
enclosure, or a later law-level table of the correct type.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| unit-lock `I` as a nonnegative integer, `I(empty)=0` | quoted Record sentence |
| realized-state primitive, no averaging | quoted primitive |
| Bessel series `I_n` at `beta = 2` | explicit remainder hypotheses |
| U(1) Haar weight `exp(beta cos theta)` | declared contrast, not 4D SU(3) |
| June 10 4D interface | open; not assumed settled |
| axiom edit identifying `<P>` with `I` | live governance path; not required |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) | no averaging over alternatives; pointwise evaluation at the realized state | quoted; applied to Haar means |
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | unit lock; content-only readout; `I` additive; `I(empty)=0` | quoted; no edit |
| [`docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md) | 4D retirement interface | cited only as not retired |

No unmerged note is used as a parent.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | remainder-controlled Bessel terms at `beta = 2` | no 4D Wilson character expansion |
| per site | one U(1) plaquette versus one unit-lock pattern | no 4D site configuration is sampled |
| per mode | the `I_n` power series, not a transfer-matrix mode | no 4D spectral gap |
| per block | integer type of `I`, non-integer `<P>(2)`, primitive ban | no June 10 retirement and no 4D `<P>*` |
| lattice-wide | checked and not executed | no lattice-wide 4D table |

The residual is a readout type split. It is not lattice-wide.

### N6 — live partial-closure paths

1. A later certified 4D SU(3) table that does not pass through this U(1)
   mean, which is the June 10 interface.
2. A Record readout of a realized unit-lock pattern, evaluated pointwise.
3. A later law-level table that keeps the ensemble mean and the Record
   count as distinct types.
4. An owner-approved typed axiom addition. The present type split does
   not require that addition, and it would not turn `<P>` into Record `I`.

The quoted primitive and Record sentences already name the two types.
They do not identify `<P>` with `I`.

### N7 — hostile steelman

> A plaquette mean is a readout. `<P>` is a number read from the
> ensemble, so it is Record `I`.

**Answer.** Record `I` is the domain count of realized unit locks. It is
an integer, and `I(empty) = 0`. `<P>(2)` is a Haar ensemble mean and lies
in `(0, 8/9)`. The realized-state primitive forbids replacing pointwise
evaluation by an average over alternatives. Theorems 2 and 3 are the
witness.

### N8 — cross-cycle echo

June 10 already refused to treat a one-plaquette proxy as the 4D
thermodynamic-limit object. The present note is a different split: even
the U(1) one-plaquette mean is the wrong *type* for Record `I`. It does
not reverse June 10, and it does not execute the 4D interface.

**Gate disposition.** PASS for the certified type split and for the
primitive's ban on identifying the ensemble mean with Record `I`.
FAIL / DO NOT SHIP for “June 10 is retired,” “`<P>` is 4D `<P>*`,” or
“an axiom update is necessary.”

## Primary Runner

[`scripts/realized_state_primitive_forbids_ensemble_plaquette_as_record_i_2026_08_13.py`](../scripts/realized_state_primitive_forbids_ensemble_plaquette_as_record_i_2026_08_13.py)
recomputes `S0_2 = 9/4`, `S1_1 = 3/2`, `S1_3 = 229/144`, the `1/2880`
remainder, and the ratio bound `8/9` in exact rational arithmetic.
Identity gates call `i0_partial`, `i1_partial`, and `record_I`. A
predicate that `<P>(2)` is an integer must fail. A predicate that `I`
equals `<P>(2)` must fail on `I = 0` and on `I = 1`. Feeding
`5934/10000` into `I_n` as a coefficient must be rejected. No cache is
written.

```bash
python3 scripts/realized_state_primitive_forbids_ensemble_plaquette_as_record_i_2026_08_13.py
```

Expected summary:

```text
TOTAL: PASS>=10 FAIL=0
```
