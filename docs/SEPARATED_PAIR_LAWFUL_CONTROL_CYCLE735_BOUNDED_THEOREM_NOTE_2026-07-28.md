# Joint two-token templates and bare Cycle-719 transport — Cycle 735

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle735_separated_pair_lawful_control_2026_07_28.py`](../scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py)
- [`frontier_cycle735_separated_pair_independent_check_2026_07_28.py`](../scripts/frontier_cycle735_separated_pair_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, primitive,
registry, policy, queue, audit result, or audit status.

## Result

On the supplied oriented ring with 11 stations, let

\[
  p\in\mathbb Z_{11},\qquad d\in\{2,3,4,5\}.
\]

The externally parameterized joint word \(W(p,d)\) writes A bits at \(p\)
and \(p+d\), and reference bits on the positive interval
\(p+1,\ldots,p+d\). The runner establishes the following finite statements:

- all 44 words are pure-X, bit exact, and have sizes 4, 5, 6, and 7 for
  \(d=2,3,4,5\);
- the 44 words represent all unordered nonadjacent pairs on the odd
  11-cycle, and all 484 passive-translation identities hold;
- each initial joint register has A-count two and satisfies the stated
  ring-11 static charge/reference relation;
- all 242 single-entry deletions change either the A-count or that static
  relation, with 88 A deletions and 154 reference deletions;
- under the **bare Cycle-719 logical controller**, the 44 A-pair orbits
  complete 484 steps, 5,324 station checks, and 968 occupied-station checks
  with exact token return, constant pair distance, and literal reverse
  restoration; the held data output equals two applications of the
  3,106-gate `global_allocator_word(2)`.

The static reference row and the bare controller orbit are separate finite
parts of the theorem. The reference row is not transported by the bare
orbit, and this package does not identify that orbit with the Cycle-731 full
guarded word.

## Adjacent controls

The same bare Cycle-719 transport check succeeds for all 11 adjacent A-pair
positions: the tokens return and literal reversal restores the supplied data.
For this overlapping case, 0 of 11 outputs equal the nonadjacent
double-allocator reference.

Separately, the inherited Cycle-724/734 radius-one guard predicate produces
22 step-0 violation rows on those 11 adjacent inputs. This is a
predicate-specific recount only. It is not used to define a maximal
distance domain or to exclude a different guard or controller.

## Independent check

The independent runner first executes the primary in a subprocess and checks
its report contract. It then:

1. derives the template, covariance, and deletion counts with a set-valued
   enumerator; and
2. evaluates the inherited Cycle-719 gate lists with its own
   X/CNOT/Toffoli interpreter.

It does not call Cycle 719's semantic evaluator, controller-step helper, or
orbit helper. Its five certificates all pass.

## Supplied inputs

- ring size 11 and its positive orientation;
- external position \(p\) and separation \(d\);
- the joint blank logical register written by \(W(p,d)\);
- the held two-bank Cycle-719 program, program order, direction-\((1,0)\)
  data genesis, and clean A/B controller rails.

These are explicit finite fixture inputs. No application position,
separation, genesis, or physical preparation mechanism is derived here.

## Dependency boundary

The load-bearing and immediately controlling parents are:

- [Cycle 719 bare recurrent controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 724 radius-one guard](LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 728 finite charge/reference relation](BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 730 charge-row enforcement](CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 731 count/charge/neighbor guarded constructor](TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md); and
- [Cycle 734 externally positioned adjacent template and inherited guard witness](PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md).

Every parent is used only at its proposal-only, unaudited scope. Cycle 731 is
listed to make the non-composition boundary recoverable: its full guarded
word is not executed or claimed by Cycle 735. No parent supplies retained
authority or an audit promotion.

## Outside the claim

- the Cycle-731 full guarded-controller orbit;
- transport of the reference row or preservation of its charge relation
  during controller motion;
- autonomous or factorized preparation;
- physical or framework-level source interpretation;
- W4 composition or renewal;
- a maximal distance domain, controller exclusion, or adjacency no-go;
- three or more tokens, other ring sizes, dirty-register domains, or a
  uniform family.

These items remain research questions or separate construction obligations;
they are not conclusions of this note.

## Negative-claim discipline

This note makes finite positive template and bare-transport claims. The
adjacent guard recount is explicitly not an exclusion result, so the
derived-no-go and named-boundary gates are not triggered.

## Verdict

Cycle 735 supplies an externally parameterized joint two-token register
family and a bounded bare Cycle-719 transport theorem. It does not supply a
Cycle-731 guarded composition theorem, independent preparation theorem, or
physical-source bridge. Independent audit remains required.
