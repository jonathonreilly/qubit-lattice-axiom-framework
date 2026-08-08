# The B=4 relation run: the translation law strengthens, the orbit law breaks — Cycle 879

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed campaign-5,
closing the B-AXIS discharge map's largest open row; no axiom surface
touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle879_b4_clock_relation_2026_07_28.py`](../scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py)
- [`frontier_cycle879_b4_relation_independent_check_2026_07_28.py`](../scripts/frontier_cycle879_b4_relation_independent_check_2026_07_28.py)

Receipt:

- [`b4_clock_relation_cycle879_receipt_2026_07_28.json`](../outputs/b4_clock_relation_cycle879_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted; substitution disclosed). Independent audit
still required.

## Scope and the disclosed probe deviations

The Cycle-866 B=4 probe re-derived from the 719 core matches its
declaration exactly: 27 stations, 324 separated placements, census
648, 47 watched wires per bank, disjoint. Corpus: 4,770,145 clock
events (5.8x B=3); longest clock 6,512 events. Deviations, disclosed
in the emitted pricing payload: the store cap was set to the horizon
rather than 866's nominal 1,024 — the nominal cap would have truncated
1,788 clocks and silently discarded 1,956,769 events; the across-key
representative cap was raised 600 -> 648 so it cannot bite (max
observed 221); a dict lookup was replaced by a gated-equivalent binary
search. No cap saturated. CAVEAT carried on the comparison table: the
B=3 side (parsed from the sha-pinned 869 cache) ran at the nominal
store cap, so B-comparisons are capped-vs-uncapped where the cap can
matter; the period finding below is a direct membership result and
cannot be a cap artifact on the B=4 side (more data reveals periods;
truncation could only hide them).

## Within-key: the exhaustion persists, weakened

278 of 8,171 substantive comparisons carry a whole-cadence dictionary
(3.4%, vs 2.7% at B=3); 269 are identity-like containment and only
**9 are non-identity**. Bank clocks: 18/3,840 (4 non-identity). Two
family members fire for the first time at scale: F1W, and F4 at
P = 54 = exactly 2 orbits with c in {0, 27}. The within-key negative
stands at B=4, priced to the same family and caps, with a genuinely
larger (still small) exception set whose members are emitted with
witnesses.

## Across-key: the translation law strengthens

At FULL-CORPUS discipline from the start (the Cycle-875 standard;
the pair-only sub-corpus 3,094/3,094 with residue 371 is emitted
labelled, never as headline): **5,085 of 5,085 F1 edges carry nonzero
offsets**; the uncovered residue is 803 of 6,258 sounding keys (87.2%
covered, up from B=3's 86.4%); the F3 factor layer holds 2,367 edges.
Same cadence, different origin remains the law, and it gets slightly
stronger with scale.

## The break: the orbit-commensurability law is a B=3 accident

At B=3 every nondegenerate period was a whole number of 19-station
orbits. At B=4, six of seven are whole 27-station orbits
(27, 54, 81, 1512, 1971, 2214) — and **P = 11 is not**
(11/27 of an orbit; 16 clocks; block gaps (1,1,6,1,1,1); a 17-event
stable tail; 6 residues). The period survives the checker's
independent detector and the direct membership adjudication
(t in S iff t+11 in S), and P = 27 fails on exactly those clocks. The
checker's L3 mutation control catches the claim flipped in EITHER
direction, so the finding is gated both ways. This is the one B=3
structural fact that breaks at B=4.

## The comparison table (data, not narrative)

Against the sha-pinned 869 figures: 4 facts PERSIST_STRENGTHENED, 1
UNCHANGED, 3 WEAKENED, 1 BREAKS_AT_B4 — each row computed, with the
capped-vs-uncapped caveat above attached to the WEAKENED labels.

## What this does to the B-AXIS discharge map

The map's largest open row ("the entire B=4 relation-family run") is
now SUPPLIED with data. It does not auto-discharge leg (ii): the 9
non-identity within-key dictionaries and the P=11 clock class must be
adjudicated against the leg-(ii) conjunction (record-native x global x
independent-of-F) before the row's status moves — the P=11 class is 16
clocks (prima facie local, not global), but adjudication is a
successor's job, not this note's. The named successors: the P=11
characterization block, and the leg-(ii) adjudication update.

## Checker

Genuinely refuting: its wider search found 2,733 substantive matches
(vs the primary's 496 at declared caps) and 32 refutation-grade
non-identity relations against a published budget of 39 — close, not
exceeded, and the budget check is a real gate. NINE mutation controls
each fail exactly the intended gate and no other (corpus sha; clean
counts; period flipped either way; headline scoped to the sub-corpus;
narrowed denominator; understated deviation; inflated identity class;
zeroed non-identity budget -> REFUTES_PRIMARY). Import firewall
verified to fire; both runners deterministic across PYTHONHASHSEED.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the ENTIRE B=4 relation-family run (the B-AXIS discharge map's largest open row, Cycle 875)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "adjudicate the 9 non-identity dictionaries and the P=11 class against the leg-(ii) conjunction; characterize the P=11 clock class (which keys, which banks, what mechanism sets an 11-tick period on a 27-station ring)"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the declared family re-run exactly at B=4 with witnesses; the period break gated by direct membership adjudication and a both-ways mutation control; deviations disclosed and priced; full-corpus headline discipline from the start"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 719 kernel and the 866-declared B=4 probe (sha-pinned,
  re-derived);
- the 869/875 figures as pinned comparison targets (parsed from
  caches, never assumed).

### Derived

- the B=4 within-key decomposition with witnesses;
- the full-corpus translation law at B=4 with its residue and factor
  layer;
- the period census and the P=11 non-commensurate class;
- the computed B-dependence table.

### Open

- the P=11 characterization (mechanism, key/bank incidence);
- the leg-(ii) adjudication of the new exception sets;
- capped-vs-capped re-comparison if the audit lane wants the B=3 side
  uncapped too.

## Verdict

Scale was the test the B=3 story had not faced, and it split the
story cleanly: the relativity-between-origins law came through
stronger, the no-dictionary-within-a-world negative came through
intact but humbler — and the tidy rule that every clock beats in whole
orbits did not come through at all. Sixteen clocks at B=4 keep an
11-tick period on a 27-station ring, and nothing in the landed story
says why. That is the best kind of open item. Independent audit still
required.
