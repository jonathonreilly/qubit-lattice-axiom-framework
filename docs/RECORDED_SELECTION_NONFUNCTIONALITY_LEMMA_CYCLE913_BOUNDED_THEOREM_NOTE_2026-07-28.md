# A recorded selection table, a finite non-functionality lemma, and no terminality: the Cycle-913 claims narrowed — Cycle 913

Date: 2026-08-04 (revised 2026-08-08, review loop iteration 1)

Authority: none

Audit: unset

Status: bounded worked result, SELF-CONTAINED after review. Every
quantity is an in-file stipulated table or an exact finite lemma; the
substrate the original block measured is not landed on origin/main and
is carried below as provenance context only. The original terminality
and prohibition claims are WITHDRAWN.

Claim type: bounded_theorem (conditional on the stipulated table)

Runners:

- [`frontier_cycle913_selection_function_2026_07_28.py`](../scripts/frontier_cycle913_selection_function_2026_07_28.py)
- [`frontier_cycle913_selection_independent_check_2026_07_28.py`](../scripts/frontier_cycle913_selection_independent_check_2026_07_28.py)

Receipt:

- [`selection_function_cycle913_receipt_2026_07_28.json`](../outputs/selection_function_cycle913_receipt_2026_07_28.json)
- [`selection_independent_check_cycle913_receipt_2026_07_28.json`](../outputs/selection_independent_check_cycle913_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Review record (review loop iteration 1, Sol reviewer, 2026-08-08)

The original note concluded that the occurrence-weight question
(historical lane shorthand "O3") "is TERMINAL", "has no non-forbidden
realization on this substrate", and that a cross-setup weight is an
operation the realized-state primitive "forbids verbatim"; and that
the actual-selection question (historical shorthand "O2") is
"SUPPLIED, not derivable, on this substrate". Review refuted the
promotions: the realized-state primitive
([REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md))
supplies pointwise evaluation and supplies NO averaging, measure,
weighting, or probability rule — but it does not FORBID a separately
derived or explicitly imported ensemble/setup measure, so "not
supplied by this primitive" was invalidly promoted to "not allowed by
the framework". Likewise, a finite fingerprint collision table shows
that the recorded selection is not a function of the chosen
nearest-neighbour fingerprints — it does not show that any lawful
formation rule must be such a function, so "not derivable on this
substrate" was an overclaim (history-dependent, time-dependent,
site-internal, composite, or separately supplied dynamics are all
unexcluded). The runner's certificate carrying the terminal ledger was
forced green (`cert_c6["pass"] = True`). No no-go-discipline packet
accompanied the negative. All terminal/prohibition/underivability
claims are WITHDRAWN and must not be cited as passed gates; the whole
input closure (the unlanded Cycle-863/878/911 stack) was absent from
this tree, so both runners were replaced by self-contained fail-closed
programs certifying only the bounded content below.

## Stipulated recorded table (declared scope input)

From the original full-checkout measurement, stipulated here as a
table and not asserted as certified fact about any landed substrate:
164 formation lock points; realized split 84 left / 80 right; menu
size 2 everywhere (328 site-possibility pairs); 67 lock points with no
written record event, splitting 51/16; a largest shared
nearest-neighbour-context collision class of 30 lock points splitting
15/15; 34,166 compiled gates with 0 targeting the endpoint wires.

## Result 1 — consistency arithmetic (exact)

The stipulated table is internally consistent: `84 + 80 = 164`,
`164 x 2 = 328`, `51 + 16 = 67 <= 164`, `15 + 15 = 30`, and the
recorded reads-never-writes ratio `0/34,166` is well-formed.

## Result 2 — the finite non-functionality lemma (exact, controlled)

A finite observation table containing two rows with identical
fingerprint and different outcomes is not a function of that
fingerprint. Applied to the stipulated abstract witness rows of the
recorded collision class (one shared neighbour context, two different
recorded selections), with a planted functional table correctly
recognized as functional and a 600-trial randomized soundness sweep of
the decision procedure in both directions. **Scope:** this establishes
non-membership of the recorded selection in the recorded
nearest-neighbour fingerprint rule class ON the recorded census rows.
It is NOT a statement that the selection rule is underivable, and no
such statement is made anywhere in this package.

## Provenance context (non-load-bearing)

The original block computed on the unlanded Cycle-863/878/911
substrate stack: the quadruple-read selection table, the bit-level
re-arm verification, the compile-level endpoint-target sweep, the
radius-1/2/3 fingerprint ladder, the world-95/world-51 witness pair,
and the covariance checks are recorded history from that uncertified
computation. Two useful recorded observations are retained AS HISTORY:
(i) the recorded endpoint wires were read and never written by any
compiled gate of that substrate build; (ii) the four recorded readouts
agreed row-for-row and tracked the setup event parity. If that stack
lands, those measurements can be re-run and certified in their own
package. The historical framing "the scan does not choose; it
carries" is an interpretation of that recorded history, not a theorem
of this note. The minimal-axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md), whose
Open Gates section keeps formation rules ("which admissible
possibility a new record locks, at which site, with what weight, or at
what rate") outside axiom content.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "which possibility does the recorded deterministic scan realize at each recorded lock point, and is the recorded selection a function of the recorded nearest-neighbour fingerprints? (historical lane shorthands O2/O3)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "carry the narrowed facts only: the recorded table's internal arithmetic is consistent, and the recorded selection is not represented by the recorded nearest-neighbour rule class on the recorded census; the actual-selection derivation question and the occurrence-weight question are BOTH OPEN (no terminality, no prohibition); an ensemble/setup measure remains a legitimate derive-or-import route to be costed, not a forbidden operation; substrate-scoped measurements wait on the unlanded stack landing"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "all results are conditional on the stipulated recorded table; the non-functionality result is scoped to the recorded fingerprint classes on the recorded census rows; nothing here is a substrate-global or framework-global negative; the realized-state primitive is read as supplying no measure, never as forbidding one"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite arithmetic and an exact decision procedure with planted controls in both directions and a randomized soundness sweep, replicated by the checker with a different algorithm; the recorded values are explicitly stipulated, never certified"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, stipulated definitions, open

### Stipulated definitions (declared scope inputs)

- the recorded selection table listed above;
- the abstract witness rows of the recorded collision class.

### Imports

- none. The input closure contains no repository file beyond the
  paired runner/cache pins.

### Derived (conditional on the stipulations)

- the consistency arithmetic of the recorded table;
- the finite non-functionality lemma with controls, applied to the
  recorded collision class.

### Open

- whether any lawful dynamics derives the recorded selection
  (history-dependent, time-dependent, site-internal, composite, and
  separately supplied rules are all unexcluded);
- the occurrence-weight question in full — including the legitimacy
  and cost of a derived or imported ensemble/setup measure, which the
  realized-state primitive does not supply and does not forbid;
- every substrate-scoped measurement (endpoint-target sweep, re-arm
  verification, covariance) — waiting on the unlanded stack;
- the successor-substrate proposal (endpoint content as a gate
  target) — a historical engineering suggestion, carried as context
  only.

## Verdict

What remains after review is deliberately modest: a recorded table
whose sums check, and a two-line lemma — same fingerprint, different
outcome, therefore not a function of the fingerprint — applied to the
class the recorded census actually exhibited. The larger conclusions
the original block drew from that lemma (nothing chooses, the weight
question ends here, the framework forbids the average) do not follow
from it and are withdrawn. The selection-derivation and
occurrence-weight questions stand open, with the measure route
correctly priced as an honest derive-or-import, not a violation.
Independent audit still required.
