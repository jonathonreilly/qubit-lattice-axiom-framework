# The Record Axiom's K/CPT-Orbit Clause Is Equivalent To A K-Invariant Registered Surface

**Date:** 2026-06-10
**Claim type:** bounded_theorem (exact finite-dimensional equivalence locating
the orbit clause's content; supplies the basis for a possible future
owner-approved slimming of the Record axiom's wording; no axiom is changed)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/kcpt_orbit_clause_kinvariant_surface_equivalence_2026_06_10.py`](../scripts/kcpt_orbit_clause_kinvariant_surface_equivalence_2026_06_10.py)
(SCORECARD: PASS=20, FAIL=0; cached:
[`logs/runner-cache/kcpt_orbit_clause_kinvariant_surface_equivalence_2026_06_10.txt`](../logs/runner-cache/kcpt_orbit_clause_kinvariant_surface_equivalence_2026_06_10.txt))

---

## What this addresses

The Record axiom
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)) states:
given a readout context with a finite central-sector decomposition and a
fixed `K`/CPT conjugation, **the realized outcome is the `K`/CPT orbit of the
realized central sector**. In the axiom-scrub question "which clauses are
independent content, and which are consequences of the others plus the record
ontology?", the orbit clause is the natural candidate: it is the one clause
that quotients the outcome set.

This note proves the exact equivalence that locates its content. The orbit
quotient is **interchangeable** with a statement about the registered scalar
surface — under the adjacent record-outcome proposal's individuation principle
(observables are constituted in the stack; outcomes are individuated by what
is registered, since nothing sits behind the record;
[`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md)).

## The theorem (finite-dimensional, exact)

**Setting.** A context is a finite central-sector decomposition
`{P_k, k in S}` plus an antiunitary `K` with `K P_k K^{-1} = P_{pi(k)}`,
`pi` an involution on the label set (`K^2 = +1` and `K^2 = -1` both
realized). A registered scalar assignment is a map `iota: S -> R`, extended
finitely additively over disjoint records. Outcomes-by-registration are the
indistinguishability classes: `k ~ k'` iff every admissible `iota` agrees on
them.

**(T1, forward).** If the admissible surface is `pi`-invariant
(`iota o pi = iota`) and orbit-separating, the indistinguishability classes
are **exactly** the `K`/CPT orbits (runner Part B; random surfaces and the
indicator basis).

**(T2, converse).** If some admissible `iota` separates two sectors in one
orbit, that orbit is not an indistinguishability class — "outcome = orbit"
fails on that surface (runner Part C). Hence:

```text
   the orbit clause   <=>   { individuation-by-registration
                              + pi-invariant, orbit-separating
                                registered surface }.
```

The substitution check reproduces "outcome = orbit" on 25 random label sets
and involutions (runner Part F).

**(T3, overlap readouts).** For the delivered partition-level readouts
`iota_rho(k) = tr(P_k rho)`, the transport identity

```text
   tr(P_{pi(k)} rho) = tr(P_k rho_K),       rho_K := the K-image state,
```

holds exactly, so `pi`-symmetry of the overlaps is equivalent to the
vanishing of the **sector-resolved K-reality defect**
`tr(P_k (rho - rho_K))`. `K`-real states give `pi`-symmetric overlaps; the
generic (non-`K`-real) state separates an orbit pair; the symmetrization
`(rho + rho_K)/2` is exactly `K`-real for **both** `K^2 = +1` and
`K^2 = -1` (runner Part D).

## What T3 exposes (and does not discharge)

Overlap-readout compatibility with the orbit clause **is** `K`-reality of the
realized state at sector resolution. The standing `K`-reality predicate (the
named coarseness predicate of guardrail G2 in the canonical record principle)
and the axiom's orbit clause are two faces of one structure:

- the **clause** guarantees outcomes are orbit-level whatever the state;
- the **delivered overlap readouts** respect that exactly on `K`-real states,
  and witness its violation otherwise (the defect form makes the violation a
  computable per-sector quantity).

Whether realized states are `K`-real remains the standing pin — exposed at
sector resolution here, **not** discharged.

## What this offers the axiom scrub

The Record axiom currently carries "and a fixed `K`/CPT conjugation" in its
context preamble and the orbit quotient in its outcome clause. By T1/T2,
an alternative wording of equal strength exists in which the context supplies
its symmetry through the **registered surface's invariance** and the orbit
quotient becomes a theorem. The equivalence is exact in both directions, so:

- nothing downstream that consumes "outcome = orbit" would change;
- the choice between the two wordings is a presentation decision about where
  the same content sits (postulated quotient vs invariant surface).

Whether to adopt either wording is an **owner-approved, separately reviewed step**
(the minimality policy's path; the 2026-06-04 to 2026-06-05 Record refinement
is the procedural precedent). This note supplies the equivalence only and
changes no axiom memo. If adopted, the change should be batched with any
other approved scrub items, since any memo edit invalidates prior direct
`minimal_axioms` audits through the axiom-premise hash guard.

## Hostile witnesses (wall-independence)

| dropped hypothesis | witness | outcome |
|---|---|---|
| `pi`-invariance | indicator of one orbit-mate | splits the orbit; clause fails (C1) |
| separation | constant readout | classes strictly coarser than orbits (B3) |
| `K`-reality of the state | generic `rho` | overlap readout separates an orbit pair, defect != 0 (D4) |
| nontrivial `pi` | `pi = id` boundary | orbits are singletons; clause vacuous; equivalence degenerates gracefully (E1) |

## Relation to adjacent results

- [`KCPT_ORBIT_COUNT_IS_THE_PARTITION_NOT_THE_WEIGHT_HOLOMORPHIC_READOUT_MEASURE_NEUTRAL_NARROW_THEOREM_NOTE_2026-06-06.md`](KCPT_ORBIT_COUNT_IS_THE_PARTITION_NOT_THE_WEIGHT_HOLOMORPHIC_READOUT_MEASURE_NEUTRAL_NARROW_THEOREM_NOTE_2026-06-06.md)
  — the orbit count is weight-blind. Complementary: that note bounds what the
  clause *delivers* (no weight); this note locates what the clause *is*
  (surface invariance). Runner Part G2 keeps the weight-blindness visible: no
  measure content enters.
- [`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md)
  — supplies the individuation-by-registration principle T1/T2 consume, and
  guardrail G2's `K`-reality predicate that T3 resolves to sector level.

## What this does not do

- It does not change, reword, or propose to bypass any axiom; the equivalence
  is supplied for a decision that is the owner's and requires separate review.
- It does not derive the `K`-reality of realized states (the generic state
  violates it; runner Part D4/G1).
- It does not touch weights, measures, or the `r` dial: the surface used is
  weight-blind by construction (Part G2), consistent with the
  partition-not-weight result.
- It does not supply a readout context, decomposition, or `K` — contexts
  remain inputs, exactly as the axiom states.
- It does not set audit status.

## Falsifiers

- A `pi`-invariant, orbit-separating surface whose indistinguishability
  classes differ from the orbits (would refute T1).
- A surface separating an orbit pair on which "outcome = orbit" still holds
  under individuation-by-registration (would refute T2).
- A state and context where the transport identity or the defect form fails
  (would refute T3).
- A `K^2 = -1` context where the symmetrization fails to be `K`-real (would
  cut T3's scope to `K^2 = +1`).

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the Record
  axiom whose orbit clause this note locates.
- [RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md)
  — individuation-by-registration and guardrail G2.
- [KCPT_ORBIT_COUNT_IS_THE_PARTITION_NOT_THE_WEIGHT_HOLOMORPHIC_READOUT_MEASURE_NEUTRAL_NARROW_THEOREM_NOTE_2026-06-06.md](KCPT_ORBIT_COUNT_IS_THE_PARTITION_NOT_THE_WEIGHT_HOLOMORPHIC_READOUT_MEASURE_NEUTRAL_NARROW_THEOREM_NOTE_2026-06-06.md)
  — the weight-blindness this note keeps intact.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. It changes no axiom memo and registers no
primitive. The independent audit lane is the only status authority.

## Audit metadata

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "Finite-dimensional equivalence: given a finite central-sector context, a K/CPT involution on sector labels, and individuation by registered scalar surfaces, the orbit outcome clause is equivalent to pi-invariant orbit-separating registered surfaces. Overlap readouts reduce to a sector-resolved K-reality defect. The K-reality pin remains open; no axiom memo, primitive, weight rule, readout context, or audit status is changed."
upstream_dependencies:
  - minimal_axioms
  - record_outcome_observable_principle_canonical_proposal_note_2026-06-05
  - kcpt_orbit_count_is_the_partition_not_the_weight_holomorphic_readout_measure_neutral_narrow_theorem_note_2026-06-06
admitted_context_inputs: []
source_sets_audit_outcome: false
```
