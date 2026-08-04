# The bar was measured and nobody had checked: route C reproduced to eleven decimals, the boundary bracketed, the comparator note missing — Cycle 914

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane opening,
window 2; no axiom surface touched). The block set out to commission
the frozen d=3 registration-bar protocol and DISCOVERED it had
already been run — twice — with its landed conclusion sitting at
audited_conditional behind a re-audit work order nobody had
executed. This block executes it: a fully independent
re-implementation from the frozen memos' equations reproduces the
committed 2026-07-11 measurement to 1.9e-11 bits with zero
certification mismatches. The d=3 bar location stands, the lambda
boundary is bracketed with its mechanism measured, and the absent
d=1 comparator note is pinned as the lane's next recovery target.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle914_d3_bar_commission_2026_07_28.py`](../scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py)
- [`frontier_cycle914_d3_bar_independent_check_2026_07_28.py`](../scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py)

Receipt:

- [`d3_bar_commission_cycle914_receipt_2026_07_28.json`](../outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json)
- [`d3_bar_independent_check_cycle914_receipt_2026_07_28.json`](../outputs/d3_bar_independent_check_cycle914_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. It supplies the evidence the audited_conditional row's
re-audit note requests; the re-audit itself belongs to the audit lane.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). **NOT BLIND**: the worker read the
committed 2026-07-11 streams while scoping the runtime budget — this
block is an independent re-execution and reproduction test, not a
blind certification; stated here and in the receipt. The primary
exits 1 BY DESIGN (the parent-memo wiring verdict BAR-NOT-PINNED is
encoded in the exit code — the conservative reading, since the
lambda set is the parent's; the delta-memo wiring verdict is
BAR-DERIVED-EFFECTIVE). Independent audit still required.

## The discovery

Route C was not uncommissioned: the tree carries a complete
committed execution (the 2026-07-11 window-measurement runner with
five checkpoint streams and an evidence manifest), the frozen delta
memo names the earlier 2026-07-10 pilot (PR #5144), and the landed
window note's ledger row is audited_conditional with the re-audit
note "dependency_not_retained: independently audit and retain the
two frozen protocol authorities as explicit comparator premises,
then re-audit this row." This block is that work order's evidence.
Also discovered by full-tree scan: FIVE cited-but-absent
predecessors including **the d=1 comparator note itself**
(REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md) — all
pinned as absent with hard-fail-if-present guards.

## The measurement (headline delta = 0.10)

| lambda | first certified Jt | theta* | witness |
|---|---|---|---|
| 0.05 | **0.6** | 0.50075 | the disjoint five-qubit opposite pair |
| 0.10 | **0.7** | 0.50473 | the same pair |
| 0.20 | **none by Jt <= 1** | — | — |

The design's PRIMARY EXPECTED WITNESS — the five-qubit opposite
pair with no shared site or bond — is what actually fires at both
certified fields. **The lambda = 0.20 boundary mechanism is
measured, not guessed**: both single fragments clear the content
gate but their conditional dependence C = 0.060395 exceeds the 0.02
independence gate (reproducing the committed run's 0.0603948 to six
figures) — the failure is SEAM CORRELATION of the
content-certifying fragments, exactly the design's risk-signature-3
prediction, not absence of content. Boundary bracket: (0.10, 0.20).
CHECK gates: 01/02 PASS (the t=0 anchor exactly zero; the
closed-form pointer-basis panel reproducing the historical manifest
bit-for-bit); 03/04 parent wiring FAIL at lambda = 0.20 (the
measured fact that motivated the delta memo), delta wiring PASS;
05 both certified lambdas inside, bracket contiguous.

## The reproduction (the block's strongest credential)

Across all 39 shared grid rows at all three lambdas: **maximum
deviation 1.9e-11 bits, ZERO R_ind mismatches**, identical first-hit
times, subsets, persistence runs, window, and boundary bracket —
two frozen implementations written a month apart with no shared
code. The checker adds a third: its own reduction (MAX-canonical vs
the primary's MIN, different chunking, shifted-Chebyshev
propagator), agreeing to 5.1e-12 with the same window.

## The comparator row (d=3 vs d=1), honestly scoped

The surviving frozen notes supply the d=1 comparator ONLY as the
0.20 declared floor on theta (a supplied input), the structural
analogies (the excess gate; the kick-on-vacuum baseline), and the
verdict semantics. **The row: every measured d=3 theta* (~0.50)
sits ~2.5x above the d=1-derived floor — `inside` at every
certified (lambda, delta).** The frozen notes refuse further mapping
in their own words, and the note that would supply the floor's
provenance is among the absent five — so no numeric d=1 bar value
can be quoted. The recovery of that note (git history, as with the
envariance note) is the lane's next block.

## Execution discipline

The frozen design governed: preparation, Hamiltonian, lambda set,
fragment partition (re-derived by the checker from the tie-break
BYTES; all fifteen pairs verified rotation-closed onto the five
declared classes), certification criteria, C_ab formula with the
declared dephasing and tensor order, and the t=0 baseline (exactly
0.0 bits against the 1e-9 requirement). Disclosed deviations, each
with its reason: the late grid (Jt > 1.2) not executed under the
900s cap (the frozen schedule is 7.1h; the executed 13 of 17
certification-subgrid points contain the entire headline window);
the lazy-Z pair rule (skipped rows provably cannot certify); the
Lanczos ground-doublet control replaced by a stationary control (no
gate depends on it); lambda = 0.02 (delta-memo only) not run. The
exact invariant-sector reduction: 5,605,504 states — MATCHING the
memo's own figure — with Chebyshev tail bounds <= 2.8e-19 and the
full numerics panel inside frozen tolerances.

## Checker

CLAIM-SURVIVES; 8/8 teeth (including a sector-table tamper tooth:
clean 6.8e-16 vs tampered 8.3e-4). The sector-reduction exactness
claim VERIFIED against full-space dense eigendecomposition on two
reduced instances (deviations 6.8e-16 and 1.2e-15) plus 20,000
random raw-formula spot checks on the real cube (1.1e-14, with
G-invariance exactly zero). The baseline re-anchoring attack
CONFIRMS the freeze correction was necessary, not cosmetic (the
doublet alternative is unsatisfiable against the exact Holevo
ceiling), with one honest negative: the checker's capped Lanczos
doublet did not converge and is reported as non-converged, not as
support. Two findings the memo forbade assuming: the two
orthogonal-complement readings are numerically EQUAL in every row
(computed separately, |delta| <= 3e-14 — a finding, not an input);
and the seam-leakage signature is the operative failure mode.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the d=3 registration-bar measurement's audited_conditional row (the re-audit work order: independently audit and retain the frozen protocol authorities as comparator premises) — the mass lane's named successor, discovered already-run"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the re-audit evidence is supplied (independent reproduction to 1.9e-11; the frozen authorities' claims verified incl. sector exactness and the baseline anchoring) — the audit lane can now re-audit the window row; NEXT: recover the absent d=1 comparator note (git history, the envariance-note pattern) so the theta floor's provenance is citable; then the delta-memo lambda = 0.02 run and the late grid on a budget that affords them; the five absent predecessors are pinned with hard-fail guards"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the parent-memo wiring verdict is BAR-NOT-PINNED (exit 1 by design; the lambda = 0.20 absence is the measured fact behind the delta memo); the delta wiring is BAR-DERIVED-EFFECTIVE; the executed grid is the disclosed certification subset; NOT BLIND (reproduction test, stated)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the measurement executes a FROZEN pre-registered protocol with every deviation disclosed and reasoned; the reproduction spans two independent implementations at 1.9e-11 with a third (checker) at 5.1e-12; the sector-exactness and baseline claims are attacked and verified; the boundary mechanism reproduces the committed figure to six digits; the comparator row is scoped by the frozen notes' own refusals"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the three frozen D3 bar memos (the protocol authorities), the
  axiom memo, the committed 2026-07-11 streams (as reproduction
  target, disclosed), all pinned; the five absent predecessors
  pinned AS ABSENT with hard-fail guards.

### Derived

- the discovery (route C already run; the re-audit work order
  identified);
- the independent re-execution with the 1.9e-11 reproduction and
  the checker's third implementation;
- the bar locations, the boundary bracket with its measured seam
  mechanism, and the CHECK-gate outcomes under both wirings;
- the comparator row at its honest scope;
- the verified sector-exactness and baseline-anchoring claims.

### Open

- the absent d=1 comparator note's recovery (next block);
- the delta-memo lambda = 0.02 and the late grid (budget-scoped);
- the audit-lane re-audit of the window row (the work order's
  completion);
- the theta* ~ 0.50 provenance question the frozen notes themselves
  declare open.

## Verdict

The lane's celebrated successor turns out to have been measured
three weeks ago and audited by no one; asked to commission it, the
block did the better thing and checked it — from the equations, with
nothing shared but the frozen memos — and the measurement holds to
eleven decimal places, boundary mechanism and all. The d=3 bar is
where the committed run said it was, the field boundary fails
exactly the way the design predicted it might, and the one number
the comparison still needs is in a note that exists only in history.
The mass lane opens not with a new measurement but with something
rarer: an old one, finally believed for a reason. Independent audit
still required.
