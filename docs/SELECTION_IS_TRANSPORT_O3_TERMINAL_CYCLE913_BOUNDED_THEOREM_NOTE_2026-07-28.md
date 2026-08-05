# The dynamics never chooses: the selection is transported setup, and the weight question ends here — Cycle 913

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed Born-lane closure,
window 2; no axiom surface touched). O2 — which possibility the
landed dynamics selects at the 164 lock points — is computed
completely, and the answer re-frames the whole question: **the
landed scan never chooses**. The selection is the transport of one
setup coordinate (event parity), carried on two wires that every
compiled gate reads and none ever writes. O2 is SUPPLIED, not
derivable, on this substrate; O3 has NO non-forbidden realization
here, with the A3 arena located exactly and the successor substrate
named.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle913_selection_function_2026_07_28.py`](../scripts/frontier_cycle913_selection_function_2026_07_28.py)
- [`frontier_cycle913_selection_independent_check_2026_07_28.py`](../scripts/frontier_cycle913_selection_independent_check_2026_07_28.py)

Receipt:

- [`selection_function_cycle913_receipt_2026_07_28.json`](../outputs/selection_function_cycle913_receipt_2026_07_28.json)
- [`selection_independent_check_cycle913_receipt_2026_07_28.json`](../outputs/selection_independent_check_cycle913_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). Both runners flag the fingerprint-
vacuity trap explicitly (a dependence analysis without that flag
would have reported a false determination); the lock's polarity is
stated plainly (the first GLOBALLY CLEAN tick, not the first dirty
one). Independent audit still required.

## Q1 — the selection table, quadruple-read

All 164 lock points read by four independent readouts agreeing
row-for-row (endpoint content; unique Hamming-1 menu item; the
scan's own re-arm; the seed's direction). Split: 84 realize (1,0),
80 realize (0,1) — perfectly aligned with setup event index (even
events select (1,0), odd select (0,1)). The re-arm readout is the
load-bearing one and stronger than specified: at the first post-lock
source-pointer rise, the scan's state equals the kernel's OWN
endpoint constructor applied to exactly one menu item —
bit-for-bit on all 5,815 wires, at 164/164 lock points, with the
counterfactual differing at exactly two wires. **The structural
lemma (compile-level, exact): across all 34,166 compiled gates, the
two endpoint wires are gate INPUTS and never gate TARGETS. The
landed dynamics reads the selection; it never writes it.**

## Q2 — what determines it: nothing the axioms talk about

- **Not local**: nearest-neighbour grouping yields a 30-point
  collision class splitting 15/15, with the canonical witness pair
  exhibited (worlds 95 and 51: identical neighbour conditions,
  identical everything outside the site, different selection).
  Widening to radius 2 and 3 changes NOTHING (the substrate is
  exhausted at radius 1 — everything further out is zero at every
  lock), so by monotonicity no neighbour-shell fingerprint at any
  radius can determine. The schedule/tick/token ladder entries that
  eventually become injective are flagged DETERMINATION-IS-VACUOUS
  (they name the site rather than describe it) and excluded from
  minimality.
- **The minimal determining context, exhaustively**: of 5,815 wires,
  88 vary across lock states and EXACTLY TWO determine — wires 1 and
  6, the endpoint pair itself, both inside the site; no outside wire
  determines alone or in any pair (3,655 pairs swept by the
  checker). In setup coordinates the determining bit is EVENT
  PARITY.
- **Not content**, under all three readings — including the sharpest:
  67 lock points have written NO record event at all and still split
  51/16. The selected possibility is not a readout value in the
  Record axiom's sense; it is carried on non-record wires.
- **The contexts DO vary** (54 distinct nearest-neighbour contexts in
  3/6/7 cubic classes — reproducing 911's class sizes) — so the
  Admissibility "vary with" clause has material to bite on, and the
  landed rule ignores it: the 911 menu-size insensitivity and this
  block's selection insensitivity have the SAME structural cause
  (the only distinguishing coordinate is never written).
- **Covariance**: translation-invariant trivially (a transported
  constant per world; 784 checks, 0 violations); NOT
  rotation-class-constant at any k — because it is not a function of
  the colouring at all.

## Q3 — the ledger verdict

**(i) O2 is SUPPLIED, and now measured**: realized(w) = (1,0) iff
the setup event index is even — the transport of a setup coordinate,
not a formation rule about neighbourhoods. The classified covariant
rule space (its counts reproduced from scratch: 10/10, 57/56, 240/220
matching the note's byte-quotes) does not contain it — every member
is a function of the neighbour colouring and the landed selection is
not. Its positive placement: restricted to either setup sector it IS
the constant rule (achiral, fully covariant), and the pair of
constant rules is a supplied-structure-indistinguishable pair whose
member is fixed by one imported bit — the classification note's own
dichotomy, resolved by initial condition. **Not derivable on this
substrate.**

**(ii) O3 is TERMINAL here.** Each world locks exactly once — the
within-world frequency is degenerate and no weight is estimable
inside a world. The A3 arena is located exactly: 164 sites x 2
possibilities = 328 site-possibility pairs, 164 realized and 164
counterfactual. The cross-world 84/80 split is an average over
setups — the operation the realized-state primitive forbids
verbatim. And the dependence result sharpens the obstruction to
closure: the coordinate that distinguishes the two possibilities IS
a setup coordinate never written by the dynamics, so a weight over
the counterfactual menu is a weight over setups UNDER ANOTHER NAME.
**O3 has no non-forbidden realization on this substrate.** Supplying
it requires either a substrate where the endpoint content is a gate
TARGET (the named successor — the precise engineering statement of
what a Born-capable substrate must have) or the A3 sentence as an
import.

## Checker

31 pass / 0 fail; the fingerprint attack (the specified hardest)
recomputed all 19 ladder groupings under its own integer encoding
with a third encoding agreeing on the decisive entries; the witness
pair reproduced; 146 fully semantic replays from tick 0; its own
lane permutation, chunk compiler, and cubic machinery; 8/8 teeth.
The primary's nine falsifiers include outcome-neutrality BOTH ways
(a planted local selection is detected as local). Restriction gates
39/39 with 911's menus recomputed from its own AST-lifted operators.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "O2 as a computation: which possibility does the landed deterministic scan select at each of the 164 lock points, and what determines it — the Born lane's correctly-typed remainder after the Cycle-911 re-typing"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "O2 measured (event-parity transport on never-written wires; supplied, not derivable; not a member of the classified rule space); O3 TERMINAL on this substrate (the counterfactual-menu weight IS a setup weight under another name; the A3 arena = the 328 site-possibility pairs); the NAMED SUCCESSOR is a substrate where endpoint content is a gate target — next campaign's opening object; carry the fingerprint-vacuity flag and the lock-polarity clarification into any consumer; the Born lane's window-2 closure assessment follows this block"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the O2/O3 verdicts are substrate-scoped (this census's landed scan at the pinned horizon); the successor substrate is named, not built"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the selection table is quadruple-read with bit-level re-arm verification at every lock point; the structural lemma is compile-level and exact; the non-locality carries an exhibited witness with the substrate provably exhausted at radius 1; the minimal-context sweep is exhaustive over wires and checker-swept over pairs; the vacuity trap is flagged by both runners; outcome-neutrality is demonstrated in both directions"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- twelve pins incl. the 911 primary + receipt + note, the 863/878
  primaries + receipts, the covariance-classification runner + note,
  the axiom memo, and the realized-state primitive note; the 719
  kernel as substrate (disclosed).

### Derived

- the complete quadruple-read selection table and the
  reads-never-writes structural lemma;
- the non-locality theorem with witness and the radius-1 exhaustion;
- the exhaustive minimal-context result (event parity; wires 1/6);
- the not-content and covariance results; the one-sided-gap
  companion to 911's caveat;
- the O2 supplied-not-derivable verdict with the classified-space
  placement;
- the O3 terminality with the located A3 arena and the named
  successor substrate.

### Open

- the successor substrate (endpoint content as a gate target) — the
  next campaign's opening object;
- the owner-surface registrations accumulated by the lane
  (P-SAMPLE-SPACE; P-WITHIN-WORLD; the A3 import if ever taken);
- the audit-lane propagations (the stranded note's landing; the
  878/863 flags).

## Verdict

The lane's last question had the humblest possible answer: nobody is
choosing. The two futures that stand open at every formation moment
are told apart by a single bit that was written before the dynamics
began and that no gate in the machine can touch — the scan does not
select an outcome, it delivers a decision made by the setup. That
closes O2 as measurement, closes O3 as impossibility, and converts
the Born question into an engineering specification one sentence
long: build the substrate where the endpoint is writable, or import
the sentence that says weights exist. The lane ends its window
knowing exactly which wall is real, where it stands, and what would
count as a door. Independent audit still required.
