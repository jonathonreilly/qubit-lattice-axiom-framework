# One wire-write makes the substrate Born-capable: the first branch pairs exist, and the obstruction moves — Cycle 918

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed Born-lane successor,
window 2b; no axiom surface touched). The named successor from Cycle
913 is STARTED, not deferred: three minimal modifications that make
the endpoint wires gate targets are constructed against the pinned
719/863 kernel, spliced (never rebuilt), and measured over the full
748-world census at the 16,384-orbit horizon in both lane layouts.
One is BORN-CAPABLE — 37 lock points realize an item their setup did
not prepare, and the first THREE dynamical branch pairs in the
framework's history exist — one is DESTRUCTIVE with its obstruction
named, one is STERILE with its mechanism measured. The block also
sharpens the successor's own successor: a writable endpoint is
NECESSARY for realized selection but NOT SUFFICIENT for O3 — the
remaining obstruction is that a gate set is a law, and a law is a
function.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle918_writable_endpoint_2026_07_28.py`](../scripts/frontier_cycle918_writable_endpoint_2026_07_28.py)
- [`frontier_cycle918_writable_independent_check_2026_07_28.py`](../scripts/frontier_cycle918_writable_independent_check_2026_07_28.py)

Receipt:

- [`writable_endpoint_cycle918_receipt_2026_07_28.json`](../outputs/writable_endpoint_cycle918_receipt_2026_07_28.json)
- [`writable_independent_check_cycle918_receipt_2026_07_28.json`](../outputs/writable_independent_check_cycle918_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. The pinned kernel file is never edited — every modification is
a schedule splice. One owner-facing surface is EMITTED, not decided
(the M_A constraint tension, below).

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). M_B's gate vocabulary (SHIFT) is
OUTSIDE the certified set — the very thing the 911 sweep forbids —
and is declared as such: it is in the design space precisely to
measure what the cross-lane axis costs. Independent audit still
required.

## The three modifications (exact gate forms)

All three are appended to the SOURCE station's macro (station 0 —
the station that already reads both endpoint wires), masked by that
station's own lane mask, with REC_A = 123 (bank-0 POINTER) and
REC_B = 254 (bank-1 POINTER — the lock site's two nearest neighbours
under the 911 embedding); LEFT = 1, RIGHT = 6. Flipping both wires
with one control IS the menu swap (1,0) <-> (0,1), so M_A and M_C
stay on-menu by construction. Gate count 34,166 -> 34,188; Cycle
913's reads-never-writes lemma is negated by all three.

- **M_A (record-driven):** `c[1] ^= c[123] & mask`;
  `c[6] ^= c[123] & mask` — two CNOTs, certified vocabulary.
- **M_B (cross-lane):** `c[1] ^= (c[1] >> 1) & mask`;
  `c[6] ^= (c[6] >> 1) & mask` — two SHIFTs, outside-vocabulary
  (declared).
- **M_C (local-content):** `c[1] ^= c[123] & c[254] & mask`;
  `c[6] ^= c[123] & c[254] & mask` — two Toffolis, certified
  vocabulary.

## The census (748 worlds, 180,224 boundaries, both layouts)

| | locks | lost/gained | endpoint writes | sel != setup | dynamical branch pairs | Z11 | layout |
|---|---|---|---|---|---|---|---|
| CONTROL | 164 | 0/0 | 0 | 0 | 0 | invariant | ok |
| M_A | 134 | 32/2 | 38,736,016 | **37** | **3** | 124 violations | ok |
| M_B | 142 | 71/49 | 32,486,656 | 29 | 2 | 78 violations | **fails** |
| M_C | 154 | 10/0 | 18,647,166 | 0 | 0 | invariant | ok |

Write-count parity at the lock: M_A {even: 97, odd: 37} (up to
5,206 endpoint writes before a lock); M_C {even: 154} — its control
fires only an even number of times before every lock, which is
exactly why it is sterile.

## Verdicts and pricing

- **M_A = BORN-CAPABLE.** 37 lock points realize an item their
  setup did not prepare; 3 dynamical branch pairs ([253,407],
  [520,630], [533,643]) out of 27 candidate pairs. It preserves
  write-once, the dead-wire slots, formation, the menu, lane
  locality, layout independence, and the certified vocabulary.
  **Price:** the 913 transport theorem is supplemented (not
  contradicted — the control reproduces it exactly); the
  monitor-phase Z11 invariance of the REALIZED selection is lost
  (124 violations); 32 worlds stop forming inside the horizon
  (2 new ones form).
- **M_B = DESTRUCTIVE, obstruction named.** Duplicate-lane
  consistency lost (2 witnesses); forward vs reversed layouts
  diverge (142 vs 135 locks); the 911 AST cross-lane certification
  fails; a runtime perturbation witness leaks. The "neighbour" a
  shift addresses is a bookkeeping artefact, so the cross-lane law
  is not well defined — the axis dies structurally, not by taste.
- **M_C = STERILE, mechanism measured.** Endpoints move (67 locks
  carry writes) but no lock point leaves its setup value: the
  two-record control fires only in even numbers before every lock
  (the parity table), so every flip undoes itself.

## The A3 arena under M_A (every caveat attached)

134 lock points x 2 = 268 site-possibility pairs; realized
(1,0) -> 78 and (0,1) -> 56 across the 67 write-bearing locks;
within-pair split 3 of 27 (1/9). These are BOOKKEEPING FRACTIONS:
counts over distinct setups, not within-setup frequencies, and the
modification that produces them is an IMPORT (a constructed
candidate, not derived dynamics). The A3 sentence is not advanced
by these numbers; they size the arena it would govern.

## The two sharpening findings

1. **Necessary, not sufficient.** The Cycle-911 branch class
   (two worlds sharing schedule AND tick-0 state, diverging later)
   is EMPTY for every gate set including M_A — and this is a CENSUS
   fact: no two census worlds share both. The determinism lemma
   makes it structural: a gate set is a law, identical
   (schedule, tick-0 state) cannot diverge, and a cross-lane escape
   destroys its own premise (M_B). So a writable endpoint buys
   realized selection (O2's object becomes dynamical) while O3's
   obstruction RELOCATES: from "the distinguishing coordinate is
   frozen" to "the law is a function." The successor's successor is
   a substrate whose law is not a function of (schedule, tick-0
   state) — named, not started.
2. **Selection still lives on the endpoint pair.** Even under M_A,
   the realized selection is determined by wires [1,6] alone — not
   nearest-neighbour record content, not ordinals, not openness,
   not the site block minus the endpoints, not the widest non-site
   context. The write moved the selection from SETUP COORDINATE to
   TRAJECTORY HISTORY, not to neighbourhood conditions; the
   Admissibility-sentence-shaped dependence is still absent.

## The owner-facing surface (emitted, not decided)

M_A meets the block's declared constraints (a) write-once/records
and (b) formation/menu, and fails (c) monitor-phase covariance of
the realized selection. Under the declared verdict criteria
(DESTRUCTIVE = breaking (a)/(b)) it is Born-capable; the (c) loss
is measured and PRICED, not resolved. Whether a Born-capable
substrate may trade monitor-phase covariance of realized selection
is a registration-shaped question for the ledger — this block takes
no position and nothing here needs a decision to stand.

## Gates, teeth, checker

Restriction gates 41/41: the control build digest-identical to the
pinned 913 build in BOTH layouts; the 911 lock set, boundaries,
keys, and range value-for-value; the 913 selection table row-for-row
(84/80); the 913 endpoint lemma; 878's 92,260 events / 748 worlds /
3,856,705 beyond-cap; the pinned compile_fast source text; the
pinned 911 snapshot_scan on a 128-orbit cross-check window. Primary
teeth 14/14 with all three verdict classes reachable by synthetic
probe. Checker: PRIMARY_SURVIVES_THIS_CHECK — independent mechanism
(the pinned 863 compiler's own schedules with the gates spliced at a
computed offset, never a rebuild; own scan; own per-lane counters —
explicit enumeration vs the primary's bit-plane ripple adder; own
Z11 action built from the census); 38/38 checks, 8/8 teeth. The
checker found and CLOSED the one real gap: the primary derived the
878 dead-wire rig only from the control — the checker re-derived
the whole rig UNDER EACH modification (dead 5,668 / safe 5,270,
identical everywhere; inherited slots still dead and safe) and
re-derived write-once from event-triple uniqueness plus ordinal
monotonicity without the primary's ledger. Runtimes: primary 324 s,
checker 386 s.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the Born lane's named successor (Cycle 913): a substrate where endpoint content is a gate target — constructed, not deferred"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the design space is mapped: record-driven = BORN-CAPABLE (first branch pairs [253,407]/[520,630]/[533,643]; priced by the Z11 loss and 32 unformed worlds), cross-lane = DESTRUCTIVE (the neighbour is bookkeeping), local-content = STERILE (even-parity mechanism); carry the necessity/insufficiency split — writable endpoints buy O2's object, O3's obstruction relocates to 'the law is a function of (schedule, tick-0 state)'; the successor's successor is a substrate breaking that functional dependence; the M_A constraint-(c) tension goes to the ledger as a registration-shaped surface"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "all verdicts are at the block's declared constraint set and verdict criteria (stated in full in the receipt); M_A's Born-capability is relative to criteria under which the (c) monitor-phase loss is a price, not a disqualifier; the A3-arena fractions are bookkeeping counts over distinct setups, not within-setup frequencies; M_B's vocabulary is declared outside the certified set"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the kernel is never edited (splice-only, AST-verified); the control is digest-identical to the pinned 913 build in both layouts with the full 913/911/878 surface reproduced value-for-value; every verdict survives an independent checker with its own splice mechanism, counters, and Z11 action; the checker closed the one gap it found by re-deriving the dead-wire rig under each modification; the branch pairs are exhibited with world indices"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the pinned 719/863 kernel pair and compiler (the substrate under
  test; spliced, never edited); the pinned 911/913/878 primaries +
  receipts (the restriction-gate authority); the three candidate
  modifications themselves (constructed imports — the design space,
  not derived dynamics).

### Derived

- the three-verdict map (BORN-CAPABLE / DESTRUCTIVE / STERILE) with
  each mechanism exhibited (write parity, layout divergence, the
  named M_B obstruction);
- the first three dynamical branch pairs, with the full census
  behind them;
- the necessity/insufficiency split and the determinism lemma (the
  O3 obstruction's relocation);
- the selection-locality persistence (wires [1,6] under M_A);
- the A3-arena sizing with its caveats;
- the priced M_A constraint tension (the owner-facing surface).

### Open

- the successor's successor: a substrate whose law is not a
  function of (schedule, tick-0 state) — named by the determinism
  lemma, not started;
- the M_A (c)-tension registration (ledger surface, no decision
  needed here);
- the A3 sentence itself (unchanged: one sentence, deferred behind
  the substrate line);
- the audit-lane rows (unchanged docket).

## Verdict

The lane asked for the smallest change that would let the substrate
choose, and the answer is two CNOTs: wire the record banks to the
endpoint pair and thirty-seven worlds lock onto values their setups
never prepared, three of them in genuine branch pairs — the first
in this framework's history. The other two candidates die
instructively: the cross-lane law was never well defined, and the
local-content law cancels itself in even strokes. What the
capability costs is measured to the world: a monitor symmetry of
the realized choice, and thirty-two worlds that no longer form.
And the deepest thing the block bought is the relocation of the
remaining wall — the endpoint was never the last obstruction, the
functional form of law was; that wall now has a name, a lemma, and
a successor substrate specified against it. Independent audit
still required.
