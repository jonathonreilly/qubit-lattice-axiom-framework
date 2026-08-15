# Finite controller clean-event census — Cycles 863–865 source salvage

Date: 2026-08-02 (review-loop salvage 2026-08-15; see Review record)

Authority: none

Audit: unset

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:
[finite controller clean-event census](../scripts/frontier_cycle863_865_arc_independent_check_2026_07_28.py)

Constitutional effect: none. This source salvage changes no axiom,
qualification, approved primitive, premise registry, audit result, or audit
status. Independent audit remains required.

## Result

The runner exactly replays one supplied finite controller corpus. It measures
controller-internal clean predicates, synchronization predicates, program
boundaries, and orbit indices. These are program observables only: this note
does not identify any of them with framework Record formation, physical time,
duration, rate, or an intrinsic clock.

The declared corpus has two controller banks, an 11-station program ring, four
seed-index variants, pairwise nonadjacent source-position sets of sizes two
through five, and 51,115 complete program orbits. The position and seed census
contains exactly 748 configurations.

| finite measurement | exact value |
|---|---:|
| configurations | 748 |
| configurations with a global-clean observation | 182 |
| configurations with a global-clean observation at an orbit end | 114 |
| configurations without a global-clean observation inside the horizon | 566 |
| uncapped global-clean predicate events | 2,505,173 |
| uncapped bank-0 / bank-1 predicate events | 14,667,058 / 58,508,289 |
| uncapped two-bank synchronization events | 6,821,527 |
| stored synchronization events under the declared per-configuration cap of 4,096 | 559,606 |
| stored synchronization events on / off an orbit boundary | 79,267 / 480,339 |
| stored synchronization fraction on an orbit boundary | 14.1647874% (14.16% rounded) |
| first synchronization equal to first orbit-end global clean | 25 of 114 applicable configurations |
| synchronization observed without an orbit-end global clean | 624 configurations |

For each of the 114 orbit-end observations, the runner also records the index
of that boundary in the configuration's stored global-clean event list. The
114 rows occupy 44 orbit-index cohorts, 15 of which have more than one member.
Their within-cohort rung-spread histogram is

```text
{0: 30, 1: 4, 2: 4, 4: 5, 5: 1}.
```

The 15 multi-member cohorts contain 85 rows. After subtracting the minimum
rung inside each cohort, their offset histogram is

```text
{0: 41, 1: 15, 2: 13, 3: 9, 4: 6, 5: 1}.
```

Grouping those 85 finite rows by their first global-clean program boundary
produces 50 groups and 35 repeated-value instances; every repeated-value group
has one offset value. This is an exact equality in the declared table. It is
not a universal predictor, a physical law, or evidence that the program
boundary is an intrinsic datum.

## What is supplied, derived, and open

### Load-bearing import

- The [Cycle-719 two-rail recurrent controller
  core](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  and its paired source runner are supplied. The census runner byte-pins the
  source runner and rebuilds the configuration census, clean-coordinate maps,
  schedules, and event tables. The Cycle-719 audit row is currently
  `unaudited`; this result is therefore bounded support conditional on that
  source, not an independently retained downstream theorem.

### Declared corpus choices

- two banks and the resulting 11-station program;
- four seed-index variants;
- pairwise nonadjacent source-position sets of sizes two through five;
- a 51,115-orbit horizon; and
- per-configuration stores capped at 4,096 global/synchronization events and
  512 per-bank events. The totals labeled uncapped are accumulated before the
  stores are truncated.

These are finite-test parameters. They are not derived physical constants or
framework primitives.

### Derived inside the declared corpus

- the 748-row configuration count;
- the exact clean/synchronization counts and orbit-boundary split in the table;
- the 44-cohort rung-spread histogram; and
- the 85-row offset table, including its 50 first-boundary groups, 35 repeated
  instances, and zero conflicting offsets inside those groups.

### Open

- a retained bridge from the controller's internal global-clean predicate to
  framework Record formation;
- any physical interpretation of a program boundary, orbit index, or event
  list as time, duration, rate, or clock data;
- behavior outside the declared two-bank corpus and finite horizon; and
- whether the finite table equality persists under a differently constructed
  controller, a larger bank family, or a physical Record-production model.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "downstream consumer not yet known; a future Record-formation/time bridge may compare against this finite controller table, but this artifact does not supply that bridge"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "first provide an independently reviewable bridge identifying a controller event with framework Record formation; only then test whether any event-order quantity has physical time semantics"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact enumeration and deterministic replay on one declared finite controller corpus, conditional on the unaudited Cycle-719 substrate; all Record and physical-time interpretations withdrawn"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

There is one load-bearing runner and it is the primary runner, so this claim
needs no `packet_helper_runner` entry or helper-registry mapping.

## Proof boundary

The bounded claim is a finite enumeration, not a framework-time theorem.

1. For a labelled cycle graph with 11 stations, enumerate every pairwise
   nonadjacent position set of sizes two through five and combine it with the
   four supplied seed-index variants.
2. Reconstruct the Cycle-719 bank/link clean-coordinate sets by one-wire
   perturbations of the packed state instead of importing a clean-event table.
3. Replay all configurations in bit-sliced exact Boolean arithmetic, with a
   duplicated first lane checked at every observation boundary.
4. Accumulate predicate totals before store truncation, and separately label
   every statistic that uses the capped stores.
5. Derive the orbit-index cohorts and offset table from the replayed event
   lists, then require every exact count and histogram printed above.

The runner's terminal marker certifies only these finite tables. It cannot
certify any interpretation that is absent from these steps.

## No-Go Discipline Gate

### N1 — strongest surviving positive

The strongest result is the exact finite census and cohort-table equality
stated above. No semantic or universal negative is needed to state it.

### N2 — withdrawn conclusions

The pre-review branch described clean events as intrinsic time, treated a
scheduler coordinate as gauge, called non-observation a timeless ontology,
claimed exhaustion of record-native predictors, and presented a connection to
the anomaly theorem's declared axis premise. All of those conclusions are
withdrawn. Nothing in this salvage may be cited for them.

### N3 — hidden-wall scan

Words such as “without,” “not,” and “open” in this note delimit the finite
claim and list absent bridges; they do not assert that the missing bridge is
impossible. No missing derivation is promoted into a structural wall.

### N4 — residual matching

The synchronization/orbit-boundary mismatch and the 566 configurations with no
global-clean observation inside the horizon are reported only as finite table
entries. They are not used as witnesses against every clock, event definition,
controller, horizon, Record-production mechanism, or framework dynamics.

### N5 — rhetoric and resolution audit

```text
per_element: not claimed
per_site: not claimed
per_mode: not claimed
per_block: exactly one declared finite controller corpus
lattice_wide: not claimed
```

The runner emits the same five quantifier lines. Its exact arithmetic is at the
configuration and finite-corpus level only.

### N6 — partial-closure paths

A future constructive route could define a physical Record-production map,
prove that one of its events coincides with this controller predicate, and
then compare order quantities across controller families and bank counts. This
is an open research route, not evidence for or against the present finite
table.

### N7 — steelman

The strongest alternative explanation is that every reported relation is an
artifact of the supplied Cycle-719 program, initialization family, finite
horizon, and scheduler. That explanation is fully compatible with this note;
the salvage deliberately makes no physical interpretation that would exclude
it.

### N8 — cross-cycle echo

The Cycle-719 source already states that controller ordinals are circuit
structure rather than physical time. This salvage preserves that boundary.
Earlier unlanded Cycles 852, 860, and 861 are provenance only and supply no
scientific premise here.

**Gate disposition:** the N1–N8 walk passes only because every negative
promotion was withdrawn. This note proposes no no-go result.

## Review record

### Iteration 1 — GPT-5.6-Sol/max, 2026-08-15 — FIX_THEN_PROCEED

The combined review found five blocking families: an unlanded Cycle-860 pin
inherited from closed PR #5881; an unsupported identification of an internal
clean predicate with framework Record formation and time; negative claims
without an N1–N8 or quantifier certificate; forced-green predicates in all
three supervisor primaries plus a branch-name pin in the checker; and missing
machine-status, trace, imports, and review fields.

The permitted source salvage keeps the independent exact replay and narrows it
to the finite tables above. It removes the three non-decisive primary runners,
their caches, and the branch-local receipt; removes all Cycle-852/860/861
dependencies and semantic time/gauge/no-go conclusions; makes the remaining
runner fresh-worktree portable; and emits fail-closed exact predicates and the
five N5 quantifier lines.

Hard landing conditions are: a fresh runner-cache envelope for the final
source; successful mutation and implementation-independent checks recorded in
the confirmation-round paragraph; a canonical-harness entry naming this
bounded scope; and a citation-graph manifest regenerated on the actual landing
tree because this note adds a graph node and a dependency edge. No audit
verdict or generated ledger/status output may co-land.

### Iteration 2 — GPT-5.6-Sol/max, 2026-08-15 — confirmation

The final runner completed through `scripts.runner_cache` in 120.99 seconds
with all three certificates and the five N5 quantifier lines passing. An
implementation-independent combinatorial check used the labelled-cycle formula
`11/(11-k) * binomial(11-k,k)` for source-set sizes two through five, obtaining
strata `44, 77, 55, 11`; their sum is 187 and the four seed variants give 748.
An ordinary state-by-state replay, separate from the bit-sliced implementation,
matched every predicate total, capped event list, first-clean boundary, and
first orbit-end clean index for eight dispersed configurations through 200
orbits.

Mutation checks failed closed as required. Changing the Cycle-719 expected
source hash made `SOURCE_CONTROLS` fail immediately with exit code 1. In a
second reverted mutation run, changing the expected corpus size from 748 to
749 and the expected multi-member row count from 85 to 86 made both
`FINITE_REPLAY_TABLE` and `FINITE_COHORT_TABLE` fail with exit code 1. The
source was restored byte-for-byte afterward and the canonical cache remained
fresh for runner SHA-256
`bfe57814d23bef038b8df11cc9821a5f4d5fc494f508c9227dd9817278ab0623`.
The confirmation also renamed the source note so its generated claim ID names
the finite controller census rather than preserving the withdrawn
`time_from_records` interpretation.

## Reproduction

From the repository root:

```bash
python3 -B scripts/frontier_cycle863_865_arc_independent_check_2026_07_28.py
```

The expected terminal marker is:

```text
CYCLE863_865_FINITE_CONTROLLER_CLEAN_EVENT_CENSUS_PASS
```

The canonical cache must be generated only through
`scripts.runner_cache.execute_and_write_cache` using the runner's declared
1,400-second timeout. A direct run is useful for review but is not a cache.

## Verdict

On one supplied two-bank, ring-11, 748-configuration corpus, exact Boolean
replay produces the finite clean-predicate, synchronization, cohort, and offset
tables above. The result is bounded support conditional on Cycle 719. It says
nothing about framework Record formation or physical time, and independent
audit remains required.
