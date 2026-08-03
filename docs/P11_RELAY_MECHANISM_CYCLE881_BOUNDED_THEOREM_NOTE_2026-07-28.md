# P=11 derived: the relay-swap gap, the horizon artifact, and the emptied exception list — Cycle 881

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed campaign-5,
successor to the Cycle-879 discovery; no axiom surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle881_p11_characterization_2026_07_28.py`](../scripts/frontier_cycle881_p11_characterization_2026_07_28.py)
- [`frontier_cycle881_p11_independent_check_2026_07_28.py`](../scripts/frontier_cycle881_p11_independent_check_2026_07_28.py)

Receipt:

- [`p11_characterization_cycle881_receipt_2026_07_28.json`](../outputs/p11_characterization_cycle881_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted; substitution disclosed). Independent audit
still required.

## The mechanism, derived and not guessed

P = 11 is the intra-program index gap between the TWO RELAY_SWAP
stations of a relay edge. Machine-read from `interleaved_program` for
B = 3..8: forward station `f(e) = 4 + 5e`, reverse station
`r(e) = (5B − 3) + 3(B − 2 − e)`, so

    DELTA(B, e) = r(e) − f(e) = 8B − 13 − 8e   on   N(B) = 8B − 5 stations.

Since `3 <= DELTA < N` always, **DELTA is never a whole orbit** — at
any B. An instrumented single-lane kernel trace (reproducing the
corpus clock tick-for-tick) identifies the gating register as the
bank-local (POINTER, U_TO_V, DIRECTION_OK) triple: the leader token
raises it at a RELAY_SWAP station and the follower lowers it sigma
ticks later; the duty cycle (DELTA − sigma clean, sigma dirty) yields
the 6 consecutive residues mod 11 and the (1,1,6,1,1,1) block
structure, all derived from sigma = 5.

## Incidence, exactly

8 keys x 2 clock indices: events {0,1} x placements
{(1,23),(2,24),(3,25),(4,26)}, all sigma = 5, leaders 1-4, clocks
bank2 and pair23; the quiescent window is exactly one 27-tick orbit.
The tempting numerology "11 = 27 − 16" is a COINCIDENCE, refuted
twice (B=3 fires DELTA=3 on 6 clocks; B=4's second class is DELTA=3
on 2 clocks). Token separation alone does not select the class either
(54 keys share sigma = 5).

## The repricing: the orbit law was never a law

Cycle 879 labelled the period result BREAKS_AT_B4 against Cycle 869's
all-orbits finding at B=3. Both labels are HORIZON-CONTINGENT, not
B-axis facts: the relay mechanism fires at B=3 (6 clocks, DELTA=3)
and at B=5 (87 clocks, checker-verified) — but at those substrates
every firing window abuts the horizon, the alignment clause fails,
and the clocks read saturated/no-period. B=4 is visible only because
its window lands at tick ~5430, mid-horizon. Corrected statement:
**non-orbit relay periods exist at every B >= 3 by the DELTA formula;
which substrate EXHIBITS them at a given horizon is an alignment
accident.** Cycle 879's cells stand as scoped (its horizon); its
B-axis framing is repriced here, as Cycle 875 repriced 869's headline
— the chain of blocks correcting each other's readings is functioning
as designed. Also disclosed: a second B=4 class (DELTA=3, 2 clocks)
that 879's detector missed under its declared caps.

## The adjudication: the exception list empties

Running the Cycle-875 leg-(ii) conjunction (RECORD_NATIVE x GLOBAL x
INDEPENDENT_OF_F) over both Cycle-879 exception sets:

- **E1, the P=11 class**: fails GLOBAL (8/648 keys, 2/10 indices) and
  INDEPENDENT_OF_F — DISCHARGED_AT_SCOPE;
- **E2, the 9 non-identity dictionaries** (all F4; recount matches
  879): fails GLOBAL (max 1 key per witness) and INDEPENDENT_OF_F by
  construction — DISCHARGED_AT_SCOPE.

Zero exceptions remain open at this scope. The B-AXIS leg-(ii)
standing itself is untouched (the open rows that remain are the ones
Cycle 875 already names — coverage residues and family closure).

## The conjecture, stated with its falsifier

The DELTA formula predicts the full non-orbit period spectrum
{8B − 13 − 8e : 0 <= e <= B − 2} at every B — verified at B=3,4
(exhaustively) and B=5 ({27,19,11,3} matches; checker-run). The
general claim at all B is a CONJECTURE; its falsifier is any substrate
whose exhibited non-orbit period is outside the DELTA set or whose
DELTA member fails to fire cap-free. Not claimed.

## Checker

Independent `apply_controller_step` replay with no phase-mask
assumption; a CAP-FREE bitmask period detector `S ^ (S >> P)` swept
ALL 6,480 clocks: 16 P=11 clocks, zero misses, zero phantoms, and no
other non-orbit period at B=4. The B=5 stress (never run by the
primary) matched the formula. Refute-spec'd throughout.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the P=11 characterization and the leg-(ii) adjudication of the Cycle-879 exception sets (the named successors of blockT2)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the discharge-map exception rows are supplied with DISCHARGED_AT_SCOPE verdicts (machine-readable); the DELTA-spectrum conjecture with its falsifier is the named frontier; horizon-alignment contingency should be carried wherever period claims are consumed"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the mechanism is machine-read from the program and verified by an instrumented tick-for-tick kernel trace; the formula is exhaustively checked at B=3,4 and stress-checked at B=5; the adjudication verdicts carry witnesses; the repricing is computed, not narrated"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 719 kernel, the 879 corpus and cells, the 875 leg-(ii)
  conjunction (sha-pinned).

### Derived

- the DELTA(B,e) formula and the gating-register mechanism;
- the exact incidence table and the coincidence refutations;
- the horizon-contingency repricing of 869/879's period labels;
- both adjudication verdicts with witnesses.

### Open

- the DELTA-spectrum conjecture at general B (falsifier stated);
- a cap-free period re-census at B=3/B=5 horizons long enough to
  exhibit the predicted classes, if the lane wants the alignment
  contingency retired empirically.

## Verdict

The eleven that broke the orbit law turns out to be the program's own
geometry: the distance between a relay's two swap stations, a number
the ring can never divide. Once derived, the mystery inverts — the
surprise is not that B=4 shows the period but that the other
substrates hide it, and the answer is an alignment accident of the
horizon. The exception list the discovery opened is now empty, closed
by the same conjunction that opened it. Independent audit still
required.
