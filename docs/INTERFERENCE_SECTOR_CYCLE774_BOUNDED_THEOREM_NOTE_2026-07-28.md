# The interference sector is empty — additivity as a structural theorem of the landed vertex — Cycle 774

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded worked result (exhaustive census + structural
mechanism; the kernel's additivity is forced, and the weakness of the
771 test is now a theorem, not a suspicion)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle774_interference_sector_2026_07_28.py`](../scripts/frontier_cycle774_interference_sector_2026_07_28.py)
- [`frontier_cycle774_interference_independent_check_2026_07_28.py`](../scripts/frontier_cycle774_interference_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 771 verified the kernel's composite prediction but found the
test easy: the configuration was block-additive. The named decisive
question — does the landed vertex have an interference sector at all?
This cycle answers it exhaustively:

- **the census**: all coherent two-channel inputs
  (a|c₁⟩ + b|c₂⟩)/norm over every channel pair and coefficient pair
  (a,b) ∈ {(1,1),(1,−1),(1,i),(1,−i),(2,1),(1,2)} — 90 coherent states
  — plus all 15 mixture baselines: **every cross-term is identically
  zero, exactly** (no float tolerances; amplitude-product arithmetic);
- **the mechanism, from the matrix**: for source channel d, the landed
  `link_recoil_vertex` sends the branch amplitude to the unique cell
  `(REVERSE[d], d, d)` — the branch tensor indices are completely
  determined by the source label. Two different channels can never
  populate the same cell, so their amplitudes never meet: **the vertex
  preserves orthogonal source labels structurally**, and
  block-additivity holds for ALL two-channel inputs, not just the
  censused family;
- **consequence for the kernel**: the Cycle-768 kernel's additive
  extension is not an assumption that survived a test — it is the only
  behavior the landed vertex permits. Equivalently: at this surface's
  scope there is no configuration on which an additive kernel and a
  non-additive response law could disagree;
- **consequence for W7's program**: the response-law question at this
  fixture scope reduces to the defining rows plus structural
  additivity — both landed. What remains open is scope, not content:
  a genuinely interference-capable surface (e.g. the composite-input
  preparations of Cycles 720/721, absent in this worktree —
  `framework_input_status: absent` printed honestly) is where a
  response law faces a non-trivial composite test;
- controls: single-channel rows reproduce the landed defining rows;
  the mixture baseline reproduces the 771 block-additivity; sha
  anchors; the 768/771 primaries blocklisted (text-only comparator);
  determinism.

## Supplied / derived / open

### Supplied

- the declared coefficient family (six exact pairs; the census is
  exhaustive over it, and the structural mechanism covers all inputs
  beyond it); everything the Cycle-320/322/749/768/771 packages
  declare.

### Derived

- the 90 + 15 census with exact zero cross-terms; the
  `(REVERSE[d], d, d)` branch-target uniqueness and the
  label-preservation mechanism; the all-inputs block-additivity
  consequence; the honest framework-input absence.

### Open

- the interference-capable surface (framework-prepared composite
  inputs — Cycles 720/721 machinery — the named next scope for W7);
  the no-refit attachment completion at this scope; everything
  inherited.

## Negative-claim discipline

"No interference sector exists" is scoped to the landed
`link_recoil_vertex` at this fixture scope and is proven structurally
from the branch-target uniqueness, not sampled; it says nothing about
other landed surfaces or extended charts.

## Verdict

The 771 checker's complaint — the test was easy — turns out to be a
theorem about the physics: this vertex cannot make a hard test. Its
branch geometry quarantines every source channel into its own cell,
additivity is the law of the surface, and the kernel is exactly as
strong as that law allows. The composite-preparation machinery is now
the only road to a stronger response test. Independent audit still
required.
