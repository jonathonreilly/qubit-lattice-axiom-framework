# The general-n sector theorem — structural, conditional on two named identities — Cycle 738

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem (conditional on two named,
anchor-verified identities)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle738_general_n_sector_theorem_2026_07_28.py`](../scripts/frontier_cycle738_general_n_sector_theorem_2026_07_28.py)
- [`frontier_cycle738_theorem_independent_check_2026_07_28.py`](../scripts/frontier_cycle738_theorem_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 737 proved the sector theorem exhaustively at the four admissible
rings and left the general statement as a precise conjecture. This
cycle turns it into a machine-checked **structural proof for all bank
counts `b ≥ 1`**, conditional on exactly two named identities:

- **L1 (shift structure)**: from the constructor's own algebra, the
  lawful one-step update acts on A-occupancy as the uniform `+1`
  circular shift for symbolic `n = 8b − 5` (AST-layer analysis of the
  station indexing, confirmed against all four frozen anchors);
- **L2 (distance conservation)**: rotation preserves all pairwise
  circular distances — exact symbolic argument over `Z_n` residues, so
  separated stays separated for every `n`;
- **L3 (invariant locality)**: the ownership predicate depends only on
  the `(s−1, s, s+1)` occupancy window plus own B/work — with the
  honest finding that **K itself defines no ownership predicate**: the
  predicate is the campaign's formalization (Cycle 734 lineage),
  which is why identity `I_ownership_local_formula` below is a named
  condition rather than a derived fact;
- **L4 (window transport)**: under rotation the multiset of
  occupied-station windows is transported unchanged; with L2 + L3,
  the invariant holds at step `t` iff it holds at step 0 — and step 0
  **is** separation. Clean-B transport is derived
  (`B_new[s] = B_old[s+1]`); clean-work transport is conditional on
  the second identity;
- **L5 (closure)**: after `n` steps the rotation is the identity;
  combined with the per-step register-return algebra (gate-kind
  domains of the handoff/relay/packet words verified), closure is
  exact for all `n`;
- **L6 (anchor consistency)**: every lemma specializes correctly at
  `b = 1..4` against the frozen Cycle-737 exhaustions — zero
  mismatches;
- **L7 (honesty audit)**: every reliance on a concrete constructor
  constant is enumerated. Exactly two survive as conditions:

  1. `I_ownership_local_formula` — for every `b ≥ 1` and station `s`,
     the intended ownership predicate at occupied `s` equals
     `not(A[s−1] or A[s+1] or B[s] or work[s])`; K itself defines no
     ownership predicate.
  2. `I_macro_clean_work_uniformity` — for every `b ≥ 1` and every row
     emitted by the interleaved program, the controlled mapped macro
     leaves its A control unchanged, addresses only data plus its own
     work bit, and maps clean `work = 0` back to `0`.

  Both identities are verified exhaustively at `b = 1..4` (the frozen
  anchors); their all-`b` truth is the exact remaining gap.

Theorem status: **`conditional_on_named_identities`** — for all
`b ≥ 1`, every pairwise-separated configuration runs its lawful orbit
(invariant satisfied at every occupied station of every step, all
pairwise distances conserved, exact closure after `n` steps), GIVEN the
two identities. This is a conditional theorem with machine-checked
lemmas, not a conjecture and not an unconditional claim.

## Supplied / derived / open

### Supplied

- the two named identities (anchor-verified at `b = 1..4`, assumed for
  `b ≥ 5`);
- the ownership-predicate formalization itself (the campaign's, not
  K's — stated plainly);
- everything the Cycle-737 package supplies per family member.

### Derived

- L1/L2/L4-transport/L5-closure as symbolic identities over
  `n = 8b − 5`; the L6 anchor specializations; the complete L7
  enumeration of concrete-constant reliances.

### Open

- discharging the two identities structurally (each is a uniformity
  statement about the constructor's emitted rows — plausibly provable
  by induction over the row-emission structure; the sharpest next
  step);
- W4 renewal; adjacent-pair control; everything inherited at original
  scopes; no time/Record/Born/source content is touched.

## Negative-claim discipline

No negative claim ships. "K defines no ownership predicate" is a
scope fact about the landed module, recorded verbatim from the AST
search, not a defect claim.

## Verdict

The sector theorem now has the shape mathematics wants: four exhaustive
anchors, five structural lemmas, and a gap reduced to two crisp
identities about the constructor's emitted rows. Whoever discharges
those two identities — by row-emission induction or by refutation at
some `b ≥ 5` — settles the general theorem either way. Independent
audit still required.
