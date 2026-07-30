# The scale ladder that carried no novelty — a three-way adversarial exchange and the content-degeneracy verdict — Cycle 772

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded worked result (adversarially corrected; verdict
CONTENT_DEGENERATE; the sample-vs-mechanism question remains open with
its obstruction named)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle772_scope_failure_scale_2026_07_28.py`](../scripts/frontier_cycle772_scope_failure_scale_2026_07_28.py)
- [`frontier_cycle772_scale_independent_check_2026_07_28.py`](../scripts/frontier_cycle772_scale_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 766 left the question: are the E0/E1 per-scope failures sample
size or mechanism? This cycle ran the scale experiment and the
adversarial exchange corrected its own first answer — the exchange
ships as the result:

- **the primary's first verdict**: a generator-uniform ladder (1×, 4×,
  16×, 64×, 256×) under the frozen assignment left both failures
  intact — E0's Born TV 0.4005 → 0.4054 (slight worsening), E1's
  0.4250 → 0.4242 (flat) — and the frozen three-way rule returned
  MECHANISM_CONSISTENT;
- **the checker's refutation**: the duplicate-content attack found the
  ladder multiplies raw events (285,192 at 256×) while the **distinct
  selector inputs stay exactly 38 at every rung** — the scaling
  replicates complete fixture epochs (relabeled indices, identical
  content), and distinct event content saturates at 3,342 (= 3 × 1,114,
  the ordinal-residue variants of the 1× events). Zero new selector
  invocations occur anywhere on the ladder: **the trajectory's
  constancy is a duplication artifact and licenses no mechanism
  inference**;
- **the corrected verdict (v2, this package)**: the primary now
  measures content novelty at every rung and gates the rule on it —
  verdict **CONTENT_DEGENERATE** ("distinct selector inputs are
  constant across the ladder while raw events multiply; the trajectory
  carries no scaled novelty and neither the SAMPLE nor the MECHANISM
  inference is licensed on this generator at this fixture scope"),
  with the novelty-ignored reading (MECHANISM_CONSISTENT) preserved
  as printed data;
- **the checker also caught a rounding slip** in the Cycle-766 prose:
  E0's uniform TV is 175/627 ≈ 0.2791, not 0.2793 — corrected in the
  766 note and receipt on this stack;
- controls: the 1× table reproduces the 766 per-scope table exactly;
  permutation sensitivity; determinism byte-identical.

**What is actually learned**: the landed 763 generator is
content-bounded at this fixture scope — its selector input space IS
the 38 fixture epochs, and no amount of laddering enlarges it. The
sample-vs-mechanism question for E0/E1 therefore cannot be answered by
scaling this generator; it requires **genuinely new selector fixtures**
(a larger landed fixture family fed through the derived selector),
which is the named next cycle.

## Supplied / derived / open

### Supplied

- the frozen 766 assignment and comparison conventions (text/AST
  comparator, never imported); the ladder; everything the
  Cycle-317/750/763/766 packages declare.

### Derived

- the full TV trajectory (as finite generator data); the content
  novelty table (38 selector inputs constant; 1,122 → 3,342 distinct
  event contents; raw 285,192); the CONTENT_DEGENERATE verdict under
  the novelty-gated rule; the duplication mechanism (epoch replication
  with index relabeling).

### Open

- the real scale experiment (new selector fixtures — larger landed
  fixture families through the derived selector); the E0/E1
  sample-vs-mechanism question itself (still undecided, now with the
  obstruction named); the all-scope family win; the weight claim
  (untouched boundary).

## Negative-claim discipline

CONTENT_DEGENERATE is a statement about this generator at this fixture
scope, not about scaling in general; MECHANISM_CONSISTENT is printed as
the novelty-ignored reading, not asserted. No weight claim in any
branch.

## Verdict

The scale experiment answered a different question than the one it was
asked: not "sample or mechanism" but "can this generator even test
that?" — and the answer, proven by the checker's duplication census and
then built into the runner's own verdict rule, is no. The 763 ensembles
are 38 selector epochs wearing 256 costumes. The next experiment needs
new epochs, not more costumes. Independent audit still required.
