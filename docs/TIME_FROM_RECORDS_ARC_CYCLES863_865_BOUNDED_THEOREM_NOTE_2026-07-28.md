# Time from records — the arc: intrinsic events, gauge tick, lawful offsets — Cycles 863–865

Date: 2026-08-02

Authority: none

Audit: unset

Status: bounded worked results (three supervisor-authored primaries,
one comprehensive independent checker; owner-directed
formation-is-the-tick program; no axiom surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle863_time_from_records_2026_07_28.py`](../scripts/frontier_cycle863_time_from_records_2026_07_28.py)
- [`frontier_cycle864_laws_in_record_time_2026_07_28.py`](../scripts/frontier_cycle864_laws_in_record_time_2026_07_28.py)
- [`frontier_cycle865_offset_law_2026_07_28.py`](../scripts/frontier_cycle865_offset_law_2026_07_28.py)
- [`frontier_cycle863_865_arc_independent_check_2026_07_28.py`](../scripts/frontier_cycle863_865_arc_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or
audit status.

## Result up front

The owner's identification — record formation IS the tick — tested to
the ground on the 852 census (748 worlds, horizon 51,115), all
checker-verified:

- **the events are intrinsic (863-C)**: the E1 record structure is
  definable as "the first formation event," 182/182 scheduler-free —
  the event-level identification is a theorem at this scope;
- **the supplied tick does not re-derive from records (863-B)**:
  bank-synchronization events sit on orbit boundaries only ~14% of
  the time; first-sync reproduces the landed E2 census for 25/114
  keys with 624 spurious — at two-bank scope the orbit cadence is
  extra structure beyond the record pattern. Checker correction
  absorbed: the primary's `sync_events_total` field is
  STORE-CAPPED (4,096 events/world); the uncapped total is
  **6,821,527**; the qualitative verdict is unchanged and now stands
  on the honest total;
- **the landed moment law transforms, near-losslessly (864-A)**:
  scheduler-cohorts are nearly synchronized in record-age (stamp
  rung), spreads 0–5 across the 15 multi-member cohorts —
  MOMENT_LAW_TRANSFORMS; periodicity MIXED with the store-cap
  censoring made exact by the checker (two of eight extended
  "aperiodic" keys were cap artifacts);
- **the offsets are lawful (865)**: within-cohort record-age offsets
  are an EXACT function of one datum — the world's set moment (birth
  time): 85 member rows, 50 predictor classes, 35 nontrivial
  agreement instances, zero violations; all seven rival predictors
  fail with witnesses — OFFSETS_LAWFUL_SINGLE:e1_moment, non-vacuous;
- **the residue is priced (checker, constructive)**: NO non-vacuous
  RECORD-NATIVE predictor reproduces the offsets across 29 singles
  and 28 pairs — the birth datum stays a gauge coordinate at this
  scope;
- **the timeless sector is real ontology at scope (864-C)**: 566 of
  748 worlds never have a clean event — under the identification,
  worlds where time never passes; their regularities (meets, marks,
  state periods) are gauge-layer content by scope;
- **the saturation probe is honestly uninformative (863-A + checker)**:
  neither the one-chunk nor the full-orbit counterfactual
  discriminates formation from control (the one-chunk contrast also
  drops trailing gates — checker diagnosis); formation-as-exhaustion
  remains UNTESTED pending the composed record-write model;
- **the B-AXIS contact (864-D)**: the ANOMALY_FORCES_TIME theorem's
  B-AXIS premise discharges iff (i) the laws restate in record-time
  — the (i)-leg evidence is this arc — and (ii) no second record
  clock exists — untested, owned by the scaled-bank construction.

**The standing picture**: anomaly consistency forces exactly one time
axis; formation events are its intrinsic clicks; every landed
temporal law tested restates in record-time up to one lawful gauge
datum per world (the birth time), which no record-native structure
replaces at two-bank scope. The scheduler carries no law; it labels
initial conditions. The E1/E2 fork trends toward dissolution-as-gauge
rather than decision — final standing awaits the scaled-bank leg.

## Supplied / derived / open

### Supplied

- the 719 core; the 852/860/861 certified machinery lineage
  (sha-pinned; 863 imported by 864/865 as a pinned core, the same
  pattern as 719); everything the cited packages declare.

### Derived

- the intrinsic-E1 theorem; the sync/tick mismatch on honest totals;
  the record-age transform of the moment law; the offset law with its
  non-vacuity arithmetic; the intrinsic-predictor exhaustion; the
  probe-inadequacy diagnoses.

### Open

- the scaled-bank construction (the derived-clock and no-second-clock
  legs; the birth-datum intrinsicness); the composed record-write
  model (formation-as-saturation's honest test); the rate law.

## Negative-claim discipline

Every negative is scoped: the tick non-derivation is at two-bank
scope on the stated horizon; the store-cap corrections are absorbed
with the capped fields named; the intrinsic-predictor exhaustion is
at the declared 29+28 family; probe inadequacy is claimed for the two
probes tried, not for all probes.

## Checker disclosure and incident note

One comprehensive checker covers the arc (the three primaries share
one replay substrate); its corrections (store-capped totals; cap
artifacts) are absorbed here and in the receipt without editing the
primaries' as-run bytes — the capped fields are documented, not
renamed. Mid-arc, the machine's worktree-cleanup automation deleted
three scratchpad worktree gitfiles; all commits were already in the
shared object store, the branch was pushed for protection, and the
worktrees were rebuilt from primary-repo metadata; process rules
banked (push supervisor commits immediately; scratchpad worktrees are
prunable at any moment).

## Verdict

Asked whether time is what records do, the smallest laboratory
answered with unusual precision: the clicks are real and belong to no
clock but their own; the laws follow them; and all that remains of
the scheduler is a birth certificate for each world — one number,
lawful, and so far irreplaceable. Independent audit still required.
