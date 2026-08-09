# Finite d=3 transverse-field registration comparator reproduction (historical alias: route C): bounded three-lambda support — Cycle 914

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded reproduction/support artifact. A fully independent
re-implementation from the frozen memos' equations reproduces three of
the four committed 2026-07-11 measurement streams to 1.9e-11 bits with
zero certification mismatches, on the fixed six-fragment partition,
the fixed frozen gates, and the sampled discrete time grid. This is
upstream support for the landed four-lambda finite-window row in
[`D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md`](D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md);
it is NOT a new theorem closure, NOT a complete re-execution of the
delta-memo contract (the commissioned `lambda = 0.02` trace was not
run), and NOT an execution of any audit-lane work order.

Claim type: bounded_theorem — scoped to the finite three-lambda
reproduction agreement itself (a bounded reproduction/support
artifact; artifact role: support). No claim in this note extends
beyond the sampled, fixed-partition, fixed-gate comparator.

Protocol authorities (pinned scope inputs, landed at the pinned bytes):

- [`D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md`](D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md)
  (parent, FROZEN 2026-07-10)
- [`D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md`](D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md)
  (delta, FROZEN 2026-07-11 — its window/tolerance definitions are used;
  its four-lambda contract is NOT discharged here)

Target row (the claim this note supports):

- [`D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md`](D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md)
  with its paired reporter
  [`d3_bar_window_measurement_2026_07_11.py`](../scripts/d3_bar_window_measurement_2026_07_11.py)
  and committed evidence in
  [`d3_bar_window_checkpoints/`](../logs/runner-cache/d3_bar_window_checkpoints/).

Runners:

- [`frontier_cycle914_d3_bar_commission_2026_07_28.py`](../scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py)
- [`frontier_cycle914_d3_bar_independent_check_2026_07_28.py`](../scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py)

The independent checker is CLAIM-SCOPED and CO-LOAD-BEARING for this
note: the third-implementation agreement (5.1e-12), the 11/11
refutation findings, the 8/8 mutation teeth, and the fail-closed exit
contract exist only on the checker's surface, and the checker is
deliberately not imported by the primary, so automatic import
discovery cannot attach it to the audit packet. It is declared as this
note's packet helper runner in the Status fields below, and its
claim-scoped registration at landing is a hard landing condition
recorded in the Review record.

Receipt:

- [`d3_bar_commission_cycle914_receipt_2026_07_28.json`](../outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json)
- [`d3_bar_independent_check_cycle914_receipt_2026_07_28.json`](../outputs/d3_bar_independent_check_cycle914_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. The target row's re-audit belongs to the audit lane and is NOT
performed or discharged by this note.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). **NOT BLIND**: the worker read the
committed 2026-07-11 streams while scoping the runtime budget — this
block is an independent re-execution and reproduction test, not a
blind certification; stated here and in the receipt. The primary
exits 1 BY DESIGN (the parent-memo wiring verdict BAR-NOT-PINNED is
encoded in the exit code — the conservative reading, since the
lambda set is the parent's; BAR-* names are protocol-internal wiring
verdicts, not scientific grades). The primary issues NO delta-wiring
completion verdict: its window summaries are three-lambda subset
summaries under the delta memo's definitions. The checker is
fail-closed: exit 0 only if every finding passes and all teeth fire.
Independent audit still required.

## The discovery (provenance)

The comparator was not uncommissioned: the tree carries a complete
committed execution (the 2026-07-11 window-measurement runner with
five checkpoint streams and an evidence manifest), and the frozen
delta memo names the earlier 2026-07-10 pilot (PR #5144). The landed
window note's ledger row carried, at drafting time, a re-audit note
requesting independent audit of the two frozen protocol authorities
as comparator premises. This note asserts nothing about that row's
current audit state — audit state is owned by the audit lane, and
whether this reproduction serves that row's re-audit is an OPEN
bridge (see Trace gate). Also discovered by full-tree scan: SIX
cited-but-absent predecessors — four notes and two runners —
including **the d=1 comparator note itself**
(REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md) — all
pinned as absent with hard-fail-if-present guards.

## The measurement (headline delta = 0.10; sampled, fixed partition, fixed gates)

| lambda | first sampled certified Jt | theta* | witness |
|---|---|---|---|
| 0.05 | **0.6** | 0.50075 | the disjoint five-qubit opposite pair |
| 0.10 | **0.7** | 0.50473 | the same pair |
| 0.20 | **no sampled hit by Jt <= 1** | — | — |

All rows are first-SAMPLED events on the discrete executed grid under
the fixed six-fragment partition and the fixed frozen gates; no
continuum-time, alternate-partition, or alternate-volume statement is
made. The design's PRIMARY EXPECTED WITNESS — the five-qubit opposite
pair with no shared site or bond — is what fires at both sampled
certified fields. The `lambda = 0.20` negative is a
**partial-narrowing**: no headline certification-subgrid hit at
`lambda = 0.20` in the supplied three-lambda, fixed-partition
comparator; the sampled `Jt = 0.7` failure is seam CMI — both single
fragments clear the content gate but their conditional dependence
C = 0.060395 exceeds the 0.02 independence gate (reproducing the
committed run's 0.0603948 to six figures), the design's
risk-signature-3 mechanism. This is a sampled in-comparator fact,
not a comparator-independent physical boundary or threshold.
Sampled boundary bracket within this comparator: (0.10, 0.20).
CHECK gates: 01 PASS (the t=0 anchor exactly zero); 02 PASS
(centered-Frobenius commutator ordering, pointer drift, and the
X-pointer demolition control — internal machinery diagnostics);
03/04 parent wiring FAIL at `lambda = 0.20` (the sampled fact that
motivated the delta memo); 03/04 window-subset summaries consistent
on the executed three-lambda subset (NO delta-wiring completion
verdict is issued — `lambda = 0.02` was not run); 05 both sampled
theta* values above the unverified imported floor, bracket
contiguous in-sample.

## The reproduction (the block's strongest credential)

Across all 39 shared grid rows at all three executed lambdas:
**maximum deviation 1.9e-11 bits, ZERO R_ind mismatches**, identical
first-sampled-hit times, subsets, persistence runs, window, and
in-sample boundary bracket — two frozen implementations written a
month apart with no shared code, on the same fixed partition and
gates. The checker adds a third: its own reduction (MAX-canonical vs
the primary's MIN, different chunking, shifted-Chebyshev propagator),
agreeing to 5.1e-12 with the same window. This reproduces three of
the four committed streams; the committed `lambda = 0.02` stream is
NOT reproduced here, so the landed four-lambda row is supported, not
independently re-executed in full.

## The comparator row (d=3 vs d=1): an unverified import, no retained inference

The surviving frozen notes supply the d=1 comparator ONLY as the
0.20 declared floor on theta — an IMPORTED value whose provenance
note (REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md) is
absent from the tree. The import is disclosed and typed in the
receipt as an unverified comparator convention. The sampled d=3
theta* values (~0.50) lie above that floor at every sampled certified
(lambda, delta); this is a disclosed numerical comparison against an
unverified import, and it supports NO retained cross-dimensional
inference. No numeric d=1 bar value can be quoted. Recovery of the
floor's provenance note (git history, as with the envariance note)
is a named open item.

## Execution discipline

The frozen design governed the supplied comparator inputs, each an
explicit declared scope input (not a framework primitive): the open
3x3x3 geometry with J=1 units; the transverse-field values; the
Hamiltonian and class-uniform +X/+Z preparation; the six-fragment
partition and its tie-break (re-derived by the checker from the
memo's BYTES); the Z pointer; the Holevo/CMI definitions and tensor
order; the content/excess/independence gates (0.05/0.02/0.02); the
deadline Jt=1; three-step persistence; drift 0.10; factor gate 1.5;
R_ind>=2; and the sampled first-hit selection rule. The fifteen
fragment pairs were verified ORBIT-EQUIVALENT under the
partition-preserving proper rotations (4 of 24; each declared class
is one connected orbit with every member reachable from its evaluated
representative — decisive in both runners). The declared partition is
NOT closed under the full proper cubic group and no such claim is
made. Disclosed deviations, each with its reason: the late grid
(Jt > 1.2) not executed under the 900s cap (the frozen schedule is
7.1h; the executed 13 of 17 certification-subgrid points contain the
entire headline window); the lazy-Z pair rule (skipped rows provably
cannot certify); the Lanczos ground-doublet control replaced by a
stationary control (no gate depends on it); `lambda = 0.02`
(delta-memo only) not run — so the delta contract is NOT discharged.
The exact invariant-sector reduction: 5,605,504 states — MATCHING the
memo's own figure — with the corrected operator-norm Chebyshev
truncation bound <= 1.33e-18 (2*sum of post-degree Bessel magnitudes
plus the deliberately skipped in-range coefficients; the earlier
"<= 2.8e-19" two-Bessel-term figure was not a bound on the omitted
series and is withdrawn) and the full numerics panel inside frozen
tolerances.

## Checker

CLAIM-SURVIVES under a fail-closed exit contract (exit 0 only if
every finding passes AND all 8 teeth fire; any refutation or failed
tooth exits 1). 8/8 teeth (including a sector-table tamper tooth:
clean 6.8e-16 vs tampered 8.3e-4). The sector-reduction exactness
claim VERIFIED against full-space dense eigendecomposition on two
reduced instances (deviations 6.8e-16 and 1.2e-15) plus 20,000
random raw-formula spot checks on the real cube (1.1e-14, with
G-invariance exactly zero). The checker also verifies that the
primary claims NO delta-contract completion. The baseline
re-anchoring attack CONFIRMS the freeze correction was necessary, not
cosmetic (the doublet alternative is unsatisfiable against the exact
Holevo ceiling), with one honest negative: the checker's capped
Lanczos doublet did not converge and is reported as non-converged,
not as support. Two findings the memo forbade assuming: the two
orthogonal-complement readings are numerically EQUAL in every row
(computed separately, |delta| <= 3e-14 — a finding, not an input);
and the seam-leakage signature is the operative sampled failure mode
in this comparator.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: d3_bar_window_bounded_note_2026-07-11
target_blocker_text: "the landed d=3 finite-window row carries a re-audit note (independently audit and retain the two frozen protocol authorities as explicit comparator premises, then re-audit the row) — owned by the audit lane, NOT executed or discharged by this note"
source_of_blocker_text: audit_ledger
reachability_to_target: supports
artifact_role: support
next_trace_action: "OPEN BRIDGE: whether this three-lambda reproduction serves the target row's re-audit is for the audit lane to decide; this note only supplies bounded reproduction evidence. NEXT: recover the absent d=1 comparator note (git history, the envariance-note pattern) so the theta floor's provenance is citable; then the delta-memo lambda = 0.02 run and the late grid on a budget that affords them; the six absent predecessors are pinned with hard-fail-if-present guards"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the parent-memo wiring verdict is BAR-NOT-PINNED (exit 1 by design; the lambda = 0.20 sampled absence is the measured fact behind the delta memo; BAR-* names are protocol-internal wiring verdicts, not scientific grades); the window summaries are THREE-LAMBDA SUBSET summaries under the delta memo's definitions — NO delta-wiring completion verdict exists; the executed grid is the disclosed certification subset; NOT BLIND (reproduction test, stated)"
hypothetical_axiom_status: null
admitted_observation_status: null
packet_helper_runner: scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py
claim_type_reason: "the run executes the FROZEN parent protocol's three-lambda set with every deviation disclosed and reasoned; the reproduction spans two independent implementations at 1.9e-11 with a third (checker) at 5.1e-12 on the same fixed comparator; the sector-exactness and baseline claims are attacked and verified; the sampled seam mechanism reproduces the committed figure to six digits; all claims are bounded to the sampled, fixed-partition, fixed-gate comparator and route to the landed row as support"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (stipulated definitions and explicit scope inputs only)

- the two frozen protocol memos (parent scout + delta), pinned and
  linked above — supplying the declared comparator inputs listed in
  Execution discipline;
- the landed window note (target row), pinned and linked above;
- the committed 2026-07-11 streams (reproduction target, disclosed);
- the theta floor 0.20 — an UNVERIFIED imported comparator
  convention (provenance note absent; typed in the receipt; no
  retained cross-dimensional inference).

### Provenance context (non-load-bearing)

- the axiom memo (docs/MINIMAL_AXIOMS_2026-06-29.md): context only in
  the predecessor and context only here; its historical snapshot
  bytes are superseded on origin/main, so it is REMOVED from both
  runners' input closures — no claim in this package consumes it;
- the six cited-but-absent predecessors (four notes, two runners),
  pinned AS ABSENT with hard-fail-if-present guards;
- the discovery narrative and PR lineage (PR #5144 pilot), cited as
  history, not as landed authority.

### Derived

- the discovery (the comparator protocol already run; provenance
  recorded above);
- the independent three-lambda re-execution with the 1.9e-11
  reproduction and the checker's third implementation;
- the sampled first-hit locations, the in-sample boundary bracket
  with its measured seam mechanism, and the CHECK-gate outcomes
  (parent wiring and three-lambda window-subset summaries);
- the comparator row at its honest scope (unverified-import
  comparison only);
- the verified sector-exactness and baseline-anchoring claims.

### Open

- the absent d=1 comparator note's recovery;
- the delta-memo `lambda = 0.02` trace and the late grid
  (budget-scoped) — required before any delta-contract or full
  four-lambda re-execution claim;
- the OPEN bridge: whether this evidence serves the target row's
  re-audit (audit lane's decision);
- the theta* ~ 0.50 provenance question the frozen notes themselves
  declare open.

## Review record (Sol review, 2026-08-08)

Iteration 1 (disposition FIX_THEN_PROCEED): this note was demoted from its original framing by the review-loop
science review (disposition FIX_THEN_PROCEED): the original note
claimed a completed re-audit work order, a delta-wiring PASS without
the commissioned `lambda = 0.02` trace, full rotation closure of the
fragment-pair partition, a bit-for-bit manifest reproduction, an
unqualified d=3 bar/boundary, and a lane-opening headline. Those
claims are withdrawn here: the negative result is a
partial-narrowing ("no headline certification-subgrid hit at
`lambda = 0.20` in the supplied three-lambda, fixed-partition
comparator; the sampled `Jt = 0.7` failure is seam CMI"), the
artifact is bounded reproduction/support for the landed four-lambda
row, and the earlier framing must not be cited as a passed gate.
The checker's exit contract was made fail-closed, and the Chebyshev
tail figure was corrected to a true operator-norm bound.

Confirmation pass iteration 2 (Sol, 2026-08-08, CONFIRMATION FAIL on
one item; fixed in this revision):

- The independent checker was absent from the restricted machine
  audit packet (it is not imported by the primary, so import
  discovery cannot see it, while the third-implementation agreement,
  the 11/11 refutation findings, the 8/8 mutation teeth, and the
  fail-closed exit contract exist only on its surface). It is now
  declared claim-scoped and co-load-bearing, with a machine-readable
  `packet_helper_runner` line in the Status fields. HARD LANDING
  CONDITION: at landing, the orchestrator must add exactly this
  claim-scoped entry to `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
  `docs/audit/scripts/build_citation_graph.py` (this branch must not
  edit audit tooling), and the current-main changed-evidence gate
  must be run on the landing topology:

  ```python
  "d3_bar_reaudit_reproduced_cycle914_bounded_theorem_note_2026-07-28": [
      "scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py",
  ],
  ```

## Verdict

Asked to commission the comparator, the block did the better thing
and checked it — from the equations, with nothing shared but the
frozen memos — and the committed three-lambda measurement holds to
eleven decimal places within its sampled, fixed-partition,
fixed-gate comparator, seam mechanism and all. The sampled bar
locations are where the committed run said they were, in-sample; the
`lambda = 0.20` sampled failure is seam CMI, as the design predicted
it might be; and the one number the d=1 comparison still needs is in
a note that exists only in history. This artifact supports the landed
2026-07-11 four-lambda row; it closes nothing by itself. Independent
audit still required.
