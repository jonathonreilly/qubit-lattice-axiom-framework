# The stratified ladder — k=4 and k=5 meet unmarked — Cycle 850

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the k=4/k=5 meeting structures exact;
the no-mark exhaustions at both strata; the ladder verdict)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle850_stratum_mark_ladder_2026_07_28.py`](../scripts/frontier_cycle850_stratum_mark_ladder_2026_07_28.py)
- [`frontier_cycle850_ladder_independent_check_2026_07_28.py`](../scripts/frontier_cycle850_ladder_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 849 proved the k=3 stratum is marked at its meets. The natural
generalization — every stratum marks its meets, and only the schedule
distinguishes them — is **FALSE**: the ladder is stratified.

- **the meeting structures exist and are exact**: k=4 (population 55
  keys, 220 event keys) meets as 11 tick-3 single-center events plus
  44 tick-4 triple-center events; k=5 (population 11 keys, 44 event
  keys) meets as 11 tick-4 single-center events — both derived from
  the 719 core and re-derived independently by the checker;
- **no native mark exists at either stratum**: the exhaustions cover
  all 5,815 single bits and all 16,904,205 bit-pairs, with zero
  survivors in both directions at both strata;
- **the checker's constructive extension also came up empty**: bounded
  bit-triples anchored on the k=3 mark bits {256, 262} and the meet
  center supports, plus inequality-form pair predicates — no mark;
- **the k=3 regression holds**: under the checker's independent
  machinery the landed mark `bit[256] == bit[262]` still separates on
  its own stratum, so the stratification rests on one consistent
  computation;
- verdict: `LADDER_STRATIFIED`.

**What this changes**: marking is a LOW-STRATUM property, not a
generic feature of the machinery. The strata now sit in three
structurally distinct tiers — k=2 marked and fired, k=3 marked and
waiting, k=4/k=5 meeting but unmarked. The Cycle-849 scheduling
contrast keeps exactly its stated scope (k=2 vs k=3) and does not
extend upward; any eventual record-formation account for the high
strata cannot ride a meet-mark, because there is none to ride.

## Supplied / derived / open

### Supplied

- the 719 two-rail controller core (sha-pinned); the landed 849
  meeting/mark machinery as declared; everything the cited packages
  declare.

### Derived

- both strata's populations, event keys, and full meeting structures;
  the two no-mark exhaustions; the checker's extended-family
  exhaustion; the k=3 regression.

### Open

- what, if anything, plays the mark's role for k=4/k=5 record
  formation (decided at axiom level by the pending owner sentence);
  the merged why; the off-backbone quiet.

## Negative-claim discipline

The no-mark verdicts are exhaustive at the declared families (all
single bits; all bit-pairs; the checker's bounded triple and
inequality extensions) at the censused meets. They are not claims
about arbitrary predicates.

## Verdict

The ladder does not climb. Two strata carry marks; two do not; and
the one mark that waits (k=3) is now known to be special rather than
typical. Whatever stamps the high strata — if anything ever does — it
will not be a meet-mark, because we have looked at every one there
could be. Independent audit still required.
