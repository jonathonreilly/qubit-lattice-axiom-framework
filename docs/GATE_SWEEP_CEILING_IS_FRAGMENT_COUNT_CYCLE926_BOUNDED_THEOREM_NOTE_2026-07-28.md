# The ceiling was the fragment count all along, and the threshold lives on a razor: the gate sweep and the separation family — Cycle 926

Date: 2026-08-05

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane hardening,
window 2b; no axiom surface touched). Cycle 919's two named
hardenings are executed, and both bite. The GATE SWEEP is exact,
not sampled: the 917 headlines are GATE-ROBUST, but the 919
located threshold is GATE-FRAGILE in the strict sense — it survives
only a 1.6e-3-bit gate band (3.92% relative half-width) and 6 of 32
persistence/deadline combinations. The SEPARATION FAMILY breaks the
four-statistics degeneracy the prior blocks disclosed, and the two
laws turn out to track DIFFERENT statistics: the redundancy ceiling
is the FRAGMENT COUNT, exactly, on all 29 geometries (the
pointer-degree reading is refuted everywhere in the swept region),
while high-field certification follows the unique conjunction
"pointer degree >= 5 AND fragment count >= 3" — one predicate out
of 990 at 100%, its two conjuncts failing through different gates.
Dated qualification edits to the 917 and 919 notes are executed
alongside this ship (the post-ship-edit pattern).

Claim type: bounded_theorem

Runners:

- [`frontier_cycle926_gate_sweep_separation_2026_07_28.py`](../scripts/frontier_cycle926_gate_sweep_separation_2026_07_28.py)
- [`frontier_cycle926_gate_sweep_independent_check_2026_07_28.py`](../scripts/frontier_cycle926_gate_sweep_independent_check_2026_07_28.py)

Receipt:

- [`gate_sweep_separation_cycle926_receipt_2026_07_28.json`](../outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json)
- [`gate_sweep_independent_check_cycle926_receipt_2026_07_28.json`](../outputs/gate_sweep_independent_check_cycle926_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Two post-ship qualification edits are executed on the
blockM4 and blockM5 branches with receipt pins refreshed.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). One disclosed implementation fix: the
917/919 anchor-building line silently drops a colliding anchor; the
frozen memo's own reading (colliding sites share a fragment) was
implemented instead, with the 24-cell/312-row exact reproduction
proving the fix is a no-op on the pinned family. Declared caps: one
planned degree-6 hub shrunk to degree-4 (estimator budget); one
control leaf hand-labelled (no claim rests on it); the deadline axis
swept only inside the executed grid. Independent audit still
required.

## Reproduction gates (all before any swept number)

21/21 frozen constants byte-verified, quote-identical to BOTH
pinned receipts; the partition rule reproduces the memo's six cube
lists; **917 AND 919 reproduced value-for-value — 12 cells and 156
rows each, maximum absolute deviation exactly 0.0** including
R_ind ledgers, witnesses, and content passes; 919's margin honesty
reproduced to the last digit (0.000783463 / 0.000832686 bits). New
capability, gated: the G6 cube rows — an unexpanded import in both
prior blocks, which would have left 2 of 26 cells unsweepable —
expand losslessly from the pinned 914 receipt's per-class tables,
gated against the pinned 914 ledger before use (the cube is still
never evolved). **All 26 cells swept, not 24.**

## Q1 — the gate sweep (exact, and the verdict is split)

The frozen protocol's only gate-dependent predicate is
C_ab <= gate, so the verdict table is piecewise constant with
breakpoints exactly at measured C_ab values — all enumerated; the
declared 65-point dense grid cross-checks the exact decomposition
with zero mismatches. Per-claim certificates (band = the gate
interval containing the frozen 0.02):

- **"The chain certifies at 0.05": GATE-ROBUST** — band
  [0.0105, 0.08] (survives a 48% gate cut); 21/32 combos.
- **"Ceiling law at 0.05": GATE-ROBUST** — band [0.0114, 0.08],
  survival 0.915, 32/32 combos.
- **"Loop cost at 0.10"**: band [0.0126, 0.0293], 32/32 combos.
- **"Threshold = degree 5": GATE-FRAGILE** — band
  **[0.0191673, 0.0207835)**, relative half-width **3.92%**,
  **6/32 combos**, 0.4% of the swept region. Just below the band
  the threshold is 6; at the upper endpoint the degree-4 G3b flips
  YES and the cut stops being clean. Fragility is localized to
  exactly two axes: the C_ab gate and the persistence count
  (persist=2 gives 3; persist=4 or 5 gives nothing). The deadline
  is robust (0.7-1.2 all give 5), and the excess-anchor and
  content-floor axes leave the threshold at 5 EVERYWHERE — the
  content side of the gate stack is not fragile at all.

The 919 note's margin honesty ("~2e-3 bits moves it") was the
right instinct; the band is now exact, and the fragility is now a
certificate rather than a caveat.

## Q2 — the separation family (the degeneracy breaks)

Eighteen new geometries. Two honest identities first: branch count
IS pointer degree by the frozen implementation's definition (an
identity, confirmed in the source bytes — never a separable law);
max degree and components carry NEITHER law (a degree-6 hub in the
environment buys nothing; a components-1 geometry still certifies).
Fragment count IS separable, through the frozen rule's own
labelling text, which is non-injective off the axial faces: the
A-family embeds the SAME K_{1,5} — identical Hamiltonian,
preparation, and evolved state — in cube coordinates where the
frozen rule yields 5, 4, 3, 2, 1 fragments at pinned pointer
degree 5. A skeptic who says "only the labels changed" is agreeing
with the finding: identical dynamics, different partition,
different verdicts. Matched pairs (fragment count, size multiset,
and n fixed; degree moved) split YES/NO at 0.10 in both the star
family and a non-star control.

## Q3 — the refined laws (different statistics; that is the headline)

- **The ceiling law**: max R_ind at the frozen low field equals
  the FRAGMENT COUNT, exactly, on all 29 geometries; the
  pointer-degree reading fits 22/29 — missing exactly the seven
  separating geometries — and survives NOWHERE in the swept region
  (0/32). Gate-robust (band [0.012, 0.08], 32/32). This composes
  cleanly with Cycle 921: on loop-free geometries every fragment
  survives the pair-cycle law, and the independence number of the
  edgeless survivor graph IS the fragment count — the two blocks'
  laws are one law seen at two tiers, with the G1 high-field drop
  remaining the one shared exception (Cycle 927's channel).
- **The threshold law**: a geometry certifies at the 0.10 field
  IFF pointer degree >= 5 AND fragment count >= 3 — the unique
  100% predicate among 990 candidates (the checker independently
  found the same single model). Neither conjunct alone survives
  anywhere. The conjuncts fail through DIFFERENT gates, with no
  exceptions: every fragment-floor failure is an INDEPENDENCE
  failure (merged anchors leave survivors too conditionally
  dependent), every degree failure at sufficient fragments is a
  PERSISTENCE failure. One law needs two statistics because two
  different gates do the killing. Carries the Q1 fragility
  qualifier verbatim. [Qualification 2026-08-05, Cycle 932: the
  d-conjunct (the persistence side) is now DERIVED — persistence
  counts frozen grid points inside a single monotone certifiable
  window, and the conjunct carries a GRID-PHASE scope: degrees
  3-4 are decided by the grid phase (windows wider than three
  samples need, opening ~0.006 after a grid point); over 401
  offsets the frozen answer (threshold 5) is the least common of
  the three possible (modal: 4). This note's persistence and
  deadline axes are re-derived from the two window edges. The
  frozen verdicts are explained, not re-graded. See the Cycle-932
  note.]
- Diagnostic-grade: the field ceiling is a single-valued function
  of the PAIR (degree, fragment count) — and of neither alone —
  across all 12 populated cells (none if f <= 1; 0.05 if f = 2;
  0.075 if f >= 3, d <= 4; 0.10 if f >= 3, d >= 5).

## The corrections executed (post-ship-edit pattern)

1. **The 917 note's prose overstated**: "the equality survives on
   every loop-free geometry" at 0.10 is false for the loop-free
   degree-2 chain (its own receipt data records max R_ind 1) — it
   holds for loop-free geometries of degree >= 3. Dated correction
   added on the blockM4 branch, pin refreshed.
2. **The 919 threshold re-scoped**: the gate-fragility certificate
   and the conjunction re-scoping added as a dated qualification on
   the blockM5 branch, pin refreshed.

## Gates, teeth, checker

Primary: 12/12 teeth fire (the planted band-edge gate value caught;
tampered partition caught; the Euler guard fires at state deviation
0.415); 16.6 s; every science number bit-identical across reruns.
Checker: 17/17 teeth, one finding, NO refutation — fully
independent machinery (sparse Pauli-kron, expm_multiply, tensordot
RDMs, bitmask max-clique, partitions re-derived from the memo
bytes, the G6 class map read from the 914 source); all 26 frozen
and 54 new cells reproduced with zero disagreements (2.6e-14 /
5.6e-14); **every quoted claim boundary confirmed tight** (holds
strictly inside, fails immediately outside); the threshold's
destinations outside the band independently reproduced; the same
single 100% model found independently. The checker's finding — the
single-statistic tie between pointer degree and branch count — is a
tie BY IDENTITY, confirming the primary's analysis. The checker
also caught and fixed four bugs in itself mid-cycle, disclosed in
its receipt; the fixes are why the boundary probes probe the strict
interior. Runtimes 16.6 s / 5.8 s.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Cycle 919's two named hardenings: the gate-robustness sweep (the ~2e-3-bit fragility) and the geometry family separating the four collapsed degree statistics"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "carry the split verdict everywhere: 917's chain-certifies and ceiling laws are GATE-ROBUST; the 919 threshold is GATE-FRAGILE (exact band [0.0191673, 0.0207835), 6/32 combos) and re-scoped to the conjunction d>=5 AND f>=3; the CEILING IS THE FRAGMENT COUNT (pointer-degree reading refuted; composes with 921's independence-number law as one law at two tiers); the (d,f) field-ceiling law is diagnostic-grade — promoting it needs claim-grade cells; named opens: the E1 single-witness dependence (f>=3 vs no-large-fragment), the persist-axis fragility, the 917/919 prose edits landed with pins refreshed"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the sweep is exact over the declared axes (gate, persistence, deadline within the executed grid, excess anchor, content floor); the (d,f) field-ceiling law and the wider probe grid are diagnostic-grade; the f>=3-vs-fragment-size distinction rests on one witness (E1) — named open; the G6 rows are expanded from pinned per-class tables, never evolved; branch count = pointer degree is an identity of the frozen implementation, not a finding"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the sweep is a complete piecewise-constant decomposition with breakpoints at measured values, cross-checked against a dense grid at zero mismatches; both prior blocks reproduce at deviation exactly zero including ledgers and witnesses; the separation family holds dynamics fixed while the frozen rule moves the partition; the unique-conjunction search is exhaustive over 990 predicates and independently reproduced; every claim boundary is verified tight from both sides"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the three frozen memos (gates and partition rule, verbatim), the
  914/917/919 primaries + receipts (the constants, anchors, and G6
  class tables), the axiom memo (pinned); the d=1 note via its git
  blob (digest-matched).

### Derived

- the exact per-claim gate-robustness certificates with tight
  boundaries;
- the gate-fragility re-grading of the 919 threshold;
- the separation family and the identity analysis
  (branch count = degree; max degree and components carry nothing);
- the fragment-count ceiling law (29/29; pointer-degree refuted);
- the unique-conjunction threshold law with its two-gate anatomy;
- the (d, f) field-ceiling function (diagnostic-grade);
- the two executed note corrections.

### Open

- the E1 single-witness dependence (a {3,2}-type split off lattice
  stars);
- the persistence-count fragility axis (persist = 3 is
  load-bearing for the threshold);
- promoting the (d, f) law to claim grade;
- the G1 high-field drop (Cycle 927, running).

## Verdict

The hardenings did what hardenings are for: one headline came back
stronger and one came back smaller, and the lane is better for
both. The chain's certificate and the ceiling law survive gate
cuts of half their size; the celebrated threshold turns out to
balance on sixteen ten-thousandths of a bit of gate and one
particular persistence count, and its true form was never a single
statistic — degree and fragment count each guard a different door,
and only geometries that pass both certify at the high field.
Deeper than either: the quantity every block since 917 called
"degree" was the fragment count wearing degree's clothes, exposed
by five geometries that share one Hamiltonian and differ only in
how the frozen rule counts their records — which folds the
ceiling, the loop law, and the separation into a single sentence
about surviving fragments. The prose that overstated is corrected
where it lives, with pins refreshed, and the razor the threshold
stands on is now measured to its exact width. Independent audit
still required.
