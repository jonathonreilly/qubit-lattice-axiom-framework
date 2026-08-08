# The measurement was right and the floor was a grid line: the deposition comparator re-audited — Cycle 920

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane closure,
window 2b; no axiom surface touched). The never-checked comparator
that supplied the lineage's 0.20 theta floor gets the full
independent-reimplementation treatment: the historical measurement
REPRODUCES exactly (22/22 quantities, three implementations) — and
the floor it was read to support is a GRID ARTIFACT: the true
crossing sits at theta = 0.1405, the declared 0.20 is the smallest
swept point above it, the criterion's namesake quantity cancels
algebraically out of its own definition, and the "sparse window"
rests on one event plus eleven structurally-zero cells. One premise
of the Cycle-916 dictionary is corrected, not retracted.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle920_deposition_reaudit_2026_07_28.py`](../scripts/frontier_cycle920_deposition_reaudit_2026_07_28.py)
- [`frontier_cycle920_deposition_independent_check_2026_07_28.py`](../scripts/frontier_cycle920_deposition_independent_check_2026_07_28.py)

Receipt:

- [`deposition_reaudit_cycle920_receipt_2026_07_28.json`](../outputs/deposition_reaudit_cycle920_receipt_2026_07_28.json)
- [`deposition_independent_check_cycle920_receipt_2026_07_28.json`](../outputs/deposition_independent_check_cycle920_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Eight audit rows are emitted; the 916-record correction (B2)
is flagged for a follow-up edit rather than left as two disagreeing
receipts.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). All recovered artifacts verified
against the 916-recorded digests before use (commands disclosed);
zero imports from the historical engine — the reimplementation is
from the note's equations, with the checker supplying a genuinely
THIRD construction. Independent audit still required.

## Q1 — reproduced, exactly

Own basis (the charge-zero Fock x rotor sector, dim 8316), own
Hamiltonian with the Jordan-Wigner signs derived in-block, own
ground state, own propagator, own bond observables. **All 22
compared quantities agree**: every once-count and re-arm count
vector identically; the amplitude table to 5e-5; the ground-state
baseline range to 1.4e-12; the energies to 9e-15; the declared floor
at 0.20. **The historical measurement is correct as published** —
the third implementation (the checker's full operator-algebra
construction, nnz matching entrywise) agrees at 9e-14 on the
decisive crossings.

## Q2 — the floor's true status: GRID ARTIFACT

- **The true crossing is theta = 0.140516818611** (bisected to
  1e-14; the joint fill is monotone). The declared 0.20 overshoots
  it by a factor 1.4233 and is simply the smallest of six
  hand-chosen thresholds above it — nothing in (0.1, 0.2) was ever
  examined.
- **The namesake quantity cancels**: fill = kappa * (A/N) = N/12
  IDENTICALLY (deviation 4.4e-16) — "deposition per activity" plays
  no role in its own floor; the criterion is a quantized
  crossing-count ("at most 3 of 12 bonds"), and any wake bound in
  [0.25, 0.3333) gives the identical floor.
- **Saturation confirmed and sharpened**: floor/max-attainable =
  0.9593 (reproducing 916's 95.9%); of the twelve gated cells at
  theta >= 0.2, ELEVEN are zero by construction — the entire
  "transient-complete cascade above the floor" rests on ONE event.
- **Not a convention artifact**: the interacting-GS baseline and the
  trajectory-t0 baseline coincide bond-by-bond to 3.3e-16 on B's own
  system (both kicks are occupation-diagonal, so bond purity is
  invariant) — **which corrects the 916 dictionary's premise B2**:
  the A-vs-B mismatch is a PREPARATION difference (product quench vs
  local kick on an entangled ground state), not a baseline-kind
  difference. The bridge still needs five premises; B2's content
  changes.
- **Parameter-pinned, and the grid hides the physics**: the note
  names no alternatives; across the engine's own declared range,
  W_max is fully converged, and moving the mass moves the TRUE
  crossing by +32% (0.1405 to 0.1849) while the GRID floor never
  moves at all — the grid is too coarse to see the dependence it
  conceals.

## Q3 — the lineage verdict and the audit rows

**0.20 is a grid label, not a measured threshold.** Completing the
915/916 citation work from the source side: the d=3 lineage's floor
citation dies twice over — the A-vs-B category error (916) and now
the source-side grid artifact (920). Eight audit rows emitted,
including: the API drift re-verified (B still runs only from
history); and **the grid mislabel confirmed OUTCOME-BEARING at
source** — the cache prints a 6-unit protocol while executing a
10-unit one, and on the printed grid all four published count
vectors would differ (the floor happens to survive; any future
citation of B's COUNTS cites numbers the stated protocol does not
produce).

## Gates, falsifiers, checker

Restriction gates hard-fail against the recovered cache bytes: all
pass value-for-value. Primary falsifiers all fire (a perturbed mass,
a holonomy-free construction, a planted cascade that relocates the
floor, a single-cell disagreement flipping Q1, a planted baseline
offset, grid-closure relocation); deterministic double-run bitwise.
Checker: 6/6 claims survive, none refuting; 11/11 teeth; the
declared system attacked against the note's, runner's, and engine's
own bytes (all terms, both kicks); the decisive crossings
independently found at 9e-14.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the never-independently-checked deposition comparator (the source of the lineage's 0.20 theta floor; runs only from history) — the 914 re-audit pattern applied"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the measurement REPRODUCES (three implementations); the floor is a GRID ARTIFACT (true crossing 0.1405; the namesake quantity cancels; one-event support) — the 0.20 citation is dead from both sides; correct the 916 B2 premise (preparation, not baseline-kind) in a follow-up edit; the outcome-bearing grid mislabel and the API drift join the audit docket; any future floor work on B refines the grid across (0.1, 0.2) and tracks the mass dependence the old grid hid"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the re-audit is at the note's own declared parameters (none alternative-named — parameter-pinned); g=0.0 unusable (gap 8e-4; reported not swept)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the reproduction spans three genuinely independent implementations with entrywise-matching operators and 9e-14 crossing agreement; the grid-artifact verdict rests on a bisected crossing, an exact algebraic cancellation, and a structurally-zero-cell census; the convention result is an exact bond-by-bond coincidence with its mechanism named; every restriction gate is against recovered cache bytes"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 916 primary + receipt (the digest authority), the frozen d=3
  memos, the axiom memo (pinned); the recovered note/runner/cache/
  witnesses via git evidence (digest-verified; commands disclosed).

### Derived

- the 22/22 reproduction across three implementations;
- the true crossing (0.1405) and the grid-artifact verdict with the
  cancellation identity and the one-event support census;
- the convention coincidence and the B2 correction;
- the parameter-dependence the grid hides;
- the eight audit rows incl. the outcome-bearing mislabel.

### Open

- the 916-record B2 follow-up edit (flagged);
- any future B-floor work (grid refinement across (0.1, 0.2); the
  mass dependence);
- the audit-lane landings (unchanged docket, now with R5/R6
  sharpened).

## Verdict

The comparator at the bottom of the lineage's most-cited number
turns out to have been measured perfectly and read wrongly: every
count reproduces to the last integer, and the threshold everyone
carried forward was never in the data — it was the first rung of a
ladder nobody looked between. The quantity the note is named for
divides out of its own criterion; the window above the floor holds
a single event; and the one number the grid could never move is the
one number everyone quoted. The lane's floor story ends where good
re-audits end: the experiment vindicated, the reading retired, and
the next grid already specified. Independent audit still required.
