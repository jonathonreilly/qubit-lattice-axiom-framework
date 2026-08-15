# Finite d=3 transverse-field registration comparator: low-field reproduction and four late-time rows — Cycle 915

Date: 2026-08-04

Authority: none

Audit: unset

Scope: bounded numerical support only. Nothing in this note is proposed
at retained grade, nothing here is a new theorem, and nothing here
asserts an impossibility, a decay law, or a limit.

Claim type: bounded_theorem — scoped strictly to (a) the finite
agreement between this run's `lambda = 0.02` rows and the already
committed 2026-07-11 `lambda = 0.02` stream, and (b) the four newly
evaluated late-time rows, whose only supported reading is "not
certified at these tested samples". Artifact role: support. No claim
in this note extends beyond the sampled, fixed-partition, fixed-gate
comparator under its imported cuts.

## Claim-bearing surface

The `lambda = 0.02` reproduction and the four late-time rows are finite,
sampled observations under the frozen protocol's imported cuts. They
support the already-landed four-lambda finite-window row; they establish
nothing new about it. Earlier revisions also carried Git-history
provenance about never-landed predecessor artifacts. That surface was
removed during review because those Git objects are not available in a
fresh `origin/main` clone and therefore cannot be a durable runner input.

## Protocol authorities (pinned scope inputs, landed at the pinned bytes)

- [`D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md`](D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md)
  (parent, FROZEN 2026-07-10)
- [`D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md`](D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md)
  (delta, FROZEN 2026-07-11 — its window/tolerance definitions and its
  `lambda = 0.02` commission are used)

Target row (the claim this note supports):

- [`D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md`](D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md)
  with its paired reporter
  [`d3_bar_window_measurement_2026_07_11.py`](../scripts/d3_bar_window_measurement_2026_07_11.py)

Predecessor package (landed; every Cycle 914 byte consumed here is its
landed byte):

- [`D3_BAR_REAUDIT_REPRODUCED_CYCLE914_BOUNDED_THEOREM_NOTE_2026-07-28.md`](D3_BAR_REAUDIT_REPRODUCED_CYCLE914_BOUNDED_THEOREM_NOTE_2026-07-28.md)
  with
  [`frontier_cycle914_d3_bar_commission_2026_07_28.py`](../scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py),
  [`frontier_cycle914_d3_bar_independent_check_2026_07_28.py`](../scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py)
  and
  [`d3_bar_commission_cycle914_receipt_2026_07_28.json`](../outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json)

## Landed-ancestor discipline

The predecessor package landed on `origin/main` at
`6277e4c6dfe77cf094b09a3529a69c1813773876` in FIXED form. Every pin,
every AST extraction and every restriction gate in this package
addresses those LANDED bytes, verified with `git cat-file`:

- the predecessor's numerical machinery is extracted from the landed
  primary, so this run inherits the landed, corrected operator-norm
  Chebyshev truncation bound;
- the predecessor issues NO delta-wiring completion verdict — it
  records `delta_contract_discharged: false` — and this package
  requires, consumes and re-derives nothing from any such verdict;
- the predecessor's orbit equivalence holds under the
  partition-preserving proper rotations only (4 of 24), and this
  package makes no full-closure claim;
- the predecessor's own exit code is 1 BY DESIGN (its parent-wiring
  verdict is encoded there), and this package neither reads nor needs
  that exit code;
- the axiom memo is REMOVED from both runners' input closures: it was
  context-only in the predecessor, its historical snapshot is
  superseded on `origin/main`, and no claim here consumes it.

## Runners

- [`frontier_cycle915_comparator_recovery_2026_07_28.py`](../scripts/frontier_cycle915_comparator_recovery_2026_07_28.py)
- [`frontier_cycle915_comparator_independent_check_2026_07_28.py`](../scripts/frontier_cycle915_comparator_independent_check_2026_07_28.py)

The independent checker is CLAIM-SCOPED and CO-LOAD-BEARING for this
note: the independent recomputation of every executed row, the
refutation findings and the eight mutation teeth exist only on the
checker's surface, and the checker is deliberately not imported by the
primary, so automatic import discovery cannot attach it to the audit
packet. It is declared as this note's packet helper runner in the
Status fields below, and its claim-scoped registration at landing is a
hard landing condition recorded in the Review record.

Receipt:

- [`comparator_recovery_cycle915_receipt_2026_07_28.json`](../outputs/comparator_recovery_cycle915_receipt_2026_07_28.json)
- [`comparator_independent_check_cycle915_receipt_2026_07_28.json`](../outputs/comparator_independent_check_cycle915_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). The numerical machinery is AST-extracted
from the landed predecessor primary (declared). NOT BLIND: the
committed `lambda = 0.02` stream was read while scoping the runtime
budget, so the low-field run is a reproduction test, not a blind
measurement. The primary's exit contract is machinery-only (exit 2 on a
failed pin, tolerance, determinism or falsifier gate; the certification
outcomes never move the exit code). The checker is FAIL-CLOSED: exit 0
only if every pin holds, no finding is refuted and all eight teeth
fire. Independent audit still required.

## The low-field reproduction at `lambda = 0.02` (bounded support)

On the executed subgrid (13 of the 17 certification-subgrid points),
at `lambda = 0.02`: the first SAMPLED certified time at the headline
tolerance is `Jt = 0.6`, `theta* = 0.50010`, and `R_ind = 6` — all six
declared fragments certify — persisting four consecutive samples;
every commissioned tolerance has a sampled hit by the deadline.

This reproduces the ALREADY COMMITTED 2026-07-11 `lambda = 0.02`
stream to 2.05e-12 bits with an identical `R_ind` ledger over the 13
shared rows. That is the whole of the result: a second and (through
the checker) a third implementation agree with a committed stream that
already landed as bounded measured support in
[`D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md`](D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md).
The sampled window under the imported membership predicate therefore
contains `{0.02, 0.05, 0.10}` in this comparator; the sampled bracket
above stays `(0.10, 0.20)` and no sampled field below `0.02` was
commissioned or run, so nothing is stated about fields outside the
commissioned set. One margin caveat is reported: at tolerance `0.05`
the first sampled hit sits one grid step later than the headline
(consistent with the committed stream), so membership at that
tolerance rests on a one-step sampled margin.

## The four late-time rows (bounded observation)

Four rows were evaluated that the landed predecessor did not run:
`Jt = 1.5` and `Jt = 2.0` at `lambda = 0.05` and `lambda = 0.10`. At
all four, `R_ind = 0` at every commissioned tolerance.

The supported reading is exactly one sentence: **the imported
certification predicate does not hold at these four tested samples.**
The remaining frozen late samples `Jt = 5, 10` were priced and not
executed, so they are untested; no statement is made about them, about
intermediate times, about other fields, or about the certification
predicate as a function of time.

Four further finite numbers are reported as measured context, not as
conclusions. At `Jt = 2.0` the five-qubit Holevo content is 0.6504
bits at `lambda = 0.05` and 0.6166 bits at `lambda = 0.10`, below the
loosest commissioned content cut (`0.80 x H_Z`, with `H_Z = 1.000` at
these rows), while `theta` at the same two rows is 0.4978 and 0.5119.
At `Jt = 1.5` the same `theta` is 0.0554 and 0.0768. Four points do
not establish a functional relationship between `theta` and
certification in either direction, and this note draws no such
relationship.

## The `0.20` theta convention: an unverified, unused import

The frozen `d = 3` protocol supplies `theta = 0.20` as a comparison
convention. The landed predecessor types it as an **unverified imported
comparator convention**, and this package preserves that typing exactly.
The primary emits no categorical `inside` / outside label and performs
no threshold test against `0.20`; it publishes the `theta*` values only.
Any interpretation of the convention is outside this finite-sample
result and is not a condition on the numerical observations reported
here.

## Independent checker

The paired checker recomputes ALL 13 executed low-field rows on
structurally distinct machinery (MAX-canonical orbit sector, shifted
Chebyshev propagator, expand-table marginals) and ALL FOUR executed
late-time rows, and runs six mutation teeth. Its exit contract is
fail-closed. Coverage is stated exactly: every executed row of this
package is independently recomputed; nothing is spot-sampled.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: d3_bar_window_bounded_note_2026-07-11
target_blocker_text: "the landed d=3 finite-window row's commissioned lambda = 0.02 trace and its late certification samples had not been executed by the predecessor package"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: support
next_trace_action: "The untested late samples Jt = 5, 10 remain outside this package. Whether this bounded evidence serves the target row's re-audit is the independent audit lane's decision, not this note's."
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the low-field and late-time rows execute the frozen protocol at the disclosed sampled scopes under imported cuts; the low-field rows reproduce an already-committed stream; the four late-time rows support only 'not certified at these tested samples'; the 0.20 theta convention remains an unverified import and is not used as a threshold"
hypothetical_axiom_status: null
admitted_observation_status: null
packet_helper_runner: scripts/frontier_cycle915_comparator_independent_check_2026_07_28.py
claim_type_reason: "the lambda = 0.02 agreement is triple-implemented (committed stream, primary, checker) at 2e-12 with an identical R_ind ledger; the four late-time rows are independently recomputed row by row; every claim is bounded to the sampled, fixed-partition, fixed-gate comparator and routes to the landed 2026-07-11 row as support"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (stipulated definitions and explicit scope inputs only)

Each item below is a supplied input, not a derived conclusion. None is
a framework primitive.

- the two frozen protocol memos, pinned and linked above, supplying:
  the open 3x3x3 geometry with `J = 1`; the transverse-field values
  including the commissioned `lambda = 0.02`; the Hamiltonian and the
  class-uniform preparation; the six-fragment partition and its
  tie-break; the Z pointer; the Holevo and conditional-mutual-information
  definitions; the content / excess / independence cuts
  (`0.05` / `0.02` / `0.02`); the tolerance cuts `{0.05, 0.10, 0.20}`
  and which of them is headline; the deadline `Jt <= 1`; the
  three-consecutive-sample persistence count; the drift cut `0.10`;
  the cross-field factor cut `1.5`; the `R_ind >= 2` rule; and the
  sampled first-hit selection rule. Every one of these is an IMPORTED
  DECLARED SCOPE INPUT; the per-item typing is emitted verbatim in the
  primary receipt;
- the theta comparison convention `0.20` — an UNVERIFIED IMPORTED
  COMPARATOR CONVENTION; no threshold test is performed against it and
  it does not condition any result in this package;
- the landed predecessor package (primary, checker, receipt), pinned
  at its landed bytes, supplying the numerical machinery and the
  restriction-gate targets;
- the committed 2026-07-11 `lambda = 0.02` stream, as the reproduction
  target;
- the numerical tolerances declared by this run itself (`1e-9`
  machinery tolerance, `1e-9` anchor tolerance, `1e-12` Chebyshev
  truncation-bound gate) — declared here, not imported physics.

### Derived

- the finite agreement between this run's 13 `lambda = 0.02` rows and
  the committed 2026-07-11 stream (2.05e-12 bits, identical `R_ind`
  ledger), independently reproduced by the checker;
- the four late-time rows and their single supported sentence.

### Open

- the untested late samples `Jt = 5, 10`;
- whether this bounded evidence serves the target row's re-audit
  (audit lane's decision).

## Review record (Sol review, 2026-08-08)

Iteration 1, disposition FIX_THEN_PROCEED, Audit Compatibility
BLOCKED. This revision withdraws the earlier framing of this package.
What was dropped:

- the pins of the predecessor's PRE-FIX bytes, and every consumption
  of its retired delta-wiring verdict. All pins now address the bytes
  landed at `6277e4c6dfe77cf094b09a3529a69c1813773876`, and the
  restriction gate now requires the landed package's own record that
  the delta contract is NOT discharged, and requires the retired
  verdict key to be ABSENT. The branch tree's copies of the
  predecessor's files are set to the landed bytes so the pins verify
  in this tree exactly as they verify on `origin/main` plus this
  delta;
- the invalid Chebyshev tail figure. The machinery now inherits the
  landed corrected operator-norm bound, and that bound is GATED
  (`<= 1e-12`) instead of excluded from the machinery check, so a bad
  truncation estimate can no longer pass;
- the theta-floor "is measured" upgrade, the categorical
  `inside` / below-window labels, and the raw `theta >= 0.20`
  predicate. The landed unverified-import typing is preserved, no
  threshold test is performed, and the same-baseline reconciliation is
  declared an OPEN BRIDGE;
- every negative and universal claim: the "structural NEGATIVE", the
  geometric no-go read out of never-landed text, "the certification
  DECAYS", and "theta alone does not track certification". The four
  late rows now support one sentence — not certified at these tested
  samples — and the sampled labels in the runner and receipt say only
  that. Because no negative claim remains, no N1–N8 packet is owed;
  the primary nevertheless emits the five canonical resolution lines
  in its stdout so the granularity of every statement is on the
  record;
- the promotion of never-landed predecessor content to authority. The
  recovered artifacts are quoted as text with an explicit
  no-authority annotation, and nothing in this note is derived from
  them;
- the bare workstream and attack-surface codes on live surfaces, and
  the branch/campaign fields in the ship receipt. Names are now
  domain-explicit with the old codes retained only as parenthetical
  historical aliases;
- the single-row spot check of the late-time surface. The checker now
  recomputes ALL FOUR executed late rows, and its exit contract is
  fail-closed.

The earlier framing is not a passed gate and is not citable as one. The
file name still carries the word "misattributed" from that earlier
framing; it is kept only so the claim identifier stays stable for the
audit lane, and it states nothing — the note's own title, headline and
claim scope are authoritative. The earlier provenance surface was
removed in iteration 3.

Iteration 2, disposition FIX_THEN_PROCEED, Audit Compatibility BLOCKED
on two findings. That revision:

- withdrew the residual same-baseline boundary sentences. The note's
  trace action and Open item, the primary receipt's baseline note and
  open-bridge field, and the CHECK-05 explanation no longer carry the
  universal-prohibition phrasing of iteration 1; no sentence on any
  surface of this package now states a general prohibition or
  conditions a reading on some future landing event. Each of those
  surfaces instead carries a recorded search fact (the primary runs and
  records `git grep` over the pinned tip's `docs/` and `scripts/` for a
  baseline-conversion result and reports what it returned) plus the
  scope disclosure that this package performs no threshold test and
  assigns no inside/outside label, with the conversion bridge OPEN and
  owned by the lane. Because no negative claim remains on any surface,
  no N1–N8 packet is owed;
- pinned the Git provenance. Both runners now declare
  `PINNED_PROVENANCE_TIP` in their own source and resolve every landing
  determination against that immutable commit — commit ancestry into
  the pin, and the pin's own path history — instead of against
  `origin/main`, the ref namespace or the `--all` reachable set. A
  source constant is bound by the cache envelope's runner hash, so a
  provenance answer can no longer go stale behind a fingerprint-fresh
  cache. Live-ref reads survive only as disclosed drift indicators that
  feed no verdict, gate or exit code, the checker verifies that both
  runners used the same pin, and every provenance conclusion in the
  note and both receipts is stated in as-of form. Every never-landed
  determination was re-verified against the new pin: all eight
  recovered artifacts are still outside the pinned tip's history, so
  nothing recovered there had since landed.

Iteration 3, fresh-main salvage review, removed the repository-provenance
surface entirely. Pinning the main commit used for an as-of question did
not make the recovered evidence objects durable: those objects were
reachable only from local, unlanded branch refs and were unavailable to a
fresh main-only clone. The numerical result never depended on those
objects. The landing surface now contains only the low-field reproduction,
the four late-time rows, and their independently recomputed evidence. The
review also removes the provenance and quotation execution paths from the
runner entry points and narrows the PR metadata to the same finite-sample
scope.

HARD LANDING CONDITIONS (both required in the landing set):

1. Add exactly this claim-scoped entry to
   `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
   `docs/audit/scripts/build_citation_graph.py`:

   ```python
   "comparator_recovered_theta_misattributed_cycle915_bounded_theorem_note_2026-07-28": [
       "scripts/frontier_cycle915_comparator_independent_check_2026_07_28.py",
   ],
   ```

2. The landing set must include a `docs/audit/data/citation_graph_manifest.json`
   regenerated on the landing tree (after condition 1), and the
   current-main changed-evidence gate must be run on that topology.

## Verdict

The reusable core of this package is small and honest: a committed
`lambda = 0.02` stream reproduced to twelve decimal places by two
further implementations, and four late-time rows in which the imported
certification predicate does not hold at the tested samples. The `0.20`
theta convention remains an unverified import and is not used as a
threshold. This artifact supports the landed 2026-07-11 row; it closes
nothing by itself. Independent audit still required.
